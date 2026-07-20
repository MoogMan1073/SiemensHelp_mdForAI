---
title: "Exchanging data with Inter Project Engineering (IPE)"
package: ProgTeamIPE2MenUS
topics: 7
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Exchanging data with Inter Project Engineering (IPE)

This section contains information on the following topics:

- [Basics of Inter Project Engineering (IPE)](#basics-of-inter-project-engineering-ipe)
- [Requirements for Inter Project Engineering (IPE)](#requirements-for-inter-project-engineering-ipe)
- [Overview for working with Inter Project Engineering (IPE)](#overview-for-working-with-inter-project-engineering-ipe)
- [Creating "Device proxy data" in the source project](#creating-device-proxy-data-in-the-source-project)
- [Creating an IPE file by means of the "Device proxy data"](#creating-an-ipe-file-by-means-of-the-device-proxy-data)
- [Secure communication via certificate (RT Professional)](#secure-communication-via-certificate-rt-professional)
- Using controller data from other projects with IPE

## Basics of Inter Project Engineering (IPE)

### Introduction to Inter Project Engineering (IPE)

The functionality of Inter Project Engineering, hereinafter referred to as IPE, is used to exchange the controller data in a source project between different projects with the help of a device proxy.

You can then transfer this data to other projects, for visualization in HMI, for example, and use it there for further configuration.

Inter Project Engineering gives you a simple way of providing controller data from a PLC programming across multiple projects for an HMI configuration.

Using the object "Device Proxy Data", you exchange controller data across multiple projects consistently and easily without redundant configuration work.

This makes it possible for HMI project engineers to work on a project without the hardware configuration having to be present in their project. This means they can work on the PLC project and on the HMI project at the same time.

You can exchange the following controller data between projects via the device proxy:

- Program blocks
- Technological objects
- PLC tags
- PLC alarms

The following data is automatically included in the exchange:

- Controller interfaces
- Configured communication processors and communication modules

This automatic data exchange ensures that the interfaces and the configured communication processors and modules are transferred along with the data you selected. This data is required to allow you to continue working consistently and without problems in your target project.

### Cross-project data exchange

The following options are available for cross-project data exchange with Inter Project Engineering:

- Exchanging controller data via IPE file
- Exchanging controller data via project file

### Exchanging controller data via IPE file

The figure below shows cross-project data exchange via an IPE file.

![Exchanging controller data via IPE file](images/127345413771_DV_resource.Stream@PNG-en-US.png)

The PLC controller data from the source project is transferred to the PLC in the target project via the object "Device Proxy Data".

PLC data that is exchanged via an IPE file must originate from TIA Portal projects of V13 or higher.

### Exchanging controller data via a project file

The figure below shows cross-project data exchange via a project file.

![Exchanging controller data via a project file](images/127345209995_DV_resource.Stream@PNG-en-US.png)

The PLC controller data from the source project is transferred to the PLC in the target project via a project file.

You can easily transfer and continue to use controller data from older TIA Portal projects as well as STEP 7 Classic projects that are not integrated in TIA Portal in your current TIA Portal projects.

However, this option depends on the device: If you transfer data from HMI devices, the TIA Portal versions of the source project and the target project must match.

### Inter Project Engineering (IPE)

The functionality of Inter Project Engineering, also referred to as "IPE", is used to exchange the controller data in a source project between different projects with the help of the "Device proxy data" object.

### IPE

The functionality of Inter Project Engineering, also referred to as "IPE", is used to exchange the controller data in a source project between different projects with the help of the "Device proxy data" object.

### IPE file

The IPE file includes CPU controller data from a source project which is transferred with the "Device proxy data" object to the CPU in the target project.

### Project file

The project file transfers CPU controller data from a source project to the CPU in the target project.

### Device proxy data

The "Device proxy data" object supports consistent data exchange of CPU controller data across projects between a source project and a target project without redundant configuration work.

### Data exchange across projects with IPE

The Inter Project Engineering (IPE) functionality gives you the following options for consistent data exchange across projects:

- Exchanging PLC data via an IPE file
- Exchanging controller data via a project file

Both files transfer CPU controller data from a source project to a CPU in the target project.

---

**See also**

[Requirements for Inter Project Engineering (IPE)](#requirements-for-inter-project-engineering-ipe)
  
[Overview for working with Inter Project Engineering (IPE)](#overview-for-working-with-inter-project-engineering-ipe)
  
[Creating "Device proxy data" in the source project](#creating-device-proxy-data-in-the-source-project)
  
[Creating an IPE file by means of the "Device proxy data"](#creating-an-ipe-file-by-means-of-the-device-proxy-data)

## Requirements for Inter Project Engineering (IPE)

### Software and hardware requirements

To use the functionality of Inter Project Engineering, the minimum software and hardware requirements for the installation of TIA Portal V13 or higher must be met.

The following requirements also apply:

- You have installed TIA Portal V13 or higher and the "SIMATIC STEP 7 Professional" software package.
- You are using a CPU of the S7-1200/1500 or S7-300/400 series.
- The same software version must be installed on all involved controllers.

### Requirements for IPE

The requirements for accepting controller data from projects are as follows:

- You have created a project with hardware configuration and PLC data that can be transferred to another project.
- You have made sure that the project is consistent before you transfer the controller data by means of the "Device proxy data" object.
- You are familiar with the defined procedures for Inter Project Engineering.

### Notes on compatibility mode

The functions for Inter Project Engineering are not available in compatibility mode.

---

**See also**

[Basics of Inter Project Engineering (IPE)](#basics-of-inter-project-engineering-ipe)
  
[Overview for working with Inter Project Engineering (IPE)](#overview-for-working-with-inter-project-engineering-ipe)
  
[Creating "Device proxy data" in the source project](#creating-device-proxy-data-in-the-source-project)
  
[Creating an IPE file by means of the "Device proxy data"](#creating-an-ipe-file-by-means-of-the-device-proxy-data)

## Overview for working with Inter Project Engineering (IPE)

### Exchanging controller data across projects

You can use the functionality of Inter Project Engineering to exchange existing controller data between different projects with the help of a "Device proxy" and to continue using this data in another project. The "Device proxy" enables easy and consistent cross-project data exchange without redundant configuration effort.

### Procedure for exchanging controller data via an IPE file

To exchange data via an IPE file, follow these steps:

1. Using TIA Portal, create a project with all required controller data and an executable user program.
2. Configure the hardware required for the project.
3. Compile the project to ensure consistency in your project.
4. In your project, create the object "Device Proxy Data" below the required CPU by clicking the corresponding command "Add device proxy data" in the "Device Proxy Data" folder.

   **Result**: The "Device Proxy Data" object has been created.
5. Select the required device proxy data in the project tree and double-click the object to open it in the editor.
6. Enter the required data for the device proxy data in the editor under "General" or apply the default setting. You can change the name and enter a comment for export of the controller data.

   In the "Define content" area of the editor select which of the existing controller data you wish to export as IPE file and click "Export device proxy data".
7. In the subsequent dialog, enter the name and storage location for the IPE file to be created and click "Save". You will be notified as soon as the export has been completed successfully.

   **Result**: The selected controller data has been exported as an IPE file.
8. In your target project, create a device proxy to be able to import the controller data contained in the IPE file. To do so, click the command "Add new device" and select the required device proxy in the dialog that opens.
9. Click the newly created device proxy and select the "Initialize device proxy" command from the shortcut menu.
10. Select the previously created IPE file to be used for the initialization, and confirm the selection in the following dialog with "OK". This starts the initialization.

    **Result**: The controller data from the source project contained in the IPE file is transferred to the device proxy in the target project.

After the successful exchange of controller data, you can continue with the configuration in your target project and, for example, connect PLC tags with HMI tags. The controller data can be updated as often as required when it is changed in the source project.

### Procedure for exchanging controller data via a project file

When exchanging controller data via a project file, device proxy data can either be predefined in the source project or it can be defined and selected from the target project.

Follow these steps to exchange data via a project file:

1. Using TIA Portal, create a project with all required controller data and an executable user program.
2. Configure the hardware required for the project.
3. Compile the project to ensure consistency in your project.
4. Open the TIA Portal project from which you want to import the controller data into the target project.
5. In your project, create the object "Device Proxy Data" below the required CPU by clicking the corresponding command "Add device proxy data" in the "Device Proxy Data" folder.

   **Result**: The "Device Proxy Data" object has been created.
6. Enter the required data for the device proxy data in the editor under "General" or apply the default setting. You can change the name and enter a comment for the device proxy data.
7. In the "Define content" area of the editor select which of the existing controller data you want to provide by means of the device proxy data.
8. Click "Save" to save the changes in the project.

   **Result**: You have successfully saved the selected controller data in your device proxy data.
9. In your target project, create a device proxy to import the controller data contained in the project file. To do so, click the command "Add new device" and select the required device proxy in the dialog that opens.
10. Click the newly created device proxy and select the "Initialize device proxy" command from the shortcut menu.
11. Select the previously created project file with the prepared device proxy data to be used for the initialization, and confirm the selection in the following dialog with "OK". This starts the initialization.

    **Result**: The controller data from the source project contained in the project file is transferred to the device proxy in the target project.

After the successful exchange of controller data, you can continue with the configuration in your target project and, for example, connect PLC tags with HMI tags. The controller data can be updated as often as required when it is changed in the source project.

### Procedure for updating already transferred controller data

**System requirements for the update:**

The following requirements must be met for updating already transferred controller data with the help of the already created "Device Proxy Data" object:

- You are using the same project for the update as for the previous transfer of the controller data.
- You are using the already created "Device Proxy Data" for transfer of the controller data.
- You have not made any changes to the hardware configuration or the communication interfaces in the meantime. You can add new hardware components.

**Updating procedure:**

1. Open the TIA Portal project from which you want to update the controller data in the target project.
2. Double-click the existing "Device Proxy Data" object and select under content which controller data you want to make available for the update.
3. Save the project or export the IPE file once again.
4. Open the required target project in the TIA Portal.
5. Click the existing device proxy in the target project and select the "Update device proxy" command from the shortcut menu.
6. Select the source which is to be used for the update, and confirm the selection.
7. In the following dialog, select under "Device" the CPU that was previously used as source, from which the controller data is to be re-imported.
8. Under "Defined device proxy data", select the required object and exit the dialog with "OK".
9. The update is then started and the selected device proxy data is transferred from the source project to the device proxy in the target project.

After the successful updating of the controller data, you can continue with the configuration in your target object and, for example, connect PLC tags with HMI tags. The controller data can be updated as often as required when it is changed in the source project.

---

**See also**

[Basics of Inter Project Engineering (IPE)](#basics-of-inter-project-engineering-ipe)
  
[Requirements for Inter Project Engineering (IPE)](#requirements-for-inter-project-engineering-ipe)
  
[Creating "Device proxy data" in the source project](#creating-device-proxy-data-in-the-source-project)
  
[Creating an IPE file by means of the "Device proxy data"](#creating-an-ipe-file-by-means-of-the-device-proxy-data)

## Creating "Device proxy data" in the source project

### Introduction

In order to exchange controller data across projects you require the "Device proxy data" object that can transfer the controller data of the associated CPU as an IPE file in the source project.

### Creating a "Device proxy data" object in the source project

Proceed as follows to create a new "Device proxy data" object:

1. Open the "Device proxy data" folder below the CPU to which you want to create a "Device proxy data".
2. Click the command "Add new device proxy data".

### Result

The "Device proxy data" object has been created and is displayed in the project navigation below the associated CPU.

The created "Device proxy data" contains the controller data of the associated CPU.

---

**See also**

[Overview for working with Inter Project Engineering (IPE)](#overview-for-working-with-inter-project-engineering-ipe)
  
[Basics of Inter Project Engineering (IPE)](#basics-of-inter-project-engineering-ipe)
  
[Requirements for Inter Project Engineering (IPE)](#requirements-for-inter-project-engineering-ipe)
  
[Creating an IPE file by means of the "Device proxy data"](#creating-an-ipe-file-by-means-of-the-device-proxy-data)

## Creating an IPE file by means of the "Device proxy data"

### Opening the "Device proxy data" and defining the content for an IPE file

Proceed as follows to create an IPE file by means of a "Device proxy data":

1. Open the required "Device Proxy Data" with a double-click in the "Device Proxy Data" folder in the project tree below the CPU.
2. Enter the required settings for the "Device proxy data" object in the editor under "General" or apply the default setting. You can change the name and enter a comment for export of the controller data.
3. In the "Define content" area of the editor select which of the existing controller data of the CU you wish to export as an IPE file and click "Export device proxy data".
4. In the subsequent dialog, enter the name and storage location for the IPE file to be created and click "Save". You will be notified as soon as the export has been completed successfully.

### Result

The selected controller data have been exported as an IPE file.

---

**See also**

[Overview for working with Inter Project Engineering (IPE)](#overview-for-working-with-inter-project-engineering-ipe)
  
[Basics of Inter Project Engineering (IPE)](#basics-of-inter-project-engineering-ipe)
  
[Requirements for Inter Project Engineering (IPE)](#requirements-for-inter-project-engineering-ipe)
  
[Creating "Device proxy data" in the source project](#creating-device-proxy-data-in-the-source-project)

## Secure communication via certificate (RT Professional)

Runtime Professional certificate-based communication has been enhanced.

### Overview

**Supported S7 PLCs**

WinCC Runtime Professional can communicate with the following S7 PLCs via certificates:

- S7-1500 PLCs as of firmware 2.9
- S7-1200 PLCs as of firmware 4.5

> **Note**
>
> All of the following statements apply only to S7 PLCs with this firmware.

**Expansions**

Certificate-based communication between Runtime Professional and S7 PLCs has been enhanced as follows:

- Communication between HMI devices and S7 PLCs with a non-integrated connection now supports self-signed certificates.
- Upgrading S7 PLCs has been simplified. Upgrading in the TIA Portal is no longer mandatory.

  An S7 PLCs that was only upgraded in the field now communicates with the HMI device via a self-signed certificate. The self-signed certificate is automatically loaded from the PLC into the certificate store of the HMI device.

To use these functions, enable the "ForceSecure" option on the HMI device.

**Using self-signed certificates**

The following self-signed certificate options are available:

- Use a self-signed certificate generated in the TIA Portal.

  Use the certificate created automatically when adding an S7 PLC or upgrading an existing S7 PLC. Or select certificate settings that differ from the default settings and generate a self-signed certificate yourself.

  When loaded, the certificate is copied to the Runtime project folder.
- Use a self-signed default certificate.

  Do not provide a certificate for the PLC in the TIA Portal and instead enable the "ForceSecure" option on the HMI device for the PLC connection type.

  A self-signed certificate is generated when loading to the PLC. The certificate is copied to the certificate store of the HMI device during the first attempt to make a connection between the PLC and the HMI device. After the certificate is copied to the folder with trusted certificates, it is used for communication.

### Enabling or disabling the "ForceSecure" option

**Introduction**

The "ForceSecure" option ensures that communication between the HMI device and the S7 PLC is protected by a certificate for the following connections:

- Non-integrated connections

- Connections for which no certificate has been configured in the TIA Portal

If the option is enabled and no PLC certificate is found in the Runtime project folder, Runtime searches for a suitable certificate in the "trusted" folder of the HMI device's certificate store.

> **Note**
>
> This option does not affect communication with S7 PLCs that do not support certificates.

**Default setting**

This option is disabled by default for integrated connections, non-integrated connections and device proxies.

**Procedure**

> **Note**
>
> It is recommended to enable the option for all connection types.

To configure the option for an HMI device, proceed as follows:

1. Create the "ForceSecure.xml" file.
2. Copy the following XML structure into the file:

   `<?xml version="1.0"?>`

   `<root>`

   `<NonIntegrated>true</NonIntegrated>`

   `<Integrated>true</Integrated>`

   `<IntegratedProxy>true</IntegratedProxy>`

   `</root>`
3. To disable certificate store evaluation for one of the connection types, set its node to "false".

   > **Note**
   >
   > Certificate-protected communication for non-integrated connections is not possible in this case.
   >
   > For integrated connections and device proxy, certificate-protected communication is possible only after upgrading the PLCs in the TIA Portal.
4. Copy the file on the engineering device into the TIA project directory of the project to which the HMI device was added into the following folder:

   "`…\AdditionalFiles\Rdp`"
5. Compile and download the HMI device.

   Your settings will be applied to the communication between the HMI device and its connected S7 PLCs.

To configure the "ForceSecure" option centrally for all projects created in the TIA Portal, proceed as follows:

1. Perform steps 1 to 3 as described above.
2. Copy the file on the engineering device into the program directory "C:\ProgramData\Siemens\Automation\ConfigFiles\RDP".
3. To use a different configuration for individual projects, proceed as described in steps 1 to 4 above.

If the XML file is located in the program directory and in the TIA project directory, the configuration from the project directory takes effect.

### Upgrading S7 PLCs

The following options are available when using self-signed certificates.

**Upgrading in the field without upgrading the S7 PLC in the TIA Portal**

Requirement:   
On the HMI device connected to an S7 PLC, the "ForceSecure" option is enabled for the S7 PLC connection type.

Procedure:

1. Upgrade the HMI device in the TIA Portal.
2. Replace the S7 PLC and the HMI device in the field.
3. Download the S7 PLC and the HMI device.

   After the download, the Runtime project folder does not contain a certificate for this S7 PLC.
4. Start Runtime.

   At the first attempt to make a connection, the self-signed certificate is automatically loaded from the S7 PLC. It ends up in the certificate store of the HMI device in the following folder:

   `%PROGRAMDATA%\Siemens\Automation\device-certificate-store\untrusted`
5. Copy the PLC certificate in the certificate store of the HMI device to the folder with the trusted certificates manually or per script:

   `%PROGRAMDATA%\Siemens\Automation\device-certificate-store\trusted\certs`

**Upgrading in the field and upgrading in the TIA Portal**

Procedure for integrated connections and device proxy:

1. Upgrade the S7 PLC and HMI device in the TIA Portal.
2. Replace the S7 PLC and the HMI device in the field.
3. Download the S7 PLC and the HMI device.

   After the download, the Runtime project folder contains the certificate for this S7 PLC.
4. Start Runtime.

   HMI device and PLC trust each other's certificates. There are no further steps for you.

Procedure for non-integrated connections:

1. Upgrade the S7 PLC and HMI device in the TIA Portal.
2. Enable the option "ForceSecure" for the non-integrated connection type for the HMI device.
3. Replace the PLC and the HMI device in the field.
4. Download the PLC and the HMI device.

   After the download, the Runtime project folder does not contain a certificate for this S7 PLC.
5. Start Runtime.

   At the first attempt to make a connection, the self-signed certificate is automatically loaded from the S7 PLC. It ends up in the certificate store of the HMI device in the following folder:

   `%PROGRAMDATA%\Siemens\Automation\device-certificate-store\untrusted`
6. Copy the PLC certificate in the certificate store of the HMI device to the folder with the trusted certificates manually or per script:

   `%PROGRAMDATA%\Siemens\Automation\device-certificate-store\trusted\certs`

   HMI device and PLC trust each other's certificates.

Alternatively, you can export the PLC certificate from the TIA Portal in advance and copy it to the "`...\trusted\certs`" folder before starting Runtime. The certificate file must have the following name:

"S7PlusChannel_<PLC_IP>.der", e.g. "S7PlusChannel_192.168.0.1.der"
