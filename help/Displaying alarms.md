---
title: "Displaying alarms"
package: DiagPLCMenUS
topics: 15
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Displaying alarms

This section contains information on the following topics:

- [Overview of the alarm display](#overview-of-the-alarm-display)
- ["Current alarms" view](#current-alarms-view)
- [Layout of the alarms in the "Current alarms" view](#layout-of-the-alarms-in-the-current-alarms-view)
- [Alarm archive](#alarm-archive)
- [Layout of the alarms in the alarm archive](#layout-of-the-alarms-in-the-alarm-archive)
- [Clear alarm archive completely](#clear-alarm-archive-completely)
- [Export archive](#export-archive)
- [Receiving alarms](#receiving-alarms)
- [Freeze alarms](#freeze-alarms)
- [Acknowledging alarms](#acknowledging-alarms)
- [Status of the alarms](#status-of-the-alarms)
- [Sort table in alarm display](#sort-table-in-alarm-display)
- [Filter table in alarm display](#filter-table-in-alarm-display)
- [Keyboard commands in the alarm display](#keyboard-commands-in-the-alarm-display)

## Overview of the alarm display

The "Alarm display" function can be used to output asynchronous alarms of diagnostics events and user-defined diagnostics alarms as well as alarms from ALARM instructions.

A note is displayed in case of an overflow of diagnostics events. As soon as the overflow has been eliminated, alarms of the types NOTIFY_AP and ALARM_AP are signaled. Only diagnostics events that are still active after the overflow are signaled. Any diagnostics events that occurred during the overflow and went out again are not signaled (no alarm history).

From the alarm display, you can also start the alarm editor with the "Edit alarm" shortcut menu command and then create user diagnostics alarms.

### Icons

The following table shows the icons and their functions:

| Icon | Function |
| --- | --- |
| ![Current alarms](images/96182198155_DV_resource.Stream@PNG-de-DE.PNG)   Current alarms | Shows the currently active (pending) alarms. Alarms that must be acknowledged are shown in blue lettering. |
| ![Alarm archive](images/96182637579_DV_resource.Stream@PNG-de-DE.PNG)   Alarm archive | Shows the alarms located in the archive. |
| ![Clear alarm archive completely](images/96182641803_DV_resource.Stream@PNG-de-DE.PNG)   Clear alarm archive completely | Deletes all alarms in the archive (even with set filter). |
| ![Export archive](images/96182646027_DV_resource.Stream@PNG-de-DE.PNG)   Export archive | Exports the current alarm archive to a file in xml format. |
| ![Multiple lines](images/66606773003_DV_resource.Stream@PNG-de-DE.PNG)   Multiple lines | Shows the alarms with multiple lines. |
| ![Freeze alarms](images/96186890507_DV_resource.Stream@PNG-de-DE.PNG)   Freeze alarms | Freezes the display of the alarms |
| ![Acknowledge alarm(s)](images/96183772171_DV_resource.Stream@PNG-de-DE.PNG)   Acknowledge alarm(s) | Confirms the selected alarm(s) as read. Alarms requiring acknowledgment are shown in blue lettering. |
| ![Filter](images/101750095115_DV_resource.Stream@PNG-de-DE.PNG)   Filter | Shows the filter for the alarm display. If filter criteria are selected, the icon has a green check mark. |

## "Current alarms" view

The "Current alarms" view is an image of the alarm acknowledgement memory of the selected CPU(s).

## Layout of the alarms in the "Current alarms" view

The "Current alarms" view represents an image of the alarm acknowledgment memory of the selected CPUs. One entry is shown in the table per active alarm. Events of an alarm ("incoming", "outgoing" and "acknowledged") are displayed in one row.

### Table structure

All attributes of the alarms can be shown as columns. You can show or hide individual columns as well as modify the width and order of the columns. These settings are saved when the project is closed.

You can sort the columns in ascending or descending order. The sorting of the columns depends on whether the "Freeze alarms" is activated or not.

The alarms can be displayed in one or more rows. In the single row display, only the first row of the multiple-row alarm data is displayed.

The alarms either require acknowledgment or do not require acknowledgment. The alarms requiring acknowledgment that have not yet been acknowledged are highlighted in bold print and can be acknowledged either with the button in the toolbar for the specific context or with the shortcut menu command "Acknowledge alarm(s)".

---

**See also**

[Sort table in alarm display](#sort-table-in-alarm-display)

## Alarm archive

In the alarm archive, alarms are displayed and archived according to the time they appear. You can set the size of the archive (between 200 and 3000 alarms) with the menu command "Options &gt; Settings &gt; Online &amp; Diagnostics". If the selected archive size is exceeded, the oldest alarm it contains is deleted.

Alarms that must be acknowledged are displayed in blue lettering and can be acknowledged with the shortcut menu command "Acknowledge alarm(s)".

The archive is constantly updated and does not need to be saved explicitly.

---

**See also**

[Clear alarm archive completely](#clear-alarm-archive-completely)
  
[Export archive](#export-archive)

## Layout of the alarms in the alarm archive

In the alarm archive, all events occurring on the selected CPUs are logged. A new entry is created for each individual event and shown as a further row in the table.

### Table structure

All attributes of the alarms can be shown as columns. You can show or hide individual columns as well as modify the width and order of the columns. These settings are saved when the project is closed.

You can sort the columns in ascending or descending order. The sorting of the columns depends on whether the "Freeze alarms" is activated or not.

The alarms can be displayed in one or more rows. In the single row display, only the first row of the multiple-row alarm data is displayed.

The alarms either require acknowledgment or do not require acknowledgment. The alarms requiring acknowledgment that have not yet been acknowledged are highlighted in blue lettering and can be acknowledged either with the button in the toolbar for the particular context or with the shortcut menu command "Acknowledge alarm(s)".

---

**See also**

[Sort table in alarm display](#sort-table-in-alarm-display)

## Clear alarm archive completely

The archive is organized as a ring buffer, in other words, when it is full, the oldest alarms are deleted from the archive. With the "Clear alarm archive completely" button, you delete the entire archive, regardless of whether or not you have selected filter criteria to display specific alarms.

### Procedure

To clear the archive, follow these steps:

1. Click the "Clear alarm archive completely" icon in the toolbar of the alarm display.

## Export archive

To archive alarms, you can export the archive. To do this, follow these steps:

1. Change to the alarm archive.
2. Click the "Export archive" icon.
3. In the dialog that opens, select the path to export the archive.

### Result

The archive is saved as an xml file at the location you selected.

## Receiving alarms

To allow alarms to be displayed, you must first set the receipt of alarms for each CPU.

### Procedure

Toe receive alarms, follow these steps:

1. Double-click on the "Online &amp; Diagnostics" folder of the relevant CPU in project navigation.
2. Click the "Online access" group in the area navigation.
3. Select the option "Receive alarms".

**Note**

If you select this procedure, alarms are only received after you have re-established an online connection to the device.

Or:

1. Select the relevant CPU in the device, network, or topology view.
2. Select the command "Receive alarms" in the "Online" menu or in the shortcut menu.

Or:

1. Select the CPU in project navigation.
2. Select the command "Receive alarms" in the "Online" menu or in the shortcut menu.

Or:

1. In the alarm view, select the desired devices for which you want to receive alarms from the drop-down list "Show alarms".

   - If no project is open, does not contain an online device or a device has not (yet) been selected, the entry "No device selected" is displayed.
   - If you click on the project name, all the subordinate devices are selected and the entry "All devices selected" is displayed
   - If you select individual devices in the project, the entry "Multiple devices selected" is displayed.
2. Confirm your selection by clicking on the green check mark below the drop-down list.

**Note**

If you select one of the three above-named procedures, you must have first established an online connection to the device.

## Freeze alarms

Provides a snapshot of the alarm view in which the screen was frozen. If you click the button again, the updating of the alarms is enabled again.

### The button "Freeze alarms" is not activated.

You can only sort the alarms by the columns "Date" and "Time". These settings are saved when the project is closed. Depending on the sorting order, current alarms are displayed at the beginning or the end of the table.

### The "Freeze alarms" button is activated.

You can sort every column of the table. If you deactivate the button again, the set sorting is, however, lost again.

## Acknowledging alarms

Alarms that must be acknowledged are shown in blue lettering.

### Procedure

To acknowledge an alarm, follow these steps:

1. Select the required alarm or alarms from the table.
2. Click on the "Acknowledge alarms" button.

**Note**

You can select more than one alarm to acknowledge at the same time. To do this, hold down the &lt;Ctrl&gt; key and then select the alarms you want to acknowledge.

### Result

The selected alarm was acknowledged and is then shown in normal characters.

> **Note**
>
> In the "Current alarms" view, acknowledged alarms that have already gone are no longer displayed.

## Status of the alarms

Depending on whether you are in the "Current alarms" view or the alarm archive, the displayed alarms may have a different status.

### Status of the alarms in the "Current alarms" view

- I: Alarm came
- IA: Alarm came and was acknowledged
- IO: Alarm has gone

If more signal changes occur than can be sent (signal overflow), OV is displayed as the status and the status is shown in red.

### Status of the alarms in the alarm archive

- No information: only with alarms generated by the PG/PC and displayed in the "Archive" tab, for example logon status, connection abort, mode changes
- I: Alarm came
- A: Alarm came and was acknowledged
- O Alarm has gone
- D: The alarm was deleted.

If more signal changes occur than can be sent (signal overflow), OV is displayed as the status and the status is shown in red.

## Sort table in alarm display

### Sorting a table in ascending or descending order

To sort the table by a column in ascending or descending order, follow the steps below:

1. Click the table header of a column if you want to sort the column in ascending order.
2. Click again on the same column of the table header to sort the column in descending order.
3. Click a third time on the table header of the same column to cancel the sorting.

### The button "Freeze alarms" is not activated.

You can only sort the alarms by the columns "Date" and "Time". These settings are saved when the project is closed.

### The "Freeze alarms" button is activated.

You can sort every column of the table. If you deactivate the button again, the set sorting is, however, lost again.

## Filter table in alarm display

You can filter all columns except the "Help" column. This is possible in the "Current alarms" and "Alarm archive" views as well as in active mode (alarms are constantly updated) and in the "Freeze alarms" mode.

As soon as a filter criterion is selected, a green check mark appears in the filter icon. If a filter criterion is defined for a column, the corresponding field has an orange background.

### Procedure

To filter alarms, follow these steps:

1. Enter a filter criterion in the field.
2. Confirm your entry with the enter key or click any other area to select the filter.  
   Up to five filter criteria per column are saved in a drop-down list. You can select the filters from here as needed.
3. If necessary, repeat the procedure for all other required criteria.

### Result

Only alarms that correspond to the set criterion (or criteria) are displayed.

If filter criteria are set in the message display when you close the project, these are displayed again when you re-open this (or any other) project. However, these settings are lost when you close the TIA Portal.

## Keyboard commands in the alarm display

### Alarm display

| Function | Shortcut keys |
| --- | --- |
| Select all alarms | Ctrl+A |
| Acknowledge all selected alarms | Ctrl+Q |
