---
title: "Using Exclusive Engineering"
package: PEExclEnenUS
topics: 21
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using Exclusive Engineering

This section contains information on the following topics:

- [Introduction to Exclusive Engineering](#introduction-to-exclusive-engineering)
- [Overview of the Exclusive Engineering work method](#overview-of-the-exclusive-engineering-work-method)
- [Requirements for working with Exclusive Engineering](#requirements-for-working-with-exclusive-engineering)
- [Icons and markings in the user interface](#icons-and-markings-in-the-user-interface)
- [Creating and managing server projects](#creating-and-managing-server-projects)
- [Creating and editing exclusive local sessions](#creating-and-editing-exclusive-local-sessions)

## Introduction to Exclusive Engineering

### Introduction

In the TIA Portal , you have the option of working with Exclusive Engineering.

Working with Exclusive Engineering has the advantage that you are working in an exclusive local session and that the TIA Project Server is used for central data management of your projects.

Use the TIA Project Server to manage the server project. You can also use a local project server.

You either work on your projects alone – with all the advantages that the project server of the TIA Portal offers – or you work together in a team on a project.

As long as you work in your exclusive local session, the project server and the server project are reserved exclusively for you. The project server and the server project are blocked from adopting changes made to the server project by other users.

As soon as you have transferred your changes to the server project, a new revision of the server project will be created. If necessary, you can also roll back to the individual revisions, thus restoring an older working version. The project history is therefore available to you at any time.

When you finish editing in the exclusive local session and remove the lock for the project server, the exclusive local session is deleted. All changes are already stored in your server project and the individual revisions of the server project. The project is available for further editing.

### Functionality of Exclusive Engineering

This is how Exclusive Engineering works in the TIA Portal:

1. The project management is on the local or external TIA Project Server.
2. You work in the exclusive local session you created, which is assigned to a specific server project.
3. You transfer the changes from the exclusive local session to the server project.
4. The server is locked for other users as long as you are working in your exclusive session.

   The server is released again for other users only when you remove the server lock.

   The exclusive local session is deleted.
5. After each data transfer to the server project, a revision is automatically created for the project history, to which you can also roll back.
6. When you have finished editing and all changes have been transferred to the server project, you can load the server project into the CPU and continue editing as usual.
7. After completing your work in the exclusive local session, you can unlock the project server again.

   The exclusive local session is deleted.

   Your changes are included in the server project.

### Parallel working with Exclusive Engineering and Multiuser Engineering

You can work in parallel in an exclusive session with Exclusive Engineering and in local sessions with Multiuser Engineering.

This way of working has some advantages and requires less time, because you can work on certain automation tasks simultaneously in a team and parallel as a single agent with exclusive rights to the server.

You can also temporarily edit a local session as an exclusive local session in the Exclusive Multiuser mode if required. More information: "[Opening an exclusive local session](#opening-an-exclusive-local-session)"

> **Note**
>
> **Working efficiently with Exclusive Engineering and Multiuser Engineering**
>
> When working in the local sessions, you should correct any errors that occur early so that working in the server project remains effective.

### Working with the TIA Project Server

You can find all the information about working with the project server in the section "Working with the TIA Project Server".

See also:

[Introduction to the project server](Working%20with%20the%20TIA%20Project-Server.md#introduction-to-the-project-server)

[Basics of the project server](Working%20with%20the%20TIA%20Project-Server.md#basics-of-the-project-server)

[Supported network configurations for the project server](Working%20with%20the%20TIA%20Project-Server.md#supported-network-configurations-for-the-project-server)

[Set network profiles for project server](Working%20with%20the%20TIA%20Project-Server.md#set-network-profiles-for-project-server)

[Installing and uninstalling the project server](Working%20with%20the%20TIA%20Project-Server.md#installing-and-uninstalling-the-project-server)

[Configuring and managing the project server](Working%20with%20the%20TIA%20Project-Server.md#configuring-and-managing-the-project-server)

---

**See also**

[Introduction to the project server](Working%20with%20the%20TIA%20Project-Server.md#introduction-to-the-project-server)
  
[Basics of the project server](Working%20with%20the%20TIA%20Project-Server.md#basics-of-the-project-server)
  
[Set network profiles for project server](Working%20with%20the%20TIA%20Project-Server.md#set-network-profiles-for-project-server)
  
[Opening an exclusive local session](#opening-an-exclusive-local-session)
  
[Supported network configurations for the project server](Working%20with%20the%20TIA%20Project-Server.md#supported-network-configurations-for-the-project-server)
  
[Installing and uninstalling the project server](Working%20with%20the%20TIA%20Project-Server.md#installing-and-uninstalling-the-project-server)
  
[Configuring and managing the project server](Working%20with%20the%20TIA%20Project-Server.md#configuring-and-managing-the-project-server)

## Overview of the Exclusive Engineering work method

### Introduction

Below you will find an overview of the general mode of operation with Exclusive Engineering.

### Rules for working with Exclusive Engineering

The following rules apply when working with Exclusive Engineering:

- You start with an empty or an already filled project and load it to the TIA Project Server or to the local project server.
- Then you create an exclusive session in which you edit the objects.
- As soon as you open an object for editing, a blue flag appears in the first column of the project tree.
- If a project has already been opened in another local session by another user, a yellow flag appears.
- If identical objects are opened in several sessions, they are marked with a red flag.

  In this case, one of the editors should close the object again so that there are no competing editing changes that overwrite each other.
- All changes may be made in the local session.

  This includes changes to the hardware configuration or to objects not supported by Multiuser Engineering.
- As long as you are working in the exclusive local session, the server is locked for the other users.

  The server is not unlocked until the exclusive session is terminated and the server lock is removed.

### Overview of the mode of operation with Exclusive Engineering

To use the functionality of Exclusive Engineering, follow these steps:

| Action | Example |
| --- | --- |
|  |  |
| **1. Create server project on the**  **TIA Project Server**     You install a project server and upload an empty or already filled single-user project to the project server used.      **Result:**   By uploading a project to the project server, you generate a server project out of the single-user project. | ![Overview of the mode of operation with Exclusive Engineering](images/126682239371_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **2. Create exclusive local session**     You create an "exclusive local session" as a copy of the server project on your computer.   - You edit the desired objects in the exclusive local session.      **Result:**   You edit your program until you have reached a certain working version and want to apply your changes to the server project. | ![Overview of the mode of operation with Exclusive Engineering](images/126458886667_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **3. Apply changes**     As soon as the work in the exclusive local session has reached a certain working version, apply the changes to the server project.   - The changes from the exclusive local session are applied to the server project through the transfer. - A new revision of the server project is created after each check-in. - You have the option of documenting the progress of the project using the comments entered.      **Result:**   Your changes are transferred to the server project.  A new revision of the server project is created. | ![Overview of the mode of operation with Exclusive Engineering](images/126459553035_DV_resource.Stream@PNG-en-US.png) |
|  |  |
| **4. Processing is completed**     Editing the various configuration tasks in the exclusive local session has been completed.  You have transferred all changes to the server project and selected the option "Exit Exclusive Engineering" in the "Apply changes" dialog.     **Result:**   The exclusive local session and the server project are synchronized.  Terminating Exclusive Engineering removes the server lock and deletes the exclusive local session. | ![Overview of the mode of operation with Exclusive Engineering](images/126685078923_DV_resource.Stream@PNG-en-US.png) |

---

**See also**

[Opening an exclusive local session](#opening-an-exclusive-local-session)

## Requirements for working with Exclusive Engineering

### System requirements

The same hardware and software requirements as for working with TIA Portal apply to working with Exclusive Engineering .

For information about the regulations in place for the products you have installed, go to "Installation" > "System requirements for installation".

> **Note**
>
> **Identical software installation required for working with Exclusive Engineering**
>
> To work with Exclusive Engineering without any restrictions, it is important that the same software products of TIA Portal are installed with identical product versions on all engineering systems used.

> **Note**
>
> **Access to the project server**
>
> Users can only receive access to the project server if they are **not** included in the local administrator group of the project server.

> **Note**
>
> **Access to the server project**
>
> Users can only receive access to the server project if they are included at least as a "Member" in the user management of the project server.

### TIA Project Server

To work with the full functionality of Exclusive Engineering , you need an installed project server.

You need administrator rights in part for installing, configuring and administering the project server.

You will find information on the compatibility of the project server under:[Notes on the compatibility of the project server](Working%20with%20the%20TIA%20Project-Server.md#notes-on-the-compatibility-of-the-project-server)

The project server is configured and administered with the supplied tools.

Two alternative procedures are available for this purpose:

- Using the graphical user interface
- Using the "Administrative Tools" and "Power Tools" which are executed with the command line.

You can configure and administer the project server using a convenient user interface or with command line commands. Both procedures lead to an identical result.

A detailed description of the procedure is available under "[Installing and uninstalling the project server](Working%20with%20the%20TIA%20Project-Server.md#installing-and-uninstalling-the-project-server)" and under "[Configuring and managing the project server](Working%20with%20the%20TIA%20Project-Server.md#configuring-and-managing-the-project-server)".

### Network profiles for the project server

You have the option of setting the required performance capability for the network profile you are using in the settings for the TIA Portal.

To do so, select the required profile from the drop-down list in TIA Portal under "Options" > "Settings" > "Project sever" > "Server network profiles".

You will find a detailed description of the network profiles under: [Set network profiles for project server](Working%20with%20the%20TIA%20Project-Server.md#set-network-profiles-for-project-server)

### Licensing for Exclusive Engineering

You do not need an additional license to work with Exclusive Engineering .

### Archiving and retrieving projects

The following restrictions apply to archiving and retrieving multiuser projects:

- You can only archive local sessions as single-user projects.
- You cannot archive or retrieve server projects.

### Opening a local session as reference project

When working with Exclusive Engineering, you can open a locally stored session as a reference project.

You can find additional information on working with reference projects, here:[Using reference projects](Editing%20projects.md#using-reference-projects)

### Length of path and file names for Exclusive Engineering

If the path and file names have more than 259 characters in total, an error message is displayed when you are working with Exclusive Engineering. You are notified that the used names are too long and that the requested action cannot be performed for this reason. Shorten the path names or file names in this case so that the required action can be performed.

---

**See also**

[Introduction to the project server](Working%20with%20the%20TIA%20Project-Server.md#introduction-to-the-project-server)
  
[Set network profiles for project server](Working%20with%20the%20TIA%20Project-Server.md#set-network-profiles-for-project-server)
  
[Notes on the compatibility of the project server](Working%20with%20the%20TIA%20Project-Server.md#notes-on-the-compatibility-of-the-project-server)
  
[Archiving an exclusive local session](#archiving-an-exclusive-local-session)
  
[Installing and uninstalling the project server](Working%20with%20the%20TIA%20Project-Server.md#installing-and-uninstalling-the-project-server)
  
[Configuring and managing the project server](Working%20with%20the%20TIA%20Project-Server.md#configuring-and-managing-the-project-server)
  
[Using reference projects](Editing%20projects.md#using-reference-projects)

## Icons and markings in the user interface

This section contains information on the following topics:

- [Icons in the user interface](#icons-in-the-user-interface)
- [Markings in the user interface](#markings-in-the-user-interface)

### Icons in the user interface

#### Introduction

When you are working with Exclusive Engineering and a local session is open, you can see the following icons in the TIA Portal user interface.

#### Icons in the toolbar

The Exclusive Engineering user interface shows the following icons in the toolbar when a local session is open:

![Icons in the toolbar](images/172098004107_DV_resource.Stream@PNG-en-US.png)

| Icon | Meaning |
| --- | --- |
| ![Icons in the toolbar](images/171998867723_DV_resource.Stream@PNG-de-DE.png) | **Multiuser mode**   The icon is enabled when a local session is open in multiuser mode.  To temporarily switch to the Exclusive Multiuser mode, click the "Exclusive multiuser mode" icon.  Requirements for the change:  - No other session is in progress or locked as an exclusive local session.   Before the mode change, the status of the local session and the server project is checked. If you need to refresh the session or server project before changing the mode, a corresponding message is displayed. |
| ![Icons in the toolbar](images/171998863627_DV_resource.Stream@PNG-de-DE.png) | **Exclusive multiuser mode**   The icon is activated when you edit a local session temporarily in the Exclusive Multiuser mode.  To return to multiuser mode, click the "Multiuser mode" icon. After that, other sessions can be opened as exclusive local sessions.  Before the mode change, the status of the local session and the server project is checked. If you need to refresh the session or server project before changing the mode, a corresponding message is displayed. |
| ![Icons in the toolbar](images/125653527307_DV_resource.Stream@PNG-de-DE.png) | **Apply changes**   If you click on this icon, your changes from the exclusive local session are applied to the corresponding server project. |
| ![Icons in the toolbar](images/125655281931_DV_resource.Stream@PNG-de-DE.png) | **Server status "locked for other users"**   This icon indicates that the associated project server is displayed as "locked" for other users because it is currently being used by you in an exclusive session. |
| ![Icons in the toolbar](images/88369531915_DV_resource.Stream@PNG-de-DE.png) | **Server status "locked"**   This icon indicates that the associated project server is currently being used by a user and is therefore locked. If you place the mouse pointer on this icon, you will receive additional information about the lock. |
| ![Icons in the toolbar](images/88369535627_DV_resource.Stream@PNG-de-DE.png) | **Server status "not connected"**   This icon indicates that the associated project server is not connected. |
| ![Icons in the toolbar](images/103395513995_DV_resource.Stream@PNG-de-DE.png) | **"Work offline" server status**   This symbol indicates that no connection is established to the project server, since you have enabled the "Work offline" function.  Clear the check box under "Project > Project server > Work offline", to re-establish a connection to the project server. |

#### Icons for displaying server projects

The following icons are displayed in the user interface for server projects and exclusive local sessions:

| Icon | Meaning |
| --- | --- |
| ![Icons for displaying server projects](images/125656947467_DV_resource.Stream@PNG-de-DE.png) | **Project server**   This icon indicates a project server when working with Exclusive Engenineering. |
| ![Icons for displaying server projects](images/125655397643_DV_resource.Stream@PNG-de-DE.png) | **Server project**   This icon identifies a server project associated with a project server. |
| ![Icons for displaying server projects](images/125658816779_DV_resource.Stream@PNG-de-DE.png) | **Local session**   This icon indicates a local session that belongs to a Multiuser server project. |
| ![Icons for displaying server projects](images/84910995339_DV_resource.Stream@PNG-de-DE.png) | **Exclusive local session**   This icon indicates a local session which is being edited in the Exclusive Multiuser mode. |

#### Icons for markings in Exclusive Engineering

The following icons for markings are used in Exclusive Engineering:

| Icon | Meaning |
| --- | --- |
| ![Icons for markings in Exclusive Engineering](images/84845469195_DV_resource.Stream@PNG-de-DE.png) | **Markable object**   This object can be marked for check-in by clicking it. |
| ![Icons for markings in Exclusive Engineering](images/82716066059_DV_resource.Stream@PNG-de-DE.png) | **Marked object**   The object was marked in your own exclusive local session for check-in. |
| ![Icons for markings in Exclusive Engineering](images/84859083659_DV_resource.Stream@PNG-de-DE.png) | **Marked object**   The object was marked for check-in in a different session or in the server project view. |
| ![Icons for markings in Exclusive Engineering](images/84859302027_DV_resource.Stream@PNG-de-DE.png) | **Marked object with conflict**   The object was marked for check-in in multiple local sessions or in a local session and in the server project view and causes a conflict.  An object should only be marked for check-in once within the entire multiuser working area.  An object marked in red can still be checked in. However, the check-in may cause unwanted overwriting in the server project because only the last checked in version is applied in the server project. |
| ![Icons for markings in Exclusive Engineering](images/84859545739_DV_resource.Stream@PNG-de-DE.png) | **Object is outdated**   If one of the icons mentioned above is also identified with this overlay, the object no longer corresponds to the latest version of the server project and should be updated.   If the object is checked in without refresh, the editing of the other user is overwritten and thus cancelled.  The refresh ensures that all editors of a multiuser project have a consistent version. |

### Markings in the user interface

#### Introduction

When working with Exclusive Engineering , multiuser-specific icons are displayed in the TIA Portal user interface which make it easier for multiple users to work at the same time. A unique, user-specific visualization is intended to make collaboration within server projects and in the local and exclusive sessions more effective and transparent.

#### Marking objects

To edit an object using Exclusive Engineering, it must first be "marked". Only objects marked for editing can be transferred into the Server project after editing.

Marking can only be added for "marked objects". Objects that cannot be processed in the exclusive local session are also not marked.

You can, however, edit such objects in the server project view.

The icons described below show you which objects were marked by you or other editors.

You can mark objects manually by clicking the gray flag in front of the respective object, or automatically. If an object not yet marked manually is opened in an editor in an exclusive local session, it is automatically marked with the "Autoselect" function.

#### Icons for markings in Exclusive Engineering

The following icons for markings are used in Exclusive Engineering:

| Icon | Meaning |
| --- | --- |
| ![Icons for markings in Exclusive Engineering](images/84845469195_DV_resource.Stream@PNG-de-DE.png) | **Markable object**   This object can be marked for check-in by clicking it. |
| ![Icons for markings in Exclusive Engineering](images/82716066059_DV_resource.Stream@PNG-de-DE.png) | **Marked object**   The object was marked in your own exclusive local session for check-in. |
| ![Icons for markings in Exclusive Engineering](images/84859083659_DV_resource.Stream@PNG-de-DE.png) | **Marked object**   The object was marked for check-in in a different session or in the server project view. |
| ![Icons for markings in Exclusive Engineering](images/84859302027_DV_resource.Stream@PNG-de-DE.png) | **Marked object**  **with conflict**   The object was marked for check-in in multiple local sessions or in a local session and in the server project view and causes a conflict.  An object should only be marked for check-in once within the entire multiuser working area.  An object marked in red can still be checked in. However, the check-in may cause unwanted overwriting in the server project because only the last checked in version is applied in the server project. |
| ![Icons for markings in Exclusive Engineering](images/84859545739_DV_resource.Stream@PNG-de-DE.png) | **Object is outdated**   If one of the icons mentioned above is also identified with this overlay, the object no longer corresponds to the latest version of the server project and should be updated.   If the object is checked in without refresh, the editing of the other user is overwritten and thus cancelled.  The refresh ensures that all editors of a server project have a consistent version. |

> **Note**
>
> **Objects without flags**
>
> Note that objects without flag may only be edited in the server project view and not in the exclusive local session.

#### Display of multiuser markings in the TIA Portal

When you are working with Multiuser Engineering in the local session or in the server project, the multiuser-specific markings are displayed in the following views of the TIA Portal in all editors:

- In the project tree
- In the detail view
- In the overview window under "Details"
- In the library views

An additional first table column is available in all table displays within the project tree when working with Exclusive Engineering. The first table column is reserved for the multiuser-specific markings described above.

The following figure shows an example of multiple selected objects in the project tree:

![Display of multiuser markings in the TIA Portal](images/104401534219_DV_resource.Stream@PNG-en-US.png)

## Creating and managing server projects

This section contains information on the following topics:

- [Introduction to working in server projects](#introduction-to-working-in-server-projects)
- [Create a new server project](#create-a-new-server-project)
- [Delete server project](#delete-server-project)

### Introduction to working in server projects

#### Introduction

Once the project server has been installed and then configured and started with the help of the Power Tools, you can manage the server projects in your TIA Portal.

#### Manage server projects

When you execute the command "Project > Project server > Manage server projects", all existing server projects and local sessions for the existing server connections are displayed in the next dialog.

If you have not added a Server project yet, the list is empty.

If server projects already exist, they are displayed. From the drop-down list in the top part of the dialog, select the required server connection for which all existing server projects and local sessions are then listed.

You can execute the following actions with the individual buttons:

- "Select server": Adds a new server connection.
- "Update": Updates the display in the dialog.
- "Manage server projects": Opens the display for the Server projects in the settings.
- "Add project to the server": Opens the dialog and adds a new server project to the selected server connection.

  You have the following options:

  - Add new project
  - Add existing project
  - In the "Server project name" field, you can enter a new name for the server project, if desired.
- "Create local session": Creates a new local session for the selected server project.
- "Cancel": Cancels the action and closes the dialog.
- "Add": Adds the selected local session.

> **Note**
>
> **Displaying server projects**
>
> Server projects can only be displayed when a connection to the Project server exists and it has been started.
>
> You will be notified if a connection could not be established.

> **Note**
>
> **Deleting server projects**
>
> To prevent inconsistencies in the project management, server projects must not be deleted "manually" with the Explorer in the storage directory.
>
> Server projects must always be deleted using the Power Tools.
>
> All associated local sessions must be deleted before a server project can be deleted.

#### Commands in the shortcut menu

The following actions can be executed in the "Manage server projects" dialog from the shortcut menu:

- Add project to the project server.
- Create a local session.
- Delete a local session.
- Export a local session as single-user project.
- Archive local session.

### Create a new server project

#### Introduction

When working with a project server, you must first create a server project.

A Server project is created by adding a standard project (single-user project) to the previously installed Project server and then be able to use this project as a Server project.

#### Requirement

The TIA Portal and a project server are installed.

#### Procedure

To create a Server project, follow these steps:

1. In the TIA Portal, click the menu command "Project > Project server > Manage Server projects".
2. In the following dialog, double-click the button "Add project to server".
3. Select the project which you want to add as Server project.

   - To add a new project, click the button "New project".
   - To add an existing project, click the button "Add existing project"
4. If required, set the required source path to the single-user project or navigate to the required directory using the "..." button.
5. Select the project which you want to add as Server project.
6. If required, enter a comment on the server project under "Details".

   The information under "Project name" and "Published by" are always preassigned and cannot be edited.

   The displayed name for the server project can be edited.
7. If you want to create a local session for the newly added server project, enable the "Create local session" button.
8. Click "Add".

   If the selected project already exists as server project or is currently opened by another user, you will be notified.

#### Result

The selected single-user project is added as new Server project and displayed under "Project > Project server > Manage server projects".

If the option "Create local multiuser session" was selected, a new local session is created and opened.

### Delete server project

#### Introduction

Once the project server has been installed and then configured and started with the help of the Power Tools , you can manage the Server projects in the TIA Portal.

The deletion of a server connection can be carried out in the TIA Portal with the command "Tools > Settings > Project Server" using the "Delete" command.

The deletion of a server project is only possible via the Power Tools.

#### Deleting a server project from the project server

To delete a server project on the project server, proceed as follows.

1. Open the Power Tools as user interface or via the command line and use the commands offered there to delete a server project.

   For more details, see: [Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

---

**See also**

[Adding and deleting a new server connection](Working%20with%20the%20TIA%20Project-Server.md#adding-and-deleting-a-new-server-connection)
  
[Commands for managing the project server](Working%20with%20the%20TIA%20Project-Server.md#commands-for-managing-the-project-server)

## Creating and editing exclusive local sessions

This section contains information on the following topics:

- [Creating an exclusive local session](#creating-an-exclusive-local-session)
- [Opening an exclusive local session](#opening-an-exclusive-local-session)
- [Editing an exclusive local session](#editing-an-exclusive-local-session)
- [Saving an exclusive local session](#saving-an-exclusive-local-session)
- [Closing an exclusive local session](#closing-an-exclusive-local-session)
- [Archiving an exclusive local session](#archiving-an-exclusive-local-session)
- [Editing the exclusive local session offline](#editing-the-exclusive-local-session-offline)
- [Exit working in the exclusive local session](#exit-working-in-the-exclusive-local-session)
- [Show all exclusive local sessions associated with a server project](#show-all-exclusive-local-sessions-associated-with-a-server-project)

### Creating an exclusive local session

#### Introduction

To work with Exclusive Engineering , you need to create an exclusive local session.

The exclusive local session is always assigned to a specific server project.

#### Requirement

The TIA Portal and a project server are installed.

You have created a server project.

#### Procedure

To create an exclusive local session, follow these steps:

1. In the TIA Portal, select the command "Project > Project server > Manage server projects".

   The "Manage server projects" dialog box opens.

   The last used server project is automatically displayed.
2. In the "Projects" column of the "Manage server projects" dialog, double-click in the cell with the text "Create new local session".

   Alternatively, select the "Create new local session" command in the shortcut menu of the server project.

   The "Create local session" dialog box opens.

   The author for the session is entered by default in this dialog box and cannot be edited.
3. Select the type of local session you want to create:

   - Exclusive Engineering:

     An editor works exclusively in the local session.

     If you close the exclusive local session after finishing editing, it will be deleted automatically.
   - Multiuser Engineering:

     Several editors working in parallel.

     You can temporarily edit the local session as an exclusive local session in the Exclusive Multiuser mode if required.
4. If necessary, change the name of the session.
5. To open the session immediately after it is created, select the "Open local session" option.
6. To create the session, click "Create".

#### Result

The exclusive local session is created and displayed in the dialog "Manage server projects" under the selected server project.

### Opening an exclusive local session

#### Introduction

You have different options for opening a local session for editing in Exclusive Engineering:

- With "Project > Open" in the TIA Portal or from the list of the most recently opened projects
- With the command "Project > Project server > Manage server projects" in the TIA Portal.
- When TIA Portal is closed with the Microsoft Windows Explorer project
- Offline without a server connection
- Opened local session can be temporarily edited in the "Exclusive Multiuser mode"

As soon as you open a local session that is assigned to the local project server, a prompt appears asking if you want to start the local project server, if it has not yet been started.

Click "Yes" to start the local project server and to open the selected local session.

> **Note**
>
> **Opening local sessions**
>
> - A renamed or deleted local session can no longer be opened.
> - You can also open a locally saved session as a reference project.
>
> If a local session can no longer be opened, you will receive a notification that it cannot be opened.
>
> You will then be asked if you want to export this local session as a single-user project.

#### Requirement

The TIA Portal and a project server are installed.

You have created an executable Server project and a valid local session.

#### Opening a local session

To open a recently used local session, follow these steps:

1. In the TIA Portal, select the command "Project > Open".

   The "Open project" dialog box opens with a list of recently used projects and sessions.

   The icons in the first column help you distinguish between single-user projects and multiuser projects.
2. Select the preferred local session and click "Open".

**"Open project" dialog: Project icons**

The icons in the first column help you distinguish between single-user projects and multiuser projects.

| Symbol | Meaning |
| --- | --- |
| ![Opening a local session](images/172092479371_DV_resource.Stream@PNG-de-DE.png) | Single-user project |
| ![Opening a local session](images/172092692619_DV_resource.Stream@PNG-de-DE.png) | Multiuser project: Local session (Multiuser Engineering) |
| ![Opening a local session](images/172092701323_DV_resource.Stream@PNG-de-DE.png) | Multiuser project: Exclusive local session (Exclusive Engineering) |

**Result**

The selected local session is opened.

#### Opening a local session from a different storage location

To open a local session that has been moved to another storage location in the meantime, follow these steps:

1. In the TIA Portal, select the command "Project > Open".

   The "Open project" dialog box opens with a list of recently used projects and sessions.
2. Select the preferred local session and click "Open".

   You are notified that you are trying to open a local session from a different storage location.
3. Confirm this query with "OK" if you want to execute the action.

**Result**

The selected local session is opened from the new storage location.

The information about the new storage location is saved in the associated server.

#### Opening a local session by means of the associated server project

To open a local session via the associated server project, follow these steps:

1. In the TIA Portal, select the command "Project > Project server > Manage server projects".

   The "Manage server projects" dialog box opens.
2. Select the required project server in the drop-down list.
3. Select the server project required and the exclusive local session from the list.
4. To also display local sessions which were created on another computer, open the multiuser settings via "Options > Settings > Multiuser".

   Activate the option "Show local session created on other systems".

   Open the "Manage server projects" dialog again. To refresh the view, click the icon ![Opening a local session by means of the associated server project](images/88372482443_DV_resource.Stream@PNG-de-DE.png).

   In the "Computer name" column you can sort according to the computer name.
5. Double-click the exclusive local session and select "Open local session" in the shortcut menu.
6. To open a new local session immediately during creation, activate the "Open local session" in the dialog "Create local session".

**Result**

All opened dialog boxes are closed and the selected local session is opened.

#### Opening a local session with the Microsoft Windows Explorer

To open a local session with the Microsoft Windows Explorer, follow these steps:

1. When the TIA Portal is closed, navigate to the directory in which your local sessions are stored in Microsoft Windows Explorer.
2. Select the desired local session with the file extension ".es<version>" and double-click to open it.

**Result**

The TIA Portal is started and the selected local session is opened.

> **Note**
>
> **Closing an exclusive local session**
>
> When working with Exclusive Engineering, close the local session with the command "Project > Close".

#### Opening a local session without a server connection

A local session can also be opened when the associated server is currently not available.

In this case, when you open the local session, a message informs you that you can continue working offline in the local session with the following restrictions:

- You cannot see the changes made by other users in your local session.

  - No yellow or red flags are displayed.
  - No "outdated" objects are displayed.
- You cannot check in your changes to the server project until the server connection has been restored.

If you confirm this message with "OK", you can continue working in your local session even without a server connection.

#### Editing a local multiuser session in Exclusive Multiuser mode

As long as no other exclusive local session is active, you can switch to "Exclusive Multiser mode" while working in a local session.

After editing, you can leave the Exclusive Multiuser mode and edit the session again as a local session.

To change the mode, use the icons in the local session toolbar.

- The Exclusive Multiuser mode is started from the local session without closing the local session.

  When a local session is open, the type of local session is displayed as an active icon in the toolbar.

  Click the disabled icon in each case to switch between the types of local session.
- When switching to the exclusive multiuser mode, all changes in the local session are retained.

**Requirement**

- The local session is based on the current project state of the server project.
- The server and the server project are not locked by another exclusive local session.

**Procedure**

To temporarily edit an open local session as an exclusive local session, follow these steps:

1. Open a local session that was created for working with Multiuser Engineering.
2. Update the local session.
3. Click the "Exclusive multiuser mode" icon: ![Editing a local multiuser session in Exclusive Multiuser mode](images/171998863627_DV_resource.Stream@PNG-de-DE.png)

   The project server and the server project are locked for other users.

   You can edit the opened local session in the Exclusive Multiuser mode.
4. Check in the changes in the server project.
5. To stop working in Exclusive Multiuser mode, click the "Multiuser mode" icon: ![Editing a local multiuser session in Exclusive Multiuser mode](images/171998867723_DV_resource.Stream@PNG-de-DE.png)

   The server lock is removed. The project server and the server project are released again for other users.

   You can continue working in the open local session with Multiuser Engineering.

### Editing an exclusive local session

#### Introduction

To be able to work in a server project within the context of Exclusive Engineering , you need to create an exclusive local session.

Each time changes are transferred to the server project, a new revision of the server project is created when working with Exclusive Engineering.

#### Requirement

The following steps are required to be able to process the engineering tasks in an exclusive local session:

- The TIA Portal and a project server are installed.
- Alternatively, you can use the local project server installed by default.
- You have created an executable project for working with Exclusive Engineering .
- You have loaded the prepared project to the project server and thus created a server project.
- You have created an exclusive local session.

#### Editing an exclusive local session

To edit objects in an exclusive local session, follow these steps:

1. Create a new exclusive local session or open an existing exclusive local session.
2. Make the desired changes to the various objects in the local session.

   Since you are working exclusively in the local session, you can edit all objects contained in your session.
3. Apply your changes to the server project by clicking on the "Apply changes" button in the project tree.

   In the "Apply changes" dialog that follows, select the desired options and click "OK".

#### Result

The changes from the exclusive local session are applied to the server project with the selected options.

A new revision of the server project is created.

The exclusive session is not saved locally.

### Saving an exclusive local session

#### Introduction

An exclusive local session is saved with Exclusive Engineering with the file identifier ".es<version number of TIA Portal>" when working with.

#### Requirement

The TIA Portal and a project server are installed.

You have created a server project and a valid local session.

#### Saving an exclusive local session

To save an exclusive local session, follow these steps:

1. Open the exclusive local session.
2. Make your required changes.
3. Select the "Save" command in the "Project" menu or click the "Save" button in the project tree.

#### Result

The exclusive local session is saved under the current project name with the file identifier ".es<version>".

### Closing an exclusive local session

#### Introduction

You close an exclusive local session as you would a single-user project with the command "Project > Close".

#### Requirement

TIA Portal and a project server are installed.

You have created a Server project and a valid exclusive local session that is open.

#### Procedure

To close an exclusive local session, follow these steps:

1. In TIA Portal, select the command "Project > Close".
2. Confirm the next prompt with "Yes" if you want to save your changes.

#### Result

The exclusive local session is closed.

The associated server project remains locked on the project server even after the exclusive local session has been closed.

### Archiving an exclusive local session

#### Introduction

Exclusive local sessions of the current product version can be archived as compressed or uncompressed single-user projects.

Archiving is independent of whether or not you have already transferred the changes you have made in the exclusive local session to the server project.

When archiving an open local session, the most recently saved state of the exclusive local session is used for archiving.

The local session archived as an exclusive single-user project has the file identifier ".zap<version number of TIA Portal>".

Archiving the exclusive local session offers the following advantages:

- Daily backup of your local session as a single-user project in TIA Portal.
- Use of the single-user project for testing and commissioning.
- Use of the single-user project as reference project for other projects.

> **Note**
>
> **Archiving of exclusive local sessions**
>
> When archiving the exclusive local session, it is saved as a single-user project and can therefore no longer be used as a local session.

#### Archiving an exclusive local session

To archive an exclusive local session as a single-user project, follow these steps:

1. Select the "Archive ..." command from the "Project" menu.

   The "Archive" dialog opens.
2. In the "Source path" field, the open local session is displayed with the extension ".als<version>" by default.

   You can also use the selection box to select a different exclusive local session for archiving.
3. To create a compressed archive file, select the "Archive as compressed file" option.
4. If you do not want to archive the search index and the HMI compile result, select the option "Discard restorable data".

   You can restore the discarded data if needed.
5. To add a date and time automatically, select the "Add date and time to the target name".
6. In the "Target path" field select the directory where you want to save the archive file or the new directory of the project.

   You can set the default directory under "Options > Settings > General > Archive settings > Storage location for project archives".
7. Click "Archive".

#### Result

The exclusive local session is archived as a single-user project.

An archive file of the local sessions with the file extension ".zap<version>" is created.

The archive file contains the complete project directory. The individual files of compressed archives are additionally reduced to the essential components to save space.

For uncompressed projects only a copy of the original project directory is created at the desired storage location.

### Editing the exclusive local session offline

#### Introduction

When you open an exclusive local session , the connection to the associated project server is automatically established.

However, you also have the option of working offline in an exclusive local session without a server connection.

If a server connection cannot be established when you open the local session, a dialog appears with a corresponding error message.

If you confirm this dialog with "OK", you can work in the local session even without a server connection with the following restrictions:

- Changes you are making in the local offline session cannot be transferred until a server connection is available once again.

> **Note**
>
> **Instructions for opening local sessions:**
>
> - A renamed or deleted local session can no longer be opened.
> - A local session cannot be opened as a reference project.
>
> When opening a local session that meets one of the criteria listed above, you will see a note informing you that the session cannot be opened.

#### Requirement

The TIA Portal and a project server are installed.

You have created an executable Server project and a valid local session.

#### Opening a local session and working offline

To open a local session, follow these steps:

1. In the TIA Portal, select the command "Project > Open".

   The "Open project" dialog box opens with a list of recently used projects and sessions.

   The icons displayed in the first column differentiate between single-user projects and server projects.
2. Select the preferred local session and click "Open".
3. If a server connection cannot be established to the associated project server, you receive a corresponding message.
4. Click "OK".
5. A second dialog opens which informs you that a server connection could not be established. If you confirm this dialog with "OK", you can continue working in your local session even without a server connection with the restrictions listed above.
6. Your changes can be saved locally in the exclusive session. The changes can be applied as soon as the server is available again.

#### Result

The selected local session is opened offline and can be edited offline.

The "Apply changes" button is grayed out and cannot be activated.

Changes can only be applied in the server project when a server connection is available again.

### Exit working in the exclusive local session

#### Introduction

There are several ways to exit working in your exclusive session, to remove the server lock again, and to delete the exclusive local session.

#### Requirement

TIA Portal and a project server are installed.

You have created a Server project and a valid exclusive local session that is open.

#### Procedure when an exclusive session is open

To exit working in an open exclusive session, proceed as follows:

1. Open the exclusive local session.
2. Click the "Apply changes" button in the project tree.

   The "Apply changes" dialog then opens.
3. Select the "Exit Exclusive Engineering " option in this dialog box.
4. Click "OK".

#### Procedure for closed exclusive sessions

To finish working in a closed exclusive session, proceed as follows:

1. Click the command "Project > Manage server projects".

   The "Manage server projects" dialog box opens.
2. Select the desired exclusive session and click "Exit local session" in the shortcut menu.
3. Click "OK".

#### Result

The changes from your exclusive local session are applied to the server project.

The lock for the project server is removed, and the server is released again for other users.

The exclusive local session is then deleted.

### Show all exclusive local sessions associated with a server project

#### Introduction

You have the option of displaying all exclusive local sessions associated with a Server project in TIA Portal.

#### Requirement

TIA Portal and a project server are installed.

You have created an executable Server project and a valid exclusive local session.

#### Displaying all local sessions

To display all exclusive local sessions belonging to a server project, follow these steps:

1. In TIA Portal, select the command "Project > Project server > Manage server projects".

   The "Manage server projects" dialog opens and displays all existing projects for the selected project server.
2. Select the required server connection.

   All server projects associated with this server connection are listed.
3. Select the required server project and open it in order to show all associated exclusive local sessions.
4. If you want to open an exclusive local session, select the respective session and click "Open".

#### Result

All exclusive local sessions available for the selected server project are displayed.
