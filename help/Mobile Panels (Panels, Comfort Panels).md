---
title: "Mobile Panels (Panels, Comfort Panels)"
package: WirelessWCCAenUS
topics: 13
devices: [Comfort Panels, Panels]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Mobile Panels (Panels, Comfort Panels)

This section contains information on the following topics:

- [Basics (Panels, Comfort Panels)](#basics-panels-comfort-panels)
- [Configuring KTP Mobile Panels for fail-safe operation (Panels, Comfort Panels)](#configuring-ktp-mobile-panels-for-fail-safe-operation-panels-comfort-panels)
- [Working with zones on connection boxes (Panels, Comfort Panels)](#working-with-zones-on-connection-boxes-panels-comfort-panels)
- [Reference (Panels, Comfort Panels)](#reference-panels-comfort-panels)

## Basics (Panels, Comfort Panels)

This section contains information on the following topics:

- [Zones (Panels, Comfort Panels)](#zones-panels-comfort-panels)
- [Zones work area on connection boxes (Panels, Comfort Panels)](#zones-work-area-on-connection-boxes-panels-comfort-panels)

### Zones (Panels, Comfort Panels)

#### Introduction

The section below applies to the following Mobile Panels:

- KTP Mobile Panels, wired, e.g., Mobile Panel KTP700

A "Zones" work area is only visible for these HMI devices.

#### Open

Depending on the HMI device selected, open the work area in the project window by double-clicking on "Zones" or "Zones and effective ranges".

#### Work area

For wired Mobile Panels, the "Zones" work area shows the zones that have been set up and the associated box ID of the connection box.

#### Inspector window

When a zone is selected, edit the name and display name under "General".

With wired Mobile Panels enter the box ID of the connection box. The zone of a connection box includes the event "Connected".

Configure the system function ActivateScreen" to the events.

---

**See also**

[Complete documentation for Mobile Wireless](http://support.automation.siemens.com/WW/view/en/26268960)

### Zones work area on connection boxes (Panels, Comfort Panels)

#### Introduction

The "Zones" work area displays the box IDs of the connection boxes and their zones in table format.

You create a list of box IDs of the connection boxes and assign specific connection boxes to a zone. The limit of the zone is defined by the length of the connecting cable to your Mobile Panel.

#### Principle

The work area consists of the "Zones" table.

![Principle](images/68722064267_DV_resource.Stream@PNG-en-US.png)

The box ID is set on the connection box and can be read out from the HMI device.

## Configuring KTP Mobile Panels for fail-safe operation (Panels, Comfort Panels)

This section contains information on the following topics:

- [Creating KTP Mobile Panel for fail-safe operation (Panels, Comfort Panels)](#creating-ktp-mobile-panel-for-fail-safe-operation-panels-comfort-panels)
- [Configuring the termination of the PROFIsafe connection (Panels, Comfort Panels)](#configuring-the-termination-of-the-profisafe-connection-panels-comfort-panels)

### Creating KTP Mobile Panel for fail-safe operation (Panels, Comfort Panels)

#### Introduction

Configure fail-safe operation in the "Devices & Networks" editor for the following KTP Mobile Panels:

- KTP400F Mobile Panel
- KTP700F Mobile Panel
- KTP900F Mobile Panel

#### Requirement

- The Inspector window is open.
- A PLC for fail-safe operation is created in the project, for example, CPU-1517F-2PN/DP.

#### Inserting a mobile panel into the project

1. Click "Add new device" in the project navigation.
2. Click on "HMI" in the "Add new device" dialog.
3. Select a KTP Mobile Panel for fail-safe operation, for example, Mobile Panel KTP700F. The device is inserted into the project.

#### Configuring fail-safe operation for the mobile panel

1. Open the network view in the "Devices & Networks" editor.
2. Select the Mobile Panel in the work area.
3. Select "Properties > General > Mode > IO device" in the inspector window.
4. Assign the fail-safe PLC under "Assigned IO controller".

   PROFINET is activated and the transfer areas of the I-device communication are displayed.
5. In the Inspector window, click "Activate PROFIsafe" under "Properties > General" > PROFIsafe".

   PROFIsafe is activated and the F-parameters are displayed under "Properties > General> PROFIsafe parameters > F-parameters".
6. To enter a new F-monitoring time, select "Manual assignment of F-monitoring time".
7. Enter an F-monitoring time suitable for your HMI device and plant.

#### Result

The fail-safe operation of the KTP Mobile Panel is configured in WinCC. Now create the corresponding F-blocks in STEP 7 and interconnect them in the controller. The PROFIsafe address must be set on the Mobile Panel.

You can find additional information on configuration and programming of fail-safe blocks in the manual "SIMATIC Safety - Configuration and Programming" of the STEP 7 documentation and in the device manual of your mobile panel.

### Configuring the termination of the PROFIsafe connection (Panels, Comfort Panels)

#### Procedure

Before you disconnect your Mobile Panel from a connection box, you have to terminate the connection to PROFIsafe.

Use the "Disconnect PROFIsafe" system function to close the PROFIsafe connection. The system function forwards your call to the fail-safe PROFINET module.

#### Requirements

- A mobile panel has been created for fail-safe operation, for example,  KTP700F Mobile Panel.
- A screen has been created and opened.

#### Procedure

To configure the PROFIsafe the connection and disconnection, follow these steps:

- Configure the "Disconnect PROFIsafe" system function on a button, for example, or use it in a script.

#### Result

If you release the configured trigger for terminating the PROFIsafe connection in runtime, a dialog for ending the PROFIsafe connection opens. The user can select "Yes" or "No".

## Working with zones on connection boxes (Panels, Comfort Panels)

This section contains information on the following topics:

- [Configuring the zone of a connection box (Panels, Comfort Panels)](#configuring-the-zone-of-a-connection-box-panels-comfort-panels)
- [Calling system functions when connected to the connection box. (Panels, Comfort Panels)](#calling-system-functions-when-connected-to-the-connection-box-panels-comfort-panels)

### Configuring the zone of a connection box (Panels, Comfort Panels)

#### Validity

The following section applies to all KTP Mobile Panels, for example, Mobile Panel KTP700.

#### Introduction

You will have to set up a zone in order to carry out plant-specific operator control and monitoring tasks.

#### Requirements

- A suitable editing language, e.g. English, must have been set in the "Project languages" editor.
- The "Zones" work area is open.

#### Procedure

1. Double-click "Add..." in the "Zones" table.
2. Enter the box ID of your connection box for "ID".
3. Enter the "MixingPlant" zone in the "Name" field.
4. Enter "MixingSystem" as the "Display name" for the zone at runtime.

   ![Procedure](images/75035202443_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/75035202443_DV_resource.Stream@PNG-en-US.png)
5. Repeat these steps for all required connection boxes in the project.

#### Result

The "MixingPlant" zone is configured. The range of the zone is defined by the length of the connecting cable of the Mobile Panel.

The display name designates the zone in the set editing language. An overview of the display names can be found in the "Project texts" editor.

### Calling system functions when connected to the connection box. (Panels, Comfort Panels)

#### Introduction

When entering a zone you have the option of triggering various system functions, e.g. calling a configured pop-up screen or logging the current user in and out. In addition, you can use user-defined VB functions, which you can also select from the toolbar.

In the following example you configure the screen that is displayed when a Mobile Panel is connected to a connection box.

#### Requirements

- A Mobile Panel which supports zones has been created, for example, Mobile Panel KTP700.
- The "MixingPlant" zone is configured.
- The "Plant_1" screen has been created and opened.
- The "MixingPlant_1" screen has been created and opened.
- The "Zones" work area is open.

#### Procedure

1. Select the "MixingPlant" zone from the "Zones" table.
2. Click "Properties> Events" in the Inspector window.
3. Click on the "Connected" event.
4. Select the "ActivateScreen" system function in the "function list".
5. Select "MixingPlant_1" as "Screen name".

#### Result

When you connect your Mobile Panel to the connection box of the "MixingPlant" zone, the "MixingPlant_1" screen appears on the display of the HMI device.

## Reference (Panels, Comfort Panels)

This section contains information on the following topics:

- [PROFIsafe address (Panels, Comfort Panels)](#profisafe-address-panels-comfort-panels)
- [Power Management (Panels, Comfort Panels)](#power-management-panels-comfort-panels)

### PROFIsafe address (Panels, Comfort Panels)

#### Validity

The PROFIsafe address is available for Mobile Panels Wireless and KTP F-devices.

> **Note**
>
> Additional information on fail-safe operation can be found in the operating instructions for the HMI device:
>
> [Complete documentation for Mobile Wireless](http://support.automation.siemens.com/WW/view/en/26268960)

#### PROFIsafe address

The PROFIsafe address used for fail-safe I/Os in PROFIsafe communication is unique on the entire network and on all stations. On the Mobile Panel Wireless, you create a default value in the project and load it to the HMI device. You can also store a PROFIsafe address on the HMI device.

The PROFIsafe address fall within the range from 1 to 65534. The two PROFIsafe addresses (in the Engineering System and on the HMI device) are checked for formal validity.

The PROFIsafe address is loaded as follows at the start of Runtime:

- You programmed a valid PROFIsafe address in the Control Panel.

  The HMI loads the PROFIsafe address set in the Control Panel.

### Power Management (Panels, Comfort Panels)

#### Validity

In the "Runtime Settings > Power Management" editor, configure the energy-saving mode of a Mobile Panel.

#### Power Management

The Mobile Panel Wireless can save energy in the following ways:

- Reduce brightness - some savings
- Switch off screen - high savings

You can also indicate after how long without operator input the power management function is enabled. The communication link is maintained. The time for "Switch off screen" is longer than the time for "Reduce brightness".
