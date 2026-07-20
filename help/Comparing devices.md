---
title: "Comparing devices"
package: HWCNDevCompare2MenUS
topics: 3
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Comparing devices

This section contains information on the following topics:

- [Basics of device comparison](#basics-of-device-comparison)
- [Making a device comparison](#making-a-device-comparison)

## Basics of device comparison

### Function

You have the option of comparing the hardware components of two devices allowing you to identify any differences. You can perform an offline/offline comparison for this purpose. The devices to be compared can be from one project or different projects.

You can compare the central as well as the distributed I/O. The devices to be compared can be assigned either automatically or manually. The automatic assignment of central I/O is based on the slot number. With the distributed I/O, the automatic assignment can be made according to the following criteria:

- Assignment using the address/HW ID: The assignment is made using the addresses or IDs of the devices. This criterion is suitable for comparing devices within a project.
- Assignment using the name: The assignment is made based on the device names. This criterion is suitable for comparing devices in different projects.

You can either specify the assignment yourself or let the system decide. In the latter case, the system selects the assignment itself depending on the context.

To compare the modules of the distributed I/O, start an offline/offline comparison for the affected distributed stations.

In the compare editor, you can start a detailed comparison for devices of the same type with the same article number. This gives you a clear comparison of the parameters of the devices and allows you to see at a glance which parameters are different.

---

**See also**

[Basics of project data comparison](Editing%20project%20data.md#basics-of-project-data-comparison)
  
[Overview of the compare editor](Editing%20project%20data.md#overview-of-the-compare-editor)
  
[Making a device comparison](#making-a-device-comparison)

## Making a device comparison

You can compare any devices to see the differences between them. When comparing devices of the same type with the same article number, you can also compare the parameters of the devices using a detailed comparison.

### Making a device comparison

Follow the steps below to compare devices:

1. Select a device in the project tree that allows offline/offline comparison.
2. Select the "Compare &gt; Offline/offline" command in the shortcut menu.

   The compare editor opens and the selected device is displayed in the left area.
3. Open the "Hardware" tab.
4. Drag an additional device to the drop area in the right-hand pane.

   All existing objects of the selected devices are displayed depending on the settings of the compare editor in the "Hardware" tab and an automatic comparison is made. You can identify the status of the comparison objects based on the symbols in the compare editor. For submodules, you can find detailed results in the "Property comparison" area.
5. If you want to change the matching criterion, click on the arrow of the "Display available assignment criteria" in the toolbar. Then, select the matching criterion you want to use.
6. If you want to make a manual comparison, click the button for switching between automatic and manual comparison above the status area. Then select the objects you want to compare.

   The properties comparison is displayed. You can see the status of the objects based on the symbols.

### Making a detailed comparison

To compare the parameters of devices of the same type and with the same article number, proceed as follows:

1. First, perform a device comparison.
2. Double-click a device for which you want to compare the parameters. Alternatively, select the "Start detailed comparison" command from the shortcut menu or click "Start detailed comparison" in the function bar.

   Another window opens listing the parameters of the two devices. The status icons allow you to see where there are differences. Expand the corresponding groups so that you can see the parameters that are different.

> **Note**
>
> **Distributed I/O**
>
> When you start the device comparison from the CPU level and want to start the detailed comparison for distributed I/O, you must carry out the detailed comparison twice. When the detailed comparison is started for the first time, there is a device comparison of the distributed I/O devices, which is displayed in the compare editor. Then carry out the detailed comparison for the desired distributed I/O system again. The detailed comparison is then displayed for these devices.

---

**See also**

[Basics of device comparison](#basics-of-device-comparison)
  
[Overview of the compare editor](Editing%20project%20data.md#overview-of-the-compare-editor)
