---
title: "Working with alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: AlarmsWCCPenUS
topics: 260
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Working with alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Principles (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#principles-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Alarm Logging (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-logging-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using Alarms in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-alarms-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
- [Using Alarms in Runtime (RT Professional)](#using-alarms-in-runtime-rt-professional)
- [Displaying security events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-security-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Sending a complete alarm from the controller to the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Reference (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#reference-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Principles (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Alarm Logging in WinCC (Basic Panels)](#alarm-logging-in-wincc-basic-panels)
- [Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
- [Alarm Logging in WinCC (RT Professional)](#alarm-logging-in-wincc-rt-professional)
- [Alarm Procedures (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-procedures-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarm states (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-states-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Acknowledgement (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#acknowledgement-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarm groups (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-groups-basic-panels-panels-comfort-panels-rt-advanced)
- [Alarm groups (RT Professional)](#alarm-groups-rt-professional)
- [Alarm number (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-number-basic-panels-panels-comfort-panels-rt-advanced)
- [Alarm number (RT Professional)](#alarm-number-rt-professional)

### Alarm Logging in WinCC (Basic Panels)

#### Introduction

The alarm system allows you to display and record operating states and faults on the HMI device that are present or occur in a plant.

An alarm may have the following content:

| No. | Time | Date | Alarm text | Status | Alarm class |
| --- | --- | --- | --- | --- | --- |
| 5 | 12:50:24:590 | 24.02.2007 | Boiler pressure above high limit. | Incoming  Outgoing | Warning: Color Red |

#### Alarm system in WinCC

The alarm system processes a variety of alarm types. The alarm procedures can be broken down into system-defined alarms and user-defined alarms:

- User-defined alarms are used to monitor the plant process.
- System-defined alarms monitor the HMI device.

The detected alarm events are displayed on the HMI device. Targeted access to the alarms combined with supplementary information about individual alarms ensures that faults are localized and cleared quickly. This reduces stoppages or even prevents them altogether.

The following figure shows the alarm system structure:

![Alarm system in WinCC](images/12407218315_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the alarm types (Basic Panels)](#overview-of-the-alarm-types-basic-panels)
  
[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm number (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-number-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on alarm classes (Basic Panels)](#basics-on-alarm-classes-basic-panels)

### Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)

#### Introduction

Alarm logging allows you to display and record operating states and faults on the HMI device that are present or occur in a plant.

An alarm may have the following content:

| No. | Time of day | Date | Alarm text | Status | Alarm class |
| --- | --- | --- | --- | --- | --- |
| 5 | 12:50:24:590 | 24.02.2007 | Boiler pressure above high limit. | Incoming  Outgoing | Warning: Color Red |

#### Alarm Logging in WinCC

Alarm logging processes various alarm procedures used by the PLC and the HMI device. The alarm procedures can be broken down into system-defined alarms and user-defined alarms:

- User-defined alarms serve to monitor the plant.
- System-defined alarms are used to monitor the HMI device or the PLC.

The detected alarm events are displayed on the HMI device. You can use the alarm logging system to log alarms from the ongoing process. Targeted access to the alarms combined with supplementary information about individual alarms ensures that faults are localized and cleared quickly. This reduces stoppages or even prevents them altogether.

The types of system-defined controller alarms depend on the controller used.

The following figure shows the structure of the alarm logging system for communication with the SIMATIC S7-300/400 controllers:

![Alarm Logging in WinCC](images/88199214091_DV_resource.Stream@PNG-en-US.png)

The following figure shows the structure of the alarm logging system for communication with the SIMATIC S7-1500 controllers:

![Alarm Logging in WinCC](images/88199389195_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of the alarm types (Panels, Comfort Panels, RT Advanced)](#overview-of-the-alarm-types-panels-comfort-panels-rt-advanced)
  
[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm number (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-number-basic-panels-panels-comfort-panels-rt-advanced)

### Alarm Logging in WinCC  (RT Professional)

#### Introduction

Alarm logging allows you to display and record operating states and faults on the HMI device that are present or occur in a plant.

An alarm may have the following content:

| No. | Time of day | Date | Alarm text | Status | Alarm class |
| --- | --- | --- | --- | --- | --- |
| 5 | 12:50:24:590 | 24.02.2007 | Boiler pressure above high limit. | Incoming  Outgoing | Warning: Color Red |

#### Alarm Logging in WinCC

Alarm logging processes various alarm procedures used by the PLC and the HMI device. The alarm procedures can be broken down into system-defined alarms and user-defined alarms:

- User-defined alarms serve to monitor the plant.
- System-defined alarms are used to monitor the HMI device or the PLC.

The detected alarm events are displayed on the HMI device. You can use the alarm logging system to log alarms from the ongoing process. Targeted access to the alarms combined with supplementary information about individual alarms ensures that faults are localized and cleared quickly. This reduces stoppages or even prevents them altogether.

The types of system-defined controller alarms on the controller box used.

The following figure shows the alarm logging structure for communication with the SIMATIC S7-300/400 controllers:

![Alarm Logging in WinCC](images/88204201867_DV_resource.Stream@PNG-en-US.png)

The following figure shows the alarm logging structure for communication with the SIMATIC S7-1500 controllers:

![Alarm Logging in WinCC](images/88204266123_DV_resource.Stream@PNG-en-US.png)

#### System diagnostics with performance tags

WinCC provides the "@PRF_ALGRT_..." system tags to analyze the alarm system.

You use them to evaluate the time response of the server. You can also view this performance evaluation in the Windows system monitor.

Performance tags with the names "@PRF_ALGRT_CHNCON_&lt;connection name&gt;_..." are created for the connections in use.

> **Note**
>
> **Connection-specific performance tags**
>
> When a connection is configured, performance tags are created in the database with the names "@PRF_ALGRT_CHNCON_&lt;connection name&gt;_...".
>
> These tags are not visible in the "System tags" tab, but can be used just like any other performance tag.
>
> When you link the connection-specific performance tags to objects, the tag assignment will have a red background in the engineering system. However, access in Runtime still works.

---

**See also**

[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)
  
[Alarm number (RT Professional)](#alarm-number-rt-professional)
  
[Checking connections with performance tags (RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#checking-connections-with-performance-tags-rt-professional)
  
[System diagnostics with performance tags (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#system-diagnostics-with-performance-tags-rt-professional)
  
[Overview of performance tags (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#overview-of-performance-tags-rt-professional)

### Alarm Procedures (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of the alarm types (Basic Panels)](#overview-of-the-alarm-types-basic-panels)
- [Overview of the alarm types (Panels, Comfort Panels, RT Advanced)](#overview-of-the-alarm-types-panels-comfort-panels-rt-advanced)
- [Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)
- [Custom alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#custom-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [System-defined alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-defined-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of the alarm types  (Basic Panels)

##### Introduction

The alarm types serve various purposes for monitoring the plant. The alarms from the individual alarm types are configured and triggered in different ways.

Select the relevant tab in the "HMI alarms" editor to configure alarms based on the individual alarm types.

##### Alarm types in WinCC

WinCC supports the following alarm types:

##### User-defined alarms

- **Analog alarms**

  - Analog alarms are used to monitor limit violations.
- **Discrete alarms**

  - Discrete alarms are used to monitor states.

##### System-defined alarms

- **System events**

  - System events belong to the HMI device and are imported into the project.
  - System events monitor the HMI device.

---

**See also**

[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[System events (Basic Panels)](#system-events-basic-panels)
  
[Alarm Logging in WinCC (Basic Panels)](#alarm-logging-in-wincc-basic-panels)

#### Overview of the alarm types (Panels, Comfort Panels, RT Advanced)

##### Introduction

The alarm types serve various purposes for monitoring the plant. The alarms from the individual alarm types are configured and triggered in different ways.

Select the relevant tab in the "HMI alarms" editor to configure alarms based on the individual alarm types.

##### Alarm types in WinCC

WinCC supports the following alarm types:

##### User-defined alarms

- **Analog alarms**

  - Analog alarms are used to monitor limit violations.
- **Discrete alarms**

  - Discrete alarms are used to monitor states.
- **Controller alarms**

  - You configure controller alarms in STEP 7.
  - You continue to process the controller alarms in WinCC.

    > **Note**
    >
    > **Device dependency**
    >
    > The controller alarm is not supported on all HMI devices.

##### System-defined alarms

- **System-defined controller alarms**

  - System-defined controller alarms consist of diagnostic alarms (SIMATIC S7) and system errors (RSE)
  - System-defined controller alarms are used to monitor the PLC.

    > **Note**
    >
    > **Device dependency**
    >
    > System-defined controller alarms are not supported on all HMI devices.
- **System events**

  - System events belong to the HMI device and are imported into the project.
  - System events monitor the HMI device.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[System-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#system-defined-controller-alarms-panels-comfort-panels-rt-advanced)
  
[System events (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of the alarm types (RT Professional)

##### Introduction

The alarm types serve various purposes for monitoring the plant. The alarms from the individual alarm types are configured and triggered in different ways.

Select the relevant tab in the "HMI alarms" editor to configure alarms based on the individual alarm types.

##### Alarm types in WinCC

WinCC supports the following alarm types:

##### User-defined alarms

- **Analog alarms**

  - Analog alarms are used to monitor limit violations.
- **Discrete alarms**

  - Discrete alarms are used to monitor states.
- **User alarms**

  - User alarms serve to monitor operator input.
  - User alarms are triggered by means of alarm number and can be also used in scripts in Runtime.
- **Controller alarms**

  - You configure controller alarms in STEP 7.
  - You continue to process the controller alarms in WinCC.

    > **Note**
    >
    > **Device dependency**
    >
    > Controller alarms and user alarms are not supported on all HMI devices.

##### System-defined alarms

- **System-defined controller alarms**

  - System-defined controller alarms are used to monitor the PLC.
  - Diagnostics alarms (SIMATIC S7) and system errors (RSE) also belong to the category of system-defined controller alarms.

    > **Note**
    >
    > **Device dependency**
    >
    > System-defined controller alarms are not supported on all HMI devices.
- **System events**

  - System events belong to the HMI device and are imported into the project.
  - System events monitor the HMI device.

---

**See also**

[Alarm Logging in WinCC (RT Professional)](#alarm-logging-in-wincc-rt-professional)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User alarms (RT Professional)](#user-alarms-rt-professional)
  
[Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[System-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#system-defined-controller-alarms-panels-comfort-panels-rt-advanced)
  
[System events (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-panels-comfort-panels-rt-advanced-rt-professional)

#### Custom alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
- [User alarms (RT Professional)](#user-alarms-rt-professional)

##### Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Description

Analog alarms signal limit violations during the process.

###### Example

The speed of the mixer in a fruit juice mixing plant must not be too high or too low. You can configure analog alarms to monitor the speed of the mixer. If the high or low limit for the speed of the mixer is violated, an alarm is output on the HMI device containing the following alarm text, for example: "Mixer speed is too low".

---

**See also**

[Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional-1)
  
[Configuring Analog Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-analog-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User alarms (RT Professional)](#user-alarms-rt-professional)
  
[Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)
  
[Overview of the alarm types (Panels, Comfort Panels, RT Advanced)](#overview-of-the-alarm-types-panels-comfort-panels-rt-advanced)
  
[Overview of the alarm types (Basic Panels)](#overview-of-the-alarm-types-basic-panels)

##### Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Description

Discrete alarms indicate a status in the current process.

###### Example

A fruit juice mixing plant consists of several tanks containing the ingredients. To ensure the correct mixing ratio of water, fruit concentrate, sugar, and flavoring, the valves in the intakes open and close at the right moment. This operation should be monitored.

You configure a suitable discrete alarm for all the valve states. If a valve on one of the four tanks opens or closes, an alarm is displayed, such as "Water valve closed".

The operator can thus monitor whether the plant is producing correctly.

---

**See also**

[Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring discrete alarms (RT Professional)](#configuring-discrete-alarms-rt-professional-1)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User alarms (RT Professional)](#user-alarms-rt-professional)
  
[Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of the alarm types (Panels, Comfort Panels, RT Advanced)](#overview-of-the-alarm-types-panels-comfort-panels-rt-advanced)
  
[Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)
  
[Overview of the alarm types (Basic Panels)](#overview-of-the-alarm-types-basic-panels)

##### Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Example of an alarm

CPU operating mode switch to Stop

###### Description

The configuration engineer creates a custom controller alarm in STEP 7. The PLC status values, such as time stamp and process values, are mapped in the controller alarm. If controller alarms are configured in STEP 7, accept them into the integrated WinCC operation as soon as a connection is established to the PLC.

> **Note**
>
> **Automatic update of new or modified controller alarms on the HMI device**
>
> When controller alarms are configured in STEP 7 and a connection to an S7-1500 controller with firmware version 2.0 (or later) is established, the controller alarms are sent to the HMI devices of device version V14. After changes of the controller alarms, the HMI device configuration must no longer be transferred.

In STEP 7, the controller alarm is assigned to an alarm class. You can import this alarm class with the controller alarm as a common alarm class.

###### Types of controller alarms

SIMATIC S7 supports different types of controller alarms. WinCC supports different types of controller alarms according to which Runtime is used.

###### Controller alarms for multiple HMI devices

If a PLC is connected to multiple HMI devices, the project engineer assigns display classes to the controller alarms in STEP7. The display classes determine the allocation to the HMI device. You can activate the display classes for your HMI device that are to be displayed on it. In this case, only the controller alarms from this display class will be displayed on the HMI device. Up to 17 display classes are possible.

---

**See also**

[Sending a complete alarm from the controller to the HMI device and automatic update (RT Professional)](#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-rt-professional)
  
[Editing controller alarms (Panels, Comfort Panels, RT Advanced)](#editing-controller-alarms-panels-comfort-panels-rt-advanced)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User alarms (RT Professional)](#user-alarms-rt-professional)
  
[Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)
  
[Overview of the alarm types (Panels, Comfort Panels, RT Advanced)](#overview-of-the-alarm-types-panels-comfort-panels-rt-advanced)

##### User alarms (RT Professional)

###### Description

User alarms indicate operator actions in Runtime. You can also configure user alarms in Runtime scripts for user-defined applications.

###### Example

An alarm of alarm class "Errors" is displayed on the HMI device of a plant. The operator eliminates this error in the plant and acknowledges the alarm in the alarm view of the HMI device. To monitor by whom and when the error was cleared, assign a user alarm to the appropriate button of the alarm view. The alarm contains the following information, for example:

- Type and content of the acknowledged alarm
- Time of acknowledgment
- Operator
- Date

---

**See also**

[Configuring user alarms (RT Professional)](#configuring-user-alarms-rt-professional-1)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)

#### System-defined alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [System events (Basic Panels)](#system-events-basic-panels)
- [System events (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-panels-comfort-panels-rt-advanced-rt-professional)
- [System-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#system-defined-controller-alarms-panels-comfort-panels-rt-advanced)

##### System events (Basic Panels)

###### Examples for alarms

- "An online connection to the PLC is established."

###### Description

A system alarm indicates the status of the system, plus communication errors between the HMI device and system.

Under "Runtime settings &gt; Alarms" you specify how long a system alarm is shown on the HMI device.

###### Support

The reference contains a list of the possible system events, along with the cause and possible remedies. If you contact online support because of a system alarm on the HMI device, you will need the alarm number and tags used in the system alarm.

---

**See also**

[Overview of the alarm types (Basic Panels)](#overview-of-the-alarm-types-basic-panels)
  
[Reference (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#reference-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[System events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### System events (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Examples of alarms

- "Overflow of the buffer for printing lines in text mode"
- "No printer is installed or a default printer has not been set up."

###### Description

A system event indicates the system status, including errors in the communication between the HMI device and system.

The system events depend on the HMI device.

You can load system events in the "HMI alarms" editor from a an *.xml file.

###### Support

The reference contains a list of the possible system events, along with the cause and possible remedies. When contacting Online Support because of a system event on the HMI device, you need the event number and tags used in the system event.

---

**See also**

[System events (RT Professional)](#system-events-rt-professional-1)
  
[Editing system events (Panels, Comfort Panels, RT Advanced)](#editing-system-events-panels-comfort-panels-rt-advanced)
  
[Editing system events (RT Professional)](#editing-system-events-rt-professional)
  
[System-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#system-defined-controller-alarms-panels-comfort-panels-rt-advanced)
  
[Overview of the alarm types (Panels, Comfort Panels, RT Advanced)](#overview-of-the-alarm-types-panels-comfort-panels-rt-advanced)
  
[Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)
  
[Reference (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#reference-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[System events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### System-defined controller alarms (Panels, Comfort Panels, RT Advanced)

###### Example of an alarm

Valve open due to overpressure

###### Description

System-defined controller alarms are installed with STEP 7 and are only available if WinCC is operated in the STEP 7 environment.

WinCC processes system-defined controller alarms of the type "SIMATIC S7 diagnostic alarm".

S7 diagnostic alarms show states and events in the SIMATIC S7 controllers. You only have read access to S7 diagnostic alarms.

- The system assigns the alarms to the "Diagnostics" alarm class.
- The available properties of the alarm, for example, the number of the alarm group, are accepted without changes.
- S7 diagnostic alarms are not acknowledged or reported. They are for signaling purposes only.

---

**See also**

[Enabling system-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#enabling-system-defined-controller-alarms-panels-comfort-panels-rt-advanced)
  
[System events (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)

### Alarm states  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

An alarm assumes various alarm states in Runtime. The user analyzes and reports on the process execution with reference to the alarm states.

> **Note**
>
> Device dependency
>
> Reporting and logging are not available for all HMI devices.

#### Description

Every alarm has an alarm status. The alarm states are made up of the following events:

- **Incoming**

  The condition for triggering an alarm is fulfilled. The alarm is displayed, such as "Boiler pressure too high".
- **Outgoing**

  The condition for triggering an alarm is no longer fulfilled. The alarm is no longer displayed as the boiler was vented.
- **Acknowledge**

  The operator acknowledges the alarm.

#### Alarms without acknowledgment

The following table shows the alarm states for alarms that do not have to be acknowledged:

| Status | Description |
| --- | --- |
| Incoming | The condition for an alarm is fulfilled. |
| Outgoing | The condition for an alarm is no longer fulfilled. |

#### Alarms with acknowledgment

The following table shows the alarm states for alarms that have to be acknowledged:

| Status | Description |
| --- | --- |
| Incoming | The condition for an alarm is fulfilled |
| Outgoing, not acknowledged | The condition for an alarm is no longer fulfilled. The operator has not acknowledged the alarm. |
| Outgoing, and subsequently acknowledged | The condition for an alarm is no longer fulfilled. The operator has acknowledged the alarm after this time. |
| Incoming,  acknowledged | The condition for an alarm is fulfilled. The operator has acknowledged the alarm. |
| Outgoing, but acknowledged first | The condition for an alarm is no longer fulfilled. The operator acknowledged the alarm while the condition was still fulfilled. |

Each occurrence of these states can be displayed and logged on the HMI device and a protocol printed.

> **Note**
>
> The display text for the states of an alarm is language-specific and configuration-specific.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on alarm classes (Basic Panels)](#basics-on-alarm-classes-basic-panels)
- [Basics on alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
- [Predefined alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#predefined-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics on alarm classes (Basic Panels)

##### Introduction

Many alarms occur in a plant. These are all of different importance. You can assign the alarms of your project to alarm classes to clearly show the user which of the alarms are most important.

##### Description

The alarm class defines how an alarm is displayed. The alarm class specifies if and how the user has to acknowledge alarms of this alarm class.

A new alarm class with mandatory acknowledgment is generated in WinCC.

> **Note**
>
> The choice of display modes for alarm classes depends on the options on your HMI device.

##### Examples of how to use alarm classes

- The alarm "Speed of fan 1 in upper tolerance range" has alarm class "Warnings". The alarm is displayed with a white background. The alarm does not have to be acknowledged.
- The alarm "Speed of fan 2 has exceeded upper warning range" is assigned to the "Errors" alarm class. The alarm is displayed with a red background and flashes at high frequency in runtime. The alarm is displayed until the user acknowledges it.

##### Using alarm classes

Use the following alarm classes to define the state machines and appearance of alarms for your project:

- Predefined alarm classes

  You cannot delete predefined alarm classes and edit them only to a limited extent. Predefined alarm classes have been created for each HMI device under "HMI alarms &gt; Alarm classes".
- Custom alarm classes

  You can create new alarm classes under "HMI alarms &gt; Alarm classes", configure how you want the alarms to be displayed, and define an acknowledgment model for alarms of this alarm class. The possible number of user-defined alarm classes depends on the Runtime used in your project.

> **Note**
>
> **Alarm classes from STEP 7**
>
> If an HMI device is connected to the controller, alarm classes from STEP 7 will also be displayed in WinCC.
>
> Display of system-defined controller alarms (configured in STEP 7) is not supported by Basic Panels. You can find additional information on the topic of "Controller alarms" and "Alarm logging" under [Alarm Logging in WinCC](#alarm-logging-in-wincc-basic-panels).

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)
  
[Predefined alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#predefined-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Using common alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#using-common-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm Logging in WinCC (Basic Panels)](#alarm-logging-in-wincc-basic-panels)

#### Basics on alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Many alarms occur in a plant. These are all of different importance. You can assign the alarms of your project to alarm classes to clearly show the user which of the alarms are most important.

##### Description

The alarm class defines how an alarm is displayed. The alarm class specifies if and how the user has to acknowledge alarms of this alarm class.

A new alarm class with mandatory acknowledgment is generated in WinCC.

> **Note**
>
> The choice of display modes for alarm classes depends on the options on your HMI device.

##### Examples of how to use alarm classes

- The alarm "Speed of fan 1 in upper tolerance range" has alarm class "Warnings". The alarm is displayed with a white background. The alarm does not have to be acknowledged.
- The alarm "Speed of fan 2 has exceeded upper warning range" is assigned to the "Errors" alarm class. The alarm is displayed with a red background and flashes at high frequency in runtime. The alarm is displayed until the user acknowledges it.

##### Using alarm classes

Use the following alarm classes to define the state machines and appearance of alarms for your project:

- Predefined alarm classes

  You cannot delete predefined alarm classes and edit them only to a limited extent. Predefined alarm classes have been created for each HMI device under "HMI alarms &gt; Alarm classes".
- Custom alarm classes

  You can create new alarm classes under "HMI alarms &gt; Alarm classes", configure how you want the alarms to be displayed, and define an acknowledgment model for alarms of this alarm class. The possible number of custom alarm classes depends on which runtime is used in your project.
- Common alarm classes

  Common alarm classes are displayed under "Common data &gt; Alarm classes" in the project tree and can be used for the alarms of an HMI device. Common alarm classes originate in the STEP 7 alarm configuration. If required, create additional common alarm classes in WinCC.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)
  
[Predefined alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#predefined-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Using common alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#using-common-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)

#### Predefined alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Predefined alarm classes

The following alarm classes already created in WinCC for every HMI device:

##### Alarm classes for user-defined alarms

- "Warnings"

  The "Warnings" alarm class is designed to show irregular statuses and routines in the process. Users do not acknowledge alarms from this alarm class.
- "Errors"

  The "Errors" alarm class is intended to show critical or dangerous states or limit violations in the process. The user must acknowledge alarms from this alarm class.

##### Alarm classes for system-defined alarms

- "System"

  The "System" alarm class contains alarms that display states of the HMI device and the PLCs. Alarms of the "System" alarm class belong to the system alarms.
- "Diagnosis Events"

  The "Diagnosis Events" alarm class contains alarms that display states and events in SIMATIC S7 controllers. Users do not acknowledge alarms from this alarm class.

  > **Note**
  >
  > **Device dependency**
  >
  > The "Diagnosis Events" alarm class is not available for all HMI devices.
- "Safety Warnings"

  The "Safety Warnings" alarm class contains alarms for fail-safe operation. Users do not acknowledge alarms from this alarm class. Alarms of the "Safety Warnings" alarm class belong to the system alarms.

  > **Note**
  >
  > **Device dependency**
  >
  > The "Safety Warnings" alarm class is not available for all HMI devices.

##### Priority of alarm classes on Comfort Panels and in RT Advanced

The following table shows the priority of alarm classes:

| Alarm class | Priority |
| --- | --- |
| Errors | 12 |
| Warnings | 4 |
| System | 16 |
| Diagnosis Events | 12 |
| Alarm with single acknowledgment | 12 |
| Alarm without acknowledgment | 4 |

If you filter the alarm view by priority, the alarm with priority "0" will appear at the top.

> **Note**
>
> If you configure the priority for the user-defined alarm classes, the priority is only adopted for controller alarms. For the other alarms, the priority is overwritten by the engineering system.

---

**See also**

[Basics on alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)
  
[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Using common alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#using-common-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on alarm classes (Basic Panels)](#basics-on-alarm-classes-basic-panels)

### Acknowledgement (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Acknowledging alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#acknowledging-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Acknowledgment model (Basic Panels, Panels, Comfort Panels, RT Advanced)](#acknowledgment-model-basic-panels-panels-comfort-panels-rt-advanced)
- [Acknowledgment model (RT Professional)](#acknowledgment-model-rt-professional)

#### Acknowledging alarms  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To make sure that an alarm was noticed by the plant operator, configure this alarm so that it is displayed until acknowledged by the operator. Alarms that indicate critical or hazardous states in the process have to be acknowledged.

##### Description

The acknowledgment of an alarm is an event that is logged and reported. Acknowledging an alarm changes the alarm status from "Incoming" to "Acknowledged". When the operator acknowledges an alarm, the operator confirms that he or she has processed the status that triggered the alarm.

> **Note**
>
> **HMI device dependency**
>
> Reporting and logging are not available for all HMI devices.

##### Triggering acknowledgment of an alarm

In Runtime, you trigger alarm acknowledgments in various ways:

- Acknowledgment by the authorized user at the HMI device
- Automatic acknowledgment by the system without operator action, e.g. by means of

  - Tags
  - PLC
  - System functions in function lists or scripts

    > **Note**
    >
    > **HMI device dependency**
    >
    > Scripts are not available for all HMI devices.

##### Acknowledging alarms that belong together

To make the alarm system clearer and easier to use in Runtime, you can configure an alarm group. You can acknowledge all alarms belonging to this alarm group in a single pass.

##### Acknowledgment by the PLC

Discrete alarms will be automatically acknowledged by the PLC, if necessary. The acknowledgment is triggered by a bit in the "Acknowledgment tag PLC". You define the bit and tag at the configuration stage.

##### Acknowledgment of an alarm on the HMI device

In Runtime, the user acknowledges an alarm in one of the following ways, depending on the configuration:

- Using the acknowledgment button &lt;ACK&gt; on the HMI device
- Using the button in the alarm view
- Using configured function keys or buttons in screens

  > **Note**
  >
  > **Acknowledgment button &lt;ACK&gt; on the HMI device**
  >
  > To ensure that critical alarms are processed only by authorized users, protect the "ACK" button on the HMI devices, including the operating controls and display objects of the alarms. Use the appropriate operator authorization for this.

  > **Note**
  >
  > **HMI device dependency**
  >
  > The acknowledgment key &lt;ACK&gt; is not available on all HMI devices.

##### Reaction to the acknowledgment of alarms of an alarm group

- Alarm acknowledgment by the operator  
  You acknowledge the alarm of an alarm group, for example, using the &lt;ACK&gt; acknowledgment key or a function key. All alarms of the alarm group are acknowledged.
- Alarm acknowledgment by the controller  
  The controller sets a tag bit to acknowledge the alarm of an alarm group.  
  The respective alarm is acknowledged.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Acknowledgment model (Basic Panels, Panels, Comfort Panels, RT Advanced)](#acknowledgment-model-basic-panels-panels-comfort-panels-rt-advanced)
  
[Acknowledgment model (RT Professional)](#acknowledgment-model-rt-professional)
  
[Configuring acknowledgment (RT Professional)](#configuring-acknowledgment-rt-professional)
  
[Configuring acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-acknowledgment-basic-panels-panels-comfort-panels-rt-advanced)

#### Acknowledgment model  (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Overview

You define the state machines for an alarm class. Alarms that are assigned to this alarm class will be acknowledged on the basis of these state machines. The following state machines are used in WinCC:

- Alarm without acknowledgment

  This alarm comes and goes without having to be acknowledged. There is no visible response from the system.
- Alarm with single-mode acknowledgment

  This alarm must be acknowledged as soon as the event that triggers the alarm occurs. The alarm remains pending until it is acknowledged.

---

**See also**

[Acknowledging alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#acknowledging-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-acknowledgment-basic-panels-panels-comfort-panels-rt-advanced)

#### Acknowledgment model (RT Professional)

##### Overview

You define the state machines for an alarm class. Alarms that are assigned to this alarm class will be acknowledged on the basis of these state machines. The following state machines are used in WinCC:

- Alarm without acknowledgment

  This alarm comes and goes without having to be acknowledged. There is no visible response from the system.
- Alarm with single-mode acknowledgment

  This alarm must be acknowledged as soon as the event that triggers the alarm occurs. The alarm remains pending until it is acknowledged.
- Alarm with dual-mode acknowledgment

  The alarm requires one acknowledgment as soon as the event that triggers the alarm has occurred, and a second acknowledgment when the event that triggers the alarm is no longer present. The alarm remains pending until it is acknowledged.
- Alarm without "outgoing" status with acknowledgment

  This alarm is displayed in the alarm view until it is acknowledged. It then disappears from the alarm view. The alarm is only logged.
- Alarm without "outgoing" status without acknowledgment

  This alarm is displayed, and goes out when the event that triggered the alarm is no longer present. The alarm is not added to the alarm view. The alarm is only logged.
- First value alarm with flashing and single-mode acknowledgment

  The first value alarm is a form of alarm processing in which the first alarm in a list of alarms to undergo a status change since the last acknowledgment is highlighted. Only the first alarm in this alarm class is displayed flashing in the alarm window.
- New value alarm with flashing and single-mode acknowledgment

  The new value alarm is a form of alarm processing in which any alarms from a list of alarms that have undergone a state change since the last acknowledgment are highlighted.
- New value alarm with flashing and dual-mode acknowledgment

  The alarm flashes if the value being monitored has changed. You acknowledge this alarm incoming and outgoing.

##### Overview of the state machines for multiple alarms

- Group Acknowledgment/Single Acknowledgment of Alarms in the Alarm View

  The alarm view has a ![Overview of the state machines for multiple alarms](images/21866163339_DV_resource.Stream@PNG-de-DE.png) "Group acknowledgment" button . This button triggers the acknowledgment of all visible alarms that require acknowledgment and are pending in the alarm view. If the "Single acknowledgment" option is enabled for an alarm, you cannot use the group acknowledgment function and must acknowledge the alarm separately using the ![Overview of the state machines for multiple alarms](images/21865909259_DV_resource.Stream@PNG-de-DE.png) button.
- Acknowledging Alarms in Alarm Groups

  If an alarm group is assigned an acknowledgment tag, use this tag in Runtime for a group acknowledgment of all alarms of this alarm group. You can configure suitable buttons or function keys for using this tag.

##### Central alarm state machine

You can configure the acknowledgment of the alarm annunciator in the following ways:

- You acknowledge the alarm annunciator alongside with the alarm that triggered it.
- To acknowledge the alarm annunciator, use a separate button in the alarm view.
- A specified tag is used to control the alarm annunciator.

##### Emergency acknowledgment

In exceptional circumstances, you can acknowledge an alarm with reference to its alarm number. The acknowledgment bit is sent to the AS even if the alarm is currently not pending.

For this reason, the function should only be used in extreme emergency situations.

---

**See also**

[Acknowledging alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#acknowledging-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring acknowledgment (RT Professional)](#configuring-acknowledgment-rt-professional)

### Alarm groups (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

Many alarms from different areas and processes occur in a plant. You can compile associated alarms into alarm groups.

#### Alarm groups

You can use the alarm groups to monitor the parts of the plant and to acknowledge the associated alarms together as required.

Alarm groups can contain alarms from different alarm classes. You only assign alarms that require acknowledgment to alarm groups.

#### Using alarm groups

It is a good idea to compile alarm groups for alarms such as the following:

- Alarms that are caused by the same fault.
- Alarms of the same type
- Alarms from a machine unit, such as "Fault in drive XY"
- Alarms from an associated part of the process, such as "Fault in cooling water supply"

#### Display in Runtime

In Runtime, the "Alarm group" column displays the number of the alarm group to which the alarm belongs.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Configuring alarm groups (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-alarm-groups-basic-panels-panels-comfort-panels-rt-advanced)

### Alarm groups (RT Professional)

This section contains information on the following topics:

- [Alarm Group Basics (RT Professional)](#alarm-group-basics-rt-professional)
- [Hierarchical alarm groups (RT Professional)](#hierarchical-alarm-groups-rt-professional)
- [Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)

#### Alarm Group Basics (RT Professional)

##### Introduction

Many alarms from different areas and processes occur in a plant. You use alarm groups to clearly represent the states of the plant areas on the HMI device, and to make the alarm system for your project easy to operate.

##### Description

An alarm group is a compilation of single alarms. An alarm group has several tags that address a specific property of the it alarms contains. You define the tags and their bits for a group. To display an alarm group on the HMI device, configure its visualization individually via the alarm group's status tag.

##### Application

You can use alarm groups for the following purposes, for example:

- To compile alarms that were caused by the same fault,

  such as "power failure"
- To compile alarms of the same type,

  such as "fuse blown"
- To sort and monitor alarms from a machine unit

  such as "fault in drive XY"
- Alarms from an associated part of the process

  such as "fault in cooling water supply"
- To process a group of all alarms from a plant area, such as:

  - Acknowledging alarms
  - Locking alarms
  - Suppressing alarm displays
- To visualize the status of plant areas
- To connect plant processes with the acknowledgment of alarms

##### Alarm Groups in WinCC

In WinCC, you work with two types of alarm group:

- Custom alarm groups

  You create custom alarm groups as required. These contain alarms that must be acknowledged, as well as sublevel alarm groups. You can create a hierarchy of custom alarm groups that contains up to five subgroups.

  You create user-defined alarm groups in WinCC under "HMI alarms &gt; Alarm groups &gt; Alarm groups".
- Alarm groups from alarm classes / class groups

  An alarm group is already created for each predefined alarm class. When you create a new alarm class, an alarm group is created with the same name. All the alarms from this alarm class will also be contained in the alarm group from the alarm class. Any changes to the alarm class configuration will be transferred to the "Alarm Groups" tab. The configuration for the corresponding alarm group will be updated. You only edit the properties of the alarm group for alarm groups from alarm classes.

  Alarm groups from alarm classes, which are also known as class groups, are displayed in WinCC under "HMI alarms &gt; Alarm groups &gt; Class groups".

  > **Note**
  >
  > An alarm is always contained in an alarm group from an alarm class. An alarm that requires acknowledgment can also belong to a custom alarm group.

##### Alarm group IDs in WinCC and STEP 7

Each alarm group has a unique ID. If you create 15 user-defined alarm groups after creating an HMI device, these alarm groups receive the IDs 17-31. If you create further user-defined alarm groups after this, these alarm groups receive IDs &gt; 35. The four pre-defined alarm classes in every WinCC project automatically occupy IDs 32-35 with their alarm groups. If you create an HMI connection between the HMI device and controller, 16 user-defined alarm groups with the IDs 1-16 are created in WinCC. With these alarm groups, WinCC supports the 16 alarm groups from STEP 7 with the IDs 1-16. WinCC does not support the alarm group with the ID 0 from STEP 7. When the HMI connection is created, at least two more alarm groups are created from alarm classes in WinCC. These alarm groups are created for the alarm classes that are created new by the HMI connection and linked with the project-wide alarm classes under "Common data &gt; Alarm classes". The at least two further alarm groups from alarm classes receive IDs &gt; 35.

The alarm group ID of a user-defined alarm group is displayed at the following locations in WinCC:

- Under "HMI alarms &gt; Alarm groups &gt; Alarm groups" in the column "ID"
- In the properties of the user-defined alarm group in the Inspector window under "Properties &gt; General &gt; General &gt; Settings &gt; ID"

The alarm group ID of a class group is displayed in WinCC in the properties of the class group in the Inspector window under "Properties &gt; General &gt; General &gt; Settings &gt; ID".

In STEP 7, you select an alarm group ID from 0-16 in the properties of a controller alarm in the Inspector window under "Advanced settings &gt; Group ID". The controller alarm is hereby assigned to the alarm group with the selected alarm group ID. The alarm group ID 0 is preset in the properties of a controller alarm. This means that a controller alarm is assigned by default to the alarm group with the ID 0, which is not supported by WinCC.

---

**See also**

[Hierarchical alarm groups (RT Professional)](#hierarchical-alarm-groups-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)
  
[Configuring alarm groups (RT Professional)](#configuring-alarm-groups-rt-professional)

#### Hierarchical alarm groups (RT Professional)

##### Introduction

WinCC allows you to compile alarms and custom alarm groups hierarchically. In this way, you construct a hierarchy of alarms that allows you to clearly and quickly detect and process the states of complex plants.

You can only create this hierarchy from alarms and alarm groups with custom alarm groups.

##### Structure of Hierarchical Alarm Groups

You compile custom alarm groups and single alarms hierarchically as required. You can also subsequently add child alarm groups.

The following figure shows a hierarchical alarm group in WinCC:

![Structure of Hierarchical Alarm Groups](images/72282831883_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> If you subsequently add an alarm group, the numbering will no longer be consecutive.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| When you create a hierarchy of alarm groups, make sure that you do not use them recursively. |  |

> **Note**
>
> If you delete an alarm group that contains other alarm groups, all lower-level alarm groups will be deleted as well.

##### Components of parent alarm groups

A parent alarm group contains the following elements as required:

- Single alarms
- Child alarm groups

##### Display suppression tag

You only assign the display suppression tag to alarm groups that contain no alarm subgroups and to customized alarm groups.

---

**See also**

[Alarm Group Basics (RT Professional)](#alarm-group-basics-rt-professional)
  
[Configuring alarm groups (RT Professional)](#configuring-alarm-groups-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)

#### Tags of an alarm group (RT Professional)

##### Tags of an alarm group

You can assign the following tags to an alarm group:

##### Status tag

The status tag stores the alarm states of an alarm group.

The status tag stores the acknowledgment request. The acknowledgment request is pending in an alarm group when at least one of the alarms in the group is queued and this alarm requires acknowledgement.

The status tag is used to visualize the alarm states and the acknowledgment request of an alarm group.

The status tag can be checked by other WinCC components.

##### Lock tag

The lock tag stores the locked status of an alarm group.

The lock tag is used to analyze the locked status of an alarm group.

##### Acknowledgment tag

The acknowledgment tag stores the "acknowledged" status of an alarm group.

The acknowledgment tag is used to acknowledge an alarm group.

The acknowledgment tag can be polled by other WinCC components.

> **Note**
>
> The acknowledgment bit of an acknowledgment tag is not automatically reset. You can configure a button or function key to do this. Use this button to reset the acknowledgment bit of the acknowledgment tag.
>
> The acknowledgment tag of an alarm group does not display the acknowledgment via the alarm view.

##### Display suppression tag

The display suppression tag automatically suppresses the display of all the alarms for an alarm group in response to a specific plant status.

The display suppression tag returns the current value of the plant status as a value between 1 and 32. All alarms of the alarm group for which the corresponding bit of the number between 1 and 32 is set in the display suppression mask are suppressed.

---

**See also**

[Alarm Group Basics (RT Professional)](#alarm-group-basics-rt-professional)
  
[Hierarchical alarm groups (RT Professional)](#hierarchical-alarm-groups-rt-professional)
  
[Configuring alarm groups (RT Professional)](#configuring-alarm-groups-rt-professional)
  
[Configuring Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Bit assignment for lock tags (RT Professional)](#bit-assignment-for-lock-tags-rt-professional)
  
[Bit assignment for display suppression tags (RT Professional)](#bit-assignment-for-display-suppression-tags-rt-professional)
  
[Bit assignment of status tag (RT Professional)](#bit-assignment-of-status-tag-rt-professional)
  
[Bit assignment for acknowledgment tags (RT Professional)](#bit-assignment-for-acknowledgment-tags-rt-professional)

### Alarm number  (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Assigning alarm numbers

The system assigns unique alarm numbers within an alarm type.

> **Note**
>
> When adapting alarm numbers, observe the uniqueness of the alarm number within an alarm type.

---

**See also**

[Alarm Logging in WinCC (Basic Panels)](#alarm-logging-in-wincc-basic-panels)
  
[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Alarm number  (RT Professional)

#### Assigning alarm numbers

The system assigns unique alarm numbers for the project.

> **Note**
>
> When adapting alarm numbers, observe the inter-project uniqueness of the alarm number.

The system event number overrides a custom alarm number. If you are using the alarm number of a system event for a user-defined alarm, change the alarm number of the user-defined alarm.

---

**See also**

[Alarm Logging in WinCC (RT Professional)](#alarm-logging-in-wincc-rt-professional)
  
[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Working with Alarms  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the Outputting of Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-outputting-of-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-acknowledgment-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring acknowledgment (RT Professional)](#configuring-acknowledgment-rt-professional)

### Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Overview

You configure the components of alarms in WinCC. The following table shows the basic components of alarms:

| Alarm class | Alarm  number | Time of day | Date | Alarm status | Alarm text | Alarm group | Tooltip | Trigger tag | Limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Warning | 1 | 11:09:14 | 06 Aug 2007 | IO | Maximum speed reached | 2 | This alarm is ... | speed_1 | 27 |
| System | 110001 | 11:25:58 | 06 Aug 2007 | I | Switch to "Online" mode | 0 | This alarm is ... | PLC-Variable_1 | – |

#### Alarm class

Alarm classes, such as "Warnings" or "Errors". The alarm class defines the following for an alarm:

- State machine
- Appearance in Runtime (e.g. color)
- Logging

> **Note**
>
> **Device dependency**
>
> Logging is not available for all HMI devices.

#### Alarm number

An alarm is identified by a unique alarm number. The alarm number is assigned by the system. You can change the alarm number to a sequential alarm number, if necessary, to identify alarms associated in your project.

#### Time and date

Every alarm has a time stamp that shows the time and date at which the alarm was triggered.

#### Alarm status

An alarm has the events "Incoming," "Outgoing," "Acknowledge." For each event, a new alarm is output with the current status of the alarm.

#### Alarm text

The alarm text describes the cause of the alarm.

The alarm text can contain output fields for current values. The values you can insert depend on the Runtime in use. The value is retained at the time at which the alarm status changes.

#### Alarm group

The alarm group bundles individual alarms.

#### Tooltip

You can configure a separate tooltip for each alarm; the user can display this tooltip in Runtime.

#### Trigger tag

A tag is assigned to each alarm as trigger. The alarm is raised when this trigger tag meets the defined condition, e.g. when its state changes or it exceeds a limit.

#### Limit

Analog alarms indicate limit violations. Depending on the configuration, WinCC outputs the analog alarm as soon as the trigger tag exceeds or undershoots the limit value.

---

**See also**

[Basics on alarm classes (Basic Panels)](#basics-on-alarm-classes-basic-panels)
  
[Basics on alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm states (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-states-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm number (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-number-basic-panels-panels-comfort-panels-rt-advanced)
  
[Alarm number (RT Professional)](#alarm-number-rt-professional)
  
[Alarm groups (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-groups-basic-panels-panels-comfort-panels-rt-advanced)
  
[Alarm groups (RT Professional)](#alarm-groups-rt-professional)
  
[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of alarm configuration tasks (Basic Panels)](#overview-of-alarm-configuration-tasks-basic-panels)
  
[Overview of the alarm types (Panels, Comfort Panels, RT Advanced)](#overview-of-the-alarm-types-panels-comfort-panels-rt-advanced)
  
[Overview of the alarm types (RT Professional)](#overview-of-the-alarm-types-rt-professional)
  
[Overview of the alarm types (Basic Panels)](#overview-of-the-alarm-types-basic-panels)
  
[Alarm Logging in WinCC (Basic Panels)](#alarm-logging-in-wincc-basic-panels)
  
[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Alarm Logging in WinCC (RT Professional)](#alarm-logging-in-wincc-rt-professional)

### Configuring Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of alarm configuration tasks (Basic Panels)](#overview-of-alarm-configuration-tasks-basic-panels)
- [Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring Alarm Classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring Alarm Groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configure alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configure-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [Configure alarms (RT Professional)](#configure-alarms-rt-professional)
- [Configuring loop-in alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-loop-in-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarms in the "HMI tags" Editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarms-in-the-hmi-tags-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of alarm configuration tasks (Basic Panels)

##### Steps to configure alarms

Configuring alarms in WinCC involves the following steps:

1. Edit and create alarm classes

   You use the alarm class to define how an alarm will be displayed in runtime and to define the state machines for it.
2. Creating tags in the "HMI tags" editor

   - Configure the tags for your project.
   - You create range values for the tags.
3. Creating tags in the "HMI alarms " editor

   - Create custom alarms and assign the tag to be monitored, alarm classes, alarm groups, and other properties to them.
   - You can also assign system functions or scripts to the alarm events.
4. Output of configured alarms

   To output configured alarms, configure an alarm view or an alarm window in the "Screens" editor.

##### Additional configuration tasks

Additional tasks could be necessary for configuring alarms, depending on the requirements of your project:

1. Creating alarm groups

   You assign the alarms of your project to alarm groups according to their association, such as by the cause of the problem (power failure) or source of the error (Motor 1).
2. Configuring Loop-In-Alarm

   A Loop-In-Alarm is configured in order to change to a screen containing relevant information on an alarm received.

---

**See also**

[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configure alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configure-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configure alarms (RT Professional)](#configure-alarms-rt-professional)
  
[Configuring loop-in alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-loop-in-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarms in the "HMI tags" Editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarms-in-the-hmi-tags-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring the Outputting of Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-outputting-of-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-acknowledgment-basic-panels-panels-comfort-panels-rt-advanced)

#### Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Steps to configure alarms

Configuring alarms in WinCC involves the following steps:

1. Edit and create alarm classes

   You use the alarm class to define how an alarm will be displayed in runtime and to define the state machines for it.
2. Creating tags in the "HMI tags" editor

   - Configure the tags for your project.
   - You create range values for the tags.

1. Creating tags in the "HMI alarms " editor

   - Create custom alarms and assign the tag to be monitored, alarm classes, alarm groups, and other properties to them.
   - You can also assign system functions or scripts to the alarm events.
2. Output of configured alarms

   To output configured alarms, configure an alarm view or an alarm window in the "Screens" editor.

##### Additional configuration tasks

Additional tasks could be necessary for configuring alarms, depending on the requirements of your project:

- Activating and editing system events

  You can import system events when you initially open the "System events" tab in the "HMI alarms" editor. On completion of the import, you can edit the system events.
- Activating and editing controller alarms

  For integrated operation of a project in STEP 7, specify the controller alarms to be displayed on your HMI device in the alarm settings.
- Creating alarm groups

  Assign the alarms of your project to alarm groups based on their relation, e.g. by error cause (e.g. "power failure"), or by error source (e.g. "Motor 1").
- Configuring Loop-In-Alarm

  Configure a Loop-In-Alarm in order to, after receipt of an alarm, change to a screen that contains your information about the selected alarm.

---

**See also**

[Alarm components and properties (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-components-and-properties-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
  
[Configure alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configure-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configure alarms (RT Professional)](#configure-alarms-rt-professional)
  
[Editing system events (RT Professional)](#editing-system-events-rt-professional)
  
[Editing system events (Panels, Comfort Panels, RT Advanced)](#editing-system-events-panels-comfort-panels-rt-advanced)
  
[Enabling system-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#enabling-system-defined-controller-alarms-panels-comfort-panels-rt-advanced)
  
[Editing controller alarms (Panels, Comfort Panels, RT Advanced)](#editing-controller-alarms-panels-comfort-panels-rt-advanced)
  
[Alarms in the "HMI tags" Editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarms-in-the-hmi-tags-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring loop-in alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-loop-in-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring the Outputting of Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-outputting-of-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring acknowledgment (RT Professional)](#configuring-acknowledgment-rt-professional)

#### Configuring Alarm Classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)
- [Configuring the state texts of an alarm class (RT Professional)](#configuring-the-state-texts-of-an-alarm-class-rt-professional)
- [Using common alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#using-common-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)

##### Creating alarm classes  (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

Create alarm classes in the "Alarm classes" tab of the "HMI alarms" editor. Some default alarm classes are already created for every project. You can create additional custom alarm classes. You can create up to 32 alarm classes.

###### Requirement

- The "HMI alarms" editor is open.
- The Inspector window is open.

###### Procedure

To create an alarm class, proceed as follows:

1. Click the "Alarm classes" tab.

   The predefined and existing custom alarm classes are displayed. The following table lists the predefined alarm classes:

   ![Procedure](images/111886374155_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111886374155_DV_resource.Stream@PNG-en-US.png)

1. Double-click "&lt;Add&gt;" in the table.

   A new alarm class is created. Each new alarm class is automatically assigned a static ID.

   The properties of the new alarm class are shown in the Inspector window.
2. Configure the alarm class under "Properties &gt; Properties &gt;General" in the Inspector window.

   - Enter a "Name" and the "Display name".
   - Depending on the HMI device, you can also activate logging, or automatic sending of e-mails.
3. Define the state machines for the alarm class under "Properties &gt; Properties &gt; Acknowledgment" in the Inspector window.
4. Change the default text under "Properties &gt; Properties &gt; Status texts" in the Inspector window.

   This text indicates the status of an alarm in Runtime.
5. Change the default colors under "Properties &gt; Properties &gt; Colors" in the Inspector window. Depending on the HMI device, also change the flashing characteristics.

These settings define how alarms from this alarm class are displayed in Runtime.

> **Note**
>
> To display the alarm classes in color in Runtime, the "Use alarm class colors" option must be activated. In the project navigation, enable "Runtime settings &gt; Alarms &gt; General &gt; Use alarm class colors" accordingly.

---

**See also**

[Configuring alarm acknowledgment by means of alarm class (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-alarm-acknowledgment-by-means-of-alarm-class-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on alarm classes (Basic Panels)](#basics-on-alarm-classes-basic-panels)
  
[Basics on alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Predefined alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#predefined-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Using common alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#using-common-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)

##### Creating alarm classes (RT Professional)

###### Introduction

Create alarm classes in the "Alarm classes" tab of the "HMI alarms" editor. Some default alarm classes are already created for every project. You can create additional custom alarm classes. You can configure up to 256 alarm classes per project.

###### Requirement

- The "HMI alarms" editor is open.
- The Inspector window is open.

###### Procedure

To create an alarm class, proceed as follows:

1. Click the "Alarm classes" tab.

   A table of the pre-defined alarm classes is shown below:

   ![Procedure](images/72284004107_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72284004107_DV_resource.Stream@PNG-en-US.png)

1. Double-click "&lt;Add&gt;" in the table.

   A new alarm class is created. Each new alarm class is automatically assigned a static ID.

   The properties of the new alarm class are shown in the Inspector window.
2. Configure the alarm class under "Properties &gt; Properties &gt;General" in the Inspector window:

   - Enter a "Name" and the "Display name".
   - Activate the"Log" check box if you want to log the alarms from this alarm class.
3. Select "Properties &gt; Properties &gt; Acknowledgment" in the Inspector window to define the state machines for the alarm class and alarm annunciator.
4. If required, change the preset state texts in the Inspector window under "Properties &gt; Properties &gt; Status".

   The status texts are used in Runtime to display the status of an alarm.
5. You can also change the default background and foreground colors under "Properties &gt; Properties &gt; Colors" in the Inspector window.

   These settings define how alarms from this alarm class are displayed in Runtime.

###### Additional settings for alarm classes

**Comments in Runtime**

The user enters a comment for an incoming alarm in Runtime, as required. Using the buttons of the alarm view, users can show the comments in the "Historical alarm list" display. You can configure this function in the alarm class. Enter the user in the "User name" system block.

**Assign comments to defined user**

To assign the comments to the user logged on, proceed as follows:

1. Select the alarm class.
2. Enable "Properties &gt; Properties &gt; Acknowledgment &gt; Settings &gt; Assign comments to defined user" in the Inspector window.

   Any user can enter the first comment if a comment has yet to be entered.

   When the first comment has been entered, all other users have read-only access to it.

**Use comment of the incoming alarm**

Whenever the status of an alarm changes, for example, from "incoming" to "acknowledged" status, the alarm is output once again with another status. The user only assigns comments to one incoming alarm. To include comments for alarm output with the new status, proceed as follows:

1. Select the alarm class.
2. Enable "Properties &gt; Properties &gt; Acknowledgment &gt; Settings &gt; Use comment of the incoming alarm" in the Inspector window.

---

**See also**

[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)
  
[Configuring acknowledgment of the alarm annunciator (RT Professional)](#configuring-acknowledgment-of-the-alarm-annunciator-rt-professional)
  
[Basics on alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Predefined alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#predefined-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging alarms (RT Professional)](#logging-alarms-rt-professional)
  
[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
  
[Alarm states (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarm-states-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Acknowledgment model (RT Professional)](#acknowledgment-model-rt-professional)
  
[Displaying logged alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-logged-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Using common alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#using-common-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring the state texts of an alarm class (RT Professional)](#configuring-the-state-texts-of-an-alarm-class-rt-professional)

##### Configuring the state texts of an alarm class (RT Professional)

###### Introduction

The texts for the status of an alarm in Runtime are displayed in the alarm view in the system blocks "Status" and "Acknowledgment status". You define the state texts of an alarm in the alarm class.

###### Requirement

- The "HMI alarms" editor is open.
- The Inspector window is open.

###### Procedure

To configure the state texts of an alarm, proceed as follows:

| 1. Create a new alarm class in the "Alarm classes" tab.    The properties of the new alarm class are shown in the Inspector window. 2. Define the state texts for runtime alarms in the Inspector window under "Properties &gt; Properties &gt; Status":       | Field | Description |    | --- | --- |    | Incoming | Text for incoming alarms when changing to the operating state to be reported |    | Outgoing | Text for outgoing alarms when changing from the operating state to be reported |    | Acknowledged | Text for acknowledged alarms |    | Incoming/outgoing | Text for incoming and outgoing alarm | 3. If required, configure additional properties of the alarm class in the Inspector window under "Properties &gt; Properties". 4. Create tags in the "HMI Tags" editor:    - Configure the tags for your project.    - Create range values for the tags. 5. Create a user-defined alarm in the "HMI Alarms" editor:    - Assign the alarm to the alarm class created, the tag to be monitored, and other properties.    - If required, assign system functions or scripts to the events of the alarm. 6. Use the project navigation to create a new screen. 7. To output the created alarm with the defined status texts in Runtime, insert the "Alarm view" object from the "Tools" task card into the screen.    The properties of the alarm view are shown in the Inspector window. 8. Deactivate the "Accept project settings" option in the Inspector window under "Properties &gt; Properties &gt; Blocks". 9. To use the "Status" and "Acknowledgment status" system blocks in the alarm view, activate the two system blocks in the "Selected" column. 10. In the "Length" column, define the text length of the "Status" and "Acknowledgment status" system blocks so that the defined state texts can be displayed in full. 11. In the rows of the "Status" and "Acknowledgment status" system blocks, select the entry "Text" or "Both" in the "Contents as" column.       | Symbol | Meaning |     | --- | --- |     | **Note**  If you select the "Both" entry, the contents of the "Status" and "Acknowledgment status" system blocks in Runtime are not only displayed as text, but also as symbols. |  | 12. To display the "Status" and "Acknowledgment status" system blocks as columns in the alarm view, activate the columns "Status" and "Acknowledgment status" under "Visible" under "Properties &gt; Properties &gt; Columns". |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

###### Result

You have configured the state texts of an alarm. The display of the defined state texts in runtime depends on the selected list in the alarm view:

| List | System block | Display of state texts from the field |
| --- | --- | --- |
| Alarm list | Status | "Incoming" or "Incoming / Outgoing" |
| Alarm list | Acknowledgment status | "Acknowledged" |
| Historical alarm list (short-term) | Status | "Incoming, Acknowledged" or "Outgoing" |
| Historical alarm list (short-term) | Acknowledgment status | No text is displayed. |
| Historical alarm list (long-term) | Status | "Incoming, Acknowledged" or "Outgoing" |
| Historical alarm list (long-term) | Acknowledgment status | No text is displayed. |
| Lock list | Status | No text configurable.  If the alarm is locked, the "Lock" text is displayed. The lock cannot be configured. |
| Lock list | Acknowledgment status | No text configurable.  No text is displayed. |

> **Note**
>
> The system generates the display of the state texts "Acknowledgment - System" (alarms acknowledged by the system) and "Emergency acknowledgment" (alarms acknowledged via the emergency acknowledgment) in the Historical alarm list (short-term) and Historical alarm list (long-term).

---

**See also**

[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)
  
[Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Description of the System Blocks (RT Professional)](#description-of-the-system-blocks-rt-professional)

##### Using common alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

Common alarm classes are displayed under "Common data &gt; Alarm classes" in the project tree. If required, create additional common alarm classes in WinCC.

Controller alarms are assigned to common alarm classes. If you work with controller alarms, common alarm classes are automatically loaded in WinCC.

###### Requirements

- You have created a project.

###### Creating common alarm class

To create a common alarm class, proceed as follows:

1. Double-click "Common data &gt; Alarm classes" in the project tree.

   The "Common alarm classes" editor opens in the work area.
2. To create a common alarm class, double-click in the first empty line of the table editor.
3. Specify the name and display name of the alarm class.
4. Select "With acknowledgment" if the alarm class requires acknowledgment.

###### Assign alarms to a common alarm class

Proceed as follows to assign an analog or discrete alarm to a common alarm class:

1. In the "HMI alarms" editor, select the alarm that you want to assign to the common alarm class.
2. Click "General" in the Inspector window.
3. Click "Common data &gt; Alarm classes" in the project tree.
4. Select the common alarm class in the detail view.
5. Drag-and-drop the alarm class to the "Alarm class" selection box or "Alarm class" column in the work area of the Inspector window of the alarm.

   ![Assign alarms to a common alarm class](images/111887608971_DV_resource.Stream@PNG-en-US.png)

   ![Assign alarms to a common alarm class](images/111887608971_DV_resource.Stream@PNG-en-US.png)

   The system creates a new alarm class that is linked to the common alarm class. The new name of the common alarm class is displayed in the "Alarm class" area of the Inspector window of the alarm. The display name of the common alarm class is activated for the alarm class in your project.
6. Click the "Alarm Class" tab.
7. Check to see whether the display name of the common alarm class is displayed in WinCC.
8. You can change the object name of the alarm class.

###### Alternative procedure

To assign an alarm to a common alarm class, proceed as follows:

1. Click the "Alarm Classes" tab.

   The alarm classes are displayed.
2. Click "Common data &gt; Alarm classes" in the project tree. The following table shows the common alarm classes:

   ![Alternative procedure](images/72284051467_DV_resource.Stream@PNG-en-US.png)

   ![Alternative procedure](images/72284051467_DV_resource.Stream@PNG-en-US.png)
3. Select the common alarm class in the detail view.
4. Drag-and-drop the alarm class to the "Alarm classes" tab of the "HMI alarms" editor

   The system creates a new alarm class that is linked to the common alarm class. The new name of the new alarm class in your project is displayed in the "Alarm class" tab.
5. Open the tab with the alarm procedure for the required alarm.
6. Under "General" in the Inspector window, select the alarm and the alarm class linked to the common alarm class.

> **Note**
>
> **Deleting a common alarm class**
>
> If you delete a common alarm class, the linked alarm class is maintained. If necessary, link the alarm class with another common alarm class or use it as WinCC alarm class.

---

**See also**

[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on alarm classes (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-alarm-classes-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)

#### Configuring Alarm Groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Configuring alarm groups (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-alarm-groups-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring alarm groups (RT Professional)](#configuring-alarm-groups-rt-professional)

##### Configuring alarm groups  (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

Create alarm groups on the "Alarm Groups" tab in the "HMI alarms" editor. An alarm group is a compilation of single alarms. You assign alarms in an alarm group by association, such as cause of the problem or source of the error. If you acknowledge an alarm from this alarm group in Runtime, all other alarms in the alarm group are acknowledged automatically.

###### Requirement

- You have created a project.
- The "HMI alarms" editor is open.
- The Inspector window is open.

###### Creating a new alarm group

1. Click the "Alarm Groups" tab.

   The existing alarm groups are displayed.

   ![Creating a new alarm group](images/72332068747_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new alarm group](images/72332068747_DV_resource.Stream@PNG-en-US.png)
2. In the work area of the table, double-click "&lt;Add&gt;" in the first free row.

   A new alarm group is created.
3. You can overwrite the proposed "Name".

###### Result

An alarm group is created. For the group acknowledgment of alarms in Runtime, assign the associated alarms that require acknowledgment to an alarm group.

---

**See also**

[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm groups (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-groups-basic-panels-panels-comfort-panels-rt-advanced)

##### Configuring alarm groups  (RT Professional)

###### Introduction

Create custom alarm groups on the "Alarm Groups" tab of the "HMI alarms" editor. The alarm groups from alarm classes are already created on a separate tab. You acknowledge alarms from an alarm group together in Runtime. Configure a corresponding group acknowledgment button for the alarm group, including an additional button for resetting the acknowledgment bit of the acknowledgment tag.

###### Requirements

- You have created a project.
- The "HMI alarms" editor is open.
- The Inspector window is open.

###### Creating a new alarm group

To create an alarm group, proceed as follows:

1. Click the "Alarm Groups" tab.

   The existing alarm groups are displayed.

   ![Creating a new alarm group](images/72307909131_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new alarm group](images/72307909131_DV_resource.Stream@PNG-en-US.png)
2. Double-click "&lt;Add&gt;" in the table.  
   A new alarm group is created.

   The properties of the new alarm group are shown in the Inspector window.
3. In the Inspector window, click "Properties &gt; Properties &gt; General" and enter a name for the alarm group.
4. In the Properties window, click "Properties &gt; Properties &gt; Tags" to specify the following tags and bits:

   - Status tag for visualizing the alarm states of the alarm group
   - Acknowledgment tag for acknowledging an alarm group
   - Lock tag for visualizing the locked status of an alarm group
   - Display suppression tag for filtering alarms in Runtime by plant status

###### Creating a child alarm group

To create a child alarm group, proceed as follows:

1. Click the "Alarm Groups" tab.
2. In the work area or in the detail view, select the alarm groups you want to insert as a child group.
3. Drag and drop the alarm groups onto another alarm group.

   The selected alarm groups become a child group in the hierarchy of this alarm group.

If you want to create a parent group for a hierarchy of alarm groups, drag and drop the entire hierarchy to this alarm group.

###### Alternative procedure

1. Click the "Alarm Groups" tab.
2. Select the alarm groups for which you want to create a subgroup.
3. In the cell on the left of the selected row, open the shortcut menu and select "Insert child element".

   A new child alarm group is created.

   ![Alternative procedure](images/72307913611_DV_resource.Stream@PNG-en-US.png)

   ![Alternative procedure](images/72307913611_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Alarm Group Basics (RT Professional)](#alarm-group-basics-rt-professional)
  
[Hierarchical alarm groups (RT Professional)](#hierarchical-alarm-groups-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)
  
[Configuring Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tag Bit Assignments (RT Professional)](#tag-bit-assignments-rt-professional)

#### Configure alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring Analog Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-analog-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [Formatting alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#formatting-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
- [Output of a tag value in the alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-a-tag-value-in-the-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
- [Output of texts from a text list in an alarm (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-texts-from-a-text-list-in-an-alarm-basic-panels-panels-comfort-panels-rt-advanced)
- [Editing system events (Panels, Comfort Panels, RT Advanced)](#editing-system-events-panels-comfort-panels-rt-advanced)
- [Editing controller alarms (Panels, Comfort Panels, RT Advanced)](#editing-controller-alarms-panels-comfort-panels-rt-advanced)
- [Enabling system-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#enabling-system-defined-controller-alarms-panels-comfort-panels-rt-advanced)

##### Configuring Analog Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

Analog alarms indicate limit violations. For example, if the speed of a motor drops below a certain value, an analog alarm is triggered.

###### Requirements

- The "HMI alarms" editor is open.
- The Inspector window is open.
- You have created the required alarm classes and alarm groups.

###### Procedure

To configure an analog alarm, proceed as follows:

1. Click the "Analog alarms" tab.
2. To create a new analog alarm, double-click in the table on "&lt;Add&gt;".

   A new analog alarm is created.
3. To configure the alarm, select "Properties &gt; Properties &gt;General" in the Inspector window:

   - Enter an alarm text as event text.

     Format the text character-for-character using the shortcut menu.

     Using the shortcut menu, you can insert output fields for HMI tags, or text from text lists.
   - You can renumber the alarm.
   - Select the alarm class and the alarm group, if necessary.

     ![Procedure](images/89645735819_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/89645735819_DV_resource.Stream@PNG-en-US.png)
4. Configure the tag that triggers the alarm under "Properties &gt; Properties &gt; Trigger &gt; Settings".

   Do not use trigger tags for anything else.

###### Configure limit values for an analog alarm

1. In the Inspector window, click the ![Configure limit values for an analog alarm](images/14170060427_DV_resource.Stream@PNG-de-DE.png) button under "Properties &gt; Properties &gt; Trigger &gt; Limit &gt; Value".

   - To use a constant as limit value, select "Constant".

     Enter the required limit value.
   - To use a tag as limit value, select "HMI tag".

     The ![Configure limit values for an analog alarm](images/21587487883_DV_resource.Stream@PNG-de-DE.png) button appears. Use this button to select the tag you want to use.
2. Select the mode:

   - "Higher": The alarm is triggered when the limit is exceeded.
   - "Lower": The alarm is triggered when the limit is undershot.

**Note**

If the required tag does not exist in the selection list yet, create it in the object list and change its properties later.

###### Optional settings for analog alarms

**Setting the delay time**

To set the delay time, proceed as follows:

- Enter a time period in the Inspector window under "Properties &gt; Properties&gt; Trigger &gt; Settings &gt; Delay".

  The alarm is only triggered when the trigger condition is still present after the delay time has elapsed.

###### Setting the deadband

> **Note**
>
> If a process value fluctuates around the limit, the alarm associated with this fault may be triggered multiple times. To prevent this from happening, configure a deadband or delay time.

To enter the deadband, follow these steps:

1. Under "Properties &gt; Properties&gt; Trigger &gt; Deadband &gt; Mode", select the change in alarm status for which the deadband is to be taken into account.
2. Enter a constant value under "Value".
3. To define the deadband value as a percentage of the limit, set the "in %" check box.

###### Automatic reporting

To print the alarms continuously:

- Select the "Activate" option under "Properties &gt; Properties &gt; Miscellaneous &gt; Report."

  > **Note**
  >
  > Device dependency
  >
  > Reporting is not available for all HMI devices.

###### Creating a tooltip

To configure a tooltip for the alarm, follow these steps:

- Select "Properties &gt; Properties &gt; Tooltip" in the Inspector window and enter your text.

###### Configuring event-driven tasks

To configure event-driven tasks, such as a loop-in alarm, follow these steps:

1. Select the analog alarm.
2. In the Inspector window, select "Properties &gt; Events &gt; Loop-In-Alarm.
3. Select, for example, the system function "ActivateScreen" or a different system function that is be called for Loop-In-Alarm.
4. Select the parameters required for the selected system function.

   With "ActivateScreen“, the screen is to be called.

---

**See also**

[Overview of alarm configuration tasks (Basic Panels)](#overview-of-alarm-configuration-tasks-basic-panels)
  
[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Output of a tag value in the alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-a-tag-value-in-the-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring trigger for alarm acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-trigger-for-alarm-acknowledgment-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
  
[Formatting alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#formatting-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
  
[Output of texts from a text list in an alarm (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-texts-from-a-text-list-in-an-alarm-basic-panels-panels-comfort-panels-rt-advanced)

##### Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

Discrete alarms triggered by the PLC indicate status changes in a plant. They indicate the opened or closed state of a valve, for example.

The following sections describes the configuration procedures in the "HMI alarms" editor. You can also configure discrete alarms in the "HMI tags" editor.

###### Requirements

- The "HMI alarms" editor is open.
- The Inspector window is open.
- You have created the required alarm classes and alarm groups.

###### Procedure

To configure a discrete alarm, proceed as follows:

1. Open the "Discrete alarms" tab.
2. To create a new discrete alarm, double-click in the work area on "&lt;Add&gt;".

   A new discrete alarm is created.
3. To configure the alarm, select "Properties &gt; Properties &gt;General" in the Inspector window:

   - Enter an alarm text as event text.

     Use the functions of the shortcut menu to format the text on a character-by-character basis, or to insert output fields for HMI tags, or texts from the text lists.
   - You can renumber the alarm.
   - Select the alarm class and the alarm group, if necessary.
4. In the Inspector window, select the tag and the bit that triggers the alarm under "Properties &gt; Properties &gt; Trigger". Note the following information:

   - Use the data types "Int" or "UInt" to select an HMI tag.
   - When you select a PLC tag, use the data types "Int" or "Word". The input and output area of a PLC tag is unsuitable as trigger.
   - Use trigger tag bits only for alarms.
   - Do not use trigger tags for anything else.
   - If you want to acknowledge the alarm via the PLC, use this tag also as PLC acknowledgment tag.

> **Note**
>
> Note the method used to count bits in the utilized PLC when specifying the bit. For more information, refer to the "Communication" section in the PLC Online Help.

> **Note**
>
> If the object does not yet exist in the selection list, create it directly in the object list and change its properties later.

###### Status-dependent alarm texts

To display a different text independent of the alarm status, link a text list to the alarm text. You control the text list with a tag.

###### Additional settings for discrete alarms

###### Creating a tooltip

To configure a tooltip for the alarm, follow these steps:

- Enter your text under "Properties &gt; Properties &gt; Tooltip".

###### Configuring event-driven tasks

To configure event-driven tasks, such as a loop-in alarm, follow these steps:

1. Select the discrete alarm.
2. Select "Properties &gt; Events" in the Inspector window and configure a new function list for the relevant event.

---

**See also**

[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of alarm configuration tasks (Basic Panels)](#overview-of-alarm-configuration-tasks-basic-panels)
  
[Configuring trigger for alarm acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-trigger-for-alarm-acknowledgment-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
  
[Output of texts from a text list in an alarm (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-texts-from-a-text-list-in-an-alarm-basic-panels-panels-comfort-panels-rt-advanced)
  
[Formatting alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#formatting-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
  
[Output of a tag value in the alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-a-tag-value-in-the-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring Analog Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-analog-alarms-basic-panels-panels-comfort-panels-rt-advanced)

##### Formatting alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

The alarm texts can be formatted or special characters inserted in the alarm texts to emphasize specific events or processes.

###### Requirement

- The "HMI alarms" editor is open.
- An alarm has been created.

###### Formatting alarm texts

To format an alarm text, proceed as follows:

1. Select the alarm to edit.
2. In the Inspector window, select the characters to format under "Properties &gt; Properties &gt; General &gt; Alarm text".
3. Select the formatting from the shortcut menu, e.g. "Underscored" or "Uppercase".

   The selected characters are displayed in Runtime with the selected formatting.

> **Note**
>
> It is not possible to underline tags and text list entries.

> **Note**
>
> **Displaying special characters in alarm texts**
>
> When configuring alarm texts, a fixed character set is used in the Engineering System. This character set allows you to use numerous special characters in alarm texts.
>
> Language-dependent fonts are used in runtime to display the texts, for example MS PGothic, SimSun. The fonts used in runtime do not support all special characters. As a result, some special characters are not displayed in runtime.

###### Removing format settings

To remove all text formats, proceed as follows:

1. In the Inspector window, select the characters whose formatting you want to remove in the alarm text.
2. Select "Delete formatting characters" from the shortcut menu.

   The selected characters are displayed in unformatted notation in Runtime.

---

**See also**

[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of alarm configuration tasks (Basic Panels)](#overview-of-alarm-configuration-tasks-basic-panels)
  
[Configuring Analog Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-analog-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Output of a tag value in the alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-a-tag-value-in-the-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
  
[Output of texts from a text list in an alarm (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-texts-from-a-text-list-in-an-alarm-basic-panels-panels-comfort-panels-rt-advanced)

##### Output of a tag value in the alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

In WinCC, you can insert output fields into the alarm text which display the content of tags.

###### Requirements

- The "HMI alarms" editor is open.
- The alarm is selected.

###### Output of a tag value in the alarm text

To insert an output field for a tag value in the alarm text, proceed as follows:

1. Place the cursor onto the required position in the event text.
2. Select "Insert tag output field" in the shortcut menu.
3. Open the object list under "Tag" and select a tag.

   You can also create the tag in the object list.
4. Under "Format", specify the length of the output field and the format for tag value output in the alarm text.

   Configure an output field of sufficient size. Otherwise, the tag content is not output to the full extent in the alarm.
5. Click ![Output of a tag value in the alarm text](images/70512612363_DV_resource.Stream@PNG-de-DE.png) to save your entries.

WinCC inserts a placeholder for the output field into the alarm text: "&lt;tag: n, [tag name]&gt;" whereby n = text string length.

###### Editing output field properties

To edit the properties of an output field, proceed as follows:

- Double-click on the output field in the alarm text and edit the settings.

###### Deleting an output field from the alarm text

To delete an output field from the alarm text, proceed as follows:

- Select the output field in the alarm text and then select the "Delete" command from the shortcut menu.

> **Note**
>
> The sequence of the tag output fields in the alarm text depends on the language. The sequence of the Runtime language is used for logging alarms to a CSV log file.
>
> Changing the tag of an output field in one language causes the modified output field to appear at the end of the alarm text in all other languages. This changes the sequence of the output fields in the log.
>
> Device dependency
>
> Logging is not available for all HMI devices.

---

**See also**

[Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring Analog Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-analog-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Formatting alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#formatting-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
  
[Output of texts from a text list in an alarm (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-texts-from-a-text-list-in-an-alarm-basic-panels-panels-comfort-panels-rt-advanced)

##### Output of texts from a text list in an alarm (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

Text lists are used to create dynamic alarm texts. For example, you can configure the output of both states of a discrete alarm in an alarm text.

Insert a corresponding output field in the alarm text and specify the tag that returns the search key for the text list.

###### Requirements

- A text list is created.
- The "HMI alarms" editor is open
- The alarm is selected

###### Output of a text list value in an alarm text

To insert an output field for a value from a text list in the alarm text, proceed as follows:

1. Place the cursor at the required position in the alarm text.
2. Select "Insert text list output field" command from the shortcut menu.
3. Select the text list under "Text list".
4. Open the object list under "Tag" and select the tag that returns the search key for the text list.

   You can also create the tag in the object list.
5. Define the length of the output field under "Format".

   Configure an output field of sufficient size so that the complete text from the text list is displayed in the alarm.
6. Click on the ![Output of a text list value in an alarm text](images/70512612363_DV_resource.Stream@PNG-de-DE.png) icon to save your entries.

   WinCC inserts a placeholder for the output field into the alarm text:

   ""&lt;textlist: n, [textlist name]&gt;" whereby n = text string length.

###### Editing output field properties

To edit the properties of an output field, proceed as follows:

- Double-click on the output field in the alarm text and edit the settings.

###### Deleting text list from the alarm text

To delete an output field from the alarm text, proceed as follows:

- Select the output field in the alarm text and then select the "Delete" command from the shortcut menu.

---

**See also**

[Formatting alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#formatting-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring Analog Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-analog-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Output of a tag value in the alarm text (Basic Panels, Panels, Comfort Panels, RT Advanced)](#output-of-a-tag-value-in-the-alarm-text-basic-panels-panels-comfort-panels-rt-advanced)

##### Editing system events (Panels, Comfort Panels, RT Advanced)

###### Editing system events

When you open the "System events" tab in the "HMI alarms" editor, WinCC prompts you to import or update the system events. Import the system events and specify the display period. You cannot delete or create new system events. You can only edit the alarm text with system events.

###### Requirements

- You have imported the system events.

###### Specifying the display period

To determine the display period, proceed as follows:

1. Double-click "Runtime settings" in the project navigation.
2. Enter a value under "Alarms &gt; System events &gt; Display period".

   This value specifies a time in seconds during which the system events are displayed on the HMI device. If you want to display system events permanently, enter "0".

###### Changing the alarm text

To change the alarm text of a system event, follow these steps:

1. Open the "HMI alarms" editor and then click the "System events" tab.
2. Select the system event that you want to edit.

1. Change the alarm text under "Properties &gt; Properties &gt; Properties &gt; General" in the Inspector window.

> **Note**
>
> If you change an alarm text for a system event that contains a placeholder, leave the number of placeholders unchanged. A placeholder may be a "%1".

###### Configuring event-driven tasks

The "Incoming" event is available for certain system events, depending on the HMI device. To configure event-driven tasks, proceed as follows:

1. Select the system event.

2. Select "Properties &gt; Properties &gt; Incoming" in the inspector window and configure a function list.

---

**See also**

[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[System events (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm Logging in WinCC (RT Professional)](#alarm-logging-in-wincc-rt-professional)
  
[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Alarm Logging in WinCC (Basic Panels)](#alarm-logging-in-wincc-basic-panels)
  
[System events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Editing controller alarms (Panels, Comfort Panels, RT Advanced)

###### Introduction

Controller alarms are configured in STEP 7. Controller alarms are available in WinCC running in a STEP 7 environment.

In WinCC you only edit the properties of controller alarms that are specific to an HMI device. Different properties of a controller alarm can be edited, depending on the HMI device and PLC.

You can filter the displayed controller alarms for your project using the display classes that were configured on the PLC for controller alarms.

> **Note**
>
> **"Automatic update" option**
>
> When "Automatic update" is set for controller alarms for the connection to the S7-1500 controller, you cannot edit the properties of the respective controller alarms. The controller alarms are not displayed in the "HMI alarms" editor in this case.
>
> If text-list tags are used in controller alarms, "Automatic update" must be active during the compile.

###### Requirements

- The connection was established to the PLC.
- Alarms were configured in STEP 7.

###### Editing controller alarms

Proceed as follows to edit controller alarms:

1. Double-click "HMI alarms" in the project navigation.

   The "HMI alarms" editor is opened.
2. Open the "Controller alarms" tab.
3. Select the alarm that you want to change in the work area.
4. Make your changes. Depending on the HMI device, it may not be possible to display or enable some of the controller alarm properties.

###### Editing SIMATIC S7 alarms

You can edit these controller alarms in the STEP 7 alarm configuration system. Proceed as follows:

1. Select the alarm that you want to change in the work area.
2. Select "Open in alarm editor of the PLC" from the shortcut menu.

   The STEP 7 alarm configuration system is opened.
3. Make your changes.

###### Filtering the controller alarm using display classes

To filter controller alarms by display classes, proceed as follows:

1. Click "Runtime settings &gt; Alarms" in the project navigation under your HMI device.

   One or several connections to a PLC are shown in "Contoller alarms".
2. Select the display classes whose controller alarms you want to display for the connection.

> **Note**
>
> **Controller alarms after a basic panel device exchange**
>
> For the controller alarms (PLC monitoring alarms, program alarms or system alarms) to be displayed after a device replacement ("Device view &gt; Change device") from a Basic Panel to a Comfort Panel, Mobile Panel or WinCC RT Advanced, you need to activate the "Display classes" setting for the respective connections under "Runtime settings &gt; Alarms &gt; Controller alarms".

###### Result

Only those controller alarms whose display class you have enabled for your HMI device will be displayed on the "Controller alarms" tab of the "HMI alarms" editor.

---

**See also**

[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm Logging in WinCC (Basic Panels)](#alarm-logging-in-wincc-basic-panels)
  
[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Alarm Logging in WinCC (RT Professional)](#alarm-logging-in-wincc-rt-professional)
  
[Basics of communication (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-communication-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Enabling system-defined controller alarms (Panels, Comfort Panels, RT Advanced)

###### Enabling system-defined controller alarms

To activate system-defined controller alarms of the type "SIMATIC S7 diagnostic alarm" for your HMI device, follow these steps:

1. Select "Runtime settings &gt; Alarms" in the project navigation.

   The alarm settings open.
2. Under "System events" select the check box "S7 diagnostic alarms (number)".
3. To display the system events with alarm text, activate "Show text".
4. To display these alarms in Runtime, configure an alarm view or an alarm window that displays alarms from the "Diagnosis Events" alarm class.

**Note**

For HMI devices with small display units, specify to display only the alarm number for system-defined controller alarms.

**Note**

The procedure described above can only be applied to connections with SIMATIC S7-300/400 controllers for system-defined controller alarms of the type "SIMATIC S7 diagnostic alarm".

---

**See also**

[System-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#system-defined-controller-alarms-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm view for the S7 diagnostic alarms (Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-the-s7-diagnostic-alarms-panels-comfort-panels-rt-advanced)

#### Configure alarms (RT Professional)

This section contains information on the following topics:

- [Configuring alarm blocks (RT Professional)](#configuring-alarm-blocks-rt-professional)
- [Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional)
- [Configuring discrete alarms (RT Professional)](#configuring-discrete-alarms-rt-professional)
- [Configuring user alarms (RT Professional)](#configuring-user-alarms-rt-professional)
- [Configuring alarm text (RT Professional)](#configuring-alarm-text-rt-professional)
- [Editing system events (RT Professional)](#editing-system-events-rt-professional)
- [Editing controller alarms (RT Professional)](#editing-controller-alarms-rt-professional)
- [Configure operator input alarms (RT Professional)](#configure-operator-input-alarms-rt-professional)
- [Configuring Operator Input Alarms for an Alarm View (RT Professional)](#configuring-operator-input-alarms-for-an-alarm-view-rt-professional)

##### Configuring alarm blocks (RT Professional)

This section contains information on the following topics:

- [Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
- [Configuring Alarm Text Blocks (RT Professional)](#configuring-alarm-text-blocks-rt-professional)
- [Setting up flashing alarm text blocks (RT Professional)](#setting-up-flashing-alarm-text-blocks-rt-professional)

###### Alarm Text Block Basics (RT Professional)

###### Introduction

An alarm display is made up of alarm text blocks. Each alarm text block corresponds to one column in the table in the alarm view.

There are three groups of alarm text blocks:

- System blocks

  System blocks contain system data, such as date, time, alarm number and status.
- User text blocks

  User text blocks contain the alarm text with the description of the cause of a fault and additional text with information, for example, the location of a fault.
- Parameter blocks

  Parameter blocks are used to link the alarms to process values, such as current fill levels, temperatures or speeds. You can configure up to 10 parameter blocks per alarm.

###### Configuring Alarm Text Blocks

You enable and edit the alarm text blocks on the "Alarm text blocks" tab. To display alarm text blocks in an alarm view, select the alarm text blocks to be displayed and logged from the enabled alarm text blocks in the "Screens" editor.

###### Text length

The maximum text length of a user text block is 255 characters.

The text length of a parameter block can be configured as follows:

- Controller alarms: up to 32 characters

  Set the length of the parameter block to 32 characters to ensure that all characters will be displayed.
- Other alarm procedures: up to 255 characters

  > **Note**
  >
  > **"Status" and "Acknowledgement status" system blocks**
  >
  > The status texts of the alarms are displayed in the "Status" system block. These alarm blocks must be configured so that they are long enough to display the status texts in full.

###### Flashing

An alarm to be acknowledged or single alarm text blocks can be displayed as flashing in Runtime. They have to meet the following requirements:

- The "Flashing" property must be enabled in the alarm class of the alarm. You configure this property on the "Alarm classes" tab.
- The "Flashing" option is enabled in the "Alarm text block" area under "General" in the Inspector window for alarm text blocks that should flash.

###### Alignment

On the "Alarm text blocks" tab, you define whether the alarm text block should be right-justified, left-justified or centered in an alarm view column.

###### Format

For certain alarm text blocks, you can choose between different display formats.

---

**See also**

[Configuring Alarm Text Blocks (RT Professional)](#configuring-alarm-text-blocks-rt-professional)
  
[Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional-1)
  
[Configuring alarm text (RT Professional)](#configuring-alarm-text-rt-professional)
  
[Parameter output in the analog alarm (RT Professional)](#parameter-output-in-the-analog-alarm-rt-professional)
  
[Configuring Operator Input Alarms for an Alarm View (RT Professional)](#configuring-operator-input-alarms-for-an-alarm-view-rt-professional)
  
[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting up flashing alarm text blocks (RT Professional)](#setting-up-flashing-alarm-text-blocks-rt-professional)
  
[Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

###### Configuring Alarm Text Blocks (RT Professional)

###### Introduction

An alarm is made up of configured alarm text blocks. You enable the alarm text blocks for an HMI device on the "Alarm text blocks" tab. Then you select, from the enabled alarm text blocks for each alarm view, which enabled alarm text blocks are to be displayed and logged.

###### Requirements

- The "HMI alarms" editor is open.
- The "Alarm text blocks" tab is selected.

###### Activating alarm text blocks

1. Select the "System blocks", "User text blocks" or "Parameter blocks" tab for the alarm text blocks.
2. Select the alarm text block to be displayed on your HMI device.
3. In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Blocks &gt; Enable".
4. In the Inspector window under "Properties &gt; Properties &gt; General &gt; Settings", define the display name of the alarm text block.
5. Under "Properties &gt; Properties &gt; General &gt; Blocks" in the Inspector window, define the text length and alignment of the alarm text block in the alarm view column.
6. In the Inspector window under "Properties &gt; Properties &gt; Settings &gt; Format", select the format of the alarm text block. This option is not available for every alarm text block.

**Note**

The write-protected names of the alarm text blocks stored in the system are displayed in the "Name in the Alarms editor" column under "Properties &gt; Properties &gt; General &gt; Settings". This column is available for the "User text blocks" and "Parameter blocks" tags.

Based on the "Name in the Alarms editor" column, you recognize the relationship between the display names of the alarm blocks in Runtime and the designations in the "Alarms" editor, even if the display names of the alarm text blocks were changed.

###### Result

The alarm text blocks are enabled and displayed in the Inspector window of the alarm view in the "Screens" editor.

###### Disabling alarm text blocks

1. Select the tabs for the alarm text blocks that you want to disable.
2. Disable the alarm text blocks that you no longer want to use for alarm view and alarm logging.
3. Repeat the process for every alarm text block that you no longer want to display.

---

**See also**

[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
  
[Description of the System Blocks (RT Professional)](#description-of-the-system-blocks-rt-professional)
  
[Setting up flashing alarm text blocks (RT Professional)](#setting-up-flashing-alarm-text-blocks-rt-professional)
  
[Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

###### Setting up flashing alarm text blocks (RT Professional)

###### Introduction

Whether or not an alarm text block flashes in Runtime depends on the alarm class of the alarm. The alarm class determines if the alarms it contains flash when acknowledgment is pending.

###### Requirements

- The alarms blocks are enabled for the HMI device.
- The alarms blocks are enabled for the respective alarm.
- The alarm is assigned to an alarm class with a state machine, which specifies whether or not the contained alarms are to flash.
- The alarm text blocks are activated in the alarm view.
- The "Alarm text blocks" tab is selected.

###### Procedure

To configure flashing for alarm text blocks in Runtime, proceed as follows:

1. Select the alarm text block to flash in Runtime from the subordinate tabs on the "Alarm text blocks" tab.
2. In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Blocks &gt; Flash".
3. Repeat this step for all the alarm text blocks that you want to flash in Runtime.

###### Result

These alarm text blocks flash in Runtime when the alarm is queued for acknowledgment.

---

**See also**

[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
  
[Configuring Alarm Text Blocks (RT Professional)](#configuring-alarm-text-blocks-rt-professional)
  
[Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Configuring analog alarms (RT Professional)

This section contains information on the following topics:

- [Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional-1)
- [Parameter output in the analog alarm (RT Professional)](#parameter-output-in-the-analog-alarm-rt-professional)

###### Configuring analog alarms (RT Professional)

###### Introduction

In the "HMI alarms" editor, you can configure analog alarms and define their properties. You can also configure analog alarms in the "HMI tags" editor.

###### Requirement

- The "HMI alarms" editor is open.
- The Inspector window is open.

###### Procedure

To configure an analog alarm, proceed as follows:

1. Click the "Analog Alarms" tab.
2. To create a new analog alarm, double-click in the table on "&lt;Add&gt;".

   A new analog alarm is created.
3. To configure the alarm, select "Properties &gt; Properties &gt;General" in the Inspector window:

   - You can always change the object name of the alarm.
   - Select the alarm class and the alarm group, if necessary.
4. To display the CPU number or PLC that sends the alarm, enter this under "Connection to the PLC". This option is only active if you have enabled the "CPU/PLC number" alarm text block on the "Alarm text blocks &gt; System blocks" tab.
5. In the Inspector window, select the tag that triggers the alarm under "Properties &gt; Properties &gt; Trigger". Do not use trigger tags for anything else.
6. To configure the alarm text, select "Properties &gt; Properties &gt; Alarm texts".

   - To enter the alarm text, select "Alarm text".
   - To create additional alarm texts, select "Additional texts".
   - Use the functions of the shortcut menu to format text on a character-by-character basis and to insert output fields for system or alarm parameters.

**Note**

You can only enter additional text in the rows that you have enabled as user text blocks on the "Alarm text blocks" tab.

###### Defining limits

1. Select the analog alarm to which you want to assign the limits.
2. At the bottom of the work area, click &lt;Add&gt; under "Limits for analog alarm".

   ![Defining limits](images/111888922251_DV_resource.Stream@PNG-en-US.png)

   ![Defining limits](images/111888922251_DV_resource.Stream@PNG-en-US.png)
3. To use a **constant** as limit:

   - In the Inspector window, click the button ![Defining limits](images/14170060427_DV_resource.Stream@PNG-de-DE.png) under "Properties &gt; Properties &gt; Trigger &gt; Value" and select "Constant".
   - Enter the required limit value.
4. To use a **tag** as limit:

   - In the Inspector window, click the button ![Defining limits](images/14170060427_DV_resource.Stream@PNG-de-DE.png) under "Properties &gt; Properties &gt; Trigger &gt; Value" and select "HMI tag".

     ![Defining limits](images/111888926731_DV_resource.Stream@PNG-en-US.png)

     ![Defining limits](images/111888926731_DV_resource.Stream@PNG-en-US.png)
   - Click the ![Defining limits](images/21587487883_DV_resource.Stream@PNG-de-DE.png)button. The object list opens.
   - Select the tag.
5. Select the trigger mode in the "Mode" field.

   - "Equal to limit": The alarm is triggered when the limit is reached.
   - "Not equal to limit": The alarm is triggered when the limit is no longer reached.
   - "High limit violation": The alarm is triggered if the limit is exceeded.
   - "Low limit violation": The alarm is triggered if the limit is undershot.
6. You can create additional limits for the alarm, if necessary.

**Note**

If the object included in the selection does not yet exist, create it in the object list and change its properties later.

**Note**

If a process value fluctuates around the limit, the alarm associated with this fault may be triggered multiple times. In this case, configure a deadband or delay time.

###### Optional settings for analog alarms

**Setting the delay time**

To display an alarm after a delay, proceed as follows:

1. Select the analog alarm.
2. In the Inspector window, select "Properties &gt; Properties &gt; Trigger".
3. Enter a time period under "Delay". The trigger condition must be fulfilled within this time for the alarm to be triggered.

**Setting the deadband**

Proceed as follows to enter a tolerance range for the arrival or departure of an alarm:

1. Select the limit to which the deadband is to be assigned.
2. In the Inspector window, select "Properties &gt; Properties &gt; Trigger".
3. Under "Deadband &gt; Mode", select the change to the alarm status to include in the evaluation of the deadband.
4. Enter a constant under "Deadband &gt; Value".
5. To define the deadband value as a percentage of the limit, activate the "%" check box.

**Saving the status of the alarm**

To save the alarm states to a tag, proceed as follows:

1. Select the analog alarm.
2. Under "Properties &gt; Properties &gt; Status" in the Inspector window, select the tag and the bit that triggers saving of the incoming/outgoing alarm states and the acknowledgment request.

**Setting the priority**

To set the priority, proceed as follows:

1. Select the analog alarm.
2. Select a value between 0 and 16 under "Properties &gt; Properties &gt; General &gt; Priority" in the Inspector window, .

   If you filter the alarm view by priority, the alarm with priority 0 will appear at the top.

**Creating an infotext**

1. Select the analog alarm.
2. Select "Properties &gt; Properties &gt; Tooltip" in the Inspector window and enter a text.

**Configuring event-driven tasks**

To configure event-driven tasks, such as a loop-in alarm, follow these steps:

1. Select the analog alarm.
2. Select "Properties &gt; Events" in the Inspector window and configure a new function list for the relevant event.

---

**See also**

[Configuring acknowledgment of the alarm annunciator (RT Professional)](#configuring-acknowledgment-of-the-alarm-annunciator-rt-professional)
  
[Analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)
  
[Configuring alarm groups (RT Professional)](#configuring-alarm-groups-rt-professional)
  
[Configuring Alarm Text Blocks (RT Professional)](#configuring-alarm-text-blocks-rt-professional)
  
[Configuring alarm text (RT Professional)](#configuring-alarm-text-rt-professional)
  
[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)
  
[Parameter output in the analog alarm (RT Professional)](#parameter-output-in-the-analog-alarm-rt-professional)
  
[Configuring loop-in alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-loop-in-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarms in the "HMI tags" Editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarms-in-the-hmi-tags-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)

###### Parameter output in the analog alarm (RT Professional)

###### Introduction

To display system or alarm parameters, insert an appropriate output field in an analog alarm.

- "Limit", "Deadband" or "Current value" can be selected as alarm parameters.
- The following system blocks can be selected as system parameters:

  - Application
  - User name
  - Computer name
  - Comment

###### Requirement

- The "HMI alarms" editor is open.
- The analog alarm is selected.

###### Procedure

To output parameters in alarm texts, proceed as follows:

1. Place the cursor at the required position in the alarm text.
2. To output an alarm parameter, select "Insert parameter field" from the shortcut menu.

   -OR-

   To output a system parameter, select "Insert system parameter" from the shortcut menu.
3. Specify the display type, length, number of decimal places and alignment of the output field for the alarm parameter.

   To display leading zeros in the output field, enable "Leading zeros".
4. Click ![Procedure](images/70512612363_DV_resource.Stream@PNG-de-DE.png) to save your entries.

WinCC inserts a placeholder for the output field into the alarm text:

- For alarm parameter: "&lt;tag: n, [###]&gt;", where n = text length in characters.

- For system parameters; "&lt;name of the system parameter&gt;"

  > **Note**
  >
  > If you test a project using the simulator, the output field values are not output in the alarm texts.

###### Deleting parameter from the alarm text

To delete an output field from the alarm text, proceed as follows:

- Select the output field in the alarm text and then select the "Delete" command from the shortcut menu.

> **Note**
>
> The sequence of output fields in the alarm text depends on the language. The sequence of the Runtime language is used for logging alarms to a CSV log file.
>
> Changing the tag of an output field in one language causes the modified output field to appear at the end of the alarm text in all other languages. This changes the sequence of the output fields in the log.

> **Note**
>
> Not only the "Insert system parameter" shortcut menu command can be used to output a system parameter in an alarm text. You can also use a format instruction that begins and ends with the "@" symbol. To output a system parameter in an alarm text using a format instruction, enter one of the following format instructions at the desired location in the alarm text:
>
> - @101%s@ = Application
> - @102%s@ = User name
> - @100%s@ = Computer name
> - @103%s@ = Comment

---

**See also**

[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
  
[Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional-1)
  
[Configuring alarm text (RT Professional)](#configuring-alarm-text-rt-professional)

##### Configuring discrete alarms (RT Professional)

This section contains information on the following topics:

- [Configuring discrete alarms (RT Professional)](#configuring-discrete-alarms-rt-professional-1)
- [Parameter output in discrete alarms (RT Professional)](#parameter-output-in-discrete-alarms-rt-professional)

###### Configuring discrete alarms (RT Professional)

###### Introduction

Discrete alarms triggered by the PLC indicate status changes in a plant. They indicate the opened or closed state of a valve, for example.

The following sections describes the configuration procedures in the "HMI alarms" editor. You can also configure discrete alarms in the "HMI tags" editor.

###### Requirements

- The "HMI alarms" editor is open.
- The Inspector window is open.

###### Procedure

To configure a discrete alarm, proceed as follows:

1. Click the "Discrete alarms" tab.
2. To create a new discrete alarm, double-click on "&lt;Add&gt;" in the table.

   A new discrete alarm is created.
3. To configure the alarm, select "Properties &gt; Properties &gt;General" in the Inspector window:

   - You can always change the object name of the alarm.
   - Select the alarm class and the alarm group, if necessary.
   - To display the CPU number or PLC that sends the alarm, enter these in the "Connection" area. This option is only active if you have enabled the "CPU/PLC number" alarm text block on the "Alarm text blocks" tab.
4. Select "Properties &gt; Properties &gt; Trigger" in the Inspector window to select the tag and the bit that triggers the alarm. Note the following information:

   - Use data types "Bool" "USInt", "UInt", or "UDInt".
   - Use trigger tag bits only for alarms.
   - Do not use trigger tags for anything else.
   - The input and output area of a PLC tag is unsuitable as trigger.

> **Note**
>
> If the object does not yet exist in the selection list, create it directly in the object list and change its properties later.

> **Note**
>
> The trigger bit is not incremented automatically if you generate a discrete alarm by copying an alarm text to a new table row. Avoid any redundant use of the trigger bit.

> **Note**
>
> Note the method used to count bits in the utilized PLC when specifying the bit. For more information, refer to the "Communication" section in the PLC Online Help.

1. Select "Mode" to specify whether to trigger the alarm at a rising or falling edge.
2. To configure the alarm text, select "Properties &gt; Properties &gt; Alarm texts".

   - To enter the alarm text, select "Alarm text".
   - To create additional alarm texts, select "Additional texts".
   - Use the functions of the shortcut menu to format text on a character-by-character basis and to insert parameter output fields.

**Note**

You can only enter additional text in the rows that you have enabled as user text blocks on the "Alarm text blocks" tab.

###### Result

The discrete alarm is created.

###### Additional settings for discrete alarms

**Creating an infotext**

To configure a tooltip for the alarm, follow these steps:

1. Select the discrete alarm.
2. Select "Properties &gt; Properties &gt; Infotext" in the Inspector window and enter the required tip.

**Enabling discrete alarm parameters**

To output process values to an output field in the alarm text, assign corresponding tags to the parameter blocks. Proceed as follows:

1. Select the alarm.
2. In the Inspector window, click "Properties &gt; Properties &gt; Alarm parameters".
3. Enter a value for the alarm parameter, or select a tag.
4. You can enter several alarm parameters.

   Insert the activated process values as selection box into an alarm text, or show them as parameter block in the alarm view.

**Note**

To show the process values as parameter blocks, the parameter blocks must be enabled in the alarm view.

You only edit parameters that you have enabled under "Parameter blocks" on the "Alarm text blocks" tab.

**Saving the alarm status**

To save the alarm states to a tag, proceed as follows:

1. Select the discrete alarm.
2. Under "Properties &gt; Properties &gt; Status" in the Inspector window, select the tag and the bit that triggers saving of the incoming/outgoing alarm states and the acknowledgment request.

**Configuring event-driven tasks**

To configure event-driven tasks, such as a loop-in alarm, follow these steps:

1. Select the discrete alarm.
2. Select "Properties &gt; Events" in the Inspector window and configure a new function list for the relevant event.

---

**See also**

[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)
  
[Configuring acknowledgment of the alarm annunciator (RT Professional)](#configuring-acknowledgment-of-the-alarm-annunciator-rt-professional)
  
[Configuring loop-in alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-loop-in-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Parameter output in discrete alarms (RT Professional)](#parameter-output-in-discrete-alarms-rt-professional)
  
[Alarms in the "HMI tags" Editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#alarms-in-the-hmi-tags-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)
  
[Configuring alarm groups (RT Professional)](#configuring-alarm-groups-rt-professional)
  
[Configuring Alarm Text Blocks (RT Professional)](#configuring-alarm-text-blocks-rt-professional)
  
[Configuring alarm text (RT Professional)](#configuring-alarm-text-rt-professional)
  
[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)

###### Parameter output in discrete alarms (RT Professional)

###### Introduction

To display system or alarm parameters, insert an appropriate output field in the analog alarm.

- You can select the parameters configured in "Properties &gt; Properties &gt; Alarm parameters" for use as alarm parameters.
- The following system blocks can be selected as system parameters:

  - Application
  - User name
  - Computer name
  - Comment

###### Requirement

- The "HMI alarms" editor is open.
- The discrete alarm is selected.

###### Procedure

To output parameters in alarm texts, proceed as follows:

1. Place the cursor at the required position in the alarm text.
2. To output an alarm parameter, select "Insert parameter field" from the shortcut menu.

   -OR-

   To output a system parameter, select "Insert system parameter" from the shortcut menu.
3. Select the parameter.
4. Moreover, you can specify the following data for alarm parameters:

   - The tag that provides the parameter values.

     The tag configured for the parameter under "Properties &gt; Properties &gt; Alarm parameters" is entered by default. If you select a different tag, WinCC updates the parameter configuration in "Properties &gt; Properties &gt; Alarm parameters" accordingly.
   - Display type, length, number of decimal places and alignment of the output field
   - To display leading zeros in the output field, enable "Leading zeros".
5. Click ![Procedure](images/70512612363_DV_resource.Stream@PNG-de-DE.png) to save your entries.

**Note**

If you test a project using the simulator, the output field values are not output in the alarm texts.

> **Note**
>
> The sequence of the tag output fields in the alarm text depends on the language. The sequence of the Runtime language is used for logging alarms to a CSV log file.
>
> Changing the tag of an output field in one language causes the modified output field to appear at the end of the alarm text in all other languages. This changes the sequence of the output fields in the log.

> **Note**
>
> Not only the "Insert system parameter" shortcut menu command can be used to output a system parameter in an alarm text. You can also use a format instruction that begins and ends with the "@" symbol. To output a system parameter in an alarm text using a format instruction, enter one of the following format instructions at the desired location in the alarm text:
>
> - @101%s@ = Application
> - @102%s@ = User name
> - @100%s@ = Computer name
> - @103%s@ = Comment

---

**See also**

[Configuring discrete alarms (RT Professional)](#configuring-discrete-alarms-rt-professional-1)
  
[Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
  
[Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional-1)
  
[Configuring alarm text (RT Professional)](#configuring-alarm-text-rt-professional)

##### Configuring user alarms (RT Professional)

This section contains information on the following topics:

- [Configuring user alarms (RT Professional)](#configuring-user-alarms-rt-professional-1)
- [Parameter output in user alarms (RT Professional)](#parameter-output-in-user-alarms-rt-professional)
- [Example: Configuring a trigger for a user alarm (RT Professional)](#example-configuring-a-trigger-for-a-user-alarm-rt-professional)
- [Example: Defining alarm parameters for a user alarm (RT Professional)](#example-defining-alarm-parameters-for-a-user-alarm-rt-professional)

###### Configuring user alarms (RT Professional)

###### Introduction

User alarms serve to to indicate operator actions in Runtime. User alarms are triggered by means of alarm number. For other custom applications, configure user alarms that are triggered in Runtime by means of scripts.

###### Requirement

- The "HMI alarms" editor is open.
- The Inspector window is open.

###### Procedure

To configure user alarms, proceed as follows:

1. Click the "User alarms" tab.
2. To create a new user alarm, double-click "&lt;Add&gt;" in the table.

   A new user alarm is created.
3. To configure the alarm, select "Properties &gt; Properties &gt;General" in the Inspector window:

   - You can always change the object name of the alarm.
   - Select the alarm class and the alarm group, if necessary.
   - To display the CPU number or PLC that sends the alarm, enter these in the "Connection" area. This option is only active if you have enabled the "CPU/PLC number" alarm text block on the "Alarm text blocks" tab.
4. Click "Alarm texts" in the Inspector window and configure the alarm text.

   - Enter the alarm text.
   - To create additional alarm texts, select "Additional texts".
   - You can insert output fields or or additional text into the alarm text.

**Note**

You can only enter additional text in the rows that you have enabled as user text blocks on the "Alarm text blocks" tab.

###### Result

The user alarm is created.

###### Additional settings for user alarms

**Creating a tooltip**

To configure a tooltip for the alarm, follow these steps:

1. Select the user alarm.
2. Select "Properties &gt; Properties &gt; Tooltip" in the Inspector window and enter your text.

**Saving the alarm status**

To save the alarm states to a tag, proceed as follows:

1. Select the user alarm.
2. Select "Properties &gt; Properties &gt; Status" in the Inspector window and select the tag and the bit that triggers saving of the incoming/outgoing alarm states and the acknowledgment request.

**Configuring event-driven tasks**

To configure event-driven tasks, proceed as follows:

1. Select the user alarm.
2. Select "Properties &gt; Events" in the Inspector window and configure a new function list for the relevant event.

---

**See also**

[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)
  
[Configuring acknowledgment of the alarm annunciator (RT Professional)](#configuring-acknowledgment-of-the-alarm-annunciator-rt-professional)
  
[User alarms (RT Professional)](#user-alarms-rt-professional)
  
[Configuring acknowledgment (RT Professional)](#configuring-acknowledgment-rt-professional)
  
[Configuring alarm blocks (RT Professional)](#configuring-alarm-blocks-rt-professional)
  
[Configuring Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a trigger for a user alarm (RT Professional)](#example-configuring-a-trigger-for-a-user-alarm-rt-professional)

###### Parameter output in user alarms (RT Professional)

###### Introduction

To display system or alarm parameters, insert an appropriate output field in the user alarm.

- The following system blocks can be selected as system parameters:

  - Application
  - User name
  - Computer name
  - Comment
- Alarm parameters are configured in the script that you use to trigger a user alarm in runtime.

###### Requirement

- The "HMI alarms" editor is open.
- The user alarm is selected.

###### Procedure

To output parameters in alarm texts, proceed as follows:

1. Place the cursor at the required position in the alarm text.
2. To output an alarm parameter, select "Insert parameter field" from the shortcut menu.

   -OR-

   To output a system parameter, select "Insert system parameter" from the shortcut menu.
3. Select the parameter.
4. Click ![Procedure](images/70512612363_DV_resource.Stream@PNG-de-DE.png) to save your entries.

**Note**

If you test a project using the simulator, the output field values are not output in the alarm texts.

> **Note**
>
> The sequence of the tag output fields in the alarm text depends on the language. The sequence of the Runtime language is used for logging alarms to a CSV log file.
>
> Changing the tag of an output field in one language causes the modified output field to appear at the end of the alarm text in all other languages. This changes the sequence of the output fields in the log.

> **Note**
>
> Not only the "Insert system parameter" shortcut menu command can be used to output a system parameter in an alarm text. You can also use a format instruction that begins and ends with the "@" symbol. To output a system parameter in an alarm text using a format instruction, enter one of the following format instructions at the desired location in the alarm text:
>
> - @101%s@ = Application
> - @102%s@ = User name
> - @100%s@ = Computer name
> - @103%s@ = Comment

---

**See also**

[Example: Configuring a trigger for a user alarm (RT Professional)](#example-configuring-a-trigger-for-a-user-alarm-rt-professional)
  
[Example: Defining alarm parameters for a user alarm (RT Professional)](#example-defining-alarm-parameters-for-a-user-alarm-rt-professional)

###### Example: Configuring a trigger for a user alarm (RT Professional)

###### Task

In the following example, you configure a user alarm that is triggered by a button in runtime.

To do this, you configure a script at the "Click" event of this button. This script calls up an alarm number and sets the associated alarm to the status "Incoming".

###### Requirements

- The "HMI alarms" editor is open.
- The Inspector window is open.
- A screen with an alarm view and a button is open.

###### Procedure

1. You configure a user alarm in the "HMI alarms" editor.

   ![Procedure](images/88263601163_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88263601163_DV_resource.Stream@PNG-en-US.png)

   The user alarm has the alarm number "17" in this case.
2. You configure the following script in the screen at the "Click" event of the button:

Sub onClick(byVal item)

Dim UserAlarm

Dim ID_UA

Dim State_UserAlarm

ID_UA = "17"

State_UserAlarm = "5"

Set UserAlarm = HMIRuntime.Alarms(ID_UA)

UserAlarm.State = state_UserAlarm

UserAlarm.Comment = "empty Comment"

UserAlarm.UserName = "Max Mustermann"

UserAlarm.Create "MyApplication"

End Sub

###### Result

If the user clicks on this button in runtime, the configured user alarm is displayed in the alarm view.

---

**See also**

[Configuring user alarms (RT Professional)](#configuring-user-alarms-rt-professional-1)
  
[Example: Defining alarm parameters for a user alarm (RT Professional)](#example-defining-alarm-parameters-for-a-user-alarm-rt-professional)

###### Example: Defining alarm parameters for a user alarm (RT Professional)

###### Task

In the following example, you configure a user alarm that is triggered by a button in runtime. For the user alarm, you define alarm parameters to be output in the alarm text.

To do this, configure the C system function "TriggerOperatorEvent" at the "Click" event of this button. This system function calls an alarm number and transfers the following parameters:

- Tag name as parameter 1 in the alarm text
- Start value of the tag as parameter 2 in the alarm text
- End value of the tag as parameter 3 in the alarm text

> **Note**
>
> **Alarm parameters in the script**
>
> WinCC has a range of functions for defining alarm parameters, for example the "MSRTCreateMsgInstanceWithCommentPlus" function of the runtime API interface.

###### Requirements

- A screen with an alarm view and a button is open.
- The user alarm with alarm number 0x001 has been configured and uses alarm parameters 1 - 3 in the alarm text.
- Tag "HMI_Tag_1" of the type "Integer" has been configured and connected.

###### Procedure

1. You configure the following script in the screen at the "Click" event of the button:

Void SCFunction_1()

(

int a, b;

a = GetTagDWord ("HMI_Tag_1"); // old value

SetTagDWord("HMI_Tag_1", 100);

b = GetTagDWord ("HMI_Tag_1"); // new value

TriggerOperatorEvent(0x001, 1, "HMI_Tag_1", 0, a, b, "myComment");

}

###### Result

If the user clicks on this button in runtime, the configured user alarm is displayed in the alarm view. The tag name is output as parameter 1, and the start and end values of the tags as parameters 2 and 3.

---

**See also**

[Parameter output in user alarms (RT Professional)](#parameter-output-in-user-alarms-rt-professional)
  
[TriggerOperatorEvent (RT Professional)](C%20scripting%20%28RT%20Professional%29.md#triggeroperatorevent-rt-professional)
  
[MSRTCreateMsgInstanceWithCommentPlus (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#msrtcreatemsginstancewithcommentplus-rt-professional)
  
[Example: Configuring a trigger for a user alarm (RT Professional)](#example-configuring-a-trigger-for-a-user-alarm-rt-professional)

##### Configuring alarm text (RT Professional)

###### Introduction

The alarm text for an alarm is made up of the alarm text, additional texts and output fields. The alarm text and additional texts are user text blocks. You can use up to 10 user text blocks for an alarm.

Each alarm text contains up to 255 characters and any number of output fields.

###### Requirements

- The "HMI alarms" editor is open.
- You have enabled user text blocks on the "Alarm text blocks" tab.
- An alarm has been created.

###### Procedure

Proceed as follows to assign additional user text blocks to the alarm text for an alarm:

1. Select the alarm that you want to edit on the relevant tab.
2. To enter the alarm text, select "Properties &gt; Properties &gt; Alarm text" in the Inspector window.
3. You can also add output fields to the alarm text.
4. To enter additional alarm texts, select "Properties &gt; Properties &gt; Alarm text &gt; Additional text" in the Inspector window.

   Enter more additional texts according to which user text blocks you enabled under "User text blocks" on the "Alarm text blocks" tab.

   > **Note**
   >
   > Use the scroll buttons ![Procedure](images/13049706123_DV_resource.Stream@PNG-de-DE.png) to view text that is not fully visible in the text box. The additional text lines are displayed.

###### Result

You have configured the alarm text with additional texts for this alarm. To display it in Runtime, enable these user text blocks in an alarm view.

---

**See also**

[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
  
[Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional-1)
  
[Configuring discrete alarms (RT Professional)](#configuring-discrete-alarms-rt-professional-1)
  
[Parameter output in the analog alarm (RT Professional)](#parameter-output-in-the-analog-alarm-rt-professional)

##### Editing system events (RT Professional)

###### Introduction

System events can only be changed to a limited extent. You cannot delete or create new system events.

###### Requirements

- You have imported the system events.
- The "HMI alarms" editor is open.

###### Procedure

To configure system events, proceed as follows:

1. Click the "System events" tab.
2. Select the system event that you want to edit.
3. Change the editable properties in the Inspector window.
4. Select the system event that you want to edit.
5. Change the editable properties in the Inspector window.

###### Configuring event-driven tasks

To configure event-driven tasks, proceed as follows:

- To configure a function list for the relevant event, select "Properties &gt; Events".

---

**See also**

[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[System events (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-panels-comfort-panels-rt-advanced-rt-professional)

##### Editing controller alarms (RT Professional)

###### Introduction

Controller alarms are configured in STEP 7. Controller alarms are available in WinCC running in a STEP 7 environment.

In WinCC you only edit the properties of controller alarms that are specific to an HMI device. Different properties of a controller alarm can be edited, depending on the HMI device and PLC.

You can filter the displayed controller alarms for your project using the display classes that were configured on the PLC for controller alarms.

> **Note**
>
> **"Automatic update" option**
>
> When "Automatic update" is set for controller alarms for the connection to the S7-1500 controller, you cannot edit the properties of the respective controller alarms. The controller alarms are not displayed in the "HMI alarms" editor in this case.
>
> If text-list tags are used in controller alarms, "Automatic update" must be active during the compile.

###### Requirements

- The connection was established to the PLC.
- Alarms were configured in STEP 7.

###### Editing controller alarms

Proceed as follows to edit controller alarms:

1. Double-click "HMI alarms" in the project navigation.

   The "HMI alarms" editor is opened.
2. Open the "Controller alarms" tab.
3. Select the alarm that you want to change in the work area.
4. Make your changes. Depending on the HMI device, it may not be possible to display or enable some of the controller alarm properties.

###### Editing SIMATIC S7 alarms

You can edit these controller alarms in the STEP 7 alarm configuration system. Proceed as follows:

1. Select the alarm that you want to change in the work area.
2. Select "Open in alarm editor of the PLC" from the shortcut menu.

   The STEP 7 alarm configuration system is opened.
3. Make your changes.

###### Filtering the controller alarm using display classes

To filter controller alarms by display classes, proceed as follows:

1. Click "Runtime settings &gt; Alarms" in the project navigation under your HMI device.

   One or several connections to a PLC are shown in "Contoller alarms".
2. Select the display classes whose controller alarms you want to display for the connection.

> **Note**
>
> **Controller alarms after a basic panel device exchange**
>
> For the controller alarms (PLC monitoring alarms, program alarms or system alarms) to be displayed after a device replacement ("Device view &gt; Change device") from a Basic Panel to a Comfort Panel, Mobile Panel or WinCC RT Advanced, you need to activate the "Display classes" setting for the respective connections under "Runtime settings &gt; Alarms &gt; Controller alarms".

###### Result

Only those controller alarms whose display class you have enabled for your HMI device will be displayed on the "Controller alarms" tab of the "HMI alarms" editor.

---

**See also**

[Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Sending a complete alarm from the controller to the HMI device and automatic update (RT Professional)](#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-rt-professional)
  
[Basics of communication (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-communication-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Configure operator input alarms (RT Professional)

###### Introduction

You have the option of triggering an operator input alarm for the operation in the process. The configuration of an operator input alarm depends on the operated object and on the type of operation.

For the operation of some objects, for example the input of a value in an I/O field or an list field, the property "Operator input log" can be activated at the objects. The layout of the alarm cannot be edited in the operator input log. The Operator Actions Report contains the value before the operation in the process value block 2, and the changed value process value block 3.

The property "Request motive" specifies whether the motif will be logged by operator for an operation. By enabling the option the operator can enter the motive (reason) of the operation as alarm after an operation in a dialog. The Operator Actions Report is logged in the alarm system. The motive as displayed as comment to the operator input alarm in the historical alarm list (long-term). In the comment dialog, the old value and the new are only displayed for the "12508141".

###### Requirement

- The "Screens" editor is open.
- An I/O field is created.
- Each object is associated with a tag.

###### Procedure

1. Select the I/O field.
2. Click "Properties &gt; Properties &gt; Security" in the Inspector window.
3. To use operator input for the object, select the option "Log &gt; Operator Actions Report".
4. If you want to log the operation motive, enable the property "Request motive".

###### Result

The configured operator input alarm is triggered when the user performs an action on the I/O field in Runtime. When you operate the object, a dialog opens in Runtime in which the operator can enter a text.

---

**See also**

[List box (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#list-box-rt-professional)
  
[Symbolic I/O field (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#symbolic-io-field-rt-professional)
  
[Combo box (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#combo-box-rt-professional)
  
[Scroll bar (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#scroll-bar-rt-professional)

##### Configuring Operator Input Alarms for an Alarm View (RT Professional)

###### Introduction

Operator input alarms for the alarm view are preconfigured system alarms. Manage system alarms using the "HMI alarms" editor. In the "Screens" editor, configure the trigger conditions for operator input alarms for the alarm view.

###### Requirement

- You have imported the system alarms from the HMI device.
- The "Screens" editor is open.
- An "Alarm view" object has been created.
- Alarm text blocks are activated in the "HMI alarms" editor.

###### Procedure

To configure operator input alarms for an alarm view, proceed as follows:

1. Select the alarm view.
2. In the Inspector window, click "Properties &gt; Properties &gt; Operator input alarms".
3. Activate the operator action at the alarm view for which an operator input alarm is to be output.

   The alarm number of the preconfigured operator input alarm for this operator action is displayed in the "Alarm number" output field.
4. To output another alarm for this operator action, enter the alarm number of this alarm.
5. To specify the columns to display in the operator input alarm, click the ![Procedure](images/22421895819_DV_resource.Stream@PNG-de-DE.png) button in "Alarm text blocks".

   A dialog opens.
6. To enable the alarm text blocks to be output with the operator input alarm, select "Alarm text blocks".
7. Under "Alarm group of operator input alarm", specify the alarm text blocks to be output with the system alarm. Under "Output as", define whether the content of the alarm text block should be output as text or as a value.

**Note**

You will find the system alarm and its alarm number on the "System alarms" tab in the "HMI alarms" editor.

###### Result

The configured operator input alarm is displayed when the user performs an action on the alarm view in Runtime.

---

**See also**

[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)

#### Configuring loop-in alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

A Loop-In-Alarm is configured to change to your screen that contains the relevant information for the error that has occurred.

> **Note**
>
> You configure the screen that contains information about the error that occurred. No standard screens are available that are automatically called depending the selected error alarm.

##### Requirement

- The screen called by the Loop-In-Alarm has been created.
- The "HMI alarms" editor is open.

##### Procedure

To configure a Loop-In-Alarm for an alarm, proceed as follows:

1. Click the tab that contains the alarm for which you want to configure the Loop-In-Alarm.
2. Select the alarm.
3. In the Inspector window, select "Properties &gt; Events &gt; Loop-In-Alarm".
4. Select the "ActivateScreen" system function.
5. Select the screen to be called by the Loop-In-Alarm as its parameter.

   ![Procedure](images/72310099851_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72310099851_DV_resource.Stream@PNG-en-US.png)

**Note**

To configure the Loop-In-Alarm for an alarm view with an "alarm line" format, use a button with the following system functions:

- "EditAlarm" for HMI devices with keys
- "AlarmViewEditAlarm" for HMI devices without keys

The system functions trigger the "Loop-In-Alarm" event. The alarm line has no buttons.

##### Result

If you select an alarm in the alarm view in Runtime and click on the "Loop-In-Alarm" button, a screen is opened with information on the selected alarm.

Even if multiple alarms are selected, exactly one alarm requiring acknowledgment is acknowledged (provided it requires acknowledgment) when the "Loop-In-Alarm" button is pressed for the first time. The system functions stored for the "Loop-In-Alarm" alarm event are always executed, regardless of whether the alarm requires acknowledgment or not.

The next time the "Loop-In-Alarm" button is pressed, only the system functions stored for the "Loop-In-Alarm" alarm event are executed.

> **Note**
>
> If no Loop-In-Alarm is configured for the selected alarm, pressing the "Loop-In-Alarm" button has no effect.

---

**See also**

[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Using the Alarm Window, Alarm View (Panels, Comfort Panels, RT Advanced)](#using-the-alarm-window-alarm-view-panels-comfort-panels-rt-advanced)
  
[Basic alarm view, using the alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basic-alarm-view-using-the-alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
  
[Alarm view (RT Professional)](#alarm-view-rt-professional)
  
[Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional-1)
  
[Configuring discrete alarms (RT Professional)](#configuring-discrete-alarms-rt-professional-1)
  
[Overview of alarm configuration tasks (Basic Panels)](#overview-of-alarm-configuration-tasks-basic-panels)

#### Alarms in the "HMI tags" Editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

In WinCC, you can create and edit discrete and analog alarms, including the trigger tags, in the "HMI tags" editor.

> **Note**
>
> If you delete, move or copy objects in the "HMI tags" editor, the changes also take effect in the "HMI alarms" editor.

###### Requirements

The "HMI tags" editor is open.

###### Procedure

To configure a discrete alarm, proceed as follows:

1. To create a tag, click on "&lt;Add&gt;" in the table at the top of the work area.

   A new tag is created.
2. Configure an internal or external tag as required.

   - Use the data types "Int" or "UInt" to select an HMI tag.
   - When you select a PLC tag, use the data types "Int" or "Word". The input and output area of a PLC tag is unsuitable as trigger.
3. Select the tag at the top of the work area.
4. Click on "&lt;Add&gt;" in the table on the "Discrete alarms" tab at the bottom of the work area.

   A new discrete alarm is created for the tag. If you have selected the incorrect data type, the tag will be marked in the discrete alarm.
5. Configure the discrete alarm in the Inspector window:

   - Enter the alarm text under "Properties &gt; Properties &gt; General &gt; Alarm text".

     You can also insert output fields into the alarm text.
   - Select an alarm class.
   - Select the trigger bit of the tag that triggers the discrete alarm under "Properties &gt; Trigger".
6. You can create additional discrete alarms to monitor the tags.

**Note**

A tag is monitored using only one alarm type. You should therefore create either analog alarms **or** discrete alarms for a tag.

###### Result

The configured discrete alarms are created in the "HMI tags" editor and displayed in the "HMI alarms" and "HMI tags" editors.

---

**See also**

[Configuring analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-analog-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of alarm configuration tasks (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-configuration-tasks-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Parameter output in the analog alarm (RT Professional)](#parameter-output-in-the-analog-alarm-rt-professional)
  
[Working with Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Configuring analog alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

In WinCC, create the discrete and analog alarms, including the trigger tags, in the "HMI tags" editor. You can also edit the alarms as in the "HMI alarms" editor. You can create up to two range values for a tag. You monitor these limits with analog alarms.

###### Requirements

The "HMI tags" editor is open.

###### Procedure

To configure an analog alarm in the "HMI tags" editor, proceed as follows:

1. To create a tag, click on "&lt;Add&gt;" in the table at the top of the work area.

   A new tag is created.
2. Configure an internal or external tag as required.
3. In the Inspector window, configure the range values of the tags under "Properties &gt; Properties &gt; Range":

   - Select whether to use a "Constant" or an "HMI tag" as limit value for your range values. The object list opens when you select "HMI tag". Select the tag you want to use.

![Procedure](images/70513582091_DV_resource.Stream@PNG-en-US.png)

1. Click the "Analog Alarms" tab at the bottom of the work area.

   Create an analog alarm for both range values.
2. Select an analog alarm and configure it in the Inspector window:

   - Enter the alarm text under "Properties &gt; Properties &gt; General &gt; Alarm text".
   - You can also insert output fields into the alarm text.
   - You can change the default alarm class.
3. Configure the analog alarms as in the "HMI alarms" editor.
4. Complete the configuration of all analog alarms.

**Note**

A tag is monitored using only one alarm type. You should therefore create either analog alarms **or** discrete alarms for a tag.

###### Result

The configured analog alarms are created in the "HMI tags" editor and displayed in the "HMI alarms" and "HMI tags" editors.

---

**See also**

[Configuring discrete alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-discrete-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Parameter output in the analog alarm (RT Professional)](#parameter-output-in-the-analog-alarm-rt-professional)
  
[Configuring analog alarms (RT Professional)](#configuring-analog-alarms-rt-professional-1)
  
[Working with Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

### Configuring the Outputting of Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of configuring alarm output (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-configuring-alarm-output-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Reporting Alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#reporting-alarms-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of configuring alarm output (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Steps to complete when configuring alarm output

You configure the alarm output in WinCC in the following steps:

1. Create alarm view

   Use the display and control objects in the "Screens" editor to display alarms in Runtime. You can also configure an alarm view for logged alarms.
2. Configure acknowledgment

   In the "Screens" editor, you can set the operator action that will trigger the acknowledgment.
3. Configure reporting

   You can create reports in the "Reports" editor to print alarms in Runtime. In the "Scheduler", "Screens", "HMI alarms" or "HMI tags" editors, you define when and how the printing of a report is triggered.

   > **Note**
   >
   > Device dependency
   >
   > Reporting and logging are not available for all HMI devices.

   > **Note**
   >
   > Note that only ASCII characters are supported when printing alarms directly in Runtime.

##### Additional configuration tasks

Additional tasks may be necessary for configuring alarm views, depending on the requirements of your project:

1. Setting up authorizations

   To make sure only authorized operators process the alarms, assign authorizations for the alarm view and the function keys of the HMI device.
2. Configuring the filtering of the alarm view

   You configure the filtering of the alarms in Runtime in the "Screens" editor. You can also configure alarm views that only display selected alarms.
3. Configure operator input alarms

   Configure the operator input alarms on the operator controls of the HMI device in the "Screens" editor. A preconfigured operator input alarm is output for an operator action. An operator input is, e.g. the acknowledgment of an alarm.

---

**See also**

[Configuring the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Reporting Alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#reporting-alarms-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Displaying Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring an alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring an alarm indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-indicator-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring alarm filtering (Panels, Comfort Panels, RT Advanced)](#configuring-alarm-filtering-panels-comfort-panels-rt-advanced)
- [Displaying Logged Alarms (Panels, Comfort Panels, RT Advanced)](#displaying-logged-alarms-panels-comfort-panels-rt-advanced)

##### Displaying Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Options for displaying alarms on the HMI device

WinCC offers the following options for displaying alarms on the HMI device:

- Alarm view

  The alarm view is configured in a screen. More than one alarm can be displayed simultaneously, depending on the configured size. You can configure multiple alarm views with different contents.
- Alarm window

  The Alarm window is configured in the "Global screen" editor. The alarm window can display multiple alarms at the same time, depending on the configured size. An event can trigger closing and reopening of the alarm window. To hide it during configuration, create an alarm window on its own level.

###### Additional signals

- Alarm indicator

  The alarm indicator is a configurable, graphical icon. When an alarm comes in, the alarm indicator is displayed on the HMI device. You configure the alarm indicator in the "Global screen" editor.

  The alarm indicator has two states:

  - Flashing: At least one alarm that requires acknowledgment is pending.
  - Static: The alarms are acknowledged but at least one of them has not gone out yet.

    The alarm indicator also displays the number of pending alarms according to the HMI device.
- E-mail notification

  To inform someone other than the operator, such as an engineer, when an alarm with a specific alarm class arrives, assign the alarm class to an e-mail address.

  > **Note**
  >
  > **Device dependency**
  >
  > E-mail notification is not available for all HMI devices.
- System functions

  You can configure a list of functions for the event associated with an alarm. These functions must be executed in Runtime when the event occurs.

  Use system functions for alarms in WinCC to control the alarm view or the alarm window other than via the toolbar.

###### Displaying the predefined alarm classes in Runtime

The following table shows the symbols used to display the predefined alarm classes in the alarm view:

| Alarm class | Displayed icon |
| --- | --- |
| "Diagnosis Events" | S7 |
| "Errors" | ! |
| "System" | $ |
| "Warnings" | &lt;No symbol&gt; |

---

**See also**

[Configuring an alarm view for active alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-active-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-indicator-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring alarm filtering (Panels, Comfort Panels, RT Advanced)](#configuring-alarm-filtering-panels-comfort-panels-rt-advanced)
  
[Displaying Logged Alarms (Panels, Comfort Panels, RT Advanced)](#displaying-logged-alarms-panels-comfort-panels-rt-advanced)
  
[Overview of configuring alarm output (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-configuring-alarm-output-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Configuring an alarm view for active alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-active-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring an alarm view for the S7 diagnostic alarms (Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-the-s7-diagnostic-alarms-panels-comfort-panels-rt-advanced)
- [Configuring an alarm view for logged alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-for-logged-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

###### Configuring an alarm view for active alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

Current alarms are displayed in Runtime in an alarm view or alarm window.

###### Requirement

- A screen is open in the "Screen" editor.
- The "Tools" task card is open.

###### Configuring alarms for the alarm view

To specify the alarms that will be shown in the alarm view, proceed as follows:

1. Insert an "Alarm view" object from the "Tools" task card into the screen.
2. Select the alarm view.

   - In the Inspector window, select "Properties &gt; Properties &gt; General &gt; View &gt; Current alarm states".

     Set whether to display alarms with and/or without mandatory acknowledgment.

     ![Configuring alarms for the alarm view](images/88275309067_DV_resource.Stream@PNG-en-US.png)

     ![Configuring alarms for the alarm view](images/88275309067_DV_resource.Stream@PNG-en-US.png)
   - To display all alarms in the alarm buffer, activate "Alarm buffer".

     ![Configuring alarms for the alarm view](images/88275340555_DV_resource.Stream@PNG-en-US.png)

     ![Configuring alarms for the alarm view](images/88275340555_DV_resource.Stream@PNG-en-US.png)
3. In the table, activate the alarm classes to be displayed in the alarm view.
4. Under ""Properties &gt; Properties &gt; View &gt; Control tag for display area", define the tag that returns the date as of which the alarms will be displayed.

   ![Configuring alarms for the alarm view](images/88276760459_DV_resource.Stream@PNG-en-US.png)

   ![Configuring alarms for the alarm view](images/88276760459_DV_resource.Stream@PNG-en-US.png)

**Note**

**Device dependency**

The "Control tag for display area" property is not available for all HMI devices.

###### Configuring the layout of the alarm view

To specify how the alarms are shown in the alarm view, proceed as follows.

1. Under "Properties &gt; Properties &gt; Layout &gt; Settings &gt; Lines per alarm" in the Inspection window, specify the number of lines to display for each alarm.
2. In "Properties &gt; Properties &gt; View", select the control elements that are available on the HMI device.
3. Configure the columns under "Properties &gt; Properties &gt; Columns":

   - Under "Visible columns" select the columns to be output in the alarm view.
   - Under "Properties Column", define the properties of the columns.
   - Under "Sort", select the sorting order of the alarms.

     ![Configuring the layout of the alarm view](images/88275336075_DV_resource.Stream@PNG-en-US.png)

     ![Configuring the layout of the alarm view](images/88275336075_DV_resource.Stream@PNG-en-US.png)
4. Activate or deactivate the "Show selection color" option under "Properties &gt; Properties &gt; Appearance &gt; Alarms".

   ![Configuring the layout of the alarm view](images/170291194123_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the layout of the alarm view](images/170291194123_DV_resource.Stream@PNG-en-US.png)

**Note**

Select the "Edit" command in the shortcut menu for the alarm view to activate the alarm view. You can set the column width and position in active mode. To enable the alarm view, set the zoom factor to 100 %.

The alarm view is deactivated as soon as you deselect the object in the screen.

###### Result

Alarms of various alarm classes are output in the alarm view during runtime.

---

**See also**

[Displaying Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
  
[Displaying Logged Alarms (Panels, Comfort Panels, RT Advanced)](#displaying-logged-alarms-panels-comfort-panels-rt-advanced)

###### Configuring an alarm view for the S7 diagnostic alarms (Panels, Comfort Panels, RT Advanced)

###### Introduction

To display S7 diagnostic alarms, configure an alarm view or alarm window for the predefined "Diagnosis Events alarm class. Activate the diagnostic alarms accordingly in the Runtime settings of your HMI device.

> **Note**
>
> **Device dependency**
>
> - The "Diagnosis Events" alarm class is not available for all HMI devices.
> - System-defined controller alarms of the type "SIMATIC S7 diagnostic alarm" can be activated for your HMI device only for connections with a SIMATIC S7-300/400 controller.

> **Note**
>
> **Using system diagnostics view and/or system diagnostics window**
>
> As soon as a system diagnostics view or a system diagnostics window in available in the HMI project, the alarm texts for the screen objects are downloaded for system diagnostics and used there. Therefore, the option "Runtime settings &gt; Alarms &gt; System alarms &gt; Show alarm text" has no effect when system diagnostics view or system diagnostics window and is always considered enabled. In this case the size of the Runtime file cannot be reduced by enabling the option.

###### Requirements

- An alarm view or alarm window is configured in the "Screens" editor
- A connection to a SIMATIC S7-300/400 controller has been established.

###### Configuring the display of S7 diagnostic alarms

To configure the display of S7 diagnostic alarms, follow these steps:

1. Select "Runtime settings &gt; Alarms" in the project navigation.
2. Under "System events" select the check box "S7 diagnostic alarms (number)".
3. To display the S7 diagnostic alarms with text, activate "With event text".
4. Open the screen with the alarm view and select the alarm view.
5. In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Display &gt; Alarm class "Diagnosis Events".

   ![Configuring the display of S7 diagnostic alarms](images/88303002763_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the display of S7 diagnostic alarms](images/88303002763_DV_resource.Stream@PNG-en-US.png)
6. Continue to configure the alarm view as for the display of current alarms.

###### Result

In Runtime the alarm view displays the S7 diagnostic alarms of the controller.

---

**See also**

[Configuring an alarm view for active alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-active-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Enabling system-defined controller alarms (Panels, Comfort Panels, RT Advanced)](#enabling-system-defined-controller-alarms-panels-comfort-panels-rt-advanced)

###### Configuring an alarm view for logged alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

In Runtime, logged alarms are displayed in an alarm view or alarm window.

###### Requirements

- An alarm view or alarm window is configured in the "Screens" editor
- An alarm log was created in the "Log" editor.
- The alarms are assigned the "loggable" attribute in the "HMI alarms" editor.

###### Configuring an alarm view for logged alarms

To configure an alarm view for logged alarms, proceed as follows:

1. Open the screen with the alarm view and select the alarm view.
2. In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Alarm log".
3. Click the "...." button and select the alarm log.
4. Continue to configure the alarm view as for the display of current alarms.

###### Result

In Runtime, the logged alarms are output in the alarm view.

##### Configuring an alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

The alarm window displays current alarms. The alarm window is configured in the "Global screen" editor. The alarm window is not assigned to any screen. Depending on the configuration the alarm window is opened when an alarm that belongs to a specific alarm class is active. Depending on the configuration, it is not closed until the alarm is acknowledged. The HMI device can still be used, even if alarms are pending and displayed. An alarm window is displayed and configured like an alarm view.

To hide an alarm window during configuration, create it on its own level.

###### Requirement

- The "Global Screen" editor is open.
- The "Tools" task card is displayed.
- The Inspector window is open.

###### Procedure

Proceed as follows to configure an alarm window:

1. Insert an "Alarm window" object from the "Tools" task card into the global screen.
2. Configure the alarm window like an alarm view.
3. Under "Properties &gt; Properties &gt; Mode &gt; Window" in the Inspector window, select how the alarm window reacts and is operated in Runtime.

   - Activate "Modal" if the alarm window is to retain the focus in Runtime after a screen change.

     This option is important, as switching back and forth between the screen and different windows with &lt;Ctrl+TAB&gt; is not supported.

###### Result

During runtime, the alarms of the selected alarm class are displayed in the alarm window.

---

**See also**

[Displaying Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm view for active alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-active-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)

##### Configuring an alarm indicator  (Basic Panels, Panels, Comfort Panels, RT Advanced)

###### Introduction

The alarm indicator uses a warning triangle to indicate that alarms are pending or require acknowledgment. If an alarm of the configured alarm class occurs, the alarm indicator is displayed.

The alarm indicator has two states:

- Flashing: At least one alarm that requires acknowledgment is pending.
- Static: At least one of the acknowledged alarms has not gone out yet.

During configuration, specify whether Runtime has to open an alarm window when you operate the alarm indicator.

###### Requirement

- The "Global Screen" editor is open.
- The "Tools" task card is open.
- The Inspector window is open.

###### Procedure

Proceed as follows to configure the alarm indicator:

1. Insert the "Alarm view" object from the "Tools" task card into the work area.
2. Select the alarm indicator.
3. Under "Properties &gt; Properties &gt; General" in the Inspector window, select the alarm classes to be displayed by the alarm view.

   Specify whether to display pending and/or acknowledged alarms in the alarm view.

   ![Procedure](images/111891212171_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111891212171_DV_resource.Stream@PNG-en-US.png)
4. Under "Properties &gt; Event", assign the system function "ShowAlarmWindow" to an event of the alarm view.

**Note**

If you have configured a permanent area in the screen or template, do not position the alarm window and alarm view in the vicinity of the permanent area. Otherwise, the alarm window and the alarm view will not be displayed in Runtime. However, the permanent area is not visible in the "Global screen" editor.

###### Result

The alarm view is displayed if alarms from the selected alarm class are pending or need to be acknowledged in Runtime. The alarm window opens when the user operates the alarm view.

---

**See also**

[Displaying Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced)

##### Configuring alarm filtering (Panels, Comfort Panels, RT Advanced)

###### Introduction

You can filter the display of alarms in the enhanced alarm view. The criterion is always a character string. There are two ways to filter the alarm view:

- A fixed criterion is configured in WinCC.

  In Runtime, all alarms that contain the complete character string in the alarm text are displayed.
- You filter the alarm view in Runtime.

  In Runtime, a filter tag sets the relevant character string in the alarm view by means of an I/O field, e.g. as described below.

  The filter affects the display in the alarm view. All alarms in the alarm buffer are retained.

###### Requirement

- The alarm view has been configured.
- The screen with the alarm view is open.
- The Inspector window is open.

###### Configuring filters for a fixed character string

1. Select the alarm view.
2. In the Inspector window, select "Properties &gt; Properties &gt; Alarm filter".
3. Enter a filter string in "Filter string".

   ![Configuring filters for a fixed character string](images/88303055371_DV_resource.Stream@PNG-en-US.png)

   ![Configuring filters for a fixed character string](images/88303055371_DV_resource.Stream@PNG-en-US.png)

###### Result

Only those alarms are displayed in Runtime that contain the complete character string from the filter in the alarm text.

###### Configuring filters for a variable character string

1. Select the alarm view.
2. In the Inspector window, select "Properties &gt; Properties &gt; Filter".
3. Select a tag from "Filter tag". The tag must be of the "String" type.
4. In the screen, configure an I/O field for entering the filter string in Runtime.

   - In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Format &gt; Display format &gt; String".
   - To link the I/O field to the alarm view, select "Process" to set the filter tag you selected for the alarm view.

     ![Configuring filters for a variable character string](images/74925742731_DV_resource.Stream@PNG-en-US.png)

     ![Configuring filters for a variable character string](images/74925742731_DV_resource.Stream@PNG-en-US.png)

###### Result

If you enter a string in the I/O field in Runtime, the alarm view only displays alarms that contain the complete string in their alarm text.

If a permanently configured character string and a filter tag were configured, the alarms will be filtered in Runtime according to the content of the filter tag. If the filter tag is blank, the permanently configured character string is used as the filter.

> **Note**
>
> Filtering is not possible for the following alarm views:
>
> - Simple alarm view
> - Alarm line
> - Alarm window
> - Alarm view for logged alarms

---

**See also**

[Displaying Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Filtering alarms (Panels, Comfort Panels, RT Advanced)](#filtering-alarms-panels-comfort-panels-rt-advanced)
  
[Working with Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Displaying Logged Alarms (Panels, Comfort Panels, RT Advanced)

###### Introduction

You display logged alarms in Runtime in an alarm view. The alarm view shows the content of an alarm log.

###### Application

For example, you want to view information about the process at the end of a shift.

###### Requirements

- An alarm log has been created.
- A screen is open.
- The Inspector window is open.

###### Procedure

Proceed as follows to configure an alarm view to output an alarm log:

1. Configure an alarm view in a screen.
2. Under "Properties &gt; Properties &gt; General &gt; Display &gt; Alarm log"" in the Inspector window, select the required alarm log.

   You can always create a new alarm log.

###### Result

During runtime, the alarms logged in the selected alarm log appear in the Alarm view.

> **Note**
>
> In runtime, the alarm texts logged are not displayed but rather the alarm texts in the current project. The logged alarm texts are only intended for external evaluation of the log file.
>
> If the alarm log displayed was configured differently, the alarm texts displayed may not correspond with those logged.

---

**See also**

[Displaying Alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm view for active alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-active-alarms-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Displaying alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Configuring filters in the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-filters-in-the-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring Alarm Statistics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-statistics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring Alarm Alerts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-alerts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Displaying logged alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-logged-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring alarm export (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-export-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring alarm evaluation in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-evaluation-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Displaying alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Options for displaying alarms on the HMI device

WinCC offers the following options for displaying alarms on the HMI device:

- Alarm view for pending and outgoing alarms

  The alarm view is configured for a screen. More than one alarm can be displayed simultaneously, depending on the configured size. You can also configure multiple alarm views with different contents and in different screens. Use the "Historical alarm list (short-term)" and "Historical alarm list (long-term)" views to display outgoing alarms.
- Alarm view for statistical values

  The "Alarm statistics" view of the alarm view displays statistical information, such as the frequency and display duration of alarms.
- Status tag of an alarm group

  You can visualize the changing alarm states of an alarm group using the status tag of that alarm group. You can customize the display in the "Screens" editor.

###### Additional signals

- Alarm annunciator

  In addition to the alarm view, WinCC displays an alarm in the form of a visual or audible alarm in the plant. The alarm annunciator may be a hooter, or a warning lamp.
- System functions and scripts

  You can configure a list of functions for the event associated with an alarm. These functions must be executed in Runtime when the event occurs.

  To be able to control the alarm view other than via the toolbar, use system functions for alarms in WinCC.

---

**See also**

[Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Configuring filters in the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-filters-in-the-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Statistics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-statistics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Alerts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-alerts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Displaying logged alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-logged-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of configuring alarm output (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-configuring-alarm-output-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Bit assignment of status tag (RT Professional)](#bit-assignment-of-status-tag-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)
  
[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

Current, and logged alarms are displayed in the alarm view. Alarms from all alarm classes are displayed in an alarm view, if necessary. Configure the criteria for alarm filtering.

###### Requirement

- A screen is open.
- The "Tools" task card is open.

###### Procedure

To configure an alarm view, proceed as follows:

1. Insert an "Alarm view" object from the "Tools" task card into the screen.
2. Select the alarm view and click "Properties &gt; Properties &gt; General" in the Inspector window.

   - Under "Display &gt; Type", select the type of alarms you want to display as default in the alarm view.
   - Under "Display &gt; Display" select which alarms are displayed. This shows or hides the alarms to be suppressed in the display.
   - Double-click of the operator on an alarm in Runtime starts a specific action. Specify this action under "Display &gt; Double-click". If you want to trigger the Loop-In-Alarm not only using the "Loop-In-Alarm" button, select "Loop-In-Alarm".
   - Select the required time base under "Time base".

     ![Procedure](images/100529955083_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/100529955083_DV_resource.Stream@PNG-en-US.png)
3. To specify the appearance of the alarm view, select "Properties &gt; Properties &gt; Appearance" in the Inspector window.
4. To specify the appearance of the headers, content, and table grid in the alarm view, select "Properties &gt; Properties &gt; Table" .

   - To specify the visualization of selected alarms in Runtime, select "Properties &gt; Properties &gt; Table &gt; Table - Select".
   - To specify the sorting method for alarms in Runtime, select "Properties &gt; Properties &gt; Table &gt; Table - Sorting".
5. To specify the sort order of alarms in Runtime, select "Properties &gt; Properties &gt; Alarm list" .

###### Configuring alarm blocks for the alarm view

1. To configure alarm blocks for the alarm view, deactivate the "Accept project settings" option in the Inspector window under "Properties &gt; Properties &gt; Blocks".
2. To use an alarm block in the alarm view, activate the alarm block in the "Selected" column.
3. To give an alarm block its own label for the column heading in the alarm view, change the text in the "Label" column.
4. To change the text length and alignment of an alarm block in the alarm view column, change the entries in the "Length" and "Alignment" columns.
5. To activate the flashing of an alarm block in Runtime, activate the check box in the "Flashing" column.
6. To display the content of an alarm block in the Alarm view column as text, symbol or both, select the corresponding entry in the "Content as" column.
7. To display the title of an alarm block in the Alarm view column as text, symbol or both, select the corresponding entry in the "Title as" column.
8. Specify the format of an alarm block in the "Format" column. This option is not available for every alarm text block.
9. To display an alarm block as a column in the alarm view, activate the column corresponding to the alarm block under "Properties &gt; Properties &gt; Columns" in the "Visible" column.

**Note**

The display of the content as a symbol is not available for all alarm blocks. For an overview of the symbols that you can display in the contents of some system blocks, see "[Description of the System Blocks](#description-of-the-system-blocks-rt-professional)".

**Note**

The display of the title as a symbol is not available for all alarm blocks.

###### Configuring Alarm view columns

1. To define the arrangement of the columns of the alarm view, select a row in the Inspector window under "Properties &gt; Properties &gt; Columns". Use the arrow buttons to move the row to the desired position.
2. Specify the sort direction for each activated column in the "Sort direction" column.
3. Define the sort order in the "Sorting order" column by assigning the values "1" to "4".

**Note**

The sorting function is only active if a maximum of four columns are contained in the alarm view.

###### Configuring the toolbar and status bar in the alarm view

1. To specify the toolbar layout, select "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - General".
2. Select "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - Operator input elements", to enable the operator input elements to be included in the alarm view toolbar.
3. To specify the status bar layout, select "Properties &gt; Properties &gt; Status bar &gt; Status bar - General".
4. Select "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - Operator input elements", to enable the operator input elements to be included in the status bar of the alarm view.

###### Result

Alarms of various alarm classes are output in the alarm view during runtime. To change the view in Runtime, click the configured buttons on the alarm view toolbar.

---

**See also**

[Displaying alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring filters in the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-filters-in-the-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Alarm Statistics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-statistics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm Text Block Basics (RT Professional)](#alarm-text-block-basics-rt-professional)
  
[Configuring Alarm Text Blocks (RT Professional)](#configuring-alarm-text-blocks-rt-professional)
  
[Setting up flashing alarm text blocks (RT Professional)](#setting-up-flashing-alarm-text-blocks-rt-professional)
  
[Configuring the state texts of an alarm class (RT Professional)](#configuring-the-state-texts-of-an-alarm-class-rt-professional)
  
[Description of the System Blocks (RT Professional)](#description-of-the-system-blocks-rt-professional)

##### Configuring filters in the alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

WinCC supports the configuration of different filters for the alarm view:

- Standard filters

  The operator cannot access standard filters in Runtime. You can copy configured standard filter for use in other alarm views.
- Custom filters

  The operator can change the custom filter in Runtime. You are using custom filter only in a single alarm view.

###### Requirement

- The screen with the configured alarm view is open in the "Screens" editor.
- The Inspector window is open.

###### Procedure

1. Select the alarm view and click "Properties &gt; Properties &gt; Filter &gt; Alarm filter" in the Inspector window.
2. To configure a custom filter, click on the "Custom" tab.
3. Define one or more filters. For each filter, specify one or more filter criteria under "Expression" with condition and value.

   ![Procedure](images/72334259083_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72334259083_DV_resource.Stream@PNG-en-US.png)
4. To configure a standard filter, select the "Standard" tab.

   You can configure several standard filters and activate these for the respective alarm view.
5. Enter the name for the standard filter and a comment.
6. To configure the filter, select the criteria, conditions, and the value for the standard filter in the "Filter" dialog.

###### Filter by process values

You cannot enter text as the criterion for a process value. To filter by the text of a parameter block, or by the process tag represented, proceed as follows:

1. Insert this process value as the alarm text for a user text block in an alarm.
2. In Runtime, filter the alarms by the text in the "Alarm text" alarm text block using the ![Filter by process values](images/21863628043_DV_resource.Stream@PNG-de-DE.png) button.

In multi-station systems, make sure that contents displayed in the "Specify selection" dialog on a client have the same names on all servers.

###### Filter by time

When filtering by time, the start and stop values are not adjusted automatically when the time base of the alarm view is changed.

###### Example

At a PC location with time zone "UTC + 1h", the alarm view has the "Local time zone" time base. You should filter by the time 10:00 to 11:00. Convert the time base to "UTC". To display the same alarms as before, change the start or stop value of the filter to 9:00 and 10:00.

---

**See also**

[Displaying alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[SQL Statements for Filtering the Alarm View (RT Professional)](#sql-statements-for-filtering-the-alarm-view-rt-professional)
  
[Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Configuring Alarm Statistics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

The alarm statistics contain statistical calculations for the logged alarms in the alarm view. The alarm statistics also contain a selection of the configured alarm text blocks. If the contents are dynamic, the alarm text blocks display the data for the last incoming alarm. You can compile the alarm statistics columns individually.

The alarm statistics contain the following statistical calculations:

- Alarm rate

  The system counts how often an alarm with the status "Incoming" is included in the log. If the alarm number does not occur, this alarm number is not included in the statistics.
- Total display time of an alarm in seconds.

  The following periods between alarm states are available as calculation variables:

  - "Incoming/Incoming"(sum +/+),
  - "Incoming/Outgoing"(sum +/-)
  - "Incoming/Initial acknowledgment"(sum +/*1)
  - "Incoming/second acknowledgment"(sum +/*2)

  Each type of calculation can be represented in a column in the alarm statistics.
- Average display time of an alarm in seconds

  The following periods between alarm states are available as calculation variables:

  - "Incoming/Incoming"(mean value +/+),
  - "Incoming/Outgoing"(mean value +/-)
  - "Incoming/Initial acknowledgment"((mean value +/*1)
  - "Incoming/second acknowledgment"((mean value +/*2)

  There is one column in the alarm statistics for each type of calculation.

The calculation of the time of acknowledgment includes the "Acknowledged" alarm status. This status includes both an emergency acknowledgment and an acknowledgment by the PLC.

###### Requirement

- The "Screens" editor is open.
- You have created a screen with an alarm view.

###### Configuring the alarm statistics functions

Proceed as follows to configure the functions of the alarm statistics:

1. Select the alarm view and click "Properties &gt; Properties &gt; Alarm statistics - General" in the Inspector window.

   ![Configuring the alarm statistics functions](images/72334516491_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the alarm statistics functions](images/72334516491_DV_resource.Stream@PNG-en-US.png)
2. To limit the calculation period, activate the "Use time range" option under "Time range". Specify the frequency.
3. To define the maximum number of alarms to be processed in the alarm statistics, enter a value at "Data records &gt; Maximum number of data records".

   This setting requires the following conditions to be met:

   - The number of alarms in the calculation period exceeds the configured "Maximum number of data records which can be read".
   - The calculation period is not configured.
4. To output a warning when this number is exceeded, activate the "Warning when limit is reached" option.

###### Setting up the alarm statistics

Proceed as follows to set the columns of the alarm statistics:

1. Select the alarm view and click "Properties &gt; Properties &gt; Alarm statistics - Elements" in the Inspector window.

   ![Setting up the alarm statistics](images/72334658699_DV_resource.Stream@PNG-en-US.png)

   ![Setting up the alarm statistics](images/72334658699_DV_resource.Stream@PNG-en-US.png)
2. In the table, enable the alarm statistics columns that are to be displayed in Runtime.
3. To specify the arrangement of columns in the alarm view in Runtime, select a row in the Inspector window. Move the row to the selected location using the ![Setting up the alarm statistics](images/21441267595_DV_resource.Stream@PNG-de-DE.png) and ![Setting up the alarm statistics](images/70640328331_DV_resource.Stream@PNG-de-DE.png) buttons.

   The columns of the alarm statistics are displayed in Runtime in the same order as the rows are arranged in the Inspector window.
4. Specify the sort direction for each row in "Sort by".
5. Specify the sort order in "Sort order" by assigning values from 1 to 4.

**Note**

The sort function is only active if the alarm statistics view contains no more than four columns.

###### Result

In Runtime, the operator clicks the ![Result](images/21863635211_DV_resource.Stream@PNG-de-DE.png) button in the alarm view to view the "Alarm statistics".

> **Note**
>
> Alarms that have the "acknowledged" and "outgoing" states are only used for the calculation if a suitable alarm with "incoming" state was found in the amount of the result .
>
> If you acknowledge an alarm with single-mode acknowledgment or dual-mode acknowledgment only once, the "Incoming/first acknowledgment" and "Incoming/second acknowledgment" alarm states are used for the statistical calculation.
>
> If there is an alarm pending at the PLC and Runtime is disabled and enabled several times, the alarm is entered several times in the log with "incoming" status. The alarm will also be included multiple times in the evaluation.

> **Note**
>
> If the same alarm number with different text has been configured for the monitoring alarms, a single line per alarm number is displayed in the "Alarm statistics".
>
> The statistics evaluation for the " Alarm statistics" is done per alarm number, therefore only a single line is displayed for an alarm number in the "Alarm statistics" regardless of the alarm text.

---

**See also**

[Displaying alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Configuring Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Setting the Display Suppression Timeout (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-display-suppression-timeout-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring Automatic Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-automatic-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

###### Overview of Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

Suppress the display of alarms to avoid an excessive burden of information for the plant operator. If only selected alarms are shown, the operator will concentrate his attention on essential alarms.

###### Requirement

The "Show alarm" and "Hide alarm" buttons are configured in the alarm view.

###### Methods for suppressing alarm displays

There are two options for suppressing the display of incoming alarms:

- **Automatic display suppression**

  The alarms are displayed in line with the specific plant status. You can enter these plant states as display suppression masks in each alarm. The design engineer specifies the values for the plant states.

  To transfer the current plant status to the alarm system, create an alarm group with a display suppression tag. This display suppression tag returns the value of the plant states.

  Assign this alarm group the alarms that the system does not display in Runtime at specific plant states.

  Example:

  In the "Shutdown" plant status you want to suppress the display of alarms that normally occur in this status. The "Online connection to the PLC was dropped" alarm will only not be displayed during "Shutdown".

  > **Note**
  >
  > If you have specified a display suppression mask for an alarm that is not assigned to an alarm group, this alarm will not be suppressed in Runtime.
  >
  > Alarms with display suppression masks that are not allocated to any alarm group will not be suppressed in Runtime. To suppress the display of specific alarms in Runtime, you always have to assign these to an alarm group.

  > **Note**
  >
  > You only use display suppression tags only for custom alarm groups.
- **Manual display suppression**

  When necessary, the user suppresses the display of an alarm in Runtime using the "Hide alarm" button in the alarm view.

  The user displays the alarm again when necessary using the "Show alarm" button.

  The system displays the alarms again after a configurable time.

  To enable the reporting of manual display suppression, configure a corresponding user alarm that is triggered when the display is suppressed manually. Configure this user alarm in the alarm view as an operator input alarm for the "Suppress" operator action.

###### Properties of alarms whose display is suppressed

The following applies to alarms whose display is suppressed:

- In the following alarm view display modes, you can use the following buttons to show the alarms again:

  - Display "Current alarms"
  - Display "Historical alarm list" (short-term)
  - Display "Historical alarm list" (long-term)
- The alarms are recorded and displayed under the "Hidden alarms" display.
- The alarms are also logged.
- If an alarm annunciator is set up for these alarms, it will not be triggered.

**Manual display suppression**

The following properties apply only to alarms whose display is suppressed **manually**.

- The alarms are shown again after a set time.
- An alarm that requires acknowledgment is acknowledged by the manual suppression of its display.
- To enable the reporting of manual display suppression, configure a corresponding user alarm that is triggered when the display is suppressed manually.

**Automatic display suppression**

The following properties apply only to alarms whose display is suppressed **automatically**.

- The display suppression does not trigger an operator input alarm.
- The PLC acknowledges alarms that require acknowledgment.

  In the time while alarms requiring acknowledgment are suppressed, the PLC acknowledges the outgoing alarms. If an alarm does not have the "Outgoing" status, the PLC acknowledges it immediately.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Notice** |
  | **Forfeiture of acknowledgment requirement**  With automatic display suppression, alarms requiring acknowledgment no longer have to be acknowledged. You should therefore only use automatic display suppression for alarms that do not require operator actions during the configured plant states. |  |

###### Interaction

The two methods of suppressing alarm displays interact as follows:

- When an alarm is automatically suppressed, use the "Hide alarm" and "Show alarm" buttons to show and hide the alarm as required.
- You have manually suppressed the display of an alarm using the button "Hide alarm".

  When the plant status changes and the conditions for automatic suppression of this alarm display are not fulfilled, the alarm is displayed once more.

  The time defined as the display suppression duration must not have elapsed.
- You have suppressed the alarm manually with the "Hide alarm" button. The status that was defined for automatic display suppression using the display suppression tags occurs. After the specified display suppression timeout was triggered, the alarm nevertheless remains suppressed.

> **Note**
>
> **Hidden system diagnostic alarms**
>
> For hidden system diagnostic alarms, the alarm texts are not displayed in the list of hidden alarms.
>
> The list of hidden alarms merely displays the configuration data of the alarm and not a live view.
>
> To display active hidden system diagnostic alarms, you must adjust the filter for the online alarm list.

---

**See also**

[Setting the Display Suppression Timeout (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-display-suppression-timeout-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Automatic Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-automatic-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Displaying alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

###### Setting the Display Suppression Timeout (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

You can set the time after which manually-suppressed alarms should be automatically displayed once more in the alarm settings.

###### Requirements

- The project navigator is open.

###### Procedure

To set the alarm display suppression timeout, follow these steps:

1. Double-click "Runtime settings &gt; Alarms" in the project navigation.

   The alarm settings open.
2. Select "General &gt; Display suppression timeout" to configure the period during which a manually suppressed alarm remains hidden.

   30 minutes are preset.

   ![Procedure](images/88320196107_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88320196107_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Overview of Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring Automatic Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-automatic-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

###### Configuring Automatic Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

With automatic display suppression, the alarm is displayed in relation to the status of the PLC. You define the plant status that causes an alarm to be hidden. Configure automatic display suppression using the "HMI alarms" editor. You will need to create an alarm group with a displace suppression tag. In the alarm, you assign the plant statuses using the display suppression mask. The display suppression tag must assume the value of the display suppression mask for an alarm so that it is not displayed in Runtime.

###### Requirement

The "Show alarm" button is configured in the alarm view.

###### Requirements

- The "HMI alarms" editor is open.
- The "Alarm groups" tab is selected.
- Alarms are set up.
- The display suppression tag must exist.

###### Creasing an alarm group for display suppression

1. Double-click "Add" in the table.

   A new alarm group is created.
2. Enter a name for the new alarm group.
3. Select the display suppression tag under "Tags" in the Inspector window.

   ![Creasing an alarm group for display suppression](images/88321107211_DV_resource.Stream@PNG-en-US.png)

   ![Creasing an alarm group for display suppression](images/88321107211_DV_resource.Stream@PNG-en-US.png)

###### Creating a display suppression mask for the alarm

1. Select the alarm.
2. To select the alarm group for which you created the alarm suppression tag, select "Properties &gt; Properties &gt; General" in the Inspector window.

   ![Creating a display suppression mask for the alarm](images/72334990603_DV_resource.Stream@PNG-en-US.png)

   ![Creating a display suppression mask for the alarm](images/72334990603_DV_resource.Stream@PNG-en-US.png)
3. To enter the display suppression mask, select "Properties &gt; Properties &gt; Display suppression" in the Inspector window.

   ![Creating a display suppression mask for the alarm](images/72334995083_DV_resource.Stream@PNG-en-US.png)

   ![Creating a display suppression mask for the alarm](images/72334995083_DV_resource.Stream@PNG-en-US.png)

###### Result

The alarm is hidden when the value set in the display suppression mask is activated at the display suppression tag. This means that the alarm is hidden when the plant is in the specified status.

> **Note**
>
> Alarms with display suppression masks that are not allocated to any alarm group will not be suppressed in Runtime. You should therefore always assign alarms to an alarm group if you want to suppress them.
>
> If an alarm is hidden, it can be shown once again in Runtime by clicking the button "Show alarm".

---

**See also**

[Overview of Alarm Display Suppression (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-alarm-display-suppression-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the Display Suppression Timeout (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-display-suppression-timeout-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

##### Configuring Alarm Alerts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

In addition to the alarm view, WinCC also supports alarm indication in the plant by means of visual or audible signals. The alarm annunciator can be a horn or a warning lamp, for example. You can also display and acknowledge the alarm annunciator in a screen.

###### Requirements

- The "Alarm annunciator acknowledgment" button is configured in the alarm view.
- The "HMI alarms" editor is open.
- Alarms are set up.
- The Inspector window is open.
- Your plant is equipped with an alarm annunciator which is connected to a tag.

###### Configuring alarms for the alarm annunciator

1. Select the alarm that you want to display using an alarm annunciator.
2. In the Inspector window, select "Properties &gt; Alarm annunciator".
3. In the "Alarm classes" tab, select the alarm class of the alarms for the alarm annunciator.

   - To acknowledge the alarm annunciator via the "Alarm annunciator acknowledgment" button of the alarm view, activate "Acknowledge &gt; Alarm annunciator &gt; By means of "Acknowledge central annunciator" button" in the Inspector window.

     To switch off the alarm annunciator, use the "Alarm annunciator acknowledgment" button. The alarm is still pending in the alarm view.
   - To acknowledge the alarm via the alarm annunciator, select the tag to which the alarm annunciator is connected.

###### Configuring alarm annunciator in the screen

1. Open the screen in which you display the alarm annunciator.
2. For example, configure a circle and an associated button with the label "Alarm annunciator".
3. At the event "Click", configure the button that runs a VBS script with the method "QuitHorn".
4. Dynamize the background color of the circle with the tag to which the alarm annunciator is connected.

###### Result

If an alarm is displayed with the alarm annunciator in Runtime, the user acknowledges the alarm as follows depending on its configuration:

- Using an "Alarm annunciator acknowledgment" button in the alarm view
- Using the configured "Alarm annunciator" button

The user can recognize the status of the alarm annunciator from the background color of the circle.

---

**See also**

[Displaying alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring acknowledgment of the alarm annunciator (RT Professional)](#configuring-acknowledgment-of-the-alarm-annunciator-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

##### Displaying logged alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

An alarm view displays logged alarms in Runtime according to the configuration. The alarm view displays alarms from the log in the "Historical alarm list" (short-term) or "Historical alarm list" (long-term) display. The "Historical alarm list" (short-term) also displays the current alarms.

###### Requirement

- The "Historical alarm list (short-term)" and "Historical alarm list (long-term)" buttons are configured in the alarm view.
- The logged alarms are located on the local log server.
- The screen with the configured alarm view is open.
- The Inspector window is open.

###### Procedure

Proceed as follows to configure an "Historical alarm list" (short-term) or "Historical alarm list" (long-term) display:

1. Select the alarm view.
2. Select "Properties &gt; Properties &gt; General &gt; Active list &gt; "Historical alarm list" (short-term) or "Historical alarm list" (long-term) in the Inspector window.
3. Configure the alarm view similar to an alarm view for active alarms.

###### Result

In Runtime, you can view logged alarms using the "Historical alarm list (short-term)" or "Historical alarm list (long-term)" buttons. To visualize only alarms of the "Errors" alarm class or alarms at certain plant areas, you can filter or sort the logged alarms.

> **Note**
>
> In the "Historical alarm list" (short-term) display, the new incoming alarms are updated immediately. In the "Historical alarm list" (long-term), on the other hand, they are not. You cannot enter or view comments in the "Historical alarm list" (short-term). Comments can only be entered in the "Historical alarm list" (long-term).

---

**See also**

[Displaying alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

##### Configuring alarm export (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

To export alarms to a "*.csv" file in Runtime, the operator clicks on the ![Introduction](images/6233371915_DV_resource.Stream@PNG-de-DE.png) button in the alarm view.You can configure this function in the alarm view in the "Screens" editor.

###### Requirements

- The screen with the configured alarm view is open.
- The Inspector window is open.

###### Procedure

To configure the export of alarms, proceed as follows:

1. Select the alarm view and configure data export by selecting "Properties &gt; Properties &gt; Data export" in the Inspector window.

   - You can specify a custom file name and folder.
   - At "Scope", specify the data to be exported from the alarm view.
   - at "CSV format", specify the separator to use in the ".csv" file.
2. Select "Operator input in Runtime" to configure the function of the ![Procedure](images/6233371915_DV_resource.Stream@PNG-de-DE.png) button in Runtime:

   - Select "Display dialog" to open the "Default settings data export" dialog.
   - To export the data directly to the specified export file, disable "Display dialog".
3. Additionally, select "Operator input in Runtime" to specify whether or not the operator is allowed to rename the file and/or change the folder in Runtime.

##### Configuring alarm evaluation in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

###### Introduction

To enable evaluation of the alarms in Runtime, assign a custom C function to the "Status changed" event of an alarm. Edit the function to suit your requirements for evaluation in Runtime.

###### Requirement

- The "HMI alarms" editor is open.
- A custom function for reading the data has been created.

  This function must contain a pointer to a string whose data is mapped by scanf to the "MSG_RTDATA_STRUCT" structure.

###### Procedure

To configure the evaluation of an alarm in Runtime, proceed as follows:

1. Select the alarm.
2. In the Inspector window, select "Properties &gt; Events &gt; Status changed".
3. Select the custom function for reading the data.

   ![Procedure](images/72352498187_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72352498187_DV_resource.Stream@PNG-en-US.png)

   The alarm data is read in Runtime. Alarm data includes,for example, the alarm number, time stamp, and alarm state.
4. In the "Scripts" editor, configure evaluation of the alarm data within the function.

###### Result

When the alarm state changes, the alarm data is read in Runtime and evaluated according to your configuration.

###### Example

Use the following, user-defined function "state" to read the status of alarms, for example:

Void state (MSG_RTDATA_STRUCT Parameter)

DWORD state;

state = Parameter.dwMsgState;

printf("Status: %d\r\n", state);

#### Reporting Alarms (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
- [Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced-rt-professional)

##### Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)

###### Overview

WinCC can report on all alarms that occur in the system. The following options are available:

- Output an alarm sequence report

  In Runtime, the standard printer of the HMI device will continuously print each alarm and any changes in its status.
- Output of an alarm report

  You configure an alarm report in the "Reports" editor and specify when it is output in Runtime:

  - For event-driven output, configure an object that is assigned the "PrintReport" system function. The object can be a button or tag.
  - For time-driven output, create a "Print job" in the scheduler. Assign an alarm report to the job.

    > **Note**
    >
    > In the alarm report, specify whether to output current or logged alarms.

###### Requirements

- A printer was configured on the HMI device.

###### Activating continuous alarm reporting

To activate continuous reporting of alarms, follow these steps:

1. Double-click "Runtime settings" in the project navigation.
2. Select "Alarms &gt; General &gt; Report".

   ![Activating continuous alarm reporting](images/70817119115_DV_resource.Stream@PNG-en-US.png)

   ![Activating continuous alarm reporting](images/70817119115_DV_resource.Stream@PNG-en-US.png)

###### Result

The latest alarms are output at the printer of the HMI device.

###### Excluding an alarm from reporting

To exclude specific alarms from reporting, proceed as follows:

1. Open the "HMI alarms" editor.
2. Select the alarm to exclude from reporting on the tab of the selected alarm type.
3. In the Inspector window, disable "Properties &gt; Properties &gt; Miscellaneous &gt; Report".

   ![Excluding an alarm from reporting](images/88322944779_DV_resource.Stream@PNG-en-US.png)

   ![Excluding an alarm from reporting](images/88322944779_DV_resource.Stream@PNG-en-US.png)

###### Result

WinCC does not output these alarms currently on the connected printer.

---

**See also**

[Overview of configuring alarm output (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-of-configuring-alarm-output-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#principles-for-preparation-of-reports-panels-comfort-panels-rt-advanced)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Principles for report output (Panels, Comfort Panels, RT Advanced)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#principles-for-report-output-panels-comfort-panels-rt-advanced)
  
[Alarm report (Panels, Comfort Panels, RT Advanced)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-report-panels-comfort-panels-rt-advanced)
  
[Working with reports (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-reports-panels-comfort-panels-rt-advanced-rt-professional-1)

##### Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced, RT Professional)

###### Overview

WinCC logs all system alarms as required.The following options are available:

- Output the current display in an alarm view

  You can print out a system report. You can also create a custom report, if necessary.In the print job, specify the print scope, page area, printer, or target file.
- Output an alarm sequence report

  In Runtime, every alarm is continuously output at a printer.

###### Requirements

- The "Screens" editor is open.
- Alarms are configured.
- You configured an alarm view with "Print current view" ![Requirements](images/44734647691_DV_resource.Stream@PNG-de-DE.png) button.

###### Procedure

To configure the outputting of the current display in an alarm view using your own report, proceed as follows:

1. Select the required alarm view.
2. To select the print job, select "Properties &gt; Properties &gt; General &gt; Print &gt; Print job" in the Inspector window.

   The default print job is the system print job. You can also select a customized print job, or a modified system print job.

###### Result

If the user clicks the ![Result](images/44734647691_DV_resource.Stream@PNG-de-DE.png) button in Runtime, the selected report with the alarms currently displayed in the alarm view is output to the printer.

> **Note**
>
> **Printer settings**
>
> Configure the printer in the HMI device's Control Panel. The settings will depend on which operating system is used on the HMI device.
>
> For more detailed information, refer to the operating instructions for your HMI device.

---

**See also**

[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
  
[Working with reports (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-reports-panels-comfort-panels-rt-advanced-rt-professional-1)

### Configuring acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring alarm acknowledgment by means of alarm class (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-alarm-acknowledgment-by-means-of-alarm-class-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring trigger for alarm acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-trigger-for-alarm-acknowledgment-basic-panels-panels-comfort-panels-rt-advanced)
- [Sending alarm acknowledgments to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)](#sending-alarm-acknowledgments-to-the-plc-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring alarm acknowledgment by means of alarm class (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

To configure an alarm with alarm acknowledgment, assign it to an alarm class with the "Alarm with single acknowledgment" state machine.

##### Requirement

- The "HMI alarms" editor is open.
- The required alarm class has been created.
- The required alarm has been created.

##### Selecting the state machines for an alarm class

The state machine for a predefined alarm class has already been set. You can only set the state machines for user-defined alarm classes. Proceed as follows:

1. In the "HMI alarms" editor, click the "Alarm class" tab and select the alarm class.
2. Select the required acknowledgment model under "Properties &gt; Properties &gt; Acknowledgment" in the Inspector window.

##### Assign alarms to an alarm class requiring acknowledgment

Proceed as follows to assign an alarm to an alarm class requiring acknowledgment.

1. In the "HMI alarms" editor, click the tab for the alarm type and select the alarm.
2. Under "Properties &gt; Properties &gt; General" in the Inspector window, select the alarm class of the alarm.

##### Result

The alarm will not disappear in Runtime until it is acknowledged by the operator.

---

**See also**

[Creating alarm classes (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring trigger for alarm acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You always specify the acknowledgment requirement for an alarm using the alarm class. Then the operator acknowledges the alarm using the "ACK" function key of the HMI device or the "Acknowledgment" button of the alarm view.

The following options are also available to trigger acknowledgment:

- Configuring a button to acknowledge an alarm
- Acknowledgment of a Discrete Alarm by the PLC

##### Requirements

- The "HMI alarms" editor is open.
- The required alarm class has been created.
- The required alarm has been created.
- An alarm view and a button are created in the "Screens" editor.

##### Configuring a button to acknowledge an alarm

To configure a button for acknowledging an alarm, proceed as follows:

1. Select the button in the "Screens" editor.
2. Under "Properties &gt; Events" in the Inspector window, assign the "AlarmViewAcknowledgeAlarm" system function to the "Click" event.
3. Select the alarm view as parameter.

##### Acknowledgment of a Discrete Alarm by the PLC

1. In the "HMI alarms" editor, click the "Discrete alarm" tab and select the discrete alarm.
2. In the Inspector window, select the tag and the bit that acknowledges the PLC alarm under "Properties &gt; Properties &gt; Acknowledgment &gt; PLC".

   ![Acknowledgment of a Discrete Alarm by the PLC](images/70821567371_DV_resource.Stream@PNG-en-US.png)

   ![Acknowledgment of a Discrete Alarm by the PLC](images/70821567371_DV_resource.Stream@PNG-en-US.png)

##### Acknowledging alarms in an alarm group

The various acknowledgment options have the following effect in alarm groups:

- Operator acknowledges the alarm

  You acknowledge the alarm of an alarm group, for example, using the &lt;ACK&gt; acknowledgment key or a function key. All alarms of the alarm group are acknowledged.
- The PLC acknowledges the alarm

  The alarm of an alarm group is acknowledged by setting a bit in the tag.

  Only the alarm to be acknowledged is acknowledged.

---

**See also**

[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)

#### Sending alarm acknowledgments to the PLC (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Requirement

- The "HMI alarms" editor is open.
- The required alarm has been created and assigned to an alarm class requiring acknowledgment.

  > **Note**
  >
  > You cannot send the acknowledgment of analog alarms to the PLC.

##### Sending alarm acknowledgments to the PLC

To configure that acknowledgment of an alarm is sent to the PLC, follow these steps:

1. In the "HMI alarms" editor, click the "Discrete alarm" tab and select the discrete alarm.
2. In the Inspector window, select "Properties &gt; Properties &gt; Acknowledgment".
3. Under "HMI", select the tag and the bit set by the alarm acknowledgment function.

**Note**

The HMI device and PLC only have read access to the acknowledgment tag memory area.

##### Result

If the operator acknowledges the alarm in Runtime, the operating step is forwarded to the PLC.

### Configuring acknowledgment (RT Professional)

This section contains information on the following topics:

- [Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)
- [Configuring alarm group acknowledgment (RT Professional)](#configuring-alarm-group-acknowledgment-rt-professional)
- [Configuring acknowledgment of the alarm annunciator (RT Professional)](#configuring-acknowledgment-of-the-alarm-annunciator-rt-professional)
- [Configuring the Group Acknowledgement of Alarms (RT Professional)](#configuring-the-group-acknowledgement-of-alarms-rt-professional)
- [Configuring the Resetting of the Acknowledgment Bit for Acknowledgment Tags (RT Professional)](#configuring-the-resetting-of-the-acknowledgment-bit-for-acknowledgment-tags-rt-professional)

#### Configuring alarm acknowledgment (RT Professional)

##### Introduction

The alarm classes define how the alarms from an alarm class are to be acknowledged. When you assign an alarm to an alarm class, you define the state machine for that alarm.

##### Requirements

- The "HMI alarms" editor is open.
- The required alarm class has been created.
- The required alarm has been created.

##### Procedure

To configure the acknowledgement of an alarm, follow these steps:

1. In the "HMI alarms" editor, click the "Alarm class" tab and select the alarm class.
2. To select the state machine, select "Properties &gt; Properties &gt; Acknowledgment &gt; Settings" in the Inspector window.

   - If you enable "Assign comment to defined user", this Runtime user writes a comment on the alarm acknowledgment that is written to the log file alongside with the alarm.
   - If you enable "Use comment of the incoming alarm", the same comment is attached to each status change of this alarm as the one assigned for the "incoming" alarm event.

     ![Procedure](images/72353472651_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/72353472651_DV_resource.Stream@PNG-en-US.png)
3. In the "HMI alarms" editor, select the alarm.
4. Select "Properties &gt; Properties &gt; General" in the Inspector window to select the alarm class of the alarm.
5. Select "Properties &gt; Properties &gt; Acknowledgement &gt; Settings" in the Inspector window to specify the acknowledgment tag to which the alarm acknowledgment is saved, including the bit set for this purpose.
6. To exclude the alarm from the group acknowledgment of the alarm view, enable "Single acknowledgment".

##### Acknowledging an alarm via a system function

1. In the "HMI alarms" editor, select the alarm.
2. In the Inspector window, click "Properties &gt; Events &gt; Incoming".

   The function list opens.
3. In the "Function list" dialog, assign the "SetBit" system function to the "Incoming" event.
4. Enter the acknowledgment tag of the "BOOL" data type as the "Tag (In/Out)" parameter.

---

**See also**

[Configuring alarm group acknowledgment (RT Professional)](#configuring-alarm-group-acknowledgment-rt-professional)
  
[Configuring acknowledgment of the alarm annunciator (RT Professional)](#configuring-acknowledgment-of-the-alarm-annunciator-rt-professional)
  
[Configuring the Group Acknowledgement of Alarms (RT Professional)](#configuring-the-group-acknowledgement-of-alarms-rt-professional)
  
[Configuring the Resetting of the Acknowledgment Bit for Acknowledgment Tags (RT Professional)](#configuring-the-resetting-of-the-acknowledgment-bit-for-acknowledgment-tags-rt-professional)
  
[Configuring trigger for alarm acknowledgment (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-trigger-for-alarm-acknowledgment-basic-panels-panels-comfort-panels-rt-advanced)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)

#### Configuring alarm group acknowledgment (RT Professional)

##### Introduction

You acknowledge an alarm group using the acknowledgment tag. To set and reset the acknowledgment bit, configure a display and operating element.

##### Requirements

- The "HMI alarms" editor is open.
- You have created the alarm groups.
- The required alarm has been created.

##### Procedure

To configure the acknowledgement of an alarm group, follow these steps:

1. In the "HMI alarms" editor, select the alarm.
2. Under "Properties &gt; Properties &gt; General" in the Inspector window, select the alarm group to which the alarm belongs.
3. Click the "Alarm groups" tab in the "HMI alarms" editor.
4. Select the alarm group.
5. Under "Properties &gt; Properties &gt; Tags &gt; Settings" in the Inspector window, select the acknowledgment tag and acknowledgment bit.
6. Open the "Screens" editor and configure a button that sets the acknowledgment bit in Runtime for the acknowledgment tag.

##### Result

The user monitors the alarms for a given function together in Runtime. If a user identifies the cause of a fault, then he or she can acknowledge all alarms for this function using the configured operator action.

---

**See also**

[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)
  
[Working with Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

#### Configuring acknowledgment of the alarm annunciator (RT Professional)

##### Introduction

In addition to the alarm view, WinCC also supports alarm indication in the plant by means of visual or audible signals. The alarm annunciator can be a horn or a warning lamp, for example. You can acknowledge the alarm annunciator in the following ways:

- Using the ![Introduction](images/21864881803_DV_resource.Stream@PNG-de-DE.png) button in the alarm view

  This "Acknowledge alarm annunciator" button must be configured in the alarm view. The button is always active, even if another option for acknowledging the alarm annunciator has been enabled. Use the ![Introduction](images/21864881803_DV_resource.Stream@PNG-de-DE.png) button to switch the alarm annunciator off. The alarm is still pending in the alarm view.
- Using a single acknowledgment

  You acknowledge the alarm annunciator with the alarm that triggered the alarm annunciator. The operator acknowledges an individual alarm by clicking the ![Introduction](images/21865909259_DV_resource.Stream@PNG-de-DE.png) "Single acknowledgment" button in the alarm view.
- Using a tag

  The specified tag is used to control the alarm annunciator.

  To acknowledge the alarm annunciator, e.g. with a button, use this option.

##### Requirements

- The "HMI alarms" editor is open.
- The required alarm class has been created.
- The required alarm has been created, and assigned to the alarm class.

##### Procedure

To configure the acknowledgment of an alarm annunciator, proceed as follows:

1. Click the "Alarm classes" tab in the "HMI alarms" editor.
2. Select the required alarm class.
3. In the Inspector window, select "Properties &gt; Properties &gt; Acknowledgment &gt; Alarm annunciator" to specify how to acknowledge the alarm annunciator.

##### Result

The operator acknowledges the alarm annunciator in Runtime as specified for the alarm class of this alarm.

---

**See also**

[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)

#### Configuring the Group Acknowledgement of Alarms (RT Professional)

##### Introduction

You can use the ![Introduction](images/21866163339_DV_resource.Stream@PNG-de-DE.png) button in the alarm view to acknowledge all pending, and visible alarms that must be acknowledged in the alarm view. You can exclude individual alarms from group acknowledgment.After group acknowledgment was triggered, the excluded alarms are still pending.

##### Requirement

- A screen is open.
- An alarm view has been created.

##### Procedure

To set up a group acknowledgement, follow these steps:

1. Open the "Screens" editor, and select the relevant alarm view.
2. In the Inspector window, select "Properties Properties &gt; Toolbar - Buttons &gt; Group acknowledgment."

   The ![Procedure](images/21866163339_DV_resource.Stream@PNG-de-DE.png) button appears in the alarm view. All alarms of an alarm view that are not excluded from group acknowledgment are acknowledged when the operator actuates this button.

##### Configuring a single acknowledgement

1. Open the "HMI alarms" editor and select the tab that contains the relevant alarm type.
2. Select the alarm that you want to exclude from the group acknowledgement.
3. Enable "Properties &gt; Properties &gt; Acknowledgment &gt; Single acknowledgment" in the Inspector window.

   When you acknowledge all the alarms in an alarm view using the ![Configuring a single acknowledgement](images/21866163339_DV_resource.Stream@PNG-de-DE.png) button, any alarms for which the "Single acknowledgement" option is enabled will be excluded. The operator acknowledges alarms with "single acknowledgment" option individually.

---

**See also**

[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)

#### Configuring the Resetting of the Acknowledgment Bit for Acknowledgment Tags (RT Professional)

##### Introduction

The user or controller resets the acknowledgment bit of the acknowledgment tag. The acknowledgment bit is reset directly in the PLC or in WinCC Runtime via a script, for example. The acknowledgment bit is not automatically reset.

##### Resetting of the acknowledgment bit by the PLC

You can use an external tag as an acknowledgment tag to allow the PLC to reset the acknowledgment bit.

If the alarm is acknowledged in Runtime in WinCC, the defined acknowledgment bit is set in the PLC. In the PLC, the acknowledgment bit is processed as required before it is reset once more.

In the PLC, an alarm is triggered by a reusable function block or by functions. In this block the alarm can also be acknowledged or the acknowledgment bit reset.

Evaluation and resetting of the acknowledgment bit by the PLC has the following advantage:

It is easy to cause the acknowledgement with external signals, such as pushbutton units in the field.

You can acknowledge externally and via the alarm view. Both methods use the same bit in the automation system for acknowledgement.

> **Note**
>
> To ensure that the alarm view in WinCC reliably acquires the external acknowledgement in time, configure the resetting by the automation system with a time delay.

##### Resetting of the acknowledgment bit by the WinCC

If you want to acknowledge an alarm via the acknowledgment tag only, reset the acknowledgment bit immediately as soon as it is set.

If you acknowledge an alarm via the alarm view, configure the resetting of the acknowledgment tags separately.

You can reset the acknowledgment bit in the following ways in WinCC:

- Button

  You can reset the acknowledgment bit using a button.
- System function

  Use the "ResetBitInTag" system function. If the acknowledgment bit is set, it will be immediately reset.

  > **Note**
  >
  > If the acknowledgment tag is of the "BOOL" data type, use the "ResetBit" system function.

  > **Note**
  >
  > If lots of alarms are processed using scripts, this places a heavy load on the work memory. The acknowledgment bit should therefore ideally be reset by the PLC.

---

**See also**

[Configuring alarm acknowledgment (RT Professional)](#configuring-alarm-acknowledgment-rt-professional)

## Alarm Logging (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Configuring alarm logging (Panels, Comfort Panels, RT Advanced)](#configuring-alarm-logging-panels-comfort-panels-rt-advanced)
- [Configuring alarm logging (RT Professional)](#configuring-alarm-logging-rt-professional)

### Configuring alarm logging (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
- [Create an alarm log (Panels, Comfort Panels, RT Advanced)](#create-an-alarm-log-panels-comfort-panels-rt-advanced)
- [Logging alarms (Panels, Comfort Panels, RT Advanced)](#logging-alarms-panels-comfort-panels-rt-advanced)
- [Configuring an alarm view for logged alarms (Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-logged-alarms-panels-comfort-panels-rt-advanced)
- [Configuring alarm buffer overflow (Panels, Comfort Panels, RT Advanced)](#configuring-alarm-buffer-overflow-panels-comfort-panels-rt-advanced)
- [Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)](#direct-access-to-the-odbc-log-database-panels-comfort-panels-rt-advanced)
- [Setting up the ODBC data source (Panels, Comfort Panels, RT Advanced)](#setting-up-the-odbc-data-source-panels-comfort-panels-rt-advanced)
- [Configuring a checksum for a log (Panels, Comfort Panels, RT Advanced)](#configuring-a-checksum-for-a-log-panels-comfort-panels-rt-advanced)
- [Evaluating the checksum of log data (Panels, Comfort Panels, RT Advanced)](#evaluating-the-checksum-of-log-data-panels-comfort-panels-rt-advanced)
- [Checksums for logs in regulated projects (Panels, Comfort Panels, RT Advanced)](#checksums-for-logs-in-regulated-projects-panels-comfort-panels-rt-advanced)
- [Log response to language switching in runtime (Panels, Comfort Panels, RT Advanced)](#log-response-to-language-switching-in-runtime-panels-comfort-panels-rt-advanced)
- [Managing logging behavior when Runtime starts (Panels, Comfort Panels, RT Advanced)](#managing-logging-behavior-when-runtime-starts-panels-comfort-panels-rt-advanced)
- [Controlling the Logging in relation to the Fill Level (Panels, Comfort Panels, RT Advanced)](#controlling-the-logging-in-relation-to-the-fill-level-panels-comfort-panels-rt-advanced)

#### Basics on alarm logging (Panels, Comfort Panels, RT Advanced)

##### Introduction

An alarm log is used to record project alarms.

> **Note**
>
> Alarm logging is not available for every HMI device.

##### Configuration steps

To log an alarm, follow these configuration steps:

1. Creating an alarm log

   You define the following properties for the alarm log:

   - Logging method

     Behavior of the log when reaching a specific fill level
   - Storage location and file format
   - Log size
   - Runtime start characteristics
2. Assigning an alarm log to an alarm class

   You can log the alarms from multiple alarm classes in an alarm log.
3. Assigning an alarm to a loggable alarm class
4. Configure display of logged alarms in an alarm view

##### Content of the alarm log

All states are logged for configured alarms. The following three entries, for example, are stored in the log for an alarm that requires acknowledgment:

- 04.08.2007 10:00:25:520, analog alarm, ID5, **K**, error, fill level exceeded by 10%
- 04.08.2007 10:01:20:442, analog alarm, ID5, **Q**, error, fill level exceeded by 10%
- 04.08.2007 10:01:30:112, analog alarm, ID5, **G**, error, fill level exceeded by 10%

In the example, the alarm states are identified by the following letters:

**K** = Incoming

**Q** = Acknowledged

**G** = Outgoing

All data belonging to an alarm is stored in the alarm log, including configuration data such as the alarm class, time stamp, and alarm text.

The potential number of logged alarms depends on the data medium used. You can further process the logged alarms in other programs for analysis purposes, for example.

> **Note**
>
> Alarm text and point of error are only logged if you have configured such a setting in the log properties.
>
> Logged alarms that contain alarm text and the point of error exceed the estimated size of the configured alarms. Check to see whether the specified storage location still has sufficient space.

> **Note**
>
> The time stamp of a logged alarm is always specified in standard UTC format (Universal Time Coordinated).

##### Logging methods

The logging method determines how the alarm log responds when the configured size is reached. WinCC supports the following logging methods:

- Circular log

  When the configured log size has been reached, the oldest entries are deleted. When the configured log size has been reached, approximately 20% of the oldest entries are deleted. It is therefore not possible to display all the configured entries. During configuration, select an appropriate size for the circulation log. Alternatively, configure a segmented circular log.
- Segmented circular log

  In a segmented circular log, multiple single logs of the same size are filled in succession. When all logs are completely full, the oldest log is overwritten.
- Log with level-dependent system alarm

  When a defined level is reached, such as 90 %, a system alarm is triggered. When the configured size of the log has been reached, new alarm events are not logged.
- Log with level-dependent execution of system functions

  When the log is completely full, the "Overflow" event is triggered. You configure a function list for the event.

  When the configured size of the log has been reached, new alarm events are not logged.

##### Displaying logged data

On the HMI device, the logged data is displayed in an alarm view that is configured for this purpose.

---

**See also**

[Configuring an alarm view for logged alarms (Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-logged-alarms-panels-comfort-panels-rt-advanced)
  
[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Create an alarm log (Panels, Comfort Panels, RT Advanced)](#create-an-alarm-log-panels-comfort-panels-rt-advanced)
  
[Logging alarms (Panels, Comfort Panels, RT Advanced)](#logging-alarms-panels-comfort-panels-rt-advanced)
  
[Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)](#direct-access-to-the-odbc-log-database-panels-comfort-panels-rt-advanced)
  
[Setting up the ODBC data source (Panels, Comfort Panels, RT Advanced)](#setting-up-the-odbc-data-source-panels-comfort-panels-rt-advanced)
  
[Configuring a checksum for a log (Panels, Comfort Panels, RT Advanced)](#configuring-a-checksum-for-a-log-panels-comfort-panels-rt-advanced)
  
[Evaluating the checksum of log data (Panels, Comfort Panels, RT Advanced)](#evaluating-the-checksum-of-log-data-panels-comfort-panels-rt-advanced)
  
[Log response to language switching in runtime (Panels, Comfort Panels, RT Advanced)](#log-response-to-language-switching-in-runtime-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm view for logged alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-for-logged-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure of *.csv files that contain alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-of-csv-files-that-contain-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Working with Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-basic-panels-panels-comfort-panels-rt-advanced)

#### Create an alarm log (Panels, Comfort Panels, RT Advanced)

##### Introduction

In Runtime, you save alarms to the alarm logs. Specify the alarm log in the alarm class. An alarm log contains the alarms of several alarm classes. Create the alarm log in the "Logs" editor. When creating an alarm log, define the following parameters:

- Name
- Size
- Storage location
- Runtime start characteristics
- Log type
- Advanced content
- Checksum

You can also enter comments for each log.

##### Requirement

- The "Alarm log" tab is open in the "Log" editor.
- The Inspector window is open.

##### Procedure

To create an alarm log, proceed as follows:

1. Double-click "&lt;Add&gt;" in the table.

   A new alarm log is created.
2. Under "Properties &gt; Properties &gt; General" in the Inspector window, enter a unique name for the alarm log.

   ![Procedure](images/70551132171_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70551132171_DV_resource.Stream@PNG-en-US.png)
3. Under "Number of data records per log", define the number of alarms to be saved to a log file.

   The approximate space required on the storage medium is displayed. Memory space requirements will increase accordingly if you log alarm texts with tag values.
4. In the "Storage location" field you select where the log entries are saved.
5. Depending on the selected "Storage location", you either select the "Path" or the "Name of the data source".
6. To determine if audit trail data were changed at a later time, activate "Properties &gt; Properties &gt; General &gt; Checksum".
7. If necessary, enter a descriptive text in the "Comment" category to document your configuration.

**Note**

**Device dependency**

The "Checksum" option is only available for display and HMI devices which support "Configuration conforms to GMP".

##### Result

The alarm log is created. You can assign one or several alarm classes to this alarm log.

---

**See also**

[Configuring an alarm view for logged alarms (Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-logged-alarms-panels-comfort-panels-rt-advanced)
  
[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Logging alarms (Panels, Comfort Panels, RT Advanced)](#logging-alarms-panels-comfort-panels-rt-advanced)
  
[Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)](#direct-access-to-the-odbc-log-database-panels-comfort-panels-rt-advanced)
  
[Configuring a checksum for a log (Panels, Comfort Panels, RT Advanced)](#configuring-a-checksum-for-a-log-panels-comfort-panels-rt-advanced)
  
[Log response to language switching in runtime (Panels, Comfort Panels, RT Advanced)](#log-response-to-language-switching-in-runtime-panels-comfort-panels-rt-advanced)
  
[Working with Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-basic-panels-panels-comfort-panels-rt-advanced)

#### Logging alarms (Panels, Comfort Panels, RT Advanced)

##### Overview

To log alarms, follow these steps:

- Create an alarm log.
- Assign the created alarm log to an alarm class.
- Assign the alarm class with the created alarm log to an alarm.
- In the Runtime settings specify the language in which you want to write the logs.
- You evaluate logged alarms.

  You can analyze the logged alarms directly in your WinCC project, such as in an alarm view, or in another user program, such as Microsoft Excel.

  > **Note**
  >
  > **Tag fields in the alarm text**
  >
  > The sequence of tag fields in the alarm text is language dependent. The sequence of the Runtime language is used for logging alarms to a "*.csv" log file.
  >
  > Changing the tag of an output field in one language causes the modified output field to appear at the end of the alarm text in all other languages. This means the sequence of the output fields in the log file can change.

  > **Note**
  >
  > **Text lists in alarm text**
  >
  > If you have inserted a text list into the alarm text and the alarm has been logged, the text list entries are displayed in the alarm log.

##### Requirements

- You have created an alarm log.
- The "HMI alarms" editor is open.

##### Assigning an alarm log to an alarm class

To assign the alarm log to an alarm class, proceed as follows:

1. Open the "Alarm classes" tab in the "HMI alarms" editor.
2. Select the required alarm class.
3. Under "Properties &gt; Properties &gt; General &gt; Log" in the Inspector window, select the alarm log.

##### Assign alarm to an alarm class

To assign an alarm to the alarm class, proceed as follows:

1. In the "HMI alarms" editor, open the "Analog alarms" tab, or the "Discrete alarms" tab.
2. Select the required alarm.
3. Under "Properties &gt; Properties &gt; General &gt; Alarm class" in the Inspection window, select the alarm class for which the alarm log was configured.

##### Result

The alarm is saved to the configured alarm log.

---

**See also**

[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Create an alarm log (Panels, Comfort Panels, RT Advanced)](#create-an-alarm-log-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm view for logged alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-for-logged-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring an alarm view for logged alarms (Panels, Comfort Panels, RT Advanced)](#configuring-an-alarm-view-for-logged-alarms-panels-comfort-panels-rt-advanced)
  
[Working with Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring Alarm Classes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-alarm-classes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring an alarm view for logged alarms (Panels, Comfort Panels, RT Advanced)

##### Introduction

In Runtime, logged alarms are displayed in an alarm view or alarm window.

##### Requirements

- An alarm view or alarm window is configured in the "Screens" editor
- An alarm log was created in the "Log" editor.
- The alarms are assigned the "loggable" attribute in the "HMI alarms" editor.

##### Configuring an alarm view for logged alarms

To configure an alarm view for logged alarms, proceed as follows:

1. Open the screen with the alarm view and select the alarm view.
2. In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Alarm log".
3. Click the "...." button and select the alarm log.
4. Continue to configure the alarm view as for the display of current alarms.

##### Result

In Runtime, the logged alarms are output in the alarm view.

---

**See also**

[Logging alarms (Panels, Comfort Panels, RT Advanced)](#logging-alarms-panels-comfort-panels-rt-advanced)
  
[Create an alarm log (Panels, Comfort Panels, RT Advanced)](#create-an-alarm-log-panels-comfort-panels-rt-advanced)
  
[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)

#### Configuring alarm buffer overflow (Panels, Comfort Panels, RT Advanced)

##### Introduction

The size of the alarm buffer depends on the type of HMI device. In WinCC, specify the percentage of the alarm buffer to be deleted on alarm buffer overflow.

##### Requirements

- You have created a project.

##### Procedure

To configure the response to an alarm buffer overflow, follow these steps:

1. Double-click "Runtime settings" in the project navigation under your HMI device.
2. Under "Alarms &gt; General &gt; Buffer clearance in percent upon buffer overflow", enter a value between 1 and 100.

   This value specifies the percentage of the alarm buffer that is deleted on alarm buffer overflow.

##### Result

If data in the alarm buffer exceeds the resources of alarm buffer memory, the configured percentage of data will be deleted from the oldest alarms in the alarm buffer.

> **Note**
>
> You cannot check the alarm buffer overflow separately by alarm method. You can use the "ClearAlarmBuffer" system function to delete specific alarms of specific alarm classes from the alarm buffer.

---

**See also**

[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Working with Logs (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-basic-panels-panels-comfort-panels-rt-advanced)

#### Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)

##### Overview

The storage location of a log can be a database or a file.

The database is addressed by means of its "Data source name" (DSN). Select the database to be used in WinCC as follows:

Select the database from the Windows Start menu under "Settings &gt; Control panel &gt; ODBC Data Sources".

In your configuration, specify the "Data source name" (DSN) instead of a directory name as storage path for log data. With the DSN, you are referencing the database and the storage location.

The entire functional scope of the database is available for additional processing and evaluation of log data.

##### Application

The data source sets up the connection to the database. Create the data source on the same PC on which the Runtime software is stored. Then enter the DSN configured on this PC when you create a log in WinCC.

The ODBC interface allows you to use other programs, such as MS Access or MS SQL Server, to access the database directly.

In addition, you can use the "StartProgram" system function to configure program calls, e.g. MS Access, on the HMI device. Runtime is not interrupted while you configure such calls.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Basics on alarm logging (RT Professional)](#basics-on-alarm-logging-rt-professional)
  
[Setting up the ODBC data source (Panels, Comfort Panels, RT Advanced)](#setting-up-the-odbc-data-source-panels-comfort-panels-rt-advanced)

#### Setting up the ODBC data source (Panels, Comfort Panels, RT Advanced)

##### Introduction

To store process values or alarms in the log database in Runtime, set up the ODBC data source.

##### Requirement

- A log database has been created.

  You create the log database using the SQL Enterprise Manager. You can find more detailed information on how to do this from Microsoft.

##### Procedure

To set up an ODBC data source, follow these steps:

1. In Control Panel, open "Administrative Tools" and select "Data Sources (ODBC)".

   The "ODBC Data Source Administrator" dialog is opened.
2. Click "User DSN &gt; Add".
3. Select the "SQL-Server and click on "Finish".
4. In the dialog that follows, enter a name for the User DSN and the SQL-Server and click on "Next".
5. In the dialog that follows, define the logon procedure for the SQL database and click on "Next".
6. Activate "Change the default database to".
7. Select the database you have created and click on "Next".
8. In the dialog that follows, click "Finish".

---

**See also**

[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)](#direct-access-to-the-odbc-log-database-panels-comfort-panels-rt-advanced)

#### Configuring a checksum for a log (Panels, Comfort Panels, RT Advanced)

##### Introduction

In a regulated project, you have the option of assigning a checksum to the log data of an data log or alarm log. This checksum can be used during plant operation to determine if the data of this log has subsequently changed.

> **Note**
>
> **Device dependency**
>
> The "Checksum" option is only available for display and HMI devices which support "Configuration conforms to GMP".

##### Requirements

- GMP compliant configuration is enabled.
- A data log or alarm log has been created.

##### Procedure

Proceed as follows to configure a data log or alarm log for the use of a checksum:

1. Open the data log or alarm log in the corresponding log editor.
2. In the "Storage location" box, select "File - CSV (ASCII)" or "File - TXT (Unicode)".

   ![Procedure](images/70806916747_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70806916747_DV_resource.Stream@PNG-en-US.png)
3. Under "Properties &gt; Properties &gt; Logging method" in the Inspector window, select the option "Display system event at" or "Trigger event".

   ![Procedure](images/70807230603_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70807230603_DV_resource.Stream@PNG-en-US.png)
4. In the editor table, activate the option "Enable checksum".
5. In the editor table, activate the option "Enable logging at runtime start".  
   Columns that are not displayed are activated with the shortcut menu of the column title.

   ![Procedure](images/70807595659_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70807595659_DV_resource.Stream@PNG-en-US.png)
6. Save the project.

##### Result

The log data of the log is assigned a checksum in runtime.

---

**See also**

[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Create an alarm log (Panels, Comfort Panels, RT Advanced)](#create-an-alarm-log-panels-comfort-panels-rt-advanced)
  
[GMP-compliant configuration (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
  
[Enabling GMP compliant configuration (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#enabling-gmp-compliant-configuration-panels-comfort-panels-rt-advanced)

#### Evaluating the checksum of log data (Panels, Comfort Panels, RT Advanced)

##### Introduction

If you have configured a data log or alarm log with generation of a checksum, you can check if the log data has subsequently changed.

> **Note**
>
> **Device dependency**
>
> The "Checksum" option is only available for display and HMI devices which support "Configuration conforms to GMP".

The DOS program "HmiCheckLogIntegrity" is available for checking the integrity of the log data.

The "HmiCheckLogIntegrity" program supports verification of the following files:

- Log files of alarm logs, data logs, and Audit in CSV format
- Log files of alarm logs, data logs, and Audit in TXT format
- Recipe data records in CSV format
- Recipe data records in TXT format

You can find the "HmiCheckLogIntegrity.exe" program in the installation directory of WinCC under the folder "WinCC Runtime Advanced", for example &lt;C:\Program Files\Siemens\Automation WinCC Runtime Advanced&gt;.

> **Note**
>
> **Audit Trail and Log with Checksum**
>
> Before you update WinCC with a Service Pack or a new version, exit and save the Audit Trail or the logs using checksum. After WinCC is updated, the audit trail or logs will be continued with new files using checksum.
>
> Make sure that the logs are started at a defined state with the new version.

##### Procedure

1. Copy the file to be checked from the HMI device to your configuration computer.
2. Open a command line prompt with "Start &gt; Programs &gt; Accessories &gt; Command Prompt".
3. Enter the path to "HmiCheckLogIntegrity.exe" followed by a space in the command line prompt. After the space, enter the storage location of the file to be checked within quotation marks.
4. Press &lt;Enter&gt;.
5. The check is performed.

   When the checked data are consistent, the "Consistency check succeeded" message appears.

   ![Procedure](images/12695302411_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/12695302411_DV_resource.Stream@PNG-de-DE.png)

   When the checked data are inconsistent, the "Consistency check failed" message appears. Information about the first inconsistent line in the file is also displayed.

   ![Procedure](images/12695310347_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/12695310347_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> If there are spaces in the path to the "HmiCheckLogIntegrity.exe" program, you need to specify the path in quotation marks.

You can also check the integrity of the log data with the AuditViewer.

---

**See also**

[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Enabling GMP compliant configuration (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#enabling-gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
  
[Evaluating Audit Trails in AuditViewer (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#evaluating-audit-trails-in-auditviewer-panels-comfort-panels-rt-advanced)

#### Checksums for logs in regulated projects (Panels, Comfort Panels, RT Advanced)

##### Checksums in regulated projects

With WinCC you configure regulated projects as required by FDA guidelines, if necessary. Use the "Audit" option to create regulated projects.

In regulated projects you supply a checksum for the logged data of an alarm log. The operator will use this checksum during operation of the plant to see if the data of an alarm log have been changed.

For the checksum to be clear, it starts with the first line of an alarm log and integrates the previous lines when continuously generating the checksum. This means a checksum can only be generated for the following logs:

- Log that sends a system alarm when it is full
- Log with execution of system functions when log is full.

Generation of a checksum is also available for alarm logs that are saved as files of the "*.csv" or "*.txt" (Unicode) format.

If you want to continue an existing log without checksum as one with checksum, a backup copy of the existing log is created in the "*.keep" file format. A new log with checksums is created.

To maintain the validity of checksums, the following limitations apply when using the system function "CopyLog":

- You cannot copy a log without checksums into a log with checksums.
- You cannot copy a log with checksums into a log without checksums.

#### Log response to language switching in runtime (Panels, Comfort Panels, RT Advanced)

##### Introduction

In the Runtime settings of your HMI device, select the language to be used for writing to logs in runtime.

##### Requirement

- The languages used in your project are activated in the "Project languages" editor, for example, "German (Germany)" and "English (USA)" .

##### Procedure

To determine the startup language, follow these steps:

1. Select "Runtime settings &gt; Language and fonts" in the project navigation.
2. Activate the runtime language, for example, "German (Germany)" and "English (USA)".
3. Set the "Language switch order". Use 0 to determine the startup language, for example:

   - German 0.
   - English 1

     With "0", German is specified as the "Startup language".
4. Select "Runtime settings &gt; General" in the project navigation.
5. Select the "Logs &gt; Logging language &gt; Startup language".

##### Result

The project starts after it is transferred. German is specified as the "Startup language" with "Language switch order". The logs are now written in German. During runtime, the operator switches the runtime language to English. The logs will still to be written in German.

The operator closes runtime. Due to the previously performed language switch, the next time the system starts the "startup language" is English. Since English is the startup language, the logs are now written in English.

The logging language remains English even when the language is switched again in runtime until runtime is closed once again.

If you use another option instead of "Startup language" to select the language, the logs are always written in the same language. This is true regardless of the language selected by the operator in runtime.

---

**See also**

[Create an alarm log (Panels, Comfort Panels, RT Advanced)](#create-an-alarm-log-panels-comfort-panels-rt-advanced)
  
[Basics on alarm logging (Panels, Comfort Panels, RT Advanced)](#basics-on-alarm-logging-panels-comfort-panels-rt-advanced)
  
[Sending a complete alarm from the controller to the HMI device and automatic update (Panels, Comfort Panels, RT Advanced)](#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-panels-comfort-panels-rt-advanced)

#### Managing logging behavior when Runtime starts (Panels, Comfort Panels, RT Advanced)

##### Introduction

When you configure a log, you define the restart characteristics of the log when Runtime is started. You define whether the logging should start when Runtime starts in the log properties. You can also define whether an existing log will be continued or overwritten.

You define the restart characteristics separately for each log.

##### Requirement

- You have created a log.
- The "Historical Data" editor is open.
- The Inspector window with the log properties is open.

##### Procedure

To configure the restart characteristics of a data log, proceed as follows:

1. Select the log for which you want to define the restart characteristics in the "Historical Data" editor.
2. In the Inspector window select "Properties &gt; Properties &gt; Restart behavior".
3. If you want logging to start when Runtime starts, enable the "Enable logging at runtime start" option in the "Logging" area.  
   You can also start logging in Runtime using the "StartLogging" system function, for example.
4. Select the restart behavior of the log in the "Log handling at restart" area.

   - The logged values are deleted and logging is started again with the option "Reset log".
   - The option "Append data to existing log" is used to append the values to be logged to the existing log.

Alternatively you can configure the restart characteristics of a log directly in the "Historical Data" editor. To view hidden columns, activate the column titles using the shortcut menu.

##### Result

Logging will start in runtime according to your settings.

#### Controlling the Logging in relation to the Fill Level (Panels, Comfort Panels, RT Advanced)

##### Introduction

The size of a log is determined by the number of entries. You use the logging method to determine how the log responds when it is full.

##### Logging methods

The following logging methods are available:

- ![Logging methods](images/70502244875_DV_resource.Stream@PNG-de-DE.png) Circular log

  When the configured log size has been reached, the oldest entries are deleted. When the configured log size has been reached, approximately 20% of the oldest entries are deleted. It is therefore not possible to display all the configured entries. During configuration, select an appropriate size for the circulation log. Alternatively, configure a segmented circular log.
- ![Logging methods](images/70509190539_DV_resource.Stream@PNG-de-DE.png) Segmented circular log

  In a segmented circular log, multiple log segments of the same size are filled in succession. When all logs are completely full, the oldest log is overwritten.
- ![Logging methods](images/70509198347_DV_resource.Stream@PNG-de-DE.png) Log that sends a system alarm when it is full

  When a defined level is reached, such as 90 %, a system alarm is triggered. When the log is 100% full, new tag values are not logged.
- ![Logging methods](images/70509564555_DV_resource.Stream@PNG-de-DE.png) Log with level-dependent triggering of an event.

  When the log is completely full, the "Overflow" event is triggered. Configure a function list for the event that will be carried out when the "Overflow" event occurs. When the configured size of the log is reached, new tag values are not logged.

  The following system functions are available for further processing of full logs:

##### Requirement

- You have created a log.
- The "Historical Data" editor is open.
- The Inspector window with the log properties is open.

##### Procedure

1. Select the log for which you want to define the logging method in the "Historical Data" editor.
2. Select "Properties &gt; Properties &gt; Logging method" in the Inspector window and select the required logging method.
3. If you have selected the "Segmented circular log" type, enter the number of log segments. The system creates an additional log segment for the main log. This results in the total number of log files created from the number of configured segments as well as the automatically created log.

   If you selected a log with the "Display system alarm on" setting, specify the level as a percentage at which a system alarm is to be triggered.

   If you selected the "Trigger event" setting, configure the function list in the "Events" group.

Alternatively you can configure the logging method directly in the "Historical Data" editor table. To view hidden columns, activate the column titles using the shortcut menu.

The "Overflow" event is not available in the editor table. You must therefore configure the function list in the Inspector window.

##### Result

The selected log responds according to the settings in Runtime.

### Configuring alarm logging (RT Professional)

This section contains information on the following topics:

- [Basics on alarm logging (RT Professional)](#basics-on-alarm-logging-rt-professional)
- [Logging alarms (RT Professional)](#logging-alarms-rt-professional)
- [Configuring the Alarm Log Backup (RT Professional)](#configuring-the-alarm-log-backup-rt-professional)
- [Connecting and Disconnecting the Alarm Log Backup (RT Professional)](#connecting-and-disconnecting-the-alarm-log-backup-rt-professional)
- [Accessing the Log Database Directly with C-API/ODK (RT Professional)](#accessing-the-log-database-directly-with-c-apiodk-rt-professional)
- [Accessing the Log Database Directly with ADO/OLE DB (RT Professional)](#accessing-the-log-database-directly-with-adoole-db-rt-professional)
- [Configuring the Reloading of Alarms after a Power Failure (RT Professional)](#configuring-the-reloading-of-alarms-after-a-power-failure-rt-professional)

#### Basics on alarm logging (RT Professional)

##### Introduction

An alarm log is used to record project alarms.Alarm logs are created by the system. For example, after an error has occurred, or a limit was exceeded in Runtime, the corresponding alarm you configured in the "HMI alarms" editor is output in Runtime.Each alarm event is logged, e.g., the transition of the alarm from "incoming" to "acknowledged" status.

You can store the alarm events in a log database and/or log them to hardcopy in an alarm report. You can output the alarms stored in the database in Runtime, for example, in an alarm view.

The logged alarms are stored in a circular log that consists of multiple single segments. The size of all the segments and of an individual segment is defined under "Alarm log" in the log settings.

You should configure backups to save the data at regular intervals.

##### Configuration steps

To log an alarm, follow these configuration steps:

1. Configuring "Log settings"

   You define the settings for the alarm logging in the log settings.
2. Enable alarm logging

   You specify that alarms of particular alarm classes will be logged.
3. Assigning an alarm to a loggable alarm class

##### Content of the alarm log

The alarm logs are used to store all alarm data, including configuration data. You can read all alarm properties from the log files, e.g. the alarm class, the timestamp, and the alarm texts.A new log segment with the new configuration data is generated whenever you edit configuration data of an alarm. This function prevents any change from having an influence on alarms logged previously.

The possible number of logged alarms depends on the server used.

> **Note**
>
> The time stamp of a logged alarm is always specified in standard UTC format (Universal Time Coordinated).

As alarm configuration is language-specific, the logs contain a configuration data table for each language configured.

##### Storage media and location

Log data are stored in a database. You can further process the saved data in other programs for analysis purposes, for example.

##### Backup for log segments

Take backups of your log segments to ensure complete documentation of your process. You define the settings under "Log settings".

##### Displaying logged data

You can view the logged data on the HMI device.Configure a corresponding alarm view that displays the log data, or use buttons to show the "Historical alarm list" (short-term), or the "Historical alarm list" (long-term) in Runtime.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Logging alarms (RT Professional)](#logging-alarms-rt-professional)
  
[Configuring the Alarm Log Backup (RT Professional)](#configuring-the-alarm-log-backup-rt-professional)
  
[Connecting and Disconnecting the Alarm Log Backup (RT Professional)](#connecting-and-disconnecting-the-alarm-log-backup-rt-professional)
  
[Accessing the Log Database Directly with C-API/ODK (RT Professional)](#accessing-the-log-database-directly-with-c-apiodk-rt-professional)
  
[Accessing the Log Database Directly with ADO/OLE DB (RT Professional)](#accessing-the-log-database-directly-with-adoole-db-rt-professional)
  
[Configuring the Reloading of Alarms after a Power Failure (RT Professional)](#configuring-the-reloading-of-alarms-after-a-power-failure-rt-professional)
  
[Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)](#direct-access-to-the-odbc-log-database-panels-comfort-panels-rt-advanced)
  
[Working with Logs (RT Professional)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-rt-professional)

#### Logging alarms (RT Professional)

##### Introduction

Specify the size and time range for the alarm log segments in the log settings.By specifying their size, you also define the number of segments.

The segments are filled successively with data in Runtime.The next segment is used on overflow of a segment.You can also configure a time-dependent segment change.If you specify a time for the segment change, the next log segment is filled after this time was reached.

> **Note**
>
> Ensure that the log size does not exceed memory resources. The log manager does not validate the selected settings.A large number of linked log segments might lead to longer waiting periods in the system during the startup and shutdown of Runtime.

##### Overview

To log alarms, follow these configuration steps:

- Configure the alarm log in the log settings.

  Define the size and segmentation.
- Configure a loggable alarm class.
- Assign the alarm to a loggable alarm class.

##### Requirements

- An alarm class has been created.

##### Configuring an alarm log

To configure the alarm log, proceed as follows:

1. Double-click "Runtime settings" in the project navigation.
2. Double-click "Logging" in the area navigator.

   The alarm settings open.

   ![Configuring an alarm log](images/72354101771_DV_resource.Stream@PNG-en-US.png)

   ![Configuring an alarm log](images/72354101771_DV_resource.Stream@PNG-en-US.png)
3. Click "Properties &gt; General" in the Inspector window and specify the following:

   - Enter the values for "Time period of all segments" and "Maximum size of all segments".

     Define the size of the log database by entering the accumulated time period for all segments and the maximum segment size.A new segment is started if either one of these criteria is exceeded. The oldest segment is overwritten after all segments were filled with data.
   - Enter your values at "Time period covered by a single segment" and "Maximum size of a segment".

     You include the size and number of single segments when entering the time period for single segments and their maximum size. A new single segment is started if either one of those conditions is exceeded. In addition, the oldest single segment is deleted after the criterion for "Time period of all segments" is exceeded.
   - Select the date and time for the start of the first segment change at "Time of first segment change".

     The segment is changed even if the configured size is exceeded after Runtime starts. In this case, the oldest individual segment is also deleted.

##### Create alarm class with logging

To create an alarm class with logging, proceed as follows:

1. Open the "HMI alarms" editor.
2. Click the "Alarm Classes" tab.
3. Select the alarm class whose alarms are logged.
4. In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Settings &gt; Alarm log".
5. Assign the alarm to be logged to this alarm class.

##### Example for the timing of the first segment change

A segment changes for the first time at 23:59 on January 17. The next time, the segment changes at the configured time in the cycle defined in "Time period contained in a single segment". If the cycle setting is "1 day", then the change will take place at 23:59 every day. If the cycle is set to "1 month", the segment will change at 23.59 on the 17th day of the next month.

---

**See also**

[Basics on alarm logging (RT Professional)](#basics-on-alarm-logging-rt-professional)
  
[Logging Settings (RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#logging-settings-rt-professional)
  
[Defining the Log Size and Segmentation (RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#defining-the-log-size-and-segmentation-rt-professional)
  
[Creating alarm classes (RT Professional)](#creating-alarm-classes-rt-professional)
  
[Working with Logs (RT Professional)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-rt-professional)

#### Configuring the Alarm Log Backup (RT Professional)

##### Principle

Make regular backups of your log data to ensure complete documentation of your process.

> **Note**
>
> The backup normally starts 15 minutes after the first time-related segment change. To start the backup and the segment synchronously with Runtime, define the time for the segment change before you start Runtime.
>
> You can enter comments for alarms displayed in the alarm view in Runtime. If the log segment in which the alarm is stored has already been swapped out, the comment will not be accepted in the swapped-out log. The comment will only be in the local log segment.
>
> If the archive segment has not yet been moved out, then the changed comment is accepted permanently.

##### Requirement

- The settings for logging are open.

##### Procedure

To create a backup of the log segments, proceed as follows:

1. Double-click "Logging" in the area navigator.
2. Enable "Alarm log &gt; Backup".

   ![Procedure](images/72357512459_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72357512459_DV_resource.Stream@PNG-en-US.png)
3. In the Inspector window, click "Properties &gt; General &gt; Settings Backup &gt; Path".
4. Click ![Procedure](images/6315966347_DV_resource.Stream@PNG-de-DE.png) and look for an existing folder in which to store the backup file. Use "Make New Folder" to create a new folder, if necessary. You can also use a network path as the storage location.

   ![Procedure](images/72357507979_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72357507979_DV_resource.Stream@PNG-en-US.png)
5. Activate "Backup" to generate a backup copy of logged data.

   Also activate "Backup to both paths" if a backup copy of logged data is to be saved to the "Path" and to the "Alternative path" folders.

   You can also use a network path as the storage location.

   If the "Backup to both paths" option is not enabled, the second backup file is used in the following situations:

   - If the storage space on a backup medium is full.
   - The original storage location is unavailable due to network failure, for example.

   An alarm is output if a storage location was not found, provided you configured corresponding system alarms.
6. Activate the "Sign" check box if the backup file must be saved with signature.

   When the connection to WinCC is reestablished, the signature is used to detect whether any changes have been made to a backup file since it was swapped out.

**Note**

The "Sign" option puts a load on the RAM. If you use log signing, the maximum size of a single segment must not exceed 200 MB.

##### Result

The log segment backup is stored in the specified location.

##### Structure of the Backup File

A backup file for an alarm log has the following structure:

- Extension

  A log segment backup consists of two files in "*.LDF" and "*.MDF" format. To transfer a backup to another PC, simply copy both files.
- File name

  The file name is in the following form: "&lt;Computer_name&gt;_&lt;Project_name&gt;_&lt;Type&gt;_&lt;Time_from&gt;_&lt;Time_to&gt;".

| Component | Explanation | Example |
| --- | --- | --- |
| Computer name |  | FLEX-LOG2 |
| Project ID | The project ID is assigned by the system. Underscores are replaced with "#". | HMI#4ZQV |
| Type | The type identification of the alarm log is "ALG" (Archive Log). |  |
| Time_from | The time period is specified in yyyymmddhhmm format. | 200812021118 for December 2, 2008, 11:18. |
| Time_to |  |  |
| Example of the complete file name of a backup file:  FLEX-LOG2_HMI#4ZQV_ALG_200811291414_200812030502.ldf |  |  |

> **Note**
>
> **Assignment to project**
>
> The project name cannot be seen in the file name of the generated project ID.
>
> To be able to allocate the backup files to the project, assign a path name to the storage location that contains the project name.

##### Signing the Backup File

If signing and backup are enabled, each log backup file is signed when swapped out. When the file is reconnected to WinCC, it is thus determined whether the file was changed after being swapped out.

If you use log signing, the maximum size of a single segment must not exceed 200 MB.

The "Enable signing" check box must be enabled for data verification. When signing is enabled, it takes longer to link the log backup file to WinCC. Up to 500 values are logged per second.

> **Note**
>
> If you disable signing off to establish a fast connection to the backup files, for example, you should avoid segment changes while it is disabled. After having closed the connection, re-enable signing so that the data to be logged is assigned a signature.

---

**See also**

[Basics on alarm logging (RT Professional)](#basics-on-alarm-logging-rt-professional)
  
[Working with Logs (RT Professional)](Working%20with%20logs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-logs-rt-professional)

#### Connecting and Disconnecting the Alarm Log Backup (RT Professional)

##### Introduction

To access the data in a swapped-out alarm log in Runtime, connect the log backup to the project. You can configure an automatic connection or connect the alarm log to the project via a script. The archived alarms are displayed in Runtime in the alarm view.

If you no longer want to access the backup of a log segment in Runtime, disconnect the log backup from the project.

##### Requirement

- The relevant backup files in "*. ldf" and "*.mdf" format are stored locally.
- The project is in Runtime.

##### Display Time Range

The alarms are only displayed in Runtime if the time window in the alarm view has been configured accordingly.

##### Example

You have configured a time window to display only the alarms of the past 24 hours. If you connect to a log backup containing alarms that are older than 24 hours, these alarms are not included in the alarm view.

##### Connecting to the alarm log automatically

To automatically connect to the alarm log backup, proceed as follows:

1. Insert the log backup files in the "RuntimeProjectPath\ProjectName\CommonArchiving" folder.
2. In Runtime, the alarm log is automatically connected to the project.

If signing is enabled, signed log backup files that are changed will not be connected automatically. A WinCC system alarm is generated and an entry is added to the Windows event log in the "Application" section.

##### Connecting to the alarm log using a script

Using the "AlarmLogs" VBS object, you can link the log backup files to the project using a script. The log segments are then copied with the "Restore" VBS method to the Common Archiving folder of the Runtime project. For additional information, see the description of the "AlarmLogs" VBS object and the "Remove" VBS method.

##### Automatically disconnecting the alarm log

To automatically disconnect the alarm log backup from the project, proceed as follows:

1. Go to the folder "RuntimeProjectPath\ProjectName\CommonArchiving".
2. Remove the log backup files from the folder.

##### Disconnecting the alarm log using a script

Using the "AlarmLogs" VBS object, you can disconnect the log backup files from the project using a script. The log segments are then removed with the "Remove" VBS method from the Common Archiving folder of the Runtime project. For additional information, see the description of the "AlarmLogs" VBS object and the "Remove" VBS method.

---

**See also**

[Basics on alarm logging (RT Professional)](#basics-on-alarm-logging-rt-professional)

#### Accessing the Log Database Directly with C-API/ODK (RT Professional)

##### Introduction

Various providers offer interfaces that you can use to access databases. These interfaces also allow you to directly access the WinCC log databases. Using direct access you can, for example, read process values to process them further in spreadsheet programs.

##### Accessing the log database with C-API/ODK

You can use the "WinCC Open Development Kit" option to access WinCC data and functions via open application programmer interfaces.

##### Additional information

You will find further information on this topic in the documentation for the WinCC Open Development Kit.

---

**See also**

[Basics on alarm logging (RT Professional)](#basics-on-alarm-logging-rt-professional)

#### Accessing the Log Database Directly with ADO/OLE DB  (RT Professional)

##### Introduction

Various providers offer interfaces that you can use to access databases. These interfaces also allow you to directly access the WinCC log databases. Using direct access you can, for example, read process values to process them further in spreadsheet programs.

##### Accessing the log databases with ADO/OLE DB

Some process values are stored in the log databases in compressed format. Use the WinCC OLE DB Provider to access these compressed process values. For non-compressed data and data from the alarm log, you can also use the Microsoft ADO/OLE DB interfaces, for example. You can use Visual Basic, Visual C++, etc., as the programming language.

> **Note**
>
> If you access the log database directly using ADO/OLE DB, remember that the log structure may be different in a new version of WinCC.

##### Additional information

You will find more detailed information on this topic on the Internet at:

[msdn.microsoft.com](http://msdn.microsoft.com/en-us/library/default.aspx)

---

**See also**

[Basics on alarm logging (RT Professional)](#basics-on-alarm-logging-rt-professional)

#### Configuring the Reloading of Alarms after a Power Failure (RT Professional)

##### Introduction

Configure the reloading of alarms so that the most recent alarms are displayed in runtime once more after a power failure. In the event of a power failure, the number of alarms that you configured is read from the alarm log. This allows the most recent process image to be reconstructed.

> **Note**
>
> Configuring the reloading of alarms after a power failure for redundant systems is not permitted.

##### Procedure

To define the number of alarms that are reloaded after a power failure, follow these steps:

1. Double-click "Runtime settings" in the project navigation under your HMI device.
2. Double-click "Alarms" in the area navigator.
3. Select "Properties &gt; General &gt; Number of alarm list entries after power failure" in the Inspector window to enter the number of alarms to be reloaded after power failure.

##### Result

After power failure, the number of alarms you configured is reloaded to the alarm view and displayed in runtime.

---

**See also**

[Basics on alarm logging (RT Professional)](#basics-on-alarm-logging-rt-professional)

## Using Alarms in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Alarms in Runtime (Basic Panels)](#alarms-in-runtime-basic-panels)
- [Alarms in Runtime (Panels, Comfort Panels, RT Advanced)](#alarms-in-runtime-panels-comfort-panels-rt-advanced)
- [Using the Alarm Window or Alarm View (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-alarm-window-or-alarm-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Using the Simple Alarm Window, Alarm View (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-simple-alarm-window-alarm-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Using the Alarm Indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-the-alarm-indicator-basic-panels-panels-comfort-panels-rt-advanced)
- [Acknowledging alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#acknowledging-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [Filtering alarms (Panels, Comfort Panels, RT Advanced)](#filtering-alarms-panels-comfort-panels-rt-advanced)

### Alarms in Runtime (Basic Panels)

#### Alarms

Alarms indicate events and states on the HMI device which have occurred in the system, in the process or on the HMI device itself. A status is reported when it is received.

An alarm could trigger one of the following alarm events:

- Incoming
- Outgoing
- Acknowledge
- Loop-in-alarm

The configuration engineer defines which alarms must be acknowledged by the user.

An alarm may contain the following information:

- Date
- Time
- Alarm text
- Location of fault
- Status
- Alarm class
- Alarm number
- Alarm group

#### Alarm classes

Alarms are assigned to various alarm classes.

- "Warnings"

  Alarms of this class usually indicate states of a plant such as "Motor switched on". Alarms in this class do not require acknowledgement.
- "Errors"

  Alarms in this class must always be acknowledged. Error alarms normally indicate critical errors within the plant such as "Motor temperature too high".
- "System"

  System alarms indicate states or events which occur on the HMI device.

  System alarms provide information on occurrences such as operator errors or communication faults.
- Custom alarm classes

  The properties of this alarm class must be defined in the configuration.

#### Alarm buffer

Alarm events are saved to an internal buffer. The size of this alarm buffer depends on the HMI device type.

The "Persistent alarm buffer" setting is used to switch the alarm buffer on and off in Runtime. For storage space reasons it can be necessary to switch off the alarm buffer.

The setting "Persistent alarm buffer" is activated under "Runtime Settings &gt; Alarms". In this setting the alarm view displays both current alarms and also alarms from the alarm buffer

If you switch off the alarm buffer you need to restart Runtime in order that the alarm view no longer displays the alarms from the alarm buffer.

#### Alarm view

The alarm view shows selected alarms or alarm events from the alarm buffer. Whether alarm events have to be acknowledged or not is specified in your configuration.

#### Alarm window

The alarm window is not assigned to any screen. Depending on the configuration the alarm window is opened when an alarm that belongs to a specific alarm class is active.

You can configure the order in which the alarms are displayed. You can choose to display the alarms in ascending or descending order of their occurrence. The alarm window can also be set to indicate the exact location of the fault, including the date and time of the alarm event. By means of configuration, the display can be filtered in such a way that only alarms that contain a specific character string will be shown.

#### Alarm indicator

The alarm indicator is a graphic symbol that is displayed on the screen when an alarm of the specified alarm class is activated.

The alarm indicator can have one of two states:

- Flashing: At least one unacknowledged alarm is pending.
- Static: The alarms are acknowledged but at least one of them is not yet deactivated. The number indicates the number of queued alarms.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Alarm window, alarm view in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-window-alarm-view-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basic alarm view, alarm window in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basic-alarm-view-alarm-window-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
  
[Alarm indicator in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-indicator-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
  
[Acknowledging alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#acknowledging-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Filtering alarms (Panels, Comfort Panels, RT Advanced)](#filtering-alarms-panels-comfort-panels-rt-advanced)

### Alarms in Runtime (Panels, Comfort Panels, RT Advanced)

#### Alarms

Alarms indicate events and states on the HMI device which have occurred in the system, in the process or on the HMI device itself. A status is reported when it is received.

An alarm could trigger one of the following alarm events:

- Incoming
- Outgoing
- Acknowledge

The configuration engineer defines which alarms must be acknowledged by the user.

An alarm may contain the following information:

- Date
- Time
- Alarm text
- Location of fault
- Status
- Alarm class
- Alarm number
- Alarm group

#### Alarm classes

Alarms are assigned to various alarm classes.

- "Warnings"

  Alarms of this class usually indicate states of a plant such as "Motor switched on". Alarms in this alarm class do not require acknowledgment.
- "Errors"

  Alarms in this class must always be acknowledged. Error alarms normally indicate critical errors within the plant such as "Motor temperature too high".
- "System"

  System alarms indicate states or events which occur on the HMI device.

  System alarms provide information on occurrences such as operator errors or communication faults.
- "Diagnosis Events"

  SIMATIC diagnostic alarms show states and events in the SIMATIC S7 controller.
- "Safety Warnings"

  The "Safety Warnings" alarm class shows alarms for fail-safe operation. Users do not acknowledge alarms from this alarm class.
- STEP 7 alarm classes

  The alarm classes configured in STEP 7 are also available to the HMI device.
- Custom alarm classes

  The properties of this alarm class are defined in the configuration.

#### Alarm buffer

Alarm events are saved to an internal buffer. The size of this alarm buffer depends on the HMI device type.

> **Note**
>
> **Valid for Panels and RT Advanced**
>
> The "Persistent alarm buffer" setting is used to switch the alarm buffer on and off in Runtime. For storage space reasons it can be necessary to switch off the alarm buffer.
>
> The setting "Persistent alarm buffer" is activated under "Runtime Settings &gt; Alarms". In this setting the alarm view displays both current alarms and also alarms from the alarm buffer
>
> If you switch off the alarm buffer you need to restart Runtime in order that the alarm view no longer displays the alarms from the alarm buffer.

#### Alarm report

When alarm logging is enabled in the project, alarms are output directly to the printer.

You can set the logging function separately for each alarm. Printing of such an alarm is initiated when the "incoming" and "outgoing" alarm events are generated.

The output of alarms of the "System" alarm class to a printer must be initiated by means of the corresponding alarm buffer. This outputs the content of the alarm buffer to the printer. To be able to initiate this print function, you need to configure an operating element in the project.

> **Note**
>
> **Valid for Panels and RT Advanced**
>
> When alarm report is enabled in the project, alarms are only printed after Runtime has been closed.

#### Alarm log

Alarm events are stored in an alarm log, provided this log file is configured. The capacity of the log file is limited by the storage medium and system limits.

#### Alarm view

The alarm view shows selected alarms or events from the alarm buffer or alarm log. Whether alarm events have to be acknowledged or not is specified in your configuration. By means of configuration, the display can be filtered in such a way that only alarms that contain a specific character string in their alarm text are shown.

#### Alarm window

The alarm window is not assigned to any screen. Depending on the configuration the alarm window is opened when an alarm that belongs to a specific alarm class is active. Depending on the configuration, it is not closed until the alarm is acknowledged.

You can configure the order in which the alarms are displayed. At the first position, the current, or the oldest alarm will be displayed. The alarm window can also be set to indicate the exact location of the fault, including the date and time of the alarm event. By means of configuration, the display can be filtered in such a way that only alarms that contain a specific character string in their alarm text are shown.

#### Alarm indicator

The alarm indicator is a graphic symbol that is displayed on the screen when an alarm of the specified alarm class is activated.

The alarm indicator can have one of two states:

- Flashing: At least one unacknowledged alarm is pending.
- Static: The alarms are acknowledged but at least one of them is not yet deactivated. The number indicates the number of queued alarms.

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[Alarm window, alarm view in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-window-alarm-view-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basic alarm view, alarm window in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basic-alarm-view-alarm-window-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
  
[Alarm indicator in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-indicator-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
  
[Acknowledging alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#acknowledging-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Filtering alarms (Panels, Comfort Panels, RT Advanced)](#filtering-alarms-panels-comfort-panels-rt-advanced)

### Using the Alarm Window or Alarm View (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Alarm window, alarm view in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-window-alarm-view-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
- [Using the Alarm Window, Alarm View (Panels, Comfort Panels, RT Advanced)](#using-the-alarm-window-alarm-view-panels-comfort-panels-rt-advanced)

#### Alarm window, alarm view in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

Alarms are indicated in the alarm view or in the alarm window on the HMI device. The layout and operation of the alarm window correspond to that of the alarm view.

The alarm window is not assigned to any screen. Depending on the configuration the alarm window is opened when an alarm that belongs to a specific alarm class is active. Depending on the configuration, it is not closed until the alarm is acknowledged.

![Application](images/72427749259_DV_resource.Stream@PNG-en-US.png)

##### Layout

Depending on the configuration, in the alarm view different columns with information regarding an alarm or an alarm event are displayed. If a filter is configured, only alarms that contain a specific string in the alarm text will be displayed.

To differentiate between the different alarm classes, the first column in the alarm view contains an icon:

| Symbol | Alarm class |
| --- | --- |
| ! | "Errors" |
| Empty | "Warnings" |
| depends on the configuration | Custom alarm classes |
| $ | "System" |
| S7 | "Diagnosis Event" |
| !! | "Safety Warnings" |

##### Operation

You use the alarm view as follows, depending on how it is configured:

- Change the order of the columns.
- Change the order in which the alarms are displayed.
- Acknowledging alarms
- Editing alarms

##### Operator controls

The buttons have the following functions:

| Button | Function |
| --- | --- |
| ![Operator controls](images/72429387787_DV_resource.Stream@PNG-de-DE.png) | Displaying a tooltip for an alarm |
| ![Operator controls](images/72429294091_DV_resource.Stream@PNG-de-DE.png) | Loop-In-Alarm  Executes the configured function (for example: "ActivateScreen") with each keystroke. It is hereby possible to call a screen containing your information about the selected alarm.  Also acknowledges an alarm requiring acknowledgment. <sup>1)</sup> |
| ![Operator controls](images/72429391883_DV_resource.Stream@PNG-de-DE.png) | Acknowledge alarm |

<sup>
1)</sup> Only if a function is configured for the selected alarm for the "loop-in-alarm" event.

##### Operation behavior

**Linked alarm window for touch panels**

When configuring the alarm window for keyboard units, enable the "Connected" (modal) property under "Properties &gt; Mode". This ensures that the alarm window does not defocus during screen changes. Switching back and forth between the screen and different windows with &lt;Ctrl+TAB&gt; is not supported. If the linked alarm window has the focus, then the buttons in the screen behind it cannot be operated. The functions configured on a function key are carried out.

##### Changing the order of the displayed alarms

When you click on the column, first of all alarms requiring acknowledgment are sorted according to date and time. Then those alarms that do not require acknowledgment are sorted according to date and time.

---

**See also**

[Using the Alarm Window, Alarm View (Panels, Comfort Panels, RT Advanced)](#using-the-alarm-window-alarm-view-panels-comfort-panels-rt-advanced)
  
[Alarms in Runtime (Panels, Comfort Panels, RT Advanced)](#alarms-in-runtime-panels-comfort-panels-rt-advanced)
  
[Alarms in Runtime (Basic Panels)](#alarms-in-runtime-basic-panels)

#### Using the Alarm Window, Alarm View (Panels, Comfort Panels, RT Advanced)

##### Introduction

As an alternative to using the mouse, you can operate the alarm view and the alarm window using the &lt;TAB&gt; key on your HMI device. This allows you to select the button and the most recently selected alarm in the alarm view. Depending on the configuration, you can also operate the alarm view via the function keys.

##### Operation using the mouse

1. Select the alarm to be edited.
2. Click the button whose function you want to run.

##### Operation using the keyboard

1. Press the &lt;Tab&gt; key until the list of displayed alarms is selected in the alarm view.
2. Click on the alarm to be edited. Use the &lt;Up&gt; and &lt;Down&gt; keys accordingly.
3. Press the &lt;Tab&gt; key until the button whose function you wish to use is selected.
4. Press &lt;Enter&gt;.

##### Change the order of the columns

1. Select the column header, such as the "Date" column header.
2. While holding down the mouse button, drag the column header to the column header "Time".

   The "Date" column is in front of the "Time" column.

##### Change the sorting

You can sort the list according to date or time.

1. Click on the corresponding column header.

   The list is sorted in descending or ascending order according to this criterion.
2. Click the same column header again to reverse the sort order.

##### Acknowledge alarm

1. Click on the alarm to be edited.
2. Click the ![Acknowledge alarm](images/72429910539_DV_resource.Stream@PNG-de-DE.png)button.

##### Loop-In-Alarm trigger

1. Click on the alarm to be edited.
2. Click the ![Loop-In-Alarm trigger](images/72429914379_DV_resource.Stream@PNG-de-DE.png)button.

   The screen containing information about the alarm is displayed.

**Note**

If you trigger a Loop-In-Alarm during an unacknowledged alarm, it is acknowledged automatically.

##### Displaying configured tooltip

1. Click on the alarm concerned.
2. Click the ![Displaying configured tooltip](images/72429918219_DV_resource.Stream@PNG-de-DE.png) button.

   The tooltip configured for the alarm is displayed.

---

**See also**

[Alarm window, alarm view in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-window-alarm-view-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)

### Using the Simple Alarm Window, Alarm View (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basic alarm view, alarm window in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basic-alarm-view-alarm-window-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
- [Basic alarm view, using the alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basic-alarm-view-using-the-alarm-window-basic-panels-panels-comfort-panels-rt-advanced)

#### Basic alarm view, alarm window in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

The simple alarm view shows selected alarms or alarm events from the alarm buffer. The layout and operation of the simple alarm window correspond to that of the simple alarm view.

> **Note**
>
> The "Single alarm view" object is not assigned dynamic functions by means of scripting.
>
> In the Engineering System, for example, dynamize the visibility of an object in the "Animations" tab of the Inspector window. In Runtime, the "Simple alarm view" does not support animations. If you configured an animation and, for example, run a consistency check on the project, an error alarm is displayed in the output window.

![Application](images/73681114891_DV_resource.Stream@PNG-de-DE.png)

##### Layout

Depending on the configuration, in the alarm view different columns with information regarding an alarm or an alarm event are displayed.

To differentiate between the different alarm classes, the first column in the alarm view contains an icon:

| Icon | Alarm class |
| --- | --- |
| ! | "Errors" |
| empty | "Warnings" |
| depends on the configuration | Custom alarm classes |
| $ | "System" |

##### Operation

You use the alarm view as follows, depending on how it is configured:

- Acknowledging alarms
- Editing alarms

##### Control elements

The buttons have the following functions:

| Button | Function |
| --- | --- |
| ![Control elements](images/73681035019_DV_resource.Stream@PNG-de-DE.png) | Acknowledge alarm |
| ![Control elements](images/73681074443_DV_resource.Stream@PNG-de-DE.png) | Loop-In-Alarm  Executes the configured function (e.g.: "ActivateScreen") whenever a key is pressed. This enables a screen that contains your information on the selected alarm to be called.  Also acknowledges an alarm that requires acknowledgment. <sup>1)</sup> |
| ![Control elements](images/73681101067_DV_resource.Stream@PNG-de-DE.png) | Displaying a tooltip for an alarm |
| ![Control elements](images/73681209611_DV_resource.Stream@PNG-de-DE.png) | Displays the full text of the selected alarm in a separate window, namely the alarm text window  In the alarm text window, you can view alarm texts that exceed the space available in the Alarm view. Close the alarm text window with the ![Control elements](images/8602317963_DV_resource.Stream@PNG-de-DE.png) button. |
| ![Control elements](images/73681141515_DV_resource.Stream@PNG-de-DE.png) | Scrolls one alarm up. |
| ![Control elements](images/73681155339_DV_resource.Stream@PNG-de-DE.png) | Scrolls one page up in the alarm view. |
| ![Control elements](images/73681169163_DV_resource.Stream@PNG-de-DE.png) | Scrolls one page down in the alarm view. |
| ![Control elements](images/73681195787_DV_resource.Stream@PNG-de-DE.png) | Scrolls one alarm down. |

<sup>
1)</sup> Only if a function is configured for the selected alarm for the event "Loop-In-Alarm".

##### Format of the control elements

The display of the buttons for using the simple alarm view depends on the configured size. You should therefore check on the HMI device whether all the required buttons are available.

---

**See also**

[Basic alarm view, using the alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basic-alarm-view-using-the-alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
  
[Alarms in Runtime (Panels, Comfort Panels, RT Advanced)](#alarms-in-runtime-panels-comfort-panels-rt-advanced)
  
[Alarms in Runtime (Basic Panels)](#alarms-in-runtime-basic-panels)

#### Basic alarm view, using the alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

As an alternative to using the mouse, you can operate the simple alarm view using the &lt;TAB&gt; key on your HMI device. This allows you to select the button and the most recently selected alarm in the alarm view. Depending on the configuration, you can also operate the alarm view via the function keys.

##### Operation using the mouse

1. Select the alarm to be edited.
2. Click the button whose function you want to run.

##### Operation using the keyboard

1. Press the &lt;Tab&gt; key until the list of displayed alarms is selected in the alarm view.
2. Click on the alarm to be edited. Use the &lt;Up&gt; and &lt;Down&gt; keys accordingly.
3. Press the &lt;Tab&gt; key until the button whose function you wish to use is selected.
4. Press &lt;Enter&gt;.

##### Acknowledge alarm

1. Select the alarm to be acknowledged.
2. Click the ![Acknowledge alarm](images/6307773323_DV_resource.Stream@PNG-de-DE.png)button.

##### Loop-In-Alarm trigger

1. Select the alarm to be edited.
2. Click the ![Loop-In-Alarm trigger](images/6307781899_DV_resource.Stream@PNG-de-DE.png)button.

   The screen containing information about the alarm is displayed.

##### Calling the infotext

1. Select the alarm to be edited.
2. Click the ![Calling the infotext](images/6307803019_DV_resource.Stream@PNG-de-DE.png)button.
3. To close the window for displaying the operator note, press the ![Calling the infotext](images/6307811339_DV_resource.Stream@PNG-de-DE.png) button or use the key combination &lt;Alt+F4&gt;.

---

**See also**

[Basic alarm view, alarm window in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basic-alarm-view-alarm-window-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)

### Using the Alarm Indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Alarm indicator in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-indicator-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)
- [Operating the alarm indicator using the mouse (Panels, Comfort Panels, RT Advanced)](#operating-the-alarm-indicator-using-the-mouse-panels-comfort-panels-rt-advanced)

#### Alarm indicator in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

The alarm indicator is displayed if alarms of the specified alarm class are pending or require acknowledgment.

![Application](images/6308617227_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The alarm indicator can have one of two states:

- Flashing: At least one unacknowledged alarm is pending.
- Static: The alarms are acknowledged but at least one of them is not yet deactivated. The number indicates the number of queued alarms.

##### Operation

Depending on the configuration, when operating the alarm indicator an alarm window is opened. The icons from the symbol library can only be operated with a mouse or touch screen.

> **Note**
>
> **Device dependency**
>
> Operation with mouse is not available for all HMI devices.

---

**See also**

[Operating the alarm indicator using the mouse (Panels, Comfort Panels, RT Advanced)](#operating-the-alarm-indicator-using-the-mouse-panels-comfort-panels-rt-advanced)
  
[Alarms in Runtime (Panels, Comfort Panels, RT Advanced)](#alarms-in-runtime-panels-comfort-panels-rt-advanced)
  
[Alarms in Runtime (Basic Panels)](#alarms-in-runtime-basic-panels)

#### Operating the alarm indicator using the mouse (Panels, Comfort Panels, RT Advanced)

##### Operation using the mouse

1. Click on the alarm indicator with the mouse pointer. Depending on the configuration, the Alarm window is open.
2. Click ![Operation using the mouse](images/8602317963_DV_resource.Stream@PNG-de-DE.png) to close the alarm window. The Alarm window can be opened again by clicking on the alarm indicator.

---

**See also**

[Alarm indicator in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-indicator-in-runtime-basic-panels-panels-comfort-panels-rt-advanced)

### Acknowledging alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

You can acknowledge alarms in Runtime according to your project configuration settings. You can acknowledge alarms as follows:

- Using the display and control object buttons
- Using the "ACK" key on your HMI device
- Using individually-configured function keys or buttons

If an operator authorization is configured for an individual control, the alarms can only be acknowledged by authorized users.

To automatically acknowledge alarms in Runtime, use the system functions and scripts, plus the "Acknowledgment by the PLC" option.

> **Note**
>
> **Device dependency**
>
> Scripts are not available for all HMI devices.

#### Acknowledgment variants

You acknowledge individual alarms or multiple alarms together in Runtime. They are distinguished as follows:

- Single acknowledgment

  Acknowledgment of an alarm using a button or a function key.
- Acknowledge alarm groups

  Acknowledgment of all the alarms of an alarm group using a button or a function key.

#### Requirement

- An alarm is displayed on the HMI device.

#### Procedure

To acknowledge an alarm, proceed as follows:

1. Select the alarm.
2. If you are using an alarm view or an alarm window, click the ![Procedure](images/72429910539_DV_resource.Stream@PNG-de-DE.png) button.
3. If you are using a simple alarm view or a simple alarm window, click the ![Procedure](images/6307773323_DV_resource.Stream@PNG-de-DE.png) button.
4. Press the "ACK" button on your HMI device to acknowledge an alarm in an alarm line.

**Note**

**Device dependency**

The extended alarm view or alarm window and the alarm line are not available for all HMI devices.

#### Result

The alarm status changes to "Acknowledged". If the condition for triggering an alarm no longer applies, the alarm status also changes to "Outgoing", and it is no longer displayed on the HMI device.

---

**See also**

[Filtering alarms (Panels, Comfort Panels, RT Advanced)](#filtering-alarms-panels-comfort-panels-rt-advanced)
  
[Alarms in Runtime (Basic Panels)](#alarms-in-runtime-basic-panels)
  
[Alarms in Runtime (Panels, Comfort Panels, RT Advanced)](#alarms-in-runtime-panels-comfort-panels-rt-advanced)

### Filtering alarms (Panels, Comfort Panels, RT Advanced)

#### Introduction

The alarm view in Runtime does not contain a control element for entering filter criteria. To provide this functionality, configure an I/O field using the "Screens" editor.

#### Requirements

- A filter has been configured for the alarm view.
- An I/O field for entering the criterion is displayed.
- Alarms are displayed in Runtime.

#### Enable filter

1. Enter the filter string in the I/O field.
2. Confirm your input.

   The alarm view displays only those alarms that are contained in the specified character string. Thereby this distinguishes between upper and lower case letters.

#### Disable filter

1. Delete the string from the I/O field that is used to filter the alarm view.
2. Confirm your input.

   All alarms are displayed in the alarm view once more.

---

**See also**

[Acknowledging alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#acknowledging-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring alarm filtering (Panels, Comfort Panels, RT Advanced)](#configuring-alarm-filtering-panels-comfort-panels-rt-advanced)
  
[Alarms in Runtime (Basic Panels)](#alarms-in-runtime-basic-panels)
  
[Alarms in Runtime (Panels, Comfort Panels, RT Advanced)](#alarms-in-runtime-panels-comfort-panels-rt-advanced)

## Using Alarms in Runtime (RT Professional)

This section contains information on the following topics:

- [Alarms in Runtime (RT Professional)](#alarms-in-runtime-rt-professional)
- [Alarm view (RT Professional)](#alarm-view-rt-professional)
- [Alarm View Buttons (RT Professional)](#alarm-view-buttons-rt-professional)
- [Filtering Alarms in Runtime (RT Professional)](#filtering-alarms-in-runtime-rt-professional)
- [Sorting Alarms in Runtime (RT Professional)](#sorting-alarms-in-runtime-rt-professional)
- [Toggling the Alarm View in Runtime (RT Professional)](#toggling-the-alarm-view-in-runtime-rt-professional)
- [Displaying logged alarms in Runtime (RT Professional)](#displaying-logged-alarms-in-runtime-rt-professional)
- [Printing Alarms in Runtime (RT Professional)](#printing-alarms-in-runtime-rt-professional)
- [Locking Alarms in Runtime (RT Professional)](#locking-alarms-in-runtime-rt-professional)
- [Acknowledgement of Alarms (RT Professional)](#acknowledgement-of-alarms-rt-professional)

### Alarms in Runtime  (RT Professional)

#### Alarms

Alarms indicate events and states on the HMI device which have occurred in the system, in the process or on the HMI device itself. A status is reported when it is received.

An alarm could trigger one of the following alarm events:

- Incoming
- Outgoing
- Acknowledge

The configuration engineer defines which alarms must be acknowledged by the user.

An alarm may contain the following information:

- Date
- Time
- Alarm text
- Location of fault
- Status
- Alarm class
- Alarm number
- Alarm group

#### Alarm classes

Alarms are assigned to various alarm classes.

- "Warnings"

  Alarms of this class usually indicate states of a plant such as "Motor switched on". Alarms in this alarm class do not require acknowledgment.
- "Errors"

  Alarms in this class must always be acknowledged. Error alarms normally indicate critical errors within the plant such as "Motor temperature too high".
- "System"

  System alarms indicate states or events which occur on the HMI device.

  System alarms provide information on occurrences such as operator errors or communication faults.
- "Diagnosis Events"

  SIMATIC diagnostic alarms show states and events in the SIMATIC S7 controller.
- "Safety Warnings"

  The "Safety Warnings" alarm class shows alarms for fail-safe operation. Users do not acknowledge alarms from this alarm class.
- STEP 7 alarm classes

  The alarm classes configured in STEP 7 are also available to the HMI device.
- Custom alarm classes

  The properties of this alarm class are defined in the configuration.

#### Alarm buffer

Alarm events are saved to an internal buffer. The size of this alarm buffer depends on the HMI device type.

> **Note**
>
> **Valid for Panels and RT Advanced**
>
> The "Persistent alarm buffer" setting is used to switch the alarm buffer on and off in Runtime. For storage space reasons it can be necessary to switch off the alarm buffer.
>
> The setting "Persistent alarm buffer" is activated under "Runtime Settings &gt; Alarms". In this setting the alarm view displays both current alarms and also alarms from the alarm buffer
>
> If you switch off the alarm buffer you need to restart Runtime in order that the alarm view no longer displays the alarms from the alarm buffer.

#### Alarm report

When alarm logging is enabled in the project, alarms are output directly to the printer.

You can set the logging function separately for each alarm. Printing of such an alarm is initiated when the "incoming" and "outgoing" alarm events are generated.

The output of alarms of the "System" alarm class to a printer must be initiated by means of the corresponding alarm buffer. This outputs the content of the alarm buffer to the printer. To be able to initiate this print function, you need to configure an operating element in the project.

> **Note**
>
> **Valid for Panels and RT Advanced**
>
> When alarm report is enabled in the project, alarms are only printed after Runtime has been closed.

#### Alarm log

Alarm events are stored in an alarm log, provided this log file is configured. The capacity of the log file is limited by the storage medium and system limits.

#### Alarm view

The alarm view shows selected alarms or events from the alarm buffer or alarm log. Whether alarm events have to be acknowledged or not is specified in your configuration. By means of configuration, the display can be filtered in such a way that only alarms that contain a specific character string in their alarm text are shown.

#### Alarm window

The alarm window is not assigned to any screen. Depending on the configuration the alarm window is opened when an alarm that belongs to a specific alarm class is active. Depending on the configuration, it is not closed until the alarm is acknowledged.

You can configure the order in which the alarms are displayed. At the first position, the current, or the oldest alarm will be displayed. The alarm window can also be set to indicate the exact location of the fault, including the date and time of the alarm event. By means of configuration, the display can be filtered in such a way that only alarms that contain a specific character string in their alarm text are shown.

#### Alarm indicator

The alarm indicator is a graphic symbol that is displayed on the screen when an alarm of the specified alarm class is activated.

The alarm indicator can have one of two states:

- Flashing: At least one unacknowledged alarm is pending.
- Static: The alarms are acknowledged but at least one of them is not yet deactivated. The number indicates the number of queued alarms.

### Alarm view (RT Professional)

#### Introduction

The "Alarm view" object displays alarms that occur during the process in a plant. You also use the alarm view to visualize alarms in list format. WinCC offers various views, such as "Current alarms" or "Historical alarm list" (short-term).

![Introduction](images/88074762635_DV_resource.Stream@PNG-de-DE.png)

In Runtime, you can use the &lt;TAB&gt; key to jump to different objects in succession to enter values, or click buttons. Alternatively you can use the alarm view with the mouse.

> **Note**
>
> An alarm appears in the alarm view with the date and time stamp crossed out in the following situations:
>
> - A locked alarm is unlocked.
> - An alarm is reloaded after a power failure. This applies only to chronological messaging.
> - The AS is restarted. This applies only to chronological messaging.

#### Requirement

- The "Loop-In-Alarm" button is configured in the alarm view.
- Cursor mode is set to "Tab cursor" for the screen.
- The objects are enabled for operation.
- The operator authorization is assigned.

#### Operation using the mouse

1. Click on the alarm to be edited.
2. Click on the operator control whose function you wish to use.

#### Operation using the keyboard

1. Press the &lt;Tab&gt; key until the list of displayed alarms is selected in the alarm view.
2. Click on the alarm to be edited. Use the &lt;Up&gt; and &lt;Down&gt; keys accordingly.
3. Press the &lt;Tab&gt; key until the operator control element you wish to use is selected.
4. Press &lt;Enter&gt;.

#### Alternative operation

Depending on the configuration, you can also operate the alarm view via the function keys.

#### Example: Change the order of the columns

The function can be configured. It is only available in Runtime if you have activated the alarm view "Font table &gt; Header column &gt; Sort" in the Inspector window.

1. Select the column header, such as the "Date" column header.
2. While holding down the mouse button, drag the column header to the column header "Time".

#### Example: Change the order of the columns

The function can be configured. It is only available in Runtime if you have activated the alarm view "Font table &gt; Header column &gt; Sort by column headers" in the Inspector window.

1. Click on the column header.
2. Click the same column header again to reverse the sort order.

#### Example: Loop-In-Alarm

Loop-In-Alarm triggers the configured change of screen to the screen containing information about the alarm.

1. Click on the alarm to be edited.
2. Click the "Loop-In-Alarm" button

#### Operation behavior

When Loop-In-Alarm is triggered for an unacknowledged alarm, it is acknowledged automatically.

---

**See also**

[Alarm View Buttons (RT Professional)](#alarm-view-buttons-rt-professional)
  
[Filtering Alarms in Runtime (RT Professional)](#filtering-alarms-in-runtime-rt-professional)
  
[Sorting Alarms in Runtime (RT Professional)](#sorting-alarms-in-runtime-rt-professional)
  
[Toggling the Alarm View in Runtime (RT Professional)](#toggling-the-alarm-view-in-runtime-rt-professional)
  
[Displaying logged alarms in Runtime (RT Professional)](#displaying-logged-alarms-in-runtime-rt-professional)
  
[Printing Alarms in Runtime (RT Professional)](#printing-alarms-in-runtime-rt-professional)
  
[Locking Single Alarms (RT Professional)](#locking-single-alarms-rt-professional)
  
[Acknowledging alarms (RT Professional)](#acknowledging-alarms-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

### Alarm View Buttons (RT Professional)

#### Introduction

The alarm view displays specific alarm lists in order to provide a better overview of the active alarms. These lists filter, and sort alarms by certain properties. You can individually define these properties, and how the lists are presented when you configure the alarm view.

#### Lists in the alarm view

You can display six different lists in the alarm window. To display the alarm lists in the alarm view, click the associated button on the alarm view's toolbar.

|  | List | Description |
| --- | --- | --- |
| ![Lists in the alarm view](images/21867060875_DV_resource.Stream@PNG-de-DE.png) | Alarm list | Shows the pending alarms. |
| ![Lists in the alarm view](images/21864489099_DV_resource.Stream@PNG-de-DE.png) | Short-term archive list | Shows the logged alarms.   The display is updated immediately when new incoming alarms occur. |
| ![Lists in the alarm view](images/21864492555_DV_resource.Stream@PNG-de-DE.png) | Long-term archive list | Shows the logged alarms.   The display is not updated immediately when new incoming alarms occur. |
| ![Lists in the alarm view](images/21867068043_DV_resource.Stream@PNG-de-DE.png) | Lock list | Shows the locked alarms. |
| ![Lists in the alarm view](images/21863635211_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics | Shows statistical information. |
| ![Lists in the alarm view](images/21867536011_DV_resource.Stream@PNG-de-DE.png) | List of Hidden Alarms | Shows the hidden alarms. Hidden alarms are also logged. |

> **Note**
>
> **Hidden system diagnostic alarms**
>
> For hidden system diagnostic alarms, the alarm texts are not displayed in the list of hidden alarms.
>
> The list of hidden alarms merely displays the configuration data of the alarm and not a live view.
>
> To display active hidden system diagnostic alarms, you must adjust the filter for the online alarm list.

#### Filtered alarm list

You use the filter of the alarms view to configure alarm views in which you display specific alarm lists. You can configure a filter for any alarm list. Configure a separate alarm view for each filtered alarm list.

> **Note**
>
> An alarm appears in the alarm list with the date and time stamp crossed out in the following situations:
>
> - A locked alarm is unlocked.
> - An alarm is reloaded after a power failure; for chronological alarms only.
> - The AS is restarted; for chronological alarms only.

---

**See also**

[Alarm view (RT Professional)](#alarm-view-rt-professional)
  
[Filtering Alarms in Runtime (RT Professional)](#filtering-alarms-in-runtime-rt-professional)

### Filtering Alarms in Runtime (RT Professional)

#### Introduction

In Runtime, you can set specific criteria that define the alarms to be displayed in the alarm view. In the example below, only alarms that contain the alarm text "Motor on" are displayed.

#### Requirement

The "Filter alarms" button ![Requirement](images/21863628043_DV_resource.Stream@PNG-de-DE.png) is configured in the alarm view.

#### Procedure

To filter alarms in the alarm view, proceed as follows:

1. Click the "Filter alarms" button in Runtime.

   The "Specify selection" dialog opens.
2. Double-click the "Text Blocks" folder in the tree structure, and click "Alarm Text". In the right pane, select the "Search string" option, and double-click "Search string".
3. The "Text input" dialog opens. Enter the search string "Motor on" and click "OK" to confirm.
4. In the "Specify selection" dialog, click "OK" to confirm your entries.

   The alarm view only shows the selected alarms.

In the "Specify selection" dialog, specify the start and end times, or search strings, for alarm text blocks such as the "Date" and "Time" system blocks. Your input must be in the format required in the dialog.

The following settings are available in the "Specify selection" dialog:

| Field | Description |
| --- | --- |
| Text filter by exact match | If the "Text filter by exact match" option is not enabled, all text blocks that contain the specified string of characters are selected.  If the "Text filter by exact match" option is enabled, all text blocks that correspond exactly to the specified string of characters are selected. |
| Persistence in RT | If the "Persistence in RT" option is enabled, changes to criteria are retained even after a screen change. |
| Persistence in CS and RT | If the "Persistence in RT and CS" option is enabled, the modified settings are also applied to the Engineering System. To do this, you must open the screen in the "Screens" editor, and save it again. The changed settings will also be used when you reactivate the project. |
| Delete filter | Use this button to delete all configured criteria. |

#### Filter by process values

You cannot enter text as the criterion for a process value.

To filter by the text of a process value block, or the process tags it represents, proceed as follows:

1. Insert this process value as the alarm text for a user text block in an alarm.
2. In Runtime, filter the alarms by the text in the "Alarm text" text block.

**Note**

In multi-station systems, make sure that contents displayed in the "Specify selection" dialog on a client have the same names on all servers.

When filtering by time, the start and stop values are not adjusted automatically when the timebase of the alarm view is changed.

Example: At the PC location with time zone "UTC + 1h", the alarm view has the "Local time zone" time base. You should filter by the time 10:00 to 11:00. Change the timebase from "Local time zone" to "UTC". If you want to display the same alarms, change the filter to 9:00 to 10:00.

---

**See also**

[Alarm view (RT Professional)](#alarm-view-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

### Sorting Alarms in Runtime (RT Professional)

#### Introduction

In Runtime, you can sort the alarms in the alarm view by column header.

Examples for sorting alarms:

- In descending order by date, time, and alarm number. The most recent alarm is displayed at the top.
- By priority

  You must have defined the priority of the alarms in the "HMI alarms" editor and configured the "Priority" alarm text block in the alarm view. As a result, in a single-line alarm view, only the top-priority alarm appears in the alarm window. A lower-priority alarm will not be displayed, even if it is more recent. The alarms are displayed in chronological order.
- The "Alarm status" alarm text block is sorted by the type of state and not by the configured status texts. For an ascending sort order, the following order is used:

  - Incoming
  - Outgoing
  - Acknowledged
  - Locked
  - Enabled
  - Automatic acknowledgment
  - Emergency acknowledgment
  - Incoming/outgoing

    > **Note**
    >
    > **Specifying sorting criteria in the ES for the alarm view**
    >
    > You can set the sort criteria to configure the alarm view as required. In the Inspector window of the alarm view, select "Properties &gt; Properties &gt; View &gt; Columns".

#### Sorting alarms

To sort the alarm view by column, define the sort order over up to four columns. An arrow and a number are shown on the right in the column header. The arrow indicates the sort order (ascending or descending). The number beside the arrow indicates the sort order of the column headers.

#### Requirement

- "Sort by click" or "Sort by double-click" is selected in the alarm view.

  Click on "Properties &gt; Properties &gt; Table &gt; Table - Sorting &gt; Settings".
- The "Autoscroll" button is activated in the alarm view.

  Click "Properties &gt; Properties &gt; Toolbar &gt; Toolbar buttons".

#### Procedure

To sort alarms in the alarm view by column, proceed as follows:

1. Click or double-click the column header by which you want to sort the alarms first.

   The number "1" is displayed, and the arrow points upwards for ascending sort order.

   - If sort order "Up and down" is enabled in the alarm view, each click or double-click in the column header toggles the sorting between the ascending and descending mode.
   - If sort order "Up, down, none" is enabled, then the sort order is cancelled after the 3rd click.
2. If you want to sort by several columns, click the column header in the required order.

**Note**

Sorting is not affected by events or changes to the alarm text block configuration.

An alarm text block corresponds to a field in an alarm. If you define an alarm text block as sorting criterion in the sort dialog and then remove this block from the alarm line under "Properties&gt; Properties &gt; Columns", the defined sort order remains unchanged. In the sort dialog, a blank field is displayed instead of the deleted alarm text block.

If you do not define another sort order order and reactivate the removed alarm text block in the alarm text block configuration, the alarms will be sorted in the original sort order once more.

---

**See also**

[Alarm view (RT Professional)](#alarm-view-rt-professional)

### Toggling the Alarm View in Runtime  (RT Professional)

#### Introduction

You filter the alarms to be displayed in the alarm view using preconfigured buttons.

#### Requirements

- The six buttons needed to display a certain selection of alarms are configured in the alarm view.

#### Procedure

To display a certain selection of alarms in the alarm view, follow these steps:

- Click on one of the following buttons in the alarm view:

  ![Procedure](images/21867060875_DV_resource.Stream@PNG-de-DE.png) Alarm list, to view alarms pending

  ![Procedure](images/21864489099_DV_resource.Stream@PNG-de-DE.png) Historical alarm list (short-term), to view logged alarms

  The display is updated immediately when new incoming alarms occur.

  ![Procedure](images/21864492555_DV_resource.Stream@PNG-de-DE.png) Historical alarm list (long-term), to view logged alarms

  ![Procedure](images/21867068043_DV_resource.Stream@PNG-de-DE.png) Lock list, to view the locked alarms

  ![Procedure](images/21863635211_DV_resource.Stream@PNG-de-DE.png) Alarm statistics, to view statistical information

  ![Procedure](images/21867536011_DV_resource.Stream@PNG-de-DE.png) List of hidden alarms, to view alarms which are logged but not visible.

---

**See also**

[Alarm view (RT Professional)](#alarm-view-rt-professional)

### Displaying logged alarms in Runtime (RT Professional)

#### Introduction

In Runtime, the alarm view displays alarms from the log, in addition to the current alarms.

#### Requirements

- All the archived data that you intend to display in Runtime must be stored locally on the archive server. The SQL server does not allow access to backup files held elsewhere, such as another computer on the network.
- The "Historical alarm list (short-term)" and "Historical alarm list (long-term)" buttons are configured in the alarm view.

#### Procedure

To show logged alarms in Runtime, follow these steps:

1. In the alarm view, click on the "Historical alarm list (short-term)" button to display logged and current alarms. Any new incoming alarms will be immediately updated in the historical alarm list (short-term).

-OR-

1. In the alarm view, click on the "Historical alarm list (long-term)" button to display only logged alarms. The historical alarm list (long-term) only displays logged alarms. You can enter or view comments in the historical alarm list (long-term).

---

**See also**

[Alarm view (RT Professional)](#alarm-view-rt-professional)

### Printing Alarms in Runtime (RT Professional)

#### Introduction

You have the following options for printing alarms in Runtime, depending on the settings made in the "HMI alarms" and "Reports" editors:

**Print alarm sequence report**

If the alarm sequence report is activated, all alarm status transitions in Runtime are output continuously to a printer. No operator input is needed in Runtime.

**Printing report**

The operator input in Runtime depends on your configuration. Your options for printing an alarm report in Runtime are as follows:

- Time-driven output

  - One-off, time-driven output, e.g. at the start of a shift
  - Repeated output at specific intervals, such as every two hours
- Event-driven output

  - Change in value of a tag
  - By clicking a configured button in a screen
  - Click the ![Introduction](images/44734647691_DV_resource.Stream@PNG-de-DE.png) button in the alarm view
  - Overflow of a log
  - Script

> **Note**
>
> Please note that only ASCII characters are supported when printing alarms directly in Runtime.

#### Requirement

- Several alarms are displayed on the HMI device.

#### Procedure

To print the current view in the alarm window in Runtime, follow these steps:

1. Filter the alarm view using the alarm view controls, if necessary.
2. Click the ![Procedure](images/44734647691_DV_resource.Stream@PNG-de-DE.png) button in the alarm view.

#### Result

The alarms displayed in the alarm window are output to the printer that you configured in the "Reports" editor.

#### Printer settings

Configure the printer in the HMI device's Control Panel. The settings will depend on which operating system is used on the HMI device. For detailed information, refer to the operating instructions of your HMI device and to the "[Reporting alarms](#reporting-alarms-panels-comfort-panels-rt-advanced-rt-professional)" chapter.

---

**See also**

[Alarm view (RT Professional)](#alarm-view-rt-professional)
  
[Working with reports (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-reports-panels-comfort-panels-rt-advanced-rt-professional-1)

### Locking Alarms in Runtime (RT Professional)

This section contains information on the following topics:

- [Locking Single Alarms (RT Professional)](#locking-single-alarms-rt-professional)
- [Locking alarms by means of alarm number (RT Professional)](#locking-alarms-by-means-of-alarm-number-rt-professional)
- [Locking Alarms using the Alarm Class or Alarm Group (RT Professional)](#locking-alarms-using-the-alarm-class-or-alarm-group-rt-professional)

#### Locking Single Alarms (RT Professional)

> **Note**
>
> **Locking and unlocking of PLC alarms**
>
> The following applies for locking and unlocking S7 PLC alarms:
>
> - S7-1500: Not available
> - S7-300 and S7-400: Not available for SFC-based alarms
>
>   S7-400: Locking/unlocking an Alarm_8(P) alarm by means of S7PMC always causes all 8 alarms of this block to be locked or unlocked.

##### Introduction

If you lock an alarm, this alarm will not be displayed, and will not be logged. You can lock single alarms, alarm classes or alarm groups as required.

> **Note**
>
> **Locked alarm:**
>
> Locked alarms are automatically unlocked when WinCC Runtime restarts. Only alarms that are locked directly in the AS by means of data blocks will continue to be locked (locking at source).
>
> **Locked alarm classes / alarm groups:**
>
> The locked state of alarm classes and alarm groups is not affected by a restart of WinCC Runtime.

##### Requirement

- The alarm view has been configured.
- The alarm view is displayed in Runtime.
- The "Lock alarm/Unlock alarm" ![Requirement](images/22575029515_DV_resource.Stream@PNG-de-DE.png) / ![Requirement](images/22575032971_DV_resource.Stream@PNG-de-DE.png) and "Locked alarms" buttons are configured.
- You are authorized to lock, and unlock alarms.

  > **Note**
  >
  > The "Disable alarms" and "Enable alarms" authorizations must be configured directly one under the other. This is necessary because the authorization level used automatically for the "Enable alarms" authorization is directly below the "Disable alarms" authorization.

##### Procedure

To lock alarms and prevent them being displayed using the button, follow these steps:

1. Select the alarm that you want to lock from the alarm view.
2. Click the "Disable alarm" button.

   The alarm is removed from the alarm list.
3. To display all locked alarms, click the "Locked alarms" button.

   The lock list is displayed.
4. Select the alarm that you want to unlock.
5. Click the "Unlock alarm" button.

   The alarm is displayed again and removed from the lock list.

---

**See also**

[Locking alarms by means of alarm number (RT Professional)](#locking-alarms-by-means-of-alarm-number-rt-professional)
  
[Locking Alarms using the Alarm Class or Alarm Group (RT Professional)](#locking-alarms-using-the-alarm-class-or-alarm-group-rt-professional)
  
[Alarm view (RT Professional)](#alarm-view-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

#### Locking alarms by means of alarm number (RT Professional)

##### Requirements

- The "Lock dialog" button ![Requirements](images/21867543179_DV_resource.Stream@PNG-de-DE.png) is configured in the alarm view.

##### Procedure

Proceed as follows to lock alarms and prevent them being displayed using the alarm number:

1. Click ![Procedure](images/21867543179_DV_resource.Stream@PNG-de-DE.png).

   The "Configure Lock List" dialog opens.

   ![Procedure](images/72360265099_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72360265099_DV_resource.Stream@PNG-en-US.png)
2. Click a server in the server list, or click the local PC for single-station projects.
3. Click the "Add" button. In the subsequent dialog, enter the alarm number that you want to lock.
4. You can lock multiple alarms at the same time. To do this, enter the alarm numbers, separated by commas. Enter a range of numbers in the format "5-10". Only contiguous number ranges are locked. If there are gaps in the specified range, an "Invalid range" message is output.
5. To unlock a locked alarm, select the alarm from the list of locked alarms, and click the "Delete" button.

**Note**

You cannot lock, or unlock more than 50 alarms at the same time.

---

**See also**

[Locking Single Alarms (RT Professional)](#locking-single-alarms-rt-professional)

#### Locking Alarms using the Alarm Class or Alarm Group (RT Professional)

##### Introduction

You can also lock alarms to prevent them from being displayed by locking the entire alarm class, or the alarm group to which the alarm belongs. None of the alarms from these locked alarm groups and alarm classes will be displayed.

##### Requirements

- The "Lock dialog" button ![Requirements](images/21867543179_DV_resource.Stream@PNG-de-DE.png) is configured in the alarm view.

##### Procedure

To lock, or unlock alarms via the alarm class, or the alarm group, proceed as follows:

1. In the alarm view, click the ![Procedure](images/21867543179_DV_resource.Stream@PNG-de-DE.png) button.

   The "Configure Lock List" dialog opens.

   ![Procedure](images/72360265099_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72360265099_DV_resource.Stream@PNG-en-US.png)
2. Click a server in the server list, or click the local PC for single-station projects.
3. In the tree structure, select an alarm class or user-defined alarm group that you want to lock.
4. Click the "Lock" button.

   All alarms from this alarm class or user-defined alarm group are locked.

To unlock the alarms, select the alarm class or user-defined alarm group and click on the "Unlock" button.

##### Operator input alarm when an alarm is locked

You can define in the alarm view, whether an operator input alarm is generated when an alarm is locked or unlocked. You can configure the operator input alarm yourself. It contains the following objects by default:

- A time stamp
- The user logged on

The time stamp for the alarm originates as follows:

- From the alarm source (such as an AS) for active locking.

Actively-locked alarms are visible, and can be used on all HMI devices.

---

**See also**

[Locking Single Alarms (RT Professional)](#locking-single-alarms-rt-professional)

### Acknowledgement of Alarms (RT Professional)

This section contains information on the following topics:

- [Acknowledging alarms (RT Professional)](#acknowledging-alarms-rt-professional)
- [Group Alarm Acknowledgement (RT Professional)](#group-alarm-acknowledgement-rt-professional)
- [Emergency acknowledgment of alarms (RT Professional)](#emergency-acknowledgment-of-alarms-rt-professional)
- [Acknowledging an alarm annunciator (RT Professional)](#acknowledging-an-alarm-annunciator-rt-professional)

#### Acknowledging alarms  (RT Professional)

##### Introduction

You can acknowledge alarms in Runtime according to your project configuration settings. You can acknowledge alarms as follows:

- Using the display and control object buttons
- With customized buttons

If an operator authorization is configured for an individual control, the alarms can only be acknowledged by authorized users.

To bypass the acknowledgement in Runtime, WinCC contains system functions and scripts that allow you to acknowledge alarms automatically.

##### Acknowledgement variants

You acknowledge individual alarms or multiple alarms together in Runtime. The following options are possible:

- Single acknowledgment

  Acknowledgment of an alarm using a button or a function key.
- Acknowledge alarm groups

  Acknowledgement of all the alarms of an alarm group using a button, or a function key.
- Group acknowledgement

  Acknowledgment of all pending alarms that require acknowledgment in the alarm view using the "Group acknowledgment" button of the alarm view.
- Dual-mode acknowledgment

  If an alarm requires dual-mode acknowledgment, you acknowledge both the incoming, and the outgoing alarm.

##### Requirement

- An alarm is displayed on the HMI device.
- The "Group acknowledgment" and "Single acknowledgment" buttons are configured in the alarm view.

##### Procedure

To acknowledge an alarm, follow these steps:

- Select the alarm.
- Click "Single acknowledgment" in the alarm view.

##### Result

The alarm status is set to "Acknowledged". If the trigger condition for an alarm no longer applies, the alarm status is also set to "outgoing" and no longer displayed on the HMI device.

---

**See also**

[Group Alarm Acknowledgement (RT Professional)](#group-alarm-acknowledgement-rt-professional)
  
[Emergency acknowledgment of alarms (RT Professional)](#emergency-acknowledgment-of-alarms-rt-professional)
  
[Acknowledging an alarm annunciator (RT Professional)](#acknowledging-an-alarm-annunciator-rt-professional)
  
[Alarm view (RT Professional)](#alarm-view-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

#### Group Alarm Acknowledgement (RT Professional)

##### Introduction

The acknowledgement of all pending, and visible alarms in the alarm window that need to be acknowledged is known as a group acknowledgement. If the "Single alarm" option is not selected for an alarm, you can trigger a group acknowledgment.

##### Requirement

There are several alarms that require acknowledgement in the alarm view.

##### Procedure

To group-acknowledge an alarm, follow these steps:

1. Read the alarm texts of the queued alarms and initiate remedial action, if necessary.
2. In the alarm view, click the ![Procedure](images/21866163339_DV_resource.Stream@PNG-de-DE.png) button.

##### Result

All queued alarms with the following properties are acknowledged:

- Requires acknowledgement
- Does not require acknowledgement
- Visible

---

**See also**

[Acknowledging alarms (RT Professional)](#acknowledging-alarms-rt-professional)

#### Emergency acknowledgment of alarms (RT Professional)

##### Introduction

In exceptional situations, the operator acknowledges an alarm based on its alarm number. The acknowledgment bit is sent to the AS even if the alarm is currently not pending. This function is only intended for use in imminent emergency situations.

##### Requirement

The ![Requirement](images/21868663947_DV_resource.Stream@PNG-de-DE.png) button is configured in the alarm view.

##### Procedure

To acknowledge an alarm in Runtime using an emergency acknowledgement, follow these steps:

1. Click the ![Procedure](images/21868663947_DV_resource.Stream@PNG-de-DE.png) button in the alarm view.

   The "Emergency Acknowledgment for Alarms" dialog opens.

   ![Procedure](images/72377193867_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72377193867_DV_resource.Stream@PNG-en-US.png)
2. Select a server.
3. To enter the alarm number, select "Alarm number".
4. Click the "Send acknowledge job" button.

   The alarm then appears in the alarm view in the color that you defined for an acknowledged alarm.

**Note**

In the dialog for selecting the servers, only server projects whose "Packages" are loaded onto the PC are shown.

---

**See also**

[Acknowledging alarms (RT Professional)](#acknowledging-alarms-rt-professional)

#### Acknowledging an alarm annunciator (RT Professional)

##### Introduction

The way you acknowledge an alarm annunciator in Runtime will depend on how you configured its acknowledgement.

##### Requirements

- The alarm annunciator and its acknowledgment are configured.
- The alarm annunciator is triggered.
- The "Alarm annunciator acknowledgment" and "Single acknowledgment" buttons are configured in the alarm view.

##### Acknowledgment using a separate key

- To acknowledge the alarm annunciator, click the "Alarm annunciator acknowledgment" button in the alarm view.

  You only acknowledge the alarm annunciator. The alarm that triggered the alarm annunciator is still set to "incoming" status.

##### Single acknowledgment

- To acknowledge the alarm annunciator, select the current alarm, and click the "Single acknowledgment" button in the alarm view.

  You thereby acknowledge the alarm annunciator and the alarm that triggered the alarm annunciator.

##### Acknowledgment tag

If the alarm annunciator is acknowledged using a tag, acknowledge the alarm annunciator using a customized button or function key, etc.

##### Result

This sets the acknowledgment bit of the alarm annunciator.

---

**See also**

[Acknowledging alarms (RT Professional)](#acknowledging-alarms-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

## Displaying security events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Displaying security events on the HMI device (Panels, Comfort Panels, RT Advanced, RT Professional)](#displaying-security-events-on-the-hmi-device-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the display of security events (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-display-of-security-events-panels-comfort-panels-rt-advanced-rt-professional)

### Displaying security events on the HMI device (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can also view security events on the HMI device for existing alarms from WinCC.

Security events are, for example, an attack on a device over the network or a change of the protection level for communication between the controller and the HMI device.

Security events are detected by the controller and forwarded to the HMI devices. The security events are displayed in the alarm log on the HMI devices.

A configuration or activation of the security events functionality is not necessary within the controller. Security events are automatically detected by the controller.

#### Restrictions

You can display security events from the following controllers on the HMI device:

- SIMATIC S7-1200
- SIMATIC S7-1500

> **Note**
>
> **Device dependency**
>
> The security events of controllers are not displayed on Basic Panels and Basic Panels 2nd Generation.

#### Configuring the display of security events

The following steps are required to display security events on the HMI device:

- Selection of controller alarms
- Creation of an alarm log for controller alarms

You can find more detailed information on configuration here:[Configuring the display of security events](#configuring-the-display-of-security-events-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[Configuring the display of security events (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-display-of-security-events-panels-comfort-panels-rt-advanced-rt-professional)

### Configuring the display of security events (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Requirements

A HMI connection is established between the HMI device and PLC.

#### Procedure

1. Open the "Runtime settings" of the HMI device.
2. Enable the "Security events" function under "Alarms".

   > **Note**
   >
   > The "Security events" function is deactivated by default and must be activated for each HMI connection.
3. Create a new alarm log in the "Log" editor under "Alarm logs".
4. Open an HMI screen.
5. Create an alarm view.

#### Result

The security events are displayed in the alarm log.

## Sending a complete alarm from the controller to the HMI device (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Sending a complete alarm from the controller to the HMI device and automatic update (Panels, Comfort Panels, RT Advanced)](#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-panels-comfort-panels-rt-advanced)
- [Sending a complete alarm from the controller to the HMI device and automatic update (RT Professional)](#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-rt-professional)
- [Configuring automatic update of controller alarms on the HMI device (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-automatic-update-of-controller-alarms-on-the-hmi-device-panels-comfort-panels-rt-advanced-rt-professional)

### Sending a complete alarm from the controller to the HMI device and automatic update (Panels, Comfort Panels, RT Advanced)

#### Basics

In addition to alarms in WinCC, you can configure controller alarms in STEP 7 and show them on your HMI device.

When controller alarms are configured in STEP 7, a connection to an S7-1500 controller is established, and controller alarms are currently pending, the controller alarms are automatically updated and sent to the HMI devices after alarm changes (e.g. change of the alarm text). This will save you time because you do not have to load configuration changes of the alarms to the HMI device separately. The HMI device does not need to exit Runtime operation when the alarms are changed.

The following controller alarms can be sent to the HMI device:

- System diagnostics
- ProDiag alarms
- Program alarms

The controller alarms can be sent completely to the HMI devices with device version V14 if the corresponding settings are configured in the controller and on the HMI device. The option "Automatic update" must be activated on the HMI device for the respective connection under "Runtime settings Alarms &gt; Controller alarms". You can find additional information on the settings under [Configuring automatic update of controller alarms on the HMI device](#configuring-automatic-update-of-controller-alarms-on-the-hmi-device-panels-comfort-panels-rt-advanced-rt-professional).

#### Device dependency

The controller alarms of the following controller are sent automatically and completely to the HMI device when they occur:

- SIMATIC S7-1500 (firmware version 2.0 and higher)

Basic Panels and Basic Panels 2nd Generation do not support controller alarms. For Basic Panels and Basic Panels 2nd Generation as well as HMI devices with a device version before V14, configuration changes of the alarms must be loaded to the controller and the HMI device.

When "Automatic update" is deactivated in the HMI device, configuration changes of the alarms must be loaded to the controller and the HMI device.

> **Note**
>
> When upgrading a project to the TIA Portal version V14, the transfer of controller alarms to the HMI device is deactivated under the "Runtime settings" of the HMI device because the connection between the HMI device and the respective controller was created in an older TIA Portal version.

#### Language settings

For alarms to be displayed in the correct language on the HMI device, the same three languages or fewer must be configured for the alarms in the controller and on the HMI device. You might have to coordinate the language selection with the control project engineer.

If different languages are configured on the HMI device and in the controller, the HMI device shows the text "###Text missing###" rather than the controller alarms during operation.

> **Note**
>
> If you want to use more than three languages simultaneously on the HMI device, you must deactivate the option for automatic update of the controller alarms. Otherwise, "##Text missing##" is displayed instead of the controller alarms for the fourth and any additional language.

**Special considerations for Asian fonts**

When using Asian languages, only the Asian characters that were used in configuring the HMI device are loaded to the HMI device during the transfer. If the texts are sent directly from the controller to the HMI device, you might encounter display problems. You can load the complete Asian font to the HMI device in these cases. You can find additional information at [Loading Asian fonts to the HMI device](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#loading-asian-fonts-to-the-hmi-device-panels-comfort-panels-rt-advanced).

#### Notes and rules

- Modified texts that you load to the controller are displayed immediately on the HMI device when the controller alarm has already been triggered.
- If the property "Alarm &gt; Basic settings &gt; Information only" was selected for a controller alarm, this controller alarm is not displayed in the alarm view in WinCC.
- The following applies to alarms that are displayed in the alarm log:

  - The alarm log includes alarms in the set language. This language is set during configuration of the HMI device under "Runtime settings &gt; General &gt; Logs &gt; Logging language". Regardless of whether you set a specific language for logging of the controller alarms in the alarm log or select the default language, the respective language must also be activated in the controller. When you specify startup language, this can lead to mixed languages in the alarm log in conjunction with the "Automatic update" option. You can find additional information on language selection of the log in Runtime under [Log response to language switching in runtime](#log-response-to-language-switching-in-runtime-panels-comfort-panels-rt-advanced).
  - The check box "Log event text and error location" must be selected for the respective alarm log under "Properties &gt; Properties &gt; Logging method" so that the logged controller alarms are displayed in the alarm view or in the alarm window.
  - The info texts of the alarms are not logged and show "###Text missing###" when an alarm log is displayed in runtime.
  - If an alarm text contains more than six values, only the first six values are saved in the log file after logging. An alarm view configured for the display of the logs shows all values contained in the alarm text.

---

**See also**

[Loading Asian fonts to the HMI device (Panels, Comfort Panels, RT Advanced)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#loading-asian-fonts-to-the-hmi-device-panels-comfort-panels-rt-advanced)
  
[Configuring automatic update of controller alarms on the HMI device (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-automatic-update-of-controller-alarms-on-the-hmi-device-panels-comfort-panels-rt-advanced-rt-professional)
  
[Log response to language switching in runtime (Panels, Comfort Panels, RT Advanced)](#log-response-to-language-switching-in-runtime-panels-comfort-panels-rt-advanced)

### Sending a complete alarm from the controller to the HMI device and automatic update (RT Professional)

#### Basics

In addition to alarms in WinCC, you can configure controller alarms in STEP 7 and show them on your HMI device.

When controller alarms are configured in STEP 7, a connection to an S7-1500 controller is established and controller alarms are currently pending, the controller alarms are automatically sent to the HMI devices and updated in case of changes (e.g. change to alarm text). This enables you to save time as you do not have to load the configuration changes of the alarms to the HMI device separately. The HMI device does not need to exit Runtime operation when the alarms are changed.

The following controller alarms can be sent to the HMI device:

- System diagnostics
- Process diagnostics
- Program alarms

The controller alarms can be sent in their entirety to the HMI devices with device version V14 if the corresponding settings are configured in the controller and on the HMI device. On the HMI device, the "Automatic update" option must be activated under "Runtime Settings &gt; Alarms &gt; Controller alarms" for the relevant connection. You can find additional information on the settings under [Configuring automatic update of controller alarms on the HMI device](#configuring-automatic-update-of-controller-alarms-on-the-hmi-device-panels-comfort-panels-rt-advanced-rt-professional).

#### Device dependency

When they occur, the controller alarms of the following controller are automatically sent in their entirety to the HMI device:

- SIMATIC S7-1500 (as of firmware version 2.0.)

Basic Panels and Basic Panels 2nd Generation do not support controller alarms. For Basic Panels and Basic Panels 2nd Generation as well as HMI devices with a device version lower than V14, the configuration changes of the alarms must be loaded to the controller and the HMI device.

If "Automatic update" is deactivated in the HMI device, the configuration changes of the alarms must be loaded to the controller and the HMI device.

> **Note**
>
> When upgrading a project to the TIA Portal version V14, the transfer of the controller alarms to the HMI device under "Runtime Settings" of the HMI device is deactivated because the connection between the HMI device and the respective controller was created in an older TIA Portal version.

#### Language settings

For alarms to be displayed in the correct language on the HMI device, the same three languages (or fewer) must be configured for the alarms in the controller and on the HMI device. You may have to coordinate the language selection with the configuration engineer.

If different languages are configured on the HMI device and in the controller, the HMI device in operation shows the text "###Text missing###" instead of the control alarms.

> **Note**
>
> If you want to use more than three languages simultaneously on the HMI device, you must deactivate the option for automatic update of the controller alarms. Otherwise, "##Text missing##" is displayed instead of the controller alarms for the fourth and any additional language.

---

**See also**

[Editing controller alarms (RT Professional)](#editing-controller-alarms-rt-professional)
  
[Controller alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#controller-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring automatic update of controller alarms on the HMI device (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-automatic-update-of-controller-alarms-on-the-hmi-device-panels-comfort-panels-rt-advanced-rt-professional)

### Configuring automatic update of controller alarms on the HMI device (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The option "Automatic update" is selected by default for all connections between the S7-1500 controllers (firmware version 2.0) and the HMI devices with the device version V14.

If the connection between an HMI device and an S7-1500 controller was created in a TIA Portal version before V14, the option "Automatic update" is deactivated even after upgrading the project to version V14. You can configure automatic updating of the controller alarms later for this connection.

"Automatic update" must be active if text-list tags are used in controller alarms.

#### Requirements

- There is an HMI connection between the HMI device and an S7-1500 controller (firmware version 2.0 or later) or a compatible device (for example, WinAC 1500).
- Controller and HMI device have at least version 14 or later.
- "Central alarm management" is activated in the controller (automatic updating was activated for the controller).
- Controller alarms were configured in STEP 7.
- An alarm view or an alarm window was configured on the HMI device.
- The alarm classes associated with the controller alarms are selected in the alarm view or in the alarm window.
- The same three languages (or fewer) are configured in the controller and on the HMI device for alarms.

#### Procedure

1. Open the "Runtime settings" of the HMI device.

   One or more connections to controllers are displayed under "Alarms &gt; Controller alarms".
2. Activate the "Automatic update" option for the respective connection for which you want to display the controller alarms.

   The "Automatic update" function must be activated separately for each connection.

> **Note**
>
> If the languages configured for the controller differ from those for the HMI device, the alarms cannot be displayed in Runtime. Instead, the alarm "##Text missing##" is displayed.

> **Note**
>
> If you want to use more than three languages simultaneously on the HMI device, you must deactivate the "Automatic update" option. Otherwise, the alarm "##Text missing##" is displayed instead of the controller alarms for the fourth and any additional language.

#### Result

In Runtime, the controller alarms are displayed in the alarm view.

---

**See also**

[Sending a complete alarm from the controller to the HMI device and automatic update (RT Professional)](#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-rt-professional)
  
[Sending a complete alarm from the controller to the HMI device and automatic update (Panels, Comfort Panels, RT Advanced)](#sending-a-complete-alarm-from-the-controller-to-the-hmi-device-and-automatic-update-panels-comfort-panels-rt-advanced)

## Reference (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Alarm events (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-events-basic-panels-panels-comfort-panels-rt-advanced)
- [Alarm events (RT Professional)](#alarm-events-rt-professional)
- [System functions for logs (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-logs-panels-comfort-panels-rt-advanced-rt-professional)
- [Structure of *.csv files that contain alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-of-csv-files-that-contain-alarms-panels-comfort-panels-rt-advanced-rt-professional)
- [Description of the System Blocks (RT Professional)](#description-of-the-system-blocks-rt-professional)
- [SQL Statements for Filtering the Alarm View (RT Professional)](#sql-statements-for-filtering-the-alarm-view-rt-professional)
- [System events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [System events (RT Professional)](#system-events-rt-professional)
- [Tag Bit Assignments (RT Professional)](#tag-bit-assignments-rt-professional)

### System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### System functions

System functions are predefined functions you can use to implement many tasks in runtime, even with no programming knowledge. You use system functions in a function list or in a script.

> **Note**
>
> **Device dependency**
>
> Scripts are not available for all HMI devices.

The table shows all the system functions available for displaying and editing alarms.

| System function | Effect |
| --- | --- |
| EditAlarm | Triggers the "Loop-In-Alarm" event for the selected alarm or for the last selected alarm in case of multiple selection. If the alarm to be edited has not yet been acknowledged, the selected alarm is also acknowledged. |
| ClearAlarmBuffer | Deletes alarms from the alarm buffer on the HMI device. |
| ClearAlarmBufferProtoolLegacy | Function such as "ClearAlarmBuffer". This system function has been retained to ensure compatibility and uses the old ProTool numbering. |
| AlarmViewUpdate | Updates the alarm view. |
| ▸AlarmViewLoopInAlarm | Triggers the "Loop-In-Alarm" event for the selected alarm or for the last selected alarm in case of multiple selection. If the alarm to be edited has not yet been acknowledged, the selected alarm is also acknowledged. |
| AlarmViewAcknowledgeAlarm | Acknowledges the alarms that are selected in the specified alarm view. |
| AlarmViewShowOperatorNotes | Displays the configured tooltip for the alarm selected in the specified alarm view. |
| AcknowledgeAlarm | Acknowledges all selected alarms. |
| SetAlarmReportMode | Switches the automatic reporting of alarms on the printer on or off. |
| ShowAlarmWindow | Hides or shows the alarm window on the HMI device. |
| ShowSystemEvent | Displays the value of the delivered parameter as a system event on the HMI device. |

> **Note**
>
> **Device dependency**
>
> The following system functions are not available for all HMI devices:
>
> - SetAlarmReportMode
> - AlarmViewUpdate
> - ShowSystemEvent

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)
  
[System functions for logs (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-logs-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure of *.csv files that contain alarms (Panels, Comfort Panels, RT Advanced, RT Professional)](#structure-of-csv-files-that-contain-alarms-panels-comfort-panels-rt-advanced-rt-professional)
  
[Description of the System Blocks (RT Professional)](#description-of-the-system-blocks-rt-professional)
  
[SQL Statements for Filtering the Alarm View (RT Professional)](#sql-statements-for-filtering-the-alarm-view-rt-professional)
  
[Basics on system events (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-system-events-basic-panels-panels-comfort-panels-rt-advanced)
  
[Bit assignment of status tag (RT Professional)](#bit-assignment-of-status-tag-rt-professional)
  
[Bit assignment for lock tags (RT Professional)](#bit-assignment-for-lock-tags-rt-professional)

### Alarm events  (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Alarm events and their display and control objects

In Runtime, the following alarm events are triggered by their display and control objects. You can configure a function list for every event.

| Object | Configurable events |
| --- | --- |
| Alarms | Incoming  Outgoing  Acknowledge  Loop-In-Alarm |
| Alarm view | Enabling  Disable  Selection changed |
| Alarm indicator | Click  Click when flashing |

> **Note**
>
> **Device dependency**
>
> The following events in the alarm view are not available for all HMI devices:
>
> - Enabling
> - Disable
> - Selection changed
> - Click
> - Click when flashing

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)

### Alarm events (RT Professional)

#### Alarm events and their display and control objects

In Runtime, the following alarm events are triggered by their display and control objects. You can configure a function list for every event.

| Object | Configurable events |
| --- | --- |
| Alarms | Incoming  Outgoing  Acknowledge  Loop-In-Alarm  Status changed |
| Alarm view | Activate  Loaded  Click toolbar button  Property changed  Change toolbar button property  Property status bar element change  Block property modified  Property column changed  Property alarm statistics column changed  Property operator input alarm changed |

---

**See also**

[Alarm Logging in WinCC (Panels, Comfort Panels, RT Advanced)](#alarm-logging-in-wincc-panels-comfort-panels-rt-advanced)

### System functions for logs (Panels, Comfort Panels, RT Advanced, RT Professional)

#### System functions

The following system functions are available for logging:

| Function name | Function method |
| --- | --- |
| ArchiveLogFile | This function moves or copies a log to another storage location for long-term archiving. Use the system function, for example, to move the audit trail from a local storage medium to the server. When handling audit trails, always use the "Move log (hmiMove)" mode in order to avoid noncompliance with FDA guidelines as a result of redundant data storage. |
| LogTag | Saves the value of the given tags in the given data log. Use the system function to log a process values at a specific time. |
| StartLogging | Starts the logging process in the specified log. You can interrupt logging in Runtime by calling the "StopLogging" system function. |
| StopLogging | Stops the logging process in the specified log. To resume logging in Runtime, select the "StartLogging" system function. |
| ClearLog | Deletes all entries in the specified log. |
| StartNextLog | Stops the logging process in the specified log. Logging is continued in the sequential log that has been configured for the specified log file. |
| CloseAllLogs | Closes all logs. The connection between WinCC and the log files or log database is terminated. You can use this system function, for example, to enable hot-swapping of the storage medium on the HMI device without exiting the Runtime software. |
| OpenAllLogs | Opens all logs to resume logging. The connection between WinCC and the log files or log database is recovered. |
| CopyLog | Copies the contents of the specified log to another log. |

---

**See also**

[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Structure of *.csv files that contain alarms (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can save an alarm log as a file in "*.csv" format. CSV stands for **C**omma **S**eparated **V**alue. In this format, the table columns that contain the names and the value of the entry are separated by semicolons. Each table row terminates with a line break.

#### Example of a log file in *.csv format

This example shows a file with logged alarms:

"Time_ms";"MsgProc";"StateAfter";"MsgClass";"MsgNumber";"Var1";...;"Var8";"TimeString";"MsgText";"PLC"37986550590,27;1;1;3;110001;"";...;"";"30.06.99 13:12:51";"Change to operating mode 'online'";37986550682,87;1;1;3;140010;"";...;"";"30.06.99 13:12:59";"Connection established: PLC_1, Station 2, Rack 0, Position 2";

> **Note**
>
> **Separators**
>
> To display the contents of "*.CSV" archives, you must ensure that the same character is not used for "Decimal separator" and "List separator" under Windows settings for "Region and language".

#### Structure of a log file in *.csv format

The following values are entered in the log file columns:

| Parameters | Description |
| --- | --- |
| Time_ms | Specify a time stamp as a decimal value ( see below for conversion) |
| Msg_Proc | Alarm procedures:   0 = Unknown alarm procedure  1 = System event  2 = Alarm bit procedure (operating alarms)  3 = Alarm number procedure ALARM_S  4 = Diagnostics event  7 = Analog alarm procedure  9 = Program alarms  100 = Alarm bit procedure (fault alarms) |
| State after | Alarm event:   0 = Incoming/Outgoing  1 = Incoming  2 = Incoming/Acknowledged/Outgoing  3 = Incoming/Acknowledged  4 = All alarms in the PLC were deleted with SFC106 or after PLC STOP/RUN an alarm is pending  6 = Incoming/Outgoing/Acknowledged |
| Msg_Class | Alarm class:   0 = No alarm class  1 = "Errors"  2 = "Warnings"  3 = "System"  4 = "Diagnostic Events"  64 ... = User-configured alarm classes |
| Msg Number | Alarm number |
| Var1 to Var8 | Value of the dynamic parameters as STRING |
| Time string | Time stamp, as STRING in legible data format |
| Msg text | Alarm in a readable STRING |
| PLC | Alarm localization (relevant PLC) |

#### Conversion of the time stamp decimal value

To further process the time stamp value using a different program, proceed as follows:

1. Divide Time_ms by 1,000,000.

   Example: 37986476928 : 1,000,000 = 37986.476928
2. The whole number portion (37986) is the date calculated from 12/31/1899.

   In Excel you can now convert the time stamp into days. To do this, assign to the cell that contains the time stamp, a respective format form the "Date" group.

   Result: 37986 results in 12/31/2003
3. The value after the point (0.476928) indicates the time:

   - Multiply the value (0.476928) by 24 to obtain the hours (11.446272).
   - Multiply the remainder (0.446272) by 60 results in the minutes (26.77632).
   - Multiply the remainder (0.77632) by 60 results in the seconds (46.5792).

   Result 11:26:46.579

   This conversion is supported by Microsoft Excel, for example.

---

**See also**

[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Description of the System Blocks (RT Professional)

#### Introduction

System blocks allow you to specify predefined information that is not freely utilizable, such as date, time and duration.

The value of the alarm text block (such as the time of day) is displayed in the alarm. The description of the system blocks provides information on the individual system blocks.

#### Overview

| System block | Description | Default length |
| --- | --- | --- |
| Date | Date of the "incoming", "outgoing", and "acknowledged" alarm statuses. | 8 |
| Time | Time of the "incoming", "outgoing", and "acknowledged" alarm statuses.   Accuracy of a WinCC time stamp: 1 s.  Display accuracy: 10 ms. | 9 |
| Duration | Time period between the "incoming", "outgoing", and "acknowledged" statuses.   There is only one column for duration:  - The column remains blank for alarms with "incoming" status. - For alarms with "outgoing" status, the time that elapses between "incoming" and "outgoing" is displayed. - When alarms are acknowledged, the time between "incoming" and "outgoing" is displayed. | 8 |
| Daylight Saving Time/Standard Time | Indicates whether daylight saving time is set. | 1 |
| Status | Indicates the alarm status, such as "Incoming" or "Outgoing".  The state texts displayed in this system block are configured in the alarm class and depend on the selected list of the alarm view. | 1 |
| Acknowledgment status | Indicates whether an alarm has been acknowledged.  The state texts displayed in this system block are configured in the alarm class and depend on the selected list of the alarm view. | 1 |
| ID | Alarm number | 3 |
| Alarm class | Alarm class The text is user-defined. | 8 |
| Controller/CPU number | Number of the CPU and AS in which the alarm was triggered.   In Runtime, the value of this system block is not taken from the AS but rather is taken from the configured data for the alarm. The value has no function in communication with the AS. | 2 |
| Tag | Tag name for the operator input alarm from I/O field (and comparable object which can output operator input alarms) | 1 |
| Log | Flag indicating whether the alarm is to be logged. | 1 |
| Comment | Indicates whether there is a comment for this alarm. A comment is the users input about an alarm, such as "This alarm occurred today because...". | 1 |
| Info text | Indicates whether there is an infotext (tooltip) for this alarm. Tooltips contain information about the alarm, limited to 255 characters, such as "This alarm may occur if ...". Tooltip cannot be edited in Runtime. | 1 |
| Loop-In-Alarm | Indicates whether the "Loop-In-Alarm" function is enabled. | 1 |
| Computer Name | Indicates the name of the PC:  - If the user has entered a comment in the "Historical alarm list (long-term)" and then changed the view, the name of the PC used appears in the "Historical alarm list (short-term)" and "Historical alarm list (long-term)". - If an alarm was acknowledged on a PC, the name of the PC appears in the "Historical alarm lists" (short and long-term) in the operator input alarm. The operator input alarm must be enabled under "Operator input alarm" in the Inspector window for the alarm view. | 10 |
| User Name | Indicates the name of the user (login name):  - If you enter a comment in the "Historical alarm list" (long-term) and then exit the view, your user name is displayed in the "Historical alarm list" (short-term) and "Historical alarm list" (long-term). - If an alarm was acknowledged by a user logged on to WinCC, the user name is displayed in the "Historical alarm lists" (short and long-term) in the operator input alarm. The operator input alarm must be enabled under "Operator input alarm" in the Inspector window for the alarm view. | 10 |
| Priority | Defines the priority of an alarm. You can sort the alarms in the alarm view by priority. With sorting by priority, you can ensure that, in a single-line alarm view, the most important alarm (high priority) is shown in the display range. A lower-priority alarm will not be displayed, even if it is more recent.  Value range: 0 - 16  In WinCC, the value corresponding to the highest priority is not specified. | 3 |

> **Note**
>
> If you enabled the "Change ISO8601 format on all components" option in the shortcut menu of WinCC RT Professional, "Properties &gt; Time settings &gt; Central date and time formatting", the date and time are also displayed in the system blocks of the alarms in ISO8601 format.

#### Possible symbols in the lists in the alarm view

For some system blocks, you can display symbols in the lists in the alarm view. Here is an overview of the meaning of the symbols.

**Symbols in the alarm list in the "Status" and "Acknowledgment status" system blocks:**

| Icon | Meaning |
| --- | --- |
| ![Possible symbols in the lists in the alarm view](images/121528741003_DV_resource.Stream@PNG-de-DE.png) | Alarm has arrived in the "Status" system block. |
| ![Possible symbols in the lists in the alarm view](images/121528749323_DV_resource.Stream@PNG-de-DE.png) | Alarm has arrived in / left the "Status" system block |
| ![Possible symbols in the lists in the alarm view](images/121536924043_DV_resource.Stream@PNG-de-DE.png) | Alarm has arrived in / been acknowledged in the "Status" system block |
| ![Possible symbols in the lists in the alarm view](images/121537009163_DV_resource.Stream@PNG-de-DE.png) | Alarm has been acknowledged in "Acknowledgment status" system block. |

**Symbols in the Historical alarm list (short-term) and Historical alarm list (long-term) in the "Status" system block:**

| Icon | Meaning |
| --- | --- |
| ![Possible symbols in the lists in the alarm view](images/121537017483_DV_resource.Stream@PNG-de-DE.png) | Alarm came in |
| ![Possible symbols in the lists in the alarm view](images/121537742603_DV_resource.Stream@PNG-de-DE.png) | Alarm went out |
| ![Possible symbols in the lists in the alarm view](images/121537981323_DV_resource.Stream@PNG-de-DE.png) | Alarm acknowledged |
| ![Possible symbols in the lists in the alarm view](images/121537989643_DV_resource.Stream@PNG-de-DE.png) | Alarm acknowledged by system |
| ![Possible symbols in the lists in the alarm view](images/121538343563_DV_resource.Stream@PNG-de-DE.png) | Alarm is hidden |
| ![Possible symbols in the lists in the alarm view](images/121538467083_DV_resource.Stream@PNG-de-DE.png) | Hidden alarm came in |
| ![Possible symbols in the lists in the alarm view](images/121538475403_DV_resource.Stream@PNG-de-DE.png) | Hidden alarm went out |
| ![Possible symbols in the lists in the alarm view](images/121538778123_DV_resource.Stream@PNG-de-DE.png) | Hidden alarm acknowledged |
| ![Possible symbols in the lists in the alarm view](images/121538863243_DV_resource.Stream@PNG-de-DE.png) | Alarm is displayed again |
| ![Possible symbols in the lists in the alarm view](images/121538871563_DV_resource.Stream@PNG-de-DE.png) | Emergency acknowledgment of alarm |
| ![Possible symbols in the lists in the alarm view](images/121539187083_DV_resource.Stream@PNG-de-DE.png) | Alarm locked |

**Symbols in the alarm list, Historical alarm list (short-term) and Historical alarm list (long-term) for some system blocks:**

| Icon | Meaning |
| --- | --- |
| ![Possible symbols in the lists in the alarm view](images/121539195403_DV_resource.Stream@PNG-de-DE.png) | Shows whether the property of a system block is activated. |
| ![Possible symbols in the lists in the alarm view](images/121539472523_DV_resource.Stream@PNG-de-DE.png) | Shows whether there is a comment for the alarm in the "Comment" system block. |
| ![Possible symbols in the lists in the alarm view](images/121539596043_DV_resource.Stream@PNG-de-DE.png) | Shows whether there is an info text for the alarm in the "Info text" system block |
| ![Possible symbols in the lists in the alarm view](images/121539604363_DV_resource.Stream@PNG-de-DE.png) | Shows in the system block "Loop-In-Alarm" whether the Loop-In-Alarm is activated |

---

**See also**

[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring the state texts of an alarm class (RT Professional)](#configuring-the-state-texts-of-an-alarm-class-rt-professional)
  
[Configuring an alarm view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-an-alarm-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

### SQL Statements for Filtering the Alarm View (RT Professional)

#### Introduction

In the alarm view, you can only use SQL statements that can be generated using the "Specify selection" dialog. The following conditions apply to WinCC:

- Structure: "Field", "Address", and "Value"

  Separate individual parameters with spaces.

  Example:

  DATETIME &gt;= '2006-12-21 00:00:00.000' AND MSGNR &gt;= 100

  All alarms from 21.12.2006 with an alarm number greater than or equal to 100
- The following information is entered in single quotes:

  - Character strings
  - Date
  - Time of day
- In the DATETIME argument, the date and time of day are separated by a blank. Regardless of the time base setting in the object properties, the output of DATETIME is based on the time base Local Time. The exception to this is when "UTC" is set as the time base. In this case, output is based on the time base "UTC".

#### Permissible Arguments

| Name | SQL name | Type | Data | Example |
| --- | --- | --- | --- | --- |
| Filter | MsgFilterSQL: | Integer | Maximum number of alarms to output | 10000  Up to 10,000 alarms are output. |
| Date/time | DATETIME | Date | 'YYYY-MM-DD hh:mm:ss.msmsms' | DATETIME &gt;= '2007-05-03 16:00:00.000'  Outputs alarms as of 05/03/2007, 16:00 hours. |
| Number | MSGNR | Integer | Alarm number | MSGNR &gt;= 10 AND MSGNR &lt;= 12  Outputs the alarms with alarm numbers 10 to 12. |
| Class | CLASS IN | Integer | Alarm class ID 1-256 and "System" alarm classes 17 + 18 | CLASS IN ( 1 )  Outputs alarms of alarm class 1. |
| Status | STATE | Integer | Value "ALARM_STATE_xx"  Only the operands "=" and "IN(...)" are permitted.  ALARM_STATE_1 ALARM_STATE_2 ALARM_STATE_3 ALARM_STATE_4 ALARM_STATE_10 ALARM_STATE_11 ALARM_STATE_16 ALARM_STATE_17 | STATE IN(1,2,3)  Outputs all alarms that came in, went out and were acknowledged.  Possible values: 1 = incoming alarms 2 = outgoing alarms 3 = acknowledged alarms 4 = blocked alarms 10 = hidden alarms 11 = displayed alarms 16 = alarms acknowledged by the system 17 = Emergency-acknowledged alarms |
| Priority | PRIORITY | Integer | Alarm priority 0 to 16 | PRIORITY &gt;= 1 AND PRIORITY =&lt; 5  Outputs alarms that have a priority between 1 and 5. |
| Controller number | AG_NR | Integer | Controller number | AG_NR &gt;= 2 AND AG_NR &lt;= 2  Outputs alarms with the Controller number 2. |
| CPU number | CPU_NR | Integer | AG sub-number | CPU_NR &gt;= 5 AND CPU_NR &lt;= 5  Outputs alarms with AG sub-number 5. |
| Instance | INSTANCE | Text | Instance | - |
| Block: 1 ... Block: 10 | TEXTxx | Text | Search string for Text1 - Text10 | TEXT2 IN ('Error','Fault')  Outputs the alarms whose Text2 corresponds with the text "Error" or "Fault".  TEXT2 LIKE 'Error'  Outputs the alarms whose Text2 corresponds with "Error".  TEXT2 LIKE '%Error%'  Outputs the alarms whose Text2 includes the text "Error". |
| Process value: 1 ... Process value: 10 | PVALUExx | Double | Search value for PVALUE1-PVALUE10 | PVALUE1 &gt;= 0 AND PVALUE1 &lt;= 50  Outputs process value 1 with start value 0 and stop value 50. |

#### Permissible Operands

- **&gt;= , &lt;= , = , &gt; , &lt;**
- **IN(...)** : Several values as an array, separated by commas, e.g.: CLASS IN( 1 ,2 ,3 ).
- **LIKE** : Text must contain string, e.g.: TEXT1 LIKE 'Error' relays alarm where Text1 contains the search string "Error". The operand LIKE is only allowed for "text" type arguments.

#### Illegal arguments and operands

Only the arguments indicated in the table and operands from the list are permitted.

Grouping arguments, with brackets, for example, is not permitted.

---

**See also**

[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### System events  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on system events (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-system-events-basic-panels-panels-comfort-panels-rt-advanced)
- [9999 - Global alarm (Panels, Comfort Panels, RT Advanced)](#9999---global-alarm-panels-comfort-panels-rt-advanced)
- [10000 - Printer alarms (Panels, Comfort Panels, RT Advanced)](#10000---printer-alarms-panels-comfort-panels-rt-advanced)
- [20000 - Global script alarms (Panels, Comfort Panels, RT Advanced)](#20000---global-script-alarms-panels-comfort-panels-rt-advanced)
- [30000 - Alarms errors when using system functions (Basic Panels, Panels, Comfort Panels, RT Advanced)](#30000---alarms-errors-when-using-system-functions-basic-panels-panels-comfort-panels-rt-advanced)
- [40000 - Linear scaling alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#40000---linear-scaling-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [50000 - Data server alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#50000---data-server-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [60000 - Windows function alarms (Panels, Comfort Panels, RT Advanced)](#60000---windows-function-alarms-panels-comfort-panels-rt-advanced)
- [70000 - Windows function alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#70000---windows-function-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [80000 - Log alarms (Panels, Comfort Panels, RT Advanced)](#80000---log-alarms-panels-comfort-panels-rt-advanced)
- [90000 - FDA alarms (Panels, Comfort Panels, RT Advanced)](#90000---fda-alarms-panels-comfort-panels-rt-advanced)
- [110000 - Offline function alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#110000---offline-function-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [120000 - Trend alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#120000---trend-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [130000 - System information alarms (Panels, Comfort Panels, RT Advanced)](#130000---system-information-alarms-panels-comfort-panels-rt-advanced)
- [140000 - Connection alarms: Connection + device (Basic Panels, Panels, Comfort Panels, RT Advanced)](#140000---connection-alarms-connection-device-basic-panels-panels-comfort-panels-rt-advanced)
- [160000 - Connection alarms: OPC: Connection (Panels, Comfort Panels, RT Advanced)](#160000---connection-alarms-opc-connection-panels-comfort-panels-rt-advanced)
- [170000 - S7 dialog alarms (Panels, Comfort Panels, RT Advanced)](#170000---s7-dialog-alarms-panels-comfort-panels-rt-advanced)
- [180000 - General alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#180000---general-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [190000 - Tag alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#190000---tag-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [190100 - Area pointer alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#190100---area-pointer-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [200000 - PLC coordination alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#200000---plc-coordination-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [200100 - Area pointer alarms project ID (Basic Panels, Panels, Comfort Panels, RT Advanced)](#200100---area-pointer-alarms-project-id-basic-panels-panels-comfort-panels-rt-advanced)
- [210000 - PLC job alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#210000---plc-job-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [220000 - WinCC communication driver alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#220000---wincc-communication-driver-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [230000 - Screen object alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#230000---screen-object-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [240000 - Authorization alarms (Panels, Comfort Panels, RT Advanced)](#240000---authorization-alarms-panels-comfort-panels-rt-advanced)
- [250000 - S7 Status/Force alarms (Panels, Comfort Panels, RT Advanced)](#250000---s7-statusforce-alarms-panels-comfort-panels-rt-advanced)
- [260000 - Password system alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#260000---password-system-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [270000 - System alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#270000---system-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [280000 - Alarms SIMATIC 505 DP Communication Driver (CSP) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#280000---alarms-simatic-505-dp-communication-driver-csp-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [290000 - Recipe system alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](#290000---recipe-system-alarms-basic-panels-panels-comfort-panels-rt-advanced)
- [300000 - Alarm_S alarms (Panels, Comfort Panels, RT Advanced)](#300000---alarm_s-alarms-panels-comfort-panels-rt-advanced)
- [310000 - Reporting alarms (Panels, Comfort Panels, RT Advanced)](#310000---reporting-alarms-panels-comfort-panels-rt-advanced)
- [330000 - Interaction alarms (Panels, Comfort Panels, RT Advanced)](#330000---interaction-alarms-panels-comfort-panels-rt-advanced)
- [340000 - Alarms info text (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#340000---alarms-info-text-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [350000 - PROFIsafe alarms (Panels, Comfort Panels, RT Advanced)](#350000---profisafe-alarms-panels-comfort-panels-rt-advanced)
- [380000 - Alarms Sm@rtServer (Panels, Comfort Panels, RT Advanced, RT Professional)](#380000---alarms-smrtserver-panels-comfort-panels-rt-advanced-rt-professional)
- [390000 alarm password encryption and certificates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#390000-alarm-password-encryption-and-certificates-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [1000000 - WinCC communication driver alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#1000000---wincc-communication-driver-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics on system events (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### System events

System events on the HMI device provide information about internal states of the HMI device and PLC.

The following overview illustrates when a system event occurs and how to eliminate the cause of error.

> **Note**
>
> **HMI device dependency**
>
> Some of the system events described in this section apply to the individual HMI devices based on their scope of functions.

> **Note**
>
> System events are output in an alarm view. System events are output in the language currently set on your HMI device.
>
> The time format (AM/PM or 24-hour format) is based on the selected language. If there is no translation of the alarm texts in this language, English or Russian is selected as a replacement language and displays the appropriate time format.

##### System event parameters

System events may contain encrypted parameters. The parameters are of relevance when troubleshooting because they provide a reference to the source code of the Runtime software. These parameters are output after the "Error code:"

---

**See also**

[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### 9999 - Global alarm (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system event

The most important system events are listed below.

9999 - Global alarm

| Number | Effect/cause | Remedy |
| --- | --- | --- |
| 9999 | The system start was interrupted.   Check the following:   - Line voltage - Cable connections - System settings - Configurations - Conversions | Check the power supply and cable connections.  Check the system settings.  Check the configurations and conversions.   If the error occurs repeatedly, contact the hotline! |

#### 10000 - Printer alarms (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

10000 - Printer alarms

| Number | Effect/cause | Solution |
| --- | --- | --- |
| 10000 | The print job could not be started or was canceled due to an unknown error. Faulty printer setup. Or: No authorization is available for accessing the network printer. The power supply was interrupted during data transfer. | Check the printer settings, cable connections and the power supply. Set up the printer once again. Obtain a network printer authorization. If the error persists, contact the hotline! |
| 10001 | No printer is installed or a default printer has not been set up. | Install a printer and/or select it as the default printer. |
| 10002 | The buffer for printing graphics is full. Up to two graphics are buffered. | Allow more time between print jobs. |
| 10003 | Graphics can now be buffered again. | -- |
| 10004 | The buffer for printing lines in text mode (e.g. alarms) is full. Up to 1000 lines are buffered. | Allow more time between print jobs. |
| 10005 | Text lines can now be buffered again. | -- |
| 10006 | The Windows printing system reports an error. Refer to the output text and the error ID to determine the possible causes. Nothing is printed or the printing is incorrect. | If necessary, repeat the action. |

#### 20000 - Global script alarms (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below. The system events are divided into different ranges.

20000 - Global script alarms

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 20010 | An error has occurred in the specified script line. Execution of the script was therefore aborted. Note the system event that might have occurred prior to this. | Select the specified script line in the configuration. Ensure that the tags used are of the allowed types. For system functions, verify the correct number of parameters and the parameter types. |
| 20011 | An error has occurred in a script that was called by the specified script.  Execution of the script was therefore aborted in the called script.  Note the system event that might have occurred prior to this. | In the configuration, select the script that has been called directly or indirectly by the specified script.  Ensure that the tags used are of the allowed types.  For system functions, verify the correct number of parameters and the parameter types. |
| 20012 | Inconsistent configuration data. The script could therefore not be generated. | Recompile the configuration data. |
| 20013 | The script component of WinCC Runtime was not initialized during the start. | Recompile your project using the "Compile &gt; Software (rebuild all)" command from the context-sensitive menu and then download the project to the HMI device. |
| 20014 | The system function returns a value that is not written in any return tag. | Select the specified script in the configuration. Check whether the script name has been assigned a value. |
| 20015 | Too many successive scripts have been triggered in short intervals. When more than 20 scripts are queued for processing, any subsequent scripts are rejected. In this case, the script indicated in the alarm is not executed. | Check what is triggering the scripts. Extend the times, e.g. the acquisition cycle of the tag initiating the script. |

#### 30000 - Alarms errors when using system functions (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below. The system events are divided into different ranges.

30000 - Alarms errors when using system functions

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 30010 | The tag could not accept the function result, e.g. when it has exceeded the value range. | Check the tag types of the system function parameters. |
| 30011 | A system function could not be executed because the function was assigned an invalid value or type in the parameter. | Check the parameter value and tag type of the invalid parameter. If a tag is used as a parameter, check its value. |
| 30012 | A system function could not be executed because the function was assigned an invalid value or type in the parameter. | Check the parameter value and tag type of the invalid parameter. If a tag is used as a parameter, check its value. |

#### 40000 - Linear scaling alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below. The system events are divided into different ranges.

40000 - Linear scaling alarms

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 40010 | The system function could not be executed since the parameters could not be converted to a common tag type. | Check the parameter types in the configuration. |
| 40011 | The system function could not be executed since the parameters could not be converted to a common tag type. | Check the parameter types in the configuration. |

#### 50000 - Data server alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below. The system events are divided into different ranges.

50000 - Data server alarms

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 50000 | The HMI device is receiving data faster than it is capable of processing. Therefore, no further data is accepted until all current data have been processed. Data exchange then resumes. | -- |
| 50001 | Data exchange has been resumed. | -- |

#### 60000 - Windows function alarms (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

60000 - Win32 function alarms

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 60000 | This alarm is generated by the "ShowSystemEvent" system function. The text to be displayed is transferred to the function as a parameter. | -- |
| 60010 | The file could not be copied in the direction defined because one of the two files is currently open or the source/target path is not available. It is possible that the Windows user has no access rights to one of the two files. | Restart the system function or check the paths of the source/target files. Under Windows: Users executing WinCC Runtime must be granted access to the files. |
| 60011 | An attempt was made to copy a file to itself. It is possible that the Windows user has no access rights to one of the two files. | Check the path of the source/target file. In Windows with NTFS: Users executing WinCC Runtime must be granted access to the files. |

#### 70000 - Windows function alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

70000 - Win32 function alarms

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 70010 | The application could not be started because it could not be found in the path specified or there is insufficient memory space. | Check whether the application exists in the specified path or close other applications. |
| 70011 | The system time could not be modified. The error message only appears in connection with area pointer "Date/time PLC". Possible causes:  - An invalid time was transferred in the job mailbox. - The Windows user has no right to modify the system time.   If the first parameter in the system event is displayed with the value 13, the second parameter indicates the byte containing the incorrect value. | Check the time that is to be set. Under Windows: Users running WinCC Runtime must be granted the right to set the system time of the operating system. |
| 70012 | Error when executing the system function "StopRuntime" with the "Runtime and operating system" option. Windows and WinCC Runtime are not closed.  The error may have been generated because other programs cannot be closed. | Close all programs currently running. Now close Windows. |
| 70013 | The system time could not be modified because an invalid value was entered. An incorrect delimiter may have been used. | Check the time which is to be set. |
| 70014 | The system time could not be modified. Possible causes:  - An invalid time was transferred. - The Windows user has no right to modify the system time.   Windows rejects the setting request. | Check the time that is to be set. Under Windows: Users running WinCC Runtime must be granted the right to set the system time of the operating system. |
| 70015 | The system time could not be read because Windows rejects the reading function. | -- |
| 70016 | An attempt was made to select a screen by means of a system function or job. This is not possible because the configured screen number does not exist. Or: A screen could not be generated due to insufficient system memory.  Or: The screen is blocked.  Or: Screen call has not been executed correctly. | Check the screen number in the system function or job against the screen numbers configured. Assign the number to a screen if necessary.  Check the details for the screen call and whether the screen is blocked for specific users. |
| 70017 | Date/time is not read from the area pointer because the address set in the PLC is either not available or has not been set up. | Change the address or set up the address in the PLC. |
| 70018 | Acknowledgment that the password list has been successfully imported. | -- |
| 70019 | Acknowledgment that the password list has been successfully exported. | -- |
| 70020 | Acknowledgment for activation of alarm reporting. | -- |
| 70021 | Acknowledgment for deactivation of alarm reporting. | -- |
| 70022 | Acknowledgment to start the action for importing the password list. | -- |
| 70023 | Acknowledgment to start the action for exporting the password list. | -- |
| 70024 | The tag value range was exceeded during system function execution. No calculation of the system function. | Check and correct the calculation. |
| 70025 | The tag value range was exceeded during system function execution. No calculation of the system function. | Check and correct the calculation. |
| 70026 | No other screens are stored in the internal screen memory. No other screens can be selected. | -- |
| 70027 | The backup of the RAM file system has been started. | -- |
| 70028 | RAM file system backup is complete. The files from the RAM have been copied to the Flash memory. Following a restart, these saved files are copied back to the RAM file system. | -- |
| 70029 | Backup of the RAM file system has failed. No backup copy of the RAM file system has been made. | Check the settings in the "Control Panel &gt; OP" dialog and save the RAM file system using the "Save Files" button in the "Persistent Storage" tab. |
| 70030 | The parameters configured for the system function are faulty. The connection to the new PLC was not established. | Compare the parameters configured for the system function with the parameters configured for the PLCs and correct them as necessary. |
| 70031 | The PLC configured in the system function is not an S7 PLC. The connection to the new PLC has not been established. | Compare the S7 PLC name parameter configured for the system function with the parameters configured for the PLC and correct them as necessary. |
| 70032 | The object configured with this number in the tab sequence is not available in the selected screen. The screen changes but the focus is set to the first object. | Check the number of the tab sequence and correct it if necessary. |
| 70033 | An e-mail could not be sent because a TCP/IP connection to the SMTP server no longer exists. This system event is only generated at the first failed attempt. All subsequent unsuccessful attempts to send an e-mail will no longer generate a system event. The event is only generated again if an e-mail has been successfully sent in the meantime. The central e-mail component in WinCC Runtime attempts to connect to the SMTP server at regular intervals (1 minute) in order to transmit the remaining e-mails. | Check the network connection to the SMTP server and re-establish it if necessary. |
| 70034 | Following a disruption, the TCP/IP connection to the SMTP server was successfully re-established. The queued e-mails are then sent. | -- |
| 70036 | No SMTP server for sending e-mails is configured. An attempt to connect to an SMTP server therefore fails and it is not possible to send e-mails.   WinCC Runtime generates the system event at the first attempt to send an e-mail. | Configure an SMTP server:  In the WinCC Engineering System using "Device settings &gt; Device settings"  In the Windows CE operating system using "Control Panel &gt; Internet Settings &gt; E-mail &gt; SMTP Server" |
| 70037 | An e-mail could not be sent for unknown reasons. The contents of the e-mail are discarded. | Check the e-mail parameters (recipient etc.). |
| 70038 | The SMTP server has rejected the sending or forwarding of an e-mail because the domain of the recipient is unknown to the server or because the SMTP server requires authentication. The contents of the e-mail are discarded. | Check the domain of the recipient address or disable the authentication on the SMTP server if possible. SMTP authentication is currently not used in WinCC Runtime. |
| 70039 | The syntax of the e-mail address is incorrect or contains invalid characters. The contents of the e-mail are discarded. | Check the e-mail address of the recipient. |
| 70040 | The syntax of the e-mail address is incorrect or contains illegal characters. | -- |
| 70041 | The import of the user management has been aborted due to an error. Nothing has been imported. | Check your user administration or download it again to the panel. |
| 70042 | The range of values of the tag was exceeded while executing the system function.  The system function was not calculated. | Check and correct the calculation. |
| 70043 | The range of values of the tag was exceeded while executing the system function.  The system function was not calculated. | Check and correct the calculation. |
| 70044 | An error occurred while sending the e-mails. The e-mails were not sent. | Check the SMTP settings and the error message in the system event. |
| 70045 | Cannot load a file required for encrypting the e-mail. | Update the operating system and Runtime. |
| 70046 | The server does not support encryption. | Select an SMTP server that supports encryption. |
| 70047 | The SSL versions of the HMI device and SMTP server may not be compatible. | Contact your network administrator or the operator of the SMTP server. |

#### 80000 - Log alarms (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

80000 - Log alarms

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 80001 | The log specified is filled to the size defined (in percent) and must be stored elsewhere. | You swap out the file or table by executing a ‘move’ or ‘copy’ function. |
| 80002 | A line is missing in the specified log. | -- |
| 80003 | The copying process for logging was not successful. In this case, it is advisable to check any subsequent system events, too. | -- |
| 80006 | Since logging is not possible, this causes a permanent loss of the functionality. | In the case of databases, check whether the corresponding data source exists and start up the system again. |
| 80009 | A copying action has been completed successfully. | -- |
| 80010 | An incorrect storage location was entered in WinCC and causes permanent loss of functionality. | Configure the storage location for the respective log again and restart the system when the full functionality is required. |
| 80012 | Log entries are stored in a buffer. If the values are read to the buffer faster than they can be physically written (using a hard disk, for example), overloading may occur and recording is then stopped. | Archive fewer values. Or: Increase the logging cycle. |
| 80013 | The overload status no longer exists. Archiving resumes the recording of all values. | -- |
| 80014 | The same action was triggered twice in quick succession. Since the process is already in operation, the action is only carried out once. | -- |
| 80015 | This system event is used to report DOS or database errors to the user. | -- |
| 80016 | The logs are separated by system function "CloseAllLogs" and the incoming entries exceed the defined buffer size. All buffer entries are deleted. | Reconnect the logs. |
| 80017 | The number of incoming entries cause a buffer overflow. This can be caused, for example, by several copying actions being activated at the same time. All copy jobs in the buffer are deleted. | Stop the copy action. |
| 80019 | The connection between WinCC and all log files was shut down, for example, after execution of the "CloseAllLogs" system function. Entries are written to the buffer and written to the logs when the connection is recovered.   There is no connection to the storage location and the storage medium can be changed. | -- |
| 80020 | The maximum number of simultaneously copy operations has been exceeded. Copying is not executed. | Wait until the current copying actions have been completed, then restart the last copy action. |
| 80021 | An attempt was made to delete a log which is still busy with a copy action. Deletion has not been executed. | Wait until the current copying actions have been completed, then restart the last action. |
| 80022 | An attempt was made to use system function "StartSequenceLog" to start a sequence log for a log which is not configured as sequence log. No sequence log file is created. | In the project, check  - whether the "StartSequenceLog" system function was properly configured. - if the tag parameters are properly provided with data on the HMI device. |
| 80023 | An attempt was made to copy a log to itself. The log is not copied. | In the project, check  - whether the "CopyLog" system function was properly configured. - if the tag parameters are properly provided with data on the HMI device. |
| 80024 | In your configuration, you specified that the "CopyLog" system function should not allow copying if the destination log already contains data ("Mode" parameter). The log is not copied. | Edit the "CopyLog" system function in your configuration, if necessary. Before you initiate the system function, delete the destination log file. |
| 80025 | You have canceled the copy operation. Data written up to this point are retained. The target log file (if configured) was not deleted. The cancellation is reported by an error entry $RT_ERR$ at the end of the target log. | -- |
| 80026 | This alarm is output after all logs are initialized. Values are written to the logs from then on. No entries are written to the logs before this time has expired, irrespective of the active state of WinCC Runtime. | -- |
| 80027 | The internal Flash memory has been specified as the storage location for a log. This is not permissible. No values are written to this log and the log file is not created. | Configure "Storage Card" or network path as the storage location. |
| 80028 | The alarm serves as status report indicating that the logs are currently being initialized. No values are logged until the alarm 80026 is output. | -- |
| 80029 | The number of logs specified in the alarm could not be initialized. Initialization of logs was finished.  The faulty log files are not available for logging jobs. | Evaluate the additional system events related to this alarm. Check the configuration, the ODBC (Open Database Connectivity), and the specified drive. |
| 80030 | The structure of the existing log file does not match the expected structure. Logging is stopped for this log. | Delete the existing log data manually, in advance. |
| 80031 | The log in CSV format is corrupted. The log cannot be used. | Delete the faulty file. |
| 80032 | Logs can be configured with events. These are triggered as soon as the log is full. Assuming WinCC Runtime is started and the log is already full, the event would never be triggered. The specified log is full and no longer accepts data. | Close WinCC Runtime, delete the log, and restart WinCC Runtime. Or: Configure a button which contains the same actions as the event and press it. |
| 80033 | "System Defined" is set in the data log file as the data source name. This causes an error. No data is written to the database logs, whereas the logging to the CSV logs works. | Reinstall SQL Sever 2005 Express. |
| 80034 | An error has occurred in the initialization of the logs. An attempt has been made to create the tables as a backup. This action was successful. A backup copy of the tables of the corrupted log file was generated and the cleared log restarted. | No action is necessary. However, it is recommended to save the backup files or delete them in order to make the space available again. |
| 80035 | An error has occurred in the initialization of the logs. An attempt has been made to create backups of the tables and this has failed. No logging or backup has been performed. | It is recommended to save the backups or to delete them in order to release memory. |
| 80039 | The alarm comes from the audit. The alarm is output after the next archive was started with system function "Start next archive". | -- |
| 80040 | The alarm comes from the audit. The alarm is output after the next archive was stopped with system function "Stop next archive". | -- |
| 80041 | The alarm comes from the audit. The alarm is output after the next archive was changed to with system function "Change to next archive". | -- |
| 80044 | The export of a log was interrupted because Runtime was closed or due to a power failure. At the restart of Runtime, it was detected that the export must be resumed. | The export resumes automatically. |
| 80045 | The export of a log was interrupted due to an error in the connection to the server or at the server itself. | The export is repeated automatically. Check:  - The connection to the server. - If the server is running. - If there is enough free space on the server. |
| 80046 | The destination file or the associated directory could not be created on the server. | Check whether there is enough space on the server and you have authorization to store the log file. |
| 80047 | The log could not be read while exporting it. | Check whether the storage medium is correctly inserted. |
| 80049 | The log could not be renamed while preparing to export it.  The job can not be completed." | Check whether the storage medium is correctly inserted and if there is sufficient space on the medium. |
| 80050 | The log which shall be exported is not closed.  The job can not be completed. | Make sure to call the "CloseAllLogs" system function before using the "ExportLog" system function. Change the configuration as required. |
| 80051 | The log to be copied contains an invalid checksum. The log was not copied. | Select a log with a valid checksum. The selected log may have been manipulated. |
| 80052 | The log cannot be read. | Check the log and the specified path. |
| 80053 | The closed log cannot be read. | Open the log. |
| 80054 | The storage medium is not available | Check whether the storage medium is correctly inserted. |

#### 90000 - FDA alarms (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

90000 - FDA alarms

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 90024 | No operator actions can be logged due to lack of space on the storage medium for log. The operator action will therefore not be executed. | Provide more storage space by inserting a blank storage medium, or backup the log files to the server using the "ExportLog" function. |
| 90025 | No user actions can be logged because of error state of the archive. Therefore the user action will not be executed. | Check whether the storage medium is correctly inserted. |
| 90026 | No operator actions can be logged because the log is closed. The operator action will therefore not be executed. | Before further operator actions are carried out, the log must be reopened with the help of system function "OpenAllLogs". Change the configuration as required. |
| 90028 | The password you entered is incorrect. | Enter the correct password. |
| 90029 | Runtime was closed during ongoing operation (perhaps due to a power failure) or a storage medium in use is incompatible with Audit Trail. An Audit Trail is not suitable if it belongs to another project or has already been logged.  It could also be that archiving was not stopped before automatic execution of the "CloseAllArchives" function was started (e.g. by the task scheduler). | Ensure that you are using the correct storage medium. |
| 90030 | Runtime was closed during ongoing operation (perhaps due to a power failure). | -- |
| 90031 | Runtime was closed during ongoing operation (perhaps due to a power failure). | -- |
| 90032 | Running out of space on the storage medium for log. | Provide more storage space by inserting a blank storage medium, or backup the log files to the server using the "ExportLog" function. |
| 90033 | No more space on the storage medium for log. As of now, no more operator actions requiring logging will be executed. | Provide more storage space by inserting a blank storage medium, or backup the log files to the server using the "ExportLog" function. |
| 90036 | Application is stopped due to power supply error. | -- |
| 90039 | You do not have the necessary authorization to perform this action. | Adapt or upgrade your authorizations. |
| 90040 | Audit Trail is switched off because of a forced user action. | Reactivate the "Audit Trail" with the help of system function "StartLog". |
| 90041 | A user action which has to be logged has been executed without a logged on user. | A user action requiring logging should only be possible with permission. Change the configuration by setting a required authorization for the input object. |
| 90044 | A user action which has to be confirmed was blocked, because there is another user action pending. | Repeat the user action if necessary. |
| 90048 | The Audit Trail cannot be printed while data relevant to the audit is being logged. | Stop logging by calling system function "StopLogging". |
| 90049 | Access to required file is not possible. | Check the network connection or the storage medium. |
| 90056 | The recipe was not imported because the file contains no checksum. | Select a file with a checksum.  You can also disable checksum verification by calling system function "ImportDataRecords". |
| 90057 | The recipe was not imported because the file contains an invalid checksum. The selected file may have been manipulated. | Select a file with a valid checksum. |

#### 110000 - Offline function alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

110000 - Offline function alarms

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 110000 | The operating mode was changed. "Offline" mode is now set. | -- |
| 110001 | The operating mode was changed. "Online" mode is now set. | -- |
| 110002 | The operating mode was not changed. | Check the connection to the PLCs. Check whether the address range for the “Coordination" area pointer is present in the PLC. |
| 110003 | The operating mode of the specified PLC was changed by the "SetConnectionMode" system function.  The "offline" operating mode is now set. | -- |
| 110004 | The operating mode of the specified PLC was changed by the "SetConnectionMode" system function.  The "online" operating mode is now set. | -- |
| 110005 | An attempt was made to use the "SetConnectionMode" system function to set the specified PLC to "online" mode, although the entire system is in "offline" mode. This changeover is not allowed. The PLC remains in "offline" mode. | Switch the complete system to "online" mode and repeat execution of the system function. |
| 110006 | The content of the "project ID" area pointer does not match the project ID configured in WinCC. The WinCC Runtime is therefore terminated. | Check:  - the project ID entered on the PLC. - the project ID entered in WinCC. |

#### 120000 - Trend alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

120000 - Trend alarms

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 120000 | The trend is not displayed because you configured an incorrect axis to the trend or an incorrect trend. | Change the configuration. |
| 120001 | The trend is not displayed because you configured an incorrect axis to the trend or an incorrect trend. | Change the configuration. |
| 120002 | The trend is not displayed because the tag assigned attempts to access an invalid PLC address. | Check whether the data area for the tag is available on the PLC, whether the configured address is correct, or whether the value range for the tag is correct. |

#### 130000 - System information alarms (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

130000 - System information alarms

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 130000 | The action was not executed. | Close all other programs.  Delete files no longer required from the hard disk. |
| 130001 | The action was not executed. | Delete files no longer required from the hard disk. |
| 130002 | The action was not executed. | Close all other programs.  Delete files no longer required from the hard disk. |
| 130003 | No data medium found. The operation is canceled. | Check the following conditions, for example:  - Access to the correct data carrier? - Is a data carrier inserted? |
| 130004 | The data carrier is write-protected. The operation is canceled. | Check whether the correct data medium is being accessed. Remove the write-protection if necessary. |
| 130005 | The file is read only. The operation is canceled. | Check whether the correct file is being accessed. Change the file attributes. |
| 130006 | No access to the file. The operation is canceled. | Check the following conditions, for example:  - Is the correct file being accessed? - Does the file exist? - Is another action preventing concurrent access to the file? |
| 130007 | The network connection is interrupted.  Records cannot be saved or read via the network connection. | Check the network connection and eliminate the cause of error. |
| 130008 | No storage card available.  The specified records cannot be saved to or read from Storage Card. | Insert the storage card. |
| 130009 | The specified folder does not exist on the storage card.  The files stored in this directory are not backed up after switching off the HMI device. | Insert the storage card. |
| 130010 | The maximum nesting depth can be exhausted when, for example, value changes in a script initiate the call of an infinite number of further scripts.   The configured functionality is not provided. | Check the configuration. |
| 130013 | No storage card available.  The specified records cannot be saved to or read from Storage Card. | Insert the storage card. |

#### 140000 - Connection alarms: Connection + device (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

140000 - Connection alarms: Connection + device

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 140000 | An online connection to the PLC is established. | -- |
| 140001 | The online connection to the PLC was shut down. | -- |
| 140003 | No tag update or write operations are executed. | Check whether the connection is up and the PLC is switched on. In the Control Panel, check the set parameters using the "Set PG/PC interface" function. Restart the system. |
| 140004 | No tag update or write operations are executed due to an incorrect access point, or incorrect module configuration. | Check the connection and whether the PLC is switched on. Check the access point or the module configuration (MPI, PPI, PROFIBUS) in the Control Panel with "Set PG/PC interface". Restart the system. |
| 140005 | No tag update or write operations are executed due to an incorrect HMI device address (possibly too high). | Use a different address for the HMI device. Check the connection and whether the PLC is switched on. Check the parameters set in the "Set PG/PC interface" dialog of the Control Panel. Restart the system. |
| 140006 | No tag update or write operations are executed due to an incorrect baud rate setting. | Select a different baud rate in WinCC (according to module, profile, communication peer, etc.). |
| 140007 | An incorrect bus profile prevents tag updates or write operations (see %1). The following parameters cannot be written to the registry database: 1:  Tslot 2:  Tqui 3:  Tset 4:  MinTsdr 5:  MaxTsdr 6:  Trdy 7:  Tid1 8:  Tid2 9:  Gap factor 10: Retry limit | Check the custom bus profile. Check the connection and whether the PLC is switched on. Check the parameters set in the "Set PG/PC interface" dialog of the Control Panel. Restart the system. |
| 140008 | An incorrect baud rate prevents tag updates or write operations. The following parameters cannot be entered in the registry database. 0:  general error 1:  incorrect version 2:  Profile cannot be entered in the registry database. 3:  Subnet type cannot be entered in the registry database. 4:  Target rotation time cannot be entered in the registry database. 5:  Highest address (HSA) is incorrect. | Check whether the connection is up and the PLC is switched on. In the Control Panel, check the set parameters using the "Set PG/PC interface" function. Restart the system. |
| 140009 | No tag updates or write operations because the S7 communication module was not found. | To reinstall the module, open the Control Panel and select "Set PG/PC interface". |
| 140010 | No S7 communication partner found because the PLC is shut down. DP/T: The option "PG/PC is the only master" is not set in the Control Panel under "Set PG/PC interface". | Switch on the PLC. DP/T: If only one master is connected to the network, disable "PG/PC is the only master" in "Set PG/PC interface". If several masters are connected to the network, enable these. Do not change any settings, for this will cause bus errors. |
| 140011 | No tag updates or write operations because communication is down. | Check the connection and whether the communication partner is switched on. |
| 140012 | Initialization error (e.g. if WinCC Runtime was closed in Task Manager). Or: Another application (e.g. STEP 7) with different bus parameters is active and the driver cannot be started with the new bus parameters (baud rate, for example). | Restart the HMI device. Or: Start WinCC Runtime and then start your other applications. |
| 140013 | The MPI cable is disconnected and, therefore, there is no power supply. | Check the connections. |
| 140014 | The configured bus address is in use by another application. | Change the HMI device address in the PLC configuration. |
| 140015 | Incorrect baud rate Or:  Incorrect bus parameters (e.g. HSA) Or: OP address &gt; HSA or: Incorrect interrupt vector (interrupt not registered by the driver) | Correct the parameters. |
| 140016 | The hardware does not support the configured interrupt. | Change the interrupt number. |
| 140017 | The set interrupt is in use by another driver. | Change the interrupt number. |
| 140018 | SIMOTION Scout disabled the consistency check. Only a corresponding note appears. | In SIMOTION Scout, reactivate the consistency check and once again download the project to the PLC. |
| 140019 | SIMOTION Scout is downloading a new project to the PLC. Connection to the PLC is canceled. | Wait until the end of the reconfiguration. |
| 140020 | Mismatch of the PLC and project (FWX file) versions. The connection to the PLC is canceled. | The following remedies are available:  Download the current version to the PLC using SIMOTION Scout.  Recompile the project using WinCC ES, close WinCC Runtime, and restart with the new configuration. |
| 140021 | Setup of the connection to the PLC failed. Incorrect configuration of the "Access password" for the connection to the PLC. | Select the "Access password" area in the "Connections" editor to check the password entered for the connection to the PLC.  Assign the correct password.  The "Password" for the connection to the PLC is assigned in the "Security" area of the PLC properties. |
| 140022 | Setup of the connection to the PLC failed.   Incorrect configuration of the access password for the connection to the PLC. | Select the "Access password" area in the "Connections" editor to check the password entered for the connection to the PLC.   The "Password" for the connection to the PLC is assigned in the "Security" area of the PLC properties. |
| 140023 | Error during time synchronization: Unable to read system time of PLC %1. | Check whether the PLC is switched on.   Select the "Access password" area in the "Connections" editor to check the password entered for the connection to the PLC. |
| 140025 | Setup of the connection to the PLC failed.   The access password of the PLC is disabled in the PLC display. | Enable the access password in the PLC display. |

#### 160000 - Connection alarms: OPC: Connection (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

160000 - Connection alarms: OPC: Connection

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 160000 | No more data is read or written. Possible causes:  - The cable connection is interrupted. - The PLC does not respond or has failed, etc. - The wrong port is used for the connection. - System overload | Check whether the cable is plugged in and the PLC is OK, and whether the correct port is used.  Restart the system if the system event persists. |
| 160001 | The connection is recovered because the cause of the interruption has been eliminated. | -- |
| 160010 | No connection to the server because the server ID (CLS-ID) cannot be determined.  Values cannot be read or written. | Check access rights. |
| 160011 | No connection to the server because the server ID (CLS-ID) cannot be determined.  Values cannot be read or written. | Check the following conditions, for example:  - Correct server name? - Correct station name? - Is the server registered? |
| 160012 | No connection to the server because the server ID (CLS-ID) cannot be determined.  Values cannot be read or written. | Check the following conditions, for example:  - Correct server name? - Correct station name? - Is the server registered?   Note for advanced users:  Interpret the value from HRESULT. |
| 160013 | The specified server was started as InProc server. This has not been released and may lead to undefined behavior because the server is running in the same process area as WinCC Runtime. | Configure the server as OutProc Server or Local Server. |
| 160014 | Only one OPC server project can be started on a PC. An alarm is output after an attempt was made to start a second project.  The second project has no OPC server functionality and cannot be located as an OPC server by external sources. | Do not start a second project with OPC server functionality on the computer. |

#### 170000 - S7 dialog alarms (Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

170000 - S7 dialog alarms

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 170000 | S7 diagnostics events are not displayed because it is not possible to log on to the S7 diagnostics at this device. The service is not supported. | -- |
| 170001 | The S7 diagnostics buffer cannot be viewed because communication with the PLC is shut down. | Set the PLC to online mode. |
| 170002 | The S7 diagnostics buffer cannot be viewed because reading of the diagnostics buffer (SSL) was canceled with an error. | -- |
| 170003 | An S7 diagnostic alarm cannot be visualized. The system returns internal error %2. | -- |
| 170004 | An S7 diagnostic alarm cannot be visualized. The system returns an internal error of error class %2, error number %3. | -- |
| 170007 | It is not possible to read the S7 diagnostics buffer (SSL) because this operation was canceled with an internal error of class %2 and error code %3. | -- |

#### 180000 - General alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

180000 - General alarms

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 180000 | A component/OCX received configuration data with a version ID which is not supported. | Install a newer component. |
| 180001 | System overload because too many actions are running in parallel. Certain actions can be executed, while others are discarded. | Several remedies are available:  - Generate alarms at a slower rate (polling). - Initiate scripts and functions at greater intervals.   If the alarm appears more frequently: Restart the HMI device. |
| 180002 | The screen keyboard could not be activated. Possible causes:  "TouchInputPC.exe" was not registered due to faulty Setup. | Reinstall WinCC Runtime. |

> **Note**
>
> **Alarms without additional information**
>
> Alarm 180003 is not described since the alarm text contains all the necessary information.

#### 190000 - Tag alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Meaning of the system events

The most important system events are listed below.

190000 - Tag alarms

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 190000 | It is possible that the tag is not updated. | -- |
| 190001 | The tag is updated after the cause of the last error state has been eliminated (recovery of normal operation). | -- |
| 190002 | The tag is not updated because communication with the PLC is down. | Select system function "SetOnline" to enable communication. |
| 190004 | The tag is not updated because the address configured for this tag does not exist. | Check the configuration. |
| 190005 | The tag is not updated because the configured PLC type does not exist for this tag. | Check the configuration. |
| 190006 | The tag is not updated because it is not possible to map the PLC type in the data type of the tag. | Check the configuration. |
| 190007 | The tag value is not modified because the connection to the PLC is interrupted or the tag is offline. | Set online mode or reconnect to the PLC. |
| 190008 | The configured tag limits were violated due to one of the following events:  - Value input - System function - Script | Observe the configured or current tag limits. |
| 190009 | An attempt was made to assign this tag a value that is outside the valid range of values for this data type.  For example, input of the value 260 for a byte tag, or input of the value -3 for an unsigned word tag. | Observe the range of values for the data type of the tags. |
| 190010 | The rate at which values are written to the tag is too high (e.g. initiated in a script loop). Values will be lost because buffer capacity is limited to 100 operations. | The following remedies are available:  - Extend the interval between multiple write actions. - Do not use an array tag longer than 6 words when configuring an acknowledgment on the HMI device using "HMI acknowledgment tag". |
| 190011 | Possible cause 1:  The value entered could not be written to the configured PLC tag because the high or low limit was exceeded.  The system discarded the entry and restored the original value.  Possible cause 2:  The connection to the PLC was interrupted. | Note that the value entered must be within the range of values of the control tag.          Check the connection to the PLC. |
| 190012 | It is not possible to convert a value from a source format to a target format, for example:  An attempt is being made to write a counter value that is outside the valid, PLC-specific range of values.  A tag of the type Integer should be assigned a value of the type string. | Check the range of values, or the data type of the tag. |
| 190013 | You entered a string that exceeds the tag length. The string is truncated automatically to a valid length. | Always enter strings that do not exceed the valid tag length. |

#### 190100 - Area pointer alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 190100 - Area pointer alarms

The most important system events are listed below.

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 190100 | The area pointer is not updated because the address configured for this pointer does not exist. Type 1  Warnings 2  Errors 3  PLC acknowledgment 4  HMI device acknowledgment 5  LED image 6  Trend request 7  Trend transfer 1 8  Trend transfer 2 No.: Consecutive number displayed in WinCC ES. | Check the configuration. |
| 190101 | The area pointer is not updated because it is not possible to map the PLC type to the area pointer type. Parameter type and no.: see alarm 190100 | -- |
| 190102 | The area pointer is updated after the cause of the last error state has been eliminated (recovery of normal operation). Parameter type and no.: See alarm 190100. | -- |

#### 200000 - PLC coordination alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 200000 - PLC coordination alarms

The most important system events are listed below.

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 200000 | Coordination is not executed because the address configured in the PLC does not exist/is not set. | Change the address or set up the address in the PLC. |
| 200001 | Coordination is canceled because the write access to the address configured in the PLC is not possible. | Change the address or set the address in the PLC at an area which allows write access. |
| 200002 | Coordination is not carried out at the moment because the address format of the area pointer does not match the internal storage format. | Internal error |
| 200003 | Coordination can be executed again because the last error state is eliminated (return to normal operation). | -- |
| 200004 | The coordination may not be executed. | -- |
| 200005 | No more data is read or written. Possible causes:  - The cable connection is interrupted. - The PLC does not respond or has failed, etc. - System overload | Ensure that the cable is plugged in and the PLC is operational. Restart the system if the system event persists. |

#### 200100 - Area pointer alarms project ID (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 200100 - Area pointer alarms project ID

The most important system events are listed below.

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 200101 | The project ID of the area pointer cannot be described.   No entry possible. | Check the configuration. |
| 200102 | Error in the type conversion. | Check the type conversion. |
| 200103 | The project ID of the area pointer is updated as the cause of the last error state has been eliminated (recovery of normal operation). | -- |
| 200104 | Unknown error | Check the   - Configuration - HMI tags - HMI alarms - System alarms - Controller alarms   If the error occurs repeatedly, contact the hotline! |
| 200105 | The online connection to the PLC was interrupted.   The connection is interrupted. | Check the following conditions, for example   - Are the access correct? - Correct server name? - Correct station name? - Is the server registered? - Is the configuration correct? |

#### 210000 - PLC job alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 210000 - PLC job alarms

The most important system events are listed below.

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 210000 | Jobs are not processed because the configured address does not exist/has not been set up in the PLC. | Change the address or set up the address in the PLC. |
| 210001 | Jobs are not processed because read/write access to the configured address is not possible in the PLC. | Change the address, or set up the address in a PLC area at which read/write access is possible. |
| 210002 | Jobs are not executed because the address format of the area pointer does not match the internal storage format. | Internal error |
| 210003 | The job buffer is processed again because the last error status has been eliminated (recovery of normal operation). | -- |
| 210004 | The job buffer is possibly not going to be processed. | -- |
| 210005 | A job mailbox with invalid number was initiated. | Check the PLC program. |
| 210006 | An error occurred while executing the job mailbox. As a result, the control job is not executed. Observe the next/previous system event. | Check the parameters of the control job. Recompile the configuration data. |

#### 220000 - WinCC communication driver alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 220000 - WinCC communication driver alarms

The most important system events are listed below.

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 220001 | The tag is not downloaded because write access to data type Bool/Bit is not supported by the sublevel communication driver/HMI device. | Change the configuration. |
| 220002 | The tag is not downloaded because write access to data type Byte is not supported by the sublevel communication driver/HMI device. | Change the configuration. |
| 220003 | The communications driver could not be loaded. The driver might not be installed. | Install the driver by reinstalling WinCC Runtime. |
| 220004 | Communication is down and no update data is transferred because the cable is not connected or defective etc. | Check the connection. |
| 220005 | Communication is up. | -- |
| 220006 | The connection between the specified PLC and the specified port is active. | -- |
| 220007 | The connection to the specified PLC is interrupted at the specified port. | Check the following:  - Is the cable plugged in? - Is the PLC OK? - Is the right port being used? - Is your configuration OK (port parameters, protocol settings, PLC address)?   Restart the system if the system event persists. |
| 220008 | The communication driver cannot access or open the specified port. This port might be in use by another application, or a port that does not exist on the target device is being used.  No communication with the PLC. | Close all applications that access the port and restart the computer.  Use another port that exists in the system. |
| 220009 | The communication path is either empty, incomplete or has an invalid format. | Enter the communication path in the correct format. |

---

**See also**

[Distinctive features when configuring (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#distinctive-features-when-configuring-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### 230000 - Screen object alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 230000 - Screen object alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 230000 | The value entered could not be used. The system discards this entry and restores the previous value.  Possible causes:  - The range of values is exceeded. - You entered invalid characters - The valid maximum number of users has been exceeded. | Enter a practical value, or delete a user that is no longer required. |
| 230002 | The user currently logged on does not have the necessary authorization, so the system discards the entry and restores the previous value. | Log on as user with appropriate authorization. |
| 230003 | Change to the specified screen failed because this screen is not available/configured. The current screen remains selected. | Configure the screen and check the selection function. |
| 230005 | The range of values of the tag has been exceeded in the I/O field. The original tag value is retained. | Observe the range of values for the tag when entering a value. |
| 230100 | During navigation in the Web browser, the system returned a message which may be of interest to the user. The Web browser continues to run but may not (fully) show the new page. | Navigate to another page. |
| 230200 | The HTTP channel connection was interrupted due to an error. This error is explained in detail by another system event. Data is no longer exchanged. | Check the network connection. Check the server configuration. |
| 230201 | The HTTP channel connection is set up. Data is exchanged. | -- |
| 230202 | WININET.DLL has detected an error. Usually, this error occurs if it is not possible to connect to the server, or the server denies a connection because the client lacks proper authorization. An unknown server certificate may also be the cause if the connection is encrypted by means of SSL. The alarm text provides details. This text is always in the language of the Windows installation because it is returned by the Windows OS. Process values are no longer exchanged. The part of the alarm returned by the Windows OS might not be displayed, e.g. "An error has occurred". WININET.DLL returns the following error: Number: 12055 Text:HTTP: &lt;no error text available&gt;." | Depending on the cause:  When an attempt to connect fails, or a timeout occurs:  - Check the network connection and the network. - Check the server address. - Check whether the WebServer is actually running on the target station.   Incorrect authorization:  - The configured user name and/or password do not match the entries on the server. Set consistent data.   If the server certificate is rejected: Certificate signed by an unknown CA ( ):  - Ignore this point, or install a certificate that has been signed with one of the root certificates known to the client station.   The date of the certificate is invalid:  - Ignore this point, or install a certificate with valid date on the server.   Invalid CN (Common Name or Computer Name):  - Ignore this point, or install a certificate with a name that corresponds to the server address. |
| 230203 | Although a connection can be made to the server, the HTTP server refused to connect. Possible causes:  - WinCC Runtime does not run on the server - The HTTP channel is not supported (503 Service unavailable).   Other errors can only occur if the Webserver does not support the HTTP channel. The language of the alarm text depends on the Webserver. Data is not exchanged. | On 503 Service unavailable error:  Check whether WinCC Runtime is running on the server and whether the HTTP channel is supported. |
| 230301 | Internal error. An English text explains the error in more detail. The error may be caused by insufficient memory. OCX does not work. | -- |
| 230302 | The name of the remote server cannot be resolved. An attempt to connect has failed. | Check the configured server address. Check whether the DNS service is available on the network. |
| 230303 | The remote server is not running on the addressed computer. incorrect server address. An attempt to connect has failed. | Check the configured server address. Check whether the remote server is running on the target computer. |
| 230304 | The remote server on the addressed computer is incompatible with VNCOCX. An attempt to connect failed. | Use a compatible remote server. |
| 230305 | Authentication has failed due to incorrect password. An attempt to connect failed. | Configure the correct password. |
| 230306 | Error in the connection to the remote server. This may occur as a result of network problems. An attempt to connect failed. | Check whether the network cable is plugged in, or whether there are network problems. |
| 230307 | The connection to the remote server was shut down. Possible causes:  - The remote server was shut down - The user instructed the server to close all connections.   The connection is cancelled. | -- |
| 230308 | This alarm provides information on the connection status. An attempt is made to connect. | -- |

> **Note**
>
> **Alarms without additional information**
>
> Alarms 230400-230409 and 230500-230501 are not described since the alarm text contains all the necessary information.

#### 240000 - Authorization alarms (Panels, Comfort Panels, RT Advanced)

##### 240000 - Authorization alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 240000 | WinCC Runtime is running in demo mode. You have no authorization, or your authorization is corrupted. | Install the authorization. |
| 240001 | WinCC Runtime is running in demo mode. You configured too many tags for the installed version. | Load an adequate authorization / powerpack. |
| 240002 | WinCC Runtime is running with time-limited emergency authorization. | Restore the full authorization. |
| 240004 | Error when reading the emergency authorization. WinCC Runtime is running in demo mode. | Restart WinCC Runtime. Install or repair the authorization (see Commissioning Instructions for Software Protection). |
| 240005 | Automation License Manager has detected an internal system error.  Possible causes:  - Corrupted file - Faulty installation - No free memory space for Automation License Manager, or similar. | Restart the HMI device/PC. If this procedure does not solve the problem, remove and then reinstall Automation License Manager. |

#### 250000 - S7 Status/Force alarms (Panels, Comfort Panels, RT Advanced)

##### 250000 - S7 Status/Force alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 250000 | The tag in the specified line in "Status Force" is not updated because the address configured for this tag is not available. | Check the set address and then verify that the address is set up in the PLC. |
| 250001 | The tag in the specified line in "Status Force" is not updated because the PLC type configured for this tag does not exist. | Check the set address. |
| 250002 | The tag in the specified line in "Status Force" is not updated because it is not possible to map the PLC type in the tag type. | Check the set address. |
| 250003 | An attempt to connect to the PLC failed. The tags are not updated. | Check the connection to the PLC. Check that the PLC is switched on and is online. |

#### 260000 - Password system alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 260000 - Password system alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 260000 | An unknown user or an unknown password has been entered in the system. The current user is logged off from the system. | Log on to the system as a user with a valid password. |
| 260001 | The logged in user does not have sufficient authorization to execute the protected functions on the system. | Log on to the system as a user with sufficient authorization. |
| 260002 | This alarm output when the "TrackUserChange" system function is triggered. | -- |
| 260003 | The user has logged off from the system. | -- |
| 260004 | The user name entered into the user view already exists in the user management. | Select another user name because user names have to be unique in the user management. |
| 260005 | The entry is discarded. | Enter a shorter user name. |
| 260006 | The entry is discarded. | Enter a shorter or longer password. |
| 260007 | The logoff time entered is outside the valid range from 0 to 60 minutes. The new value entered is discarded and the original value is retained. | Enter a logon timeout value between 0 and 60 minutes. |
| 260008 | An attempt was made in WinCC to read a PTProRun.pwl file created with ProTool V 6.0. Reading of the file was canceled due to incompatibility of the format. | -- |
| 260009 | You have attempted to delete the user "Administrator" or "PLC User". These users are fixed components of the user management and cannot be deleted. | If you need to delete a user, because perhaps you have exceeded the maximum number permitted, delete another user. |
| 260012 | The password entries in the "Change password" dialog box and in the confirmation field do not match. The password is not changed. User will be logged off. | You have to log on to the system again. Then enter the identical passwords twice to be able to change the password. |
| 260013 | The password entered in the "Change password" dialog box is invalid because it has already been used. The password is not changed. User will be logged off. | You have to log on to the system again. Then enter a new password that has not been used before. |
| 260014 | You have tried to log on with an incorrect password three times in a row. You will be locked out and assigned to group no. 0. | You can log on to the system with your correct password. Only an administrator can change the assignment to a group. |
| 260024 | The password you entered does not meet the necessary security guidelines. | Enter a password that contains at least one number. |
| 260025 | The password you entered does not meet the necessary security guidelines. | Enter a password that comprises at least three characters. |
| 260026 | The password you entered does not meet the necessary security guidelines. | Enter a password that contains at least one special character. |
| 260028 | Upon system start-up, an attempt to log on, or when trying to change the password of a SIMATIC log-on user, the system attempts to access the SIMATIC Logon Server.  If attempting to log on, the new user is not logged in. If a different user was logged on before, then this user is logged off. | Check the connection to the SIMATIC Logon Server and its configuration; for example:  1. Port number  2. IP address  3. Server name  4. Functional transfer cable.  Or use a local user. |
| 260030 | The SIMATIC Logon user could not change their password on the SIMATIC Logon Server. The new password is possibly non-compliant with password rules set on the server, or the user is not authorized to change their password.  The old password remains and the user is logged off. | Log on again and select a different password. Check the password rules on the SIMATIC Logon Server. |
| 260033 | The "Change password" or "Log on user" actions could not be performed. | Check the connection to the SIMATIC Logon Server and its configuration; for example:  1. Port number  2. IP address  3. Server name  4. Functional transfer cable  Or use a local user. |
| 260034 | The last logon operation has not yet ended. A user action or a logon dialog can therefore not be called.  The logon dialog is not opened. The user action is not executed. | Wait until the logon operation is complete. |
| 260035 | The last attempt to change the password was not completed. A user action or a logon dialog can therefore not be called.  The logon dialog is not opened. The user action is not executed. | Wait until the procedure is complete. |
| 260036 | There are insufficient licenses on the SIMATIC Logon Sever. The logon is not authorized. | Check the licensing on the SIMATIC Logon Server. |
| 260037 | There is no license on the SIMATIC Logon Sever. A logon is not possible.  It is not possible to log on via the SIMATIC Logon Server, only via a local user. | Check the licensing on the SIMATIC Logon Server. |
| 260040 | The system attempts to access the SIMATIC Logon Server upon system start-up or when trying to change the password.  If attempting to log on, the new user is not logged in. If a different user was logged on before, then this user is logged off. | Check connection to the domain and its configuration in the Runtime security settings editor.  Or use a local user. |
| 260043 | It was not possible to log the user on to the SIMATIC Logon Server. The user name or the password could be incorrect or the user does not have sufficient rights to log on.  The new user is not logged in. If a different user was logged on before, then this user is logged off. | Try again. If necessary, check the password data on the SIMATIC Logon Server. |
| 260044 | It was not possible to log the user on to the SIMATIC Logon Server as their account is blocked.  The new user is not logged in. If a different user was logged on before, then this user is logged off. | Check the user data on the SIMATIC Logon Server. |
| 260045 | The SIMATIC Logon user is not associated to any or several groups.  The new user is not logged in. If a different user was logged on before, then this user is logged off. | Check user data on the SIMATIC Logon Server and the configuration in your WinCC project. A user may only be assigned to one group. |

> **Note**
>
> **Alarms without additional information**
>
> Alarms 260010, 260011, 260015-260023, 260029, 260031, 260032, 260038, 260039, 260041, 260042 and 260048 are not described since the alarm text contains all the necessary information.

#### 270000 - System alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 270000 - System Alarms

The most important system events are listed below.

| Number | Effect/causes | Remedy |
| --- | --- | --- |
| 270000 | The alarm does not indicate the tag because it is accessing an invalid address in the PLC. | Check whether the data area for the tag exists on the PLC, whether the configured address is correct, and whether the value range for the tag is correct. |
| 270001 | There is a device-specific limit as to how many alarms may be queued for viewing (see the operating instructions). This limit has been exceeded. The view no longer contains all the alarms. However, all alarms are written to the alarm buffer. | -- |
| 270002 | The view shows alarms of a log for which there is no data in the current project. Placeholders are output for the alarms. | Delete old log data, if necessary. |
| 270003 | The service cannot be set up because too many devices want to access this service. A maximum of four devices can execute this action. | Reduce the number of HMI devices which want to use the service. |
| 270004 | Access to the persistent alarm buffer is not possible. Alarms cannot be restored or backed up. | If the problems persist at the next restart, contact Customer Support (delete Flash). |
| 270005 | Persistent alarm buffer corrupted: Alarms cannot be restored. | If the problems persist at the next restart, contact Customer Support (delete Flash). |
| 270006 | Project modified: Alarms cannot be restored from the persistent alarm buffer. | The project was compiled and downloaded again to the HMI device. The error should no longer occur at the next restart of the HMI device. |
| 270007 | A configuration problem is preventing you from the restoring the data (e.g. a DLL was deleted, or unknown directory). | Update the operating system and download your project again to the HMI device. |

#### 280000 - Alarms SIMATIC 505 DP Communication Driver (CSP) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Alarms SIMATIC 505 DP Communication Driver (CSP)

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 280000 | The connection between the controller and port is active. | -- |
| 280001 | The connection to the PLC at the port is interrupted. | Check the following:   - Is the cable plugged in? - Is the controller active? - Is the correct port being used? - Is the configuration OK? |
| 280002 | The parameters of the controller are correct, the XSUB and .REC files are available. | -- |
| 280003 | - The parameters of the controller are correct, the XSUB and .REC files are not available. - The controller is in STOP mode. | - Download the XSUB and .REC files to the controller. - Verify that the controller is in STOP mode. |
| 280004 | - The communication cable between HMI device and controller is disconnected. - The controller is in STOP mode. | Check the following:   - The communication cable between operating unit and controller - Mode of the controller (Run/STOP) |

#### 290000 - Recipe system alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### 290000 - Recipe system alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 290000 | The recipe tag could not be read or written. It is assigned the start value. The alarm can be entered in the alarm buffer for up to four more faulty tags. After that, alarm 290003 is output. | Check the configuration to see whether the address has been set up in the PLC. |
| 290001 | An attempt was made to assign the recipe tag a value that is outside the valid range of values for this type. The alarm can be entered in the alarm buffer for up to four more faulty tags if necessary. After that, alarm 290004 is output. | Observe the range of values for the tag type. |
| 290002 | It is not possible to convert a value from a source format to a target format. The alarm can be entered in the alarm buffer for up to four more faulty recipe tags if necessary. After that, alarm 290005 is output. | Check the range of values or type of the tag. |
| 290003 | This alarm is output after alarm 290000 was triggered more than five times. In this case, no further separate alarms are generated. | Check the configuration to see whether the tag addresses have been set up in the PLC. |
| 290004 | This alarm is output after alarm 290001 was triggered more than five times. In this case, no further separate alarms are generated. | Observe the range of values for the tag type. |
| 290005 | This alarm is output after alarm 290002 was triggered more than five times. In this case, no further separate alarms are generated. | Check the range of values or type of the tag. |
| 290006 | The limits configured for the tag have been exceeded by the values entered. | Observe the configured or current tag limits. |
| 290007 | There is a difference between the source and target structure in the recipe currently being processed. The source structure contains an additional recipe tag that is not available in the target structure and cannot be assigned. The value is discarded. | Remove the specified recipe tag in the specified recipe from your configuration. |
| 290008 | There is a difference between the source and target structure in the recipe currently being processed. The target structure contains an additional recipe tag that is not available in the source structure. The recipe tag specified is assigned its start value. | Insert the specified recipe tag into the source structure. |
| 290010 | The storage location configured for the recipe is invalid. Possible causes: Invalid characters, write protection, data carrier out of space or not available. | Check the configured storage location. |
| 290011 | A data record of the specified number does not exist. | Check the source for the number (constant or tag value). |
| 290012 | A recipe of the specified number does not exist. | Check the source for the number (constant or tag value). |
| 290013 | An attempt was made to save a data record under a data record number that already exists. The operation is not executed. | The following remedies are available:  - Check the source for the number (constant or tag value). - First, delete the data record. - Modify the "Overwrite" function parameter. |
| 290014 | The specified import file was not found. | Check the following:  - The file name - Ensure that the file is in the specified directory. |
| 290020 | Check back to verify that the download of data records from the HMI device to the PLC has started. | -- |
| 290021 | Check back to verify that the download of records from the HMI device to the PLC was completed. | -- |
| 290022 | Check back to indicate that the download of data records from the HMI device to the PLC was canceled due to an error. | Check the following conditions in the configuration:  - Are the tag addresses configured in the PLC? - Does the recipe number exist? - Does the data record number exist? - Is the "Overwrite" function parameter set? |
| 290023 | Check back to verify that the download of data records from the PLC to the HMI device has started. | -- |
| 290024 | Check back to verify that the download of data records from the PLC to the HMI device was completed. | --- |
| 290025 | Check back to indicate that the download of data records from the PLC to the HMI device was canceled due to an error. | Check the following conditions in the configuration:  - Are the tag addresses configured in the PLC? - Does the recipe number exist? - Does the data record number exist? - Is the "Overwrite" function parameter set? |
| 290026 | An attempt was made to read/write a data record that is not free at present. This error can occur if recipes were configured for download with synchronization. | Set the mailbox status to zero. |
| 290027 | Unable to connect to the PLC at present. As a result, the data record cannot be read or written. Possible causes: No hardware connection to the PLC (no cable plugged in, cable is defect), or the PLC is switched off. | Check the connection to the PLC. |
| 290030 | This alarm is output after you selected screen which contains a recipe view in which a data record is already selected. | Reload the data record from the storage location, or retain the current values. |
| 290031 | While saving, it was detected that a data record with the specified number already exists. | Overwrite the data record, or cancel the action. |
| 290032 | During the export of data records, a file with the specified name was found. | Overwrite the file, or cancel the process. |
| 290033 | Confirmation prompt before deleting data records. | -- |
| 290040 | A data record error with error code %1 that cannot be described in more detail occurred. The action is canceled. It is possible that the mailbox was not installed correctly on the PLC. | Check the storage location, the data record, the "Data record" area pointer, and the connection to the PLC. Restart the action after a short waiting time. If the error persists, contact Customer Support. Forward the relevant error code to Customer Support. |
| 290041 | A data record or file cannot be saved because the storage location is out of sufficient space. | Delete files no longer required. |
| 290042 | An attempt was made to execute several recipe actions simultaneously. The last action is not executed. | Retrigger the action after a short waiting time. |
| 290043 | Confirmation prompt before saving data records. | -- |
| 290044 | The database for the recipe was corrupted and will be deleted. | -- |
| 290050 | A check back indicates that the export of data records was started. | -- |
| 290051 | A check back indicates successful completion of the export of data records. | -- |
| 290052 | A check back indicates that the export of data records was canceled due to an error. | Ensure that the structure of the data records at the storage location and the current recipe structure on the HMI device are identical. |
| 290053 | A check back indicates that the import of records was started. | -- |
| 290054 | A check back indicates successful completion of the import of data records. | -- |
| 290055 | A check back indicates that the import of data records was canceled due to an error. | Ensure that the structure of the data records at the storage location and the current recipe structure on the HMI device are identical. |
| 290056 | Error when reading/writing the value in the specified row/column. The action was canceled. | Check the specified row/column. |
| 290057 | The tags of the recipe specified were toggled from "offline" to "online" mode. Each change of a tag in this recipe is now immediately transferred to the PLC. | -- |
| 290058 | The tags of the specified recipe were toggled from "online" to "offline" mode. Modifications to tags in this recipe are no longer immediately transferred to the PLC but must be transferred there explicitly by downloading a data record. | -- |
| 290059 | A check back indicates that the specified record was successfully saved. | -- |
| 290060 | A check back indicates that the specified data record memory was cleared. | -- |
| 290061 | A check back indicates that deletion of the data record memory was canceled due to an error. | -- |
| 290062 | The data record number exceeds the maximum of 65536. This data record cannot be created. | Select another number. |
| 290063 | This occurs when you execute system function "ExportDataRecords" while the "Overwrite" parameter is set to "No".  An attempt was made to save a recipe under a file name that already exists. The export is canceled. | Check the parameters of the "ExportDataRecords" system function. |
| 290064 | A check back indicates that the deletion of data records was started. | -- |
| 290065 | A check back indicates successful completion of the deletion of data records. | -- |
| 290066 | Confirmation prompt before deleting data records. | -- |
| 290068 | Confirmation prompt for deletion of the selected recipe data records. | -- |
| 290069 | Confirmation prompt for deletion of all recipe data records. | -- |
| 290070 | The data record specified was not found in the import file. | Check the source of the data record number, or the data record name (constant, or tag value). |
| 290071 | When the editing data record values, you entered a value that is below the low limit of the recipe tag. The entry is discarded. | Enter a value within the recipe tag limits. |
| 290072 | When editing data record values, you entered a value that exceeds the high limit of the recipe tag. The entry is discarded. | Enter a value within the recipe tag limits. |
| 290073 | An action (e.g. saving a record) failed for an unknown reason. The error corresponds to status alarm IDS_OUT_CMD_EXE_ERR in the large recipe view. | -- |
| 290074 | While saving, a data record with the specified number but with different name was found. | Overwrite the record, change the record number or cancel the action. |
| 290075 | A data record of this name already exists. The data record is not saved. | Select a different data record name. |
| 290110 | The default values could not be set due to an error. | -- |
| 290111 | The recipes subsystem cannot be used. Recipe views have no content and recipe-specific functions will not be executed.  Possible causes:  - Error when loading the recipes. - The recipe structure was changed in the ES. The recipes were not included in the latest project download. This means that the new configuration data no longer matches the old recipes on the device. | Download the project to the device again, including the recipes (the corresponding check box in the download dialog must be check marked). |

> **Note**
>
> **Alarms without additional information**
>
> Alarms 290067 and 290076-290109 are not described since the alarm text contains all the necessary information.

#### 300000 - Alarm_S alarms (Panels, Comfort Panels, RT Advanced)

##### 300000 - Alarm_S alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 300000 | Faulty configuration of process monitoring (e.g. using PDiag or S7-Graph): More alarms are queued than specified in the specifications of the CPU. No further ALARM_S alarms can be managed by the PLC and reported to the HMI devices. | Change the PLC configuration. |
| 300001 | ALARM_S is not registered on this PLC. | Select a controller that supports the ALARM_S service. |

> **Note**
>
> **Alarms without additional information**
>
> Alarms 300100-300102 are not described since the alarm text contains all the necessary information.

#### 310000 - Reporting alarms (Panels, Comfort Panels, RT Advanced)

##### 310000 - Reporting alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 310000 | An attempt is being made to print too many reports in parallel. Only one log file can be output to the printer at a given time; the print job is therefore rejected. | Wait until the previous active log was printed. Repeat the print job if necessary. |
| 310001 | An error occurred on triggering the printer. The report is either not printed or printed with errors. | Evaluate the additional system events related to this alarm. Repeat the print job if necessary. |

#### 330000 - Interaction alarms (Panels, Comfort Panels, RT Advanced)

##### 330000 - Interaction alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 330022 | Too many open dialogs on the HMI device. | Close all dialogs you do not require on the HMI device. |

> **Note**
>
> **Alarms without additional information**
>
> Alarms 330001-330021, 330023-330070 are not described since the alarm text contains all the necessary information.

#### 340000 - Alarms info text (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### 340000 - Alarms info text

> **Note**
>
> **Alarms without additional information**
>
> Alarms 340001-340005 are not described since the alarm text contains all the necessary information.

#### 350000 - PROFIsafe alarms (Panels, Comfort Panels, RT Advanced)

##### 350000 - PROFIsafe alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 350000 | PROFIsafe packets were not received within the specified time. There is a communication problem with the F-CPU.   RT is terminated. | Check the WLAN connection. |
| 350001 | PROFIsafe packets were not received within the specified time. There is a communication problem with the F-CPU.  The PROFIsafe connection is set up again. | Check the WLAN connection. |
| 350002 | Internal error.  Runtime is terminated. | Internal error |
| 350003 | Check back for indicating the connection setup to the F-CPU.  The Emergency-Off buttons are active immediately. | -- |
| 350004 | PROFIsafe communication was set up and the connection was shut down. Runtime can be terminated.  The Emergency-Off buttons are deactivated immediately. | -- |
| 350005 | Incorrect address configured for the F-Device. A PROFIsafe connection cannot be set up. | Check and change the address of the F device in the WinCC ES. |
| 350006 | The project was started. At the start of the project, check the proper function of the ACK buttons. | Press the two ACK buttons successively in the "Acknowledge" and "Panic" positions. |
| 350008 | You configured an incorrect number of failsafe buttons.  A PROFIsafe connection cannot be set up. | Modify the number of failsafe buttons in the project. |
| 350009 | The device is in Override mode.   It may no longer be possible to detect the location because transponder detection fails. | Exit the override mode. |
| 350010 | Internal error: The device has no failsafe buttons. | Return the device to Siemens.  Worldwide contact partners |

#### 380000 - Alarms Sm@rtServer (Panels, Comfort Panels, RT Advanced, RT Professional)

##### 380000 - Alarms Sm@rtServer

> **Note**
>
> **Alarms without additional information**
>
> Alarms 380000-380100 are not described since the alarm text contains all the necessary information.

#### 390000 alarm password encryption and certificates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### 390000 alarm password encryption and certificates

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 390000 | The Runtime project was loaded by a different Windows user than the one who created the password encryption certificate. | A Runtime project with encrypted communication connections to S7 controllers must be loaded for each Windows user who wants to use these connections in Runtime. |

> **Note**
>
> **Alarms without additional information**
>
> Alarms 390001-390003 are not described because the alarm text contains all necessary information.

#### 1000000 - WinCC communication driver alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### 1000000 - WinCC communication driver alarms

The most important system events are listed below.

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1000306 | General certificate error for connection %s to IP address: %s, detailed error code %s. | To establish a new connection, reinstall the certificate. |
| 1000307 | The validity of the PLC certificate %s has expired, detailed error code %s. | Install a new certificate. |
| 1000308 | The PLC certificate %s is not trusted. Manual trusting is possible, detailed error code %s" | Install a new certificate. |
| 1000309 | The PLC certificate %s is not trusted. Manual trusting is not possible, detailed error code %s. | Install a new certificate. |
| 1000310 | The PLC certificate %s was revoked, detailed error code %s". | Install a new certificate. |

### System events (RT Professional)

This section contains information on the following topics:

- [System events (RT Professional)](#system-events-rt-professional-1)
- [1000000 - Alarms Runtime](#1000000---alarms-runtime)
- [1000800 - Alarms WinCC client](#1000800---alarms-wincc-client)
- [1000900 - Alarms Performance Monitor](#1000900---alarms-performance-monitor)
- [1001000 - Alarms Screens in Runtime](#1001000---alarms-screens-in-runtime)
- [1002000 - Alarms Tag logging](#1002000---alarms-tag-logging)
- [1003018 - Alarms Alarm system](#1003018---alarms-alarm-system)
- [1004000 - Alarms Print jobs](#1004000---alarms-print-jobs)
- [1005000 - Alarms Text library](#1005000---alarms-text-library)
- [1006000 - Alarms Global scripts](#1006000---alarms-global-scripts)
- [1008000 - Alarms User administration](#1008000---alarms-user-administration)
- [1009000 - Alarms Lifebeat Monitoring](#1009000---alarms-lifebeat-monitoring)
- [1010000 - Alarms STRRT](#1010000---alarms-strrt)
- [1011000 - Alarms Group display](#1011000---alarms-group-display)
- [1011101 - Alarms Picture Tree Manager](#1011101---alarms-picture-tree-manager)
- [1011201 - Alarms Split Screen Manager](#1011201---alarms-split-screen-manager)
- [1012001 - Alarms Time synchronization](#1012001---alarms-time-synchronization)
- [1012200 - Alarms Redundancy](#1012200---alarms-redundancy)
- [1012400 - Alarms WebNavigatorClient](#1012400---alarms-webnavigatorclient)
- [1012500 - Alarms Process Historian](#1012500---alarms-process-historian)
- [1012700 - Alarms Redundancy self-diagnostics](#1012700---alarms-redundancy-self-diagnostics)
- [1016000 - Alarms IndustrialDataBridge](#1016000---alarms-industrialdatabridge)
- [12508141 - Alarms](#12508141---alarms)

#### System events (RT Professional)

##### Introduction

The system events generated by the various WinCC modules are described below. You can integrate these events into your alarm system using the "WinCC - System Events" menu command.

> **Note**
>
> You can obtain additional information on the system events in the "Comment" block of the active alarm.

> **Note**
>
> System events are output in an alarm view. System events are output in the language currently set on your HMI device.
>
> The time format (AM/PM or 24-hour format) is based on the selected language. If no translation of the alarm texts exists in this language, English is used as replacement and the corresponding time format is displayed.

---

**See also**

[System events (Panels, Comfort Panels, RT Advanced, RT Professional)](#system-events-panels-comfort-panels-rt-advanced-rt-professional)

#### 1000000 - Alarms Runtime

##### Meaning of the system events

The most important system alarms are listed below.

1000000 - Alarms WinCC Runtime

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1000000 | Error |  |
| 1000001 | Error while loading the object engine |  |
| 1000002 | Channel could not be loaded |  |
| 1000003 | Tag - Low limit violation |  |
| 1000004 | Tag - High limit violation |  |
| 1000005 | Error formatting a tag |  |
| 1000006 | Error scaling a tag |  |
| 1000100 | Driver error |  |
| 1000200 | Status |  |
| 1000201 | Object engine was loaded |  |
| 1000202 | Runtime was activated |  |
| 1000203 | Runtime was deactivated |  |
| 1000204 | Connection not established |  |
| 1000205 | Connection established |  |
| 1000206 | Client connection established |  |
| 1000207 | Client connection terminated |  |
| 1000208 | Client connection terminated |  |
| 1000209 | Connection deleted |  |
| 1000210 | Connection changed |  |
| 1000211 | Connection reestablished |  |
| 1000300 | Driver status |  |
| 1000301 | The legitimization of the connection @1%s@ has failed. The password is wrong! |  |
| 1000302 | The PLC is protected. A password must be configured for the connection @1%s@. |  |
| 1000303 | The legitimization of the connection @1%s@ has failed. The password is locked Unlock locally (e.g. on the display). |  |

#### 1000800 - Alarms WinCC client

##### Meaning of the system events

The most important system alarms are listed below.

1000800 - Alarms WinCC client

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1000800 | Import |  |
| 1000801 | Export |  |
| 1000802 | Delete |  |
| 1000803 | New |  |
| 1000804 | Reload |  |
| 1000805 | Default server |  |
| 1000806 | Implicit update |  |
| 1000807 | Update |  |

#### 1000900 - Alarms Performance Monitor

##### Meaning of the system events

The most important system alarms are listed below.

1000900 - Alarms Performance Monitor

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1000900 | @1%s@:@7%s@ is low |  |
| 1000901 | @1%s@:@7%s@ is OK |  |
| 1000902 | @1%s@:@7%s@ is high |  |
| 1000903 | @1%s@:@7%s@ is OK |  |
| 1000904 | @1%s@:@7%s@ is low |  |
| 1000905 | @1%s@:@7%s@ is OK |  |
| 1000906 | @1%s@:@7%s@ is high |  |
| 1000907 | @1%s@:@7%s@ is OK |  |
| 1000908 | @1%s@:@7%s@ is low |  |
| 1000909 | @1%s@:@7%s@ is OK |  |
| 1000910 | @1%s@:@7%s@ is high |  |
| 1000911 | @1%s@:@7%s@ is OK |  |
| 1000912 | @1%s@:Redundancy loss of terminal adapter @2%s@ |  |
| 1000913 | @1%s@:Redundancy of terminal adapter @2%s@ restored |  |
| 1000914 | @1%s@:Terminal adapter @2%s@ connected |  |
| 1000915 | @1%s@:Terminal adapter @2%s@ disconnected |  |

#### 1001000 - Alarms Screens in Runtime

##### Meaning of the system events

The most important system alarms are listed below.

1001000 - Alarms Screens in Runtime

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1001000 | General error |  |
| 1001001 | Operator action not active |  |
| 1001002 | Wrong picture format |  |
| 1001003 | Picture not found |  |
| 1001004 | No dynamic active in picture |  |
| 1001005 | Tag could not be written |  |
| 1001006 | Dynamic actions in picture are not active |  |

#### 1002000 - Alarms Tag logging

##### Meaning of the system events

The most important system alarms are listed below.

1002000 - Alarms Tag logging

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1002000 | General error |  |
| 1002001 | Error during initialization |  |
| 1002002 | Error loading the runtime data |  |
| 1002003 | Error changing languages |  |
| 1002004 | Error accessing the database |  |
| 1002005 | Error creating runtime objects |  |
| 1002006 | Error in online configuration |  |
| 1002007 | Error in client/server environment |  |
| 1002008 | Error in memory management |  |
| 1002009 | Error compiling measured values |  |
| 1002010 | Error processing measured values |  |
| 1002011 | Error logging measured values |  |
| 1002012 | Error in Normalization DLL |  |
| 1002013 | Error in user archive option |  |
| 1002014 | Error in process-controlled logging |  |
| 1002015 | Error in API |  |
| 1002016 | Error in application window |  |
| 1002017 | System fault |  |
| 1002018 | Error overflow in database queue |  |
| 1002019 | Error overflow in notification queue |  |
| 1002020 | Error overflow of the Normalization DLL queue - loss of data! |  |
| 1002021 | Problems with the connection to the central archive server. |  |
| 1002022 | The problem in the connection to the central archive server has been eliminated. |  |
| 1002023 | Archive value edited - Archive tag=@10%s@ Time stamp=@1%s@ New value=@2%s@ Old value=@3%s@ |  |
| 1002024 | Archive value created - Archive tag=@10%s@ Time stamp=@1%s@ Value=@2%s@ |  |

#### 1003018 - Alarms Alarm system

##### Meaning of the system events

The most important system alarms are listed below.

1003018 - Alarms Alarm system

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1003018 | Alarm does not require acknowledgment  An attempt was made to acknowledge a alarm that does not require acknowledgment. |  |
| 1003019 | Alarm has already been acknowledged  An attempt was made to acknowledge a alarm that has already been acknowledged. |  |
| 1003020 | Alarm class for the alarm not found  The alarm class associated with the alarm does not exist. |  |
| 1003021 | Alarm status cannot be processed  The alarm status (Incoming, Outgoing, Acknowledged, ...) could not be interpreted. |  |
| 1003022 | Alarm is locked  This alarm occurs if you attempt to trigger a locked alarm via the API. |  |
| 1003023 | Alarm date/time stamp invalid  The date/time stamp from the AS could not be interpreted. |  |
| 1003032 | Alarm window template name unknown  This error occurs when an alarm window that is already configured in the "Screens" editor is subsequently deleted.   In the case of client/server projects, this alarm could also be triggered by a communication error in the network. |  |
| 1003033 | Alarm window could not be created |  |
| 1003034 | Alarm window - data invalid  Incorrect project data. |  |
| 1003048 | Bit is outside the tag range  For example, an attempt was made to trigger the 18th bit of a 16-bit tag. |  |
| 1003049 | No tag change |  |
| 1003050 | Event tag (bit) already occupied by an alarm  The bit of the alarm tag has already been interconnected with an alarm. |  |
| 1003051 | Acknowledgment tag (bit) already occupied by an alarm  The acknowledgment tag bit has already been interconnected with an alarm. |  |
| 1003052 | Status tag already occupied by an alarm  The bit of the status tag has already been interconnected with an alarm. |  |
| 1003053 | Error during conversion of Variant data type |  |
| 1003054 | Event tag (bit) already occupied--&gt;different type |  |
| 1003055 | Event tag or tag type invalid  The data type of the alarm tag is invalid. You may have used a tag with sign. |  |
| 1003056 | Acknowledgment tag or tag type invalid |  |
| 1003057 | Status tag or tag type invalid  The data type of the status tag is invalid. You may have used a tag with sign. |  |
| 1003058 | Handle invalid  This error message can occur during access via the API. |  |
| 1003059 | Selection criteria invalid  This error message can occur during access via the API. |  |
| 1003060 | Resources DLL for language not found  One of the language-dependent files is missing. |  |
| 1003061 | Error while creating the memory mapped file  This internal error indicates a problem involving the memory. |  |
| 1003062 | Error while creating the synchronization mechanism  This error occurs when the operating system is overloaded. |  |
| 1003063 | Incorrect parameter  The error message can occur during access via the API. |  |
| 1003064 | Transfer buffer too small  The error message can occur during access via the API. |  |
| 1003065 | Function is not available at this time  The error message can occur during access via the API. |  |
| 1003066 | Format DLL send data cannot be evaluated |  |
| 1003067 | Format DLL Do not execute function |  |
| 1003068 | No alarm text blocks in the report | Check the alarm sequence report. |
| 1003069 | Invalid protocol identifier |  |
| 1003070 | Report printout is already active  An attempt was made to restart an active report. |  |
| 1003071 | Alarm system runtime &lt;server&gt; not initialized  The server reports that the project was activated without the runtime component of Alarm Logging. |  |
| 1003072 | Printout of the alarm sequence report has not been started. |  |
| 1003073 | Printout of the short-term archive report has not been started. |  |
| 1003074 | Printout of the sequence archive report has not been started. |  |
| 1003075 | Maximum number of alarms that can be configured online  The maximum number of alarms that can be configured online (default setting is 600) has been exceeded. |  |
| 1003076 | Parameter error in S7 frame  A parameter error has occurred on the interface to S7. |  |
| 1003077 | Parameter error for ALGRT  A parameter error has occurred on the interface to ALGRT. |  |
| 1003078 | Parameter error for TLGRT  A parameter error has occurred on the interface to TLGRT. |  |
| 1003079 | Parameter error in additional data  The additional data of the alarms are faulty. |  |
| 1003080 | Parameter error in AR_SEND structure  The structure of the AR-SEND user data is faulty. |  |
| 1003081 | General error  An internal error of unknown cause has occurred. |  |
| 1003082 | Alarm loss on the automation system |  |
| 1003083 | Connecting and updating the automation system is underway |  |
| 1003084 | Connecting and updating the automation system is finished |  |
| 1003085 | System modification in RUN (CiR) active |  |
| 1003086 | System modification in RUN (CiR) is finished |  |
| 1003087 | Error while logging on to receive alarm. |  |
| 1003098 | Alarm logging overflow - alarms are lost |  |
| 1003099 | [Computer name]:Alarm [alarm number] locked [alarm text of locked alarm]  This alarm occurs when a alarm is locked. |  |
| 1003100 | [Computer name]:Alarm [alarm number] unlocked [alarm text of unlocked alarm]   This alarm occurs when a alarm is unlocked. |  |
| 1003101 | Acknowledgment request for alarm [alarm number] was issued  This alarm occurs when a alarm is acknowledged. |  |
| 1003102 | [Computer name]:Alarm group [alarm group number] locked  This alarm occurs when a alarm group is locked. |  |
| 1003103 | [Computer name]:Alarm group [alarm group number] unlocked  This alarm occurs when a alarm group is unlocked. |  |
| 1003104 | [Computer name]:Alarm logging overflow ended - no more alarms will be lost |  |
| 1003105 | [Computer name]:Incoming alarm queue has reached critical value |  |
| 1003106 | [Computer name]:Incoming alarm queue has reached normal value |  |
| 1003107 | [Computer name]:Alarm [alarm number] hidden:@1%s@ |  |
| 1003108 | [Computer name]:Alarm [alarm number] shown:@1%s@ |  |
| 1003109 | Connection to master is down. |  |
| 1003110 | Found incomplete configuration data for alarm [PC name]: . Status: @1%d@. |  |
| 1003300 | Edited configuration data for alarm found. |  |
| 1003301 | Error while logging on to receive alarm. |  |
| 1003302 | Not all alarms could be acknowledged due to temporary resource bottleneck. Acknowledge again. |  |

#### 1004000 - Alarms Print jobs

##### Meaning of the system events

The most important system alarms are listed below.

100400 - Alarms Print jobs

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1004000 | General error |  |
| 1004001 | PRT_OUT directory full |  |
| 1004002 | Spool directory full |  |
| 1004003 | Report was not printed. PRT_OUT directory full |  |
| 1004004 | Report was not printed. Spool directory full |  |
| 1004005 | Alarm sequence report is reprinted |  |
| 1004006 | Spool directory full |  |
| 1004007 | Hardcopy was not printed. Spool directory full |  |

#### 1005000 - Alarms Text library

##### Meaning of the system events

The most important system alarms are listed below.

100500 - Alarms Text library

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1005000 | General error |  |
| 1005001 | Error while logging off the Runtime applications. |  |
| 1005002 | Error while logging on the Runtime applications. |  |
| 1005003 | Error during initialization of the MMF.  A memory error has occurred. |  |
| 1005004 | Error while loading the MMF.  Error while accessing the database. |  |
| 1005005 | Error while opening the MMF.  A memory error has occurred. |  |
| 1005006 | Error while creating the service window. |  |
| 1005007 | No language found. |  |
| 1005008 | Text ID not found.  The requested Text ID could not be found in the text library. |  |
| 1005009 | Read access to the MMF denied. |  |
| 1005010 | Language not found.  The requested language has not been configured in the text library. |  |
| 1005011 | Languages table could not be opened.  Either the data are faulty or the table is locked in the database. |  |
| 1005012 | Text table could not be opened.  Either the data are faulty or the table is locked in the database. |  |
| 1005013 | Invalid language specified.  The Language ID specified is invalid. |  |
| 1005014 | DBConnect error  No connection to the database could be set up. |  |

#### 1006000 - Alarms Global scripts

##### Meaning of the system events

The most important system alarms are listed below.

100600 - Alarms Global scripts

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1006000 | Error |  |
| 1007000 | Overflow  Overload: either there are too many actions running in a cycle that is too small, or an action is suspended (endless loop, dialog output). All the other actions are in the queue and cannot be processed. |  |
| 1007001 | Action error  One of the following errors has occurred:  - Exception in the action (specific cause unknown) - Exception when accessing the return result (char* associated memory invalid) - Stack overflow upon execution of the action - The action contains a division by 0 - The action contains an access to a non-existing symbol - The action contains an access violation | You can integrate the OnErrorExecute function in your script, which allows for a detailed analysis of the error. |
| 1007002 | Overflow  Internal lists have overflowed. |  |
| 1007003 | Connection error  The connection to the server is broken. |  |
| 1007004 | Action error 1  The called function is not known. | Check the notation of the function call and implementation of the function. |
| 1007005 | Action error 2  This error can have several causes:  - The action does not contain a P code. Recompile the action. - The function could not be loaded, for example, due to incorrect function name. - The type of return value of the function is invalid. | You can integrate the OnErrorExecute function in your script, which allows for a detailed analysis of the error. |
| 1007006 | Tag error  A requested tag was not supplied by WinCC Explorer within 10 seconds. | Check the spelling of the tag name. In the case of external tags, there may be a communication problem between the WinCC Explorer and the PLC. You have the option to incorporate the OnErrorExecute function into your script, which allows for a detailed analysis of the error. |
| 1007007 | Info  Additional information under "Diagnostics of WinCC / Runtime Monitoring for Actions". |  |
| 1007009 | Error in thread  Additional information under "Diagnostics of WinCC / Runtime Monitoring for Actions". |  |

#### 1008000 - Alarms User administration

##### Meaning of the system events

The most important system alarms are listed below.

100800 - Alarms User administration

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1008000 | Connection to the smart card reader interrupted |  |
| 1008001 | Incorrect login name/password |  |
| 1008002 | Incorrect login name/password by smart card |  |
| 1008003 | Manual login |  |
| 1008004 | Login with smart card |  |
| 1008005 | Manual logout |  |
| 1008006 | Logout with smart card |  |
| 1008007 | Automatic logout through timer |  |
| 1008008 | Authorizations effective for service user/group '@102%s@' |  |

#### 1009000 - Alarms Lifebeat Monitoring

##### Meaning of the system events

The most important system alarms are listed below.

100900 - Alarms Lifebeat Monitoring

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1009000 | Error |  |
| 1009999 | Tag @2%s@ does not exist |  |

#### 1010000 - Alarms STRRT

##### Meaning of the system events

The most important system alarms are listed below.

101000 - Alarms STRRT

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1010000 | Error |  |

#### 1011000 - Alarms Group display

##### Meaning of the system events

The most important system alarms are listed below.

1011000 - Alarms Group display

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1011000 | Group display error at start up |  |
| 1011001 | Group display hierarchy not updated |  |
| 1011002 | Group display: Connection fault |  |
| 1011003 | Group display: Tag does not exist |  |

#### 1011101 - Alarms Picture Tree Manager

##### Meaning of the system events

The most important system alarms are listed below.

1011101 - Alarms Picture Tree Manager

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1011101 | Error during startup |  |

#### 1011201 - Alarms Split Screen Manager

##### Meaning of the system events

The most important system alarms are listed below.

1011201 - Alarms Split Screen Manager

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1011201 | Error during startup |  |
| 1011202 | The fill level of the project drive is over 80%. |  |
| 1011203 | The project was created with the wrong WinCC version. |  |

#### 1012001 - Alarms Time synchronization

##### Meaning of the system events

The most important system alarms are listed below.

1012001 - Alarms Time synchronization

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1012001 | Switched to master operation |  |
| 1012002 | Cannot send time frame |  |
| 1012003 | Time reception service: Poor or failed signal |  |
| 1012004 | Cannot receive time frame |  |
| 1012005 | Cannot receive any time frame on redundant bus |  |
| 1012006 | No time frame. Switch to redundant device |  |
| 1012007 | Can successfully send time frame |  |
| 1012008 | Time reception service functions properly |  |
| 1012009 | Can successfully receive time frames |  |
| 1012010 | Can receive time frames properly on redundant bus |  |
| 1012011 | Switched to slave operation |  |
| 1012012 | Time synchronization deactivated |  |
| 1012013 | Time synchronization activated |  |
| 1012014 | DCF77 client service failure |  |
| 1012015 | DCF77 client service functions properly |  |
| 1012016 | @2%s@ switched to master mode @3%s@ |  |
| 1012017 | @2%s@ switched to slave mode @3%s@ |  |
| 1012018 | @2%s@ cannot send time frame |  |
| 1012019 | @2%s@ can successfully send time frame |  |
| 1012020 | @2%s@ sets the local time |  |
| 1012021 | LAN time synchronization with PC @2%s@ faulty |  |
| 1012022 | LAN time synchronization set on PC @2%s@ |  |
| 1012023 | LAN time synchronization with PC @2%s@ established |  |
| 1012024 | Configured device names of time synchronization do not match the PC installation |  |
| 1012025 | LAN - time cannot be accepted from connected WinCC server |  |
| 1012026 | Time jump noted - switched to permanent slave mode |  |
| 1012027 | Time jump noted - time synchronization permanently disabled |  |
| 1012028 | Time reception service not started |  |
| 1012029 | Time reception service running |  |
| 1012030 | Time synchronization disabled |  |

#### 1012200 - Alarms Redundancy

##### Meaning of the system events

The most important system alarms are listed below.

1012200 - Alarms Redundancy

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1012200 | Partner station has failed |  |
| 1012201 | Partner station restarted |  |
| 1012202 | Projects are not functionally identical |  |
| 1012203 | Log synchronization failed |  |
| 1012204 | Internal redundancy error |  |
| 1012205 | Connection to partner faulty |  |
| 1012206 | Connection to partner restored |  |
| 1012207 | Partner server - WinCC has not been started |  |
| 1012208 | Log synchronization starts |  |
| 1012209 | Log synchronization complete |  |
| 1012210 | Tag Logging being synchronized |  |
| 1012211 | Tag Logging synchronization complete |  |
| 1012212 | Alarm Logging being synchronized |  |
| 1012213 | Alarm Logging synchronization complete |  |
| 1012214 | User archive is being synchronized |  |
| 1012215 | User archive synchronization complete |  |
| 1012216 | Synchronization was interrupted |  |
| 1012217 | Partner server project not activated |  |
| 1012218 | Client was switched automatically |  |
| 1012219 | Client was switched manually |  |
| 1012220 | Synchronization not ready for all user archives |  |
| 1012221 | Synchronization ready for all user archives |  |
| 1012222 | Main connection faulty |  |
| 1012223 | Main connection operational |  |
| 1012224 | Backup connection faulty |  |
| 1012225 | Backup connection operational |  |
| 1012226 | Partner server project activated |  |
| 1012227 | Error: Partner computer is not a server |  |
| 1012228 | Log synchronization starts '@2%s@' |  |
| 1012229 | Log synchronization complete '@2%s@' |  |
| 1012240 | RedundancyControl error triggers switchover |  |
| 1012241 | RedundancyControl: Switchover to status |  |
| 1012242 | Delta download has been started |  |
| 1012243 | Delta download is complete |  |
| 1012244 | Overload during online synchronization of Alarm Logging |  |
| 1012245 | RedundancyControl: Loss of serial connection |  |
| 1012246 | RedundancyControl: Serial connection reestablished |  |
| 1012247 | OS server (standby) redundancy error |  |
| 1012248 | OS server (standby) redundancy reestablished |  |
| 1012250 | Possible inconsistency of the log databases |  |
| 1012251 | Internal error |  |
| 1012252 | Backup: Error while writing to backup path |  |
| 1012253 | Backup: Insufficient disk space on target drive |  |
| 1012254 | No connection to the WriteArchiveServer |  |
| 1012255 | No connection to Microsoft Message Queue |  |
| 1012256 | No connection to the WinCC project |  |
| 1012257 | No connection to the database |  |
| 1012258 | No connection to the text library |  |
| 1012259 | Error while creating the TagLogging data |  |
| 1012260 | Error while creating the AlarmLogging data |  |
| 1012261 | Notice: Backup is delayed until the partner server restarts. |  |
| 1012265 | Database verification failed |  |
| 1012301 | No access to SQL server (risk of data loss) |  |
| 1012348 | Insufficient free disk space on project drive |  |
| 1012349 | Loss of connection via network adapter (MAC) address |  |
| 1012350 | Connection reestablished via network adapter (MAC) address |  |
| 1012351 | RedundancyControl:   System blockage detected. Switch to Fault status. |  |
| 1012352 | RedundancyControl:   System blockage detected. Restart your computer as soon as possible. |  |
| 1012354 | [Computer name]:RedundancyControl:   Status changed to FAULT. However, server isolation is not activated. |  |
| 1012355 | [Computer name]:RedundancyControl:   Status changed to FAULT. However, server isolation is locked by @1%s@. Reason: @2%s@ |  |
| 1012356 | RedundancyControl: Status changed to FAULT =&gt; server is isolated |  |
| 1012357 | [Computer name]:RedundancyControl:   Status changed to FAULT. However, automatic restart is not activated. |  |
| 1012358 | [Computer name]:RedundancyControl:   Status changed to FAULT. However, automatic restart is locked. The network adapter is disconnected and DHCP is released. |  |
| 1012359 | [Computer name]:RedundancyControl:   Reboot of computer disabled by @1%s@. Reason: @2%s@ |  |
| 1012360 | [Computer name]:RedundancyControl:   Restart of the computer canceled. The last restart took place less than @1%s @ s ago. |  |
| 1012361 | [Computer name]:RedundancyControl: Restart of the computer canceled. After @1%s@ restarts, no more restarts are permitted for @2%s@ s. |  |
| 1012362 | [Computer name]:RedundancyControl:   Rebooting computer in @1%s@ s |  |
| 1012363 | [Computer name]:RedundancyControl:   ERROR status deferred until partner has reached stable status. |  |

#### 1012400 - Alarms WebNavigatorClient

##### Meaning of the system events

The most important system alarms are listed below.

1012400 - Alarms WebNavigatorClient

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1012400 | WebClient @1%s@ Connection established (User=@2%s@) |  |
| 1012401 | WebClient @1%s@ Connection terminated (User=@2%s@) |  |

#### 1012500 - Alarms Process Historian

##### Meaning of the system events

The most important system alarms are listed below.

1012500 - Alarms Process Historian

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1012500 | [Computer name]:Start recovery for Process Historian |  |
| 1012501 | [Computer name]:Recovery for Process Historian completed |  |
| 1012502 | [Computer name]:Communication with Process Historian not possible |  |
| 1012503 | [Computer name]:Communication with Process Historian faulty |  |
| 1012504 | [Computer name]:Communication with Process Historian restored |  |
| 1012505 | [Computer name]:Process Historian server offline since @1%s@ |  |
| 1012506 | [Computer name]:Buffer limit of channel @1%s@ exceeded |  |
| 1012507 | [Computer name]:Buffer limit of channel @1%s@ normal |  |
| 1012508 | [Computer name]:Less than @1%d@ GB of disk space available on data storage medium '@2%s@' for communication with the Process Historian. |  |
| 1012509 | [Computer name]:Communication with the Process Historian was terminated. Less than @1%d@ GB of disk space available on data storage medium '@2%s@'. |  |
| 1012510 | [Computer name]:Connection to the Process Historian could not be established (check configuration). |  |
| 1012600 | [Computer name]:@1%d@% of data storage capacity used |  |
| 1012601 | [Computer name]:System out of resources |  |
| 1012602 | [Computer name]:Redundancy failed |  |
| 1012603 | [Computer name]:Redundancy restored |  |
| 1012604 | [Computer name]:License volume exceeded Shutdown in @1%d@ days |  |
| 1012605 | [Computer name]:PH-Ready @1%s@ failed |  |
| 1012606 | [Computer name]:An automatic redundancy switchover of the Process Historian servers has taken place. |  |
| 1012607 | [Computer name]:Less than @1%d@ GB of disk space available for Process Historian database. |  |
| 1012608 | [Computer name]:Less than @1%d@ GB of disk space available for the "tempdb" database. |  |
| 1012609 | [Computer name]:Less than @1%d@ GB of disk space available for emergency restore operation. |  |
| 1012610 | [Computer name]:New backup for emergency restore operation failed. Insufficient memory. |  |
| 1012611 | [Computer name]:An unknown error occurred while creating a backup for the emergency restore operation. |  |
| 1012612 | [Computer name]:Memory path @1%s@ not accessible for emergency restore operation. |  |
| 1012613 | [Computer name]:The emergency threshold value for drive @1%s@ was reached. Process Historian is locked as a result. |  |
| 1012614 | [Computer name]:None of the prepared segments exists. Please check why this is. |  |
| 1012615 | [Computer name]:Not all prepared segments have been created. |  |

#### 1012700 - Alarms Redundancy self-diagnostics

##### Meaning of the system events

The most important system alarms are listed below.

1012700 - Alarms Redundancy self-diagnostics

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1012700 | [Computer name]: Value @7%s@ of device @10%s@ is invalid. |  |
| 1012701 | [Computer name]: Value @7%s@ of device @10%s@ has violated the error limit HIGH. |  |
| 1012702 | [Computer name]: Value @7%s@ of device @10%s@ has violated the error limit LOW. |  |
| 1012703 | [Computer name]: Value @7%s@ of device @10%s@ has violated the warning limit HIGH. |  |
| 1012704 | [Computer name]: Value @7%s@ of device @10%s@ has violated the warning limit LOW. |  |
| 1012705 | [Computer name]: Value @7%s@ of device @10%s@ no longer violates the error limit. |  |
| 1012706 | [Computer name]: Value @7%s@ of device @10%s@ is OK. |  |
| 1012707 | [Computer name]: Device @10%s@ causes @2%s@. |  |
| 1012708 | [Computer name]: Value @7%s@ of device @10%s@ is invalid. |  |

#### 1016000 - Alarms IndustrialDataBridge

##### Meaning of the system events

The most important system alarms are listed below.

1016000 - Alarms IndustrialDataBridge

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 1016000 | @1%s@ provider initialization failed for connection: @2%s@. |  |
| 1016001 | @1%s@ consumer initialization failed for connection: @2%s@. |  |
| 1016002 | @1%s@ provider data transmission failed for connection: @2%s@. |  |
| 1016003 | @1%s@ consumer data transmission failed for connection: @2%s@. |  |
| 1016004 | Provider initialization database failed for connection: @2%s@. |  |
| 1016005 | Consumer initialization database failed for connection: @2%s@. |  |
| 1016006 | Provider data transmission database failed for connection: @2%s@. |  |
| 1016007 | Consumer data transmission database failed for connection: @2%s@. |  |
| 1016008 | Provider initialization dynamic database failed for connection: @2%s@. |  |
| 1016009 | Consumer initialization dynamic database failed for connection: @2%s@. |  |
| 1016010 | Provider data transmission dynamic database failed for connection: @2%s@. |  |
| 1016011 | Consumer data transmission dynamic database failed for connection: @2%s@. |  |

#### 12508141 - Alarms

##### Meaning of the system events

The most important system alarms are listed below.

12508141 - Alarms

| Number | Effect/causes | Solution |
| --- | --- | --- |
| 12508141 | @10%s@: @7%s@ @102%s@ new=@3%g@ @8%s@ old=@2%g@ @8%s@ |  |

### Tag Bit Assignments (RT Professional)

This section contains information on the following topics:

- [Tags for Alarm Groups and Alarms (RT Professional)](#tags-for-alarm-groups-and-alarms-rt-professional)
- [Tags for Alarm Groups (RT Professional)](#tags-for-alarm-groups-rt-professional)

#### Tags for Alarm Groups and Alarms (RT Professional)

This section contains information on the following topics:

- [Bit assignment of status tag (RT Professional)](#bit-assignment-of-status-tag-rt-professional)
- [Bit assignment for acknowledgment tags (RT Professional)](#bit-assignment-for-acknowledgment-tags-rt-professional)

##### Bit assignment of status tag (RT Professional)

###### Introduction

In WinCC you can define a status tag for an alarm or an alarm group. The status tag for am alarm group represents the states of the alarms and child alarm groups it contains.

###### Description

The following states of an alarm or alarm group are stored in a status tag:

- Incoming/outgoing alarm (status bit)
- Alarm queued for acknowledgment / acknowledged (acknowledgment bit)

###### Data type of a status tag

The status tag is an internal or external WinCC tag. You can use the following data types for status tags:

- Unsigned 8-bit value

  The data type represents the states of up to four alarms.
- Unsigned 16-bit value

  The data type represents the states of up to eight alarms.
- Unsigned 32-bit value

  The data type represents the states of up to 16 alarms.

Each alarm or alarm group occupies 2 bits in the status tag.

> **Note**
>
> A status bit of a status tag can only be assigned to one alarm.

###### Acknowledgment bit of the status tag of an alarm

When an incoming alarm is received and is not acknowledged, the acknowledgment bit has status "1".

If the alarm was acknowledged, the acknowledgment bit status changes to "0".

| Alarm event | Acknowledgment bit |
| --- | --- |
| Incoming alarm was not acknowledged | 1 |
| Alarm acknowledged | 0 |

###### Acknowledgment bit of the status tag of an alarm group

When at least one incoming alarm is received and is not acknowledged, the acknowledgment bit status in an alarm group changes to "1".

If all the alarms for the alarm group were acknowledged, the acknowledgment bit is reset to "0".

###### Status bit for the status tags of an alarm or alarm group

If an incoming alarm or alarm group is received and has not yet gone, the acknowledgment bit has status "1". If the alarm has gone, the acknowledgment bit status changes to "0".

| Alarm event | Status bit |
| --- | --- |
| Incoming alarm or alarm group | 1 |
| Alarm gone | 0 |

> **Note**
>
> Alarms whose alarm class has the "Alarm without status" property cannot be displayed in a status tag.

###### Status tag of a locked alarm

If you lock an alarm in Runtime, the bits in the status tags will be reset or not set, regardless of the alarm status. The "locked" status of an alarm is not indicated in the status tag.

> **Note**
>
> To visualize the locked status of an alarm group, use the locked tag for the alarm group.

###### Status tag for chronological alarms

You can use a structure tag to represent the status of a chronological alarm. In the structure tag, the "EventState" element, for example, represents the status of a chronological alarm.

###### Position of the Status and Acknowledgment Bit

You can define the position of the status bit within a status tag. The acknowledgment bit must be a certain distance from this bit. The following definitions apply to the data type:

| Data type | Position of status bit | Distance | Position of acknowledgment bit |
| --- | --- | --- | --- |
| Unsigned 8-bit value | 0 - 3 | 4 | 4 - 7 |
| Unsigned 16-bit value | 0 - 7 | 8 | 8 - 15 |
| Unsigned 32-bit value | 0 - 15 | 16 | 16 - 31 |

###### Examples

**Status Tag of Data Type "32 Bit Unsigned"**

Status bit = Position 9

Distance = 16 positions

Acknowledgment bit = Position 25

![Examples](images/76062956939_DV_resource.Stream@PNG-en-US..png)

**Status Tag of Data Type "16 Bit Unsigned"**

Status bit = 6

Distance = 8 positions

Acknowledgment bit = Position 14

![Examples](images/76063691019_DV_resource.Stream@PNG-en-US..png)

**Status Tag of Data Type "8 Bit Unsigned"**

Status bit = 2

Distance = 4 positions

Acknowledgment bit = Position 6

![Examples](images/76063695499_DV_resource.Stream@PNG-en-US..png)

###### Configuring Function Lists for a Change in Value

You can configure a list of functions for the "Value change" event for the tag. You can hide any non-relevant bits of the tag to reduce the number of possible signal states for the tag. You can configure the hiding of the non-relevant bits using a C or VB script.

It is not necessary to hide the non-relevant bits if the following condition is fulfilled:

- You are using a separate status tag for each alarm.
- The non-relevant bits of these status tags always have the value "0".

---

**See also**

[Bit assignment for acknowledgment tags (RT Professional)](#bit-assignment-for-acknowledgment-tags-rt-professional)
  
[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)

##### Bit assignment for acknowledgment tags (RT Professional)

###### Introduction

In WinCC you can define an acknowledgment tag for an alarm or alarm group.

###### Description

Use the acknowledgment tag to:

- Acknowledge an alarm
- Acknowledge an alarm group

  The acknowledgment tag of an alarm group acknowledges all the alarms and alarm subgroups it contains.
- Displaying the acknowledgment status of an alarm group
- Linking the acknowledgment to other WinCC components

  You can use the acknowledgment tag to link the acknowledgment to other WinCC components.

If the operator acknowledges an alarm or alarm group in Runtime, then the associated acknowledgment bit will be set.

###### Using acknowledgment tags

You have the following options available for configuring acknowledgment tags:

- You can configure a separate acknowledgment tag for each alarm or alarm group.
- You can compile several alarms or alarm groups in an acknowledgment tag. The acknowledgment bit allows you to distinguish between alarms and alarm groups.

Each alarm occupies one bit in the acknowledgment tag.

###### Data Type of an acknowledgment tag

The structure of the acknowledgment tag is not specified. The data type depends on the number of alarms that you want to represent in the acknowledgment tag.

###### Resetting the Acknowledgment Bit for acknowledgment tags

You configure the setting or resetting of the acknowledgment bit in WinCC using a button or via the PLC.

> **Note**
>
> When you acknowledge an alarm group in Runtime, the acknowledgment bit does not indicate this acknowledgment in the alarm view.

- See also "Resetting the acknowledgment bit"
- See also "Tags of an alarm group"

---

**See also**

[Bit assignment of status tag (RT Professional)](#bit-assignment-of-status-tag-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)

#### Tags for Alarm Groups (RT Professional)

This section contains information on the following topics:

- [Bit assignment for lock tags (RT Professional)](#bit-assignment-for-lock-tags-rt-professional)
- [Bit assignment for display suppression tags (RT Professional)](#bit-assignment-for-display-suppression-tags-rt-professional)

##### Bit assignment for lock tags (RT Professional)

###### Introduction

In WinCC you can define a lock tag for an alarm group.

###### Description

The lock tag of an alarm group is used to evaluate the locked status of that alarm group. You can define a lock bit in the lock tag for this purpose.

###### Using the Lock Tag

You have the following options for configuring lock tags:

- You can configure a separate lock tag for each alarm group.
- You can compile several alarm groups in a lock tag. The lock bit allows you to distinguish between alarm groups.

When you lock an alarm group in Runtime, the associated lock bit is set in the configured tag.

###### Data Type of a Lock Tag

The structure of the lock tag is not specified. The data type depends on the number of alarms that you want to represent in the lock tag.

---

**See also**

[Bit assignment for display suppression tags (RT Professional)](#bit-assignment-for-display-suppression-tags-rt-professional)
  
[System functions for alarms (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#system-functions-for-alarms-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)

##### Bit assignment for display suppression tags  (RT Professional)

###### Introduction

In WinCC you can define a display suppression tag for a custom alarm group. The display suppression tag saves the potential plant states. Only one plant state can be active at one time. The display suppression tag is therefore set by only one bit.

###### Description

In the display suppression mask, you can specify which alarm of an alarm group is to be suppressed for specific plant states in Runtime.

###### Data type of the display suppression tag

The display suppression tag is an external WinCC tag that stores the plant state. You can use the following data types for display suppression tags:

- Unsigned 8-bit value
- Unsigned 16-bit value
- Unsigned 32-bit value

###### Display suppression mask

In the Inspector window of an alarm, you can use the display suppression mask to define the plant states at which the alarm is not shown. The project engineer sets the bits that define specific plant states. A plant can have a maximum of 32 states.

You enter the selected plant states as hexadecimal value in the Inspector window of the alarm under "Display suppression &gt; Mask".

The display suppression tag saves the plant state. When a plant state listed in the mask occurs, the alarm is no longer displayed. To view the alarms currently hidden due to a plant state, you can switch the alarm view in Runtime to "Alarms with display suppression".

###### Example

Five examples for the display suppression mask are offered below:

- Display suppression mask 0x0. The alarm is displayed.

  ![Example](images/9802750347_DV_resource.Stream@PNG-de-DE.png)
- Display suppression mask 0x1. If the "1" bit is set in the display suppression tag, the alarm is not displayed.

  ![Example](images/9802753931_DV_resource.Stream@PNG-de-DE.png)
- Display suppression mask 0xD. If the "1", "3" or "4" bit is set in the display suppression tag, the alarm is not displayed.

  ![Example](images/9805957515_DV_resource.Stream@PNG-de-DE.png)
- Display suppression mask 0x80000008. If the "4" or "32" bit is set in the display suppression tag, the alarm is not displayed.

  ![Example](images/9805961099_DV_resource.Stream@PNG-de-DE.png)
- Display suppression mask 0xFFFFFFFF. If any bit is set in the display suppression tags, the alarm is not displayed.

  ![Example](images/9805964683_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Bit assignment for lock tags (RT Professional)](#bit-assignment-for-lock-tags-rt-professional)
  
[Tags of an alarm group (RT Professional)](#tags-of-an-alarm-group-rt-professional)
