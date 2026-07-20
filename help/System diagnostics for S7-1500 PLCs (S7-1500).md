---
title: "System diagnostics for S7-1500 PLCs (S7-1500)"
package: SysDiagRSE1500enUS
topics: 11
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# System diagnostics for S7-1500 PLCs (S7-1500)

This section contains information on the following topics:

- [Introduction (S7-1500)](#introduction-s7-1500)
- [Basics of system diagnostics (S7-1500)](#basics-of-system-diagnostics-s7-1500)
- [Displaying settings of system diagnostics (S7-1500)](#displaying-settings-of-system-diagnostics-s7-1500)
- [Settings (S7-1500)](#settings-s7-1500)
- [Exporting and importing system diagnostic settings (S7-1500)](#exporting-and-importing-system-diagnostic-settings-s7-1500)

## Introduction (S7-1500)

### Introduction

When a system error occurs, hardware components and devices of other manufacturers (slaves whose properties are set by their GSD file) can trigger a system reaction. The hardware components provide information on the system error that has occurred.

For S7-1500 PLCs, the system diagnostics provides a convenient way to evaluate this diagnostic information and display it in the form of alarms.

In addition, additional diagnostic information allows the error to be specified in more detail, e.g., channel "switch_top", wire break, or measuring range exceeded.

## Basics of system diagnostics (S7-1500)

You can use the system diagnostics to analyze errors in the system and generate alarms with a written error description and an indication of the error location.

These alarms are defined for each component with alarm capability (e.g., channel fault, rack error).

### Recommended procedure

Make the settings for the system diagnostics and the structure of the alarms.

You will find detailed information in the sections below.

## Displaying settings of system diagnostics (S7-1500)

### Requirement

You are in the "Common data" folder in the project tree.

### Procedure

To display and edit the settings for system diagnostics, follow these steps:

1. Double-click the "System diagnostics settings" entry.
2. You can view and edit the settings in the system diagnostics.

## Settings (S7-1500)

This section contains information on the following topics:

- [General settings (S7-1500)](#general-settings-s7-1500)
- [Alarm settings (S7-1500)](#alarm-settings-s7-1500)

### General settings (S7-1500)

#### Using fixed numbers for message IDs

If you select this option, make sure that the system diagnostics messages are given fixed message numbers (1–512) that do not change if, for example, the user changes the order of the message types.

#### Signaling network errors as maintenance demanded instead of errors

If you select this option, network errors will be reported as 'Maintenance demanded' (CPU firmware version 2.5 and later).

#### Suppressing messages about deactivating IO devices

If you select this option, no messages will be displayed if there are inactive IO devices in your project (CPU firmware version 3.0 and later).

### Alarm settings (S7-1500)

For the alarm categories listed below, you can define whether an alarm is output and whether or not this alarm requires acknowledgment:

- Error
- Maintenance demanded
- Maintenance required
- Info

To do this, select the relevant options in the "Alarm" and "Acknowledgment" columns.

The set alarm class is displayed in the "Alarm class" column.

The set priority of the alarm class is displayed in the "Priority" column.

## Exporting and importing system diagnostic settings (S7-1500)

This section contains information on the following topics:

- [Basics for exporting and importing system diagnostic settings (S7-1500)](#basics-for-exporting-and-importing-system-diagnostic-settings-s7-1500)
- [Exporting system diagnostic settings (S7-1500)](#exporting-system-diagnostic-settings-s7-1500)
- [Importing system diagnostic settings (S7-1500)](#importing-system-diagnostic-settings-s7-1500)

### Basics for exporting and importing system diagnostic settings (S7-1500)

#### Description

You can export the system diagnostic settings of a project and import them into another project. The advantage of importing these settings is that they do not have to be created separately for each project.

The system diagnostic settings are saved in a data file (*.dat).

### Exporting system diagnostic settings (S7-1500)

#### Requirement

A project is open.

#### Procedure

To export the system diagnostic settings, follow these steps:

1. In the project tree, click on the "Shared data" folder and double-click "System diagnostic settings".
2. In the system diagnostics, click on the "Exporting system diagnostic settings" icon in the toolbar. The "Save as" dialog opens.
3. Select the path to which you want to save the export file.
4. Click the "Save" button.

#### Result

A .dat file is created at the selected memory location.

### Importing system diagnostic settings (S7-1500)

#### Requirement

The project into which you want to import the system diagnostic settings is open.

#### Procedure

To import the system diagnostic settings, follow these steps:

1. In the project tree, click on the "Shared data" folder and double-click "System diagnostic settings".
2. In the system diagnostics, click on the "Importing system diagnostic settings" icon in the toolbar. The "Open" dialog opens.
3. Select the path where the file to be imported is stored.
4. Select the required .dat file.
5. Click the "Open" button.

> **Note**
>
> The "Import" icon is grayed out when the open project is read-only (e.g. reference object).
>
> If an error occurs during the import, an alarm is displayed and the process is aborted.

#### Result

The system diagnostic settings are displayed.
