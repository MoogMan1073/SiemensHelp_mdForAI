---
title: "Functions for Startdrive"
package: SdrOpennessenUS
topics: 70
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Functions for Startdrive

This section contains information on the following topics:

- [Introduction](#introduction)
- [Security information](#security-information)
- [TypeIdentifier - identifier of the components](#typeidentifier---identifier-of-the-components)
- [References](#references)
- [Code examples](#code-examples)

## Introduction

Using TIA Portal-Openness, you automate the engineering and control the TIA Portal using a program that you created yourself.

In this help document, you can find a lot of information and code examples for this program that you generate yourself. You can also generate and use your own programs for the TIA Portal "Startdrive" application.

Before you configure your own program for Startdrive from the subsequently listed code example, please carefully observe the general information relating to Openness, which you can find under the following keywords in this information system:

- [Preconditions for using TIA Portal Openness](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#requirements-for-tia-portal-openness)
- [Install TIA Portal Openness](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#installing-tia-portal-openness)
- [Access the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#accessing-the-tia-portal)
- [TIA Portal Openness object model](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#tia-portal-openness-object-model)
- [Programming steps](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#programming-steps)

> **Note**
>
> **Activated project protection (UMAC)**
>
> If you want to edit a project for which a project protection is activated via "Openness API", you need to have the corresponding access rights for this purpose. Your user account must have the following function rights:
>
> - Change project via Openness API
> - Open and edit the project
> - Open the project read-only
>
> Additional function rights are required for technology objects. If you do not have any access rights, contact your administrator.
>
> For drives as of SINAMICS FW V6.1 or higher, you require the same access rights for your user account to access the drive online as in Startdrive.
>
> Additional information on access rights and on user administration in general is provided on Page "User administration and Security".

## Security information

This section contains information on the following topics:

- [Encrypted communication with SecureString passwords](#encrypted-communication-with-securestring-passwords)
- [Passwords in TIA Openness](#passwords-in-tia-openness)

### Encrypted communication with SecureString passwords

> **Note**
>
> **SecureString passwords for secure communication**
>
> In order to secure communication between Openness API and the TIA Portal when using Startdrive Openness functions, use passwords which have been encrypted with a SecureString.

> **Note**
>
> **Direction of communication**
>
> It is only possible to use SecureString passwords when downloading Openness functions to the TIA Portal and not in the opposite communication direction.

> **Note**
>
> A SecureString object should never be constructed from a String because the sensitive data is already subject to the memory persistence consequences of the immutable String class. The best way to construct a SecureString object is from a character-at-a-time unmanaged source, such as the Console.ReadKey method.

> **Note**
>
> The API user is responsible for security measures when handling passwords using code.

You can find more information on configuring SecureString passwords in the code examples [download](#download) and [Creating SecureString passwords](#how-to-assign-a-securestring-password).

---

**See also**

[Passwords in TIA Openness](#passwords-in-tia-openness)

### Passwords in TIA Openness

#### Handling passwords in TIA Openness

Password handling in Startdrive Openness is based on TIA Openness.

Please carefully observe the general information relating to passwords in TIA Openness, which you can find under the following keywords in this help:

- [Defining the display password](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#setting-a-display-password)
- [Handling PLC passwords linked to blocks](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#handling-plc-block-binding-passwords)
- [Password protection for PLCs](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#protecting-plc-through-password)
- [Setting protection levels](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#access-level-setting)
- [Block protection and unprotection](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#setting-and-removing-protections-from-a-block)
- [Loading hardware, software and files into the PLC device](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#uploading-plc-device)

---

**See also**

[Encrypted communication with SecureString passwords](#encrypted-communication-with-securestring-passwords)

## TypeIdentifier - identifier of the components

Each version of any Startdrive component comprises a unique number, which is called the TypeIdentifier . In the Openness program code, you can use these TypeIdentifiers in order to uniquely identify and name a component.

In Startdrive, the display of the TypeIdentifier is optional, and deactivated as default.

### Activating the display of the TypeIdentifier in Startdrive

1. In the Startdrive project view, select menu "Options > Settings".

   The "Settings" configuration area opens.
2. Select "Hardware configuration" in the secondary navigation.
3. Activate the option "Activate display of the Type Identifier for devices and modules".

   The display of the TypeIdentifier is now active.

### Reading out the TypeIdentifier in Startdrive

In a Startdrive project, the TypeIdentifier can be read out at the following locations when the display is active:

- For all components (in the inspector window):
- For Control Units (when creating a drive device)

To read out the TypeIdentifier for a component in the inspector window, proceed as follows:

1. In the device view of the Startdrive project, double-click on the required component.

   The inspector window opens. The active component version is shown in the list.
2. The associated TypeIdentifiers are listed in the outer right-hand column. Example: `OrderNumber:6SL3131-7TE23-6Axx`

   Copy this TypeIdentifier to your Openness application.

Proceed as follows to read out the TypeIdentifier for a Control Unit:

1. In the Startdrive project navigation, double click on "Add new device".

   The dialog with the same name opens.
2. Select the required control module from the selection.

   The TypeIdentifier (under the article number and firmware number) for the corresponding Control Unit is displayed to the right in the detailed display. Example: `OrderNumber:6SL3040-1MA01-0Axx/V5.2/S120`
3. Copy this TypeIdentifier to your Openness application.

## References

This section contains information on the following topics:

- [AddressComposition](#addresscomposition)
- [AddressContext](#addresscontext)
- [AddressIoType](#addressiotype)
- [Commissioning](#commissioning)
- [ConfigurationEntry](#configurationentry)
- [DriveDataEncryption (from SINAMICS FW V6.1)](#drivedataencryption-from-sinamics-fw-v61)
- [DriveDomainFunctions](#drivedomainfunctions)
- [DriveObject](#driveobject)
- [DriveObjectActivation](#driveobjectactivation)
- [DriveObjectContainer](#driveobjectcontainer)
- [ModuleAccessPoint](#moduleaccesspoint)
- [DriveObjectTypeHandler](#driveobjecttypehandler)
- [DriveParameter](#driveparameter)
- [DriveParameterComposition](#driveparametercomposition)
- [HardwareProjection](#hardwareprojection)
- [EncoderConfiguration](#encoderconfiguration)
- [MotorConfiguration](#motorconfiguration)
- [OnlineDriveObject](#onlinedriveobject)
- [OnlineDriveObjectContainer](#onlinedriveobjectcontainer)
- [StartDriveDownloadCheckConfiguration](#startdrivedownloadcheckconfiguration)
- [SafetyTelegram](#safetytelegram)
- [TechnologyExtension](#technologyextension)
- [TechnologyExtensionComposition](#technologyextensioncomposition)
- [TechnologyExtensionInstallationProvider](#technologyextensioninstallationprovider)
- [TechnologyExtensionPackage](#technologyextensionpackage)
- [Telegram](#telegram)
- [TelegramComposition](#telegramcomposition)
- [TelegramType](#telegramtype)
- [TorqueTelegram](#torquetelegram)
- [AxisEncoderHardwareConnectionInterface](#axisencoderhardwareconnectioninterface)
- [UmacConfiguration (from SINAMICS FW V6.1)](#umacconfiguration-from-sinamics-fw-v61)
- [UpdateCheckSums (from SINAMICS FW V6.1)](#updatechecksums-from-sinamics-fw-v61)

### AddressComposition

#### AddressComposition

The `AddressComposition` class represents the address of a telegram.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

`public sealed class AddressComposition`

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `IoType` | [AddressIoType](#addressiotype) | Returns information on the type of the address. |
| `Context` | [AddressContext](#addresscontext) | Returns information on the context of the address. |
| `StartAddress` | `Int32` | Returns the start address of the telegram or specifies it. |
| `Length` | `Int32` | Returns the length of the telegram. |

---

**See also**

[TelegramType](#telegramtype)

### AddressContext

#### AddressContext

The Enum AddressContext contains information on the context of the address.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

public enum AddressContext

The following table describes the **enum entries**:

| Name | Description |
| --- | --- |
| `AddressContext.None` | No context has been found for the address |
| `AddressContext.Device` | Context is a device address |
| `AddressContext.Head` | Context is a head address |

### AddressIoType

#### AddressIoType

The Enum AddressIoType contains information on the type of the address.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

public enum AddressIoType

The following table describes the **enum entries**:

| Name | Description |
| --- | --- |
| `AddressIoType.None` | The IO type cannot be used |
| `AddressIoType.Input` | Type is an input address |
| `AddressIoType.Output` | Type is an output address |
| `AddressIoType.Diagnosis` | Type is a diagnosis address |
| `AddressIoType.Substitute` | Type is a substitute address |

### Commissioning

#### Commissioning

The `Commissioning` class is used for commissioning a drive. It can be applied to `DriveFunctionInterface` or `OnlineDriveFunctionInterface`. If the user uses the function for a SINAMICS S drive, it returns the return value zero.

The following table describes the **methods** of the class:

| Name | Parameter | Return value | Description |
| --- | --- | --- | --- |
| `SetSimoGearMlfb` | string simoGearMlfb | bool | Sets the SIMOGEAR Article No. of a drive. |

---

**See also**

[Setting the SIMOGEAR article number for G115D drives](#setting-the-simogear-article-number-for-g115d-drives)

### ConfigurationEntry

#### ConfigurationEntry

Class `ConfigurationEntry` is used to save parameter data, which can be determined from the `ConfigurationEntryCompositions` of a motor or encoder configuration.

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `EnumValueList` | `IDictionary<it, string>` | Returns a list with possible values of the enum parameter. |
| `MaxValue` | `object` | Maximum value of the `ConfigurationEntry`. |
| `MinValue` | `object` | Minimum value of the `ConfigurationEntry`. |
| `Name` | `string` | Name of the `ConfigurationEntry`. |
| `Number` | `int` | Numerical representation of the name for `ConfigurationEntry`. |
| `Description` | `string` | Description of the `ConfigurationEntry`. |
| `Parent` | `IEngineeringObject` | Engineering Object model-parent element of this object. |
| `Unit` | `string` | Unit of the `ConfigurationEntry`. |
| `Value` | `object` | Value of the `ConfigurationEntry`. |

### DriveDataEncryption (from SINAMICS FW V6.1)

Class `DriveDataEncryption` allows the encryption of drive data (DDE, Drive Data Encryption) for SINAMICS drives from firmware version V6.1 to be activated and deactivated with Openness.

The following table describes the **methods** of class `DriveDataEncryption`:

| Name | Parameter | Return value | Description | Exceptions |
| --- | --- | --- | --- | --- |
| `Activate` | SecureString password | bool | Activate `DriveDataEncryption` with password. | - |
| `Deactivate` | SecureString password | bool | Deactivate `DriveDataEncryption` with password. | - |

> **Note**
>
> **`Security` class**
>
> The `Security` class is a higher-level class. The class is used in the background to access all APIs that are involved in security.

### DriveDomainFunctions

#### DriveDomainFunctions

Class `DriveDomainFunctions` is used to restore the factory settings or the backup of the RAM content to the ROM.

It can only be applied to an `OnlineDriveFunctionInterface` object.

For G120 drives, the `DriveDomainFunctions` object can only be accessed if the Power Module is connected to the device. Otherwise, null or an exception is returned.

The following table describes the **methods** of the class:

| Name | Description |
| --- | --- |
| `PerformFactoryReset` | This method is responsible for restoring the factory settings. |
| `PerformRAMtoROMCopyAllDriveObject` | The date of all drive objects is written from the RAM to the memory card/hard disk. |

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `Parent` | `IEngineeringObject` | Engineering Object model-parent element of this object. |

### DriveObject

#### DriveObject

The `DriveObject` class allows access to the drive object. Access to the drive parameters or the telegram is possible via the drive object, for example.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

`public sealed class DriveObject`

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `Parameters` | [DriveParameterComposition](#driveparametercomposition) | Returns a list with the available parameters of the drive object. |
| `Telegrams` | [TelegramComposition](#telegramcomposition) | Returns a list with the available telegrams of the drive object.  The list can be changed with class `TelegramComposition`. |

---

**See also**

[Determining a drive object](#determining-a-drive-object)

### DriveObjectActivation

#### DriveObjectActivation

Class `DriveObjectActivation` is used to activate the modules or determine the module status. It can be applied to `DriveObjectFunctions` from `DriveFunctionInterface` or `OnlineDriveFunctionInterface`.

The following table describes the **methods** of the class:

| Name | Description |
| --- | --- |
| `ChangeActivationState(DriveObjectActivationState)` | Changes the activation status of the drive object. Returns false if the operation cannot be completed.   Possible status values:   - Deactivate - Activate - DeactivateAndNotPresent |

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `ActivationState` | `DriveObjectActivationState` | Returns the actual status value. |
| `IsActive` | `Boolean` | For an active drive object, returns true. |

### DriveObjectContainer

#### DriveObjectContainer

The `DriveObjectContainer` is a service of the drive object (`DeviceItem`) for the current device (`Device`).

The following table describes the **navigators** of the `DriveObjectContainer`:

| Name | Data type | Description |
| --- | --- | --- |
| `DriveObjects` | [DriveObjectComposition](#driveparametercomposition) | Returns a list with the available drive objects. The drive objects allow access to the drive parameters and telegrams. |
| `Parent` | IEngineeringObject | Engineering Object model-parent element of this object. |

### ModuleAccessPoint

#### ModuleAccessPoint

The `ModuleAccessPoint` is a service of the drive object (`DeviceItem`) for the current device (`Device`).

The following table describes the **properties** of the Hardware Identifier of the `ModuleAccessPoint`:

| Name | Data type | Access | Description |
| --- | --- | --- | --- |
| `Hardware identifier` | `IEnumerable<IBrowsable>` | ReadOnly | Returns the list of hardware identifiers. |

### DriveObjectTypeHandler

#### DriveObjectTypeHandler

Class `DriveObjectTypeHandler` is used to switch over the drive object type for every drive object and to determine the drive object type - as well as all possible drive object types of the actual drive object. It can only be applied to `DriveFunctionInterface`.

The following table describes the **methods** of the class:

| Name | Description |
| --- | --- |
| `ChangeDriveObjectType((target)DriveObjectType)` | Changes the actual type of the drive object to a new type that can be selected.   Returns false if the operation cannot be completed. |

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `PossibleDriveObjectTypes` | `DriveObjectTypeComposition` | The use of `targetDriveObjectType` results in an exception on the actual drive object. |
| `CurrentDriveObjectType` | `DriveObjectType` | Indicates the currently assigned drive object type. |

### DriveParameter

#### DriveParameter

The `DriveParameter` class allows access to a drive parameter. Not all drive parameters are available for access via Openness.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

public sealed class DriveParameter

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `ArrayIndex` | `Int32` | Returns the index of an array parameter.  Value range: 0-7FFF  The index is -1 for parameters without array   **Example**    `p108[4].15`     `par.ArrayIndex` produces 4 |
| `ArrayLength` | `Int32` | Returns the number of array elements.  The index is 0 for parameters without an array |
| `Bits` | [DriveParameterComposition](#driveparametercomposition) | Returns an `DriveParameter` object for one bit of the parameter.  In this way, for example, the value or the name of the bit parameter can be read from a bit parameter.   **Example**    `DriveParameter param133 = cu.Parameters.Find(133, 0);`    `DriveParameter param133Bit1 = param133.Bits[1];`    `String paramName = param133Bit1.Name;` |
| `EnumValueList` | `IDictionary<int, string>` | Returns a list with possible values of the enum parameter.  For example `<1, [1] Quick commissioning>`   `null`, if the parameter is not a parameter of the `Enum` type. |
| `MaxValue` | `Object` | Returns the maximum value for the currently selected unit. |
| `MinValue` | `Object` | Returns the minimum value for the currently selected unit. |
| `Name` | `string` | Returns the name of the parameter. E.g. `"p108[0].2"` |
| `ParameterText` | `string` | Returns the text of the short description for the parameter. |
| `Number` | `Int32` | Returns the number of the parameter.   **Example**    `p108[0].2`   The return value is 108 |
| `Unit` | `string` | Returns the unit of the parameter as text. |
| `Value` | `Object` | Returns the offline/online value of the parameter or writes a value onto the parameter.  If the event of write errors, an `EngineeringTargetInvocationException` is triggered.   **Examples**   - `P2080Bit6.Value = 0;` - `P2080Bit6.Value = cu.Parameters.Find("r19");`    **BICO source**   The parameters of a BICO source can only be read   **BICO signal sinks**   Possible values are 0, 1 or a `DriveParameter` object.  A `DriveParameter` object is returned when the BICO signal sink is connected to a different parameter.   See also example [Reading and writing BICO parameters](#reading-and-writing-bico-parameters). |

---

**See also**

[Reading and writing parameters](#reading-and-writing-parameters)

### DriveParameterComposition

#### DriveParameterComposition

The `DriveParameterComposition` class allows access to parameters of the drive. Not all drive parameters are approved for access via Openness.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

public sealed class DriveParameterComposition

The following table describes the **methods** of the class:

| Name | Description |
| --- | --- |
| `Find(string)` | Returns the [DriveParameter](#driveparameter) object for which a search is being made via the name.   `null` if the parameter is not found   **Example**    `Find("P108[1]");` |
| `Find(UInt16, Int32)` | Returns the [DriveParameter](#driveparameter) object for which a search is being made via the parameter index and array index.   `null` if the parameter is not found   **Examples**   - `cu.Find(108, 1);` - `cu.Find(51, -1);` |

### HardwareProjection

Class `HardwareProjection` is responsible for commissioning the motor and the encoder. The object can be found for `DriveFunctionInterface` and `OnlineDriveFunctionInterface`.

For G120 drives, motors and encoders can be configured both online and offline. On the other hand, for S120 drives, configuration is only possible offline.

For G120 drives, the `HardwareProjection` object can only be accessed if the Power Module is inserted in the drive device. Otherwise, when calling functions `HardwareProjection`, a null or an exception is returned.

For an offline configuration, use the hardware configuration of the `DriveFunctionInterface`. For an online configuration, use the hardware configuration of the `OnlineDriveFunctionInterface`.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives`    `Siemens.Engineering.MC.Drives.DFI`    `Siemens.Engineering.MC.Drives.Enums` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **methods** of the class:

| Name | Parameter | Return value | Description | Exceptions |
| --- | --- | --- | --- | --- |
| `SetMotorType` | MotorType type, ushort driveDataSet | bool | Sets the motor type at the Control Unit (only for G120). | Only available for G120 drives. |
| `GetCurrentMotorConfiguration`   For S120:   `GetCurrentMotorConfiguration(ushort motorDataset)` | ushort driveDataSet | MotorConfiguration | Depending on the data set number of the drive, determines the currently existing configuration area. | - |
| `ProjectMotorConfiguration` | MotorConfiguration motConfig, ushort driveDataSet | bool | Configures the motor configuration of a drive device depending on the data set number of the drive. | - |
| `SetEncoder` | EncoderType type, EncoderInterface interfaceType, AbsoluteIncrementalFlag absIncFlag, RotaryLinearFlag rotLinFlag, ushort encoderNumber | bool | Sets the encoder at the Control Unit (only for G120). | Only available for G120 drives. |
| `GetCurrentEncoderConfiguration` | ushort encoderNumber | EncoderConfiguration | Depending on the data set number of the encoder, determines the currently existing configuration area. | - |
| `ProjectEncoderConfiguration` | EncoderConfiguration encConfig, ushort enccoderNumber | bool | Configures the motor configuration of a drive device depending on the data set number of the encoder. | - |

The following table describes the **properties** of the class:

| Name | Data type | Access | Description |
| --- | --- | --- | --- |
| `Parent` | `IEngineeringObject` | ReadOnly | Engineering Object model-parent element of this object. |

---

**See also**

[Connecting technology objects with hardware modules via telegram objects](#connecting-technology-objects-with-hardware-modules-via-telegram-objects)

### EncoderConfiguration

#### EncoderConfiguration

Class `EncoderConfiguration` saves data of non-Siemens encoders.

- The user must populate the `ConfigurationEntryComposition` object.
- Object `RequiredConfigurationEntries` must also be populated.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives`    `Siemens.Engineering.MC.Drives.DFI`    `Siemens.Engineering.MC.Drives.Enum` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **properties** of the class:

| Name | Data type | Access | Description |
| --- | --- | --- | --- |
| `RequiredConfigurationEntries` | `ConfigurationEntryComposition` | ReadOnly | Accessible configuration inputs of EncoderConfiguration. |
| `Parent` | `IEngineeringObject` | ReadOnly | Engineering Object model-parent element of this object. |
| `RequiredConfigurationEntries` | `IEnumerable<IBrowsable>` | Writeable | Returns all encoder parameters that can be used, with the exception of p404.0 and/or p404.1. |
| `EncoderTypes` | `IEnumerable<IBrowsable>` | ReadOnly | Depending on the encoder, returns parameter p404.0 and/or p404.1. |

The following table describes the **methods** of the class:

| Name | Parameter | Return value | Description |
| --- | --- | --- | --- |
| `SetEncoderType` | RotaryLinearFlag enum | bool | Defines the non-DRIVE-CLiQ encoder type to be either rotary or linear . |
| `SetEncoderType` | RotaryLinearFlag enum, AbsoluteIncrementalFlag enum | bool | Defines the DRIVE-CLiQ encoder type to be either rotary or linear as well as absolute or incremental.   Not intended for use with non-DRIVE-CLiQ encoders.   G220 drives with firmware version V6.2 only support absolute or incremental encoder types. This API can be used for setting. |

### MotorConfiguration

#### MotorConfiguration

Class `MotorConfiguration` is responsible for commissioning motors and encoders.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives`    `Siemens.Engineering.MC.Drives.DFI`    `Siemens.Engineering.MC.Drives.Enums` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

**Response for Siemens motors:**

Action `SetMotortype` must be called to set the motor type. This action comprises the Enum `MotorType` and a number, which represents the `DriveDatasetNumber`.

The action `SetMotortype` is not available for S120 drives. For these drives, the motor type is set using the hardware catalog by applying the `PlugNew()` method.

The following table describes the enums:

| Enum name | Description |
| --- | --- |
| `NoMotor` | 0: No motor |
| `InductionMotor` | 1: Induction motor |
| `SynchronousMotor` | 2: Synchronous motor |
| `NoCodeNumber1LE1InductionMotor` | 10: 1LE1 induction motor (not a code number) |
| `NoCodeNumber1LG6InductionMotor` | 13: 1LG6 induction motor (not a code number) |
| `NoCodeNumber1xx1SIMOTICSFDInductionMotor` | 14: 1xx1 SIMOTICS FD induction motor (not a code number) |
| `NoCodeNumber1LA7InductionMotorNoCodeNumber` | 17: 1LA7 induction motor (not a code number) |
| `MotorSeriesNumber1LA81PQ8StandardInduction` | 18: 1LA8 / 1PQ8 standard induction motor series |
| `NoCodeNumber1LA9InductionMotor` | 19: 1LA9 induction motor (not a code number) |

**Response for non-Siemens motors:**

Class `MotorConfiguration` is used to save data of non-Siemens motors. It contains 2 objects `ConfigurationEntryComposition`, which, when commissioning, must be populated with the corresponding motor data. Object `RequiredConfigurationEntries` must also be populated. Object `OptionalConfigurationEntries` does not have to be populated.

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `RequiredConfigurationEntries` | `ConfigurationEntryComposition` | Accessible configuration entries of this motor configuration. |
| `OptionalConfigurationEntries` | `ConfigurationEntryComposition` | Accessible configuration entries of this motor configuration. |
| `Parent` | `IEngineeringObject` | Engineering object model-parent elements of this object (only S120 drives). |

### OnlineDriveObject

#### OnlineDriveObject

The `OnlineDriveObject` class allows online access to the drive object. Drive parameters can be accessed via the drive object.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

public sealed class OnlineDriveObject

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `Parameters` | [DriveParameterComposition](#driveparametercomposition) | Returns a list with the available parameters of the online drive object.   `null`, if the mode is "Offline".  In offline mode, an exception is triggered when a method is called or for a write access to a parameter. |

---

**See also**

[Determining a drive object](#determining-a-drive-object)
  
[Reading and writing parameters](#reading-and-writing-parameters)
  
[Reading and writing parameters online](#reading-and-writing-parameters-online)

### OnlineDriveObjectContainer

#### OnlineDriveObjectContainer

The `OnlineDriveObjectContainer` is a service of the drive object (`DeviceItem`) for the current device (`Device`).

The following table describes the **navigators** of the `OnlineDriveObjectContainer`:

| Name | Data type | Description |
| --- | --- | --- |
| `OnlineDriveObjects` | `OnlineDriveObjectComposition` | Returns a list with the available online drive objects ([OnlineDriveObject](#onlinedriveobject)). The drive objects allow access to the drive parameters. |
| `DriveDataEncryption` | `Siemens.Engineering.MC.Drives.SecurityObjects.DriveDataEncryption` | Configures the encryption of drive data (DDE, drive data Encryption) for SINAMICS drives from firmware version V6.1. |

### StartDriveDownloadCheckConfiguration

#### StartDriveDownloadCheckConfiguration

Class `StartDriveDownloadCheckConfiguration` is derived from the class `DownloadCheckConfiguration` and has the same properties. Class `DownloadCheckConfiguration` is described in the standard Openness help.

The class provides the configuration settings via checkboxes from the user.

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `Checked` | `bool` | Returns the current setting of the configuration or activates/deactivates the configuration. |

---

**See also**

[Download](#download)

### SafetyTelegram

#### SafetyTelegram

Class `SafetyTelegram` stands for the telegram of the drive object. Exception `EngineeringTargetInvocationException` is displayed for errors in the write attributes.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `TelegramNumber` | `Int32` | Number of the main telegram. Free telegrams are designated with a value of 999. |
| `Type` | [TelegramType](#telegramtype) | Telegram type that is returned as enum "TelegramType". |
| `Addresses` | [AddressComposition](#addresscomposition) | Composition of all addresses of a telegram. |
| `PKW` | [Telegram](#telegram) | Composition of all PKW channels of the telegram.   null - if the telegram does not have a PKW part. |

### TechnologyExtension

#### TechnologyExtension

The following table describes the **properties** of the class:

| Name | Data type | Access | Description |
| --- | --- | --- | --- |
| `Identifier` | `string` | ReadOnly | Returns the identifier for the Technology Extension. |
| `Name` | `string` | ReadOnly | Returns the name of the Technology Extension |
| `DisplayName` | `string` | ReadOnly | Returns the display name of the Technology Extension. |
| `IsActivated` | `boolean` | ReadOnly | Returns the activation status of the Technology Extension. |

The following table describes the **navigators** of the class:

| Name | Type | Access | Description |
| --- | --- | --- | --- |
| `Parent` | IEngineeringObject | ReadOnly | Engineering Object model-parent element of this object. |

The following table describes the **methods** of the class:

| Name | Return value | Parameter | Description |
| --- | --- | --- | --- |
| `Activate` | `bool` | - | Activates the Technology Extension. |
| `Deactivate` | `bool` | - | Deactivates the Technology Extension. |

---

**See also**

[Using Technology Extensions](#using-technology-extensions)

### TechnologyExtensionComposition

#### TechnologyExtensionComposition

The `TechnologyExtensionComposition` class includes all Technology Extensions assigned to a particular DriveObject. All Technology Extensions are handled in the same way.

The following table describes the **properties** of the class:

| Name | Data type | Access | Description |
| --- | --- | --- | --- |
| `Count` | `int` | ReadOnly | Returns the number of elements included in `TechnologyExtensionComposition`. |

The following table describes the **navigators** of the class:

| Name | Type | Access | Description |
| --- | --- | --- | --- |
| `Parent` | IEngineeringObject | ReadOnly | Engineering Object model-parent element of this object. |

The following table describes the **methods** of the class:

| Name | Return value | Parameter | Description |
| --- | --- | --- | --- |
| `Find` | TechnologyExtension item | string name/identifier | Finds a Technology Extension using the name/identifier. |
| `Contains` | `bool` | TechnologyExtension item | Determines whether an element is included in `TechnologyExtensionComposition`. |
| `GetEnumerator` | IEnumerator<TechnologyExtension> | - | Returns an enumerator which runs through a list of available Technology Extensions. |

---

**See also**

[Using Technology Extensions](#using-technology-extensions)

### TechnologyExtensionInstallationProvider

#### TechnologyExtensionInstallationProvider

The `TechnologyExtensionInstallationProvider` class is a function of the TIA Portal and enables a `TechnologyExtensionPackage` to be installed.

The following table describes the **navigators** of the class:

| Name | Type | Access | Description |
| --- | --- | --- | --- |
| `TechnologyExtensionPackages` | TechnologyExtensionPackageComposition | ReadOnly | Compilation of `TechnologyExtensionPackages`. |

The following table describes the **methods** of the class:

| Name | Type of return value | Parameter | Description | Exceptions |
| --- | --- | --- | --- | --- |
| `Install` | `bool` | ReadOnly | This method installs a `TechnologyExtensionPackage`.     **Parameter description**   filePath: Fully qualified path name of the .tec file to be installed. | EngineeringException |
| `Uninstall` | `bool` | ReadOnly | This method uninstalls a `TechnologyExtensionPackage`.    Parameter description  packageIdentifier: Identifier to determine the `TechnologyExtensionPackage` to be uninstalled. confirmUninstallInUse: This option is used to confirm uninstallation of a Technology Extension used in the open project. | EngineeringException |

---

**See also**

[Using Technology Extensions](#using-technology-extensions)

### TechnologyExtensionPackage

#### TechnologyExtensionPackage

The `TechnologyExtensionPackage` class allows access to Technology Extensions.

The following table describes the **properties** of the class:

| Name | Data type | Access | Description |
| --- | --- | --- | --- |
| `Identifier` | `string` | ReadOnly | Returns the identifier of the `TechnologyExtensionPackage`. The syntax for definition is: <name>/<version> |
| `Name` | `string` | ReadOnly | Returns the name of the `TechnologyExtensionPackage`. |
| `DisplayName` | `string` | ReadOnly | Returns the `DisplayName` of the `TechnologyExtensionPackage`. |

The following table describes the **navigators** of the class:

| Name | Type | Access | Description |
| --- | --- | --- | --- |
| `Parent` | IEngineeringObject | ReadOnly | Engineering Object model-parent element of this object. |

---

**See also**

[Using Technology Extensions](#using-technology-extensions)

### Telegram

#### Telegram

Class `Telegram` allows access to the structure of a telegram from a drive object.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

`public sealed class Telegram`

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `TelegramNumber` | `Int32` | Returns the number of the main telegram or specifies the number.  A freely configurable telegram has the number 999. |
| `Type` | [TelegramType](#telegramtype) | Returns the type of telegram as `Enum``TelegramType`. |
| `Addresses` | [AddressComposition](#addresscomposition) | Returns an `AdressComposition` with information on the address. |
| `PKW` | `Telegram` | Returns channel `PKW` as `Telegram`.   `null` if the property is not available  A telegram with `PKW` is telegram 353, for example. |
| `Hardware Identifier` | `IEnumerable<IBrowsable>` | Returns the list of hardware identifiers. |

The following table describes the **methods** of the class:

| Name | Description |
| --- | --- |
| `CanChangeTelegram(Int32)` | Returns `true` if the telegram can be changed to the parameterized standard type. |
| `GetSize(` [AddressIoType](#addressiotype) `)` | Returns the size of the inputs or outputs of the telegram. |
| `CanChangeSize(` [AddressIoType](#addressiotype) `, Int32, bool)` | Returns `true` if the size of the telegram can be changed as parameterized. Standard telegrams can only be enlarged.  The retention of the previous telegram address is taken into account when the option is parameterized with `true`. |
| `ChangeSize(` [AddressIoType](#addressiotype) `, Int32, bool)` | Returns `true` if the size of the telegram could be changed as parameterized.   The retention of the previous telegram address is taken into account when the option is parameterized with `true`. |

### TelegramComposition

#### TelegramComposition

The `TelegramComposition` class allows access to the telegrams of a drive object. The structure of a telegram can be read out via class [Telegram](#telegram).

Note that referenced objects may become invalid through class `TelegramComposition`. For example, object [Telegram](#telegram) becomes invalid after the telegram size is changed.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

public sealed class TelegramComposition

The following table describes the **methods** of the class:

| Name | Description |
| --- | --- |
| `CanInsertAdditionalTelegram(Int32, Int32)` | Returns `true` if an extension can be created in accordance with the parameterized sizes (input and output sizes). |
| `CanInsertTorqueTelegram (Int32, telegramNumber)` | When adding a new torque telegram with an already existing telegram number, checks whether this is possible. |
| `CanInsertSupplementaryTelegram(Int32)` | Returns `true` if a supplementary telegram can be created in accordance with the parameterized telegram number. |
| `EraseTelegram(TelegramType)` | Deletes a telegram with a known telegram type from the drive object.   Returns `true` if the parameterized telegram could be deleted.  If a torque telegram is used as type, then object "torqueTelegram" is deleted.  If a Safety Integrated telegram is used as type, then object "safetyTelegram" is deleted.   Standard telegrams cannot be deleted.  In the event of an error, an `EngineeringTargetInvocationException` is initiated. |
| `Find(TelegramType)` | Returns the [Telegram](#telegram) object if it could be found via the parameterized telegram type or Safety Integrated telegram type.   `null` if the telegram is not found.  If a torque telegram is used as type, then object `torqueTelegram` is returned, assuming that it exists.   If a Safety Integrated telegram is used as type, then object `safetyTelegram` is returned, assuming that it exists.    **Example**    `Telegram telegram = telegrams.Find(TelegramType.MainTelegram);` |
| `InsertAdditionalTelegram(Int32, Int32)` | Creates an extension for the drive object in accordance with the parameterized sizes and returns `true` if the extension could be inserted.  In the event of an error, an `EngineeringTargetInvocationException` is initiated. |
| `InsertTorqueTelegram  (Int32, telegramNumber)` | Adds a new torque telegram with an already existing telegram number to a drive object. |
| `InsertSafetyTelegram (Int32, telegramNumber)` | Adds a Safety Integrated telegram with its specified telegram number to a drive object. |
| `InsertSupplementaryTelegram(Int32)` | Creates the supplementary telegram with the parameterized telegram number and returns `true` if the telegram could be inserted.  In the event of an error, an `EngineeringTargetInvocationException` is initiated. |

### TelegramType

#### TelegramType

The Enum TelegramType contains predefined telegram types.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **syntax** of the class:

public enum TelegramType

The following table describes the **enum entries**:

| Name | Description |
| --- | --- |
| `MainTelegram` | ID of the main telegram |
| `SupplementaryTelegram` | ID of the supplementary telegram |
| `AdditionalTelegram` | ID of an extension |

### TorqueTelegram

#### TorqueTelegram

Class `TorqueTelegram` stands for the telegram of the drive object. Exception `EngineeringTargetInvocationException` is displayed for errors in the write attributes.

| Symbol | Meaning |
| --- | --- |
| **Namespace:** | `Siemens.Engineering.MC.Drives` |
| **Assembly:** | `Siemens.Engineering.MC.Drives` in `Siemens.Engineering.dll` |

The following table describes the **properties** of the class:

| Name | Data type | Description |
| --- | --- | --- |
| `TelegramNumber` | `Int32` | Telegram number. |
| `Type` | [TelegramType](#telegramtype) | Telegram type that is returned as enum "TelegramType". |
| `Addresses` | [AddressComposition](#addresscomposition) | Composition of all addresses of a telegram. |
| `PKW` | [Telegram](#telegram) | Composition of all PKW channels of the telegram.   null - if the telegram does not have a PKW part. |

### AxisEncoderHardwareConnectionInterface

#### AxisEncoderHardwareConnectionInterface

The class facilitates access to the properties of the technology object.

The following table describes the **methods** of the class:

| Name | Parameter | Return value | Description |
| --- | --- | --- | --- |
| `Connect` | Telegram | bool | Defines the non-DRIVE-CLiQ encoder type to be either rotary or linear. |
| `Connect` | Telegram, ConnectOption | bool | Defines the DRIVE-CLiQ encoder type to be either rotary or linear as well as absolute or incremental.   Not intended for use with non-DRIVE-CLiQ encoders.   G220 drives with firmware version V6.2 only support absolute or incremental encoder types. This API can be used for setting. |

### UmacConfiguration (from SINAMICS FW V6.1)

For SINAMICS drives from firmware version V6.1, class UmacConfiguration allows function User Management and Access Control (UMAC) to be activated and deactivated with Openness.

The following table describes the **methods** of class `UmacConfiguration`:

| Name | Parameter | Return value | Description | Exceptions |
| --- | --- | --- | --- | --- |
| `Activate` | - | bool | Activates `UmacConfiguration` for the drive. | - |
| `Deactivate` | - | bool | Deactivates `UmacConfiguration` for the drive. | - |

> **Note**
>
> **`Security` class**
>
> The `Security` class is a higher-level class. The class is used in the background to access all APIs that are involved in security.

### UpdateCheckSums (from SINAMICS FW V6.1)

For SINAMICS drives from firmware version V6.1, class `UpdateCheckSums` allows Safety Integrated Functions to be configured with Openness.

The following table describes the **methods** of class `UpdateCheckSums`:

| Name | Parameter | Return value | Description | Exceptions |
| --- | --- | --- | --- | --- |
| `UpdateCheckSums` | - | bool | Recalculates and overwrites the checksum value of Safety Integrated reference parameters. | - |

## Code examples

This section contains information on the following topics:

- [General](#general)
- [Determining the activation status](#determining-the-activation-status)
- [Executing drive functions](#executing-drive-functions)
- [Creating a drive](#creating-a-drive)
- [Creating a drive component](#creating-a-drive-component)
- [Determining a drive object](#determining-a-drive-object)
- [Determining the drive object type](#determining-the-drive-object-type)
- [Reading and writing BICO parameters](#reading-and-writing-bico-parameters)
- [Download](#download)
- [Editing DRIVE-CLiQ connections](#editing-drive-cliq-connections)
- [Carrying out the first steps in Startdrive](#carrying-out-the-first-steps-in-startdrive)
- [Defining the encoder type](#defining-the-encoder-type)
- [Configuring devices](#configuring-devices)
- [Determining hardware identifiers](#determining-hardware-identifiers)
- [Creating a component for a drive component (S120 only)](#creating-a-component-for-a-drive-component-s120-only)
- [Defining the motor type and motor configuration](#defining-the-motor-type-and-motor-configuration)
- [Reading and writing parameters](#reading-and-writing-parameters)
- [Reading and writing parameters online](#reading-and-writing-parameters-online)
- [Saving the parameterization](#saving-the-parameterization)
- [How to assign a SecureString password](#how-to-assign-a-securestring-password)
- [Configuring Safety Integrated (checksums) (from SINAMICS FW V6.1)](#configuring-safety-integrated-checksums-from-sinamics-fw-v61)
- [Using Safety Integrated telegrams](#using-safety-integrated-telegrams)
- [Setting the SIMOGEAR article number for G115D drives](#setting-the-simogear-article-number-for-g115d-drives)
- [Using Technology Extensions](#using-technology-extensions)
- [Connecting technology objects with hardware modules via telegram objects](#connecting-technology-objects-with-hardware-modules-via-telegram-objects)
- [Inserting and extending telegrams](#inserting-and-extending-telegrams)
- [Using torque telegrams](#using-torque-telegrams)
- [Activating/deactivating UMAC for drives](#activatingdeactivating-umac-for-drives)
- [Activating the encryption of drive data/DDE (from SINAMICS FW V6.1)](#activating-the-encryption-of-drive-datadde-from-sinamics-fw-v61)
- [Restoring factory settings](#restoring-factory-settings)

### General

The following code examples describe the basic procedure for various applications. The code is not necessarily complete or compilable.

### Determining the activation status

The following examples show how you can determine the activation status for S120 drives, either offline or online:

Determining the activation status of an S120 drive offline

using Siemens.Engineering.MC.Drives;

DriveFunctionInterface dfi = ...

DriveObjectActivation driveObjectActivation = dfi.DriveObjectFunctions.DriveObjectActivation;

//driveObjectActivation can be null in case of the actual driveobject does not support activation.

//change activation state

driveObjectActivation.ChangeActivationState(DriveObjectActivationState.Deactivate);

//get the activation state

DriveObjectActivationState activationState = driveObjectActivation.ActivationState;

//get the Is Active property

bool isActive = driveObjectActivation.IsActive;

Determining the activation status of an S120 drive online

using Siemens.Engineering.MC.Drives;

OnlineDriveFunctionInterface onlinedfi = ...

DriveObjectActivation driveObjectActivation = onlinedfi.DriveObjectActivation;

//driveObjectActivation can be null in case of the actual driveobject does not support activation in online.

//change activation state

driveObjectActivation.ChangeActivationState(DriveObjectActivationState.Deactivate);

//get the activation state

DriveObjectActivationState activationState = driveObjectActivation.ActivationState;

//get the IsActive property

bool isActive = driveObjectActivation.IsActive;

### Executing drive functions

The following examples show how you can simply access drive functions, either offline or online:

Executing drive functions offline

using Siemens.Engineering.MC.Drives;

DriveObject driveObject = ...

DriveFunctionInterface dfi = driveObject.GetService<DriveFunctionInterface>();

// dfi can be null in case of the actual driveobject does not support it.

Executing drive functions online

using Siemens.Engineering.MC.Drives;

OnlineDriveObject onlineDriveObject = ...

OnlineDriveFunctionInterface onlineDfi = onlineDriveObject.GetService<OnlineDriveFunctionInterface>();

// onlineDfi can be null in case of the actual onlineDriveObject

// does not support it or if the device is offline.

### Creating a drive

You can create a drive with method `CreateWithItem()` of collection `Devices`.

The drives are specified using parameters of the method. The format of the parameters is described in the following.

#### Creating a G120 drive

Format of the parameters for a G120:

`CreateWithItem(@"OrderNumber: mlfb / FirmwareVersion /", "NameOfTheDevice", positionNumber)`

The following example shows how you can create a G120 drive.

Creating a G120 drive

TiaPortal portal = new TiaPortal(TiaPortalMode.WithUserInterface);

Project tiaproject= portal.Projects.Open("..."); //The path of the project

Device s120Device = tiaproject.Devices.CreateWithItem(@"OrderNumber:6SL3246-0BA22-1FA0/4.7.6/", "Device_0", null);

#### Creating S120, S150, S200, S210, MV, G130, G150 and G220 drives

Parameter format for S120, S150, S200, S210, MV, G130, G150 and G220 drives:

`CreateWithItem(@"OrderNumber: mlfb / FirmwareVersion / AdditionalTypeIdentifier", "NameOfTheDevice", positionNumber)`

Possible values for `AdditionalTypeIdentifier`:

- Empty string (e.g. for G120)
- S120
- S150
- S200
- S210
- MV
- G130
- G150
- G220

The following example shows how you can create an S120 drive.

Creating an S120 drive

TiaPortal portal = new TiaPortal(TiaPortalMode.WithUserInterface);

Project tiaproject= portal.Projects.Open("..."); //The path of the project

Device s120Device = tiaproject.Devices.CreateWithItem(@"OrderNumber:6SL3040-1MA01-0Axx/V4.8/S120", "Device_0", null);

### Creating a drive component

You can create a drive component for a drive unit with the `PlugNew()` method of the `Device` object.

The following example shows how to create a drive component.

Creating a Motor Module

DeviceItem subModul = sdrDevice.PlugNew(@"OrderNumber:6SL3xxx-xxxxx-xxxx",​ "MotorModul", 65535);

### Determining a drive object

The following examples show how to determine drive objects offline and online.

Determining an offline drive object

using Siemens.Engineering.MC.Drives;

//G devices

Project project =  portal.Projects.Open("..."); //Destination folder to open the project

DeviceItem item = project.Devices[0].Items[0].Items[0];

DriveObject driveObject = item.GetService<DriveObjectContainer>().DriveObjects[0];

//S devices

Project project =  portal.Projects.Open("..."); //Destination folder to open the project

DeviceItem item = project.Devices[0].Items[0];

DriveObject driveObject = item.GetService<DriveObjectContainer>().DriveObjects[0];

Determining an online drive object

using Siemens.Engineering.MC.Drives;

//G devices

Project project =  portal.Projects.Open("..."); //Destination folder to open the project

DeviceItem item = project.Devices[0].Items[0].Items[0];

OnlineDriveObject onlineDriveObject = item.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

//S devices

Project project =  portal.Projects.Open("..."); //Destination folder to open the project

DeviceItem item = project.Devices[0].Items[0];

OnlineDriveObject onlineDriveObject = item.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

### Determining the drive object type

The following examples shows how you can determine the actual drive object type – and the types that can be alternatively set.

Determining drive object types

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

DriveObject driveObject = ...

DriveFunctionInterface dfi = driveObject.GetService<DriveFunctionInterface>();

DriveObjectTypeHandler driveObjectTypeHandler = dfi.DriveObjectFunctions.DriveObjectTypeHandler;

// dfi can be null in case of the actual driveobject does not support it.

// driveObjectTypeHandler can be null, if the actual driveObject does not support it.

// Get the possible drive object types on the drive object.

DriveObjectTypeComposition possibleDriveObjectTypes = driveObjectTypeHandler.PossibleDriveObjectTypes;

// Get the current drive object type on the drive object.

DriveObjectType currentDriveObjectType = driveObjectTypeHandler.CurrentDriveObjectType;

//Call the ChangeDriveObjectType method with the current drive object type.

//The method parameter should be the target drive object type.

driveObjectTypeHandler.ChangeDriveObjectType(possibleDriveObjectTypes[0]);

### Reading and writing BICO parameters

The following example shows how to read and write values of BICO parameters. You require a drive object for access.

Reading BICO parameters

using Siemens.Engineering.MC.Drives;

DriveParameter bicoSink= driveObject.Parameters.Find("p681");

if(bicoSink!=null)

{

if(bicoSink.Value is DriveParameter)

{

DriveParamter bicoSourceValue = bicoSink.Value as DriveParameter;

Console.WriteLine("The value of parameter " + bicoSink.Name + ": " + bicoSource.Name + " " + bicoSource.ParameterText);

}

else if (bicoSink.Value == null)

{

Console.WriteLine("Value contains an invalid connection or the source parameter is not accessible via Openness");

}

else

{

Console.WriteLine("The value of parameter " + bicoSink.Name + ": " + bicoSink.Value.ToString());

}

}

Writing BICO parameters

using Siemens.Engineering.MC.Drives;

DriveParameter bicoSource= driveObject.Parameters.Find("r19");

DriveParameter bicoSink = driveObject.Parameters.Find("p738");

if(bicoSource != null)

{

try

{

bicoSink.Value = bicoSource;

}

catch(UserException ex)

{

Console.WriteLine("Write failure :" + ex.Message);

}

}

### Download

After starting the download, you must adjust and confirm the configuration settings. The configuration settings are provided as child objects of object `DownloadConfiguration` – and there are three different types:

- `StartDriveDownloadCheckConfiguration`
- `DownloadSelectionConfiguration`
- `DownloadPasswordConfiguration`

The following examples show the evaluation of the different types of configuration settings in the PreDownload Delegate.

Evaluation of the configuration settings after starting the download

using Siemens.Engineering.Download;

using Siemens.Engineering.Online;

static void PreDownload(DownloadConfiguration configuration)

{

Console.WriteLine(configuration.Message);

StartDriveDownloadCheckConfiguration sdcc = configuration as StartDriveDownloadCheckConfiguration;

if (sdcc != null)

{

sdcc.Checked = true;

return;

}

DownloadPasswordConfiguration downloadPasswordConfiguration = configuration as DownloadPasswordConfiguration;

if (downloadPasswordConfiguration != null)

{

SecureString s = new SecureString();

string passwordText = "password";

foreach (var str in passwordText)

{

s.AppendChar(str);

}

downloadPasswordConfiguration.SetPassword(s);

return;

}

DownloadSelectionConfiguration downloadSelectionConfiguration = configuration as DownloadSelectionConfiguration;

if (downloadSelectionConfiguration != null)

{

downloadSelectionConfiguration.SelectedIndex = 0;

return;

}

}

The following examples show how to download a project to the device.

Download to the S120 device

using Siemens.Engineering.Download;

using Siemens.Engineering.Online;

`try`

`{`

`DeviceItem item = ... //device item of the CU (e.g. : project.Devices[0].Items[0].Items[0])`

`DownloadProvider downloadProvider = item.GetService<DownloadProvider>();`

`DownloadConfigurationDelegate pre = PreDownload;`

`DownloadConfigurationDelegate post = PostDownload;`

`ConnectionConfiguration connConfiguration = downloadProvider.Configuration;`

`ConfigurationMode configurationMode = connConfiguration.Modes.Find("PN/IE");`

`ConfigurationPcInterface pcInterface = configurationMode.PcInterfaces[0];`

`ConfigurationSubnet subnet = pcInterface.Subnets.Find(/*subnet name*/);`

`IConfiguration configuration = subnet.Addresses.Find(/*IP address of the device*/);`

`downloadProvider.Download(configuration, pre, post, DownloadOptions.Software);`

`}`

`catch (Exception e)`

`{`

`Console.WriteLine(e.Message);`

`}`

`//configuration handling before download`

`static void PreDownload(DownloadConfiguration configuration)`

`{`

`Console.WriteLine(configuration.Message);`

`StartDriveDownloadCheckConfiguration dcc = configuration as StartDriveDownloadCheckConfiguration ;`

`if (dcc != null)`

`{`

`dcc.Checked = true;`

`}`

`}`

`//configuration handling after download`

`static void PostDownload(DownloadConfiguration configuration)`

`{`

`Console.WriteLine(configuration.Message);`

`}`

**Additional settings for downloads for drives as of SINAMICS FW V6.1**

If you add a drive with SINAMICS FW V6.1 or higher to a project, then the security settings for this drive are in the factory setting.

It is only possible to download from a drive such as this if UMAC is activated for the project.

Configuring UMAC

`UmacConfigurator UmacConfiguratorService = project.GetService<UmacConfigurator>();var projectUsers = UmacConfiguratorService.ProjectUsers;`

Creating a user for the project

`ProjectUser projectUser = projectUsers.Create("AdminUser", "AdminUser123#".ToSecureString());`

Adding a system role

`projectUser.Roles.Add(systemRole);`

Also requires that a valid TLS certificate is downloaded as described in the following example:

Setting a TLS certificate

`private static OnlineConfigurationDelegate m_OnlineConfigurationDelegate = null;`

`private bool TryDownloadToDeviceTest()`

`{`

`String newAddress = ...// network ip;`

`try`

`{`

`Device device =...//device`

`DeviceItem item = device.Items[0].Items[0];`

`DownloadProvider downloadProvider = item.GetService<DownloadProvider>();`

`ConnectionConfiguration conf = downloadProvider.Configuration;`

`}`

`}`

Activating notification for TLS events

`if (m_OnlineConfigurationDelegate == null)`

`{`

`m_OnlineConfigurationDelegate = OnlineCallBackMethod;`

`conf.OnlineLegitimation += m_OnlineConfigurationDelegate;`

`}`

Setting download configuration settings

`//perform download`

`{`
  
`catch (Exception e)`
  
 `{`
  
 `Console.WriteLine(e.ToString());`
  
 `return false;`
  
 `}`
  
 `return true;`
  
 `}`
  
 `private static void OnlineCallBackMethod(OnlineConfiguration onlineConfiguration)`
  
 `{`
  
 `TlsVerificationConfiguration verificationConfiguration = onlineConfiguration as TlsVerificationConfiguration;`
  
 `if (verificationConfiguration != null)`
  
 `{`
  
 `verificationConfiguration.CurrentSelection = TlsVerificationConfigurationSelection.Trusted;`
  
 `}`
  
`}`

---

**See also**

[Encrypted communication with SecureString passwords](#encrypted-communication-with-securestring-passwords)

### Editing DRIVE-CLiQ connections

The following example shows how to edit DRIVE-CLiQ connections with Openness.

Editing DRIVE-CLiQ connections

TiaPortal portal = new TiaPortal(TiaPortalMode.WithUserInterface);

Project tiaproject = portal.Projects.Open(new FileInfo(@"C:\Users\testUser\Documents\Automation\Project109\Project109.ap15")); //The path of the project

Device device = tiaproject.Devices.CreateWithItem(@"OrderNumber:6SL3040-1MA01-0Axx/V4.8/S120", "Device_0", null); //Create the device

DeviceItem subModul = device.PlugNew(@"OrderNumber:6SL3x2x-1xxxx-xxxx", "", 65535); //Plug a submodul (in this case : Motor modul)

DeviceItem cu = device.DeviceItems[1];          // The CU is always the 1 indexed in the DeviceItems of the Device

DeviceItem subModulDQInterface = subModul.DeviceItems[0];      //We need the DQ interface from the submodul

DeviceItem cuDQInterface = cu.DeviceItems[3];                 //This is the DQ interface of the CU

NetworkPort subModulDQ = ((IEngineeringServiceProvider)subModulDQInterface.DeviceItems[0]).GetService<NetworkPort>(); //We need the DriveCliq port of the DQ interface from the submodul

NetworkPort cuDQ = ((IEngineeringServiceProvider)cuDQInterface.DeviceItems[0]).GetService<NetworkPort>();                  //We need the DriveCliq port of the DQ interface from the CU

cuDQ.DisconnectFromPort(subModulDQ); //Delete the connection between the two ports (automatically created when plugging a modul)

cuDQ.ConnectToPort(subModulDQ); //Create a new connection

### Carrying out the first steps in Startdrive

The following example shows how you can localize or generate an active TIA Portal process.

Finding or generating a TIA Portal process

using Siemens.Engineering;

// Get the list of the running TIA Portal processes.

IList<TiaPortalProcess> procs = TiaPortal.GetProcesses();

TiaPortal portal;

// When there is at least one running TIA Portal, we will attach to the first from the list.

if (procs.Count != 0)

{

portal = procs[0].Attach();

}

// When there is no running TIA Portal, we create one.

else

{

portal = new TiaPortal(TiaPortalMode.WithUserInterface);

}

The following example shows how you can localize or generate a Startdrive project.

Finding or generating a Startdrive project

using Siemens.Engineering;

Project project;

// When the portal has one project, we save it in a variable.

if (portal.Projects.Count == 1)

{

project = portal.Projects[0];

}

// When there is no existing project, we create one with a specific path, and the actual time

else

{

project = portal.Projects.Create(

new DirectoryInfo(@"C:\Projects\Project_" + DateTime.Now.Ticks),

DateTime.Now.Ticks.ToString());

}

The following example shows how you can determine as to whether a specific Startdrive variant (package and version) is installed.

Determining whether the required Startdrive version is installed

using Siemens.Engineering;

if (tiaProcess.InstalledSoftware.Any(sw => sw.Name.Equals("SINAMICS Startdrive Advanced") && sw.Version.Equals("V15"))) { Console.WriteLine("Startdrive is available");}

// "V15" is the current startdrive version started at December 2017.

// "V15.1" will be the current startdrive version beginning with December 2018.

// "SINAMICS Startdrive Basic" and "SINAMICS Startdrive Advanced" are the 2 possible startdrive function packages.

### Defining the encoder type

The following example shows how you can set the encoder type or the encoder data set number offline.

Setting the encoder type and/or the encoder data set number offline via the hardware configuration

**using** Siemens.Engineering.MC.Drives

**using** Siemens.Engineering.MC.Drives.DFI

**using** Siemens.Engineering.MC.Drives.Enums;

DeviceItem cuDeviceItem = m_Device.DeviceItems[1];

DriveObject cuDriveObject = cuDeviceItem.GetService<DriveObjectContainer>().DriveObjects[0];

DriveFunctionInterface cuDriveFunctionInterface = cuDriveObject.GetService<DriveFunctionInterface>();

HardwareProjection hardwareProjection = cuDriveFunctionInterface.HardwareProjection;

// To enable the setting of an EncoderType, the value of p96 should

// be set to 0 (Application class == [0] Expert) if it is present on

// the current G drive.

DriveParameter p96 = cuDriveObject.Parameters.Find("p96");

if (p96 != null)

{

p96.Value = 0;

}

// Setting Encoder 1 on the drive.

// In case of encoders, we have to set several enums to define an

// encoder type. These enums are: EncoderInterface, EncoderType,

// AbsoluteIncrementalFlag, and RotaryLinearFlag.

// There can be a problem, if the given enum combination is not valid.

// In that case, it has to give back a feedback.

hardwareProjection.SetEncoder(

EncoderInterface.Terminal,

EncoderType.HTLTTL,

AbsoluteIncrementalFlag.Incremental,

RotaryLinearFlag.Rotary,

1);

// It is possible to set 2 encoders to a motor, one with encoderNumber == 1

// and the other with encoderNumber == 2

The following example shows how you can set the encoder type or the encoder data set number using an online connection.

Setting the encoder type and/or the encoder data set number online via the hardware configuration

**using** Siemens.Engineering.MC.Drives

**using** Siemens.Engineering.MC.Drives.DFI

**using** Siemens.Engineering.MC.Drives.Enums;

DeviceItem cuDeviceItem = m_Device.DeviceItems[1];

OnlineDriveObject cuOnlineDriveObject = cuDeviceItem.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

OnlineDriveFunctionInterface cuDriveFunctionInterface = cuOnlineDriveObject.GetService<OnlineDriveFunctionInterface>();

HardwareProjection hardwareProjection = cuDriveFunctionInterface.HardwareProjection;

// To enable the setting of an Encoder, the value of p96 should

// be set to 0 (Application class == [0] Expert) if it is present

// the current G drive.

DriveParameter p96 = cuOnlineDriveObject.Parameters.Find("p96");

if (p96 != null)

{

p96.Value = 0;

}

// Setting Encoder 1 on the drive.

// In case of encoders we have to set several enums to define an

// encoder type. These enums are: EncoderInterface, EncoderType,

// AbsoluteIncrementalFlag, and RotaryLinearFlag.

// There can be a problem, if the given enum combination is not valid.

// In that case, it has to give back a feedback.

hardwareProjection.SetEncoder(

EncoderInterface.Terminal,

EncoderType.HTLTTL,

AbsoluteIncrementalFlag.Incremental,

RotaryLinearFlag.Rotary,

1);

// It is possible to set 2 encoders to a motor, one with encoderNumber == 1

// and the other with encoderNumber == 2

The following example shows how you can read out the actual encoder configuration from the drive.

Reading out the encoder configuration

DeviceItem cuDeviceItem = m_Device.DeviceItems[1];

DriveObject cuDriveObject = cuDeviceItem.GetService<DriveObjectContainer>().DriveObjects[0];

DriveFunctionInterface cuDriveFunctionInterface = cuDriveObject.GetService<DriveFunctionInterface>();

HardwareProjection encoderProjection = cuDriveFunctionInterface.HardwareProjection;

// Before setting an encoder, p96 should be 0

// (See section "Projecting EncoderConfiguration")

encoderProjection.SetEncoder(

EncoderInterface.Terminal,

EncoderType.HTLTTL,

AbsoluteIncrementalFlag.Incremental,

RotaryLinearFlag.Rotary,

1);

EncoderConfiguration encoderConfiguration = encoderProjection.GetCurrentEncoderConfiguration(1);

The following example shows how you can configure the actual encoder configuration offline.

Configuring an encoder offline

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

// Project encoder configuration in Offline state

DeviceItem cuDeviceItem = m_Device.DeviceItems[1];

DriveObject cuDriveObject = cuDeviceItem.GetService<DriveObjectContainer>().DriveObjects[0];

DriveFunctionInterface cuDriveFunctionInterface = cuDriveObject.GetService<DriveFunctionInterface>();

HardwareProjection hardwareProjection = cuDriveFunctionInterface.HardwareProjection;

// Before setting an encoder type, p96 should be 0

// (See section "Projecting EncoderConfiguration")

// To Project an EncoderConfiguration, first set e.g. Encoder 1 with .SetEncoder(...).

hardwareProjection.SetEncoder(

EncoderInterface.Terminal,

EncoderType.HTLTTL,

AbsoluteIncrementalFlag.Incremental,

RotaryLinearFlag.Rotary,

1);

// Get the current configuration of Encoder 1.

EncoderConfiguration config = hardwareProjection.GetCurrentEncoderConfiguration(1);

// Fill out Encoder 1's configuration values.

config.RequiredConfigurationEntries.ToList().ForEach(ce =>

{

switch (ce.Name)

{

case "p405.0":

ce.Value = 0;

break;

case "p405.1":

ce.Value = 1;

break;

case "p408":

ce.Value = 1024;

break;

case "p425":

ce.Value = 2048;

break;

default:

break;

}

});

// Project the Encoder 1 configuration to the device.

bool result = cuDriveFunctionInterface.HardwareProjection.ProjectEncoderConfiguration(config, 1);

The following example shows how you can configure the actual encoder configuration online.

Configuring an encoder online

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

// Project encoder configuration in Online state

DeviceItem cuDeviceItem = m_Device.DeviceItems[1];

DeviceItem cuDeviceItemForOnline = m_Device.DeviceItems[0];

//You need the rack for going online on G120 Device, which is .DeviceItems[0]

// GoOnline...

// To use these function in Online, you have to use the OnlineDriveFunctionInterface

OnlineDriveObject onlineDriveObject = cuDeviceItem.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

OnlineDriveFunctionInterface onlineDfi = onlineDriveObject.GetService<OnlineDriveFunctionInterface>();

HardwareProjection hardwareProjection = onlineDfi.HardwareProjection;

// Before setting an encoder, p96 should be 0

// (See section "Projecting EncoderConfiguration")

// To Project an EncoderConfiguration, first set e.g. Encoder 1 with .SetEncoder(...).

hardwareProjection.SetEncoder(

EncoderInterface.Terminal,

EncoderType.HTLTTL,

AbsoluteIncrementalFlag.Incremental,

RotaryLinearFlag.Rotary,

1);

// Get the current configuration of Encoder 1.

EncoderConfiguration config = hardwareProjection.GetCurrentEncoderConfiguration(1);

// Fill out Encoder 1's configuration values.

config.RequiredConfigurationEntries.ToList().ForEach(ce =>

{

switch (ce.Name)

{

case "p405.0":

ce.Value = 0;

break;

case "p405.1":

ce.Value = 1;

break;

case "p408":

ce.Value = 1024;

break;

case "p425":

ce.Value = 2048;

break;

default:

break;

}

});

// Project the Encoder 1 configuration to the device.

bool result = onlineDfi.HardwareProjection.ProjectEncoderConfiguration(config, 1);

The following example shows how you can write the configuration entry to the console.

Write out configuration entry

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

MotorConfiguration motorConfig = hardwareProjection.GetCurrentMotorConfiguration(0);

foreach (var configurationEntry in motorConfig.RequiredConfigurationEntries)

{

Console.WriteLine(configurationEntry.Name);

}

EncoderConfiguration encConfig = hardwareProjection.GetCurrentEncoderConfiguration(1);

foreach (var configurationEntry in encConfig.RequiredConfigurationEntries)

{

Console.WriteLine(configurationEntry.Name);

}

The following example shows how you can configure DRIVE-CLiQ encoders.

Configuring DRIVE-CLiQ encoders

using Siemens.Engineering.MC.Drives.Enums;

private bool TestEncoderProjectionForAcxDrives(){  
 bool result = false;  
 //Revelant drive already added to project m_Project.Devices[0]  
 DeviceItem motorModule = m_Project.Devices[0].DeviceItems[2]; //get the motor module or power module  
 DriveObject mmDriveObject = motorModule.GetService<DriveObjectContainer>().DriveObjects[0];  
 DriveFunctionInterface mmDriveFunctionInterface = mmDriveObject.GetService<DriveFunctionInterface>();  
 HardwareProjection hwProjection = mmDriveFunctionInterface.HardwareProjection;  
  
 try  
 {  
 EncoderConfiguration encoderConfiguration = hwProjection.GetCurrentEncoderConfiguration(0);   
 //get EncoderConfiguration for encoder at index 0  
  
 IList<ConfigurationEntry> encoderTypes = encoderConfiguration.EncoderTypes.ToList();  
 //get the type of encoder, this would return only the applicable parameters p404.0 & p404.1  
  
 bool setEncoderTypeResult = encoderConfiguration.SetEncoderType(RotaryLinearFlag.Linear, AbsoluteIncrementalFlag.Incremental);  
 //SetEncoderType is optional and can be used to change Encoder Type.  
 //SetEncoderType can be used to set Rotary or Linear as Encoder Type.  
 //For DriveCliq encoder, along with Rotary/Linear, you can also set the Encoder type as Incremental or Absolute.  
  
 if (setEncoderTypeResult)  
 {  
 encoderConfiguration.RequiredConfigurationEntries.ToList().ForEach(e =>  
 {  
 if (e.Name.Equals("p404.0"))  
 {  
 e.Value = true;  
 }  
 }); //set parameter p404.0 (Linear encoder) to true  
 result = hwProjection.ProjectEncoderConfiguration(encoderConfiguration, 0);  
 }  
 }  
 catch (Exception e)  
 {  
 Console.WriteLine(e.Message+ "\n" + e.StackTrace);  
 }  
 return result;  
}

The following example shows how you can configure non-Siemens encoders without DRIVE-CLiQ.

Configuring non-Siemens encoders without DRIVE-CLiQ

using Siemens.Engineering.MC.Drives.Enums;

private bool TestEncoderProjectionForAcxDrives()  
{  
 bool result = false;  
 //Revelant drive already added to project m_Project.Devices[0]  
 DeviceItem motorModule = m_Project.Devices[0].DeviceItems[2]; //get the motor module or power module  
 DriveObject mmDriveObject = motorModule.GetService<DriveObjectContainer>().DriveObjects[0];  
 DriveFunctionInterface mmDriveFunctionInterface = mmDriveObject.GetService<DriveFunctionInterface>();  
 HardwareProjection hwProjection = mmDriveFunctionInterface.HardwareProjection;  
  
 try  
 {  
 EncoderConfiguration encoderConfiguration = hwProjection.GetCurrentEncoderConfiguration(0);   
 //get EncoderConfiguration for encoder at index 0  
  
 IList<ConfigurationEntry> encoderTypes = encoderConfiguration.EncoderTypes.ToList();  
 //get the type of encoder, this would return only the applicable parameter p404.0   
  
 bool setEncoderTypeResult = encoderConfiguration.SetEncoderType(RotaryLinearFlag.Linear);  
 //SetEncoderType is optional and can be used to change Encoder Type.  
 //SetEncoderType can be used to set Rotary or Linear as Encoder Type.  
  
 if (setEncoderTypeResult)  
 {  
 encoderConfiguration.RequiredConfigurationEntries.ToList().ForEach(e =>  
 {  
 if (e.Name.Equals("p404.0"))  
 {  
 e.Value = true;  
 }  
 }); //set parameter p404.0 (Linear encoder) to true  
 result = hwProjection.ProjectEncoderConfiguration(encoderConfiguration, 0);  
 }  
 }  
 catch (Exception e)  
 {  
 Console.WriteLine(e.Message+ "\n" + e.StackTrace);  
 }  
 return result;  
}

### Configuring devices

The following example shows how you can configure S120 and G120 drives offline.

Configuring S120 and G120 drives offline

**using** Siemens.Engineering.MC.Drives

**using** Siemens.Engineering.MC.Drives.DFI

**using** Siemens.Engineering.MC.Drives.Enums;

DriveObject driveObject = ...

DriveFunctionInterface dfi = driveObject.GetService<DriveFunctionInterface>();

HardwareProjection hardwareProjection = dfi.HardwareProjection;

// dfi can be null in case of the actual driveobject does not support it.

// hardwareProjection can be null, if the actual driveObject does not support it.

// For example: On G120 drives, you have to use the CU as driveobject. On S120

// drives, you have to use the MotorModul as driveObject.

The following example shows how you can configure S120 and G120 drives online.

Configuring S120 and G120 drives online

**using** Siemens.Engineering.MC.Drives

**using** Siemens.Engineering.MC.Drives.DFI

**using** Siemens.Engineering.MC.Drives.Enums;

OnlineDriveObject onlineDriveObject = ...

OnlineDriveFunctionInterface onlineDfi = onlineDriveObject.GetService<OnlineDriveFunctionInterface>();

HardwareProjection hardwareProjection = onlineDfi.HardwareProjection;

// onlineDfi can be null in case of the actual onlineDriveObject

// does not support it or if the device is offline.

// hardwareProjection can be null, if the actual onlineDriveObject

// does not support it.

// For example: On G120 drives, you have to use the CU as onlineDriveObject. On

// S120 drives, you have to use the MotorModul as onlineDriveObject.

### Determining hardware identifiers

The following examples show how you can determine the [hardware identifier](#telegram) of various objects.

Determining the hardware identifiers of telegrams

using Siemens.Engineering.MC.Drives;

Device s120Drive = m_Project.Devices[1];  
DeviceItem driveUnit = s120Drive.DeviceItems[0];  
DriveObjectContainer driveObjectContainer = driveUnit.GetService<DriveObjectContainer>();  
DriveObject driveObject = driveObjectContainer.DriveObjects[0];  
Telegram mainTelegram = driveObject.Telegrams[0];  
  
IList<HwIdentifier> hwIdentifiers = mainTelegram.HwIdentifiers?.ToList(); //get the Hardware Identifier  
long identifier = hwIdentifiers[0].Identifier;

Determining the hardware identifier of a Module Access Point

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.HW.HwIdentifier;

Device s120Drive = m_Project.Devices[1];  
DeviceItem driveUnit = s120Drive.DeviceItems[0];  
DriveObjectContainer driveObjectContainer = driveUnit.GetService<DriveObjectContainer>();  
DriveObject driveObject = driveObjectContainer.DriveObjects[0];  
Telegram mainTelegram = driveObject.Telegrams[0];  
  
IList<HwIdentifier> hwIdentifiers = mainTelegram.HwIdentifiers?.ToList(); //get the Hardware Identifier  
long identifier = hwIdentifiers[0].Identifier;  
  
Device deviceS120 = m_Project.Devices[1]; //S120 with Double Motor Module  
Device deviceG120 = m_Project.Devices[2]; //G120  
Device deviceG220 = m_Project.Devices[3]; //G220  
  
ModuleAccessPoint moduleAccessPointS120 = deviceS120.DeviceItems[1].GetService<ModuleAccessPoint>();  
IList<HwIdentifier> hwIdentifiersS120 = moduleAccessPointS120.HwIdentifiers.ToList();  
long identifierS120 = hwIdentifiersS120[0].Identifier;  
  
ModuleAccessPoint moduleAccessPointDriveAxis = deviceS120.DeviceItems[2].GetService<ModuleAccessPoint>();  
IList<HwIdentifier> hwIdentifiersDriveAxis = moduleAccessPointDriveAxis.HwIdentifiers.ToList();  
long identifierDriveAxis = hwIdentifiersDriveAxis[0].Identifier;  
  
ModuleAccessPoint moduleAccessPointDriveAxisTwo = deviceS120.DeviceItems[3].GetService<ModuleAccessPoint>();  
IList<HwIdentifier> hwIdentifiersDriveAxisTwo = moduleAccessPointDriveAxisTwo.HwIdentifiers.ToList();  
long identifierDriveAxisTwo = hwIdentifiersDriveAxisTwo[0].Identifier;  
  
ModuleAccessPoint moduleAccessPointG120 = deviceG120.DeviceItems[1].GetService<ModuleAccessPoint>();  
IList<HwIdentifier> hwIdentifiersG120 = moduleAccessPointG120.HwIdentifiers.ToList();  
long identifierG120 = hwIdentifiersG120[0].Identifier;  
  
ModuleAccessPoint moduleAccessPointG220 = deviceG220.DeviceItems[1].GetService<ModuleAccessPoint>();  
IList<HwIdentifier> hwIdentifiersG220 = moduleAccessPointG220.HwIdentifiers.ToList();  
long identifierG220 = hwIdentifiersG220[0].Identifier;

### Creating a component for a drive component (S120 only)

You have the option of creating a component below a drive component for the S120.

Also enter a type designation to distinguish between the various encoders. The possible type designations and restrictions for encoders are described in the table below.

The following example shows how to create a component below a drive component.

Creating a motor and an encoder below a Motor Module

DeviceItem subModul = sdrDevice.PlugNew(@"OrderNumber:6SL3xxx-xxxxx-xxxx", "MotorModul", 65535);

//Plug a motor to the motor modul

subModul.Container.PlugNew(@"OrderNumber:1PH2092-4WG4x-xxxx", "Motor_1",65535);

//Plug an encoder to the motor modul

subModul.Container.PlugNew(@"OrderNumber:XExxxxx-xxxxx-xxxx//DRIVE-CLIQ.202", "Encoder_1",65535);

#### Type designations for encoders and restrictions

The following restrictions apply when inserting encoders via Openness:

- Only an unspecific Sensor Module can be created for some encoders when inserting via Openness. In this case, you must configure the specific type of the Sensor Module in the TIA Portal.
- Maximum two encoders can be inserted for one Motor Module.

The following table lists the available type designations for encoders.

| DRIVE-CLiQ | Resolver | sin/cos | SSI | sin/cos+SSI | HTL/TTL | HTL/TTL+SSI | EnDat 2.1 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| DRIVE-CLIQ.202 | Resolver.0 | SIN_COS.0 | SSI.0 | SIN_COS_+_SSI.0 | HTL_TTL.0 | HTL_TTL+SSI.0 | EnDat_2.1.2051 |
| DRIVE-CLIQ.204 | Resolver.1001 | SIN_COS.2001 | SSI.3081 | SIN_COS_+_SSI.2081 | HTL_TTL.3001 | HTL_TTL+SSI.3088 | EnDat_2.1.2052 |
| DRIVE-CLIQ.212 | Resolver.1002 | SIN_COS.2002 | SSI.3082 | SIN_COS_+_SSI.2082 | HTL_TTL.3002 | HTL_TTL+SSI.3090 | EnDat_2.1.2053 |
| DRIVE-CLIQ.214 | Resolver.1003 | SIN_COS.2003 | SSI.9999 | SIN_COS_+_SSI.2083 | HTL_TTL.3003 | HTL_TTL+SSI.9999 | EnDat_2.1.2054 |
| DRIVE-CLIQ.242 | Resolver.1004 | SIN_COS.2004 | ‑ | SIN_COS_+_SSI.2084 | HTL_TTL.3005 | ‑ | EnDat_2.1.2055 |
| DRIVE-CLIQ.244 | Resolver.9999 | SIN_COS.2005 | ‑ | SIN_COS_+_SSI.9999 | HTL_TTL.3006 | ‑ | EnDat_2.1.2151 |
| DRIVE-CLIQ.9999 | ‑ | SIN_COS.2006 | ‑ | ‑ | HTL_TTL.3007 | ‑ | EnDat_2.1.9999 |
| DRIVE-CLIQ.10100 | ‑ | SIN_COS.2007 | ‑ | ‑ | HTL_TTL.3008 | ‑ | EnDat_2.1.10100 |
| ‑ | ‑ | SIN_COS.2008 | ‑ | ‑ | HTL_TTL.3009 | ‑ | ‑ |
| ‑ | ‑ | SIN_COS.2010 | ‑ | ‑ | HTL_TTL.3011 | ‑ | ‑ |
| ‑ | ‑ | SIN_COS.2012 | ‑ | ‑ | HTL_TTL.3020 | ‑ | ‑ |
| ‑ | ‑ | SIN_COS.2013 | ‑ | ‑ | HTL_TTL.3109 | ‑ | ‑ |
| ‑ | ‑ | SIN_COS.2110 | ‑ | ‑ | HTL_TTL.9999 | ‑ | ‑ |
| ‑ | ‑ | SIN_COS.2111 | ‑ | ‑ | ‑ | ‑ | ‑ |
| ‑ | ‑ | SIN_COS.2112 | ‑ | ‑ | ‑ | ‑ | ‑ |
| ‑ | ‑ | SIN_COS.9999 | ‑ | ‑ | ‑ | ‑ | ‑ |

### Defining the motor type and motor configuration

The following examples show how you can set a motor type for G120 drives via the device configuration:

Setting the motor type offline via the hardware configuration

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

//Offline (Only on G120 drives)

DriveFunctionInterface dfi = ...

HardwareProjection hardwareProjection = dfi.HardwareProjection;

// hardwareProjection can be null in case of the actual driveObject

// does not support activation.

// Setting the required MotorType and DriveDataSetNumber on the drive.

// It is only supported on G120 drives.

//First parameter is the MotorType, Second parameter is the DriveDataSetNumber

hardwareProjection.SetMotorType(MotorType.InductionMotor, 0);

// There can be a problem, if the selected MotorType is not available

// on the drive. In that case, it has to give back a feedback.

Setting the motor type online via the hardware configuration

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

//Online (Only on G120 drives)

OnlineDriveFunctionInterface onlineDfi = ...

HardwareProjection hardwareProjection = onlineDfi.HardwareProjection;

// hardwareProjection can be null in case of the actual

// onlineDriveObject does not support activation.

// Setting the required MotorType and DriveDataSetNumber on

// the drive. It is only supported on G120 drives.

// First parameter is the MotorType, Second parameter is the DriveDataSetNumber

hardwareProjection.SetMotorType(MotorType.InductionMotor, 0);

// There can be a problem, if the selected MotorType is not available on

// the drive. In that case, it has to give back a feedback.

The following examples show how you can read out the motor type for G120 drives from the drive:

Determining the motor configuration offline

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

// Offline

// WARNING: You have to set the MotorType on G drives before

// you would like to get the current configuration, otherwise

// you will get an exception/feedback, which informs you that

// there is no motor set.

// On S120 drives, you don't have to do that, but you have to

// plug a motor to motor modul.( later on)

HardwareProjection hardwareProjection = dfi.HardwareProjection;

// Get the current motor configuration

// It needs a datasetnumber, which is currently only supported on G120 drives.

MotorConfiguration motorConfiguration = hardwareProjection.GetCurrentMotorConfiguration(0);

Determining the motor configuration online

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

// Online

// WARNING: You have to set the MotorType on G drives before

// you would like to get the current configuration, otherwise

// you will get an exception/feedback, which informs you that

// there is no motor set.

HardwareProjection hardwareProjection = onlineDfi.HardwareProjection;

// Get the current motor configuration

// It needs a datasetnumber, which is currently only supported on G120 drives.

MotorConfiguration motorConfiguration = hardwareProjection.GetCurrentMotorConfiguration(0);

The following example shows how you can create a motor configuration for G120 drives:

Configuring the motor configuration for G120 drives

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

DeviceItem cuDeviceItem = m_Device.DeviceItems[1];

DriveObject cuDriveObject = cuDeviceItem.GetService<DriveObjectContainer>().DriveObjects[0];

DriveFunctionInterface cuDriveFunctionInterface = cuDriveObject.GetService<DriveFunctionInterface>();

HardwareProjection hardwareProjection = cuDriveFunctionInterface.HardwareProjection;

hardwareProjection.SetMotorType(MotorType.InductionMotor, 0);

MotorConfiguration config = hardwareProjection.GetCurrentMotorConfiguration(0);

config.RequiredConfigurationEntries.ToList().ForEach(ce =>

{

switch (ce.Number)

{

case 305:

ce.Value = 20;

break;

case 307:

ce.Value = 30;

break;

case 311:

ce.Value = 200;

break;

case 304:

ce.Value = 450;

break;

case 310:

ce.Value = 50;

break;

case 335:

ce.Value = 1;

break;

default:

break;

}

});

bool result = cuDriveFunctionInterface.HardwareProjection.ProjectMotorConfiguration(config, 0);

The following examples show how you can configure motors for S120 and G220 drives:

Configuring motors for S120 and G220 drives

`private bool S120ProjectMotorConfigurationTestWithName_ServoInductionMotor()`

`{`

`m_Device.PlugNew(@"OrderNumber:6SL3120-1TE15-0Axx//10002", "", 65535); //momo`

`DeviceItem mmDeviceItem = m_Device.DeviceItems[2];`

`mmDeviceItem.PlugNew(@"OrderNumber:XMxxxxx-xxxxx-xxxx//Motor data input-Induction motors", "", 65535);`

`DriveObject mmDriveObject = mmDeviceItem.GetService<DriveObjectContainer>().DriveObjects[0];`

`DriveFunctionInterface mmDriveFunctionInterface = mmDriveObject.GetService<DriveFunctionInterface>();`

`HardwareProjection hwProjection = mmDriveFunctionInterface.HardwareProjection;`

`bool result = false;`

`try`

`{`

`MotorConfiguration motConfig = hwProjection.GetCurrentMotorConfiguration(0);`

`if (motConfig.RequiredConfigurationEntries.Count == 0 || motConfig.OptionalConfigurationEntries.Count == 0)`

`{`

`return false;`

`}`

`motConfig.RequiredConfigurationEntries.ToList().ForEach(ce =>`

`{`

`//get all other properties of motor`

`switch (ce.Name)`

`{`

`case "p305":`

`ce.Value = 1000;`

`break;`

`case "p307":`

`ce.Value = 500;`

`break;`

`case "p311":`

`ce.Value = 30;`

`break;`

`case "p304":`

`ce.Value = 10;`

`break;`

`case "p310":`

`ce.Value = 20;`

`break;`

`case "p322":`

`ce.Value = 22;`

`break;`

`case "p604":`

`ce.Value = 30;`

`break;`

`case "p605":`

`ce.Value = 45;`

`break;`

`case "p350":`

`ce.Value = 64;`

`break;`

`case "p354":`

`ce.Value = 65;`

`break;`

`case "p356":`

`ce.Value = 66;`

`break;`

`case "p358":`

`ce.Value = 67;`

`break;`

`case "p360":`

`ce.Value = 68;`

`break;`

`default:`

`break;`

`}`

`});`

`motConfig.OptionalConfigurationEntries.ToList().ForEach(ce =>`

`{`

`switch (ce.Name)`

`{`

`case "p308":`

`ce.Value = 1;`

`break;`

`case "p338":`

`ce.Value = 6000;`

`break;`

`case "p348":`

`ce.Value = 20000;`

`break;`

`default:`

`break;`

`}`

`});`

`result = hwProjection.ProjectMotorConfiguration(motConfig, 0);`

`}`

`catch (Exception ex)`

`{`

`Console.WriteLine(ex.Message + "\n" + ex.StackTrace);`

`TestInterface.Log.Error(ex.Message + "\n" + ex.StackTrace);`

`}`

`return result;`

`}`

### Reading and writing parameters

The following example shows how to read and write values of drive parameters. You require a drive object for access.

Access to parameters

using Siemens.Engineering.MC.Drives;

//Access a parameter via its name

DriveParameter parameter = driveObject.Parameters.Find("p5391[0]");

//Example of reading parameter attributes

if (parameter != null)

{

Console.WriteLine("The Name of the parameter is : " + parameter.Name);

Console.WriteLine("The value of the parameter is : " + parameter.Value.ToString());

Console.WriteLine("The minvalue of the parameter is : " + parameter.MinValue);

Console.WriteLine("The MaxValue of the parameter is : " + parameter.MaxValue);

Console.WriteLine("The Unit of the parameter is : " + parameter.Unit);

//Example for write:

parameter.Value = 60;

}

// Access a parameter via Number and ArrayIndex// Note that

//   - arrayless parameters (e.g. p96 on G120) are indexed by -1

//   - parameters that consist of only a bit array do not count as

//     array parameters, they are indexed by -1 as well and the

//     further bit values can be accessed by the 'Bits' property

//     of the given parameter (e.g. r2139 on G120). For further

//     information about accessing bit parameters see the next

//     section of this code snippet

DriveParameter r947_6 = driveObject.Parameters.Find(947, 6); // returns r947[6]if (r947_6 != null)

{

Console.WriteLine("The Name of the parameter is : " + r947_6.Name);

Console.WriteLine("The value of the parameter is : " + r947_6.Value.ToString());

}

//Accessing bit values

DriveParameter p2720 = driveObject.Parameters.Find(2720, 0);if (p2720 != null)

{

// Note that in general, pXXX.Bits[YYY] is not necessarily equivalent to pXXX.YYY.

// pXXX.Bits is an array of available bit values in ascending order by their names

// and not an array of bit values indexed by their names.

// For example: let the available bit values be [pXXX.0, pXXX.2, pXXX.3], then

// pXXX.Bits[2] == pXXX.3, not pXXX.2

DriveParameter p2720Bit1 = p2720.Bits[1]; // returns p2720[0].1

if (p2720Bit1 != null)

{

Console.WriteLine("The name of the parameter is : " + p2720Bit1.Name);

Console.WriteLine("The value of the second bit of the parameter is : " + p2720Bit1.Value.ToString());

}

}

//Get the enum values of a parameter

DriveParameter r47 = driveObject.Parameters.Find("r47");

foreach (var enumItem in r47.EnumValueList)

{

Console.WriteLine("Enum value: " + enumItem.Key.ToString() + " = " + enumItem.Value);

}

---

**See also**

[Contacts at Siemens](https://www.automation.siemens.com/aspa_app?ci=yes&lang=en)

### Reading and writing parameters online

The following example shows how to obtain a list with the available online parameters. You require an online drive object for access.

The read and write access to individual online parameters from the parameter list is identical to that in the [Reading and writing parameters](#reading-and-writing-parameters) example.

Access to online parameters

using Siemens.Engineering.MC.Drives;

DeviceItem item = ... //device item of the CU (e.g. : project.Devices[0].Items[0].Items[0])

OnlineDriveObject onlineDriveObject = item.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

if (onlineDriveObject != null)

{

var parameters = onlineDriveObject.Parameters;

}

### Saving the parameterization

The following example shows how you can determine the parameterization from S120, S210 or G120 drives.

Determining the parameterization online from the drives

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

OnlineDriveObject onlineDriveObject = item.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

OnlineDriveFunctionInterface onlineDfi = onlineDriveObject.GetService<OnlineDriveFunctionInterface>();

DriveDomainFunctions driveDomainFunctions = onlineDfi.DriveDomainFunctions;

// onlineDfi can be null in case of the actual onlineDriveObject

// does not support it or if the device is offline.

// driveDomainFunctions can be null, if the actual onlineDriveObject

// does not support it.

// For example: On G120 and S210 drives, you have to use the CU to get the onlineDriveObject.

// Please, pay attention at S120 drives. Here you can use any module (CU, MotorModul, lineModul) as onlineDriveObject but preferable the CU, because it will run on CU!

The following example shows how you can copy the parameterization for S120, S210 or G120 drives from RAM to ROM and thus store it in a power-independent manner.

Backing up from RAM to ROM

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

//In case of G120 device.

DeviceItem cuDeviceItem = m_Device.DeviceItems[1];

OnlineDriveObject cuDriveObject = cuDeviceItem.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

//In case of S120 and S210 device you should generally get the CU driveobject.

DeviceItem cuDeviceItem = m_Device.DeviceItems[0];OnlineDriveObject cuDriveObject = cuDeviceItem.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

// To use the function, you have to use the OnlineDriveFunctionInterface.

OnlineDriveFunctionInterface cuDriveFunctionInterface = cuDriveObject.GetService<OnlineDriveFunctionInterface>();

DriveDomainFunctions driveDomainFunctions = cuDriveFunctionInterface.DriveDomainFunctions;

// This function will perform a RAM to ROM copy on all device.

// It is important that the CU should be in online state before you call this function anyway the program will give an exception.

// This call may take a few moments before be finished.

bool result = DriveDomainFunctions.PerformRAMtoROMCopyAllDriveObject();

### How to assign a SecureString password

With the SetPassword() method you can assign passwords for secure communication during downloading. The parameter must be a SecureString.

The following example shows how to assign a SecureString password.

How to assign a SecureString password

public void SetPassword(DownloadPasswordConfiguration downloadPasswordConfiguration)

        {

            if (downloadPasswordConfiguration != null)

           {

                SecureString s = GetSecureString();

                downloadPasswordConfiguration.SetPassword(s);

                return;

            }

        }

  private SecureString GetSecureString()

        {

            SecureString securePwd = new SecureString();

            ConsoleKeyInfo key;

            Console.Write("Enter password: ");

            do

            {

                key = Console.ReadKey(true);

                // Ignore any key out of range.

                if (((int)key.Key) >= 65 && ((int)key.Key <= 90))

                {

                    // Append the character to the password.

                    securePwd.AppendChar(key.KeyChar);

                    Console.Write("*");

                }

                // Exit if Enter key is pressed.

            } while (key.Key != ConsoleKey.Enter);

            return securePwd;

        }

---

**See also**

[Encrypted communication with SecureString passwords](#encrypted-communication-with-securestring-passwords)

### Configuring Safety Integrated (checksums) (from SINAMICS FW V6.1)

The following examples show how you can configure Safety Integrated Functions via checksums for SINAMICS drives from firmware version V6.1 with Openness. This function is only available in the offline mode.

Before accessing `UpdateCheckSums`, the [drive object must first be determined](#determining-a-drive-object) via `DriveObject`.

Configuring Safety Integrated via checksums (only offline)

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

DriveObject cuDriveObject = cuDeviceItem.GetService<DriveObjectContainer>().DriveObjects[0];  
DriveFunctionInterface driveFunctionInterface = cuDriveObject .GetService<DriveFunctionInterface>();  
  
if (driveFunctionInterface.SafetyCommissioning == null)  
 {  
 return false;  
 }  
  
//UpdateCheckSums throws exception in case, if the specified CoreObject is null or not offline  
bool retValue = driveFunctionInterface.SafetyCommissioning.UpdateCheckSums();  
  
// onlineDfi can be null in case of the actual onlineDriveObject  
// does not support it or if the device is online.  
  
// G120 and S120 drives(drives with SINAMICS Firmware version older than V6.1) do not support it.  
// For G120 drives(CU250S-2_PN), driveFunctionInterface.SafetyCommissioning returns 'UpdateCheckSums is not supported for 2nd gen drives'  
// For S120 acx drives, driveFunctionInterface.SafetyCommissioning returns null

### Using Safety Integrated telegrams

The following example shows how you can use Safety Integrated telegrams (e.g. 30) in Openness.

Using Safety Integrated telegrams

using Siemens.Engineering.MC.Drives;

TelegramComposition telegrams = drvObj.Telegrams;

//Add safety telegram

const int tgrmNumber = 30;

drvObj.Telegrams.InsertSafetyTelegram(tgrmNumber);

//Find safety telegram

Telegram safetyTgrm = drvObj.Telegrams.Find(TelegramType.SafetyTelegram);

// Get and set safety telegram attributes

uint watchDogTime = (uint)safetyTgrm.GetAttribute("Failsafe_FMonitoringtime");

safetyTgrm.SetAttribute("Failsafe_FMonitoringtime", 300);

const int newSafetyTelegramNumber= 900;

if (safetyTgrm.CanChangeTelegram(newSafetyTelegramNumber))

{

safetyTgrm.TelegramNumber = newSafetyTelegramNumber;

}

//Remove Safety telegram

drvObj.Telegrams.EraseTelegram(TelegramType.SafetyTelegram);

### Setting the SIMOGEAR article number for G115D drives

The following example shows how you can set the SIMOGEAR article number for G115D drives.

Setting the SIMOGEAR article number for G115D drives

**using** Siemens.Engineering.MC.Drives;

Dvar commissioning= dfi.Commissioning;

var commissioning= dfi.Commissioning;

//Commissioning can be null if the actual driveobject does not support the Commissioning (e.g. SINAMICS S devices).

//Setting the article number of the SimoGear

commissioning.SetSimoGearMlfb("2KJ8001-2EG20-4DG1-D0X");

---

**See also**

[Commissioning](#commissioning)

### Using Technology Extensions

The following examples show how you can use Technology Extensions.

Install TechnologyExtensionPackage

string packageFilePath = @"Y:\\TRCDATA_V1_1_0_1.tec";

TechnologyExtensionInstallationProvider tecInstallationProvider = TiaPortal.GetService<TechnologyExtensionInstallationProvider>();

FileInfo packageFile = new FileInfo(packageFilePath);

try

{

tecInstallationProvider.Install(packageFile);

}

catch (EngineeringException ex)

{

Console.WriteLine(ex.Message + "\n" + ex.StackTrace);

}

Activate Technology Extension

TechnologyExtension tecExtension= ...

tecExtension.Activate();

return tecExtension.IsActivated;

Deactivate Technology Extension

TechnologyExtension tecExtension=...

tecExtension.Deactivate();

return tecExtension.IsActivated;

Uninstall TechnologyExtensionPackage

string tecPackageIdentifier = "TRCDATA/1100802";

bool confirmUninstallInUse = true;

TechnologyExtensionInstallationProvider tecInstallationProvider =

TiaPortal.GetService<TechnologyExtensionInstallationProvider>();

TechnologyExtensionPackage tecPackage = tecInstallationProvider.TechnologyExtensionPackages.Find(tecPackageIdentifier);

if (tecPackage == null)

{

Console.WriteLine("the specified TechnologyExtensionPackage '{tecPackageIdentifier}' was not found");

return;

}

try

{

tecInstallationProvider.Uninstall(tecPackage.Identifier, confirmUninstallInUse);

}

catch (EngineeringException ex)

{

Console.WriteLine(ex.Message + "\n" + ex.StackTrace);

}

Read out DriveObjectContainer of a SINAMICS device

**using** Siemens.Engineering;

**using** Siemens.Engineering.HW;

**using** Siemens.Engineering.MC.Drives

Device device = ...;

foreach (DeviceItem deviceItem in device.DeviceItems)

{

DriveObjectContainer doContainer = deviceItem.GetService<DriveObjectContainer>();

// do something

}

Navigate to a DriveObject

Device device = ...;

foreach (DeviceItem deviceItem in device.DeviceItems)

{

DriveObjectContainer doContainer = deviceItem.GetService<DriveObjectContainer>();

DriveObjectComposition driveObjects = doContainer.DriveObjects;

foreach (DriveObject driveObject in driveObjects)

{

// do something with the DriveObject

}

}

Navigate to a Technology Extension

DriveObject driveObject = ...

TechnologyExtensionContainer tecContainer = driveObject.GetService<TechnologyExtensionContainer>();

TechnologyExtensionComposition tecExtensions = tecContainer.TechnologyExtensions;

foreach (TechnologyExtension tecExtension in tecExtensions)

{

// do something with the TechnologyExtensions

}

Find TechnologyExtension using TechnologyExtension.Name

DriveObject driveObject = ...;

TechnologyExtensionContainer tecContainer = driveObject.GetService<TechnologyExtensionContainer>();

TechnologyExtension tecExtension = tecContainer.TechnologyExtensions.FirstOrDefault(x => x.Name == tecExtensionName);

// do something with the TechnologyExtension

---

**See also**

[TechnologyExtension](#technologyextension)
  
[TechnologyExtensionComposition](#technologyextensioncomposition)
  
[TechnologyExtensionInstallationProvider](#technologyextensioninstallationprovider)
  
[TechnologyExtensionPackage](#technologyextensionpackage)

### Connecting technology objects with hardware modules via telegram objects

You can connect technology objects with hardware modules via telegram objects using method Connect.

Connecting technology objects with hardware modules via telegram objects

private bool Test()  
{  
 Device plcStation = m_Project.Devices[0];   
 DriveObject driveObject = m_Project.Devices.ElementAt(1).DeviceItems[2].GetService<DriveObjectContainer>().DriveObjects[0];  
 Telegram telegram = driveObject.Telegrams[0];  
  
 DeviceItem plcDevice = plcStation.DeviceItems[1];  
 SoftwareContainer softwareContainer = plcDevice.GetService<SoftwareContainer>();  
 Software software = softwareContainer.Software;  
  
 TechnologicalInstanceDB techObj0 = ((Siemens.Engineering.SW.PlcSoftware)software).TechnologicalObjectGroup.TechnologicalObjects[0];  
 AxisHardwareConnectionProvider axisHardwareConnectionProvider0 = techObj0.GetService<AxisHardwareConnectionProvider>();  
 AxisEncoderHardwareConnectionInterface axisEncoderHardwareConnectionInterfaces0 = axisHardwareConnectionProvider0.ActorInterface;  
  
 try  
 {  
 axisEncoderHardwareConnectionInterfaces0.Connect(telegram); //Connect API  
 }  
 catch (Exception e)  
 {  
  
 }  
}

Connecting technology objects with a hardware module via a telegram object and ConnectOption.

private bool Test()  
{  
 Device plcStation = m_Project.Devices[0];   
 DriveObject driveObject = m_Project.Devices.ElementAt(1).DeviceItems[2].GetService<DriveObjectContainer>().DriveObjects[0];  
 Telegram telegram = driveObject.Telegrams[0];  
  
 DeviceItem plcDevice = plcStation.DeviceItems[1];  
 SoftwareContainer softwareContainer = plcDevice.GetService<SoftwareContainer>();  
 Software software = softwareContainer.Software;  
  
 TechnologicalInstanceDB techObj0 = ((Siemens.Engineering.SW.PlcSoftware)software).TechnologicalObjectGroup.TechnologicalObjects[0];  
 AxisHardwareConnectionProvider axisHardwareConnectionProvider0 = techObj0.GetService<AxisHardwareConnectionProvider>();  
 AxisEncoderHardwareConnectionInterface axisEncoderHardwareConnectionInterfaces0 = axisHardwareConnectionProvider0.ActorInterface;  
  
 try  
 {  
 //Connect API  
 axisEncoderHardwareConnectionInterfaces0.  
 Connect(telegram, Siemens.Engineering.MC.Drives.Enums.ConnectOption.Default); //Default = 0, AllowAllModules = 1  
 //Or the following way can also be used  
 axisEncoderHardwareConnectionInterfaces0.Connect(telegram, 0); //Default = 0, AllowAllModules = 1  
 }  
 catch (Exception e)  
 {  
  
 }  
}

---

**See also**

[HardwareProjection](#hardwareprojection)

### Inserting and extending telegrams

The following example shows how to insert an extension and change the size of a standard telegram. You require a drive object for access.

Inserting an extension and changing the size of a standard telegram

using Siemens.Engineering.MC.Drives;

TelegramComposition telegrams = drvObj.Telegrams;

Telegram telegram = telegrams.Find(TelegramType.MainTelegram);

Console.WriteLine("The Cu has the telegram: " + telegram.TelegramNumber);

Console.WriteLine("The Setpoint channel-specific size of the telegram is: " + telegram.GetOutputSize());

foreach (var address in telegram.Addresses)

{

if (address.IoType == AddressIoType.Output)

{

Console.WriteLine("The Setpoint channel-specific starting address of the connected PLC is: " + address.StartAddress);

}

else if(address.IoType == AddressIoType.Input)

{

Console.WriteLine("The Actual value channel-specific starting address of the connected PLC is: " + address.StartAddress);

}

}

// Add an additional Telegram

if (drvObj.Telegrams.CanInsertAdditionalTelegram(2,4))

{

drvObj.Telegrams.InsertAdditionalTelegram(2,4);

}

// Add a 3 word extension to the main telegram

Telegram mainTelegram == drvObj.Telegrams.Find(TelegramType.MainTelegram);

Int32 newSize = mainTelegram.GetSize(AddressIoType.Input) + 3;

if (mainTelegram.CanChangeSize(AddressIoType.Input, newSize, true))

{

mainTelegram.ChangeSize(AddressIoType.Input, newSize, true)

}

### Using torque telegrams

The following example shows how you can use torque telegrams (e.g. 750) in Openness.

Using torque telegrams

using Siemens.Engineering.MC.Drives;

const int torqueTelegramNumber = 750;

TelegramComposition telegrams = drvObj.Telegrams;

// Add a new torque telegram

if (drvObj.Telegrams.CanInsertTorqueTelegram(torqueTelegramNumber))

{

drvObj.Telegrams.InsertTorqueTelegram(torqueTelegramNumber);

}

// Find torque telegram

Telegram torqueTelegram = drvObj.Telegrams.Find(TelegramType.TorqueTelegram);

### Activating/deactivating UMAC for drives

The following examples show how you can activate and deactivate function User Management and Access Control (UMAC) for SINAMICS drives from firmware version V6.1 with Openness. With Openness, UMAC can only be activated or deactivated in the offline mode.

Before accessing `UmacConfiguration`, the [drive object must first be determined](#determining-a-drive-object) via `DriveObject`.

Activating UMAC (only offline)

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.Security;

DeviceItem cuDeviceItem = device.DeviceItems[0];  
DriveObject cuDriveObject = cuDeviceItem.GetService<DriveObjectContainer>().DriveObjects[0];  
Security cusecurity=cuDriveObject.Security;  
if(cuSecurity == null)

//For G120 drives(CU250S-2_PN), as UmacConfiguration is not supported for drives with SINAMICS Firmware version older than V6.1, the value of ''Security'' object will be null  
{  
 return false;  
}  
UmacConfiguration umacConfiguration = cusecurity.UmacConfiguration;

//Activate the UMAC for drive

bbool result = umacConfiguration.Activate();

Deactivating UMAC (only offline)

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.Security;

//For online  
OnlineDriveObject cuOnlineDriveObject = device.DeviceItems[itemPosition].GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];  
  
//Activate the DriveDataEncryption for the drive  
bool result = cuOnlineDriveObject.Security.DriveDataEncryption.Activate(curpassword);  
  
//Deactivate the DriveDataEncryption for drive  
bool result = cuOnlineDriveObject.Security.DriveDataEncryption.Deactivate(oldpassword);

//Deactivate the UMAC for the drive

bool result = umacConfiguration.Deactivate();

### Activating the encryption of drive data/DDE (from SINAMICS FW V6.1)

The following examples show how you can activate and deactivate the encryption of drive data (DDE, Drive Data Encryption) for SINAMICS drives from firmware version V6.1 with Openness.

Before accessing `DriveDataEncryption`, the [drive object must first be determined](#determining-a-drive-object) via `DriveObject`.

Activating and deactivating the encryption of drive data / DDE offline

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.Security;

//For offline  
DriveObject driveObject = device.DeviceItems[itemPosition].GetService<DriveObjectContainer>().DriveObjects[0];  
  
//Activate the DriveDataEncryption for the drive  
bool result = driveObject.Security.DriveDataEncryption.Activate(curpassword);  
  
//Deactivate the DriveDataEncryption for drive  
bool result = driveObject.Security.DriveDataEncryption.Deactivate(oldpassword);

Activating and deactivating the encryption of drive data / DDE online

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.Security;

//For online  
OnlineDriveObject cuOnlineDriveObject = device.DeviceItems[itemPosition].GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];  
  
//Activate the DriveDataEncryption for the drive  
bool result = cuOnlineDriveObject.Security.DriveDataEncryption.Activate(curpassword);  
  
//Deactivate the DriveDataEncryption for drive  
bool result = cuOnlineDriveObject.Security.DriveDataEncryption.Deactivate(oldpassword);

### Restoring factory settings

The following example shows how you can restore the factory settings for S120, S210 or G120 drives.

Restoring factory settings

using Siemens.Engineering.MC.Drives;

using Siemens.Engineering.MC.Drives.DFI;

using Siemens.Engineering.MC.Drives.Enums;

OnlineDriveObject onlineDriveObject = ...

OnlineDriveFunctionInterface onlineDfi = onlineDriveObject.GetService<OnlineDriveFunctionInterface>();

DriveDomainFunctions driveDomainFunctions = onlineDfi.DriveDomainFunctions;

// onlineDfi can be null in case of the actual onlineDriveObject

// does not support it or if the device is offline.

// saveParametrization can be null, if the actual onlineDriveObject

// does not support it.

// For example: On G120 and S210 drives, you have to use the CU to get the onlineDriveObject.

// S120 drives, you can use any module (CU, MotorModul, lineModul) as onlineDriveObject but preferable the CU.

//In case of G120 device

DeviceItem cuDeviceItem = g120Device.DeviceItems[1];

OnlineDriveObject cuDriveObject = cuDeviceItem.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

//In case of S120 and S210 devices you should generally get the CU driveobject

DeviceItem cuDeviceItem = s120Device.DeviceItems[0]

OnlineDriveObject cuDriveObject = cuDeviceItem.GetService<OnlineDriveObjectContainer>().OnlineDriveObjects[0];

// To use the function, you have to use the OnlineDriveFunctionInterface

OnlineDriveFunctionInterface cuDriveFunctionInterface = cuDriveObject.GetService<OnlineDriveFunctionInterface>();

DriveDomainFunctions driveDomainFunctions = cuDriveFunctionInterface.DriveDomainFunctions;

// This function will perform a FactoryReset for S120 drives

// It is important that the CU should be in online state before you call this function anyway the program will give an exception.  
// This call may take a few moments before be finished.

bool result = driveDomainFunctions.PerformFactoryReset(ResetMode.SafetyParameterReset);

//G120 drives have 2 flags for the ResetMode

The flag ParameterReset is used to reset the norml parameters.

The flag SafetyParameterReset is used to reset the safety parameters
