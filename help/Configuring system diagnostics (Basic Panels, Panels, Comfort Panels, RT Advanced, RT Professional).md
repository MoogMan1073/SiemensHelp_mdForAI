---
title: "Configuring system diagnostics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: SysDiagWCCPenUS
topics: 32
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring system diagnostics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [System diagnostics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#system-diagnostics-basic-panels-panels-comfort-panels-rt-advanced)
- [System diagnostics (RT Professional)](#system-diagnostics-rt-professional)

## System diagnostics (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basic Panel basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basic-panel-basics-basic-panels-panels-comfort-panels-rt-advanced)
- [Panels and Runtime Advanced basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#panels-and-runtime-advanced-basics-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring system diagnostics objects (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-system-diagnostics-objects-basic-panels-panels-comfort-panels-rt-advanced)

### Basic Panel basics (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [System diagnostics basics (Basic Panels)](#system-diagnostics-basics-basic-panels)
- [System diagnostics views (Basic Panels)](#system-diagnostics-views-basic-panels)

#### System diagnostics basics (Basic Panels)

##### Introduction

Using system diagnostics, you can display the messages from the diagnostic buffer of all integrated connections.

##### System diagnostics view

The system diagnostics display is an operating and display object that you use in a screen.

You navigate directly to the cause of the error and the associated connection. You have access to all integrated connections that you have configured in the "Devices &amp; networks" editor.

#### System diagnostics views (Basic Panels)

##### Introduction

Three different views are available in the basic System diagnostics view:

- Device view
- Diagnostic buffer view
- Detail view

##### Device view

The device view is only displayed if more than one integrated connection has been configured.

The device view shows all available connections in a table. Double-clicking a connection opens the diagnostic buffer view.

![Device view](images/76421626123_DV_resource.Stream@PNG-de-DE.png)

##### Diagnostic buffer view

The diagnostic buffer view shows the current data from the diagnostic buffer.

To update the diagnostic buffer view, you click ![Diagnostic buffer view](images/40973105547_DV_resource.Stream@PNG-de-DE.png).

![Diagnostic buffer view](images/76421621771_DV_resource.Stream@PNG-en-US.png)

##### Detail view

The detail view gives detailed information about the selected connection and any pending errors. Check whether the data is correct in the detail view.

![Detail view](images/76422252427_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Contents of the detail view**
>
> The contents of the detail view are only available for integrated connections with S7-1200 and S7-1500 controllers.

##### Navigation buttons

| Button | Key | Function |
| --- | --- | --- |
| ![Navigation buttons](images/43725616139_DV_resource.Stream@PNG-de-DE.png) | Enter key | In the device view:  Opens the diagnostic buffer view of the selected device.  In the diagnostic buffer view:  Opens the detail view. |
| ![Navigation buttons](images/43725611531_DV_resource.Stream@PNG-de-DE.png) | Esc key | In the diagnostic buffer view:  Opens the device view.  In the detail view:  Opens the diagnostic buffer view. |
| ![Navigation buttons](images/40973105547_DV_resource.Stream@PNG-de-DE.png) | Configured function key, e.g. F1. | Updates the diagnostic buffer view. |

### Panels and Runtime Advanced basics (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [System diagnostics basics (Panels, Comfort Panels, RT Advanced)](#system-diagnostics-basics-panels-comfort-panels-rt-advanced)
- [System diagnostics views (Panels, Comfort Panels, RT Advanced)](#system-diagnostics-views-panels-comfort-panels-rt-advanced)

#### System diagnostics basics (Panels, Comfort Panels, RT Advanced)

##### Introduction

You use system diagnostics to detect problems and errors in any part of your plant. WinCC has two display and operating elements for quick error localization.

For the controller to be able to transfer error messages to the system diagnostics view or the system diagnostics window, an HMI connection must exist between controller and HMI device. In addition, the system diagnostics must be enabled both in the PLC and on the HMI device.

In a SIMATIC S7-300/400 controller, the system diagnostics is disabled by default but can be enabled in the properties of the controller. In a SIMATIC S7-1200/1500 controller, the system diagnostics is enabled by default and cannot be deactivated.

With an HMI connection to a SIMATIC S7-300/400 controller, the "System diagnostics" option is enabled on the HMI device under "Runtime settings &gt; Alarms &gt; Controller alarms" by default and cannot be disabled. With an HMI connection to a SIMATIC S7-1200/1500 controller, the "System diagnostics" option is enabled by default on the HMI device under "Runtime settings &gt; Alarms &gt; Controller alarms" and cannot be disabled.

##### System diagnostics view

The alarm view shows the status of a PLC while the system diagnostics view gives you an overview of all devices available in your plant: You navigate directly to the cause of the error and to the relevant device. You have access to all diagnostics-capable devices which you have configured in the "Devices &amp; networks" editor.

##### System diagnostics window

The system diagnostics window is an operating and display element that you can only use in the global screen.

The functions of the system diagnostics window are no different than those of the system diagnostics view. Because the system diagnostics window is configured in the global screen, you can, for example, also specify if the object is closable in Runtime.

> **Note**
>
> **System diagnostics on Basic Panels**
>
> The "System diagnostics window" object is not available on Basic Panels.

#### System diagnostics views (Panels, Comfort Panels, RT Advanced)

##### Introduction

There are four different views available in the system diagnostics view and the system diagnostics window:

- Device view
- Diagnostic buffer view
- Detail view
- Matrix view (for master systems, PROFIBUS, PROFINET only)

##### Device view

The device view shows all the available devices of a layer in a table. Double-clicking on a device opens either the child devices or the detail view. Symbols in the first column provide information about the current status of the device.

![Device view](images/76412792587_DV_resource.Stream@PNG-en-US.png)

##### Diagnostic buffer view

In the diagnostic buffer view, the current data from the diagnostic buffer of the device is displayed. The diagnostic buffer view can only be called up in the device view.

To update the diagnostic buffer view, you click ![Diagnostic buffer view](images/76412508811_DV_resource.Stream@PNG-de-DE.png).

![Diagnostic buffer view](images/76412584843_DV_resource.Stream@PNG-en-US.png)

##### Detail view

The detail view gives detailed information about the selected device and the pending errors. Check whether the data is correct in the detail view. You cannot sort error texts in the detail view.

![Detail view](images/76414010891_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Contents of the detail view**
>
> The contents of the detail view are only available for integrated connections with S7-1200 and S7-1500 controllers.

##### Distributed I/O view

The distributed I/O view is available for master systems and IO systems. In this view, you can see the status of the subdevices of the system. Each element in the view shows the device name, the device type and the IP address or the PROFIBUS address.

![Distributed I/O view](images/76414124299_DV_resource.Stream@PNG-de-DE.png)

In the case of a fault, the affected element is visually highlighted:

- Red border indicates a fault in a lower-level element.
- Red background indicates a fault in the element itself, for example, the device is not available.

##### Navigation buttons

| Button | Key | Function |
| --- | --- | --- |
| ![Navigation buttons](images/76411547531_DV_resource.Stream@PNG-de-DE.png) | Enter key | Opens the child devices or the detail view if there are no child devices. |
| ![Navigation buttons](images/76412429707_DV_resource.Stream@PNG-de-DE.png) | Esc key | Opens the parent device or the device view if there is no parent device. |
| ![Navigation buttons](images/76411543691_DV_resource.Stream@PNG-de-DE.png) | Home key | Opens the device view. |
| ![Navigation buttons](images/76412501515_DV_resource.Stream@PNG-de-DE.png) | Configured function key, e.g. F1. | Opens the diagnostic buffer view.  Only visible in the device view. |
| ![Navigation buttons](images/76412508811_DV_resource.Stream@PNG-de-DE.png) | Configured function key, e.g. F2. | Updates the diagnostic buffer view. |

> **Note**
>
> **Navigation in the matrix view of Comfort Panels with function keys**
>
> The Shift key is additionally used to select PNIO or PROFIBUS slaves in the matrix view.

##### Language switching in runtime

Switch over the language in runtime before you open the details view.

If you switch over the runtime language while the details view is opened, you change back to the diagnostic buffer view.

Open the details view again. The selected runtime language is now displayed correctly.

### Configuring system diagnostics objects (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Activating system diagnostics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#activating-system-diagnostics-basic-panels-panels-comfort-panels-rt-advanced)
- [Adding a system diagnostics indicator (Panels, Comfort Panels, RT Advanced)](#adding-a-system-diagnostics-indicator-panels-comfort-panels-rt-advanced)
- [Configuring a system diagnostics window in the global screen (Panels, Comfort Panels, RT Advanced)](#configuring-a-system-diagnostics-window-in-the-global-screen-panels-comfort-panels-rt-advanced)
- [Configuring button as system diagnostics indicator (Panels, Comfort Panels, RT Advanced)](#configuring-button-as-system-diagnostics-indicator-panels-comfort-panels-rt-advanced)
- [Configuring the system diagnostic view (Panels, Comfort Panels, RT Advanced)](#configuring-the-system-diagnostic-view-panels-comfort-panels-rt-advanced)
- [Configuring the system diagnostic view (Basic Panels)](#configuring-the-system-diagnostic-view-basic-panels)
- [Splitting the view in system diagnostics view (Panels, Comfort Panels, RT Advanced)](#splitting-the-view-in-system-diagnostics-view-panels-comfort-panels-rt-advanced)

#### Activating system diagnostics (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

An HMI connection must exist between controller and the HMI device so that the controller can send error messages to the system diagnostics view. In addition, the system diagnostics must be enabled both in the PLC and on the HMI device.

In a SIMATIC S7-300/400 controller, the system diagnostics is disabled by default but can be enabled. In a SIMATIC S7-1200/1500 controller, the system diagnostics is enabled by default and cannot be deactivated.

With an HMI connection to a SIMATIC S7-300/400 controller, the system diagnostics on the HMI device is activated by default and cannot be deactivated. With an HMI connection to a SIMATIC S7-1200/1500 controller, the system diagnostics on the HMI device can be activated and deactivated by default.

The following describes how to activate system diagnostics in a controller on an HMI device, if necessary.

##### Requirement

- There is an HMI connection between controller and HMI device.

##### Activating system diagnostics in the controller

To activate the system diagnostics in a controller, proceed as follows:

1. Open the "Device configuration" of the controller in the project tree.
2. In the "Device view" tab, select the CPU on the rack.
3. Select "Properties &gt; General &gt; System diagnostics" in the Inspector window.
4. Activate the option "Activate system diagnostics for this device".
5. Right-click the controller in the project tree and select "Compile &gt; Hardware (rebuild all)" in the shortcut menu.

##### Activating system diagnostics on the HMI device

To activate the system diagnostics on an HMI device, proceed as follows:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Select the option "System diagnostics" under "Alarms &gt; Controller alarms".

   The display of system diagnostic alarms is enabled in runtime.

> **Note**
>
> **Special feature system diagnostic alarms SIMATIC S7-300/400**
>
> When you deactivate the display class 0 for the respective HMI connection under "Runtime settings &gt; Alarms &gt; Controller alarms &gt; Display classes", the system diagnostic alarms are not transferred to the HMI device by the controller even when the system diagnostics is activated in the controller and on the HMI device.

#### Adding a system diagnostics indicator (Panels, Comfort Panels, RT Advanced)

##### Introduction

The system diagnostics indicator is a predefined graphic symbol of the library which alerts you to errors in your system.

If an error occurs, the appearance of the object changes. The library object can display two states:

- No error

- Error

##### Requirement

- The "Libraries" task card is opened.
- The global library "Buttons and Switches &gt; Master copies &gt; DiagnosticsButtons" is open.
- A screen is open.
- A system diagnostics window has been created in the global screen.

##### Procedure

1. Select the "DiagnosticsIndicator" object in the library.
2. Drag-and-drop the library object to the position in the work area where you want to insert the object.

   The library object is inserted.

   ![Procedure](images/97212885003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97212885003_DV_resource.Stream@PNG-en-US.png)
3. Select the library object.
4. Click "Properties &gt; Events" in the Inspector window.

   The system function "ShowSystemDiagnosticsWindow" is preset for the event "Click".

**Note**

**System diagnostics indicator for different device types**

When selecting the object ensure that you use the correct object for the device type used in the project.

##### Result

The status diagnostics indicator has been added to the project and connected with the system diagnostics window.

The system diagnostics indicator changes its appearance if an error message is output in Runtime. The system diagnostics window opens when you click on the system diagnostics indicator. The system diagnostics window shows the detail view of the affected device.

##### Configuring access protection for the system diagnostics window

Configure access protection for the system diagnostics indicator to prevent unauthorized access to the system diagnostics window.

1. Select the "DiagnosticsIndicator" object in the screen.
2. Select an authorization in "Properties &gt; Properties &gt; Security in Runtime" in the Inspector window.

A logon dialog opens when you click on the system diagnostics indicator in Runtime. The system diagnostics window does not open unless you have the required authorization.

#### Configuring a system diagnostics window in the global screen (Panels, Comfort Panels, RT Advanced)

##### Introduction

The system diagnostics window gives you an overview of all devices available in your plant. The system diagnostics window operates like the system diagnostics view, but it is only available in the global screen.

##### Requirements

- At least one PLC has been created.
- A Comfort Panel or WinCC RT Advanced has been created.
- System diagnostics is enabled in every controller and on the HMI device .
- The global screen is open.
- The Inspector window is open.

##### Procedure

1. Double-click the "System diagnostics window" object in the "Tools" task card. The object is added to the global screen.
2. Select "Properties &gt; Properties &gt; Columns &gt; Devices/Detail view" in the Inspector window.
3. Activate the columns that you require in the device view for Runtime, e.g. Status, Name, Address.
4. Activate the properties that you require in the Detail view for Runtime, e.g. status, name, higher level designation.
5. Activate the columns that you require in the diagnostic buffer view, e.g. Status, Name.
6. Customize the column headers, if necessary.
7. Enable "Properties &gt;Properties &gt; Layout &gt; Column settings &gt; Columns moveable" to move the columns in Runtime.
8. Enable "Properties &gt; Properties &gt; Window &gt; Closable" to allow the system diagnostics window to be closed in Runtime.

##### Result

The system diagnostics window has been added to the global screen. The system diagnostics window will respond to error messages in the plant and display the device affected.

Configure a system diagnostics indicator in a screen to open the system diagnostics window.

#### Configuring button as system diagnostics indicator (Panels, Comfort Panels, RT Advanced)

##### Introduction

Instead of using the object "DiagnosticsIndicator" from the library, you can configure a button, for example, to indicate errors in your plant.

##### Requirements

- At least one PLC has been created.
- System diagnostics is enabled in every controller and on the HMI device .
- The "Tools" task card is open.
- A bit graphics list has been created with two different graphics for the statuses.
- A screen is open.
- You have created a system diagnostics view.

##### Procedure

1. Double-click the "Button" object in the "Tools" task card. A button will be added to the screen.
2. In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Mode &gt; Graphic".
3. Select the bit graphics list under "Graphic &gt; Graphics list".
4. Select the "@DiagnosticsIndicatorTag" tag under "Properties &gt; Properties &gt; General &gt; Tag" in the Inspector window.

##### Configuring system function to the button

1. Click "Properties &gt; Events" in the Inspector window.
2. Select the "Click" event.
3. Click on "Add function" in the table.
4. Select the "ActivateSystemDiagnosticsView" system function.
5. Select the system diagnostics view.

##### Result

You have now configured a button which will respond to error messages from the PLC. The button changes its appearance if an error message is output in Runtime.

The button has two states:

- Error

  The system diagnostics view opens when you click the button. The system diagnostics view shows the detail view of the device concerned.
- No error

  The system diagnostics view opens when you click the button. The system diagnostics view shows the device view.

#### Configuring the system diagnostic view (Panels, Comfort Panels, RT Advanced)

##### Introduction

You add a System diagnostics view to your project to get an overview of all devices available in your plant.

##### Requirements

- At least one PLC has been created.
- A Comfort Panel or WinCC RT Advanced has been created.
- System diagnostics is enabled in every controller and on the HMI device .
- You have created a screen.
- The Inspector window is open.

##### Procedure

1. Double-click the "System diagnostics view" object in the "Tools" task card. The object is added to the screen.
2. Select "Properties &gt; Properties &gt; Columns &gt; Devices/Detail view" in the Inspector window.
3. Activate the columns that you require in the device view for Runtime, e.g. Status, Name, Slot.
4. Activate the columns that you require in the detail view for Runtime, e.g. Status, Name, Plant designation.
5. Activate the columns that you require in the diagnostic buffer view, e.g. Status, Name.
6. Enable "Properties &gt;Properties &gt; Layout &gt; Column settings &gt; Columns moveable" to move the columns in Runtime.
7. You can change the column headers under "Properties &gt; Properties &gt; Column headers", if necessary.

##### Result

The system diagnostics view has been added to the screen. Error for the entire plant are now displayed in the system diagnostics view in Runtime.

#### Configuring the system diagnostic view (Basic Panels)

##### Introduction

For an overview of all integrated connections, you insert a system diagnostics view in your project.

##### Requirements

- A PLC has been created.
- A Basic Panel has been created.
- An integrated connection has been created in the "Devices &amp; Networks" editor.
- You have created a screen.
- The Inspector window is open.

##### Procedure

1. Double-click the "System diagnostics view" object in the "Tools" task card. The object is added to the screen.
2. In the Inspector window, select "Properties &gt; Layout".
3. Enter a number under "Lines per entry", i.e. 5.

##### Result

The system diagnostics view has been added to the screen.

To obtain the latest alarms, update the diagnostic buffer.

#### Splitting the view in system diagnostics view (Panels, Comfort Panels, RT Advanced)

##### Introduction

The system diagnostics view also offers a split view of the display. You have the option to see the devices and the associated details at a glance.

##### Requirements

- At least one PLC has been created.
- An HMI device has been created, for example, a Comfort Panel.
- System diagnostics is enabled in every controller and on the HMI device .
- You have created a screen.
- The Inspector window is open.

##### Procedure

1. Double-click the "System diagnostics view" object in the "Tools" task card. The object is added to the screen.
2. In the Inspector window, click "Properties &gt; Properties &gt; Layout".
3. Activate "Show split view".
4. Activate "Fit to size &gt; Auto-size".
5. You may also change the number of lines for the "Device view" and the "Detail view" if required.

##### Result

The system diagnostics view has been added to the screen. The system diagnostics view is split into two areas.

The top area shows the device view. The bottom view shows the detail view.

![Result](images/76421042699_DV_resource.Stream@PNG-en-US.png)

If you open the diagnostic buffer view, the top area displays an overview of the diagnostic buffer and the bottom area displays the details.

![Result](images/76420833291_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Contents of the detail view**
>
> The contents of the detail view are only available for integrated connections with S7-1200 and S7-1500 controllers.

## System diagnostics (RT Professional)

This section contains information on the following topics:

- [Runtime Professional basics (RT Professional)](#runtime-professional-basics-rt-professional)
- [Configuring system diagnostics objects (RT Professional)](#configuring-system-diagnostics-objects-rt-professional)
- [Example: System diagnostics with all objects (RT Professional)](#example-system-diagnostics-with-all-objects-rt-professional)

### Runtime Professional basics (RT Professional)

This section contains information on the following topics:

- [System diagnostics basics (RT Professional)](#system-diagnostics-basics-rt-professional)
- [System diagnostics views (RT Professional)](#system-diagnostics-views-rt-professional)

#### System diagnostics basics (RT Professional)

##### Introduction

You use system diagnostics to detect problems and errors in any part of your plant. WinCC offers two operating elements for quick error localization.

For the controller to be able to transfer error messages to the system diagnostics view or the system diagnostics window, an HMI connection must exist between controller and HMI device. In addition, the system diagnostics must be enabled both in the PLC and on the HMI device.

In a SIMATIC S7-300/400 controller, the system diagnostics is disabled by default but can be enabled in the properties of the controller. In a SIMATIC S7-1200/1500 controller, the system diagnostics is enabled by default and cannot be deactivated.

With an HMI connection to a SIMATIC S7-300/400 controller, the "System diagnostics" option is enabled on the HMI device under "Runtime settings &gt; Alarms &gt; Controller alarms" by default and cannot be disabled. With an HMI connection to a SIMATIC S7-1200/1500 controller, the "System diagnostics" option is enabled by default on the HMI device under "Runtime settings &gt; Alarms &gt; Controller alarms" and cannot be disabled.

##### System diagnostics view

The alarm view shows the status of a PLC while the system diagnostics view gives you an overview of all devices available in your plant: You navigate directly to the cause of the error and to the relevant device. You have access to all diagnostics-capable devices which you have configured in the "Devices &amp; networks" editor.

##### System diagnostics indicator

The system diagnostics indicator is a predefined graphic symbol of the library which alerts you to errors in your system.

The system diagnostics indicator changes its appearance when an error occurs.

##### GoTo button

The GoTo button is a predefined graphic symbol in the library. When diagnostic alarms appear in the alarm view, you can use the GoTo function to jump to the error location in the system diagnostics view.

---

**See also**

[Activating system diagnostics (RT Professional)](#activating-system-diagnostics-rt-professional)

#### System diagnostics views (RT Professional)

##### Introduction

There are four different views available in the system diagnostics view and the system diagnostics window:

- Device view
- Diagnostic buffer view
- Detail view
- Matrix view (for master systems, PROFIBUS, PROFINET only)

##### Device view

The device view shows all the available devices of a layer in a table. Double-clicking on a device opens either the child devices or the detail view. Symbols in the first column provide information about the current status of the device.

![Device view](images/97216230155_DV_resource.Stream@PNG-en-US.png)

##### Diagnostic buffer view

In the diagnostic buffer view, the current data from the diagnostic buffer of the device is displayed. The diagnostic buffer view can only be called up in the device view.

To update the diagnostic buffer view, click "Update".

![Diagnostic buffer view](images/76412584843_DV_resource.Stream@PNG-en-US.png)

##### Detail view

The detail view gives detailed information about the selected device and the pending errors. Check whether the data is correct in the detail view. You cannot sort error texts in the detail view.

![Detail view](images/76414010891_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Contents of the detail view**
>
> The contents of the detail view are only available for integrated connections with S7-1200 and S7-1500 controllers.

##### Navigation buttons

| Button | Key | Function |
| --- | --- | --- |
| ![Navigation buttons](images/60987960971_DV_resource.Stream@PNG-de-DE.png) | Enter key | Opens the child devices or the detail view if there are no child devices. |
| ![Navigation buttons](images/60987968651_DV_resource.Stream@PNG-de-DE.png) | Esc key | Opens the parent device or the device view if there is no parent device. |
| ![Navigation buttons](images/60989333131_DV_resource.Stream@PNG-de-DE.png) | Home key | Opens the device view. |
| ![Navigation buttons](images/60989340811_DV_resource.Stream@PNG-de-DE.png) | Function key F4. | Opens the diagnostic buffer view.  Only visible in the device view. |
| ![Navigation buttons](images/53784988555_DV_resource.Stream@PNG-de-DE.png) | Function key F5. | Updates the diagnostic buffer view. |

### Configuring system diagnostics objects (RT Professional)

This section contains information on the following topics:

- [Activating system diagnostics (RT Professional)](#activating-system-diagnostics-rt-professional)
- [Adding a system diagnostics indicator (RT Professional)](#adding-a-system-diagnostics-indicator-rt-professional)
- [Configuring button as system diagnostics indicator (RT Professional)](#configuring-button-as-system-diagnostics-indicator-rt-professional)
- [Configuring the system diagnostics view (RT Professional)](#configuring-the-system-diagnostics-view-rt-professional)
- [Splitting the view in system diagnostics view (RT Professional)](#splitting-the-view-in-system-diagnostics-view-rt-professional)

#### Activating system diagnostics (RT Professional)

##### Introduction

An HMI connection must exist between controller and the HMI device so that the controller can send error messages to the system diagnostics view. In addition, the system diagnostics must be enabled both in the PLC and on the HMI device.

In a SIMATIC S7-300/400 controller, the system diagnostics is disabled by default but can be enabled. In a SIMATIC S7-1200/1500 controller, the system diagnostics is enabled by default and cannot be deactivated.

With an HMI connection to a SIMATIC S7-300/400 controller, the system diagnostics on the HMI device is activated by default and cannot be deactivated. With an HMI connection to a SIMATIC S7-1200/1500 controller, the system diagnostics on the HMI device can be activated and deactivated by default.

The following describes how to activate system diagnostics in a controller on an HMI device, if necessary.

##### Requirement

- There is an HMI connection between controller and HMI device.

##### Activating system diagnostics in the controller

To activate the system diagnostics in a controller, proceed as follows:

1. Open the "Device configuration" of the controller in the project tree.
2. In the "Device view" tab, select the CPU on the rack.
3. Select "Properties &gt; General &gt; System diagnostics" in the Inspector window.
4. Activate the option "Activate system diagnostics for this device".
5. Right-click the controller in the project tree and select "Compile &gt; Hardware (rebuild all)" in the shortcut menu.

##### Activating system diagnostics on the HMI device

To activate the system diagnostics on an HMI device, proceed as follows:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Select the option "System diagnostics" under "Alarms &gt; Controller alarms".

   The display of system diagnostic alarms is enabled in runtime.

> **Note**
>
> **Special feature system diagnostic alarms SIMATIC S7-300/400**
>
> When you deactivate the display class 0 for the respective HMI connection under "Runtime settings &gt; Alarms &gt; Controller alarms &gt; Display classes", the system diagnostic alarms are not transferred to the HMI device by the controller even when the system diagnostics is activated in the controller and on the HMI device.

---

**See also**

[System diagnostics basics (RT Professional)](#system-diagnostics-basics-rt-professional)

#### Adding a system diagnostics indicator (RT Professional)

##### Introduction

The system diagnostics indicator is a predefined graphic symbol of the library which alerts you to errors in your system.

If an error occurs, the appearance of the object changes. The library object can display two states:

- No error

- Error

##### Requirement

- The "Libraries" task card is opened.
- The global library "Buttons and Switches &gt; Master copies &gt; DiagnosticsButtons" is open.
- A screen is open.
- A system diagnostics window has been created in the global screen.

##### Procedure

1. Select the "DiagnosticsIndicator" object in the library.
2. Drag-and-drop the library object to the position in the work area where you want to insert the object.

   The library object is inserted.

   ![Procedure](images/97212885003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97212885003_DV_resource.Stream@PNG-en-US.png)
3. Select the library object.
4. Click "Properties &gt; Events" in the Inspector window.

   The system function "ShowSystemDiagnosticsWindow" is preset for the event "Click".

**Note**

**System diagnostics indicator for different device types**

When selecting the object ensure that you use the correct object for the device type used in the project.

##### Result

The status diagnostics indicator has been added to the project and connected with the system diagnostics window.

The system diagnostics indicator changes its appearance if an error message is output in Runtime. The system diagnostics window opens when you click on the system diagnostics indicator. The system diagnostics window shows the detail view of the affected device.

##### Configuring access protection for the system diagnostics window

Configure access protection for the system diagnostics indicator to prevent unauthorized access to the system diagnostics window.

1. Select the "DiagnosticsIndicator" object in the screen.
2. Select an authorization in "Properties &gt; Properties &gt; Security in Runtime" in the Inspector window.

A logon dialog opens when you click on the system diagnostics indicator in Runtime. The system diagnostics window does not open unless you have the required authorization.

#### Configuring button as system diagnostics indicator (RT Professional)

##### Introduction

Instead of using the object "DiagnosticsIndicator" from the library, you can configure a button, for example, to indicate errors in your plant.

##### Requirements

- At least one PLC has been created.
- System diagnostics is enabled in every controller and on the HMI device .
- The "Tools" task card is open.
- A bit graphics list has been created with two different graphics for the statuses.
- A screen is open.
- You have created a system diagnostics view.

##### Procedure

1. Double-click the "Button" object in the "Tools" task card. A button will be added to the screen.
2. In the Inspector window, select "Properties &gt; Properties &gt; General &gt; Mode &gt; Graphic".
3. Select the bit graphics list under "Graphic &gt; Graphics list".
4. Select the "@DiagnosticsIndicatorTag" tag under "Properties &gt; Properties &gt; General &gt; Tag" in the Inspector window.

##### Configuring system function to the button

1. Click "Properties &gt; Events" in the Inspector window.
2. Select the "Click" event.
3. Click on "Add function" in the table.
4. Select the "ActivateSystemDiagnosticsView" system function.
5. Select the system diagnostics view.

##### Result

You have now configured a button which will respond to error messages from the PLC. The button changes its appearance if an error message is output in Runtime.

The button has two states:

- Error

  The system diagnostics view opens when you click the button. The system diagnostics view shows the detail view of the device concerned.
- No error

  The system diagnostics view opens when you click the button. The system diagnostics view shows the device view.

#### Configuring the system diagnostics view (RT Professional)

##### Introduction

You add a System diagnostics view to your project to get an overview of all devices available in your plant.

##### Requirements

- At least one PLC has been created.
- An HMI device has been created.
- An HMI connection has been established between the controller and HMI device.
- System diagnostics is enabled in every controller and on the HMI device .
- You have created a screen.
- The Inspector window is open.

##### Procedure

1. Double-click the "System diagnostics view" object in the "Tools" task card. The object is added to the screen.
2. Select "Properties &gt; Properties &gt; Columns &gt; Devices/Detail view" in the Inspector window.
3. Activate the columns that you require in the device view for Runtime, e.g. Status, Name, Slot.
4. Activate the columns that you require in the detail view for Runtime, e.g. Status, Name, Plant designation.
5. Activate the columns that you require in the diagnostic buffer view, e.g. Status, Name.
6. Select "Properties &gt;Properties &gt; Layout &gt; Column settings &gt; Columns movable" to enable move of the columns in Runtime.
7. You can change the column headers under "Properties &gt; Properties &gt; Column headers", if necessary.

##### Result

The system diagnostics view has been added to the screen. Error for the entire plant are now displayed in the system diagnostics view in Runtime.

#### Splitting the view in system diagnostics view (RT Professional)

##### Introduction

The system diagnostics view also offers a split view of the display. You have the option to see the devices and the associated details at a glance.

##### Requirements

- At least one PLC has been created.
- An HMI device has been created.
- System diagnostics is enabled in every controller and on the HMI device .
- You have created a screen.
- The Inspector window is open.

##### Procedure

1. Double-click the "System diagnostics view" object in the "Tools" task card. The object is added to the screen.
2. In the Inspector window, click "Properties &gt; Properties &gt; Layout".
3. Activate "Show split view".
4. You may also change the number of lines for the "Device view" and the "Detail view" if required.

##### Result

The system diagnostics view has been added to the screen. The system diagnostics view is split into two areas.

The top area shows the device view. The bottom view shows the detail view.

![Result](images/97420419083_DV_resource.Stream@PNG-en-US.png)

If you open the diagnostic buffer view, the top area displays an overview of the diagnostic buffer and the bottom area displays the details.

> **Note**
>
> **Contents of the detail view**
>
> The contents of the detail view are only available for integrated connections with S7-1200 and S7-1500 controllers.

### Example: System diagnostics with all objects (RT Professional)

This section contains information on the following topics:

- [Example: Procedures overview (RT Professional)](#example-procedures-overview-rt-professional)
- [Example: Creating screens (RT Professional)](#example-creating-screens-rt-professional)
- [Example: Inserting objects in the screens (RT Professional)](#example-inserting-objects-in-the-screens-rt-professional)
- [Example: Adding a system diagnostics indicator (RT Professional)](#example-adding-a-system-diagnostics-indicator-rt-professional)
- [Example: Inserting a GoTo button (RT Professional)](#example-inserting-a-goto-button-rt-professional)

#### Example: Procedures overview (RT Professional)

##### Introduction

- A controller and an HMI device have been created.
- An HMI connection has been established between the controller and HMI device.
- System diagnostics is activated in the controller and on the HMI device.

##### Configuration steps

To get a quick view of errors, create an overview screen with the various objects for displaying diagnostic alarms.

The following example shows how to efficiently use the objects of the "Tools" or "Libraries" task cards in your project.

The example is divided into several steps:

- Creating screens

  The project engineer creates multiple screens for system diagnostics:

  - Overview screen with all objects for system diagnostics
  - Screen for the alarm view
  - Screen for the system diagnostics view
- Inserting objects in the screens

  The project engineer inserts various objects in the screens:

  - Alarm view in the "Alarm" screen
  - Screen window for displaying the alarm view and system diagnostics view
- Configuring objects

  The project engineer connects objects to enable targeted navigation to the cause of the error in runtime.

  - System diagnostic indicator with screen window of the system diagnostics view
  - Goto button with the screen window and the alarm view and system diagnostics view.

---

**See also**

[Example: Adding a system diagnostics indicator (RT Professional)](#example-adding-a-system-diagnostics-indicator-rt-professional)
  
[Example: Inserting a GoTo button (RT Professional)](#example-inserting-a-goto-button-rt-professional)
  
[Example: Creating screens (RT Professional)](#example-creating-screens-rt-professional)
  
[Example: Inserting objects in the screens (RT Professional)](#example-inserting-objects-in-the-screens-rt-professional)

#### Example: Creating screens (RT Professional)

##### Introduction

In the following, you will create three screens for displaying various objects.

##### Requirement

- A project is open.
- An HMI device has been created.

##### Procedure

1. Open the project tree.
2. Click "Add new screen" in the Screens folder.
3. Open the shortcut menu of the screen and assign the name "Overview SysDiag".
4. Create another screen named "Alarm".
5. Open the "Libraries" task card.
6. Open the global library "Buttons and Switches &gt; Kopiervorlagen &gt; DiagnosticsButtons &gt; RTProfessional".
7. Click the "DiagnosticScreen" object in the global library.
8. Drag-and-drop the object into the "Screens" folder in the project tree.

##### Result

You have created three screens in the project tree:

- Overview SysDiag
- Alarm
- SystemDiagnostics

A system diagnostics view has been created in the "SystemDiagnostics" screen.

---

**See also**

[Example: Procedures overview (RT Professional)](#example-procedures-overview-rt-professional)

#### Example: Inserting objects in the screens (RT Professional)

##### Introduction

In the following example, you will insert various objects from the "Tools" task card into the screens.

##### Requirement

The following three screens have been created:

- Overview SysDiag
- Alarm
- SystemDiagnostics

The "Tools" task card is open.

##### Procedure

1. Open the "Alarm" screen.
2. Drag-and-drop an "Alarm view" from the "Tools" task card into the screen.
3. Open the screen "Overview SysDiag".
4. Drag-and-drop a "Screen window" from the "Tools" task card into the screen.
5. Enter the name "Alarm" under "Properties &gt; Properties &gt; Miscellaneous &gt; Name" in the Inspector window.
6. Select the "Alarm" screen under "Properties &gt; Properties &gt; General &gt; Content &gt; Displayed screen".
7. Create a second screen window named "SysDiag".
8. Select the "SystemDiagnostics" screen under "Properties &gt; Properties &gt; General &gt; Content &gt; Displayed screen".

##### Result

You have inserted an alarm view in the "Alarm" screen. The alarm view has the unchanged name "Alarm_view_1".

You have created two screen windows in the "Overview SysDiag" screen. The first screen window has the name "Alarm" and shows the alarm view. The second screen window has the name "SysDiag" and shows the system diagnostics view.

---

**See also**

[Example: Procedures overview (RT Professional)](#example-procedures-overview-rt-professional)

#### Example: Adding a system diagnostics indicator (RT Professional)

##### Introduction

The system diagnostics indicator is a predefined graphic symbol of the library which alerts you to errors in your system.

If an error occurs, the appearance of the object changes. The library object can display two states:

- No error

- Error

##### Requirement

- The "Libraries" task card is opened.
- The global library "Buttons and Switches &gt; Master copies &gt; DiagnosticsButtons &gt; RT Professional" is open.
- The following three screens have been created:

  - Overview SysDiag
  - Alarm
  - SystemDiagnostics
- The "SysDiag" screen window has been created and linked with the "DiagnosticScreen" screen.

##### Procedure

1. Select the "DiagnosticsIndicator" object in the library.
2. Drag the library object to the screen "Overview SysDiag".

   The library object is inserted.
3. Select the library object.
4. Click "Properties &gt; Events" in the Inspector window.

   Three system functions are preset for the "Click" event.

   ![Procedure](images/97219281675_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/97219281675_DV_resource.Stream@PNG-en-US.png)
5. Select "SysDiag" for the "Screen name" parameter in the "ActivateScreenInScreenWindow" system function.
6. Select "SysDiag" for the "Screen object" parameter in the "SetPropertyByConstant" system function.

##### Result

The system diagnostics indicator has been added to the project and connected with the "SysDiag" screen window.

The system diagnostics indicator changes its appearance if an error message is output in Runtime. The SysDiag screen window in which system diagnostics view is configured opens when you click the system diagnostics indicator. The system diagnostics view shows the detail view of the device concerned.

---

**See also**

[Example: Procedures overview (RT Professional)](#example-procedures-overview-rt-professional)

#### Example: Inserting a GoTo button (RT Professional)

##### Requirements

- The "Libraries" task card is opened.
- The global library "Buttons and Switches &gt; Master copies &gt; DiagnosticsButtons &gt; RT Professional" is open.
- The following three screens have been created:

  - Overview SysDiag
  - Alarm
  - SystemDiagnostics
- The "Alarm" screen window has been created and linked with the "Alarm" screen.
- The "SysDiag" screen window has been created and linked with the "DiagnosticScreen" screen.

##### Configuring a Goto button in the screen

1. Open the screen "SystemDiagnostic".
2. Open the global library "Buttons and Switches &gt; Master copies &gt; DiagnosticsButtons".
3. Select the "DiagnosticsGoto" object in the library.
4. Drag the library object to the screen "Overview SysDiag". The library object is inserted.
5. Select the library object.
6. Click "Properties &gt; Events" in the Inspector window.

   Three system functions are preset for the event.

   ![Configuring a Goto button in the screen](images/97227244043_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a Goto button in the screen](images/97227244043_DV_resource.Stream@PNG-en-US.png)
7. Select "SysDiag" for the "Screen name" parameter in the "ActivateScreenInScreenWindow" system function.
8. Select "SysDiag" for the "Screen object" parameter in the "SetPropertyByConstant" system function.
9. Select the following settings in the "SetPropertyByProperty" system function:

   - Screen name: Alarm
   - Object: Alarm_view_1

##### Result

You have configured the Goto button and linked it to the alarm view and the system diagnostics view.

Click on the GoTo button if the alarm view outputs an error message in the "Alarms" screen window in runtime.

A system diagnostics view has been added to the "SysDiag" picture window. The device with the associated error is opened in the detail view.

---

**See also**

[Example: Procedures overview (RT Professional)](#example-procedures-overview-rt-professional)
