---
title: "OPC for Runtime Advanced (Panels, Comfort Panels, RT Advanced)"
package: OPCWCCAenUS
topics: 19
devices: [Comfort Panels, Panels, RT Advanced]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# OPC for Runtime Advanced (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [(Panels, Comfort Panels, RT Advanced)](#panels-comfort-panels-rt-advanced)
- [Security concept of OPC UA (Panels, Comfort Panels, RT Advanced)](#security-concept-of-opc-ua-panels-comfort-panels-rt-advanced)
- [(Panels, Comfort Panels, RT Advanced)](#panels-comfort-panels-rt-advanced-1)
- [(Panels, Comfort Panels, RT Advanced)](#panels-comfort-panels-rt-advanced-2)
- [(Panels, Comfort Panels, RT Advanced)](#panels-comfort-panels-rt-advanced-3)

## (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [OPC (Panels, Comfort Panels, RT Advanced)](#opc-panels-comfort-panels-rt-advanced)
- [OPC Specifications (Panels, Comfort Panels, RT Advanced)](#opc-specifications-panels-comfort-panels-rt-advanced)
- [Compatibility (Panels, Comfort Panels, RT Advanced)](#compatibility-panels-comfort-panels-rt-advanced)
- [Using OPC in WinCC (Panels, Comfort Panels, RT Advanced)](#using-opc-in-wincc-panels-comfort-panels-rt-advanced)

### OPC (Panels, Comfort Panels, RT Advanced)

#### Introduction

OPC refers to standardized multi-vendor software interfaces for data exchange in automation engineering.

The OPC interfaces provide a standardized environment in which devices and applications from various manufacturers can be linked.

OPC is based on the Windows technology COM (Component Object Model) and DCOM (Distributed Component Object Model).

OPC UA (Unified Architecture) is the technology succeeding OPC. OPC UA is platform-independent and can use different reports as a communication medium.

#### Principle of operation

In WinCC, you can configure HMI devices as OPC servers or OPC clients. The particular HMI device determines which OPC servers and OPC clients are available.

### OPC Specifications (Panels, Comfort Panels, RT Advanced)

### Compatibility (Panels, Comfort Panels, RT Advanced)

Support of the mentioned specifications is checked regularly by the "Compliance Test Tool" (CTT) of the OPC Foundation. Interoperability with OPC products of other manufacturers is ensured through the participation in "OPC Interoperability Workshops".

The test results submitted are published on the website of the OPC Foundation. The results can be called up from there using the search term "OPC Self-Certified Products".

### Using OPC in WinCC (Panels, Comfort Panels, RT Advanced)

## Security concept of OPC UA (Panels, Comfort Panels, RT Advanced)

### Introduction

The WinCC OPC UA uses the TCP/IP protocol for data exchange. Instance certificates are exchanged for authorization between WinCC OPC UA server and OPC UA client. In addition, you can encode the data transfer.

### Security concept

The WinCC OPC UA server and each OPC UA client authorize themselves mutually by exchanging certificates.

By default, the WinCC OPC UA server creates during installation a self signed instance certificate. The server sends this instance certificate to the client. You can alternatively replace this instance certificate with a project-specific instance certificate.

> **Note**
>
> **Private key and own certificates**
>
> If you have an own certification center, you can create your own certificates and make them available for all communication partners. In this case, delete the instance certificate created by WinCC OPC UA server.

The instance certificate of the client that is allowed to communicate with the server must be stored on both the server and the client in the appropriate directory.

### Storage locations of the instance certificates

The instance certificate is stored on the OPC UA server in the following path:

- On PCs: "\ProgramData\Siemens\CoRtHmiRTm\MiniWeb1X.X.X\SystemRoot\SSL"
- On Panels: "\flash\simatic\SystemRoot\SSL**"**

The instance certificate is stored on the OPC UA client in the following path:

- On PCs: "ProgramData\Siemens\CoRtHmiRTm\OPC\PKI\CA\"
- On Panels: "flash\Simatic\SystemRoot\OPC\PKI\CA\"

If you configure two OPC connections in your project, create the following directories under [...]\OPC\PKI\CA\:

- "Default"
- "!Conn_1"
- "!Conn_2"

Each directory contains the subdirectories "certs", "rejected" and "private". Self-signed instance certificates and private keys are stored under "Default\certs" or "Default\private". The OPC-UA connections only use these certificates.

The client always stores the sent server certificates first in the "rejected" directory and does not allow a connection to the server. To allow connection to the server at the client end, you need to move the certificate in question from the "rejected" directory into the "certs" directory.

The server also initially stores the client certificate in the "rejected" directory under [...]\SystemRoot\SSL. To allow connection to the server at the server end, you need to move the certificate in question from the "rejected" directory into the "certs" directory under [...]\SystemRoot\SSL.

### Configuring the OPC UA client for the security mode

If the OPC UA server is running and the OPC UA client was started with an encrypted connection, set up the communication between the OPC UA server and the OPC UA client in security mode.

1. Move the instance certificate sent from the server from the "rejected" directory to the "certs" directory on the OPC UA client.
2. Move the instance certificate sent from the client from the "rejected" directory to the "certs" directory on the OPC UA server.

Once the client and the server have authorized each other, they communicate in security mode.

> **Note**
>
> If you want to use certificates of third-party vendors for the OPC UA client, stop Runtime and copy the third-party certificates and private keys into the directories "!Conn1\certs" and "!Conn1\private". Then copy the certificate from the "certs" directory into the "SSL" directory on the server. Then start Runtime again**.**

### Security settings

The following table lists the security settings supported by the WinCC OPC UA server:

| SecurityPolicy | Message Security Mode |  |  |
| --- | --- | --- | --- |
| None<sup>1</sup> | None |  |  |
| Basic128Rsa15 <sup>2</sup> | None <sup>3</sup> | Sign<sup> 4</sup> | SignAndEncrypt <sup>5</sup> |
| 1: The certificate exchange is switched off. Every OPC UA client can log on to the WinCC OPC UA server. |  |  |  |
| 2: Certificate exchange with depth of encryption of 128 bit. |  |  |  |
| 3: The data packages are exchanged after certificate check unsecured between client and server. |  |  |  |
| 4: The data packages are signed with the certificates, but not encoded |  |  |  |
| 5: The data packages are signed with the certificates and encoded |  |  |  |

## (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring an HMI device as OPC DA server (Panels, Comfort Panels, RT Advanced)](#configuring-an-hmi-device-as-opc-da-server-panels-comfort-panels-rt-advanced)
- [Configuring an HMI device as an OPC UA server (Panels, Comfort Panels, RT Advanced)](#configuring-an-hmi-device-as-an-opc-ua-server-panels-comfort-panels-rt-advanced)
- [Configuring DCOM user permissions in Windows (Panels, Comfort Panels, RT Advanced)](#configuring-dcom-user-permissions-in-windows-panels-comfort-panels-rt-advanced)

### Configuring an HMI device as OPC DA server (Panels, Comfort Panels, RT Advanced)

### Configuring an HMI device as an OPC UA server (Panels, Comfort Panels, RT Advanced)

#### Introduction

The following HMI devices can be used as OPC UA servers:

- Comfort Panels
- RT Advanced

#### Procedure

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Select the "Operate as OPC server" option under "Service" in the "Runtime settings".
3. Configure the server settings at "OPC settings > OPC Unified Architecture Server configuration":

   - Change the "Port number", if required.
   - Activate at least one "SecurityPolicy" and the respective "Message security mode".
4. Save the project.
5. Download the project to the HMI device.
6. Start runtime on the HMI device.

**Note**

**Unsecured communication between client and server possible**

Use the "none" setting only for test and diagnostics purposes.

#### Result

The OPC server is accessible.

If an OPC client connects to the OPC server, the OPC server on the HMI device is started.

### Configuring DCOM user permissions in Windows (Panels, Comfort Panels, RT Advanced)

#### Introduction

The OPC DA client and OPC DA server are DCOM applications, whose security settings must be set in compliance with the DCOM security mechanisms:

- The OPC client needs launch/activation rights and access rights for the OPC DA server.
- The OPC DA server only needs access rights for the OPC DA client

The following must be known on the PCs of the OPC DA server and the OPC DA client respectively:

- The user account for which the OPC DA client is executed

#### Requirement

You have administrator rights.

#### Procedure

The procedure for configuring DCOM user rights is described on the Internet on the website of the [OPC Foundation](https://opcfoundation.org/).

For more information on assigning user rights, see the Windows documentation.

## (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Creating a connection to a WinCC OPC DA server (Panels, Comfort Panels, RT Advanced)](#creating-a-connection-to-a-wincc-opc-da-server-panels-comfort-panels-rt-advanced)
- [Creating a connection to an OPC UA server (Panels, Comfort Panels, RT Advanced)](#creating-a-connection-to-an-opc-ua-server-panels-comfort-panels-rt-advanced)
- [Accessing process values of an OPC server (Panels, Comfort Panels, RT Advanced)](#accessing-process-values-of-an-opc-server-panels-comfort-panels-rt-advanced)

### Creating a connection to a WinCC OPC DA server (Panels, Comfort Panels, RT Advanced)

### Creating a connection to an OPC UA server (Panels, Comfort Panels, RT Advanced)

#### Introduction

The OPC UA client can access process data in the hierarchical name space of an OPC UA server.

For the OPC UA client to access the process values of an OPC UA server, the OPC UA server and the OPC UA client authorize each other by exchanging certificates. In addition, you can encode the data transfer.

The OPC UA client usually classifies each certificate of an OPC UA server as a "trustworthy". How an OPC UA server responds to a connection request of the OPC UA client depends on the configuration of the OPC UA server.

In order to establish communication to an OPC UA server, inform yourself from the OPC UA server operator about the following:

- URL of the OPC UA server
- Security settings
- Required certificates

#### Requirement

URL and security settings of the OPC UA server are known.

#### Procedure

To create a connection to an OPC UA server, proceed as follows:

1. Open the "Connections" editor on the HMI device.
2. Create a new connection and enter a meaningful name.
3. Select the entry "OPC UA" as the "Communication driver".
4. In the work area, under "Parameters", configure the "OPC server":

   - Specify the "Discovery URL" of the OPC UA server or select the OPC UA server from the list.
   - Select the "Security policy"
   - Select the "Message security mode"

#### Result

The OPC UA connection is configured. You create tags to access data from the OPC UA server.

---

**See also**

[Supported OPC UA services of the OPC UA client (Panels, Comfort Panels, RT Advanced)](#supported-opc-ua-services-of-the-opc-ua-client-panels-comfort-panels-rt-advanced)

### Accessing process values of an OPC server (Panels, Comfort Panels, RT Advanced)

#### Requirement

- The OPC server to be addressed is ready-to-operate and in the "running" status
- A connection to the OPC-Server is created

#### Procedure

To access process values of an OPC-Server via the OPC connection, follow these steps:

1. On the configuration PC in the project navigation, open the "HMI tags" editor under the HMI device that you use as an OPC client.
2. Create a tag with the same data type as the tag on the OPC server.
3. Select the OPC connection for "Connection".
4. Enter the "Address", or select the desired tag on the OPC server via the object list.

#### Result

If you launch Runtime on the HMI device, the process value from the OPC server will be written to the tag on the HMI device via the OPC connection.

---

**See also**

[Permitted data types (OPC) (Panels, Comfort Panels, RT Advanced)](#permitted-data-types-opc-panels-comfort-panels-rt-advanced)
  
[Access to tags with OPC (Panels, Comfort Panels, RT Advanced)](#access-to-tags-with-opc-panels-comfort-panels-rt-advanced)

## (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Permitted data types (OPC) (Panels, Comfort Panels, RT Advanced)](#permitted-data-types-opc-panels-comfort-panels-rt-advanced)
- [Access to tags with OPC (Panels, Comfort Panels, RT Advanced)](#access-to-tags-with-opc-panels-comfort-panels-rt-advanced)
- [Supported OPC UA services of the OPC UA client (Panels, Comfort Panels, RT Advanced)](#supported-opc-ua-services-of-the-opc-ua-client-panels-comfort-panels-rt-advanced)

### Permitted data types (OPC) (Panels, Comfort Panels, RT Advanced)

### Access to tags with OPC (Panels, Comfort Panels, RT Advanced)

### Supported OPC UA services of the OPC UA client (Panels, Comfort Panels, RT Advanced)

#### OPC UA Services support

The OPC UA client supports the following OPC UA services:

- SecurityPolicy - Basic128Rsa15
- SecurityPolicy - Basic256
- SecurityPolicy - None
- DataAccess ClientFacet

You can additional information about OPC UA services in the "OPC UA Part 3 - Address Space Model 1.01 Specification" document under "§5.6".

#### Explanation of the security settings

The following table lists the security settings supported by the OPC UA client:

| SecurityPolicy | Message Security Mode |  |
| --- | --- | --- |
| None<sup>1</sup> | None |  |
| Basic128Rsa15<sup>2</sup> |  | SignAndEncrypt<sup>4</sup> |
| Basic256<sup>3</sup> | Sign |  |
| 1: The certificate exchange is disabled. Every OPC UA client can log on to the WinCC OPC UA server. This setting can be disabled on each OPC UA server. |  |  |
| 2: Certificate exchange with depth of encryption of 128 bit. |  |  |
| 3: Certificate exchange with depth of encryption of 256 bit. |  |  |
| 4: The data packages are signed with the certificates and encoded. |  |  |

> **Note**
>
> **Unsecured communication between client and server possible**
>
> Use the "none" setting only for test and diagnostics purposes.
>
> For a secure communication between client and server, use in operating mode at least the following settings:
>
> - SecurityPolicy: Basic128Rsa15
> - Message Security Mode: Sign

---

**See also**

[Creating a connection to an OPC UA server (Panels, Comfort Panels, RT Advanced)](#creating-a-connection-to-an-opc-ua-server-panels-comfort-panels-rt-advanced)
