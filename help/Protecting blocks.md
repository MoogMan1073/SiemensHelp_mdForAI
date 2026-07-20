---
title: "Protecting blocks"
package: ProgBlockProtectionenUS
topics: 13
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Protecting blocks

This section contains information on the following topics:

- [Protecting blocks](#protecting-blocks-1)
- [Connecting the password provider](#connecting-the-password-provider)
- [Show available password provider](#show-available-password-provider)
- [Recording activities of the password providers](#recording-activities-of-the-password-providers)
- [Define the type of password assignment](#define-the-type-of-password-assignment)
- [Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
- [Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
- [Setting up block know-how protection](#setting-up-block-know-how-protection)
- [Opening know-how protected blocks](#opening-know-how-protected-blocks)
- [Printing know-how protected blocks](#printing-know-how-protected-blocks)
- [Changing a password](#changing-a-password)
- [Removing block know-how protection](#removing-block-know-how-protection)

## Protecting blocks

### Introduction

You have the following options for protecting your blocks

- Know-how protection:

  With the help of know-how protection you can use a password to protect blocks of the OB, FB, FC type and global data blocks from unauthorized access.
- Copy protection:

  For S7-1200/1500 CPUs, you can also set up copy protection for code blocks which binds execution of the block to the CPU or the memory card with the defined serial number. When using copy protection for a block it makes sense to also know-how-protect the block to ensure that copy protection can only be revoked with a password.
- Write protection:

  You can assign write protection for code blocks, which prevent unintentional changes to the block.

Note the following points for know-how protection:

- You can not manually protect instance data blocks; they depend on the know-how protection of the assigned FB. This means that when you create an instance data block for a know-how protected FB, the instance data block also receives this know-how protection. This is independent of whether you explicitly create the instance data block or if it is created by a block call.
- With global data blocks you cannot edit the initial values and comments, this is possible, however, with instance data blocks.
- You cannot provide ARRAY data blocks with know-how protection.
- The load memory requirement can be higher for know-how-protected blocks.

If a block is know-how protected, only the following data is readable without the correct password:

- Interface parameters Input, Output, InOut, Return, Static
- Block title
- Block comment
- Block properties
- Tags of global data blocks without specification of the location of use

The following actions can be performed with a know-how protected block:

- Copying and deleting
- Calling in a program
- Compare offline/online
- Downloading

The code of the block, on the other hand, is protected from unauthorized reading and modification.

> **Note**
>
> Please note the following:
>
> - S7-1200 version 1.0 and S7-300/400 (only GRAPH and SCL blocks): If you download a know-how-protected block to a device, no restore information is loaded along with it. This means that you cannot open a know-how-protected block again even with the correct password if you upload it from the device.
> - Only the non-protected data is compared in offline-online comparison of know-how protected blocks.
> - You will no longer be able to access the block if you do not have the password.
> - If you add a know-how-protected block to a library, the master copy created will also be know-how protected.
> - You will find information on whether or not the block can be used as protected library item in the block properties under "Compilation > Library conformance". For this purpose, the block cannot use any tags from the operand areas Output (Q), Input (I), Bit memory (M), Timer function (T) or Count function (C), and cannot access data blocks.
> - Cross-references to used tags, bit memories, inputs and outputs in know-how-protected blocks are only displayed if the relevant blocks were unlocked before the cross-reference list was created by entering the correct password.
> - Automatic renumbering and manual renumbering without password of know-how-protected blocks is only possible for CPUs of the series S7-1500 and S7-1200 (V4). The know-how protection must also be set with a TIA Portal version V13 SP1 or higher. If these requirements for a know-how-protected block are not met, the loadable binary component of the block is no longer up-to-date when you change the number. In this case, the block must be recompiled before downloading it to a device. For know-how-protected blocks, this is only possible with the correct password. Keep this in mind particularly if you want to copy a know-how-protected block to another device in which there is already a block with the same number.
> - Always pass on a project that includes know-how-protected blocks as a project archive or library archive. In this way, you ensure that the know-how protection cannot be bypassed.
> - You cannot change the know-how protection settings for an open, know-how protected block.

### Using a password provider

You have the option of connecting the TIA Portal to an external password management system via a password provider. For this, a project product version V14 SP1 and higher is required.

If you are using a password provider, you can select the password from a list of passwords when setting know-how protection, copy or write protection. Only the names of the passwords are displayed in the list, the passwords themselves are not visible. When a block is opened, the TIA Portal connects to the password provider and retrieves the corresponding password. If the password provider is not available at this time, you can only open the block fully if manual input is defined as the fallback strategy and the corresponding password is known. The name of the password is not sufficient here. Depending on the selected security setting in the password provider, you can change the password for a know-how protected block or revoke protection again.

The use of a password provider increases security for your program code, as it is not necessary to pass on passwords for know-how protected blocks to other editors. Instead, all editors can connect the same password provider in order to obtain access to the blocks. If an editor leaves the project, there is no need to change the password.

In the event of problems with connected password providers, you can record the activities of password providers and forward the recording to Customer Support for analysis.

> **Note**
>
> **Safety note for block protection**
>
> If a block is protected by a password that was entered manually, manual input is always required to edit the block or its protection settings. This is true even if a password provider contains a password with the same content at a later time.

### Password policies

If you assign or change the password manually, the password must meet the following policies:

- The password must be at least 8 characters long.
- The password must not be longer than 120 characters.
- The password must contain at least one digit.
- The password must contain at least one special character.
- The password must contain at least one upper case letter and one lower case letter.

---

**See also**

[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)
  
[Creating a project archive](Editing%20projects.md#creating-a-project-archive)
  
[Archiving global libraries](Using%20libraries.md#archiving-global-libraries)

## Connecting the password provider

As an alternative to manual password input, a password provider can be connected to the TIA Portal. When using a password provider, you can select a password from a list of available passwords. When a know-how protected block is opened, the TIA Portal connects to the password provider and retrieves the corresponding password.

To connect a password provider you have to install and activate it. A settings file in which the use of a password provider is defined is also required.

### Installing and activating password providers

To install and activate a password provider, proceed as follows:

1. Install the desired password provider in accordance with the installation instructions of the password provider.
2. Open the TIA Portal.
3. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
4. In the area navigation, select the "Password provider > Available password providers" group.

   The newly installed password provider is displayed in the table of available password providers.
5. Select the check box in the "Status" column to use the password provider.

   The installed password provider is now active and can be used.
6. Set the preferred password input such that the password provider is used.

   See also: [Define the preferred password assignment](#define-the-type-of-password-assignment)

### Create a settings file for using password providers

To create a settings file for the use of password providers, proceed as follows:

1. Create an XML file with the content specified below. Use the coding "UTF-8".
2. In the setting tag with the name "EnablePasswordPreference", define whether a user can switch between manual password assignment and password assignment via a password provider.
3. In the setting tag with the name "PasswordPreference", define which type of password assignment is to be used.
4. Save the XML file.
5. Save the file named "CorporateSettings.xml" in the following directory on your computer:

   C:\ProgramData\Siemens\Automation\Portal V[Versionsnummer]\CorporateSettings\

   "[Version number]" stands for the corresponding product version, e.g. V19.

### Content of settings file

The settings file must have the following content:

XML

<?xml version="1.0" encoding="utf-8"?>

<Document>

<Settings.Settings ID="0">

<ObjectList>

<Settings.General ID="1" AggregationName="General">

<ObjectList>

<Settings.PasswordProviders ID="3" AggregationeName="PasswordProviders">

<AttributeList>

<EnablePasswordPreference>

<Value>true</Value>

</EnablePasswordPreference>

<DefaultPasswordPreference>

<Value>Advanced</Value>

</DefaultPasswordPreference>

</AttributeList>

</Settings.PasswordProviders>

</ObjectList>

</Settings.General>

</ObjectList>

</Settings.Settings>

</Document>

You specify the settings for the password provider in the element "Settings.PasswordProviders":

- The following values are possible for "EnablePasswordPreference":

  - "true": In the TIA Portal the user can switch between manual password assignment and password assignment via password providers.
  - "false": Switching between manual password assignment and password assignment via password providers is not possible in the TIA Portal.

  The default setting is "false".
- The following values are possible for "DefaultPasswordPreference":

  - "Manual": Assignment of passwords in the TIA Portal is done manually.
  - "Advanced": Passwords are assigned in the TIA Portal via a password provider.
  - "AdvancedWithManualFallback": Passwords are assigned in the TIA Portal via a password provider. If the password provider is not available, the protected block can be accessed via manual password input.

  The default setting is "Manual".

  If the "CorporateSettings.xml" file already exists and has different settings, supplement the element "Settings.PasswortProviders" in the "ObjectList>" element.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Show available password provider

You can display the password providers which are available in the TIA Portal.

### Requirement

Password assignment via password provider was defined using a settings file.

### Procedure

Proceed as follows to display the available password providers:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. In the area navigation, select the "Password provider > Available password providers" group.

   The available password providers are displayed in the overview table.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Recording activities of the password providers

In the event of problems in connection with connected password providers, you can record the activities of password providers. No passwords are recorded. You can then forward the recording to Customer Support for analysis.

### Requirement

A password provider is connected and activated.

### Activate recording of the activities of the password providers

Proceed as follows to activate the recording:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. In the area navigation, select the "Password providers > Analysis of the password providers" group.
3. Select the "Log activities of the password provider" check box.

   The text field for the storage location of the recording file and the "Browse" button become active.
4. Enter a storage location for the recording file or select it using the "Browse" button.

### Deactivate recording of the activities of password providers

Proceed as follows to deactivate recording:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. In the area navigation, select the "Password providers > Analysis of the password providers" group.
3. Deselect the "Log activities of the password provider" check box.

   The text field for the storage location of the recording file and the "Browse" button become inactive.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Define the type of password assignment

The TIA Portal offers the following options for the type of password assignment for blocks for know-how protection, copy protection and write protection:

- "Manual password input"

  With manual password input, you enter the password directly in the dialog for the password request.
- "Selection via password provider"

  With password input via an external password provider, you can select the password using a name from the list of available passwords. If the password provider is not available, it is not possible to set protection. The block can only be accessed later if there is a connection to the password provider.
- "Selection via password provider with manual input as fallback strategy for access"

  Like password input via an external password provider. If the password provider is not available and you know the password, you can, however, open the block for editing by entering the password manually.

Manual password input is the default setting.

### Requirement

The following requirements must be met in order that password assignment via an external password provider can be used

- Password assignment via password provider was defined using a settings file.
- The change of the type of password assignment was allowed in the settings file.
- A password provider is connected.

### Procedure

Proceed as follows to define the type of password assignment:

1. Select the "Settings" command in the "Options" menu.

   The "Settings" window is displayed in the work area.
2. In the area navigation, select the "Password provider > Password assignment" group.
3. Activate the desired type of password assignment.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Setting up and removing block copy protection (S7-1200, S7-1500)

For S7-1200 /1500 CPUs, you can set up copy protection which binds execution of the block to a specific CPU or a specific memory card. The block can then only be executed if it is in the device with the set serial number. If you want to add the serial number automatically through a download process, you must specify a copy protection password. This password is queried during a download process of the block. You can change the password without having to remove the know-how protection of the block. When you change the copy protection settings or remove the copy protection, the password is retained until the next compilation process.

It is important that you also know-how-protect any block for which you have set up copy protection. If you do not, anyone can reset the copy protection.

> **Note**
>
> **Note the following:**
>
> S7-1500 and S7-1200 V2.2 and higher: If you download a copy protected block to a device that does not match the specified serial number, the entire download operation will be rejected. This means that blocks without copy protection, too, will not be downloaded.

### Setting up copy protection

To set up copy protection for a block, follow these steps:

1. Open the properties of the block for which you wish to set up copy protection.
2. Select the "Protection" entry in the area navigation in the block properties.
3. Select either "Bind to serial number of the CPU" or "Bind to serial number of the memory card" from the drop-down list in the "Copy protection" area.
4. Enter either the serial number directly or enable the option "Serial number inserted when downloading to a device or memory card" if the serial number is to be inserted automatically when you load.

   Continue with step 7 if you have entered the serial number directly. If the serial number is to be added automatically during the download process, you must also execute steps 5 and 6.
5. Click "Define password".

   The "Define protection" dialog opens.
6. If you are using manual password input, enter the password in the fields "New password" and "Confirm password".
7. If you are using a password provider, first select the password provider and then the password.
8. Confirm your entries with "OK".

   The status box provides the information that a copy protection password is defined.
9. You can now set up the know-how protection for the block in the "Know-how protection" area, if the block does not already have know-how protection.

### Removing copy protection

To remove copy protection, follow these steps:

1. Open the properties of the block for which you wish to remove copy protection.
2. Select the "Protection" entry in the area navigation in the block properties.
3. Select "No binding" in the drop-down list in the "Copy protection" area.

**Note**

If the block has know-how protection, you must open the block with the correct password in order to be able to change the copy protection settings.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Setting up and removing block write protection

You can set up write protection for blocks of the type OB, FB, FC to prevent them from being changed unintentionally. Blocks with write protection can only be opened as "read only", the block properties can however still be edited.

Please note that write protection is not know-how protection, as you can remove write protection again at any time. If a block is write-protected, you cannot additionally set up know-how protection. Remove the write protection for the block if you want to set up know-how protection for it.

### Setting up write protection

To set write protection for a block, follow these steps:

1. Open the properties of the block for which you wish to set up write protection.
2. Select the "Protection" entry in the area navigation in the block properties.
3. In the area "Write protection" select "Define password".

   The "Define protection" dialog opens.
4. If you are using manual password input, enter the password in the fields "New password" and "Confirm password".
5. If you are using a password provider, first select the password provider and then the password.
6. Confirm your entries with "OK".

   The status box provides the information that a write protection password is defined. The text of the button changes to "Change password".
7. Select the "Write protection" check box.

   The "Access protection" dialog will open.
8. Enter the correct password or select the correct password if you are using a password provider.

   Write protection is enabled and will be active the next time the block is opened.

### Disabling write protection

Proceed as follows to disable write protection:

1. Open the properties of the block for which you wish to disable write protection.
2. Select the "Protection" entry in the area navigation in the block properties.
3. In the area "Write protection" select the "Write protection" check box.

   The "Access protection" dialog will open.
4. Enter the correct password or select the correct password if you are using a password provider.

   The write protection for the block is disabled the block can be edited again the next time the block is opened. The password is retained, so that you can enable write protection again at any time.

### Enable write protection.

Proceed as follows to enable write protection:

1. Open the properties of the block for which you wish to enable write protection.
2. Select "Protection" in the area navigation in the inspector window.
3. In the area "Write protection" select the "Write protection" check box.

   The "Access protection" dialog will open.
4. Enter the correct password or select the correct password if you are using a password provider.

   The write protection for the block is reset and will be active the next time the block is opened.

### Changing the write protection password

To change the write protection password, follow these steps:

1. Open the properties of the block for which you wish to change the write protection password.
2. Select the "Protection" entry in the area navigation in the block properties.
3. Click the "Change password" button.

   The "Change protection" dialog opens.
4. If you are using manual password input, enter the old password in the field "Old password" and the new password in the field "New password". Also enter the new password in the "Confirm password" box
5. If you are using a password provider, first select the password provider and then the new password.
6. Confirm your entries with "OK".

   The write protection password for the block is changed.

> **Note**
>
> It is always possible to change the write protection password for the block. This depends on whether write protection is active or not.

### Removing write protection

To set write protection for a block, follow these steps:

1. Open the properties of the block for which you wish to remove write protection.
2. Select the "Protection" entry in the area navigation in the block properties.
3. Click the "Change password" button.

   The "Change protection" dialog opens.
4. If you are using manual password input, enter the current password in the field "Old password".
5. If you are using a password provider, first select the password provider and then the current password.
6. Click "Remove"

   The write protection for the block is removed. Unlike deactivation of write protection, the password is also deleted.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Setting up block know-how protection

You can set up know-how protection for blocks in the devices in your project.

### Procedure

To set up block know-how protection, follow these steps:

1. Select the blocks with no know-how protection which you want to protect.
2. Select the command "Know-how protection" in the "Edit" menu.

   The "Define protection" dialog opens.
3. If you are using manual password input, enter the password in the fields "New password" and "Confirm password". Follow the valid password policies.

   See also: [Protecting blocks](#protecting-blocks-1)
4. If you are using a password provider, first select the password provider and then the password.
5. Confirm your entries with "OK".
6. Close the "Define protection" dialog with "OK".

### Result

The blocks selected will be know-how-protected. Know-how protected blocks are marked with a lock in the project tree. The password entered is valid for all blocks selected.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Opening know-how protected blocks

If the use of a password provider is set as the type of password assignment, the TIA Portal connects to the password provider when a protected block is opened. If the connection is successful, there is no need to enter a password. If the password provider is not available, you can only open the block fully if you had defined manual input as the fallback strategy and know the corresponding password. The name of the password is not sufficient here.

You can only open multiple know-how protected blocks at once if they are protected with the same password.

### Requirement

- "Manual password input" is set as the type of password assignment.
- "Selection via password provider with manual input as fallback strategy for access" is set and there is no connection to the password provider.

### Procedure

To open a know-how protected block, follow these steps:

1. Double-click on the block you wish to open.

   The "Access protection" dialog will open.
2. Enter the password for the know-how protected block.
3. Confirm your entry with "OK".

### Result

The know-how protected block will open provided you have entered the correct password. However, the block will remain know-how protected. If you copy the block or add it to a library, for example, the copies will also be know-how protected.

Once you have opened the block, you can edit the program code and the block interface of the block for as long as the block or TIA Portal is open. The password must be entered again the next time the block is opened. If you close the "Access protection" dialog with "Cancel", the block will open but the block code will not be displayed and you will not be able to edit the block.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Printing know-how protected blocks

You can only print complete know-how protected blocks if they have been opened with the correct password. If you print a closed block or if the block was not opened with the correct password, only the non-protected block data will be printed.

### Procedure

To print a know-how protected block in full, follow these steps:

1. Open the know-how protected block you wish to print.

   See also: [Opening know-how protected blocks](#opening-know-how-protected-blocks)
2. Select the "Print" command in the "Project" menu.

   The "Print" dialog will open.
3. Select the printer in the "Name" field.
4. Click "Advanced" to modify the Windows printer settings.
5. Select the documentation information set in the "Document information" drop-down list that you want to use for the frame layout.
6. Under "Print objects/area" select whether you want to print all objects or the complete area, or only a selection.
7. Under "Properties" select the print scope.

   - Select "All" to print the complete block.
   - Choose "Visible" to print all the information within the block that is visible on the screen.
   - Select "Compact" to print a shortened form of the block.
8. Click "Preview" to generate a print preview in advance.

   A print preview is created in the work area.
9. Click "Print" to start the printout.

---

**See also**

[Printing project contents](Editing%20project%20data.md#printing-project-contents)
  
[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Changing a password](#changing-a-password)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Changing a password

If you are using a password provider, whether you are able to change the password for know-how protected blocks depends on the specifications of the password provider.

### Procedure

To change the password, follow these steps:

1. Select the know-how protected blocks for which you want to change the password.
2. Select the command "Know-how protection" in the "Edit" menu.

   The "Change protection" dialog opens.
3. If you are using manual password input, enter the old password in the field "Old password" and the new password in the field "New password". Also enter the new password in the "Confirm password" box Follow the valid password policies.

   See also: [Protecting blocks](#protecting-blocks-1)
4. If you are using a password provider, first select the password provider and then the new password.
5. Close the "Change protection" dialog with "OK".

**Note**

You can only change the password for several blocks at once if all blocks selected have the same password.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Removing block know-how protection](#removing-block-know-how-protection)

## Removing block know-how protection

If you are using a password provider, whether you are able to remove the know-how protection of a block depends on the specifications of the password provider.

### Procedure

To remove block know-how protection, follow these steps:

1. Select the blocks for which you want to remove know-how protection.
2. Select the command "Know-how protection" in the "Edit" menu.

   The "Change protection" dialog opens.
3. If you are using manual password input, enter the password for know-how protection of the block in the field "Old password". This is not required if you are using a password provider.
4. Click the "Remove" button.

**Note**

You can only remove know-how protection for several blocks at once if all blocks selected have the same password.

### Result

Know-how protection will be disabled for the blocks selected.

---

**See also**

[Protecting blocks](#protecting-blocks-1)
  
[Connecting the password provider](#connecting-the-password-provider)
  
[Show available password provider](#show-available-password-provider)
  
[Recording activities of the password providers](#recording-activities-of-the-password-providers)
  
[Define the type of password assignment](#define-the-type-of-password-assignment)
  
[Setting up and removing block copy protection (S7-1200, S7-1500)](#setting-up-and-removing-block-copy-protection-s7-1200-s7-1500)
  
[Setting up and removing block write protection](#setting-up-and-removing-block-write-protection)
  
[Setting up block know-how protection](#setting-up-block-know-how-protection)
  
[Opening know-how protected blocks](#opening-know-how-protected-blocks)
  
[Printing know-how protected blocks](#printing-know-how-protected-blocks)
  
[Changing a password](#changing-a-password)
