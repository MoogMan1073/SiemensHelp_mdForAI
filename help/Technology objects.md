---
title: "Technology objects"
package: ImExTOOpennessenUS
topics: 24
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technology objects

This section contains information on the following topics:

- [Overview of technology objects and versions](#overview-of-technology-objects-and-versions)
- [XML structure of the technology object interface section](#xml-structure-of-the-technology-object-interface-section)
- [Exporting technology objects](#exporting-technology-objects)
- [Importing technology objects](#importing-technology-objects)
- [S7-1200 Motion Control](#s7-1200-motion-control)
- [S7-1500 Motion Control](#s7-1500-motion-control)
- [PID control](#pid-control)
- [Counting](#counting)
- [Easy Motion Control](#easy-motion-control)

## Overview of technology objects and versions

### Technology objects

The following table shows the available technology objects for import and export.

| CPU | Technology | Technology object | Version of technology object | CPU FW |
| --- | --- | --- | --- | --- |
| S7-1200 | Motion Control | TO_PositioningAxis | ≥ V7.0 | ≥ V4.4 |
| TO_CommandTable |  |  |  |  |
| PID Control | PID_Compact | ≥ V2.3 | ≥ V4.2 |  |
| PID_3Step | V2.3 |  |  |  |
| PID_Temp | V1.1 |  |  |  |
| S7-1500 | Motion Control | TO_SpeedAxis | ≥ V5.0 | ≥ V2.8 |
| TO_PositioningAxis |  |  |  |  |
| TO_ExternalEncoder |  |  |  |  |
| TO_SynchronousAxis |  |  |  |  |
| TO_OutputCam |  |  |  |  |
| TO_CamTrack |  |  |  |  |
| TO_MeasuringInput |  |  |  |  |
| TO_Cam (S7-1500T) |  |  |  |  |
| TO_Kinematics (S7-1500T) |  |  |  |  |
| TO_LeadingAxisProxy (S7-1500T) |  |  |  |  |
| TO_Cam_10k (S7-1500T) | ≥ V6.0 | ≥ V2.9 |  |  |
| TO_Interpreter (S7-1500T) | ≥ V8.0 | ≥ V3.1 |  |  |
| TO_InterpreterMapping (S7-1500T) |  |  |  |  |
| TO_InterpreterProgram (S7-1500T) |  |  |  |  |
| Counting and measurement | High_Speed_Counter | ≥ V4.1 | Any |  |
| SSI_Absolute_Encoder | ≥ V3.1 |  |  |  |
| PID Control | PID_Compact | ≥ V2.3 | ≥ V2.0 |  |
| PID_3Step | V2.3 |  |  |  |
| PID_Temp | V1.1 |  |  |  |
| CONT_C | V1.1 | Any |  |  |
| CONT_S |  |  |  |  |
| TCONT_CP |  |  |  |  |
| TCONT_S |  |  |  |  |
| S7-300/400 | PID Control | CONT_C | V1.1 | Any |
| CONT_S |  |  |  |  |
| TCONT_CP |  |  |  |  |
| TCONT_S |  |  |  |  |
| TUN_EC |  |  |  |  |
| TUN_ES |  |  |  |  |
| PID_CP | V2.0 |  |  |  |
| PID_ES |  |  |  |  |
| EMC | AXIS_REF | V2.0 |  |  |

## XML structure of the technology object interface section

### Basic principle

The data in the XML file from the import/export is structured with reference to an openness XML file format. Every import file must fulfill the structural conditions.

The export file includes all edited tags and constants of the interface section of an exported technology object data block.

The project data can contain more data than the import XML file, e.g. external references. These must be exported separately.

Only writeable values can be imported via TIA Portal Openness XML.

Depending on the TIA Portal Openness export settings, the export file includes a defined set of attributes and elements. Export files from higher versions of the TIA Portal are not compatible with lower versions of the TIA Portal and could not be imported in those. SimaticML files exported with the latest TechObject version are also supported for the newer ones.

### Basic structure

The SimaticML format is nearly the same as the export/import format of user blocks.

For technology objects, the following elements are required inside the element SW.TechnologicalObject.TechnologicalInstandDB.

![Basic structure](images/169485346571_DV_resource.Stream@PNG-en-US.png)

- InstanceOfName

  The name of the instance, from which the technology object is derived.
- Interface

  - Sections elements represent the hierarchy structure of the technology object datatypes and their version.
  - Member elements represent all parameters mapped directly to the technology object data block tags.
  - The AttributeList includes all defined attributes of a member. Attributes, that are system defined or assigned by a default value are not listed in the XML structure. The member attributes &lt;ReadOnly&gt; and &lt;Informative&gt; are only written to the XMLexport file if their value is TRUE.
- Name

  The name of the technology object in TIA Portal project
- Number

  The number of the technology object data block in TIA Portal project
- OfSystemLibElement

  The type of the technology object
- OfSystemLibVersion

  The version of the technology object
- ParameterData

  - Parameter elements represent parameters, that are not mapped directly to technology object data block tags or parameters, that are read-only technology object data block tags but writeable in the PublicAPI.
  - AdditionalData elements represent informations that are not stored in technology object data block tags, par example connections to drives or other technology objects.
- ProgrammingLanguage

  The only valid content is Motion_DB.

### Parameters mapped directly to technology object data block tags

The sequence of the following description of elements represents parameters of a speed axis technology object mapped directly to technology object data blocks.

![Parameters mapped directly to technology object data block tags](images/169485334667_DV_resource.Stream@PNG-en-US.png)

### Parameters not mapped directly to technology object data block tags

The sequence of the following description of elements represents parameters of a speed axis technology object not mapped directly to technology object data blocks.

![Parameters not mapped directly to technology object data block tags](images/169485338635_DV_resource.Stream@PNG-en-US.png)

### Additional information

For more information concerning Interface element and attributes of SimaticML elements see [XML structure of the block interface section](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#xml-structure-of-the-block-interface-section) .

## Exporting technology objects

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- A project contains TO to be exported.
- PLC is not online.

### Application

The TIA Portal Openness API supports the export of all technology objects listed in the table [Overview of technology objects and versions](#overview-of-technology-objects-and-versions) to an XML file. You can only export consistent technology objects. Hardware configuration or tag tables are not exported with the technology object, but must be exported separately. You check the consistency of a technology object using the IsConsistent attribute. This flag can be set by successfully compiling of the respective technology object. The generation of the corresponding export file indicates that the export is completed.

In the following cases an exception is thrown:

- You try to export an inconsistent technology object.
- You try to export a technology object or a version of a technology object that does not support the export.
- You try to export a technology object while you are in online mode.

### Parameters of Motion Control technology objects

Most parameters of Motion Control technology objects are directly mapped to technology object data block tags. These parameters will be exported in XML element Member in the Interface section.

Parameters that do not map directly to technology object data block tags will be exported in XML element ParameterData.

Detailed description of parameters:

- [Specific parameters for TO_PositioningAxis and TO_CommandTable](#specific-parameters-for-to_positioningaxis-and-to_commandtable),
- [Specific parameters for Axis and Encoder technology objects](#specific-parameters-for-axis-and-encoder-technology-objects),
- [Specific parameters for LeadingAxisProxy technology objects](#specific-parameters-for-leadingaxisproxy-technology-objects)
- [Specific parameters for measuring input technology objects](#specific-parameters-for-measuring-input-technology-objects)
- [Specific parameters for output cam and cam track technology objects](#specific-parameters-for-output-cam-and-cam-track-technology-objects)
- [Specific parameters for Cam technology objects](#specific-parameters-for-cam-technology-objects)
- [Specific parameters for Kinematics technology objects](#specific-parameters-for-kinematics-technology-objects)

### Program code

void Export(FileInfo path, ExportOptions options);

The path parameter describes the path and file name of the export file that should be created. The parameter (ExportOptions options) specifies [options for the export](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#exporting-configuration-data).

| Attributes | Description |
| --- | --- |
| ExportOptions.None | Exports only modified parameters. |
| ExportOptions.WithDefaults | This option exports the parameters that have their default value. The default value itself is not exported. The same behavior is defined also for the TO specific parts of the XML export. The respective default values that are exported are defined for each TO type. |
| ExportOptions.WithReadOnly | This option exports additional informative attributes and values. During import, read only values are not written back to the DB. The respective read only values that are exported are defined for each TO type. |
| ExportOptions.WithDefaults | ExportOptions.WithReadOnly | Combination of the two options above. |

Modify the following program code to find and export a technology object to an XML file:

// Find a specific technology object by its name and export this

private static void ExportTechnologicalObject(FileInfo path, ExportOptions options, PlcSoftware plcSoftware, String nameOfTO)

{

    // Find by name

    TechnologicalInstanceDBComposition technologicalObjects = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects;

    TechnologicalInstanceDB technologicalObject = technologicalObjects.Find(nameOfTO);

// Export TO

  technologicalObject.Export(path, options);

}

Modify the following program code to export a technology object OutputCam to an XML file:

// Export OutputCam

private static void ExportOutputCam(FileInfo path, ExportOptions options, TechnologicalInstanceDB parentTO, String nameOfOutputCam)

{

//Retrieve service OutputCamMeasuringInputContainer

OutputCamMeasuringInputContainer container =

parentTO.GetService&lt;OutputCamMeasuringInputContainer&gt;();

//Get access to TO_OutputCam container

TechnologicalInstanceDBComposition outputcamCamtrackContainer = container.OutputCams;

//Find technology object TO_OutputCam

TechnologicalInstanceDB outputCam = outputcamCamtrackContainer.Find("nameOfOutputCam");

// Export

outputCam.Export(path, options);

}

## Importing technology objects

### Requirements

- The TIA Portal Openness application is connected to the TIA Portal.  
  See [Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
- A project is open.  
  See [Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)
- PLC is not online.

### Application

The TIA Portal Openness API supports the import of technology objects from an XML file.

### Exceptions

If the import data contains parameters that are not defined for the respective TO type, an EngineeringTargetInvocationException is thrown.

If the value of a parameter has a wrong format and cannot be converted to the type of the parameter, an EngineeringTargetInvocationException is thrown. The Import will be succeeded but an error will be produced on compile.

### Open connection

In TIA Portal, open connections are created when a tag that is connected to a TO is deleted. The further behavior of open connections is identical to the behavior of open connections created by deleting a connected tag. If the partner TO is missing during the import, an open connection will be established in this case. This also applies to TO types that can not be used for certain connections.

### Program code

IList&lt;SW.TechnologicalObjects.TechnologicalInstanceDB&gt; Import(FileInfo path, ImportOptions options);

Modify the following program code to import one or several technology objects from an XML file. For more information about the ImportOptions see [Importing configuration data](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#importing-configuration-data).

// Import technology objects

private static void Import(FileInfo path, ImportOptions options, PlcSoftware plcSoftware)

{

// Create technological instance

TechnologicalInstanceDBComposition technologicalObjects = plcSoftware.TechnologicalObjectGroup.TechnologicalObjects;

// Import TO

technologicalObjects.Import(path, options);

}

## S7-1200 Motion Control

This section contains information on the following topics:

- [Specific parameters for TO_PositioningAxis and TO_CommandTable](#specific-parameters-for-to_positioningaxis-and-to_commandtable)
- [External references](#external-references)

### Specific parameters for TO_PositioningAxis and TO_CommandTable

#### Application

The API supports the export and import of technology objects.

Parameters of TO_PositioningAxis and TO_CommandTable that are data block members are exported in the "Interface" section of the export file. Additional parameters are exported in the "ParameterData" section of the export file. The next chapter shows all additional parameters.

You can find a list of all available tags in SIMATIC STEP 7 S7-1200 Motion Control function manual on the [internet](https://support.industry.siemens.com/cs/ww/en/view/109773400).

> **Note**
>
> The data type information is only exported for parameters that are part of the "Interface" section.

#### Additional parameters TO_PositioningAxis

The following additional parameters are not directly mapped to DB members and will be exported in section ParameterData depending on the ExportOption:

| Symbol | Meaning |
| --- | --- |
| **Parameter Name** | **Possible Values** |
| _Actor.Interface.PTO | Pulse generator data:  0: Pulse_1  1: Pulse_2  2: Pulse_3  3: Pulse_4 |
| _Actor.Interface.EnableDriveOutput | Tag name of the connected device address |
| _Actor.Interface.DriveReadyInput | Tag name of the connected device address |
| _Actor.Interface.DataConnection | 0: Drive  1: DB |
| _Actor.Interface.DataBlock | See the functional view for possible values |
| _Actor.Interface.Analog | See the functional view for possible values |
| _Actor.Interface.ProfiDriveIn | Tag name of the connected device address |
| _Actor.Interface.ProfiDriveOut | Tag name of the connected device address |
| _Actor.DataAdaptionOffline | TRUE or FALSE |
| _Sensor[1].Interface.ProfiDriveIn | Tag name of the connected device address |
| _Sensor[1].Interface.ProfiDriveOut | Tag name of the connected device address |
| _ Sensor[1].Interface.EncoderConnection | 4: HSC  7: Encoder on PROFINET/PROFIBUS |
| _Sensor[1].DataAdaptionOffline | TRUE or FALSE |
| _Sensor[1].Interface.DataConnection | 0: Encoder  1: DB |
| _ Sensor[1].Interface.HSC | HSC number:   0: HSC_1   1: HSC_2   2: HSC_3   3: HSC_4 |
| _ Sensor[1].Interface.DataBlock | See the functional view for possible values |
| _ Sensor[1].PassiveHoming.DigitalInput | Tag name of the connected device address |
| _ Sensor[1].ActiveHoming.DigitalInput | Tag name of the connected device address |
| _PositionLimits_HW.MinSwitch | Tag name of the connected device address |
| _PositionLimits_HW.MaxSwitch | Tag name of the connected device address |

#### Additional parameters TO_CommandTable

The following additional parameters are not directly mapped to DB members:

| Parameter name | Possible values |
| --- | --- |
| _WarningsEnable | TRUE or FALSE |
| _UseAxisParametersFrom | "Sample axis", Name of axis |

### External references

#### External references at the TO_PositioningAxis

The configuration window of TO_PositioningAxis displays information that is not stored in technology object data block tags. This external information is therefore not part of the exported xml file.

The tags used by the axis for assignment between symbolic names and addresses are stored in a tag table and must be exported and imported separately.

If the following parameters have not previously been set in the hardware configuration, they must be set by [Writing parameters of technology object](Technology%20objects%20%28TOOpennessenUS%29.md#writing-parameters-of-technology-object).

**In case of PTO-Axis:**

An explicit set of _Actor.Interface.PTO to connect the technology object to the PTO-Output.

- _Actor.Interface.PTO_OutputA
- _Actor.Interface.PTO_OutputBEnable
- _Actor.Interface.PTO_OutputB
- _Actor.Interface.PTO_SignalType

Used digital inputs for homing

- _Sensor[1].ActiveHoming.DigitalInput
- _Sensor[1].PassiveHoming.DigitalInput

Used digital inputs for position limits

- _PositionLimits_HW.MaxSwitch
- _PositionLimits_HW.MinSwitch

**In case of Analog/ProfiDrive:**

An explicit set of following parameters to activate the PIP to OB-Servo:

- _Actor.Interface.ProfiDriveOutName
- _Actor.Interface.ProfiDriveInName
- _Sensor[1].Interface.ProfiDriveOutName
- _Sensor[1].Interface.ProfiDriveInName

**In case of HSC is used for encoder connection:**

An explicit set of _Sensor[1].Interface.HSC to connect the technology object to the HSC and activate the HSC in Hardware Configuration.

- _ Sensor[1].Interface.HSC_OperatingMode
- _ Sensor[1].Interface.HSC_InputA
- _ Sensor[1].Interface.HSC_InputB

## S7-1500 Motion Control

This section contains information on the following topics:

- [Specific parameters for Axis and Encoder technology objects](#specific-parameters-for-axis-and-encoder-technology-objects)
- [Specific parameters for LeadingAxisProxy technology objects](#specific-parameters-for-leadingaxisproxy-technology-objects)
- [Specific parameters for measuring input technology objects](#specific-parameters-for-measuring-input-technology-objects)
- [Specific parameters for output cam and cam track technology objects](#specific-parameters-for-output-cam-and-cam-track-technology-objects)
- [Specific parameters for Cam technology objects](#specific-parameters-for-cam-technology-objects)
- [Specific parameters for Kinematics technology objects](#specific-parameters-for-kinematics-technology-objects)
- [Specific parameters for Interpreter technology objects](#specific-parameters-for-interpreter-technology-objects)
- [Specific parameters for Interpreter program technology objects](#specific-parameters-for-interpreter-program-technology-objects)

### Specific parameters for Axis and Encoder technology objects

#### Application

The API supports the import and export of technology objects. The following section describes the specific parameters.

#### Export TO_SpeedAxis, TO_PositioningAxis, TO_SynchronousAxis and TO_ExternalEncoder

Some parameters that map to read-only technology object data block tags are writeable in the PublicAPI. This parameters will be exported to ParameterData in the exported xml-file. The parameter name, the allowed values and default values are the same ones as for the corresponding data block tags.

The affected parameters are listed in the following tables:

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | TO_SpeedAxis | TO_PositioningAxis / TO_SynchronousAxis | TO_ExternalEncoder |
| Actor.Type | X | X | - |
| Actor.Interface.EnableDriveOutput | X | X | - |
| Actor.Interface.DriveReadyInput | X | X | - |
| Actor.Interface.EnableTorqueData | X | X | - |
| VirtualAxis.Mode | X | X | - |
| Sensor[n].Existent<sup>1)</sup> | - | X | - |
| Sensor[n].Interface.Number<sup>1)</sup> | - | X | - |
| Sensor[n].Type<sup>1)</sup> | - | X | - |
| Sensor.Interface.Number | - | - | X |
| Sensor.Type | - | - | X |
| CrossPlcSynchronousOperation.Interface[n].EnableLeadingValueOutput<sup>5)</sup> | - | X | X |
| <sup>1)</sup> S7-1500 PLC: n=1; S7-1500T PLC: 1≤n≤4    <sup>4)</sup> ≥V5.0   <sup>5)</sup> V5.0 n=1; ≥V6.0 1≤n≤8 |  |  |  |

Some parameters do not map directly to technology object data block tags. This parameters will be exported to ParameterData in the exported xml-file. The parameter name, the allowed values and default values are the same ones as for the corresponding data block tags.

The affected parameters are listed in the following tables:

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **Name** | **Default Value** | TO_SpeedAxis | TO_PositioningAxis / TO_SynchronousAxis | TO_ExternalEncoder |
| _Actor.DataAdaptionOffline | false | X | X | - |
| _Actor.Interface.Telegram | 0 | X | X | - |
| _Units.LengthUnit | 1013 (mm) | - | X | X |
| _Units.VelocityUnit | 1062 (mm/s) | 1083 (1/mm) | X | X |
| _Units.TorqueUnit | 1126 (Nm) | X | X | - |
| _Units.ForceUnit | 1120 (N) | - | X | - |
| _Sensor[n].DataAdaptionOffline<sup>1)</sup> | false | - | X | - |
| _Sensor[n].Interface.Telegram<sup>1)</sup> | 0 | - | X | - |
| _Sensor.DataAdaptionOffline | false | - | - | X |
| _Sensor.Interface.Telegram | false | - | - | X |
| _Properties.MotionType | 0 | - | X | X |
| _Properties.UseHighResolutionPositionValues<sup>4)</sup> | false | - | X | X |
| _CrossPlcSynchronousOperation.ActivateLocalLeadingValueDelayTimeCalculation<sup>4)</sup> | true | - | X | X |

Some parameters do not map directly to technology object data block tags. This parameters will be exported to ParameterData in the exported xml-file. In SimaticML, only the name of the connected tag is exported.

The affected parameters are listed in the following tables:

|  |  |  |  |
| --- | --- | --- | --- |
| **Name** | TO_SpeedAxis | TO_PositioningAxis / TO_SynchronousAxis | TO_ExternalEncoder |
| _Actor.Interface.EnableDriveOutputAddress | X | X | - |
| _Actor.Interface.DriveReadyInputAddress | X | X | - |
| _Sensor[n].ActiveHoming.DigitalInputAddress<sup>1)</sup> | - | X | - |
| _Sensor[n].PassiveHoming.DigitalInputAddress<sup>1)</sup> | - | X | - |
| _Sensor.ActiveHoming.DigitalInputAddress | - | - | X |
| _Sensor.PassiveHoming.DigitalInputAddress | - | - | X |
| _PositionLimits_HW.MinSwitchAddress | - | X | - |
| _PositionLimits_HW.MaxSwitchAddress | - | X | - |
| _CrossPlcOperation.Interface[n].AddressOut<sup>5)</sup> | - | X | X |

#### XML element Connection

The XML element Connection describes the connections of a technology object. The names and values of the attributes listed below correspond to the parameter names and values of the particular AxisEncoderHardwareConnectionInterface.

- Required Attribute "Interface"

  - Possible values:

  |  |  |  |  |
  | --- | --- | --- | --- |
  | **Value** | TO_SpeedAxis | TO_PositioningAxis / TO_SynchronousAxis | TO_ExternalEncoder |
  | Actor | X | X | - |
  | Sensor | - | - | X |
  | Sensor[n]<sup>1)</sup> | - | X | - |
  | Torque | X | X | - |
  | 1) S7-1500 PLC: n=1; S7-1500T PLC: 1≤n≤4 |  |  |  |
- Optional Attributes InputAddress and OutputAddress

  - Both attributes must either be present together or not be used at all
  - The possible values are bit addresses (as in API)
  - The attribute describes connections to DeviceItems and Channels
- Optional Attribute ConnectOption

  - May only be used together with InputAddress and OutputAddress
  - The attribute corresponds to method parameter of same name at AxisEncoderHardwareConnectionInterface.Connect
  - The attribute has the possible values Default and AllowAllModules
- Optional Attribute SensorIndexInActorTelegram

  - The attribute is used for connections to sensor part in actor telegram
  - The rules are the same as defined for the according API attribute
- Optional Attribute PathToDBMember

  - The attribute has the same possible values as for parameter of corresponding method
  - Describes a connection to a DB member
- Optional Attribute OutputTag

  - The value is name of connected PlcTag
  - The attribute describes a connection to an analog tag

#### Connect TO_SynchronousAxis with leading values

You connect TO_SynchronousAxis with leading values via the service SynchronousAxisMasterValues, see [Connecting synchronous axis with leading values](Technology%20objects%20%28TOOpennessenUS%29.md#connecting-synchronous-axis-with-leading-values).

### Specific parameters for LeadingAxisProxy technology objects

#### Application

The API supports the import and export of technology objects. The following section describes the specific parameters.

#### Export TO_LeadingAxisProxy

The parameter _Interface.AddressIn does not map directly to technology object data block tags. These parameters will be exported to ParameterData in the exported xml-file. In SimaticML, only the name of the connected tag is exported.

Here the same rules apply as described in [Specific parameters for Axis and Encoder technology objects](#specific-parameters-for-axis-and-encoder-technology-objects).

### Specific parameters for measuring input  technology objects

#### Application

The API supports the import and export of technology objects. The following section describes the specific parameters.

#### Export TO_MeasuringInput

Some parameters that map to read-only technology object data block tags are writeable in the PublicAPI. These parameters will be exported to ParameterData in the exported xml-file.

Some parameters do not map directly to technology object data block tags. This parameters will be exported to ParameterData in the exported xml-file.

The parameter name, the allowed values and default values are the same ones as for the corresponding data block tags.

The attribute ParameterDatacontains the following parameters for TO_MeasuringInput:

- Parameter.MeasuringInputType
- _ListenToMeasuringInput

The parameter "_AssociatedObject" does not map directly to technology object data block tag. It will not be exported to ParameterData in the exported xml-file.

#### XML element "Connection"

The XML element Connection describes the connections of a technology object. The names and values of the attributes listed below correspond to the parameter names and values of the particular MeasuringInputHardwareConnectionProvider.

| Symbol | Meaning |
| --- | --- |
| **Value** | Description |
| Interface | Single possible value: MeasuringInput |
| InputAddress | - The value is bit address - It describes a connection to a DeviceItem or a channel |

---

**See also**

[Connecting to the TIA Portal](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#connecting-to-the-tia-portal)
  
[Opening a project](TIA%20Portal%20Openness%20API%20for%20automation%20of%20engineering%20workflows.md#opening-a-project)

### Specific parameters for output cam and cam track technology objects

#### Application

The API supports the import and export of technology objects. The following section describes the specific parameters.

#### Export TO_OutputCam and TO_CamTrack

Some parameters that map to read-only technology object data block tags are writeable in the PublicAPI. These parameters will be exported to ParameterData in the exported xml-file. The parameter name, the allowed values and default values are the same ones as for the corresponding data block tags.

For TO_OutputCam the attribute ParameterDatacontains the parameter Interface.LogicOperation.

TO_CamTrack does not have any elements in the attribute ParameterData.

The parameter "_AssociatedObject" does not map directly to technology object data block tag. It will not be exported to ParameterData in the exported xml-file.

#### XML element "Connection"

The XML element Connection describes the connections of a technology object. The names and values of the attributes listed below correspond to the parameter names and values of the particular OutputCamHardwareConnectionProvider.

|  |  |  |  |
| --- | --- | --- | --- |
| **Value** | Description | TO_OutputCam | TO_CamTrack |
| Interface | Single possible value: OutputCam | X | - |
| OutputAddress | - The value is bit address - It describes a connection to a channel | X | X |
| OutputTag | - The value is name of connected PlcTag - It describes a connection to an analog tag | X | X |

### Specific parameters for Cam technology objects

#### Application

The API supports the import and export of technology objects. The following section describes the specific parameters.

#### Export TO_Cam or TO_CAM_10k

The cam profile of a cam technology object of type TO_Cam or of type TO_CAM_10k will be exported to the element ParameterData.

The sequence of the following description of elements represents the structure of ParameterData.

![Export TO_Cam or TO_CAM_10k](images/169485342603_DV_resource.Stream@PNG-en-US.png)

#### XML structure of ParameterData

| XML element | Description |
| --- | --- |
| ProfileData | The XML element ProfileData is a single child element of Parameters inside the EOM attribute ParameterData.  Top level extension element, contains the XML element GeneralConfiguration followed by the XML element Elements. |
| GeneralConfiguration | The XML element GeneralConfiguration describes the general configuration that is valid for the complete cam profile.  Additionally, the following optional attributes are used:  - Attribute StandardContinuity Possible values are Position, Velocity, Acceleration (default value) and Jerk - Attribute StandardOptimizationGoal Possible values are None (default value), Velocity, Acceleration, Jerk and DynamicMoment - Attribute InterpolationMode Possible values are Linear, CubicSpline (default value) and BezierSpline - Attribute BoundaryConditions Possible values are NoConstraint (default value) and FirstDerivative |
| DesignLeadingRange | The XML element describes the leading value range of the curve definition.  The following two optional attributes with datatype xsd:float are used:  - Attribute Start Default value is 0 - Attribute End  Default value is 360   The value of Start must be less than the value of End. |
| DesignFollowingRange | The XML element describes the following value range of the curve definition.   - Attribute Start Default value is -1 - Attribute End  Default value is 1 |
| Elements | The XML element contains the list of cam profile elements.   Possible XML elements are:  - Point - Line - Polynomial - VDITransition - Sine - InverseSine - PointGroup   Except of the XML element Point, all XML Elements uses the required XML attributes StartX and EndX of type xsd:float.  These attributes contain the X coordinate at the start respectively the end of the segment. |
| Point | The XML element describes a single point. The following attributes are used, all of them have the datatype xsd:float and default value 0:  - Required Attribute X - Required Attribute Y - Optional Attribute Velocity - Optional Attribute Acceleration - Optional Attribute Jerk |
| Line | The XML element describes a Line segment. The following attributes are used, all of them have the datatype xsd:float and default value 0:  - Optional Attribute StartY  Contains the Y coordinate at the start of the line - Optional Attribute EndY Contains the Y coordinate at the end of the line - Optional Attribute Gradient Contains the gradient of the line   Two of these three optional attributes must be present in the export.XML |
| Polynomial | The XML element describes a Polynomial segment. The XML element Polynomial has the sub elements TrigonometricValues, Coefficients and Constraints.TrigonometricValues can be used optionally, but either Coefficients or Constraints need to be present. |
| TrigonometricValues | The XML element TrigonometricValues can be optionally used as sub element of Polynomial.  It has the following attributes with datatype xsd:float:  - Optional Attribute Amplitude Default value is 1 - Optional Attribute StartPhase Default value is 0 - Optional Attribute EndPhase Default value is 6.2831853071795862 - Optional Attribute Frequency Default value is 1 - Optional Attribute PeriodLength Default value is 1   Two of the attributes StartPhase, EndPhase, Frequency and PeriodLength must be used. Additionally, at least StartPhase or EndPhase needs to be present. |
| Coefficients | The XML element Coefficients can be optionally used as sub element of Polynomial.It has the optional attributes C0, C1, C2, C3, C4, C5 and C6. Each of them has the datatype xsd:float and the default value 0. |
| Constraints | This XML element can be optionally used as sub element of Polynomial.  It has the following attributes with datatype xsd:float and default value 0:  Optional Attribute LeftValue  Optional Attribute RightValue  Optional Attribute LeftVelocity  Optional Attribute RightVelocity  Optional Attribute LeftAcceleration  Optional Attribute RightAcceleration  Optional Attribute LeftJerk  Optional Attribute RightJerk  Optional Attribute Lambda   Additionally, it has the optional attribute LambdaMode which supports the values Relative and Absolute (default value). |
| VDITransition | The XML element describes a VDI transition segment.  It has the optional attributes LeftContinuity and RightContinuity which can have the values AsProfile (default value), Position, Velocity, Acceleration and Jerk.  Additionally, the optional attribute OptimizationGoal with the possible values AsProfile (default value), None, Velocity, Acceleration, Jerk and DynamicMoment can be used. |
| InverseSine | The XML element describes an InverseSine segment. It has the following optional attributes:  - InterpolationPointCount - MaxFollowingValueTolerance - MathStartX - MathEndX - Minimum - Maximum - Inversed |
| Sine | The XML element describes a Sine segment. The Sine element has the following attributes:  - Amplitude - StartPhase - EndPhase - Frequency - PeriodLength - Inclination - StartOffset - EndOffset |
| PointGroup | The XML element describes a PointGroup segment that contains several Points. The PointGroup element has the following optional attributes:  - ApproximationDataPoints - ApproximationTolerance - LeadingValueMode - FollowingValueMode - ApproximationMode |

### Specific parameters for Kinematics technology objects

#### Application

The API supports the import and export of technology objects. The following section describes the specific parameters.

#### Export TO_Kinematics

Some parameters that map to read-only technology object data block tags are writeable in the PublicAPI. These parameters will be exported to ParameterData in the exported xml-file. The parameter name, the allowed values and default values are the same ones as for the corresponding data block tags.

- Kinematics.TypeOfKinematics
- MotionQueue.MaxNumberOfCommands

Some parameters do not map directly to technology object data block tags. These parameters will be exported to ParameterData in the exported xml-file. The parameter name, the allowed values and default values are the same ones as for the corresponding data block tags.

The affected parameters are listed in the following tables:

| Name | Default value |
| --- | --- |
| _Units.LengthUnit | 1013 (mm) |
| _Units.LengthVelocityUnit | 1062 (mm/s) |
| _Units.AngleUnit | 1126 (Nm) |
| _Units.AngleVelocityUnit | 1120 (N) |
| _Properties.UseHighResolutionPositionValues<sup>6)</sup> | false |
| _X_Minimum | 0.0 |
| _X_Maximum | 0.0 |
| _Y_Minimum | 0.0 |
| _Y_Maximum | 0.0 |
| _Z_Minimum | 0.0 |
| _Z_Maximum | 0.0 |
| _A3_Maximum | 0.0 |

#### XML structure of Connection

The XML element Connection describes the connections of a technology object.

The names and values of the attributes listed below correspond to the parameter names and values of the particular AxisEncoderHardwareConnectionInterface.

| XML element | Description |
| --- | --- |
| AdditionalData | The element contains up to six KinematicsAxis elements, followed by one ConveyorTrackingLeadingValues element. |
| KinematicsAxis | The element describes a connected kinematics axis. This XML element has the following attributes:  - Required Attribute Index   The value of the index must be unique.    - &lt;V7.0 Possible values are 1..4     The index values corresponds to kinematics axis A1 to A4.   - As of V7.0 Possible values are 1..6     The index values corresponds to kinematics axis A1 to A6.     Kinematics axes A5 and A6 can only be used with "S7-1500T Motion Control KinPlus". - Required Attribute Ref Denotes the name of the connected axis technology object. This reference needs to be unique. - Required attribute Type Contains the type of the connected axis. The version of the connected axis is not nessassary. |
| ConveyorTrackingLeadingValues | The element contains elements for SetPointCoupling followed by elements for ActualValueCoupling, DelayedCoupling. |
| SetPointCoupling | The element describes a connected leading value TO that is coupled via setpoint values. It has the following attributes:  - Required Attribute Ref Denotes the name of the connected technology object which provides the leading value for conveyor tracking. - Required attribute Type Contains the associated TO type (version independent) |
| ActualValueCoupling | The element describes a connected leading value TO that is coupled via actual values. The same attributes as at SetPointCoupling elements are used. |
| DelayedCoupling | The element describes a connected leading value TO that is coupled via actual values. The same attributes as at SetPointCoupling elements are used. |

### Specific parameters for Interpreter technology objects

#### Application

The API supports the import and export of technology objects. The following section describes the specific parameters.

#### Export TO_Interpreter

The parameter Parameter.MaxNumberOfCommands maps to the read-only technology object data block tag that is writeable in the PublicAPI.

The parameter Parameter.MaxNumberOfCommands will be exported to ParameterData in the exported xml-file. The parameter name, the allowed values and default values are the same ones as for the corresponding data block tags.

### Specific parameters for Interpreter program technology objects

#### Application

The API supports the import and export of technology objects.

The interpreter program technology object does not have any parameters.

#### Export TO_InterpreterProgram

The source code of the interpreter program technology object will be exported to the XML element SourceData.

The following sequence of elements represents the structure of ParameterData.

![Export TO_InterpreterProgram](images/168196179339_DV_resource.Stream@PNG-en-US.png)

## PID control

This section contains information on the following topics:

- [Specific attributes for PID_Compact](#specific-attributes-for-pid_compact)
- [Specific attributes for PID_3Step and PID_Temp](#specific-attributes-for-pid_3step-and-pid_temp)

### Specific attributes for PID_Compact

The API interface supports the export and import of technology objects. You can find a list of all available variables in "SIMATIC S7-1200/S7-1500 PID control" function manual on the [internet](https://support.industry.siemens.com/cs/ww/en/view/108210036).

#### Export

For the PID_Compact technology object all parameters are directliy mapped to technology object data block tags. All parameters have the same data type and the default value as defined in the date block. The XML element `ParameterData` is empty.

#### Import

As of Version PID_Compact V3.0 all parameters are part of the import.

Up to PID_Compact V2.4 the following parameters for PID_Compact are not part of the import:

- PhysicalUnit
- PhysicalQuantity
- _Config.OutputSelect
- _Retain.CtrlParams.SetByUser

These parameters will have the default value after the import.

> **Note**
>
> Up to PID_Compact V2.4, remake the associated settings manually after an import of the export file. This can be done by using the function [Writing parameters](Technology%20objects%20%28TOOpennessenUS%29.md#writing-parameters-of-technology-object).

### Specific attributes for PID_3Step and PID_Temp

The API interface supports the export and import of technology objects. You can find a list of all available variables in "SIMATIC S7-1200/S7-1500 PID control" function manual on the [internet](https://support.industry.siemens.com/cs/ww/en/view/108210036).

#### Export

For the PID_3Step and PID_Temp technology objects all parameters are directliy mapped to technology object data block tags. All parameters have the same data type and the default value as defined in the date block. The XML element `ParameterData` is empty.

#### Import

The following parameters for PID_3Step and PID_Temp are not part of the import:

- PhysicalUnit
- PhysicalQuantity

These parameters will have the default value after the import. If you want to modify them you have to use the function [Writing parameters](Technology%20objects%20%28TOOpennessenUS%29.md#writing-parameters-of-technology-object).

> **Note**
>
> Remake the associated settings manually after an import of a PID_3Step or PID_Temp export file.

## Counting

This section contains information on the following topics:

- [Specific attributes for High_Speed_Counter and SSI_Absolute_Encoder](#specific-attributes-for-high_speed_counter-and-ssi_absolute_encoder)

### Specific attributes for High_Speed_Counter and SSI_Absolute_Encoder

The API interface supports the export and import of technology objects. You can find a list of all available parameters in the product information "Parameters of technology objects in TIA Portal Openness" on the [internet](https://support.industry.siemens.com/cs/ww/en/view/109744932).

For the TO types High_Speed_Counter and SSI_Absolute_Encoder all parameters correspond to TO DB members and have the data type and the default value as defined in the TO DB. The EOM attribute `ParameterData` is empty.

## Easy Motion Control

This section contains information on the following topics:

- [Specific attributes for AXIS_REF](#specific-attributes-for-axis_ref)

### Specific attributes for AXIS_REF

The API interface supports the export and import of technology objects. You can find a list of all available parameters in the product information "Parameters of technology objects in TIA Portal Openness" on the [internet](https://support.industry.siemens.com/cs/ww/en/view/109744932).

For the TO type AXIS_REF all parameters correspond to TO DB members and have the data type and the default value as defined in the TO DB. The EOM attribute `ParameterData` is empty.
