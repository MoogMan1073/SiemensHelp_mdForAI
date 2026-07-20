---
title: "Configuring alarms (RT Unified)"
package: AlarmsWCCUenUS
topics: 86
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring alarms (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Configuring alarms (RT Unified)](#configuring-alarms-rt-unified-1)
- [Exporting or importing alarms (RT Unified)](#exporting-or-importing-alarms-rt-unified)
- [Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified)
- [Logging alarms (RT Unified)](#logging-alarms-rt-unified)
- [Displaying and using alarms (RT Unified)](#displaying-and-using-alarms-rt-unified)
- [Display security events (RT Unified)](#display-security-events-rt-unified)
- [Sending complete alarms from the controller to the HMI device (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-rt-unified)
- [Reference (RT Unified)](#reference-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Alarm system (RT Unified)](#alarm-system-rt-unified)
- [Alarms (RT Unified)](#alarms-rt-unified)
- [Alarm states (RT Unified)](#alarm-states-rt-unified)
- [Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
- [Alarm classes (RT Unified)](#alarm-classes-rt-unified)
- [Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified)
- [Components and properties of alarms (RT Unified)](#components-and-properties-of-alarms-rt-unified)

### Alarm system (RT Unified)

#### Introduction

Alarms indicate events, operating modes, or faults that occur or prevail in your plant. Alarms can be used, for example, for diagnostic purposes during troubleshooting and can help you locate the cause of the fault immediately. You can adjust your processes through targeted intervention so that compliant products continue to be produced despite the fault, or the process is stabilized and the fault only causes a minimal loss of production.

WinCC has a whole range of technical tools for implementing an alarm system. You can use these tools to set up an alarm system that meets all requirements under currently applicable national and international standards and guidelines.

Events from the monitoring function in WinCC are displayed in the form of alarms via the alarm system, acknowledged by the operator, and logged if necessary. For this purpose, alarms must be configured, which are divided into alarm classes.

#### Alarm system

The alarm system distinguishes between the following alarms:

- User-defined alarms:

  - Analog alarms: Show limit violations (value changes), are used for monitoring the plant.
  - Discrete alarms: Show status changes, are used for monitoring the plant.
  - User-defined PLC alarms: are configured in STEP 7, show status values of the controller, are used to monitor the plant.
- System-defined alarms:

  - System alarms: belong to the HMI device and are used to monitor it.
  - System-defined PLC alarms: consist of system diagnostic alarms and system errors and are used to monitor the controller.

![Alarm system](images/147472166795_DV_resource.Stream@PNG-en-US.png)

The detected alarm events are displayed on the HMI device.

> **Note**
>
> Observe the following restrictions for PLC alarms:
>
> - WinCC only supports PLC alarms of a SIMATIC S7-1500 controller.
> - WinCC only supports PLC alarms that are automatically updated by the central alarm management in the PLC.

| Symbol | Meaning |
| --- | --- |
| ![Alarm system](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| - When configuring an alarm system, you must take into account the limits of the capabilities of the subsequent operators. - An alarm system must be designed to use and allow for characteristic aspects of human perception. - Important alarms must be highlighted to be noticed quickly. The display of important information should be redundant to make it easier to see. - Supplementary information on individual alarms ensures rapid fault localization and troubleshooting. - Information should if possible be directed at more than one sense (for example, visible and sound signals). Only an alarm system that meets these criteria will help the operator to monitor and control the plant. |  |

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Alarms (RT Unified)](#alarms-rt-unified)
  
[Alarm states (RT Unified)](#alarm-states-rt-unified)
  
[Alarm classes (RT Unified)](#alarm-classes-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified)
  
[Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
  
[Components and properties of alarms (RT Unified)](#components-and-properties-of-alarms-rt-unified)
  
[Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified-1)
  
[Editing system alarms (RT Unified)](#editing-system-alarms-rt-unified)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)

### Alarms (RT Unified)

This section contains information on the following topics:

- [User-defined alarms: (RT Unified)](#user-defined-alarms-rt-unified)
- [System-defined alarms (RT Unified)](#system-defined-alarms-rt-unified)

#### User-defined alarms: (RT Unified)

This section contains information on the following topics:

- [Analog alarms: (RT Unified)](#analog-alarms-rt-unified)
- [Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)
- [User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)

##### Analog alarms: (RT Unified)

###### Description

Analog alarms display limit violations. You have defined in advance a limit value for the trigger tag and the trigger mode. An analog alarm is triggered depending on which mode you have defined, for example, when the value is higher than, lower than, or the same as the defined value.

###### Example

The speed of a motor must not be too high or too low. You can configure the appropriate analog alarm to monitor the speed of the motor. If the high limit or low limit for the speed of the motor is violated, an alarm is generated on the HMI device containing, for example, the following alarm text: "Motor speed is too low".

---

**See also**

[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
  
[Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)
  
[User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)
  
[System alarms (RT Unified)](#system-alarms-rt-unified)
  
[System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)
  
[Alarm system (RT Unified)](#alarm-system-rt-unified)

##### Discrete alarms (RT Unified)

###### Description

Discrete alarms indicate status changes in a plant. A discrete alarm is triggered when the value of a specific bit of an internal or external tag changes.

###### Example

Imagine that the state of a valve is to be monitored during operation. The two possible valve states are "opened" and "closed". In this case, a discrete alarm is configured for each valve state. If the status of the valve changes, a discrete alarm is output, containing for example the following alarm text: "Valve closed".

---

**See also**

[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
  
[Analog alarms: (RT Unified)](#analog-alarms-rt-unified)
  
[User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)
  
[System alarms (RT Unified)](#system-alarms-rt-unified)
  
[System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)
  
[Alarm system (RT Unified)](#alarm-system-rt-unified)

##### User-defined PLC alarms (RT Unified)

###### Example of an alarm

"The temperature in Tank 2 is too high."

###### Description

The configuration engineer creates a custom PLC alarm, e.g. a program alarm, in STEP 7. The PLC status values, such as time stamp and process values, are mapped in the PLC alarm. If PLC alarms are configured in STEP 7, accept them into the integrated WinCC operation as soon as a connection is established to the PLC. The PLC alarm of an alarm class is assigned in STEP 7. You import this alarm class with the PLC alarm as a common alarm class.

> **Note**
>
> **Automatic update of new or modified PLC alarms on the HMI device**
>
> If PLC alarms are configured in STEP 7 and an HMI connection to a SIMATIC S7-1500 controller (firmware version 2.0 or higher) is established, PLC alarms are sent to the HMI device. After changes to the PLC alarms, the HMI device configuration no longer has to be transferred. The prerequisite is that the "Central alarm management in the PLC" option is enabled in the properties of the controller. In addition, the option "Automatic update" must be enabled in the runtime settings of the HMI device under "Alarms > Controller alarms".

> **Note**
>
> If the connection between HMI device and controller is interrupted, only the last occurring controller alarm can be sent and displayed after restarting the Runtime software. When the connection is re-established, all controller alarms are transmitted correctly again.

> **Note**
>
> WinCC only supports PLC alarms of a SIMATIC S7-1500 controller. In addition, WinCC only supports PLC alarms that are automatically updated by the central alarm management in the PLC.

###### PLC alarms for HMI devices

If a PLC is connected to one or more HMI devices, the configuration engineer assigns display classes to the PLC alarms in STEP 7. The display classes determine the allocation to the HMI device. You activate the display classes that are to be available for each HMI device. In this case, only the PLC alarms from this display class will be displayed on the HMI device. Up to 17 display classes are possible.

---

**See also**

[Filtering PLCs alarm using display classes (RT Unified)](#filtering-plcs-alarm-using-display-classes-rt-unified)
  
[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)
  
[Configuring automatic updates of PLC alarms on the HMI device (RT Unified)](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified)
  
[Analog alarms: (RT Unified)](#analog-alarms-rt-unified)
  
[Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)
  
[System alarms (RT Unified)](#system-alarms-rt-unified)
  
[System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)
  
[Alarm system (RT Unified)](#alarm-system-rt-unified)

#### System-defined alarms (RT Unified)

This section contains information on the following topics:

- [System alarms (RT Unified)](#system-alarms-rt-unified)
- [System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)

##### System alarms (RT Unified)

###### Example of an alarm

"Memory is full!"

###### Description

A system alarm indicates the status of the system and communication errors between the HMI device and the system. System alarms are output in runtime in the configured alarm control. System alarms are output in the language currently set on your HMI device.

The time format (AM/PM or 24-hour format) is based on the selected language. If there is no translation of the alarm texts in this language, English is selected as the substitute language and the corresponding time format is displayed.

---

**See also**

[Editing system alarms (RT Unified)](#editing-system-alarms-rt-unified)
  
[Analog alarms: (RT Unified)](#analog-alarms-rt-unified)
  
[Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)
  
[User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)
  
[System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)
  
[Alarm system (RT Unified)](#alarm-system-rt-unified)

##### System-defined PLC alarms (RT Unified)

###### Example of an alarm

"CPU maintenance required"

###### Description

System-defined PLC alarms are installed with STEP 7 and are only available if WinCC is operated in the STEP 7 environment.

System-defined PLC alarms are used to monitor states and events of a PLC. System-defined PLC alarms consist of system diagnostic alarms and system errors (RSE).

> **Note**
>
> **Automatic update of system diagnostic alarms on the HMI device**
>
> If an HMI connection to a SIMATIC S7-1500 controller (firmware version 2.0 or higher) is established, system diagnostic alarms are sent to the HMI device and automatically updated. The prerequisite is that the "Central alarm management in the PLC" option is enabled in the properties of the controller. In addition, the options "Automatic update" and "System diagnostics" must be enabled in the runtime settings of the HMI device under "Alarms > Controller alarms".

> **Note**
>
> Note the following restrictions:
>
> - WinCC only supports system diagnostics alarms of a SIMATIC S7-1500 controller.
> - WinCC only supports system diagnostic alarms that are automatically updated by the central alarm management in the PLC.

---

**See also**

[Configuring the display of system diagnostics alarms (RT Unified)](#configuring-the-display-of-system-diagnostics-alarms-rt-unified)
  
[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)
  
[Configuring automatic updates of PLC alarms on the HMI device (RT Unified)](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified)
  
[Analog alarms: (RT Unified)](#analog-alarms-rt-unified)
  
[Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)
  
[User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)
  
[System alarms (RT Unified)](#system-alarms-rt-unified)
  
[Alarm system (RT Unified)](#alarm-system-rt-unified)

### Alarm states (RT Unified)

#### Description

Every alarm has an alarm state. The alarm states are made up of the following events:

- **Active**

  The condition for triggering an alarm is fulfilled. The alarm is displayed, e.g. "Boiler pressure too high".
- **Inactive**

  The condition for triggering an alarm is no longer fulfilled. The alarm is no longer displayed because the boiler was vented.
- **Acknowledged**

  The operator has acknowledged the alarm.

> **Note**
>
> Alarm states are visible to the operator in runtime through status texts. Status texts can be configured in the runtime settings.

#### Alarms not requiring acknowledgment

The following table shows the alarm states for alarms not requiring acknowledgment:

| Icon | Alarm state | Status text | Description |
| --- | --- | --- | --- |
| ![Alarms not requiring acknowledgment](images/113621246475_DV_resource.Stream@PNG-de-DE.png) | Active | Incoming | The condition of an alarm is fulfilled.  The alarm does not need to be acknowledged. |
| ![Alarms not requiring acknowledgment](images/113621250187_DV_resource.Stream@PNG-de-DE.png) | Inactive | Normal | The condition of an alarm is no longer fulfilled.  The alarm is no longer pending. |

#### Alarms requiring acknowledgment

The following table shows the alarm states for alarms requiring acknowledgment:

| Icon | Alarm state | Status text | Description |
| --- | --- | --- | --- |
| ![Alarms requiring acknowledgment](images/113621246475_DV_resource.Stream@PNG-de-DE.png) | Active | Incoming | The condition of an alarm is fulfilled. |
| ![Alarms requiring acknowledgment](images/113621250187_DV_resource.Stream@PNG-de-DE.png) | Active/inactive | Incoming/Outgoing | The condition of an alarm is no longer fulfilled.   The user has not acknowledged the alarm. |
| ![Alarms requiring acknowledgment](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Active/inactive/acknowledged | Normal | The condition of an alarm is no longer fulfilled.   The user has acknowledged the alarm after this time. |
| ![Alarms requiring acknowledgment](images/113622144139_DV_resource.Stream@PNG-de-DE.png) | Active/acknowledged | Incoming/acknowledged | The condition of an alarm is fulfilled.   The user has acknowledged the alarm. |
| ![Alarms requiring acknowledgment](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Active/acknowledged/inactive | Normal | The condition of an alarm is no longer fulfilled.   The user acknowledged the alarm while the condition was still fulfilled. |

> **Note**
>
> The display texts of the alarm states are different depending on the language and configuration.

#### Alarms requiring acknowledgment and confirmation

The following table shows the alarm states for alarms requiring acknowledgment and confirmation:

| Icon | Alarm state | Status text | Description |
| --- | --- | --- | --- |
| ![Alarms requiring acknowledgment and confirmation](images/113621246475_DV_resource.Stream@PNG-de-DE.png) | Active | Incoming | The condition of an alarm is fulfilled. |
| ![Alarms requiring acknowledgment and confirmation](images/113621250187_DV_resource.Stream@PNG-de-DE.png) | Active/inactive | Incoming/outgoing | The condition of an alarm is no longer fulfilled.   The user has not acknowledged the alarm. |
| ![Alarms requiring acknowledgment and confirmation](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Active/inactive/acknowledged | Incoming/outgoing/acknowledged | The condition of an alarm is no longer fulfilled.   The user acknowledged the alarm after this time. |
| ![Alarms requiring acknowledgment and confirmation](images/113622144139_DV_resource.Stream@PNG-de-DE.png) | Active/acknowledged | Incoming/acknowledged | The condition of an alarm is fulfilled.   The user has acknowledged the alarm. |
| ![Alarms requiring acknowledgment and confirmation](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Active/acknowledged/inactive | Incoming/acknowledged/outgoing | The condition of an alarm is no longer fulfilled.   The user acknowledged the alarm while the condition was still fulfilled. |
| ![Alarms requiring acknowledgment and confirmation](images/113622144139_DV_resource.Stream@PNG-de-DE.png) | Normal | Normal | The condition of an alarm is fulfilled.  The user has acknowledged and confirmed the alarm. |

#### Disabled alarms

You can disable an alarm to prevent a nuisance alarm from impairing the effectiveness of your system, for example.

- Disabled: The alarm was disabled (locked). The alarm transitions to its final state without any further state transitions.
- Not disabled: The alarm is activated (enabled). The alarm is visible again in its last state.

#### Shelved alarms

The display of specific alarms is shelved (suppressed), for example in order not to overload the plant operator with information.

- Manually shelved: The alarm was manually shelved by the operator.
- Shelved due to design: The alarm was automatically shelved due to a condition and is automatically hidden in runtime.

---

**See also**

[Alarm system (RT Unified)](#alarm-system-rt-unified)
  
[Alarm classes (RT Unified)](#alarm-classes-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified)
  
[Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
  
[Components and properties of alarms (RT Unified)](#components-and-properties-of-alarms-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Acknowledgment model (RT Unified)

#### Overview

The acknowledgment model and the state machine for predefined alarm classes have already been set. You can only define the acknowledgment model and the state machine for user-defined alarm classes. All alarms included in this alarm class are then acknowledged according to this acknowledgment model and the state machine.

The following state machines are available for HMI alarm classes:

- Alarm with simple acknowledgment

  This alarm requires acknowledgment as soon as the event that triggers the alarm has occurred. The alarm is pending until it is acknowledged and outgoing.

  The following predefined alarm classes use this state machine: "SystemAlarm", "SystemWarning", "Critical", "Warning", "OperatorInputRequest", "Alarm", "Acknowledgement"
- Alarm with optional simple acknowledgment

  This alarm does not require acknowledgment as soon as the event that triggers the alarm occurs. The alarm is pending until the condition that triggered the alarm is no longer fulfilled.
- Alarm with acknowledgment and confirmation

  The alarm requires acknowledgment as soon as the event that triggers the alarm occurs, or when the alarm has been reset. In addition, the alarm requires confirmation when the event that triggers the alarm is no longer pending. The alarm is pending until it is acknowledged and confirmed.

  The following predefined alarm classes use this state machine: "AlarmWithReset", "CriticalWithReset", "WarningWithReset".
- Alarm without acknowledgment

  This alarm comes and goes without having to be acknowledged.

  The following predefined alarm classes use this state machine: "SystemNotification", "Notification", "No Acknowledgement".
- Alarm without inactive state with acknowledgment

  This alarm requires acknowledgment as soon as the event that triggers the alarm has occurred. The alarm is pending until it is acknowledged.

  The following predefined alarm classes use this state machine: "SystemAlarmWithoutClearEvent", "SystemWarningWithoutClearEvent".
- Alarm without inactive state without acknowledgment

  This alarm is only displayed in the "Show logged alarms" and "Show and update logged alarms" views.

  The following predefined alarm classes use this state machine: "Information", "Systeminformation", "OperatorInputInformation".
- Alarm without state  
  This alarm only has the temporary status "Incoming" and can be seen in the log.

The following state machines are available for HMI alarm classes that are associated with common alarm classes:

- Alarm with simple acknowledgment
- Alarm without acknowledgment

#### Acknowledging and confirming alarms

- Group acknowledgment of alarms in the alarm control

  The alarm control has an "Acknowledge visible alarms" button. This button triggers the acknowledgment of all alarms pending in the alarm control that are visible and require acknowledgment.
- Single acknowledgment of alarms in the alarm control

  The alarm control has a "Single acknowledgment" button. This button triggers the acknowledgment of single alarms selected in the alarm control.
- Single confirm of alarms with acknowledgment and confirmation in the alarm control

  The alarm control has a "Single confirm" button. The alarm with the state machine "Alarm with acknowledgment and confirmation" is confirmed individually via this button after it was previously acknowledged via group acknowledgment or single acknowledgment and was outgoing.

> **Note**
>
> If the "Alarms - show current" button is pressed, the most recent alarm is always shown first. Group acknowledgment is only carried out for visible alarms.

---

**See also**

[Alarm system (RT Unified)](#alarm-system-rt-unified)
  
[Configuring alarm acknowledgment (RT Unified)](#configuring-alarm-acknowledgment-rt-unified)
  
[Components and properties of alarms (RT Unified)](#components-and-properties-of-alarms-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified)
  
[Alarm states (RT Unified)](#alarm-states-rt-unified)
  
[Alarm classes (RT Unified)](#alarm-classes-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Alarm classes (RT Unified)

#### Introduction

Many alarms of varying importance occur in a plant. You can assign your project alarms to alarm classes to clearly show the operator which alarms are the most important.

#### Description

Every alarm must be assigned to an alarm class when you create new alarms. The alarm class defines the appearance and the acknowledgment model of the alarm (simple acknowledgment, acknowledgment and confirmation, no acknowledgment).

A new alarm class with mandatory acknowledgment is generated in WinCC. For each device, predefined alarm classes are created by default.

#### Examples of how to use alarm classes

- The alarm class of the "Fan 1 speed in upper tolerance range" alarm is "Warning". The alarm is displayed with a yellow background. The alarm must be acknowledged.
- The "Speed of fan 2 has exceeded upper warning range" alarm is assigned to the "Alarm" alarm class. The alarm is displayed with a red background and flashes at high frequency in runtime. The alarm is displayed until the alarm is outgoing and the operator has acknowledged the alarm.

#### Using alarm classes

Use the following alarm classes to define the state machines and appearance of alarms for your project:

- Predefined alarm classes

  You cannot delete predefined alarm classes and can only edit them to a limited extent. Predefined alarm classes are created under "HMI alarms > Alarm classes".
- User-defined alarm classes

  You can create new alarm classes under "HMI alarms > Alarm classes" and configure the desired display of alarms and an acknowledgment model for the alarms of this alarm class. The possible number of user-defined alarm classes depends on which Runtime is used in your project.
- Common alarm classes

  Common alarm classes are displayed under "Common data > Alarm classes" in the project tree and can be used for the alarms of an HMI device. Common alarm classes are used in STEP 7 for PLC alarms. You can create additional common alarm classes in WinCC. Common alarm classes are divided into predefined and user-defined common alarm classes. The predefined common alarm classes are "Acknowledgement" (for alarms with acknowledgment) and "No Acknowledgement" (for alarms without acknowledgment).

For each alarm class (including predefined alarm classes), you can configure the text color, background color and flashing for the alarm states "Incoming", "Incoming/outgoing", "Incoming/acknowledged", and "Incoming/outgoing/acknowledged":

![Using alarm classes](images/102483525259_DV_resource.Stream@PNG-en-US.png)

#### Predefined alarm classes

The following predefined alarm classes are available under "Alarm classes" in the "HMI alarms" editor.

System alarms:

- "SystemInformation"

  Alarms of this alarm class have no "Outgoing" state and do not require acknowledgment. This alarm class is only used for logging.
- "SystemNotification"

  Alarms of this alarm class do not require acknowledgment.
- "SystemWarning"

  Alarms of this alarm class must be acknowledged.
- "SystemWarningWithoutClearEvent"

  Alarms of this alarm class have no "Outgoing" state and must be acknowledged.
- "SystemAlarm"

  Alarms of this alarm class must be acknowledged.
- "SystemAlarmWithoutClearEvent"

  Alarms of this alarm class have no "Outgoing" state and must be acknowledged.

Default alarms:

- "Acknowledgement"

  Alarms of this alarm class must be acknowledged. The "Acknowledgement" alarm class is linked to the predefined common alarm class "Acknowledgement".
- "No Acknowledgement"

  Alarms of this alarm class do not require acknowledgment. The "No Acknowledgement" alarm class is linked to the predefined common alarm class "No Acknowledgement".
- "Information"

  Alarms of this alarm class have no "Outgoing" state and do not require acknowledgment. This alarm class is only used for logging.
- "OperatorInputInformation"

  Alarms of this alarm class have no "Outgoing" state and do not require acknowledgment. The "OperatorInputInformation" alarm class is designed to show the reports that are relevant for an audit. This alarm class is only used for logging.
- "Notification"

  Alarms of this alarm class do not require acknowledgment. The "Notification" alarm class is designed to show irregular states and routines in the process.
- "OperatorInputRequest"

  Alarms of this alarm class must be acknowledged.
- "Warning"

  Alarms of this alarm class must be acknowledged.
- "WarningWithReset"

  Alarms of this alarm class must be acknowledged. This alarm class must also be reset. On resetting, the disabled alarm is enabled.
- "Alarm"

  Alarms of this alarm class must be acknowledged. The "Alarm" alarm class is designed to show critical or dangerous states or limit violations in the process.
- "AlarmWithReset"

  Alarms of this alarm class must be acknowledged. This alarm class must also be reset. On resetting, the disabled alarm is enabled.
- "Critical"

  Alarms of this alarm class must be acknowledged. The "Critical" alarm class is designed to show critical faults in the plant, for example, "Motor temperature too high". This alarm is recorded in the log with its alarm states.
- "CriticalWithReset"

  Alarms of this alarm class must be acknowledged. This alarm class must also be reset. On resetting, the disabled alarm is enabled. The "CriticalWithReset" alarm class is designed to show critical faults in the plant, for example, "Motor temperature too high".

> **Note**
>
> The alarm classes whose names contain "System" are designed to show the states of the device and the controllers, for example, to provide information on operating errors or malfunctions in communication.

> **Note**
>
> The predefined alarm classes are write-protected and cannot be deleted. You can, however, change the preset background and foreground colors and font colors if necessary. If required, you can also change the name of the predefined alarm classes "Acknowledgement" and "No Acknowledgement". The names of the linked predefined common alarm classes "Acknowledgement" and "No Acknowledgement" are not changed. You cannot change the name of the linked predefined common alarm classes, not even under "Common data > Alarm classes". Common alarm classes are automatically added for the non-integrated mode.

#### User-defined alarm classes

The properties of this alarm class are defined during configuration. You can assign a name, a state machine, a priority and, if necessary, a log to the alarm class. You can also define the display of the user-defined alarm using text and background colors.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Creating alarm classes (RT Unified)](#creating-alarm-classes-rt-unified)
  
[Use common alarm classes (RT Unified)](#use-common-alarm-classes-rt-unified)
  
[Alarm system (RT Unified)](#alarm-system-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified)
  
[Alarm states (RT Unified)](#alarm-states-rt-unified)
  
[Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
  
[Components and properties of alarms (RT Unified)](#components-and-properties-of-alarms-rt-unified)

### Acknowledging alarms (RT Unified)

#### Introduction

To ensure that an alarm has been registered by the operator of a plant, configure this alarm so that it is displayed until the operator has acknowledged it. Alarms that indicate critical or hazardous states in the process must be acknowledgeable.

Acknowledging an alarm is an event that is logged. Acknowledging an alarm in the "Incoming" state changes the alarm state of an alarm from "Incoming" to "Acknowledged". By acknowledging an alarm, the operator confirms that the state that triggered the alarm has been processed.

#### Acknowledging an alarm

The operator acknowledges an alarm in runtime via the alarm control buttons.

---

**See also**

[Alarm system (RT Unified)](#alarm-system-rt-unified)
  
[Configuring alarm acknowledgment (RT Unified)](#configuring-alarm-acknowledgment-rt-unified)
  
[Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
  
[Alarm classes (RT Unified)](#alarm-classes-rt-unified)
  
[Alarm states (RT Unified)](#alarm-states-rt-unified)
  
[Components and properties of alarms (RT Unified)](#components-and-properties-of-alarms-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Components and properties of alarms (RT Unified)

#### Overview

The following table shows the basic components of alarms that you can configure in WinCC:

| Alarm class | Alarm number | Time | Date | State machine | Alarm text | Info text | Trigger tag | Limit value |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Warning | 1 | 11:09:14 | 06.08.2017 | Alarm with simple acknowledgment | Maximum speed reached | This alarm is... | speed_1 | 27 |

#### Alarm class

The alarm class of an alarm determines whether the alarm has to be acknowledged.

The alarm class defines the following for an alarm:

- State machine/acknowledgment model
- Appearance in runtime (e.g. color)
- Log in which an alarm is logged
- Priority

#### Alarm number

An alarm is identified by an alarm number (ID). The alarm number is assigned by the system for internally managing an alarm. You can change the alarm number to a sequential alarm number, if necessary, to identify alarms associated with your project.

An alarm number may only be used once on a device.

> **Note**
>
> Discrete alarms and analog alarms can be given an identical alarm number by the system. The alarm number can be customized on request.

> **Note**
>
> When customizing alarm numbers, ensure that they are unique within the project.

The alarm number of a system alarm has a higher priority than the user-defined alarm. If you use the alarm number of a system alarm for a user-defined alarm, change the alarm number of the user-defined alarm.

#### Time and date

Each alarm shows in a time stamp the time and date when the alarm was triggered.

#### State machine

An alarm has the state machine or the acknowledgment model of the alarm class.

The state machine is the way an alarm is displayed in various states and processed by the system.

#### Alarm states

An alarm always has a specific alarm state in runtime. Based on the alarm states, the operator can analyze the course of the process.

#### Alarm text

The alarm text describes the cause of the alarm.

The alarm text can contain output fields for current values. The values you can insert depend on the runtime in use. The value is retained at the time at which the alarm status changes.

#### Info text

If required, you can configure a separate info text for each alarm, which the operator can then display in runtime.

#### Trigger tag

Each alarm has a tag assigned as a trigger. The alarm is output when this trigger tag meets the specified condition, e.g. when it changes state or exceeds a limit value.

#### Limit value

Analog alarms display limit violations. Depending on the configuration, WinCC outputs the analog alarm as soon as the trigger tag exceeds or undershoots the configured limit value.

#### Computer

Operator input alarms have a "Computer" column in the alarm summary. The computer name is displayed there for local alarms, and the IP address for alarms from the web client.

#### Users

The user acknowledges the alarm. If an empty user name is passed to an alarm, it does not represent a user name.

For alarms triggered by a variable, no user name is shown in the alarm display.

#### Duration

The amount of time, in nanoseconds, between when the alarm is triggered and its last status change.

---

**See also**

[Alarm system (RT Unified)](#alarm-system-rt-unified)
  
[Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
  
[Alarm states (RT Unified)](#alarm-states-rt-unified)
  
[Alarm classes (RT Unified)](#alarm-classes-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

## Configuring alarms (RT Unified)

This section contains information on the following topics:

- [Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
- [Creating alarm classes (RT Unified)](#creating-alarm-classes-rt-unified)
- [Use common alarm classes (RT Unified)](#use-common-alarm-classes-rt-unified)
- [Configuring the status texts of alarms (RT Unified)](#configuring-the-status-texts-of-alarms-rt-unified)
- [Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified)
- [Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified)
- [Integrating OPC UA server alarm instances (RT Unified)](#integrating-opc-ua-server-alarm-instances-rt-unified)
- [Configuring the alarm texts (RT Unified)](#configuring-the-alarm-texts-rt-unified)
- [Configuring info texts (RT Unified)](#configuring-info-texts-rt-unified)
- [Outputting parameters in a discrete or analog alarm (RT Unified)](#outputting-parameters-in-a-discrete-or-analog-alarm-rt-unified)
- [Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
- [Configuring multilingual alarm texts (RT Unified)](#configuring-multilingual-alarm-texts-rt-unified)
- [Editing system alarms (RT Unified)](#editing-system-alarms-rt-unified)
- [Filtering PLCs alarm using display classes (RT Unified)](#filtering-plcs-alarm-using-display-classes-rt-unified)
- [Configuring alarm acknowledgment (RT Unified)](#configuring-alarm-acknowledgment-rt-unified)

### Workflow for configuring alarms (RT Unified)

#### Work steps for configuring alarms

Follow these steps to configure alarms:

1. Configure alarm classes  
   In the "HMI alarms" editor, adapt the predefined alarm classes or configure your own alarm classes. Use the alarm class to define the state machine of an alarm and the display of the alarm in runtime.
2. Create trigger tags  
   Create trigger tags in the "HMI tags" editor and configure the trigger bit for discrete alarms or the range limits for analog alarms.
3. Configure alarms  
   Create user-defined alarms in the "HMI alarms" editor and assign the alarm classes and the tags to be monitored.  
   Under "Runtime settings > Alarms", adapt the status texts or activate the use of PLC alarms.
4. Configure the alarm display  
   Use the "Alarm control" object in the "Screens" editor to configure an alarm control.
5. Log alarms  
   In the "Logs" editor, create an alarm log and assign the log to an alarm class in the "HMI alarms" editor.

![Work steps for configuring alarms](images/104778990347_DV_resource.Stream@PNG-en-US.png)

#### Additional configuration tasks

Depending on the requirements of your project, additional steps may be necessary to configure alarms:

- Adapt status texts  
  You can specify status texts under "Runtime settings > Alarms".
- Editing system alarms

  You can edit system alarms in the "HMI alarms" editor or under "Languages & Resources > Project texts". In the "Category" column, you can tell by the "HMI system message" label that this is a system alarm.
- Activate PLC alarms

  For integrated operation of a project in STEP 7, specify the PLC alarms to be displayed on your HMI device in the alarm settings.

  > **Note**
  >
  > WinCC only supports PLC alarms of a SIMATIC S7-1500 controller. In addition, WinCC only supports PLC alarms that are automatically updated by the central alarm management in the PLC.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Creating alarm classes (RT Unified)](#creating-alarm-classes-rt-unified)
  
[Use common alarm classes (RT Unified)](#use-common-alarm-classes-rt-unified)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
  
[Configuring multilingual alarm texts (RT Unified)](#configuring-multilingual-alarm-texts-rt-unified)
  
[Editing system alarms (RT Unified)](#editing-system-alarms-rt-unified)
  
[Configuring alarm acknowledgment (RT Unified)](#configuring-alarm-acknowledgment-rt-unified)
  
[Filtering PLCs alarm using display classes (RT Unified)](#filtering-plcs-alarm-using-display-classes-rt-unified)
  
[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)
  
[Configuring automatic updates of PLC alarms on the HMI device (RT Unified)](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified)
  
[Configuring the display of system diagnostics alarms (RT Unified)](#configuring-the-display-of-system-diagnostics-alarms-rt-unified)

### Creating alarm classes (RT Unified)

#### Introduction

You can create alarm classes to define the acknowledgment type and the alarm display of an alarm in Runtime. Individual alarms are assigned to the alarm classes.

You can create alarm classes in the "Alarm classes" tab of the "HMI alarms" editor. Some alarm classes are already created for every project by default. You can create additional custom alarm classes as required. In addition, the alarm class specifies whether and how the operator has to acknowledge alarms of this alarm class.

The system alarm classes are write-protected and cannot be deleted. You can, however, change the preset background and foreground colors and font colors if necessary. All system alarm classes have the word "System" in their name and are to be used for system-defined alarms.

> **Note**
>
> Alarm colors are editable depending on the state machine. Some colors are not editable for certain state machines.

#### Requirement

- The "HMI alarms" editor is open.
- The Inspector window is open.

#### Procedure

To create an alarm class, follow these steps:

1. Click the "Alarm classes" tab.

   The table below shows the pre-defined alarm classes:

   ![Procedure](images/123006675083_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/123006675083_DV_resource.Stream@PNG-en-US.png)
2. Double-click "<Add new>" in the table.

   A new alarm class is created. Each new alarm class is automatically assigned a fixed ID.

   The properties of the new alarm class are shown in the Inspector window.
3. To configure the alarm class, select "Properties > General" in the Inspector window:

   - Enter a name for the alarm class.
   - Set the priority of the alarm class.
4. In the Inspector window, set the state machine of the alarm class.

   See [Configuring alarm acknowledgment](#configuring-alarm-acknowledgment-rt-unified).
5. You can also change the default background color as well as the text color and the settings for flashing under "Properties > Colors" in the Inspector window.

   These settings define how alarms from this alarm class are displayed in Runtime.

**Note**

For alarm colors to be displayed in Runtime, the "Use alarm colors" option must be enabled in the properties of the alarm control in the Inspector window. This option is enabled by default.

#### Alarm class "Acknowledgement":

An alarm of the "Acknowledgment" alarm class passes through the following alarm states:

- Incoming

  When the alarm occurs.
- Incoming/Outgoing

  When the alarm is outgoing.
- Normal

  After resetting the value on the PLC and through acknowledgment by the operator.

#### Alarm class "No acknowledgement"

An alarm of the "No acknowledgment" alarm class passes through the following alarm states:

- Incoming

  When the alarm occurs.
- Normal

  When the alarm is outgoing.

#### Alarm class "AlarmWithReset"

An alarm of the "No acknowledgment" alarm class passes through the following alarm states:

- Incoming

  When the alarm occurs.
- Incoming/outgoing or incoming/acknowledged

  When the alarm is outgoing.
- Incoming/acknowledged/outgoing or incoming/outgoing/acknowledged

  After resetting of the alarm by the operator.
- Normal

  After performing all actions.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Alarm classes (RT Unified)](#alarm-classes-rt-unified)
  
[Use common alarm classes (RT Unified)](#use-common-alarm-classes-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)

### Use common alarm classes (RT Unified)

#### Introduction

Common alarm classes are displayed under "Common data > Alarm classes" in the project tree and can be used for the alarms of an HMI device. Common alarm classes are used in STEP 7 for PLC alarms. You can create additional common alarm classes in WinCC. Common alarm classes are divided into predefined and user-defined common alarm classes. The predefined common alarm classes are "Acknowledgement" (for alarms with acknowledgment) and "No Acknowledgement" (for alarms without acknowledgment).

If you have created an HMI device and create a common alarm class, the system creates an alarm class for the created common alarm class under "HMI alarms > Alarm classes" which is linked to the common alarm class. If you change all properties for a created common alarm class, the system changes the properties "State machine" and "Priority" of the linked alarm class according to your changes to the "Acknowledgment" and "Priority" properties of the common alarm class. However, your changes to the "Name" and "Display name" properties of the common alarm class have no effect on the properties of the linked alarm class. When you delete a common alarm class, the linked alarm class is also deleted.

> **Note**
>
> From the "Common alarm class" property of an alarm class, you can see whether the alarm class is linked with a common alarm class and, if so, with which common alarm class. To see the property in the "HMI alarms" editor in the "Alarm classes" tab, enable there the "Common alarm class" column using the shortcut menu of the column titles. To see the property in the Inspector window, select an alarm class under "HMI alarms > Alarm classes" and click "General" in the Inspector window.

#### State machine

Common alarm classes have one of the following state machines:

- Alarm with simple acknowledgment
- Alarm without acknowledgment

You can configure the state machine directly in the "Alarm classes" editor. Configuration at the linked HMI alarm class in the "HMI alarms" editor is not possible.

> **Note**
>
> For the state machine "Alarm without acknowledgement", the background color configured for the state is ignored in the "Incoming/Outgoing" state.

#### Requirement

- You have created a project.

#### Creating common alarm classes

To create a common alarm class, follow these steps:

1. Double-click "Common data > Alarm classes" in the project tree.

   The "Alarm classes" editor opens in the working area.
2. To create a common alarm class, double-click in the first empty line of the table editor.
3. Specify the name, display name, and priority of the common alarm class and enable the mandatory acknowledgment, if required.

   A common alarm class is created. The system also creates an alarm class under "HMI alarms > Alarm class", which is linked to the common alarm class. The linked alarm class is given the same name and priority as the common alarm class by the system. If you have enabled the mandatory acknowledgment for the common alarm class, the linked alarm class is given the "Alarm with simple acknowledgment" state machine by the system. If you have not enabled the mandatory acknowledgment, it is given the state machine "Alarm without acknowledgment". The defined display name of the common alarm class has no effect on the properties of the linked alarm class.
4. If required, change the name of the alarm class that is linked to the common alarm class under "HMI alarms > Alarm classes".

   If you change the name of the linked alarm class, the common alarm class name is not changed by the system.

#### Assigning alarms to a common alarm class

Follow these steps to assign an analog or discrete alarm to a common alarm class:

1. In the "HMI alarms" editor, select the alarm that you want to assign to the common alarm class.
2. Click "General" in the Inspector window.
3. Click "Common data > Alarm classes" in the project tree. Alternatively, click "HMI Alarms" in the project tree.

   In the first case, the common alarm class is displayed in the details view. In the second case, the details view shows the alarm class which is linked to the common alarm class.
4. Select the common alarm class or the linked alarm class in the details view.
5. Drag the common alarm class or the linked alarm class to the "Alarm class" field or "Alarm class" column in the working area of the Inspector window of the alarm.

   In both cases, the alarm is assigned to the alarm class that is linked to the common alarm class.

   ![Assigning alarms to a common alarm class](images/129160877195_DV_resource.Stream@PNG-en-US.png)

   ![Assigning alarms to a common alarm class](images/129160877195_DV_resource.Stream@PNG-en-US.png)

#### Changing the common alarm class

To change a common alarm class, follow these steps:

1. Double-click "Common data > Alarm classes" in the project tree.

   The "Alarm classes" editor opens in the working area.
2. If necessary, change the name of the created common alarm class.

   The changed name of the common alarm class has no effect on the name of the alarm which is linked to the common alarm class.
3. If necessary, change the display name of the common alarm class.

   The changed display name of the common alarm class has no effect on the properties of the linked alarm class.
4. If required, enable or disable the mandatory acknowledgment of the common alarm class.

   If you enable the mandatory acknowledgment, the system changes the state machine of the linked alarm class to "Alarm with simple acknowledgment". If you disable the mandatory acknowledgment, the system changes the state machine of the linked alarm class to "Alarm without acknowledgment".
5. If necessary, change the priority of the common alarm class.

   The system changes the priority of the linked alarm class according to your change to the priority of the common alarm class.

> **Note**
>
> You can only change the display names for a predefined common alarm class. The changed display name of a predefined common alarm class has no effect on the properties of the alarm class which is linked to the predefined common alarm class.

#### Deleting a common alarm class

To delete a common alarm class, follow these steps:

1. Double-click "Common data > Alarm classes" in the project tree.

   The "Alarm classes" editor opens in the working area.
2. Select the created common alarm class that you want to delete.
3. Select the "Delete" entry from the shortcut menu.

   The system deletes the common alarm class and the alarm class linked with the common alarm class.
4. If an analog or discrete alarm has been assigned to the deleted linked alarm class, assign a different alarm class to the alarm. Otherwise a compile error will be generated.

> **Note**
>
> You cannot delete predefined common alarm classes or the alarm classes that are linked with them.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Alarm classes (RT Unified)](#alarm-classes-rt-unified)
  
[Creating alarm classes (RT Unified)](#creating-alarm-classes-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)

### Configuring the status texts of alarms (RT Unified)

#### Introduction

The texts for the states of alarms in runtime are displayed in the alarm control in the "Status Text" column. You can specify the status texts of alarms in the runtime settings.

> **Note**
>
> If no alarm status texts are defined, a compile error will be generated.

#### Requirement

- An alarm control has been configured.

#### Procedure

To configure the alarm status texts, follow these steps:

| 1. Open the "Runtime settings" of the HMI device. 2. Specify the status texts of alarms in runtime under "Alarms > Status texts":       | Field | Description |    | --- | --- |    | Incoming | Text for incoming alarms when changing to the operating state to be reported. The condition of an alarm is fulfilled. |    | Incoming/outgoing | Text for an outgoing alarm. The condition of an alarm is no longer fulfilled. |    | Incoming/acknowledged | Text for an acknowledged and outgoing alarm. The condition of an alarm is no longer fulfilled. |    | Incoming/acknowledged/outgoing | Text for an incoming, acknowledged, and outgoing alarm The condition of an alarm is no longer fulfilled. |    | Incoming/outgoing/acknowledged | Text for an incoming, outgoing, and acknowledged alarm. The condition of an alarm is no longer fulfilled. |    | Removed | Text for alarms in "Removed" state. Only PLC alarms can have this state. The state text is only displayed in the alarm log. If the HMI connection between HMI device and controller is disconnected and then re-established, the status text is displayed. |    | Normal | The condition of an alarm is no longer fulfilled. The alarm is no longer pending. The alarm is acknowledged as required by the alarm class. The alarm is reset by "Single confirm" as required by the alarm class. | 3. Change the status texts as required. Keep in mind that these texts are not language specific. In Runtime, always the text configured in engineering is always displayed, independent of the current Runtime language. 4. Select the "Alarm control" in the "Screens" editor. 5. To display the "Status text" column in the "Alarm control" object, select the "Visibility" property in the Inspector window under "Properties > Alarm control > Columns > [...] Status text alarm column". |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

---

**See also**

[Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified-1)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Configuring discrete alarms (RT Unified)

This section contains information on the following topics:

- [Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
- [Configure trigger (RT Unified)](#configure-trigger-rt-unified)
- [Sending an alarm acknowledgment to the PLC (RT Unified)](#sending-an-alarm-acknowledgment-to-the-plc-rt-unified)

#### Configuring discrete alarms (RT Unified)

##### Introduction

Discrete alarms are triggered by the PLC and indicate status changes in a plant. A discrete alarm is triggered by a specific value (bit) of a tag.

Imagine, for example, that the state of a valve is to be monitored during operation. The two possible valve states are "opened" and "closed". In this case, a discrete alarm is configured for each valve state. If the status of the valve changes, a discrete alarm is output, containing for example the following alarm text: "Valve closed".

> **Note**
>
> By default, the alarm class "Alarm" is assigned to every newly created discrete alarm. Adapt the alarm class if necessary.

##### Requirement

- The "HMI alarms" editor is open.
- The Inspector window is open.

##### Procedure

To configure a discrete alarm, proceed as follows:

1. Click the "Discrete alarms" tab.
2. To create a new discrete alarm, double-click "<Add>" in the table.

   A new discrete alarm is created.
3. Assign a name for the discrete alarm.
4. To configure the alarm, select "Properties > General" in the Inspector window:

   - Edit the name of the alarm as required.
   - Select the alarm class.
   - Configure the priority of the alarm (a value between "0" and "16").

**Note**

The name of a discrete alarm may contain up to 128 characters.

**Note**

Users can sort or filter the alarms in the alarm control by priority. Sorting on priority ensures that, with a single-line alarm control, the most important alarm (high priority) is displayed in the display area.

Upon filtering priority "16" in the alarm control, only alarms with priority "16" appear.

The priority of the alarm class applies to alarms with priority "0".

The priority of the alarm when displayed in runtime takes precedence over the priority of the alarm class.

| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| - Large machines and plants have a significant number of alarm sources that can trigger different types of alarms. It makes sense to structure the alarm system so that the operator can keep track of this wide range. One suitable method for this is alarm prioritization. Importance and urgency are the criteria for assigning the priority value and/or assigning the alarm class. Alarm priorities can also be based on the potential impact (system downtime, loss of production, production delay etc.). If multiple alarms are output, the system can suggest to the operator the order in which they should be handled on the basis of priorities. - You can create discrete alarms together with the trigger tags and edit them in the "HMI tags" editor. You create tags in the usual way. Then click <Add> in the table on the "Discrete alarms" tab at the bottom of the work area. A new discrete alarm is created for the tag that has been created. If you have selected the wrong data type, the tag will be highlighted in the discrete alarm. If you delete, move or copy objects in the "HMI tags" editor, these changes also take effect in the "HMI alarms" editor. The configured discrete alarms are created in the "HMI tags" editor and displayed in the "HMI alarms" and "HMI tags" editors.   If you are using an array as a data type for managing alarms, you can assign a discrete alarm to the individual array elements. The alarms assigned to the array elements are displayed under "Discrete alarms" or when you select the array. The alarms have their position within the array as an extension, e.g. "HMI_Tag_1[2]". - Supplementary information on the individual alarms ensures rapid fault localization and troubleshooting. |  |

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[Configuring alarm acknowledgment (RT Unified)](#configuring-alarm-acknowledgment-rt-unified)
  
[Creating alarm classes (RT Unified)](#creating-alarm-classes-rt-unified)
  
[Use common alarm classes (RT Unified)](#use-common-alarm-classes-rt-unified)
  
[Configuring multilingual alarm texts (RT Unified)](#configuring-multilingual-alarm-texts-rt-unified)
  
[Editing system alarms (RT Unified)](#editing-system-alarms-rt-unified)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)
  
[Creating internal tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#creating-internal-tags-rt-unified)

#### Configure trigger (RT Unified)

You can define trigger properties for discrete alarms. You can specify a trigger tag, a trigger bit and a trigger mode for an alarm.

##### Requirement

- The "HMI alarms" editor is open.
- A discrete alarm is created.

##### Procedure

To define the trigger properties, follow these steps:

1. Select the discrete alarm.
2. Click on "Trigger" under "Properties" in the Inspector window.

   The "Trigger" window opens.
3. Select the tag and the bit that are to trigger the alarm.

   Select a tag with the following data type: Bool, Byte, Word, DWord, LWord or Array with Byte, Word, DWord, LWord
4. You can also specify whether to trigger the alarm at a rising or falling edge.

   ![Procedure](images/134669574411_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/134669574411_DV_resource.Stream@PNG-en-US.png)

**Note**

**Restrictions for trigger bits**

Each use of a trigger tag requires a different trigger bit. The availability of trigger bits depends on the data type of the trigger tag.

##### Result

Trigger tag, trigger bit and trigger mode have been specified for the selected discrete alarm.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

#### Sending an alarm acknowledgment to the PLC (RT Unified)

##### Requirement

- The "HMI alarms" editor is open.
- The desired alarm is created and assigned to an alarm class with mandatory acknowledgement.

##### Procedure

To configure the acknowledgment of an alarm to be sent to the PLC, follow these steps:

1. In the "HMI alarms" editor, click the "Discrete alarms" tab and select the desired discrete alarm.
2. In the Inspector window, select "Properties > Properties > Acknowledgment".
3. Under "Status tag", select the tag and the bit set by the alarm acknowledgment function.

   The selection of the tags depends on your configuration in the "HMI tags" editor and the fact whether the alarm is acknowledged is stored in these tags.

   Supported data types for the status tag: Word, DWord, LWord, Byte.

**Note**

The HMI device and PLC only have read access to the status tag memory area.

**Note**

The normal status of the bit is 1.

When the alarm is in the "active" state, the bit changes from 1 to 0.

When you acknowledge the alarm, the bit changes from 0 to 1.

To configure that the alarm is acknowledged by the PLC, follow these steps:

1. In the "HMI alarms" editor, click the "Discrete alarms" tab and select the desired discrete alarm.
2. In the Inspector window, select "Properties > Properties > Acknowledgment".
3. Under "Control tag", select the tag and the bit set by the alarm acknowledgment function.
4. The tag can be any tag, there are no restrictions.

   Supported data types for the control tag: Word, DWord, LWord, Byte.

![Procedure](images/166758655883_DV_resource.Stream@PNG-en-US.png)

##### Result

If the operator acknowledges the alarm in Runtime, the operating step is forwarded to the PLC.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Configuring analog alarms (RT Unified)

This section contains information on the following topics:

- [Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)
- [Configure trigger (RT Unified)](#configure-trigger-rt-unified-1)

#### Configuring analog alarms (RT Unified)

##### Introduction

You can configure analog alarms to display limit violations. You have defined in advance a limit value for the trigger tag and the trigger mode. An analog alarm is triggered depending on which mode you have defined, for example, when the value is higher than, lower than, or the same as the defined value.

For example, if the speed of a motor drops below a certain value, an analog alarm is triggered. This alarm could contain the following text: "Motor speed is too low".

> **Note**
>
> By default, the alarm class "Alarm" is assigned to every newly created analog alarm. Adapt the alarm class if necessary.

##### Requirement

- The "HMI alarms" editor is open.
- The Inspector window is open.

##### Procedure

To configure an analog alarm, follow these steps:

1. Click the "Analog Alarms" tab.
2. To create a new analog alarm, double-click "<Add new>" in the table.

   A new analog alarm is created.
3. To configure the alarm, select "Properties > General" in the Inspector window:

   - Edit the name of the alarm as required.
   - Select the alarm class.
   - Configure the priority of the alarm (a value between "0" and "16").

**Note**

You can sort or filter the alarms in the alarm control by priority. Sorting by priority ensures that, with a single-line alarm control, the most important alarm (high priority) is displayed in the display area.

If you filter by priority "16" in the alarm control, only alarms with priority "16" will appear.

The priority of the alarm class applies to alarms with priority "0".

The priority of the alarm when displayed in Runtime takes precedence over the priority of the alarm class.

| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| - Large machines and plants have a significant number of alarm sources that can trigger different types of alarms. It makes sense to structure the alarm system so that the operator can keep track. One suitable method for this is alarm prioritization. Importance and urgency are the criteria for assigning the priority value and/or assigning the alarm class. Alarm priorities can also be based on the potential impact (system downtime, loss of production, production delay etc.). If multiple alarms are output, the system can suggest to the operator the order in which they should be handled on the basis of priorities. - You can create analog alarms together with the trigger tags and edit them in the "HMI tags" editor. Create the tags in the usual way and configure the range values of the tags. Then click "<Add new>" in the table on the "Analog alarms" tab at the bottom of the work area. A new analog alarm is created for the tag that has been created. If you have selected the wrong data type, the tag will be highlighted in the analog alarm. If you delete, move or copy objects in the "HMI tags" editor, these changes also take effect in the "HMI alarms" editor. The configured analog alarms are created in the "HMI tags" editor and displayed in the "HMI alarms" and "HMI tags" editors. - Supplementary information on individual alarms ensures rapid fault localization and troubleshooting. |  |

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Analog alarms: (RT Unified)](#analog-alarms-rt-unified)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[Configuring alarm acknowledgment (RT Unified)](#configuring-alarm-acknowledgment-rt-unified)
  
[Creating alarm classes (RT Unified)](#creating-alarm-classes-rt-unified)
  
[Use common alarm classes (RT Unified)](#use-common-alarm-classes-rt-unified)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring multilingual alarm texts (RT Unified)](#configuring-multilingual-alarm-texts-rt-unified)
  
[Creating internal tags (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#creating-internal-tags-rt-unified)

#### Configure trigger (RT Unified)

Trigger properties can be defined for analog alarms. You can specify a trigger tag, a trigger bit, and a trigger mode for an alarm.

##### Requirement

- The "HMI alarms" editor is open.
- An analog alarm has been created.

##### Procedure

To define the trigger properties, follow these steps:

1. Select the analog alarm.
2. Click on "Trigger" under "Properties" in the Inspector window.

   The "Trigger" window opens.
3. Specify the trigger tags and limits. Use one of the following data types: "Int", "Real", "LReal", "SInt", "USInt", "UInt", "UDInt" and "ULInt".
4. Select the trigger mode in the "Mode" field:

   - "Less": The alarm is triggered if the limit is undershot.
   - "Greater": The alarm is triggered if the limit is overshot.
   - "Equal": The alarm is triggered when the limit is reached.
   - "Not equal": The alarm is triggered if the limit is not reached.
   - "Less or equal": The alarm is triggered if the limit is undershot or reached.
   - "Greater or equal": The alarm is triggered if the limit is overshot or reached.
5. You can create additional limits for the alarm as required. Note the following information:

   - A tag is monitored using only one alarm procedure. You should therefore create either analog alarms **or** discrete alarms for a tag.
   - If the object included in the selection does not yet exist, create it in the object list and change its properties later.

   ![Procedure](images/102478238731_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/102478238731_DV_resource.Stream@PNG-en-US.png)

**Note**

Do not use trigger tags for anything else.

##### Result

Trigger tags and limits have been defined for the selected analog alarm.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Integrating OPC UA server alarm instances (RT Unified)

You have the option of integrating alarm instances from an OPC UA server into your Runtime project. Proceed as described in the section [Integrating OPC UA server alarm instances into a Unified client](OPC%20UA%20-%20Open%20Platform%20Communications%20%28RT%20Unified%29.md#integrating-opc-ua-server-alarm-instances-into-a-unified-client-rt-unified-1).

### Configuring the alarm texts (RT Unified)

#### Introduction

For an alarm, you can configure up to ten alarm texts, namely one alarm text and up to nine additional texts. If required, you can insert output fields for displaying alarm parameters in each alarm text. Each alarm text contains up to 512 characters.

#### Requirement

- An alarm has been created.
- An alarm control has been configured.

#### Procedure

To configure alarm texts, follow these steps:

1. In the "HMI alarms" editor, select the discrete or analog alarm.
2. Enter an alarm text under "Properties > Properties > Alarm texts > Settings > Alarm text" in the Inspector window.
3. If necessary, insert parameter output fields in the alarm text via the "Insert parameter field" shortcut menu command.
4. Enter additional alarm texts in the fields for additional texts under "Properties > Properties > Alarm texts" in the Inspector window.
5. If necessary, insert parameter output fields in the additional alarm texts via the "Insert parameter field" shortcut menu command.
6. Select the alarm control in the "Screens" editor.
7. To display the alarm texts in Runtime, enable the required columns of the columns numbered 10 to 19 in the Inspector window under "Properties > Properties > Alarm control > Columns".

   ![Procedure](images/134677910027_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/134677910027_DV_resource.Stream@PNG-en-US.png)

**Note**

If necessary, you can insert a parameter field with a right-click on the text box. You can assign a process and a file format to the parameter.

**Note**

**Formatting of the text**

If you use the clipboard to copy a text into an alarm or additional text, formatting may become invalid. You can delete the formatting with the command "Delete formatting". You can execute the command via the shortcut menu by right-clicking on the corresponding text.

#### Result

Alarm texts have been defined for the selected alarm.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Configuring info texts (RT Unified)

Info texts can be written for analog and discrete alarms, and can be displayed in Runtime via the "Infotext - configuration" button of the alarm control.

#### Requirement

- The "HMI alarms" editor is open.
- A discrete alarm is created.

#### Procedure

To define info texts, follow these steps:

1. Select the discrete or analog alarm.
2. Click on "Info text" under "Properties" in the Inspector window.

   The "Info text" window opens.
3. Enter the info text.

   ![Procedure](images/134677166347_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/134677166347_DV_resource.Stream@PNG-en-US.png)

#### Result

An info text has been defined for the selected alarm.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Outputting parameters in a discrete or analog alarm (RT Unified)

#### Introduction

To display alarm parameters in a discrete or analog alarm, insert a corresponding output field. You can select the parameters configured in "Properties > Properties > Alarm parameters" for use as alarm parameters.

#### Requirement

- The "HMI alarms" editor is open.
- The discrete or analog alarm is selected.

#### Procedure

To output a parameter in an alarm text, follow these steps:

1. Place the cursor at the required position in the alarm text field.
2. To output an alarm parameter, select "Insert parameter field" from the shortcut menu.

   A dialog box opens.
3. Select the desired parameter.
4. Moreover, you can specify the following data for alarm parameters:

   - The tag that provides the parameter values.

     The tag configured for the parameter under "Properties > Properties > Alarm parameters" is entered by default. If you select a different tag, WinCC updates the parameter configuration in "Properties > Properties > Alarm parameters" accordingly.
   - Display type, text list, length, number of decimal places and alignment of the output field
   - To display leading zeros in the output field, enable "Leading zeros".
5. Confirm the dialog to save your entries.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Configuring optional parameters for discrete and analog alarms (RT Unified)

#### **Setting the alarm context**

In a large plant system, it makes sense to save information about alarm origins, such as the physical, geographical, or logical grouping of plant units that is defined by the site. This helps operators in identifying the causes of the alarm and the source of the fault.

1. Select the alarm.
2. You can configure information on alarm sources in the "Origin" field of the Inspector window under "Properties > Properties > General > Alarm context".

The "Area" field is a static field and contains information about the device.

#### **Creating info texts for alarms**

To configure an infotext for an alarm and thus support operators, follow these steps:

1. Select a discrete or analog alarm.
2. Select "Properties > Info text" in the Inspector window and enter the required text.
3. To insert a line break in the info text, press "Shift+Enter" at the corresponding text location.

   > **Note**
   >
   > The row height is not adjusted automatically, but must be set manually in the properties of the alarm control.
4. To create multi-lingual info texts, enter the respective texts in the predefined project languages in the Inspector window and, if necessary, in the reference language.

#### **Activating parameters for a discrete or analog alarm**

To output process values to an output field in the alarm text, assign corresponding tags to the parameter blocks. Follow these steps:

1. Select the alarm.
2. In the Inspector window, click "Properties > Alarm parameters".
3. Select a tag for the alarm parameter.
4. You can enter multiple alarm parameters if required.

   Insert the activated process values as a selection box in an alarm text.

   > **Note**
   >
   > You can configure up to 10 tags as alarm parameters for discrete and analog alarms.
   >
   > All available data types are supported.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[Configuring multilingual alarm texts (RT Unified)](#configuring-multilingual-alarm-texts-rt-unified)
  
[Editing system alarms (RT Unified)](#editing-system-alarms-rt-unified)
  
[Configuring alarm acknowledgment (RT Unified)](#configuring-alarm-acknowledgment-rt-unified)
  
[Translating texts directly (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#translating-texts-directly-rt-unified)
  
[Exporting project texts (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#exporting-project-texts-rt-unified)
  
[Analog alarms: (RT Unified)](#analog-alarms-rt-unified)
  
[Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)

### Configuring multilingual alarm texts (RT Unified)

#### Requirement

- The "HMI alarms" editor is open.
- An alarm has been created.

#### Procedure

1. Select one or more alarms for which you want to configure multilingual alarm texts.
2. You can view the alarm texts already configured in the set project languages under "Properties > Alarm texts".
3. If available, enter the alarm texts in the required project languages.

   The alarm texts will then be displayed in the set runtime language in runtime.

> **Note**
>
> All alarm texts are managed together with other project texts under "Languages & Resources > Project texts".
>
> If you cannot configure the project texts in multiple languages yourself, export them to an Excel file and have them translated. You can then import the texts to your project.

---

**See also**

[Basics of project texts (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#basics-of-project-texts-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
  
[Working with multiple languages (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#working-with-multiple-languages-rt-unified)
  
[Importing project texts (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#importing-project-texts-rt-unified)
  
[Translating texts directly (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#translating-texts-directly-rt-unified)
  
[Selecting the reference language and editing language (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#selecting-the-reference-language-and-editing-language-rt-unified)

### Editing system alarms (RT Unified)

#### Basics

A system alarm indicates the status of the system and communication errors between the HMI device and the system. System alarms are output in runtime in the configured alarm control. System alarms are output in the language currently set on your HMI device.

The time format (AM/PM or 24-hour format) is based on the selected language. If there is no translation of the alarm texts in this language, English is selected as the substitute language and the corresponding time format is displayed.

**Example of an alarm**

"Memory is full!"

#### Editing system alarms

You can edit system alarms in the "HMI alarms > System alarms" editor or under "Languages & Resources > Project texts". In the "Category" column, you can tell by the "HMI system message" label that this is a system alarm. You can export the system alarms together with the other texts under "Project texts" and have them translated.

#### Parameters of the system alarms

System alarm can contain encrypted parameters. The parameters are of relevance when troubleshooting because they provide a reference to the source code of the runtime software. These parameters are output after the "Error code: text"

---

**See also**

[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
  
[System alarms (RT Unified)](#system-alarms-rt-unified)

### Filtering PLCs alarm using display classes (RT Unified)

#### Introduction

PLC alarms are configured in STEP 7. PLC alarms are available in WinCC running in a STEP 7 environment.

If a PLC is connected to multiple HMI devices, the configuration engineer assigns display classes to the PLC alarms in STEP 7. The display classes determine the allocation to the HMI device. You can activate the display classes for your HMI device that are to be displayed on it. In this case, only the PLC alarms from this display class will be displayed on the HMI device. Up to 17 display classes are possible.

> **Note**
>
> WinCC only supports PLC alarms of a SIMATIC S7-1500 controller. In addition, WinCC only supports PLC alarms that are automatically updated by the central alarm management in the PLC.

#### Requirement

- A connection was established to the PLC.
- Alarms were configured in STEP 7.

#### Filtering PLCs alarm using display classes

To filter PLC alarms by display class, follow these steps:

1. Click "Runtime settings > Alarms" in the project tree under your HMI device.

   One or several connections to a PLC are shown in "PLC alarms".
2. Select the display classes whose PLC alarms you want to display for the connection.

---

**See also**

[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)
  
[Configuring automatic updates of PLC alarms on the HMI device (RT Unified)](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)
  
[Alarm system (RT Unified)](#alarm-system-rt-unified)

### Configuring alarm acknowledgment (RT Unified)

#### Introduction

The alarm class defines how the alarms from an alarm class are to be acknowledged. When you assign an alarm to an alarm class, you define the state machine and the acknowledgment model for that alarm.

#### Requirement

- The "HMI alarms" editor is open.
- The desired alarm class has been created.
- The desired alarm has been created.

#### Procedure

To configure the acknowledgement of an alarm, follow these steps:

1. In the "HMI alarms" editor, click the "Alarm class" tab and select the desired alarm class.
2. You select the desired state machine under "Properties > General > Acknowledgment" in the Inspector window.

   ![Procedure](images/100428327179_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/100428327179_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The "Acknowledge visible alarms", "Single acknowledgment", and "Single confirm" buttons which are relevant for acknowledgment are enabled in the alarm control by default and can be operated in runtime.

#### Configuring the state machine of common alarm classes

The "Alarm class" tab also shows alarm classes that are linked to common alarm classes. The "General > Common alarm classes" property is set for these alarm classes.

Alarm classes with such a link have one of the following state machines:

- Alarm with simple acknowledgment
- Alarm without acknowledgment

It is not possible to change the state machine in the "HMI alarms" editor. If necessary, change the state machine in the editor for common alarm classes.

---

**See also**

[Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)
  
[Creating alarm classes (RT Unified)](#creating-alarm-classes-rt-unified)
  
[Configuring discrete alarms (RT Unified)](#configuring-discrete-alarms-rt-unified-1)
  
[Configuring analog alarms (RT Unified)](#configuring-analog-alarms-rt-unified-1)
  
[Configuring optional parameters for discrete and analog alarms (RT Unified)](#configuring-optional-parameters-for-discrete-and-analog-alarms-rt-unified)
  
[Use common alarm classes (RT Unified)](#use-common-alarm-classes-rt-unified)

## Exporting or importing alarms (RT Unified)

This section contains information on the following topics:

- [Exporting alarms (RT Unified)](#exporting-alarms-rt-unified)
- [Importing alarms (RT Unified)](#importing-alarms-rt-unified)

### Exporting alarms (RT Unified)

#### Introduction

WinCC has an export function for alarms.

#### Requirement

- The WinCC project for export is open.
- Alarms have been created in the project.
- The "HMI alarms" editor is open.

#### Exporting alarms

To export alarms from a WinCC project, follow these steps:

1. Click the ![Exporting alarms](images/70613019147_DV_resource.Stream@PNG-de-DE.png) button in the "Discrete alarms" or "Analog alarms" tab.

   The "Export HMI alarms" dialog box opens.
2. Click "..." and specify the file in which data is saved.
3. Specify whether you want to export "Discrete alarms" and/or "Analog alarms".
4. Click "Export".

   The export starts. When the export is complete, an alarm about completion of the export is displayed.
5. Confirm the alarm on completion of the export with "OK".

#### Result

The exported data has been written to an xlsx file. The xlsx file has been stored in the specified folder.

If you have only exported discrete alarms, the xlsx file is comprised of a "DiscreteAlarms" worksheet only. If you have only exported analog alarms, the xlsx file is comprised of "AnalogAlarms" and "Limits" worksheets. If you have exported discrete alarms and analog alarms, the xlsx file is comprised of "DiscreteAlarms", "AnalogAlarms", and "Limits" worksheets.

Each alarm is in a separate row in the xlsx file.

> **Note**
>
> The list entries with the "FieldInfo" designation specify whether the alarm text contains dynamic parameters. The settings are separated by a semicolon ";".

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Importing alarms (RT Unified)

#### Introduction

WinCC provides an import function for alarms. Alarms are identified by means of the alarm ID. An existing alarm is overwritten by the data from the import file if the alarm ID already exists in the project on import. A new alarm is created in the project if the alarm does not yet exist in the project on import.

#### Requirement

- An xlsx file with alarms has been created.
- The xlsx file has the same structure as an xlsx file that is created when alarms are exported.
- The IDs and names that were assigned for alarms in the xlsx file are unique throughout the project.
- The WinCC project for import is open.
- The "HMI alarms" editor is open.

#### Importing alarms

To import alarms into a WinCC project, follow these steps:

1. Click the ![Importing alarms](images/70613888907_DV_resource.Stream@PNG-de-DE.png) button in the "Discrete alarms" or "Analog alarms" tab.

   The "Import HMI alarms" dialog box opens.
2. Click "..." and select the file that you want to import.
3. Click "Import".

   The import starts. An xml log file is created on import. When the import is complete, a message on completion of the import is displayed.
4. Confirm the message on completion of the import with "OK".

**Note**

To open the created xml log file, click the link "Click here to view the log file". It is advisable to open the xml log file especially if the import was completed with warnings.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

## Configuring the alarm control (RT Unified)

This section contains information on the following topics:

- [Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified-1)
- [Displaying all information about an alarm (RT Unified)](#displaying-all-information-about-an-alarm-rt-unified)
- [Configuring the toolbar (RT Unified)](#configuring-the-toolbar-rt-unified)
- [Configuring the information bar (RT Unified)](#configuring-the-information-bar-rt-unified)
- [Configuring columns and sorting (RT Unified)](#configuring-columns-and-sorting-rt-unified)
- [Configuring filters in the alarm control (RT Unified)](#configuring-filters-in-the-alarm-control-rt-unified)
- [Configuring the export of alarms (RT Unified)](#configuring-the-export-of-alarms-rt-unified)
- [Displaying logged alarms (RT Unified)](#displaying-logged-alarms-rt-unified)
- [Configuring alarm statistics (RT Unified)](#configuring-alarm-statistics-rt-unified)
- [Configuring the display of system diagnostics alarms (RT Unified)](#configuring-the-display-of-system-diagnostics-alarms-rt-unified)

### Configuring the alarm control (RT Unified)

#### Introduction

The alarm control is configured for a screen. Current or logged alarms are displayed in runtime in the alarm control. It displays multiple alarms simultaneously, depending on its configured size. You configure criteria for filtering the alarms.

You configure the alarm control in the Engineering System using the "Alarm control" object.

You can configure multiple alarm controls with different contents and in different screens as needed.

> **Note**
>
> **Text alignment in cells of the alarm control**
>
> The "Spacing" and "Text trimming" properties only have an effect in the "Graphic and Texts", "Graphic or Text" and "Graphic" modes.

#### Requirement

- A screen is open.
- The "Toolbox" task card is open.

#### Procedure

1. Insert an "Alarm control" object from the "Tools" task card into the screen.

   ![Procedure](images/132489387019_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/132489387019_DV_resource.Stream@PNG-en-US.png)
2. Under "Properties", define the desired height, width and position of the Alarm control.
3. Under "Properties > Miscellaneous > Alarm control", define the layout and color composition of the alarm control as well as the design of the header and the contents of the table grid.
4. To ensure that the most current alarm is always displayed and highlighted in the alarm control in runtime, enable the "Miscellaneous > Alarms - show current" property.   
   The visible area of the alarm control is moved in runtime if necessary. Users cannot select alarms individually or sort them by column. Alarms that have been filtered out of the alarm control are not displayed.

   If you configure the "Alarms - show current" button as visible and operable, users can pause and start this behavior in runtime as required. The alarm control always starts with the behavior configured in "Miscellaneous > Alarms - show current".
5. Under "Alarm source" you specify which alarms the alarm control displays in runtime by default.

   Depending on your task or the requirements in your company, you can select from the following display options:

   - "Not configured": The alarm control does not display any alarms.
   - "Pending alarms": The alarm control displays the currently pending alarms.
   - "Logged alarms": The alarm control displays the logged alarms.
   - "Logged alarms updated": The alarm control displays the logged alarms that are updated at specified intervals.
   - "Alarm definition": The alarm control displays all alarms configured in the Engineering System, regardless of whether they have occurred.
   - "Alarm statistics": Activates the display of a statistical overview of display duration and frequency of alarms.

   Depending on your selection, the view in the alarm control already changes in the Engineering System. The buttons relevant for the settings are shown as being active, while buttons that are not relevant are grayed out. These settings are applied for runtime.
6. Define which alarms are displayed in runtime by default in the alarm summary for pending alarms and for defined alarms.

   - In the selection list under "Miscellaneous > Alarms - current", select which alarms are displayed as pending alarms.
   - In the selection list under "Miscellaneous > Alarms - displayed", select which alarms are displayed as defined alarms.

   Depending on your task or the requirements in your company, select one or more display options depending on the status of the alarms:

   - "None": The alarm control displays all alarms.
   - "Not suppressed": The alarm control displays only the alarms that are not suppressed.
   - "Locked": The alarm control displays only the disabled alarms.
   - "Suppressed by design": The alarm control displays only the alarms that are suppressed by design.
   - "Shelved": The alarm control displays only the shelved alarms.

   Your selection is displayed in the alarm control by default when you start runtime.
7. If necessary, select the authorization needed to operate the alarm control in runtime.
8. Under time zone you set the desired time zone by entering a decimal value for the time zone.

   - "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
   - "-1": The local time zone of the device

**Note**

If you do not make a selection, the alarm control displays all alarms.

**Note**

You can change the display at any time in runtime even if you have selected a different display option in the Engineering System under "Alarm source" or "Active alarms".

**Note**

In Runtime, you also have the option of setting the time zone via a selection list.

#### Result

Alarms of various alarm classes are output in the alarm control in runtime. To change the control in runtime, click the configured buttons of the toolbar in the alarm control.

#### Using an alarm color

To display the colors configured for an alarm in the alarm control, follow these steps in the Engineering System:

1. Enable the "Format > Alarm colors - use" property in the properties of the alarm control.
2. Enable the "Alarm colors - use" property under "Miscellaneous > Alarm control > Columns" for each column that is to use the configured alarm color.

In the Inspector window of the alarm control under "Properties > Properties > Miscellaneous > Alarm control" you can set the colors of the alarm control, e.g. "Selection - background color", "Selection - foreground color", "Background - alternative color".

![Using an alarm color](images/166962069899_DV_resource.Stream@PNG-en-US.png)

#### Requirements for window settings

You can find the window settings under "Properties > Properties > Appearance > Window settings".

If the "Show border" option is not enabled, the "Can be sized" option is ignored.

If the "Show header" option is not enabled, the "Can be moved", "Can be maximized" and "Can be closed" options are ignored.

![Requirements for window settings](images/164402081547_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring the toolbar (RT Unified)](#configuring-the-toolbar-rt-unified)
  
[Configuring filters in the alarm control (RT Unified)](#configuring-filters-in-the-alarm-control-rt-unified)
  
[Configuring the export of alarms (RT Unified)](#configuring-the-export-of-alarms-rt-unified)
  
[Displaying logged alarms (RT Unified)](#displaying-logged-alarms-rt-unified)
  
[Defining the output format (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#defining-the-output-format-rt-unified)
  
[Configuring columns and sorting (RT Unified)](#configuring-columns-and-sorting-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[Configuring an alarm control for plant objects (RT Unified)](Configuring%20plant%20hierarchies%20%28RT%20Unified%29.md#configuring-an-alarm-control-for-plant-objects-rt-unified)
  
[Configuring the status texts of alarms (RT Unified)](#configuring-the-status-texts-of-alarms-rt-unified)
  
[Display messages from participating devices (RT Unified)](Using%20distributed%20systems%20%28RT%20Unified%29.md#display-messages-from-participating-devices-rt-unified)
  
[Configuring reordering of the columns (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#configuring-reordering-of-the-columns-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Displaying all information about an alarm (RT Unified)

#### Introduction

When configuring an alarm control, you have the option of providing the operator with a pop-up in runtime that shows further information about an alarm selected in runtime.

The following system function is available for this purpose: [Alarm.GetSelectedAlarmAttributes()](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#alarmgetselectedalarmattributes-rt-unified).

#### Requirement

- An alarm control has been configured.

#### Procedure

1. In the Inspector window, select the "Selection changed" event.
2. Call the "GetSelectedAlarmAttributes" function in a script.

   All attributes of the alarm are read out.
3. Display the attributes in Runtime in a pop-up.

The output of the attributes can also be triggered by a button.

A snippet "Get all alarm properties of the selected alarm from the alarm control" is available under "HMI Runtime > Screen" in the script editor.

#### Result

The "Alarms - show current" button (Autoscroll) must be switched off.

The operator selects an entry in the alarm control in runtime.

A pop-up with the attributes of the alarm is displayed.

The function also outputs attributes for logged alarms and alarms of the alarm statistics.

### Configuring the toolbar (RT Unified)

#### Introduction

You operate the alarm control in runtime using the buttons in the toolbar. During configuration, you define the contents of the toolbar.

The following buttons are visible in the alarm control by default:

- "Show active alarms"
- "Show logged alarms"
- "Show and update logged alarms"
- "Alarm statistics - view"
- "First line"
- "Previous line"
- "Next line"
- "Last line"
- "Single acknowledgment"
- "Acknowledge visible alarms"
- "Single confirm"
- "Alarms - show current"
- "Alarm statistics - setup"
- "Selection display"
- "Sorting - configuration"

The following buttons are not visible in the alarm control by default and must be made visible via "Properties > Properties > Miscellaneous > Toolbar > Elements". To these additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

- "Show defined alarms"
- "Alarm annunciator"
- "Move to next acknowledgeable alarm"
- "Previous page"
- "Next page"
- "Info text - setup"
- "Comments - setup"
- "Disable alarm"
- "Enable alarm"
- "Shelve alarm"
- "Unshelve alarm"
- "Copy lines"
- "Time base - setup"
- "Display options - setup"
- "Locked alarms - configuration"
- "Export"
- "Select context"

#### Requirement

- The "Alarm control" object is selected in the screen.
- The Inspector window is open.

#### Configuring the toolbar

1. Configure the general properties of the toolbar, such as alignment or background color, in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar".
2. Under "Properties > Properties > Miscellaneous > Toolbar > Elements" in the Inspector window, enable the buttons you need in runtime, e.g. "Export".
3. Configure the display of the respective button, e.g. background color, border, and maximum and minimum size.
4. If needed, you can define a tooltip for the buttons.
5. If a button is not to be operated in runtime, deselect "Operator control - allow".

   You can reactivate a deactivated a button using a script in runtime, for example.

> **Note**
>
> The order and functionality of the buttons are defined in the system and cannot be changed.

#### Custom ID

The custom ID can be used if you want to specifically access a certain button with an ID to be set via scripting.

You set this property under "Properties > Properties > Miscellaneous > Toolbar > Elements > Button".

#### Start behavior for "Alarms - show current"

The "Alarms - show current" button starts with the behavior configured in "Properties > Miscellaneous > Show current".

If you configure the button as operable, users can change the behavior in runtime. By clicking the button they pause or restart the display of the current alarms as needed.

---

**See also**

[Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified-1)
  
[Configuring columns and sorting (RT Unified)](#configuring-columns-and-sorting-rt-unified)
  
[Configuring filters in the alarm control (RT Unified)](#configuring-filters-in-the-alarm-control-rt-unified)
  
[Configuring the export of alarms (RT Unified)](#configuring-the-export-of-alarms-rt-unified)
  
[Displaying logged alarms (RT Unified)](#displaying-logged-alarms-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Configuring the information bar (RT Unified)

#### Introduction

The information bar displays status information of the alarm control. During configuration, you configure the content of the information bar.

#### Requirement

- The "Alarm control" object is selected in the screen.
- The Inspector window is open.

#### Configuring the information bar

1. In the Inspector window, configure the general properties of the Information bar such as the font or the background color under "Properties > Properties > Miscellaneous > Status bar".
2. In the Inspector window, select the elements you need in runtime, such as date, time, connection status, etc. under "Properties > Properties > Miscellaneous > Information bar > Elements".
3. To adjust the size of an element in the information bar, select "User-defined".
4. Enter the width and height in pixels.
5. To set the order of the elements, select the element in the list and move it to the desired position.

#### Custom ID

The custom ID can be used if you want to selectively access a specific button with an ID to be set via scripting.

You set this property under "Properties > Properties > Miscellaneous > Toolbar > Elements > Button".

### Configuring columns and sorting (RT Unified)

#### Introduction

You configure the order in which the columns of the alarm control are displayed in runtime.

#### Requirement

- The "Alarm control" object is selected in the screen.
- The Inspector window is open.

#### Configuring columns

1. Click "Properties > Alarm control > Columns" in the Inspector window.
2. Enable the "Visibility" property for the relevant columns.
3. Under "Alarm text block" select the content that is to be displayed in the column, e.g. "Alarm class".
4. Under "Alarm column [n] > Header > Text", enter the desired column name that is to be displayed in the alarm control.

**Note**

For the column names to be configured as multilingual, you must enter the name of the column under "Alarm column [n] > Header > Text".

You will then see the configured text in the Inspector window under "Texts" and can store additional languages.

If you only enter the name under "Alarm column [n] > Name", multilingual configuration is not possible.

#### Configuring the sorting

To sort alarms column by column in the alarm control, follow these steps:

1. Under "Properties > Alarm control > Allow sorting" so that sorting is generally possible in the alarm control in runtime.
2. Under "Properties > Alarm control > Columns", open the alarm column by which you want to initially sort the alarms, e.g. the "Priority" column.
3. Select the sorting order "1".
4. Select the desired sorting direction, e.g. "Ascending".

   - The number "1" with the arrow pointing upwards for ascending sort order is displayed in runtime in the column with sorting order "1".
   - If the sorting order "Ascending" has been enabled in the alarm control, a click on the column header changes the sorting direction from ascending to descending.
5. To allow sorting for this column, enable "Alarm column [n] > Sorting - allow".

**Note**

You can configure any sorting order.

However, if the "Alarms - Show current" button has been enabled under "Properties", the most current alarms are always displayed first.

#### Column sorting of date/time values in the alarm control

In the engineering system, you can configure different output formats for displaying date/time values. The following applies to the column sorting of these values in an alarm control on the Unified Comfort Panel:

The following output formats do not support sorting in columns:

- {D,@EEE, MMM dd, `yy}
- {D,medium}
- {D,long}
- {D}

The following output formats support sorting in columns only in English:

- {D,@dd. MMMM yyyy}
- {D,@dd. MMM}
- {D, @MMM dd, yyyy}
- {D, @MMMM dd}
- {D} {T}

---

**See also**

[Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified-1)
  
[Configuring the toolbar (RT Unified)](#configuring-the-toolbar-rt-unified)
  
[Configuring filters in the alarm control (RT Unified)](#configuring-filters-in-the-alarm-control-rt-unified)
  
[Configuring the export of alarms (RT Unified)](#configuring-the-export-of-alarms-rt-unified)
  
[Displaying logged alarms (RT Unified)](#displaying-logged-alarms-rt-unified)

### Configuring filters in the alarm control (RT Unified)

#### Introduction

You filter the display of alarms in the alarm control as needed. You configure a static value, a tag or a script for the filter. You configure this function in the "Alarm control" object in the "Screens" editor. To filter the alarms in runtime, click the "Selection display" button in runtime.

You can filter by all parameters, such as ID, name, alarm class, priority, etc.

This operating instruction introduces the process for configuring a filter using an example.

#### Requirement

- The "Alarm control" object is selected in the screen.
- The Inspector window is open.

#### Procedure

1. In the Inspector window under "Properties > Filter", click on the "..." button in the "Static value" column.

   The "Alarm filter configuration" dialog box opens.

   ![Procedure](images/135575887627_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/135575887627_DV_resource.Stream@PNG-en-US.png)
2. Click "<Add>" in the "AND/OR" column to create a filter.
3. In the "Criterion" column, open the selection list and select the entry "Alarm class".
4. In the "Operand" column, open the selection list and select the entry "Equal to".
5. Enter the value "Alarm" in the field of the "Setting" column.
6. Click the "OK" button.

**Note**

The following characters cannot be used in the Settings column:

- Quotes
- Single quotation marks

| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| You can also create filter criteria directly in runtime and use them as filters. To operate the filter in runtime, enable the "Visibility" property under "Properties > Toolbar > Elements > Control bar button Selection display [26]". |  |

#### Examples of alarm filters

| Example | Criterion | Condition | Setting | Description |
| --- | --- | --- | --- | --- |
| Filter by alarm class | "Name of alarm class" | = | Alarm | Displays the alarms that belong to alarm class "Alarm". |
| Filter by priority | Priority | Greater than | 4 | Displays the alarms with priority greater than 4. |
| Filter by alarm text | "Alarm text" | Contains | Motor_12 | Displays the alarms that contain the alarm text "Motor_12". |
| Filter by time | Last modification | Less than or equal to | Wednesday, 15 April 2020 17:00 | Displays the alarms that occurred after 5 pm (17:00) on 15 April 2020. |

#### Filter by time

If the time base of the alarm control is changed, the start value and stop value for filtering by time are not adjusted automatically.

**Example**

At the location of the PC with time zone "UTC + 1h", the alarm control has the "Local time zone" time base. If you filter by the time 10:00 to 11:00 and then change the time base to "UTC", you must change the start value and stop value of the filter to 9:00 and 10:00 to display the same alarms as before.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified-1)
  
[Configuring the toolbar (RT Unified)](#configuring-the-toolbar-rt-unified)
  
[Configuring columns and sorting (RT Unified)](#configuring-columns-and-sorting-rt-unified)
  
[Configuring the export of alarms (RT Unified)](#configuring-the-export-of-alarms-rt-unified)
  
[Displaying logged alarms (RT Unified)](#displaying-logged-alarms-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)

### Configuring the export of alarms (RT Unified)

#### Introduction

To export alarms to a "*.csv" file in runtime, click on the "Export" button in the alarm control. You configure the "Export" button in the alarm control in the "Screens" editor.

#### Requirement

- The screen with the configured alarm control is open.
- The Inspector window is open.

#### Procedure

To configure the export of alarms, proceed as follows:

1. Select the alarm control and enable the "Visibility" property in the Inspector window under "Properties > Toolbar > Elements > Export button".

You define the export settings, such as the file name, the scope of the export and the format, in runtime in the "Export data" dialog.

---

**See also**

[Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified-1)
  
[Configuring the toolbar (RT Unified)](#configuring-the-toolbar-rt-unified)
  
[Configuring columns and sorting (RT Unified)](#configuring-columns-and-sorting-rt-unified)
  
[Configuring filters in the alarm control (RT Unified)](#configuring-filters-in-the-alarm-control-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Displaying logged alarms (RT Unified)

#### Overview

If an alarm log has been created, an alarm control in runtime also displays logged alarms.

The buttons relevant for logging, "Show logged alarms" and "Show and update logged alarms", are enabled in the alarm control by default and can be operated in runtime.

You display logged alarms in runtime using these buttons.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Basics of alarm logging (RT Unified)](#basics-of-alarm-logging-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Configuring the alarm control (RT Unified)](#configuring-the-alarm-control-rt-unified-1)
  
[Configuring the toolbar (RT Unified)](#configuring-the-toolbar-rt-unified)
  
[Configuring columns and sorting (RT Unified)](#configuring-columns-and-sorting-rt-unified)
  
[Configuring filters in the alarm control (RT Unified)](#configuring-filters-in-the-alarm-control-rt-unified)
  
[Configuring the display of security events (RT Unified)](#configuring-the-display-of-security-events-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)

### Configuring alarm statistics (RT Unified)

#### Introduction

The alarm statistics shows statistical calculations for logged alarms in the alarm control. The alarm statistics also shows a selection of the configured alarm blocks. If there is dynamic content, the alarm blocks show the data of the alarm last arrived. The columns of the alarm statistics can be arranged individually.

The alarm statistics shows the following statistical calculation types:

- Frequency of an alarm

  The system counts the number of occurrences of an alarm with "active" status in the log. If the alarm number is not found, this alarm number is not included in the statistics.
- Total display time of an alarm in seconds

  You can calculate the following time periods between alarm states:

  - Sum active active
  - Sum active inactive
  - Sum active acknowledged
- Average display time of an alarm in seconds

  You can calculate the following time periods between alarm states:

  - Average active active
  - Average active inactive
  - Average active acknowledged

There is a column available in the alarm statistics for each type of calculation.

The calculation of the time of acknowledgment includes the "acknowledged" alarm status. This "acknowledged" alarm state includes the acknowledgment by the controller.

#### Requirement

- The "Alarm control" object is selected in the screen.
- The Inspector window is open.

#### Setting up columns of the alarm statistics

To set up the alarm statistics columns, proceed as follows:

1. Click "Properties > Miscellaneous > Alarm statistic - view > Columns" in the Inspector window.
2. Select the "Visibility" option for the desired columns.

#### Settings for calculating the alarm statistics

You can configure the following options:

| Setting | Description |
| --- | --- |
| Start time | Start time for the calculation. |
| Time range start | - Now   The current time is displayed as the start time of the calculation. - Fixed   The start time of the calculation can be changed as required. |
| Time range base | Unit of time for the calculation. The following settings are available:  - Undefined   The default time unit "Minute" is used with this setting. - Millisecond - Second - Minute - Hour - Day - Month - Year |
| Time range factor | The time range factor depends on the "Time range base" setting. For example, if the number 4 is set for the time range factor and "Minutes" is set for the time range base, all alarms that are logged within this period will be evaluated. |

To configure the settings for the alarm statistics, proceed as follows:

1. Click "Properties > Miscellaneous > Alarm statistic - settings" in the Inspector window.
2. Specify the desired properties.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Configuring the display of system diagnostics alarms (RT Unified)

#### Introduction

System diagnostics alarms are installed with STEP 7 and are used to monitor states and events of a controller. To display system diagnostics alarms in an alarm control in runtime, configure first in STEP 7 and then in WinCC.

> **Note**
>
> WinCC only supports system diagnostics alarms of a SIMATIC S7-1500 controller. WinCC also supports only system diagnostic alarms that are automatically updated by the central alarm management in the controller.

#### Requirement

- There is an HMI connection between the HMI Device and a SIMATIC S7-1500 controller (as of firmware version 2.0).

#### Configuring the display of system diagnostics alarms in STEP 7

To configure the display of system diagnostics alarms in runtime in STEP 7, proceed as follows:

1. Open the "Device configuration" of the controller in the project tree.
2. In the "Device view" tab, select the CPU on the rack.
3. Select "Properties > General > System diagnostics" in the Inspector window.

   You will see that the option "Select system diagnostics for this device" is selected and cannot be cleared. Because the system diagnostics of the controller is always enabled.
4. Activate the option "Central alarm management in the PLC" in the Inspector window under "Properties > General > PLC alarms".

   The automatic update of system diagnostics alarms on the HMI device is enabled in the controller.
5. Open the "Common data" folder in the project tree and double-click "System diagnostic settings".

   The system diagnostic settings are opened. You see the predefined categories of system diagnostics alarms in the table under "Category":

   - "Error"
   - "Maintenance demanded"
   - "Maintenance required"
   - "About"
6. In the table under "Category", select the alarm categories that are to be displayed in the alarm control in runtime.
7. In the table under "Alarm class", assign project-wide alarm classes to the alarm categories.
8. Right-click the controller in the project tree and select "Compile > Hardware (rebuild all)" in the shortcut menu.

#### Configuring the display of system diagnostics alarms in WinCC

To configure the display of system diagnostics alarms in runtime in WinCC, proceed as follows:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Select the option "Automatic update" under "Alarms > Controller alarms".

   The automatic update of system diagnostics alarms on the HMI device is enabled in the HMI device.
3. Select the option "System diagnostics" under "Alarms > Controller alarms".

   The display of system diagnostics alarms in runtime is enabled.
4. Configure an alarm control.

#### Result

The system diagnostics alarms of the controller are displayed in the alarm control in runtime.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)
  
[Configuring automatic updates of PLC alarms on the HMI device (RT Unified)](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified)
  
[System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)

## Logging alarms (RT Unified)

This section contains information on the following topics:

- [Basics of alarm logging (RT Unified)](#basics-of-alarm-logging-rt-unified)
- [Size of a log entry in the alarm log (RT Unified)](#size-of-a-log-entry-in-the-alarm-log-rt-unified)
- [Assigning an alarm class (RT Unified)](#assigning-an-alarm-class-rt-unified)
- [Logging alarms in multiple languages (RT Unified)](#logging-alarms-in-multiple-languages-rt-unified)

### Basics of alarm logging (RT Unified)

#### Introduction

An alarm log is used to log alarms that occur in the monitored process. You can use alarm logging to analyze error states and to document the process. Essential business and technical insights into the operating state of a system can be extracted from a subsequent evaluation of the logged alarms.

Alarms of connected and appropriately configured PLCs are also logged and made available in all configured languages.

#### How it works

Each alarm is assigned to one alarm class. To ensure clarity with large amounts of data, it is possible to prioritize and configure alarm classes differently. Under "HMI alarms", you can assign logs to the alarm classes.

Alarm logs are created by the system in Runtime. If an error or limit violation occurs, for example, an alarm configured in the "HMI alarms" editor is output in Runtime. Each alarm event is logged, e.g. status change of the alarm from "incoming" to "acknowledged".

#### Content of the alarm log

In the alarm logs, alarms and their properties are saved in all configured languages. The time stamp of a logged alarm is always specified in standard UTC format (Coordinated Universal Time).

#### Displaying logged data

You can display the logged data in Runtime in the alarm control. To display logged data, use the "Show logged alarms" button in the alarm control.

---

**See also**

[Displaying logged alarms (RT Unified)](#displaying-logged-alarms-rt-unified)
  
[Creating a data log and an alarm log (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#creating-a-data-log-and-an-alarm-log-rt-unified)
  
[How it works (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#how-it-works-rt-unified)
  
[Log basics (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#log-basics-rt-unified)
  
[Storage locations of logs (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#storage-locations-of-logs-rt-unified)
  
[Editing log contents with scripts and system functions (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#editing-log-contents-with-scripts-and-system-functions-rt-unified)
  
[Size of a log entry in the alarm log (RT Unified)](#size-of-a-log-entry-in-the-alarm-log-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Size of a log entry in the alarm log (RT Unified)

The size of a log entry depends on the following factors:

- Number of configured languages

  You configure the languages to be logged in the Runtime settings of the HMI device.

  If more than one language is defined, memory is required for each additional language to store the language entry.
- Alarm texts and additional texts

  - Length of the alarm texts and the additional texts
  - Memory requirement of individual characters

    Symbols and complex characters have greater memory requirements.
- Database type used

#### Calculation

The size of a log entry is calculated as follows:

Basic entry without alarm text + Memory requirements of all texts + (Number of configured languages-1)*Memory requirement of an additional language entry

The text lengths and the memory requirements of the individual characters depend on the respective language. The following formula can be used to easily estimate the memory requirement of all texts:

Number of configured languages​*Total length of the alarm text and the additional texts*Memory requirement of one character

The individual values depend on the database type used.

|  | SQLite | Microsoft SQL |
| --- | --- | --- |
| Additional memory requirement per segment | - | Approx. 3.5 MB |
| Basic entry without alarm texts | Approx. 300 bytes | Approx. 2000 bytes |
| Memory requirement of an additional language entry | Approx. 100 bytes | Approx. 200 bytes |
| Memory requirements of a character | At least 1 byte | At least 2 bytes |

#### Recommended use of database types

The use of Microsoft SQL for alarm logs is recommended under the following conditions:

- Number of alarm states to be logged greater than 100 per second
- More than 26 million log entries must be available (excluding deleted log segments in the backup)

---

**See also**

[How it works (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#how-it-works-rt-unified)
  
[Logging alarms in multiple languages (RT Unified)](#logging-alarms-in-multiple-languages-rt-unified)
  
[Basics of alarm logging (RT Unified)](#basics-of-alarm-logging-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Assigning an alarm class (RT Unified)

#### Introduction

One alarm log each is assigned to predefined and user-defined alarm classes. In this way, you can categorize alarms in different logs.

> **Note**
>
> **Assigning an alarm class**
>
> If you do not assign an alarm class to an alarm log, you will receive an error message when you compile the project.
>
> Assign at least one alarm class to each alarm archive.

#### Requirement

- An alarm log has been created in the "Logs" editor.

#### Procedure

1. Double-click on the "HMI alarms" entry in the project tree.

   The "HMI alarms" editor is opened.
2. Select the "Alarm classes" tab.

   The list of alarm classes is displayed.
3. Double-click on an entry in the "Log" column.

   The selection button is displayed.
4. Select an alarm log.

---

**See also**

[Basics of alarm logging (RT Unified)](#basics-of-alarm-logging-rt-unified)
  
[Creating a data log and an alarm log (RT Unified)](Logging%20data%20%28RT%20Unified%29.md#creating-a-data-log-and-an-alarm-log-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Logging alarms in multiple languages (RT Unified)

#### Introduction

You can log alarm texts in different languages. To do this, select the option in the runtime settings of the HMI device.

#### Requirement

- The languages in which the alarm texts are to be logged are created as project languages.

#### Procedure

1. Open "Runtime settings" in the project tree below the HMI device.
2. Select "Language & Font".
3. To activate a language for runtime, select the check box in the "Activate" column.

   This option must be enabled in order to log alarm texts in the corresponding language.
4. To log the alarm texts in a specific language, select the check box in the "Enable for logging" column.

![Procedure](images/136199569419_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Activate available languages in Runtime |
| ② | Enabling languages for logging |
| ③ | Adding project languages |

---

**See also**

[Basics of alarm logging (RT Unified)](#basics-of-alarm-logging-rt-unified)
  
[Size of a log entry in the alarm log (RT Unified)](#size-of-a-log-entry-in-the-alarm-log-rt-unified)

## Displaying and using alarms (RT Unified)

This section contains information on the following topics:

- [Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
- [Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
- [Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
- [Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
- [Displaying alarm statistics (RT Unified)](#displaying-alarm-statistics-rt-unified)
- [Operating alarm statistics (RT Unified)](#operating-alarm-statistics-rt-unified)
- [Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
- [Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
- [Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
- [Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
- [Unshelving an alarm (RT Unified)](#unshelving-an-alarm-rt-unified)
- [Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)

### Operating the alarm control and displaying it in runtime (RT Unified)

#### Introduction

In Runtime, the alarm control displays alarms that occur during the process in a plant. You configure the alarm control in the Engineering System using the "Alarm control" object. Alarms indicate events and states on the HMI device which have occurred in the system, in the process, or on the HMI device itself. A state is reported when it occurs. Use the alarm control functions to work with incoming alarms. The following alarm events can occur for an alarm:

- Incoming
- Outgoing
- Acknowledge

The configuration engineer defines which alarms must be acknowledged by the operator.

![Introduction](images/105049094411_DV_resource.Stream@PNG-de-DE.png)

#### Alarm control

The alarm control displays selected alarms or alarm events from the alarm buffer or alarm log. Whether alarm events have to be acknowledged or not is specified in your configuration. You can configure the order in which the alarms are displayed. Either the current or the oldest alarm is displayed first.

In the alarm control, you can display various lists that filter and sort according to specific properties. To display the alarm lists in the alarm control and switch the alarm control in runtime, click the corresponding button on the alarm control function bar.

| Button | Description | Description |
| --- | --- | --- |
| ![Alarm control](images/132457983883_DV_resource.Stream@PNG-de-DE.png) | Show active alarms | Shows the pending alarms. |
| ![Alarm control](images/132458068107_DV_resource.Stream@PNG-de-DE.png) | Show logged alarms | Shows the logged alarms.  The display is not updated immediately when new incoming alarms occur. |
| ![Alarm control](images/132458075531_DV_resource.Stream@PNG-de-DE.png) | Show and update logged alarms | Shows the logged alarms.  The display is updated immediately when new incoming alarms occur. |
| ![Alarm control](images/132459375883_DV_resource.Stream@PNG-de-DE.png) | Show defined alarms | Shows the alarms configured in the Engineering System. |

> **Note**
>
> The maximum number of alarms that can be displayed in an alarm control in Runtime depends on the selected view. Note the information in the performance features.

#### Roles and authorizations

When working with the alarm control, you can assign roles and authorizations that determine who can configure in the Engineering System and operate it in runtime.

In the Engineering System under "Security Settings > Settings" you have the option to set the user name and password for the open project with which the project is now protected with "Protect this project". Under "Security settings > Users and roles" you create users under the "Users" tab, to whom you can assign roles as well as rights. In addition to the predefined roles, you can also define additional roles under the "Roles" tab and then assign them to a user.

#### Operator control with the mouse

**Selecting and controlling alarms**

- Click on an alarm.
- Click on a button in the function bar.

The function of the button is applied to the alarm.

**Reordering columns**

You have the option of changing the column order configured in the Engineering System. You can find additional information in the section [Rearranging columns in runtime](Configuring%20screens%20%28RT%20Unified%29.md#rearranging-columns-in-runtime-rt-unified).

**Sorting alarms by column**

You have the option of sorting the alarms by column. You can find additional information in the section [Sorting alarms in Runtime](#sorting-alarms-in-runtime-rt-unified).

#### Operator control with keyboard

Press <Shift + Enter> until the focus is on the alarm control. Then select the alarm to be edited and operate it using the function bar.

Use the following keys:

| Keyboard shortcut | Function |
| --- | --- |
| PAGE UP | Navigates up the alarm control row by row. |
| PAGE DOWN | Navigates down the alarm control row by row. |
| SHIFT + PAGE UP | Navigates the alarm control column by column to the left. |
| SHIFT + PAGE DOWN | Navigates the alarm control column by column to the right. |
| CTRL + UP | Sets the selection as the start of row. |
| CTRL + DOWN | Sets the selection as end of row. |
| CTRL + RIGHT | Sets the selection as start of column. |
| CTRL + LEFT | Sets the selection as end of column. |
| HOME | Sets the selection as the start of row. |
| END | Sets the selection as end of row. |

#### Display of date/time values in the alarm control

After the first download of a project, date/time values in the alarm control are shown in English time format by default. If your preferred language is not English, then switch the language once to English and back to your preferred language. After that, the date/time values are shown in the alarm control in your prioritized language.

#### Multiple selection of alarms on panels via touch gesture

**Requirement**

Configuration of the alarm control in the engineering system:

- Under "Properties > Miscellaneous > Alarm control > Selection - Mode", the "Multiple" entry is set for "Static value".
- The "Previous line" and "Next line" buttons are configured.

**Operation in runtime**

1. Tap an alarm in the alarm control.

   The alarm is selected.
2. To extend the selection by one or more previous alarms, tap the "Previous line" button until the desired alarms are selected.
3. To extend the selection by one or more subsequent alarms, tap the "Next line" button until the desired alarms are selected.

---

**See also**

[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Sorting alarms in Runtime (RT Unified)

#### Introduction

In runtime, you can sort the alarms in the alarm control by column header.

Sorting alarms:

- In descending order by date, time, and alarm number. The latest alarm appears at the top.
- Ascending

  For an ascending sort order, the following sequence is used:

  - Incoming
  - Incoming/acknowledged
  - Incoming/acknowledged/outgoing
  - Incoming/outgoing/acknowledged
  - Shelved
  - Suppressed
- No sorting

  When the alarm control is sorted by columns, an arrow and a number are shown on the right in the column header. The arrow indicates the ascending or descending sort order. The number beside the arrow indicates the sort order of the column headers.

#### Default sorting of alarms

- By priority

  If the "Priority" column is defined in the alarm control, sorting is based on alarm priority.

  As a result, in the case of a single-line alarm control, only the top-priority alarm appears in the alarm window. A lower-priority alarm is not displayed, even if it is more recent. The alarms are displayed in chronological order.
- If one of the following columns is configured in the alarm display, sorting on a Unified Comfort Panel is according to the specified order.

1. Priority
2. Modification time
3. Raise time
4. Alarm state

If none of the columns are configured, sorting occurs according to the "Time" column.

#### Requirement

- In the Engineering System, "Sorting - allow" is enabled in the alarm control for the respective columns.
- The "Visibility" and "Operator control - allow" settings are activated for the following alarm control buttons in the Engineering System:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132458826507_DV_resource.Stream@PNG-de-DE.png) | Sorting - configuration |
  | ![Requirement](images/132458366859_DV_resource.Stream@PNG-de-DE.png) | Alarms - show current |
- "Alarms - Show current" paused in runtime.

#### Sorting alarms by clicking on the column header

To sort alarms in the alarm control by column header, follow these steps:

1. In Runtime, click the column header of the alarm control you want to sort by.

   An arrow and a number are displayed in the column representing the order and method of sorting.

#### Sorting alarms via buttons

To sort alarms in the alarm control using the "Sorting - configuration" button, follow these steps:

1. In Runtime, click the "Sorting - configuration" button in the alarm control.

   The window for sorting opens.
2. Use the drop-down list to select a column and define whether you want to sort in ascending or descending order.
3. Apply your criteria via the "OK" button.

   The alarm control is sorted according to your criteria. The current sorting of the columns is indicated by an arrow and a number.

> **Note**
>
> To ensure that changes to existing sort criteria in the button are applied without errors, it is recommended that you first reset the changes using the "Clear sort criteria" button.

---

**See also**

[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Filtering alarms in Runtime (RT Unified)

#### Introduction

You can use criteria in Runtime to define which alarms you want to display in the alarm control. In the example below, only the alarms that contain the alarm text "Motor on" are displayed. To do this, use the "Selection display" button in the alarm control.

#### Requirement

- The "Visibility" and "Operator control - allow" settings are activated for the following alarm control buttons in the Engineering System:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132459557643_DV_resource.Stream@PNG-de-DE.png) | Selection display |

#### Procedure

To filter alarms in the alarm control, follow these steps:

1. Click "Selection display" in Runtime.

   The "Selection" dialog opens.
2. Under "Criterion" select the criterion "Alarm text".
3. Enter the alarm text "Motor on" in the "Settings" column.

> **Note**
>
> The following characters cannot be used in the Settings column:
>
> - Quotes
> - Single quotation marks

#### Result

The alarm control only shows those alarms that contain the words "Motor on" in the alarm text. If necessary, define additional filter criteria by selecting the required condition in the "AND/OR" column and the respective criterion in the "Criterion" column.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Configuring filters in the alarm control (RT Unified)](#configuring-filters-in-the-alarm-control-rt-unified)
  
[Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)

### Displaying logged alarms in Runtime (RT Unified)

#### Introduction

You can use the "Show logged alarms" and "Show and update logged alarms" alarm lists to display logged alarms.

#### Requirement

- An alarm log is configured.
- All the logged data that you intend to display in Runtime must be stored locally on the log server. The alarm log does not allow access to backup files held elsewhere, such as another PC in the network.
- The "Visibility" and "Operator control - allow" settings are activated for the following alarm control buttons in the Engineering System:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132458068107_DV_resource.Stream@PNG-de-DE.png) | Show logged alarms |
  | ![Requirement](images/132458075531_DV_resource.Stream@PNG-de-DE.png) | Show and update logged alarms |

#### Procedure

1. To display only logged alarms, click the "Show logged alarms" button in the alarm control:

   ![Procedure](images/105743986699_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/105743986699_DV_resource.Stream@PNG-de-DE.png)

   The alarm control shows the logged alarms. The display is not updated immediately when new incoming alarms occur.

   Each page shows a maximum of 1 000 alarms. Use the "Previous page" and "Next page" buttons for scrolling.
2. Click the "Show and update logged alarms" button in the alarm control to display logged and current alarms:

   ![Procedure](images/105743986699_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/105743986699_DV_resource.Stream@PNG-de-DE.png)

   The alarm control shows the logged alarms. The display is updated immediately when new active alarms occur.

   The alarm control shows a maximum of 100 alarms.

#### Limitation for the "Show logged alarms" alarm list

For log alarms with identical time stamps, it is possible in rare cases that log alarms are skipped when paging forwards and backwards.

To display the skipped alarms, page again, this time in the opposite direction.

**Example**

- The alarm log contains several 1 000 log alarms. Ten of the log alarms have an identical time stamp. The first five of these alarms are displayed at the end of the current page.

  The alarm control is sorted by time stamp in ascending order.
- Click on "Next page".

  The next 1 000 alarms whose time stamp is higher than the time stamp of the last alarm shown on the previous page are displayed.

  The remaining five alarms with identical time stamp are skipped when changing the page.
- Click on "Previous page".

  You will see all ten alarms with identical time stamps, as well as the next 990 alarms with lower time stamps.

> **Note**
>
> In the case of more than 1 000 log alarms with identical time stamps, not all skipped alarms can be displayed by paging in the opposite direction.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Displaying logged alarms (RT Unified)](#displaying-logged-alarms-rt-unified)
  
[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
  
[Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
  
[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Configuring the display of security events (RT Unified)](#configuring-the-display-of-security-events-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)

### Displaying alarm statistics (RT Unified)

#### Introduction

The alarm statistics represent statistical calculations of logged alarms.

![Introduction](images/139494878987_DV_resource.Stream@PNG-en-US.png)

You can use a button in the alarm control to export the alarm statistics to an Excel file.

> **Note**
>
> **Filter**
>
> A filter set in the alarm control is not effective in the alarm statistics.

> **Note**
>
> **Display options**
>
> Selected display options via the "Display options - setup" button in the alarm control have no effect in the alarm statistics.

#### Requirement

- Alarms are logged.
- For the following button of the alarm control, the "Visibility" and "Allow operator control" are enabled in the engineering system:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/139055173387_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics - view |

#### Procedure

To display the alarm statistics in Runtime, proceed as follows:

1. Click the "Alarm statistics - view" button in the alarm control.

#### Result

The alarms to be displayed in the alarm statistics are specified in the engineering system. Depending on the engineering system, the following columns are displayed:

| Column | Description |
| --- | --- |
| Number | Configured number of the alarm. |
| Frequency | Frequency of an alarm. The system counts the number of occurrences of an alarm with "active" status in the log. If the alarm number is not found, this alarm number is not included in the statistics. |
| Sum active active | Total display time of an alarm in seconds. The time period between the alarm states "active" and "active" is calculated. |
| Sum active inactive | Total display time of an alarm in seconds. The time period between the alarm states "active" and "inactive" is calculated. |
| Sum active acknowledged | Total display time of an alarm in seconds. The time period between the alarm states "active" and "acknowledged" is calculated. |
| Average active active | Average display time of an alarm in seconds. The time period between the alarm states "active" and "active" is calculated. |
| Average active inactive | Average display time of an alarm in seconds. The time period between the alarm states "active" and "inactive" is calculated. |
| Average active acknowledged | Average display time of an alarm in seconds. The time period between the alarm states "active" and "acknowledged" is calculated. |

The calculation of the time of acknowledgment includes the "acknowledged" alarm state. This "acknowledged" alarm state includes the acknowledgment by the controller.

> **Note**
>
> For the calculation, alarms with the status "acknowledged" and "inactive" are only used if a suitable alarm with the status "active" is found in the result set beforehand.
>
> If an alarm from the controller is pending and runtime is disabled and enabled several times, the alarm is entered into the log several times with the state "active". The alarm is also included multiple times in the calculation.

---

**See also**

[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Operating alarm statistics (RT Unified)

#### Introduction

Using the alarm statistics setup, you can change the settings for calculating the alarm statistics. The following settings are available:

| Setting | Description |
| --- | --- |
| Time range start | - Now   The current time is displayed as the start time of the calculation. - Fixed   The start time of the calculation can be changed as required. |
| Start time | Start time for the calculation. If the "Now" option is selected under "Time range start", the start time cannot be changed. |
| Time range base | Unit of time for the calculation. The following settings are available:  - Undefined   The default time unit "Minute" is used with this setting. - Millisecond - Second - Minute - Hour - Day - Month - Year |
| Time range factor | The time range factor depends on the "Time range base" setting. For example, if the number 4 is set for the time range factor and "Minutes" is set for the time range base, all alarms that are logged within this period will be evaluated. |

#### Requirement

- Alarms are located in the alarm log.
- For the following button of the alarm control, the "Visibility" and "Allow operator control" are enabled in the engineering:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/140319034891_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics - setup |
- The alarm statistics are selected in the alarm control.

#### Procedure

To display the alarm statistics setup in runtime, follow these steps:

1. Click on the "Alarm statistics - setup" button in the alarm control.

   The configuration opens.
2. Change the settings as required.
3. Click the "OK" button.

#### Result

The calculation of the alarm statistics is displayed according to the changed settings.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Acknowledging alarms (RT Unified)

#### Introduction

Pending alarms are acknowledged in Runtime depending on the configuration of your project and the defined alarm classes. The number of alarms to be acknowledged can be taken from the counter next to the "Single confirm" button or the status bar if it has been configured accordingly in the Engineering System for the alarm control. According to the acknowledgement model, different variants are available.

> **Note**
>
> If an operator authorization is configured for the operator controls, the alarms can only be acknowledged by authorized users.

#### Acknowledgment variants

In Runtime, you can acknowledge individual or multiple alarms. The following options are possible:

- Single acknowledgment

  Acknowledgment of an alarm using the "Single acknowledgment" button of the alarm control.
- Group acknowledgment

  Acknowledgment of all pending, visible alarms that require acknowledgment in the alarm control using the "Acknowledge visible alarms" button in the alarm control.
- Acknowledgment and confirmation

  When an alarm requires acknowledgment and confirmation, acknowledge that the alarm is incoming or outgoing. After the alarm has been cleared, reset the alarm using the "Single confirm" button of the alarm control.

#### Requirement

- The "Visibility" and "Operator control - allow" settings are activated for the following alarm control buttons in the Engineering System:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132458249611_DV_resource.Stream@PNG-de-DE.png) | Single acknowledgment |
  | ![Requirement](images/132458359435_DV_resource.Stream@PNG-de-DE.png) | Acknowledge visible alarms |
  | ![Requirement](images/132458428939_DV_resource.Stream@PNG-de-DE.png) | Single confirm |
  | ![Requirement](images/132458366859_DV_resource.Stream@PNG-de-DE.png) | Alarms - show current |

#### Procedure

To acknowledge an alarm in Runtime, follow these steps:

1. Click the "Alarms - show current" button in the alarm control.
2. Select the alarm.
3. Click "Single acknowledgment" in the alarm control.

#### Result

Depending on the state machine of the alarm class, the alarm receives the "Acknowledged" status. The alarm can also receive the state "outgoing" if the event for triggering an alarm is no longer pending.

---

**See also**

[Configuring alarm acknowledgment (RT Unified)](#configuring-alarm-acknowledgment-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
  
[Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
  
[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Group acknowledgment of alarms (RT Unified)

#### Introduction

A group acknowledgment is the acknowledgment of all pending, visible alarms and alarms that require acknowledgment in the alarm window. In Runtime, use the "Acknowledge visible alarms" button in the alarm control for this purpose.

#### Requirement

- The "Visibility" and "Operator control - allow" settings are activated for the following alarm control buttons in the Engineering System:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132458359435_DV_resource.Stream@PNG-de-DE.png) | Acknowledge visible alarms |

> **Note**
>
> The "Acknowledge visible alarms" button acknowledges all visible alarms only if no alarm is selected or highlighted.
>
> If an alarm is selected or highlighted, only the selected or highlighted alarm will be acknowledged after clicking the "Acknowledge visible alarms" button.

#### Procedure

For group acknowledgement of alarms in Runtime, follow these steps:

1. Read the alarm texts of the pending alarms and perform corrective actions, if necessary.
2. In the alarm control, click "Acknowledge visible alarms".

#### Result

All pending alarms with the following properties have been acknowledged:

- Requires acknowledgement
- Visible

---

**See also**

[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
  
[Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
  
[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Exporting alarms (RT Unified)

#### Introduction

In Runtime you can export the data directly from the alarm control, for example, for further processing or analysis. Use the "Export" button in the alarm control for this purpose.

#### Requirement

- The "Visibility" and "Operator control - allow" settings are activated for the following alarm control buttons in the Engineering System:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132458997003_DV_resource.Stream@PNG-de-DE.png) | Export |

#### Procedure

To export data from the alarm control in Runtime, follow these steps:

1. Click the "Export" button of the alarm control.
2. Under "File name" specify the file name of the export file.
3. Under "Scope of data export", you can specify which alarm control data is to be exported.
4. Under "Format" select the format of the export file.
5. Confirm with "OK".

#### Result

The export file appears in the browser download and can be downloaded.

---

**See also**

[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
  
[Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
  
[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Shelving alarms (RT Unified)

#### Introduction

You can shelve an alarm, for example, to prevent an alarm message from impairing the effectivity of your system. In Runtime, use the "Shelve alarm" button in the alarm control for this purpose.

> **Note**
>
> If an operator authorization is configured for these control elements, the alarms can only be shelved by authorized users.

#### Requirement

The following setups have been made in the Engineering System:

- The alarm list "Show defined alarms" is configured so that shelved alarms are displayed.
- The "Visibility" and "Operator control - allow" settings are activated for the following alarm control buttons in the Engineering System:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132459375883_DV_resource.Stream@PNG-de-DE.png) | Show defined alarms |
  | ![Requirement](images/132458989579_DV_resource.Stream@PNG-de-DE.png) | Shelve alarm |
  | ![Requirement](images/132459309323_DV_resource.Stream@PNG-de-DE.png) | Locked alarms - configuration |

#### Shelving alarms

To shelve an alarm in Runtime, follow these steps:

1. In the alarm control, select the "Show defined alarms" alarm list.
2. Select the alarm.
3. Click the "Shelve alarm" button.

#### Display shelved alarms

To display the currently shelved alarms in runtime, follow these steps:

1. In the alarm control, select the "Show defined alarms" alarm list.
2. Click the "Locked alarms - configuration" button.
3. Activate the option for shelved alarms.

---

**See also**

[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
  
[Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
  
[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Unshelving an alarm (RT Unified)

#### Introduction

An alarm that you have shelved can be released again at any time. In Runtime, use the "Unshelve alarm" button in the alarm control for this purpose.

> **Note**
>
> If an operator authorization is configured for these control elements, the alarms can only be shelved by authorized users.

#### Requirement

The following setups have been made in the Engineering System:

- The alarm list "Show defined alarms" is configured so that shelved alarms are displayed.

  Alternatively: If the "Visibility" and "Operator control - allow" settings are enabled for the "Locked alarms - configuration" button, you can use this button to change the alarm list configuration in Runtime.
- The "Visibility" and "Operator control - allow" settings are activated for the following alarm control buttons in the Engineering System:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132459375883_DV_resource.Stream@PNG-de-DE.png) | Show defined alarms |
  | ![Requirement](images/132458892555_DV_resource.Stream@PNG-de-DE.png) | Unshelve alarm |
  | ![Requirement](images/132459309323_DV_resource.Stream@PNG-de-DE.png) | Locked alarms - configuration |

#### Display shelved alarms

To display the currently shelved alarms in runtime, follow these steps:

1. In the alarm control, select the "Show defined alarms" alarm list.
2. Click the "Locked alarms - configuration" button.
3. Activate the option for shelved alarms.

#### Revoking shelved alarms

To unshelve an alarm in Runtime, follow these steps:

1. In the alarm control, select the "Show defined alarms" alarm list.
2. Select the alarm.
3. Click "Unshelve alarm".

---

**See also**

[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Disabling alarms (RT Unified)](#disabling-alarms-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
  
[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

### Disabling alarms (RT Unified)

> **Note**
>
> **No disabling or enabling of PLC alarms**
>
> Disabling or enabling of PLC alarms for an S7-1500 PLC is not supported.

#### Introduction

You can disable alarms to avoid an excessive burden of information for the plant operator. If only selected alarms are displayed, the operator can concentrate on the important alarms.

You can enable disabled alarms at any time. In runtime, you can use the "Disable alarm" and "Enable alarm" buttons in the alarm control for this purpose.

Disabled alarms are automatically visible again when Runtime restarts.

#### Requirement

The following setups have been made in the Engineering System:

- The alarm list "Show defined alarms" is configured so that disabled alarms are displayed.

  Alternatively: If the "Visibility" and "Operator control - allow" settings are enabled for the "Locked alarms - configuration" button, you can use this button to change the alarm list configuration in Runtime.
- The user is authorized to disable and enable alarms.
- The "Visibility" and "Operator control - allow" settings are enabled for the following alarm control buttons:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132459375883_DV_resource.Stream@PNG-de-DE.png) | Show defined alarms |
  | ![Requirement](images/132458742283_DV_resource.Stream@PNG-de-DE.png) | Disable alarm |
  | ![Requirement](images/132459726603_DV_resource.Stream@PNG-de-DE.png) | Enable alarm |
  | ![Requirement](images/132459309323_DV_resource.Stream@PNG-de-DE.png) | Locked alarms - configuration |

> **Note**
>
> The "Disable alarms" and "Enable alarms" authorizations must be configured directly one under the other. This is necessary because the authorization level used automatically for the "Enable alarms" authorization is directly below the "Disable alarms" authorization.

#### Properties of disabled alarms

The following applies to disabled alarms:

- Disabled alarms are not logged.
- When a disabled alarm is enabled again, it is checked by the system and, if the alarm cause still exists, displayed again.

#### Displaying disabled alarms

To display a disabled alarm in runtime, follow these steps:

1. In the alarm control, select the "Show defined alarms" alarm list.
2. Click the "Locked alarms - configuration" button.
3. Enable the option for disabled alarms.

#### Disabling alarms

To disable an alarm in Runtime, follow these steps:

1. In the alarm control, select the "Show defined alarms" alarm list.
2. Select the alarm.
3. Click the "Disable alarm" button.

   The alarm is removed from the alarm list.

#### Enabling alarms

To enable an alarm in Runtime, follow these steps:

1. In the alarm control, select the "Show defined alarms" alarm list.
2. Select the alarm.
3. Click the "Enable alarm" button.

---

**See also**

[Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
  
[Operating the alarm control and displaying it in runtime (RT Unified)](#operating-the-alarm-control-and-displaying-it-in-runtime-rt-unified)
  
[Sorting alarms in Runtime (RT Unified)](#sorting-alarms-in-runtime-rt-unified)
  
[Filtering alarms in Runtime (RT Unified)](#filtering-alarms-in-runtime-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified-1)
  
[Group acknowledgment of alarms (RT Unified)](#group-acknowledgment-of-alarms-rt-unified)
  
[Exporting alarms (RT Unified)](#exporting-alarms-rt-unified-1)
  
[Alarm control (RT Unified)](Configuring%20screens%20%28RT%20Unified%29.md#alarm-control-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

## Display security events (RT Unified)

This section contains information on the following topics:

- [Display security events on the HMI device (RT Unified)](#display-security-events-on-the-hmi-device-rt-unified)
- [Configuring the display of security events (RT Unified)](#configuring-the-display-of-security-events-rt-unified)

### Display security events on the HMI device (RT Unified)

#### Introduction

In addition to the existing alarms in WinCC, you can also view security events on the HMI device.

Security events are, for example, an attack on a device over the network, or a change of the protection level for communication between the controller and the HMI device.

Security events are detected by the controller and passed on to the HMI device. Security events are displayed in the alarm log on the HMI device.

It is not necessary to configure or activate the security event functionality within the controller. Security events are automatically detected by the controller.

#### Configuring the display of security events

The following steps are necessary to display security events on the HMI Device:

- Activation of PLC alarms
- Creation of an alarm log for PLC alarms

You can find more detailed information on configuration here: [Configuring the display of security events](#configuring-the-display-of-security-events-rt-unified)

#### Notes

- WinCC only supports security events of a SIMATIC S7-1500 controller.
- WinCC only supports security events that are automatically updated by the central alarm management in the PLC.
- Security events always use the "SystemInformation" alarm class.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Configuring the display of security events (RT Unified)](#configuring-the-display-of-security-events-rt-unified)
  
[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)
  
[Logging alarms (RT Unified)](#logging-alarms-rt-unified)
  
[Alarm system (RT Unified)](#alarm-system-rt-unified)
  
[Alarms (RT Unified)](#alarms-rt-unified)

### Configuring the display of security events (RT Unified)

#### Requirement

- There is an HMI connection between the HMI Device and a SIMATIC S7-1500 controller (as of firmware version 2.0).
- The "Central alarm management in the PLC" option is enabled in the controller properties (the automatic update of security events on the HMI device is enabled in the controller).

#### Procedure

1. Open the "Runtime settings" of the HMI device.
2. Select the option "Automatic update" under "Alarms > Controller alarms".

   The automatic update of security events on the HMI device is enabled in the HMI device.
3. Select the option "Security events" under "Alarms > Controller alarms".

   The display by security events in runtime is enabled.

   > **Note**
   >
   > The "Security events" option is cleared by default and must be selected for each HMI connection.
4. Create a new alarm log in the "Log" editor under "Alarm logs".
5. Open an HMI screen.
6. Create an alarm control.

#### Result

The security events are displayed in the alarm log in Runtime.

---

**See also**

[Display security events on the HMI device (RT Unified)](#display-security-events-on-the-hmi-device-rt-unified)
  
[Configuring automatic updates of PLC alarms on the HMI device (RT Unified)](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified)
  
[Displaying logged alarms (RT Unified)](#displaying-logged-alarms-rt-unified)
  
[Displaying logged alarms in Runtime (RT Unified)](#displaying-logged-alarms-in-runtime-rt-unified)
  
[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)

## Sending complete alarms from the controller to the HMI device (RT Unified)

This section contains information on the following topics:

- [Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)
- [Configuring automatic updates of PLC alarms on the HMI device (RT Unified)](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified)

### Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)

#### Basics

In addition to alarms in WinCC, you can configure PLC alarms in STEP 7 and display them on your HMI device.

If PLC alarms are configured in STEP 7, an integrated HMI connection to a SIMATIC S7-1500 controller is established and an alarm is triggered on the controller, then the PLC alarms are automatically sent to the HMI device and updated in case of alarm changes (e.g. change to alarm text). This saves you time since you do not have to upload the configuration changes of the alarms to the HMI device separately. The HMI device does not need to exit Runtime operation when the alarms are changed.

The following PLC alarms can be sent to the HMI device:

- Program alarms
- ProDiag alarms
- GRAPH alarms
- System diagnostic alarms

The PLC alarms can be sent to the HMI device in their entirety if the corresponding settings are configured in the controller and on the HMI device. On the HMI Device, the option "Automatic update" under "Runtime settings > Alarms > Controller alarms" must be selected for the respective connection. You can find additional information on the settings at [Configuring automatic updates of PLC alarms on the HMI device](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified).

#### Device dependency

If the controller and the HMI device are configured accordingly, the PLC alarms from the following controller are sent automatically and completely to the HMI device when they occur:

- SIMATIC S7-1500 (firmware version 2.0 and higher)

#### Language settings

For alarms to be displayed in the correct language on the HMI device, the same three languages (or fewer) must be configured for the alarms in the controller and on the HMI device. You might have to coordinate the language selection with the configuration engineer.

If different languages are configured on the HMI device and in the controller, the HMI device in operation shows the alarm text "###Text missing###" instead of the PLC alarms.

#### Notes

- If the "Information only" option was activated for a program alarm in STEP 7, the program alarm uses the "Information" alarm class.
- PLC alarms that are automatically updated by the central alarm management in the controller cannot be shelved or manually suppressed.
- If a security event occurs, the "SystemInformation" alarm class is used.
- The alarm number of an alarm corresponds to the alarm ID in the controller.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Filtering PLCs alarm using display classes (RT Unified)](#filtering-plcs-alarm-using-display-classes-rt-unified)
  
[Configuring automatic updates of PLC alarms on the HMI device (RT Unified)](#configuring-automatic-updates-of-plc-alarms-on-the-hmi-device-rt-unified)
  
[Configuring the display of system diagnostics alarms (RT Unified)](#configuring-the-display-of-system-diagnostics-alarms-rt-unified)
  
[Display security events on the HMI device (RT Unified)](#display-security-events-on-the-hmi-device-rt-unified)
  
[User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)
  
[System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)

### Configuring automatic updates of PLC alarms on the HMI device (RT Unified)

#### Introduction

The "Automatic update" option is selected by default for a connection between a SIMATIC S7-1500 controller (firmware version 2.0 or higher) and an HMI device.

#### Requirement

- There is an HMI connection between the HMI Device and a SIMATIC S7-1500 controller (as of firmware version 2.0).
- The "Central alarm management in the PLC" option is enabled in the controller properties (the automatic update of PLC events on the HMI device is enabled in the controller).
- PLC alarms have been configured in STEP 7.
- An alarm control is configured on the HMI device.
- The same three languages (or fewer) are configured in the controller and on the HMI device for alarms.

#### Procedure

1. Open the "Runtime settings" of the HMI device.

   One or more connections to controllers are displayed under "Alarms > Controller alarms".
2. Activate the "Automatic update" option for the specific connection for which you want to display the PLC alarms.

   The "Automatic update" option must be selected separately for each connection.

> **Note**
>
> If the language of an alarm text is not available on the HMI device, the alarm text '##Text missing##' is displayed.

#### Result

The PLC alarms are displayed in the alarm control in runtime.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)
  
[Filtering PLCs alarm using display classes (RT Unified)](#filtering-plcs-alarm-using-display-classes-rt-unified)
  
[Configuring the display of system diagnostics alarms (RT Unified)](#configuring-the-display-of-system-diagnostics-alarms-rt-unified)
  
[Configuring the display of security events (RT Unified)](#configuring-the-display-of-security-events-rt-unified)
  
[User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)
  
[System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)
  
[Workflow for configuring alarms (RT Unified)](#workflow-for-configuring-alarms-rt-unified)

## Reference (RT Unified)

This section contains information on the following topics:

- [Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
- [System alarms (RT Unified)](#system-alarms-rt-unified-1)

### Alarm terminology (RT Unified)

| WinCC Engineering | WinCC Runtime | DIN 19235 | DIN EN 62682 | Description |
| --- | --- | --- | --- | --- |
| Analog alarm | Analog alarm | Analog alarm | Absolute alarm | An alarm that is triggered when a limit value is exceeded. |
| Discrete alarm | Discrete alarm | Discrete alarm | Discrete alarm | An alarm that is triggered when digital signals match a specified pattern during an ongoing process. |
| Suppressed by design |  |  | Suppressed by design | An alarm is not signaled based on a condition. |
| Event |  |  | Event | An event represents a requested or unrequested status change. |
| Initial alarm |  | Initial alarm | Initial alarm | An alarm that is selected first after the last acknowledgment from a number of alarms. |
| Outgoing |  |  | Inactive | The condition for triggering an alarm is no longer fulfilled.  Can also be displayed in Runtime with Cleared. |
| Outgoing alarm |  | Outgoing alarm | Inactive alarm | The alarm is no longer displayed because the triggering condition is no longer fulfilled. |
| Incoming |  |  | Active | The condition for triggering an alarm is fulfilled.  Can also be displayed in Runtime with Raised. |
| Locked alarm | Disabled alarm | Locked alarm | Locked alarm | An alarm that is blocked by interlocking. |
| Alarm group |  | Group of alarms | Alarm group | A group of alarms with a shared assignment. This assignment can be, for example, the process area or the equipment group. |
| Incoming alarm |  | Incoming alarm | Active alarm | An alarm that is displayed when the triggering condition is fulfilled. |
| Alarm log |  |  | Alarm log | A long-term log for alarm logging. |
| Alarm filter |  |  |  | Criteria that limit the display of alarms in the alarm control. |
| Alarm list | Alarm summary |  | Alarm list | A display that lists the signaled alarms with selected information (e.g. date, priority, and alarm type). |
| Alarm type |  |  | Alarm type | An alarm attribute that permits differentiation of the alarm condition (e.g. alarm with low or high process value). |
| Alarm procedures |  | Alarm procedures | Alarm procedures | An alarm procedure monitors the plant. The alarms of the individual alarm procedures are triggered in various ways. |
| Alarm |  | Alarm | Alarm | Acoustic or visual information about the malfunction. |
| Alarm control |  | Alarm control | Alarm control | The alarm control displays the alarms that occur during the process in a plant. |
| Alarm class |  | Alarm class | Alarm class | A group of alarms with a shared set of management requirements (e.g. safety requirements). |
| Alarm priority |  | Alarm priority | Alarm priority | The relative significance that is assigned to an alarm in an alarm system and that represents the urgency of the alarm. |
| Alarm report |  |  | Alarm report | A report of the logged or pending alarms. |
| New value alarm |  | New value alarm |  | An alarm processing that highlights from a number of alarms those alarms whose state has changed since the last acknowledgment. |
| Acknowledgment |  | Acknowledgment | Acknowledgment | Operator activity that confirms the acknowledgment of the alarm. |
| Feedback |  | Feedback |  | The feedback confirms a command, a status or a condition. The feedback also indicates whether a change or a status change has occurred. |
| Deadband |  |  | Deadband | The deadband suppresses the noise component in the settled controller state of the PID controller. |
| Suppressed alarm | Shelved alarms | Suppressed alarm | Suppressed alarm | An alarm that is blocked by interlocking. |
| Alarm annunciator |  | Alarm annunciator | Alarm annunciator | A device or device group that alerts the operator about changes in the process conditions. |

### System alarms  (RT Unified)

This section contains information on the following topics:

- [System alarm basics (RT Unified)](#system-alarm-basics-rt-unified)
- [System alarms S7Plus (RT Unified)](#system-alarms-s7plus-rt-unified)
- [System alarms parameter sets (RT Unified)](#system-alarms-parameter-sets-rt-unified)
- [System alarm reporting (RT Unified)](#system-alarm-reporting-rt-unified)
- [System alarms scripting (RT Unified)](#system-alarms-scripting-rt-unified)
- [System alarms communication (RT Unified)](#system-alarms-communication-rt-unified)
- [System alarms VCS (RT Unified)](#system-alarms-vcs-rt-unified)
- [System alarms Runtime (RT Unified)](#system-alarms-runtime-rt-unified)

#### System alarm basics  (RT Unified)

##### System alarms

System alarms provide information on the HMI device about the internal states of the HMI device and controller.

The following overview illustrates when a system alarm occurs and how to eliminate the cause of error.

> **Note**
>
> System alarms are output in an alarm control. System alarms are output in the language currently set on your HMI device.

##### System alarm parameters for HMI devices

System alarms are nested, tag-based alarms. They are defined in a SystemData template for S7 Plus in the template for the S7 Plus HMI connection. Whenever engineering creates an S7 Plus HMI connection, a nested alarm is also created.

As of version V18, system alarms must have a constant alarm ID. Therefore, each component gets its own range of numbers.

> **Note**
>
> The ID of the alarm must be constant.

##### Standard languages for system alarms

Texts of system alarms are available in the following languages by default:

- English (US)
- German (Germany)
- Chinese (PR China)
- French (France)
- Italian (Italy)
- Spanish (Spain)

If you want to output system alarms in other languages, you can create texts in the language manually.

> **Note**
>
> If you disable a non-standard language in the project, manually created system alarm texts may be lost. To avoid such loss, export the system alarm texts before disabling them.

Another option is to export the system alarm texts in a standard language and change the language name in the xlsx file to the target language (e.g. en-US to en-GB). Make desired changes to the texts and then import the xlsx file to add the system alarm texts in the target language.

---

**See also**

[Alarm terminology (RT Unified)](#alarm-terminology-rt-unified)
  
[Exporting project texts (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#exporting-project-texts-rt-unified)
  
[Importing project texts (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#importing-project-texts-rt-unified)
  
[Configuring the status texts of alarms (RT Unified)](#configuring-the-status-texts-of-alarms-rt-unified)
  
[Editing system alarms (RT Unified)](#editing-system-alarms-rt-unified)
  
[Configuring in multiple languages (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#configuring-in-multiple-languages-rt-unified)

#### System alarms S7Plus (RT Unified)

##### System alarms S7Plus

The following is a list of the most important system alarms.

| ID | Alarm text | Effect/cause | Solution |
| --- | --- | --- | --- |
| 537526273 | Computer1 [@5%s@]: @3%t#2T@ | The connection to a S7-1200/1500 PLC could not be established.  Possible causes:  - General connection problems (cable not plugged in, PLC switched off, network component interrupted). - Failed authentication on the PLC side (wrong or invalid password). - Connection certificate error (wrong or invalid connection certificate). - Connection resources are exhausted.     1. Error from the lower-level communication level.  - Error on HMI side - Error on PLC side or network   - Not connected   - Access denied   - Authentication failed   2. General error with the connection certificate.  - OpenSSL has encountered an error while checking the connection certificate. The detail error message contains the OpenSSL error code.   3. The connection certificate used has expired.  - The alarm text contains the name of the certificate.   4. The connection certificate used has been revoked.  5. The connection certificate has not been trusted, but manual trust is possible.  6. The connection certificate has not been trusted, manual trust is not possible. | Check that the S7-1200/1500 PLC and/or HMI station has no problems.  Check if the cable is plugged in, the PLC is switched on and the network component is not interrupted.   Check if the password is correct and valid.  Check if the IP address is correct and pinging the IP address is possible.  Check the S7Online access point.  Check the validity of the certificate. |
| 537526274 | Computer1 (@2%s@): Partner is not fully operational. | The S7-1200/1500 PLC is not in RUN mode.  The HMI station is connected to the PLC, but the internal PLC program is not executed. | Check that the S7-1200/1500 PLC has no problems.  Bring the S7-1200/1500 into the RUN mode. |
| 537526275 | The PLC does not support the central alarm management. | System diagnostic alarms have been configured for the S7-1200/1500 PLC, but the PLC does not support full-text alarms. | Check the PLC configuration.  Upgrade the S7-1200/1500 PLC to a firmware version that supports full text alarms, or deselect the "Automatic update" setting. |
| 537526276 | Overload of PLC resources for monitoring HMI tags. Maximum PLC resources - @2%s@. | The S7-1200/1500 PLC communication resources for HMI tags are overloaded.   The communication resources required for cyclic monitoring are more than the PLC has available. Instead, cyclic read requests are used for the resources that are not available. This leads to increased communication load.  Time delays on HMI and PLC are to be expected.  The alarm is triggered by an overload of 50% which is caused by the local HMI station. | Check the number of tags used simultaneously with the resources of the S7-1200/1500 PLC for cyclic jobs.  Check if other HMI stations are connected to the S7-1200/1500 PLC. |

#### System alarms parameter sets (RT Unified)

##### 2000 - System alarm parameter sets

The following is a list of the most important system alarms.

| ID | Alarm text | Effect/causes |
| --- | --- | --- |
| 537657345 | Parameter set [Name/ID]: Transfer to PLC successfully completed | The parameter set was successfully written from the memory to the PLC. |
| 537657346 | Parameter set [Name/ID]: Transfer to PLC aborted with error | The alarm appears in the following situations:   - A parameter set type with the name or ID does not exist in Runtime. Transfer to the PLC has been aborted. - A parameter set with the name or ID does not exist in Runtime. Transfer to the PLC has been aborted. |
| 537657347 | Parameter set [Name/ID]: Transfer from PLC successfully completed | The parameter set was successfully loaded into memory by the PLC. |
| 537657348 | Parameter set [Name/ID]: Transfer from PLC aborted with error | The possible causes are as follows:  - If a parameter set with the name or ID exists in Runtime, the values of the parameter set in the memory are overwritten with the values read by the PLC. - The transfer of PLC failed during the unsuccessful PLC connection. |
| 537657349 | Parameter set [Name/ID] not available: | A parameter set type with the name or ID is not available in Runtime. |
| 537657350 | Parameter set [Name/ID] not available | A parameter set with the name or ID is not available in memory. |
| 537657351 | Parameter set [Name/ID]: Import failed | The possible causes are as follows:  - The path specified for the import file cannot be accessed. - The header in the import file is incorrect. - Specified import parameters are not available in the import file. - Checksum validation failed if checksum was activated during import. |
| 537657352 | Parameter set [Name/ID]: Import successfully completed | The parameter set was successfully imported from a file. |
| 537657353 | Parameter set [Name/ID]: Export failed | The path specified for the export file cannot be accessed. |
| 537657360 | Parameter set [Name/ID]: Export successfully completed | The parameter set was successfully exported to a file. |
| 537657361 | Invalid checksum: Import failed | Checksum validation failed due to a change in the import file. |
| 537657362 | Import successfully completed | All parameter sets were imported successfully. |
| 537657363 | Import failed | The path specified for the import file cannot be accessed. None of the parameter sets present in the import file were imported. |
| 537657364 | Import partially completed | Not all parameter sets present in the import file could be imported. A possible cause is that the values of the elements cannot be imported, e.g. the value is not within the value range of the elements or the value does not correspond to the configured data type or data format. |
| 537657365 | Export successfully completed | All parameter sets available in Runtime have been exported to the file. |
| 537657366 | Export failed | The path specified for the export file cannot be accessed. |

#### System alarm reporting (RT Unified)

##### System alarm reporting

The following is the list of the most important system alarms.

| ID | Alarm text | Effect/causes | Solution |
| --- | --- | --- | --- |
| 538640385 | Initialization of the reporting service failed | Initialization of the reporting service fails. | Contact Siemens customer service. |
| 538640386 | Report Data Provider cannot be started | The data provider for reports could not be started. | Contact Siemens customer service. |
| 538640387 | The report cannot be started for the job [name]. | The Report Creator for report jobs cannot be started. | Check the report job settings.  If you use the "ExecuteReport" system function, check the name of the report job and the parameters passed when calling the function. |
| 538640388 | An error occurred during communication with the database server | The reporting database cannot be found or access is not possible for other reasons. | Check whether the reporting database is available at the storage location configured in the Runtime settings in engineering.  Examples:   - Does the folder specified as storage location in the Runtime settings exist? - Has the folder been specified in the correct notation? - On a panel: Is the SD card plugged in? |
| 538640389 | The creation of the report job [name] failed | The Report Creator is missing information about the report job.   A possible reason for this are problems with processing the report template. | Check the report job settings and the report template. |
| 538640390 | Report failed | Report Creator reports an error while generating the report. | Check the detailed error message for the report:   Control "Reports" > "Reports" tab > "Status" column. |

#### System alarms scripting (RT Unified)

##### System alarms scripting

The following is a list of the most important system alarms.

| ID | Alarm text | Effect/cause | Solution |
| --- | --- | --- | --- |
| 537329665 | Script debugger is activated | The script debugger for screens is enabled in the Runtime Manager. | The alarm is cleared when the script debugger for screens is disabled in the Runtime Manager. |
| 537329666 | Script debugger is activated | Script debugger for the scheduled tasks is enabled in Runtime Manager. | This alarm is cleared when the script debugger for the scheduler is disabled in the Runtime Manager. |
| 537329667 | The alarm text is specified by the user via the script. | This alarm is triggered by the CreateOperatorInputInformation system function.  The alarm text always comes in the language selected by the user. | -- |
| 537329668 | The alarm text is specified by the user via the script. | This alarm is triggered by the CreateSystemAlarm system function.  The alarm text always comes in the language selected by the user. | -- |
| 537329669 | The alarm text is specified by the user via the script. | This alarm is triggered by the CreateSystemInformation system function. The alarm text always appears in the language selected by the user. | -- |

#### System alarms communication (RT Unified)

##### System alarms communication

The following is a list of the most important system alarms.

| Drivers | ID | Alarm text | Effect/cause | Solution |
| --- | --- | --- | --- | --- |
| AllenBradleyEIP | 538574849 | PLCDisconnectAlarm | The connection to the Allen-Bradley PLC could not be established. | Check if:  - The cable is connected - The PLC is switched on. - The network component is not interrupted. |
| 538574850 | Computer1 [Name]: Partner is not fully operational | The PLC is not fully operational. |  |  |
| Omron EIP | 538574851 | PLCDisconnectAlarm | The connection to the Omron PLC could not be established. | Check if:  - The cable is connected - The PLC is switched on. - The network component is not interrupted. |
| 538574852 | Computer1 [Name]: Partner is not fully operational | The PLC is not fully operational. |  |  |
| Mitsubishi MC | 538574853 | PLCDisconnectAlarm | The connection to the Mitsubishi MC PLC could not be established. | Check if:  - The cable is connected - The PLC is switched on. - The network component is not interrupted. |
| 538574854 | Computer1 [Name]: Partner is not fully operational | The PLC is not fully operational. |  |  |
| Mitsubishi IQ | 538574855 | PLCDisconnectAlarm | The connection to the Mitsubishi IQ PLC could not be established. | Check if:  - The cable is connected - The PLC is switched on. - The network component is not interrupted. |
| 538574856 | Computer1 [Name]: Partner is not fully operational | The PLC is not fully operational. |  |  |
| StdModbusTCP | 538574857 | PLCDisconnectAlarm | The connection to the Modbus PLC could not be established. | Check if:  - The cable is connected - The PLC is switched on. - The network component is not interrupted. |
| 538574864 | Computer1 [Name]: Partner is not fully operational | The PLC is not fully operational. |  |  |

#### System alarms VCS (RT Unified)

##### System alarms VCS

The following is a list of the most important system alarms.

| ID | Alarm text | Effect/cause | Solution |
| --- | --- | --- | --- |
| 537264129 | Computer1 (@2%s@): Manager (@1%s@) is not connected. | This alarm appears when execution of the visual core service (VCS) module is restricted.  The VCS module is responsible for all processes needed to display process pictures.  The possible causes are as follows:  - The processes crashed. - The processes could not be started. |  |

#### System alarms Runtime (RT Unified)

##### System alarms IOWA

The following is a list of the most important system alarms.

| ID | Alarm text | Effect/causes | Solution |
| --- | --- | --- | --- |
| 536870913 | Computer1[@1%s@]: System starting | The system is started. This alarm is triggered as soon as the system starts booting and cleared when this process is completed. | This alarm is cleared automatically as soon as the system is booted, i.e. when all managers listed in the progs file are booted (except managers that are started manually). |
| 536870914 | Computer1 [@1%s@]: System shutting down | The system is stopped. This alarm is triggered as soon as the system starts shutting down, and cleared when the system is restarted. | It is cleared automatically when the system starts up again. |
| 536870915 | Computer1[@S1%s@]: Delta activation in progress | This alarm indicates that a delta download is in progress. This alarm is set when the delta download is started and remains active until the delta activation is completed. | It disappears automatically as soon as the delta download is completed. No action is required by the operator. |
| 536870916 | Computer1 [@S1%s@]: Delta rollback in progress | This alarm appears when the delta activation has failed and a rollback of the changes has been triggered. It remains active while the rollback is executed and is reset afterwards. | The alarm disappears automatically as soon as the rollback and therefore the failed delta download is completed. No action is required by the operator. |
| 536870917 | Computer1 [@1%s@]: Low work memory | This alarm warns that the free physical work memory (RAM) will soon be exhausted. | Increase the work memory (RAM) or reduce the load. |
| 536870918 | Computer1 [@1%s@]: Very low work memory | This alarm warns that the free physical work memory (RAM) is critically low. | Increase the work memory (RAM) or reduce the load. |
| 536870919 | Computer1 [@1%s@]: Low hard disk space | This alarm warns that the free memory space will soon be exhausted. | Delete the data that is not required. |
| 536870920 | Computer1 [@1%s@]: Very low hard disk space | This alarm warns that the free memory space is no longer sufficient. | Delete the data that is not required. |
| 536870921 | Computer1 [@2%s@]: Manager [@1%s@] is not connected. | This alarm indicates that the connection to the Service Manager has been lost. | Check the network connection or the status of the manager. The system attempts to establish a connection on its own. |
| 536870922 | Computer1 [@2%s@]: Service [@1%s@] is not being executed. | This alarm indicates that the connection to a service instance has been lost. | Check the network connection or the status of the manager. The system attempts to establish a connection on its own. |
| 536870923 | Online backup in progress | This alarm is displayed when the online backup operation is performed. It remains set until the online backup is completed. | The alarm disappears automatically when the online backup is completed or aborted with an error. No action is required by the operator. |
| 536870924 | SystemManagerAlarm | This alarm indicates that the System Manager has lost its connection to the Event Manager. | Check the network connection or the status of the manager. The system attempts to establish a connection on its own. |
| 536870925 | RedundancyLossAlarm | This alarm indicates that there is currently no established connection to the redundant partner. This may be because the connection to the other host has been lost or because the connection has not yet been established (other host not running, network problem). | Check the network connection and whether the other host was started with the correct configuration.  The system attempts to establish a connection on its own. |
| 536870926 | RuntimeVersionDifferent | This alarm appears when a redundantly configured system is started with two different Runtime versions on the two hosts.  The "RuntimeVersion" configuration entry is different on the peers, which means that different software versions are installed on the two hosts. | Check the Runtime version value in the configurations on both devices and ensure that the correct software versions are being used.  Update the incorrect hosts to the correct Runtime version. |
| 536870927 | Computer1 [@S1%s@]: Connection ID: @S7%u@, Connection status: @2%u@ | This alarm indicates that the connection status between the driver and the PLC has changed. |  |
| 536870928 | Computer1 [@S1%s@]: @5%t#4T@ | This alarm appears when a configuration error has been detected by a component. | The component should describe the problem in detail so that the user can make the required changes in the configuration. |
| 536870929 | Computer1 [@S1%s@]: Successful rollback after failed activation. | This alarm is displayed when a delta download attempt fails and the changes are not activated. | There can be several reasons why the delta download process fails. The detailed reason should help identify the problem. Common problems include configuration issues within the delta project, incompatibility with the currently running project, requirements for a delta download are not met (such as a mandatory manager not running), another process is running that is preventing the delta download from running. |
| 536870930 | Computer1 [@S1%s@]: Delta rollback failed | This alarm is displayed when a problem is detected in a component during a delta download and a rollback is initiated. However, this rollback also fails for unexpected reasons. Consequently, this may result in a project that is in an inconsistent state. | The project may be in an inconsistent state. Perform a full download to return to a consistent project. |
| 536870931 | Computer1 [@S1%s@]: Saving of configuration changes has failed. | This alarm is displayed when saving configuration changes fails.   Writing the changes was unsuccessful and the changes are lost after shutdown. | Check whether the required write rights have been granted for the project folder. |
| 536870932 | Computer1 [@S1%s@]: Merging of the RDF files has failed: @2%s@ | This alarm indicates that the Runtime configuration data consolidation (RDF merge) failed. | Verify that the required authorizations have been granted for the project folder and that the files in the project are not locked by other processes. |
| 536870933 | Computer1 [@S1%s@]: Delta activation has failed. The file system is damaged. | This alarm is activated when a delta download was successfully activated, but the delta build number could not be added to the permanent list of activated deltas. | Verify that the required authorizations have been assigned to the project folder and that the files in the project are not locked by other processes, especially the delta list file in the deltas subdirectory. |
| 536870934 | Computer1 [@S1%s@]: A leap in time of @2%1.3f@ seconds was determined. | This alarm indicates that a time jump has occurred. Do not change the system time. | Check the device battery and system time. |
| 536870935 | Runtime Collaboration: @2%t#<RuntimeCollaborationFailureReason.1>@ during the connection of computer1 [@S1%s@] with system @5%u@ [@6%s@] to @4%s@. | This alarm indicates an unsuccessful connection attempt of the Dist Manager to another system with the cause of the error specified in the alarm text. There can be several reasons why a connection attempt fails. Common problems that can occur: Target system not available, certificate problems, wrong system ID or name configured for the target, time synchronization problem. | The alarm text, which includes the reason for the error and information about the connection attempt, should help identify the problem. - If the target system is not available: Check if the target system is running with correct configurations (Dist and, if necessary, Proxy Manager are started), check for network errors (check if the device itself is reachable, the ports used are open) - Certificate problems: Check if both client and server system have correct and valid certificates.  Incorrect system ID or name: The client system has a mismatched configuration to the target system (server), where either the system ID or name differs from the actual ID or name of the system. - Time synchronization problem: The system time difference between the two systems is greater than the maximum allowed difference. |
| 536870936 | Computer1 [@2%s@]: Loading of the configuration data created in Runtime has failed: @3%s@ | This alarm indicates that configuration data created through Runtime engineering or by the Runtime itself could not be loaded.  This data is stored in Runtime configuration files within the Runtime project and is read when Runtime is restarted. | Usually indicates a serious problem.   Problems with the storage medium itself or with corrupted files. |
| 536870937 | Computer1 [@S1%s@]: 'LoggingOverloadError' event was activated. | Outdated | Instead, use StorageSystemWriteDataLostAlarm_[StorageApplicationAbbreviation]. |
| 536870938 | Computer1 [@S1%s@]: User name: @S2%s@, Tag name: @2%s@, Old value: @3%v@, New value: @4%v@, Unit: @5%s@, Cause: @6%s@ | A value was changed by the user. | Audit Trail value change documentation. |
| 536870939 | Computer1 [@S1%s@]: User name: @S2%s@, Tag name: @2%s@, Old value: @3%v@, New value: @4%v@, Unit: @5%s@, Cause: @6%s@ | A value change by the user has not occurred. | Audit Trail value change documentation. |
| 536870940 | Computer1 [@S1%s@]: Online backup has failed | This alarm is triggered when an online backup was requested, but the operation fails. | The backup may fail for several reasons, which can be found in the detailed description. A mandatory manager may not be running, or may have been stopped during the backup, or there may be an access rights problem in the target directory.  Certain components may have also implemented their own logic for online backup that fails. |
| 536870941 | Computer1 [@S1%s@]: The certificate for @2%s@ was not found in the certificate memory. Details: @3%s@ | This alarm is triggered when a component cannot use certificates due to issues.  Either no certificate is configured or there is a problem with the public and/or private keys. | Check the configured certificates used by this component. |
| 536870942 | Computer1 [@S1%s@]: The certificate for @2%s@ will expire soon. Expiration date: @3%s@. Details: @4%s@ | This alarm is triggered when a component is using a certificate that is about to expire. The exact time depends on what the specific component has defined as soon to expire.  Usually, this alarm is triggered about 1 week before the expiration date. | Update the certificates used by the respective component. |
| 536870943 | Computer1 [@S1%s@]: The certificate for @2%s@ has expired. Expiration date: @3%s@. Details: @4%s@ | This alarm is triggered when a component attempts to use an expired certificate. | Update the certificates used by the respective component. |
| 536870944 | SystemDistributionManagerAlarm | This alarm indicates that the connection to the Distribution Manager has been lost. | Check the network connection or the status of the manager.  The system attempts to establish a connection on its own. |
| 536870945 | Computer1 [@2%s@]: Driver [@1%s@] Overload warning. | This alarm indicates that the driver can no longer continuously process the number of value changes it receives from the PLC. This state can be temporary or permanent. Received values are temporarily stored by the driver and processed at a later time. | If this occurs only temporarily, it is enough to wait. If this occurs more frequently, then using another driver can share the load between the two drivers and thus prevent the problem.   It could also be an indication that the event manager can no longer handle the number of value changes. In this case, the driver is storing the value changes, which in turn can cause an overload condition with this driver. |
| 536870946 | Computer1 [@2%s@]: Driver [@1%s@} Overload has occurred. | This alarm indicates that the driver can no longer cope with the number of value changes it receives from the PLC. This state can be temporary or permanent. In this case, it cannot be excluded that values are lost. | If this occurs only temporarily, it is enough to wait. If this occurs more frequently, then using another driver can share the load between the two drivers and thus prevent the problem.   It could also be an indication that the event manager can no longer handle the number of value changes. In this case, the driver is storing the value changes, which in turn can cause an overload condition with this driver. |
| 536870948 | Computer1 [@2%s@]: Manager [@1%s@] is not connected. | This alarm indicates that the driver has lost its connection to the Event Manager. | Check the network connection or the status of the manager.  The system attempts to establish a connection on its own. |
| 536870949 | DiskSpaceWarning | This alarm indicates that the configured limit for free space on the external storage medium has been exceeded. | Delete the data that is not required.  Expand the external storage medium. |
| 536870950 | DiskSpaceAlarm | This alarm warns that the free memory space on the external storage medium is no longer sufficient. | Delete the data that is not required.  Expand the external storage medium. |
| 536870951 | RemovableStorageMediumAlarm | This alarm indicates that a removable storage medium has been removed. | The alarm can be disabled for permanently installed data storage media. |
| 536870952 | High limit violated for tag @1%s@. Computer name: @S1%s@ | High limit violation for a tag value range. | The tag value is above the defined value range - check the cause. |
| 536870953 | Low limit violated for tag @1%s@. Computer name: @S1%s@ | Low limit violation of a tag value range. | The tag value is below the defined value range - check the cause. |
| 536870954 | MissingCRLAlarm | This alarm is triggered when the component that monitors CRLs cannot find the CRLs for the CA certificate file(s). The subject names of all relevant CAs are specified in the alarm. | Specify the missing CRLs. |
| 536870955 | ExpiredCRLAlarm | This alarm is triggered by the component that monitors CRLs when expired CRLs have been deployed. The subject names of all relevant CAs are specified in the alarm. | Renew the CRLs used. |
| 536871425 | Computer1 [@5%s@]: @3%t#2T@ | The connection to the S7 PLC was interrupted. | Check the S7 PLC and/or driver for problems.  Check if the IP address of the PLC is correct and pinging the IP address is possible. |
| 536871426 | Computer1 [@2%s@]: Partner is not fully operational. | The S7 PLC is in Stop mode. The driver is connected to the PLC, but the internal PLC program is not executed. | Check the S7 PLC for problems and bring the S7 to the "Run" mode if necessary. |
| 536871681 | PlcDisconnectedAlarm_OPCUA | The connection to the OPC UA server was interrupted. | Check the OPC UA server and/or driver for problems.   Check the connection between the OPC UA server and/or driver, especially if it is not blocked by a firewall. |
| 536871937 | Computer1 [@3%s@]: @1%s@ (@2%s@): has no connection to the logging system. | AlarmLogging service has lost the connection to the database.  This is probably due to an internal error of the database. If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the database server. In some cases, starting/restarting the database may solve the problem. Otherwise, the database log files can help to find the cause. |
| 536871938 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Log is full. | At least one storage medium used by the AlarmLogging service is full, so new value changes cannot be saved. If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the connected storage media and free some space on the devices that are (almost) full. Changing the log configuration can help reduce the amount of disk space needed by limiting the maximum amount of space a particular log can use before deleting data. |
| 536871939 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Insufficient resources of the logging system. | The database used by the AlarmLogging service is still running, but has reported that it has run out of resources (e.g. work memory, disk space).   No more writing is possible.  (Only applicable with Process Historian.) | Check the storage medium if it is out of space.   The database server logs can also help to find out the cause of the problem. Storage space problems can be caused by a high load that the system cannot handle. |
| 536871940 | Computer1 [@3%s@]: @1%s@: A write buffer overflow has occurred in log @2%s@. Data will be lost. | In the AlarmLogging service, the buffers are full and therefore some data has already been lost.  Possible causes:  - Infrastructure problem (e.g. connection abort, hard disk full, see other system alarms in this case). - Generally, a high load that cannot be handled by the system.   With redundant deployment, if only one host has this problem temporarily, the data from the other host is synchronized once the problem is resolved. | Correct the root cause of the problem.   If the problem is infrastructural, follow the instructions of the corresponding system alarm. If there is none, the cause is probably too much load on the system or write speed degradation (for example, slowing down of a storage medium).   Check the hardware elements, reduce the system load, or if it is a persistent problem, the hardware configuration may not be sufficient for the current project. |
| 536871941 | Computer1 [@2%s@]: @1%s@: The passive logging system has lost the connection to the active logging system. | The redundant databases used by the AlarmLogging service have lost connection to each other (triggered only on the passive host).  Possible causes:  - The active database is completely shut down. - A problem with the network connection.   If the StorageSystemPassiveSynchronizing alarm is also triggered, it means that the problem is corrected and the alarm is cleared as soon as synchronization is completed.  (Only applicable with Process Historian.) | Check the status of the active database.   If it does not run, try restarting it or analyze its log files to learn more about the problem.   If the database is running, ensure that the network connection between the two hosts is working. |
| 536871942 | Computer1 [@2%s@]: @1%s@: Synchronizing data | Logged data synchronization is in progress between the active and passive databases. Redundancy failover during this state may result in loss of logged data.   (Only applicable with Process Historian.) | This system alarm does not signify an error; it is normal behavior when the two redundant databases are synchronizing data. Therefore, no action is required.  As long as this system alarm is pending, you should not initiate redundancy failover, otherwise the logged data may be lost. |
| 536871943 | Computer1 [@2%s@]: @1%s@: Failover error | AlarmLogging service: An error occurred while the database was trying to switch roles between the active and passive databases. (Only applicable with Process Historian.) | Analyze the Process Historian log files to learn more about the reason for the failure. If other system alarms are also triggered, they may also be related. |
| 536871944 | Computer1 (@3%s@): @1%s@ (@2%s@) No connection to the logging system backend | AlarmLogging service: The backend of the database was shut down. It is either completely down or the corresponding network connection has problems.  (Only applicable with Process Historian.) | Check the status of the database backend. If it does not work, try restarting it or analyze the log files to learn more about the problem.  Otherwise, ensure that the network connection is working. |
| 536871945 | Computer1 [@3%s@] - @1%s@: An overflow of the transaction buffer and write buffer has occurred in log @2%s@ of the passive partner. Data may be lost. Avoid a manual failover of the redundancy partner while this alarm is active. | In the passive AlarmLogging service, the buffers are full and therefore some data has already been lost.  Possible causes:  - Infrastructure problem (e.g. connection abort, hard disk full, see other system alarms in this case). - Generally, a high load that cannot be handled by the system.   If the connection between the redundant services is interrupted, this can also cause this problem. If the active service has no problems, this alarm does not mean real data loss. (Only applicable with Process Historian.) | Correct the root cause of the problem.   If the problem is infrastructural, follow the instructions of the corresponding system alarm. If there is none, the cause is probably too much load on the system or write speed degradation (for example, slowing down of a storage medium).   Check the hardware elements, reduce the system load, or if it is a persistent problem, the hardware configuration may not be sufficient for the current project.   If the connection to the active service has been lost, but it is working without any problems, it is important not to initiate redundancy failover after the connection is restored while this alarm is still present to avoid real data loss. |
| 536871946 | Computer1 [@3%s@] - @1%s@: (@2%s@) Connection to the long-term logging system is lost. | AlarmLogging service has its lost connection to the long-term storage system.   This is probably due to an internal database error or a network problem. (Only applicable with Process Historian.) | Check the status of the long-term database server. Starting/restarting the server may solve the problem. If it is running, ensure that the network connection is working.  Otherwise, the database logs may help find the cause. |
| 536871947 | Computer1 [@4%s@] - @1%s@ (@2%s@ - @3%s@): Long-term logging system is out of hard disk space. | At least one storage medium used by the AlarmLogging service long-term storage system is full, so new value changes cannot be saved.  (Only applicable with Process Historian.) | Check the status of the connected storage media on the long-term storage system and free up some space on the devices (almost) full. Changing the log configuration can help reduce the amount of disk space needed by limiting the maximum amount of space a particular log can use before deleting the data. |
| 536871948 | Computer1 [@3%s@] - @1%s@: (@2%s@): Long-term logging system no longer has any system resources. | The long-term storage system used by the AlarmLogging service is still running, but has reported that it is out of resources (e.g. memory, disk space). No more writing is possible.  (Only applicable with Process Historian.) | Check the long-term storage media to see if they are running out of space. The database server logs can also help to find out the cause of the problem. Storage space problems can be caused by a high load that the system cannot handle. |
| 536871949 | Computer1 [@2%s@] - @1%s@: The passive and the active long-term logging system are no longer synchronized. | The redundant long-term databases used by AlarmLogging service have lost connection to each other (triggered only on the passive host).   Possible causes:  - The active database is completely shut down. - A problem with the network connection.   (Only applicable with Process Historian.) | Check the status of the active long-term storage system. If it is down, try to restart it or analyze its logged files to learn more about the problem.   If the database is running, ensure that the network connection between the two hosts is working. |
| 536871950 | Computer1 [@2%s@] - @1%s@: Synchronizing long-term logging system | AlarmLogging service: Synchronization of logged data between the active and passive long-term storage systems is in progress. Redundancy failover during this state may result in loss of logged data.  (Only applicable with Process Historian.) | This system alarm does not signify an error; it is normal behavior when the two redundant databases are synchronizing data. Therefore, no action is required.  As long as this system alarm is pending, you should not initiate redundancy failover, otherwise the logged data may be lost. |
| 536871951 | Computer1 [@2%s@] - @1%s@: Failover error in the long-term logging system. | AlarmLogging service: An error occurred when the long-term storage system tried to switch roles between the active and passive databases. (Only applicable with Process Historian.) | Analyze the Process Historian log files to learn more information about the reason for the failure. |
| 536871952 | Computer1 [@3%s@] - @1%s@: (@2%s@) A general error has occurred. Check the traces for additional information. | AlarmLogging service: An unknown error occurred during the execution of a database operation. | Analyze previous traces to learn more about the problem.   One possible scenario that can cause this problem is the unexpected removal of a storage medium. In this case, reinstall the storage medium and restart Runtime. Otherwise, contact Siemens support for assistance. |
| 536871953 | Computer1 [@6%s@] - @1%s@ (@2%s@ - @3%s@): Logging medium cannot be reached. @5%t#4T@ | AlarmLogging service: When trying to create a database or reconnect to a storage medium, a storage medium was not available or authorizations were lacking. | Check if the configuration (path of the log) is valid for all logs and if all required storage media are connected and working.   If authorizations are available, ensure they are set correctly for the file system. |
| 536871954 | Computer1 [@2%s@]: The logging system @1%s@ has detected a more recent database version that is not compatible with the current runtime version. Update the runtime version on your device or use a device with the same runtime version as the database version. | AlarmLogging service: The Runtime software used is older than the databases used. Probably the database was moved from a device with newer software to a device with older software. | Move the database to a device with the same or a newer version of the Runtime software, or upgrade the software version of the device. |
| 536871955 | Computer1 [@2%s@]: @1%s@: Synchronizing the logging data of the redundant partners. | The redundant AlarmLogging services synchronize data with each other. This is normal behavior that only serves as an indication that the historical data on both hosts is not quite up-to-date. | No action is required, but as long as this system alarm persists, it is recommended not to shut down any of the hosts.  If this alarm has persisted since the last startup/restart of one of the hosts, do not restart or shut down the longer running host since data loss may occur. |
| 536871956 | Computer1 [@2%s@]: @1%s@: Error during background synchronization. Check the traces for additional information. | AlarmLogging service: An error occurred during data synchronization. | Check the additional alarm information to identify and eliminate the cause of the error.  The synchronization is repeated at regular intervals so that it can be performed shortly after the cause has been eliminated. |
| 536872193 | Computer1 [@3%s@]: @1%s@ (@2%s@): has no connection to the logging system. | AlarmPersistency service has its lost connection to the database.   Possible cause: Internal error of the database. If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the database.  Otherwise, the log files may help find the cause. |
| 536872194 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Log is full. | At least one storage medium used by the AlarmPersistency service is full, so new value changes cannot be saved. If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the connected storage media and free up some space on the devices (almost) full. |
| 536872195 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Insufficient resources of the logging system. | Not applicable. |  |
| 536872196 | Computer1 [@3%s@]: @1%s@: A write buffer overflow has occurred in log @2%s@. Data will be lost. | In the AlarmPersistency service, the buffers are full and therefore some data has already been lost.  Possible causes:  - Infrastructure problem (e.g. connection abort, hard disk full, see other system alarms in this case). - Generally, a high load that cannot be handled by the system.   With redundant deployment, if only one host has this problem temporarily, the data from the other host is synchronized once the problem is resolved. | Correct the root cause of the problem.   If the problem is infrastructural, follow the instructions of the corresponding system alarm. If there is none, the cause is probably too much load on the system or write speed degradation (for example, slowing down of a storage medium).   Check the hardware elements, reduce the system load, or if it is a persistent problem, the hardware configuration may not be sufficient for the current project. |
| 536872197 | Computer1 [@2%s@]: @1%s@: The passive logging system has lost the connection to the active logging system. | Not applicable. |  |
| 536872198 | Computer1 [@2%s@]: @1%s@: Synchronizing data | Not applicable. |  |
| 536872199 | Computer1 [@2%s@]: @1%s@: Failover error | Not applicable. |  |
| 536872200 | Computer1 (@3%s@): @1%s@ (@2%s@) No connection to the logging system backend | Not applicable. |  |
| 536872201 | Computer1 [@3%s@] - @1%s@: An overflow of the transaction buffer and write buffer has occurred in log @2%s@ of the passive partner. Data may be lost. Avoid a manual failover of the redundancy partner while this alarm is active. | Not applicable. |  |
| 536872202 | Computer1 [@3%s@] - @1%s@: (@2%s@) Connection to the long-term logging system is lost. | Not applicable. |  |
| 536872203 | Computer1 [@4%s@] - @1%s@ (@2%s@ - @3%s@): Long-term logging system is out of hard disk space. | Not applicable. |  |
| 536872204 | Computer1 [@3%s@] - @1%s@: (@2%s@): Long-term logging system no longer has any system resources. | Not applicable. |  |
| 536872205 | Computer1 [@2%s@] - @1%s@: The passive and the active long-term logging system are no longer synchronized. | Not applicable. |  |
| 536872206 | Computer1 [@2%s@] - @1%s@: Synchronizing long-term logging system | Not applicable. |  |
| 536872207 | Computer1 [@2%s@] - @1%s@: Failover error in the long-term logging system. | Not applicable. |  |
| 536872208 | Computer1 [@3%s@] - @1%s@: (@2%s@) A general error has occurred. Check the traces for additional information. | AlarmPersistency service: An unknown error occurred during the execution of a database operation. | Analyze previous traces to learn more about the problem.   One possible scenario that can cause this problem is the unexpected removal of a storage medium. In this case, reinstall the storage medium and restart Runtime.   Otherwise, contact Siemens support for assistance. |
| 536872209 | Computer1 [@6%s@] - @1%s@ (@2%s@ - @3%s@): Logging medium cannot be reached. @5%t#4T@ | AlarmPersistency service: When trying to create a database or reconnect to a storage medium, no storage medium was available or authorizations were lacking. | Check if the configuration (path of the AlarmPersistency database) is valid and if all required storage media are connected and working.   If available, ensure that the file system authorizations are set correctly. |
| 536872210 | Computer1 [@2%s@]: The logging system @1%s@ has detected a more recent database version that is not compatible with the current runtime version. Update the runtime version on your device or use a device with the same runtime version as the database version. | AlarmPersistency service: The Runtime software used is older than the databases used. Probably the database was moved from a device with newer software to a device with older software. | Move the database to a device with the same or a newer version of the Runtime software or update the software version of the device. |
| 536872211 | Computer1 [@2%s@]: @1%s@: Synchronizing the logging data of the redundant partners. | Not applicable. |  |
| 536872212 | Computer1 [@2%s@]: @1%s@: Error during background synchronization. Check the traces for additional information. | Not applicable. |  |
| 536872449 | Computer1 [@3%s@]: @1%s@ (@2%s@): has no connection to the logging system. | TagLogging service has lost its connection to the database.  Possible cause: Internal error of the database. If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the database server. In some cases, starting/restarting the database may solve the problem. Otherwise, the database log files can help to find the cause. |
| 536872450 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Log is full. | At least one storage medium used by the TagLogging service is full, so new value changes cannot be saved. If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the connected storage media and free some space on the devices (almost) full. Changing the log configuration can help reduce the amount of disk space needed by limiting the maximum amount of space a particular log can use before deleting data. |
| 536872451 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Insufficient resources of the logging system. | The database used by the TagLogging service is still running, but has reported that it is out of resources (e.g. work memory, disk space).  No more writing is possible.  (Only applicable with Process Historian.) | Check the storage medium if it is out of space.   The database server logs can also help to find out the cause of the problem. Storage space problems can be caused by a high load that the system cannot handle. |
| 536872452 | Computer1 [@3%s@]: @1%s@: A write buffer overflow has occurred in log @2%s@. Data will be lost. | In the TagLogging service, the buffers are full and therefore some data has already been lost.  Possible causes:  - Infrastructure problem (e.g. connection abort, hard disk full, see other system alarms in this case). - Generally, a high load that cannot be handled by the system.   With redundant deployment, if only one host has this problem temporarily, the data from the other host is synchronized once the problem is resolved. | Correct the root cause of the problem.   If the problem is infrastructural, follow the instructions of the corresponding system alarm. If there is none, the cause is probably too much load on the system or write speed degradation (for example, slowing down of a storage medium).   Check the hardware elements, reduce the system load, or if it is a persistent problem, the hardware configuration may not be sufficient for the current project. |
| 536872453 | Computer1 [@2%s@]: @1%s@: The passive logging system has lost the connection to the active logging system. | The redundant databases used by the TagLogging service have lost connection to each other (triggered only on the passive host).  Possible causes:   - The active database is completely shut down. - A problem with the network connection.   If the StorageSystemPassiveSynchronizing alarm is also triggered, it means that the problem is resolved and the alarm will be cleared as soon as synchronization is completed. (Only applicable with Process Historian.) | Check the status of the active database.   If the database is not running, try restarting it or analyze its log files to learn more about the problem.   If the database is running, ensure that the network connection between the two hosts is working. |
| 536872454 | Computer1 [@2%s@]: @1%s@: Synchronizing data | TagLogging service: Logged data synchronization is in progress between the active and passive databases. Redundancy failover during this state may result in loss of logged data. (Only applicable with Process Historian.) | This system alarm does not signify an error; it is normal behavior when the two redundant databases are synchronizing data. Therefore, no action is required.  As long as this system alarm is pending, you should not initiate redundancy failover, otherwise the logged data may be lost. |
| 536872455 | Computer1 [@2%s@]: @1%s@: Failover error | TagLogging service: An error occurred while the database was trying to switch roles between the active and passive databases. (Only applicable with Process Historian.) | Analyze the Process Historian log files to learn more about the reason for the failure. If other system alarms are also triggered, they may also be related. |
| 536872456 | Computer1 (@3%s@): @1%s@ (@2%s@) No connection to the logging system backend | TagLogging service: The backend of the database was shut down. It is either completely down or the network connection to it is having problems. (Only applicable with Process Historian.) | Check the status of the database backend. If it does not work, restart it or analyze the log files to learn more about the causes.  Ensure that the network connection is working. |
| 536872457 | Computer1 [@3%s@] - @1%s@: An overflow of the transaction buffer and write buffer has occurred in log @2%s@ of the passive partner. Data may be lost. Avoid a manual failover of the redundancy partner while this alarm is active. | In the passive TagLogging service, the buffers are full and therefore some data has already been lost.   Possible causes:  - Infrastructure problem (e.g. connection abort, hard disk full, see other system alarms in this case). - Generally, a high load that cannot be handled by the system. - Interrupted connection between the redundant services.   If the active service has no problems, this alarm does not mean real data loss. (Only applicable with Process Historian.) | Correct the root cause of the problem.   If the problem is infrastructural, follow the instructions of the corresponding system alarm. If there is none, the cause is probably too much load on the system or write speed degradation (for example, slowing down of a storage medium). Check the hardware elements, reduce the system load, or if it is a persistent problem, the hardware configuration may not be sufficient for the current project.   If the connection to the active service has been lost, but it is working without any problems, it is important not to initiate redundancy failover after the connection is restored while this alarm is still present to avoid real data loss. |
| 536872458 | Computer1 [@3%s@] - @1%s@: (@2%s@) Connection to the long-term logging system is lost. | TagLogging service has its lost connection to the long-term storage system.  Possible causes:  - Internal database error. - Network problem.   (Only applicable with Process Historian.) | Check the status of the long-term database server.  Start/restart the server.   If it is running, ensure that the network connection is working.  Database logs can also help to find the cause. |
| 536872459 | Computer1 [@4%s@] - @1%s@ (@2%s@ - @3%s@): Long-term logging system is out of hard disk space. | At least one storage medium used by the TagLogging service long-term storage system is full, so new value changes cannot be saved.  (Only applicable with Process Historian.) | Check the status of the connected storage media on the long-term storage system and free up some space on the devices (almost) full. Changing the log configuration can help reduce the amount of disk space needed by limiting the maximum amount of space a particular log can use before deleting the data. |
| 536872460 | Computer1 [@3%s@] - @1%s@: (@2%s@): Long-term logging system no longer has any system resources. | The long-term storage system used by the TagLogging service is still running, but has reported that it is out of resources (e.g. memory, disk space).   No more writing is possible. (Only applicable with Process Historian.) | Check the long-term storage media to see if they are running out of space.   The database server logs can also help to find out the cause of the problem.  Storage space problems can be caused by a large load that the system cannot handle. |
| 536872461 | Computer1 [@2%s@] - @1%s@: The passive and the active long-term logging system are no longer synchronized. | The redundant long-term databases used by the TagLogging service have lost connection to each other (triggered only on the passive host).   Possible causes:  - The active database is completely shut down. - A problem with the network connection.   (Only applicable with Process Historian.) | Check the status of the active long-term storage system. If it is down, try to restart it or analyze its logged files to learn more about the problem.   If the database is running, ensure that the network connection between the two hosts is working. |
| 536872462 | Computer1 [@2%s@] - @1%s@: Synchronizing long-term logging system | TagLogging service: Synchronization of logged data between the active and passive long-term storage systems is in progress. Redundancy failover during this state may result in loss of logged data. (Only applicable with Process Historian.) | This system alarm does not signify an error; it is normal behavior when the two redundant databases are synchronizing data. Therefore, no action is required.  As long as this system alarm is pending, you should not initiate redundancy failover, otherwise the logged data may be lost. |
| 536872463 | Computer1 [@2%s@] - @1%s@: Failover error in the long-term logging system. | TagLogging service: An error occurred while the long-term storage system was trying to switch roles between the active and passive databases. (Only applicable with Process Historian.) | Analyze the Process Historian log files to learn more about the reason for the failure. |
| 536872464 | Computer1 [@3%s@] - @1%s@: (@2%s@) A general error has occurred. Check the traces for additional information. | TagLogging service: An unknown error occurred during the execution of a database operation. | Analyze previous traces to learn more about the problem. One possible cause of this problem is the unexpected removal of a storage device.  In this case, reinstall the storage medium and restart Runtime. Otherwise, contact Siemens support for assistance. |
| 536872465 | Computer1 [@6%s@] - @1%s@ (@2%s@ - @3%s@): Logging medium cannot be reached. @5%t#4T@ | TagLogging service: When trying to create a database or reconnect to a storage medium, a storage medium was not available or authorizations were lacking. | Check if the configuration (path of the log) is valid for all logs and if all required storage media are connected and working.   If authorizations are available, ensure that the file system authorizations are set correctly. |
| 536872466 | Computer1 [@2%s@]: The logging system @1%s@ has detected a more recent database version that is not compatible with the current runtime version. Update the runtime version on your device or use a device with the same runtime version as the database version. | TagLogging service: The Runtime software used is older than the databases used. Probably the database was moved from a device with newer software to a device with older software. | Move the database to a device with the same or a newer version of the Runtime software or update the software version of the device. |
| 536872467 | Computer1 [@2%s@]: @1%s@: Synchronizing the logging data of the redundant partners. | The redundant TagLogging services synchronize the data with each other. This is normal behavior that only indicates that the historical data on both hosts is not quite up to date. | No action is required, but as long as this system alarm persists, it is recommended not to shut down any of the hosts.  If this alarm has persisted since the last startup/restart of one of the hosts, do not restart or shut down the longer running host since data loss may occur. |
| 536872468 | Computer1 [@2%s@]: @1%s@: Error during background synchronization. Check the traces for additional information. | TagLogging service: An error occurred during data synchronization. | Check the additional alarm information to identify and eliminate the cause of the error.  The synchronization is repeated at regular intervals so that it can be performed shortly after the cause has been eliminated. |
| 536872705 | Computer1 [@3%s@]: @1%s@ (@2%s@): has no connection to the logging system. | TagPersistency service has its lost connection to the database.  Possible cause:  - Internal database error.   If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the database.   The log files of the Runtime system can also help to find the cause. |
| 536872706 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Log is full. | At least one storage medium used by the TagPersistency service is full, so new value changes cannot be saved. If this situation continues for too long, the buffers for values can become full, resulting in data loss. | Check the status of the connected storage media and free up some space on the devices (almost) full. |
| 536872707 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Insufficient resources of the logging system. | Not applicable. |  |
| 536872708 | Computer1 [@3%s@]: @1%s@: A write buffer overflow has occurred in log @2%s@. Data will be lost. | In the TagPersistency service, the buffers are full and therefore some data has already been lost.  Possible causes:  - Infrastructure problem (e.g. connection abort, hard disk full, see other system alarms in this case). - Generally, a high load that cannot be handled by the system.   With redundant deployment, if only one host has this problem temporarily, the data from the other host is synchronized once the problem is resolved. | Correct the root cause of the problem.   If the problem is infrastructural, follow the instructions of the corresponding system alarm. If there is none, the cause is probably too much load on the system or write speed degradation (for example, slowing down of a storage medium). Check the hardware elements, reduce the system load, or if it is a persistent problem, the hardware configuration may not be sufficient for the current project. |
| 536872709 | Computer1 [@2%s@]: @1%s@: The passive logging system has lost the connection to the active logging system. | Not applicable. |  |
| 536872710 | Computer1 [@2%s@]: @1%s@: Synchronizing data | Not applicable. |  |
| 536872711 | Computer1 [@2%s@]: @1%s@: Failover error | Not applicable. |  |
| 536872712 | Computer1 (@3%s@): @1%s@ (@2%s@) No connection to the logging system backend | Not applicable. |  |
| 536872713 | Computer1 [@3%s@] - @1%s@: An overflow of the transaction buffer and write buffer has occurred in log @2%s@ of the passive partner. Data may be lost. Avoid a manual failover of the redundancy partner while this alarm is active. | Not applicable. |  |
| 536872714 | Computer1 [@3%s@] - @1%s@: (@2%s@) Connection to the long-term logging system is lost. | Not applicable. |  |
| 536872715 | Computer1 [@4%s@] - @1%s@ (@2%s@ - @3%s@): Long-term logging system is out of hard disk space. | Not applicable. |  |
| 536872716 | Computer1 [@3%s@] - @1%s@: (@2%s@): Long-term logging system no longer has any system resources. | Not applicable. |  |
| 536872717 | Computer1 [@2%s@] - @1%s@: The passive and the active long-term logging system are no longer synchronized. | Not applicable. |  |
| 536872718 | Computer1 [@2%s@] - @1%s@: Synchronizing long-term logging system | Not applicable. |  |
| 536872719 | Computer1 [@2%s@] - @1%s@: Failover error in the long-term logging system. | Not applicable. |  |
| 536872720 | Computer1 [@3%s@] - @1%s@: (@2%s@) A general error has occurred. Check the traces for additional information. | TagPersistency service: An unknown error occurred during the execution of a database operation. | Analyze previous traces to learn more about the problem. One possible cause is the unexpected removal of a storage medium.  In this case, reinstall the storage medium and restart Runtime. Otherwise, contact Siemens support for assistance. |
| 536872721 | Computer1 [@6%s@] - @1%s@ (@2%s@ - @3%s@): Logging medium cannot be reached. @5%t#4T@ | TagPersistency service: When trying to create a database or reconnect to the storage medium, no storage medium was available or authorizations were lacking. | Check if the configuration (path of the TagPersistency database) is valid and if all required storage media are connected and working.   If authorizations are available, ensure that the file system authorizations are set correctly. |
| 536872722 | Computer1 [@2%s@]: The logging system @1%s@ has detected a more recent database version that is not compatible with the current runtime version. Update the runtime version on your device or use a device with the same runtime version as the database version. | TagPersistency service: The Runtime software used is older than the databases used. Probably the database was moved from a device with newer software to a device with older software. | Move the database to a device with the same or a newer version of the Runtime software or update the software version of the device. |
| 536872723 | Computer1 [@2%s@]: @1%s@: Synchronizing the logging data of the redundant partners. | Not applicable. |  |
| 536872724 | Computer1 [@2%s@]: @1%s@: Error during background synchronization. Check the traces for additional information. | Not applicable. |  |
| 536872961 | Computer1 [@3%s@]: @1%s@ (@2%s@): has no connection to the logging system. | ContextLogging service has its lost connection to the database.  Possible cause:  - Internal database error.   If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the database server.  Start/restart database.  The log files of the database can also help to find the cause. |
| 536872962 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Log is full. | At least one storage medium used by ContextLogging service is full, so new value changes cannot be saved. If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the connected storage media and free up some space on the devices (almost) full. Changing the log configuration can help reduce the amount of disk space needed by limiting the maximum amount of space a particular log can use before deleting the data. |
| 536872963 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Insufficient resources of the logging system. | Not applicable. |  |
| 536872964 | Computer1 [@3%s@]: @1%s@: A write buffer overflow has occurred in log @2%s@. Data will be lost. | In the ContextLogging service, the buffers are full and therefore some data has already been lost.  Possible causes:  - Infrastructure problem (e.g. connection abort, hard disk full, see other system alarms in this case). - Generally, a high load that cannot be handled by the system.   With redundant deployment, if only one host has this problem temporarily, the data from the other host is synchronized once the problem is resolved. | Correct the root cause of the problem.   If the problem is infrastructural, follow the instructions of the corresponding system alarm. If there is none, the cause is probably too much load on the system or write speed degradation (for example, slowing down of a storage medium). Check the hardware elements, reduce the system load, or if it is a persistent problem, the hardware configuration may not be sufficient for the current project. |
| 536872965 | Computer1 [@2%s@]: @1%s@: The passive logging system has lost the connection to the active logging system. | Not applicable. |  |
| 536872966 | Computer1 [@2%s@]: @1%s@: Synchronizing data | Not applicable. |  |
| 536872967 | Computer1 [@2%s@]: @1%s@: Failover error | Not applicable. |  |
| 536872968 | Computer1 (@3%s@): @1%s@ (@2%s@) No connection to the logging system backend | Not applicable. |  |
| 536872969 | Computer1 [@3%s@] - @1%s@: An overflow of the transaction buffer and write buffer has occurred in log @2%s@ of the passive partner. Data may be lost. Avoid a manual failover of the redundancy partner while this alarm is active. | Not applicable. |  |
| 536872970 | Computer1 [@3%s@] - @1%s@: (@2%s@) Connection to the long-term logging system is lost. | Not applicable. |  |
| 536872971 | Computer1 [@4%s@] - @1%s@ (@2%s@ - @3%s@): Long-term logging system is out of hard disk space. | Not applicable. |  |
| 536872972 | Computer1 [@3%s@] - @1%s@: (@2%s@): Long-term logging system no longer has any system resources. | Not applicable. |  |
| 536872973 | Computer1 [@2%s@] - @1%s@: The passive and the active long-term logging system are no longer synchronized. | Not applicable. |  |
| 536872974 | Computer1 [@2%s@] - @1%s@: Synchronizing long-term logging system | Not applicable. |  |
| 536872975 | Computer1 [@2%s@] - @1%s@: Failover error in the long-term logging system. | Not applicable. |  |
| 536872976 | Computer1 [@3%s@] - @1%s@: (@2%s@) A general error has occurred. Check the traces for additional information. | ContextLogging service: An unknown error occurred during the execution of a database operation. | Analyze previous traces to learn more about the problem. A possible cause can be the unexpected removal of a storage medium.  In this case, reinstall the storage medium and restart Runtime. Otherwise, contact Siemens support for assistance. |
| 536872977 | Computer1 [@6%s@] - @1%s@ (@2%s@ - @3%s@): Logging medium cannot be reached. @5%t#4T@ | ContextLogging service: When trying to create a database or reconnect to the storage medium, no storage medium was available or authorizations were lacking. | Check if the configuration (path of the log) is valid for all logs and if all required storage media are connected and working.   If authorizations are available, ensure that the file system authorizations are set correctly. |
| 536872978 | Computer1 [@2%s@]: The logging system @1%s@ has detected a more recent database version that is not compatible with the current runtime version. Update the runtime version on your device or use a device with the same runtime version as the database version. | ContextLogging service: The Runtime software used is older than the databases used. Probably the database was moved from a device with newer software to a device with older software. | Move the database to a device with the same or a newer version of the Runtime software or update the software version of the device. |
| 536872979 | Computer1 [@2%s@]: @1%s@: Synchronizing the logging data of the redundant partners. | The redundant ContextLogging services synchronize the data with each other. This is normal behavior that only indicates that the historical data on both hosts is not quite up to date. | No action is required, but as long as this system alarm persists, it is recommended not to shut down any of the hosts.  If this alarm has persisted since the last startup/restart of one of the hosts, do not restart or shut down the longer running host since data loss may occur. |
| 536872980 | Computer1 [@2%s@]: @1%s@: Error during background synchronization. Check the traces for additional information. | ContextLogging service: An error occurred during data synchronization. | Check the additional alarm information to identify and eliminate the cause of the error.  The synchronization is repeated at regular intervals so that it can be performed shortly after the cause has been eliminated. |
| 536873217 | Computer1 [@3%s@]: @1%s@ (@2%s@): has no connection to the logging system. | AuditTrail service has its lost connection to the database.  Possible cause:  - Internal database error.   If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the database server.  Start/restart database.  The log files of the database can also help to find the cause. |
| 536873218 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Log is full. | At least one storage medium used by the AuditTrail service is full, so new value changes cannot be saved. If this situation continues for too long, the buffers for values may become full, resulting in data loss. | Check the status of the connected storage media and free up some space on the devices (almost) full. Changing the log configuration can help reduce the amount of disk space needed by limiting the maximum amount of space a particular log can use before deleting the data. |
| 536873219 | Computer1 [@4%s@]: @1%s@ (@2%s@ - @3%s@): Insufficient resources of the logging system. | Not applicable. |  |
| 536873220 | Computer1 [@3%s@]: @1%s@: A write buffer overflow has occurred in log @2%s@. Data will be lost. | In the AuditTrail service, the buffers are full and therefore some data has already been lost.  Possible cause:  - Infrastructure problem (e.g. connection abort, hard disk full, see other system alarms in this case). - Generally, a high load that cannot be handled by the system.   With redundant deployment, if only one host has this problem temporarily, the data from the other host is synchronized once the problem is resolved. | Correct the root cause of the problem.   If the problem is infrastructural, follow the instructions of the corresponding system alarm. If there is none, the cause is probably too much load on the system or write speed degradation (for example, slowing down of a storage medium). Check the hardware elements, reduce the system load, or if it is a persistent problem, the hardware configuration may not be sufficient for the current project. |
| 536873221 | Computer1 [@2%s@]: @1%s@: The passive logging system has lost the connection to the active logging system. | Not applicable. |  |
| 536873222 | Computer1 [@2%s@]: @1%s@: Synchronizing data | Not applicable. |  |
| 536873223 | Computer1 [@2%s@]: @1%s@: Failover error | Not applicable. |  |
| 536873224 | Computer1 (@3%s@): @1%s@ (@2%s@) No connection to the logging system backend | Not applicable. |  |
| 536873225 | Computer1 [@3%s@] - @1%s@: An overflow of the transaction buffer and write buffer has occurred in log @2%s@ of the passive partner. Data may be lost. Avoid a manual failover of the redundancy partner while this alarm is active. | Not applicable. |  |
| 536873226 | Computer1 [@3%s@] - @1%s@: (@2%s@) Connection to the long-term logging system is lost. | Not applicable. |  |
| 536873227 | Computer1 [@4%s@] - @1%s@ (@2%s@ - @3%s@): Long-term logging system is out of hard disk space. | Not applicable. |  |
| 536873228 | Computer1 [@3%s@] - @1%s@: (@2%s@): Long-term logging system no longer has any system resources. | Not applicable. |  |
| 536873229 | Computer1 [@2%s@] - @1%s@: The passive and the active long-term logging system are no longer synchronized. | Not applicable. |  |
| 536873230 | Computer1 [@2%s@] - @1%s@: Synchronizing long-term logging system | Not applicable. |  |
| 536873231 | Computer1 [@2%s@] - @1%s@: Failover error in the long-term logging system. | Not applicable. |  |
| 536873232 | Computer1 [@3%s@] - @1%s@: (@2%s@) A general error has occurred. Check the traces for additional information. | AuditTrail service: An unknown error occurred during the execution of a database operation. | Analyze previous traces to learn more about the problem.  A possible cause can be the unexpected removal of a storage medium.  In this case, reinstall the storage medium and restart Runtime. Otherwise, contact Siemens support for assistance. |
| 536873233 | Computer1 [@6%s@] - @1%s@ (@2%s@ - @3%s@): Logging medium cannot be reached. @5%t#4T@ | AuditTrail service: When trying to create a database or reconnect to the storage medium, no storage medium was available or authorizations were lacking. | Check if the configuration (path of the log) is valid for all logs and if all required storage media are connected and working.   If authorizations are available, ensure that the file system authorizations are set correctly. |
| 536873234 | Computer1 [@2%s@]: The logging system @1%s@ has detected a more recent database version that is not compatible with the current runtime version. Update the runtime version on your device or use a device with the same runtime version as the database version. | AuditTrail service: The Runtime software used is older than the databases used. Probably the database was moved from a device with newer software to a device with older software. | Move the database to a device with the same or a newer version of the Runtime software or update the software version of the device. |
| 536873235 | Computer1 [@2%s@]: @1%s@: Synchronizing the logging data of the redundant partners. | The redundant AuditTrail services synchronize the data with each other. This is normal behavior that only indicates that the historical data on both hosts is not quite up to date. | No action is required, but as long as this system alarm persists, it is recommended not to shut down any of the hosts.  If this alarm has persisted since the last startup/restart of one of the hosts, do not restart or shut down the longer running host since data loss may occur. |
| 536873236 | Computer1 [@2%s@]: @1%s@: Error during background synchronization. Check the traces for additional information. | AuditTrail service: An error occurred during data synchronization. | Check the additional alarm information to identify and eliminate the cause of the error.   The synchronization is repeated at regular intervals so that it can be performed shortly after the cause has been eliminated. |
