---
title: "WinCC Unified GraphQL (RT Unified)"
package: GQLWCCUenUS
topics: 68
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Unified GraphQL (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified)
- [Basics (RT Unified)](#basics-rt-unified)
- [Quick start (RT Unified)](#quick-start-rt-unified)
- [Schema (RT Unified)](#schema-rt-unified)
- [Reference of GraphQL API (RT Unified)](#reference-of-graphql-api-rt-unified)
- [Code examples (RT Unified)](#code-examples-rt-unified)
- [Recommended procedures (RT Unified)](#recommended-procedures-rt-unified)
- [Troubleshooting (RT Unified)](#troubleshooting-rt-unified)

## Introduction (RT Unified)

### WinCC Unified GraphQL API

GraphQL API is a web-based interface for implementing applications (GraphQL clients) that have read and write access to runtime data.

### Functional scope

GraphQL provides you with the following functions to access Runtime:

| Tags | Active alarms | Logged alarms | Configured alarms |
| --- | --- | --- | --- |
| - Read process value - Write process value - Subscribe to changes | - Read - Subscribe to changes - Acknowledge / reset | - Read | - Activate / deactivate - Unshelve alarm - Acknowledging all active alarm instances |

### Benefits

Use of Unified GraphQL clients offers the following benefits:

- High user-friendliness, easy integration and few dependencies
- Growing prevalence of GraphQL
- No installation of Unified Runtime on the developer device and when operating the client application
- GraphQL API can be used by all applications that access a network via HTTP and WebSockets (e.g. web applications, desktop applications, console applications).
- You can integrate ready-to-use GraphQL client libraries for a variety of programming languages into your project.

  You can easily extend these libraries through a user-defined GraphQL layer.
- There are ready-to-use GraphQL clients you can use to execute GraphQL operations without having to develop them yourself. An example is the Apollo client used in the quick start section of this user help.
- Built-in API documentation that is available online and always up-to-date
- Precise control of the client over the data processed and transferred by the server

### Technical details

- HTTP and WebSockets are the transport layer for client operations and server responses.
- The operations and responses use a JSON-based format.
- The structure of client queries and server responses is described by a schema.
- Each operation specifies a selection set. Only the attributes specified in the selection set are contained in the server response.

## Basics (RT Unified)

This section contains information on the following topics:

- [Limitations (RT Unified)](#limitations-rt-unified)
- [Security (RT Unified)](#security-rt-unified)
- [Escaping (RT Unified)](#escaping-rt-unified)
- [More information (RT Unified)](#more-information-rt-unified)

### Limitations (RT Unified)

Unified GraphQL API is subject to the following limitations:

- The GraphQL interface supports only Unified PC.
- Access is limited to the runtime to which the GraphQL client is logged in. Access to HMI devices connected via Runtime Collaboration is not possible.
- In the existing version of Unified GraphQL, several alarm properties cannot be used as a filter in `activeAlarms` subscriptions and `acitveAlarms` queries.

  For a list of these alarm properties, see section [Filtering alarms](#filtering-alarms-rt-unified).
- The maximum length of client requests is 1 MB.

  If this limit is exceeded, the GraphQL server responds with error code 413 (PayloadTooLargeError).

### Security (RT Unified)

This section provides security-relevant information on the GraphQL server.

#### Secure communication via IIS web server

To ensure secure communication and to protect the GraphQL server and runtime, the GraphQL server is accessed via the IIS web server of Unified Runtime.

Direct access to GraphQL is not supported.

#### Session duration

A session between the GraphQL server and GraphQL client remains open as long as there is activity, e.g. a regularly executed query.

All sessions of all users are closed in the following cases:

- Start of the GraphQL server with a different manager number
- Deletion of the internal session database

#### Closing all sessions of a user

You have the following options:

- The user logs out from one of his sessions and, in so doing, passes the value `True` for parameter `allSessions`.
- The administrator changes the password of the user in the engineering system. The administrator logs in to GraphQL with the changed login data of the user. The administrator logs the user out and, in so doing, passes the value `True` for parameter `allSessions`.

#### Access control

The access of GraphQL clients to Runtime can be restricted as follows:

- Linking access to function rights

  An operation of the GraphQL client is only executed if the user who is logged on at the client has the required rights.  
  Read permission is required for queries and subscriptions, write permission for mutations.
- Controlling access to the object level

  The read access and write access of the user logged on at the GraphQL client is defined per object:

  - Read access to an object without authorization: The object is removed from the server response.
  - Write access to an object without authorization: The operation is aborted.

### Escaping (RT Unified)

Attribute values and object names, for example of tags or alarms, may contain special characters which are escape sequences in the Runtime system or the programming language of the GraphQL client. Escape sequences do not represent a text but start a special function during the program execution.

To ensure that a special character is interpreted as a normal character, prefix the character in the GraphQL client program code with a masking character (EN: Escaping).

> **Note**
>
> **Masking character**
>
> Runtime system: $
>
> Apollo Studio: \

If a special character is an escape sequence in the Runtime system and the programming language, combine the masking characters.

**Example**

The character " is an escape sequence in the Runtime system and Apollo Studio. To, for example, address a tag with the name MOT1" enter the following string: MOT1$\"

### More information (RT Unified)

You can find more information on GraphQL here:

- About GraphQL in general: <https://graphql.org/>
- About Apollo Studio: <https://www.apollographql.com/>
- Solutions to technical problems concerning GraphQL: <https://stackoverflow.com/>

## Quick start (RT Unified)

This section contains information on the following topics:

- [Purpose of this quick start (RT Unified)](#purpose-of-this-quick-start-rt-unified)
- [Requirements (RT Unified)](#requirements-rt-unified)
- [Setting up the GraphQL client (RT Unified)](#setting-up-the-graphql-client-rt-unified)
- [Logging in to the GraphQL server (RT Unified)](#logging-in-to-the-graphql-server-rt-unified)
- [Executing a GraphQL operation (RT Unified)](#executing-a-graphql-operation-rt-unified)
- [Authorizing an operation request (RT Unified)](#authorizing-an-operation-request-rt-unified)
- [Using the syntax highlighting and autocompletion functions of Apollo (RT Unified)](#using-the-syntax-highlighting-and-autocompletion-functions-of-apollo-rt-unified)

### Purpose of this quick start (RT Unified)

This quick start demonstrates, using a ready-to-use GraphQL client freely available in Apollo Studio, how to establish a connection to a Unified GraphQL server, log in to runtime and then query, manipulate and subscribe to runtime data.

The quick start sets you up for subsequent experimentation with the GraphQL client of Apollo and helps you to get started working with WinCC Unified GraphQL.

### Requirements (RT Unified)

To follow the instructions and examples of the quick start, the following general requirements must be met:

- WinCC Unified Runtime is installed on a PC.
- A runtime project is running on the PC.
- The GraphQL Server Manager on this PC is effective via IIS through: **https://localhost/graphql/**

---

**See also**

[Setting up the GraphQL client (RT Unified)](#setting-up-the-graphql-client-rt-unified)

### Setting up the GraphQL client (RT Unified)

#### Procedure

1. Start a web browser on a device that has access to the runtime server.
2. Enter the following address in the address line and press Enter:

   <https://studio.apollographql.com/sandbox/explorer>

   Apollo Studio opens:

   ![Procedure](images/159361952139_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/159361952139_DV_resource.Stream@PNG-de-DE.png)
3. Click on the gear icon in the address line.

   The configuration settings for the GraphQL client open. Apply the following settings:

   ![Procedure](images/159362844683_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/159362844683_DV_resource.Stream@PNG-de-DE.png)

   Schema introspection is active for Unified GraphQL Server. That is why you see a green dot in the address line after configuration of the GraphQL client. In addition, the documentation of the GraphQL API is available in the client:

   ![Procedure](images/159362854155_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/159362854155_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Requirements (RT Unified)](#requirements-rt-unified)
  
[Basics on the schema (RT Unified)](#basics-on-the-schema-rt-unified)

### Logging in to the GraphQL server (RT Unified)

> **Note**
>
> For information on the SWAC login, see section ["loginSWAC" mutation](#loginswac-mutation-rt-unified).

In order for a GraphQL client to access runtime data, it must be logged in to Runtime with a user.

#### Requirement

In addition to the general requirements, the following is required:

- The GraphQL server has been set up.

#### Procedure

1. Log the GraphQL client in to the GraphQL server by calling the mutation `login`, as shown below.

   Pass the login data of a UMC user configured for runtime to the operation as input parameter.

#### Result

The server opens a session. The server response contains the ID of the authorization token:

![Result](images/159367939851_DV_resource.Stream@PNG-de-DE.png)

You use this token for subsequent requests of GraphQL operations. If the client has been inactive for a while, the token expires. The client must log in again.

> **Note**
>
> By requesting the `extendSession`mutation, you keep the session open in spite of inactivity.

---

**See also**

[Requirements (RT Unified)](#requirements-rt-unified)
  
[Setting up the GraphQL client (RT Unified)](#setting-up-the-graphql-client-rt-unified)
  
[Authorizing an operation request (RT Unified)](#authorizing-an-operation-request-rt-unified)
  
["login" mutation (RT Unified)](#login-mutation-rt-unified)
  
["extendSession" mutation (RT Unified)](#extendsession-mutation-rt-unified)

### Executing a GraphQL operation (RT Unified)

#### Requirement

In addition to the general requirements, the following is required:

- The GraphQL server has been set up.
- The GraphQL client is logged in to the server. The authorization token issued at login is still valid.
- The user with whom the GraphQL client is logged in has the following function rights:

  - Query or subscription: "GraphQL - read access" or "GraphQL - read/write access"
  - Mutation: "GraphQL - read/write access"

#### Procedure

To execute GraphQL operations for a Unified GraphQL client, proceed as described below. The basic procedure is the same for all three operation types.

1. In Apollo Studio, select the Explorer view and input the desired operation in the "Operation" panel.

   You have the following options:

   - Manually entering the operation request in the panel
   - Pointing the mouse to the desired position in the panel, changing to the Documentation view, selecting the desired operation there and adding it with the "+" icon
2. Specify the input parameters.

   You have the following options:

   - Manually passing the parameters in the operation request:

     ![Procedure](images/159364156427_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/159364156427_DV_resource.Stream@PNG-de-DE.png)
   - Creating a tag in the "Variables" panel and using it in the "Operation" panel. For this you enter the character "`$`" followed by the tag name in the "Operation" panel:

     ![Procedure](images/159366777099_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/159366777099_DV_resource.Stream@PNG-de-DE.png)
3. In the "Headers" panel, define additional HTTP header values, e.g. obligatory authorization tokens for access to tags and active alarms.
4. Click the button for executing the operation.

**Note**

**Tag as input parameter**

Ensure that the tag exists in the connected runtime and that the tag name is written correctly.

#### Result

- The operation is executed.
- If the client is logged in, you see the response of the GraphQL server in the "Response" panel.

  If the client is not logged in, you see a corresponding error message in the "Response" panel.

#### Examples for the various operation types

- Query type:

  ![Examples for the various operation types](images/159464717707_DV_resource.Stream@PNG-de-DE.png)
- Mutation type:

  ![Examples for the various operation types](images/159466032779_DV_resource.Stream@PNG-de-DE.png)

  If you execute a query for the tag after the mutation, you receive the modified value.
- Subscription type:

  ![Examples for the various operation types](images/159467104651_DV_resource.Stream@PNG-de-DE.png)

  If you execute a mutation for the tag after the subscription, you receive a notification.

#### Closing a subscription

To close a subscription, click "X" button in the "Subscriptions" panel.

> **Note**
>
> **Subscriptions in Apollo Studio**
>
> There is only one active subscription in the GraphQL client in Apollo Studio. If you start a second subscription, it replaces the first one. The second subscription is then the active subscription.

---

**See also**

[Requirements (RT Unified)](#requirements-rt-unified)
  
[Authorizing an operation request (RT Unified)](#authorizing-an-operation-request-rt-unified)

### Authorizing an operation request (RT Unified)

#### Requirement

In addition to the general requirements, the following is required:

- The GraphQL server has been set up.
- The GraphQL client is logged in to the server. The authorization token issued at login is still valid.
- The desired operation is displayed in the "Operation" panel.

#### Procedure

1. Select the "Headers" panel of the operation.
2. Add a header if necessary.
3. Enter the following header data:

   - Key: "Authorization"
   - Value: "Bearer <Token ID from the login response>"
4. Activate the header.

   ![Procedure](images/159397435275_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/159397435275_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Requirements (RT Unified)](#requirements-rt-unified)
  
[Executing a GraphQL operation (RT Unified)](#executing-a-graphql-operation-rt-unified)
  
[Logging in to the GraphQL server (RT Unified)](#logging-in-to-the-graphql-server-rt-unified)

### Using the syntax highlighting and autocompletion functions of Apollo (RT Unified)

#### Introduction

This section describes how to integrate the Apollo GraphQL extension for syntax highlighting and autocompletion into Visual Studio Code.

#### Procedure

1. Download the Apollo GraphQL extension from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=apollographql.vscode-apollo).
2. Install it.
3. Apply the following settings:

   ![Procedure](images/159713235595_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/159713235595_DV_resource.Stream@PNG-de-DE.png)

#### Result

When the schema inspection of the GraphQL server is active and the GraphQL server is running, Visual Studio supports you with additional features.

Example:

- Hover the mouse pointer over a GraphQL code. A tooltip with additional information opens:

  ![Result](images/159723406219_DV_resource.Stream@PNG-de-DE.png)
- When entering GraphQL code, you receive autocomplete suggestions:

  ![Result](images/159723397643_DV_resource.Stream@PNG-de-DE.png)

## Schema (RT Unified)

This section contains information on the following topics:

- [Basics on the schema (RT Unified)](#basics-on-the-schema-rt-unified)
- [Structure of a client query (RT Unified)](#structure-of-a-client-query-rt-unified)

### Basics on the schema (RT Unified)

The GraphQL schema is an object in JSON format that describes the GraphQL API, which is understandable by humans and applications alike.

If the schema of the GraphQL server is known to the GraphQL client, the client supports you with autocompletion and syntax checking.

In Apollo Studio, you can see that the client knows the schema by the green dot in the address bar. The documentation of the GraphQL API is then available in the client:

![Figure](images/159362854155_DV_resource.Stream@PNG-de-DE.png)

#### Automatically querying the schema

The schema inspection is active for GraphQL server by default. Therefore, GraphQL clients automatically query the schema from the server.

#### Manually downloading the schema

You can also download the schema manually, e.g. by executing the following npx command in the Windows command line:

npx apollo-cli download-schema http://localhost:4000/graphql --output schema.json

More information on the manual download of the schema can be found [here](https://stackoverflow.com/questions/37397886/get-graphql-whole-schema-query).

#### Syntax highlighting and autocompletion in editors

To make use of syntax highlighting and autocompletion in editors when implementing a GraphQL client, extensions suitable for the development environment must be installed. For example, you can install the Apollo GraphQL extension for Visual Studio Code.

See also [Using the syntax highlighting and autocompletion functions of Apollo](#using-the-syntax-highlighting-and-autocompletion-functions-of-apollo-rt-unified).

### Structure of a client query (RT Unified)

#### Overview

1 query  
2 {  
3 tagValues(names: "DEMO_CPU_TEMPERATURE")   
4 {  
5 value   
6 {  
7 value  
8 timestamp  
9 quality  
10 {  
11 quality  
12 }  
13 }  
14 error  
15 {  
16 code  
17 description  
18 }  
19 }  
20 }

| Line | Description |
| --- | --- |
| 1 | The operation type of the requested operation, in this example: `query` |
| 3 | Name of the requested operation and list of input parameters in the following format:  (<Name_Parameter1>: "<Value>", <Name_Parameter2>: "<Value>") |
| 4 to 19 | The selection set with the attributes requested from the server |

> **Note**
>
> **Order of requested attributes in the server response**
>
> The server response returns the attributes requested by the selection set in the same order as specified in the selection set of the client request.

#### Structure of the selection set

The selection set is where you specify for the operation request which attributes the server returns. You can request all the attributes defined in the return type of the operation.

Notation:  
`Operation name ( <Input parameter>) {<Selection set> }`

Where <Selection set> stands for a comma-separated list of the attribute names requested by the server.

Specification of type-based attributes:   
<Name of type-based attribute> { <Comma-separated list of attribute names> }

Example of type-based attributes: The attributes `value`, `quality` and `error` from the selection set above.

> **Note**
>
> **Order of attributes in the server response**
>
> The server returns the attributes in its response in the same order as requested in the selection set of the client request.

## Reference of GraphQL API (RT Unified)

This section contains information on the following topics:

- [General information on GraphQL API (RT Unified)](#general-information-on-graphql-api-rt-unified)
- [GraphQL operation types (RT Unified)](#graphql-operation-types-rt-unified)
- [Operations for tags (RT Unified)](#operations-for-tags-rt-unified)
- [Operations for alarms (RT Unified)](#operations-for-alarms-rt-unified)
- [Other operations (RT Unified)](#other-operations-rt-unified)
- [Reference for Unified-specific types and enumerations (RT Unified)](#reference-for-unified-specific-types-and-enumerations-rt-unified)

### General information on GraphQL API (RT Unified)

An important feature of GraphQL API is its high user-friendliness. For Unified GraphQL API, this means:

- Tags and active alarms from runtime are addressed using their name and not their ID.

  The names are configured in the engineering.
- QualityCodes are represented by the string assigned to them in an enumeration. This improves readability of the code.
- Color values are translated to the standard RGBA notation.
- Date information is represented according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).
- To execute bulk operations, it is possible to pass GraphQL operations as input parameter lists.

  The operation is then applied to each list element.
- Internal error messages are translated into user-level messages.

### GraphQL operation types (RT Unified)

#### Overview

GraphQL operations have one of the following operation types:

- Query
- Mutation
- Subscription

#### Queries

You use queries for read operations. The query sends an HTTPS request to the GraphQL server.

Example: Querying tag values or alarms that satisfy a filter criterion

#### Mutations

You use mutations for write operations. The mutation sends a one-time query to the GraphQL server.

Example: Writing the value and QualityCode of the value to a tag

#### Subscriptions

You use subscriptions so that your GraphQL client can react to runtime events promptly without having to continually query the runtime status. The subscription creates a permanent WebSocket connection between the GraphQL server and client. When a client subscribes to an alarm or tag, the server notifies the client when changes to the alarm or tag are active.

Example: The GraphQL client is to execute a certain operation when the value of a tag changes.

Subscriptions are usually closed by the client, but they can also be closed by the server or mutually by both sides, e.g. in the event of a network failure.

Subscriptions use the graphql-transport-ws protocol. Configure this protocol for your GraphQL library or implement WebSocket communication based on this protocol.

Client-side GraphQL libraries provide different options for closing subscriptions, depending on the programming language being used. For example, Python uses an asynchronous iterator that the notification runs through. When the loop is exited, the subscription is closed.

---

**See also**

[Disconnection by server (RT Unified)](#disconnection-by-server-rt-unified)

### Operations for tags (RT Unified)

This section contains information on the following topics:

- ["tagValues" query (RT Unified)](#tagvalues-query-rt-unified)
- ["writeTags" mutation (RT Unified)](#writetags-mutation-rt-unified)
- ["tagValues" subscription (RT Unified)](#tagvalues-subscription-rt-unified)

#### "tagValues" query (RT Unified)

##### Requirements

- The user who is logged in to runtime for the GraphQL client has the rights "GraphQL - read access" or "GraphQL - read/write access" in runtime.

##### Description

tagValues(names: [String]): [TagValueResult]

| Symbol | Meaning |
| --- | --- |
| Operation name | `tagValues` |
| Operation type | `query` |
| Function | Reads the tags specified in input parameter `names`.  Read access is possible to tags with a simple data type, as well as to elements of structure tags and arrays with a simple data type. |
| Input parameters | `names`   - Mandatory parameter - Data type: String - List of names of the tags whose properties you want to read.   Notation: `names:["``<Name Tag1>``", "``<Name Tag2>``", "``<...>``"]`   Example: `names:["motor1.tempMax", "motor1.tempMin"]`   Addressing of tags:   - Addressing a tag with simple data type: `<Tag name>`   - Addressing an element of a structure tag: `<Structure tag name>.<Element name>` Example: `motor1.speed`   - Addressing an individual element of an array: `<Array name>[<Index>]` Example: `FloatArrayTag[0]`   - Address all tags of an array: `<Array name>`     Example: `FloatArrayTag` The tags are returned in an array in the response. |
| Selection set | Mandatory specification  Specify which attributes the server returns for the queried tags. You can request the attributes defined in the `TagValueResult` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |
| Server response | Supplies the attributes requested in the selection set for all tags specified with `names` as key-value pairs of a JSON data record. |
| Error messages (`code`: `description`) | - `0:`    `Success` - `2:`    `Cannot resolve provided name` - `202:`    `Only leaf elements of a Structure Tag can be addressed` |

##### Example

`query exampleTagQuery{`

`tagValues(names:[“ExampleTagName1”, “ExampleTagName2”]){`

`name`

`value{`

`value`

`timestamp`

`quality`

`{`

`quality`

`subStatus`

`}`

`}`

`error{`

`description`

`code`

`}`

`}`

`}`

---

**See also**

["TagValueResult" type (RT Unified)](#tagvalueresult-type-rt-unified)

#### "writeTags" mutation (RT Unified)

##### Requirements

- The user who is logged in to runtime for the GraphQL client has the right "GraphQL - read/write access" in runtime.

##### Description

writeTagValues(  
 input: [TagValueInput],   
 timestamp: Timestamp  
 quality: QualityInput  
 ): [WriteTagValuesResult]

| Symbol | Meaning |
| --- | --- |
| Operation name | `writeTagValues` |
| Operation type | `mutation` |
| Function | Writes the tags specified in input parameter `input`.  Write access is possible to tags with a simple data type, as well as to elements of structure tags and arrays with a simple data type.  The mutation allows you to write multiple tags or multiple properties of the same tag with a single operation request. |
| Input parameters | `input`   - Mandatory parameter - Data type: String - A list of the tags and values that you want to write   Notation: `input:[ {<``Information on tag 1``>}, {<``Information on tag 2``>},{<...>}]`   Example: `input: [{name: "motor1.speed", value: "100"}, {name: "motor2.speed", value: "140"}]`   Make the following entries for each tag:   - `name`: For addressing the tag     Addressing a tag with simple data type: `<Tag name>`     Addressing an element of a structure tag: `<Structure tag name>.<Element name>` Example: `motor1.speed`     Addressing an individual element of an array: `<Array name>[<Index>]` Example: `FloatArrayTag[0]`     It is not possible to address all elements of an array together.   - `value`: The process value that is written to the tag     The data type of the passed value must be convertible to the data type of the tag.   - (Optional) `timestamp`: The time stamp of the process value as `Timestamp`<sup>1</sup>   - (Optional) `quality`: The QualityCode of the process value as `QualityInput`    `timestamp`   - Optional   Written to all tags from `input` for which no time stamp has been passed.<sup>1</sup>   If the input parameter is empty, the current system time is used as the time stamp. - Data type: `Timestamp`    `quality`   - Optional   Written to all tags from `input` for which no QualityCode has been passed.   If the input parameter is empty, "GOOD" is used as QualityCode. - Data type: `QualityInput` |
| Selection set | Mandatory specification  Specify which attributes the server returns for the written tags. You can request the attributes defined in the `WriteTagValueResult` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |
| Server response | Supplies the attributes requested in the selection set for all tags specified with `input` as key-value pairs of a JSON data record. |
| Error messages (`code`: `description`) | - `0:`    `Success` - `2:`    `Cannot resolve provided name` - `201:`    `Cannot convert provided value to data type` - `202:`    `Only leaf elements of a Structure Tag can be addressed` |
| <sup>1</sup> The timestamp must be newer that the current timestamp of the tag and must not be in the future. |  |

##### Example

`mutation exampleTagValueWrite {`

`writeTagValues(input:[`

`{`

`name:"ExampleStringTag",`

`value: "Example value text”`

`},`

`{`

`name:"ExampleIntegerTag",`

`value: 42,`

`timestamp:"2022-07-26T06:25:15Z"`

`}`

`], quality:{quality: GOOD_NON_CASCADE}){`

`name`

`error{`

`code`

`description`

`}`

`}`

`}`

---

**See also**

["WriteTagValueResult" type (RT Unified)](#writetagvalueresult-type-rt-unified)
  
["QualityInput" type (RT Unified)](#qualityinput-type-rt-unified)

#### "tagValues" subscription (RT Unified)

##### Requirements

- The user who is logged in to runtime for the GraphQL client has the rights "GraphQL - read access" or "GraphQL - read/write access" in runtime.
- The WebSocket protocol has been activated.

  > **Note**
  >
  > The WebSocket protocol is not activated by WinCC Unified Setup. Activate it manually if necessary: "Enable or Disable Windows Features > Internet Information Services > WWW Services > Application Development Features > WebSocket Protocol".

##### Description

tagValues(names: [String]): TagValueNotification

| Symbol | Meaning |
| --- | --- |
| Operation name | `tagValues` |
| Operation type | subscription |
| Function | Subscribes the tags specified in input parameter `names`. |
| Input parameters | `names`   - Mandatory parameter - Data type: String - List of names of the tags whose properties you want to subscribe to.   Notation: `names:["``<Name Tag1>``", "``<Name Tag2>``", "``<...>``"]`   Addressing of tags:   - Address an element of a structure tag: `<Name of the structure tag>.<Name of the element>`   - Address a single element of an array: `<Name of the array>[<Index>]`     Example: `FloatArrayTag[0]`   - Address all tags of an array: `<Name of the array>`     Example: `FloatArrayTag` The tags are returned in an array in the response. |
| Selection set | Mandatory specification  Specify which attributes the server returns for the subscribed tags. You can request the attributes defined in the `TagValuesNotification` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified).  Recommendation: Request `name` and `notifcationReason`. |
| Server response | Until the subscription is closed, supplies an initial notification for the subscribed tags with the current values of the attributes requested in the selection set as key-value pairs of a JSON data record, and supplies subsequent notifications when a subscribed tag changes. |
| Error messages (`code`: `description`) | - `0:`    `Success` - `2:`    `Cannot resolve provided name` - `202:`    `Only leaf elements of a Structure Tag can be addressed` |

##### Closing a subscription

The subscription of a tag closes implicitly:

- When the tag is renamed.
- When the tag is deleted.

When you close the subscription in the GraphQL client explicitly, all previously subscribed tags are no longer subscribed.

##### Example

`subscription subscription{`

`tagValues(names:["Example_Tag_1", "Example_Tag_2"]){`

`name`

`value{`

`value`

`timestamp`

`quality{`

`quality`

`substatus`

`}`

`}`

`error{`

`code`

`description`

`}`

`notificationReason`

`}`

`}`

---

**See also**

["TagValueNotification" type (RT Unified)](#tagvaluenotification-type-rt-unified)

### Operations for alarms (RT Unified)

This section contains information on the following topics:

- ["activeAlarms" query (RT Unified)](#activealarms-query-rt-unified)
- ["loggedAlarms" query (RT Unified)](#loggedalarms-query-rt-unified)
- [Mutations "acknowledgeAlarms" and "resetAlarms" (RT Unified)](#mutations-acknowledgealarms-and-resetalarms-rt-unified)
- [Mutations "enableAlarms" and "disableAlarms" (RT Unified)](#mutations-enablealarms-and-disablealarms-rt-unified)
- [Mutations "shelveAlarms" and "unshelveAlarms" (RT Unified)](#mutations-shelvealarms-and-unshelvealarms-rt-unified)
- ["activeAlarms" subscription (RT Unified)](#activealarms-subscription-rt-unified)
- [Filtering alarms (RT Unified)](#filtering-alarms-rt-unified)

#### "activeAlarms" query (RT Unified)

##### Requirements

- The user who is logged in to runtime for the GraphQL client has the rights "GraphQL - read access" or "GraphQL - read/write access" in runtime.

##### Description

activeAlarms(  
 systemNames: [String]  
 filterString: String  
 filterLanguage: String  
 languages: [String]  
 ): [ActiveAlarm]

| Symbol | Meaning |
| --- | --- |
| Operation name | `activeAlarms` |
| Operation type | `query` |
| Function | Queries the active alarms from the server. |
| Input parameters | `systemNames`   - Optional - Data type: String - Reserved for future versions. - Specifies the runtime whose alarms are queried.   In the current version, the queried alarms are always the alarms of the runtime connected to the GraphQL server.    `filterString`   - Optional - Data type: String - Defines filter criteria for the alarms. See section [Filtering alarms](#filtering-alarms-rt-unified).   If you do not define a filter, the server returns all alarms active in runtime.    `filterLanguage`   - Optional - Data type: String - When `filterString` uses a string with a translatable alarm property, you use `filterLanguage` to define which language is used for the comparison.<sup>1</sup> - Default value: "en-US"    `languages`   - Optional - Data type: String array - Defines the languages in which the server returns the texts of translatable alarm properties and the order of the requested languages.<sup>1</sup>   Example:    `queryLanguageExample { activeAlarms(languages:["en-US", "de-DE"] { name, eventText, alarmText1, alarmClassName, state, raiseTime, priority } }`    The server response supplies the attributes specified in the selection set for the queried alarms. Translatable properties, such as `eventText`, are each returned in a string array. The element with index 0 always contains the English text and the element with index 1 the German text. - Default value: "en-US" |
| Selection set | Mandatory specification  Specify which attributes the server returns for the queried alarms. You can request the attributes defined in the `ActiveAlarm` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |
| Server response | Supplies the attributes requested in the selection set for the queried alarms as key-value pairs of a JSON data record. |
| Error messages (`code` and `description`) | - `0:`    `Success` - `301:`    `Syntax error in query string` - `302:`    `At least one of the requested languages is invalid` - `303:`    `The provided filter language is invalid` |
| <sup>1</sup> Languages must be specified in ISO language code format (e.g. "en-US", "de-DE"). Note that the entry is case-sensitive. |  |

##### Example

`query exampleAlarmQuery`

`{`

`activeAlarms(languages:["en-US", "de-DE"],  
 filterLanguage:"en-US",  
 filterString:(raiseTime <= '2022-07-26T09:00' AND userName LIKE '* Doe') OR priority > 2")`

`{`

`name`

`eventText`

`alarmText1`

`alarmClassName`

`state`

`raiseTime`

`priority`

`}`

`}`

---

**See also**

["ActiveAlarm" and "ActiveAlarmNotification" types (RT Unified)](#activealarm-and-activealarmnotification-types-rt-unified)
  
["Error" type (RT Unified)](#error-type-rt-unified)

#### "loggedAlarms" query (RT Unified)

##### Requirement

- The user who is logged in to runtime for the GraphQL client has the rights "GraphQL - read access" or "GraphQL - read/write access" in runtime.

##### Description

loggedAlarms(  
 systemNames: [String]  
 filterString: String  
 filterLanguage: String  
 languages: [String]  
 startTime: Timestamp  
 endTime: Timestamp  
 maxNumberOfResults: Int  
 ): [LoggedAlarm]

| Symbol | Meaning |
| --- | --- |
| Operation name | `loggedAlarms` |
| Operation type | `query` |
| Function | Queries the logged alarms from the server. |
| Input parameters | `systemNames`:  - Optional - Corresponding to the query `activeAlarms`    `filterString`, `filterLanguage`, `languages`:   - Optional - Corresponding to the query `activeAlarms`   To filter the logged alarms on the basis of the attributes defined in the type `LoggedAlarm`.    `startTime`, `endTime`:   - Optional - For filtering   Restricts the query to logged entries whose alarm status was changed the last time within the time frame defined by `startTime` and `endTime`. - Data type: `Timestamp`    `maxNumberOfResults`   - Optional - Upper limit for the number of the requested alarm entries - Data type: Int |
| Selection set | Mandatory specification  Specify which attributes the server returns for the queried logged alarms. You can request the attributes defined in the `LoggedAlarm` type.   For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |
| Server response | Supplies the attributes requested in the selection set for the queried logged alarms as key-value pairs of a JSON data record. |
| Error messages (`code` and `description`) | - `0:`    `Success` - `301:`    `Syntax error in query string` - `302:`    `At least one of the requested languages is invalid (or not logged)` - `303:`    `The provided filter language is invalid (or not logged)` |

---

**See also**

[Type "LoggedAlarm" (RT Unified)](#type-loggedalarm-rt-unified)

#### Mutations "acknowledgeAlarms" and "resetAlarms" (RT Unified)

##### Introduction

You have the following options:

- Acknowledging or resetting all active alarms of one or more configured alarms.
- Acknowledging or resetting specific alarm instances of one or more configured alarms.

> **Note**
>
> **Alarms without group acknowledgment or group reset**
>
> The configuration of a configured alarm can prevent a group acknowledgment or group reset. In this case you have to acknowledge or reset each alarm instance in an own operation call.
>
> The execution of `acknowledgeAlarms` and `resetAlarms` aborts when the operation for two or more configured alarms is called and one of the alarms does not allow group acknowledgment or group reset.

##### Requirement

- The user who is logged in to runtime for the GraphQL client has the right "GraphQL - read/write access" in runtime.
- The state machine of the alarms specified in the `input` parameter requires acknowledgement or acknowledgement and confirmation of the alarms.

##### Description

acknowledgeAlarms(  
 input: [AlarmIdentifierInput]  
 ): [ActiveAlarm]

resetAlarms(  
 input: [AlarmIdentifierInput]  
 ): [ActiveAlarm]

|  |  |  |
| --- | --- | --- |
| Operation name | `acknowledgeAlarms` | `resetAlarms` |
| Operation type | `mutation` |  |
| Function | Acknowledges the active alarms specified in the input parameter `input`. | Resets the alarms specified in the input parameter `input` . |
| Input parameters | `input`:  - Mandatory parameter - Data type: `[AlarmIdentifierInput]` - Specifies the alarms to be acknowledged or reset |  |
| Selection set | Mandatory specification  Specify which attributes the server returns for the queried alarms. You can request the attributes defined in the `ActiveAlarm` type.   For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |  |
| Server response | Supplies the attributes requested in the selection set for the alarms as key-value pairs of a JSON data record. |  |
| Error messages (`code` and `description`) | - `0:`    `Success` - `2:`    `Cannot resolve provided name` - `304:`    `Invalid object state` - `305:`    `The alarm cannot be read / acknowledged / reset in current state` - `x:`    `Alarm instance does not exist` |  |

---

**See also**

[Type "AlarmIdentifierInput" (RT Unified)](#type-alarmidentifierinput-rt-unified)
  
["ActiveAlarm" and "ActiveAlarmNotification" types (RT Unified)](#activealarm-and-activealarmnotification-types-rt-unified)

#### Mutations "enableAlarms" and "disableAlarms" (RT Unified)

##### Introduction

You have the following options:

- Disabling one or more configured alarms

  The alarm condition of these alarms is no longer checked. No new alarm instances occur.
- Enabling one or more disabled configured alarms

  The alarm condition of these alarms is checked again. New alarm instances occur again.

##### Requirement

- The user who is logged in to runtime for the GraphQL client has the right "GraphQL - read/write access" in runtime.

##### Description "disableAlarms" and "enableAlarms"

disableAlarms(  
 names: [String]  
 ): [AlarmMutationResult]

enableAlarms(  
 names: [String]  
 ): [AlarmMutationResult]

|  |  |  |
| --- | --- | --- |
| Operation name | `disableAlarms` | `enableAlarms` |
| Operation type | `mutation` |  |
| Function | Disables the alarms specified in the input parameter `names`. | Enables the alarms specified in the input parameter `names`. |
| Input parameters | `names`:  - Mandatory parameter - Data type: `[String]` - The fully qualified name of one or more configured alarms.   The alarms are disabled or enabled.   Specify the fully qualified name of a configured alarm:   - Alarm of a tag: <System name>::<Tag name>:<Alarm name>   - Alarm of an element of a structure tag or array: <System name>::<Tag name>.<Element path>:<Alarm name> Delimiter for the components of the element path: "." |  |
| Selection set | Mandatory specification  Specify which attributes the server returns for the queried alarms. You can request the attributes defined in the `AlarmMutationResult` type.   For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |  |
| Server response | Supplies the attributes requested in the selection set for the alarms as key-value pairs of a JSON data record. |  |
| Error messages (`code` and `description`) | - `0:`    `Success` - `2:`    `Cannot resolve provided name` |  |

---

**See also**

[Type "AlarmMutationResult" (RT Unified)](#type-alarmmutationresult-rt-unified)

#### Mutations "shelveAlarms" and "unshelveAlarms" (RT Unified)

##### Requirement

- The user who is logged in to runtime for the GraphQL client has the right "GraphQL - read/write access" in runtime.

##### Description

shelveAlarms(  
 names: [String]  
 shelveTimeout: Timespan  
 ): [AlarmMutationResult]

unshelveAlarms(  
names: [String]  
): [AlarmMutationResult]

|  |  |  |
| --- | --- | --- |
| Operation name | `shelveAlarms` | `unshelveAlarms` |
| Operation type | `mutation` |  |
| Function | Shelves the alarms. The attribute `suppressionState` of the alarms is set to `0x2 Shelved`.  If the GraphQL client has subscribed to one of the shelved alarms, the client receives a notification on the shelving.   The shelved alarms are still available and logged in the system. If the Graph QL client has subscribed a shelved alarm, it keeps receiving notifications on changes at the alarm from the Runtime system.  The implementation of the GraphQL client controls how the client:  - Deals with notifications about subscribed shelved alarms, for example. whether to suppress them. - Deals with operation calls that include shelved alarms, for example whether to disallow read access to these alarms. | Cancels the shelving of the alarms again. This creates a log entry. |
| Input parameters | `names`:  - Mandatory parameter - Data type: `[String]` - The fully qualified name of one or more configured alarms.   The active alarm instances of these alarms are shelved or their shelving is canceled.   Specify the fully qualified name of a configured alarm:   - Alarm of a tag: <System name>::<Tag name>:<Alarm name>   - Alarm of an element of a structure tag or array: <System name>::<Tag name>.<Element path>:<Alarm name> Delimiter for the components of the element path: "." |  |
| `shelveTimeout`:  - Optional - Time interval after which the shelving of the alarms is automatically canceled.   Must not be greater than the timeout configured in Runtime.    If no value is transferred, the timeout configured for Runtime is used. - Data type: Timespan | - |  |
| Selection set | Mandatory specification  Specify which attributes the server returns for the queried alarms. You can request the attributes defined in the `AlarmMutationResult` type.  For information on the notation, see section [Type "AlarmMutationResult"](#type-alarmmutationresult-rt-unified). |  |
| Server response | Supplies the attributes requested in the selection set for the alarms as key-value pairs of a JSON data record. |  |
| Error messages (`code` and `description`) | - `0:`    `Success` - `2:`    `Cannot resolve provided name` |  |

---

**See also**

[Structure of a client query (RT Unified)](#structure-of-a-client-query-rt-unified)

#### "activeAlarms" subscription (RT Unified)

##### Requirements

- The user who is logged in to runtime for the GraphQL client has the rights "GraphQL - read access" or "GraphQL - read/write access" in runtime.
- The WebSocket protocol has been activated.

  > **Note**
  >
  > The WebSocket protocol is not activated by WinCC Unified Setup. Activate it manually if necessary: "Enable or Disable Windows Features > Internet Information Services > WWW Services > Application Development Features > WebSocket Protocol".

##### Description

activeAlarms(  
 systemNames: [String]  
 filterString: String  
 filterLanguage: String  
 languages: [String]  
 ): ActiveAlarmNotification

| Symbol | Meaning |
| --- | --- |
| Operation name | `activeAlarms` |
| Operation type | `subscription` |
| Function | Subscribes to active alarms. |
| Input parameters | `systemNames`   - Optional - Data type: String - Reserved for future versions. - Specifies the runtime whose alarms are subscribed to.   In the current version, the queried alarms are always the alarms of the runtime connected to the GraphQL server.    `filterString`   - Optional - Data type: String - Defines filter criteria for the alarms. See section [Filtering alarms](#filtering-alarms-rt-unified).   If you do not define a filter, you subscribe to all alarms active in runtime.    `filterLanguage`   - Optional - Data type: String - When `filterString` uses a string with a translatable alarm property, you use `filterLanguage` to define which language is used for the comparison.<sup>1</sup> - Default value: "en-US"    `languages`   - Optional - Data type: String array - Defines the languages in which the server returns the texts of translatable alarm properties and the order of the requested languages.<sup>1</sup>   Example:    `queryLanguageExample { activeAlarms(languages:["en-US", "de-DE"] { name, eventText, alarmText1, alarmClassName, state, raiseTime, priority } }`    The initial notification and the subsequent notifications supply the attributes specified in the selection set for the subscribed alarm. Translatable properties, such as `eventText`, are each returned in a string array. The element with index 0 always contains the English text and the element with index 1 the German text. |
| Selection set | Mandatory specification  Specify which attributes the server returns for the subscribed alarms. You can request the attributes defined in the `ActiveAlarmNotification` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified).  Recommendation: Request `name` and `notifcationReason`. |
| Server response | Until the subscription is closed, the server sends an initial notification and sends subsequent notifications when an attribute of one of the subscribed alarms specified in the selection set changes.   The notifications contain the current values of the attributes requested in the selection set as key-value pairs of a JSON data record. |
| Error messages (`code` and `description`) | - `0:`    `Success` - `301:`    `Syntax error in query string` - `302:`    `At least one of the requested languages is invalid` - `303:`    `The provided filter language is invalid` |
| <sup>1</sup> Languages must be specified in ISO language code format (e.g. "en-US", "de-DE"). Note that the entry is case-sensitive. |  |

##### Example

`subscription exampleAlarmSubscription`

`{`

`activeAlarms(languages:["en-US", "de-DE"],  
 filterLanguage:"en-US",  
 filterString:(raiseTime <= '2022-07-26T09:00' AND userName LIKE '* Doe') OR priority > 2")`

`{`

`name`

`notificationReason`

`eventText`

`alarmText1`

`alarmClassName`

`state`

`raiseTime`

`priority`

`}`

`}`

---

**See also**

["Error" type (RT Unified)](#error-type-rt-unified)
  
["ActiveAlarm" and "ActiveAlarmNotification" types (RT Unified)](#activealarm-and-activealarmnotification-types-rt-unified)

#### Filtering alarms (RT Unified)

##### Introduction

You use input parameters of `activeAlarms` queries and `activeAlarms` subscriptions to define filters that control which alarms are read or subscribed to and which logged alarms are read. This improves the performance of your GraphQL clients.

##### Limitation

In the current version of Unified GraphQL, you cannot filter by the following alarm properties:

- `state`
- `stateMachine`
- `changeReason`
- `sourceType`
- `suppressionState`
- `invalidFlags`
- `producer`
- `userResponse`
- `textColor`
- `backColor`
- `valueQuality`
- `quality`

##### Input parameter "filterString"

You use input parameter `filterString` to define the filter criteria. The filter string corresponds to the WHERE part of a valid ChromQueryLanguage string with addition of the keyword WHERE.

> **Note**
>
> ChromQueryLanguage (QCL) is based on SQL. You can also use most of the valid, simple SQL expressions in CQL.

Wildcards permitted in `filterString`:

| Symbol | Meaning |
| --- | --- |
| * | Replaces any number of characters. |
| ? | Replaces exactly 1 character. |

Operators permitted in `filterString`:

| Symbol | Meaning |
| --- | --- |
| > |  |
| > |  |
| = |  |
| LIKE |  |
| () | For grouping of expressions |
| AND  OR | For logically combining expressions |

> **Note**
>
> **Filtering by the "**
> **path**
> **" property**
>
> `path` is the full name of the alarm. It has the following components:
>
> - Alarm of a tag: <System name>::<Tag name>:<Alarm name>
> - Alarm of an element of a structure tag or array: <System name>::<Tag name>.<Element path>:<Alarm name>
>
>   Delimiter for the components of the element path: "."
>
> If the GraphQL client only has access to one runtime system or you want to query the alarms of all connected systems, you can replace the system name with the wildcard "*".

##### Input parameter "filterLanguage"

If `filterString` uses a translatable alarm property, use input parameter `filterLanguage` to specify the language of the text.

Specify the language in ISO language code format (e.g. "en-US", "de-DE"). Note that the entry is case-sensitive.

##### Examples

- `filterString: "alarmClassName = 'SystemNotification'"`

  Returns all active alarms with alarm class "SystemNotification".
- `filterString: "(raiseTime <= '2022-07-26T09:00' AND userName LIKE '* Doe') OR priority > 2"`

  Returns all alarms that were active before 2022-07-26 9:00 and whose associated user has the last name "Doe" or whose priority is greater than 2.
- `filterString: "eventText LIKE 'Maximum value exceeded'"` and `filterLanguage: "en-US"`

  The response returns only alarms that have the value "`Maximum value exceeded`" for `eventText` in English.

  > **Note**
  >
  > You specify the languages and the order in which the texts of the translatable alarm properties are returned with input parameter `languages` in the operation request.
- `filterString: "path LIKE '*::motor1.currentSpeed:*'"`

  Supplies all active alarms of the `currentSpeed` element of the `motor1` structure tag.

---

**See also**

["activeAlarms" query (RT Unified)](#activealarms-query-rt-unified)
  
["activeAlarms" subscription (RT Unified)](#activealarms-subscription-rt-unified)

### Other operations (RT Unified)

This section contains information on the following topics:

- ["login" mutation (RT Unified)](#login-mutation-rt-unified)
- ["loginSWAC" mutation (RT Unified)](#loginswac-mutation-rt-unified)
- ["extendSession" mutation (RT Unified)](#extendsession-mutation-rt-unified)
- ["session" query (RT Unified)](#session-query-rt-unified)
- ["nonce" query (RT Unified)](#nonce-query-rt-unified)
- [Subscription "reduState" (RT Unified)](#subscription-redustate-rt-unified)

#### "login" mutation (RT Unified)

##### Requirements

- The login data of a UMC user configured for runtime is known.

##### Description of "login"

login (  
 username: String  
 password: String  
 ): Session

| Symbol | Meaning |
| --- | --- |
| Operation name | `login` |
| Operation type | mutation |
| Function | Logs the GraphQL client in to the GraphQL server with the login data of a UMC user configured for Runtime.  The user remains logged in until the session is closed, the user is logged out or the connection is disconnected. |
| Input parameters | `username`   - Mandatory parameter - Data type: String - The user name of a UMC user configured for Runtime    `password`   - Mandatory parameter - Data type: String - The password of the UMC user |
| Selection set | Mandatory specification  Specify which attributes the server returns. You can request the attributes defined in the `Session` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified).  Request at least `token`. You require `token` for subsequent server requests. You pass `token` in the HTTP header `Authorization`, with appended `Bearer` prefix. |
| Server response | Supplies the attributes of the `Session` instance requested in the selection set as key-value pairs of a JSON data record. |
| Error messages (`code`: `description`) | - `0:`    `Success` - `101:`    `Incorrect credentials provided` - `102:`    `UMC error` |

---

**See also**

[Disconnection by server (RT Unified)](#disconnection-by-server-rt-unified)
  
["extendSession" mutation (RT Unified)](#extendsession-mutation-rt-unified)
  
[Logging in to the GraphQL server (RT Unified)](#logging-in-to-the-graphql-server-rt-unified)
  
["Session" type (RT Unified)](#session-type-rt-unified)

#### "loginSWAC" mutation (RT Unified)

##### Requirements

- The login data of a UMC user configured for runtime is known.
- The GraphQL client obtained a valid `Nonce` instance by calling `nonce` from the server.
- The GraphQL client has logged in to UMC with its user name and password and transmitted the nonce to UMC when logging in. In response, UMC sent a claim with a built-in nonce as well as a signed claim with a built-in nonce with a private key.

##### Description of "loginSWAC"

loginSWAC(  
 claim: String  
 signedClaim: String  
 ): Session

| Symbol | Meaning |
| --- | --- |
| Operation name | `loginSWAC` |
| Operation type | mutation |
| Function | Transmits the claim and signed claim that the GraphQL client received when logging in to UMC to the GraphQL server. When the `Nonce` contained in `claim` or `signedClaim` is valid, the client is logged on to the server.   The user remains logged in until the session is closed, the user is logged out or the connection is disconnected. |
| Input parameters | `claim`   - Mandatory parameter - Data type: String - The claim submitted by UMC.    `signedClaim`   - Mandatory parameter - Data type: String - The SignedClaim submitted by UMC. |
| Selection set | Mandatory specification  Specify which attributes the server returns. You can request the attributes defined in the `Session` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified).  Request at least `token`. You require `token` for subsequent server requests. You pass `token` in the HTTP header `Authorization`, with appended `Bearer` prefix. |
| Server response | Supplies the attributes requested in the selection set of the `Session` instance generated for the login as key-value pairs of a JSON data record. |
| Error messages (`code`: `description`) | - `0:`    `Success` - `101:`    `Incorrect credentials provided` - `103:`    `Nonce expired` |

---

**See also**

["nonce" query (RT Unified)](#nonce-query-rt-unified)
  
["Nonce" type (RT Unified)](#nonce-type-rt-unified)
  
[Disconnection by server (RT Unified)](#disconnection-by-server-rt-unified)

#### "extendSession" mutation (RT Unified)

##### Requirement

- The GraphQL client is logged in to the server with a valid UMC user.

##### Description

extendSession: Session

| Symbol | Meaning |
| --- | --- |
| Operation name | `extendSession` |
| Operation type | mutation |
| Description | Extends the session of the GraphQL client.   Call the operation to prevent clients that are mainly waiting for notifications from a subscription, for example, from becoming inactive (session timeout) and having to log on again.  Each operation of a client resets the session timeout, i.e. active clients do not need to run extendSession at regular intervals. |
| Input parameters | - |
| Selection set | Mandatory specification  Specify which attributes the server returns. You can request the attributes defined in the `Session` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |
| Server response | Supplies the attributes of the `Session` instance requested in the selection set as key-value pairs of a JSON data record. |
| Error messages (`code`: `description`) | - |

---

**See also**

["login" mutation (RT Unified)](#login-mutation-rt-unified)
  
["Session" type (RT Unified)](#session-type-rt-unified)
  
["session" query (RT Unified)](#session-query-rt-unified)

#### "session" query (RT Unified)

##### Requirement

- The GraphQL client is logged in to the server.

##### Description

session(  
 allSessions: Boolean  
 ): [Session]

| Symbol | Meaning |
| --- | --- |
| Operation name | `session` |
| Operation type | query |
| Description | Queries the current session data from the server. |
| Input parameters | `allSessions`   - Optional - Data type: Bool - Default: False: - True: The server sends the data for all sessions of the logged-in user. |
| Selection set | Mandatory specification  Specify which attributes the server returns. You can request the attributes defined in the `Session` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |
| Server response | Supplies the attributes of the `Session` instance or instances requested in the selection set as key-value pairs of a JSON data record. |
| Error messages (`code`: `description`) | - |

---

**See also**

["Session" type (RT Unified)](#session-type-rt-unified)
  
["extendSession" mutation (RT Unified)](#extendsession-mutation-rt-unified)

#### "nonce" query (RT Unified)

##### Description

nonce: Nonce

| Symbol | Meaning |
| --- | --- |
| Operation name | `nonce` |
| Operation type | `query` |
| Function | Queries a `Nonce` instance from the GraphQL server.  The nonce is required for the SWAC login. |
| Input parameters | - |
| Selection set | Mandatory specification  Specify which attributes the server returns. You can request the attributes defined in the `Nonce` type. For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified).  Request `value`. |
| Server response | Supplies the attributes of the `Nonce` instance requested in the selection set as key-value pairs of a JSON data record. |
| Error messages (`code`: `description`) | - `0:`    `Success` - `101:`    `Incorrect credentials provided` - `103:`    `Nonce expired` |

---

**See also**

["Nonce" type (RT Unified)](#nonce-type-rt-unified)
  
["loginSWAC" mutation (RT Unified)](#loginswac-mutation-rt-unified)

#### Subscription "reduState" (RT Unified)

##### Requirement

- The user who is logged in to runtime for the GraphQL client has the rights "GraphQL - read access" or "GraphQL - read/write access" in runtime.

##### Description

| Symbol | Meaning |
| --- | --- |
| Operation name | `reduState` |
| Operation type | `subscription` |
| Function | Subscribes to the redundancy status of the host connected with the GraphQL client in a redundant system. |
| Input parameters | - |
| Selection set | Mandatory specification  Specify which attributes the server returns for the queried alarms. You can request the attributes defined in the `ReduStateNotification` type.   For information on the notation, see section [Structure of a client query](#structure-of-a-client-query-rt-unified). |
| Server response | Supplies the attributes requested in the selection as key-value pairs of a JSON data record. |

> **Note**
>
> **Passive redundancy status**
>
> If the GraphQL client receives a notification that the status is passive, log off the client from the connected GraphQL server. Connect the client with the GraphQL server of the active host.

---

**See also**

[Types "ReduStateNotification" and "ReduStateValue" (RT Unified)](#types-redustatenotification-and-redustatevalue-rt-unified)

### Reference for Unified-specific types and enumerations (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-1)
- ["ActiveAlarm" and "ActiveAlarmNotification" types (RT Unified)](#activealarm-and-activealarmnotification-types-rt-unified)
- [Type "AlarmIdentifierInput" (RT Unified)](#type-alarmidentifierinput-rt-unified)
- ["AlarmInvalidFlags" type (RT Unified)](#alarminvalidflags-type-rt-unified)
- [Type "AlarmMutationResult" (RT Unified)](#type-alarmmutationresult-rt-unified)
- ["Error" type (RT Unified)](#error-type-rt-unified)
- [Type "LoggedAlarm" (RT Unified)](#type-loggedalarm-rt-unified)
- ["Nonce" type (RT Unified)](#nonce-type-rt-unified)
- ["Quality" type (RT Unified)](#quality-type-rt-unified)
- ["QualityInput" type (RT Unified)](#qualityinput-type-rt-unified)
- [Types "ReduStateNotification" and "ReduStateValue" (RT Unified)](#types-redustatenotification-and-redustatevalue-rt-unified)
- ["Session" type (RT Unified)](#session-type-rt-unified)
- ["TagValueNotification" type (RT Unified)](#tagvaluenotification-type-rt-unified)
- ["TagValueResult" type (RT Unified)](#tagvalueresult-type-rt-unified)
- ["Time span" type (RT Unified)](#time-span-type-rt-unified)
- ["Time stamp" type (RT Unified)](#time-stamp-type-rt-unified)
- ["User" type (RT Unified)](#user-type-rt-unified)
- ["UserGroup" type (RT Unified)](#usergroup-type-rt-unified)
- ["Value" type (RT Unified)](#value-type-rt-unified)
- ["WriteTagValueResult" type (RT Unified)](#writetagvalueresult-type-rt-unified)

#### Introduction (RT Unified)

This section describes the Unified data types used in the GraphQL client queries and server responses.

For information about the enumerations used in these types, see the interface documentation that is available online when schema introspection is enabled.

#### "ActiveAlarm" and "ActiveAlarmNotification" types (RT Unified)

##### Description

Instances of the type `ActiveAlarm` represent the information about alarms that you can request in `activeAlarms` queries from the server. Instances of type `ActiveAlarmNotification` represent information that you can request through `activeAlarm` subscriptions.

This includes:

- Properties of active alarms

  The table below provides a reference for the alarm properties.

  Translatable properties are returned as a string array. The array contains the alarm property texts in the languages requested and the order defined with input parameter `languages` in the operation request.
- The `languages` attribute

  A string array with the languages that the user has specified with input parameter `languages` in the `activeAlarms` request.

  For correct processing of the strings returned in the arrays for translatable alarm properties.

##### Reference of the alarm properties

The following table lists the alarm properties provided in the `ActiveAlarm` and `ActiveAlarmNotification` types in alphabetical order:

| Name | Data type | Description |
| --- | --- | --- |
| `acknowledgmentTime` | `Timestamp` | `Timestamp` instance for the time at which the alarm was acknowledged |
| `alarmClassID` | `Int` | User-defined ID of the alarm class of the alarm |
| `alarmClassName` | `String` | Name of the alarm class of the alarm |
| `alarmClassSymbol` | `[String]` | The symbols configured for the alarm class  Translatable property |
| `alarmGroupID` | `Int` | User-defined ID of the alarm group to which alarm belongs |
| `alarmParameterValues` | `[Variant]` | To dynamize the following texts:   `alarmText1` to `alarmText9` these values can be used as parameters in these texts. |
| `alarmText1`    `bis`     `alarmText9` | `[String]` | Additional texts for the alarm  Translatable properties |
| `alarmType` | `[String]` | Supplies details regarding the alarm condition. The values can be user-defined or product-specific.  Translatable property |
| `area` | `String` | Name of the area to which the alarm belongs |
| `backColor` | `Color` | Background color of the alarm in the alarm control |
| `changeReason` | `[AlarmChangeReason]` | Reason for changes to the alarm as defined in enumeration `AlarmChangeReason` |
| `clearTime` | `Timestamp` | `Timestamp` instance for the time at which the alarm became inactive |
| `connectionName` | `String` | Only for PLC alarms  Name of the HMI connection |
| `deadBand` | `Variant` | Hysteresis for `valueLimit` for suppressing the noise component during alarm generation |
| `duration` | `Timespan` | The time interval between the time when the alarm became active and the time when the alarm state changed the last time |
| `eventText` | `[String]` | Main text for the alarm, typically describes the cause of the alarm  Translatable property |
| `flashing` | `Boolean` | True: The alarm flashes in the alarm control |
| `hostName` | `String` | Name of the device that hosts the source of the alarm  In the case of alarms triggered by operator input, this is the client on which the operator made the input. |
| `infoText` | `[String]` | More information for the operator, such as instructions or standard procedures for handling this alarm  Translatable property |
| `instanceID` | `Int` | Alarm ID of the active alarm  For unambiguous alarm identification of configured alarms that can have more than one active alarm instance at a time. |
| `invalidFlags` | `AlarmInvalidFlags` | `AlarmInvalidFlags` instance that indicates whether attributes or configuration of the alarm are invalid. |
| `loopInAlarm` | `String` | A script function that jumps to the screen that has triggered the alarm. |
| `loopInAlarmParameterValues` | `Variant` | Parameters for loop-in-alarms |
| `modificationTime` | `Timestamp` | `Timestamp` instance for the last time one of the properties of the alarm was changed |
| `name` | `String` | Name of the configured alarm |
| `notificationReason` | `String` | Only for `ActiveAlarmNotification`  Reason for the notification  Possible values:  - "Added"   An active alarm was added to the subscription. - "Modified"   A subscribed alarm was modified. - "Removed"   A subscribed alarm was removed from the subscription because it became inactive or no longer satisfies the filter criteria. |
| `origin` | `String` | Name of the object that activated this alarm instance, e.g. an HMI device or function block. |
| `path` | `String` | The full alarm name  Can be used for filtering the `activeAlarm` query or subscription. See section [Filtering alarms](#filtering-alarms-rt-unified). |
| `priority` | `Int` | The current priority of the active alarm  Possible values:  - 0: No priority assigned - 1-5: Low (primarily an informative function) - 6-10: Medium (warnings) - 11-15: High (errors) - 16: Highest (critical alarms) |
| `producer` | `AlarmProducer` | The Siemens product or the function of a domain to which the alarm source belongs, as defined in enumeration `AlarmProducer` |
| `quality` | `Quality` | Quality of `state` as `Quality` instance |
| `raiseTime` | `Timestamp` | `Timestamp` instance for the time at which the alarm became active |
| `resetTime` | `Timestamp` | `Timestamp` instance for the time at which the alarm was reset |
| `sourceID` | `String` | Identifies the source of the alarm instance  For controller alarms, the communication driver assigns the ID based on the reference of the external alarm source, such as the alarm area ID of the S7 PLC.  For application alarms, the application or the service assigns the ID so that the alarm has a relationship with a service-specific object, e.g. recipe name/ID by the service of the parameter set control. |
| `sourceType` | `AlarmSourceType` | Type of source from which the alarm was generated, e.g. tag-based, PLC-based or system-based, as defined in enumeration `AlarmSourceType` |
| `state` | `AlarmState` | The current state of the active alarm as defined in enumeration `AlarmState` |
| `stateMachine` | `AlarmStateMachine` | State machine of the active alarm  The state machine defines possible states of the alarm and transitions between these states, as defined in enumeration `AlarmStateMachine` |
| `stateText` | `[String]` | The user-defined description of the alarm state  Translatable property |
| `suppressionState` | `AlarmSuppressionState` | Visibility of the alarm  Shelved alarms are not visible in the alarm control but are still active, as defined in enumeration `AlarmSuppressionState` |
| `systemSeverity` | `Int` | Alarm severity from the perspective of the system  The number of severe alarms in a system provides an indication of the health of the system. In redundant systems, the healthier host becomes the active host and the less healthy host becomes the passive host. |
| `textColor` | `Color` | Text color of the alarm in the alarm control |
| `userName` | `String` | Name of the user associated with the last alarm event |
| `userResponse` | `AlarmUserResponse` | The expected operator response as defined in enumeration `AlarmUserResponse` |
| `value` | `Variant` | The value of the alarm |
| `valueLimit` | `Variant` | Limit for value as of which the alarm becomes active.  If a dynamic limit has been configured for the alarm, then the updated limit |
| `valueQuality` | `Quality` | Quality of `value` as `Quality` instance |

---

**See also**

["activeAlarms" query (RT Unified)](#activealarms-query-rt-unified)
  
["activeAlarms" subscription (RT Unified)](#activealarms-subscription-rt-unified)
  
["AlarmInvalidFlags" type (RT Unified)](#alarminvalidflags-type-rt-unified)
  
["Time span" type (RT Unified)](#time-span-type-rt-unified)
  
["Time stamp" type (RT Unified)](#time-stamp-type-rt-unified)
  
["Quality" type (RT Unified)](#quality-type-rt-unified)

#### Type "AlarmIdentifierInput" (RT Unified)

##### Description

The `AlarmIdentifierInput` type defines attributes for specifying the alarms to be acknowledged or reset.

The data type has the following attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `name` | `String` | - Mandatory specification - The fully qualified name of a configured alarm   Alarm of a tag: <System name>::<Tag name>:<Alarm name>   Alarm of an element of a structure tag or array: <System name>::<Tag name>.<Element path>:<Alarm name> Delimiter for the components of the element path: "." |
| `instanceID` | `Int` | - Optional - The ID of an alarm instance of the configured alarm - If "0" is transferred as the `instanceID` or if no `instanceID` is transferred, all active alarms of the configured alarm are acknowledged. |

---

**See also**

[Mutations "acknowledgeAlarms" and "resetAlarms" (RT Unified)](#mutations-acknowledgealarms-and-resetalarms-rt-unified)

#### "AlarmInvalidFlags" type (RT Unified)

##### Description

The `AlarmInvalidFlags` type defines attributes for invalid attributes or configurations of alarms.

| Name | Data type | Description |
| --- | --- | --- |
| `invalidConfiguration` | `Boolean` | The alarm has an invalid configuration. |
| `invalidTimestamp` | `Boolean` | The alarm has an invalid time stamp. |
| `invalidAlarmParameter` | `Boolean` | The alarm has an invalid alarm parameter. |
| `invalidEventText` | `Boolean` | The alarm has an invalid event text. |

---

**See also**

["ActiveAlarm" and "ActiveAlarmNotification" types (RT Unified)](#activealarm-and-activealarmnotification-types-rt-unified)

#### Type "AlarmMutationResult" (RT Unified)

##### Description

The `AlarmMuationResult` type defines attributes for specifying the alarms to be acknowledged or reset.

The data type has the following attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `alarmName` | `String` | - Mandatory specification - The fully qualified name of the configured alarm   Specify the fully qualified name of a configured alarm:   - Alarm of a tag: <System name>::<Tag name>:<Alarm name>   - Alarm of an element of a structure tag or array: <System name>::<Tag name>.<Element path>:<Alarm name> Delimiter for the components of the element path: "." |
| `error` | `Error` | - Optional - Feedback on the success of the operation |

---

**See also**

[Mutations "enableAlarms" and "disableAlarms" (RT Unified)](#mutations-enablealarms-and-disablealarms-rt-unified)
  
[Mutations "shelveAlarms" and "unshelveAlarms" (RT Unified)](#mutations-shelvealarms-and-unshelvealarms-rt-unified)

#### "Error" type (RT Unified)

##### Description

The `Error` type defines the attributes of item-level errors.

For GraphQL operations with item-level errors, you can request these attributes from the server via the selection set when the operations call is made.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `code` | String | Numeric code of the error message |
| `description` | String | Detailed description of the error message |

---

**See also**

[Top-level and item-level errors (RT Unified)](#top-level-and-item-level-errors-rt-unified)
  
["TagValueResult" type (RT Unified)](#tagvalueresult-type-rt-unified)
  
["WriteTagValueResult" type (RT Unified)](#writetagvalueresult-type-rt-unified)
  
["TagValueNotification" type (RT Unified)](#tagvaluenotification-type-rt-unified)
  
["Session" type (RT Unified)](#session-type-rt-unified)

#### Type "LoggedAlarm" (RT Unified)

##### Description

The data type `LoggedAlarm` provides the following attribute:

- `hasComments`

  Shows whether comments on the logged alarm are pending.

  Data type: `boolean`

With exception of the following attributes the data type `LoggedAlarm` also provides the same attributes as the data type `ActiveAlarm`:

- `flashing`
- `connectionName`
- `sourceID`
- `systemSeverity`
- `loopInAlarm`
- `loopInAlarmParameterValues`
- `path`
- `userResponse`

These alarm attributes are not logged.

---

**See also**

["loggedAlarms" query (RT Unified)](#loggedalarms-query-rt-unified)

#### "Nonce" type (RT Unified)

##### Description

The `Nonce` type defines attributes of a nonce that are required to log in to a GraphQL client via SWAC login.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `value` | `String` | The nonce string |
| `validFor` | `Int` | Time span in seconds until the nonce instance expires |

---

**See also**

["nonce" query (RT Unified)](#nonce-query-rt-unified)
  
["loginSWAC" mutation (RT Unified)](#loginswac-mutation-rt-unified)

#### "Quality" type (RT Unified)

##### Description

An instance of type `Quality` represents the quality of a tag value or alarm value (`value` attribute).

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `quality` | `MainQuality` | The main QualityCode, as defined in enumeration `MainQuality` |
| `subStatus` | `QualitySubStatus` | The reason for the main QualityCode, as defined in enumeration `QualitySubStatus` |
| `limit` | `QualityLimit` | Information on whether or how the QualityCode is related to defined limit values, as defined in enumeration `QualityLimit` |
| `extendedSubStatus` | `QualityExtendedSubStatus` | More detailed information on `subStatus`, as defined in enumeration `QualityExtendedSubStatus` |
| `sourceQuality` | `Boolean` | The source that set `value` also set quality. |
| `sourceTime` | `Boolean` | The source that set `value` also set a time stamp. |
| `timeCorrected` | `Boolean` | The time stamp set by the source has been corrected. |

#### "QualityInput" type (RT Unified)

##### Description

The `QualityInput` type describes the attributes that are passed when `writeTags` is called in the input parameter `quality`.

| Name | Data type | Description |
| --- | --- | --- |
| `quality` | `MainQuality` | Mandatory specification  The main QualityCode, as defined in enumeration `MainQuality` |
| `subStatus` | `QualitySubStatus` | The reason for the main QualityCode, as defined in enumeration `QualitySubStatus` |

---

**See also**

["writeTags" mutation (RT Unified)](#writetags-mutation-rt-unified)

#### Types "ReduStateNotification" and "ReduStateValue" (RT Unified)

##### "ReduStateNotification" type description

The `ReduStateNotification` type has the following attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `value` | `ReduStateValue` | Instance of the data type "ReduStateValue" |
| `notificationReason` | `String` | Reason for the notification |

##### "ReduStateValue" type description

The `ReduStateValue` type has the following attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `value` | `ReduStateValue` | The redundancy status as defined in the enumeration `ReduState`:  - `ACTIVE`    The host of the GraphQL server currently connected with the GraphQL client is active. - `PASSIVE`    The host of the GraphQL server currently connected with the GraphQL client is passive. |
| `timestamp` | `Timestamp` | The time stamp |

---

**See also**

[Subscription "reduState" (RT Unified)](#subscription-redustate-rt-unified)

#### "Session" type (RT Unified)

##### Description

The `Session` type defines attributes of a session.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `token` | `String` | ID of the authorization token for this session  In subsequent server requests, pass the ID of the authorization token in the HTTP header `Authorization`, preceded by the `Bearer` prefix.  When operations are called that require a user to be logged on to the server, this ID must be passed in the HTTP header `Authorization`, preceded by a `Bearer` prefix. |
| `expires` | `Timestamp` | Time at which the session expires, as `Timestamp` instance |
| `error` | `Error` | `Error` instance of possible item-level errors |

---

**See also**

["session" query (RT Unified)](#session-query-rt-unified)
  
["UserGroup" type (RT Unified)](#usergroup-type-rt-unified)
  
["User" type (RT Unified)](#user-type-rt-unified)
  
["login" mutation (RT Unified)](#login-mutation-rt-unified)
  
["extendSession" mutation (RT Unified)](#extendsession-mutation-rt-unified)
  
["Error" type (RT Unified)](#error-type-rt-unified)

#### "TagValueNotification" type (RT Unified)

##### Description

The `TagValueNotification` type defines which attributes the notifications for subscribed tags can contain.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `name` | `String` | Name of the subscribed tag |
| `value` | `Value` | `Value` instance of the tag |
| `error` | `Error` | `Error` instance of possible item-level errors |
| `notificationReason` | `String` | Possible values:  - "Added"   The subscription of the tag was started. The property values of the tag are sent at the start time of the subscription. - "Modified"   The tag was modified. Your current property values are sent. - "Removed"   The subscription of the tag was closed. |

---

**See also**

["Error" type (RT Unified)](#error-type-rt-unified)
  
["tagValues" subscription (RT Unified)](#tagvalues-subscription-rt-unified)

#### "TagValueResult" type (RT Unified)

##### Description

The `TagValueResult` type defines which attributes the server can supply in its response after the `tagValues` query is called.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `name` | `String` | Tag name |
| `value` | `Value` | `Value` instance of the tag |
| `error` | `Error` | `Error` instance of possible item-level errors |

---

**See also**

["tagValues" query (RT Unified)](#tagvalues-query-rt-unified)
  
["Error" type (RT Unified)](#error-type-rt-unified)
  
["Value" type (RT Unified)](#value-type-rt-unified)

#### "Time span" type (RT Unified)

##### Description

Type used to define a time span.

Data type of time span: RAW (integer in 100 ns)

---

**See also**

["ActiveAlarm" and "ActiveAlarmNotification" types (RT Unified)](#activealarm-and-activealarmnotification-types-rt-unified)

#### "Time stamp" type (RT Unified)

##### Description

Type for the definition of a time stamp according to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601).

---

**See also**

["ActiveAlarm" and "ActiveAlarmNotification" types (RT Unified)](#activealarm-and-activealarmnotification-types-rt-unified)

#### "User" type (RT Unified)

##### Description

The `User` type defines attributes of the user logged in to GraphQL.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `id` | `String` | User ID |
| `name` | `String` | User name |
| `groups` | `[UserGroup]` | The user group to which the users belong, as `UserGroup` instance |
| `fullName` | `String` | The full user name, such as first name and last name |
| `language` | `String` | The language set for the user in UMC  Can be empty. |
| `autoLoggOffSec` | `Int` | Time period in seconds for which the user can be inactive before their authorization token expires |

---

**See also**

["Session" type (RT Unified)](#session-type-rt-unified)
  
["UserGroup" type (RT Unified)](#usergroup-type-rt-unified)

#### "UserGroup" type (RT Unified)

##### Description

The `UserGroup` type defines attributes of a user group.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `id` | `String` | ID of the user group |
| name | `String` | Name of the user group |

---

**See also**

["User" type (RT Unified)](#user-type-rt-unified)

#### "Value" type (RT Unified)

##### Description

An instance of type `Value` represents a tag value.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `value` | `Variant` | The current process value |
| `timestamp` | `Timestamp` | Timestamp of the last change of `value` |
| `quality` | `Quality` | Quality of `value` |

---

**See also**

["TagValueResult" type (RT Unified)](#tagvalueresult-type-rt-unified)
  
["Quality" type (RT Unified)](#quality-type-rt-unified)
  
["TagValueNotification" type (RT Unified)](#tagvaluenotification-type-rt-unified)

#### "WriteTagValueResult" type (RT Unified)

##### Description

An instance of type `WriteTagValueResult` represents a feedback for the write access to a tag.

Attributes:

| Name | Data type | Description |
| --- | --- | --- |
| `name` | `String` | Tag name |
| `error` | `Error` | Error instance of possible item-level errors |

---

**See also**

["writeTags" mutation (RT Unified)](#writetags-mutation-rt-unified)
  
["Error" type (RT Unified)](#error-type-rt-unified)

## Code examples (RT Unified)

Numerous code examples in multiple programming languages are included in the scope of delivery of WinCC Unified GraphQL.

### Overview

| Programming language | Covered topics |
| --- | --- |
| Python | Login  Querying and changing data  Subscribing to data |
| HTML and Javascript | Subscribing to data and displaying in Google diagrams |
| C# | Purely WebSocket-based subscription without GraphQL library |
| SWAC | Login with a SWAC-based login method |

### Installation

The GraphQL examples are an integral component of the Openness SDK and available on the WinCC Unified installation medium.

You can find information on installing the SDK in the "Installation SDK" user help.

## Recommended procedures (RT Unified)

This section contains information on the following topics:

- [Performance optimization (RT Unified)](#performance-optimization-rt-unified)
- [Disconnection by server (RT Unified)](#disconnection-by-server-rt-unified)

### Performance optimization (RT Unified)

The performance capability of a GraphQL client depends on how the GraphQL API is being used.

Below are tips on how you can optimize the performance of your GraphQL application.

#### Limiting the selection

In its response to the client, the GraphQL server transmits the fields in the selection set that were specified by the client for the operation request. In most cases, fields that were not requested are not processed by the server.

Improve the performance of your client by using selection sets that are precisely tailored to your requirements.

**Example**

- `activeAlarms` query with extensive selection set:

  `query {activeAlarms(languages: ["en-US", "de-DE"]filterLanguage: "en-US") {name instanceID alarmGroupID raiseTime acknowledgmentTime clearTime resetTime modificationTime state textColor backColor flashing alarmClassName alarmClassSymbol alarmClassID stateMachine priority alarmParameterValues languages alarmType eventText infoText alarmText1 alarmText2 alarmText3 alarmText4 alarmText5 alarmText6 alarmText7 alarmText8 alarmText9 stateText origin area changeReason connection valueLimit sourceType suppressionState hostName userName value valueQuality { quality subStatus } quality { quality subStatus } invalidFlags { invalidAlarmParameter invalidConfiguration invalidEventText invalidTimestamp } deadBand producer duration sourceID systemSeverity loopInAlarm loopInAlarmParameterValues tag userResponse } }`
- `activeAlarms` query with limited selection set:

  `query { activeAlarms( languages: ["en-US", "de-DE"] filterLanguage: "en-US" ) { name instanceID eventText } }`

#### Bulk operations

Method calls of a web client have a larger overhead than method calls of locally connected DLLs or RPCs (Remote Procedure Calls) because a connection between the client and server has to be established in the background. This also applies to GraphQL.

Reduce this overhead by calling a method once and passing a list of objects as input parameter instead of individually calling the method for each object. The GraphQL server executes the operation for all objects from the list and supplies the result in a response.

**Example**

| Symbol | Meaning |
| --- | --- |
| Objective | Read out the timestamp of multiple tags |
| Query | query{ tagValues(names: ["Tag_1"],["Tag_2"],["Tag_3"]) {value {value timestamp} error { description }} |
| Response | {"data": {"tagValues": [ {"value": {"value": 75, "timestamp": "2022-07-20T07:50:46.476" }, "error": {"description": "Succeeded" }},{"value": {"value": false, "timestamp": "1970-01-01T00:00:00.000Z" }, "error": {"description": "Succeeded" }},{{"value": "value": false, "timestamp": "1970-01-01T00:00:00.000Z" }, "error": {"description": "Succeeded" }}]}} |

| Symbol | Meaning |
| --- | --- |
| ![Bulk operations](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tip for working efficiently** |
| Change the same tag in the same mutation request multiple times.  Example: A GraphQL client is to document the values of a tag for audit purposes. The client subscribes to the tag and caches the reported value changes (value and timestamp). At regular intervals, the client executes a mutation to which it passes the cached values with their associated timestamps. |  |

#### Using efficient client libraries

Libraries for GraphQL clients hide the details on HTTP and WebSockets from the developers. They convert the responses of the server into objects that correspond to the programming language, check whether the client code violates the schema, and more. This simplifies programming of a GraphQL client but slows down its execution.

How useful and performant a library is depends on which functions the library takes on, how well it is programmed and the programming language used.

Test a variety of libraries in advance before deciding which library is best suited to your needs.

#### Using a custom client

If performance is the most important factor, you can use the GraphQL API directly with an HTTP and/or WebSocket library instead of a client library.

Queries and mutations are HTTP POST messages in which the operation is sent in the POST body and the authorization in the HTTP header.

Subscriptions are WebSocket connections. Their input parameters are transferred as WebSocket messages.

You can examine the details of the messages, e.g. with the Google Chrome developer tools, while operations are executed in Apollo Studio.

---

**See also**

[Filtering alarms (RT Unified)](#filtering-alarms-rt-unified)

### Disconnection by server (RT Unified)

#### Overview

Normally, the client closes the connection to the GraphQL server by requesting the `logout` mutation. In rare cases, the server closes the connection, e.g. when it is stopped.

When the server closes the connection, the GraphQL client library receives a notification regarding this. The client must reestablish the connection. If the server is still running, the client must execute the subscription again.

#### Handling of subscriptions after connection reestablishment

If the server is still running, the client can execute the subscription again.

If the server has been stopped, the client must cyclically query the server until it is available again, e.g. by executing the subscription operation until it is successful.

#### Examples

- Folder "Support\Openness\GraphQL\Examples\PythonClient" on the WinCC Unified installation medium contains the following code example: "gql_subscription.py"

  In the example, the iterator is closed and a specific exception is thrown.
- The following Python code snippet shows how the client closes the subscription and how it is notified when the server closes the subscription:

  ![Examples](images/159747602571_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

["login" mutation (RT Unified)](#login-mutation-rt-unified)

## Troubleshooting (RT Unified)

This section contains information on the following topics:

- [Top-level and item-level errors (RT Unified)](#top-level-and-item-level-errors-rt-unified)
- [GraphQL server doesn't start (RT Unified)](#graphql-server-doesnt-start-rt-unified)

### Top-level and item-level errors (RT Unified)

#### Error groups

The following error groups exist in GraphQL:

- Top-level errors

  The entire method request has failed. Only the error message is supplied, and no result data.
- Item-level errors

  The method was able to be requested, but parts of the method call were not successful.

  Result data is supplied. The parts of the method request that were not successful contain an error code other than "0" in the `error` attribute and an error description other than "Succeeded".

> **Note**
>
> **Error attributes specified in the selection set**
>
> In order for the server response to contain error information about item-level errors, you must request the desired error attributes when calling the operation with the selection set.
>
> It is recommended that the `code` or `description` attribute, or both, be requested.

#### Example for a top-level error

If the requested language is invalid, this results in the following error message:

`{`
  
 `"errors": [`
  
 `{`
  
 `"message": "At least one of the requested languages is invalid.",`
  
 `"locations": [`
  
 `{`
  
 `"line": 2,`
  
 `"column": 3`
  
 `}],`
  
 `"path": ["activeAlarms"],`
  
 `"extensions":   
 {`
  
 `"code": "INTERNAL_SERVER_ERROR"`
  
 `}`
  
 `}],`
  
 `"data":   
 {`
  
 `"activeAlarms": null`
  
 `}`
  
`}`

Attributes:

- `message`: Easy-to-understand error description
- `locations` and `path` The part of the query that contains errors
- `code`: A general or specific error code

  `INTERNAL_SERVER_ERROR` is the default error code if no specific error code exists.
- (when development mode is enabled) `stackTrace`: For further error diagnostics

#### Example for an item-level error

A writeTagValues call is to write values to two tags. The write operation was able to be successfully performed for tag "TrainingString1" but not for tag "Intern_Int_2". The result data for "Intern_Int_2" contains the error code and an error description. The reason for the error is that the passed data type (String) could not be converted to the expected data type (DTInt):

`{`
  
 `"data": {`
  
 `"writeTagValues": [`
  
 `{`
  
 `"name": "TrainingString1",`
  
 `"error":   
 {`
  
 `"code": "0",`
  
 `"description": "Succeeded"`
  
 `}`
  
 `},`
  
 `{`
  
 `"name": "Intern_Int_2",`
  
 `"error":   
 {`
  
 `"code": "201",`
  
 `"description": "Can't convert provided value to data type 'DTInt': 'failing string value'"`
  
 `}`
  
 `}]`
  
 `}`
  
`}`

---

**See also**

[Structure of a client query (RT Unified)](#structure-of-a-client-query-rt-unified)
  
["Error" type (RT Unified)](#error-type-rt-unified)

### GraphQL server doesn't start (RT Unified)

| Symbol | Meaning |
| --- | --- |
| Problem | GraphQL server doesn't start |
| Identify the cause | 1. In the installation folder of WinCC Unified, double-click the "RTILtraceViewer.exe" file under "​WinCCUnified\bin​".    The "TraceViewer" application is started. 2. Browse the traces for the trace entry documenting the failed start of the GraphQL server. |
| Examples of possible causes | - The port configured for the GraphQL server is being used by another application. - A configured plug-in could not be loaded. |

#### Port occupied

If the port needed for the GraphQL server is being used by another application, the GraphQL server cannot start.

Resulting trace entry:

- Severity "Fatal"
- Message: "Port 4000 already in use. Exiting..."

Remedy: Select a different port for the other application.
