---
title: "CloudConnect: Topics and groups"
package: OPCUAPubSubenUS
topics: 18
source: Siemens TIA Portal Information System (offline help, en-US)
---


# CloudConnect: Topics and groups

This section contains information on the following topics:

- [Parameters of the topics / groups](#parameters-of-the-topics-groups)
- [Properties dialog of the topics](#properties-dialog-of-the-topics)

## Parameters of the topics / groups

This section contains information on the following topics:

- [Configuring topics or groups](#configuring-topics-or-groups)
- [Topic editor](#topic-editor)
- [User data editor](#user-data-editor)

### Configuring topics or groups

#### Configuration under different cloud operators

By selecting the cloud provider, you determine whether topics or groups are configured for the data transmission:

- MindConnect IoT Extension

  You can create several groups.

  A group can contain multiple data points.

  In IoT Extension, a group corresponds to the structure characteristic "Series". All groups are permanently assigned to the standard topic "s/us".
- Other Cloud

  You can create several topics.

  A topic can contain multiple data points.

#### Opening the Topic editor

Open the Topic editor as follows:

1. Expand the project tree:

   Station > Local modules > CP 1545-1 > Cloud connection >

   - "Published topics" / "Subscribed topics" or
   - "Published groups"
2. Click on "Add Topic" or "Add Group".

   The Topic editor is opened and a new topic or group is created.

#### Opening the payload editor

When the Topic editor is open, you can see the following two tabs in the upper right corner:

- Topic editor
- Payload editor

You can switch between the two editors by clicking on the tabs.

In the Payload editor, you define the format of the payload to be published.

> **Note**
>
> **Configuring the payload format for publishers only**
>
> Note that the payload format is only configured for data that is published.

#### Exporting and importing CloudConnect data in XML format

Open the dialog as follows:

1. Make sure that the correct Cloud provider is selected in the general device settings:

   - For topics: Other cloud
   - For groups: Siemens MindSphere - MindConnect IoT Extension
2. Expand the project tree:

   Station > Local modules > CP 1545-1 > Cloud connection
3. In the shortcut menu, click on "Export CloudConnect Data" or "Import CloudConnect data".

   The window for importing and exporting the file is opened in *.XML format.

**General information:**

- When you omit an optional element/attribute, it will receive the respective default value in TIA.
- If the *.XML file contains invalid inputs, you will receive the corresponding error messages in TIA.
- Only published topics (and subscribed topics, if applicable) or subscribed groups may be present, but not both at the same time.
- To import tags into data points, these must exist in the CPU of the target device. If the tag name contained in the XML file is not found during the import, the respective field will remain empty after the import. To still be able to use the data point, you must select a tag for the data point.

#### XML syntax and permitted values

| Syntax | Element/attribute name | Permitted data types and values | Meaning/Comment |
| --- | --- | --- | --- |
| `<PublishedGroup>` or `<PublishedTopic>` |  |  |  |
| `<General>` | - Name - Author - Comment | - String - String - String | - Required - Optional - Optional |
| `<QoS>` |  | Integer; 0-2 | Optional |
| `<TimeTrigger> <Cyclic>`      `oder`      `<TimeTrigger> <Date>` | - CycleTime - Frequency - TimeOfTheDay - Weekday - DayOfTheMonth | - Integer; 10-4294967295, ms - String; Daily, Weekly, Monthly - Integer; 0-1439, minutes (00:00 - 23:59 in minutes) - String; Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday - Integer; 1-31 | - Required for element `TimeTrigger > Cyclic` Required for element `TimeTrigger > Date` - Optional - Optional - Optional |
| `<DataPoints> <DataPoint> <General>`    `<DataPoints> <DataPoint> <General> <Tag>` | - Name | - String - String | - Required - Optional |
| `<DataPoints> <DataPoint> <ValueTrigger>` | - Type - Value - RangeLow - RangeHigh | - String; Deviation, Lower Threshold, Upper Threshold, Outside Range, Inside Range - String - String - String | - Required for element `ValueTrigger` - Optional - Optional - Optional |
| `<Payload>` | - Format - Customize | - String; XML, JSON, MindConnect IoT Extension, Custom - Boolean; true, false - <![CDATA[Permitted content see section [Payload formats](#payload-formats)]]> | - Required - Optional - Optional |
| `<SubscribedTopic>` |  |  |  |
| `<General>` | - Name - Author - Comment | - String - String - String | - Required - Optional - Optional |
| `<QoS>` |  | Integer; 0-2 | Optional |
| `<DataPoints> <DataPoint> <General>`    `<DataPoints> <DataPoint> <General> <Tag>` | - Name | - String - String | - Required - Optional |

#### XML structure

`<?xml version="1.0" encoding="UTF-8"?>`

`<CloudConnectData>`

`<PublishedTopics>`

`<PublishedTopic>`

`<General Name="Published Topic_1" Author="Jane Doe" Comment="My published topic"/>`

`<QoS>1</QoS>`

`<TimeTrigger>`

`<Date Frequency="Daily" TimeOfTheDay="720"/>`

`</TimeTrigger>`

`<DataPoints>`

`<DataPoint>`

`<General Name="Published_datapoint_1">`

`<Tag>"Data_block_1"."Enabled"</Tag>`

`</General>`

`</DataPoint>`

`<DataPoint>`

`<General Name="Published_datapoint_2">`

`<Tag>"Data_block_1"."LastStatusMsg"</Tag>`

`</General>`

`</DataPoint>`

`<DataPoint>`

`<General Name="Published_datapoint_3">`

`<Tag>"Data_block_1"."ErrorCount"</Tag>`

`</General>`

`<ValueTrigger Type="Deviation" Value="1"/>`

`</DataPoint>`

`</DataPoints>`

`<Payload Format="XML" Customize="true">`

`<![CDATA[<?xml version="1.0" encoding="UTF-8"?>`

`<root>`

`<!-- Custom plant identification number -->`

`<MyCustomXMLTag>0123456789</MyCustomXMLTag>`

`<DataItems>`

`<DataItem>`

`<Variable>{{Published_datapoint_1.NAME}}</Variable>`

`<Type>{{Published_datapoint_1.TYPE}}</Type>`

`<Value>{{Published_datapoint_1.VALUE}}</Value>`

`</DataItem>`

`<DataItem>`

`<Variable>{{Published_datapoint_2.NAME}}</Variable>`

`<Type>{{Published_datapoint_2.TYPE}}</Type>`

`<Value>{{Published_datapoint_2.VALUE}}</Value>`

`</DataItem>`

`<DataItem>`

`<Variable>{{Published_datapoint_3.NAME}}</Variable>`

`<Type>{{Published_datapoint_3.TYPE}}</Type>`

`<Value>{{Published_datapoint_3.VALUE}}</Value>`

`<QualityCode>{{Published_datapoint_3.QUALITY_CODE}}</QualityCode>`

`</DataItem>`

`</DataItems>`

`</root>]]>`

`</Payload>`

`</PublishedTopic>`

`<PublishedTopic>`

`<General Name="Published Topic_2" Author="Jane Doe" Comment="Another published topic"/>`

`<QoS>2</QoS>`

`<TimeTrigger>`

`<Cyclic CycleTime="500"/>`

`</TimeTrigger>`

`<DataPoints>`

`<DataPoint>`

`<General Name="Published_datapoint_1">`

`<Tag>"Data_block_1"."Actuation_Speed"</Tag>`

`</General>`

`<ValueTrigger Type="Inside Range" RangeLow="150" RangeHigh="300"/>`

`</DataPoint>`

`<DataPoint>`

`<General Name="Published_datapoint_2">`

`<Tag>"Data_block_1"."X-Position"</Tag>`

`</General>`

`<ValueTrigger Type="Outside Range" RangeLow="0" RangeHigh="200"/>`

`</DataPoint>`

`</DataPoints>`

`<Payload Format="XML"/>`

`</PublishedTopic>`

`<PublishedTopic>`

`<General Name="Published Topic_3" Author="Jane Doe" Comment="Yet another published topic"/>`

`<QoS>0</QoS>`

`<TimeTrigger>`

`<Date Frequency="Weekly" Weekday="Wednesday"/>`

`</TimeTrigger>`

`<DataPoints>`

`<DataPoint>`

`<General Name="Published_datapoint_1">`

`<Tag>"Data_block_2"."ManufacturedItems"</Tag>`

`</General>`

`<ValueTrigger Type="Lower Threshold" Value="50"/>`

`</DataPoint>`

`<DataPoint>`

`<General Name="Published_datapoint_2">`

`<Tag>"Data_block_1"."RejectedQuality"</Tag>`

`</General>`

`<ValueTrigger Type="Upper Threshold" Value="3"/>`

`</DataPoint>`

`</DataPoints>`

`</PublishedTopic>`

`</PublishedTopics>`

`<SubscribedTopics>`

`<SubscribedTopic>`

`<General Name="Subscribed Topic_3" Author="Jane Doe" Comment="My subscribed topic"/>`

`<QoS>2</QoS>`

`<DataPoints>`

`<DataPoint>`

`<General Name="Subscribed_datapoint_1">`

`<Tag>"Data_block_2"."In_Storage"</Tag>`

`</General>`

`</DataPoint>`

`<DataPoint>`

`<General Name="Subscribed_datapoint_2">`

`<Tag>"Data_block_2"."Required"</Tag>`

`</General>`

`</DataPoint>`

`</DataPoints>`

`</SubscribedTopic>`

`</SubscribedTopics>`

`</CloudConnectData>`

### Topic editor

This section contains information on the following topics:

- [Publisher and subscriber](#publisher-and-subscriber)
- [Configuring the data points](#configuring-the-data-points)
- [Data types](#data-types)
- [Trigger](#trigger)
- [Value trigger](#value-trigger)
- [Value ranges of the data types for value triggers](#value-ranges-of-the-data-types-for-value-triggers)

#### Publisher and subscriber

##### The Topic editor for the publisher and the subscriber

You open the Topic editor via the project tree:

Station > Local modules > CP 1545-1 > Cloud connection >  
     "Published topics" / "Subscribed topics" or "Published groups"

**Data point configuration in the topic editor**

In the topic editor, you configure the individual data points of the publisher or subscriber.

You can see the following differences for the publisher and the subscriber when you select a data point:

- **Publisher**

  A data point has the following parameter groups:

  - General
  - Trigger (Value trigger)
- **Subscriber**

  A data point has only one parameter group:

  - General

**Properties dialog of the topic/group**

You configure the following properties of the topics/groups in the respective properties dialog:

- General properties (name etc.)
- Quality of Service (QoS)
- Trigger (Time trigger)

You open the properties dialog via the payload editor or via the "Properties" shortcut menu of the topics/groups in the project tree. For details, see [Properties dialog of the topics](#properties-dialog-of-the-topics).

##### The Payload editor for the publisher

You can only set the payload format for the publisher. You will find details in the section [Payload configuration](#payload-configuration).

As a subscriber, the CP only supports the JSON format.

You open the Payload editor for the publisher via the second tab next to the topic editor.

##### Consistency between publisher and subscriber

If a CP as a subscriber receives data from a publisher at runtime, the subscriber checks the following parameters supplied by the publisher in the payload for each value received:

- Topic name
- Data point name
- Data type

Result of the consistency check:

- Parameters identical

  If the three mentioned parameters of the publisher are identical with the parameters configured in the subscriber, then the subscriber writes the received data to the data block of its CPU.
- Parameters not identical

  If the three mentioned parameters of the publisher are not identical with the parameters configured in the subscriber, the subscriber discards the data.

The station name of a publisher is not evaluated by the CP as a subscriber.

#### Configuring the data points

##### Inserting data points in a topic / group

After creating a topic or group, click in the first free row of the table (Add tag).

Select the desired DB tag of the CPU via the object selection dialog. For the DB tags, see [Operand areas and tags](CloudConnect.md#operand-areas-and-tags).

The DB tag is transferred to the table as a data point, the properties and parameters are displayed below.

The table lists all configurable data points.

You can use the "Properties" button above the table to open the properties dialog of the topic or group. For information on the configuration, see [Properties dialog of the topics](#properties-dialog-of-the-topics).

##### Configuring data points

When configuring the data points, note the information under [Permitted Characters](Additional%20information.md#permitted-characters).

- **Tag**

  Configured name of the DB tag
- **Data type**

  Configured data type of the data point

  For the supported data types, see [Data types](#data-types).
- **Attribute**

  ⇒ Validity: MindConnect IoT Extension

  The attribute is applied to the payload as <ADDITIONAL_ATTRIBUTE>; see section [Payload configuration](#payload-configuration).

  With a connection to IoT Extension, the attribute is interpreted as a label of the physical units of the respective data point. The standard units are:

  - C = Temperature in degrees Celsius
  - P = Pressure in bars
  - mm = Length in millimeters
  - km/h = Speed in km/h
  - m/s2 = Acceleration in m/s<sup>2</sup>
  - % = Size in percent
  - %RH = Relative humidity in percent
  - A = Current in amperes
  - V = Voltage in volts
  - W = Power in watts
  - kWh = Energy in kilowatt hours
  - VAh = Apparent energy in volt ampere hours
  - dBm = Transmit power in decibel-milliwatts (logarithmic ratio)
  - lux = Illuminance in lux (lm/m<sup>2</sup>)

  Other compound units of the SI system can also be specified, for example:

  m/h, m/s, m, km, mW, kW, mWh, mA, VArh
- **Trigger**

  For information on the configuration, see [Trigger](#trigger).

#### Data types

##### Supported data types

The table lists the configurable data types.

If needed, check whether the data types are supported by your broker.

<DATAPOINT_TYPE> indicates the data type during publication. For the publication of the useful data and the tag, <DATAPOINT_TYPE> see section [Payload configuration](#payload-configuration).

Data types available for Cloud access

| S7 data types (bits) | <DATAPOINT_TYPE> | Remarks |
| --- | --- | --- |
| BOOL (1) | BOOL | Values transferred: 0, 1 |
| BYTE (8) | UINT8 |  |
| CHAR (8) | CHAR | No WCHAR |
| USINT (8) | UINT8 |  |
| INT (16) | INT16 |  |
| UINT (16) | UINT16 |  |
| WORD (16) | UINT16 |  |
| REAL (32) | SINGLE_FLOAT |  |
| DWORD (32) | UINT32 |  |
| DINT (32) | INT32 |  |
| UDINT (32) | UINT32 |  |
| LREAL (64) | DOUBLE_FLOAT |  |
| STRING (2..256 Char) ***** | S7_STRING ***** | No WSTRING |
| DATE_AND_TIME (64) ***** | S7_DT ***** |  |
| DTL (96) ***** | S7_DTL ***** |  |
| ***** No support for Siemens MindSphere |  |  |

#### Trigger

##### Trigger

Triggers are used to define the conditions for the transfer of the stored values of a topic/group to the cloud or to the broker.

The following trigger types are available:

- **Value trigger**

  A value trigger can be configured individually for each data point.

  The following trigger types can be configured:

  - Deviation: Transfer in case of deviation from the last stored value
  - Threshold LOW: Transfer when the value falls below a configurable threshold
  - Threshold HIGH: Transfer when a configurable threshold value is exceeded
  - Range within: Transfer when the value enters a configurable value range
  - Range outside: Transfer when the value leaves a configurable value range

  For details, see [Value trigger](#value-trigger).
- **Time trigger**

  A time trigger can be configured in the properties dialog of the topic or group. It is valid for all data points of the topic or group.

  The following trigger types can be configured:

  - Cyclic

    Cyclic transmission
  - Time

    Once daily / Once weekly / Once monthly

  For details, see [Time trigger](#time-trigger).

  > **Note**
  >
  > **Time trigger with migration of the CP V1.0**
  >
  > Projects from predecessor versions that contain the CP with firmware version 1.0 demonstrate the following behavior for the time trigger with migration of the CP to firmware version 1.1:
  >
  > Time triggers of the data points configured in predecessor versions are transferred to the topic or group with CP V1.1. If multiple time triggers were configured in a topic or group, the first found time trigger is applied.

##### Triggering the transfer

As soon as the trigger condition of a trigger type is fulfilled, the transfer of all data points of this topic or group is triggered.

> **Note**
>
> **Volume of the transferred data**
>
> Note that different value triggers and an additional time trigger each trigger the transfer of the entire topic or group.

#### Value trigger

##### Variants of the value trigger

The following variants of the value trigger can be configured:

- Deviation

  The value is transferred as soon as it deviates by the configured amount from the last value stored in the CPU.

  Note the value range of the data type of the respective data point.
- Threshold LOW

  The value is transferred as soon as it drops below the configured value.
- Threshold HIGH

  The value is transferred as soon as it exceeds the configured value.
- Range within

  The value is transferred as soon as it is inside the configured range.
- Range outside

  The value is transferred as soon as it is outside the configured range.

The value ranges of the value triggers depend on the data type of the data point.

##### Duration of transfer (value trigger)

For all value triggers, note that the data of a topic or a group is transferred as long as the trigger condition is met. This has effects on the transferred data volume.

> **Note**
>
> **Transfer in "Scan cycle of variables"**
>
> When the trigger condition of a value trigger is met, the data is transferred to the broker with each scan cycle of variables.

##### Data type dependent support of the value trigger

Not every data type supports the value trigger. The table shows the support of the value trigger for each configurable data type.

- Marked with "**x**": Value trigger is supported.
- Marked with "**‑**": Value trigger is not supported.

Support of the value trigger by data types

| S7 data type (bits) | Supported value trigger |
| --- | --- |
| BOOL (1) | **x** ***** |
| BYTE (8) | **x** |
| CHAR (8) | **x** |
| USINT (8) | **x** |
| INT (16) | **x** |
| UINT (16) | **x** |
| WORD (16) | **x** |
| REAL (32) | **x** |
| DWORD (32) | **x** |
| DINT (32) | **x** |
| UDINT (32) | **x** |
| LREAL (64) | **x** |
| STRING (2..256 Char) | **x** ****** |
| DATE_AND_TIME (64) | **‑** |
| DTL (96) | **‑** |
| ***** Deviation only (value 0)   ****** Only deviation (value 0); Trigger when character or number of characters changes. |  |

#### Value ranges of the data types for value triggers

##### Value ranges of the data types

Threshold values are configured for the trigger types "Deviation", "Threshold LOW", "Threshold HIGH", "Range within" and "Range outside".

The data types that are suitable for threshold triggers have the following value ranges:

- Bool: 0 / 1
- Byte: 0...255 / -128...+127
- Char: 0...255
- USInt: 0...255
- Int: -32768...+32767
- UInt: 0...65535
- Word: -32768...+32767 / 0...65535
- DInt: -2147483648...+2147483647
- UDInt: 0...4294967295
- DWord: -2147483647...+2147483647 / 0...4294967295
- Real: +1.175495e-38...+3.402823e+38
- LReal: +12.2250738585072014e-308...+1.7976931348623157e+308

##### Value ranges of S7 analog input modules

With a positive integer (Int: 0...32767), 270 corresponds to about 1% of the raw value of an S7 analog input module (27648 = 100%).

### User data editor

This section contains information on the following topics:

- [Payload configuration](#payload-configuration)
- [Payload formats](#payload-formats)
- [QualityCode](#qualitycode)

#### Payload configuration

##### Payload formats

The CP uses UTF‑8 character encoding for formatting the payload.

Different cloud systems use different formats when transferring payload. Depending on the connected cloud system ("Cloud operator" parameter) the CP may output the payload in different formats. The different formats are available as selectable templates.

As a publisher, the CP uses the code selected or manually adapted in a topic or group in all topics or groups.

The following templates or options are available:

- Siemens MindSphere - MindConnect IoT Extension

  Only possible format for Siemens MindSphere
- JSON

  Possible format for "Other cloud" cloud provider

  Cloud services that expect JSON format for processing topics.

  The syntax corresponds to ECMA-404 and ISO/IEC 21778:2017.
- XML

  Possible format for "Other cloud" cloud provider

  Format for cloud services that expect the XML format for processing topics.
- Free format

  Possible format for "Other cloud" cloud provider

  If this option is selected, the text box for the format is cleared and can be edited. You can now edit an individual syntax for the payload format.

  Formats for cloud services which expect special formats.

  > **Note**
  >
  > **No processing of customized formats by the CP as a subscriber**
  >
  > Note that the CP as a subscriber cannot process adapted or modified formats.

See [Configuration: Overview and rules](CloudConnect.md#configuration-overview-and-rules) for the maximum amount of the payload.

See [Payload formats](#payload-formats) for the syntax of the formats.

##### Configuration options

The elements in the Payload editor have the following functions:

- "Format" drop-down list

  You select the format you want to use for the payload transfer here.
- "Customize"

  When the option is selected, the text box becomes editable and you can individually adapt the previously selected standard format. Conceivable adaptations could be, for example:

  - Deleting code components that are not required
  - Inserting fixed texts

  You can change the code in the text box below the check box. Always adhere to the specified syntax.

  > **Note**
  >
  > **Syntax consistency**
  >
  > Ensure the consistency of a manually changed code.
  >
  > Errors in the payload format can make the payload unreadable.

  For the two formats JSON and XML, you can check your changes by clicking the "Validate" button.

  If the code meets your requirements, save it.
- "Validate" button

  The function only considers the JSON and XML formats. The check is only performed when the "Customize" option is enabled.

  When you click the button, the format you have customized (JSON or XML) is checked for a number of syntax errors and a corresponding message is output.

  Note that it is not possible to check for all possible syntax and format errors. Data point names or attribute names are not checked.

#### Payload formats

##### Payload format "MindConnect IoT Extension"

`200, "{{`
`Pub_data-point`
`_1.NAME}}", "{{GROUP}}", "{{`
`Pub_data-point`
`_1.VALUE}}", "{{`
`Pub_data-point`
`_1.ADDITIONAL_ATTRIBUTE}}", "{{PUBLISH_TIMESTAMP}}"`

##### Payload format "JSON"

`{  
    "Timestamp" : "{{PUBLISH_TIMESTAMP}}",  
    "DataItems" : [  
    {  
        "Variable" : "{{`
`Pub_data-point`
`_1.NAME}}",  
        "Type" : "{{`
`Pub_data-point`
`_1.TYPE}}",  
        "Value" : "{{`
`Pub_data-point`
`_1.VALUE}}",  
        "QualityCode" : "{{`
`Pub_data-point`
`_1.QUALITY_CODE}}"  
    },  
    {  
        "Variable" : "{{`
`Pub_data-point`
`_2.NAME}}",  
        "Type" : "{{`
`Pub_data-point`
`_2.TYPE}}",  
        "Value" : "{{`
`Pub_data-point`
`_2.VALUE}}",  
        "QualityCode" : "{{`
`Pub_data-point`
`_2.QUALITY_CODE}}"  
    }]  
}`

##### Payload format "XML"

`<?xml version="1.0" encoding="UTF-8"?>`
  
`<root>`
  
`<Timestamp>{{PUBLISH_TIMESTAMP}}</Timestamp>`
  
`<DataItems>`
  
`<DataItem>`
  
`<Variable>{{`
`Pub_data-point`
`_1.NAME}}</Variable>`
  
`<Type>{{`
`Pub_data-point`
`_1.TYPE}}</Type>`
  
`<Value>{{`
`Pub_data-point`
`_1.VALUE}}</Value>`
  
`<QualityCode>{{`
`Pub_data-point`
`_1.QUALITY_CODE}}</QualityCode>`
  
`</DataItem>`
  
`<DataItem>`
  
`<Variable>{{`
`Pub_data-point`
`_2.NAME}}</Variable>`
  
`<Type>{{`
`Pub_data-point`
`_2.TYPE}}</Type>`
  
`<Value>{{`
`Pub_data-point`
`_2.VALUE}}</Value>`
  
`<QualityCode>{{`
`Pub_data-point`
`_2.QUALITY_CODE}}</QualityCode>`
  
`</DataItem>`
  
`</DataItems>`
  
`</root>`

##### Code components

The code for formatting the payload consists of the components listed below.

The following description of the individual code components is structured as follows:

- **Code component**

  `Syntax`

  Meaning

  - Example (not for all components)

##### Code components: Syntax and meaning

- **200**

  `200`

  Function code (MindConnect IoT Extension)
- **Time stamp**

  `{{PUBLISH_TIMESTAMP}}`

  Meaning: Time of the publication

  - Example:

    Syntax: "`{{PUBLISH_TIMESTAMP}}`"  
    Results in string: "`2018-08-20T13:58:16.192313634+00:00`"
- **Data point / Variable**

  `{{`
  `Pub_data_point`
  `_n.NAME}}`

  Name of the data point
- **Group**

  `{{GROUP}}`

  Group name (MindConnect IoT Extension)
- **Value**

  `{{`
  `Pub_data-point`
  `_n.VALUE}}`

  Value of the data point
- **Attribute**

  `{{`
  `Pub_data-point`
  `_n.ADDITIONAL_ATTRIBUTE}}`

  Attribute (MindConnect IoT Extension)
- **Data type**

  `{{`
  `Pub_data-point`
  `_n.TYPE}}`

  Data type of the data point output by the device

  For the output of the data types, see section [Operand areas and tags](CloudConnect.md#operand-areas-and-tags).
- **QualityCode**

  `{{`
  `Pub_data-point`
  `_n.QUALITY_CODE}}`

  Quality status of the value

  For the meaning, see [QualityCode](#qualitycode).

##### Sequences not permitted in the payload content

The following sequences are not permitted in the payload content:

- {{#
- {{^
- {{/
- {{>
- {{&
- {{{

##### Example of transferred payload (JSON)

Below you will find an example of the transferred payload of a topic.

The topic contains three variables of an S7 station for the data points "DP1", "DP2" and "DP3".

The value of the "DataItems" key is an array with the objects of the three variables.

{

    "Timestamp" : "{{PUBLISH_TIMESTAMP}}",

    "DataItems" : [

    {

        "Variable" : "{{DP1.NAME}}",

        "Type" : "{{DP1.TYPE}}",

        "Value" : "{{DP1.VALUE}}",

        "QualityCode" : "{{DP1.QUALITY_CODE}}"

    },

    {

        "Variable" : "{{DP2.NAME}}",

        "Type" : "{{DP2.TYPE}}",

        "Value" : "{{DP2.VALUE}}",

        "QualityCode" : "{{DP2.QUALITY_CODE}}"

    },

    {

        "Variable" : "{{DP3.NAME}}",

        "Type" : "{{DP3.TYPE}}",

        "Value" : "{{DP3.VALUE}}",

        "QualityCode" : "{{DP3.QUALITY_CODE}}"

    }]

}

##### Escape sequences

Escape sequences which adapt the code according to the protocol used can be used to convert certain special characters.

Special characters can occur within the following name components, for example:

- Station name
- Topic name
- Group name

The following escape sequences are supported by the CP:

- JSON PubSub

  Standard JSON escape sequences

  For the escape sequences used, see [JSON escape sequences](Additional%20information.md#json-escape-sequences).
- XML

  Standard XML escape sequences
- CSV

  Standard CSV escape sequences

The publisher converts the respective special characters into escape sequences.

For the subscriber, the escape sequences are converted into the reverse direction.

#### QualityCode

##### Transmission and "QualityCode"

The "QualityCode" quality status of a data point is also transferred with the payload. The status indicates the validity of the value.

The status is set by the CP as a publisher and has the following value range:

- GOOD

  The value is valid.
- BAD

  The value of the tag is not valid or not current. Possible causes:

  - CPU in STOP
  - Value not current
  - Tag not configured

The value of the status has the following effect on the transmission:

- Publisher → Cloud

  The publication of CP messages as a publisher is independent of the value of the status.
- Cloud → Subscriber

  Reception of messages by the CP as a subscriber is independent of the value of the status.

  However, when a message with "BAD" status is received, the value is not written to the DB tag of the CPU by the subscriber.

## Properties dialog of the topics

This section contains information on the following topics:

- [Opening the properties dialog](#opening-the-properties-dialog)
- [Time trigger](#time-trigger)
- [Quality of Service (QoS)](#quality-of-service-qos)

### Opening the properties dialog

When you open the CP in the navigation area below the local modules, the properties dialog may be opened in two ways:

- Via the shortcut menu (right-click) of the topics / groups
- When the Topic editor is open, use the "Properties" button above the data point table

### Time trigger

#### Variants of the time trigger

The following variants of the time trigger can be configured:

- Cyclic

  The value is transmitted cyclically, configurable in milliseconds.
- Time
- The following intervals can be set:

  - Once daily

    The value is transferred once a day at the configured time.
  - Once weekly

    The value is transferred once a week at the configured time.
  - Once monthly

    The value is transferred once a month at the configured time.

    Note:  
    If a month has fewer days than specified in the configuration, the value is not transferred.

### Quality of Service (QoS)

#### Quality of Service (QoS)

- **Required Quality of Service (QoS)**

  This is where you define the desired transmission behavior (Quality of Service) of this topic.

  The configured value is transferred to the communication partner as requirement. If a broker does not meet the required QoS level, in many cases it selects the level that comes closest to the one required. Inform yourself about the behavior of your broker as it relates to the QoS.

  Range of values:

  - QoS 0

    Transfer no more than once

    The CP sends the topic once to the broker. The CP does not expect an acknowledgment.

    If the topic is not received by the broker, it is lost.
  - QoS 1

    Transfer at least once

    The CP sends the topic to the broker until it receives a PUBACK packet as acknowledgment from the broker.
  - QoS 2

    Transfer exactly once

    The CP sends the topic and waits until it receives the two-step acknowledgment from the broker as specified.

    This version represents the highest level of quality, but it is also associated with the highest administrative burden for the client as well as the server.

  Default setting: 0
