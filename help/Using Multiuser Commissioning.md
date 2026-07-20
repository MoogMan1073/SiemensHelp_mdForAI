---
title: "Using Multiuser Commissioning"
package: PEMuComenUS
topics: 10
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using Multiuser Commissioning

This section contains information on the following topics:

- [Introduction to Multiuser Commissioning](#introduction-to-multiuser-commissioning)
- [Overview of the general mode of operation with Multiuser Commissioning](#overview-of-the-general-mode-of-operation-with-multiuser-commissioning)
- [Settings for working with Multiuser Commissioning](#settings-for-working-with-multiuser-commissioning)
- [Requirements for working with Multiuser Commissioning](#requirements-for-working-with-multiuser-commissioning)
- [Enabling and disabling commissioning mode](#enabling-and-disabling-commissioning-mode)
- [Working with synchronous commissioning](#working-with-synchronous-commissioning)
- [Working with asynchronous commissioning](#working-with-asynchronous-commissioning)
- [Important notes on working with asynchronous commissioning](#important-notes-on-working-with-asynchronous-commissioning)
- [Functionality of the commissioning editor](#functionality-of-the-commissioning-editor)

## Introduction to Multiuser Commissioning

### Introduction

In the TIA Portal , you have the option of working with Multiuser Commissioning in the commissioning phase as part of the "Multiuser Engineering" product.

After you have created and edited multiuser projects with multiple users in Multiuser Engineering , commissioning can be executed just as conveniently and also in the team with Multiuser Commissioning .

This approach significantly reduces the commissioning times for your projects. You can use your plant faster and start production sooner.

As of V16, Multiuser Commissioning is available to you in "synchronous mode" and in "asynchronous mode".

The same requirements and rules apply to multiuser commissioning as they do for multiuser engineering. This means you cannot make changes to the hardware configuration and to objects that are not supported in commissioning mode.

### Switching on commissioning mode

For commissioning mode to be active, it needs to be switched on in the Administration Tool .

Synchronous commissioning is started as default setting when commissioning mode is switched on in the Administration Tool.

For more details, see: [Enabling and disabling commissioning mode](#enabling-and-disabling-commissioning-mode)

You switch between synchronous and asynchronous commissioning in the TIA Portal settings (Options > Settings > Multiuser > Commissioning settings) or by clicking the corresponding button in the project tree.

For the current session, you can switch using the button in the project tree. However, this switch only remains active until the session is closed. When the local session is opened again, the default setting from the TIA Portal settings will be used once more.

### Multiuser Commissioning in synchronous mode

In synchronous mode, you work with Multiuser Commissioning as before. This setting is the default.

- Working in synchronous mode enables you to download the device in a convenient manner. Your local session is updated automatically after download.
- You cannot perform any other activities in the TIA Portal until download to the device is complete.

You can find more notes on working in synchronous mode in the section [Working with synchronous commissioning](#working-with-synchronous-commissioning).

### Multiuser Commissioning in asynchronous mode

In asynchronous commissioning, a second instance of the TIA Portal runs in the background.

- The times for download to the device are significantly reduced in asynchronous mode.
- As a user, you are only informed if decisions and actions are required for download to the device. If no user decisions are required, download to the device takes place asynchronously in the background.
- If errors occur during compiling or downloading and user decisions are required, this is displayed in the Multiuser Commissioning editor.
- Your local session is **not** updated automatically after download.

You can find more notes on working in asynchronous mode in the section [Working with asynchronous commissioning](#working-with-asynchronous-commissioning).

---

**See also**

[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)
  
[Working with asynchronous commissioning](#working-with-asynchronous-commissioning)
  
[Working with synchronous commissioning](#working-with-synchronous-commissioning)
  
[Enabling and disabling commissioning mode](#enabling-and-disabling-commissioning-mode)

## Overview of the general mode of operation with Multiuser Commissioning

### Introduction

If you want to work with multiple users simultaneously in multiuser projects during the commissioning phase, specific procedures should be observed.

Below you will find an overview of the general mode of operation with Multiuser Commissioning.

### Requirements for working with Multiuser Commissioning

You have already executed the following steps with Multiuser Engineering in the engineering phase:

1. Install a project server.
2. Create a suitable server project on the project server.
3. Create local sessions for all users.
4. Create the automation task step-by-step in the different local versions and check in all changes to the server project.
5. Update the local sessions with the server project.
6. Continue operation step-by-step until the server project is ready for commissioning and the engineering phase can be completed.
7. Before you start commissioning, the project must be loaded from the server view to the device.
8. The local sessions must be updated before you start commissioning.
9. Start multiuser commissioning using the administration tool by clicking on "Commissioning mode".
10. You can switch between synchronous and asynchronous commissioning by clicking on the "Commissioning mode" button in the user interface of TIA Portal.

> **Note**
>
> **Checking-in in commissioning mode**
>
> Avoid checking in data **manually** in commissioning mode because these changes will interrupt continuous working in commissioning mode.
>
> All changes from the local sessions are compiled and checked in to the server project during loading.

### Working with Multiuser Commissioning

Please observe the following notes for working in server projects:

- Before they can be used in the commissioning phase with Multiuser Commissioning , the projects should have already been edited with Multiuser Engineering and contain the entire hardware configuration, the required blocks, connections and global settings.

  For more information on this topic, refer to: [Requirements for server projects](Using%20Multiuser%20Engineering.md#requirements-for-server-projects)
- Avoid working on the same objects simultaneously by consulting beforehand with the other users.
- All global settings, such as changes within the device configuration, must be made in the server project view (i.e. in the central server project).
- All objects of a multiuser project can be edited in the server project view. You can also edit objects that do not support the Multiuser Engineering functionality.
- All changes checked into the server project from the local sessions must be compiled to always keep a consistent version on the server project.
- After download to the CPU, the server project is automatically updated. A new revision of the server project is created after each download.

### Overview of the mode of operation with Multiuser Commissioning

To use the Multiuser Commissioning functionality, carry out the following steps:

| Action | Example |
| --- | --- |
|  |  |
| **1. Processing in the engineering phase is completed**     The processing of the various configuration tasks in the local sessions has been completed.     **Result:**   All changes have been compiled and are checked in to the server project.  The local sessions and the server project are synchronized.  There are no more markings in the local sessions.  The server project was downloaded to the CPU. This means the version of the server project and the version of the multiuser project on the CPU are consistent.     **Note**:  This completes the engineering phase. | ![Overview of the mode of operation with Multiuser Commissioning](images/124904488203_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **2. Working in the commissioning phase**     You now switch to "Commissioning mode" in the Administration Tool and start with the commissioning phase.  The procedure is as follows:  - You edit the local session in commissioning mode as usual. - As of TIA Portal V16, you have the option to choose between synchronous and asynchronous commissioning mode. The procedure for synchronous commissioning mode is described below. - During download, all changes from the local sessions are compiled and checked into the server project. - The server project and, in synchronous commissioning mode, also the local session are updated automatically after each download to the CPU. Changes made by other users will then become visible in the local session. - A new revision of the server project is created after each download to the CPU. - Continue working in commissioning mode until commissioning is complete. - If required, you can export the server project as single-user project and continue editing and managing it as usual in the TIA Portal.      **Result:**   It is ensured in commissioning mode that the online project in the CPU and the offline project in the project server are consistent. This makes for easier commissioning because there is no need for synchronization.  However, if desired, inconsistencies can be permitted, for example when you check into the server project directly from the local session without downloading beforehand. | ![Overview of the mode of operation with Multiuser Commissioning](images/124907850123_DV_resource.Stream@PNG-en-US.png) |

### Advantages of working with Multiuser Commissioning

By downloading a project version that is always synchronized in the server project as well as on the CPU and is therefore consistent, fewer errors are forwarded to other users.

By working on different objects, such as different tags, blocks, PLC tags, interrupts, screens, text and graphic lists, technology objects etc., on one or multiple devices within a multiuser project at the same time, you can make your commissioning times more effective and reduce them significantly.

---

**See also**

[Requirements for server projects](Using%20Multiuser%20Engineering.md#requirements-for-server-projects)

## Settings for working with Multiuser Commissioning

### Introduction

The general settings for Multiuser Engineering also apply to working with Multiuser Commissioning . You can make the following settings in the TIA Portal under "Options > Settings" in the "Multiuser" tab:

- General
- Searching in the project
- Compilation settings
- Commissioning settings

As of TIA Portal V16, you can make the following settings for Multiuser Commissioning in the TIA Portal under "Options > Settings" in the "Commissioning" tab:

- Running Multiuser Commissioning in synchronous mode

  For more details, see: [Working with synchronous commissioning](#working-with-synchronous-commissioning)
- Running Multiuser Commissioning in asynchronous mode

  For more details, see: [Working with asynchronous commissioning](#working-with-asynchronous-commissioning)

### Activating Multiuser Commissioning

You can choose between engineering mode and commissioning mode when working with Multiuser Engineering .

The setting is made in the Administration Tool.

For more details, see: [Managing the project server with the graphic Administration Tool](Working%20with%20the%20TIA%20Project-Server.md#managing-the-project-server-with-the-graphic-administration-tool)

Open the Administration Tool and add the server you are using.

Select the required server project.

The "Multiuser Commissioning" button has been added to the Administration Tool toolbar.

As soon as this button is pressed, you switch to commissioning mode. The symbol for commissioning mode is also displayed in the TIA Portal project tree as overlay symbol in front of the project name.

![Activating Multiuser Commissioning](images/115233591051_DV_resource.Stream@PNG-en-US.png)

In commissioning mode, the server project is always updated after download to the CPU.

The changes from the local sessions are compiled before they are downloaded to the CPU. If the download process is successful, the changes are transferred to the server project. A new revision is then created on the project server each time and - in synchronous mode - the local session is updated.

If you are working in asynchronous mode, it is advisable to synchronize the local session manually from time to time so that you are always working with an up-to-date version of the server project.

If the project server is not reachable, you receive a corresponding error message and commissioning mode is closed.

In this case you can download directly to the CPU from the local session in engineering mode and transfer your changes to the server project once the connection to the server has been established again.

### Exiting commissioning mode

You exit commissioning mode again by deactivating the "Multiuser Commissioning" button.

Click on the Commissioning mode button again to deactivate it. The deactivated Commissioning mode button means the engineering mode is active.

The small overlay symbol in front of the project name is no longer displayed in engineering mode.

### Automatic interruption of commissioning mode

Commissioning mode is automatically interrupted in the following cases:

- Whenever errors occur during compilation of the changes.
- Whenever errors occur during subsequent download to the CPU.
- Whenever errors occur during the transfer of changes downloaded to the CPU to the server project.
- Whenever network interrupts occur.
- When working offline, when you are working without being connected to the server project in the local session.
- When the server project is locked by another user.

Whenever errors occur you receive an error message with information on the type of error and possible remedy.

---

**See also**

[Settings for working with Multiuser Engineering](Using%20Multiuser%20Engineering.md#settings-for-working-with-multiuser-engineering)
  
[Working with synchronous commissioning](#working-with-synchronous-commissioning)
  
[Working with asynchronous commissioning](#working-with-asynchronous-commissioning)

## Requirements for working with Multiuser Commissioning

### Introduction

If you are commissioning a project with Multiuser Commissioning as part of a team, it is very important for successful cooperation that all editors of the project be familiar with the following rules.

### Setting the commissioning mode

Commissioning mode is set in the Administration Tool.

The setting is usually made by the administrator and applies to all existing local sessions of a server project.

This means that either all local sessions are working in engineering mode or all local sessions are working in commissioning mode.

For more details, see: [Enabling and disabling commissioning mode](#enabling-and-disabling-commissioning-mode)

### Project server: Reachability in commissioning mode

As soon as you start downloading to the CPU in commissioning mode , an attempt is made to establish a connection to the multiuser server to update the local session in the project server as well.

If the project server is not reachable at this time, a dialog with a corresponding message opens.

The dialog that opens offers the following options:

- Attempt to reconnect to the project server
- Work offline, thus without the project server being connected:

  Switch to engineering mode and load from the local session to the CPU without updating the server project.
- Cancel the action

Each option opens an additional dialog with more options for selection and cancellation.

**Asynchronous commissioning: Limitations for S7-1200 / S7-1500 H**

If you are working in commissioning mode, only limited use of asynchronous commissioning is possible for the following CPUs:

- S7-1200
- S7-1500 H in redundant mode

These CPUs can have only one online connection to the TIA Portal. Simultaneous online connections to multiple instances of the TIA Portal are not possible.

When working in asynchronous commissioning, an attempt is made to open a second TIA Portal instance in addition to the active online connection to the CPU. Since the CPU supports only one connection, the action is aborted with an error message.

This results in the following rule:

- As long as you are not connected online with your CPU in TIA Portal, you can work with asynchronous commissioning.

  In order to work with asynchronous commissioning, disconnect any existing online connections.
- With an S7-1500 H-CPU, you can only work in asynchronous commissioning mode as long as redundancy is deactivated.
- To establish an online connection to the CPU in the TIA Portal, switch from asynchronous commissioning mode to synchronous commissioning mode.

### Automatic interruption of commissioning mode

Commissioning mode is automatically interrupted by the system in the following cases:

- Whenever errors occur during the transfer of changes to the server project.
- Whenever errors occur during compilation of the changes.
- Whenever network interrupts occur.
- Whenever errors occur during download to the CPU.
- When working offline, when you are working in the local session without being connected to the server project.
- When the server project is locked by another editor.

Whenever errors occur you receive an error message with information on the type of error and possible solution.

## Enabling and disabling commissioning mode

### Introduction

As of TIA Portal V15.1, you can switch between "Engineering mode" and "Commissioning mode" when working with Multiuser Engineering .

The default setting is engineering mode.

The same requirements apply for working in "commissioning mode" as for working in "engineering mode".

In "engineering mode" , you edit your multiuser projects as usual and configure your automation tasks at the same time in the different local sessions.

As soon as your multiuser project is ready for commissioning, you switch to "commissioning mode" in the Administration Tool .

The following functions are available in "commissioning mode":

- The changes from the local sessions are compiled and downloaded to the CPU.
- The changes are then automatically transferred to the server project and the local session is updated.
- A new revision is created on the server after each download.
- This ensures that the project versions in the CPU and on the multiuser server are consistent.

> **Note**
>
> If the multiuser server is not reachable or other errors occur during downloading, you receive an error message and "commissioning mode" is exited.
>
> In this case you can download directly to the CPU from the local session in "engineering mode" and transfer your changes to the server project once the connection to the server has been established again.

### Enabling and disabling "commissioning mode"

"Commissioning mode" is enabled and disabled in the Administration Tool. You always set the mode for all local sessions of a server project. All local sessions can either be in engineering mode or in commissioning mode.

See also: [Managing server projects and server libraries](Working%20with%20the%20TIA%20Project-Server.md#managing-server-projects-and-server-libraries)

See also: [Managing the project server with the graphic Administration Tool](Working%20with%20the%20TIA%20Project-Server.md#managing-the-project-server-with-the-graphic-administration-tool)

Proceed as follows:

1. Open the graphic tool for the multiuser server administration.

   - To open the start menu, click the command "Start" > "All Programs" > "Siemens Automation".
   - Click on the entry "TIA Project Server - Administration" to open the Administration Tool.
2. Under "Administration", you can find a list of the configured server connections as soon as you have set up a connection to the multiuser server with "Add server connection". On the right side, you receive additional information about the objects selected on the left in a detail view.
3. On the left side, select the server and the project for which you want to set up commissioning mode.
4. On the right side, click the "Multiuser Commissioning" button in the toolbar.

   - As soon as the button is active, it is given a blue background and the project selected on the left side receives the commissioning symbol as overlay.
   - With commissioning mode, the "Check for different data before download (recommended)" option is also activated.

   ![Enabling and disabling "commissioning mode"](images/115233591051_DV_resource.Stream@PNG-en-US.png)

   ![Enabling and disabling "commissioning mode"](images/115233591051_DV_resource.Stream@PNG-en-US.png)
5. Click the "commissioning mode" button in the toolbar again to exit "commissioning mode".

   - As soon as the button is deactivated, it has no color and no overlay symbol is displayed for the project selected on the left side.

### Result

The "commissioning mode" is switched on by clicking the "Multiuser Commissioning" button and switched off by clicking it again.

---

**See also**

[Managing the project server with the graphic Administration Tool](Working%20with%20the%20TIA%20Project-Server.md#managing-the-project-server-with-the-graphic-administration-tool)
  
[Managing server projects and server libraries](Working%20with%20the%20TIA%20Project-Server.md#managing-server-projects-and-server-libraries)

## Working with synchronous commissioning

### Introduction

Multiuser Commissioning is available in "synchronous mode" and "asynchronous mode".

You switch between synchronous and asynchronous commissioning in the TIA Portal settings via Options > Settings > Multiuser > Commissioning settings.

For the current session, you can switch using the button in the project tree. However, this switch only remains active until the session is closed. When the local session is opened again, the default setting from the TIA Portal settings will be used once more.

### Working with synchronous commissioning

With synchronous commissioning, you work with Multiuser Commissioning as before. This setting is the default.

This is how synchronous Multiuser Commissioning works in the TIA Portal:

1. First you create and edit your projects in the engineering phase with Multiuser Engineering.

   For more details, see: [Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)
2. As soon as your projects are ready for commissioning, you continue working with Multiuser Commissioning .

   - As with commissioning, project management is located either on a local or external server.
   - Different users work in local sessions, based on the projects managed by the server.
   - Users can also work independently from each other in local sessions also during commissioning.
   - The changes from the local sessions are first always downloaded to the common CPU and then after successful download, transferred to the server project.
   - Downloaded changes from other users are displayed and can be conveniently applied.
   - The server project is already synchronized on the project server. This means consistent versions of the server project are always downloaded to the CPU. Time-consuming synchronization of different project versions on the CPU therefore becomes obsolete.

### Notes on working in synchronous commissioning mode

Observe the following notes on working in synchronous mode:

- You cannot perform any other activities in the TIA Portal until download to the device is complete.
- Working in synchronous commissioning requires significantly more time because the projects always need to be opened and closed.
- To save time and be able to work faster, switch to "asynchronous commissioning mode", which runs in a second instance of the TIA Portal in the background.

---

**See also**

[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)

## Working with asynchronous commissioning

### Introduction

As of V16, Multiuser Commissioning is available to you in "synchronous mode" and in "asynchronous mode".

You switch between synchronous and asynchronous commissioning in the TIA Portal settings via Options > Settings > Multiuser > Commissioning settings.

For the current session, you can switch using the button in the project tree. However, this switch only remains active until the session is closed. When the local session is opened again, the default setting from the TIA Portal settings will be used once more.

### Working with asynchronous Multiuser Commissioning

With asynchronous commissioning, you also work with Multiuser Commissioning as before.

This is how Multiuser Commissioning works in TIA Portal:

1. First you create and edit your projects in the engineering phase with Multiuser Engineering.

   For more details, see: [Overview of the mode of operation with Multiuser Engineering](Using%20Multiuser%20Engineering.md#overview-of-the-mode-of-operation-with-multiuser-engineering)
2. As soon as your projects are ready for commissioning, you continue working with Multiuser Commissioning .

   - As with commissioning, project management is located either on a local or external server.
   - Different users work in local sessions, based on the projects managed by the server.
   - Users can work independently from each other in local sessions, also during commissioning.
   - The changes from the local sessions are first always downloaded to the common CPU and then after successful download, transferred to the server project.
   - Downloaded changes from other users are displayed and can be conveniently applied.
   - The server project is already synchronized on the project server. This means consistent versions of the server project are always downloaded to the CPU. Time-consuming synchronization of different project versions on the CPU therefore becomes obsolete.

### Procedure for working in asynchronous commissioning mode

Observe the following procedure for working in asynchronous mode:

- In asynchronous commissioning, a second instance of the TIA Portal runs in the background. In this way, the times for loading into the device are significantly reduced in asynchronous mode.
- As a user, you are only informed if decisions and actions are required for download to the device.
- If no user decisions are required, download to the device takes place asynchronously in the background.
- If errors occur during compiling or downloading and user decisions are required, this is displayed in the Multiuser Commissioning editor.

  For more details, see: [Functionality of the commissioning editor](#functionality-of-the-commissioning-editor)
- In the commissioning editor, you receive additional information on which actions or decisions are required of you. If errors prevent a download to the CPU, you are prompted to resolve the errors in the server project view and then check in again.
- If errors occur that cannot be resolved in asynchronous mode, you should switch to synchronous commissioning mode. Then open the server project view and resolve the errors shown. Afterwards, start check-in from the server project view. You can switch back to asynchronous mode after this, if you wish.
- You will also be shown status information, warnings and error messages:

  - Compilation errors and download warnings are displayed in the commissioning editor.
  - Information and warnings are displayed in the Inspector window under the "Info > General" tab. When asynchronous commissioning has been started, a corresponding message is displayed here with a green arrow. When you click on this arrow, the commissioning editor is opened in the foreground.

---

**See also**

[Overview of the mode of operation with Multiuser Engineering](Using%20Multiuser%20Engineering.md#overview-of-the-mode-of-operation-with-multiuser-engineering)
  
[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)
  
[Functionality of the commissioning editor](#functionality-of-the-commissioning-editor)

## Important notes on working with asynchronous commissioning

### Introduction

As of V16, Multiuser Commissioning is available to you in "synchronous mode" and in "asynchronous mode".

Important notes and tips on working with asynchronous commissioning are provided below.

### Important notes on working in asynchronous commissioning mode

The following notes and tips facilitate your work and help you to utilize the advantages of asynchronous commissioning:

**Defining login information in Windows**

- If you use login information for the project server that is different to your Windows login information, you need to add the login information for the project server to the Windows Credential Manager:

  - To do this, open the Control Panel and select the Credential Manager under the relevant user account.
  - Click on "Windows Credentials" and add a new credential.
  - To do this, enter the Internet or network address of the server used, as well as the user name and password that allow access to the server, in the subsequent dialog.

**Limitations of working with Safety**

- Program changes requiring a Safety password can be loaded in synchronous or asynchronous commissioning.
- For loading in asynchronous commissioning, you need a user management (UMAC) configured with the corresponding rights for the Safety project.

**Renumbering data blocks in asynchronous commissioning**

- If renumbering of data blocks becomes necessary for a download in asynchronous commissioning, e.g. after copying a data block, you will receive a corresponding message in the TIA Portal. If you confirm the request for renumbering, the renumbering is performed during compiling. However, asynchronous commissioning is first aborted with an error message.
- In this case, start the download to the device again. The renumbered block is then transferred to the device.

**Renaming objects in asynchronous commissioning**

- When working with asynchronous commissioning, renaming of objects can only be performed in the server project view; otherwise, asynchronous commissioning will be aborted.

**Certificates**

- To apply the certificates required for the server, you should close and re-open the TIA Portal once after the first certificate confirmation.
- The certificates are then saved in the settings and applied permanently. In this way, you avoid repeated queries of the certificates.

**Unlock server**

- If an abort with server lock occurs due to an error when working in commissioning mode, you can unlock the server as follows:

  - Open the server project view in the TIA Portal and close it again.
  - As an alternative, you can also reset the server lock via the Administration Tool .

**Creating new objects in the local session**

- If you work with multiple users in different local sessions in asynchronous mode, you should always update your local session after creating and checking in new objects.
- This has the advantage that the newly created objects in your local session can be synchronized with the server project.
- Blocks with identical block numbers in the different local sessions can be renumbered after the synchronization, for example. This enables you to continue working with a consistent server project version.

**Loading in asynchronous commissioning**

- In asynchronous commissioning, only the function "Software (only changes)" is executed. Therefore, no hardware configuration is transferred.

**Updating the local session in asynchronous commissioning**

- When working with asynchronous commissioning, the local session is **not** automatically updated.
- Make sure to update your local session at regular intervals in order to apply the changes made by other users on the server project to your local session.

**Permanently displaying the commissioning editor**

- Because asynchronous commissioning runs in the background, the commissioning editor is not displayed permanently. As soon as you start your first download to the device, the commissioning editor is opened in the background and displayed in the status bar. Click the icon in the status bar to open the editor.
- If you want to see the commissioning editor permanently, you have the following options:

  - Undock the commissioning editor from the TIA Portal and position it next to the TIA Portal on your screen or on a second screen.
  - Alternatively, you can split the work window in the TIA Portal and display the commissioning editor permanently in the split window.

## Functionality of the commissioning editor

### Introduction

The multiuser commissioning editor is only required when working in asynchronous mode.

In asynchronous commissioning, a second instance of the TIA Portal runs asynchronously in the background, which enables significantly faster download times.

The commissioning editor is started in the background the first time asynchronous download is started and is displayed as a button in the status bar.

If errors or problems occur during downloading when working in asynchronous mode, these are displayed in the commissioning editor so that you can resolve them.

### Opening the commissioning editor

If you are working with asynchronous commissioning and perform a download operation, you will receive the corresponding messages on this as usual in the "Info > General" tab in the Inspector window. As soon as asynchronous commissioning has been started in the background, you receive a corresponding message with an appended green arrow.

You have the following options to open the editor:

1. Open the commissioning editor by clicking the "Commissioning editor" button shown in the status bar after starting the download operation.
2. Open the commissioning editor by clicking on the green arrow in the Inspector window as shown in the graphic.

The following graphic displays the messages in English in the Inspector window.

![Opening the commissioning editor](images/127925354507_DV_resource.Stream@PNG-en-US.png)

### Permanently displaying the commissioning editor

If messages or decisions for the download to the device are required when working in asynchronous mode, these are displayed in the commissioning editor.

The commissioning editor does **not** automatically come to the foreground, however.

> **Note**
>
> **Permanently displaying the commissioning editor**
>
> To permanently display the commissioning editor that is open in the background, you should undock it from the TIA Portal and position it in a separate window on a second monitor.
>
> Alternatively, you can split the work window in the TIA Portal and display the commissioning editor permanently in the split window.
>
> You will then be able to see queued messages from the background instance immediately and make the relevant decisions.

When the commissioning editor has been closed, it can be opened again by clicking on the message in the Info window. On every new download to the device, a closed commissioning editor is opened in the **background** again and displayed in the status bar.

### Structure of the commissioning editor

The figure below shows an example of the structure of the commissioning editor with English interface language:

![Structure of the commissioning editor](images/127925345675_DV_resource.Stream@PNG-en-US.png)

### Structure of the commissioning editor

The commissioning editor has the following structure:

**1. Toolbar**:

Shows the button for saving the layout settings on the right-hand side.

**2. Button area:**

Shows the commissioning-specific buttons for the download.

The left-hand button indicates that "Commissioning is being executed".

You can view pending load restrictions via the "Pending load restrictions" button.

If there are requirements or user decisions are needed during download to the device, these are displayed under "Load requirements".

You can select and execute required actions in the corresponding drop-down list under "Action".

Using the buttons in the top right corner, you can apply or cancel selected actions with "Apply" or "Cancel".

**3. Commissioning messages**

The messages and information on the download to the device are shown here.
