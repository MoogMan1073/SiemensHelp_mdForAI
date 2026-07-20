---
title: "Certificates in WinCC Unified Runtime (RT Unified)"
package: WinCCUnifiedCert_enUS
topics: 174
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Certificates in WinCC Unified Runtime (RT Unified)

This section contains information on the following topics:

- [Certificates in WinCC Unified (RT Unified)](#certificates-in-wincc-unified-rt-unified)
- [Introduction (RT Unified)](#introduction-rt-unified)
- [Certificates for Unified Panels (RT Unified)](#certificates-for-unified-panels-rt-unified)
- [Certificates for Unified PCs (RT Unified)](#certificates-for-unified-pcs-rt-unified)
- [Working with certificates (RT Unified)](#working-with-certificates-rt-unified)
- [Using CA-based certificates (RT Unified)](#using-ca-based-certificates-rt-unified)
- [Using general certificates (RT Unified)](#using-general-certificates-rt-unified)
- [Using self-signed certificates (RT Unified)](#using-self-signed-certificates-rt-unified)
- [WinCC Unified Certificate Manager (RT Unified)](#wincc-unified-certificate-manager-rt-unified)

## Certificates in WinCC Unified (RT Unified)

![Figure](images/172301541387_DV_resource.Stream@PNG-en-US.png)

## Introduction (RT Unified)

This section contains information on the following topics:

- [Certificates in WinCC Unified Runtime (RT Unified)](#certificates-in-wincc-unified-runtime-rt-unified-1)
- [About this help (RT Unified)](#about-this-help-rt-unified)

### Certificates in WinCC Unified Runtime (RT Unified)

Certificates protect the communication of plants, systems and networks against cyber threats. Certificates are used for:

- The authentication
- The encryption and decryption of the transferred data

#### Certificates in WinCC Unified

**Protecting communication**

Certificates protect the security-relevant communication between the Runtime of a Unified HMI device and the communication partners of the Runtime.

The following communication is always protected through certificates:

- Unified Collaboration communication
- Unified web server communication

With respective configuration the following communication can also be protected with certificates:

- OPC UA communication
- Communication with S7-1500 controller series as of Firmware 2.9 and S7-1200 controllers as of Firmware 4.5
- WinCC Smart Server communication between a Smart Client panel und and a Smart Server

**Detecting changes to data records in Audit Trail**

The WinCC Unified Audit option uses certificates to generate a checksum for Audit Trail data records. You can determine whether the contents of a data record were changed by means of the checksum. This checksum also ensures that no lines have been added to or removed from the Audit Trail file.

Audit certificates are not used for communication with another device.

#### Plant protection through certificate authorities

Certificates issued by a certificate authority (abbreviated CA) (CA-based certificates) are unique and provide the highest level of protection for your plant.

WinCC Unified supports you:

- With the generation of the CA-based certificates of your HMI devices (Unified certificates), their installation on the HMI devices and their distribution to the communication partners of the HMI devices
- With the installation of the CA-based certificates of the communication partners (third party certificates) on the HMI devices

> **Note**
>
> **Self-signed certificates**
>
> Alternatively the use of self-signed certificates is also possible. Self-signed certificates are less secure than CA-based certificates. Their usage is subject to numerous limitations.
>
> Also when using self-signed Unified certificates, WinCC Unified supports you with the creation or installation of the certificates of the HMI device as well as with the installation of the self-signed third party certificates of its communication partners.
>
> Mixed usage is also possible. For example. a Unified OPC UA server can use a CA-based certificate, while one of its clients uses a self-signed certificate.

> **Note**
>
> **Recommendation**
>
> For security reasons the usage of CA-based certificates is recommended.

#### General certificates

WinCC Unified furthermore allows you to create general CA-based certificates for your HMI devices or other devices, for example to protection the communication of an own application.

---

**See also**

[Communication partners (RT Unified)](#communication-partners-rt-unified)
  
[Runtime and simulation (RT Unified)](#runtime-and-simulation-rt-unified)
  
[Unified certificate authority (RT Unified)](#unified-certificate-authority-rt-unified)
  
[Certificates for Unified Panels (RT Unified)](#certificates-for-unified-panels-rt-unified)
  
[Certificates for Unified PCs (RT Unified)](#certificates-for-unified-pcs-rt-unified)
  
[Workflow for using certificates on HMI devices (RT Unified)](#workflow-for-using-certificates-on-hmi-devices-rt-unified)
  
[Using general certificates (RT Unified)](#using-general-certificates-rt-unified)
  
[About this help (RT Unified)](#about-this-help-rt-unified)

### About this help (RT Unified)

#### Contents

This help describes the following:

- The certificate-bound communication between devices from the same network
- How to create certificates of a Unified HMI device and distribute them to and install them on the HMI device and its communication partners
- How to install the third-party certificates of the communication partners of an HMI device on the HMI device

Information on how to create the third-party certificates and how to install the Unified certificates on the devices of the communication partners can be found in the user help of the respective communication partner.

For the mutual SSL authentication, it is assumed that the HMI device and its communication partners use the same certificate type.

---

**See also**

[Certificates in WinCC Unified Runtime (RT Unified)](#certificates-in-wincc-unified-runtime-rt-unified-1)

## Certificates for Unified Panels (RT Unified)

This section contains information on the following topics:

- [Collaboration certificates (Panel) (RT Unified)](#collaboration-certificates-panel-rt-unified)
- [Web server certificates (Panel) (RT Unified)](#web-server-certificates-panel-rt-unified)
- [OPC UA certificates (Panel) (RT Unified)](#opc-ua-certificates-panel-rt-unified)
- [Audit certificates (Panel) (RT Unified)](#audit-certificates-panel-rt-unified)
- [Smart Server certificates for Panels (RT Unified)](#smart-server-certificates-for-panels-rt-unified)

### Collaboration certificates (Panel) (RT Unified)

This section contains information on the following topics:

- [Collaboration certificates and Runtime version (RT Unified)](#collaboration-certificates-and-runtime-version-rt-unified)
- [Workflow (Collaboration for Panels) (RT Unified)](#workflow-collaboration-for-panels-rt-unified)
- [Creating certificates (Collaboration for Panels) (RT Unified)](#creating-certificates-collaboration-for-panels-rt-unified)
- [Installing certificates (Collaboration for Panels) (RT Unified)](#installing-certificates-collaboration-for-panels-rt-unified)
- [Establishing the trust relationship (Collaboration for Panels) (RT Unified)](#establishing-the-trust-relationship-collaboration-for-panels-rt-unified)
- [Automatic trust relationship between Collaboration devices (RT Unified)](#automatic-trust-relationship-between-collaboration-devices-rt-unified)

#### Collaboration certificates and Runtime version (RT Unified)

Runtime Collaboration requires that the Collaboration certificates of 2 Collaboration partners be created with a certificate authority device whose installed Runtime version is equal to or higher than the installed Runtime version of the Collaboration partner with the higher Runtime version.

For this reason, the upgrading of Collaboration devices requires the creation, distribution and installation of new Collaboration certificates.

Example:

- A Unified PC and a Unified Panel with Runtime version V17 are Collaboration partners.
- You upgrade the Panel to V18.
- Create new Collaboration certificates for both HMI devices on a certificate authority device with installed Runtime version V18 or higher. Distribute them to and install them on the devices.

---

**See also**

[Workflow (Collaboration for Panels) (RT Unified)](#workflow-collaboration-for-panels-rt-unified)

#### Workflow (Collaboration for Panels) (RT Unified)

##### Introduction

WinCC Unified Collaboration protects the communication between the Collaboration devices through the use of certificates.

The certificates must be issued by a Unified certificate authority (CA-based certificates). You use the WinCC Unified Certificate Manager application for this.

> **Note**
>
> Certificate Manager always creates CA-based certificates. The use of CA-based certificates facilitates establishment of the trust relationship and provides the highest protection for your plant.
>
> The use of self-signed certificates is not supported for Collaboration.

##### Required certificates

For successful communication between two Collaboration devices, you need the following certificates for each Collaboration device:

- Collaboration certificate of the HMI device
- Root certificate of the certificate authority that issued the Collaboration certificate, along with its CRL file.

##### Workflow

To provide the certificates needed by a Unified Panel Collaboration device, follow these steps:

1. Create the Collaboration certificate of the Panel.
2. Install the Collaboration certificate on the Panel.
3. Restart Runtime on the Panel.
4. Establish the trust relationship between the Panel and its Collaboration partner.

---

**See also**

[Creating certificates (Collaboration for Panels) (RT Unified)](#creating-certificates-collaboration-for-panels-rt-unified)
  
[Installing certificates (Collaboration for Panels) (RT Unified)](#installing-certificates-collaboration-for-panels-rt-unified)
  
[Establishing the trust relationship (Collaboration for Panels) (RT Unified)](#establishing-the-trust-relationship-collaboration-for-panels-rt-unified)
  
[Collaboration certificates (PC) (RT Unified)](#collaboration-certificates-pc-rt-unified)
  
[Collaboration certificates and Runtime version (RT Unified)](#collaboration-certificates-and-runtime-version-rt-unified)

#### Creating certificates (Collaboration for Panels) (RT Unified)

##### Introduction

You create the Collaboration certificate of a Unified Panels on the certificate authority device. You use the WinCC Unified Certificate Manager application for this.

The certificate authority device is always a Unified PC.

##### Procedure

If you do not have a certificate authority yet, follow these steps:

1. Create the certificate authority.

   In so doing, you create the root certificate of the certificate authority and its CRL file automatically.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
2. Add the Panel to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
3. Add the Collaboration certificate to the Panel.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

If you already have a certificate authority, follow these steps:

1. If the Panel has not yet been added to the infrastructure of the certificate authority, add the Panel.

   See section [Adding devices](#adding-devices-rt-unified).
2. Add the Collaboration certificate to the Panel.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

---

**See also**

[Workflow (Collaboration for Panels) (RT Unified)](#workflow-collaboration-for-panels-rt-unified)
  
[Collaboration certificates and Runtime version (RT Unified)](#collaboration-certificates-and-runtime-version-rt-unified)

#### Installing certificates (Collaboration for Panels) (RT Unified)

##### Introduction

The Collaboration certificate of a Unified Panel is installed in the following steps:

- Export on the certificate authority device
- Import on the Panel

> **Note**
>
> You always export and import all certificates of the Panel as well as the root certificate of the issuing certificate authority and its CRL file.
>
> These certificates are automatically installed by the import.

##### Requirement

- The Collaboration certificate has been added for the Panel on the certificate authority device.

##### Procedure

1. Export the certificates of the Panel on the certificate authority device. Use the WinCC Unified Certificate Manager for this.

   See section [Exporting certificates of a Panel](#exporting-certificates-of-a-panel-rt-unified).
2. Import the certificates to the Panel. Use the Control Panel for this.

   See section [Importing and installing certificates of a Panel](#importing-and-installing-certificates-of-a-panel-rt-unified).

---

**See also**

[Workflow (Collaboration for Panels) (RT Unified)](#workflow-collaboration-for-panels-rt-unified)
  
[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)

#### Establishing the trust relationship (Collaboration for Panels) (RT Unified)

##### Introduction

Secure communication between Collaboration devices requires that the devices trust each other's Collaboration certificate.

That is automatically the case when a device trusts the root certificate of the certificate authority that issued the Collaboration certificate of the other device, and vice versa.

##### Trusting the Collaboration partner of a Panel

To ensure that a Unified Panel trusts its Collaboration partner, follow these steps:

1. Check whether the Panel already trusts the root certificate of its Collaboration partner.

   See sections [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified) and [Automatic trust relationship between Collaboration devices](#automatic-trust-relationship-between-collaboration-devices-rt-unified).
2. If the Panel does not yet trust the root certificate, install it manually.

   See section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified).

---

**See also**

[Workflow (Collaboration for Panels) (RT Unified)](#workflow-collaboration-for-panels-rt-unified)

#### Automatic trust relationship between Collaboration devices (RT Unified)

This section describes cases in which a Collaboration device automatically trusts the certificate of its Collaboration partner. You do not have to establish the trust relationship manually.

##### Same certificate authority

Requirement:

- The Collaboration certificates of both devices have the same certificate authority. That is, the certificates have the same root certificate.
- The own Collaboration certificate has been installed on each device

  During installation of this certificate, the root certificate is also automatically installed on the device. It is installed in the folder containing the trusted certificate authorities.

Result:

The first time the connection is established for Collaboration, the devices check the Collaboration certificate of their Collaboration partner. Since they already trust the root certificate, the Collaboration certificate is automatically installed in the folder with the trusted certificates.

##### Trusted certificate authority

Requirement:

- The Collaboration certificates of the Collaboration devices have different certificate authorities. That is, the certificates have different root certificates.
- One Collaboration device has a communication partner whose application certificate was issued by the same certificate authority as the Collaboration certificate of its Collaboration partner. The device already trusts the certificate authority of this communication partner.

Result:

- The first time the connection is established for Collaboration, the device checks the Collaboration certificate of the Collaboration partner.
- Since the device already trusts the root certificate of the other communication partner, it automatically installs the Collaboration certificate in the folder with the trusted certificates.

  > **Note**
  >
  > For successful Collaboration communication, the devices must trust each other. Check on the other Collaboration device to determine if it also already trusts the root certificate. See section [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified).
  >
  > Establish the trust relationship there manually, if necessary.

Example**:**

A Panel communicates with a second Panel using Unified Collaboration. The Collaboration application certificates of the Panels have different certificate authorities. Both Panels already trust the root certificates of their Collaboration partner.

For the first Panel, a Unified PC is configured as an additional Collaboration partner. The Collaboration application certificate of the PC has the same certificate authority and, thus, the same root certificate as the second Panel.

Since the first Panel already trusts the root certificate of the second Panel, it automatically also trusts the Collaboration application certificate of the PC.

---

**See also**

[Establishing the trust relationship (Collaboration for Panels) (RT Unified)](#establishing-the-trust-relationship-collaboration-for-panels-rt-unified)

### Web server certificates (Panel) (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-1)
- [Using a CA-based certificate (Panel as web server) (RT Unified)](#using-a-ca-based-certificate-panel-as-web-server-rt-unified)
- [Using a self-signed certificate (Panel as web server) (RT Unified)](#using-a-self-signed-certificate-panel-as-web-server-rt-unified)

#### Introduction (RT Unified)

##### Basics of web server communication

WinCC Unified protects the communication between a Runtime web server and its web clients through the use of a web server certificate. The clients must trust the web server certificate (one-way SSL authentication).

The web server certificate can be issued by a Unified certificate authority (CA-based certificate) or be self-signed.

> **Note**
>
> For security reasons, it is recommended to use a CA-based certificate. You use the "WinCC Unified Certificate Manager" application to create the certificate.
>
> You can find help on choosing a certificate type in section [Selecting a suitable certificate type](#selecting-a-suitable-certificate-type-rt-unified).

The procedure for creating the web server certificate, installing it on the web server device and establishing the trust relationship with the web server on the clients depends on the chosen certificate type.

---

**See also**

[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
  
[Workflow with a self-signed certificate (Panel as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-panel-as-web-server-rt-unified)
  
[Unified certificate authority (RT Unified)](#unified-certificate-authority-rt-unified)

#### Using a CA-based certificate (Panel as web server) (RT Unified)

This section contains information on the following topics:

- [Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
- [Creating certificates (Panel as web server) (RT Unified)](#creating-certificates-panel-as-web-server-rt-unified)
- [Installing certificates (Panel as web server) (RT Unified)](#installing-certificates-panel-as-web-server-rt-unified)
- [Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)
- [Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified)
- [Automatic trust relationship with a Panel web server (RT Unified)](#automatic-trust-relationship-with-a-panel-web-server-rt-unified)
- [Installing the root certificate for Edge and Chrome (RT Unified)](#installing-the-root-certificate-for-edge-and-chrome-rt-unified)
- [Installing the root certificate for Firefox (RT Unified)](#installing-the-root-certificate-for-firefox-rt-unified)
- [Installing the root certificate on iOS devices (RT Unified)](#installing-the-root-certificate-on-ios-devices-rt-unified)
- [Installing the root certificate for the web browser of a Panel (RT Unified)](#installing-the-root-certificate-for-the-web-browser-of-a-panel-rt-unified)

##### Workflow with a CA-based certificate (Panel as web server) (RT Unified)

If you are using a Unified Panel as a Runtime web server and want to use a CA-based web server certificate, you need the following certificates:

- Web server certificate of the Panel
- Root certificate of the certificate authority that issued the web server certificate, along with its CRL file.

###### Requirement

- Web-based client access has been enabled for the Panel.

###### Procedure

1. Create the web server certificate of the Panel.

   See section [Creating certificates (Panel as web server)](#creating-certificates-panel-as-web-server-rt-unified).
2. Install the web server certificate on the Panel.

   See section [Installing certificates (Panel as web server)](#installing-certificates-panel-as-web-server-rt-unified).
3. Establish the trust relationship with the web server on the web clients.

   See section [Establishing the trust relationship with the web server](#establishing-the-trust-relationship-with-the-web-server-rt-unified).

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-1)
  
[Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)
  
[Trusting the Panel web server on the web client (RT Unified)](#trusting-the-panel-web-server-on-the-web-client-rt-unified)

##### Creating certificates (Panel as web server) (RT Unified)

###### Introduction

You create the CA-based web server certificate of a Unified Panels on the certificate authority device. You use the WinCC Unified Certificate Manager application for this.

The certificate authority device is always a Unified PC.

###### Procedure

If you do not have a certificate authority yet, follow these steps:

1. Create the certificate authority.

   In so doing, you create the root certificate of the certificate authority and its CRL file automatically.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
2. Add the Panel to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
3. Add the web server certificate to the Panel.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

If you already have a certificate authority, follow these steps:

1. If the Panel has not yet been added to the infrastructure of the certificate authority, add the web server Panel.

   See section [Adding devices](#adding-devices-rt-unified).
2. Add the web server certificate to the Panel.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

---

**See also**

[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)

##### Installing certificates (Panel as web server) (RT Unified)

###### Introduction

The web server certificate of a Unified Panel is installed in the following steps:

- Export on the certificate authority device
- Import to the Panel

> **Note**
>
> You always export and import all certificates of the Panel as well as the root certificate of the issuing certificate authority and its CRL file.
>
> These certificates are automatically installed by the import.

###### Requirement

- The web server certificate has been added for the Panel on the certificate authority device.

###### Procedure

1. Export the certificates of the Panel on the certificate authority device. Use the WinCC Unified Certificate Manager for this.

   See section [Exporting certificates of a Panel](#exporting-certificates-of-a-panel-rt-unified).
2. Import the certificates to the Panel. Use the Control Panel for this.

   See section [Importing and installing certificates of a Panel](#importing-and-installing-certificates-of-a-panel-rt-unified).

> **Note**
>
> The import installs the web server certificate and binds it to the Runtime web page of the Panel.
>
> The web page is then restarted to enforce the use of the new certificate. Any connected web clients are thereby disconnected and must log in again.

---

**See also**

[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
  
[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)

##### Establishing the trust relationship with the web server (RT Unified)

###### Introduction

Secure communication between a Unified Runtime web server and its web clients requires that the clients trust the web server certificate.

That is automatically the case when a client trusts the root certificate of the certificate authority that issued the web server certificate.

###### Timing

You can establish the trust relationship on a planned or as needed basis:

- Planned: You install the root certificate before the client attempts to connect to the web server for the first time.

  The client then already trusts the web server certificate the first time a connection is established.
- As needed: You install the root certificate when the client first attempts to connect to the web server.

  If the root certificate of the web server has not yet been installed at that time, you can download it on the Unified home page and then install it in the client.

###### Installing the root certificate before a connection is established for the first time

| 1. If applicable, check whether the client already trusts the root certificate of the web server.     See sections [Checking the status of the web server root certificate on the web client.](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified) and [Automatic trust relationship with a Panel web server](#automatic-trust-relationship-with-a-panel-web-server-rt-unified). 2. If the client already trusts the root certificate, you don't have to do anything.    If the client does not trust the root certificate, install it manually in the certificate store of the browser.        | Utilized browser | Certificate store used by the browser | For procedure, see section |    | --- | --- | --- |    | Edge and Chrome on Windows | Windows system certificate store | [Installing the root certificate before the first connection (Edge and Chrome)](#installing-the-root-certificate-before-the-first-connection-edge-and-chrome-rt-unified) |    | Firefox on Windows | Certificate store of Firefox | [Installing the root certificate before the first connection (for Firefox)](#installing-the-root-certificate-before-the-first-connection-for-firefox-rt-unified) |    | Web browser of a Unified Panel | Certificate store of the Panel | [Installing the root certificate before the first connection (Panel web browser)](#installing-the-root-certificate-before-the-first-connection-panel-web-browser-rt-unified) |    | Browser on iOS devices | System certificate store of the iOS device | [Installing the root certificate on iOS devices before the first connection](#installing-the-root-certificate-on-ios-devices-before-the-first-connection-rt-unified) | |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

###### Installing the root certificate at the first connection attempt

Follow the steps below according to the browser:

| Browser | Certificate store used by the browser | For procedure, see section |
| --- | --- | --- |
| Edge and Chrome on Windows | Windows system certificate store | [Installing the root certificate at the first connection (Edge and Chrome)](#installing-the-root-certificate-at-the-first-connection-edge-and-chrome-rt-unified) |
| Firefox on Windows | Certificate store of Firefox | [Installing the root certificate at the first connection (for Firefox)](#installing-the-root-certificate-at-the-first-connection-for-firefox-rt-unified) |
| Web browser of a Unified Panel | Certificate store of the Panel | [Installing the root certificate at the first connection (Panel web browser)](#installing-the-root-certificate-at-the-first-connection-panel-web-browser-rt-unified) |
| Browser on iOS devices | System certificate store of the iOS device | [Installing the root certificate on iOS devices at the first connection](#installing-the-root-certificate-on-ios-devices-at-the-first-connection-rt-unified) |

---

**See also**

[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)

##### Checking the status of the web server root certificate on the web client. (RT Unified)

###### Introduction

This section describes how to check whether a web client already trusts the root certificate of a Runtime web server.

In that case, the root certificate has been installed in the certificate store of the web client in the folder containing the trusted certificate authorities.

###### Procedure for Microsoft Edge and Chrome as web client

Microsoft Edge and Chrome use the Windows system certificate store.

Use Windows &gt; Search "Manage computer certificates" to check whether the root certificate has been installed under "Certificates - Local Computer" &gt; "Trusted Root Certification Authorities" &gt; "Certificates".

###### Procedure for Firefox

Firefox uses its own dedicated certificate store.

To check the status of a certificate, follow these steps:

1. Open the "Settings" page of Firefox.
2. Select "Privacy &amp; Security".
3. Click "View Certificates" in the "Certificates" area.
4. Select the "Authorities" tab in the "Certificate Manager" window.
5. Check whether the root certificate is included in the list of trusted authorities.

###### Procedure for iOS devices

Follow the procedure described in the user help of the manufacturer.

###### Procedure for "Web browser" of a Unified Panel

"Web browser" of the Unified Panel uses the certificate store of the Panel.

To check whether the Panel already trusts the root certificate, follow the procedure described in section [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified).

##### Automatic trust relationship with a Panel web server (RT Unified)

This section describes cases in which a web client automatically trusts the CA-based certificate of a Unified Panel web server. You do not have to establish the trust relationship manually.

###### Edge or Chrome as client and same certificate authority

Requirement

- You use Microsoft Edge or Chrome as web client.
- The clients have been installed on a Unified PC.
- The web server certificate of the Panel and at least one application certificate of the client PC were issued by the same certificate authority. That is, they have the same root certificate.

Result:

- During installation of the certificates of the Unified PC, WinCC Unified Certificate Manager also installs the root certificate in the system certificate store of Windows. Microsoft Edge and Chrome use this certificate store.
- Since the clients already trust the root certificate, the web server certificate is automatically installed in the folder with the trusted certificates when a connection is established for the first time.
- The connection between the client and web server is secure from the outset.

###### Communicating with multiple web servers of the same certificate authority

Requirement:

- The web server certificates of two Unified Runtime web servers were issued by the same certificate authority. That is, they have the same root certificate.
- The web client already trusts the root certificate of one of the Unified Runtime web servers.
- The client connects to the second web server.

Result:

- The client already trusts the root certificate at the first connection attempt. For this reason, the web server certificate of the second web server is automatically installed in the folder with the trusted certificates when the connection is established.
- The connection between the web client and web server is secure from the outset.

---

**See also**

[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)

##### Installing the root certificate for Edge and Chrome (RT Unified)

This section contains information on the following topics:

- [Installing the root certificate before the first connection (Edge and Chrome) (RT Unified)](#installing-the-root-certificate-before-the-first-connection-edge-and-chrome-rt-unified)
- [Installing the root certificate at the first connection (Edge and Chrome) (RT Unified)](#installing-the-root-certificate-at-the-first-connection-edge-and-chrome-rt-unified)

###### Installing the root certificate before the first connection (Edge and Chrome) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on an Edge or Chrome web client before the client connects to the web server for the first time. The description applies to clients installed on Windows devices.

The procedure is explained using Edge as an example. The procedure is the same for Chrome.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager.

  See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
- The web server root certificate has been exported on the certificate authority device with Certificate Manager to a storage location the web client can access.

  See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).

  > **Note**
  >
  > **Alternative**
  >
  > If a Unified PC belongs to the infrastructure of the certificate authority of the web server whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.
  >
  > See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).
- Microsoft Edge or Chrome has been installed on the web client device.

###### Procedure

1. Double-click the root certificate file on the web client device.

   The root certificate is opened with the Windows standard form.

   ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)
2. Click "Install Certificate".
3. In the certificate import wizard, select "Local Machine" as the storage location and "Trusted Root Certification Authority" as the certificate store.
4. Start the import.
5. (optional) Check whether the root certificate was successfully installed in the Windows system certificate store.

   See section [Checking the status of the web server root certificate on the web client.](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified).

###### Result

At the first call of the web server web page, the browser trusts the root certificate of the web server and, thus, it automatically also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)
  
[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)

###### Installing the root certificate at the first connection (Edge and Chrome) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) at the first connection attempt of an Edge or Chrome web client. The description applies to clients installed on Windows devices.

The procedure is explained using Edge as an example. The procedure is the same for Chrome.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager. It has been installed on the web server.
- A Runtime project is running on the web server.
- Microsoft Edge or Chrome has been installed on the web client device.
- The web server root certificate has not yet been installed in the Windows system certificate store of the client device.
- The client device has access to the web server.

###### Procedure

1. Start Microsoft Edge on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed:

   ![Procedure](images/129763286923_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129763286923_DV_resource.Stream@PNG-de-DE.png)
3. Open the field with the error details and confirm that you want to open the web page.

   The WinCC Unified home page is loaded.
4. On the home page, select the "Certificate Authority" field and confirm "Open file" in the download dialog.

   ![Procedure](images/129766055435_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129766055435_DV_resource.Stream@PNG-de-DE.png)

   The root certificate is downloaded to the default download directory.
5. Double-click the downloaded file.

   The root certificate is opened with the Windows standard form.

   ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)
6. Click "Install Certificate".
7. In the certificate import wizard, select "Local Machine" as the storage location and "Trusted Root Certification Authority" as the certificate store.
8. Start the import.
9. (optional) Check whether the root certificate was successfully installed in the Windows system certificate store.

   See section [Checking the status of the web server root certificate on the web client.](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified).
10. Reload the page.

**Note**

**URL of a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the root certificate of the web server and, thus, it also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)
  
[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

##### Installing the root certificate for Firefox (RT Unified)

This section contains information on the following topics:

- [Installing the root certificate before the first connection (for Firefox) (RT Unified)](#installing-the-root-certificate-before-the-first-connection-for-firefox-rt-unified)
- [Installing the root certificate at the first connection (for Firefox) (RT Unified)](#installing-the-root-certificate-at-the-first-connection-for-firefox-rt-unified)

###### Installing the root certificate before the first connection (for Firefox) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on a Firefox web client before the client connects to the web server for the first time. The description applies to clients installed on Windows devices.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager.

  See also section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
- The web server root certificate has been exported on the certificate authority device with Certificate Manager to a storage location the web client can access.

  See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).

  > **Note**
  >
  > **Alternative**
  >
  > If a Unified PC belongs to the infrastructure of the certificate authority of the web server whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.
  >
  > See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).
- Firefox has been installed on the web client device.

###### Procedure

1. Start Firefox on the web client device.
2. Install the root certificate in the certificate store of Firefox. To do this, follow these steps:

   - Open the "Settings" page of Firefox.
   - Select "Privacy &amp; Security".
   - Click "View Certificates" in the "Certificates" area.
   - Select the "Authorities" tab in the "Certificate Manager" window:

     ![Procedure](images/142189917195_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/142189917195_DV_resource.Stream@PNG-en-US.png)
   - Click "Import" and select the root certificate file.
   - In the window that opens, select the option "This certificate can identify websites" and confirm your selection.

###### Result

At the first call of the web server web page, the browser trusts the root certificate of the web server and, thus, it automatically also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)
  
[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)

###### Installing the root certificate at the first connection (for Firefox) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on a Firefox web client when the client first attempts to connect to the web server. The description applies to clients installed on Windows devices.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager. It has been installed on the web server.
- A Runtime project is running on the web server.
- Firefox has been installed on the web client device.
- The web server root certificate has not yet been installed in the certificate store of the browser.
- The client device has access to the web server.

###### Procedure

1. Start Firefox on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed.
3. Open the "Advanced" field and confirm the "Accept the Risk and Continue" field.
4. An exception is entered for this page in the Firefox Certificate Manager.
5. On the WinCC Unified home page, select the "Certificate Authority" field.
6. Save the root certificate. To do this, click "Save file" in the Firefox dialog that follows.
7. Install the root certificate in the certificate store of Firefox. To do this, follow these steps:

   - Open the "Settings" page of Firefox.
   - Select "Privacy &amp; Security".
   - Click "View Certificates" in the "Certificates" area.
   - Select the "Authorities" tab in the "Certificate Manager" window:

     ![Procedure](images/142189917195_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/142189917195_DV_resource.Stream@PNG-en-US.png)
   - Click "Import" and select the root certificate file.
   - In the window that opens, select the option "This certificate can identify websites" and confirm your selection.
   - Click "Servers" and remove the exception that was created by step 2.
8. Reload the page.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the root certificate of the web server and, thus, it also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)
  
[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)

##### Installing the root certificate on iOS devices (RT Unified)

This section contains information on the following topics:

- [Installing the root certificate on iOS devices before the first connection (RT Unified)](#installing-the-root-certificate-on-ios-devices-before-the-first-connection-rt-unified)
- [Installing the root certificate on iOS devices at the first connection (RT Unified)](#installing-the-root-certificate-on-ios-devices-at-the-first-connection-rt-unified)

###### Installing the root certificate on iOS devices before the first connection (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on an iOS web client before the client connects to the web server for the first time.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager.
- The web server root certificate has been exported on the certificate authority device with Certificate Manager to a storage location.

  See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).

  > **Note**
  >
  > **Alternative**
  >
  > If a Unified PC belongs to the infrastructure of the certificate authority of the web server whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.
  >
  > See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).
- The web client device has access to the root certificate file, for example, because the file was sent to the device via email.
- The desired browser has been installed on the web client device.

###### Procedure

1. Tap the root certificate file on the iOS device.

   You are informed that the website is trying to load a configuration profile.
2. Tap "Allow"

   The configuration profile is loaded.
3. Tap "Close".
4. Select "Settings &gt; General &gt; Profile" on the device.
5. Tap the configuration profile you just loaded.
6. Tap "Install" at the top right.

   ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)
7. Tap "Install" again at the top right.

   ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)
8. Tap "Install" again in the "Profile" confirmation prompt:

   ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

   The certificate is installed.
9. Select "Settings &gt; General &gt; About &gt; Certificate Trust Settings" on the device:

   ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)
10. Select the "Enable full trust for root certificates" option for the web server root certificate.

###### Result

At the first call of the web server web page, the browser trusts the root certificate of the web server and, thus, it automatically also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)
  
[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

###### Installing the root certificate on iOS devices at the first connection (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on an iOS web client when the client first attempts to connect to the web server.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager. It has been installed on the web server.
- A Runtime project is running on the web server.
- The desired browser has been installed on the web client device.
- The web server root certificate has not yet been installed in the certificate store of the browser.
- The client device has access to the web server.

###### Procedure

1. Start the browser on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   A warning message is displayed.
3. Open the details for the message and select the button for loading the page.

   The WinCC Unified home page is loaded.
4. Load the root certificate to your device. Follow these steps:

   - On the home page, select the "Certificate Authority" field.

     ![Procedure](images/129766055435_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129766055435_DV_resource.Stream@PNG-de-DE.png)

     A pop-up opens. It informs you that the website is trying to load a configuration profile.
   - Tap "Allow"

     The configuration profile is loaded.
   - Tap "Close".
5. Install the configuration profile on your device. Follow these steps:

   - Select "Settings &gt; General &gt; Profile" on the device.
   - Tap the configuration profile you just loaded.
   - Tap "Install" at the top right.

     ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)
   - Tap "Install" again at the top right.

     ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)
   - Tap "Install" again in the "Profile" confirmation prompt:

     ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

     The root certificate is installed.

     You see the entry "Verified".

     ![Procedure](images/129772977419_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772977419_DV_resource.Stream@PNG-de-DE.png)
   - Select "General &gt; About &gt; Certificate Trust Settings".

     ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)
   - Select "WinCC Unified CA" and select "Next".

     ![Procedure](images/129773533707_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129773533707_DV_resource.Stream@PNG-de-DE.png)
6. Load the Unified home page again.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the root certificate of the web server and, thus, it also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)
  
[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

##### Installing the root certificate for the web browser of a Panel (RT Unified)

This section contains information on the following topics:

- [Installing the root certificate before the first connection (Panel web browser) (RT Unified)](#installing-the-root-certificate-before-the-first-connection-panel-web-browser-rt-unified)
- [Installing the root certificate at the first connection (Panel web browser) (RT Unified)](#installing-the-root-certificate-at-the-first-connection-panel-web-browser-rt-unified)

###### Installing the root certificate before the first connection (Panel web browser) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server in the web browser of a Unified Panel before the browser connects to the web server for the first time.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager.
- The web server root certificate has been exported on the certificate authority device with Certificate Manager to a storage location the web client can access.

  See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).

  > **Note**
  >
  > **Alternative**
  >
  > If a Unified PC belongs to the infrastructure of the certificate authority of the web server whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.
  >
  > See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

###### Procedure

Web browser uses the certificate store of the Panel. To install the root certificate there, follow the procedure described in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified).

###### Result

At the first call of the web server web page, the browser trusts the root certificate of the web server and, thus, it automatically also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)
  
[Checking the status of a root certificate on the HMI device (RT Unified)](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified)
  
[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)

###### Installing the root certificate at the first connection (Panel web browser) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) in the web browser of a Unified Panel when the web browser first attempts to connect to the web server.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager. It has been installed on the web server.
- A Runtime project is running on the web server.
- The web server root certificate has not yet been installed in the certificate store of the Panel.
- The Panel has access to the web server.

###### Procedure

1. Start the "Web browser" application on the Panel.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed.
3. Open the field with the error details and confirm that you want to open the web page.

   The WinCC Unified home page is loaded.
4. On the home page, select the "Certificate Authority" field and confirm "Open file" in the download dialog.

   The root certificate is downloaded.
5. Web browser uses the certificate store of the Panel. Install the root certificate there. Follow the procedure described in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified).

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

Web browser trusts the root certificate of the web server and, thus, it also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Checking the status of a root certificate on the HMI device (RT Unified)](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified)
  
[Workflow with a CA-based certificate (Panel as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-panel-as-web-server-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

#### Using a self-signed certificate (Panel as web server) (RT Unified)

This section contains information on the following topics:

- [Workflow with a self-signed certificate (Panel as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-panel-as-web-server-rt-unified)
- [Trusting the Panel web server on the web client (RT Unified)](#trusting-the-panel-web-server-on-the-web-client-rt-unified)

##### Workflow with a self-signed certificate (Panel as web server) (RT Unified)

A Unified Panel that is used as a Runtime web server can use a self-signed web server certificate.

> **Note**
>
> Self-signed certificates provide less protection than CA-based certificates. Use them for testing, for example. It is recommended that they then be replaced with CA-based certificates.

###### Limitations

- The self-signed web server certificate has a lifetime of 12 months.
- If no CA-based web server certificate has been installed on the Panel, each Runtime restart creates a new self-signed web server certificate. You must install the certificate on the web clients as a trusted certificate.

###### Requirement

- Web-based client access has been enabled for the Unified Panel.

###### Procedure

1. Stop Runtime on the Panel.
2. Check whether a CA-based web server certificate has already been installed on the Panel in the own application certificates. If so, uninstall it.

   See section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified).
3. Start Runtime on the Panel.

   A self-signed web server certificate is created, installed on the Panel and bound to the Runtime web page.

   The certificate is bound to the IP address and device name/FQDN of the Panel.
4. Trust the web server certificate on the web clients. See section [Trusting the Panel web server on the web client](#trusting-the-panel-web-server-on-the-web-client-rt-unified).

**Note**

Repeat this step after each Runtime start or Panel restart.

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-1)

##### Trusting the Panel web server on the web client (RT Unified)

This section contains information on the following topics:

- [Installing the self-signed web server certificate for Edge and Chrome (RT Unified)](#installing-the-self-signed-web-server-certificate-for-edge-and-chrome-rt-unified)
- [Installing the self-signed web server certificate for Firefox (RT Unified)](#installing-the-self-signed-web-server-certificate-for-firefox-rt-unified)
- [Installing the self-signed web server certificate for an iOS device (RT Unified)](#installing-the-self-signed-web-server-certificate-for-an-ios-device-rt-unified)
- [Installing the self-signed web server certificate for the web browser of a Panel (RT Unified)](#installing-the-self-signed-web-server-certificate-for-the-web-browser-of-a-panel-rt-unified)

###### Installing the self-signed web server certificate for Edge and Chrome (RT Unified)

###### Introduction

This section describes how to install the self-signed web server certificate of a Runtime web server (Unified PC or Unified Panel) on an Edge or Chrome web client on Windows.

The procedure is explained using Edge as an example. The procedure is the same for Chrome.

###### Requirement

- The Runtime web server uses a self-signed web server certificate.
- A Runtime project is running on the web server.
- Microsoft Edge or Chrome has been installed on the web client device.
- The client device has access to the web server.

###### Procedure

1. Start Microsoft Edge on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   Edge warns you that the connection is not secure.
3. Download the certificate. To do this, follow these steps:

   - Click the triangle with the exclamation point in the address bar:

     ![Procedure](images/169984863115_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/169984863115_DV_resource.Stream@PNG-de-DE.png)
   - Click the notice that the connection to the website is not secure:

     ![Procedure](images/169989134091_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/169989134091_DV_resource.Stream@PNG-de-DE.png)
   - Click the "Show certificate" icon:

     ![Procedure](images/169989629323_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/169989629323_DV_resource.Stream@PNG-de-DE.png)
   - Click "Export" in the "Details" tab.
   - Select a storage location and save the certificate.
4. Install the certificate in the certificate store of Windows. To do this, follow these steps:

   - Double-click the downloaded certificate file.

     The certificate is opened with the Windows standard form.

     ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)
   - Click "Install Certificate".
   - In the certificate import wizard, select "Local Machine" as the storage location and "Trusted Root Certification Authority" as the certificate store.
   - Start the import.
5. Reload the page.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the self-signed web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified)
  
[Workflow with a self-signed certificate (Panel as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-panel-as-web-server-rt-unified)

###### Installing the self-signed web server certificate for Firefox (RT Unified)

###### Introduction

This section describes how to install the self-signed web server certificate of a Runtime web server (Unified PC or Unified Panel) on a Firefox web client on Windows.

###### Requirement

- The Runtime web server uses a self-signed web server certificate.
- A Runtime project is running on the web server.
- Firefox has been installed on the web client device.
- The client device has access to the web server.

###### Procedure

1. Start Firefox on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed.
3. Download the certificate. To do this, follow these steps:

   - Open the "Advanced" field.
   - Click "More Information".

     A dialog with the page information opens.
   - Click "Security &gt; View Certificate".

     A tab with the certificate information opens.
   - Click "PEM (certificate)" under "Miscellaneous &gt; Save".
   - Select a storage location and save the certificate.
4. Install the certificate in the certificate store of Firefox. To do this, follow these steps:

   - Open the "Settings" page of Firefox.
   - Select "Privacy &amp; Security".
   - Click "View Certificates" in the "Certificates" area.
   - Click "Import" and select the certificate file.
5. Reload the page.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the self-signed web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a self-signed certificate (Panel as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-panel-as-web-server-rt-unified)

###### Installing the self-signed web server certificate for an iOS device (RT Unified)

###### Introduction

This section describes how to install the self-signed web server certificate of a Runtime web server (Unified PC or Unified Panel) on the web client of an iOS device.

The procedure is explained using Safari as an example. The procedure is the same for other browsers.

###### Requirement

- A self-signed web server certificate has been installed on the web server HMI device.
- A Runtime project is running on the web server.
- The client device is an iOS device.
- The device has access to the web server.
- Safari has been installed on the device.

###### Procedure

1. Start Safari on the HMI device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed.
3. Load the self-signed web server certificate to your device. Follow these steps:

   - CHECK: How? / Click where?   
     Is the self-signed certificate also considered a configuration profile?

     A pop-up opens. It informs you that the website is trying to load a configuration profile.
   - Tap "Allow".

     The configuration profile is loaded.
   - Tap "Close".
4. Install the configuration profile on your device. Follow these steps:

   - Select "Settings &gt; General &gt; Profile" on the device.
   - Tap the configuration profile you just loaded.
   - Tap "Install" at the top right.

     ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)
   - Tap "Install" again at the top right.

     ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)
   - Tap "Install" again in the "Profile" confirmation prompt:

     ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

     The certificate is installed.
   - Select "Settings &gt; General &gt; About &gt; Certificate Trust Settings" on the device:

     ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)
   - Select the "Full trust for root certificates" option for the certificate.
5. (optional) Check whether the web server certificate was successfully installed.

   Follow the same procedure as you use to check whether a web server root certificate has been installed on the web client.
6. Load the Unified home page again.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the self-signed web server certificate.

You can log in to Runtime with a secure connection.

###### Alternative procedure

1. Export the self-signed web server certificate on the device of another web client that communicates with the same web server, e.g. with Edge.
2. Transfer the certificate to the iOS device, for example, by sending it as an email attachment and downloading the attachment to the iOS device.

   A pop-up opens. It informs you that the website is trying to load a configuration profile.
3. Tap "Allow".

   The configuration profile is loaded.
4. Tap "Close".
5. Continue as described above, starting from step 4.

---

**See also**

[Workflow with a self-signed certificate (Panel as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-panel-as-web-server-rt-unified)
  
[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified)

###### Installing the self-signed web server certificate for the web browser of a Panel (RT Unified)

###### Introduction

This section describes how to install the self-signed web server certificate of a Runtime web server (Unified PC or Unified Panel) in the web browser of a Unified Panel.

###### Requirement

- A self-signed web server certificate has been installed on the web server HMI device.
- A Runtime project is running on the web server.
- The client device has access to the web server.

###### Procedure

1. Start the "Web browser" application on the Panel.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   The browser warns you that the connection is not secure.
3. Display the details for the connection.
4. Display the certificate.
5. Download the certificate.

   The certificate is loaded into the certificate store of the Panel. The Panel does not yet trust the certificate.
6. Trust the certificate with "Control Panel &gt; Security &gt; Certificates".
7. Reload the page in the web browser.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The web browser trusts the self-signed web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a self-signed certificate (Panel as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-panel-as-web-server-rt-unified)
  
[Importing and installing root certificates and CRL files on Panels (RT Unified)](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified)

### OPC UA certificates (Panel) (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-2)
- [Using CA-based certificates (OPC UA for Panel) (RT Unified)](#using-ca-based-certificates-opc-ua-for-panel-rt-unified)
- [Using a default self-signed certificate (Panel as OPC UA server) (RT Unified)](#using-a-default-self-signed-certificate-panel-as-opc-ua-server-rt-unified)
- [Engineering System as OPC UA client (RT Unified)](#engineering-system-as-opc-ua-client-rt-unified)

#### Introduction (RT Unified)

If the OPC UA server uses a security policy, the OPC UA communication is protected through the use of certificates. The OPC UA server must trust the OPC UA certificates of its clients, and vice versa (mutual SSL authentication).

##### Panel as OPC UA server

If you are using a Unified Panel as an OPC UA server, its OPC UA server certificate can be issued by a certificate authority (CA-based certificate) or be self-signed.

> **Note**
>
> For security reasons, it is recommended to use a CA-based certificate. You use WinCC Unified Certificate Manager to create the certificate.

> **Note**
>
> For Panels that are used as OPC UA servers, a tag export to an OPC UA NodeSet XML file is not possible.

##### Panel as OPC UA client

A Unified Panel that is used as an OPC UA client must use a certificate issued by a Unified certificate authority (CA-based certificate). You use WinCC Unified Certificate Manager to create the certificate.

> **Note**
>
> If you are using a Panel as an OPC UA client, the Engineering System also acts as an OPC UA client during configuration of the device. See section [Engineering System as OPC UA client](#engineering-system-as-opc-ua-client-rt-unified).

##### Contents of this help

This help describes the following:

- Creating a CA-based OPC UA server certificate or OPC UA client certificate of the Panel
- Installing the CA-based certificate on the Panel
- Using the default self-signed certificate for Panel as OPC UA server
- Establishing the trust relationship with the OPC UA communication partner on the Panel
- Distributing the OPC UA certificate of the Panel to the OPC UA communication partner

  This step sets up the establishment of the trust relationship with the Panel on the OPC UA communication partner.

> **Note**
>
> **Procedure at the OPC UA communication partners**
>
> For information on how to create and install the OPC UA certificate of the communication partner and distribute it to the Panel and how to trust the certificate of the Panel on the communication partner, refer to the operating instructions of the respective communication partner.

---

**See also**

[CA-based certificate workflow (OPC UA for Panel) (RT Unified)](#ca-based-certificate-workflow-opc-ua-for-panel-rt-unified)
  
[Using a default self-signed certificate (Panel as OPC UA server) (RT Unified)](#using-a-default-self-signed-certificate-panel-as-opc-ua-server-rt-unified)
  
[Selecting a suitable certificate type (RT Unified)](#selecting-a-suitable-certificate-type-rt-unified)

#### Using CA-based certificates (OPC UA for Panel) (RT Unified)

This section contains information on the following topics:

- [CA-based certificate workflow (OPC UA for Panel) (RT Unified)](#ca-based-certificate-workflow-opc-ua-for-panel-rt-unified)
- [Creating certificates (OPC UA for Panel) (RT Unified)](#creating-certificates-opc-ua-for-panel-rt-unified)
- [Installing certificates (OPC UA for Panel) (RT Unified)](#installing-certificates-opc-ua-for-panel-rt-unified)
- [Establishing the trust relationship (OPC UA for Panel) (RT Unified)](#establishing-the-trust-relationship-opc-ua-for-panel-rt-unified)
- [Automatic trust relationship in OPC UA communication (RT Unified)](#automatic-trust-relationship-in-opc-ua-communication-rt-unified)

##### CA-based certificate workflow (OPC UA for Panel) (RT Unified)

For CA-based OPC UA communication, a Unified Panel needs the following certificates:

- OPC UA application certificate suitable for the role of the Panel during OPC UA communication:

  - OPC UA server certificate  
    or
  - OPC UA client certificate
- Root certificate of the certificate authority that issued the OPC UA application certificate of the Panel, along with its CRL file.

###### Requirement

- The OPC UA server uses a security policy.
- The OPC UA communication partner of the Panel has an OPC UA application certificate that was issued by a certificate authority.
- The certificate has been installed on the communication partner as an own certificate.

###### Workflow

1. Create an OPC UA server certificate or an OPC UA client certificate for the Panel, depending on the role of the Panel.

   See section [Creating certificates (OPC UA for Panel)](#creating-certificates-opc-ua-for-panel-rt-unified).
2. Install the certificate on the Panel.

   See section [Installing certificates (OPC UA for Panel)](#installing-certificates-opc-ua-for-panel-rt-unified).
3. Restart Runtime on the Panel.
4. Establish the trust relationship between the Panel and its OPC UA communication partner.

   See section [Establishing the trust relationship (OPC UA for Panel)](#establishing-the-trust-relationship-opc-ua-for-panel-rt-unified).

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-2)

##### Creating certificates (OPC UA for Panel) (RT Unified)

###### Introduction

You create the OPC UA server certificate or OPC UA client certificate of a Unified Panel on the certificate authority device. You use the WinCC Unified Certificate Manager application for this.

The certificate authority device is always a Unified PC.

###### Procedure

If you do not have a certificate authority yet, follow these steps:

1. Create the certificate authority.

   In so doing, you create the root certificate of the certificate authority and its CRL file automatically.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
2. Add the Panel to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
3. Add the OPC UA server certificate or the OPC UA client certificate to the Panel, depending on the role of the Panel.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

If you already have a certificate authority, follow these steps:

1. If the Panel has not yet been added to the infrastructure of the certificate authority, add the Panel.

   See section [Adding devices](#adding-devices-rt-unified).
2. Add the OPC UA server certificate or the OPC UA client certificate to the Panel, depending on the role of the Panel.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

---

**See also**

[CA-based certificate workflow (OPC UA for Panel) (RT Unified)](#ca-based-certificate-workflow-opc-ua-for-panel-rt-unified)

##### Installing certificates (OPC UA for Panel) (RT Unified)

###### Introduction

The OPC UA application certificate of a Unified Panel is installed in the following steps:

- Export on the certificate authority device
- Import on the Panel

> **Note**
>
> You always export and import all certificates of the Panel as well as the root certificate of the issuing certificate authority and its CRL file.
>
> These certificates are automatically installed by the import.

###### Requirement

- The desired OPC UA application certificate has been added for the Panel on the certificate authority device.

###### Procedure

1. Export the certificates of the Panel on the certificate authority device. Use the WinCC Unified Certificate Manager for this.

   See section [Exporting certificates of a Panel](#exporting-certificates-of-a-panel-rt-unified).
2. Import the certificates to the Panel. Use the Control Panel for this.

   See section [Importing and installing certificates of a Unified Panel](#importing-and-installing-certificates-of-a-unified-panel-rt-unified).

---

**See also**

[CA-based certificate workflow (OPC UA for Panel) (RT Unified)](#ca-based-certificate-workflow-opc-ua-for-panel-rt-unified)
  
[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)

##### Establishing the trust relationship (OPC UA for Panel) (RT Unified)

###### Introduction

Secure OPC UA communication requires that the communication partners trust each other's OPC UA application certificates.

That is automatically the case when the OPC UA client trusts the root certificate of the certificate authority that issued the OPC UA server certificate, and vice versa.

###### Procedure

1. Check the Panel to determine whether it already trusts the root certificate of its OPC UA communication partner.

   See sections [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified) and [Automatic trust relationship in OPC UA communication](#automatic-trust-relationship-in-opc-ua-communication-rt-unified).

   If the Panel already trusts the root certificate, continue with step 3.
2. If the Panel does not trust the root certificate, install it manually.

   Follow these steps:

   - Export the root certificate of the OPC UA communication partner and its CRL file to a storage location the Panel can access.

     Follow the procedure described in the operating instructions of the communication partner.
   - Install the root certificate and the CRL file on the Panel.

     See section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified).
3. Check the communication partner to determine whether it already trusts the root certificate of the Panel.

   Follow the procedure described in the application help of the communication partner.

   If the communication partner already trusts the root certificate, you don't have to do anything.
4. If the communication partner does not trust the root certificate, install it manually.

   Follow these steps:

   - Export the root certificate on the certificate authority device with Certificate Manager to an external data storage medium.

     See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).
   - Connect the OPC UA communication partner to the external data storage medium.
   - Install the root certificate and its CRL file on the communication partner.

     Follow the procedure described in the user help of the communication partner. If necessary, manually copy both files to the folder for trusted certificates.

**Note**

**Alternative**

If a Unified PC belongs to the infrastructure of the certificate authority of the Panel whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.

See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

At the next connection attempt, the OPC UA server and OPC UA client trust each other.

---

**See also**

[CA-based certificate workflow (OPC UA for Panel) (RT Unified)](#ca-based-certificate-workflow-opc-ua-for-panel-rt-unified)
  
[Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)

##### Automatic trust relationship in OPC UA communication (RT Unified)

This section describes cases in which a device automatically trusts the CA-based certificate of its OPC UA communication partner. You do not have to establish the trust relationship manually on this device.

###### Same certificate authority

If both OPC UA communication partners are HMI devices and their OPC UA certificates have the same certificate authority, they automatically trust their OPC UA certificates.

###### Trusted certificate authority

If a device already trusts the certificate authority that issued the OPC UA certificate of the other device, it also automatically trusts the other device's OPC UA certificate.

**Example**

A Unified OPC UA server communicates with an OPC UA client. Server and client have different certificate authorities. The Unified OPC UA server trusts the root certificate of the OPC UA client, and vice versa. As a result, the devices also trust their OPC UA certificates.

A second OPC UA client authenticates itself to the Unified OPC UA server. Its OPC UA client certificate was issued by the same certificate authority that issued the OPC UA client certificate of the first client.

Since the Unified OPC UA server already trusts the root certificate, the server automatically also trusts the OPC UA client certificate of the second client.

###### Tag export of a Unified OPC UA server

In OPC UA communication, you have the option of exporting the tags of the project of a Unified OPC UA server running in Runtime. The device must be a Unified PC that has an OPC UA server certificate and OPC UA exporter certificate.

In CA-based communication, the root certificate of the certificate authority that issues these certificates is also automatically installed when you generate the certificates of the device with WinCC Unified Certificate Manager. The OPC UA server component and OPC UA exporter component of the device trust each other automatically.

---

**See also**

[Establishing the trust relationship (OPC UA for Panel) (RT Unified)](#establishing-the-trust-relationship-opc-ua-for-panel-rt-unified)

#### Using a default self-signed certificate (Panel as OPC UA server) (RT Unified)

##### Introduction

A Unified Panel that is used as an OPC UA server can use a self-signed OPC UA server certificate (default certificate).

If there is no CA-based OPC UA server certificate in the own certificates at Runtime start of the Panel, the self-signed OPC UA server certificate is automatically created and installed on the Panel.

> **Note**
>
> Self-signed certificates provide less protection than CA-based certificates. Use them for testing, for example. It is recommended that they then be replaced with CA-based certificates.

##### Limitations

- The self-signed OPC UA server certificate has a lifetime of 12 months.
- If no CA-based OPC UA server certificate has been installed on the Panel, each Runtime restart creates a new self-signed OPC UA server certificate. You must reestablish the trust relationship with the OPC UA server after each Runtime restart on the client.

##### Requirement

- The OPC UA server uses a security policy.
- The OPC UA client uses a self-signed OPC UA client certificate.
- Server and client do not yet trust their OPC UA certificates.
- Server and client are running.

##### Procedure

1. Check whether a CA-based OPC UA server certificate has been installed on the Panel as an own certificate.

   See section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified).
2. If so, uninstall the CA-based OPC UA server certificate and restart Runtime.

   See section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified).

   At the next connection attempt, the OPC UA client and OPC UA server exchange their certificates.
3. After the first connection attempt, the OPC UA client certificate is in the "untrusted" folder of the certificate store on the Panel.

   Trust the certificate on the Panel. See section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified).
4. After the first connection attempt, the OPC UA server certificate is in the rejected certificate store on the client device.

   Trust the certificate on the client. Follow the procedure described in the user help of the client. If necessary, manually copy the certificate to the folder for trusted certificates.

**Note**

Repeat this step after each Runtime start or Panel restart.

---

**See also**

[Importing and installing root certificates and CRL files on Panels (RT Unified)](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified)
  
[Establishing the trust relationship (OPC UA for Panel) (RT Unified)](#establishing-the-trust-relationship-opc-ua-for-panel-rt-unified)
  
[Introduction (RT Unified)](#introduction-rt-unified-2)

#### Engineering System as OPC UA client (RT Unified)

##### Introduction

If you are using a Unified PC or a Unified Panel as an OPC UA client, you configure which tags of the OPC UA server the client accesses and which alarm instances it receives in the Engineering System. For this reason, the Engineering System also acts as an OPC UA client during configuration of the device.

##### Provision and installation of the certificates

The client certificate of the Engineering System is created and transferred to the server automatically the first time a connection is established.

Trust the client certificate on the server. Follow the procedure described in the user help of the server. If necessary, manually copy the certificate to the folder for trusted certificates.

The Engineering System automatically receives the server certificate and trusts it without your having to take any action.

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-2)

### Audit certificates (Panel) (RT Unified)

This section contains information on the following topics:

- [Workflow (RT Unified)](#workflow-rt-unified)
- [Creating certificates (Audit for Panels) (RT Unified)](#creating-certificates-audit-for-panels-rt-unified)
- [Installing certificates (Audit for Panels) (RT Unified)](#installing-certificates-audit-for-panels-rt-unified)

#### Workflow (RT Unified)

##### Introduction

The WinCC Unified Audit option uses certificates to generate a checksum for Audit Trail data records. The checksum can be used to determine if the contents of a data record have been altered. The checksum also ensures that no lines have been removed from or added to the Audit Trail.

Audit certificates are not used for communication with another device.

The Audit certificate of a Unified Panel or Unified PC must be issued by a Unified certificate authority (CA-based certificate). You use the "WinCC Unified Certificate Manager" application for this.

> **Note**
>
> Certificate Manager always creates CA-based certificates. The use of CA-based certificates facilitates establishment of the trust relationship and provides the highest protection for your plant.
>
> The use of self-signed certificates is not supported for Audit.

##### Required certificates

For WinCC Unified Audit, you need the following certificates:

- Audit certificate of the HMI device
- Root certificate of the certificate authority that issued the Audit certificate, along with its CRL file.

##### Workflow

To provide the certificates needed by an HMI device for Audit, follow these steps:

1. Create the Audit certificate of the HMI device.
2. Install the Audit certificate on the HMI device.
3. Restart Runtime on the HMI device.

---

**See also**

[Creating certificates (Audit for Panels) (RT Unified)](#creating-certificates-audit-for-panels-rt-unified)
  
[Installing certificates (Audit for Panels) (RT Unified)](#installing-certificates-audit-for-panels-rt-unified)

#### Creating certificates (Audit for Panels) (RT Unified)

##### Introduction

You create the Audit certificate of a Unified Panel on the certificate authority device. You use the "WinCC Unified Certificate Manager" application for this.

The certificate authority device is always a Unified PC.

##### Procedure

If you do not have a certificate authority yet, follow these steps:

1. Create the certificate authority.

   In so doing, you create the root certificate of the certificate authority and its CRL file automatically.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
2. Add the Panel to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
3. Add the Collaboration certificate to the Panel.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

If you already have a certificate authority, follow these steps:

1. If the Panel has not yet been added to the infrastructure of the certificate authority, add the Panel.

   See section [Adding devices](#adding-devices-rt-unified).
2. Add the Audit certificate to the Panel.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

---

**See also**

[Workflow (RT Unified)](#workflow-rt-unified)

#### Installing certificates (Audit for Panels) (RT Unified)

##### Introduction

The Audit certificate of a Unified Panel is installed in the following steps:

- Export on the certificate authority device
- Import on the Panel

> **Note**
>
> You always export and import all certificates of the Panel as well as the root certificate of the issuing certificate authority and its CRL file.
>
> These certificates are automatically installed by the import.

##### Requirement

- The Audit certificate has been added for the Panel on the certificate authority device.

##### Procedure

1. Export the certificates of the Panel on the certificate authority device. Use the WinCC Unified Certificate Manager for this.

   See section [Exporting certificates of a Panel](#exporting-certificates-of-a-panel-rt-unified).
2. Import the certificates to the Panel. Use the Control Panel for this.

   See section [Importing and installing certificates of a Panel](#importing-and-installing-certificates-of-a-panel-rt-unified).

---

**See also**

[Workflow (RT Unified)](#workflow-rt-unified)

### Smart Server certificates for Panels (RT Unified)

If you are using a Unified Panel as a Smart Server, you can protect the communication between the Smart Server and Smart Client through the use of a self-signed Smart Server certificate.

With corresponding configuration of the Panel in the Engineering System, the certificate is automatically created and installed on the Panel when the Panel is loaded. When the connection between the server and client is established, the certificate is automatically transferred to the client. The client must trust the certificate.

You can find more information in the TIA Portal help system under "Using distributed systems &gt; WinCC Smart Server".

## Certificates for Unified PCs (RT Unified)

This section contains information on the following topics:

- [Collaboration certificates (PC) (RT Unified)](#collaboration-certificates-pc-rt-unified)
- [Web server certificates (PC) (RT Unified)](#web-server-certificates-pc-rt-unified)
- [OPC UA certificates (PC) (RT Unified)](#opc-ua-certificates-pc-rt-unified)
- [Audit certificates (PC) (RT Unified)](#audit-certificates-pc-rt-unified)

### Collaboration certificates (PC) (RT Unified)

This section contains information on the following topics:

- [Collaboration certificates and Runtime version (RT Unified)](#collaboration-certificates-and-runtime-version-rt-unified-1)
- [Workflow (Collaboration for PCs) (RT Unified)](#workflow-collaboration-for-pcs-rt-unified)
- [Creating certificates (Collaboration for PCs) (RT Unified)](#creating-certificates-collaboration-for-pcs-rt-unified)
- [Installing certificates (Collaboration for PCs) (RT Unified)](#installing-certificates-collaboration-for-pcs-rt-unified)
- [Establishing the trust relationship (Collaboration for PCs) (RT Unified)](#establishing-the-trust-relationship-collaboration-for-pcs-rt-unified)
- [Automatic trust relationship between Collaboration devices (RT Unified)](#automatic-trust-relationship-between-collaboration-devices-rt-unified-1)

#### Collaboration certificates and Runtime version (RT Unified)

Runtime Collaboration requires that the Collaboration certificates of 2 Collaboration partners be created with a certificate authority device whose installed Runtime version is equal to or higher than the installed Runtime version of the Collaboration partner with the higher Runtime version.

For this reason, the upgrading of Collaboration devices requires the creation, distribution and installation of new Collaboration certificates.

Example:

- A Unified PC and a Unified Panel with Runtime version V17 are Collaboration partners.
- You upgrade the Panel to V18.
- Create new Collaboration certificates for both HMI devices on a certificate authority device with installed Runtime version V18 or higher. Distribute them to and install them on the devices.

---

**See also**

[Workflow (Collaboration for PCs) (RT Unified)](#workflow-collaboration-for-pcs-rt-unified)

#### Workflow (Collaboration for PCs) (RT Unified)

##### Introduction

WinCC Unified Collaboration protects the communication between the Collaboration devices through the use of certificates.

The certificates must be issued by a Unified certificate authority (CA-based certificates). You use the WinCC Unified Certificate Manager application for this.

> **Note**
>
> Certificate Manager always creates CA-based certificates. The use of CA-based certificates facilitates establishment of the trust relationship and provides the highest protection for your plant.
>
> The use of self-signed certificates is not supported for Collaboration.

##### Required certificates

For successful communication between two Collaboration devices, you need the following certificates for each Collaboration device:

- Collaboration certificate of the device
- Root certificate of the certificate authority that issued the Collaboration certificate, along with its CRL file.

##### Workflow

To provide the certificates needed by a Unified PC Collaboration device, follow these steps:

1. Create the Collaboration certificate of the PC.
2. Install the Collaboration certificate on the PC.
3. Restart Runtime on the PC.
4. Establish the trust relationship between the PC and its Collaboration partner.

---

**See also**

[Creating certificates (Collaboration for PCs) (RT Unified)](#creating-certificates-collaboration-for-pcs-rt-unified)
  
[Installing certificates (Collaboration for PCs) (RT Unified)](#installing-certificates-collaboration-for-pcs-rt-unified)
  
[Establishing the trust relationship (Collaboration for PCs) (RT Unified)](#establishing-the-trust-relationship-collaboration-for-pcs-rt-unified)
  
[Collaboration certificates (Panel) (RT Unified)](#collaboration-certificates-panel-rt-unified)
  
[Collaboration certificates and Runtime version (RT Unified)](#collaboration-certificates-and-runtime-version-rt-unified-1)

#### Creating certificates (Collaboration for PCs) (RT Unified)

##### Introduction

You create the Collaboration certificate of a Unified PC on the certificate authority device. You use the WinCC Unified Certificate Manager application for this.

The certificate authority device is always a Unified PC.

##### Procedure

If you do not have a certificate authority yet, follow these steps:

1. Create the certificate authority.

   In so doing, you create the root certificate of the certificate authority and its CRL file automatically.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
2. Add the PC to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
3. Add the Collaboration certificate to the PC.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

If you already have a certificate authority, follow these steps:

1. If the PC has not yet been added to the infrastructure of the certificate authority, add the PC.

   See section [Adding devices](#adding-devices-rt-unified).
2. Add the Collaboration certificate to the PC.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

---

**See also**

[Workflow (Collaboration for PCs) (RT Unified)](#workflow-collaboration-for-pcs-rt-unified)
  
[Collaboration certificates and Runtime version (RT Unified)](#collaboration-certificates-and-runtime-version-rt-unified-1)

#### Installing certificates (Collaboration for PCs) (RT Unified)

##### Introduction

The Collaboration certificate of a Unified PC is installed in the following steps:

- Export on the certificate authority device
- Import to the PC
- Installation on the PC

> **Note**
>
> You always export and import all certificates of the PC as well as the root certificate of the issuing certificate authority and its CRL file.

##### Requirement

- The Collaboration certificate has been added for the PC on the certificate authority device.

##### Procedure

1. Export the certificates of the PC on the certificate authority device. Use the WinCC Unified Certificate Manager for this.

   See section [Exporting certificates of a Unified PC](#exporting-certificates-of-a-unified-pc-rt-unified).
2. Import the certificates to the PC. Use the Certificate Manager for this.

   See section [Importing certificates of a Unified PC](#importing-certificates-of-a-unified-pc-rt-unified).
3. Install all certificates together on the PC or only the Collaboration certificate. Use the Certificate Manager for this.

   See section [Installing all certificates or single certificates of a PC](#installing-all-certificates-or-single-certificates-of-a-pc-rt-unified).

---

**See also**

[Workflow (Collaboration for PCs) (RT Unified)](#workflow-collaboration-for-pcs-rt-unified)
  
[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)

#### Establishing the trust relationship (Collaboration for PCs) (RT Unified)

##### Introduction

Secure communication between Collaboration devices requires that the devices trust each other's Collaboration certificate.

That is automatically the case when a device trusts the root certificate of the certificate authority that issued the Collaboration certificate of the other device, and vice versa.

##### Trusting the Collaboration partner of a PC

To ensure that a Unified PC trusts its Collaboration partner, follow these steps:

1. Check whether the PC already trusts the root certificate of its Collaboration partner.

   See sections [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified) and [Automatic trust relationship between Collaboration devices](#automatic-trust-relationship-between-collaboration-devices-rt-unified-1).
2. If the PC does not yet trust the root certificate, install it manually.

   See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

---

**See also**

[Workflow (Collaboration for PCs) (RT Unified)](#workflow-collaboration-for-pcs-rt-unified)

#### Automatic trust relationship between Collaboration devices (RT Unified)

This section describes cases in which a Collaboration device automatically trusts the certificate of its Collaboration partner. You do not have to establish the trust relationship manually.

##### Same certificate authority

Requirement:

- The Collaboration certificates of both devices have the same certificate authority. That is, the certificates have the same root certificate.
- The own Collaboration certificate has been installed on each device

  During installation of this certificate, the root certificate is also automatically installed on the device. It is installed in the folder containing the trusted certificate authorities.

Result:

The first time the connection is established for Collaboration, the devices check the Collaboration certificate of their Collaboration partner. Since they already trust the root certificate, the Collaboration certificate is automatically installed in the folder with the trusted certificates.

##### Trusted certificate authority

Requirement:

- The Collaboration certificates of the Collaboration devices have different certificate authorities. That is, the certificates have different root certificates.
- One Collaboration device has a communication partner whose application certificate was issued by the same certificate authority as the Collaboration certificate of its Collaboration partner. The device already trusts the certificate authority of this communication partner.

Result:

- The first time the connection is established for Collaboration, the device checks the Collaboration certificate of the Collaboration partner.
- Since the device already trusts the root certificate of the other communication partner, it automatically installs the Collaboration certificate in the folder with the trusted certificates.

  > **Note**
  >
  > For successful Collaboration communication, the devices must trust each other. Check on the other Collaboration device to determine if it also already trusts the root certificate. See section [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified).
  >
  > Establish the trust relationship there manually, if necessary.

Example**:**

A Panel communicates with a second Panel using Unified Collaboration. The Collaboration application certificates of the Panels have different certificate authorities. Both Panels already trust the root certificates of their Collaboration partner.

For the first Panel, a Unified PC is configured as an additional Collaboration partner. The Collaboration application certificate of the PC has the same certificate authority and, thus, the same root certificate as the second Panel.

Since the first Panel already trusts the root certificate of the second Panel, it automatically also trusts the Collaboration application certificate of the PC.

---

**See also**

[Establishing the trust relationship (Collaboration for PCs) (RT Unified)](#establishing-the-trust-relationship-collaboration-for-pcs-rt-unified)

### Web server certificates (PC) (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-3)
- [Using a CA-based certificate (PC as web server) (RT Unified)](#using-a-ca-based-certificate-pc-as-web-server-rt-unified)
- [Using a self-signed certificate (PC as web server) (RT Unified)](#using-a-self-signed-certificate-pc-as-web-server-rt-unified)

#### Introduction (RT Unified)

##### Basics of web server communication

WinCC Unified protects the communication between a Runtime web server and its web clients through the use of a web server certificate. The clients must trust the web server certificate (one-way SSL authentication).

The web server certificate can be issued by a certificate authority (CA-based certificate) or be self-signed.

> **Note**
>
> For security reasons, it is recommended to use a CA-based certificate. You use the WinCC Unified Certificate Manager application to create the certificate.
>
> You create a self-signed web server certificate during installation of Runtime or later with the "WinCC Unified Configuration Manager" application.
>
> You can find help on choosing a certificate type in section [Selecting a suitable certificate type](#selecting-a-suitable-certificate-type-rt-unified).

The procedure for creating the web server certificate, installing it on the web server device and establishing the trust relationship with the web server on the clients depends on whether you are using CA-based or self-signed certificates.

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
  
[Workflow with a self-signed certificate (PC as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-pc-as-web-server-rt-unified)
  
[Unified certificate authority (RT Unified)](#unified-certificate-authority-rt-unified)

#### Using a CA-based certificate (PC as web server) (RT Unified)

This section contains information on the following topics:

- [Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
- [Creating certificates (PC as web server) (RT Unified)](#creating-certificates-pc-as-web-server-rt-unified)
- [Installing certificates (PC as web server) (RT Unified)](#installing-certificates-pc-as-web-server-rt-unified)
- [Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)
- [Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1)
- [Automatic trust relationship with a PC web server (RT Unified)](#automatic-trust-relationship-with-a-pc-web-server-rt-unified)
- [Installing the root certificate for Edge and Chrome (RT Unified)](#installing-the-root-certificate-for-edge-and-chrome-rt-unified-1)
- [Installing the root certificate for Firefox (RT Unified)](#installing-the-root-certificate-for-firefox-rt-unified-1)
- [Installing the root certificate on iOS devices (RT Unified)](#installing-the-root-certificate-on-ios-devices-rt-unified-1)
- [Installing the root certificate for a UCP web browser (RT Unified)](#installing-the-root-certificate-for-a-ucp-web-browser-rt-unified)

##### Workflow with a CA-based certificate (PC as web server) (RT Unified)

> **Note**
>
> Unified PCs always need a web server certificate.

If you are using a Unified PC as a Runtime web server and want to use a CA-based web server certificate, you need the following certificates:

- Web server certificate of the PC
- Root certificate of the certificate authority that issued the web server certificate, along with its CRL file.

###### Procedure

1. Create the web server certificate of the PC.

   See section [Creating certificates (PC as web server)](#creating-certificates-pc-as-web-server-rt-unified).
2. Install the certificate on the PC.

   See section [Installing certificates (PC as web server)](#installing-certificates-pc-as-web-server-rt-unified).

   This binds the web server certificate to the Runtime web page of the PC.
3. Establish the trust relationship with the web server on the web clients.

   See section [Establishing the trust relationship with the web server](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1).

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-3)

##### Creating certificates (PC as web server) (RT Unified)

###### Introduction

You create the CA-based web server certificate of a Unified PC on the certificate authority device. You use the WinCC Unified Certificate Manager application for this.

The certificate authority device is always a Unified PC.

###### Procedure

If you do not have a certificate authority yet, follow these steps:

1. Create the certificate authority.

   In so doing, you create the root certificate of the certificate authority and its CRL file automatically.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
2. Add the web server PC to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
3. Add the web server certificate to the PC.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

If you already have a certificate authority, follow these steps:

1. If the PC has not yet been added to the infrastructure of the certificate authority, add the web server PC.

   See section [Adding devices](#adding-devices-rt-unified).
2. Add the web server certificate to the PC.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)

##### Installing certificates (PC as web server) (RT Unified)

###### Introduction

The web server certificate of a Unified PC is installed in the following steps:

- Export on the certificate authority device
- Import to the PC
- Installation on the PC

> **Note**
>
> You always export and import all certificates of the PC as well as the root certificate of the issuing certificate authority and its CRL file.

###### Requirement

- The web server certificate has been added for the PC on the certificate authority device.

###### Procedure

1. Export the certificates of the PC on the certificate authority device. Use the WinCC Unified Certificate Manager for this.

   See section [Exporting certificates of a Unified PC](#exporting-certificates-of-a-unified-pc-rt-unified).
2. Import the certificates to the PC. Use the Certificate Manager for this.

   See section [Importing certificates of a Unified PC](#importing-certificates-of-a-unified-pc-rt-unified).
3. Install all certificates together on the PC or only the web server certificate. Use the Certificate Manager for this.

   See section [Installing all certificates or single certificates of a PC](#installing-all-certificates-or-single-certificates-of-a-pc-rt-unified).

> **Note**
>
> The installation binds the web server certificate to the Runtime web page. It replaces the web server certificate selected during Runtime installation or later in the "Website settings" step in the WinCC Unified Configuration tool.
>
> The web page is then restarted to enforce the use of the new certificate. Any connected web clients are thereby disconnected and must log in again.

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
  
[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)

##### Establishing the trust relationship with the web server (RT Unified)

###### Introduction

Secure communication between a Unified Runtime web server and its web clients requires that the clients trust the web server certificate.

That is automatically the case when a client trusts the root certificate of the certificate authority that issued the web server certificate.

###### Timing

You can establish the trust relationship on a planned or as needed basis:

- Planned: You install the root certificate before the client attempts to connect to the web server for the first time.

  The client then already trusts the web server certificate the first time a connection is established.
- As needed: You install the root certificate when the client first attempts to connect to the web server.

  If the root certificate of the web server has not yet been installed at that time, you can download it on the Unified home page and then install it in the client.

###### Installing the root certificate before a connection is established for the first time

| 1. If applicable, check whether the client already trusts the root certificate of the web server.     See sections [Checking the status of the web server root certificate on the web client.](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1) and [Automatic trust relationship with a PC web server](#automatic-trust-relationship-with-a-pc-web-server-rt-unified). 2. If the client already trusts the root certificate, you don't have to do anything.    If the client does not trust the root certificate, install it manually in the certificate store of the browser.        | Utilized browser | Certificate store used by the browser | For procedure, see section |    | --- | --- | --- |    | Edge and Chrome on Windows | Windows system certificate store | [Installing the root certificate before the first connection (Edge and Chrome)](#installing-the-root-certificate-before-the-first-connection-edge-and-chrome-rt-unified-1) |    | Firefox on Windows | Certificate store of Firefox | [Installing the root certificate before the first connection (for Firefox)](#installing-the-root-certificate-before-the-first-connection-for-firefox-rt-unified-1) |    | Web browser of a Unified Panel | Certificate store of the Panel | [Installing the root certificate before the first connection (Panel web browser)](#installing-the-root-certificate-before-the-first-connection-panel-web-browser-rt-unified-1) |    | Browser on iOS devices | System certificate store of the iOS device | [Installing the root certificate on iOS devices before the first connection](#installing-the-root-certificate-on-ios-devices-before-the-first-connection-rt-unified-1) | |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

###### Installing the root certificate at the first connection attempt

Follow the steps below according to the browser:

| Browser | Certificate store used by the browser | For procedure, see section |
| --- | --- | --- |
| Edge and Chrome on Windows | Windows system certificate store | [Installing the root certificate at the first connection (Edge and Chrome)](#installing-the-root-certificate-at-the-first-connection-edge-and-chrome-rt-unified-1) |
| Firefox on Windows | Certificate store of Firefox | [Installing the root certificate at the first connection (for Firefox)](#installing-the-root-certificate-at-the-first-connection-for-firefox-rt-unified-1) |
| Web browser of a Unified Panel | Certificate store of the Panel | [Installing the root certificate at the first connection (Panel web browser)](#installing-the-root-certificate-at-the-first-connection-panel-web-browser-rt-unified-1) |
| Browser on iOS devices | System certificate store of the iOS device | [Installing the root certificate on iOS devices at the first connection](#installing-the-root-certificate-on-ios-devices-at-the-first-connection-rt-unified-1) |

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)

##### Checking the status of the web server root certificate on the web client. (RT Unified)

###### Introduction

This section describes how to check whether a web client already trusts the root certificate of a Runtime web server.

In that case, the root certificate has been installed in the certificate store of the web client in the folder containing the trusted certificate authorities.

###### Procedure for Microsoft Edge and Chrome as web client

Microsoft Edge and Chrome use the Windows system certificate store.

Use Windows &gt; Search "Manage computer certificates" to check whether the root certificate has been installed under "Certificates - Local Computer" &gt; "Trusted Root Certification Authorities" &gt; "Certificates".

###### Procedure for Firefox

Firefox uses its own dedicated certificate store.

To check the status of a certificate, follow these steps:

1. Open the "Settings" page of Firefox.
2. Select "Privacy &amp; Security".
3. Click "View Certificates" in the "Certificates" area.
4. Select the "Authorities" tab in the "Certificate Manager" window.
5. Check whether the root certificate is included in the list of trusted authorities.

###### Procedure for iOS devices

Follow the procedure described in the user help of the manufacturer.

###### Procedure for "Web browser" of a Unified Panel

"Web browser" of the Unified Panel uses the certificate store of the Panel.

To check whether the Panel already trusts the root certificate, follow the procedure described in section [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified).

---

**See also**

[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)

##### Automatic trust relationship with a PC web server (RT Unified)

This section describes cases in which a web client automatically trusts the CA-based certificate of a Unified PC Runtime web server. You do not have to establish the trust relationship manually.

###### Edge or Chrome as local web client

Requirement:

- You use Microsoft Edge or Chrome as web client.
- Web server and client are installed on the same Unified PC.

Result:

- During installation of the certificates of the Unified PC, WinCC Unified Certificate Manager also installs the web server root certificate in the system certificate store of Windows. Microsoft Edge and Chrome use this certificate store.
- Since the clients already trust the root certificate, the web server certificate is automatically installed in the folder with the trusted certificates when a connection is established for the first time.
- The connection between the client and web server is secure from the outset.

###### Edge or Chrome as remote web client and same certificate authority

Requirement

- You use Microsoft Edge or Chrome as web client.
- The clients have been installed on a Unified PC.
- The web server certificate of the web server PC and at least one application certificate of the client PC were issued by the same certificate authority. That is, they have the same root certificate.

Result:

- During installation of the certificates of the Unified PC, Certificate Manager also installs the root certificate in the system certificate store of Windows. Microsoft Edge and Chrome use this certificate store.
- Since the clients already trust the root certificate, the web server certificate is automatically installed in the folder with the trusted certificates when a connection is established for the first time.
- The connection between the client and web server is secure from the outset.

###### Communicating with multiple web servers of the same certificate authority

Requirement:

- The web server certificates of two Unified Runtime web servers were issued by the same certificate authority. That is, they have the same root certificate.
- The web client already trusts the root certificate of one of the web servers.

  The manner in which the trust relationship was established is irrelevant.
- The client connects to the second web server.

Result:

- The client already trusts the root certificate at the first connection attempt. For this reason, the web server certificate of the second web server is automatically installed in the folder with the trusted certificates when the connection is established.
- The connection between the client and web server is secure from the outset.

---

**See also**

[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)

##### Installing the root certificate for Edge and Chrome (RT Unified)

This section contains information on the following topics:

- [Installing the root certificate before the first connection (Edge and Chrome) (RT Unified)](#installing-the-root-certificate-before-the-first-connection-edge-and-chrome-rt-unified-1)
- [Installing the root certificate at the first connection (Edge and Chrome) (RT Unified)](#installing-the-root-certificate-at-the-first-connection-edge-and-chrome-rt-unified-1)

###### Installing the root certificate before the first connection (Edge and Chrome) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on an Edge or Chrome web client before the client connects to the web server for the first time. The description applies to clients installed on Windows devices.

The procedure is explained using Edge as an example. The procedure is the same for Chrome.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager.

  See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
- The web server root certificate has been exported on the certificate authority device with Certificate Manager to a storage location the web client can access.

  See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).

  > **Note**
  >
  > **Alternative**
  >
  > If a Unified PC belongs to the infrastructure of the certificate authority of the web server whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.
  >
  > See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).
- Microsoft Edge or Chrome has been installed on the web client device.

###### Procedure

1. Double-click the root certificate file on the web client device.

   The root certificate is opened with the Windows standard form.

   ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)
2. Click "Install Certificate".
3. In the certificate import wizard, select "Local Machine" as the storage location and "Trusted Root Certification Authority" as the certificate store.
4. Start the import.
5. (optional) Check whether the root certificate was successfully installed in the Windows system certificate store.

   See section [Checking the status of the web server root certificate on the web client.](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1).

###### Result

At the first call of the web server web page, the browser trusts the root certificate of the web server and, thus, it automatically also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)

###### Installing the root certificate at the first connection (Edge and Chrome) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) at the first connection attempt of an Edge or Chrome web client. The description applies to clients installed on Windows devices.

The procedure is explained using Edge as an example. The procedure is the same for Chrome.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager. It has been installed on the web server.
- A Runtime project is running on the web server.
- Microsoft Edge or Chrome has been installed on the web client device.
- The web server root certificate has not yet been installed in the Windows system certificate store of the client device.
- The client device has access to the web server.

###### Procedure

1. Start Microsoft Edge on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed:

   ![Procedure](images/129763286923_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129763286923_DV_resource.Stream@PNG-de-DE.png)
3. Open the field with the error details and confirm that you want to open the web page.

   The WinCC Unified home page is loaded.
4. On the home page, select the "Certificate Authority" field and confirm "Open file" in the download dialog.

   ![Procedure](images/129766055435_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129766055435_DV_resource.Stream@PNG-de-DE.png)

   The root certificate is downloaded to the default download directory.
5. Double-click the downloaded file.

   The root certificate is opened with the Windows standard form.

   ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)
6. Click "Install Certificate".
7. In the certificate import wizard, select "Local Machine" as the storage location and "Trusted Root Certification Authority" as the certificate store.
8. Start the import.
9. (optional) Check whether the root certificate was successfully installed in the Windows system certificate store.

   See section [Checking the status of the web server root certificate on the web client.](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1).
10. Reload the page.

**Note**

**URL of a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the root certificate of the web server and, thus, it also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)

##### Installing the root certificate for Firefox (RT Unified)

This section contains information on the following topics:

- [Installing the root certificate before the first connection (for Firefox) (RT Unified)](#installing-the-root-certificate-before-the-first-connection-for-firefox-rt-unified-1)
- [Installing the root certificate at the first connection (for Firefox) (RT Unified)](#installing-the-root-certificate-at-the-first-connection-for-firefox-rt-unified-1)

###### Installing the root certificate before the first connection (for Firefox) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on a Firefox web client before the client connects to the web server for the first time. The description applies to clients installed on Windows devices.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager.

  See also section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
- The web server root certificate has been exported on the certificate authority device with Certificate Manager to a storage location the web client can access.

  See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).

  > **Note**
  >
  > **Alternative**
  >
  > If a Unified PC belongs to the infrastructure of the certificate authority of the web server whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.
  >
  > See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).
- Firefox has been installed on the web client device.

###### Procedure

1. Start Firefox on the web client device.
2. Install the root certificate in the certificate store of Firefox. To do this, follow these steps:

   - Open the "Settings" page of Firefox.
   - Select "Privacy &amp; Security".
   - Click "View Certificates" in the "Certificates" area.
   - Select the "Authorities" tab in the "Certificate Manager" window:

     ![Procedure](images/142189917195_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/142189917195_DV_resource.Stream@PNG-en-US.png)
   - Click "Import" and select the root certificate file.
   - In the window that opens, select the option "This certificate can identify websites" and confirm your selection.

###### Result

At the first call of the web server web page, the browser trusts the root certificate of the web server and, thus, it automatically also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1)
  
[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)

###### Installing the root certificate at the first connection (for Firefox) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on a Firefox web client when the client first attempts to connect to the web server. The description applies to clients installed on Windows devices.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager. It has been installed on the web server.
- A Runtime project is running on the web server.
- Firefox has been installed on the web client device.
- The web server root certificate has not yet been installed in the certificate store of the browser.
- The client device has access to the web server.

###### Procedure

1. Start Firefox on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed.
3. Open the "Advanced" field and confirm the "Accept the Risk and Continue" field.
4. An exception is entered for this page in the Firefox Certificate Manager.
5. On the WinCC Unified home page, select the "Certificate Authority" field.
6. Save the root certificate. To do this, click "Save file" in the Firefox dialog that follows.
7. Install the root certificate in the certificate store of Firefox. To do this, follow these steps:

   - Open the "Settings" page of Firefox.
   - Select "Privacy &amp; Security".
   - Click "View Certificates" in the "Certificates" area.
   - Select the "Authorities" tab in the "Certificate Manager" window:

     ![Procedure](images/142189917195_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/142189917195_DV_resource.Stream@PNG-en-US.png)
   - Click "Import" and select the root certificate file.
   - In the window that opens, select the option "This certificate can identify websites" and confirm your selection.
   - Click "Servers" and remove the exception that was created by step 2.
8. Reload the page.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the root certificate of the web server and, thus, it also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1)
  
[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

##### Installing the root certificate on iOS devices (RT Unified)

This section contains information on the following topics:

- [Installing the root certificate on iOS devices before the first connection (RT Unified)](#installing-the-root-certificate-on-ios-devices-before-the-first-connection-rt-unified-1)
- [Installing the root certificate on iOS devices at the first connection (RT Unified)](#installing-the-root-certificate-on-ios-devices-at-the-first-connection-rt-unified-1)

###### Installing the root certificate on iOS devices before the first connection (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on an iOS web client before the client connects to the web server for the first time.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager.
- The web server root certificate has been exported on the certificate authority device with Certificate Manager to a storage location.

  See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).

  > **Note**
  >
  > **Alternative**
  >
  > If a Unified PC belongs to the infrastructure of the certificate authority of the web server whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.
  >
  > See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).
- The web client device has access to the root certificate file, for example, because the file was sent to the device via email.
- The desired browser has been installed on the web client device.

###### Procedure

1. Tap the root certificate file on the iOS device.

   You are informed that the website is trying to load a configuration profile.
2. Tap "Allow"

   The configuration profile is loaded.
3. Tap "Close".
4. Select "Settings &gt; General &gt; Profile" on the device.
5. Tap the configuration profile you just loaded.
6. Tap "Install" at the top right.

   ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)
7. Tap "Install" again at the top right.

   ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)
8. Tap "Install" again in the "Profile" confirmation prompt:

   ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

   The certificate is installed.
9. Select "Settings &gt; General &gt; About &gt; Certificate Trust Settings" on the device:

   ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)
10. Select the "Enable full trust for root certificates" option for the web server root certificate.

###### Result

At the first call of the web server web page, the browser trusts the root certificate of the web server and, thus, it automatically also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

###### Installing the root certificate on iOS devices at the first connection (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) on an iOS web client when the client first attempts to connect to the web server.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager. It has been installed on the web server.
- A Runtime project is running on the web server.
- The desired browser has been installed on the web client device.
- The web server root certificate has not yet been installed in the certificate store of the browser.
- The client device has access to the web server.

###### Procedure

1. Start the browser on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   A warning message is displayed.
3. Open the details for the message and select the button for loading the page.

   The WinCC Unified home page is loaded.
4. Load the root certificate to your device. Follow these steps:

   - On the home page, select the "Certificate Authority" field.

     ![Procedure](images/129766055435_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129766055435_DV_resource.Stream@PNG-de-DE.png)

     A pop-up opens. It informs you that the website is trying to load a configuration profile.
   - Tap "Allow"

     The configuration profile is loaded.
   - Tap "Close".
5. Install the configuration profile on your device. Follow these steps:

   - Select "Settings &gt; General &gt; Profile" on the device.
   - Tap the configuration profile you just loaded.
   - Tap "Install" at the top right.

     ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)
   - Tap "Install" again at the top right.

     ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)
   - Tap "Install" again in the "Profile" confirmation prompt:

     ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

     The root certificate is installed.

     You see the entry "Verified".

     ![Procedure](images/129772977419_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772977419_DV_resource.Stream@PNG-de-DE.png)
   - Select "General &gt; About &gt; Certificate Trust Settings".

     ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)
   - Select "WinCC Unified CA" and select "Next".

     ![Procedure](images/129773533707_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129773533707_DV_resource.Stream@PNG-de-DE.png)
6. Load the Unified home page again.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the root certificate of the web server and, thus, it also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)
  
[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

##### Installing the root certificate for a UCP web browser (RT Unified)

This section contains information on the following topics:

- [Installing the root certificate before the first connection (Panel web browser) (RT Unified)](#installing-the-root-certificate-before-the-first-connection-panel-web-browser-rt-unified-1)
- [Installing the root certificate at the first connection (Panel web browser) (RT Unified)](#installing-the-root-certificate-at-the-first-connection-panel-web-browser-rt-unified-1)

###### Installing the root certificate before the first connection (Panel web browser) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server in the web browser of a Unified Panel before the browser connects to the web server for the first time.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager.
- The web server root certificate has been exported on the certificate authority device with Certificate Manager to a storage location the web client can access.

  See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).

  > **Note**
  >
  > **Alternative**
  >
  > If a Unified PC belongs to the infrastructure of the certificate authority of the web server whose certificates were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.
  >
  > See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

###### Procedure

Web browser uses the certificate store of the Panel. To install the root certificate there, follow the procedure described in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified).

###### Result

At the first call of the web server web page, the browser trusts the root certificate of the web server and, thus, it automatically also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
  
[Checking the status of a root certificate on the HMI device (RT Unified)](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

###### Installing the root certificate at the first connection (Panel web browser) (RT Unified)

###### Introduction

This section describes how to install the root certificate of a Runtime web server (Unified PC or Unified Panel) in the web browser of a Unified Panel when the web browser first attempts to connect to the web server.

###### Requirement

- The web server certificate has been created with WinCC Unified Certificate Manager. It has been installed on the web server.
- A Runtime project is running on the web server.
- The web server root certificate has not yet been installed in the certificate store of the Panel.
- The Panel has access to the web server.

###### Procedure

1. Start the "Web browser" application on the Panel.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed.
3. Open the field with the error details and confirm that you want to open the web page.

   The WinCC Unified home page is loaded.
4. On the home page, select the "Certificate Authority" field and confirm "Open file" in the download dialog.

   The root certificate is downloaded.
5. Web browser uses the certificate store of the Panel. Install the root certificate there. Follow the procedure described in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified).

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

Web browser trusts the root certificate of the web server and, thus, it also trusts the web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a CA-based certificate (PC as web server) (RT Unified)](#workflow-with-a-ca-based-certificate-pc-as-web-server-rt-unified)
  
[Checking the status of a root certificate on the HMI device (RT Unified)](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified)
  
[Establishing the trust relationship with the web server (RT Unified)](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

#### Using a self-signed certificate (PC as web server) (RT Unified)

This section contains information on the following topics:

- [Workflow with a self-signed certificate (PC as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-pc-as-web-server-rt-unified)
- [Configuring a self-signed certificate (RT Unified)](#configuring-a-self-signed-certificate-rt-unified)
- [Trusting the PC web server on the web client (RT Unified)](#trusting-the-pc-web-server-on-the-web-client-rt-unified)

##### Workflow with a self-signed certificate (PC as web server) (RT Unified)

A Unified PC that is used as a Runtime web server can use a self-signed web server certificate.

> **Note**
>
> Self-signed certificates provide less protection than CA-based certificates. Use them for testing, for example. It is recommended that they then be replaced with CA-based certificates.

> **Note**
>
> Unified PCs always need a web server certificate.

###### Limitations

- The self-signed web server certificate has a lifetime of 12 months.

###### Procedure

1. Create a new self-signed web server certificate and bind it to the Runtime web page. Or, select an existing self-signed certificate and bind it to the web page.

   See section [Configuring a self-signed certificate](#configuring-a-self-signed-certificate-rt-unified).
2. If a Runtime project is not yet running on the PC, start the desired project.
3. Establish the trust relationship with the web server on the web clients.

   See section [Trusting the PC web server on the web client](#trusting-the-pc-web-server-on-the-web-client-rt-unified).

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-3)

##### Configuring a self-signed certificate (RT Unified)

| Symbol | Meaning |
| --- | --- |
| ![Figure](images/145494195723_DV_resource.Stream@PNG-de-DE.png) | **Tips for effective procedure** |
| Typically, you create a self-signed web server certificate during Runtime installation. You use this certificate to test the configuration.   Afterwards, you replace it with a CA-based web server certificate. |  |

###### Introduction

You create and install the self-signed web server certificate of the Unified PC during installation of Unified Runtime or at a later time.

###### During installation

1. In the "Website settings" step of the installation, select the "Create a new certificate" option.
2. (optional) Runtime uses the device name/FQDN of the PC by default for addressing the Runtime web page and the identity provider. To use the IP address instead, select the "Use IP address instead of computer name" option under "Addressing the website and the identity provider".
3. Configure the other steps if required.
4. Restart the system.

###### After installation

1. Start the "WinCC Unified Configuration Manager" application on the PC.
2. ​Navigate to the "Website settings" step.
3. (optional) Runtime uses the device name/FQDN of the PC by default for addressing the Runtime web page and the identity provider. To use the IP address instead, select the "Use IP address instead of computer name" option under "Addressing the website and the identity provider".
4. To create a new self-signed certificate, follow these steps:

   - Select the "Create a new certificate" option.
   - Enter a certificate name.
5. To use a previously created self-signed certificate, follow these steps:

   - Select the "Select an existing certificate" option.
   - Select the desired self-signed certificate from the list.

**Note**

**Displayed certificates**

You see all certificates whose device binding is consistent with the setting you selected for addressing the Runtime web page and identity provider.

###### Result

- "Create a new certificate" option selected:

  A new self-signed certificate is created, installed and bound to the web page.
- "Select an existing certificate" option selected:

  The selected self-signed certificate is installed and bound to the web page.

The Runtime web page and the identity provider are addressed according to your selection.

---

**See also**

[Workflow with a self-signed certificate (PC as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-pc-as-web-server-rt-unified)

##### Trusting the PC web server on the web client (RT Unified)

This section contains information on the following topics:

- [Installing the self-signed web server certificate for Edge and Chrome (RT Unified)](#installing-the-self-signed-web-server-certificate-for-edge-and-chrome-rt-unified-1)
- [Installing the self-signed web server certificate for Firefox (RT Unified)](#installing-the-self-signed-web-server-certificate-for-firefox-rt-unified-1)
- [Installing the self-signed web server certificate for an iOS device (RT Unified)](#installing-the-self-signed-web-server-certificate-for-an-ios-device-rt-unified-1)
- [Installing the self-signed web server certificate for the web browser of a Panel (RT Unified)](#installing-the-self-signed-web-server-certificate-for-the-web-browser-of-a-panel-rt-unified-1)

###### Installing the self-signed web server certificate for Edge and Chrome (RT Unified)

###### Introduction

This section describes how to install the self-signed web server certificate of a Runtime web server (Unified PC or Unified Panel) on an Edge or Chrome web client on Windows.

The procedure is explained using Edge as an example. The procedure is the same for Chrome.

###### Requirement

- The Runtime web server uses a self-signed web server certificate.
- A Runtime project is running on the web server.
- Microsoft Edge or Chrome has been installed on the web client device.
- The client device has access to the web server.

###### Procedure

1. Start Microsoft Edge on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   Edge warns you that the connection is not secure.
3. Download the certificate. To do this, follow these steps:

   - Click the triangle with the exclamation point in the address bar:

     ![Procedure](images/169984863115_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/169984863115_DV_resource.Stream@PNG-de-DE.png)
   - Click the notice that the connection to the website is not secure:

     ![Procedure](images/169989134091_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/169989134091_DV_resource.Stream@PNG-de-DE.png)
   - Click the "Show certificate" icon:

     ![Procedure](images/169989629323_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/169989629323_DV_resource.Stream@PNG-de-DE.png)
   - Click "Export" in the "Details" tab.
   - Select a storage location and save the certificate.
4. Install the certificate in the certificate store of Windows. To do this, follow these steps:

   - Double-click the downloaded certificate file.

     The certificate is opened with the Windows standard form.

     ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129696632715_DV_resource.Stream@PNG-de-DE.png)
   - Click "Install Certificate".
   - In the certificate import wizard, select "Local Machine" as the storage location and "Trusted Root Certification Authority" as the certificate store.
   - Start the import.
5. Reload the page.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the self-signed web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Configuring a self-signed certificate (RT Unified)](#configuring-a-self-signed-certificate-rt-unified)
  
[Workflow with a self-signed certificate (PC as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-pc-as-web-server-rt-unified)
  
[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1)

###### Installing the self-signed web server certificate for Firefox (RT Unified)

###### Introduction

This section describes how to install the self-signed web server certificate of a Runtime web server (Unified PC or Unified Panel) on a Firefox web client on Windows.

###### Requirement

- The Runtime web server uses a self-signed web server certificate.
- A Runtime project is running on the web server.
- Firefox has been installed on the web client device.
- The client device has access to the web server.

###### Procedure

1. Start Firefox on the web client device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed.
3. Download the certificate. To do this, follow these steps:

   - Open the "Advanced" field.
   - Click "More Information".

     A dialog with the page information opens.
   - Click "Security &gt; View Certificate".

     A tab with the certificate information opens.
   - Click "PEM (certificate)" under "Miscellaneous &gt; Save".
   - Select a storage location and save the certificate.
4. Install the certificate in the certificate store of Firefox. To do this, follow these steps:

   - Open the "Settings" page of Firefox.
   - Select "Privacy &amp; Security".
   - Click "View Certificates" in the "Certificates" area.
   - Click "Import" and select the certificate file.
5. Reload the page.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the self-signed web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a self-signed certificate (PC as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-pc-as-web-server-rt-unified)
  
[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1)

###### Installing the self-signed web server certificate for an iOS device (RT Unified)

###### Introduction

This section describes how to install the self-signed web server certificate of a Runtime web server (Unified PC or Unified Panel) on the web client of an iOS device.

The procedure is explained using Safari as an example. The procedure is the same for other browsers.

###### Requirement

- A self-signed web server certificate has been installed on the web server HMI device.
- A Runtime project is running on the web server.
- The client device is an iOS device.
- The device has access to the web server.
- Safari has been installed on the device.

###### Procedure

1. Start Safari on the HMI device.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   An error message is displayed.
3. Load the self-signed web server certificate to your device. Follow these steps:

   - CHECK: How? / Click where?   
     Is the self-signed certificate also considered a configuration profile?

     A pop-up opens. It informs you that the website is trying to load a configuration profile.
   - Tap "Allow".

     The configuration profile is loaded.
   - Tap "Close".
4. Install the configuration profile on your device. Follow these steps:

   - Select "Settings &gt; General &gt; Profile" on the device.
   - Tap the configuration profile you just loaded.
   - Tap "Install" at the top right.

     ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129766715275_DV_resource.Stream@PNG-de-DE.png)
   - Tap "Install" again at the top right.

     ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772560651_DV_resource.Stream@PNG-de-DE.png)
   - Tap "Install" again in the "Profile" confirmation prompt:

     ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

     The certificate is installed.
   - Select "Settings &gt; General &gt; About &gt; Certificate Trust Settings" on the device:

     ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)

     ![Procedure](images/129773293963_DV_resource.Stream@PNG-de-DE.png)
   - Select the "Full trust for root certificates" option for the certificate.
5. (optional) Check whether the web server certificate was successfully installed.

   Follow the same procedure as you use to check whether a web server root certificate has been installed on the web client.
6. Load the Unified home page again.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The browser trusts the self-signed web server certificate.

You can log in to Runtime with a secure connection.

###### Alternative procedure

1. Export the self-signed web server certificate on the device of another web client that communicates with the same web server, e.g. with Edge.
2. Transfer the certificate to the iOS device, for example, by sending it as an email attachment and downloading the attachment to the iOS device.

   A pop-up opens. It informs you that the website is trying to load a configuration profile.
3. Tap "Allow".

   The configuration profile is loaded.
4. Tap "Close".
5. Continue as described above, starting from step 4.

---

**See also**

[Workflow with a self-signed certificate (PC as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-pc-as-web-server-rt-unified)
  
[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1)

###### Installing the self-signed web server certificate for the web browser of a Panel (RT Unified)

###### Introduction

This section describes how to install the self-signed web server certificate of a Runtime web server (Unified PC or Unified Panel) in the web browser of a Unified Panel.

###### Requirement

- A self-signed web server certificate has been installed on the web server HMI device.
- A Runtime project is running on the web server.
- The client device has access to the web server.

###### Procedure

1. Start the "Web browser" application on the Panel.
2. Enter the URL of the Unified web server in the address bar:`https://``<IP address of the HMI device or its FQDN/device name>`

   The browser warns you that the connection is not secure.
3. Display the details for the connection.
4. Display the certificate.
5. Download the certificate.

   The certificate is loaded into the certificate store of the Panel. The Panel does not yet trust the certificate.
6. Trust the certificate with "Control Panel &gt; Security &gt; Certificates".
7. Reload the page in the web browser.

**Note**

**Access to a Unified PC web server**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name as the URL depends on how the web server certificate was bound to the web server PC. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

​If needed, ask your administrator.

###### Result

The web browser trusts the self-signed web server certificate.

You can log in to Runtime with a secure connection.

---

**See also**

[Workflow with a self-signed certificate (PC as web server) (RT Unified)](#workflow-with-a-self-signed-certificate-pc-as-web-server-rt-unified)
  
[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1)
  
[Importing and installing root certificates and CRL files on Panels (RT Unified)](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified)
  
[Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)

### OPC UA certificates (PC) (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-4)
- [Using CA-based certificates (OPC UA for PC) (RT Unified)](#using-ca-based-certificates-opc-ua-for-pc-rt-unified)
- [Using a default self-signed certificate (PC as OPC UA server and exporter) (RT Unified)](#using-a-default-self-signed-certificate-pc-as-opc-ua-server-and-exporter-rt-unified)
- [Engineering System as OPC UA client (RT Unified)](#engineering-system-as-opc-ua-client-rt-unified-1)

#### Introduction (RT Unified)

If the OPC UA server uses a security policy, the OPC UA communication is protected through the use of certificates. The OPC UA server must trust the OPC UA certificates of its clients, and vice versa (mutual SSL authentication).

##### PC as OPC UA server

If you are using a Unified PC as an OPC UA server, its OPC UA server certificate and OPC UA exporter certificate can be issued by a certificate authority (CA-based certificate) or be self-signed.

> **Note**
>
> For security reasons, it is recommended to use a CA-based certificate. You use WinCC Unified Certificate Manager to create the certificate.

##### PC as OPC UA client

A Unified PC that is used as an OPC UA client must use a certificate issued by a Unified certificate authority (CA-based certificate). You use WinCC Unified Certificate Manager to create the certificate.

> **Note**
>
> If you are using a PC as an OPC UA client, the Engineering System also acts as an OPC UA client during configuration of the device. Its certificate is created, installed and transferred automatically. For details on this and on establishing the trust relationship, see section [Engineering System as OPC UA client](#engineering-system-as-opc-ua-client-rt-unified-1).

##### Contents of this help

This help describes the following:

- Creating a CA-based OPC UA server certificate or OPC UA client certificate of the PC
- Installing the CA-based certificate on the PC
- Using the default self-signed certificate for PCs as OPC UA server
- Establishing the trust relationship with the OPC UA communication partner on the PC
- Distributing the OPC UA certificate of the PC to the OPC UA communication partner

  This step sets up the establishment of the trust relationship with the PC on the OPC UA communication partner.

> **Note**
>
> **Procedure at the OPC UA communication partners**
>
> For information on how to create and install the OPC UA certificate of the communication partner and distribute it to the PC and how to trust the certificate of the PC on the communication partner, refer to the operating instructions of the respective communication partner.

---

**See also**

[CA-based workflow (OPC UA for PC) (RT Unified)](#ca-based-workflow-opc-ua-for-pc-rt-unified)
  
[Using a default self-signed certificate (PC as OPC UA server and exporter) (RT Unified)](#using-a-default-self-signed-certificate-pc-as-opc-ua-server-and-exporter-rt-unified)

#### Using CA-based certificates (OPC UA for PC) (RT Unified)

This section contains information on the following topics:

- [CA-based workflow (OPC UA for PC) (RT Unified)](#ca-based-workflow-opc-ua-for-pc-rt-unified)
- [Creating certificates (OPC UA for PC) (RT Unified)](#creating-certificates-opc-ua-for-pc-rt-unified)
- [Installing certificates (OPC UA for PC) (RT Unified)](#installing-certificates-opc-ua-for-pc-rt-unified)
- [Establishing the trust relationship (OPC UA for PC) (RT Unified)](#establishing-the-trust-relationship-opc-ua-for-pc-rt-unified)
- [Automatic trust relationship in OPC UA communication (RT Unified)](#automatic-trust-relationship-in-opc-ua-communication-rt-unified-1)

##### CA-based workflow (OPC UA for PC) (RT Unified)

For CA-based OPC UA communication, a Unified PC needs the following certificates:

- OPC UA application certificate suitable for the role of the PC during OPC UA communication:

  - OPC UA server certificate and, if applicable, OPC UA exporter certificate,  
    or
  - OPC UA client certificate
- Root certificate of the certificate authority that issued the OPC UA application certificate, along with its CRL file.

###### Requirement

- The OPC UA server uses a security policy.
- The OPC UA communication partner of the PC has an OPC UA application certificate that was issued by a certificate authority.
- The certificate has been installed on the communication partner as an own certificate.

###### Workflow

1. Create an OPC UA server certificate and OPC UA exporter certificate or an OPC UA client certificate for the PC, depending on the role of the PC.

   See section [Creating certificates (OPC UA for PC)](#creating-certificates-opc-ua-for-pc-rt-unified).
2. Install the certificate(s) on the PC.

   See section [Installing certificates (OPC UA for PC)](#installing-certificates-opc-ua-for-pc-rt-unified).
3. Restart Runtime on the PC.
4. Establish the trust relationship between the PC and its OPC UA communication partner.

   See section [Establishing the trust relationship (OPC UA for PC)](#establishing-the-trust-relationship-opc-ua-for-pc-rt-unified).

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-4)

##### Creating certificates (OPC UA for PC) (RT Unified)

###### Introduction

You create the OPC UA server certificate and OPC UA exporter certificate or the OPC UA client certificate of a Unified PC on the certificate authority device. You use the WinCC Unified Certificate Manager application for this.

The certificate authority device is always a Unified PC.

###### Procedure

If you do not have a certificate authority yet, follow these steps:

1. Create the certificate authority.

   In so doing, you create the root certificate of the certificate authority and its CRL file automatically.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
2. Add the PC to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
3. Add the OPC UA server certificate and, if applicable, OPC UA exporter certificate or the OPC UA client certificate to the PC, depending on the role of the PC.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

If you already have a certificate authority, follow these steps:

1. If the PC has not yet been added to the infrastructure of the certificate authority, add the PC.

   See section [Adding devices](#adding-devices-rt-unified).
2. Add the OPC UA server certificate and, if applicable, OPC UA exporter certificate or the OPC UA client certificate to the PC, depending on the role of the PC.  
   See section [Add application certificates](#add-application-certificates-rt-unified).

---

**See also**

[CA-based workflow (OPC UA for PC) (RT Unified)](#ca-based-workflow-opc-ua-for-pc-rt-unified)

##### Installing certificates (OPC UA for PC) (RT Unified)

###### Introduction

The OPC UA application certificate of a Unified PC is installed in the following steps:

- Export on the certificate authority device
- Import on the PC
- Installation on the PC

> **Note**
>
> You always export and import all certificates of the PC as well as the root certificate of the issuing certificate authority and its CRL file.

###### Requirement

- The desired OPC UA application certificate has been added for the PC on the certificate authority device.

###### Procedure

1. Export the certificates of the PC on the certificate authority device. Use the WinCC Unified Certificate Manager for this.

   See section [Exporting certificates of a Unified PC](#exporting-certificates-of-a-unified-pc-rt-unified).
2. Import the certificates to the PC. Use the Certificate Manager for this.

   See section [Importing certificates of a Unified PC](#importing-certificates-of-a-unified-pc-rt-unified).
3. Install all certificates together on the PC or only the OPC UA certificate. Use the Certificate Manager for this.

   See section [Installing all certificates or single certificates of a PC](#installing-all-certificates-or-single-certificates-of-a-pc-rt-unified).

---

**See also**

[CA-based workflow (OPC UA for PC) (RT Unified)](#ca-based-workflow-opc-ua-for-pc-rt-unified)

##### Establishing the trust relationship (OPC UA for PC) (RT Unified)

###### Introduction

Secure OPC UA communication requires that the communication partners trust each other's OPC UA application certificates.

That is automatically the case when the OPC UA client trusts the root certificate of the certificate authority that issued the OPC UA server certificate, and vice versa.

###### Procedure

1. Check the PC to determine whether it already trusts the root certificate of its OPC UA communication partner.

   See sections [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified) and [Automatic trust relationship in OPC UA communication](#automatic-trust-relationship-in-opc-ua-communication-rt-unified-1).

   If the PC already trusts the root certificate, continue with step 3.
2. If the PC does not trust the root certificate, install it manually.

   Follow these steps:

   - Export the root certificate of the OPC UA communication partner and its CRL file to a storage location the PC can access.

     Follow the procedure described in the operating instructions of the communication partner.
   - Install the root certificate and the CRL file on the PC.

     See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).
3. Check the communication partner to determine whether it already trusts the root certificate of the PC.

   Follow the procedure described in the application help of the communication partner.

   If the communication partner already trusts the root certificate, you don't have to do anything.
4. If the communication partner does not trust the root certificate, install it manually.

   Follow these steps:

   - Export the root certificate on the certificate authority device with Certificate Manager to an external data storage medium.

     See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).
   - Connect the OPC UA communication partner to the external data storage medium.
   - Install the root certificate and its CRL file on the communication partner.

     Follow the procedure described in the user help of the communication partner. If necessary, manually copy both files to the folder for trusted certificates.

**Note**

**Alternative**

If the certificates of the PC were already installed with Certificate Manager, you can export the root certificate on the PC with SIMATIC Runtime Manager.

See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

At the next connection attempt, the OPC UA server and OPC UA client trust each other.

---

**See also**

[CA-based workflow (OPC UA for PC) (RT Unified)](#ca-based-workflow-opc-ua-for-pc-rt-unified)

##### Automatic trust relationship in OPC UA communication (RT Unified)

This section describes cases in which a device automatically trusts the CA-based certificate of its OPC UA communication partner. You do not have to establish the trust relationship manually on this device.

###### Same certificate authority

If both OPC UA communication partners are HMI devices and their OPC UA certificates have the same certificate authority, they automatically trust their OPC UA certificates.

###### Trusted certificate authority

If a device already trusts the certificate authority that issued the OPC UA certificate of the other device, it also automatically trusts the other device's OPC UA certificate.

**Example**

A Unified OPC UA server communicates with an OPC UA client. Server and client have different certificate authorities. The Unified OPC UA server trusts the root certificate of the OPC UA client, and vice versa. As a result, the devices also trust their OPC UA certificates.

A second OPC UA client authenticates itself to the Unified OPC UA server. Its OPC UA client certificate was issued by the same certificate authority that issued the OPC UA client certificate of the first client.

Since the Unified OPC UA server already trusts the root certificate, the server automatically also trusts the OPC UA client certificate of the second client.

###### Tag export of a Unified OPC UA server

In OPC UA communication, you have the option of exporting the tags of the project of a Unified OPC UA server running in Runtime. The device must be a Unified PC that has an OPC UA server certificate and OPC UA exporter certificate.

In CA-based communication, the root certificate of the certificate authority that issues these certificates is also automatically installed when you generate the certificates of the device with WinCC Unified Certificate Manager. The OPC UA server component and OPC UA exporter component of the device trust each other automatically.

---

**See also**

[Establishing the trust relationship (OPC UA for PC) (RT Unified)](#establishing-the-trust-relationship-opc-ua-for-pc-rt-unified)

#### Using a default self-signed certificate (PC as OPC UA server and exporter) (RT Unified)

##### Introduction

A Unified PC that is used as an OPC UA server can use a self-signed OPC UA server certificate. It can use a self-signed OPC UA exporter certificate for tag export. (default certificates)

The certificates are created and installed on the PC automatically.

> **Note**
>
> These self-signed certificates are only used if no corresponding CA-based OPC UA certificate has been installed in the own certificates at Runtime start on the PC.

> **Note**
>
> Self-signed certificates provide less protection than CA-based certificates. Use them for testing, for example. It is recommended that they then be replaced with CA-based certificates.

##### Establishing the trust relationship

You can establish the trust relationship between the OPC UA server and OPC UA client before or after the first connection attempt.

The OPC UA server certificate and OPC UA exporter certificate trust each other automatically.

##### Requirement

- The OPC UA server uses a security policy.
- The OPC UA client uses a self-signed OPC UA client certificate.
- Server and client do not yet trust their OPC UA certificates.
- Server and client are running.

##### Procedure

1. Check whether a CA-based OPC UA server certificate and an OPC UA exporter certificate have been installed on the PC as an own certificate.

   See section [Managing own certificates of a Unified PC](#managing-own-certificates-of-a-unified-pc-rt-unified).
2. If so, uninstall these CA-based OPC UA certificates and restart Runtime on the PC.

   At the next connection attempt between the server and client, the PC sends the self-signed OPC UA server certificate. The PC uses the self-signed OPC UA exporter certificate for that tag export.
3. Trust the OPC UA client certificate on the PC.

   Follow the procedure described below.
4. Trust the OPC UA server certificate of the PC on the OPC UA client.

   Follow the procedure described below.

##### Trusting the OPC UA client certificate on the PC

To trust the client certificate before the first connection attempt, follow these steps:

1. Export the self-signed OPC UA client certificate on the client device to a storage location the PC can access. Follow the procedure described in the user help of the client.
2. Trust the certificate on the PC. See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

To trust the client certificate after the first connection attempt, follow these steps:

1. After the first connection attempt, the OPC UA client certificate is in the "untrusted" folder of the certificate store on the PC.

   Trust the certificate on the PC. See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

##### Trusting the OPC UA server certificate on the OPC UA client

To trust the server certificate before the first connection attempt, follow these steps:

1. Copy the OPC UA server certificate from the certificate store of the PC to a storage location the OPC UA client can access.

   The certificate store is located in `C:\ProgrammData\SCADAProjects\certstore`.
2. Trust the OPC UA server certificate on the OPC UA client. Follow the procedure described in the user help of the client. If necessary, manually copy the certificate to the folder for trusted certificates.

To trust the server certificate after the first connection attempt, follow these steps:

1. After the first connection attempt, the OPC UA server certificate is in the rejected certificate store on the client device.

   Trust the certificate on the client. Follow the procedure described in the user help of the client. If necessary, manually copy the certificate to the folder for trusted certificates.

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-4)

#### Engineering System as OPC UA client (RT Unified)

##### Introduction

If you are using a Unified PC or a Unified Panel as an OPC UA client, you configure which tags of the OPC UA server the client accesses and which alarm instances it receives in the Engineering System. For this reason, the Engineering System also acts as an OPC UA client during configuration of the device.

##### Provision and installation of the certificates

The client certificate of the Engineering System is created and transferred to the server automatically the first time a connection is established.

Trust the client certificate on the server. Follow the procedure described in the user help of the server. If necessary, manually copy the certificate to the folder for trusted certificates.

The Engineering System automatically receives the server certificate and trusts it without your having to take any action.

---

**See also**

[Introduction (RT Unified)](#introduction-rt-unified-4)

### Audit certificates (PC) (RT Unified)

This section contains information on the following topics:

- [Workflow (RT Unified)](#workflow-rt-unified-1)
- [Creating certificates (Audit for PCs) (RT Unified)](#creating-certificates-audit-for-pcs-rt-unified)
- [Installing certificates (Audit for PCs) (RT Unified)](#installing-certificates-audit-for-pcs-rt-unified)

#### Workflow (RT Unified)

##### Introduction

The WinCC Unified Audit option uses certificates to generate a checksum for Audit Trail data records. The checksum can be used to determine if the contents of a data record have been altered. The checksum also ensures that no lines have been removed from or added to the Audit Trail.

Audit certificates are not used for communication with another device.

The Audit certificate of a Unified Panel or Unified PC must be issued by a Unified certificate authority (CA-based certificate). You use the "WinCC Unified Certificate Manager" application for this.

> **Note**
>
> Certificate Manager always creates CA-based certificates. The use of CA-based certificates facilitates establishment of the trust relationship and provides the highest protection for your plant.
>
> The use of self-signed certificates is not supported for Audit.

##### Required certificates

For WinCC Unified Audit, you need the following certificates:

- Audit certificate of the HMI device
- Root certificate of the certificate authority that issued the Audit certificate, along with its CRL file.

##### Workflow

To provide the certificates needed by an HMI device for Audit, follow these steps:

1. Create the Audit certificate of the HMI device.
2. Install the Audit certificate on the HMI device.
3. Restart Runtime on the HMI device.

#### Creating certificates (Audit for PCs) (RT Unified)

##### Introduction

You create the Audit certificate of a Unified PC on the certificate authority device. You use the "WinCC Unified Certificate Manager" application for this.

The certificate authority device is always a Unified PC.

##### Procedure

If you do not have a certificate authority yet, follow these steps:

1. Create the certificate authority.

   In so doing, you create the root certificate of the certificate authority and its CRL file automatically.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
2. Add the PC to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
3. Add the Collaboration certificate to the PC.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

If you already have a certificate authority, follow these steps:

1. If the PC has not yet been added to the infrastructure of the certificate authority, add the PC.

   See section [Adding devices](#adding-devices-rt-unified).
2. Add the Audit certificate to the PC.   
   See section [Add application certificates](#add-application-certificates-rt-unified).

#### Installing certificates (Audit for PCs) (RT Unified)

##### Introduction

The audit certificate of a Unified PC is installed in the following steps:

- Export on the certificate authority device
- Import on the PC
- Installation on the PC

> **Note**
>
> You always export and import all certificates of the PC as well as the root certificate of the issuing certificate authority and its CRL file.

##### Requirement

- The Audit certificate has been added for the PC on the certificate authority device.

##### Procedure

1. Export the certificates of the PC on the certificate authority device. Use the WinCC Unified Certificate Manager for this.

   See section [Exporting certificates of a Unified PC](#exporting-certificates-of-a-unified-pc-rt-unified).
2. Import the certificates to the PC. Use the Certificate Manager for this.

   See section [Importing certificates of a Unified PC](#importing-certificates-of-a-unified-pc-rt-unified).
3. Install all certificates together on the PC or only the Audit certificate. Use the Certificate Manager for this.

   See section [Installing all certificates or single certificates of a PC](#installing-all-certificates-or-single-certificates-of-a-pc-rt-unified).

## Working with certificates (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Workflow for using certificates on HMI devices (RT Unified)](#workflow-for-using-certificates-on-hmi-devices-rt-unified)
- [Determining the required application certificates (RT Unified)](#determining-the-required-application-certificates-rt-unified)
- [Selecting a suitable certificate type (RT Unified)](#selecting-a-suitable-certificate-type-rt-unified)
- [Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)
- [Managing own certificates of a Unified PC (RT Unified)](#managing-own-certificates-of-a-unified-pc-rt-unified)
- [Managing third-party certificates of a Unified PC (RT Unified)](#managing-third-party-certificates-of-a-unified-pc-rt-unified)

### Basics (RT Unified)

This section contains information on the following topics:

- [Communication partners (RT Unified)](#communication-partners-rt-unified)
- [Own certificates and third-party certificates of HMI devices (RT Unified)](#own-certificates-and-third-party-certificates-of-hmi-devices-rt-unified)
- [Unified tools for certificates (RT Unified)](#unified-tools-for-certificates-rt-unified)
- [Device binding of a certificate (RT Unified)](#device-binding-of-a-certificate-rt-unified)
- [Communication with S7-1500 and S7-1200 (RT Unified)](#communication-with-s7-1500-and-s7-1200-rt-unified)
- [Runtime and simulation (RT Unified)](#runtime-and-simulation-rt-unified)

#### Communication partners (RT Unified)

The following table shows:

- With which communication partners a Unified HMI device can communicate via certificates.
- Whether the usage of certificates is mandatory for communication.

| Communication partners | Using certificates ... | See also |
| --- | --- | --- |
| Runtime of a different Unified HMI device | Communication runs via Runtime Collaboration: Is obligatory | [Workflow (Collaboration for Panels)](#workflow-collaboration-for-panels-rt-unified)    [Workflow (Collaboration for PCs)](#workflow-collaboration-for-pcs-rt-unified) |
| Communication runs via OPC UA: Depends on the security guideline configured at the OPC UA server. | [OPC UA certificates (Panel)](#opc-ua-certificates-panel-rt-unified)    [OPC UA certificates (PC)](#opc-ua-certificates-pc-rt-unified) |  |
| Web client<sup>1</sup> | Is obligatory | [Web server certificates (Panel)](#web-server-certificates-panel-rt-unified)    [Web server certificates (PC)](#web-server-certificates-pc-rt-unified) |
| Smart Client<sup>2</sup> | Depends on the configuration of the Panel in the Engineering System. | [Smart Server certificates for Panels](#smart-server-certificates-for-panels-rt-unified) |
| S7 PLC of the series S7-1500 and S7-1200 | Depends on the configuration of the controller in the Engineering System. | [Communication with S7-1500 and S7-1200](#communication-with-s7-1500-and-s7-1200-rt-unified) |
| Other Siemens devices  Example: S7 PLC of a different series, SINUMERIK device or Comfort Panel | Communication runs via OPC UA: Depends on the security guideline configured at the OPC UA server. | [OPC UA certificates (Panel)](#opc-ua-certificates-panel-rt-unified)    [OPC UA certificates (PC)](#opc-ua-certificates-pc-rt-unified) |
| Third-party devices |  |  |
| <sup>1</sup>Only for communication with a Unified Runtime web server   <sup>2</sup>Only for communication with a Unified Panel WinCC Smart Server |  |  |

> **Note**
>
> **Audit**
>
> The audit certificate is not used for communication with a communication partner.

---

**See also**

[Certificates in WinCC Unified Runtime (RT Unified)](#certificates-in-wincc-unified-runtime-rt-unified-1)

#### Own certificates and third-party certificates of HMI devices (RT Unified)

**Own certificates**

An HMI device authenticates itself to its communication partners or encrypts the communication with the communication partners with its own certificates.

An HMI device can have the following own certificates:

|  | Storage location on the HMI device |
| --- | --- |
| CA-based application certificates | Unified certificate store, in the folder containing the own certificates |
| Self-signed application certificates | Internal |
| General certificates (always CA-based) | Unified PC: Certificate store of the application that uses the general certificate  Unified Panel: Unified certificate store, in the folder containing the own certificates |

> **Note**
>
> When you install CA-based own certificates on an HMI device, you install the root certificate of the Unified certificate authority and its CRL file automatically.
>
> The root certificate and CRL file do not belong to the own certificates. These files are located in the certificate store, in the folder containing the trusted certificate authorities.
>
> They are installed on the HMI device in order to establish the trust relationship with other HMI devices of the same Unified certificate authority automatically. This help includes the root certificate and CRL file in the group of third-party certificates.

**Third-party certificates**

The communication partners use the third-party certificates to authenticate themselves to the HMI device or encrypt the communication with the HMI device.

An HMI can have the following third-party certificates:

|  | Storage location on the HMI device |
| --- | --- |
| CA-based application certificates | Unified certificate store, in the third-party certificates folder |
| Self-signed application certificates |  |
| General certificates (always CA-based) |  |
| When using a third-party CA-based certificate: Root certificate and CRL file of the issuing certificate authority | Unified certificate store, in the folder containing the trusted certificate authorities |

---

**See also**

[Unified tools for certificates (RT Unified)](#unified-tools-for-certificates-rt-unified)
  
[Determining the required application certificates (RT Unified)](#determining-the-required-application-certificates-rt-unified)
  
[Using general certificates (RT Unified)](#using-general-certificates-rt-unified)

#### Unified tools for certificates (RT Unified)

##### Introduction

This section describes the tools you use to perform the following tasks:

- Creating and managing own certificates of the HMI device and distributing them to the communication partners
- Installing and managing own certificates of an HMI device on the device
- Trusting and managing the third-party certificates of the communication partners on the HMI devices

Information on how to create the third-party certificates and how to install the Unified certificates on the devices of the communication partners can be found in the user help of the respective communication partner.

##### Creating and distributing CA-based own certificates

You create the CA-based certificates of your HMI devices on the certificate authority device with the WinCC Unified Certificate Manager tool.

You use Certificate Manager to perform the following tasks:

- Creating the Unified certificate authority (private key, root certificate and CRL file)
- Issuing or renewing the application certificates and general certificates of your HMI devices
- Exporting the configured certificates as setup for installation on the respective HMI devices

  The procedure is different for application certificates and general certificates.
- Distributing the root certificate and its CRL file to the communication partners

  > **Note**
  >
  > **Alternative for Unified PCs**
  >
  > If the certificates of a Unified PC were already installed on the PC, you can also export the root certificate and its CRL file on the PC with SIMATIC Runtime Manager and distribute them to the communication partners.
- Recreating the complete configuration of the certificate authority
- Creating a backup of the complete configuration of the certificate authority

##### Installing and managing CA-based own certificates

You install and manage CA-based own certificates of an HMI device with the following tools:

- Unified PC:

  - Application certificates: WinCC Unified Certificate Manager
  - General certificates: The installation is performed outside of Certificate Manager. See section [Using general certificates](#using-general-certificates-rt-unified).
- Unified Panel: Control Panel (application certificates and general certificates)

The tools access the Unified certificate store of the HMI device.

##### Installing the Unified root certificate

During export, import and installation of CA-based own certificates of an HMI device, the root certificate of the Unified certificate authority and its CRL file are also exported and imported and installed in the folder containing the trusted root certificate authorities.

Alternatively, you can individually install the root certificate and/or its CRL file. On a Unified PC you use SIMATIC Runtime Manager for this. On a Unified Panel you use Control Panel.

##### Creating, installing and distributing self-signed own certificates

HMI devices that are used as a Runtime web server or an OPC UA server can use self-signed own certificates instead of CA-based certificates.

Unified PCs that are used as an OPC UA server can also use a self-signed OPC UA exporter certificate.

Unified Panels that are Smart Servers can only use a self-signed Smart Server certificate.

You use the following tools to create these certificates and install them in the own certificates:

| Certificate | Tool |
| --- | --- |
| Self-signed web server certificate of a Unified PC | Creation and installation of the certificate: with WinCC Unified Configuration  Transfer to the web clients: automatically |
| Self-signed web server certificate of a Unified Panel | The certificate is created and installed automatically. |
| Self-signed OPC UA server certificates of a Unified Panel or Unified PC  Self-signed OPC UA exporter certificate of a Unified PC |  |
| Self-signed Smart Server certificate of a Unified Panel |  |

The certificates are automatically transferred when the connection to the communication partners is established.

##### Managing third-party certificates

You use the following tools to manage the certificates of the communication partners of an HMI device:

| Device type | Tool |
| --- | --- |
| Unified PC | SIMATIC Runtime Manager |
| Unified Panel | Control Panel |

This includes the following activities:

- Importing root certificates and their CRL files

  You can also export the root certificate and CRL file with SIMATIC Manager.
- Trusting or rejecting certificates
- Displaying details for a certificate
- Uninstalling certificates by deleting them

The tools access the Unified certificate store of the HMI device.

---

**See also**

[Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)
  
[Managing third-party certificates of a Unified PC (RT Unified)](#managing-third-party-certificates-of-a-unified-pc-rt-unified)
  
[Managing own certificates of a Unified PC (RT Unified)](#managing-own-certificates-of-a-unified-pc-rt-unified)
  
[Using CA-based certificates (RT Unified)](#using-ca-based-certificates-rt-unified)

#### Device binding of a certificate (RT Unified)

##### Introduction

An application certificate is always bound to the device on which the application is installed. In order for the certificate to be bound to a device, the following information is written to the certificate:

- Device name   
  Restricts communication to accesses from the same network

  or

  Fully Qualified Domain Name/FQDN   
  If the device belongs to a domain
- Or the IP address   
  Only when fixed IP addresses are used
- Or both

The communication partners use this information to verify whether the sender of the transferred certificate is identical to the device for which the certificate was issued.

##### Device binding for CA-based certificates

When you use CA-based Unified certificates, you configure the information used to bind the application certificates to the HMI device when you add the HMI device in WinCC Unified Certificate Manager. All application certificates of the device use the same setting.

> **Note**
>
> A subsequent change to this setting is only possible if you delete the device from the CA infrastructure and add it again. You must then add, distribute and install the application certificates of the device again.
>
> For this reason, it is recommended that the device name/FQDN and IP address be entered for this setting.

> **Note**
>
> **Device binding for Unified PC web server**
>
> The web server certificate must always also contain the information that is used to generate the address of the identity provider and the website of WinCC Unified Runtime. You define the method for generating this address during installation of Runtime or later with the WinCC Unified Configuration tool in the "Website settings" step.

> **Note**
>
> **Device binding for OPC UA server and OPC UA exporter**
>
> The application certificates for OPC UA server and OPC UA exporter must always also contain the device name or FQDN.

##### Device binding for self-signed certificates

Self-signed Unified certificates are always bound to the certificate using device name/FQDN and IP address.

---

**See also**

[Adding devices (RT Unified)](#adding-devices-rt-unified)

#### Communication with S7-1500 and S7-1200 (RT Unified)

Runtime Unified supports secure communication with PLCs of the series S7-1200 and S7-1500.

With secure communication, the connection between Runtime and PLC is encrypted by the TLS protocol. A valid PLC certificate must be configured on the PLC.

##### Requirement

- Firmware installed on the controller:

  - S7-1500: 2.9 and higher
  - S7-1200: 4.5 and higher
- A certificate was provided for the controller in the Certificate Manager in the Engineering System.

  > **Note**
  >
  > It is recommended to enable the "Only allow secure PG/PC and HMI communication" option on the PLC under "Protection &amp; Security &gt; Connection mechanism". If this option is selected, the Engineering System automatically generates a self-signed PLC certificate. The PLC always uses secure communication. Disabling this option increases the security risk.
  >
  > You can replace this default certificate in the certificate manager of TIA Portal:
  >
  > - Generate your own self-signed certificate with different certificate settings.
  > - Upload a self-signed one.
  > - Upload a CA-based certificate, the root certificate of the issuing certification authority and its CRL file.
  >
  > More information on the certificate manager of TIA Portal is available in the TIA Portal online help under "Editing devices and networks &gt; Configuring devices and networks &gt; Configuring networks &gt; Secure Communication &gt; Secure PG/HMI Communication".
- Communication between HMI device and PLC:

  - The HMI device has an integrated connection to the PLC.  
    Or
  - The HMI device has a non-integrated connection to a device proxy. The device proxy uses the current device proxy data of the PLC.  
    Or
  - The HMI device has been connected to the PLC using the "ChangeConnection" system function.

##### Connection establishment

The PLC sends its certificate to the HMI device (one-way SSL authentication). The HMI device checks the certificate:

- If the HMI device trusts the PLC certificate, the connection is established. The session remains until the connection is interrupted. The process is repeated the next time the connection is established.

  > **Note**
  >
  > Stopping or restarting Runtime interrupts the connection.
  >
  > The following actions do not interrupt the connection:
  >
  > - Stopping or restarting the PLC.
  > - Download to device (PLC or HMI device)
- If the HMI device does not trust the certificate, the connection is rejected. A system event is output. After the time needed for reconnection (ReconnectTime) has elapsed, the HMI device starts a new connection attempt.

**Integrated connection and non-integrated connection via device proxy.**

When loading the HMI device, the PLC certificate is automatically loaded into the HMI device as well. The PLC certificate is part of the current configuration of the device and has the "Trusted" status. It is managed internally in the system and is not visible in SIMATIC Runtime Manager or in the Control Panel.

When establishing a connection, the HMI device already trusts the PLC certificate. The connection is established automatically.

> **Note**
>
> If you change the PLC certificate after loading the HMI device without reloading the HMI device, the HMI device will not trust the new PLC certificate the next time it connects. You must trust the certificate manually.

**Connection via "ChangeConnection"**

After calling the "ChangeConnection" system function, the HMI device initially does not trust the PLC certificate. The PLC certificate has the status "untrusted". You must trust the certificate manually.

##### Distributing a PLC certificate manually

Proceed as described here:

- Unified PC: [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified)
- Unified Panel: [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)

##### Communication with other controllers

The certificated-protected communication between a Unified HMI device and a Siemens controller with different firmware, or from a different series, or with a controller from a third party must run via OPC UA.

---

**See also**

[Communication partners (RT Unified)](#communication-partners-rt-unified)

#### Runtime and simulation (RT Unified)

When the communication of an HMI device is protected through the use of certificates, you need certificates for simulation and system operation of the device.

### Workflow for using certificates on HMI devices (RT Unified)

#### Introduction

If you are using security-related Unified components on the HMI devices of your system, you must provide the following certificates:

- Certificates used by the HMI devices to authenticate themselves to their communication partners (Unified certificates)
- Certificates used by the communication partners of the HMI devices to authenticate themselves to the HMI devices (third-party certificates)

> **Note**
>
> Some components require a mutual SSL authentication, meaning that both the HMI device and its communication partner need a certificate. They must trust each other's certificates.
>
> Other components require a one-way SSL authentication, meaning that only the HMI device needs a certificate and its communication partner must trust the certificate, or vice versa.
>
> See also section [Determining the required application certificates](#determining-the-required-application-certificates-rt-unified).

#### Procedure

To provide these certificates, follow these steps:

1. Determine which application certificates are needed by the HMI devices and which are needed by their communication partners.

   See section [Determining the required application certificates](#determining-the-required-application-certificates-rt-unified).
2. Decide whether to use CA-based or self-signed certificates for these certificates.

   See section [Selecting a suitable certificate type](#selecting-a-suitable-certificate-type-rt-unified).
3. When using CA-based Unified certificates, issue the needed application certificates of the HMI device with a Unified certificate authority, distribute them to the HMI devices and install them there:

   - If you do not have a certificate authority yet, follow the procedure described in section [First-time use of CA-based certificates](#first-time-use-of-ca-based-certificates-rt-unified).
   - If you already have a certificate authority, follow the procedure described in section [Continued use of CA-based certificates](#continued-use-of-ca-based-certificates-rt-unified).
4. The use of self-signed certificates is also possible for the following components:

   - Unified OPC UA server
   - Unified OPC UA exporter
   - Unified web server
   - Smart Server

   You can find information on creating and installing the certificates in section [Using self-signed certificates](#using-self-signed-certificates-rt-unified).
5. Create the certificates of the communication partners and install them on their devices.

   To do this, follow the procedure described in the user help of the respective communication partner.
6. Establish the trust relationship between the HMI devices and their communication partners:

   - For CA-based certificates, follow the procedure described in section [Trusting CA-based certificates](#trusting-ca-based-certificates-rt-unified).
   - For self-signed certificates, follow the procedure described in section [Using self-signed certificates](#using-self-signed-certificates-rt-unified).

**Note**

The use of CA-based certificates is recommended.

CA-based certificates are mandatory for some Unified components.

**Note**

**Installation at runtime**

When you install the CA-based certificates of an HMI device at runtime, the existing connections are not interrupted. The HMI device does not start using the new certificates until after a Runtime restart.

A Runtime restart is not required for use of a newly installed web server certificate.

### Determining the required application certificates (RT Unified)

An application certificate is the certificate which sends an application during the connection establishment to another application to authenticate itself.

#### Procedure

1. Note for each HMI device which security-relevant Unified components are used on the device.
2. Use the table below to determine which application certificate the HMI devices and their communication partners require.

**Note**

Some components require reciprocal SSL authentication, meaning that the HMI device and its communication partner both require a certificate. They must trust their certificates reciprocally.

Some components require one-sided SSL authentication, meaning that only the HMI device requires a certificate and its communication partner must trust the certificate or vice versa.

#### Required certificates

| Unified components used on the HMI device | Communication partners of the HMI device | Required application certificates | Trust relationship |
| --- | --- | --- | --- |
| Runtime web server<sup>1</sup> | Web clients | The HMI device requires a web server certificate. | One-sided SSL authentication  The web clients must trust the web server certificate. |
| OPC UA Server | OPC UA clients | The HMI device requires an OPC UA Server certificate and the communication partners an OPC UA Client certificate or vice versa. | Reciprocate SSL authentication  The OPC UA clients must trust the OPC UA Server certificate and vice versa. |
| OPC UA Client | OPC UA Server |  |  |
| OPC UA Exporter<sup>2</sup> | n.a. | The Unified PC requires an OPC UA Server certificate and an OPC UA Exporter certificate. | n.a.  OPC UA Server certificate and the OPC UA Exporter certificate trust each other automatically. |
| Collaboration | A different HMI device | Both HMI devices require a Collaboration certificate. | Reciprocate SSL authentication  The devices must trust their Collaboration certificates. |
| Audit | n.a. | The HMI device requires an Audit certificate. | n.a.  The certificate generates checksums. It is not used for communication. |
| Component of the PLC communication | S7-1500 and S7-1200 | The S7 controller requires a certificate. | One-sided SSL authentication  The HMI device must trust the PLC certificate. |
| Smart Server<sup>3</sup> | Smart Client | The Smart Server requires a certificate | One-sided SSL authentication  The Smart Client must trust the Smart Server certificate. |
| <sup>1</sup> Unified PCs are always Runtime web servers. They always need a web server certificate.    <sup>2</sup> Only on Unified PCs that are used as OPC UA servers. OPC UA Exporter exports the runtime variables into an OPC UA Nodeset XML file.    <sup>3</sup> Only for Unified Comfort Panels |  |  |  |

---

**See also**

[Trusting CA-based certificates (RT Unified)](#trusting-ca-based-certificates-rt-unified)
  
[Workflow for using CA-based certificates (RT Unified)](#workflow-for-using-ca-based-certificates-rt-unified)

### Selecting a suitable certificate type (RT Unified)

#### Introduction

Application certificates are issued by a certification instance. By signing the application certificate the certification instance guarantees the authenticity of the certificate and thus the identity of its owner (subject).

There are two types of certification instances:

- A Certificate Authority (CA)

  Application certificates which were signed by a certificate authority are CA-based certificates.

  > **Note**
  >
  > It is not possible to create own CA-based application certificates of an HMI device with an external certificate authority. The certificates must be created by a Unified certificate authority with the application "WinCC Unified Certificate Manager".
- The certificate itself

  Application certificates that confirm the validity of the certificate through their own signature are self-signed certificates.

If a communication partner trusts the certification instance, it trusts all application certificates that were issued by the certificate authority.

> **Note**
>
> This user help assumes that both devices use the same type of certificate authority for reciprocal SSL authentication.
>
> Mixed usage is also technically possible.

#### Supported types

The following table provides an overview of which certificate types support the security-relevant components:

| Component/role of the HMI device | Own certificates |  | Third-party certificates |  |  |
| --- | --- | --- | --- | --- | --- |
| CA-based | Self-signed | Communication partners | CA-based | Self-signed |  |
| Web server | ✓ | ✓ | Web client | n.a. |  |
| OPC UA Client | ✓ | - | OPC UA server | ✓ | ✓ |
| OPC UA Server | ✓ | ✓ | OPC UA Client<sup>1</sup> | ✓ | ✓ |
| OPC UA Exporter<sup>2</sup> | ✓ | ✓ | n.a. |  |  |
| Runtime Collaboration | ✓ | - | Runtime Collaboration partner<sup>3</sup> | ✓ | - |
| Audit | ✓ | - | n. a. |  |  |
| PLC communication | n.a. |  | S7-1500, S7-1200 | ✓ | ✓ |
| Smart Server | - | ✓ | Smart Client | n.a. |  |
| <sup>1 </sup>If the OPC UA Client is an HMI device, the Client HMI device must use a CA-based certificate.   <sup>2</sup> Variable export is only possible on Unified PCs that are used as OPC UA Servers. The OPC UA Exporter component communicates with the OPC UA Server component of the Unified PC. Communication with a different device does not take place for the variable export.    <sup>3</sup> The communication partner must also be a Unified HMI device. Its certificate must be issued by a Unified certificate authority. |  |  |  |  |  |

#### Selection of the suitable type

CA-based certificates are especially suitable in the following cases:

- For a high protection level of the plant communication
- For access to an HMI device from an external network

Self-signed certificates are suitable:

- For testing the system configuration
- For small plants or plant sections that operate in a closed network

> **Note**
>
> - For security reasons the use of CA-based certificates is recommended, both for Unified certificates as well as for third party certificates.
> - When making your decision, also consider internal company specifications or project-specific factors such as the security guideline that is relevant for a plant.

#### Benefits from the usage of CA-based Unified certificates

- Central creation and management of all Unified certificates
- Easy distribution of the certificates TO the HMI devices as well as installation on the HMI devices
- Easy update, distribution and installation of expired certificates during running operation, including update of the entire certificate configuration of the certificate authority in case the root certificate expires.
- Easy establishment of the trust relationship to the HMI devices at the communication partners
- Encrypted, password-protected export and import of certificates
- Very high protection level of the communication
- Simple data backup of the entire configuration of the certificate authority

#### Benefits for the use of self-signed Unified certificates

- No or low effort for the creation of the certificates and for their installation on the HMI devices

---

**See also**

[Unified certificate authority (RT Unified)](#unified-certificate-authority-rt-unified)
  
[Using self-signed certificates (RT Unified)](#using-self-signed-certificates-rt-unified)
  
[Requirements and limitations when using CA-based certificates (RT Unified)](#requirements-and-limitations-when-using-ca-based-certificates-rt-unified)

### Managing third party certificates and own certificates of a Unified Panel (RT Unified)

#### Introduction

You manage the CA-based own certificates of the panel and its third-party certificates in the Control Panel of a Unified Panel.

> **Note**
>
> Self-signed own certificates are generated and installed outside the Control Panel. You have the possibility to delete them in the Control Panel.
>
> Certificates of S7 controllers with an integrated connection to the Panel are managed system-internally. They are not visible in the Control Panel.

**Own certificates**

The Control Panel offers the following possibilities for own certificates:

| Symbol | Meaning |
| --- | --- |
| Import and install | Only for CA-based own certificates  Proceed as described:   - For application certificates, see the section [Importing and installing certificates of a Panel](#importing-and-installing-certificates-of-a-panel-rt-unified). - For general certificates, see the section [Workflow for general certificates](#workflow-for-general-certificates-rt-unified). |
| Display | For CA-based and self-signed certificates  Proceed as described below. |
| Delete |  |

**Third-party certificates**

The Control Panel offers the following possibilities for third party certificates:

|  |  |  |  |
| --- | --- | --- | --- |
|  | Root certificates and CRL files | Application certificates and general certificates |  |
| Import and install | ✓ | - | You import and install only root certificates and their CRL file manually. Follow the steps described in the section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified).   A third-party CA-based application certificate or general certificate is automatically trusted by the panel if its root certificate is installed on the panel. Manual import and installation of the certificate are not required.  Third-party self-signed certificates are transferred automatically during the first connection attempt at the certificate stores of the Panel and receive the status "untrusted". You can trust or delete them in the Control Panel. Manual import and installation of the certificate are not required. |
| Display | ✓ | ✓ | Proceed as described below.  As a rule you only trust self-signed certificates manually. CA-based certificates are trusted by the Panel automatically after import and installation of the root certificate. |
| Trust | - | ✓ |  |
| Reject | - | ✓ |  |
| Delete | ✓ | ✓ |  |

> **Note**
>
> Third-party application-certificates can be CA-based or self-signed. Third-party general certificates must be CA-based.

**More information**

You can find additional information on the function "Certificates" of the Control Panel in the "SIMATIC HMI devices Unified Comfort Panels" operating instructions.

#### Display

1. In the Control Panel, select "Security"" &gt; "Certificates".
2. In the "Certificate stores" list select one of the following entries:

   - To display own certificates, select the entry "My Certificates".

     You can see a list with own certificates of the Panel.
   - To display third-party application certificates or third-party general certificates, select the entry "Other Certificates".

     You can see a list of the CA-based or self-signed third party certificates available on the Panel. You see both certificates with the status "Trusted" and "Untrusted".
   - For root certificates and their CRL files select the entry "Certificate Authorities".

     You see a list of the root certificates installed on the panel as trusted and their CRL files.
3. Click the desired certificate.

The certificate details are displayed.

#### Trusting or rejecting

1. In the Control Panel select "Security" &gt; "Certificates".
2. Select the "Other Certificates" entry from the "Certificate stores" list.

   You see both certificates with the status "Trusted" and "Untrusted".
3. To trust a third-party certificate marked as untrusted, select it and choose "Trust".

   The certificate receives the status "Trusted".
4. To identify a third-party certificate as untrusted without deleting, mark it and select "Revoke".

   The certificate receives the status "Untrusted".

   The certificate is still available in the certificate store. If required, you can trust them again in the future.

#### Delete

> **Note**
>
> Deleting uninstalls and removes a certificate from the certificate store.

1. In the Control Panel select "Security" &gt; "Certificates".
2. Select the desired entry from the "Certificate stores" list.

   Depending on the selected entry you see a list of the certificates available on this device. After selection of "Other certificates" you see both certificates with the status "Trusted" and "Untrusted".
3. Click the desired certificate or the CRL file and select "Delete".

The selected certificate or the file is deleted immediately without query.

---

**See also**

[Deleting application certificates (RT Unified)](#deleting-application-certificates-rt-unified)

### Managing own certificates of a Unified PC (RT Unified)

#### Overview

You manage the CA-based own application certificates of a Unified PC with WinCC Unified Certificate Manager.

Certificate Manager offers the following options:

| Symbol | Meaning |
| --- | --- |
| Import and install | Follow the procedure described in section [Importing and installing certificates of a Unified PC](#importing-and-installing-certificates-of-a-unified-pc-rt-unified). |
| Display | Follow the procedure described below. |
| Delete |  |

> **Note**
>
> Self-signed own certificates are created, installed and managed outside of Certificate Manager.
>
> You install and manage general own certificates outside of Certificate Manager. See section [Workflow for general certificates](#workflow-for-general-certificates-rt-unified).

For information on how to manage the third-party certificates of the PC (self-signed certificates and CA-based certificates of the communication partners and their root certificates), see section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

#### Requirement

- Certificate Manager is open on the Unified PC.
- The certificates of the device have been imported or imported and installed with Certificate Manager.
- The "Installed certificates" tab is visible.

#### Displaying a certificate

1. Select a certificate.

The "Details" area shows detailed information about the certificate.

#### Deleting a certificate

1. Select a certificate.
2. Right-click and select "Delete".

The certificate is uninstalled.

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

### Managing third-party certificates of a Unified PC (RT Unified)

#### Introduction

Data exchange between WinCC Unified Runtime and its communication partners can be protected by certificates. The communication partners use self-signed certificates or certificates issued by a certificate authority (CA-based certificates).

In the SIMATIC Runtime Manager, you manage the certificates of the communication partners of the Unified PC (third-party certificates) in the "Certificates" tab.

You have the following options:

- Importing certificates, root certificates and CRL files
- Trust, reject, or delete certificates and root certificates already in the certificate store
- Exporting certificates, root certificates and CRL files to distribute them to other devices

  > **Note**
  >
  > **Alternative**
  >
  > If the Unified PC has its own CA-based certificates, you can also export the root certificate and CRL file of its Unified Certificate Authority using the WinCC Unified Certificate Manager application.

> **Note**
>
> **Import and export of root certificates and CRL files**
>
> A root certificate and its CRL file must be imported separately.
>
> If you have exported a root certificate, its CRL file is also exported. If required, you can also export the CRL files individually.

> **Note**
>
> Certificates of S7 controllers with an integrated connection to the Unified PC are managed system-internally. They are not visible in the SIMATIC Runtime Manager.

#### Structure

![Structure](images/153675591179_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Button for importing a certificate or CRL file |
| ② | "Certificates" area  A list of the third-party certificates available in the certificate store (self-signed certificates, CA-based certificates and their root certificate). If the PC has its own CA-based certificates, you can also find the root certificate of the Unified Certificate Authority here. |
| ③ | "State" column  Shows whether the Unified PC trusts a certificate. |
| ④ | "Certificate Revocation Lists (CRL)" area  A list of the root certificate CRL files from "Certificates" |

#### Requirement

- The Runtime Manager is open.
- The certificates and CRL files to be imported are located in a folder to which the Unified PC has access.

#### Managing certificates

| 1. Click the ![Managing certificates](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar. 2. Select the "Certificates" tab. 3. You can perform the following actions:       | Action | Procedure |    | --- | --- |    | Import and trust | | Symbol | Meaning | | --- | --- | | 1. Click "Import new certificate or certificate revocation list (CRL)":               ![Managing certificates](images/143169617931_DV_resource.Stream@PNG-de-DE.png)         ![Managing certificates](images/143169617931_DV_resource.Stream@PNG-de-DE.png) 2. Select the location where the certificate is stored, for example, an external data carrier, and select the certificate. 3. Confirm your input. |  |  The certificate is imported and copied to the "trusted" folder on the PC. Or the CRL file is imported. |    | Trust | Right-click on a certificate and select "Trust". The certificate is moved to the "trusted" folder on the PC. |    | Reject | Right-click the certificate and select "Reject". The certificate is moved to the "untrusted" folder on the PC. |    | Display | Right-click on a certificate and select "Show". A window with detailed information on the certificate opens. |    | Delete | Right-click on a certificate and select "Delete". The certificate is deleted from the certificate store on the PC. |    | Export | | Symbol | Meaning | | --- | --- | | 1. Right-click the certificate and select "Export". 2. If you have selected a root certificate, select the file format. 3. Select the target folder, for example, an external data storage medium. 4. Confirm your input. |  |  The certificate is copied to the target folder. If you have selected a root certificate, its CRL file is also copied. Distribute the files to the desired devices. To do this, proceed as described in the application help of the device. | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Managing CRL files

| 1. Click the ![Managing CRL files](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar. 2. Select the "Certificates" tab. 3. You can perform the following actions:       | Action | Procedure |    | --- | --- |    | Import | | Symbol | Meaning | | --- | --- | | 1. Click "Import new certificate or certificate revocation list (CRL)":               ![Managing CRL files](images/143169617931_DV_resource.Stream@PNG-de-DE.png)         ![Managing CRL files](images/143169617931_DV_resource.Stream@PNG-de-DE.png) 2. Select the location of the CRL file, e.g. an external data storage medium, and select the file. 3. Confirm your input. |  |  The file is imported and copied in the "trusted" folder on the PC. |    | Delete | Right-click on a CRL file and select "Delete". The file is deleted from the "trusted" folder on the PC. |    | Export | | Symbol | Meaning | | --- | --- | | 1. Right-click on the CRL file and select "Export". 2. Select the file format. 3. Select the target folder, for example, an external data storage medium. 4. Confirm your input. |  |  The CRL file is copied to the target folder. Distribute the files to the desired devices. To do this, proceed as described in the application help of the device. | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

---

**See also**

[Exporting root certificate and CRL file (RT Unified)](#exporting-root-certificate-and-crl-file-rt-unified)
  
[Managing own certificates of a Unified PC (RT Unified)](#managing-own-certificates-of-a-unified-pc-rt-unified)

## Using CA-based certificates (RT Unified)

This section contains information on the following topics:

- [Requirements and limitations when using CA-based certificates (RT Unified)](#requirements-and-limitations-when-using-ca-based-certificates-rt-unified)
- [Basics of CA-based communication (RT Unified)](#basics-of-ca-based-communication-rt-unified)
- [Unified certificate authority (RT Unified)](#unified-certificate-authority-rt-unified)
- [Workflow for using CA-based certificates (RT Unified)](#workflow-for-using-ca-based-certificates-rt-unified)
- [Creating and exporting the CA infrastructure (RT Unified)](#creating-and-exporting-the-ca-infrastructure-rt-unified)
- [Importing and installing certificates of a Unified PC (RT Unified)](#importing-and-installing-certificates-of-a-unified-pc-rt-unified)
- [Importing and installing certificates of a Unified Panel (RT Unified)](#importing-and-installing-certificates-of-a-unified-panel-rt-unified)
- [Trusting CA-based certificates (RT Unified)](#trusting-ca-based-certificates-rt-unified)
- [Exporting an application certificate as a public certificate (RT Unified)](#exporting-an-application-certificate-as-a-public-certificate-rt-unified)

### Requirements and limitations when using CA-based certificates (RT Unified)

The following requirements and limitations apply to the use of CA-based Unified certificates.

#### Requirements

- The certificate authority device must be a Unified PC.
- Users need local Administrator rights to start WinCC Unified Certificate Manager.

#### Limitations

- Use of an external certificate authority is not possible.
- The certificate authority and certificates must be created with Certificate Manager.
- The CA infrastructure includes the root with the root certificate and the end-entities with the application certificates. Use of intermediate certificates (intermediate CAs) is not possible.
- The root certificate has a maximum lifetime of 150 months.
- Application certificates become invalid when their root certificate expires.
- Runtime Collaboration requires that the Collaboration certificates of 2 Collaboration partners be created with a certificate authority device whose installed Runtime version is equal to or higher than the installed Runtime version of the Collaboration partner with the higher Runtime version.

  For this reason, the upgrading of Collaboration devices requires the creation, distribution and installation of new Collaboration certificates.

  Example:

  - A Unified PC and a Unified Panel with Runtime version V17 are Collaboration partners.
  - You upgrade the Panel to V18.
  - Create new Collaboration certificates for both HMI devices on a certificate authority device with installed Runtime version V18 or higher. Distribute them to and install them on the devices.

### Basics of CA-based communication (RT Unified)

> **Note**
>
> This user help assumes that, in the case of mutual SSL authentication, both devices use the same type of certificate authority.
>
> A mixed use is technically also possible.

#### Certificate authorities

CA-based certificates are issued by a certificate authority (CA). The certificate authority can be an independent organization or a recognized service provider. Companies themselves can also act as certificate authority. They themselves then issue certificates, for example, for company-internal communication or for communication with partners or customers.

By signing the application certificate, the certificate authority guarantees the authenticity of the certificate and, thus, the identity of its owner (subject).

For use of CA-based Unified certificates, you need a Unified certificate authority. See section [Unified certificate authority](#unified-certificate-authority-rt-unified).

#### Establishing the trust relationship in CA-based communication

When a device trusts the root certificate of a certificate authority, it automatically trusts all application certificates issued by this certificate authority.

#### Communication using public and private keys

When CA-based certificates are used, communication takes place using public and private keys

- A certificate authority has a private key and a public key.

  - The certificate authority signs the certificates it issues. It uses the private key for this. The signature guarantees that the certificate was really issued by the certificate authority.

    The private key remains secret. It is known only to the certificate authority.
  - The public key is the root certificate.

    When a device trusts the root certificate, it trusts all application certificates that were signed with the private key of the certificate authority.
- The certificate authority issues a CA-based application certificate for a device on request.

  - It binds the certificate to the device. See also section [Device binding of a certificate](#device-binding-of-a-certificate-rt-unified).
  - It signs the application certificate with its private key.
  - It creates a private key and a public key for the application certificate.

    These keys are used later to encrypt the communication between the device and its communication partners.
- The device must install the application certificate in its certificate store in the folder containing the own certificates.
- In the case of one-way SSL authentication, you establish the trust relationship between the communication partner and the device by exporting the root certificate of the application certificate and installing it on the communication partner in the folder containing the trusted certificate authorities.
- When the device establishes a connection to the communication partner, it transfers the public key of its application certificate. The communication partner checks the following:

  - The signature of the application certificate belongs to one of the certificate authorities it trusts.
  - The sender of the certificate is identical to the device to which the certificate is bound.

  If this is the case, the communication partner automatically installs the application certificate in its certificate store in the folder with trusted certificates.
- The communication partner generates a session key, encrypts it with the public key of the application certificate and sends it to the device.
- The device decrypts the session key with the private key of its application certificate.
- The device and the communication partner then use this session key to encrypt and decrypt their communication.

In the case of mutual SSL authentication, the device must also trust the root certificate of its communication partner.

#### Use of CA-based Unified certificates

You create and install the CA-based application certificates of an HMI device using WinCC Unified Certificate Manager.

The communication between the HMI device and its communication partners takes place as described above.

The following applies:

- Issuing application certificates, distributing them to the HMI device and installing them there: procedure depends on the communication partners of the device (web clients, OPC UA communication partners, etc.).
- Establishing the trust relationship between an HMI device and its communication partner: procedure depends on the communication partner (web client, OPC UA communication partner, etc.).
- When you use WinCC Unified Certificate Manager to install all certificates of an HMI device together or a single application certificate, the root certificate of the issuing certificate authority is automatically also installed on the HMI device:

  - In the certificate store of WinCC Unified
  - For Unified PCs: In the Windows system certificate store

  If the HMI device has a communication partner whose application certificate has the same certificate authority, the HMI device trusts this certificate automatically.

---

**See also**

[Requirements and limitations when using CA-based certificates (RT Unified)](#requirements-and-limitations-when-using-ca-based-certificates-rt-unified)
  
[Managing third-party certificates of a Unified PC (RT Unified)](#managing-third-party-certificates-of-a-unified-pc-rt-unified)
  
[Selecting a suitable certificate type (RT Unified)](#selecting-a-suitable-certificate-type-rt-unified)
  
[Workflow for using CA-based certificates (RT Unified)](#workflow-for-using-ca-based-certificates-rt-unified)
  
[Creating and exporting the CA infrastructure (RT Unified)](#creating-and-exporting-the-ca-infrastructure-rt-unified)
  
[Importing and installing certificates of a Unified PC (RT Unified)](#importing-and-installing-certificates-of-a-unified-pc-rt-unified)
  
[Importing and installing certificates of a Unified Panel (RT Unified)](#importing-and-installing-certificates-of-a-unified-panel-rt-unified)
  
[Trusting CA-based certificates (RT Unified)](#trusting-ca-based-certificates-rt-unified)

### Unified certificate authority (RT Unified)

For use of CA-based Unified certificates, you need a Unified certificate authority.

> **Note**
>
> The use of an external certificate authority to create CA-based Unified certificates is not supported.

#### Creating the Unified certificate authority

You create the certificate authority on a PC with a Unified Runtime installation using the WinCC Unified Certificate Manager tool.

#### Infrastructure of the Unified certificate authority

The infrastructure of the Unified certificate authority includes the following:

- Root (Root CA)

  The root includes the following:

  - Private key

    The private key is not visible in the user interface of Certificate Manager.
  - Root certificate (public key / CA certificate)

    The root certificate is the highest visible node of the certificate authority in the user interface of Certificate Manager.
  - CRL file (Certificate Revocation List)

    The CRL file contains a list of the certificates that the certificate authority has issued and then revoked.
- Devices for which you issue CA-based certificates

  These are usually HMI devices. When general certificates are used, they can also be other devices.
- Certificates (end-entities/leaf certificates) of the devices

  For HMI devices you create application certificates and, if applicable, general certificates. For devices that are not HMI devices, you create only general certificates.

  The certificates are located under the device nodes in the user interface of Certificate Manager.

> **Note**
>
> Configuration Manager does not support intermediate certificates (intermediate CAs).

#### CA container of the certificate authority

The CA container (certificate authority container) of a Unified certificate authority includes the following:

- Root certificate
- ​CRL file
- ​Application certificates and general certificates of the added devices

#### Complete configuration of the certificate authority

The complete configuration of a Unified certificate authority includes the following:​

- Private key
- ​Root certificate (public key)
- CRL file
- ​Application certificates and general certificates of the added devices

---

**See also**

[Basics of CA-based communication (RT Unified)](#basics-of-ca-based-communication-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)
  
[Selecting a suitable certificate type (RT Unified)](#selecting-a-suitable-certificate-type-rt-unified)
  
[WinCC Unified Certificate Manager (RT Unified)](#wincc-unified-certificate-manager-rt-unified)

### Workflow for using CA-based certificates (RT Unified)

This section contains information on the following topics:

- [First-time use of CA-based certificates (RT Unified)](#first-time-use-of-ca-based-certificates-rt-unified)
- [Continued use of CA-based certificates (RT Unified)](#continued-use-of-ca-based-certificates-rt-unified)

#### First-time use of CA-based certificates (RT Unified)

Follow the procedure described in this section if you do not have a Unified certificate authority yet and want to use CA-based Unified certificates on HMI devices.

You can find information on how to use general CA-based certificates in section [Using general certificates](#using-general-certificates-rt-unified).

> **Note**
>
> This description assumes that both the HMI devices and their communication partners are using CA-based application certificates.

##### Requirement

- WinCC Unified Runtime is installed on the PC that is to serve as the certificate authority (certificate authority device).
- The required CA-based application certificates have been issued for the communication partners.

  To create these certificates, follow the procedure described in the user help of the respective communication partner.
- The root certificate and CRL file of the certificate authority that issued the application certificates of the communication partners have been exported as described in the user help of the respective communication partner. You have access to both files.
- For communication with an S7 controller:

  - The controller has the following firmware:

    S7-1500: Firmware 2.9 or higher

    S7-1200: Firmware 4.5 or higher
  - The HMI device has an integrated connection to the controller.
  - Secure communication was enabled for the controller in the Engineering System

##### Procedure

1. Create the certificate authority and its CA infrastructure (HMI devices and their application certificates) on the certificate authority device.
2. Export the certificates of the HMI devices.
3. Import the certificates of the HMI device to each HMI device and install them there.
4. If you install the certificates of an HMI device at runtime, restart Runtime on the device.
5. Establish the trust relationship between the HMI device and its communication partners for each HMI device.

**Note**

Existing connections are not interrupted by the installation of certificates. Runtime uses the old certificates until it is restarted.

A Runtime restart is not required for use of a newly installed web server certificate.

Follow the procedure described below.

> **Note**
>
> **Certificate authority device as HMI device**
>
> If you are using the certificate authority device as a Unified PC and you only want to provide the application certificates of this PC, the export and import steps are omitted. You can install the certificates of the PC without exporting and importing them beforehand.

##### Creating the certificate authority and CA infrastructure

1. Start the Certificate Manager tool on the certificate authority device.
2. Create the certificate authority.

   See section [Creating a certificate authority and root certificate](#creating-a-certificate-authority-and-root-certificate-rt-unified).
3. Add the needed HMI devices to the certificate authority.

   See section [Adding devices](#adding-devices-rt-unified).
4. Add the needed application certificates to each HMI device.

   See section [Add application certificates](#add-application-certificates-rt-unified).
5. (optional) Create a backup of the complete configuration of the certificate authority

   See section [Create backup](#create-backup-rt-unified).

> **Note**
>
> You can change the infrastructure of your system later, for example, as follows:
>
> - Add or delete application certificates to or from an HMI device.
> - Add or delete HMI devices.
> - Renew application certificates whose lifetime has expired.
> - Renew an expired root certificate or its CRL file.
>
> See section [Continued use of CA-based certificates](#continued-use-of-ca-based-certificates-rt-unified).

##### Exporting certificates of HMI devices

The export of certificates sets up their installation on the HMI devices.

Follow these steps:

- For Unified PCs: Export the CA container once.

  The certificates of all devices of the certificate authority are exported to a common storage file.

  When the file is imported to a Unified PC, you see the certificates of all devices of the certificate authority. However, you can only install the certificates of the local device. The other devices are shown for information purposes only.

  > **Note**
  >
  > If a small storage file is needed to save memory space, you can also export the certificates of a single Unified PC. Then, all certificates of the selected PC are exported to the storage files.

  See section [Exporting certificates of a Unified PC](#exporting-certificates-of-a-unified-pc-rt-unified).
- For Unified Panels: Export the certificates of a single Unified Panel. All certificates of the selected Panel are exported to the storage files.

  Repeat this action for all Panels.

  > **Note**
  >
  > A joint export of the certificates of all devices of the certificate authority is not possible.

  See section [Exporting certificates of a Panel](#exporting-certificates-of-a-panel-rt-unified).

##### Importing and installing certificates

Import the certificates to the HMI devices and install them there:

- For Unified PCs: See sections [Importing certificates of a Unified PC](#importing-certificates-of-a-unified-pc-rt-unified) and [Installing all certificates or single certificates of a PC](#installing-all-certificates-or-single-certificates-of-a-pc-rt-unified).
- For Unified Panels: See sections [Importing and installing certificates of a Panel](#importing-and-installing-certificates-of-a-panel-rt-unified) and [Manually importing and individual certificates to a Panel and installing them](#manually-importing-and-individual-certificates-to-a-panel-and-installing-them-rt-unified).

##### Establishing the trust relationship

> **Note**
>
> If the following conditions are met, no further steps are needed to establish the trust relationship:
>
> - The HMI devices of the certificate authority communicate only with each other and with S7 controllers to which they have an integrated connection.
> - The HMI devices communicate with each other exclusively using CA-based certificates of their common certificate authority.
> - The certificates of the HMI devices have been installed on the devices.
> - For web server communication, you use only the following web clients:
>
>   - Edge and Chrome on Unified PCs that belong to the infrastructure of the certificate authority
>   - Web browser of Unified Panels that belong to the infrastructure of the certificate authority

| 1. Export the Unified root certificate and the CRL file on the certificate authority device using Certificate Manager.    See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).      | Symbol | Meaning |    | --- | --- |    | **Note**   **Alternative approach for Unified PCs**  If one of the HMI devices is a Unified PC whose certificates were already installed with Certificate Manager, you can also export both files on the Unified PC with SIMATIC Runtime Manager. See also section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified). |  | 2. Install the Unified root certificate on the communication partners of the HMI devices:       | Communication partner | Procedure |    | --- | --- |    | Web client of a Runtime web server | Follow the procedure described in section [Trusting the web server certificate](#trusting-the-web-server-certificate-rt-unified) for the respective web client. |    | OPC UA device | Follow the procedure described in the user help of the respective OPC UA communication partner. |    | Runtime Collaboration device | If the Collaboration devices have different Unified certificate authorities, install the root certificate and CRL file of one device on the other, and vice versa. For Panels, follow the procedure described in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified). For PCs, follow the procedure described in section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified). If the devices have the same Unified certificate authority, the devices trust each other automatically. |    | S7 controller | Not applicable |       | Symbol | Meaning |    | --- | --- |    | **Note**  If the same communication partner communicates with multiple HMI devices that have the same certificate authority, install the root certificate on the communication partner once. It is not necessary to manually install the root certificate in some following cases: You will find information on this in the following sections: - [Automatic trust relationship with a PC web server](#automatic-trust-relationship-with-a-pc-web-server-rt-unified) - [Automatic trust relationship with a Panel web server](#automatic-trust-relationship-with-a-panel-web-server-rt-unified) - [Automatic trust relationship in OPC UA communication](#automatic-trust-relationship-in-opc-ua-communication-rt-unified) - [Automatic trust relationship between Collaboration devices](#automatic-trust-relationship-between-collaboration-devices-rt-unified)Where appropriate, check whether the root certificate has already been installed on the communication partner: - Web client as communication partner: See section [Checking the status of the web server root certificate on the web client.](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1). - Runtime Collaboration communication partner: See section [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified). - Remaining communication partners: Follow the procedure described in the user help of the respective communication partner. |  | 3. Install the root certificates of the communication partners on each HMI device:       | Communication partner | Procedure on the HMI device |    | --- | --- |    | Web client | Not applicable |    | Runtime Collaboration device | If the Collaboration devices have different Unified certificate authorities, install the root certificate and CRL file of one device on the other, and vice versa. For Panels, follow the procedure described in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified). For PCs, follow the procedure described in section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified). If the devices have the same Unified certificate authority, the devices trust each other automatically. |    | OPC UA device | Follow the procedure described in section [Trusting OPC UA certificates](#trusting-opc-ua-certificates-rt-unified). |    | S7 controller | No action is necessary.  See section [Communication with S7-1500 and S7-1200](#communication-with-s7-1500-and-s7-1200-rt-unified). |       | Symbol | Meaning |    | --- | --- |    | **Note**  If the HMI device has multiple communication partners of the same certificate authority, install the root certificate on the HMI device once. |  | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

> **Note**
>
> Establishment of a trust relationship is not required to use Audit Trail on an HMI device.

---

**See also**

[Recreation of certificates (RT Unified)](#recreation-of-certificates-rt-unified)
  
[Trusting CA-based certificates (RT Unified)](#trusting-ca-based-certificates-rt-unified)

#### Continued use of CA-based certificates (RT Unified)

##### Introduction

If you are using security-related Unified components on the HMI devices of your system, you must provide the following certificates:

- Certificates used by the HMI devices to authenticate themselves to their communication partners (Unified certificates)
- Certificates used by the communication partners of the HMI devices to authenticate themselves to the HMI devices (third-party certificates)

Follow the procedure described in this section if you are already using CA-based Unified certificates and the infrastructure of your system changes, for example, because application certificates or HMI device had to be added or deleted or certificates had to be renewed.

You can find information on how to use general CA-based certificates in section [Using general certificates](#using-general-certificates-rt-unified).

> **Note**
>
> This description assumes that both the HMI devices and their communication partners are using CA-based application certificates.

> **Note**
>
> Some components require a mutual SSL authentication, meaning that both the HMI device and its communication partner need a certificate. They must trust each other's certificates.
>
> Other components require a one-way SSL authentication, meaning that only the HMI device needs a certificate and its communication partner must trust the certificate, or vice versa.
>
> See also section [Determining the required application certificates](#determining-the-required-application-certificates-rt-unified).

##### Requirement

- A certificate authority with the desired infrastructure has been created on the certificate authority device using WinCC Unified Certificate Manager.
- The required CA-based application certificates have been issued for the communication partners.

  To create these certificates, follow the procedure described in the user help of the respective communication partner.
- The root certificate and CRL file of the certificate authority that issued the application certificates of the communication partners have been exported as described in the user help of the respective communication partner. You have access to both files.
- For communication with an S7 controller:

  - The controller has the following firmware:

    S7-1500: Firmware 2.9 or higher

    S7-1200: Firmware 4.5 or higher
  - The HMI device has an integrated connection to the controller.
  - Secure communication was enabled for the controller in the Engineering System

##### Procedure

1. Start Certificate Manager on the certificate authority device.
2. Change the CA infrastructure as needed, for example, by adding or deleting devices and certificates.
3. Export the certificates of the HMI devices.
4. Import the certificates of the HMI device to each HMI device for which you made changes and install them there.
5. If you install the certificates of an HMI device at runtime, restart Runtime on the device.
6. Establish the trust relationship between the HMI devices and their communication partners for the newly added or renewed certificates.

**Note**

Existing connections are not interrupted by the installation of certificates. Runtime uses the old certificates until it is restarted.

A Runtime restart is not required for use of a newly installed web server certificate.

Follow the procedure described below.

> **Note**
>
> **Certificate authority device as HMI device**
>
> If you are using the certificate authority device as a Unified PC and you only want to provide the application certificates of this PC, the export and import steps are omitted. You can install the certificates of the PC without exporting and importing them beforehand.

##### Changing the CA infrastructure of the certificate authority

1. Change the infrastructure of the certificate authority as needed.

   You have the following options:

   - Add new devices and their application certificates.

     See sections [Adding devices](#adding-devices-rt-unified) and [Add application certificates](#add-application-certificates-rt-unified).
   - Edit the certificates of an existing device, for example, by adding a new application certificate or renewing or deleting an existing application certificate.

     See sections [Add application certificates](#add-application-certificates-rt-unified), [Deleting application certificates](#deleting-application-certificates-rt-unified) and [Recreating a certificate](#recreating-a-certificate-rt-unified).
   - Delete devices.

     See section [Deleting devices](#deleting-devices-rt-unified).
   - Renew the CRL file on expiration

     See section [Updating a CRL file](#updating-a-crl-file-rt-unified).
   - To renew an expiring root certificate, recreate the complete configuration of the certificate authority (root certificate, CRL file and certificates of all devices).

     See section [Recreating the entire configuration](#recreating-the-entire-configuration-rt-unified).
2. Optional: Back up the certificate authority.

##### Exporting certificates of HMI devices

Export the certificates of newly added or changed HMI devices. The export sets up their installation on the HMI device.

Follow these steps:

- For Unified PCs: Export the CA container once.

  The certificates of all devices of the certificate authority are exported to a common storage file.

  When the certificates are imported to a Unified PC, you see the certificates of all devices of the certificate authority. However, you can only install the certificates of the local device. The other devices are shown for information purposes only.

  > **Note**
  >
  > If a small storage file is needed to save memory space, you can also export the certificates of a single Unified PC. Then, all certificates of the selected PC are exported to the storage files.

  See section [Exporting certificates of a Unified PC](#exporting-certificates-of-a-unified-pc-rt-unified).
- For Unified Panels: Export the certificates of a single Unified Panel. All certificates of the selected Panel are exported to the storage files.

  Repeat this action for all Panels whose certificate configuration was changed.

  > **Note**
  >
  > A joint export of the certificates of all devices of the certificate authority is not possible.

  See section [Exporting certificates of a Panel](#exporting-certificates-of-a-panel-rt-unified).

##### Importing and installing certificates

Import the certificates to the HMI devices whose configuration you changed in Certificate Manager and install them there:

- For Unified PCs: See sections [Importing certificates of a Unified PC](#importing-certificates-of-a-unified-pc-rt-unified) and [Installing all certificates or single certificates of a PC](#installing-all-certificates-or-single-certificates-of-a-pc-rt-unified).
- For Unified Panels: See sections [Importing and installing certificates of a Panel](#importing-and-installing-certificates-of-a-panel-rt-unified) and [Manually importing and individual certificates to a Panel and installing them](#manually-importing-and-individual-certificates-to-a-panel-and-installing-them-rt-unified).

##### Establishing the trust relationship

You establish the trust relationship for the following:

- HMI devices you have newly added
- HMI devices for which you added a new certificate or renewed or deleted an existing certificate
- If you recreated the configuration of the certificate authority: all HMI devices

> **Note**
>
> If the following conditions are met, no further steps are needed to establish the trust relationship:
>
> - The HMI devices of the certificate authority communicate only with each other and with S7 controllers to which they have an integrated connection.
> - The certificates of the HMI devices have been installed on the devices.
> - The HMI devices communicate with each other exclusively using CA-based certificates of their common certificate authority.
> - For web server communication, you use only the following web clients:
>
>   - Edge and Chrome on Unified PCs that belong to the infrastructure of the certificate authority
>   - Web browser of Unified Panels that belong to the infrastructure of the certificate authority

Follow these steps:

| 1. (optional) Create a list of the communication partners of these HMI devices. 2. Export the Unified root certificate and the CRL file on the certificate authority device using Certificate Manager.    See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified).      | Symbol | Meaning |    | --- | --- |    | **Note**   **Alternative approach for Unified PCs**  If one of the HMI devices is a Unified PC whose certificates were already installed with Certificate Manager, you can also export both files on the Unified PC with SIMATIC Runtime Manager. See also section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified). |  | 3. Install the Unified root certificate on the communication partners of the HMI devices:       | Communication partner | Procedure on the communication partner |    | --- | --- |    | Web client | Follow the procedure described in section [Trusting the web server certificate](#trusting-the-web-server-certificate-rt-unified) for the respective web client. |    | OPC UA device | Follow the procedure described in the user help of the respective OPC UA communication partner. |    | Runtime Collaboration device | If the Collaboration devices have different Unified certificate authorities, install the root certificate and CRL file of one device on the other, and vice versa. For Panels, follow the procedure described in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified). For PCs, follow the procedure described in section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified). If the devices have the same Unified certificate authority, the devices trust each other automatically. |    | S7 controller | Not applicable |       | Symbol | Meaning |    | --- | --- |    | **Note**  If the same communication partner communicates with multiple HMI devices that have the same certificate authority, install the root certificate on the communication partner once. It is not necessary to manually install the root certificate in some following cases: You can find more information on this in the following sections: - [Automatic trust relationship with a PC web server](#automatic-trust-relationship-with-a-pc-web-server-rt-unified) - [Automatic trust relationship with a Panel web server](#automatic-trust-relationship-with-a-panel-web-server-rt-unified) - [Automatic trust relationship in OPC UA communication](#automatic-trust-relationship-in-opc-ua-communication-rt-unified) - [Automatic trust relationship between Collaboration devices](#automatic-trust-relationship-between-collaboration-devices-rt-unified)Where appropriate, check whether the root certificate has already been installed on the communication partner: - Web client as communication partner: See section [Checking the status of the web server root certificate on the web client.](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified). - Runtime Collaboration communication partner: See section [Checking the status of a root certificate on the HMI device](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified). - Remaining communication partners: Follow the procedure described in the user help of the respective communication partner. |  | 4. Install the root certificates of the communication partners on each HMI device:       | Communication partner | Procedure on the HMI device |    | --- | --- |    | Web client | Not applicable |    | Runtime Collaboration device | If the Collaboration devices have different Unified certificate authorities, install the root certificate and CRL file of one device on the other, and vice versa. For Panels, follow the procedure described in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified). For PCs, follow the procedure described in section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified). If the devices have the same Unified certificate authority, the devices trust each other automatically. |    | OPC UA device | Follow the procedure described in section [Trusting OPC UA certificates](#trusting-opc-ua-certificates-rt-unified). |    | S7 controller | No action is necessary.  See section [Communication with S7-1500 and S7-1200](#communication-with-s7-1500-and-s7-1200-rt-unified). |       | Symbol | Meaning |    | --- | --- |    | **Note**  If the HMI device has multiple communication partners of the same certificate authority, install the root certificate on the HMI device once. |  | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

> **Note**
>
> Establishment of a trust relationship is not required to use Audit Trail on an HMI device.

---

**See also**

[Create backup (RT Unified)](#create-backup-rt-unified)
  
[Trusting CA-based certificates (RT Unified)](#trusting-ca-based-certificates-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)

### Creating and exporting the CA infrastructure (RT Unified)

This section contains information on the following topics:

- [Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)
- [Adding devices (RT Unified)](#adding-devices-rt-unified)
- [Deleting devices (RT Unified)](#deleting-devices-rt-unified)
- [Add application certificates (RT Unified)](#add-application-certificates-rt-unified)
- [Deleting application certificates (RT Unified)](#deleting-application-certificates-rt-unified)
- [Export options (RT Unified)](#export-options-rt-unified)
- [Exporting certificates of a Unified PC (RT Unified)](#exporting-certificates-of-a-unified-pc-rt-unified)
- [Exporting certificates of a Panel (RT Unified)](#exporting-certificates-of-a-panel-rt-unified)
- [Exporting root certificate and CRL file (RT Unified)](#exporting-root-certificate-and-crl-file-rt-unified)
- [Exporting a single application certificate (RT Unified)](#exporting-a-single-application-certificate-rt-unified)
- [Recreation of certificates (RT Unified)](#recreation-of-certificates-rt-unified)
- [Recreating a certificate (RT Unified)](#recreating-a-certificate-rt-unified)
- [Recreating the entire configuration (RT Unified)](#recreating-the-entire-configuration-rt-unified)
- [Updating a CRL file (RT Unified)](#updating-a-crl-file-rt-unified)
- [Create backup (RT Unified)](#create-backup-rt-unified)
- [Password requirements (RT Unified)](#password-requirements-rt-unified)

#### Creating a certificate authority and root certificate (RT Unified)

Normally, you issue the CA-based certificates of the HMI devices of a system or subsystem with the same Unified certificate authority.

> **Note**
>
> Use of an external certificate authority is not possible. The Unified certificate authority and its certificates must be created with WinCC Unified Certificate Manager.

##### Requirement

A certificate authority has not yet been created on the certificate authority device with Certificate Manager.

##### Procedure

1. Decide which Unified PC in your network is to be the certificate authority device.
2. Open WinCC Unified Certificate Manager on this device.
3. Select the "CA configuration" tab.
4. In the work area, double-click "Create new certificate authority".
5. Enter the properties of the root certificate in the "New certificate authority" dialog.

   - "General" tab

     The general properties of the new certificate authority, e.g. name, name of organization

     Mandatory field: "Name"
   - "Security" tab

     Security-related properties of the new certificate authority, such as key size and lifetime.

     If necessary, select a different key size and lifetime for the certificate.

     Mandatory fields: Password fields for the private key
6. Click "Create".

##### Result

- The private key is generated.
- The root certificate is generated.
- An empty CRL (Certificate Revocation List) file is generated.
- In the "CA configuration" tab, a node for the root certificate is created and below it one for the CRL file.

> **Note**
>
> The private key is only available on the certificate authority device. The certificate authority uses it to sign the application certificates of the Unified devices. It is not visible in the user interface of Certificate Manager.

##### Next steps

- Create the CA infrastructure. To do this, add the Unified devices to the certificate authority and create their application certificates.

  > **Note**
  >
  > If there are changes to the infrastructure of your system later, such as addition of HMI devices, adapt the infrastructure of the certificate authority as needed.
- To distribute the Unified root certificate and its CRL file without distributing the certificates of the devices, for example, to external communication partners, export them individually.

##### Deleting certificate authority and root certificate

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Data loss prevention**  Delete the certificate authority and root certificate only in the following cases:  - After you have saved the data of the certificate authority. - When you no longer need the certificate authority and its data. |  |

**Procedure**

1. Open Certificate Manager on the certificate authority device.
2. Select the "CA configuration" tab.
3. Click the root certificate on the left and select "Delete".

**Result**

The certificate authority and all its data are deleted from the certificate authority device.

> **Note**
>
> If the certificates were already installed on the HMI devices, they are still installed there. Delete them from the devices if necessary.

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)
  
[Password requirements (RT Unified)](#password-requirements-rt-unified-1)
  
[Adding devices (RT Unified)](#adding-devices-rt-unified)
  
[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)
  
[Exporting root certificate and CRL file (RT Unified)](#exporting-root-certificate-and-crl-file-rt-unified)

#### Adding devices (RT Unified)

##### Requirement

A certificate authority has been created on the certificate authority device in WinCC Unified Certificate Manager.

##### Procedure

| 1. On the certificate authority device, open Certificate Manager. 2. Select the "CA configuration" tab.    You see the root certificate and its CRL file, as well as all the devices that have already been added and their application certificates. 3. Right-click the root certificate and select "Add device ...". 4. In the "New device" dialog, enter the device name, the IP address of the device, or both.    For devices in a domain, enter the fully qualified domain name (FQDN) or IP address of the device, or both.    The application certificates of the device are bound to the device using the information.     You can no longer change your entries afterward.      |  |  |  |    | --- | --- | --- |    | **Note**   **Recommendation**  Enter the device name/FQDN and IP address. For devices with dynamic IP addresses, use the FQDN. |  |  |     |  |  |  |    | --- | --- | --- |    | **Note**   **Allowed device names**  The use of the name "localhost" is not allowed and will be automatically replaced by Certificate Manager with the device name of the local device. |  |  |       | Specific characteristics | Mandatory information | Optional additional information (recommended) |    | --- | --- | --- |    | The HMI device operates as a web server, and the identity provider and Unified Runtime website are addressed using the IP address. | IP address If the IP address is missing, a validation error occurs when accessing the Runtime web page. | Device name or FQDN |    | HMI device operates as an OPC UA server (OPC UA server certificate, OPC UA exporter certificate) | Device name or  FQDN | IP address | |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

A node for the device is generated in the "CA configuration" tab.

Icons of the device nodes:

| Symbol | Meaning |
| --- | --- |
| ![Result](images/151497477003_DV_resource.Stream@PNG-de-DE.png) | The local machine (if added) |
| ![Result](images/151517914379_DV_resource.Stream@PNG-de-DE.png) | Other devices |

##### Next step

Create the application certificates of the added device.

##### Changing the device binding of the certificates

When adding a device, you define how the application certificates are bound to the device. To change your definition, follow these steps:

1. Delete the HMI device from the certificate authority.
2. Add the HMI device again, this time using the desired definition.
3. Add the needed application certificates to the HMI device.
4. Export the certificates of the HMI device.
5. Install the certificates on the HMI device.
6. Uninstall the certificates with the outdated device binding:

   - On a Unified PC: See section [Managing own certificates of a Unified PC](#managing-own-certificates-of-a-unified-pc-rt-unified).
   - On a Unified Panel: See section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified).

##### Handling a device after a change of IP address or computer name

If the IP address or computer name of a device added in Certificate Manager was changed subsequently, follow these steps:

1. Delete the device from the certificate authority.
2. Create it again, this time with the new IP address and/or new computer name.
3. Add the needed application certificates to the HMI device.
4. Export the certificates of the HMI device.
5. Install the certificates on the HMI device.
6. Uninstall the certificates with the outdated device binding:

   - On a Unified PC: See section [Managing own certificates of a Unified PC](#managing-own-certificates-of-a-unified-pc-rt-unified).
   - On a Unified Panel: See section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified).

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)
  
[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)
  
[Deleting devices (RT Unified)](#deleting-devices-rt-unified)
  
[Device binding of a certificate (RT Unified)](#device-binding-of-a-certificate-rt-unified)

#### Deleting devices (RT Unified)

##### Requirement

A device has been added to the certificate authority.

##### Procedure

1. Right-click on the device.
2. Select "Delete".
3. Confirm your selection.

##### Result

The device and its application certificates are deleted from the certificate authority.

> **Note**
>
> The certificates installed on the HMI device are not deleted. If necessary, delete the certificates from the device, as well:
>
> - On a Unified PC: See section [Managing own certificates of a Unified PC](#managing-own-certificates-of-a-unified-pc-rt-unified).
> - On a Unified Panel: See section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified).

---

**See also**

[Adding devices (RT Unified)](#adding-devices-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Add application certificates (RT Unified)

This section describes how to add application certificates to HMI devices. For information on adding general certificates, see section [Using general certificates](#using-general-certificates-rt-unified).

##### Requirement

An HMI device has been added to the certificate authority in Certificate Manager.

##### Procedure

1. On the certificate authority device, open Certificate Manager.
2. Select the "CA configuration" tab.
3. Right-click on the device and select "Add Certificate &gt; &lt;Certificate type&gt; ... "
4. Enter the properties of the certificate in the "New certificate" dialog.

   - "General" tab

     The general properties of the new certificate, e.g. name of organization

     Mandatory field for the "Web server" certificate: "Name" field
   - "Security" tab

     Security-related properties of the new certificate, e.g. key length and lifetime.

     If necessary, select a different key size and lifetime for the certificate.

   Some fields are write-protected. The properties you can edit on the tabs depend on the certificate type.
5. Click "OK".
6. Repeat steps 3 through 5 until the device has the needed application certificates.

**Note**

Use the "Fully qualified domain name" as name for web server certificates.

**Note**

**Runtime**

For web server certificates, the runtime is limited to a maximum of 27 months. Longer runtimes are not accepted by some browsers.

##### Result

The application certificates of the device have been configured.

##### Next step

Export the certificates.

> **Note**
>
> If you are using the certificate authority device as a Unified PC and you only want to provide the application certificates of this PC, the export and import steps are omitted. You can install the certificates of the PC without exporting and importing them beforehand.

##### Other options

You can create a new application certificate, for example, because it has reached the end of its lifetime.

You can export an application certificate as a public certificate.

You can export the root certificate to distribute it to the communication partners.

---

**See also**

[Deleting application certificates (RT Unified)](#deleting-application-certificates-rt-unified)
  
[Recreating a certificate (RT Unified)](#recreating-a-certificate-rt-unified)
  
[Exporting an application certificate as a public certificate (RT Unified)](#exporting-an-application-certificate-as-a-public-certificate-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Deleting application certificates (RT Unified)

##### Requirement

The certificate authority has a device with an application certificate.

##### Procedure

1. On the certificate authority device, open Certificate Manager.
2. Select the "CA configuration" tab.
3. Right-click on the application certificate under the desired device.
4. Select "Delete".
5. Confirm your selection.

##### Deleting the application certificate

The application certificate is deleted.

> **Note**
>
> The certificates installed on the device are not deleted.
>
> If necessary, delete the certificate from the device. On a Unified PC, you use Certificate Manager to do this. On a Unified Panel, you use the "Security &gt; Certificates" function in the Control Panel.

---

**See also**

[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)
  
[Managing own certificates of a Unified PC (RT Unified)](#managing-own-certificates-of-a-unified-pc-rt-unified)
  
[Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)

#### Export options (RT Unified)

##### Overview

The following table provides an overview of which export options WinCC Unified Certificate Manager offers and how to use them:

| Option | Use | Available on the certificate authority device | Available on a Unified PC target device |
| --- | --- | --- | --- |
| Export the CA container | To provide the certificates of one or more Unified PCs | ✓ | - |
| Export the certificates of a device | To provide the certificates of a single Unified Panel  Can also be used to provide the certificates of a single Unified PC. | ✓ | - |
| Export a single application certificate | To provide it as a public certificate | ✓ | ✓ |
| Export the root certificate and CRL file | To establish the trust relationship between a Unified device and its communication partners  To provide an updated CRL file | ✓ | - |
| Export the complete configuration of the certificate authority | To back up data of the certificate authority | ✓ | - |

##### Exporting a general certificate

The following table provides an overview of the export options offered by WinCC Unified Certificate Manager and how to use them:

| Option | Use | Available on the certificate authority device | Available on a Unified PC (PC as communication partner) |
| --- | --- | --- | --- |
| Export the public key | To provide it as a public certificate | ✓ | ✓ |
| Export the private key and public key | As preparation for installing the general certificate on the device for which the certificate was issued | ✓ | - |

#### Exporting certificates of a Unified PC (RT Unified)

##### Introduction

This step sets up the import and installation of application certificates of the Unified PC on the PC as well as the root certificate of the issuing certificate authority and its CRL file.

> **Note**
>
> General certificates are exported and imported and installed separately. See section [Using general certificates](#using-general-certificates-rt-unified).

##### Use cases

You export certificates in the following cases:

- After adding the device and configuring its application certificates for the first time
- When you change the certificates configured for the PC on the certificate authority device after the certificates were installed on the PC, for example, by adding, deleting or recreating application certificates
- ​After recreation of the complete configuration of the certificate authority (for example, due to expiration of the root certificate)
- ​After updating the CRL file

  > **Note**
  >
  > If you only want to update the CRL file, an export is not mandatory. You can also export the CRL file individually and import it to the PC using SIMATIC Runtime Manager.
  >
  > See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified) and section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

> **Note**
>
> If you are using the certificate authority device as a Unified PC and you only want to provide the application certificates of this PC, the export and import steps are omitted. You can install the certificates of the PC without exporting and importing them beforehand.

##### Export options

You have the following options:

- Export CA container

  The certificates of all devices of the certificate authority are written to a common export file.
- Export device

  The export file contains only the certificates of the selected Unified PC.

In both cases, you can only install the certificates of this PC on the Unified PC.

| Symbol | Meaning |
| --- | --- |
| ![Export options](images/137753016459_DV_resource.Stream@PNG-de-DE.png) | **Tip for an efficient procedure** |
| Recommended procedure:  - If you have changed the certificates of multiple devices, export the CA container. - If you have changed the certificates of a single Unified PC, export the certificates of this device. |  |

##### Requirement

The certificates of the Unified PC have been configured on the certificate authority device.

##### Procedure

1. On the certificate authority device, open Certificate Manager.
2. Select the "CA configuration" tab.
3. Follow these steps:

   To export the certificates of all devices:

   - Right-click on the root certificate.
   - Select "Export &gt; CA Container".

   To export only the certificates of the Unified PC:

   - Right-click on the Unified PC.
   - Select "Export device &gt; To PC".
4. In the dialog that opens, enter and repeat a password to protect the export file.

   See also section [Password requirements](#password-requirements-rt-unified-1).
5. Click "Export".
6. Click on "Save" and select the storage location and the file name.

##### Result

The root certificate, CRL file and certificates of the Unified PC or all devices are stored encrypted with the specified password in a secure storage file.

##### Next step

Import the certificates of the PC to the PC and install them.

---

**See also**

[Importing certificates of a Unified PC (RT Unified)](#importing-certificates-of-a-unified-pc-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Exporting certificates of a Panel (RT Unified)

##### Introduction

This step sets up the import and installation of application certificates of the Unified Panel on the Panel as well as the root certificate of the issuing certificate authority and its CRL file.

> **Note**
>
> General certificates are exported and imported and installed separately. See section [Using general certificates](#using-general-certificates-rt-unified).

##### Use cases

You export certificates in the following cases:

- After adding the device and configuring its application certificates for the first time
- When you change the certificates configured for the Panel on the certificate authority device after the certificates were installed on the Panel, for example, by adding, deleting or creating new application certificates
- After recreation of the complete configuration of the certificate authority (for example, due to expiration of the root certificate)
- After updating the CRL file

  > **Note**
  >
  > Alternatively, you can also export the CRL file individually. See section [Exporting root certificate and CRL file](#exporting-root-certificate-and-crl-file-rt-unified). Then import it using the "Security &gt; Certificates" function in the Control Panel of the Unified Panel.

##### Requirement

The certificates of the Panel have been configured on the certificate authority device.

##### Procedure

1. Open WinCC Unified Certificate Manager on the certificate authority device.
2. Select the "CA configuration" tab.
3. Right-click on the desired Panel.
4. Select "Export device &gt; To Panel".
5. In the dialog that opens, enter and repeat a password to protect the export file.

   See also section [Password requirements](#password-requirements-rt-unified-1).
6. (Optional) Adjust the number of iterations for the encryption.
7. Click "Export".
8. Select the file path and file name and click "Save".

   The data is stored in a TAR log and encrypted with the password.
9. Copy the TAR log to an external storage medium.

**Note**

Do not use spaces or special characters, such as "/", that the Panel might interpret as a command during the import.

##### Next step

Import the certificates to the device and install them.

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)
  
[Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)

#### Exporting root certificate and CRL file (RT Unified)

##### Introduction

You can export and distribute the root certificate and CRL file separately from the certificates of devices as a public certificate with Certificate Manager. This is necessary in the following cases, for example:

- To establish the trust relationship between an HMI device and its communication partners
- To update an expired CRL file

You can select between the following options:

- Exporting root certificate and CRL file
- Exporting CRL file only

> **Note**
>
> **Alternative approach for Unified PCs**
>
> If the HMI device is a PC on which the root certificate and its CRL file are already installed, you can also export both files with SIMATIC Runtime Manager.
>
> See also section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

##### Requirement

A certificate authority has been created on the certificate authority device in Certificate Manager.

##### Exporting root certificate and CRL file

1. On the certificate authority device, open Certificate Manager.
2. In the "CA configuration" tab, click the root certificate on the right.
3. Select "Export &gt; CA Certificate ...".
4. Select a file format.
5. Confirm your entries.
6. Select a target folder.
7. Confirm your entries.

The root certificate and its CRL file are exported to the target folder, each to a separate file.

##### Export CRL file only

1. On the certificate authority device, open Certificate Manager.
2. Select the "CA configuration" tab.
3. Under the root certificate, right-click the Certificate Revocation list.
4. Select "Export".
5. Select a file format.
6. Confirm your entries.
7. Select a target folder.
8. Confirm your entries.

The CRL file is exported to the target folder.

##### Distribute files

After the export, distribute the files to the target devices:

- For distribution to communication partners, follow the procedure described in the user help of the device.
- On a Unified PC you install the files with SIMATIC Runtime Manager.
- On a Unified Panel you install the files in the Control Panel under "Security &gt; Certificates" using the "Import" function.

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Exporting a single application certificate (RT Unified)

With WinCC Unified Certificate Manager, you can export application certificates individually as public certificates.

##### Requirement

An application certificate has been added to a device in WinCC Unified Certificate Manager.

##### Exporting certificate to the certificate authority device

1. On the certificate authority device, open Certificate Manager.
2. Select the "CA configuration" tab.
3. Right-click on the application certificate under the device.
4. Select "Export certificate...".
5. Select a file format.
6. Confirm your entries.
7. Select a target folder.
8. Confirm your entries.

##### Export certificate on the device

**Additional requirements**

- The device is a unified PC.
- The application certificate has been installed on the device.

**Procedure**

1. On the Unified PC, open Certificate Manager.
2. Select the "Installed certificates" tab.
3. Right-click on the application certificate.
4. Select "Export certificate...".
5. Select a file format.
6. Confirm your entries.
7. Select a target folder.
8. Confirm your entries.

##### Result

The public key of the certificate is exported. Distribute it to the external communication partners of the device.

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Recreation of certificates (RT Unified)

Certificate Manager offers the option to recreate existing certificates.

You must recreate certificates in the following cases:

| Symbol | Meaning |
| --- | --- |
| Expiration of an application certificate or a general certificate | Recreate the certificate. |
| Expiry of the root certificate | Recreate the entire configuration of the certificate authority. |
| Expiry of the CRL file | Update the CRL file. |
| Change to the IP address or the computer name of a Unified device<sup>1</sup> | Recreate the application certificates and general certificates of the device. |
| <sup>1</sup> For a Unified PC that is used as an HMI device as well as a certificate authority device: If you have changed the computer name or the IP address, recreate the entire configuration of the certificate authority. Distribute and install it. When the certificate authority device is not used as an HMI device, there is no need to renew the certificate configuration. |  |

---

**See also**

[Recreating a certificate (RT Unified)](#recreating-a-certificate-rt-unified)
  
[Recreating the entire configuration (RT Unified)](#recreating-the-entire-configuration-rt-unified)
  
[Updating a CRL file (RT Unified)](#updating-a-crl-file-rt-unified)

#### Recreating a certificate (RT Unified)

You recreate application certificates and general certificates in the following cases:

- The lifetime of a certificate has expired.
- Entries for a valid certificate are to be edited, for example to correct entries.
- The IP address or computer name of the device has been changed.

##### Procedure

1. Open WinCC Unified Certificate Manager on the certificate authority device.
2. Select the "CA configuration" tab.
3. Right-click on the certificate of the desired device and select "Recreate ...".

   The "New &lt;description&gt; certificate" dialog opens. The entries of the old certificate are downloaded into the dialog.
4. Change the desired properties.
5. Click "OK".

##### Result

A new certificate is created. Export the certificates of the device and install the certificate on the device.

---

**See also**

[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)
  
[Recreation of certificates (RT Unified)](#recreation-of-certificates-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)
  
[Exporting certificates of a Unified PC (RT Unified)](#exporting-certificates-of-a-unified-pc-rt-unified)
  
[Exporting certificates of a Panel (RT Unified)](#exporting-certificates-of-a-panel-rt-unified)
  
[Using general certificates (RT Unified)](#using-general-certificates-rt-unified)

#### Recreating the entire configuration (RT Unified)

The expiration of the root certificate requires that the entire configuration of the certificate authority is created again.

##### Requirement

A certificate authority has been created and configured on the certificate authority device in Certificate Manager.

##### Procedure

1. On the certificate authority device, open Certificate Manager.
2. Select the "CA configuration" tab.

   You will see the configuration of the certificate authority.
3. Right-click the root certificate and select "Recreate all".
4. The "Recreate certificate authority" dialog opens.

   The properties of the previous certificate authority are taken over as default. Change them if necessary.
5. Enter the same password as when you created the certificate authority and confirm it.
6. Click "Create".

##### Result

The configuration of the certificate authority is recreated:

- Private key
- Root certificate
- CRL file
- All devices and their certificates

##### Next steps

- Export the certificates of the devices. Import and install them on the devices.
- Distribute the root certificate and CRL file to the communication partners of the devices.

---

**See also**

[Recreation of certificates (RT Unified)](#recreation-of-certificates-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Updating a CRL file (RT Unified)

When the root certificate is created, the CRL file is given a lifetime of 24 months. When the lifetime expires, it is necessary to update the CRL file.

##### Requirement

A certificate authority has been created on the certificate authority device in Certificate Manager.

##### Procedure

1. On the certificate authority device, open Certificate Manager.
2. Select the "CA configuration" tab.
3. Under the root certificate, click the "Certificate Revocation List" node on the right.
4. Select "Update".

##### Result

A new CRL file with a lifetime of 24 months is created.

##### Next step

Distribute and install the CRL file to the target devices:

- On a Unified PC, you install the file with SIMATIC Runtime Manager. See section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).
- On a Unified Panel, you install the file in the Control Panel under "Security &gt; Security" using the "Import" function. See section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified).
- For distribution to the communication partners, follow the procedure described in the user help of the device.

---

**See also**

[Recreation of certificates (RT Unified)](#recreation-of-certificates-rt-unified)
  
[Exporting root certificate and CRL file (RT Unified)](#exporting-root-certificate-and-crl-file-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Create backup (RT Unified)

##### Procedure

To create a backup copy of all the data of the certificate authority, follow these steps:

1. Open Certificate Manager on the certificate authority device.
2. Select the "CA configuration" tab.
3. Right-click the root certificate and select "Export &gt; Full backup".
4. To protect the backup file, enter a password and repeat it in the "Export" dialog.

   See also section [Password requirements](#password-requirements-rt-unified).
5. Click "Export".
6. Select a storage location and file name and click "Export".

##### Result

The entire configuration of the certificate authority is written to a backup file.

##### Loading the backup

1. Open Certificate Manager.
2. In the "CA configuration" tab, double-click the "Open configuration ..." entry.
3. Select the backup file and confirm with "Open".
4. Enter the password set when creating the backup and confirm with "Open".

---

**See also**

[Recreation of certificates (RT Unified)](#recreation-of-certificates-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Password requirements (RT Unified)

The passwords defined in the Certificate Manager must meet the following requirements:

- Length: At least 8 characters
- In each case at least one uppercase letter, one lowercase letter, one number and one special character

### Importing and installing certificates of a Unified PC (RT Unified)

This section contains information on the following topics:

- [Importing certificates of a Unified PC (RT Unified)](#importing-certificates-of-a-unified-pc-rt-unified)
- [Installing all certificates or single certificates of a PC (RT Unified)](#installing-all-certificates-or-single-certificates-of-a-pc-rt-unified)

#### Importing certificates of a Unified PC (RT Unified)

##### Introduction

The import sets up the installation of CA-based own application certificates on the Unified PC as well as the root certificate of the issuing certificate authority and its CRL file.

> **Note**
>
> General certificates are exported and imported and installed separately. See section [Using general certificates](#using-general-certificates-rt-unified).

> **Note**
>
> If you are using the certificate authority device as a Unified PC and you only want to provide the application certificates of this PC, no import is necessary. You can install the certificates of the PC without exporting and importing them beforehand.

##### Requirement

- The CA container or the certificates of the Unified PC have been exported on the certificate authority device.
- The PC has access to the storage location of the export file.

##### Procedure

1. Open WinCC Unified Certificate Manager on the PC.
2. Select the "CA configuration" tab.
3. Double-click "Open configuration ...".
4. Select the export file.
5. Enter the password selected during export.
6. Confirm your entries.

##### Result

The configuration file is loaded to the "CA configuration" tab. What you see on the tab after loading depends on the selected export option:

- CA container exported:

  You see the complete infrastructure of the certificate authority, except for the private key.

  You can only install the application certificates of the local device. The other devices and their certificates and the general certificates are shown for information purposes only.
- Certificates of the device exported:

  You see the root certificate and its CRL file, as well as the certificates of the local device.

  The general certificates of the device are shown for information purposes only. You cannot install these certificates.

Exiting Certificate Manager closes the loaded configuration.

##### Next step

Install the certificates on the device.

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

#### Installing all certificates or single certificates of a PC (RT Unified)

You can choose between the following:

- Install all certificates of the Unified PC as well as the root certificate and CRL file.

  > **Note**
  >
  > General certificates are exported and imported and installed separately. See section [Using general certificates](#using-general-certificates-rt-unified).
  >
  > On Unified PCs, you also see the general certificates in WinCC Unified Certificate Manager after importing a configuration file. This is for information purposes only. You cannot install the general certificates with Certificate Manager.
- Install a single application certificate.

  Root certificate and CRL file are automatically also installed.

##### Requirement

- Certificate Manager is open on the PC on which you want to install the certificates.
- The certificates of the PC have been imported to the device using Certificate Manager.

##### Procedure

1. Select the "CA configuration" tab.
2. Select one of the following options:

   To install all certificates of the PC:

   - Right-click the node of the local machine.

     The local machine has the following icon: ![Procedure](images/151497477003_DV_resource.Stream@PNG-de-DE.png)
   - Select "Install all certificates".

   To install a single application certificate:

   - Under the local machine node, right-click the certificate.
   - Select "Install".

##### Result

Depending on your choice, either the root certificate and CRL file as well as all application certificates are installed or only the selected application certificate is installed:

- The application certificates are installed in the certificate stores defined for the respective application, in the folder containing own certificates.

  > **Note**
  >
  > The web server certificate is automatically bound to the Runtime web page by the installation. It replaces the web server certificate selected during Runtime installation or later in the "Website settings" step in the "WinCC Unified Configuration" tool. The web page will then be restarted to enforce the use of the new certificate. Any connected web browsers will be disconnected as a result and will have to log in again.
  >
  > The following certificates only become effective after a restart of the WinCC Unified Runtime:
  >
  > - OPC UA server certificate
  > - Runtime Collaboration certificate
  > - Audit Trail system certificate
- The root certificate and its CRL file are installed in the certificate stores, in the folders containing the trusted certificate authorities.

If the trust relationship between the PC and its communication partners has already been established, the PC can successfully communicate with its communication partners.

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)
  
[Managing own certificates of a Unified PC (RT Unified)](#managing-own-certificates-of-a-unified-pc-rt-unified)

### Importing and installing certificates of a Unified Panel (RT Unified)

This section contains information on the following topics:

- [Importing and installing certificates of a Panel (RT Unified)](#importing-and-installing-certificates-of-a-panel-rt-unified)
- [Manually importing and individual certificates to a Panel and installing them (RT Unified)](#manually-importing-and-individual-certificates-to-a-panel-and-installing-them-rt-unified)

#### Importing and installing certificates of a Panel (RT Unified)

> **Note**
>
> You always import all application certificates of the Unified Panel. These certificates as well as the root certificate of the issuing certificate authority and its CRL file are installed on the Panel by the import.

> **Note**
>
> General certificates are exported and imported and installed separately. See section [Using general certificates](#using-general-certificates-rt-unified).

##### Requirement

- The certificates of the Panel have been exported on the certificate authority device with "Export device &gt; To Panel".

  See section [Exporting certificates of a Panel](#exporting-certificates-of-a-panel-rt-unified).
- The export file was copied to an external storage medium.
- The file name contains no spaces or special characters, such as "/", that the Panel might interpret as a command during the import.

##### Procedure

1. Connect the panel to the external storage medium.
2. In the Control Panel, select "Security &gt; Certificates".
3. Click "Import".

   The "Import certificates" dialog opens.
4. Select the storage medium and the export file containing the certificates.
5. Enter the password that was used to encrypt the file during export.
6. Enter the iteration that was specified when the certificate was created.
7. Click "Import".

##### Result

The certificates are imported and installed:

- The application certificates are installed in the own certificates of the Panel.

  To display them, select the entry "My Certificates" as the "Certificate store".

  > **Note**
  >
  > The web server certificate is automatically bound to the Runtime web page by the installation. The web page is then restarted to enforce the use of the new certificate. Any connected web browsers are thereby disconnected and must log in again.
  >
  > The following certificates only become effective after a restart of WinCC Unified Runtime:
  >
  > - OPC UA server certificate
  > - Runtime Collaboration certificate
  > - Audit Trail system certificate
- The root certificate and its CRL file are installed in the trusted certificate authorities of the Panel.

  To display them, select the entry "Certificate Authorities" in "Certificate Store".

> **Note**
>
> **Manual importing and installing**
>
> Alternatively, you can import the certificates to the Panel manually and install them. See section [Manually importing and individual certificates to a Panel and installing them](#manually-importing-and-individual-certificates-to-a-panel-and-installing-them-rt-unified).

---

**See also**

[Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)

#### Manually importing and individual certificates to a Panel and installing them (RT Unified)

You can also import and install the application certificates of a Unified Panel manually instead of using the Control Panel of the device.

##### Requirement

- The certificates of the Unified Panel have been exported with "Export device &gt; To Panel".

  See section [Exporting certificates of a Panel](#exporting-certificates-of-a-panel-rt-unified).
- The export file was copied to an external storage medium.

##### Procedure

1. Decrypt the export file using OpenSSL.

   `openssl enc -d -aes256 -salt -iter <25000> -in <exportfilename> -out <tarfilename.tar> -k <password>`

   The value for the parameter `-iter` must match the iteration count specified during export.

   The decrypted TAR log contains the configured certificates in the respective application-specific folder structure.
2. Copy the file to the Panel device.
3. Manually distribute the certificates to the specific repositories of the respective application.

### Trusting CA-based certificates (RT Unified)

This section contains information on the following topics:

- [Trusting the web server certificate (RT Unified)](#trusting-the-web-server-certificate-rt-unified)
- [Trusting Collaboration certificates (RT Unified)](#trusting-collaboration-certificates-rt-unified)
- [Trusting OPC UA certificates (RT Unified)](#trusting-opc-ua-certificates-rt-unified)
- [Checking the status of a root certificate on the HMI device (RT Unified)](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified)
- [Importing and installing root certificates and CRL files on Panels (RT Unified)](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified)

#### Trusting the web server certificate (RT Unified)

You can find information on how to trust a CA-based web server certificate on a web client here:

- Unified Panel as web server: See section [Establishing the trust relationship with the web server](#establishing-the-trust-relationship-with-the-web-server-rt-unified).
- Unified PC as web server: See section [Establishing the trust relationship with the web server](#establishing-the-trust-relationship-with-the-web-server-rt-unified-1).

#### Trusting Collaboration certificates (RT Unified)

You can find information on how to trust the Collaboration certificate of a Collaboration partner on a Collaboration Panel in section [Establishing the trust relationship (Collaboration for Panels)](#establishing-the-trust-relationship-collaboration-for-panels-rt-unified).

You can find information on how to trust the Collaboration certificate of a Collaboration partner on a Collaboration PC in section [Establishing the trust relationship (Collaboration for PCs)](#establishing-the-trust-relationship-collaboration-for-pcs-rt-unified).

#### Trusting OPC UA certificates (RT Unified)

You can find information on how to establish the trust relationship between a Unified Panel and its OPC UA communication partner on a Unified Panel that is used as an OPC UA server or OPC UA client in section [Establishing the trust relationship (OPC UA for Panel)](#establishing-the-trust-relationship-opc-ua-for-panel-rt-unified).

You can find information on how to establish the trust relationship between a Unified PC and its OPC UA communication partner on a Unified PC that is used as an OPC UA server or OPC UA client in section [Establishing the trust relationship (OPC UA for PC)](#establishing-the-trust-relationship-opc-ua-for-pc-rt-unified).

#### Checking the status of a root certificate on the HMI device (RT Unified)

##### Introduction

This section describes how to check whether an HMI device already trusts the root certificate of a communication partner.

In that case, the root certificate has been installed in the certificate store of the HMI device, in the folder containing the trusted certificate authorities.

##### Procedure on a Unified PC

| Symbol | Meaning |
| --- | --- |
| 1. Start the SIMATIC Runtime Manager application on the PC. 2. Click the ![Procedure on a Unified PC](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar. 3. ​Select the "Certificates" tab. 4. Check under ② and ③ to see if the desired root certificate is included in the list of root certificates and third-party certificates installed on the device and whether the device trusts the certificate:               ![Procedure on a Unified PC](images/153675591179_DV_resource.Stream@PNG-en-US.png)         ![Procedure on a Unified PC](images/153675591179_DV_resource.Stream@PNG-en-US.png)        | Symbol | Meaning |    | --- | --- |    | ① | Button for importing a certificate or CRL file You trust a certificate by importing it. You can later reject the certificate and trust it again. |    | ② | List of third-party certificates: - Root certificates - Application certificates that are self-signed or issued by a certification authority - General certificates |    | ③ | Shows whether the HMI device trusts a certificate |    | ④ | List of CRL files | |  |

You can find information on how to trust a root certificate or how to import and trust one in section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

##### Procedure on a Unified Panel

1. In the Control Panel, select "Security" &gt; "Certificates".
2. In the "Certificate stores" list, select the entry "Certificate Authorities".

   ![Procedure on a Unified Panel](images/162709734795_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure on a Unified Panel](images/162709734795_DV_resource.Stream@PNG-de-DE.png)
3. Check whether the desired root certificate is included in the list of trusted root certificates installed on the device.

You can find information on how to trust a root certificate or how to import and trust one in section [Importing and installing root certificates and CRL files on Panels](#importing-and-installing-root-certificates-and-crl-files-on-panels-rt-unified).

---

**See also**

[Checking the status of the web server root certificate on the web client. (RT Unified)](#checking-the-status-of-the-web-server-root-certificate-on-the-web-client-rt-unified-1)

#### Importing and installing root certificates and CRL files on Panels (RT Unified)

This section describes how to import a root certificate and its CRL file to a Unified Panel. The root certificate and CRL file are installed in the folder containing trusted certificate authorities by the import. The Panel trusts the root certificate and automatically trusts all certificates that were issued by the certificate authority of the root certificate.

The import is required in the following cases:

- To establish the trust relationship between the Panel and a communication partner whose application certificate was issued by a certificate authority.
- When the CRL file of an installed root certificate has been updated.

> **Note**
>
> If the Panel has a CA-based own certificate and its root certificate changes, it is not sufficient to import the new root certificate. You must recreate the complete configuration on the certificate authority device and import and install the certificates of the Panel on the Panel. See section [Recreating the entire configuration](#recreating-the-entire-configuration-rt-unified).

##### Requirement

- The root certificate or CRL file of the communication partner was copied to an external storage medium.

##### Procedure

1. Connect the Panel to the external storage medium.
2. In the Control Panel, select "Security &gt; Certificates".
3. Click "Import".

   The "Import certificates" dialog opens.
4. To install the root certificate, select the storage medium and the export file containing the root certificate.

   To update the CRL file, select the storage medium and the export file containing the CRL file.
5. Enter the password that was used to encrypt the file during export.
6. Enter the iteration that was specified when the certificate was created.
7. Click "Import".

##### Result

The root certificate or CRL file is installed in the folder containing trusted certificate authorities. The Panel automatically trusts all application certificates that have this root certificate, except for the certificates listed in the CRL file.

To display the root certificate and the CRL file, select the entry "Certificate Authorities" as the "Certificate Store".

---

**See also**

[Unified tools for certificates (RT Unified)](#unified-tools-for-certificates-rt-unified)
  
[Checking the status of a root certificate on the HMI device (RT Unified)](#checking-the-status-of-a-root-certificate-on-the-hmi-device-rt-unified)
  
[Managing third party certificates and own certificates of a Unified Panel (RT Unified)](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified)

### Exporting an application certificate as a public certificate (RT Unified)

You can export application certificates individually as public certificates with Certificate Manager.

#### Requirement

An application certificate has been added to a device in Certificate Manager.

#### Exporting certificate to the certificate authority device

1. On the certificate authority device, open Certificate Manager.
2. Select the "CA configuration" tab.
3. Right-click on the application certificate under the device.
4. Select "Export certificate...".
5. Select a file format.
6. Confirm your entries.
7. Select a target folder.
8. Confirm your entries.

#### Export certificate on the device

**Additional requirements**

- The device whose application certificate is to be exported is a Unified PC.
- The application certificate has been installed on the device.

**Procedure**

1. On the Unified PC, open Certificate Manager.
2. Select the "Installed certificates" tab.
3. Right-click on the application certificate.
4. Select "Export certificate...".
5. Select a file format.
6. Confirm your entries.
7. Select a target folder.
8. Confirm your entries.

#### Result

The public key of the certificate is exported. Distribute it to the external communication partners.

---

**See also**

[Add application certificates (RT Unified)](#add-application-certificates-rt-unified)
  
[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)

## Using general certificates (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-5)
- [Workflow for general certificates (RT Unified)](#workflow-for-general-certificates-rt-unified)
- [Duplicating a general certificate (RT Unified)](#duplicating-a-general-certificate-rt-unified)
- [Exporting the public key (RT Unified)](#exporting-the-public-key-rt-unified)

### Introduction (RT Unified)

WinCC Unified Certificate Manager enables you to create general CA-based certificates for both HMI devices and other devices.

Application examples:

- Protecting communication of self-written applications through the use of certificates

  For example, ODK applications for HMI devices or applications for other devices
- When using a local web client that logs in to the Runtime web server with RFID and PM-LOGON: creating the certificate that the PM-LOGON server uses to authenticate itself to its clients.

#### Advantages

General certificates provide the same overall advantages as CA-based certificates:

- Secure communication
- Easy establishment of the trust relationship through installation of the root certificate
- Automatic trust relationship if the device and its communication partner have the same certificate authority or the communication partner already trusts the root certificate of the certificate authority

#### Overview

You create a general certificate with Certificate Manager. A device added in Certificate Manager can have multiple general certificates.

You distribute the general certificate with Certificate Manager. This sets up the installation on the device itself and the establishment of the trust relationship on its communication partners.

A general certificate is installed on its device outside of Certificate Manager.

---

**See also**

[Workflow for general certificates (RT Unified)](#workflow-for-general-certificates-rt-unified)

### Workflow for general certificates (RT Unified)

#### Requirement

- WinCC Unified Runtime is installed on a PC.
- The PC serves as the certificate authority device for the CA-based communication of your HMI devices.
- A certificate authority has already been created on the PC in Certificate Manager.
- For an application created for a Unified Panel to use the general certificate of the Panel, it must address the certificate store of the Panel.

#### Procedure

To use general certificates, follow these steps:

| Symbol | Meaning |
| --- | --- |
| 1. Start Certificate Manager on the certificate authority device. 2. If the device for which you want to create the general certificate is not yet part of the CA infrastructure, add it. 3. Right-click the device and select "Add Certificate &gt; General ...". 4. Enter the properties of the certificate in the "New certificate" dialog.    The following applies:    - You can use a template. To do this, select the "Use template" option and select the template from the list next to it.        | Symbol | Meaning |      | --- | --- |      | **Note**  Only one template is available in the current version. Alternatively, you can duplicate a general certificate that has already been added and change the desired properties on the duplicate. |  |    - "Security" tab, "Key usage" and "Enhanced key usage" fields: To add, delete or edit a usage, right-click in the field and select the desired command. 5. Set up the installation of the general certificate on the device. Follow these steps:    - Right-click on the general certificate and select "Export certificate ...".      The "Export certificate" dialog opens.    - Select the "Export with private key" option.    - To protect the usage of the private key, assign a password.         | Symbol | Meaning |      | --- | --- |      | **Note**  To be able to use the private key, the target application must also provide this password. |  |    - Specify the format for the export. Select one of the following options for this:         | Symbol | Meaning |      | --- | --- |      | "Export public certificate in DER format" | Public key and private key are exported to a common PFX file. |      | "Export public certificate in PEM format" | Public key and private key are each exported to a separate PEM file. |    - Click "Export".    - Select the storage location and confirm your entry. 6. Transfer the file or files to the device. 7. Install the private key and public key of the certificate in the own certificates of the device. Follow the procedure described in the user help of the respective device or the application.      | Symbol | Meaning |    | --- | --- |    | **Note**  If the device is a Unified Panel, install them in the certificate store of the Panel. Follow the procedure described below. If the device is a Unified PC, the certificate store depends on the implementation of the application. Use of the following certificate stores is possible: - Windows certificate store   Double-click the export file(s). Manually install the file(s) in the appropriate folder of the Windows certificate store. - WinCC Unified certificate store, other file-based certificate stores   Manually copy the file(s) in a file explorer to the appropriate folder of the certificate store.Installation with Certificate Manager is not possible. |  | 8. If necessary, establish the trust relationship between the device and its communication partner.       | Symbol | Meaning |    | --- | --- |    | **Note**  In the following cases, the communication partner already trusts the root certificate and, thus, also the general certificate of the device: - The communication partner is an HMI device. The HMI device has the same certificate authority as the device. The certificates of the HMI device are installed on the HMI device. - The device and its communication partner have different certificate authorities. The communication partner already communicates with another device that has the same Unified certificate authority as the device with the general certificate. |  |     Follow these steps:    - Export the root certificate and its CRL file on the certificate authority device in Certificate Manager.    - Transfer the file containing the root certificate and the CRL file to the device of the communication partner.    - Install the root certificate on the device of the communication partner in the folder containing the trusted root certificate authorities.      Follow the procedure described in the user help of the respective device.      If the communication partner is a Unified PC, use SIMATIC Runtime Manager for this.       If the communication partner is a Unified Panel, use "Control Panel &gt; Security &gt; Certificates". |  |

#### Installing the general certificate of a Unified Panel on the Panel

1. Transfer the file(s) with the public key and private key of the general certificate to an external storage medium.
2. Connect the storage medium to the Panel.
3. In the Control Panel, select "Security &gt; Certificates".
4. Click "Import".

   The "Import certificates" dialog opens.
5. Select the storage medium and the export file.
6. Enter the password that was used to encrypt the file during export.
7. Enter the iteration that was specified when the certificate was created.
8. Click "Import".

---

**See also**

[Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)
  
[Adding devices (RT Unified)](#adding-devices-rt-unified)
  
[Creating a certificate authority and root certificate (RT Unified)](#creating-a-certificate-authority-and-root-certificate-rt-unified)
  
[Introduction (RT Unified)](#introduction-rt-unified-5)

### Duplicating a general certificate (RT Unified)

#### Requirement

A general certificate has been added to a device in WinCC Unified Certificate Manager.

#### Procedure

1. In the "CA Configuration" tab, open a device that has a general certificate.
2. Right-click the certificate and select "Duplicate ...".
3. The "Duplicate certificate" dialog opens.
4. Edit the properties of the new general certificate as needed.
5. Click "OK".

### Exporting the public key (RT Unified)

#### Requirement

A general certificate has been added to a device in WinCC Unified Certificate Manager.

#### Procedure

1. In Certificate Manager, right-click the general certificate and select "Export certificate ...".

   The "Export certificate" dialog opens.

   The "Export with private key" option is deselected
2. Specify the file format in which the public key is exported. Select one of the following options for this:

   - "Export public certificate in DER format"
   - "Export public certificate in PEM format"
3. Click "Export".
4. Select the storage location and confirm your entry.

#### Result

The public key of the certificate is exported. Distribute it to the external communication partners of the device.

## Using self-signed certificates (RT Unified)

> **Note**
>
> **Recommendation**
>
> ​For security reasons the usage of CA-based certificates is recommended.

### Introduction

A self-signed certificate confirms its validity through its own signature. It is less secure than a CA-based certificate. Its usage is subject to numerous limitations.

### Limitations

Self-signed certificates offer a lower protection than CA-based certificates:

- They are vulnerable to "man in the middle" attacks.

  In the case of "Man in the middle" attacks, data exchanged between the communication partners is intercepted or changed.
- It is not possible to detect whether a self-signed certificate was compromised.
- Self-signed certificates can not be managed centrally.
- Users must trust self-signed web server certificates in each browser individually and call the certificate individually again if it is no longer trustworthy.

Furthermore, using self-signed certificates is subject to the following limitations:

- Firewall and network settings can prevent the usage of self-signed certificates.
- ​The web clients of a Unified web server must install the web server certificate in the web browser. The installation of self-signed certificates is not supported by all web browsers.
- Depending on the web browser, it is possible to define exceptions. For more detailed information, refer to the operating instructions of the browser.
- You can not use self-signed certificates for the following Unified components. They always require the usage of CA-based Unified certificates:

  - WinCC Unified Collaboration
  - WinCC Unified Audit
  - Unified OPC UA Clients
- The self-signed web server certificate expires after 12 months.
- The self-signed certificates of Unified Panels are re-created with each runtime start or restart. The communication partners must subsequently trust the new certificate.

### Self-signed own certificates of HMI devices

A HMI device can have the following self-signed own certificates:

| Certificate | HMI device | More information |
| --- | --- | --- |
| Web server certificate | Unified Panels | Section [Workflow with a self-signed certificate (Panel as web server)](#workflow-with-a-self-signed-certificate-panel-as-web-server-rt-unified) |
| Unified PCs | Section [Workflow with a self-signed certificate (PC as web server)](#workflow-with-a-self-signed-certificate-pc-as-web-server-rt-unified) |  |
| OPC UA Server certificate | Unified Panels | Section [Using a default self-signed certificate (Panel as OPC UA server)](#using-a-default-self-signed-certificate-panel-as-opc-ua-server-rt-unified) |
| Unified PCs | Section [Using a default self-signed certificate (PC as OPC UA server and exporter)](#using-a-default-self-signed-certificate-pc-as-opc-ua-server-and-exporter-rt-unified) |  |
| OPC UA Exporter certificate | Unified PC that is an OPC UA Server |  |
| Smart Server certificate | Unified Panels | Section [Smart Server certificates for Panels](#smart-server-certificates-for-panels-rt-unified) |

### Self-signed third-party certificates

The communication partners of an HMI device can have self-signed certificates. Information on how you create these certificates is available in the user help of the respective communication partner.

For information on how to display the self-signed third-party certificates on an HMI device, how to trust, reject or uninstall them, see section [Managing third party certificates and own certificates of a Unified Panel](#managing-third-party-certificates-and-own-certificates-of-a-unified-panel-rt-unified) and section [Managing third-party certificates of a Unified PC](#managing-third-party-certificates-of-a-unified-pc-rt-unified).

For information on the protection of the communication between HMI device and S7 controller through a self-signed PLC certificate, see section [Communication with S7-1500 and S7-1200](#communication-with-s7-1500-and-s7-1200-rt-unified).

### Self-signed OPC UA Client certificate of the engineering system.

During the configuration of a Unified OPC UA Client the engineering system acts as an OPC UA Client. It uses a self-signed certificate. For information on using this certificate, see section [Engineering System as OPC UA client](#engineering-system-as-opc-ua-client-rt-unified-1).

---

**See also**

[Using CA-based certificates (RT Unified)](#using-ca-based-certificates-rt-unified)

## WinCC Unified Certificate Manager (RT Unified)

This section contains information on the following topics:

- [Introduction (RT Unified)](#introduction-rt-unified-6)
- [Opening Certificate Manager (RT Unified)](#opening-certificate-manager-rt-unified)
- [User interface (RT Unified)](#user-interface-rt-unified)
- [Customize surface (RT Unified)](#customize-surface-rt-unified)
- [Changing the user interface language (RT Unified)](#changing-the-user-interface-language-rt-unified)
- [Password requirements (RT Unified)](#password-requirements-rt-unified-1)

### Introduction (RT Unified)

You use the WinCC Unified Certificate Manager application to create, manage and distribute the CA-based application certificates of your HMI devices. You also use Certificate Manager to create, manage and distribute the general CA-based certificates of the HMI devices and, if needed, other devices.

On Unified web server PCs, you also use Certificate Manager to install own CA-based application certificates of the PC and to display or uninstall them.

---

**See also**

[Customize surface (RT Unified)](#customize-surface-rt-unified)
  
[Changing the user interface language (RT Unified)](#changing-the-user-interface-language-rt-unified)
  
[Using CA-based certificates (RT Unified)](#using-ca-based-certificates-rt-unified)
  
[Workflow for using CA-based certificates (RT Unified)](#workflow-for-using-ca-based-certificates-rt-unified)
  
[Using general certificates (RT Unified)](#using-general-certificates-rt-unified)

### Opening Certificate Manager (RT Unified)

#### Requirement

The user logged in to the PC has local administrator rights.

#### Procedure

To open WinCC Unified Certificate Manager, choose one of the following options:

- Double-click the Desktop shortcut that was created during Runtime installation.
- Select the application in the Windows Start bar.
- With standard installation, you will find the application under "C:\Program Files\Siemens\Automation\WinCCUnified\ WebConfigurator\WinCC_CertManager.exe".

  Double-click the EXE file.

### User interface (RT Unified)

This section contains information on the following topics:

- [Structure of the user interface (RT Unified)](#structure-of-the-user-interface-rt-unified)
- ["CA configuration" tab (RT Unified)](#ca-configuration-tab-rt-unified)
- ["Installed certificates" tab (RT Unified)](#installed-certificates-tab-rt-unified)

#### Structure of the user interface (RT Unified)

##### Overview

The interface of WinCC Unified Certificate Manager has the following structure:

![Overview](images/163008337035_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Menu bar |
| ② | Toolbar |
| ③ | Work area with the "CA configuration" and "Installed certificates" tabs |
| ④ | "Details" area (fixed)  The "Details" area shows you detailed information about the certificate selected in the work area. |
| ⑤ | Information bar |
| ⑥ | "Output" area (hidden)  The "Output" area logs operator control actions. |

You can customize the display of the interface to suit your needs. See also [Customize surface](#customize-surface-rt-unified).

##### Menu bar

| Menu | Description |
| --- | --- |
| "File &gt; Exit" | Closes Certificate Manager. |
| "View" | Configure which Certificate Manager interface elements you see.  You can open or close the following interface elements:  - "Output" area - "Details" area - "CA configuration" tab - "Installed certificates" tab |
| "Help" | "Certificate Manager Help"  Opens the user help in a browser. |
| "Info Certificate Manager"  Opens a dialog with information about the installed software version. |  |

##### Toolbar

| Button |  |
| --- | --- |
| ![Toolbar](images/151127983115_DV_resource.Stream@PNG-de-DE.png) | To change the user interface language |
| ![Toolbar](images/151126848139_DV_resource.Stream@PNG-de-DE.png) | To call the user help |

##### Tab of the working area

See ["Installed certificates" tab](#installed-certificates-tab-rt-unified) and ["CA configuration" tab](#ca-configuration-tab-rt-unified).

---

**See also**

[Creating and exporting the CA infrastructure (RT Unified)](#creating-and-exporting-the-ca-infrastructure-rt-unified)
  
[Importing and installing certificates of a Unified PC (RT Unified)](#importing-and-installing-certificates-of-a-unified-pc-rt-unified)

#### "CA configuration" tab (RT Unified)

##### On a certificate authority device

On a certificate authority device, you can perform the following actions on the "CA configuration" tab:

- Create the certificate authority (root certificate and CRL file)
- Manage devices and certificates (add, delete, recreate)
- Export the device certificates as well as the root certificate and the CRL file
- If the certificate authority device is also used as an HMI device: Install or delete the application certificates issued by the certificate authority
- Renew all certificates of a device, individual certificates, the CRL file or the entire CA infrastructure including the root certificate
- Data backup

> **Note**
>
> **Content of the tab**
>
> After starting WinCC Unified Certificate Manager, you will see the same data that the certificate authority had when you last closed the Certificate Manager:
>
> - If no data has been generated yet, you will see the nodes "Open configuration ..." and "Create certificate authority ..."
> - If data has already been generated, you see the root certificate of the Unified certificate authority and its CRL file as well as the devices added to the CA infrastructure, their application certificates and general certificates.
>
>   You can edit them.

##### On runtime PCs

On Unified PCs that do not serve as a certificate authority, you can perform the following actions on the "CA configuration" tab:

- Import and install or delete the application certificates issued for the PC by the certificate authority

> **Note**
>
> **Content of the tab**
>
> After launching the Certificate Manager, you will see the nodes "Open new configuration ..." and "Create certificate authority ...".
>
> After opening a new configuration, you will see the root certificate of the Unified certificate authority and its CRL file, as well as the configured devices, their application certificates, and general certificates.
>
> You can only install the application certificates of the local device. The display of the general certificates of the PC as well as the certificates of the other devices is for information purposes only.
>
> Closing the Certificate Manager also closes the configuration.

##### General certificates

You can generate and export general certificates on the "CA configuration" tab on the certificate authority device. The export prepares the installation of the general certificate on its device.

On Unified PCs, you also see the general certificates in Certificate Manager after the import. This is for information purposes only. A general certificate is installed on the PC outside of Certificate Manager.

---

**See also**

[Structure of the user interface (RT Unified)](#structure-of-the-user-interface-rt-unified)
  
[Creating and exporting the CA infrastructure (RT Unified)](#creating-and-exporting-the-ca-infrastructure-rt-unified)

#### "Installed certificates" tab (RT Unified)

In the "Installed certificates" tab, you can see which application certificates are installed on the local device.

You have the option to uninstall certificates by deleting them.

---

**See also**

[Structure of the user interface (RT Unified)](#structure-of-the-user-interface-rt-unified)

### Customize surface (RT Unified)

Display and arrangement of the interface elements of WinCC Unified Certificate Manager are configurable:

| User interface elements | Close / Open | Move | Undock / dock | Fix / Unfix | Show / Hide |
| --- | --- | --- | --- | --- | --- |
| "Details" area | ✓ | ✓ | ✓ | ✓ | ✓ |
| "Output" area | ✓ | ✓ | ✓ | ✓ | ✓ |
| Tab of the working area | ✓ | ✓ | - | - | - |

#### Closing and opening

To close a user interface element, click the "X" button. Alternatively, disable it in the "View" menu.

To open a closed user interface element, enable it in the "View" menu.

#### Move

1. Move the title bar of the desired user interface element with the left mouse button pressed.

   Possible insertion positions are displayed in the interface:

   ![Move](images/151125350411_DV_resource.Stream@PNG-de-DE.png)

   ![Move](images/151125350411_DV_resource.Stream@PNG-de-DE.png)

   The offered insertion positions depend on which element you move and which elements the application window already displays.
2. To see a preview of the new arrangement, move the mouse cursor to one of the positions and keep the mouse cursor pressed:

   ![Move](images/151120399243_DV_resource.Stream@PNG-en-US.png)

   ![Move](images/151120399243_DV_resource.Stream@PNG-en-US.png)
3. Release the mouse cursor over the desired insertion position.

The user interface element is moved.

#### Undocking and docking

When you move the header of the "Details" or "Output" area, the area is undocked from the application window and displayed as a standalone window. You can move the window freely.

To dock the area back to the application window, move it to one of the suggested insertion positions.

#### Fixing and unfixing

The following button fixes or unfixes the "Details" and "Output" areas:

| Representation of the user interface | Status | Changing setting |
| --- | --- | --- |
| ![Fixing and unfixing](images/151125909387_DV_resource.Stream@PNG-de-DE.png) | Fixed  The area is displayed even if it does not have the focus. | Click the button to switch the setting. |
| ![Fixing and unfixing](images/151125917963_DV_resource.Stream@PNG-de-DE.png) | The area is hidden as soon as it loses focus. |  |

#### Showing and hiding

**Requirement**

The "Details" and "Output" areas are not fixed.

**Procedure**

To show an area, click on its text. The area is displayed.

It is automatically hidden when you click the mouse cursor outside the area.

### Changing the user interface language (RT Unified)

#### Procedure

1. Click the button with the arrow in the toolbar:

   ![Procedure](images/151127983115_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/151127983115_DV_resource.Stream@PNG-de-DE.png)
2. Select the desired language.

#### Result

Changing the user interface language

### Password requirements (RT Unified)

The passwords defined in the Certificate Manager must meet the following requirements:

- Length: At least 8 characters
- In each case at least one uppercase letter, one lowercase letter, one number and one special character
