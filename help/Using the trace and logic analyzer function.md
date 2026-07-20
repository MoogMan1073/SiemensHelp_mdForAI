---
title: "Using the trace and logic analyzer function"
package: TFTraceEditorenUS
topics: 94
devices: [S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using the trace and logic analyzer function

This section contains information on the following topics:

- [Description](#description)
- [Trace software user interface](#trace-software-user-interface)
- [Project trace software user interface](#project-trace-software-user-interface)
- [Long-term project trace software user interface](#long-term-project-trace-software-user-interface)
- [Operation](#operation)
- [Devices](#devices)
- [Glossary](#glossary)

## Description

This section contains information on the following topics:

- [Supported hardware](#supported-hardware)
- [Recording of measured values with the trace function](#recording-of-measured-values-with-the-trace-function)
- [Trace configuration, recording, installed trace and measurement](#trace-configuration-recording-installed-trace-and-measurement)
- [Data storage](#data-storage)
- [Long-term trace (S7-1500)](#long-term-trace-s7-1500)
- [Project trace](#project-trace)
- [Long-term project trace](#long-term-project-trace)

### Supported hardware

If a device supports the trace and logic analyzer function, ![Figure](images/171753628939_DV_resource.Stream@PNG-de-DE.png) "Traces" is offered for selection in the project tree below the device.

The following [devices](#devices) support the trace and logic analyzer function:

- SIMATIC S7-1200 CPUs (as of firmware version V4.0)
- SIMATIC S7-1500, ET 200SP, CPU 1513pro-2 PN and CPU 1516pro-2 PN CPUs
- SIMATIC S7-1500 Software Controller
- SIMATIC Drive Controller
- ET 200SP Open Controller
- SINAMICS drives that are supported in Startdrive
- SINAMICS V90 (with HSP 0185)
- SIRIUS SIMOCODE pro (with Simocode ES)
- SIRIUS Soft Starter 3RW (with Soft Starter ES)

### Recording of measured values with the trace function

#### Introduction

The trace and logic analyzer function can be called in the [project tree](#structure-of-the-user-interface) by double-clicking an entry in the "Traces" system folder. The measurements on the memory card can also be read and displayed via the diagnostic interface of the Web server.

You record device tags and evaluate the recordings with the trace and logic analyzer function. Tags are, for example, drive parameters or system and user tags of a CPU. The number of installed traces is hardware-dependent. You can use the project trace to record tags from multiple devices across devices.

The recordings are saved on the device and, when required, can be read out with the engineering system (ES) and saved permanently. The trace and logic analyzer function is therefore suitable for monitoring highly dynamic processes. The recorded values are overwritten when the recording is activated again.

The trace and logic analyzer functions are also used in the commissioning editors of technology objects (for example, axle control panels). Active recordings from the axis control panel are displayed in the "Traces" system folder as installed traces. Recordings can be added to the measurements in the curve diagram of the axis control panel or the PID via a shortcut menu command.

Depending on the [device](#devices) used, the recording options can vary.

A [quick start](#trace-quick-start) for working with the trace and logic analyzer function can be found in the Operation section.

The following figure shows the mode of operation of the trace:

![Introduction](images/171753632907_DV_resource.Stream@PNG-en-US.png)

**① Trace configuration on the programming device (PG) in the TIA Portal**

You can specify the signals to be recorded, the duration of the recording and the trigger condition in the trace configuration. The trace configuration depends on the device and is described at the respective [device](#devices).

**② Transferring the trace configuration from the PG to the device**

You can transfer the complete trace configuration to the device when an online connection is established.

**③ Waiting for the recording**

If the installed trace configuration is [activated](#activatingdeactivating-an-installed-trace), then the recording is performed independently of the PG. The recording is started as soon as the trigger condition is satisfied.

**④ Transferring the measurement from the device to the PG**

The [saving of the measurement in the project](#saving-measurements-in-the-project) stores the measurement in the opened project of the TIA Portal. The measurement can be saved at any time after completing the recording, irrespective of the time of the measurement.

**⑤ Evaluating, managing and saving the measurement**

Numerous options are available for the evaluation of the measurement in the curve diagram and in the signal table. Various display types are possible, for example, a bit representation for binary signals.  
Signal waves from different measurements can be put together as an combined measurement and compared with each other.   
Measurements can also be exported and imported as a file.  
With the [saving of the project](#saving-measurements-in-the-project) in the TIA Portal, the measurements transferred to the project are also saved.

---

**See also**

[Transferring the trace configuration from the device to the project](#transferring-the-trace-configuration-from-the-device-to-the-project)

### Trace configuration, recording, installed trace and measurement

This section explains the meaning and relationships of the terms: trace configuration, recording, installed trace and measurement.

#### Trace configuration

Implement the following settings in the ![Trace configuration](images/171753805579_DV_resource.Stream@PNG-de-DE.png) trace configuration:

- Signals to be recorded with display options
- Recording conditions

  - Sampling
  - Trigger
  - Measurements on device (memory card)

Trace configurations can be copied to the "Traces" folder by drag-and-drop operation or by means of the clipboard. The application of a configuration depends on the device type. The following sources are possible:

- Trace configuration
- Measurement
- Measurements on device (memory card)
- Combined measurement (selection of a measurement contained in it)

#### Recording

A recording is performed in the device. There is only one recording for each installed trace configuration. When a new recording is started, the old recording is overwritten.

An installed recording is not retentive (it is lost when the device is switched off/on) but can be saved permanently in the project as a measurement.

#### Installed trace

An installed trace ![Installed trace](images/171754030347_DV_resource.Stream@PNG-de-DE.png) consists of a trace configuration and optionally a recording. The maximum number of installed traces depends on the device.

The trace configuration is stored retentively on the device. The retentivity of the trace configuration may also be configurable depending on the device, e.g. with the S120.

The configuration data is displayed write-protected.

#### Measurement

A measurement ![Measurement](images/171753809163_DV_resource.Stream@PNG-de-DE.png) consists of a trace configuration and a recording, provided that recorded data is present. Each installed trace can be saved as a measurement in the project.

The recording of a measurement can be viewed offline.

The configuration data is displayed write-protected.

#### Measurements on device (memory card)

The ![Measurements on device (memory card)](images/171754038283_DV_resource.Stream@PNG-de-DE.png) "Measurements on device (memory card)" folder contains measurements that are saved on the device (for example, on the memory card). These measurements are retentive and can only be deleted by the user.

The installed measurements can be transferred to the "Measurements" folder using drag &amp; drop and are then saved as measurements in the project.

#### Trace configuration with an installed trace of the same name

Usually, there is a trace configuration in the project with the same name for an installed trace. When there is an online connection, this trace is displayed with the ![Trace configuration with an installed trace of the same name](images/171754034315_DV_resource.Stream@PNG-de-DE.png) icon in the project tree.

See also [User interface - “Traces” project tree folder](#user-interface---traces-project-tree-folder).

#### Combined measurement

The combined measurement ![Combined measurement](images/171754042251_DV_resource.Stream@PNG-de-DE.png) allows a comparison and analysis of signals from different measurements with each other.

Measurements can be synchronized with each other and displayed overlaid.

Changes to the settings for measurements within the combined measurement have no impact on the original measurements. The original measurements remain unchanged.

---

**See also**

[Data storage](#data-storage)
  
[Saving measurements in the project](#saving-measurements-in-the-project)
  
[Devices](#devices)

### Data storage

The trace toolbar and the curve diagram also enable the transfer of the trace configuration and the viewing of the recording.

The following figure is a schematic diagram of the data storage:

![Figure](images/171754174219_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Saving the trace configuration and measurement**
>
> You save the trace configuration and measurement with the project in the TIA Portal.
>
> If you close the project without saving, the trace configurations and the measurements transferred to the project are discarded. The trace editor can be closed and reopened without loss of data until the project is closed.

---

**See also**

[Transferring the trace configuration from the device to the project](#transferring-the-trace-configuration-from-the-device-to-the-project)
  
[Activating/deactivating an installed trace](#activatingdeactivating-an-installed-trace)
  
[Saving measurements in the project](#saving-measurements-in-the-project)
  
[User interface - curve diagram](#user-interface---curve-diagram)

### Long-term trace (S7-1500)

A long-term trace records signals.

In contrast to trace, long-term trace has the following special features:

- In the long-term trace configuration, you define a target path in the PG. The long-term trace recording is saved as a .csv file and as an .lttcd file in the configured target path on the PG.
- You cannot configure a recording duration or a trigger.
- No support of measurements in the device (memory card)
- No support for FFT/Bode formulas or FFT diagrams/Bode diagram

A description of which devices support the long-term trace is provided at the respective [devices](#devices).

#### Long-term trace workflow

A [Quick Start](#quick-start-for-long-term-trace-s7-1500) for working with long-term traces can be found in the Operation section.

The following figure shows how the long-term trace works:

![Long-term trace workflow](images/171754180491_DV_resource.Stream@PNG-en-US.png)

**① Long-term trace configuration on the programming device (PG) in the TIA Portal**

You can define the signals to be recorded and the target path for the long-term trace measurements in the long-term trace configuration. The long-term trace configuration depends on the device and is described for the respective [devices](#devices).

**② Transferring the long-term trace configuration from the PG to the device**

You can transfer the complete long-term trace configuration to the device when an online connection is established.

**③ Starting the long-term trace recording and saving the long-term trace measurement in the target path**

You start the long-term trace recording by activating the trace configuration. The long-term trace recording is displayed in the time diagram.

The long-term trace measurement is saved as a .csv file and as an .lttcd file in the configured target path on the PG.

You can find additional information about long-term trace recording as a csv file in the section [Long-term trace recording](S7-1200-1500%20CPUs%20%28S7-1200%2C%20S7-1500%29.md#long-term-trace-recording-s7-1500).

> **Note**
>
> Note that problems with online access between the PG and the CPU can result in errors or even failure of the recording.
>
> If possible, connect the PG directly to the CPU.

**④ Displaying, managing, and evaluating the long-term trace measurement**

For evaluation, you can add the long-term trace measurement to the system folder "Measurements".

Numerous options are available for the evaluation of the measurement in the curve diagram and in the signal table. Various display types are possible, for example, a bit representation for binary signals.

In the "Combined measurements" folder, you can compare and analyze signals from different long-term trace measurements. The combined long-term trace measurements can be synchronized with each other and displayed in combination. Changes to the settings of long-term trace measurements within the combined long-term trace measurement do not affect the original long-term trace measurements. The original long-term trace measurements remain unchanged.

---

**See also**

[Saving measurements in the project](#saving-measurements-in-the-project)

### Project trace

This section contains information on the following topics:

- [General](#general)
- [Time synchronization](#time-synchronization)

#### General

A project trace includes trace configurations of multiple devices and records the signals across devices.

Each device can trigger the recording on all participating devices. After receiving the global trigger, the devices with valid project trace configuration start the recording.

Each of the respective [devices](#devices) describes whether the project trace function is supported.

##### Requirements

The following requirements must be fulfilled for recording with project trace:

- PROFINET RT or IRT communication
- All devices are located in a PROFINET subnet (no routing)
- An online connection from the TIA Portal to all devices to transfer the project trace to the devices.
- The "Record immediately" trigger mode may be configured for a maximum of one device.
- A trigger must be configured for at least one device.

#### Time synchronization

The accuracy of the time synchronization depends on how the trace sample event is determined. Isochronous communication provides the highest accuracy because the IRT cycle is used. In all other cases, the respective time of the device where the signals are recorded is used.

A project trace can contain devices with RT and IRT communication.

For a synchronous display of the signals, the X axis must be set in "Time (relative)" mode. In this representation, the measurements are arranged in time so that their trigger events are at 0 ms.

To facilitate the evaluation with absolute time, synchronize the clock times of the devices.

Information on the trace sample event can be found in the device-specific descriptions, e.g. for [S7-1200/1500 CPU](#devices) under "Recording levels".

##### Trigger time for RT communication

Devices which receive the trigger from another device, have a time-delayed trigger event. For RT communication, the time of a trigger event is derived from the transfer time and the recording time. The trigger event is first detected at the end of the recording OB and uses this time as the trigger time. The time delay between the original trigger time and the evaluation in the OB cannot be determined for RT communication. This means the signal trends of devices which receive the trigger from another device appear moved forward. After saving the measurements, you can manually correct these signals with a time offset.

##### Example of a recording with project trace

The figure below shows a recording with project trace and the correction of the representation with an offset.

![Example of a recording with project trace](images/171754339979_DV_resource.Stream@PNG-en-US.png)

### Long-term project trace

This section contains information on the following topics:

- [General](#general-1)
- [Time synchronization](#time-synchronization-1)

#### General

A long-term project trace contains trace configurations of multiple devices and records the signals across devices. In STEP 7, you activate the recording of the long-term project trace in all devices at the same time. All recorded signals are displayed together in a synchronous diagram. The number of long-term project trace configurations is not limited.   
In contrast to project trace, there are the following special features of long-term project trace:

- In the long-term project trace configuration, you define a target path in the PG. The long-term project trace recording is saved as a .csv file and as an .lttcd file in the configured target path on the PG.
- You cannot configure a recording duration, a trigger and a sample count.

Each of the respective [devices](#devices) describes whether the long-term project trace function is supported.

> **Note**
>
> The number of devices that can be in the respective long-term trace configuration is limited to 5.

##### Long-term project trace workflow

A [Quick Start](#quick-access-to-the-long-term-project-trace) for working with long-term project traces can be found in the Operation section.

The following figure shows how the long-term project trace works:

![Long-term project trace workflow](images/166889336587_DV_resource.Stream@PNG-en-US.png)

**① Long-term project trace configuration on the programming device (PG) in the TIA Portal**

In the long-term project trace configuration, you define the signals to be recorded and the target path for the long-term project trace recordings.

**② Transferring the long-term project trace configuration from the PG to the device**

You can transfer the complete long-term project trace configuration to the device when an online connection is established.

**③ Start long-term project trace recording and save in target path.**

Start the recording by activating the trace configuration. The long-term project trace recording is displayed in the time diagram.

The long-term project trace measurement is saved as a .csv and as a .lttcd file in the configured target path.

You can find additional information about long-term project trace recording as a csv file in the section [Long-term project trace recording](S7-1200-1500%20CPUs%20%28S7-1200%2C%20S7-1500%29.md#long-term-project-trace-recording-s7-1200-s7-1500).

> **Note**
>
> Note, if there are problems in the online access between PG and the CPU, the recording may be disturbed or even fail.  
> Connect the PG directly to the CPU if possible.

**④ Displaying, managing, and evaluating the long-term project trace measurement**

For evaluation, you can add the long-term project trace measurement to the system folder "Measurements".

Numerous options are available for the evaluation of the measurement in the curve diagram and in the signal table. Various display types are possible, for example, a bit representation for binary signals.

##### Requirements

The following requirements must be fulfilled for recording with long-term project trace:

- S7-1500 CPU
- PROFINET RT or IRT communication
- All devices are located in a PROFINET subnet (no routing)
- An online connection from the TIA Portal to all devices to transfer the project trace to the devices.

---

**See also**

[Saving measurements in the project](#saving-measurements-in-the-project)

#### Time synchronization

The accuracy of the time synchronization depends on how the trace sample event is determined. Isochronous communication provides the highest accuracy because the IRT cycle is used. In all other cases, the clock time of the device is used.

A long-term project trace can contain devices with RT and IRT communication.

For a synchronous display of the signals, the X axis must be set in "Time (relative)" mode. In this representation, the measurements are arranged in time so that the start of recording is always at the time 0 ms.

To facilitate the evaluation with absolute time, synchronize the clock times of the devices.

You can find information on the trace sample event in the device-specific descriptions, e.g. for S7-1200/1500 CPU under "Recording level".

## Trace software user interface

This section contains information on the following topics:

- [Structure of the user interface](#structure-of-the-user-interface)
- [Project tree](#project-tree)
- [Working area](#working-area)
- [Inspector window](#inspector-window)
- [Trace task card](#trace-task-card)

### Structure of the user interface

The user interface of the trace and logic analyzer function consists of several areas. The layout of the user interface in the TIA Portal is described here.

The figure below shows an example of the distribution of the surface:

![Figure](images/171756687371_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| **Project tree**   Management and creation of the trace and measurements directly in the project tree and via context menu commands. |  |
| **Working area** |  |
|  | ① Title bar of the working area  Shows the device to which the current display belongs. |
| ② Trace toolbar  Buttons for managing the trace in the project and device:  - Activation/deactivation of installed traces - Deletion of installed traces - Transfer of trace configurations and measurements between the device and the project - Export of trace configurations and measurements - Switchover between offline and online display |  |
| ③ Status display of the trace   Display of the current status of the recording. |  |
| ④ Configuration tab  Device-specific configuration of the recording duration, trigger condition and signal selection.  Configuring the devices for project trace.  See [Device-specific descriptions](#devices). |  |
| ⑤ Time diagram / FFT diagram / Bode diagram tab  Display of the recorded values as a curve diagram, FFT diagram or Bode diagram, and the signals from the displayed measurement.   Specification of the display options. |  |
| Signal selection tab  Display of all signals that are contained in the combined measurements. |  |
| **"Trace" task card**   Display of the measurement cursor data with mathematical evaluation ⑥ and snapshots. |  |
| **⑦ Inspector window**   Display of general information about the trace configuration |  |

### Project tree

This section contains information on the following topics:

- [User interface - “Traces” project tree folder](#user-interface---traces-project-tree-folder)
- [User interface - “Measurements” project tree folder](#user-interface---measurements-project-tree-folder)
- [User interface - “Installed measurements (memory card)” project tree folder](#user-interface---installed-measurements-memory-card-project-tree-folder)
- [User interface - "Combined measurements" project tree folder](#user-interface---combined-measurements-project-tree-folder)
- [User interface - "Long-term traces" project tree folder (S7-1500)](#user-interface---long-term-traces-project-tree-folder-s7-1500)

#### User interface - “Traces” project tree folder

Trace configurations and installed traces are displayed in the ![Figure](images/171753628939_DV_resource.Stream@PNG-de-DE.png) "Traces" folder.

More information about the "Traces" sub-folder is provided in the following sections.

Double-click a trace to open the corresponding "Configuration" or "Time diagram" tab in the working area.

##### Icons in the "Traces" folder

The following table explains the icons in the ![Icons in the "Traces" folder](images/171753628939_DV_resource.Stream@PNG-de-DE.png) "Traces" folder:

| Icon | Description |
| --- | --- |
| ![Icons in the "Traces" folder](images/171754594571_DV_resource.Stream@PNG-de-DE.png) | Add trace configuration  Double-click the icon to add a new trace configuration. |
| ![Icons in the "Traces" folder](images/171754347403_DV_resource.Stream@PNG-de-DE.png) | Trace configuration (offline)  Double-click the icon to open the "Configuration" tab. |
| ![Icons in the "Traces" folder](images/171754030347_DV_resource.Stream@PNG-de-DE.png) | Installed trace (online)  The icon is only displayed when there is no offline trace configuration of the same name for the installed trace.  Double-click the icon to open the "Time diagram" tab. |
| ![Icons in the "Traces" folder](images/171754034315_DV_resource.Stream@PNG-de-DE.png) | Trace configuration with an installed trace of the same name  If the ![Icons in the "Traces" folder](images/171754623243_DV_resource.Stream@PNG-de-DE.png) button is deactivated, the trace configuration from the project is displayed. The trace corresponds to a trace configuration.  If the ![Icons in the "Traces" folder](images/171754627211_DV_resource.Stream@PNG-de-DE.png) button is activated, the trace configuration from the device is displayed. The trace corresponds to an installed trace.  Double-click on the symbol to open the "Time diagram" tab of the installed trace. |

##### Status

When there is an online connection, the status is displayed in the right-hand column of the project tree. The status is also displayed as tooltip above the respective icon.

The following table shows the meaning of the icons:

| Icon | Description |
| --- | --- |
| ![Status](images/171754602507_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are identical |
| ![Status](images/171754598539_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are different |
| ![Status](images/171754619275_DV_resource.Stream@PNG-de-DE.png) | Configuration only exists online |

##### **Shortcut menu commands**

The following table shows the shortcut menu commands for the ![Shortcut menu commands](images/171753628939_DV_resource.Stream@PNG-de-DE.png) "Traces" system folder:

| Shortcut menu command | Description |
| --- | --- |
| "Add new group" | Inserts a new folder. |
| "Add new trace" | Inserts a new trace configuration and opens the configuration tab. |
| "Import trace configuration" | Imports a trace configuration from a file. |

The following table shows the shortcut menu commands for trace configurations ![Shortcut menu commands](images/171754347403_DV_resource.Stream@PNG-de-DE.png) and installed traces ![Shortcut menu commands](images/171754034315_DV_resource.Stream@PNG-de-DE.png) / ![Shortcut menu commands](images/171754030347_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Trace configuration | Installed trace | Description |
| --- | --- | --- | --- |
| "Copy" | x | - | Copies the trace configuration or trace to the clipboard. |
| "Paste" | x | - | Inserts a trace configuration or measurement from the clipboard. |
| "Delete" | x | x | Deletes the selected objects from the project tree or from the device. |
| "Rename" | x | - | Switches the selected object to the editing mode. |
| "Export trace configuration" | x | - | Export a trace configuration as a file with the file extension "* .ttcfgx" or a trace in the device with the file extension "* .ttrecx".  For reasons of compatibility with TIA Portal V12, the "* .ttcfg" and "* .ttrec" file extensions are supported, although they do not contain any information about the device family. |

The trace configuration can also be copied across devices within the same device family.

#### User interface - “Measurements” project tree folder

The ![Figure](images/171754647947_DV_resource.Stream@PNG-de-DE.png) “Measurements" folder shows the saved measurements.

##### Icons in the “Measurements" folder

The following table explains the icons in the ![Icons in the “Measurements" folder](images/171754647947_DV_resource.Stream@PNG-de-DE.png) “Measurements" folder:

| Icon | Description |
| --- | --- |
| ![Icons in the “Measurements" folder](images/171754631179_DV_resource.Stream@PNG-de-DE.png) | Measurement (offline)  Double-click the icon to open the "Time diagram" tab.  The configuration for a measurement can be transferred to the “Traces” folder using drag &amp; drop. |

##### Shortcut menu commands

The following table shows the shortcut menu commands for the ![Shortcut menu commands](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Measurements" system folder:

| Shortcut menu command | Description |
| --- | --- |
| “Add new group” | Inserts a new folder. |
| "Import measurement" | Imports a measurement from a file with the "*.ttrecx" file extension.   The import is device-independent.  For reasons of compatibility, the "*.ttrec" file extension is supported in V12, although it does not contain any information about the device family. |

The following table shows the shortcut menu commands for measurements ![Shortcut menu commands](images/171754631179_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Description |
| --- | --- |
| "Copy" | Copies the trace configuration of the selected objects to the clipboard. |
| "Paste" | Inserts a measurement from the clipboard. |
| "Delete" | Deletes the selected objects from the project tree or from the device. |
| "Rename" | Switches the selected object to the editing mode. |
| “Generate new overlay measurement” | Generates a new overlay measurement with the selected measurements. |
| "Export measurement" | Exports a measurement with the last saved standard view ![Shortcut menu commands](images/171754651915_DV_resource.Stream@PNG-de-DE.png)  The measurement is saved with the extension "*.ttrecx" or "*.csv". For reasons of compatibility, the "*.ttrec" file extension is supported in V12, although it does not contain any information about the device family. |

The measurements can also be copied independent of the device family.

#### User interface - “Installed measurements (memory card)” project tree folder

The ![Figure](images/171754038283_DV_resource.Stream@PNG-de-DE.png) "Measurements on device (memory card)" folder shows all measurements present on the memory card. The folder is only displayed when there is an online connection to the device.

Drag folders or measurements contained here to the "Measurements" system folder using drag &amp; drop. This transfers the measurements to the project.​

> **Note**
>
> **Transferring numerous and large trace measurements from the device (memory card)**
>
> Transferring trace measurements from the device to the project increases the memory requirement.
>
> Avoid copying a large number of measurements with large amounts of data at the same time because this can lead to high memory consumption and extended periods needed for copying.

##### Icons in the "Traces" folder

The following table explains the icons in the system folder ![Icons in the "Traces" folder](images/171754038283_DV_resource.Stream@PNG-de-DE.png):

| Icon |  | Description |
| --- | --- | --- |
| ![Icons in the "Traces" folder](images/171754655883_DV_resource.Stream@PNG-de-DE.png) |  | Folders generated automatically with information on the recording activation time:  The name of the folder cannot be changed. |
|  | ![Icons in the "Traces" folder](images/171754631179_DV_resource.Stream@PNG-de-DE.png) | Installed measurement  Double-click the icon to open the "Time diagram" tab.  The time stamp in the name shows the occurrence of the trigger event.​ |

##### **Shortcut menu commands**

The following table shows the shortcut menu commands for the group folder ![Shortcut menu commands](images/171754655883_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Description |
| --- | --- |
| "Copy" | Copies the selected objects to the clipboard. |
| "Delete" | Deletes the selected objects from the project tree and from the device. |

The following table shows the shortcut menu commands for measurements ![Shortcut menu commands](images/171754631179_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Description |
| --- | --- |
| "Open" | Opens the measurement in the "Time diagram" tab. |
| "Copy" | Copies the selected objects to the clipboard. |
| "Delete" | Deletes the selected objects from the project tree and from the device. |
| "Export measurement" | Exports a measurement as a file with the extension "*.ttrecx" or "*.csv".  For reasons of compatibility, the "*.ttrec" file extension is supported in V12, although it does not contain any information about the device family. |
| "Properties" | Displays the general [properties of the measurement](#interface---inspector-window). |

#### User interface - "Combined measurements" project tree folder

The system folder ![Figure](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Combined measurements" shows the configured combined measurements.

##### Icons in the "Combined measurements" folder

The following table explains the icons in the system folder ![Icons in the "Combined measurements" folder](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Combined measurements":

| Icon | Description |
| --- | --- |
| ![Icons in the "Combined measurements" folder](images/171754672651_DV_resource.Stream@PNG-de-DE.png) | Add new combined measurements  Double-click the icon to add a new combined measurement and open the "Time diagram" tab. |
| ![Icons in the "Combined measurements" folder](images/171754042251_DV_resource.Stream@PNG-de-DE.png) | Combined measurement  Double-click the icon to open the "Time diagram" tab. |

##### **Shortcut menu commands**

The following table shows the shortcut menu commands for the system folder ![Shortcut menu commands](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Combined measurements" or for a group folder contained within this![Shortcut menu commands](images/171754680587_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Description |
| --- | --- |
| "Add new group" | Inserts a new folder. |
| "Add new combined measurement" | Inserts a new combined measurement and opens the "Time diagram" tab. |
| "Import combined measurement" | Imports an combined measurement from a file with the file extension "*.ttcbmx" |

The following table shows the shortcut menu commands for combined measurements![Shortcut menu commands](images/171754042251_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Description |
| --- | --- |
| "Open" | Opens the selected combined measurements in the working area. |
| "Import measurement" | Imports a measurement from a file with the file extension "*.ttrecx"   For reasons of compatibility with V12, the "*.ttrec" file extension is supported, although it does not contain any information about the device family. |
| "Export combined measurement" | Exports an combined measurement  The combined measurement is saved with the extension "*.ttcbmx" or "*.csv". The "*.ttcbmx" format can also be imported again. |
| "Copy" | Copies the selected objects to the clipboard. |
| "Paste" | Pastes measurements, measurements from traces in the device or from an combined measurement from the clipboard.  Multiple objects can be inserted from the clipboard if they are all of the same type. |
| "Delete" | Deletes the selected objects from the project tree or from the device. |
| "Rename" | Switches the selected object to the editing mode. |
| "Properties" | Displays the general properties for the combined measurements. |

The combined measurements can also be copied device-wide.

#### User interface - "Long-term traces" project tree folder (S7-1500)

Long-term trace configurations and installed long-term traces are displayed in the "Long-term traces" ![Figure](images/171754647947_DV_resource.Stream@PNG-de-DE.png) folder.

Double-click a long-term trace to open the corresponding "Configuration" or "Time diagram" tab in the workspace.

##### Icons in the "Long-term traces" folder

The following table explains the icons in the ![Icons in the "Long-term traces" folder](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Long-term traces" folder:

| Icon | Description |
| --- | --- |
| ![Icons in the "Long-term traces" folder](images/171754722955_DV_resource.Stream@PNG-de-DE.png) | Add new long-term trace  Double-click the icon to add a new long-term trace configuration. |
| ![Icons in the "Long-term traces" folder](images/171754726923_DV_resource.Stream@PNG-de-DE.png) | Long-term trace configuration (offline)  Double-click the icon to open the "Configuration" tab. |
| ![Icons in the "Long-term traces" folder](images/171754773259_DV_resource.Stream@PNG-de-DE.png) | Installed long-term trace (online)  The icon is only displayed when there is no offline long-term trace configuration of the same name for the installed trace.  Double-click the icon to open the "Time diagram" tab. |
| ![Icons in the "Long-term traces" folder](images/171754730891_DV_resource.Stream@PNG-de-DE.png) | Long-term trace configuration with installed long-term trace of the same name  If the ![Icons in the "Long-term traces" folder](images/88138852619_DV_resource.Stream@PNG-de-DE.png) button is deactivated, the trace configuration from the project is displayed. The trace corresponds to a trace configuration.  If the ![Icons in the "Long-term traces" folder](images/88136852235_DV_resource.Stream@PNG-de-DE.png) button is activated, the trace configuration from the device is displayed. The trace corresponds to an installed trace.  Double-click on the icon to open the "Time diagram" tab of the installed trace. |
| ![Icons in the "Long-term traces" folder](images/171754647947_DV_resource.Stream@PNG-de-DE.png) | "Measurements" folder  The "Measurements" folder displays long-term trace measurements ![Icons in the "Long-term traces" folder](images/171754777227_DV_resource.Stream@PNG-de-DE.png).  The "Measurements" folder in the "Long-term traces" folder behaves like the "Measurements" folder in the "Traces" folder. [User interface - “Measurements” project tree folder](#user-interface---measurements-project-tree-folder) |
| ![Icons in the "Long-term traces" folder](images/171754676619_DV_resource.Stream@PNG-de-DE.png) | "Combined measurements" folder  The "Combined measurements" folder displays combined long-term trace measurements ![Icons in the "Long-term traces" folder](images/171754042251_DV_resource.Stream@PNG-de-DE.png).  Double-click the ![Icons in the "Long-term traces" folder](images/171754672651_DV_resource.Stream@PNG-de-DE.png) icon to add a new combined long-term trace measurement.  The "Combined measurements" folder in the "Long-term traces" folder behaves like the "Combined measurements" folder in the "Traces" folder. |

##### Status

When there is an online connection, the status is displayed in the right-hand column of the project tree. The status is also displayed as tooltip above the respective icon.

The following table shows the meaning of the icons:

| Icon | Description |
| --- | --- |
| ![Status](images/67336425739_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are identical |
| ![Status](images/67336416907_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are different |
| ![Status](images/67357388171_DV_resource.Stream@PNG-de-DE.png) | Configuration only exists online |

##### **Shortcut menu commands**

The following table shows the shortcut menu commands for the "Long-term traces" ![Shortcut menu commands](images/171754647947_DV_resource.Stream@PNG-de-DE.png) folder:

| Shortcut menu command | Description |
| --- | --- |
| "Add new group" | Adds a new folder. |
| "Add new long-term trace" | Adds a new long-term trace configuration and opens the Configuration tab. |

The following table shows the shortcut menu commands for long-term trace configurations ![Shortcut menu commands](images/171754726923_DV_resource.Stream@PNG-de-DE.png) and installed long-term traces ![Shortcut menu commands](images/171754730891_DV_resource.Stream@PNG-de-DE.png) /![Shortcut menu commands](images/171754773259_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Long-term trace configuration | Installed long-term trace | Description |
| --- | --- | --- | --- |
| "Copy" | x | - | Copies the long-term trace configuration or installed long-term trace to the clipboard. |
| "Paste" | x | - | Inserts a long-term trace configuration or measurement from the clipboard. |
| "Delete" | x | x | Deletes the selected objects from the project tree or from the device. |
| "Rename" | x | - | Switches the selected object to the editing mode. |

The long-term trace configuration can also be copied across devices within the same device family.

### Working area

This section contains information on the following topics:

- [User interface - trace toolbar](#user-interface---trace-toolbar)
- [User interface - Configuration tab](#user-interface---configuration-tab)
- [User interface - Time diagram tab](#user-interface---time-diagram-tab)
- [User interface - FFT diagram tab](#user-interface---fft-diagram-tab)
- [User interface - Bode diagram tab](#user-interface---bode-diagram-tab)
- [User interface - Signal selection tab (Combined measurements)](#user-interface---signal-selection-tab-combined-measurements)

#### User interface - trace toolbar

Tools are available for handling the trace via buttons.

The following table shows the functions of the buttons:

| Icon | Description |
| --- | --- |
| ![Figure](images/171754781195_DV_resource.Stream@PNG-de-DE.png) | Transfer the selected trace configuration to the device  The selected trace configuration is transferred to the device. |
| ![Figure](images/171754836363_DV_resource.Stream@PNG-de-DE.png) | Transfer the selected trace configuration from the device  The selected configuration is applied as new trace configuration to the ![Figure](images/171753628939_DV_resource.Stream@PNG-de-DE.png) "Traces" system folder. The current display options are included in the new trace configuration.  A trace configuration of the same name is overwritten in the system folder. |
| ![Figure](images/171754623243_DV_resource.Stream@PNG-de-DE.png) | Observe on/off  Change of the display between online and offline.  Monitoring is not possible in the Bode diagram.   **Note**   Once monitor and automatic scaling are activated at the same time, no more actions can be undone using the "Undo" button.   **Note**   When an installed trace is first started the display in the curve diagram is set to automatic scaling by default. Make sure when the recording is restarted that any changes to the scaling settings are retained. Reactivate automatic scaling manually if necessary in order to monitor the recording. |
| ![Figure](images/171754840331_DV_resource.Stream@PNG-de-DE.png) | Activate recording  If the recording of an installed trace is repeated, then the settings relevant for the display (curve diagram and signal table) are also retained for the new recording.    **Note**   When a recording is restarted, the previously recorded values are lost.  To save the recorded values, [save the measurement in the project](#saving-measurements-in-the-project) before you activate the recording again. |
| ![Figure](images/171754844299_DV_resource.Stream@PNG-de-DE.png) | Deactivate recording |
| ![Figure](images/171754890635_DV_resource.Stream@PNG-de-DE.png) | Delete installed trace  Deletes the selected trace from the device. |
| ![Figure](images/171754952843_DV_resource.Stream@PNG-de-DE.png) | Automatically repeat recording  After a recording, the recording is automatically activated again. The display of the curve diagram is refreshed when the recording is completed.  This type of refresh is particularly suitable for [monitoring fast signals](#automatic-repetition-of-measurements). |
| ![Figure](images/171754848267_DV_resource.Stream@PNG-de-DE.png) | Transfer the selected measurement from the device to the project  The measurement is added to the ![Figure](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Measurements" system folder.   **Note**   Only the data loaded from the device is saved. This data is displayed in the curve diagram. If necessary, wait until the display is updated. |
| With long-term trace measurements  The measurement is added to the ![Figure](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Long-term trace measurements" system folder.   **Note**   Only the data loaded from the device is saved. The data is only displayed in the time diagram after recording has stopped. |  |
| ![Figure](images/171754894603_DV_resource.Stream@PNG-de-DE.png) | Export trace configuration  Exports a trace configuration as a file with the file extension "*.ttcfgx". For reasons of compatibility with V12, the "*.ttcfg" file extension is supported, although it does not contain any information about the device family. |
| ![Figure](images/171754915339_DV_resource.Stream@PNG-de-DE.png) | Generate a trace configuration  Generates a new trace configuration from the measurement. |
| ![Figure](images/171754898571_DV_resource.Stream@PNG-de-DE.png) | Export measurement with the settings from the current view  Exports a measurement as a file with the file extension "*.ttrecx" or "*.csv". For reasons of compatibility with V12, the "*.ttrec" file extension is supported, although it does not contain any information about the device family. |
| ![Figure](images/171754960779_DV_resource.Stream@PNG-de-DE.png) | Signal filter  Filters the signal table by the signals matching the diagram type. If you are in the Bode diagramtab, for example, only calculated Bode signals are displayed in the signal table when the signal filter is set.   **Note**   The signal filter does not hide a signal when an invalid value is listed in the "Formula" column of the signal table. |
| ![Figure](images/171754919307_DV_resource.Stream@PNG-de-DE.png) | Import measurement (only with combined measurements)  Imports a measurement from a file with the file extension "*.ttrecx".   For reasons of compatibility with V12, the "*.ttrec" file extension is supported, although it does not contain any information about the device family. |
| ![Figure](images/171754956811_DV_resource.Stream@PNG-de-DE.png) | Export combined measurement (only with combined measurements)  The combined measurement is saved with the extension "*.ttcbmx" or "*.csv". The "*.ttcbmx" format can be imported via the shortcut menu in the project tree. |
| ![Figure](images/171754923275_DV_resource.Stream@PNG-de-DE.png) | Select a measurement (only with combined measurements)  The drop down list box contains the imported measurements. Select the desired measurement to display the configuration. |

#### User interface - Configuration tab

This section contains information on the following topics:

- [User interface - Configuration](#user-interface---configuration)

##### User interface - Configuration

The trace configuration depends on the device and is described at the respective [device](#devices).

#### User interface - Time diagram tab

This section contains information on the following topics:

- [User interface - curve diagram](#user-interface---curve-diagram)
- [User interface - signal table](#user-interface---signal-table)
- [Interface - Formula editor](#interface---formula-editor)
- [User interface - Measurements (Combined measurements)](#user-interface---measurements-combined-measurements)

##### User interface - curve diagram

The curve diagram displays the selected signals of a recording. Analog signals are displayed in the upper curve diagram. Binary signals are displayed as bit track in the lower diagram. You can adjust the display of the signals in the [signal table](#user-interface---signal-table) and with the toolbar of the curve diagram.

With project trace, the curve diagram displays a finished or canceled recording. Under the device you can monitor any recording.

###### Setting options and displays in the curve diagram

The following figure shows an example of the display:

![Setting options and displays in the curve diagram](images/171758912011_DV_resource.Stream@PNG-en-US.png)

The scale in the diagram applies to the selected (highlighted in gray) signal in the legend. The legend can be moved and its size can be adjusted with the mouse.

The ![Setting options and displays in the curve diagram](images/171755163531_DV_resource.Stream@PNG-de-DE.png) icon shows the device trigger time with a vertical line.

A drop-down list for selecting the unit is available below the curve for the "Time (relative)" setting for the time axis. The "Automatic" setting automatically adjusts the unit based on the displayed time range.

> **Note**
>
> **Non-interpretable data types**
>
> Some data types require a defined format, e.g. the S7 data type `LTime_of_Day`. If this format is not available, the data type is interpreted as INT.

###### Functions using the mouse wheel

The following table shows which functions are possible in the curve diagram using the mouse wheel:

| Function of the mouse wheel | Description |
| --- | --- |
| Move the curve diagram vertically | Turning the mouse wheel moves the display in the upper curve diagram up or down.   If the signals are arranged in traces, the display of the group is shifted below the cursor.  The mouse pointer must be positioned above the curve diagram with the analog signals. |
| Move the curve diagram horizontally | Turning the mouse wheel with the &lt;Shift&gt; button pressed down moves the display in the curve diagram to the left or the right.   The cursor must be positioned above the curve diagram. |
| Zoom in and zoom out | Turning the mouse wheel with the &lt;Ctrl&gt; button pressed down zooms in or out of the display in the curve diagram. The cursor position is the starting point for zooming in or out.  The value axis of the lower curve diagram (bit tracks) is not affected.  The cursor must be positioned above the curve diagram. |

###### Functions using the keyboard

The following table shows which keyboard commands are possible with a focus on the curve diagram:

| Shortcut key | Description |
| --- | --- |
| Selecting a measurement cursor |  |
| &lt;Ctrl+Shift+1&gt; | The vertical measurement cursor t1 is selected or deselected. |
| &lt;Ctrl+Shift+2&gt; | The vertical measurement cursor t2 is selected or deselected. |
| &lt;Ctrl+Shift+3&gt; | The horizontal measurement cursor Y1 is selected or deselected. |
| &lt;Ctrl+Shift+4&gt; | The horizontal measurement cursor Y2 is selected or deselected. |
| &lt;Tab&gt; | The next measurement cursor is selected. |
| Positioning a vertical measurement cursor |  |
| &lt;Left&gt;, &lt;Right&gt; | With the unit "Samples", the selected measurement cursor is moved by one sample by the signal in the foreground. With the unit "Time (relative)", the measurement cursor is moved by one pixel. |
| &lt;Shift+Left&gt;, &lt;Shift+Right&gt; | With the unit "Samples", the selected measurement cursor is moved by 10 samples by the signal in the foreground. With the unit "Time (relative)", the measurement cursor is moved by 10 pixels. |
| Positioning a horizontal measurement cursor |  |
| &lt;Up&gt;, &lt;Down&gt; | The selected measurement cursor is moved by one pixel along the value axis. |
| &lt;Shift+Up&gt;, &lt;Shift+Down&gt; | The selected measurement cursor is moved by 10 pixels along the value axis. |
| Display of vertical measurement cursors |  |
| &lt;Ctrl+Space&gt; | The vertical measurement cursors are shown or hidden. |
| &lt;Ctrl+Shift+Space&gt; | The vertical measurement cursors are shown and centered for the current view. |
| Changing the view |  |
| &lt;Space&gt; | Move view |
| &lt;Ctrl+0&gt; | Set 100% view in open editor |
| &lt;Ctrl++&gt; | Apply zoom in with 10% |
| &lt;Ctrl+-&gt; | Apply zoom out with 10% |

###### Toolbar of the curve diagram

Tools are available for adapting the display via buttons.

The following table shows the functions of the buttons:

| Icon | Function | Description |
| --- | --- | --- |
| ![Toolbar of the curve diagram](images/171754977547_DV_resource.Stream@PNG-de-DE.png) | Undo | Undoes the display adjustments last made.  If several display adjustments have been made, they can be undone step-by-step.  Applicable to the following display adjustments:  - Show all - Display entire time range - Automatic scaling of the value axis - Move view - Zoom selection - Vertical zoom selection - Horizontal zoom selection - Zoom in - Zoom out |
| ![Toolbar of the curve diagram](images/171754981131_DV_resource.Stream@PNG-de-DE.png) | Redo | Redoes the last undone display adjustment.   If several display adjustments have been undone, they can be redone step-by-step. |
| ![Toolbar of the curve diagram](images/171754651915_DV_resource.Stream@PNG-de-DE.png) | Standard view | Uses the current view as standard for this recording. If the trace recording is shown again later, the standard view is restored. |
| ![Toolbar of the curve diagram](images/171755009803_DV_resource.Stream@PNG-de-DE.png) | Move view | Moves the display with the mouse button pressed. |
| ![Toolbar of the curve diagram](images/171754984715_DV_resource.Stream@PNG-de-DE.png) | Zoom selection | Selection of an arbitrary range with the mouse button pressed. The display is scaled to the range selection. |
| ![Toolbar of the curve diagram](images/171754988299_DV_resource.Stream@PNG-de-DE.png) | Vertical zoom selection | Selection of a vertical range with the mouse button pressed. The display is scaled to the range selection. |
| ![Toolbar of the curve diagram](images/171754991883_DV_resource.Stream@PNG-de-DE.png) | Horizontal zoom selection | Selection of a horizontal range with the mouse button pressed. The display is scaled to the range selection. |
| ![Toolbar of the curve diagram](images/171755105675_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlargement of the display. The ranges of the time axis and value axis are reduced every time the button is clicked. The curves are displayed larger. |
| ![Toolbar of the curve diagram](images/171755109643_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduction of the display. The ranges of the time axis and value axis are increased every time the button is clicked. The curves are displayed smaller. |
| ![Toolbar of the curve diagram](images/171755013387_DV_resource.Stream@PNG-de-DE.png) | Display all | Scales the display of the available data so that the entire time range and all values are displayed. |
| ![Toolbar of the curve diagram](images/171755117195_DV_resource.Stream@PNG-de-DE.png) | Automatic scaling of the value axis | Scaling of the display so that all values are displayed for the currently displayed time range.  The relative scaling ratio between the signals may change.    **Note**   The automatic scaling of the value axis is stopped when the zoom function is activated for the value axis. This button reactivates the automatic adjustments to the minimum/maximum values. |
| ![Toolbar of the curve diagram](images/171755159563_DV_resource.Stream@PNG-de-DE.png) | Show the overall time range | Scaling of the display so that the values in the value range currently displayed are displayed for the overall time range.  The value range displayed only then changes if "Display all values" ![Toolbar of the curve diagram](images/171755117195_DV_resource.Stream@PNG-de-DE.png) is activated.   **Note**   The automatic scaling of the time axis is stopped when a zoom function is activated for the time axis. This button reactivates the automatic adjustments for the time range. |
| ![Toolbar of the curve diagram](images/171754995467_DV_resource.Stream@PNG-de-DE.png) | Arrange in tracks | Activate or deactivate the trace arrangement.  When the trace arrangement is activated the signals are arranged among themselves with the relevant value axes.  Scaling groups are displayed in the same trace.  This setting does not affect the display for the bit traces. |
| ![Toolbar of the curve diagram](images/171755167499_DV_resource.Stream@PNG-de-DE.png) | Unit changeover of the time axis | Switching the unit of the time axis  The following units are adjustable:  - "Samples" - "Time (relative)"    Relative time related to the trigger time - "Time stamp of the samples" |
| ![Toolbar of the curve diagram](images/171755113611_DV_resource.Stream@PNG-de-DE.png) | Display samples | The samples are displayed as small circles on the curves. |
| ![Toolbar of the curve diagram](images/171755222667_DV_resource.Stream@PNG-de-DE.png) | Interpolated representation | Linear interpolation between two consecutive samples for floating point numbers  If linear interpolation is not enabled (default), the connection between the measuring points is drawn in steps. |
| ![Toolbar of the curve diagram](images/171754999051_DV_resource.Stream@PNG-de-DE.png) | Display vertical measurement cursors | Display of the vertical measurement cursors. The vertical position of the two measurement cursors can be moved with the mouse. The associated measured values and the difference of the measurement cursors corresponding to the position are shown in the signal table. Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display more information.  Also use the cursor keys. The following actions are possible for vertical measurement cursors with the cursor keys:  - Select - Positioning - Show or hide measurement cursor - Center measurement cursors |
| ![Toolbar of the curve diagram](images/171755002635_DV_resource.Stream@PNG-de-DE.png) | Display horizontal measurement cursors | Display of the horizontal measurement cursors.  The horizontal position of the two measurement cursors can be moved with the mouse.  Display the ["Measurement cursor" pane](#user-interface---signal-table) in the Trace task card in order to display the values or to reposition the measurement cursor through entering the position.  Also use the cursor keys. The following actions are possible for horizontal measurement cursors with the cursor keys:  - Select - Positioning |
| ![Toolbar of the curve diagram](images/171755226635_DV_resource.Stream@PNG-de-DE.png) | Show/hide time range display | Show or hide the time range display below the curve diagram  The time range display shows the area in the curve diagram in yellow based on a selected signal.  The yellow area can be moved with the mouse and the borders can be changed horizontally.    ![Toolbar of the curve diagram](images/171755230603_DV_resource.Stream@PNG-de-DE.png) |
| ![Toolbar of the curve diagram](images/171755055371_DV_resource.Stream@PNG-de-DE.png) | Show/hide chart legend | Showing or hiding of the legend in the curve diagram and the bit track labels. |
| ![Toolbar of the curve diagram](images/171755059339_DV_resource.Stream@PNG-de-DE.png) | Align the chart legend to the left | Display of the legend and the bit track labels on the left side of the curve diagram. |
| ![Toolbar of the curve diagram](images/171755063307_DV_resource.Stream@PNG-de-DE.png) | Align the chart legend to the right | Display of the legend and the bit track labels on the right side of the curve diagram. |
| ![Toolbar of the curve diagram](images/171755006219_DV_resource.Stream@PNG-de-DE.png) | Change background color | Changeover between various background colors. |

###### Shortcut menu commands

The following table shows the shortcut menu commands in the curve diagram:

| Shortcut menu command | Description |  |
| --- | --- | --- |
| "Undo" | Undoes the display adjustments last made.  If several display adjustments have been made, they can be undone step-by-step.  Applicable to the following display adjustments:  - Show all - Display entire time range - Automatic scaling of the value axis - Move view - Zoom selection - Vertical zoom selection - Horizontal zoom selection - Zoom in - Zoom out |  |
| "Redo" | Redoes the last undone display adjustment.   If several display adjustments have been undone, they can be redone step-by-step. |  |
| ''Zoom in'' | Zoom in to the display. The ranges of the time axis and value axis are reduced every time the button is clicked. The curves are displayed larger. |  |
| ''Zoom out'' | Zoom out of the display. The ranges of the time axis and value axis are increased every time the button is clicked. The curves are displayed smaller. |  |
| "Display all" | Scales the display of the available data so that the entire time range and all values are displayed. |  |
| "Automatic scaling of the value axis" | Scaling of the display so that all values are displayed for the currently displayed time range.  The relative scaling ratio between the signals may change.    **Note**   The automatic scaling of the value axis is stopped when the zoom function is activated for the value axis. This button reactivates the automatic adjustments to the minimum/maximum values. |  |
| "Display entire time range" | Scaling of the display so that the values in the value range currently shown are displayed for the overall time range.  The value range displayed only then changes if "Display all values" is activated.   **Note**   The automatic scaling of the time axis is stopped when a zoom function is activated for the time axis. This button reactivates the automatic adjustments for the time range. |  |
| "Arrange in tracks" | Activate or deactivate the trace arrangement.  When the trace arrangement is activated the signals are arranged among themselves with the relevant value axes.  Signal groups are displayed in the same trace.  This setting does not affect the display for the bit traces. |  |
| "Measurement cursor" | You can find the following options in this submenu: |  |
| "Show vertical measurement cursors" | Display of vertical measurement cursor.  The vertical position of the two measurement cursors can be moved with the mouse. The associated measured values and the difference of the measurement cursors corresponding to the position are shown in the signal table. Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display further information.  Also use the cursor keys. The following actions are possible for vertical measurement cursors with the cursor keys:  - Select - Positioning - Show or hide measurement cursor - Center measurement cursors |  |
| "Show horizontal measurement cursors" | Display of the horizontal measurement cursors.  The horizontal position of the two measurement cursors can be moved with the mouse.  Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display the values or to reposition the measurement cursor through entering the position.  Also use the cursor keys. The following actions are possible for horizontal measurement cursors with the cursor keys:  - Select - Positioning |  |
| "Center measurement cursors" | Positions the activated measurement cursors at a central point in the current display. |  |
| "Save diagram as image" | Exports the current display in graphic format, e.g. as a bitmap. |  |
| "Copy image to clipboard" | Copies the current display to the clipboard. |  |
| "Add to measurements"  (only axis control panel and PID) | Adds the displayed recording to the "Measurements" system folder. |  |
| "Automatic bit track height" | Automatically adjusts the height of the bit tracks and thereby determines the size of the lower curve diagram.  The setting is automatically deactivated once you change the space allocation between the curve diagrams manually.   **Note**   You can change the vertical space allocation between the upper and lower curve diagram. To do this drag the time axis of the upper curve diagram up or down with the mouse. |  |

##### User interface - signal table

The signal table lists the signals of the selected measurement and provides setting options for some properties.

Trace settings can be changed on the device in online mode. The changes of the display options can be applied to the project using the ![Figure](images/171754836363_DV_resource.Stream@PNG-de-DE.png) button. Otherwise the changes are discarded during the switch to offline mode.

If the installed trace is added to the measurements, the current settings of the signal table are saved in the measurement.

The signals can be sorted using drag-and-drop. The bits of a signal can be resorted within a signal.

###### Setting options and displays in the signal table

The following figure shows an example of the display:

![Setting options and displays in the signal table](images/171758916235_DV_resource.Stream@PNG-en-US.png)

The following table shows the settings and displays of the recorded signals:

| Column |  | Description |
| --- | --- | --- |
| "Status"  (Only project trace in online mode) |  | Status display |
|  | ![Setting options and displays in the signal table](images/171755451787_DV_resource.Stream@PNG-de-DE.png) | No online connection |
| ![Setting options and displays in the signal table](images/171755455755_DV_resource.Stream@PNG-de-DE.png) | Configuration only exists offline |  |
| ![Setting options and displays in the signal table](images/171754598539_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are different |  |
| ![Setting options and displays in the signal table](images/171755459723_DV_resource.Stream@PNG-de-DE.png) | No access right |  |
| ![Setting options and displays in the signal table](images/67336425739_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are identical |  |
| Signal or error symbol |  |  |
|  | ![Setting options and displays in the signal table](images/171755289355_DV_resource.Stream@PNG-de-DE.png) | Signal |
| ![Setting options and displays in the signal table](images/171755401483_DV_resource.Stream@PNG-de-DE.png) | Failsafe signal |  |
| ![Setting options and displays in the signal table](images/171755405451_DV_resource.Stream@PNG-de-DE.png) | Signal from a data block |  |
| ![Setting options and displays in the signal table](images/171755409419_DV_resource.Stream@PNG-de-DE.png) | Signal from a failsafe data block |  |
| ![Setting options and displays in the signal table](images/171755376779_DV_resource.Stream@PNG-de-DE.png) | Calculated signal (formula) |  |
| ![Setting options and displays in the signal table](images/171755384715_DV_resource.Stream@PNG-de-DE.png) | Error in the formula of the calculated signal |  |
| ![Setting options and displays in the signal table](images/171755285771_DV_resource.Stream@PNG-de-DE.png)     ![Setting options and displays in the signal table](images/171755326475_DV_resource.Stream@PNG-de-DE.png) |  | Selection for display in the curve diagram - a maximum of 16 signals can be selected.  The point indicates that at least one bit has been selected for display as bit track for the signal in the bit selection. |
| "Signal reference" (only trace) |  | Automatically generated number of the signal  The signal are accessed via the signal reference in the formulas. |
| "Device" (project trace only) |  | Display of the device name |
| "Name" |  | Display of the signal name  A click on the name of a displayed signal updates the scale in the curve diagram.  You can enter a name for a calculated signal in the last line without a signal symbol. The calculated signal is entered with its name. |
| "Measurement" (Only combined measurements) |  | Display of the measurement  Shows the name of the measurement to which the signal belongs. |
|  | ![Setting options and displays in the signal table](images/171755292939_DV_resource.Stream@PNG-de-DE.png) | Open bit selection  Individual bits can also be selected for the following data types for display as a bit track in the lower curve diagram:  - Byte, Word, DWord, LWord - SInt, USInt, Int, UInt, DInt, UDInt, LInt, ULInt   Example of an opened bit selection for the DWORD data type:    ![Setting options and displays in the signal table](images/171755296907_DV_resource.Stream@PNG-de-DE.png)   Select or deselect the relevant bit for display by clicking the ![Setting options and displays in the signal table](images/171755285771_DV_resource.Stream@PNG-de-DE.png) icon. |
|  | ![Setting options and displays in the signal table](images/171755292939_DV_resource.Stream@PNG-de-DE.png) Bode | Automatically generated Bode signals  Bode signals are automatically generated for amplitude and phase after entering a Bode formula for a signal. Click on the arrow to display the Bode signals. |
| "Data type" |  | Display of the data type |
| "Display format" |  | Display format of the signal  The display formats supported for the signal are offered for selection.  A display format suitable for the data type is set with "Default". |
| "Address" |  | Display of the address of the signal  The field remains empty with optimized / type correct tags. |
| "Formula" (only trace) |  | Display or entry of a formula  A formula can contain mathematical functions with numbers and signals. Use the formula editor to conveniently create formulas. |
|  | ![Setting options and displays in the signal table](images/171755380747_DV_resource.Stream@PNG-de-DE.png) | Call of the formula editor for calculated signals  Click on the icon to open the formula editor. |
| "Color" |  | Display and setting option for the color of the signal |
| "Scaling group" |  | Display or input of the scaling group name for one scaling group  The Y-scales are scaled identically for all signals of one scaling group.  Enter an identical scaling group name for those signals that are to be scaled identically.  Remove signals from the scaling group by deleting the scaling group name.  The scaling groups are saved via the function "Use current view as standard" (button ![Setting options and displays in the signal table](images/171754651915_DV_resource.Stream@PNG-de-DE.png)).   **Notes**   You cannot group binary signal events.  In hex display format, group only the signals with a format compatible to the sign for the display.  This setting is not available for the Bode diagram. |
|  | Gray field for chain icon | Move the cursor over the gray field or the chain icon (![Setting options and displays in the signal table](images/171755330443_DV_resource.Stream@PNG-de-DE.png) or ![Setting options and displays in the signal table](images/171755334411_DV_resource.Stream@PNG-de-DE.png)) to add the signal to a scaling group or delete the signal from the scaling group.  Clicking the ![Setting options and displays in the signal table](images/171755330443_DV_resource.Stream@PNG-de-DE.png) chain icon adds the signal to a scaling group or creates a new scaling group.  Clicking the ![Setting options and displays in the signal table](images/171755334411_DV_resource.Stream@PNG-de-DE.png) chain icon removes the signal from the scaling group.  For a selected signal with scaling group, the ![Setting options and displays in the signal table](images/171755334411_DV_resource.Stream@PNG-de-DE.png) chain icon displays all signals of the same scaling group. |
| Input field | The input field displays the scaling group name.  As an alternative to the chain icon, you can assign or delete a group name via text input in this field. |  |
| "Min. Y-scale" |  | Display or input of the minimum value for the scaling of the signal |
| "Max. Y-scale" |  | Display or input of the maximum value for the scaling of the signal |
| "Y(t1)" |  | Display of the value at the position of the first measurement cursor |
| "Y(t2)" |  | Display of the value at the position of the second measurement cursor |
| "ΔY" |  | Display of the value difference between the first and the second measurement cursor |
| ![Setting options and displays in the signal table](images/171755117195_DV_resource.Stream@PNG-de-DE.png) |  | Selection of the automatic scaling of the value axis for the signal  When the check box is selected, the minimum and maximum values for scaling the signal are adjusted so that all values are displayed for the currently displayed time range.  The ![Setting options and displays in the signal table](images/171755117195_DV_resource.Stream@PNG-de-DE.png) button on the toolbar of the curve diagram activates automatic scaling for all scalable signals. |
| "Unit" |  | Display of the unit   For example, for unit-based values from technology objects |
| "Comment" |  | Display and input option for a comment about the signal |

###### Shortcut menu commands

The following table shows the shortcut menu commands of the signal table:

| Shortcut menu command | Description |
| --- | --- |
| "Insert calculated signal" | Inserts a re-calculated signal at the top in the table |
| "Edit formula" | Opens the formula editor for the calculated signal |
| "Cut" | Cannot be selected |
| "Copy" | Copies the contents of the selected lines to the clipboard. |
| "Paste" | Cannot be selected |
| "Delete" | Cannot be selected |
| "Rename" | Cannot be selected |
| "Display format" | Allows you to switch the display format  The display formats supported for the signal are offered for selection. |
| "Display signal(s)" | Displays the selected signals in the curve diagram. |
| "Hide signal(s)" | Hides the selected signals in the curve diagram. |

---

**See also**

[Use of the signal table](#use-of-the-signal-table)
  
[Using the signal group in the signal table](#using-the-signal-group-in-the-signal-table)

##### Interface - Formula editor

The formula editor provides various mathematical functions for analyzing signals. Open the editor in the signal table by clicking ![Figure](images/171755380747_DV_resource.Stream@PNG-de-DE.png).

###### Configuration options and displays in the formula editor

The following figure shows an example of the display:

![Formula editor](images/171758933259_DV_resource.Stream@PNG-en-US.png)

Formula editor

The following table shows the configuration options and displays of the formula editor:

| Field/Button |  | Description |
| --- | --- | --- |
| "Name" |  | Display and input of the name for the created formula  The name must be unique and only contain characters that are allowed in Windows file names. |
| "Data type" |  | Display of formula data type  The data type is pre-assigned with a floating-point number of LREAL type and cannot be changed. |
| "Unit" |  | Display and input of a unit  Freely specified user-defined unit. |
| Drop-down list with signals |  | Selection of the signals  The drop-down list contains the signals from the signal table and inserts a selected signal into the formula. |
| "Formula entry" |  | Text field to display and enter the formula  Create a formula by typing into this text box or by using the buttons for the mathematical functions.  Signals can be referenced in the text box using the signal reference with a prefixed $ character or the name in double quotes in the formula. Mixed input is possible.  Restrictions:  - Bits from a bit selection (e.g. below the INT data type) are not allowed in the formula. - Do not use any signal references to a tag in the formula that start with "$", for example, `$0("$0")`. |
| Mathematical functions |  |  |
|  | + | Addition |
| - | Subtraction |  |
| * | Multiplication |  |
| / | Division |  |
| () | Brackets  Grouping expressions |  |
| SQR | Square |  |
| SQRT | Square root |  |
| ABS | Absolute value  Calculates the size of a number.   **Examples**    `ABS(5)` → 5   `ABS(-3)` → 3   `ABS(-3.14)` → 3.14 |  |
| MOD | Modulo  Calculates the residual value of a division   **Examples**    `MOD(5,3)` → 2   `MOD(3.14,3)` → 0.14 |  |
| REC | Reciprocal value (1/x) |  |
| DIFF<sup> 1)</sup> | Numerical differentiation   **Examples**   Formula: `DIFF($0,SAMPLETIME)` |  |
| INT <sup>1)</sup> | Numerical integration   **Examples**   Formula: `INT($0,SAMPLETIME)` |  |
| RMS<sup> 1)</sup> | Quadratic mean  The squares of all measured values are totaled and then divided by the number of measured values. The quadratic mean is the square root of this value.   **Examples**   Formula: `RMS($0,SAMPLETIME)` |  |
| AV | Mean value filter from 1st to 5th order  If the specification of an order is missing, the mean filter of the 1st order is used.   **Examples**    `AV($0,1)` → Mean filter 1st order   `AV($0,5)` → Mean filter 5th order |  |
| π | Mathematical constant Pi |  |
| AM | Arithmetic mean  The arithmetic mean is a moving average over five samples. |  |
| DIF | Simple subtraction with mean filter from 1st to 5th order  If the specification of an order is missing, simple subtraction is performed with a 1st order filter.   **Examples**    `DIF($0,1)` → Single subtraction with 1st order filter   `DIF($0,5)` → Single subtraction with 5th order filter   `DIF($0)` → Single subtraction with 1st order filter   **Example: Calculate an acceleration curve from a velocity signal**     `$0`: Velocity signal in meters per second Cycle time of the constant cycle velocity recording: 1 ms  Formula: `DIF($0,1)/0.001`  Unit: `m/s`<sup>2</sup> |  |
| DIF2 | Double subtraction with mean filter from 1st to 5th order  If the specification of an order is missing, then double subtraction is executed with a 1st order filter.   **Examples**    `DIF2($0,1)` → Double subtraction with 1st order filter   `DIF2($0,5)` → Double subtraction with 5th order filter   `DIF2($0)` → Double subtraction with 1st order filter   **Example: Calculate an acceleration curve from a position sequence**     `$0`: Position sequence in meters Cycle time of the constant cycle position recording: 1 ms  Formula: `DIF2($0,1)/SQR(0.001)` Unit: `m/s`<sup>2</sup> |  |
| FFT | Fast Fourier transform  A calculated signal as input parameter or calculations for the parameters are not permitted.   Additional calculations with the FFT function are not permitted.   **Mandatory parameters**   An analog signal must be specified for the input parameter.   Permitted data types:  SINT, INT, DINT, LINT, USINT, UINT, UDINT, ULINT, REAL, LREAL, BYTE, WORD, DWORD, LWORD   **Optional parameters**   The following parameters can be optionally specified:  - RemoveDirectCurrent   Remove direct current component   Data type Bool   If the parameter is not set, "true" is assumed as the default (Remove direct current component). - RangeStart   Index of the first sample to be displayed.   The index of the samples is displayed on the X axis in the FFT diagram.    If the parameter is not set, the first sample of the measurement is assumed as the default. - RangeEnd (RangeStart required)   Index of the last sample to be displayed.   The index of the samples is displayed on the X axis in the FFT diagram.    If the parameter is not set, the last sample of the measurement is assumed as the default.    **Valid examples**   $0=Input signal   `FFT($0,true)`    `FFT($0,0,1000)`    `FFT($0,false,0,1000)`    **Invalid examples**    `FFT($0,20)`    `FFT($0,0)`    `FFT($0,1000,0)`    `FFT($0)+10`    `FFT($0)+SQRT($5)` |  |
| BODE | Bode diagramwith amplitude and phase  Calculated signals as parameter or calculations for the parameters are not permitted.   Additional calculations with the Bode function are not permitted.   **Mandatory parameters**   Analog signals must be specified for the parameters of the input and output signal.   Permitted data types for the parameters:  SINT, INT, DINT, LINT, USINT, UINT, UDINT, ULINT, REAL, LREAL, BYTE, WORD, DWORD, LWORD   **Optional parameters**   The following parameters can be optionally specified:  - RangeStart   Index of the first sample to be displayed.   The index of the samples is displayed on the X axis in the Bode diagram.   If the parameter is not set, the first sample of the measurement is assumed as the default. - RangeEnd (RangeStart required)   Index of the last sample to be displayed.   The index of the samples is displayed on the X axis in the Bode diagram.   If the parameter is not set, the last sample of the measurement is assumed as the default.    **Valid examples**   $0=input signal, $1=output signal   `BODE($0,$1)`    `BODE($0,$1,0,1000)`    **Invalid examples**    `BODE($0,20)`    `BODE($0,$1,0)`    `BODE($0,$1,1000)`    `BODE($0+1,0)`    `BODE($0,$1)+10`    `BODE($0,$1)+SQRT($5)` |  |
| "Show signal name" |  | Display of the signal names   If the check box is selected, the signal names in the formula are displayed instead of the signal references. |
| "Validate" |  | Check the validity of the formula |
| "Result of validation" |  | Result of validation  Displays the result of the validation and indicates errors and error locations. |
| "OK" |  | Transfer the entries in the formula editor |
| "Cancel" |  | Discard the entries in the formula editor |
| <sup>1) </sup>The constant `SAMPLETIME` is only available for equidistant recording cycles. Time unit for `SAMPLETIME` is always μs. |  |  |

> **Note**
>
> The functions DIF, DIF2, DIFF, AM, RMS, AV and INT can only process one recorded signal as argument. Not all invalid formulas are marked as errors.

##### User interface - Measurements (Combined measurements)

The Measurements tab displays the individual measurements and among other things provides the setting options for synchronization.

###### Setting options and displays in the Measurements tab

The following figure shows an example of the display:

![Setting options and displays in the Measurements tab](images/171758937867_DV_resource.Stream@PNG-en-US.png)

The following table shows the settings and displays for the measurements:

| Column |  | Description |
| --- | --- | --- |
| Alignment of the measurements (not available for the Bode diagram) |  |  |
|  | "Trigger/measurement point" | Alignment of the measurements in accordance with the trigger or measurement point  The individual zero point for the measurement is predefined in the table under the "Alignment" column. |
| "Time stamp (absolute time)" | Alignment of the measurements in accordance with their time stamp  The signals are aligned in accordance with the time from the absolute time stamp. |  |
| Table columns |  |  |
|  | ![Setting options and displays in the Measurements tab](images/171754631179_DV_resource.Stream@PNG-de-DE.png) | Static display of the measurement icon |
| "Name" | Display and change options for the measurement name  The name must be a unique one and can be changed. |  |
| "Alignment" | Alignment of the measurement (only adjustable with the "Trigger/measurement point" check box activated)  Determines the individual zero point for a measurement. All signals for the measurement are displayed in relation to this zero point.  The following settings are possible:  - Trigger - First sample after the trigger event - First sample - Last measurement point   This setting is not available for the Bode diagram. |  |
| "Offset" | Offset related to the time axis  Moves the measurement left or right by the offset stated on the time axis.  The offset can also be transferred via the clipboard to the cell from the ΔX value of the measurement cursor. See [Aligning measurements with measurement cursor](#aligning-measurements-with-measurement-cursor).  This setting is not available for the Bode diagram. |  |
| "Time stamp" | Display of the trigger time |  |
| "Comment" | Display and input option for a comment about the signal |  |

###### Shortcut menu commands

The following table shows the shortcut menu commands of the signal table:

| Shortcut menu command | Description |
| --- | --- |
| "Cut" | Cannot be selected |
| "Copy" | Copies the contents of the selected lines to the clipboard. |
| "Paste" | Cannot be selected |
| "Delete" | Cannot be selected |
| "Rename" | Switches the selected cell to the editing mode. |
| "Import measurement" | Imports a measurement from a file, e.g. with the "*.ttrecx" file extension.   The import is device-independent and also suitable, for example, for comparing measurements of a PLC with the measurements of a drive device.  For reasons of compatibility, the "*.ttrec" file extension is supported in V12, although it does not contain any information about the device family. |
| "Export measurement" | Exports a measurement as a file with the extension "*.ttrecx" or "*.csv".   For reasons of compatibility, the "*.ttrec" file extension is supported in V12, although it does not contain any information about the device family. |

#### User interface - FFT diagram tab

This section contains information on the following topics:

- [User interface - curve diagram](#user-interface---curve-diagram-1)
- [User interface - signal table](#user-interface---signal-table-1)
- [Interface - Formula editor](#interface---formula-editor-1)

##### User interface - curve diagram

The FFT diagram shows the frequency spectra of measured signals calculated with the FFT formula.

The Y axis shows the amplitude. The display of values on the Y axis is linear.

The X axis represents the frequency in Hertz. You can set the display of values on the X axis as linear or logarithmic.

###### Setting options and displays in the curve diagram

The following figure shows an example of the display:

![Setting options and displays in the curve diagram](images/171758942475_DV_resource.Stream@PNG-en-US.png)

Below the curve diagram, you can change the partitioning of the X axis with the options "Linear" and "Logarithmic".

###### Functions using the mouse wheel

The following table shows which functions are possible in the curve diagram using the mouse wheel:

| Function of the mouse wheel | Description |
| --- | --- |
| Move the curve diagram vertically | Turning the mouse wheel moves the display in the upper curve diagram up or down.   If the signals are arranged in traces, the display of the group is shifted below the cursor.  The mouse pointer must be positioned above the curve diagram with the analog signals. |
| Move the curve diagram horizontally | Turning the mouse wheel with the &lt;Shift&gt; button pressed down moves the display in the curve diagram to the left or the right.   The cursor must be positioned above the curve diagram. |
| Zoom in and zoom out | Turning the mouse wheel with the &lt;Ctrl&gt; button pressed down zooms in or out of the display in the curve diagram. The cursor position is the starting point for zooming in or out.  The value axis of the lower curve diagram (bit tracks) is not affected.  The cursor must be positioned above the curve diagram. |

###### Functions using the keyboard

The following table shows which keyboard commands are possible with a focus on the curve diagram:

| Shortcut key | Description |
| --- | --- |
| Selecting a measurement cursor |  |
| &lt;Ctrl+Shift+1&gt; | The vertical measurement cursor t1 is selected or deselected. |
| &lt;Ctrl+Shift+2&gt; | The vertical measurement cursor t2 is selected or deselected. |
| &lt;Ctrl+Shift+3&gt; | The horizontal measurement cursor Y1 is selected or deselected. |
| &lt;Ctrl+Shift+4&gt; | The horizontal measurement cursor Y2 is selected or deselected. |
| &lt;Tab&gt; | The next measurement cursor is selected. |
| Positioning a vertical measurement cursor |  |
| &lt;Left&gt;, &lt;Right&gt; | With the unit "Samples", the selected measurement cursor is moved by one sample by the signal in the foreground. |
| &lt;Shift+Left&gt;, &lt;Shift+Right&gt; | With the unit "Samples", the selected measurement cursor is moved by 10 samples by the signal in the foreground. |
| Positioning a horizontal measurement cursor |  |
| &lt;Up&gt;, &lt;Down&gt; | The selected measurement cursor is moved by one pixel along the Y axis. |
| &lt;Shift+Up&gt;, &lt;Shift+Down&gt; | The selected measurement cursor is moved by 10 pixels along the value axis. |
| Display of vertical measurement cursors |  |
| &lt;Ctrl+Space&gt; | The vertical measurement cursors are shown or hidden. |
| &lt;Ctrl+Shift+Space&gt; | The vertical measurement cursors are shown and centered for the current view. |
| Changing the view |  |
| &lt;Space&gt; | Move view |
| &lt;Ctrl+0&gt; | Set 100% view in open editor |
| &lt;Ctrl++&gt; | Apply zoom in with 10% |
| &lt;Ctrl+-&gt; | Apply zoom out with 10% |

###### Toolbar of the curve diagram

Tools are available for adapting the display via buttons.

The following table shows the functions of the buttons:

| Icon | Function | Description |  |
| --- | --- | --- | --- |
| ![Toolbar of the curve diagram](images/171754977547_DV_resource.Stream@PNG-de-DE.png) | Undo | Undoes the display adjustments last made.  If several display adjustments have been made, they can be undone step-by-step.  Applicable to the following display adjustments:  - Show all - Display entire time range - Automatic scaling of the value axis - Move view - Zoom selection - Vertical zoom selection - Horizontal zoom selection - Zoom in - Zoom out |  |
| ![Toolbar of the curve diagram](images/171754981131_DV_resource.Stream@PNG-de-DE.png) | Redo | Redoes the last undone display adjustment.   If several display adjustments have been undone, they can be redone step-by-step. |  |
| ![Toolbar of the curve diagram](images/171754651915_DV_resource.Stream@PNG-de-DE.png) | Standard view | Not used |  |
| ![Toolbar of the curve diagram](images/171755009803_DV_resource.Stream@PNG-de-DE.png) | Move view | Moves the display with the mouse button pressed. |  |
| ![Toolbar of the curve diagram](images/171754984715_DV_resource.Stream@PNG-de-DE.png) | Zoom selection | Selection of an arbitrary range with the mouse button pressed. The display is scaled to the range selection. |  |
| ![Toolbar of the curve diagram](images/171754988299_DV_resource.Stream@PNG-de-DE.png) | Vertical zoom selection | Selection of a vertical range with the mouse button pressed. The display is scaled to the range selection.  Depending on the mouse position, the selection influences either the amplitude response or the phase response. |  |
| ![Toolbar of the curve diagram](images/171754991883_DV_resource.Stream@PNG-de-DE.png) | Horizontal zoom selection | Selection of a horizontal range with the mouse button pressed. The display is scaled to the range selection. |  |
| ![Toolbar of the curve diagram](images/171755105675_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlargement of the display. The ranges of the time axis and value axis are reduced every time the button is clicked. The curves are displayed larger. |  |
| ![Toolbar of the curve diagram](images/171755109643_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduction of the display. The ranges of the time axis and value axis are increased every time the button is clicked. The curves are displayed smaller. |  |
| ![Toolbar of the curve diagram](images/171755013387_DV_resource.Stream@PNG-de-DE.png) | Display all | Scales the display of the available data so that the entire time range and all values are displayed. |  |
| ![Toolbar of the curve diagram](images/171755117195_DV_resource.Stream@PNG-de-DE.png) | Automatic scaling of the value axis | Scaling of the display so that the entire value range is displayed for the set time range. |  |
| ![Toolbar of the curve diagram](images/171755159563_DV_resource.Stream@PNG-de-DE.png) | Show the overall time range | Scaling of the display so that the values in the value range currently displayed are displayed for the overall time range.  The value range displayed only then changes if "Display all values" ![Toolbar of the curve diagram](images/171755117195_DV_resource.Stream@PNG-de-DE.png) is activated.   **Note**   The automatic scaling of the time axis is stopped when a zoom function is activated for the time axis. This button reactivates the automatic adjustments for the time range. |  |
| ![Toolbar of the curve diagram](images/171754995467_DV_resource.Stream@PNG-de-DE.png) | - | Not used |  |
| ![Toolbar of the curve diagram](images/171755113611_DV_resource.Stream@PNG-de-DE.png) | Display samples | The samples are displayed as small circles on the curves. |  |
| ![Toolbar of the curve diagram](images/171755222667_DV_resource.Stream@PNG-de-DE.png) | - | Not used |  |
| ![Toolbar of the curve diagram](images/171754999051_DV_resource.Stream@PNG-de-DE.png) | Display vertical measurement cursors | Display of the vertical measurement cursors. The vertical position of the two measurement cursors can be moved with the mouse. The associated measured values and the difference of the measurement cursors corresponding to the position are shown in the signal table. Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display more information.  Also use the cursor keys. The following actions are possible for vertical measurement cursors with the cursor keys:  - Select - Positioning - Show or hide measurement cursor - Center measurement cursors |  |
| ![Toolbar of the curve diagram](images/171755002635_DV_resource.Stream@PNG-de-DE.png) | Display horizontal measurement cursors | Display of the horizontal measurement cursors.  The horizontal position of the two measurement cursors can be moved with the mouse.  Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display the values or to reposition the measurement cursor through entering the position.  Also use the cursor keys. The following actions are possible for horizontal measurement cursors with the cursor keys:  - Select - Positioning |  |
| ![Toolbar of the curve diagram](images/171755226635_DV_resource.Stream@PNG-de-DE.png) | Show/hide time range display | Show or hide the time range display below the curve diagram  The time range display shows the area in the curve diagram in yellow based on a selected signal. In the Bode diagram, the time range display has an effect on the frequency.  The yellow area can be moved with the mouse and the borders can be changed horizontally. |  |
| ![Toolbar of the curve diagram](images/171755055371_DV_resource.Stream@PNG-de-DE.png) | Show/hide chart legend | Showing or hiding of the legend in the curve diagram. |  |
| ![Toolbar of the curve diagram](images/171755059339_DV_resource.Stream@PNG-de-DE.png) | Align the chart legend to the left | Display of the legend on the left side of the curve diagram. |  |
| ![Toolbar of the curve diagram](images/171755063307_DV_resource.Stream@PNG-de-DE.png) | Align the chart legend to the right | Display of the legend on the right side of the curve diagram. |  |
| ![Toolbar of the curve diagram](images/171755006219_DV_resource.Stream@PNG-de-DE.png) | Change background color | Changeover between various background colors. |  |

###### Shortcut menu commands

The following table shows the shortcut menu commands in the curve diagram:

| Shortcut menu command | Description |  |
| --- | --- | --- |
| "Undo" | Undoes the display adjustments last made.  If several display adjustments have been made, they can be undone step-by-step.  Applicable to the following display adjustments:  - Show all - Display entire time range - Automatic scaling of the value axis - Move view - Zoom selection - Vertical zoom selection - Horizontal zoom selection - Zoom in - Zoom out |  |
| "Redo" | Redoes the last undone display adjustment.   If several display adjustments have been undone, they can be redone step-by-step. |  |
| ''Zoom in'' | Zoom in to the display. The ranges of the time axis and value axis are reduced every time the button is clicked. The curves are displayed larger. |  |
| ''Zoom out'' | Zoom out of the display. The ranges of the time axis and value axis are increased every time the button is clicked. The curves are displayed smaller. |  |
| "Display all" | Scales the display of the available data so that the entire time range and all values are displayed. |  |
| "Automatic scaling of the value axis" | Scaling of the display so that all values are displayed for the currently displayed time range.  The relative scaling ratio between the signals may change.    **Note**   The automatic scaling of the value axis is stopped when the zoom function is activated for the value axis. This button reactivates the automatic adjustments to the minimum/maximum values. |  |
| "Display entire time range" | Scaling of the display so that the values in the value range currently shown are displayed for the overall time range.  The value range displayed only then changes if "Display all values" is activated.   **Note**   The automatic scaling of the time axis is stopped when a zoom function is activated for the time axis. This button reactivates the automatic adjustments for the time range. |  |
| "Arrange in tracks" | Activate or deactivate the trace arrangement.  When the trace arrangement is activated the signals are arranged among themselves with the relevant value axes.  Signal groups are displayed in the same trace.  This setting does not affect the display for the bit traces. |  |
| "Measurement cursor" | You can find the following options in this submenu: |  |
| "Show vertical measurement cursors" | Display of vertical measurement cursor.  The vertical position of the two measurement cursors can be moved with the mouse. The associated measured values and the difference of the measurement cursors corresponding to the position are shown in the signal table. Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display further information.  Also use the cursor keys. The following actions are possible for vertical measurement cursors with the cursor keys:  - Select - Positioning - Show or hide measurement cursor - Center measurement cursors |  |
| "Show horizontal measurement cursors" | Display of the horizontal measurement cursors.  The horizontal position of the two measurement cursors can be moved with the mouse.  Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display the values or to reposition the measurement cursor through entering the position.  Also use the cursor keys. The following actions are possible for horizontal measurement cursors with the cursor keys:  - Select - Positioning |  |
| "Center measurement cursors" | Positions the activated measurement cursors at a central point in the current display. |  |
| "Save diagram as image" | Exports the current display in graphic format, e.g. as a bitmap. |  |
| "Copy image to clipboard" | Copies the current display to the clipboard. |  |
| "Add to measurements"  (Only axis control panel and PID, and only if FFT feature is enabled) | Adds the displayed recording to the "Measurements" system folder. |  |

##### User interface - signal table

See [User interface - signal table](#user-interface---signal-table) in the section User interface - Time diagram tab.

##### Interface - Formula editor

See [Interface - Formula editor](#interface---formula-editor) in the section User interface - Time diagram tab.

#### User interface - Bode diagram tab

This section contains information on the following topics:

- [User interface - curve diagram](#user-interface---curve-diagram-2)
- [User interface - signal table](#user-interface---signal-table-2)
- [Interface - Formula editor](#interface---formula-editor-2)

##### User interface - curve diagram

The Bode diagram shows the amplitude and phase of the transfer function as a function of the frequency. The X axis represents the frequency in Hertz.

The Y axis shows the following values:

- Amplitude response in the top curve diagram, values linear in decibels
- Phase response in the bottom curve diagram, values linear in degrees

The following requirements must be met for the calculation and display of the Bode diagram:

- The recording cycle must be constant.
- The input signal must contain at least three samples.

The curve diagram is calculated using two measured signals with the Bode formula in the formula editor and displayed.

###### Setting options and displays in the curve diagram

The following figure shows an example of the display:

![Setting options and displays in the curve diagram](images/171758984843_DV_resource.Stream@PNG-en-US.png)

Below the curve diagram, you can change the partitioning of the X axis with the options "Linear" and "Logarithmic".

###### Functions using the mouse wheel

The following table shows which functions are possible in the curve diagram using the mouse wheel:

| Function of the mouse wheel | Description |
| --- | --- |
| Move the curve diagram vertically | Turning the mouse wheel moves the display in the upper curve diagram up or down.   If the signals are arranged in traces, the display of the group is shifted below the cursor.  The mouse pointer must be positioned above the curve diagram with the analog signals. |
| Move the curve diagram horizontally | Turning the mouse wheel with the &lt;Shift&gt; button pressed down moves the display in the curve diagram to the left or the right.   The cursor must be positioned above the curve diagram. |
| Zoom in and zoom out | Turning the mouse wheel with the &lt;Ctrl&gt; button pressed down zooms in or out of the display in the curve diagram. The cursor position is the starting point for zooming in or out.  The value axis of the lower curve diagram (bit tracks) is not affected.  The cursor must be positioned above the curve diagram. |

###### Functions using the keyboard

The following table shows which keyboard commands are possible with a focus on the curve diagram:

| Shortcut key | Description |
| --- | --- |
| Selecting a measurement cursor |  |
| &lt;Ctrl+Shift+1&gt; | The vertical measurement cursor t1 is selected or deselected. |
| &lt;Ctrl+Shift+2&gt; | The vertical measurement cursor t2 is selected or deselected. |
| &lt;Ctrl+Shift+3&gt; | The horizontal measurement cursor Y1 is selected or deselected. |
| &lt;Ctrl+Shift+4&gt; | The horizontal measurement cursor Y2 is selected or deselected. |
| &lt;Tab&gt; | The next measurement cursor is selected. |
| Positioning a vertical measurement cursor |  |
| &lt;Left&gt;, &lt;Right&gt; | With the unit "Samples", the selected measurement cursor is moved by one sample by the signal in the foreground. |
| &lt;Shift+Left&gt;, &lt;Shift+Right&gt; | With the unit "Samples", the selected measurement cursor is moved by 10 samples by the signal in the foreground. |
| Positioning a horizontal measurement cursor |  |
| &lt;Up&gt;, &lt;Down&gt; | The selected measurement cursor is moved by one pixel along the Y axis. |
| &lt;Shift+Up&gt;, &lt;Shift+Down&gt; | The selected measurement cursor is moved by 10 pixels along the value axis. |
| Display of vertical measurement cursors |  |
| &lt;Ctrl+Space&gt; | The vertical measurement cursors are shown or hidden. |
| &lt;Ctrl+Shift+Space&gt; | The vertical measurement cursors are shown and centered for the current view. |
| Changing the view |  |
| &lt;Space&gt; | Move view |
| &lt;Ctrl+0&gt; | Set 100% view in open editor |
| &lt;Ctrl++&gt; | Apply zoom in with 10% |
| &lt;Ctrl+-&gt; | Apply zoom out with 10% |

###### Toolbar of the curve diagram

Tools are available for adapting the display via buttons.

The following table shows the functions of the buttons:

| Icon | Function | Description |  |
| --- | --- | --- | --- |
| ![Toolbar of the curve diagram](images/171754977547_DV_resource.Stream@PNG-de-DE.png) | Undo | Undoes the display adjustments last made.  If several display adjustments have been made, they can be undone step-by-step.  Applicable to the following display adjustments:  - Show all - Display entire time range - Automatic scaling of the value axis - Move view - Zoom selection - Vertical zoom selection - Horizontal zoom selection - Zoom in - Zoom out |  |
| ![Toolbar of the curve diagram](images/171754981131_DV_resource.Stream@PNG-de-DE.png) | Redo | Redoes the last undone display adjustment.   If several display adjustments have been undone, they can be redone step-by-step. |  |
| ![Toolbar of the curve diagram](images/171754651915_DV_resource.Stream@PNG-de-DE.png) | Standard view | Not used |  |
| ![Toolbar of the curve diagram](images/171755009803_DV_resource.Stream@PNG-de-DE.png) | Move view | Moves the display with the mouse button pressed. |  |
| ![Toolbar of the curve diagram](images/171754984715_DV_resource.Stream@PNG-de-DE.png) | Zoom selection | Selection of an arbitrary range with the mouse button pressed. The display is scaled to the range selection. |  |
| ![Toolbar of the curve diagram](images/171754988299_DV_resource.Stream@PNG-de-DE.png) | Vertical zoom selection | Selection of a vertical range with the mouse button pressed. The display is scaled to the range selection.  Depending on the mouse position, the selection influences either the amplitude response or the phase response. |  |
| ![Toolbar of the curve diagram](images/171754991883_DV_resource.Stream@PNG-de-DE.png) | Horizontal zoom selection | Selection of a horizontal range with the mouse button pressed. The display is scaled to the range selection. |  |
| ![Toolbar of the curve diagram](images/171755105675_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlargement of the display. The ranges of the time axis and value axis are reduced every time the button is clicked. The curves are displayed larger. |  |
| ![Toolbar of the curve diagram](images/171755109643_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduction of the display. The ranges of the time axis and value axis are increased every time the button is clicked. The curves are displayed smaller. |  |
| ![Toolbar of the curve diagram](images/171755013387_DV_resource.Stream@PNG-de-DE.png) | Display all | Scales the display of the available data so that the entire time range and all values are displayed. |  |
| ![Toolbar of the curve diagram](images/171755117195_DV_resource.Stream@PNG-de-DE.png) | Automatic scaling of the value axis | Scaling of the display so that the entire value range is displayed for the set time range. |  |
| ![Toolbar of the curve diagram](images/171755159563_DV_resource.Stream@PNG-de-DE.png) | Show the overall time range | Scaling of the display so that the values in the value range currently displayed are displayed for the overall time range.  The value range displayed only then changes if "Display all values" ![Toolbar of the curve diagram](images/171755117195_DV_resource.Stream@PNG-de-DE.png) is activated.   **Note**   The automatic scaling of the time axis is stopped when a zoom function is activated for the time axis. This button reactivates the automatic adjustments for the time range. |  |
| ![Toolbar of the curve diagram](images/171754995467_DV_resource.Stream@PNG-de-DE.png) | - | Not used |  |
| ![Toolbar of the curve diagram](images/171755113611_DV_resource.Stream@PNG-de-DE.png) | Display samples | The samples are displayed as small circles on the curves. |  |
| ![Toolbar of the curve diagram](images/171755222667_DV_resource.Stream@PNG-de-DE.png) | - | Not used |  |
| ![Toolbar of the curve diagram](images/171754999051_DV_resource.Stream@PNG-de-DE.png) | Display vertical measurement cursors | Display of the vertical measurement cursors. The vertical position of the two measurement cursors can be moved with the mouse. The associated measured values and the difference of the measurement cursors corresponding to the position are shown in the signal table. Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display more information.  Also use the cursor keys. The following actions are possible for vertical measurement cursors with the cursor keys:  - Select - Positioning - Show or hide measurement cursor - Center measurement cursors |  |
| ![Toolbar of the curve diagram](images/171755002635_DV_resource.Stream@PNG-de-DE.png) | Display horizontal measurement cursors | Display of the horizontal measurement cursors.  The horizontal position of the two measurement cursors can be moved with the mouse.  Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display the values or to reposition the measurement cursor through entering the position.  Also use the cursor keys. The following actions are possible for horizontal measurement cursors with the cursor keys:  - Select - Positioning |  |
| ![Toolbar of the curve diagram](images/171755226635_DV_resource.Stream@PNG-de-DE.png) | Show/hide time range display | Show or hide the time range display below the curve diagram  The time range display shows the area in the curve diagram in yellow based on a selected signal. In the Bode diagram, the time range display has an effect on the frequency.  The yellow area can be moved with the mouse and the borders can be changed horizontally. |  |
| ![Toolbar of the curve diagram](images/171755055371_DV_resource.Stream@PNG-de-DE.png) | Show/hide chart legend | Showing or hiding of the legend in the curve diagram. |  |
| ![Toolbar of the curve diagram](images/171755059339_DV_resource.Stream@PNG-de-DE.png) | Align the chart legend to the left | Display of the legend on the left side of the curve diagram. |  |
| ![Toolbar of the curve diagram](images/171755063307_DV_resource.Stream@PNG-de-DE.png) | Align the chart legend to the right | Display of the legend on the right side of the curve diagram. |  |
| ![Toolbar of the curve diagram](images/171755006219_DV_resource.Stream@PNG-de-DE.png) | Change background color | Changeover between various background colors. |  |

###### Shortcut menu commands

The following table shows the shortcut menu commands in the curve diagram:

| Shortcut menu command | Description |  |
| --- | --- | --- |
| "Undo" | Undoes the display adjustments last made.  If several display adjustments have been made, they can be undone step-by-step.  Applicable to the following display adjustments:  - Show all - Display entire time range - Automatic scaling of the value axis - Move view - Zoom selection - Vertical zoom selection - Horizontal zoom selection - Zoom in - Zoom out |  |
| "Redo" | Redoes the last undone display adjustment.   If several display adjustments have been undone, they can be redone step-by-step. |  |
| ''Zoom in'' | Zoom in to the display. The ranges of the time axis and value axis are reduced every time the button is clicked. The curves are displayed larger. |  |
| ''Zoom out'' | Zoom out of the display. The ranges of the time axis and value axis are increased every time the button is clicked. The curves are displayed smaller. |  |
| "Display all" | Scales the display of the available data so that the entire time range and all values are displayed. |  |
| "Automatic scaling of the value axis" | Scaling of the display so that all values are displayed for the currently displayed time range.  The relative scaling ratio between the signals may change.    **Note**   The automatic scaling of the value axis is stopped when the zoom function is activated for the value axis. This button reactivates the automatic adjustments to the minimum/maximum values. |  |
| "Display entire time range" | Scaling of the display so that the values in the value range currently shown are displayed for the overall time range.  The value range displayed only then changes if "Display all values" is activated.   **Note**   The automatic scaling of the time axis is stopped when a zoom function is activated for the time axis. This button reactivates the automatic adjustments for the time range. |  |
| "Measurement cursor" | You can find the following options in this submenu: |  |
| "Show vertical measurement cursors" | Display of vertical measurement cursor.  The vertical position of the two measurement cursors can be moved with the mouse. The associated measured values and the difference of the measurement cursors corresponding to the position are shown in the signal table. Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display further information.  Also use the cursor keys. The following actions are possible for vertical measurement cursors with the cursor keys:  - Select - Positioning - Show or hide measurement cursor - Center measurement cursors |  |
| "Show horizontal measurement cursors" | Display of the horizontal measurement cursors.  The horizontal position of the two measurement cursors can be moved with the mouse.  Display the ["Measurement cursor" pane](#user-interface---measurement-cursor-pane) in the Trace task card in order to display the values or to reposition the measurement cursor through entering the position.  Also use the cursor keys. The following actions are possible for horizontal measurement cursors with the cursor keys:  - Select - Positioning |  |
| "Center measurement cursors" | Positions the activated measurement cursors at a central point in the current display. |  |
| "Save diagram as image" | Exports the current display in graphic format, e.g. as a bitmap. |  |
| "Copy image to clipboard" | Copies the current display to the clipboard. |  |
| "Add to measurements" (Axis control panel and PID only, and only if Bode feature is enabled) | Adds the displayed recording to the "Measurements" system folder. |  |

##### User interface - signal table

See [User interface - signal table](#user-interface---signal-table) in the section User interface - Time diagram tab.

##### Interface - Formula editor

See [Interface - Formula editor](#interface---formula-editor) in the section User interface - Time diagram tab.

#### User interface - Signal selection tab (Combined measurements)

This section contains information on the following topics:

- [User interface - Signal selection (Combined measurements)](#user-interface---signal-selection-combined-measurements)

##### User interface - Signal selection (Combined measurements)

The Signal selection tab shows the signals for all measurements and allows signals that are presented in the signal table of the diagram to be preselected.

###### Setting options and displays in the Signal selection tab.

The following figure shows an example of the display:

![Setting options and displays in the Signal selection tab.](images/171758988811_DV_resource.Stream@PNG-en-US.png)

The following table shows the settings and displays for the table:

| Column | Description |
| --- | --- |
| ![Setting options and displays in the Signal selection tab.](images/171755289355_DV_resource.Stream@PNG-de-DE.png) | Static display of the signal icon |
| "Available in the diagram" | Selection for the display in the curve diagram  When the selection is activated the signal is transferred to the signal table for the curve diagram. |
| “Measurement” | Display of the measurement to which the signal belongs |
| “Name” | Display of the signal name |
| “Data type “ | Display of the data type |
| "Address" | Display of the address (not for symbolic tags) |
| "Scaling group" | Display of the scaling group name |
| "Comment" | Display of a comment on the signal |

You will find further information on the specific settings in [User interface - signal table](#user-interface---signal-table).

###### Shortcut menu commands

The following table shows the shortcut menu commands for the signal selection:

| Shortcut menu command | Description |
| --- | --- |
| "Copy" | Copies the content of the selected lines to the clipboard. |
| “Display selection in the signal table” | The selected signals are displayed in the signal table and are available in the diagram. |
| “Remove selection from the signal table” | The removed signals are not available in the diagram. |

Several objects can be selected.

### Inspector window

This section contains information on the following topics:

- [Interface - Inspector window](#interface---inspector-window)

#### Interface - Inspector window

The Inspector window displays general information about the trace.

Additional information is available for measurements:

- Time stamp range

  The availability of the time stamps depends on the configured recording conditions.
- Measuring point range
- Cycle time range

  For equidistant cycle recordings, the time duration between two measurement points is displayed.

  This time, for example, can be used in the formula editor.

##### Sample time stamp

The following figure shows the time stamps for a measurement:

![Sample time stamp](images/171755578891_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Analysis of measurements with sporadically occurring recording condition**
>
> When evaluating your measurements, keep in mind that the recording condition between the activation time and the trigger time may not have been fulfilled.

### Trace task card

This section contains information on the following topics:

- [User interface - Measurement cursor pane](#user-interface---measurement-cursor-pane)
- [User interface - Snapshots pane](#user-interface---snapshots-pane)

#### User interface - Measurement cursor pane

The "Measurement cursor" pane shows the position of the measurement cursor in the curve diagram and the values at the intersection points.

##### Setting options and displays of the "Measurement cursor" pane

The figure below shows the "Measurement cursor" pane:

![Setting options and displays of the "Measurement cursor" pane](images/171758993419_DV_resource.Stream@PNG-en-US.png)

The following table describes the settings and displays:

| Setting/display |  | Description |
| --- | --- | --- |
| Horizontal measurement cursor |  |  |
|  | Y1 | Position of first measurement cursor  The value states the position in relation to the scale of the signal currently selected. You also have the option of specifying a new position for the measurement cursor in this entry field for moving with the mouse. |
| Y2 | Position of the second measurement cursor  The value states the position in relation to the scale of the signal currently selected. You also have the option of specifying a new position for the measurement cursor in this entry field for moving with the mouse. |  |
| ΔY | Display of the position difference between the first and the second measurement cursor |  |
| Vertical measurement cursor |  |  |
|  | t1 | Position of first measurement cursor  You also have the option of specifying a new position for the measurement cursor in this entry field for moving with the mouse. |
| t2 | Position of the second measurement cursor  You also have the option of specifying a new position for the measurement cursor in this entry field for moving with the mouse. |  |
| Δt | Display of the position difference between the first and the second measurement cursor |  |
| Intersection points with selected signal |  |  |
|  | Y(t1) | Display of the value at the position of the first measurement cursor |
| Y(t2) | Display of the value at the position of the second measurement cursor |  |
| ΔY | Display of the value difference between the first and the second measurement cursor |  |
| Mathematical analysis in the range of the measurement cursor·[t1;t2] for the selected signal (not for Bode diagram) |  |  |
|  | AM(Y) | Mean  The arithmetic mean is calculated for the range between the vertical measurement cursors. |
| INT(Y) | Integral  The integral is calculated for the range between the vertical measurement cursors. |  |
| RMS(Y) | RMS value  The root-mean square (RMS value) is calculated for the range between the vertical measurement cursors. |  |

---

**See also**

[User interface - curve diagram](#user-interface---curve-diagram)

#### User interface - Snapshots pane

The "Snapshots" pane allows the user to save and restore different views for a measurement.

A snapshot is taken of the current view in the "Timing diagram" or "Bode diagram" tab. The snapshots are saved in the measurement with the project.

##### Setting options and displays of the "Snapshots" pane

The figure below shows the "Snapshots" pane:

![Setting options and displays of the "Snapshots" pane](images/171759023627_DV_resource.Stream@PNG-en-US.png)

The following table shows the functions of the buttons:

| Icon | Description |
| --- | --- |
| ![Setting options and displays of the "Snapshots" pane](images/171755585419_DV_resource.Stream@PNG-de-DE.png) | Generate snapshot of the current view  Saves the current view as a snapshot in the "Timing diagram" or "Bode diagram" tab. |

The following table shows the settings and displays:

| Column | Description |
| --- | --- |
| ![Setting options and displays of the "Snapshots" pane](images/171755589387_DV_resource.Stream@PNG-de-DE.png) | Static display of the snapshot symbol |
| "Name" | Display and change options for the name |
| "Time stamp" | Display of the snapshot generation time |
| "Comment" | Display and input option for a comment |

Several rows can be selected and deleted.

Double-clicking on a row opens the measurement with the saved view in the "Time diagram" or "Bode diagram" tab.

##### Shortcut menu commands

The following table shows the shortcut menu commands of the table:

| Shortcut menu command | Description |
| --- | --- |
| "Restore snapshot" | Shows the measurement with the saved view in the "Time diagram" or "Bode diagram" tab. |
| "Delete" | Deletes the snapshot |
| "Rename" | Switches the cell to the editing mode |

Several rows can be selected and deleted.

## Project trace software user interface

This section contains information on the following topics:

- [Structure of the user interface](#structure-of-the-user-interface-1)
- [Project tree](#project-tree-1)
- [Working area](#working-area-1)
- [Inspector window](#inspector-window-1)
- [Trace task card](#trace-task-card-1)

### Structure of the user interface

The user interface of the project trace consists of several combined areas.

The figure below shows an example of the layout of the user interface:

![Figure](images/171759028235_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| **Project tree**   Manage and create project traces and measurements directly in the project tree and via shortcut-menu commands. |  |
| **Working area** |  |
|  | ① Title bar of the working area  Displays the name of the project trace. |
| ② Project trace toolbar  Buttons to manage the project traces:  - Transfer trace configurations to the devices - Display status overview of participating devices - Establish online connection to participating devices - Activating/deactivating project traces - Deleting project traces - Transferring measurements from the devices to the project |  |
| ③ Status display of the project trace   Display of the current status of the recording. |  |
| ④ Configuration tab  Configuration of the participating devices and signals for the project trace. |  |
| ⑤ Time diagram tab  Display of the recorded values as a curve diagram and the signals from the displayed measurement.   Specification of the display options. |  |
| **⑥"Trace" task card**   Display of the measurement cursor data with mathematical evaluation ⑥ and snapshots. |  |
| **⑦ Inspector window**   Device-specific configuration of the recording duration, trigger condition and signal selection.  Display of general information about the project trace. |  |

---

**See also**

[Devices](#devices)

### Project tree

This section contains information on the following topics:

- [User interface - Project tree folder "Cross-device functions" - "Project traces"](#user-interface---project-tree-folder-cross-device-functions---project-traces)

#### User interface - Project tree folder "Cross-device functions" - "Project traces"

Project trace configurations and measurements ![Figure](images/171754042251_DV_resource.Stream@PNG-de-DE.png)are shown in the system folder ![Figure](images/171755772555_DV_resource.Stream@PNG-de-DE.png) "Project traces".

Double-click a project trace to open the corresponding "Configuration" or "Time diagram" tab in the working area.

##### Symbols in the "Project traces" folder

The following table explains the symbols in the folder ![Symbols in the "Project traces" folder](images/171755772555_DV_resource.Stream@PNG-de-DE.png) "Project traces":

| Icon |  | Description |
| --- | --- | --- |
| ![Symbols in the "Project traces" folder](images/67316559115_DV_resource.Stream@PNG-de-DE.png) |  | Adding a project trace configuration  Double-click the symbol to add a new project trace configuration and open the "Configuration" tab. |
| ![Symbols in the "Project traces" folder](images/171755776523_DV_resource.Stream@PNG-de-DE.png) |  | Project trace configuration  Double-click the icon to open the "Configuration" or "Time diagram" tab. |
| ![Symbols in the "Project traces" folder](images/171754676619_DV_resource.Stream@PNG-de-DE.png) |  | "Measurements" folder  The folder contains combined measurements that were added using the ![Symbols in the "Project traces" folder](images/171754848267_DV_resource.Stream@PNG-de-DE.png) button. The measurements are compatible with the combined measurements within the devices. The configurations of the individual measurements are displayed when the combined measurement is copied or moved to the corresponding folder of a device. |
|  | ![Symbols in the "Project traces" folder](images/171754042251_DV_resource.Stream@PNG-de-DE.png) | Measurement   Double-click the icon to open the "Time diagram" tab. |

##### **Shortcut menu commands**

The following table shows the shortcut-menu commands for the system folder ![Shortcut menu commands](images/171755772555_DV_resource.Stream@PNG-de-DE.png) "Project traces":

| Shortcut menu command | Description |
| --- | --- |
| "Add new project trace" | Adds a new project trace and opens the "Configuration" tab. |

The following table shows the shortcut-menu commands for the project trace configuration ![Shortcut menu commands](images/171755776523_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Description |
| --- | --- |
| "Delete" | Deletes the selected objects from the project tree or from the device. |
| "Rename" | Switches the selected object to the editing mode. |

> **Note**
>
> **Shortcut menu commands for the**
>
> ![Shortcut menu commands](images/171754676619_DV_resource.Stream@PNG-de-DE.png)
>
> "Measurements" system folder
>
> The shortcut commands are described in [User interface - "Combined measurements" project tree folder](#user-interface---combined-measurements-project-tree-folder).
>
> You can export measurements of the project trace as combined measurement and import them again under a device. For the import, use the shortcut menu of the system folder ![Shortcut menu commands](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Combined measurements" under the device.

### Working area

This section contains information on the following topics:

- [User interface - Project trace toolbar](#user-interface---project-trace-toolbar)
- [User interface - status overview of the participating devices](#user-interface---status-overview-of-the-participating-devices)
- [User interface - Configuration tab](#user-interface---configuration-tab-1)
- [User interface - Time diagram tab](#user-interface---time-diagram-tab-1)

#### User interface - Project trace toolbar

Buttons provide tools for handling the project trace.

The following table shows the functions of the buttons:

| Icon | Description |
| --- | --- |
| ![Figure](images/171754781195_DV_resource.Stream@PNG-de-DE.png) | Transferring the trace configurations to the devices  The trace configurations are transferred to the participating devices. |
| ![Figure](images/171755848459_DV_resource.Stream@PNG-de-DE.png) | Display of the status overview  Shows the [status overview of the participating devices](#user-interface---status-overview-of-the-participating-devices). |
| ![Figure](images/171755780491_DV_resource.Stream@PNG-de-DE.png) | Establishing an online connection  The online connection to the participating devices is established. |
| ![Figure](images/171754840331_DV_resource.Stream@PNG-de-DE.png) | Activate recording  If the recording of an installed trace is repeated, then the settings relevant for the display (curve diagram and signal table) are also retained for the new recording.   You cannot redo an interrupted recording.   **Note**   When a recording is restarted, the previously recorded values are lost.  To save the recorded values, save the measurement in the project before you activate the recording again. |
| ![Figure](images/171754844299_DV_resource.Stream@PNG-de-DE.png) | Deactivate recording  Deactivates the traces in all devices that can be reached online. |
| ![Figure](images/171754890635_DV_resource.Stream@PNG-de-DE.png) | Delete traces from devices  Deletes the traces from the participating devices that can be reached online. |
| ![Figure](images/171754848267_DV_resource.Stream@PNG-de-DE.png) | Transferring measurements from the devices to the project  The measurements are added to the system folder ![Figure](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Measurements".   **Note**   Only the data loaded from the devices is saved. This data is displayed in the curve diagram. If necessary, wait until the display is updated. |

#### User interface - status overview of the participating devices

The dialog shows status information about the participating devices.

For participating devices with status without error, you can apply trace configurations to the devices.

##### Display in the status overview table

The following table shows the displays of the status overview:

| Column |  | Description |
| --- | --- | --- |
| - |  | Display of whether there is an error for the project trace in the participating device or whether the trace configuration is faulty.  A tooltip above the symbol displays information about the cause of the error. |
|  | ![Display in the status overview table](images/171755852427_DV_resource.Stream@PNG-de-DE.png) | **Meaning in offline mode**   - Configured trace is faulty    **Meaning in online mode**   - Configured trace is faulty - Recording was interrupted - Connection error |
| Device |  | Display of the device name |
| Device status |  | Status display of the online connection |
|  | ![Display in the status overview table](images/171755856395_DV_resource.Stream@PNG-de-DE.png) | Offline |
| ![Display in the status overview table](images/171755937163_DV_resource.Stream@PNG-de-DE.png) | Connect or disconnect |  |
| ![Display in the status overview table](images/171755941131_DV_resource.Stream@PNG-de-DE.png) | Online |  |
| Trace status |  | Status display of the devices  If there is an existing online connection, a symbol indicates the status of the trace configuration for the corresponding device. In addition, the trace status for the device is displayed, for example, "Monitoring".   **Note**   If only one device in the project trace shows the "Monitoring" trace status, the project trace is not working correctly; there is no time synchronization between the devices. |
|  | ![Display in the status overview table](images/67336425739_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are identical |
| ![Display in the status overview table](images/67336416907_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are different |  |
| ![Display in the status overview table](images/171755455755_DV_resource.Stream@PNG-de-DE.png) | Configuration only exists offline |  |

##### Remedy for errors

The following list shows possible sources of error and the remedy.

- Firmware

  With the [devices](#devices) it is described if and from which firmware a device supports the project trace.
- Trace configuration

  Check the settings for the respective device in the "Properties" tab of the Inspector window.
- Canceled recording

  You can restart an interrupted recording by transferring the trace configurations again.
- Project trace requirements

  Check that the [general requirements for the project trace](#general) are met.

#### User interface - Configuration tab

This section contains information on the following topics:

- [User interface - Configuration](#user-interface---configuration-1)

##### User interface - Configuration

The "Configuration" tab is used to define the participating devices for the project trace. You configure the device-dependent trace configuration and the properties of the project trace in the [Inspector window](#interface---inspector-window-1).

The displayed trace configuration is always the offline configuration, even with an existing online connection. Transfer changes of the trace configurations to the devices using the ![Figure](images/171754781195_DV_resource.Stream@PNG-de-DE.png) button.

###### Setting options and displays in the overview of the participating devices

The figure below shows an example of the display of the overviews table:

![Setting options and displays in the overview of the participating devices](images/171759038475_DV_resource.Stream@PNG-en-US.png)

The following table shows the settings and displays of the participating devices:

| Column |  | Description |
| --- | --- | --- |
| Device |  | Input of the device name |
|  | ![Setting options and displays in the overview of the participating devices](images/29567349259_DV_resource.Stream@PNG-de-DE.png) | Button to open the device selection table  The button is displayed when the table line is selected. Clicking the symbol opens a table which offers possible devices for selection. The selected device is displayed in the input field. |
| Trigger |  | The symbol ![Setting options and displays in the overview of the participating devices](images/171756055051_DV_resource.Stream@PNG-de-DE.png) indicates which devices can activate a trigger.  Configure this device-dependent setting in the "Properties" tab of the Inspector window. |
| Trace sample event |  | Display of the trace sample event  In the "Properties" tab of the Inspector window, configure in which cycle (OB with a SIMATIC CPU) the recording should take place. |
| Cycle time |  | Display of the time cycle resulting from the selection of the trace sample event |
| Record every |  | Input of the reduction ratio |
| Number of samples |  | Input of the number of samples to be recorded  The recording duration is adjusted according to the input. |
| Recording duration |  | Input of the recording duration  The number of samples is adjusted according to the input. |
| Errors |  | Display of an error in the trace configuration |
|  | ![Setting options and displays in the overview of the participating devices](images/171755948683_DV_resource.Stream@PNG-de-DE.png) | A tooltip above the symbol displays information about the cause of the error.  Configured traces with the Error status cannot be transferred to the device. |

#### User interface - Time diagram tab

The "Time diagram" tab of the project trace behaves in the same way as the trace and is described in the section [User interface - Time diagram tab](#user-interface---time-diagram-tab).

### Inspector window

This section contains information on the following topics:

- [Interface - Inspector window](#interface---inspector-window-1)

#### Interface - Inspector window

The display in the "Properties" tab of the Inspector window depends on the current selection in the working area.

If no table row with a device is selected in the working area, general information about the project trace is displayed. If a table row with a device is selected, the device-dependent trace configuration is displayed, which is described for the respective [device](#devices).

##### General information in the "Properties" tab.

The following figure shows an example of the display:

![General information in the "Properties" tab.](images/171759043083_DV_resource.Stream@PNG-en-US.png)

The following table shows the settings and displays of the recorded signals:

| Field | Description |
| --- | --- |
| Name | Input field for the name of the project trace |
| Author | Input field for the name of the author |
| Comment | Input field for a comment. |
| Trace ID | Display of the Trace ID  Using this ID, you can distinguish, for example, between several active project traces. |
| Port number | Input field for the port number of the connection  The devices participating in the project trace communicate via this port. The numbers must be identical and unique on all devices.  Observe also the instructions for assigning port numbers in the TIA Portal information system. |

### Trace task card

The displayed panes are described in the section "[Trace task card](#trace-task-card)".

## Long-term project trace software user interface

This section contains information on the following topics:

- [Structure of the user interface](#structure-of-the-user-interface-2)
- [Project tree](#project-tree-2)
- [Workspace](#workspace)
- [Inspector window](#inspector-window-2)
- [Trace task card](#trace-task-card-2)

### Structure of the user interface

The user interface of the long-term project trace consists of several combined areas.

The figure below shows an example of the layout of the user interface:

![Figure](images/172451548427_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| **Project tree**   Manage and create long-term project traces and measurements directly in the project tree and via shortcut-menu commands. |  |
| **Workspace** |  |
|  | ① Title bar of the workspace  Shows the name of the long-term project trace |
| ② Toolbar of the long-term project trace.   Buttons to manage the long-term project traces:  - Apply trace configurations to the devices - Display status overview of participating devices - Establish online connection to participating devices - Activate/deactivate recording - Delete traces from devices - Add to measurements |  |
| ③ Status display of long-term project trace.  Display of the current status of the recording. |  |
| ④ Configuration tab  Configuration of the participating devices and signals for the long-term project trace. |  |
| ⑤ Time diagram tab  Display the recorded values as a curve diagram and the signals from the displayed measurement. Specify the display options. |  |
| **⑥ "Trace" task card**   Display of the measurement cursor data with mathematical evaluation |  |
| **⑦ Inspector window**   Device-specific configuration Display of general information for the long-term project trace |  |

### Project tree

This section contains information on the following topics:

- [User interface - Project tree folder "Cross-device functions" - "Long-term project traces"](#user-interface---project-tree-folder-cross-device-functions---long-term-project-traces)

#### User interface - Project tree folder "Cross-device functions" - "Long-term project traces"

Long-term project traces configurations and measurements ![Figure](images/171754042251_DV_resource.Stream@PNG-de-DE.png) are shown in the system folder ![Figure](images/171755772555_DV_resource.Stream@PNG-de-DE.png) "Long-term project traces".

Double-click on a long-term project trace to open the corresponding "Configuration" or "Time diagram" tab in the workspace.

##### Icons in the "Long-term project traces" folder

The following table explains the icons in the ![Icons in the "Long-term project traces" folder](images/171755772555_DV_resource.Stream@PNG-de-DE.png) "Long-term project traces" folder:

| Icon |  | Description |
| --- | --- | --- |
| ![Icons in the "Long-term project traces" folder](images/67316559115_DV_resource.Stream@PNG-de-DE.png) |  | Add long-term project trace configuration  Double-click the icon to add a new long-term project trace configuration and open the "Configuration" tab. |
| ![Icons in the "Long-term project traces" folder](images/171755776523_DV_resource.Stream@PNG-de-DE.png) |  | Long-term project trace configuration  Double-click the icon to open the "Configuration" or "Time diagram" tab. |
| ![Icons in the "Long-term project traces" folder](images/171754676619_DV_resource.Stream@PNG-de-DE.png) |  | "Measurements" folder  The folder contains combined measurements that were added using the ![Icons in the "Long-term project traces" folder](images/171754848267_DV_resource.Stream@PNG-de-DE.png) button. The measurements are compatible with the combined measurements within the devices. The configurations of the individual measurements are displayed when the combined measurement is copied or moved to the corresponding folder of a device. |
|  | ![Icons in the "Long-term project traces" folder](images/171754042251_DV_resource.Stream@PNG-de-DE.png) | Measurement   Double-click the icon to open the "Time diagram" tab. |

##### **Shortcut menu commands**

The following table shows the shortcut-menu commands for the system folder ![Shortcut menu commands](images/171755772555_DV_resource.Stream@PNG-de-DE.png) "Long-term project traces":

| Shortcut menu command | Description |
| --- | --- |
| "Add new long-term project trace" | Adds a new long-term project trace and opens the "Configuration" tab. |

The following table shows the shortcut-menu commands for the long-term project trace configuration ![Shortcut menu commands](images/171755776523_DV_resource.Stream@PNG-de-DE.png):

| Shortcut menu command | Description |
| --- | --- |
| "Delete" | Deletes the selected objects from the project tree or from the device. |
| "Rename" | Switches the selected object to the editing mode. |

> **Note**
>
> **Shortcut menu commands for the**
>
> ![Shortcut menu commands](images/171754676619_DV_resource.Stream@PNG-de-DE.png)
>
> "Measurements" system folder
>
> The shortcut commands are described in [User interface - "Combined measurements" project tree folder](#user-interface---combined-measurements-project-tree-folder).

### Workspace

This section contains information on the following topics:

- [User interface - Long-term project trace toolbar](#user-interface---long-term-project-trace-toolbar)
- [User interface - status overview of the participating devices](#user-interface---status-overview-of-the-participating-devices-1)
- [User interface - Configuration tab](#user-interface---configuration-tab-2)
- [User interface - Time diagram tab](#user-interface---time-diagram-tab-2)

#### User interface - Long-term project trace toolbar

Tools for handling the long-term project trace are available via buttons.

The following table shows the functions of the buttons:

| Icon | Description |
| --- | --- |
| ![Figure](images/171754781195_DV_resource.Stream@PNG-de-DE.png) | Transferring the trace configurations to the devices  The trace configurations are transferred to the participating devices. |
| ![Figure](images/171755848459_DV_resource.Stream@PNG-de-DE.png) | Display of the status overview  Shows the [status overview of the participating devices](#user-interface---status-overview-of-the-participating-devices-1). |
| ![Figure](images/171755780491_DV_resource.Stream@PNG-de-DE.png) | Establishing an online connection  The online connection to the participating devices is established. |
| ![Figure](images/171754840331_DV_resource.Stream@PNG-de-DE.png) | Activate recording  If the recording of a trace is repeated, then the settings relevant for the display (curve diagram and signal table) are also retained for the new recording.   You cannot redo an interrupted recording.   **Note**   When a recording is restarted, the previously recorded values are lost.  To save the recorded values, save the measurement in the project before you activate the recording again. |
| ![Figure](images/171754844299_DV_resource.Stream@PNG-de-DE.png) | Deactivate recording  Deactivates the traces in all devices that can be reached online. |
| ![Figure](images/171754890635_DV_resource.Stream@PNG-de-DE.png) | Delete traces from devices  Deletes the traces from the participating devices that can be reached online. |
| ![Figure](images/171754848267_DV_resource.Stream@PNG-de-DE.png) | Add to measurements  The recording is added as a measurement in the system folder ![Figure](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Measurements". |

#### User interface - status overview of the participating devices

The dialog shows status information about the participating devices.

For participating devices with status without error, you can apply trace configurations to the devices.

##### Display in the status overview table

The following table shows the displays of the status overview:

| Column |  | Description |
| --- | --- | --- |
| - |  | Display of whether there is an error for the long-term project trace in the participating device or whether the trace configuration is faulty.  A tooltip above the symbol displays information about the cause of the error. |
|  | ![Display in the status overview table](images/171755852427_DV_resource.Stream@PNG-de-DE.png) | **Meaning in offline mode**   - Configured trace is faulty    **Meaning in online mode**   - Configured trace is faulty - Recording was interrupted - Connection error |
| Device |  | Display of the device name |
| Device status |  | Status display of the online connection |
|  | ![Display in the status overview table](images/171755856395_DV_resource.Stream@PNG-de-DE.png) | Offline |
| ![Display in the status overview table](images/171755937163_DV_resource.Stream@PNG-de-DE.png) | Connect or disconnect |  |
| ![Display in the status overview table](images/171755941131_DV_resource.Stream@PNG-de-DE.png) | Online |  |
| Trace status |  | Status display of the devices  If there is an existing online connection, a symbol indicates the status of the trace configuration for the corresponding device. In addition, the trace status for the device is displayed, for example, "Monitoring".   **Note**   If only one device in the long-term project trace shows the "Monitoring" trace status, the long-term project trace is not working correctly; there is no time synchronization between the devices. |
|  | ![Display in the status overview table](images/67336425739_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are identical |
| ![Display in the status overview table](images/67336416907_DV_resource.Stream@PNG-de-DE.png) | Online and offline configuration are different |  |
| ![Display in the status overview table](images/171755455755_DV_resource.Stream@PNG-de-DE.png) | Configuration only exists offline |  |

##### Remedy for errors

The following list shows possible sources of error and the remedy.

- Firmware

  With the [devices](#devices) it is described if and from which firmware a device supports the long-term project trace.
- Trace configuration

  Check the settings for the respective device in the "Properties" tab of the Inspector window.
- Canceled recording

  You can restart an interrupted recording by transferring the trace configurations again.
- Project trace requirements

  Check that the [general requirements for the long-term project trace](#general-1) are fulfilled.

#### User interface - Configuration tab

This section contains information on the following topics:

- [User interface - Configuration](#user-interface---configuration-2)

##### User interface - Configuration

The "Configuration" tab is used to define the participating devices for the long-term project trace. You configure the device-dependent trace configuration and the properties of the long-term project trace in the [Inspector window](#inspector-window-2).

The displayed trace configuration is always the offline configuration, even with an existing online connection. Transfer changes of the trace configurations to the devices using the ![Figure](images/171754781195_DV_resource.Stream@PNG-de-DE.png) button.

###### Setting options and displays in the overview of the participating devices

The figure below shows an example of the display of the overviews table:

![Setting options and displays in the overview of the participating devices](images/172448150795_DV_resource.Stream@PNG-en-US.png)

The following table shows the settings and displays of the participating devices:

| Column |  | Description |
| --- | --- | --- |
| Device |  | Input of the device name |
|  | ![Setting options and displays in the overview of the participating devices](images/29567349259_DV_resource.Stream@PNG-de-DE.png) | Button to open the device selection table  The button is displayed when the table line is selected. Clicking the symbol opens a table which offers possible devices for selection. The selected device is displayed in the input field.  The number of devices that can be selected in the table is limited to 5. After 5 devices have been selected, this button is available only in read mode. |
| Cycle time |  | Display of the time cycle resulting from the selection of the trace sample event |
| Record every |  | Input of the reduction ratio |
| Target path |  | Display of the folder used for recording the long-term project traces. |
| Errors |  | Display of an error in the trace configuration |
|  | ![Setting options and displays in the overview of the participating devices](images/171755948683_DV_resource.Stream@PNG-de-DE.png) | A tooltip above the symbol displays information about the cause of the error.  Configured traces with the Error status cannot be transferred to the device. |

#### User interface - Time diagram tab

The "Time diagram" tab of the long-term project trace behaves in the same way as the trace and is described in the section [User interface - Time diagram tab](#user-interface---time-diagram-tab).

### Inspector window

This section contains information on the following topics:

- [Interface - Inspector window](#interface---inspector-window-2)

#### Interface - Inspector window

The display in the "Properties" tab of the Inspector window depends on the current selection in the workspace.

If no table row with a device is selected in the workspace, general information about the long-term project trace is displayed. If a table row with a device is selected, the device-dependent trace configuration is displayed, which is described for the respective device.

##### General information in the "Properties" tab.

The following figure shows an example of the display:

![General information in the "Properties" tab.](images/172446992651_DV_resource.Stream@PNG-en-US.png)

The following table shows the settings and displays of the recorded signals:

| Field | Description |
| --- | --- |
| Name | Input field for the name of the long-term project trace |
| Author | Input field for the name of the author |
| Comment | Input field for a comment. |
| Target path | Display of the folder used for storing the long-term project trace |
| Trace ID | Display of the Trace ID  Using this ID, you can distinguish, for example, between several active long-term project traces. |

### Trace task card

The displayed panes are described in the section [Trace task card](#trace-task-card).

## Operation

This section contains information on the following topics:

- [Quick start](#quick-start)
- [Recording](#recording)
- [Analyzing](#analyzing)

### Quick start

This section contains information on the following topics:

- [Trace quick start](#trace-quick-start)
- [Quick Start for long-term trace (S7-1500)](#quick-start-for-long-term-trace-s7-1500)
- [Project trace quick start](#project-trace-quick-start)
- [Quick access to the long-term project trace](#quick-access-to-the-long-term-project-trace)

#### Trace quick start

This description shows the steps for a recording of the S7-1500 CPU as an example. The displayed settings can differ depending on the device.

##### Requirement

A device is configured that supports the trace and logic analyzer function.

##### Creating a trace

The following figure shows the project tree with the ![Creating a trace](images/171753628939_DV_resource.Stream@PNG-de-DE.png) "Traces" system folder below the device:

![Creating a trace](images/171759047691_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Double-click the "Add new trace" entry.

   A new trace configuration ![Creating a trace](images/171754347403_DV_resource.Stream@PNG-de-DE.png) is created and the "Configuration" tab opens in the working area.
2. Adapt the name of the trace configuration by clicking the text.

##### Selecting signals

The following figure shows the configuration of the signals:

![Selecting signals](images/171759052299_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Select the signals to be recorded in the "Signals" area.

   Or:
2. Drag one or more signals, e.g. from a tag table, and drop them in the signal table.

##### Configuring the recording cycle

The following figure shows the configuration of the sampling:

![Configuring the recording cycle](images/171759056907_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Under "Sampling", configure the recording conditions for the measurement.

##### Configuring the trigger

The following figure shows the configuration of the trigger:

![Configuring the trigger](images/171759074315_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Configure the trigger mode and the condition for the selected trigger.

##### Configuring display options (optional)

The following figure shows the configuration of the display options:

![Configuring display options (optional)](images/171759083531_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Switch to the "Time diagram" tab.
2. Set the desired display options in the curve diagram and in the signal table.

##### Transferring the trace configuration to the device

Procedure:

1. Transfer the trace configuration to the device with the ![Transferring the trace configuration to the device](images/171754781195_DV_resource.Stream@PNG-de-DE.png) button.

   The following functions are executed:

   - An online connection is established to the device.
   - The trace configuration is transferred to the device.
   - The monitoring is activated.
   - The display switches to the "Time diagram" tab.

##### Activating a recording

Procedure:

1. Click ![Activating a recording](images/171754840331_DV_resource.Stream@PNG-de-DE.png).

##### Displaying the recording

The following figure shows the curve diagram with a recording:

![Displaying the recording](images/171759078923_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Wait until the "Recording" or "Recording completed" status is displayed in the status display of the trace.
2. Switch to the "Time diagram" tab.
3. Click the ![Displaying the recording](images/171755292939_DV_resource.Stream@PNG-de-DE.png) icon of a signal in the signal table.

   The individual bits of the signal are offered for display as a bit track.
4. In the signal table, select or deselect the individual signals and bits for display with the ![Displaying the recording](images/171756061707_DV_resource.Stream@PNG-de-DE.png) icon.

##### Saving the measurement in the project

Procedure:

1. Transfer the measurement to the project with the ![Saving the measurement in the project](images/171754848267_DV_resource.Stream@PNG-de-DE.png) button.

   The measurement is displayed in the project tree under the ![Saving the measurement in the project](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Measurements" system folder.

---

**See also**

[User interface - trace toolbar](#user-interface---trace-toolbar)

#### Quick Start for long-term trace (S7-1500)

This description shows the steps for a long-term trace recording of the S7-1500 CPU as an example. The displayed settings can differ depending on the device.

##### Requirement

A device that supports the long-term trace function is created in the TIA Portal project.

##### Creating a long-term trace

The following figure shows the project tree with the ![Creating a long-term trace](images/67314995979_DV_resource.Stream@PNG-de-DE.png) "Traces" system folder below the device:

![Creating a long-term trace](images/171759100939_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Double-click the "Add new long-term trace" entry.

   A new long-term trace configuration ![Creating a long-term trace](images/171754726923_DV_resource.Stream@PNG-de-DE.png) is created and the "Configuration" tab opens in the workspace.
2. Adapt the name of the trace configuration by clicking the text.

##### Selecting signals

The following figure shows the configuration of the signals:

![Selecting signals](images/171759104907_DV_resource.Stream@PNG-en-US.png)

##### Configuring the recording cycle

The following figure shows the configuration of the sampling:

![Configuring the recording cycle](images/171759108875_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Under "Sampling", configure the recording conditions for the measurement.

##### Configuring the target path

The default target path is the folder of the STEP 7 project.

The following figure shows the configuration of the target path:

![Configuring the target path](images/171741469579_DV_resource.Stream@PNG-en-US.png)

##### Transferring the trace configuration to the device

Procedure:

1. Transfer the trace configuration to the device with the ![Transferring the trace configuration to the device](images/88138288395_DV_resource.Stream@PNG-de-DE.png) button.

   The following functions are executed:

   - An online connection is established to the device.
   - The trace configuration is transferred to the device.
   - The monitoring is activated.
   - The display switches to the "Time diagram" tab.

The trace configuration is saved in the target path as an .lttcd file.

##### Activating recording

Procedure:

1. Click the ![Activating recording](images/88138500875_DV_resource.Stream@PNG-de-DE.png) button.

The "Recording in progress" status is displayed.

The recording is saved in the target path as a .csv file.

> **Note**
>
> Note that problems with online access between the PG and the CPU can result in errors or even failure of the recording.
>
> If possible, connect the PG directly to the CPU.

You can also find more information about long-term trace recording as a csv file in the section[Long-term trace recording](S7-1200-1500%20CPUs%20%28S7-1200%2C%20S7-1500%29.md#long-term-trace-recording-s7-1500).

##### Deactivating recording

Procedure:

1. Click ![Deactivating recording](images/171754844299_DV_resource.Stream@PNG-de-DE.png).

The "Stopped" status is displayed.

##### Displaying the recording

The recording from the long-term trace is displayed in the time diagram.

![Displaying the recording](images/171759125643_DV_resource.Stream@PNG-en-US.png)

##### Saving the long-term trace measurement in the project

Procedure:

1. Transfer the measurement to the project with the ![Saving the long-term trace measurement in the project](images/88138508555_DV_resource.Stream@PNG-de-DE.png) button.

The long-term trace measurement is displayed in the project tree under the ![Saving the long-term trace measurement in the project](images/67316550283_DV_resource.Stream@PNG-de-DE.png) "Measurements" system folder.

##### Add to combined long-term trace measurement

To create a combined long-term trace measurement based on the long-term trace measurement, proceed as follows:

1. In the ![Add to combined long-term trace measurement](images/67316550283_DV_resource.Stream@PNG-de-DE.png) "Measurements" system folder, select the long-term trace measurement.
2. Use drag-and-drop to move the long-term trace measurement (![Add to combined long-term trace measurement](images/171754631179_DV_resource.Stream@PNG-de-DE.png)) to the system folder ![Add to combined long-term trace measurement](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Combined measurements".

The combined long-term trace measurement (![Add to combined long-term trace measurement](images/171754042251_DV_resource.Stream@PNG-de-DE.png)) is displayed in the system folder.

To add another long-term trace measurement to an existing combined long-term trace measurement, proceed as follows:

1. In the![Add to combined long-term trace measurement](images/67316550283_DV_resource.Stream@PNG-de-DE.png) "Measurements" system folder, select the long-term trace measurement.
2. Use drag-and-drop to move the long-term trace measurement (![Add to combined long-term trace measurement](images/171754631179_DV_resource.Stream@PNG-de-DE.png)) to the combined long-term trace measurement (![Add to combined long-term trace measurement](images/171754042251_DV_resource.Stream@PNG-de-DE.png)).

#### Project trace quick start

This description shows an example of the steps for a recording with project trace for two S7-1500 CPUs. The displayed settings can differ depending on the device.

##### Requirements

- Two S7-1500 CPUs with firmware version V2.8 or higher are configured.
- The [general requirements for the project trace](#general) are fulfilled.

##### Add project trace

The following figure shows the project tree with the ![Add project trace](images/171755772555_DV_resource.Stream@PNG-de-DE.png) "Project traces" system folder below the cross-device functions:

![Add project trace](images/171759129611_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Double-click the "Add new project trace" entry.

   A new project trace configuration ![Add project trace](images/171755776523_DV_resource.Stream@PNG-de-DE.png) is created and the "Configuration" tab opens in the working area.
2. Adapt the name of the project trace configuration by clicking the text.

##### Adding devices

The following figure shows the adding of the devices.

![Adding devices](images/171759134219_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Select the devices in the "Participating devices" area.

##### Configuring signals and recording conditions of devices

The following figure shows two participating devices and the configuration of "PLC_1".

![Configuring signals and recording conditions of devices](images/171759151627_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Select a device in the "Participating devices" area.
2. Select the "Properties" tab in the Inspector window.
3. Select the signals to be recorded in the "Signals" area.

   Or:
4. Drag one or more signals, e.g. from a tag table, and drop them in the signal table.
5. Configure the sampling.
6. Configure the trigger mode and the condition for the selected trigger.
7. Redo the configuration from step 1 for each participating device.

For "PLC_2", "Trigger from another Device" is configured as trigger mode in the example shown here.

##### Apply trace configurations to the devices

Procedure:

1. Open the status overview of the participating devices using the ![Apply trace configurations to the devices](images/171755848459_DV_resource.Stream@PNG-de-DE.png) button.
2. Transferring the trace configurations to the devices using the ![Apply trace configurations to the devices](images/171754781195_DV_resource.Stream@PNG-de-DE.png) button.
3. Check the status in [Status overview](#user-interface---status-overview-of-the-participating-devices) and correct any errors that have occurred.

##### Activate recording

Procedure:

1. Click ![Activate recording](images/171754840331_DV_resource.Stream@PNG-de-DE.png).

##### Displaying recordings

Procedure:

1. In the status overview of the participating devices, check whether the required recordings have already been completed.
2. Switch to the "Time diagram" tab.

##### Saving measurements in the project

Procedure:

1. Transfer the measurements to the project using the ![Saving measurements in the project](images/171754848267_DV_resource.Stream@PNG-de-DE.png) button.

   The measurements are displayed in the project tree under the system folder ![Saving measurements in the project](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Measurements".

#### Quick access to the long-term project trace

This description shows an example of the steps for a recording with long-term project trace for two S7-1500 CPUs. The displayed settings can differ depending on the device.

##### Requirements

- Two S7-1500 CPUs with firmware version V2.8 or higher are configured.
- The [general requirements](#general-1) for the long-term project trace are fulfilled.

> **Note**
>
> In read-only mode, the long-term project trace option is disabled or can only be used with restrictions.

##### Add long-term project trace

The following figure shows the project tree with the ![Add long-term project trace](images/166846142347_DV_resource.Stream@PNG-de-DE.png) "Long-term project traces" system folder below the cross-device functions:

![Add long-term project trace](images/172446696715_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Double-click on the "Add new long-term project trace" entry.

   A new long-term project trace configuration is created and the "Configuration" tab opens in the workspace.
2. Adapt the name of the long-term project trace configuration by clicking the text.

##### Adding devices

The following figure shows the adding of the devices.

![Adding devices](images/172446323979_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Select the devices under the "Participating devices".

##### Configuring signals and recording conditions of devices

The following figure shows two participating devices and the configuration of "PLC_1".

![Configuring signals and recording conditions of devices](images/172445452939_DV_resource.Stream@PNG-en-US.png)

Procedure:

1. Select a device in the "Participating devices" area.
2. Select the "Properties" tab in the Inspector window.
3. Select the recording conditions in the "Signals" area.

   Or:
4. Drag one or more signals, e.g. from a tag table, and drop them in the signal table.
5. Configure the recording conditions.
6. Redo the configuration from step 1 for each participating device.

##### Apply trace configurations to the devices

Procedure:  
1 Open the status overview of the participating devices using the ![Apply trace configurations to the devices](images/171755848459_DV_resource.Stream@PNG-de-DE.png) button.  
2. Transferring the trace configurations to the devices using the ![Apply trace configurations to the devices](images/171754781195_DV_resource.Stream@PNG-de-DE.png) button  
3. Check the status in [Status overview](#user-interface---status-overview-of-the-participating-devices-1) and correct any errors that have occurred.

##### Activating recording

Procedure:

1. Click the ![Activating recording](images/171754840331_DV_resource.Stream@PNG-de-DE.png) button.

##### Displaying the recording

Procedure:

1. Switch to the "Time diagram" tab.

##### Saving measurements in the project

Procedure:

1. Transfer the measurements to the project using the ![Saving measurements in the project](images/171754848267_DV_resource.Stream@PNG-de-DE.png) button.

   The measurements are displayed in the project tree under the system folder ![Saving measurements in the project](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Measurements".

### Recording

This section contains information on the following topics:

- [Activating/deactivating an installed trace](#activatingdeactivating-an-installed-trace)
- [Transferring the trace configuration from the device to the project](#transferring-the-trace-configuration-from-the-device-to-the-project)
- [Saving measurements in the project](#saving-measurements-in-the-project)
- [Automatic repetition of measurements](#automatic-repetition-of-measurements)

#### Activating/deactivating an installed trace

##### Requirement

- There is an online connection to the device.
- There is a trace in the device.
- The trace in the device is displayed in the working area.
- The ![Requirement](images/171754627211_DV_resource.Stream@PNG-de-DE.png) button is activated for viewing the displayed trace.

##### Activating an installed trace

To activate the recording for an installed trace, proceed as follows:

1. Click ![Activating an installed trace](images/171754840331_DV_resource.Stream@PNG-de-DE.png).

   The installed trace is activated and starts the recording according to the configured trigger condition. The trigger condition is device-specific and described in Section "Configuration" below the respective [device](#devices).

   The current status of the recording is displayed in the status display of the trace.

**Note**

When a recording is restarted, the previously recorded values are lost.

To save the recorded values, [save the measurement in the project](#saving-measurements-in-the-project) before you activate the recording again.

##### Deactivating an installed trace

To deactivate an activated installed trace, proceed as follows:

1. Click ![Deactivating an installed trace](images/171754844299_DV_resource.Stream@PNG-de-DE.png).

   The installed trace is deactivated.

   The status display of the trace changes to "Inactive".

---

**See also**

[User interface - trace toolbar](#user-interface---trace-toolbar)

#### Transferring the trace configuration from the device to the project

##### Requirement

- There is an online connection to the device.
- There is a trace in the device.

##### Procedure

To transfer a trace configuration to the project, proceed as follows:

1. Open a trace in the device.
2. If required, activate the ![Procedure](images/171754627211_DV_resource.Stream@PNG-de-DE.png) button for viewing.
3. Click ![Procedure](images/171754836363_DV_resource.Stream@PNG-de-DE.png) to transfer the trace configuration from the device.

##### Result

The configuration is taken over as new trace configuration in the ![Result](images/171753628939_DV_resource.Stream@PNG-de-DE.png) "Traces" system folder.

The current display options are included in the new trace configuration.

A trace configuration of the same name is overwritten in the system folder.

---

**See also**

[User interface - trace toolbar](#user-interface---trace-toolbar)

#### Saving measurements in the project

##### Requirement

- There is an online connection to the device.
- There is a trace with recording in the device.
- The installed trace data must have been displayed at least once in the curve diagram. The recording data is loaded from the device for the display.

##### Procedure

To save a recording in the project, proceed as follows:

1. Open the trace in the device with the recorded data.
2. If required, make sure that the current data is loaded from the device by activating the ![Procedure](images/171754627211_DV_resource.Stream@PNG-de-DE.png) button.
3. After activating the ![Procedure](images/171754627211_DV_resource.Stream@PNG-de-DE.png) button wait until all data has been loaded and displayed.
4. Click ![Procedure](images/171754848267_DV_resource.Stream@PNG-de-DE.png).

   The measurement is added to the ![Procedure](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Measurements" system folder.
5. Save the project in the TIA Portal.

---

**See also**

[User interface - trace toolbar](#user-interface---trace-toolbar)

#### Automatic repetition of measurements

The recording is automatically re-activated at the end of each recording. The display in the curve is similar to the display of an oscilloscope.

##### Requirements

- There is an online connection to the device.
- There is a trace in the device.

##### Procedure

To monitor the progress of a fast signal, proceed as follows:

1. Select a trace in the device.
2. Double-click the selected trace.
3. Click ![Procedure](images/171754627211_DV_resource.Stream@PNG-de-DE.png) for monitoring.
4. Click ![Procedure](images/171756273163_DV_resource.Stream@PNG-de-DE.png) to automatically repeat the recording.

### Analyzing

This section contains information on the following topics:

- [Analyzing a specific time range of an ongoing recording](#analyzing-a-specific-time-range-of-an-ongoing-recording)
- [Use of the curve diagram](#use-of-the-curve-diagram)
- [Use of the signal table](#use-of-the-signal-table)
- [Using the signal group in the signal table](#using-the-signal-group-in-the-signal-table)
- [Comparing recordings (combined measurement)](#comparing-recordings-combined-measurement)
- [Printing a recording](#printing-a-recording)

#### Analyzing a specific time range of an ongoing recording

A measurement of a trace in the device can be generated at any time.

Use this functionality, for example, to save the data recorded up until this point in a recording and to analyze it as a static measurement.

##### Requirements

- An ongoing recording is displayed in the "Time diagram" tab.

##### Procedure

To analyze a certain time range for an ongoing recording, follow these steps:

1. Click ![Procedure](images/88138508555_DV_resource.Stream@PNG-de-DE.png).

   The data recorded up to now is added to the measurements.  
   The current recording is not affected by this and continues running uninterrupted.

#### Use of the curve diagram

The curve diagram shows the signals of a recording selected in the signal table.

The display area can be zoomed as required. Measurement cursors can be used to select individual values for display in the signal table.

The following operating instructions describe the use of the curve diagram and of the measurement cursors as examples.

##### Requirements

- An installed trace or a measurement has been selected for display.
- The ![Requirements](images/171754627211_DV_resource.Stream@PNG-de-DE.png) button is activated to monitor an installed trace.
- The "Time diagram" tab is open in the working area.

##### Monitor an ongoing recording.

To display all of the data in an ongoing recording, proceed as follows:

1. Activate "Display all" via the ![Monitor an ongoing recording.](images/171755013387_DV_resource.Stream@PNG-de-DE.png) button.

The entire time range and all values for the ongoing recording are displayed.

To display a consistent time window in an ongoing recording, proceed as follows:

1. Activate "Display all" via the ![Monitor an ongoing recording.](images/171755013387_DV_resource.Stream@PNG-de-DE.png) button.
2. Select the desired time range via the ![Monitor an ongoing recording.](images/171754991883_DV_resource.Stream@PNG-de-DE.png) button.

The trend view is updated while the scaling of the time range remains the same.

> **Note**
>
> A measurement of a trace in the device can be generated at any time. In this way, you can analyze the data recorded until that point as static measurement.

##### Evaluation of a certain instant of a recording

To display the values for a specific sample, proceed as follows:

1. Display the vertical measurement cursors via the ![Evaluation of a certain instant of a recording](images/171754999051_DV_resource.Stream@PNG-de-DE.png) button.
2. Move a measurement cursor with the mouse to the required position in the recording.

   The values of the signals are displayed in the signal table and in the "Measurement cursor" pane of the "Trace" task card.

##### Evaluation of the difference between two samples

To display the difference, proceed as follows:

1. Display the vertical measurement cursors via the ![Evaluation of the difference between two samples](images/171754999051_DV_resource.Stream@PNG-de-DE.png) button.
2. Move both measurement cursors with the mouse to the required samples in the recording.

   The values of the signals and the difference are displayed in the signal table and in the "Measurement cursor" pane of the "Trace" task card.

##### Using horizontal measurement cursors

To check whether a certain value has been reached, proceed as follows:

1. Display the horizontal measurement cursors via the ![Using horizontal measurement cursors](images/171755002635_DV_resource.Stream@PNG-de-DE.png) button.
2. Move a measurement cursor with the mouse to the required value of the recording.

   The values of the measurement cursors for the selected signal are displayed in the "Measurement cursor" pane of the "Trace" task card.

##### Moving the time range displayed

Proceed as follows to move the time range displayed:

1. Select a time range via the ![Moving the time range displayed](images/171754991883_DV_resource.Stream@PNG-de-DE.png) button.
2. Move the curve to the desired time range by turning the mouse wheel with the &lt;Shift&gt; key pressed down.

##### Bringing a signal into the foreground

1. Display the legend via the ![Bringing a signal into the foreground](images/171755055371_DV_resource.Stream@PNG-de-DE.png) button.
2. Click a signal in the legend.

Or:

1. Click a signal in the curve diagram.

The signal is displayed in the foreground and is highlighted/selected in the signal table. The value axis is updated for the selected signal.

---

**See also**

[User interface - curve diagram](#user-interface---curve-diagram)
  
[User interface - signal table](#user-interface---signal-table)

#### Use of the signal table

The signal table shows the signals of an installed trace or a measurement. The preselected signals in the signal selection are displayed with a combined measurement. You can show or hide individual signals for the display in the table and adapt the properties for the display.   
Individual bits can be selected for some data types and displayed as a bit track.

The following operating instructions describe the operation of the signal table.

##### Requirements

- An installed trace or a measurement has been opened in the "Time diagram" tab.
- The ![Requirements](images/171754627211_DV_resource.Stream@PNG-de-DE.png) button is activated to monitor an installed trace.
- For the display of individual bits as a bit track:  
  at least one recorded signal supports the display as a bit track.

##### Display or hide individual signals and change the color

To adapt the display to suit your requirements, proceed as follows:

1. Click the icon of the respective signal in the ![Display or hide individual signals and change the color](images/171756277131_DV_resource.Stream@PNG-de-DE.png) column to select or deselect it for the display.
2. Click in the "Color" column for the respective signal and select a color.

   The default color for the signal changes.

##### Bringing a signal into the foreground

1. In the signal table, select the line of the signal.

   The Y-scale of the signal is displayed.

   The signal curve is brought into the foreground in the curve diagram.

##### Selecting individual bits for display as a bit track

To display individual bits as a bit track in the lower curve diagram, proceed as follows:

1. Click the ![Selecting individual bits for display as a bit track](images/171755292939_DV_resource.Stream@PNG-de-DE.png) icon of a signal in the signal table.
2. Click the ![Selecting individual bits for display as a bit track](images/171755285771_DV_resource.Stream@PNG-de-DE.png) icon in the open bit selection of the signal.

   The bits are selected or deselected for display.

---

**See also**

[User interface - curve diagram](#user-interface---curve-diagram)
  
[User interface - signal table](#user-interface---signal-table)

#### Using the signal group in the signal table

Individual signals can be scaled identically in a scaling group, which makes it easier to compare the curve characteristics.

Binary signals cannot be grouped.

The following operating instructions describe how to work with the scaling group.

> **Note**
>
> **Saving scaling groups**
>
> The scaling groups can be saved individually for each measurement via the "Use current view as standard" function (![Figure](images/171754651915_DV_resource.Stream@PNG-de-DE.png) button).
>
> If the scaling groups and the project are not saved, then the scaling groups created will be lost when the "Time diagram" tab is closed.

##### Requirements

- An installed trace or a measurement is displayed.
- The ![Requirements](images/171754627211_DV_resource.Stream@PNG-de-DE.png) button is activated to monitor an installed trace.
- The "Time diagram" tab is open in the working area.
- There are at least two signals in the signal table that are not of the BOOL type.

##### Assigning signals to a scaling group

To apply a scaling group and assign signals to this group, proceed as follows:

1. In the signal table, select the line or cell of the required signal.
2. Click the gray field in the "Scaling group" column.

   The sequence icon is displayed in the gray field and the name of the scaling group is pre-assigned: ![Assigning signals to a scaling group](images/171756280715_DV_resource.Stream@PNG-de-DE.png)
3. Click the gray fields of further signals that are to be assigned to this scaling group.

Or:

1. Click in the text field of the "Scaling group" column for a signal to be grouped.
2. Enter a name for the group.
3. Enter the same group name in the respective text fields for further signals or select the group name via the drop-down list.

The Y-scales of the grouped signals are scaled with the values of the signal that was selected first. Changes to a scale value always affect the entire group.

##### Removing signals from a scaling group

To delete the assignment of a signal to a scaling group, proceed as follows:

1. Click the ![Removing signals from a scaling group](images/171755334411_DV_resource.Stream@PNG-de-DE.png) sequence icon for the required signal in the "Scaling group" column.

Or:

1. Click the text field for the required signal in the "Scaling group" column.
2. Press the &lt;Del&gt; key.

Or:

1. Select the respective text field in the "Scaling group" column for several signals using the &lt;Shift&gt; and &lt;Ctrl&gt; keys.
2. Press the &lt;Del&gt; key.

The signals are removed from the scaling group or the scaling group is deleted.

---

**See also**

[User interface - signal table](#user-interface---signal-table)

#### Comparing recordings (combined measurement)

This section contains information on the following topics:

- [Apply combined measurement](#apply-combined-measurement)
- [Comparing recordings](#comparing-recordings)
- [Aligning measurements with measurement cursor](#aligning-measurements-with-measurement-cursor)

##### Apply combined measurement

Combined measurements can be applied in the project tree with a comparison function for different measurements.

The following instructions describe how you can create a combined measurement under the ![Figure](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Combined measurements" system folder

###### Requirement

A device is configured that supports the trace and logic analyzer function.

###### Procedure

To apply an combined measurement, proceed as follows:

1. Select one or more measurements in the ![Procedure](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Measurements" system folder.
2. Drag the measurements to the ![Procedure](images/171754676619_DV_resource.Stream@PNG-de-DE.png) "Combined measurements" system folder.

A new combined measurement is created. This contains copies of the selected measurements.

##### Comparing recordings

###### Requirement

- An combined measurement is created or is created implicitly by dragging the measurements to the system folder ![Requirement](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Combined measurements".

  See also [Apply combined measurement](#apply-combined-measurement).

###### Adding measurements for comparison

To compare measurements, insert the measurements to be compared to the combined measurements. Proceed as follows for this:

1. In the project tree drag one or more measurements from the system folder ![Adding measurements for comparison](images/171754647947_DV_resource.Stream@PNG-de-DE.png) "Measurements" to the icon for the ![Adding measurements for comparison](images/171754631179_DV_resource.Stream@PNG-de-DE.png) combined measurement ![Adding measurements for comparison](images/171754042251_DV_resource.Stream@PNG-de-DE.png).

Or:

1. Import saved measurements via the "Import measurement" shortcut menu command.

A copy of the measurements is added to the combined measurement.

###### Select signals of the measurements for the signal table

Proceed as follows to select the signals for the signal table in the "Time diagram" tab:

1. Double-click on the icon for the combined measurement ![Select signals of the measurements for the signal table](images/171754042251_DV_resource.Stream@PNG-de-DE.png) in the project tree.

   The tabs for the combined measurement will be displayed in the working area.
2. Click the "Signal selection" tab in the working area.

   The signals for all measurements are displayed in the table.
3. Activate or deactivate the signal check box for those signals that should be visible or should not be visible in the signal table.

The activated signals are displayed in the signal table of the "Time diagram" tab.

###### Use of the signal table

Proceed as follows to open and use the signal tables:

1. Click the "Time diagram" tab in the working area.
2. Click on the "Signals" tab within the "Time diagram" tab.
3. Use the signal tables as described under [Use of the signal table](#use-of-the-signal-table).

###### Align measurements

Proceed as follows to align the time axis for the measurements for the comparison:

1. Click on the "Measurements" tab within the "Time diagram" tab.
2. Select the alignment for the measurements via the check box.
3. Adjust the alignment and if necessary set an offset for the alignment of the individual measurements.

The measurements are aligned with each other accordingly on the time axis.

(The alignment of measurements with the measurement cursor is described in [Aligning measurements with measurement cursor](#aligning-measurements-with-measurement-cursor).)

###### Use of the curve diagram

Proceed as follows to open and use the curve diagram:

1. Click the "Time diagram" tab in the working area.
2. Use the curve diagram as described under [Use of the curve diagram](#use-of-the-curve-diagram).

##### Aligning measurements with measurement cursor

###### Requirement

- An combined measurement is applied.
- Measurements for comparison are added to the combined measurement.
- Signals of the measurements for the signal table are selected.
- The "Time diagram" tab for the combined measurement opens in the working area.

###### Aligning measurements to measured position difference Δt

Proceed as follows to align the time axis of two measurements:

1. Display the vertical measurement cursors via the ![Aligning measurements to measured position difference Δt](images/171754999051_DV_resource.Stream@PNG-de-DE.png) button.
2. Zoom into the time range, e.g. with the ![Aligning measurements to measured position difference Δt](images/171754991883_DV_resource.Stream@PNG-de-DE.png) button until you are able to position the first measurement cursor precisely on the desired reference point for the first measurement.
3. Move the first measurement cursor with the mouse to the required position.
4. Search for the reference point for the second measurement, e.g. by switching to "Display all" with the ![Aligning measurements to measured position difference Δt](images/171755013387_DV_resource.Stream@PNG-de-DE.png) button.
5. Zoom into the time range, e.g. with the ![Aligning measurements to measured position difference Δt](images/171754991883_DV_resource.Stream@PNG-de-DE.png) button until you are able to position the second measurement cursor precisely on the desired reference point for the second measurement.
6. Move the second measurement cursor with the mouse to the required position.
7. Open the "Trace" task card.
8. In the "Measurement cursor" pane, select the position difference value Δt.
9. Copy the value to the clipboard.
10. Insert the value from the clipboard into the Offset cell of the first or second measurement.

The two measurements are aligned with each other.

> **Note**
>
> When inserting the position difference as the offset make sure that you also adjust the leading character as necessary.

---

**See also**

[User interface - Measurement cursor pane](#user-interface---measurement-cursor-pane)
  
[Use of the curve diagram](#use-of-the-curve-diagram)

#### Printing a recording

The curve diagram supports the saving of the display as a graphic and the copying of the display to the clipboard. Also use [these functions](#user-interface---curve-diagram) for printing.

## Devices

This section contains information on the following topics:

- [S7-1200/1500 CPUs (S7-1200, S7-1500)](S7-1200-1500%20CPUs%20%28S7-1200%2C%20S7-1500%29.md#s7-12001500-cpus-s7-1200-s7-1500)
- [SINAMICS G120](SINAMICS%20G120.md#sinamics-g120)
- [SINAMICS G220](SINAMICS%20G220.md#sinamics-g220)
- [SINAMICS S120](SINAMICS%20S120.md#sinamics-s120)
- [SINAMICS S200](SINAMICS%20S200.md#sinamics-s200)
- [SINAMICS S210](SINAMICS%20S210.md#sinamics-s210)
- SINAMICS V90 PN

## Glossary

### Combined measurement

Permits a comparison and analysis of signals from different measurements.

 

### Curve diagram

Displays the selected signals of a recording.

 

### Global trigger

If a project trace is triggered by a participating device to start recording synchronously in all participating devices.

 

### Installed trace

Consists of a trace configuration and optionally a recording.

 

### Measurement

Consists of a trace configuration with an associated recording.

 

### Pretrigger

Defines the interval in which the signals are already recorded before the actual trigger condition is fulfilled.

 

### Project trace

Contains all the information to record signals from multiple devices with a global trigger.

 

### Recording

Is performed in the device. There is only one recording for each installed trace configuration.

 

### Recording condition

Sampling and trigger for a trace configuration.

 

### Recording duration

Factor in number of samples. The factor of 100 means, for example, that 100 samples are recorded.

 

### Reduction

Factor in number of cycles. A factor of 2 means, for example, that a recording is made every second cycle.

 

### Sampling

Setting, in which cycle, how fast and how long the recording is to be made.

 

### Signal table

Lists the signals of the selected measurement and provides setting options for some properties.

 

### Snapshot

Contains the settings for the view for a measurement.

 

### Trace configuration

Contains all the information required to record signals in a device.

 

### Trigger

Specifies the trigger mode and the condition for the "Trigger on tag" mode.

 

### Trigger mode

Specifies whether the recording should be started immediately or based on a trigger tag.

 

### Trigger tag

Signal to trigger the recording.

 

### Trigger time

The meaning of the measurement trigger time depends on the device.

e.g. SIMATIC S7-1200/1500 CPUs: Specifies the absolute time of the control system at the start of recording.
