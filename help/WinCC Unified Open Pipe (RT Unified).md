---
title: "WinCC Unified Open Pipe (RT Unified)"
package: WinCCRTUOpPenUS
topics: 35
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Unified Open Pipe (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [Safety-related settings (RT Unified)](#safety-related-settings-rt-unified)
- [Behavior of the browse commands (RT Unified)](#behavior-of-the-browse-commands-rt-unified)
- [Using basic syntax (RT Unified)](#using-basic-syntax-rt-unified)
- [Using expert syntax (RT Unified)](#using-expert-syntax-rt-unified)

## Introduction (RT Unified)

### Welcome to WinCC Unified Open Pipe

WinCC Unified Open Pipe is an Openness concept based on pipe technology to connect a customer application to WinCC Unified RT.

Compared to Openness RT (ODK), WinCC Unified Open Pipe offers a limited number of functions. However, the connection code can be written in any programming language that supports pipe technology. Even batch access to the pipe is possible.

The main aim of WinCC Unified Open Pipe is to make it possible for you to connect an existing application to WinCC Unified RT with little workload and independent of the programming language. The available commands let you communicate with WinCC Unified RT using tags and alarms.

### Pipe technology

The pipe is a data stream with buffer between two processes that works according to the FIFO principle (First In First Out). One process is provided by WinCC Unified RT (OpennessManager). It creates the pipe and processes the requests of the customer application. The second process is the customer application. It connects to the pipe by using its name, sends requests and receives responses.

![Pipe technology](images/122887532939_DV_resource.Stream@PNG-de-DE.png)

Name of the pipe:

- Under Windows: "\\.\pipe\HmiRuntime"
- Under Linux: "/tmp/HmiRuntime"

As soon as the pipe is open, single-line commands can be sent; they must end in a line break ("\n" or "\r\n"). Responses are returned using the same pipe instance.

### Basic syntax and expert syntax

Two types of syntax are available for WinCC Unified Open Pipe:

- Basic syntax

  You use the basic syntax when you are working with basic batch files (e.g. in a CMD.exe or batch).
- Expert syntax

  You use the expert syntax when you are working with scripts or programming languages that have a JSON parser, e.g. Python, Node.js or Powershell.

### Samples

You will find the following file on the installation medium: "Support\Openness\Siemens.Unified.Openness_SDK_<version number>.zip"

Extract the file locally to any directory on your computer. You will then find examples of the use of WinCC Unified Open Pipe in the subfolder "OpenPipe\Samples".

## Safety-related settings (RT Unified)

### Pipe access

- The use of Open Pipe is limited to local communication between the Open Pipe application and Runtime.
- To access the pipe, the user of the client script must belong to the following user group:

  - Under Windows: "SIMATIC HMI"
  - Under Linux: "industrial"

## Behavior of the browse commands (RT Unified)

### Browse behavior

WinCC Unified Open Pipe provides several Browse commands in the simple syntax and in the expert syntax. The following behavior is common to all commands:

- Initial request

  In an initial request, you define the request using optional parameters.
- Page size

  To get the result faster, you can use a parameter to specify a page size in the initial request. If the result exceeds the specified page size, the response is distributed over several pages.

  Without this parameter the configured page size is used. You can read the configured page size via the commands "ReadConfig" and set it via "WriteConfig".
- Next request

  You get the next results page via the following requests. Next requests only have the parameter "Next".
- A Browse command is complete when a Next request returns an empty response.
- A Browse command that has not yet reached the last page of results is canceled in the following cases:

  - When the configured time limit for inactivity is exceeded.

    You can read the time limit via the commands ReadConfig and set it via WriteConfig.
  - When a new browse request is started.

### Configurable settings

The following settings control the browse behavior:

| Setting | Default value | Value range | Description |
| --- | --- | --- | --- |
| DefaultPageSize | 1000 | 0 ... Uint32_Max | If a browse request was called without the PageSize parameter and the number of hits is greater than the value of DefaultPageSize, the response is distributed over several pages.  Value 0: No pagination |
| BrowseTimeOut | 300 s | 0 ... Uint32_Max | For requests with pagination, defines after how many seconds without activity the request is canceled. After that a Next request returns an error.   Value 0: No timeout |

With the command "ReadConfig" you request the settings, with the command "WriteConfig" you set them. Changes apply to the current pipe session.

## Using basic syntax (RT Unified)

This section contains information on the following topics:

- [Basics of basic syntax (RT Unified)](#basics-of-basic-syntax-rt-unified)
- [Commands (RT Unified)](#commands-rt-unified)
- [Reference (RT Unified)](#reference-rt-unified)

### Basics of basic syntax (RT Unified)

#### Characteristics

The basic syntax has the following characteristics:

- Simple text-based syntax without JSON parts.
- Only commands for individual objects, e.g. write access to a single tag.
- Object names may not include special characters or space characters.
- No cookies.

**Structure of a request**

`<Command> <Object> <Value>`

- `Command`: Command name, e.g. "WriteTagValue"
- `Object`: Name of the object for which the command is called, e.g. "Tag1"
- `Value`: Input value, e.g. "True"

**Structure of a response**

OnSuccess:

`Notify<Command> <Object> <Value1…ValueN>`

- `Command`: Command name, e.g. "ReadTagValue"
- `Object`: Name of the object for which the command was called, e.g. "Tag1"
- `Value1`…`ValueN`: For example, value and quality of the read tags

OnError:

`Error<Command> <Object> <Error text>`

- `Command`: Command name, e.g. "ReadTagValue"
- `Object`: Name of the object for which the command was called, e.g. "Tag1"
- `Error text`: Detailed error description

#### Overview of the commands of the simple syntax

| Command | OnSuccess | OnError | Description |
| --- | --- | --- | --- |
| `SubscribeTagValue <Tag>` | `NotifySubscribeTagValue <Tag> <Quality> <Value>` | `ErrorSubscribeTagValue <Tag> <Error text>`    `ErrorNotifyTagValue <Tag> <Error text>` | Subscribe tag for monitoring.   `Quality`={good, bad, uncertain} |
| `UnsubscribeTagValue <Tag>` | `NotifyUnsubscribeTagValue <Tag>` | `ErrorUnsubscribeTagValue <Tag> <Error text>` | Unsubscribe tag from monitoring. |
| `ReadTagValue <Tag>` | `NotifyReadTagValue <Tag> <Quality> <Value>` | `ErrorReadTagValue <Tag> <Error text>` | Reads the value of the tags from the system. |
| `WriteTagValue <Tag> <Value>` | `NotifyWriteTagValue <Tag>` | `ErrorWriteTagValue <Tag> <Error text>` | Writes the value to the tag. |
| `SetCharSet <Value>` | `NotifySetCharSet <Value>` | `ErrorSetCharSet <Value> <Error text>` | Changes to a different character coding. |
| `ReadConfig <Parameter>` | `NotifyReadConfig <Parameter> <Value>` | `ErrorReadConfig <Error text>` | Reads a setting configured for the general browse behavior. |
| `WriteConfig <Parameter>` | `NotifyWriteConfig <Parameter> <Value>` | `ErrorWriteConfig <Error text>` | Sets a setting for the general browse behavior. |
| `BrowseTags`:  - Initial request:    `BrowseTags <System>  <Page size> --filter <Filter>` - Next request:    `BrowseTags --next` | `NotifyBrowseTags <System>::<Tag> ... <System>::<Tag>` | `ErrorBrowseTags <Error text>` | Returns the names of the tags of the local system or all systems communicating via runtime collaboration. |
| `BrowseConfiguredAlarms`:  - Initial request:    `BrowseConfiguredAlarms <System>  <Page size> --filter <Filter>` - Next request:    `BrowseConfiguredAlarms --next` | `NotifyBrowseConfiguredAlarms <System>::<Alarm> ... <System>::<Alarm>` | `ErrorBrowseConfiguredAlarms <Error text>` | Returns the names of the configured alarms of the local system or all systems communicating via Runtime Collaboration. |
| `BrowseAlarmClasses <System>` | `NotifyBrowseAlarmClasses <System>::<Alarm class> ... <System>::<Alarm class>` | `ErrorBrowseConfiguredAlarms <Error text>` | Returns the alarm classes of the local system or all systems communicating via Runtime Collaboration. |

#### Errors and error texts

This help only provides a selection of possible error messages. The error texts can also differ from the texts in your projects.

### Commands (RT Unified)

This section contains information on the following topics:

- [SubscribeTagValue (RT Unified)](#subscribetagvalue-rt-unified)
- [UnsubscribeTagValue (RT Unified)](#unsubscribetagvalue-rt-unified)
- [ReadTagValue (RT Unified)](#readtagvalue-rt-unified)
- [WriteTagValue (RT Unified)](#writetagvalue-rt-unified)
- [SetCharSet (RT Unified)](#setcharset-rt-unified)
- [ReadConfig (RT Unified)](#readconfig-rt-unified)
- [WriteConfig (RT Unified)](#writeconfig-rt-unified)
- [BrowseTags (RT Unified)](#browsetags-rt-unified)
- [BrowseConfiguredAlarms (RT Unified)](#browseconfiguredalarms-rt-unified)
- [BrowseAlarmClasses (RT Unified)](#browsealarmclasses-rt-unified)

#### SubscribeTagValue (RT Unified)

##### Description

The command "SubscribeTagValue" subscribes the specified tag for monitoring.

**Error handling**

- When the tag value contains a line break (\n), the value cannot be signaled. An error is signaled.
- When the same tag is subscribed a second time for monitoring, an error is signaled.
- A global monitoring error is signaled with "ErrorSubscribeTagValue". Because no monitoring was set up, there is no need to unsubscribe the tag from monitoring.
- An error relating to the tag value is signaled with `"`ErrorNotifyTagValue". Monitoring is set up in this case, but the tag value cannot be signaled for various reasons. Unsubscribe the tag from monitoring when it is no longer needed.

**Request**

`SubscribeTagValue <Tag>`

For example: `SubscribeTagValue Tag_1`

**Response**

OnSuccess (or partial success):

`NotifySubscribeTagValue <Tag> <Quality> <Value>`

For example:

- `NotifySubscribeTagValue Tag_1 Uncertain 0`
- `NotifySubscribeTagValue Tag_1 Good 10`
- `NotifySubscribeTagValue Tag_1 Bad 12`

OnError:

- Global error:

  `ErrorSubscribeTagValue <Tag> <Error text>`

  For example:

  - `ErrorSubscribeTagValue Tag_1 Tag does not exist`
  - `ErrorSubscribeTagValue Tag_1 Subscription already exists`
- Error for tag value:

  `ErrorNotifyTagValue <Tag> <Error text>`

  For example:

  - `ErrorNotifyTagValue Tag_1 Encoding error`
  - `ErrorNotifyTagValue Tag_1 Value contains newline`

#### UnsubscribeTagValue (RT Unified)

##### Description

The `"`UnsubscribeTagValue" command unsubscribes a tag from monitoring.

**Request**

`UnsubscribeTagValue <Tag>`

For example: `UnsubscribeTagValue Tag_1`

**Response**

OnSuccess:

`NotifyUnsubscribeTagValue <Tag>`

For example:

- `NotifyUnsubscribeTagValue Tag_1`
- `NotifyUnsubscribeTagValue Tag_1`
- `NotifyUnsubscribeTagValue Tag_1`

OnError:

`ErrorUnsubscribeTagValue <Tag> <Error text>`

For example: `ErrorUnsubscribeTagValue Tag_1 Subscription does not exist`

#### ReadTagValue (RT Unified)

##### Description

The "ReadTagValue" command reads the value of a tag from the system. Only the tag value and the quality are signaled.

When the tag value contains a line break (\n), the value cannot be signaled. An error is signaled.

**Request**

`ReadTagValue <Tag>`

For example: `ReadTagValue Tag_1`

**Response**

OnSuccess (or partial success):

`NotifyReadTagValue <Tag> <Quality> <Value>`

For example:

- `NotifyReadTagValue Tag_1 Uncertain 0`
- `NotifyReadTagValue Tag_1 Good 10`
- `NotifyReadTagValue Tag_1 Bad 12`

OnError:

`ErrorReadTagValue <Tag> <Error text>`

For example:

- `ErrorReadTagValue Tag_1 Tag does not exist`
- `ErrorReadTagValue Tag_1 Encoding error`
- `ErrorReadTagValue Tag_1 Value contains newline`

#### WriteTagValue (RT Unified)

##### Description

The "WriteTagValue" command writes a value to a single tag.

When the transferred tag value contains a line break (\n), only the partial string in front of the line break is written to the tag.

**Request**

`WriteTagValue <Tag> <Value>`

For example: `WriteTagValue Motor.Label MC001`

**Response**

OnSuccess (or partial success):

`NotifyWriteTagValue <Tag>`

For example: `NotifyWriteTagValue Motor.Label`

OnError:

`ErrorWriteTagValue <Tag> <Error text>`

For example: `ErrorWriteTagValue Motor.Label Tag does not exist`

#### SetCharSet (RT Unified)

##### Description

Sets the character encoding to one of the following specified values: {UTF-8, cp437, cp850}

The default character encoding is UTF-8.

The following character coding values must be supported as a minimum:

- UTF-8
- cp850

  In German Windows systems, this is the default for the SystemLocale.
- cp437

  In US Windows systems, this is the default for the SystemLocale.

Internally, strings are treated as Unicode strings (often as UTF-16 in a CFSTR). For external communication over the pipe, the Unicode characters must be converted into a byte representation.

When a character cannot be converted for a specific character coding (e.g. the Greek character "π" in the character coding cp437), an "encoding error" is triggered.

**Request**

`SetCharSet <Value>`

For example: `SetCharSet UTF-8`

**Response**

OnSuccess:

`NotifySetCharSet <Value>`

For example: `NotifySetCharSet UTF-8`

OnError:

`ErrorSetCharSet <Value> <Error text>`

For example: `ErrorSetCharSet UTF-9 unknown character set`

#### ReadConfig (RT Unified)

##### Description

The "ReadConfig" command reads a setting configured for general browse behavior. To read multiple settings, call the command several times.

**Request**

ReadConfig <Param>

- `Param`:

  Value: The configuration parameters

  Possible parameters:

  - `DefaultPageSize`

    The page size used when a browse request is called without the "PageSize" parameter
  - `BrowseTimeOut`

    Number of seconds after which an inactive browse request is aborted.

For example:

ReadConfig DefaultPageSize

**OnSuccess**

NotifyReadConfig <Parameter> <Value>

For example:

NotifyReadConfig DefaultPageSize 1000

NotifyReadConfig BrowseTimeOut 300

**OnError**

ErrorReadConfig <Error description>

For example:

ErrorReadConfig Invalid arguments passed to browsing function.

#### WriteConfig (RT Unified)

##### Description

The "WriteConfig" command sets a setting configured for general browse behavior. To set multiple settings, call the command several times

**Request**

WriteConfig <Parameter> <Value>

- `Parameter`:

  Value: The configuration parameters

  Possible parameters:

  - `DefaultPageSize`

    The page size used when a browse request is called without the "PageSize" parameter

    Preset value: 1000
  - `BrowseTimeOut`

    Number of seconds after which an inactive browse request is canceled.

    Preset value: 300 s

For example:

WriteConfig DefaultPageSize 500

**Response**

OnSuccess:

NotifyWriteConfig <Parameter>

For example:

NotifyWriteConfig DefaultPageSize

OnError:

ErrorWriteConfig <Error description>

For example:

ErrorWriteConfig Invalid arguments passed to browsing function.

#### BrowseTags (RT Unified)

##### Description

The "BrowseTags" command returns the names of the tags of the local HMI system or all HMI systems communicating via runtime collaboration.

Information on the general browse behavior of the command can be found in section [Behavior of the browse commands](#behavior-of-the-browse-commands-rt-unified).

If the number of hits exceeds the page size of the response, the command consists of an initial request and 1 to N Next requests:

- You define the query in the initial request.

  It provides a response that delivers the first set of hits.
- You can call the remaining hits via Next requests.

##### Initial request

BrowseTags <System> <Page size> --filter <Filter>

- `System`: Optional

  Controls from which system the tags are read.

  - Value: "*"

    All systems that communicate with each other via runtime collaboration
  - Default value: The local system
- `Page size`: Optional

  Controls how many tags a response returns.

  Default value: The configured page size is used. See also section [ReadConfig](#readconfig-rt-unified).
- `--filter`
   `<Filter>`: Optional

  Restricts the command to tags whose "Name" matches the filter.

  - `--filter`: Command line command
  - `<Filter>:` The filter string

    Permitted wildcards:

    | Wildcard | Description | Example |
    | --- | --- | --- |
    | * | Replaces 0 to more characters | Filter string: "Motor*"   Tags contained in the response: - "Motor" - "MotorOn" - "MotorOff" |
    | ? | Replaces 1 character | Filter string: "Motor_?"   Tags contained in the response: - "Motor_1" - "Motor_2" |
  - Default value: All tags of the system specified by `SystemNames` are queried.

For example:

BrowseTags * 100 --filter *Tag0* // browse for tags of all systems with filter and paging

##### Next request

BrowseTags --next

##### Response

**OnSuccess**

NotifyBrowseTags <System>::<Tag name> ... <System>::<Tag name>

For example:

NotifyBrowseTags HMI_RT_1::InternalTag0 HMI_RT_2::InternalTag01 HMI_RT_2::InternalTag02

**OnError**

ErrorBrowseTags <Error description>

For example:

ErrorBrowseTags Invalid arguments passed to browsing function.

#### BrowseConfiguredAlarms (RT Unified)

##### Description

The "BrowseConfiguredAlarms" command returns the names of the configured alarms of the local HMI system or all HMI systems communicating via Runtime Collaboration.

Information on the general browse behavior of the command can be found in section [Behavior of the browse commands](#behavior-of-the-browse-commands-rt-unified).

If the number of hits exceeds the page size of the response, the command consists of an initial request and 1 to N Next requests:

- You define the query in the initial request.

  It provides a response that delivers the first set of hits.
- You can call the remaining hits via Next requests.

##### Initial request

BrowseConfiguredAlarms <System> <Page size> --filter <Filter>

- `System`: Optional

  Controls from which system the alarms are read.

  - Value: "*"

    All systems that communicate with each other via runtime collaboration
  - Default value: The local system
- `Page size`: Optional

  Controls how many alarms a response returns.

  Default value: The configured page size is used. See also section [ReadConfig](#readconfig-rt-unified).
- `--filter`
   `<Filter>`: Optional

  Restricts the command to alarms whose "Name" matches the filter.

  - `--filter`: Command line command
  - `<Filter>:` The filter string

    Permitted wildcards:

    | Wildcard | Description | Example |
    | --- | --- | --- |
    | * | Replaces 0 to more characters | Filter string: "Motor*:Analog_ Alarm"   Alarms contained in the response: - "MotorOn:AnalogAlarm" - "MotorOff:AnalogAlarm" |
    | ? | Replaces 1 character | Filter string: "Motor_?:Analog_ alarm"   Alarms contained in the response:  - "Motor_1:Analog_alarm" - "Motor_2:Analog_alarm" |
  - Default value: All tags of the system specified by `SystemNames` are queried.

For example:

BrowseConfiguredAlarms * 100 --filter *Analog* // browse for alarms of all systems with filter and paging

##### Next request

BrowseConfiguredAlarms --next

##### Response

**OnSuccess**

NotifyBBrowseConfiguredAlarms <System>::<Alarm name> ... <System>::<Alarm name>

For example:

NotifyBrowseConfiguredAlarms HMI_RT_1::Motor_1:AnalogAlarm_1 HMI_RT_2::Motor_1:AnalogAlarm_1 HMI_RT_2::Motor_2:AnalogAlarm_1

**OnError**

ErrorBrowseConfiguredAlarms <Error description>

For example:

ErrorBrowseConfiguredAlarms A parameter is not valid or out of range.

#### BrowseAlarmClasses (RT Unified)

##### Description

The command "`BrowseAlarmClasses`" returns the alarm classes of the local HMI system or all HMI systems communicating via Runtime Collaboration.

Information on the general browse behavior of the command can be found in section [Behavior of the browse commands](#behavior-of-the-browse-commands-rt-unified).

> **Note**
>
> Paging is not available for "BrowseAlarmClasses".

**Request**

`BrowseAlarmClasses`
 `<System>`

- `System`: Optional

  Controls from which system the tags are read.

  - Value: "*"

    All systems that communicate with each other via runtime collaboration
  - Default value: The local system

For example:

`BrowseAlarmClasses` 
`//Browse for alarm classes in local system`

**Response**

OnSuccess

NotifyBrowseAlarmClasses <System>::<Alarm class> ... <System>::<Alarm class>

For example:

NotifyBrowseAlarmClasses HMI_RT_1::Alarm HMI_RT_1::SystemNotification HMI_RT_1::SystemInformation HMI_RT_1::SystemAlarm HMI_RT_1::Notification HMI_RT_1::OperatorInputInformation

OnError

ErrorBrowseAlarmClasses <Error description>

For example:

ErrorBrowseAlarmClasses Invalid arguments passed to browsing function.

---

**See also**

[ReadConfig (RT Unified)](#readconfig-rt-unified)

### Reference  (RT Unified)

The following section contains a reference of the properties of tags that you get with the command ReadTagValue.

The commands transfer the property values as string.

#### Tag properties

**"Name" property**

Name of the tag

**"Value" property**

Value of the tag at the moment of the read operation.

**"Quality" property**

Quality of the read operation of the tag

Possible values:

- "Good"
- "Bad"
- "Uncertain"

**"ErrorDescription" property**

Description of the error code of the last read or write operation of the tag

## Using expert syntax (RT Unified)

This section contains information on the following topics:

- [Basics of expert syntax (RT Unified)](#basics-of-expert-syntax-rt-unified)
- [Commands (RT Unified)](#commands-rt-unified-1)
- [Reference (RT Unified)](#reference-rt-unified-1)
- [Syntax of the alarm filter (RT Unified)](#syntax-of-the-alarm-filter-rt-unified)

### Basics of expert syntax (RT Unified)

#### Characteristics

The expert syntax has the following characteristics:

- Complete JSON commands and replies.
- Commands for individual objects and multiple objects, for example, to write multiple tags in one call.
- Character coding is always UTF-8.
- Cookies are available and mandatory.

**Structure of a request**

`{`

`"`
`Message`
`": "<Command>",`

`"`
`Params`
`":`

`{`

`"<Object name>":`

`[`

`"<Param1>",`

`"<Param2>"`

`]`

`},`

`"`
`ClientCookie`
`": "<Cookie name>"`

`}`

**Structure of a response**

OnSuccess

`{`

`"`
`Message`
`": "Notify<Command>",`

`"`
`Params`
`":`

`{`

`"<Object name>":`

`[`

`{`

`"<Value1>"`

`},`

`{`

`"<Value2>"`

`}`

`]`

`},`

`"`
`ClientCookie`
`": "<Cookie name>"`

`}`

OnError

{

"Message": "Error<Command>",

"ErrorCode": "<Error code>",

"ErrorDescription": "<Error description>",

"ClientCookie": "<Cookie name>"

}

#### Overview of the commands of the expert syntax

| Command | OnSuccess | OnError | Description |
| --- | --- | --- | --- |
| `SubscribeTag <Tag> <ClientCookie>` | `NotifySubscribeTag <Tag name>  <Value>  <TimeStamp>  <Quality>  <QualityCode> <hasChanged> <Error code>  <Error text> <ClientCookie>` | `ErrorSubscribeTag <Error code> <Error text> <ClientCookie>` | Subscribes one or more tags for monitoring. |
| `UnsubscribeTag <ClientCookie>` | `NotifyUnsubscribeTag <ClientCookie>` | `ErrorUnsubscribeTag <Error code> <Error text> <ClientCookie>` | Unsubscribes the tag or tags from the cookie from monitoring. |
| `ReadTag <Tags> <ClientCookie>` | `NotifyReadTag <Tag name>  <Value>  <TimeStamp>  <Quality>  <QualityCode> <Errorcode>  <Error text> <ClientCookie>` | `ErrorReadTag  <Error code> <Error text> <ClientCookie>` | Reads the value of one or more tags of the system. |
| `WriteTag <Tags, Values>`    `<ClientCookie>` | `NotifyWriteTag <Tag name> <Error code> <Error text>`    `<ClientCookie>` | `ErrorWriteTag  <Error code> <Error text> <ClientCookie>` | Writes the specified values to the specified tags. |
| `SubscribeAlarm <Filter> <Systems> <Language> <ClientCookie>` | `NotifySubscribeAlarm <ClientCookie> <Alarms>` | `ErrorSubscribeAlarm <Error code> <Error text> <ClientCookie>` | Subscribes the alarms defined over the filter, the system and the language ID for monitoring. |
| `UnsubscribeAlarm <ClientCookie>` | `NotifyUnsubscribeAlarm <ClientCookie>` | `Error UnsubscribeAlarm <Error code> <Error text> <ClientCookie>` | Unsubscribes the alarms from the cookie from monitoring. |
| `ReadAlarm <Filter> <Systems> <Language>`    `<ClientCookie>` | `NotifyReadAlarm <ClientCookie> <Alarms>` | `ErrorReadAlarm <Error code> <Error text> <ClientCookie>` | Reads the alarms defined by the filter, the system and the LanguageID. |
| `ReadConfig <Parameter> <ClientCookie>` | `NotifyReadConfig <Parameter> <Value> <ClientCookie>` | `ErrorReadConfig <Error code> <Error text> <ClientCookie>` | Reads the settings configured for the general browse behavior. |
| `WriteConfig <Parameter> <ClientCookie>` | `NotifyWriteConfig <Parameter> <Value> <ClientCookie>` | `ErrorWriteConfig <Error code> <Error text><ClientCookie>` | Sets the settings for the general browse behavior. |
| `BrowseTags`   - Initial request:    `BrowseTags <LanguageId> <Filter> <Attribute> <PageSize> <Systems> <ClientCookie>` - Next request:    `BrowseTags <Next> <ClientCookie>` | `NotifyBrowseTags <Attribute> <Value> ... <Attribute> <Value> <ClientCookie>` | `ErrorBrowseTags <Error code> <Error text> <ClientCookie>` | Returns "Name", "DisplayName" and "DataType" as well as optional additional attribute values of the tags of the local system or several HMI systems communicating via runtime collaboration. |
| `BrowseConfiguredAlarms`:  - Initial request:    `BrowseConfiguredAlarms <LanguageId> <Filter> <Attributes> <PageSize> <SystemNames> <ClientCookie>` - Next request:    `BrowseConfiguredAlarms <Next> <ClientCookie>` | `NotifyBrowseConfiguredAlarms <Alarm class> <Alarms> ... <Alarm class> <Alarms> <ClientCookie>` | `ErrorBrowseConfiguredAlarms <Error code> <Error text> <ClientCookie>` | Returns "AlarmClass", "Name" and "Area" as well as optional further attribute values of the configured alarms of an HMI system or several systems communicating via Runtime Collaboration. |
| `BrowseAlarmClasses <Filter> <Attributes> <Systems>` | `NotifyBrowseAlarmClasses <Alarm class> ... <Alarm class> <ClientCookie>` | `ErrorBrowseAlarmClasses <Error code> <Error text> <ClientCookie>` | Returns the alarm classes of the local system or all systems communicating via Runtime Collaboration. |

#### Errors and error texts

This help only provides a selection of possible error messages. The error texts can also differ from the texts in your projects.

#### Attributes of the tags and alarms

You can find a description of the attributes of the tags and alarms in the help document [Runtime - Open Development Kit (ODK)](Runtime%20API%20%28RT%20Unified%29.md#basics-rt-unified).

### Commands (RT Unified)

This section contains information on the following topics:

- [SubscribeTag (RT Unified)](#subscribetag-rt-unified)
- [UnsubscribeTag (RT Unified)](#unsubscribetag-rt-unified)
- [ReadTag (RT Unified)](#readtag-rt-unified)
- [WriteTag (RT Unified)](#writetag-rt-unified)
- [SubscribeAlarm (RT Unified)](#subscribealarm-rt-unified)
- [UnsubscribeAlarm (RT Unified)](#unsubscribealarm-rt-unified)
- [ReadAlarm (RT Unified)](#readalarm-rt-unified)
- [ReadConfig (RT Unified)](#readconfig-rt-unified-1)
- [WriteConfig (RT Unified)](#writeconfig-rt-unified-1)
- [BrowseTags (RT Unified)](#browsetags-rt-unified-1)
- [BrowseConfiguredAlarms (RT Unified)](#browseconfiguredalarms-rt-unified-1)
- [BrowseAlarmClasses (RT Unified)](#browsealarmclasses-rt-unified-1)

#### SubscribeTag (RT Unified)

##### Description

The "SubscribeTag" command subscribes one or more tags for monitoring. The following properties are monitored:

- Tag value
- Quality
- Quality code
- Time stamp

"NotifiySubscribeTag" always returns all monitored tags, even if only the value of one monitored tag changes. The change can be a change to the quality code, time stamp or tag value. The order of tags in the response corresponds to the order in the "SubscribeTag" request.

It is permitted to have the same tag monitored by multiple "SubscribeTag" calls.

**Request**

`{"Message":"SubscribeTag","Params":{"Tags":["<Tag>","<Tag>"]},"ClientCookie":"<Cookie>"}`

- `Tags`: List of the tags to be monitored
- `ClientCookie`: Is used for "UnsubscribeTag" and to assign the notification to its monitoring.

For example:

{"Message":"SubscribeTag","Params":{"Tags":["Tag_0","Tag_1"]},"ClientCookie":"mySubscription1"}

**Response**

**OnSuccess**

`{"Message":"NotifySubscribeTag", "Params":{"Tags":[{"Name":"<Tag>", "Quality":"<Value>", "QualityCode":"<Value>", "TimeStamp":"<Value>", "Value":"<Tag value>", "ErrorCode":<Value>, "ErrorDescription":"<Error text>"}, {"Name":"<Tag>", "Quality":"<Value>", "QualityCode":"<Value>", "TimeStamp":"<Value>", "Value":"<Tag value>", "ErrorCode":<Value>, "ErrorDescription":"<Error text>"}]}, "ClientCookie":"<Cookie>"}`

For example:

`{"Message":"NotifySubscribeTag", "Params":{"Tags":[{"Name":"Tag_0", "Quality":"Good", "QualityCode":"192", "TimeStamp":"2019-01-30T11:25:35Z", "Value":"16", "ErrorCode":0, "ErrorDescription":""}, {"Name":"Tag_1", "Quality":"Uncertain", "QualityCode":"76", "TimeStamp":"2019-01-30T11:25:35Z", "Value":"1", "ErrorCode":-2147483620, "ErrorDescription":"Tag does not exist"}]}, "ClientCookie":"mySubscription1"}`

**OnError**

`{"Message":"ErrorSubscribeTag", "ErrorCode":<Value>, "ErrorDescription":"<Error text>", "ClientCookie":"<Cookie>"}`

For example:

`{"Message":"ErrorSubscribeTag", "ErrorCode":-2147483621, "ErrorDescription":"Subscription could not be created", "ClientCookie":"mySubscription1"}`

#### UnsubscribeTag (RT Unified)

##### Description

The "UnsubscribeTag" command unsubscribes a tag from monitoring that was started with the cookie transferred in the call of "SubscribeTag".

**Request**

`{"Message":"UnsubscribeTag","ClientCookie":"<Cookie>"}`

For example:

{"Message":"UnsubscribeTag","ClientCookie":"mySubscription1"}

**Response**

**OnSuccess**

`{"Message":"NotifyUnsubscribeTag","ClientCookie":"<Cookie>"}`

For example:

`{"Message":"NotifyUnsubscribeTag","ClientCookie":"mySubscription1"}`

**OnError**

`{"Message":"ErrorUnsubscribeTag", "ErrorCode":<Value>, "ErrorDescription":"<Error text>", "ClientCookie":"Cookie"}`

For example:

`{"Message":"ErrorUnsubscribeTag", "ErrorCode":-2147483621, "ErrorDescription":"Subscription could not be closed", "ClientCookie":"mySubscription1"}`

#### ReadTag (RT Unified)

##### Description

The "ReadTag" command reads multiple tags. The tag value, the quality, the quality code and the time stamp are signaled.

The order of tags in the response corresponds to the order in the "ReadTag" request.

**Request**

`{"Message":"ReadTag","Params":{"Tags":["<Tag>","<Tag>"]},"ClientCookie":"<Cookie>"}`

For example:

{"Message":"ReadTag","Params":{"Tags":["Tag_0","Tag_1"]},"ClientCookie":"myRequest1"}

**Response**

**OnSuccess**

`{"Message":"NotifyReadTag","Params":{"Tags":[{"Name":"<Tag>","Quality":"<Value>","QualityCode":"<Value>","TimeStamp":"<Value>","Value":"<TagValue>","ErrorCode":<Value>,"ErrorDescription":"<ErrorText>"},{"Name":"<Tag>","Quality":"<Value>","QualityCode":"<Value>","TimeStamp":"<Value>","Value":"<TagValue>","ErrorCode":<Value>,"ErrorDescription":"<ErrorText>"}]},"ClientCookie":"<Cookie>"}`

For example:

`{"Message":"NotifyReadTag","Params":{"Tags":[{"Name":"Tag_0","Quality":"Good","QualityCode":"192","TimeStamp":"2019-01-30T11:25:35Z","Value":"16","ErrorCode":0,"ErrorDescription":""},{"Name":"Tag_1","Quality":"Uncertain","QualityCode":"76","TimeStamp":"2019-01-30T11:25:35Z","Value":"1","ErrorCode":-2147483620,"ErrorDescription":"Tag does not exist"}]},"ClientCookie":"myRequest1"}`

**OnError**

`{"Message":"ErrorReadTag","ErrorCode":<Value>,"ErrorDescription":"<Error text>", "ClientCookie":"<Cookie>"}`

For example:

`{"Message":"ErrorReadTag","ErrorCode":-2147483621,"ErrorDescription":"Failed to Read", "ClientCookie":"myRequest1"}`

#### WriteTag (RT Unified)

##### Description

The "WriteTag" command writes the values of multiple tags.

**Request**

`{"Message":"WriteTag","Params":{"Tags":[{"Name":"<Tag>","Value":"<Tag value>"},{"Name":"<Tag>","Value":"<Tag value>"}]},"ClientCookie":"<Cookie>"}`

For example:

{"Message":"WriteTag","Params":{"Tags":[{"Name":"Tag_0","Value":"50"},{"Name":"Tag_1","Value":"40"}]},"ClientCookie":"myRequest2"}

**Response**

**OnSuccess**

`{"Message":"NotifyWriteTag","Params":{"Tags":[{"Name":"<Tag>","ErrorCode":<Value>,"ErrorDescription":"<ErrorText>"},{"Name":"<Tag>","ErrorCode":<Value>,"ErrorDescription":"<ErrorText>"}]},"ClientCookie":"<Cookie>"}`

For example:

`{"Message":"NotifyWriteTag","Params":{"Tags":[{"Name":"Tag_0","ErrorCode":0,"ErrorDescription":""},{"Name":"Tag_1","ErrorCode":-2147483620,"ErrorDescription":"Tag does not exist"}]},"ClientCookie":"myRequest2"}`

**OnError**

`{"Message":"ErrorWriteTag","ErrorCode":<Value>,"ErrorDescription":"<Error text>", "ClientCookie":"<Cookie>"}`

For example:

`{"Message":"ErrorWriteTag","ErrorCode":-2147483621,"ErrorDescription":"Failed to Write", "ClientCookie":"myRequest2"}`

#### SubscribeAlarm (RT Unified)

##### Description

The "SubscribeAlarm" command subscribes systems for monitoring of changes of active alarms.

The first time "NotifySubscribeAlarm" is called, all active alarms are queried. Afterwards "NotifySubscribeAlarm" is only called if the status of an alarm changes.

**Request**

`{"Message":"SubscribeAlarm","Params":{"SystemNames":["<System>","<System>"],"Filter":"<Filter>","LanguageId":<ID>},"ClientCookie":"<Cookie>"}`

- `SystemNames`: Optional

  When the list is empty or missing, all known systems are subscribed for monitoring.
- `Filter`: Optional
- `LanguageID`: Optional
- `ClientCookie`:

  Is used for "UnsubscribeAlarm" and to assign the notification to its monitoring.

For example:

{"Message":"SubscribeAlarm","Params":{"SystemNames":["System0","System1"],"Filter":"AlarmClassName != ‘Warning’","LanguageId":1033},"ClientCookie":"CookieForSubscribeAlarms123"}

**Response**

**OnSuccess**

`{"Message":"NotifySubscribeAlarm","ClientCookie":"<Cookie>","params":{"Alarms":[{<Key value pairs for the properties of the first alarm>},{<Key value pairs for the properties of the second alarm>}, {<...>}]}}`

For example:

`{"Message":"NotifySubscribeAlarm","ClientCookie":"CookieForSubscribeAlarms123","params":{"Alarms":[{"AcknowledgmentTime":"1970-01-01 00:00:00.0000000","AlarmClassName":"Alarm","AlarmClassSymbol":"Alarm","AlarmText1":"","AlarmText2":"","AlarmText3":"","AlarmText4":"","AlarmText5":"","AlarmText6":"","AlarmText7":"","AlarmText8":"","AlarmText9":"","Area":"","BackColor":"4294967295","ChangeReason":"3","ClearTime":"1970-01-01 00:00:00.0000000","Connection":"1.0.0.0.0.0","DeadBand":"No deadband configured.","Duration":"00:00:01.7431098","EventText":"","Flashing":"FALSE","HostName":"md1z5cpc","ID":"0","InfoText":"","InstanceID":"9","LoopInAlarm":"","ModificationTime":"2019-01-30 11:25:39.9780320","Name":"RUNTIME_1::Tag_2:Alarm2","NotificationReason":"1","Origin":"","Priority":"1","RaiseTime":"2019-01-30 11:25:39.9780320","ResetTime":"1970-01-01 00:00:00.0000000","SourceID":"","SourceType":"1","State":"1","StateMachine":"7","StateText":"R","SuppressionState":"0","SystemSeverity":"0","Tag":"RUNTIME_1::Tag_2","TextColor":"4278190080","UserName":"","Value":"7","ValueLimit":"No limit configured.","ValueQuality":"192"},{"AcknowledgmentTime":"1970-01-01 00:00:00.0000000","AlarmClassName":"Alarm","AlarmClassSymbol":"Alarm","AlarmText1":"","AlarmText2":"","AlarmText3":"","AlarmText4":"","AlarmText5":"","AlarmText6":"","AlarmText7":"","AlarmText8":"","AlarmText9":"","Area":"","BackColor":"4294967295","ChangeReason":"3","ClearTime":"1970-01-01 00:00:00.0000000","Connection":"1.0.0.0.0.0","DeadBand":"No deadband configured.","Duration":"00:00:01.7431098","EventText":"","Flashing":"FALSE","HostName":"md1z5cpc","ID":"0","InfoText":"","InstanceID":"9","LoopInAlarm":"","ModificationTime":"2019-01-30 11:25:39.9780320","Name":"RUNTIME_1::Tag_2:Alarm1","NotificationReason":"1","Origin":"","Priority":"1","RaiseTime":"2019-01-30 11:25:39.9780320","ResetTime":"1970-01-01 00:00:00.0000000","SourceID":"","SourceType":"1","State":"1","StateMachine":"7","StateText":"R","SuppressionState":"0","SystemSeverity":"0","Tag":"RUNTIME_1::Tag_2","TextColor":"4278190080","UserName":"","Value":"7","ValueLimit":"No limit configured.","ValueQuality":"192", "AlarmGroupID": "1"}]}`

**OnError**

`{"Message":"ErrorSubscribeTag", "ErrorCode":<Value>, "ErrorDescription":"<Error text>", "ClientCookie":"<Cookie>"}`

For example:

`{"Message":"ErrorSubscribeAlarm","ErrorCode":"-2147483621","ErrorDescription":"Alarm Subscription failed because of invalid filter","ClientCookie":"CookieForSubscribeAlarms123"}`

#### UnsubscribeAlarm (RT Unified)

##### Description

The "UnsubscribeAlarm" command unsubscribes the alarms from monitoring that was started with the cookie transferred in the call of "SubscribeAlarm".

**Request**

`{"Message":"UnsubscribeAlarm","ClientCookie":"<Cookie>"}`

For example:

{"Message":"UnsubscribeAlarm","ClientCookie":"CookieForSubscribeAlarms123"}

**Response**

**OnSuccess**

`{"Message":"NotifyUnsubscribeAlarm","ClientCookie":"<Cookie>"}`

For example:

`{"Message":"NotifyUnsubscribeAlarm","ClientCookie":"CookieForSubscribeAlarms123"}`

**OnError**

`{"Message":”ErrorUnsubscribeAlarm","ErrorCode":<Value>,"ErrorDescription":"<Error text>", "ClientCookie":"<Cookie>"}`

For example:

`{"Message":"ErrorUnsubscribeAlarm","ErrorCode":-2147483621,"ErrorDescription":"Subscription could not be closed", "ClientCookie":"CookieForSubscribeAlarms123"}`

#### ReadAlarm (RT Unified)

##### Description

The "ReadAlarm" command reads all active alarms.

**Request**

`{"Message":"ReadAlarm","Params":{"SystemNames":["<System>","<System>"],"Filter":"<Value>","LanguageId":<Value>},"ClientCookie":"<Cookie>"}`

- `SystemNames`: Optional

  When the list is empty or missing, all known systems are subscribed for monitoring.
- `Filter`: Optional
- `LanguageID`: Optional
- `ClientCookie`:

  Is used for "UnsubscribeAlarm" and to assign the notification to its monitoring.

For example:

{"Message":"ReadAlarm","Params":{"SystemNames":["System0","System1"],"Filter":"","LanguageId":1033},"ClientCookie":"CookieForReadAlarmRequest456"}

**Response**

`{"Message":"NotifyReadAlarm", "ClientCookie":"<Cookie>","params":{"Alarms":[{<Key value pairs for properties of the first alarm>},{<Key value pairs for the properties of the second alarm>}, {<...>}]}}`

**OnSuccess**

For example:

`{"Message":"NotifyReadAlarm", "ClientCookie":"CookieForReadAlarmRequest456", "params":{"Alarms":[{"AcknowledgmentTime":"1970-01-01 00:00:00.0000000", "AlarmClassName":"Alarm", "AlarmClassSymbol":"Alarm","AlarmText1":"","AlarmText2":"","AlarmText3":"","AlarmText4":"","AlarmText5":"","AlarmText6":"","AlarmText7":"","AlarmText8":"","AlarmText9":"","Area":"","BackColor":"4294967295","ChangeReason":"3","ClearTime":"1970-01-01 00:00:00.0000000","Connection":"1.0.0.0.0.0","DeadBand":"No deadband configured.","Duration":"00:00:01.7431098","EventText":"","Flashing":"FALSE","HostName":"md1z5cpc","ID":"0","InfoText":"","InstanceID":"9","LoopInAlarm":"","ModificationTime":"2019-01-30 11:25:39.9780320","Name":"RUNTIME_1::Tag_2:Alarm2","NotificationReason":"1","Origin":"","Priority":"1","RaiseTime":"2019-01-30 11:25:39.9780320","ResetTime":"1970-01-01 00:00:00.0000000","SourceID":"","SourceType":"1","State":"1","StateMachine":"7","StateText":"R","SuppressionState":"0","SystemSeverity":"0","Tag":"RUNTIME_1::Tag_2","TextColor":"4278190080","UserName":"","Value":"7","ValueLimit":"No limit configured.","ValueQuality":"192"},{"AcknowledgmentTime":"1970-01-01 00:00:00.0000000","AlarmClassName":"Alarm","AlarmClassSymbol":"Alarm","AlarmText1":"","AlarmText2":"","AlarmText3":"","AlarmText4":"","AlarmText5":"","AlarmText6":"","AlarmText7":"","AlarmText8":"","AlarmText9":"","Area":"","BackColor":"4294967295","ChangeReason":"3","ClearTime":"1970-01-01 00:00:00.0000000","Connection":"1.0.0.0.0.0",DeadBand":"No deadband configured.","Duration":"00:00:01.7431098","EventText":"","Flashing":"FALSE","HostName":"md1z5cpc","ID":"0","InfoText":"","InstanceID":"9","LoopInAlarm":"","ModificationTime":"2019-01-30 11:25:39.9780320","Name":"RUNTIME_1::Tag_2:Alarm1","NotificationReason":"1","Origin":"","Priority":"1","RaiseTime":"2019-01-30 11:25:39.9780320","ResetTime":"1970-01-01 00:00:00.0000000","SourceID":"","SourceType":"1","State":"1","StateMachine":"7","StateText":"R","SuppressionState":"0","SystemSeverity":"0","Tag":"RUNTIME_1::Tag_2","TextColor":"4278190080","UserName":"","Value":"7","ValueLimit":"No limit configured.","ValueQuality":"192"", "AlarmGroupID": "1"}]}`

**OnError**

`{"Message":"ErrorReadAlarm","ErrorCode":<Value>, "ErrorDescription":"<Error text>", "ClientCookie":"<Cookie>"}`

For example:

`{"Message":"ErrorReadAlarm","ErrorCode":-2147483621, "ErrorDescription":"Alarm Subscription failed because of invalid filter", "ClientCookie":"CookieForReadAlarmRequest456"}`

#### ReadConfig (RT Unified)

##### Description

The "ReadConfig" command reads the settings configured for the general browse behavior.

**Request**

{"Message": "ReadConfig", "Params": ['<Parameter>', '<Parameter>'], "ClientCookie": '<Cookie>'}

- `Params`:

  Value: Comma-separated list of configuration parameters

  Possible parameters:

  - `DefaultPageSize`

    The page size used when a browse request is called without the "PageSize" parameter
  - `BrowseTimeOut`

    Number of seconds after which an inactive browse request is canceled.
- `Cookie`:

  Name of the response cookie

For example:

{"Message": "ReadConfig", "Params": ['DefaultPageSize', 'BrowseTimout'], "ClientCookie": "myBrowseAlarmsRequest1"}

**OnSuccess**

{"Message":"NotifyReadConfig", "Params": {"<Parameter>":<Value>, "<Parameter>":<Value>}, "ClientCookie": '<Cookie>'}

For example:

{"Message":"NotifyReadConfig", "Params": {"DefaultPageSize":500, "BrowseTimeOut":60}, "ClientCookie": "myBrowseAlarmsRequest1"}

**OnError**

{"Message": "ErrorReadConfig", "ErrorCode": "<Code>", "ErrorDescription": "<Description>", "ClientCookie": "<Cookie>"}

For example:

{"Message": "ErrorReadConfig", "ErrorCode": "-2165322729", "ErrorDescription": "Invalid arguments passed to browsing function.", "ClientCookie": "myBrowseAlarmsRequest1"}

#### WriteConfig (RT Unified)

##### Description

The "WriteConfig" command sets configurable settings for the general browse behavior.

**Request**

{"Message": "WriteConfig", "Params": ["<Parameter>":<Value>, "<Parameter>":<Value>], "ClientCookie": '<Cookie>'}

- `Params`:

  Value: Comma-separated list of configuration parameters and their values

  Possible parameters:

  - `DefaultPageSize`

    The page size used when a browse request is called without the "PageSize" parameter

    Preset value: 1000
  - `BrowseTimeOut`

    Number of seconds after which an inactive browse request is canceled.

    Preset value: 300 s
- `Cookie`:

  Name of the response cookie

For example:

{"Message": "WriteConfig", "Params": ["DefaultPageSize":500, "BrowseTimout":60], "ClientCookie": "myBrowseAlarmsRequest1"}

**OnSuccess**

{"Message":"NotifyWriteConfig", "Params": {"<Parameter>":<Value>, "<Parameter>":<Value>}, "ClientCookie": '<Cookie>'}

For example:

{"Message":"NotifyWriteConfig", "Params": {"DefaultPageSize":500, "BrowseTimeOut":60}, "ClientCookie": "myBrowseAlarmsRequest1"}

**OnError**

{"Message": "ErrorWriteConfig", "ErrorCode": "<Code>", "ErrorDescription": "<Description>" "ClientCookie": "<Cookie>"}

For example:

{"Message": "ErrorWriteConfig", "ErrorCode": "-2165322733", "ErrorDescription": "A parameter is not valid or out of range.", "ClientCookie": "myBrowseAlarmsRequest1"}

#### BrowseTags (RT Unified)

##### Description

The "BrowseTags" command returns "Name", "DisplayName" and "DataType" as well as optional further attribute values of the tags of an HMI system or several HMI systems communicating via runtime collaboration.

Information on the general browse behavior of the command can be found in section [Behavior of the browse commands](#behavior-of-the-browse-commands-rt-unified).

If the number of hits exceeds the page size of the response, the command consists of an initial request and 1 to N Next requests:

- You define the query in the initial request.

  It provides a response that delivers the first set of hits.
- You can call the remaining hits via Next requests.

##### Initial request

{"Message": "BrowseTags", "Params": {"LanguageId": <Value>, "Filter": "<String>", "Attributes": ["<Attribute name>", ..., "<Attribute name>"], "PageSize": <Value>, "SystemNames": ["<Name>", ..., "<Name>"]}, "ClientCookie": "<Cookie>"}

- `LanguageId`: Optional

  Controls in which language the "DisplayName" of the tags is returned.

  - Value: The language ID
  - Default value: The default language of the system from which the tag originates
- `Filter`: Optional

  Restricts the command to tags whose "Name" matches the filter.

  - Value: Filter string

    Permitted wildcards:

    | Wildcard | Description | Example |
    | --- | --- | --- |
    | * | Replaces 0 to more characters | Filter string: "Motor*"   Tags contained in the response: - "Motor" - "MotorOn" - "MotorOff" |
    | ? | Replaces 1 character | Filter string: "Motor_?"   Tags contained in the response: - "Motor_1" - "Motor_2" |
  - Default value: All tags of the system specified by `SystemNames` are queried.
- `Attributes`: Optional

  Controls which tag attributes returns the response:

  - Value: Comma-separated enumeration of the attribute names

    The response returns "Name", "DisplayName" and "DataType" as well as the specified attributes.
  - Value: "*"

    The response provides all attributes supported by the TIA Portal for tags: Name, DisplayName, AcquisitionMode, Persistent, DataType, Connection, AcquisitionCycle, MaxLength, SubstituteValueUsage, InitialValue, SubstituteValue, InitialMaxValue, InitialMinValue, Address
  - Default value: The response returns "Name", "DisplayName" and "DataType".
- `PageSize`: Optional

  Controls how many tags a response returns.

  Default value: The configured page size is used. See also section [ReadConfig](#readconfig-rt-unified-1).
- `SystemNames`: Optional

  Controls from which system the tags are read.

  - Value: "*"  
    All systems that communicate with each other via runtime collaboration
  - Value: Comma-separated list of systems that communicate with each other via runtime collaboration

    FOR EXAMPLE: "HMI_RT_1", "HMI_RT_2"
  - Default value: The local system
- `ClientCookie`:

  Value: Name of the response cookie

For example:

{"Message": "BrowseTags", "Params": {"LanguageId": 1033, "Filter": "*InternalTag_Bool_1*", "Attributes": ["AcquisitionMode", "MaxValue"], "PageSize": 50, "SystemNames": ["HMI_RT_1", "HMI_RT_2"]}, "ClientCookie": "myBrowseTagRequest1"}

##### Next request

{"Message": "BrowseTags", "Params": "Next", "ClientCookie": "<Cookie>"}

For example:

{"Message": "BrowseTags", "Params": "Next", "ClientCookie": "myBrowseTagRequest1"}

##### Response

**OnSuccess**

{"ClientCookie": "<Cookie>", "Message": "NotifyBrowseTags", "Params": {"Tags": [{"<Attribute name":<Value>, "<Attribute name>":<Value>, "DataType":<Value>, "DisplayName": "<Value>", "Name":"<Value>"}],}}

For example:

{"ClientCookie": "<myBrowseTagRequest1>", "Message": "NotifyBrowseTags", "Params": {"Tags": [{"AcquisitionMode":0, "MaxValue":1000, "DataType":1, "DisplayName": "HMI_RT_1::InternalTag_Bool_1", "Name":"HMI_RT_1::InternalTag_Bool_1"}],}}

**OnError**

{"Message": "ErrorBrowseTags", "ErrorCode": "<Code>", "ErrorDescription": "<Description>", "ClientCookie": "Cookie>"}

For example:

{"Message": "ErrorBrowseTags", "ErrorCode": "-2165323798", "ErrorDescription": "Invalid system name.", "ClientCookie": myBrowseTagRequest1"}

#### BrowseConfiguredAlarms (RT Unified)

##### Description

The "BrowseConfiguredAlarms" command returns "AlarmClass", "Name" and "Area" as well as optional further attribute values of the configured alarms of an HMI system or several systems communicating via Runtime Collaboration.

Information on the general browse behavior of the command can be found in section [Behavior of the browse commands](#behavior-of-the-browse-commands-rt-unified).

If the number of hits exceeds the page size of the response, the command consists of an initial request and 1 to N Next requests:

- You define the query in the initial request.

  It provides a response that delivers the first set of hits.
- You can call the remaining hits via Next requests.

##### Initial request

{"Message": "BrowseConfiguredAlarms", "Params": {"LanguageId": <Value>, "Filter": "<String>", "Attributes": ["<Attribute name>", ..., "<Attribute name>"], "PageSize": <Value>, "SystemNames": ["<Name>", ..., "<Name>"]}, "ClientCookie": "<Cookie>"}

- `LanguageId`: Optional

  Controls in which language the alarm texts are returned.

  - Value: The language ID
  - Default value: The default language of the system from which the alarm originates
- `Filter`: Optional

  Restricts the command to alarms whose "Name" matches the filter.

  - Value: Filter string

    Permitted wildcards:

    | Wildcard | Description | Example |
    | --- | --- | --- |
    | * | Replaces 0 to more characters | Filter string: "Motor*:Analog_Alarm"   Alarms contained in the response:  - "MotorOn:AnalogAlarm" - "MotorOff:AnalogAlarm" |
    | ? | Replaces 1 character | Filter string: "Motor_?:Analog_alarm"   Alarms contained in the response:  - "Motor_1:Analog_alarm" - "Motor_2:Analog_alarm" |
  - Default value: All alarms of the system specified by `SystemNames` are queried.
- `Attributes`: Optional

  Controls which alarm attributes the response returns:

  - Value: Comma-separated enumeration of the attribute names

    The response returns "AlarmClass", "Name" and "Area" as well as the specified attributes.
  - Value: "*"

    The response returns the following attributes: Name, ID, SourceType, AlarmClassName, Priority, EventText, AlarmText1, AlarmText2, AlarmText3, AlarmText4, AlarmText5, AlarmText6, AlarmText7, AlarmText8, AlarmText9, InfoText, Group, Origin, Area
  - Default: The response returns "AlarmClass", "Name" and "Area".
- `PageSize`: Optional

  Controls how many alarms a response returns.

  Default value: The configured page size is used. See also section [ReadConfig](#readconfig-rt-unified-1).
- `SystemNames`: Optional

  Controls from which system the alarms are read.

  - Value: "*"  
    All systems that communicate with each other via runtime collaboration
  - Value: Comma-separated list of systems that communicate with each other via runtime collaboration

    FOR EXAMPLE: "HMI_RT_1", "HMI_RT_2"
  - Default value: The local system
- `ClientCookie`:

  Value: Name of the response cookie

For example:

{"Message": "BrowseConfiguredAlarms", "Params": {"LanguageId": 1033, "Filter": "*alarm_*", "Attributes": ["Priority"], "PageSize": 50, "SystemNames": ["HMI_RT_1"], }, "ClientCookie": "myBrowseAlarmsRequest1"}

##### Next request

{"Message": "BrowseConfiguredAlarms", "Params": "Next", "ClientCookie": "<Cookie>"}

For example:

{"Message": "BrowseConfiguredAlarms", "Params": "Next", "ClientCookie": "myBrowseAlarmsRequest1"}

##### Response

**OnSuccess**

{"ClientCookie": "<Cookie>", "Message": "NotifyBrowseConfiguredAlarms", "Params": {"AlarmClasses":[{"AlarmClassName":"<Value>", "Alarms":[{"AlarmClassName":"<Value>", "Area":<Value>, "Name":<Value>, "Name":<Value>, "Priority":<Value>}, {"AlarmClassName":"<Value>", "Area":<Value>, ...}], {"AlarmClassName":"<Value>", "Alarms":[{"AlarmClassName": "<Value>, ...}]}

For example:

{"ClientCookie":"myBrowseAlarmsRequest1", "Message":"NotifyBrowseConfiguredAlarms", "Params":{"AlarmClasses":[{"Name":"HMI_RT_1::Warning",

"Alarms":[{"AlarmClassName":"HMI_RT_1::Warning", "Area":"HMI_RT_1::Alarming", "Name":"HMI_RT_1::Tag6:Analog_alarm_2", "Priority":12}, {"AlarmClassName":"HMI_RT_1::Warning",

"Area":"HMI_RT_1::Alarming", "Name":"HMI_RT_1::AlarmTag_1:Discrete_alarm_1", "Priority":12}]}]}}

**OnError**

{"Message": "ErrorBrowseConfiguredAlarms", "ErrorCode": "<Code>", "ErrorDescription": "<Description>", "ClientCookie": "Cookie>"}

For example:

{"Message": "ErrorBrowseAlarms", "ErrorCode": "-2165323798 / -2165322773", "ErrorDescription": "Invalid system name.", or “Your browse request has been expired”, "ClientCookie": "myBrowseAlarmsRequest1"}

#### BrowseAlarmClasses (RT Unified)

##### Description

The command "`BrowseAlarmClasses`" returns the alarm classes of the local HMI system or all HMI systems communicating via Runtime Collaboration.

Information on the general browse behavior of the command can be found in section [Behavior of the browse commands](#behavior-of-the-browse-commands-rt-unified).

**Request**

{"Message": "BrowseAlarmClasses", "Params": {"Filter": <String>, "Attributes"["<Attribute name>", ..., "<Attribute name>"], "SystemNames": ["<Name>", ..., "<Name>"]}, "ClientCookie": "<Cookie>"}

- `Filter`: Optional

  Restricts the command to alarm classes whose "Name" matches the filter.

  - Value: Filter string

    Permitted wildcards:

    | Wildcard | Description | Example |
    | --- | --- | --- |
    | * | Replaces 0 to more characters | Filter string: "*Alarm"   Alarm classes contained in the response:  - "Alarm" - "SystemAlarm" |
    | ? | Replaces 1 character | Filter string: "Alarm_Prio_?  Alarms contained in the response:  - "Alarm_Prio_1" - "Alarm_Prio_2" |
  - Default value: All alarm classes of the system specified by `SystemNames` are queried.
- `Attributes`: Optional

  Controls which attributes of the alarm class return the response:

  - Value: Comma-separated enumeration of attributes

    The response returns "Name" and "StateMachine" as well as the specified attributes.
  - Value: "*"

    The response returns the following attributes: Name, StateMachine, ID, Priority, NormalStateTextColor, NormalStateBackColor, RaisedStateTextColor, RaisedStateBackColor, RaisedStateFlashing, AcknowledgedStateTextColor, AcknowledgedStateBackColor, AcknowledgedStateFlashing, ClearedStateTextColor, ClearedStateBackColor, ClearedStateFlashing, AcknowledgedClearedStateTextColor, AcknowledgedClearedStateBackColor, AcknowledgedClearedStateFlashing
  - Default: The response returns "Name" and "StateMachine".
- `System`: Optional

  Controls from which system the tags are read.

  - Value: "*"

    All systems that communicate with each other via runtime collaboration
  - Value: Comma-separated list of systems that communicate with each other via runtime collaboration

    FOR EXAMPLE: "HMI_RT_1", "HMI_RT_2"
  - Default value: The local system

For example:

{"Message": "BrowseAlarmClasses", "Params": {"Filter": "*Alarm*", "SystemNames": ["HMI_RT_1"]}, "ClientCookie": "myBrowseAlarmClassRequest1"} //Browse for alarm classes in specified system with filter

**Response**

OnSuccess

NotifyBrowseAlarmClasses <System>::<Alarm class> ... <System>::<Alarm class>

For example:

NotifyBrowseAlarmClasses HMI_RT_1::Alarm HMI_RT_1::SystemNotification HMI_RT_1::SystemInformation HMI_RT_1::SystemAlarm HMI_RT_1::Notification HMI_RT_1::OperatorInputInformation

OnError

ErrorBrowseAlarmClasses <Error description>

For example:

ErrorBrowseAlarmClasses Invalid arguments passed to browsing function.

### Reference  (RT Unified)

The following section contains a reference of the properties of alarms and tags that you get with the commands ReadAlarm and ReadTag.

The commands transfer the property values as string.

#### Tag properties

**"Name" property**

Name of the tag

**"Value" property**

Value of the tag at the moment of the read operation.

**"Quality" property**

Quality of the read operation of the tag

Possible values:

- "Good"
- "Bad"
- "Uncertain"

**"QualityCode" property**

Quality code of the read operation of the tag

**"TimeStamp" property**

Time stamp of the last successful read operation of the tag

**"Error" property**

Error code of the last read or write operation of the tag

**"ErrorDescription" property**

Description of the error code of the last read or write operation of the tag

#### Alarm properties

**"InstanceID" property**

InstanceID for an alarm with multiple instances

**"SourceID" property**

Source at which the alarm was triggered.

**"Name" property**

Name of the alarm

**"AlarmClassName" property**

Name of the alarm class

**"AlarmClassSymbol" property**

Symbol of the alarm class

**"AlarmParameterValues" property**

Parameter values of the alarm

**"AlarmText1" … "AlarmText9" properties**

Additional texts 1-9 of the alarm

**"ChangeReason" property**

Trigger event of the modification of the alarm state

**"Connection" property**

Connection via which the alarm was triggered.

**"State" property**

Current alarm state

The property can contain the following values:

- "0": Normal
- "1": Raised
- "2": RaisedCleared
- "5": RaisedAcknowledged
- "6": RaisedAcknowledgedCleared
- "7": RaisedClearedAcknowledged
- "8": Removed

**"StateText" property**

Current alarm state as text, e.g. "active" or "inactive"

**"EventText" property**

Text that describes the alarm event.

**"InfoText" property**

Text that describes an operator instruction for the alarm.

**"TextColor" property**

Number with the text color of the alarm state

**"BackColor" property**

Number with the background color of the alarm state

**"Flashing" property**

Indicates whether the alarm flashes.

Values: "TRUE" or "FALSE"

**"ModificationTime" property**

Time of last modification to the alarm state

**"RaiseTime" property**

Trigger time of the alarm

**"AcknowledgementTime" property**

Time of alarm acknowledgment

**"ClearTime" property**

Time of alarm reset

**"ResetTime" property**

Time of alarm reset

**"SuppressionState" property**

Status of alarm visibility

**"SystemSeverity" property**

Severity of the system error

**"Priority" property**

Relevance for display and sorting of the alarm

**"Origin" property**

Origin for display and sorting of the alarm

**"Area" property**

Origin for display and sorting of the alarm

**"Value" property**

Current process value of the alarm

**"ValueQuality" property**

Quality of the process value of the alarm

**"ValueLimit" property**

Limit of the process value of the alarm

**"UserName" property**

User name of the operator control alarm

**"HostName" property**

Name of the host that triggered the alarm.

**"ID" property**

ID of the alarm that is also used in the display.

**"AlarmGroupID" property**

ID of the alarm group to which alarm belongs.

**"SourceType" property**

Source from which the alarm was generated, e.g. tag-based, controller-based or system-based alarm.

`HmiAlarmSourceType SourceType { get; }`

The enumeration "HmiAlarmSourceType" can contain the following values:

- `Undefined` (0)
- `Tag` (1)
- `Controller` (2)
- `System` (3)
- `Alarm` (4)

**"DeadBand" property**

Range of the triggering tag, in which no alarms are generated.

`object DeadBand { get; }`

**"LoopInAlarm" property**

Function that navigates from the alarm control to its origin.

`string LoopInAlarm { get; }`

**"NotificationReason" property**

Reason for the notification

The property can contain the following values:

- `"O": Unknown`
- `"1": Add`

  The alarm was added to the filtered result list. The alarm meets the filter criteria that apply to the monitoring.
- `"2": Modify`

  Properties of the alarm were changed, but the alarm is still part of the filtered result list.
- `"3": Remove`

  The alarm was part of the result list, but it no longer meets the filter criteria due to changes to its properties.

  > **Note**
  >
  > Changes to the alarms will not result in notifications until the alarm again meets the filter criteria. In this case, "NotificationReason" is set to `Add`.

> **Note**
>
> **Removing an alarm from business logic**
>
> The use case of the client determines whether the client ignores notifications via alarms with the "NotificationReason" `Modify` or `Remove`.
>
> For example:
>
> - State-based monitoring: The client wants to show a list of incoming alarms. All notification reasons are relevant. The client removes an alarm from the list as soon as the notification reason is `Remove`.
> - Event-based monitoring: The client wants to send an email when an alarm comes in. Only the notification reason `Add` is relevant.

Example:

A customer application begins monitoring with the filter criterion "State" = 1. An alarm is triggered. Runtime notifies the customer application of the "NotificationReason" as follows:

| NotificationReason | Description |
| --- | --- |
| Add | - The "State" property is 1. The alarm is active. |
| Modify | - The "State" property has not changed. - Another property that is not part of the filter criterion has changed, e.g. "Priority". |
| Remove | The "State" property has changed, e.g. alarm is inactive. |

**"Duration" property**

Returns the time interval in nanoseconds between triggering of the alarm and its previous status change.

### Syntax of the alarm filter (RT Unified)

With an AlarmSubscription, a filter can be transferred so that not all active alarms of the alarm system are notified, but only those which match the filter. The filter syntax is based on SQL syntax. However, only the WHERE instruction is relevant. The keyword "WHERE" must be omitted.

#### Operators

The following operators can be used in the filter string of the alarm filter:

| Operator | Description | Example |
| --- | --- | --- |
| `=` | equal to | `Name = 'Recipe246'` |
| `<>` | not equal | `Value <> 0.0` |
| `>` | greater than | `Value > 25.0` |
| `<` | less than | `Value < 75.0` |
| `>=` | greater than or equal to | `Value >= 25.0` |
| `<=` | less than or equal to | `Value <= 75.0` |
| `OR, ||` | logical OR | `State = 1 OR State = 3` |
| `AND, &&` | logical AND | `Value >= 25.0 AND Value <= 75.0` |
| `BETWEEN` | within a range | `Value BETWEEN 25.0 AND 75.0` |
| `NOT BETWEEN` | outside a range | `Value NOT BETWEEN 25.0 AND 75.0` |
| `LIKE string` | corresponds to the string string | `Name LIKE 'Motor*'` |
| `NOT LIKE string` | does not correspond to the string string | `Name NOT LIKE 'Valve*'` |
| `IN (v1, v2, …)` | corresponds to one or more values | `State IN (1, 4, 7)` |
| `NOT IN (v1, v2, …)` | does not correspond to one or more values | `State NOT IN (0, 2, 3, 5, 6)` |
| `(…)` | brackets expressions | `Value <= 75.0 AND (State = 1 OR State = 3)` |

Precedence of the operators:

| Rank | Operators |
| --- | --- |
| 1 | - Relational operators:   =, <>, >, <, >=, <= - LIKE - IN - BETWEEN |
| 2 | NOT |
| 3 | AND, && |
| 4 | OR, || |

Permitted wildcards:

| Wildcard | Description | Example |
| --- | --- | --- |
| * | Replaces 0 to more characters | `Name LIKE ‘Motor*’`     `Reference = <1.*.15>1` |
| ? | Replaces 1 character | `Name = ‘Recipe?’` |
