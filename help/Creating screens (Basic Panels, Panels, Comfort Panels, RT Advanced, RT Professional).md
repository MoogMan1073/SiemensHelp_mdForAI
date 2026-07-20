---
title: "Creating screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: ScreensWCCPenUS
topics: 345
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Creating screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with objects and object groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-objects-and-object-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with text lists and graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-text-lists-and-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamizing screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-function-keys-basic-panels-panels-comfort-panels-rt-advanced)
- [Working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-faceplates-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Display and operating elements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#display-and-operating-elements-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
- [Screen basics (RT Professional)](#screen-basics-rt-professional)
- [Device-dependent functional scope of screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependent-functional-scope-of-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Elements and basic settings (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#elements-and-basic-settings-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)
- [Working with pop-up screens (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-pop-up-screens-basic-panels-panels-comfort-panels-rt-advanced)
- [Working with slide-in screens (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-slide-in-screens-basic-panels-panels-comfort-panels-rt-advanced)
- [Working with designs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-designs-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with styles and style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-styles-and-style-sheets-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

In WinCC you create screens that an operator can use to control and monitor machines and plants. When you create your screens, the object templates included support you in visualizing processes, creating images of your plant, and defining process values.

#### Application example

The figure shows a screen that was created in WinCC. With the help of this screen, the operator can operate and monitor the mixing station of a fruit juice manufacturing system. Fruit juice base is supplied from various tanks to a mixing unit. The screen indicates the fill level of the tanks.

![Application example](images/9486884875_DV_resource.Stream@PNG-en-US.png)

#### Screen design

Insert an object you need to represent a process into your screen. Configure the object to correspond to the requirements of your process.

A screen may consist of static and dynamic elements.

- Static elements such as text or graphic objects do not change their status in runtime. The tank labels (W, K, Z, A) shown in this example of a mixing unit are static elements.
- Dynamic elements change their status based on the process. Visual current process values as follows:

  - From the memory of the PLC
  - From the memory of the HMI device in the form of alphanumeric displays, trends and bars.

  Input fields on the HMI device are also considered dynamic objects. The fill level values of the tanks in our example of a mixing plant are dynamic objects.

Process values and operator inputs are exchanged between the controller and the HMI device via tags.

#### Screen properties

The screen layout is determined by the features of the HMI device you are configuring. It corresponds with the layout of the user interface of this device. If the set HMI device has function keys, the screen shows these function keys. Other properties such as the screen resolution, fonts and colors are also determined by the characteristics of the selected HMI.

#### Function keys

A function key is a key on the HMI device to which you can assign one or several functions in WinCC. The functions are triggered as soon as the operator presses the key on the HMI device.

A function key can be assigned global or local functions:

Global function keys always trigger the same action, regardless of the currently displayed screen.

Local function keys trigger different actions depending on the currently displayed screen on the HMI device. This assignment applies only to the screen in which you have defined the function key.

#### Navigation

You configure a screen navigation to enable the operator to call a screen on the HMI device in Runtime.

- The "Screen" editor is used to configure buttons for calling other screens.

- You use the "Global Screen" editor to configure globally assigned function keys.

---

**See also**

[Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-of-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Screen basics (RT Professional)](#screen-basics-rt-professional)
  
[Device-dependent functional scope of screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependent-functional-scope-of-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Task cards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#task-cards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of objects (RT Professional)](#overview-of-objects-rt-professional)
  
[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on dynamizing screens (Basic Panels)](#basics-on-dynamizing-screens-basic-panels)
  
[Basics on libraries (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-on-libraries-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[Print job/script diagnostics (RT Professional)](#print-jobscript-diagnostics-rt-professional)
  
[Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)

### Screen basics (RT Professional)

#### Introduction

In WinCC you create screens that an operator can use to control and monitor machines and plants. When you create your screens, the object templates included support you in visualizing processes, creating images of your plant, and defining process values.

#### Application example

The figure shows a screen that was created in WinCC. With the help of this screen, the operator can operate and monitor the mixing station of a fruit juice manufacturing system. Fruit juice base is supplied from various tanks to a mixing unit. The fill levels of the tanks are indicated.

![Application example](images/9486884875_DV_resource.Stream@PNG-en-US.png)

#### Screen design

Insert an object you need to represent a process into your screen. Configure the object to correspond to the requirements of your process.

A screen may consist of static and dynamic elements:

- Static elements such as text or graphic objects in the screen above do not change their status in Runtime. The tank labels (W, K, Z, A) shown in this example of a mixing unit are static elements.
- Dynamic elements change their status based on the process. Visual current process values as follows:

  - From the memory of the PLC
  - From the memory of the HMI device in the form of alphanumeric displays, trends and bars.

  Input fields on the HMI device are also considered dynamic objects. The fill level values of the tanks in our example of a mixing plant are dynamic objects.

Process values and operator inputs are exchanged between the controller and the HMI device via tags.

#### Navigation

You configure a screen navigation to enable the operator to call a screen on the HMI device in Runtime.

- You use the "Menus & Toolbars" editor to configure the navigation between the screens.
- The "Screen" editor is used to configure buttons for calling other screens.

---

**See also**

[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Device-dependent functional scope of screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependent-functional-scope-of-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Device-dependent functional scope of screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The functions of an HMI device determine the display of the device in WinCC and the scope of functions of the editors.

The following screen properties are determined by the functions of the selected HMI device:

- Device layout
- Screen resolution
- Number of colors
- Fonts
- Objects available

#### Device layout

The device layout of a screen forms the image of the HMI device in your configuration. The device layout of the screen shows all the function keys available on the HMI device, for example.

#### Screen resolution

The screen resolution is determined by the different display dimensions of the various operator panels. You can only change the screen resolution if you configure the "WinCC Runtime Advanced" or "WinCC Runtime Professional" HMI device.

#### Number of colors

You can assign colors to the screen objects. The number of possible colors is determined by the color depth and specific colors supported on the selected HMI device.

#### Fonts

You can customize the appearance of the texts in all the screen objects that contain static or dynamic text. How to highlight individual texts in a screen. Select the font, font style and size, and set additional effects such as underscoring, for example.

![Fonts](images/87574025739_DV_resource.Stream@PNG-en-US.png)

The settings for the text markups such as font style and effects always refer to the entire text of a screen object. That is, you can display the complete title in bold format, but not its individual characters or words, for example.

#### Objects available

Some of the screen objects can not be configured globally for all HMI devices. These screen objects are not displayed in the "Tools" task card. For a KTP 1000 touch panel unit you can not configure a slider, for example.

---

**See also**

[Screen basics (RT Professional)](#screen-basics-rt-professional)

### Elements and basic settings (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Task cards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#task-cards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Zooming the view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#zooming-the-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Moving the view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-the-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Task cards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The following task cards are available in the "Screens" editor:

- Toolbox: Display and operating objects
- Animations: Templates for dynamic configuration
- Layout: Aid for customizing the display
- Libraries: Administration of the project library and of the global libraries

  > **Note**
  >
  > **WinCC Basic**
  >
  > The "Animations" task card is not available in WinCC Basic.

##### Toolbox

The "Toolbox" task card contains objects in different panes:

- Basic objects
- Elements
- Controls
- User controls (optional)
- Graphics

You paste objects from the palettes into your screens by drag&drop or a double click. The objects available for selection are determined by the features of the HMI device you are configuring. The following icons are used to change the display mode:

| Icon | Meaning |
| --- | --- |
| ![Toolbox](images/25697189515_DV_resource.Stream@PNG-de-DE.png) | Displays the objects as a list. |
| ![Toolbox](images/25697193355_DV_resource.Stream@PNG-de-DE.png) | Displays the objects as a graphic. |

##### Animations

The "Animations" task card contains the possible dynamizations of a screen object in the palettes. You paste the animations to a screen object by drag&drop or a double click from the "Movements", "Display" and "Tag Binding" palettes.

##### Layout

The "Layout" task card contains the following panes for displaying objects and elements:

- Layers: Serves to manage screen object layers The layers are displayed in a tree view and contain information about the active layer and the visibility of all layers.
- Grid: You specify whether you want to align the objects to a grid or to other objects and set the grid size for a grid.
- Objects out of range: Objects that lie outside the visible area are displayed with name, position and type.

##### Libraries

The "Libraries" task card show the following libraries in separate panes:

- Project library: The project library is stored together with the project.
- Global library: The global library is stored in a separate file in the specified path on your configuration PC.

---

**See also**

[Zooming the view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#zooming-the-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Moving the view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-the-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)

#### Zooming the view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To view a small screen section in closer detail, use the zoom tool to magnify the screen in the working area. The maximum zoom amounts to 800%.

You can zoom with the toolbar in the work area or with the "Layout > Zoom" task card.

There are different ways to increase the screen, for example, with the zoom factor or by adapting the work area to the height of the screen.

##### Requirement

The screen is opened.

##### Procedure

Proceed as follows to zoom a view with the selection frame:

1. Click the ![Procedure](images/14136619275_DV_resource.Stream@PNG-de-DE.png) toolbar button.
2. Use the mouse to draw a selection frame in the screen.

After you have released the mouse button, the section enclosed by the selection frame is zoomed to fit the complete work area.

Alternatively, use the slider in the lower right-hand corner of the screen.

##### Result

The selected screen section is magnified.

---

**See also**

[Task cards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#task-cards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Moving the view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To display only a section of the entire screen in the work area, use the ![Introduction](images/14135827467_DV_resource.Stream@PNG-de-DE.png) icon of the "Screens" editor:

##### Requirement

- A screen is open.
- The view shows only a screen section.

##### Procedure

To move the view:

1. Click the ![Procedure](images/14135827467_DV_resource.Stream@PNG-de-DE.png) icon at the bottom right corner of the work area and press the left mouse button.

   A miniature view of the full screen is shown. An orange frame shows the currently selected area.
2. Hold down the mouse button and drag the frame to the desired area.

**Note**

The screen is scrolled when you drag a screen object from the visible to a currently hidden section.

---

**See also**

[Task cards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#task-cards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Working with screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)
- [Steps (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#steps-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating a new screen (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-new-screen-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating a new screen (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-new-screen-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing screens (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-screens-basic-panels-panels-comfort-panels-rt-advanced)
- [Defining the start screen of the project (Basic Panels, Panels, Comfort Panels, RT Advanced)](#defining-the-start-screen-of-the-project-basic-panels-panels-comfort-panels-rt-advanced)
- [Defining the start screen of the project (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-start-screen-of-the-project-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Changing the screen resolution (RT Advanced)](#changing-the-screen-resolution-rt-advanced)

#### Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Steps

To create screens, you need to take the following initial steps:

- Plan the structure of the process visualization: Number of screens and their layout

  Example: Subprocesses are visualized in separate screens, and merged in a master screen.
- Define your screen navigation control strategies.
- Adapt the templates and the global screen.

  You define objects centrally and assign function keys for example.
- Create the screens. Use the following options of efficient screen creation:

  - Working with libraries
  - Working with layers
  - Working with faceplates

---

**See also**

[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#steps-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a new screen (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-new-screen-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing screens (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-screens-basic-panels-panels-comfort-panels-rt-advanced)
  
[Defining the start screen of the project (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-start-screen-of-the-project-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)
  
[Task cards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#task-cards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Steps (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Steps

To create screens, you need to take the following initial steps:

- Plan the structure of the process visualization: Number of screens and their layout Example: Subprocesses are visualized in separate screens, and merged in a master screen.
- Define your screen navigation control strategies.

  Create the menus and toolbars to navigate between the screens.
- Create the screens. Use the following options to achieve efficient screen configuration:

  - Working with libraries
  - Working with faceplates
  - Working with layers
  - Working with designs

---

**See also**

[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)

#### Creating a new screen (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Create screens to display processes in your system.

##### Requirement

- The project has been created.
- The Inspector window is open.

##### Procedure

1. Double-click "Screens > Add New Screen" in the project navigation.

   The screen is generated in the project and appears in your view. The screen properties are shown in the Inspector window.
2. Enter a meaningful name for the screen.
3. Configure the screen properties in the Inspector window:

   - Specify whether and on which template the screen is based.
   - Set the "Background Color" and the "Screen Number."
   - Specify a documenting text under "Tooltip".
   - Specify the layers to be displayed under "Layers" in the engineering system.
   - Select dynamic screen update under "Animations."
   - Select "Events" to define which functions you want to execute in Runtime when you call and exit the screen or at other events.

**Note**

Not all HMI devices support the "Visibility" animation.

##### Result

You created the screen in your project. You can now paste objects and control elements from the "Tools" task card and assign function keys in further work steps.

---

**See also**

[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)

#### Creating a new screen (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Create screens to display processes in your system.

##### Requirement

- The project has been created.
- The Inspector window is open.

##### Procedure

To create a new screen:

1. Double-click "Screens > Add New Screen" in the project tree.

   The screen is generated in the project and appears in your view. The screen properties are shown in the Inspector window.
2. Enter a meaningful name for the screen, such as "Overview_Diagram."

   Do not use the special characters ?, . , ", /, \, *, <, >

   This name is language-neutral.
3. If required, enter a descriptive display name. The name is language-specific and can be translated for the required languages. You can output the display name in a text field with the SetPropertyByProperty system function, for example.
4. Configure the screen in the Inspector window:

   - Set the background color and the grid color under "General."
   - Specify a tooltip providing additional information.
   - Specify the size of the screen under "Layout."
   - Define the pattern and the color of a fill pattern under "Appearance."
   - Specify the layers to be displayed under "Layers" in the engineering system.
   - Specify the tab sequence for activating the screen objects and selecting the objects to be activated under "Miscellaneous."
   - Under "Hide/Show" specify whether a size to be defined is used to determine the display for layers and/or objects.
   - Dynamize the display and operating objects under "Animations."
   - Select "Events" to define which functions you want to execute in runtime when you call and exit the screen or at other events.

##### Result

You created the screen in your project. You can now paste objects and control elements from the "Toolbox" task card in further work steps.

---

**See also**

[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)

#### Managing screens (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You can move screens within a project to other groups, or copy, rename, and delete them.

##### Moving screens in a group

1. Select the "Screens" folder in the project tree.
2. Select the "Add group" command from the shortcut menu.

   A folder called "Group_x" is inserted.
3. Select the screen in the project tree.
4. Drag-and-drop the screen to the required group.

   The screen is moved into this group.

##### Copy screen

1. Select the screen in the project tree.
2. Select the "Copy" command in the shortcut menu to copy the screen to the clipboard.
3. In the project tree, select the screen insert position.
4. Select "Paste" from the shortcut menu to insert the screen.

   A copy of the screen is inserted. A consecutive number is appended to the name of the original in the copy.

Alternatively, press <Ctrl> while you drag the screen to the required position.

> **Note**
>
> If you copy a screen with interconnected template for several devices and projects, the template will also be copied. Any existing matching template is not used. This holds particularly true when you copy the screens with drag-and-drop.

##### Rename screen

1. Select the screen in the project tree.
2. Select "Rename" from the shortcut menu.
3. Type in a new name.
4. Press <Enter>.

As an option, use the <F2> function key to rename the screen.

##### Delete screen

1. Select the screen in the project tree.
2. Select "Delete" from the shortcut menu.

   The screen and all its objects are deleted from the current project.

---

**See also**

[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)

#### Defining the start screen of the project (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

The start screen is the initial screen opened at the start of project in Runtime. You can define a different start screen for each one of the HMI devices. Beginning at this start screen, the operator calls the other screens.

##### Requirement

The project contains the screen you want to use as the start screen.

##### Procedure

1. Double-click "Runtime settings > General" in the project tree.

   ![Procedure](images/87575376651_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/87575376651_DV_resource.Stream@PNG-en-US.png)
2. Select the desired screen as "Start screen".

Alternatively select a screen in the project tree and select "Define as start screen" in the shortcut menu.

##### Result

The start screen opens on the HMI at the start of Runtime.

---

**See also**

[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)

#### Defining the start screen of the project (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The start screen is the initial screen opened at the start of project in Runtime. You can define a different start screen for each one of the HMI devices. Beginning at this start screen, the operator calls the other screens.

##### Requirement

The project contains the screen you want to use as the start screen.

##### Procedure

1. Double-click "Runtime settings > General" in the project tree.

   ![Procedure](images/60721519371_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/60721519371_DV_resource.Stream@PNG-en-US.png)
2. Select the desired screen as "Start screen".

Alternatively select a screen in the project tree and select "Define as start screen" in the shortcut menu.

##### Result

The start screen opens on the HMI at the start of Runtime.

#### Changing the screen resolution (RT Advanced)

You change the screen resolution in the Runtime settings of the HMI device.

The screen resolution can be configured for the following HMI devices:

- RT Advanced

##### Configuring a fixed screen resolution

1. Open the Runtime settings of the HMI device.
2. Select the screen resolution under "General > Screen > Screen resolution".

   ![Configuring a fixed screen resolution](images/74946779787_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a fixed screen resolution](images/74946779787_DV_resource.Stream@PNG-en-US.png)

### Working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)
- [Global screen (Basic Panels, Panels, Comfort Panels, RT Advanced)](#global-screen-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating a new template (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-new-template-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring permanent areas in the template (Panels, Comfort Panels, RT Advanced)](#configuring-permanent-areas-in-the-template-panels-comfort-panels-rt-advanced)
- [Managing a template (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-a-template-basic-panels-panels-comfort-panels-rt-advanced)
- [Using a template in the screen (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-a-template-in-the-screen-basic-panels-panels-comfort-panels-rt-advanced)

#### Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Configure the objects in a template which are to be displayed in all screens based on this template.

Note the following rules:

- A screen must not be based on a template.
- A screen is only based on one template.
- You can create several templates for one device.
- A template cannot be based on another template.

##### Objects for a template

You determine functions and objects in the template which are to apply for all screens based on this template:

- Assignment of function keys: You also assign the function keys in the template for HMI devices with function keys. This assignment overwrites a possible global assignment.
- Permanent areas: Some devices support a permanent area for all screens in the top area of the screen. In contrast to the template, the permanent area occupies an area of the screen for itself alone.
- Operator controls: You can paste all screen objects which you also use for a screen into a template.

##### Application examples

- You want to assign the ActivateScreen" function to a function key in the template. The operator uses this key to switch to another screen in runtime. This configuration applies to all screens that are based on this template.
- A graphic with your company logo can be added to the template. The logo appears on all screens that are based on this template.

  > **Note**
  >
  > If an object from the template has the same position as an object in the screen, the template object is covered.

---

**See also**

[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Steps (Basic Panels, Panels, Comfort Panels, RT Advanced)](#steps-basic-panels-panels-comfort-panels-rt-advanced)
  
[Task cards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#task-cards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a new template (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-new-template-basic-panels-panels-comfort-panels-rt-advanced)
  
[Managing a template (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-a-template-basic-panels-panels-comfort-panels-rt-advanced)
  
[Using a template in the screen (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-a-template-in-the-screen-basic-panels-panels-comfort-panels-rt-advanced)
  
[Global screen (Basic Panels, Panels, Comfort Panels, RT Advanced)](#global-screen-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring permanent areas in the template (Panels, Comfort Panels, RT Advanced)](#configuring-permanent-areas-in-the-template-panels-comfort-panels-rt-advanced)

#### Global screen (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You define global elements for all screens of an HMI device independently of the used template.

##### Function keys

For HMI devices with function keys you assign the function keys globally in the "Global Screen" editor. This global assignment applies for all screens of the HMI device.

Proceed as follows to assign function keys locally in screens or templates:

1. Click the function key in your screens or templates.
2. Deactivate "Properties > Properties > General > Use Global Assignment" in the inspection window.

##### Indicator and control objects for alarms

The "Alarm window" and "Alarm indicator" objects that are available as global objects are configured within the "Global screen" editor.

The "Alarm window" and "Alarm indicator" are always shown in the foreground.

For Comfort Panels you also have the possibility of configuring a "System diagnostic view" in the global screen.

> **Note**
>
> If you have configured a permanent area in a template, do not position the alarm window and alarm indicator in the area of the permanent area. Otherwise, the alarm window and the alarm indicator will not be displayed in Runtime.
>
> However, the permanent area is not visible in the "Global screen" editor.

##### Order of configuration of screens

The following order applies for the configuration:

- The global screen comes before screens and templates
- Screens come before templates

  ![Order of configuration of screens](images/23649276939_DV_resource.Stream@PNG-en-US.png)

The system layer is not configurable. This contains

- input dialog boxes
- alarms from the operating system
- the direct keys for touch panels

---

**See also**

[Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)

#### Creating a new template (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In a template, you can centrally modify objects and function keys. Changes to an object or of a function key assignment in the template are applied to the object in all the screens which are based on this template.

> **Note**
>
> **HMI device dependency**
>
> Function keys are not available on all HMI devices.

##### Requirement

- The project has been created.
- The Inspector window is open.

##### Procedure

1. Select "Screen management > Templates" in the project tree and then double-click "Add new template".

   The template is created in the project, and appears in your view.

   The properties of the template are displayed in the Inspector window.
2. Define the name of the template under "Properties > Properties > General" in the Inspector window.
3. Specify the layers in the engineering system that are displayed under "Properties >Properties >Layers" in the Inspector window.
4. Add the necessary objects from the "Tools" task card.
5. Configure the function keys.

##### Result

The template is created in your project.

---

**See also**

[Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)

#### Configuring permanent areas in the template (Panels, Comfort Panels, RT Advanced)

##### Introduction

In the permanent area, you configure objects which are visible in all screens. In contrast to the template, the permanent area occupies an area of the screen for itself alone.

You can configure permanent areas in a template or in a screen. In the project tree, the permanent area is available under "Screen management > Permanent area".

##### Configuring permanent areas

To configure a permanent area, follow these steps:

1. Open a template for a HMI device with a permanent area.
2. Using the mouse (cursor form: ![Configuring permanent areas](images/14137122443_DV_resource.Stream@PNG-de-DE.png)), drag the top edge of the editable screen area downwards.

   ![Configuring permanent areas](images/14769887883_DV_resource.Stream@PNG-de-DE.png)

   ![Configuring permanent areas](images/14769887883_DV_resource.Stream@PNG-de-DE.png)
3. Configure the desired objects within the permanent area.

The default height of the permanent area is "0". The maximum height is the maximum height of the screen minus 10 pixels.

##### Result

The content of the permanent area is shown on every screen and in the template. The area above this line is now used as a permanent area in all the screens of the HMI device. Objects already configured in the screens are moved down by the height of the permanent area.

---

**See also**

[Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)

#### Managing a template (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You can move, copy, rename, and delete templates within a project in the Project window.

##### Moving a template into a group

1. Select the templates in the project navigation "Screen management > Templates".
2. Select "Add group" in the shortcut menu.

   A folder called "Group_x" is inserted.
3. Select the template in the project navigation.
4. Drag-and-drop the template to the required group.

   The template is moved to this group.

##### Copying templates

1. Select the template in the project navigation.
2. Select "Copy" in the shortcut menu.
3. Select the position in the project navigation where you want to paste the template.
4. Select "Paste" from the shortcut menu to insert the template.

   A unique name is assigned automatically to the copy.

Alternatively, you can hold down the <Ctrl> key, and drag the template into position.

##### Deleting a template

1. In the project navigation, select the template to be deleted.
2. Select "Delete" in the shortcut menu.

   The template, and all its objects are deleted from the current project.

##### Assigning a template to a screen

1. In the project navigation, select the screen to which you want to assign the template.
2. In the Inspector window, select "Properties > Properties > General".
3. Select the desired template under "Template."

   The selected template and all the objects contained in it are assigned to the screen.

---

**See also**

[Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)

#### Using a template in the screen (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You use a template in the screen. All the objects configured in the template are also available in the screen.

##### Requirement

A template has been created.

A screen has been created.

##### Procedure

Proceed as follows to use a template in a screen:

1. Double click a screen in the project tree. The screen opens in the work area.
2. Open "Properties > Properties > General" in the inspector window.
3. Select a template that is to be applied to the screen under "Template".

##### Show template in screen

When you edit a screen, you can show an existing template in the screen.

Proceed as follows to show a template in the screen:

1. Activate "Extras > Settings > Visualization > Show template in screens" in the menu.

##### Result

The screen is based on the selected template. All objects which you have configured in the template are available in the screen. The template is displayed in the screen.

---

**See also**

[Basics on working with templates (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-templates-basic-panels-panels-comfort-panels-rt-advanced)

### Working with pop-up screens (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics for working with pop-up screens (Panels, Comfort Panels, RT Advanced)](#basics-for-working-with-pop-up-screens-panels-comfort-panels-rt-advanced)
- [Creating a new pop-up screen (Panels, Comfort Panels, RT Advanced)](#creating-a-new-pop-up-screen-panels-comfort-panels-rt-advanced)
- [Managing pop-up screens (Panels, Comfort Panels, RT Advanced)](#managing-pop-up-screens-panels-comfort-panels-rt-advanced)
- [Using the pop-up screen (Panels, Comfort Panels, RT Advanced)](#using-the-pop-up-screen-panels-comfort-panels-rt-advanced)

#### Basics for working with pop-up screens (Panels, Comfort Panels, RT Advanced)

##### Introduction

You use the pop-up screen to configure a screen for additional content, for example, object settings. The pop-up screen is displayed on top of the current screen as soon as you call a system function.

Only one pop-up screen at a time is displayed in a screen.

> **Note**
>
> **Device dependency of the "Pop-up screen" object**
>
> The "Pop-up screen" object is only available for KTP Mobile Panels, Comfort Panels and RT Advanced.

##### Use

You configure a button in the screen and assign the "ShowPopupScreen" or "ShowPopupScreenSizable" function in order to display a pop-up screen with a defined size.

When operating the button, a pop-up screen is opened or closed. In the pop-up screen, you make the settings.

##### Size

You have the option to configure pop-up screens that are larger than the screen size:

- Horizontal, up to maximum double the width
- Vertical, up to maximum six times the height

##### Objects in the pop-up screen

You configure the following objects in the pop-up screen:

- Basic objects, such as lines and polygon-based objects
- Elements, such as buttons
- Controls, such as trend view or alarm view
- Faceplates

> **Note**
>
> You cannot configure alarm windows, system diagnostics windows and alarm indicators in the pop-up screen.
>
> Softkeys and hotkeys are not supported in the "Pop-up screen" object.

> **Note**
>
> Objects in the pop-up screen as well as the pop-up screen itself do not support access with VB scripting.

#### Creating a new pop-up screen (Panels, Comfort Panels, RT Advanced)

##### Introduction

A new pop-up screen is created in Project tree > Screen management. The size of a pop-up screen is defined in the properties.

##### Requirements

- The project has been created.
- The Inspector window is open.

##### Creating a new pop-up screen

1. Double-click "Screen management > Pop-up screens > Add new pop-up screen" in the project tree.

   The pop-up screen is generated in the project and is displayed in the work area.

   The pop-up screen properties are displayed in the Inspector window.
2. Define the name of the pop-up screen under "Properties > Properties > General" in the Inspector window.
3. Specify the layers in the engineering system that are displayed under "Properties >Properties >Layers" in the Inspector window.
4. Define the height and width of the pop-up screen under "Properties > Properties > Layout" in the Inspector window.
5. Define the color for the scroll arrows and the sizing handle in the scroll bar in "Properties > Properties > Scroll bar" in the Inspector window.
6. Add the necessary objects from the "Tools" task card.
7. Configure the function keys.

**Note**

You cannot address the "Pop-up screen" object and the objects configured in it with VB scripts.

**Note**

Objects and controls can be dynamized in the pop-up screen. The pop-up screen itself does not support dynamization.

##### Result

You have created a new pop-up screen in which you have configured objects and functions.

#### Managing pop-up screens (Panels, Comfort Panels, RT Advanced)

##### Introduction

You can move, copy, rename, and delete pop-up screens within a project in the Project window.

##### Moving pop-up screens in a group

1. Select "Screen management > Pop-up screens" in the project tree.
2. Select "Add group" in the shortcut menu.

   A folder called "Group_x" is inserted.
3. Select the pop-up screen in the project tree.
4. Drag-and-drop the pop-up screen to the required group.

   The pop-up screen is moved into this group.

##### Copying pop-up screen

1. Select the pop-up screen in the project tree.
2. Select "Copy" from the shortcut menu.
3. In the project tree, select the pop-up screen insert position.
4. Select "Paste" in the shortcut menu.

   A unique name is assigned automatically to the copy.

##### Deleting pop-up screen

1. Select the pop-up screen you want to delete in the project tree.
2. Select "Delete" in the shortcut menu.

   The pop-up screen and all its objects are deleted from the current project.

#### Using the pop-up screen (Panels, Comfort Panels, RT Advanced)

##### Introduction

You configure the system function to open a pop-up screen at the event of an operating object. The linked system function is executed when the event occurs in runtime.

> **Note**
>
> You configure a button to open a pop-up screen in a slide-in screen.
>
> If the configured position of the pop-up screen is outside the slide-in screen, the slide-in screen is closed when the pop-up screen closes.

##### Requirements

- A pop-up screen has been configured.
- A screen is open.
- The Inspector window is open.

##### Procedure

1. Configure a button.
2. Click "Properties > Events" in the Inspector window.
3. Select an event, for example, "Click".
4. Click on "Add function" in the table.
5. Select the "ShowPopupScreen" system function.

##### Result

The pop-up screen opens when the operator clicks the button in runtime.

### Working with slide-in screens (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics on working with slide-in screens (Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-slide-in-screens-panels-comfort-panels-rt-advanced)
- [Configuring slide-in screens (Panels, Comfort Panels, RT Advanced)](#configuring-slide-in-screens-panels-comfort-panels-rt-advanced)
- [Configuring slide-in screens for devices without multi-touch function (Panels, Comfort Panels, RT Advanced)](#configuring-slide-in-screens-for-devices-without-multi-touch-function-panels-comfort-panels-rt-advanced)
- [Using slide-in screens (Panels, Comfort Panels, RT Advanced)](#using-slide-in-screens-panels-comfort-panels-rt-advanced)

#### Basics on working with slide-in screens (Panels, Comfort Panels, RT Advanced)

##### Introduction

The "Slide-in screen" object provides quick navigation between the start screen and the slide-in screens containing additional configured contents stored outside the start screen. Navigation is supported by the multi-touch functions. The configurable handles appearing at the edges of the start screen provide quick access to the stored slide-in screens.

The size of the slide-in screens depends on the HMI device used.

> **Note**
>
> **Device dependency of the "Slide-in screen" object**
>
> The "Slide-in screen" object is only available for KTP Mobile Panels, Comfort Panels and RT Advanced.

##### Application

The "Slide-in screen" is used to configure up to four slide-in screens for additional contents and operator controls, for example, a virtual keyboard or a system dialog.

By default, the following slide-in screens are set up for each device:

- "Slide-in screen top": appears at the top of the start screen in Runtime
- "Slide-in screen bottom": appears at the bottom of the start screen in Runtime
- "Slide-in screen left": appears at the left of the start screen in Runtime
- "Slide-in screen right": appears at the right of the start screen in Runtime

It is possible to configure objects in each of these slide-in screens.

![Application](images/100707395211_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> It is not possible to delete the default slide-in screens or to set up your own slide-in screens.

##### Objects in the slide-in screen

You configure the following objects in the slide-in screen:

- Basic objects, such as lines and polygon-based objects
- Elements, such as buttons
- Controls, such as trend view or alarm view
- Faceplates

> **Note**
>
> Objects in the slide-in screen as well as the slide-in screen itself do not support access with VB scripting.

> **Note**
>
> Release buttons and locked operator controls cannot be configured in the slide-in screen.
>
> Softkeys and hotkeys are not supported in the slide-in screen.

---

**See also**

[Configuring slide-in screens (Panels, Comfort Panels, RT Advanced)](#configuring-slide-in-screens-panels-comfort-panels-rt-advanced)
  
[Configuring slide-in screens for devices without multi-touch function (Panels, Comfort Panels, RT Advanced)](#configuring-slide-in-screens-for-devices-without-multi-touch-function-panels-comfort-panels-rt-advanced)
  
[Using slide-in screens (Panels, Comfort Panels, RT Advanced)](#using-slide-in-screens-panels-comfort-panels-rt-advanced)

#### Configuring slide-in screens (Panels, Comfort Panels, RT Advanced)

##### Introduction

By default, four slide-in screens are preset for each device in the project tree under "Screen management > Slide-in screens". For each of these slide-in screens, you configure the size, the layout and the handle for operation in Runtime using the properties.

##### Requirement

- The project has been created.
- An HMI device has been created.
- The Inspector window is open.

##### Configuring properties for slide-in screens

1. Select the slide-in screen you wish to configure in the project tree under "Screen management > Slide-in screens.

   The slide-in screen properties are displayed in the Inspector window.
2. Define the background color of the slide-in screen in the "Background color" selection list of the "Properties > Properties > General" Inspector window.
3. Define the grid color of the slide-in screen in the "Grid color" selection list.
4. Enable the "Activate" check box.
5. Specify the layers in the engineering system that are displayed under "Properties >Properties >Layers" in the Inspector window.
6. Define the height and width of the slide-in screen in "Properties > Properties > Layout" in the Inspector window:

   - Define the height only for "Slide-in screen top" and "Slide-in screen bottom".
   - Define the width only for "Slide-in screen left" and "Slide-in screen right".

**Note**

The names of all slide-in screens are write-protected and cannot be changed.

> **Note**
>
> If you do not need all four slide-in screens, enable the slide-in screens relevant to you only.
>
> If you do not need any slide-in screens, leave the "Activate" check box empty for all four slide-in screens.

> **Note**
>
> Slide-in screens cannot be deleted nor copied to a different HMI device.
>
> However, it is possible to copy the objects configured in a slide-in screen to another slide-in screen.

##### Configuring handles for slide-in screens

1. Define the color of the first line of the handle in the "Lines" area of the "Color" selection list under "Properties > Properties > Handle" in the Inspector window.
2. Define the color of the second line of the handle in the "Alternative color" selection list.
3. Define the color for the operable area of the handle in the "Color" selection list under "Operable area".
4. Select one of the following options from the "Visibility" area:

   - "Hide handle automatically" (activated by default)
   - "Always show handle"
   - "Never show handle"

> **Note**
>
> When selecting the "Hide handle automatically" option, the handle only becomes visible once the user clicks the operable area.
>
> You select the "Never display handle" option when the slide-in screen is configured using the "ShowSlideInScreen" system function.

> **Note**
>
> You are notified by a warning if a handle which is configured as visible covers a configured object in a screen, such as a button, completely or partially.

> **Note**
>
> The following dimensions are defined for the handle:
>
> - The width of a handle for the "Slide-in screen top" and "Slide-in screen bottom" objects is one-third of the screen length.
> - The height of a handle for the "Slide-in screen left" and "Slide-in screen right" objects is one-third of the screen width.

##### Result

You have configured the properties of the slide-in screens and the handle for operation in Runtime.

---

**See also**

[Basics on working with slide-in screens (Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-slide-in-screens-panels-comfort-panels-rt-advanced)

#### Configuring slide-in screens for devices without multi-touch function (Panels, Comfort Panels, RT Advanced)

##### Introduction

You use the "ShowSlideInScreen" system function to make the slide-in screens available on devices without multi-touch functions, for example Key Panels. You link this system function to buttons. Buttons are used to navigate between the start screen and the slide-in screens.

##### Requirement

- The project has been created.
- An HMI device has been created.
- A screen is open.
- The Inspector window is open.

##### Procedure

1. Drag the "Button" object to the screen from the toolbox.
2. Enter a suitable text of any length for the button.
3. In the Inspector window, select "Properties > Events > Click".

   The "Function list" dialog box is opened.
4. Select the "ShowSlideInScreen" system function from the "Keyboard operation for screen objects" group.
5. Assign the ID of the slide-in screen appearing in runtime when the button is operated to the "ShowSlideInScreen" function:

   - "Slide-in screen left"
   - "Slide-in screen top"
   - "Slide-in screen right"
   - "Slide-in screen bottom"
6. Assign the appropriate mode to the "ShowSlideInScreen" function:

   - "Toggle"
   - "Off"
   - "On"

**Note**

Navigation in Runtime is much easier if the buttons for operating the slide-in screens are created directly in the start screen.

##### Result

You have configured the slide-in screens for operation on devices without multi-touch function. When clicking on the respective button in the screen in Runtime, the slide-in screen behaves in accordance with the configuration.

---

**See also**

[Basics on working with slide-in screens (Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-slide-in-screens-panels-comfort-panels-rt-advanced)

#### Using slide-in screens (Panels, Comfort Panels, RT Advanced)

##### Introduction

In slide-in screens, you configure additional contents and operator controls, for example, navigation buttons, an alarm view or a trend view.

##### Requirements

- The project has been created.
- An HMI device has been created.
- A slide-in screen is open.
- The Inspector window is open.

##### Procedure

1. Add the necessary objects from the "Tools" task card to the slide-in screen.
2. Configure the function keys.

> **Note**
>
> You cannot address the "Slide-in screen" object and the objects configured in it with VB scripts.

> **Note**
>
> Objects and controls can be dynamized in the slide-in screens. The slide-in screens as such do not support dynamization.

##### Result

You have configured objects and functions in the slide-in screen.

---

**See also**

[Basics on working with slide-in screens (Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-slide-in-screens-panels-comfort-panels-rt-advanced)

### Working with designs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)
- [Designs editor (RT Professional)](#designs-editor-rt-professional)
- [Creating a design (RT Professional)](#creating-a-design-rt-professional)
- [Changing a design (RT Professional)](#changing-a-design-rt-professional)
- [Deleting a design (RT Professional)](#deleting-a-design-rt-professional)
- [Applying a design (RT Professional)](#applying-a-design-rt-professional)
- [Specifying the basic design user interface of an HMI device (RT Professional)](#specifying-the-basic-design-user-interface-of-an-hmi-device-rt-professional)
- [Applying design templates to screens (RT Professional)](#applying-design-templates-to-screens-rt-professional)
- [Using design templates for basic objects and elements (RT Professional)](#using-design-templates-for-basic-objects-and-elements-rt-professional)
- [Applying design templates to controls (RT Professional)](#applying-design-templates-to-controls-rt-professional)
- [Use default design (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#use-default-design-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics on working with designs (RT Professional)

##### What are designs?

Designs are templates for displaying screens and the objects configured there. A design contains, for example, color specifications for foreground, border line, text, etc..

The design is applied to the following objects:

- Screens
- Menus and toolbars
- Screen objects

##### Application

To design the user interfaces of several HMI devices in a uniform layout, assign the same design to each HMI device.

You can modify the layout of screens and objects by customizing the current design to suit your requirements. The new design is activated automatically for all screens and objects of the HMI device.

##### Managing designs

You manage designs in the "Designs" editor.

WinCC features a number of predefined designs such as "WinCC Classic" for user interfaces in the classic WinCC layout and "WinCC Glass" for user interfaces in the style of Windows Vista. Predefined designs cannot be deleted or changed.

##### Pre-defined global designs

WinCC provides the following designs for the projects:

- WinCC Dark (standard design)

  Design in dark gray to black shades with relief-like 3D design of the objects.
- WinCC 3D

  Design in gray tones with relief-like 3D design of the objects.
- WinCC Glass

  Design in blue shades with a glass-like shimmer effect.
- WinCC Simple

  Simple design in light blue shades.
- WinCC Ocean

  Dark design in blue-green shades with its own central color palette.
- WinCC Retro

  The design imitates the appearance of "WinCC Classic". The functionality corresponds to the other WinCC designs from WinCC V7.
- WinCC Classic (migrated projects)

  WinCC V6.2 standard design available for migrated projects for compatibility reasons.

  The design supports only a part of the functions that were introduced as of WinCC V7.0: For example, you cannot use SVG graphics.

---

**See also**

[Use default design (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#use-default-design-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Designs editor (RT Professional)

##### Introduction

Designs are project-specific. The "Designs" editor is available in the project tree under "Common data".

##### Structure of the "Designs" editor

The "Designs" area lists all designs. The "Preview" area shows how images and objects are displayed with the selected design.

![Structure of the "Designs" editor](images/171491313419_DV_resource.Stream@PNG-en-US.png)

Predefined designs have a gray background and cannot be deleted or modified. The default design is selected in the "Default" column.

Click the desired design in the "Designs" list for a preview of another design. The "Preview" in the right pane is refreshed:

- The first line offers a preview of the menu layout.
- The icons on the left offer a preview of the layout of the toolbar.
- The objects of the "Tools" task card are grouped by basic objects, elements and controls.

You can find detailed information on which layout properties are specified by the design in the Inspector window.

---

**See also**

[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)
  
[Use default design (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#use-default-design-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a design (RT Professional)](#creating-a-design-rt-professional)
  
[Changing a design (RT Professional)](#changing-a-design-rt-professional)
  
[Deleting a design (RT Professional)](#deleting-a-design-rt-professional)

#### Creating a design (RT Professional)

##### Requirement

The "Designs" editor is open.

##### Procedure

Proceed as follows:

1. Click "Add" in the list of designs.

   A new design is created. The WinCC default properties are set for screens, menus, toolbars and objects.
2. Overwrite the suggested name with a meaningful name.
3. Enter a description of the design, e.g. the intended use in the "Comment" column.
4. Configure the design as required.

##### Result

You have created and configured a new design.

---

**See also**

[Designs editor (RT Professional)](#designs-editor-rt-professional)
  
[Changing a design (RT Professional)](#changing-a-design-rt-professional)
  
[Deleting a design (RT Professional)](#deleting-a-design-rt-professional)
  
[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)

#### Changing a design (RT Professional)

##### Requirement

The "Designs" editor is open.

##### Procedure

Proceed as follows:

1. Select the design you wish to change from the list of designs.
2. Make the required changes in the Inspector window.
3. Check the result in the preview.

**Note**

You cannot manipulate the predefined designs of WinCC.

The changes are effective immediately.

---

**See also**

[Designs editor (RT Professional)](#designs-editor-rt-professional)
  
[Creating a design (RT Professional)](#creating-a-design-rt-professional)
  
[Deleting a design (RT Professional)](#deleting-a-design-rt-professional)
  
[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)

#### Deleting a design (RT Professional)

##### Requirement

The "Designs" editor is open.

##### Procedure

Proceed as follows:

- Select "Delete" from the shortcut menu of the desired design.

  > **Note**
  >
  > You cannot manipulate the predefined designs of WinCC.

##### Result

The design is deleted. WinCC assigns the predefined "WinCC Classic" design as the new default design to HMI devices to which the deleted design was assigned as default in the Runtime settings.

---

**See also**

[Designs editor (RT Professional)](#designs-editor-rt-professional)
  
[Creating a design (RT Professional)](#creating-a-design-rt-professional)
  
[Changing a design (RT Professional)](#changing-a-design-rt-professional)
  
[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)

#### Applying a design (RT Professional)

##### Core message

In WinCC, every HMI device is assigned a design as a basic design. The following basic design specifications are applied to all screens of the HMI device:

- Settings relating to the display of the shadow of an object (if "Shadow" is activated for the object)
- Settings relating to the display of elements when the mouse pointer is moved over them (hover effect)
- Settings relating to the layout of menus and toolbars

For the individual screens, elements and controls, you also specify in each case whether the specifications of the basic design or the individual settings are applied in the Inspector window.

---

**See also**

[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)
  
[Designs editor (RT Professional)](#designs-editor-rt-professional)
  
[Use default design (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#use-default-design-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Specifying the basic design user interface of an HMI device (RT Professional)](#specifying-the-basic-design-user-interface-of-an-hmi-device-rt-professional)
  
[Applying design templates to screens (RT Professional)](#applying-design-templates-to-screens-rt-professional)
  
[Using design templates for basic objects and elements (RT Professional)](#using-design-templates-for-basic-objects-and-elements-rt-professional)
  
[Applying design templates to controls (RT Professional)](#applying-design-templates-to-controls-rt-professional)

#### Specifying the basic design user interface of an HMI device (RT Professional)

##### Procedure

To change the basic design of the user interface of an HMI device, follow the steps below:

1. Open the "Runtime settings" of the HMI device.
2. Under "General > Settings", specify whether the default design or a different design is used as the basic design.

---

**See also**

[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)
  
[Applying a design (RT Professional)](#applying-a-design-rt-professional)
  
[Applying design templates to screens (RT Professional)](#applying-design-templates-to-screens-rt-professional)
  
[Using design templates for basic objects and elements (RT Professional)](#using-design-templates-for-basic-objects-and-elements-rt-professional)
  
[Applying design templates to controls (RT Professional)](#applying-design-templates-to-controls-rt-professional)

#### Applying design templates to screens (RT Professional)

##### Procedure

Proceed as follows to use design templates for the representation of images on a screen:

1. Open the desired screen in the "Screens" editor.
2. Activate "Properties > Properties > Design > Settings > Use color scheme" in the Inspector window.

##### Result

The settings of the design are applied to the screen.

All the settings that are not predefined by the design are activated and can be changed.

---

**See also**

[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)
  
[Specifying the basic design user interface of an HMI device (RT Professional)](#specifying-the-basic-design-user-interface-of-an-hmi-device-rt-professional)
  
[Applying a design (RT Professional)](#applying-a-design-rt-professional)
  
[Using design templates for basic objects and elements (RT Professional)](#using-design-templates-for-basic-objects-and-elements-rt-professional)
  
[Applying design templates to controls (RT Professional)](#applying-design-templates-to-controls-rt-professional)

#### Using design templates for basic objects and elements (RT Professional)

##### Procedure

To apply the design specifications for the layout of basic elements and elements, proceed as follows:

1. Open the screen in the "Screens" editor.
2. Click the required object in the work area.
3. Select the group settings "Properties > Properties > Designs" in the Inspector window.
4. Activate "Shadow" to visualize the object with a shadow.
5. Activate "Use color scheme" to to apply the default colors of the design.

##### Result

The design settings are applied to the object. In the Inspector window, the fields for setting the background color, frame etc. are deactivated. All the settings that are not predefined by the design are activated and can be changed.

If the "Shadow" option is deactivated in the design, the object is displayed without a shadow in the screen - even if a "shadow" is activated in the object properties.

---

**See also**

[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)
  
[Applying a design (RT Professional)](#applying-a-design-rt-professional)
  
[Specifying the basic design user interface of an HMI device (RT Professional)](#specifying-the-basic-design-user-interface-of-an-hmi-device-rt-professional)
  
[Applying design templates to screens (RT Professional)](#applying-design-templates-to-screens-rt-professional)
  
[Applying design templates to controls (RT Professional)](#applying-design-templates-to-controls-rt-professional)

#### Applying design templates to controls (RT Professional)

##### Procedure

Proceed as follows to apply design templates for visualization of controls:

1. Open the screen in the "Screens" editor.
2. Click the required object in the work area.
3. Deactivate "Properties > Properties > Appearance > Style > Use project settings for design".
4. Select the design from the selection list.

The control is displayed in the style specified in the design.

---

**See also**

[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)
  
[Applying a design (RT Professional)](#applying-a-design-rt-professional)
  
[Specifying the basic design user interface of an HMI device (RT Professional)](#specifying-the-basic-design-user-interface-of-an-hmi-device-rt-professional)
  
[Applying design templates to screens (RT Professional)](#applying-design-templates-to-screens-rt-professional)
  
[Using design templates for basic objects and elements (RT Professional)](#using-design-templates-for-basic-objects-and-elements-rt-professional)

#### Use default design (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

A design is specified as a default design. If you want to design the user interfaces of several HMI devices in a uniform layout, specify the desired design as the default design, and assign it to the HMI devices as the basic design in the Runtime settings "Default design".

If you want to change the layout of the screens and objects, adapt the default design to your requirements or configure a different design as the default design. The latter is the actual advantage of working with the default design: You can practically change the layout for the screens and objects of all the HMI devices at the click of a mouse.

##### Configuring a default design

Proceed as follows:

1. Open the "Designs" editor.
2. Select the desired design in the list of designs in the "Default" column in the work area.

   Or:

   Display a preview of the desired desire in the work area and select "Properties > Properties > General > Design > Default" in the Inspector window.
3. If required, adapt the design to your requirements.

##### Use default design

The default design settings are effective for the objects which satisfy the following conditions:

- "Runtime settings > General > Settings > Use default design" is activated for the HMI device.
- For screens, basic elements and elements: "Properties > Properties> Design > Settings > Use color scheme" is selected in the Inspector window.
- For controls: "Properties > Properties > Appearance > Style > Accept project settings" is selected in the Inspector window.

---

**See also**

[Basics on working with designs (RT Professional)](#basics-on-working-with-designs-rt-professional)
  
[Designs editor (RT Professional)](#designs-editor-rt-professional)
  
[Applying a design (RT Professional)](#applying-a-design-rt-professional)

### Working with styles and style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on working with styles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-styles-basic-panels-panels-comfort-panels-rt-advanced)
- [Displaying predefined styles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#displaying-predefined-styles-basic-panels-panels-comfort-panels-rt-advanced)
- [Defining a style (Basic Panels, Panels, Comfort Panels, RT Advanced)](#defining-a-style-basic-panels-panels-comfort-panels-rt-advanced)
- [Managing styles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-styles-basic-panels-panels-comfort-panels-rt-advanced)
- [Adjusting the font size to the device size (Basic Panels, Panels, Comfort Panels, RT Advanced)](#adjusting-the-font-size-to-the-device-size-basic-panels-panels-comfort-panels-rt-advanced)
- [Using style items (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-style-items-basic-panels-panels-comfort-panels-rt-advanced)
- [Basics on working with style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-style-sheets-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating a new style sheet (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-new-style-sheet-basic-panels-panels-comfort-panels-rt-advanced)
- [Managing style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-style-sheets-basic-panels-panels-comfort-panels-rt-advanced)
- [Using style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-style-sheets-basic-panels-panels-comfort-panels-rt-advanced)

#### Basics on working with styles (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

The style editor is a global editor. You define a uniform appearance for display and operating elements in the style editor. In this way, you harmonize the display of objects in Runtime. The style editor offers predefined styles. Additional predefined styles are available for download at [Siemens Industry Online Support](http://support.automation.siemens.com/WW/view/en/91174767).

You can choose one of the predefined styles or create your own style. You use the style editor independently of devices and projects.

##### Views in the style editor

Objects are grouped in the style editor according to their main visual features.

The following groups are available:

- Buttons, lines, and polygon-based objects
- Text-based objects
- Trend-based objects, such as trend view,
- graphic or value-based objects, such as value table.

##### Style items

You use a style item to define the appearance of a screen object within a style. You can design several objects of the same type differently in one style. You define, for example, different style items for simple buttons and navigation buttons.

You create and manage style items in the style editor.

##### Style sheets

You use style sheets to configure the same properties for a group of objects. In a style sheet you can, for example, define the width and background color of table headers for all table-based objects. Style sheets are divided into predefined types depending on the included properties, for example, buttons, limits, table headers.

You use style sheets to define the design of shared object properties. Some special object properties are not included in style sheets. You use styles to design all objects of a project with visual consistency.

##### Managing styles and style sheets

You create and edit styles and style sheets in the project library. To get a better overview of types in expansive libraries, you save styles and style sheets in folders with meaningful names. You should also assign meaningful names to the styles and style sheets you create yourself.

![Managing styles and style sheets](images/69458550923_DV_resource.Stream@PNG-en-US.png)

##### Support of styles in faceplates

Styles and style items can be assigned to faceplate instances.

However, there is no direct connection between the faceplate types and styles, so selection and preview of a style item in the faceplate editor is not possible. To assign a style item to a faceplate, enter the name of the style item under "Style item appearance".

The configured style item is used in the instance of a faceplate, provided the name of the style item exists in the style used. Ensure that the name is written correctly.

---

**See also**

[Displaying predefined styles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#displaying-predefined-styles-basic-panels-panels-comfort-panels-rt-advanced)
  
[Defining a style (Basic Panels, Panels, Comfort Panels, RT Advanced)](#defining-a-style-basic-panels-panels-comfort-panels-rt-advanced)
  
[Managing styles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#managing-styles-basic-panels-panels-comfort-panels-rt-advanced)
  
[Using style items (Basic Panels, Panels, Comfort Panels, RT Advanced)](#using-style-items-basic-panels-panels-comfort-panels-rt-advanced)

#### Displaying predefined styles (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In the "Style" editor, you see predefined styles and create your own styles for representing display and operating objects in Runtime.

##### Open "Styles" editor

1. Double-click "Common data" in the project navigation.
2. Click the "Styles" editor. The editor opens.
3. The standard styles are displayed in the work area of the "Style" editor:

**Note**

**Style editor in the project navigation**

The style editor is only visible in the project navigation if a device that supports styles, e.g., Comfort Panels, is created in the project.

- WinCC Light
- WinCC Dark
- WinCC Fresh
- WinCC Wireframe.

##### Result

The settings for the groups and individual objects are displayed in the work area.

You will assign predefined styles or define your own styles in the next steps.

Predefined styles are write-protected and cannot be changed.

---

**See also**

[Basics on working with styles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-styles-basic-panels-panels-comfort-panels-rt-advanced)

#### Defining a style (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

In the "Styles" editor, you see predefined styles. Predefined styles are write-protected and cannot be changed.

In addition, you have the option of defining your own styles and applying them to individual objects, groups, and even projects.

##### Defining a style

1. Open the "Common data" folder in the project navigation.
2. Open the "Style" editor.
3. Click "Add" in the "Styles" area.

   A new style is created.

   The library view opens. The version of the type is displayed in the "Types" folder. The version 0.0.1 has the status "in progress".
4. In the Inspector window, select the colors, borders and other settings for individual objects.

   ![Defining a style](images/68055925387_DV_resource.Stream@PNG-en-US.png)

   ![Defining a style](images/68055925387_DV_resource.Stream@PNG-en-US.png)
5. In order to activate the new style, select the current version "in progress" and select "Release version" in the shortcut menu.  
   The new style appears in the "Styles" editor.

##### Result

You have added a new style which can be applied to objects or projects.

##### Defining a style based on a predefined style

1. Open the "Common data" folder in the project navigation.
2. Open the "Style" editor.
3. Select a predefined style in the work area.
4. Select the "Duplicate type" command in the shortcut menu.  
   The "Duplicate type" dialog opens.
5. Overwrite the suggested name with a meaningful name.
6. In the "Comment" column, enter a description of the style, e.g. the intended use.
7. Click "OK" to confirm your input.
8. Select the created type in the project library.
9. Select "Edit new type" in the shortcut menu.

   The library view opens. The version of the type is displayed in the "Types" folder. The version 0.0.2 has the status "in progress".
10. Configure the type as required.
11. Select the "Release version" command from the shortcut menu of the edited version.

##### Result

They have configured a new style based on the predefined style of WinCC.

---

**See also**

[Basics on working with styles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-styles-basic-panels-panels-comfort-panels-rt-advanced)
  
[State of type versions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#state-of-type-versions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Managing styles (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Deleting a style

You can delete styles that you have defined yourself.

1. Open the "Common data" folder in the project navigation.
2. Open the "Style" editor.
3. Select the style in the work area that you want to delete.
4. Select the "Delete" command in the shortcut menu.

**Note**

You cannot delete the predefined styles of WinCC.

The style is deleted.

##### Editing a style

You can edit styles that you have defined yourself.

1. Open the project library.
2. Select the released version of the style that you want to change.
3. Select "Edit type" in the shortcut menu.

   A new version "in progress" is created.
4. Make the required changes in the Inspector window.
5. Select the "Release version" command from the shortcut menu of the edited version to put the changes into effect.

   The changes made take effect.

##### Determining a standard style for a project

A project can be assigned a standard style to achieve a visual conformity of all display objects in the project.

1. Open the "Common data" folder in the project navigation.
2. Open the "Style" editor.
3. Activate a style in the work area.

The activated style is used as standard style in the project. When you add a device to the project, this device uses the standard style.

##### Changing the style for a specific device

Within a project, you change the style for a specific device.

1. Open the "Runtime settings" editor of the HMI device.
2. Select a device style under "General".

The selected style is applied to the device.

If the device style is not assigned, the device uses the standard style of the project.

---

**See also**

[Basics on working with styles (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-working-with-styles-basic-panels-panels-comfort-panels-rt-advanced)

#### Adjusting the font size to the device size (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You define the size of the device to whose objects you want to apply a style in the style editor. This means you specify device-dependent font sizes in a style. All font sizes are automatically adapted to the device size by selecting a specific reference size.

The table below shows the device sizes and the reference font sizes in pixels:

| Device size | Font size in pixels |
| --- | --- |
| 4" display | 15 px |
| 7" display | 17 px |
| 9" display | 15 px |
| 12" display | 19 px |
| 15" display | 19 px |
| 19" display | 17 px |
| 22" display | 21 px |
| WinCC RT Advanced | 17 px |

##### Activating automatic adjustment of font sizes

1. Double-click the "Runtime settings" editor in the project window.
2. Click "General".
3. Activate the option "Adjust font size in style" under "General > Screen".

   ![Activating automatic adjustment of font sizes](images/74853635595_DV_resource.Stream@PNG-en-US.png)

   ![Activating automatic adjustment of font sizes](images/74853635595_DV_resource.Stream@PNG-en-US.png)

   Automatic adjustment of font sizes to the device size was activated in a style.

##### Adjusting font size in a device style

1. Open the corresponding style for editing in the project library.
2. Select the reference size of the HMI device in the work area.

   ![Adjusting font size in a device style](images/74854828939_DV_resource.Stream@PNG-en-US.png)

   ![Adjusting font size in a device style](images/74854828939_DV_resource.Stream@PNG-en-US.png)

   All font sizes in the style are automatically adjusted to the selected device size.

#### Using style items (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You use style items to change the style of a screen object without changing the entire device style. You can, for example, define types of buttons with the help of different style items that are to receive the same appearance in one or several devices.

You define style items in the style editor.

##### Adding a new style item

1. Open the project library.
2. Select the released version of the style that you want to change.
3. Select "Edit type" in the shortcut menu.

   A new version "in progress" is created.
4. Select the object that you want to use in a different style.
5. Click the plus sign next to the object name.

   ![Adding a new style item](images/66789249291_DV_resource.Stream@PNG-en-US.png)

   ![Adding a new style item](images/66789249291_DV_resource.Stream@PNG-en-US.png)

   A new style item has been created.

   You can also select "Duplicate style item" in the shortcut menu of the object.
6. Make the required changes in the inspector window.
7. Assign a meaningful name to the new style item under "Properties > Miscellaneous > Object > Name".
8. Release the version of the style.

##### Deleting a style item

You can delete style items that you have defined yourself.

1. Open the project library.
2. Select the style that includes the style item.
3. Open the "in progress" version.
4. Select the style item that you want to delete in the work area.
5. Select the "Delete" command in the shortcut menu.

**Note**

You cannot rename or delete predefined WinCC style items.

The style item is deleted.

##### Specifying a style item for an object

If you have configured additional style items for an object in the device style, you can use the predefined style item for a screen object.

1. Open "Properties > Styles/Designs > Settings".
2. Enable the option "Use style/design".
3. Select the predefined style item under "Style item appearance".

   ![Specifying a style item for an object](images/89374787595_DV_resource.Stream@PNG-en-US.png)

   ![Specifying a style item for an object](images/89374787595_DV_resource.Stream@PNG-en-US.png)

   The object is displayed as selected style item.

#### Basics on working with style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

Some screen objects have the same properties which can be configured similarly. These general properties are grouped in style sheets. You can configure several properties for several objects simultaneously and consistently by using style sheets.

##### Types of style sheets

Style sheets are divided into several predefined categories. Each category contains a specific number of common properties shared by different objects. Select the required category when you create a style sheet. A style sheet can only be applied to objects for which the corresponding category is defined.

The table below shows the available categories and objects that can be configured with them.

| Category/Objects | Polylines/ Lines | Text-based objects | Buttons | Value-based objects | Table-based objects | Diagrams |
| --- | --- | --- | --- | --- | --- | --- |
| Button | - | - | X | - | X | X |
| Object body | X | - | - | X | X | X |
| Diagram body | - | - | - | - | - | X |
| Focus and selection | - | X | X | - | X | X |
| Limits | - | X | - | X | - | - |
| Labels | - | - | - | X | - | - |
| Scale | - | - | - | X | - | - |
| Table body | - | - | - | - | X | X |
| Table header | - | - | - | - | X | X |
| Text field | - | X | - | - | - | - |

##### Use of style sheets

You apply a style sheet to a style item when editing a style. The properties configured in the style sheet are transferred to the style item.

To apply a style sheet to a style item, drag the required style sheet from the task card to the style item in the work area using drag-and-drop.

##### Managing style sheets

Style sheets are library types. You manage style sheets in the project library. Style sheet categories are available in the project library in the "Style sheets > Categories" task card during style editing.

The style sheets that are available for a style sheet type are available in the "Style sheets > Visual attributes" task card. The task card includes predefined style sheets as well as style sheets you have created yourself and released.

#### Creating a new style sheet (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You configure the properties for several objects of a similar type in a style sheet.

##### Create new style sheet

1. Open the project library.
2. Click the "Add new type" button.

   The "Add new type" dialog opens.
3. Select the option "HMI style sheet" in the dialog.
4. Select the type of the style sheet.

   ![Create new style sheet](images/74855162635_DV_resource.Stream@PNG-en-US.png)

   ![Create new style sheet](images/74855162635_DV_resource.Stream@PNG-en-US.png)
5. Assign a meaningful name to the style sheet.
6. Click "OK" to confirm your input.

   The new style sheet was created.

##### Create new style sheet based on a style

To automatically configure the properties for similar screen objects when editing a style, create a new style sheet based on properties of a style item that have already been configured.

1. Select the style item you want to use to create a style sheet.
2. Select "Create new style sheet" in the shortcut menu.
3. Select the category for the style sheet in the submenu.

   The "Add type" dialog opens.
4. Assign a meaningful name to the style sheet.
5. Click "OK" to confirm.

   The new style sheet based on a style was created and has been added to the "Style sheets > Visual attributes" task card.

   The properties in the style sheet were applied from the selected style item. The properties of the style sheet not included in the selected style have been assigned default values.

#### Managing style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You edit, copy and delete the style sheets in the project library.

You can also open, copy, create and delete style sheets with the commands in the shortcut menu of the "Style sheets > Categories" task card.

##### Edit style sheet

You can edit style sheets that you have created yourself.

1. Open the project library.
2. Select the released version of the style sheet that you want to change.
3. Select "Edit type" in the shortcut menu.

   A new version "in progress" is created.
4. Make the required changes in the Inspector window.
5. Select the "Release version" command from the shortcut menu of the edited version to put the changes into effect.

   The changes made take effect.

##### Delete style sheet

You can delete style sheets that you have defined yourself.

1. Open the project library.
2. Select the style sheet that you want to delete in the project library.
3. Select the "Delete" command in the shortcut menu.

**Note**

You cannot delete the predefined style sheets of WinCC.

**Note**

You cannot delete the style sheet which includes an "in progress" type. To delete the style sheet, start by releasing all versions of the style sheet.

The style sheet is deleted.

##### Copy style sheet

1. Open the project library.
2. Select the style sheet that you would like to copy.
3. Select "Duplicate type" in the shortcut menu.
4. Overwrite the suggested name with a meaningful name.
5. In the "Comment" column, enter a description of the style sheet, for example, the intended use.
6. Click "OK" to confirm your input.

   The required style sheet was copied and stored in the same folder.

#### Using style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

You are using a style sheet while editing a style in the style editor. Style sheets are object-specific and are only applied to style items with which they are compatible.

Only a released version of a style sheet can be applied to a style item.

You have the following options to use a style sheet:

- To design the selected style item, drag the style sheet to a style item in the style editor.
- To design several style items of a group, drag the style sheet to a group of style items.
- To design all style items of the style which are compatible with the style sheet, drag the style sheet to an empty area in the style editor.

##### Requirement

- You have created a style.
- A version of the style is opened "in progress".

##### Apply style sheet to style item

1. Select the style sheet category in the "Style sheets > Categories" task card.
2. Select the required style sheet in the "Style sheets > Visual attributes" task card.
3. Drag the selected style sheet to a style item with drag&drop.

   ![Apply style sheet to style item](images/74855470859_DV_resource.Stream@PNG-en-US.png)

   ![Apply style sheet to style item](images/74855470859_DV_resource.Stream@PNG-en-US.png)

   When you drop the style sheet on the style item, the style item applies the settings from the style sheet.

**Note**

There is no connection between the style item and the used style sheet. When you change the style sheet, the changes are not automatically applied in the style item. Apply the style sheet again to make the changes to the style sheet effective in the style item.

**Note**

Style sheets are not linked with screen objects. Unused or outdated style sheet versions are deleted by cleaning up or versioning the library.

##### Result

You have applied a style sheet to a style item in a style.

## Working with objects and object groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Working with objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with object groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-object-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring the keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-the-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Examples (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#examples-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Working with objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of objects (RT Professional)](#overview-of-objects-rt-professional)
- [Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)
- [Overview of objects (Basic Panels)](#overview-of-objects-basic-panels)
- [Options for editing objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#options-for-editing-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Inserting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Deleting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#deleting-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Positioning an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#positioning-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Resizing objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#resizing-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Selecting multiple objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-multiple-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Aligning objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#aligning-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Moving objects with keyboard shortcuts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-objects-with-keyboard-shortcuts-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Moving an object forwards or backwards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-an-object-forwards-or-backwards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Showing objects outside the screen area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#showing-objects-outside-the-screen-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Rotating objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#rotating-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Flipping objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#flipping-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Designing an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#designing-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Designing an object (RT Professional)](#designing-an-object-rt-professional)
- [Designing the fill pattern (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#designing-the-fill-pattern-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Specifying scroll bars (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#specifying-scroll-bars-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Using predefined styles (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#using-predefined-styles-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Formatting text in an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#formatting-text-in-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Connecting tags and text lists in the text (RT Advanced)](#connecting-tags-and-text-lists-in-the-text-rt-advanced)
- [Formatting graphics in an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#formatting-graphics-in-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Rotating an object in runtime (RT Professional)](#rotating-an-object-in-runtime-rt-professional)
- [Designing table-based objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#designing-table-based-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Designing a border (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#designing-a-border-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Defining color gradients (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-color-gradients-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring ranges (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-ranges-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Flashing (Panels, Comfort Panels, RT Advanced)](#flashing-panels-comfort-panels-rt-advanced)
- [Flashing (RT Professional)](#flashing-rt-professional)
- [Inserting multiple objects of the same type (stamping) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-multiple-objects-of-the-same-type-stamping-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Repositioning and resizing multiple objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#repositioning-and-resizing-multiple-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Hiding or showing objects (RT Professional)](#hiding-or-showing-objects-rt-professional)
- [Linking user data types with objects (RT Professional)](#linking-user-data-types-with-objects-rt-professional)
- [Managing own controls (RT Advanced, RT Professional)](#managing-own-controls-rt-advanced-rt-professional)
- [External graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#external-graphics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing external graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-external-graphics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Storing an external image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-external-image-in-the-graphics-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Individually adjusting graphics in controls (RT Professional)](#individually-adjusting-graphics-in-controls-rt-professional)

#### Overview of objects (RT Professional)

##### Introduction

Objects are graphics elements which you use to design the screens of your project.

The "Toolbox" task card contains all objects that can be used for the HMI device.

Display the tool window with menu command "View" by activating the "Task Card" option.

The toolbox contains various palettes, depending on the currently active editor. If the "Screens" editor is open, the toolbox contains the following palettes:

- "Basic objects"

  The basic objects include basic graphic objects such as "Line", "Circle", "Text field" or "Graphic view".
- "Elements"

  The elements include basic control elements, e.g. "I/O field", "Button" or "Gauge".
- "Controls"

  The controls provide advanced functions. They also represent process operations dynamically, for example "Trend view" and "Recipe view".
- "My controls"

  In this palette, you can add ActiveX controls and simple .Net controls to the Toolbox window. From this palette you incorporate ActiveX controls into your project. The following restrictions apply:

  - Only the ActiveX controls that are registered in the operating system of the configuration computer are available.
  - Only the simple .Net controls are supported by the TIA Portal. XAML controls, for example, WPF (Windows Presentation Foundation) controls, are not supported.
- "Graphics"

  Graphics are broken down into subjects in the form of a directory tree structure. The various folders contain the following graphic illustrations:

  - Machine and plant areas
  - Measuring equipment
  - Operator controls

  You can create links to your own graphic folders. The external graphics are located in these folders and subfolders. They are displayed in the toolbox and incorporated into the project using links.
- "Libraries" task card

  In addition to the display and operating objects, the library objects are available. They are located within the palettes of the "Libraries" task card. A library contains preconfigured objects such as graphics of pipes, pumps, or preconfigured buttons. You can also integrate multiple instances of library objects into your project without having to reconfigure them.

  The WinCC software package includes libraries, e.g. "HMI Buttons & Switches".

  You may also store customized objects and faceplates in user libraries. Faceplates are objects that you create from existing screen objects, and for which you define the configurable properties.

##### Basic objects

| Icon | Object | Instructions |
| --- | --- | --- |
| ![Basic objects](images/14137318283_DV_resource.Stream@PNG-de-DE.png) | "Line" | - |
| ![Basic objects](images/6341645323_DV_resource.Stream@PNG-de-DE.png) | "Polyline" | The polyline is an open object. Even if the start and end points have the same coordinates, the area they enclose cannot be filled in. If you want to fill a polygon, select the "Polygon" object. |
| ![Basic objects](images/6341624203_DV_resource.Stream@PNG-de-DE.png) | "Polygon" | - |
| ![Basic objects](images/14137326475_DV_resource.Stream@PNG-de-DE.png) | "Ellipsis" | - |
| ![Basic objects](images/14137666955_DV_resource.Stream@PNG-de-DE.png) | "Circle" | - |
| ![Basic objects](images/14137687947_DV_resource.Stream@PNG-de-DE.png) | "Rectangle" | - |
| ![Basic objects](images/9128426891_DV_resource.Stream@PNG-de-DE.png) | "Circular arc" | The circular arc is an open object. Even if the start and end points have the same coordinates, the area they enclose cannot be filled in. If you want to fill a circle, select the "Circle" or "Circle segment" object. |
| ![Basic objects](images/9128511883_DV_resource.Stream@PNG-de-DE.png) | "Ellipse arc" | An ellipse arc is an open object. Even if the start and end points have the same coordinates, the area they enclose cannot be filled in. If you want to fill an ellipse, select the "Ellipse" or "Ellipse segment" object. |
| ![Basic objects](images/9128571275_DV_resource.Stream@PNG-de-DE.png) | "Circle segment" | - |
| ![Basic objects](images/9128579467_DV_resource.Stream@PNG-de-DE.png) | "Ellipse segment" | - |
| ![Basic objects](images/9128638859_DV_resource.Stream@PNG-de-DE.png) | "Connector" | Connects objects with lines. |
| ![Basic objects](images/14137724043_DV_resource.Stream@PNG-de-DE.png) | "Text field" | One or more lines of text. The font and layout are adjustable. |
| ![Basic objects](images/14138092683_DV_resource.Stream@PNG-de-DE.png) | "Graphic view" | Displays graphics from external graphic programs, and inserts OLE objects. The following graphic elements can be used: "*.emf", "*.wmf", "*.dib", "*.bmp", "*.jpg", "*.jpeg", "*.gif", "*.tif" and "*.svg". |
| ![Basic objects](images/24194040843_DV_resource.Stream@PNG-de-DE.png) | "Pipe" | Represents a continuous pipe with several bends in a pipe system. |
| ![Basic objects](images/24195917067_DV_resource.Stream@PNG-de-DE.png) | "Double T-piece" | Represents a pipe junction in a pipe system. |
| ![Basic objects](images/24194033419_DV_resource.Stream@PNG-de-DE.png) | "T piece" | Represents a T-shaped pipe connection. |
| ![Basic objects](images/24195924491_DV_resource.Stream@PNG-de-DE.png) | "Pipe bends" | Represents a bent section of pipe. |

##### Elements

| Icon | Object | Instructions |
| --- | --- | --- |
| ![Elements](images/61134008971_DV_resource.Stream@PNG-de-DE.png) | "I/O field" | Outputs the values of a tag, and/or writes values to a tag.  You can define limits for the tag values shown in the I/O field. To hide the operator input in runtime, configure "Hidden input". |
| ![Elements](images/90430666251_DV_resource.Stream@PNG-de-DE.png) | "Editable text field" | Displays several lines of text in a rectangle on the screen. |
| ![Elements](images/90473759883_DV_resource.Stream@PNG-de-DE.png) | "List box" | Displays a selection of several list entries. |
| ![Elements](images/90473883915_DV_resource.Stream@PNG-de-DE.png) | "Combo box" | Displays a selection of several entries in a drop-down list. |
| ![Elements](images/14138241419_DV_resource.Stream@PNG-de-DE.png) | "Button" | Executes a list of functions, or a script as configured. |
| ![Elements](images/9127594379_DV_resource.Stream@PNG-de-DE.png) | "Round button" | Operates processes, such as acknowledge alarms. |
| ![Elements](images/60619802379_DV_resource.Stream@PNG-de-DE.png) | "Symbolic I/O field" | Outputs the values of a tag, and/or writes values to a tag. A text from a text list is displayed in relation to the tag value. |
| ![Elements](images/14137923723_DV_resource.Stream@PNG-de-DE.png) | "Graphic I/O field" | Outputs the values of a tag, and/or writes values to a tag. A graphic from a graphics list is displayed in relation to the tag value. |
| ![Elements](images/14138282635_DV_resource.Stream@PNG-de-DE.png) | "Bar" | The bar represents a value from the PLC in the form of a scaled bar graph. |
| ![Elements](images/9126172939_DV_resource.Stream@PNG-de-DE.png) | "Symbol library" | Used to add screen objects based on controls of the same name. |
| ![Elements](images/6342255883_DV_resource.Stream@PNG-de-DE.png) | "Slider" | Used to display a current value or to enter a numeric value. |
| ![Elements](images/9128178571_DV_resource.Stream@PNG-de-DE.png) | "Scroll bar" | Enters a numerical value at the PLC. The value can be adjusted smoothly. |
| ![Elements](images/9128225163_DV_resource.Stream@PNG-de-DE.png) | "Check box" | Selects options. |
| ![Elements](images/9128233355_DV_resource.Stream@PNG-de-DE.png) | "Option button" | Selects an option. |
| ![Elements](images/6342378763_DV_resource.Stream@PNG-de-DE.png) | "Gauge" | Displays numeric values.  The appearance of the gauge is adjustable. |
| ![Elements](images/6341869963_DV_resource.Stream@PNG-de-DE.png) | "Clock" | Displays the system time in analog or digital format. |
| ![Elements](images/9128384907_DV_resource.Stream@PNG-de-DE.png) | "Memory space view" | Shows the existing memory size. |

##### Controls

| Icon | Object | Description |
| --- | --- | --- |
| ![Controls](images/9128279947_DV_resource.Stream@PNG-de-DE.png) | "Screen window" | Displays other screens of the object. |
| ![Controls](images/14138311051_DV_resource.Stream@PNG-de-DE.png) | "f(t) trend view" | Represents multiple curves with values from the PLC, or from a log. |
| ![Controls](images/9128300939_DV_resource.Stream@PNG-de-DE.png) | "f(x) trend view" | Represents the values of a tag as a function of another tag. |
| ![Controls](images/9128309131_DV_resource.Stream@PNG-de-DE.png) | "Table view" | Represents current or archived process data in a table. |
| ![Controls](images/25554576011_DV_resource.Stream@PNG-de-DE.png) | "Value table" | Represents evaluated data and statistics in a table. |
| ![Controls](images/21488204555_DV_resource.Stream@PNG-de-DE.png) | "System diagnostics view" | Provides an overview of all diagnostics capable devices. Displays errors in the plant. |
| ![Controls](images/14138303115_DV_resource.Stream@PNG-de-DE.png) | "User view" | Allows an administrator to administer users on the HMI device.  It also allows an operator without administrator rights to change their password. |
| ![Controls](images/72306933515_DV_resource.Stream@PNG-de-DE.png) | "HTML browser" | Displays HTML pages. |
| ![Controls](images/26356391307_DV_resource.Stream@PNG-de-DE.png) | "Print job/Script diagnostics" | Displays data of the Global Script application and of the log system for editing. |
| ![Controls](images/25630948747_DV_resource.Stream@PNG-de-DE.png) | "Recipe view" | Used to display and modify recipes. |
| ![Controls](images/9129274251_DV_resource.Stream@PNG-de-DE.png) | Media Player | Enables video and audio files to be played. |
| ![Controls](images/26351583755_DV_resource.Stream@PNG-de-DE.png) | "Channel diagnostics display" | Allows users to control the active connections. |
| ![Controls](images/14138365323_DV_resource.Stream@PNG-de-DE.png) | "Alarm view" | Shows currently pending alarms or alarm events from the alarm buffer or alarm log. |
| ![Controls](images/79486104075_DV_resource.Stream@PNG-de-DE.png) | "PLC code view"<sup>1)</sup> | Displays the PLC programs which have been programmed in the LAD or FBD programming languages. |
| ![Controls](images/78293900683_DV_resource.Stream@PNG-de-DE.png) | "ProDiag overview"<sup>2)</sup> | Indicates the current state of operand monitoring. |
| ![Controls](images/79486112651_DV_resource.Stream@PNG-de-DE.png) | "GRAPH overview"<sup>2)</sup> | Shows the current status of the program in a sequence and single step view. |
| ![Controls](images/100988370443_DV_resource.Stream@PNG-de-DE.png) | "Criteria analysis view"<sup>3)</sup> | Shows the operands with error in the program that were determined by the criteria analysis. |

<sup>1)</sup> Available as of device version V14.

<sup>2)</sup> Available as of device version V14.

<sup>3)</sup> Available as of device version V15.

> **Note**
>
> Some of the toolbox objects are either available with restricted functionality, or not at all. This depends on the HMI device you are configuring. Unavailable properties of an object are displayed as deactivated, and cannot be selected.

> **Note**
>
> **Support for SVG graphics as of TIA Portal version V15**
>
> You can use the SVG graphics in the following screen objects:
>
> Pictures (as background image)
>
> Round buttons
>
> Graphic view
>
> Graphic I/O field
>
> Graphic list entry

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)
  
[Designing an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#designing-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Designing an object (RT Professional)](#designing-an-object-rt-professional)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of objects (Panels, Comfort Panels, RT Advanced)

##### Introduction

Objects are graphics elements which you use to design the screens of your project.

The "Toolbox" task card contains all objects that can be used for the HMI device. Display the Task Card with menu command "View" by activating the "Task Card" option.

The toolbox contains various palettes, depending on the currently active editor. If the "Screens" editor is open, the toolbox contains the following palettes:

- "Basic objects"

  The basic objects include basic graphic objects such as "Line", "Circle", "Text field" or "Graphic view".
- "Elements"

  The elements include basic control elements, e.g. "I/O field", "Button" or "Gauge".
- "Controls"

  The controls provide advanced functions. They also represent process operations dynamically, for example Trend view and Recipe view.
- "Graphics"

  Graphics are broken down into subjects in the form of a directory tree structure. The various folders contain the following graphic illustrations:

  - Machine and plant areas
  - Measuring equipment
  - Operator controls
  - Flags
  - Buildings

  You can create links to your own graphic folders. The external graphics are located in these folders and subfolders. They are displayed in the toolbox and incorporated into the project using links.
- "Libraries" task card

  In addition to the display and operating objects, the library objects are available. They are located within the palettes of the "Libraries" task card. A library contains preconfigured objects such as graphics of pipes, pumps, or preconfigured buttons. You can also integrate multiple instances of library objects into your project without having to reconfigure them.

  The WinCC software package includes libraries, e.g. "HMI Buttons & Switches".

  You can also store customized objects, and faceplates in user libraries.

  Faceplates are objects that you create from existing screen objects, and for which you define the configurable properties.

  > **Note**
  >
  > **HMI device dependency**
  >
  > Some of the toolbox objects are either available with restricted functionality, or not at all. This depends on the HMI device you are configuring. Unavailable properties of an object are displayed as deactivated, and cannot be selected.

##### Basic objects

| Icon | Object | Instructions |
| --- | --- | --- |
| ![Basic objects](images/14137318283_DV_resource.Stream@PNG-de-DE.png) | "Line" | - |
| ![Basic objects](images/6341645323_DV_resource.Stream@PNG-de-DE.png) | "Polyline" | The polyline is an open object. Even if the start and end points have the same coordinates, the area they enclose cannot be filled in. If you want to fill a polygon, select the "Polygon" object. |
| ![Basic objects](images/6341624203_DV_resource.Stream@PNG-de-DE.png) | "Polygon" | - |
| ![Basic objects](images/14137326475_DV_resource.Stream@PNG-de-DE.png) | "Ellipsis" | - |
| ![Basic objects](images/14137666955_DV_resource.Stream@PNG-de-DE.png) | "Circle" | - |
| ![Basic objects](images/14137687947_DV_resource.Stream@PNG-de-DE.png) | "Rectangle" | - |
| ![Basic objects](images/14137724043_DV_resource.Stream@PNG-de-DE.png) | "Text field" | One or more lines of text. The font and layout are adjustable. |
| ![Basic objects](images/14138092683_DV_resource.Stream@PNG-de-DE.png) | "Graphic view" | Displays graphics from external graphic programs, and inserts OLE objects. The following graphic formats can be used: "*.emf", "*.wmf", "*.dib", "*.bmp", "*.jpg", "*.jpeg", "*.gif" and "*.tif". |

##### Elements

| Icon | Object | Instructions |
| --- | --- | --- |
| ![Elements](images/61134008971_DV_resource.Stream@PNG-de-DE.png) | "I/O field" | Outputs the values of a tag, and/or writes values to a tag.  You can define limits for the tag values shown in the I/O field. To hide the operator input in runtime, configure "Hidden input". |
| ![Elements](images/14138241419_DV_resource.Stream@PNG-de-DE.png) | "Button" | Executes a list of functions, or a script as configured. |
| ![Elements](images/60619802379_DV_resource.Stream@PNG-de-DE.png) | "Symbolic I/O field" | Outputs the values of a tag, and/or writes values to a tag. A text from a text list is displayed in relation to the tag value. |
| ![Elements](images/14137923723_DV_resource.Stream@PNG-de-DE.png) | "Graphic I/O field" | Outputs the values of a tag, and/or writes values to a tag. A graphic from a graphics list is displayed in relation to the tag value. |
| ![Elements](images/14137716107_DV_resource.Stream@PNG-de-DE.png) | "Date/time field" | Outputs the system date and time, or the time and date from a tag. This allows the operator to enter new values. The display format is adjustable. |
| ![Elements](images/14138282635_DV_resource.Stream@PNG-de-DE.png) | "Bar" | The bar represents a value from the PLC in the form of a scaled bar graph. |
| ![Elements](images/21378324491_DV_resource.Stream@PNG-de-DE.png) | "Charge condition" | Shows the charge condition of the battery for Mobile Wireless |
| ![Elements](images/61134016779_DV_resource.Stream@PNG-de-DE.png) | "Switch" | Toggles between two defined states. You can label a switch with text, or a graphic. |
| ![Elements](images/6342255883_DV_resource.Stream@PNG-de-DE.png) | "Slider" | Displays a current value from the PLC, or sends a numeric value to the PLC. |
| ![Elements](images/9126172939_DV_resource.Stream@PNG-de-DE.png) | "Symbol library" | Used to add screen objects based on controls of the same name. |
| ![Elements](images/21378523915_DV_resource.Stream@PNG-de-DE.png) | "Effective range name" | Shows the name of the effective range. |
| ![Elements](images/21378643211_DV_resource.Stream@PNG-de-DE.png) | "Effective range name (RFID)" | Displays the name of the effective range (RFID). |
| ![Elements](images/21378635787_DV_resource.Stream@PNG-de-DE.png) | "Effective range signal" | Indicates how accurately the Mobile Panel Wireless is positioned within an effective range. |
| ![Elements](images/21378317067_DV_resource.Stream@PNG-de-DE.png) | "WLAN reception" | Indicates how good the WLAN radio connection is. |
| ![Elements](images/6342378763_DV_resource.Stream@PNG-de-DE.png) | "Gauge" | Displays numeric values.  The appearance of the gauge is adjustable. |
| ![Elements](images/21378531339_DV_resource.Stream@PNG-de-DE.png) | "Zone name" | Displays the name of the zone. |
| ![Elements](images/21378538763_DV_resource.Stream@PNG-de-DE.png) | "Zone signal" | Indicates how accurately the Mobile Panel Wireless is positioned within a zone. |
| ![Elements](images/6341869963_DV_resource.Stream@PNG-de-DE.png) | "Clock" | Displays the system time in analog or digital format. |

##### Controls

| Icon | Object | Description |
| --- | --- | --- |
| ![Controls](images/14138365323_DV_resource.Stream@PNG-de-DE.png) | "Alarm view" | Shows currently pending alarms or alarm events from the alarm buffer or alarm log. |
| ![Controls](images/14138311051_DV_resource.Stream@PNG-de-DE.png) | "Trend view" | Represents multiple curves with values from the PLC, or from a log. |
| ![Controls](images/14138303115_DV_resource.Stream@PNG-de-DE.png) | "User view" | Allows an administrator to administer users on the HMI device.  It also allows an operator without administrator rights to change their password. |
| ![Controls](images/72306933515_DV_resource.Stream@PNG-de-DE.png) | "HTML browser" | Displays HTML pages. |
| ![Controls](images/72371554827_DV_resource.Stream@PNG-de-DE.png) | "Camera view"<sup>1)</sup> | Displays pictures from a connected network camera. |
| ![Controls](images/72371545995_DV_resource.Stream@PNG-de-DE.png) | "PDF view" | Displays PDF documents. |
| ![Controls](images/6344541835_DV_resource.Stream@PNG-de-DE.png) | "Watch table" | This function gives the operator direct read / write access from the HMI device to individual address areas in the connected SIMATIC S7. |
| ![Controls](images/21376581003_DV_resource.Stream@PNG-de-DE.png) | "Sm@rtClient view" | Allows an operator to monitor and maintain a connected device remotely. |
| ![Controls](images/14138344587_DV_resource.Stream@PNG-de-DE.png) | "Recipe view" | Displays data records, and allows them to be edited. |
| ![Controls](images/9128300939_DV_resource.Stream@PNG-de-DE.png) | "f(x) trend view" | Represents the values of a tag as a function of another tag. |
| ![Controls](images/21488204555_DV_resource.Stream@PNG-de-DE.png) | "System diagnostics view" | Provides an overview of all diagnostics capable devices. Displays errors in the plant. |
| ![Controls](images/79486104075_DV_resource.Stream@PNG-de-DE.png) | "PLC code view"<sup>2)</sup> | Displays the PLC programs which have been programmed in the LAD or FBD programming languages. |
| ![Controls](images/81547087371_DV_resource.Stream@PNG-de-DE.png) | "GRAPH overview"<sup>3)</sup> | Shows the current program status for executed steps of the PLC sequencer. |
| ![Controls](images/78293900683_DV_resource.Stream@PNG-de-DE.png) | "ProDiag overview"<sup>3)</sup> | Indicates the current state of operand monitoring. |
| ![Controls](images/100988370443_DV_resource.Stream@PNG-de-DE.png) | "Criteria analysis view"<sup>4)</sup> | Shows the operands with error in the program that were determined by the criteria analysis. |
| ![Controls](images/9129274251_DV_resource.Stream@PNG-de-DE.png) | "Media Player" | Media files are shown in the media player. |

<sup>1)</sup> Available for Comfort Panels and KTP Mobile Panels (as of device version V13) and RT Advanced (as of device version V14 SP1)

<sup>2)</sup> Available for WinCC Runtime Advanced (as of device version V14) and Comfort Panels and KTP Mobile Panels (as of device version V14 with a display size > 4'').

<sup>3)</sup> Available for WinCC Runtime Advanced, Comfort Panels and KTP Mobile Panels (as of device version V14)

<sup>4)</sup> Available as of device version V15.

---

**See also**

[Overview of objects (RT Professional)](#overview-of-objects-rt-professional)
  
[Options for editing objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#options-for-editing-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Inserting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Deleting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#deleting-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Positioning an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#positioning-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Resizing objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#resizing-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting multiple objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-multiple-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Aligning objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#aligning-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Moving an object forwards or backwards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-an-object-forwards-or-backwards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Showing objects outside the screen area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#showing-objects-outside-the-screen-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Rotating objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#rotating-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Flipping objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#flipping-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Designing an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#designing-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Designing an object (RT Professional)](#designing-an-object-rt-professional)
  
[Hiding or showing objects (RT Professional)](#hiding-or-showing-objects-rt-professional)
  
[Managing own controls (RT Advanced, RT Professional)](#managing-own-controls-rt-advanced-rt-professional)
  
[External graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#external-graphics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing external graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-external-graphics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Storing an external image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-external-image-in-the-graphics-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overview-of-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced)
  
[Flashing (RT Professional)](#flashing-rt-professional)
  
[Inserting multiple objects of the same type (stamping) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-multiple-objects-of-the-same-type-stamping-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Flashing (Panels, Comfort Panels, RT Advanced)](#flashing-panels-comfort-panels-rt-advanced)
  
[Overview of objects (Basic Panels)](#overview-of-objects-basic-panels)
  
[Rotating an object in runtime (RT Professional)](#rotating-an-object-in-runtime-rt-professional)
  
[Repositioning and resizing multiple objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#repositioning-and-resizing-multiple-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of objects (Basic Panels)

##### Introduction

Objects are graphics elements which you use to design the screens of your project.

The "Tools" task card contains all objects that can be used for the HMI device. Display the Task Card with menu command "View" by activating the "Task Card" option.

The toolbox contains various palettes, depending on the currently active editor. If the "Screens" editor is open, the toolbox contains the following palettes:

- "Basic objects"

  The basic objects include basic graphic objects such as "Line", "Circle", "Text field" or "Graphic view".
- "Elements"

  The elements include basic operator controls, e.g. "I/O field", "Button" or "Gauge".
- "Controls"

  The controls provide advanced functions. They also represent process operations dynamically, for example Trend view and Recipe view.
- "Graphics"

  Graphics are broken down into subjects in the form of a directory tree structure. The various folders contain the following graphic illustrations:

  - Machine and plant areas
  - Measuring equipment
  - Operator controls
  - Flags
  - Buildings

  You can create links to your own graphic folders. The external graphics are located in these folders and subfolders. They are displayed in the toolbox and incorporated into the project using links.
- "Libraries" task card

  In addition to the display and operating elements, the library objects are available. They are located within the palettes of the "Libraries" task card. A library contains preconfigured objects such as graphics of pipes, pumps, or preconfigured buttons. You can also integrate multiple instances of library objects into your project without having to reconfigure them.

  The WinCC software package includes libraries, e.g. "HMI Buttons & Switches".

  You can also store customized objects, and faceplates in user libraries.

  Faceplates are objects that you create from existing screen objects, and for which you define the configurable properties.

  > **Note**
  >
  > **HMI device dependency**
  >
  > Some of the toolbox objects are either available with restricted functionality, or not at all. This depends on the HMI device you are configuring. Unavailable properties of an object are displayed as deactivated, and cannot be selected.

##### Basic objects

| Symbol | Object | Instructions |
| --- | --- | --- |
| ![Basic objects](images/14137318283_DV_resource.Stream@PNG-de-DE.png) | "Line" | - |
| ![Basic objects](images/14137326475_DV_resource.Stream@PNG-de-DE.png) | "Ellipse" | - |
| ![Basic objects](images/14137666955_DV_resource.Stream@PNG-de-DE.png) | "Circle" | - |
| ![Basic objects](images/14137687947_DV_resource.Stream@PNG-de-DE.png) | "Rectangle" | - |
| ![Basic objects](images/14137724043_DV_resource.Stream@PNG-de-DE.png) | "Text field" | One or more lines of text. The font and layout are adjustable. |
| ![Basic objects](images/14138092683_DV_resource.Stream@PNG-de-DE.png) | "Graphic view" | Displays graphics from external graphic programs, and inserts OLE objects. The following graphic formats can be used: "*.emf", "*.wmf", "*.dib", "*.bmp", "*.jpg", "*.jpeg", "*.gif" and "*.tif". |

##### Elements

| Symbol | Object | Instructions |
| --- | --- | --- |
| ![Elements](images/61134008971_DV_resource.Stream@PNG-de-DE.png) | "I/O field" | Outputs the values of a tag, and/or writes values to a tag.  You can define limits for the tag values shown in the I/O field. To hide the operator input in runtime, configure "Hidden input". |
| ![Elements](images/14138241419_DV_resource.Stream@PNG-de-DE.png) | "Button" | Executes a function list, or a script as configured. |
| ![Elements](images/60619802379_DV_resource.Stream@PNG-de-DE.png) | "Symbolic I/O field" | Outputs the values of a tag, and/or writes values to a tag. A text from a text list is displayed in relation to the tag value. |
| ![Elements](images/14137923723_DV_resource.Stream@PNG-de-DE.png) | "Graphic I/O field" | Outputs the values of a tag, and/or writes values to a tag. A graphic from a graphics list is displayed in relation to the tag value. |
| ![Elements](images/14137716107_DV_resource.Stream@PNG-de-DE.png) | "Date/time field" | Outputs the system date and time, or the time and date from a tag. This allows the operator to enter new values. The display format is adjustable. |
| ![Elements](images/14138282635_DV_resource.Stream@PNG-de-DE.png) | "Bar" | The bar represents a value from the PLC in the form of a scaled bar graph. |
| ![Elements](images/61134016779_DV_resource.Stream@PNG-de-DE.png) | "Switch" | Toggles between two defined states. You can label a switch with text, or a graphic. |

##### Controls

| Symbol | Object | Description |
| --- | --- | --- |
| ![Controls](images/14138365323_DV_resource.Stream@PNG-de-DE.png) | "Alarm view" | Shows currently pending alarms or alarm events from the alarm buffer or alarm log. |
| ![Controls](images/14138311051_DV_resource.Stream@PNG-de-DE.png) | "Trend view" | Represents multiple curves with values from the PLC, or from a log. |
| ![Controls](images/14138303115_DV_resource.Stream@PNG-de-DE.png) | "User view" | Allows an administrator to administer users on the HMI device.  It also allows an operator without administrator rights to change their password. |
| ![Controls](images/72306933515_DV_resource.Stream@PNG-de-DE.png) | "HTML Browser"<sup>1)</sup> | Displays HTML pages. |
| ![Controls](images/14138344587_DV_resource.Stream@PNG-de-DE.png) | "Recipe view" | Displays data records, and allows them to be edited. |
| ![Controls](images/21488204555_DV_resource.Stream@PNG-de-DE.png) | "System diagnostics view" | Provides an overview of all devices capable of diagnostics.  Displays errors in the plant. |

<sup>1)</sup>Available for Basic Panels 2nd Generation.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Options for editing objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Objects are graphics elements which you use to design the screens of your project.

You have the following options for editing objects:

- Copying, pasting or deleting objects using the shortcut menu If you copy an object in a screen and the screen already includes an object of the same name, the name of the object is changed.
- Maintaining the standard size of the objects you are inserting or customizing their size on insertion.
- Moving an object in front of or behind other objects
- Rotating objects
- Mirroring objects
- Defining the tab sequence for objects
- Stamping: Inserting several objects of the same type
- Selecting several objects simultaneously
- Repositioning and resizing multiple objects
- You can assign external graphics to objects, e.g. in the Graphic View.

  You can view only the images you have previously stored in the graphic browser of your WinCC project.

  You can save graphics in the graphic browser:

  - Via drag & drop from the "Graphics" object group to the working area
  - As a graphic file in the following formats: *.bmp, *.dib, *.ico, *.emf, *.wmf, *.gif, *.tif, *.svg, *.jpeg or *.jpg
  - As an OLE object

    You either create a new OLE object or save an existing graphic file as an OLE object. To save an OLE object, an OLE-compatible graphics program must be installed on the configuration computer.

---

**See also**

[Inserting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Deleting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#deleting-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Positioning an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#positioning-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Resizing objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#resizing-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting multiple objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-multiple-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Aligning objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#aligning-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Moving an object forwards or backwards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-an-object-forwards-or-backwards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Showing objects outside the screen area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#showing-objects-outside-the-screen-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Rotating objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#rotating-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Flipping objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#flipping-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Inserting multiple objects of the same type (stamping) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-multiple-objects-of-the-same-type-stamping-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Hiding or showing objects (RT Professional)](#hiding-or-showing-objects-rt-professional)
  
[Managing own controls (RT Advanced, RT Professional)](#managing-own-controls-rt-advanced-rt-professional)
  
[External graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#external-graphics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing external graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-external-graphics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Storing an external image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-external-image-in-the-graphics-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)
  
[Repositioning and resizing multiple objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#repositioning-and-resizing-multiple-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Inserting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In the "Screens" or "Reports" editor, insert the objects to the "Toolbox" task card. Use the mouse to drag the objects into the work area. You either keep the objects in their original size, or scale them up or down when you paste them.

In addition, you can copy or move objects via the clipboard from one editor to another, for example to transfer a screen object to a report. Alternatively, you can also use the mouse instead of the clipboard for copying and moving:

- Copy: <Ctrl + Drag&Drop>
- Moving: Drag&drop

  > **Note**
  >
  > **Basic Panels**
  >
  > The "Reports" editor is not available for Basic Panels.

##### Requirement

The "Tools" task card is open.

##### Inserting objects in their standard size

1. In the "Toolbox" task card, select the desired graphic object or the desired graphic in the WinCC graphics folder.

   When you move the cursor across the work area, it turns into a crosshair with an appended object icon.
2. Click the location in the work area where you want to insert the object or graphic.

   The object is inserted with its standard size at the desired position in the work area.

Alternatively, double-click the object in the "Toolbox" task card.

##### Copying an object

1. Select the desired object.
2. Select "Copy" in the shortcut menu.
3. Click the desired location and select "Paste" in the shortcut menu.

WinCC inserts a copy of the object at the desired location. You can only change the properties that are appropriate for the relevant context.

Example: In the "Screens" editor, you can set the mode for input and output for I/O fields. In the "Reports" editor, the mode is set to "Output".

Original and copy are not interconnected and are configured independently from one another.

##### Inserting lines

1. Select the desired graphic object in the "Tools" task card.
2. Click on a location in the work area. A line in the standard size is inserted.

##### Inserting a polygon or polyline

1. Select the desired object "Polyline" or "Polygon" in the "Tools" task card.
2. Click on a location in the work area. This fixes the starting point of the object.
3. Click another location in the work area. A corner point is set.
4. For every additional corner point, click on the corresponding location in the work area.
5. Double-click on a location in the work area. The last corner point is set.

   This fixes all the points of the polygon or polyline.

**Note**

**Basic Panels**

The "Polyline" and "Polygon" objects are not available for Basic Panels.

> **Note**
>
> If you want to insert several objects of the same type, use the "Stamp" function. This avoids having to reselect the object in the "Tools" task card every time before inserting it. To do so, select the ![Inserting a polygon or polyline](images/60629650059_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar of the "Tools" task card.

---

**See also**

[Moving an object forwards or backwards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-an-object-forwards-or-backwards-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Deleting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can delete objects individually or with a multiple selection.

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object that you want to delete.

   To delete multiple objects, keep the <Shift> key pressed and select the objects to be deleted one after the other. Alternatively, drag and maximize an area around the desired objects with the mouse.
2. Select "Delete" from the shortcut menu.

##### Result

The selected objects are deleted.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Positioning an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you select an object, it is enclosed by a rectangle with resizing handles. This rectangle is the selection rectangle. The position of an object is defined by the coordinates of the top left corner of the rectangle surrounding the object.

![Introduction](images/14138611339_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> If the position is outside the work area the object is not displayed in Runtime.

##### Position and align

You have the possibility of having a grid displayed in the work area. You have three options for easier positioning of objects:

- "Snap to grid" When you resposition objects, they are automatically snapped and pasted to the grid. If you hold down the <Alt> key, the object is no longer snapped to the grid.
- "Snap to objects" When you reposition objects, they are displayed with help lines. You can use other objects for orientation during positioning.
- "None": You position the objects in any position.

You activate and deactivate the grid and options as follows:

- In the "Options > Settings > Visualization > Screens" menu
- In the "Layout > Grid" task card

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object you want to move.

   The selected object is framed by a rectangle with resizing handles.

   ![Procedure](images/14138611339_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/14138611339_DV_resource.Stream@PNG-de-DE.png)
2. Left-click the object and keep the mouse button pressed.
3. Move the mouse pointer onto the new position.

   The contour of the object moves with the mouse and displays the new position for the object.

   ![Procedure](images/14138619275_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/14138619275_DV_resource.Stream@PNG-de-DE.png)

   The object initially remains at its original position.
4. Now release the mouse button.

   The object is moved into the position indicated by the contour of the selection rectangle.

##### Alternative procedure

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter the X and Y values for the position under "Position & Size".

##### Result

The object appears at its new position.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Resizing objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you select an object, it is enclosed by a rectangle with handles. You have the following options of resizing an object:

- Drag the handles using the mouse.
- Modify the "Size" property in the Inspector window.

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object you want to resize.

   The selection rectangle appears. The following figure shows a selected object:

   ![Procedure](images/14138611339_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/14138611339_DV_resource.Stream@PNG-de-DE.png)
2. Drag a resizing contact of the rectangle to a new position.

   The size of the object changes.

   - The size of the object is aligned to the grid pattern, provided the "Snap to grid" function is set.
   - Press <ALT> to disable this function while you drag the object.

     In order to scale the object proportionally, keep the <Shift> key pressed while changing the size with the mouse.

##### Alternative procedure

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter the size of the object under "Position & Size".

##### Harmonizing the object size

1. Select the objects.
2. Now, click one of the following buttons: ![Harmonizing the object size](images/25693595659_DV_resource.Stream@PNG-de-DE.png) or ![Harmonizing the object size](images/14139797259_DV_resource.Stream@PNG-de-DE.png) or ![Harmonizing the object size](images/14139800843_DV_resource.Stream@PNG-de-DE.png)

   The size of the selected objects is matched to each other.

The following screen shows how the selected objects are adapted to the height of the reference object:

| Symbol | Meaning |
| --- | --- |
| ![Harmonizing the object size](images/6340523531_DV_resource.Stream@PNG-de-DE.png) | ![Harmonizing the object size](images/10274694667_DV_resource.Stream@PNG-de-DE.png) |

| Icon | Description |
| --- | --- |
| ![Harmonizing the object size](images/14139797259_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the width of the reference object. |
| ![Harmonizing the object size](images/14139800843_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the height of the reference object. |
| ![Harmonizing the object size](images/25693595659_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the width and height of the reference object. |

##### Result

The object now appears with its new size.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Selecting multiple objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Select all objects you want to align with each other or to change global properties. This procedure is called "multiple selection."

The Inspector window shows all the properties of the selected objects.

You now have several options of selecting multiple objects:

- Draw a selection frame around the objects.
- Hold down the <Shift> key, and click the required objects.

##### Selection frame of a multiple selection

The selection frame surrounds all objects of a multiple selection. The selection frame is comparable with the rectangle that surrounds an individual object.

The selection frame is not visible. When you have made your multiple selection, the following frame is displayed:

- The reference object is indicated by the rectangle around it.
- The other selected objects are indicated by a dashed-line frame.

##### Specifying a reference object

The reference object is the object upon which the other objects are oriented. The reference object is framed by a rectangle with handles. The following figure shows a reference object with two other selected objects:

![Specifying a reference object](images/23810439179_DV_resource.Stream@PNG-de-DE.png)

You have the following options to specify the reference object:

- Select the objects via multiple selection. The object selected first is then the reference object.
- Draw a selection frame around the objects. The reference object compiled automatically. If you wish to specify a different object within the selection as the reference object, click on the desired object. This action does not cancel your multiple selection.

##### Requirement

You have opened the work area containing at least two objects.

##### Selecting multiple objects with a selection frame

1. Position the mouse pointer in the work area close to one of the objects to be selected.
2. Hold down the mouse button, and draw a selection frame around the objects to be selected.

Or:

1. Hold down the <Shift> key.
2. Click the relevant objects, working in succession.

   All the selected objects are identified by frames.

   The object selected first is identified as reference object.

**Note**

To remove an object from the multiple selection, press <SHIFT>, hold it down and then click the relevant object once again.

##### Result

Multiple objects are selected. One of those is identified as the reference object. You can now perform the following steps:

- Changing the object properties of all the objects
- Resizing all the objects by the same ratio, by dragging the selection frame to increase or reduce the size
- Moving all the objects in one group
- Aligning the objects to the reference object

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Aligning objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Procedure

1. Select the objects via multiple selection.
2. Specify an object as the reference object.
3. Select the desired command in the toolbar or the shortcut menu - see table below.

   The selected objects will be aligned.

##### Aligning objects flush

The selected objects will be aligned flush to the reference object.

| Icon | Description |
| --- | --- |
| ![Aligning objects flush](images/14138671627_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the left edge of the reference object. |
| ![Aligning objects flush](images/14139626763_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the vertical center axis of the reference object. |
| ![Aligning objects flush](images/13283458059_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the right edge of the reference object. |
| ![Aligning objects flush](images/14139673355_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the upper edge of the reference object. |
| ![Aligning objects flush](images/14139681035_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the horizontal center axis of the reference object. |
| ![Aligning objects flush](images/14139701771_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the lower edge of the reference object. |
| ![Aligning objects flush](images/14139747851_DV_resource.Stream@PNG-de-DE.png) | Centers the selected objects to the center points of the reference object. |
| ![Aligning objects flush](images/25602636683_DV_resource.Stream@PNG-de-DE.png) | Centers the selected objects vertically in the screen. |

##### Snap to object

When you reposition objects, they are displayed with help lines. You can use other objects for orientation during positioning.

![Snap to object](images/41595801227_DV_resource.Stream@PNG-de-DE.png)

If you are working with the keyboard, press the Alt key. When you move the selected object with the arrow keys, the next anchor point is displayed.

##### Distributing objects evenly

You need at least three selected objects. A reference object is not required.

1. Select the objects.
2. Click one of the buttons "Distribute horizontally equal" or "Distribute vertically equal".

   The selected objects are distributed at equal distances.

The following screen shows how you align the vertical spacing of the selected objects:

| Symbol | Meaning |
| --- | --- |
| ![Distributing objects evenly](images/41609043211_DV_resource.Stream@PNG-de-DE.png) | ![Distributing objects evenly](images/41610037643_DV_resource.Stream@PNG-de-DE.png) |

| Icon | Description |
| --- | --- |
| ![Distributing objects evenly](images/14139755787_DV_resource.Stream@PNG-de-DE.png) | Aligns the horizontal distance between the objects.   The position of the objects on the extreme left and right side remains unchanged. All other objects are distributed evenly between them. |
| ![Distributing objects evenly](images/14139759627_DV_resource.Stream@PNG-de-DE.png) | Aligns the vertical distance between the objects.   The position of the objects at the extreme top and bottom (right and left) remains unchanged. All other objects are distributed evenly between them. |

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Moving objects with keyboard shortcuts (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can move the objects in the screen by using shortcut keys or select them by type.

##### Controlling objects with the keyboard

| Function | Keyboard shortcut |
| --- | --- |
| Moves the selected screen object to the left to the first available vertical alignment position. | <Alt+Shift+Left> |
| Moves the selected screen object to the right to the first available vertical alignment position. | <Alt+Shift+Right> |
| Moves the selected screen object up to the first available horizontal alignment position. | <Alt+Shift+Up> |
| Moves the selected screen object down to the first available horizontal alignment position. | <Alt+Shift+Down> |
| Selects all screen objects of this type. | <Ctrl+Shift+A> |
| Selects all objects that support the use styles. | <Ctrl+Shift+D> |

#### Moving an object forwards or backwards (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can use the "Order" functions in the shortcut menu of a selected object or in the toolbar to move a selected object in front of or behind other objects within an object layer.

> **Note**
>
> ActiveX controls are always positioned in front of an object layer (.NET property).

##### Requirement

You have opened a screen which contains a layer with multiple objects.

##### Procedure

1. Select the object you want to move forward or backward.
2. Select the "Sort" command and one of the following commands from the shortcut menu:

| Icon | Description |
| --- | --- |
| ![Procedure](images/14139870219_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object before all the other objects of the same layer |
| ![Procedure](images/14139873803_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object to the lowest position in the same layer |
| ![Procedure](images/14824879627_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object up by one position |
| ![Procedure](images/14824887563_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object down by one position |

##### Alternative procedure

1. Open the "Layers" palette of the "Layout" task card.
2. Navigate to the required object.
3. Hold down the mouse button, and drag the object in the tree topology to the required position in the layer.
4. Now release the mouse button.

##### Result

The object is moved up or down.

---

**See also**

[Inserting an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Showing objects outside the screen area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

If you assign objects to positions that are outside the configurable area, these objects will be hidden. The functions of the "Objects outside the visible area" palette in the "Layout" task card are used to move these objects back into the screen.

##### Requirement

- You have opened a screen which contains objects that are outside the configurable area.
- The "Layout" task card is open.

##### Procedure

1. Open the "Layout > Objects outside the area" task card.

   This displays a list of objects that are outside the configurable area.
2. Select the the object which you want to move back into the screen from the list.
3. Select "Move to screen" in the object shortcut menu.

Alternatively open the "Layout > Layer" task card. Objects outside the area are indicated by the ![Procedure](images/14146121867_DV_resource.Stream@PNG-de-DE.png) icon. If you click this icon, the object is moved back into the screen.

##### Result

The objects are moved to the configurable area.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Rotating objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can rotate a suitable object clockwise or counterclockwise around its center axis in steps of 90°.

> **Note**
>
> Not all the objects can be rotated. Some objects that can be rotated in screens cannot be rotated in reports.

You can also rotate multiple objects using the multiple selection function. Certain WinCC objects such as buttons cannot be rotated.

The alignment of elements in an object will change in a rotated object. The following figure shows how a rectangle and an ellipse behave under the different commands for rotating an object:

![Introduction](images/14146396043_DV_resource.Stream@PNG-en-US.png)

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object that you want to rotate.
2. Click one of the following toolbar icons:

   ![Procedure](images/14146129803_DV_resource.Stream@PNG-de-DE.png), to rotate the object clockwise around its center point. The angle of rotation is 90°.

   ![Procedure](images/14146133387_DV_resource.Stream@PNG-de-DE.png), to rotate the object counterclockwise around its center point. The angle of rotation is 90°.

   ![Procedure](images/14146354571_DV_resource.Stream@PNG-de-DE.png), to rotate the object clockwise by 180°.

##### Result

The object is shown at its new angle.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Flipping objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can flip an object along its vertical or horizontal center axis. The alignment of elements in an object will change when you flip an object. The following figure shows how a rectangle and an ellipse behave under the different commands for flipping an object.

![Introduction](images/14658859147_DV_resource.Stream@PNG-en-US.png)

##### Requirement

You have opened a screen which contains at least one object.

##### Procedure

1. Select the object that you want to flip.
2. Click the "Flip" command in the shortcut menu and select one of the options displayed:

   - ![Procedure](images/14146613259_DV_resource.Stream@PNG-de-DE.png), to flip the selected object along its vertical center axis.
   - ![Procedure](images/14146617099_DV_resource.Stream@PNG-de-DE.png), to flip the selected object along its horizontal center axis.

##### Result

The object is shown at its flipped position.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Designing an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You design the border and background of an object.

##### Requirements

A line has been created in a screen.

##### Procedure

1. Select the line on your screen.
2. In the Inspector window, select "Properties > Properties > Appearance":
3. Select "Dash" as the style.
4. To display the dashed line in two colors, select the line width "1".
5. Select the setting "Arrow" in the "Line ends" area.

##### Result

The line is displayed in two colors as a dashed line. The end of the line is an arrow.

---

**See also**

[Overview of objects (RT Professional)](#overview-of-objects-rt-professional)

#### Designing an object (RT Professional)

##### Introduction

You design the border and background of an object.

##### Requirement

A circle has been created in a screen.

##### Procedure

1. Select the circle in the screen.
2. In the Inspector window, select "Properties > Properties > Appearance":
3. Select "Solid" as the background fill pattern.
4. Activate "Fill level".
5. Enter "50" for the fill level.
6. Select "Solid" as the style.

##### Result

The object is displayed as a semicircle without a border.

---

**See also**

[Overview of objects (RT Professional)](#overview-of-objects-rt-professional)

#### Designing the fill pattern (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC lets you design the background color and the fill pattern of an object. The design options change in the Inspector window depending on object for which you are making the filling pattern.

For certain objects, you can not only define the color, but also a transparent background or a background with a color gradient.

> **Note**
>
> ****Device-specific nature of the properties****
>
> The fill style that is available depends on the object and the HMI device used.

##### Requirement

The object has been created and selected.

##### Designing the background color of an object

1. In the Inspector window, select "Properties > Properties > Appearance".
2. Select a color for the background of the object, for example, yellow.

   The object is filled with the selected color.

   ![Designing the background color of an object](images/70721322251_DV_resource.Stream@PNG-en-US.png)

   ![Designing the background color of an object](images/70721322251_DV_resource.Stream@PNG-en-US.png)

##### Designing the fill pattern of an object

1. In the Inspector window, select "Properties > Properties > Appearance".
2. To define a transparent background for the object, select transparent.

   You can find information about designing a fill pattern with a color gradient in the section [Defining color gradients](#defining-color-gradients-basic-panels-panels-comfort-panels-rt-advanced-rt-professional).

   The object is shown as transparent.

   ![Designing the fill pattern of an object](images/74903800075_DV_resource.Stream@PNG-en-US.png)

   ![Designing the fill pattern of an object](images/74903800075_DV_resource.Stream@PNG-en-US.png)

You can optionally set the fill pattern in the Inspector window under "Properties > Properties > Fill Pattern".

---

**See also**

[Defining color gradients (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-color-gradients-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Specifying scroll bars (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

You can use the scroll bars for navigation in the table-based objects:

- Use the scroll arrows to scroll line by line either up or down or from left to right in the view.
- Use the scroll box in the scroll bar to scroll slowly to the required position in an object.
- Click on the scroll box to navigate quickly in the object through a large volume of data.

> **Note**
>
> On HMI devices with keys, you can move the scroll bar with arrow keys.
>
> In pop-up screens, use <ALT>+<arrow key> to scroll.

In WinCC version V14 and higher, you can configure different colors for the scroll bars.

##### Scrolling in controls

Two display options for scrolling are available under "Runtime settings > Screens > Scrolling in controls":

- Scroll bar with scroll arrows for devices with device version V14 or higher

  The scroll bar is displayed in the screen object with scroll arrows and scroll box.
- Scroll indicator

  A scroll indicator is shown in the screen object

In the Engineering System, you can see the scroll preview in all controls with the exception of HTML browser, PDF display and NC partial program display.

> **Note**
>
> The display of scroll indicators is not supported in the PLC code display or in the pop-up screens.

##### Showing all data

The scroll bars are used to display content in limited space on the screen. Please remember in configuration that the scroll bars themselves take up space in the control. The width and height of the scroll bars vary depending on the screen resolution.

If you configure a control to display just a few lines, the scroll bars may cover the content in runtime. To avoid hiding the data, take account of the scroll bars in configuration.

> **Note**
>
> When configuring the user display, avoid the setting "Fit object to contents". This setting calculates the object size in runtime automatically and cannot be changed.

##### Configuring scroll bar colors

You can configure the color of the scroll bar in conjunction with other colors for certain objects.

- The scroll bar arrows and scroll box are shown in the text color of the table
- The scroll bar background color is the alternative color of the table

> **Note**
>
> In the objects graphic I/O field, HTML browser, PDF display and file browser, the scroll bar colors cannot be changed.

##### Example

This example shows the configuration of scroll bar colors for an alarm view.

1. Open "Properties > Properties > Appearance".
2. Select a color for the table foreground, for example "blue" for the scroll arrows and the scroll box in the scroll bar.
3. Select the alternative color, for example "yellow" for the even rows in the table and the background of the scroll bar.

   The scroll bar is displayed in the configured colors.

   ![Example](images/84980317579_DV_resource.Stream@PNG-en-US.png)

   ![Example](images/84980317579_DV_resource.Stream@PNG-en-US.png)

#### Using predefined styles (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can assign predefined styles to objects and faceplates in runtime. You can change the background color of the display and operating elements using predefined styles. In this way, you harmonize the display in Runtime.

##### Requirement

The "Toolbox" task card is open.

##### Setting predefined styles

1. Select the object that you want to insert in the "Toolbox" task card.
2. Select one of the following options in the "Toolbox" task card:

   - "Default" to use the default style
   - "Use device design" to use the color settings from the current device design
3. Insert the required object in the work area.

   The object is displayed in the selected style.
4. The objects are created in the selected style as long as the style remains activated in the toolbar.

   To return to the default style, select the "Default" option in the toolbar.

---

**See also**

[Working with styles and style sheets (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-styles-and-style-sheets-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Formatting text in an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Some objects, for example, the I/O field, support text within the object.

You have several options to align text.

##### Configuring the distance from the object border

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter the value "5" for the left border, for example.

The text is aligned five pixels from the left border of the object.

##### Aligning the text position

1. In the Inspector window, select "Properties > Properties > Text format".
2. Select the horizontal alignment, for example, centered.
3. Select the vertical alignment, for example, top.

   The text is shown at the top center in the object.

##### Defining the text orientation

1. In the Inspector window, select "Properties > Properties > Text format".
2. Select the orientation of the text, for example, vertical, right.

   The text flow is shown from bottom to top.

#### Connecting tags and text lists in the text (RT Advanced)

##### Introduction

Comfort Panels and WinCC Runtime Advanced give you the option to add output fields for tags or entries to a text list for the following objects:

- Symbolic I/O field
- Text field

> **Note**
>
> The symbolic I/O field supports the connection of tags and text list entries in the "Two states" mode.

##### Requirement

- The object has been created and selected

##### Connecting tags in a text field

1. Open "Properties > Properties > General" in the inspector window.
2. Open the shortcut menu of the input field.

   ![Connecting tags in a text field](images/66258430859_DV_resource.Stream@PNG-en-US.png)

   ![Connecting tags in a text field](images/66258430859_DV_resource.Stream@PNG-en-US.png)
3. Select the command "Insert parameter field ...".  
   A dialog opens.
4. Select the tag and the format in which you want to display the tag.
5. Confirm your entries.

The name of the connected tag is displayed in the text field of the object.

##### Connecting the text list

1. Open "Properties > Properties > General" in the inspector window.
2. Open the shortcut menu of the input field.
3. Select the command "Insert text list field ...".  
   A dialog opens.
4. Select the text list from which a text entry is displayed.
5. Confirm your entries.

The reference to the text list entry is displayed in the text field of the object.

> **Note**
>
> The number of references to text list entries that in turn include references to text list entries or tags is limited to three layers.

#### Formatting graphics in an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC lets you insert graphics into some objects and format them. You can change the size, orientation and distances of a graphic to the object border. You change the properties of the graphic in the Inspector window of the relevant object.

##### Requirement

- The selected object is in graphic mode.
- The selected object contains at least one graphic.

##### Resizing a graphic

1. In the Inspector window, select "Properties > Properties > Layout".
2. Select "No stretching of picture" or "Stretch picture".

   The contained graphic is displayed in its original size or stretched to the size of the object.

> **Note**
>
> To adjust the object size to the contained graphic, select "Fit object to contents".

##### Aligning a graphic horizontally and vertically

1. In the Inspector window, select "Properties > Properties > Layout".
2. To determine the horizontal position of the graphic, select "Right", for example.
3. To determine the vertical position of the graphic, select "Top", for example.

   The graphic is then shown at the top right of the object.

![Aligning a graphic horizontally and vertically](images/60039271563_DV_resource.Stream@PNG-de-DE.png)

##### Defining the distance from the object border

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter the value for the distance to the object border, for example, "20" for the top border.

   The graphic is shown with a distance of 20 pixels to the top border of the object.

![Defining the distance from the object border](images/60039856139_DV_resource.Stream@PNG-de-DE.png)

| Icon | Description |
| --- | --- |
| ![Defining the distance from the object border](images/60039864971_DV_resource.Stream@PNG-de-DE.png) | Sets the distance from the left border of the object. |
| ![Defining the distance from the object border](images/60047681547_DV_resource.Stream@PNG-de-DE.png) | Sets the distance from the right border of the object. |
| ![Defining the distance from the object border](images/60047933323_DV_resource.Stream@PNG-de-DE.png) | Sets the distance from the top border of the object. |
| ![Defining the distance from the object border](images/60047941899_DV_resource.Stream@PNG-de-DE.png) | Sets the distance from the bottom border of the object. |

#### Rotating an object in runtime (RT Professional)

##### Introduction

You define the rotation of an object around a reference point. You define the reference point with "X", "Y" in the Inspector window in the group "Properties > Properties > Layout".

The rotation of the object is visible in Runtime only.

![Introduction](images/15317686539_DV_resource.Stream@PNG-en-US.png)

##### X, Y

The attributes "X" and "Y" define the horizontal and vertical distance of the reference point from the object origin.

The values are specified as a percentage. The object width or object height correspond to a value of 100%. The reference point value can be outside the selection rectangle. This means that both negative values and positive values higher than 100% are possible.

##### Angle

The angle defines the rotation of an object around the reference point. The angle is specified in degrees. The configured start point corresponds to a value of 0°. The position of an object deviates from its configured start position by the value of the angle.

---

**See also**

[Polygon (Panels, Comfort Panels, RT Advanced, RT Professional)](#polygon-panels-comfort-panels-rt-advanced-rt-professional)
  
[Polyline (Panels, Comfort Panels, RT Advanced, RT Professional)](#polyline-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Designing table-based objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC offers various properties for designing display and operating objects.

You change the properties of table-based objects in the Inspector window of the relevant object.

##### Designing colors

Select the colors for font, selections and areas under "Properties > Properties > Appearance".

![Selecting table properties](images/57306182155_DV_resource.Stream@PNG-en-US.png)

Selecting table properties

##### Designing the border of the table header

1. In the Inspector window, open "Properties > Properties > Table header border".
2. Select "Solid", for example, as the style.
3. Select 5, for example, as the "Width".
4. Select red, for example, as a foreground color.

The border of the table header is shown with a red border and width of 5 pixels. With "Solid" border style, only the foreground color is visible.

##### Colors and color gradient in the table header

1. Select the table-based object in the screen.
2. In the Inspector window, open "Properties > Properties > Table header fill pattern".
3. Select the fill pattern, for example "Horizontal gradient".
4. Select a background color, for example, blue, under "Gradient".
5. Activate "Gradient 1".
6. Select a color for "Gradient 1", for example, white.
7. Select a "Width" for the color gradient, for example, 12.
8. Activate Gradient 2.
9. Select a color for Gradient 2, for example, yellow.
10. Select a "Width" for the color gradient, for example, 10

The table header is displayed with a color gradient.

#### Designing a border (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC offers various properties for designing display and operating objects.

The I/O field example below shows the possible settings for designing borders.

You change the appearance in the Inspector window of the relevant object.

##### Designing a border

1. Open "Properties > Properties > Appearance".
2. Select the width of the border, e.g. "5".
3. Select the style of the border, e.g. double line.
4. Select the foreground color.
5. Select the background color.

!["Double line" border style](images/57299593611_DV_resource.Stream@PNG-en-US.png)

"Double line" border style

##### Border style

The figure below shows a border in "3D style".

![Border style](images/59586799755_DV_resource.Stream@PNG-de-DE.png)

The figure below shows a border in "Solid" style.

![Border style](images/59586804363_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Device-specific nature of the properties**
>
> The border style that is available depends on the object and the HMI device used.

#### Defining color gradients (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

For the objects in WinCC, color gradients can be specified as background for various surfaces.

Change the category in the Inspector window, depending on which surface you fill with a color gradient. The procedure remains the same.

The following section describes how to configure the color gradient of buttons.

##### Horizontal color gradient with two colors

1. Select an object with buttons, for example, a button.
2. In the Inspector window, select "Properties > Properties > Fill Pattern".
3. Select "Fill Pattern > Horizontal gradient".
4. Select a background color for the vertical color gradient, for example, orange.
5. Activate "Gradient 1".
6. Select a "Color" for Gradient 1, for example, red.
7. Select a "Width" for Gradient 1, for example, "10".

![Horizontal color gradient with two colors](images/61129207179_DV_resource.Stream@PNG-de-DE.png)

The background of the button is displayed in orange.

For the horizontal color gradient, Gradient 1 is shown from the left border. Gradient 1 is 10 pixels wide.

##### Vertical color gradient with three colors

1. Select a button in the screen.
2. In the Inspector window, select "Properties > Properties > Fill Pattern".
3. Select the "Vertical gradient" background.
4. Select a background color under "Gradient", for example, orange.
5. Activate "Gradient 1".
6. Select a color for "Gradient 1", for example, red.
7. Select a "Width" for the color gradient, for example, 8.
8. Activate Gradient 2.
9. Select a color for Gradient 2, for example, yellow.
10. Select a "Width" for the color gradient, for example, 10.

| Symbol | Meaning |
| --- | --- |
| ![Vertical color gradient with three colors](images/60575686027_DV_resource.Stream@PNG-de-DE.png) | ← Color Gradient 1 |
| ← Background color |  |
| ← Color Gradient 2 |  |

For the vertical color gradient, Gradient 1 is shown from top to bottom. Gradient 1 is 8 pixels wide.

The background of the button is displayed in orange.

Gradient 2 is shown at the bottom border. Gradient 2 is 10 pixels wide.

#### Configuring ranges (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

As of WinCC V14, you have the option of defining up to five value ranges for the "Gauge", "Bar" and "Slider" objects and configuring them centrally in a process tag. This means you can, for example, distinguish between different operating states with different colors. To display the ranges defined in the tag in the screen object, activate the option "Display ranges of tags" in the Inspector window under "Properties > Limits/Ranges".

This setting is not available for display with inner scale, for example, the option "Layout with inner bar" must be cleared for the bar.

You define the following five ranges:

| Limit/range | Use |
| --- | --- |
| Upper 2 | Displays the high danger range. |
| Upper 1 | Displays the high warning range. |
| Normal | Displays the normal range. |
| Lower 1 | Displays the low warning range. |
| Lower 2 | Displays the low danger range. |

##### Limits/ranges

You specify limits for numerical values to restrict the value range. This range is defined by a high limit and a low limit. You specify the use and color of ranges as well as the maximum and minimum values at the screen object.

![Limits/ranges](images/84746487179_DV_resource.Stream@PNG-en-US.png)

You can find additional information on limits under "[Defining limits for a tag](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#defining-limits-for-a-tag-basic-panels-panels-comfort-panels-rt-advanced)".

##### Requirements

- You have created at least one tag.
- You have defined four ranges at the tag.
- You have created the screen object.

##### Configuring ranges

1. Specify the tag that defines the ranges for the screen object under "Properties > General > Process tag".
2. If necessary, specify the values for maximum and minimum.
3. Select the option "Display ranges of tags" under "Properties > Limits/Ranges".

   ![Configuring ranges](images/88009370763_DV_resource.Stream@PNG-en-US.png)

   ![Configuring ranges](images/88009370763_DV_resource.Stream@PNG-en-US.png)
4. Specify which ranges are displayed in the object.
5. You can change the default colors for the ranges, if required.

##### Result

You have configured ranges in a screen object. The ranges are displayed in different configured colors in Runtime.

![Result](images/86886460939_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Defining Limits for a Tag (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#defining-limits-for-a-tag-basic-panels-panels-comfort-panels-rt-advanced)
  
[Bar (RT Professional)](#bar-rt-professional)

#### Flashing (Panels, Comfort Panels, RT Advanced)

##### Introduction

You want an object to flash in Runtime.

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object that you want to flash.
2. In the Inspector window, select the type "Standard enabled" under "Properties > Properties > Flashing".

##### Result

The object flashes in runtime.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Flashing (RT Professional)

##### Introduction

You display objects flashing in runtime. You select the flash rate and colors for the object.

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object that you want to flash.
2. In the Inspector window, select the type "Advanced" under ""Properties > Properties > Flashing".
3. Activate "Line" to make the line flash in runtime.
4. Activate "Text" to make the text flash in runtime.
5. Activate "Background" to make the background flash in runtime.
6. Select the flash rate.
7. Select a color for the "OFF" state.
8. Select a color for the "ON" state.

**Note**

Flashing is only visible in runtime when there is a difference between the two colors.

##### Result

In runtime, the object flashes in the selected colors and flash rate.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Inserting multiple objects of the same type (stamping) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC offers the possibility to "stamp" several objects of the same type directly one after the other, i.e. paste without having to reselect the object every time. In addition you have the possibility of multiplying an object that has already been inserted.

##### Requirement

The "Tools" task card is open.

##### Inserting several objects of one type

1. Select the object that you want to insert in the "Tools" task card.
2. Click the ![Inserting several objects of one type](images/60629650059_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar of the "Tools" task card.

   The "Stamp" function is activated.
3. To insert the object with its standard size, click the relevant insertion position in the work area.

   To insert the object with another size, position the mouse pointer at the desired location in the work area. Press the left mouse button and drag the object to the required size.

   The object is inserted in the work area as soon as you release the mouse button.
4. Repeat step 3 to insert further objects of the same type.
5. Click the ![Inserting several objects of one type](images/60629650059_DV_resource.Stream@PNG-de-DE.png) icon again.

   The "Stamp" function is deactivated.

**Note**

You can copy existing objects using the drag-and-drop +<CTRL> function. The existing object is not moved in this case. You paste a copy of this object into the new position instead.

##### Inserting and multiplying an object

1. Insert the desired object from the "Tools" task card.
2. Press the <Ctrl> key and position the cursor on one of the handles displayed in the figure shown below.

   ![Inserting and multiplying an object](images/6340346507_DV_resource.Stream@PNG-en-US.png)

   ![Inserting and multiplying an object](images/6340346507_DV_resource.Stream@PNG-en-US.png)
3. Drag the handles to the right and/or down while keeping the left mouse button pressed.
4. The object is multiplied depending on available space if you keep moving the cursor.

   ![Inserting and multiplying an object](images/8144852875_DV_resource.Stream@PNG-de-DE.png)

   ![Inserting and multiplying an object](images/8144852875_DV_resource.Stream@PNG-de-DE.png)

##### Result

You have pasted and stamped an object in a screen.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Repositioning and resizing multiple objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Possible modifications

After you have selected multiple objects, you edit them:

- Shift using the mouse

  - To change the absolute position of the marked objects, position the mouse pointer over an object, and shift the multiple selection with the mouse button pressed.
  - To resize all the objects by the same ratio, grab the resizing handles of the reference object.
- Move over the work area with the icons of the toolbar

  - Change the position of the marked objects with respect to each other
  - Align the height and width of the marked objects
- Moving with the shortcut menu commands of the work area

  - Change the position of the marked objects with respect to each other
  - Align the height and width of the marked objects

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Hiding or showing objects (RT Professional)

##### Introduction

You can hide and show objects from or up to a defined size. This means, for example, that objects are only shown if a sufficient size allows the required detail to be displayed.

##### Requirement

A screen is open.

##### Procedure

Proceed as follows to hide specific objects in a screen:

1. Click in an area of the screen that does not contain an object.
2. Activate the "Activate for objects" check box under "Hide/Show" in the Inspector window.
3. Specify the minimum and maximum percentage within which the objects in question should be displayed. The specified limit values are also still shown.

##### Result

Those objects are shown whose size lies within the specified range when the object layer is visible. The object continues to be displayed as long as either the height or the width lies within the specified range.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Linking user data types with objects (RT Professional)

##### Introduction

If you work with user data types, only create a user type once and then use it multiple times for objects, animations, feature lists and scripts. If, for example, a component is used more than once in your system, you can link the component with a suitable user type that contains structured subelements for each lower-level component.

You assign a user data type defined in the project library to a screen and link the elements of this user data type to objects. The elements of a user data type can be used for screens and screen objects instead of HMI tags or PLC tags. You use them for animations, function lists and scripts, for example.

##### Procedure

1. Select the "Use user data type" check box under "Properties > Properties > User data type" in the Inspector window.
2. In the "User data type" selection list, select a HMI user data type or PLC user data type from the project library that you want to assign to the screen.

   ![Procedure](images/71790659211_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/71790659211_DV_resource.Stream@PNG-en-US.png)

The user data type is assigned to the screen.

##### Linking elements of a user data type with objects

1. Insert in the screen an object that you want to link to an element of a user data type.
2. In the Inspector window under "Properties > Properties > General", select the element from the "Tag" selection list that you want to link to the object.

   ![Linking elements of a user data type with objects](images/71793983243_DV_resource.Stream@PNG-en-US.png)

   ![Linking elements of a user data type with objects](images/71793983243_DV_resource.Stream@PNG-en-US.png)

   Alternatively, you can link the element using autocomplete.

> **Note**
>
> You can recognize by the point prefixed to the element name that an element of a user data type in the "Tag" selection list has been used.
>
> The "@NOP" prefix indicates that an HMI tag or a PLC tag in the "Tag" selection list was used.

##### Comments

- If you disable the "Use user data type" check box under "Properties > Properties > User data type", the link between the element and the object is removed.
- If you assign the screen a different user data type, the link between the element and the object is removed. However, if an identically named element is contained in the new user data type on the same structural level, the link between the element and the object is retained.
- If you rename the element, the link between the element and the object is removed.
- If you change the data type of the element, the link between the element and the object is retained.

---

**See also**

[Configuring a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Working with user data types (Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-user-data-types-panels-comfort-panels-rt-advanced-rt-professional)

#### Managing own controls (RT Advanced, RT Professional)

##### Introduction

You can use your own controls in the WinCC editions "WinCC Advanced" and "WinCC Professional". Add standardized or user-defined controls in the "Toolbox > My Controls" task card. The configuration of user-specific controls on levels is not supported. User-specific controls are always positioned in the foreground in runtime.

The ActiveX controls registered in the operating system and the .Net controls on your system are available for use in WinCC.

- ActiveX controls are operator controls from any providers, which can be used by other programs over a defined OLE-based interface. For reasons of stability and performance, not all registered Active X controls can be configured in WinCC. Only the controls visible in the selection dialog can be used in WinCC.

  > **Note**
  >
  > Under certain circumstances, ActiveX controls are displayed differently in the Engineering System. If problems occur in the display, use .Net Controls.
- .Net controls are operator controls from any providers based on the Microsoft .Net Framework. Only the simple .Net controls are supported. XAML controls, for example, WPF (Windows Presentation Foundation) controls, are not supported in the TIA Portal. Further, the use of parameters is not supported with .Net controls.
- Specific .Net controls are user-defined .Netcontrols based on the Microsoft .Net Framework.

If the name of an event of a control contains the character string "Changed", this event is not displayed in WinCC. If you are using arbitrary controls in your project, which are not included in the scope of delivery, you must first of all add these to "My controls" before you copy the project to other PCs.

> **Note**
>
> If you use any controls that are not included in the scope of delivery (for example, from third parties), errors might occur, for example, reduced performance or system crashes. You must therefore check whether these controls are executable on the HMI device.
>
> The user of such control software is alone responsible for any problems caused by its use. We therefore advise you to closely examine such elements prior to their use.

##### Requirement

- The required ActiveX control is installed in the PC's operating system.
- The desired .Net control is available on the PC in an assembly.
- A screen is open.
- The "Toolbox" task card is open.

##### Adding a new control to the "My controls" group

1. Open "Toolbox > My controls" in the "Toolbox" task card.
2. Select "Select objects" from the shortcut menu.

   A dialog opens. This contains all the controls available on the system. Controls that already exist in the "Toolbox" task card are identified by a check mark.

   ![Adding a new control to the "My controls" group](images/56171238027_DV_resource.Stream@PNG-en-US.png)

   ![Adding a new control to the "My controls" group](images/56171238027_DV_resource.Stream@PNG-en-US.png)
3. Select the desired tab, e.g. ActiveX controls.
4. Activate the required control.
5. Confirm your selection with "OK".

##### Inserting a custom .Net control in the "My controls" group

1. Select the "Custom .Net controls" tab. The list is empty the first time you select the tab.
2. Click the "…" button.
3. Select the folder in which the assembly is contained.
4. Select a file.
5. Click "Open." All the available controls are displayed in the "Custom .Net controls" tab.
6. Activate the required .Net control.
7. Confirm your selection with "OK".

> **Note**
>
> **.Net controls in Runtime Advanced**
>
> If you have incorporated a .Net control in your project as "Custom .Net control", you have to copy the files belonging to these controls to the installation directory of WinCC Runtime, e.g. "C:\ProgramFiles\Siemens\Automation\WinCC RT Advanced". Otherwise, the control cannot be loaded in Runtime.

> **Note**
>
> **.Net-Controls in Runtime Professional**
>
> When the software is loaded to the HMI device, .Net controls are not transferred. The .Net control might have to be transmitted separately. The .Net control must be located on the HMI device in the directory provided or registered using regsvr32.

##### Result

The control now appears in the "Toolbox > My controls" task card and can be configured in a screen.

##### Removing a control from the "My controls" group

1. Select "Delete" from the shortcut menu for the control concerned.

   The control is removed from the "My controls" group.

##### Synchronization of the ActiveX controls

Changes to properties of ActiveX controls are only saved if the control synchronizes the OCXState property correctly in the case of changes.

For controls such as "Microsoft Date and Time Picker Control" that do not synchronize the OCXState property correctly, the changes are discarded after the screen is closed, during compilation or after the migration.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### External graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can use graphics created with an external graphic program in WinCC. To use these graphics you store them in the project graphics of the WinCC project.

You can save graphics in the project graphics:

- When you drag-and-drop graphics objects from the "Graphics" pane into the work area, these are stored automatically in the project graphics. The graphic names are numbered in the order of their creation, for example, "Graphic_1." Use the <F2> function key to rename the graphic.
- As a graphic file with the following formats:

  *.bmp, *.ico, *.emf, *.wmf, *.gif, *.tif, *.png, *.svg, *.jpeg, *.jpg

  > **Note**
  >
  > All file formats are downloaded to the devices and saved as bitmap (*.png/*.jpg). Due to the conversion, vector formats pixelate, resulting in visible artifacts in different resolutions. It is therefore recommended to use several graphics that are customized to the target resolution.
- As an OLE object that is embedded in WinCC and is linked to an external graphic editor. In the case of an OLE link, you open the external graphic editor from WinCC. The linked object is edited using the graphic editor. An OLE link only works if the external graphic editor is installed on your PC, and supports OLE.

##### Use of graphics from the project graphics

Graphics from the project graphics are used in your screens:

- In a Graphic view
- In a graphic list
- As labeling for a button/function key

##### Transparent graphics

In WinCC you also use graphics with a transparent background. When a graphic with a transparent background is inserted into a graphic object of WinCC, the transparency is replaced by the background color specified for the graphic object. The selected background color is linked firmly with the graphic. If you use the graphic in another graphic object of WinCC, this object is displayed with the same background color as the graphic object that was configured first. If you want to use the graphic with different background colors, include this graphic in the project graphics again under a different name. The additional background color is configured when the graphic is used at the corresponding graphic object of WinCC.

> **Note**
>
> **Transparent graphics in WinCC Professional**
>
> Transparent graphics and graphics with the format *.svg are not supported in WinCC Classic Design.

##### Managing graphics

An extensive collection of graphics, icons and symbols is installed with WinCC, for example:

In the Toolbox window of the "Graphic" pane the graphic objects are structured by topic in the "WinCC graphics folder." The link to the WinCC graphics folder cannot be removed, edited or renamed.

The "Graphics" pane is also used to manage the external graphics. The following possibilities are available:

- Creating links to graphics folders

  The external graphic objects in this folder, and in the subfolders, are displayed in the toolbox and are thus integrated in the project.
- Editing folder links
- You open the program required for editing of the external graphic in WinCC.

##### Restrictions on SVG graphics

SVG graphics are converted to Siemens SVG Standard. Note the following restrictions when using SVG graphics:

- The CSS definitions are converted to inline attributes.
- The embedded scripts and non-local URL links are not supported in the SVG graphics and are removed from the original graphics during conversion.
- The use of SVG graphics with embedded animations is not supported.
- The use of large SVG graphics affects performance due to the load associated with the increased characters.

The representation of SVG graphics depends on the browser used.

##### Editing SVG graphics

It is not possible to open SVG graphics in an external editor using the "Edit" command.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Managing external graphics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

External graphics that you want to use in WinCC are managed in the "Screens" editor by using the "Tools" task card in the "Graphics" pane.

##### Requirement

- The "Screens" editor is open.
- The "Tools" task card is open.
- The graphics are available.
- The graphics have the following formats:

  *.bmp, *.ico, *.emf, *.wmf, *.gif, *.tif, *.svg, *.jpeg or *.jpg

##### Creating a folder link

1. Click "My graphics folder."
2. Select "Link" in the shortcut menu.

   The "Create link to folder" dialog is opened. The dialog suggests a name for the folder link.
3. Edit the name as required. Select the path containing the graphic objects.
4. Click "OK" to confirm your input.

   The new folder link is added to the "Graphics" object group. The external graphics that are located in the target folder and in sub-folders are displayed in the toolbox.

##### Editing folder links

1. Select the folder link to edit.
2. Select the "Edit link..." command from the shortcut menu.   
   The "Create link to folder" dialog is opened.
3. Edit the name and path of the folder link as required.
4. Click "OK" to confirm your input.

##### Renaming the folder link

1. Select the folder link to rename.
2. Select "Rename" from the shortcut menu.
3. Assign a name to the new folder link.

##### Removing a folder link

1. Select the folder link you want to delete.
2. Select "Remove" in the shortcut menu.

##### Edit external graphics

1. Select the graphic you want to edit.
2. Select the "Edit graphic" command from the shortcut menu.

   This opens the screen editor associated with the graphic object file.

##### Editing graphics folders from WinCC

1. Select the graphic you want to edit.
2. Select the "Open parent folder" command from the shortcut menu.

   The Windows Explorer opens.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)

#### Storing an external image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To display graphics that have been created in an external graphics program in your screens, you will first have to store these graphics in the graphics browser of the WinCC project.

##### Requirement

- A screen has been created.
- A Graphic View is inserted in the screen.
- The Inspector window of the Graphic view is open.

To store an external graphic in the image browser:

- A graphic is available.

To store an OLE object in the browser:

- An OLE-compatible graphics program is installed on your configuration computer.

##### Save graphics file

1. Open the Windows Explorer.
2. Select the graphic that you want to store.
3. Drag-and-drop the graphic into the graphic browser.

##### Creating and saving a new graphic as an OLE object

1. Select the Graphic view on your screen.
2. In the Inspector window, select "Properties > Properties > General":
3. Open the graphic selection list.
4. Click ![Creating and saving a new graphic as an OLE object](images/14146668299_DV_resource.Stream@PNG-de-DE.png).
5. The "Insert object" dialog box opens.
6. From the "Insert object" dialog box, select "New" and an object type. The settings in "Settings > "OLE settings" determine which object types are shown.
7. Click "OK." The associated graphic program is opened.

   When you are finished creating graphics, end the graphic programming software with "File > Close" or "File > Close & return to WinCC."

   The graphic will be stored in the graphic programming software standard format and added to the graphic browser.

**Note**

In addition, the dialog "External application running..." will open. The dialog will not close until you exit the external application.

##### Inserting created graphics in WinCC

> **Note**
>
> A new graphic object created as OLE object may not be directly accepted in WinCC when you save it to an external graphics program.

1. Reopen the dialog for inserting a graphic.
2. From the "Insert object" dialog box, select "Create from file."
3. Click the "Browse" button.
4. Navigate to the created graphic and select it.

##### Saving an existing graphic object as an OLE object

1. In the Inspector window, select "Properties > Properties > General":
2. Open the graphic selection list.
3. Click ![Saving an existing graphic object as an OLE object](images/14146668299_DV_resource.Stream@PNG-de-DE.png).
4. The "Insert object" dialog box opens.
5. From the "Insert object" dialog box, select "Create from file."
6. Click the "Browse" button.
7. Use the dialog to help you navigate to the folder in which the graphic file is saved.

**Note**

In addition, the dialog "External application running..." will open. The dialog will not close until you exit the external application.

**Note**

To import graphics files, note the following size restrictions:

*.bmp, *.tif, *.emf, *.wmf ≤4 MB

*.jpg, *.jpeg, *.ico, *.gif "*≤1 MB

##### Result

The image file is now stored in your image browser. It is shown in a screen with a Graphic view , or is added as a list element in an image list.

You can double-click OLE objects in your library to open them for editing in the corresponding graphic editor. When you have finished editing graphics, end the graphic programming software with "File > Close" or "File > Close & return to WinCC." The changes are applied to WinCC.

---

**See also**

[Overview of objects (RT Professional)](#overview-of-objects-rt-professional)

#### Individually adjusting graphics in controls (RT Professional)

##### Introduction

In the standard configuration, neither the graphics for control buttons nor the size of those graphics can be changed. However, WinCC Professional provides the option to customize the appearance of controls to your own requirements. For example, you can enlarge the buttons of the controls for touch operation.

Controls are customized by creating and editing the graphics that are used by the software. To show a change made during runtime, select the new style from the configuration dialog of the control.

You have the following options for the customization of controls:

- Change the size and design of the buttons
- Adjust symbols in the table elements
- Changing the design of the scroll bar

Further information, a sample project and sample graphics are available on the Internet under [Individualizing WinCC Runtime Professional Controls.](http://support.automation.siemens.com/WW/view/en/76327375)

##### Basics

It is possible to individualize the following controls:

- Recipe view
- Alarm view
- f(x) trend view
- f(t) trend view
- Table view
- Value table

After the installation of TIA Portal, the "CCAxControlSkins" folder is created under "C:\Program Files(x86)\Common Files\Siemens\bin\" for the design of the controls.

To use modified designs, you need to create subfolders within the "CCAxControlSkins" folder. The number and the name of the subfolder are determined by the elements in the controls you want to customize.

The design of a control can then be selected as a "Style" property in the "Style" selection list on the "General" page of the control's configuration dialog.

To make the symbols created for table elements of a control visible, the "Content as symbol" option must be selected for the corresponding column in the "Appearance" area.

> **Note**
>
> When creating a new design, you do not need to create all the files. The default settings of the controls are used for all files that are not available.

##### Settings in the engineering system

Some adjustments in the engineering system are required to enable you to customize controls.

1. Select the control that you want to customize in the screen.

   The properties of the control are displayed in the Inspector window.
2. Under "Properties > Properties > Columns", select one of the entries in the "Title as" column for the display of the respective column title:

   - "Both" (text and symbol)
   - "None"
   - "Symbol"
   - "Text"

   ![Settings in the engineering system](images/97069207179_DV_resource.Stream@PNG-en-US.png)

   ![Settings in the engineering system](images/97069207179_DV_resource.Stream@PNG-en-US.png)

   Select the desired style you need to configure in Runtime.

   To perform the customization directly in the engineering system, use dynamics properties with tags or local C and VB scripts.

##### Creating a folder structure for your own designs

To enable new graphics to be used, a folder structure must be generated locally following specific rules.

1. Under "C:\Program Files(x86)\Common Files\Siemens\bin\CCAxControlsSkins", create a new folder from which graphics can be loaded to the control, e.g. "NewControlStyle".
2. In the new folder, generate a subfolder with the name of the control whose appearance you want to change, e.g. "AlarmControl" for the alarm view.
3. Create additional subfolders in the new folder:

   - "Toolbar" folder for the toolbar button graphics
   - "GridIcons" folder for graphics in the table cells

     ![Creating a folder structure for your own designs](images/76939335691_DV_resource.Stream@PNG-en-US.png)

     ![Creating a folder structure for your own designs](images/76939335691_DV_resource.Stream@PNG-en-US.png)
4. If you want to change the scroll bar display, create a "Scrollbar" folder for the scroll bar graphics under "C:\Program Files(x86)\Common Files\Siemens\bin\CCAxControlsSkins".

> **Note**
>
> Only those graphics that are stored in the folders are used for changes. The default settings of the controls are used for files that are not located in the folders.

> **Note**
>
> Please make sure that the file and folder names are spelled correctly so that the software can access the graphics.   
> Permissible image formats are PNG, GIF, JPG, and ICO.

> **Note**
>
> Please note, in particular when using multi-station systems or the "WebNavigator" option, that the "CCAxControlSkins" folder must be stored locally, i.e. on the WinCC Client.

##### Adjusting buttons on the toolbar

1. In the "Toolbar" folder of the relevant control, create an "IconsNormal.png" file.
2. Using image processing software, insert individual button graphics in the file one after another.
3. To use new graphics, edit the "IconsNormal.png" and "IconsDisabled.png" files.
4. To change the size of the toolbar graphics, enlarge or reduce the "IconsBackground.png" graphic.   
   This file defines the size of all toolbar buttons together.
5. To adjust the space around the hyphen, save the "Space.png" file in the "Toolbar" folder.
6. Generate the file "Left.png", which is used to define the width of the margin to the left of the button.
7. To show a change during runtime, select the newly generated style from the configuration dialog of the control.

![Adjusting buttons on the toolbar](images/96721936395_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The "Skin" parameter can be set only via the dynamics of the "Style" property with VB scripting, for example, HMIRuntime.Screens("Alarm").ScreenItems("Alarm view_1").SkinName = "MyOwnSkin".

##### Adjusting table elements

Proceed as follows to show different symbols depending on values in the table cells:

1. In the "..\[ControlName]\GridIcons" folder, generate the subfolders for each column in the table in which the graphics are displayed.

   Rename the subfolder to the name of the object property and save the state name in English, for example, "State" for the "Status" column.
2. In the "State" folder, you need to save the graphics with the respective state names in English, for example, "ComeQuit".

   For the state for which you have saved a graphic, the new symbol appears in the table cell when the state occurs.
3. To assign symbols for message numbers, assign a graphic for each numerical value.

   If you want to specify symbols for specific intervals, define the range in the file name with an underscore, e.g. "50_100.png" for the interval between 50 to 100. The limits are contained in the interval.
4. To display only symbols instead of text for an alarm text block/column, you must specify a graphic file for each occurring text.
5. Configure the display options for the content during runtime in the configuration dialog on the "Alarm blocks" tab.

**Note**

No symbols can be displayed for the "Date" or "Time" columns.

##### Adjusting the scroll bar

The scroll bar display consists of the various different graphics, and is created from the individual image files during runtime. Follow these steps to adjust the scroll bar:

1. Create the "Scrollbar" folder for the scroll bar graphics under "C:\Program Files(x86)\Common Files\Siemens\bin\CCAxControlsSkins".
2. Create the subfolders "horizontal" and "vertical" in the "Scrollbar" folder.
3. In this folder you place the individual graphics of the scroll bar, from which the scroll bar is assembled at runtime.
4. Select the style you have generated from the configuration dialog of the control during runtime.

   The scroll bars will be displayed in the new style.

##### Result

If you select the new style for the control during runtime, the updated graphics are displayed in the control.

![Result](images/76686574091_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Dynamization in the inspector window (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamization-in-the-inspector-window-panels-comfort-panels-rt-advanced-rt-professional)

### Working with object groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Grouping objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#grouping-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Ungrouping (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#ungrouping-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Adding objects to the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adding-objects-to-the-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Removing objects from the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#removing-objects-from-the-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Editing an object in a group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-an-object-in-a-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Groups are several objects that are grouped together with the "Group" function. You edit a group in the same way as any other object.

##### Overview

WinCC offers the following methods for editing multiple objects:

- [Multiple selection](#selecting-multiple-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Grouping objects](#grouping-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

##### Editing mode

To edit an individual object in a group, select the object in the "Layout > Layers" task card.

Alternatively select "Group > Edit group" in the object group's shortcut menu.

##### Hierarchical groups

You add further objects or groups to extend a group. The group is enlarged by the new objects and is structured hierarchically in main and sub-groups. Such hierarchical groups must be broken up in stages. You also break up the group in the same order in which you grouped the objects or groups. It takes exactly the same number of steps to break up these hierarchical groups as it did to create them.

##### Rectangle surrounding the object

Only one surrounding rectangle is now displayed for the whole group. The surrounding rectangles of all objects are displayed for a multiple selection on the other hand.

##### Layers

All objects of a group are located in the same layer.

##### Properties of a group

A group has its own properties, such as authorization. If you set a property at a group, all objects of the group inherit this setting. If the same property is configured differently at an object in the group, the value of the property at the object and not the value in the group applies in Runtime.

---

**See also**

[Ungrouping (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#ungrouping-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Adding objects to the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adding-objects-to-the-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Removing objects from the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#removing-objects-from-the-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Editing an object in a group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-an-object-in-a-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Grouping objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The "Group" command combines multiple objects to form a group.

You can change the size and position of the group. The following rules apply:

- The system automatically adapts the position coordinates of the grouped objects when you reposition the group. The relative position of the grouped objects to the group is not affected.
- The system automatically adapts the height and width of the grouped objects in proportion to a change of the group size.
- To change the size of the group proportionately, hold down the <Shift> key and drag the rectangle around the object until has the required size.

  > **Note**
  >
  > To create a hierarchical group, organize the individual groups like objects.

##### Requirement

- You have opened a screen which contains at least two objects.

##### Creating object groups

1. Select all the objects you want to organize in a group.
2. Select the command "Group > Group" from the shortcut menu.

The objects of the group are displayed with a rectangle around the objects.

##### Grouping objects within a group

1. Select the group you want to edit.
2. Select the command "Group > Edit group" from the shortcut menu.

   The group that you are editing is highlighted by a red frame.
3. Select the objects of a group that you want to combine into a subgroup.
4. Select the command "Group > Group" from the shortcut menu.

A subgroup with the objects is created.

##### Adding objects into an existing group

1. Select the group to which you want to add objects.
2. Press the <Shift> key and select the object you want to add to the group.
3. Select the "Group > Add to group" command from the shortcut menu.

The object is added to this group.

##### Alternative procedure

You can also edit groups in the "Layout" task card. Using drag-and-drop you can also easily edit nested groups in the "Layers" pane.

##### Result

The selected objects are combined in a group. The multiple selection rectangle becomes the rectangle surroundings the objects in the group. The handles are shown only for the group. The group in in the active layer.

---

**See also**

[Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Ungrouping (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#ungrouping-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Adding objects to the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adding-objects-to-the-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Removing objects from the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#removing-objects-from-the-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Editing an object in a group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-an-object-in-a-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Ungrouping (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Select the "Ungroup" command to split a group into the original object fractions.

##### Requirement

- You have opened a screen that contains a group.

##### Ungroup

1. Select the group.
2. Select the "Group > Ungroup" command from the shortcut menu.

##### Ungrouping a group within a group

1. Select the higher-level group.
2. Select the command "Group > Edit group" from the shortcut menu.

   The group that you are editing is highlighted by a red frame.
3. Select the lower-level group.
4. Select the "Group > Ungroup" command from the shortcut menu.

##### Result

The lower-level group is ungrouped. The objects are assigned to the next higher group.

##### Alternative procedure

You can also edit groups in the "Layout" task card. Using drag-and-drop you can also easily edit nested groups in the "Layers" pane.

---

**See also**

[Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Grouping objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#grouping-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Adding objects to the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#adding-objects-to-the-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Removing objects from the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#removing-objects-from-the-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Editing an object in a group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-an-object-in-a-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Adding objects to the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The "Add objects to group" command is used to add objects to a group, without ungrouping it first.

##### Requirements

A screen with one group and at least one other object is opened.

##### Procedure

1. Select the group.
2. Press the <Shift> key and select the object you want to add to the group.
3. Select the "Group > Add to group" command from the shortcut menu.

##### Result

The group consists of the original objects, and the newly-added objects. The added objects are arranged at the front of the group.

##### Alternative procedure

You can also edit groups in the "Layout" task card. Using drag&drop you can also easily edit hierarchical groups in the "Layers" palette.

---

**See also**

[Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Removing objects from the group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You use the "Remove objects from group" command to remove individual objects from a group, without ungrouping it first.

You do not have to remove the object from the group to edit an object in a group. You can edit the objects of a group individually.

##### Requirement

- You have opened a screen that contains a group.

##### Removing objects from a group

To remove an object from a group:

1. Select the group.
2. Select the command "Group > Edit group" from the shortcut menu.

   The group you want to edit is highlighted by a red frame.
3. Select all objects in the group that you want to remove from the group.
4. Select the "Group > Remove from group" command from the shortcut menu.

The objects are removed from the group.

> **Note**
>
> If there are only two objects in the group, the menu command "Remove from group" is not available.

##### Deleting objects from a group

To remove an object from the group, and from the screen:

1. Select the group.
2. Select the command "Group > Edit group" from the shortcut menu.

   The group you want to edit is highlighted by a red frame.
3. Select the objects in the group that you want to delete.
4. Select "Delete" from the shortcut menu.

**Note**

If there are only two objects in the group, the menu command "Delete" is not available.

##### Alternative procedure

You can also edit groups in the "Layout" task card. Using drag-and-drop you can also easily edit nested groups in the "Layers" pane.

---

**See also**

[Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Editing an object in a group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can edit the objects of a group individually.

##### Requirement

You have opened a screen that contains a group.

##### Editing grouped objects

1. Select the group.

   ![Editing grouped objects](images/9130318731_DV_resource.Stream@PNG-de-DE.png)

   ![Editing grouped objects](images/9130318731_DV_resource.Stream@PNG-de-DE.png)

   The properties of the group are displayed in the Inspector window.
2. Change the position and size of the grouped objects in "Properties > Properties >Layout."
3. Change the name of the group in "Properties > Properties > Miscellaneous."

##### Modifying the properties of an object within a group

1. Select the group.
2. Select the object whose properties you want to change in the Inspector window.

   ![Modifying the properties of an object within a group](images/74915579659_DV_resource.Stream@PNG-en-US.png)

   ![Modifying the properties of an object within a group](images/74915579659_DV_resource.Stream@PNG-en-US.png)

   The properties of the object are displayed.
3. Change the object properties.

> **Note**
>
> The dynamization of properties for all objects of the group which have these properties is not possible in a group. You can only dynamize the properties of the objects associated with a group for each object itself.

##### Result

Although you have edited the object, it is still an element of the group. These changes do not affect the other objects of the group.

---

**See also**

[Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Configuring the keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overview-of-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced)
- [Overview of keyboard access (RT Professional)](#overview-of-keyboard-access-rt-professional)
- [Defining cursor mode (RT Professional)](#defining-cursor-mode-rt-professional)
- [Defining the operator authorization and operator control enable for an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-operator-authorization-and-operator-control-enable-for-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Defining object types for tab cursor mode (RT Professional)](#defining-object-types-for-tab-cursor-mode-rt-professional)
- [Setting the tab sequence order (Basic Panels, Panels, Comfort Panels, RT Advanced)](#setting-the-tab-sequence-order-basic-panels-panels-comfort-panels-rt-advanced)
- [Setting the tab sequence order (RT Professional)](#setting-the-tab-sequence-order-rt-professional)

#### Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

For keyboard units without a mouse, the operator activates control objects using the <Tab> key. You can set up keyboard input to make the process easier to run, and to make sure that the operator enters all the necessary values. If you are using the keyboard, use the <Tab> key to activate the objects in a certain order, and to enter the necessary values.

For HMI devices without key, you can simulate the <Tab> key by configuring the "SimulateSystemKey" system function to a function key.

##### Operator authorizations and operator control enables

If you configure an object for operator input with the <Tab> key, the object must have both an operator authorization, and an operator control enable.

##### Editing the tab sequence

The tab sequence is determined automatically when the control objects are created. The numbers of the tab sequence are assigned in the sequence in which the libraries are created.

It makes sense to change the tab sequence in the following cases:

- The operator changes directly to a specific control object.
- The screen requires a specific sequence

Change to the tab sequence mode to change the tab sequence. In this mode, the tab sequence number is displayed at the top left of the control objects. The tab sequence numbers of hidden objects are also shown. The distribution of these numbers is edited using the mouse.

> **Note**
>
> Other functions are not available in the tab sequence mode.

---

**See also**

[Overview of keyboard access (RT Professional)](#overview-of-keyboard-access-rt-professional)
  
[Defining cursor mode (RT Professional)](#defining-cursor-mode-rt-professional)
  
[Defining the operator authorization and operator control enable for an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#defining-the-operator-authorization-and-operator-control-enable-for-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Defining object types for tab cursor mode (RT Professional)](#defining-object-types-for-tab-cursor-mode-rt-professional)
  
[Setting the tab sequence order (Basic Panels, Panels, Comfort Panels, RT Advanced)](#setting-the-tab-sequence-order-basic-panels-panels-comfort-panels-rt-advanced)
  
[Setting the tab sequence order (RT Professional)](#setting-the-tab-sequence-order-rt-professional)
  
[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Overview of keyboard access (RT Professional)

##### Introduction

To influence the process, the operator edits operable objects such as I/O fields or buttons in Runtime. You set up keyboard input to make the process easier to run, and to make sure that the operator enters all necessary values. When the operator makes entries, he uses the <Tab> key to activate the objects in a specified order and to enter the necessary values.

##### Keyboard access

There are two methods of mouseless operator input:

- Alpha cursor: The operator uses the <Tab> key in Runtime to activate objects of the "I/O field", and "text list" type only.
- Tab cursor: Depending on the settings, the operator uses the <Tab> key in Runtime to activate all objects that permit an input.

You define the cursor mode when Runtime starts. You set the cursor mode in the Inspector window of the screen.

##### Combining the Alpha cursor and Tab cursor modes

When you have defined a hotkey, the operator can toggle the cursor mode between the two modes during runtime if necessary. In this case you specify the tab sequence for both cursor types.

##### Operation in Runtime

You use the tab sequence to define in which order the operator can activate objects. The default setting is operation using the <Tab> key. If required, define operation using a hotkey or the mouse.

---

**See also**

[Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overview-of-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Defining cursor mode (RT Professional)

##### Introduction

You define the cursor mode when Runtime starts. The operator can change the cursor mode in Runtime as required. You set the cursor mode in the object properties of the screen.

##### Requirement

You have opened a screen which contains multiple objects.

##### Procedure

1. Click on a empty surface on the screen.
2. In the Inspector window, click "Properties > Properties > Miscellaneous".
3. Select the desired cursor mode under "Tab sequence".

##### Result

The required cursor mode is active when Runtime starts.

---

**See also**

[Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overview-of-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Defining the operator authorization and operator control enable for an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

If you configure an object for operator input with the <Tab> key, the object must have both an operator authorization, and an operator control enable.

##### Requirement

You have opened a screen which contains at least one object.

##### Procedure

1. Select the object.
2. Select "Properties > Properties > Security" in the Inspector window.
3. Select the operator authorization under "Authorization."
4. Activate the authorization to operate.

##### Result

The operator can use the <Tab> key in Runtime to select the object.

---

**See also**

[Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overview-of-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Defining object types for tab cursor mode (RT Professional)

##### Introduction

In the Inspector window, you can define the object types that the operator activates using the <Tab> key in "Tab cursor" mode.

![Introduction](images/87580173707_DV_resource.Stream@PNG-en-US.png)

##### Requirement

- You have opened a screen which contains at least one object.
- The objects have been enabled for use in Runtime, and have operator authorization.
- "Tab cursor" mode is specified.

##### Procedure

1. Click on a empty surface on the screen.
2. Select the object types to be used in Runtime using the <Tab> key in the inspector window under "Properties > Properties > Miscellaneous > Tab sequence object types".

   ![Procedure](images/61217822859_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61217822859_DV_resource.Stream@PNG-en-US.png)

##### Result

The user can activate all the defined objects in Runtime using the <Tab> key in "Tab cursor" mode.

---

**See also**

[Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overview-of-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Setting the tab sequence order (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

All operable objects can be reached in runtime with the <Tab> key. You use the "Tab sequence" command to define the order in which the operator can activate objects in runtime.

> **Note**
>
> You cannot reach objects with the "Output" or "Two states" mode in runtime with the <Tab> key.

You can operate the screen in runtime:

- Using the <Tab> key
- Using the mouse
- Using a configured hotkey

##### Requirement

- The active screen contains operable objects.
- No object is selected.
- The objects have been enabled for use in runtime, and have operator authorization.

##### Procedure

1. Select "Edit tab sequence" in the "Edit" menu.

   Tab sequence mode is activated. The tab sequence number is displayed for all objects that can be used. The tab sequence number is also displayed for hidden objects.
2. Use edit the tab sequence mode, click the accessible objects in the order in which you want them to be activated using <Tab> in runtime.

   The following figure shows how the tab sequence is defined in the screen. In runtime, the <Tab> key first activates the alarm view (number 1), then the I/O field (number 2), and then the button (number 3):

   ![Procedure](images/14553543819_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/14553543819_DV_resource.Stream@PNG-de-DE.png)
3. To exclude a screen object from the tab sequence, press the key combination <Shift+Ctrl> and click on the desired object.

   The tab sequence number is no longer displayed in the screen object. The screen object is now excluded from the tab sequence. The remaining tab sequence numbers are automatically decreased by 1.
4. To reenter an excluded screen object in the tab sequence, repeat step 3.

   The screen object entered as the first object in the tab sequence.

##### Result

The operator selects the objects in the specified order in Runtime with the <Tab> key.

> **Note**
>
> **Changes after upgrades to a new software version**
>
> If you have configured a tab sequence in screens with faceplates in an older WinCC version, you should check the tab sequence of these screens after an upgrade to a newer WinCC version. The tab sequence may have been changed in both the screen and the faceplate.

---

**See also**

[Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overview-of-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Setting the tab sequence order (RT Professional)

##### Introduction

Every object can be accessed in Runtime in the mode "Tab cursor". You use the "Tab sequence" command to define the order in which the operator can activate objects in Runtime. You can operate the process screen in runtime:

- Using the <Tab> key
- Using the mouse
- Using a configured hotkey

##### Requirements

- You have opened a screen which contains at least one object.
- The objects have been enabled for use in Runtime, and have operator authorization.
- "Tab cursor" or "Alpha cursor" mode is activated.

##### Procedure

1. Select "Edit > Tab sequence > Edit tab cursor" or "Edit alpha cursor".

   Tab sequence mode is activated. The tab sequence number is displayed for all objects that can be used. The tab sequence number is also displayed for hidden objects.
2. Use edit the tab sequence mode, click the accessible objects in the order in which you want them to be activated using <Tab> in Runtime.

   The following figure shows how the tab sequence is defined in the screen. In Runtime, the <Tab> key first activates the I/O field (number 2), and then the button (number 3).

   ![Procedure](images/14553543819_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/14553543819_DV_resource.Stream@PNG-de-DE.png)

##### Result

The operator selects the objects in the specified order in Runtime with the <Tab> key.

> **Note**
>
> **Changes after upgrading to a new software version**
>
> If you have configured a tab sequence in screens with faceplates in an older WinCC version, check the tab sequence of these screens after upgrading to a newer WinCC version. The tab sequence may have been changed in both the screen and the faceplate.

---

**See also**

[Overview of keyboard access (Basic Panels, Panels, Comfort Panels, RT Advanced)](#overview-of-keyboard-access-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Examples (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Inserting a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Task

In this example, you insert a rectangle in a screen. You can configure the following properties:

- Name = "MyRectangle"
- Position = (20, 20)
- Size = (100,100)
- Color = red
- Black frame 2 pixels wide

##### Principle

The rectangle is a closed object which can be filled with a color or pattern. The height and width of a rectangle can be adjusted to allow its horizontal and vertical alignment.

![Principle](images/14149131403_DV_resource.Stream@PNG-de-DE.png)

##### Overview

Carry out the following steps in order to create a rectangle:

- Inserting a rectangle
- Configuring a rectangle

---

**See also**

[Basics on groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)
  
[Example: Inserting a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Inserting a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Task

In this example, you insert and rename a rectangle. Do not use the special characters ?, ", /, \, *, <, > for the name.

##### Requirement

- A screen is open.
- The Inspector window is open.
- The "Tools" task card is open.

##### Procedure

1. Click the "Basic objects" palette in the "Tools" task card.
2. Drag the "Rectangle" object into the screen.
3. In the Inspector window, select "Properties > Properties > Miscellaneous".
4. Type in the new name "MyRectangle".

##### Result

The rectangle is now inserted and named "MyRectangle". The rectangle has the default properties of the "rectangle" object.

---

**See also**

[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Task

In this example you configure a rectangle:

- Color = red
- Black frame 2 pixels wide
- Position = (20, 20)
- Size = (100,100)

##### Changing the color of the rectangle

To change the color of the rectangle:

1. Select the rectangle.
2. Define the background color in "Properties > Properties > Appearance > Background > Color" in the Inspector window.
3. Select "Solid" as the fill pattern.
4. Define the color for the border in "Properties > Properties > Appearance > Border > Color" in the Inspector window.
5. Enter the value "2" for "width".
6. Select "Solid" as the "Style".

##### Interim result

The rectangle is red and has a black frame with a width of two pixels.

##### Repositioning and resizing the rectangle

To change the position and size of the rectangle:

1. Select the rectangle.
2. In the Inspector window, select "Properties > Properties > Layout".

   ![Repositioning and resizing the rectangle](images/87584240651_DV_resource.Stream@PNG-en-US.png)

   ![Repositioning and resizing the rectangle](images/87584240651_DV_resource.Stream@PNG-en-US.png)
3. Set "20" for the both the X and Y coordinates under "Position & Size".
4. Set "100" for the height and for the width.

##### Result

The rectangle is positioned at the coordinates (20, 20), and has a width and height of 100 pixels.

---

**See also**

[Example: Inserting and configuring a rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-inserting-and-configuring-a-rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Working with text lists and graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Working with text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with C text lists (RT Professional)](#working-with-c-text-lists-rt-professional)

### Working with text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating a text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Assigning texts and values to an area text list (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-texts-and-values-to-an-area-text-list-basic-panels-panels-comfort-panels-rt-advanced)
- [Assigning texts and values to an area text list (RT Professional)](#assigning-texts-and-values-to-an-area-text-list-rt-professional)
- [Assigning texts and values to a bit text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-texts-and-values-to-a-bit-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Assigning texts and values to a bit number text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-texts-and-values-to-a-bit-number-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Notes for bit number text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#notes-for-bit-number-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring objects with a text list (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-objects-with-a-text-list-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring objects with a text list (RT Professional)](#configuring-objects-with-a-text-list-rt-professional)

#### Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Texts are assigned to the values of a tag in a text list. Assign the text list to a symbolic I/O field for example in the configuration. This supplies the text to be displayed to the object. The text lists are created in the ""Text List" editor. You configure the interface between the text list and a tag at the object that uses the text list.

The selection of objects that can have a text list assigned depends on the Runtime.

##### Application

The text list is used, for example, to display a drop-down list in a symbolic I/O field.

If the symbolic I/O field is a display field, the associated texts will differ according to the value of the configured tags. If the symbolic I/O field is an input field, the configured tag assumes the associated value when the operator selects the corresponding text in Runtime.

> **Note**
>
> **Display of tag values without text**
>
> The display of tag values to which no text has been assigned depends on the Runtime:
>
> - The display and operating element remains empty.
> - Three asterisks *** are displayed.

##### Ranges for the text list

Three types are available for the text lists:

- Value/Range

  This setting assigns text entries from the text list to integer values or value ranges of a tag. You can select the number of text entries as needed. The maximum number of entries depends on the HMI device you are using.

  You specify a default value which is shown if the value of the tag lies outside the defined range.
- Bit (0, 1)

  This setting assigns text entries from the text list to two states of a binary tag. You can create a text entry for each state of the binary tag.
- Bit number (0 - 31)

  This setting assigns a text entry from the text list to each bit of a tag. The maximum number of text entries is 32. This form of text list can be used, for example, in a sequence control when processing a sequence in which only one bit of the used tag may be set. You influence the behavior of the bit number (0 - 31) with the set bit of the least significance and a default value.

##### Multilingual texts

You can configure multiple languages for the texts in a text list. The texts will then be displayed in the set language in Runtime. To this purpose you set the languages in the Project window under "Language support > Project languages."

##### Configuration steps

The following steps are necessary to display texts in a symbolic I/O field for example:

1. Creating the text list
2. Assignment of the texts to values or value ranges of a text list
3. Assignment of a text list in the display object, for example, to the symbolic I/O field

---

**See also**

[Creating a text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Assigning texts and values to an area text list (RT Professional)](#assigning-texts-and-values-to-an-area-text-list-rt-professional)
  
[Assigning texts and values to a bit text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-texts-and-values-to-a-bit-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Assigning texts and values to a bit number text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-texts-and-values-to-a-bit-number-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Notes for bit number text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#notes-for-bit-number-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring objects with a text list (RT Professional)](#configuring-objects-with-a-text-list-rt-professional)
  
[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Output of texts from a text list in an alarm (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#output-of-texts-from-a-text-list-in-an-alarm-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring a text list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-text-list-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating a text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The text list allows you to assign specific texts to values and to output these in Runtime, for example in a symbolic I/O field. The type of symbolic I/O field can be specified, for example as a pure input field.

The following types of list are available:

- Value/Range
- Bit
- Bit Number

##### Procedure

1. Double-click "Text and graphics lists" in the project window.
2. Open the "Text lists" tab.

   ![Procedure](images/87585710347_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/87585710347_DV_resource.Stream@PNG-en-US.png)
3. Click "Add" in the "Text lists" table.

   The Inspector window of the text list is open.
4. Assign a name to the text list that indicates its function.
5. Select the text list type under "Selection":

   - Value/Range: Text from the text list is displayed when the tag has a value that lies within the specified range.
   - Bit (0,1): A text from the text list is displayed when the tag has the value 0. A different text from the text list is displayed when the tag has the value 1.
   - Bit number (0-31): Text from the text list is displayed when the tag has the value of the assigned bit number.
6. Enter a comment for the text list.

**Note**

You should not use semicolons in the texts in a text list in WinCC Runtime Professional. The semicolon is a control character and is automatically deleted from a text.

##### Result

A text list is created.

---

**See also**

[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a text list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-text-list-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning texts and values to an area text list (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

For each area text list you specify which texts are displayed at which value range.

##### Requirement

- The "Text and graphics list" editor is open.
- The "Text lists" tab is open.
- An area text list has been created and selected.

##### Procedure

1. Click "Add" in the "Text list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/70649488523_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70649488523_DV_resource.Stream@PNG-en-US.png)
2. Select the setting "Range" in "Properties > Properties > General > Value" in the Inspector window.

   ![Procedure](images/76061051275_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/76061051275_DV_resource.Stream@PNG-en-US.png)

   - Enter the value "1" for "Min" for example.
   - Enter the value "20" for "Max" for example.
   - For "Text", enter the text that is displayed in Runtime if the tag is within the specified value range.
3. Click "Add" in the "Text list entries" table. A second list entry is created.
4. Select the setting "Range" in "Properties > Properties > General > Value" in the Inspector window.

   - Enter the value "21" for "Min" for example.
   - Enter the value "40" for "Max" for example.
   - For "Text", enter the text that is displayed in Runtime when the tag is within the specified value range.
5. If required, activate the "default entry".

   The entered text is always displayed when the tag has an undefined value. Only one default entry is possible per list.

**Note**

Use a maximum of 320 characters for the text.

##### Result

An area text list is created. Texts have been assigned to the possible value ranges.

---

**See also**

[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning texts and values to an area text list (RT Professional)

##### Introduction

For each area text list you specify which texts are displayed at which value range.

##### Requirement

- The "Text and graphics list" editor is open.
- The "Text lists" tab is open.
- An area text list has been created and selected.

##### Procedure

1. Click "Add" in the "Text list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/70649488523_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70649488523_DV_resource.Stream@PNG-en-US.png)
2. Select one of the following settings in the Inspector window under "Properties > Properties > General > Value".

   ![Procedure](images/9150167563_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/9150167563_DV_resource.Stream@PNG-en-US.png)

   - "Range": Minimum to maximum tag value, for example 1 ≦ Value ≦ 21
   - "To": Maximum tag value, e.g. value ≦ 13
   - "Individual value": Exactly one tag value, for example Value = 21
   - "From": Minimum tag value, e.g. value ≧ 2
3. Enter the text that is displayed in Runtime when the tag has the specified value or lies within the specified range of values under "Text."
4. If required, activate the "default entry".

   The entered text is always displayed when the tag has an undefined value. Only one default entry is possible per list.
5. Create further corresponding list entries for additional value ranges of the same text list.

**Note**

Use a maximum of 255 characters and no semicolons for the text.

##### Result

An area text list is created. Texts that appear in Runtime are assigned to the possible values.

---

**See also**

[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning texts and values to a bit text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

For each text list, you specify which text is displayed at which bit value.

##### Requirement

- The "Text and graphics list" editor is open.
- The "Text lists" tab is open.
- A bit text list has been created and selected.

##### Procedure

1. Click "Add" in the "Text list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/70651185291_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70651185291_DV_resource.Stream@PNG-en-US.png)
2. Select the setting "Single value" in "Properties > Properties > General > Value" in the Inspector window.

   - Enter "0" for "Value."
   - Enter the text which is displayed in Runtime under "Text" if the bit tag is set to "0".
3. Click "Add" in the "Text list entries" table. A second list entry is created.
4. Select the setting "Single value" in "Properties > Properties > General > Value" in the Inspector window.

   - Enter "1" under "Value."
   - Enter the text which is to be displayed in Runtime under "Text" if the bit tag is set to "1".

> **Note**
>
> Use a maximum of 320 characters for the text.
>
> Use a maximum of 255 characters and no semicolons for the text in WinCC Runtime Professional.

##### Result

A bit text list is created. Texts that appear in Runtime are assigned to the possible values "0" and "1".

---

**See also**

[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning texts and values to a bit number text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

For each bit number text list you specify which texts are displayed at which bit number.

##### Requirement

- The "Text and graphics list" editor is open.
- The "Text lists" tab is open.
- A bit number text list has been created and selected.

##### Procedure

1. Click "Add" in the "Text list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/70649488523_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70649488523_DV_resource.Stream@PNG-en-US.png)
2. Select the setting "Single value" in "Properties > Properties > General > Value" in the Inspector window.

   - Enter "10", for example, for "Value".
   - Under "Text", enter the text that is displayed in Runtime when the tag has the value "10".
3. If required, activate the "default entry".

   The entered text is always displayed when the tag has an undefined value. Only one default entry is possible per list.
4. Create further list entries for additional bit numbers of the same text list.

> **Note**
>
> Use a maximum of 320 characters for the text.
>
> Use a maximum of 255 characters and no semicolons for the text in WinCC Runtime Professional.

> **Note**
>
> ****Bit selection for text lists****
>
> The output of the text list depends on the "Bit selection for text and graphics lists" option in the Runtime settings. Use this option to specify that the bit selection for text lists should be used on your HMI device. When you enable the option, the text displayed is the one configured for the set bit with the least significance. When you disable this option, only the text that has been configured for the set bit is displayed .

##### Result

A bit number text list is created. Texts that appear in Runtime are assigned to the specified bit numbers.

---

**See also**

[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Notes for bit number text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The bit number (0 - 31) range assigns a text entry from the list to each bit of a tag. If the option "Bit selection for text and graphic lists" is disabled in the Runtime settings and no default value is set, the following standard behavior applies:

- If only 1 bit is configured of all set bits, the stored text is displayed for the configured bit.  
  In the following example, only the set bit with significance "4" is configured. Text 2 is displayed.

  |  |  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Significance | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
  | Set bits | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
  | Configured | - | Text 3 | - | Text 2 | Text 1 | - | - | - |
- If no bit is set or when several configured bits are set, no text is displayed.

##### Default value

Define a default value to prevent an empty display. A configured default value is displayed in the following cases:

- The option "Bit selection for text and graphic lists" is disabled. No bit or several configured bits are set in the tag.

- The option "Bit selection for text and graphic lists" is enabled and no bit is set or a text is not configured for the set bit with the least significance.

##### Displaying the default value

1. Enable the text for the default entry in the "Default" column of the "Text list entries" table.   
   The value "Default entry" appears in the "Value" column of the text entry.
2. You can also select the "Default" option under "Properties > General" in the inspector window.

##### Set bit with the least significance

If no text is configured for the set bit with the least significance and if no

default value is set, nothing is displayed. If a default value is configured, the default value is displayed.

If no text is configured for the set bit with the least significance and if no default value is set, nothing is displayed. If a default value is configured, the default value is displayed.

To only display the text for the set bit with the least significance, enable the "Bit selection for text and graphic lists" option in the "Runtime settings" editor.

This setting is deselected by default to maintain downward compatibility. The setting is valid for all text lists of the HMI device.

##### Multiline text list entries

Use the <SHIFT>+<RETURN> shortcut to enter a line break in the text entry. Line breaks are represented by the "¶" paragraph mark.

Multiline text list entries are only output in symbolic output fields as well as on buttons with multiple lines. In all other cases, multiline texts are displayed with the paragraph mark.

#### Configuring objects with a text list (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

The output value and value application for text lists are specified in the display and operating object that displays the texts of the text list in Runtime. The properties of these objects are configured as required.

##### Requirement

- A text list is created.
- You have created a tag.
- The "Screens" editor is open.
- A screen with a symbolic I/O field is open. The object is edited.

##### Procedure

1. Select the text list which you want to have displayed in Runtime in "Properties > Properties > General > Text list" in the Inspection window.
2. Select the setting "Output" as the "Mode".
3. Select the tag the value of which determines the display in the symbolic I/O field as "Tag".

   ![Procedure](images/74905709451_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/74905709451_DV_resource.Stream@PNG-en-US.png)

**Note**

**Runtime dependency**

Different field types are available for a symbolic I/O field depending on the Runtime.

##### Result

The defined texts of the text list are displayed in the symbolic I/O field in Runtime when the tag has the specified value.

---

**See also**

[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring objects with a text list (RT Professional)

##### Introduction

The output value and value application for text lists are specified in the display and operating object that displays the texts of the text list in Runtime. The properties of these objects are configured as required.

##### Requirement

- A text list is created.
- You have created a tag.
- The "Screens" editor is open.
- A screen with a symbolic I/O field is open. The object is edited.

##### Procedure

1. Select the text list which you want to have displayed in Runtime in "Properties > Properties > General > Text list" in the Inspection window.
2. Select the setting "Output" as the "Mode".
3. Select the tag the value of which determines the display in the symbolic I/O field as "Tag".

   ![Procedure](images/72330201739_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72330201739_DV_resource.Stream@PNG-en-US.png)

**Note**

**Runtime dependency**

Different field types are available for a symbolic I/O field depending on the Runtime.

##### Result

The defined texts of the text list are displayed in the symbolic I/O field in Runtime when the tag has the specified value.

---

**See also**

[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Working with graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-of-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating a graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-graphics-list-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating a graphics list (RT Professional)](#creating-a-graphics-list-rt-professional)
- [Assigning a graphic and values to an area graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-a-graphic-and-values-to-an-area-graphics-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Assigning graphics and values to an area graphics list (RT Professional)](#assigning-graphics-and-values-to-an-area-graphics-list-rt-professional)
- [Assigning graphics and values to a bit graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-graphics-and-values-to-a-bit-graphics-list-basic-panels-panels-comfort-panels-rt-advanced)
- [Assigning graphics and values to a bit number graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-graphics-and-values-to-a-bit-number-graphics-list-basic-panels-panels-comfort-panels-rt-advanced)
- [Notes for bit number graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#notes-for-bit-number-graphics-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring objects with a graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-objects-with-a-graphics-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The possible values of a tag are assigned to specific graphics in a graphics list. During configuration, you can create a graphics list for a button or a graphic I/O field. This supplies the graphics to be displayed to the object.

The graphics lists are created with the "Text and graphics list" editor. You configure the interface between the graphics list and a tag at the object that uses the graphics list. The availability of the graphics list is determined by the HMI device used.

##### Application

You can configure the graphics list for the following situations:

- Drop-down list with a graphic I/O field
- State-specific graphic for a button

The graphics in a graphics list can be configured as multilingual. The graphics will then be displayed in the set language in Runtime.

##### Graphic sources

Graphics can be added to the graphics list from the following sources:

- By selecting from a graphic browser
- Selection of an existing file   
  You can use the following file types:   
  *.bmp, *.ico, *.emf, *.wmf, *.gif, *.tiff, *.png, *.svg, *.jpeg and *.jpg.
- By creating a new file

##### Function

If the graphic I/O field is a display field, the associated graphics will differ according to the value of the configured tags. If the graphic I/O field is an input field, the configured tag assumes the associated value when the operator selects a graphic in Runtime.

##### Ranges for the graphics list

Three types are available for the graphics lists:

- Value/Range

  This setting assigns graphic entries from the graphics list to integer values or value ranges of a tag. You can select the number of graphic entries as needed. The maximum number of entries depends on the HMI device you are using.

  You specify a default value which is shown if the value of the tag lies outside the defined range.
- Bit (0, 1)

  This setting assigns graphic entries from the graphics list to two states of a binary tag. You can create a graphic entry for each state of the binary tag.
- Bit number (0 - 31)

  This setting assigns a graphic entry from the graphics list to each bit of a tag. The maximum number of graphic entries is 32. This form of graphics list can be used, for example, in a sequential control chart when processing a sequencer in which only one bit of the used tag may be set. You influence the behavior of the bit number (0 - 31) with the set bit of the least significance and a default value.

##### Configuration steps

The following tasks are required to display graphics, for example, in a graphic I/O field:

1. Creating the graphics list
2. Assignment of the graphics to values or value ranges of a graphics list
3. Assignment of a graphics list in the display object, for example, the graphic I/O field

---

**See also**

[Creating a graphics list (RT Professional)](#creating-a-graphics-list-rt-professional)
  
[Assigning a graphic and values to an area graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-a-graphic-and-values-to-an-area-graphics-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Assigning graphics and values to a bit graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-graphics-and-values-to-a-bit-graphics-list-basic-panels-panels-comfort-panels-rt-advanced)
  
[Assigning graphics and values to a bit number graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-graphics-and-values-to-a-bit-number-graphics-list-basic-panels-panels-comfort-panels-rt-advanced)
  
[Notes for bit number graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#notes-for-bit-number-graphics-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring objects with a graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-objects-with-a-graphics-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a graphics list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-graphics-list-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)

#### Creating a graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

The graphics list allows you to assign specific graphics to variable values and to output these in a graphic IO field in Runtime. You can specify the type of graphic I/O field, for example as a pure output field.

##### Procedure

1. Double-click "Text and graphics lists" in the project window.
2. Open the "Graphics lists" tab.

   ![Procedure](images/111671495435_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111671495435_DV_resource.Stream@PNG-en-US.png)
3. Click "Add" in the "Graphics lists" table. The Inspector window of the graphics list will open up.

   ![Procedure](images/60712248587_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/60712248587_DV_resource.Stream@PNG-en-US.png)
4. Assign a name to the graphics list that indicates its function.
5. Select the graphics list type "Bit number (0 - 31)" for example under "Select".
6. Enter a comment for the graphics list.

##### Result

A graphics list of the type "Range (0 - 31)" is created.

---

**See also**

[Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-of-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating a graphics list (RT Professional)

##### Introduction

The graphics list allows you to assign specific graphics to variable values and to output these in a graphic IO field in Runtime. You can specify the type of graphic IO field, for example as a pure output field.

##### Procedure

1. Double-click "Text and graphics lists" in the project navigation.
2. Open the "Graphics lists" tab.
3. Click "Add" in the "Graphics lists" table.

   The Inspector window of the graphics list will open up.

   ![Procedure](images/87623073803_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/87623073803_DV_resource.Stream@PNG-en-US.png)
4. Assign a name to the graphics list that indicates its function.
5. Select the "Value/Range" graphics list type under "Selection."
6. Enter a comment for the graphics list.

##### Result

An area graphics list is created.

---

**See also**

[Creating a graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-graphics-list-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring a graphics list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-graphics-list-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning a graphic and values to an area graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

For each area graphics list you specify which graphics are displayed at which value range.

##### Requirement

- The "Text and graphics list" editor is open.
- The "Graphics list" tab is open.
- An area graphics list has been created and selected.

##### Procedure

1. Click "Add" in the "Graphics list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/55963899531_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/55963899531_DV_resource.Stream@PNG-en-US.png)
2. Select the settings "Range" in "Properties > Properties > General > Value" in the Inspector window:

   - Enter the value "1" for "Min" for example.
   - Enter the value "20" for "Max" for example.
   - Select a graphic that is displayed in Runtime when the tag is within the specified value range.

     ![Procedure](images/55964115979_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/55964115979_DV_resource.Stream@PNG-en-US.png)
3. Click "Add" in the "Graphics list entries" table. A further list entry is created.
4. Select the settings "Single value" in "Properties > Properties > General > Value" in the Inspector window:

   - Enter the value "21" for example.
   - Select a graphic which is displayed in Runtime if the bit "21" is set in the tag.

     ![Procedure](images/55964111499_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/55964111499_DV_resource.Stream@PNG-en-US.png)
5. If required, activate the "default entry".

   The graphic is always displayed when the tag has an undefined value. Only one default entry is possible per list.

**Note**

As an alternative to the drop-down menu, you can insert graphics from libraries or from your file system:

1. Select a graphic in the library or in your file system.
2. Drag-and-drop the graphic into the "Graphics list entries > Graphic" table.

##### Result

An area graphics list is created. Graphics that appear in Runtime are assigned to the possible values.

---

**See also**

[Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-of-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning graphics and values to an area graphics list (RT Professional)

##### Introduction

For each area graphics list you specify which graphics are displayed at which value range.

##### Requirement

- The "Text and graphics list" editor is open.
- The "Graphics list" tab is open.
- An area graphics list has been created and selected.

##### Procedure

1. Click "Add" in the "Graphics list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/72357797003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72357797003_DV_resource.Stream@PNG-en-US.png)
2. Select the settings "Single value" in "Properties > Properties > General > Value" in the Inspector window:

   - Enter the value "0" for example.
   - Select a graphic which is displayed in Runtime if the bit "0" is set.

     ![Procedure](images/55964111499_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/55964111499_DV_resource.Stream@PNG-en-US.png)
3. If required, activate the "default entry".

   The graphic is always displayed when the tag has an undefined value. Only one default entry is possible per list.
4. Activate "Properties > Properties > General > Use transparent color" in the inspector window and select a color.
5. Activate "Properties > Properties > Flash > Use flash" in the inspector window.
6. Select "Flash frequency > Slow" for example.
7. Create further list entries for additional bit numbers of the same graphics list.

**Note**

As an alternative to the drop-down menu, you can insert graphics from libraries or from your file system:

1. Select a graphic in the library or in your file system.
2. Drag-and-drop the graphic into the "Graphics list entries > Graphic" table.

##### Result

An area graphics list is created. Graphics that appear in Runtime are assigned to the specified bit numbers. The graphic flashes when the tag has a defined value.

#### Assigning graphics and values to a bit graphics list  (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

For each graphics list you specify which graphic is displayed at which bit value.

##### Requirement

- The "Text and graphics list" editor is open.
- The "Graphics list" tab is opened.
- A bit graphics list has been created and selected.

##### Procedure

1. Click "Add" in the "Graphics list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/72357797003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72357797003_DV_resource.Stream@PNG-en-US.png)
2. Select the settings "Single value" in the inspector window "Properties > Properties > General > Value":

   - Enter "0" as the value.
   - Select a graphic which is displayed in Runtime if the bit "0" is set in the tag.
3. Click "Add" in the "Graphics list entries" table. A new list entry is created.
4. Select "Properties > Properties > General > Value > Single value": in the Inspector window.

   - Enter "1" as the value.
   - Select a graphic which is displayed in Runtime if the bit "1" is set in the tag.

**Note**

As an alternative to the drop-down menu, you can insert graphics from libraries or from your file system:

1. Select a graphic in the library or in your file system.
2. Drag-and-drop the graphic into the "Graphics list entries > Graphic" table.

##### Result

A bit graphics list is created. Graphics that appear in Runtime are assigned to the values "0" and "1".

---

**See also**

[Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-of-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning graphics and values to a bit number graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

For each bit number graphics list you specify which graphics are displayed at which bit number.

##### Requirement

- The "Text and graphics list" editor is open.
- The "Graphics list" tab is open.
- A bit number graphics list has been created and selected.

##### Procedure

1. Click "Add" in the "Graphics list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/72357797003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72357797003_DV_resource.Stream@PNG-en-US.png)
2. Select the settings "Single value" in the Inspector window "Properties > Properties > General > Value":

   - Enter the value "1" for example.
   - Select a graphic which is displayed in Runtime if the bit "0" is set in the tag.

     ![Procedure](images/55964111499_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/55964111499_DV_resource.Stream@PNG-en-US.png)
3. If required, activate the "default entry".

   The graphic is always displayed when the tag has an undefined value. Only one default entry is possible per list.
4. Create further list entries for additional bit numbers of the same graphics list.

**Note**

As an alternative to the drop-down menu, you can insert graphics from libraries or from your file system:

1. Select a graphic in the library or in your file system.
2. Drag-and-drop the graphic into the "Graphics list entries > Graphic" table.

> **Note**
>
> ****Bit selection for graphic lists****
>
> The output of the graphic list depends on the "Bit selection for text and graphics lists" option in the Runtime settings. Use this option to specify that the bit selection for graphic lists should be used on your HMI device. When you enable the option, the graphic displayed is the one configured for the set bit with the least significance. When you disable this option, the graphic that has been configured only for the set bit is displayed.

##### Result

A bit number graphics list is created. Graphics that appear in Runtime are assigned to the specified bit numbers.

---

**See also**

[Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-of-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Notes for bit number graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The bit number (0 - 31) range assigns a graphic entry from the list to each bit of a tag. If the option "Bit selection for text and graphic lists" is disabled in the Runtime settings and no default value is set, the following standard behavior applies:

- If only 1 bit is configured of all set bits, the stored graphic is displayed for the configured bit.  
  In the following example, only the set bit with significance "4" is configured. Graphic 2 is displayed.

  |  |  |  |  |  |  |  |  |  |
  | --- | --- | --- | --- | --- | --- | --- | --- | --- |
  | Significance | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
  | Set bits | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 |
  | Configured | - | Graphic 3 | - | Graphic 2 | Graphic 1 | - | - | - |
- If no bit is set or when several bits are set that are also configured, only the cactus graphic is displayed.

##### Default value

Define a default value to prevent an empty display. A configured default value is displayed in the following cases:

- The option "Bit selection for text and graphic lists" is disabled. No bit or several configured bits are set in the tag.
- The option "Bit selection for text and graphic lists" is enabled and no bit is set or a graphic is not configured for the set bit with the least significance.

##### Displaying the default value

1. Enable the graphic for the default entry in the "Default" column of the "Graphics list entries" table.   
   The value "Default entry" appears in the "Value" column of the entry.
2. You can also select the "Default" option under "Properties > General" in the inspector window.

##### Set bit with the least significance

When "Bit selection for text and graphic lists" is enabled, the graphic displayed is the one configured for the set bit with the least significance.

If no graphic is configured for the set bit with the least significance and if no default value is set, the cactus graphic is displayed. If a default value is configured, the graphic configured for the default value is displayed.

To only display the graphic for the set bit with the least significance, enable the "Bit selection for text and graphic lists" option in the "Runtime settings" editor.

This setting is deselected by default to maintain downward compatibility. The setting is valid for all graphic lists of the HMI device.

#### Configuring objects with a graphics list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The output value and value application for graphics list are specified in the display and operating object that displays the graphics of the graphics list in Runtime. The properties of these objects are configured as required.

##### Requirement

- A graphics list is created. The values have been defined. Graphics have been assigned to the values.
- You have created a tag.
- The "Screens" editor is open.
- A screen with a graphics I/O field is open. The object is edited.

##### Procedure

1. Select the graphics list the graphics of which you want to have displayed in Runtime in "Properties > Properties > General > Graphics list" in the Inspector window.
2. Select the "Input/output" setting for "Mode".

   ![Procedure](images/74906063755_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/74906063755_DV_resource.Stream@PNG-en-US.png)
3. As "Tag", select the tag whose values are defined by the display in the graphic I/O field.

**Note**

**Runtime dependency**

Different field types are available for a graphic I/O field depending on the Runtime.

##### Result

The defined graphics of the graphics list are displayed in the graphic I/O field in Runtime when the tag has the specified value.

---

**See also**

[Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-of-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Working with C text lists (RT Professional)

This section contains information on the following topics:

- [Basics on C text lists (RT Professional)](#basics-on-c-text-lists-rt-professional)
- [Creating entries in the C text list (RT Professional)](#creating-entries-in-the-c-text-list-rt-professional)

#### Basics on C text lists (RT Professional)

##### Introduction

Each HMI device is assigned to a C text list. In this list you create multilingual texts, which you then reference via the text ID in a C script. You use the C text list exclusively with functions of the API.

##### Use

You use the C text list, for example, to display texts in a screen object.

##### Multilingual texts

You can configure multiple languages for the texts in a C text list. The texts will then be displayed in the set language in Runtime. To this purpose you set the languages in the Project window under "Language support > Project languages".

##### Configuration steps

The following steps are necessary to display texts in a screen object, for example:

1. Create entries in the C text list
2. Create a screen object
3. Link C script, for example to an event of the screen object
4. Reference entries in the C script through the corresponding functions

---

**See also**

[Creating entries in the C text list (RT Professional)](#creating-entries-in-the-c-text-list-rt-professional)
  
[TXTRTGetInfoText (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#txtrtgetinfotext-rt-professional)
  
[TXTRTGetInfoTextMC (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#txtrtgetinfotextmc-rt-professional)

#### Creating entries in the C text list  (RT Professional)

##### Introduction

In the C text list you create multilingual texts, which you then reference via the text ID in a C script. You use the C text list exclusively with functions of the API.

##### Procedure

To create an entry in the C text list, follow these steps:

1. Double-click "Text and graphics lists" in the project tree.
2. Open the "C text list" tab.

   ![Procedure](images/111672848011_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111672848011_DV_resource.Stream@PNG-en-US.png)
3. Click "Add" in the table.

   The Inspector window of the C text list opens.
4. Enter the text and your comment, if needed.

   The text ID is created automatically.
5. Change the ID as needed to identify texts that belong together.

   The text ID must be within the number range 1 to 2147483647 and it must be unique. The uniqueness is checked by the system.

**Note**

If you change the text ID of an entry already referenced, this change is ignored by the syntax check in the script editor.

##### Result

An entry has been created in the C text list.

---

**See also**

[Basics on C text lists (RT Professional)](#basics-on-c-text-lists-rt-professional)
  
[TXTRTGetInfoText (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#txtrtgetinfotext-rt-professional)
  
[TXTRTGetInfoTextMC (RT Professional)](Runtime%20API%20%28RT%20Professional%29.md#txtrtgetinfotextmc-rt-professional)

## Dynamizing screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on dynamizing screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamization with animations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamization-with-animations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamization with property animation (RT Professional)](#dynamization-with-property-animation-rt-professional)
- [Dynamization in the property list (RT Professional)](#dynamization-in-the-property-list-rt-professional)
- [Dynamizing with system functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-with-system-functions-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics on dynamizing screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on dynamizing screens (Basic Panels)](#basics-on-dynamizing-screens-basic-panels)
- [Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamization in the inspector window (Basic Panels)](#dynamization-in-the-inspector-window-basic-panels)
- [Dynamization in the inspector window (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamization-in-the-inspector-window-panels-comfort-panels-rt-advanced-rt-professional)
- [Show overview of the dynamizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#show-overview-of-the-dynamizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics on dynamizing screens (Basic Panels)

##### Dynamizing objects

In WinCC you dynamize objects to map your system and show processes on HMI devices.

You implement dynamizations by

- Animations
- Tags
- System functions

One example is the mapping of a tank, the liquid level of which rises or falls in relation to a process value.

The options for dynamization depend on the object involved. When you copy an object, its dynamization functions are included.

---

**See also**

[Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)
  
[Dynamization in the inspector window (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamization-in-the-inspector-window-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Show overview of the dynamizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#show-overview-of-the-dynamizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on dynamization in the property list (RT Professional)](#basics-on-dynamization-in-the-property-list-rt-professional)
  
[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Basic on events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-on-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Dynamizing objects

In WinCC you dynamize objects to map your system and show processes on HMI devices.

You implement dynamizations by

- Animations
- System functions
- Tags
- Local scripts

One example is the mapping of a tank, the liquid level of which rises or falls in relation to a process value.

The options for dynamization depend on the object involved. When you copy an object, its dynamization functions are included.

##### Customized menus and toolbars

Use the "Menus and Toolbars" editor to configure customized menus and toolbars. These menus and toolbars are displayed in all screens of your project or in the screen windows. The menu entries and icons are connected by means of tags or VB scripts.

Use the customized menus and toolbars, for example, to change from a screen in your project to any other screen.

---

**See also**

[Basics on dynamizing screens (Basic Panels)](#basics-on-dynamizing-screens-basic-panels)
  
[Dynamization in the inspector window (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamization-in-the-inspector-window-panels-comfort-panels-rt-advanced-rt-professional)
  
[Cycle basics (RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#cycle-basics-rt-professional)

#### Dynamization in the inspector window (Basic Panels)

##### Introduction

Basically, you can dynamize all the screen objects which you have configured in a screen. Which dynamization possibilities and which events are available depends on the device and the selected object.

##### Animations

WinCC helps you to implement dynamization using predefined animations. If you want to animate an object, first configure the desired animation in the object's inspector window. Then adapt the animation to the requirements of your project.

The selection of the supported animations depends on the HMI device and the selected object. You choose between the following types of animation:

- Layout: Appearance, visibility
- Movements: direct, diagonal, horizontal and vertical movement
- Variable binding

You can configure the "Variable binding" type of animation several times for one object.

You configure animations in the "Properties > Animations" inspector window.

![Animations](images/74855728139_DV_resource.Stream@PNG-en-US.png)

##### Events

Operable objects also react to events, such as a mouse click.

You configure a function list with system functions on an event. The system functions are processed as a reaction to the triggered event.

You configure events in the "Properties > Events" inspector window.

![Events](images/111848724747_DV_resource.Stream@PNG-en-US.png)

You can find more detailed information on this under "[Working with Function Lists](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-function-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

---

**See also**

[Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)
  
[Working with Function Lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-function-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Dynamization in the inspector window (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Basically, you can dynamize all the screen objects which you have configured in a screen. Which dynamization possibilities and which events are available depends on the device and the selected object.

The inspector window offers you the possibilities for dynamization of screen objects in three tabs.

##### Property list

With the ![Property list](images/25618366987_DV_resource.Stream@PNG-de-DE.png) button you go to the properties list in the "Properties > Properties" inspector window.

In the property list, you set any dynamization for the individual object properties using tags or local C and VB scripts. You can, for example, dynamically change the background color of an object.

In the "Dynamic Value" column you can dynamize the object property of a tag, a C-script or a VB-script.

Whether an object property can be dynamized is indicated in the Property list by means of the background color:

- Light gray: Can be dynamized
- Dark gray: Cannot be dynamized

Any animations you have already configured will also appear in the object property list, where you can edit the animations.

The following table shows you how to sort the property list:

| Symbol | Meaning |
| --- | --- |
| ![Property list](images/25620696459_DV_resource.Stream@PNG-de-DE.png) | Sort by alphabet |
| ![Property list](images/25620700299_DV_resource.Stream@PNG-de-DE.png) | Sort by category |

With the ![Property list](images/25618366987_DV_resource.Stream@PNG-de-DE.png) button you return to the property pages in the inspector window.

![Property list](images/74856049547_DV_resource.Stream@PNG-en-US.png)

##### Animations

You have two different options for animating objects.

You configure animations

- in the inspector window under "Properties > Animations",
- in the "Animations" task card.

WinCC helps you to implement dynamization using predefined animations. If you want to animate an object, first configure the desired animation with the tools of the toolbox or in the object's inspector window. Then customize the animation in the Inspector window to suit the requirements of your project.

The selection of the supported animations depends on the device and the selected object. You choose between the following types of animation:

- Tag binding
- Layout: Appearance, control enable, visibility
- Movements: direct, diagonal, horizontal and vertical movement
- Property animation

  > **Note**
  >
  > **HMI device dependency**
  >
  > The "Control enable" animation is not available for every HMI device.

You can configure the "Tag binding" and "Property animation" types of animation several times for one object.

You configure animations in the "Properties > Animations" inspector window.

![Animations](images/74855728139_DV_resource.Stream@PNG-en-US.png)

##### Events

Operator control enabled objects also react to events, such as a mouse click.

You configure a function list with system functions or local scripts on an event. The system functions or the local script are processed as a reaction to the triggered event.

You configure events in the "Properties > Events" inspector window.

![Events](images/111848724747_DV_resource.Stream@PNG-en-US.png)

You can find more detailed information on this under "[Working with Function Lists](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-function-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

---

**See also**

[Local scripts (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#local-scripts-rt-professional)
  
[Working with Function Lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-function-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Show overview of the dynamizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can set the update cycle separately for every single dynamization. The number of different update cycles is limited to five per project.

##### Show overview of existing dynamizations

1. Select a screen in the project tree.
2. Select "Overview dynamizations" in the shortcut menu.

   ![Show overview of existing dynamizations](images/89040710411_DV_resource.Stream@PNG-en-US.png)

   ![Show overview of existing dynamizations](images/89040710411_DV_resource.Stream@PNG-en-US.png)

##### Result

All objects and their dynamizations are shown in the work area in the screen. Under "Cycle" you select another update cycle if necessary.

---

**See also**

[Basics on dynamization in the property list (RT Professional)](#basics-on-dynamization-in-the-property-list-rt-professional)
  
[Basics on dynamizing screens (Basic Panels)](#basics-on-dynamizing-screens-basic-panels)

### Dynamization with animations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamizing the appearance of an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-the-appearance-of-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring movements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-movements-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring direct movement (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-direct-movement-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamizing control enable of an operating element (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-control-enable-of-an-operating-element-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamizing the visibility of an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-the-visibility-of-an-object-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring animation with tag connection (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-animation-with-tag-connection-panels-comfort-panels-rt-advanced-rt-professional)
- [Animations of object groups (Basic Panels)](#animations-of-object-groups-basic-panels)
- [Animations of object groups (Panels, Comfort Panels, RT Advanced, RT Professional)](#animations-of-object-groups-panels-comfort-panels-rt-advanced-rt-professional)
- [Animations in multiple selection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#animations-in-multiple-selection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Use predefined animations to dynamize screen objects.

##### Requirement

- You have opened a screen which contains at least one dynamic object.
- The Inspector window is open.
- The toolbox window is displayed.

##### Procedure in the inspector window

1. In the Inspector window, select "Properties > Animations".
2. Select the animation you want to use.
3. Click the ![Procedure in the inspector window](images/21534885131_DV_resource.Stream@PNG-de-DE.png)button.

##### Procedure in the "Animations" task card.

1. Open the object group containing the required animation in the "Animations" task card.
2. Drag the animation onto the object that you want to make dynamic.

Alternatively you select the object in the screen and double click the desired animation in the "Animation" task card.

##### Result

The animation appears in the Inspector window of the object. You configure the animation in the following steps.

In the animations overview, the green arrow indicates which animation is already configured. The configured animation opens in the inspector window when you click the green arrow.

![Result](images/70651912075_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Data types for the animations**
>
> When you dynamize an animation with a tag, you always see only the data types that are permitted. For example, the "Visibility" animation only supports tags with the data types Bool, DInt, Int, SInt, UDInt, UInt, USInt.

---

**See also**

[Dynamizing the appearance of an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-the-appearance-of-an-object-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring movements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-movements-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring direct movement (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-direct-movement-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Dynamizing control enable of an operating element (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-control-enable-of-an-operating-element-panels-comfort-panels-rt-advanced-rt-professional)
  
[Dynamizing the visibility of an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-the-visibility-of-an-object-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring animation with tag connection (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-animation-with-tag-connection-panels-comfort-panels-rt-advanced-rt-professional)
  
[Animations in multiple selection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#animations-in-multiple-selection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)
  
[Animations of object groups (Panels, Comfort Panels, RT Advanced, RT Professional)](#animations-of-object-groups-panels-comfort-panels-rt-advanced-rt-professional)
  
[Dynamization with property animations (RT Professional)](#dynamization-with-property-animations-rt-professional)

#### Dynamizing the appearance of an object (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The appearance of a screen object is controlled by changing the value of a tag in runtime. When the tag adopts a certain value, the screen object changes its color or flashing characteristics according to the configuration.

##### Type

Areas or single values of the tag are observed in Runtime depending on the selection. The appearance of the object changes according to the configuration.

> **Note**
>
> **"Multiple bits" selection**
>
> If you use the "Multiple bits" option, also select "Bit selection for appearance" option in the runtime settings under "Screens > General".

##### Requirement

- A screen is open.
- A dynamic object is contained and selected in the screen.
- The Inspector window is open.
- The toolbox window is displayed.

##### Procedure

1. In the Inspector window, select "Properties > Animations".

   The animations available for the selected object are displayed.
2. Select the animation "Appearance" and click the ![Procedure](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.

   The parameters of the animation are displayed.
3. Select a tag in "Tag > Name".
4. Select "Type > Range" for example.
5. Click "Add" in the table.
6. Enter the tag interval "0 - 20" in the "Range" column for example.
7. For "Foreground color" and "Background color", select the color the object is to acquire in Runtime when the tag reaches the interval.
8. Select a flashing mode for the object from the "Flashing" list.
9. Repeat steps 5 to 8 to create another tag interval, e.g. "21 - 60".

   ![Procedure](images/111849663627_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111849663627_DV_resource.Stream@PNG-en-US.png)

##### Result

In Runtime, the flashing response, and color of the object change dynamically according to the process value returned in the tag.

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring movements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can configure dynamic objects in such a way that they move on a certain track. The movement is controlled via tags. The object moves every time the tag is updated.

You can only program one type of movement for each object.

##### Requirement

- You have created a tag.
- You have opened a screen which contains at least one dynamic object.
- The Inspector window is open.
- The toolbox window is displayed.

##### Procedure

1. Select the screen object you want to control dynamically.

   The object properties are displayed in the Inspector window.
2. In the Inspector window, select "Properties > Animations".

   The animations available for the selected object are displayed.
3. Select "Horizontal movement" and click the ![Procedure](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.

   The parameters of the animation are displayed.

   A transparent copy of the object is shown in the work area, which is connected to the source object by means of an arrow.
4. Select a tag for control of movement.
5. Move the object copy to the relevant destination. The system automatically enters the pixel values of the final position in the Inspector window.
6. Customize the range of values for the tag as required.

   ![Procedure](images/111850068747_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111850068747_DV_resource.Stream@PNG-en-US.png)

##### Result

In Runtime, the object moves in response to every change in value of the tag that is used to control the movement. The direction of movement corresponds to the configured type of movement "horizontal".

> **Note**
>
> You configure vertical and diagonal movements similar to horizontal movements

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring direct movement (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The object is moved respectively in x direction and y direction with "Direct movement". Two tags define the number of pixels by which the object moves from its original static start position.

##### Requirement

- Two tags are set up.
- You have opened a screen which contains at least one dynamic object.
- The Inspector window is open.
- The toolbox window is displayed.

##### Configuring "Direct movement"

1. Select the screen object you want to control dynamically.

   The object properties are displayed in the Inspector window.
2. In the Inspector window, select "Properties > Animations".
3. Select "Direct movement" and click the ![Configuring "Direct movement"](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.

   The parameters of the animation are displayed.
4. Select a tag for the X position with which the movement in x direction is controlled.
5. Select a tag for the Y position with which the movement in y direction is controlled.

   ![Configuring "Direct movement"](images/60906470667_DV_resource.Stream@PNG-en-US.png)

   ![Configuring "Direct movement"](images/60906470667_DV_resource.Stream@PNG-en-US.png)

##### Result

In Runtime, the object moves in response to every change in value of the tag that is used to control the movement.

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Dynamizing control enable of an operating element (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can dynamically change the usability of an operating element. The object either can, or cannot be used in Runtime, depending on the value of a tag.

You can use this dynamic control to restrict operator access to an operating element to specific situations, such as for maintenance.

##### Requirement

- You have created a tag.
- A screen with an operating element is open.
- The Inspector window is open.
- The toolbox window is displayed.

##### Procedure

1. Select the operating element in the screen that you want to control dynamically.

   The object properties are displayed in the Inspector window.
2. In the Inspector window, select "Properties > Animations".

   The animations available for the selected object are displayed.
3. Select "Control enable" and click the ![Procedure](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.

   The parameters of the animation are displayed.

   ![Procedure](images/111851536267_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111851536267_DV_resource.Stream@PNG-en-US.png)
4. Select a tag.
5. Activate "Range".

   - For "From:" enter e.g. the value "0"
   - For "To:" enter e.g. the value "100"
6. Activate "Control enable > Activated".

##### Result

The screen object is operator control enabled in Runtime depending on the tag value:

- The object becomes operator control enabled when the tag value is between 0 and 100.
- The object is not operator control enabled if the tag value is outside the range.

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Dynamizing the visibility of an object (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Dynamization of the "Visibility" property allows you to output an alarm to your screen, which is triggered when the tag value exceeds a critical range, for example. The alarm is cleared when the tag value returns to the non-critical range.

The "Simple recipe view" and "Simple alarm view" objects are always visible.

##### Requirement

- You have created a tag.
- You have opened a screen containing an object that you want to show or hide in Runtime.
- The Inspector window is open.

##### Procedure

1. Select the screen object you want to control dynamically.

   The object properties are displayed in the Inspector window.
2. In the Inspector window, select "Properties > Animations".

   The animations available for the selected object are displayed.
3. Select "Visibility" and click the ![Procedure](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.

   The parameters of the animation are displayed.
4. Select a tag.
5. Activate "Range".
6. Select, for example, "from 20" and "to 40"
7. Activate "Visible".

   ![Procedure](images/89378914571_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/89378914571_DV_resource.Stream@PNG-en-US.png)

##### Result

The screen object is shown or hidden in Runtime depending on the tag value.

- If the tag value matches the configured range between 20 and 40, the screen object is shown.
- If the tag value is outside the configured range, the screen object is hidden.

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring animation with tag connection (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you object property an object property with a tag, the object property is changed in Runtime depending on the tag value.

The following example shows the tag binding in the "Properties > Animations" inspector window. If you have configured tag binding it is also visible in the property list or in the property pages in the inspector window.

##### Requirement

- An object with the property to be dynamized is selected.
- You have created a tag.
- The Inspector window is open.

##### Procedure

1. Select the screen object whose properties you want to control dynamically.

   The object properties are displayed in the Inspector window.
2. In the Inspector window, select "Properties > Animation".

   The animations available for the selected object are displayed.
3. Select "Tag connection" and click the ![Procedure](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.

   The parameters of the animation are displayed.
4. Select the object property that you want to dynamize in "Properties > Animation > Tag binding > Property > Name", e.g. "Background color".
5. Select a tag.

   ![Procedure](images/60909759883_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/60909759883_DV_resource.Stream@PNG-en-US.png)

##### Result

You have dynamized the "Background color" property with a tag. The background color of the screen object changes in Runtime depending on which value the tag adopts.

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Animations of object groups (Basic Panels)

##### Applying animations to object groups

The inspector window shows all objects of a group and their possible animations. The animation types which are supported by all objects in the group are also listed separately.

![Applying animations to object groups](images/111843406347_DV_resource.Stream@PNG-en-US.png)

If you configure an animation for an object group, this animation will apply to all individual objects that support this animation.

The animation of nested groups is not supported.

##### Application example

The "horizontal movement" animation is configured for the object of an object group. The "direct movement" animation is configured for the whole object group. Only the animation of the object group i.e. "direct movement" is executed in Runtime. This also applies for object groups within object groups. Only the animation of the group on the top layer is listed.

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Animations of object groups (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Changing animations of object groups

The inspector window shows all objects of a group and their possible animations. The animation types which are supported by all objects in the group are also listed separately.

If you configure an animation for an object group, this animation will apply to all individual objects that support this animation.

![Changing animations of object groups](images/111843884171_DV_resource.Stream@PNG-en-US.png)

##### Application example

The "horizontal movement" animation is configured for the object of an object group. The "direct movement" animation is configured for the whole object group. Both animation types are executed in runtime. This also applies for object groups within object groups.

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Animations in multiple selection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Changing animations for multiple objects

For a multiple selection, the animations that are configured for the reference object appear in the Inspector window. You can change the animations as usual. The changes will apply to all the objects in the multiple selection that support the configured animation. This means that even objects for which you have not yet configured an animation will have the reference object's animation.

##### Application example

Select a button, and a circle at the same time. The button is the reference object. The "Appearance" animation is already configured for the button, so it appears in the Inspector window of the multiple selection. When you activate "Properties > Animations >Appearance > Flashing" in the inspector window, the settings of the "Appearance" animation apply for the button and for the circle.

##### Configuring new animations for multiple objects

If you configure a new animation for the objects of a multiple selection, this animation will apply to all selected objects that support the configured animation. If the new animation replaces an existing animation, a security prompt appears.

##### Application example

You select a circle, and a rectangle. The "Diagonal movement" animation is already configured for the circle. You configure the "Horizontal movement" animation for the multiple selection. This animation applies to the rectangle since no animation of the Movement type is yet configured for it. For the circle, you are asked to confirm that you want to replace the existing "Diagonal movement" animation with the new "Horizontal movement" animation.

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Dynamization with property animation (RT Professional)

This section contains information on the following topics:

- [Dynamization with property animations (RT Professional)](#dynamization-with-property-animations-rt-professional)
- [Configuring property animation of the "Range" type (RT Professional)](#configuring-property-animation-of-the-range-type-rt-professional)
- [Configuring property animation of the "Bool" type (RT Professional)](#configuring-property-animation-of-the-bool-type-rt-professional)
- [Configuring property animation of the "Direct" type (RT Professional)](#configuring-property-animation-of-the-direct-type-rt-professional)
- [Configuring property animation of the "Single bit" type (RT Professional)](#configuring-property-animation-of-the-single-bit-type-rt-professional)
- [Configuring property animation of the "Multiple bits" type (RT Professional)](#configuring-property-animation-of-the-multiple-bits-type-rt-professional)

#### Dynamization with property animations (RT Professional)

##### Introduction

With the property animation you dynamize the properties of screens and screen objects depending on certain value ranges or tags. You select value ranges and determine how the linked object property changes when the tag adopts a certain value in runtime. You have the option of dynamizing several object properties simultaneously, e.g. the position and the color of a screen object. You can also configure several property animations on one object.

> **Note**
>
> **Dynamizing several object properties at the same time**
>
> You can dynamize multiple object properties with animation. The order of processing in runtime is not necessarily the same as the order of property configuration in the Inspector window under "Properties > Animation".

> **Note**
>
> If you use the operands "=", ">", "<", "!=" in the expression, note the following:  
> The value for "true" = -1   
> The value for "false" = 0
>
> Please note that the runtime value of a Boolean tag "true" = 1 and = "false" = 0.

##### Type

The following types are available to define the value range:

- Range (floating point)

  You configure different value ranges with floating point numbers. Enter each value range in square brackets and specify whether the range limit is included in this value range. If the value is within a configured value range in runtime, the linked object property is dynamized.
- Range (integer)

  One or more value ranges of a tag are viewed. You configure different value ranges. You define the appropriate values of the object property for every value range. If the value is within a configured value range in runtime, the linked object property is dynamized.

  Only define value ranges as integers. A non-integer tag value or expression is rounded up or down accordingly.
- Bool (true, false)

  The Boolean tag or an expression which contains a logical comparison is viewed. If the tag or return value of the expression returns one of the two values – true or false – the value is assigned to the dynamized property.
- Direct

  Unlike the other types, the tag value or expression in the "Direct" type is written directly into the object property.
- Single bit

  You can select the bit of the tag which is to be monitored. If the bit is to be set, configure the value "0". If the bit is not to be set, configure the value "1".
- Multiple bits

  One or more bit numbers of a tag are viewed. You configure different bit numbers. The linked object property is only dynamized if the tag value in runtime exactly matches one of the configured bit numbers. If the variable value does not match, the static value of the object property is displayed.

##### Expression

The "Expression" option is only available for the "Range", "Boolean" and "Direct" types.

You can formulate the expression by using tags, VB-scripts and arithmetic operators. The value of the expression is determined in runtime and compared with the configured value ranges. The following selection of VBS keywords and constants is available within an expression:

`"`
`mod`
`", "`
`not`
`", "`
`and`
`" "`
`or`
`","`
`xor`
`","`
`eqv`
`", "`
`imp`
`", "`
`vbTrue`
`", "`
`vbFalse`
`"`

##### Evaluation "Quality Code"

Use "Quality Code" to check the status and quality of a tag. The quality of the entire value transmission and value processing of the respective tag is combined in the displayed "Quality Code". The monitoring of the "Quality Code" enables you to draw conclusions about the quality of the tags in the process.

The evaluation of the "Quality Code" has priority over the defined value ranges.

If you use several tags, the "Quality Code" of the tags is evaluated in the order in which they appear from left to right in the expression. The configured values are only viewed if the "Quality Code" of the tag is correct.

The figure below shows a selection of the offered "Quality Codes". The "Quality Codes" are sorted in descending order of priority in this list.

![Evaluation "Quality Code"](images/23717507211_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring a new animation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-new-animation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring property animation of the "Range" type (RT Professional)](#configuring-property-animation-of-the-range-type-rt-professional)
  
[Configuring property animation of the "Direct" type (RT Professional)](#configuring-property-animation-of-the-direct-type-rt-professional)
  
[Configuring property animation of the "Bool" type (RT Professional)](#configuring-property-animation-of-the-bool-type-rt-professional)

#### Configuring property animation of the "Range" type (RT Professional)

##### Introduction

When you dynamize an object property with a tag, the object property is changed in runtime depending on the tag value. The following example shows the dynamization of a circle. The circle changes its color and position depending on a tag.

##### Requirement

- You have created a "Tag1" tag.
- You have created a screen.
- You have inserted and marked a circle in the screen.
- The Inspector window is open.

##### Select animation type, tag and type

1. Click "Properties > Animations" in the Inspector window.  
   The animations available for the selected object are displayed.
2. Select "Animate property" and click the ![Select animation type, tag and type](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.  
   The animation parameters are displayed.
3. Enter the name "Light" under "Settings > Name".
4. Select "Range" as type.
5. Activate "Process > Tag".
6. Select "Tag1" under "Process > Tag".

##### Select object properties and ranges

1. Click "Add property" ![Select object properties and ranges](images/21534885131_DV_resource.Stream@PNG-de-DE.png).  
   A selection list opens.
2. Select the property "Y position". A column "Y position" is added to the table.
3. Click "Add property" ![Select object properties and ranges](images/21534885131_DV_resource.Stream@PNG-de-DE.png).  
   A selection list opens.
4. Select the property "Color background". A column "Color background" is added to the table.
5. Click "Add" in the table.
6. Define the first range from "0 - 49".
7. Click "Add" in the table.
8. Define the second range from "50 - 99".
9. Click "Add" in the table.
10. Define the third range from "100 - 149".

##### Assign the background color and position to a range

Define the following settings for the ranges:

- Range 0 - 49: Y position "200"; color "green"
- Range 50 - 99: Y position"220"; color "yellow"
- Range 100 - 149: Y position "240"; color "red"

  ![Assign the background color and position to a range](images/111854269579_DV_resource.Stream@PNG-en-US.png)

##### Result

Depending on the value range in which the tag is located in runtime, the circle changes its position and background color.

---

**See also**

[Dynamization with property animations (RT Professional)](#dynamization-with-property-animations-rt-professional)

#### Configuring property animation of the "Bool" type (RT Professional)

##### Introduction

When you dynamize an object property with a tag, the object property is changed in runtime depending on the tag value. In the following example, a button is shown and hidden depending on the value of an expression.

> **Note**
>
> Boolean tags for the "Bool" type are implicitly converted to the VB script values "true" = -1 and "wrong" = 0 using the VB script function, CBool.
>
> Use the constants "`vbTrue`" and "`vbFalse`" for a unique comparison in the expression.

##### Requirement

- A "TCelsius" tag of the "Uint" type is created.
- You have created a screen.
- You have inserted and marked a button in the screen.
- The Inspector window is open.

##### Select animation type, expression and type

1. Click "Properties > Animations" in the Inspector window.  
   The animations available for the selected object are displayed.
2. Select "Animate property" and click the ![Select animation type, expression and type](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.  
   The animation parameters are displayed.
3. Enter the name "Visibility" under "Settings > Name".
4. Select "Bool" as type.
5. Activate "Process > Expression".
6. Enter the following expression in the field: "(('TCelsius’ × 9) / 5) + 32 < 100".

**Note**

Make sure to write the tag names in single inverted commas in the direct input.

**Note**

Boolean tags can be evaluated simplified:   
"'Booltag1' AND NOT 'Booltag2'".

Alternatively, enter the expression with the buttons above the field. For example, click the ![Select animation type, expression and type](images/23919192587_DV_resource.Stream@PNG-de-DE.png) button and select a tag from the selection list.

##### Select object property

1. Click "Add property" ![Select object property](images/21534885131_DV_resource.Stream@PNG-de-DE.png).  
   A selection list opens.
2. Select the "Visibility" property. A "Visible" column is added to the table.
3. Activate the "Visibility" property for the "True" value in the table.

   ![Select object property](images/111846865291_DV_resource.Stream@PNG-en-US.png)

   ![Select object property](images/111846865291_DV_resource.Stream@PNG-en-US.png)

##### Result

The value of the expression is determined in runtime. The button is displayed if the value matches the configured "True" value.

---

**See also**

[Dynamization with property animations (RT Professional)](#dynamization-with-property-animations-rt-professional)

#### Configuring property animation of the "Direct" type (RT Professional)

##### Introduction

When you dynamize an object property with a tag, the object property is changed in Runtime depending on the tag value. The following example shows the dynamization of an I/O field. The I/O field changes its output value depending on a tag.

##### Requirement

- You have created a "Tag1" tag.
- You have created a screen.
- You have inserted and selected an I/O field with the "Output" mode in the screen.
- The inspector window is open.

##### Select animation type, tag and type

1. Click "Properties > Animations" in the Inspector window.

   The animations available for the selected object are displayed.
2. Select "Animate property" and click the ![Select animation type, tag and type](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.

   The parameters of the animation are displayed.
3. Enter the name "Fill level" under "Settings > Name".
4. Select "Direct" as type".
5. Activate "Process > Tag".
6. Select "Tag1" under "Process > Tag".

##### Result

The tag value in Runtime is written directly into the I/O field.

---

**See also**

[Dynamization with property animations (RT Professional)](#dynamization-with-property-animations-rt-professional)

#### Configuring property animation of the "Single bit" type (RT Professional)

##### Introduction

When you dynamize an object property with a tag, the object property is changed in runtime depending on the tag value. The following example shows the dynamization of a button. The button changes its border color depending on the tag.

##### Requirement

- You have created a "Tag1" tag.
- You have created a screen.
- You have inserted and marked a button in the screen.
- The Inspector window is open.

##### Select animation type, tag and type

1. Click "Properties > Animations" in the Inspector window.  
   The animations available for the selected object are displayed.
2. Select "Animate property" and click the ![Select animation type, tag and type](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.  
   The animation parameters are displayed.
3. Enter the name "Border color" under "Settings > Name".
4. Select "Single bit" as the type.
5. Select the bit position, for example, "4".
6. Activate "Process > Tag".
7. Select the "Tag_1" tag under "Process > Tag".

##### Select object property with the type "Single bit"

1. Click "Add property" ![Select object property with the type "Single bit"](images/21534885131_DV_resource.Stream@PNG-de-DE.png).  
   A selection list opens.
2. Select the "Border color" property, for example. A column "Border color" is added to the table.
3. Enter the value "0" in the "Value" column.   
   The color you configured under "Properties > Appearance > Border > Color" is displayed in the "Border color" column.
4. Enter the value "1" in the "Value" column.
5. In the "Border color" column, select the alternative border color, for example, blue.

   ![Select object property with the type "Single bit"](images/150169202571_DV_resource.Stream@PNG-en-US.PNG)

   ![Select object property with the type "Single bit"](images/150169202571_DV_resource.Stream@PNG-en-US.PNG)

##### Result

If bit "4" of the tag has the value "1" in runtime, the border is shown in blue. If bit "4" is not set, the border is shown in red.

#### Configuring property animation of the "Multiple bits" type (RT Professional)

##### Introduction

When you dynamize an object property with a tag, the object property is changed in runtime depending on the tag value. The following example shows the dynamization of a button. The button changes its border color depending on the tag.

##### Requirement

- You have created a "Tag1" tag.
- You have created a screen.
- You have inserted and marked a button in the screen.
- The Inspector window is open.

##### Select animation type, tag and type

1. Click "Properties > Animations" in the Inspector window.  
   The animations available for the selected object are displayed.
2. Select "Animate property" and click the ![Select animation type, tag and type](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.  
   The animation parameters are displayed.
3. Enter the name "Color" under "Settings > Name".
4. Select "Multiple bits" as the type.
5. Activate "Process > Tag".
6. Select the "Tag_1" tag under "Process > Tag".

##### Select object property with the type "Multiple bits"

1. Click "Add property" ![Select object property with the type "Multiple bits"](images/21534885131_DV_resource.Stream@PNG-de-DE.png).  
   A selection list opens.
2. Select the property "Border color". A column "Border color" is added to the table.
3. Add the value "0" in the "Value" column.  
   The color you configured under "Properties > Appearance > Border > Color" is displayed in the "Border color" column.
4. In the second row, enter the value "5", for example, in the "Value" column.
5. In the "Border color" column, select a border color, for example, blue.
6. In the third row, enter the value "8" in the "Value" column.
7. In the "Border color" column, select a border color, for example, green.
8. In the fourth row, enter the value "11", for example, in the "Value" column.
9. In the "Border color" column, select a border color, for example, yellow.

   ![Select object property with the type "Multiple bits"](images/150290727179_DV_resource.Stream@PNG-en-US.png)

   ![Select object property with the type "Multiple bits"](images/150290727179_DV_resource.Stream@PNG-en-US.png)

##### Result

When the tag value in runtime is identical to the configured value, the order color of the button is changed accordingly. If the variable value does not match any of the configured values, the static value of the object property is displayed.

### Dynamization in the property list (RT Professional)

This section contains information on the following topics:

- [Basics on dynamization in the property list (RT Professional)](#basics-on-dynamization-in-the-property-list-rt-professional)
- [Dynamizing an object property with a tag (RT Professional)](#dynamizing-an-object-property-with-a-tag-rt-professional)
- [Programming a dynamization method for a tag change (RT Professional)](#programming-a-dynamization-method-for-a-tag-change-rt-professional)
- [Dynamizing an object property with local scripts (RT Professional)](#dynamizing-an-object-property-with-local-scripts-rt-professional)

#### Basics on dynamization in the property list (RT Professional)

##### Basic principle of dynamization

In the case of an object property that can be dynamized you first specify the type of dynamization. The following figure shows the types of dynamization available:

![Basic principle of dynamization](images/101653405451_DV_resource.Stream@PNG-en-US.png)

Depending on the type of dynamization you either select a tag using the object list or you create a local script.

##### Dynamization with tags

If you dynamize an object property with a tag, you can configure a function list additionally on the following events:

- Changed
- Tag status changed
- Quality code changed

The tags are updated in the update cycle set for the screen.

The figure below shows the "Radius" object property dynamized with a tag. When the value of the tag changes, a function list is executed additionally:

![Dynamization with tags](images/100534627211_DV_resource.Stream@PNG-en-US.png)

You can also convert the function list into a local script.

##### Quality Code

Use "Quality Code" to check the status and quality of a tag. The quality of the entire value transmission and value processing of the respective tag is combined in the displayed "Quality Code". The monitoring of the "Quality Code" enables you to draw conclusions about the quality of the tags in the process.

##### Dynamization with local scripts

With a local script you dynamize an object property in Runtime by means of the return value of the local script. The script is created directly at the instance where it is used. The following figure shows the implementation of a status indicator by dynamizing the background color using a VB script:

![Dynamization with local scripts](images/72358867339_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Dynamizing an object property with a tag (RT Professional)](#dynamizing-an-object-property-with-a-tag-rt-professional)
  
[Programming a dynamization method for a tag change (RT Professional)](#programming-a-dynamization-method-for-a-tag-change-rt-professional)
  
[Dynamizing an object property with local scripts (RT Professional)](#dynamizing-an-object-property-with-local-scripts-rt-professional)
  
[Show overview of the dynamizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#show-overview-of-the-dynamizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)
  
[Local scripts (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#local-scripts-rt-professional-1)

#### Dynamizing an object property with a tag (RT Professional)

##### Introduction

When you dynamize an object property with a tag, the object property is changed in Runtime depending on the tag value. When you indirectly dynamize the object property, you connect the property to a tag that sets the property value in Runtime.

##### Requirement

- An object with the property to be dynamized is selected.
- You have created a tag.
- The Inspector window is open.

##### Procedure

1. Select the screen object whose properties you want to control dynamically.

   The object properties are displayed in the Inspector window.
2. Click the ![Procedure](images/25618366987_DV_resource.Stream@PNG-de-DE.png) button in the Inspector window.

   The property list is displayed with the properties of the selected object.
3. Select the property to be dynamized.
4. In the "Dynamization" column, select the entry "HMI_Tag".

   A dialog opens.
5. Select a tag.
6. Activate "Use indirect addressing" to dynamize the object property.

   ![Procedure](images/101655007883_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/101655007883_DV_resource.Stream@PNG-en-US.png)

##### Result

The object property changes in Runtime according to how the property list is configured.

##### Representation of a multiple selection in the property list

If you selected multiple objects at the same time, the "Object type" column is added to the property list. The objects that support the property displayed in the row are displayed in this column. Changes to, or dynamization applied to a property affect all the objects displayed in the "Object type" column.

---

**See also**

[Basics on dynamization in the property list (RT Professional)](#basics-on-dynamization-in-the-property-list-rt-professional)
  
[Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)

#### Programming a dynamization method for a tag change (RT Professional)

##### Introduction

If you have entered a tag in the "Dynamization" column, you can configure a function list additionally on different events.

##### Requirement

- An object with the property to be dynamized is selected.
- You have created a tag.
- The property list is open in the inspector window.
- An object property is connected with the tag.

##### Procedure

1. Extend the property list by clicking next to the property which you have dynamized with a tag.
2. Three other lines with the following events are displayed below the property.

   - Changed
   - Tag status changed
   - Quality code changed
3. Configure a function list for the required event.

   Alternatively you can convert the function list into a local script.

   ![Procedure](images/111847848075_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111847848075_DV_resource.Stream@PNG-en-US.png)

##### Result

The object property changes in Runtime according to how the property list is configured.

---

**See also**

[Basics on dynamization in the property list (RT Professional)](#basics-on-dynamization-in-the-property-list-rt-professional)

#### Dynamizing an object property with local scripts (RT Professional)

##### Introduction

With a local script you dynamize an object property in Runtime by the return value of the script.

##### Requirement

- The object with the property to be dynamized is selected.
- The Inspector window is open.

##### Procedure

1. Click ![Procedure](images/25618359435_DV_resource.Stream@PNG-de-DE.png) in the Inspector window.
2. Select the object property to be dynamized.
3. Select the "VB script" or "C script" entry in the "Dynamization" column.

   A dialog opens.
4. Write the program code.
5. Click "![Procedure](images/24096985227_DV_resource.Stream@PNG-de-DE.png)" in the toolbar to change the trigger.

##### Result

The object property changes in Runtime according to how the property list is configured.

##### Deleting the dynamization

1. Select the dynamized object property in the property list.
2. Select the "None" entry in the "Dynamization" column.

---

**See also**

[Basics on dynamization in the property list (RT Professional)](#basics-on-dynamization-in-the-property-list-rt-professional)
  
[Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)
  
TransparentColorPictureOff (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)
  
[Creating local scripts (RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-local-scripts-rt-professional)

### Dynamizing with system functions (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basic on events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-on-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configure system function on the "Click" event (Basic Panels)](#configure-system-function-on-the-click-event-basic-panels)
- [Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basic on events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Screen objects react to events. You configure a function list with system functions on the events of an object.

##### Events

Which events and system functions are available depends on the object used.

If the operator activates a screen object for example, the configured system function is executed.

You can find additional information at "[Basics on Function Lists](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-function-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

---

**See also**

[Basics on dynamizing screens (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-dynamizing-screens-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configure system function on the "Click" event (Basic Panels)](#configure-system-function-on-the-click-event-basic-panels)
  
[Working with Function Lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#working-with-function-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configure system function on the "Click" event (Basic Panels)

##### Introduction

You configure a function list on an object event. The linked system function is executed when the event occurs in runtime.

##### Requirements

A screen is open.

A button has been created in the screen.

The inspector window is open.

##### Procedure

1. Select the button.
2. Click "Properties> Events" in the Inspector window.
3. Select the "Click" event.
4. Click "Add function" in the table.
5. Select the "ShowAlarmWindow" system function.

##### Result

The alarm window opens in the screen if the operator clicks the button in runtime.

---

**See also**

[Basic on events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-on-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics of the function list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20system%20functions%20and%20Runtime%20scripting%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-the-function-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this example, you configure a button that can be used to toggle between multiple runtime languages during runtime.

##### Requirements

- You have completed the "Configuring a button in multiple languages" example.
- The "Screen_1" screen is open.
- The button on the screen has been selected.

##### Procedure

1. In the Inspector window, select "Properties > Events > Press".
2. Click on "Add function" in the table.
3. Select the "SetLanguage" system function and the "Switch" setting.

##### Result

You have assigned the button the function "SetLanguage". Pressing the button during runtime will switch the runtime language. The runtime languages are switched in the order specified by the number sequence in the "Languages and fonts" editor.

---

**See also**

[Basic on events (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-on-events-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-function-keys-basic-panels-panels-comfort-panels-rt-advanced-1)
- [Assigning function keys globally (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-function-keys-globally-basic-panels-panels-comfort-panels-rt-advanced)
- [Local assignment of function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#local-assignment-of-function-keys-basic-panels-panels-comfort-panels-rt-advanced)
- [Assigning a function to a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-a-function-to-a-function-key-basic-panels-panels-comfort-panels-rt-advanced)
- [Assigning operator authorization for a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-operator-authorization-for-a-function-key-basic-panels-panels-comfort-panels-rt-advanced)
- [Assigning a graphic to a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-a-graphic-to-a-function-key-basic-panels-panels-comfort-panels-rt-advanced)
- [Configuring LED tags (Basic Panels, Panels, Comfort Panels, RT Advanced)](#configuring-led-tags-basic-panels-panels-comfort-panels-rt-advanced)
- [Example: Using function keys for screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-using-function-keys-for-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)

### Working with function keys  (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

The function key is a physical key on your HMI device and its functions can be configured. A function list can be configured for the events "Key pressed" and "Release key".

A function key can be assigned global or local functions.

> **Note**
>
> **Availability for specific HMI devices**
>
> Function keys are not available on all HMI devices.

#### Global function keys

Global function keys always trigger the same action, regardless of the displayed screen.

Global function keys are configured in the "Global Screen" editor. The global assignment applies for all the screens of the set HMI device.

Global function keys reduce programming considerably, because there is no need to assign these global keys to each individual screen.

#### Local function keys in screens

Local function keys in screens can trigger a different action in each screen. This assignment applies only to the screen in which you have defined the function key.

Within a screen, a function key has only one function assignment, either a global or local one. The project planner specifies which assignment has priority.

> **Note**
>
> If a screen with local function keys is overlapped by an alarm view or an alarm window, then the function keys are still active in runtime. This may happen in particular on HMI devices with a small display.

#### Local function keys in templates

Local functions keys that are assigned in templates are valid for all the screens based on this template. They can trigger a different action in every screen. Function keys for templates are assigned in the template of the "Screens" editor. Within a template, a function key has only one function assignment, either a global or local one. The project planner specifies which assignment has priority.

#### Hotkey assignment

You can assign hotkeys, such as buttons, to control objects. The available hotkeys depend on the HMI device.

> **Note**
>
> The function key has a local or global action assigned to it. If the function key also has a hotkey assigned to it, then the hotkey function will be executed in Runtime.

#### Graphics

When a function key is placed directly next to the display, you can assign a graphic to it to make the function of the function key more clear.

#### Display of assignment

The following table shows which symbols display the assignment of the function keys:

| Function key | Description |
| --- | --- |
| ![Display of assignment](images/6338248715_DV_resource.Stream@PNG-de-DE.png) | Not assigned |
| ![Display of assignment](images/6338082187_DV_resource.Stream@PNG-de-DE.png) | Global assignment |
| ![Display of assignment](images/9041901579_DV_resource.Stream@PNG-de-DE.png) | Assigned locally in the template |
| ![Display of assignment](images/6338090891_DV_resource.Stream@PNG-de-DE.png) | Local assignment |
| ![Display of assignment](images/9041909771_DV_resource.Stream@PNG-de-DE.png) | Local assignment (local assignment of the template overwrites global assignment) |
| ![Display of assignment](images/6338201995_DV_resource.Stream@PNG-de-DE.png) | Local assignment (local assignment overwrites global assignment) |
| ![Display of assignment](images/9042033163_DV_resource.Stream@PNG-de-DE.png) | Local assignment (local assignment overwrites local assignment of the template) |
| ![Display of assignment](images/9042080523_DV_resource.Stream@PNG-de-DE.png) | Local assignment (local assignment overwrites local assignment of the template, which already overwrites global assignment) |
| ![Display of assignment](images/6338257035_DV_resource.Stream@PNG-de-DE.png) | Assigning buttons with screen navigation |

> **Note**
>
> **Basic Panels**
>
> The "Screen Navigation" editor is not available for Basic Panels.

---

**See also**

[Assigning function keys globally (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-function-keys-globally-basic-panels-panels-comfort-panels-rt-advanced)
  
[Local assignment of function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#local-assignment-of-function-keys-basic-panels-panels-comfort-panels-rt-advanced)
  
[Assigning a function to a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-a-function-to-a-function-key-basic-panels-panels-comfort-panels-rt-advanced)
  
[Assigning operator authorization for a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-operator-authorization-for-a-function-key-basic-panels-panels-comfort-panels-rt-advanced)
  
[Assigning a graphic to a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)](#assigning-a-graphic-to-a-function-key-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Using function keys for screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-using-function-keys-for-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)

### Assigning function keys globally (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

You define the global assignment of a function key in the "Global Screen" editor. The global assignment applies to all screens of the set HMI device.

> **Note**
>
> **Availability for specific HMI devices**
>
> Function keys are not available on all HMI devices.

#### Requirement

- You have opened the project.
- The Inspector window is open.

#### Procedure

Proceed as follows to assign a screen-based function to a function key:

1. To open the "Global Screen" editor, double-click "Global Screen" in the "Screen management" group of the Project window.
2. Select the desired function key.

   The properties of the function key are shown in the Inspector window.

   ![Procedure](images/111856430219_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111856430219_DV_resource.Stream@PNG-en-US.png)
3. Under "General", configure a graphic and an operator authorization for the function key.
4. Configure a function list for the required event under "Events".

#### Result

If a local assignment does not overwrite the global assignment, the assignment of the function key changes in all the screens of the set HMI device in accordance with your entry.

---

**See also**

[Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-function-keys-basic-panels-panels-comfort-panels-rt-advanced-1)

### Local assignment of function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

Function keys are assigned globally and locally. A local assignment of the function keys is only valid for the screen or the template in which it was defined. The following local function keys are available:

- Local function keys of a screen

  Different functions are assigned to the function key for each screen. This assignment applies only to the screen in which you have defined the function key.
- Local function keys of a template

  You assign the function keys in a template. The assignment applies to all the screens that are based on this template and are not overwritten by a local assignment in a screen.

A local assignment overwrites the global assignment of a function key.

> **Note**
>
> **Availability for specific HMI devices**
>
> Function keys are not available on all HMI devices.

#### Using existing assignments

The option for using existing assignments is referred to as follows in the Inspector window:

- In a template: "Use global assignment"
- In a screen:

  - Screen based on a template: "Use local template"
  - Screen not based on a template: "Use global assignment"

The "Use local template" option includes the use of the local assignment in the template and the global assignment.

#### Requirement

- You have opened the screen or the template in which you want to assign a function key locally.
- The Inspector window is open.

#### Procedure

Proceed as follows:

1. Select the desired function key in the screen or in the template.

   The properties of the function key are shown in the Inspector window.
2. Click "General" in the Inspector window.

   ![Procedure](images/111856996619_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111856996619_DV_resource.Stream@PNG-en-US.png)
3. Disable the "Use local template" or "Use global assignment" option.
4. Under "General", configure a graphic and an operator authorization for the function key.
5. Configure a function list for the required event under "Events".

#### Result

The function key is assigned the configured function in the screen or in the template.

---

**See also**

[Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-function-keys-basic-panels-panels-comfort-panels-rt-advanced-1)

### Assigning a function to a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

A function key can have two states:

- Pressed: Defined by the "Key pressed" event.
- Released: Defined by the "Release key" event.

Both of these events are configured in the Inspector window of the function key. You can assign any event a function list which contains system functions or scripts. Execution of this function list is event-driven in runtime.

> **Note**
>
> **Availability for specific HMI devices**
>
> Function keys are not available on all HMI devices.

> **Note**
>
> **Basic Panels**
>
> Scripts are not available for Basic Panels.

#### Requirement

To assign the function key a global function:

- The "Global Screen" editor is open.

To assign the function key a local function:

- The screen in which you want to assign a function key is open.

If you want to assign a function key locally in a template:

- The template in which you want to assign a function key is open.
- The Inspector window is open.

#### Procedure

Proceed as follows:

1. Select the function key you want to define.

   The properties of the function key are shown in the Inspector window.
2. Configure the function list for the desired result in the Inspector window under "Properties" in the "General" group.

#### Result

The function list is executed in runtime when the operator presses or releases the function key.

---

**See also**

[Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-function-keys-basic-panels-panels-comfort-panels-rt-advanced-1)

### Assigning operator authorization for a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

In WinCC you can assign a runtime authorization for a function key in runtime. This allows you to restrict access to the function keys to specific persons or operator groups when you configure your project. Only authorized personnel can then change important parameters and settings in runtime.

You configure access protection in order to avoid operator errors and increase plant or machine security.

> **Note**
>
> **HMI device dependency**
>
> Function keys are not available on all HMI devices.

#### Requirement

- The user groups have been defined.

To protect a global function key:

- The "Global Screen" editor is open.

If you want to protect a local function key of a screen or of a template:

- The screen or the template which contains the function key is open.
- The Inspector window is open.

#### Procedure

Follow these steps:

1. Select the relevant function key.

   The properties of the function key are shown in the Inspector window.
2. Click "General" in the inspector window.

   ![Procedure](images/111857652875_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111857652875_DV_resource.Stream@PNG-en-US.png)
3. In the "Authorization" list, select the user group you want to allow runtime access to the function key.

#### Result

The runtime authorization is configured.

---

**See also**

[Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-function-keys-basic-panels-panels-comfort-panels-rt-advanced-1)

### Assigning a graphic to a function key (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

In order to make the function of a key more clear, you can insert a graphic in the screen alongside the function key. Graphics can only be assigned to function keys that border the screen margin of the HMI device.

> **Note**
>
> **HMI device dependency**
>
> Function keys are not available on all HMI devices.

> **Note**
>
> **Assigning graphics to a function key**
>
> A graphic can only be assigned to a function key if the bottom edge of the permanent window does not conceal the area of the function key graphic.

#### Requirement

To assign a graphic to a global function key:

- The "Global Screen" editor is open.

If you want to assign a graphic to a local function key in a screen or template:

- The screen or the template that contains the corresponding function key is open.
- The Inspector window is open.
- You have created the graphic for the function key.

#### Procedure

Follow these steps:

1. Select the relevant function key.

   The properties of the function key are shown in the Inspector window.
2. Click "General" in the inspector window.

   ![Procedure](images/111858348939_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111858348939_DV_resource.Stream@PNG-en-US.png)
3. Click in the "Graphic" area of the list.

   The graphic browser of your WinCC project appears. The pane on the left side shows the external graphics which are stored in the browser. The pane on the right side shows you a preview of the graphic you have selected in the browser.

   ![Procedure](images/61041575179_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61041575179_DV_resource.Stream@PNG-en-US.png)

   Using the ![Procedure](images/6338638731_DV_resource.Stream@PNG-de-DE.png) and ![Procedure](images/6338400011_DV_resource.Stream@PNG-de-DE.png) icons, you can display the collection either in form of thumbnails or as a list.

   In order to open and edit OLE objects with the associated graphics program, double-click on the object.
4. In the browser click the desired graphic or store the relevant graphic in the graphic browser.

   The graphic preview is shown in the right pane.
5. Click "Select" to add the graphic to the screen.

   Click "Clear" to remove the graphic from the screen.

#### Result

The graphic is displayed next to the function key.

---

**See also**

[Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-function-keys-basic-panels-panels-comfort-panels-rt-advanced-1)

### Configuring LED tags (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Requirements

- An HMI device with key operation has been created.
- You have created an LED tag.
- The global screen is open.

#### Procedure

1. Click an F-key of the HMI device.
2. In the Inspector window, click "Properties > Properties > General".

   ![Procedure](images/66938705803_DV_resource.Stream@PNG-en-US.PNG)

   ![Procedure](images/66938705803_DV_resource.Stream@PNG-en-US.PNG)
3. Select a tag under "LED tag" in the "General > Settings" area.
4. Under "Bit" enter the correct bit number.

   The correct bit number depends on the HMI device and the input and output assignments on the HMI device.

---

**See also**

[Assignment of inputs and outputs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#assignment-of-inputs-and-outputs-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Assignment of inputs and outputs (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#assignment-of-inputs-and-outputs-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)

### Example: Using function keys for screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Task

In this example you create a local function key in a screen. When the operator presses this function key, a screen change to a predefined screen is triggered, for example "Boiler 2".

> **Note**
>
> **Availability for specific HMI devices**
>
> Function keys are not available on all HMI devices.

#### Requirement

- The screen in which you want to assign the function key is open.
- You have created the "Boiler 2" screen.
- The Inspector window is open.

#### Procedure

Proceed as follows to use the "ActivateScreen" function:

1. Select the desired function key.

   The properties of the function key are shown in the Inspector window.
2. Click "General."
3. To overwrite a global assignment, disable the "Use local template" option.
4. Click "Key pressed" under "Events".

   ![Procedure](images/111858915851_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111858915851_DV_resource.Stream@PNG-en-US.png)
5. Select the "ActivateScreen" system function from the list.

   The "ActivateScreen" function appears in the "Function list" dialog box, including the "Screen name" and "Object number" parameters.

   ![Procedure](images/111858920331_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111858920331_DV_resource.Stream@PNG-en-US.png)
6. Select the "Boiler 2" screen from the "Screen name" list.

#### Result

The operator changes to the "Boiler 2" screen in runtime by pressing the selected function key.

---

**See also**

[Working with function keys (Basic Panels, Panels, Comfort Panels, RT Advanced)](#working-with-function-keys-basic-panels-panels-comfort-panels-rt-advanced-1)

## Working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Moving objects on layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-objects-on-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Setting the active layer (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-active-layer-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Showing and hiding layers (Basic Panels, Panels, Comfort Panels, RT Advanced)](#showing-and-hiding-layers-basic-panels-panels-comfort-panels-rt-advanced)
- [Showing and hiding layers (RT Professional)](#showing-and-hiding-layers-rt-professional)
- [Hiding layers and objects in Runtime (RT Professional)](#hiding-layers-and-objects-in-runtime-rt-professional)
- [Renaming layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#renaming-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Layers

Use layers in order to achieve differentiated editing of the objects in a screen. A screen consists of 32 layers that you can give any names. If you assign objects to the layers, you thereby define the screen depth. Objects of layer 0 are located at the screen background, while objects of layer 31 are located in the foreground.

![Layers](images/61117699595_DV_resource.Stream@PNG-en-US.png)

The objects of a single layer are also arranged hierarchically. When you create a screen, the object inserted first is located at the rear within the layer. Each further object is placed one position towards the front. You can shift objects forwards and backwards within a layer.

#### Principle of the layer technique

Always one layer of the 32 layers is active. New objects you add to the screen are always assigned to the active layer. The number of the active level is displayed in the inspector window of the screen and in the "Layout > Layers" task card.

When you open a screen, all 32 layers of the screen are displayed. You can hide all the layers except for the active layer in the inspector window of the screen and in the "Layout > Layers" task card. You then explicitly edit objects of the active layer.

In the tree view of the "Layers" palette in the "Layout" task card, you administer layers and objects with drag-and-drop and the context menu.

#### Application examples

Use layers, for example, in the following cases:

- To hide the labeling of objects when editing,
- To hide objects, e.g. alarm windows, while configuring other objects

#### Restrictions on the objects in RT Professional

Some controls in WinCC RT Professional appear in a separate window in Runtime.

The following controls are displayed in Runtime regardless of the levels:

- Table view
- F(x) trend view
- F(t) trend view
- Value table
- Recipe view
- Alarm view
- .Net control
- HTML browser
- Screen window

The assignment of these controls to certain levels has no effect in Runtime.

---

**See also**

[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Moving objects on layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-objects-on-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Setting the active layer (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-the-active-layer-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Showing and hiding layers (Basic Panels, Panels, Comfort Panels, RT Advanced)](#showing-and-hiding-layers-basic-panels-panels-comfort-panels-rt-advanced)
  
[Showing and hiding layers (RT Professional)](#showing-and-hiding-layers-rt-professional)
  
[Hiding layers and objects in Runtime (RT Professional)](#hiding-layers-and-objects-in-runtime-rt-professional)
  
[Renaming layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#renaming-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Moving objects on layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

By default, a new object is inserted on the active layer. You can, however, assign an object to another layer at a later time.

#### Requirement

- A screen with an object is open.
- The Inspector window is open.

#### Procedure

1. Select the object in the screen.

   The object properties are displayed in the Inspector window.
2. Enter the layer to which you want to move the object in "Properties > Properties > Miscellaneous > Layer" in the Inspector window.

Alternatively, select the object from the "Layout" task card and drag it to the required layer.

#### Changing the order of objects

1. Select the object in the screen.

   The object properties are displayed in the Inspector window.
2. To move the object to the front or back, select the "Order" > "Move backward" or "Move forward" command from the shortcut menu.

   Alternatively, use the ![Changing the order of objects](images/14156860427_DV_resource.Stream@PNG-de-DE.png) or ![Changing the order of objects](images/14157072907_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.

#### Result

The object is assigned to the selected layer, and positioned at the top of the layer.

---

**See also**

[Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Setting the active layer (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The screen objects are always assigned to one of the 32 layers. There is always an active layer in the screen. New objects you add to the screen are always assigned to the active layer.

The number of the active layer is indicated in the "Layer" toolbar. The active layer is indicated by the ![Introduction](images/61118622091_DV_resource.Stream@PNG-de-DE.png) icon in the "Layout > Layers" task card.

Layer 0 is the active layer when you start programming. You can activate a different layer during configuration, if necessary.

#### Requirement

- You have opened a screen which contains at least one object.
- The Inspector window of the active screen is open.

#### Procedure

1. Click "Properties > Properties > Layers" in the Inspector window of the current screen.
2. Enter the layer number in "Settings > Active layer".

#### Alternative procedure

1. Select "Layout > Layers" in the "Layout" task card.
2. Select the "Set to active" command from the shortcut menu of a layer.

#### Result

The layer with the specified number is now active.

---

**See also**

[Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Showing and hiding layers (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

You can show or hide the layers of a screen as required. You specify the layers that are shown in the Engineering System. When you open a screen, all the layers are always shown.

![Introduction](images/61118795275_DV_resource.Stream@PNG-en-US.png)

#### Requirement

- The screen is opened.
- The "Layout" task card is open.

#### Procedure

1. Select the layer that you want to hide or show in the "Layout > Layers" task card.
2. Click one of the icons next to the corresponding layer:

   - ![Procedure](images/14157090443_DV_resource.Stream@PNG-de-DE.png) A shown layer is hidden
   - ![Procedure](images/14157145227_DV_resource.Stream@PNG-de-DE.png) A hidden layer is shown

**Note**

The active layer cannot be hidden.

#### Alternative procedure

1. Click in an area of the screen that does not contain an object.

   The screen properties are shown in the Inspector window.
2. In the Inspector window, select "Properties > Properties > Layers":

   ![Alternative procedure](images/61118800011_DV_resource.Stream@PNG-en-US.png)

   ![Alternative procedure](images/61118800011_DV_resource.Stream@PNG-en-US.png)
3. In the list, disable the levels you wish to hide.

   If you activate "All ES layers" for a layer, the objects in this layer will be shown in the Engineering System.

#### Result

The layers are shown according to your settings.

---

**See also**

[Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Showing and hiding layers (RT Professional)

#### Introduction

You can show or hide the layers of a screen as required. You define whether the layers are displayed in the engineering system, and/or in Runtime. When you open a screen, all the layers are always shown.

![Introduction](images/87671528715_DV_resource.Stream@PNG-en-US.png)

#### Requirement

- The screen is opened.

#### Procedure

1. In the Inspector window, select "Properties > Properties > Layers":
2. Deactivate the layers that are not to be displayed in the Engineering System.
3. Deactivate the layers that are not to be displayed in runtime.

Alternatively you can also activate and deactivate the layers in the "Layer" task card.

#### Result

The activated layers are displayed in ES and in Runtime.

---

**See also**

[Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Hiding layers and objects in Runtime (RT Professional)

#### Introduction

Layers and the objects stored in them can be shown and hidden in Runtime system-dependently depending on the zoom factor. This means, for example, that a layer is only shown if a sufficient zoom factor allows the required detail to also be displayed.

You can hide or show objects depending on the defined pixel size.

#### Requirement

A screen is open.

#### Hiding layers

1. Click in an area of the screen that does not contain an object.
2. Activate "Properties > Properties > Hide/Show > Activate for layers" in the Inspector window.

   ![Hiding layers](images/87677404683_DV_resource.Stream@PNG-en-US.png)

   ![Hiding layers](images/87677404683_DV_resource.Stream@PNG-en-US.png)
3. In the table enter the minimum and the maximum value for the zoom factor within which the respective layer is displayed.

#### Hiding objects

1. Click in an area of the screen that does not contain an object.
2. Activate "Properties > Properties > Hide/Show > Activate for layers" in the Inspector window.

   ![Hiding objects](images/87677444747_DV_resource.Stream@PNG-en-US.png)

   ![Hiding objects](images/87677444747_DV_resource.Stream@PNG-en-US.png)
3. Enter the minimum size in which the objects are displayed under "Min. pixels."
4. Enter the maximum size in which the objects are displayed under "Max. pixels."

#### Result

Levels which are outside the zoom factor are not displayed in Runtime. Objects which are outside the specified size are also not displayed.

---

**See also**

[Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Supported gestures (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supported-gestures-rt-professional)

### Renaming layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

When you create a screen, the 32 layers are numbered consecutively by default. To improve clarity, you can rename the layers to suit your requirements.

#### Requirement

- The screen is opened.

#### Procedure

1. Click in an area of the screen that does not contain an object.

   The screen properties are shown in the Inspector window.
2. In the Inspector window, select "Properties > Properties > Layers".

   ![Procedure](images/61118795275_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61118795275_DV_resource.Stream@PNG-en-US.png)
3. Enter the new layer name.

   ![Procedure](images/61120467979_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61120467979_DV_resource.Stream@PNG-en-US.png)

#### Result

The layer is displayed with the new name.

---

**See also**

[Basics on working with layers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-working-with-layers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Working with faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-faceplates-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating and managing faceplate types
  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-and-managing-faceplate-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamizing faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-faceplates-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Creating and dynamizing faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-and-dynamizing-faceplates-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basics on faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
- [Device dependency of faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
- [Faceplate editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#faceplate-editor-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics on faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Faceplates are a configured group of display and operating objects that you manage and change centrally in a library. You can use a faceplate in several projects as required. The faceplates are stored in the project library.

##### Use

You use faceplates to create individually configured display and operating objects. You can use faceplates several times in the project or in different projects. All instances of a faceplate in the project are changed centrally. This reduces the configuration effort.

##### Types and instances

Faceplates are based on a type-instance model to support the central changeability. You create central properties for an object in types. The instances represent local points of use of the types.

- Faceplate type

  You create a display and operating object according to your requirements and store it in the project library. The instances are bound to the respective faceplate type. If you change a property of a faceplate type, the property is saved centrally and also changed in all instances. In the faceplate type, you define the properties that can be changed on the faceplate. You edit a faceplate type in the "Faceplates" editor.
- Faceplate

  The faceplate is an instance of the faceplate type. You use a faceplate in screens as a display and operating object. You configure the variable properties of the faceplate type on the instance. You assign the tags of your project to the faceplate, for example. If you configure properties on the faceplate, you overwrite the properties of the faceplate type. The changes on the faceplate are saved at the point of use and have no effect on the faceplate type. To reset the variable properties at the faceplate to the properties of the faceplate type, select "Reset instance" in the shortcut menu.

The figure below shows the relationships between the faceplate type and the faceplate. The background color of the I/O field is configured in the faceplate type in such a way that every instance can change the property. Blue is used as the background color in the faceplate type. You use yellow as the background color in the faceplate.

![Types and instances](images/24014214923_DV_resource.Stream@PNG-de-DE.png)

When you change the background color in the faceplate type, this has no effect on the faceplate because the "Background color" property is assigned on an instance-specific basis.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Faceplate editor (Panels, Comfort Panels, RT Advanced, RT Professional)](#faceplate-editor-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics of dynamizing faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-dynamizing-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Device dependency of faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Device dependency of faceplates

Not all HMI devices support every display and operating object. The screen objects that are not available in the respective HMI device are not displayed when using the faceplate.

Independent of the device, all properties are offered for the configuration during the generation of faceplates. When using a faceplate in a screen, only the properties supported by the configured device are available.

The following devices support faceplates:

##### Runtimes

- WinCC Runtime Advanced
- WinCC Runtime Professional

##### Comfort Panels

- KTP 400
- KP 400
- TP 700
- KP 700
- TP 900
- KP 900
- TP 1200
- KP 1200
- TP 1500
- KP 1500
- TP 1900
- TP 2200

##### Mobile Panels

- Mobile Panel 277
- Mobile Panel 277 IWLAN V2
- Mobile Panel 277F IWLAN V2
- Mobile Panel 277F IWLAN (RFID Tag)
- Mobile Panel KTP 400F
- Mobile Panel KTP 700
- Mobile Panels KTP 700F
- Mobile Panel KTP 900
- Mobile Panel KTP 900F

#### Faceplate editor (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Open

Create faceplate types and edit them in the library view.

##### Layout

The library view for faceplate types consists of several editors, e.g. "Screens" and "Tags" which are arranged in the work area and the configuration area.

![Layout](images/74853582987_DV_resource.Stream@PNG-en-US.png)

##### Work area

In the work area, place the objects contained in the faceplate type as you usually do in the "Screens" editor. You can remove objects, or use the "Toolbox" task card to add new objects.

> **Note**
>
> Faceplates cannot be rotated or mirrored.

##### Configuration section

- Properties

  The static and dynamic properties are identified as follows:

  - The ![Configuration section](images/24020562443_DV_resource.Stream@PNG-de-DE.png) symbol identifies a dynamic property. Dynamic implementation of this property, using tags or text and graphic lists.
  - The ![Configuration section](images/53523137163_DV_resource.Stream@PNG-de-DE.png) symbol identifies a static property. You change only the values of a static property.

    > **Note**
    >
    > **Device dependency of static properties**
    >
    > Static properties are only available for panels and RT Advanced.

  You define the faceplate type properties in the "Properties" tab.

  You use the following two lists for this:

  - The "Contained objects" list

    This list includes the properties of the objects contained in the faceplate type. These properties can only be configured in the faceplate type in the "Faceplate" editor.
  - The "Interface" list contains the properties and tags of the faceplate type. The "Interface" list consists of the pre-defined category "Dynamic properties" and user-defined categories.
- Events

  You define the faceplate type events in the "Events" tab. You use the following two lists for this:

  - The "Contained objects" list contains the events of the objects embedded in the faceplate type.
  - The "Interface" list contains the events of the faceplate.

    You create links between the two lists using a drag and drop operation.
- Tags

  You can also create faceplate tags on the "Tags" tab. The tags are only available within the faceplate type. You can interconnect the faceplate type tags directly with an object contained in the faceplate type.
- Scripts

  You configure scripts for the faceplate type in the "Scripts" tab. In the script, you can call system functions or program new functions to convert values, for example. The scripts are only available within the faceplate type. They work with VB Script code.

  > **Note**
  >
  > The "Scripts" tab is not available for Runtime Professional.
- Text lists

  You can also create and edit texts lists for the faceplate type in the "Text lists" tab. These text lists are only available within the faceplate type. You can interconnect the text lists of the faceplate type directly with an object contained in the faceplate type, such as a symbolic I/O field.

- Graphic lists

  If necessary, you can also create graphics lists for the faceplate type in the "Graphics lists" tab. These graphic lists are only available within the faceplate type. You can interconnect the graphic lists of the faceplate type directly with an object contained in the faceplate type, e.g. a graphic I/O field.

- User texts

  The "User text" tab shows the contained user text of the opened faceplate type, for example entries from text lists. You can enter the compilations for the individual project languages directly in the "User text" tab.

---

**See also**

[Basics on faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Creating and managing faceplate types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Editing the category and property of a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-the-category-and-property-of-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring a tag in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-tag-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring scripts in the faceplate type (Panels, Comfort Panels, RT Advanced)](#configuring-scripts-in-the-faceplate-type-panels-comfort-panels-rt-advanced)
- [Configuring an event in the faceplate type (Panels, Comfort Panels, RT Advanced)](#configuring-an-event-in-the-faceplate-type-panels-comfort-panels-rt-advanced)
- [Configuring an event in the faceplate type (RT Professional)](#configuring-an-event-in-the-faceplate-type-rt-professional)
- [Configuring a text list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-text-list-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring a graphics list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-graphics-list-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Translating texts directly in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-directly-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Exporting and importing texts in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-and-importing-texts-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Editing a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Resizing a faceplate (Panels, Comfort Panels, RT Advanced)](#resizing-a-faceplate-panels-comfort-panels-rt-advanced)
- [Resizing a faceplate (RT Professional)](#resizing-a-faceplate-rt-professional)
- [Creating an instance of the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-instance-of-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Removing faceplate from faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#removing-faceplate-from-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Faceplate types are display and operating objects which are made up of several objects, e.g. controller modules.

##### Requirements

You have opened a screen which contains multiple objects.

##### Procedure in the project view

1. Select all the objects that you need for the faceplate type.
2. Select the "Create faceplate type" command in the shortcut menu of the multiple selection.

   A dialog opens.
3. Enter a name for the faceplate.
4. If necessary, add a comment or change the version number.

**Result**

The library view opens. Two versions of the type are displayed in the "types" folder. Version 0.0.1 has been released and contains the currently selected objects.

The 0.0.2 version has the status "in progress". Edit the faceplate type in version 0.0.2 as required.

##### Procedure in the library view

1. The library view is open.
2. Select the "Add new type" command in the shortcut menu of the project library. A dialog opens.
3. Select the runtime for which the faceplate type is to be available. An empty faceplate type is created.
4. Drag-and-drop the objects from the "Toolbox" task card to the work area of the faceplate type.

##### Result

The new faceplate type is created and displayed under the selected name in the project library.

The faceplate type is assigned the status "in progress" and the version 0.0.1.

---

**See also**

[Basics on faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Editing the category and property of a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-the-category-and-property-of-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a tag in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-tag-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring scripts in the faceplate type (Panels, Comfort Panels, RT Advanced)](#configuring-scripts-in-the-faceplate-type-panels-comfort-panels-rt-advanced)
  
[Configuring an event in the faceplate type (RT Professional)](#configuring-an-event-in-the-faceplate-type-rt-professional)
  
[Configuring a text list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-text-list-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a graphics list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-graphics-list-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Translating texts directly in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#translating-texts-directly-in-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Editing a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#editing-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Resizing a faceplate (Panels, Comfort Panels, RT Advanced)](#resizing-a-faceplate-panels-comfort-panels-rt-advanced)
  
[Creating an instance of the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-instance-of-the-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Removing faceplate from faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#removing-faceplate-from-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Master copies and types (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20global%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#master-copies-and-types-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring a faceplate type  (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In the configuration area of the "Faceplates" editor you define which properties and process values of the objects contained in the faceplate can be configured in the "Properties" tab.

> **Note**
>
> For tooltip texts configured for objects in the faceplate to be displayed in Runtime, insert the property "Tooltip text" as faceplate property.

> **Note**
>
> Independent of the device, all properties are offered for the configuration during the generation of faceplates. When using a faceplate in a screen, only the properties supported by the configured device are available.

> **Note**
>
> The use of user-defined PLC data types (UDTs) of PLCs S7-300 and S7-400 is not supported. These PLC data types cannot be selected as a faceplate property.

##### Requirements

- The faceplate is generated and is displayed in the "Faceplate" editor.
- The "Properties" tab is open in the configuration area.

##### Procedure

1. To create a new property, click the "Add property" ![Procedure](images/21587149707_DV_resource.Stream@PNG-de-DE.png) button in the interface list.

   A new property is displayed in the "Interface" list.
2. To create a new category, click the "Add category" ![Procedure](images/21587157131_DV_resource.Stream@PNG-de-DE.png) button in the interface list.

   A new category including a new property is displayed in the "Interface" list.
3. Click the name of the property and assign a name, for example, "Color".
4. Select the data type.

   ![Procedure](images/83097688843_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/83097688843_DV_resource.Stream@PNG-en-US.png)

**Note**

**Property names of the faceplates in RT Professional**

Note the following rules when entering property names of the faceplates:

- The name must start with a letter.
- The name can contain alphanumeric characters and the underscore.
- The name may not contain more than 255 characters.
- Do not use any UNICODE characters (for example, Chinese characters).

**Note**

**Using user data types (UDTs) in faceplates in RT Professional**

If an element of a faceplate is assigned as data type of the user data type (UDT), the following rule applies:

The length of the name of a property of the faceplate together with the length of the name of the lower-level element of the "User Data Type" (UDT) data type must not exceed 126 characters.

##### Interim result

You have created a new property.

1. Click an object in the "Contained objects" list.
2. Select a property, e.g. "Appearance > Background color".
3. Move the property from the "Contained objects" list to the desired property in the "Interface" list by drag&drop.

   The connection is displayed as a colored line.

   The system assigns the same data type to the property in the "Interface" list as that of the property in the "Contained objects" list.

   To change the data type, select the data type from the data types of the connected property.
4. Repeat step 3 to connect other properties of the contained properties with the interface.

   ![Interim result](images/61833267723_DV_resource.Stream@PNG-en-US.png)

   ![Interim result](images/61833267723_DV_resource.Stream@PNG-en-US.png)

**Note**

The property from the "Contained objects" list must be in concordance with the data type of the already connected property of the "Interface" list.

##### Deleting a connection

1. Click the connection that you wish to delete.
2. In the shortcut menu select the "Delete" command or use the <DEL> key.

   The connection is deleted.

##### Interconnecting user data types with faceplates

As of V13 SP1, you can use the HMI user data types and the PLC user data types as properties of the faceplates.

You interconnect the HMI user data types and the PLC user data types with the faceplates using interface properties by connecting the faceplates with the structural elements of the interface properties.

To set the HMI user data types and the PLC user data types as properties of the faceplates, follow these steps:

1. Select the user data type in the selection list under "Type".

   ![Interconnecting user data types with faceplates](images/72000632331_DV_resource.Stream@PNG-en-US.png)

   ![Interconnecting user data types with faceplates](images/72000632331_DV_resource.Stream@PNG-en-US.png)
2. In the Inspector window under "Properties > Properties > General", select the interface property of the faceplate in the "Tag" selection list.

   ![Interconnecting user data types with faceplates](images/72012763019_DV_resource.Stream@PNG-en-US.png)

   ![Interconnecting user data types with faceplates](images/72012763019_DV_resource.Stream@PNG-en-US.png)

   The faceplate is interconnected with the user data type.

##### Result

You have created a new property or a new category with a property. You have connected the property of the interface with a property of the contained objects. If you use an instance of the faceplate type in a screen, you configure the properties of the faceplate which you have created in the "Interface" list.

> **Note**
>
> **Device dependency of static properties**
>
> Static properties are only available for panels and RT Advanced. You work with dynamic properties in RT Professional.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Linking user data types with objects (RT Professional)](#linking-user-data-types-with-objects-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Editing the category and property of a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Deleting a property in the "Interface" list

1. Select "Edit faceplate" in the shortcut menu. The "Faceplates" editor is open.
2. Select the property which you want to delete in the "Interface" list.
3. Select "Delete" in the shortcut menu.

The property is deleted from the "Interface" list. Existing connections to the contained objects are deleted. All linked faceplates lose their instance-specific property.

##### Deleting a category in the "Interface" list

1. Select "Edit faceplate" in the shortcut menu. The "Faceplates" editor is open.
2. Select the category which you want to delete in the "Interface" list.
3. Select "Delete" in the shortcut menu.

The category including the properties is deleted from the "Interface" list. Existing connections to the contained objects are deleted. All linked faceplates lose their instance-specific properties.

##### Moving a property to another category

1. Select a property in the "Interface" list.
2. Move the property to a new category by "drag&drop".

You have moved the property to a new category.

##### Changing the data type of a property

1. Select a property in the "Interface" list.
2. Click the second column of the drop-down list.
3. Select a data type.

You have changed the data type of the property in the "Interface" list.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring a tag in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You connect a tag in the faceplate type directly with the properties of the objects contained in the faceplate type. The tags in the faceplate type are a central means of defining dynamic properties in the faceplate type.

The tags of a faceplate type have limited functionality. The "Tags" tab of the configuration area has the same structure as the "Tags" editor.

> **Note**
>
> Use of the "." or "@" character in names of tags in faceplate types is not permitted. Do not use the special characters in the tag names in faceplates.

##### Array elements for faceplates

In the following situations, you may not assign an array element or a multiplex tag that is interconnected with a faceplate to a property of a screen object:

- The property is configured in a faceplate as parameter of a system function.
- System functions or scripts are assigned in the faceplate to events of the property.

##### Requirements

- The library view is open.
- The faceplate type is created and has the "in progress" status.
- The "Tags" tab is open in the configuration area.

##### Procedure

1. Click "Add" in the "HMI tags" table. A new tag is created in the faceplate type.
2. Open "Properties > Events" in the inspector window if necessary. You configure the "Value change" event on the tag for example.
3. In the work area, select the object to which you want to assign this tag, e.g. an I/O field.
4. Select the tag in the inspector window of the I/O field "Properties > Properties > General > Process > Tag".

**Note**

Only tags of the faceplate type are displayed in the object list in the "Faceplates" editor.

##### Result

You have created a tag in the faceplate type. You are using the tag in the faceplate for scripting, for example.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring scripts in the faceplate type (Panels, Comfort Panels, RT Advanced)

##### Introduction

In the configuration area of the "Faceplates" editor you create scripts which you only use within a faceplate type. You can only refer to tags of the faceplate type or properties of the contained objects within the script. The script is used as a copy in the instance of the faceplate type.

##### Requirement

- The library view is open.
- The faceplate type is created and has the "in progress" status.
- Faceplate tags or dynamic properties have been created.

##### Procedure

1. Click the "Scripts" tab in the configuration area of the faceplate.
2. Double click "Faceplate scripts > Add VB script".
3. Write the program code.
4. Press the shortcut keys <CTRL+J> to Include tags of the faceplate type in the script. The object list opens.
5. Click "HMI tags".

   All tags of the faceplate type are displayed in the object list.
6. Select a tag and confirm the selection.
7. Press the shortcut keys <CTRL+J> to use properties of the faceplate type in the script. The object list opens.
8. Click "Properties".

   All dynamic properties of the "Interface" list for the faceplate type are displayed in the object list.

##### Result

You have created a script in the faceplate type. The instance of the faceplate type uses a copy of the script. The script is executed in runtime depending on the configuration.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring an event in the faceplate type (Panels, Comfort Panels, RT Advanced)

##### Introduction

In the configuration area of the "Faceplates" editor you define which events of the objects contained in the faceplate can be configured in the "Events" tab. You configure a function list on the events of the faceplate in the "Screens" editor.

##### Requirement

- The library view is open.
- The faceplate type is created and has the "in progress" status.
- The "Events" tab of the configuration area is open.

##### Procedure

1. Click an object in the "Contained objects" list.
2. Select an event, e.g. "Activate".
3. Move the event from the "Contained objects" list to a new category in the "Interface" list.

   The new event is displayed in the "Interface" list.

   The connection appears as a colored line.

   ![Procedure](images/89577916171_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/89577916171_DV_resource.Stream@PNG-en-US.png)
4. Double-click the event and, if required, change the name of the event.

##### Result

You have created an event in the faceplate type. if you use an instance of the faceplate type, you will only be offered the configured events in the inspector window.

You configure a function list on the event in the faceplate.

![Result](images/65640915979_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring an event in the faceplate type  (RT Professional)

##### Introduction

In the configuration area of the "Faceplates" editor, you can define in the "Events" tab which events of the contained objects can be configured in the faceplate. VB scripts for the events of the faceplate instance are configured in the "Images" editor.

##### Requirement

- The faceplate type is created and is displayed in the "Faceplates" editor.
- The "Events" tab of the configuration area is open.

##### Procedure

1. Click an object in the "Contained objects" list.
2. Select an event, e.g. "Activate".
3. Move the event from the "Contained objects" list to a new category in the "Interface" list.

   The new event is displayed in the "Interface" list.

   The connection appears as a colored line.

   ![Procedure](images/61374046987_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61374046987_DV_resource.Stream@PNG-en-US.png)
4. Double-click the event and, if required, change the name of the event.

##### Result

You have created an event in the faceplate type. If you use a faceplate instance, the events available at the faceplate instance as well as the events assigned at the interface of the faceplate type are offered to you in the Inspector window.

VB scripts for events are configured on the faceplate. If you configure a VB script, you must use SmartTag functions.

![Result](images/171014077835_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring a text list in the faceplate type  (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In a faceplate type, you connect a text list with an object included in the faceplate type. Text is assigned to the values of a tag in a text list. The text list is used, for example, to display a selection list in a symbolic I/O field contained in the faceplate type. The interface between the text list and a tag of the faceplate type is configured at the object that uses the text list.

##### Requirements

- The library view is open.
- The faceplate type is created and has the "in progress" status.
- The "Text list" tab is open in the configuration range.
- A tag has been created in the faceplate type.

##### Procedure

1. Click "Add" in the "Text lists" table. A new text list is created in the faceplate type.
2. Assign a name to the text list that indicates its function.
3. Select the text list type, e.g. "Value/Range" under "Select".
4. Click "Add" in the "Text list entries" table.
5. Define the values or range of values for the text list.
6. Enter a text for every value range which is displayed in Runtime when the tag is within the specified value range.
7. Select an object, e.g. a symbolic I/O field, in the work area of the faceplate type.
8. In the Inspector window of the object, enable "Properties > Properties > General > Label > Text list".
9. Select the "Text list" from the selection list.
10. Select a tag of the faceplate type under "Process > Tag".

##### Result

You have created a text list in the faceplate type. This text list is linked to an object contained in the faceplate type. You have configured a faceplate type tag at the object.

---

**See also**

[Basics on text lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-text-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a text list (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-text-list-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring a graphics list in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In a graphics list, specific graphics are assigned to possible values of a tag. In a faceplate type, you connect a graphics list with an object included in the faceplate type. Graphics are assigned to the values of a tag in a graphics list. For example, the graphics list is used to display a selection list in a graphic I/O field contained in the faceplate type. The interface between the graphics list and a tag of the faceplate type is configured at the object that uses the graphics list.

##### Requirements

- The library view is open.
- The faceplate type is created and has the "in progress" status.
- The "Graphics list" tab is open in the configuration range.
- A tag has been created in the faceplate type.

##### Procedure

1. Click "Add" in the "Graphics lists" table. A new graphics list is created in the faceplate type.
2. Assign a functional name to the graphics list.
3. Select a graphics list type, e.g. "Range (... - ...)", under "Selection".
4. Click "Add" in the "Graphics list entries" table. A new entry is created in the list.
5. Define the values or range of values for the graphics list.
6. Select a graphic for every value or value range which is displayed in runtime when the tag is within the specified value range.
7. Select an object, e.g. a graphic I/O field, in the work area of the faceplate type.
8. Activate "Properties > Properties > General > Contents > Graphics list" in the object's Inspector window.
9. Select the "Graphics list" from the selection list.
10. Select a tag of the faceplate type in "Process > Tag".

##### Result

You have created a graphics list in the faceplate type. This graphics list is linked to an object contained in the faceplate type. You have configured a faceplate type tag at the object.

---

**See also**

[Basic principles of graphics lists (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basic-principles-of-graphics-lists-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating a graphics list (RT Professional)](#creating-a-graphics-list-rt-professional)
  
[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Translating texts directly in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Translating texts

If you use several languages in your project, you can translate individual texts directly. As soon as you change the language of the software user interface, the translated texts are available in the selected language.

> **Note**
>
> When you create a faceplate in the "Text" tab, alarm class texts and alarm texts are automatically created in the tab. These texts are required for the WinCC alarm logging.

##### Requirements

- A project is open.
- You have opened the "Faceplates" editor.
- You have created a faceplate type.
- The faceplate type contains at least one object with text, e.g. a text field.

##### Procedure

Proceed as follows to translate individual texts:

1. Open the "Tasks" task card.
2. Click the ![Procedure](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button under "Languages & Resources > Editing language". The "Project languages" editor opens.
3. Activate at least two project languages.
4. Open the "Texts" tab in the "Faceplates" editor.

   A list with the texts in the project is displayed in the work area. There is a separate column for each project language.

   ![Procedure](images/111859969291_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111859969291_DV_resource.Stream@PNG-en-US.png)
5. Click on the ![Procedure](images/22300349963_DV_resource.Stream@PNG-de-DE.png) button in the toolbar to group identical texts together.
6. To hide texts that do not have a translation, click on the ![Procedure](images/22301968011_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
7. Click on an empty column and enter the translation.

##### Result

You have translated individual texts in the "Texts" tab of the faceplate type. The texts will then be displayed in the runtime language.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Exporting and importing texts in the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Exporting and importing texts

You have the option to export the texts of the faceplates for translation and then to import them back again. An OpenOffice XML file is created for the export that can be edited with Microsoft Excel and other spreadsheet programs. You set the languages available for the export and import in the "Languages" tab. You export and import the text of a faceplate type using the buttons "Export project texts" ![Exporting and importing texts](images/152091872011_DV_resource.Stream@PNG-de-DE.png) and "Import project texts" ![Exporting and importing texts](images/152091879563_DV_resource.Stream@PNG-de-DE.PNG) in the toolbar.

Alternatively, you can export and import the texts of the faceplates using the commands "Export texts" and "Import texts" in the "Library" task card. In this case, the project languages defined for this project are used for the export and import.

##### Requirements

- A project is open.
- You have opened the "Faceplates" editor.
- You have created a faceplate type.
- The faceplate type contains at least one object with text, e.g. a text field.

##### Exporting texts

To export the texts, proceed as follows:

1. Open the faceplate type in the project library.
2. Open the "Texts" tab in the "Faceplates" editor.

   A list with the texts in the project is displayed in the work area. There is a separate column for each project language.

   ![Exporting texts](images/111859969291_DV_resource.Stream@PNG-en-US.png)

   ![Exporting texts](images/111859969291_DV_resource.Stream@PNG-en-US.png)
3. To export the text to an .xslx file, click "Export project texts" ![Exporting texts](images/152091872011_DV_resource.Stream@PNG-de-DE.png).

   The "Export" dialog box opens.
4. Select the source language and the target language in the dialog.
5. Select either the content selected in the current window for export or select the user texts from categories.
6. Enter the name and path for the export file.
7. Click "Export".

   Once the export is successfully concluded, the export file is stored under the specified path.

##### Importing texts

To import the text back into the TIA Portal after editing or translation, follow these steps:

1. Open the faceplate type in the project library.
2. Open the "Texts" tab in the "Faceplates" editor.
3. Click "Import project texts" ![Importing texts](images/152091879563_DV_resource.Stream@PNG-de-DE.PNG) in the toolbar.

   The "Import" dialog box opens.
4. Select the path and name of the import file in the "Select file for import" box.

   If you have made changes to the source language in the export file and would like to overwrite the entries in the project with the changes, select the "Import source language" check box.
5. Click on "Import".

##### Result

You have exported the text of a faceplate for translation and imported it back into the TIA Portal after translation.

#### Editing a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

All faceplate types in the project library have a status. You create a faceplate type in the "in progress" status. You can edit the faceplate types as required in this status. When editing is complete, release the faceplate type.

##### Requirement

- A faceplate type has been created.
- The faceplate type has the version 0.0.1. and the status "in progress".
- The "Library" task card or the library view is open.

##### Enable faceplate type

1. Select version 0.01 of the faceplate type in the project library.
2. Select "Release version" in the shortcut menu.

You have released version 0.0.1 of the faceplate type.

##### Edit faceplate type

1. Select, for example, the released version 0.0.1 of a faceplate type in the project library.
2. Select "Edit faceplate type" in the shortcut menu.

The library view opens. The new version 0.0.2 of the faceplate type has been created.

The faceplate type has the "In progress" status.

##### Restoring the last version of the faceplate type

The last released version of the faceplate type is version 0.0.2.

Edit the faceplate type. A new version 0.0.3 is created and the "in progress" status is assigned to it.

1. Select the faceplate type from the project library.
2. Select "Discard changes and restore type" in the shortcut menu.

All changes to the faceplate type since the last enabling operation are rejected. The faceplate type is enabled again and has the version 0.0.2.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)

#### Resizing a faceplate (Panels, Comfort Panels, RT Advanced)

##### Introduction

In the faceplate type, specify the response of the faceplate when it is resized.

##### Requirements

- A faceplate type has been created.
- You have opened the "Faceplates" editor.
- The Inspector window is open.

##### Specifying the response to resizing

1. Activate "Properties > Properties > Layout > Fit to size > Auto-size".
2. Select the "Fixed aspect ratio" setting, for example.

   This setting retains the aspect ratio when you resize the faceplate.
3. Click the faceplate in the "Libraries" task card.
4. Select "Release version" in the shortcut menu.

##### Result

You have specified how the faceplate responds when its size in a screen is changed. You can change the response for a particular faceplate.

Select a faceplate in the screen. Select the required setting in "Properties > Properties > Layout > Characteristics" in the Inspector window.

#### Resizing a faceplate (RT Professional)

##### Introduction

In the faceplate type, specify the response of the faceplate when it is resized.

##### Requirements

- A faceplate type has been created.
- You have opened the "Faceplates" editor.
- The Inspector window is open.

##### Specifying the response to resizing

1. Activate "Properties > Properties > Layout > Fit to size > Auto-size."
2. Select one of the following options for "Response to resizing":

   - Fixed size

     Specifies that the size of the faceplate is unchangeable.
   - Proportional

     The faceplate is scaled proportionally. The rectangle surrounding the object is not scaled.
   - None

     No restriction on resizing of the faceplate.
   - Original size

     Specifies that the size of the faceplate is unchangeable, but the size of the rectangle surrounding the object can be adapted.
   - Keep aspect ratio

     The size of the faceplate is changeable. The aspect ratio is kept during resizing.
3. Click the faceplate in the "Libraries" task card.
4. Select "Enable faceplate type" in the shortcut menu.

##### Result

You have specified how the faceplate responds when its size in a screen is changed. You can change the response for a particular faceplate.

Select a faceplate in the screen. Select the required setting in "Properties > Properties > Layout > Characteristics" in the Inspector window.

#### Creating an instance of the faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The faceplate type is stored in the project library. If you use the faceplate type in a screen, you create an instance of the faceplate type.

> **Note**
>
> Note that a faceplate is always configured for a particular class of HMI devices. For example, you cannot use a faceplate type that is configured for "RT Professional" in a screen on an "RT Advanced" HMI device.

> **Note**
>
> The number of faceplate instances per screen is not limited. However, you should be aware of the fact that the number of faceplate instances used, or the use of scripts in the faceplate instances, will have an impact on performance.

> **Note**
>
> If you would like to copy a faceplate instance from one project to another project, first copy the faceplate type to the target project, followed by the faceplate instance.

##### Requirement

- A screen is open.
- The "Libraries" task card is opened.
- The project library is open and it contains at least one faceplate type.

  > **Note**
  >
  > Faceplate types are also stored in global libraries. When you add a faceplate type from the global library to the screen, the system automatically saves a copy of it to the project library.
- The Inspector window is open.

##### Procedure

1. Move the desired faceplate type from a library to the screen by drag&drop.

##### Result

You have created an instance of the faceplate type. The instance is given the version number of the most recently released type.

Configure the properties of the faceplate in the Inspector window as required. To dynamize the faceplate, open the interface in the Inspector window.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Removing faceplate from faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Cancel application, to remove specified instances from the update of the faceplate type.

> **Note**
>
> The "Remove faceplate from faceplate type" option is only available for selection if the faceplate type uses more than one screen object.

##### Requirement

- A faceplate type has been created.
- The faceplate must be used in a minimum of one screen.

##### Remove faceplate object from faceplate type.

1. Select a faceplate on the screen.
2. In the shortcut menu, select "Remove faceplate object from faceplate type".

##### Result

The faceplate is converted into a group that is independent of the faceplate type. Modifications of the faceplate type have no effect on this group.

---

**See also**

[Creating a faceplate type (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-a-faceplate-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Dynamizing faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics of dynamizing faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-dynamizing-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
- [Dynamizing faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-faceplates-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics of dynamizing faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

You can dynamically control events and properties of faceplates in two ways:

- Dynamically controlling faceplates

  You configure the events or dynamic properties individually for the application point on the faceplate. To do this, define in the "Faceplates" editor that these properties and events are configurable in the faceplate. To dynamize the faceplates in the "Screens" editor, use the scripts and tags that are created in the project.

  > **Note**
  >
  > **Dynamization of faceplate instances**
  >
  > Events cannot be dynamized at a faceplate instance via a function list or a C script.
  >
  > When using a VB script, you must use SmartTag functions.
- Dynamizing the faceplate type

  You dynamize the objects which are contained in the faceplate type in the "Faceplates" editor. You configure the individual objects as in the "Screens" editor. Tags and scripts are available in the "Faceplates" editor to dynamize properties and events. You do not have access to the tags and scripts of the project within the faceplate.

  Every faceplate created with the faceplate type has the same preconfigured dynamization. You can edit this dynamic control only in the "Faceplates" editor.

  > **Note**
  >
  > **Dynamization of instances of a faceplate type in a group**
  >
  > You are using the instance of a faceplate type in an object group. The properties of the instance are also displayed as properties of the group. Any dynamization with tags, scripts or animations of the group is not displayed in Runtime.

##### Updating faceplates

If you automatically calculate the trigger for scripts on the faceplate type with the "Calculate trigger automatically (recommended)" option, the update cycle of the instances is about 2 seconds and is independent of the picture update cycle configured in the pictures.

##### Animation

WinCC provides preconfigured dynamic control in the "Animations" task card. You use animations to dynamize faceplates and faceplate types.

---

**See also**

[Dynamizing faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics on faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Dynamizing faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You dynamize a faceplate in exactly the same way as you dynamize an object from the "Tools" task card.

You connect the dynamic properties of the faceplate in the "Screens" editior with a tag or a script which supplies values to the property in runtime.

You Include tags and scripts which you have created in the project for the faceplate.

##### Requirements

- A faceplate is inserted in the screen.

##### Procedure

1. Select the faceplate.
2. In the Inspector window, open "Properties > Animation".

   The animations available for the selected object are displayed.
3. Select "Horizontal movement" and click the ![Procedure](images/21534885131_DV_resource.Stream@PNG-de-DE.png) button.

   The parameters of the animation are displayed.

   A transparent copy of the object is shown in the work area, which is connected to the source object by means of an arrow.
4. Select a tag for control of movement.
5. Move the object copy to the relevant destination. The system automatically enters the pixel values of the final position in the Inspector window.
6. Customize the range of values for the tag as required.

##### Result

In Runtime, the object moves in response to every change in value of the tag that is used to control the movement. The direction of movement corresponds to the configured type of movement "horizontal".

---

**See also**

[Basics of dynamizing faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-of-dynamizing-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[SmartTags (Panels, Comfort Panels, RT Advanced)](VBS%20object%20model%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#smarttags-panels-comfort-panels-rt-advanced)
  
[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Example: Creating and dynamizing faceplates (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Creating a faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-a-faceplate-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Configuring a faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Creating a script in the faceplate type (Panels, Comfort Panels, RT Advanced)](#example-creating-a-script-in-the-faceplate-type-panels-comfort-panels-rt-advanced)
- [Example: Creating an instance of the faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-an-instance-of-the-faceplate-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Configuring included objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-included-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In this example you create a faceplate in which you can convert the value of a length measuring system from kilometers into meters. The length in meters is displayed in an output field.

##### Procedures overview

The example is divided into the following steps:

1. Creating a faceplate type
2. Configuring a faceplate type
3. Creating a script in the faceplate type
4. Connecting a script with the contained objects of the faceplate type
5. Creating a faceplate and connecting with a tag

---

**See also**

[Basics on faceplates (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-faceplates-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Creating a faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-a-faceplate-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Creating a script in the faceplate type (Panels, Comfort Panels, RT Advanced)](#example-creating-a-script-in-the-faceplate-type-panels-comfort-panels-rt-advanced)
  
[Example: Creating an instance of the faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-an-instance-of-the-faceplate-type-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring included objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-included-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Creating a faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Task

You create a faceplate type.

##### Requirement

- A screen is open.
- The toolbox window is displayed.

##### Settings

For the example you require objects with the following settings:

| Object | Object name | Properties |
| --- | --- | --- |
| Text field | Label_Meter | Text: Meter |
| I/O field | Output_Meter | Mode: Output |
| Button | KM_to_Meter | Text OFF: Convert |

##### Procedure

1. In the toolbox, click the individual objects and drag&drop the objects into the screen.
2. Set the properties as shown above.
3. Select all objects.
4. Select the "Create faceplate type" command in the shortcut menu of the multiple selection.

   The "Add type" window opens.
5. Enter "KMtoMeter" as type name.

##### Result

The faceplate type appears in the project library under the name "KMtoMeter". The faceplate type is assigned the "in progress" status.

---

**See also**

[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Configuring a faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Job

You create the dynamic property and tag of the faceplate type.

##### Creating a new property

1. Click "Properties" in the configuration area of the faceplate.
2. In the "Interface" list, click the ![Creating a new property](images/61378581515_DV_resource.Stream@PNG-de-DE.png) icon "Add property".

   A new property is added to the "Interface" list.
3. Double click the name of the property and enter "KMToMeter".
4. Click the selection list and select the data type "Int".

   ![Creating a new property](images/89588604043_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new property](images/89588604043_DV_resource.Stream@PNG-en-US.png)

##### Interim result

The "KMToMeter" property is displayed in the "Interface" list. The symbol identifies the dynamic property. The property will be linked to a tag in the next step.

##### Creating a tag in the faceplate type

1. Click "Tags" in the configuration area.
2. Click "Add" in the "HMI tags" table. A new tag is added to the table. The inspector window of the tag is opened.
3. In the Inspector window, select "Properties > Properties > General":
4. Enter "BB_Tag" as the name. Select the "Int" data type.

##### Result

The "KMToMeter" property and the "BB_Tag" of the faceplate type are created in the configuration area of the "Faceplates" editor.

---

**See also**

[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Creating a script in the faceplate type (Panels, Comfort Panels, RT Advanced)

##### Task

You create a script that converts the value of a length measuring system from kilometers to meters.

##### Procedure

1. Click "Scripts > Faceplate scripts" in the configuration area.
2. Double click "Add VB script".
3. Press the shortcut keys <CTRL+J>.

   The object list opens.
4. Click "HMI tags".

   The faceplate tag "BB_Tag" is displayed in the object list.

   ![Procedure](images/72362634123_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72362634123_DV_resource.Stream@PNG-en-US.png)
5. Select the faceplate type tag "BB_Tag". Confirm the selection.
6. Insert an "=" sign.
7. Press the shortcut keys <CTRL+J>. The object list is opened.
8. Click "Properties."

   The dynamic property "KMtoMeter" is displayed in the object list.

   ![Procedure](images/100712093707_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/100712093707_DV_resource.Stream@PNG-en-US.png)
9. Select the "KMToMeter" dynamic property. Confirm the selection.
10. Enter "*1000" at the end of the code. This corresponds to the conversion factor from kilometers to meters.
11. Enter the name "Script_1" under "Properties > Properties > General >Setting > Name" in the Inspector window.

    ![Procedure](images/24023112715_DV_resource.Stream@PNG-en-US.png)

    ![Procedure](images/24023112715_DV_resource.Stream@PNG-en-US.png)

##### Result

The script has been created in the faceplate type. If you use the "KMtoMeter" faceplate type in a screen, you assign a tag to the "KMtoMeter" property. The value of this tag is multiplied by factor 1000 and assigned to the tag of the faceplate type "BB_Tag" as a new value. In this way you supply values to the tags of the faceplate type.

---

**See also**

[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Creating an instance of the faceplate type (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Task

You insert the faceplate type "KMtoMeter" in a screen and assign a tag to the dynamic property "KMtoMeter".

##### Requirement

- The "Screens" editor is open.
- A new screen has been created.

##### Settings

For the example you require a tag with the following settings:

| Name | PLC connection | Type |
| --- | --- | --- |
| Kilometer | No | ULong |

##### Procedure

1. Create the HMI tag "Kilometer" with the settings named above.
2. Open the "project library" in the "Libraries" task card.
3. Move the "KMtoMeter" faceplate type into the screen by drag&drop.
4. Click "Properties > Properties > Interface" in the Inspector window.

   The table shows all the properties which you can dynamize in the faceplate.

   ![Procedure](images/72686371339_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72686371339_DV_resource.Stream@PNG-en-US.png)
5. Click the "Dynamization" column in the "KMtoMeter" line.
6. Select "HMI tag".
7. Click the "..." button.
8. Select the tag "Kilometer" from the object list.
9. Confirm the selection.

##### Result

The dynamic property "KMtoMeter" is linked with the "Kilometer" tag. During runtime the dynamic property is supplied with values of the "Kilometer" tag. The values are multiplied by factor 1000 in the script of the faceplate type and assigned to the tag in the faceplate as a new value.

---

**See also**

[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Example: Configuring included objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Task

You connect the included objects in the faceplate "KMtoMeter" to a faceplate tag and a faceplate script.

You connect the I/O field with the "BB_Var" tag of the faceplate type. You connect the "Click" event for a button to the script "Script_1".

##### Requirement

The faceplate is displayed in the "Faceplates" editor.

##### Interconnecting I/O field with a tag

1. Select the "Output_Meter" I/O field in the faceplate.
2. Connect the I/O field with the faceplate tag "BB_Tag" in the "General > Process > Tag" inspector window.

##### Connecting an event to a faceplate script

1. Select the "KM_to_Meter" button in the faceplate.
2. Select "Script_1" in the inspector window under "Events > Click".

##### Result

The I/O field is connected with the tag of the faceplate type. The button is connected with the script of the faceplate type.

If you click the button of the faceplate during runtime, the script is executed. The value of the tag of the faceplate is output in the I/O field.

---

**See also**

[Example: Configuring a faceplate (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-faceplate-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Configuring screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Screen navigation basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#screen-navigation-basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Menus and toolbars for Runtime Professional (RT Professional)](#menus-and-toolbars-for-runtime-professional-rt-professional)

### Screen navigation basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)
- [Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Assigning screen change to button (Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-screen-change-to-button-panels-comfort-panels-rt-advanced-rt-professional)
- [Assigning screen change to function key (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-screen-change-to-function-key-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Types of navigation for the screen change

For a production process consisting of multiple subprocesses, you will configure multiple screens. You have the following options to enable the operator to switch from one screen to the next in Runtime:

- Assign buttons to screen changes
- Configuring screen changes at local function keys

##### Procedure

Before you create a screen change, define the plant structure and derive from it the screen changes that you want to configure.

Create the start screen under "Runtime Settings > General > Start screen".

---

**See also**

[Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Assigning screen change to button (Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-screen-change-to-button-panels-comfort-panels-rt-advanced-rt-professional)
  
[Assigning screen change to function key (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-screen-change-to-function-key-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of working with menus and toolbars (RT Professional)](#overview-of-working-with-menus-and-toolbars-rt-professional)
  
[Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
  
[Screen basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](#screen-basics-basic-panels-panels-comfort-panels-rt-advanced)

#### Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Types of navigation for the screen change

For a production process consisting of multiple subprocesses, you will configure multiple screens. You have the following options to enable the operator to switch from one screen to the next in Runtime:

- Assign buttons to screen changes

- Configuring a screen change at a menu and toolbars

  > **Note**
  >
  > For some HMI devices, you can alternatively create buttons for the screen change in the permanent area. In this case, the button is incorporated into every screen.

##### Procedure

Before you create a screen change, define the screen hierarchy based on the plant structure and derive from it the screen changes that you want to configure.

Create the start screen under "Runtime Settings > General > Start screen".

---

**See also**

[Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

#### Assigning screen change to button (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Configure a button in the screen to switch between the screens on the HMI device during operation.

> **Note**
>
> If you have set the "Visibility" of animations to "Hidden" in the Inspector window of a screen, this screen cannot be called up in Runtime.

##### Requirements

- You have created the project.
- You have created the "Screen_2" screen.
- "Screen_1" is created.

##### Procedure

1. Double-click "Screen_1" in the project navigation. The screen is displayed in the work area.
2. Move "Screen_2" from the project tree to the open screen by drag&drop.

   A button with the name "Screen_1" is inserted.
3. In the Inspector window, select "Properties > Events > Click".

   The "ActivateScreen" system function is displayed in the "Function list".

   ![Procedure](images/88019840907_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88019840907_DV_resource.Stream@PNG-en-US.png)
4. At the "Object number" attribute, define, if required, the tab sequence number of the object on which the focus is to be set after a screen change. You can also specify a tag that contains the object number.

##### Alternative procedure

1. Move a button from the "Tools" task card to "Screen2" by drag&drop.
2. In the Inspector window, select "Properties > Events > Click".
3. Select the "ActivateScreen" system function.
4. Select "Screen_2" for the "Screen number".

##### Result

The operator goes to "Screen_1 with the button in Runtime. If you have specified an object number, the object with this object number has the focus following a screen change.

---

**See also**

[Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)

#### Assigning screen change to function key (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Configure a screen change function key in the screen to switch between the screens on the HMI device during operation.

> **Note**
>
> If you have set the "Visibility" of animations to "Hidden" in the inspector window of a screen, this screen cannot be called up in Runtime.

##### Requirements

- You have created a project.
- You have created the "Screen_2" screen.
- You have created the "Screen_1" screen.

##### Procedure

1. Double click "Screen_1" in the project tree. The screen is displayed in the work area.
2. Move "Screen_2" from the project tree to a function key, e.g. "F2".

   The configured function key displays a yellow triangle.
3. Click "Properties > Events > Press key" in the inspector window.

   The "ActivateScreen" system function is displayed.

##### Result

The operator goes to the specified "Screen_2" with function key "F2" in Runtime.

---

**See also**

[Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)

### Menus and toolbars for Runtime Professional (RT Professional)

This section contains information on the following topics:

- [Basics (RT Professional)](#basics-rt-professional)
- [Working with menus and toolbars (RT Professional)](#working-with-menus-and-toolbars-rt-professional)
- [Example: Configuring a screen change with toolbars (RT Professional)](#example-configuring-a-screen-change-with-toolbars-rt-professional)

#### Basics (RT Professional)

This section contains information on the following topics:

- [Overview of working with menus and toolbars (RT Professional)](#overview-of-working-with-menus-and-toolbars-rt-professional)
- [Menu basics (RT Professional)](#menu-basics-rt-professional)
- [Configuration (RT Professional)](#configuration-rt-professional)
- ["Menus and Toolbars" editor (RT Professional)](#menus-and-toolbars-editor-rt-professional)

##### Overview of working with menus and toolbars (RT Professional)

###### Introduction

Use the "Menus and Toolbars" editor to configure customized menus and toolbars. The customized menus and toolbars are displayed in all screens of a project and in the screen windows. You connect the menu commands and icons with the local scripts.

###### Application

You use customized menus and toolbars, for example to implement a screen navigation. The customized menus and toolbars are displayed in each screen of a project or in a screen window. You can thus move from any screen to all the screens for which you have configured screen changes at menu entries or icons.

---

**See also**

[Menu basics (RT Professional)](#menu-basics-rt-professional)
  
[Configuration (RT Professional)](#configuration-rt-professional)
  
["Menus and Toolbars" editor (RT Professional)](#menus-and-toolbars-editor-rt-professional)
  
[Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Menu basics (RT Professional)

###### Introduction

A menu is placed at the top margin of each screen beginning on the left. In a configuration file you specify which menu and toolbars are created with this file in screens or screen windows. You can configure one menu line for each configuration file.

###### Menu structure

The configuration options for a menu element depend on the position where the menu is located in the menu structure.

You create the following components for a menu:

- Main menu command

  - Is displayed in the screen.
  - Opens a submenu.
- Menu item

  - Is displayed in the screen when the main menu opens.
  - Executes a defined procedure when clicked.
  - You can enter a parameter (for example a screen name) that is to be passed to the procedure under "Properties > Events."
  - Opens a submenu, if it exists.
- Submenu command

  - Is displayed in the screen when a higher-level menu item is open.
- Separator lines between the menu entries

The following figure shows a typical menu structure with different menu elements:

![Menu structure](images/9118386571_DV_resource.Stream@PNG-en-US.png)

###### Editing options

You have the following options for configuring a menu:

- Adding a new main menu
- Adding a new menu command / submenu command
- Adding a separator line
- Moving a selected menu command to the left
- Moving a selected menu command to the right
- Changing settings in the Inspector window

---

**See also**

[Overview of working with menus and toolbars (RT Professional)](#overview-of-working-with-menus-and-toolbars-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Configuration (RT Professional)

###### Introduction

The menus and toolbars that you have configured are combined in the configuration files. Each configuration file contains a maximum of one menu, but can contain several toolbars. You can create any number of configuration files. A configuration file is selected for the following reasons:

- To add a menu and a toolbar to a screen window
- To add a menu and a toolbar to all the screens of your project
- To exchange the menus and toolbars in Runtime dynamically

###### Configuring a configuration file

You have the following options for configuration a configuration file:

- Assign authorizations

  The elements are automatically disabled if a logged in user does not have the required authorization.
- Hiding or disabling menu entries and icons

  You can also exchange the configuration file, for e.g. in case of user change during runtime, if you save the modified functional scope in a new configuration file.

---

**See also**

[Overview of working with menus and toolbars (RT Professional)](#overview-of-working-with-menus-and-toolbars-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### "Menus and Toolbars" editor (RT Professional)

###### Introduction

Use the "Menus and Toolbars" editor to create, configure and edit customized menus and toolbars. The customized menus and toolbars are combined in the configuration files and are then displayed in all the screens of a project as well as in the screen windows. You connect the menu commands and icons with the local scripts.

###### Layout

The "Menus and Toolbars" editor has three tabs:

- Toolbars
- Menus
- Configurations

  ![Layout](images/61388079371_DV_resource.Stream@PNG-en-US.png)

You open the editor in the project navigation by double-clicking "Screen management > Menus and Toolbars".

###### Work area

The work area is divided into two sections in the "Toolbars" and "Menus" tabs:

- In the table you define the complete toolbar and/or complete menu.
- The lower section offers you a preview of your toolbars or menus. You create and configure the individual icons and/or menu commands and specify the structure, labelling texts and symbolizing graphics.

The "Configurations" tab has an undivided work area that contains the table editor for selecting the corresponding toolbars and the corresponding menus.

###### Inspector window

You configure the menus and toolbars in the Inspector window under "Properties > Properties."

---

**See also**

[Overview of working with menus and toolbars (RT Professional)](#overview-of-working-with-menus-and-toolbars-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

#### Working with menus and toolbars (RT Professional)

This section contains information on the following topics:

- [Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
- [Creating a toolbar (RT Professional)](#creating-a-toolbar-rt-professional)
- [Connecting a menu command or icon to a procedure (RT Professional)](#connecting-a-menu-command-or-icon-to-a-procedure-rt-professional)
- [Creating a configuration file (RT Professional)](#creating-a-configuration-file-rt-professional)
- [Editing menus and toolbars (RT Professional)](#editing-menus-and-toolbars-rt-professional)
- [Configuring menus and toolbars for all the screens (RT Professional)](#configuring-menus-and-toolbars-for-all-the-screens-rt-professional)
- [Configuring menus and toolbars in a screen window (RT Professional)](#configuring-menus-and-toolbars-in-a-screen-window-rt-professional)
- [Adapting menus and toolbars in runtime (RT Professional)](#adapting-menus-and-toolbars-in-runtime-rt-professional)

##### Creating a menu (RT Professional)

###### Introduction

In the "Menus and Toolbars" editor you create a menu with main menu commands and the corresponding menu commands with up to six hierarchy levels. The menu is shown as it is displayed later in the screens or a screen window.

###### Requirement

- The "Menus and Toolbars" editor is open.
- The "Menus" tab is open.

###### Creating a menu

1. Double-click "Add" in the "Menus" table.

   The first main menu command is created in the preview of the menu commands.
2. Change the name of the menu and enter a comment, if appropriate.

###### Creating main menu commands

1. Click in the preview of the menu on the already created main menu command.

   Four yellow stars are displayed around the selection rectangle.

   ![Creating main menu commands](images/21405622795_DV_resource.Stream@PNG-en-US.png)

   ![Creating main menu commands](images/21405622795_DV_resource.Stream@PNG-en-US.png)
2. Click the yellow star to the right of the standard text.

   A further main menu command is created.

   ![Creating main menu commands](images/21405720331_DV_resource.Stream@PNG-en-US.png)

   ![Creating main menu commands](images/21405720331_DV_resource.Stream@PNG-en-US.png)
3. Enter a name under "Properties > Properties > General >Name" in the Inspector window.
4. Enter a label for the main menu command "Properties > Properties > General >Text" in the Inspector window.

   ![Creating main menu commands](images/72558093323_DV_resource.Stream@PNG-en-US.png)

   ![Creating main menu commands](images/72558093323_DV_resource.Stream@PNG-en-US.png)

1. To display the main menu command as visible in Runtime, activate "Properties > Properties > Miscellaneous > Visibility".
2. To define an operator authorization, select an authorization under "Properties > Properties > Security".

###### Creating menu commands

1. Click in the preview on a main menu command.

   Yellow stars are displayed around the selection rectangle.

   ![Creating menu commands](images/21405622795_DV_resource.Stream@PNG-en-US.png)

   ![Creating menu commands](images/21405622795_DV_resource.Stream@PNG-en-US.png)
2. Click the yellow star below the selection rectangle.

   A menu command is created under the main menu command.

   ![Creating menu commands](images/21405727755_DV_resource.Stream@PNG-en-US.png)

   ![Creating menu commands](images/21405727755_DV_resource.Stream@PNG-en-US.png)
3. Configure the menu command in the Inspector window like a main menu command.

**Note**

The authorization, visibility and activation for Runtime can be configured both in the menu as well as in each individual menu command. In the case of differing configurations the following applies: Menu overwrites menu command.

###### Creating submenu commands

1. Click in the preview on a menu command.

   Yellow stars are displayed around the selection rectangle.

   ![Creating submenu commands](images/21405622795_DV_resource.Stream@PNG-en-US.png)

   ![Creating submenu commands](images/21405622795_DV_resource.Stream@PNG-en-US.png)
2. Click the yellow star to the right of the menu command.

   A submenu command is created.

   ![Creating submenu commands](images/21393310987_DV_resource.Stream@PNG-en-US.png)

   ![Creating submenu commands](images/21393310987_DV_resource.Stream@PNG-en-US.png)
3. Configure the submenu command in the Inspector window like a main menu command.

###### Result

The menu is created and can be selected as the menu for a specific configuration file in the "Configurations" tab.

---

**See also**

[Creating a toolbar (RT Professional)](#creating-a-toolbar-rt-professional)
  
[Creating a configuration file (RT Professional)](#creating-a-configuration-file-rt-professional)
  
[Editing menus and toolbars (RT Professional)](#editing-menus-and-toolbars-rt-professional)
  
[Configuring menus and toolbars for all the screens (RT Professional)](#configuring-menus-and-toolbars-for-all-the-screens-rt-professional)
  
[Configuring menus and toolbars in a screen window (RT Professional)](#configuring-menus-and-toolbars-in-a-screen-window-rt-professional)
  
[Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)
  
[Adapting menus and toolbars in runtime (RT Professional)](#adapting-menus-and-toolbars-in-runtime-rt-professional)
  
[Connecting a menu command or icon to a procedure (RT Professional)](#connecting-a-menu-command-or-icon-to-a-procedure-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Creating a toolbar (RT Professional)

###### Introduction

Use the "Menus and Toolbars" editor to create a toolbar with buttons. The toolbar is shown in the preview as it is displayed later in the screens or a screen window.

You can configure any number of toolbars for each configuration. For each toolbar you specify the placement position of the toolbar in the screen. Further, you can also define whether the user should have the option of freely placing the toolbar.

> **Note**
>
> Toolbars are device-specific due to the connected scripts. The functionalities are lost when they are used for a different device.

###### Requirement

- The "Menus and Toolbars" editor is open.
- The tab "Toolbars" is displayed.

###### Creating a toolbar

1. Double-click "Add" in the "Toolbars" table.

   A toolbar is created and has a pre-assigned name given to it.

   A button is created in the preview of the toolbar.
2. Enter a name to the toolbar in the "Name" column.
3. Select one of the following options as "Button type":

   - Text and graphics combined
   - Graphics only
   - Text only
4. Specify the size of the buttons in the "Screen size" column.

###### Adjusting buttons

1. Select the toolbar for which you want to create buttons.
2. Click the already existing button in the preview of the toolbar.

   The button contains a default text and/or a default graphic depending on the type.

   ![Adjusting buttons](images/26074662027_DV_resource.Stream@PNG-en-US.png)

   ![Adjusting buttons](images/26074662027_DV_resource.Stream@PNG-en-US.png)

   The properties are displayed in the Inspector window.

   ![Adjusting buttons](images/72558286731_DV_resource.Stream@PNG-en-US.png)

   ![Adjusting buttons](images/72558286731_DV_resource.Stream@PNG-en-US.png)
3. Enter a name under "Properties > Properties > General" in the Inspector window.
4. Depending on the button type, select a text and/or a graphic for the button design.
5. To display the button as visible in Runtime, activate "Properties > Properties > Miscellaneous > Visibility".
6. To display a tooltip in Runtime, enter a text under "Properties > Properties > Miscellaneous > Tooltip".
7. To define an operator authorization, select an authorization under "Properties > Properties > Security".
8. To insert further buttons, click in the preview of the toolbar on the ![Adjusting buttons](images/21438792203_DV_resource.Stream@PNG-de-DE.png) symbol.

**Note**

The authorization, visibility and activation for Runtime can be configured both in the toolbar as well as in each individual button. The following rule is valid for different configurations: Toolbar overwrites button.

###### Result

A toolbar with the define toolbars has been created and can be selected as the menu for a specific configuration file in the "Configurations" tab.

---

**See also**

[Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Connecting a menu command or icon to a procedure (RT Professional)

###### Introduction

Use the "Menus and Toolbars" editor to configure customized menus and toolbars. The customized menus and toolbars are displayed in all the screens of a project and/or also in a screen window. The individual menu commands and buttons are connected with a function list. Only "Click" is available as an event.

###### Requirement

- A "Screen_1" screen has been created.
- A "Screen_2" screen has been created.
- The "Menus and Toolbars" editor is open.
- A button or menu command is created.

###### Configuring an event with a system function to a button or menu command.

1. Select the button or menu command.
2. In the Inspector window, select "Properties > Events > Click".
3. Select the "ActivateScreen" system function from the function list.
4. Select "Screen_2" as the "Screen name".

   ![Configuring an event with a system function to a button or menu command.](images/88019840907_DV_resource.Stream@PNG-en-US.png)

   ![Configuring an event with a system function to a button or menu command.](images/88019840907_DV_resource.Stream@PNG-en-US.png)

###### Configuring an event to a button or menu command via scripts.

1. Select the button or menu command.
2. In the Inspector window, select "Properties > Events > Click".
3. Click the icon ![Configuring an event to a button or menu command via scripts.](images/26075174539_DV_resource.Stream@PNG-de-DE.png) "VB script" in the toolbar of the Inspector window.
4. Write the required script.

   The "Item" is the object that triggers the event, in this case the button or the menu command. It is specified using the "Name" property in the script.

###### Result

When the operator clicks the button or the menu command, the configured function is executed in Runtime.

---

**See also**

[Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Creating a configuration file (RT Professional)

###### Introduction

Use a configuration file to display menus and/or toolbars in all screens of your project or in a screen window. A configuration file consists of one/no menu and/or any number of toolbars.

###### Requirement

- The "Menus and Toolbars" editor is open.
- The "Configurations" tab is displayed.
- Menus and toolbars are required.

###### Creating a configuration file

1. Double-click "Add" in the "Configurations" table. A configuration file is created.
2. Change the name of the configuration file and enter a comment, if appropriate.
3. Select a name under "Properties > Properties > Menu >Name" in the Inspector window.

   ![Creating a configuration file](images/72558633739_DV_resource.Stream@PNG-en-US.png)

   ![Creating a configuration file](images/72558633739_DV_resource.Stream@PNG-en-US.png)
4. Specify whether the menu is to be activated and visible in Runtime and which authorization is required for operation.
5. Select the toolbars you want to add to the configuration file under "Properties > Properties > Toolbars" in the Inspector window.

   ![Creating a configuration file](images/61392216075_DV_resource.Stream@PNG-en-US.png)

   ![Creating a configuration file](images/61392216075_DV_resource.Stream@PNG-en-US.png)
6. Specify for each selected toolbar whether or not the toolbar is to be activated and visible in Runtime and which authorization is required for operation.
7. You define the alignment for each toolbar in "Properties > Properties > Toolbars" in the Inspector window.

###### Result

The configuration file can be selected in the project for all screens or in a screen window.

---

**See also**

[Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Editing menus and toolbars (RT Professional)

###### Introduction

You edit and change already created menus and toolbars in the work are of the "Menus and Toolbars" editor".

###### Inserting a separation line

1. Open the "Menus" tab or Toolbars" tab.
2. Select the menu command or button in front of which you want to insert a separation line.
3. Click ![Inserting a separation line](images/21438792203_DV_resource.Stream@PNG-de-DE.png).

   A separation line is shown before the selected menu item.

You can alternatively insert separation lines by means of the shortcut menu and the command "Add separator."

###### Moving a menu command / button

1. Open the "Menus" tab or Toolbars" tab.
2. Select the menu command or the button you wish to move.
3. Click one of the symbols ![Moving a menu command / button](images/21441264651_DV_resource.Stream@PNG-de-DE.png) or ![Moving a menu command / button](images/21441273483_DV_resource.Stream@PNG-de-DE.png).

   The menu command or button is moved one place to the left or to the right.

Alternatively, you can move a selected element by dragging and dropping it onto the desired position. A marking displays the selected target position.

###### Showing and hiding menus

1. Open the "Menus" tab.
2. To display all the menu commands, click ![Showing and hiding menus](images/21441193483_DV_resource.Stream@PNG-de-DE.png).
3. To display only the main menu commands, click the ![Showing and hiding menus](images/21441276427_DV_resource.Stream@PNG-de-DE.png) symbol.

   Only the main menu is displayed.

---

**See also**

[Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Configuring menus and toolbars for all the screens (RT Professional)

###### Introduction

In the Runtime settings you can define a configuration file with a user-defined menu and toolbars as standard. The customized menu and toolbars are displayed in each screen at the configured position.

You can use VB Script to load other configuration files in Runtime. For e.g. when another user logs in, you can load a configuration file with modified scope of customized menus and toolbars.

###### Configuring menus and toolbars for all the screens

1. Open the "Runtime settings" editor.
2. Select the configuration file whose menu and toolbars are to be displayed in all the screens of your project under "General > Menus and toolbars."

###### Result

When you activate a project, all customized menus and toolbars will be displayed in all the screens of the project.

---

**See also**

[Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Configuring menus and toolbars in a screen window (RT Professional)

###### Introduction

Independent of the start configuration, you can load, in a screen window, an additional configuration file with customized menus and toolbars.

The customized menus and toolbars of the screen window and the start configuration can thus be displayed in the screen window.

###### Requirement

- You have created a configuration file.
- A screen is open.

###### How to configure menus and toolbars in a screen window

1. Drag-and-drop the "Screen window" object into the screen.
2. In the Inspector window, select the configuration file in "Properties > Properties > General".

###### Result

The customized menus and toolbars are displayed in the screen window during runtime.

---

**See also**

[Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Adapting menus and toolbars in runtime (RT Professional)

###### Introduction

Use the "Menus and Toolbars" editor to configure customized menus and toolbars. The customized menus and toolbars are displayed in all screens of a project and in the screen windows. You connect the menu entries and icons with procedures from the local scripts.

###### Example

You can dynamize the "MT configuration" property in a screen window. It is also possible to change the configuration of the basic screen and the screen window by means of VB script.

The following example shows a procedure in which the configuration file is transferred as a parameter.

Sub ChangeMenuToolbarConfigFile (ByVal strMTConfigFile)

HMIRuntime.MenuToolBarConfig = strMTConfigFile

End Sub

> **Note**
>
> One menu and several toolbars can be configured in every configuration.
>
> You can make individual elements of menus or buttons inactive or invisible. This allows display of an adapted functional scope in various screens by editing the configuration and saving it under a different name.

---

**See also**

[Creating a menu (RT Professional)](#creating-a-menu-rt-professional)
  
[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

#### Example: Configuring a screen change with toolbars (RT Professional)

This section contains information on the following topics:

- [Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)
- [Example: Configuring functions at buttons (RT Professional)](#example-configuring-functions-at-buttons-rt-professional)
- [Example: Creating a configuration file (RT Professional)](#example-creating-a-configuration-file-rt-professional)
- [Example: Configuring a configuration file in the screen window (RT Professional)](#example-configuring-a-configuration-file-in-the-screen-window-rt-professional)

##### Example: Configuring toolbars and buttons (RT Professional)

###### Introduction

Your process is split into six process image partitions. One screen is the start screen that does not have a higher-level screen.

###### Requirement

- The screens of the project have been created.
- The "Menus and Toolbars" editor is open.
- The "Toolbars" tab is opened.

###### Creating a toolbar for a start screen

1. Click "Add" in the "Toolbars" table. An toolbar is created.
2. Enter the name "Screen_Change_Start_Screen" in the column.
3. Select the setting "Combined" as the "Button type".
4. Select the screen size "S48x48".

   ![Creating a toolbar for a start screen](images/61392920587_DV_resource.Stream@PNG-en-US.png)

   ![Creating a toolbar for a start screen](images/61392920587_DV_resource.Stream@PNG-en-US.png)
5. Repeat the procedure: Create a toolbar with a corresponding name for each screen.

###### Creating buttons for a start screen

1. Select the first button and select "Properties > Properties > General" in the Inspector window.

   ![Creating buttons for a start screen](images/72558891147_DV_resource.Stream@PNG-en-US.png)

   ![Creating buttons for a start screen](images/72558891147_DV_resource.Stream@PNG-en-US.png)
2. Enter the text "Screen up" under "Text".
3. Select the graphic "Up_Arrow" under "Graphic".
4. To display the button as visible in Runtime, activate "Properties > Properties > Miscellaneous > Visibility".
5. Enter the text "Changes to parent screen" under "Properties > Properties > Miscellaneous > Tooltip".
6. Click ![Creating buttons for a start screen](images/21438792203_DV_resource.Stream@PNG-de-DE.png) in the preview of the toolbar.

   ![Creating buttons for a start screen](images/26074662027_DV_resource.Stream@PNG-en-US.png)

   ![Creating buttons for a start screen](images/26074662027_DV_resource.Stream@PNG-en-US.png)

   A button is created.
7. Repeat the procedure for all the buttons with the following properties:

   - Button_2: Text: "Screen down"; Graphic: "Down_Arrow".
   - Button_3: Text: "Screen left"; Graphic: "Left_Arrow".
   - Button_4: Text: "Screen right"; Graphic: "Right_Arrow".
   - Button_5: Text: "Start screen"; Graphic: "Home".

###### Result

A specific toolbar is now available for each screen.

###### Further steps

The following steps are still necessary to use the toolbars for the screen change:

- Assigning system functions to buttons
- Inserting toolbars into a configuration file
- Configuring in the screen window

---

**See also**

[Basics on screen navigation (Basic Panels, Panels, Comfort Panels, RT Advanced)](#basics-on-screen-navigation-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Configuring functions at buttons (RT Professional)](#example-configuring-functions-at-buttons-rt-professional)
  
[Example: Creating a configuration file (RT Professional)](#example-creating-a-configuration-file-rt-professional)
  
[Example: Configuring a configuration file in the screen window (RT Professional)](#example-configuring-a-configuration-file-in-the-screen-window-rt-professional)

##### Example: Configuring functions at buttons (RT Professional)

###### Introduction

In order for each button to execute the desired function during a screen change, configure the system functions using the function lists.

###### Requirement

- The toolbars for all the screens have been created.
- Buttons for the corresponding screens have been created for each toolbar.
- The "Menus and Toolbars" editor is open.
- The "Toolbars" tab is opened.

###### Configuring system functions at a button of the toolbar.

1. Open the toolbar for the start screen.
2. Select the first button.
3. In the Inspector window, select "Properties > Events > Click".
4. Select the "ActivateScreen" system function from the function list.
5. Enter the name of the screen to which the change is to take place under "Screen name."
6. Enter "2" under "Object number" as the screen object in the screen to which the change is to take place. The focus is set to the screen object with the tab sequence number "2."
7. Repeat the procedure for all the buttons of this toolbar:

   Always select the screen to be activated with the corresponding button as "Screen name".
8. Repeat the procedure for all the toolbars of the other screens:

**Note**

The object number is defined during the configuration of the tab sequence in the screen. The sequence can be displayed in the screen by selecting the menu command "Edit > Tab sequence > Edit tab sequence".

###### Result

The buttons of all the toolbars are configured with the desired system functions for changing the screen.

###### Further steps

The following steps are still necessary to use the toolbars for the screen change:

- Creating configuration files with toolbars
- Configuring configuration files in the screen window

---

**See also**

[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Example: Creating a configuration file (RT Professional)

###### Introduction

In a configuration you specify which menu and toolbars are created with this file in screens or screen windows.

###### Requirement

- The toolbars for all the screens have been created.
- Buttons are created for every toolbar.
- The "Menus and Toolbars" editor is open.
- The "Configurations" tab is opened.

###### Defining a configuration

1. Click "Add" in the "Configurations" table.

   A new configuration is created.
2. Enter the name "Configuration_Start_Screen" in the "Name" column.
3. Select the toolbar "Toolbar_start_screen" in the "Toolbars" table.
4. Select the setting "Down" under "Alignment".

   The toolbar is displayed in the screen window at the lower margin of the display section.
5. To protect the toolbar with an operator authorization in Runtime, select an authorization.
6. Repeat the procedure for each screen you wish to create:

###### Result

The configuration files for displaying the toolbars of all screen windows have been created.

###### Further steps

The following steps are still necessary to use the toolbars for the screen change:

- Configuring configuration files in the screen window

---

**See also**

[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

##### Example: Configuring a configuration file in the screen window (RT Professional)

###### Introduction

To change from any screen to additional screens, create as many screen windows as you require to represent your complete process in an overview screen. Both the corresponding screen and the associated configuration are configured in each screen window.

###### Requirement

- Screens have been created.
- A configuration file is created for each screen.

###### Configuring a configuration file in a screen window

1. Double-click "Screens > Add Screen" in the project window. A new screen is created.
2. Assign the name "Overview_Screen_Project" to this screen.
3. Drag-and-drop the "Screen window" object into the screen.
4. Enter a name for the title bar under "Properties > Properties > General >Title" in the Inspector window.
5. Select a screen that is displayed in the screen window in the Inspector window under "Properties > Properties > General > Name".
6. Define the configuration under "Properties > Properties > General > Configurations" in the Inspector window.
7. Repeat the procedure for all the screens and configurations.

###### Result

An overview screen with screen windows is created. A screen and a configuration are defined for each screen window.

---

**See also**

[Example: Configuring toolbars and buttons (RT Professional)](#example-configuring-toolbars-and-buttons-rt-professional)

## Display and operating elements (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Objects for Basic Panels (Basic Panels)](#objects-for-basic-panels-basic-panels)
- [Objects for Comfort Panels (Panels, Comfort Panels)](#objects-for-comfort-panels-panels-comfort-panels)
- [Objects for Mobile Panels (Panels, Comfort Panels)](#objects-for-mobile-panels-panels-comfort-panels)
- [Objects for WinCC Runtime Advanced (RT Advanced)](#objects-for-wincc-runtime-advanced-rt-advanced)
- [Objects for WinCC Runtime Professional (RT Professional)](#objects-for-wincc-runtime-professional-rt-professional)

#### Objects for Basic Panels (Basic Panels)

##### Availability of display and operating objects for Basic Panels

Only the objects which can be used for the device you are configuring will be shown in the object window. The following table shows the availability of indicator and operating objects for the Basic Panels.

On devices with the device version earlier than V13, configure simple display objects. On devices with the device version V13 or later, configure table-based display objects.

##### Overview

|  | KP300 Basic  KP400 Basic | KTP400 Basic  KTP600 Basic  KTP1000 Basic  TP1500 Basic | KTP700 Basic PN  KTP900 Basic | KTP700 Basic DP  KTP1200 Basic DP | KTP1200 Basic PN |
| --- | --- | --- | --- | --- | --- |
| Bar | Yes | Yes | Yes | Yes | Yes |
| User view | Yes | Yes | Yes <sup>1)</sup> | Yes <sup>1)</sup> | Yes <sup>1)</sup> |
| Date/time field | Yes | Yes | Yes | Yes | Yes |
| I/O field | Yes | Yes | Yes | Yes | Yes |
| Ellipse | Yes | Yes | Yes | Yes | Yes |
| Graphic view | Yes | Yes | Yes | Yes | Yes |
| Graphic I/O field | Yes | Yes | Yes | Yes | Yes |
| Help indicator | Yes | No | No | No | No |
| HTML browser | No | No | Yes | No | Yes |
| Circle | Yes | Yes | Yes | Yes | Yes |
| Trend view | Yes | Yes | Yes <sup>1)</sup> | Yes <sup>1)</sup> | Yes <sup>1)</sup> |
| Line | Yes | Yes | Yes | Yes | Yes |
| Alarm view  Alarm window | Yes | Yes | Yes <sup>1)</sup> | Yes <sup>1)</sup> | Yes <sup>1)</sup> |
| Alarm indicator | Yes | Yes | Yes | Yes | Yes |
| Rectangle | Yes | Yes | Yes | Yes | Yes |
| Recipe view | Yes | Yes | Yes <sup>1)</sup> | Yes <sup>1)</sup> | Yes <sup>1)</sup> |
| Button | Yes | Yes | Yes | Yes | Yes |
| Switch | Yes | Yes | Yes | Yes | Yes |
| Symbolic I/O field | Yes | Yes | Yes | Yes | Yes |
| System diagnostic view | Yes | Yes | Yes <sup>1)</sup> | Yes <sup>1)</sup> | Yes <sup>1)</sup> |
| Text field | Yes | Yes | Yes | Yes | Yes |

1) The objects are displayed on the panels as table-based objects.

---

**See also**

[Objects for Comfort Panels (Panels, Comfort Panels)](#objects-for-comfort-panels-panels-comfort-panels)
  
[Objects for Mobile Panels (Panels, Comfort Panels)](#objects-for-mobile-panels-panels-comfort-panels)
  
[Objects for WinCC Runtime Advanced (RT Advanced)](#objects-for-wincc-runtime-advanced-rt-advanced)
  
[Objects for WinCC Runtime Professional (RT Professional)](#objects-for-wincc-runtime-professional-rt-professional)

#### Objects for Comfort Panels (Panels, Comfort Panels)

##### Availability of display and operating elements for Comfort Panels

Only the objects which can be used for the device you are configuring will be shown in the object window. The following table shows the availability of indicator and control objects on Comfort Panels.

##### Overview

|  | KP400 Comfort  KTP400 Comfort | KP700 Comfort  TP700 Comfort | KP900 Comfort  TP900 Comfort | KP1200 Comfort  TP1200 Comfort | KP1500 Comfort  TP1500 Comfort | TP1900 Comfort  TP2200 Comfort |
| --- | --- | --- | --- | --- | --- | --- |
| Bar | Yes | Yes | Yes | Yes | Yes | Yes |
| User view | Yes | Yes | Yes | Yes | Yes | Yes |
| Watch table | Yes | Yes | Yes | Yes | Yes | Yes |
| Date/time field | Yes | Yes | Yes | Yes | Yes | Yes |
| I/O field | Yes | Yes | Yes | Yes | Yes | Yes |
| Ellipse | Yes | Yes | Yes | Yes | Yes | Yes |
| f(x) trend view | Yes | Yes | Yes | Yes | Yes | Yes |
| Function key | only on keyboard units |  |  |  |  |  |
| Graphic view | Yes | Yes | Yes | Yes | Yes | Yes |
| Graphic I/O field | Yes | Yes | Yes | Yes | Yes | Yes |
| GRAPH overview | Yes | Yes | Yes | Yes | Yes | Yes |
| Handwheel | No | No | No | No | No | No |
| Help indicator | No | No | No | No | No | No |
| HTML browser | No | Yes | Yes | Yes | Yes | Yes |
| Camera view | Yes | Yes | Yes | Yes | Yes | Yes |
| Circle | Yes | Yes | Yes | Yes | Yes | Yes |
| Criteria analysis view | Yes | Yes | Yes | Yes | Yes | Yes |
| Trend view | Yes | Yes | Yes | Yes | Yes | Yes |
| Charge condition | No | No | No | No | No | No |
| Illuminated pushbutton | No | No | No | No | No | No |
| Line | Yes | Yes | Yes | Yes | Yes | Yes |
| Media Player | Yes | Yes | Yes | Yes | Yes | Yes |
| Alarm view  Alarm window | Yes | Yes | Yes | Yes | Yes | Yes |
| Alarm indicator | Yes | Yes | Yes | Yes | Yes | Yes |
| PDF view | Yes | Yes | Yes | Yes | Yes | Yes |
| PLC code view | No | Yes | Yes | Yes | Yes | Yes |
| Polygon | Yes | Yes | Yes | Yes | Yes | Yes |
| Polyline | Yes | Yes | Yes | Yes | Yes | Yes |
| ProDiag overview | Yes | Yes | Yes | Yes | Yes | Yes |
| Rectangle | Yes | Yes | Yes | Yes | Yes | Yes |
| Recipe view | Yes | Yes | Yes | Yes | Yes | Yes |
| Button | Yes | Yes | Yes | Yes | Yes | Yes |
| Switch | Yes | Yes | Yes | Yes | Yes | Yes |
| Slider | Yes | Yes | Yes | Yes | Yes | Yes |
| Key switch | No | No | No | No | No | No |
| Sm@rtClient view | Yes | Yes | Yes | Yes | Yes | Yes |
| Symbol library | Yes | Yes | Yes | Yes | Yes | Yes |
| Symbolic I/O field | Yes | Yes | Yes | Yes | Yes | Yes |
| System diagnostic view | Yes | Yes | Yes | Yes | Yes | Yes |
| System diagnostics window | Yes | Yes | Yes | Yes | Yes | Yes |
| Text field | Yes | Yes | Yes | Yes | Yes | Yes |
| Clock | Yes | Yes | Yes | Yes | Yes | Yes |
| Effective range signal | No | No | No | No | No | No |
| Effective range name | No | No | No | No | No | No |
| Effective range name (RFID) | No | No | No | No | No | No |
| WLAN reception | No | No | No | No | No | No |
| Gauge | Yes | Yes | Yes | Yes | Yes | Yes |
| Zone name | No | No | No | No | No | No |
| Zone signal | No | No | No | No | No | No |

---

**See also**

[Objects for Basic Panels (Basic Panels)](#objects-for-basic-panels-basic-panels)

#### Objects for Mobile Panels (Panels, Comfort Panels)

##### Availability of display and operating elements for Mobile Panels

Only the objects which can be used for the device you are configuring will be shown in the object window. The following table shows the availability of indicator and control objects for the Mobile Panels.

##### Overview

|  | KTP700 Mobile  KTP700F Mobile  KTP900 Mobile  KTP900F Mobile  TP1000F Mobile | KTP400F Mobile |
| --- | --- | --- |
| Bar | Yes | Yes |
| User view | Yes | Yes |
| Watch table | Yes | Yes |
| Date/time field | Yes | Yes |
| I/O field | Yes | Yes |
| Ellipse | Yes | Yes |
| f(x) trend view | Yes | Yes |
| Function key | Yes | Yes |
| Graphic view | Yes | Yes |
| Graphic I/O field | Yes | Yes |
| GRAPH overview | Yes | Yes |
| Handwheel | No | No |
| Help indicator | No | No |
| HTML browser | Yes | Yes |
| Camera view | Yes | Yes |
| Circle | Yes | Yes |
| Criteria analysis view | Yes | Yes |
| Trend view | Yes | Yes |
| Charge condition | No | No |
| Illuminated pushbutton | Yes <sup>1)</sup> | Yes <sup>1)</sup> |
| Line | Yes | Yes |
| Media Player | No | No |
| Alarm view  Alarm window | Yes | Yes |
| Alarm indicator | Yes | Yes |
| PDF view | Yes | Yes |
| PLC code view | Yes | No |
| Polygon | Yes | Yes |
| Polyline | Yes | Yes |
| ProDiag overview | Yes | Yes |
| Rectangle | Yes | Yes |
| Recipe view | Yes | Yes |
| Button | Yes | Yes |
| Switch | Yes | Yes |
| Slider | Yes | Yes |
| Key switch | Yes <sup>1)</sup> | Yes <sup>1)</sup> |
| Sm@rtClient view | Yes | Yes |
| Symbol library | Yes | Yes |
| Symbolic I/O field | Yes | Yes |
| System diagnostic view | Yes | Yes |
| System diagnostics window | Yes | Yes |
| Text field | Yes | Yes |
| Clock | Yes | Yes |
| WLAN reception | No | No |
| Gauge | Yes | Yes |
| 1) optional operator control |  |  |

---

**See also**

[Objects for Basic Panels (Basic Panels)](#objects-for-basic-panels-basic-panels)

#### Objects for WinCC Runtime Advanced (RT Advanced)

##### Availability of display and operating elements for WinCC Runtime Advanced

Only the objects which can be used for the device you are configuring will be shown in the object window. The following table shows the availability of indicator and control objects for WinCC Runtime Advanced.

##### Overview

|  | WinCC Runtime Advanced |
| --- | --- |
| Bar | Yes |
| User view | Yes |
| Watch table | Yes |
| Date/time field | Yes |
| I/O field | Yes |
| Ellipse | Yes |
| f(x) trend view | Yes |
| Function key | No |
| Graphic view | Yes |
| Graphic I/O field | Yes |
| GRAPH overview | Yes |
| Handwheel | No |
| Help indicator | No |
| HTML browser | Yes |
| Camera view | Yes |
| Circle | Yes |
| Criteria analysis view | Yes |
| Trend view | Yes |
| Charge condition | No |
| Illuminated pushbutton | No |
| Line | Yes |
| Media Player | No |
| Alarm view  Alarm window | Yes |
| Alarm indicator | Yes |
| PDF view | Yes |
| PLC code view | Yes |
| Polygon | Yes |
| Polyline | Yes |
| ProDiag overview | Yes |
| Rectangle | Yes |
| Recipe view | Yes |
| Switch | Yes |
| Button | Yes |
| Slider | Yes |
| Key switch | No |
| Sm@rtClient view | Yes |
| Symbol library | Yes |
| Symbolic I/O field | Yes |
| System diagnostic view | Yes |
| System diagnostics window | Yes |
| Text field | Yes |
| Clock | Yes |
| Effective range signal | No |
| Effective range name | No |
| Effective range name (RFID) | No |
| WLAN reception | No |
| Gauge | Yes |
| Zone name | No |
| Zone signal | No |

---

**See also**

[Objects for Basic Panels (Basic Panels)](#objects-for-basic-panels-basic-panels)
  
[Camera view (Panels, Comfort Panels, RT Advanced)](#camera-view-panels-comfort-panels-rt-advanced)
  
[PDF view (Panels, Comfort Panels, RT Advanced)](#pdf-view-panels-comfort-panels-rt-advanced)

#### Objects for WinCC Runtime Professional (RT Professional)

##### Availability of display and operating objects

Only the objects which can be used for the device you are configuring will be shown in the object window. The following tables show the availability of indicator and operating objects for WinCC Runtime Professional.

##### Overview

WinCC Runtime Professional

|  | WinCC Runtime Professional |
| --- | --- |
| Bar | Yes |
| User view | Yes |
| Watch table | No |
| Screen window | Yes |
| Scroll bar | Yes |
| Date/time field | No |
| Double T-piece | Yes |
| Print job/Script diagnostics | Yes |
| I/O field | Yes |
| Editable text field | Yes |
| Ellipse | Yes |
| Ellipse arc | Yes |
| Ellipse segment | Yes |
| Function key | No |
| f(x) trend view | Yes |
| f(t) trend view | Yes |
| Graphic view | Yes |
| Graphic I/O field | Yes |
| GRAPH overview | Yes |
| HTML browser | Yes |
| Camera view | No |
| Channel diagnostics display | Yes |
| Combo box | Yes |
| Check box | Yes |
| Circle | Yes |
| Circular arc | Yes |
| Circle segment | Yes |
| Criteria analysis view | Yes |
| Trend view | No |
| Charge condition | No |
| Illuminated pushbutton | No |
| Line | Yes |
| List box | Yes |
| Media Player | Yes |
| Alarm view | Yes |
| Alarm indicator | No |
| Option button | Yes |
| PLC code view | Yes |
| Polygon | Yes |
| Polyline | Yes |
| ProDiag overview | Yes |
| Rectangle | Yes |
| Recipe view | Yes |
| Round button | Yes |
| Pipe | Yes |
| Pipe bends | Yes |
| Switch | No |
| Button | Yes |
| Slider | Yes |
| Sm@rtClient view | No |
| Disk space view | Yes |
| Symbol library | Yes |
| Symbolic I/O field | Yes |
| System diagnostic view | Yes |
| System diagnostics window | No |
| Table view | Yes |
| Text field | Yes |
| T piece | Yes |
| Clock | Yes |
| Connector | Yes |
| Value table | Yes |
| Effective range name | No |
| Effective range name (RFID) | No |
| Effective range signal | No |
| WLAN reception | No |
| Gauge | Yes |
| Zone name | No |
| Zone signal | No |

---

**See also**

[Objects for Basic Panels (Basic Panels)](#objects-for-basic-panels-basic-panels)

### Objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Bar (Basic Panels, Panels, Comfort Panels, RT Advanced)](#bar-basic-panels-panels-comfort-panels-rt-advanced)
- [Bar (RT Professional)](#bar-rt-professional)
- [User view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [User view, simple (Basic Panels, Panels, Comfort Panels, RT Advanced)](#user-view-simple-basic-panels-panels-comfort-panels-rt-advanced)
- [User view, advanced (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-view-advanced-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Watch table (Panels, Comfort Panels, RT Advanced)](#watch-table-panels-comfort-panels-rt-advanced)
- [Screen window (RT Professional)](#screen-window-rt-professional)
- [Scroll bar (RT Professional)](#scroll-bar-rt-professional)
- [Date/time field (Basic Panels, Panels, Comfort Panels, RT Advanced)](#datetime-field-basic-panels-panels-comfort-panels-rt-advanced)
- [Double T-piece (RT Professional)](#double-t-piece-rt-professional)
- [Print job/script diagnostics (RT Professional)](#print-jobscript-diagnostics-rt-professional)
- [I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#io-field-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [I/O field: Behavior during operation (RT Professional)](#io-field-behavior-during-operation-rt-professional)
- [I/O field: Format pattern (Panels, Comfort Panels, RT Advanced)](#io-field-format-pattern-panels-comfort-panels-rt-advanced)
- [I/O field: Format (RT Professional)](#io-field-format-rt-professional)
- [Editable text field (RT Professional)](#editable-text-field-rt-professional)
- [Ellipse (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#ellipse-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Elliptical arc (RT Professional)](#elliptical-arc-rt-professional)
- [Ellipse segment (RT Professional)](#ellipse-segment-rt-professional)
- [f(t) trend view (RT Professional)](#ft-trend-view-rt-professional)
- [f(x) trend view (Panels, Comfort Panels, RT Advanced)](#fx-trend-view-panels-comfort-panels-rt-advanced)
- [f(x) trend view (RT Professional)](#fx-trend-view-rt-professional)
- [Graphic view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#graphic-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Graphic I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced)](#graphic-io-field-basic-panels-panels-comfort-panels-rt-advanced)
- [Graphic I/O field (RT Professional)](#graphic-io-field-rt-professional)
- [GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#graph-overview-panels-comfort-panels-rt-advanced-rt-professional)
- [Handwheel (Panels, Comfort Panels)](#handwheel-panels-comfort-panels)
- [Help indicator (Basic Panels)](#help-indicator-basic-panels)
- [HTML browser (Basic Panels, Panels, Comfort Panels, RT Advanced)](#html-browser-basic-panels-panels-comfort-panels-rt-advanced)
- [HTML browser (RT Professional)](#html-browser-rt-professional)
- [Camera view (Panels, Comfort Panels, RT Advanced)](#camera-view-panels-comfort-panels-rt-advanced)
- [Channel diagnostics display (RT Professional)](#channel-diagnostics-display-rt-professional)
- [Combo box (RT Professional)](#combo-box-rt-professional)
- [Check box (RT Professional)](#check-box-rt-professional)
- [Circle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#circle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Circular arc (RT Professional)](#circular-arc-rt-professional)
- [Circle segment (RT Professional)](#circle-segment-rt-professional)
- [Criteria analysis view (Panels, Comfort Panels, RT Advanced, RT Professional)](#criteria-analysis-view-panels-comfort-panels-rt-advanced-rt-professional)
- [Trend view (Basic Panels, Panels, Comfort Panels, RT Advanced)](#trend-view-basic-panels-panels-comfort-panels-rt-advanced)
- [Charge condition (Panels, Comfort Panels)](#charge-condition-panels-comfort-panels)
- [Illuminated pushbutton (Panels, Comfort Panels)](#illuminated-pushbutton-panels-comfort-panels)
- [Line (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#line-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [List box (RT Professional)](#list-box-rt-professional)
- [Media Player (Comfort Panels, RT Professional)](#media-player-comfort-panels-rt-professional)
- [Alarm view (RT Professional)](#alarm-view-rt-professional)
- [Alarm view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
- [Alarm view, simple (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-view-simple-basic-panels-panels-comfort-panels-rt-advanced)
- [Alarm view, advanced (Panels, Comfort Panels, RT Advanced)](#alarm-view-advanced-panels-comfort-panels-rt-advanced)
- [Alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
- [Alarm indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-indicator-basic-panels-panels-comfort-panels-rt-advanced)
- [Option buttons (RT Professional)](#option-buttons-rt-professional)
- [PDF view (Panels, Comfort Panels, RT Advanced)](#pdf-view-panels-comfort-panels-rt-advanced)
- [PLC code view (Panels, Comfort Panels, RT Advanced)](#plc-code-view-panels-comfort-panels-rt-advanced)
- [PLC code view (RT Professional)](#plc-code-view-rt-professional)
- [Polygon (Panels, Comfort Panels, RT Advanced, RT Professional)](#polygon-panels-comfort-panels-rt-advanced-rt-professional)
- [Polyline (Panels, Comfort Panels, RT Advanced, RT Professional)](#polyline-panels-comfort-panels-rt-advanced-rt-professional)
- [ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#prodiag-overview-panels-comfort-panels-rt-advanced-rt-professional)
- [Rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#rectangle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Recipe view (RT Professional)](#recipe-view-rt-professional)
- [Recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-as-of-v13-basic-panels-panels-comfort-panels-rt-advanced)
- [Recipe view, simple (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-simple-basic-panels-panels-comfort-panels-rt-advanced)
- [Recipe view, advanced (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-advanced-basic-panels-panels-comfort-panels-rt-advanced)
- [Round button (RT Professional)](#round-button-rt-professional)
- [Pipe (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#pipe-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Pipe elbow (RT Professional)](#pipe-elbow-rt-professional)
- [Switch (Basic Panels, Panels, Comfort Panels, RT Advanced)](#switch-basic-panels-panels-comfort-panels-rt-advanced)
- [Button (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#button-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Slider (Panels, Comfort Panels, RT Advanced, RT Professional)](#slider-panels-comfort-panels-rt-advanced-rt-professional)
- [Key switch (Panels, Comfort Panels)](#key-switch-panels-comfort-panels)
- [Sm@rtClient view (Panels, Comfort Panels, RT Advanced)](#smrtclient-view-panels-comfort-panels-rt-advanced)
- [Memory space view (RT Professional)](#memory-space-view-rt-professional)
- [Symbol library (Panels, Comfort Panels, RT Advanced, RT Professional)](#symbol-library-panels-comfort-panels-rt-advanced-rt-professional)
- [Symbolic I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced)](#symbolic-io-field-basic-panels-panels-comfort-panels-rt-advanced)
- [Symbolic I/O field (RT Professional)](#symbolic-io-field-rt-professional)
- [System diagnostics view (Basic Panels)](#system-diagnostics-view-basic-panels)
- [System diagnostics view (Panels, Comfort Panels, RT Advanced)](#system-diagnostics-view-panels-comfort-panels-rt-advanced)
- [System diagnostics view (RT Professional)](#system-diagnostics-view-rt-professional)
- [System diagnostics window (Panels, Comfort Panels, RT Advanced)](#system-diagnostics-window-panels-comfort-panels-rt-advanced)
- [Table view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#table-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Text field (Panels, Comfort Panels, RT Advanced, RT Professional)](#text-field-panels-comfort-panels-rt-advanced-rt-professional)
- [T-piece (RT Professional)](#t-piece-rt-professional)
- [Clock (Panels, Comfort Panels, RT Advanced, RT Professional)](#clock-panels-comfort-panels-rt-advanced-rt-professional)
- [Connector (RT Professional)](#connector-rt-professional)
- [Value table (RT Professional)](#value-table-rt-professional)
- [WLAN reception (Panels, Comfort Panels)](#wlan-reception-panels-comfort-panels)
- [Gauge (Panels, Comfort Panels, RT Advanced, RT Professional)](#gauge-panels-comfort-panels-rt-advanced-rt-professional)

#### Bar (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Use

The tags are displayed graphically using the "Bar" object. The bar graph can be labeled with a scale of values.

![Use](images/56746006923_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Color transition: Specifies the change in color display when limit values are exceeded.
- Displaying the limit lines / limit markers: Shows the configured limit as a line or marker.
- Define bar segments: Defines the gradations on the bar scale.
- Define scale gradation: Defines the subdivisions, scale markings and intervals of a bar scale.

##### Color transition

You define how the color change is represented in "Properties > Properties > Appearance" in the Inspector window.

| Color transition | Description |
| --- | --- |
| "Segmented" | If a particular limit was reached, the bar changes color segment by segment. With segment by segment representation, you visualize, for example, which limits are exceeded by the displayed value. |
| "Entire bar" | If a particular limit was reached, the entire bar changes color. |

##### Displaying limit lines and limit markers

You display the configured limit in the bar as a line or marking in Runtime using the "Lines" and "Markings" property:

1. In the Inspector window, select "Properties > Properties > Appearance":
2. Activate "Lines" and "Markings".

##### Define bar segments

Use the "Subdivisions" property to define the number of segments into which the bar is divided by the main gradations on the scale.

Use the "Interval" property to divide the distance between the main gradations. The value appears as the difference in value between two adjacent main gradations:

1. In the Inspector window, select "Properties > Properties > Scales":
2. Activate "Show scale."
3. Select the corresponding value for "Settings > Subdivisions".
4. Select the corresponding value for "Settings > Marks label".
5. Select the corresponding value for "Large interval > Interval".

##### Configuring limits/ranges

You can represent limits and ranges in different colors. Define the colors in the Inspector window.

1. In the Inspector window, select "Properties > Properties > Limits/Ranges".
2. Activate the limits/ranges that are to be displayed in Runtime
3. If necessary, change the default colors for the limits/ranges.

> **Note**
>
> If you select the option "Show ranges of tags", you can display up to five ranges in a slider with values that can be specified via a process tag. You define the values for the ranges with a process tag, which you interconnect with the screen object.
>
> The "Show ranges of tags" option is available for Comfort Panels, KTP Mobile Panels and RT Advanced.

> **Note**
>
> If the "Show ranges of tags" option is enabled, the setting "Color gradient Segmented" under "Properties > Appearance > Bar" has no effect in Runtime.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Bar (RT Professional)

##### Application

The tags are displayed graphically using the "Bar" object. The bar graph can be labeled with a scale of values.

![Application](images/56746006923_DV_resource.Stream@PNG-de-DE.png)

For information about how to define a value range and configure it centrally using a process tag, see "[Configuring ranges](#configuring-ranges-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)".

##### Layout

In the Inspector window, you customize the settings for the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Color transition: Specifies the change in color display when limit values are exceeded.
- Displaying the limit markers: Displays the configured limit value as an arrow.
- Define bar segments: Defines the gradations on the bar scale.
- Define scale gradation: Defines the position of the zero point on a bar scale.

##### Color transition

You define how the color change is represented in "Properties > Properties > Appearance" in the Inspector window.

| Color transition | Description |
| --- | --- |
| "Segmented" | If a particular limit was reached, the bar changes color segment by segment. With segment by segment representation, you visualize, for example, which limits are exceeded by the displayed value. |
| "Entire bar" | If a particular limit was reached, the entire bar changes color. |

##### Displaying the limit markers

You display the configured limit in the bar as an arrow in Runtime using the "Selections" property:

1. In the Inspector window, select "Properties > Properties > Appearance":
2. Activate "Selections".

##### Define bar segments

Use the "Scales" property to define the subdivisions into which the bar is divided by the main gradations on the scale.

Use the "Interval" property to divide the distance between the main gradations. The value appears as the difference in value between two adjacent main gradations:

1. In the Inspector window, select "Properties > Properties > Scales":
2. Enable "Show scale".
3. Enter the corresponding value for "Large interval > Interval".

**Note**

Intervals can only be changed if the "Auto-size" option is disabled.

##### Define scale gradation

Use the "Zero point" property to define the zero point on the bar graph scale. Enter the value as a percentage. The percentage relates to the distance between the end values on the scale. For a value of 0 %, for example, the zero point is represented at the height of the lowest value on the scale. The zero point can also be outside the shown area.

The "Zero point" property is only evaluated if the "Bar scaling" property is set to "Auto-size":

1. In the Inspector window, open "Properties > Properties > Scales"
2. Activate "Auto-size".
3. Enter the required value for "Start values .> Zero point".

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### User view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

The "User view" object is used to set up and administer users and authorizations. The user view is used, for example, to create new users in Runtime and assign them to a user group.

On HMI devices with device version V13 or later, the table-based user view is available for managing users and authorizations.

![Use](images/122143964299_DV_resource.Stream@PNG-en-US.PNG)

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Number of lines: Specifies the maximum number of visible entries.
- Columns moveable: Specifies whether the operator can change the sequence of columns in Runtime.

In addition, you set the borders, the fill pattern and the colors of the table header in the Inspector window.

##### Number of lines

The number of lines in the user view displayed in Runtime is specified in the Inspector window. The setting for the number of lines is only effective if "Fit object to contents" is active.

1. Click "Properties > Properties > View" in the Inspector window.
2. Enter an integer value under "Number of lines".
3. Click "Properties > Properties > Layout" in the Inspector window.
4. Select "Fit object to contents".

##### Columns moveable

The operator can change the sequence of columns in Runtime with the "Columns moveable" property.

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Activate "Columns moveable".

##### Column width

In the Inspector window, you can change the width of columns displayed in Runtime.

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Enter integer values for the column width under "Columns".

**Note**

The "Password" column is a dynamic column which adapts to the outer dimensions of the object so that the object content occupies the entire width. The column width you assign is applied as the minimum size. In a dynamic column, the minimum size is changed; however, the width is displayed dynamically to fill the display.

#### User view, simple (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

The "User view" object is used to set up and administer users and authorizations.

![Application](images/59674871691_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Do not use the user view in a group.

> **Note**
>
> The "Simple user view" object cannot be operated dynamically with a script.

> **Note**
>
> Configure the "Simple user view" object on devices with device version 12.0.0.0 or older.

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Number of lines: Specifies the maximum number of visible entries.

##### Number of lines

The number of lines in the user view displayed in Runtime is specified in the Inspector window. The setting for the number of lines is only effective if the property "Fit object to contents" is active.

1. In the Inspector window, select "Properties > Properties > View".
2. Enter an integer value under "Number of lines".
3. In the Inspector window, activate "Properties > Properties > Layout".
4. Select "Fit object to contents".

##### Display in Runtime

The appearance depends on the authorizations:

- All users on the HMI device are displayed in the User view to the administrator or to a user with administrator authorizations.
- For a user without administrator rights, only the user's own entry is shown.

##### Operation

Depending on the configuration you can:

- Manage users, e.g. create, delete.
- Change existing user data.
- Export or import user data.

  > **Note**
  >
  > The number is limited to 100 users and one PLC user on an HMI device. This restriction does not apply to PCs. On a PC, the maximum number of users is restricted by the physical memory.

#### User view, advanced (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "User view" object is used to set up and administer users and authorizations. The user view is used, for example, to create new users in Runtime and assign them to a user group.

##### Advanced user view

Depending on the HMI devices, the extended or simple user view is available for administration of users and authorizations.

![Advanced user view](images/59674867211_DV_resource.Stream@PNG-en-US.png)

##### Changing the view type

On HMI devices with a display size larger than 6 ", you can configure both the advanced user view and a simplified user view. The view type is only available for configuration on devices up to device version V13.

![Changing the view type](images/59674871691_DV_resource.Stream@PNG-en-US.png)

Proceed as follows to configure the appropriate user view:

1. Click "Properties > Properties > Layout > Mode" in the Inspector window.
2. Select "Simplified" or "Advanced".

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Number of lines: Specifies the maximum number of visible entries.
- Columns moveable: Specifies whether the operator can change the sequence of columns in Runtime.

##### Number of lines

The number of lines in the user view displayed in Runtime is specified in the Inspector window. The setting for the number of lines is only effective if "Fit object to contents" is active.

1. Click "Properties > Properties > View" in the Inspector window.
2. Enter an integer value under "Number of lines".
3. Click "Properties > Properties > Layout" in the Inspector window.
4. Select "Fit object to contents".

##### Columns moveable

The operator can change the sequence of columns in Runtime with the "Columns movable" property.

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Activate "Columns moveable".

This option is only available at the complex user view.

---

**See also**

[User view (Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#user-view-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-users-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Managing users in the complex user view (Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#managing-users-in-the-complex-user-view-panels-comfort-panels-rt-advanced-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Watch table (Panels, Comfort Panels, RT Advanced)

##### Use

The "Watch table" object is used to configure an editor that will allow you to process single address areas of a SIMATIC S7 in runtime.

![Use](images/74907825163_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The "Watch table" object is enabled for the following PLCs:
>
> - SIMATIC S7-300
> - SIMATIC S7-400

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- PLC type: Specifies the PLC type in the object for which the address area is output in runtime.
- Operator controls: Specifies the controls of the object.
- Visible columns: Specifies the displayed columns in Runtime.
- Columns moveable: Specifies whether the operator can change the sequence of columns in Runtime.

##### Operator controls

Set the control elements that you can use to control the "Watch table" object in runtime under "Properties > Properties > Display" in the "Settings" area of the inspector window.

|  | Function |
| --- | --- |
| ![Operator controls](images/6399293323_DV_resource.Stream@PNG-de-DE.png) | This button refreshes the display in the status value column. |
| ![Operator controls](images/6399301643_DV_resource.Stream@PNG-de-DE.png) | Use this button to accept the new value in the control value column. The control value is then written to the PLC. |

##### Visible columns

The columns that are displayed in runtime are specified in the Inspector window in the "General" group in the "Visible columns" area.

| Column | Description |
| --- | --- |
| "Connection" | The PLC of which the address areas are displayed. |
| "Type" "DB number" "Offset" "Bit" | The address area of the operand. |
| "Data type" "Format" | The data type of the operand. |
| "Status value" | The value that was read from the specified address of the operand. |
| "Control value" | The value written to the specified address of the operand. |

##### Sequence of columns

The operator can use the "Column ordering" property to change the sequence of columns in runtime.

1. Select "Properties > Properties > Columns" in the Inspector window.
2. Activate "Properties of columns > Sequence of columns".

##### System functions

Two system functions are available for updating the values in the watch table and transferring the values to the PLC:

- StatusSteuernLeseWerte
- StatusSteuernSchreibeWerte

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Screen window (RT Professional)

##### Application

You use the "Screen window" object to represent other screens from the project in the current screen. You can make the object dynamic to constantly update the content of a screen window, for example. Customized menus and toolbars are used to add specific buttons to the screen window.

You can also use independent screen windows independently of the screen in question. With appropriate hardware equipment and support by the operating system you can also control multiple monitors and map processes in a more comprehensive and differentiated manner.

![Application](images/88034369419_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you can customize the settings for the object position, geometry, style, frame and color. You can adapt the following properties in particular:

- Zoom factor: Defines the size of the embedded screen.
- Screen section: Defines the section of the embedded screen that is displayed in the screen window. If the embedded screen is larger than the screen window, you configure scroll bars for the screen window.
- Independent screen windows: Specified that the screen windows are displayed independently from the screen in which they were configured.

> **Note**
>
> **Cascading screen windows**
>
> Screen windows can also display screens which, in turn, contain screen windows. The ability to display cascaded screen windows in runtime depends on the operating system. In the 32-bit version, 22 cascaded screen windows can be displayed. In the 64-bit version, 14 cascaded screen windows can be displayed.

> **Note**
>
> **Use of controls in cascading screen windows**
>
> The use of controls, e.g. an alarm control in cascading screen windows, can lead to a memory overflow (out of memory) of the browser. The web page can then no longer be displayed.

##### Matching the size of the embedded screen and screen window

You can match the size of the embedded screen to the size of the screen window in the following ways:

- You want the embedded screen to appear smaller.

  Enter the required zoom factor under "Properties > Properties > General" in the Inspector window.
- You want to scroll to a section of the embedded screen.

  In the Inspector window, activate "Properties > Properties > Layout > Scroll bar".

  The user can scroll to details of the embedded screen in Runtime.

  You can move the position of the scroll bar horizontally or vertically under "Properties > Properties > Layout > Scroll bar position" in the Inspector window.
- You can adapt the embedded screen to the size of the screen window, or vice versa.

  Select either "Fit window to screen", or "Fit screen to window" in "Properties > Properties >" in the Inspector window.

  If you select the "Fit window to screen" setting, the size of the screen window is adapted to the embedded screen in Runtime and can no longer be changed in the engineering system.

  Choose between two options in scaling mode for the "Fit screen to window" setting:

  - Uniform: The full embedded screen is displayed in the screen window. If the aspect ratios differ, the screen does not fill the screen window.
  - Fill: The screen fills the screen window. If the aspect ratios differ, parts of the screen are trimmed.

  The aspect ratio is retained with both options.

##### Define screen section

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Enter the values for the horizontal and vertical displacement of the zero point of the screen display under "Offset."

   The desired section is displayed in the screen window.
3. If you want to scroll from the defined section to other areas of the screen, activate "Properties > Properties > Appearance > Scrollbar".

##### Defining independent screen windows

1. Insert a screen window in the start screen.
2. Select the screen that is displayed in the screen window under "Properties > Properties > General > Name".
3. Select "Properties > Properties > General > Independent screen windows".
4. Select "Position and mode":

   - As configured: The screen window is displayed in the configured size and at the configured position.
   - Centered: The screen window is displayed in the configured size in a central position.
   - Maximized: The screen window is adjusted to the monitor size.
5. If you are using multiple monitors select the desired monitor for the screen window under "Monitor number".
6. Repeat steps 1 to 5 for all further independent screen windows.

**Note**

The monitor numbers refer to the number of monitors set in Microsoft Windows: "Control Panel > Display > Settings > Display"

##### Define tag prefix

Define a tag prefix to access structure instances in Runtime. The tag prefix is freely definable but must match the name of the structure instance.

> **Note**
>
> **The dynamic interconnection of tags in runtime**
>
> To interconnect tags dynamically in runtime, use the tag prefix or indirectly addressed tags.
>
> Avoid using both methods at the same time.

1. Click "Properties > Properties > General > Contents" in the Inspector window.
2. Enter one of the created structure instances with a period after the name under "Tag prefix", e.g. "Motor1.".

The "Temperature" tag is requested on an object in the screen window. If a tag prefix "Motor1." is assigned to the screen window, the "Motor1.Temperature" tag is requested.

If the tag prefix for a screen window is set, the tag prefix is prefixed to all tags contained in the screen to be displayed. This also applies when the request is made in a function. If a tag or a tag prefix is to be read, you must prefix "@NOTP::" to the tag name.

> **Note**
>
> **Availability of tag prefixes in indicator and control objects**
>
> The tag prefix property is only available for "slider" and "pointer instrument" objects.
>
> The objects of the "Controls" palette do not support the tag prefix.

> **Note**
>
> If the screen is assigned to a user data type, the "Tag prefix" cannot be edited.

> **Note**
>
> **Do not specify any additional tag prefix in the lower-level screen window**
>
> If a screen window is configured in a referenced screen of a screen window, the tag prefix of the higher-level screen window is used in the lower-level screen window. Do not specify any additional tag prefix in the lower-level screen window, because bundled structure tags are not supported in WinCC. The interpretation "TagPrefix1.TagPrefix2.TagName" cannot be used for dynamizations.

##### Defining a structured process tag

As an alternative to the tag prefix, you can assign the "screen window" object to a structured process tag. In order for a structured process tag to be selected, the user data type must be assigned to the screen in the screen window. This data type must be saved in the project library.

1. Once the screen of the HMI user data type is assigned, you can select a process tag of the HMI user data type from the "Process tag" list.

   Or:

   Once the screen of the PLC user data type is assigned, you can select a process tag that is connected to a PLC tag or a PLC data block.

The selected process tag appears under "Tag prefix" and "Process tag".

> **Note**
>
> The "Process tag" property cannot be made dynamic. Use the "Tag prefix" property to make it dynamic.
>
> The "Process tag" property cannot be addressed by using VB or C scripting. Use the "Tag prefix" property for VB or C scripting.

> **Note**
>
> **Cascading screen windows**
>
> For cascading screen windows, the screen in which you configure the screen window must be assigned a user type. In this case, both a process tag as well as a structural element of the assigned user data type can be selected under "Process tag". In order for the user data type to be selected, it must be available in the project library.

##### Special feature of visibility animation

If you want to animate the visibility of a screen window and the screen window is not to be visible at first, disable the "Visibility" setting under "Properties > Miscellaneous".

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Scroll bar (RT Professional)

##### Application

The "Scroll bar" object is used to control processes. The scroll bar allows you to make stepless changes to values, for example. To incorporate a scroll bar into the process, dynamize the corresponding attribute.

![Application](images/88035386763_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, style and color. You can, in particular, adapt the following properties as required:

- Maximum value and minimum value: Specifies the top and bottom values of the scale.
- Alignment: Defines the horizontal, or vertical alignment.

##### Maximum value and minimum value

You define the top and bottom values of the scale in the Inspector window.

1. In the Inspector window, select "Properties > Properties > General":
2. Enter a number under "Maximum static" and "Minimum static". If you select a tag as the end value of the scale, the number will be no longer available.

##### Define alignment

Define whether the scroll bar is aligned vertically or horizontally in the Inspector window.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Select the required alignment under "Style."

---

**See also**

[Configure operator input alarms (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-operator-input-alarms-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Date/time field  (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Use

The "Date/time field" object shows the system time and the system date. The appearance of the "Date/time field" depends on the language set on the HMI device.

![Use](images/61111956491_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, style, colors and font types of the object. You can adapt the following properties in particular:

- Display system time: Specifies that the system time is displayed.
- Include tag: Specifies that the time of the connected tag is displayed.
- Long date/time format: This setting defines the format displayed for the data and time.

##### Display system time

The time displayed in the "Date/time field" on the HMI device is specified in the Inspector window.

1. In the Inspector window, select "Properties > Properties > General".
2. Select "Format > System time".

##### Using tags

The time of the interconnected tag is displayed in the date/time field.

1. In the Inspector window, select "Properties > Properties > General".
2. In the "Format" area, select a tag with the "DateTime" data type, e.g. an internal tag.

##### Long date/time format

Visualization of the date and time is specified in the "Format" area under "General" in the Inspector window.

| Option | Description |
| --- | --- |
| "Enabled" | Date and time are displayed in full, e.g. "Sunday, December 31, 2000 10:59:59 AM" |
| "Disabled" | Date and time are displayed in short form, e.g. "12/31/2000 10:59:59 AM" |

##### Behavior during operation

If the operator ignores the syntax when entering values or enters invalid values in Runtime, these entries will not be applied. Instead, the original value (plus the time that has elapsed in the meantime) appears in the date/time field and a system event is displayed on the HMI device.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Double T-piece (RT Professional)

##### Application

You use the "Double T-piece" to reproduce a pipe junction. To reproduce a pipe system, connect the "Double T-piece" to other objects, e.g. pipe bend or T piece.

![Application](images/21196071563_DV_resource.Stream@PNG-de-DE.png)

##### Layout

Customize the object position, color and width in the Inspector view.

---

**See also**

[Pipe (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#pipe-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Pipe elbow (RT Professional)](#pipe-elbow-rt-professional)
  
[T-piece (RT Professional)](#t-piece-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Print job/script diagnostics (RT Professional)

##### Application

You use the "Print job/Script diagnostics" object to show content from the "Print jobs" and "Scripts" editors. Information is transferred to the "Print job/Script diagnostics" object in runtime and to enable an operation. Depending on which windows content and which template you use, you can display a preview of the print job, for example.

![Application](images/25441736843_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. You can adapt the following properties in particular:

- Window content: Defines the application that is displayed in the "Print job/Script diagnostics" object.
- Template: Defines the template in which the window content is displayed in the "Print job/Script diagnostics" object.

##### Templates for using functions

The following templates are available for functions:

- GSC diagnostics

  The "Print job/Script diagnostics" object is supplied by applications of the functions. It displays the results from the diagnostic system.

##### Templates for using print jobs

The following templates are available for the "Print jobs" window content:

- All print jobs

  The "Print job/Script diagnostics" object is supplied by the print jobs. The available print jobs are shown as a list.
- Shortcut menu for all jobs

  The "Print job/Script diagnostics" object is supplied by the print jobs. The available print jobs are shown as a list. A shortcut menu offers the following actions:

  - Print preview
  - Print report
- Jobs detailed view

  The "Print job/Script diagnostics" object is supplied by the print jobs. There is a menu for selecting the available print jobs. Detailed information is displayed for the selected print job.
- Shortcut menu for selected jobs.

  The "Print job/Script diagnostics" object is supplied by the print jobs. The available print jobs are shown as a list.

  To display print jobs in the list, select "Properties > Properties > General > Display print job/script diagnostics in Control" in the Print Job editor. A shortcut menu offers the following actions:

  - Print preview
  - Print report

##### Configure window content

You define the window content of the object in the Inspector window.

1. In the Inspector window, select "Properties > Properties > General".
2. Select the window content, e.g. "Print jobs".

##### Configure template

You define the template for the window content of the object in the Inspector window:

1. In the Inspector window, select "Properties > Properties > General".
2. Select a template

   ![Configure template](images/61246207627_DV_resource.Stream@PNG-en-US.png)

   ![Configure template](images/61246207627_DV_resource.Stream@PNG-en-US.png)

##### Window layout in Runtime

In runtime, the "Print Job/Script Diagnostics" object appears as a standalone window within a process picture. Use the attributes under "Window display" to customize the window layout features.

![Window layout in Runtime](images/61246301707_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "I/O field" object is used to enter and display process values.

![Application](images/58080827147_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Mode: Specifies the response of the object in Runtime.
- Display format: Specifies the display format in the I/O field for input and output of values.
- Hidden input: Specifies whether the input value is displayed normally or encrypted during input.

  > **Note**
  >
  > **Reports**
  >
  > In reports, I/O fields only output data. "Output" mode is preset. Properties for configuring input are not available, e.g. "hidden input".

##### Mode

The response of the I/O field is specified in the Inspector window in "Properties > Properties > General > Type".

| Mode | Description |
| --- | --- |
| "Input" | Values can only be input into the I/O field in Runtime. |
| "Input/output" | Values can be input and output in the I/O field in Runtime. |
| "Output" | The I/O field is used for the output of values only. |

##### Display format

The display format for the input and output of values is specified in "Properties > Properties > General > Format" in the Inspector window.

| Display format |  |
| --- | --- |
| "Binary" | Input and output of values in binary form |
| "Date" | Input and output of date information. The format depends on the language setting on the HMI device. |
| "Date/time" | Input and output of date and time information. The format depends on the language setting on the HMI device. |
| "Decimal" | Input and output of values in decimal form |
| "Hexadecimal" | Input and output of values in hexadecimal form |
| "Time" | Input and output of times. The format depends on the language setting on the HMI device. |
| "String" | Input and output of character strings. |

> **Note**
>
> **Data formats**
>
> Not all data formats are available for selection for Runtime Professional.

##### Connection to Char data type

If you connect the I/O field to a controller tag of data type "Char", the following restrictions apply:

- The input accepts only digits: 0 … 9.

  The entered string of digits is converted to the corresponding character according to the ASCII table.

  Example: Input 6 + 5 becomes "A".
- Only enter digit sequences between 0 and 129.

To input alphanumeric characters directly, use the alternative data type "WChar", for example.

##### Hidden input

In runtime the input can be displayed normally or encrypted, for example for hidden input of a password. A "*" is displayed for every character during hidden input. The data format of the value entered cannot be recognized.

1. In the Inspector window, select "Properties > Properties > Characteristics":
2. Select "Hidden input".

##### Avoid overlaps in output fields

If several I/O fields are configured as output fields with a transparent background in a screen, these I/O fields may overlap. The transparent part of the one field covers the digits of the other field. This may cause display problems in Runtime. In order to avoid such overlaps, set the borders of the I/O fields to zero in the object properties under "Properties > Properties > Appearance". Select "Properties > Properties > Layout > Fit object to contents."

##### Limits

Under "Properties > Properties > Limits" in the Inspector window, set the colors for the values that violate the high or low limits.  
You define the limits via the properties of a tag. In Runtime Professional you can specify if the colors should be used.

When there is a limit violation during Runtime, the background color of the I/O field changes according to your configuration, even if the I/O field is in "Input" mode.

In Runtime Professional, you can also define the limit range for the entry in the I/O field via "Properties > Properties > Limits".

If you enter a numeric value outside this limit, it is not applied; for example, 80 with a limit of 78. In this case, the HMI device generates a system event, if an alarm window is configured. The original value is displayed again.

##### Decimal places for numerical values

The configuration engineer can define the number of decimal places for a numerical input field. The number of decimal places is checked when you enter a value in this type of I/O field. Decimal places in excess of the limit are ignored. Empty decimal places are filled with "0".

##### Behavior when switching between input fields

When you change to another input field within the same screen, and the screen keyboard appears, the "Exit field" event is not executed for the previous field unless you close the screen keyboard.

---

**See also**

[Configure operator input alarms (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-operator-input-alarms-rt-professional)
  
[I/O field: Format pattern (Panels, Comfort Panels, RT Advanced)](#io-field-format-pattern-panels-comfort-panels-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### I/O field: Behavior during operation (RT Professional)

##### Introduction

In WinCC Runtime Professional, you can configure the window display of the "I/O field" object via the properties in the Inspector window.

##### Behavior during operation

**Apply value on completed entry**

The "Apply value on completed entry" attribute specifies when an input value is to be applied. If the attribute has the value "No", then the input value is applied when the input is confirmed with <ENTER> . Otherwise the input value is automatically applied as soon as the preset number of characters has been entered.

**Apply value on exit**

By means of the "Apply value on exit" property, the application of a value can also be enabled for the case where the I/O field is exited without prior confirmation or reaching the required number of characters.

**Clear on invalid input**

The "Clear on invalid input" property can be used to prevent application of an incorrect input value when the field is exited. For example, an input value that does not correspond to the predefined data format of the input field is incorrect.

**Clear on focus**

The "Clear on focus" property specifies whether the field contents are to be cleared when the input field is selected.

**Cursor control**

Specifies a value at which the alpha cursor automatically jumps to the next field in the TAB sequence after an input is made.

**Edit on enable**

The "Edit on enable" attribute specifies for input fields whether or not an immediate change into input mode occurs when the object takes focus.

**Hidden input**

The "Hidden input" attribute specifies whether the input value is displayed during input as normal or encrypted. If this attribute has the value "Yes", every character input is replaced with the "*" character. The value entered and the data format of the value cannot be recognized.

#### I/O field: Format pattern (Panels, Comfort Panels, RT Advanced)

##### Introduction

Four different display formats are available for the input and output of values in an I/O field. Numerical values can be edited in binary, decimal or hexadecimal format. The "String" display format must be specified for the I/O field to display text.

Various format patterns can be selected or freely defined based on the display format.   
The definition for a format can be rewritten as a sequence of formatting codes. The formatting codes act as placeholders for a specific group of characters. For example, if a formatting code for which only the display of the numbers 0-9 is preset for a specific position in the display of an I/O field, only letters can be input at this position.

In addition to the numerical values in an I/O field, you can also output character strings and date/time. To output a character string, use a tag of the data type "String" with a maximum field length of 320 characters. To display date/time formats, use tags with the "Date/time" data type. The display of date/time depends on the language setting on the HMI device in runtime.

##### Formatting codes - "Binary" data format

| Symbol | Meaning |
| --- | --- |
| 1 | Placeholder for the binary values 0 and 1. The number of formatting code "1" specifies the number of digits allowed for the display of a binary value. |

Example: The eight-digit binary value 10011101 can be displayed as follows:

| Format | Permissible number of digits | Display |
| --- | --- | --- |
| 1111111111 | 8 | 10011101 |

Additional formatting options depend on the data types of the tags used, e.g. in the data type Int, the formatting is "11111111 11111111".

##### Formatting codes - "Decimal" data format

| Symbol | Meaning |
| --- | --- |
| 9 | Placeholder for the numbers 0 to 9. The number of formatting code "9" specifies the number of digits allowed for the display of a decimal value and can also be used for negative values with the prefix "-". If the actual number of decimal places exceeds the number specified in the display format, the displayed value is rounded. |
| , | A period defines the location of the decimal point. The formatting code "." may be used at any point in the format, but it can only be used once. Decimals are only supported for floating-point data types. If you want to display a tag value of fixed-point data types, select the option "Decimal places" for the implicit conversion of the values. |
| s | Positive decimal numbers are displayed with a sign. The formatting code "s" should be in the first place of the output format and may only be used once. |
| e | The decimal number is displayed in exponent notation. The formatting code "e" should be in the last place of the output format and may only be used once. |

Example: The six-digit floating-point number 123.456 can be displayed as follows:

| Format | Permissible number of digits | Display |
| --- | --- | --- |
| 999 | 3 | 123 |
| 999.9 | 4 | 123.5 |
| s999.9 | 4 + sign | +123.5 |
| 999,999 | 6 | 123.456 |
| 9999.9999 | 8<sup>1)</sup> | 0123.4560 |
| s9999.9999 | 8 + sign<sup>1)</sup> | +0123.4560 |
| 9.99999e | 6 | 1.23456e+002<sup>2)</sup> |

<sup>1)</sup> To do this, activate the option "Leading zeros"

<sup>2)</sup> This display is only possible in an I/O field in output mode

##### I/O field with "decimal" display format and format pattern without "s" prefix

You have linked a process tag to an I/O field. The I/O field is assigned the "decimal" display format. You can select a format without a sign as a format pattern.

##### Formatting codes - "Hexadecimal" data format

The six-digit fixed-point number 123456 can be displayed as follows:

| Format | Number of digits | Display |
| --- | --- | --- |
| FFFFFFFF | 8 | 0001E240 |

Additional formatting options depend on the data types of the tags used, e.g. in the data type Int, the formatting is "FFFF".

---

**See also**

[I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#io-field-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### I/O field: Format (RT Professional)

##### Introduction

Four different display formats are available in WinCC Runtime Professional for the input and output of values in an I/O field. Numerical values can be edited in binary, decimal or hexadecimal format. The "String" display format must be specified for the I/O field to display text.

Various format patterns can be selected or freely defined based on the display format.   
The definition for a format can be rewritten as a sequence of formatting codes. The formatting codes act as placeholders for a specific group of characters. For example, if a formatting code for which only the display of the numbers 0-9 is preset for a specific position in the display of an I/O field, only letters can be input at this position.

> **Note**
>
> If the value you want to display does not correspond exactly to the definition of the format, only three asterisks are displayed. This applies for the length of the entire character string and also for the type and position of the individual characters.

##### Formatting codes - "Binary" data format

| Symbol | Meaning |
| --- | --- |
| 1 | Placeholder for the binary values 0 and 1. The number of formatting code "1" specifies the number of digits allowed for the display of a binary value. |
| 0 | If needed, the binary value is preceded by a leading zero. The format can also begin with the format code "0", but it can only include it once. |

Example: The eight-digit binary value 10011101 can be displayed as follows:

| Format | Permissible number of digits | Display |
| --- | --- | --- |
| 11 | 2 | 01 |
| 011 | 2 + leading zero | 001 |
| 1111 | 4 | 1101 |
| 01111 | 4 + leading zero | 01101 |
| 1111111 | 7 | 0011101 |
| 01111111 | 7 + leading zero | 00011101 |
| 1111111111 | 10 | 10011101 |
| 01111111111 | 10 + leading zero | 010011101 |

##### Formatting codes - "Decimal" data format

| Symbol | Meaning |
| --- | --- |
| 9 | Placeholder for the numbers 0 to 9. The number of formatting code "1" specifies the number of digits allowed for the display of a decimal value. If the actual number of decimal places exceeds the number specified in the display format, the displayed value is rounded. |
| , | A period defines the location of the decimal point. The formatting code "." may be used at any point in the format, but it can only be used once. |
| s | Positive decimal numbers are displayed with a sign. The formatting code "s" should be in the first place of the output format and may only be used once. |
| 0 | Leading and trailing zeros are displayed, when the actual number of integer or decimal places is less than the specified number in the display format. The formatting code "0" must be before the first "9" and may only be used once. |
| e | The decimal number is displayed in exponent notation. The formatting code "e" should be in the last place of the output format and may only be used once. |

Example: The six-digit decimal value 123.456 can be displayed as follows:

| Format | Permissible number of digits | Display |
| --- | --- | --- |
| 999 | 3 | 124 |
| 999.9 | 4 | 123.5 |
| s999.9 | 4 + sign | +123.5 |
| 999,999 | 6 | 123.456 |
| 09999.9999 | 8 +  zeros | 0123.4560 |
| s09999.9999 | 8 + sign + zeros | +0123.4560 |
| 1111111111 | 10 | 10011101 |
| 9.99999e | 6 | 1.23456e+002 |

> **Note**
>
> When storing a floating-point number in IEEE format of S5, a format for display in an IO field should be used that provides for the sign and exponent (e.g. s0999.999e).

##### I/O field with "decimal" display format and format pattern without "s" prefix

You have linked a process tag to an I/O field. The I/O field is assigned the "decimal" display format. You may select a signed or an unsigned display format.

A "Format pattern" setting without "s", e.g., "999" has the following effects:

1. You cannot set negative values using the I/O field in Runtime.
2. If the tag assumes a negative value, the I/O field generates a two's complement and a corrupted positive value is output.

##### Formatting codes - "Hexadecimal" data format

| Symbol | Meaning |
| --- | --- |
| f | Placeholder for the letters A to F or a to f and numbers 0 to 9, which are used to represent hexadecimal numbers. The permitted number of characters is defined by the number of the formatting codes "f" in the output format. |
| 0 | Leading zeros of the hexadecimal value are displayed if the output format begins with the format code "0". The formatting code "0" may only be included once. |

Example: The eight-digit binary value ABCDEF01 can be displayed as follows:

| Format | Permissible number of digits | Display |
| --- | --- | --- |
| ff | 2 | 01 |
| 0ff | 2 + leading zero | 001 |
| ffff | 4 | EF01 |
| 0ffff | 4 + leading zero | 0EF01 |
| ffffffffff | 10 | ABCDEF01 |
| 0ffffffffff | 7 + leading zero | 0ABCDEF01 |

##### Formatting codes - "String" data format

The exact length of a character string is defined by the number of formatting codes used (exception "*").

| Symbol | Meaning |
| --- | --- |
| * | Input of a character string of any length |
| ? | Input of any character string |
| a | Lower-case letters, upper-case letters and digits are allowed no separators or similar. |
| A | Upper-case letters and digits are allowed no lower-case letters, separators or similar. |
| b | Lower-case letters and upper-case letters are allowed no digits, separators or similar. |
| B | Only upper-case letters are allowed no lower-case letters, digits, separators or similar. |
| 1-9 | The formatting codes "1", "2", ..., "9" are used as placeholders for digits. The selected formatting code also defines the actual digits allowed: For example, if the "2" is specified, only the digits 0, 1 or 2 can be displayed. The formatting code "8" allows all digits except for the 9. |
| h | Only the digits 0 to 9 and the letters A to F or a to f are allowed. The formatting code "h" allows only characters that are required to display hexadecimal numbers. |
| t | The formatting code "t" forces input of a separator at the specified position. These separators are valid: Slash, colon, comma, period and space. |

#### Editable text field (RT Professional)

##### Application

The "Editable text field" object enables you to display several lines of text in a rectangle on the screen. If the text is larger than the rectangle, WinCC automatically adds a scroll bar to the right margin.

If you allow operation, the operator can edit the text in runtime. You can use the multiple-line text for the input or output of text by connecting tags.

![Application](images/56786403723_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, style, colors and font types of the object. You can adapt the following properties in particular:

- Text: Defines the text for the "Editable text field".

##### Text

The text for the "Editable text field" is defined in the inspector window.

1. Click "Properties > Properties > General" in the inspector window.
2. Enter a text of any length.

   For texts over several lines you can set a line break by pressing <Enter>, with the key combination <Shift + Enter> or the key combination <Ctrl + Enter>.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Ellipse (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Ellipse" is an enclosed object that can be filled with a color or pattern.

![Application](images/58080857739_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you can customize the settings for the object position, geometry, style, frame and color. You can adapt the following properties in particular:

- Horizontal radius: Specifies the horizontal radius of the elliptical object.
- Vertical radius: Specifies the vertical radius of the elliptical object.

##### Horizontal radius

The horizontal radius of the "Ellipse" object is specified in the Inspector window. The value is entered in pixels.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value between 0 and 2500 under "Horizontal."

##### Vertical radius

The vertical radius of the "Ellipse" object is specified in the Inspector window. The value is entered in pixels.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value between 0 and 2500 at "Vertical."

---

**See also**

[Elliptical arc (RT Professional)](#elliptical-arc-rt-professional)
  
[Ellipse segment (RT Professional)](#ellipse-segment-rt-professional)
  
[Rotating objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#rotating-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Flipping objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#flipping-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Elliptical arc  (RT Professional)

##### Application

The "Elliptical arc" is an open object. Use the "Ellipse segment" object if you want to fill the object with color. By default, an elliptical arc is a quarter ellipse. It can be customized as required.

![Application](images/2701797643_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you can customize the settings for the object position, geometry, style, frame and color. You can adapt the following properties in particular:

- Horizontal and vertical radii: Specifies the horizontal and vertical radius of the elliptical object.
- Start and end angle: Specify where the start and end angle lie on a virtual circle of 360°.

##### Defining radii

Define the horizontal and vertical radius of the "Elliptical arc" object in the Inspector window. Enter the values using Pixels as the unit.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value for "Horizontal radius" and "Vertical radius".

##### Define start and end angle

Determine the length of the elliptical arc using the "Start Angle" and "End Angle" attributes. Enter the values using Degrees as the unit.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value for "Angle start" and "Angle end".

##### Alternative procedure

You can also change the start and end points of the elliptical arc using the mouse.

1. Place the cursor on a start or end point of the elliptical arc. The start and end points are indicated by small blue squares.

   The mouse cursor changes to a cross.
2. Hold down the mouse button, and drag the start or end point to the desired position.

---

**See also**

[Ellipse (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#ellipse-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Ellipse segment (RT Professional)

##### Application

The "Ellipse segment" is a closed object that you can fill with a color or pattern. By default, an ellipse segment is a quarter ellipse. It can be customized as required.

![Application](images/2701042187_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. You can adapt the following properties in particular:

- Horizontal and vertical radii: Specifies the horizontal and vertical radius of the elliptical object.
- Start and end angle: Specify where the start and end point lie on a virtual circle of 360°.

##### Defining radii

Define the horizontal and vertical radius of the "Ellipse segment" object in the Inspector window. Enter the values using Pixels as the unit:

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value for "Horizontal radius" and "Vertical radius" in the "Arc" area.

##### Define start and end angle

Determine the size of the ellipse segment using the "Start Angle" and "End Angle" attributes. Enter the values using Degrees as the unit:

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value for "Start angle" and "End angle" in the "Arc" area.

##### Alternative procedure

You can also change the start and end points of the ellipse segment using the mouse.

1. Place the cursor on a start or end point of the ellipse segment. The start and end points are indicated by small blue squares.

   The mouse cursor changes to a cross.
2. Hold down the mouse button, and drag the start or end point to the desired position.

---

**See also**

[Ellipse (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#ellipse-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### f(t) trend view (RT Professional)

##### Use

You use the "f(t) trend view" object to display tag values from the current process, or from the log in the form of trends as a function of the time.

![Use](images/88041429899_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, colors and font types of the object. You can adapt the following properties in particular:

- Adding and configuring trends
- Configuring a diagram
- Window settings
- Persistence
- Toolbar

##### Configuring trends

1. Select the data supply for the trend under "Properties > Properties > Trends > Data source".

   - "Log tags": The trend view is supplied with values from a data log.
   - "User-defined": The trend view is supplied user-defined in Runtime by means of scripts.
   - "Tags": The trend view is supplied with values of a tag.
2. Under "Data range", define whether the trend displays the values statically or if the values are refreshed.

   - "Automatic": The displayed value range is automatically adapted to the current values.
   - "Initial value / End value": You define the minimum value and maximum value for the value range.
3. Under "Limits", configure the colored marking of specific values, .e.g.. high and low limit.
4. Select "Properties > Properties > Time axis".
5. Configure the "Time range" of the trend display.

   - "Time span": You define the time range using a starting time and a following time span.
   - "End time": You define the time range using a starting time and an end time.
   - "Measuring points": You define the time range using a starting time and a number of measuring points.

##### Configuring a diagram

Configure the display of several trends under "Diagram":

- Common or separate diagrams
- Common or separate axes
- Writing direction of all trends

##### Window settings

Under "Layout > Window", define whether the user can change the size of the window in runtime and can close the window.

##### Persistence

Select "Properties > Properties > Security > Persistence" to specify whether or not a user may edit trend view configuration in Runtime and the retention period of such changes.

- "No persistence"

  The changes to the configuration are not saved. The changes are discarded at the next screen change and when Runtime is closed.
- "Persistence"

  The changes to the configuration are saved. The changes are retained even after Runtime was closed. You may also select "Response at screen change" to discard changes at the screen change.
- "Persistence in Runtime"

  The changes to the configuration are only saved during Runtime. The changes are discarded as soon as you close Runtime. You may also select "Response at screen change" to discard changes at the screen change.

##### Toolbar

You define the operator controls of the f(t) trend view in Runtime under "Properties > Properties > Toolbar" in the Inspector window. The following operator controls are available for the f(t) trend view:

| Button | Name | Function |
| --- | --- | --- |
| ![Toolbar](images/23982571147_DV_resource.Stream@PNG-de-DE.png) | Online help | Opens the online help. |
| ![Toolbar](images/23942155147_DV_resource.Stream@PNG-de-DE.png) | Open configuration | Opens the configuration dialog. |
| ![Toolbar](images/102411264395_DV_resource.Stream@PNG-de-DE.png) | First data record | Scroll in the log:  Shows the trend curve starting with the first logged value. |
| ![Toolbar](images/102411268235_DV_resource.Stream@PNG-de-DE.png) | Previous data record | Scroll in the log:  Shows the trend curve of the previous time interval. |
| ![Toolbar](images/102411284875_DV_resource.Stream@PNG-de-DE.png) | Next data record | Scroll in the log:  Shows the trend curve of the next time interval. |
| ![Toolbar](images/102411288715_DV_resource.Stream@PNG-de-DE.png) | Last data record | Scroll in the log:  Shows the trend curve up to the last logged value. |
| ![Toolbar](images/23942162827_DV_resource.Stream@PNG-de-DE.png) | Show/ hide ruler | Determines the coordinates of a point of the trend. |
| ![Toolbar](images/102270138379_DV_resource.Stream@PNG-de-DE.png) | Zoom area | Increases the size of any section of the trend window. |
| ![Toolbar](images/23980203659_DV_resource.Stream@PNG-de-DE.png) | Original view | Switches from the magnified trend view back to the normal view |
| ![Toolbar](images/23929835147_DV_resource.Stream@PNG-de-DE.png) | Tag selection | Opens the dialog for selecting the log and tags. |
| ![Toolbar](images/25824357899_DV_resource.Stream@PNG-de-DE.png) | Trend selection | Opens the dialog for setting the visibility of trends. |
| ![Toolbar](images/102411252619_DV_resource.Stream@PNG-de-DE.png) | Time range selection | Opens the dialog for setting the time range displayed in the trend window. |
| ![Toolbar](images/23980641931_DV_resource.Stream@PNG-de-DE.png) | Previous trend | Displays the previous trend in the foreground. |
| ![Toolbar](images/23980803211_DV_resource.Stream@PNG-de-DE.png) | Next trend | Displays the next trend in the foreground. |
| ![Toolbar](images/102411244939_DV_resource.Stream@PNG-de-DE.png) | Start/end update | Stops and starts the trend update. The values are buffered and updated as soon as you start trend update again. |
| ![Toolbar](images/23931759499_DV_resource.Stream@PNG-de-DE.png) | Print log | Starts printing the trends shown in the trend window. You define the print job under "General > Print > Print job". |
| ![Toolbar](images/23932623883_DV_resource.Stream@PNG-de-DE.png) | Selection of the statistics area | Enables you to define a time range for which statistical values are determined. Vertical lines which you use to set the time range are displayed in the trend window. |
| ![Toolbar](images/23932725131_DV_resource.Stream@PNG-de-DE.png) | Statistics window | Opens a statistics window to display the minimum, maximum, means, and standard deviation for the selected time range and the selected trend. |
| ![Toolbar](images/25825901579_DV_resource.Stream@PNG-de-DE.png) | Exporting process data in runtime as a CSV file | Opens the dialog for saving the trend data in CSV format. |

The order of the buttons is fixed. Under "Hotkey" you can set up individual key assignments, and shortcuts for every button on the toolbar.

---

**See also**

[f(x) trend view (RT Professional)](#fx-trend-view-rt-professional)
  
[Table view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#table-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configure trend view (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-trend-view-rt-professional)
  
[Value table (RT Professional)](#value-table-rt-professional)
  
[Configuring persistence (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-persistence-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### f(x) trend view (Panels, Comfort Panels, RT Advanced)

##### Application

You use the "f(x) trend view" object to represent the values of a tag as a function of another tag. This means that you can present temperature trends as a function of the pressure, for example.

![Application](images/89588619275_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, colors and font types of the object. You can adapt the following properties in particular:

- Adding and configuring trends
- Configuring a diagram
- Window settings
- Persistence
- Toolbar

##### Configuring trends

You create and configure trends in the Inspector window "Properties > Properties > Properties > Trend".

1. Select the data supply for the trend in the "Data source" column.

   - "Logging tag": The trend view is supplied with values from a data log.
   - "Tags": The trend view is supplied with current values from the PLC. The values are constantly updated.
2. Configure the area of the trend display under "Data area".

   - "Time span": You define the time range using a starting time and a following time span.
   - "End time": You define the time range using a starting time and an end time.
   - "Measuring points": You define the time range using a starting time and a number of measuring points.
3. Configure the value range of the trend display under "X axis" and "Y axis".
4. Under "Limits", configure the colored marking of specific values, .e.g. high and low limit, uncertain status.

##### Configuring a diagram

Configure the display of several trends under "Properties > Properties > Appearance":

- Common diagram or separate diagrams
- Common or separate axes
- Writing direction of all trends

##### Toolbar

In Runtime, the operator controls of the f(x) trend view are defined in the "Properties > Properties > Toolbar" Inspector window. The following operator controls are available for the f(x) trend view:

| Button | Name | Function |
| --- | --- | --- |
| ![Toolbar](images/74756700939_DV_resource.Stream@PNG-de-DE.png) | Zoom +/- | Increases or decreases the size of the trends in the trend window. Increase the size of the trends by left-clicking with the mouse. Hold down <Shift> and left-click to decrease the size of the trends. |
| ![Toolbar](images/33643902475_DV_resource.Stream@PNG-de-DE.png) | Zoom area | Increases the size of any section of the trend window. Specify an area in the trend window by using the mouse. This area of the trend window is enlarged. |
| ![Toolbar](images/33643905803_DV_resource.Stream@PNG-de-DE.png) | Zoom X axis | Increases or decreases the size of the X axis in the trend window. Enlarge the X axis by left-clicking with the mouse. Hold down <Shift> and left-click to decrease the size of the X axis. |
| ![Toolbar](images/33643909131_DV_resource.Stream@PNG-de-DE.png) | Zoom Y axis | Increases or decreases the size of the Y axis in the trend window. Enlarge the Y axis by left-clicking with the mouse. Hold down <Shift> and left-click to decrease the size of the Y axis. |
| ![Toolbar](images/33643912459_DV_resource.Stream@PNG-de-DE.png) | Trend area | Shift the trends in the trend window along the X axis and Y axis by using this button. |
| ![Toolbar](images/33643992587_DV_resource.Stream@PNG-de-DE.png) | Axis area | Shift the trends in the trend window along the value axis by using this button. |
| ![Toolbar](images/23980203659_DV_resource.Stream@PNG-de-DE.png) | Original view | Switches from the magnified trend view back to the normal view. |
| ![Toolbar](images/102411248779_DV_resource.Stream@PNG-de-DE.png) | Start/stop | Stops and starts the trend update. The values are buffered and updated as soon as you start trend update again. |
| ![Toolbar](images/23942162827_DV_resource.Stream@PNG-de-DE.png) | Ruler | Determines the coordination of a point of the trend. |

The order of the buttons is fixed. The operator can set up individual key assignments, and shortcuts for every button on the toolbar.

##### Notes on performance

The display of tags with short acquisition cycles can cause the data displayed in the f(X) trend view to be updated slowly.

To avoid delayed display in the control, configure the acquisition cycle of the tags greater than or equal to 1 s.

---

**See also**

[Configure trend view (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-trend-view-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### f(x) trend view (RT Professional)

##### Use

You use the "f(x) trend view" object to represent the values of a tag as a function of another tag. This means that you can present temperature trends as a function of the pressure, for example. You can also compare the trend to a setpoint trend.

![Use](images/88065315979_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, colors and font types of the object. You can adapt the following properties in particular:

- Adding and configuring trends
- Configuring a diagram
- Window settings
- Persistence
- Toolbar

##### Configuring trends

1. Select the data supply for the trend under "Properties > Properties > Trends > Data source".

   - "Log tags": The trend view is supplied with values from a data log.
   - "User-defined": The trend view is supplied user-defined in Runtime by means of scripts.
   - "Recipe" The trend view is supplied with values from a recipe.
   - "Tags": The trend view is supplied with values of a tag.
2. Configure the area of the trend view under "Data area".

   - "Time span": You define the time range using a starting time and a following time span.
   - "End time": You define the time range using a starting time and an end time.
   - "Measuring points": You define the time range using a starting time and a number of measuring points.
   - "Start ID" and "Number of data records": With data supply via recipes, you define the range by the ID of the first data record and the number of subsequent data records.
3. Configure the value range of the trend display under "X axis" and "Y axis".

   - "Automatic": The displayed value range is automatically adapted to the current values.
   - "Initial value / End value": You define the minimum value and maximum value for the value range.
4. Under "Limits", configure the colored marking of specific values, .e.g.. high and low limit, uncertain status.

##### Configuring a diagram

Configure the display of several trends under "Layout":

- Common diagram or separate diagrams
- Common or separate axes
- Writing direction of all trends

##### Window settings

Under "Layout > Window", define whether the user can change the size of the window in runtime and can close the window.

##### Persistence

Under "Security > Persistence" define how long a user's changes to the trend view in runtime are retained.

- "Allow persistence"

  Users can change settings. Changes are retained until the next screen change.
- "Persistence until logoff"

  User group changes are retained until logoff.
- "Persistence until next loading"

  User group changes are retained until the project is updated on the HMI device.

##### Toolbar

You define the operator controls of the f(x) trend view in Runtime under "Properties > Toolbar" in the Inspector window. The following operator controls are available for the f(x) trend view:

| Button | Name | Function |
| --- | --- | --- |
| ![Toolbar](images/23982571147_DV_resource.Stream@PNG-de-DE.png) | Online help | Opens the online help. |
| ![Toolbar](images/23942155147_DV_resource.Stream@PNG-de-DE.png) | Configuration dialog box | Opens the configuration dialog. |
| ![Toolbar](images/102270138379_DV_resource.Stream@PNG-de-DE.png) | Zoom +/- | Enlarges and/or shrinks the trends in the trend window. You can enlarge the trend with the left mouse button. You can reduce the size of the trend by holding down <Shift> and left-clicking. |
| ![Toolbar](images/33643902475_DV_resource.Stream@PNG-de-DE.png) | Zoom area | Increases the size of any section of the trend window. Use the mouse to specify an area in the trend window. This area of the trend window is enlarged. |
| ![Toolbar](images/33643905803_DV_resource.Stream@PNG-de-DE.png) | Zoom X axis | Enlarges and/or reduces the X axis in the trend window. You can enlarge the X axis with the left mouse button. You can reduce the size of the X axis by holding down <Shift> and left-clicking. |
| ![Toolbar](images/33643909131_DV_resource.Stream@PNG-de-DE.png) | Zoom Y axis | Enlarges and/or reduces the Y axis in the trend window. You can enlarge the Y axis by left-clicking. You can reduce the size of Y axis by holding down <Shift> and left-clicking. |
| ![Toolbar](images/33643912459_DV_resource.Stream@PNG-de-DE.png) | Move trend range | You can move the trends in the trend window along the X axis and the Y axis using the button. |
| ![Toolbar](images/33643992587_DV_resource.Stream@PNG-de-DE.png) | Move axis range | You can move the trends in the trend window along the value axis using the button. |
| ![Toolbar](images/23980203659_DV_resource.Stream@PNG-de-DE.png) | Original view | Switches from the magnified trend view back to the normal view |
| ![Toolbar](images/23929835147_DV_resource.Stream@PNG-de-DE.png) | Select data connection | Opens a dialog for selecting logs and tags. |
| ![Toolbar](images/8263486859_DV_resource.Stream@PNG-de-DE.png) | Select trends | Opens a dialog for setting the visibility of trends. |
| ![Toolbar](images/102411252619_DV_resource.Stream@PNG-de-DE.png) | Select time range | Opens a dialog for setting the displayed time range in the trend window. |
| ![Toolbar](images/23980641931_DV_resource.Stream@PNG-de-DE.png) | Previous trend | Displays the previous trend in the foreground. |
| ![Toolbar](images/23980803211_DV_resource.Stream@PNG-de-DE.png) | Next trend | Displays the next trend in the foreground. |
| ![Toolbar](images/102411244939_DV_resource.Stream@PNG-de-DE.png) | Start/stop | Stops and starts the trend update. The values are buffered and updated as soon as you start trend update again. |
| ![Toolbar](images/23931759499_DV_resource.Stream@PNG-de-DE.png) | Print | Click this button to print the trend shown in the trend window. The print job used during printing is defined in the configuration dialog in the "General" tab. |
| ![Toolbar](images/25825901579_DV_resource.Stream@PNG-de-DE.png) | Export data | This button is used for exporting all or the selected runtime data to a csv file.  If the "Display dialog" option is activated, a dialog opens in which you can view the settings for export and start the export. You may also select the file and the directory for the export with the corresponding authorizations.  If no dialog is displayed, the export of data to the default file begins immediately. |
| ![Toolbar](images/23942162827_DV_resource.Stream@PNG-de-DE.png) | Ruler | Determines the coordinates of a point of the trend. |
| ![Toolbar](images/33645263115_DV_resource.Stream@PNG-de-DE.png) | Connect backup | Opens a dialog in which selected logs are connected to WinCC Runtime. |
| ![Toolbar](images/33652020363_DV_resource.Stream@PNG-de-DE.png) | Disconnect backup | Opens a dialog in which selected logs are disconnected from WinCC Runtime. |

The order of the buttons is fixed. The operator can set up individual key assignments, and shortcuts for every button on the toolbar.

---

**See also**

[f(t) trend view (RT Professional)](#ft-trend-view-rt-professional)
  
[Table view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#table-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configure trend view (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-trend-view-rt-professional)
  
[Value table (RT Professional)](#value-table-rt-professional)
  
[Configuring persistence (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-persistence-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Graphic view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

The "Graphic view" object is used to display graphics.

![Use](images/61123866763_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Graphic: Specifies the graphic file that is displayed in the object.
- Adjust graphic: Specifies the automatic size stretching for objects with graphics.
- Transparent color: Specify whether or not the transparent color is used for the graphic.

##### Inserting graphics

Use the following graphic formats in the "Graphic view" object: *.bmp, *.tif, *.png, *.ico, *.emf, *.wmf, *.gif, *.svg, *.jpg or *.jpeg. You may also use graphics as OLE objects in the Graphic view .

1. In the Inspector window, select "Properties > Properties > General".
2. Select the graphic that you wish to insert.

   The graphic preview is shown in the right pane.

   You have the option to create the graphic from a file using the ![Inserting graphics](images/82738200203_DV_resource.Stream@PNG-de-DE.png) button, or to create a new graphic from an OLE object using the ![Inserting graphics](images/82744225035_DV_resource.Stream@PNG-de-DE.png) button.
3. Click "Apply" to insert the graphic in the Graphic view .

##### Adjust graphic

Whether a graphic displayed in a Graphic view is stretched to the size of the Graphic view in runtime is specified in the Inspector window.

| Option | Description |
| --- | --- |
| "No auto-sizing" | The size is not automatically adapted in Runtime. |
| "Fit graphic to object size" | The graphic is automatically adapted to the object size in Runtime. |
| "Fit object size to graphic" | Graphic display is adapted to the largest used graphic and other graphics are stretched. |
| "Adjust object size to graphic" | Graphic display is adapted to the largest used graphic but the other graphics retain their original size. |

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select the required size adjustment for the graphic.

##### Transparent color

This property defines whether the transparent color is used for the graphic to be displayed.

1. In the Inspector window, select "Properties > Properties > Appearance":
2. Select "Background > Transparent".
3. Select a transparent color.

**Note**

When using bitmaps in WinCC screens the "Transparent color" setting demands a high character performance in the layout on the panel. Visualization performance is enhanced by disabling the "Transparent" setting in the properties of the relevant display object. This restriction applies in particular when bitmaps are used as background image.

**Note**

**Basic Panels**

The "Transparent" property is not available for Basic Panels.

**Note**

If the selected transparent color of the graphic is not shown properly although the "Transparent" property is activated, the color in the graphic is not entirely consistent with the selected color. For example, the selected transparent color [R=255;G=255;B=255] looks almost exactly like the color in the graphic that is expected to be transparent [R=255;G=251;B=255]. In this case, the graphics used in the object must be reedited. Under "Project Navigation > Languages & Resources > Graphics", select the graphic that you want to display transparently. From the shortcut menu of the default graphic, select the "Edit" command and fill in the background of the graph with the desired color that appears transparent in the screen. Save the graphic.

---

**See also**

[Storing an external image in the graphics library (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#storing-an-external-image-in-the-graphics-library-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Options for editing objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#options-for-editing-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of objects (RT Professional)](#overview-of-objects-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Graphic I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

The "Graphic I/O field" object can be used to configure a list for display and selection of graphic files.

![Application](images/58080912779_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Scroll bar type: Specifies the graphic layout of the scroll bar.
- Mode: Specifies the response of the object in Runtime.

> **Note**
>
> **Scroll bar**
>
> The "Scroll bar > Type" property is available for Panels and Runtime Advanced up to device version V12.

> **Note**
>
> **Reports**
>
> Graphic I/O fields output exclusively graphics in reports. "Output" mode is preset. Properties for configuring the selection of graphics are not available, e.g. "scroll bar".

> **Note**
>
> **Border**
>
> You can configure the width and the style of the border of a graphic I/O field in the "Two states" mode.
>
> The dynamization of the border colors in "Two states" mode has no effect during runtime.

##### Mode

The response of the "Graphic I/O field" object is specified under "Properties > Properties > General > Type > Mode" in the Inspector window.

| Mode | Description |
| --- | --- |
| "Input" | The "Graphic I/O field" object is only used to select graphics. |
| "Input/output" | The "Graphic I/O field" object is used to select and display graphics. |
| "Output" | The "Graphic I/O field" object is used to display graphics only. |
| "Two states" | The "Graphic I/O field" object is only used to display graphics and can have a maximum of two states.  You use no graphics list but insert one graphic each for the "ON" and "OFF" state. |

##### Adjust graphic

Whether a graphic displayed in a graphic I/O field is stretched to the size of the view in Runtime is specified in the Inspector window.

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select the required size adjustment for the graphic.

##### Scroll bar type

The response for the graphic representation of the scroll bar is specified under "Properties > Properties > Appearance > Scroll Bar > Type" in the Inspector window.

| Type | Description |
| --- | --- |
| "Permanent" | The scroll bar is always visible. |
| "No scrollbar" | The scroll bar is not visible. |
| "Visible after clicking" | The scroll bar is made visible by a mouse click. |

##### Behavior during operation

If the graphic I/O field displays a cactus image, a graphic to be output for a specific value has not been defined in the project. The contents of the graphic I/O field change color to show that it is now activated. The frame in 3D is only shown graphically in an output field.

---

**See also**

[Symbolic I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced)](#symbolic-io-field-basic-panels-panels-comfort-panels-rt-advanced)
  
[Print job/script diagnostics (RT Professional)](#print-jobscript-diagnostics-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Graphic I/O field (RT Professional)

##### Use

With the "Graphic I/O field" object you configure a graphics list which is used to display and select graphic files.

![Use](images/88066765195_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you can customize the settings for the object position, geometry, style, frame and color. You can adapt the following properties in particular:

- Mode: Specifies the response of the object in runtime.
- Fit to size: Specifies the ratio of the display window and the embedded graphic.

##### Mode

The response of the "Graphic I/O field" object is specified in the Inspector window in "Properties > Properties > General > Mode".

| Mode | Description |
| --- | --- |
| "Output" | The "Graphic I/O field" object is used to display graphics only. |
| "Two states" | The "Graphic I/O field" object is only used to display graphics and can have a maximum of two states.  You use no graphics list but insert one graphic each for the "ON" and "OFF" state. |

##### Fit to size

The ratio for the graphic representation in the display window is specified under "Properties > Properties > Layout > Fit to size" in the Inspector window.

| Sizing type | Description |
| --- | --- |
| "Fit object size to content" | The display window is adapted automatically to the size of the graphic. |
| "Fit content to object size" | Adjust the graphic to the display window size. |

---

**See also**

[Symbolic I/O field (RT Professional)](#symbolic-io-field-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

The "GRAPH Overview" object is used to display the current program status for executed steps of the GRAPH sequencer. Errors during execution of a program are displayed directly at the corresponding step.

![Use](images/81518474379_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **ProDiag license required**
>
> To use the "GRAPH Overview" object in conjunction with the ProDiag supervision in your program, you need a ProDiag license.

The following information is displayed in the "GRAPH Overview" object:

- Name and status of the function block
- Status of initial and simultaneous steps
- Number and name of the first step currently executed step
- Operating mode for running the GRAPH sequencer

WinCC supports the display of step names for the GRAPH blocks in multiple languages starting from Version 5.0. The step names will then be displayed in the selected Runtime language following a language changeover in Runtime. If the selected language is not available in the GRAPH block, the names are displayed in the default language (English).

> **Note**
>
> The "GRAPH Overview" object cannot be used in faceplates or in the global screen.

> **Note**
>
> **Device dependency of the "GRAPH Overview" object**
>
> The "GRAPH Overview" object is available for RT Advanced, RT Professional, Comfort Panels and KTP Mobile Panels.

> **Note**
>
> **Requirement for display in GRAPH overview**
>
> For the display of the program status of an S7 GRAPH instance data block in the "GRAPH overview" object to be possible, the instance-specific properties of the block must be set as "Visible in HMI" and "Accessible from HMI".

##### Layout

In the Inspector window, you customize the position, style, colors and font types of the object. You can adapt the following properties in particular:

- Assigned GRAPH DB tag
- Buttons on the toolbar

##### Operating mode

Four operating modes are available for running the GRAPH sequence:

- Auto (default setting) - Automatically switches to the next step when the transition is fulfilled.
- TAP - Automatically switches to the next step when the transition is fulfilled and there is an edge change from "0" to "1" at the T_PUSH parameter.
- TOP - Automatically switches to the next step when the transition is fulfilled or there is an edge change from "0" to "1" at the T_PUSH parameter.
- Manual - The next step is not automatically enabled when the transition is fulfilled. The steps can be selected and deselected manually.

> **Note**
>
> You set the operating mode by modifying the interface parameters of the GRAPH block in your control program.

In WinCC Runtime Professional, you have the option of editing the name of the operating mode that is displayed in the GRAPH overview.

##### Configuring three-line mode with criteria analysis

In three-line mode you see additional lines with the previous and next steps in the GRAPH overview as well as the first operand with error of the criteria analysis.

![Configuring three-line mode with criteria analysis](images/165915662347_DV_resource.Stream@PNG-en-US.png)

- To display the previous and next steps, select the "Previous and next step" option under "Properties > Appearance > Options".
- To display the first operand with error of the criteria analysis, select the "Criteria analysis" option under "Properties > Appearance > Options".

  > **Note**
  >
  > The criteria analysis will not output any information in the GRAPH overview in the following cases:
  >
  > - If the version of the GRAPH block is older than V4.0
  > - If the initial value acquisition was not activated or if the initial values were not acquired
  > - If no error is present in the current step

##### Configuring a compact view

You can also configure a compact GRAPH overview without toolbar buttons and operating mode display, as was previously possible in WinCC Professional versions before V14.

To display the GRAPH overview compactly in single-line compatibility mode, select the "Single-line mode" option under "Properties > Appearance > Options".

![Configuring a compact view](images/81523039115_DV_resource.Stream@PNG-de-DE.png)

##### Symbols

You specify the symbols that are displayed in the GRAPH Overview in the Inspector window under "Properties > Appearance > Options". The following symbols are available for GRAPH Overview:

| Symbol | Name | Function |
| --- | --- | --- |
| ![Symbols](images/81523267723_DV_resource.Stream@PNG-de-DE.png) | Error | Indicates that an error has occurred during the execution of a step. |
| ![Symbols](images/81524872587_DV_resource.Stream@PNG-de-DE.png) | Initial step | Indicates that the currently executing step is the first step in the GRAPH block. |
| ![Symbols](images/81523276555_DV_resource.Stream@PNG-de-DE.png) | Simultaneous step | Shows that there are other simultaneous steps in the GRAPH block in addition to the current one. |

##### Buttons

You specify the buttons that are displayed in the GRAPH Overview under "Properties > Toolbar > General".

| Button | Name | Function |
| --- | --- | --- |
| ![Buttons](images/81524907019_DV_resource.Stream@PNG-de-DE.png) | Next step | Jumps to the next step, if the GRAPH block contains more than four steps. |
| ![Buttons](images/82552734219_DV_resource.Stream@PNG-de-DE.png) | Last step | Jumps to the first step of the sequencer when the final step has been reached. |
| ![Buttons](images/81524915851_DV_resource.Stream@PNG-de-DE.png) | Alarm view | Opens the configured alarm view with the error message in Panels and RT Advanced.  Opens the configured alarm view with the error message in RT Professional. |
| ![Buttons](images/81524937483_DV_resource.Stream@PNG-de-DE.png) | PLC code view | Opens the configured PLC code view. |

##### Display the current program status

A PLC including a GRAPH instance data block has been created and contains at least one PLC tag which is visible in and accessible from the HMI.

1. Move the GRAPH overview out of the toolbox window using drag-and-drop.
2. In the Inspector window, select "Properties > Properties > General".
3. Open the selection button under "Process > Tag".

   The "Add new object" dialog opens.
4. Select the corresponding PLC in the "Program blocks" folder.
5. Select the corresponding PLC tag of the GRAPH instance data block.
6. You can dynamize the properties in the "GRAPH Overview" object using tags and color-code the states.

   You can find a detailed description of dynamizing a property in the section [Dynamizing screens](#dynamizing-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional).

> **Note**
>
> If no connection exists between the HMI device and the selected PLC, a connection is set up automatically.
>
> In addition, an HMI tag is created which is connected to the PLC tag.

---

**See also**

[Initial value acquisition and criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#initial-value-acquisition-and-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)
  
[Supervising machinery and plants with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supervising-machinery-and-plants-with-prodiag-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a GRAPH overview (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-graph-overview-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Displaying the status of the GRAPH sequencer (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#displaying-the-status-of-the-graph-sequencer-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring property animation of the "Range" type (RT Professional)](#configuring-property-animation-of-the-range-type-rt-professional)
  
[Objects for WinCC Runtime Professional (RT Professional)](#objects-for-wincc-runtime-professional-rt-professional)
  
[Dynamizing screens (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#dynamizing-screens-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Handwheel (Panels, Comfort Panels)

##### Use

The object "Handwheel" is a control element for some SIMATIC Mobile Panels. You can enter incremental values in Runtime using the "HandWheel" object.

![Use](images/6382264331_DV_resource.Stream@PNG-de-DE.png)

##### Layout

You can set the following property in the Inspector window:

- Tag: Specifies the tags to which the "HandWheel" object is linked.

##### Global assignment

The "Tag" property is used to specify the global assignment of the "HandWheel" object in the global screen. There is only one global screen per HMI device.

1. In the Inspector window, select "Properties > Properties > General".
2. Select a tag from the selection list under "Settings > Tag".

##### Local assignment

The "HandWheel" object is assigned to another tag. To do so you configure a function that assigns the tag to the handwheel in Runtime.

Example for configuration to a button:

1. Open the screen in which the "HandWheel" object is assigned to another tag.
2. Drag the "Button" object from the toolbox to the screen. Select the button on your screen.
3. Click "Properties > Events > Click" in the Inspector window.
4. The "Function list" dialog box opens. Click the first line of the function list. The list of system functions and scripts available in the project appears.
5. Select the system function "SetTagToHandWheel" from the "Other functions" group. Select a tag from the combo box at "Value".

**Note**

The Mobile Panel may ignore the change of the value in the PLC made at another location while the handwheel is being operated. The value is the PLC is overwritten again.

---

**See also**

[Illuminated pushbutton (Panels, Comfort Panels)](#illuminated-pushbutton-panels-comfort-panels)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Help indicator (Basic Panels)

##### Application

The object "help indicator" is available for the HMI device KP300 Basic. If a a tooltip exists for the selected object, the help indicator is displayed during runtime. If a tooltip was configured for the opened screen, the help indicator always remains visible.

![Application](images/25441881611_DV_resource.Stream@PNG-de-DE.png)

You configure the object "help indicator" exclusively in the global screen.

##### Layout

You can adapt the following properties in the Inspector window:

- Position: Determines the position of the object "Help indicator."

##### Position

You can use this property to set the position of the object "Help indicator."

1. Select the object "Help indicator" in the template.
2. In the Inspector window, select "Properties > Properties > Layout".
3. Enter a value for X and Y. You can also use the cursor keys to position the selected object.

If you have configured a screen object at this position, the visible help indicator covers the screen object. The help indicator is covered only by incoming system alarms and dialogs.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### HTML browser (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Use

The "HTML Browser" object is designed for the visualization of simple HTML pages. This function allows you to draw up machine-specific descriptions which are stored centrally and which can then be displayed from different HMI devices.

![Use](images/69805802379_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> Switching the functionality of the HTML Browser to that of a file explorer by one of the following methods, for example, is not authorized in the context of WinCC:
>
> - Entering a folder or drive, for example "\" or "C:", or
> - Connecting to an FTP server, for example "ftp://"
>
> One reason is to prevent inadvertent changes to files, their deletion or execution.
>
> When configuring, ensure that the operator can only enter valid Internet addresses, for example, by using symbolic I/O fields. Configure a password-protected input for service purposes.

> **Note**
>
> Only one instance of the HTML Browser is supported per screen for Panels to preserve memory space.
>
> If you move quickly from a slide-in-screen to a pop-up screen and an HTML browser is configured in both screens, the second HTML browser will not open. After closing the slide-in screen, wait two seconds until the handle is no longer visible and then open the pop-up screen.

> **Note**
>
> **Device-based dependency of the "HTML browser" object**
>
> The "HTML browser" object is available for Basic Panels, Comfort Panels and KTP Mobile Panels starting with a 7'' display size and RT Advanced.

##### Layout

Customize the object position and size in the Inspector window. In particular, you can customize the following property:

- URL: Specifies which Internet address is opened in the HTML Browser.
- Tag for URL: Specifies the tag which sets the Internet address.

If the toolbar of the HTML browser toolbar is not activated, the browser background is transparent on a Comfort Panel and in Runtime Advanced, and the progress indicators are not visible.

##### Address

The Internet address is specified in "Properties > Properties > General >URL" in the Inspector window.

> **Note**
>
> **For Basic Panels 2nd Generation:**
>
> If you want to load a website from a USB flash drive to your HMI device, the address in the "URL" field must begin with the prefix "\media\usb\".
>
> Example: You want to load the html5.htm web page from the USB device USB_XY. Enter "\media\usb\USB_XY\html5.htm" in the Inspector window.

> **Note**
>
> The DNS service for Internet access with the "HTML browser" object is not supported for Basic Panels 2nd Generation.  
> This means only access via the IP address is supported.

##### Browser type (RT Advanced as of V13 SP1)

You can select the browser type in Runtime Advanced as of version V13 SP1.

Specify the type of the Web browser under "Properties > Properties > General > HTML browser type" in the Inspector window.

Two options are available:

- Web browser based on WebKit engine without Active X support

  > **Note**
  >
  > Dialogs from websites are not supported in the WebKit browser. "Yes" or "OK" is always set as answer instead.
- Web browser based on Internet Explorer with Active X support

  > **Note**
  >
  > If Internet Explorer does not load the website, use the WebKit browser without Active X support.

##### Basic procedure

1. Create an internal tag of the "String" data type, for example, InternetAddress, in the "Tag" editor.
2. Insert the "HTML Browser" object in the screen in the "Screens" editor.
3. In the Inspector window, select "Properties > Properties > General".
4. At "Tag for the URL", select the "InternetAddress" tag from the selection list.
5. Insert an I/O field in the screen in the "Screens" editor.
6. In the Inspector window of the IO field "Properties > Properties > General > Tag for URL", select the "InternetAddress" tag from the selection list.

   ![Basic procedure](images/72547288715_DV_resource.Stream@PNG-en-US.png)

   ![Basic procedure](images/72547288715_DV_resource.Stream@PNG-en-US.png)

The HTML Browser opens the relevant page after the operator has entered an address in the I/O field.

##### Operator controls

Operator controls are configured buttons in the process screen or softkeys on the HMI device.

The "HTML Browser" object does not have its own operator controls. Assign the system functions used to control the "HTML Browser" object to your configured operator controls, such as buttons.

1. For example, drag the "Button" object to the screen from the toolbox.
2. Input a text of any length or select a graphic, for example Update.
3. In the Inspector window, select "Properties > Events > Click".  
    The "Function list" dialog opens.
4. The system functions for controlling the "HTML Browser" object can be found in the list of system functions in the "Keyboard operation for screen objects" group.   
   Select a function from the list, for example, HTMLBrowserRefresh.
5. Select the object name of the HTML Browser in which the command will be executed from the "Screen object" list.

##### Defining the website selection

To define the website selection that is provided in the HTML browser, you can define a number of allowed URL addresses.

You define a String or Wstring type tag or for the "Tag for URL" property of the HTML browser that can be filled with the predefined URL addresses in the following ways:

- Using the "SetTag" system function, which you configure on a button
- Using an I/O field

  > **Note**
  >
  > Any website can be accessed by entering the address in an I/O field.
  >
  > To restrict the selection of permitted websites, use the provision of the pre-defined URL addresses via a system function or a script.
- Via a script (Panels and RT Advanced only)
- Via the PLC

##### Displaying SIMOTION PLC websites in the HTML browser

If the SIMOTION PLC websites are not displayed correctly in the HTML browser, add "/basic" after the website URL to display the websites in basic mode.

##### Comments

The functional scope of the HTML Browser is limited in comparison to the Internet Explorer:

- The HTML Browser will only show pure HTML pages. VBScript, Java, JavaScript, Flash and ActiveX controls are not supported. Set up the HTML pages for display in the HTML Browser by using a text editor or using a simple HTML editor.
- Links to embedded files, for example *.pdf or *.xls, are not supported.
- Queries and dialogs that are conducted during the access of, for example protected pages are not supported. When accessing protected pages, enter your user name and password in the URL: <http://username:password@servername> (for example "http://Administrator:Admin123@192.168.0.199").

> **Note**
>
> The object "HTML Browser" supports dynamization.
>
> If you select the HTML browser type "Web browser, based on a WebKit engine", only the tag connection is available for dynamization under "Address".

> **Note**
>
> **For Basic Panels 2nd Generation and Comfort Panels:**
>
> The object "HTML Browser" does not support proxy settings. This means the "HTML Browser" object cannot access URLs that require a change of the proxy settings.

> **Note**
>
> **HTML browser in "Scroll indicator" mode**
>
> If you have specified the "Scroll indicator" scroll mode in "Runtime settings > Screens > Scrolling in controls", it may occur that some websites are not correctly displayed.

> **Note**
>
> **HTML browser in "Web browser, based on WebKit Engine" mode with screen scroll bars**
>
> You configure the "HTML browser" object in the "Web browser based on WebKit Engine" mode and activate the scrolling mode for the display. The right and the lower bars are activated for scrolling in Runtime.
>
> If the bars of the displayed HTML page and the HTML browser object overlap in Runtime, operate the scroll bars of the HTML browser with a mouse click and double-click on the scroll bars of the website. If you have already configured the object in the HMI screen, try to avoid the double scroll bars by adjusting the object to the size of the website to be displayed.

---

**See also**

[Web browser of WebKit engine: Overview (Panels, Comfort Panels)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#web-browser-of-webkit-engine-overview-panels-comfort-panels)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### HTML browser (RT Professional)

##### Application

The "HTML Browser" object is designed for the visualization of simple HTML pages. Centrally stored machine-specific descriptions can therefore be displayed by different HMI devices.

![Application](images/172199627787_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> Switching the functionality of the HTML browser as file explorer, e.g. in the following ways, is not enabled:
>
> - Entry of a folder or drive, for example "\" or "C:"
> - Connecting to an FTP server, for example "ftp://"
>
> This prevents files from being unintentionally changed, executed or deleted.
>
> When configuring, ensure that the operator can only enter valid Internet addresses, for example, by using symbolic I/O fields. Configure a password-protected input for service purposes.

##### Layout

Customize the object position and size in the Inspector window. You can adjust the following properties in particular:

- Address: Specifies which Internet address is opened in the HTML Browser.
- Toolbar: Specifies whether a navigation toolbar is shown.

##### Address

The Internet address is specified in the Inspector window under "Properties > Properties > General > Window > URL".

##### Web browser type

You can specify the type of web browser in the Inspector window, under "Properties > Properties > General > Web browser type".

Two options are available:

- Web browser control based on Internet Explorer
- Web browser control based on Chromium

##### Basic procedure

1. Create an internal tag of the "String" data type, for example, "InternetAddress", in the "Tag" editor.
2. Insert the "HTML Browser" object in the screen in the "Screens" editor.
3. In the Inspector window, select "Properties > Properties > General".
4. AFor "Tag for URL", select the "InternetAddress" tag from the selection list.
5. For "Web browser type", select "... based on Chromium".
6. Insert an I/O field in the screen in the "Screens" editor.
7. Select the "InternetAddress" tag from the selection list under "Properties > Properties > General> Tag for URL" in the Inspector window.

   ![Basic procedure](images/172716497291_DV_resource.Stream@PNG-en-US.png)

   ![Basic procedure](images/172716497291_DV_resource.Stream@PNG-en-US.png)

When the operator enters or activates an address in the I/O field, the HTML browser opens the relevant page.

##### Restrictions and remarks

- The "Browser" object supports the following reports:

  - https://
  - http://
  - file://
- Note that the "http://" and "file://" reports do not function in the simulation.
- Queries and dialogs that are conducted during the access of, for example protected pages are not supported. When accessing protected pages, enter your user name and password in the URL: <http://username:password@servername> (for example "http://Administrator:Admin123@192.168.0.199").
- The "Web control" object only displays content that is supported by the web browser in which Runtime is open.
- The object is implemented as an iFrame. Pages with X-frame option settings that prevent the display in an iFrame are not displayed in the object.

##### Show PDF files in Runtime

The "Browser" object displays PDF files that are available:

- Locally on the HMI device
- On the Internet
- On an external storage medium

You can view a PDF file in the following ways:

- Under "Properties > URL", enter the address "https://localhost/WebRH/<pdfname.pdf>".
- Enter a valid Internet address under "Properties > Properties > URL".
- In the configuration of the "Browser" operating object under "Properties", link the URL with a tag of the type WString which contains the path and file name.
- Enter path and file name in the URL input field of the "Browser" operating object.

  Syntax: file:///<path>/<file name>.pdf

  Pay attention to uppercase/lowercase spelling.

The "Browser" object supports a large number of default parameters with which you can influence how a PDF file is displayed.

Examples of parameters when opening the PDF file:

- Jump to specific page: https://winccunified/WebRH/UCPManual.pdf#page=18
- Jump to table of contents: https://winccunified/WebRH/UCPManual.pdf#tableofcontents
- Zoom in on page: https://winccunified/WebRH/UCPManual.pdf#zoom=200

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Symbol

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Camera view (Panels, Comfort Panels, RT Advanced)

##### Use

You use the "Camera view" object to configure the camera view which outputs screens for the operator in runtime from a connected network camera.

Monitoring with the help of the network camera lends itself for situations in which the operator has limited visibility of the plant or cannot get close to the machines. The operator can then respond to any problem much faster to remedy its cause.

![Use](images/68146873227_DV_resource.Stream@PNG-de-DE.png)

The camera view can be configured in the following screens:

- In a screen
- In a template
- In a slide-in screen
- In a pop-up screen

> **Note**
>
> **Device dependency of the "Camera view" object**
>
> The "Camera view" object is available for Comfort Panels, KTP Mobile Panels (as of device version V13) and RT Advanced.

> **Note**
>
> Only one camera view may be in operation in runtime at the time.

> **Note**
>
> Use the "Camera view" object only with network cameras.   
> Make sure that the connected network camera is located in a secure network with known devices and IP addresses.
>
> For more information on security, go to:
>
> [http://www.siemens.com/industrialsecurity](http://www.industry.siemens.com/topics/global/en/industrial-security/Pages/Default.aspx)

##### Layout

You enter the information on the source of the video stream as well as position and size of the camera view in the Inspector window. You can adapt the following properties in particular:

- URL for the source of the video stream:

  - Camera URL: Specifies a static URL which is only entered during configuration.
  - Camera URL tag: Specifies a dynamic URL which the operator can change later in runtime.
- Transmission protocol: Specifies the transmission protocol by which the data exchange between the panel and the network camera takes place.
- Position and size of the camera view: Specifies position and size of the camera view as well as the aspect ratio and size of the displayed video stream.

##### Supported network cameras and recommended settings

Use the "Camera view" object with the network cameras which support the streaming protocol RTP/RTSP and MJPEG, H.264 and MPEG4 codecs.

You can find information on the supported network cameras and recommended settings under [Supported network cameras and settings.](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supported-network-cameras-and-settings-panels-comfort-panels-rt-advanced)

##### Specifying URL for the source of the video stream

1. Insert the camera view in the screen in the "Screens" editor. The camera view is found in the task card "Tools" > "Controls".
2. Click "Properties > Properties > General > Media" in the Inspector window.
3. Enter the static camera URL in the "Camera URL" field, for example, "rtsp://user:password@192.168.56.208" for a Siemens camera.

   The address of the network camera is available in the network camera manual.
4. Assign a tag to the camera view under "Camera URL tag" in the Inspector window. The tag must be of the data type "String" for external tags and "WString" for internal tags.

   When you assign a tag to the camera view, the user can change the source of the video stream in runtime.

**Note**

The camera URL always starts with "rtsp://" and must only include permitted characters. If you enter characters that are not permitted or if the URL does not start with "rtsp://", the camera cannot be operated in runtime. The operator will receive an error message in the "Camera view" to indicate the problem.

The following characters of the US ASCII character set are permitted:

0123456789

A...Z a...z

!#$%&()*+,'-_./:;<=>?@ [\]_{|}~^(")`

> **Note**
>
> If you leave the "Camera URL tag" field blank, the static URL is used in runtime.
>
> If you enter information in the "Camera URL" and "Camera URL tag" field, the dynamic URL is used in runtime.

##### Specifying the transmission protocol

1. Click "Properties > Properties > General > Media" in the Inspector window.
2. Specify the transmission protocol with the "Use UDP instead of TCP" check box.

   The selection of the protocol depends on the protocol types which your network camera supports. Information on supported protocols is available in the network camera manual.

   In most cases, a TCP connection has reliable synchronization with the camera view.

##### Specifying position and size of the camera view

1. Click "Properties > Properties > General > Layout" in the Inspector window.
2. Enter the size of the object under "Camera view" in the "Position & Size" area. To achieve the best picture quality of the video stream, enter the physical resolution of the network camera as size of the camera view.

   The recommended setting "Keep video size" is selected by default in the "Fit to size" area. The "Keep aspect ratio" check box is disabled and cannot be selected.
3. To keep the aspect ratio of the video stream, disable "Keep video size".

   The "Keep aspect ratio" check box is automatically selected.

**Note**

The screen is not scaled when you keep the size of the video stream. The screen size of the network camera is output 1:1 by the camera view. If the camera view is smaller than the selected resolution of the network camera, only a corresponding section of the camera screen is output by the camera view. If the camera view is greater than the selection solution of the network camera, any blank spaces are displayed as black horizontal or vertical margins. For optimal performance on panels, we recommend using the "Keep video size" option and configuring the camera view to match the resolution of the camera in order to avoid black borders in the camera view.

Any blank spaces are output as black horizontal or vertical margins by the camera view when you keep the aspect ratio of the video stream.

**Note**

When you disable the "Keep video size" and "Keep aspect ratio" check boxes, the camera screen may be distorted.

##### Comments

> **Note**
>
> You cannot configure system functions for the camera view.

> **Note**
>
> When you test a project with the simulator, a black screen with a camera symbol is output.

---

**See also**

[Objects for WinCC Runtime Advanced (RT Advanced)](#objects-for-wincc-runtime-advanced-rt-advanced)
  
[Supported network cameras and settings (Panels, Comfort Panels, RT Advanced)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supported-network-cameras-and-settings-panels-comfort-panels-rt-advanced)

#### Channel diagnostics display (RT Professional)

##### Application

You use the "Channel diagnostics display" object to monitor the active connections in Runtime. The "Channel Channel diagnostics display" object allows you to output the following status and diagnostic information for the channel units:

- Output status/statistical information about the connections in Runtime
- Text output to a logbook file for fault analysis, and troubleshooting
- Text output to a trace file to help the Hotline in pinpointing the cause of connection problems

  ![Application](images/2701862283_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window you can customize the settings for the object position, geometry, style, frame and color.

##### Check channel and connection

To do this, activate your project. Status information on all configured connections is displayed in the object "Channel diagnostics view" in the Channels/Connections tab.

1. Open a screen.
2. Insert the "Channel diagnostics view" from the "Controls" object pane into the screen.
3. Save the screen.
4. Start Runtime.
5. Select the screen in which you have configured the Channel diagnostics view.
6. The configured connections are displayed in the "Channels/Connection" tab.
7. Check the icons in front of the connection name. If the status of a channel, and connection are OK, a green check mark is displayed in front the associated entry.
8. If there is no green check mark in front of the name of channel and connection, click a connection. The status information for this connection is displayed in the area on the right.
9. Switch to the "Configuration" tab. Select one of the displayed channels and configure which error displays are to be entered in the associated log file.
10. Check the channel-specific log file. Open the log file from the "Siemens\Automation\SCADA_2007\WinCC\Diagnose" folder in a text editor.
11. Check the latest entries with the "ERROR" flag.
12. Activate the trace function.

    Contact Customer Support if you are unable to locate the error, even after checking the log file.

##### Overview of the status messages

The following statuses are displayed in the "Channel diagnostics display" object:

- Channel / connection ready without restriction
- Channel / connection ready with some restrictions
- No information available about connection status
- Channel / connection failed

---

**See also**

[Diagnostics with the Channel diagnostics view (RT Professional)](Communicating%20with%20PLCs%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#diagnostics-with-the-channel-diagnostics-view-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Combo box (RT Professional)

##### Application

You use the "Combo box" object to present and select entries in a drop-down menu. You activate an entry by default so that the operator only changes the preset value if necessary. To incorporate combo boxes into the process, dynamize the corresponding properties.

![Application](images/88074732683_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, style, colors and font type settings of the object. You can adapt the following properties in particular:

- Number of entries: Defines the number of combo boxes.
- Selection of entries: Defines which entry is displayed as activated by default.

##### Defining the number of entries

1. In the Inspector window, select "Properties > Properties > General".
2. Define the desired number of list boxes under "Label > Entries".

At the same time, the value of the "Entries" attribute specifies the high limit for the "Index" property under "Label." Changing the value can have the following effects:

##### Changing the number

New fields are added under the field with the highest value for the "Index" property if you increase the number of entries.

All fields for which the value of the "Index" property is higher than the new number will be deleted if you reduce the number of entries.

---

**See also**

[List box (RT Professional)](#list-box-rt-professional)
  
[Configure operator input alarms (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-operator-input-alarms-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Check box  (RT Professional)

##### Application

You use the "Check box" object to present and select multiple options. You activate check boxes by default so that the operator only changes the preset value if necessary. The operator can select several options in Runtime. To incorporate a check box into the process, dynamize the corresponding properties.

![Application](images/2651661195_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Number of check boxes: Defines the number of options.
- Check box selection: Defines which options are displayed as activated by default.

##### Define number of check boxes

1. In the Inspector window, select "Properties > Properties > General".
2. Define the desired number of check boxes under "Label > Entries".

At the same time, the value of the attribute specifies the upper limit for the "Index" property under "Label." Changing the value can have the following effects:

- Increases the number

  New fields are added under the field with the highest value of the "Index" property. You can change the default label for the new field using the "Text" property under "Label."
- Reduces the number

  All fields for which the value of the "Index" property is greater than the new number are deleted.

##### Define the default setting of the check boxes

In the table under "Properties > Properties > General > Label > Presetting enabled", you define which options are shown activated in a check box list. You can activate multiple options.

Each option is represented by a bit in a 32-bit word. To activate a field, the corresponding bit must have the value "1". The 32-bit word contains the information for all options of the check box list. The value of the "Presetting enabled" property is specified in hexadecimal format.

---

**See also**

[Option buttons (RT Professional)](#option-buttons-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Circle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Circle" object is a closed object which can be filled with a color or pattern.

![Application](images/58080968203_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you can customize the settings for the object position, geometry, style, frame and color. You can adapt the following properties in particular:

- Radius: Specifies the size of the circle.

##### Radius

The radius of the "Circle" object is specified in the Inspector window. The value is entered in pixels.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value between 0 and 2500 in the "Radius" area.

---

**See also**

[Circular arc (RT Professional)](#circular-arc-rt-professional)
  
[Circle segment (RT Professional)](#circle-segment-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Circular arc (RT Professional)

##### Application

The "Circular arc" is an open object. Use the "Circle segment" object if you want to fill the object with color. By default, a circular arc is a quarter circle. It can be customized as required.

![Application](images/2701810571_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. You can adapt the following properties in particular:

- Radius: Define the size of the circular arc.
- Start and end angle: Specify where the start and end angle lie on a virtual circle of 360°.

##### Defining the radius

Define the horizontal, and the vertical radius of the "Circular arc" object in the Inspector window. Enter the values using Pixels as the unit.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value for "Radius" in the "Arc" area.

##### Define start and end angle

Determine the length of the circular arc using the "Start Angle" and "End Angle" attributes. Enter the values using Degrees as the unit.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value for "Start angle" and "End angle" in the "Radii" area.

##### Alternative procedure

You can also change the start and end points of the circular arc using the mouse.

1. Place the cursor on a start or end point of the circular arc. The start and end points are indicated by small blue squares.

   The mouse cursor changes to a cross.
2. Hold down the mouse button, and drag the start or end point to the desired position.

---

**See also**

[Circle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#circle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Circle segment (RT Professional)](#circle-segment-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Circle segment (RT Professional)

##### Application

The "Circle segment" is a closed object that you can fill with a color or pattern. By default, a circle segment is a quarter circle. It can be customized as required.

![Application](images/2701784715_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. You can adapt the following properties in particular:

- Radius: Define the size of the circle segment.
- Start and end angle: Specify where the start and end angle lie on a virtual circle of 360°.

##### Radius

You define the radius of the "Circle segment" object in the Inspector window. Enter the value using Pixels as the unit.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value for "Radius" in the "Arc" area.

##### Define start and end angle

Determine the size of the circle segment using the "Start Angle" and "End Angle" attributes. Enter the values using Degrees as the unit.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter a value for "Start angle" and "End angle" in the "Radii" area.

##### Alternative procedure

You can also change the start and end points of the circle segment using the mouse.

1. Place the cursor on a start or end point of the circle segment. The start and end points are indicated by small blue squares.

   The mouse cursor changes to a cross.
2. Hold down the mouse button, and drag the start or end point to the desired position.

---

**See also**

[Circle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#circle-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Circular arc (RT Professional)](#circular-arc-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Criteria analysis view (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

The "Criteria analysis view" object shows you the operands with error in the user program that have triggered a selected ProDiag or GRAPH alarm. As a result, you have the option of seeing the list of operands with error in addition to the alarm in the same screen.

To see the evaluation of the criteria analysis in the "Criteria analysis view" object in Runtime, select the initial value acquisition in the settings of the function blocks in the user program. Initial value acquisition is available for GRAPH function blocks Version 4.0 and higher and ProDiag function blocks V2.0 and higher.

To enable the link to the corresponding error message, configure a reference to a previously configured alarm view. If you select a GRAPH alarm or a ProDiag alarm in the alarm view in Runtime, then the name, address, comment and value of the operand that caused this error is displayed in the criteria analysis view.

![Use](images/110724048523_DV_resource.Stream@PNG-en-US.png)

You see the incoming alarms and operands with error at a glance in Runtime if you configure the criteria analysis view and its linked alarm view in the same screen.

> **Note**
>
> Criteria analysis is only available for the user programs for which initial value acquisition has been activated.
>
> Activate initial value acquisition in the properties of the following blocks:
>
> - ProDiag function blocks with version greater than or equal to V2.0
> - GRAPH function blocks with version greater than or equal to V4.0

> **Note**
>
> The "Criteria analysis view" object is not available in the global screen.

##### Layout

You change the settings for the position, style, colors, and fonts of the object in the Inspector window.

##### Columns

The following columns are displayed in the criteria analysis view in Runtime.

| Column | Description |
| --- | --- |
| Symbol name | Symbolic name of the operand in the user program. |
| Address | Absolute address of the operand. |
| Comment | Additional comments from the user program in the language that is loaded into the controller. |
| Value | The value of the operand at the time of the error. |

##### Configuring the criteria analysis view

1. Move the criteria analysis view from the toolbox window using drag-and-drop.
2. Select "Properties > Properties > General" in the Inspector window.
3. Open the selection button under the "Tag" property.
4. Select the status tag of the corresponding alarm view.

   To enable linking to alarms, enter the tag for the criteria analysis for the configured alarm view under "Properties > Properties > Display".
5. In the Inspector window, select "Properties > Properties > Columns".
6. Select the columns that you require in the device view for Runtime.
7. Customize the headers and the width of the columns if necessary.

##### Configuring the criteria analysis view (RT Professional)

1. Move the criteria analysis view from the toolbox window using drag-and-drop.
2. Select "Properties > Properties > General" in the Inspector window.
3. Enter the name of the configured alarm view under "Data source".

##### Using the keyboard to operate the criteria analysis view

To operate the PLC code view with the keyboard, proceed as follows:

1. Press the <Tab> key repeatedly until the focus is on the desired button.

   Use <Shift + Tab> to navigate back to the previous button.
2. Press <Enter>.

   The command is executed.

---

**See also**

[Overview of initial value acquisition and criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#overview-of-initial-value-acquisition-and-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)
  
[Initial value acquisition and criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#initial-value-acquisition-and-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example of order of the criteria analysis (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-of-order-of-the-criteria-analysis-panels-comfort-panels-rt-advanced-rt-professional)

#### Trend view (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

The trend view is meant for the graphical representation of tag values from the current process or from a log in form of trends.

![Application](images/80126115979_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, color, and font types of the object. You can adapt the following properties in particular:

- Display value table, ruler and grid: Specifies whether a value table, a ruler or a grid is displayed in addition to the coordinate system to improve legibility.
- Toolbars: Defines the display of the operator controls.

##### Display value table, ruler and grid

For improved legibility a value table, a ruler and a grid can be displayed in Runtime.

1. Activate "Properties > Properties > Appearance > Show ruler".
2. Activate "Properties > Properties > Table > Show table".
3. Activate "Properties > Properties > Table > Show grid".

##### Toolbars

The layout of the operator controls is defined in the "Properties > Properties > Toolbar" inspector window.

> **Note**
>
> **Basic Panels**
>
> Because archiving with Basic Panels is only possible for devices as of the 2nd Generation, the operator controls are not available on all Basic Panels.

| Toolbar button | Brief description | Description |
| --- | --- | --- |
| ![Toolbars](images/102411264395_DV_resource.Stream@PNG-de-DE.png) | "Go to start" | Scroll to the current value of the trend. |
| ![Toolbars](images/102270138379_DV_resource.Stream@PNG-de-DE.png) | "Zoom in" | Reduces the displayed time slice. |
| ![Toolbars](images/61123900939_DV_resource.Stream@PNG-de-DE.png) | "Zoom out" | Zooms into the displayed time section. |
| ![Toolbars](images/61123904779_DV_resource.Stream@PNG-de-DE.png) | "Ruler backward" | Moves the ruler back. |
| ![Toolbars](images/61124817419_DV_resource.Stream@PNG-de-DE.png) | "Ruler forward" | Moves the ruler forward. |
| ![Toolbars](images/102411268235_DV_resource.Stream@PNG-de-DE.png) | "Backward" | Scrolls back by half of the display width. |
| ![Toolbars](images/102411284875_DV_resource.Stream@PNG-de-DE.png) | "Forward" | Scrolls forward by half of the display width. |
| ![Toolbars](images/61124821259_DV_resource.Stream@PNG-de-DE.png) | "Ruler" | Shows or hides the ruler. The ruler displays the X-value associated with a Y-value. |
| ![Toolbars](images/61124828939_DV_resource.Stream@PNG-de-DE.png)       ![Toolbars](images/61124825099_DV_resource.Stream@PNG-de-DE.png) | "Start/stop" | Stops trend recording or continues trend recording. |

##### Operation on Basic Panels and devices with small display size

The trend view buttons are not displayed on Basic Panels and HMI devices with a display size of less than 6". You can operate the trend view using the function keys of the HMI device that are assigned corresponding system functions.

##### Displaying column headers

The layout of the table in the trend view depends on the view settings in the Control Panel. Depending on the setting, the column headers might be truncated. This setting is found under "Display > Appearance" in the control panel. To display column headers correctly, set the display in "Windows and buttons" to "Windows Classic" style.

This behavior only occurs during configuration. The column headers are displayed correctly in Runtime.

##### Consistency test

If warnings or errors are displayed in the output window during a consistency check in connection with trend views, clicking "Go to Error/Tag" on the shortcut menu will not always take you to the exact error position. In some cases only the trend view is shown as cause of error.

##### Adding, configuring, and removing trends

The trends of the trend view are managed in the Inspector window under "Properties > Properties > Trend". You can copy trends between different trend views.

##### Notes on operating Comfort Panels

Zoom:

- The view is 100% for the first display of the trend view. You can zoom in the display. After you have zoomed into the display, the Zoom-out button is also displayed.
- After the very first opening of the trend view, you can zoom into the display up to 3 times.
- Each time you zoom in, the displayed time interval is halved. Example: The time interval on the X axis is 100 seconds. The time interval is 50 seconds after the first zoom-in, after the second zoom-in 25 seconds and so on. Accordingly, the time interval is doubled in the case of a zoom-out.
- When the view is zoomed-in to the maximum possible value, you can zoom out up to 6 times. Accordingly, you can zoom into the view up to 6 times after maximum zoom-out. The maximum possible values cannot be changed.
- The current zoom-in or zoom-out level cannot be saved.

Forward/backward funktion:

- You can always press the Backward button. Reducing the displayed time interval has no effect on the functionality of the Backward button.
- The Forward button only becomes active after you have pressed the backward button once.

---

**See also**

[Trends (Panels, Comfort Panels, RT Advanced)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#trends-panels-comfort-panels-rt-advanced)
  
[Configuring trend displays for values from the PLC (Panels, Comfort Panels, RT Advanced)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-trend-displays-for-values-from-the-plc-panels-comfort-panels-rt-advanced)
  
[Configure trend view (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-trend-view-rt-professional)
  
[Creating trends for the trend window. (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#creating-trends-for-the-trend-window-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Charge condition (Panels, Comfort Panels)

##### Application

The object "Charging condition" is a control element for some SIMATIC Mobile Panels. The "Charging condition" object indicates the charging status of the battery. Charge the battery in good time. Alternatively, you can replace the battery with a spare battery.

##### Layout

| Symbol | Description | Charging condition |
| --- | --- | --- |
| ![Layout](images/21132147723_DV_resource.Stream@PNG-de-DE.png) | Battery is charged | >20 % |
| ![Layout](images/21132150795_DV_resource.Stream@PNG-de-DE.png) | Battery must be charged | <20 % and >6 % |
| ![Layout](images/21132153867_DV_resource.Stream@PNG-de-DE.png) | Battery is weak | < 6 % |

##### Operation

The object is for display only and cannot be controlled by the operator.

---

**See also**

[WLAN reception (Panels, Comfort Panels)](#wlan-reception-panels-comfort-panels)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Illuminated pushbutton (Panels, Comfort Panels)

##### Application

The object "Illuminated pushbutton" is a control element for some SIMATIC Mobile Panels. The LEDs can be activated by the PLC. The illuminated LED signals the operator in Runtime that the illuminated pushbutton has to be pressed. The illuminated pushbutton is configured in the global screen.

![Application](images/52218064139_DV_resource.Stream@PNG-de-DE.png)

##### Layout

You can adapt the following properties in the Inspector window:

- Tag: Specifies the tag in which the status of the illuminated pushbutton is written.
- LED assignment: Specifies the assignment of the LED to the bit in the LED tag.

##### Tag

The "Tag" property is used to specify the global assignment of the "Illuminated pushbutton" object in the global screen.

> **Note**
>
> **Notes on configuring**
>
> The current status of the illuminated pushbutton is written to the tag when Runtime is started and whenever the button is pressed. This may cause inconsistencies between the status of the illuminated pushbutton and the illuminated pushbutton tags.
>
> Carry out the following configuration steps so that the illuminated pushbutton always reflects the actual state.
>
> 1. If the tag has a connection to the PLC, the current value is transferred from the PLC to the tag after establishment of communication. The tag that contains the current status of the key is overwritten by this process. The illuminated pushbutton tag may therefore no longer reflect the current value of the illuminated pushbutton, for example if the Mobile Panel is switched off while the illuminated pushbutton is pressed.
> 2. If the illuminated pushbutton is pushed before communication to the PLC could be established (for example after a device start-up), it may not be possible to send the value of the illuminated pushbutton tag to the PLC. In this case the value of the tag in the PLC is different from the current status of the key.

##### Basic procedure

1. Specify the connection to the PLC in the "Connections" editor. Activate the "Coordination" area pointer to ensure that the life bit is available to the PLC side.

   ![Basic procedure](images/83577579275_DV_resource.Stream@PNG-en-US.png)

   ![Basic procedure](images/83577579275_DV_resource.Stream@PNG-en-US.png)
2. Open the "HMI tags" editor and create three tags.

   - Internal tag: Pushbutton_State
   - External tag: BufferTag
   - External tag: Pushbutton_PLC
3. Open the Inspector window of the "Pushbutton_State" tag.
4. In the Inspector window, select "Properties > Events > Value change". Click the first line of the function list. The list opens, showing the system functions available in the project.
5. Select the "SetTag" system function.

   - Select the "Pushbutton_PLC" tag at "Tag (output)".
   - Select the "Pushbutton_State" tag at "Value".

     ![Basic procedure](images/72559058955_DV_resource.Stream@PNG-en-US.png)

     ![Basic procedure](images/72559058955_DV_resource.Stream@PNG-en-US.png)

     The value of the "Pushbutton_PLC" tag is written to the PLC with the "Pushbutton_PLC" tag. A program in the PLC evaluates the life bit. If communication is established, the current value is written to the "Pushbutton_PLC" tag from the PLC. The "BufferTag" is required to transfer the current position of the pushbutton to the PLC.
6. Open the Inspector window of the "BufferTag" tag.
7. In the Inspector window, select "Properties > Events > Value change".
8. Click the first line of the function list. The list opens, showing the system functions available in the project.
9. Select the "SetTag" system function.

   - Select the "Pushbutton_PLC" tag at "Tag (output)".
   - Select the "Pushbutton_State" tag at "Value".

     ![Basic procedure](images/77919852811_DV_resource.Stream@PNG-en-US.png)

     ![Basic procedure](images/77919852811_DV_resource.Stream@PNG-en-US.png)

   After establishing communication the current value is written to the "BufferTag" from the PLC. The "SetTag" system function is executed by the value change in the auxiliary tag. The system function re-allocates the value of the "Pushbutton_State" tag to the "Pushbutton_PLC" tag.
10. Open the global screen in the "Screen navigation" editor.
11. Select the illuminated key on the global screen.
12. Select the tag "Pushbutton_State" in "Properties > Properties > General > Settings >Tag" in the Inspector window.

    If you press the illuminated pushbutton, the value is written to the "Pushbutton_PLC" tag.

##### LED assignment

To actuate the LED an LED tag or an array tag must be set up in the PLC and specified as an LED tag during configuration. The LED tag is specified at "LED tag" in the "Settings" area in the "General" group. With "LED bit" the allocated bit is given. When the bit is set the following states of the LED can be realized in runtime.

| Bit n+1 | Bit n | LED function |
| --- | --- | --- |
| 0 | 0 | Off |
| 0 | 1 | Fast flash |
| 1 | 0 | Slow flash |
| 1 | 1 | On permanently |

---

**See also**

[Handwheel (Panels, Comfort Panels)](#handwheel-panels-comfort-panels)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Line (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Line" object is an open object. The line length and gradient slope are defined by the height and width of the rectangle enclosing the object.

![Application](images/56750884491_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. You can adapt the following properties in particular:

- Line style
- Line start and end

##### Line style

The representation of the line is specified under "Properties > Properties > Appearance" in the Inspector window. The line is shown without interruption if you select "Solid", for example.

> **Note**
>
> The line styles available depend on the selected HMI device.

##### Line start and end

The start and end points of the line are specified under "Properties > Properties > Appearance > Line ends" in the Inspector window.

Use arrow point, for example, as start and end point. The available start and end points depend on the device.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### List box (RT Professional)

##### Application

You use the "List box" object to present and select multiple list entries. You activate list entries by default so that the operator only changes the preset entry if necessary. If the list box is larger than the selection rectangle, WinCC automatically adds a scroll bar to the right margin.

To incorporate list fields into the process, dynamize the corresponding properties.

![Application](images/21175772299_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, style, colors and font type settings of the object. You can adapt the following properties in particular:

- Number of entries: Defines the number of list entries.
- Selection of entries: Defines which entry is displayed as activated by default.

##### Defining the number of entries

1. In the Inspector window, select "Properties > Properties > General".
2. Define the desired number of list entries under "Entries".

At the same time, the value of the "Entries" attribute specifies the upper limit for the "Index" property under "Label." Changing the value can have the following effects:

##### Changing the number

New fields are added under the field with the highest value for the "Index" property if you increase the number of entries. You can change the default label for the new field using the "Text" property under "Label."

All fields for which the value of the "Index" property is higher than the new number will be deleted if you reduce the number of entries.

##### Specifying the default setting of the list boxes

Specify which list entry is displayed as active with "Properties > Properties > General > Presetting enabled".

Each option is represented by a bit in a 32-bit word. To activate a field, the corresponding bit must have the value "1". The 32-bit word contains the information for all texts of the list of list boxes. The value of the "Selected fields" property is given in hexadecimal notation.

---

**See also**

[Combo box (RT Professional)](#combo-box-rt-professional)
  
[Configure operator input alarms (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-operator-input-alarms-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Media Player (Comfort Panels, RT Professional)

##### Use

In Runtime, the Media Player is used to play multimedia files.

![Use](images/88074754571_DV_resource.Stream@PNG-de-DE.png)

The Media Player is only available for the following devices:

- Comfort Panels
- RT Professional

> **Note**
>
> **Playing videos on Comfort Panels**
>
> You can play video sequences on Comfort Panels in the "Media Player" screen object. You can find more detailed information on playing videos on the Internet under:   
> [http://support.automation.siemens.com](http://support.automation.siemens.com/WW/view/en/62101921) (entry ID 62101921)

##### Layout

You can set the following properties in the Inspector window:

- Display status bar: Determines whether to display the status bar.
- Display operator controls: specifies the operator controls in Runtime.
- Show tracker: establishes, whether a slider is available for the operation.

##### Operator controls

The operator controls that can be used to control the Media Player in Runtime are specified in the Inspector window under "Properties > Properties > Appearance > Elements".

##### Number of replays (Comfort Panels)

To play the file multiple times, select number of playbacks under "Properties > Properties > General > Number of replays". Select a value from 0 to 2,147,483,647.

##### Supported file formats (Comfort Panels)

The following audio formats are supported by Media Player:

- Moving Picture Experts Group standard 1, Layer 1, 2, 3 (.mpa, .mp2, .mp3)
- Waveform Audio (.wav)

The following video formats are supported by Media Player:

- Moving Picture Experts Group standard 1 (.mpg, .mpeg, .mpv, .mpe)
- Advanced Streaming Format (.asf)
- Windows Media Video Format (.wmv)
- Audio-Video Interleaved (.avi)

> **Note**
>
> Media Player does not support the creation and management of favorites. If you create favorites before closing the Media Player, they will not reappear when you open it again.

> **Note**
>
> The Media Player cannot be operated using the keyboard.
>
> You cannot simulate the Media Player. A static screen appears in the simulation window instead of the Media Player.

##### Supported file formats (RT Professional)

The following file formats are supported by Media Player:

- graphics file formats (.gif, .bmp, .jpg, .jpeg, .png)
- Moving Picture Experts Group standard 1 (.mpg, .mpeg, .mp4)
- QuickTime Movie (.mov, .qt)
- Advanced Streaming Format (.asf)
- Windows Media Video Format (.wmv)
- Audio Video Interleave (.avi)

> **Note**
>
> **Requirements for video files**
>
> To play video files in the Windows Server 2008 R2 SP1 and 2012 R2, install the Microsoft feature "Desktop Experience". You will find more detailed information on this topic on the Internet in the Microsoft documentation.

> **Note**
>
> Playing back multimedia files in the control depends on the video and audio codecs installed on the PC, as well as on the file format.

> **Note**
>
> **Data loss when copying the project**
>
> If you copy the project to another PC, keep the following in mind:
>
> Files indicated in the WinCC Media Control are not copied along with the other files if they are dynamically linked and no UNC path is specified. You have to load the files into the project again.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Alarm view (RT Professional)

##### Use

The "Alarm view" object displays alarms that occur during the process in a plant. You also use the alarm view to visualize alarms in list format. WinCC offers various views, such as "Current alarms" or "Historical alarm list" (short-term).

![Use](images/104328652171_DV_resource.Stream@PNG-en-US.png)

##### Layout

You change the settings for the position, geometry, style, color, and font of the object in the Inspector window. You can adapt the following properties in particular:

- Operator controls: Defines the operator controls of the alarm view.
- Status bar: Defines the elements in the status bar.
- Time base: Defines the time basis used to output the alarms.
- AutoScroll: Defines whether it is always the latest alarm that is selected in the alarm view.
- Text format: Defines the font and font size.
- Sorting: Defines whether and how the alarms can be sorted in Runtime.
- Table: Defines the properties of the table in the alarm view.
- Loop-In-Alarm: Specifies whether double-clicking an alarm triggers the configured screen change.

  > **Note**
  >
  > The "alarm view" object cannot be grouped.
  >
  > You only configure a script at the "Incoming" event

##### Configuring output of alarms

- Selection of displays and filters: Defines which alarms are displayed in this alarm view.
- Alarm statistics: Activates the display of a statistical overview for the display duration and frequency of the alarms.
- Print: This setting defines which print job is used for the alarm view.

##### Operator controls

You define the control elements of the alarm view in Runtime, and their operator authorizations, under "Properties > Properties > Toolbar" in the inspector window. The following control elements are available for the alarm view:

| Button |  | Function |
| --- | --- | --- |
| ![Operator controls](images/21867060875_DV_resource.Stream@PNG-de-DE.png) | Display "Current alarms" | Shows the currently active alarms. |
| ![Operator controls](images/21864489099_DV_resource.Stream@PNG-de-DE.png) | Display "Historical alarm list" (short-term) | Shows the logged and currently active alarms. |
| ![Operator controls](images/21864492555_DV_resource.Stream@PNG-de-DE.png) | Display "Historical alarm list" (long-term) | Shows the logged alarms. |
| ![Operator controls](images/21867068043_DV_resource.Stream@PNG-de-DE.png) | Display "Locked alarms" | Shows all locked alarms in the system. |
| ![Operator controls](images/21863635211_DV_resource.Stream@PNG-de-DE.png) | Display "Alarm statistics" | Displays a statistical overview for the display duration and frequency of the alarms. |
| ![Operator controls](images/21864881803_DV_resource.Stream@PNG-de-DE.png) | "Alarm annunciator acknowledgment" | Acknowledges a visual, or audible signaling device. |
| ![Operator controls](images/21865909259_DV_resource.Stream@PNG-de-DE.png) | "Single acknowledgment" | Acknowledges an individual alarm. |
| ![Operator controls](images/21866163339_DV_resource.Stream@PNG-de-DE.png) | "Group acknowledgment" | Acknowledges all active visible alarms in the alarm view that require acknowledgment, unless they are subject to single acknowledgment. |
| ![Operator controls](images/26451542027_DV_resource.Stream@PNG-de-DE.png) | "Autoscroll" | Defines whether it is always the latest alarm that is selected in the alarm view. The visible area of the alarm view moves, if necessary.   You can only select individual alarms if "Autoscroll" is not active. |
| ![Operator controls](images/21863628043_DV_resource.Stream@PNG-de-DE.png) | "Filter" | Opens a dialog for filtering alarms in the alarm view. Even alarms that are not displayed in the filtered view will be logged. |
| ![Operator controls](images/26451545867_DV_resource.Stream@PNG-de-DE.png) | "Display Options" dialog | Opens a dialog for defining which alarms are displayed in the alarm view.   If the "All alarms" option is selected, the alarm view displays both hidden, and visible alarms.  If the "Visible alarms" option is activated, the alarm view contains only visible alarms.  If the "Hidden alarms" option is activated, the alarm view contains only hidden alarms. |
| ![Operator controls](images/21867543179_DV_resource.Stream@PNG-de-DE.png) | "Lock dialog" | Opens a dialog for locking alarms. Any alarms that meet these criteria are neither displayed, nor logged. |
| ![Operator controls](images/26440258699_DV_resource.Stream@PNG-de-DE.png) | "Print alarm report" | Prints the alarm report that is configured for the alarm view. |
| ![Operator controls](images/44734647691_DV_resource.Stream@PNG-de-DE.png) | "Print current view" | Starts printing the alarms displayed in the alarm view. |
| ![Operator controls](images/26440099979_DV_resource.Stream@PNG-de-DE.png) | "Emergency acknowledgment" | Applies emergency acknowledgment to an alarm that requires acknowledgment. The acknowledgment bit for an alarm is sent directly to the AS, even if the alarm is not active. |
| ![Operator controls](images/26440103819_DV_resource.Stream@PNG-de-DE.png) | "First alarm" | Selects the first of the active alarms. The visible area of the alarm view moves, if necessary. This button can only be used if the "Autoscroll" function is disabled. |
| ![Operator controls](images/26440107659_DV_resource.Stream@PNG-de-DE.png) | "Last alarm" | Selects the last of the active alarms. The visible area of the alarm view moves, if necessary. This button can only be used if the "Autoscroll" function is disabled. |
| ![Operator controls](images/26440111499_DV_resource.Stream@PNG-de-DE.png) | "Next alarm" | Selects the next alarm in relation to the currently selected alarm. The visible area of the alarm view moves, if necessary. This button can only be used if the "Autoscroll" function is disabled. |
| ![Operator controls](images/26440243339_DV_resource.Stream@PNG-de-DE.png) | "Previous alarm" | Selects the previous alarm in relation to the currently selected alarm. The visible area of the alarm view moves, if necessary. This button can only be used if the "Autoscroll" function is disabled. |
| ![Operator controls](images/26440247179_DV_resource.Stream@PNG-de-DE.png) | "Infotext dialog" | Opens a dialog to display an infotext. |
| ![Operator controls](images/26440251019_DV_resource.Stream@PNG-de-DE.png) | "Comment dialog" | Opens a text editor where you can enter comments.  This button is not available in the alarm view unless the "Historical alarm list (long-term)" display is displayed. |
| ![Operator controls](images/26440254859_DV_resource.Stream@PNG-de-DE.png) | "Loop-In-Alarm" | If a screen change is configured, the display switches to a screen containing information about the alarm. |
| ![Operator controls](images/22575032971_DV_resource.Stream@PNG-de-DE.png) | "Unlock alarm" | Unlocks an alarm in the display "Locked alarms." |
| ![Operator controls](images/22575029515_DV_resource.Stream@PNG-de-DE.png) | "Lock alarm" | Locks an alarm in the current alarm list, and in the alarm log lists. The alarm is added to the display "Locked alarms." |
| ![Operator controls](images/26440262539_DV_resource.Stream@PNG-de-DE.png) | "Sort dialog" | Opens a dialog for setting user-defined sort criteria for the displayed alarms. |
| ![Operator controls](images/26440317579_DV_resource.Stream@PNG-de-DE.png) | "Time base dialog" | Opens a dialog for selecting the time base for the time data displayed in alarms. |
| ![Operator controls](images/21867536011_DV_resource.Stream@PNG-de-DE.png) | "List of hidden alarms" | Opens the display "Hidden alarms." |
| ![Operator controls](images/21863962379_DV_resource.Stream@PNG-de-DE.png) | "Hide alarms" | Suppresses the display of an alarm in the displays "Current alarms", "Historical alarm list (short-term)" or "Historical alarm list (long-term)." The alarm is added to the display "Hidden alarms." |
| ![Operator controls](images/21863965835_DV_resource.Stream@PNG-de-DE.png) | 'Show alarm" | Shows in the display "Hidden alarms" again an alarm in the displays "Current alarms", "Historical alarm list (short-term)" or "Historical alarm list (long-term)." The alarm is removed from to the display "Hidden alarms." |

##### Status bar

You define which of the elements of the status bar are displayed using "Properties > Properties > Status bar" from the Inspector window. The following display elements are available for the alarm view:

| Button | Function |
| --- | --- |
| Date | System date |
| Time of day | System time |
| ![Status bar](images/21867543179_DV_resource.Stream@PNG-de-DE.png) | Lock is set. |
| ![Status bar](images/21863628043_DV_resource.Stream@PNG-de-DE.png) | A filter is activated. |
| List: | Number of current alarms |
| Window: | Number of alarms in the window |
| Ackn: | Number of active alarms requiring acknowledgment |

##### Access protection in Runtime

Configure access protection under "Properties > Properties > Security" in the Inspector window. If a logged-on user has the required authorization, he can acknowledge, and edit alarms using the control elements in the alarm view.

The logon dialog box is displayed in the following cases:

- The logged-on user attempts to process the alarm but does not have the required authorization.
- A user attempts to process an alarm while no user is logged on.

##### Set timebase

1. In the Inspector window, select "Properties > Properties > General".
2. Select the required timebase under "Properties > Properties > Miscellaneous > Time base."
3. Under "Time-based standard sort", define whether the alarms are sorted in ascending or descending order in Runtime.

##### Enable Autoscroll

1. In the Inspector window, activate "Properties > Properties > Layout > Window > Autoscroll".

##### Define text format

To format the alarm text:

1. In the Inspector window, select "Properties > Properties > Text format".
2. Click the "..." button in the "Font" area.

   A dialog opens.
3. Select the font and size in the dialog.

##### Set up sort order

1. In the Inspector window, select "Properties > Properties > Columns".

   ![Set up sort order](images/88083730315_DV_resource.Stream@PNG-en-US.png)

   ![Set up sort order](images/88083730315_DV_resource.Stream@PNG-en-US.png)
2. Select sort criteria and sorting order.

##### Set to a table in the alarm view

1. Click "Properties > Properties > Table font" in the Inspector window.
2. Define settings for the rows and cells in the "Table body" area.

   - "Optimum line height" activated: The font is aligned to the height of the line.
   - "Truncate cell contents": If the text is longer than the cell, the text is displayed truncated.
3. In the "Line numbering" area, define whether each row has a header.
4. Select the column header layout from the "Column headers" area.

##### Set Loop-In-Alarm

1. In the Inspector window, click "Properties > Properties > Miscellaneous".
2. Activate the "Loop-In-Alarm with double-click" option.

##### Displaying column headers

The layout of the alarm view is dependent on the view settings in the control panel. Depending on the setting, the column headers may be truncated. This setting is available in the Control Panel, "Display" > "Appearance" tab. To display column headers correctly, set the display in "Windows and buttons" to "Windows Classic" style.

This behavior only occurs during configuration. The column headers are displayed correctly in Runtime.

---

**See also**

[Configuring an alarm view for active alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-an-alarm-view-for-active-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring persistence (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-persistence-rt-professional)
  
BackColor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Alarm view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Use

Advanced alarm view is used to display alarms on the HMI device.

On HMI devices with device version V13 or later, the advanced table-based alarm view is available for managing alarms.

![Use](images/65174580491_DV_resource.Stream@PNG-en-US.png)

##### Alarm line

The alarm line allows display of the most current pending alarm in Runtime. The following figure shows an alarm line:

![Alarm line](images/6324796043_DV_resource.Stream@PNG-en-US.png)

How to configure the alarm line:

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select "Mode > Alarm line".

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object.

> **Note**
>
> The fonts available for selection depend on the fonts you have configured in the Runtime settings under "Language & font" and the fonts supported by your HMI device.

You can adapt the following properties in particular:

- Toolbar: Defines the operator controls of the alarm view.
- Alarm classes: This setting defines which alarm classes are displayed in the alarm view.
- Columns: Specifies the displayed columns in Runtime.
- Columns moveable: Specifies whether the sequence of columns can be changed in Runtime.
- Identification of alarm classes: To be able to distinguish various alarm classes, they are identified in the first column of the alarm view.
- Filter: Defines that only alarms which contain a specific character string in the alarm text will be displayed.
- Define display area: This setting specifies the date from which alarms are displayed in the alarm view.
- Sorting by date/time possible: Specifies whether the alarms can be sorted in Runtime by date and time.

  > **Note**
  >
  > If you have different alarm classes output, these will be initially sorted into alarm classes in Runtime, and then by the time at which the alarm occurred.

##### Operator controls

The operator controls that can be used to control the alarm view in Runtime are specified in the Inspector window under "Properties > Properties > Toolbar". The following table shows the operator controls in the alarm view and their function:

| Button | Name | Function |
| --- | --- | --- |
| ![Operator controls](images/64016834699_DV_resource.Stream@PNG-de-DE.png) | "Info text" | Displays a tooltip for an alarm. |
| ![Operator controls](images/64009030411_DV_resource.Stream@PNG-de-DE.png) | "Acknowledge" | Acknowledges an alarm. |
| ![Operator controls](images/64016843147_DV_resource.Stream@PNG-de-DE.png) | "Loop-in-alarm" | Executes the configured function (for example: "ActivateScreen") with each keystroke. It is hereby possible to call a screen containing your information about the selected alarm.  Also acknowledges an alarm requiring acknowledgment. <sup>1)</sup> |

<sup>
1)</sup> Only if a function is configured for the selected alarm for the "loop-in-alarm" event.

##### Select alarm classes

1. Click "Properties > Properties > General" in the Inspector window.
2. Under "Alarm classes", activate the alarm classes to be displayed in the alarm view in Runtime.

##### Access protection in Runtime

You can configure access protection in the "Properties > Security" group in the properties of the alarm view. A logged-on user with the required authorization can acknowledge and edit alarms using the operator controls in the alarm view. If the logged-on user does not have the required authorization, or if no user is logged in, pressing the "Acknowledge" or "Edit" buttons or double-clicking an alarm line opens the logon dialog.

##### Define columns

Define the columns to be displayed in the alarm view in Runtime in the Inspector window.

1. In the Inspector window, select "Properties > Properties > Columns".
2. Activate the columns that are to be displayed in Runtime under "Visible columns".

##### Sequence of columns

If this property is enabled, the column sequence in the alarm view can be changed in Runtime.

1. In the Inspector window, select "Properties > Properties > Columns".
2. Select "Column properties > Columns moveable".

##### Sorting

If this property is enabled, the alarms displayed in the alarm view in Runtime can be sorted by date and time.

1. In the Inspector window, select "Properties > Properties > Columns".
2. Select "Column properties > Sorting by date/time possible".

##### Filter alarms

This property is used to define that only alarms that contain a configured string in the alarm text will be displayed in Runtime for the extended alarm view.

1. In the Inspector window, select "Properties > Properties > Filter".
2. In the "Filter string" field, enter the desired term for filtering.   
   Alternatively, you can configure a filter tag using the "Filter tag" field. The contents of the filter tag serve as the filter criterion in Runtime.

##### Identify alarm classes

An icon is displayed in the first column of the alarm view. This symbol allows the alarm to be allocated to an alarm class.

1. In the Inspector window, select "Properties > Properties > Columns".
2. Select "Visible columns > Alarm class name".
3. Open the "HMI alarms" editor and click on the "Alarm classes" tab.
4. Specify an icon for use to identify the alarms of this alarm class for an alarm class in the "Display name" column.

**Note**

The "alarm view" object cannot be grouped.

##### Set colors for alarm classes

You have the option of having alarms of selected alarm classes shown in different colors in Runtime. You set the background colors of the alarms in the "HMI alarms" editor.

1. Open the "HMI alarms" editor and click on the "Alarm classes" tab.
2. Set the colors for alarms under "Properties > Properties > Colors".
3. Depending on the HMI device, also change the flashing characteristics if required.
4. To show alarms in the alarm view in the defined colors, activate the option "Alarm class colors" under "Runtime settings > Alarms > General".

##### Define display area

You select a tag which defines the time from which alarms should be displayed. The following data types are permitted:

- External tags: Date, Date_and_Time, Time_of_Day
- Internal tags: DateTime

To define the display area, proceed as follows:

1. Click "Properties > Properties > Display" in the Inspector window.
2. Define the tag in which the time is specified under "Control tag for display area".

##### Switch to PLC code view

You configure the "ActivatePLCCodeView" system function on a button to enable the jump from a monitoring alarm in the display to the affected program code in the PLC code view. In the alarm view, you define a control tag that you use to give the button dynamic properties. Control tag is used to evaluate whether the entry point of the selected monitoring signal is possible in the PLC code view. To define the control tag, proceed as follows:

1. Click "Properties > Properties > Display" in the Inspector window.
2. Specify a Boolean tag under "Properties > Display > Control tag for PLC code view" that will control the jump from the last active ProDiag alarm or GRAPH alarm to the PLC code view.

You have the option make the button dynamic using animations, for example, so that the button changes color with an incoming alarm.

##### Displaying column headers

The layout of the alarm view is dependent on the view settings in the control panel. Depending on the setting, the column headers may be truncated. This setting is found under "Display > Layout tab" in the control panel. To display column headers correctly, set the display in "Windows and buttons" to "Windows Classic" style.

This behavior only occurs during configuration. The column headers are displayed correctly in Runtime.

---

**See also**

BackColor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Alarm view, simple (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Use

Alarms are indicated in the Alarm view or in the Alarm window of the HMI device.

The following screen contains a simple alarm view:

![Use](images/6324736523_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> The "Single alarm view" object cannot be operated dynamically with a script.

> **Note**
>
> Configure the "Simple alarm view" object on devices with device version 12.0.0.0 or older.

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object.

> **Note**
>
> The fonts available for selection depend on the fonts you have configured in the Runtime settings under "Language & font" and the fonts supported by your HMI device.

You can adapt the following properties in particular:

- Operator controls: Defines the operator controls of the alarm view.
- Alarm classes: This setting defines which alarm classes are displayed in the alarm view.
- Columns: Specifies the displayed columns in Runtime.

  > **Note**
  >
  > If you have different alarm classes output, these will be initially sorted into alarm classes in Runtime, and then by the time at which the alarm occurred.

##### Operator controls

The operator controls that can be used to control the alarm display in Runtime are specified in the Inspector window under "Display > Settings". The following table shows the operator controls in the alarm view, and what they do:

| Button |  | Function |
| --- | --- | --- |
| "Info text" | ![Operator controls](images/77905955211_DV_resource.Stream@PNG-de-DE.png) | Displays info text for an alarm. |
| "Acknowledge" | ![Operator controls](images/77905963019_DV_resource.Stream@PNG-de-DE.png) | Acknowledges an alarm. |
| "Loop-In-Alarm" | ![Operator controls](images/77906367883_DV_resource.Stream@PNG-de-DE.png) | Executes the configured function (for example: "ActivateScreen") with each keystroke. It is hereby possible to call a screen containing your information about the selected alarm.  Also acknowledges an alarm requiring acknowledgment. <sup>1)</sup> |

<sup>
1)</sup> Only if a function is configured for the selected alarm for the "loop-in-alarm" event.

##### Select alarm classes

1. Click "Properties" in the Inspector window.
2. Under "Alarm classes", activate the alarm classes to be displayed in the alarm view in Runtime.

##### Define columns

Define the columns to be displayed in the alarm view in Runtime in the Inspector window.

1. In the Inspector window, click "Properties > Columns".
2. Activate the columns that are to be displayed in Runtime under "Columns".

##### Displaying column headers

The layout of the alarm view is dependent on the view settings in the control panel. Depending on the setting, the column headers may be truncated. This setting is found under "Display > Layout tab" in the control panel. To display column headers correctly, set the display in "Windows and buttons" to "Windows Classic" style.

This behavior only occurs during configuration. The column headers are displayed correctly in Runtime.

> **Note**
>
> In the engineering system, you can dynamically control the visibility of an object, for example, in the "Animations" group of the Inspector window. In Runtime, the "Simple alarm view" does not support animations. If you have configured an animation and, for example, wish to perform a consistency check of the project, then an error alarm is issued in the Output window.

#### Alarm view, advanced (Panels, Comfort Panels, RT Advanced)

##### Alarm view

Alarms are indicated in the Alarm view or in the Alarm window of the HMI device. The following screen contains an alarm view with no content:

![Alarm view](images/6324617227_DV_resource.Stream@PNG-en-US.png)

##### Alarm line

The alarm line allows display of the most current pending alarm in Runtime. The following figure shows an alarm line:

![Alarm line](images/6324796043_DV_resource.Stream@PNG-en-US.png)

How to configure the alarm line:

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select "Mode > Alarm line".

##### Changing the view type

On HMI devices with a display size larger than 6 ", you can configure both the advanced alarm view and a simplified alarm view. The view type is only available for configuration on devices up to device version V13.

![Changing the view type](images/6324736523_DV_resource.Stream@PNG-de-DE.png)

Proceed as follows to configure the simplified alarm view:

1. Click "Properties > Properties > Layout > Mode" in the Inspector window.
2. Select "Simplified".

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object.

> **Note**
>
> The fonts available for selection depend on the "Language and fonts" you have configured in the device settings and the fonts your HMI device supports.

You can adapt the following properties in particular:

- Operator controls: Defines the operator controls of the alarm view.
- Alarm classes: This setting defines which alarm classes are displayed in the alarm view.
- Columns: Specifies the displayed columns in Runtime.
- Sequence of columns: Specifies whether the sequence of columns can be changed in Runtime.
- Identification of alarm classes: To be able to distinguish various alarm classes, they are identified in the first column of the alarm view.
- Filter: Defines that only alarms that contain a specific character string in the alarm text will be displayed.
- Enable sorting: Specifies whether the alarms can be sorted in Runtime by date and time.
- Define display area: This setting specifies the date from which alarms are displayed in the alarm view.

  > **Note**
  >
  > If you have different alarm classes output, these will be initially sorted into alarm classes in Runtime, and then by the time at which the alarm occurred.

##### Operator controls

The operator controls that can be used to control the alarm view in Runtime are specified in the Inspector window under "Properties > Properties > Display > Settings". The following table shows the operator controls in the alarm view, and what they do:

| Button |  | Function |
| --- | --- | --- |
| "Tooltip" | ![Operator controls](images/77905955211_DV_resource.Stream@PNG-de-DE.png) | Displays a tooltip for an alarm. |
| "Acknowledge" | ![Operator controls](images/77905963019_DV_resource.Stream@PNG-de-DE.png) | Acknowledges an alarm. |
| "Loop-In-Alarm" | ![Operator controls](images/77906367883_DV_resource.Stream@PNG-de-DE.png) | Executes the configured function (e.g.: "ActivateScreen") whenever a key is pressed. This enables a screen that contains your information on the selected alarm to be called.  Also acknowledges an alarm that requires acknowledgment. <sup>1)</sup> |

<sup>
1)</sup> Only if a function is configured for the selected alarm for the event "Loop-In-Alarm".

##### Select alarm classes

1. Click "Properties > Properties > General" in the Inspector window.
2. Under "Alarm classes", activate the alarm classes to be displayed in the alarm view in Runtime.

##### Access protection in Runtime

Configure access protection in the "Properties > Security" group in the properties of the alarm view. If a logged-on user has the required authorization, he can acknowledge and edit alarms using the operator controls in the alarm view. If the logged-on user does not have the required authorization, or if no user is logged in, pressing the "Acknowledge" or "Edit" buttons or double-clicking an alarm line opens the logon dialog.

##### Define columns

Define the columns to be displayed in the alarm view in Runtime in the Inspector window.

1. In the Inspector window, select "Properties > Properties > Columns".
2. Activate the columns that are to be displayed in Runtime under "Columns".

##### Sequence of columns

If this property is enabled, the column sequence in the alarm view can be changed in Runtime.

1. In the Inspector window, select "Properties > Properties > Columns".
2. Select "Column properties > Column order".

##### Enable sorting

If this property is enabled, the alarms displayed in the alarm view in Runtime can be sorted by date and time.

1. In the Inspector window, select "Properties > Properties > Columns".
2. Select "Column properties > Sorting by date/time possible".

##### Filter alarms

This property is used to define that only alarms that contain a configured string in the alarm text will be displayed in Runtime for the extended alarm view.

1. In the Inspector window, select "Properties > Properties > Filter".
2. Enter the required term for filtering in the field "Filter string".  
   Alternatively, you configure a filter tag using the field "Filter tag". The contents of the filter tag serve as the filter criterion in Runtime.

##### Identify alarm classes

An icon is displayed in the first column of the alarm view. This symbol allows the alarm to be allocated to an alarm class.

1. In the Inspector window, select "Properties > Properties > Columns".
2. Select "Columns > Alarm class".
3. Open the "Alarms" editor, and click the "Alarm classes" tab.
4. Specify an icon for use to identify the alarms of this alarm class for an alarm class in the "Display name" column.

**Note**

The "alarm view" object cannot be grouped.

##### Specifying colors for alarm classes

You have the option to display alarms of the selected alarm classes in different colors in Runtime. You specify the background colors of the alarms in the "HMI alarms" editor.

1. Open the "HMI alarms" editor, and click the "Alarm classes" tab.
2. Define the colors for alarms under "Properties > Properties > Colors".
3. To show alarms in the alarm view in the defined colors, activate the option "Alarm class colors" under "Runtime settings > Alarms > General".

##### Define display area

You select a tag which defines the time from which alarms should be displayed. The following data types are permitted:

- External tags: Date, Date_and_Time, Time_of_Day
- Internal tags: DateTime

To define the display area, proceed as follows:

1. Click "Properties > Properties > Display" in the Inspector window.
2. Define the tag in which the time is specified under "Control tag for the display area".

##### Configuration behavior

**Displaying column headers**

The layout of the alarm view is dependent on the view settings in the control panel. Depending on the setting, the column headers may be truncated. This setting is found under "Display > Layout tab" in the control panel. To display column headers correctly, set the display in "Windows and buttons" to "Windows Classic" style.

This behavior only occurs during configuration. The column headers are displayed correctly in Runtime.

##### Displaying the buttons for operation

The display of the buttons for using the alarm view depends on the configured size. You should check on the HMI device whether all necessary buttons are available.

---

**See also**

[Alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
  
[Alarm indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-indicator-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm view for active alarms (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-an-alarm-view-for-active-alarms-basic-panels-panels-comfort-panels-rt-advanced)
  
BackColor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Use

Alarms are indicated in the Alarm view or in the Alarm window of the HMI device. The layout and operation of the Alarm window are similar to that of the Alarm view. The Alarm window has the following characteristics that are the same as in the Alarm view:

- Alarm window
- Alarm line: The alarm line is not available on Basic Panels.

The Alarm window is configured in the "Global screen" editor.

The alarm window is not assigned to any screen. Depending on the configuration the alarm window is opened when an alarm that belongs to a specific alarm class is active. Based on the configuration, it is not closed until the alarm is acknowledged.

![Use](images/74900880139_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> In the engineering system you dynamize, for example, the visibility of an object in "Properties > Animations" in the inspector window. In Runtime, the "Simple alarm window" object does not support animations. If you have configured an animation and, for example, wish to perform a consistency check of the project, then an error alarm is issued in the Output window.

##### Simple alarm window

The simple alarm window is available on Basic Panels with a device version prior to V13 to display the alarms.

![Simple alarm window](images/65960565899_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You configure the Alarm window in the same way as the Alarm view. In addition you adapt the following properties:

- Fixed alarm window: Specifies that the Alarm window retains the focus after a screen change.
- Window: You define the operator input and response of the Alarm window in Runtime.

  > **Note**
  >
  > If you have different alarm classes output, these will be initially sorted into alarm classes in Runtime, and then by the time at which the alarm occurred.

##### Operator controls

The operator controls that can be used to control the alarm view in Runtime are specified in the inspector window under "Properties >Display > Settings". The following table shows the operator controls in the Alarm window, and what they do:

| Button |  | Function |
| --- | --- | --- |
| "Tooltip" | ![Operator controls](images/77905955211_DV_resource.Stream@PNG-de-DE.png) | Displays a tooltip for an alarm. |
| "Acknowledge" | ![Operator controls](images/77905963019_DV_resource.Stream@PNG-de-DE.png) | Acknowledges an alarm. |
| "Loop-In-Alarm" | ![Operator controls](images/77906367883_DV_resource.Stream@PNG-de-DE.png) | Executes the configured function (for example: "ActivateScreen") with each keystroke. It is hereby possible to call a screen containing your information about the selected alarm.  Also acknowledges an alarm requiring acknowledgment. <sup>1)</sup> |

<sup>
1)</sup> Only if a function is configured for the selected alarm for the "loop-in-alarm" event.

##### Access protection in Runtime

Configure access protection under "Properties > Properties > Security" in the inspector window of the alarm view. If a logged-on user has the required authorization, he can acknowledge and edit alarms using the operator controls in the alarm view. If the logged-in user does not have the required authorization, or if no user is logged in, clicking the "Acknowledge" or "Edit" buttons or double-clicking an alarm line opens the login dialog box.

> **Note**
>
> **Basic Panels**
>
> Access protection is not available for Basic Panels.

##### Activating the focus of the Alarm window

Select the following option so that the Alarm window does not lose the focus after a screen change:

1. In the Inspector window, select "Properties > Properties > Mode".
2. Enable "Label".

##### Window

Define the response of the Alarm window under "Properties > Properties > Mode > Window" in the inspector window. The following table shows the possible properties:

| Option | Function |
| --- | --- |
| Automatic display | The Alarm window is automatically displayed when a system event occurs, for example. |
| Closable | The window closes again after a set time has elapsed. You define the display duration in the alarm settings. |
| Modal | The alarm window is linked to a confirmation, e.g. the alarm must be acknowledged. If the modal alarm window has the focus, the buttons in the screen behind it cannot be used. The functions configured on a function key are carried out. |
| Sizeable | You can change the size of the Alarm window in Runtime. |

---

**See also**

[Alarm view, advanced (Panels, Comfort Panels, RT Advanced)](#alarm-view-advanced-panels-comfort-panels-rt-advanced)
  
[Alarm indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-indicator-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-an-alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
  
Layer (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)
  
BackColor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Alarm indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

The alarm indicator is a graphic symbol that shows current errors or errors that need to be acknowledged, depending on the configuration. The alarm indicator is configured in the "Global screen" editor. The following figure shows an alarm indicator:

![Application](images/90667213707_DV_resource.Stream@PNG-de-DE.png)

##### Alarm classes

You define which alarm classes are shown with an alarm indicator in "General > Alarm classes" in the Inspector window. Alarm classes, such as "Warnings" or "Errors".

##### Define operator control in Runtime

1. Select the alarm indicator in the screen.
2. Click "Events > Click" or "Click when flashing" in the Inspector window.
3. The "function list" opens. Click the first line of the function list. The list of system functions, and scripts available in the project opens.
4. Select the "ShowAlarmWindow". system function under "Alarms."
5. Under "object name" select the name of the Alarm window from the selection list. Under "Layout", define whether the Alarm window should be visible, hidden, or should toggle between the two states.

---

**See also**

[Alarm view, advanced (Panels, Comfort Panels, RT Advanced)](#alarm-view-advanced-panels-comfort-panels-rt-advanced)
  
[Alarm window (Basic Panels, Panels, Comfort Panels, RT Advanced)](#alarm-window-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring an alarm indicator (Basic Panels, Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-an-alarm-indicator-basic-panels-panels-comfort-panels-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Option buttons (RT Professional)

##### Application

You use the "Option button" object to display, and select various options. Only one of these options can be selected respectively by the operator. Enable one of the options by default so that the operator only changes the default value if necessary. To incorporate an option button into the process, dynamize the corresponding attribute.

![Application](images/88159143307_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you can customize the settings for the object position, geometry, style, frame and color. You can adapt the following properties in particular:

- Number of fields
- Selection of the fields: Specifies which fields are displayed as activated.

##### Specifying the number of fields

You specify the number of fields in the Inspector window:

1. Click "Properties > Properties > General" in the inspector window.
2. Define the desired number of fields in the area "Label > Number of fields".

The value of the "Number of fields" property also indicates the upper limit value for the "Index" property. Changing the value can have the following effects:

- Increasing the number of fields

  New fields are added under the field with the highest value of the "Index" property. The standard label of the new field is changed with "Font > Text".
- Decreasing the number of fields

  All fields for which the value of the "Index" property is greater than the new number are removed.

##### Specifying the default setting of the option buttons

The "Default" property is used to specify which of the fields of the option buttons are to be displayed as active. If the default setting for the field is that it is to be activated, activate the "Default" field under "General" in the table row. Only one field may be activated at any time.

---

**See also**

[Check box (RT Professional)](#check-box-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### PDF view (Panels, Comfort Panels, RT Advanced)

##### Use

Using the object "PDF view" you project a PDF view on which the operator can open and display documents in PDF format in runtime. The documents in PDF format are located in the internal or external memory of the respective HMI device in this case.

The PDF view supports PDF versions 1.0 to 1.7. The search function is supported for PDF versions 1.4 to 1.7.

![Use](images/89631768971_DV_resource.Stream@PNG-de-DE.png)

You can configure the PDF view in the following:

- In a screen
- In a template
- In a slide-in screen
- In a pop-up screen

> **Note**
>
> The "PDF view" object can be configured multiple times in a project. However, a maximum of one PDF view can be active at the same time.

> **Note**
>
> **Device dependency of the "PDF view" object**
>
> The "PDF view" object is only available for KTP Mobile Panels, Comfort Panels and RT Advanced.

> **Note**
>
> Only one "PDF view" object can be inserted per screen.

##### Layout

You provide information about the position and size of the PDF view in the Inspector window. You can adapt the following properties in particular:

- File name: Specifies the PDF file that opens by default in the PDF view.
- File name tag: Specifies the tag that opens any PDF file.
- Toolbar: Specifies the buttons of the toolbar. If all buttons are disabled, the toolbar is not displayed in Runtime.

##### Basic procedure

1. Create an internal tag of data type "String" in the "Tag" editor, for example, "PDFFile".
2. Insert the PDF view in the screen of the "Screens" editor. The PDF view is available in the "Tools > Controls" task card.
3. In the Inspector window, select "Properties > Properties > General".
4. Enter the file name of the PDF file that opens by default in runtime in "File name".

   You can also leave the "File name" field blank.
5. For "File name tag", select the "PDFFile" tag from the selection list.
6. Insert an I/O field in the screen in the "Screens" editor.
7. In the Inspector window of the I/O field "Properties > Properties > General > Tag" select the "PDFFile" tag from the selection list.
8. Assign the PDF view the "PDFFile" tag under "File name tag" in the Inspector window.
9. Create a text field for the label in the configured I/O field, for example, "PDF path".

If the operator enters the file name along with the path in the I/O field, the PDF view opens the file in question.

##### Toolbar (RT Advanced)

In Runtime Advanced, you can configure a toolbar for the PDF view with which the PDF view is operated in Runtime.

You configure the operator controls that are only visible in the PDF view in Runtime in the engineering system in the Inspector window under "Properties > Properties > Toolbar":

- Search: Specifies whether the search bar and "forward" and "backward" buttons are displayed.

  To search in the displayed document, enter the search term in the search field. The searched text must not contain more than 255 characters. The found text is visually highlighted in the PDF view. You navigate between the search results in the text using the "Forward" and "Backward" buttons. If the found text is located outside of the visible area, the PDF display automatically scrolls to the search result.

  If the sought-after term cannot be found in the document, the search box is highlighted in yellow and the navigation buttons are grayed out. The searched text must not contain more than 255 characters. Line breaks and other formatting characters are ignored in the search.

  > **Note**
  >
  > The search for a text that contains special characters or umlauts is not supported in PDF documents with version 1.3 or older.
- Copy: Specifies that the "Select"/"Move" and "Copy" buttons are displayed.

  To select the required section of text, switch on selection mode in the PDF view with the help of the "Select" symbol. Click in front of the first character and drag the cursor over the text to select the text section. The desired section is highlighted in blue. When you have selected the text, click "Copy" to copy the selected text. You can insert the text which is saved in the clipboard in a different object.

  Even if the selected section contains images and other objects, only the text is copied from the selected area to the clipboard.

  Only the text that is currently displayed in the PDF viewer is copied to the Clipboard. Make sure that the desired section of text is fully visible when selecting it.
- Zoom: Specifies that the "Zoom In", "Zoom Out", "Fit to Page Width" and "Fit to Page Height" buttons are shown.

  You adapt the view of the PDF view using the buttons in the zoom bar. The document is opened with the "Adapt to page width" setting by default. If you adapt the view to the page height, the entire page is displayed in the PDF view.

| Operator control | Designation | Function |
| --- | --- | --- |
| ![Toolbar (RT Advanced)](images/112101242891_DV_resource.Stream@PNG-de-DE.png) | "Browse" | Searches for a character string within the document.   You use the arrows to navigate forwards and backwards between the search results. |
| ![Toolbar (RT Advanced)](images/94508221195_DV_resource.Stream@PNG-de-DE.png) | "Select" | Selects the text. |
| ![Toolbar (RT Advanced)](images/94435789195_DV_resource.Stream@PNG-de-DE.png) | "Copy" | Copies the selected text. |
| ![Toolbar (RT Advanced)](images/94508370827_DV_resource.Stream@PNG-de-DE.png) | "Move" | Moves the view horizontally and vertically. |
| ![Toolbar (RT Advanced)](images/94508418315_DV_resource.Stream@PNG-de-DE.png) | "Fit to Page Width" | Adapts the display to the page width. |
| ![Toolbar (RT Advanced)](images/94451392651_DV_resource.Stream@PNG-de-DE.png) | "Fit to Page Height" | Adapts the display to the page height. |
| ![Toolbar (RT Advanced)](images/94435819659_DV_resource.Stream@PNG-de-DE.png) | "Zoom in" | Enlarges the display. |
| ![Toolbar (RT Advanced)](images/94508212363_DV_resource.Stream@PNG-de-DE.png) | "Zoom out" | Reduces the display. |

##### Configuring operator controls

Operator controls are configured buttons in the process picture or softkeys on the HMI device for operating the object.

Configure operator controls yourself, for example, buttons, and link the operator controls with system functions.

1. For example, drag the "Button" object to the screen from the toolbox.
2. Enter a text of any length.
3. In the Inspector window, select "Properties > Events > Click".   
   The "Function list" dialog box is opened.
4. The system functions for operation of the PDF view are available in the list of system functions in the group "Keyboard operation for screen objects".   
   From the list select a function, for example, "PDFZoomIn".
5. From the "Screen object" list, select the object name of the PDF view in which the command is executed.

##### System functions

The following system functions are available for the "PDF view" object:

| System function | Description |
| --- | --- |
| "PDFZoomIn" | Zooms in one zoom level |
| "PDFZoomOut" | Zooms out one zoom level |
| "PDFGotoNextPage" | Moves to the next page |
| "PDFGotoPreviousPage" | Moves to the previous page |
| "PDFGotoFirstPage" | Moves to the first page |
| "PDFGotoLastPage" | Moves to the last page |
| "PDFFitToWidth" | Fits the display to fit the width of the PDF view window |
| "PDFFitToHeight" | Fits the display to the height of the PDF view window |
| "PDFZoomOriginal" | Changes the display to the original size |
| "PDFScrollUp" | Scrolls up |
| "PDFScrollDown" | Scrolls down |
| "PDFScrollLeft" | Scrolls to the left |
| "PDFScrollRight" | Scrolls to the right |
| "PDFGotoPage" | Moves to the specified page |

> **Note**
>
> Scrolling on all HMI devices also works with multi-touch operation.

The figure below shows a PDF view with the configured operator controls:

![System functions](images/68526818187_DV_resource.Stream@PNG-en-US.png)

##### Comments

Compared to Adobe Acrobat, the PDF view has limited functionality:

- The PDF view does not support links.
- The PDF view supports the following zoom levels:

  - Zoom levels 25% to 200% for KTP Mobile Panels, Comfort Panels
  - Zoom levels 25% to 400% for Runtime Advanced

> **Note**
>
> In Runtime Advanced you can scale the view using multi-touch gestures. You zoom into/out from the view using two finger zoom.

> **Note**
>
> In Runtime Advanced, no pop-up notes (sticky notes) can be displayed in PDF files with the PDF view.

> **Note**
>
> The "PDF view" object cannot be addressed by using VB scripting.

> **Note**
>
> A lot of RAM might be needed to display and scroll through large PDF files. In such cases, the system event 130000 "Not enough RAM" is displayed.

---

**See also**

[Objects for WinCC Runtime Advanced (RT Advanced)](#objects-for-wincc-runtime-advanced-rt-advanced)

#### PLC code view (Panels, Comfort Panels, RT Advanced)

##### Use

The "PLC code view" object is used to display the current program status of user programs and security programs (F blocks) which have been programmed in the LAD, FBD or GRAPH programming languages. Errors during execution of a GRAPH sequencer are displayed directly at the corresponding step.

![Use](images/112904121483_DV_resource.Stream@PNG-en-US.png)

The PLC code view is divided into the following areas:

- Header

  The header shows the PLC name, the FB name, as well as the number and name of the network in Runtime.
- Information area

  The PLC network is graphically represented in the information area in Runtime.
- Symbol table

  The symbol table shows the symbolic names of the operands, absolute addresses of the operands and corresponding comments.
- Toolbar

  The toolbar shows the buttons available in the PLC code view in Runtime.

> **Note**
>
> The "PLC Code View" object cannot be used in faceplates, in the global screen, in pop-up screens and slide-in screens.

> **Note**
>
> **Device dependency of the "PLC code view" object**
>
> The "PLC code view" object is available for RT Advanced, Comfort Panels and KTP Mobile Panels with 7" display size or more.

##### Layout

You change the settings for the position, style, colors, and fonts of the object in the Inspector window. You also, importantly, adjust the toolbar buttons here.

- You specify the display of path information in the header of the PLC code view under "Display > Show header (path)".
- You specify the number of lines that are displayed in the symbol table in Runtime under "Symbol table lines > Number of visible lines".
- You specify the width of the detail view relative to the information area under "GRAPH detail area > GRAPH detail area width (%)".
- You specify the two-line display of GRAPH step names in Runtime under "GRAPH view > Two-line view".

  To enable the two-line view, the "Show two lines" option must be selected under "Options > Settings > PLC programming > GRAPH > Length of step and transition names".

##### Toolbar

The operator controls with which the PLC code view is operated in Runtime are configured under "Properties > Properties > Toolbar > Buttons" in the Inspector window.

| Operator control | Designation | Function |
| --- | --- | --- |
| ![Toolbar](images/81241269643_DV_resource.Stream@PNG-de-DE.png) | "Symbol area" | Shows the symbol area. |
| ![Toolbar](images/81241914123_DV_resource.Stream@PNG-de-DE.png) | "Previous network" | Navigates to the previous network |
| ![Toolbar](images/81241278475_DV_resource.Stream@PNG-de-DE.png) | "Next network" | Navigates to the next network |
| ![Toolbar](images/81241922571_DV_resource.Stream@PNG-de-DE.png) | "Zoom in" | Enlarges the information area. |
| ![Toolbar](images/81241931019_DV_resource.Stream@PNG-de-DE.png) | "Zoom out" | Reduces the information area. |
| ![Toolbar](images/81242387467_DV_resource.Stream@PNG-de-DE.png) | "Detail" | Shows the detail view. |
| ![Toolbar](images/81242408715_DV_resource.Stream@PNG-de-DE.png) | "Step mode" | Switches between manual and automatic step selection for the active step. |
| ![Toolbar](images/84248476683_DV_resource.Stream@PNG-de-DE.png) | "Transition or Interlock" | Switches between the transition and interlock network views. |
| ![Toolbar](images/94991861387_DV_resource.Stream@PNG-de-DE.png) | "Actual values or initial values" | Switches between the views of actual values and initial values. |
| ![Toolbar](images/108445315723_DV_resource.Stream@PNG-de-DE.png) | "Single network or entire function block" | Switches between the view from a single network with the input logic and the view of the entire function block. |

##### Configuring the PLC code view

1. Drag-and-drop the PLC Code View from the toolbox view.
2. Click "Properties > Properties > Toolbar" in the Inspector window.
3. Select the buttons that you require in Runtime, for example: Next network, Previous network, Step mode.
4. If required, configure the button display, e.g. background color or fill pattern.
5. In the Inspector window, select "Properties > Properties > Columns".
6. Select the columns that you require in the device view for Runtime.
7. Customize the column headers or order if necessary.
8. Select an authorization for operation in "Properties > Properties > Security".

##### Controlling the PLC code view with the keyboard

To control the PLC code view with the keyboard, proceed as follows:

1. Press the <Tab> key repeatedly until the focus is on the desired button.

   You can use the <Shift + Tab> shortcut keys to navigate back to the previous button.
2. Press <Enter>.

   The command is executed.

##### Operation with the touch screen

Scrolling by dragging in the symbol table of the PLC code view is not supported.   
To scroll horizontally and vertically in the symbol table, use the scroll bars and the scroll arrows.

##### Multilingual GRAPH names

WinCC supports the display of step names and transition names for the GRAPH blocks in multiple languages starting from Version 5.0. The step names and transition names will then be displayed in the selected Runtime language following a language changeover in Runtime. If the selected language is not available in the GRAPH block, the names are displayed in the default language (English).

##### Mnemonics in the PLC code view

The PLC code viewer shows the data in the mnemonics you have set in TIA Portal. The international mnemonics are set by default. The international mnemonics provide e.g. the displayed addresses in all configured languages in runtime with the ID "IO", independent of the configured runtime languages.

##### Properties of a PLC in Runtime

If a PLC is connected to the PLC code view in WinCC and Runtime is active, changing the name of the PLC will trigger errors. Therefore, do not change the PLC name, the IP address, or other properties of the HMI connection.

##### Addressing tags in the "PLC code view" object

The "PLC code view" object only supports symbolic addressing of tags. If the operand is not addressed symbolically, the network with the operand cannot be displayed and an error message is generated.

##### Displaying time-value constants

When time-value constants are displayed, the time is shown in the format "Hours/Minutes/Seconds/" in the PLC code view, depending on the input configured in the Engineering System. For example, a constant "150 s" specified in the Engineering System appears in Runtime as "2 min 30 s".

---

**See also**

[Supervising machinery and plants with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supervising-machinery-and-plants-with-prodiag-panels-comfort-panels-rt-advanced-rt-professional)
  
[Supported data types (Panels, Comfort Panels, RT Advanced)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supported-data-types-panels-comfort-panels-rt-advanced)
  
[Supported instructions (Panels, Comfort Panels, RT Advanced)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supported-instructions-panels-comfort-panels-rt-advanced)
  
[Configuring the PLC code view (Panels, Comfort Panels, RT Advanced)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-the-plc-code-view-panels-comfort-panels-rt-advanced-1)
  
[Configuring the PLC code view (Panels, Comfort Panels, RT Advanced)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-the-plc-code-view-panels-comfort-panels-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### PLC code view (RT Professional)

##### Use

The "PLC Code View" object is available for the HMI device, WinCC Runtime Professional. This object is used to display the current program status of PLC programs which have been programmed in the LAD, FBD or GRAPH programming languages. Errors during execution of a GRAPH step sequencer are displayed directly at the corresponding step.

![Use](images/110878817675_DV_resource.Stream@PNG-en-US.png)

The PLC code view is divided into the following areas:

- Toolbar

  The toolbar shows the buttons available in the PLC code view in Runtime.
- Header

  The header shows the PLC name, the FB name, as well as the number and name of the network in Runtime.
- Network area

  The PLC network is graphically represented in the network area in Runtime.
- Symbol table

  The symbol table shows the symbolic names of the operands, absolute addresses of the operands and corresponding comments.

> **Note**
>
> The "PLC Code View" object cannot be used in groups or faceplates.

##### Layout

In the Inspector window, you customize the position, style, colors and font types of the object. You can adapt the following properties in particular:

- Buttons of the toolbar under "Toolbar > Toolbar buttons"
- Number of lines that are displayed in the symbol table in Runtime under "Symbol table lines > Number of visible lines"
- Two-line display of GRAPH step names in Runtime under "GRAPH view > Two-line view"

  To enable the two-line view, the "Show two lines" option must be selected under "Options > Settings > PLC programming > GRAPH > Length of step and transition names".

##### Displaying the network

The network to be displayed in the PLC code view is determined by user-defined functions. Depending on the programming language of the PLC program, one of the following API functions is called from within the user-defined function:

- OpenViewerIECPLByCall
- OpenViewerIECPLByFCCall
- OpenViewerIECPLByAssignment
- OpenViewerS7GraphByBlock

You can find detailed information and examples of how to set up a user-defined function in the [Description of API functions](Runtime%20API%20%28RT%20Professional%29.md#basics-rt-professional-10).

##### Toolbar

The operator controls with which the PLC code view is operated in Runtime are configured under "Properties > Properties > Toolbar > Buttons" in the Inspector window.

| Operator control | Designation | Function |
| --- | --- | --- |
| ![Toolbar](images/83180944907_DV_resource.Stream@PNG-de-DE.png) | "Symbol area" | Shows the symbol area. |
| ![Toolbar](images/83205324939_DV_resource.Stream@PNG-de-DE.png) | "Previous network" | Navigates to the previous network |
| ![Toolbar](images/83205333771_DV_resource.Stream@PNG-de-DE.png) | "Next network" | Navigates to the next network |
| ![Toolbar](images/83205457803_DV_resource.Stream@PNG-de-DE.png) | "Zoom in" | Enlarges the information area. |
| ![Toolbar](images/83205543435_DV_resource.Stream@PNG-de-DE.png) | "Zoom out" | Reduces the information area. |
| ![Toolbar](images/83205727499_DV_resource.Stream@PNG-de-DE.png) | "Detail" | Shows the detail view. |
| ![Toolbar](images/83205552267_DV_resource.Stream@PNG-de-DE.png) | "Step mode" | Switches between manual and automatic step selection for the active step. |
| ![Toolbar](images/83205800331_DV_resource.Stream@PNG-de-DE.png) | "Transition or Interlock" | Switches between transition view and interlock view. |
| ![Toolbar](images/94991852555_DV_resource.Stream@PNG-de-DE.PNG) | "Actual or initial values" | Switches between the views of actual values and initial values. |
| ![Toolbar](images/110880752267_DV_resource.Stream@PNG-de-DE.png) | "Single network or entire function block" | Switches between the view from a single network with the input logic and the view of the entire function block. |

##### Multilingual GRAPH names

WinCC supports the display of step names and transition names for the GRAPH blocks in multiple languages starting from Version 5.0. The step names and transition names will then be displayed in the selected Runtime language following a language changeover in Runtime. If the selected language is not available in the GRAPH block, the names are displayed in the default language (English).

##### Properties of a PLC in Runtime

If a PLC is connected to the PLC code view in WinCC and Runtime is active, changing the name of the PLC will trigger errors. Therefore, do not change the PLC name, the IP address, or other properties of the HMI connection.

##### Error message when PLC is loaded with a newer version of the TIA Portal

An error message is output if the PLC code view from an older version of WinCC accesses a program on the PLC that is loaded with a new version. Make sure that the PLC and the HMI are loaded with the same version of the TIA Portal.

##### Addressing tags in the "PLC code view" object

The "PLC code view" object only supports symbolic addressing of tags. If the operand is not addressed symbolically, the network with the operand cannot be displayed and an error message is generated.

---

**See also**

[Configuring the PLC code view (Panels, Comfort Panels, RT Advanced)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-the-plc-code-view-panels-comfort-panels-rt-advanced-1)
  
[Configuring the PLC code view (Panels, Comfort Panels, RT Advanced)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-the-plc-code-view-panels-comfort-panels-rt-advanced)
  
[Supervising machinery and plants with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supervising-machinery-and-plants-with-prodiag-panels-comfort-panels-rt-advanced-rt-professional)
  
[Supported instructions (RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supported-instructions-rt-professional)
  
[Supported data types (Panels, Comfort Panels, RT Advanced)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supported-data-types-panels-comfort-panels-rt-advanced)

#### Polygon (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Polygon" is a closed object which you can fill with a background color.

![Application](images/58121345035_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. In particular, you can customize the following property:

Geometry: Modifies, deletes or adds corners.

##### Geometry

The corner points are numbered in the order of their creation. You can change, delete, or add more corner points:

1. In the Inspector window, select "Properties > Properties > Layout".
2. Select the required corner point in the "Geometry" area. Input a value at "X position " and "Y position ".
3. To add a corner point, click the ![Geometry](images/14828972939_DV_resource.Stream@PNG-de-DE.png) button.
4. To delete a corner point, click the ![Geometry](images/14829467019_DV_resource.Stream@PNG-de-DE.png) button.

##### Alternative procedure

You can also change, delete, or add new corner points using the mouse:

1. Select the object. Position the mouse cursor on the desired corner. The mouse cursor changes to a crosshair.
2. Drag the corner to the desired position while holding down the mouse button.
3. Right-click the position at which you want to insert the corner point. Select "Add point" from the shortcut menu.

##### Configuring Rotation in runtime

You configure the "Polygon" object so that it rotates about a reference point in runtime. The rotation in runtime is only possible for devices with Runtime Professional.

Enter the values for the angle of rotation using Degrees as the unit.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter values for the following attributes in the "Rotation" area.

   - X
   - Y
   - Angle

---

**See also**

[Polyline (Panels, Comfort Panels, RT Advanced, RT Professional)](#polyline-panels-comfort-panels-rt-advanced-rt-professional)
  
[Rotating an object in runtime (RT Professional)](#rotating-an-object-in-runtime-rt-professional)

#### Polyline (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Polyline" is an open object. Use the "Polygon" object if you want to fill the object with color.

![Application](images/58121507723_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. You can adapt the following properties in particular:

- Line start and end: Specifies the type of line start and line end.
- Geometry: Modifies, deletes or adds corners.

##### Line start and end

You define the start point and the end point of the line under "Properties > Properties >"Appearance" in the Inspector window. Use arrow point, for example, as start and end point. The available start and end points depend on the device.

##### Geometry

The corner points are numbered in the order of their creation. You can change, delete, or add more corner points:

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select the required corner point in the "Geometry" area. Input a value at "X position" and "Y position".
3. To add a corner point, click the ![Geometry](images/14828972939_DV_resource.Stream@PNG-de-DE.png) button.
4. To delete a corner point, click the ![Geometry](images/14829467019_DV_resource.Stream@PNG-de-DE.png) button.

##### Alternative procedure

You can also change, delete, or add new corner points using the mouse:

1. Select the object. Position the mouse cursor on the desired corner. The mouse cursor changes to a crosshair.
2. Drag the corner to the desired position while holding down the mouse button.

##### Configuring rotation in Runtime

You configure the "Polyline" object so that it rotates about a reference point in Runtime. The rotation in Runtime is only possible for devices with Runtime Professional.

Enter the values for the angle of rotation using Degrees as the unit.

1. Click "Layout" in the Inspector window.
2. Enter values for the following attributes in the "Rotation" area.

   - X
   - Y
   - Angle

---

**See also**

[Polygon (Panels, Comfort Panels, RT Advanced, RT Professional)](#polygon-panels-comfort-panels-rt-advanced-rt-professional)

#### ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

The "ProDiag overview" object provides an overview of the current status of the configured monitoring in Runtime. When an error occurs, the type of error and the error category are determined in the ProDiag overview. You can navigate directly to the error message in an alarm view and have the affected program code shown in the PLC code view.

![Use](images/164377566859_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The "ProDiag overview" object cannot be used in faceplates or in the global screen.

> **Note**
>
> **Device dependency of the "ProDiag overview" object**
>
> The "ProDiag overview" object is available for RT Advanced, RT Professional, Comfort Panels and KTP Mobile Panels.

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Displayed buttons
- Names and colors for categories
- Names and colors for monitoring types

##### Configuring the ProDiag overview

A CPU and a ProDiag FB are created.

1. In the Inspector window, select "Properties > Properties > General".
2. Open the selection button under the "Tag" property.
3. Select the status tag of ProDiag FB.

   Alternatively, drag the status tag from the detail view and drop it at the desired point of use.
4. Under "Output > Categories", define the names, colors and flashing behavior for the categories.
5. Under "Output > Supervision types", define the names, colors and flashing behavior for the supervision types.
6. Select an authorization for operation under "Properties > Properties > Security".

##### Configuring a compact view

You can configure the ProDiag overview in a compact view.

![Configuring a compact view](images/80801307019_DV_resource.Stream@PNG-en-US.png)

Disable the display of categories and monitoring types under "Properties > Appearance > Options". Disable all buttons under "Properties > Toolbar > General".

##### Monitoring types and categories

You can display a maximum of eight categories and six types of monitoring in the "ProDiag overview" object. The pre-defined categories and monitor types are available:

| Designation | Categories |
| --- | --- |
| E | Error |
| W | Warning |
| I | Info |

Rename the categories C4 to C8, which are created by default, according to your requirements.

| Designation | Monitoring type |
| --- | --- |
| O | Operand error |
| I | Interlock error |
| R | Reaction error |
| A | Action error |
| P | Position error |
| M | Alarm |

You can change the display symbols of monitoring types and categories at any time under "Output" in the Inspector window.

##### Symbols

You specify the symbols that are displayed in the ProDiag overview in the Inspector window under "Properties > Appearance > Options". The following symbols are available for ProDiag overview:

| Icon | Name | Function |
| --- | --- | --- |
| ![Symbols](images/79043005195_DV_resource.Stream@PNG-de-DE.png) | Help | Opens the user-defined tooltip. |
| ![Symbols](images/79043014283_DV_resource.Stream@PNG-de-DE.png) | Info | Displays the information for monitoring. |
| ![Symbols](images/80801398795_DV_resource.Stream@PNG-de-DE.png) | Error | Indicates that an error has occurred. |

##### "Alarm view" button

To display the "Alarm view" in the ProDiag overview, select the "Show alarm window button" property under "Properties > Toolbar > General".

| Button | Name | Function |
| --- | --- | --- |
| !["Alarm view" button](images/164643614091_DV_resource.Stream@PNG-de-DE.png) | Alarm view | Opens the configured alarm view with the error message. |

##### Deactivated display

If there is a faulty connection to the controller during runtime, the object "ProDiag overview" is displayed grayed-out (unavailable). This deactivated display can be due to the following:

- The controller is deactivated
- The configured ProDiag program block was removed from the control program
- The controller is in stop mode

As soon as the cause of the error is removed and the connection reestablished, the ProDiag overview shows the current online status of the monitoring during runtime.

---

**See also**

[Basics of supervision with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-supervision-with-prodiag-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basics of supervising operands (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-supervising-operands-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring the ProDiag overview (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-the-prodiag-overview-panels-comfort-panels-rt-advanced-rt-professional)
  
[Supervising machinery and plants with ProDiag (Panels, Comfort Panels, RT Advanced, RT Professional)](Using%20the%20diagnostics%20functions%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#supervising-machinery-and-plants-with-prodiag-panels-comfort-panels-rt-advanced-rt-professional)

#### Rectangle (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Rectangle" is a closed object which you can fill with a color.

![Application](images/58081421323_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Corner radius: Specifies the horizontal and vertical distance between the corner of the rectangle and the start point of a rounded corner.

##### Corner radius

The corners of the "Rectangle" object can be rounded to suit your requirements. When the properties "X" and "Y" are set to the 100 % value, the rectangle is displayed as an ellipse. As soon as one of the properties has the value 0%, a normal rectangle without a rounded corner is shown.

1. Click "Properties > Properties > Layout" in the inspector window.
2. Enter a value for "X" in the "Corner radius" area.

   The input value is the percentage proportion of half the width of the rectangle.
3. Enter a value for "Y" in the "Corner radius" area.

   The input value is the percentage proportion of half the height of the rectangle.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Recipe view (RT Professional)

##### Application

The "Recipe view" object is used to display and modify recipes.

![Application](images/56795284107_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Log/View: Defining a recipe or recipe query
- Toolbar: Defines the operator controls of the recipe view.
- Columns: Specifies the columns that are displayed in the recipe data record.

##### Log/View

Define the recipe or recipe query to be displayed in the recipe view under "Properties > Properties > General > Log/View" in the Inspector window.

##### Toolbar

The control elements with which the recipe view is operated in Runtime are configured under "Properties > Properties > Buttons" in the Inspector window. In the simple recipe view the operating elements are based on the functions of the menu.

| Operator control |  | Description |
| --- | --- | --- |
| ![Toolbar](images/67385995915_DV_resource.Stream@PNG-de-DE.png) | "Tooltip" | Calls the info text for the recipe display. |
| ![Toolbar](images/67388091019_DV_resource.Stream@PNG-de-DE.png) | "Configuration dialog" | Opens the configuration dialog box in which you change the properties of the recipe display. |
| ![Toolbar](images/67388094859_DV_resource.Stream@PNG-de-DE.png) | "Select data connection" | Opens a dialog for selecting a recipe or recipe query. The recipe data are then shown in the table of the recipe view. |
| ![Toolbar](images/67388098699_DV_resource.Stream@PNG-de-DE.png) | "First row" | The first data record is displayed in the table by the button. |
| ![Toolbar](images/67388307339_DV_resource.Stream@PNG-de-DE.png) | "Previous row" | The previous data record is displayed in the table by the button. |
| ![Toolbar](images/67388311179_DV_resource.Stream@PNG-de-DE.png) | "Next row" | The next data record is displayed in the table by the button. |
| ![Toolbar](images/67388315147_DV_resource.Stream@PNG-de-DE.png) | "Last row" | The last data record is displayed in the table by the button. |
| ![Toolbar](images/67388318987_DV_resource.Stream@PNG-de-DE.png) | "Delete rows" | The content of the marked lines are deleted. |
| ![Toolbar](images/67388322827_DV_resource.Stream@PNG-de-DE.png) | "Cut rows" | The content of the marked lines are cut out. |
| ![Toolbar](images/67388326667_DV_resource.Stream@PNG-de-DE.png) | "Copy rows" | The content of the marked lines are copied. |
| ![Toolbar](images/67388330507_DV_resource.Stream@PNG-de-DE.png) | "Paste rows" | The content of the copied or cut-out lines is inserted starting from the marked line. |
| ![Toolbar](images/67388334347_DV_resource.Stream@PNG-de-DE.png) | "Read tags" | The contents of the connected WinCC tags are read and written into the recipe elements by the button. The "Tags" communication type must be activated in the displayed recipe to be able to use the button. The recipe elements must be connected with tags. |
| ![Toolbar](images/67388338187_DV_resource.Stream@PNG-de-DE.png) | "Write tags" | The contents of the recipe elements are written into the connected WinCC tags. The "Tags" communication type must be activated in the displayed recipe to be able to use the button. The recipe elements must be connected with tags. |
| ![Toolbar](images/67388342027_DV_resource.Stream@PNG-de-DE.png) | "Import log" | Using a button, a CSV file is imported from the "ua" directory of the project folder into the table of the recipe view. |
| ![Toolbar](images/67388345867_DV_resource.Stream@PNG-de-DE.png) | "Export log" | The original contents of the table are exported with table headers by the button when loading. The recipe is stored as a CSV file in the "ua" directory of the project folder. |
| ![Toolbar](images/67388349707_DV_resource.Stream@PNG-de-DE.png) | "Sort dialog" | Opens a dialog box for setting a customized sorting of the displayed columns. |
| ![Toolbar](images/67388353547_DV_resource.Stream@PNG-de-DE.png) | "Print" | Starts the printout of the displayed values. The print job used for printing is defined in the configuration dialog in the "General" tab. |
| ![Toolbar](images/67388361227_DV_resource.Stream@PNG-de-DE.png) | "Set time base" | Opens a dialog box for setting the time base for the used times. |
| ![Toolbar](images/67388357387_DV_resource.Stream@PNG-de-DE.PNG) | "Export data" | Using a button, you can export the recipe or recipe query to a CSV file as configured but with the current runtime data. If the "Display dialog" option is active, a dialog opens in which you can view the settings for exporting and can start the export. With the appropriate operator authorizations you may also select the file and the directory for export.  If no dialog is displayed, export of data to the default file is started immediately. |
| ![Toolbar](images/67388365067_DV_resource.Stream@PNG-de-DE.PNG) | "User-defined" | Displays the first button created by the user. The function of the button is customized. |

##### Columns

In the Inspector window under "Properties > Properties > Columns > Column properties", you define which columns are displayed in the recipe view.

##### Configuration behavior

**Displaying column headers**

The layout of the recipe view is dependent on the view settings in the control panel. Depending on the setting, the column headers may be truncated. This setting is found under "Display > Appearance" in the control panel. To display column headers correctly, set the display in "Windows and buttons" to "Windows Classic" style.

This behavior only occurs during configuration. The column headers are displayed correctly in Runtime.

---

**See also**

[Displaying recipes (RT Professional)](Working%20with%20recipes%20%28RT%20Professional%29.md#displaying-recipes-rt-professional)
  
[Properties of the recipe view (RT Professional)](Working%20with%20recipes%20%28RT%20Professional%29.md#properties-of-the-recipe-view-rt-professional)
  
[Editing recipe data (RT Professional)](Working%20with%20recipes%20%28RT%20Professional%29.md#editing-recipe-data-rt-professional)
  
[Configuring persistence (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-persistence-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Recipe view (as of V13) (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Use

The "Recipe view" object is used to display recipes on the HMI device.

> **Note**
>
> **Device dependency of the "Advanced recipe view" object**
>
> The "Advanced recipe view" object is available on the HMI devices Basic Panels 2nd Generation, Comfort Panels, Mobile Panels with the device version V13.

![Use](images/74775278859_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Toolbar: Defines the operator controls of the recipe view.
- Display number: Defines whether the number of the recipe and the number of the recipe data record is displayed.
- Label: Sets the label for the name of the recipe and the recipe data record.

##### Operator controls

The operator controls with which the recipe view is operated in Runtime are configured under "Properties > Properties > Buttons" in the Inspector window. In the simple recipe view the operating elements are based on the functions of the menu.

| Operator control |  | Description |
| --- | --- | --- |
| ![Operator controls](images/65171821835_DV_resource.Stream@PNG-de-DE.png) | "Info text" | Calls up the configured tooltip for the selected recipe. |
| ![Operator controls](images/65174313867_DV_resource.Stream@PNG-de-DE.png) | "Add data record" | Creates a new recipe data record in the recipe. |
| ![Operator controls](images/65174322699_DV_resource.Stream@PNG-de-DE.png) | "Delete data record" | Deletes the selected data record. |
| ![Operator controls](images/68659792523_DV_resource.Stream@PNG-de-DE.png) | "Rename" | Changes the name of selected data record. |
| ![Operator controls](images/65174413195_DV_resource.Stream@PNG-de-DE.png) | "Save" | Saves the modified record with its current name. |
| ![Operator controls](images/65174473227_DV_resource.Stream@PNG-de-DE.png) | "Save as..." | Saves the modified record with a new name. |
| ![Operator controls](images/65174404363_DV_resource.Stream@PNG-de-DE.png) | "Write to PLC" | Sends the current value to the PLC. |
| ![Operator controls](images/65174369931_DV_resource.Stream@PNG-de-DE.png) | "Read from PLC" | Reads the current value from the PLC. |
| ![Operator controls](images/65174571659_DV_resource.Stream@PNG-de-DE.png) | "Synchronize recipe tags" | Compares the values of the selected data record with the values on the PLC. |

##### Display number

Specifies whether the number of the recipe and the number of the recipe data record are displayed in Runtime. The number of the recipe uniquely identifies the recipe in the project.

1. Click "Properties > Properties > View" in the Inspector window.
2. Select "Display > Display numbers".

##### Display label

Use this property to specify the name to be shown for recipes and data records in the recipe view.

1. Click "Properties > Properties > Label" in the Inspector window.
2. Select "Display labels".
3. Enter the labels for the recipe and the recipe data record.

##### Behavior during configuration

**Displaying column headers**

The layout of the recipe view is dependent on the view settings in the control panel. Depending on the setting, the column headers may be truncated. This setting is found under "Display > Appearance" in the control panel. To display column headers correctly, set the display in "Windows and buttons" to "Windows Classic" style.

This behavior only occurs during configuration. The column headers are displayed correctly in Runtime.

##### Scrolling in the recipe view

A recipe view contains an element that is shown as a text list in the recipe table. You can only scroll between the elements in the table of the recipe view, if you have previously selected an element that does not contain a text list.

#### Recipe view, simple (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Use

The "Recipe view" object is used to display and modify recipes.

![Use](images/65160694155_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Configure the "Simple recipe view" object on devices with device version 12.0.0.0 or older.

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Toolbar: Specifies the menu commands of the recipe view.

##### Toolbar

The menu items with which the recipe view is operated in Runtime are configured under "Properties > Properties > Toolbar" in the Inspector window.

| Menu command | Description |
| --- | --- |
| "Tooltip" | Calls up the configured tooltip for the selected recipe. |
| "Add data record" | Creates a new recipe data record in the recipe. |
| "Delete data record" | Deletes the selected data record. |
| "Save" | Saves the modified record with its current name. |
| "Save as" | Saves the modified record with a new name. |
| "Write to PLC" | Sends the current value to the PLC. |
| "Read from PLC" | Reads the current value from the PLC. |
| "Rename" | Specifies that the "Rename" button is shown. |
| "Forward" | Specifies that the menu buttons are visible. |
| "Back" | Specifies that the "Back" button is shown. |

#### Recipe view, advanced (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Advanced recipe view

The "Recipe view" object is used to display and modify recipes. The advanced or the simple user view is available depending on the HMI device

![Advanced recipe view](images/56759762059_DV_resource.Stream@PNG-en-US.png)

##### Changing the view type

On HMI devices with a display larger than 6", both the advanced and the simplified recipe view can be used to manage and process recipes. The view type is only available for configuration on devices up to device version V13.

> **Note**
>
> Do not use the simple recipe view in a group.

![Changing the view type](images/65160694155_DV_resource.Stream@PNG-en-US.png)

Configuring the simple recipe view:

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select "Mode > Display type > Simplified".

**Note**

**Behavior for Runtime Professional, Runtime Advanced and Panels**

In the Engineering System you can dynamically control the visibility of an object, for example, in the "Animations" tab of the Inspector window. In Runtime, the "Simple recipe view" does not support animations. If you have configured an animation and, for example, want to check the consistency of the project, an error alarm is displayed in the Output window.

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Operator controls: Defines the operator controls of the recipe view.
- Display number: Defines whether the number of the recipe and the number of the recipe data record is displayed.

##### Operator controls

The operator controls with which the recipe view is operated in Runtime are configured under "Properties > Properties > Buttons" in the Inspector window. In the simple recipe view the operating elements are based on the functions of the menu.

| Operator control |  | Description |
| --- | --- | --- |
| ![Operator controls](images/14829503371_DV_resource.Stream@PNG-de-DE.png) | "Tooltip" | Calls up the configured tooltip for the selected recipe. |
| ![Operator controls](images/72283805323_DV_resource.Stream@PNG-de-DE.png) | "Add data record" | Creates a new recipe data record in the recipe. |
| ![Operator controls](images/72283591691_DV_resource.Stream@PNG-de-DE.png) | "Delete data record" | Deletes the selected data record. |
| ![Operator controls](images/72283874187_DV_resource.Stream@PNG-de-DE.png) | "Save" | Saves the modified record with its current name. |
| ![Operator controls](images/72283908619_DV_resource.Stream@PNG-de-DE.png) | "Save as" | Saves the modified record with a new name. |
| ![Operator controls](images/72283981451_DV_resource.Stream@PNG-de-DE.png) | "Synchronize recipe tags" | Compares the values of the selected data record with the values on the PLC. |
| ![Operator controls](images/72283582859_DV_resource.Stream@PNG-de-DE.png) | "Write to PLC" | Sends the current value to the PLC. |
| ![Operator controls](images/72283865355_DV_resource.Stream@PNG-de-DE.png) | "Read from PLC" | Reads the current value from the PLC. |

##### Display number

Specifies whether the number of the recipe and the number of the recipe data record are displayed in Runtime. The number of the recipe uniquely identifies the recipe in the project.

1. Click "Properties > Properties > View" in the Inspector window.
2. Select "Display > Display numbers".

##### Configuration behavior

##### Displaying column headers

The layout of the recipe view is dependent on the view settings in the control panel. Depending on the setting, the column headers may be truncated. This setting is found under "Display > Appearance" in the control panel. To display column headers correctly, set the display in "Windows and buttons" to "Windows Classic" style.

This behavior only occurs during configuration. The column headers are displayed correctly in Runtime.

---

**See also**

[Recipe view, simple (Basic Panels, Panels, Comfort Panels, RT Advanced)](#recipe-view-simple-basic-panels-panels-comfort-panels-rt-advanced)
  
[Description of the advanced recipe view (prior to V13) (Panels, Comfort Panels, RT Advanced)](Working%20with%20recipes%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#description-of-the-advanced-recipe-view-prior-to-v13-panels-comfort-panels-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Round button (RT Professional)

##### Application

The "Round button" object is used to control processes. A round button is used, for example, to confirm alarms. To incorporate a round button into the process, dynamize the corresponding attribute.

![Application](images/61281511179_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. In particular, you can customize the following property:

Mode: Specifies whether the round button is shown pressed or as a toggle switch.

Type: The round button can be shown, for example, with text and graphic.

##### Show round button pressed

1. In the Inspector window, select "Properties > Properties > General".
2. Activate "Mode > Pressed".
3. To show the round button as two-way switch, activate "Mode > Toggle".

##### Specifying the round button type

1. In the Inspector window, select "Properties > Properties > General".
2. Select, for example, "Graphics and text" as "Type".

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Pipe (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

You reproduce a continuous pipe with several bends with the object "Pipe". To reproduce a pipe system, connect the "Pipe" object to other objects, e.g. pipe bend or T piece.

![Application](images/21175769355_DV_resource.Stream@PNG-de-DE.png)

##### Layout

Customize the object position and color in the Inspector window. You can adapt the following properties in particular:

- Geometry: You add additional points and extend the object.

A pipe may have any number of corners. The corner points are numbered in the order of their creation. You can move them individually.

---

**See also**

[Pipe elbow (RT Professional)](#pipe-elbow-rt-professional)
  
[T-piece (RT Professional)](#t-piece-rt-professional)
  
[Double T-piece (RT Professional)](#double-t-piece-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Pipe elbow (RT Professional)

##### Application

A pipe bend is displayed using the "Pipe bend" object. To reproduce a pipe system, connect the "Pipe bend" object to other objects, e.g. pipe bend or double T piece.

![Application](images/21175806731_DV_resource.Stream@PNG-de-DE.png)

##### Layout

Customize the object position and color in the Inspector window. You can adapt the following properties in particular:

- Angle: You specify the start and end angle of the pipe bend.
- Radius: You specify the horizontal and vertical radius of the pipe bend.

The attributes are interdependent.

- When you change "Start angle" and "End angle", the width and height are also automatically changed.

  "Horizontal radius " and "Vertical radius" are retained.
- When you change "Horizontal radius" and "Vertical radius", the width and height are also automatically changed.

  "Start angle" and "End angle" are retained.
- When you change the width and the height, the "Horizontal radius" and "Vertical radius" are also automatically changed.

  "Start angle" and "End angle" are retained.

---

**See also**

[Pipe (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#pipe-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[T-piece (RT Professional)](#t-piece-rt-professional)
  
[Double T-piece (RT Professional)](#double-t-piece-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Switch (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

The "Switch" object is used to configure a switch that is used to switch between two predefined states in runtime. The current state of the "Switch" object can be visualized with either a label or a graphic.

The following figure shows a "Switch" type switch.

![Application](images/58081516939_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. In particular, you can customize the following property:

- Type: Defines the graphic representation of the object.

##### Type

Button visualization is specified at "Properties > Properties > General >Type" in the Inspector window.

| Type | Description |
| --- | --- |
| "Switch" | The two states of the "Switch" are displayed in the form of a switch. The position of the switch indicates the current state. The state is changed in runtime by sliding the switch.   You specify the direction of movement of the switch in "Switch orientation" with this type. |
| "Switch with text" | The switch is shown as a button. The current state is visualized with a label. In runtime click on the button to actuate the switch. |
| "Switch with graphic" | The switch is shown as a button. The current state is visualized with a graphic. In runtime click on the button to actuate the switch. |

> **Note**
>
> **Basic Panels**
>
> The "Switch" type is not available for Basic Panels.

---

**See also**

[Overview of objects (Panels, Comfort Panels, RT Advanced)](#overview-of-objects-panels-comfort-panels-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Button (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Button" object allows you to configure an object that the operator can use in Runtime to execute any configurable function.

![Application](images/58081605515_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Mode: Defines the graphic representation of the object.
- Text / Graphic: Defines whether the Graphic view is static or dynamic.
- Define hotkey: Defines a key, or shortcut that the operator can use to actuate the button.

  > **Note**
  >
  > You can only define a hotkey for HMI devices with keys.

##### Mode

The button display is defined in "Properties > Properties > General >Mode" in the Inspector window.

| Mode | Description |
| --- | --- |
| "Invisible" | The button is not visible in Runtime. |
| "Text" | The button is displayed with text. This text explains the function of the button. |
| "Graphic" | The button is displayed with a graphic. This graphics represents the function of the button. |
| "Graphics or text" | The button is displayed with text or graphics.  If the graphics cannot be displayed, the corresponding text is displayed. |
| "Graphics and text" | The button is displayed with text and graphics. |

Different options are available depending on the device.

##### Text / Graphic

The "Mode" property settings are used to define whether the display is static or dynamic. The display is defined in "Properties > Properties > General >Text" or "Graphic" in the Inspector window.

You can, for example, select the following options for the "Graphic" or "Text" type.

| Type | Option | Description |
| --- | --- | --- |
| "Graphic" | "Graphic" | Use "Graphic when button is "not pressed"" to specify a graphic displayed in the button for the "OFF" state.   Use "Graphic when button is "pressed"" to specify a graphic for the "ON" state. |
| "Graphics list" | The graphic in the button depends on the state. The corresponding entry from the graphics list is displayed depending on the state. |  |
| "Text" | "Text" | Use "Text when button is "not pressed"" to specify the text displayed in the button for the "OFF" state.  Use "Text when button is "pressed"" to specify text for the "ON" state. |
| "Text list" | The text in the button depends on the state. The entry from the text list corresponding to the state is displayed. |  |

> **Note**
>
> You cannot use text lists and graphics lists in buttons in WinCC Runtime Professional.

##### Define hotkey

In the Inspector window, a key or key combination is defined that the operator can use to control the button in Runtime.

1. In the Inspector window, select "Properties > Properties > General".
2. Select a key or key combination from the selection list in the "Hotkey" area.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button for language switching (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-for-language-switching-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button with access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-configuring-a-button-with-access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Slider (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

Process values are monitored and adapted within a defined range with the "Slider" object. The monitored range is visualized in the form of a slider. By adjusting the slider, you intervene in the process and correct the displayed process value.

> **Note**
>
> Do not configure a system function at the "Change" event for a regulated project if it is used to execute a GMP-relevant action.
>
> Instead configure the system functions at the "Value change" event of the tags in order to reduce the number of user actions.

![Use](images/58121566347_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can, in particular, adapt the following properties as required:

- Maximum Value and Minimum Value: Specifies the top and bottom values of the scale.
- Display current value: Specifies whether the current position of the controller appears below the slider.
- Display of bars: The sliders above and below the bar can be hidden.

##### Maximum Value and Minimum Value

The top and bottom end values of the scale are specified in the Inspector window.

1. In the Inspector window, activate "Properties > Properties > General".
2. Enter a number at "Maximum scale value" and "Minimum scale value". If you select a tag as the end value of the scale, the number will be no longer available.

##### Configuring limits/ranges

You can display limits and ranges in different colors. You define the colors in the Inspector window.

1. In the Inspector window, select "Properties > Properties > Limits/Ranges".
2. Activate the limits/ranges that are to be displayed in runtime.
3. You can change the default colors for the ranges, if required.

> **Note**
>
> When you select the option "Show ranges from tag", you can display up to five ranges in the slider whose values are specified by means of a process tag. You define the values for the ranges with a process tag, which you interconnect with the screen object.
>
> The option "Show ranges from tag" is available for Comfort Panels, KTP Mobile Panels and RT Advanced.

##### Display current value

Specify that the value of the current position is displayed below the slider in the Inspector window.

1. In the Inspector window, activate "Properties > Properties > Layout".
2. Select "Show current value."

##### Display bar

The bar can be hidden.

1. In the Inspector window, activate "Properties > Properties > Layout".
2. Deactivate "Display bar".

##### Behavior during operation

The displayed value on the slider control may deviate from the actual value of the associated tag in the following circumstances:

- The value range (minimum and maximum value) configured for the slider control does not correspond to the configured limits for the slider control tag.
- An invalid password has been entered for a password-protected slider control.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Key switch (Panels, Comfort Panels)

##### Use

The object "KeySwitch" is an optional control element for the SIMATIC Mobile Panel. In runtime, the key switch is used to lock functions that can be triggered from the Mobile Panel.

You configure the object "Key switch" object in the "global screen".

![Use](images/1473615243_DV_resource.Stream@PNG-de-DE.png)

##### Tag

The "Tag" property is used to specify the "Key switch" object assignment in the global screen.

> **Note**
>
> **Notes on configuring**
>
> When starting runtime and every time the key is pressed the current position of the key switch is written to the tag. In doing so it can cause inconsistencies between the position of the key switch and the key switch tags.
>
> A specific configuration is required to make sure that the key switch tag reflects the actual position of the key switch at all times. See the instructions below for the basic procedure.
>
> 1. If the tag has a process connection, the current value is transferred from the PLC to the tag after establishment of communication. The tag that contains the current position of the key is overwritten by this process. It can be that the key switch tag no longer reflects the current value of the key switch, e.g. if the Mobile Panel is switched off while the key is being turned.
> 2. If the key switch is pressed before communication with the PLC has been established (e.g. after a device start-up), it may not be possible to send the value of the key switch tag to the PLC. In this case the value of the tag in the PLC is different from the current position of the key.

##### Basic procedure

1. Specify the connection to the PLC in the "Connections" editor. Activate the "Coordination" area pointer to ensure that the life bit is available to the PLC side.

   ![Basic procedure](images/47175657739_DV_resource.Stream@PNG-en-US.png)

   ![Basic procedure](images/47175657739_DV_resource.Stream@PNG-en-US.png)
2. Create three tags in the "Tag" editor.

   - Internal tag: Position_Keyswitch
   - External tag: Auxiliary tag
   - External tag: Keyswitch_PLC
3. Open the Inspector window of the "Position_Keyswitch" tag.
4. In the Inspector window, select "Properties > Events > Value change".
5. Click the first line of the function list. The list opens, showing the system functions available in the project.
6. Select the "SetTag" system function.

   - Select the "Keyswitch_PLC" tag at "Tag (output)".
   - Select the "Position_Keyswitch" tag at "Value".

     ![Basic procedure](images/74752678539_DV_resource.Stream@PNG-en-US.png)

     ![Basic procedure](images/74752678539_DV_resource.Stream@PNG-en-US.png)

     The value of the "Keyswitch_PLC" tag is written to the PLC with the "Position_Keyswitch" tag. A program in the PLC evaluates the life bit. If communication is established, the current value is written to the "Keyswitch_PLC" tag from the PLC.
7. Open the Inspector window of the "Auxiliary tag" tag.
8. In the Inspector window, select "Properties > Events > Value change".
9. Click the first line of the function list. The list opens, showing the system functions available in the project.
10. Select the "SetTag" system function.

    - Select the "Keyswitch_PLC" tag at "Tag (output)".
    - Select the "Position_Keyswitch" tag at "Value".

      ![Basic procedure](images/72559063691_DV_resource.Stream@PNG-en-US.png)

      ![Basic procedure](images/72559063691_DV_resource.Stream@PNG-en-US.png)

      After establishing communication the current value is written to the "Auxiliary Tag" from the PLC. The "SetTag" system function is executed by the value change in the auxiliary tag. The system function re-allocates the value of the "Position_Keyswitch" tag to the "Keyswitch_PLC".
11. Open the global screen in the "Screen management" editor.
12. Select the key switch in the screen.
13. Select the "Position_KeySwitch" tag in the Inspector window under "Properties > Properties > General > Settings > Tag".

    If you actuate the key switch, the value is written to the "Position_KeySwitch" tag.

#### Sm@rtClient view (Panels, Comfort Panels, RT Advanced)

##### Application

The "Sm@rtClient View" object is used to configure a network connection to the remote monitoring and remote maintenance of a connected unit.

![Application](images/6398981131_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Connect on start: Establishes whether when opening the Sm@rtClient view the connection to the HMI device is automatically created which should be remote-controlled.
- Shared use_ Specifies that an HMI device is shared by several Sm@rtClient Views.
- Local cursor: Specifies whether the cursor data is transferred separately in order to increase the performance.
- Use cursor key scroll: For keyboard devices places the control of the horizontal and vertical scroll with the cursor keys.
- Show controls: Specifies whether there are additional fields for entering the address and password.
- Allow menu: Specifies whether the shortcut menu is enabled to control the Sm@rtClient view.
- Connection type: Establishes the expected transfer speed for the remote monitoring.
- Scaling: Specifies whether the Sm@rtClient view can be zoomed in or out.

##### Connect on start

Establishes whether when opening the Sm@rtClient view the connection to the HMI device is automatically created which is remote-controlled.

1. In the Inspector window, select "Properties > Properties > General".
2. Select "View > Connect on start".

##### Shared use

Define whether the HMI device can be used by several Sm@rtClient views under "Properties > Properties > General > View > Shared".

| Shared use |  |
| --- | --- |
| Enabled | HMI devices on which remote control is activated can access the remote HMI device and control the process. Only one HMI device can be active at a time in this case. A different HMI device can only assume control when there has been no activity on the active HMI device for a specified period of time. |
| Disabled | Only one HMI device can use the remote control at any given time. The activities can be followed on the other HMI devices.   Depending on the settings on the Sm@rtServer the following options are available if another HMI device logs on:  - The HMI device is rejected. - The active HMI device is disconnected and the new HMI device is connected. |

##### Local cursor

If this property is set, then the cursor data is transferred separately.

1. In the Inspector window, select "Properties > Properties > General".
2. Select "View > Local cursor".

##### Display extended objects

If this property is set then there are additional fields for inputting the address and password. For the fields to be shown the "Connect on start" option is not activated.

1. In the Inspector window, select "Properties > Properties > General".
2. Select "View > Show enhanced objects".

##### Allow menu

If this property is set, then a shortcut menu to control the Sm@rtClient view is opened in Runtime.

When operating using the mouse, the left mouse key must remain depressed for a few seconds for the shortcut menu to open.

1. In the Inspector window, select "Properties > Properties > General".
2. Select "View > Allow Menu".

##### Connection type

The "Connection type" property establishes the expected transfer speed for the remote monitoring.

Set the connection type at "Connection type" under "Properties > Properties > General > Connection type" in the Inspector window.

| Connection type |  |
| --- | --- |
| LAN | Connection via network |
| Slow | Connection with a low transfer speed |
| Medium speed | Connection with a medium transfer speed |
| Modem | Connection via an analog modem |
| Very slow | Connection with a very low transfer speed |

##### Scaling

If this property is set, then via "Client scale factor" and "Server scale" you can reduce or enlarge the Sm@rtClient view on the HMI device.

1. In the Inspector window, select "Properties > Properties > Scaling".
2. Select "Scaling > Scaling".
3. Enter the values for the scaling under "Client scale factor" and "Server scale factor".

##### Behavior during operation

If the program cannot resolve the dynamic address of a Sm@rtClient view after a screen change, the system connects to the configured server using the static address of the server. If a tag is now set using the dynamic address, you can make a second connection to this server. As a solution, preset the tags of the dynamic address for example by means of a script.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Memory space view (RT Professional)

##### Application

The "Memory space view" object is used to display the memory space view. You can create one memory space display for each drive.

![Application](images/2701849355_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Drive: Defines the drive whose memory assignment is displayed in the memory space display.
- Monitoring limits: Defines the values for the monitoring limits.

##### Define drive

1. In the Inspector window, activate "Properties > Properties > General".
2. Enter the relevant letter in the "Drive letter" area.

##### Change monitoring limits

Enter the monitoring limits for Alarm, Warning, and Tolerance in the Inspector view. The values are specified as a percentage. The percentage of the occupied memory space is monitored in relation to the total capacity of the specified drive:

1. In the Inspector window, activate "Properties > Properties > General".
2. Enter the value for each monitoring limit as a percentage in the "Limits" area.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Symbol library (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Symbol library" object contains a large collection of ready-to-use icons. These icons are used to represent systems and plant areas in screens.

![Application](images/6407740939_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Select icon: Specifies which library object will be used.
- Fill style: Specifies the graphic design of the object.
- Flip: Specifies the flip type of the library object.
- Rotate: Specifies the angle around which the library object is rotated.
- Fixed aspect ratio Defines whether the aspect ratio is maintained if the size is changed.

##### Select symbol

Select the icon at "Properties > Properties > General" in the Inspector window.

##### Fill style

Specify the design of the library object at "Properties > Properties > Appearance > Style" in the Inspector window.

![Fill style](images/39641093387_DV_resource.Stream@PNG-de-DE.png)

|  |  |  |
| --- | --- | --- |
| 1 | "Hollow" | The library object is displayed in outline. |
| 2 | "Solid" | Black lines remain as outlines. Elements of the icon with a different color are displayed as a main color. |
| 3 | "Original" | The screen object will not be changed. |
| 4 | "Shaded" | Black lines remain as outlines. Elements of the symbol in other colors are displayed as brightness levels of a main color. |

If you change the setting from "hollow" to "original" or "shaded" then the color of the display on the configuration computer will deviate from that on the HMI device. This deviation is caused by the different color resolutions. You may also use a graphic object from the "Graphics" object group. The graphic objects are structured by topic and by depth of color in the "WinCC graphics folder."

##### Flip and rotate

The content of the screen flips around the horizontal or vertical central axis of the icon. The icon can be flipped horizontally, vertically or simultaneously horizontally and vertically.

The screen content rotates around the central point of the icon. The symbol is rotated clockwise in increments of 90, 180, or 270 degrees.

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select the mirroring mode at "Orientation > Mirror image".
3. Select the angle of rotation at "Orientation > Rotate".

##### Fixed aspect ratio

The smaller page of the library object defines the maximum size of the symbol. If you change the size of the library object unproportionally, the symbol is still scaled proportionally. Proceed as follows to configure a fixed aspect ratio:

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select "Form > Fixed aspect ratio".

##### Behavior during operation

The possibility of operating the mouse is indicated in Runtime by the cursor symbol changing, depending on the configuration. Operation feedback, e.g. by means of a color change, does not take place.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Symbolic I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Application

The "Symbolic I/O field" object can be used to configure a selection list for input and output of texts in Runtime.

![Application](images/58122044811_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Mode: Specifies the response of the object in Runtime.
- Text list: Specifies the text list that is linked to the object.
- Button for selection list: Specifies that the object has a button to open the selection list.

  > **Note**
  >
  > **Reports**
  >
  > In reports, symbolic I/O fields only output data. "Output" mode is preset. Properties for configuring the selection of graphics are not available, e.g. "button for selection list".

##### Mode

The response of the symbolic I/O field is specified in the Inspector window in "Properties > Properties > General > Type".

| Mode | Description |
| --- | --- |
| "Output" | The symbolic I/O field is used to output values. |
| "Input" | The symbolic I/O field is used to input values. |
| "Input/output" | The symbolic I/O field is used for the input and output of values. |
| "Two states" | The symbolic I/O field is used only to output values and has a maximum of two states. The field switches between two predefined texts. This is used, for example, to visualize the two states of a valve: closed or open. |

> **Note**
>
> The behavior possible for the symbolic I/O field depends on the Runtime.

##### Text list

In the Inspector window, you specify which text list is linked to the symbolic I/O field.

1. In the Inspector window, select "Properties > Properties > General".
2. Under "Contents" open the selection list for "Text list".
3. Select a text list.

##### Button for selection list

The "Button for selection list" property is used to display a button for opening the selection list.

1. Select "Properties > Properties > Layout" in the Inspector window.
2. Select "Response > Button for selection list".

**Note**

**Basic Panels**

The "Button for selection list" option is not available for Basic Panels.

##### Behavior during operation

The selection list of the symbolic I/O field displays an empty text line if a corresponding entry was not defined in the project. The active state is indicated on the HMI device by changing the color of contents of the symbolic I/O field.

##### Special features

- The "corner radius" property is not available for a symbolic I/O field on Comfort Panels or RT Advanced. The corner radius that you specify for the "Symbolic I/O field" object in the style editor has no effect in the screen editor for these target systems.

---

**See also**

[Connecting tags and text lists in the text (RT Advanced)](#connecting-tags-and-text-lists-in-the-text-rt-advanced)
  
[Graphic I/O field (Basic Panels, Panels, Comfort Panels, RT Advanced)](#graphic-io-field-basic-panels-panels-comfort-panels-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Symbolic I/O field (RT Professional)

##### Application

The "Symbolic I/O field" object can be used to configure a selection list for input and output of texts in Runtime.

![Application](images/58122044811_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can customize the following properties in particular:

- Mode: Specifies the response of the object in Runtime.
- Text list: Specifies the text list that is linked to the object.

##### Mode

The response of the symbolic I/O field is specified in the Inspector window in "Properties > Properties > General > Type".

| Mode | Description |
| --- | --- |
| "Output" | The symbolic I/O field is used to output values. |
| "Input" | The symbolic I/O field is used to input values. |
| "Input/output" | The symbolic I/O field is used for the input and output of values. |
| "Two states" | The symbolic I/O field is used only to output values and has a maximum of two states. The field switches between two predefined texts. This is used, for example, to visualize the two states of a valve: closed or open. |

##### Text list

In the Inspector window you specify which text list is linked to the symbolic I/O field.

1. In the Inspector window, select "Properties > Properties > General":
2. Open the selection list for "Text list".
3. Select a text list.

---

**See also**

[Graphic I/O field (RT Professional)](#graphic-io-field-rt-professional)
  
[Configure operator input alarms (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configure-operator-input-alarms-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### System diagnostics view (Basic Panels)

##### Introduction

The system diagnostics view offers you an overview of all the available devices in your plant. You navigate directly to the cause of the error and to the relevant device. You have access to all diagnostics-capable devices which you have configured in the "Devices & networks" editor.

##### Use

The system diagnostics view enables you to achieve the maximum level of detail of the diagnostics data. A precise diagnosis is possible, as all the available data is displayed. You have the system status of the entire plant at one glance.

##### Views in the system diagnostics view

A simple system diagnostics view is available on Basic Panels with a device version prior to V13.

![Views in the system diagnostics view](images/84538686987_DV_resource.Stream@PNG-de-DE.png)

The advanced system diagnostics view is available on Basic Panels with a device version of V13 or later.

![Views in the system diagnostics view](images/84538691467_DV_resource.Stream@PNG-en-US.PNG)

Three different views are available in the system diagnostics view.

- Device view
- Diagnostic buffer view
- Detail view

##### Device view

The device view of the system diagnostics view shows all the available connections in tabular form. Double-clicking a connection opens the detail view. The device view is only displayed if more than one connection has been created in the "Devices & Networks" editor.

##### Diagnostic buffer view

In the diagnostic buffer view, the current data from the diagnostic buffer is displayed.

##### Detail view

The detail view gives detailed information about the selected connection. You cannot sort error texts in the detail view. The detail view is only available if there is an integrated connection to an S7-1200 or S7-1500.

##### Layout

You change the settings for the position, geometry, style, color, and font of the object in the Inspector window. You can adapt the following properties in particular:

- Lines per entry: Specifies the number of lines that are shown for an entry.

##### Configuring the system diagnostics view

1. Drag-and-drop the system diagnostics view from the toolbox.
2. In the Inspector window, select "Properties > Layout".
3. Enter a number under "Lines per entry", i.e. 5.
4. Select an authorization for operation in "Properties > Properties > Security".

---

**See also**

[Basic Panel basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-panel-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring system diagnostics objects (Basic Panels, Panels, Comfort Panels, RT Advanced)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-system-diagnostics-objects-basic-panels-panels-comfort-panels-rt-advanced)

#### System diagnostics view (Panels, Comfort Panels, RT Advanced)

##### Introduction

The system diagnostics view offers you an overview of all the available devices in your plant. You navigate directly to the cause of the error and to the relevant device. You have access to all diagnostics-capable devices which you have configured in the "Devices & networks" editor.

##### Application

The system diagnostics view enables you to achieve the maximum level of detail of the diagnostics data. A precise diagnosis is possible, as all the available data is displayed. You have the system status of the entire plant at one glance.

![Application](images/76412792587_DV_resource.Stream@PNG-en-US.png)

Four different views are available in the system diagnostics view.

- Device view
- Detail view
- Diagnostic buffer view
- Distributed I/O view

> **Note**
>
> The "System diagnostics view" object cannot be used in faceplates.

##### Layout

You change the settings for the position, geometry, style, color, and font of the object in the Inspector window. You can adapt the following properties in particular:

- Columns: Defines the elements of the device view and detail view.
- Show split view: Specifies that the device view and the detail view are shown simultaneously.

##### Configuring the system diagnostics view

1. Drag-and-drop the system diagnostics view from the toolbox.
2. You define the start view for the system diagnostics view under "Properties > Properties > General > Mode".
3. In the Inspector window, select "Properties > Properties > Columns".
4. Select the columns that you require in the device view for Runtime, for example, Operating mode, Name, Slot.
5. Select the columns which you need in the detail view for runtime, e.g., Operating mode, Name, Address.
6. Select the columns that you require in the diagnostic buffer view, e.g., Status, Name, Rack.
7. Customize the column headers, if necessary.
8. Enter "IP" for "Address", for example.

   The column header "IP" is displayed in the device view in Runtime.
9. Rename other elements if necessary.
10. Select an authorization for operation in "Properties > Properties > Security".

##### Showing device view and detail view in a single display

You can split the system diagnostics view and allow the device and detail view to be shown in the same window.

1. In the Inspector window, click "Properties > Properties > Layout".
2. Activate "Show split view".

##### Symbols in the system diagnostics view

| Icon | Function |
| --- | --- |
| ![Symbols in the system diagnostics view](images/21518648075_DV_resource.Stream@PNG-de-DE.png) | Device in operation |
| ![Symbols in the system diagnostics view](images/21517504779_DV_resource.Stream@PNG-de-DE.png) | Device cannot be accessed |
| ![Symbols in the system diagnostics view](images/21518640651_DV_resource.Stream@PNG-de-DE.png) | Errors in device |
| ![Symbols in the system diagnostics view](images/67719993227_DV_resource.Stream@PNG-de-DE.png) | Input/output data are not available |
| ![Symbols in the system diagnostics view](images/21518633227_DV_resource.Stream@PNG-de-DE.png) | Device deactivated |
| ![Symbols in the system diagnostics view](images/21519127947_DV_resource.Stream@PNG-de-DE.png) | Maintenance required |
| ![Symbols in the system diagnostics view](images/21519135371_DV_resource.Stream@PNG-de-DE.png) | Maintenance recommended |
| ![Symbols in the system diagnostics view](images/39262041867_DV_resource.Stream@PNG-de-DE.png) | Superimposed symbol  Shows the subordinate status |
| ![Symbols in the system diagnostics view](images/39261970059_DV_resource.Stream@PNG-de-DE.png) | Current configuration |
| ![Symbols in the system diagnostics view](images/21518659723_DV_resource.Stream@PNG-de-DE.png) | Stop e.g. Update, Boot, Own initialization |
| ![Symbols in the system diagnostics view](images/21528643979_DV_resource.Stream@PNG-de-DE.png) | Stop |
|  |  |

---

**See also**

[System diagnostics window (Panels, Comfort Panels, RT Advanced)](#system-diagnostics-window-panels-comfort-panels-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Panels and Runtime Advanced basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#panels-and-runtime-advanced-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring system diagnostics objects (Basic Panels, Panels, Comfort Panels, RT Advanced)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-system-diagnostics-objects-basic-panels-panels-comfort-panels-rt-advanced)

#### System diagnostics view (RT Professional)

##### Introduction

The system diagnostics view offers you an overview of all the available devices in your plant. You navigate directly to the cause of the error and to the relevant device. You have access to all diagnostics-capable devices which you have configured in the "Devices & networks" editor.

##### Use

The system diagnostics view enables you to achieve the maximum level of detail of the diagnostics data. A precise diagnosis is possible, as all the available data is displayed. You have the system status of the entire plant at one glance.

![Use](images/97216230155_DV_resource.Stream@PNG-en-US.png)

Three different views are available in the system diagnostics view.

- Device view
- Detail view
- Diagnostic buffer view

> **Note**
>
> The "System diagnostics view" object cannot be used in faceplates.

##### Layout

You change the settings for the position, geometry, style, color, and font of the object in the Inspector window. You can adapt the following properties in particular:

- Columns: Defines the elements of the device view and detail view.
- Show split view: Specifies that the device view and the detail view are shown simultaneously.

##### Configuring the system diagnostics view

1. Drag-and-drop the system diagnostics view from the toolbox.
2. In the Inspector window, select "Properties > Properties > Columns".
3. Select the columns that you require in the device view for Runtime, for example, status, name, slot.
4. Select the columns which you need in the detail view for runtime, e.g., status, name, address.
5. Customize the column headers, if necessary.
6. Enter "IP" for "Address", for example.

   The column header "IP" is displayed in the device view in runtime.
7. Rename other elements if necessary.
8. Select an authorization for operation in "Properties > Properties > Security".

##### Showing device view and detail view in a single display

You can split the system diagnostics view and allow the device and detail view to be shown in the same window.

1. In the Inspector window, click "Properties > Properties > Layout".
2. Activate "Show split view".

##### Single display

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select "Mode > Display type > Single".

##### Symbols in the system diagnostics view

| Icon | Function |
| --- | --- |
| ![Symbols in the system diagnostics view](images/21518648075_DV_resource.Stream@PNG-de-DE.png) | Device in operation |
| ![Symbols in the system diagnostics view](images/21517504779_DV_resource.Stream@PNG-de-DE.png) | Device cannot be accessed |
| ![Symbols in the system diagnostics view](images/21518640651_DV_resource.Stream@PNG-de-DE.png) | Errors in device |
| ![Symbols in the system diagnostics view](images/67719993227_DV_resource.Stream@PNG-de-DE.png) | Input/output data are not available |
| ![Symbols in the system diagnostics view](images/21518633227_DV_resource.Stream@PNG-de-DE.png) | Device deactivated |
| ![Symbols in the system diagnostics view](images/21519127947_DV_resource.Stream@PNG-de-DE.png) | Maintenance required |
| ![Symbols in the system diagnostics view](images/21519135371_DV_resource.Stream@PNG-de-DE.png) | Maintenance recommended |
| ![Symbols in the system diagnostics view](images/39262041867_DV_resource.Stream@PNG-de-DE.png) | Superimposed symbol  Shows the subordinate status |
| ![Symbols in the system diagnostics view](images/39261970059_DV_resource.Stream@PNG-de-DE.png) | Current configuration |
| ![Symbols in the system diagnostics view](images/21518659723_DV_resource.Stream@PNG-de-DE.png) | Stop e.g. Update, Boot, Own initialization |
| ![Symbols in the system diagnostics view](images/21528643979_DV_resource.Stream@PNG-de-DE.png) | Stop |
|  |  |

---

**See also**

[Runtime Professional basics (RT Professional)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#runtime-professional-basics-rt-professional)
  
[Configuring system diagnostics objects (RT Professional)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-system-diagnostics-objects-rt-professional)
  
[Example: System diagnostics with all objects (RT Professional)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#example-system-diagnostics-with-all-objects-rt-professional)

#### System diagnostics window (Panels, Comfort Panels, RT Advanced)

##### Introduction

The system diagnostics window offers you an overview of all the available devices in your plant. You navigate directly to the cause of the error and to the relevant device. You have access to all diagnostics-capable devices which you have configured in the "Devices & networks" editor.

The system diagnostics window is only available in the global screen.

##### Application

The system diagnostics window enables you to achieve the maximum level of detail of the diagnostics data. A precise diagnosis is possible, as all the available data is displayed. You have the system status of the entire plant at one glance.

![Application](images/74865273995_DV_resource.Stream@PNG-en-US.png)

Four different views are available in the system diagnostics window.

- Device view
- Detail view
- Diagnostic buffer view
- Distributed I/O view

> **Note**
>
> The "System diagnostics window" object cannot be used in faceplates.

##### Layout

You change the settings for the position, geometry, style, color, and font of the object in the Inspector window. You can adapt the following properties in particular:

- Columns: Defines the elements of the device view and detail view.
- Table headers: Specifies the table headers of the view.
- Window: Specifies whether the system diagnostics window can be closed, for example.

##### Configuring the system diagnostics window

1. Drag and drop the system diagnostics view from the toolbox into the global screen.
2. You define the start view for the system diagnostics window under "Properties > Properties > General > Mode".
3. In the Inspector window, select "Properties > Properties > Columns".
4. Select the columns that you require in the device view for Runtime, e.g., Operating mode, Name, Slot.
5. Select the columns that you require in the detail view for Runtime, e.g., Operating mode, Name, Plant designation.
6. To change a column header, click in the field and (for example) enter "IP" for "Address".

   The column header "IP" is displayed in the device view in Runtime.
7. Rename other elements if necessary.
8. To be able to close the system diagnostics window in Runtime, select "Properties > Properties > Window > Closable" in the Inspector window.

##### Icons in the system diagnostics window

| Button | Function |
| --- | --- |
| ![Icons in the system diagnostics window](images/21518648075_DV_resource.Stream@PNG-de-DE.png) | Device in operation |
| ![Icons in the system diagnostics window](images/21517504779_DV_resource.Stream@PNG-de-DE.png) | Device cannot be accessed |
| ![Icons in the system diagnostics window](images/21518640651_DV_resource.Stream@PNG-de-DE.png) | Errors in device |
| ![Icons in the system diagnostics window](images/21518633227_DV_resource.Stream@PNG-de-DE.png) | Device deactivated |
| ![Icons in the system diagnostics window](images/67719993227_DV_resource.Stream@PNG-de-DE.png) | Input/output data are not available |
| ![Icons in the system diagnostics window](images/21519127947_DV_resource.Stream@PNG-de-DE.png) | Maintenance required |
| ![Icons in the system diagnostics window](images/21519135371_DV_resource.Stream@PNG-de-DE.png) | Maintenance recommended |
| ![Icons in the system diagnostics window](images/39262041867_DV_resource.Stream@PNG-de-DE.png) | Superimposed symbol  Shows the subordinate status |
| ![Icons in the system diagnostics window](images/39261970059_DV_resource.Stream@PNG-de-DE.png) | Current configuration |
| ![Icons in the system diagnostics window](images/21518659723_DV_resource.Stream@PNG-de-DE.png) | Stop e.g. Update, Boot, Own initialization |
| ![Icons in the system diagnostics window](images/21528643979_DV_resource.Stream@PNG-de-DE.png) | Stop |
|  |  |

##### System diagnostics window: Show wire break error

You have activated wire break diagnostics for a module. The error text is displayed in the system diagnostics window when a wire break error occurs. You can see the error text and possible causes of the error in the module detail view. Output of the channel number of the affected channel is not supported.

---

**See also**

[System diagnostics view (Panels, Comfort Panels, RT Advanced)](#system-diagnostics-view-panels-comfort-panels-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Panels and Runtime Advanced basics (Basic Panels, Panels, Comfort Panels, RT Advanced)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#panels-and-runtime-advanced-basics-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring system diagnostics objects (Basic Panels, Panels, Comfort Panels, RT Advanced)](Configuring%20system%20diagnostics%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-system-diagnostics-objects-basic-panels-panels-comfort-panels-rt-advanced)

#### Table view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

You use the "Table view" object to display the tag values in a table. You can display current, or logged values in the table.

![Use](images/100714069131_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, colors and font types of the object. You can adapt the following properties in particular:

- Configuring data source and columns
- Configuring a table
- Window settings
- Persistence
- Toolbar

##### Configuring data source and columns

1. Open "Properties > Properties > Value column".
2. Select the log tag or compressed log tag that supplies the column with values under "Data source".
3. Under "Time column", select the column of the table view in which the data source is to be displayed.
4. Select the time range of the table under "Properties > Properties > Time column > Time range":

   - "Time span": You define the time range using a starting time and a following time span.
   - "End time": You define the time range using a starting time and an end time.
   - "Measuring points": You define the time range using a starting time and a number of measuring points.
5. Use "Format > Update" to specify whether the table displays the values statically or the values are refreshed.
6. Under "Style" specify the format for displaying the time and the alignment within the column.

##### Configuring a table

Under "Properties > Properties > Table", you specify whether the columns of the table have a title and whether the grid lines of the table are displayed.

##### Window settings

Under "Properties > Properties > Layout > Window" you define whether the user can change the size of the window and close the window in Runtime.

##### Persistence

Under "Properties > Properties > Security > Persistence", define how long a user's changes to the trend view in runtime are retained.

- "Allow persistence"

  Users can change settings. Changes are retained until the next screen change.
- "Persistence until logoff"

  User group changes are retained until logoff.
- "Persistence until next loading"

  User group changes are retained until the project is updated on the HMI device.

##### Toolbar

You define the operator controls of the table view in Runtime in the "Properties > Properties > Toolbar" inspector window. The following operator controls are available for the table view:

| Button | Name | Function |
| --- | --- | --- |
| ![Toolbar](images/23982571147_DV_resource.Stream@PNG-de-DE.png) | Online help | Opens the online help. |
| ![Toolbar](images/23942155147_DV_resource.Stream@PNG-de-DE.png) | Open configuration | Opens the configuration dialog. |
| ![Toolbar](images/102411264395_DV_resource.Stream@PNG-de-DE.png) | First data record | Browse the log: Shows the tag values starting with the first logged value. |
| ![Toolbar](images/102411268235_DV_resource.Stream@PNG-de-DE.png) | Previous data record | Browse the log: Shows the tag values in the previous time interval. |
| ![Toolbar](images/102411284875_DV_resource.Stream@PNG-de-DE.png) | Next data record | Browse the log: Shows the tag values in the subsequent time interval. |
| ![Toolbar](images/102411288715_DV_resource.Stream@PNG-de-DE.png) | Last data record | Browse the log: Shows the tag values up to the last logged value. |
| ![Toolbar](images/23926371723_DV_resource.Stream@PNG-de-DE.png) | Edit data | Allows the editing of data in any table field that is opened when the user double-clicks it. |
| ![Toolbar](images/23929835147_DV_resource.Stream@PNG-de-DE.png) | Tag selection | Opens the dialog for selecting the log and tags. |
| ![Toolbar](images/23926797707_DV_resource.Stream@PNG-de-DE.png) | Select column | Opens the dialog for setting the visibility of columns. |
| ![Toolbar](images/102411252619_DV_resource.Stream@PNG-de-DE.png) | Time range selection | Opens the dialog for setting the time range displayed in the table view. |
| ![Toolbar](images/23926805899_DV_resource.Stream@PNG-de-DE.png) | Previous column | Displays the previous column in the foreground |
| ![Toolbar](images/23927518091_DV_resource.Stream@PNG-de-DE.png) | Next column | Displays the next column in the foreground |
| ![Toolbar](images/102411244939_DV_resource.Stream@PNG-de-DE.png) | Start/end update | Stops and starts the column update. The values are buffered and updated as soon as you start column update again. |
| ![Toolbar](images/23931759499_DV_resource.Stream@PNG-de-DE.png) | Print log | Starts printing the columns displayed in the table view. You define the print job under "General > Print > Print job". |
| ![Toolbar](images/23932623883_DV_resource.Stream@PNG-de-DE.png) | Selection of the statistics area | Enables you to define a time range for which statistical values are determined. |
| ![Toolbar](images/23932725131_DV_resource.Stream@PNG-de-DE.png) | Statistics window | Opens a statistics window to display the minimum, maximum, means, and standard deviation for the selected time range and the selected column. |

##### Dynamizing the value column in the table view (RT Professional)

Note the following information about dynamizing the properties in the value column of a table view:

- The "ValueColumnName" property specifies the name of the selected value column. The "ValueColumnName" attribute can be dynamized with the "ValueColumnRename" attribute. The data type is STRING.
- The "ValueColumnRename" property changes the name of the value column referenced with the "ValueColumnIndex" attribute. The attribute can be dynamized with the "ValueColumnRename" name. With "ValueColumnRename" you also dynamize the "ValueColumnName" attribute. The data type is STRING.
- The "TimeColumnName" property specifies the name of the selected time column. The "TimeColumnName" attribute can be dynamized with the "TimeColumnRename" attribute. The data type is STRING.
- The "TimeColumnRename" property changes the name of the time column referenced with the "TimeColumnIndex" attribute. The attribute can be dynamized with the "TimeColumnRename" name. With "TimeColumnRename" you also dynamize the "TimeColumnName" attribute. The data type is STRING.

---

**See also**

[f(t) trend view (RT Professional)](#ft-trend-view-rt-professional)
  
[f(x) trend view (RT Professional)](#fx-trend-view-rt-professional)
  
[Configuring the Table View (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-the-table-view-rt-professional)
  
[Value table (RT Professional)](#value-table-rt-professional)
  
[Configuring persistence (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-persistence-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Operating table view in Runtime (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#operating-table-view-in-runtime-rt-professional)

#### Text field (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Text field" is a closed object which you can fill with a color.

![Application](images/56785035659_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Text: Specifies the text for the text field.
- Size of text field: Defines whether the size of the object is adapted to the space required by the largest list entry.

##### Text

Specify the text for the text field in the Inspector window.

1. In the Inspector window, select "Properties > Properties > General".
2. Enter a text.

   For texts over several lines you can set a line break by pressing the key combination <Shift + Enter>.

##### Size of text field

In the Inspector window, you can define whether the size of the object is adapted to the space required by the largest list entry.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Activate "Resize > Fit to contents".

---

**See also**

[Connecting tags and text lists in the text (RT Advanced)](#connecting-tags-and-text-lists-in-the-text-rt-advanced)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### T-piece (RT Professional)

##### Application

You use the "T piece" object to reproduce a T-shaped pipe junction. To reproduce a pipe system, connect the "T piece" object to other objects, e.g. pipe or pipe bend.

![Application](images/21175453835_DV_resource.Stream@PNG-de-DE.png)

##### Layout

Customize the object position and color in the Inspector window. You can adapt the following properties in particular:

Rotation: Specifies the angle of rotation in degrees of the T piece.

##### Rotation

You specify by how many degrees the "T piece" is rotated under "Properties > Properties > Layout > Rotation" in the Inspector window. The value entered is automatically rounded to a multiple of 90.

- 0: the "leg" of the T piece is pointing downward
- 90: the "leg" of the T piece is pointing to the left
- 180: the "leg" of the T piece is pointing upward
- 270: the "leg" of the T piece is pointing to the right

---

**See also**

[Pipe (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#pipe-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Pipe elbow (RT Professional)](#pipe-elbow-rt-professional)
  
[Double T-piece (RT Professional)](#double-t-piece-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Clock (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Application

The "Clock" object displays the date and time.

![Application](images/118533042187_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Analog display: Specifies whether the clock is shown as an analog clock or digital clock.
- Display clock dial: Specifies whether hour marks of the analog clock will be displayed.
- Width and length of hands: Specifies the width and length of the hands.

##### Analog display

In the Inspector window you can specify whether the clock is displayed as an analog or digital clock. The digital clock shows both the time and the date. The display format depends on the language set on the HMI device.

1. In the Inspector window, select "Properties > Properties > General":
2. Activate "Analog".

##### Display dial

In the Inspector window you can specify whether hour marks will be displayed.

1. In the Inspector window, select "Properties > Properties > General":
2. Activate "Analog".
3. Activate "Show dial".

##### Width and length of hands

The width of the second hand, minute hand and hour hand is set for the analog display.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter values for "width" and "length".

   The values for the length are interpreted as a percentage of the size of the clock. The value for the length of the second hand influences the radius of the dial at the same time.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Connector (RT Professional)

##### Application

You use the "Connector" object to interconnect several objects using a line. You can also attach multiple connectors to one another.

There are two types of connector:

- Automatic: The connector consists of horizontal and vertical parts.

  ![Application](images/25860009355_DV_resource.Stream@PNG-de-DE.png)
- Single: The connecting points are connected by a straight line.

  ![Application](images/25861293195_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the object position, shape, style, and color. You can adapt the following properties in particular:

- Line style
- Line start and end

##### Connecting objects

To connect objects, join the ends of the connectors to the connecting points on the objects.

1. Click the "Connector" object in the "Tools" task card.
2. Click on an object in the screen. The connector is connected to the first object.
3. Click on another object in the screen.

   Both objects are connected to each other.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Value table (RT Professional)

##### Application

You use the "Value table" object to show evaluated data and statistics in a table.

![Application](images/88167011211_DV_resource.Stream@PNG-en-US.png)

- f(t) trend view
- f(x) trend view
- Table view

##### Layout

In the Inspector window, you customize the position, geometry, style, colors and font types of the object. You can adapt the following properties in particular:

- Data source for displaying the values
- Mode
- Toolbar

##### Data source for displaying the values

You define which values are displayed in the value table in the "Properties > Properties > General > Data source" inspector window.

Select among the following objects:

- f(t) trend view
- f(x) trend view
- Table view

By default, the configuration for the display format, the format is taken from the connected control. The size, value range and zoom factor of the control are taken into account to display the optimum number of decimal places. You can configure the display formats for individual values in the Inspector window of the value table yourself, for example, to show a precise number of decimal places.

##### Mode

You define the mode in the "Properties > Properties > General > Mode" inspector window. You have a choice of three different types depending on the data source.

- The ruler window shows the coordinate values of the trends on the ruler or values of a selected line in the table.
- The statistics area window shows the values of the lower limit and upper limit of the trends between two rulers or the selected area in the table. The statistics area window is not provided for the object f(x) trend view.
- The statistics window shows the statistical evaluation of the trends between two rulers or the selected values in the table. The statistics window is not provided for the object "f(x) trend view".

##### Toolbar

You define the control elements of the value table in Runtime in the "Properties > Properties > Toolbar - Toolbar - Buttons" inspector window. The following control elements are available for the recipe data:

|  |  |  |
| --- | --- | --- |
| **Button** | **Brief description** | **Description** |
| ![Toolbar](images/23448984971_DV_resource.Stream@PNG-de-DE.png) | Tooltip | Calls help for the WinCC value table. |
| ![Toolbar](images/44727320715_DV_resource.Stream@PNG-de-DE.png) | Configuration dialog box | Opens the configuration dialog box in which you change the properties of the value table. |
| ![Toolbar](images/44732127627_DV_resource.Stream@PNG-de-DE.png) | Ruler window | You query the coordinate points of a trend with the button. The trend data are displayed in the ruler window. |
| ![Toolbar](images/102411256459_DV_resource.Stream@PNG-de-DE.png) | Define statistics area | Enables you to define a time range for which statistics values are determined. |
| ![Toolbar](images/44732131595_DV_resource.Stream@PNG-de-DE.png) | Calculating statistics | The button shows the statistical values in the statistics window. The displayed values refer to a selected trend with the configured calculation time period. The button can only be pressed if a statistics window is connected with an f(t) trend view. |
| ![Toolbar](images/44732123659_DV_resource.Stream@PNG-de-DE.png) | Printing | Start the print-out of the values shown in the table. You define the print job to be used in the "Properties > Properties > General > Print job" inspector window. |
| ![Toolbar](images/44731625483_DV_resource.Stream@PNG-de-DE.png) | Exporting data | This button is used for exporting all or the selected runtime data into a "CSV" file. If the "Properties > Properties > Data export > Show dialog" inspector window is activated, a dialog box opens in runtime. The dialog box offers you settings for the export and starting the export. With the appropriate authorizations you can also select the file and the directory for the export. If no dialog box is displayed, the data export to the preset file starts immediately. |
| ![Toolbar](images/44731633419_DV_resource.Stream@PNG-de-DE.png) | Customized 1 | Shows the first key function created by the user. The function of the button is user-defined. |

---

**See also**

[Table view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#table-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[f(t) trend view (RT Professional)](#ft-trend-view-rt-professional)
  
[f(x) trend view (RT Professional)](#fx-trend-view-rt-professional)
  
[Value table basics (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#value-table-basics-rt-professional)
  
[Configuring the value table (RT Professional)](Displaying%20Tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-the-value-table-rt-professional-1)
  
[Configuring persistence (RT Professional)](Compiling%20and%20loading%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-persistence-rt-professional)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### WLAN reception (Panels, Comfort Panels)

##### Application

The "WLAN reception" object is a control element for some SIMATIC Mobile Panels. The "WLAN reception" object displays the signal strength of the WLAN wireless connection. In addition, the signal strength is measured and displayed by means of 5 bars.

##### Layout

| Symbol | Meaning | Signal strength |
| --- | --- | --- |
| ![Layout](images/21144982411_DV_resource.Stream@PNG-de-DE.png) | No wireless connection | No signal |
| ![Layout](images/21144985483_DV_resource.Stream@PNG-de-DE.png) | Very poor wireless connection | =<20 % |
| ![Layout](images/21144993035_DV_resource.Stream@PNG-de-DE.png) | Poor wireless connection | >20 % =<40 % |
| ![Layout](images/21145410187_DV_resource.Stream@PNG-de-DE.png) | Wireless connection OK | >40 % =<60 % |
| ![Layout](images/21145520139_DV_resource.Stream@PNG-de-DE.png) | Good wireless connection | >60 % =<80 % |
| ![Layout](images/21145527691_DV_resource.Stream@PNG-de-DE.png) | Very good wireless connection | >80 % |

##### Operation

The object is for display only and cannot be controlled by the operator.

---

**See also**

[Charge condition (Panels, Comfort Panels)](#charge-condition-panels-comfort-panels)
  
[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Gauge (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Use

The "Gauge" object shows numeric values in the form of an analog gauge. For example, a glance in Runtime is enough to note that the boiler pressure is in the normal range.

> **Note**
>
> The gauge is for display only and cannot be controlled by the operator.
>
> Configure system functions that are performed at value changes in the tag properties at the "Value change" event and not at the "Change" event of the gauge. If your project is to comply with Good Manufacturing Practices, and the system function performs a GMP-relevant action. e.g. increasing a GMP-relevant tag, every value change of the tag used at the gauge is interpreted as a user action.

![Use](images/58122226059_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Display peak value pointer: Specifies whether the actual measurement range is indicated with a slave pointer.
- Maximum Value and Minimum Value: Specifies the top and bottom values of the scale.
- Start value of the danger range and start value of the warning range: Specifies the scale value from which the danger range and the warning range start.
- Display normal range: Specifies whether the normal range is shown in color on the scale.
- Color of individual ranges: Different operating modes, such as normal range, warning range and danger range, are shown in different colors so that the operator can distinguish them easily.

> **Note**
>
> The use of many differently sized "Gauge" objects can reduce the performance in Runtime. With "Gauge", avoid minimally different heights and widths, for example, 48 pixels, 49 pixels, 51 pixels, etc. Use the same sizes instead.

##### Display peak value

The "Display peak value" property can be used to activate a marker function for the maximum and minimum pointer movement in Runtime. The actual measurement range is shown with a slave pointer.

1. In the Inspector window, activate "Properties > Properties > Appearance > Show peak values".

##### Maximum Value and Minimum Value

You can set the top and bottom end values of the scale in the Inspector window.

1. In the Inspector window, select "Properties > Properties > General".
2. Enter a number under "Process > Maximum scale value" and for "Minimum scale value".

   If you select a tag as the end value of the scale, the number will be no longer available.

> **Note**
>
> Ensure that the minimum value is always less than the maximum value, especially if you make the minimum value or maximum value dynamic through a tag. If the minimum value is greater than the maximum value, no adjustment is made to the scale end values.

##### Start value of the danger range and start value of the warning range

Define the scale value at which the danger range and the warning range start in the Inspector window.

1. In the Inspector window, select "Properties > Properties > Limits/Ranges".
2. Enter the start value for the danger range in "Upper 2" and the start value for the warning range in "Upper 1".
3. Select "start value of danger range" and "start value of warning range" to display the ranges on the scale.

##### Normal range visible

In the Inspector window, define whether to show the normal range in color.

1. In the Inspector window, select "Properties > Properties > Limits/Ranges".
2. Select "Normal".

##### Color of individual ranges

You can display the normal range, the danger range and the warning range in different colors. Define the color in the Inspector window.

1. In the Inspector window, select "Properties > Properties > Limits/Ranges".
2. Select a color from the color palette for the three areas.

**Note**

The following restrictions apply for HMI devices with Windows CE up to version 5.0:

- The three ranges (normal / warning / danger) are not visualized in different colors in Runtime.

> **Note**
>
> When you select the option "Show ranges from tag", you can display up to five ranges in the gauge whose values are specified by means of a process tag. You define the values for the areas with a process tag, which you interconnect with the screen object.
>
> The option "Show ranges from tag" is available for Comfort Panels, KTP Mobile Panels and RT Advanced.

---

**See also**

[Device dependency of the objects (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#device-dependency-of-the-objects-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
