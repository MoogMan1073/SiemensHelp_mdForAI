---
title: "Simulate runtime (RT Unified)"
package: RuntimeWCCUenUS
topics: 11
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Simulate runtime (RT Unified)

This section contains information on the following topics:

- [Simulate Unified Comfort Panel (RT Unified)](#simulate-unified-comfort-panel-rt-unified)
- [Simulating Unified PC (RT Unified)](#simulating-unified-pc-rt-unified)

## Simulate Unified Comfort Panel (RT Unified)

This section contains information on the following topics:

- [Basics of simulation (RT Unified)](#basics-of-simulation-rt-unified)
- [Enable "Load preview" dialog (RT Unified)](#enable-load-preview-dialog-rt-unified)
- [Simulating a project (RT Unified)](#simulating-a-project-rt-unified)
- [Simulating a central user management (RT Unified)](#simulating-a-central-user-management-rt-unified)

### Basics of simulation (RT Unified)

#### Introduction

You can use the simulator to test the performance of your runtime project on the configuration PC. This allows you to quickly locate any logical configuration errors before productive operation.

The simulation is compiled like a real project and loaded into the Runtime installed on the configuration PC.

The project is downloaded as follows:

- The project is fully downloaded if the simulation of the project is not executed in runtime.
- If the simulation of the project is executed in runtime and changes can be compiled and downloaded, only changes are downloaded.

> **Note**
>
> **The "Load preview" dialog is skipped by default when simulating.**
>
> If necessary, activate the dialog under "Options &gt; Settings &gt; Simulation".

You recognize a simulation in the SIMATIC Runtime Manager by the "Simulation" type. A runtime project can be downloaded to the PC as a real project and as a simulation at the same time.

With an installed Runtime as of version V17, backward compatibility is also supported for simulations.

You can simulate runtime projects whose configured runtime version is the current version or the previous version.

> **Note**
>
> **Do not use in a production environment**
>
> The simulation is not intended for use in a production environment and must not be used in a manufacturing plant.

> **Note**
>
> **PLC tags are not simulated.**
>
> PLC tags are not simulated. PLC tags are overwritten in the PLC. This can influence the process.

#### Field of application

You can use the simulator to test the following functions, for example:

- Screen change and screen navigation
- Internal tags
- Screen display
- Configured alarms which are not triggered by a PLC

---

**See also**

[Simulating a project (RT Unified)](#simulating-a-project-rt-unified)
  
[Restrictions in compiling and loading changes (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#restrictions-in-compiling-and-loading-changes-rt-unified)
  
[Using PLCSIM (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#using-plcsim-rt-unified)

### Enable "Load preview" dialog (RT Unified)

The "Load preview" dialog is skipped by default when simulating projects.

In the "Load preview" dialog, make the settings for loading into the simulation. In addition, information on the HMI runtime and on the secured transmission is displayed.

To permanently select the "Load preview" dialog when simulating projects, follow these steps:

1. Open the settings under "Options &gt; Settings".
2. Select "Simulation".
3. In the "HMI Simulation" area, select the check box "Show 'Load preview' dialog during download to simulation".

#### Settings in the "Load preview" dialog

The "Load preview" dialog gives you the following setting options:

- Load Runtime:

  - Full download (default selection)
  - No action
- Runtime start:

  - Start runtime (default selection)
  - No action
- Runtime values:

  - Keep current values (default selection)
  - Reset to start values
  - Keep selected

    Options for tags, active alarms and user administration data in the drop-down menu.
- Reset logs:

  - No reset (default selection)
  - Reset all

After loading, the selected settings are applied to the simulation for future loading processes.

> **Note**
>
> **Skipping the "Load preview" dialog**
>
> If you have not yet made any settings, the default selection is used. The settings used and the alarms that appear are displayed in the Inspector window in the "Info &gt; Download" tab.
>
> If other settings are required, open the "Load preview" dialog using the "Online &gt; Download to device" command without permanently activating the dialog.

#### Result

The "Load preview" dialog is displayed before each loading into the simulation.

### Simulating a project (RT Unified)

#### Introduction

You simulate a project on the configuration PC and download the simulation via an Ethernet connection. The connection uses Ethernet port 20008.

> **Note**
>
> **Ethernet port 20008**
>
> If an application already occupies Ethernet port 20008, loading is not possible.
>
> If no connection to the target can be established, check the port assignments. If another application is using Ethernet port 20008, close this application.

#### Requirement

- The "SIMATIC WinCC Unified Runtime" component is installed on the configuration PC.
- The project is open in the configuration PC.
- The PLC and the HMI device have been compiled successfully.
- A user is configured.

#### Procedure

To start the simulation with enabled "Load preview" dialog, follow these steps:

| Symbol | Meaning |
| --- | --- |
| 1. Select one of the following buttons:    - From the shortcut menu of the HMI device: "Start simulation"    - In the toolbar: "Start simulation"    - Menu command "Online &gt; Simulation &gt; Start"    - Under "Visualization &gt; Simulate device" in the portal view.The compilation result is displayed in the Inspector window under "Info &gt; Compile".      | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | **Running runtime is stopped during complete download of a simulation** A project running in runtime is stopped when a simulation is completely loaded. |  |     | Symbol | Meaning |    | --- | --- |    | **Note**  **The "Load preview" dialog is skipped by default when simulating.** If necessary, activate the dialog under "Options &gt; Settings &gt; Simulation". |  | 2. Open the browser. 3. Call the URL "https://localhost" in the browser.    Instead of the name "localhost", you can use the PC name. 4. Select "WinCC Unified RT". 5. Enter the user name and password.    The configured screen is displayed as start screen in the browser. 6. Test, for example:    - Screen change and screen navigation    - Layout    - Internal tags 7. To stop the simulation, you have these options:    - Select "Online &gt; Stop runtime/simulation" in the menu bar.    - Select "Stop runtime/simulation" in the shortcut menu of the HMI device.While the simulation is running, the project is always loaded in simulation mode. |  |

> **Note**
>
> **Simulation and license**
>
> If no license is found for Runtime, an alarm appears and the simulation runs in demo mode. After 1 hour, you will be reminded that no license was found.

---

**See also**

[Basics of simulation (RT Unified)](#basics-of-simulation-rt-unified)
  
[Managing users in Runtime (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#managing-users-in-runtime-rt-unified)

### Simulating a central user management (RT Unified)

You want to simulate a project in which a central user management is configured for a customer. You have two options if you do not have access to the central user management of the customer:

- Configure your own central user management.
- Configure a local user management.

#### Requirement

- You know which groups and their function rights are contained in the central user management of the customer.

#### Configuring a central user management

Configure a central user management for the simulation project.

1. Create the users.
2. Create the user groups according to the customer project.
3. Assign the users to the groups.
4. Establish the connection to the central user management.
5. Start the simulation.
6. Log on in runtime.

Changes can be downloaded.

#### Configuring a local user management

Configure a local user management.

1. Create one or more users.
2. Assign the roles to the users.
3. Start the simulation.

Changes cannot be downloaded.

## Simulating Unified PC (RT Unified)

This section contains information on the following topics:

- [Basics of simulation (RT Unified)](#basics-of-simulation-rt-unified-1)
- [Enable "Load preview" dialog (RT Unified)](#enable-load-preview-dialog-rt-unified-1)
- [Simulating a project (RT Unified)](#simulating-a-project-rt-unified-1)
- [Simulating a central user management (RT Unified)](#simulating-a-central-user-management-rt-unified-1)

### Basics of simulation (RT Unified)

#### Introduction

You can use the simulator to test the performance of your runtime project on the configuration PC. This allows you to quickly locate any logical configuration errors before productive operation.

The simulation is compiled and downloaded just like a real project.

The project is downloaded as follows:

- The project is fully downloaded if the simulation of the project is not executed in runtime.
- If the simulation of the project is executed in runtime and changes can be compiled and downloaded, only changes are downloaded.

> **Note**
>
> **The "Load preview" dialog is skipped by default when simulating.**
>
> If necessary, activate the dialog under "Options &gt; Settings &gt; Simulation".

You recognize a simulation in the SIMATIC Runtime Manager by the "Simulation" type. A runtime project can be downloaded to the PC as a real project and as a simulation at the same time. You cannot run the real project and the simulation at the same time in runtime.

With an installed Runtime as of version V17, backward compatibility is also supported for simulations.

You can simulate runtime projects with a configured Runtime version of V16 or V17.

#### Field of application

You can use the simulator to test the following functions, for example:

- Screen change and screen navigation
- Internal tags
- Layout
- Configured alarms which are not triggered by a PLC

---

**See also**

[Simulating a project (RT Unified)](#simulating-a-project-rt-unified-1)
  
[Restrictions in compiling and loading changes (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#restrictions-in-compiling-and-loading-changes-rt-unified)
  
[Using PLCSIM (RT Unified)](Compiling%20and%20loading%20%28RT%20Unified%29.md#using-plcsim-rt-unified)

### Enable "Load preview" dialog (RT Unified)

The "Load preview" dialog is skipped by default when simulating projects.

In the "Load preview" dialog, make the settings for loading into the simulation. In addition, information on the HMI runtime and on the secured transmission is displayed.

To permanently select the "Load preview" dialog when simulating projects, follow these steps:

1. Open the settings under "Options &gt; Settings".
2. Select "Simulation".
3. In the "HMI Simulation" area, select the check box "Show 'Load preview' dialog during download to simulation".

#### Settings in the "Load preview" dialog

The "Load preview" dialog gives you the following setting options:

- Load Runtime:

  - Full download (default selection)
  - No action
- Runtime start:

  - Start runtime (default selection)
  - No action
- Runtime values:

  - Keep current values (default selection)
  - Reset to start values
  - Keep selected

    Options for tags, active alarms and user administration data in the drop-down menu
- Reset logs:

  - No reset (default selection)
  - Reset all

After loading, the selected settings are applied to the simulation for future loading processes.

> **Note**
>
> **Skipping the "Load preview" dialog**
>
> If you have not yet made any settings, the default selection is used. The settings used and the alarms that appear are displayed in the Inspector window in the "Info &gt; Download" tab.
>
> If other settings are required, open the "Load preview" dialog using the "Online &gt; Download to device" command without permanently activating the dialog.

#### Result

The "Load preview" dialog is displayed before each loading into the simulation.

### Simulating a project (RT Unified)

#### Requirement

- The "SIMATIC WinCC Unified Runtime" component is installed on the configuration PC.
- The project is open in the configuration PC.
- The PLC and the HMI device have been compiled successfully.
- A user is configured.

Always start the simulation in WinCC and then S7-PLCSIM.

If you have not installed the TIA Portal or S7-PLCSIM yourself, you must be a member in the following Windows user groups:

- PlcSimUsers
- RTIL Tracing Users
- Siemens TIA Engineer
- SIMATIC HMI
- SIMATIC HMI VIEWER

#### Procedure

To start the simulation, follow these steps:

| Symbol | Meaning |
| --- | --- |
| 1. Select one of the following buttons:    - From the shortcut menu of the HMI device: "Start simulation"    - In the toolbar: "Start simulation"    - Menu command "Online &gt; Simulation &gt; Start"    - Under "Visualization &gt; Simulate device" in the portal view.The compilation result is displayed in the Inspector window under "Info &gt; Compile".      | Symbol | Meaning |    | --- | --- |    |  | **Notice** |    | **Running runtime is stopped during complete download of a simulation** A project running in runtime is stopped when a simulation is completely loaded. |  |     | Symbol | Meaning |    | --- | --- |    | **Note**  **The "Load preview" dialog is skipped by default when simulating.** If necessary, activate the dialog under "Options &gt; Settings &gt; Simulation". |  | 2. Open the browser. 3. Call the URL "https://localhost" in the browser.    Instead of the name "localhost", you can use the PC name. 4. Select "WinCC Unified RT". 5. Enter the user name and password.    The configured screen is displayed as start screen in the browser. 6. Test, for example:    - Screen change and screen navigation    - Layout    - Internal tags 7. You have several options for stopping the simulation:    - Select "Online &gt; Stop runtime/simulation" in the menu bar.    - Select "Stop runtime/simulation" in the shortcut menu of the HMI device.As long as the simulation is running, the project is always loaded in simulation mode. |  |

> **Note**
>
> **Simulation and license**
>
> If no license is found for Runtime, an alarm appears and the simulation runs in demo mode. After 1 hour, you will be reminded that no license was found.

---

**See also**

[Basics of simulation (RT Unified)](#basics-of-simulation-rt-unified-1)
  
[Specify tag persistency (RT Unified)](Configuring%20tags%20%28RT%20Unified%29.md#specify-tag-persistency-rt-unified)

### Simulating a central user management (RT Unified)

You want to simulate a project in which a central user management is configured for a customer. You have two options if you do not have access to the central user management of the customer:

- Configure your own central user management.
- Configure a local user management.

#### Requirement

- You know which groups and their function rights are contained in the central user management of the customer.

#### Configuring a central user management

Configure a central user management for the simulation project.

1. Create the users.
2. Create the user groups according to the customer project.
3. Assign the users to the groups.
4. Establish the connection to the central user management.
5. Start the simulation.
6. Log on in runtime.

Changes can be downloaded.

#### Configuring a local user management

Configure a local user management.

1. Create one or more users.
2. Assign the roles to the users.
3. Start the simulation.

Changes cannot be downloaded.

---

**See also**

[Central user management (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#central-user-management-rt-unified)
  
[Managing central users and user groups (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#managing-central-users-and-user-groups-rt-unified)
  
[Specifying local or central user management (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#specifying-local-or-central-user-management-rt-unified)
  
[Managing local users (RT Unified)](Configuring%20users%20and%20roles%20%28RT%20Unified%29.md#managing-local-users-rt-unified)
