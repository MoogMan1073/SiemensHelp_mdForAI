---
title: "Operating Unified Panel (RT Unified)"
package: WinCCRTPanenUS
topics: 26
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Operating Unified Panel (RT Unified)

This section contains information on the following topics:

- [Users in runtime (RT Unified)](#users-in-runtime-rt-unified)
- [Viewing memory card data (RT Unified)](#viewing-memory-card-data-rt-unified)
- [Operation in Unified Runtime (RT Unified)](#operation-in-unified-runtime-rt-unified)
- [Entering barcodes via handheld readers (RT Unified)](#entering-barcodes-via-handheld-readers-rt-unified)

## Users in runtime (RT Unified)

### Introduction

To protect your project, create users and assign roles to them. You can create local users or central users in the UMC (User Management Component). To access the runtime of a project, a user must be configured before loading. You configure the user administration in the engineering system.

### Local user administration

To transfer the local user administration from the engineering system to the HMI device, the HMI device "Keep current user administration data in the runtime" must be disabled in the "Load preview" dialog before loading.

Runtime starts after loading the local user administration settings.

### Central user administration in the UMC

The connection to the central UMC server is established after loading the settings of the central user administration. Runtime starts and you log on in Runtime.

---

**See also**

[Using central user management in the Control Panel (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#using-central-user-management-in-the-control-panel-rt-unified)
  
[Protecting the Control Panel from being accessed (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#protecting-the-control-panel-from-being-accessed-rt-unified)

## Viewing memory card data (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Working with backups (RT Unified)](#working-with-backups-rt-unified)

### Basics (RT Unified)

WinCC provides you with the possibility of viewing data stored on your memory card. The function supports the use of memory cards of the HMI device and of the PLC.

You have the following options:

- [Viewing a backup](#viewing-a-backup-rt-unified)
- [Renaming and deleting backups](#renaming-and-deleting-backups-rt-unified)

---

**See also**

[Viewing a backup (RT Unified)](#viewing-a-backup-rt-unified)
  
[Renaming and deleting backups (RT Unified)](#renaming-and-deleting-backups-rt-unified)

### Working with backups (RT Unified)

This section contains information on the following topics:

- [Viewing a backup (RT Unified)](#viewing-a-backup-rt-unified)
- [Renaming and deleting backups (RT Unified)](#renaming-and-deleting-backups-rt-unified)

#### Viewing a backup (RT Unified)

##### Introduction

If you have stored the backup of an HMI device on a memory card, this backup can also be viewed in the TIA Portal.

##### Requirements

- WinCC is installed.
- A memory card with a backup is available.
- The card reader is connected to the configuration PC.
- The project view is open.

##### Backup on the memory card in the card reader

1. Insert the memory card into the card reader.
2. Open "Card Reader/USB storage" in the project tree.
3. Select the card reader drive.

   The "Online card data" folder is displayed.
4. Open the "Online card data" folder.
5. Click the backup to open the shortcut menu.
6. Select "Properties".

##### Backup on the memory card of the PLC

Proceed as follows if the backup is stored on the memory card of the PLC:

1. Connect the PLC with the configuration PC.
2. Click on the PLC in the project navigation.
3. Select "Connect online" from the shortcut menu.

   A connection to the PLC is established.

   Once the PLC is connected, the "Online card data" folder is displayed.
4. Open the "Online card data" folder.

   > **Note**
   >
   > **Accessing a password-protected PLC**
   >
   > When you attempt to access a PLC that is protected by a password, you will be prompted to enter the password.
   >
   > You need at least read access rights in order to view the data that is stored on the memory card.
5. Click the backup to open the shortcut menu.
6. Select "Properties".

##### Result

The backup properties are displayed in a separate dialog:

- General properties

  - Date and time when the backup was created
  - Software version with which the backup was created.
- Supported HMI devices with which the backup is compatible

---

**See also**

[Renaming and deleting backups (RT Unified)](#renaming-and-deleting-backups-rt-unified)

#### Renaming and deleting backups (RT Unified)

##### Introduction

You can rename and delete backups from a memory card in the project navigation of the TIA Portal.

##### Requirements

- WinCC is installed.
- The card reader is connected to the configuration PC.

  Or The PLC is connected online with the configuration PC.
- A memory card with a backup is available.
- The project view is open.
- The backup is displayed in the project navigation.

  > **Note**
  >
  > **Accessing a password-protected PLC**
  >
  > When you attempt to access a PLC that is protected by a password, you will be prompted to enter the password.
  >
  > You need write access rights to rename or delete memory card data.

##### Procedure

1. Click on the backup in the project navigation.
2. Open the shortcut menu.
3. Select "Rename" to rename the file.
4. Enter a new name.
5. Select "Delete" to delete the file.

##### Result

The backup file is now renamed or deleted.

---

**See also**

[Viewing a backup (RT Unified)](#viewing-a-backup-rt-unified)

## Operation in Unified Runtime (RT Unified)

This section contains information on the following topics:

- [Overview (RT Unified)](#overview-rt-unified)
- [Operation with the touch screen (RT Unified)](#operation-with-the-touch-screen-rt-unified)
- [Triggering an action (RT Unified)](#triggering-an-action-rt-unified)
- [Entering a value (RT Unified)](#entering-a-value-rt-unified)
- [Moving operator controls (RT Unified)](#moving-operator-controls-rt-unified)
- [Changing Runtime language (RT Unified)](#changing-runtime-language-rt-unified)
- [Web browser of WebKit engine (RT Unified)](#web-browser-of-webkit-engine-rt-unified)

### Overview (RT Unified)

#### Operating options for an HMI device

The following operating options are available:

- Operation via touch screen  
  The HMI device has a touch-sensitive touch screen. Use your finger or a suitable touch pen to operate the touch screen.
- Operation via mouse and keyboard  
  You can use the mouse and keyboard to operate the device like a PC.

Adhere to the instructions for operating the device in the relevant operating instructions.

#### Individually configured operation

The configuration engineer has various options available for setting up operation.

Examples of actions whose execution is always determined on a project-specific basis:

- Screen change
- Reporting
- Changing runtime language

There are no specific operating elements to execute certain functions. The configuration engineer specifies the project-specific execution. The screen change can be triggered, for example, via a button.

Information on project-specific operations can be found in the system documentation.

### Operation with the touch screen (RT Unified)

This section contains information on the following topics:

- [Overview of operation with the touch screen (RT Unified)](#overview-of-operation-with-the-touch-screen-rt-unified)
- [Placing the focus on objects (RT Unified)](#placing-the-focus-on-objects-rt-unified)
- [Operating objects with transparent fill (RT Unified)](#operating-objects-with-transparent-fill-rt-unified)
- [Using multi-touch functions (RT Unified)](#using-multi-touch-functions-rt-unified)

#### Overview of operation with the touch screen (RT Unified)

You use the touchscreen to operate the HMI device or the project running on your HMI device.

##### Special features when operating using the touch screen

Operation with the touch screen is characterized by the following special features:

- Enable

  To enable the operator control, use your finger or a suitable touch pen to operate the touch screen. To generate a double-click, touch the operator control twice in rapid succession.
- Value input

  You enter numbers and letters on the touch screen with a screen keyboard.

##### Input using the screen keyboard

The screen keyboard is displayed when you select a screen item that requires input. The screen keyboard is hidden again when input is complete.

Further information on the screen keyboard can be found in the operating instructions of the HMI device.

#### Placing the focus on objects (RT Unified)

You have the following options:

- Click or tap on the object.

  > **Note**
  >
  > **Giving focus to objects with a transparent background**
  >
  > If an object has a transparent background, click on a visible area of the object.
- Press <Tab> until the object has the focus.

#### Operating objects with transparent fill (RT Unified)

The objects displayed on a screen can have transparent ranges.

Example: Sliders, bars and pointer instruments are enclosed by a transparent rectangle.

##### Requirement

An event which is triggered by operating actions such as typing or clicking has been configured for the object in the engineering.

##### Trigger event

To trigger the event, proceed as follows:

- If the object does not have the focus, click a visible part of the object, e.g. its border.
- If the object already has the focus, the event is also triggered by clicking in the transparent area.

#### Using multi-touch functions (RT Unified)

This section contains information on the following topics:

- [Supported gestures (RT Unified)](#supported-gestures-rt-unified)
- [Special features for multi-touch operation (RT Unified)](#special-features-for-multi-touch-operation-rt-unified)
- [Two-hand operation of operator controls (RT Unified)](#two-hand-operation-of-operator-controls-rt-unified)

##### Supported gestures (RT Unified)

###### Definition

Various touch gestures are available for the runtime operation. Some touch gestures have different effects in the process screens than in the controls.

> **Note**
>
> **No operation with three or more fingers.**
>
> Only use one or two fingers when operating with touch gestures.
>
> If you use more than two fingers with touch gestures, this can cause incorrect operation.
>
> In the case of multi-touch operation with several fingers, you only operate the respectively configured objects.

###### Supported touch gestures in process screens

| Icon | Gesture | Function |
| --- | --- | --- |
| ![Supported touch gestures in process screens](images/102214480139_DV_resource.Stream@PNG-de-DE.png) | Tap | To select an object, tap on the corresponding position in the process screen. |
| ![Supported touch gestures in process screens](images/102214596107_DV_resource.Stream@PNG-de-DE.png) | Drag with one finger | To move objects with a window, drag the object by its title bar in the desired direction. |
| ![Supported touch gestures in process screens](images/102199055755_DV_resource.Stream@PNG-de-DE.png) | Zoom | To zoom in or zoom out, drag simultaneously with two fingers. |
| ![Supported touch gestures in process screens](images/102214609035_DV_resource.Stream@PNG-de-DE.png) | Drag with two fingers | To move the zoomed area of a process screen, drag with two fingers in an area where there are no control objects. |
| ![Supported touch gestures in process screens](images/142861099659_DV_resource.Stream@PNG-de-DE.png) | Wiping | To switch between two process screens, swipe horizontally or vertically with one finger. A touch area must be configured for this function. |
| ![Supported touch gestures in process screens](images/102214557451_DV_resource.Stream@PNG-de-DE.png) | Keep pressed | The function corresponds to a right-click.  To trigger the event configured for the right-click, press for longer than a second on the object or the link. |

###### Supported touch gestures in controls

| Icon | Gesture | Behavior | Supported WinCC controls |
| --- | --- | --- | --- |
| ![Supported touch gestures in controls](images/102214480139_DV_resource.Stream@PNG-de-DE.png) | Tap | - To select a row, tap the row. - With corresponding configuration of the control: To select a cell. - With corresponding configuration of the control: To sort a column.   To sort a column, click on the column header. - In trend controls:  Zooms in on the trend area along the X/Y axis.   Requirement: The "Zoom +/-", "Zoom time axis +/-" or "Zoom value axis +/-" button is pressed. | - Alarm control - Process control - Trend control - f(x) trend control - Ruler window - System diagnostics control - Parameter set control |
| ![Supported touch gestures in controls](images/102214493067_DV_resource.Stream@PNG-de-DE.png) | Tap with two fingers | Zooms out of the trend control. Requirement: The "Zoom +/-", "Zoom time axis +/-" or "Zoom value axis +/-" button is pressed.  Leave a little space between your fingers when tapping. | - Trend control - f(x) trend control |
| ![Supported touch gestures in controls](images/102214609035_DV_resource.Stream@PNG-de-DE.png) | Drag with two fingers | To move window contents, such as zoomed-in tables or trends, drag with two fingers in the operating element window. | - Process control - Ruler window - Browser |
| ![Supported touch gestures in controls](images/102214596107_DV_resource.Stream@PNG-de-DE.png) | Drag with one finger | - Moves the ruler. - Moves the X axis or Y axis.   Requirement: The "Move trend area" or "Move axis area" button is pressed or the control is zoomed in. | - Trend control - f(x) trend control |
| To select multiple lines. Tap on a line and drag your finger up or down.  With corresponding configuration of the control: To select multiple cells. | - Process control - Ruler window - System diagnostics control - Parameter set control |  |  |
| To adapt the column width, tap a column grid line and drag your finger to the right or left. | - Alarm control - Ruler window |  |  |
| To move zoomed-in window contents, drag with one finger. | Browser |  |  |
| ![Supported touch gestures in controls](images/102214518795_DV_resource.Stream@PNG-de-DE.png) | Double tap | To edit a cell value, double-tap the cell.  Requirement:  - Table view: The "Edit" button is pressed. - Parameter set control: A parameter set is selected. | - Process control - Parameter set control |
| ![Supported touch gestures in controls](images/102199055755_DV_resource.Stream@PNG-de-DE.png) | Scale | To zoom in or out in an operating element, drag with two fingers in the operating element window. | Trend control, browser |
| ![Supported touch gestures in controls](images/102214441611_DV_resource.Stream@PNG-de-DE.png) | Two-hand operation  Hold the release button with one finger, and operate an object with the second finger | An operating element can be configured for two-hand operation, that is, the object can only be operated when a release button is being pressed at the same time.  For two-hand operation in WinCC you configure:  - A button that is defined as a release button in the security settings of a plant screen. - The security property "Require explicit unlock" at all operating elements that can only be operated when the release button is pressed. |  |

---

**See also**

[Special features for multi-touch operation (RT Unified)](#special-features-for-multi-touch-operation-rt-unified)

##### Special features for multi-touch operation (RT Unified)

###### Scrolling in lists and controls

You can scroll through lists and controls by dragging.

###### Special features of the trend view

You enlarge or reduce the view in "Trend view" and "f(x) trend view" objects by pinch-to-zoom with two fingers.

Double tap to switch from the magnified trend view back to the normal view.

The zooming function is limited to the time axis in the "Trend view" object.

If you have enabled the option "Range > Auto-size" during configuration of the value axes in f(x) trend view, the axes are constantly calculated during zooming.

Horizontal scrolling is not supported in the "Trend view" object.

> **Note**
>
> **Current view is not persistent**
>
> The changes of zoom factor and position changed by scrolling are not saved.
>
> The trend view is reset to the default setting during a screen change.

---

**See also**

[Supported gestures (RT Unified)](#supported-gestures-rt-unified)

##### Two-hand operation of operator controls (RT Unified)

This section contains information on the following topics:

- [Two-hand operation of operator controls (RT Unified)](#two-hand-operation-of-operator-controls-rt-unified-1)
- [Locking and unlocking operator controls (RT Unified)](#locking-and-unlocking-operator-controls-rt-unified)
- [Configuring the release button in the screen (RT Unified)](#configuring-the-release-button-in-the-screen-rt-unified)

###### Two-hand operation of operator controls (RT Unified)

###### Introduction

WinCC supports two-hand operation of operator controls for Unified Comfort Panel. It ensures safe operation of operator controls which are used to change critical system settings, for example, control tags with machine limits.

###### Locked and unlocked operator controls

You define specific operator controls as "locked operator controls" for two-hand operation of operator controls. Locked operator controls usually cannot be operated in runtime. Operators can only operate the locked operator controls when they press a release button at the same time.

In runtime, locked operator controls can only be accessed with the tab sequence when a release button is pressed at the same time.

###### Locked operator controls and release buttons

You can configure all operator controls as locked.

You must configure at least one button in the screens as release button. This can be any unlocked button. The unlocking of locked operator controls by pressing the release button has an effect on all open screens.

###### Display in runtime

The locked operator controls are displayed as dimmed in runtime. The locked operator controls are completely visible when they are unlocked by means of the release button.

###### Simulation of projects with multi-touch functions

WinCC supports the simulation of configured multi-touch functions. Requirement is that your monitor supports multi-touch operation.

###### Locking and unlocking operator controls (RT Unified)

You can lock and unlock operator controls in projects for multi-touch devices. Locked operator controls can only be operated in runtime when the operator presses a release button at the same time.

You can lock and unlock individual operator controls or several operator controls simultaneously.

###### Procedure

1. Configure operator controls of the type I/O field, button or slider.
2. Select the required operator control(s).
3. To lock the operator controls, enable the "Require explicit unlock" option under "Properties > Properties > Security".

   ![Procedure](images/142829706507_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142829706507_DV_resource.Stream@PNG-en-US.png)
4. To unlock the operator controls, disable the "Require explicit unlock" option under "Properties > Properties > Security".

In runtime, locked operator controls can only be operated when a release button is pressed at the same time.

> **Note**
>
> Locking of operator controls is an add-on to the existing security settings of the operator control. This means that in case of locked operator controls - in addition to pressing the release button - the general operability ("Allow operator control" option) and the required operator control ("Authorization" property) must be present so that the operator control can be operated in runtime.

###### Defining the release button

To use the locked operator controls, you must configure at least one release button in one of the displayed screens.

###### Configuring the release button in the screen (RT Unified)

So that you can operate locked operator controls on multi-touch devices, configure a release button.

###### Procedure

1. Select the screen.
2. Select the desired button of the screen under "Properties > Security" under "Enable explicit unlock".

   ![Procedure](images/142819085195_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142819085195_DV_resource.Stream@PNG-en-US.png)
3. To turn a release button back into a normal button, select a different button or "None" under "Properties > Security" under "Enable explicit unlock".

### Triggering an action (RT Unified)

#### Introduction

Triggering an action at an operator control can mean the following:

- A command is executed.

  Example: Touch a button to trigger a script or perform a predefined function.
- An object is enabled.

  Example: Touch a table cell to enter a value in a list.

#### Requirement

- You have navigated to the operator control on which you want to trigger the action.
- The operator control has the focus.

#### Procedure

- Touch the operator control on the touch screen once or twice in rapid succession.

#### Result

The following results are possible:

- The requested command is executed.
- The screen keyboard is opened and/or the cursor blinks in the input area of the operator control.
- The element is selected and can be moved.

### Entering a value (RT Unified)

#### Introduction

Depending on the input format, you enter numeric or alphanumeric values in an input field using the screen keyboard.

#### Requirement

- The object is an input field or table field.
- The operator control is enabled.

#### Entering a value

1. Enter the desired value.
2. To confirm the value and exit the field, press the <Enter> key.
3. To discard the value and exit the field, press the <Esc> key.

#### Result

A value is entered or discarded. You navigate as needed to the next operator control.

For more detailed information, refer to the operating instructions for your HMI device.

### Moving operator controls (RT Unified)

#### Introduction

You operate movable operator controls of a screen item in Runtime via the touchscreen, such as a slider.

#### Requirement

- A movable operator control is selected.

#### Procedure

1. Use a corresponding gesture to move the operator control, e.g. "drag" for a slider.
2. To finish the movement, navigate to another screen object or operator control.

#### Result

The position of the movable operator control and the display in the screen object have changed.

### Changing Runtime language (RT Unified)

#### Introduction

The project on the HMI device can be multilingual. A corresponding operating element which lets you change the language setting on the HMI device has been configured in runtime.

The project always starts with the language set in the previous session.

#### Requirement

- The desired language for the project is available on the HMI device.
- The language switching function is linked to an operating element, for example, to a button.

#### Selecting a language

You can change project languages at any time. The language-specific objects are displayed in the selected language when the language switching function is called.

You can switch the language in Runtime in one of the following ways:

- Use a configured operating element to switch from one language to the next in a list.
- Use a configured operating element to directly set the required language.

### Web browser of WebKit engine (RT Unified)

#### Introduction

If the "Browser" object is configured for an HMI device, then the "Browser" operating object is displayed in the corresponding runtime screen. Only the web browser of the WebKit engine is available on HMI devices. This web browser offers many HTML5 features, but no Active X support.

#### HTML5 functions

The following HTML5 standard functions are fully or partly supported by the Web browser of the WebKit engine:

- Parsing rules
- Elements
- Forms and fields
- Output
- Communication
- User interactions
- Performance
- Security
- History and Navigation
- 2D graphics
- Memory
- Animations
- Web applications
- Files and file systems

> **Note**
>
> **Functions not supported in the WebKit engine web browser**
>
> - Microdata
> - Enter
> - Peer to peer
> - Position and orientation
> - Video, audio
> - Responsive images
> - 3D graphics
> - Streams
> - Web components

The following tables show the availability of the HTML5 functions in the web browser of the WebKit engine in detail:

| Parsing rules | Available |
| --- | --- |
| <!DOCTYPE html> triggers the standard mode | Yes |
| HTML5 tokenizer | Yes |
| HTML 5 tree building | Yes |
| Parsing Inline SVG | Yes |
| Parsing Inline MathML | Yes |

| Elements | Available |
| --- | --- |
| Embedded invisible data | Yes |
| **New or modified elements** |  |
| Section elements | Yes |
| Grouping content elements that belong together | Partly |
| Semantic elements of the text level | Partly |
| Interactive elements | Partly |
| **Global attributes and methods** |  |
| Hidden attributes | Yes |
| Inserting dynamic markups | Yes |

| Forms and fields | Available |
| --- | --- |
| **Field types** |  |
| type = text | Yes |
| type = search | Yes |
| type = tel | Yes |
| type = URL | Yes |
| type = email | Yes |
| type = date | No |
| type = month | No |
| type = week | No |
| type = time | No |
| type = datetime | No |
| type = datetime-local | No |
| type = number | Yes |
| type = range | Yes |
| type = color | Yes |
| type = checkbox | Yes |
| type = image | Yes |
| type = file | Yes |
| textarea | Yes |
| select | Yes |
| fieldset | Yes |
| datalist | Yes |
| keygen | Yes |
| output | Yes |
| progress | Yes |
| meter | Yes |
| **Fields** |  |
| Field validation | Yes |
| Assignment of forms and controls | Yes |
| Other attributes | Yes |
| CSS sectors | Yes |
| Events | Yes |
| **Forms** |  |
| Form validation | Yes |

| Output | Available |
| --- | --- |
| Full-screen support | No |
| Web notifications | Yes |

| Communication | Available |
| --- | --- |
| Server-sent events | Yes |
| Web beacons | No |
| **XML HttpRequest Level 2** |  |
| File upload | Yes |
| Response type | Yes |
| **WebSocket** |  |
| Basic Socket Communication | Yes |
| ArrayBuffer and Blob | Yes |

| User interactions | Available |
| --- | --- |
| **Drag-and-drop** |  |
| Attributes | Yes |
| Events | Yes |
| **Editing HTML** |  |
| Editing elements | Yes |
| Editing documents | Yes |
| CSS sectors | No |
| APIs | Yes |
| **Clipboard** |  |
| Clipboard for API and events | No |
| **Spell check** |  |
| Spelling attributes | Yes |

| Performance | Available |
| --- | --- |
| Native binary data | Yes |
| **Workers** |  |
| Web workers | Yes |
| Shared workers | Yes |

| Security | Available |
| --- | --- |
| Web Cryptography API | No |
| Content Security Policy 1.0 | Yes |
| Content Security Policy 1.1 | No |
| Cross-Origin Resource Sharing | Yes |
| Cross-Document Messaging | Yes |
| **iFrames** |  |
| Sandboxes iFrame | Yes |
| Seamless iFrame | Yes |
| iFrame with inline contents | Yes |

| History and Navigation | Available |
| --- | --- |
| Session history | Yes |

| 2D graphics | Available |
| --- | --- |
| Canvas 2D graphics | Yes |
| **2D primitives** |  |
| Text input in graphics | Yes |
| Path input in graphics | No |
| Drawing an ellipse in graphics | No |
| Drawing a dashed line in graphics | Yes |
| System focus ring | No |
| **Functions** |  |
| Hit testing | No |
| Aperture mode | No |
| **Formats for image export** |  |
| PNG | Yes |
| JPEG | Yes |
| JPEG-XR | No |
| WebP | No |

| Animation | Available |
| --- | --- |
| window.requestAnimationFrame | Yes |

| Web applications | Available |
| --- | --- |
| **Offline resources** |  |
| Application cache | Yes |
| Service workers | No |
| **Content and scheme handlers** | No |

| Memory | Available |
| --- | --- |
| **Key value storage** |  |
| Session memory | Yes |
| Local storage | No |
| **Database storage** |  |
| IndexedDB | No |
| Blob object store | No |
| ArrayBuffer object store | No |
| Web SQL database | Yes |

| Files and file systems | Available |
| --- | --- |
| **Reading files** |  |
| Basic support for reading files | Yes |
| Creating a blob from a file | Yes |
| Creating a data URL from a blob | Yes |
| Creating an ArrayBuffer from a blob | Yes |
| Creating a blob URL from a blob | Yes |
| **Accessing a file system** |  |
| API file system | No |
| File API: Folders and system | No |

| Additional functions | Available |
| --- | --- |
| **Styles** |  |
| Style items | No |
| **Scripts** |  |
| Asynchronous script execution | Yes |
| Signaling script errors in Runtime | Yes |
| Events for script execution | No |
| Base 64 encoding and decoding | Yes |
| JSON coding and decoding | Yes |
| URL API | Yes |
| MutationObserver | "Yes" (pre-selected) |
| Promises | No |
| Page visibility | "Yes" (pre-selected) |
| Text selection | Yes |
| Scrolling (Scroll into view) | Yes |

## Entering barcodes via handheld readers (RT Unified)

### Introduction

Optical handheld readers enable you to optically identify components, machines and other objects and to transfer the read-out data on your HMI device directly to certain operating objects.

Optical handheld readers capture codes such as two-dimensional data matrix codes, one-dimensional barcodes and postal barcodes.

Supported optical handheld readers can be found at the following entry on the Internet:

[FAQ 19188460](https://support.industry.siemens.com/cs/ww/en/view/19188460)

You can find templates for the settings and instructions on configuration in the manual for your optical handheld reader.

### Procedure

You use the connected optical reader to read a code into the object that has the focus.

After the read-in, confirm the value with the Enter key or with the "Suffix - Enter" that you have previously configured in the settings of your optical reader.

### Objects for input with optical handheld reader

The following objects support input via an optical handheld reader:

| Object | Preconditions for input |
| --- | --- |
| IO field  Clock | The corresponding data type is selected.  The object and the tag length are configured accordingly.  The operating object has the cursor focus. |
| Parameter set control | The parameter set has the cursor focus. |
| Browser | The operating object has the cursor focus. |
| Runtime dialogs which support keyboard entry | The dialog is open and the corresponding input field has the cursor focus. |
| File browser | The field "File path" has the cursor focus. |

### Result

The code is read and entered into the corresponding input field.
