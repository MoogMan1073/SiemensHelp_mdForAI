---
title: "Configuring user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: UserAdminWCCPenUS
topics: 61
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Setting up the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#setting-up-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Reference (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#reference-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Examples (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#examples-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Field of application of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Form of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#form-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Users work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [User groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [User groups work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Settings for the user administration (Basic Panels)](#settings-for-the-user-administration-basic-panels)
- [Settings for the user administration (Panels, Comfort Panels, RT Advanced)](#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)
- [Settings for the user administration (RT Professional)](#settings-for-the-user-administration-rt-professional)
- [Target groups in user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#target-groups-in-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Field of application of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Principle

The access protection controls access to data and functions in Runtime. This feature protects your applications against unauthorized operation. Safety-related operations are already limited to specific user groups when a project is being created. To this purpose you set up users and user groups that you equip with characteristic access rights, so-called authorizations. You then configure the authorizations required for operation of safety-related objects. Operators only have access, for example, to specific operator controls. Commissioners, for example, have unlimited access in Runtime.

#### Definition

You administer users, user groups and authorizations centrally in the user administration of WinCC. You transfer users and user groups together with the project to the HMI device. The users and passwords are managed on the HMI device in the User view.

#### Application example

You configure the "Service" authorization so that only service technicians have access to the configuration parameters. You assign the authorization to the "Service technician" user group. This allows all members of this group to set the protected configuration parameters.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Protection against incorrect operation**  Access protection does not protect against incorrect operations. It is your job to ensure that only authorized personnel with appropriate training will design, commission, operate and maintain plants and machines.  Access protection is not suitable for defining work routines and monitoring their observance. |  |

---

**See also**

[Form of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#form-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Target groups in user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#target-groups-in-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Objects with access protection (Panels, Comfort Panels, RT Advanced)](#objects-with-access-protection-panels-comfort-panels-rt-advanced)
  
[Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#central-user-administration-using-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button with logon dialog box (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-with-logon-dialog-box-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Form of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

In case of a project in manufacturing engineering, the environment at the equipment manufacturer has to be differentiated from the environment at the end customer as plant operator.

The equipment manufacturer allows users, for example Mr. Foreman, a specific access within the application or HMI device. However, a user Foreman does not exist at the end customer. The machine manufacturer cannot know the end users and the tasks they have to perform for configuration. The final users are usually set after commissioning at the end customer.

![Introduction](images/20284969867_DV_resource.Stream@PNG-en-US.png)

#### Principle

To minimize the work required for management, authorizations are assigned via user groups and not directly to individual users.

A user group assembles configured authorizations according to common jobs. For example, all permissions required for a service job are collected in a "Service technician" group. When you create a user who should be responsible for servicing, you simply assign him to the "Service technician" group.

The user view enables user administration in Runtime. Use user view to create, delete and assign an authorization to users in Runtime.

The user administration separates the administration of the users from the configuration of the authorizations. This ensures flexibility at the access protection.

Defaults can be set for the user administration during the configuration phase in the Engineering System.

---

**See also**

[Field of application of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can create users in the "Users" tab of the "User administration" editor and assign them to user groups. The "Users" tab is part of the user administration in WinCC.

#### Open

To open the "Users" tab, double-click "User administration" in the project window.

#### Work area

The users are managed in the work area:

- You create or delete users.
- You assign users to user groups.

  > **Note**
  >
  > You can assign a user to exactly one user group.

  > **Note**
  >
  > On an HMI device the number is limited to 100 users and one PLC user. This restriction does not apply to PCs. On a PC, the maximum number of users is restricted by the physical memory.

#### Inspector window

When you select a user, you can change the password in the "General" group. Under "Automatic logoff" you can specify if the user is to be automatically logged off by the HMI device when there is no operator activity after the specified time.

#### Backup and restore

The user data is encrypted and saved on the HMI device to protect it from loss due to power failure.

The users, passwords, group assignments and logoff times set up on the HMI device can be backed up and restored. This prevents you having to enter all of the data again on another HMI device.

> **Note**
>
> The currently valid user data is overwritten in the following cases:
>
> - Depending on settings, the next time the project is downloaded
> - Upon restore of a backed-up project
> - Upon import of the user administration via an operator control. The newly downloaded or restored user data and passwords take effect immediately.

> **Note**
>
> The user data from earlier Runtime versions can be backed up and restored in the V14.
>
> The user data of the V14 cannot be restored to earlier versions.

---

**See also**

[Field of application of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Users work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Basic Panels)](#settings-for-the-user-administration-basic-panels)
  
[Settings for the user administration (RT Professional)](#settings-for-the-user-administration-rt-professional)
  
[Objects with access protection (Panels, Comfort Panels, RT Advanced)](#objects-with-access-protection-panels-comfort-panels-rt-advanced)
  
[Settings for the user administration (Panels, Comfort Panels, RT Advanced)](#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)

### Users work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The "Users" work area lists the users and user groups in table form. You administrate the users and assign them to a user group.

#### Principle

The work area consists of the "Users" and "Groups" tables.

![Principle](images/122143415435_DV_resource.Stream@PNG-en-US.png)

The "Users" table shows the existing users. When you select a user in this table, the "Groups" table shows the user group to which the user belongs.

> **Note**
>
> For the user "Administrator", the default password is "administrator". For security reasons, you should change the password of this user.

---

**See also**

[User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Panels, Comfort Panels, RT Advanced)](#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)
  
[User groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Basic Panels)](#settings-for-the-user-administration-basic-panels)
  
[Settings for the user administration (RT Professional)](#settings-for-the-user-administration-rt-professional)

### User groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You can create users and authorizations in the "User groups" tab of the "User Administration" editor. The "User groups" tab is part of the user administration in WinCC.

#### Open

Double-click the "User administration" in the project window. Open the "User groups" tab.

#### Work area

The user groups and authorizations are managed in the work area:

- You create new user groups and authorizations or delete them.
- You assign the authorizations to the user groups.

#### Inspector window

When a user group or an authorization is selected, you can edit the name in the "General" group. You can also enter a brief description in the "Comment" group.

---

**See also**

[User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Panels, Comfort Panels, RT Advanced)](#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)
  
[Users work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Basic Panels)](#settings-for-the-user-administration-basic-panels)
  
[Settings for the user administration (RT Professional)](#settings-for-the-user-administration-rt-professional)

### User groups work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The "User groups" work area shows a table of the groups and their authorizations. You administer the user groups and assign authorizations to them.

#### Principle

The work area consists of the "Groups" and "Authorizations" tables.

![Principle](images/56037405067_DV_resource.Stream@PNG-en-US.png)

The "Groups" table shows the existing user groups. When you select a user group in this table, the "Active" column of the "Authorizations" table shows the authorizations which were assigned to the user group.

The number of the user group and of the authorization is assigned by the user administration. The designations and descriptions are assigned by you.

The number of predefined authorizations are fixed. Authorizations that you create can be freely edited. Ensure that the assigned numbers are unique.

---

**See also**

[User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Panels, Comfort Panels, RT Advanced)](#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)
  
[Users work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Basic Panels)](#settings-for-the-user-administration-basic-panels)
  
[Settings for the user administration (RT Professional)](#settings-for-the-user-administration-rt-professional)

### Settings for the user administration (Basic Panels)

#### Introduction

In the "Runtime settings &gt; User administration" editor, configure the security settings for users and their passwords in runtime.

#### Open

Double-click the "Runtime settings" editor in the project window. Click "User administration".

#### Work area

You carry out the settings for the validity of passwords in runtime in the work area. You determine the complexity of the password, for example.

> **Note**
>
> If the password from a previous project no longer corresponds to the guideline, the user is prompted to enter a new password.

#### Effects in Runtime

The security settings have the following effects in runtime, depending on the configuration.

- "General" group

  - "Enable limit for logon attempts" check box selected

    The number entered in the "Number of incorrect logon attempts" box defines the number of logon attempts a user is allowed before being assigned to the "Unauthorized" group.

    "Enable limit for logon attempts" check box not selected

    The user has an unlimited number of logon attempts in runtime.
  - "Number of incorrect logon attempts" field

    If you enter "4" in the field, for example, and the fourth logon attempt fails, the user is automatically assigned to the "Unauthorized" group.

    You can specify 1 to 9 attempts.
  - "Logon only with password" check box

    When the check box is selected, the user will be authenticated by the password. The user name is not required.

    To match users to passwords, you cannot configure passwords more than once.

    > **Note**
    >
    > If the "Logon only with password" option is enabled, the system resets the passwords for users that have already been created. We therefore recommend that you always enable the "Logon only with password" option before creating users.
    >
    > If you transfer user data from previous device versions in which the "Logon only with password" option was disabled, there might be multiple users with identical passwords. These users are listed in the user view. However, only users whose user name comes first by alphabetical order can log on in Runtime.
- "Hierarchy level" group

  - "Group-specific rights for user administration" check box

    When this check box is selected, administrators only manage users whose group number is less than or equal to their own.

    For example, an administrator whose group number is 5 can only manage users whose group number is less than or equal to 5. This means that the administrator can assign users only to groups with a group number less than or equal to 5.
- "Password" group

  - "Enable password aging" check box selected

    The password expires after the number of days set in the "Validity of the password (days)" field.

    The "Password aging" column is selected in the "User groups" editor. This enables you to specify group-by-group, if the passwords should expire or if the password generations should be saved. Passwords never expire for groups for which password aging is not enabled.
  - "Prewarning time (days)" field

    The user is informed that the password will expire the specified number of days before the password expires.
  - "Password generations" field

    If the user changes the password, the new password must be different from the specified number of previous password. The number of password generations ranges from 1 to 5.
- "Password complexity" group

  - "Must include special characters" check box selected

    The user must enter a password containing at least one special character at any position.
  - "Must include number" check box selected

    The user must enter a password containing at least one number at any position.
  - "Minimum password length" field

    The user must enter a password with a minimum length, as specified in the "Minimum password length" field.

    The minimum length of the password is 3 characters.
  > **Note**
  >
  > If the "Must include special characters" option is enabled, the system resets the passwords for users that have already been created. It is therefore recommended to always enable the "Must include special characters" option before creating users.
  >
  > The following special characters are permitted for passwords:
  >
  > -+.,/*:\"?_()=^!€%∼`§'{}[]&lt;&gt;#$;&amp;|@

---

**See also**

[User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Panels, Comfort Panels, RT Advanced)](#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)
  
[Users work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Settings for the user administration (Panels, Comfort Panels, RT Advanced)

#### Introduction

In the "Runtime settings &gt; User administration" editor, configure the security settings for users and their passwords at runtime.

#### Open

Double-click the "Runtime settings" editor in the project window. Click "User administration".

#### Work area

You carry out the settings for the validity of passwords in runtime in the work area. You determine the complexity of the password, for example.

> **Note**
>
> If the password from a previous project no longer corresponds to the guideline, the user is prompted to enter a new password.

#### Effects in Runtime

The security settings have the following effects in runtime, depending on the configuration.

- "General" group

  - "Change initial password" check box selected

    The user must change the administrator-assigned password when logging on for the first time.
  - "Change logoff time" checkbox selected

    Simple user rights are sufficient for changing the logoff time.

    The logoff time is the period after which the user administration automatically logs off a user when no operator activity is detected in the system.

    The logoff time for the SIMATIC Logon user must be enabled in the "Automatic logoff" tab.

    Any user changes of the logoff time are logged in the Audit Trail.
  - "Enable limit for logon attempts" check box selected

    The number entered in the "Number of incorrect logon attempts" box defines the number of logon attempts a user is allowed before being assigned to the "Unauthorized" group.

    "Enable limit for logon attempts" check box not selected

    The user has an unlimited number of logon attempts in runtime.
  - "Number of incorrect logon attempts" field

    If you enter "4" in the field, for example, and the fourth logon attempt fails, the user is automatically assigned to the "Unauthorized" group.

    You can specify 1 to 9 attempts.
  - "Logon only with password" check box

    When the check box is selected, the user will be authenticated by the password. The user name is not required.

    To match users to passwords, you cannot configure passwords more than once.

    > **Note**
    >
    > If the "Logon only with password" option is enabled, the system resets the passwords for users that have already been created. We therefore recommend that you always enable the "Logon only with password" option before creating users.
    >
    > If you transfer user data from previous device versions in which the "Logon only with password" option was disabled, there might be multiple users with identical passwords. These users are listed in the user view. However, only users whose user name comes first by alphabetical order can log on in Runtime.
- "Hierarchy level" group

  - "Group-specific rights for user administration" check box

    When this check box is selected, administrators only manage users whose group number is less than or equal to their own.

    For example, an administrator whose group number is 5 can only manage users whose group number is lower than or equal to 5. This means that the administrator can assign users only to groups with a group number lower than or equal to 5.
- "Password" group

  - "Enable password aging" check box selected

    The password expires after the number of days set in the "Validity of the password (days)" field.

    The "Password aging" column is selected in the "User groups" editor. This enables you to specify group-by-group, if the passwords should expire or if the password generations should be saved. Passwords never expire for groups for which password aging is not enabled.
  - "Prewarning time (days)" field

    The user is informed that the password will expire the specified number of days before the password expires.
  - "Password generations" field

    If the user changes the password, the new password must be different from the specified number of previous password. The number of password generations ranges from 1 to 5.
- "Password complexity" group

  - "Must include special characters" check box selected

    The user must enter a password containing at least one special character at any position.
  - "Must include number" check box selected

    The user must enter a password containing at least one number at any position.
  - "Minimum password length" field

    The user must enter a password with a minimum length, as specified in the "Minimum password length" field.

    The minimum length of the password is 3 characters.

    > **Note**
    >
    > If the "Must include special characters" option is enabled, the system resets the passwords for users that have already been created. We therefore recommend that you always enable the "Must include special characters" option before creating users.
    >
    > The following special characters are permitted for passwords:
    >
    > -+.,/*:\"?_()=^!€%∼`§'{}[]&lt;&gt;#$;&amp;|@
- "SIMATIC Logon" group

  - "Activate SIMATIC Logon" check box selected

    A connection is established to the server. Authorization is performed via SIMATIC Logon.
  - "Encrypted transfer" checkbox selected

    The data is encrypted before it is transferred to the server.

---

**See also**

[Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#central-user-administration-using-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)
  
[User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Users work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Basic Panels)](#settings-for-the-user-administration-basic-panels)
  
[Settings for the user administration (RT Professional)](#settings-for-the-user-administration-rt-professional)

### Settings for the user administration (RT Professional)

#### Introduction

In the "Runtime settings &gt; User administration", editor you specify whether users log on dynamically to an HMI device in runtime. You can also activate a central user administration by means of SIMATIC Logon.

#### Open

Double-click the "Runtime settings" editor in the project window. Click "User administration".

> **Note**
>
> The view of the work area depends on the HMI device in use.

#### Work area

In the work area, you can specify how the operator logs on to the HMI device:

- Dynamic logon

  With dynamic logon, you assign a variable to each HMI device. A variable value is assigned to a user. The user then logs on in runtime by setting the variable value on an HMI device, for example, using a key switch.
- SIMATIC Logon

  When you use SIMATIC Logon, you specify the display name that is shown on the HMI device. SIMATIC Logon supports centralized user administration. As soon as you select the "SIMATIC Logon" option, the users created in the "User administration" editor will be ignored. The "Users" work area is no longer displayed.

  Only groups whose settings agree with the names of the Windows groups are important.

  > **Note**
  >
  > If you use SIMATIC Logon , you cannot use the "Automatic Logon" option.

#### Effects in Runtime

With dynamic logon, the user is logged on to the HMI device as soon as the variable contains the correct value.

The set automatic logoff time does not affect users that log on via a logon tag.

When SIMATIC Logon is used, the operator logs on to the Windows operating system. The user settings, such as the password validity, are read by SIMATIC Logon from the user administration of the operating system.

---

**See also**

[User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Settings for the user administration (Panels, Comfort Panels, RT Advanced)](#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)
  
[Users work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User groups work area (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-groups-work-area-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on users dynamically (RT Professional)](#logging-on-users-dynamically-rt-professional)
  
[Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#central-user-administration-using-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)

### Target groups in user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Principle

The target groups serve as examples for different groups of persons who use the user administration. We can distinguish between the following four groups in the user administration:

1. Administrator OEM
2. Administrator RT
3. Project engineer
4. Operator

As Administrator OEM, you create the user groups, users and authorizations for Runtime in the Engineering System of, for example, an equipment manufacturer.

As Administrator RT, you administer users in Runtime by means of the "User view."

As the project engineer, you assign the authorizations to the user groups in the Engineering System. You also configure authorizations for objects.

As Operator, you log on in Runtime. You can only access a protected object if you have the required authorization.

> **Note**
>
> The Administrator RT target group already exists in the Runtime user administration as the predefined user group "Administrator group." For ease of understanding, the predefined user groups and authorizations are not used below.

---

**See also**

[Field of application of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Objects with access protection (Panels, Comfort Panels, RT Advanced)](#objects-with-access-protection-panels-comfort-panels-rt-advanced)

## Setting up the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Administering users for Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#administering-users-for-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing users on the server (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-users-on-the-server-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Administering users for Web Client (RT Professional)](#administering-users-for-web-client-rt-professional)
- [Administering users in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#administering-users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Administering users for Runtime  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating a user group (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-user-group-basic-panels-panels-comfort-panels-rt-advanced)
- [Creating a user group (RT Professional)](#creating-a-user-group-rt-professional)
- [Assigning an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-users-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Assigning a user to a user group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-a-user-to-a-user-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-users-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Managing user groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Changing the number of the user group (Basic Panels, Panels, Comfort Panels, RT Advanced)](#changing-the-number-of-the-user-group-basic-panels-panels-comfort-panels-rt-advanced)
- [Logging on users dynamically (RT Professional)](#logging-on-users-dynamically-rt-professional)

#### Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You create an authorization and assign it to one or more user groups.

##### Requirements

The "User groups" work area is open.

##### Procedure

1. Double-click "Add" in the "Authorizations" table.
2. Enter "Stop runtime" as the name of the authorization.
3. Enter a brief description as the "Comment".

---

**See also**

[Creating a user group (RT Professional)](#creating-a-user-group-rt-professional)
  
[Assigning an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-users-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Assigning a user to a user group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#assigning-a-user-to-a-user-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-users-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on using SIMATIC Logon (Panels, Comfort Panels, RT Advanced)](#logging-on-using-simatic-logon-panels-comfort-panels-rt-advanced)
  
[Logging on users dynamically (RT Professional)](#logging-on-users-dynamically-rt-professional)
  
[Access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Target groups in user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#target-groups-in-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing users for the Web client (RT Professional)](#managing-users-for-the-web-client-rt-professional)
  
[Logging on using SIMATIC Logon (RT Professional)](#logging-on-using-simatic-logon-rt-professional)
  
[Creating a user group (Basic Panels, Panels, Comfort Panels, RT Advanced)](#creating-a-user-group-basic-panels-panels-comfort-panels-rt-advanced)
  
[Managing user groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-user-groups-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Changing the number of the user group (Basic Panels, Panels, Comfort Panels, RT Advanced)](#changing-the-number-of-the-user-group-basic-panels-panels-comfort-panels-rt-advanced)

#### Creating a user group (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

User groups are created so that you do not have to assign an authorization to every single user. You create a user group, assign authorizations and then assign users to it.

> **Note**
>
> The name of the user group has to be unique within the project. Otherwise the input is not accepted.

> **Note**
>
> **Using SIMATIC Logon**
>
> Ensure that the names of the user groups in Windows and WinCC are identical.

##### Requirements

The "User groups" work area is open.

##### Procedure

1. Double-click "Add" in the "Groups" table.
2. Enter "Operators" as the "Name" of the user group.
3. Change the "Number" of the user group as required.
4. Enter "Display name" of the "Operators" user group.
5. Enter a brief description as the "Comment".

In runtime, the user view shows the display name of the user group. The display name of the user group depends on the language. You can specify the name in several languages and switch between languages in runtime.

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating a user group (RT Professional)

##### Introduction

User groups are created so that you do not have to assign an authorization to every single user. You create a user group, assign authorizations and then assign users to it.

> **Note**
>
> **Using SIMATIC Logon**
>
> Ensure that the names of the user groups in Windows and WinCC are identical.

> **Note**
>
> The name of the user group has to be unique within the project. Otherwise the input is not accepted.

##### Requirements

The "User groups" work area is open.

##### Procedure

1. Double-click "Add" in the "Groups" table.
2. Enter "Operators" as the name of the user group.
3. Change the "Number" of the user group as required.
4. Enter a brief description as the "Comment."

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you allocate an authorization to a user group, all assigned users have this authorization.

##### Requirements

- A "Stop runtime" authorization has been created.
- An "Operators" user group has been created.
- The "User groups" work area is open.

##### Procedure

1. Click on the "Operators" user group in the "Groups" table. The "Authorizations" table shows all authorizations.
2. Enable the "Stop runtime" authorization in the "Authorizations" table.

**Note**

The "Stop runtime" authorization is only a designation and does not have any relation to the function "StopRuntime". You have to establish this relation yourself. To do so, configure the "StopRuntime" system functions at a button and select "Stop runtime" as the "Authorization".

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Creating users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You create a user so that users can log on with their user names in runtime after loading to the device.

As an alternative, you can create and change users by means of the "User view" in Runtime.

> **Note**
>
> Applies only to Runtime Professional:
>
> New users who want to access through a Web client or a WebUX client on the system, can only be created in the engineering system.
>
> When you create a user in Runtime with the user view, it is not possible to assign a Web startup screen to this user. This user is therefore not authorized to access the Web.
>
> Neither can existing users be granted web access rights in Runtime.

In order for a created user to have authorizations you have to assign them to a user group and allocate authorizations to the user group.

The logon is successful when the user name entered during the logon matches a user in Runtime. In addition, the entered password must agree with the stored password of the user.

> **Note**
>
> Note that the entry is case-sensitive.

##### Requirements

The "Users" work area is open.

##### Procedure

1. Double-click "Add" in the "Users" table.
2. Enter "Foreman" as the user name.
3. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Password" column. A dialog box for entering the password is displayed.
4. Enter the password of the user.
5. To confirm the password, enter it a second time in the lower field.
6. Close the dialog box using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
7. If a user is to be logged off after a specific time period, activate "Automatic logoff".
8. Click in the "Logoff time" column. The preset value for "Logoff time" is 5 minutes.
9. Enter a brief description as the "Comment".

**Note**

The user name must be unique within the project. Otherwise the input is not accepted.

**Note**

Do not use special characters such as / " § $ % ? ' &amp; when you enter a user name and a password.

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Assigning a user to a user group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you assign a user to a user group, the user has the authorizations of the user group.

> **Note**
>
> You have to assign a user to exactly one user group. The assignment is checked during the consistency check and generation of the project.

##### Requirements

- The user "Foreman" has been created.
- An "Operators" user group has been created.
- The "Users" work area is open.

##### Procedure

1. Click on the "Foreman" user in the "Users" table. The "Groups" table shows all user groups.
2. Activate the "Operators" user group in the "Groups" table.

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Managing users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In the work area, you can administer users and assign them to user groups.

##### Requirements

The "Users" work area is open.

##### Changing the user name

1. In the "Users" table, double-click the field in the "Name" column to change the user name.
2. Change the user name.
3. Confirm your entry with &lt;Return&gt;.

Alternatively, select the user in the work area. Change the user name under "Properties &gt; Properties &gt; General" in the Inspector window.

##### Changing the password of the user

1. Click the ![Changing the password of the user](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Password" column of the "Users" table. A dialog box for entering the password opens.
2. In the "Enter password" field, enter the new password.
3. Enter the new password again in the "Confirm password" field.
4. Confirm your entry with &lt;Return&gt;.

Alternatively, select the user in the work area. Change the password under "Properties &gt; Properties &gt; General" in the Inspector window.

##### Displaying invisible columns

1. Position the mouse cursor on the title of the "Users" table.
2. Right-click to open the shortcut menu and enable the display of the "Logoff time" column, for example.

##### Changing the logoff time of the user

1. In the "Users" area, double-click on the field in the "Logoff time" column to change the logoff time.
2. Change the logoff time.
3. Confirm your entry with &lt;Return&gt;.

Alternatively, select the user in the work area. Change the logoff time under "Properties &gt; Properties &gt; Automatic logoff" in the Inspector window.

##### Deleting a user

1. Select the line of the user to be deleted.
2. Open the shortcut menu with the right mouse button and select the "Delete" command.

**Note**

Predefined users cannot be deleted.

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Managing user groups (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In the workplace you administer user groups and assign authorizations for use in runtime.

##### Requirements

The "User groups" work area is open.

##### Changing the name of the user group

1. In the "Groups" table, double-click the field in the "Name" column to change the name of the user group.
2. Change the name of the user group.
3. Confirm your entry with &lt;Return&gt;.

Alternatively, select the user group in the work area. Change the name under "Properties &gt; Properties &gt; General" in the Inspector window.

> **Note**
>
> Predefined user groups cannot be deleted.

##### Displaying invisible columns

1. Position the mouse cursor on the title of the "Users" table.
2. Right-click to open the shortcut menu and enable the display of the "Display name" column, for example.

##### Changing the displayed name of the user group

1. In the "Groups" table, double-click the field in the "Display name" column to change the display name of the user group.
2. Change the displayed name of the user group.
3. Confirm your entry with &lt;Return&gt;.

Alternatively, select the user group in the work area. Change the display name under "Properties &gt; Properties &gt; General" in the Inspector window.

##### Deleting a user group

1. Mark the line of the user group to be deleted.
2. Open the shortcut menu with the right mouse button and select the "Delete" command.

**Note**

Predefined user groups cannot be deleted.

##### Changing the name of the authorization

1. In the "Authorizations" table, double-click the field in the "Name" column to change the name of the authorization.
2. Change the name of the authorization.
3. Confirm your entry with &lt;Return&gt;.

Alternatively, select the authorization in the work area. Change the name under "Properties &gt; Properties &gt; General" in the Inspector window.

##### Deleting authorizations

1. Mark the line of the authorization to be deleted.
2. Open the shortcut menu with the right mouse button and select the "Delete" command.

**Note**

Predefined authorizations cannot be deleted.

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Changing the number of the user group (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

To assign group-specific rights, edit the number of a user group.

##### Requirements

- In the "Runtime settings&gt; User administration" editor, "Group-specific rights for user administration" is selected.
- The "Operator" user group has been created.
- A "User administration" authorization has been assigned.
- The "User groups" work area is open.

##### Procedure

1. Click on the "Operator" user group in the "Groups" table.
2. Enter "6" in the "Number" column of the user group.
3. Enable the "User administration" authorization in the "Authorizations" table.

##### Result

The members of the "Operator" user group can only manage users whose group number is less than or equal to 6.

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Logging on users dynamically (RT Professional)

##### Introduction

Two configuration steps are required to allow "Dynamic logon":

1. Assign an HMI device to a configured variable.
2. Assign a specific variable value to a user.

**Note**

If you have activated SIMATIC Logon, dynamic logon is not possible.

##### Requirements

- User administration exists.
- A "Login" variable of the "Byte" type is created.
- The user that has been added or downloaded has a password.

##### Procedure

**Assignment of the HMI device to the variable**

1. Double-click "Runtime settings &gt; User administration" in the project window.
2. Double-click "Add" in the "Dynamic logon" area of the table.
3. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "HMI device" column. A dialog box for selecting the HMI device opens.
4. Select an HMI device.
5. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Variable" column. A dialog box for selecting the variable opens.
6. Select the "Login" variable.

**Assignment of the user to the variable value**

1. Open the "Users" work area.
2. Position the mouse cursor on the title of the "Users" table.
3. Open the shortcut menu with the right mouse button and activate the display of the "Dynamic logon" and "User identification" columns.
4. Double-click "Add" in the "Users" table.
5. Enter "Smith" as the user name.
6. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Password" column. A dialog box for entering the password is displayed.
7. Enter the password of the user.
8. To confirm the password, enter it a second time in the lower field.
9. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
10. Activate the "Dynamic logon" column.

##### Result

When the variable equals 1, the user "Smith" will be logged on.

> **Note**
>
> The used variable must be of the type "binary" or 8, 16 or 32 bit.

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Managing users on the server (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#central-user-administration-using-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)
- [Authentication and certificate management in SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#authentication-and-certificate-management-in-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)
- [Making settings on the server (Panels, Comfort Panels, RT Advanced, RT Professional)](#making-settings-on-the-server-panels-comfort-panels-rt-advanced-rt-professional)
- [Logging on using SIMATIC Logon (Panels, Comfort Panels, RT Advanced)](#logging-on-using-simatic-logon-panels-comfort-panels-rt-advanced)
- [Logging on using SIMATIC Logon (RT Professional)](#logging-on-using-simatic-logon-rt-professional)

#### Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

To manage users and user groups for several applications or HMI devices, activate SIMATIC Logon.

##### Principle

SIMATIC Logon is a tool for system-wide user administration. If you use SIMATIC Logon, the users are centrally managed outside the application or HMI device.

You configure the user groups and their permissions as you usually do with the local user administration in WinCC. You assign identical names to the user groups on the server and in WinCC. Authorizations are assigned in runtime to a user group when the names are identical.

You do not have to create users in WinCC because they are taken dynamically from Windows user management during the logon process. The application or HMI device forwards each logon or password change to SIMATIC Logon for processing.

> **Note**
>
> SIMATIC Logon is a product requiring a license. For more information on SIMATIC Logon go to &lt;http://support.automation.siemens.com&gt;.
>
> Enter the ID "34519648" in the search field and start searching. The "SIMATIC Logon - Electronic Signature" manual is available to download.

##### Log on process via SIMATIC Logon Service

The following diagram illustrates the process that runs automatically when a user logs onto Runtime.

![Log on process via SIMATIC Logon Service](images/121081626507_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Field of application of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Making settings on the server (Panels, Comfort Panels, RT Advanced, RT Professional)](#making-settings-on-the-server-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on using SIMATIC Logon (Panels, Comfort Panels, RT Advanced)](#logging-on-using-simatic-logon-panels-comfort-panels-rt-advanced)
  
[Logging on using SIMATIC Logon (RT Professional)](#logging-on-using-simatic-logon-rt-professional)
  
[Settings for the user administration (Panels, Comfort Panels, RT Advanced)](#settings-for-the-user-administration-panels-comfort-panels-rt-advanced)
  
[Authentication and certificate management in SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#authentication-and-certificate-management-in-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)

#### Authentication and certificate management in SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

SIMATIC Logon (V1.5 SP3 and later) supports secure encrypted communication connections to the following device families as of device version V13 SP1 and higher:

- Comfort Panels
- KTP Mobile Panels
- Runtime Advanced

> **Note**
>
> HMI devices with a device version V13 or earlier can only make a non-secure / non-encrypted connection to a SIMATIC Logon server.

##### Basics

The first time a connection is made the SIMATIC Logon certificate is compared with the local certificate of the HMI device. The compared certificate is stored under "SimaticLogon\rejected". If you trust the certificate of the SIMATIC Logon server, copy the stored certificate into the local certificate store.

The certificate store is located in the following path:

- On the PC usually under "C:\Program Files\Siemens\CoRtHmiRtm\SimaticLogon\certs"
- On HMI panels under "\flash\simatic\SimaticLogon\certs"

When the comparison has been successfully performed can a secure encrypted connection be successfully established.

You can find additional information about tested browsers on the Internet on the Customer Support pages, entry ID=109480490:

- [https://support.industry.siemens.com/cs/document/109480490/](https://support.industry.siemens.com/cs/de/de/view/109480490)

---

**See also**

[Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#central-user-administration-using-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)

#### Making settings on the server  (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Perform the following steps on your sever to ensure correct operation of SIMATIC Logon.

##### Procedure

1. Install SIMATIC Logon Services.
2. Create the user group in the user administration of the operating system.
3. Create the users in the user administration of the operating system.
4. Assign the new users to a group.
5. Transfer the licenses for each HMI device on the server.

**Note**

Users of SIMATIC Logon must be members of a user group of the operating system. Members of a subgroup cannot be logged on.

> **Note**
>
> You can find more detailed information in the documentation supplied with SIMATIC Logon.

> **Note**
>
> The password policies stored on the server are valid if users are authorized by means of SIMATIC Logon.

> **Note**
>
> You can configure the logoff time for the SIMATIC Logon user with "Configure SIMATIC Logon" on the server.
>
> You set the automatic logoff time identical for all users, regardless of the panels.

---

**See also**

[Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#central-user-administration-using-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)

#### Logging on using SIMATIC Logon (Panels, Comfort Panels, RT Advanced)

##### Requirements

- User administration exists.
- The groups created in WinCC agree with the Windows groups on the server.
- There is a server with SIMATIC Logon Service installed.

> **Note**
>
> A user may only be a member of one user group in WinCC. When a user is a member of several user groups on the server, only one of these user groups can be made known in WinCC.
>
> "Administrators" and "Users" are predefined groups in both Windows and WinCC. Any new user created in Windows is automatically a member of the "Users" group. A user will be a member of two groups if assigned to a new group, for example, to the "SL user" group.
>
> Remove this user from the "Users" group of the operating system to enable logon of this user using SIMATIC Logon.
>
> A system message in runtime always confirms the successful logon of a user on the server.

> **Note**
>
> When you use SIMATIC Logon to manage access to a panel or a device with WinCC Runtime Advanced, you must note that the characters '/' and '\' cannot be used in the names of Windows user groups or Windows users.

##### Procedure

1. Open the "Runtime settings &gt; User administration" editor in the Project window.
2. Select "Enable SIMATIC Logon".
3. Select "Windows domain" or "Windows computer", depending on where you administer your users.
4. Enter the name or IP address of the SIMATIC Logon server in the "Server name" text box.
5. Enter the port number for TCP/IP communication in the "Port number" text box. The valid range of values lies between 1024 and 49151. The preset port number is "16389" and used by SIMATIC Logon as the default.
6. Enter the Windows domain or the logon server with the user data in the "Windows domain" text box.

   Enter the name of the sever to access users on the logon server.

   Enter the name of the domain if the logon sever is in a domain and you wish to access users of the domain.
7. Activate the "Encrypted transfer" check box in order to encrypt the data before sending it to the server.

**Note**

Make sure your SIMATIC Logon Server always has the same IP address if you use IP addresses.

**Note**

Local Windows users are not accepted when the logon server is in a domain.

##### Emergency user

If the server cannot be accessed, all local users that were created in WinCC user administration can also be used as emergency users.

Emergency users have the rights of the user group to which they were assigned.

> **Note**
>
> For additional information, refer to the included SIMATIC Logon documentation.
>
> Can be located under: [Installation directory SIMATIC Logon] \manuals

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#central-user-administration-using-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)

#### Logging on using SIMATIC Logon (RT Professional)

##### Requirements

- User administration exists.
- The groups created in WinCC agree with the Windows groups on the server.
- There is a server with SIMATIC Logon Service installed.

> **Note**
>
> When a user is a member of several user groups, the user is assigned the sum of authorizations for the groups. Logon is possible.

##### Procedure

1. Double-click the "Runtime settings" in the project window.
2. Double-click the "User administration" in the work area.
3. Activate "SIMATIC Logon."

---

**See also**

[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Central user administration using SIMATIC Logon (Panels, Comfort Panels, RT Advanced, RT Professional)](#central-user-administration-using-simatic-logon-panels-comfort-panels-rt-advanced-rt-professional)

### Administering users for Web Client (RT Professional)

This section contains information on the following topics:

- [Administering user groups for Web Client (RT Professional)](#administering-user-groups-for-web-client-rt-professional)
- [Managing users for the Web client (RT Professional)](#managing-users-for-the-web-client-rt-professional)

#### Administering user groups for Web Client (RT Professional)

##### Introduction

For each user group to be administered for web clients, you must configure the following:

- A start screen of your choice enabled for web access
- A language of your choice
- Number of reserved licenses (for WebUX)

This allows you to make various sections of a project immediately accessible or inaccessible for users.

> **Note**
>
> The name of the user group has to be unique within the project. Otherwise the input is not accepted.

##### Requirements

- The "Start" screen has been created and the web access is activate.
- The selected project language is activated.
- The "Web operators" user group has been created.

##### Procedure

1. Double-click the "Runtime settings" editor in the project window.
2. Click "User administration".
3. In the "User groups" tab, select the user group "Web operators".
4. In the Inspector window, select "Properties &gt; Properties &gt; Web options".
5. Under "WebNavigator settings", click the ![Procedure](images/30890839819_DV_resource.Stream@PNG-de-DE.png) button in the "Start screen" selection list.

   A dialog box for selecting the start screen opens.
6. Select the "Start" screen for runtime.
7. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
8. Repeat steps 5 to 7 to set a start screen for WebUX.
9. To configure a language for the user group, click the ![Procedure](images/84609363851_DV_resource.Stream@PNG-de-DE.png) button under "Options" in the "Web language" selection list.

   A dialog box for selecting the language opens.
10. Select the desired language as the runtime language of the user group.

Alternatively, you can make these settings in the shortcut menu by selecting the columns "WebNavigator start screen", "WebUX start screen" and "Web language" and making the respective configuration.

> **Note**
>
> The name of the user group is language-dependent. You can specify the name in several languages and switch between languages in runtime.

---

**See also**

[Managing users for the Web client (RT Professional)](#managing-users-for-the-web-client-rt-professional)
  
[Basics (RT Professional)](WinCC%20WebUX%20%28RT%20Professional%29.md#basics-rt-professional)
  
[Licensing (RT Professional)](WinCC%20WebUX%20%28RT%20Professional%29.md#licensing-rt-professional)

#### Managing users for the Web client  (RT Professional)

##### Introduction

You must configure the following for each user to be logged on to the Web client (WebNavigator or WebUX):

- A start screen of your choice enabled for web access
- A language of your choice
- Number of reserved licenses (for WebUX)

This allows you to make various sections of a project immediately accessible or inaccessible for users.

> **Note**
>
> New users who want to access through a Web client or a WebUX client on the system, can only be created in the engineering system.
>
> When you create a user in Runtime with the user view, it is not possible to assign a Web startup screen to this user. This user is therefore not authorized to access the Web.
>
> Neither can existing users be granted web access rights in Runtime.

##### Requirements

- The "Start" screen has been created and the web access is activate.
- The selected project language is activated.

##### Procedure

1. Double-click the "Runtime settings" editor in the project window.
2. Click "User administration".
3. In the "Users" tab, select a user for whom you want to make the settings.
4. In the Inspector window, select "Properties &gt; Properties &gt; Web options".
5. Under "WebNavigator settings", click the ![Procedure](images/30890839819_DV_resource.Stream@PNG-de-DE.png) button in the "Start screen" selection list.

   A dialog box for selecting the start screen opens.
6. Select the "Start" screen.
7. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
8. Repeat steps 5 to 7 to set a start screen for WebUX.
9. Under "Reserved number of licenses", you configure the number of reserved WebUX licenses for the selected user using the ![Procedure](images/84603730955_DV_resource.Stream@PNG-de-DE.png) button.
10. To configure a language for the user, click the ![Procedure](images/84609363851_DV_resource.Stream@PNG-de-DE.png) button under "Options" in the "Web language" selection list.

    A dialog box for selecting the language opens.
11. Select the desired language as the runtime language of the web user.

**Note**

If more reserved licenses are configured than are available on the WebUX server, only the first users listed under the user administration are taken into consideration.

**Note**

If the "Use WebNavigator licenses for WebUX" option is selected, no reserved WebUX licenses can be guaranteed.

Alternatively, you can make these settings in the shortcut menu by selecting the columns "WebNavigator start screen", "WebUX start screen" and "Web language" and "Licenses reserved for WebUX" and making the respective configuration.

> **Note**
>
> The language setting is retained when the user becomes part of a new group. However, the start screen is overwritten.

> **Note**
>
> By default, the WebNavigator licenses are used for WebUX. If you want to use these licenses separately, clear the "Use WebNavigator licenses for WebUX" check box under "Runtime settings &gt; Web access".

> **Note**
>
> Users can now also log off manually from the WebNavigator client using the ODK function "PWRTLogout()". You can find one description of the function in the Runtime API documentation under "Functions of the user administration &gt; Functions for logon, logoff".

---

**See also**

[Administering user groups for Web Client (RT Professional)](#administering-user-groups-for-web-client-rt-professional)
  
[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Licensing (RT Professional)](WinCC%20WebUX%20%28RT%20Professional%29.md#licensing-rt-professional)
  
[Basics (RT Professional)](WinCC%20WebUX%20%28RT%20Professional%29.md#basics-rt-professional)

### Administering users in Runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [User view (Panels, Comfort Panels, RT Advanced, RT Professional)](#user-view-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring a user view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-user-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Creating users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-users-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Managing users in the complex user view (Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-users-in-the-complex-user-view-panels-comfort-panels-rt-advanced-rt-professional)
- [Unlock locked out users (Basic Panels, Panels, Comfort Panels, RT Advanced)](#unlock-locked-out-users-basic-panels-panels-comfort-panels-rt-advanced)
- [Logging on as a user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-on-as-a-user-basic-panels-panels-comfort-panels-rt-advanced)
- [Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)
- [Exporting the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-the-user-administration-panels-comfort-panels-rt-advanced-rt-professional)
- [Importing the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-the-user-administration-panels-comfort-panels-rt-advanced-rt-professional)

#### Users in runtime  (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Principle

You create users and user groups and assign authorizations to them. You configure objects with authorizations. After download to the HMI device, all objects which were configured with an authorization are protected against unauthorized access in Runtime.

##### User view

When you configure a user view in the Engineering System, you administer users in this user view following download to the HMI device.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| Changes in the user view are effective immediately in Runtime. Changes in runtime are not updated in the engineering system. When downloading the user administration to the HMI device, all changes in the user view are overwritten after a security prompt and based on the settings. |  |

Users who have a "User administration" authorization have unlimited access to the user view. This allows them to administer all users. Any other user has only limited access to the user view for self administration.

---

**See also**

[Configuring a user view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-user-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-users-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Logging on as a user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-on-as-a-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Exporting the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-the-user-administration-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-the-user-administration-panels-comfort-panels-rt-advanced-rt-professional)
  
[Access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Target groups in user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#target-groups-in-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Unlock locked out users (Basic Panels, Panels, Comfort Panels, RT Advanced)](#unlock-locked-out-users-basic-panels-panels-comfort-panels-rt-advanced)
  
[User view (Panels, Comfort Panels, RT Advanced, RT Professional)](#user-view-panels-comfort-panels-rt-advanced-rt-professional)
  
[Managing users in the complex user view (Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-users-in-the-complex-user-view-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

#### User view (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Purpose

You configure a user view in the engineering system to also administer the users in Runtime.

##### Structure

The user view shows the following in each line:

- The user
- Their encrypted password
- The corresponding user group
- The logoff time

If no user is logged on, the user view is empty. The content of the individual fields is displayed after logon.

##### User view of an administrator

![User view of an administrator](images/75049743371_DV_resource.Stream@PNG-en-US.png)

When an administrator is logged on, the user view shows all the users. The administrator changes the user name and the password. The administrator creates new users and assigns them to an existing user group.

##### User view of a user

![User view of a user](images/75055159819_DV_resource.Stream@PNG-en-US.png)

When no administrator is logged on, the user view shows only the logged-on user. Users can change their own password and logoff time.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

#### Configuring a user view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You configure a user view in the Engineering System to also administer users in Runtime.

##### Requirements

A screen has been created.

##### Procedure

1. Select the "User view" object from the "Controls" category in the toolbox.
2. Drag-and-drop the "User view" object into the screen.
3. Click on "Properties &gt; Properties" in the Inspector window.
4. Specify the appearance of the "User view".
5. You can, for example, select " "Display mode &gt; Fit to size &gt; Fit object to contents".

##### Result

You have created a user view in the screen.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

#### Creating users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You create a user so that users can log on under their user name in runtime.

As an alternative, you can create users in the engineering system and download them to the HMI device.

> **Note**
>
> Applies only to Runtime Professional:
>
> New users who want to access through a Web client or a WebUX client on the system, can only be created in the engineering system.
>
> When you create a user in Runtime with the user view, it is not possible to assign a Web startup screen to this user. This user is therefore not authorized to access the Web.
>
> Neither can existing users be granted web access rights in Runtime.

The logon is successful only when the user name entered during the logon matches a user in runtime. In addition, the password entered at logon has to match that of the user.

> **Note**
>
> Note that the entry is case-sensitive.

> **Note**
>
> Do not use special characters such as / " § $ % ? ' &amp; when you enter a user name and a password.

You assign the user to a user group. The user then has the authorizations of the user group.

> **Note**
>
> Runtime users must be assigned to a user group. The user group is created in the engineering system. The designation of the user group is language-dependent.

##### Requirements

- The user view is open.
- A "Group 2" user group has been created.

##### Procedure

1. Click "&lt;New User&gt;" in the user view. A dialog opens.
2. Enter "Foreman" as the user name.
3. Press the &lt;Return&gt; button.
4. Click "Password".
5. Enter the password of the user.
6. Press the &lt;Return&gt; button. The password is hidden.
7. Click in the "Group" column.
8. Select "Group 2" as the "Group".

   ![Procedure](images/74766056203_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/74766056203_DV_resource.Stream@PNG-en-US.png)
9. Press the &lt;Return&gt; button.
10. Click in the "Logoff time" column.
11. Enter the time after which the user is logged off automatically.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

#### Managing users in the complex user view (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

If you have configured a user view in the engineering system, the users and user groups can be managed in runtime.

> **Note**
>
> Changes in the user view are effective immediately in runtime. Changes in runtime are not updated in the engineering system. When downloading the user administration to the HMI device, all changes in the user view are overwritten after a security prompt and based on the settings.

##### Requirements

- Runtime is enabled.
- A complex user view has been created.
- The screen with the user view is open.
- You have the default "User administration" authorization.

  > **Note**
  >
  > If you do not have a "User administration" authorization, you can only change your own password and your logoff time.

##### Changing the user name

1. Enter a new user name in the "Users" column in the user display.
2. Confirm your entry with &lt;Return&gt;.

**Note**

The user can then no longer log on with their previous password in runtime. If you delete the name and press &lt;Return&gt;, the user is deleted.

##### Changing the password of the user

Availability of complex user display in selected devices only.

1. Enter a new password in the "password" column in the user display.
2. Confirm your entry with &lt;Return&gt;.

**Note**

The user can then no longer log on with his previous password in runtime.

If you delete the password in the complex user view and press &lt;Return&gt;, the user will be deleted.

##### Changing the logoff time of the user

1. Enter a new logoff time in the "Logoff time" column in the user display.
2. Confirm your entry with &lt;Return&gt;.

##### Deleting a user

1. Click the name of the user to be deleted.
2. Delete the name.
3. Press the &lt;Return&gt; button.

**Note**

The user can no longer log on in runtime.

##### Assigning a user to a different user group

1. Activate the user group field for the corresponding user.
2. Select a user group.
3. Confirm your selection with &lt;Return&gt;.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

#### Unlock locked out users (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Unlock locked out users

The check box "Activate limit for login attempts" is activated in the "Runtime settings &gt; User administration".   
The number 3 is entered in the field "Number of invalid login attempts".

If users have three failed attempts at login, for example by entering an incorrect password, they are assigned to the "Unauthorized" group. The user loses all authorizations. The user can still log on, but no longer has any authorizations. Only a user with administrator rights re-assigns the unauthorized user to a user group.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

#### Logging on as a user (Basic Panels, Panels, Comfort Panels, RT Advanced)

##### Introduction

As a rule you log-on as a user by means of a special button. The logon dialog box is displayed to this purpose.

The logon dialog box is displayed by default during access to a protected object if

- No user is logged on in Runtime.
- The logged-on user does not have the required authorization.

  > **Note**
  >
  > On Basic Panels, the system always opens the logon dialog when you press an access-protected button.

##### Requirements

- Under "Runtime settings &gt; User administration" the

  - "Enable limit for logon attempts" check box has been selected.
  - The number 3 is entered in the field "Number of incorrect login attempts".
- The "ShowLogonDialog" system function is configured on a button called "Logon".

##### Procedure

1. Click the "Logon" button. The logon dialog box is displayed.

   ![Procedure](images/75067566987_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/75067566987_DV_resource.Stream@PNG-en-US.png)
2. Enter your user name as it was specified in the user administration, for example "Foreman".

   If someone has logged on before you, the name of the user will be displayed.
3. Enter the corresponding password. The input is concealed.
4. Click "OK" to close the dialog box.

**Note**

When entering the password, note that it is case sensitive.

> **Note**
>
> When you change the HMI device, you do not need to re-enter the password if the permitted special characters are included in the password on all HMI devices.
>
> The following special characters are permitted for passwords:
>
> ()€&amp;@$%+#^[]|*-"&lt;&gt;!,.;:/_=\'? `~{}$
>
> If you switch to V14 from an older device version and prohibited special characters were used for the password, the password is deleted. You are informed about this with an error message and have to save a new password.

##### Logon was successful

If you have entered the user name "Foreman" and the entered password corresponds with the stored password, you are logged on as the user "Foreman" in runtime. You have the authorizations of the user "Foreman".

When the user "Foreman" accesses a protected object such as the "Logging" button, access to this protected object will only be authorized if the user "Foreman" has the required authorization. The programmed function is executed immediately.

If you do not have the required authorization after the successful log-on, a corresponding error message is displayed. However, you remain logged on in Runtime.

##### Logon was unsuccessful

An error message is displayed.

In order to maintain security, you or the user logged-on before you no longer has any authorizations. However, access to unprotected objects remains possible. The user view does not, however, show any entries. The user view and the authorizations change after the next successful log-on.

If the third login attempt has failed, the user will be assigned to the "Unauthorized" group. For this reason, do not configure a user group with this display name.

If the "Log off" function is called up or the logoff time of the user has expired, the user is logged off.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

#### Logging on as a user (RT Professional)

##### Introduction

As a rule you log-on as a user by means of a special button. The logon dialog box is displayed to this purpose.

The logon dialog box is displayed by default during access to a protected object if

- No user is logged on in Runtime.
- The logged-on user does not have the required authorization.

##### Requirements

- The "ShowLogonDialog" system function is configured on a button called "Logon".

##### Procedure

1. Click the "Logon" button. The logon dialog box is displayed.

   ![Procedure](images/75067566987_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/75067566987_DV_resource.Stream@PNG-en-US.png)
2. Enter your user name as it was specified in the user administration, for example "Foreman".

   If someone has logged on before you, the name of the user will be displayed.
3. Enter the corresponding password. The input is concealed.
4. Click "OK" to close the dialog box.

##### Logon was successful

If you have entered the user name "Foreman" and the entered password corresponds with the stored password, you are logged on as the user "Foreman" in runtime. You have the authorizations of the user "Foreman".

When the user "Foreman" accesses a protected object such as the "Logging" button, access to this protected object will only be authorized if the user "Foreman" has the required authorization. The programmed function is executed immediately.

If you do not have the required authorization after the successful log-on, a corresponding error message is displayed. However, you remain logged on in Runtime.

##### Logon was unsuccessful

An error message is displayed.

In order to maintain security, you or the user logged-on before you no longer has any authorizations. However, access to unprotected objects remains possible. The user view does not, however, show any entries. The user view and the authorizations change after the next successful log-on.

If the "Log off" function is called up or the logoff time of the user has expired, the user is logged off.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User view (Panels, Comfort Panels, RT Advanced, RT Professional)](#user-view-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring a user view (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-a-user-view-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating users (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-users-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[Managing users in the complex user view (Panels, Comfort Panels, RT Advanced, RT Professional)](#managing-users-in-the-complex-user-view-panels-comfort-panels-rt-advanced-rt-professional)
  
[Unlock locked out users (Basic Panels, Panels, Comfort Panels, RT Advanced)](#unlock-locked-out-users-basic-panels-panels-comfort-panels-rt-advanced)
  
[Logging on as a user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#logging-on-as-a-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Exporting the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)](#exporting-the-user-administration-panels-comfort-panels-rt-advanced-rt-professional)
  
[Importing the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)](#importing-the-user-administration-panels-comfort-panels-rt-advanced-rt-professional)

#### Exporting the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

The users and user groups are transferred to the HMI device from the Engineering System. If you have configured a user view, you can administer the users at the HMI device via the user view.

If a user has access to several HMI devices, the same user and the same password must be configured on each HMI device. Create a standard for user administration of the different HMI devices. Export the users and passwords on an HMI device to a storage medium, such as a floppy, memory card or a network drive. You import the users and passwords from this storage medium at all the other HMI devices.

You program a function which exports the user data at a button.

The system function "ExportImportUserAdministration" is not available on all HMI devices.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| When exporting, the user data are encrypted and written from the HMI device to the target file. The target file is overwritten |  |

##### Requirements

- An HMI device has been created.
- A screen has been created.
- A button has been created in the screen.
- The Inspector window is open.

##### Procedure

1. Click the button in the screen.
2. Click "Properties &gt; Events &gt; Click" in the Inspector window.
3. Click the entry "Add function" in the function list.
4. Select the "ExportImportUserAdministration" system function.
5. Select "Export" as the "Direction". When exporting, the target file is overwritten with the user data.
6. Enter the full path of the destination file as the "File name", for example "a:\test\usersview.txt".

**Note**

Ensure that the file name is written correctly. If the directory, for example "\test\", does not exist, it will be created without a prompt.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

#### Importing the user administration (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

If a user has access to several HMI devices, the same user and the same password must be configured on each HMI device. Create a standard for user administration of the different HMI devices. Export the users and passwords on an HMI device to a storage medium, such as a floppy, memory card or a network drive. You import the users and passwords from this storage medium at all the other HMI devices.

You configure a function which imports the user data at a command button.

The system function "ExportImportUserAdministration" is not available on all HMI devices.

> **Note**
>
> The export/import of the user administration configuration encompasses all the settings. Existing objects (users, groups, logon settings, authorization levels) are overwritten during the import. The imported users and passwords are valid immediately.

##### Requirements

- A screen has been created.
- A command button has been created in the screen.
- The Inspector window is open.

##### Procedure

1. Click the button in the screen.
2. Click "Properties &gt; Events &gt; Click" in the Inspector window.
3. Click the entry "Add function" in the function list.
4. Select the "ExportImportUserAdministration" system function.
5. Select "Import" as the "Direction." When importing, the user data in the HMI device are overwritten.
6. Enter the full path of the source file as the "File name", for example "a:\test\usersview.txt".

**Note**

Ensure that the file name is written correctly. If the folder, for example "\test\", or the file does not exist, an error message will be displayed.

---

**See also**

[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Logging on as a user (RT Professional)](#logging-on-as-a-user-rt-professional)

### Configuring access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Configuring operating authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-operating-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You configure an authorization at an object in order to protect it against access. All logged-on users who have this authorization can then access the object. If a user does not have runtime authorization to operate an object, the logon dialog box is displayed automatically.

> **Note**
>
> Several system functions are available under "User administration" so that user, password, and user group can be edited, for example, in the PLC.

---

**See also**

[Configuring operating authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#configuring-operating-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Users in runtime (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#users-in-runtime-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Creating an authorization (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-an-authorization-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Target groups in user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#target-groups-in-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

#### Configuring operating authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You configure the "Stop runtime" authorization on a button. Then only those users who have the appropriate authorization have access to this button, for example all the users of the "Operators" user group.

This ensures that access to the command button is protected. If a logged-on user who belongs to the "Operators" user group and has the required authorizations clicks the button, runtime is stopped.

An example describes in detail how to configure a command button with access protection.

##### Requirements

- The "Operators" user group has been created.
- The "Stop runtime" authorization has been created.
- A screen has been created and opened.
- The screen contains a button.

##### Procedure

1. Click the button in the screen.
2. Click "Properties &gt; Properties &gt; Security" in the Inspector window.
3. Select "Stop runtime" as the "Authorization".
4. In the Inspector window, select "Properties &gt; Events &gt; Click".
5. Select a system function from the function list, for example, "StopRuntime".

**Note**

The "Enable" and "Disable" events are only used to detect whether an object was selected or deselected. The events do not, however, trigger a password prompt.

Do not use the "Enable"or "Disable" event if you want to configure access protection at the function call of the object.

---

**See also**

[Access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## Reference (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Objects with access protection (Basic Panels)](#objects-with-access-protection-basic-panels)
- [Objects with access protection (Panels, Comfort Panels, RT Advanced)](#objects-with-access-protection-panels-comfort-panels-rt-advanced)
- [Objects with access protection (RT Professional)](#objects-with-access-protection-rt-professional)
- [Default user groups and authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced)](#default-user-groups-and-authorizations-basic-panels-panels-comfort-panels-rt-advanced)
- [Default user groups and authorizations (RT Professional)](#default-user-groups-and-authorizations-rt-professional)

### Objects with access protection (Basic Panels)

#### Introduction

The following objects can be configured with an authorization:

- I/O field
- Button
- Symbolic I/O field
- Graphic I/O field
- Date/time field
- Switch
- Alarm view
- User view
- Recipe view
- System diagnostic view

---

**See also**

[Objects with access protection (Panels, Comfort Panels, RT Advanced)](#objects-with-access-protection-panels-comfort-panels-rt-advanced)
  
[Objects with access protection (RT Professional)](#objects-with-access-protection-rt-professional)
  
[Default user groups and authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced)](#default-user-groups-and-authorizations-basic-panels-panels-comfort-panels-rt-advanced)
  
[Default user groups and authorizations (RT Professional)](#default-user-groups-and-authorizations-rt-professional)

### Objects with access protection (Panels, Comfort Panels, RT Advanced)

#### Introduction

The following objects can be configured with an authorization:

- I/O field
- Button
- Symbolic I/O field
- Graphic I/O field
- Date/time field
- Switch
- Symbol library
- Slider
- Effective range name
- Effective range name (RFID)
- Alarm view
- Alarm window
- User view
- HTML Browser
- Watch table
- Sm@rtClient view
- Recipe view
- f(x) trend view
- System diagnostic view
- System diagnostic window
- PLC code view
- GRAPH overview
- ProDiag overview

---

**See also**

[Field of application of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Default user groups and authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced)](#default-user-groups-and-authorizations-basic-panels-panels-comfort-panels-rt-advanced)
  
[Default user groups and authorizations (RT Professional)](#default-user-groups-and-authorizations-rt-professional)
  
[Target groups in user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#target-groups-in-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[User (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#user-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Objects with access protection (RT Professional)](#objects-with-access-protection-rt-professional)
  
[Objects with access protection (Basic Panels)](#objects-with-access-protection-basic-panels)

### Objects with access protection (RT Professional)

#### Introduction

The following objects can be configured with an authorization:

- Connector
- Pipe
- Double T-piece
- T piece
- Pipe bends
- I/O field
- Editable text field
- List box
- Combo box
- Button
- Round button
- Symbolic I/O field
- Graphic I/O field
- Bar
- Slider
- Scroll bar
- Check box
- Option button
- Gauge
- Clock
- User view
- HTML Browser
- Recipe view
- Alarm view
- f(x) trend view
- f(t) trend view
- Table view
- Value table
- System diagnostics view
- Media Player
- Channel diagnostics view
- PLC code view
- GRAPH overview
- ProDiag overview

In order to configure the following objects with access control, you additionally link the system function "ShowLogonDialog" to an event, for example, Click.

- Line
- Polyline
- Polygon
- Ellipse
- Ellipse segment
- Circle segment
- Ellipse arc
- Circular arc
- Circle
- Rectangle
- Text field
- Graphic view
- Screen window
- Print job/Script diagnostics

---

**See also**

[Objects with access protection (Panels, Comfort Panels, RT Advanced)](#objects-with-access-protection-panels-comfort-panels-rt-advanced)
  
[Objects with access protection (Basic Panels)](#objects-with-access-protection-basic-panels)

### Default user groups and authorizations  (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Principle

The predefined user groups and authorizations have the following numbers:

| User group | Number |
| --- | --- |
| "Administrator group" | 1 |
| "Users" | 2 |

| Authorization | Number |
| --- | --- |
| "User administration" | 1 |
| "Monitor" | 2 |
| "Operate" | 3 |

---

**See also**

[Objects with access protection (Panels, Comfort Panels, RT Advanced)](#objects-with-access-protection-panels-comfort-panels-rt-advanced)
  
[Objects with access protection (Basic Panels)](#objects-with-access-protection-basic-panels)

### Default user groups and authorizations (RT Professional)

#### Principle

The predefined user groups and authorizations have the following numbers:

User group:

- "Administrator group"
- "Users"

| Authorization | Number |
| --- | --- |
| "User administration" | 1 |
| "Monitor" | 2 |
| "Operate" | 3 |
| "Enable remote control" | 1000 |
| "Web access - View only" | 1002 |

Authorization 1000, "Enable remote control", is practical for client-server projects.

Authorization 1002, "Web access - view only" is significant in combination with the Web Navigator.

---

**See also**

[Objects with access protection (Panels, Comfort Panels, RT Advanced)](#objects-with-access-protection-panels-comfort-panels-rt-advanced)
  
[Objects with access protection (Basic Panels)](#objects-with-access-protection-basic-panels)

## Examples (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Example: Configuring a button with logon dialog box (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-with-logon-dialog-box-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Logging the logon and logoff events (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-logging-the-logon-and-logoff-events-basic-panels-panels-comfort-panels-rt-advanced)
- [Example: Structure of user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-structure-of-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Creating and configuring authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-and-configuring-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Configuring a button with access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-with-access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Creating user groups and assigning authorizations: (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-user-groups-and-assigning-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Example: Creating users and assigning them to a user group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-users-and-assigning-them-to-a-user-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Example: Configuring a button with logon dialog box (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Task

In the following example, you configure the "ShowLogonDialog" function for a button. A different user can then log on in runtime when the shift changes, for example. In the process the user previously logged on is logged off.

> **Note**
>
> In runtime the logon dialog box is not displayed by default until you access a protected object. Either no user is logged on or the logged-on user does not have the required authorization.

#### Requirements

- A screen has been created.
- A button has been created in the screen.

#### Procedure

1. Click the button in the screen.
2. Click "Properties &gt; Events &gt; Release" in the Inspector window.
3. Click the entry "Add function" in the "Function list" table.
4. Select the system function "ShowLogonDialog" from the "User administration" group.

   ![Procedure](images/82506061451_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/82506061451_DV_resource.Stream@PNG-en-US.png)

#### Result

If the user clicks on the button in runtime, the function "ShowLogonDialog" is called up. When the function "ShowLogonDialog" is called up, the logon dialog box is displayed. The user logs on with their user name and password.

---

**See also**

[Field of application of the user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Logging the logon and logoff events (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-logging-the-logon-and-logoff-events-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Structure of user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-structure-of-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Example: Logging the logon and logoff events (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Task

In the following example, you configure the function "TraceUserChange" to the event "User change".

#### Principle

The "TraceUserChange" function is called when a user logs on or off. When a function is called up, a system message with information about the corresponding user is output.

This system message can be archived. When archiving, the system message is provided with a date stamp and time stamp. This ensures that you can track which user was logged on at the HMI device at which time and for how long.

#### Requirements

- You have created an HMI device with Runtime Advanced.
- The Inspector window is open.

#### Procedure

1. Double-click the "Scheduler" in the Project view.
2. Double-click "Add" in the table of the tasks.
3. Enter "Logon-Protocol" as the "Name".
4. Select "User change" as the "Trigger".
5. Open "Properties &gt; Events" in the Inspector window.
6. Click the entry "Add function" in the "Function list" table.
7. Select the "TraceUserChange" system function.

#### Result

A system message is output when a user logs on or logs off.

---

**See also**

[Example: Configuring a button with logon dialog box (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-with-logon-dialog-box-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Example: Structure of user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Task

In the following example you set up a user administration for different users and user groups. The example orientates itself to a typical requirement profile from manufacturing engineering.

#### Principle

Completely different groups of persons are involved in a plant or project. Each group of persons protects its respective data and functions against access by others. For this purpose, users are created and assigned to a user group.

You can reproduce different views through user groups.

Example:

- Organizational view: Commissioners, Operators, Shift I, Shift II
- Technological view: Axis control, Tool changers, Plant North, Plant South

The following example orientates itself to the organizational view.

Every user group has characteristic requirements regarding access protection: A user group has operating authorizations for specific application cases. A programmer changes, for example, recipe data records.

In the example the users Miller, Group Smith and Foreman are created and assigned to different user groups.

Ms. Miller works as a programmer in the engineering system. The Group Smith are commissioners. Mr. Foreman is an operator.

#### Requirements

- A new project has been created.
- The "User administration" editor is open.

#### Procedures overview

Working with user administration has the following procedure in the example:

1. Creating authorizations The planner specifies which authorizations are required for access protection.
2. Configuring authorizations: The planner specifies which objects may be operated and which functions may be executed.
3. Creating user groups and allocating authorizations: The administrator creates the user groups together with the planner. The planner uses the authorizations to specify who may operate objects and change parameters.
4. Creating users and assigning them to a user group: The administrator administers the users.

#### Result

The aim is the following structure of the user administration of users, user groups and authorizations:

| Users |  |  | User groups | Authorizations |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Miller | Smith | Foreman | Roles | Changing recipe records | Changing system parameters | Changing process parameters | Managing |
|  |  |  | Administrator group |  |  |  | x |
| X |  |  | Programmer | X |  |  |  |
|  | X |  | Commissioning engineers | X | X | X |  |
|  |  | X | Operators | x |  |  |  |

The user "Foreman" who belongs to the "Operators" user group has access to the configured "To Recipe view" button.

> **Note**
>
> Alternatively, you can create several users as operators with different operating authorizations, for example, Operator Level 1, Operator Level 2.

---

**See also**

[Example: Configuring a button with logon dialog box (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-with-logon-dialog-box-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button with access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-with-access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Creating user groups and assigning authorizations: (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-user-groups-and-assigning-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Creating users and assigning them to a user group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-users-and-assigning-them-to-a-user-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Example: Creating and configuring authorizations (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Task

The following example shows you how to create the authorizations

#### Procedure

1. Open the "User groups" work area.
2. Double-click "Add" in the "Authorizations" table.
3. Enter "Change recipe data records" as the "Name" of the authorization.
4. Repeat steps 2 and 3 to create additional authorizations: "Change system parameters", "Change process parameters".

#### Result

![Result](images/73135008523_DV_resource.Stream@PNG-en-US.png)

### Example: Configuring a button with access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Task

In the following example you use a system function to create a button for a screen change. You protect the "To Recipe view" button against unauthorized operation. To do so, you configure the "Change recipe data records" authorization at the "To Recipe view" button.

#### Requirements

- A "Change recipe data records" authorization has been created.
- A "Recipes" screen has been created.
- A "Start" screen has been created and opened.
- A button has been created and marked in the "Start" screen.

#### Procedure

1. Click "Properties &gt; Properties &gt; General" in the Inspector window.
2. Enter "To Recipe view" as the text.
3. Click "Properties &gt; Events &gt; Click" in the Inspector window.
4. Click the "Add function" entry in the first line of the "Function list" table.
5. Select the "ActivateScreen" system function in the "Screens" group.
6. Click the ![Procedure](images/30890839819_DV_resource.Stream@PNG-de-DE.png) button in the "Screen name" field. A dialog box for selecting the screen opens.
7. Select the "Recipes" screen and use the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) button to close the dialog box.
8. Click "Properties &gt; Properties &gt; Security" in the Inspector window.
9. Select "Change recipe data records" as the "Authorization."

#### Result

![Result](images/111974016651_DV_resource.Stream@PNG-en-US.png)

Access to the "To Recipe view" button is protected. If, for example, the user "Smith" clicks the button in Runtime, the function "Recipe view" screen is called up. Prerequisite is that the user "Smith" has logged on correctly and has the required authorization. The "Recipes" screen contains a recipe view and other screen objects.

> **Note**
>
> If the logged-on user does not have the required authorization or if no user is logged on, the "Logon dialog box" is displayed. An alarm indicating that no operator authorization is available for this user appears in Runtime Professional in this case.

---

**See also**

[Example: Structure of user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-structure-of-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Creating users and assigning them to a user group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-users-and-assigning-them-to-a-user-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Creating user groups and assigning authorizations: (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-user-groups-and-assigning-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Example: Creating user groups and assigning authorizations: (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Task

In the following example you create the user groups and assign authorizations to them.

#### Procedure

1. Open the "User groups" work area.
2. Double-click "Add" in the "Groups" table.
3. Enter "Programmer" as the "Name".
4. Repeat steps 2 and 3 to create the "Commissioner" and "Operator" user groups.
5. Click "Administrator" in the "Groups" table.
6. Activate the "Change system parameters" authorization in the "Authorizations" table.

#### Interim result

![Interim result](images/73135349259_DV_resource.Stream@PNG-en-US.png)

#### Procedure

1. Click "Operator" in the "Groups" table.
2. Activate the "Change recipe data records" authorization in the "Authorizations" table.
3. Click "Commissioner" in the "Groups" table.
4. Activate the authorizations "Change recipe data records", "Change system parameters" and "Change process parameters" in the "Authorizations" table.
5. Click "Programmer" in the "Groups" table.
6. Activate the "Change recipe data records" authorization in the "Authorizations" table.

#### Result

![Result](images/73135715595_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Example: Structure of user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-structure-of-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Creating users and assigning them to a user group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-users-and-assigning-them-to-a-user-group-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button with access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-with-access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Example: Creating users and assigning them to a user group (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Task

In the following example you create the users and assign user groups to them. The users are sorted alphabetically immediately after the name has been entered.

#### Procedure

1. Open the "Users" work area.
2. Double-click "Add" in the "Users" table.
3. Enter "Miller" as the user name.
4. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Password" column. The dialog box for entering the password is opened.
5. Enter "miller" as the password.
6. To confirm the password, enter it a second time in the lower field.
7. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
8. Activate the "Programmer" user group in the "Groups" table.

#### Interim result

![Interim result](images/57908305931_DV_resource.Stream@PNG-en-US.png)

#### Procedure

1. Double-click "Add" in the "Users" table.
2. Enter "Smith" as the user name.
3. Click the ![Procedure](images/70589889163_DV_resource.Stream@PNG-de-DE.png) button in the "Password" column. The dialog box for entering the password is opened.
4. Enter "smith" as the password.
5. To confirm the password, enter it a second time in the lower field.
6. Close the dialog box by using the ![Procedure](images/84603740299_DV_resource.Stream@PNG-de-DE.png) icon.
7. Activate the "Commissioner" user group in the "Groups" table.
8. Repeat steps 2 to 6 for the user "Foreman."
9. Activate the "Operators" user group in the "Groups" table.

#### Result

![Result](images/57908310411_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Example: Structure of user administration (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-structure-of-user-administration-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Creating user groups and assigning authorizations: (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-creating-user-groups-and-assigning-authorizations-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Configuring a button with access protection (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#example-configuring-a-button-with-access-protection-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
