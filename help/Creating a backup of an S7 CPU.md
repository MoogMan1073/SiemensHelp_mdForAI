---
title: "Creating a backup of an S7 CPU"
package: ProgOnlineBackupenUS
topics: 10
devices: [PC, S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Creating a backup of an S7 CPU

This section contains information on the following topics:

- [Backup options for S7 CPUs](#backup-options-for-s7-cpus)
- [Backing up S7-300 and S7-400 CPUs (S7-300, S7-400, PC)](#backing-up-s7-300-and-s7-400-cpus-s7-300-s7-400-pc)
- [Backing up S7-1200 and S7-1500 CPUs (S7-1200, S7-1500, S7-1500T)](#backing-up-s7-1200-and-s7-1500-cpus-s7-1200-s7-1500-s7-1500t)

## Backup options for S7 CPUs

You will make a number of changes to your automation system over time, for example, add new devices, replace existing devices or adapt the user program. If these changes were to result in undesirable behavior, you can restore the automation plant to an earlier version. To continue working without interruptions after replacing individual devices, you can accept existing programs and values. The CPUs offer different options for backup and restoration of the hardware configuration and software.

### Backup options

The table below provides an overview of the backup and restoration options of S7 CPUs:

|  | Snapshot of the monitored values | Upload from device (software) | Upload device as new station (hardware and software) | Download backup from online device |
| --- | --- | --- | --- | --- |
| **Use case** | Restoring a specific status of a data block.  The actual values of data blocks including time stamp are accepted in the project. | Upload blocks on a CPU to the project. | Upload of hardware configuration and software from a device to the project. | Create a complete backup of a CPU as restore point. The backup copy is consistent and cannot be changed or opened. |
| **Requirement** | The CPU has already been created in a project. The data blocks must be identical online and offline. | The CPU is created in the project. | The device is available in the hardware catalog of TIA Portal. Any necessary HSPs or GSD files are installed. | - |
| **Possible in mode** | RUN, STOP | RUN, STOP | RUN, STOP | STOP |
| **Possible for F-CPUs** | Yes | Yes | Yes | Yes |
| **Backup can be edited** | Yes | Yes | Yes | No |

### Backup contents

The table below shows which data you can upload and back up with which options:

|  | Snapshot of the monitored values | Upload from device (software) | Upload device as new station (hardware and software)<sup>1</sup> | Backup from online device<sup>2</sup> |
| --- | --- | --- | --- | --- |
| **Data block**    **Actual value copied to snapshot** <sup>3</sup> | Yes | No | Yes | No |
| **Retentive data**    **Data block and bit memory** | No | No | Yes | Yes |
| **Software blocks** | No | Yes | Yes | Yes |
| **PLC tags (tag and constant names)** | No | Yes (for S7-1200 and S7-1500 CPUs) | Yes (for S7-1200 and S7-1500 CPUs) | Yes |
| **Technology objects** | No | Yes | Yes | Yes |
| **Trace configuration** | No | No | No | Yes |
| **Hardware configuration** | No | No | Yes | Yes |
| **Monitoring tables (web server)** | No | No | Yes | Yes |
| **Local data, bit memories, timers, counters and process image** | Yes | No | No | Yes |
| **Archives and recipes (PLC)** | No | No | No | Yes |
| **General data on the SIMATIC Memory Card, for example, help for program blocks or GSD files** | No | No | No | Yes |
| <sup>1</sup> Depending on which version of the TIA Portal was loaded. It can only be read again with the product version with which it was loaded.   <sup>2</sup> The "Backup from online device" type of backup backs up the actual values of the tags that are set as retentive. To ensure consistency of the retentive data, disable all write access to retentive data during the backup, in order to, for example, avoid HMI write accesses when backing up.   <sup>3</sup> Actual values of the non-retentive data are reset to their start values during a transition from STOP to RUN mode. When the CPU is backed up only the start values of non-retentive data are backed up. |  |  |  |  |

### Special considerations during backup of actual values

The "Backup from online device" type of backup backs up the actual values of the tags that are set as retentive. To ensure consistency of the retentive data, disable all write access to retentive data during the backup.

---

**See also**

[Creating a backup of a device (S7-300, S7-400, PC)](#creating-a-backup-of-a-device-s7-300-s7-400-pc)
  
[Creating a backup of a device (S7-1200, S7-1500)](#creating-a-backup-of-a-device-s7-1200-s7-1500)
  
[General information on loading](Editing%20project%20data.md#general-information-on-loading)
  
[Downloading project data to a device](Editing%20project%20data.md#downloading-project-data-to-a-device)
  
[Downloading project data to a memory card](Editing%20project%20data.md#downloading-project-data-to-a-memory-card)
  
[Uploading project data from a device](Editing%20project%20data.md#uploading-project-data-from-a-device)
  
[Loading project data from a memory card](Editing%20project%20data.md#loading-project-data-from-a-memory-card)

## Backing up S7-300 and S7-400 CPUs (S7-300, S7-400, PC)

This section contains information on the following topics:

- [Creating a backup of a device (S7-300, S7-400, PC)](#creating-a-backup-of-a-device-s7-300-s7-400-pc)
- [Restoring the software and hardware configuration of a device (S7-300, S7-400, PC)](#restoring-the-software-and-hardware-configuration-of-a-device-s7-300-s7-400-pc)
- [Backing up a device configuration (S7-300, S7-400, PC)](#backing-up-a-device-configuration-s7-300-s7-400-pc)

### Creating a backup of a device (S7-300, S7-400, PC)

#### Backing up the software and hardware configuration of an S7-300/400 CPU

If you have already downloaded a configuration to an S7-300/400 CPU, it is advisable to make a backup. You may have modified the configuration and want to test the new configuration. Before you download the new configuration to the CPU, you can create a backup of the current device state and then restore the current configuration at a later date. The backup is performed with the current values of the CPU. In the case of S7-400 CPUs with fail-safe function, the initial values are backed up.

You can create as many backups as you want and store a variety of configurations for a CPU. The backups are named with the name of the CPU and the time and date of the backup. You can find the backup in the project tree under the CPU in the "Online backups" folder.

The following figure shows an example of an S7 CPU for which two backups were created:

![Backing up the software and hardware configuration of an S7-300/400 CPU](images/142136952971_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Backup options for S7 CPUs](#backup-options-for-s7-cpus)

### Restoring the software and hardware configuration of a device (S7-300, S7-400, PC)

If you have backed up the configuration of a device at an earlier point in time, you can transfer the backup back to the device. The saved configuration is then restored on the device.

#### Requirement

You must have previously configure the device and stored a backup of the device in the project.

#### Procedure

To restore older software and hardware state on a device, follow these steps:

1. Open up the folder of the device in the project tree to display the lower-level objects.
2. Open the "Online backups" folder.
3. Select the backup you want to restore.
4. In the "Online" menu, select the "Download to device" command.

   - If you had previously established an online connection, the "Load preview" dialog opens. This dialog displays alarms and recommends actions needed for the loading operation.
   - If you had not previously established an online connection, the "Extended download to device" dialog opens, and you must first select the interfaces via which you want to establish the online connection to the device.

     See also: [Establishing and terminating an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
5. Check the alarms in the "Load preview" dialog, and select the actions in the "Action" column, if necessary.
6. As soon as downloading becomes possible, the "Load" button is enabled.
7. Click the "Load" button.

   The backup is transferred to the device and device is restored. The "Load results" dialog then opens. In this dialog, you can check whether or not the loading operation was successful and take any further action that may be necessary.
8. Click the "Finish" button.

**Note**

Performing the proposed actions during operation of the plant can cause serious damage to property or injury to persons if there are functional disturbances or program errors.

---

**See also**

[Function right "Download PLC"](Managing%20users%20and%20roles.md#function-right-download-plc)

### Backing up a device configuration (S7-300, S7-400, PC)

You can back up the configuration of an S7-300/400 CPU in the TIA Portal. So you can download and test a new configuration to a device without any risk. If needed, you can restore the initial configuration of the CPU.

#### Requirement

- The CPU has already been created in the project.
- The CPU is online. If there is no online connection yet, an online connection is established during the backup.

#### Procedure

To create a backup of the current configuration of a CPU, follow these steps:

1. Select the CPU in the project tree.
2. Select the "Backup from online device" command in the "Online" menu.

#### Result:

A backup of the entire hardware configuration and software is created. The backup is stored in the project tree in the "Name of the CPU &gt; Online backups" folder. The backup is assigned the name of the CPU with the time and date of the backup. You can rename the backup, but you cannot make any changes to the contents of the backup.

## Backing up S7-1200 and S7-1500 CPUs (S7-1200, S7-1500, S7-1500T)

This section contains information on the following topics:

- [Creating a backup of a device (S7-1200, S7-1500)](#creating-a-backup-of-a-device-s7-1200-s7-1500)
- [Backing up a device configuration (S7-1200, S7-1500)](#backing-up-a-device-configuration-s7-1200-s7-1500)
- [Restoring the configuration of a device (S7-1200, S7-1500)](#restoring-the-configuration-of-a-device-s7-1200-s7-1500)

### Creating a backup of a device (S7-1200, S7-1500)

#### Backing up the software and hardware configuration of a CPU

If you have already downloaded a configuration to an S7-1200/S7-1500 CPU, it may be useful to make a backup. You may have modified the configuration and want to test the new configuration. Before you download the new configuration to the CPU, create a backup of the current device version. You can restore the current configuration at a later time.

You can create as many backups as you want and store a variety of configurations for a CPU. The backups are named with the name of the CPU and the time and date of the backup. You can find the backup in the project tree under the CPU in the "Online backups" folder.

The following figure shows an example of an S7 CPU for which two backups were created:

![Backing up the software and hardware configuration of a CPU](images/142136952971_DV_resource.Stream@PNG-en-US.png)

#### Scope of the backup

The backup includes all data that are needed to restore a particular configuration version of a CPU. The following data is backed up, for example:

- Contents of the memory card, if present
- Retentive memory areas for example of data blocks, counters, and bit memory
- Other retentive memory contents, such as IP address parameters

The backup is performed with the current values of the CPU. Entries in the diagnostics buffer are not included in the backup, and neither is the current time.

The backup does not contain the password to protect confidential PLC configuration data.

#### Creating a backup using a different method

You can also create a backup using the SIMATIC Automation Tool (SAT) or the standard web page "Online backup" of the web server.

- If you back up files using STEP 7, STEP 7 saves the files in the STEP 7 project.
- If you back up files using the web server, your programming device/PC saves the backup files in the standard folder for downloads.

The following rules apply:

- You cannot restore STEP 7 backups using the web server.
- You cannot restore web server backups using STEP 7.

However, you can save STEP 7 backups directly in the download folder of your programming device. A backup stored in this way can be restored using the web server. To save the backup on your programming device, follow these steps:

1. In the project tree, right-click on a file in the "Online backups" folder.
2. Select "Save as" in the shortcut menu.
3. Navigate to the folder in which you want to save the file, e.g. the standard folder for downloads on your programming device.
4. Click "Save".

---

**See also**

[General information on loading](Editing%20project%20data.md#general-information-on-loading)
  
[Backup options for S7 CPUs](#backup-options-for-s7-cpus)
  
[Protection of confidential configuration data (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#protection-of-confidential-configuration-data-s7-1200-s7-1500-s7-1500t)

### Backing up a device configuration (S7-1200, S7-1500)

You can back up a functional configuration of a CPU in the TIA Portal and access it at a later time; this means you can then restore the backup. This allows you to load a modified configuration, for example, to test product enhancements, to change programs for troubleshooting in the system or you can replace components on a test basis. You can then restore the initial configuration of the CPU.

The CPU goes to STOP while a backup is being created. If an access level is configured for the CPU, you need the password for read access to the CPU.

#### Requirement

- The CPU has already been created in the project.
- The device is connected to the programming device/PC directly via the PROFINET interface of the CPU. PROFIBUS interfaces of the CPU and interfaces of CMs/CPs are not supported.
- The CPU is online. If there is no online connection yet, an online connection is established during the backup.
- The CPU is in "STOP" mode.

#### Procedure

To create a backup of the current configuration of a CPU, follow these steps:

1. Select the CPU in the project tree.
2. Select the "Backup from online device" command in the "Online" menu.

   If necessary, you must enter the password for read access to the CPU and confirm that the CPU should enter "STOP" mode.

#### Result:

A backup of the entire hardware configuration and software is created. The backup is stored in the project tree in the "Name of the CPU &gt; Online backups" folder. The backup is assigned the name of the CPU with the time and date of the backup. You can rename the backup, but you cannot make any changes to the contents of the backup.

An entry is created for each backup operation in the diagnostic buffer of the CPU.

---

**See also**

[Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
  
[Restoring the configuration of a device (S7-1200, S7-1500)](#restoring-the-configuration-of-a-device-s7-1200-s7-1500)

### Restoring the configuration of a device (S7-1200, S7-1500)

If you have backed up the configuration of a device at an earlier point in time, you can transfer the backup back to the device. The saved configuration is then restored on the device.

The CPU goes to STOP while a backup is being loaded to the CPU. If an access level is configured for the CPU, you need the password for write access to the CPU.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Download backups with unknown content**  If you activate the recommended actions during download during plant operation, you can cause serious damages or injuries in case of malfunctions or program errors.  Make sure that the backup contents do not include a configuration which results in unexpected plant behavior. |  |

#### Requirement

- The device is configured and a backup of the device is stored in the project.
- The device is connected to the programming device/PC directly via the PROFINET interface of the CPU.
- The CPU is in "STOP" mode.
- You have the password for read access to the CPU, if an access level was configured.

#### Procedure

To restore older software and hardware state on a device, follow these steps:

1. Open up the folder of the device in the project tree to display the lower-level objects.
2. Open the "Online backups" folder.
3. Select the backup you want to restore.
4. In the "Online" menu, select the "Download to device" command.

   - If you had previously established an online connection, the "Load preview" dialog opens. This dialog displays alarms and recommends actions needed for the loading operation.
   - If you had not previously established an online connection, the "Extended download to device" dialog opens, and you must first select the interfaces via which you want to establish the online connection to the device.

     See also: [Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
5. Check the alarms in the "Load preview" dialog, and select the actions in the "Action" column, if necessary.
6. As soon as downloading becomes possible, the "Load" button is enabled.
7. Click the "Load" button.

   The backup is transferred to the device and device is restored. The "Load results" dialog then opens. In this dialog, you can check whether or not the loading operation was successful and take any further action that may be necessary.
8. Click the "Finish" button.

   If necessary, you must enter the password for read access to the CPU and confirm that the CPU should enter "STOP" mode.

   The contents of the backup are restored on the CPU. The CPU is then restarted.

---

**See also**

[Establishing or changing an online connection](Using%20online%20and%20diagnostics%20functions.md#establishing-or-changing-an-online-connection)
  
[Function right "Download PLC"](Managing%20users%20and%20roles.md#function-right-download-plc)
