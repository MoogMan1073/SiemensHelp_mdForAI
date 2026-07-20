---
title: "Creating CEM programs (S7-1200, S7-1500)"
package: ProgBlockCEMenUS
topics: 39
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Creating CEM programs (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic information on CEM (S7-1200, S7-1500)](#basic-information-on-cem-s7-1200-s7-1500)
- [The programming window of CEM (S7-1200, S7-1500)](#the-programming-window-of-cem-s7-1200-s7-1500)
- [Designing a cause-effect matrix using the example of a baggage conveying system (S7-1200, S7-1500)](#designing-a-cause-effect-matrix-using-the-example-of-a-baggage-conveying-system-s7-1200-s7-1500)
- [Programming causes (S7-1200, S7-1500)](#programming-causes-s7-1200-s7-1500)
- [Programming effects (S7-1200, S7-1500)](#programming-effects-s7-1200-s7-1500)
- [Programming intersections (S7-1200, S7-1500)](#programming-intersections-s7-1200-s7-1500)
- [Block interface of a CEM program (S7-1200, S7-1500)](#block-interface-of-a-cem-program-s7-1200-s7-1500)

## Basic information on CEM (S7-1200, S7-1500)

This section contains information on the following topics:

- [CEM programming language (S7-1200, S7-1500)](#cem-programming-language-s7-1200-s7-1500)
- [Rules for creating CEM programs (S7-1200, S7-1500)](#rules-for-creating-cem-programs-s7-1200-s7-1500)

### CEM programming language (S7-1200, S7-1500)

#### Programming language

CEM (Cause-Effect-Matrix) is a programming language with which you can quickly and clearly define direct cause-effect relationships. You describe specific process events and define possible process reactions. You assign these to one another in a two-dimensional matrix.

In CEM methodology, a process event is called a "cause", while the process reaction is called an "effect". A cause is responsible for the activation of one or more effects. A cause is represented by a row in the matrix, an effect by a column. Intersections connect causes and effects to each other. They specify which causes have an effect on the respective effects.

Clear representation of cause and effect ensures that a CEM program can be quickly understood both in the project configuration and commissioning phase as well as during servicing.

> **Note**
>
> **Video tutorial on CEM**
>
> [Automate efficient engineering with Cause Effect Matrix (CEM) in less than 10 minutes](https://youtu.be/FaR9rVXUkJo)

#### Example

![Example](images/138305546891_DV_resource.Stream@PNG-de-DE.png)

#### Application

- Enable and interlock logics

  Typical interlock functions are access restrictions to plant units as well as the non-safety-oriented shutdown of machines or plant units due to supervisions.

  A typical enable function is the query of preconditions for opening valves or starting motors or process actions.
- Group supervisions

  States of numerous sensors can be quickly and conveniently monitored with the cause-effect matrix and reactions can be triggered even due to "m out of n" logic.

  Example: A supervision of 100 sensors is not to put out an alarm until at least five of the sensors signal a bad status.
- Graphical programming of processes

  Cause-and-effect diagrams are based on the technological structure of the system or the process and are easy to understand due to the graphic representation. Therefore, they are the proven basis for interdisciplinary cooperation during the entire development process, commissioning, startup, operation and maintenance phases of the systems.

> **Note**
>
> **System requirements**
>
> CEM is supported in S7-1500 as of firmware V2.6 and in S7-1200 as of firmware V4.2.
>
> **Restrictions**
>
> The restrictions for CEM are described in the Readme.
>
> See also: [Notes on CEM](STEP%207.md#notes-on-cem-s7-1200-s7-1500)

### Rules for creating CEM programs (S7-1200, S7-1500)

#### Number of causes and effects in a block

You can program a maximum of 250 causes and 250 effects in a CEM block.

#### Runtime behavior of CEM programs

CEM programs are executed from left to right. The following diagram shows the runtime behavior:

![Runtime behavior of CEM programs](images/138310718219_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① ② ③ ④ | First, all causes are evaluated from top to bottom. |
| ⑤ ⑥ | Next, the intersection column to the very left is executed and the associated effect is set or reset. |
| ⑦ ⑧ | All additional intersection columns with their effects are then executed from left to right. |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Call of CEM blocks in the user program**  In order to ensure that the CEM block runs correctly, the block must be called at least once every twelve days. Otherwise, internal time functions may overflow and disrupt the program flow. |  |

#### Block calls

In CEM programs, it is not possible to call other lower-level blocks.

#### Instructions

When programming, only the instructions from the "Basic instructions" palette are available. Instructions from other pallets, for example you cannot use the "Extended instructions" palette in a CEM program.

#### Optimized block access

Basically, CEM blocks use the optimized block format. The "Optimized block access" attribute is always enabled for the CEM blocks and cannot be deselected.

## The programming window of CEM (S7-1200, S7-1500)

This section contains information on the following topics:

- [Overview of the programming window (S7-1200, S7-1500)](#overview-of-the-programming-window-s7-1200-s7-1500)
- [Creating CEM blocks and opening the programming window (S7-1200, S7-1500)](#creating-cem-blocks-and-opening-the-programming-window-s7-1200-s7-1500)

### Overview of the programming window (S7-1200, S7-1500)

The programming window is the area where you create the cause-effect matrix.

You can perform the following tasks here:

- Programming causes
- Programming effects
- Programming intersections

#### Structure of the programming window

The following figure shows the programming window of CEM:

![Structure of the programming window](images/134013331595_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Programming area for effects |
| ② | Programming area for causes |
| ③ | Programming area for intersections |

> **Note**
>
> **Keyboard operation**
>
> The keyboard operations that are available to you when programming with CEM are described here:
>
> [Using the keyboard in the program editor](Program%20editor.md#using-the-keyboard-in-the-program-editor)

#### Adjusting the display in the programming window

You can adjust the display of the matrix in the programming window depending on your programming task. For example, you can set up the display so that as many causes and effects as possible are shown and you do not have to move the work area.

You can use the following functions for this:

- Minimizing causes and effects
- Showing and hiding programming areas for causes and effects
- Showing and hiding comments
- Showing and hiding favorites

#### Minimizing causes and effects

In the minimized view, only the name of a cause or effect is displayed. The instruction box with the interconnected operands is hidden and only the name of the element remains visible. You can minimize either only the causes, only the effects or both elements.

To display causes or effects minimized, follow these steps:

1. Click one of the two buttons on the toolbar:

   - "Minimize/expand causes"  
      or
   - "Minimize/expand effects"

   The boxes of the causes or effects are hidden.
2. To show the boxes again, click the button again.

#### Showing and hiding programming areas for causes and effects

The areas in which the causes and effects are displayed can be shown or hidden. When an area is hidden, only the numbers of the causes or effects are visible.

To show or hide a programming area, follow these steps:

1. Click on the arrow buttons inside the split bar.

#### Showing and hiding comments

To hide the comments for all causes and effects, follow these steps:

1. Click the "Show/hide comments in causes and effects" button on the toolbar.
2. To show the comments again, click the button again.

#### Showing and hiding favorites

You can save frequently used instructions as favorites. These favorites are then displayed in the "Instructions" task card and the "Favorites" pane. You can also display the favorites in the programming window. You can then access your favorites even if the "Instructions" task card is not visible.

To display the favorites in the programming window, follow these steps:

1. Click the "Display favorites in the editor" button in the toolbar.
2. To hide the favorites again, click the button again.

### Creating CEM blocks and opening the programming window (S7-1200, S7-1500)

You can open the programming window by creating a new CEM block or opening an existing CEM block.

#### Creating a CEM block

To create a CEM block, follow these steps:

1. Open the "Program blocks" folder in the project tree.
2. Double-click the "Add new block" command.

   The "Add new block" dialog box opens.
3. Click the "Function block (FB)" button.
4. Select "CEM" as language.
5. Enter a name for the new block.
6. Enter the properties of the new block.
7. To enter additional properties of the new block, click "Additional information".

   An area with additional entry fields is displayed.
8. Enter all the desired properties.
9. Select the "Add new and open" check box if the block is to be opened as soon as it is created.
10. Confirm your entries with "OK".

The new CEM block is created. You can find the block in the project tree in the "Program blocks" folder.

#### Opening a CEM block

To open an existing CEM block, follow these steps:

1. Open the "Program blocks" folder in the project tree.
2. Double-click the block.

The block will open in the CEM programming window.

---

**See also**

[Creating blocks](Creating%20and%20managing%20blocks.md#creating-blocks)
  
[Managing blocks](Creating%20and%20managing%20blocks.md#managing-blocks)

## Designing a cause-effect matrix using the example of a baggage conveying system (S7-1200, S7-1500)

This section contains information on the following topics:

- [Introduction to the example program (S7-1200, S7-1500)](#introduction-to-the-example-program-s7-1200-s7-1500)
- [Program example: Creating causes (S7-1200, S7-1500)](#program-example-creating-causes-s7-1200-s7-1500)
- [Program example: Creating effects (S7-1200, S7-1500)](#program-example-creating-effects-s7-1200-s7-1500)
- [Program example: Creating intersections (S7-1200, S7-1500)](#program-example-creating-intersections-s7-1200-s7-1500)
- [Extending the example with an interlock function (S7-1200, S7-1500)](#extending-the-example-with-an-interlock-function-s7-1200-s7-1500)
- [Program status of the example program (S7-1200, S7-1500)](#program-status-of-the-example-program-s7-1200-s7-1500)

### Introduction to the example program (S7-1200, S7-1500)

This chapter is an introduction to the CEM methodology. Using a simple technological example program, it will show you how to design a cause-effect matrix and configure it step by step.

> **Note**
>
> **Video tutorial for the example program**
>
> [Automate efficient engineering with Cause Effect Matrix (CEM) in less than 10 minutes](https://youtu.be/FaR9rVXUkJo)

#### **Methodology of a CEM program**

Many applications in production and process engineering require defined reactions to specific process events. You can program these reactions with a cause-effect matrix. In doing so, you describe specific process events and define possible process reactions.

In CEM methodology, a process event is called a "cause", while the process reaction is called an "effect". A cause is responsible for the activation of one or more effects.

- A cause is represented by a row in the matrix.
- Effects are placed in the columns of the matrix.
- Points of intersection that connect causes and effects with each other are called "Intersections". They determine which causes affect the respective effects.

#### **Technological task**

Our example deals with controlling a simple baggage conveying system. The following preconditions are to be tested:

- Has a bag been placed on the belt?
- Does the bag weigh a maximum of 20 kg?
- What is the destination of the bag (Berlin or Hawaii)?

Different conveyor belts are switched on depending on these preconditions.

![Technological task](images/141021097995_DV_resource.Stream@PNG-de-DE.png)

The basic example must subsequently be extended with an interlock function:

If a customs officer wants to inspect a bag, he can stop the conveyor belts by pressing a button. After the inspection, he can restart the belts by pressing another pushbutton.

### Program example: Creating causes (S7-1200, S7-1500)

#### Creating causes

For the example program, four causes are required, which query whether the preconditions for the baggage transport have been met.

![Creating causes](images/138313902219_DV_resource.Stream@PNG-en-US.png)

1. The cause "GetSensors" checks whether a bag has been placed on the belt. This is detected by means of two light barriers. The bag was placed correctly when it passed both light barriers. Therefore, select an AND logic operation of both sensors.

   In addition, a timer is programmed to influence the activation of the cause. The timer "OnDelay" delays activation of the cause by 10 seconds. This timer is used to check whether the bag was on the belt for long enough to be weighed.
2. Additionally, at the cause "GetScale", there is a check whether the bag weighed a maximum of 20 kg. A comparator is used to do so.
3. The third cause, "Berlin", checks the destination airport of the bag. It has to become active if the bag’s destination is "Berlin".
4. The fourth cause becomes active if the bag’s destination is "Hawaii".

Detailed step-by-step instructions for programming the causes can be found here:

[Programming causes](#programming-causes-s7-1200-s7-1500)

### Program example: Creating effects (S7-1200, S7-1500)

#### Creating effects

The conveying system consists of two belts, either of which is switched on depending on the bag’s destination. You therefore need two effects for controlling the two belts.

![Creating effects](images/138316335115_DV_resource.Stream@PNG-en-US.png)

1. The effect "RunBeltBerlin" switches on the belt for destination Berlin.
2. The effect "RunBeltHawaii" switches on the belt for destination Hawaii.

Detailed step-by-step instructions for programming the effects can be found here:

[Programming effects](#programming-effects-s7-1200-s7-1500)

### Program example: Creating intersections (S7-1200, S7-1500)

#### Creating intersections

Now, at the intersections of the cause-effect matrix, the so-called intersections, you have to define which conditions have to be fulfilled so that belt 1 or belt 2 gets switched on. According to the task definition, there are three conditions assigned to each conveyor belt:

- Has a bag been on the belt for 10 seconds?
- Does it weigh a maximum of 20 kg?
- What is the destination of the bag?

All three conditions must be satisfied for the belt to start moving.

Therefore, you have to program three intersections in the CEM matrix for each effect. The intersections of a column must all be satisfied for the assigned effect to become active. They must be linked with a logical AND.

The following steps are necessary for this task:

1. First, program the actions in the intersections.
2. Then connect the actions with an AND.

#### Programming actions in intersections

You can program the following actions in intersections:

- The action "N" sets the signal state at the input of an effect to "1" as long as the cause is active. When the cause becomes inactive, the effect is automatically reset to signal state "0".
- The actions "S" and "R" are always used in pairs. "S" sets the signal state at the input of an effect to "1". The signal state remains at "1" until it is reset by the action "R".

See also: [Programming intersections](#programming-intersections-s7-1200-s7-1500)

For the intersections that you edit in this programming step, select the "N" action, as shown in the figure below using the example of the intersection between the cause "GetSensors" and the effect "RunBeltBerlin":

![Programming actions in intersections](images/138316464011_DV_resource.Stream@PNG-en-US.png)

#### Linking intersections with AND logic operation

By default, the intersections of a column are linked by a logical OR in CEM. As soon as one of the intersections becomes active, the associated effect is carried out.

However, in our tasks, the effects must only be executed if all the three conditions are satisfied.

In this case, you must link the three conditions with a logical AND.

Use an action group to do so. Combine all the three actions of the column in a group. The number indicates that all the three actions have to be active for the result of the group to be "true", so that the associated effect is executed.

See also: [Action groups in intersections](#action-groups-in-intersections-s7-1200-s7-1500)

![Linking intersections with AND logic operation](images/138316605707_DV_resource.Stream@PNG-en-US.png)

The three actions of each column are now linked by a logical AND.

#### Result

You have thus completed the basic example for the baggage conveying system:

- If a bag is on the belt for 10 seconds, there is a check to ensure that it does not exceed the permissible maximum weight of 20.0 kg.
- In addition, the destination of the bag is checked and the corresponding conveyor belt is switched on.

### Extending the example with an interlock function (S7-1200, S7-1500)

#### Programming the interlock

The basic example must now be extended with an interlock function:

If a customs officer wants to inspect a bag, he can press a red button. When that happens, both the belts must come to a standstill and a red indicator lamp must start to glow. When the inspection is over, the customs officer presses a green button to turn off the indicator lamp and to restart the belts.

![Programming the interlock](images/138316760459_DV_resource.Stream@PNG-en-US.png)

1. Add Cause 5 "LuggageCheck" to the matrix and link the signal of the red button to this cause. The cause must check whether the button was pressed.
2. Add Cause 6 "LuggageOK" and link it to the signal of the green button.
3. Now add Effect 3, "SetRedLight". The effect sets the output parameter "#blinkRed", which makes the lamp start to flash.

   Moreover, it also sets the static parameter "#statBlinkRed". This serves for stopping and starting the conveyor belts.

   See also:

   [Add output](#adding-or-inverting-inputs-and-outputs-at-a-cause-s7-1200-s7-1500)
4. At the intersection of Cause 5 and Effect 3, program the action "S". Its effect is that the red lamp flashes as soon as the red button is pressed. In addition, "#statBlinkRed" is set. Since you are using the action "S" here, Effect 3 "SetRedLight" stays permanently set, even if the signal "redButton" is not present any more. Thus, the indicator lamp continues to flash until it is explicitly reset.
5. At the intersection of Cause 6 and Effect 3, program the action "R". Its effect is that the lamp stops flashing when the green button is pressed. In addition, "#statBlinkRed" is reset.
6. Now, you only have to link the control of the two belts with the "#statblinkRed". To do so, modify Cause 1 "GetSensors". Add one more input to the AND logic operation.   
   The cause must only be active when the red lamp is not lit. Therefore, invert the input and connect it to "#statBlinkRed".

   See also:

   [Add input](#adding-or-inverting-inputs-and-outputs-at-an-effect-s7-1200-s7-1500)

   [Inverting](#adding-or-inverting-inputs-and-outputs-at-an-effect-s7-1200-s7-1500)

#### Result

You have now implemented an interlock for the baggage conveying system.

### Program status of the example program (S7-1200, S7-1500)

This section contains information on the following topics:

- [A bag is carried to Berlin (S7-1200, S7-1500)](#a-bag-is-carried-to-berlin-s7-1200-s7-1500)
- [A customs officer presses the red button (S7-1200, S7-1500)](#a-customs-officer-presses-the-red-button-s7-1200-s7-1500)
- [The customs officer releases the red button (S7-1200, S7-1500)](#the-customs-officer-releases-the-red-button-s7-1200-s7-1500)
- [The customs officer presses the green button (S7-1200, S7-1500)](#the-customs-officer-presses-the-green-button-s7-1200-s7-1500)

#### A bag is carried to Berlin (S7-1200, S7-1500)

##### Introduction

You can determine the mode of operation of the example program in the program status.

See also: [Program status display for intersections](Testing%20CEM%20programs%20%28S7-1200%2C%20S7-1500%29.md#program-status-display-for-intersections-s7-1200-s7-1500)

##### A bag is carried to Berlin

The following figure shows the program status when a bag of permissible weight and Berlin as the destination is transported.

![A bag is carried to Berlin](images/140189937291_DV_resource.Stream@PNG-en-US.png)

The program status display can be interpreted as follows:

| Program element | Program status display | Description |
| --- | --- | --- |
| Cause 1-3 are active. | ![A bag is carried to Berlin](images/139983474187_DV_resource.Stream@PNG-de-DE.png) | Green bar |
| Cause 4 is not active. | ![A bag is carried to Berlin](images/136953187851_DV_resource.Stream@PNG-de-DE.png) | Blue bar |
| All the intersections are active in column 1. The entire action group is thus satisfied. | ![A bag is carried to Berlin](images/136952964107_DV_resource.Stream@PNG-de-DE.png) | Green circle filled with green |
| The first two intersections are active in column 2. However, the entire action group is not yet satisfied. | ![A bag is carried to Berlin](images/136953120779_DV_resource.Stream@PNG-de-DE.png) | Blue circle with dual-color filling (green/blue) |
| In column 2, the third intersection of the action group is not active. | ![A bag is carried to Berlin](images/136953704459_DV_resource.Stream@PNG-de-DE.png) | Blue circle with blue filling |
| Effect 1 is active. | ![A bag is carried to Berlin](images/136953438987_DV_resource.Stream@PNG-de-DE.png) | Green bar |
| Effect 2 is not active. | ![A bag is carried to Berlin](images/136952972043_DV_resource.Stream@PNG-de-DE.png) | Blue bar |

#### A customs officer presses the red button (S7-1200, S7-1500)

##### Introduction

You can determine the mode of operation of the example program in the program status.

See also: [Program status display for intersections](Testing%20CEM%20programs%20%28S7-1200%2C%20S7-1500%29.md#program-status-display-for-intersections-s7-1200-s7-1500)

##### A customs officer presses the red button

The following figure shows the program status when a customs officer presses the red button.

![A customs officer presses the red button](images/140190117387_DV_resource.Stream@PNG-en-US.png)

The program status display can be interpreted as follows:

| Program element | Program status display | Description |
| --- | --- | --- |
| Cause 5 is active and activates Effect 3 via action "S": The red lamp starts to flash and "#statBlinkRed" is set. | ![A customs officer presses the red button](images/136953712395_DV_resource.Stream@PNG-de-DE.png) | Green circle filled with green |
| Cause 1 queries "statBlinkRed" inverted and thus becomes inactive. | ![A customs officer presses the red button](images/136953187851_DV_resource.Stream@PNG-de-DE.png) | Blue bar |
| The two action groups in columns 1 and 2 are not satisfied any more. | ![A customs officer presses the red button](images/136953120779_DV_resource.Stream@PNG-de-DE.png) | Blue circle with dual-color filling (green/blue) |
| ![A customs officer presses the red button](images/136953704459_DV_resource.Stream@PNG-de-DE.png) | Blue circle with blue filling |  |
| The associated effects are deactivated. | ![A customs officer presses the red button](images/136952972043_DV_resource.Stream@PNG-de-DE.png) | Blue bar |

#### The customs officer releases the red button (S7-1200, S7-1500)

##### Introduction

You can determine the mode of operation of the example program in the program status.

See also: [Program status display for intersections](Testing%20CEM%20programs%20%28S7-1200%2C%20S7-1500%29.md#program-status-display-for-intersections-s7-1200-s7-1500)

##### The customs officer releases the red button

The following figure shows the program status when a customs officer releases the red button.

![The customs officer releases the red button](images/140190156683_DV_resource.Stream@PNG-en-US.png)

The program status display can be interpreted as follows:

| Program element | Program status display | Description |
| --- | --- | --- |
| Cause 5 becomes inactive again, since the signal "#redButton" is not present any more | ![The customs officer releases the red button](images/136953187851_DV_resource.Stream@PNG-de-DE.png) | Blue bar |
| The "S" action has set the associated Effect 3, set permanently to 1. | ![The customs officer releases the red button](images/136953771531_DV_resource.Stream@PNG-de-DE.png) | Green circle, cyan fill |
| Effect 3 remains set. | ![The customs officer releases the red button](images/136953438987_DV_resource.Stream@PNG-de-DE.png) | Green bar |

#### The customs officer presses the green button (S7-1200, S7-1500)

##### Introduction

You can determine the mode of operation of the example program in the program status.

See also: [Program status display for intersections](Testing%20CEM%20programs%20%28S7-1200%2C%20S7-1500%29.md#program-status-display-for-intersections-s7-1200-s7-1500)

##### The customs officer presses the green button

The following figure shows the program status when a customs officer presses the green button.

![The customs officer presses the green button](images/140190311179_DV_resource.Stream@PNG-en-US.png)

The program status display can be interpreted as follows:

| Program element | Program status display | Description |
| --- | --- | --- |
| The operand "#greenButton" carries Signal 1 and Cause 6 "LuggageOK" becomes active. | ![The customs officer presses the green button](images/139983474187_DV_resource.Stream@PNG-de-DE.png) | Green bar |
| Action "R" resets the associated Effect 3 and the operand "#statBlinkRed" carries Signal 0. | ![The customs officer presses the green button](images/136953779467_DV_resource.Stream@PNG-de-DE.png) | Blue circle with green filling |
| Cause 1 "GetSensors" becomes active once again. | ![The customs officer presses the green button](images/139983474187_DV_resource.Stream@PNG-de-DE.png) | Green bar |
| The action group in column 1 is satisfied again. | ![The customs officer presses the green button](images/136952964107_DV_resource.Stream@PNG-de-DE.png) | Green circle filled with green |
| Effect 1 "RunBeltBerlin" becomes active again. | ![The customs officer presses the green button](images/136953438987_DV_resource.Stream@PNG-de-DE.png) | Green bar |

## Programming causes (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic information on causes (S7-1200, S7-1500)](#basic-information-on-causes-s7-1200-s7-1500)
- [Programming instructions in causes (S7-1200, S7-1500)](#programming-instructions-in-causes-s7-1200-s7-1500)
- [Adding or inverting inputs and outputs at a cause (S7-1200, S7-1500)](#adding-or-inverting-inputs-and-outputs-at-a-cause-s7-1200-s7-1500)
- [Programming timers in causes (S7-1200, S7-1500)](#programming-timers-in-causes-s7-1200-s7-1500)
- [Inserting and editing causes (S7-1200, S7-1500)](#inserting-and-editing-causes-s7-1200-s7-1500)

### Basic information on causes (S7-1200, S7-1500)

When you insert a new CEM function block in your project, it already contains a matrix with a cause and an effect. You can add more causes and effects to the Matrix and edit them.

You can program a maximum of 250 causes and 250 effects in a CEM block.

#### Function of causes

You can query the signal states of one or more operands in a cause and link them with each other logically. In this way, you can formulate a condition that must be fulfilled for the signal state at the output of the cause to be "TRUE". In this case, the cause becomes active and acts on the assigned intersections.

The following figure shows two causes:

- The condition of Cause1 is not fulfilled and the cause is inactive.
- The condition of Cause2 is fulfilled and the cause becomes active.

![Function of causes](images/140207396491_DV_resource.Stream@PNG-de-DE.png)

#### Instructions in causes

You can use various instructions to formulate the condition of a cause. You can use exactly one instruction in each cause. The instructions are divided into the following categories:

- Bit logic operations

  e.g. AND and OR operations or simple assignments
- Comparator operations

  e.g. Compare to greater than, less than or equal to
- Timers

  You can use timers to influence the time of activation or deactivation of a cause.

For a detailed description and programming examples of the individual instructions and timers, refer to the "[Cause instructions](CEM%20%28S7-1200%2C%20S7-1500%29.md#cause-instructions-s7-1200-s7-1500)" section.

#### Structure of a cause

A cause consists of the following elements:

![Structure of a cause](images/138317017355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Cause name |
| ② | Cause number |
| ③ | Operand |
| ④ | Input pin |
| ⑤ | Header of the instruction box |
| ⑥ | Instruction box |
| ⑦ | Timer range |
| ⑧ | Output connection |
| ⑨ | Status bar of the cause |
| ⑩ | Comments area |

#### Interface parameters of causes

The interface of a CEM function block contains a structure for each programmed cause. It contains specific information about the causes that you can query in your program.

The following graphic shows how you can query the interface parameters of a cause. If Cause1 is active, the structure element "Cause1.A" carries signal "1" in the block interface. The signal state is queried in Cause3.

![Interface parameters of causes](images/139986775435_DV_resource.Stream@PNG-de-DE.png)

For a detailed description of the interface parameters, refer to the "Block interface of a CEM program" section.

See also: [Block interface of a CEM program](#block-interface-of-a-cem-program-s7-1200-s7-1500)

#### Steps for programming causes

Basically, you follow these steps to program causes:

| Step | Description | Additional information |
| --- | --- | --- |
| 1 | Insert cause | [Inserting and editing causes](#inserting-and-editing-causes-s7-1200-s7-1500) |
| 2 | Select an instruction and, if needed, define a data type for the instruction | [Programming instructions in causes](#programming-instructions-in-causes-s7-1200-s7-1500) |
| 3 | Connect parameters of the instruction |  |
| 4 | Add more inputs (optional) | [Adding or inverting inputs and outputs](#adding-or-inverting-inputs-and-outputs-at-a-cause-s7-1200-s7-1500) |
| 5 | Invert inputs or outputs of the instruction (optional) |  |
| 6 | Program timers that influence the activation or deactivation of the cause (optional) | [Programming timers in causes](#programming-timers-in-causes-s7-1200-s7-1500) |

### Programming instructions in causes (S7-1200, S7-1500)

Each cause contains a condition that must be fulfilled for the cause to become active.

A newly inserted cause already contains an empty box. There you program the condition in the following steps:

#### Selecting an instruction

To select an instruction for the cause, follow these steps:

1. Position the cursor over the triangle in the top right-hand corner of the empty box.

   A drop-down list is displayed.
2. Select the required instruction in the drop-down list.

   See also: [Cause instructions](CEM%20%28S7-1200%2C%20S7-1500%29.md#cause-instructions-s7-1200-s7-1500)

#### Defining a data type

Some instructions can be executed with several different data types. If you use one of these instructions, three question marks "???" are displayed in the box below the selected instruction.

To define a data type, follow these steps:

1. Click on the question marks "???".

   The drop-down list opens and the data types permitted for the instruction are displayed.
2. Select a data type from the drop-down list.

#### Interconnecting parameters

When inserting a cause, the character string "&lt;??.?&gt;" is inserted at each parameter as placeholder for the operand to be connected. To display the available data types in a tooltip, move the cursor over the placeholder.

To select an operand and interconnect it with the parameter, follow these steps:

1. Click on the placeholder "&lt;??.?&gt;".

   An input field is opened.
2. Enter the corresponding operand, e.g. a PLC tag, a local tag or a constant.

   If you have not yet defined the parameter, select the command "Define tag" from the shortcut menu.

Or drag it from the PLC tag table:

1. Open the "PLC tags" folder in the project tree and select a PLC tag table.
2. Open the detail view.
3. Drag the desired tag from the detail view to the appropriate placeholder "&lt;??.?&gt;".

Or drag it from the block interface:

1. Open the block interface.
2. Drag the desired operands from the block interface to the appropriate placeholder "&lt;??.?&gt;".

---

**See also**

[Basic information on causes (S7-1200, S7-1500)](#basic-information-on-causes-s7-1200-s7-1500)
  
[Inserting and editing causes (S7-1200, S7-1500)](#inserting-and-editing-causes-s7-1200-s7-1500)
  
[Adding or inverting inputs and outputs at a cause (S7-1200, S7-1500)](#adding-or-inverting-inputs-and-outputs-at-a-cause-s7-1200-s7-1500)
  
[Programming timers in causes (S7-1200, S7-1500)](#programming-timers-in-causes-s7-1200-s7-1500)

### Adding or inverting inputs and outputs at a cause (S7-1200, S7-1500)

#### Adding inputs

You can expand some instructions with additional inputs to query and link the signal states of several operands.

The following cause instructions can be expanded:

- AND logic operation
- OR logic operation
- EXCLUSIVE OR logic operation

To do this, follow these steps:

1. Select an existing input.
2. Select the "Add input/output" command in the shortcut menu.

   Or:

   Click on the yellow star symbol beside the last input in the instruction box.

   Or:

   From the "Basic instructions &gt; General" task card, drag the "Insert input/output" instruction to the desired position.

   See also: [Add input/output](CEM%20%28S7-1200%2C%20S7-1500%29.md#add-inputoutput-s7-1200-s7-1500)

#### Inverting inputs and outputs

You also have the option to invert the signal state at an input or output.

To do this, follow these steps:

1. Right-click on an input or output.

   Press the &lt;CTRL&gt; key to select several inputs within a cause.
2. Select the "Invert pin" command in the shortcut menu.

   Or:

   From the "Basic instructions &gt; General" task card, drag the "Invert" instruction to the desired input or output.

   The inversion is represented by a small circle at the input or output.
3. To reverse the inversion, select the "Invert" command again.

   See also: [Invert pin](CEM%20%28S7-1200%2C%20S7-1500%29.md#invert-pin-s7-1200-s7-1500)

#### Example

The following example shows a cause with an AND logic operation, which was extended by an additional input and its output inverted. All three inputs have signal "1". However, because the signal state is inverted at the cause output, the cause does not act via the intersection on the effect.

To simplify matters, the effect has been aligned horizontally in the figure.

![Example](images/139986787083_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Basic information on causes (S7-1200, S7-1500)](#basic-information-on-causes-s7-1200-s7-1500)

### Programming timers in causes (S7-1200, S7-1500)

You can influence the time of activation or deactivation of a cause by programming timers. You can assign exactly one timer to each cause.

#### Example

The example below shows the time "OnDelay". To simplify matters, the effect has been aligned horizontally in the figure.

"OnDelay" delays the activation of Cause1 by the programmed duration of 2 seconds and 3 milliseconds. The timer starts when the condition programmed in the cause is met. Only when the time period has expired, the cause becomes active and acts via the Intersection "N" on the assigned Effect1.

![Example](images/140207826827_DV_resource.Stream@PNG-de-DE.png)

#### Overview of the timers in CEM

The following timers are available in CEM:

| Time | Principle of operation | Additional information |
| --- | --- | --- |
| OnDelay | delays the activation of a cause by the programmed duration | [OnDelay: Delay activation](CEM%20%28S7-1200%2C%20S7-1500%29.md#ondelay-delay-activation-s7-1200-s7-1500) |
| OffDelay | delays the deactivation of a cause by the programmed duration | [OffDelay: Delay deactivation](CEM%20%28S7-1200%2C%20S7-1500%29.md#offdelay-delay-deactivation-s7-1200-s7-1500) |
| Pulse | activates a cause for a defined duration. | [Pulse: Activate for a limited time](CEM%20%28S7-1200%2C%20S7-1500%29.md#pulse-activate-for-a-limited-time-s7-1200-s7-1500) |

#### Programming timers

To program a timer, follow these steps:

1. Select a cause.
2. Double-click on a timer in the "Instructions" task card.

---

**See also**

[Basic information on causes (S7-1200, S7-1500)](#basic-information-on-causes-s7-1200-s7-1500)

### Inserting and editing causes (S7-1200, S7-1500)

#### Select cause

If you select a cause, you automatically select the entire cause line. The cause itself and all its intersections are selected.

To select one or more causes, follow these steps:

1. In the left area of the cause line, click on the gray number of the cause.
2. To select additional causes, click on further cause numbers while holding down the &lt;Ctrl&gt; key.

To select multiple causes within an area, follow these steps:

1. Click on the gray number of the first cause.
2. Hold down the &lt;Shift&gt; key and click on the number of the last cause.

To select all causes of a matrix, follow these steps:

1. Click on a cause.
2. Select the "Edit &gt; Select all" menu command.

#### Add cause at last position

To add a new cause at the last position, follow these steps:

1. Click on the "Add new" button after the last cause.

   The cause is added at the last position.
2. You can enter an optional comment about the new cause and assign a meaningful name.

Or

1. Select a cause.
2. In the "Basic instructions" task card, open the "Cause instructions" folder.
3. Double-click one of the cause instructions in the following categories:

   - Bit logic operation
   - Comparator operations
   - Timers

   The cause is added at the last position and already contains the selected instruction.
4. You can enter an optional comment about the new cause and assign a meaningful name.

Or

1. Select a cause.
2. In the "Basic instructions" task card, open the "General" folder.
3. Double click on the "Empty box" element.
4. The cause is added at the last position.
5. Position the cursor over the triangle in the top right-hand corner of the empty box.

   A drop-down list is displayed.
6. Select an instruction from the list.

#### Add a cause after a selected cause.

To add a new cause after a selected cause, follow these steps:

1. Select the cause after which you want to add a new cause.
2. Select the "Add cause" command from the shortcut menu.

   A new cause is added after the selected cause.

Or

1. Select an element of a cause, for example a comment.
2. In the "Basic instructions" task card, open the "General" folder.
3. Double click on the "Empty box" element.
4. A cause is inserted after the selected element.
5. Position the cursor over the triangle in the top right-hand corner of the empty box.

   A drop-down list is displayed.
6. Select an instruction from the list.

#### Insert cause at any position

To insert a new cause at any position, follow these steps:

1. Open the category "Cause instructions" in the "Basic instructions" task card.
2. Select an instruction and drag it to the desired position in the cause column.

   A new cause is inserted after the selected cause.

#### Rename cause

When you create a new cause, it is given a pre-defined name, for example "Cause1". You can rename the cause to give it a meaningful name.

To rename a cause, follow these steps:

1. Double-click the cause name.
2. Enter a new name.

#### Moving causes

To move causes, follow these steps:

1. Select one or more causes.
2. Drag the causes to the desired position.
3. To move causes into another CEM block, drag them while holding down the &lt;Ctrl&gt; key.

Or

1. Select the "Cut" command in the shortcut menu.
2. Select the cause after which you want to insert the copied causes.
3. Select the "Paste" command in the shortcut menu.

#### Copying causes

To copy causes, follow these steps:

1. Select one or more causes.
2. Hold down the &lt;Ctrl&gt; key and drag the causes to the desired position.
3. To copy the causes into another CEM block, drag the causes without pressing the &lt;Ctrl&gt; key.

Or

1. Select the "Copy" command in the shortcut menu.
2. Select the cause after which you want to insert the copied causes.
3. Select the "Paste" command in the shortcut menu.

#### Deleting causes

To delete causes, follow these steps:

1. Select one or more causes.
2. Select the "Delete" command in the shortcut menu.

A CEM program always contains at least one empty cause. If you select and delete all causes of a program, an empty cause remains which cannot be deleted.

---

**See also**

[Basic information on causes (S7-1200, S7-1500)](#basic-information-on-causes-s7-1200-s7-1500)
  
[Programming instructions in causes (S7-1200, S7-1500)](#programming-instructions-in-causes-s7-1200-s7-1500)

## Programming effects (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic information on effects (S7-1200, S7-1500)](#basic-information-on-effects-s7-1200-s7-1500)
- [Programming instructions in effects (S7-1200, S7-1500)](#programming-instructions-in-effects-s7-1200-s7-1500)
- [Adding or inverting inputs and outputs at an effect (S7-1200, S7-1500)](#adding-or-inverting-inputs-and-outputs-at-an-effect-s7-1200-s7-1500)
- [Inserting and editing effects (S7-1200, S7-1500)](#inserting-and-editing-effects-s7-1200-s7-1500)

### Basic information on effects (S7-1200, S7-1500)

When you insert a new CEM function block in your project, it already contains a matrix with a cause and an effect. You can add more causes and effects to the Matrix and edit them.

You can program a maximum of 250 causes and 250 effects in a CEM block.

#### Function of effects

With the help of effects you can formulate the reaction of the cause-effect matrix to certain process events.

An effect is always assigned to one or more intersection columns. If a process event occurs and ensures that one of the columns becomes active via a cause, the associated effect also becomes active.

Each effect contains an instruction that you program and that is executed when the effect becomes active. The instruction sets the signal states of the interconnected operands to "0" or "1".

The following figure shows two effects:

- "Cause1" is active and acts via the Intersection on "Effect1". The interconnected operand "Gate1" is signal "1"
- "Cause2" is not active. Thus, the assigned "Effect2" is also not active and the interconnected operand "Gate2" is signal "0".

![Function of effects](images/139987029771_DV_resource.Stream@PNG-en-US.png)

#### Instructions in effects

In each effect, you can use exactly one instruction.

The following instructions are available:

- =: Assignment
- S: Set output
- R: Reset output

For a detailed description and programming examples of the individual instructions, refer to the "Effect instructions" section.

See also: [Effect instructions](CEM%20%28S7-1200%2C%20S7-1500%29.md#effect-instructions-s7-1200-s7-1500)

#### Effects with multiple intersection columns

You also have the option of assigning several intersection columns to an effect.

The different columns are linked by a logical OR: When one of the columns becomes active, the assigned effect becomes active as well.

A detailed description and program examples can be found in the section "Programming intersections".

See also: [Linking multiple intersection columns with OR](#linking-multiple-intersection-columns-with-or-s7-1200-s7-1500)

#### Structure of an effect

An effect consists of the following elements:

![Structure of an effect](images/138317824907_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Effect number |
| ② | Comments area |
| ③ | Operand |
| ④ | Output connection |
| ⑤ | Effect name |
| ⑥ | Header of the instruction box |
| ⑦ | Instruction box |
| ⑧ | Input terminal strip |
| ⑨ | Status bar of the effect |

#### Interface parameters of effects

The interface of a CEM function block contains a structure for each programmed effect. It contains specific information on the effects that you can query in your program. However, write access to the parameters is not possible. They are set automatically while the program is running.

The following figure shows how you can query the interface parameters of an effect. If "Effect1" is active, the structure element "# Effect1.A" is signal "1" in the block interface. The signal state is queried in "Cause2" and "Effect2" activated accordingly.

![Interface parameters of effects](images/139987071627_DV_resource.Stream@PNG-en-US.png)

For a detailed description of the interface parameters, refer to the "Block interface of a CEM program" section.

See also: [Block interface of a CEM program](#block-interface-of-a-cem-program-s7-1200-s7-1500)

#### Steps for programming effects

Basically, you follow these steps to program effects:

| Step | Description | Additional information |
| --- | --- | --- |
| 1 | Insert an effect | [Inserting and editing effects](#inserting-and-editing-effects-s7-1200-s7-1500) |
| 2 | Select instruction and interconnect parameters | [Programming instructions in effects](#programming-instructions-in-effects-s7-1200-s7-1500) |
| 3 | Add additional intersection column (optional) | [Link multiple intersections with OR](#linking-multiple-intersection-columns-with-or-s7-1200-s7-1500) |
| 4 | Add inputs (optional) | [Adding or inverting inputs and outputs](#adding-or-inverting-inputs-and-outputs-at-an-effect-s7-1200-s7-1500) |
| 5 | Invert inputs or outputs of the instruction (optional) |  |

---

**See also**

[Programming intersections (S7-1200, S7-1500)](#programming-intersections-s7-1200-s7-1500)

### Programming instructions in effects (S7-1200, S7-1500)

Each effect contains an instruction that you program and that is executed when the effect becomes active. The instruction sets the signal states of the interconnected operands to "0" or "1".

A newly inserted effect already contains an empty box. You program the instruction there with the following steps:

#### Selecting an instruction

To select an instruction for the effect, follow these steps:

1. Position the cursor over the triangle in the top right-hand corner of the empty box.

   A drop-down list is displayed.
2. Select the required instruction in the drop-down list.

   See also: [Effect instructions](CEM%20%28S7-1200%2C%20S7-1500%29.md#effect-instructions-s7-1200-s7-1500)

#### Interconnecting parameters

When inserting an effect, the character string "&lt;??.?&gt;" is inserted at each parameter as a placeholder for the operand to be connected.

To select an operand and interconnect it with the parameter, follow these steps:

1. Click on the placeholder "&lt;??.?&gt;".

   An input field is opened.
2. Enter the corresponding operand, for example a PLC tag or a local tag.

   If you have not yet defined the parameter, select the command "Define tag" from the shortcut menu.

Or drag it from the PLC tag table:

1. Open the "PLC tags" folder in the project tree and select a PLC tag table.
2. Open the detail view.
3. Drag the desired tag from the detail view to the appropriate placeholder "&lt;??.?&gt;".

Or drag it from the block interface:

1. Open the block interface.
2. Drag the desired operands from the block interface to the appropriate placeholder "&lt;??.?&gt;".

### Adding or inverting inputs and outputs at an effect (S7-1200, S7-1500)

#### Adding inputs

If you insert an additional input to an effect, a new intersection column is created for the effect.

To do this, follow these steps:

1. Right-click on an effect.
2. Select the "Add intersection column" command in the shortcut menu.

Or:

1. Click on the yellow star symbol beside the last input in the instruction box.

   See also: [Linking multiple intersection columns with OR](#linking-multiple-intersection-columns-with-or-s7-1200-s7-1500)

#### Adding outputs

You may extend instructions by additional outputs to set or reset several operands.

To do this, follow these steps:

1. Right-click on an effect.
2. Select the "Add output" command from the shortcut menu.

Or:

1. Click on the yellow star symbol beside the last output of the instruction box.

   See also: [Add input/output](CEM%20%28S7-1200%2C%20S7-1500%29.md#add-inputoutput-s7-1200-s7-1500)

#### Inverting inputs and outputs

To invert the signal state at an input or output, follow these steps:

1. Right-click on an input or output.

   Press the &lt;CTRL&gt; key to select multiple outputs within an effect.
2. Select the "Invert pin" command in the shortcut menu.

   Or:

   From the "Basic instructions &gt; General" task card, drag the "Invert pin" instruction to the desired input or output.

   The inversion is represented by a small circle at the input or output.
3. To reverse the inversion, select the "Invert pin" command again.

   See also: [Invert pin](CEM%20%28S7-1200%2C%20S7-1500%29.md#invert-pin-s7-1200-s7-1500)

#### Example

The following example shows an effect with two outputs. One of the outputs has been inverted. The active effect sets "Gate1" to "0" and "Gate2" to "1".

To simplify matters, the effect has been aligned horizontally in the figure.

![Example](images/140010501131_DV_resource.Stream@PNG-de-DE.png)

### Inserting and editing effects (S7-1200, S7-1500)

#### Selecting effects

When you select an effect, you automatically also select the intersection columns assigned to it.

To select one or more effects, follow these steps:

1. Click on the gray number of the effect in the upper part of the effect column.
2. To select additional effects, click on more effect numbers while holding down the &lt;Ctrl&gt; key.

To select multiple effects within an area, follow these steps:

1. Click on the gray number of the first effect.
2. Hold down the &lt;Shift&gt; key and click on the number of the last effect.

To select all effects of a matrix, follow these steps:

1. Click on an effect.
2. Select the "Edit &gt; Select all" menu command.

To select a single intersection column, follow these steps:

1. In the grey bar below the effect, click on the area above the relevant intersection column.

#### Inserting effect at last position

To insert a new effect in the last position, follow these steps:

1. Click on the "Add new" button after the last effect.

   The effect is inserted at the last position.
2. Optionally, enter a comment for the new effect and assign a meaningful name.

Or

1. In the "Basic instructions" task card, open the "Effect instructions" folder.

   Double-click on an effect instruction, for example "Assignment".

   The effect is inserted at the last position and already contains the selected instruction.
2. Optionally, enter a comment for the new effect and assign a unique name.

Or

1. Select an effect.
2. In the "Basic instructions" task card, open the "General" folder.
3. Double click on the "Empty box" element.
4. The effect is added at the last position.
5. Position the cursor over the triangle in the top right-hand corner of the empty box.

   A drop-down list is displayed.
6. Select an instruction from the list.

#### Inserting effect after a selected effect

To insert a new effect after a selected effect, follow these steps:

1. Select the effect after which you want to insert a new effect.
2. Select the "Insert effect" command in the shortcut menu.

   A new effect is inserted after the selected effect.

Or

1. Select an element of an effect, for example a comment.
2. In the "Basic instructions" task card, open the "General" folder.
3. Double click on the "Empty box" element.
4. An effect is inserted after the selected element.
5. Position the cursor over the triangle in the top right-hand corner of the empty box.

   A drop-down list is displayed.
6. Select an instruction from the list.

#### Insert effect at any position

To insert a new effect at any position, follow these steps:

1. Open the category "Effect instructions" in the "Basic instructions" task card.
2. Select an instruction and drag it to the desired position in the effect line.

   A new effect is inserted after the selected effect.

#### Renaming effect

To rename an effect, follow these steps:

1. Double-click the effect name.
2. Enter a new name.

#### Moving effects

To move effects, follow these steps:

1. Select one or more effects.
2. Drag the effects to the desired position.
3. To move effects into another CEM block, drag them while holding down the &lt;Ctrl&gt; key.

Or

1. Select the "Cut" command in the shortcut menu.
2. Select the effect after which you want to insert the copied effect.
3. Select the "Paste" command in the shortcut menu.

#### Copying effects

To copy effects, follow these steps:

1. Select one or more effects.
2. Hold down the &lt;Ctrl&gt; key and drag the effects to the desired position.
3. To copy the effects into another CEM block, drag the effects without pressing the &lt;Ctrl&gt; key.

Or

1. Select the "Copy" command in the shortcut menu.
2. Select the effect after which you want to insert the copied effects.
3. Select the "Paste" command in the shortcut menu.

#### Deleting effects

To delete effects, follow these steps:

1. Select one or more effects.
2. Select the "Delete" command in the shortcut menu.

A CEM program always contains at least one empty effect. If you select and delete all effects of a program, an empty effect remains which cannot be deleted.

---

**See also**

[Basic information on effects (S7-1200, S7-1500)](#basic-information-on-effects-s7-1200-s7-1500)
  
[Programming instructions in effects (S7-1200, S7-1500)](#programming-instructions-in-effects-s7-1200-s7-1500)

## Programming intersections (S7-1200, S7-1500)

This section contains information on the following topics:

- [Basic information on intersections (S7-1200, S7-1500)](#basic-information-on-intersections-s7-1200-s7-1500)
- [Priority rules for actions in intersections (S7-1200, S7-1500)](#priority-rules-for-actions-in-intersections-s7-1200-s7-1500)
- [Action groups in intersections (S7-1200, S7-1500)](#action-groups-in-intersections-s7-1200-s7-1500)
- [Programming actions and action groups (S7-1200, S7-1500)](#programming-actions-and-action-groups-s7-1200-s7-1500)
- [Editing and moving intersections (S7-1200, S7-1500)](#editing-and-moving-intersections-s7-1200-s7-1500)
- [Linking multiple intersection columns with OR (S7-1200, S7-1500)](#linking-multiple-intersection-columns-with-or-s7-1200-s7-1500)
- [Editing and moving intersection columns (S7-1200, S7-1500)](#editing-and-moving-intersection-columns-s7-1200-s7-1500)

### Basic information on intersections (S7-1200, S7-1500)

#### Function of intersections

"Intersections" are the points that connect the causes and effects of a cause-effect matrix with one another. They specify which causes have an effect on the respective effects.

#### Actions in intersections

You program an action in each intersection. When the intersection becomes active, this action is applied to the effect.

You can program the following actions in intersections:

| Action | Description |
| --- | --- |
| ![Actions in intersections](images/138323448715_DV_resource.Stream@PNG-de-DE.png) | As long as the intersection is active, the signal state at the input of the effect is "1". |
| ![Actions in intersections](images/138324275595_DV_resource.Stream@PNG-de-DE.png) | The signal state at the input of the effect is set retentively to "1". |
| ![Actions in intersections](images/138324283275_DV_resource.Stream@PNG-de-DE.png) | The signal state at the input of the effect is reset retentively to "0". |

#### Priority rules for actions

If multiple actions are defined in one intersection column, the result of the entire column is calculated according to priority rules.

See also: [Priority rules for actions in intersections](#priority-rules-for-actions-in-intersections-s7-1200-s7-1500)

#### Action groups

You can group multiple actions in one intersection column to program logical operations. For example, you can create an "AND" logic operation or a "2 out of 3 logic operation".

See also: [Action groups in intersections](#action-groups-in-intersections-s7-1200-s7-1500)

#### Example: OR logic operation

The following example shows you how to link two causes with OR. The intersection action is executed when "Cause1" or "Cause2" is active.

For comparison, the same program is displayed in FBD representation:

![Example: OR logic operation](images/138321817483_DV_resource.Stream@PNG-de-DE.png)

#### Example: AND logic operation

The following example shows you how to link two causes with AND. The intersection action is executed when "Cause1" and "Cause2" are active.

For comparison, the same program is displayed in FBD representation:

![Example: AND logic operation](images/138321825163_DV_resource.Stream@PNG-de-DE.png)

#### Example: 2 out of 3 logic operation

The following example shows you how to link three causes with "2 out of 3 logic operation". The intersection action is executed when two of the three causes are active.

For comparison, the same program is displayed in FBD representation.

![Example: 2 out of 3 logic operation](images/138491047051_DV_resource.Stream@PNG-de-DE.PNG)

---

**See also**

[Programming actions and action groups (S7-1200, S7-1500)](#programming-actions-and-action-groups-s7-1200-s7-1500)
  
[Examples of program status display in CEM (S7-1200, S7-1500)](Testing%20CEM%20programs%20%28S7-1200%2C%20S7-1500%29.md#examples-of-program-status-display-in-cem-s7-1200-s7-1500)

### Priority rules for actions in intersections (S7-1200, S7-1500)

#### Description

The actions in intersections have different priorities according to which the result of the Intersection column is calculated:

The following table shows the priorities:

| Action | Value | Description |
| --- | --- | --- |
| ![Description](images/138324275595_DV_resource.Stream@PNG-de-DE.png) | true | Sets the input of the effect permanently to Signal 1. |
| false | Has no effect on the signal. |  |
| ![Description](images/138323448715_DV_resource.Stream@PNG-de-DE.png) | true | Sets the input of the effect to Signal 1. |
| false | Sets the signal to 0 if it is not set by an S. |  |
| ![Description](images/138324283275_DV_resource.Stream@PNG-de-DE.png) | true | Sets the input of the effect permanently to Signal 0 if this is not set to 1 by an S or an N. |
| false | Has no effect on the signal. |  |

---

**See also**

[Examples of program status display in CEM (S7-1200, S7-1500)](Testing%20CEM%20programs%20%28S7-1200%2C%20S7-1500%29.md#examples-of-program-status-display-in-cem-s7-1200-s7-1500)

### Action groups in intersections (S7-1200, S7-1500)

#### Description

An action group combines multiple intersections of a column. It is defined by the following elements:

- An action (S, R or N)
- a number

The number indicates how many intersections from the group must be active for the result of the action group to be "true".

All intersections that have the same combination of action and number form an action group. An action group can, for example, consist of three intersections with the specification "2N". This means that two of the three intersections must be active for the result of the group to be "true".

A column can also contain multiple action groups of different type.

#### Examples

The following example shows an action group of the type "2N". This means that two of the four causes must be active for the result of the action group to be "true".

![Examples](images/138323228555_DV_resource.Stream@PNG-de-DE.png)

The following example shows a column with the two action groups "2N" and "2S". This means that either two causes of the action group "2N" or two causes of the action group "2S" must be active for the overall result of the column to be "true". When both conditions are met at the same time, the priority rules for actions apply.

![Examples](images/138323236235_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Programming actions and action groups (S7-1200, S7-1500)](#programming-actions-and-action-groups-s7-1200-s7-1500)
  
[Priority rules for actions in intersections (S7-1200, S7-1500)](#priority-rules-for-actions-in-intersections-s7-1200-s7-1500)
  
[Linking multiple intersection columns with OR (S7-1200, S7-1500)](#linking-multiple-intersection-columns-with-or-s7-1200-s7-1500)

### Programming actions and action groups (S7-1200, S7-1500)

#### Programming actions

The easiest way to program actions is by using the keyboard. To do this, follow these steps:

1. Select an intersection.
2. Enter the action you want on the keyboard (N, S or R).

#### Programming action groups using the keyboard

You can also enter action groups using the keyboard. To do this, follow these steps:

1. Select an intersection.
2. Enter the desired action group on the keyboard (for example, 2N, 3S or 4R).
3. Add additional intersections to the group by entering the same identification (z. B. 2N, 3S, 4R).
4. Add as many intersections as you need to reach the required minimum number.

   Example: At least two intersections are required for a "2N" group.

#### Programming action groups using the action dialog

You can use the action dialog to support you when programming action groups. To program an action group using the action dialog, follow these steps:

1. Double-click an intersection.

   The action dialog is opened.
2. From the "Select intersection action" selection list, select the action you want (N, S or R).
3. You now have two options:

   - To add the action to an existing group, select the desired action group in the "Select action group" selection list.
   - To create a new action group, select the item "New action group" in the "Select action group" selection list. Then enter the number of intersections in the "Configure action group" input field that have to be satisfied for the action group to be satisfied.
4. The "out of" field shows how many elements are currently included in the action group.

   If the minimum number of required elements has not been reached yet, the required minimum number is displayed.

---

**See also**

[Basic information on intersections (S7-1200, S7-1500)](#basic-information-on-intersections-s7-1200-s7-1500)
  
[Action groups in intersections (S7-1200, S7-1500)](#action-groups-in-intersections-s7-1200-s7-1500)

### Editing and moving intersections (S7-1200, S7-1500)

#### Selecting intersection

To select an intersection, follow these steps:

1. Click on an intersection.
2. To select additional intersections, click on additional intersections while holding down the &lt;Ctrl&gt; key or use the lasso function.

To select multiple intersections within an area, follow these steps:

1. Click on the first intersection.
2. Hold down the &lt;Shift&gt; key and click on the last intersection.

To select all intersections of a matrix, follow these steps:

1. Click on an intersection.
2. Select the "Edit &gt; Select all" menu command.

#### Moving intersection

To move intersections, follow these steps:

1. Select one or more contiguous intersections.
2. Click on an action in one of the selected intersections and hold down the mouse button.
3. Drag the intersections to the desired position.

   If you drag the intersections onto existing intersections, they will be overwritten.

   If you drag the intersections outside of the intersection area, they will be deleted.

#### Copying intersection

To copy intersections, follow these steps:

1. Select one or more contiguous intersections.
2. Click on an action in one of the selected intersections and hold down the mouse button.
3. Hold down the &lt;Ctrl&gt; key and drag the intersections to the desired position.

   If you drag the intersections onto existing intersections, they will be overwritten.

   If you drag the intersections outside of the intersection area, they will be deleted.

#### Deleting intersection

To delete intersections, follow these steps:

1. Select one or more intersections.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Editing and moving intersection columns (S7-1200, S7-1500)](#editing-and-moving-intersection-columns-s7-1200-s7-1500)

### Linking multiple intersection columns with OR (S7-1200, S7-1500)

You can assign several intersection columns to an effect. All intersection columns of an effect are linked by a logical OR. When one of the columns becomes active, the input of the effect is signal "1".

A maximum of five intersection columns can be assigned to an effect.

#### Action groups in different intersection columns

You can define action groups in each intersection column. All groups are evaluated column by column. This applies to action groups of all action types ("N", "S" and "R").

The figure below shows an effect with two intersection columns. The two actions "2N" in the first column form an action group. This is indicated in the figure by the blue rectangle. The two actions "2N" in the second column form a second action group, which is shown by the green rectangle.

Both action groups are linked by a logical OR. "Effect1" becomes active if either the action group "2N" in the first column OR the action group "2N" in the second column becomes active. The order of the columns does not matter during the evaluation.

![Action groups in different intersection columns](images/138324819083_DV_resource.Stream@PNG-en-US.png)

The following figure shows the example in online layout.

"Button1" and "Sensor1" have signal "1". The action group in the first column becomes active and sets the input of the effect to signal "1".

The action group in the second column is not active because "Button2" is not set. However, this does not affect the effect because it is set by the first column.

![Action groups in different intersection columns](images/140010901259_DV_resource.Stream@PNG-en-US.png)

#### Actions "S" and "R" in different intersection columns

The actions "S" and "R" are always used in pairs. If you use several intersection columns at an effect, the two actions "S" and "R" do not have to be in the same column, but can be distributed over different columns.

The figure below shows an example. "Effect1" is set to active and the output "openGate1" is set permanently if the conditions in "Cause1" and "Cause3" are fulfilled. If the conditions are no longer fulfilled, the "openGate1" output is still set. "openGate1" is reset again if one of the two conditions is no longer fulfilled and, in addition, "Cause2" is fulfilled.

![Actions "S" and "R" in different intersection columns](images/138325101579_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Editing and moving intersection columns (S7-1200, S7-1500)](#editing-and-moving-intersection-columns-s7-1200-s7-1500)
  
[Action groups in intersections (S7-1200, S7-1500)](#action-groups-in-intersections-s7-1200-s7-1500)

### Editing and moving intersection columns (S7-1200, S7-1500)

#### Adding an intersection column at last position

To insert a new intersection column in the last position, follow these steps:

1. Right-click on the instruction box in the effect.
2. Select the "Add intersection column" command in the shortcut menu.

   If the effect already contains the maximum number of five columns, the menu command is grayed out.

Or:

1. Click on the yellow star icon in the lower right corner of the instruction box.

   A new intersection column is added at the last position. If the effect already contains the maximum number of five columns, the star symbol is not displayed.

   ![Adding an intersection column at last position](images/135524519435_DV_resource.Stream@PNG-de-DE.png)

   ![Adding an intersection column at last position](images/135524519435_DV_resource.Stream@PNG-de-DE.png)

#### Inserting intersection column after a selected column or intersection

To insert a new intersection column after a selected column, follow these steps:

1. Select the column or intersection after which you want to insert a new column.
2. Select the "Add intersection column" command in the shortcut menu.

   A new intersection column is inserted after the selected column. If the effect already contains the maximum number of five columns, the menu command is grayed out.

#### Selecting intersection columns

To select an intersection column, follow these steps:

1. In the status bar of the effect, click the area above the relevant intersection column.
2. To select additional intersection columns, click on the areas above other columns while holding down the &lt;Ctrl&gt; key.

   ![Selecting intersection columns](images/135563977611_DV_resource.Stream@PNG-de-DE.png)

   ![Selecting intersection columns](images/135563977611_DV_resource.Stream@PNG-de-DE.png)

#### Moving intersection columns

To move an intersection column within an effect or to another effect, follow these steps:

1. Select the column.
2. Drag the column to the desired position.

   The column is inserted behind the column above which you drop it.

#### Copying intersection columns

To copy an intersection column, follow these steps:

1. Select the column.
2. Hold down the &lt;Ctrl&gt; key and drag the column to the desired position.

   The column is inserted behind the column above which you drop it.

#### Deleting intersection columns

To delete an intersection column, follow these steps:

1. Select the column.
2. Select the "Delete" command in the shortcut menu.

---

**See also**

[Linking multiple intersection columns with OR (S7-1200, S7-1500)](#linking-multiple-intersection-columns-with-or-s7-1200-s7-1500)
  
[Editing and moving intersections (S7-1200, S7-1500)](#editing-and-moving-intersections-s7-1200-s7-1500)
  
[Action groups in intersections (S7-1200, S7-1500)](#action-groups-in-intersections-s7-1200-s7-1500)

## Block interface of a CEM program (S7-1200, S7-1500)

This section contains information on the following topics:

- [Overview of a CEM block interface (S7-1200, S7-1500)](#overview-of-a-cem-block-interface-s7-1200-s7-1500)

### Overview of a CEM block interface (S7-1200, S7-1500)

#### Overview

The interface of a CEM function block contains a structure for each programmed cause and effect. The structure contains specific information on the causes and effects that you can query in your program. Write access to the interface parameters is not possible.

A program example for the use of an interface parameter is provided in the section "[Basic information on causes](#basic-information-on-causes-s7-1200-s7-1500)".

#### Static parameters of a cause

The following table shows the parameters that are created for each cause of the CEM function block in the "Static" section of the block interface:

| Component | Description | Data type |
| --- | --- | --- |
| A | Cause is active. | BOOL |
| A0 | Cause was deactivated. | BOOL |
| A1 | Cause was activated | BOOL |
| AF | Cause instruction is active. | BOOL |
| AT | Timer function is active. | BOOL |
| T | Active time of the cause since last activation. | TIME |
| PT | Programmed period of the timer function | TIME |
| ET | Elapsed time of the timer function | TIME |
| IM | System internal | DWORD |

#### Static parameters of an effect

The following table shows the parameters that are created for each effect of the CEM function block in the "Static" section of the block interface:

| Component | Description | Data type |
| --- | --- | --- |
| A | Effect is active. | BOOL |
| A0 | Effect was deactivated. | BOOL |
| A1 | Effect was activated | BOOL |
| T | Active time of the effect since last activation. | TIME |
| Q | RS flip-flop bit memory of the intersections of the effect is active. | BOOL |
| IM | System internal | DWORD |

#### Activation of parameters A, A1 and A0

The following figure gives an overview of the behavior of parameters A, A0 and A1 using a cause as example. The behavior of the effect parameters A, A0 and A1 is identical.

![Activation of parameters A, A1 and A0](images/140482471691_DV_resource.Stream@PNG-de-DE.png)

| Parameters | Description |
| --- | --- |
| A | The "A" parameter is active as long as the assigned cause or effect. |
| A1 | The "A1" parameter carries out an edge evaluation:   - If the cause or effect was deactivated in the current cycle, "A1" is signal "1". - At the time of the next evaluation of the cause or effect in the following cycle, "A1" is reset to "0". |
| A0 | The "A0" parameter also carries out an edge evaluation:   - If the cause or effect was disabled in the current cycle, "A0" is signal "1". - At the time of the next evaluation of the cause or effect in the following cycle, "A0" is reset to "0". |
