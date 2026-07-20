---
title: "CloudConnect"
package: CC7enUS
topics: 23
source: Siemens TIA Portal Information System (offline help, en-US)
---


# CloudConnect

This section contains information on the following topics:

- [CP configuration](#cp-configuration)
- [Parameters of the topics / groups](#parameters-of-the-topics-groups)
- [Properties dialog of the topics](#properties-dialog-of-the-topics)

## CP configuration

This section contains information on the following topics:

- [Cloud communication](#cloud-communication)
- [Configuration: Overview and rules](#configuration-overview-and-rules)
- ["CloudConnect" parameter group](#cloudconnect-parameter-group)
- [Operand areas and tags](#operand-areas-and-tags)

### Cloud communication

#### Protocols for the cloud connection

The CP supports the following protocols for communication with a cloud broker or cloud server:

- MQTT

  According to OASIS standard version 3.1.1

#### Supported cloud systems

The CP supports the connection to cloud systems that support broker functionality with the MQTT protocol.

The configuration of cloud access ("Cloud provider") is adapted to communication with the following cloud systems and services:

- Siemens MindSphere ‑ MindConnect IoT Extension

  The CP is the publisher.
- Other Cloud

  Profile for another cloud system, for example:

  - AWS (Amazon) ‑ IoT Core
  - Azure (Microsoft) ‑ IoT Hub
  - IBM Cloud (IBM) ‑ Watson IoT Platform

  The CP can be the publisher and subscriber.

#### Communication partner

- Publisher

  A publisher publishes data to a cloud broker.

  Together with the CP as a subscriber (only when communicating via "Other cloud"), the following devices can act as a publishers:

  - CP 1545‑1
  - Third-party device

    Third-party devices, the configuration and payload format of the messages of which are compatible with the CP.
- Subscriber

  A subscriber logs on to the cloud broker and subscribes to data of the publisher.

  Together with the CP as a publisher, the following devices can act as a subscribers:

  - CP 1545‑1

    (only for communication via "Other cloud")
  - Third-party device

    Third-party devices, the configuration and payload format of the messages of which are compatible with the CP.

For compatibility of CP and third-party device, see:

- [Configuration: Overview and rules](#configuration-overview-and-rules)
- [Publisher and subscriber](#publisher-and-subscriber)
- [Payload configuration](#payload-configuration)

#### Secure communication certificate ‑

If you want to use secured cloud communication, select "MQTT over TLS" option under "Security > CloudConnect > Broker configuration".

In this parameter group you specify the broker certificate to be used, which you have previously imported in the global security settings and assigned to the CP.

If a partner (Publisher / Subscriber) that communicates with the CP via the cloud requires certificates for secure communication, use the certificate of the partner at the CP in the "Client certificate" drop-down list.

For information on the configuration, see ["CloudConnect" parameter group](#cloudconnect-parameter-group).

### Configuration: Overview and rules

#### Configuration of cloud access

1. To allow the cloud application to access the process image, create the required data blocks and DB variables in the local CPU.

   The configured data points of the topics/groups access DB variables of the CPU, see section [Operand areas and tags](#operand-areas-and-tags).
2. First, configure the parameter groups for the CP under "Security > Cloud access" in the Inspector window.

   To do this, create at least one user with the role "NET Administrator" in the Global Security settings.
3. Expand the project tree:

   Station > Local modules > CP 1545-1 > Cloud connection >  
        "Published topics" / "Subscribed topics" or  
        "Published groups"

   - Click on "Add Topic" or "Add Group".

     The Topic editor is opened and a new topic or group is created.
   - Insert data points into the topics or groups and configure them.

     Read the note on topic name, data point name and data type in the following section "Configuration rules and recommendations".
   - Open the Payload editor and define the format of the payload to be published.

   For information on the configuration, see [Configuring topics or groups](#configuring-topics-or-groups).
4. Select the topic / group and open the properties dialog via the "Properties" shortcut menu command or from the opened Topic editor via the "Properties" button.

   - Configure the name and optionally "Author" and "Comment".

     Read the information on the topic name in the following section.
   - If required, configure a time trigger for the topic or group.
   - Configure the "Quality of Service (QoS)".
   - For information on the configuration, see [Quality of Service (QoS)](#quality-of-service-qos).

#### Configuration rules and recommendations

**Configuration rules**

Observe the following rules for configuration:

- **Data blocks**

  - Size

    The number of variables in the DB is not limited.

    When you create arrays, only elements/tags of arrays with a maximum size of < 10000 elements can be published.
- **Topics / Groups**

  - Quantity

    Maximum number per CP: 500
  - Name

    Within a cloud application, the name of a topic must be unique.

    This applies to all participating publishers and subscribers.

    Also read the information in the [Permitted Characters](Additional%20information.md#permitted-characters) section.
  - Size

    The number of data points that a topic or group may contain is additionally limited by the total amount of the payload, see below.

  **Data points**

  - Quantity

    Maximum number of data points per CP: 500

    Maximum number of data points per topic / group: 500

    The number of data points that a topic or group may contain is additionally limited by the total amount of the payload, see below.
  - Name

    Within a topic, the name of a data point must be unique.

    Also read the information in the [Permitted Characters](Additional%20information.md#permitted-characters) section.

  **Payload amount**

  - Total amount of payload per topic / group

    Maximum 500000 Byte (corresponds to 500000 ASCII characters)
  - Total amount of payload per CP

    Maximum 500000 Byte (corresponds to 500000 ASCII characters)

  The amount of payload in the configuration depends on the payload format used. The size of the standard payload format with one data point and a data point name length of 21 ASCII characters is:

  - JSON : 258 Byte
  - XML : 363 Byte
  - MindSphere ‑ MindConnect IoT Extension : 160 Byte

  If you use longer names or additional code components (e.g. additional attributes), you need to add these.

  Example for the calculation of the payload amount:  
  With an amount of payload format of 500 ASCII characters for a data point, one data point per topic and 500 configured topics, the total amount of payload would be 250000 bytes.

  Note:  
  Because the variables are replaced by values when the messages are published, the amount of payload on the network can be different to the amount of payload in the configuration.

**Recommendations for configuration**

When transferring data in a hierarchically structured system, it is generally advisable to name the components according to this hierarchical structure.

Example for the name of a data point to be transferred:

  "Plant1_Unit1_Aggregate1_DB_1_Signal1"

Within a cloud application, individual publishers can publish data to multiple subscribers and individual subscribers can subscribe to data from multiple publishers. In general, but especially in this case, the following configuration is recommended:

- Data point name / DB number

  If you use the number of the data block (DB) that the data point accesses as part of the data point name, it is easier to assign the data point.
- Publisher

  - Create a separate DB for every subscriber for the CP as a publisher.
  - If a CP subscribes to data from multiple publishers, configure a different DB number for the respective DB intended for this subscriber with the different publishers.

    This prevents variables from different publishers from having an identical data point name if the data point names use the DB number as part of the name.
- Subscriber

  Create a separate DB for each publisher for the CP as a subscriber.

  Comment:  
  Subscribed data can only be written in DB tags. For further processing, the user program must access the DB tags. This prevents subscribed data from changing the process image directly during receiving.

The described recommendations are not mandatory but increase the clarity when assigning data and reduces the possibility of identical names.

### "CloudConnect" parameter group

#### Requirement

Activation of the security functions is a requirement for the configurability of cloud communication.

If you disable the security functions later, note that all previously configured cloud data will be lost, except for the data points and topics or groups.

#### General

- **Activate CloudConnect**

  Activates communication with a cloud system via the Ethernet interface of the CP.
- **Cloud provider**

  Select the desired cloud provider:

  - Siemens MindSphere ‑ MindConnect IoT Extension
  - Other cloud (profile for other cloud system)
- **Device name**

  Validity: MindConnect IoT Extension only

  For the meaning, see [Onboarding in MindConnect IoT Extension](Additional%20information.md#onboarding-in-mindconnect-iot-extension).

  Do not use quotation marks (") in the name; this results in the messages being sent twice. See also [Permitted Characters](Additional%20information.md#permitted-characters).
- **Scan cycle of variables**

  Cycle (ms) in which the DB variables of the CPU are queried.

  Range of values: 100..4294967295 ms

  > **Note**
  >
  > **Volume of transferred data**
  >
  > The value of the parameter has direct effects on the transferred data volume.
  >
  > When the trigger condition of a value trigger is met, the data is transferred to the broker with each scan cycle of variables. See also the note in section [Value trigger](#value-trigger).
  >
  > **Data loss**
  >
  > If you configure a very short scan cycle of variables together with a very large number of data points, it can occur with some brokers that not all of the published data can be read from the input buffer of the cloud server.
  >
  > Also note the function of the frame memory, see "Data buffering" section below.
- **Topics with time stamp**

  When this option is enabled, the current time stamp is added to each value at the time of each publication.

#### Broker configuration

- **MQTT**
   **/** 
  **MQTT via TLS**

  Alternatively, select one of the following protocol variants:

  - MQTT (unencrypted transmission)
  - MQTT via TLS (encrypted transmission)

    In this case, see the procedure for the required certificates, see "Client certificate" parameter below.
- **Minimum TLS version**

  Defines the TLS version used by the CP and the partner.
- **Broker certificate**

  The parameter is only active when you have enabled encrypted transmission "MQTT via TLS". In this case, you need a certificate from your cloud provider.

  Default setting: "Automatic". With the "Automatic" setting, a certificate from the trusted certificates is assigned.

  To manually assign the certificate, follow these steps.

  - Import the partner certificate:

    Global security settings > Certificate manager > Trusted certificates > right mouse click
  - Assign the certificate to the CP:

    Select certificate in the "Trusted certificates" list > right mouse click

    The certificate appears in the "Certificates of the partner devices" list on the CP in the parameter group "Security > Certificate manager".
  - Now select the imported certificate in the "Broker certificate" drop-down list.
- **Broker address**

  Address of the broker server (IPv4 address or host name)
- **Broker port**

  Port number of the broker server

  - Port 1883 is preset for unencrypted transmission (MQTT).
  - Port 8883 is preset for encrypted transmission (MQTT via TLS).
- **Client ID**

  Enter the client ID that was assigned by your service provider or that you defined.

  Max. 255 characters from the ASCII band (hex) 0x20 .. 0x7F
- **Client certificate**

  The CP certificate is only used for secure cloud communication (MQTT via TLS).

  When a partner (Cloud / Publisher / Subscriber) that communicates with the CP requires certificates for secure communication, use the certificate of the CP. The client certificate is automatically created by STEP 7, used for the CP, and displayed in the output field of the parameter.

  **Handling the certificates:**

  The corresponding certificates must be exchanged for secure communication:

  - Exporting the certificate of the CP or the STEP 7 project

    For the CP certificate to be used, the CA certificate of the TIA project must be imported to the cloud server as trusted certificate. To do so, export the CA certificate with the matching hash algorithm from the global security settings:  
    "Security settings > Security features > Certificate manager > Certificate Authority (CA)" > Certificate selection > Shortcut menu "Export".

    Then transfer the certificate to the cloud server.
  - Importing the certificate of the communication partner

    You must import the respective certificate from the communication partner as a trusted certificate into your STEP 7 project. To do this, follow these steps:

    Save the certificate in the file system of the STEP 7 project computer. Import the certificate in the global security settings:  
    "Security settings > Security features > Certificate manager > Trusted certificates and root certification authorities" > Selection of an empty table row > Shortcut menu "Import".

    The procedure depends on the cloud being used.

    For some clouds, such as AWS, for example, you must assign this certificate to the CP as device certificate. To do this, follow these steps:
  - Assigning the cloud certificate to the CP (depending on the cloud)

    Requirement: You have imported the certificate of the cloud in the global security settings as described above.

    Select the certificate in the "Trusted certificates and root certification authorities" list, click on the shortcut menu "Assign" and select the CP in the next dialog.

    The certificate is now displayed in the local Certificate manager of the CP in the "Certificates of the partner devices" list.
- **Clean session**

  When this option is enabled, the session information is deleted when the connection is terminated.

  When the option is disabled, the session information is retained when the connection is terminated.

  > **Note**
  >
  > **Recommendation: Enable "Clean session"**
  >
  > It is recommended that you enable the parameter.
  >
  > If QoS is configured with a value > 0 and "Clean session" is disabled, unclear situations can arise in the event of connection aborts with respect to pending acknowledgments.

#### Broker monitoring

- **Keepalive interval**

  Monitoring time of the connection with the broker

  If no further data is pending for transmission within the configured monitoring time after the data is sent or if the CP does not receive a packet from the broker, the CP sends a keep-alive packet (PINGREQ) to the broker which it must acknowledge (PINGRESP).

  Note the effect of the parameter on the behavior in the event of disconnections, see manual.

#### Broker authentication

- **Enable authentication**

  When this option is enabled, the connection to the broker is established with authentication. If possible, use TLS to transmit the user name and password.

  When the option is disabled, the connection is established anonymously.
- **User name**

  Enter the user name that was assigned by your service provider or that you defined.
- **Password**

  Enter the password that was assigned by your service provider or that you defined.

#### Data buffering

The CP saves accumulating messages that have not yet been published in its frame memory. This has a capacity of 3500 messages.

The frame memory operates chronologically; in other words, the oldest data is sent first (FIFO principle). When the maximum capacity is exceeded, the oldest messages are overwritten.

### Operand areas and tags

#### Symbolic addressing of the process data of the CPU

The process data provided by the CP to the CloudConnect services are addressed via tags in data blocks of the CPU.

To access the process data that is to be transferred via the cloud, you must create at least one DB:

- Data block

  - Create the block as a global DB.
  - Enable the "DB accessible from OPC UA" attribute in the properties dialog of the DB.

#### Configuring the DB tags

When configuring the DB tags, note the following:

- Enable the option "Accessible from HMI/OPC UA".
- Enable the option "Writable from HMI/OPC UA".

  Required for write access

You can find the data types that can be used for the cloud connection in the section [Data types](#data-types).

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
- Other cloud

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

#### Exporting, importing and editing CloudConnect data in XML format

You can use these functions to configure CloudConnect data outside of STEP 7 or to copy existing topics or groups of a configured CP to other, not yet configured CPs.

**Export CloudConnect Data**

Open the export dialog in the following way:

1. Expand the project tree:

   Station > Local modules > CP 1545-1 > Cloud connection
2. In the shortcut menu of the "Cloud connection" entry, click on "Export CloudConnect Data".

   The window for exporting the XML file opens.

**Editing an XML file**

You can edit or expand an exported XML file with configuration data in a suitable editor.

Note the following points:

- When you omit an optional element/attribute, it will receive the respective default value on import into the STEP 7 project.
- If the XML file contains invalid inputs, STEP 7 outputs an error message and aborts the import.

**Import CloudConnect Data**

Before importing CloudConnect data, check that the suitable cloud provider is selected in the device configuration:

- For topics: Other cloud
- For groups: Siemens MindSphere - MindConnect IoT Extension

The following prerequisite must be met for the complete import of the CloudConnect data of an existing CP (source device) into another CP (target device):

- The corresponding tags must exist in the CPU of the target device.
- The tags in the DB of the target device CPU must have the same name as those of the source device CPU.

  If the tag name contained in the XML file is not found during the import, the respective data point will remain empty after the import.

  To still be able to use the data point, you must select a tag for the data point in the DB of the CPU.

The easiest way to achieve the same DBs in the source and target device is as follows:

1. Copy the DB of the CPU of the source device from which you have exported the CloudConnect data.
2. Paste the copied DB into the CPU of the target device.

The import procedure is equivalent to the export procedure: Shortcut menu of "Cloud connection" > "Import CloudConnect Data"

If there is already CloudConnect data in the target device, you are asked whether you want the existing data to be retained or overwritten.

#### XML syntax and permitted values

| Syntax | Element/attribute name | Permitted data types and values | Meaning/Comment |
| --- | --- | --- | --- |
| `<PublishedGroup>` or `<PublishedTopic>` |  |  |  |
| `<General>` | - Name - Author - Comment | - String - String - String | - Required - Optional - Optional |
| `<QoS>` |  | Integer; 0-2 | Optional |
| `<TimeTrigger> <Cyclic>`     or     `<TimeTrigger> <Date>` | - CycleTime - Frequency - TimeOfTheDay - Weekday - DayOfTheMonth | - Integer; 10-4294967295, ms - String; Daily, Weekly, Monthly - Integer; 0-1439, minutes (00:00 - 23:59 in minutes) - String; Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday - Integer; 1-31 | - Required for element `TimeTrigger > Cyclic` Required for element `TimeTrigger > Date` - Optional - Optional - Optional |
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

##### Requirement: Created DB tags

Appropriate DB tags must first be created on the CPU to allow configuration of the data points.

All tags intended to be used for data point configuration must have the attribute "Reachable from HMI/OPC UA/Web API".

For writable tags, the "Writable from HMI/OPC UA/Web API" attribute also needs to be enabled.

##### Inserting data points in a topic / group

1. Open the desired topics or the group (Project tree > Station > Local modules > CP > "Cloud connection").

   The topic editor opens.
2. Click in the first free row of the table (Add tag).
3. Select the desired DB tag of the CPU via the object selection dialog. For the DB tags, see [Operand areas and tags](#operand-areas-and-tags).

   The DB tag is transferred to the table as a data point, the properties and parameters are displayed below.

The table lists all configurable data points.

You can use the "Properties" button above the table to open the properties dialog of the topic or group. For information on the configuration, see [Properties dialog of the topics](#properties-dialog-of-the-topics).

**Alternative method for creating specific data points**

1. Click (multiple times) in the first free row of the table (Add tag).
2. With the keyboard, type in part of the name of a tag.

   All tags that contain the entered string are shown.
3. Select the required tag with a mouse click.

![Inserting data points in a topic / group](images/154111536395_DV_resource.Stream@PNG-en-US.png)

**Simplified creation of multiple data points**

You can create multiple data points in one step in the following way:

1. In the project tree, expand the station, the CP under the local modules and the directory of the topics or groups.
2. Open the desired topic or group.

   The topic editor appears.
3. Expand the "Program blocks" folder in the project tree.
4. Select the relevant DB for the assignment of the DB tags.

   The content is displayed in the "Detail view" window under the project tree.
5. In the detail view, select all tags that you want to use for the assignment to data points.

   (Multiple selection with <Shift> or <Ctrl>)
6. Drag-and-drop the selected tags into the table of the topic editor.

![Inserting data points in a topic / group](images/154106529931_DV_resource.Stream@PNG-en-US.png)

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
| BOOL (1) | **x *** |
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
| STRING (2..256 Char) | **x **** |
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

See [Configuration: Overview and rules](#configuration-overview-and-rules) for the maximum amount of the payload.

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

  For the output of the data types, see section [Operand areas and tags](#operand-areas-and-tags).
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
