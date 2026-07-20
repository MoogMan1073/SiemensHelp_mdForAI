---
title: "Configuring screens (RT Unified)"
package: ScreensWCCUenUS
topics: 311
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring screens (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Overview of screen objects (RT Unified)](#overview-of-screen-objects-rt-unified)
- [Configuring screen objects (RT Unified)](#configuring-screen-objects-rt-unified)
- [Using groups (RT Unified)](#using-groups-rt-unified)
- [Configuring text lists and graphics lists (RT Unified)](#configuring-text-lists-and-graphics-lists-rt-unified)
- [Configuring dynamization (RT Unified)](#configuring-dynamization-rt-unified)
- [Trigger events (RT Unified)](#trigger-events-rt-unified)
- [Configuring faceplates (RT Unified)](#configuring-faceplates-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Basics of screens (RT Unified)](#basics-of-screens-rt-unified)
- ["Screens" editor (RT Unified)](#screens-editor-rt-unified)
- [Defining the start screen: (RT Unified)](#defining-the-start-screen-rt-unified)
- [Configuring the background color of the screen (RT Unified)](#configuring-the-background-color-of-the-screen-rt-unified)
- [Using styles (RT Unified)](#using-styles-rt-unified)
- [Changing the screen resolution (RT Unified)](#changing-the-screen-resolution-rt-unified)
- [Configuring zooming in runtime without Control key (RT Unified)](#configuring-zooming-in-runtime-without-control-key-rt-unified)
- [Configuring screen management (RT Unified)](#configuring-screen-management-rt-unified)

### Basics of screens (RT Unified)

#### Introduction

In WinCC you create screens that a user can use to control and monitor machines and plants. When you create screens, the pre-defined object templates support you in visualizing your plant, displaying processes and specifying process values.

![Introduction](images/146702890507_DV_resource.Stream@PNG-de-DE.png)

#### Structure of screens

A screen is a graphical representation of your project. In the screen, you configure objects, their properties and connections.

Insert the objects you need to represent the process into your screen. Configure the objects to match the requirements of your process.

![Structure of screens](images/146702894603_DV_resource.Stream@PNG-de-DE.png)

A screen can consist of static and dynamic elements:

- ① Static elements such as text or graphic objects in the screen above do not change in runtime.
- ② Dynamic elements change their status based on the process. You visualize current process values from the memory of the PLC or the HMI device.

  Dynamic objects include, for example, alphanumeric displays, trends and bars, as well as input fields on the HMI device, such as IO fields, switches and sliders.

  Process values and operator inputs are exchanged between the PLC and the HMI device by means of tags.

#### Screen window

You display other project screens in the screen window. The screen window enhances navigation between screens and allows "screen in a screen" display.

You can use screen windows for purposes such as:

- Frequent switching between plant units
- Showing and hiding screens, for example without exiting central process visualization
- Displaying multiple plant units in one screen

---

**See also**

[Resources Monitor (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#resources-monitor-rt-unified)
  
[Creating a user interface efficiently (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#creating-a-user-interface-efficiently-rt-unified)

### "Screens" editor (RT Unified)

This section contains information on the following topics:

- ["Screens" editor - structure (RT Unified)](#screens-editor---structure-rt-unified)
- [Task cards (RT Unified)](#task-cards-rt-unified)
- [Zooming in on the screen in the screen editor (RT Unified)](#zooming-in-on-the-screen-in-the-screen-editor-rt-unified)
- [Using the toolbar in the screen editor (RT Unified)](#using-the-toolbar-in-the-screen-editor-rt-unified)

#### "Screens" editor - structure (RT Unified)

##### Introduction

Use the "Screens" editor to create the visualization of your project. You add the screens to your project in which you configure and manage the graphical objects, their properties and connections.

##### Structure of the user interface

The following screen shows the structure of the user interface with "Screens" editor open:

![Structure of the user interface](images/171982900107_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Project tree |
| ② | Screen editor |
| ③ | Screen editor - screen area visible in runtime |
| ④ | Screen editor - screen area invisible in runtime |
| ⑤ | Task cards |
| ⑥ | Inspector window |

##### Project tree

In the project tree, add the screens to the project in the "Screens" folder.

To open the "Screens" editor, follow these steps:

1. Open the "Screens" folder in the project tree.
2. Add a screen. The "Screens" editor opens.

##### "Screens" editor

The "Screens" editor includes:

- Screen editor with the visible and invisible screen area in runtime
- Task cards
- Inspector window

##### Screen editor - screen area visible in runtime

By default, the screen editor displays only the screen area visible in runtime.

You add the objects from the "Tools" task card to the visible screen area of the screen editor. Here you manage and design the objects.

##### Screen editor - screen area invisible in runtime

When you zoom out on a screen in the screen editor, the screen area that is invisible in runtime appears in the screen editor. For example, you can store the configured objects in the invisible screen area. You cannot zoom the objects in the invisible screen area.

##### Task cards

The following task cards are available in the "Screens" editor:

- Toolbox: Display and operating objects
- Layout: Aid for customizing the display
- Tasks: "Find and replace" function and language selection
- Libraries: Management of the project library and of the global libraries

##### Inspector window

Additional information on a selected object or on the executed actions is displayed in the Inspector window.

The Inspector window consists of the following components:

- "Properties" tab

  This tab displays the object properties. Here you can configure the editable properties, events, texts or expressions.
- "Info" tab

  In this tab, you can display additional information about the object and alarms on the actions carried out, such as compiling.
- "Diagnostics" tab

  This tab provides information on system diagnostics events, configured alarm events, and connection diagnostics.

#### Task cards (RT Unified)

##### Introduction

The following task cards are available in the "Screens" editor:

- Toolbox: Display and operating objects
- Layout: Aid for customizing the display
- Tasks: "Find and replace" function and language selection
- Libraries: Administration of the project library and of the global libraries

##### Toolbox

The "Toolbox" task card contains objects in different palettes:

- Basic objects
- Elements
- Controls
- My controls
- Graphics
- Dynamic widgets

You paste objects from the palettes into the screens by drag&drop or a double click. The objects available for selection are determined by the features of the HMI device you are configuring.

You can toggle between the following views in the "Toolbox" task card:

- Thumbnails view ![Toolbox](images/148545632779_DV_resource.Stream@PNG-de-DE.png)
- List view ![Toolbox](images/148540824203_DV_resource.Stream@PNG-de-DE.png)

In the symbol view you can switch the labeling of the objects on or off in the shortcut menu.

##### Layout

The "Layout" task card contains the following palettes for displaying objects and elements:

- Layers: You manage the layers of screen objects in the "Layers" palette. The layers are displayed in a tree view and contain information about the active layer and the visibility of all layers.
- Grid: You choose the layout mode and turn the grid on and off in the "Grid" palette. You define the grid size in the x and y directions.
- Objects out of range: Objects that lie outside the visible area are displayed with name, position and type.

##### Tasks

The "Tasks" task card contains the following palettes:

- Find and replace: Used to search within an open editor. It includes all options that you need for an efficient search. You have the option of replacing hits individually or automatically replacing all the found texts.
- Languages and resources: Used to select the editing and reference language.

##### Libraries

The "Libraries" task card show the following libraries in separate palettes:

- Project library: In the "Project library" palette, you can store the library elements that you want to use more than once in the project. The project library is stored together with the project.
- Global library: In the "Global libraries" palette, you manage the global libraries whose library elements you want to reuse over several projects. The global library is stored in a separate file in the specified path on your configuration PC.
- Info (project library): The following is displayed in the "Info" palette:

  - The contents of the library elements
  - The individual versions of types
  - The last date of change of the version

#### Zooming in on the screen in the screen editor (RT Unified)

##### Introduction

You can zoom into a screen from the zero point in the screen editor. The zero point is located in the upper left corner of the screen.

##### Requirement

- A screen is open.

##### Zooming the screen from the zero point

To zoom a screen from the zero point, select one of the following options:

- Click the selection list in the lower-right corner of the screen editor.

  ![Zooming the screen from the zero point](images/168731495307_DV_resource.Stream@PNG-en-US.png)

  - Select a percentage value.

    The screen is enlarged or reduced by the selected percentage value.
  - Select "Fit to screen", "Fit to width" or "Fit to height".

    The screen is adapted to the window size, the width or the height of the screen.
- Click the scroll bar to zoom in or out of the screen.

  ![Zooming the screen from the zero point](images/168731499915_DV_resource.Stream@PNG-en-US.png)

  The screen is enlarged or reduced by 25% with each click.
- Use the mouse:

  - Press <Ctrl>. Move the mouse wheel up or down at the same time.

    The screen is zoomed into or out of.
- Use the keyboard:

  - To zoom into the screen, press <Ctrl + Plus>.
  - To zoom out of the screen, press <Ctrl + Minus>.

You zoom into the entire content of the screen. Open pop-up windows are not zoomed.

##### Objects in the zoomed screen

The size of the objects in the screen is adapted proportionally to the zoom factor.

For objects in a screen with a small zoom factor, the bounding box and the handles are adjusted proportionally to the zoom factor.

---

**See also**

[Screen window (RT Unified)](#screen-window-rt-unified)

#### Using the toolbar in the screen editor (RT Unified)

##### Introduction

The toolbar in the screen editor allows you to position the objects in the screen and to configure some properties.

##### Positioning objects

The first half of the screen editor toolbar allows you to:

- Transfer the format of the object
- Rotate objects in the screen
- Align objects
- Move objects forward or backward
- Move objects in layers

![Positioning objects](images/166143463563_DV_resource.Stream@PNG-de-DE.png)

##### Configuring object properties

To efficiently configure the frequently used properties, the second half of the toolbar contains the following functions:

![Configuring object properties](images/166143766539_DV_resource.Stream@PNG-de-DE.png)

- Font:

  - Font
  - Font size
  - Format bold font
  - Format italic font
  - Underline
  - Strikethrough
  - Increase font size
  - Decrease font size
- Horizontal text alignment:

  - Left
  - Centered
  - Right
- Specify border width or line width
- Line type:

  - Solid
  - Dashed
  - Dotted
  - Dash dot
  - Dash dot dot

When a group is selected, the functions for grouped objects are disabled.

If a property can be changed in at least one object, the functions are enabled.

---

**See also**

[Aligning objects (RT Unified)](#aligning-objects-rt-unified)
  
[Transfer format (RT Unified)](#transfer-format-rt-unified)
  
[Rotating object (RT Unified)](#rotating-object-rt-unified)
  
[Moving an object forward or backward (RT Unified)](#moving-an-object-forward-or-backward-rt-unified)

### Defining the start screen: (RT Unified)

#### Introduction

The start screen is the screen displayed when the project is started in runtime. Define a start screen for each target system. From the start screen, the operator navigates to the other screens.

To compile and download a project, a screen must be defined as the start screen in the project.

#### Requirement

- A WinCC Unified PC or a Unified Comfort Panel is installed.
- At least one HMI screen is open.

#### Defining the start screen

To define the start screen, follow these steps:

1. In the project tree, right-click on the screen that you want to define as the start screen.
2. Click "Define as start screen" in the shortcut menu.

   ![Defining the start screen](images/170927241995_DV_resource.Stream@PNG-en-US.png)

   ![Defining the start screen](images/170927241995_DV_resource.Stream@PNG-en-US.png)

Alternatively, right-click in the open "Screens" editor. Click "Define as start screen" in the shortcut menu.

The selected screen is displayed as the start screen when the project is started in runtime.

### Configuring the background color of the screen (RT Unified)

#### Introduction

You can use one of the available styles or configure a specific background color for the screens in your project. This gives you a common layout.

#### Configuring a background color

To configure a background color of the screens, follow these steps:

1. Under "Options > Settings > Visualization > Screens > Colors", deactivate the "Use background color from style (WinCC Unified)" option.

   The option is deactivated by default.

   ![Configuring a background color](images/168405068939_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a background color](images/168405068939_DV_resource.Stream@PNG-en-US.png)
2. Choose one of the available colors in the drop-down list.

In a newly created device, the selected color is used in all screens.

In an existing device, the configured color is used in all newly added screens.

---

**See also**

[Using styles (RT Unified)](#using-styles-rt-unified)

### Using styles  (RT Unified)

This section contains information on the following topics:

- [Defining the style](#defining-the-style)
- [Predefined styles](#predefined-styles)
- [Switching styles by means of user-defined functions (RT Unified)](#switching-styles-by-means-of-user-defined-functions-rt-unified)
- [Custom styles (RT Unified)](#custom-styles-rt-unified)

#### Defining the style

##### Introduction

You can specify predefined styles for Unified devices. Predefined styles are write-protected and cannot be changed.

##### Defining the style

To specify a style, follow these steps:

1. Click "Runtime settings" in the project tree.
2. Select the desired style under "General > Screen":

   - Bright style
   - Dark style
   - Expanded style

![Defining the style](images/162762799115_DV_resource.Stream@PNG-en-US.png)

##### Result

You have specified a new style that is applied to screens, objects or projects.

#### Predefined styles

##### Introduction

You can assign a predefined style to the screens. Select between the following styles:

- Bright style
- Expanded style
- Dark style

##### Bright style

![Bright style](images/168622928011_DV_resource.Stream@PNG-de-DE.png)

##### Expanded style

![Expanded style](images/168622931979_DV_resource.Stream@PNG-de-DE.png)

##### Dark style

![Dark style](images/162761047563_DV_resource.Stream@PNG-de-DE.png)

#### Switching styles by means of user-defined functions (RT Unified)

##### Introduction

In runtime you can use user-defined functions to change or determine the style.

##### Changing a style with user-defined function

To change the style with a user-defined function, use the following code:

`//Switch to bright style`

`HMIRuntime.UI.Style = "FlatStyle_Bright";`

`//Switch to dark style`

`HMIRuntime.UI.Style = "FlatStyle_Dark";`

`//Switch to extended style`

`HMIRuntime.UI.Style = "ExtendedStyle";`

##### Determining a style with user-defined function

To determine the style with a user-defined function, use the following code:

`let MyStyle;`

`MyStyle = HMIRuntime.UI.Style;`

`HMIRuntime.Trace("My current style is: " + MyStyle);`

#### Custom styles (RT Unified)

##### Introduction

In addition to the pre-defined styles in TIA Portal, you can also import your customized styles and apply them in the project.

You can create your own styles with the SIMATIC WinCC Unified Corporate Designer application.

##### SIMATIC WinCC Unified Corporate Designer

SIMATIC WinCC Unified Corporate Designer is a stand-alone application that is aligned to TIA Portal. You can define your own styles in the application. Corporate Designer is offered as a download, independent of TIA Portal.

Corporate Designer generates a corporate design file for TIA Portal V18 and V19, for V19 a file with file extension ".cd19". You can import the file into the WinCC Unified engineering system.

You can select the defined style objects in the engineering system to display the screen objects. The objects are then displayed in Runtime according to the style you created with the Corporate Designer.

For more information, refer to the document [SIMATIC WinCC Unified Corporate Designer](https://support.industry.siemens.com/cs/ww/en/view/109824234).

##### Importing custom styles

To import a custom style, follow these steps:

1. Create a directory "Styles" in the project folder under "</UserFiles/>".
2. Place the ".cd19" file in the folder "<Project_Directory>/UserFiles/Styles/".
3. Click "Runtime settings..." in the project tree.
4. Click ![Importing custom styles](images/165797699211_DV_resource.Stream@PNG-de-DE.png) under "General > Screen > Selected style".

   The "Styles" directory is searched for accessible corporate design files. All valid styles found are imported into the WinCC Unified device. If a new version of a corporate design that has already been imported exists, it is read in again.
5. Open the selection box "General > Screen > Selected style" with the arrow.

   ![Importing custom styles](images/172604456715_DV_resource.Stream@PNG-en-US.png)

   ![Importing custom styles](images/172604456715_DV_resource.Stream@PNG-en-US.png)
6. Select the custom style.

You have imported the custom style and set it as the style of the project.

> **Note**
>
> You can import several user-defined styles onto a device. All imported styles are transferred to the target system and you can switch between user-defined styles in Runtime.
>
> You can find more information on switching between styles in the section [Switching styles by means of user-defined functions](#switching-styles-by-means-of-user-defined-functions-rt-unified).

### Changing the screen resolution (RT Unified)

#### Introduction

The default screen size is adjusted to the resolution of the device. You can change the screen resolution in the Runtime settings of the device.

#### Configuring a fixed screen resolution

To change the screen resolution, follow these steps:

1. Open the runtime settings of the device.
2. Select the screen resolution under "General > Screen > Screen resolution".

![Configuring a fixed screen resolution](images/170934264971_DV_resource.Stream@PNG-en-US.png)

The screen resolution is adapted.

#### Adapting the screen size to the display

In the project, you can swap one device for another device with different display size. To adapt the configured screen size to the size of the new target device, follow these steps:

1. Select the screen in the project tree.
2. Right-click on the screen. The shortcut menu opens.
3. Select "Resize to display".

The configured screen size is adapted to the size of the new target device.

#### Scrolling in the screen

If not all objects are visible in the screen, a scroll bar appears on the right edge of the screen.

To view all objects, move the scroll bar up and down or from left to right with the mouse.

| Symbol | Meaning |
| --- | --- |
| ![Scrolling in the screen](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for working effectively** |
| - Place the mouse cursor in the screen. Move forward or backward with the mouse wheel to    scroll up and down in the screen. |  |

### Configuring zooming in runtime without Control key (RT Unified)

#### Introduction

You can configure the zooming in runtime in the runtime settings of the device. You have the following options:

- Zooming by holding down the Control key and scrolling with the mouse wheel.
- Zooming by scrolling with the mouse wheel without holding down the Control key.

#### Zooming without holding down the Control key

To zoom in runtime without holding down the Control key, follow these steps:

1. Under "Runtime settings > General > Screen", activate the "Zoom without pressing the Ctrl button" option.

   The option is deactivated by default.

   ![Zooming without holding down the Control key](images/171425684619_DV_resource.Stream@PNG-en-US.png)

   ![Zooming without holding down the Control key](images/171425684619_DV_resource.Stream@PNG-en-US.png)

### Configuring screen management (RT Unified)

This section contains information on the following topics:

- [Configuring screen management (RT Unified)](#configuring-screen-management-rt-unified-1)
- [Configuring zooming and scrolling for runtime (RT Unified)](#configuring-zooming-and-scrolling-for-runtime-rt-unified)

#### Configuring screen management (RT Unified)

##### Introduction

You can configure a main screen window in screen management. A screen is assigned to the main screen window. The main screen window allows you to focus on areas of the assigned screen in Runtime by zooming and scrolling.

##### Requirement

- A project has been created.
- A WinCC Unified PC or a Unified Comfort Panel is installed.

##### Configuring the main screen window in the screen editor

You can configure exactly one main screen window. To configure a main screen window, follow these steps:

1. Click "Screen management" in the project tree.
2. Double-click on "Main screen window".

   ![Configuring the main screen window in the screen editor](images/163903312395_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the main screen window in the screen editor](images/163903312395_DV_resource.Stream@PNG-en-US.png)

   The "Main screen window" editor opens.
3. The editor displays the properties that are important for zooming and scrolling. Define the following in the editor:

   - Name of the main screen window
   - Zoom - factor
   - Screen to be added to the main screen window.
   - Horizontal scroll bar - position
   - Vertical scroll bar - position

   ![Configuring the main screen window in the screen editor](images/163940275723_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the main screen window in the screen editor](images/163940275723_DV_resource.Stream@PNG-en-US.png)

You configure the other properties of the main screen window in the Inspector window under "Properties".

You can delete the configured main screen window and add a new main screen window.

##### Main screen window as start screen

The main screen window is used as the start screen in runtime instead of the screen you set as the start screen in the runtime settings. Synchronization between screens is not necessary.

##### Dynamizing the "Screen name" and "Screen number" properties

You can dynamize the "Screen name" and "Screen number" properties via a script.

#### Configuring zooming and scrolling for runtime (RT Unified)

##### Introduction

You can configure the zoom and scroll functions for the main screen window in Runtime and dynamize these properties using tags or scripts. In Runtime, you can control the behavior of the assigned screen using the dynamized properties.

##### Allow zooming in runtime

To configure the screen for zooming in runtime, follow these steps:

1. Click "Screen management > Main screen window" in the project tree.
2. Select a screen as the main screen window.
3. In the Inspector window of the main screen window, activate the "Zoom - allow" property under "Properties > Format".

   The option is activated by default.

![Allow zooming in runtime](images/165511584267_DV_resource.Stream@PNG-en-US.png)

If, for example, you want to move a displayed section in runtime, then you also configure the following properties of the main screen window:

- Zoom factor
- Horizontal scroll bar
- Vertical scroll bar

You can find more information in the section [Screen window](#screen-window-rt-unified).

##### Configuring zooming

To configure the zooming, follow these steps:

1. Select a zoom factor in the Inspector window under "Properties > Properties > Format > Zoom - factor".
2. Set the zoom factor to a number from 0.1 to 8.

   If you enter a number that is higher than that, the number is automatically lowered to 8.

##### Configuring scrolling

To configure the scrolling, follow these steps:

1. Select the position of the horizontal scroll bar in the Inspector window under "Properties > Format > Horizontal scroll bar - position".
2. Select the visibility of the horizontal scroll bar under "Properties > Format > Horizontal scroll bar - visibility".
3. Select the position of the vertical scroll bar under "Properties > Properties > Format > Vertical scroll bar - position".
4. Select the visibility of the vertical scroll bar under "Properties > Format > Vertical scroll bar - visibility".

## Overview of screen objects (RT Unified)

This section contains information on the following topics:

- [Show object type and name in the tooltip (RT Unified)](#show-object-type-and-name-in-the-tooltip-rt-unified)
- [Basic objects (RT Unified)](#basic-objects-rt-unified)
- [Elements (RT Unified)](#elements-rt-unified)
- [Controls (RT Unified)](#controls-rt-unified)
- [My Controls (RT Unified)](#my-controls-rt-unified)
- [Graphics (RT Unified)](#graphics-rt-unified)
- [Dynamic widgets (RT Unified)](#dynamic-widgets-rt-unified)

### Show object type and name in the tooltip (RT Unified)

#### Introduction

You can display the type and name of the object in the screen.

#### Displaying the object type and object name in the tooltip

To show the type and name of the object in the tooltip, follow these steps:

1. Move the cursor over the object in the screen.
2. Hover with the cursor over the object.

The type and name of the object are displayed in a tooltip.

![Displaying the object type and object name in the tooltip](images/159819982731_DV_resource.Stream@PNG-en-US.png)

### Basic objects (RT Unified)

This section contains information on the following topics:

- [Text box (RT Unified)](#text-box-rt-unified)
- [Graphic view (RT Unified)](#graphic-view-rt-unified)
- [Line (RT Unified)](#line-rt-unified)
- [Rectangle (RT Unified)](#rectangle-rt-unified)
- [Circle (RT Unified)](#circle-rt-unified)
- [Ellipse (RT Unified)](#ellipse-rt-unified)
- [Polyline (RT Unified)](#polyline-rt-unified)
- [Polygon (RT Unified)](#polygon-rt-unified)
- [Circular arc (RT Unified)](#circular-arc-rt-unified)
- [Elliptical arc (RT Unified)](#elliptical-arc-rt-unified)
- [Circle segment (RT Unified)](#circle-segment-rt-unified)
- [Ellipse segment (RT Unified)](#ellipse-segment-rt-unified)
- [Example: Configuring a rectangle (RT Unified)](#example-configuring-a-rectangle-rt-unified)

#### Text box (RT Unified)

##### Use

The "Text box" is a closed object which you can fill with a color. The text box is used to display text.

![Use](images/162159351819_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Text": Specifies the text for the text box.
- "Text trimming": Specifies whether ellipsis is to be displayed after a line break for a long text.
- "Text break": Specifies whether the next word is to be automatically moved to the next row for a long text.

##### Text

To define a text for the text box, follow these steps:

1. In the Inspector window, click "Properties > Properties > General > Font".
2. Select a font.
3. In the Inspector window, click "Properties > Properties > General > Text" .
4. Enter a text.

| Symbol | Meaning |
| --- | --- |
| ![Text](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working efficiently** |
| - Separate the words in the input window "Text" with <Shift+Return>. The words are displayed in individual rows in the text box. |  |

##### Direct text input

To change the text in the text box directly via the keyboard, follow these steps:

1. Select the text box.
2. Double-click in the text box and enter a text.

Note the following special information:

- Diacritics, such as ä ê ñ, can only be entered if the keyboard layout provides a key for this character. Key sequences, e.g. <`a> for à, are not recognized.
- It is not possible to enter Unicode characters using Alt codes.
- Asian language characters cannot be entered using an Input Method Editor (IME).

If you require such characters in the text, you have the following options:

- Use a keyboard layout on which this character is present as a key.
- Copy the character or the entire text from any source. Insert the text into the selected object.
- Edit the text in the Inspector window under "Properties > Properties > General > Text".

##### Editing text in runtime

The text that you have specified in the text box in the engineering system is read-only for Runtime by default.

To edit the text in runtime, follow these steps:

1. Click "Properties > Properties > Miscellaneous >Read-only" in the Inspector window.
2. Disable the option in the "Static value" column.

You can edit the text specified in the engineering system in runtime.

##### Trimming text

If there is a long text that is not fully displayed in the text field, specify ellipsis characters.

1. In the Inspector window, click "Properties > Properties > Format > Text trimming".
2. In the "Static value" column, select the option "With character ellipsis".

The text displayed is truncated with ellipsis.

##### Enabling line breaks

If there is a long text that is not fully displayed in the text field, activate line breaks. Determine if the text box is large enough for display with line breaks.

1. In the Inspector window, click "Properties > Properties > Format > Text break".
2. Select the option "Word wrap" in the "Static value" column.

The text is displayed in full with line breaks.

##### Dynamizing a text box with text list

To dynamize the text box with text list, follow these steps:

1. Create a text box.
2. Select a resource list in the "Dynamization" column in the Inspector window under "Properties > Properties > General > Text".
3. Select an existing tag under "Resource list > Settings > Tag". Alternatively, create a new tag using the "Add" button.
4. Select an existing text list under "Resource list > Settings > Resource list". Alternatively, add a new text list using the "Add" button.

> **Note**
>
> It is not possible to dynamize a text box using a resource list with a local session tag.

| Symbol | Meaning |
| --- | --- |
| ![Dynamizing a text box with text list](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working efficiently** |
| - You can create a text box by dragging-and-dropping a text list from the detail view of the text and graphics lists into the screen. The text box is linked to the text list. Configure the tags whose values determine the display in the text box. |  |

##### Dynamizing a text box

Drag-and-drop a tag from the detail view of the tag table directly into the text box. The text box is linked to the tag and the tag name appears in the text box.

---

**See also**

[Configuring object with a text list (RT Unified)](#configuring-object-with-a-text-list-rt-unified)
  
[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)
  
[Enter text directly into the object (RT Unified)](#enter-text-directly-into-the-object-rt-unified)

#### Graphic view (RT Unified)

##### Use

The "Graphic view" object is used to display graphics.

![Use](images/162157601675_DV_resource.Stream@PNG-de-DE.png)

Use the following graphic formats in the "Graphic view" object: *.bmp, *.ico, *.gif, *.tiff, *.png, *.svg, *.jpeg, *.jpg. You can also use the graphics as OLE objects in the graphic view.

Runtime does not support display of animated GIF files.

High-resolution graphic objects require a lot of memory in the project and cause long loading times. In addition, the performance in runtime decreases. Use graphic objects with a resolution that is sufficient for a high-quality display in the runtime project. Note the display resolution of the target device and the size in which the graphic object is displayed on the display of the target device. Adapt the resolution of large graphic objects accordingly before using them in your project.

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Graphic": Specifies the graphic file that is displayed in the object.
- "Background graphic - scale": Specifies how the graphic is scaled.

##### Inserting graphics

1. In the Inspector window, click "Properties > Properties > General > Graphic".
2. In the "Static value" column, click the arrow in the text box. Graphics from the graphics collection are displayed in the preview. You have the following options for inserting a graphic:

   - Select a graphic from the graphics collection.
   - Insert a graphic from a file using the ![Inserting graphics](images/100728040715_DV_resource.Stream@PNG-de-DE.png) button.
   - Create a new graphic from an OLE object using the ![Inserting graphics](images/100728049419_DV_resource.Stream@PNG-de-DE.png) button.
3. Click "Apply" to insert the graphic in the Graphic view.

| Symbol | Meaning |
| --- | --- |
| ![Inserting graphics](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working efficiently** |
| - Drag-and-drop a graphic from the detail view into the screen. A graphic view is created and linked to the graphic. |  |

##### Scaling a background graphic

The following modes for scaling graphics are available:

- None

  The graphic is inserted centered into the graphic view. If the graphic is larger than the graphic view, the graphic is displayed incompletely.
- Fill

  The graphic fills the graphic view. This mode can lead to a distortion of the graphic.
- Uniform

  The graphic is fully displayed and without distortion in the graphic view.
- Stretch to fit

  The graphic is adjusted to the size of the graphic view without distortion. As a result, the graphic may not be displayed completely.
- Tiled

  The graphic is displayed in original size, multi-tiled until the graphic view is filled.

To select a mode for scaling the graphic, proceed as follows:

1. Click "Format > Background graphic - scale" in the Inspector window.
2. Select the desired mode in the "Static value" column.

##### Dynamizing a graphic view with graphic list

To dynamize a graphic view with graphic list, follow these steps:

1. Create a graphic view.
2. Select a resource list in the "Dynamization" column in the Inspector window under "Properties > Properties > General > Graphic".
3. Select an existing tag under "Resource list > Settings > Tag". Alternatively, create a new tag using the "Add" button.
4. Select an existing graphic list under "Resource list > Settings > Resource list". Alternatively, add a new graphic list using the "Add" button.

| Symbol | Meaning |
| --- | --- |
| ![Dynamizing a graphic view with graphic list](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working efficiently** |
| - You create a graphic view by dragging and dropping a graphic list from the detailed view of the text and graphic lists into the screen. The graphic view is linked to the graphics list. Configure the tags whose values determine the display in the graphic view. |  |

---

**See also**

[Configuring objects with a graphic list (RT Unified)](#configuring-objects-with-a-graphic-list-rt-unified)

#### Line (RT Unified)

##### Use

The "Line" object is an open object.

![Use](images/162160156427_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Line - Type"
- "Line - Start" and "Line - End"

##### Dash type

The layout of the line is specified under "Properties > Properties > Appearance > Line - Type" in the Inspector window. The line is shown without interruption if you select "Solid", for example.

> **Note**
>
> The available line types depend on the selected HMI device.

##### Line start and line end

The start and end points of the line are specified under "Properties > Properties > Appearance > Line - start / Line - end" in the Inspector window.

Use arrow points, for example, as the start and end points of the line. The available start and end points depend on the device.

---

**See also**

[Changing the object size (RT Unified)](#changing-the-object-size-rt-unified)

#### Rectangle (RT Unified)

##### Application

The "Rectangle" is a closed object which you can fill with a color.

![Application](images/162160164107_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you can customize the settings for the position, geometry and color of the object. You can adapt the following properties in particular:

- "Corner > Radius": Specifies the horizontal and vertical distance between the corner of the rectangle and the start point of a rounded corner.

##### Specifying the corners

The corners of the "Rectangle" object can be rounded to suit your requirements. If the "Radius" property for all four corners is set to 0, a standard rectangle without rounded corners is displayed.

To define the layout of the corners, follow these steps:

1. In the Inspector window, click "Properties > Properties > Appearance > Corners".
2. Enter the radius for each corner.

#### Circle (RT Unified)

##### Application

The "Circle" object is a closed object that you can fill with a color or pattern.

![Application](images/162158136587_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Radius": Specifies the size of the circle.

##### Radius

The radius of the "Circle" object is specified in the Inspector window. The value is entered in pixels.

To specify the radius, follow these steps:

1. In the Inspector window, click "Properties > Size and position > Radius".
2. Enter a value of between 0 and 2500.

#### Ellipse (RT Unified)

##### Application

The "Ellipse" object is a closed object that you can fill with a color or pattern.

![Application](images/162158441099_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window you customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Radius X": Specifies the vertical radius of the elliptical object.
- "Radius Y": Specifies the horizontal radius of the elliptical object.

##### Radius X

The horizontal radius of the "Ellipse" object is specified in the Inspector window. The value is entered in pixels.

1. Click "Properties > Size and position" in the Inspector window.
2. For "Radius X", enter a value between 0 and 2500.

##### Radius Y

The vertical radius of the "Ellipse" object is specified in the Inspector window. The value is entered in pixels.

1. Click "Properties > Size and position" in the Inspector window.
2. Enter a value between 0 and 2500 for "Radius Y".

#### Polyline (RT Unified)

##### Use

The "Polyline" is an open object. Use the "Polygon" object if you want to fill the object with color.

![Use](images/162160482187_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Line start" and "Line end": Specifies the type of line start and line end.
- "Points": Modifies, deletes or adds corners.

##### Line start and line end

Define the start and end of the line in the "Properties" Inspector window. Use arrow point, for example, as start and end point. The available start and end points depend on the device.

##### Points

The corner points are numbered in the order of their creation. You can change, delete, or add more corner points:

1. In the Inspector window, click "Properties > Size and position > Points".
2. Select the required corner point. Enter a value for "X coordinate" and "Y coordinate".
3. Click on "Points" in the "Name" column to add or delete a corner point.

   A "Points" dialog opens.
4. Use the "Add" command to create a new point. You can delete corner points by selecting the corresponding row in the dialog and selecting "Delete" from the shortcut menu for the row.

##### Automatic creation of points

To create the points automatically, follow these steps:

1. Select a cell in the "X coordinate" or "Y coordinate" column.

   ![Automatic creation of points](images/172196121611_DV_resource.Stream@PNG-en-US.png)

   ![Automatic creation of points](images/172196121611_DV_resource.Stream@PNG-en-US.png)
2. Drag the blue border up or down. The value is applied to the target cells.

   ![Automatic creation of points](images/172196131723_DV_resource.Stream@PNG-en-US.png)

   ![Automatic creation of points](images/172196131723_DV_resource.Stream@PNG-en-US.png)

   If you select multiple cells and there is a logical relationship between the values, the values of the destination cells are adapted according to the logical relationship.

   ![Automatic creation of points](images/172197370635_DV_resource.Stream@PNG-en-US.png)

   ![Automatic creation of points](images/172197370635_DV_resource.Stream@PNG-en-US.png)

##### Configuring rotation in runtime

You configure the "Polyline" object so that it rotates about a reference point in runtime.

Enter the values for rotation in degrees:

1. In the Inspector window, click "Properties > Size and position".
2. Enter the required values for the following attributes:

   - Pivot point
   - Rotation
   - X pivot point
   - Y pivot point

---

**See also**

[Changing the object size (RT Unified)](#changing-the-object-size-rt-unified)
  
[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

#### Polygon (RT Unified)

##### Use

The "Polygon" is a closed object which you can fill with a background color.

![Use](images/162161043467_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Points": Modifies, deletes or adds corners.

##### Points

The corner points are numbered in the order of their creation. You can change, delete, or add more corner points:

1. In the Inspector window, click "Properties > Size and position > Points".
2. Select the required corner point. Enter a value for "X coordinate" and "Y coordinate".
3. Click on "Points" in the "Name" column to add or delete a corner point.

   A dialog opens.
4. Use the "Add" command to create a new point.

   You can delete corner points by selecting the corresponding row in the dialog and selecting "Delete" from the shortcut menu for the row.

##### Automatic creation of points

To automatically create the points for polygons and polylines, follow these steps:

1. Select a cell in the "X coordinate" or "Y coordinate" column.
2. Drag the blue border up or down. The value is applied to the target cells.

   If you select multiple cells and there is a logical relationship between the values, the values of the destination cells are adapted according to the logical relationship.

##### Configuring rotation in runtime

You configure the "Polygon" object so that the object rotates around a reference point in runtime.

Enter the values for rotation in degrees.

1. In the Inspection window, click "Properties > Size and position".
2. Enter values for the following attributes in the "Rotation" area.

   - Pivot point
   - Rotation
   - X pivot point
   - Y pivot point

---

**See also**

[Changing the object size (RT Unified)](#changing-the-object-size-rt-unified)
  
[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)
  
[Polyline (RT Unified)](#polyline-rt-unified)

#### Circular arc (RT Unified)

##### Use

The "Circular arc" is an open object. Use the "Circle segment" object if you want to fill the object with color.

A circular arc is a quarter circle by default. It can be customized as required.

![Use](images/162161425035_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Radius": Define the size of the circular arc.
- "Angle - start" and "Angle - range": Specify where the start and end angle lie on a virtual circle of 360°.

##### Defining the radius

You define the radius of the "Circular arc" object in the Inspector window. Enter the value in pixels.

1. Click "Properties > Size and position" in the Inspector window.
2. Enter a value for "Radius".

##### Defining the start angle and angle range

You set the length of the circular arc using the "Angle - start" and "Angle - range" attributes. Enter the values using Degrees as the unit.

1. Click "Properties > Size and position" in the Inspector window.
2. Enter one value each for "Angle - start" and "Angle - range".

#### Elliptical arc (RT Unified)

##### Use

The "Elliptical arc" is an open object. Use the "Ellipse segment" object if you want to fill the object with color.

An elliptical arc is a quarter ellipse by default. It can be customized as required.

![Use](images/162161729547_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Radius": Specifies the size of the elliptical arc.
- "Radius X" and "Radius Y": Specifies the horizontal and vertical radius of the elliptical object.
- "Angle - start" and "Angle - range": Specify where the start and end point lie on a virtual circle of 360°.

##### Defining the radius

Define the horizontal and vertical radius of the "Elliptical arc" object in the Inspector window. Enter the values using Pixels as the unit.

1. Click "Properties > Size and position" in the Inspector window.
2. Enter one value each for "Radius X" and "Radius Y".

##### Defining the start angle and angle range

Set the length of the elliptical arc using the "Angle - start" and "Angle - range" attributes. Enter the values using Degrees as the unit.

1. Click "Properties" in the Inspector window.
2. Enter one value each for "Angle - start" and "Angle - range".

#### Circle segment (RT Unified)

##### Use

The "Circle segment" is a closed object that you can fill with a color or pattern.

A circle segment is a quarter circle by default. It can be customized as required.

![Use](images/162162328459_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Radius": Define the size of the circle segment.
- "Angle - start" and "Angle - range": Specify where the start and end angle lie on a virtual circle of 360°.

##### Radius

You define the radius of the "Circle segment" object in the Inspector window. Enter the value using Pixels as the unit.

1. Click "Properties > Size and position" in the Inspector window.
2. Enter a value for "Radius".

##### Defining the start angle and angle range

Set the size of the circle segment using the "Angle - start" and "Angle - range" attributes. Enter the values using Degrees as the unit.

1. Click "Properties > Size and position" in the Inspector window.
2. Enter one value each for "Angle - start" and "Angle - range".

#### Ellipse segment (RT Unified)

##### Use

The "Ellipse segment" is a closed object that you can fill with a color or pattern.

An ellipse segment is a quarter ellipse by default. It can be customized as required.

![Use](images/162162607371_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Radius X" and "Radius Y": Specifies the horizontal and vertical radius of the elliptical object.
- "Angle - start" and "Angle - range": Specify where the start and end point lie on a virtual circle of 360°.

##### Defining the radius

Define the horizontal and vertical radius of the "Ellipse segment" object in the Inspector window. Enter the values using Pixels as the unit:

1. Click "Properties > Size and position" in the Inspector window.
2. Enter one value each for "Radius X" and "Radius Y".

##### Defining the start angle and angle range

Set the size of the ellipse segment using the "Angle - start" and "Angle - range" attributes. Enter the values using Degrees as the unit.

1. Click "Properties > Size and position" in the Inspector window.
2. Enter one value each for "Angle - start" and "Angle - range".

#### Example: Configuring a rectangle (RT Unified)

##### Task

In this example, you learn how to configure the rectangle.

You configure:

- Color = red
- Black border 2 pixels wide
- Position = (20, 20)
- Size = (100,100)

##### Changing the color of the rectangle

Follow these steps to change the color of the rectangle:

1. Select the rectangle.
2. Define the background color under "Properties > Appearance > Background - color" in the Inspector window.
3. Select the "Solid" option under "Background - fill pattern".
4. Define the border color under "Properties > Appearance > Border - color".
5. Enter the value "2" for "Border width".

The rectangle is red and has a black border with a width of two pixels.

##### Repositioning and resizing the rectangle

Follow these steps to change the position and size of the rectangle:

1. Select the rectangle.
2. Enter the value "20" in each case under "Properties > Size and position > Position - left / Position - top".
3. Enter the value "100" in each case under "Properties > Size and position > Size - width / Size - height".

##### Result

The rectangle is positioned at the coordinates (20, 20), and has a width and height of 100 pixels.

### Elements (RT Unified)

This section contains information on the following topics:

- [IO field (RT Unified)](#io-field-rt-unified)
- [Symbolic IO field (RT Unified)](#symbolic-io-field-rt-unified)
- [List box (RT Unified)](#list-box-rt-unified)
- [Button (RT Unified)](#button-rt-unified)
- [Switch (RT Unified)](#switch-rt-unified)
- [Bar (RT Unified)](#bar-rt-unified)
- [Slider (RT Unified)](#slider-rt-unified)
- [Gauge (RT Unified)](#gauge-rt-unified)
- [Clock (RT Unified)](#clock-rt-unified)
- [Check box (RT Unified)](#check-box-rt-unified)
- [Radio button (RT Unified)](#radio-button-rt-unified)
- [Touch area (RT Unified)](#touch-area-rt-unified)
- [Examples (RT Unified)](#examples-rt-unified)

#### IO field (RT Unified)

##### Use

The "IO field" object is used to enter and display process values.

![Use](images/162571350411_DV_resource.Stream@PNG-de-DE.png)

The IO field is displayed empty by default. When you configure a value, the value is displayed in the IO field based on the selected output format.

| Symbol | Meaning |
| --- | --- |
| ![Use](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| - You can create an IO field by moving a configured tag from the detail view onto the screen using drag-and-drop. An IO field is created and linked to the tag. - If you select multiple tags and move them from the detail view onto the screen using drag-and-drop, an IO field is created for each tag which is linked to the respective tag. |  |

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Mode": Specifies whether the values are entered and displayed in Runtime or if the values are only displayed.
- "Reaction to input": Specifies the behavior of the object in runtime.
- "Hidden input": Specifies whether the input value is displayed normally or encrypted during input.

##### Mode

You can define the behavior of the IO field in the Inspector window under "Properties > General > Mode".

| Mode | Description |
| --- | --- |
| "Input/output" | Values are entered and output in the IO field in runtime. |
| "Output" | The IO field is used for the output of values only. |

In reports, IO fields only output data. "Output" mode is preset. Properties for configuring input are not available, for example "Hidden input".

If you have configured "Output" mode for an IO field, no input is possible. The "Input finished" event cannot be triggered for this. If you configure a function or script for the "Input finished" event nevertheless, an error message is displayed.

##### Reaction to input

To define the behavior of the object in runtime, you select one or more of the following options under "Properties > General > Miscellaneous > Reaction to input":

- "Clear last value on focus". The last value is cleared when the IO field is selected.
- "Input on activate". The IO field changes automatically to input mode and allows an input to be made when the IO field is selected.
- "Accept value after exit". The entered value is applied to the process value on exiting the IO field.
- "Hidden input". If "Hidden input" is active, the IO field displays the substitute character "*" in place of the entered character. You can use the hidden input for the entry of a password, for example. The data format of the value entered cannot be recognized.

![Reaction to input](images/170045466379_DV_resource.Stream@PNG-en-US.png)

##### Connection to Char data type

If you connect the IO field to a controller tag of data type "Char", the following restrictions apply:

- The input accepts digits only: 0 … 9.

  The entered string of digits is converted to the corresponding character according to the ASCII table.

  Example: Input 6 + 5 becomes "A".
- Only enter digit sequences between 0 and 129.

To enter alphanumeric characters directly, use the "WChar" data type as an alternative, for example.

##### Value range for the LTIME data type

LTime values are saved as 64-bit Int with sign. For HMI tags with LTime data type:

| Symbol | Meaning |
| --- | --- |
| Value range | -9223372036854775808 to 9223372036854775807 |
| Unit | 100 ns |

S7-1500 tags with data type LTime have the unit nanoseconds (ns). HMI user inputs in IO fields that are linked with such tags are converted to ns when the value is sent to the controller.

> **Note**
>
> Depending on the JavaScript engine of the web client, the actual value may lose accuracy during communication between the HMI device and the controller due to rounding if it is outside the value range of MAX_SAFE_INTEGER.
>
> Additional information on MAX_SAFE_INTEGER can be found [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER).

##### Settings for tags

If required, activate the "Use indirect addressing" or "Read only" options in the "Tag settings" area.

- "Use indirect addressing"

  The configured tag of the "WString" data type must contain the name of another tag as text.
- "Read only"

  The change to the property value is not applied in the tag.

The "Read only" option is enabled by default.

![Settings for tags](images/169385421963_DV_resource.Stream@PNG-en-US.png)

##### No events during input

While an IO field is in input mode, no events are transmitted to the server for the IO field. This means that no events are triggered and no user code is executed.

Exit input mode with <Enter> or <Esc> so that the events configured for the I/O field in engineering take effect again.

---

**See also**

[Indirect addressing (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#indirect-addressing-rt-unified)
  
[Triggering the "Input finished" event (RT Unified)](#triggering-the-input-finished-event-rt-unified)

#### Symbolic IO field (RT Unified)

##### Use

You can use the "Symbolic IO field" object to configure a selection list for input and output of texts or graphics in runtime.

![Use](images/162573536267_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> Selecting the default entry is not possible in runtime.

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Mode": Specifies the behavior of the object in runtime.
- "Resource list": Specifies the text or graphic list that will be linked with the object.

##### Mode

The response of the symbolic IO field is specified in the Inspector window in "Properties > Properties > Miscellaneous > Mode".

| Mode | Description |
| --- | --- |
| "Output" | The symbolic IO field is used for the output of values. |
| "Input/output" | The symbolic IO field is used for the input and output of values. |

##### Linking symbolic IO field with text list

To link a text list with the symbolic IO field, follow these steps:

1. In the Inspector window, select "Properties > Properties > General > Resource list".
2. Open the selection list for "Text list" in the "Static value" column.
3. Select a text list.
4. Open the "Text and graphic lists" editor in the project tree.
5. Select the "Text lists" tab. Click on the selected text list.
6. Select an entry in the "Text list entries" table as the default entry. The text from the default entry is displayed in the object.  
   If you have not specified a default entry, the first entry in the "Text" column is displayed in the object.

| Symbol | Meaning |
| --- | --- |
| ![Linking symbolic IO field with text list](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| - Drag a text list from the detail view of the text and graphic lists to the symbolic IO field. The symbolic IO field is linked to the text list. |  |

##### Linking symbolic IO field with graphic list

To link a graphic list with the symbolic IO field, follow these steps:

1. In the Inspector window, select "Properties > Properties > General > Resource list".
2. Open the selection list for "Graphic list" in "Resource list".
3. Select a graphic list.
4. Open the "Text and graphic lists" editor in the project tree.
5. Select the "Graphic lists" tab. Click on the selected graphic list.
6. Select an entry in the "Graphic list entries" table as the default entry. The graphic from the standard entry is displayed in the object.  
   If you have not specified a default entry, the first entry in the "Graphic" column is displayed in the object.

| Symbol | Meaning |
| --- | --- |
| ![Linking symbolic IO field with graphic list](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| - Use drag-and-drop to move a graphic list from the detail view of the text and graphic lists to the symbolic IO field. The symbolic IO field is linked to the graphic list. |  |

##### Dynamizing a symbolic IO field

To dynamize the symbolic IO field using a tag, follow these steps:

1. In the Inspector window, select "Properties > Properties > General > Process value".
2. Select "Tag" in the "Dynamization" column. The "Tag" page will open.
3. Select:

   - Select an existing tag under "Tag > Process > Tag", or
   - Create a new tag using the "Add" button.

| Symbol | Meaning |
| --- | --- |
| ![Dynamizing a symbolic IO field](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| - Use drag-and-drop to move a tag from the detail view of the tag table to the symbolic IO field. The symbolic IO field is linked to the tag. |  |

#### List box (RT Unified)

##### Use

You use the "List box" object to present and select multiple list entries. You activate list entries by default so that the operator only changes the preset entry if necessary. If the list box is larger than the bounding box, WinCC automatically adds a scroll bar to the right margin.

To incorporate list boxes into the process, dynamize the corresponding properties.

![Use](images/162356416267_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Selection items": Defines the list entries.
- "Select item": Defines which entry is displayed as activated by default.

##### Defining the number of entries

You specify the number of entries in the Inspector window:

1. In the Inspector window, select "Properties > General > Selection items".
2. Click on the selection button in the "Static value" column.

   A dialog opens.
3. Specify the desired number of entries with "Add".

   To delete entries, click in the corresponding line and press the <DEL> key or click ![Defining the number of entries](images/133294505739_DV_resource.Stream@PNG-de-DE.png).
4. To change the order of the entries, click in the corresponding line and move the entry using the icons ![Defining the number of entries](images/133295026059_DV_resource.Stream@PNG-de-DE.png).

##### Specifying the default value of the list entry

Use the "Select item" property of a selection item to specify which list item is to be shown as enabled.

You can activate multiple options.

To do so, select the check box in the "Static value" column of the "Select item" property of the respective selection item.

##### Dynamizing a list box

Drag-and-drop a tag from the detail view of the tag table into the list box. The list box is linked to the tag.

> **Note**
>
> It is not possible to dynamize a list box using a resource list with a local session tag.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following property containing a graphic with a tag or with a script:

- Graphic

---

**See also**

[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)
  
[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)

#### Button (RT Unified)

##### Use

The "Button" object allows you to configure an object that the operator can use in runtime to execute a configurable function.

![Use](images/162571963531_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Appearance - style item": Specifies whether the button is displayed as a rectangle or a circle.
- "Type": Define the graphic display of the object.
- "Background graphic - scale": Specify how the graphic is scaled.

##### Displaying the button as a rectangle or circle

In order to display the button as a rectangle or circle, follow these steps:

1. Click "Properties > Appearance > Appearance - style item" in the Inspector window.
2. To display the button as a rectangle, select the option "HmiButton" in the "Static value" column.

   To display the button as a circle, select the option "HmiRoundButton" in the "Static value" column.

   ![Displaying the button as a rectangle or circle](images/172307809931_DV_resource.Stream@PNG-en-US.png)

   ![Displaying the button as a rectangle or circle](images/172307809931_DV_resource.Stream@PNG-en-US.png)

##### Defining the content

You can specify how the button is displayed under "Properties > General > Content > Type" in the Inspector window.

| Type | Description |
| --- | --- |
| "Text" | The button is displayed with text. This text explains the function of the button. |
| "Graphic" | The button is displayed with a graphic. This graphics represents the function of the button. |
| "Graphics or text" | The button is displayed with text or graphics.  If the graphics cannot be displayed, the corresponding text is displayed. |
| "Graphics and text" | The button is displayed with text and graphics. |

Different options are available depending on the device.

##### Scaling a background graphic

The following modes for scaling graphics in buttons are available:

- None

  The graphic is inserted centered inserted into the button. If the graphic is larger than the button, the graphic will be displayed incompletely.
- Fill

  The graphic fills the button. This mode can lead to a distortion of the graphic.
- Uniform

  The graphic is fully displayed and without distortion in the button.
- Stretch to fit

  The graphic is adjusted to the size of the button without distortion. As a result, the graphic may not be displayed completely.

To select a mode for scaling the graphic, proceed as follows:

1. In the Inspector window, select "Properties > General > Content > Background graphic - scale".
2. Select the desired mode in the "Static value" column.

| Symbol | Meaning |
| --- | --- |
| ![Scaling a background graphic](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working efficiently** |
| - You add a graphic to the button by dragging-and-dropping the graphic from the detail view of the project graphics to the button. |  |

##### Text / Graphic

Depending on the "Content" property, define whether the display is static or dynamic. The display is defined under "Properties > General > Text" or "Graphic" in the Inspector window.

Your options for the type "Text" or "Graphic" include the following.

| Type | Description |
| --- | --- |
| "Text" | Use "Text with pressed button" to specify the text displayed in the button for the "ON" state. |
| "Graphic" | Use "Graphic with pressed button" to specify a graphic displayed in the button in the "ON" state. |

##### Direct text input

To change the labeling in the button directly via the keyboard, follow these steps:

1. Selecting the button.
2. Double-click in the button and enter a text.

Note the following special information:

- Diacritics, such as ä ê ñ, can only be entered if the keyboard layout provides a key for this character. Key sequences such as <`a> for à, are not recognized.
- It is not possible to enter Unicode characters using Alt codes.
- Asian language characters cannot be entered using an Input Method Editor (IME).

If you need such characters in the label, you have the following options:

- Use a keyboard layout on which this character is present as a key.
- Copy the character or full label from any source. Insert the character into the selected object.
- Edit the label in the Inspector window under "Properties > Properties > General > Text".

##### Configuring a screen change

1. Drag a button from the "Toolbox" task card to a screen.
2. Configure the "ChangeScreen" system function to an event of the button.
3. Add another screen in the "Value" column.

| Symbol | Meaning |
| --- | --- |
| ![Configuring a screen change](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working efficiently** |
| - You can configure a screen change by dragging-and-dropping a configured screen from the project tree into the open screen. A button is automatically created and linked to the screen. |  |

##### Dynamizing a button with text list

Drag-and-drop a text list from the detail view of the text and graphic lists to the button. The button is linked to the text list.

> **Note**
>
> It is not possible to dynamize a button using a resource list with a local session tag.

##### Dynamizing a button with graphic list

Drag-and-drop a graphic list from the detail view of the text and graphic lists directly to the button. The button is linked to the graphic list.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Graphic - pressed button

---

**See also**

[Enter text directly into the object (RT Unified)](#enter-text-directly-into-the-object-rt-unified)
  
[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)

#### Switch (RT Unified)

##### Use

The "Switch" object is used to configure a switch that is used to switch between two predefined states in runtime. The current state of the "Switch" object can be visualized with either a label or a graphic.

![Use](images/162573674763_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Type": Specifies the graphic representation of the object.

##### Type of representation

You can specify how the switch is displayed under "Properties > General > Content > Type" in the Inspector window.

| Type | Description |
| --- | --- |
| "Graphic" | The current state of the switch is shown with a graphic. In runtime click on the button to actuate the switch. |
| "Text" | The current state of the switch is shown with a label. In runtime click on the button to actuate the switch. |
| "Graphics or text" | The switch displays graphics or a text. If the graphics are not available, the text is displayed. |
| "Graphics and text" | The switch displays graphics and a text. |

##### Dynamizing a switch with text list

Drag-and-drop a text list from the detail view of the text and graphics lists directly to the switch. The switch is linked to the text list.

##### Dynamizing a switch with graphics list

Drag-and-drop a graphics list from the detail view of the text and graphics lists to the switch. The switch is linked to the graphics list.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Graphic - pressed button

---

**See also**

[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)

#### Bar (RT Unified)

##### Use

Use the "Bar" object to display the tags graphically. The bar graph can be labeled with a scale of values.

![Use](images/162572063627_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Trend indicator - show": Shows whether the current value is higher or lower than the previous value.
- "Process value indicator - mode": Specifies how the process value is displayed in the bar chart.
- "Scale": Specifies the properties for the bar scale.

When the object in the light or dark style does not meet the following dimensions in Runtime, it is automatically displayed in compact mode:

- Vertical alignment: 100 pixels high or 30 pixels wide
- Horizontal alignment: 30 pixels high or 100 pixels wide

##### Displaying the process value indicator

You can use the "Process value indicator - mode" property to select the process value of the selected tag in the bar in runtime:

1. In the Inspector window, click "Properties > Miscellaneous > Process value indicator - mode".
2. Select another "Indicator" mode in the "Static value" column.
3. Go to "Process value indicator - foreground color" and select the display color for the process value.

##### Defining bar segments

You can define the settings for the bar scale under "Properties > General > Scale":

- "Scaling type": Specifies how the bar scale is calculated, for example "Linear".
- "Alignment": Specifies whether the bar is displayed horizontally or vertically.
- "Scale mode": Specifies whether the scale is subdivided with tick marks, numbers, or not at all.
- "Scale value - maximum" and "Scale value - minimum": Sets the start value and the end value to be displayed in the scale.

##### Defining scale gradation

Use the "Division count" property to define the subdivision count for the bar scale divisions.

The "Subdivision count" property defines the number of ticks between the division marks.

1. In the Inspector window, click "Properties > General > Scale".
2. Enter the required values for the "Division count" and "Subdivision count".

**Note**

The division count can only be changed if "Automatic scaling" is disabled.

##### Dynamizing bars

Drag a tag from the detail view of the tag table into the bar. The bar is linked to the tag.

---

**See also**

[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)

#### Slider (RT Unified)

##### Use

You can use the "Slider" object to monitor process values within a defined range and adjust the values. The monitored range is visualized in the form of a slider. By adjusting the slider, you intervene in the process and correct the displayed process value.

![Use](images/162572317323_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Scale value - maximum" and "Scale value - minimum": Specifies the top and bottom values of the scale.
- "Process value indicator - mode": Specifies how the current process value is displayed in the slider.
- "Trend indicator - show": Specifies how the current value has changed compared to the previous values.

When the object in the light or dark style does not meet the following dimensions in Runtime, it is automatically displayed in compact mode:

- Vertical alignment: 100 pixels high or 30 pixels wide
- Horizontal alignment: 30 pixels high or 100 pixels wide

##### Maximum and minimum scale value

The top and bottom end values of the scale are specified in the Inspector window.

1. In the Inspector window, click "Properties > Properties > General > Scale".
2. Enter a number each at "Scale value - maximum" and "Scale value - minimum". If you select a tag as the end value of the scale, the number will no longer be available.

##### Show value

Specify that the value of the current position is displayed below the slider in the Inspector window.

1. Click "Properties > Miscellaneous" in the Inspector window.
2. Select "Value - show".

##### Process value indicator - mode

Specify a mode for the process value display:

1. In the Inspector window, click "Properties > Miscellaneous > Process value indicator - mode".
2. Select a mode in the "Static value" column.

| Mode | Description |
| --- | --- |
| Bar | Displays the bar with the process value indicator. |
| Indicator | Shows the process value indicator as a position on the bar. |
| Detailed indicator | Shows the process indicator in the bar. |
| Bar with detailed indicator | Shows the current process value and its position in the slider bar. |

> **Note**
>
> If you have configured a tag for the "Process value indicator mode" property of a slider, changing the tag in runtime has no effect on the slider.

##### Dynamizing a slider

Drag a tag from the detail view of the tag table into the slider. The slider is linked to the tag.

---

**See also**

[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)

#### Gauge (RT Unified)

##### Use

The "Gauge" object shows numeric values in the form of an analog gauge. For example, a glance in runtime is enough to note that the boiler pressure is in the normal range. The gauge is purely for display and you cannot operate it.

![Use](images/162572647435_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Peak indicator": Specifies whether the measurement range is indicated with a peak indicator.
- "Trend indicator - show": Shows whether the current value is higher or lower than the previous value.
- "Scale value - maximum" and "Scale value - minimum": Specifies the top and bottom values of the scale.
- "Normal range - color": Specifies the color in which the normal range is displayed.
- "Scale": Specifies various settings for the scale view.

When the object in the light or dark style is less than 180 pixels tall or wide in Runtime, it is automatically displayed in compact mode.

##### Displaying peak value

The "Peak indicator" property can be used to enable a marker function for the maximum or minimum pointer movement in runtime.

1. Click "Properties > Miscellaneous > Peak indicator" in the Inspector window.
2. Select the option "High" or "Low" in the "Static value" column.

##### Scale value - maximum and Scale value - minimum

You can set the top and bottom end values of the scale in the Inspector window.

1. In the Inspector window, click "Properties > General > Scale".
2. Select a value under "Properties > General > Scala> Output format".
3. Enter a number each at "Scale value - maximum" and "Scale value - minimum".

   If you select a tag as the end value of the scale, the number will no longer be available.

> **Note**
>
> If you specify the value {H} (Hexadecimal) for the output format, negative values are not displayed correctly in the gauge. If you want to output negative values via a gauge, use {F}, {N} or {I} as output format.

##### Configuring a scale

1. In the Inspector window, click "Properties > General > Scale".
2. Under "Angle - start", specify the angle at which the scale is to start. The angle is specified in degrees, starting at the zero position.

   The scale runs clockwise. A start value of 0 corresponds to a display of 3 o'clock.
3. Under "Angle - range", specify the range in degrees to be covered by the scale.
4. Under "Scale mode", specify whether the divisions are displayed as ticks or numbers.

##### Dynamizing a gauge

Drag a tag from the detail view of the tag table into the gauge. The gauge is linked to the tag.

#### Clock (RT Unified)

##### Use

The "Clock" object displays the time.

![Use](images/162572824203_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Appearance - style item": Specifies the analog or digital display.
- "Clock face - mode": Specifies whether the hour marks of the analog clock are displayed as ticks or numbers.
- "Hand - show hours", "Hand - show minutes" and "Hand - show seconds": Specifies whether the hour hand, minute hand and second hand are displayed on the clock.

With the default setting, the "Clock" object displays the time of the client.

##### Display the clock in analog or digital form

To display the clock in analog or digital form, follow these steps:

1. Click "Properties > Appearance > Appearance - style item" in the Inspector window.
2. To display the clock in analog form, select the option "HmiClock" in the "Static value" column.

   To display the clock in digital form, select the option "HmiDigitalClock" in the "Static value" column.

   ![Display the clock in analog or digital form](images/172305529355_DV_resource.Stream@PNG-en-US.png)

   ![Display the clock in analog or digital form](images/172305529355_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The clock is automatically displayed digitally if you select
>
>
>
> 1. the bright or dark style under "Runtime settings".
> 2. Set the "Size - width" or "Size - height" less than 100 pixels under "Properties > Size and position".

##### Configuring the clock face

In the Inspector window, you can specify how the hour marks are displayed.

1. In the Inspector window, click "Properties > General > Clock face - mode".
2. Select "Ticks" to display hours as ticks.

   To show the hours numerically in the display, select "Numbers".

##### Dynamizing the clock

Drag-and-drop one tag from the detail view of tag table into the clock. The clock is linked to the tag.

If the "Process value" property of the clock is connected to a DateTime tag, the clock uses the tag value as a start value and continues counting. When the tag value is changed, the clock is synchronized and continues counting from the new value.

> **Note**
>
> If the screen is supposed to display a static time of day, link a tag of the type DateTime with an IO field.

---

**See also**

[Defining the style](#defining-the-style)

#### Check box (RT Unified)

##### Use

You use the "Check box" object to display and select multiple entries. You activate a selection item by default so that the operator only changes the preset value if necessary. The operator can select multiple options in runtime. You can specify a text or a graphic for each option.

To include a check box in the process, dynamize the corresponding properties.

![Use](images/162572990219_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Selection items": Defines the number of options.
- "Select item": Defines which entries are displayed as activated by default.

> **Note**
>
> The item height option of the radio button is set to "0" during the creation of a new object. This value does not represent the actual value 0, but a default setting.

##### Defining the number of entries

You specify the number of entries in the Inspector window:

1. In the Inspector window, select "Properties > General > Selection items".
2. Click on the selection button in the "Static value" column.

   A dialog opens.
3. Specify the desired number of entries with "Add".

   To delete entries, click in the corresponding line and press the <DEL> key or click ![Defining the number of entries](images/133294505739_DV_resource.Stream@PNG-de-DE.png).
4. To change the order of the entries, click in the corresponding line and move the entry using the icons ![Defining the number of entries](images/133295026059_DV_resource.Stream@PNG-de-DE.png).

##### Using graphics and texts in the selection items

You can mark the selection items with texts or graphics. The following modes are available:

- "Graphic and text": The selection item shows text and graphic.
- "Graphic or text" The selection item is visualized either by a graphic or a text. If the graphic is not available, the text is displayed.
- "Graphic": The selection item is visualized with a graphic.
- "Text": The selection item is visualized with an inscription.

To configure the CheckBox contents, follow these steps:

1. Under "Properties > Format > Content > Type" select the type for display of the selection items, e.g. "Graphic and text".
2. Under "General > Selection items > [x] Selection item > Text", enter the text to be displayed in the check box as a selection item.
3. Under "Selection items > [x] Selection item > Graphic", open the selection list.
4. Select the appropriate graphic.

##### Specifying the default of the check box

Use the "Select item" property of a selection item to define whether it is to be shown as enabled in a check box list.

You can activate multiple options.

To do so, select the check box in the "Static value" column of the "Select item" property of the respective selection item.

##### Dynamizing a check box

Drag-and-drop a tag from the detail view of the tag table directly to the check box. The check box is linked to the tag.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following property containing a graphic with a tag or with a script:

- Graphic

---

**See also**

[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)
  
[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)

#### Radio button (RT Unified)

##### Use

You can use the "Radio button" object to display and select various options. Only one of these options can be selected by the operator. Enable one of the options by default so that the operator only changes the default value if necessary. To include a radio button in the process, dynamize the corresponding attributes.

![Use](images/162573258763_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Selection items": Defines the number of options.
- "Select item": Defines which entry is displayed as activated by default.

> **Note**
>
> The item height option of the radio button is set to "0" during the creation of a new object. This value does not represent the actual value 0, but a default setting.

##### Defining the number of entries

You specify the number of entries in the Inspector window:

1. In the Inspector window, select "Properties > General > Selection items".
2. Click on the selection button in the "Static value" column.

   A dialog opens.
3. Specify the desired number of entries with "Add".

   To delete entries, click in the corresponding line and press the <DEL> key or click ![Defining the number of entries](images/133294505739_DV_resource.Stream@PNG-de-DE.png).
4. To change the order of the entries, click in the corresponding line and move the entry using the icons ![Defining the number of entries](images/133295026059_DV_resource.Stream@PNG-de-DE.png).

##### Using graphics and texts in the selection items

You can mark the selection items with texts or graphics. The following modes are available:

- "Graphic and text": The selection item shows text and graphic.
- "Graphic or text" The selection item is visualized either by a graphic or a text. If the graphic is not available, the text is displayed.
- "Graphic": The selection item is visualized with a graphic.
- "Text": The selection item is visualized with an inscription.

To configure the contents in the radio button, follow these steps:

1. Under "Properties > Content > Type", select the type for display of the selection items, e.g. "Graphic and text".
2. Under "Selection items > [x] Selection item > Text" enter the text that is to be shown in the check box as the selection item.
3. Under "Selection items > [x] Selection item > Graphic", open the selection list.
4. Select the appropriate graphic.

##### Specifying the default value of the radio button

Use the "Select item" property of a selection item to specify which radio button item is to be shown as enabled.

You can only enable one item.

Under "Properties > Selection items", activate the "Select item" property of the item to be activated by default.

##### Dynamizing a radio button

Drag-and-drop a tag from the detail view of the tag table into the radio button. The radio button is linked to the tag.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following property containing a graphic with a tag or with a script:

- Graphic

---

**See also**

[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)
  
[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)

#### Touch area (RT Unified)

##### Use

The "Touch area" object allows you to configure an object that the operator can use in runtime to execute a configurable function. A gesture on the user interface starts the execution of the function. The gesture is recognized in the area where it begins.

The "Touch area" object is shown as a dotted area in the engineering system.

![Use](images/162573421323_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object.

##### Defining gestures

The "Touch Area" object distinguishes between the following gestures:

- Right
- Left
- Up
- Down

To distinguish between the gestures, program a J-Script that evaluates the gesture.

1. Click ![Defining gestures](images/130773202443_DV_resource.Stream@PNG-de-DE.png) in the Inspector window under "Properties > Events > Gesture detected".
2. Copy the code example into the programming window.

Code example

export function Touch_area_1_OnGestureDetected(item, gesture) {

// value of tag ‚MyTag1‘ will be set depending on the detected gesture

if(gesture == UI.Enums.HmiGesture.SwipeRight)

{

UI.RootWindow.Screen = 'ScreenRight';

let tag1 = Tags('tag1');

tag1.Write(1); //write value '1234' to tag 'MyTag1'

}

if(gesture == UI.Enums.HmiGesture.SwipeLeft)

{

UI.RootWindow.Screen = 'ScreenLeft';

let tag1 = Tags('tag1');

tag1.Write(2); //write value '1234' to tag 'MyTag1'

}

if(gesture == UI.Enums.HmiGesture.SwipeUp)

{

UI.RootWindow.Screen = 'ScreenUp';

let tag1 = Tags('tag1');

tag1.Write(3); //write value '1234' to tag 'MyTag1'

}

if(gesture == UI.Enums.HmiGesture.SwipeDown)

{

UI.RootWindow.Screen = 'ScreenDown';

let tag1 = Tags('tag1');

tag1.Write(4); //write value '1234' to tag 'MyTag1'

}

if(gesture == UI.Enums.HmiGesture.Unknown)

{

let tag1 = Tags('tag1');

tag1.Write(0); //write value '1234' to tag 'MyTag1'

}

}

#### Examples (RT Unified)

This section contains information on the following topics:

- [Example: Configuring an IO field (RT Unified)](#example-configuring-an-io-field-rt-unified)
- [Example: Set values (RT Unified)](#example-set-values-rt-unified)

##### Example: Configuring an IO field (RT Unified)

###### Task

In this example, you learn how to configure an IO field and connect it to a tag.

You configure:

- Color = blue
- Border color = gray
- Mode = Input/output
- HMI tag = MyTag

###### Requirement

- A project is open.
- A screen is configured.

###### Configuring an IO field

To configure an IO field, follow these steps:

1. Open the "Elements" palette in the "Toolbox" task card.
2. Drag the "IO field" object onto the screen.
3. In the Inspector window, navigate to "Properties > Appearance > Background - color".
4. In the "Static value" column, select the blue color.
5. Navigate to "Properties > Appearance > Border - color".
6. In the "Static value" column, select the gray color.
7. Select the "Input/output" mode under "Properties > General > Mode".

###### Connecting the IO field to a tag

To connect the IO field to a tag, follow these steps:

1. In the Inspector window, click "Properties > General > Process value" in the "Dynamization" column.
2. Select the entry "Tag" from the list.

   The "Tag" dialog opens.
3. Click on the selection button under "Tag > Process > Tag". A dialog opens.
4. Click the "Add" button to add "MyTag" tag. Click "OK".
5. Go to "Properties > Miscellaneous > Reaction to input" and set how the values are to be handled in runtime, for example "Accept value after exit".

###### Result

The IO field has been configured as specified and connected to the tag. In runtime, you can see the current value of the tag in the IO field and can also input the value for the tag. The value is applied to the tag.

##### Example: Set values (RT Unified)

###### Task

In this example, you learn how to show the process values in runtime, enter the values, or change the values. You also learn how to visualize the display of the actual speed of a motor and how to regulate it.

You configure:

- Two IO fields for the input and output of the process values.
- Two text boxes for describing the IO fields.
- A slider to display and adjust the values.

###### Requirement

- A project is open.
- A screen is configured.
- The tags "SetValue" and "ActualValue" have been created as process values for the motor speed.

###### Configuring IO fields

With two IO fields, you can display the current value of the tags in the screen. You can enter the values for the process or change the values.

To configure the IO fields, follow these steps:

1. Insert the "IO field" object from the "Toolbox" task card into the screen.
2. Specify the height, width, and position for the object under "Properties > Size and position".
3. Under "Properties > General > Mode" specify the "Input/output" mode in the "Static value" column.
4. Click under "Properties > General > Process value". In the drop-down list of the "Dynamization" column, select the entry "Tag".

   The "Tag" dialog opens.
5. Under "Tag" specify the "SetValue" tag whose values you want to display and change in runtime.
6. Define an additional IO field for the "ActualValue" tag in "Output" mode.
7. Configure two text boxes, "Actual value" and "Set value", as the IO fields description.

| Symbol | Meaning |
| --- | --- |
| ![Configuring IO fields](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| - You can also create a new IO field by moving a configured tag from the detail view onto an HMI screen using drag-and-drop.  An IO field is created automatically and connected to the desired tag. |  |

###### Configuring a slider

You can use a slider to intervene in the process and change the displayed process value.

Follow these steps to configure the slider:

1. Add the "Slider" object to the screen from the "Toolbox" task card.
2. Specify the desired height, width and position for the object under "Properties > Size and position".
3. Under "Properties > Miscellaneous > Process value indicator - mode", specify the "Detailed indicator" mode in the "Static value" column.
4. Click under "Properties > General > Process value".
5. In the drop-down list of the "Dynamization" column, select the entry "Tag".

   The "Tag" dialog opens on the right in the Inspector window.
6. Under "Tag" specify the "SetValue" tag whose values you want to display and change in runtime.

###### Result

In runtime, the actual motor speed is displayed in the IO field. You can transfer the speed in the IO field "Set value" to the motor. Using the slider, you can read the actual speed and control the speed yourself by moving the slider.

### Controls (RT Unified)

This section contains information on the following topics:

- [Configuring the toolbar and information bar (RT Unified)](#configuring-the-toolbar-and-information-bar-rt-unified)
- [Alarm control (RT Unified)](#alarm-control-rt-unified)
- [Alarm control, simple (RT Unified)](#alarm-control-simple-rt-unified)
- [Trend control (RT Unified)](#trend-control-rt-unified)
- [Trend control, simple (RT Unified)](#trend-control-simple-rt-unified)
- [Function trend control (RT Unified)](#function-trend-control-rt-unified)
- [Trend companion (RT Unified)](#trend-companion-rt-unified)
- [Screen window (RT Unified)](#screen-window-rt-unified)
- [Faceplate container (RT Unified)](#faceplate-container-rt-unified)
- [Parameter set control (RT Unified)](#parameter-set-control-rt-unified)
- [System diagnostics control (RT Unified)](#system-diagnostics-control-rt-unified)
- [Process control (RT Unified)](#process-control-rt-unified)
- [Web control (RT Unified)](#web-control-rt-unified)
- [Media Player (RT Unified)](#media-player-rt-unified)
- [GRAPH overview](#graph-overview)
- [PLC code view (RT Unified)](#plc-code-view-rt-unified)
- [ProDiag overview](#prodiag-overview)

#### Configuring the toolbar and information bar (RT Unified)

##### Introduction

You can operate the controls in runtime using the buttons in the toolbar. The information bar displays the status messages of the control. During configuration, you define the contents of the toolbar and information bar.

> **Note**
>
> You have the possibility to address the buttons of the toolbar via a script using the "ExecuteToolbarButton" system function, even if the toolbar is hidden.
>
> You can use this function, for example, to create a custom toolbar or when there is little space available on the screen.

![Introduction](images/150697104139_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar |
| ② | Information bar |

##### Requirement

- You have opened the screen which contains at least one object, for example, the trend companion.
- The Inspector window is open.

##### Configuring the toolbar

To configure the toolbar, follow these steps:

1. In the Inspector window under "Properties > Miscellaneous > Toolbar", configure the general properties of the toolbar, such as background color or visibility.
2. In the Inspector window, under "Properties > Properties > Miscellaneous > Toolbar > Elements > Button > Visibility", enable the buttons that you need in Runtime.
3. Configure the button display, for example, background color, border and size.
4. Under "Properties > Properties > Miscellaneous > Toolbar > Elements > Button > Authorization", select the authorization that is required in Runtime to operate the button.
5. When a button is not operated in Runtime, disable "Allow operator control". You can reactivate a disabled a button by using a script in runtime, for example.

**Note**

Only elements whose visibility is activated in the TIA Portal are transferred to the runtime. Elements whose visibility is disabled in the TIA Portal are deleted from the array of elements. You cannot address the elements in runtime, via a script for example. If you hide an element, the numbering of the following element in the runtime changes.

Example: The parameter set control has 10 elements. Array numbers 0 to 9 are assigned to the elements in the TIA Portal. If you deactivate the visibility of the element with the array number 8, the element with the array number 9 must be addressed in runtime with the number 8.

If you want to hide an element and still access it, use dynamization, e.g. via a script.

##### Configuring the information bar

To configure the information bar, follow these steps:

1. In the Inspector window under "Properties > Properties > Miscellaneous > Information bar", configure the general properties of the information bar, such as background color or visibility.
2. In the Inspector window under "Properties > Properties > Miscellaneous > Information bar > Elements > State display > Visibility", enable the elements that you need in Runtime.
3. Configure the display of the respective element.
4. Select the authorization that is required in Runtime to operate the element.
5. When an element is not operated in Runtime, disable "Allow operator control". You can enable a disabled element again, for example, with a script in Runtime.

#### Alarm control (RT Unified)

##### Use

The "Alarm control" object displays the alarms that occur in a plant during the process. You can also use the alarm control to display the alarms in the lists. You configure the alarm display in the engineering system via the "Alarm control" object.

WinCC offers various views, such as "Show active alarms" or "Show logged alarms".

![Use](images/132489387019_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Alarm control": Specifies various properties for the display of alarms, such as background color and row height.
- "Sorting - allow": Defines whether the alarms are sorted in runtime.
- "Information bar": Defines the elements of the information bar.
- "Toolbar": Specifies the buttons of the alarm control.
- "Focus - show visual": Specifies whether the selected properties are visible.

##### Specifying the properties of the alarm control

To specify the properties of the alarm control, follow these steps:

1. In the Inspector window, click "Properties > Properties > Miscellaneous > Alarm control".
2. Define settings for the rows and cells, e.g.:

   - "Row height": Specifies the height of the lines in the alarm control.
3. Define the settings for the headers under "Header - settings", e.g.:

   - "Row header": Defines whether each row has a header.
   - "Column header": Specifies the representation of the column header.
4. Define the width and color of the grid lines.
5. Define the use of scroll bars.

##### Configure output of alarms

To configure the outputs of the alarm control, specify the following properties:

- "General > Alarm source": Specifies which alarms are displayed in this alarm control.
- "Miscellaneous > Alarms - show current":

  If you activate this property, the following applies in runtime:

  - The recent alarms are always shown first in the alarm control.
  - Alarms that have been filtered out of the alarm control are not displayed.
  - ​The visible area of the alarm control moves automatically, if necessary.
  - Users cannot select the alarms individually or sort them by column.

  If you configure the "Alarms - Show current" button as visible and operable, you can pause and start this behavior in runtime as required. The alarm control always starts with the behavior configured via "Miscellaneous > Alarms - Show current".
- "Miscellaneous > Alarm statistics settings": Setting options that contribute to the evaluation of the alarm statistics, e.g. start time, maximum number of alarms.

##### Setting up column sorting

To set up the column sorting, follow these steps:

1. In the Inspector window, click on "Properties > Miscellaneous > Alarm control > Columns > [1] Alarm statistics column".
2. Select the sorting direction and sorting order for the individual columns.

Under "Properties > Properties > Format > Default sorting direction", define the sort direction of the alarms in the alarm control, e.g. "Ascending".

##### Configuring reordering of the columns

You can configure whether operators can rearrange the table columns using drag-and-drop in Runtime. More information is available in the section [Configuring reordering of the columns](#configuring-reordering-of-the-columns-rt-unified).

##### Access protection in runtime

To configure access protection in runtime, follow these steps:

- Activate the "Operator control - allow" property under "Properties > Properties > Miscellaneous > Toolbar > Elements > [1] Button > Operator control - allow".
- Define the type of authorization in the "Static value" column under "Properties > Properties > Miscellaneous > Toolbar > Elements > [1] Button > Authorization".

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

##### Setting the time zone

Under Properties > Properties > Miscellaneous > Time zone, you set the desired time zone by entering a decimal value for the time zone.

- "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
- "-1": The local time zone of the device.

You can also set the time zone via a selection list in runtime.

##### Configuring the information bar

The information bar of the alarm control shows you, for example, the current time and the connection status.

To configure the information bar, follow these steps:

1. Configure the general properties of the information bar, such as the font and background color, under "Properties > Properties > Miscellaneous > Information bar".
2. Configure the display of the information bar elements under "Properties > Properties > Miscellaneous > Information bar > Elements".

##### Toolbar

You can define the buttons of the alarm control in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the alarm control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/132457983883_DV_resource.Stream@PNG-de-DE.png) | Show active alarms | Show the currently pending alarms. |
| ![Toolbar](images/132458068107_DV_resource.Stream@PNG-de-DE.png) | Show logged alarms | Shows the logged alarms. |
| ![Toolbar](images/132458075531_DV_resource.Stream@PNG-de-DE.png) | Show and update logged alarms | Updates the logged alarms and shows them. |
| ![Toolbar](images/132459375883_DV_resource.Stream@PNG-de-DE.png) | Show defined alarms | Shows the alarms configured in the system. |
| ![Toolbar](images/139055181963_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics - view | Visualizes statistical information, such as frequency and display duration of logged alarms. |
| ![Toolbar](images/155638139659_DV_resource.Stream@PNG-de-DE.png) | Alarm annunciator | Not supported in WinCC Unified. |
| ![Toolbar](images/132458615563_DV_resource.Stream@PNG-de-DE.png) | First line | Selects the first of the pending alarms. The visible area of the alarm control is moved.   This button is only operable if the "Alarms - show current" button is disabled. |
| ![Toolbar](images/132458689035_DV_resource.Stream@PNG-de-DE.png) | Previous line | Selects the previous alarm, starting from the currently selected alarm. The visible area of the alarm control is moved.   This button is only operable if the "Alarms - show current" button is disabled. |
| ![Toolbar](images/132458681611_DV_resource.Stream@PNG-de-DE.png) | Next line | Selects the next alarm, starting from the currently selected alarm. The visible area of the alarm control is moved.   This button is only operable if the "Alarms - show current" button is disabled. |
| ![Toolbar](images/132458622987_DV_resource.Stream@PNG-de-DE.png) | Last line | Selects the last of the pending alarms. The visible area of the alarm control is moved.   This button is only operable if the "Alarms - show current" button is disabled. |
| ![Toolbar](images/132459718923_DV_resource.Stream@PNG-de-DE.png) | Move to next acknowledgeable alarm | Selects the next alarm, starting from the currently selected alarm. The visible area of the alarm control is moved.   This button is only operable if the "Alarms - show current" button is disabled. |
| ![Toolbar](images/132459055883_DV_resource.Stream@PNG-de-DE.png) | Previous page | Navigates to the next page |
| ![Toolbar](images/132459217163_DV_resource.Stream@PNG-de-DE.png) | Next page | Moves to the previous page |
| ![Toolbar](images/132458249611_DV_resource.Stream@PNG-de-DE.png) | Single acknowledgment | Acknowledges a single alarm.  A counter shows how many alarms are unacknowledged. The counter includes all connected servers, but no filters. |
| ![Toolbar](images/132458359435_DV_resource.Stream@PNG-de-DE.png) | Acknowledge visible alarms | Acknowledges all visible alarms requiring acknowledgment in the alarm control, if they do not require single acknowledgment. |
| ![Toolbar](images/132458428939_DV_resource.Stream@PNG-de-DE.png) | Single confirm | Resets the alarm. Relevant for alarms with the state machine "Alarm with acknowledgment and confirmation" that have already been acknowledged and are outgoing. |
| ![Toolbar](images/132458366859_DV_resource.Stream@PNG-de-DE.png) | Alarms - show current | Defines whether the current alarm is always highlighted in the alarm control.   Button not pressed: The "Alarms - show current" button is enabled.  - The current alarms are always displayed first in the alarm control. - The visible area of the alarm control moves automatically, if necessary. - You cannot select the alarms individually or sort them by column.   Button pressed: The "Alarms - show current" button pauses. |
| ![Toolbar](images/132458734859_DV_resource.Stream@PNG-de-DE.png) | Info text - configuration | Opens a dialog to display an info text. |
| ![Toolbar](images/100729025803_DV_resource.Stream@PNG-de-DE.png) | Comment - configuration | Opens a dialog for adding a comment. |
| ![Toolbar](images/140319026315_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics - setup | Opens the dialog to change the time range for the alarm statistics. |
| ![Toolbar](images/132458742283_DV_resource.Stream@PNG-de-DE.png) | Disable alarm | Hides an alarm in the current alarm list and in the alarm log lists. The alarm is added to the "Locked alarms" display. |
| ![Toolbar](images/132459726603_DV_resource.Stream@PNG-de-DE.png) | Enable alarm | Shows an alarm again. |
| ![Toolbar](images/132458989579_DV_resource.Stream@PNG-de-DE.png) | Shelve alarm | Shelves an alarm, for example, to prevent an alarm message from impairing the effectiveness of your system. The alarm appears in the "Shelved alarms" control. |
| ![Toolbar](images/132458892555_DV_resource.Stream@PNG-de-DE.png) | Unshelve alarm | Cancels the reset of the respective alarm. |
| ![Toolbar](images/132459549963_DV_resource.Stream@PNG-de-DE.png) | Copy lines | Copies the selected alarms. |
| ![Toolbar](images/132458885131_DV_resource.Stream@PNG-de-DE.png) | Time base - configuration | Opens a dialog for setting the time zone for the time information shown in alarms. |
| ![Toolbar](images/132459557643_DV_resource.Stream@PNG-de-DE.png) | Selection display | Opens a dialog for filtering alarms. You can define the filter criteria or filter the alarms by criteria defined in the engineering system. |
| ![Toolbar](images/132458826507_DV_resource.Stream@PNG-de-DE.png) | Sorting setup | Opens a dialog for setting user-defined sort criteria for the displayed alarms. |
| ![Toolbar](images/132459317003_DV_resource.Stream@PNG-de-DE.png) | Display options - configuration | Opens a dialog for configuring the display options of the alarm control. You can define which alarms are displayed, for example, only shelved alarms or all alarms. |
| ![Toolbar](images/132459309323_DV_resource.Stream@PNG-de-DE.png) | Locked alarms - configuration | Opens a dialog for configuring the display options of the locked alarms. |
| ![Toolbar](images/132458997003_DV_resource.Stream@PNG-de-DE.png) | Export | Starts the export of alarms to a .CSV file. |
| ![Toolbar](images/132822801163_DV_resource.Stream@PNG-de-DE.png) | Select context | Opens the configuration dialog of the context. |

##### Restrictions on Unified Comfort Panel

If you use the "Alarm control" control on the Unified Control Panel, be aware of the following restrictions:

- Flashing on range violation is not supported for the alarm control.
- Scroll bars are not available in the alarm control. Use the touchscreen to move the contents of the alarm control horizontally or vertically.
- The "Show current" function is only supported in connection with ascending sorting order.
- Moving columns within the alarm control is not supported.
- If you have configured a text for the first element in the status bar and a screen for the second element, the screen may not be displayed immediately after loading. In this case, perform a screen change.
- Multiple selection of filter criteria is not supported in the filter dialog of the alarm control.
- The dynamization of the visibility of columns via a script or a system function is not supported.

---

**See also**

[Configuring the alarm control (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-alarm-control-rt-unified-1)
  
[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)
  
[Alarm terminology (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#alarm-terminology-rt-unified)
  
[Alarm control, simple (RT Unified)](#alarm-control-simple-rt-unified)

#### Alarm control, simple (RT Unified)

##### Use

The "Alarm control, simple" object is used for the simple display of alarms on devices with device version V19 or higher. You can configure the display and functions of the simple alarm control in the same way as with the alarm control on other devices.

![Use](images/172564689291_DV_resource.Stream@PNG-en-US.png)

The simple alarm control is available:

- As standard on Unified Basic Panels.
- As an option on other devices.

The simple alarm control is available in all the styles selected under the device's Runtime settings.

##### Layout

In the simple alarm control, the following columns are activated:

- ID
- Alarm text
- Raise time

You can change the visibility of the disabled columns in the Inspector window.

In the simple alarm control, the visibility of the following is disabled:

- Window settings
- Toolbar
- Information bar

##### Selecting simple alarm control

On devices other than the Unified Basic Panel, you can choose between two alarm control style items:

1. Under "Properties > Properties > Appearance", select the property "Appearance - style item".
2. Select one of the following in the "Static value" column.

   - "HmiAlarmControl" for the alarm control.
   - "SimplifiedAlarmControl" for the simple alarm control.

If you switch from the "HmiAlarmControl" style item to the "SimplifiedAlarmControl" style item, the following applies:

- Properties that are supported by "SimplifiedAlarmControl" retain their value and can be changed at will.
- Properties not supported by "SimplifiedAlarmControl" are no longer displayed. If you configure the "HmiAlarmControl" style item again, these properties will have their original value.

![Selecting simple alarm control](images/172728543499_DV_resource.Stream@PNG-en-US.png)

##### Changing device type

If you change the device type, the configured properties are retained.

---

**See also**

[Alarm control (RT Unified)](#alarm-control-rt-unified)

#### Trend control (RT Unified)

##### Use

You can use the "Trend control" object to display tag values from the current process or from the log in the form of trends as an autorepeat.

![Use](images/152951877899_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The trend area located in the future continues the last drawn value.

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Trend areas": Specifies the representation of the trends.
- "Trends": Defines the configuration of the trends.
- "Toolbar": Defines the buttons for the trend control.

##### Configuring the trend area

To configure the trend display, follow these steps:

1. Create the following under "Properties > Properties > General > Trend areas":

   - Common or individual trend areas
   - Common or separate axes
   - Writing direction of all trends

   By default, the first trend area [0] is already created in the object. You can create more trend areas using the selection button in the "Static value" column.
2. Configure the value axes and the time axes.
3. Open the settings of the time axis under "Properties > General > Time axes bottom > Time axis [0]".

   Configure the "Time range" of the trend display:

   - "Time interval": You define the time range using a starting time and a following time interval.
   - "Start time and end time": You define the time range using a starting time and an end time.
   - "Measuring points": You define the time range using a starting time and a number of measuring points.
4. Open the settings of the value axis under "Properties > General > Trend areas > Trends > Left value axis > Value axis Y [0]":

   - If required, configure the value range, the output format, and the scaling of the value axis.
   - If required, configure the value range, the output format, and the scaling of the value axis.
5. Go to "Properties > General > Trend areas > Trends" and configure the trends for the trend area.

> **Note**
>
> In a trend control with several configured trend areas, the buttons "First data record" and "Last data record" always act only on the last trend area that was configured. In other trend areas, you can use the "Select time range" button to navigate to the first or last data record.  
> If you have to navigate to the first or last data record very frequently in all configured trend areas, it is advisable to configure the trend area in multiple trend controls.

##### Configuring trends

To configure the trends for each trend area, follow these steps:

1. Select the data supply for the respective trend under "Properties > General > Trend areas > Trends > [0] Trend > Data source Y > Source":

   - "Logging tag": The trend control is supplied with values from a tag log.
   - "HMI tag": The trend control is supplied with values of a tag.
2. Select the data supply for the tag under "Properties > General > Trend areas > Trends > Trend [0] > Data source Y > Tag".

   - In the case of an HMI tag, specify the tag name in the "Static value" column.
   - In the case of a logging tag, enter the name of the HMI tag in the "Static value" column first.   
     Enter the name of the associated logging tags separated by a colon, for example, "HMITag_1:LoggingTag_1".
3. Configure the display mode for trends under "Trend mode".

> **Note**
>
> In a trend control with multiple trends, a trend can also be selected using the legend in runtime.

##### Dynamically hiding axes

You can toggle the visibility of the trend axes via a script.

If the axes are dynamically hidden on a Unified Panel, the trend area is enlarged. This enables optimal use of the available space, especially on panels with small display diagonals. This behavior is not detectable in the simulation.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Graphic - pressed button
- Icon

##### Setting the time zone

Under "Properties > Properties > Miscellaneous > Time zone", you set the desired time zone by entering a decimal value for the time zone.

- "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
- "-1": The local time zone of the device.

You can also set the time zone via a selection list in runtime.

##### Toolbar

You can define the buttons of the trend control in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the trend control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/100727706251_DV_resource.Stream@PNG-de-DE.png) | First record | Shows the trend direction starting with the first logged value. |
| ![Toolbar](images/100727713931_DV_resource.Stream@PNG-de-DE.png) | Previous record | Shows the trend direction of the previous time interval. |
| ![Toolbar](images/100727802635_DV_resource.Stream@PNG-de-DE.png) | Start/Stop | Stops and starts the trend update.  Started: The trend is continuously updated. It always shows the latest values.  Stopped: New values are buffered and updated as soon as you start the trend update again. |
| ![Toolbar](images/100727721611_DV_resource.Stream@PNG-de-DE.png) | Next record | Shows the trend direction of the next time interval. |
| ![Toolbar](images/100727729291_DV_resource.Stream@PNG-de-DE.png) | Last record | Shows the trend direction up to the last logged value. |
| ![Toolbar](images/100727787275_DV_resource.Stream@PNG-de-DE.png) | Previous trend | Displays the previous trend in the foreground. |
| ![Toolbar](images/100727794955_DV_resource.Stream@PNG-de-DE.png) | Next trend | Displays the next trend in the foreground. |
| ![Toolbar](images/100727736971_DV_resource.Stream@PNG-de-DE.png) | Ruler | Determines the coordinates of a point of the trend. |
| ![Toolbar](images/102865768459_DV_resource.Stream@PNG-de-DE.png) | Zoom time axis +/- | Enlarges or reduces the time axis display. |
| ![Toolbar](images/102865777291_DV_resource.Stream@PNG-de-DE.png) | Zoom value axis +/- | Enlarges or reduces the value axis display. |
| ![Toolbar](images/102864432395_DV_resource.Stream@PNG-de-DE.png) | Zoom area | Increases the size of any section of the trend window. |
| ![Toolbar](images/102865759627_DV_resource.Stream@PNG-de-DE.png) | Zoom +/- | Enlarges or reduces the view in the trend window. |
| ![Toolbar](images/104586572427_DV_resource.Stream@PNG-de-DE.png) | Move trend area | Moves the display in the trend area.   Values from the future trend area apply the last displayed value. |
| ![Toolbar](images/100727936011_DV_resource.Stream@PNG-de-DE.png) | Move axes area | Moves the display in the axes area. |
| ![Toolbar](images/100727752331_DV_resource.Stream@PNG-de-DE.png) | Original view | Switches from the magnified trend control back to the normal view. |
| ![Toolbar](images/100727779595_DV_resource.Stream@PNG-de-DE.png) | Select time range | Opens the dialog for setting the time range displayed in the trend window. |
| ![Toolbar](images/100727767691_DV_resource.Stream@PNG-de-DE.png) | Select trends | Opens the dialog for setting the visibility of trends. |
| ![Toolbar](images/100727760011_DV_resource.Stream@PNG-de-DE.png) | Select data connection | Opens the dialog for selecting the logs and tags to serve as the data source for the trend control. |
| ![Toolbar](images/100727817995_DV_resource.Stream@PNG-de-DE.png) | Statistics area | Enables you to define a time range for which statistical values are determined. Vertical lines which you use to set the time range are displayed in the trend window.   To display the values, connect the trend control to the trend companion. |
| ![Toolbar](images/100727825675_DV_resource.Stream@PNG-de-DE.png) | Calculate statistics | Opens a statistics window to display the minimum, maximum, means, and standard deviation for the selected time range and the selected trend.   To display the values, connect the trend control to the trend companion. |
| ![Toolbar](images/100727810315_DV_resource.Stream@PNG-de-DE.png) | Print | PC: Starts printing the trends shown in the trend window.   Unified Comfort Panel: The data are sent to the specified standard printer in the Control Panel. The last 10 print jobs are saved as a graphic on the panel in the directory /home/industrial/ControlScreenshot.  Unified Basic Panel: The print function is not supported. |
| ![Toolbar](images/100727833355_DV_resource.Stream@PNG-de-DE.png) | Export | Opens the dialog for saving the trend data in CSV format. |
| ![Toolbar](images/155636569483_DV_resource.Stream@PNG-de-DE.png) | Select context | Opens the configuration dialog of the context. |

---

**See also**

[Configuring a trend control (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-a-trend-control-rt-unified)
  
[Configuring the toolbar and information bar (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-the-toolbar-and-information-bar-rt-unified)
  
[Defining the data source (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#defining-the-data-source-rt-unified)
  
[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)
  
[Trend control, simple (RT Unified)](#trend-control-simple-rt-unified)

#### Trend control, simple (RT Unified)

##### Use

The "Simple trend control" object is used for the display of tag values on devices with device version V19 or higher. You can configure the display and functions of the simple trend control in the same way as with the trend control on other devices.

![Use](images/172567372939_DV_resource.Stream@PNG-en-US.png)

The simple trend control is available:

- As standard on Unified Basic Panels.
- As an option on other devices.

The simple trend control is available in all styles that you select under the device's Runtime settings.

##### Layout

In the simple trend control, the visibility of the following is deactivated:

- Window settings
- Toolbar
- Information bar
- Legend

##### Selecting the simple trend control

On devices other than the Unified Basic Panel, you can choose between two trend control style items:

1. Under "Properties > Properties > Appearance", select the property "Appearance - style item".
2. Select one of the following in the "Static value" column.

   - "HmiTrendControl" for the trend control.
   - "SimplifiedTrendControl" for the simple trend control.

If you switch from the "HmiTrendControl" style item to the "SimplifiedTrendControl" style item, the following applies:

- Properties that are supported by "SimplifiedTrendControl" retain their value and can be changed at will.
- Properties not supported by "SimplifiedTrendControl" are no longer displayed. If you configure the "HmiTrendControl" style item again, these properties will have their original value.

![Selecting the simple trend control](images/172728553867_DV_resource.Stream@PNG-en-US.png)

##### Changing device type

If you change the device type, the configured properties are retained.

---

**See also**

[Trend control (RT Unified)](#trend-control-rt-unified)

#### Function trend control (RT Unified)

##### Use

You can use the "Function trend control" object to represent the values of a tag as a function of another tag. This means that you can present temperature trends as a function of the pressure, for example. You can also compare the trend to a setpoint trend.

![Use](images/162574116619_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The trend area located in the future continues the last drawn value.

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Function trends": Defines the configuration of the function trends.
- "Toolbar": Defines the buttons of the function trend control.

##### Configuring function trends

To configure the function trends for each function trend area, follow these steps:

1. Select the data supply for the function trend under "Properties > General > Function trend - area > Function trends > [0] Function trend > Data source X > Source".

   - "Logging tag": The trend control is supplied with values from a tag log.
   - "HMI tag": The trend control is supplied with values of a tag.
2. Enter the tag name under "Properties > General > Function trend - areas > [0] Function trend - area > Function trends > [0] Function trend > Data source X > Tag":

   - In the case of an HMI tag, specify the tag name in the "Static value" column.
   - In the case of a logging tag, enter the name of the HMI tag in the "Static value" column first. Enter the name of the associated logging tags separated by a colon, for example, "HMITag_1:LoggingTag_1".
3. Configure the data supply for "Data source Y".
4. Open the settings of the time axis under "Properties > General > Function trend - area > Function trends > [0] Function trend > Time range".

   Configure the trend display for the "Time range".

   - "Time interval": You define the time range using a starting time and a following time interval.
   - "Start time and end time": You define the time range using a starting time and an end time.
   - "Measuring points": You define the time range using a starting time and a number of measuring points.
5. Configure the value range of the trend display under:

   - "Properties > General > Function trend - areas > [0] Function trend - area > Value axes - left > [0] Value axis Y".
   - "Properties > General > Function trend - areas > [0] Function trend - area > Value axes - bottom > [0] Value axis X".

   Select one of the options:

   - "Automatically adapt value range". The displayed value range is automatically adapted to the current values.
   - "Scale value - maximum" and "Scale value - minimum". Define the minimum value and maximum value for the value range.

##### Dynamically hiding axes

You can toggle the visibility of the trend axes via a script.

If the axes are dynamically hidden on a Unified Panel, the trend area is enlarged. This enables optimal use of the available space, especially on panels with small display diagonals. This behavior is not detectable in the simulation.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Graphic - pressed button
- Icon
- Marker graphic

##### Toolbar

You can define the buttons of the function trend control in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the function trend control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/100727802635_DV_resource.Stream@PNG-de-DE.png) | Start/Stop | Stops and starts the trend update.  Started: The trend is continuously updated. It always shows the latest values.  Stopped: New values are buffered and updated as soon as you start the trend update again. |
| ![Toolbar](images/102865768459_DV_resource.Stream@PNG-de-DE.png) | Zoom X axis +/- | Zooms in to or out of the X axis in the trend window. |
| ![Toolbar](images/102864432395_DV_resource.Stream@PNG-de-DE.png) | Zoom area | Increases the size of any section of the trend window. |
| ![Toolbar](images/100727744651_DV_resource.Stream@PNG-de-DE.png) | Zoom +/- | Enlarges and/or shrinks the trends in the trend window. |
| ![Toolbar](images/100727919371_DV_resource.Stream@PNG-de-DE.png) | Zoom Y axis +/- | Enlarges and/or reduces the Y axis in the trend window. |
| ![Toolbar](images/100727752331_DV_resource.Stream@PNG-de-DE.png) | Original view | Switches from the magnified trend control back to the normal view. |
| ![Toolbar](images/100727787275_DV_resource.Stream@PNG-de-DE.png) | Previous trend | Displays the previous trend in the foreground. |
| ![Toolbar](images/100727794955_DV_resource.Stream@PNG-de-DE.png) | Next trend | Displays the next trend in the foreground. |
| ![Toolbar](images/100727736971_DV_resource.Stream@PNG-de-DE.png) | Ruler | Determines the coordinates of a point of the trend. |
| ![Toolbar](images/100727927691_DV_resource.Stream@PNG-de-DE.png) | Move trend area | Moves the trends along the X axis and Y axis in the trend window.  Values from the future trend area apply the last displayed value. |
| ![Toolbar](images/100727936011_DV_resource.Stream@PNG-de-DE.png) | Move axes area | Moves the trends along the value axis in the trend window. |
| ![Toolbar](images/100727779595_DV_resource.Stream@PNG-de-DE.png) | Select time range | Opens the dialog for setting the time range displayed in the trend window. |
| ![Toolbar](images/100727976587_DV_resource.Stream@PNG-de-DE.png) | Select trends | Opens a dialog for setting the visibility of trends. |
| ![Toolbar](images/100727760011_DV_resource.Stream@PNG-de-DE.png) | Select data connection | Opens a dialog for selecting logs and tags. |
| ![Toolbar](images/100727810315_DV_resource.Stream@PNG-de-DE.png) | Print | PC: Starts printing the trends shown in the trend window.   Unified Comfort Panel: The data are sent to the specified standard printer in the Control Panel. The last 10 print jobs are saved as a graphic on the panel in the directory /home/industrial/ControlScreenshot.  Unified Basic Panel: The print function is not supported. |
| ![Toolbar](images/100727833355_DV_resource.Stream@PNG-de-DE.png) | Export | Starts the export of all or the selected runtime data to a "CSV" file. |

---

**See also**

[Configuring the function trend control (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-the-function-trend-control-rt-unified)
  
[Configuring the toolbar and information bar (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-the-toolbar-and-information-bar-rt-unified)
  
[Defining the data source (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#defining-the-data-source-rt-unified)
  
[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

#### Trend companion (RT Unified)

##### Use

You use the "Trend companion" object to show evaluated data and statistics from a trend control or function trend control in a table.

![Use](images/162767870091_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Data source": Specifies the source for representing the values.
- "Trend companion - mode": Defines the mode of the values display in the trend companion.
- "Toolbar": Specifies the buttons in the trend companion.

##### Defining the data source for displaying the values

To define the display of values in the trend companion, follow these steps:

1. Configure a trend control or a function trend control.
2. Select the trend companion. Click "Properties > General > Data source".
3. Select the trend control or function trend control as the data source.

To adapt the display to the connected object, select the "Data source - use background color" and "Data source - use font color" options under "Properties > Format".

By default, the format of the connected object is adopted during the configuration for the display format. The size, value range and zoom factor of the object are taken into account to display the optimum number of decimal places.

You can configure the display formats for individual values in the Inspector window of the trend companion, for example, to display an exact number of decimal places.

##### Defining the mode of the trend companion

To define the mode of the trend companion, follow these steps:

1. Select the mode under "Properties > Properties > General > Trend companion - mode".
2. Select one of 3 different mode types depending on the data source:

   - The "Ruler" mode shows the coordinate values of the trends on the ruler or the values of a selected row in the table.
   - The "Statistics area" mode shows the values of the low limit and high limit of the trends between two rulers or the selected area in the table.

     The "Statistics area" mode is not available for the function trend control object.
   - The "Statistic result" mode shows the statistical evaluation of the trends between two rulers or the selected values in the table.

     The "Statistics result" mode is not available for the "function trend control" object.

##### Configuring reordering of the columns

You can configure whether operators can rearrange the table columns using drag-and-drop in Runtime. More information is available in the section [Configuring reordering of the columns](#configuring-reordering-of-the-columns-rt-unified).

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

##### Setting the time zone

Under Properties > Properties > Miscellaneous > Time zone, you set the desired time zone by entering a decimal value for the time zone.

- "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
- "-1": The local time zone of the device.

You can also set the time zone via a selection list in runtime.

##### Toolbar

You can define the buttons of the trend companion in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the trend companion:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/100731434635_DV_resource.Stream@PNG-de-DE.png) | Calculate statistics | Shows the statistical values in the statistics window. The displayed values refer to a selected trend with the configured calculation time period.   The button is only enabled if a statistics window is connected with a trend control. |
| ![Toolbar](images/100731376651_DV_resource.Stream@PNG-de-DE.png) | Statistics area | Enables you to define a time range for which statistical values are determined. |
| ![Toolbar](images/102862132107_DV_resource.Stream@PNG-de-DE.png) | Ruler window | Queries the coordinate points of a trend. The trend data are displayed in the ruler window. |
| ![Toolbar](images/111934860811_DV_resource.Stream@PNG-de-DE.png) | Print | PC: Reserved for future versions.  Unified Panel: The data are sent to the specified standard printer in the Control Panel. The last 10 print jobs are saved as a graphic on the panel in the directory /home/industrial/ControlScreenshot.  Unified Basic Panel: The print function is not supported. |
| ![Toolbar](images/100731364747_DV_resource.Stream@PNG-de-DE.png) | Export | Starts the export of all or the selected runtime data to a "csv" file. |

---

**See also**

[Configuring the trend companion (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-the-trend-companion-rt-unified)
  
[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

#### Screen window (RT Unified)

##### Use

You can use the "Screen window" object to represent other screens from the project in the current screen. To constantly update the content of a screen window, for example, you dynamize the object.

You can also use independent screen windows independently of the screen in question. With appropriate hardware equipment and support by the operating system you can also control multiple monitors and map processes in a more comprehensive and differentiated manner.

![Use](images/100727419659_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Zoom - factor": Defines the size of the embedded screen.
- "Size - fit": Specifies whether:

  - The embedded screen is scaled to the size of the screen window.
  - The screen window is scaled to the size of the embedded screen.

##### Matching the size of the embedded screen and screen window

To match the size of the embedded screen to the size of the screen window, choose one of the following options:

- You want the embedded screen to appear smaller or larger:

  Set the desired zoom factor in the Inspector window "Properties > Format > Zoom - factor". Enter the value between 0.1 and 8.
- You want to scroll to a section of the embedded screen:

  - In the "Properties > Format" Inspector window, activate the visibility of the horizontal and vertical scroll bar.
  - Set the position of the scroll bars.

    The user can move to details of the embedded screen in runtime.
- You can adapt the embedded screen to the size of the screen window, or vice versa:

  Select either "Fit window to screen", or "Fit screen to window" under "Properties > Format > Size - fit" in the Inspector window.

##### Dynamization of screens in screen windows

You can configure screens in screen windows that are dynamized via a tag or a script.  
In this case, note when configuring the screen window:

- Dynamization via a script: A static value must always be configured for the "Screen" property of the screen window.
- Dynamization via a tag: Specify the screens to be displayed as conditions of the dynamization tag. Direct specification of the screen name in the dynamization tag is not possible.

##### Opening cascaded screen windows in a screen window

Screen windows can also display screens that, in turn, contain screen windows. Up to 14 cascaded screen windows can be displayed.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following property containing a graphic with a tag or with a script:

- Icon

##### Adapting the size in runtime

To resize a screen window in runtime, follow these steps:

1. Activate the options "Show border" and "Can be sized" in the Inspector window "Properties > Appearance > Window settings".

   The width of the border is not evaluated.

If the embedded screen is larger than the screen window, you can configure the scroll bars for the screen window under "Properties > Format".

##### Moving the screen window in runtime

To move a screen window in runtime, follow these steps:

1. Activate the options "Show heading" and "Can be moved" in the Inspector window "Properties > Appearance > Window settings".

##### Zooming the screen window in runtime

To zoom the screen window in runtime, follow these steps:

1. Under "Properties > Format", activate the "Zoom - allow" property. The property is enabled by default in the Engineering System.

In runtime, use:

- Mouse:

  - Press <Ctrl>. Move the mouse wheel up or down at the same time. The screen is zoomed into or out of.
- Keyboard:

  - To zoom into the screen, press <Ctrl + Plus>.
  - To zoom out of the screen, press <Ctrl + Minus>.

##### Moving a screen section in runtime

To move the displayed screen section, follow these steps:

1. Under "Properties > Format", activate the "Zoom - allow" property. The property is enabled by default in the Engineering System.

In runtime, use:

- Mouse:

  - Hold down the left mouse button and move the mouse in the desired direction.
  - To move up, move the mouse wheel upwards.

    To move down, move the mouse wheel downwards.
- The following keys on the keyboard:

  - Arrow keys: Move left/right and up/down
  - Screen keys: Move up/down
  - <Home>: Show upper left corner
  - <End>: Show lower right corner

##### Clicking on an object behind the screen window in runtime

Screen windows can overlay other objects placed on the screen that users must operate in runtime.

To click on an object placed under the screen window in runtime, follow these steps:

1. Under "Properties > General > Screen", select the screen you want to load into the screen window, for example, "Screen_2".
2. Set the "Transparent" entry in the "Static value" column under "Appearance > Background - fill pattern" in the properties of the screen selected in step 1.

Application example:

You use a round menu with a button next to it. To prevent the rectangular border surrounding the menu from obscuring the button, make the menu available in a screen window. Proceeding as described above has the result that the button remains operable for users.

---

**See also**

[Zooming in on the screen in the screen editor (RT Unified)](#zooming-in-on-the-screen-in-the-screen-editor-rt-unified)

#### Faceplate container (RT Unified)

##### Use

The faceplate container is used to display faceplates in runtime. If a faceplate type has been instantiated in the container, the desired faceplate type is specified in the "Contained type" property.

You can find detailed information on configuring faceplates in the section "[Configuring faceplates](#basics-of-faceplates-rt-unified)".

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Window settings": Specifies the representation of the faceplate container in runtime.
- "Faceplate type": Defines the faceplate type that is instantiated in the faceplate container.

##### Defining window settings

To resize a faceplate instance in runtime, activate the options "Show border" and "Can be sized" in the Inspector window "Properties > Appearance > Window settings".

The width of the border is not evaluated.

To move a faceplate instance in runtime, select the options "Show heading" and "Can be moved" in the Inspector window under "Properties > Appearance > Window settings".

##### Defining the faceplate type

To define the faceplate type, select the faceplate type that is instantiated in the faceplate container under "Properties > Miscellaneous > Faceplate type".

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following property containing a graphic with a tag or with a script:

- Icon

---

**See also**

[Basics of faceplates (RT Unified)](#basics-of-faceplates-rt-unified)

#### Parameter set control (RT Unified)

##### Use

You can use the "Parameter set control" object to display and manage parameter sets in runtime and to exchange them with the controller.

![Use](images/164241066507_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Editing mode": Defines the activation status of the toolbar buttons.
- "Toolbar": Defines the buttons of the parameter set control.
- "Information bar": Specifies the representation of the information bar.
- "Parameter view": Specifies the display of the parameter table in the object.

##### Using a parameter set type

If you only want to use a particular parameter set type with its parameter sets in runtime, select the desired parameter set type under "Properties > General > Fixed parameter set type".

##### Configuring the time zone

To configure the time zone, follow these steps:

Under "Properties > Miscellaneous > Time zone", set the desired time zone by entering a numerical value.

The numerical value stands for a time zone, for example:

- "-1" stands for UTC-1h (Central European Time, standard time)
- "1" stands for UTC-12h (International Date Line West)
- "2" stands for UTC-11h (Hawaii)

##### Defining the editing mode

To specify the editing mode and to enable or disable the buttons, follow these steps:

Under "Properties > Miscellaneous > Editing mode", configure the activation status of the toolbar buttons "Create", "Save", "Save as", "Rename" and "Delete". These toolbar buttons are used to edit parameter sets.

You can select between the following settings:

- "None": Deactivates all buttons.
- "Update": Activates the "Save" and "Rename" buttons.
- "Create": Activates the "Create" and "Save as" buttons.
- "Delete": Activates the "Delete" button.

##### Configuring reordering of the columns

Configure whether operators can reorder the table columns in runtime using drag-and-drop. More information is available in the section [Configuring reordering of the columns](#configuring-reordering-of-the-columns-rt-unified).

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

##### Setting the time zone

Under Properties > Properties > Miscellaneous > Time zone, you set the desired time zone by entering a decimal value for the time zone.

- "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
- "-1": The local time zone of the device.

You can also set the time zone via a selection list in runtime.

##### Configuring the information bar

To configure the information bar, follow these steps:

1. Configure the general properties of the information bar, such as the font and background color, under "Properties > Miscellaneous > Information bar".
2. To adjust the height of the "Status text" element, specify the height under "Properties > Miscellaneous > Information bar > Elements > [0] Element".

The "Status Text" element is the only status line element of the parameter set control. Status messages are displayed in this element in runtime.

##### Toolbar

You can define the buttons of the parameter set control in runtime and their operator authorizations in the Inspector window under "Properties > Miscellaneous > Toolbar > Elements". By default, all buttons are displayed in the toolbar. To hide specific buttons, deactivate the "Visibility" property in the settings of the corresponding button.

> **Note**
>
> Buttons for which the "Visibility" option is deactivated during the configuration cannot be made visible again in runtime by a script. After loading into a device, the array of available items contains only those buttons that are configured as visible.

The following buttons are available for the parameter set control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/110181830795_DV_resource.Stream@PNG-de-DE.png) | Create | Creates a new parameter set. |
| ![Toolbar](images/110183221771_DV_resource.Stream@PNG-de-DE.png) | Save | Saves a parameter set. |
| ![Toolbar](images/110183230347_DV_resource.Stream@PNG-de-DE.png) | Save as | Saves an existing parameter set under a new name and new ID. |
| ![Toolbar](images/110183264523_DV_resource.Stream@PNG-de-DE.png) | Rename | Renames the selected parameter set. |
| ![Toolbar](images/110183337099_DV_resource.Stream@PNG-de-DE.png) | Write to PLC | Writes the values of the selected parameter set to the PLC. |
| ![Toolbar](images/110183345675_DV_resource.Stream@PNG-de-DE.png) | Read from PLC | Writes the values of the selected parameter set from the PLC. |
| ![Toolbar](images/110183443851_DV_resource.Stream@PNG-de-DE.png) | Import | Imports parameter sets from a "*.tsv" file. |
| ![Toolbar](images/110183503627_DV_resource.Stream@PNG-de-DE.png) | Export | Exports parameter sets to a "*.tsv" file. |
| ![Toolbar](images/110183512203_DV_resource.Stream@PNG-de-DE.png) | Cancel | Cancels the process. |
| ![Toolbar](images/154713266059_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes the selected parameter set. |

> **Note**
>
> A "*.tsv" file is a text file that uses the tabulator as a list separator.

---

**See also**

[Configuring the parameter set view (RT Unified)](Configuring%20parameter%20sets%20%28RT%20Unified%29.md#configuring-the-parameter-set-view-rt-unified)
  
[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

#### System diagnostics control (RT Unified)

##### Use

You can use the "System diagnostics control" object to display the diagnostic status of several PLCs using traffic light SVGs. The diagnostic status contains the overall status of all relevant PLCs. The merged state is always the worst state of all PLCs.

![Use](images/164243214987_DV_resource.Stream@PNG-en-US.png)

The object supports the S7-1500 as of firmware version 2.0. The prerequisite is that the "Central alarm management in the PLC" setting is enabled on the PLC.

> **Note**
>
> If you configure the HMI connections to more than 50 PLCs for the object, this can lead to an overload in runtime. As a result, HMI connections can no longer be established.

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Diagnostic view": Defines various properties for the display of system diagnostics, such as the background color and row height.
- "Information bar": Specifies the representation of the information bar.
- "Toolbar": Specifies the buttons of the system diagnostics control.

##### Access protection in runtime

You can configure access protection with the properties "Operator control - allow" and "Authorization" in the Inspector window. A logged-in user having the required authorization can acknowledge and edit the system diagnostics control using the buttons in the system diagnostics control.

##### Defining the properties of the system diagnostics control

To define the properties of the system diagnostics control, follow these steps:

1. Click "Properties > General > Diagnostic view" in the Inspector window.
2. Define the settings for the rows and cells.

   - "Row height": Specifies the height of the rows in the system diagnostics control.
   - "Cells - internal spacing": Defines the internal spacing in the cells.
3. Define the settings for the headers under "Properties > General > Diagnostic view > Header - settings":

   - "Row header": Defines whether each row has a header.
   - "Column header": Specifies the representation of the column header.
4. Define the width and color of the grid lines.
5. Define the use of scroll bars.

##### Setting up column sorting

To set up the column sorting, follow these steps:

1. In the Inspector window, click "Properties > General > Diagnostic view > Columns > [0] Column".
2. Select the sorting direction and sorting order for the individual columns.

##### Configuring reordering of the columns

Configure whether operators can reorder the table columns in runtime using drag-and-drop. More information is available in the section [Configuring reordering of the columns](#configuring-reordering-of-the-columns-rt-unified).

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

##### Setting the time zone

Under Properties > Properties > Miscellaneous > Time zone, you set the desired time zone by entering a decimal value for the time zone.

- "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
- "-1": The local time zone of the device.

You can also set the time zone via a selection list in runtime.

##### Configuring the information bar

The information bar of the system diagnostics control shows the connection status and path.

To configure the information bar, follow these steps:

1. Configure the general properties of the information bar, such as the font and background color, under "Properties > Miscellaneous > Information bar".
2. Configure the display of the information bar elements under "Properties > Miscellaneous > Information bar > Elements".

##### Toolbar

You can define the buttons of the system diagnostics control in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the system diagnostics control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/155631893131_DV_resource.Stream@PNG-de-DE.png) | Home page | Shows the home page. |
| ![Toolbar](images/143094621963_DV_resource.Stream@PNG-de-DE.png) | Reload | Updates the view of the diagnostic event. |
| ![Toolbar](images/132458615563_DV_resource.Stream@PNG-de-DE.png) | First line | Selects the first of the pending diagnostic events. The visible area of the view is moved. |
| ![Toolbar](images/132458689035_DV_resource.Stream@PNG-de-DE.png) | Previous line | Selects the previous diagnostic event, starting from the currently selected diagnostic event. The visible area of the view is moved. |
| ![Toolbar](images/132458681611_DV_resource.Stream@PNG-de-DE.png) | Next line | Selects the next diagnostic event, starting from the currently selected diagnostic event. The visible area of the view is moved. |
| ![Toolbar](images/132458622987_DV_resource.Stream@PNG-de-DE.png) | Last line | Selects the last of the pending diagnostic events. The visible area of the view is moved. |
| ![Toolbar](images/143097143051_DV_resource.Stream@PNG-de-DE.png) | Share view | Enables/disables the detail view. |
| ![Toolbar](images/156264938379_DV_resource.Stream@PNG-de-DE.png) | Previous | Navigates to the previous PLC. |
| ![Toolbar](images/155631901707_DV_resource.Stream@PNG-de-DE.png) | Show diagnostic buffer | Changes from the matrix view to the diagnostic view. The diagnostic view shows the diagnostics buffer of the PLC.   This button is only enabled if a PLC or one of its lower-level modules is shown in the matrix view. |

---

**See also**

[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)
  
[System diagnostics display (RT Unified)](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#system-diagnostics-display-rt-unified)

#### Process control (RT Unified)

##### Use

You use the "Process control" object to display the tag values in a table. You can display current, or logged values in the table. You can configure up to nine value columns. The first column is reserved for the time column.

![Use](images/164244695691_DV_resource.Stream@PNG-en-US.png)

The "Process control" object is supported with version V19 exclusively for Unified PC.

If you use the object under Unified Comfort Panel, an error message of the compiler is returned. If you have configured the control for Unified Comfort Panel, delete the control before compiling.

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Column": Defines the setting of the value column.
- "Data source": Specifies the source for representing the values.
- "Toolbar": Specifies the buttons for the process control.

##### Configuring columns

To configure the columns, follow these steps:

1. Open the settings of the time column under "Properties > Miscellaneous > Process control > Columns > Time range column [0]".
2. Under "Properties > Miscellaneous > Process control > Columns > [0] Time range column > Time range", select the time range of the table:

   - "Time interval": You define the time range using a starting time and a following time interval.
   - "Start time and end time": You define the time range using a starting time and an end time.
   - "Measuring points": You define the time range using a starting time and a number of measuring points.
3. Open the settings of the respective value column under "Properties > Miscellaneous > Process control > Columns > [1] Column".
4. Under "Sort order", define the order in which the columns of the process control are shown.
5. Set the direction in which the values are sorted under "Sorting direction - default".
6. Define whether operators can re-arrange the table columns in runtime using drag-and-drop. More information is available in the section [Configuring reordering of the columns](#configuring-reordering-of-the-columns-rt-unified).

##### Defining the data source for displaying the values

To define the display of the values in the process control, follow these steps:

Under "Properties > Miscellaneous > Process control > Columns > [1] Column > Data source > Source", select:

1. Type of data source:

   - HMI tag
   - Logging tag
2. Tag that supplies the column with values.

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

##### Setting the time zone

Under Properties > Properties > Miscellaneous > Time zone, you set the desired time zone by entering a decimal value for the time zone.

- "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
- "-1": The local time zone of the device.

You can also set the time zone via a selection list in runtime.

##### Toolbar

You can define the buttons of the process control in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the process control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/100727706251_DV_resource.Stream@PNG-de-DE.png) | First record | Shows the tag values starting with the first logged value. |
| ![Toolbar](images/100727713931_DV_resource.Stream@PNG-de-DE.png) | Previous record | Shows the tag values in the previous time interval. |
| ![Toolbar](images/100727802635_DV_resource.Stream@PNG-de-DE.png) | Start/Stop | Stops and starts the column update. The values are buffered and updated as soon as you start column update again. |
| ![Toolbar](images/100727721611_DV_resource.Stream@PNG-de-DE.png) | Next record | Shows the values of the tag in the next time interval. |
| ![Toolbar](images/100727729291_DV_resource.Stream@PNG-de-DE.png) | Last record | Shows the tag values up to the last logged value. |
| ![Toolbar](images/100731189259_DV_resource.Stream@PNG-de-DE.png) | Edit | Allows the editing of data in any table field that is opened when the user double-clicks it. |
| ![Toolbar](images/100731164299_DV_resource.Stream@PNG-de-DE.png) | Previous column | Displays the previous column in the foreground |
| ![Toolbar](images/100731172619_DV_resource.Stream@PNG-de-DE.png) | Next column | Displays the next column in the foreground |
| ![Toolbar](images/100727779595_DV_resource.Stream@PNG-de-DE.png) | Select time range | Opens the dialog for setting the time range displayed in the process control. |
| ![Toolbar](images/100727760011_DV_resource.Stream@PNG-de-DE.png) | Select data connection | Opens the dialog for selecting the archives and tags that serve as data the source for this process control. |
| ![Toolbar](images/104597553419_DV_resource.Stream@PNG-de-DE.png) | Create archive value | Creates an archived value. |
| ![Toolbar](images/155629076747_DV_resource.Stream@PNG-de-DE.png) | Export | Starts the export of all or the selected runtime data to a "csv" file. |

---

**See also**

[Configuring the process control (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#configuring-the-process-control-rt-unified)
  
[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

#### Web control (RT Unified)

##### Use

You use the "Web control" object to display basic HTML pages and documents in PDF format.

You have access to the data of the local user management in runtime via a "Browser".

![Use](images/130561358347_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "URL": Specifies which Internet address is opened in the HTML Browser.
- "Toolbar": Specifies the buttons of the browser.

##### Defining the URL

The "browser" object supports the following protocols:

- On a Unified Basic Panel and Unified Comfort Panel:

  - https://
  - http://
  - file://
- On a Unified PC:

  - https://

To define the URL, follow these steps:

Define the Internet address in the Inspector window under "Properties > Properties > URL".

> **Note**
>
> Please note that the "http://" and "file://" protocols do not function in the simulation.

##### Displaying HTML pages

Please note the following when using the object:

- The "Web control" object only displays content that is supported by the web browser in which runtime is open.
- The object is implemented as an iFrame. Pages with X-frame option settings that prevent the display in an iFrame are not displayed in the object.

##### Limitations

The "Web control" object has a limited range of functions compared to a standard browser:

- Navigation from the "Web control" object is not supported (top-level navigation).
- Calls of queries and dialogs (popups and modal dialogs) are only supported if they were activated in the file <Path for the WinCC Unified installation directory>WinCCUnified\WebRH\public\content\custom\CustomSettings.json:

  `{"CustomSettings": {"HmiWebControl" : {"AllowPopups" : true,"AllowModals" : true}}}`

  > **Note**
  >
  > Popups and modal dialogs stop the update.

##### Displaying PDF files in the "Browser" on a Unified PC

The "Browser" object displays PDF files that are available:

- Locally on the HMI device
- On the Internet

You can view a PDF file in the following ways:

- Copy the PDF files to the directory "C:\Program Files\Siemens\Automation\WinCCUnified\WebRH\public".

  Under "Properties > URL", enter the address "https://localhost/WebRH/<pdfname.pdf>".

  > **Note**
  >
  > You cannot display any PDF files that are saved locally in a different directory on your PC.

  You can also use the IP address or the PC name instead of "localhost".

  If you operate runtime on a different PC than the TIA Portal, also save the PDF files on the runtime PC.
- Enter a valid Internet address under "Properties > Properties > URL".

##### Influencing how the document is displayed on a Unified PC

The "Browser" object supports a large number of default parameters with which you can influence how a PDF file is displayed.

Examples of parameters when opening the PDF file:

- Jump to specific page: https://winccunified/WebRH/UCPManual.pdf#page=18
- Jump to table of contents: https://winccunified/WebRH/UCPManual.pdf#lnhaltsverzeichnis
- Zoom in on page: https://winccunified/WebRH/UCPManual.pdf#zoom=200

##### Displaying PDF files in the "Browser" on a Unified Comfort Panel

The "Browser" object displays PDF files that are available:

- Locally on the HMI device

  On a Unified Comfort Panel, the download directory of the browser is: "/home/industrial/download".
- On an external storage medium

You can view a PDF file in the following ways:

- Enter path and file name in the URL input field of the "Browser" operating object.
- In the configuration of the "Browser" operating object under "Properties", link the URL with a tag of the type WString which contains path and file name.

Syntax: file:///<path>/<filename>.pdf

Pay attention to uppercase/lowercase spelling.

Examples:

- Open file from the data memory card: file:///media/simatic/X51/UCPManual.pdf
- Open locally saved file: file:///home/industrial/UCPManual.pdf

##### Influencing how the document is displayed on a Unified Comfort Panel

The "Browser" object supports a large number of default parameters with which you can influence how a PDF file is displayed.

Examples of parameters when opening the PDF file:

- Open file on page 20: file:///media/simatic/X51/UCPManual.pdf?20#page=20
- Open file with zoom factor 150%: file:///media/simatic/X51/UCPManual.pdf?150#zoom=150
- Open file on page 20 with zoom factor 150%: file:///media/simatic/X51/UCPManual.pdf?(20,150)#page=20&zoom=150

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

##### Toolbar

You can define the buttons of the browser in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". The buttons are enabled by default.

The following buttons are available for the process control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/160829719819_DV_resource.Stream@PNG-de-DE.png) | Home page | Shows the home page. |
| ![Toolbar](images/160830944395_DV_resource.Stream@PNG-de-DE.png) | Reload | Refreshes the view of the browser. |
| ![Toolbar](images/160829711243_DV_resource.Stream@PNG-de-DE.png) | Address | Shows the Internet address that opens in the browser. |

---

**See also**

[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

#### Media Player (RT Unified)

##### Use

You use the "Media Player" object in Runtime to play multimedia files.

![Use](images/143133719563_DV_resource.Stream@PNG-de-DE.png)

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "URL": Specifies the file to be played in the Media Player.
- "Toolbar": Specifies the buttons of the Media Player.

##### Supported file formats

All file formats that are supported by the browser used are also supported in the Media Player.

Playing back multimedia files in the object depends on the video and audio codecs installed on the PC, as well as on the file format.

> **Note**
>
> The playback of .mp4 and .mkv files using the "Media Player" control may result in a loss in performance. Use the .ogv or .webm formats instead.

If you copy the project to another PC, keep in mind: If the files are linked dynamically and not specified with the UNC path, the files specified in Media Player are not included in the copy. You have to load the files into the project again.

##### Accessing a file on a Unified PC in Runtime

On a Unified PC Runtime, you can access the files in Runtime that you have stored in the public directory of the WinCC Unified installation.

To access a file, follow these steps:

1. Store the file in the Public directory of the WinCC Unified installation, e.g. "C:\Program Files\Siemens\Automation\WinCCUnified\WebRH\public". You can also create a subdirectory, e.g. "MediaFiles".
2. Open the properties of the Media Player in your TIA Portal project.
3. Click "Properties > General > URL" in the Inspector window. Enter the URL.

   You can structure a valid URL according to the following scheme: "https://<ComputerName>.<DomainName>/WebRH/<FileName>".  
   Example: "https://mycomputer.siemens.net/WebRH/Twistlock.mp4".

   If you have created a subdirectory, e.g. "MediaFiles", enter the URL in the following format: "https://mycomputer.siemens.net/WebRH/MediaFiles/Twistlock.mp4".

Alternatively, you can change the address via a script, e.g.:

Screen.FindItem('MediaControl').Url = https://<ComputerName>.<DomainName>/WebRH/<FileName>

##### Accessing a file on a Unified Comfort Panel in Runtime

On a Unified Comfort Panel, you can access files in Runtime that you have stored on an external storage medium, e.g. an SD card or a USB flash drive.

To access a file, follow these steps:

1. Store the file on an external storage medium, e.g. a USB flash drive connected to the X61 interface.
2. Open the properties of the Media Player in your TIA Portal project.
3. Click "Properties > General > URL". Enter the URL.

   You form a valid URL according to the following scheme: "file:///media/simatic/<file location>/<file name>".  
   Example: "file:///media/simatic/X61/content/video.mp4".

   If you have created a subdirectory, e.g. "MediaFiles", enter the URL in the following format: "file:///media/simatic/X61/MediaFiles/content/video.mp4".

Alternatively, you can change the address via a script, e.g.:

Screen.FindItem('MediaControl').Url = file:///<media>/simatic/X61/content/<file name>

##### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Graphic - pressed button
- Icon

##### Toolbar

You can define the buttons of the Media Player in Runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To add more buttons in the display object, activate the "Visibility" property under the settings of the corresponding button.

The following buttons are available for the Media Player:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/156318161675_DV_resource.Stream@PNG-de-DE.png) | Play | Plays the video or audio file. |
| ![Toolbar](images/156330326027_DV_resource.Stream@PNG-de-DE.png) | Pause | Pauses the video or audio file. |
| ![Toolbar](images/156330505355_DV_resource.Stream@PNG-de-DE.png) | Stop | Stops the video or audio file. |
| ![Toolbar](images/156330496779_DV_resource.Stream@PNG-de-DE.png) | Search forward | Searches for the next video or audio file. |
| ![Toolbar](images/156330360203_DV_resource.Stream@PNG-de-DE.png) | Search backward | Searches for the last video or audio file. |
| ![Toolbar](images/156330317451_DV_resource.Stream@PNG-de-DE.png) | Mute | Mutes the video or audio file. |

---

**See also**

[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)
  
[http://support.automation.siemens.com](http://support.automation.siemens.com/WW/view/en/62101921)

#### GRAPH overview

##### Use

The "GRAPH Overview" object is used to display the current program status for executed steps of the GRAPH sequencer. Errors during execution of a program are displayed directly at the corresponding step.

The following information is displayed in the "GRAPH Overview" object:

- Name and status of the function block
- Status of initial and simultaneous steps
- Number and name of the first step currently executed step
- Operating mode for running the GRAPH sequencer

WinCC supports the display of step names for the GRAPH blocks in multiple languages starting from Version 6.0. The step names will then be displayed in the selected Runtime language following a language changeover in Runtime. If the selected language is not available, the names are displayed in the default language (English).

![Use](images/164599456139_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> To view the program status of an GRAPH instance data block in the "GRAPH overview" object, set the block's instance-specific properties to "Visible in HMI" and "Accessible from HMI".

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Process > Tag": Assign the tag.
- "Toolbar": Specifies the buttons of the GRAPH overview.

##### Operating mode

There are four modes of operation available to you for running the GRAPH sequence:

- AUTO (default setting) - Automatically switches to the next step when the transition is fulfilled.
- TAP - Automatically switches to the next step when the transition is fulfilled and there is an edge change from "0" to "1" at the T_PUSH parameter.
- TOP - Automatically switches to the next step when the transition is fulfilled or there is an edge change from "0" to "1" at the T_PUSH parameter.
- MAN - The next step is not automatically enabled when the transition is fulfilled. You can select and deselect the steps manually.

> **Note**
>
> You set the operating mode by modifying the interface parameters of the GRAPH block in your control program.

In WinCC Unified Runtime, you can customize the name for the operating mode that is displayed in the GRAPH overview.

##### Configuring a compact view

You can also configure a slim GRAPH overview without toolbar buttons and operating mode display.

To display a slim GRAPH overview in single-line compatibility mode, drag the control to the desired size.

##### Symbols

The symbols displayed in the GRAPH overview are pre-defined:

| Symbol |  | Function |
| --- | --- | --- |
| ![Symbols](images/81523267723_DV_resource.Stream@PNG-de-DE.png) | Error | Indicates that an error has occurred during the execution of a step. |
| ![Symbols](images/81524872587_DV_resource.Stream@PNG-de-DE.png) | Initial step | Indicates that the currently executing step is the first step in the GRAPH step sequence. |
| ![Symbols](images/81523276555_DV_resource.Stream@PNG-de-DE.png) | Simultaneous step | Shows that there are other simultaneous steps in the GRAPH step sequence in addition to the current one. |

##### Toolbar

You can define the buttons of the GRAPH overview in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". By default, only the "Next Step" button is available. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the GRAPH overview:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/162811779467_DV_resource.Stream@PNG-de-DE.png) | Next Step | Jumps to the next step in parallel step. When you get to the last step, you can jump back to the first step. |
| ![Toolbar](images/162811783435_DV_resource.Stream@PNG-de-DE.png) | Jump to Alarm Control | Opens the configured alarm control with the error message in WinCC Unified.  The button is intended to be populated with appropriate system functions/scripts. |
| ![Toolbar](images/162821541003_DV_resource.Stream@PNG-de-DE.png) | Jump To PLC code view | Opens the configured PLC code view.  The button is intended to be populated with appropriate system functions/scripts.  Ideally, use the "OpenGRAPHViewerFromOverview" system function. |
| ![Toolbar](images/162821544971_DV_resource.Stream@PNG-de-DE.png) | Jump to TIA Portal | Several script functions are available for opening the TIA Portal. |

---

**See also**

[Configuring a GRAPH overview (RT Unified)](Operating%20Unified%20PC%20%28RT%20Unified%29.md#configuring-a-graph-overview-rt-unified)
  
[Process diagnostics (RT Unified)](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#process-diagnostics-rt-unified)

#### PLC code view (RT Unified)

##### Use

The "PLC code view" object is used to display the current program status of user programs that have been programmed in the LAD, FBD or GRAPH graphic programming languages.

A variety of information about the user program is displayed in the PLC code view:

- Information area
- Toolbar
- Detail view
- Transition/Interlock view

![Use](images/162821795211_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Toolbar": Specifies the buttons of the PLC code view control.
- "Toolbar": Shows information about the first or the selected icon.

##### Information area

In the information area of the PLC code view, you are shown:

- In the left area, the GRAPH sequence.
- In the right area, the details, e.g. for the step or for the transition. In the ProDiag view, the networks to the supervised operands are displayed in this area.

##### Buttons of the toolbar

You can define the buttons of the PLC code view control in runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the PLC code view:

| Button |  | Function |
| --- | --- | --- |
| ![Buttons of the toolbar](images/162823707019_DV_resource.Stream@PNG-de-DE.png) | Previous | Navigates to the previous sequence / previous network. |
| ![Buttons of the toolbar](images/162823710987_DV_resource.Stream@PNG-de-DE.png) | Continue | Navigates to the next sequence / next network. |
| ![Buttons of the toolbar](images/162823714955_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlarges the information area. |
| ![Buttons of the toolbar](images/162823757323_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduces the information area. |
| ![Buttons of the toolbar](images/162823761291_DV_resource.Stream@PNG-de-DE.png) | Toggle GRAPH mode | Switches between manual and automatic step selection for the active step. |
| ![Buttons of the toolbar](images/162823765259_DV_resource.Stream@PNG-de-DE.png) | Toggle detail view | 1. GRAPH view: Switches between the transition and interlock networks.  2. ProDiag view: Switches between network and the whole block. |
| ![Buttons of the toolbar](images/162825361163_DV_resource.Stream@PNG-de-DE.png) | Toggle criteria analysis | Switches between the network view including criteria analysis and the standard network display without criteria analysis. |

---

**See also**

[Configuring the PLC code view](Operating%20Unified%20PC%20%28RT%20Unified%29.md#configuring-the-plc-code-view)
  
[Process diagnostics (RT Unified)](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#process-diagnostics-rt-unified)

#### ProDiag overview

##### Use

The "ProDiag overview" object provides an overview of the current status of the configured monitoring in Runtime.

When an error occurs, the type of error and the error category are determined in the ProDiag overview. You can navigate directly to the alarm control to find the error and you can jump from the corresponding alarm to the PLC code viewer control. You can display the affected program code in the PLC code viewer control.

![Use](images/164456222219_DV_resource.Stream@PNG-en-US.png)

The "ProDiag overview" object is available for WinCC Unified.

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Displayed buttons
- Names and colors for categories
- Names and colors for monitoring types

##### Monitoring types and categories

You can display a maximum of 8 categories and 6 monitoring types in the "ProDiag overview" object. The following pre-defined categories and monitoring types are available:

| Designation | Categories |
| --- | --- |
| E (Error) | Error |
| W (Warning) | Warning |
| I (Info) | Information |
| C4 ... C8 | Additional categories |

Rename the categories C4 to C8, which are created by default, according to your requirements.

| Designation | Monitoring type |
| --- | --- |
| O (Operand) | Operand error |
| I (Interlock) | Interlock error |
| R (Reaction) | Reaction error |
| A (Action) | Action error |
| P (Position) | Position error |
| M (Message error) | Alarm |

You can change display symbols of the supervision types and categories at any time in the Inspector window under "Miscellaneous".

##### Symbols

The icons displayed in the ProDiag overview are fixed.

| Icon | Name | Function |
| --- | --- | --- |
| ![Symbols](images/80801398795_DV_resource.Stream@PNG-de-DE.png) | Error | Indicates that an error has occurred. |

##### "Jump to Alarm Control" button

The "Jump to Alarm Control" button in the ProDiag overview is activated by default.

| Button | Name | Function |
| --- | --- | --- |
| !["Jump to Alarm Control" button](images/164643614091_DV_resource.Stream@PNG-de-DE.png) | Jump to Alarm Control | Opens the configured alarm control with the error message after system functions or scripts have been assigned to the button. |

##### Deactivated display

If there is a faulty connection to the controller during runtime, the object "ProDiag overview" is displayed grayed-out (unavailable). This deactivated display can be due to the following:

- The controller is deactivated
- The configured ProDiag program block was removed from the control program
- The controller is in Stop mode

As soon as the cause of the error is removed and the connection reestablished, the ProDiag overview shows the current online status of the monitoring during runtime.

---

**See also**

[Configuring the ProDiag overview](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#configuring-the-prodiag-overview)
  
[Process diagnostics (RT Unified)](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#process-diagnostics-rt-unified)

### My Controls (RT Unified)

This section contains information on the following topics:

- [Using custom web controls (RT Unified)](#using-custom-web-controls-rt-unified)
- [Updating Custom Web Controls (RT Unified)](#updating-custom-web-controls-rt-unified)
- [My Controls - Overview (RT Unified)](#my-controls---overview-rt-unified)

#### Using custom web controls (RT Unified)

##### Introduction

You can use custom web controls in WinCC.

For custom web controls to be displayed in the TIA Portal, store the custom web controls in the folder <project_folder>/UserFiles/CustomControls.

##### Requirement

- A project has been created.
- A Unified device has been created.
- A screen is open.

##### Using custom web controls

Custom web controls are stored in the TIA Portal in "Tools > My Controls".

If you want to use a custom web control, follow these steps:

1. Insert the custom web control into the open screen by dragging-and-dropping the control from the "My Controls" palette to the screen.
2. Specify the properties of the custom web control in the Inspector window.
3. Configure the events for the custom web control.

##### Using custom web controls as a master copy

When you add the custom web control as a master copy to the project library, the control is changed.

You update the copied custom web control by clicking on the "Update" icon.

##### Uniform display of custom web controls

To make the display of a Custom Web Control independent of the browser you are using, use a style sheet when programming the Custom Web Control.

##### Managing properties and events

You can change the properties and create or delete events without having to open the project again or restart TIA Portal.

You have the following two options for managing the properties and events:

- Extract the manifest file from the .zip file, make the changes, and save the manifest file back to the .zip file.
- Create a separate .zip file with the changed manifest file and overwrite the .zip file in the CustomControls folder.

#### Updating Custom Web Controls (RT Unified)

##### Introduction

After changing the properties for custom web controls or configuring new events, you can update custom web controls.

##### Updating custom web controls

If you have changed the properties for custom web controls or configured new events, you can update the custom web controls as follows:

1. Click the Update icon ![Updating custom web controls](images/137628691979_DV_resource.Stream@PNG-de-DE.png) in the "My Controls" palette.
2. Custom web controls are updated.
3. A message appears in the Inspector window:

   - "The object '{0}' was updated successfully".
   - "The object '{0}' was updated successfully, but some properties have been lost due to incompatible changes to the interface."
   - "All objects are up to date". You have not changed any properties or alarms.
   > **Note**
   >
   > The placeholder '{0}' stands for a unique and complete path on which the custom web control is stored.

##### Restrictions for the update

If you have opened a project as read-only, the update is not possible.

The following changes to the custom web control prevent the automatic update:

- Renaming properties or events
- Deleting properties or events
- Changing the data type

#### My Controls - Overview (RT Unified)

This section contains information on the following topics:

- [Audit Viewer (RT Unified)](#audit-viewer-rt-unified)
- [Plant overview (RT Unified)](#plant-overview-rt-unified)
- [Reports (RT Unified)](#reports-rt-unified)

##### Audit Viewer (RT Unified)

###### Use

You use the "Audit Viewer" object to evaluate in table form all data of the audit trail in Runtime.

![Use](images/164250608139_DV_resource.Stream@PNG-de-DE.png)

###### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object. You can adjust the following properties in particular:

- "Text": Defines the text for the heading of the Audit Viewer.
- "Window settings": Defines the settings for display in Runtime.

###### Text

To define a text for the heading of the Audit Viewer, follow these steps:

1. Activate the "Show heading" option in the Inspector window under "Properties > Appearance > Window settings". The option is activated by default.
2. Click "Properties > Miscellaneous > Label > Font" in the Inspector window.
3. Select a font.
4. Click "Properties > Miscellaneous > Label > Text" in the Inspector window.
5. Enter a text.

###### Resizing in Runtime

To resize the Audit Viewer in Runtime, follow these steps:

1. Activate the options "Show border" and "Can be sized" in the Inspector window under "Properties > Appearance > Window settings". The options are activated by default.

   The width of the border is not evaluated.

###### Dynamization of graphic properties with tags or scripts

You can dynamize the following property containing a graphic with a tag or with a script:

- Icon

##### Plant overview (RT Unified)

###### Use

You use the "Plant overview" object to display the configured plant view in runtime. In the plant overview, you can navigate through the system to the plant objects and see your plant at a glance.

If you have configured screens or alarms for the lower-level plant objects and have linked them to the "Plant overview" object, navigate to these screens and alarms and display them.

![Use](images/156012252043_DV_resource.Stream@PNG-de-DE.png)

With version V19, the "Plant overview" control is supported only for Unified PC.

If you use the control under Unified Comfort Panel, an error message of the compiler is returned. If you have configured the control for Unified Comfort Panel, delete the control before compiling.

###### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object.

To enable navigation between the screens of the plant objects, configure the companion controls under "Properties > Miscellaneous > Interface > Companion controls".

###### Buttons

The following buttons are available for the "Plant overview" object in runtime:

| Button | Name | Function |
| --- | --- | --- |
| ![Buttons](images/110901057035_DV_resource.Stream@PNG-de-DE.png) | Expand | Expands the plant view with the lower-level plant objects. |
| ![Buttons](images/110902806667_DV_resource.Stream@PNG-de-DE.png) | Collapse | Collapses the plant view with the lower-level plant objects. |
| ![Buttons](images/156012260491_DV_resource.Stream@PNG-de-DE.png) | Filter | Defines which plant objects are displayed. |

##### Reports (RT Unified)

###### Use

You use the "Reports" object to create and manage report tasks in runtime. You have access to the reports generated by the report jobs.

![Use](images/156016290699_DV_resource.Stream@PNG-en-US.png)

You can find detailed information on configuring the object in the engineering system in the section [Configuring production reports in the engineering system](Creating%20production%20reports%20%28RT%20Unified%29.md#configuring-production-reports-in-the-engineering-system-rt-unified).

You can find detailed information on configuring report tasks in runtime in the section [Working with production reports in Runtime](Creating%20production%20reports%20%28RT%20Unified%29.md#working-with-production-reports-in-runtime-rt-unified).

###### Layout

In the Inspector window, you can customize the settings for the position, geometry, style, and color of the object.

---

**See also**

[Basics of Reporting (RT Unified)](Creating%20production%20reports%20%28RT%20Unified%29.md#basics-of-reporting-rt-unified)
  
[The user interface of the "Reports" control (RT Unified)](Creating%20production%20reports%20%28RT%20Unified%29.md#the-user-interface-of-the-reports-control-rt-unified)

### Graphics (RT Unified)

This section contains information on the following topics:

- [Graphics (RT Unified)](#graphics-rt-unified-1)
- [External graphics (RT Unified)](#external-graphics-rt-unified)
- [Managing external graphics (RT Unified)](#managing-external-graphics-rt-unified)
- [Managing SVG graphics (RT Unified)](#managing-svg-graphics-rt-unified)
- [Restrictions on SVG graphics (RT Unified)](#restrictions-on-svg-graphics-rt-unified)

#### Graphics (RT Unified)

##### Introduction

An extensive collection of graphics, icons and symbols is installed with WinCC.

In the Toolbox window of the "Graphic" pane the graphic objects are structured by topic in the "WinCC graphics folder." You cannot remove, edit or rename the link to the WinCC graphics folder.

![Introduction](images/162092694539_DV_resource.Stream@PNG-en-US.png)

##### Storing graphics in the project graphics

The project graphics can be found in the project tree under "Project > Languages & Resources > Project graphics".

![Storing graphics in the project graphics](images/162102390283_DV_resource.Stream@PNG-en-US.png)

You can save graphics in the project graphics:

- Graphic objects from the Tools > Graphics palette:

  When you drag-and-drop the graphics objects from the "Graphics" pane into the work area, these are stored automatically in the project graphics.

  The graphic names are numbered in the order of their creation, for example, "Graphic_1." Use the <F2> function key to rename the graphic.
- Graphic file with the following formats:

  *.bmp, *.ico, *.emf, *.wmf, *.gif, *.tiff, *.png, *.svg, *.jpeg or *.jpg
- OLE objects that are linked to an external graphics program and are embedded in WinCC.

  In the case of an OLE link, you open the external graphic editor from WinCC. The linked object is edited using the graphic editor. An OLE link only works if the external graphic editor is installed on your PC, and supports OLE.

> **Note**
>
> High-resolution graphic objects require a lot of memory in the project and cause long loading times. They also reduce performance in Runtime.
>
> Use graphic objects with a resolution that is sufficient for a high-quality display in the Runtime project. Note the display resolution of the target device and the size in which the graphic object is displayed on the display of the target device. Adapt the resolution of large graphic objects accordingly before using them in your project.

##### Using graphics from the project graphics

Graphics from the project graphics are used in your screens:

- In a graphic view
- In a graphic list
- As labeling for a button

To use a graphic in the screen or in the screen object, drag the desired graphic to the screen or the screen object. Alternatively, select the graphic from the selection list in the "Graphic" property in the Inspector window.

##### Using graphics with transparent background

In WinCC, you also use graphics with a transparent background. When a graphic with a transparent background is inserted into a graphic object of WinCC, the transparency is replaced by the background color specified for the graphic object. The selected background color is linked firmly to the graphic.

If you use the graphic in another graphic object of WinCC, this object is displayed with the same background color as the graphic object that was configured first.

If you want to use the graphic with different background colors, include this graphic in the project graphics again under a different name. The additional background color is configured when the graphic is used at the corresponding graphic object of WinCC.

#### External graphics (RT Unified)

##### Introduction

You can use graphics created with an external graphic program in WinCC. To use these graphics you store them in the project graphics of the WinCC project.

##### Managing external graphics

Use the "Toolbox" task card in the "Graphics" palette to manage your external graphics. The following possibilities are available:

- Creating links to graphics folders.

  The external graphics in this folder, and in the subfolders, are displayed in the toolbox and are thus integrated in the project.
- Editing folder links.
- You open the program required for editing of the external graphic in WinCC.

#### Managing external graphics (RT Unified)

##### Introduction

External graphics that you want to use in WinCC are managed in the "Screens" editor by using the "Tools" task card in the "Graphics" pane.

##### Requirement

- The "Screens" editor is open.
- The "Toolbox" task card is open.
- The graphics are available.
- The graphics have the following formats:

  *.bmp, *.ico, *.emf, *.wmf, *.gif, *.tiff, *.svg, *.jpeg, *.jpg

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
2. Select "Open folder" from the shortcut menu.

   The Windows Explorer opens.

#### Managing SVG graphics (RT Unified)

##### Introduction

You can import SVG graphics into the TIA Portal for visualization. You can adapt the source file for the SVG graphics so that the SVG graphics are displayed correctly in the TIA Portal.

##### Requirement

- A project has been created.
- A Unified device has been created.
- A screen is open.

##### Importing SVG graphics

To import an SVG graphic into the TIA Portal, follow these steps:

1. In the project tree, under "Languages & Resources", click on "Project graphics".
2. Use drag-and-drop to add an SVG graphic from your storage location into the project graphics.
3. In the "Default graphic" column, click the added graphic.
4. Information about the SVG graphic is displayed in the Inspector window under "General > Properties".

##### Displaying SVG conversion information

You can find the "Show SVG conversion information" button in the Inspector window, under "Properties > General" in the "Standard graphic" area.

To display the SVG conversion information, follow these steps:

1. Click on the button.
2. An "SVG conversion information" dialog with 2 scrollable read-only text boxes opens:

   - "SVG content": The content of the SVG image file is imported into the TIA Portal as a result of the conversion.
   - "SVG conversion protocol": Messages about the changes during conversion.

     During the import of SVG files into the TIA Portal, the contents that are not supported by WinCC Unified and HMI systems are removed.

You can select and copy the text in the dialog.

##### "SVG conversion information" dialog

The "SVG conversion information" dialog contains:

- Messages created during the import of the SVG file.
- Information on the content that was removed during conversion.

Depending on the exact content of the original SVG file, checking and conversion may be carried out in multiple test cycles. The protocol segments of the test cycles are separated by a hyphenated separator line ("-----"). The row number of the original SVG file is only specified for the first conversion test cycle.

The conversion protocol is created and provided in English, regardless of the current user interface language or runtime language settings in the project.

##### Editing SVG graphics

To edit an SVG graphic, follow these steps:

1. In the project graphics, right-click the graphic in the "Default graphic" column.

   The shortcut menu opens.
2. Click "Edit".

   An external editor for editing the graphics opens.

You can now edit the SVG graphic.

#### Restrictions on SVG graphics (RT Unified)

##### Introduction

The SVG graphics support the SVG 1.2 Tiny standard. Note the following restrictions when using SVG graphics:

##### Restrictions on SVG graphics

- The use of SVG graphics that include the elements or commands according to the SVG 2.0 standard can lead to unexpected behavior.
- The CSS definitions are converted to inline attributes.
- Embedded scripts and non-local URLs are not supported in the SVG graphics and are removed from the original graphics during conversion when imported into the TIA Portal.
- The use of SVG graphics with embedded animations is not supported.
- The file names of SVG graphics must not include German umlauts or Chinese characters.
- The use of large SVG graphics affects performance due to the load associated with the increased characters.
- Migration of SVG graphics from WinCC V7 to TIA Portal is not supported.
- The following SVG characteristics are not supported:

  - Scripting
  - Interactivity
  - Styling
  - Expandability - no ForeignObjects
  - Animations
- Screen objects using an SVG graphic that was scaled in the Engineering System as a background graphic are not displayed correctly in Runtime in Chrome.
- SVG graphics for which the "Scale background graphic" property in engineering in faceplates is set to "Stretch to fit" are not displayed correctly in Runtime in Chrome.

  Convert such a graphic into a bitmap to use it in engineering. Or, for Runtime, select a web browser other than the web client, such as Firefox.
- If the "Scale background graphic" property is configured with the value "None" for screen objects, set the following SVG attributes to display SVG graphics:

  - Width: Pixel or percent
  - Height: Pixel or percent

  Specifications for width and height are recommended in pixels. If the width and height are not set, the pixel values entered in the SVG attribute "viewbox" are used. This does not apply to Firefox.
- Scaled SVG graphics in Chrome: Elements using an SVG graphic that was scaled in the engineering system as background graphic are not displayed correctly in Chrome in Runtime.
- In an SVG graphic, the vertices of a polyline must be defined directly, e.g. <polyline points="100,100 150,25 150,75 200,0">.
- In an SVG graphic, the range <defs>...</defs> must be located directly at the beginning of the SVG code.
- An SVG graphic can be imported only if it contains the <hmi:self> XML element.

### Dynamic widgets (RT Unified)

This section contains information on the following topics:

- [Managing dynamic SVG graphics (RT Unified)](#managing-dynamic-svg-graphics-rt-unified)
- [Updating dynamic SVG graphics (RT Unified)](#updating-dynamic-svg-graphics-rt-unified)
- [Using dynamic SVG graphics as a master copy (RT Unified)](#using-dynamic-svg-graphics-as-a-master-copy-rt-unified)

#### Managing dynamic SVG graphics (RT Unified)

##### Introduction

You can use dynamic SVG graphics in WinCC. For SVG graphics to be displayed in the TIA Portal, store the graphics in the folder <project_folder>/UserFiles/SVGControls.

##### Requirement

- A project has been created.
- A Unified device has been created.
- A screen is open.

##### Managing dynamic SVG graphics

The dynamic SVG graphics are stored in the TIA Portal in "Tools > Dynamic widgets > Project graphics".

To manage a dynamic SVG graphic, follow these steps:

1. Insert a dynamic SVG graphic into the open screen by dragging the graphic from the "Project graphics" folder to the screen.
2. Specify the properties of the SVG graphic in the Inspector window.
3. Configure the events for the SVG graphic.

You can change the properties and create or delete events without having to open the project again or restart TIA Portal.

##### Editing dynamic SVG graphics in the external editor

It is not possible to open dynamic SVG graphics in an external editor using the "Edit" command.

#### Updating dynamic SVG graphics (RT Unified)

##### Introduction

If you have changed the properties of the dynamic SVG graphic or configured new events, update the dynamic SVG graphic as follows:

##### Requirement

- A project has been created.
- A Unified device has been created.
- A screen is open.

##### Updating dynamic SVG graphics

To update the dynamic SVG graphic, follow these steps:

1. In the "Dynamic widgets" palette, click the update icon ![Updating dynamic SVG graphics](images/137628691979_DV_resource.Stream@PNG-de-DE.png).
2. The dynamic SVG graphics are updated.
3. A message appears in the Inspector window:

   - "The object '{0}' was updated successfully".
   - "The object '{0}' was updated successfully, but some properties have been lost due to incompatible changes to the interface."
   - "All objects are up to date". You have not changed any properties or alarms.
   > **Note**
   >
   > The placeholder '{0}' stands for a unique and complete path on which the SVG graphic is stored.

##### Restrictions for the update

If you have opened a project as read-only, the update is not possible.

The following changes to the dynamic SVG graphic prevent the automatic update:

- Renaming properties or events.
- Deleting properties or events.
- Changing the data type.

#### Using dynamic SVG graphics as a master copy (RT Unified)

##### Introduction

You can add a dynamic SVG graphic as a master copy to the project library.

##### Requirement

- A project has been created.
- A Unified device has been created.
- A screen is open.

##### Using dynamic SVG graphic as a master copy

When you add a dynamic SVG graphic as a master copy to the project library, the dynamic SVG graphic is changed.

You update the copied dynamic SVG graphic by clicking on the "Update" icon.

## Configuring screen objects (RT Unified)

This section contains information on the following topics:

- [Select multiple objects (RT Unified)](#select-multiple-objects-rt-unified)
- [Copying objects (RT Unified)](#copying-objects-rt-unified)
- [Creating objects automatically (RT Unified)](#creating-objects-automatically-rt-unified)
- [Defining the output format (RT Unified)](#defining-the-output-format-rt-unified)
- [Disable remote control (RT Unified)](#disable-remote-control-rt-unified)
- [Hotkeys (RT Unified)](#hotkeys-rt-unified)
- [Configuring object properties (RT Unified)](#configuring-object-properties-rt-unified)
- [Designing objects (RT Unified)](#designing-objects-rt-unified)
- [Moving objects (RT Unified)](#moving-objects-rt-unified)
- [Designing colors (RT Unified)](#designing-colors-rt-unified)
- [Formatting text in the object (RT Unified)](#formatting-text-in-the-object-rt-unified)
- [Linking objects (RT Unified)](#linking-objects-rt-unified)
- [Using layers (RT Unified)](#using-layers-rt-unified)
- [Two-hand operation of operator controls (RT Unified)](#two-hand-operation-of-operator-controls-rt-unified)

### Select multiple objects (RT Unified)

#### Introduction

To manage multiple objects at once, select all the objects in question. This procedure is called "multiple selection." The Inspector window shows all the properties of the selected objects.

With a multiple selection, you have the following options:

- Move or rotate all objects together.
- Resize all objects by the same factor by using the mouse to drag the object-enclosing rectangle on the reference object accordingly larger or smaller.
- Align the objects to the reference object.
- Change object properties.

You have the following options to select multiple objects:

- Draw a selection border around the objects.
- Hold down the <Shift> key, and click the required objects.

#### Selection border of a multiple selection

The selection border surrounds all objects of a multiple selection. The selection border is comparable with the bounding box that surrounds an object.

The selection border is only visible as long as it is pulled up with the mouse button pressed. When you have made your multiple selection, the following border is displayed:

- The reference object is indicated by the bounding box.
- The other selected objects are indicated by a border. The color of the border depends on the background color of the screen.

The color of the selection border is adapted to the background color of the screen in such a way that the selection border is correctly displayed and visible with multiple selection.

#### Specifying a reference object

The reference object is the object upon which the other objects are oriented. The reference object is framed by a bounding box with handles. The following figure shows a reference object with three additional selected objects:

![Specifying a reference object](images/100725896075_DV_resource.Stream@PNG-de-DE.png)

You have the following options to specify the reference object:

- Select the objects using multiple selection. The object selected first is then the reference object.
- Draw a selection border around the objects. As a reference object, the object is automatically defined as on top in the foreground. If you wish to specify a different object within the selection as the reference object, click on the desired object. This action does not cancel your multiple selection.

#### Requirement

- The HMI screen is open with at least two objects.

#### Selecting multiple objects with a selection border

To select multiple objects using a selection border, follow these steps:

1. Position the mouse pointer in the work area close to one of the objects to be selected.
2. Hold down the mouse button, and draw a selection border around the objects to be selected.

#### Selecting multiple objects using the <Shift> key

To select multiple objects with the <Shift> key, follow these steps:

1. Hold down the <Shift> key.
2. Click the relevant objects, working in succession.

   All the selected objects are identified by borders.

   The object selected first is identified as reference object.

**Note**

To remove an object from the multiple selection, press <Shift>, hold it down and then click the relevant object once again.

#### Result

Multiple objects are selected. An object is identified as the reference object.

### Copying objects (RT Unified)

#### Introduction

You can copy objects individually or with a multiple selection.

#### Requirement

- The HMI screen is open with at least one object.

#### Copying objects

To copy an object, follow these steps:

1. Select the object.
2. Copy the object with <Ctrl + C> or select "Copy" in the shortcut menu.
3. Paste the object with <Ctrl + V> or select "Paste" in the shortcut menu.
4. Drag and drop the copied object to the required position.

If you want to copy multiple objects using multiple selection, draw a selection frame around the desired objects and proceed as described above.

#### Using copied objects with the same spacing

If you want to use the copied object multiple times, proceed as described above. Press <Ctrl + V> or select "Paste" repeatedly to automatically paste the objects in the HMI screen with equal spacing.

The same principle also applies to multiple selection of the objects.

### Creating objects automatically (RT Unified)

#### Introduction

You can automatically create the objects by dragging a screen, a graphic, a graphic list, a text list or a tag into an HMI screen.

#### Requirement

- The HMI screen is open.

#### Creating objects automatically

You can create the following objects automatically:

- Button: Drag an HMI screen from the project tree to another screen.
- Graphic view:

  - Drag a graphic from the detail view of the project graphics into the screen.
  - Drag a graphic list from the detail view of the text and graphic lists into the screen.
- Text box: Drag a text list from the detail view of the text and graphic lists into the screen.
- IO field: Drag a tag from the detail view of the tag table into the screen.

### Defining the output format (RT Unified)

#### Introduction

In many objects you can adjust the output format for the displayed values or define it yourself. You can process and output the process value that is displayed in the object in different notations.  
You can select frequently used output formats directly in the user interface. You can adjust the formatting codes or define them yourself.  
You can define the output of a screen object in "Properties > General > Output format" for the following data:

- Floating-point numbers
- Binary
- Hexadecimal
- Decimal
- Text
- Duration, date, time
- Percent, currency, unit
- Numerical values

The definition of the output format is based on UNICODE CLDR. You can find additional information on the CLDR project and on the definitions on the Internet at <http://cldr.unicode.org/>

#### Requirement

- The HMI screen is open with at least one object.

#### Defining the output format

You can define the output format by stringing together formatting codes. The formatting codes act as placeholders for a specific group of characters. If, for example, a formatting code that only allows the display of the digits 0-9 is specified for a position in the display of the IO field, you cannot input letters at this position.

The definitions for the output format are independent of the language. The output format can be language-specific and thus take linguistic differences into account, for example, for output of the date.

You can define and combine different format patterns yourself.

| Symbol | Meaning |
| --- | --- |
| ![Defining the output format](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| - Select the output format from the drop-down list or edit it manually in the input window. You can also customize the combined output formats, for example, change the output format "{D} {T}" manually to "{D,long} {T}". |  |

The tables below show examples for the definition of output formats that are frequently used.

#### "Binary" data format

You use the "Binary" data format to display binary values. The "Binary" data format has the following inputs:

- Sign "B"
- Number of digits (optional)
- Information on forming blocks (optional)

| Output format example | Mindigits | Block size | Tag value | Result |
| --- | --- | --- | --- | --- |
| {B} | Default | - | 16 | 1 0000 |
| {B8} | 8 | - | 16 | 0001 0000 |
| {B8} | 8 | - | 80 | 0101 0000 |
| {B8,4} | 8 | 4 | 80 | 0101 0000 |
| {B,2} | Default | 2 | 80 | 1 01 00 00 |
| {B} | Default | - | -1 | 1111 1111 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Mindigits | Number of digits (optional) | Minimum: 1 | Maximum: 64 | Default value: 1 |
| Block size | Number of digits in front of the separator (optional) | Minimum: 0 (none) | Maximum: 8 | Default value: 4 |

> **Note**
>
> The "Binary" data format does not support any negative values in Unified Runtime.
>
> If you wish to output negative values, use the "Integer" or "Float" data formats with the {F} or {N} sign.

#### "Hexadecimal" data format

You use the "Hexadecimal" data format to display hexadecimal values. The "Hexadecimal" data format has the following inputs:

- Sign "H"
- Number of digits (optional)
- Information on forming blocks (optional)

| Output format example | Mindigits | Block size | Tag value | Result |
| --- | --- | --- | --- | --- |
| {H} | Default | - | 1 | 1 |
| {H} | Default | - | 15 | F |
| {H} | Default | - | 45054 | AFFE |
| {H4,2} | 4 | 2 | 45054 | AF FE |
| {H,2} | Default | 2 | 45054 | AF FE |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Mindigits | Number of digits (optional) | Minimum: 1 | Maximum: 16 | Default value: 1 |
| Block size | Number of digits in front of the separator (optional) | Minimum: 0 (none) | Maximum: 8 | Default value: 4 |

> **Note**
>
> The "hexadecimal" data format does not support any negative values in Unified Runtime.
>
> If you wish to output negative values, use the "Integer" or "Float" data formats with the {F} or {N} sign.

#### "Integer" data format

You use the "Integer" data format to display decimal values. The "Integer" data format has the following inputs:

- Sign "I"
- Number of digits (optional)
- Plus or minus sign in front of the sign (optional)

| Output format example | Mindigits | Tag value | Result |
| --- | --- | --- | --- |
| {I} | Default | 9 | 9 |
| {I4} | 4 | 9 | 0009 |
| {0000} | Default | 9 | 0009 |
| {I2} | 2 | 123 | 123 |
| {I} | Default | 1.6 | 1 |
| {+I} | Default | 1 | +1 |
| {I1} | 1 | 123456789 | 123456789 |
| {#,##0} | Default | 1,234 | 1,234 |
| {E} | Default | 1.12E+3 | 1.12E+3 |
| {E3} | 3 | 1.123E+3 | 1.123E+3 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| +/- | Sign (optional) |  |  | Default value: None |
| Mindigits | Number of digits (optional) | Minimum: 1 | Maximum: 8 | Default value: 1 |

#### "Float" data format

You use the "Float" data format to display values with floating-point numbers. The "Float" data format has the following inputs:

- Sign "F", "N", "E"
- Number of decimal places (optional)
- Plus or minus sign in front of the sign (optional)

| Output format example | Mindigits | Tag value | Result |
| --- | --- | --- | --- |
| {F} | default | 123.456 | 123.46 |
| {+F} | default | 123.1 | +123.10 |
| {F3} | 3 | 123.123 | 123.123 |
| {N} | default | 123 | 123.00 |
| {+N} | default | 123 | +123.00 |
| {N1} | 1 | 123 | 123.0 |
| {#,##0.###} | default | 1234.567 | 1,234.567 |
| {#,##0.##} | default | 1234.123 | 1234.12 |
| {#,###.#} | default | 1234.123 | 1,234.1 |
| {E} | default | 1123 | 1.12E+3 |
| {E1} | 1 | 1123 | 1.1E+3 |
| {E3} | 3 | 1123 | 1.123E+3 |
| {+E} | default | 1123 | +1.12E+3 |
| {E0} | 0 | 1123 | 1E+3 |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| +/- | Sign (optional) |  |  | Default value: None |
| Mindigits | Number of decimal places (optional) | F - Minimum: 1  N - Minimum: 0  E - Minimum: 0 | Maximum: 9  Maximum: 9  Maximum: 9 | Default value: 2 |

#### "String" data format

You use the "String" format to display texts. The "String" data format has the following inputs:

- Sign "S"
- Number of characters (optional)
- Formatting parameters (optional)

| Output format example | Maxchars | String format | Tag value | Result |
| --- | --- | --- | --- | --- |
| {S} | Default | - | Motor | Motor |
| {S4} | 4 | - | Motor | Moto |
| {S,trim} | Default | trim | Motor | Motor |
| {S,upper} | Default | upper | Motor | MOTOR |
| {S,lower} | Default | lower | Motor | motor |
| {S,trim,upper} | Default | trim, upper | Motor | MOTOR |
| {S3,trim,upper} | 3 | trim, upper | Motor | MOT |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Maxchars | Number of characters (optional) | Minimum: 1 | Maximum: 99 | Default value: Complete input |
| String format | Parameters for formatting of the input (optional) | trim: Outputs the input string without spaces.  upper: Outputs the input string in uppercase letters.  lower: Outputs the input string in lowercase letters. |  |  |

#### "Duration" data format

The accuracy of the duration inputs is limited to 1 ms. All inputs of less than 1 ms are shown as 0 in runtime.

To display fractions of a second, use .S, .SS or .SSS according to the pattern for the duration.

The "Period" data format has the following inputs:

- Sign "P"
- Number of time units (optional)

| Output format example | Tag value (ns) | Result |
| --- | --- | --- |
| {P} | 1:20 | 1:20 |
| {P,s} | 10000000 | 1 |
| {P,s} | -10000000 | -1 |
| {P,s} | 10000000 | 01 |
| {P,m:ss} | 35990000000 | 59:59 |
| {P,h:mm:ss} | 36000000000 | 1:00:00 |
| {P,hh:mm:ss} | 36000000000 | 01:00:00 |
| {P,D hh:mm:ss} | 864000000000 | 1D 00:00:00 |
| {P,DD hh:mm:ss} | 864000000000 | 01D 00:00:00 |
| {P,s.S} | 10000 | 0.0 |
| {P,s.SS} | 10000 | 0.00 |
| {P,s.SSS} | 10000 | 0.001 |
| {P,s.SSS} | 9999 | 0.000 |

| Symbol | Meaning |
| --- | --- |
| Durationunit | Duration |

The output format {P} enables automatic mode. In the mode the result with the smallest necessary unit of time is written. The table below shows some examples for tag values and their output in automatic mode.

| Tag value (ns) | Result | Meaning |
| --- | --- | --- |
| 9999 | 0 | 0.9999 ms |
| 10000 | 0.001 | 1ms |
| 9990000 | 0.999 | 999ms |
| 10000000 | 1 | 1s |
| 10010000 | 1.001 | 1s 1ms |
| 600000000 | 1:00 | 1m |
| 700000000 | 1:10 | 1m 10s |
| 35999990000 | 59:59.999 | 59m 59s 999ms |
| 36000010000 | 1:00:00.001 | 1h 1ms |
| 863999990000 | 23:59:59.999 | 23h 59m 59s 999ms |
| 937845670000 | 1D 02:03:04.567 | 1D 2h 3m 4s 567ms |
| 86400000000000 | 100D | 100D |

#### Localized output: "Date" and "time" data format

"Date" and "time" data formats can be localized. The output format depends on the system language. The table below shows the examples for "German".

| Data format | Permitted values and default values | Output format example | Tag value | Result |
| --- | --- | --- | --- | --- |
| Date: {D,Length} | Length:  short  medium   long  or code according to CLDR format with the sign @  Default value: short | {D} | 2019-03-21T21:08:33 | 21.03.19 |
| {D,medium} | 2019-03-21T21:08:33 | 21.03.2019 |  |  |
| {D,long} | 2019-03-21T21:08:33 | March 21, 2019 |  |  |
| {D,@y} | 2019-03-21T21:08:33 | 2019 |  |  |
| {D,@dd.MM.yyyy} | 2019-03-21T21:08:33 | 21.03.2019 |  |  |
| {D,@dd. MMMM yyyy} | 2019-03-21T21:08:33 | March 21, 2019 |  |  |
| {D,@dd.MM} | 2019-03-21T21:08:33 | 21.03 |  |  |
| {D,@dd. MMM} | 2019-03-21T21:08:33 | March 21 |  |  |
| {D,@MM-dd-yyyy} | 2019-03-21T21:08:33 | 03-21-2019 |  |  |
| {D,@MMM dd, yyyy} | 2019-03-21T21:08:33 | March 21, 2019 |  |  |
| {D,@M.d} | 2019-03-21T21:08:33 | 3.21 |  |  |
| {D,@MMMM dd} | 2019-03-21T21:08:33 | March 21 |  |  |
| {D,@yyyy/mm/dd} | 2019-03-21T21:08:33 | 2019/03/21 |  |  |
| {D,@EEE, MMM dd, ’yy} | 2019-03-21T21:08:33 | Thu., June 15, '19 |  |  |
| {D,@EEEE, MMMM d, yy} | 2019-03-21 | Thursday, March 21, 19 |  |  |
| Time: {T,Time format} | Time format:  short  medium  medium.S  medium.SS  medium.SSS  or code according to CLDR format with the sign @  Default value: medium | {T} | 2019-03-21T21:08:33 | 21:08:33 |
| {T,short} | 2019-03-21T21:08:33 | 21:08 |  |  |
| {T,@h:mm a} | 21:08:33 | 9:08 p.m. |  |  |
| {T,@HH:mm} | 21:08:33 | 21:08 |  |  |
| {T,@hh:mm a} | 21:08:33 | 9:08 p.m. |  |  |
| {T,@HH:mm:ss} | 21:08:33 | 21:08:33 |  |  |
| {T,@HH:mm:ss.SSS} | 21:08:33.1230 | 21:08:33.123 |  |  |
| {T,medium.SSS} | 21:08:33.1239 | 21:08:33.123 |  |  |

#### Combined output

You can combine the output formats:

| Description | Output format example | Tag value | Result |
| --- | --- | --- | --- |
| Date and time | {D} – {T} | 2019-03-21T21:08:33 | 21.03.2019 – 21:08:33 |
| {D} {T} | 2019-03-21T21:08:33 | 21.03.19 21:08:33 |  |
| {D,@EEEE, dd. MMMM yyyy, h:mm:ss a} | 2019-03-21T21:08:33 | Donnerstag, 21. März 2019, 9:08:33 nachm. |  |
| {D,@dd.MM.yyyy HH:mm} | 2019-03-21T21:08:33 | 21.03.2019 21:08 |  |
| Date and time with line break | {D}\n{T} | 2019-03-21T21:08:33 | 21.03.2019   21:08:33 |
| Two numerical values | hex {H} – dec {I} | 45054 | hex AFFE – dec 45054 |
| Text with prefix | myMotor {S} | motor34 | myMotor motor34 |
| Number with prefix | MyMotor#{00} | 12 | MyMotor#12 |
| Percent | {I}% | 20 | 20% |
| Currency | {#,##0} EUR | 20 | 20 EUR |
| Currency | ${#,##0.##} | 20 | $20 |
| Unit | {F2} m/s | 10.00 | 10.00 m/s |

---

**See also**

[Configuring the alarm control (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#configuring-the-alarm-control-rt-unified-1)
  
<http://cldr.unicode.org/>

### Disable remote control (RT Unified)

#### Introduction

You can disable the "Allow operator control" property for operable objects. You cannot then operate the objects in runtime. The object or the buttons on the object are dimmed.

#### Requirement

- The HMI screen is open with at least one object.

#### Disable the "Allow operator control" property

You can disable the option for operator control in runtime using the "Allow operator control" property.

The disabled property "Allow operator control" has the following effect:

- The objects in the "Elements" group are grayed out.
- For objects in the "Controls" group, the operable areas, e.g. buttons on the toolbar, are grayed out.

The following figure shows the grayed out buttons in the alarm control:

![Disable the "Allow operator control" property](images/162534584459_DV_resource.Stream@PNG-en-US.png)

The objects are displayed in the same way in the engineering system and in runtime.

### Hotkeys (RT Unified)

#### Introduction

You can use the hotkeys in Runtime to perform various actions. You can specify the hotkeys as a key or key combination in the Engineering System.

Examples of hotkey functions:

- Change language
- Change screen
- Acknowledge alarm

The use of the hotkeys is supported:

- For WinCC Unified PC
- For the View Of Things application

The use of the hotkeys is not supported:

- For Unified Comfort Panels
- For faceplates

> **Note**
>
> It is recommended to use the US English layout keyboard.

#### Requirement

- The HMI screen with at least one button or object is open.

#### Supported objects

You can configure hotkeys in the "Properties" tab of the Inspector window for the following objects:

- Button
- Controls with one toolbar

The default value for a hotkey in the "Static value" column is "None".

#### Configuring hotkeys

You can find the "Hotkey" property in the Inspector window in the "Properties" tab:

- Button: "Properties > Miscellaneous > Hotkey".
- Controls with one toolbar: "Properties > Miscellaneous > Toolbar > Elements > [0] Button > Hotkey".

To configure a hotkey for a button, for example, follow these steps:

1. Select the button.
2. Select "Properties > Miscellaneous > Hotkey".
3. In the input field, click in the "Static value" column.

   A dialog opens.

   ![Configuring hotkeys](images/160196142091_DV_resource.Stream@PNG-en-US.png)

   ![Configuring hotkeys](images/160196142091_DV_resource.Stream@PNG-en-US.png)
4. Select a keyboard shortcut.

   ![Configuring hotkeys](images/160196152715_DV_resource.Stream@PNG-en-US.png)

   ![Configuring hotkeys](images/160196152715_DV_resource.Stream@PNG-en-US.png)
5. Using the options in the selection dialog, you can do the following:

   - Delete settings and close the dialog ![Configuring hotkeys](images/160197140235_DV_resource.Stream@PNG-de-DE.png).
   - Discard changes and close the dialog ![Configuring hotkeys](images/160196585483_DV_resource.Stream@PNG-de-DE.png).
   - Apply settings and close the dialog ![Configuring hotkeys](images/160197118859_DV_resource.Stream@PNG-de-DE.png).

**Note**

You may use a keyboard shortcut only once in a screen. In case of duplicate use, an error message will appear.

#### Result

You have configured a key or key combination for a hotkey.

### Configuring object properties (RT Unified)

This section contains information on the following topics:

- [Managing properties (RT Unified)](#managing-properties-rt-unified)
- ["Filter" function (RT Unified)](#filter-function-rt-unified)
- ["Favorites" function (RT Unified)](#favorites-function-rt-unified)
- [Highlighting and resetting properties (RT Unified)](#highlighting-and-resetting-properties-rt-unified)
- [Configuring collection properties (RT Unified)](#configuring-collection-properties-rt-unified)

#### Managing properties (RT Unified)

##### Introduction

The properties of an object are displayed in the property list in the Inspector window. Here you can edit the properties, e.g. change the size and position of an object, or dynamize objects.

There are three functions available in the Inspector window that allow you to efficiently edit properties:

- Filter
- Favorites
- Hide change events

You manage the properties in the Inspector window using the ![Introduction](images/167561911435_DV_resource.Stream@PNG-de-DE.png) icons.

![Introduction](images/167563416971_DV_resource.Stream@PNG-en-US.png)

##### Display of the property list in the Inspector window

The properties are displayed in the property list either in alphabetical order or in categories.

You can sort the property list as follows:

- ![Display of the property list in the Inspector window](images/166234619275_DV_resource.Stream@PNG-de-DE.png) Display of properties in alphabetical order
- ![Display of the property list in the Inspector window](images/166234623243_DV_resource.Stream@PNG-de-DE.png) Display of the properties grouped in categories

With both views, all details of the individual properties can be shown or hidden:

- ![Display of the property list in the Inspector window](images/166236790411_DV_resource.Stream@PNG-de-DE.png) All details are shown
- ![Display of the property list in the Inspector window](images/166236794379_DV_resource.Stream@PNG-de-DE.png) All details are hidden

| Symbol | Meaning |
| --- | --- |
| ![Display of the property list in the Inspector window](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for working efficiently** |
| - Drag-and-drop a tag or resource list from the details view in the project tree to a property in the Inspector window.   The details of the lower-level of the property are displayed. |  |

##### "Filter" function

Activate the "Filter" function !["Filter" function](images/165848560523_DV_resource.Stream@PNG-de-DE.png).

If you enter the name or parts of the name in the search field, the properties that fulfill the search criterion are displayed.

##### "Favorites" function

Activate the "Favorites" function !["Favorites" function](images/165848568459_DV_resource.Stream@PNG-de-DE.png).

The selected, frequently used properties are displayed.

##### "Hide change events" function

Activate the "Hide change events" function !["Hide change events" function](images/167561903115_DV_resource.Stream@PNG-de-DE.png).

If you activate the function, the arrow in front of the name of a property is displayed only for properties that contain other properties.

The function is deactivated by default.

!["Hide change events" function](images/167564081675_DV_resource.Stream@PNG-en-US.png)

##### Showing dynamized properties

Dynamized properties are shown in dark blue font and in bold in the Inspector window in the "Name" column.

Groups containing a dynamized property are shown in dark blue font.

---

**See also**

[Displaying dynamization of the properties (RT Unified)](#displaying-dynamization-of-the-properties-rt-unified)
  
["Filter" function (RT Unified)](#filter-function-rt-unified)
  
["Favorites" function (RT Unified)](#favorites-function-rt-unified)

#### "Filter" function (RT Unified)

##### Introduction

The "Filter" function is available in the Inspector window. You can use to edit the properties efficiently. The "Filter" function enables you to search for the individual properties in the Inspector window or filter the properties that fulfill a search criterion.

##### Requirement

- The HMI screen is open with at least one object.

##### Filter properties

To filter the properties of a screen object, follow these steps:

1. Click on the "Filter" icon ![Filter properties](images/165848560523_DV_resource.Stream@PNG-de-DE.png) in "Properties > Properties" in the Inspector window.
2. In the "Search" input field, type in the term you are looking for, e.g. "Color" in the "Name" column.
3. Confirm the input with the <Return> key.

   ![Filter properties](images/169595964171_DV_resource.Stream@PNG-en-US.png)

   ![Filter properties](images/169595964171_DV_resource.Stream@PNG-en-US.png)

All hits of the properties which contain the term "color" are displayed.

##### Using search terms with other objects or screens

If you choose another screen object or another screen, the current search term remains in the input field.

The search terms that you have entered in the currently open project are retained until the opened project is closed.

![Using search terms with other objects or screens](images/169596109835_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Managing properties (RT Unified)](#managing-properties-rt-unified)

#### "Favorites" function (RT Unified)

##### Introduction

The "Favorites" function is available in the Inspector window. You can use it to edit the properties efficiently. You can display the system-defined favorites and your own favorite properties for each screen object.

You can find an overview of system-defined favorites under "Settings > Visualization > Favorites screens (WinCC Unified)" in the "Favorites properties" table:

![Introduction](images/169559271947_DV_resource.Stream@PNG-en-US.png)

The user-defined favorites are shown in the "User-defined favorites" column in the table.

You can also locate the individual properties of an object by using the "Filter" function in the Inspector window ![Introduction](images/165848560523_DV_resource.Stream@PNG-de-DE.png).

##### Requirement

- The HMI screen is open with at least one object.

##### Add property to favorites

You can add your favorite properties of a screen object to the favorites.

To add a property to the favorites, follow these steps:

1. Right-click on a property that is not defined as a favorite by the system.

   The shortcut menu opens.

   ![Add property to favorites](images/169559276811_DV_resource.Stream@PNG-en-US.png)

   ![Add property to favorites](images/169559276811_DV_resource.Stream@PNG-en-US.png)
2. Select "Add to favorites". The number of favorite properties is not limited.
3. To display all favorites, click the icon ![Add property to favorites](images/165848568459_DV_resource.Stream@PNG-de-DE.png).

##### Remove property from favorites

To remove a property from the favorites, follow these steps:

1. To display all favorites, click the icon ![Remove property from favorites](images/165848568459_DV_resource.Stream@PNG-de-DE.png).
2. Right-click on the favorite property.

   The shortcut menu opens.

   ![Remove property from favorites](images/169559524875_DV_resource.Stream@PNG-en-US.png)

   ![Remove property from favorites](images/169559524875_DV_resource.Stream@PNG-en-US.png)
3. Select "Remove from favorites".

You can find all favorites added or deleted by you in the "Favorite properties" table under "Settings > Visualization > Favorites screens (WinCC Unified)".

---

**See also**

[Managing properties (RT Unified)](#managing-properties-rt-unified)

#### Highlighting and resetting properties (RT Unified)

##### Introduction

In the Runtime settings of the device, you can set one of the pre-defined styles. You can change some properties of screens and screen objects in the Inspector window, for example the background color, irrespective of the style values.

##### Highlighting properties of screens and screen objects

In order to identify the properties whose values differ from the style values, follow these steps:

1. Click on the "Filter" icon.
2. In the "Static value" column, select "Different from style value".

   ![Highlighting properties of screens and screen objects](images/169593403659_DV_resource.Stream@PNG-en-US.png)

   ![Highlighting properties of screens and screen objects](images/169593403659_DV_resource.Stream@PNG-en-US.png)

   All modified properties are displayed and are formatted bold in the "Static value" column.

   ![Highlighting properties of screens and screen objects](images/169593399051_DV_resource.Stream@PNG-en-US.png)

   ![Highlighting properties of screens and screen objects](images/169593399051_DV_resource.Stream@PNG-en-US.png)

##### Resetting properties of screens and screen objects

To reset the changed property values to the default value of the selected style, follow these steps:

1. Right-click on the property. The shortcut menu opens.
2. Select "Reset property value".

   ![Resetting properties of screens and screen objects](images/169593394443_DV_resource.Stream@PNG-en-US.png)

   ![Resetting properties of screens and screen objects](images/169593394443_DV_resource.Stream@PNG-en-US.png)

   The property value is reset to the default value of the selected style.

You can reset the following properties:

- Manually set properties.
- Properties that have a corresponding value in the current style.

The properties that do not have a style value are not formatted in bold or displayed in the filter, even if you have set the properties manually.

#### Configuring collection properties (RT Unified)

This section contains information on the following topics:

- [Element collections (RT Unified)](#element-collections-rt-unified)
- [Displaying the properties of a collection (RT Unified)](#displaying-the-properties-of-a-collection-rt-unified)
- [Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

##### Element collections (RT Unified)

###### Introduction

Some screen objects contain a collection of similar elements under the properties, for instance points, items, buttons, and trend areas.

These elements and their properties are displayed in a table on the right-hand side of the Inspector window, where you can manage the collection properties.

###### Examples of collections

Examples of elements that form a collection under the properties of an object include:

- Points:

  - Polygon
  - Polyline
- Items:

  - Check box
  - Radio button
  - List box
- Columns:

  - Alarm control
  - Process control
- Trend areas

  - Trend control
  - Function trend control
- Buttons in the toolbar:
- Elements in the information bar:

  - Controls, e.g. alarm control

###### Example: Trend control with "Trend areas" collection

As an example, the following screen shows a trend control in the workspace of the "Screens" editor.

The "Trend areas" property was clicked on in the Inspector window at the bottom left.

Clicking on the "Trend areas" property displays the table on the right with the elements of the collection, here the trend areas, and their properties.

![Example: Trend control with "Trend areas" collection](images/172445248779_DV_resource.Stream@PNG-en-US.png)

##### Displaying the properties of a collection (RT Unified)

###### Introduction

Some screen objects contain a collection of similar elements under the properties. The properties of the elements in the collection are displayed and managed in a table in the Inspector window.

###### Requirement

- The HMI screen is open with at least one object, e.g. a trend control.
- The object contains a collection of elements, e.g. trends.

###### Managing the properties of elements in the collection

To manage the individual properties of the elements in the collection in the table, follow these steps:

1. In a trend control, for instance, click "Properties > General > Trend areas > Trends". The "Trends" table is displayed.
2. Right-click in the row with the property names. The shortcut menu opens.

   ![Managing the properties of elements in the collection](images/172316247307_DV_resource.Stream@PNG-en-US.png)

   ![Managing the properties of elements in the collection](images/172316247307_DV_resource.Stream@PNG-en-US.png)
3. You have the option to:

   - Show or hide the individual properties.
   - Show all columns.
   - Optimize the width of a column.
   - Optimize width of all columns.

You can move the columns in the table using drag-and-drop.

###### Displaying and managing properties in the table

The properties are displayed in the table as follows:

- Cells without content are displayed to save space.
- Check boxes and numeric values are displayed centered.
- Modified sorting of the columns is saved across projects.
- Modified visibility of the columns is saved across projects.

##### Auto-filling the property values of a collection (RT Unified)

###### Introduction

Some screen objects contain a collection of similar elements under the properties. You can auto-fill the property values of the elements in the collection.

###### Requirement

- The HMI screen is open with at least one object.
- The object contains a collection of elements, e.g. trends.

###### Auto-filling the property values in the collection

To automatically fill in the property values of the elements in the collection, follow these steps:

1. Select the collection according to the object, e.g.:

   - For polygons and polylines, click "Properties > Properties > Size and position > Points".
   - For the elements, e.g. check box, click "Properties > Properties > General > Selection items".
   - With the controls, e.g. alarm control, click "Properties > Properties > Miscellaneous > Alarm control > Columns".
   - For controls with a toolbar, click "Properties > Miscellaneous> Toolbar > Elements".
2. Select one or more contiguous cells in the collection in the right part of the Inspector window.
3. Drag the blue border around this cell up or down.

   ![Auto-filling the property values in the collection](images/172190010763_DV_resource.Stream@PNG-en-US.png)

   ![Auto-filling the property values in the collection](images/172190010763_DV_resource.Stream@PNG-en-US.png)

The values are transferred to the destination cells.

###### Moving and deleting cells

To move or delete the cells, follow these steps:

1. In the right part of the Inspector window, drag the blue border around the cells.
2. Move or delete the selected cells using the ![Moving and deleting cells](images/137779796747_DV_resource.Stream@PNG-de-DE.png) and ![Moving and deleting cells](images/137779804939_DV_resource.Stream@PNG-de-DE.png) buttons.

The cells are moved or deleted.

---

**See also**

[Polyline (RT Unified)](#polyline-rt-unified)
  
[Polygon (RT Unified)](#polygon-rt-unified)
  
[Dynamizing object property via tag (RT Unified)](#dynamizing-object-property-via-tag-rt-unified)
  
[Transferring property conditions (RT Unified)](#transferring-property-conditions-rt-unified)

### Designing objects (RT Unified)

This section contains information on the following topics:

- [Changing the object size (RT Unified)](#changing-the-object-size-rt-unified)
- [Changing the position of an object (RT Unified)](#changing-the-position-of-an-object-rt-unified)
- [Transfer format (RT Unified)](#transfer-format-rt-unified)
- [Designing the fill pattern (RT Unified)](#designing-the-fill-pattern-rt-unified)
- [Designing the border of an object (RT Unified)](#designing-the-border-of-an-object-rt-unified)
- [Configuring reordering of the columns (RT Unified)](#configuring-reordering-of-the-columns-rt-unified)
- [Rearranging columns in runtime (RT Unified)](#rearranging-columns-in-runtime-rt-unified)
- [Changing a property for multiple objects (RT Unified)](#changing-a-property-for-multiple-objects-rt-unified)

#### Changing the object size (RT Unified)

##### Introduction

When you select an object, it is framed by a bounding box with blue handles. You have the following options for resizing an object:

- Use the mouse to drag the blue handles on the bounding box.
- Configure the properties in the Inspector window.

> **Note**
>
> You can change the form of the objects "Line", "Polyline" and "Polygon" as follows:
>
> - Use the mouse to drag the orange handles on the object.
> - Configure the properties in the Inspector window.

##### Requirement

- The HMI screen is open with at least one object.

##### Changing object size with the mouse

To change the object size with the mouse, follow these steps:

1. Select the object you want to resize.

   The bounding box is displayed. The following figure shows a selected object:

   ![Changing object size with the mouse](images/100725818251_DV_resource.Stream@PNG-de-DE.png)

   ![Changing object size with the mouse](images/100725818251_DV_resource.Stream@PNG-de-DE.png)
2. Drag a handle of the box to a new position.

The object size is changed.

| Symbol | Meaning |
| --- | --- |
| ![Changing object size with the mouse](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| If you press the <Ctrl + Shift> keys while dragging, the object size is changed according to the aspect ratio. |  |

##### Changing the size of multiple objects with the mouse

To change the size of multiple objects with the mouse, follow these steps:

1. Select the objects by multiple selection.

   The bounding box is displayed.
2. Drag a handle of the box to a new position.

The size of the selected objects is changed.

| Symbol | Meaning |
| --- | --- |
| ![Changing the size of multiple objects with the mouse](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| If you press the <Ctrl + Shift> keys while dragging, the selected objects are resized according to the aspect ratio. |  |

##### Configuring the object size through properties

To change the object size through properties, follow these steps:

1. Select "Properties" > "Properties" > "Size and position".
2. In the "Static value" column, enter the "Size - width" and "Size - height" coordinates.

The object size is changed.

##### Changing object size using keys

To change the object size using keys, follow these steps:

1. Select the object you want to resize.
2. On the keyboard, press the keys:

   - <Ctrl + Arrow key>
   - <Ctrl + Shift + Arrow key>

The object size is changed depending on the arrow key selected.

#### Changing the position of an object (RT Unified)

##### Introduction

When you select an object, it is framed by a bounding box with blue handles. You have the following options for repositioning an object:

- Position the object with the mouse.
- Configure the object properties in the Inspector window.

##### Requirement

- The HMI screen is open with at least one object.

##### Changing the object position with the mouse

To change the object position with the mouse, follow these steps:

1. Select the object whose position you want to change.

   The bounding box is displayed.
2. Left-click the object and keep the left mouse button pressed.
3. Move the object with the mouse pointer to the new position.

The object is moved to the new position.

##### Configuring the object position through properties

To change the object position using properties, follow these steps:

1. Select "Properties" > "Properties" > "Size and position".
2. In the "Static value" column, enter the "Position - left" and "Position - top" coordinates.

The position of the object in reference to the screen origin is changed. The zero position is located at the top left-hand corner of the screen.

##### Changing the object position using keys

To change the object position using keys, follow these steps:

1. Select the object you want to resize.
2. On the keyboard, press the <Shift + Arrow> keys

The object position is changed depending on the arrow key selected.

#### Transfer format (RT Unified)

##### Introduction

You can transfer the format of an object to another object. You can find the "Transfer format" icon in the function bar of the screen editor.

![Introduction](images/156894970891_DV_resource.Stream@PNG-de-DE.png)

##### Transferring the format

You use the "Transfer format" function to transfer the properties of the source object to the target object.

You can transfer edit the properties:

- From a source object to the same target object, for example, from line to line.
- From a source object to a different target object, for example, from line to a circle.
- From a source object to multiple target objects, for example, from line to line, circle and button.

##### Requirement

- The HMI screen is open with at least one object.

##### Transferring the format

To transfer the properties of an object to a single target object, follow these steps:

1. Select an object.
2. Click on the "Transfer format" icon. When you hover the mouse over an object, the symbol for the mouse pointer changes ![Transferring the format](images/169001490443_DV_resource.Stream@PNG-de-DE.png).
3. Click on another object.

   The properties are transferred to the target object.

To transfer the properties of an object to multiple target objects, follow these steps:

1. Select an object.
2. Click on the "Transfer format" icon. When you hover the mouse over an object, the symbol for the mouse pointer changes ![Transferring the format](images/169001490443_DV_resource.Stream@PNG-de-DE.png).
3. Drag a selection border around the target objects with the mouse.

   The properties are transferred to multiple target objects.

##### Table of objects and categories of the properties

The table below contains the objects and categories of the properties that you can transfer to another object.

These properties can be found in the Inspector window under:

- "Properties > General"
- "Properties > Format"
- "Properties > Appearance"

The properties that you cannot transfer to another object are listed in the "With the exception of" column.

| Object | All properties of the category | With the exception of |
| --- | --- | --- |
| Line, polyline, polygon, ellipse, ellipse segment, circle segment, elliptical arc, circular arc, circle, rectangle | Appearance |  |
| Text box | General | Text |
| Format |  |  |
| Appearance |  |  |
| Graphic view | Format |  |
| Appearance |  |  |
| IO field | General | Output format  Mode  Process value |
| Format |  |  |
| Appearance |  |  |
| Symbolic IO field | General | Process value  Resource list |
| Format | Content > Type |  |
| Appearance |  |  |
| Button, switch | General | Content > Type |
| Format |  |  |
| Appearance |  |  |
| Bar | General | Label > Text  Scale > Scale value - maximum, Scale value - minimum  Process value  Title > Text |
| Appearance |  |  |
| Slider | General | Label > Text  Title > Text |
| Appearance |  |  |
| Gauge | General | Label > Text   Title > Text   Process value  Scale > Output format  Scale > Scale value - maximum, Scale value - minimum |
| Appearance |  |  |
| Check box, radio button, list box | Format | Content > Type |
| Appearance |  |  |
| Clock | General |  |
| Appearance |  |  |
| Miscellaneous | Name  Time - source  Tab index  Title > Text  Tooltip  Connection quality - show  Connection status |  |
| Touch area | Appearance |  |
| Alarm control | Format |  |
| Appearance |  |  |
| Miscellaneous | Alarms - show current  Alarms - current  Alarms - displayed  Label > Text  Alarm control > Header - settings, Color mode, Filter - allow, Selection - select entire rows, Selection - mode, Sorting - allow, Columns, Row height  Alarm statistics - view > Header - settings, Color mode, Filter - allow, Selection - select entire rows, Selection - mode, Sorting - allow, Columns, Row height  Alarm statistics - settings  Name  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status  Time zone |  |
| Media Player | Appearance |  |
| Miscellaneous | Autoplay  Label > Text  Name  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status  Video output |  |
| Screen window | Format |  |
| Appearance |  |  |
| Miscellaneous | Label > Text  Screen name  Screen number  Tab order - Continue in screen window  Name  Icon  System  Tab index  Connection status |  |
| Trend control | Appearance |  |
| Miscellaneous | Label > Text  Name  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status  Time zone |  |
| Trend companion | Format |  |
| Appearance |  |  |
| Miscellaneous | Label > Text  Appearance - trend ruler > Header - settings, Color mode, Filter - allow, Selection - select entire rows, Selection - mode, Sorting - allow, Columns, Row height  Name  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status  Time zone |  |
| Process control | Appearance |  |
| Miscellaneous | Editing mode  Label > Text  Name  Online  Process control > Header - settings, Color mode, Selection - select entire rows, Selection - mode, Sorting - allow, Columns, Row height  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status  Time factor - average  Time zone |  |
| Function trend control | Appearance |  |
| Miscellaneous | Axes - swap  Label > Text  Name  Online  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status |  |
| Web control | Appearance |  |
| Miscellaneous | Label > Text  Name  Online  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status |  |
| Parameter set control | Appearance |  |
| Miscellaneous | Editing mode  Label > Text  Details - hide  Name  Parameter view > Header - settings, Color mode, Filter - allow, Selection - select entire rows, Selection - mode, Sorting - allow, Columns, Row height  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status  Time zone |  |
| Faceplate container | Appearance |  |
| Miscellaneous | Label > Text  Faceplate type  Name  Interface  Icon  Tab index  Connection status |  |
| System diagnostics control | Appearance |  |
| Miscellaneous | Label > Text  Name  Information bar > Operator control - allow, Elements, Tooltips - show  Icon  Function bar > Operator control - allow, Elements, Tooltips - show  Tab index  Connection status  Time zone |  |

---

**See also**

[Using the toolbar in the screen editor (RT Unified)](#using-the-toolbar-in-the-screen-editor-rt-unified)

#### Designing the fill pattern (RT Unified)

##### Introduction

You can design the fill pattern of an object. The design options change in the Inspector window depending on the object for which you are making the filling pattern.

For certain objects, you can define a color background, a transparent background or a background with a color gradient.

##### Requirement

- The HMI screen is open with at least one object.

##### Designing the fill pattern of an object

To design the fill pattern of an object, e.g. a circle, follow these steps:

1. In the Inspector window, click "Properties > Properties > Appearance > Background - Fill pattern".
2. To define a transparent background for the object, for example, select "Transparent".

| Symbol | Meaning |
| --- | --- |
| ![Designing the fill pattern of an object](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Efficiency tip** |
| Using multiple selection, you can set the fill pattern in multiple objects at the same time. |  |

##### Result

The object is shown as transparent.

##### Additional design options

Additional design options are available in the Inspector window under "Properties > Properties > Appearance". The procedure for using these options is the same as the one described in the examples above.

##### Restriction for objects with events

Events for operator actions are only triggered if the operator action takes place in the marked, visible area of the object.

If the fill pattern of an object is transparent, click exactly on the object border in runtime in order to trigger the events configured for the object. Select the border width so that you can hit the border.

> **Note**
>
> Objects for which the "Opacity" property has the value "0" are also not visible in runtime and do not trigger events.

#### Designing the border of an object (RT Unified)

##### Introduction

Elements and some basic objects have a border. You can configure the width and color of the border.

Anti-aliasing affects the appearance of the border line at certain border width settings, such as 1 px. The border line may appear blurred or brighter.

##### Requirement

- The HMI screen is open.
- An element or one of the following basic objects is placed:

  - Text box
  - Rectangle
  - Circle and circle segment
  - Ellipse and ellipse segment
  - Polyline

##### Change frame width

1. Select the object.
2. In the Inspector window, click "Properties > Properties > Appearance > Border - width".
3. Enter the desired width.

For elements and text boxes, the border is drawn on the inner edge of the object. For the other basic objects, it is drawn at the inner edge and outer edge. The values of the "Size - width" and "Size - height" properties remain the same.

##### Change frame color

1. Select the object.
2. Click "Properties > Properties > Border - color" in the Inspector window.
3. Enter the RGB values of the color or select a color from the drop-down list.

   Select "More colors" in the drop-down list to add custom colors to the selection or set the specifications using HSL.

> **Note**
>
> Alternatively, you can change the color in the central color management of the object.

---

**See also**

[Central color management (RT Unified)](#central-color-management-rt-unified)

#### Configuring reordering of the columns (RT Unified)

##### Introduction

You have the option of configuring the following table-based controls in such a way that operators can reorder the table columns in runtime:

- Alarm control
- Trend companion
- Parameter set control
- System diagnostics control
- Process control

##### Requirement

- The "Screens" editor is open.
- One of the above-named controls has been placed on the screen.

##### Procedure

1. Select, for example, an alarm control in the work area.
2. In the Inspector window, click "Properties > Properties > Miscellaneous > Alarm control > Header - settings".
3. To allow the columns to be rearranged in runtime, enable the property "Columns - Change sequence".

   To prevent reordering, deselect the property.

##### Result

Once the project has been downloaded to the device, operators can use drag-and-drop to reorder the columns displayed in the control in runtime.

#### Rearranging columns in runtime (RT Unified)

##### Introduction

You can reorder the table columns in the following table-based controls:

- Alarm control
- Trend companion
- Process control
- Parameter set control
- System diagnostics control

##### Requirement

Reordering of columns is allowed by the configuration of the control in the engineering.

##### Procedure

Using drag-and-drop, move the header of the column to be moved onto the header of another column.

> **Note**
>
> The time column cannot be moved.

##### Result

The moved column is inserted at the position that the mouse pointer had when the drag-and-drop movement ended.

The new column order applies only to the current client. If you switch to another page or refresh the browser window, the column order is lost.

> **Note**
>
> If you move a column next to a hidden column and then show this column afterwards, it is always displayed to the right of the moved column.

##### Example 1: Inserting columns to the right or the left

The procedure is illustrated based on the example of an alarm control. In the initial situation, the table of the alarm control has the following column arrangement:

![Example 1: Inserting columns to the right or the left](images/150312214667_DV_resource.Stream@PNG-de-DE.png)

To insert the "Origin" column to the right of the "Alarm text" column, follow these steps:

1. Drag-and-drop the column header from "Origin" to the right column header half of the "Alarm text" column:

   ![Example 1: Inserting columns to the right or the left](images/150321298443_DV_resource.Stream@PNG-de-DE.png)

   ![Example 1: Inserting columns to the right or the left](images/150321298443_DV_resource.Stream@PNG-de-DE.png)
2. The "Origin" column is inserted to the right of the "Alarm text" column.

   ![Example 1: Inserting columns to the right or the left](images/150321691019_DV_resource.Stream@PNG-de-DE.png)

   ![Example 1: Inserting columns to the right or the left](images/150321691019_DV_resource.Stream@PNG-de-DE.png)

To insert the "Origin" column to the left of the "Alarm text" column, follow these steps:

1. Drag-and-drop the column header from "Origin" to the left column header half of the "Alarm text" column:

   ![Example 1: Inserting columns to the right or the left](images/150321699595_DV_resource.Stream@PNG-de-DE.png)

   ![Example 1: Inserting columns to the right or the left](images/150321699595_DV_resource.Stream@PNG-de-DE.png)
2. The "Origin" column is inserted to the left of the "Alarm text" column.

   ![Example 1: Inserting columns to the right or the left](images/150321823371_DV_resource.Stream@PNG-de-DE.png)

   ![Example 1: Inserting columns to the right or the left](images/150321823371_DV_resource.Stream@PNG-de-DE.png)

##### Example 2: Reordering of columns in combination with hidden columns

This example illustrates the reordering of columns in combination with hidden columns.

- The alarm control has the same column arrangement as in example 1.
- The alarm control was configured in the engineering in such a way that the display of the "Origin" column is controlled dynamically in Runtime by setting a tag.

To reorder the columns in combination with hidden columns, follow these steps:

1. Hide the "Origin" column by setting the tag.
2. Insert the "Status text" column to the left of the "Area" column.
3. Show the "Origin" column by setting the tag.

The order of the columns is as follows: "Alarm class", "Status text", "Origin", "Area", "Alarm text".

#### Changing a property for multiple objects (RT Unified)

##### Introduction

You can change the static value of a property for multiple objects at the same time.

##### Requirement

- The HMI screen with at least two objects is open.

##### Changing properties for multiple objects

To change the static value of a property for multiple objects at the same time, follow these steps:

1. Select several objects in the screen via multiple selection.
2. Select a property, e.g. the background color, in the Inspector window.
3. Change the static value of the property.

The property is changed on all selected objects that have this property.

---

**See also**

[Select multiple objects (RT Unified)](#select-multiple-objects-rt-unified)

### Moving objects (RT Unified)

This section contains information on the following topics:

- [Rotating object (RT Unified)](#rotating-object-rt-unified)
- [Aligning objects (RT Unified)](#aligning-objects-rt-unified)
- [Moving an object forward or backward (RT Unified)](#moving-an-object-forward-or-backward-rt-unified)
- [Moving objects on layers (RT Unified)](#moving-objects-on-layers-rt-unified)
- [Moving objects in the screen (RT Unified)](#moving-objects-in-the-screen-rt-unified)
- [Rotating an object around a pivot point (RT Unified)](#rotating-an-object-around-a-pivot-point-rt-unified)

#### Rotating object (RT Unified)

##### Introduction

You can rotate an object clockwise or counterclockwise around its center axis in steps of 90°. You can also rotate multiple objects using the multiple selection function. Each object has its own reference point for rotation and is rotated around its own reference point during multiple selection.

You cannot rotate certain WinCC objects, e.g. controls.

##### Requirement

- The HMI screen is open with at least one object.

##### Rotating an object

To rotate an object, follow these steps:

1. Select the object that you want to rotate.
2. Click on one of the symbols in the toolbar to rotate the object.

The object is now displayed rotated.

Alternatively, select the command for rotating the object under "Rotate" in the shortcut menu.

##### Symbols for rotating the object

| Symbol | Meaning |
| --- | --- |
| ![Symbols for rotating the object](images/100726120587_DV_resource.Stream@PNG-de-DE.png) | The object is rotated clockwise around its center. The angle of rotation is 90°. |
| ![Symbols for rotating the object](images/100726128267_DV_resource.Stream@PNG-de-DE.png) | The object is rotated counter-clockwise around its center. The angle of rotation is 90°. |
| ![Symbols for rotating the object](images/100726135947_DV_resource.Stream@PNG-de-DE.png) | The object is rotated clockwise by 180°. |

##### Alignment of rotated objects

The alignment of elements in an object will change in a rotated object.

The following figure shows how a rectangle and an ellipse behave under the different commands for rotating an object:

![Alignment of rotated objects](images/172323880459_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Using the toolbar in the screen editor (RT Unified)](#using-the-toolbar-in-the-screen-editor-rt-unified)

#### Aligning objects (RT Unified)

##### Introduction

You can align the screen objects in the screen with reference to a reference object.

The selected objects are aligned justified to the reference object. The reference object is the object that you selected first.

##### Requirement

- The HMI screen is open with at least two objects.

##### Aligning selected objects

To align the selected objects in relation to a reference object, follow these steps:

1. Select the desired objects using multiple selection.
2. Specify an object as the reference object.
3. Click on one of the symbols in the toolbar for aligning the object.

The selected objects are now aligned in relation to the reference object.

Alternatively, select the command for aligning the object under "Alignment" in the shortcut menu.

##### Symbols for aligning the object

| Icon | Description |
| --- | --- |
| ![Symbols for aligning the object](images/100725921547_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the left edge of the reference object. |
| ![Symbols for aligning the object](images/100725929227_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the vertical center axis of the reference object. |
| ![Symbols for aligning the object](images/100725936907_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the right edge of the reference object. |
| ![Symbols for aligning the object](images/100725957387_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the upper edge of the reference object. |
| ![Symbols for aligning the object](images/100725965067_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the horizontal center axis of the reference object. |
| ![Symbols for aligning the object](images/100725972747_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the lower edge of the reference object. |
| ![Symbols for aligning the object](images/100725980427_DV_resource.Stream@PNG-de-DE.png) | Centers the selected objects to the center points of the reference object. |
| ![Symbols for aligning the object](images/147445594507_DV_resource.Stream@PNG-de-DE.png) | Centers the selected objects vertically in the screen. |
| ![Symbols for aligning the object](images/104615059083_DV_resource.Stream@PNG-de-DE.png) | Centers the selected objects horizontally in the screen. |
| ![Symbols for aligning the object](images/142973719051_DV_resource.Stream@PNG-de-DE.png) | Distributes at least 3 selected objects evenly horizontally. |
| ![Symbols for aligning the object](images/142973723147_DV_resource.Stream@PNG-de-DE.png) | Distributes at least 3 selected objects evenly vertically. |
| ![Symbols for aligning the object](images/142969068171_DV_resource.Stream@PNG-de-DE.png) | Specifies the same height for all selected objects. |
| ![Symbols for aligning the object](images/142969075851_DV_resource.Stream@PNG-de-DE.png) | Specifies the same width for all selected objects. |
| ![Symbols for aligning the object](images/142969079947_DV_resource.Stream@PNG-de-DE.png) | Specifies the same height and width for all selected objects. |

##### Aligning individual objects

To align an object in the screen in relation to other objects using minor lines, follow these steps:

1. Select an object.
2. Drag the object to a position until the blue minor lines become visible.
3. Position the object using the auxiliary lines.

The object is now aligned in relation to other objects.

---

**See also**

[Using the toolbar in the screen editor (RT Unified)](#using-the-toolbar-in-the-screen-editor-rt-unified)

#### Moving an object forward or backward (RT Unified)

##### Introduction

You can move an object in front of or behind other objects within a layer.

##### Requirement

- The HMI screen is open with at least two objects.

##### Moving objects forward or backward

To move an object forward or backward, follow these steps:

1. Select the object you want to move forward or backward.
2. Click on one of the symbols in the toolbar to move the object.

The object is moved in the layer.

Alternatively, select the command for moving the object under "Arrange" in the shortcut menu.

##### Symbols for moving the object one layer up or down

| Icon | Description |
| --- | --- |
| ![Symbols for moving the object one layer up or down](images/166167841291_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object in front of all the other objects of the same layer. |
| ![Symbols for moving the object one layer up or down](images/166167837195_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object forward by one position. |
| ![Symbols for moving the object one layer up or down](images/166167845387_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object back by one position. |
| ![Symbols for moving the object one layer up or down](images/166170435083_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object to the lowest position in the same layer. |

##### Alternative procedure

1. Open the "Layers" palette of the "Layout" task card.
2. Navigate to the required object.
3. Hold down the mouse button, and drag the object in the tree topology to the required position in the layer.
4. Now release the mouse button.

---

**See also**

[Using the toolbar in the screen editor (RT Unified)](#using-the-toolbar-in-the-screen-editor-rt-unified)

#### Moving objects on layers (RT Unified)

##### Introduction

Newly added objects are on the active layer by default. You can, however, assign an object to another layer at a later time.

##### Requirement

- The HMI screen is open with at least one object.

##### Moving an object to another layer

To move an object to another layer, follow these steps:

1. Select the object.
2. Click on one of the symbols in the toolbar for moving the object.

The object is assigned to the selected layer, and brought to the front.

Alternatively, select the object from the "Layout" task card and drag-and-drop it to the required layer.

##### Symbols for moving the object to a layer

| Symbol | Meaning |
| --- | --- |
| ![Symbols for moving the object to a layer](images/166171418123_DV_resource.Stream@PNG-de-DE.png) | The object is moved one layer to the front, for example, from layer 0 to layer 1. |
| ![Symbols for moving the object to a layer](images/166171422219_DV_resource.Stream@PNG-de-DE.png) | The object is moved one layer back, e.g. from layer 1 to layer 0. |

#### Moving objects in the screen (RT Unified)

##### Introduction

There are various ways in which you can move objects individually or with a multiple selection.

##### Requirement

- The HMI screen is open with at least one object.

##### Move objects

To move the objects, follow these steps:

1. Select the object that you want to move.
2. The following options are available for moving:

   - Moving by selecting and dragging with the mouse.
   - Moving using the arrow keys on your keyboard with pixel accuracy.
   - Coarser move using <Shift> and the arrow keys on your keyboard. The increment depends on the settings that you have configured for the grid under "Options > Settings > Visualization > Screens > Grid".

The same principle also applies to multiple selection of the objects.

##### Automatic scrolling

If you drag-and-drop the object to one of the corners of the screen, automatic scrolling is triggered. You can place the object in other areas of the screen.

#### Rotating an object around a pivot point (RT Unified)

##### Introduction

You define the rotation of an object around a pivot point. In the Inspector window of an object, specify the coordinates of the "Pivot point X" and "Pivot point Y". Specify the angle of rotation for the object under "Properties > Rotation - angle".

The pivot point can be outside the object.

##### Requirement

- The HMI screen containing at least one object group is open.

##### Rotation

Defines the rotation of an object around the pivot point. Rotation is specified in degrees. The configured start point corresponds to a value of 0°. The position of an object deviates from its configured initial position by the rotation value. The negative and positive values are allowed.

You can also place an object outside the visible plant complex. You can view objects outside the visible area by using the "Layout > Objects out of range" task card. You change the position of an object in the Inspector window under "Properties".

##### Pivot point

Define the pivot point under "Properties > Rotation - Pivot point":

- Absolute to the center point: Sets the rotation to around the absolute center of the object.
- Absolute to screen: Sets the rotation to around the absolute zero point of the screen. The zero point is in the top left corner of the screen.

##### Rotation position

The attributes "X pivot point" and "Y pivot point" define the horizontal and vertical distance of the pivot point from the point of origin.

- Center point of the object
- Zero point of the screen

The values are specified as a device-independent pixel (DIP).

The pivot point can also be located outside the bounding box. The negative and positive values are allowed.

##### Example: Configuring rotation for a rectangle

To configure the rotation of a rectangle, follow these steps:

1. Open the "Basic objects" palette in the "Toolbox" task card.
2. Drag the "Rectangle" object into the screen.
3. Click "Properties > Pivot point" in the Inspector window.
4. In the "Static value" column, select "Absolute to center point".
5. Enter a value of 45 for "Rotation".

The object is rotated clockwise by 45°.

### Designing colors (RT Unified)

This section contains information on the following topics:

- [Designing the background color (RT Unified)](#designing-the-background-color-rt-unified)
- [Defining color gradients (RT Unified)](#defining-color-gradients-rt-unified)
- [Central color management (RT Unified)](#central-color-management-rt-unified)

#### Designing the background color (RT Unified)

##### Introduction

You can design the background color of an object. For certain objects, you can define a background with a color gradient.

##### Requirement

- The HMI screen is open with at least one object.

##### Designing the background color of an object

To design the background color of an object, follow these steps:

1. In the Inspector window, click "Properties > Properties > Appearance > Background - color".
2. Select a color for the background of the object, for example, yellow.

| Symbol | Meaning |
| --- | --- |
| ![Designing the background color of an object](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Efficiency tip** |
| Using multiple selection, you can define the background color simultaneously in multiple objects. |  |

##### Result

The object is filled with the selected color.

#### Defining color gradients (RT Unified)

##### Introduction

You can define different color gradients for the objects. Change the category in the Inspector window, depending on which surface you fill with a color gradient.

##### Requirement

- The HMI screen is open with at least one object.

##### Configure horizontal color gradient with two colors

To configure a horizontal color gradient for an object, follow these steps:

1. Select an object, e.g. rectangle.
2. In the Inspector window, select "Horizontal gradient" under "Properties > Background - fill pattern".
3. Go to "Properties > Fill direction" and select the direction in which the color is to run, for example "Left to right".
4. Select a background color for the horizontal color gradient, e.g. orange, under "Properties > Background - color".
5. Select the other color for the gradient, e.g. yellow, under "Properties > Background - alternative color".

   ![Configure horizontal color gradient with two colors](images/100726610315_DV_resource.Stream@PNG-de-DE.png)

   ![Configure horizontal color gradient with two colors](images/100726610315_DV_resource.Stream@PNG-de-DE.png)

##### Result

The background of the rectangle is displayed with a color gradient of orange to yellow.

#### Central color management (RT Unified)

This section contains information on the following topics:

- [Basic principles for central color management (RT Unified)](#basic-principles-for-central-color-management-rt-unified)
- [Changing the object color (RT Unified)](#changing-the-object-color-rt-unified)

##### Basic principles for central color management (RT Unified)

###### Introduction

In WinCC Unified, you can change the colors that are used in a project in a centralized manner.

###### Requirement

- You have created a project.
- You have created a screen.

###### Opening the "Change object color" dialog box

You open the "Change object color" dialog box:

- In the shortcut menu of a device or object
- In the menu bar under "Tools > Change object color"

  ![Opening the "Change object color" dialog box](images/152158155659_DV_resource.Stream@PNG-en-US.png)

###### Using the "Change object color" dialog box

The "Change object color" dialog box contains a hierarchical overview of all color-relevant object properties.

In the display, you can navigate within the display and operating objects. You will receive an overview of all colors in use. You specify a color selection and replace it with other colors.

![Using the "Change object color" dialog box](images/156823896075_DV_resource.Stream@PNG-en-US.png)

###### Unsupported objects

You have access to all colors used and configured in the project with the "Change object color" dialog.

Excluded from this are colors that are used:

- In types and instances from a library
- In scripts
- In designs
- In screens with write protection

---

**See also**

[Changing the object color (RT Unified)](#changing-the-object-color-rt-unified)

##### Changing the object color (RT Unified)

###### Introduction

The scope of the objects displayed in the "Change object color" dialog depends on the location at which the dialog is called:

- If you select a device and call the dialog, all color references used on the device are displayed.
- If you select an object within a screen and call the dialog, only those color references that are included in the object are displayed.

###### Requirement

- You have created a project.
- You have created a screen.
- At least one object has been created in the screen.

###### Opening the "Change object color" dialog box

To change the object color, follow these steps:

1. Select the object that contains the required color references.
2. Select "Change object color" in the shortcut menu of the object.

   The "Change object color" dialog box opens.

![Opening the "Change object color" dialog box](images/152138940939_DV_resource.Stream@PNG-en-US.png)

###### Select the color you want to change

The following table shows you the options for choosing the color you want to change:

| Symbol | Meaning |
| --- | --- |
| Select the object property whose color you want to change. | - Select a property directly in the overview. - Enter a property in the "Property filter" dialog.  The selected property is now visible in the overview table. |
| In the "Color" text box, select the color that you want to change. | | Symbol | Meaning | | --- | --- | | 1. Click on the arrow in the "Color" text box. The project color selection opens. 2. Select a standard color.  To select a user-defined color, click "More colors". |  | |
| Select the color directly from the selected object. | | Symbol | Meaning | | --- | --- | | 1. Drag a color box from the "Current color" column to the "Color" text box. |  | |

###### Change color

To change a color, proceed as follows:

1. Select the color you want to change as described above.
2. To display the current selection, enable one or both of the options "Matching" and "Non-matching".
3. To select similar colors as well, set the tolerance. Enable the "HSL tolerance method" option.

   In the "Colors found" text box, you will see the number of similar colors.
4. In the "Replace with" text box, select a color.
5. Select one of the buttons:

   - "Replace the color of the selected object"
   - "Replace the color of the matching objects"

   The selected color is displayed in the "Replace with" column.
6. Click "OK".

   The dialog closes. The colors in the object are changed.

###### Result

You have configured new color references in the selected object.

### Formatting text in the object (RT Unified)

This section contains information on the following topics:

- [Enter text directly into the object (RT Unified)](#enter-text-directly-into-the-object-rt-unified)
- [Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)
- [Show default entry of text and graphic list in the object (RT Unified)](#show-default-entry-of-text-and-graphic-list-in-the-object-rt-unified)
- [Displaying tag value in the object dynamically (RT Unified)](#displaying-tag-value-in-the-object-dynamically-rt-unified)

#### Enter text directly into the object (RT Unified)

##### Introduction

You can change the label of the "Text box" and "Button" objects directly via the keyboard.

##### Requirement

- The HMI screen with a text box or a button is open.

##### Entering text directly into the object

To enter text directly in a text box or a button, follow these steps:

1. Select the object that you want to label.
2. Double-click in the object and type the text.

The text has been entered into an object.

##### Special features of direct text input

The following special features apply to direct input:

- Diacritics, such as ä ê ñ, can only be entered if the keyboard layout provides a key for this character. Key sequences such as <`a> for à, are not recognized.
- It is not possible to enter Unicode characters using Alt codes.
- Asian language characters cannot be entered using an Input Method Editor (IME).

If you need such characters in labeling the object, you have the following options:

- Use a keyboard layout on which this character is present as a key.
- Copy the character or full label from any source. Paste the text into the selected object.
- Edit the label in the Inspector window under "Properties > Properties > General > Text".

Direct text entry also supports multiline text. Enter the line break using the <Shift + Return> shortcut.

---

**See also**

[Text box (RT Unified)](#text-box-rt-unified)
  
[Button (RT Unified)](#button-rt-unified)

#### Entering multiline text (RT Unified)

##### Introduction

For objects with the "Text" property, you can enter the text on multiple lines.

##### Requirement

- The HMI screen with at least one object with the "Text" property is open.

##### Enable line break

Enter the line break using the <Shift + Return> shortcut.

##### Multiple line text for objects

Enter the multiple line text for the following objects in the Inspector window under "Properties > Properties > General > Text":

- Text box
- Button
- Switch

  ![Multiple line text for objects](images/148509488395_DV_resource.Stream@JPG-en-US.jpg)

Enter the multiple line text for the following objects under "Properties > Properties > General > Title > Text".

The text may only contain 2 lines at a time.

- Bar
- Slider

For the following objects, enter the multiple line text under "General > Selection items > [x] Selection item> Text".

The text may contain more than 2 lines if the property "Format > Item height" is adjusted accordingly.

- Check box
- Radio button
- List box

You can use multiple line texts with a maximum of two lines in the text list for symbolic IO fields.

##### Alternatively, enter the multiple line text

Alternatively, enter the multiple line text:

- In the Inspector window, under "Properties > Text".

  Enter the line break using the <Shift + Return> shortcut. A line break is displayed as a blank.

  ![Alternatively, enter the multiple line text](images/148511360395_DV_resource.Stream@PNG-en-US.png)
- By entering text directly into the object for:

  - Text box
  - Button

#### Show default entry of text and graphic list in the object (RT Unified)

##### Introduction

For objects with the dynamization type "Resource list", you can have a text or a graphic from the resource list displayed as the default entry in the object.

##### Requirement

- The HMI screen with an object, e.g. a button, is open.
- At least one object property supports the "Resource list" dynamization type, for example, "text" or "graphic".

##### Displaying a text as the default entry in the object

To display a text as the default entry in the object, follow these steps:

1. In the Inspector window, select "Properties > Properties > General > Text".
2. Select "Resource list" in the "Dynamization" column.
3. In the "Resource list" dialog, select a text list under "Settings > Resource list".
4. Click on the button in the "Resource list" line ![Displaying a text as the default entry in the object](images/148458605323_DV_resource.Stream@PNG-de-DE.png).   
   The selected text list opens.
5. Select an entry in the "Text list entries" table as the default entry. The text from the default entry is displayed in the object.  
   If you have not specified a default entry, the first entry in the "Text" column is displayed in the object.

##### Displaying a graphic as the default entry in the object

To display a graphic as the default entry in the object, follow these steps:

1. In the Inspector window, select "Properties > Properties > General > Graphic".
2. Select "Resource list" in the "Dynamization" column.
3. In the "Resource list" dialog, select a graphic list under "Settings > Resource list".
4. Click on the button in the "Resource list" line ![Displaying a graphic as the default entry in the object](images/148458605323_DV_resource.Stream@PNG-de-DE.png).   
   The selected graphic list opens.
5. Select an entry in the "Graphic list entries" table as the default entry. The graphic from the standard entry is displayed in the object.  
   If you have not specified a default entry, the first entry in the "Graphic" column is displayed in the object.

---

**See also**

[Configuring object with a text list (RT Unified)](#configuring-object-with-a-text-list-rt-unified)

#### Displaying tag value in the object dynamically (RT Unified)

##### Introduction

In some objects, dynamic information can be displayed in the properties that contain a text.

If you insert the reference to a tag in the "Text" or "Tooltip" property, for example, the current value of the inserted tag is displayed in the object in Runtime.

Supported objects:

- Text box
- Button
- Symbolic IO field
- Switch

In the message texts, e.g. in the alarm control, the dynamic information may already be inserted.

> **Note**
>
> Local session tags are not supported as a source for the dynamic information.

##### Requirement

- The HMI screen with an object, e.g. a text box or a button, is open.

##### Configuring a tag value in the object

To configure a tag value in an object, e.g. in a text box, follow these steps:

1. Configure a tag, e.g. "IntTag".
2. In the Inspector window, select "Properties > Properties > General > Text".
3. Enter a text in the "Static value" column in the input field, e.g. "IntTag_Value".
4. Right-click in the input field. The shortcut menu opens.

   ![Configuring a tag value in the object](images/160392767499_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a tag value in the object](images/160392767499_DV_resource.Stream@PNG-en-US.png)
5. Select "Insert parameter field" in the shortcut menu. A dialog opens.

   ![Configuring a tag value in the object](images/160392778379_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a tag value in the object](images/160392778379_DV_resource.Stream@PNG-en-US.png)
6. Select the "IntTag" tag under "Tag" in the dialog.
7. Configure the format of the display:

   - Display type
   - Length
   - Decimal places
   - Alignment:
   - Leading zeros
8. Confirm the selection. The field with the tag name becomes visible in the input field.

   ![Configuring a tag value in the object](images/160394549387_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a tag value in the object](images/160394549387_DV_resource.Stream@PNG-en-US.png)
9. Compile and load the device.

> **Note**
>
> If you have inserted the parameter field with a tag in an object, you cannot edit the text in the object directly. After deleting the parameter field, you can edit the text in the object directly again.
>
> More information on direct text input is available in [Enter text directly into the object](#enter-text-directly-into-the-object-rt-unified).

##### Result

The object displays the current tag value in Runtime.

### Linking objects (RT Unified)

This section contains information on the following topics:

- [Linking an object to a text list (RT Unified)](#linking-an-object-to-a-text-list-rt-unified)
- [Linking an object to a graphic list (RT Unified)](#linking-an-object-to-a-graphic-list-rt-unified)
- [Linking an object to tags (RT Unified)](#linking-an-object-to-tags-rt-unified)

#### Linking an object to a text list (RT Unified)

##### Introduction

You can link the objects to a text list.

##### Requirement

- The HMI screen with an object is open.

##### Linking objects to a text list

You can link a text list to the following objects:

- Text box
- Button
- Switch
- Symbolic IO field

To link a text list to an object, follow these steps:

1. In the Inspector window, select "Properties > Properties > General > Text".
2. Select the "Resource list" option in the "Dynamization" column. The "Resource list" page opens.
3. Select the text list from which the text is displayed.

The text list has been linked to an object.

| Symbol | Meaning |
| --- | --- |
| ![Linking objects to a text list](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| - Use drag-and-drop to move a text list from the detail view of the text and graphic lists directly onto an object in a screen. The object is linked to the text list. |  |

#### Linking an object to a graphic list (RT Unified)

##### Introduction

You can link the objects to a graphic list.

##### Requirement

- The HMI screen with an object is open.

##### Linking objects to a graphic list

You can link a graphic list to the following objects:

- Graphic view
- Button
- Switch
- Symbolic IO field

To link a graphic list to an object, follow these steps:

1. In the Inspector window, select "Properties > Properties > General > Graphic".
2. Select the "Resource list" option in the "Dynamization" column. The "Resource list" page opens.
3. Select the graphic list from which the graphic is displayed.

The graphic list has been linked to an object.

| Symbol | Meaning |
| --- | --- |
| ![Linking objects to a graphic list](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| - Use drag-and-drop to move a graphic list from the detail view of the text and graphic lists directly onto an object in a screen. The object is linked to the graphic list. |  |

#### Linking an object to tags (RT Unified)

##### Introduction

You can link the objects to a tag.

##### Requirement

- The HMI screen with an object is open.

##### Link objects to a tag

You can link a tag to the following objects:

- Text box
- IO field
- Symbolic IO field
- List box
- Bar
- Slider
- Gauge
- Clock
- Check box
- Radio button
- Trend control
- Process control

To link a tag with an object, proceed as follows:

1. In the Inspector window, select "Properties > Properties > General > Process value".
2. Select "Tag" in the "Dynamization" column. The "Tag" page will open.
3. Select an existing tag under "Tag > Process > Tag".

   Alternatively, create a new tag using the "Add" button.

The tag has been linked to an object.

| Symbol | Meaning |
| --- | --- |
| ![Link objects to a tag](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| - Drag a tag from the detail view of the tag table directly to an object in a screen. The object is linked to the tag. |  |

### Using layers (RT Unified)

This section contains information on the following topics:

- [Basic information on using layers (RT Unified)](#basic-information-on-using-layers-rt-unified)
- [Renaming a layer (RT Unified)](#renaming-a-layer-rt-unified)
- [Moving objects between layers (RT Unified)](#moving-objects-between-layers-rt-unified)
- [Specifying the active layer (RT Unified)](#specifying-the-active-layer-rt-unified)
- [Hiding and showing layers (RT Unified)](#hiding-and-showing-layers-rt-unified)
- [Toggle the visibility of layers in runtime in the ES (RT Unified)](#toggle-the-visibility-of-layers-in-runtime-in-the-es-rt-unified)
- [Toggling the visibility of layers in runtime using the JScript function (RT Unified)](#toggling-the-visibility-of-layers-in-runtime-using-the-jscript-function-rt-unified)

#### Basic information on using layers (RT Unified)

##### Layers

Use layers in order to achieve differentiated editing of the objects in a screen. Using layers, multiple objects can be combined and edited together, for example. Layers are also used to improve clarity during configuring, because multiple objects can be hidden and displayed again when required.

A screen has 32 layers. The name of the individual layers is determined by the user interface language and changes when the user interface language is changed. If you assign objects to the layers, you thereby define the screen depth. Objects of layer 0 are located in the screen background, while objects of layer 31 are located in the foreground.

![Layers](images/123407460491_DV_resource.Stream@PNG-en-US.png)

The objects of a single layer are also arranged hierarchically. If you create a new object, it is arranged in the foreground. You can shift objects forwards and backwards within a layer.

##### Principle of the layer technique

Always one layer of the 32 layers is active. New objects you add to the screen are always assigned to the active layer. The active layer is indicated in the "Layout > Layers" task card.

When you open a screen, all 32 layers of the screen are displayed. You can hide all layers except for the active layer in the "Layout > Layers" task card. You then explicitly edit objects of the active layer.

In the "Layout > Layers" task card, you can also manage layers and objects with drag-and-drop and the shortcut menu.

##### Application examples

Use layers, for example, in the following cases:

- To hide the labeling of objects when editing,
- To hide individual objects, while you configure other objects

#### Renaming a layer (RT Unified)

##### Introduction

When you create a screen, the 32 layers are numbered consecutively by default. To improve clarity, you can rename the layers to suit your requirements.

##### Requirement

- A screen with an object is open.

##### Renaming a layer

To rename the name of a layer, follow these steps:

1. Click on Runtime settings in the project tree.
2. In the "Name" column, click in the row of the layer.
3. Enter a name.

![Renaming a layer](images/157639783819_DV_resource.Stream@PNG-en-US.png)

##### Result

The selected layer has been renamed.

#### Moving objects between layers (RT Unified)

##### Introduction

By default, newly inserted objects are in the foreground of the active layer. You can assign an object to a different layer and change the order of objects within a layer at a later time.

##### Requirement

- There is a screen open with at least one object.

##### Moving objects between layers

To move the objects, follow these steps:

1. Select the object in the "Layout > Layers" task card.
2. Drag-and-drop the object to the required layer.

##### Moving objects to another layer in the Inspector window

To move the objects to another layer in the Inspector window, follow these steps:

1. In the drop-down list under "Properties > Miscellaneous > Layer", select the layer to which you want to move the object.

   Alternatively, you can enter the name of the layer in the input field.

   ![Moving objects to another layer in the Inspector window](images/168361676939_DV_resource.Stream@PNG-en-US.png)

   ![Moving objects to another layer in the Inspector window](images/168361676939_DV_resource.Stream@PNG-en-US.png)

You can also use multiple selection to move several objects to a layer.

##### Changing the order of objects within a layer

To change the sequence of objects, follow these steps:

1. Select the object in the screen.
2. Select the desired command under "Arrange" in the shortcut menu. Depending on the current position of the object, you can move it completely into the foreground, to the front, to the back or completely into the background.

##### Result

The object is arranged according to the selection. In the "Layout > Layers" task card, the order of the objects is displayed as follows: Objects of layer 0 are located in the screen background, while objects of layer 31 are located in the foreground. Within a layer, the objects displayed at the top of the list are in the background of the layer.

#### Specifying the active layer (RT Unified)

##### Introduction

The screen objects are always assigned to one of the 32 layers. There is always an active layer in the screen. New objects you add to the screen are always assigned to the active layer.

The active layer is indicated by a ![Introduction](images/123408364299_DV_resource.Stream@PNG-de-DE.png) icon in the "Layout > Layers" task card.

You can activate a different layer during configuration, if necessary.

##### Requirement

- You have opened a screen which contains at least one object.

##### Procedure

To set a layer as active, follow these steps:

1. Select "Layout > Layers" in the "Layout" task card.
2. Select the "Set to active" command from the shortcut menu of a layer.

##### Result

The selected layer becomes the active layer.

#### Hiding and showing layers (RT Unified)

##### Introduction

You can show or hide the layers of a screen as required.

##### Requirement

- The screen is open.

##### Hiding or showing layers

To hide or show layers, follow these steps:

1. Select the layer that you want to hide or show in the "Layout > Layers" task card.
2. Click one of the icons next to the corresponding layer:

- ![Hiding or showing layers](images/123409730187_DV_resource.Stream@PNG-de-DE.png) A shown layer is hidden.
- ![Hiding or showing layers](images/123410237963_DV_resource.Stream@PNG-de-DE.png) A hidden layer is shown.

You cannot hide the active layer.

Alternatively, select the "Hide layer" or "Show layer" command from the shortcut menu of a layer.

##### Result

Only the displayed layers are shown in the Engineering System.

Setting the visibility of the levels in the Engineering System has no influence on the visibility of the levels in Runtime.

#### Toggle the visibility of layers in runtime in the ES (RT Unified)

##### Introduction

You can toggle the visibility of layers in runtime in the Engineering System.

##### Requirement

- The screen is open.

##### Toggling the visibility of layers in the Engineering System

To switch the visibility of layers in runtime in the Engineering System, follow these steps:

1. In the Inspector window, select "Properties > Properties, Miscellaneous > Layers".
2. Select the layer whose runtime visibility you want to toggle.
3. Under "Miscellaneous > Levels > [x] Level", select the "Runtime visible" option in the "Static value" column.

   ![Toggling the visibility of layers in the Engineering System](images/160251664907_DV_resource.Stream@PNG-en-US.png)

   ![Toggling the visibility of layers in the Engineering System](images/160251664907_DV_resource.Stream@PNG-en-US.png)
4. If you now click on the field "Layers" under "Miscellaneous", the overview of all layers becomes visible in the right part of the Inspector window.

   You can toggle the visibility directly in the overview.

##### Result

You can now toggle the visibility of the layers in Runtime.

Only the displayed layers are shown in the Engineering System.

Setting the visibility of the levels in runtime has no influence on the visibility of the levels in the Engineering System.

#### Toggling the visibility of layers in runtime using the JScript function (RT Unified)

##### Introduction

You can toggle the visibility of layers in runtime using the JScript function.

##### Requirement

- The screen is open.

##### Toggling the visibility of layers via the JScript function

To toggle the visibility of the layers in runtime using a JScript function, follow these steps:

1. In the Engineering System, place the objects of a screen in the "Layout" task card on different layers.
2. Program a JScript function to change the visibility of, for example, "Layer_1" in the current screen.  
   `Screen.Layers ("Layer_0").Visible = false;`
3. Configure this function, e.g. on an event of a button.

If the event occurs in runtime, all objects placed on this layer become invisible.

To make a layer visible in the current screen, use: `Screen.Layers("Layer_0").Visible = true;`

##### Result

You can change the visibility of the layers in Runtime.

### Two-hand operation of operator controls (RT Unified)

This section contains information on the following topics:

- [Two-hand operation of operator controls (RT Unified)](#two-hand-operation-of-operator-controls-rt-unified-1)
- [Locking and unlocking operator controls (RT Unified)](#locking-and-unlocking-operator-controls-rt-unified)
- [Configuring the release button in the screen (RT Unified)](#configuring-the-release-button-in-the-screen-rt-unified)

#### Two-hand operation of operator controls (RT Unified)

##### Introduction

WinCC supports two-hand operation of operator controls for Unified PC. It ensures safe operation of operator controls which are used to change critical system settings, for example, control tags with machine limits.

##### Locked and unlocked operator controls

You define specific operator controls as "locked operator controls" for two-hand operation of operator controls. Locked operator controls usually cannot be operated in runtime. Operators can only operate the locked operator controls when they press a release button at the same time.

In runtime, locked operator controls can only be accessed with the tab sequence when a release button is pressed at the same time.

##### Locked operator controls and release buttons

You can configure all operator controls as locked.

You must configure at least one button in the screens as release button. This can be any unlocked button. The unlocking of locked operator controls by pressing the release button has an effect on all open screens.

##### Display in runtime

The locked operator controls are displayed as dimmed in runtime. The locked operator controls are completely visible when they are unlocked by means of the release button.

##### Simulation of projects with multi-touch functions

WinCC supports the simulation of configured multi-touch functions. Requirement is that your monitor supports multi-touch operation.

#### Locking and unlocking operator controls (RT Unified)

You can lock and unlock operator controls in projects for multi-touch devices. Locked operator controls can only be operated in runtime when the operator presses a release button at the same time.

You can lock and unlock individual operator controls or several operator controls simultaneously.

##### Procedure

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

##### Defining the release button

To use the locked operator controls, you must configure at least one release button in one of the displayed screens.

#### Configuring the release button in the screen (RT Unified)

So that you can operate locked operator controls on multi-touch devices, configure a release button.

##### Procedure

1. Select the screen.
2. Select the desired button of the screen under "Properties > Security" under "Enable explicit unlock".

   ![Procedure](images/142819085195_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142819085195_DV_resource.Stream@PNG-en-US.png)
3. To turn a release button back into a normal button, select a different button or "None" under "Properties > Security" under "Enable explicit unlock".

## Using groups (RT Unified)

This section contains information on the following topics:

- [Basics of groups (RT Unified)](#basics-of-groups-rt-unified)
- [Grouping objects (RT Unified)](#grouping-objects-rt-unified)
- [Managing groups (RT Unified)](#managing-groups-rt-unified)
- [Managing objects in groups (RT Unified)](#managing-objects-in-groups-rt-unified)
- [Managing group properties (RT Unified)](#managing-group-properties-rt-unified)

### Basics of groups (RT Unified)

#### Introduction

You can put two or more objects together to form a group with the "Group" function.

You can manage a group of objects in the Engineering System and in Runtime just like you manage an individual object, e.g. you can change the color or visibility of all grouped objects in one step.

Grouping is available on a Unified PC and Unified Control Panel as of version V18. The grouping of objects is not supported in the VoT application.

#### Editing objects together

You can edit multiple objects together by means of:

- [Multiple selection](#select-multiple-objects-rt-unified): With multiple selection, the bounding boxes of all objects are displayed.
- [Grouping objects](#grouping-objects-rt-unified): With a group, one bounding box is displayed for the whole group.

#### Groupable objects

You can add the following objects to a group:

- Basic objects
- Elements
- Faceplate containers
- Graphics
- Dynamic widgets

Nesting of groups – group in group – is not supported.

#### Non-groupable objects

You cannot add the following objects to a group:

- Controls (except faceplate containers)
- Custom controls

#### Layers

All objects of a group are located in the same layer. The groups are arranged hierarchically in a layer.

You can also add objects to a group or remove them from a group in the "Layout > Layers" task card using drag-and-drop.

#### Properties of a group

- The group has its own coordinate system. The coordinates of all objects contained in the group are referenced to the upper left corner of the group.
- Each group has its own properties. You can define the properties of a group for the runtime:

  - Via a dynamic property.
  - Via a script.
- If you set a property for a group, all objects of the group inherit this property.
- If you configure the same property differently on an object in the group, the property value on the object is valid in runtime, not the value in the group.
- When you resize an object, the group is also resized.
- The grouping of objects is also possible within faceplate types.
- Groups have no events for which you can configure event scripts or function lists. The events of the objects in the group work in the same way as for objects that are not grouped.
- Nesting of groups – group in group – is not supported.

### Grouping objects (RT Unified)

#### Introduction

The "Group" menu command combines multiple objects to form a group.

#### Requirement

- A screen containing at least two objects is open.

#### Grouping objects

Follow these steps to group objects:

1. Select all the objects you want to group using multiple selection.

   ![Grouping objects](images/156789394955_DV_resource.Stream@PNG-de-DE.png)

   ![Grouping objects](images/156789394955_DV_resource.Stream@PNG-de-DE.png)
2. Select the "Group > Group" command from the shortcut menu.

   ![Grouping objects](images/156789403531_DV_resource.Stream@PNG-en-US.png)

   ![Grouping objects](images/156789403531_DV_resource.Stream@PNG-en-US.png)
3. The group objects are displayed with a bounding box.

   ![Grouping objects](images/156789516299_DV_resource.Stream@PNG-de-DE.png)

   ![Grouping objects](images/156789516299_DV_resource.Stream@PNG-de-DE.png)

#### Result

The selected objects are combined in a group. The multiple selection bounding box becomes the group bounding box. The resizing handles are shown only for the group.

The group is in the active layer.

The group is given a unique default name, e.g. "Group_1".

The coordinates of the upper left corner of the group are defined in such a way that the position of the objects contained in the group remains unchanged in the screen. The height and width of the group is defined to accommodate the full extent of the objects contained in the group.

### Managing groups (RT Unified)

This section contains information on the following topics:

- [Selecting a group (RT Unified)](#selecting-a-group-rt-unified)
- [Changing the size of the group (RT Unified)](#changing-the-size-of-the-group-rt-unified)
- [Copying and pasting a group (RT Unified)](#copying-and-pasting-a-group-rt-unified)
- [Ungrouping a group (RT Unified)](#ungrouping-a-group-rt-unified)
- [Moving a group (RT Unified)](#moving-a-group-rt-unified)
- [Moving groups between layers (RT Unified)](#moving-groups-between-layers-rt-unified)
- [Group in editing mode (RT Unified)](#group-in-editing-mode-rt-unified)
- [Rotating a group and objects in the group (RT Unified)](#rotating-a-group-and-objects-in-the-group-rt-unified)

#### Selecting a group (RT Unified)

##### Introduction

You can select a group and further edit it.

##### Requirement

- A screen containing at least one group of objects is open.

##### Selecting a group

To select a group, choose one of the following options:

- Click on an object in the group.

  The group is selected.

  ![Selecting a group](images/169749887243_DV_resource.Stream@PNG-de-DE.png)
- If the whole group is visible in the "Screens" editor, you can also select the group by drawing a lasso around it.

##### Ungrouping a group

To ungroup a group, follow these steps:

1. Select the group.
2. Right-click to open the shortcut menu.
3. In the shortcut menu, select the "Group > Ungroup" command.

The group is ungrouped. The objects from the group remain in the screen.

#### Changing the size of the group (RT Unified)

##### Introduction

You can change the size of an object group in the Engineering System.

When you select the group, it is framed by a bounding box with blue handles. You have the following options for changing the size and position of a group:

- Drag with the mouse
- Configure group properties

After the size of the group has been changed, the objects contained in the group are scaled proportionally to their original size and the target size.

##### Requirement

- The HMI screen containing at least one object group is open.

##### Changing the size of the group with the mouse

To change the size of the group with the mouse, follow these steps:

1. Select the group whose size you want to change.

   The bounding box is displayed.
2. Drag a handle of the box to a new position.

The size of the group is changed.

| Symbol | Meaning |
| --- | --- |
| ![Changing the size of the group with the mouse](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| If you press the <Shift> key while dragging, the group is resized according to the aspect ratio. |  |

> **Note**
>
> - Circular objects, such as circles, circular arcs, circle segments, gauges, and clocks, are only resized if both dimensions are changed at the same time by dragging one of the corner handles. If the size of the group is not adapted proportionally, the circular objects cannot be displayed correctly.
> - If a group was first significantly reduced in size and then enlarged again, the objects in it may shift or reshape due to precision losses.

##### Configuring the size of the group through properties

To change the size of the group through properties, follow these steps:

1. Select the group whose size you want to change.
2. Select "Properties" > "Properties" > "Size and position".
3. In the "Static value" column, enter the "Size - width" and "Size - height" coordinates.

The object size is changed.

#### Copying and pasting a group (RT Unified)

##### Introduction

You can copy and paste a group.

##### Requirement

- A screen containing at least one group of objects is open.

##### Copying and pasting a group

To copy a group, choose one of the following options:

- Right-click the group in the "Layers" task card. Select "Copy" and "Paste" in the shortcut menu.

  ![Copying and pasting a group](images/169750989707_DV_resource.Stream@PNG-en-US.png)
- Select the group. Copy the group with <Ctrl + C> and paste it with <Ctrl + V>.

You can paste the copied group:

- In the same screen
- In a different screen
- On another Unified device

> **Note**
>
> References in function lists or scripts to other objects in the group are kept as the original reference.
>
> Example:
>
> - Group_1 contains Button_1 and Circle_1.
> - Button_1 has a script that references Circle_1.
> - After copying and pasting, the copied Group_2 contains Button_2 and Circle_2.
> - The script on Button_2 continues to reference Circle_1.

#### Ungrouping a group (RT Unified)

##### Introduction

You can ungroup a group.

##### Requirement

- A screen containing at least one group of objects is open.

##### Ungrouping a group

To ungroup a group, follow these steps:

1. Select the group.
2. Right-click to open the shortcut menu.

   ![Ungrouping a group](images/169820243467_DV_resource.Stream@PNG-en-US.png)

   ![Ungrouping a group](images/169820243467_DV_resource.Stream@PNG-en-US.png)
3. In the shortcut menu, select the "Group > Ungroup" command.

The group is ungrouped. The objects from the group remain in the screen.

#### Moving a group (RT Unified)

##### Introduction

You can move an object group in various ways.

##### Requirement

- The HMI screen containing at least one object group is open.

##### Moving an object group

To move the object group, follow these steps:

1. Select the object group you want to move.
2. The following options are available for moving:

   - Moving by selecting and dragging with the mouse.
   - Moving with pixel accuracy using the arrow keys on your keyboard.
   - Moving in larger pixel increments using <Shift> and the arrow keys on your keyboard. The increment depends on the settings you configured for the grid under "Options > Settings > Visualization > Screens > Grid".

#### Moving groups between layers (RT Unified)

##### Introduction

You can move groups between layers in the "Layout > Layers" task card and change the order of groups within a layer.

The objects in the groups are moved to the same layer as the parent group and keep their order.

##### Requirement

- The HMI screen containing at least one object group is open.

##### Moving groups between the layers

You have the following options for moving one or more groups between the layers:

- Moving one group to another layer using drag-and-drop
- Selecting the "Arrange" command in the shortcut menu of the group, and then selecting:

  - "Bring to front"
  - "Bring forward"
  - "Send backward"
  - "Send to back"
- Moving multiple groups using multiple selection and drag-and-drop.

> **Note**
>
> Moving of groups is only possible if no objects contained in the group have been selected.

#### Group in editing mode (RT Unified)

##### Introduction

You can configure the individual objects in the group in editing mode.

When you select an object within the group, the group goes into editing mode. When the group is in editing mode, it is framed by a red rectangle.

![Introduction](images/169824245387_DV_resource.Stream@PNG-de-DE.png)

##### Requirement

- The HMI screen containing at least two objects is open.
- The objects have been put together to form a group.

##### Activating editing mode

To activate editing mode for a group, choose one of the following options:

- Click an object in the group with the left mouse button. Select "Group > Edit group" in the shortcut menu.
- Double-click an object in the group.
- Select an object within a group by clicking on the object in the "Layout > Layers" task card.
- An object in the group can be selected through an error message, cross-reference or search result.

##### Options in editing mode

- When the group is in editing mode, you can select an object contained in the group by clicking it. The group remains in editing mode.
- If you select an object outside the group, the editing mode is deactivated.
- You can also select the following using multiple selection:

  - Multiple objects in a group.
  - Multiple groups in the screen.
- Direct text input: If you double-click an object in which a direct text input is possible, you can enter the text. If the group is not in editing mode, editing mode is activated.
- A rotated group is displayed as not rotated in editing mode. After editing mode is deactivated, the group is displayed rotated again. The configured value of the "Rotation - angle" property remains unchanged.

##### Configuring objects in editing mode

You can configure the objects in the group in editing mode in the following ways:

- Changing properties of the selected objects.
- Aligning or distributing objects or setting them to the same size.
- Adding or removing points of point-based objects, e.g. for polyline and polygon.
- Copying objects. When pasted, the objects are placed outside the group.
- Linking objects, e.g. with a tag, using drag-and-drop.

The group is updated after size or position changes of the objects it contains.

---

**See also**

[Aligning objects in the group (RT Unified)](#aligning-objects-in-the-group-rt-unified)

#### Rotating a group and objects in the group (RT Unified)

##### Introduction

You can rotate a group and the objects in the group.

You define the rotation of a group around a pivot point. You can specify the "Pivot point X" and "Pivot point Y" coordinates of the pivot point in the Inspector window of the group. You can specify the rotation angle for the rotation of the group under "Properties > Rotation - angle".

The pivot point can also be located outside the group.

##### Requirement

- The HMI screen containing at least one group is open.

##### Rotating a group

The rotation defines the rotation of the group around the pivot point. The value of the rotation is specified in degrees. The configured initial position corresponds to a value of 0°. The position of the group differs from its configured initial position by the rotation value. Negative and positive values are permissible.

##### Pivot point

Define the pivot point under "Properties > Rotation - pivot point":

- Absolute to center: Specifies that the rotation is an absolute rotation around the center point of the group.
- Absolute to screen: Specifies that the rotation is an absolute rotation around the zero point of the screen. In this case, the zero point is located at the top left corner of the screen.

##### Pivot point positioning

The attributes "Pivot point X" and "Pivot point Y" define the horizontal and vertical distance of the pivot point from the origin point.

- Center point of the group
- Zero point of the screen

The values are specified in device-independent pixels (DIP).

The pivot point can also be located outside the bounding box. Negative and positive values are permissible.

##### Result

The group is rotated. All objects in the group are rotated according the rotation of the group.

##### Rotated objects in the group

You have the following options:

- You can create a group of the rotated objects.
- You can rotate the objects in the group.

The pivot points X and Y are viewed relative to the group, if pivot point mode "Absolute to screen" is selected.

##### Limitations

- The rotation of objects contained in the group is not taken into account when calculating the group boundaries or when changing the size of a group.
- When you edit the objects in a rotated group, the group is displayed non-rotated while it is in editing mode. After editing mode is exited, the group is displayed rotated. The configured value of the "Rotation - angle" property remains unchanged.
- The rotation of a group is not taken into account when adding and removing objects to and from the group.
- Based on these limitations, the following is recommended:

  - Configuring a group and its objects without rotation.
  - Use a dynamic rotation in runtime when needed.

### Managing objects in groups (RT Unified)

This section contains information on the following topics:

- [Adding an object to the group (RT Unified)](#adding-an-object-to-the-group-rt-unified)
- [Aligning objects in the group (RT Unified)](#aligning-objects-in-the-group-rt-unified)
- [Moving an object in the group (RT Unified)](#moving-an-object-in-the-group-rt-unified)
- [Removing an object from the group (RT Unified)](#removing-an-object-from-the-group-rt-unified)
- [Deleting an object from the group (RT Unified)](#deleting-an-object-from-the-group-rt-unified)

#### Adding an object to the group (RT Unified)

##### Introduction

You can add one or more objects to a group.

The size of the group is automatically adapted after the addition of objects.

##### Requirement

- The HMI screen containing at least one object group is open.
- At least one object has been configured outside the group.

##### Adding an object to a group in the screen editor

To add an object to a group, follow these steps:

1. Select a group and one or more objects using multiple selection.
2. Click on the object you want to add.
3. Right-click to open the shortcut menu.

   ![Adding an object to a group in the screen editor](images/169830644107_DV_resource.Stream@PNG-en-US.png)

   ![Adding an object to a group in the screen editor](images/169830644107_DV_resource.Stream@PNG-en-US.png)
4. In the shortcut menu, select the "Group > Add to group" command.

   The object(s) are added to the group.

**Note**

If you have selected objects that are not supported, e.g. a control or another group, the command is hidden.

##### Adding an object in a layer to the group

You can also add the objects to a group in the "Layout > Layers" task card using drag-and-drop.

#### Aligning objects in the group (RT Unified)

##### Introduction

You can align the selected objects in relation to a reference object in a group.

The size of the group is automatically adapted after changing the position of the objects contained in the group.

##### Requirement

- The HMI screen containing at least two objects is open.
- The objects have been put together to form a group.

##### Aligning selected objects in a group

The reference object is the object that you selected first.

To align selected objects in a group in relation to a reference object, follow these steps:

1. Select the desired objects in the "Layout > Layers" task card.
2. Click on the bar above the toolbar.

   The icons in the toolbar are displayed.

   ![Aligning selected objects in a group](images/169759217291_DV_resource.Stream@PNG-en-US.png)

   ![Aligning selected objects in a group](images/169759217291_DV_resource.Stream@PNG-en-US.png)
3. Select the desired command for alignment in the toolbar.

   ![Aligning selected objects in a group](images/169759819403_DV_resource.Stream@PNG-en-US.png)

   ![Aligning selected objects in a group](images/169759819403_DV_resource.Stream@PNG-en-US.png)

The selected objects in the group are aligned in relation to the reference object.

---

**See also**

[Aligning objects (RT Unified)](#aligning-objects-rt-unified)
  
[Group in editing mode (RT Unified)](#group-in-editing-mode-rt-unified)

#### Moving an object in the group (RT Unified)

##### Introduction

You can move one or more objects in the group.

The size of the group is automatically adapted after changing the position of the objects contained in the group.

##### Requirement

- A screen containing at least one group of objects is open.

##### Moving an object within the group

To move an object within the group, follow these steps:

- Move the object in the group in the "Layout > Layers" task card using drag-and-drop.

  ![Moving an object within the group](images/169830469131_DV_resource.Stream@PNG-en-US.png)
- Double-click the object.

  Move the object directly in the group in the screen editor using drag-and-drop.

  ![Moving an object within the group](images/169830460555_DV_resource.Stream@PNG-de-DE.png)

#### Removing an object from the group (RT Unified)

##### Introduction

You can remove one or more objects from the group using multiple selection as follows:

- Drag the object onto a layer in the "Layout > Layers" task card.
- Drag the object onto another object outside the group.
- Remove the object via the shortcut menu in the screen editor.

A group may also contain a single object. If you remove the last object from the group, the group is automatically deleted.

The size of the group is automatically adapted after the removal of objects.

##### Requirement

- A screen containing at least one group of objects is open.

##### Dragging the object onto a layer

To drag an object onto a layer, follow these steps:

1. Select an object in the group, e.g. Button_1, in the "Layout > Layers" task card.

   ![Dragging the object onto a layer](images/169805871755_DV_resource.Stream@PNG-en-US.png)

   ![Dragging the object onto a layer](images/169805871755_DV_resource.Stream@PNG-en-US.png)
2. Move the object directly from the group onto a layer using drag-and-drop.

   ![Dragging the object onto a layer](images/169805880331_DV_resource.Stream@PNG-en-US.png)

   ![Dragging the object onto a layer](images/169805880331_DV_resource.Stream@PNG-en-US.png)
3. The object is removed from the group and placed in last position in the layer.

   ![Dragging the object onto a layer](images/169806080907_DV_resource.Stream@PNG-en-US.png)

   ![Dragging the object onto a layer](images/169806080907_DV_resource.Stream@PNG-en-US.png)

##### Dragging the object onto another object outside the group

To drag an object onto another object outside the group, follow these steps:

1. Select an object in the group, e.g. Button_1, in the "Layout > Layers" task card.

   ![Dragging the object onto another object outside the group](images/169805871755_DV_resource.Stream@PNG-en-US.png)

   ![Dragging the object onto another object outside the group](images/169805871755_DV_resource.Stream@PNG-en-US.png)
2. Move the object onto another object outside the group using drag-and-drop.

   ![Dragging the object onto another object outside the group](images/169806103051_DV_resource.Stream@PNG-en-US.png)

   ![Dragging the object onto another object outside the group](images/169806103051_DV_resource.Stream@PNG-en-US.png)
3. The object is removed from the group and placed in first position in the layer.

   ![Dragging the object onto another object outside the group](images/169806111627_DV_resource.Stream@PNG-en-US.png)

   ![Dragging the object onto another object outside the group](images/169806111627_DV_resource.Stream@PNG-en-US.png)

##### Removing the object via the shortcut menu in the screen editor

To remove an object via the shortcut menu in the screen editor, follow these steps:

1. Select an object in the group, e.g. Button_1, in the screen editor.
2. Right-click on the button.

   The shortcut menu opens.

   ![Removing the object via the shortcut menu in the screen editor](images/169807758603_DV_resource.Stream@PNG-en-US.png)

   ![Removing the object via the shortcut menu in the screen editor](images/169807758603_DV_resource.Stream@PNG-en-US.png)
3. Select "Group > Remove from group".

   The object is removed from the group and placed outside the group in the screen.

   ![Removing the object via the shortcut menu in the screen editor](images/169820234379_DV_resource.Stream@PNG-en-US.png)

   ![Removing the object via the shortcut menu in the screen editor](images/169820234379_DV_resource.Stream@PNG-en-US.png)

   The object is placed in last position in the layer.

   ![Removing the object via the shortcut menu in the screen editor](images/169806080907_DV_resource.Stream@PNG-en-US.png)

   ![Removing the object via the shortcut menu in the screen editor](images/169806080907_DV_resource.Stream@PNG-en-US.png)

   If you have removed multiple objects from the group using multiple selection, the objects retain their order in the layer.

#### Deleting an object from the group (RT Unified)

##### Introduction

You can delete one or more objects from the group using multiple selection as follows:

- Delete the object in a layer in the "Layout > Layers" task card.
- Delete the object via the shortcut menu in the screen editor.

A group may also contain a single object. If you delete the last object from the group, the group is automatically deleted.

The size of the group is automatically adapted after the removal of objects.

##### Requirement

- A screen containing at least one group of objects is open.

##### Deleting an object in the layer

To delete an object in a layer, follow these steps:

1. Select an object in the group, e.g. Button_1, in the "Layout > Layers" task card.

   ![Deleting an object in the layer](images/169805871755_DV_resource.Stream@PNG-en-US.png)

   ![Deleting an object in the layer](images/169805871755_DV_resource.Stream@PNG-en-US.png)
2. Right-click on the button.

   ![Deleting an object in the layer](images/169824753035_DV_resource.Stream@PNG-en-US.png)

   ![Deleting an object in the layer](images/169824753035_DV_resource.Stream@PNG-en-US.png)

   The shortcut menu opens.
3. Select "Delete".

   The object is deleted from the group.

##### Deleting the object via the shortcut menu in the screen editor

To delete an object via the shortcut menu in the screen editor, follow these steps:

1. Select an object in the group, e.g. Button_1, in the screen editor.
2. Right-click on the button.

   The shortcut menu opens.

   ![Deleting the object via the shortcut menu in the screen editor](images/169824761611_DV_resource.Stream@PNG-en-US.png)

   ![Deleting the object via the shortcut menu in the screen editor](images/169824761611_DV_resource.Stream@PNG-en-US.png)
3. Select "Delete".

   The object is deleted from the group.

   ![Deleting the object via the shortcut menu in the screen editor](images/169829416587_DV_resource.Stream@PNG-en-US.png)

   ![Deleting the object via the shortcut menu in the screen editor](images/169829416587_DV_resource.Stream@PNG-en-US.png)

### Managing group properties (RT Unified)

This section contains information on the following topics:

- [Properties of the group (RT Unified)](#properties-of-the-group-rt-unified)
- [Aggregated properties of the objects in groups (RT Unified)](#aggregated-properties-of-the-objects-in-groups-rt-unified)
- [Adding a property of the group to favorites (RT Unified)](#adding-a-property-of-the-group-to-favorites-rt-unified)
- [Properties of the group in multiple selection (RT Unified)](#properties-of-the-group-in-multiple-selection-rt-unified)

#### Properties of the group (RT Unified)

##### Introduction

Properties of the group are properties that you edit at the group level.

You can configure the group properties in the Engineering System and interpret them in runtime.

##### Properties of the group

The following properties affect the entire group.

- Name
- Coordinates "Position - left" and "Position - top". The coordinates of all objects contained in the group are referenced to the upper left corner of the group.
- "Size - height" and "Size - width" form the outer boundary of the objects contained in the group.

  These values are automatically updated when:

  - Objects are added to the group.
  - Objects are removed from the group.
  - The position of the objects contained in the group is changed.
- Rotation-related properties:

  - "Rotation - pivot point"
  - "Rotation - angle"
  - "Rotation - pivot point X"
  - "Rotation - pivot point Y"

  If the group is rotated, all objects contained in the group are displayed rotated.
- Visibility: The visibility is only toggled in runtime. All objects are always visible during engineering.

  The visibility functions in a cascaded manner:

  - If the visibility of the group has been set to "false", all objects are invisible.
  - If the visibility of the group has been set to "true", the objects for which visibility is set to "true" are visible.
- When "Operator control - allow" is activated, operator control of the objects in the group is permitted.

  Activation of the operator control functions in a cascaded manner:

  - If the "Operator control - allow" property is deactivated, operator control is not possible for any objects.
  - If the "Operator control - allow" property is activated, operator control of objects for which "Operator control - allow" is activated is possible.

  Deactivated objects are displayed grayed out.

---

**See also**

["Favorites" function (RT Unified)](#favorites-function-rt-unified)

#### Aggregated properties of the objects in groups (RT Unified)

##### Introduction

The object properties in the group are displayed as aggregated properties in the Inspector window under "Properties > Miscellaneous > Interface". You can either configure these properties with a static value or dynamize them.

> **Note**
>
> Only the properties of the topmost level are available on the interface for aggregated properties. Properties within the sub-hierarchy are not available.

##### Requirement

- The HMI screen containing at least one object group is open.

##### Configuring aggregated properties with a static value

The following applies for the aggregated properties with a static value:

- If the static value of a configured property is the same for all objects, the current value is displayed at the group level.
- If the static value of a configured property is different for the objects, "Ambiguous value" is displayed in the input field in the "Static value" column.
- If the configured static value of a property of an object is invalid, this is not indicated at the group level. Validation only takes place at the level of the individual objects.
- When you configure a static value for a property under "Properties > Miscellaneous > Interface", the value is passed to every object in the group that has this property.
- For some properties, e.g. the process value, you cannot configure a static value at the group level.

![Configuring aggregated properties with a static value](images/170254296715_DV_resource.Stream@PNG-en-US.png)

##### Dynamizing aggregated properties on the group level

The following applies to dynamizing aggregated properties on the group level:

- If you configure dynamization for a property under "Properties > Miscellaneous > Interface", this dynamization is only displayed on the group level in the engineering system. The dynamization is not visible in the properties of the objects in the group in the engineering system.

  In Runtime, the dynamization of the group is applied to all objects in the group.

> **Note**
>
> The dynamization type "Flashing" is not available for dynamizing the aggregated properties of a group.

##### Dynamizing aggregated properties on the group and object level

The following applies to dynamization of aggregated properties on the group and object level:

- If you dynamize a property on both group and object level, in Runtime the property is dynamized on both the group level and at an object according to the configuration. If you change one of the configured tags, the property is set according to the configured dynamization. The property is thus displayed based to the last dynamization event that occurred, according to the "last wins" principle.
- If you dynamize the process value on the group level, the values are applied to all objects within the group.

  If you dynamize the process value on the object level, the values are not applied to the group.
- If the dynamization on both the group and object levels are linked to the same tag with different values, the result is not defined.

##### Non-aggregatable properties

The following object properties are not displayed under the aggregated properties. You cannot configure or dynamize these object properties at the group level:

- Properties of the group, e.g. coordinates or visibility.
- Appearance - style item
- Resource list
- Selection item
- Connection status
- Focus - show visual

For the following properties, you cannot configure a static value at the group level.

- Process value
- Text

#### Adding a property of the group to favorites (RT Unified)

##### Introduction

You can define your own favorite properties in the "Group" screen object.

The following properties are defined as favorites by the system:

- "Size -width"
- "Size - height"
- "Position - left"
- "Position - top"
- "Name"
- "Visibility"

  ![Introduction](images/169763388427_DV_resource.Stream@PNG-en-US.png)

##### Adding a property to favorites

To add a property to favorites, follow these steps:

1. Right-click on a property that is not defined as a favorite by the system.
2. Select "Add to favorites" in the shortcut menu.

   ![Adding a property to favorites](images/169761534859_DV_resource.Stream@PNG-en-US.png)

   ![Adding a property to favorites](images/169761534859_DV_resource.Stream@PNG-en-US.png)
3. To display all favorites, click the icon ![Adding a property to favorites](images/165848568459_DV_resource.Stream@PNG-de-DE.png).

The number of favorite properties is not limited.

> **Note**
>
> You cannot add the aggregated properties of the objects contained in the group to favorites.

##### Removing a property from favorites

To remove a property from favorites, follow these steps:

1. To display all favorites, click the icon ![Removing a property from favorites](images/165848568459_DV_resource.Stream@PNG-de-DE.png).
2. Right-click the favorite property.
3. Select "Remove from favorites" in the shortcut menu.

#### Properties of the group in multiple selection (RT Unified)

##### Introduction

A group, together with other groups and/or other objects, can be part of a multiple selection. The custom and aggregated properties are displayed under the aggregated properties.

##### Properties of the group in multiple selection

The aggregated group properties are:

- Displayed uncategorized under the "Properties" part.
- Not aggregated with the properties of the objects that are not grouped.

If static property values are defined for multiple selection, the values are passed to all parts of the multiple selection, including custom and aggregated group properties.

If the property is dynamically configured for multiple selection, the dynamic configuration is propagated to all parts of the multiple selection, including custom and aggregated group properties.

##### Example

If a multiple selection includes the objects of the topmost level as well as groups, you can change the background color of all objects.

1. Define the background color for the objects of the topmost layer under "Properties > Appearance > Background color".
2. Define the background color for the grouped objects under "Properties > Miscellaneous > Interface > Background color".

All objects in the multiple selection have the same background color.

## Configuring text lists and graphics lists (RT Unified)

This section contains information on the following topics:

- [Configuring text lists (RT Unified)](#configuring-text-lists-rt-unified)
- [Configuring graphics lists (RT Unified)](#configuring-graphics-lists-rt-unified)

### Configuring text lists (RT Unified)

This section contains information on the following topics:

- [Basics of text lists (RT Unified)](#basics-of-text-lists-rt-unified)
- [Creating a text list (RT Unified)](#creating-a-text-list-rt-unified)
- [Assigning texts and values to an area text list (RT Unified)](#assigning-texts-and-values-to-an-area-text-list-rt-unified)
- [Assigning texts and values to a bit text list (RT Unified)](#assigning-texts-and-values-to-a-bit-text-list-rt-unified)
- [Assigning texts and values to a bit number text list (RT Unified)](#assigning-texts-and-values-to-a-bit-number-text-list-rt-unified)
- [Configuring object with a text list (RT Unified)](#configuring-object-with-a-text-list-rt-unified)
- [Dynamizing texts in a text list (RT Unified)](#dynamizing-texts-in-a-text-list-rt-unified)

#### Basics of text lists (RT Unified)

##### Introduction

Texts are assigned to the values of a tag in a text list. During configuration, you assign the text list to a text field, for example. This supplies the text to be displayed to the object.

You create and edit the text list in the "Text and graphic list" editor. You configure the interface between the text list and a tag at the object that uses the text list.

In WinCC Unified V19 or higher, you can also create text lists as a type in the project library.

The availability of the text list is determined by the HMI device used.

##### Use

You can configure the text list for the following applications:

- Output of texts depending on tag value.
- Display of a selection list in a list box. The associated texts are displayed in the list box depending on the value of the configured tags.

> **Note**
>
> **Display of tag values without text**
>
> The display of tag values to which no text has been assigned depends on the runtime:
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
- Bit number (0-31):

  This setting assigns a text entry from the text list to each bit of a tag. The maximum number of text entries is 32. You use this form of text list, for example, in a sequential control chart when processing a sequencer in which only one bit of the used tag may be set. You influence the behavior of the bit number (0 - 31) with the set bit of the least significance and a default value.

##### Multilingual texts

You can configure multiple languages for the texts in a text list. The texts will then be displayed in the set language in runtime. To this purpose you set the languages in the Project window under "Languages & Resources > Project languages."

##### Configuration steps

The following steps are necessary to display texts in a screen object:

1. Creating the text list
2. Assignment of the texts to values or value ranges of a text list
3. Assigning a text list in the display object
4. Assigning a tag

#### Creating a text list (RT Unified)

##### Introduction

The text list allows you to assign specific texts to values and output these in runtime, for example in an I/O field. Specify the I/O field type, for example, as a pure input field.

##### Procedure

Follow these steps to create a text list:

1. Double-click "Text and graphic lists" in the project tree.
2. Open the "Text lists" tab.

   ![Procedure](images/131377501835_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/131377501835_DV_resource.Stream@PNG-en-US.png)
3. Click "Add" in the "Text lists" table. The Inspector window of the text list is open.
4. Assign a name to the text list that indicates its function.
5. Select the text list type under "Selection":

   - Value/Range: Text from the text list is displayed when the tag has a value that lies within the specified range.
   - Bit (0,1): A text from the text list is displayed if the tag has adopted the value 0. Another text from the text list is displayed if the tag has adopted the value 1.
   - Bit number (0-31): Text from the text list is displayed when the tag has the value of the assigned bit number.
6. Enter a comment for the text list.

##### Result

A text list is created.

#### Assigning texts and values to an area text list (RT Unified)

##### Introduction

For each area text list you specify which texts are displayed at which value range. The entered text is only displayed when the value is within the permitted range.

The following options are available:

- "Range": You enter the minimum value and maximum value for the range.
- "To": You enter the maximum value for the permitted range.
- "Single value": When the specified bit is set, the text is displayed in runtime.
- "From": You enter the minimum value for the permitted range.

##### Requirement

- The "Text and graphic list" editor is open.
- The "Text lists" tab is open.
- An area text list has been created and selected.

##### Procedure

To assign texts and values to a range text list, follow these steps:

1. Click "Add" in the "Text list entries" table.  
   The Inspector window for this list entry opens.

   ![Procedure](images/131309840523_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/131309840523_DV_resource.Stream@PNG-en-US.png)
2. Select one of the options in the Inspector window "Properties > General > Value" and enter values.
3. Enter the text that is displayed in runtime when the tag has the specified value or lies within the specified range of values under "Text." The text may contain a maximum of 128 characters.
4. Activate the "Default entry" for all unassigned values. The entered text is always displayed when the tag has an undefined value. Only one default entry is possible per list.
5. Add additional entries to the text list for additional value ranges.

**Note**

Selecting the default entry is not possible in runtime.

##### Result

An area text list is created. Texts that appear in runtime are assigned to the possible values.

#### Assigning texts and values to a bit text list (RT Unified)

##### Introduction

For each bit text list, you specify which text is displayed at which bit value.

##### Requirement

- The "Text and graphic list" editor is open.
- The "Text lists" tab is open.
- A bit text list has been created and selected.

##### Procedure

To assign texts and values to a bit text list, follow these steps:

1. Click "Add" in the "Text list entries" table.  
   The Inspector window for this list entry opens.

   ![Procedure](images/131227251595_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/131227251595_DV_resource.Stream@PNG-en-US.png)
2. Select the setting "Single value" in the Inspector window "Properties > General > Value" and enter "0" as "value".
3. Under "Text", type in the text that is displayed in runtime when the tag has the value "0". The text may contain a maximum of 128 characters.
4. Click "Add" in the "Text list entries" table. A second list entry is created.
5. Select the setting "Single value" in the Inspector window "Properties > General > Value" and enter "1" as "value".
6. Under "Text", type in the text that is displayed in runtime when the tag has the value "1".

##### Result

A bit text list is created. Texts that appear in runtime are assigned to the possible values "0" and "1".

#### Assigning texts and values to a bit number text list (RT Unified)

##### Introduction

For each bit number text list you specify which texts are displayed at which bit number.

##### Requirement

- The "Text and graphic list" editor is open.
- The "Text lists" tab is open.
- A bit number text list has been created and selected.

##### Assign texts and values to the bit number text list

To assign texts and values to a bit number text list, follow these steps:

1. Click "Add" in the "Text list entries" table.  
   The Inspector window for this list entry opens.

   ![Assign texts and values to the bit number text list](images/131237089035_DV_resource.Stream@PNG-en-US.png)

   ![Assign texts and values to the bit number text list](images/131237089035_DV_resource.Stream@PNG-en-US.png)
2. In the Inspector window, select the "Single value" setting under "Properties > General > Value". Enter "5", for example, for "Value".
3. For all unassigned values, enable the "Default" option for the default entry. The text appears when the tag assumes an undefined value. Only one default entry is possible per list.
4. Enter the text under "Text". When the tag has taken the value "5", the text is displayed in runtime.   
   The text may contain a maximum of 128 characters.
5. You can add additional entries to the text list for more bit numbers.

**Note**

Selecting the default entry is not possible in runtime.

##### Result

A bit number text list is created. Texts that appear in runtime are assigned to the specified bit numbers.

##### Multiline text list entries

For objects with the "Text" property, you can enter the text on multiple lines.

Use the <Shift + Return> key combination to enter a line break in the text entry. Line breaks are represented in the text box by the "¶" paragraph mark.

---

**See also**

[Entering multiline text (RT Unified)](#entering-multiline-text-rt-unified)

#### Configuring object with a text list (RT Unified)

##### Introduction

The output value and value application for text lists are specified in the display and operating object that displays the texts of the text list in runtime. The properties of these objects are configured as required.

##### Requirement

- A text list is created. The values have been defined. The texts are assigned to the values.
- You have created a tag.
- The "Screens" editor is open.
- A screen with an object, such as a text box, is open. The text box is selected.

##### Procedure

1. In the Inspector window under "Properties > Properties > General > Text" in the "Dynamization" column, select the "Resource list" entry.
2. Select the tag whose values determine the display in the text box under "Resource list > Settings > Tag".
3. Select the text list which you want to display in runtime under "Resource list > Settings > Resource list".
4. Click on the button in the "Resource list" line ![Procedure](images/148458605323_DV_resource.Stream@PNG-de-DE.png).   
   The selected text list opens.
5. Select an entry in the "Text list entries" table as the default entry. The text from the default entry is displayed in the object.  
   If you have not specified a default entry, the first entry in the "Text" column is displayed in the object.

| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| - Drag-and-drop a text list from the detail view into the screen. A text box is created and linked to the text list. Configure the tags whose values determine the display in the graphic view. |  |

##### Result

The defined texts of the text list are displayed in the text field in runtime when the tag has the specified value.

---

**See also**

[Text box (RT Unified)](#text-box-rt-unified)
  
[Show default entry of text and graphic list in the object (RT Unified)](#show-default-entry-of-text-and-graphic-list-in-the-object-rt-unified)

#### Dynamizing texts in a text list (RT Unified)

##### Introduction

In some objects, dynamic information can be displayed in the properties that contain a text.

If you insert a reference to a text list in the "Text" or "Tooltip" property, for example, the current value of the inserted text list is displayed in the object in Runtime.

Supported objects:

- Text box
- Button
- Symbolic IO field
- Switch

In the message texts, e.g. in the alarm control, the dynamic information may already be inserted.

> **Note**
>
> Local session tags are not supported as a source for the dynamic information.

##### Requirement

- The HMI screen with an object, e.g. a text box or a button, is open.

##### Configuring a text list in the object

To display a text list in an object, e.g. in a text box, follow these steps:

1. Configure a tag, e.g. "IntTag".
2. Configure a text list, e.g. "Textliste_1".
3. In the Inspector window, select "Properties > Properties > General > Text".
4. Enter a text in the "Static value" column in the input field, e.g. "Text list".
5. Right-click in the input field. The shortcut menu opens.

   ![Configuring a text list in the object](images/160411319435_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a text list in the object](images/160411319435_DV_resource.Stream@PNG-en-US.png)
6. Select "Insert parameter field" in the shortcut menu. A dialog opens.

   ![Configuring a text list in the object](images/160411174027_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a text list in the object](images/160411174027_DV_resource.Stream@PNG-en-US.png)
7. Select the "IntTag" tag under "Tag" in the dialog.
8. Under "Display type", select "Text list".
9. Under "Text list", select the text list "Textlist_1".
10. Confirm the selection. The field with the tag name becomes visible in the input field.

    ![Configuring a text list in the object](images/160411182859_DV_resource.Stream@PNG-en-US.png)

    ![Configuring a text list in the object](images/160411182859_DV_resource.Stream@PNG-en-US.png)

    The default entry of the text list is displayed in the text box.
11. Compile and load the device.

Alternatively, you can configure the text list entry directly in the text list.

![Configuring a text list in the object](images/160411385355_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> Circular references are not supported.

##### Result

The object displays the current text list entry in Runtime.

### Configuring graphics lists (RT Unified)

This section contains information on the following topics:

- [Basics of graphic lists (RT Unified)](#basics-of-graphic-lists-rt-unified)
- [Creating a graphic list (RT Unified)](#creating-a-graphic-list-rt-unified)
- [Assigning graphics and values to an area graphic list (RT Unified)](#assigning-graphics-and-values-to-an-area-graphic-list-rt-unified)
- [Assigning graphics and values to a bit graphic list (RT Unified)](#assigning-graphics-and-values-to-a-bit-graphic-list-rt-unified)
- [Assigning graphics and values to a bit number graphic list (RT Unified)](#assigning-graphics-and-values-to-a-bit-number-graphic-list-rt-unified)
- [Configuring objects with a graphic list (RT Unified)](#configuring-objects-with-a-graphic-list-rt-unified)

#### Basics of graphic lists (RT Unified)

##### Introduction

The possible values of a tag are assigned to specific graphics in a graphic list. During configuration, assign the graphic list to a button or a graphic view. This supplies the graphics to be displayed to the object.

The graphic lists are created with the "Text and graphic list" editor. You configure the interface between the graphic list and a tag at the object that uses the graphic list.

The availability of the graphic list is determined by the HMI device used.

##### Application

You can configure the graphic list for the following situations:

- Selection list with a graphic view.
- State-specific graphic for a button.

##### Graphic sources

Graphics can be added to the graphic list from the following sources:

- By selecting from the project graphics.
- By selecting an existing file. You can use the following file types:   
  *.bmp, *.ico, *.emf, *.wmf, *.gif, *.tiff, *.png, *.svg, *.jpeg, *.jpg.
- Creating a new file.

##### Ranges for the graphic list

Three types are available for the graphic lists:

- Value/Range

  This setting assigns graphic entries from the graphic list to integer values or value ranges of a tag. You can select the number of graphic entries as needed. The maximum number of entries depends on the HMI device you are using.

  You specify a default value which is shown if the value of the tag lies outside the defined range.
- Bit (0, 1)

  This setting assigns graphic entries from the graphic list to two states of a binary tag. You can create a graphic entry for each state of the binary tag.
- Bit number (0-31):

  This setting assigns a graphic entry from the graphic list to each bit of a tag. The maximum number of graphic entries is 32. You use this form of graphic list, for example, in a sequential control system when processing a sequencer in which only one bit of the used tags can be set. You influence the behavior of the bit number (0 - 31) with the set bit of the least significance and a default value.

##### Multilingual graphics

The graphics in a graphic list can be configured as multilingual. The graphics are then be displayed in the set runtime language. To this purpose you set the languages in the Project window under "Languages & Resources > Project languages".

##### Configuration steps

The following steps are required to display graphics in a graphic view:

1. Creating the graphic list
2. Assignment of the graphics to values or value ranges of a graphic list
3. Assigning a graphic list in the display object.
4. Assigning a tag

#### Creating a graphic list (RT Unified)

##### Introduction

The graphic list allows you to assign specific graphics to variable values and output these in a graphic I/O field in runtime. Specify the type of the graphic I/O field, for example, as a pure output field.

##### Procedure

1. Double-click "Text and graphic lists" in the project tree.
2. Open the "Graphic lists" tab.

   ![Procedure](images/131377512331_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/131377512331_DV_resource.Stream@PNG-en-US.png)
3. Click "Add" in the "Graphic lists" table. The Inspector window of the graphic list will open up.
4. Assign a name to the graphic list that indicates its function.
5. Select the graphic list type under "Selection":

   - Value/Range: Graphic from the graphic list is displayed when the tag has a value that lies within the specified range.
   - Bit (0,1): A graphic from the graphic list is displayed when the tag has the value 0. A different graphic from the graphic list is displayed when the tag has the value 1.
   - Bit number (0-31): Graphic from the graphic list is displayed when the tag has the value of the assigned bit number.
6. Enter a comment for the graphic list.

##### Result

A graphic list is created.

#### Assigning graphics and values to an area graphic list (RT Unified)

##### Introduction

For each area graphic list you specify which graphics are displayed at which value range. The selected graphic is only displayed when the value is within the permitted range.

The following options are available:

- "Range": You enter the minimum value and maximum value for the range.
- "To": You enter the maximum value for the permitted range.
- "Single value": When the specified bit is set, the selected graphic is displayed in runtime.
- "From": You enter the minimum value for the permitted range.

##### Requirement

- The "Text and graphic list" editor is open.
- The "Graphic list" tab is open.
- An area graphic list has been created and selected.

##### Procedure

1. Click "Add" in the "Graphic list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/100732484107_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/100732484107_DV_resource.Stream@PNG-en-US.png)
2. Select an option in the Inspector window "Properties > General > Value". Enter values.
3. In the "Graphic" column, select a graphic to be displayed in runtime if the tag has the specified value or is within the specified value range.
4. For all unassigned values, enable the "Default" option for the default entry. The graphic is displayed when the tag has an undefined value. Only one default entry is possible per list.
5. Add additional entries to the graphic list for additional value ranges.

**Note**

Selecting the default entry is not possible in runtime.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| Inserting a graphic using drag-and-drop operation:  | Symbol | Meaning | | --- | --- | | 1. Select a graphic in the library or in your file system. 2. Drag-and-drop the graphic into the "Graphic list entries > Graphic" table. |  | |  |

##### Result

An area graphic list is created. Graphics that appear in runtime are assigned to the possible values.

#### Assigning graphics and values to a bit graphic list (RT Unified)

##### Introduction

For each bit graphic list you specify which graphic is displayed at which bit value.

##### Requirement

- The "Text and graphic list" editor is open.
- The "Graphic list" tab is opened.
- A bit graphic list has been created and selected.

##### Procedure

1. Click "Add" in the "Graphic list entries" table.

   The Inspector window for this list entry opens.

   ![Procedure](images/131279197835_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/131279197835_DV_resource.Stream@PNG-en-US.png)
2. Select the setting "Single value" in the Inspector window under "Properties > General > Value" and enter "0" as "value".
3. Click "Add" in the "Graphic list entries" table. A second list entry is created.
4. Select the setting "Single value" in the Inspector window under "Properties > General > Value" and enter "1" as "value".
5. Select a graphic that is displayed in runtime when the tag has the value "1".

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| Inserting a graphic using drag-and-drop operation:  | Symbol | Meaning | | --- | --- | | 1. Select a graphic in the library or in your file system. 2. Drag-and-drop the graphic into the "Graphic list entries > Graphic" table. |  | |  |

##### Result

A bit graphic list is created. Graphics that appear in runtime are assigned to the values "0" and "1".

#### Assigning graphics and values to a bit number graphic list (RT Unified)

##### Introduction

For each bit number graphic list you specify which graphics are displayed at which bit number.

##### Requirement

- The "Text and graphic list" editor is open.
- The "Graphic list" tab is open.
- A bit number graphic list has been created and selected.

##### Assigning graphics and values to the bit number graphic list

To assign the graphics and values to a bit number graphic list, follow these steps:

1. Click "Add" in the "Graphic list entries" table.

   The Inspector window for this list entry opens.

   ![Assigning graphics and values to the bit number graphic list](images/131279207947_DV_resource.Stream@PNG-en-US.png)

   ![Assigning graphics and values to the bit number graphic list](images/131279207947_DV_resource.Stream@PNG-en-US.png)
2. Select the "Single value" settings in the Inspector window "Properties > General > Value". Enter "5", for example, for "Value".
3. For all unassigned values, enable the "Default" option for the default entry. The graphic is displayed when the tag has an undefined value. Only one default entry is possible per list.
4. Enter the graphic under "Properties > General > Graphic". When the tag has taken the value "5", the graph is displayed in runtime.
5. You can add additional entries to the graphic list for more bit numbers.

**Note**

Selecting the default entry is not possible in runtime.

| Symbol | Meaning |
| --- | --- |
| ![Assigning graphics and values to the bit number graphic list](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for an efficient procedure** |
| Inserting a graphic using drag-and-drop operation:  | Symbol | Meaning | | --- | --- | | 1. Select a graphic in the library or in your file system. 2. Drag-and-drop the graphic into the "Graphic list entries > Graphic" table. |  | |  |

##### Result

A bit number graphic list is created. Graphics that appear in runtime are assigned to the specified bit numbers.

#### Configuring objects with a graphic list (RT Unified)

##### Introduction

The output value and value application for graphic list are specified in the display and operating object that displays the graphics of the graphic list in runtime. The properties of these objects are configured as required.

##### Requirement

- A graphic list is created. The values have been defined. Graphics have been assigned to the values.
- You have created a tag.
- The Screens editor is open.
- A screen with an object, such as a graphic view, is open. The graphic display is selected.

##### Procedure

1. In the Inspector window under "Properties > Properties > General > Graphics", in the "Dynamization" column, select the "Resource list" entry.
2. Under "Resource list > Settings > Tag", select the tag whose values determine the display in the graphic view.
3. Select the graphic list which you want to have displayed in runtime under "Resource list > Settings > Resource list".
4. Click on the button in the "Resource list" line ![Procedure](images/148458605323_DV_resource.Stream@PNG-de-DE.png).   
   The selected graphic list opens.
5. Select an entry in the "Graphic list entries" table as the default entry. The graphic from the standard entry is displayed in the object.  
   If you have not specified a default entry, the first entry in the "Graphic" column is displayed in the object.

| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | Tips for an efficient procedure |
| --- | --- |
| - Drag a graphics list from the detail view of the text and graphics lists to the screen. A graphic view is created and linked to the graphics list. Configure the tags whose values determine the display in the graphic view. |  |

##### Result

If the tag adopts the specified value, the defined graphics are displayed in the graphic view in runtime.

---

**See also**

[Graphic view (RT Unified)](#graphic-view-rt-unified)

## Configuring dynamization (RT Unified)

This section contains information on the following topics:

- [Basics of dynamizing screens (RT Unified)](#basics-of-dynamizing-screens-rt-unified)
- [Displaying dynamization of the properties (RT Unified)](#displaying-dynamization-of-the-properties-rt-unified)
- [Filter dynamized properties (RT Unified)](#filter-dynamized-properties-rt-unified)
- [Display dynamization type (RT Unified)](#display-dynamization-type-rt-unified)
- [Changing a dynamization for multiple objects (RT Unified)](#changing-a-dynamization-for-multiple-objects-rt-unified)
- [Dynamizing object properties (RT Unified)](#dynamizing-object-properties-rt-unified)

### Basics of dynamizing screens (RT Unified)

#### Dynamizing objects

Dynamics are used to change the properties of screen objects and screens in runtime depending on another value. The source for this value changes is referred to as "Dynamization type".

#### Dynamization types

The following table shows the dynamization types available in WinCC:

| Dynamization type | Description | Supported property classes | Examples |
| --- | --- | --- | --- |
| Tag | Defines the property value depending on the tag value. | All | "Process value" or "Left" properties |
| Script | Defines the property value depending on the return value. | All | "Process value" or "Left" properties |
| Resource list | Defines the property value depending on an entry from a text list or graphic list. | Text / Graphic | Properties "Text", "Tooltip" or "Graphic". |
| Flashing | Defines that the property flashes in configurable colors. | Colors | Properties "Foreground color" or "Border color". |
| Expression | Specifies the property value depending on several tag values. The tag values are linked by logical operators. | Depends on the screen object | "Size" or "Background color" properties |

#### Examples of dynamizations

The table below shows typical application examples for each type of dynamization:

| Dynamization type | Application example |
| --- | --- |
| Tag | Visualize the level. The "Process value" property of a bar graph is dynamized with a tag that contains the level from the PLC. |
| Script | Simulate the filling process. To simulate a movement of bottles on a conveyor belt, the properties "Left", "Top" and "Visible" are dynamized with scripts. |
| Resource list | Display the plant status. The meaning of a quality code is saved in a text list. Depending on the transferred numerical quality code, its meaning is displayed on the HMI device. |
| Flashing | Visualize limit violations. When the level of a tank drops below a limit, the visualized tank is to flash in two signal colors. |
| Expression | Visualization of machine states. Machine states of different plant objects are stored in tags of the type "Bool". Complex visualizations are derived from the combination of tag values. |

---

**See also**

[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

### Displaying dynamization of the properties (RT Unified)

#### Introduction

In the Inspector window of an object, you can see which object properties are dynamized.

#### Displaying dynamization of the property

Dynamized properties are shown in dark blue font and in bold in the Inspector window in the "Name" column.

Groups that contain a dynamized property are displayed in dark blue font.

![Displaying dynamization of the property](images/163348367243_DV_resource.Stream@PNG-en-US.png)

### Filter dynamized properties (RT Unified)

#### Introduction

You can display only the dynamic properties in the Inspector window of an object.

#### Filter dynamized properties

If you use the "Filter" function and select "All dynamized" in the "Dynamization" column, the following is displayed:

- All dynamized properties in dark blue font and bold.
- The groups in which a property is dynamized in dark blue font.

![Filter dynamized properties](images/160121375627_DV_resource.Stream@PNG-en-US.png)

### Display dynamization type (RT Unified)

#### Introduction

You can locate the individual types of dynamization by using the "Filter" icon ![Introduction](images/165848560523_DV_resource.Stream@PNG-de-DE.png).

#### Find type of dynamization by input

To search for a type of dynamization by entering the type of dynamization, follow these steps:

1. Click on the "Filter" icon.
2. Enter a type of dynamization.
3. Confirm your selection with the <Return> key.

   ![Find type of dynamization by input](images/160122288139_DV_resource.Stream@PNG-en-US.png)

All properties with the selected type of dynamization are displayed.

#### Find type of dynamization by selection

To search for a type of dynamization by selecting the type of dynamization, follow these steps:

1. Click on the "Filter" icon.
2. Click the arrow in the first cell of the "Dynamization" column.
3. Select the desired type of dynamization from the drop-down list.

   ![Find type of dynamization by selection](images/160122555019_DV_resource.Stream@PNG-en-US.png)

All properties with the selected type of dynamization are displayed.

### Changing a dynamization for multiple objects (RT Unified)

#### Introduction

You can change the dynamization of a property for several objects at the same time.

#### Changing a dynamization for multiple objects

To change the dynamization of a property for several objects at the same time, follow these steps:

1. Select several objects in the screen via multiple selection.
2. Select a property.
3. Dynamize the property, for example, by using a script.

The dynamization of the property is applied to all selected objects that have the property.

---

**See also**

[Select multiple objects (RT Unified)](#select-multiple-objects-rt-unified)

### Dynamizing object properties (RT Unified)

This section contains information on the following topics:

- [Dynamizing object properties via tags (RT Unified)](#dynamizing-object-properties-via-tags-rt-unified)
- [Dynamizing an object property via a script (RT Unified)](#dynamizing-an-object-property-via-a-script-rt-unified)
- [Dynamizing an object property via a resource list (RT Unified)](#dynamizing-an-object-property-via-a-resource-list-rt-unified)
- [Dynamizing object property via flashing (RT Unified)](#dynamizing-object-property-via-flashing-rt-unified)
- [Dynamizing an object property via an expression (RT Unified)](#dynamizing-an-object-property-via-an-expression-rt-unified)
- [Examples (RT Unified)](#examples-rt-unified-1)

#### Dynamizing object properties via tags (RT Unified)

This section contains information on the following topics:

- [Dynamizing object property via tag (RT Unified)](#dynamizing-object-property-via-tag-rt-unified)
- [Transferring property conditions (RT Unified)](#transferring-property-conditions-rt-unified)
- [Automatically fill in property values for tags (RT Unified)](#automatically-fill-in-property-values-for-tags-rt-unified)
- [Dynamizing an object property with "Range" evaluation type (RT Unified)](#dynamizing-an-object-property-with-range-evaluation-type-rt-unified)
- [Dynamizing an object property with "Multiple bits" evaluation type (RT Unified)](#dynamizing-an-object-property-with-multiple-bits-evaluation-type-rt-unified)
- [Dynamizing an object property with "Single bit" evaluation type (RT Unified)](#dynamizing-an-object-property-with-single-bit-evaluation-type-rt-unified)

##### Dynamizing object property via tag (RT Unified)

###### Introduction

When you dynamize an object property via a tag, the object property is changed in runtime depending on the tag value.

###### Requirement

- A screen is open.
- An object is configured.
- You have configured a tag.
- The object property supports the dynamization type "Tag".

###### Dynamizing an object property via a tag

To dynamize an object property via a tag, follow these steps:

1. Select the object.
2. Under "Properties > Properties > Dynamization" select the object property in the Inspector window.
3. Select the "Tag" option. The area for configuring the tags is displayed.

   ![Dynamizing an object property via a tag](images/169385421963_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing an object property via a tag](images/169385421963_DV_resource.Stream@PNG-en-US.png)
4. Select a tag under "Tag > Process > Tag". Only the relevant tags are displayed in the selection dialog. If you want to see all tags, enable "Show all" in the selection dialog.
5. Define the evaluation type of the tags:

   - None
   - Range
   - Multiple bits
   - Single bit
6. Define the properties for the respective evaluation type of the tags.
7. If required, enable the options "Use indirect addressing" or "Read only" in the "Settings" area.

   - "Use indirect addressing"

     The configured tag of the "WString" data type must contain the name of another tag as text.
   - "Read only"

     The change to the property value is not applied to the tag.

The object property is dynamized via a tag. The tag value specifies the property value in runtime.

###### Unsupported tag data types

All tag data types are supported for the "Multiple bits" or "Single bit" evaluation types with the exception of:

- DateTime
- WChar
- WString

> **Note**
>
> Mathematical operations are only possible with JavaScript for "Logical" data types. Mathematical system functions, e.g. IncreaseTag, only work with SInt or UInt.

---

**See also**

[Indirect addressing (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#indirect-addressing-rt-unified)

##### Transferring property conditions (RT Unified)

###### Introduction

You can use "Copy" and "Paste" to transfer the conditions of an object property to the same or similar properties of another object.

###### Transferring property conditions

To transfer the conditions of an object property to the same or similar properties of another object, follow these steps:

1. Select one or more conditions under "Type > Condition".
2. Select "Copy" in the shortcut menu.

   ![Transferring property conditions](images/155660103051_DV_resource.Stream@PNG-en-US.png)

   ![Transferring property conditions](images/155660103051_DV_resource.Stream@PNG-en-US.png)
3. Select another object or object property in the "Screens" editor.
4. Paste the copied conditions under "Condition".

Note the following:

- Any existing conditions are overwritten on pasting.
- The data types must be the same or similar, e.g. "Background - color" and "Background - alternative color".
- Inserting data is possible even if no tag is assigned to the property.
- When pasting data, if the number of copied conditions is greater than the possible number of conditions at the target object, only the maximum possible number of conditions will be pasted.

---

**See also**

[Auto-filling the property values of a collection (RT Unified)](#auto-filling-the-property-values-of-a-collection-rt-unified)

##### Automatically fill in property values for tags (RT Unified)

###### Introduction

You can automatically fill the properties of tags in the "Range" and "Multiple bits" evaluation type.

###### Auto-fill property values

To automatically fill in the property values, follow these steps:

1. Select a cell under "Tag > Type > Condition".
2. Drag the blue border up or down. The value is applied to the target cells.

   ![Auto-fill property values](images/148801957899_DV_resource.Stream@PNG-en-US.png)

   ![Auto-fill property values](images/148801957899_DV_resource.Stream@PNG-en-US.png)

If you select multiple cells in the "Condition" column and there is a logical relationship between the values, the values of the destination cells are adapted according to the relationship.

---

**See also**

[Dynamizing an object property with "Range" evaluation type (RT Unified)](#dynamizing-an-object-property-with-range-evaluation-type-rt-unified)
  
[Dynamizing an object property with "Multiple bits" evaluation type (RT Unified)](#dynamizing-an-object-property-with-multiple-bits-evaluation-type-rt-unified)

##### Dynamizing an object property with "Range" evaluation type  (RT Unified)

###### Introduction

When you dynamize an object property via a tag, the object property is changed in runtime depending on the tag value.

The following example shows the dynamization of a button. The button changes its alternative background color depending on the tag of the "Range" type.

###### Requirement

- A screen is open.
- An object, for example a button, is configured.
- You have configured a tag.
- The object property supports the dynamization type "Tag".

###### Dynamizing an object property with "Range" evaluation type

To dynamize an object property with "Range" evaluation type, follow these steps:

1. Select the object, for example, a button.
2. In the Inspector window under "Properties > Properties > General > Text > Background - Alternative color", dynamize an object property, such as "Background - Alternative color".
3. Select "Tag" in the "Dynamization" column.
4. Select a tag under "Tag > Process > Tag".
5. Select "Range" as the evaluation type.
6. Enter the ranges in the "Condition" column.
7. Define the alternative background color for each area in the "Background - Alternative Color" column.

   ![Dynamizing an object property with "Range" evaluation type](images/152936860939_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing an object property with "Range" evaluation type](images/152936860939_DV_resource.Stream@PNG-en-US.png)

###### Result

The color of the button changes depending on the value range in which the tag is located in runtime.

###### Overlapping ranges

If there is overlapping of values in the individual ranges, note that:

- Cells where range overlaps occur are highlighted in color.

  ![Overlapping ranges](images/151381627147_DV_resource.Stream@PNG-en-US.png)
- The overlaps are reported as a warning when compiling the project. Downloading to the device is possible.
- The first highlighted value is always used in runtime.

---

**See also**

[Automatically fill in property values for tags (RT Unified)](#automatically-fill-in-property-values-for-tags-rt-unified)

##### Dynamizing an object property with "Multiple bits" evaluation type  (RT Unified)

###### Introduction

When you dynamize an object property via a tag, the object property is changed in runtime depending on the tag value.

The following example shows the dynamization of a button. The button changes its alternative background color depending on the tag of the "Multiple bits" type.

###### Requirement

- A screen is open.
- An object, for example a button, is configured.
- You have configured a tag.
- The object property supports the dynamization type "Tag".

###### Dynamizing an object property with "Multiple bits" evaluation type

To dynamize an object property with the "Multiple bits" evaluation type, follow these steps:

1. Select the object, for example, a button.
2. In the Inspector window under "Properties > Properties > General > Text > Background - Alternative color", dynamize an object property, such as "Background - Alternative color".
3. Select "Tag" in the "Dynamization" column.
4. Select a tag under "Tag > Process > Tag".
5. Select "Multiple bits" as the type.
6. Enter the bit number.
7. Define the alternative background colors for the bit number in the "Background - alternative color" column.

   ![Dynamizing an object property with "Multiple bits" evaluation type](images/163293613707_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing an object property with "Multiple bits" evaluation type](images/163293613707_DV_resource.Stream@PNG-en-US.png)

###### Result

When the tag has accepted the assigned bit number in runtime, the color of the button is changed accordingly.

###### Unsupported tag data types

All tag data types are supported for the "Multiple bits" or "Single bit" evaluation types with the exception of:

- DateTime
- WChar
- WString

> **Note**
>
> Mathematical operations are only possible with JavaScript for "Logical" data types. Mathematical system functions, e.g. IncreaseTag, only work with SInt or UInt.

---

**See also**

[Automatically fill in property values for tags (RT Unified)](#automatically-fill-in-property-values-for-tags-rt-unified)

##### Dynamizing an object property with "Single bit" evaluation type  (RT Unified)

###### Introduction

When you dynamize an object property via a tag, the object property is changed in runtime depending on the tag value.

The following example shows the dynamization of a button. The button changes its alternative background color depending on the tag of the "Single bit" type.

###### Requirement

- A screen is open.
- An object, for example a button, is configured.
- You have configured a tag.
- The object property supports the dynamization type "Tag".

###### Selecting an object property with "Single bit" evaluation type

To dynamize an object property with the "Single bit" evaluation type, follow these steps:

1. Select the object, for example, a button.
2. In the Inspector window under "Properties > Properties > General > Text > Background - Alternative color", dynamize an object property, such as "Background - Alternative color".
3. Select "Tag" in the "Dynamization" column.
4. Select a tag under "Tag > Process > Tag".
5. Select "Single bit" as the evaluation type.
6. Select the bit position, for example, "3".
7. Define the properties for the "0" and "1" value of the condition.

   ![Selecting an object property with "Single bit" evaluation type](images/165406695051_DV_resource.Stream@PNG-en-US.png)

   ![Selecting an object property with "Single bit" evaluation type](images/165406695051_DV_resource.Stream@PNG-en-US.png)

###### Result

When the tag at "3" position has taken the value "1" in runtime, the color of the button is changed.

###### Unsupported tag data types

All tag data types are supported for the "Multiple bits" or "Single bit" evaluation types with the exception of:

- DateTime
- WChar
- WString

> **Note**
>
> Mathematical operations are only possible with JavaScript for "Logical" data types. Mathematical system functions, e.g. IncreaseTag, only work with SInt or UInt.

#### Dynamizing an object property via a script (RT Unified)

##### Introduction

You can dynamize the object properties via a script. The execution of the script is started by a trigger. Set a cycle or tag as a trigger.

##### Requirement

- A screen is open.
- An object is configured.
- An object property supports the dynamization type "Script".

##### Dynamizing an object property via a script

To dynamize an object property using a script, follow these steps:

1. Select the object, for example, a button.
2. In the Inspector window under "Properties > Properties > Dynamization", dynamize an object property, such as "Background - Color".
3. In the "Dynamization" column, select the "Script" option. The editor for scripts is displayed. Select one of the following options:

   - Create a "Global definition". Click "Global definition". Write the code for the global definition.
   - Write the code for the script.
4. Insert a tag into the script. Referenced tags are automatically offered as triggers.
5. Select the trigger ![Dynamizing an object property via a script](images/24096985227_DV_resource.Stream@PNG-de-DE.png) that triggers the dynamization in Runtime.

   The dialog for selecting a trigger is displayed.

   ![Dynamizing an object property via a script](images/163392331531_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing an object property via a script](images/163392331531_DV_resource.Stream@PNG-en-US.png)

   Select one of the following options:

   - A tag that is referenced in the script automatically (default).
   - A tag that is not referenced in the script.
   - A cycle.

##### Result

The object property is dynamized via a script. The return value of the script specifies the property value in Runtime.

> **Note**
>
> The dynamization of an event is only monitored regarding an operator authorization if the triggering event, e.g. "Press button", is triggered by a user.

#### Dynamizing an object property via a resource list (RT Unified)

##### Introduction

You can dynamize the object properties via a resource list. In runtime, the entry from the configured text list or graphic list is displayed at the property.

##### Requirement

- A screen is open.
- An object is configured.
- You have configured a tag.
- A text list or graphic list is configured.
- The object property supports the "Resource list" dynamization type.

##### Dynamizing an object property via a resource list

To dynamize an object property via a resource list, follow these steps:

1. Select the object.
2. In the Inspector window, select "Properties > Properties > General > Text".
3. Select "Resource list" in the "Dynamization" column.
4. Under "Settings > Resource list" in the "Resource list" dialog, select a text list, for example.
5. Click on the button in the "Resource list" line ![Dynamizing an object property via a resource list](images/148458605323_DV_resource.Stream@PNG-de-DE.png).

   The selected text list is opened directly for editing.

   ![Dynamizing an object property via a resource list](images/148525068299_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing an object property via a resource list](images/148525068299_DV_resource.Stream@PNG-en-US.png)
6. Select an entry in the "Text list entries" table as the default entry. The text from the default entry is displayed in the object.

   If you do not specify a default entry, the first entry in the "Text" column is displayed in the object. The same applies to a graphic list.

##### Result

The object property is dynamized via a resource list. The tag value specifies the entry from the configured text list or graphic list that is displayed in runtime.

---

**See also**

[Show default entry of text and graphic list in the object (RT Unified)](#show-default-entry-of-text-and-graphic-list-in-the-object-rt-unified)

#### Dynamizing object property via flashing  (RT Unified)

##### Introduction

You can display objects as flashing in runtime. You can configure the flashing characteristics for each color setting of an object that supports flashing in the Inspector window.

You select the colors, the condition, and the flashing frequency.

> **Note**
>
> Flashing in runtime does not change the color value of the property.

##### Requirement

- A screen is open.
- An object is configured.
- The object property supports the dynamization type "Flashing".

##### Dynamizing object property via flashing

To dynamize an object property via "Flashing", follow these steps:

1. Select the object.
2. In the Inspector window under "Properties", select the property for which you want to define the flashing characteristics, for example, "Background - color".
3. Select "Flashing" in the "Dynamization" column. The "Flashing" page appears.
4. Select the flash colors. Flashing is only visible in runtime when there is a difference between the two colors.
5. Select the condition for the object flashing in runtime.
6. Select the flashing frequency.

The object property is dynamized with flashing using the dynamization type "Flashing". When the configured condition occurs in runtime, the object property flashes in the configured colors and at the set rate.

##### Condition and rate

The following options are available for the condition:

- "Never": You disable the flashing.
- "Always": You enable the flashing.
- "Range violation": The property flashes when the configured permissible range is violated.

  > **Note**
  >
  > Flashing for a range violation only works if you have linked the object to a PLC tag. When the value of the PLC tag lies outside the defined range, the object will start flashing automatically.

The following options are available for the rate:

- "Slow"
- "Medium"
- "Fast"

##### Result

The object property is dynamized. When the configured condition occurs in runtime, the object property flashes in the configured colors and at the set rate.

#### Dynamizing an object property via an expression (RT Unified)

This section contains information on the following topics:

- [Dynamizing an object property via an expression (RT Unified)](#dynamizing-an-object-property-via-an-expression-rt-unified-1)
- [Logical operators for expressions (RT Unified)](#logical-operators-for-expressions-rt-unified)

##### Dynamizing an object property via an expression (RT Unified)

###### Introduction

You can dynamize the object properties using expressions with multiple tags.

In an expression, tags are linked by logical operators. The result of the expression determines the dynamization. For example, you can link two tags of type "Bool" with the AND operator. If both tags return the value TRUE, then the result of the expression is also TRUE and the property value is set accordingly.

The following applies to the input values for logic operations:

- Value 0 = FALSE
- Value not equal to 0 = TRUE

###### Requirement

- A screen is open.
- An object is configured.
- The object property supports the dynamization type "Expression".

###### Select object property

To select an object property for dynamization with an expression, follow these steps:

1. Select the object.
2. In the Inspector window, under "Properties", select the "Expressions" tab.
3. Select the property you want to dynamize from the "Add property" selection list.

   ![Select object property](images/163278820747_DV_resource.Stream@PNG-en-US.png)

   The selected property is displayed with the default values.

   ![Select object property](images/160122567179_DV_resource.Stream@PNG-en-US.png)

Alternatively, specify "Expression" as the dynamization type for a property in the "Dynamization" column in the Inspector window, e.g. for "Foreground - Color" under "Properties > Foreground - color".

###### Delete object property

To delete the selected object property, follow these steps:

1. In the first row in the column, click the property you want to delete.

   The "Remove property" button appears.

   ![Delete object property](images/163278831627_DV_resource.Stream@PNG-en-US.png)
2. Click on the "Remove property" button.

   The property is removed.

###### Dynamizing an object property with an expression

To dynamize an object property via an expression, follow these steps:

1. In the "Condition" column, click "<Add>".
2. Click ![Dynamizing an object property with an expression](images/160131120779_DV_resource.Stream@PNG-de-DE.png).

   The editor for expressions is displayed.

   ![Dynamizing an object property with an expression](images/160131129355_DV_resource.Stream@PNG-en-US.png)

   - To insert a tag, click the icon for tags ![Dynamizing an object property with an expression](images/166977108107_DV_resource.Stream@PNG-de-DE.png).

     The selection dialog for tags is displayed.
   - To insert an operator at the cursor position, click AND, OR, NOT or XOR.
   - To insert a parenthesis at the cursor position, click on the icons for parentheses.
3. To save the expression, click ![Dynamizing an object property with an expression](images/160132254347_DV_resource.Stream@PNG-de-DE.png).
4. Determine the properties to apply to the screen object when the expression returns the TRUE value.
5. You can add further conditions for the currently selected property.

   ![Dynamizing an object property with an expression](images/160132736523_DV_resource.Stream@PNG-en-US.png)
6. To dynamize another property of the selected object using an expression, click "Add property".

   Properties for which a dynamization has already been configured cannot be added a second time.

> **Note**
>
> When an object property is dynamized with the "NOT" operator, the expression to be negated must be placed inside parentheses, e.g. NOT( 'HMI_Tag_7' ).

###### Result

The expression is evaluated when one of the tag values changes.

Properties change as soon as the result of the expression changes.

If none of the conditions returns TRUE, the default value is assumed.

If multiple conditions are defined, the first condition in the list that returns TRUE is applied.

Expressions that cannot be evaluated are skipped, e.g. because of a syntax error or a tag that cannot be accessed.

If the tag values change, all expressions are reevaluated. Working from top to bottom, the first row that is evaluated as TRUE defines the values and the flashing for the properties.

##### Logical operators for expressions (RT Unified)

###### Introduction

In an expression, tags are linked by logical operators. The result of the expression determines the dynamization of the object properties.

###### Input values for logical operators

The following applies to the input values for logic operations:

- Value 0 = FALSE
- Value not equal to 0 = TRUE

You can find the results of expressions with various values and operators in the tables below.

###### Defining the evaluation order

The parentheses define the evaluation order. The expression inside parentheses is evaluated first.

Examples:

- (TRUE OR FALSE)AND TRUE => (TRUE)AND TRUE => TRUE
- TRUE OR(FALSE AND TRUE) => TRUE OR(FALSE) => TRUE

###### Operator AND

| Expression | Result |
| --- | --- |
| TRUE AND TRUE | TRUE |
| TRUE AND FALSE | FALSE |
| FALSE AND TRUE | FALSE |
| FALSE AND FALSE | FALSE |

###### Operator OR

| Expression | Result |
| --- | --- |
| TRUE OR TRUE | TRUE |
| TRUE OR FALSE | TRUE |
| FALSE OR TRUE | TRUE |
| FALSE OR FALSE | FALSE |

###### Operator NOT

| Expression | Result |
| --- | --- |
| NOT TRUE | FALSE |
| NOT FALSE | TRUE |

###### Operator XOR

| Expression | Result |
| --- | --- |
| TRUE XOR TRUE | FALSE |
| TRUE XOR FALSE | TRUE |
| FALSE XOR TRUE | TRUE |
| FALSE XOR FALSE | FALSE |

#### Examples (RT Unified)

This section contains information on the following topics:

- [Dynamize "Graphic" object property via tag (RT Unified)](#dynamize-graphic-object-property-via-tag-rt-unified)
- [Dynamizing "Graphic" object property via script (RT Unified)](#dynamizing-graphic-object-property-via-script-rt-unified)
- [Dynamic object property with flashing via script (RT Unified)](#dynamic-object-property-with-flashing-via-script-rt-unified)
- [Dynamizing the flashing of an object property via user-defined function (RT Unified)](#dynamizing-the-flashing-of-an-object-property-via-user-defined-function-rt-unified)
- [Dynamizing "Screen" object property via tag (RT Unified)](#dynamizing-screen-object-property-via-tag-rt-unified)

##### Dynamize "Graphic" object property via tag (RT Unified)

###### Introduction

You can use a tag to dynamize a property containing a graphic.

The following object properties can contain a graphic:

- Graphic (e.g. a list box)
- Graphic - pressed button (e.g. a button)
- Background graphic (one screen only)
- Marker graphic (e.g. an alarm control)
- Icon (e.g. a trend control)

###### Task

In this example, you can learn how to dynamize the "Graphic" property at the "Button" object via a tag of the "Range" type.

You configure:

- Button
- HMI tag "MyTag"
- Graphic in the project graphics

###### Requirement

- A project is open.
- A screen is configured.
- A button is configured in the screen.

###### Adding a graphic

To add a graphic to the project graphics, follow these steps:

1. In the project tree under "Languages and resources > Project graphics", add a graphic, e.g. "Icon_filter", from your storage location.

###### Configuring the HMI tag

To configure the HMI tag for die dynamization of the "Graphic" property, follow these steps:

1. Configure a "MyTag" tag of the data type "WString" in the project tree under "HMI tags".
2. In the Inspector window of the "MyTag" tag under "Properties > Properties > Values", enter the name of the added "Icon_filter" graphic in the "Start value" input field.

   ![Configuring the HMI tag](images/155920563595_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the HMI tag](images/155920563595_DV_resource.Stream@PNG-en-US.png)

###### Dynamizing the "Graphic" property via tag

Follow these steps to dynamize the "Graphic" property at the "Button" object via the "MyTag" tag of the "Range" type:

1. Click "Properties > Properties > General > Graphic" in the Inspector window of the screen editor. In the drop-down list of the "Dynamization" column, select the entry "Tag".

   ![Dynamizing the "Graphic" property via tag](images/155849206795_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing the "Graphic" property via tag](images/155849206795_DV_resource.Stream@PNG-en-US.png)

   The "Tag" dialog opens.
2. Click on the selection button ![Dynamizing the "Graphic" property via tag](images/155852251275_DV_resource.Stream@PNG-de-DE.png) under "Tag > Process > Tag".

   A dialog opens.
3. Add the "MyTag" tag.
4. Select the "Range" type under "Tag > Type". Define the conditions.
5. Select the graphic in the "Graphic" column.

   ![Dynamizing the "Graphic" property via tag](images/155855063051_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing the "Graphic" property via tag](images/155855063051_DV_resource.Stream@PNG-en-US.png)
6. Click on the selection button ![Dynamizing the "Graphic" property via tag](images/155862853387_DV_resource.Stream@PNG-de-DE.png) under "Tag > Type" in the "Graphic" column.

   A dialog opens.

   ![Dynamizing the "Graphic" property via tag](images/155862843019_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing the "Graphic" property via tag](images/155862843019_DV_resource.Stream@PNG-en-US.png)

   Select the graphic that you have stored in the project graphics.
7. Load the project into the device.

###### Result

All graphics in the project graphics are loaded into the runtime. You can use the name of the selected graphic in the tag. The graphic is displayed on the button in runtime.

If the "IntTag" tag is in the range "0 - 1" in runtime, the selected graphic is visible in the button.

##### Dynamizing "Graphic" object property via script (RT Unified)

###### Introduction

You can use a script to dynamize a property that contains a graphic.

###### Task

In this example you dynamize the "Graphic" property of the "Trend control" object via a script.

###### Requirement

- A project is open.
- A screen is configured.
- A trend control is configured in the screen.
- An HMI tag "MyTag" of the data type "Int" is configured with the start value "10".

###### Dynamizing the "Graphic" property via script

To dynamize the "Graphic" property of a trend control button via a script, follow these steps:

1. Select the trend control in the "Screens" editor.
2. In the Inspector window, click on "Properties > Properties > Miscellaneous > Toolbar > Elements > [2] Button > Graphic". In the drop-down list of the "Dynamization" column, select the entry "Script".

   ![Dynamizing the "Graphic" property via script](images/156951171979_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing the "Graphic" property via script](images/156951171979_DV_resource.Stream@PNG-en-US.png)

   The "Scripts" editor opens.
3. Click ![Dynamizing the "Graphic" property via script](images/157268048907_DV_resource.Stream@PNG-de-DE.png).

   A dialog opens.
4. Add the "MyTag" tag as a trigger of the script which initiates dynamization in runtime.

   ![Dynamizing the "Graphic" property via script](images/156956185355_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing the "Graphic" property via script](images/156956185355_DV_resource.Stream@PNG-en-US.png)
5. Add the following code in the "Scripts" editor:

Copy code

var value;

let tag = Tags("MyTag");

let tagValue = tag.Read();

HMIRuntime.Trace("Value of MyTag: " + tagValue);

switch (tagValue) {

case 10:

   value = HMIRuntime.Resources.Graphics("GraphicCollection.Up_Arrow").Name;

   break;

case 20:

   value = HMIRuntime.Resources.Graphics("GraphicCollection.Down_Arrow").Name;

   break;

}

return value;

###### Result

The graphic property is dynamized via a script. The return value of the script specifies the graphic of the trend diagram button in runtime.

If the "MyTag" HMI tag assumes the value "10" or "20" in runtime, the respective graphic is displayed in the button.

##### Dynamic object property with flashing via script (RT Unified)

###### Introduction

You can display objects as flashing in runtime. You can configure the flashing characteristics for each color setting of an object that supports flashing in the Inspector window.

The flashing in runtime does not change the color value of the property.

###### Task

In this example you dynamize a property with flashing.

You configure:

- Colors
- Flashing condition
- Flashing frequency

###### Requirement

- A screen is open.
- An object is configured.
- An object property supports the dynamization type "Script".

###### Dynamizing an object property with flashing using a script

To dynamize an object property with flashing using a script, follow these steps:

1. Select the object.
2. In the Inspector window under "Properties", select the property for which you want to define the flashing characteristics, for example, "Background color".
3. In the "Dynamization" column, select the "Script" option. The right part of the Inspector window is displayed.
4. Enter a matching script.

   - To deactivate flashing, enter the following script:

     `Screen.Items("Circle").PropertyFlashing("BackColor", false);`
   - To activate flashing, enter the following script:

     `Screen.Items("Circle").PropertyFlashing("BackColor", true);`
   - To activate flashing and to define the properties, enter the following script:

     `Screen.Items("Circle").PropertyFlashing("BackColor", true, HMIRuntime.Math.RGB(255, 0, 0), HMIRuntime.Math.RGB(0, 255, 0), UI.Enums.HmiFlashingRate.Fast);`

> **Note**
>
> For dynamization of a faceplate, replace the term "Screen" with "Faceplate" in the script.

| Symbol | Meaning |
| --- | --- |
| ![Dynamizing an object property with flashing using a script](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |
| You can find snippets for flashing in the shortcut menu of the "Scripts" editor under "Snippets > HMI Runtime > Screen" |  |

###### Result

The object property is dynamized with flashing with the dynamization type "Script". When the configured condition occurs in runtime, the object property flashes in the configured colors and at the set rate.

##### Dynamizing the flashing of an object property via user-defined function (RT Unified)

###### Introduction

You can display objects as flashing in runtime. You can configure the flashing characteristics for each color setting of an object that supports flashing in the Inspector window.   
You select the colors, the condition, and the flashing frequency.

> **Note**
>
> Flashing in runtime does not change the color value of the property.

###### Requirement

- A screen is open.
- An object is configured.
- The object property supports the dynamization type "Flashing".

###### Dynamizing object property with flashing via user-defined function

If you want to enable flashing via a user-defined function at an event, select the condition "Never" for the "Flashing" option at the relevant property under "Properties > Properties > Dynamization".

To dynamize an object property with flashing via a user-defined function, follow these steps:

| Symbol | Meaning |
| --- | --- |
| 1. Select the object that is to trigger flashing, e.g. a button. 2. In the Inspector window, under "Events", select the event to trigger flashing, e.g. "Press". 3. Select the "Convert function list to script" button. 4. To enable flashing, enter the following script, for example:      `Screen.Items("flashObject").PropertyFlashing("BackColor", true);`     - `flashObject` is an object that flashes when the user-defined function is triggered.    - `BackColor` represents the property that is flashing.To activate flashing and to define the properties, enter the following script:     - `Screen.Items("flashObject").PropertyFlashing("BackColor", true, HMIRuntime.Math.RGB(255, 0, 0), HMIRuntime.Math.RGB(0, 255, 0), UI.Enums.HmiFlashingRate.Fast);`      | Symbol | Meaning |    | --- | --- |    | ![Dynamizing object property with flashing via user-defined function](images/145494195723_DV_resource.Stream@PNG-de-DE.png)      ![Dynamizing object property with flashing via user-defined function](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for working effectively** |    | You can find snippets for flashing in the shortcut menu of the "Scripts" editor under "Snippets > HMI Runtime > Screen" |  | 5. Select the object that you want to flash. 6. Select the property that is to flash, e.g. the background color. 7. Make the following setting for the property:    - Condition: "Never"    - If not already defined by the script, set different values for color and alternative color.      Define the frequency. |  |

The object property is dynamized with flashing via a user-defined function.

When the configured condition occurs in runtime, the object property flashes in the configured colors and at the set rate.

> **Note**
>
> For dynamization of a faceplate, replace the term "Screen" with "Faceplate" in the script.

###### Result

The object property is dynamized with flashing via the user-defined function. When the configured condition occurs in runtime, the object property flashes in the configured colors and at the set rate.

##### Dynamizing "Screen" object property via tag (RT Unified)

You can dynamize the "Screen" property of a screen window via a tag. The tag can use the name or number of a screen.

###### Task

In this example, dynamize the "Screen" property of the "Screen window" object via a tag that uses a screen number.

You configure:

- Screen
- Screen window
- HMI tag "ScreenNumber"

###### Requirement

- A project is open.
- A screen is configured and set as the start screen.
- A screen window is configured in the start screen.

###### Configuring the HMI tag

Follow these steps to configure the HMI tag for dynamization of the property:

1. Configure a "ScreenNumber" tag of the data type "Int" in the project tree under "HMI tags".

   The data type defines the type of screen referencing:

   - "Int": Dynamization uses the screen number of a screen.
   - "WString": Dynamization uses the name of a screen.
2. In the Inspector window of the "ScreenNumber" tag under "Properties > Properties > Values", enter the screen number "1" in the "Start value" input field.

   ![Configuring the HMI tag](images/160962507403_DV_resource.Stream@PNG-en-US.png)

   ![Configuring the HMI tag](images/160962507403_DV_resource.Stream@PNG-en-US.png)

###### Configuring a new screen

To configure a screen for display in the screen window, follow these steps:

1. Configure a new screen in the project tree under "Screens".
2. Enter the screen number "1" in the Inspector window of the "Screens" editor under "Properties > Properties > Miscellaneous > Screen number".

   ![Configuring a new screen](images/160960936843_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a new screen](images/160960936843_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The value of the screen number under all configured screens must be unique and greater than "0".

###### Dynamizing the "Screen" property via tag

Proceed as follows to dynamize the "Screen" property at the "Screen window" object via the "ScreenNumber" tag:

1. In the "Screens" editor of the start screen, select the "Screen window" object.
2. In the Inspector window, click "Properties > Properties > General > Screen". In the drop-down list of the "Dynamization" column, select the entry "Tag".

   ![Dynamizing the "Screen" property via tag](images/160962497035_DV_resource.Stream@PNG-en-US.png)

   ![Dynamizing the "Screen" property via tag](images/160962497035_DV_resource.Stream@PNG-en-US.png)

   The "Tag" dialog opens.
3. Click on the selection button ![Dynamizing the "Screen" property via tag](images/155852251275_DV_resource.Stream@PNG-de-DE.png) under "Tag > Process > Tag".

   A dialog opens.
4. Add the "ScreenNumber" tag.
5. Download the project to the device.

###### Result

The screen with screen number "1" is displayed in runtime in the screen window.

If the integer value of the HMI tag "ScreenNumber" changes in runtime, the screen with the corresponding screen number is displayed in the screen window.

## Trigger events (RT Unified)

This section contains information on the following topics:

- [Basics on the events (RT Unified)](#basics-on-the-events-rt-unified)
- [Triggering "Activated" and "Deactivated" events (RT Unified)](#triggering-activated-and-deactivated-events-rt-unified)
- [Triggering a "Press" event (RT Unified)](#triggering-a-press-event-rt-unified)
- [Triggering a "Release" event (RT Unified)](#triggering-a-release-event-rt-unified)
- ["Press key" and "Release key" events: (RT Unified)](#press-key-and-release-key-events-rt-unified)
- [Trigger "Click left mouse button" event (RT Unified)](#trigger-click-left-mouse-button-event-rt-unified)
- [Trigger "Click right mouse button" event (RT Unified)](#trigger-click-right-mouse-button-event-rt-unified)
- [Triggering the "Input finished" event (RT Unified)](#triggering-the-input-finished-event-rt-unified)
- ["Loaded" event (RT Unified)](#loaded-event-rt-unified)
- ["Cleared" event (RT Unified)](#cleared-event-rt-unified)
- ["Connected" event (RT Unified)](#connected-event-rt-unified)
- [Triggering the "Status changed" event (RT Unified)](#triggering-the-status-changed-event-rt-unified)
- [Trigger "Command fired" event (RT Unified)](#trigger-command-fired-event-rt-unified)
- [Trigger "Gesture detected" event (RT Unified)](#trigger-gesture-detected-event-rt-unified)
- [Triggering events through touch operation (RT Unified)](#triggering-events-through-touch-operation-rt-unified)
- [Example: Configure the system function "Screen change" (RT Unified)](#example-configure-the-system-function-screen-change-rt-unified)
- [Events on the "Media Player" object (RT Unified)](#events-on-the-media-player-object-rt-unified)
- [Events on the "Plant overview" object. (RT Unified)](#events-on-the-plant-overview-object-rt-unified)
- [Events on the "GRAPH overview" object (RT Unified)](#events-on-the-graph-overview-object-rt-unified)

### Basics on the events (RT Unified)

#### Introduction

In runtime, an event triggers an action that you have configured on an object.

#### Basics on the events

You can configure one or multiple events on an object. You program a script on an event. The script defines an action that is executed in runtime when the operator triggers a specific event by operating the object.

The available events depend on the object being used.

#### Events

The following table shows the available events:

| Event | Description |
| --- | --- |
| Activated | Mouse operation: Occurs when the operator presses the left or right mouse button.  Touch operation: Occurs when the operator touches the screen with the finger.  Keyboard operation: Occurs when the operator selects an object using the configured tab sequence.   The "Activated" event is only used to detect whether an object was selected. The event does not trigger a password prompt. For this reason, do not use the "Activated" event if you want to configure access protection on the function call of the object. |
| Deactivated | Occurs when the operator takes the focus off an object by activating a different object.  System functions or user-defined functions on the "Deactivated" event of an object are not executed with a screen change.   The "Deactivated" event is only used to detect whether an object was deselected. The event does not trigger a password prompt. For this reason, do not use the "Deactivated" event if you want to configure access protection on the function call of the object. |
| Press | Mouse operation: Occurs after the "Activated" event when the operator presses the left or right mouse button.  Touch operation: Occurs when the operator touches the screen with the finger.  Keyboard operation: Occurs when an object has the focus, and the operator presses either the <Return> or <Space> key. |
| Release | Mouse operation: Occurs when the operator releases the left or right mouse button.  Touch operation: Occurs when the operator takes the finger off the screen. When a motion is detected, the "Release" event is triggered at the limit of a different screen object.  Keyboard operation: Occurs when the operator releases one of the buttons <Return> or <Space>. |
| Press key | Keyboard operation: Occurs when the operator presses a key on the keyboard. The event is not triggered if one of the buttons <Return> or <Space> is pressed.   The event is not supported for Unified Panel. |
| Release key | Keyboard operation: Occurs when the operator releases a key on the keyboard.  The event is not supported for Unified Panel. |
| Trigger hotkey | Occurs when the operator presses a hotkey on the keyboard. |
| Left-click | Mouse operation: Occurs when the system detects a click with the left mouse button, i.e. shortly after the "Release" event.  Touch operation: Occurs after the "Release" event has occurred and if less than a second has elapsed since the "Press" event. |
| Click right mouse button | Mouse operation: Occurs when the system detects a click with the right mouse button, i.e. immediately after the "Release" event.  Touch operation: Occurs after the "Release" event has occurred and if more than a second has elapsed since the "Press" event. |
| Input finished | Occurs when the operator has entered the custom values in an IO field. |
| Loaded | Occurs when a screen is fully loaded in runtime after a screen change. |
| Cleared | Occurs when the active screen is not loaded in runtime. |
| Connected | Occurs when the object has been successfully initialized and the data connection to the controller has been established. |
| Status changed | Occurs when the state of the switch changes, for example, from "On" to "Off". |
| Command fired | Occurs when the operator has actuated a button in the toolbar or information bar. |
| Gesture detected | Occurs when the operator performs a touch gesture. |
| Play | Occurs when the video or audio file is being replayed. |
| Pause | Occurs when playing of the video or audio file is paused. |
| Playback finished | Occurs when the video or audio file has been played. |
| Selection changed | Occurs when the selection is changed. |
| Expand | Occurs when all plant objects under a node are displayed. |
| Expand all | Occurs when all plant objects are displayed. |
| Minimize | Occurs when all plants objects under a node are hidden. |
| Minimize all | Occurs when all plant objects are hidden. |
| Alarm control - Button touched | Occurs when the operator touches the "Jump to the alarm control button" in the "GRAPH overview" object. |
| PLC code view - Button touched | Occurs when the operator touches the "Jump to the PLC code view" button in the "GRAPH overview" object. |
| TIA Portal - Button touched | Occurs when the operator touches the "Jump to the TIA Portal" button in the "GRAPH overview" object. |

#### Example

The figure below shows the event "Click left mouse button" as an example:

When you want to trigger an event by clicking with the left mouse button, follow these steps:

1. Click on the object with the left mouse button.   
   The system detects the operation and triggers the "Activated" and "Pressed" events.
2. Release the left mouse button.  
   The system detects the operation and triggers the events "Release" and "Click left mouse button".

![Example](images/151923762315_DV_resource.Stream@PNG-en-US.png)

### Triggering "Activated" and "Deactivated" events (RT Unified)

#### Introduction

You can trigger the event "Activated" and "Deactivated" through movement with the left or right mouse button, on the touchscreen or through keyboard operation.

When an object has the focus, the "Activated" event is automatically triggered before the "Pressed" event.

#### "Activated" event

You have the following options to trigger the "Activated" event:

- Mouse operation: Press the left or right mouse button.
- Touch operation: Touch the screen using your finger.
- Keyboard operation: Select an object using the configured tab sequence.

#### "Deactivated" event

You trigger the "Deactivated" event when you take the focus off an object by activating a different object.

In case of a screen change, the "Deactivated" event of an object is triggered but the system functions or user-defined functions on the "Deactivated" event are not executed.

The "Deactivated" event is only used to detect whether an object was deselected. The event does not trigger a password prompt. For this reason, do not use the "Deactivated" event if you want to configure access protection on the function call of the object.

### Triggering a "Press" event (RT Unified)

#### Introduction

You can trigger the "Press" event through movement with the left or right mouse button, on the touchscreen or through keyboard operation.

When an object has the focus, the "Activated" event is automatically triggered before the "Press" event.

#### "Press" event

You have the following options to trigger the "Press" event:

- Mouse operation: Occurs when you press the left or right mouse button.
- Touch operation: Occurs when you touch the screen with your finger.
- Keyboard operation: Occurs when an object has the focus, and you press either the <Return> or <Space> key.

The figure below shows the "Activated" and "Press" events:

!["Press" event](images/151923952907_DV_resource.Stream@PNG-en-US.png)

### Triggering a "Release" event (RT Unified)

#### Introduction

You can trigger the event "Release" through movement with the left mouse button or on the touchscreen.

#### "Release" event by moving in the object with the mouse

When you want to trigger the event "Release" through the mouse operation, follow these steps:

1. Click on the object with the left mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Move with the mouse in the object in x and/or y direction.
3. Release the left mouse button.

   Releasing triggers the "Release" event.

   The "Click left mouse button" event is not triggered.

#### "Release" event by movement in the object using touch control

When you want to trigger the event "Release" through the touch operation, follow these steps:

1. Touch the object using your finger.

   Touching triggers the "Activated" and "Press" events.
2. Move with your finger in the object in x and/or y direction.
3. Release the object.

   The releasing triggers the "Release" event.

!["Release" event by movement in the object using touch control](images/151924071179_DV_resource.Stream@PNG-en-US.png)

#### "Release" event by moving over the object boundary with the mouse

When you want to trigger the event "Release" through the mouse operation, follow these steps:

1. Click on the object with the left mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Move with the mouse in x and/or y direction beyond the object limit.
3. Release the left mouse button.

   Releasing triggers the "Release" event.

   The "Click left mouse button" event is not triggered.

If you continue moving with the finger in the object instead of releasing it, no additional event is triggered.

After you release the finger or the mouse button outside of the object, no additional event is triggered.

#### "Release" event by movement over the object boundary using touch operation

When you want to trigger the event "Release" through the touch operation, follow these steps:

1. Touch the object using your finger.

   Touching triggers the "Activated" and "Press" events.
2. Move with your finger in the object in x and/or y direction beyond the object limit.
3. Release the object.

   The releasing triggers the "Release" event.

!["Release" event by movement over the object boundary using touch operation](images/151924088331_DV_resource.Stream@PNG-en-US.png)

#### "Release" event by movement into another object

Releasing the left mouse button or finger after reaching the object boundary triggers the "Release" event.

If you move with the left mouse button or finger in another object, no further event will be triggered.

!["Release" event by movement into another object](images/151924131083_DV_resource.Stream@PNG-en-US.png)

#### Objects with a slide bar

When you click on objects with a slide bar, for example, slider or bar, with the left mouse button or touch them on the touchscreen, the movement of the slide bar is started. The "Release" event is not triggered at the object limit but only after the release.

The "Click left mouse button" event is not triggered.

#### Restrictions on the screen objects with the "Release" event

Make sure that screen objects with a configured "Release" event are not impaired in their function during the operation in runtime.

If you have configured a "Release" event for a screen object, for example for a button, the configured function is not executed if:

- If the button is pressed in runtime and a popup opens in the meantime, for example, covering the button.
- The position of the button changes by zooming or scrolling.
- During a screen change.

### "Press key" and "Release key" events: (RT Unified)

#### Introduction

You can trigger the "Press key" and "Release key" events by keyboard action.

The behavior of the <Return> and <Space> keys differs from the behavior of the other keys on the keyboard.

#### Using key on the keyboard

If you want to trigger the "Release key" event by keyboard action, follow these steps:

1. Press a key on the keyboard.

   The "Press key" event is triggered.
2. Release the key.

   The "Release key" event is triggered.

![Using key on the keyboard](images/151925477387_DV_resource.Stream@PNG-en-US.png)

#### Using the <Return> or <Space> key

The keys <Return> and <Space> can trigger direct actions, for example, for button or rectangle.

When you want to trigger the events through the keys <Return> or <Space>, follow these steps:

1. Select an object on which you have configured an event.
2. Press the <Return> or <Space> key.

   The "Press" and "Press key" events are triggered.
3. Release the key.

   The "Release key", "Release" and "Click left mouse button" events are triggered.

![Using the <Return> or <Space> key](images/151925494539_DV_resource.Stream@PNG-en-US.png)

#### Objects with selection elements

In the objects with selection elements, e.g. check box, the <Return> key behaves like any key.

You can use the <Space> key, for example to change the selection from "On" to "Off" or to trigger an event.

### Trigger "Click left mouse button" event (RT Unified)

#### Introduction

You can trigger the event "Click left mouse button" by clicking with the left mouse button.

#### "Click left mouse button" event

When you want to trigger the "Click left mouse button" event through mouse action, follow these steps:

1. Click on the object with the left mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release" and "Click left mouse button" events.

!["Click left mouse button" event](images/151924299275_DV_resource.Stream@PNG-en-US.png)

### Trigger "Click right mouse button" event (RT Unified)

#### Introduction

You can trigger the event "Click right mouse button" by clicking with the right mouse button.

#### "Click right mouse button" event

When you want to trigger the event "Click right mouse button" through mouse operation, follow these steps:

1. Click on the object with the right mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Release the right mouse button.

   Releasing triggers the "Release" and "Click right mouse button" events.

!["Click right mouse button" event](images/151924493067_DV_resource.Stream@PNG-en-US.png)

### Triggering the "Input finished" event (RT Unified)

#### Introduction

You can trigger the "Input finished" event by operating the "IO field" object. For example, you can script this event to check whether the value you entered is within the defined limits.

#### Triggering the "Input finished" event by mouse action

If you want to trigger the "Input finished" event by mouse action, follow these steps:

1. Left-click on the "IO field" object.
2. Enter a value.
3. Confirm the entry by pressing <Return> or by left-clicking on another object.

   Clicking or pressing triggers the "Input finished" event.

#### Triggering the "Input finished" event by touch operation

If you want to trigger the "Input finished" event by touch operation, follow these steps:

1. Touch the "IO field" object using your finger.
2. Enter a value.
3. Touch another object with your finger.

---

**See also**

[IO field (RT Unified)](#io-field-rt-unified)

### "Loaded" event (RT Unified)

The "Loaded" event occurs when a screen is fully loaded after a screen change or runtime start.

### "Cleared" event (RT Unified)

The "Cleared" event occurs when the active screen is not loaded in runtime.

### "Connected" event (RT Unified)

The "Connected" event occurs when the data connection between an object, for example a trend control, and the controller has been established.

### Triggering the "Status changed" event (RT Unified)

#### Introduction

You can trigger the "Status changed" event by operating the "Switch" object.

#### Trigger "Status changed" event by mouse operation

When you want to trigger the "Status changed" event through mouse operation, follow these steps:

1. Click with the left mouse button on the "Switch" object.

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and "Status changed" events.

#### Trigger "Status changed" event by touch operation

When you want to trigger the "Status changed" event using touch operation, follow these steps:

1. Touch the object using your finger.

   Touching triggers the "Activated" and "Press" events.
2. Release the object.

   Releasing triggers the "Release", "Click left mouse button" and "Status changed" events.

![Trigger "Status changed" event by touch operation](images/151924600459_DV_resource.Stream@PNG-en-US.png)

### Trigger "Command fired" event (RT Unified)

#### Introduction

You can trigger the "Command fired" event by operating a button in the object, e.g. "Alarm control".

#### Trigger "Command fired" event by mouse operation

When you want to trigger the event "Command fired" through mouse operation, follow these steps:

1. Click on a button in the "Alarm control" object with the left mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and "Command fired" events.

#### Triggering a "Command fired" event by touch operation

When you want to trigger the "Command fired" event through touch operation, follow these steps:

1. Touch a button in the "Alarm control" object with your finger.

   Touching triggers the "Activated" and "Press" events.
2. Release the object.

   Releasing triggers the "Release", "Click left mouse button" and "Command fired" events.

![Triggering a "Command fired" event by touch operation](images/151924627851_DV_resource.Stream@PNG-en-US.png)

### Trigger "Gesture detected" event (RT Unified)

#### Introduction

The "Gesture detected" event occurs when the operator has performed a touch gesture.

#### Distinguish gestures

The "Touch Area" object distinguishes between the following gestures:

- Right
- Left
- Up
- Down

#### Programming a J-script

To distinguish between the gestures, program a J-Script that evaluates the gesture.

1. Click ![Programming a J-script](images/130773202443_DV_resource.Stream@PNG-de-DE.png) in the Inspector window under "Properties > Events > Gesture detected".
2. Copy the code example into the programming window.

Code example

export function Touch_area_1_OnGestureDetected(item, gesture) {

// value of tag ‚MyTag1‘ will be set depending on the detected gesture

if(gesture == UI.Enums.HmiGesture.SwipeRight)

{

UI.RootWindow.Screen = 'ScreenRight';

let tag1 = Tags('tag1');

tag1.Write(1); //write value '1234' to tag 'MyTag1'

}

if(gesture == UI.Enums.HmiGesture.SwipeLeft)

{

UI.RootWindow.Screen = 'ScreenLeft';

let tag1 = Tags('tag1');

tag1.Write(2); //write value '1234' to tag 'MyTag1'

}

if(gesture == UI.Enums.HmiGesture.SwipeUp)

{

UI.RootWindow.Screen = 'ScreenUp';

let tag1 = Tags('tag1');

tag1.Write(3); //write value '1234' to tag 'MyTag1'

}

if(gesture == UI.Enums.HmiGesture.SwipeDown)

{

UI.RootWindow.Screen = 'ScreenDown';

let tag1 = Tags('tag1');

tag1.Write(4); //write value '1234' to tag 'MyTag1'

}

if(gesture == UI.Enums.HmiGesture.Unknown)

{

let tag1 = Tags('tag1');

tag1.Write(0); //write value '1234' to tag 'MyTag1'

}

}

### Triggering events through touch operation (RT Unified)

#### Introduction

You can trigger events by touching the object on the touchscreen.

> **Note**
>
> Touch gestures and "Press" and "Release" events are not supported for client access of a PC with a touchscreen to a SmartServer.

#### Limit value

The time between touching and releasing the object on the touchscreen decides which of the events is triggered.

If the time between touching and releasing (t3 – t2) the object is less than the specified limit, releasing the pressed object on the touchscreen triggers the event "Click left mouse button".

If the time between touching and releasing (t3 – t2) the object is greater than the specified limit, releasing the pressed object on the touchscreen triggers the event "Click right mouse button".

> **Note**
>
> If not specified by the operating system or the Web control, the limit value is 1 000 ms.

#### Simulating clicking with the left mouse button

If you want to trigger the "Click left mouse button" event through touch operation, follow these steps:

1. Touch the object using your finger.

   Touching triggers the "Activated" and "Press" events.
2. Release the object within the limit.

   Releasing triggers the "Release" and "Click left mouse button" events.

![Simulating clicking with the left mouse button](images/151925585291_DV_resource.Stream@PNG-en-US.png)

#### Simulating clicking with the right mouse button

If you want to trigger the "Click right mouse button" event through touch operation, follow these steps:

1. Touch the object using your finger.

   Touching triggers the "Activated" and "Press" events.
2. Release the object after the limit has expired.

   Releasing triggers the "Release" and "Click right mouse button" events.

![Simulating clicking with the right mouse button](images/151925653643_DV_resource.Stream@PNG-en-US.png)

### Example: Configure the system function "Screen change" (RT Unified)

#### Task

In this example you configure the system function "Screen change".

#### Requirement

- A project is open.
- A screen is configured.

#### Configure the system function "Screen change"

To configure a "Screen change" system function, follow these steps:

1. Create a screen "Screen1" and drag, for example, a button into the screen.
2. Create a screen "Screen2" and drag, for example, a circle into the screen.

#### Configuring "Screen1"

To add the "Click left mouse button" event to the button in "Screen1", follow these steps:

1. Select the button and click "Click left mouse button" under "Events".
2. Click "Add script". A "Script" window is opened.
3. Click on the first curly bracket in the script. The bracket turns green.
4. Under "Code templates > HMIRuntime > Screen", select the function "Change base screen".
5. Drag and drop the function to the bracket. Enter "Screen2" in the script.
6. Click "OK".

#### Configuring "Screen2"

To add the "Click left mouse button" to the circle in "Screen2", follow these steps:

1. Select the circle and click "Click left mouse button" under "Events".
2. Click "Add script". A "Script" window is opened.
3. Click on the first curly bracket in the script. The bracket turns green.
4. Under "Code templates > HMIRuntime > Screen", select the function "Change base screen".
5. Drag and drop the function to the bracket, and write "Screen1" in the script.
6. Click "OK".

#### Loading the project and starting runtime

To load the project and start runtime, follow these steps:

1. Load the project under "Project > Device".
2. Start runtime.
3. Click on the button with the left mouse button. You switch to "Screen2".

#### Result

When you click on the circle with the left mouse button, you switch to "Screen1". When you click on the button with the left mouse button, you switch to "Screen2".

The system function "Screen change" has been configured.

### Events on the "Media Player" object (RT Unified)

This section contains information on the following topics:

- [Triggering a "Play" event (RT Unified)](#triggering-a-play-event-rt-unified)
- [Trigger "Pause" event (RT Unified)](#trigger-pause-event-rt-unified)
- [Triggering a "Playback finished" event (RT Unified)](#triggering-a-playback-finished-event-rt-unified)

#### Triggering a "Play" event (RT Unified)

##### Introduction

You can trigger the "Play" event by operating the "Play" button in the "Media Player" object.

##### Trigger "Play" event by mouse operation

If you want to trigger the "Play" event by mouse operation, follow these steps:

1. Click on the "Play" button in the "Media Player" object with the left mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and "Play" events.

##### Triggering a "Play" event by touch operation

If you want to trigger the "Play" event through the touch operation, follow these steps:

1. In the "Media Player" object, touch the "Play" button with your finger.

   Touching triggers the "Activated" and "Press" events.
2. Release the object.

   Releasing triggers the "Release", "Click left mouse button" and "Play" events.

![Triggering a "Play" event by touch operation](images/151925269643_DV_resource.Stream@PNG-en-US.png)

#### Trigger "Pause" event (RT Unified)

##### Introduction

You can trigger the "Pause" event by operating the "Pause button" in the "Media Player" object.

##### Triggering a "Pause" event by mouse operation

If you want to trigger the "Pause" event through mouse operation, follow these steps:

1. Click on the "Pause" button in the "Media Player" object with the left mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and "Pause" events.

##### Triggering a "Pause" event by touch operation

If you want to trigger the "Pause" event through the touch operation, follow these steps:

1. In the "Media Player" object, touch the "Pause" button with your finger.

   Touching triggers the "Activated" and "Press" events.
2. Release the object.

   Releasing triggers the "Release", "Click left mouse button" and "Pause" events.

![Triggering a "Pause" event by touch operation](images/151925373835_DV_resource.Stream@PNG-en-US.png)

#### Triggering a "Playback finished" event (RT Unified)

##### Introduction

You can trigger the "Playback finished" event by operating the "Stop" button in the "Media Player" object.

##### Triggering a "Playback finished" event by mouse operation

If you want to trigger the "Playback finished" event by mouse operation, follow these steps:

1. Click on the "Stop" button in the "Media Player" object with the left mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and "Playback finished" events.

##### Triggering a "Playback finished" event by touch operation

If you want to trigger the event "Playback finished" by the touch operation, follow these steps:

1. In the "Media Player" object, touch the "Stop" button with your finger.

   Touching triggers the "Activated" and "Press" events.
2. Release the object.

   Releasing triggers the "Release", "Click left mouse button" and "Playback finished" events.

   ![Triggering a "Playback finished" event by touch operation](images/152261157259_DV_resource.Stream@PNG-en-US.png)

### Events on the "Plant overview" object. (RT Unified)

This section contains information on the following topics:

- [Triggering a "Selection changed" event (RT Unified)](#triggering-a-selection-changed-event-rt-unified)
- [Triggering an "Expand" event (RT Unified)](#triggering-an-expand-event-rt-unified)
- [Triggering an "Expand all" event (RT Unified)](#triggering-an-expand-all-event-rt-unified)
- [Triggering a "Minimize" event (RT Unified)](#triggering-a-minimize-event-rt-unified)
- [Triggering a "Minimize all" event (RT Unified)](#triggering-a-minimize-all-event-rt-unified)

#### Triggering a "Selection changed" event (RT Unified)

##### Introduction

You can trigger the "Selection changed" event in the "Plant overview" object by clicking the left mouse button.

##### Triggering a "Selection changed" event

If you want to trigger the "Selection changed" event through mouse operation, follow these steps:

1. Click on a node with the left mouse button.

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and finally "Selection changed" events.

   ![Triggering a "Selection changed" event](images/152197399819_DV_resource.Stream@PNG-en-US.png)

#### Triggering an "Expand" event (RT Unified)

##### Introduction

You can trigger the "Expand" event in the "Plant overview" object by clicking the left mouse button.

##### Triggering an "Expand" event

If you want to trigger the "Expand" event by mouse operation, follow these steps:

1. Left-click on the symbol for "Expand".

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and finally "Expand" events.

   ![Triggering an "Expand" event](images/152196969227_DV_resource.Stream@PNG-en-US.png)

#### Triggering an "Expand all" event (RT Unified)

##### Introduction

You can trigger the "Expand all" event in the "Plant overview" object by clicking the left mouse button.

##### Triggering an "Expand all" event

If you want to trigger the "Expand all" event by mouse operation, follow these steps:

1. Left-click on the symbol for "Expand all".

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and finally "Expand all".

   ![Triggering an "Expand all" event](images/152197088523_DV_resource.Stream@PNG-en-US.png)

#### Triggering a "Minimize" event (RT Unified)

##### Introduction

You can trigger the "Minimize" event in the "Plant overview" object by clicking the left mouse button.

##### Triggering a "Minimize" event

If you want to trigger the "Minimize" event by mouse operation, follow these steps:

1. Left-click on the symbol for "Minimize".

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and finally "Minimize" events.

   ![Triggering a "Minimize" event](images/152196107659_DV_resource.Stream@PNG-en-US.png)

#### Triggering a "Minimize all" event (RT Unified)

##### Introduction

You can trigger the "Minimize all" event in the "Plant overview" object by clicking the left mouse button.

##### Triggering a "Minimize all" event

If you want to trigger the "Release" event by mouse operation, follow these steps:

1. Left-click on the symbol for "Minimize all".

   Clicking triggers the events "Activated" and "Press".
2. Release the left mouse button.

   Releasing triggers the "Release", "Click left mouse button" and finally "Minimize all" events.

   ![Triggering a "Minimize all" event](images/152196952331_DV_resource.Stream@PNG-en-US.png)

### Events on the "GRAPH overview" object (RT Unified)

This section contains information on the following topics:

- [Triggering "Alarm control - Button touched" event (RT Unified)](#triggering-alarm-control---button-touched-event-rt-unified)
- [Trigger "PLC code view - Button touched" event (RT Unified)](#trigger-plc-code-view---button-touched-event-rt-unified)
- [Triggering "TIA Portal - Button touched" event (RT Unified)](#triggering-tia-portal---button-touched-event-rt-unified)

#### Triggering "Alarm control - Button touched" event (RT Unified)

The "Alarm control - Button touched" event occurs when you touch the "Jump to the alarm control" button in the "GRAPH overview" object.

#### Trigger "PLC code view - Button touched" event (RT Unified)

The event "PLC code view - Button touched" occurs when you touch the "Jump to the PLC code view" button in the "GRAPH overview" object.

#### Triggering "TIA Portal - Button touched" event (RT Unified)

The "TIA Portal - Button touched" event occurs when you touch the "Jump to the TIA Portal" button in the "GRAPH overview" object.

## Configuring faceplates (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-1)
- [Creating and managing faceplates (RT Unified)](#creating-and-managing-faceplates-rt-unified)
- [Connecting faceplate types to OPC UA (RT Unified)](#connecting-faceplate-types-to-opc-ua-rt-unified)
- [Dynamizing faceplates (RT Unified)](#dynamizing-faceplates-rt-unified)
- [Example: Creating and using faceplates (RT Unified)](#example-creating-and-using-faceplates-rt-unified)

### Basics (RT Unified)

This section contains information on the following topics:

- [Basics of faceplates (RT Unified)](#basics-of-faceplates-rt-unified)
- [Device dependency of faceplates (RT Unified)](#device-dependency-of-faceplates-rt-unified)
- ["Faceplate types" editor (RT Unified)](#faceplate-types-editor-rt-unified)
- [Lowest device version of a faceplate type (RT Unified)](#lowest-device-version-of-a-faceplate-type-rt-unified)
- [Performance improvement when using a large number of faceplates (RT Unified)](#performance-improvement-when-using-a-large-number-of-faceplates-rt-unified)
- [Faceplates and TIA version upgrade (RT Unified)](#faceplates-and-tia-version-upgrade-rt-unified)

#### Basics of faceplates (RT Unified)

##### Introduction

Faceplates are user-defined groups of display and operating objects that are stored, managed and edited in the project library in a versioned manner. Faceplates are sometimes also referred to as "HMI blocks".

Faceplates support scripting and can therefore also open other faceplates in a pop-up window.

Depending on design and configuration, faceplates can be used universally and easily integrated into existing projects and employed several times.

##### Use

You use faceplates in order to create and re-use individually configured display and operating objects. You can edit faceplates centrally in the faceplate type. This reduces the configuration effort.

Depending on the application, a faceplate is a user-defined simple screen item or a detailed representation of a complex plant component.

Ideally, you should use faceplates for plant objects or parts that you use several times and that have identical data structures.

> **Note**
>
> **Option to compile and load changes is lost**
>
> Please note the following instructions for compiling and loading changes:
>
> - A dialog is often displayed when the option to compile only changes is about to be lost. The change can be confirmed or rejected.
>
>   - If you confirm the change, the complete project must be compiled or loaded.
>   - When you reject the change, the option to compile and load changes is retained.
> - If you use the "Undo" button to undo a change that requires compiling or loading the entire project, the entire project must still be compiled or loaded.
> - For the relevant changes and actions, an alarm is displayed in the Inspector window when the option to load changes is already lost. The entire project must be compiled and loaded.

##### Type/instance concept

Faceplates are based on a type/instance concept.

The faceplate type and its versions are managed centrally in the project library.

An instance of a version of a faceplate type is used in a screen as a faceplate container.

##### Faceplate type

- You create a faceplate type in the project library.
- More than one version of a faceplate type can be created.

##### Faceplate container

The faceplate container is an independent object in which a version of the faceplate type is instantiated.

- Each instance is connected to the faceplate version that has been used.

  This means that if you change a property or the data structure of a faceplate version, this property change immediately affects all faceplate instances that are based on the faceplate version.
- A faceplate container is used just like other display and operating objects in screens.
- If a version of a faceplate type has been instantiated in the container, the corresponding faceplate type is specified in the "Faceplate type of the instance" property.
- The tags and interface properties configured in the version of a faceplate type are linked in the faceplate container.

##### Example

If you use multiple valves within the project, you typically always use the same data structure to control and query the status of these valves. Therefore, it makes sense to use the same display and operating objects for the visualization of these valves.

1. In a faceplate type, you configure how the valve is displayed and which input and output tags the valve has in the form of tags.
2. If required, configure another faceplate type that contains the same data structure and functions as a pop-up window.

   This pop-up window can be called by the first faceplate type using a script.
3. For each valve in the system with the same data structure, instantiate the desired faceplate type and link its tags and PLC user data types with the corresponding valves in the system.

---

**See also**

[Faceplate container (RT Unified)](#faceplate-container-rt-unified)

#### Device dependency of faceplates (RT Unified)

The functionality of the faceplate depends on the lowest device version of a faceplate type.

##### Devices

The following devices support faceplates:

- SIMATIC WinCC Unified PC
- SIMATIC Unified Comfort Panel

---

**See also**

[Lowest device version of a faceplate type (RT Unified)](#lowest-device-version-of-a-faceplate-type-rt-unified)

#### "Faceplate types" editor (RT Unified)

##### Project library

You can create and edit faceplate types in the project library.

##### Layout

![Layout](images/160588084235_DV_resource.Stream@PNG-en-US.png)

To view the tab of the editor, close the note ![Layout](images/149594229387_DV_resource.Stream@PNG-de-DE.png).

##### Visualization

You can design the faceplate type in the "Visualization" tab.

You insert the following objects from the "Tools" task card:

- "Basic objects"
- "Elements"
- "Controls"

  The following controls are available:

  - Alarm control
  - Trend control
  - Faceplate container

    Empty container that you can later connect to a faceplate type.

You can find more information in the section [Overview of screen objects](#overview-of-screen-objects-rt-unified).

You can define the properties of the faceplate type and the objects in the Inspector window under "Properties > Properties". Here, you define display name, appearance and size, for example.

##### Assigning names to tags and properties

> **Note**
>
> **Use unique names**
>
> The name of a tag or a property may be assigned across all tabs only once in a faceplate type.

##### Tags interface

On the "Tag interface" tab, you can configure the interface tags of the faceplate type and link the interface tags to HMI tags.

PLC user data types are supported on the interface.

##### Property interface

On the "Property interface" tab, you can configure the interface properties of the faceplate type.

The properties configured here are available for the instance of the faceplate type under "Miscellaneous > Interface".

You can create interface properties of the following data types:

- 64-bit integer
- Authorization
- Boolean
- Color
- Floating-point number
- Graphic
- Configuration string
- Multilingual text
- Resource list
- Unsigned 64-bit integer

##### Local tags

On the "Local Tags" tab, you can configure tags that are used exclusively within the faceplate type.

For example, you can use local tags in scripts within the faceplate type.

##### Event interface

In the "Event interface" tab, you configure events and associated parameters. You interconnect the events in the "Visualization" tab with the faceplate type or objects in the faceplate type.

On the faceplate container, the events are available under "Properties > Events". You can configure functions of the function list or scripts.

##### Interfaces of faceplate types can be copied

The entries of an interface in a faceplate type can be selected individually or copied in blocks as an entire interface and pasted again in another faceplate type.

This applies to:

- Tags interface
- Property interface
- Local tags
- Event interface

Pasting is also possible at the same place in the faceplate type.

To copy and paste, use the shortcut menu or the shortcut keys <Ctrl> + <C> and <Ctrl> + <V>.

To copy and paste all entries, select the entries by keeping the "Shift" key pressed or by using the keyboard shortcut <Ctrl> + <A> and copy via the shortcut menu or via the keyboard shortcut <Ctrl> + <C>. Insert the entries via the shortcut menu or the keyboard shortcut <Ctrl> + <V>.

#### Lowest device version of a faceplate type (RT Unified)

##### Introduction

When you create the faceplate type, define the lowest device version for the faceplate type.

If you select the highest available device version, all functions are available. If you select a lower device version, some features are not available.

> **Note**
>
> **Configured device version and lowest device version of the faceplate type**
>
> The configured device version of the HMI device in which an instance of the faceplate type is to be used must be equal to or higher than the lowest device version of the faceplate type.
>
> The following changes in the project may cause error messages due to a device version that is too low:
>
> - Changing the configured device version of the HMI device to a lower version
> - Deleting a faceplate type
> - Copying and pasting screens or faceplate containers between different HMI devices
> - Copy screen with a faceplate container from the library to a screen

> **Note**
>
> **TIA Portal version and device version of the faceplate type**
>
> A warning appears when you open a project that contains a faceplate type with a higher device version than the installed TIA Portal version in the project library or as an instance. It is possible to open the project, but the following restrictions apply:
>
> - You cannot open or release the affected faceplate type.
> - You cannot compile the project.
> - If you open a screen that contains an instantiated faceplate type with a higher device version, the faceplate container is shown as empty.

> **Note**
>
> **Upgrading the device version as a bulk operation**
>
> The device version is upgraded as a bulk operation. If upgrading the device version of individual faceplate types fails, e.g. because a faceplate version is still being processed, the operation is stopped with warnings.
>
> In order to investigate the cause of the warnings, use the view log file option.

##### Available functions depending on the device version

| Function | Available as of version |
| --- | --- |
| Interface property of the "Resource list" data type | 16.0.0.0 |
| Interface property of the "Color" data type | 16.0.0.0 |
| Interface property of the "Configuration string" data type | 17.0.0.0 |
| Interface property of the "Authorization" data type | 17.0.0.1 (Update 1) |
| Interface property of the "Multilingual text" data type | 18.0.0.0 |
| Interface property of the "Graphic" data type | 18.0.0.0 |
| Alarm control | 18.0.0.0 |
| Trend control | 18.0.0.0 |
| Arrays from user data types | 18.0.0.0 |
| Arrays from values of simple data types | 18.0.0.0 |
| Link tags of the data type "DateTime" or "LTime" with the PLC tags. | 18.0.0.0 |
| Tags of the "PLCUDT" and "HMIUDT" data type | 18.0.0.0 |
| Using a faceplate type in another faceplate type | 18.0.0.0 |
| Interface events | 18.0.0.0 |
| Local tags | 18.0.0.0 |
| Using dynamic SVG graphics from the library in faceplates | 18.0.0.0 |
| "Suspendable" property for performance optimization | 19.0.0.0 |

#### Performance improvement when using a large number of faceplates (RT Unified)

##### Performance improvement in the Engineering System

To improve performance during the engineering process when using numerous faceplates, activate the "Simplified display of Faceplate Containers" option under "Settings > Visualization > Unified Faceplate".

![Performance improvement in the Engineering System](images/160587084043_DV_resource.Stream@PNG-en-US.png)

The faceplates are displayed in a simplified way when this option is activated in the Engineering System. This change has no effect on the display in Runtime. In Runtime, faceplates are displayed in unrestricted quality.

##### Performance improvement in runtime

To improve the performance in runtime when using a large number of faceplates, use the "Suspendable" property of faceplate types.

The "Suspendable" property of a faceplate type is deactivated by default. To activate the property, select the "Suspendable" option in the faceplate type under "Properties > Properties > Miscellaneous". Faceplate instances of the faceplate type suspend the execution of scripts if their "Visibility" property has been deactivated.

On reactivation of the visibility of a faceplate in runtime, all scripts that are due to be executed for the faceplate are run.

#### Faceplates and TIA version upgrade (RT Unified)

##### Version upgrade from V16 to V17 or higher

Note the following points when upgrading from version V16 to V17 or higher:

- As of V17, faceplates are located in the project library and are managed and used in types and versions.
- To prevent inconsistencies when linking data types, you must copy the user data types used in the PLC to the library before upgrading the version from V16 to V17 or higher.

  To do this, use drag-and-drop to move the PLC user data type to the library under "Project library > Types".
- When upgrading TIA Portal from V16 to V17 or higher, the names of existing faceplate types are automatically converted. In the higher version, the name of the faceplate type is given the version number "_0.0.1" as an extension. If, as a result, the permissible maximum total length of 128 characters is exceeded, an error message is displayed on the HMI device when the project is compiled.

  In this case, shorten the name of the faceplate type.
- The function rights "Function_right_01" to "Function_right_20" assigned to a faceplate in the V16 project are removed during the version upgrade.
- All master copies of faceplate types are removed during the version upgrade.

  Master copies of faceplate types are no longer supported as of V17.

### Creating and managing faceplates (RT Unified)

This section contains information on the following topics:

- [Creating a faceplate type in the project library (RT Unified)](#creating-a-faceplate-type-in-the-project-library-rt-unified)
- [Creating a faceplate type from a screen (RT Unified)](#creating-a-faceplate-type-from-a-screen-rt-unified)
- [Working with faceplate types and versions (RT Unified)](#working-with-faceplate-types-and-versions-rt-unified)
- [Editing the visualization of a faceplate type (RT Unified)](#editing-the-visualization-of-a-faceplate-type-rt-unified)
- [Configuring multilingualism for objects of a faceplate type (RT Unified)](#configuring-multilingualism-for-objects-of-a-faceplate-type-rt-unified)
- [Configuring tags in the faceplate type (RT Unified)](#configuring-tags-in-the-faceplate-type-rt-unified)
- [Interface properties in faceplates (RT Unified)](#interface-properties-in-faceplates-rt-unified)
- [Interface events in faceplates (RT Unified)](#interface-events-in-faceplates-rt-unified)
- [Checking the version consistency and fixing inconsistencies (RT Unified)](#checking-the-version-consistency-and-fixing-inconsistencies-rt-unified)
- [Checking the consistency at the faceplate type and fixing inconsistencies (RT Unified)](#checking-the-consistency-at-the-faceplate-type-and-fixing-inconsistencies-rt-unified)
- [Releasing a faceplate version of a type (RT Unified)](#releasing-a-faceplate-version-of-a-type-rt-unified)
- [Creating a faceplate instance](#creating-a-faceplate-instance)
- [Using a PLC user data type (RT Unified)](#using-a-plc-user-data-type-rt-unified)
- [Using an HMI user data type (RT Unified)](#using-an-hmi-user-data-type-rt-unified)
- [Using a faceplate type in another faceplate type (RT Unified)](#using-a-faceplate-type-in-another-faceplate-type-rt-unified)
- [Copying faceplate types and faceplate instances to other projects (RT Unified)](#copying-faceplate-types-and-faceplate-instances-to-other-projects-rt-unified)

#### Creating a faceplate type in the project library (RT Unified)

##### Introduction

Faceplate types are display and operating objects that are made up of several screen objects, such as I/O fields and controller blocks.

A faceplate type consists of one or more versions.

##### Requirement

The "Libraries" task card is open.

##### Procedure

1. Expand the "Types" folder in the project library.
2. Select the "Add new type" command.

   The "Add new type" dialog opens.
3. Select "HMI faceplate" and select "Unified Comfort Panel / WinCC Unified PC".
4. Enter a descriptive name in the "Name" field.
5. Adapt the lowest device version.

   A new faceplate type with a preliminary faceplate version is created and shown in the project library.

**Note**

The name must satisfy the following conditions:

- Maximum character length: 128 characters
- Unique name
- No special characters:

  # $ +% . / : [ ] ' ~ " `
- No JavaScript elements

##### Result

You have created a new faceplate type with a version. The preliminary faceplate version 0.0.1 is open in the editor and has the status "In progress".

---

**See also**

[Basics of screens (RT Unified)](#basics-of-screens-rt-unified)

#### Creating a faceplate type from a screen (RT Unified)

As an alternative to creating a faceplate type in the project library, you can create a faceplate type directly from a screen of an HMI device. This can be useful, for example, if after configuring screen objects, you find that you want to reuse the screen objects and adapt tags and properties to the new application.

> **Note**
>
> - References to graphics in the "Graphic view" screen object are not transferred and must be inserted again.
> - When tags are used for the dynamization, the reference is resolved as soon as a tag with the same name is created in the tag interface of the faceplate type.
> - Configured function lists at events of screen objects are not transferred and have to be created again.

> **Note**
>
> **Dynamic SVGs**
>
> If you create a faceplate type from a group of selected screen objects, dynamic SVG graphics are not included. To insert a dynamic SVG graphic into a faceplate, open the faceplate type in the editor and insert the SVG graphic from the library here.

##### Requirement

- A screen is configured and open.

##### Procedure

1. Select all the screen objects you want to use in the faceplate type by multiple selection in the screen.
2. Right-click to open the shortcut menu of the selected objects and select "Create faceplate".

   A new faceplate type is created in the project library that contains the copied screen objects and their configured properties.

##### Result

You have created a new faceplate type from a screen. The faceplate type contains the copied screen objects and their properties. The preliminary faceplate version is 0.0.1 and has the status "In progress".

#### Working with faceplate types and versions (RT Unified)

This section contains information on the following topics:

- [Using the toolbar in the editor (RT Unified)](#using-the-toolbar-in-the-editor-rt-unified)
- [Editing a faceplate type (RT Unified)](#editing-a-faceplate-type-rt-unified)
- [Updating a faceplate type (RT Unified)](#updating-a-faceplate-type-rt-unified)
- [Renaming a faceplate type (RT Unified)](#renaming-a-faceplate-type-rt-unified)
- [Opening a faceplate type or version write-protected (RT Unified)](#opening-a-faceplate-type-or-version-write-protected-rt-unified)
- [Replacing a faceplate type (RT Unified)](#replacing-a-faceplate-type-rt-unified)
- [Defining a version as the "default" version (RT Unified)](#defining-a-version-as-the-default-version-rt-unified)
- [Deleting a faceplate type or a version (RT Unified)](#deleting-a-faceplate-type-or-a-version-rt-unified)
- [Duplicating a faceplate type (RT Unified)](#duplicating-a-faceplate-type-rt-unified)
- [Assigning a faceplate version number (RT Unified)](#assigning-a-faceplate-version-number-rt-unified)

##### Using the toolbar in the editor (RT Unified)

###### Introduction

When you open the version of a faceplate type, the toolbar is displayed in the editor.

###### Toolbar

![Toolbar](images/149817466635_DV_resource.Stream@PNG-de-DE.png)

The toolbar provides information about the status of the opened version.

The toolbar allows access to the following functions, depending on the status of the opened version:

- Edit type
- Release version
- Discard changes and delete version
- Check if dependent types need to be adjusted.

###### Minimizing / showing the toolbar

To minimize the toolbar, click on ![Minimizing / showing the toolbar](images/151556342155_DV_resource.Stream@PNG-de-DE.png) or on "x".

To display the toolbar, click ![Minimizing / showing the toolbar](images/151556342155_DV_resource.Stream@PNG-de-DE.png).

##### Editing a faceplate type (RT Unified)

###### Introduction

When you open a released faceplate type for editing, a new version of the faceplate type is created based on the most recent version, "[Default]". When you edit an older version, the new version is based on the selected version.

###### Requirement

A faceplate type has been created.

###### Editing a faceplate type or version

You edit a released faceplate type or a type version as follows:

1. Select the faceplate type or the specific version you want to change.
2. Select "Edit type" from the shortcut menu.

   A new version of the faceplate type is created.

   The new version is opened in the "In progress" status.

   The new version is displayed in the editor.
3. Edit the newly created version.

##### Updating a faceplate type (RT Unified)

###### Introduction

When a faceplate type is updated, all instances of the faceplate type are updated.

###### Requirement

- A faceplate type has been created and released.
- The "Libraries" task card is open.

###### Procedure

1. Select the faceplate type that you want to update.
2. Select "Update types" in the shortcut menu.
3. Select whether you want to update the types in a project or in the library.

   A dialog opens.

   - If "Project" is selected: Select the devices in which you want to perform the update.
   - If "Library" is selected: Select the library in which you want to perform the update.
4. Specify whether the unused type version is going to be deleted from the library.
5. Confirm your selection.

> **Note**
>
> **Updating faceplate types in plant objects**
>
> Note that when faceplate types used in plant objects are updated, the interface assignment and dynamization within the plant object type is deleted if the interface tag or interface property was changed.

###### Result

You have updated all instances of the selected faceplate type in a library or in the project.

##### Renaming a faceplate type (RT Unified)

###### Introduction

You can rename a faceplate type after it has been created. If you have referenced a version of a faceplate type in a script and you then rename the faceplate type, all references are automatically renamed.

###### Procedure

To enter a new name, select the faceplate type in the library.

1. Press <F2>.

   - or -

   In the shortcut menu, select "Rename".
2. Enter a new name.

The name is automatically checked for length, uniqueness and permitted characters. The name is reset to the previous name if the new name does not meet the requirements.

##### Opening a faceplate type or version write-protected (RT Unified)

###### Introduction

You can open a faceplate type or an enabled type version write-protected. In write-protected mode, you can see all configurations within the type version but you cannot make any changes.

###### Requirement

At least one released type version is available in a library.

###### Procedure

To open a faceplate type in write-protected mode, select the faceplate type or a released version in the library.

When you open a faceplate type as read-only, the default version is always opened.

- Select "Open" from the shortcut menu.

  The toolbar is displayed and indicates that the faceplate type version is write-protected.

---

**See also**

[Using the toolbar in the editor (RT Unified)](#using-the-toolbar-in-the-editor-rt-unified)

##### Replacing a faceplate type (RT Unified)

###### Introduction

The "Replace type" function replaces the used versions of a faceplate type in a project with a version of another faceplate type.

The source for replacing faceplate types is always a version. The target is always the enabled version of a faceplate type.

###### Requirement

- The "Libraries" task card is open.
- At least two faceplate types have been created and released.
- The faceplate type is used in the project.

###### Procedure

To replace all instances of the source type with the selected version of the target type, follow these steps:

1. Open the shortcut menu of the faceplate type or the version that you want to replace.

   If a faceplate type is selected for replacement, then the version defined as "Default" is used as the source version to be replaced.
2. Select "Replace type".

   The "Replace type" dialog is displayed.

   All compatible HMI devices and target types are displayed.
3. Select an HMI device.
4. Select a faceplate type.
5. Select a version of the target type.
6. Select "OK".

   A status message is displayed in the Inspector window in the "Info > General" tab.

###### Result

You have replaced the instantiated faceplate type with a different type.

##### Defining a version as the "default" version (RT Unified)

When you add a faceplate type to a library, use types from a library, and release or update versions, the highest released version is used as the "default" version. You can specify another released version as the default version.

###### Requirements

- You have opened the project library or a global library.
- The desired version has been released.

###### Procedure

1. Select a version.
2. Open the shortcut menu.
3. Select "Set as "Default"".

###### Result

The newly set "Default" version is used instead of the highest released version when instantiating, creating, releasing and updating the type.

---

**See also**

[Consistency status of types (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#consistency-status-of-types-rt-unified)

##### Deleting a faceplate type or a version (RT Unified)

Note the following when deleting faceplate types or versions:

- A faceplate type or a version can only be deleted if there are no dependencies on other types.
- When you delete a faceplate type, all versions of the type are deleted.
- When you delete all versions of a faceplate type, the type is also deleted.
- When you delete a version that has instances in the project, the instances are also deleted from the project.
- When you delete a type version with the "default" identifier and no additional versions of this type exist, the type is deleted.
- When you want to delete a type version with the "default" identifier and other versions of this type exist, the "default" identifier must first be assigned to a different version. Versions with the "default" identifier cannot be deleted if other versions of the type exist.
- If you delete a faceplate type or a version which exists in the "Types" folder in a global library, it remains in the global library.

###### Requirement

- The version that is to be deleted is released.
- The faceplate type that is to be deleted contains only released versions.

###### Procedure

1. To delete a faceplate version, select it and press <Del>.

   - or -

   Select "Delete" in the shortcut menu of the version.

   The "Confirm delete" dialog opens.
2. Confirm the delete operation.

   If the faceplate version is used in projects, the "Delete instances of the version" dialog appears, informing you that all instances of the version to be deleted will be removed.
3. Confirm the delete operation.

> **Note**
>
> If a deleted version is referenced in a script, an empty reference remains in the script after deletion. Remove it manually or insert a new reference.

##### Duplicating a faceplate type (RT Unified)

Faceplate types in the project library can be duplicated. When you duplicate a faceplate type, the following applies to the duplicate:

- The duplicate is created in the same folder.
- The duplicate is created from the version of the type with the "default" identifier.
- The duplicate does not have an instance in the project.

###### Requirement

The faceplate type contains at least one released version.

###### Procedure

To duplicate a type in the project library, follow these steps:

1. Select the faceplate type or type version to duplicate.
2. Select "Duplicate type" from the shortcut menu.

   The "Duplicate type" dialog opens.
3. Enter the properties of the new type:

   - Enter a name for the new type in the "Name of type" field.
   - In the "Lowest device version" field, select the device version with which the type should be used.
   - Enter a version number for the new type in the "Version" field.
   - Enter the name of the editor who is responsible in the "Author" field.
   - Enter a comment on the type in the "Comment" field.
4. Confirm with "OK".

   The new faceplate type is generated with a released version.

**Note**

Only device versions that are the same as or higher than the original version can be selected.

##### Assigning a faceplate version number (RT Unified)

A library is more clearly structured if types related by content have the same version number. The identical version number reflects the work progress. When you have completed the work on multiple associated faceplate types, you can assign the same version number to these types.

A log of the changes is created automatically. If you have versioned the faceplate types in the project library, you will find the log in the project tree under "Common data > Logs". If you have versioned the faceplate types in a global library, you will find the log in the "Common data > Logs" folder in the level below the global library.

###### Requirement

- The "Libraries" task card is open.
- Faceplate types with "In progress" status have not been selected.

###### Procedure

To assign the same version to several faceplate types, follow these steps:

1. Select the faceplate types to which you want to assign a common version.

   Press and hold the <Ctrl> key and click on the faceplate types.

   If you have organized types in the library into folders, you can select one or more folders.
2. Select "Assign version" from the shortcut menu.

   The "Assign version" dialog opens.

   ![Procedure](images/160595094923_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/160595094923_DV_resource.Stream@PNG-en-US.png)
3. If necessary, change the properties of the version:

   - In the "Version" field, determine the new version number. The version number must be higher than the highest version number of all selected types.
   - In the "Author" field, enter the person responsible for the version to be released.
   - In the "Comment" field, enter a comment on the version to be released.
4. Confirm with "OK".

###### Result

The selected versions of the faceplate types are changed as follows:

- A new version of all selected faceplate types is created with the specified version number.
- The properties are applied to all selected faceplate types. Lower versions used in the project remain unaffected by the changes. When you make no changes to the properties, the properties of the last released version or the version specified by the user as "default" of each faceplate type are applied.
- When a version is set as "default" by the user, the new version of the selected type is created from the default version with the specified version number. This newly created version will then have the "default" identifier.
- The version number of dependent types is incremented to the next free version number as long as the dependent types were not included in your selection. If you had selected a dependent type as well, the version number you specified will be assigned.

> **Note**
>
> **Assigning a version number based on inconsistency**
>
> Updating the project library with versions of a global library or another TIA Portal instance can result in the project library having two faceplate versions with the same version number created by different authors. This leads to inconsistency and the project cannot be compiled. If this happens, change the version number of one of the duplicate versions.

---

**See also**

[Consistency status of types (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#consistency-status-of-types-rt-unified)

#### Editing the visualization of a faceplate type (RT Unified)

You can edit the visualization on the "Visualization" tab of the editor.

The procedure corresponds to that for editing screens in the "Screens" editor.

##### Requirement

A faceplate type has been created.

##### Editing the visualization

1. Open a version of the faceplate type for editing.

   The visualization of the version is displayed on the "Visualization" tab in the editor.
2. Move objects from the "Toolbox" or "Libraries" task card to the "Visualization" tab of the faceplate version using drag-and-drop.

   Objects from the palettes "Controls" and "My Controls" are not available or only available to a limited extent.

   For dynamic SVG graphics, drag-and-drop pasting is only available as of version V18. If the device version is changed to a version < V18, you will get an error during the compile.

All the editing functions that you already know from configuring screens are available.

You can copy screen objects from one faceplate type to one or more other faceplate types without losing their attributes. If a copied property or tag does not exist in the target faceplate type, the corresponding property or tag is highlighted in red and must be added in the target faceplate type.

> **Note**
>
> Screen objects can only be copied within a TIA Portal project. Copy operations between different TIA Portal instances are not supported.

##### Editing properties

Both the properties of the faceplate type and the properties of the objects used are edited in the Inspector window under "Properties > Properties".

1. Select the object.

   - If you want to adapt the properties of the faceplate type, click in a free area of the editor.
   - If you want to adapt the properties of a used object, click on it.

     The displayed handles indicate the selected object.
2. Open the shortcut menu and select "Properties".

   The Inspector window displays the properties of the object or faceplate type.
3. Edit the properties.

##### Fitting the screen size to its content

With the "Resize screen to content" function, you can automatically adjust the width and height of a faceplate type to the placed objects.

1. Click in a free area of the editor.
2. Open the shortcut menu and select "Resize screen to content".
3. Select the desired margin.

**Result**

- All configured objects of the visualization are framed with the desired margin.
- Objects that are located in a hidden layer are also taken into account.
- The screen size is reduced or enlarged depending on whether the configured objects are located inside the screen or portions of it are located outside the screen.
- The relative positions of the objects to one another are retained.

> **Note**
>
> If objects have been rotated absolutely to the screen, the "Resize screen to content" function may lead to a faulty adjustment.

---

**See also**

[Overview of screen objects (RT Unified)](#overview-of-screen-objects-rt-unified)

#### Configuring multilingualism for objects of a faceplate type (RT Unified)

##### Introduction

The project languages are set in the "Project languages" editor. You specify which project language is to be the editing language and which the reference language.

##### Requirement

- A faceplate type has been created and opened for editing.
- At least one object is configured.

##### Procedure

1. Open the "Languages & Resources" menu command in the project tree.

   The lower-level elements are displayed.
2. Double-click on "Project languages".

   The possible project languages are displayed in the work area.
3. Enable the relevant project languages or disable the languages that you do not need.
4. Go to the project library and open the faceplate type for whose objects you want to create multilingual texts.
5. Select the object for which you want to store a multilingual text.
6. Open the Inspector window under "Properties > Texts" and create the corresponding texts in the set languages.

**Note**

**Copying multilingual objects**

The copies of multilingual objects to a different project only include text objects in the project languages which are activated in the target project. Activate all project languages in the target project to include the corresponding text objects when transferring the copy.

**Note**

If you disable a project language, all text and graphic objects you have already created in this language are disabled from the current project. When the language is re-enabled, these are also re-enabled.

##### Displaying multilingual texts in runtime

To activate the set languages in runtime, follow these steps:

1. Double-click on "Runtime settings" in the project tree.
2. Click on "Language & Font".
3. Enable the required languages.

---

**See also**

[Exporting and importing library texts (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#exporting-and-importing-library-texts-rt-unified)

#### Configuring tags in the faceplate type (RT Unified)

This section contains information on the following topics:

- [Overview (RT Unified)](#overview-rt-unified)
- [Configuring interface tags in the faceplate type (RT Unified)](#configuring-interface-tags-in-the-faceplate-type-rt-unified)
- [Configuring local tags in the faceplate type (RT Unified)](#configuring-local-tags-in-the-faceplate-type-rt-unified)

##### Overview (RT Unified)

###### Introduction

You configure interface tags or local tags in faceplate types. For each tag you define a data type. In addition to simple data types like Bool or Int, you can define arrays.

###### Tags of the data type "DateTime" or "LTime"

You can create tags of the data types "DateTime" or "LTime".

You can link interface tags of the "DateTime" or "LTime" data types, for example, with HMI tags of the data types "DateTime" or "LTime" on the faceplate container.

You can also link interface tags of the "DateTime" or "LTime" data types with the following data types of the S7-1500 PLC:

| Data type of the interface tag | Data types of the PLC S7-1500 |
| --- | --- |
| DateTime | Date |
| DateTime | Date_And_Time |
| DateTime | LDT |
| DateTime | DTL |
| LTime | Time |
| LTime | LTime |
| LTime | Time_Of_Day |
| LTime | LTime_Of_Day |

###### Tags of the "Array" data type

You can define tags of the "Array" data type. The array index begins with 0.

> **Note**
>
> **"WChar", "WString" and "HMIUDT"**
>
> Arrays of "WChar", "WString" and "HMIUDT" data types are not possible.

##### Configuring interface tags in the faceplate type (RT Unified)

###### Introduction

In the faceplate type you can configure interface tags for dynamizing the properties of the objects contained in the faceplate type or embedding in scripts.

The interface tags of a faceplate type are linked exclusively via the faceplate container to the project tags.

> **Note**
>
> **User data types**
>
> User data types, including with nested structures, are supported.
>
> When using PLC user data types, make sure that, if possible, they only contain elements that are actually required for the configuration. Elements that are not needed have a negative impact on the performance when working with faceplate types.

> **Note**
>
> **Subsequent changes to interface tag names**
>
> Note that the values of interfaces that are already connected at the faceplate container are reset to their default values when you subsequently change names in the faceplate type.

###### Requirements

- The faceplate type has been created.
- The version is open for editing.
- The "Tag interface" tab is open in the editor.

###### Defining tags

> **Note**
>
> Only tags of the faceplate type are displayed within the editor.

1. Click on the button ![Defining tags](images/120361298315_DV_resource.Stream@PNG-de-DE.png) "Add Tag" or double-click the "Add" field.
2. Click on the tag name and assign a name. The name can be changed later.
3. Select the data type:

   - To select a simple data type, enter the name of the data type or select a data type from the selection list.
   - To select an array, click the arrow and select the data type.

     To determine the size of the array, enter a numerical value for the array upper limit.

     Example: 3 for an array with 4 elements [0 … 3].

     To convert an array into a simple data type, delete the value for "Array limits".

     ![Defining tags](images/155324401419_DV_resource.Stream@PNG-en-US.png)

     ![Defining tags](images/155324401419_DV_resource.Stream@PNG-en-US.png)

     The WChar, Wstring and HMIUDT data types cannot be created as arrays.
   - To link a data structure, select "PLCUDT" for a PLC user data type or "HMIUDT" for an HMI user data type as the data type.

     Under "User data type structure", select a previously created user data type.

**Note**

The tag name must satisfy the following conditions:

- Maximum character length: 128 characters
- Unique name
- Beginning with a letter or underscore
- No special characters:

  , ; . : ! ? " ' ^ ´ ` ~ - + = / \ ¦ @ * # $ % & § ° ( ) [ ] { } < >
- No spaces
- No JavaScript elements

**Note**

**User data types**

PLCUDT: You create PLC user data types on a PLC in project tree.

HMIUDT: You create HMI user data types in the "Libraries" task card.

###### Changing tags

You can adapt the data type or the array limit of a tag retroactively.

To convert a simple data type into an array, select the arrow in the "Data type" column and specify the top array limit.

To convert an array into a simple data type, select the arrow in the "Data type" column and delete the top array limit.

###### Deleting an interface tag

To delete an interface tag, select the entry you wish to delete and click ![Deleting an interface tag](images/134621778187_DV_resource.Stream@PNG-de-DE.png). Alternatively, delete the tag interface by pressing the <Del> key.

###### Changing the order of the interface tags in the editor

To change the order, select the respective entry and move it gradually up or down by clicking the ![Changing the order of the interface tags in the editor](images/134588594315_DV_resource.Stream@PNG-de-DE.png) buttons.

###### Result

You have configured the interface tags needed for the faceplate type.

The interface tags defined in the faceplate type are accessible in the corresponding faceplate instances and can be used for dynamization and for creating scripts within the faceplate type.

##### Configuring local tags in the faceplate type (RT Unified)

###### Introduction

You can use local tags in a faceplate type to pass on information within the faceplate type. Elements of a faceplate can be dynamized, for example, as a function of the current properties of another element.

The local tags are not visible at an instance of the faceplate type and thus cannot be manipulated.

###### Requirements

- The faceplate type has been created.
- The version is open for editing.
- The "Local tags" tab is open in the editor.

###### Defining local tags

1. Double-click on the "<Add>" cell in the "Name" column.
2. If required, change the suggested name of the tag.
3. Select the data type:

   - Simple data types: Enter the name of the data type or select a data type from the list.
   - Array: Select the "Array" data type. Click the arrow and define the data type and array limit.

**Note**

The tag name must satisfy the following conditions:

- Maximum character length: 128 characters
- Unique name within the faceplate type
- No special characters:

  : . # / % [ ] $ " ' * ? ~

###### Using a local tag

- To display a local tag and manipulate it in Runtime, connect the local tag, e.g. to an I/O field.
- To change the properties, e.g. color, of a screen object in Runtime as a function of the properties of another screen object, dynamize the properties using a local tag.
- If you use local tags in scripts, the events are assigned to the utilized screen objects.

###### Result

You have configured local tags for the faceplate type.

The local tags defined in the faceplate type are not accessible in the instances of the faceplate type.

#### Interface properties in faceplates (RT Unified)

This section contains information on the following topics:

- [Overview (RT Unified)](#overview-rt-unified-1)
- [Configure interface property (RT Unified)](#configure-interface-property-rt-unified)
- [Example: Defining "Configuration string" and using it in a script (RT Unified)](#example-defining-configuration-string-and-using-it-in-a-script-rt-unified)

##### Overview (RT Unified)

###### Introduction

You can define interface properties that you can use later in the faceplate type for the dynamization of properties. The following data types are available:

- 64-bit integer
- Authorization
- Boolean
- Color
- Floating-point number
- Graphic
- Configuration string
- Multilingual text
- Resource list
- Unsigned 64-bit integer

These data types can be instantiated in a faceplate container.

> **Note**
>
> **Changing the names of interface properties**
>
> Note that the values of interfaces that are already connected at the faceplate container are reset to their default values when you subsequently change names in the faceplate type.

###### Description of the interface properties

| Interface property | Description |
| --- | --- |
| 64-bit integer | You can link properties that correspond to an integer with data type "64-bit integer". You can then assign corresponding elements with this numerical value within a screen in the faceplate instance. In this way you can assign different numerical values to objects in different faceplate instances. |
| Authorization | You can link properties of the "Authorization" type with authorizations. You can assign corresponding function rights in the faceplate instance. In this way, you can restrict the operator control of objects in different faceplate instances in different ways.  If you specify the value "None" for the interface property on a faceplate instance, operator control is not restricted. |
| Boolean | You can link properties that correspond to a logical truth value (true and false) with data type "Boolean". You can assign corresponding elements with this value in the faceplate instance. In this way you can assign different values to objects in different faceplate instances. |
| Color | You can link properties of the type "Color" with the data type "Color". You can assign color values in the faceplate instance. In this way the objects can be displayed in different colors in different faceplate instances. |
| Floating-point number | You can link properties corresponding to a floating point number with the "Floating point number" data type. You can assign corresponding numerical values in the faceplate instance. In this way you can assign different numerical values to objects in different faceplate instances. |
| Graphic | You can associate properties that correspond to a graphic with the "Graphic" data type. You link graphics in the "Visualization" tab, for example, with the "Graphic view" and "Switch" screen objects. In the faceplate instance, you can assign graphics from the project's graphics collection or released type versions of the "Graphic" type from the project library. In this way you can assign different graphics to objects in different faceplate instances. |
| Configuration string | The data type "Configuration string" allows for the flexible assignment of values. A configuration string can include names or numbers, for example, that are addressed in scripts and can be transferred. |
| Multilingual text | You can link properties of the "Multilingual text" type with texts. In the faceplate instance, you can assign static texts, resource lists, tags or scripts. When entering static texts, use the key combination <Shift + Enter> to insert a line break. In the Inspector window you create texts for the projected languages under "Properties > Texts".  In this way, you can configure different texts in different faceplate instances. |
| Resource list | You can link properties of the type "Resource list" with the "Resource list" data type. In the faceplate instance you can then assign elements from the graphic and text lists. In this way you can assign different text and graphic elements to objects in different faceplate instances. |
| Unsigned 64-bit integer | You can link properties that correspond to an unsigned 64-bit integer with the data type "Unsigned 64-bit integer". You can then assign corresponding numerical values in the faceplate instance. In this way you can assign different numerical values to objects in different faceplate instances. |

###### Deleting interface properties

To delete an interface property, select the property you wish to delete and click![Deleting interface properties](images/134621778187_DV_resource.Stream@PNG-de-DE.png).

Alternatively, press <Delete>.

---

**See also**

[Creating a faceplate instance](#creating-a-faceplate-instance)

##### Configure interface property (RT Unified)

###### Requirement

- The faceplate type has been created.
- The version is open for editing.
- The "Property interface" tab is open.
- A screen is created in the HMI device.

###### Procedure

1. Click the "Add" field or click the ![Procedure](images/120361298315_DV_resource.Stream@PNG-de-DE.png) button.

   A new interface property is created.
2. Change the values for the name, if required, and select the data type.
3. Switch to the "Visualization" tab.
4. Select the screen object that is to be linked to the interface property.
5. Open the "Properties > Properties" Inspector window.
6. Select the "Property interface" method in the "Dynamization" column.
7. Select the previously created interface property.
8. Release the version of the faceplate type and change to the project tree to interconnect the interfaces in the screen.
9. Open the screen and configure a faceplate container by dragging the faceplate type to the screen.
10. Open the Inspector window of the faceplate container and go to "Properties > Properties > Miscellaneous > Interface".
11. Select the created interface property. In the "Static value" column, assign a fixed value to the property. If you make several entries, separate the individual values with a semicolon.

    You can also assign values of the following categories to the property in the "Dynamization" column:

    - Tag
    - Script
    - Flashing (for colors)
    - Resource list (for text and graphic list elements)

**Note**

The name must satisfy the following conditions:

- Maximum character length: 128 characters
- Unique name
- Beginning with a letter or underscore
- No special characters:

  , ; . : ! ? " ' ^ ´ ` ~ - + = / \ ¦ @ * # $ % & § ° ( ) [ ] { } < >
- No spaces
- No JavaScript elements

**Note**

"Flashing" is not supported in Runtime.

| Symbol | Meaning |
| --- | --- |
| ![Procedure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for an efficient procedure** |
| In the "Static value" column, you can copy and paste values via the shortcut menu of the text box. |  |

---

**See also**

[Creating a faceplate instance](#creating-a-faceplate-instance)

##### Example: Defining "Configuration string" and using it in a script (RT Unified)

You can assign data values to interface properties with the "Configuration string" data type at the faceplate instance or using a script.

###### Requirement

- A faceplate type "Faceplate_1" has been created and opened for editing.
- A screen is created in the HMI device.

> **Note**
>
> Reference faceplate versions with full version numbers, such as: Faceplate_1_V_0_0_3.

###### Example of value assignment at the faceplate instance

1. Open the "Property interface" tab.
2. Create the following interface properties:

   - Label_Names
   - Label_Rotation
3. Assign the data type "Configuration string" to the interface properties.
4. Switch to the "Visualization" tab.
5. Configure three text boxes: "Text box_1", "Text box_2" and "Text box_3"
6. Configure a button with the text "Rotation" and one with the text "Read".
7. In the Inspector window of the "Rotation" button, open the "Events" tab.
8. Create the following script for the "Press" event:

   `export function Button1_OnDown(item, x, y, modifiers, trigger) {`

   `let myProperty = Faceplate.Properties.Label_Rotation;`

   `let angles = myProperty.split(";");`

   `Faceplate.Items("Text box_1").RotationAngle = angles[0];`

   `Faceplate.Items("Text box_2").RotationAngle = angles[1];`

   `Faceplate.Items("Text box_3").RotationAngle = angles[2];`

   `}`
9. In the Inspector window of the "Read" button, open the "Events" tab.
10. Create the following script for the "Press" event:

    `export function Button2_OnDown(item, x, y, modifiers, trigger) {`

    `let myProperty = Faceplate.Properties.Label_Names;`

    `let words = myProperty.split(";");`

    `Faceplate.Items("Text box_1").Text = words[0];`

    `Faceplate.Items("Text box_2").Text = words[1];`

    `Faceplate.Items("Text box_3").Text = words[2];`

    `}`
11. Release the faceplate type.
12. Change to the project tree.
13. Open a screen.
14. Create a faceplate instance by dragging the faceplate type from the project library to the screen.
15. Open the Inspector window of the faceplate instance and navigate to "Properties > Properties > Miscellaneous > Interface".
16. Navigate to the created interface properties and assign them meaningful values, such as:

    - Label_Names: "Label1;Label2;Label3"
    - Label_Rotation: "5;15;45"
17. Compile and load the project.

###### Result

When pressing the "Rotation" button, the text boxes of the faceplate are rotated by the values that were assigned to the interface property.

When pressing the "Read" button, the values assigned to the interface properties are read and the text boxes show the respective text.

###### Example of faceplate pop-up with value assignment via script

1. Open the "Property interface" tab.
2. Create the interface property "Title" and assign the "Configuration string" data type to it.
3. Switch to the "Visualization" tab.
4. Create a text box "Text box_1".
5. Open the Inspector window of the faceplate and switch to the "Events" tab.
6. Create the following script for the "Loaded" event:

   To do so, click on ![Example of faceplate pop-up with value assignment via script](images/160566469643_DV_resource.Stream@PNG-de-DE.png) "Convert function to script".

   `export function Faceplate_Typ_OnLoaded(item) {`

   `let myProperty = Faceplate.Properties.Title;`

   `Faceplate.Items("Text box_1").Text = myProperty;`

   }
7. Enable the faceplate.
8. Change to the project tree.
9. Open a screen.
10. Add a button "Button_1" on the screen.
11. Create a faceplate instance by dragging the faceplate to the screen.
12. Open the Inspector window of the button and switch to the "Events" tab.
13. Create the following script for the "Press left mouse button" event:

    To do so, click on ![Example of faceplate pop-up with value assignment via script](images/160566469643_DV_resource.Stream@PNG-de-DE.png) "Convert function to script".

    `export function Button_1_OnTapped(item, x, y, modifiers, trigger) {`

    `let data = {Title:"Text in Popup"};`

    `let po = UI.OpenFaceplateInPopup("Faceplate_1_V_0_0_1", "Popup", data, UI.ActiveScreen, false);`

    `po.Left = 100;`

    `po.Top = 150;`

    `}`
14. Compile and load the project.

**Note**

**Referencing the faceplate type**

The type is referenced by the name of the type, as shown in the properties, e.g. "Faceplate_1_V_0_0_1".

Include the complete version number. The version number specified in the script is automatically updated when a new version of the type is released.

###### Result

When you press the button in runtime, the faceplate opens as a popup. The title "Text in pop-up" is read from the script and displayed in the text box.

---

**See also**

[Creating a faceplate instance](#creating-a-faceplate-instance)

#### Interface events in faceplates (RT Unified)

This section contains information on the following topics:

- [Configuring an interface event in the faceplate type (RT Unified)](#configuring-an-interface-event-in-the-faceplate-type-rt-unified)
- [Example: Configuring and using an interface event (RT Unified)](#example-configuring-and-using-an-interface-event-rt-unified)

##### Configuring an interface event in the faceplate type (RT Unified)

###### Introduction

You use interface events to define events and associated parameters in the faceplate type. At the instance, you configure functions of the function list and scripts to the created event. This gives you the option of configuring various effects on the instances for an event defined in the faceplate type.

Various data types are available for the parameters associated with an interface event.

###### Requirement

- A screen is created in the HMI device.
- The faceplate type has been created.
- The version is open for editing.
- The "Event interface" tab is open.

###### Data types of parameters

The following data types are available for the parameters of interface events:

| Data types | Description |
| --- | --- |
| Bool | Logical values (True/False) |
| Byte | Unsigned 8-bit value |
| Char | ASCII character |
| Color | Color |
| DateTime | Date/time information |
| DInt | Signed 32-bit value |
| DWord | Unsigned 32-bit value |
| HmiEventTrigger | The enumeration "HmiEventTrigger" can have the following values:  - Unknown (0): Unknown - Touch (1): Triggered by touch HMI device - Left (16): Triggered by left mouse button. - Middle (17): Triggered by middle mouse button. - Right (18): Triggered by right mouse button. - Enter (256): Triggered by <Enter>. - Space (257): Triggered by <Space>. - Escape (258): Triggered by <Esc>. |
| HmiGesture | The enumeration "HmiGesture" can have the following values:  - Unknown (0): unknown - SwipeLeft (1): Swipe left - SwipeRight (2): Swipe right - SwipeUp (3): Swipe up - SwipeDown (4): Swipe down |
| HmiKeyboardModifier | The enumeration "HmiKeyboardModifier" can have the following values:  - None (0): None - Control (1): <Ctrl> - Shift (2): <Shift> - Alt (4): <Alt> |
| Int | Integer |
| LInt | Signed 32-bit value |
| LReal | 64-bit floating-point number IEEE 754 |
| LString | 64-bit character sequence |
| LWord | Unsigned 64-bit value |
| Real | 32-bit floating-point number IEEE 754 |
| SInt | Signed 8-bit value |
| String | 32-bit character sequence |
| Time | Time information |
| UDInt | Unsigned 32-bit value |
| UInt | Unsigned integer |
| ULInt | Unsigned 64-bit value |
| USInt | Unsigned 8-bit value |
| Word | Unsigned 16-bit value |

###### Configuring an interface event

1. On the "<Add>" or select the button ![Configuring an interface event](images/120361298315_DV_resource.Stream@PNG-de-DE.png).

   A new interface event is created.
2. If required, change the values for the name.
3. Select "<Add>" below the interface event.

   A new parameter is created.
4. Change the value for the name.
5. Add more parameters if needed.
6. Switch to the "Visualization" tab.
7. Select the faceplate instance or a screen object with which the interface event is to be linked.
8. Open the "Properties > Events" Inspector window.
9. Select an event.
10. Click on ![Configuring an interface event](images/160566469643_DV_resource.Stream@PNG-de-DE.png) "Convert function to script".

    A script is created.
11. In the script, open the shortcut menu and select "Snippets > Faceplate > Raise a custom faceplate event".

    The following code is inserted:

    `let parameters = {Parameter_1:1, ColorParameter:0xff00ff00};`

    `Faceplate.RaiseEvent("MyCustomEventName", parameters);`
12. Adapt the names of the parameters in the script.
13. For the name of the interface event in the script, select the name that is created in "Event interface".
14. Release the type version of the faceplate.
15. Open the screen of the HMI device.
16. Create a faceplate instance of the released type version in the screen.
17. Select the faceplate instance.
18. Open the Inspector window under "Properties > Events".
19. Select the interface event in the event list.
20. Configure a function of the function list or a script to the event.

**Note**

The name must satisfy the following conditions:

- Maximum character length: 128 characters
- Unique name
- Beginning with a letter or underscore
- No special characters:

  , ; . : ! ? " ' ^ ´ ` ~ - + = / \ ¦ @ * # $ % & § ° ( ) [ ] { } < >
- No spaces
- No JavaScript elements

###### Editing an interface event

> **Note**
>
> **Effects on the faceplate instance when the interface event is changed in the faceplate type**
>
> If you change the interface event, consider the following effects on the faceplate instance:
>
> - If you have configured a script to the interface event and change the names of the parameters, you must manually update the parameters of the interface event used in it.
> - If you have renamed the interface event, the name in the event list is updated automatically.
> - If you have renamed the interface event or associated parameters and configured a script to the interface event, they are automatically updated in the script header.

1. Select the released type version.
2. Open the shortcut menu and select "Edit type".

   A new type version is created and opened for editing.
3. Select the "Event interface" tab.
4. Change the name of the interface event.
5. Change the name of the parameters.
6. Switch to the "Visualization" tab.
7. Select the faceplate instance or screen object linked with the interface event.
8. In the Inspector window, adapt the script under "Properties > Events":

   - Change the names of the parameters to match the changes in the "Event interface" tab.
   - Change the interface event names to match the changes in the "Event interface" tab.
9. Release the type version of the faceplate.

   Enable the "Update instances in project" option.
10. Confirm with "OK".

    The faceplate instance in the screen of the HMI device is updated.
11. If required, configure functions of the function list to the event again.
12. If required, adapt the names of the interface event parameters in the script.

##### Example: Configuring and using an interface event (RT Unified)

With interface events, you define events in the faceplate type which you interconnect to instances with different functions of the function list or scripts.

###### Requirement

- A screen is created in the HMI device.
- A faceplate type "Faceplate_1" has been created and opened for editing.

###### Procedure

1. Switch to the "Event interface" tab of the faceplate type.
2. Click the "<Add>" field or select the ![Procedure](images/120361298315_DV_resource.Stream@PNG-de-DE.png) button.

   A new interface event is created.
3. Change the name of the interface event to "My_Interface_Event".
4. Select "<Add>" below the interface event.

   A new parameter is created.

   The data type of the parameter is "Int".
5. Change the name of the parameter to "Parameter_Int".
6. Select "<Add>" below the interface event.

   A new parameter is created.
7. Change the name of the parameter to "Parameter_Bool".
8. Change the data type of the parameter to "Bool".
9. Switch to the "Visualization" tab of the faceplate type.
10. Add a button.
11. Change the name of the button to "Button_1".
12. Select the "Button" screen object.
13. Open the Inspector window under "Properties > Events".
14. Create the following script for the "Click left mouse button" event:

    `export function Button_1_OnTapped(item, x, y, modifiers, trigger) {`

    `let parameters = {Parameter_Int:90,Parameter_Bool:true };`

    `Faceplate.RaiseEvent("My_Interface_Event", parameters);`

    `}`
15. Release the type version of the faceplate.
16. Create the HMI tags "HMI_Tag_Int" of "Int" data type in the HMI device.
17. Create the HMI tags "HMI_Tag_Bool" of "Bool" data type in the HMI device.
18. Open the screen of the HMI device.
19. Create a faceplate instance of the released type version in the screen.
20. Select the faceplate instance.
21. Open the Inspector window under "Properties > Events" and select the event "My_Interface_Event".
22. Click on ![Procedure](images/160566469643_DV_resource.Stream@PNG-de-DE.png) "Convert function to script".
23. Create the following script:

    `export function Faceplate_container_1_OnMy_Interface_Event(item, Parameter_Int, Parameter_Bool) {`

    `let tag1 = Tags("HMI_Tag_Int");`

    `let tag2 = Tags("HMI_Tag_Bool");`

    `tag1.Write(Parameter_Int);`

    `tag2.Write(Parameter_Bool)`

    `}`
24. Configure 2 I/O fields in the screen:

    - "IO field_Int": Link the "Process value" property of the I/O field with the tag "HMI_Tag_Int".
    - "IO field_Bool": Link the "Process value" property of the I/O field with the tag "HMI_Tag_Bool".
25. Compile and load the project.

###### Result

The values of the IO fields change as follows when the "Button_1" button is pressed in Runtime:

- "IO field_Int": 90
- "IO field_Bool": 1

#### Checking the version consistency and fixing inconsistencies (RT Unified)

##### Introduction

To ensure the consistency of a version of a faceplate type, you have two options:

- You can run a consistency check yourself before releasing a faceplate version.
- An automatic consistency check is performed when the version is released.

In both variants, the created version is checked for missing or faulty references to screens or tags, for example. A message is displayed in case of an error.

##### Requirement

- A faceplate version has been created but has not been released yet.
- Objects have been configured.

##### Checking the consistency yourself

1. Select the version whose consistency you want to check.
2. Select "Check consistency" from the shortcut menu.

   The result of the consistency check is displayed in the Inspector window in the "Info > General" tab.

##### Remedying the inconsistency

To remedy any inconsistency, follow these steps:

1. Open the Inspector window under "Information > General".   
   An error and an error description are displayed in the Inspector window.
2. Click the green arrow![Remedying the inconsistency](images/122844867979_DV_resource.Stream@PNG-de-DE.png) in the "Go to" column.   
   You are navigated automatically to the error location.
3. Eliminate the error.
4. If necessary, perform another consistency check to check whether all errors have been resolved.

You have fixed all consistency errors. The consistency check of the version of the faceplate type shows no errors.

---

**See also**

[Consistency status of types (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#consistency-status-of-types-rt-unified)

#### Checking the consistency at the faceplate type and fixing inconsistencies (RT Unified)

##### Introduction

When editing versions of the faceplate types, incorrect referencing may unintentionally occur with the faceplate type and outdated instances if the default version of the dependent type is not used in the default version or a version other than the default version is instantiated in the device.  
  
As soon as you release a version, a consistency check is automatically performed.

The "Status" column shows whether an inconsistency exists when referencing the faceplate type.

![Introduction](images/161087774347_DV_resource.Stream@PNG-en-US.png)

**Resolving inconsistency through referencing of the non-default version of another faceplate type**

**Requirement**

- A faceplate type has been created and released.
- The "Libraries" task card is open.
- The "Status" column in the project library displays the symbol![Introduction](images/140613459339_DV_resource.Stream@PNG-de-DE.png).

**Procedure**

To correct an inconsistency which occurs through the referencing of a non-default version, follow these steps:

1. Open the shortcut menu of the inconsistent type.
2. Select the "Fix inconsistencies" menu item.
3. Select one of the following options:

   - "Adapt inconsistent type"  
     A new version of the faceplate type is created and has the status "In progress".   
     In the new version, the default version of the referenced faceplate type is automatically used.
   - "Set the currently referenced version as "default""  
     The currently referenced version of the faceplate type is automatically set as the "default".

**Remove inconsistency in the device through instantiating the non-default version**

**Requirement**

- A faceplate type has been created and released.
- The "Libraries" task card is open.
- The "Status" column in the project library displays the symbol![Introduction](images/143118763787_DV_resource.Stream@PNG-de-DE.png).

**Procedure**

To eliminate an inconsistency which occurs through the instantiation of a non-default version in the device, update the faceplate type (see section [Updating a faceplate type](#updating-a-faceplate-type-rt-unified))

#### Releasing a faceplate version of a type (RT Unified)

When you are finished editing a type version, release the version for productive use. Assign a version number for the release. You can also use multiple selection to release several versions at the same time.

If you have made structural changes to the type version to be released, such as changes at the interfaces, only the types that reference the changed type version and are affected by the change are set to the "In progress" status. To set all referencing types to the "In progress" status by default when they are released, select the check box "Set all dependent types to the 'In test' status" in the settings under "General > Library settings" in the "Release type" area.

##### Introduction

Only released versions of a faceplate type can be instantiated in a screen.

##### Requirement

- The "Libraries" task card is open or you are in the library view.
- The faceplate version that you want to release has the "In progress" status.
- The faceplate version is consistent.

##### Procedure

To release type versions, follow these steps:

1. Select the faceplate version you want to release.
2. Select the "Release version" command from the shortcut menu.

   The "Release type version" dialog box opens.
3. If necessary, change the properties of the version:

   - Enter a name for the faceplate type in the "Type name" field. If you have selected several versions for release, the "Name" field cannot be changed.
   - In the "Version" field, define a main and an intermediate version number for the version to be released. If you have selected several versions for release, the "Version" field cannot be changed and the last version number is used for the release.
   - In the "Author" field, enter the editor of the version to be released.
   - In the "Comment" field, enter a comment on the version to be released.
4. If necessary, change additional options of the faceplate version:

   - "Update instances in the project" option: Select the check box to update all instances in the project to the most recent version.
   - Option "Delete unused type versions without "Default" label from the library": Select the check box to delete all faceplate versions from the library that are not connected to any instance in the project. Versions with dependencies on other types are not deleted.
   - "Set dependent types to edit mode" option: If you have made incompatible changes to the type version to be released, such as changes at the interfaces, this check box is selected by default. Faceplate types that reference the changed type version are set to the "In progress" status by default. Clear the check box if you do not want to set the referencing types to the "In progress" status.

     If you have only made compatible changes to the type version to be released, this check box is cleared by default.
5. Confirm with "OK".

##### Result

- The selected faceplate version has been released.
- The properties are applied for the faceplate type itself, the version to be released, and for all future versions. Versions already released remain unaffected by the changes.
- The released faceplate version is given the "Default" identifier.
- If needed, all instances with the same original version are updated to the most recent version and the unused versions of the type are deleted.
- Depending on the changes you have made, releasing the type version has effects on types that reference this version:

  - If you have made incompatible changes to the type version to be released, such as changes at the interfaces, the types that directly reference the changed type version are set to the "In progress" state. The calling types still reference the last released version.
  - If you have only made compatible changes to the type version to be released, the types that directly reference the changed type version are not changed. The calling types reference the newly released version in this case.
- The icon in the "Status" column shows whether the references of the type are consistent with other types.

---

**See also**

[Consistency status of types (RT Unified)](WinCC%20Unified%20%28RT%20Unified%29.md#consistency-status-of-types-rt-unified)
  
[Checking the version consistency and fixing inconsistencies (RT Unified)](#checking-the-version-consistency-and-fixing-inconsistencies-rt-unified)

#### Creating a faceplate instance

##### Introduction

The faceplate type is stored in the project library. When you use the faceplate type in a screen, you create an instance of the faceplate type.

> **Note**
>
> Note that a faceplate is always configured for a particular class of HMI devices. For example, you cannot use a faceplate type that is configured for Runtime Advanced in a screen of a Unified HMI device.

> **Note**
>
> The number of faceplate instances in a screen is not limited. Note that the performance when opening or updating a screen is affected by the number of faceplate instances or the use of scripts in the faceplate instances.

##### Requirement

- A screen is open.
- The "Libraries" task card is open and the project library has been expanded.
- A faceplate type has been configured.
- The faceplate version you want to instantiate has been released.

##### Procedure using the project library

1. Drag the faceplate type or the desired version from the project library to the screen.

   The faceplate container with the faceplate instance is added to the screen.

   The version marked with "Default" is always used when you drag the faceplate type to the screen.
2. Open the Inspector window under "Properties > Properties > Miscellaneous > Interface".
3. Connect the faceplate tags to project tags.
4. Specify the values of the interface properties.
5. Open the Inspector window under "Properties > Events".
6. Specify functions of the function list or scripts of the interface events.
7. Open the Inspector window under "Properties > Properties > Format > Fit to size".
8. To adjust the size of the faceplate or the container window, choose between "Fit window to screen" and "Fit screen to window".

**Note**

If you do not select resize, screen objects or navigation elements may not be displayed or may not be displayed completely.

##### Procedure using the "Faceplate container" control

1. Open the "Toolbox > Controls" task card.
2. Drag the "Faceplate container" control to the screen.

   An instance of the "Faceplate container" control is configured. No faceplate type is linked.
3. Open the Inspector window of the faceplate container under "Properties > Properties > Miscellaneous".
4. Select the desired faceplate type under "Faceplate type" in the "Static value" column.
5. Open the Inspector window under "Properties > Properties > Miscellaneous > Interface".
6. Connect the faceplate tags to project tags.
7. Specify the values of the interface properties.
8. Open the Inspector window under "Properties > Events".
9. Specify functions of the function list or scripts of the interface events.
10. Open the Inspector window under "Properties > Properties > Format > Fit to size".
11. To adjust the size of the faceplate or the container window, choose between "Fit window to screen" and "Fit screen to window".

**Note**

If you do not select resize, screen objects or navigation elements may not be displayed or may not be displayed completely.

| Symbol | Meaning |
| --- | --- |
| ![Procedure using the "Faceplate container" control](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for an efficient procedure** |
| In the "Static value" column, you can copy and paste values via the shortcut menu of the text box. |  |

##### Change the faceplate version in the container

You change the link to a faceplate version in the properties of the faceplate container under "Miscellaneous > Faceplate type". The selection window lists the released faceplate versions of all faceplates.

| Symbol | Meaning |
| --- | --- |
| ![Change the faceplate version in the container](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for an efficient procedure** |
| - Under "Cross-references", you get a quick overview of all used objects within a faceplate container and the use of faceplate versions in screens. - You open the cross-references either in the Inspector window of the container under "Info > Cross-references" or via the shortcut menu of the respective object. - In the shortcut menu of the faceplate container, you can use the "Go to library version" function to jump directly to the referenced faceplate type in the project library. |  |

##### Result

- The faceplate type is instantiated in a faceplate container.
- The objects configured in the faceplate type are visible in the faceplate container.
- Interface tags and interface properties have been defined for the faceplate container.
- Functions of the function list and scripts are defined for the interface events of the faceplate container.
- If required, the properties of the faceplate container can be configured and dynamized in the inspector window.

#### Using a PLC user data type (RT Unified)

##### Introduction

You can configure data blocks based on a PLC user data type (UDT). You can use tags that are based on this PLC user data type in faceplate instances.

The following advantages arise from reusing the PLC user data type:

- You minimize the configuration effort.
- You reduce the consumption of resources.
- They ensure unique and consistent naming of tags in data blocks and faceplate types and hereby significantly reduce the probability of configuration errors.

> **Note**
>
> Do not use more than one version of a PLC user data type in a faceplate type.

The following complex PLC data types are supported:

- User data types that are based on other user data types.
- User data types that use arrays comprising simple elements or user data types.

  > **Note**
  >
  > Arrays whose limits are defined permanently with integer values or variably with user constants are supported.
- User data types that are based on a different user data type that, in turn, use arrays comprising simple elements or user data types.
- User data types that consist of further structured data types, e.g. CREF, PLCUDT, HMIUDT, NREF, IEC-specific parameters, and arrays comprising structured data types.

  > **Note**
  >
  > Nesting is limited to 8 levels for structured user data types.
  >
  > Depending on the size and nesting of the PLC user data types, the performance when assigning the PLC user data type and when opening the affected faceplate type may be impaired.

##### Requirement

- A SIMATIC S7-1200 or SIMATIC S7-1500 controller is configured.
- An HMI device has been configured.
- At least one PLC user data type has been configured.
- At least one PLC tag based on the PLC user data type has been configured.
- A faceplate type has been configured and opened for editing.
- A screen has been created.

##### Importing a device proxy into a project

If you import a device proxy into a project, the PLC user data types are not imported.

1. Create a user data type based on the PLC user data type in the project library of the source project.
2. Copy the user data type into the global library.
3. Apply the user data type to the project library of the project in which the HMI device is located.
4. Link the user data types with faceplate types as usual.

##### Procedure

1. Create a user data type that is based on the PLC user data type:

   - Drag-and-drop the PLC user data type from the device overview to the "Types" folder of the project library.
2. Create a PLC tag that is based on the PLC user data type:

   - Create a tag in the "PLC tags" editor.
   - Select a PLC user data type as the data type.
3. Connect an HMI tag to a PLC tag:

   - Create a tag in the "HMI tags" editor.
   - Under "Connection", select the external connection to the PLC.
   - Link the PLC tag that is based on a PLC user data type.
4. Create an interface tag in the faceplate type:

   - Go to the "Faceplate types" editor and open the "Tag interface" tab.
   - Create an interface tag.
   - Define the "PLCUDT" data type.
   - Under "User data type structure", select the PLC user data type.

   Alternatively, you drag-and-drop a version of the PLC user data type from the project library onto the "<Add>" field in the "Tag interface" tab.

   An interface tag with the data type "PLCUDT" is generated and linked with the version of the PLC user data type.
5. Release the faceplate type.
6. Create a faceplate instance:

   - Open the previously created screen and create an instance of the faceplate type.
   - Open the Inspector window of the faceplate instance.
   - Under "Properties > Properties > Miscellaneous > Interfaces", assign the HMI tags based on the PLC tags to the specific properties in the "Static value" column.

> **Note**
>
> Note that the version is not updated automatically in the faceplate type when you change the version of the referenced PLC user data type. Therefore, inconsistencies may occur if the linked version is not the default version. To clean up the inconsistency, you have the following options:
>
> - In the shortcut menu of the inconsistent type, select the "Clean up inconsistencies" menu item. The type does not have to be released for this purpose.
> - Open the faceplate version for editing and update the version of the linked PLC user data type manually in the task card "Tags interfaces" and enable the faceplate type.

When a PLC user data type is set to the "In test" state, the faceplate type referencing this PLC user data type is set to the "In progress" state. After release of the PLC user data type in the library, you may experience consistency problems in the faceplate type. In this case, update the PLC user data type reference in the tag interface to the current version.

##### Result

You are using tags that are based on a PLC user data type in a faceplate instance.

#### Using an HMI user data type (RT Unified)

##### Introduction

You have the possibility to use HMI user data types in faceplates.

The use of HMI user data types provides the following advantages:

- You minimize the configuration effort.
- You reduce the consumption of resources.
- You ensure the unique and consistent naming of tags and thus significantly reduce the probability of configuring errors.

##### Requirement

- An HMI device has been configured.
- At least one HMI user data type has been configured.
- A faceplate type has been configured and opened for editing.
- A screen has been created.

##### Procedure

1. Create an interface tag in the faceplate type:

   - Go to the "Faceplate types" editor and open the "Tag interface" tab.
   - Create an interface tag.
   - Define the "HMIUDT" data type.
   - Under "User data type structure", select the HMI user data type.

   Alternatively, you drag-and-drop a version of an HMI user data type from the project library onto the "<Add>" field in the "Tag interface" tag. An interface tag with the data type "HMIUDT" is generated and linked with the version of the HMI user data type.
2. Create an object:

   - Drag an object, e.g. an I/O field, from the "Toolbox" task card to the "Visualization" tab.
   - Under "Properties > Properties > General > Process value", select "Tag" in the Dynamization field and assign an element to the interface tag.
   - Release the faceplate type.
3. Create a faceplate instance:

   - Open the previously created screen and create an instance of the faceplate type.
   - Open the Inspector window of the faceplate instance.
   - Assign the appropriate HMI tag under "Properties > Properties > Miscellaneous > Interfaces".

##### Result

You are using tags that are based on an HMI user data type in a faceplate instance.

#### Using a faceplate type in another faceplate type (RT Unified)

##### Introduction

You can use a faceplate type in another faceplate type. In this way you assemble multiple faceplate types and increase the reusability of the faceplates.

The faceplate type used in another faceplate type is called an inner faceplate type. The faceplate type in which another faceplate type is used is called the outer faceplate type.

You can link the interface tags and interface properties configured in the inner faceplate type with interface tags and interface properties of the outer faceplate type. Local tags of the inner faceplate type cannot be linked to tags of the outer faceplate type.

##### Requirement

- A screen is created in the HMI device.

##### Procedure

> **Note**
>
> **Reference to the same faceplate type is not supported**
>
> No other version of the same faceplate type can be used in a faceplate type.

1. Create a faceplate type in the library, e.g. "Faceplate_1".
2. Configure interface tags and interface properties in the faceplate type, e.g. "Interface_Tag_Faceplate_1" and "Interface_Property_Faceplate_1".
3. Configure screen objects in the "Visualization" tab.
4. Link the screen objects with interface tags and interface properties.
5. Release the faceplate type.
6. Create another faceplate type, for example, "Faceplate_2".
7. Configure interface tags and interface properties in the faceplate type, e.g. "Interface_Tag_Faceplate_2" and "Interface_Property_Faceplate_2".
8. Switch to the "Visualization" tab of the outer faceplate type, e.g. "Faceplate_2".
9. Drag and drop the inner faceplate type, e.g. "Faceplate_1", from the library into the "Visualization" tab.

   Alternatively, you can configure the "Faceplate container" control and link the "Faceplate type" property to the inner faceplate type.
10. Select the inner faceplate type.
11. Open the Inspector window under "Properties > Properties > Miscellaneous > Interface".
12. Link the interface tags and interface properties of the inner faceplate type or the faceplate container to the interface tags and interface properties of the outer faceplate type.

    If you use interface tags of the "PLCUDT" or "HMIUDT" data type, only compatible interface tags are displayed in the selection window.
13. Release the outer faceplate type.
14. Open the screen of the HMI device.
15. Drag and drop the outer faceplate into the screen.
16. Connect the faceplate tags to project tags.
17. Specify the values of the interface properties.
18. Open the Inspector window under "Properties > Events".
19. Specify system functions of the function list or scripts of the interface events.

**Note**

**Smallest required device version**

The smallest required device version of the outer faceplate type must be equal to or larger than that of the inner faceplate type.

#### Copying faceplate types and faceplate instances to other projects (RT Unified)

##### Introduction

Faceplate types can be transferred to other projects.

##### Requirements

- The target project contains the devices on which faceplates can be used.
- Faceplate types: If PLC user data types are used in the faceplate type, the same PLC user data types must be available in the target project.
- Faceplate instances: It must also be possible to integrate the tags of the used faceplate types into the target project.
- Both projects (source and target) are open in different instances of TIA Portal.

> **Note**
>
> **Dependencies**
>
> Hierarchical dependencies exist between user data types, faceplate type and faceplate instances:
>
> Therefore, note the order:
>
>
>
> 1. Faceplate instances use faceplate types.
> 2. Faceplate types use user data types where necessary.
>
> 1. Configure PLC user data types.
> 2. Copy the faceplate type.
> 3. Copy the faceplate instances.

##### Configuring PLC user data types

1. Switch to the project from which you want to copy the faceplate type.
2. Check the faceplate type to be copied for any used PLC user data types.
3. Go to the target project.
4. In the target project, configure the PLC user data types required in the faceplate type that is to be copied.

##### Copying a faceplate type

1. Switch to the project from which you want to copy the faceplate type.
2. Select the desired faceplate type.
3. Copy the desired faceplate type.
4. Go to the target project.
5. Select the "Types" folder in the project library.
6. Insert the faceplate type into the target project.
7. Integrate the required PLC user data types into the new faceplate type.

##### Copying via "Global libraries"

Alternatively, you can make the faceplate type available for other projects by copying it to a global library.

To copy a faceplate type to another project via a global library, follow these steps:

1. Switch to the project from which you want to copy the faceplate type.
2. Copy the faceplate type.
3. Open the "Global libraries" pane and paste the copied faceplate type there.
4. Go to the target project.
5. Open the "Global libraries" pane.
6. Copy the previously pasted faceplate type from the global library to the project library.
7. Integrate the required PLC user data types into the new faceplate type.

**Note**

**Name redundancy**

In case of a name redundancy, the name of the copied faceplate type is given a version number in the form "-[number]", e.g. "Faceplate_1".

##### Copying a faceplate instance

1. Switch to the project from which you want to copy the faceplate instance.
2. Select the desired faceplate instance.
3. Copy the desired faceplate instance.
4. Go to the target project.
5. Open the screen in which the faceplate instance is to be inserted.
6. Paste the faceplate container.

   The faceplate type is created in the project.
7. Link the required tags in the faceplate container with those in the project.

---

**See also**

[Basics of faceplates (RT Unified)](#basics-of-faceplates-rt-unified)

### Connecting faceplate types to OPC UA (RT Unified)

OPC UA is a standardized manufacturer-independent software interface for data exchange in automation engineering.

You can use data values from an OPC UA connection in faceplate types.

#### Requirement

- A OPC UA connection is configured.

#### Procedure

To use data values from an OPC UA connection, you must assign the data types to the corresponding Unified data types. You can find the assignment of OPC UA and Unified data types in the table below:

| OPC UA data type | Unified Faceplates data type |
| --- | --- |
| Int32 | DInt |
| Boolean | Bool |
| Byte | USInt |
| DateTime | DateTime |
| Double | LReal |
| Float | Real |
| Int16 | Int |
| SByte | SInt |
| String | WString* |
| UInt16 | UInt |
| UInt32 | UDInt32 |
| *Only possible as a local tag, data type for interface tags not available. |  |

Data types that are not listed in the table are not supported by Unified Faceplates.

For more information on OPC UA, refer to the Runtime - Open Platform Communications (OPC) documentation.

### Dynamizing faceplates (RT Unified)

This section contains information on the following topics:

- [Basics for the dynamization of faceplates (RT Unified)](#basics-for-the-dynamization-of-faceplates-rt-unified)
- [Dynamizing a faceplate type (RT Unified)](#dynamizing-a-faceplate-type-rt-unified)
- [Dynamizing a faceplate instance (RT Unified)](#dynamizing-a-faceplate-instance-rt-unified)
- [Dynamizing an object property using a tag parameter (RT Unified)](#dynamizing-an-object-property-using-a-tag-parameter-rt-unified)
- [Accessing properties of the faceplate container with a script (RT Unified)](#accessing-properties-of-the-faceplate-container-with-a-script-rt-unified)
- [Configure faceplate as pop-up (RT Unified)](#configure-faceplate-as-pop-up-rt-unified)

#### Basics for the dynamization of faceplates (RT Unified)

##### General

Both the properties of the faceplate type and the properties of the objects used in the "Visualization" tab are dynamized in the Inspector window under "Properties > Properties".

You link functions of the function list and scripts to the faceplate type or objects of the faceplate type in the "Visualization" tab in the Inspector window under "Properties > Events".

##### Use

You can dynamize events and properties of faceplates at two levels.

1. Dynamizing a faceplate type
2. Dynamizing a faceplate instance

##### Dynamizing a faceplate type

> **Note**
>
> **Using tags**
>
> Only use tags that are defined within the faceplate type.

You can dynamize properties of objects or events in the faceplate type on the "Visualization" tab of the "Faceplate types" editor. You configure the individual objects as in the "Screens" editor.

- To dynamize properties, the following methods are available in the editor:

  - Tag
  - Script
  - Flashing (for colors)

    > **Note**
    >
    > "Flashing" is not supported in Runtime.
  - Property interface

    With this method, you use the interface properties configured in the "Property interface" tab.

  Depending on the property, only certain methods are available.
- You dynamize events by using functions of the function list or scripts.

  Faceplates support various methods. For more information on supported methods, see the [FaceplateType](WinCC%20Unified%20object%20model%20%28RT%20Unified%29.md#faceplatetype-rt-unified) section.
- You do not have access to the tags and scripts of the project within the faceplate type.

  You must therefore configure interface tags in the faceplate type that you link with the tags of the project in the faceplate instance.
- Each faceplate instance created with the faceplate version has the same objects with identical dynamization.

  You can edit this dynamization exclusively in the "Faceplate types" editor.

##### Dynamizing a faceplate instance

You configure the events or dynamic properties individually on the faceplate container. This dynamization refers exclusively to the faceplate container.

Properties of the objects used in the faceplate type cannot be dynamized directly. For this purpose, interface tags, interface properties or interface events must be defined in the faceplate type, via which a dynamization is triggered.

---

**See also**

[Basics of dynamizing screens (RT Unified)](#basics-of-dynamizing-screens-rt-unified)

#### Dynamizing a faceplate type (RT Unified)

##### Introduction

You dynamize screen objects in the faceplate type in the Inspector window editor.

To trigger the reaction to events in the faceplate instance, you can, for example, use the interface tags that were created beforehand in the faceplate type.

You can connect the dynamic properties of the faceplate container with a tag or a script that provides the property with values in Runtime.

Creating scripts in the faceplate type works the same way as creating scripts on objects in screens.

##### Support of system functions

The use of system functions within faceplates is not fully supported. The following system functions are available in the function list and in scripts:

| Function list |  | Script |
| --- | --- | --- |
| **Alarm system** |  |  |
|  | CreateOperatorInputInformation | HMIRuntime.Alarming.SysFct.CreateOperatorInputInformation |
| CreateSystemInformation | HMIRuntime.Alarming.SysFct.CreateSystemInformation |  |
| CreateSystemAlarm | HMIRuntime.Alarming.SysFct.CreateSystemAlarm |  |
| **Resource** |  |  |
|  | LookUpText | HMIRuntime.Resources.SysFct.LookUpText |
| **Tag** |  |  |
|  | UpdateTag | HMIRuntime.Tags.SysFct.UpdateTag |
| IncreaseTag | HMIRuntime.Tags.SysFct.IncreaseTag |  |
| InvertBitInTag | HMIRuntime.Tags.SysFct.InvertBitInTag |  |
| ResetBitInTag | HMIRuntime.Tags.SysFct.ResetBitInTag |  |
| ShiftAndMask | HMIRuntime.Tags.SysFct.ShiftAndMask |  |
| SetBitInTag | HMIRuntime.Tags.SysFct.SetBitInTag |  |
| SetTagValue | HMIRuntime.Tags.SysFct.SetTagValue |  |
| DecreaseTag | HMIRuntime.Tags.SysFct.DecreaseTag |  |

The available system functions can be displayed grouped by areas or sorted alphabetically.

You can find more information at [System functions](Using%20system%20functions%20%28RT%20Unified%29.md#system-functions-rt-unified).

##### Requirement

A faceplate type has been created.

##### Dynamizing events

> **Note**
>
> **Using tags**
>
> Use tags that have been defined within the faceplate type under "Tag interface" or "Local tags".
>
> You link the tags defined in the faceplate type with the project tags in the faceplate instance.

1. Select the faceplate type or an object in the faceplate type.
2. Open the Inspector window under "Properties > Events".
3. Select an event.
4. Select a function from the function list or create a script.

**Note**

**"Cleared" event**

The "Cleared" event is triggered when the faceplate is already resolved. Therefore, access to interface tags and local tags of the faceplate type is not possible.

> **Note**
>
> **Global definition in the faceplate type**
>
> All definitions in the "Global definition" area of the "Scripts" editor in the faceplate type are used in all instances of the faceplate type. When you define a tag in the "Global definition" area, for example, any value changes of this tag can be seen in all instances of the faceplate type.

| Symbol | Meaning |
| --- | --- |
| ![Dynamizing events](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | **Tip for working efficiently** |
| You are supported by snippets when creating scripts; you access these snippets from the shortcut menu under "Snippets > Faceplates". |  |

##### Dynamizing object properties

1. Select the relevant object.
2. Open the Inspector window of the object and select "Properties".
3. In the "Dynamization" column of the Inspector window, select the menu of the property that you want to dynamize.
4. Select the method:

   - Tag
   - Script
   - Expression
   - Property interface
   - Flashing (for colors)

**Note**

The availability of methods is dependent on the selected property.

"Flashing" is not supported in Runtime.

---

**See also**

[Introduction to runtime scripting (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#introduction-to-runtime-scripting-rt-unified)
  
[System functions (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#system-functions-rt-unified)

#### Dynamizing a faceplate instance (RT Unified)

##### Introduction

You dynamize properties of the faceplate instance in exactly the same way as you dynamize properties of another object in the "Screens" editor.

In the "Screens" editor, you can connect the dynamic properties of the faceplate container with a tag or a script that provides the property with values in Runtime.

You have previously created the tags and scripts in the project.

In the Inspector window under "Properties > Events" you will find the interface events defined in the faceplate type.

##### Requirement

A faceplate container with a faceplate instance is inserted in the screen.

> **Note**
>
> **Requirement for triggering the "Enabled" event in Runtime**
>
> To trigger the "Enabled" event at the faceplate container, you must enable the options "Display frame" and "Show heading" in the properties of the control under "Window settings".

##### Dynamizing events

1. Select the faceplate container.
2. Open the Inspector window under "Properties > Events".
3. Select an event.
4. Select a function from the function list or create a script.

| Symbol | Meaning |
| --- | --- |
| ![Dynamizing events](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | **Tip for working efficiently** |
| You are supported by snippets when creating scripts; you access these snippets from the shortcut menu under "Snippets > Faceplates". |  |

##### Dynamizing object properties

1. Select the faceplate instance.
2. Open "Properties" > "Properties" in the Inspector window of the faceplate instance.
3. In the "Dynamization" column, select the menu of the property you want to dynamize.
4. Select the required method:

   - Tag
   - Script
   - Expression
   - Resource list (for strings)
   - Tag parameter (for interfaces)
   - Flashing (for colors)

   Depending on the property, only certain methods are available.

**Note**

"Flashing" is not supported in Runtime.

---

**See also**

[Basics for the dynamization of faceplates (RT Unified)](#basics-for-the-dynamization-of-faceplates-rt-unified)
  
[Basics of dynamizing screens (RT Unified)](#basics-of-dynamizing-screens-rt-unified)

#### Dynamizing an object property using a tag parameter (RT Unified)

##### Introduction

The dynamization of object properties using tag parameters is only possible for interfaces of faceplate instances.

You define a tag name consisting of static and dynamic parts as the tag parameter. The dynamic parts are tag references that are replaced in runtime with the current tag values. The resulting tag name is thus dependent on the values of the tag references.

> **Note**
>
> Tags with numeric data types or data type "WString" are supported as tag references.
>
> You can use multiple tag references in a dynamic tag name.

Example:  
You want to access different HMI tags, e.g. "Engine1" to "Engine10", of a "UDT_1" user data type via a faceplate instance. To do this, you define another "RefTag" tag as a dynamic part of an "Engine'RefTag'.UDT_Tag1" interface property. Depending on the value of the "RefTag" tag in Runtime, the resulting name of the HMI tag "Engine1" to "Engine10" associated with the faceplate instance changes.

##### Requirement

- A faceplate type with a tag interface has been configured and released.
- A faceplate instance of the faceplate type has been configured in a screen.
- At least one HMI tag with numeric data type or data type "WString" has been configured for use as reference.
- HMI tags (tags, arrays, structures) to be accessed by the dynamization have been configured.

  The tags or elements of arrays and structures to be accessed must correspond to the data type of the tag interface.

##### Dynamizing an interface with a tag parameter

To select an interface for the dynamization with a tag parameter, follow these steps:

1. Select the faceplate instance in the screen.
2. Select an interface tag in the Inspector window under "Properties > Miscellaneous > Interface".
3. Select "Tag parameter" for the dynamization.

   The "Tag parameter" editor window opens in the Inspector window.
4. Select a tag as the static part of the dynamic tag name.
5. Delete the single quotation marks at the beginning and end of the tag name.

   > **Note**
   >
   > As long as no dynamic part has been defined, the background color of the input field is yellow.

   ![Dynamizing an interface with a tag parameter](images/171120622603_DV_resource.Stream@PNG-en-US.png)
6. Select one or more tags as tag reference (dynamic part).

   > **Note**
   >
   > You can insert the tag reference by placing the cursor at the desired place and opening the tag selection dialog with <Ctrl+J>.
   >
   > Alternatively, you can enter the tag reference manually. Note that no check is performed to verify that the tag actually exists.

   ![Dynamizing an interface with a tag parameter](images/171120627211_DV_resource.Stream@PNG-en-US.png)

##### Result

The tag name is assigned to the interface of the faceplate instance using the tag references.

#### Accessing properties of the faceplate container with a script (RT Unified)

##### Procedure

To read or write faceplate container properties from a faceplate type, use the `Parent` property of the `Faceplate` object in a script.

You can access the following properties of the faceplate container, for example:

- Position
- Height and width
- Visibility
- Interface tags
- Interface properties

##### Example: Reading the position of the faceplate container

HMIRuntime.Trace(Faceplate.Parent.Top);

HMIRuntime.Trace(Faceplate.Parent.Left);

Read out the alarm with the RTIL Trace Viewer.

##### Example: Changing the position of the faceplate container via a button

export function Button_1_OnTapped(item, x, y, modifiers, trigger) {

// Read Faceplate container coordinates

   let containerTop = Faceplate.Parent.Top;

   let containerLeft = Faceplate.Parent.Left;

// Write Faceplate container coordinates. Increment with 100 pixels

   Faceplate.Parent.Top = containerTop + 100;

   Faceplate.Parent.Left = containerLeft + 100;

}

##### Example: Read connected tags

let TagNameSystem;

TagNameSystem = Faceplate.Parent.Properties.TagProperty_1.Tag;

HMIRuntime.Trace("System Tag Name: " + TagNameSystem);

Read out the alarm with the RTIL Trace Viewer.

---

**See also**

[Tracing with the RTIL Trace Viewer (RT Unified)](Runtime%20scripting%20%28RT%20Unified%29.md#tracing-with-the-rtil-trace-viewer-rt-unified)

#### Configure faceplate as pop-up (RT Unified)

##### Introduction

A faceplate can be opened in Runtime as pop-up window by means of a script.

> **Note**
>
> **Only faceplate versions used in the HMI device are available in Runtime.**
>
> - Use the faceplate version in the HMI device as faceplate container or in a script as reference.
>
>   The reference is not resolved if you dynamically generate the name of the faceplate version to be opened as a popup with a script.
> - If there is no faceplate version with the name, an empty container is opened.

You have the option of calling a pop-up window either inside or outside a faceplate type:

- Outside a faceplate type: You transfer all interface tags and interface properties in the script.
- Inside a faceplate type: The interface tags and interface properties of the pop-up are applied from the faceplate type in which the pop-up window is triggered.

| Symbol | Meaning |
| --- | --- |
| ![Introduction](images/101804624523_DV_resource.Stream@PNG-de-DE.png) | **Tip for working effectively** |
| The "OpenFaceplateInPopup" and "Close" methods are available as a snippet. The available snippets are displayed in the shortcut menu of the "Scripts" editor. |  |

##### Requirement

- A screen is open.

##### Open and close pop-up windows outside a faceplate type

To configure a faceplate as a pop-up window, for example, to an event of a screen object, follow these steps:

1. Create a faceplate type.
2. Create faceplate tags, for example, "Interface_Tag_1".
3. Create interface properties, for example, "Color_Property_1" (color data type) and "ResourceList_Property_1" (resource list data type).
4. Configure the visualization of the faceplate.
5. Interconnect the tags and properties.
6. Release the version of the faceplate type.
7. Open the screen of the HMI device.
8. Configure the screen object that is to trigger the event, for example, a button.
9. Open the Inspector window under "Properties > Events".
10. Select an event.
11. Click on ![Open and close pop-up windows outside a faceplate type](images/160566469643_DV_resource.Stream@PNG-de-DE.png) "Convert function to script".

    A function is generated.
12. Assign tags and interface properties to the faceplate interface. In the example, the "data" parameter is used.

    To specify text lists, use the prefix "@Default", for example, "@Default.Text_list_1".
13. Create a global definition for the faceplate pop-up.

    Example:

    `//JEx: "Faceplate in Popup"`

    `var po;`
14. Use the "OpenFaceplateInPopup" method.

    - Define the type of the pop-up window with the full version number, for example "Faceplate_1_V_0_0_1".
    - Define the title of the pop-up window, for example, "Popup".
    - Specify the parameter of the interface, for example, "data".
    - Optional: The pop-up window is closed automatically when the specified screen is exited.

      Default: 0. The pop-up window remains open until it is closed manually or Runtime is terminated.

      In the example, the pop-up window is closed as soon as the active screen is exited.
    - Optional: Specify whether the pop-up window is hidden.

      Default: false. The pop-up window is visible.
15. If required, specify where the pop-up window is opened.
16. Configure a "Close pop-up" button.
17. Open the Inspector window of the button under "Properties > Events".
18. Select an event.
19. Click on ![Open and close pop-up windows outside a faceplate type](images/160566469643_DV_resource.Stream@PNG-de-DE.png) "Convert function to script".

    A function is generated.
20. Use the "Close" method.

**Note**

**Interface property of the "Multilingual text" data type**

Interface properties of the "Multilingual text" data type cannot be passed to a faceplate that is called as a popup window outside of a faceplate type.

**Note**

Graphic lists are not supported.

**Note**

When referencing faceplate types, you must replace spaces and periods within the faceplate name with underscores.

##### Example code for calling the faceplate pop-up outside a faceplate type

//JEx: "Faceplate in Popup"

//TagsRequired: "HMI_Tag_1"

//FPlateRequired: "Faceplate_1", "Interface_Tag_1", "Color_Property_1", "ResourceList_Property_1"

export function Button_1_OnTapped(item, x, y, modifiers, trigger) {

let data = {Interface_Tag_1:{Tag:"HMI_Tag_1"},Color_Property_1:0xff00ff00,ResourceList_Property_1:"@Default.Text_list_1"};

po = UI.OpenFaceplateInPopup("Faceplate01_V_0_0_1", "Popup", data, UI.ActiveScreen, false);

po.Left = 100;

po.Top = 150;

}

##### Example code for closing the faceplate pop-up outside a faceplate type

//JEx: "Close Faceplate in Popup"

//FPlateRequired: "Faceplate01_V_0_0_3", "po"

export function Button_2_OnTapped(item, x, y, modifiers, trigger) {

if (po)

{

po.Close();

po = undefined;

}

}

##### Calling a pop-up window within a faceplate type

To configure a faceplate as a pop-up window, for example, to an event of a screen object within a different faceplate type, follow these steps:

1. Create a faceplate type, for example, "Faceplate_1".

   The event that opens the pop-up window is configured in this faceplate type.
2. Create another faceplate type, for example, "Popup_1".

   This faceplate type is opened as a pop-up window.
3. Create the same interface tags in both faceplate types, for example, "Interface_Tag_1".
4. Create the same interface properties in both faceplate types, for example, "Color_Property_1" and "ResourceList_Property_1" (resource list data type).
5. Configure a screen object that is to open the pop-up window, e.g. a button, in the "Visualization" tab of "Faceplate_1".
6. Configure additional objects to visualize the two faceplate types.
7. Interconnect the tags and properties of both faceplate types.
8. Select the screen object which is to open the pop-up window.
9. Open the Inspector window under "Properties > Events".
10. Select an event.
11. Click on ![Calling a pop-up window within a faceplate type](images/160566469643_DV_resource.Stream@PNG-de-DE.png) "Convert function to script".

    A function is generated.
12. Use the "OpenFaceplateInPopup" method.

    - Define the type of the popup window with the desired version, for example, "Popup_1_V_0_0_1".  
      The correctly detected reference to the faceplate type is highlighted in green.
    - Define the title of the pop-up window, for example, "Popup".
    - Optional: The pop-up window is closed automatically when the specified screen is exited.

      Default: `independentWindow = false`.

      The pop-up window is closed when the faceplate or the screen is exited.

      In the example, the pop-up window remains open until the pop-up window is closed manually or Runtime is exited.
    - Optional: Specify whether the pop-up window is hidden.

      Default: `invisible = false`.

      The pop-up window is visible.
13. If required, specify where the pop-up window is opened.

    `po.Left = 100;`

    `po.Top = 150;`
14. Switch to the faceplate type "Popup_1".
15. Configure a "Close pop-up" button.
16. Open the Inspector window of the button under "Properties > Events".
17. Select an event.
18. Select the "Convert function to script" button.

    A function is generated.
19. Use the "Close" method.
20. Release both type versions.

**Note**

The name and data type of the interface tags and interface properties must match. The order may be changed. Missing interface tags or interface properties are not transferred.

##### Example code for calling the faceplate pop-up within a faceplate type

//JEx: "Faceplate in Popup within another Faceplate"

//FPlateRequired: "Popup_1"

export function Button_1_OnTapped(item, x, y, modifiers, trigger) {

po = Faceplate.OpenFaceplateInPopup("Popup_1_V_0_0_1", "Popup", true, false);

po.Left = 100;

po.Top = 150;

}

##### Example code for closing the faceplate pop-up within a faceplate type

//JEx: " Close Faceplate in Popup within another Faceplate"

//FPlateRequired: "Popup_1_V_0_0_1"

export function Button_2_OnTapped(item, x, y, modifiers, trigger) {

Faceplate.Close();

}

##### Result

When the configured event is triggered in Runtime, the pop-up window opens or closes.

### Example: Creating and using faceplates (RT Unified)

This section contains information on the following topics:

- [Example: Configuring faceplates (RT Unified)](#example-configuring-faceplates-rt-unified)
- [Example: Introduction (RT Unified)](#example-introduction-rt-unified)
- [Example: Create HMI tags (RT Unified)](#example-create-hmi-tags-rt-unified)
- [Example: Creating faceplate types (RT Unified)](#example-creating-faceplate-types-rt-unified)
- [Example: Configuring interface tags in faceplate types (RT Unified)](#example-configuring-interface-tags-in-faceplate-types-rt-unified)
- [Example: Configure local tags in faceplate types. (RT Unified)](#example-configure-local-tags-in-faceplate-types-rt-unified)
- [Instead of tags: Using PLC user data type in the faceplate type (RT Unified)](#instead-of-tags-using-plc-user-data-type-in-the-faceplate-type-rt-unified)
- [Example: Instantiate the inner faceplate type in the outer faceplate type (RT Unified)](#example-instantiate-the-inner-faceplate-type-in-the-outer-faceplate-type-rt-unified)
- [Example: Configuring interface properties in faceplate types (RT Unified)](#example-configuring-interface-properties-in-faceplate-types-rt-unified)
- [Example: Create an interface event (RT Unified)](#example-create-an-interface-event-rt-unified)
- [Example: Using e script to change tags (RT Unified)](#example-using-e-script-to-change-tags-rt-unified)
- [Example: Creating a local script for opening the pop-up (RT Unified)](#example-creating-a-local-script-for-opening-the-pop-up-rt-unified)
- [Example: Create local script to close the pop-up (RT Unified)](#example-create-local-script-to-close-the-pop-up-rt-unified)
- [Example: Configure the screen and instantiate the faceplate type. (RT Unified)](#example-configure-the-screen-and-instantiate-the-faceplate-type-rt-unified)
- [Example: Configuring a trend control with logging tags in faceplate type (RT Unified)](#example-configuring-a-trend-control-with-logging-tags-in-faceplate-type-rt-unified)
- [Example: Using a dynamic tag as an interface property (RT Unified)](#example-using-a-dynamic-tag-as-an-interface-property-rt-unified)
- [Example: Displaying a project in runtime. (RT Unified)](#example-displaying-a-project-in-runtime-rt-unified)

#### Example: Configuring faceplates (RT Unified)

##### Procedures overview

The example is divided into the following steps:

1. Create HMI tags.
2. Configure faceplate types:

   - A faceplate type that is instantiated in the screen.
   - A faceplate type that is opened as a pop-up from within the faceplate.
   - A faceplate type that is instantiated in the faceplate.
3. Configure interface tags in the faceplate types.
4. Configure local tags in faceplate types.

   Instead of tags: Use PLC user data types and thus minimize configuration work.
5. Instantiate inner faceplate type in outer faceplate type,
6. Configure interface properties in faceplate types.
7. Create an interface event.
8. Create a script to modify tags.
9. Creating the local scripts,
10. Configure the screen and instantiate the faceplate type.
11. Display project in Runtime.

---

**See also**

[Example: Creating faceplate types (RT Unified)](#example-creating-faceplate-types-rt-unified)
  
[Example: Configuring interface tags in faceplate types (RT Unified)](#example-configuring-interface-tags-in-faceplate-types-rt-unified)
  
[Instead of tags: Using PLC user data type in the faceplate type (RT Unified)](#instead-of-tags-using-plc-user-data-type-in-the-faceplate-type-rt-unified)
  
[Example: Creating a local script for opening the pop-up (RT Unified)](#example-creating-a-local-script-for-opening-the-pop-up-rt-unified)

#### Example: Introduction (RT Unified)

The example works with two motors and their data.

You configure a screen that displays data of the motor "Engine 01" in a faceplate instance.

A second faceplate is instantiated in this faceplate, which has two buttons and a text box.

Press "Start Engine" and "Stop Engine" to change the speed of the motor to 2 or 0 rpm.

After pressing, the output field indicates whether the motor is in the status "On" or "Off".

Use the slider to adapt the speed.

If the speed exceeds a specified value, the output field under speed control changes its color from white to red.

![Figure](images/160507168395_DV_resource.Stream@PNG-de-DE.png)

By pressing another button within the faceplate type, you open a new faceplate type as a pop-up that displays the speed of the motor "Engine 02".

![Figure](images/160528371595_DV_resource.Stream@PNG-de-DE.png)

#### Example: Create HMI tags (RT Unified)

##### Task

You create the HMI tags required for the project.

##### Requirement

- A project has been created.
- An HMI device has been configured.

##### Procedure

| 1. Open the "Standard tag table" editor under "HMI Tags" in the project tree. 2. Create the following tags in the "HMI tags" tab:       | Tag name | Data type |    | --- | --- |    | Engine01_CurrentRPM | Int |    | Engine01_SpeedMax | Int |    | Engine01_SpeedMin | Int |    | Engine02_CurrentRPM | Int | 3. Assign valid values to the tags in the Inspector window under "Properties > Properties > Values". |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

You have configured the HMI tags required for the example.

#### Example: Creating faceplate types (RT Unified)

##### Task

1. To create a faceplate type that is instantiated in the start screen. This faceplate type displays the "Engine 01" data in Runtime. Clicking a button opens another faceplate type as a popup.
2. You create a faceplate type that is opened as a pop-up from the faceplate type created in the first step when a button is clicked. This faceplate type displays the current speed of "Engine 02" in Runtime.
3. To create a faceplate type that is embedded in the faceplate from the first step and starts and stops the motor "Engine 01".

##### Requirement

- A project has been created.
- An HMI device has been configured.

##### Procedure

1. To create the first faceplate for "Engine 01"", create a new faceplate type in the project library and name it accordingly, for example, "FP_Engine01".

   A version 0.0.1 of the faceplate type is being created and has the status "In progress".

   The version is opened in the "Visualization" tab.
2. Drag the required objects from the "Toolbox" task card to the faceplate type. The objects required for the example are listed and described in the table below.
3. Arrange the objects according to your needs. This may look like this, for example:

   ![Procedure](images/160454292491_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/160454292491_DV_resource.Stream@PNG-de-DE.png)
4. To create the second faceplate type for "Engine 02", repeat steps 1 and 2. Name the faceplate type, for example, "FP_Engine02".
5. Arrange the objects according to your needs. This may look like this, for example:

   ![Procedure](images/160447281931_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/160447281931_DV_resource.Stream@PNG-de-DE.png)
6. To create the third faceplate type for "Engine StartStop", repeat steps 1 and 2. Name the faceplate type, for example, "FP_StartStop".
7. Arrange the objects according to your needs. This may look like this, for example:

   ![Procedure](images/160454459531_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/160454459531_DV_resource.Stream@PNG-de-DE.png)

##### Objects in the faceplate types

| Faceplate type | Object | Object name | Meaning/Properties |
| --- | --- | --- | --- |
| FP_Engine01 | Rectangle | Rectangle_1 | Limitation and background of the display area |
| Gauge | Gauge_1 | Instrument display of the current motor speed |  |
| Text box | Text box_1 | Text "Engine_01" |  |
| Text box | Text box_2 | Text "Speed Max" |  |
| Text box | Text box_3 | Text "Speed Min" |  |
| Text box | Text box_4 | Text "rpm" |  |
| Text box | Text box_5 | Text "rpm" |  |
| Text box | Text box_6 | Text "rpm" |  |
| IO field | IO field_1 | Display of the HMI tag "Engine01_SpeedMin" |  |
| IO field | IO field_2 | Display of the HMI tag "Engine01_SpeedMax" |  |
| IO field | IO field_3 | Display of the current motor speed. |  |
| Button | Button_1 | Pressing the button opens a pop-up that shows the speed for Engine 02. |  |
| FP_Engine02 | Rectangle | Rectangle_1 | Limitation and background of the display area |
| Gauge | Gauge_1 | Instrument display of the current motor speed |  |
| Text box | Text box_1 | Text "rpm" |  |
| IO field | IO field_1 | Display of the current motor speed. |  |
| Button | Button_1 | Pressing the button closes the pop-up. |  |
| FP_StartStop | Rectangle | Rectangle_1 | Limitation and background of the display area |
| Button | Button_1 | When the button is pressed, the speed of Engine 01 is set to the value 2. |  |
| Button | Button_2 | When the button is pressed, the speed of Engine 01 is set to the value 0. |  |
| IO field | IO field_1 | Display of the current motor status "On" or "Off". |  |

##### Result

The required faceplate types have been created and are in the status "In progress". The objects required in the faceplate types are configured.

---

**See also**

[Creating a faceplate type in the project library (RT Unified)](#creating-a-faceplate-type-in-the-project-library-rt-unified)
  
[Working with faceplate types and versions (RT Unified)](#working-with-faceplate-types-and-versions-rt-unified)

#### Example: Configuring interface tags in faceplate types (RT Unified)

##### Task

To configure tags in the faceplate type with which you can dynamically control properties and which are required for data exchange in the project.

##### Requirement

The faceplate types required for the example are created and are in the "In progress" state.

##### Configuring interface tags

> **Note**
>
> Interface tags are required for the exchange of values between the faceplate and the project.
>
> When used in screens, access to individual object properties in faceplates is possible exclusively via faceplate tags.
>
> When you follow the example with PLC user data types, use the PLC user data type accordingly. Note that the PLC user data type must exist in the project library in this case.

1. Open the faceplate type "FP_Engine01".
2. In the editor, switch to the "Tags Interface" tab.
3. Configure the required tags. To do this, click the button ![Configuring interface tags](images/120361703819_DV_resource.Stream@PNG-de-DE.png) or on "Add".

   The tags required for the various faceplate types are listed in the table below.
4. Repeat steps 1 to 3 for the faceplate types "FP_Engine02" and "FP_StartStop".

##### Interface tags of the faceplate types

| Faceplate type | Tag | Data type | Source | Target |
| --- | --- | --- | --- | --- |
| FP_Engine01 | Engine01_CurrentRPM | Int | Current speed Engine 01   (Actual value) | IO field   (Faceplate) |
| Engine01_SpeedMax | Int | Specification of the maximum speed | IO field   (Faceplate) |  |
| Engine01_SpeedMin | Int | Specification of the minimum speed | IO field   (Faceplate) |  |
| Engine02_CurrentRPM | Int | Current speed Engine 02   (Actual value) | IO field   (Faceplate) |  |
| FP_Engine02 | Engine02_CurrentRPM | Int | Current speed Engine 02  (Actual value) | IO field   (Faceplate) |
| FP_StartStop | Engine01_CurrentRPM | Int | Current speed Engine 01  (Actual value) | IO field  (FP_Engine01) |

##### Assigning interface tags in the faceplate types

To assign tags to the created objects in the faceplate types, follow these steps:

1. Open the Faceplate type in the "Visualization" tab.
2. Select the object to which you want to assign a tag.
3. Open the Inspector window under "Properties > Properties > General".
4. Under "Process value" in the "Dynamization" column, set the value "Tag".

   A screen for selecting the tag is shown on the right-hand side of the Inspector window.
5. Assign the corresponding tag to the "Process value" property. You will find the tag assignment in the table.

   If the tag is linked in the project, the object displays the corresponding values in Runtime.

**Note**

When you follow the example with PLC user data types, use the PLC user data type accordingly.

##### Tag assignment

| Faceplate type | Object | Object name | Tag assignment |
| --- | --- | --- | --- |
| FP_Engine01 | Gauge | Gauge_1 | Engine01_CurrentRPM |
| IO field | IO field_1 | Engine01_SpeedMax |  |
| IO field | IO field_2 | Engine01_SpeedMin |  |
| IO field | IO field_3 | Engine02_CurrentRPM |  |
| FP_Engine02 | Gauge | Gauge_1 | Engine02_CurrentRPM |
| IO field | IO field_1 | Engine02_CurrentRPM |  |
| FP_StartStop | IO field | IO field_1 | Engine01_CurrentRPM |

---

**See also**

[Using a PLC user data type (RT Unified)](#using-a-plc-user-data-type-rt-unified)
  
[Instead of tags: Using PLC user data type in the faceplate type (RT Unified)](#instead-of-tags-using-plc-user-data-type-in-the-faceplate-type-rt-unified)

#### Example: Configure local tags in faceplate types. (RT Unified)

##### Task

You configure a local tag in the faceplate type "FP_StartStop". Clicking the "Button_1" or "Button_2" buttons changes the local tag to "On" or "Off". The I/O field "IO field_1" displays the value of the local tag.

##### Requirement

- The faceplate type "FP_StartStop" has been created.
- The faceplate type is in the "in progress" status.

##### Configuring the local tags

> **Note**
>
> Local tags are used to exchange values within the faceplate. When used in screens, access to individual object properties in faceplates is not possible via local tags.

1. Open the faceplate type "FP_StartStop".
2. In the editor, go to the "Local tags" tab.
3. Configure the tag "OnOff" as a WString. To do this, click the button ![Configuring the local tags](images/120361703819_DV_resource.Stream@PNG-de-DE.png) or on "Add".

##### Assigning local tags in the faceplate types

1. Open the "Visualization" tab.
2. Select the I/O field "IO field_1".
3. Open the Inspector window under "Properties > Properties > General".
4. Under "Process value" in the "Dynamization" column, set the value "Tag". A screen for selecting the tag is shown on the right-hand side of the Inspector window.
5. Assign the local tag "OnOff" to the "Process value" property. If the tag is linked in the project, the object displays the corresponding values in Runtime.

   > **Note**
   >
   > When you follow the example with PLC user data types, use the PLC user data type accordingly.

##### Assigning values to local tag

To assign values to the configured local tag when the buttons are clicked, follow these steps:

1. Select the button "Button_1".
2. Open the Inspector window under "Properties > Events".
3. Select the event "Click left mouse button" and click the ![Assigning values to local tag](images/151911935115_DV_resource.Stream@PNG-de-DE.png) button.  
   A new script is created.
4. Define the following script:  
   `export function Button_Start_OnTapped(item, x, y, modifiers, trigger){`  
    `let tag1 = Tags("Engine01_CurrentRPM").Read();  
    if(tag1 == 0){  
    HMIRuntime.Tags.SysFct.SetTagValue("OnOff", "On");  
    }  
   }`
5. Repeat steps 2 and 3 for the "Button_2" button.
6. Select the event "Click left mouse button" and click the ![Assigning values to local tag](images/151911935115_DV_resource.Stream@PNG-de-DE.png) button.  
   A new script is created.
7. Define the following script:  
   `export function Button_Start_OnTapped(item, x, y, modifiers, trigger){`  
    `HMIRuntime.Tags.SysFct.SetTagValue("OnOff", "Off");  
   }`

> **Note**
>
> The scripts are extended in the course of this example to meet the still missing requirements.

##### Result

You have configured a local tag and assigned it to an I/O field. When the buttons are clicked, a value is assigned to the local tag.

#### Instead of tags: Using PLC user data type in the faceplate type (RT Unified)

##### Introduction

You have configured multiple motors of the same type. To do so, use data blocks based on a PLC user data type.

##### Task

You use the existing PLC user data type in the faceplate type.

You link the tags of the data blocks defined in the PLC user data type with those in the faceplate instance.

##### Requirement

- A SIMATIC S7-1200 or SIMATIC S7-1500 controller is configured.
- A PLC user data type suitable for the motor type is configured.
- At least one PLC tag based on the PLC user data type has been configured.
- The "Unified Faceplate Types" is opened with the created faceplate type.

##### Procedure

1. Drag the desired PLC user data type that you want to use in the project from the project tree into the project library under "Types".
2. Adapt the faceplate type so that the PLC user data type for the motors is also used in this faceplate type.

   - Switch to the "Tags interface" tab.
   - Select "PLCUDT" as the data type.
   - Under "User data type structure", select the defined PLC user data type.

     The PLC user data type supplies the faceplate type with the corresponding tags.
   - Switch back to the "Visualization" tab.
   - Keep in mind that tags are accessed in the faceplate type via the PLC user data type.

     This affects, for example, the use of faceplate tags in dynamized object properties and in local scripts.
3. Release the faceplate type.
4. From the faceplate type, create the same number of faceplate instances as the number of motors you have configured.
5. Link the tags from the data blocks and faceplate instances with each other.

   - The tag names in data blocks and faceplate instance are hierarchically structured.
   - This means that the tags from the individual faceplate instances can always be assigned uniquely to the tags of the respective data block.
   - When the PLC user data type contains tags that you do not require in the visualization, ignore these tags.

---

**See also**

[Using a PLC user data type (RT Unified)](#using-a-plc-user-data-type-rt-unified)

#### Example: Instantiate the inner faceplate type in the outer faceplate type (RT Unified)

##### Task

Insert the faceplate type "FP_StartStop" in the faceplate type "FP_Engine01".

##### Requirement

- The faceplate types "FP_StartStop" and "FP_Engine01" are created.
- The faceplate types are in the "In progress" status.

##### Procedure

1. Release the faceplate type "FP_StartStop".
2. Open the faceplate type "FP_Engine01" in the "Visualization" tab.
3. Drag-and-drop the "FP_Start_Stop" faceplate type into the "FP_Engine01" faceplate type at the desired location. This may look like this, for example:

   ![Procedure](images/160447273227_DV_resource.Stream@PNG-de-DE.png)

##### Assigning interface tags to the inner faceplate type

To assign tags to the inner faceplate type "FP_StartStop" from the outer faceplate type "FP_Engine01", follow these steps:

1. Open the faceplate type "FP_Engine01" in the "Visualization" tab.
2. Select the faceplate instance from "FP_StartStop".
3. Open the Inspector window under "Properties > Properties > Miscellaneous > Interface".
4. Assign the tag "Engine01_CurrentRPM" to the "Engine01_CurrentRPM" interface.

##### Result

An inner faceplate type is created in an outer faceplate type and the interface tags are assigned.

---

**See also**

[Using a faceplate type in another faceplate type (RT Unified)](#using-a-faceplate-type-in-another-faceplate-type-rt-unified)
  
[Using a PLC user data type (RT Unified)](#using-a-plc-user-data-type-rt-unified)
  
[Instead of tags: Using PLC user data type in the faceplate type (RT Unified)](#instead-of-tags-using-plc-user-data-type-in-the-faceplate-type-rt-unified)

#### Example: Configuring interface properties in faceplate types (RT Unified)

##### Task

Design the background color of the I/O field "IO field_3" (display box for the speed (actual value)) with interface properties. If a specified speed is exceeded, the background color of the I/O field should change from white to red.

##### Requirement

- The faceplate type "FP_Engine01" is configured.
- The faceplate type "FP_Engine01" is open for editing.

##### Configure interface property

1. Change to the "Property interface" tab in the editor.
2. Click the button ![Configure interface property](images/120361703819_DV_resource.Stream@PNG-de-DE.png) or on "Add".
3. Assign the name "BackgroundColor".
4. Select the "Color" data type:
5. Go to the "Visualization" tab.

##### Assign interface property

1. Select the I/O field "IO field_3".
2. Open the Inspector window under "Properties > Properties > Appearance".
3. Under "Background - color", in the "Dynamization" column, set the value to "Property interface".

   A screen for selecting the interface property is shown on the right side of the Inspector window.
4. Assign the interface property "BackgroundColor" to the "Background - color" property.

##### Result

You have configured an interface property that allows you to customize the background color in the faceplate instance.

The value of the interface property "BackgroundColor" adapts the background of the I/O field "IO field_3" in Runtime.

---

**See also**

[Interface properties in faceplates (RT Unified)](#interface-properties-in-faceplates-rt-unified)

#### Example: Create an interface event (RT Unified)

##### Task

You configure an interface event in the faceplate type "FP_StartStop". To set the speed to 0, use the interface event in the faceplate instance that is used in the faceplate type "FP_Engine01".

##### Requirement

- The faceplate type "FP_StartStop" is configured.
- The faceplate type "FP_StartStop" is open for editing.

##### Configuring an interface event

1. In the editor, go to the "Event interface" tab.
2. Click on the button or on the entry "Add".  
   A new interface event is created.
3. Assign the name "Engine_Stop".
4. Click on the entry "Add" below the interface event.  
   A new parameter is created. The data type of the parameter is "Int".
5. Assign the name "Stop".

##### Assigning an interface event

1. Select the "Button_2" button.
2. Open the Inspector window under "Properties > Events".
3. Select the event "Click left mouse button" and click on the button ![Assigning an interface event](images/151911935115_DV_resource.Stream@PNG-de-DE.png).
4. Define the following script:  
   `export function Button_Stop_OnTapped(item, x, y, modifiers, trigger) {  
    let parameters = {Stop:0};  
    Faceplate.RaiseEvent("Engine_Stop", parameters);  
    HMIRuntime.Tags.SysFct.SetTagValue("OnOff", "Off");  
   }`
5. Release the faceplate type "FP_StartStop".

##### Calling an interface event in instance

1. Open the faceplate type "FP_Engine01".
2. Select the faceplate instance of the "FP_StartStop" faceplate type.
3. Open the Inspector window under "Properties > Events".
4. Select the "Engine_Stop" event and click the button ![Calling an interface event in instance](images/151911935115_DV_resource.Stream@PNG-de-DE.png).
5. Define the following script:  
   `export function Faceplate_container_1_OnStop_Engine(item, Stop) {  
    HMIRuntime.Tags.SysFct.SetTagValue("Engine01_CurrentRPM", Stop);  
   }`

##### Result

You have configured an interface event with which you can set the speed to the value 0.

#### Example: Using e script to change tags (RT Unified)

##### Task

To increase the speed via the interface tag "Engine01_CurrentRPM", expand the script that runs when the "Button_1" button is clicked.

##### Requirement

- The faceplate type "FP_StartStop" is configured.
- The interface tag "Engine01_CurrentRPM" has been configured.
- The faceplate type "FP_StartStop" is open for editing.

##### Configuring a script

1. In the editor, switch to the "Visualization" tab.
2. Select the button "Button_1".
3. Open the Inspector window under "Properties > Events".
4. Select the event "Click left mouse button" and click on ![Configuring a script](images/151911935115_DV_resource.Stream@PNG-de-DE.png).
5. Define the following script:  
   `export function Button_Start_OnTapped(item, x, y, modifiers, trigger) {  
    let tag1 = Tags("Engine01_CurrentRPM").Read();  
    if (tag1 == 0) {  
    HMIRuntime.Tags.SysFct.SetTagValue("Engine01_CurrentRPM", 2);  
    HMIRuntime.Tags.SysFct.SetTagValue("OnOff", "On");`  
    `}  
   }`

##### Result

You have configured a script with which the speed is set to a value of 2 when you click the "Button_1" button.

#### Example: Creating a local script for opening the pop-up (RT Unified)

##### Task

You create a script that runs when a button is clicked and transfers values to tags. Clicking the button in the faceplate type opens an additional faceplate type as a pop-up.

##### Requirement

- The faceplate types "FP_Engine01" and "FP_Engine02" are created.
- The "FP_Engine02" faceplate type is released in the version 0.0.1.

  > **Note**
  >
  > If necessary, adapt the script below according to your released version.
  >
  > Replace spaces and periods with underscores.
- The faceplate type "FP_Engine01" is open for editing.

##### Procedure for creating the script: Opening the faceplate pop-up in the faceplate type

1. In the editor, switch to the "Visualization" tab.
2. Select the "Button_1" button.
3. Open the Inspector window under "Properties > Events".
4. Select the entry "Click left mouse button" and click on the button ![Procedure for creating the script: Opening the faceplate pop-up in the faceplate type](images/151911935115_DV_resource.Stream@PNG-de-DE.png).
5. Define the following script:  
   `export function Button_1_OnTapped(item, x, y, modifiers, trigger) {  
    let po = Faceplate.OpenFaceplateInPopup("FP_Engine02_V_0_0_1", "Engine02", true, false);  
    po.Left = 100;  
    po.Top = 150;  
    po.Visible = true;  
   }`

**Note**

When you follow the example with PLC user data types, note the deviating tag names.

##### Result

You have configured a script at the button in the faceplate type that opens an additional faceplate as a pop-up.

---

**See also**

[Dynamizing a faceplate type (RT Unified)](#dynamizing-a-faceplate-type-rt-unified)
  
[Configure faceplate as pop-up (RT Unified)](#configure-faceplate-as-pop-up-rt-unified)

#### Example: Create local script to close the pop-up (RT Unified)

##### Task

You create a script that runs when a button is clicked and closes the faceplate pop-up in which the button is located.

##### Requirement

- The faceplate types "FP_Engine01" and "FP_Engine02" are created.
- The faceplate type "FP_Engine02" is open for editing.

##### Procedure for creating the script: Closing the faceplate pop-up

1. In the editor, switch to the "Visualization" tab.
2. Select the button.
3. Open the Inspector window under "Properties > Events".
4. Select the entry "Click left mouse button" and click on the button ![Procedure for creating the script: Closing the faceplate pop-up](images/151911935115_DV_resource.Stream@PNG-de-DE.png).
5. Define the following script:  
   `export function Button_1_OnTapped(item, x, y, modifieres, trigger) {  
    Faceplate.Close();  
   }`

##### Result

To close the faceplate pop-up, you have configured a script on the button in the faceplate type.

#### Example: Configure the screen and instantiate the faceplate type. (RT Unified)

##### Task

You insert an instance of the faceplate type "FaceplateEngine01" in a screen and link the tags of the faceplate instance with tags in the project.

##### Requirement

- A screen has been created.
- The "Screens" editor is open.

##### Creating a faceplate instance

1. Release all created faceplate types.
2. Drag and drop the "FP_Engine01" faceplate type into the "Screens" editor.  
   Alternatively, drag the "Faceplate container" object into the editor and link the container with the faceplate type.
3. Define the properties of the faceplate container.
4. Under "Interface", assign the appropriate tag to all existing interface tags.

   Assign a value for the "BackgroundColor" interface property.

**Note**

To avoid error messages about inconsistency, start with the inner faceplate when releasing the faceplates. In the example, this is "FP_StartStop". Then release the faceplate that will be instantiated in the script. In the example, this is "FP_Engine02". To finish, release "FP_Engine01".

##### Assigning tags

1. Select the faceplate instance or the faceplate container.
2. Open the Inspector window under "Properties > Properties > Miscellaneous > Interface".
3. Assign the appropriate HMI tag to all existing interface tags.

##### Assigning interface properties

1. Select the faceplate instance or the faceplate container.
2. Open the Inspector window under "Properties > Properties > Miscellaneous > Interface".
3. Under "BackgroundColor", in the "Dynamization" column, set the value to "Script".
4. Create the following script:  
   `export function Faceplate_Container_1_Properties_BackgroundColor_Trigger (item) {  
    var value;  
    let ProcessValue = Tags("Engine01_CurrentRPM").Read();  
    if (ProcessValue > 40) {  
    value = HMIRuntime.Math.RGB(255,0,0)`  
    `}  
    else {  
    value = HMIRuntime.Math.RGB(255,255,255)  
    }  
    return value;  
   }`

The background color of the I/O field "IO field_3" in faceplate type "FP_Engine01" is white up to a speed of 40. When this speed is exceeded, the background color changes to red.

##### Inserting a slider

1. Drag and drop a slider from the "Toolbox" task card into the screen.
2. Select the slider and open the Inspector window under "Properties > Properties > General".
3. Assign the "Engine01_CurrentRPM" tag to the "Process value" property.

##### Result

The faceplate type is instantiated on a screen in a faceplate container.

You have linked the interface tags with project tags.

You have assigned a dynamic value to the "BackgroundColor" property of the I/O field "IO field_3".

You have configured a slider that can be used to adapt the speed "Engine01_CurrentRPM" in Runtime.

This completes the integration of the faceplate type into the project.

---

**See also**

[Creating a faceplate instance](#creating-a-faceplate-instance)

#### Example: Configuring a trend control with logging tags in faceplate type (RT Unified)

##### Task

You create a data log with two logging tags. You configure a faceplate type with a trend control. You use interface properties of the faceplate type to link the trend control with the logging tags.

##### Requirement

- An HMI screen has been configured.
- HMI tags "Engine01_CurrentRPM" and "Engine02_CurrentRPM" have been configured.

##### Creating logging tags

1. Open "Logs" of the HMI device in the project tree.
2. Add the data log "DataLog_EngineRPM".
3. Open the "Default tag table" editor under "HMI tags" in the project tree.
4. Click the HMI tag "Engine01_CurrentRPM".
5. Click "Logging tags" in the work area.
6. Add a logging tag.

   The logging tag is automatically linked with the HMI tag "Engine01_CurrentRPM" and added to the created data log "DataLog_EngineRPM".
7. Name the logging tag "LogTag_Engine01_CurrentRPM".

   ![Creating logging tags](images/166692142347_DV_resource.Stream@PNG-en-US.png)

   ![Creating logging tags](images/166692142347_DV_resource.Stream@PNG-en-US.png)
8. Click the HMI tag "Engine02_CurrentRPM" and repeat steps 5 to 8.

##### Configuring a faceplate type with trend control

1. Create the faceplate type "FP_TrendView".
2. Navigate to "Controls" in the "Toolbox" task card.
3. Add a trend control to the faceplate type using drag-and-drop.
4. Add another trend to the trend control in the Inspector window in the properties under "General > Trend areas > [0] Trend area > Trends" .
5. Change the "Display name" property of the trends in "Engine01 - RPM" and "Engine02 - RPM".
6. Select the color in the "Line - Color" property for both trends.
7. Deactivate all window settings except "Show border" in the properties under "Appearance" in the Inspector window.
8. Adapt the size of the faceplate type in the properties under "Size and position" in the Inspector window.

   ![Configuring a faceplate type with trend control](images/166692280715_DV_resource.Stream@PNG-en-US.png)

   ![Configuring a faceplate type with trend control](images/166692280715_DV_resource.Stream@PNG-en-US.png)

##### Creating interface properties in faceplate type

1. In the work area, select "Property interface".
2. Add two interface properties "Engine01_DataSource_Interface" and "Engine02_DataSource_Interface".
3. For both interface properties, select "Configuration string" as data type.
4. Click on the background of the faceplate type.
5. In the Inspector window, select an event of the type "Loaded".
6. Convert the function list to a script.
7. Insert the following script:  
   `export function Faceplate_Typ_OnLoaded(item) {  
   Faceplate.Items("Trend control_1").TrendAreas.Item(0).Trends(0).DataSourceY.Source = Faceplate.Properties.Engine01_DataSource_Interface;  
   Faceplate.Items("Trend control_1").TrendAreas.Item(0).Trends(1).DataSourceY.Source = Faceplate.Properties.Engine02_DataSource_Interface;  
   }`
8. Release the faceplate type.

##### Linking the logging tags with the faceplate instance

1. Open the configured HMI screen.
2. Place a faceplate instance of the configured faceplate type from the project library in the HMI screen using drag-and-drop.
3. Click on the faceplate instance in the HMI screen.
4. In the properties in the Inspector window, navigate to "Miscellaneous > Interface".
5. Link the interfaces with the corresponding logging tags in the form: <HMI tag>:<Logging tag>.

   In this case, this is "Engine01_CurrentRPM:LogTag_Engine01_CurrentRPM" and "Engine02_CurrentRPM:LogTag_Engine02_CurrentRPM".

   ![Linking the logging tags with the faceplate instance](images/166692444683_DV_resource.Stream@PNG-en-US.png)

   ![Linking the logging tags with the faceplate instance](images/166692444683_DV_resource.Stream@PNG-en-US.png)

##### Result

You have created a log with logging tags.

A faceplate type with a trend control and interface properties has been created.

A faceplate instance of the faceplate type is configured in the screen.

The logging tags are passed to the faceplate instance at the interfaces.

---

**See also**

[WinCC Unified Engineering V18 | Logging tags](https://support.industry.siemens.com/cs/mdm/109813308?c=159373006859&lc=en-WW)

#### Example: Using a dynamic tag as an interface property (RT Unified)

##### Task

You dynamize the "Interface" object property of a faceplate instance with a tag parameter. You configure a button that changes the dynamic tag name of the interface when clicked.

##### Requirement

- A screen has been created in the HMI device.
- The "Engine01_CurrentRPM" and "Engine02_CurrentRPM" HMI tags have been created.

##### Configuring HMI tags

1. Open the default tag table in the project tree.
2. Create the following HMI tag:

   | Name | Type |
   | --- | --- |
   | Engine03_CurrentRPM | Int |
   | Engine04_CurrentRPM | Int |
   | Engine05_CurrentRPM | Int |
   | EngineRef | WString |
3. Set the start value of the "EngineRef" tag to "01" under "Properties > Properties > Values".

##### Configuring a faceplate type

1. Duplicate the "FP_Engine02" faceplate type in the project library via the shortcut menu.
2. Name the new faceplate type "FP_EngineSwitch".
3. Delete the "Button_1" screen object.
4. Insert an object of "Text box" type via the gauge.

   ![Configuring a faceplate type](images/171624366219_DV_resource.Stream@PNG-de-DE.png)

##### Dynamizing a text box

- Click on the text box.
- Navigate in the properties to "General > Text".
- Select a script for dynamization.
- Insert the following script:

  `export function Text_box_1_Text_trigger(item) {`
    
  `var value;`
    
  `value = Faceplate.Parent.Properties.Engine02_CurrentRPM.Tag;`
    
  `return value;`
    
  `}`
- Click on the trigger symbol ![Dynamizing a text box](images/171430343819_DV_resource.Stream@PNG-de-DE.png).
- Select the trigger "T250ms".
- Release the faceplate type.

##### Configuring a button with event

1. Open the HMI screen in the editor window.
2. Insert an object of "Button" type.
3. Change the text of the button to "Switch Engine".
4. Select the "Click left mouse button" event in the Inspector window.
5. Convert the function list to a script.
6. Insert the following script:

   `export function Button_Start_OnTapped(item, x, y, modifiers, trigger){`
     
   `const Engine_list = ["01", "02", "03", "04", "05"];`
     
   `let currentEngine = Engine_list.indexOf(Tags("EngineRef").Read());`
     
   `let nextEngine = (++ currentEngine)%Engine_list.length;`
     
   `Tags("EngineRef").Write(Engine_list[nextEngine]);`
     
   `}`

##### Configuring a faceplate instance

1. Add a faceplate instance of "FP_EngineSwitch" to the screen.
2. Select the faceplate instance and navigate to "Properties > Properties > Miscellaneous > Interfaces > Engine02_CurrentRPM".
3. Select "Tag parameter" for dynamization of the interface.

   The "Tag parameter" window opens.
4. Select the "Engine01_CurrentRPM" tag for the "Engine02_CurrentRPM" interface.
5. Delete the single quotation marks at the beginning and end of the tag name.
6. Insert the tag reference 'EngineRef' in place of the "01" in the dynamic tag name.

   | Symbol | Meaning |
   | --- | --- |
   | ![Configuring a faceplate instance](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for working effectively** |
   | To select the tag reference, click at the desired place in the dynamic tag name and press <Ctrl+J>. |  |

   ![Configuring a faceplate instance](images/171624374795_DV_resource.Stream@PNG-en-US.png)

##### Result

A faceplate type has been duplicated.

A text box is dynamized by a script.

The interface of a faceplate instance is dynamized by tag parameters.

A button for changing the motor in the faceplate instance is created.

#### Example: Displaying a project in runtime. (RT Unified)

##### Procedure

1. Compile and upload the project to the HMI device.
2. Open the Runtime on the HMI device.

##### Result

When you have implemented the project as shown in the example, you will see the following elements in Runtime that display the values you have specified:

1. Start screen:

   ![Result](images/171430597899_DV_resource.Stream@PNG-de-DE.png)

   ![Result](images/171430597899_DV_resource.Stream@PNG-de-DE.png)
2. After pressing the button to start the motor:

   ![Result](images/171430726539_DV_resource.Stream@PNG-de-DE.png)

   ![Result](images/171430726539_DV_resource.Stream@PNG-de-DE.png)
3. After pressing the button to open the pop-up:

   ![Result](images/171430721803_DV_resource.Stream@PNG-de-DE.png)

   ![Result](images/171430721803_DV_resource.Stream@PNG-de-DE.png)
4. After changing the values of the "Engine01_CurrentRPM" and "Engine02_CurrentRPM" tags by sliders or IO fields:

   ![Result](images/171430777099_DV_resource.Stream@PNG-de-DE.png)

   ![Result](images/171430777099_DV_resource.Stream@PNG-de-DE.png)
5. After pressing the button multiple times and entering a value in the IO field:

   ![Result](images/171430900875_DV_resource.Stream@PNG-de-DE.png)

   ![Result](images/171430900875_DV_resource.Stream@PNG-de-DE.png)
