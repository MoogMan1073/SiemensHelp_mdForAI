---
title: "My WinCC Unified (RT Unified)"
package: WinCCUnifiedMyenUS
topics: 16
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# My WinCC Unified (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [Restrictions and requirements (RT Unified)](#restrictions-and-requirements-rt-unified)
- [Opening My WinCC Unified (RT Unified)](#opening-my-wincc-unified-rt-unified)
- [User interface (RT Unified)](#user-interface-rt-unified)
- [Add rule (RT Unified)](#add-rule-rt-unified)
- [Exporting and importing rules (RT Unified)](#exporting-and-importing-rules-rt-unified)
- [Clone rules (RT Unified)](#clone-rules-rt-unified)
- [Client settings (RT Unified)](#client-settings-rt-unified)
- [Start screen settings (RT Unified)](#start-screen-settings-rt-unified)
- [Settings for kiosk (RT Unified)](#settings-for-kiosk-rt-unified)
- [Display Runtime in kiosk mode (RT Unified)](#display-runtime-in-kiosk-mode-rt-unified)

## Introduction (RT Unified)

### Introduction

With My WinCC Unified, you define during runtime how the Runtime of a Unified PC web server is displayed in its clients.

My WinCC Unified works rule-based. For each rule, you define:

- For which client device the rule applies.

  The rule is applied to all users who log in to the Runtime of the Unified PC runtime on this client device.
- Whether auto-login is active.

  When auto-login is enabled, the client can automatically log in to Runtime without entering a username and password (auto-login).

  A default user who has no function rights is used to log in.
- Whether Runtime is displayed in kiosk mode.
- Which start screen is displayed after logging in to Runtime, and display of the start screen (section, start point, etc.).

My WinCC Unified is available:

- As web application
- On client devices for which kiosk mode is configured: In the Windows tray, via "WinCC Unified Control Center".

### Workflow

1. Install the SIMATIC WinCC Unified Control Center application on the client devices on which you want to display Runtime in kiosk mode.
2. Open My WinCC Unified.

   My WinCC Unified connects to the Runtime of the Unified PC in the background.
3. Add rules for the client devices of the Unified PC in My WinCC Unified.
4. Configure the rules.

When a user logs in to Runtime in a web client or starts Runtime in kiosk mode on a kiosk device, Runtime is displayed as defined by the rule.

---

**See also**

[Restrictions and requirements (RT Unified)](#restrictions-and-requirements-rt-unified)
  
[Install SIMATIC WinCC Unified Control Center (RT Unified)](#install-simatic-wincc-unified-control-center-rt-unified)
  
[Opening My WinCC Unified (RT Unified)](#opening-my-wincc-unified-rt-unified)
  
[Add rule (RT Unified)](#add-rule-rt-unified)

## Restrictions and requirements (RT Unified)

### My WinCC Unified restrictions

- My WinCC Unified is only available for Unified PC Runtime web server.
- You can create rules only for client devices with static IP addresses.
- If you enable auto-login in a rule for a client device, no operator control of objects or functions that are linked to function rights is possible on this device after automatic login to Runtime.

### Restrictions in kiosk mode

- The display of Runtime in kiosk mode is supported only on Windows PCs.
- It is not possible to exit the kiosk mode via touch gestures.

### Requirements

The following general requirements apply for opening My WinCC Unified and starting Runtime in kiosk mode:

- WinCC Unified Runtime 19 is installed on the Unified PC.
- A Unified PC with device version V19 was configured in the engineering system and loaded onto the Unified PC.
- The corresponding Runtime project has the status "Running" on the Unified PC.
- The user management configuration of the project is active.
- When using the central user management:

  - At least one user is created in the UMC system.
  - The user created in the UMC system has been imported into the TIA Portal project before the loading.
  - The user has the function rights required to operate My WinCC Unified through his roles.
- When using the local user management:

  - Before the loading, at least one user has been created in TIA Portal.
  - The user has the function rights required to operate My WinCC Unified through his roles.
- A valid web server certificate (self-signed or CA-based) is installed on the Unified PC that is used as the Runtime web server.
- Opening My WinCC Unified:

  - In a web client: The browser you use as a web client trusts the web server certificate.
  - Via the SIMATIC WinCC Unified Control Center application using the Windows tray:

    The SIMATIC WinCC Unified Control Center application is installed on the client device.

    The Windows certificate store of the device trusts the Runtime web server certificate.
- Start kiosk mode:

  - The SIMATIC WinCC Unified Control Center application is installed on the kiosk device.
  - The Windows certificate store of the kiosk device trusts the Runtime web server certificate.
  - In My WinCC Unified, a rule has been added for the kiosk device in which the kiosk mode has been enabled.

### Function rights

The following function rights are required to log on to and operate My WinCC Unified:

- Read access: "My WinCC Unified - Read device and user settings"

  > **Note**
  >
  > V19 supports only device-specific settings.
- Read access and write access: "My WinCC Unified - Read and write access to device specific settings"

> **Note**
>
> For compatibility reasons, logging on to My WinCC Unified and configuring the start screen settings is also possible via the "Remote access" function right.

### Trust web server certificate

Start kiosk mode:

| Web server certificate | Establishing the trust relationship | Procedure |
| --- | --- | --- |
| CA-based | Establish the trust relationship before connecting to Runtime. | Install the root certificate before connecting for the first time in Edge or Chrome. |
| Self-signed | On the kiosk device, start Edge or Chrome and open the Unified Runtime start page. Install the self-signed web server certificate in Edge or Chrome. |  |

Starting My WinCC Unified with the Windows tray via "WinCC Unified Control Center":

| Web server certificate | Establishing the trust relationship | Procedure |
| --- | --- | --- |
| CA-based | Establish the trust relationship before connecting to Runtime. | Install the root certificate in Edge or Chrome before connecting for the first time. |
| Self-signed | On the kiosk device, start Edge or Chrome and open the Unified Runtime start page. Install the self-signed web server certificate in Edge or Chrome. |  |

Starting My WinCC Unified in a web client:

| Web server certificate | Establishing the trust relationship | Procedure |
| --- | --- | --- |
| CA-based | Recommendation: Establish the trust relationship before connecting to Runtime. | - Edge and Chrome as web client:   Install the root certificate before connecting for the first time in Edge or Chrome. - Firefox as web client:   Install the root certificate before connecting to Firefox for the first time. |
| Alternative: Establish the trust relationship when you first establish the connection. | - Edge and Chrome as web client:   Install the root certificate the first time you connect in Edge or Chrome. - Firefox as web client:   Install the root certificate the first time you connect to Firefox. |  |
| Self-signed | Establish the trust relationship when you first establish the connection. | - Edge and Chrome as web client:   Install the self-signed web server certificate the first time you connect in Edge or Chrome. - Firefox as web client:   Install the self-signed web server certificate the first time you connect in Firefox. |

---

**See also**

[Install SIMATIC WinCC Unified Control Center (RT Unified)](#install-simatic-wincc-unified-control-center-rt-unified)
  
[Installing the root certificate before the first connection (Edge and Chrome) (RT Unified)](Certificates%20in%20WinCC%20Unified%20Runtime%20%28RT%20Unified%29.md#installing-the-root-certificate-before-the-first-connection-edge-and-chrome-rt-unified-1)
  
[Installing the root certificate at the first connection (Edge and Chrome) (RT Unified)](Certificates%20in%20WinCC%20Unified%20Runtime%20%28RT%20Unified%29.md#installing-the-root-certificate-at-the-first-connection-edge-and-chrome-rt-unified-1)
  
[Installing the root certificate before the first connection (for Firefox) (RT Unified)](Certificates%20in%20WinCC%20Unified%20Runtime%20%28RT%20Unified%29.md#installing-the-root-certificate-before-the-first-connection-for-firefox-rt-unified-1)
  
[Installing the root certificate at the first connection (for Firefox) (RT Unified)](Certificates%20in%20WinCC%20Unified%20Runtime%20%28RT%20Unified%29.md#installing-the-root-certificate-at-the-first-connection-for-firefox-rt-unified-1)
  
[Installing the self-signed web server certificate for Edge and Chrome (RT Unified)](Certificates%20in%20WinCC%20Unified%20Runtime%20%28RT%20Unified%29.md#installing-the-self-signed-web-server-certificate-for-edge-and-chrome-rt-unified-1)
  
[Installing the self-signed web server certificate for Firefox (RT Unified)](Certificates%20in%20WinCC%20Unified%20Runtime%20%28RT%20Unified%29.md#installing-the-self-signed-web-server-certificate-for-firefox-rt-unified-1)

## Opening My WinCC Unified (RT Unified)

### Introduction

Your procedure depends on whether you open My WinCC Unified in a web client or on a kiosk device with the Windows tray via "WinCC Unified Control Center".

### Requirement

See section [Restrictions and requirements](#restrictions-and-requirements-rt-unified).

### Open in a web client

1. Start the Web client.
2. In the address bar of the browser, enter the URL of the Unified Runtime web server: "https://&lt;IP-address of the HMI device or its FQDN or device name&gt; ".
3. Press Enter.

   You see the Unified home page:

   ![Open in a web client](images/169963596299_DV_resource.Stream@PNG-de-DE.png)

   ![Open in a web client](images/169963596299_DV_resource.Stream@PNG-de-DE.png)
4. Click "My WinCC Unified".

   A new tab opens. You see the logon dialog.
5. Enter the user name and password of a user with the required function rights and select another language if necessary. Confirm your entries.

### Open on a kiosk device via the Windows tray

1. If the device is in kiosk mode, exit kiosk mode.
2. Select "WinCC Unified Control Center" in the Windows tray:

   ![Open on a kiosk device via the Windows tray](images/172968208395_DV_resource.Stream@PNG-de-DE.png)

   ![Open on a kiosk device via the Windows tray](images/172968208395_DV_resource.Stream@PNG-de-DE.png)

   If no server is configured yet, you will see the following extended Windows tray.

   ![Open on a kiosk device via the Windows tray](images/172972590603_DV_resource.Stream@PNG-de-DE.png)

   ![Open on a kiosk device via the Windows tray](images/172972590603_DV_resource.Stream@PNG-de-DE.png)

   Continue with step 3.

   If a Unified Server has already been configured, the extended Windows tray shows details about that server and the connection status:

   ![Open on a kiosk device via the Windows tray](images/172972599691_DV_resource.Stream@PNG-de-DE.png)

   ![Open on a kiosk device via the Windows tray](images/172972599691_DV_resource.Stream@PNG-de-DE.png)

   Your procedure depends on whether you want to connect My WinCC Unified to this server, and on the connection status:

   - Connect to other server: Continue with step 4.
   - Connect to the configured server. The connection status is not "Connection available": Start Runtime on the server. Then continue with step 5.
   - Connect to the configured server. The connection status is "Connection available": Continue with step 6.
3. If no server is configured yet, follow these steps:

   - In the extended Windows tray, select "Configure Server".

     The "Configure Server" dialog box opens.

     ![Open on a kiosk device via the Windows tray](images/172978445579_DV_resource.Stream@PNG-de-DE.png)

     ![Open on a kiosk device via the Windows tray](images/172978445579_DV_resource.Stream@PNG-de-DE.png)
   - "Server display name": Enter the display name of the server.
   - "Server": Depending on what information is stored in the web server certificate, enter the IP address or the device name of the server.

     Mandatory information
   - Click "Apply".

     The window is extended:

     ![Open on a kiosk device via the Windows tray](images/172978761867_DV_resource.Stream@PNG-de-DE.png)

     ![Open on a kiosk device via the Windows tray](images/172978761867_DV_resource.Stream@PNG-de-DE.png)

   Continue with step 5.
4. If a different server is configured than the one you want to connect to, change the server. Follow these steps:

   - In the "Server Status" area, click "...".
   - Select "Delete".
   - Configure the server in the "Configure Server" area:

     "Server display name": Enter the display name of the server.

     "Server": Depending on what information is stored in the web server certificate, enter the IP address or the device name of the server. Mandatory information
   - Click "Apply".
5. Under "Server Status", click on "Check Status".

   It is checked whether a connection to the configured server is possible.

   - Status is not "Connection available": No connection is possible. Start the Runtime of the server and repeat the check.
   - Status is "Connection available": The connection is possible.
6. If a connection is possible, select "WinCC Unified Control Center &gt; My WinCC Unified" in the Windows tray.
7. Log in to Runtime in the "User login" dialog:

   - Enter the user name and password of a user with the necessary function rights.
   - Select another language if required.
   - Confirm your entries.

> **Note**
>
> "Configure Server" remembers inputs transferred by "Apply". If you select the IP address provided under "Server", the display name transferred with "Server display name" for this IP address is automatically entered under "Apply".
>
> You can change the display name of the configured server later. In the "Server Status" area, click "... &gt; Edit" and change your entry.

### Result

My WinCC Unified connects to the Runtime of the Unified PC in the background.

You see the start view of My WinCC Unified:

![Result](images/172972082315_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> When using a central user management, My WinCC Unified is displayed in the language you selected when you logged in in the "User login" dialog.  
> If this language is not available for the current project or if the language setting has not been set in the central user management, the following language is displayed:
>
> - Engineering with TIA Portal: The language for which the lowest number was configured in the Runtime settings.
> - ​Engineering with Online Engineering: The language set as default language in the "Languages" tab in the "Languages and Resources" editor.
>
> ​If you do not select a language in the "User login" dialog, My WinCC Unified is displayed in the language that is set for the browser.

---

**See also**

[Exit Kiosk mode (RT Unified)](#exit-kiosk-mode-rt-unified)
  
[User interface (RT Unified)](#user-interface-rt-unified)

## User interface (RT Unified)

### Structure

Structure of the My WinCC Unified user interface using the client overview as an example:

![Structure](images/172980409995_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Navigation bar |
| ② | Navigator for rules |
| ③ | Search field  Filters the rules displayed in the navigator according to the entered search string. |
| ④ | "+ Add new" button   To add a new rule. |
| ⑤ | A list of available rules. The rules are sorted according to when they are added.  To load a rule into the work area, click on the rule. |
| ⑥ | "..." button  Opens a menu for exporting and importing the rules. |
| ⑦ | "+" and "-" buttons  Adds or removes a facet from the rule.  The "Client settings" facet is always available. You cannot remove it. |
| ⑧ | Work area  Shows the rule selected in the navigator. |
| ⑨ | The facets of the rule loaded into the work area  To display a facet, click on the facet.  The facet settings are displayed in the work area. You can edit them. |
| ⑩ | To configure the currently selected facet. |
| ⑪ | Function bar for saving, cloning or deleting the displayed rule |

### Navigation bar buttons

| Button | Description |
| --- | --- |
| ![Navigation bar buttons](images/172875928075_DV_resource.Stream@PNG-de-DE.png) | Home |
| ![Navigation bar buttons](images/172878317195_DV_resource.Stream@PNG-de-DE.png) | Client overview   To manage and configure the client-specific rules |

### Buttons of the toolbar

| Button | Description |
| --- | --- |
| ![Buttons of the toolbar](images/171148114571_DV_resource.Stream@PNG-de-DE.png) | Saves the changes to the rule currently loaded in the work area. |
| ![Buttons of the toolbar](images/171134039051_DV_resource.Stream@PNG-de-DE.png) | Clones the rule loaded into the work area.  Edit the client settings and, if required, the other facets of the rule. |
| ![Buttons of the toolbar](images/171148122891_DV_resource.Stream@PNG-de-DE.png) | Deletes the rule loaded into the work area. |

## Add rule (RT Unified)

### Requirement

My WinCC Unified is open.

### Procedure

1. In the "Client overview" navigation bar, click ![Procedure](images/172878317195_DV_resource.Stream@PNG-de-DE.png).
2. Click "+ Add new" in the navigator.

   The new rule is created and loaded into the work area.

   The rule has the facet "Client settings".
3. Configure the client settings.

   See section [Client settings](#client-settings-rt-unified).
4. Click "+" and select the facets you require.
5. Configure the settings of the added facets.

   See sections [Start screen settings](#start-screen-settings-rt-unified) and [Settings for kiosk](#settings-for-kiosk-rt-unified).
6. To remove a facet, click on the facet and then on "-".

   The "Client settings" facet cannot be removed.
7. Click in the toolbar ![Procedure](images/171148114571_DV_resource.Stream@PNG-de-DE.png).

### Result

The rule is applied to all clients that log in to Runtime from the device configured in "Client settings".

When you add or edit a rule for an already started client, the following applies:

- Web client: The configuration takes effect after the web page has been updated.
- Kiosk client: The configuration takes effect after kiosk has been restarted on the client.

---

**See also**

[Opening My WinCC Unified (RT Unified)](#opening-my-wincc-unified-rt-unified)
  
[Exporting and importing rules (RT Unified)](#exporting-and-importing-rules-rt-unified)

## Exporting and importing rules (RT Unified)

### Introduction

My WinCC Unified supports the export and import of rules via a YAML file. This enables you to:

- Edit rules locally
- Transfer rules between Unified Runtime servers

Information about the structure of the YAML file can be found below.

> **Note**
>
> The YAML files are not protected against manipulation. You are responsible for ensuring the integrity of these files.
>
> PINs configured in My WinCC Unified are hashed during export.

### Export

**Requirement**

- Rules have been added in My WinCC Unified.
- You are logged on to My WinCC Unified.

**Procedure**

1. In the "Client overview" navigation bar, click ![Export](images/172878317195_DV_resource.Stream@PNG-de-DE.png).
2. Click "..." in the navigator.
3. Select "Export".
4. Select the export file name and location.
5. Confirm your entries.

**Result**

All rules of the Runtime server are exported to a YAML file.

### Import

**Requirement**

- You have access to the YAML file.
- You are logged on to My WinCC Unified.
- The user logged on to My WinCC Unified has the "My WinCC Unified - Read and write access to device-specific settings" function right.

**Procedure**

1. Select "Client overview" in the navigation bar.
2. Click "..." in the navigator.
3. Select "Import".
4. Select the YAML file.
5. Confirm your entries.

**Result**

The rules from the file are imported into the navigator.

If the file and the navigator contain a rule for the same client device, the settings from the file are applied.

> **Note**
>
> If you changed or added a PIN when editing the YAML file, the PIN is hashed during import. The import takes longer than importing a file that contains only PINs that have already been hashed.

### Structure of the YAML file

The following example shows the required structure of the YAML files:

WebClientConfiguration:

  - Unit_1:

      Identity: 192.168.178.20

      IdentityType: IP_ADDRESS

      StartScreen: 1_Main

      ZoomAndPositionOffset:

        Left: 500

        Top: 1000

        ZoomFactor: 2

      AutoLogin: true

      KioskSettings:

        LockDownStatus: true

        BreakOutData:

          IsEnabled: true

          SelectedKey: ALT+F4

          IsPinConfigured: true

          Pin: RYMUwKebeMiP7KIgLv1iwA0R9RhhkEvqv4vjpW/uuosGXabd4gbeQS/GbRB2Hbpm+lmHLoZgYR1kEQp4wRbXyg==

          Keys:

- Alt+F4

        FolderData:

          IsExternalDriveAccessible: true

          FolderItems:

            - Path: c:\user1\download\

              IsDefault: true

  - Unit_2:

      Identity: 192.168.178.21

      IdentityType: IP_ADDRESS

      StartScreen: 2_CustomControl

      ...

---

**See also**

[Add rule (RT Unified)](#add-rule-rt-unified)
  
[Opening My WinCC Unified (RT Unified)](#opening-my-wincc-unified-rt-unified)

## Clone rules (RT Unified)

### Requirement

- A rule has been added in My WinCC Unified.
- You are logged on to My WinCC Unified.

### Procedure

1. In the "Client overview" navigation bar, click ![Procedure](images/172878317195_DV_resource.Stream@PNG-de-DE.png).
2. Click a rule in the navigator.

   The rule is loaded into the work area.
3. Click in the toolbar ![Procedure](images/171134039051_DV_resource.Stream@PNG-de-DE.png).

   A new rule is added. Except for the client settings, it is identical to the previously loaded rule.
4. Click "Client settings" and configure the settings for the device.
5. (Optional) Edit the other facets as required (edit, add, delete).
6. Click in the toolbar ![Procedure](images/171148114571_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

[Add rule (RT Unified)](#add-rule-rt-unified)
  
[Opening My WinCC Unified (RT Unified)](#opening-my-wincc-unified-rt-unified)

## Client settings (RT Unified)

In the "Client settings" facet, you specify which device the rule applies to.

![Figure](images/172987248523_DV_resource.Stream@PNG-de-DE.png)

The rule applies to all clients started on this device.

The facet is mandatory. You cannot add or remove them using the "+" and "-" buttons.

### Settings

|  | Description |
| --- | --- |
| "Client name" | Mandatory field  The device name or FQDN (Fully Qualified Domain Name)  If the rule applies to the local clients of the Unified PC, you can also enter "localhost". |
| "Client address" | Mandatory field  The IP address  You have the following options:  - Enter an IP address or multiple IP address (e.g. `192.65.168.160` or `192.65.168.160, 192.65.168.165`). The rule applies to this device or these devices. - Enter an IP address range (e.g. `192.65.168.160-192.65.168.190`). The rule applies to all devices in this address range. - Combine these options (e.g. `192.65.168.160`, `192.65.168.165-192.65.168.190`). |
| ![Settings](images/172860048139_DV_resource.Stream@PNG-de-DE.png) | Reserved for future versions. |

> **Note**
>
> Do not enter an IP address in multiple rules.
>
> If you enter an IP address in a rule and the IP address also belongs to the address range configured in another rule, the rule in which you entered the IP address is applied.
>
> **Examples of "Client address"**
>
> You define the following rules:
>
> - 1st rule: "Client address": `192.65.168.165`
>
>   Successfully saved.
> - 2nd rule: "Client address": `192.65.168.160-192.65.168.190, 192.65.168.199`
>
>   Successfully saved. For the display of Runtime on the client device with the IP address 192.65.168.165, the 1st rule is applied.
> - 3rd rule: "Client address": 192.65.168.199
>
>   Saving is not successful because the IP address is already entered in the 2nd rule.

---

**See also**

[Add rule (RT Unified)](#add-rule-rt-unified)

## Start screen settings (RT Unified)

In the "Start screen" facet, you determine which start screen the clients see in Runtime.

![Figure](images/172989714571_DV_resource.Stream@PNG-de-DE.png)

You add the facet using the "+" buttons and remove it using the "-" button.

### Settings

|  | Description |
| --- | --- |
| "Authentication" | "Show start screen without login" option:  - Activated: The Web clients of the device are logged in to Runtime with a default user without user input. You automatically see the start screen that is usually configured. - Disabled: The Web clients of the device must enter their user name and password to log in to Runtime. |
| "Selected start screen" | Select the start screen: You are offered all the start screens of the project running in Runtime. |
| "Apply current client session" | If WinCC Unified Runtime is open in the same Web client, click this button to apply the settings of the screen currently displayed in Runtime to the rule.  Button is disabled if there is more than 1 address or one address range is entered under "Client address". |
| "Resolution" | The resolution configured in engineering  Read-only |
| "Screen area" | "Use the complete screen as start screen" option: The complete process screen is displayed as the start screen. |
| "Use a selected screen area as start screen" option: Only the area of the process screen selected under "Screen area" is displayed as the start screen. |  |
| "Screen area" |  |
| "Zoom factor": | Enter the zoom factor.  Default: 100% |
| "Start point X", "Start point Y" | Enter the starting point of the upper left corner of the screen area to be displayed.  Default: 0 |

---

**See also**

[Add rule (RT Unified)](#add-rule-rt-unified)

## Settings for kiosk (RT Unified)

In the "Kiosk" facet, you determine whether Runtime runs in kiosk mode on the device configured in "Client settings".

![Figure](images/172989723659_DV_resource.Stream@PNG-de-DE.png)

You add the facet using the "+" buttons and remove it using the "-" button.

### Settings

|  | Description |
| --- | --- |
| "Suppressed shortcuts" |  |
| "Disable shortcut keyes for operating system" | - Option disabled: Users can use the Windows shortcut keys in kiosk mode. - Option enabled: Users cannot use the Windows shortcut keys in kiosk mode, except for the shortcut configured in "Key to exit runtime". |
| "Key to exit runtime" | Configure whether users can exit Runtime via a shortcut key when the "Disable shortcut keyes for operating system" option is enabled:  - "Disabled"   A restart of the kiosk device is required to exit Runtime. - "Alt+F4"   Runtime can be exited by pressing "Alt+F4" or by restarting the kiosk device. |
| "User needs to enter a PIN to exit runtime" | The option is only available if you have selected the entry "Key to exit runtime" in "Alt+F4".  - Option enabled: After pressing Alt+F4, the user is prompted to enter a PIN. Runtime is exited only after entering the PIN configured below. - Option disabled: Runtime is exited without entering a PIN. |
| "PIN" | Enter an 8-digit number as the PIN. |
| "Repeat PIN" | Repeat the PIN. |
| "Access to file system" |  |
| "Enable access to external drives plugged to this device" | If this option is enabled, Runtime has access to all external drives connected to the kiosk device. |
| ![Settings](images/172901656715_DV_resource.Stream@PNG-de-DE.png) | Filters which of the added folders you see. |
| ![Settings](images/171148122891_DV_resource.Stream@PNG-de-DE.png) | Removes all added folders |
| ![Settings](images/172875757579_DV_resource.Stream@PNG-de-DE.png) | Adds a new line to the list of local folders  You must add at least the path to a local folder. |
| Per line: |  |
| "Path to folder" | Enter the path to the local folder to which Runtime will have access. |
| "Delete access"     ![Settings](images/171148122891_DV_resource.Stream@PNG-de-DE.png) | Deletes the line. |
| "Default path" | Option enabled: Runtime uses entered folder as default for download folder.  Can only be enabled for one folder. |

---

**See also**

[Add rule (RT Unified)](#add-rule-rt-unified)

## Display Runtime in kiosk mode (RT Unified)

This section contains information on the following topics:

- [Install SIMATIC WinCC Unified Control Center (RT Unified)](#install-simatic-wincc-unified-control-center-rt-unified)
- [Configuring kiosk mode (RT Unified)](#configuring-kiosk-mode-rt-unified)
- [Start kiosk mode (RT Unified)](#start-kiosk-mode-rt-unified)
- [Exit Kiosk mode (RT Unified)](#exit-kiosk-mode-rt-unified)

### Install SIMATIC WinCC Unified Control Center (RT Unified)

The SIMATIC WinCC Unified Control Center application must be installed on clients that are to run in kiosk mode.

#### Requirement

- You have administration rights on the PC on which you want to use Runtime in kiosk mode.

#### Procedure

To install SIMATIC WinCC Unified Control Center, follow these steps:

1. Insert the installation medium in the relevant drive.
2. Copy the installation files to the PC.
3. On the PC, in the folder with the installation files, right-click the "Start" application.
4. Select "Run as administrator".
5. Select the required installation language.
6. Follow the installation instructions.
7. Reboot the PC.

#### Result

- The application is installed.
- The SIMATIC WinCC Unified Client Service is installed and running.
- The Windows tray is extended by the icon of "WinCC Unified Control Center":

  ![Result](images/172968208395_DV_resource.Stream@PNG-de-DE.png)

  Commands available via the icon:

  - "Configure Server"

    For configuring the connection to the Runtime web server to which My WinCC Unified and the kiosk mode connect.
  - "My WinCC Unfied"

    At the start of My WinCC Unified.
  - "Launch UI Client"

    To start Runtime in kiosk mode.

---

**See also**

[Start kiosk mode (RT Unified)](#start-kiosk-mode-rt-unified)

### Configuring kiosk mode (RT Unified)

#### Requirement

My WinCC Unified is open.

#### Procedure

1. In the "Client overview" navigation bar, click ![Procedure](images/172878317195_DV_resource.Stream@PNG-de-DE.png).
2. Add a new rule or click on a rule in the navigator.

   See section [Add rule](#add-rule-rt-unified).

   Or click on an existing rule.
3. If the "Kiosk" facet has not yet been added, click "+" and select "Kiosk".
4. Configure the kiosk settings. See [Settings for kiosk](#settings-for-kiosk-rt-unified).
5. Click in the toolbar ![Procedure](images/171148114571_DV_resource.Stream@PNG-de-DE.png).

### Start kiosk mode (RT Unified)

#### Requirement

See section [Restrictions and requirements](#restrictions-and-requirements-rt-unified).

#### Procedure

1. Select "WinCC Unified Control Center" in the Windows tray:

   ![Procedure](images/172968208395_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/172968208395_DV_resource.Stream@PNG-de-DE.png)

   If no server is configured yet, you will see the following extended Windows tray.

   ![Procedure](images/172972590603_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/172972590603_DV_resource.Stream@PNG-de-DE.png)

   Continue with step 2.

   If a server has already been configured, the extended Windows tray shows details about that server and the connection status:

   ![Procedure](images/172972599691_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/172972599691_DV_resource.Stream@PNG-de-DE.png)

   Your procedure depends on whether you want to connect My WinCC Unified to this server, and on the connection status:

   - Connect to other server: Continue with step 3.
   - Connect to the configured server. The connection status is not "Connection available": Start Runtime on the server. Then continue with step 4.
   - Connect to the configured server. The connection status is "Connection available": Continue with step 5.
2. If no server is configured yet, follow these steps:

   - In the extended Windows tray, select "Configure Server".

     The "Configure Server" dialog box opens.

     ![Procedure](images/172978445579_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/172978445579_DV_resource.Stream@PNG-de-DE.png)
   - "Server display name": Enter the display name of the server.
   - "Server": Depending on what information is stored in the web server certificate, enter the IP address or the device name of the server.

     Mandatory information
   - Click "Apply".

     The window is extended:

     ![Procedure](images/172978761867_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/172978761867_DV_resource.Stream@PNG-de-DE.png)

   Continue with step 5.
3. If a different server is configured than the one you want to connect to, change the server. Follow these steps:

   - Click "..." in the plant complex "Server Status".
   - Select "Delete".
   - Configure the server in the "Configure Server" area:

     "Server display name": Enter the display name of the server.

     "Server": Depending on what information is stored in the web server certificate, enter the IP address or the device name of the server. Mandatory information
   - Click "Apply".
4. Under "Server Status", click on "Check Status".

   It is checked whether a connection to the configured server is possible.

   - Status is not "Connection available": No connection is possible. Start the Runtime of the server and repeat the check.
   - Status is "Connection available": The connection is possible.
5. If a connection is possible, select "WinCC Unified Control Center &gt; Launch UI Client" in the Windows tray.
6. Log in to Runtime in the "User login" dialog:

   - Enter the user name and password of a user with the necessary function rights.
   - Select another language if required.
   - Confirm your entries.

#### Result

Runtime is started in kiosk mode.

On the kiosk device, Runtime has access only to the locations configured in the rule.

> **Note**
>
> When using a central user management, My WinCC Unified is displayed in the language you selected when you logged in in the "User login" dialog.  
> If this language is not available for the current project or if the language setting has not been set in the central user management, the following language is displayed:
>
> - Engineering with TIA Portal: The language for which the lowest number was configured in the Runtime settings.
> - ​Engineering with Online Engineering: The language set as default language in the "Languages" tab in the "Languages and Resources" editor.
>
> ​If you do not select a language in the "User login" dialog, the application is displayed in the language set for the browser.

---

**See also**

[Exit Kiosk mode (RT Unified)](#exit-kiosk-mode-rt-unified)

### Exit Kiosk mode (RT Unified)

#### Requirement

Kiosk mode is running.

#### Procedure

Your procedure depends on how the kiosk mode was configured in the client rule:

| Symbol | Meaning |
| --- | --- |
| Use of Windows shortcut keys disabled, except for Alt+F4   (Default) | | Symbol | Meaning | | --- | --- | | 1. Press Alt+F4. 2. Depending on the configuration: If you need to enter a PIN to exit, enter the PIN that is configured in the rule. |  | |
| Use of all Windows shortcut keys disabled | | Symbol | Meaning | | --- | --- | | 1. Reboot the device. |  | |
| Use of Windows shortcut keys allowed | | Symbol | Meaning | | --- | --- | | 1. Press Alt+F4, restart the device or start Windows Task Manager and end the Kiosk process there. |  | |

---

**See also**

[Start kiosk mode (RT Unified)](#start-kiosk-mode-rt-unified)
