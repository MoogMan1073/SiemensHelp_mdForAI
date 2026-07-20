---
title: "Configuring security"
package: HWSimNetSecurityenUS
topics: 218
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring security

This section contains information on the following topics:

- [General](#general)
- [SCALANCE S](#scalance-s)
- [Security for S7-300 /S7-400 / PC CPs](#security-for-s7-300-s7-400-pc-cps)
- [Security for S7-1200-/S7-1500-CPs](#security-for-s7-1200-s7-1500-cps)

## General

This section contains information on the following topics:

- [Supported devices](#supported-devices)
- [Overview - Scope of performance and method of operation](#overview---scope-of-performance-and-method-of-operation)
- [User interface for security functions](#user-interface-for-security-functions)
- [Running a consistency check](#running-a-consistency-check)
- [Replacing a security module](#replacing-a-security-module)
- [Managing certificates](#managing-certificates)
- [Special features of user management for security functions](#special-features-of-user-management-for-security-functions)
- [Authentication using a RADIUS server](#authentication-using-a-radius-server)
- [Generating configuration data for SCALANCE M modules](#generating-configuration-data-for-scalance-m-modules)
- [Generating configuration data for security devices](#generating-configuration-data-for-security-devices)
- [Setting up a firewall](#setting-up-a-firewall)
- [Syslog](#syslog)
- [Carrying out module-specific log settings](#carrying-out-module-specific-log-settings)
- [Security module as router](#security-module-as-router)
- [Configuring time-of-day synchronization](#configuring-time-of-day-synchronization)
- [Security module as DHCP server](#security-module-as-dhcp-server)
- [Configuring SNMP](#configuring-snmp)
- [Configuring proxy ARP](#configuring-proxy-arp)
- [Activate Web server on security module](#activate-web-server-on-security-module)
- [IPsec VPN tunnel: Creating and assigning VPN groups](#ipsec-vpn-tunnel-creating-and-assigning-vpn-groups)
- [Establishing an OpenVPN tunnel to the SINEMA Remote Connect server](#establishing-an-openvpn-tunnel-to-the-sinema-remote-connect-server)
- [Configuring router and firewall redundancy](#configuring-router-and-firewall-redundancy)
- [Online functions - diagnostics and logging](#online-functions---diagnostics-and-logging)
- [Download functions](#download-functions)

### Supported devices

#### Supported devices

The security functions described in this help section are supported y the following products;

- SCALANCE S-600:

  - S602 V4
  - S612 V4
  - S623 V4
  - S627-2M V4
- S7 CPs / TIM: CP 343-1 GX31 Advanced, CP 443-1 GX30 Advanced, CP 443-1 OPC UA, CP 1543-1, CP 1542SP-1 IRC, CP 1543SP-1, CP 1545-1, CP 1243-1 BX30, CP 1243-1 PCC, CP 1242-7 KX31, CP 1243-7 LTE, CP 1243-8 IRC, TIM 4R-IE, TIM 4R-IE DNP3, TIM 1531 IRC
- PC CP: CP 1628

#### General terminology "security module"

In this section of the information system the name "security module" is used instead of the product names named above. You will find the functional differences between the products in the Siemens Industry Mall.

#### Use of the terms "interface" and "port"

In this documentation, the ports of SCALANCE S modules are named as follows:

- "External interface": The external port of the SCALANCE S602 / S612 / S623 or an external port of the SCALANCE S627-2M (marked red)
- "Internal interface": The internal port of the SCALANCE S602 / S612 / S623 or an internal port of the SCALANCE S627-2M (marked green)
- "DMZ interface": The DMZ port of the SCALANCE S623 / S627-2M (marked yellow)

The term "port" itself is used when the focus of interest is a special port of an interface.

#### Structure of this section of the help system

Topics that are relevant to several module types can be found in the "General" section. Information that is only relevant to a certain module type can be found in the sections relating specifically to these module types.

### Overview - Scope of performance and method of operation

#### General use of the term "STEP 7"

Configuration of security functions is supported as of STEP 7 V12. For this reason, in this section of the information system, the name "STEP 7" will be used for all versions of STEP 7 V12 or higher.

#### Scope of performance

You can use the following security functions in STEP 7:

- Configuration of the security modules
- Creating VPN configuration files for VPN devices from third-party manufacturers
- Test and diagnostics functions, status displays

#### Offline configuration view and online diagnostics view

The security functions are configured in two views:

- Offline configuration view

  In the offline configuration view, you create the configuration data. Prior to downloading, there must already be a connection to the security modules.
- Online diagnostics view

  The online/diagnostics view is used for diagnostics of the security module and, among other things, allows you to run firmware updates.

#### How it works - security and consistency

- Access only for authorized users

  The security functions of every project are only available when project protection is active. This protects the security functions from accidental or unauthorized changes.
- Consistent project data

  Consistency checks are running even while you make the entries in the dialogs. In addition, cross-dialog, project-wide consistency checks are carried out.

  Only consistent project data can be downloaded to the security modules.
- Protecting project data by encryption

  The project and configuration data relevant to security are protected by encryption. Depending on the security module, data can be stored in the project and/or on the C-PLUG.

### User interface for security functions

![Figure](images/105142226315_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Security functions    ![Figure](images/105144854795_DV_resource.Stream@PNG-en-US.png)   The global security functions are located in the project navigation. The global security functions can be configured independently of the module and subsequently assigned to individual security modules as required. Changes to the global security functions must be loaded on all security modules involved. This also applies to the settings of redundancy relationships.  To display the global security functions completely in the project navigation the project protection must be activated and there must be at least one security module in the project. If the first security module is a CP, the local security settings of the CP must also be activated.  The following main folders and entries are available in the global security functions:  - Certificate manager In the certificate manager, you see an overview of all the certificates used in the project. You can, for example, import new certificates as well as export, renew or replace existing certificates. - Firewall Under the "Firewall" entry, you can define global IP and MAC firewall rule sets and user-specific IP rule sets (SCALANCE S modules only) and assign security modules. Global firewall rule sets can also be exported from STEP 7 and imported into STEP 7. IP and MAC service definitions are used to define the IP and MAC firewall rules compactly and clearly. - VPN groups All created VPN groups are contained in this folder. You can create new VPN groups here and assign security modules to these VPN groups. You can also adapt VPN group properties of VPN groups that have already been created. - NTP Here, you can create NTP servers and assign them to one or more security modules. This ensures that time synchronization is performed through the assigned NTP server. Unsecured NTP servers can only be configured in the local security settings. - Syslog - RADIUS Here, you can create RADIUS servers and assign them to one or more security modules. With this, you ensure that authentication queries from users who log on to the selected security module to activate user-specific IP rule sets are forwarded to the assigned RADIUS server. - Log files (offline view) Opens logged system, audit and packet filter events that you saved as a file in the online diagnostics. |
| ② | Work area    ![Figure](images/61482500619_DV_resource.Stream@PNG-en-US.png)   Once you have selected a module in the work area, you can configure its local security settings in "Properties" > "General". If the selected object is in a VPN group, related information is displayed in the VPN tab. |
| ③ | VPN tab    ![Figure](images/61482701451_DV_resource.Stream@PNG-en-US.png)   This tab displays information about all the VPN groups to which the security module that was selected in the working area belongs. Information about the respective participants of a VPN group can be displayed and hidden. |
| ④ | Local security settings    ![Figure](images/68944661515_DV_resource.Stream@PNG-en-US.png)   Local security settings are configured for a specific module. After one of these objects has been selected in the working area, its local security settings are available in the Inspector window under "Properties" > "General". To display the local security settings, project protection must be activated.  For CPs in the Inspector window, the "Activate security features" check box must be activated n the "Properties" > "General" tab, "Security" entry. The local security settings are then displayed below the "Security" entry. When the check box is selected, the some of the CP settings (assuming they were enabled) are migrated automatically to the local security settings.  Depending on the particular security module, additional security functions are also available such as NTP (secure), SNMPv3, FTPS.  In addition, firewall rules that enable a connection to be established are created automatically for configured connections. Log settings are available to record blocked packets. |

#### Secure and non-secure configuration areas

The user interface can be divided into secure and non-secure configuration areas.

The secure areas are areas in which configuration is possible only after activating project protection. These areas are encrypted and therefore only available to persons authorized in the user management even if the project is accessible to a wider circle of people.

Functions from the non-secure areas, on the other hand, can be configured without activating project protection. The correctness of the settings must be checked before downloading the project to the plant components if a wider circle of people can make modifications to the project.

Below, you will find a list of the configuration areas of the user interface showing which areas are secure and which are non-secure. To some extent, this depends on the security module for which the configuration is created.

- All settings from the global security functions are secure.
- Secure and non-secure configuration areas for SCALANCE S modules:

  - The settings under the entry "General" in the local security settings are non-secure.
  - Higher-level settings (e.g. MRP settings such as MRP manager etc.) that are not configured on the security module itself but may affect the security module are non-secure. This does not relate to the global security functions.
  - The other settings are protected.
- Secure and non-secure configuration areas for CPs:

  - All settings outside the "Security" entry are non-secure.
  - Higher-level settings (e.g. MRP settings such as MRP manager, PROFINET settings, connections etc.) that are not configured on the security module itself but may affect the security module are non-secure. This does not relate to the global security functions.
  - All the settings for the interfaces and ports, in particular IP addresses, are non-secure.
  - All settings below the "Security" entry are secure.

#### Restrictions in the use of libraries

If a master copy is created in the global library for a security module, the configuration of this security module is lost in the master copy. You need to log in again if you use a master copy.

If a master copy is created in the project library for a security module, the configuration of this security module is retained, apart from the cross-module information for VPN and redundancy relationships.

#### IP addresses for configurable servers

When configuring servers, the (alias) IP addresses of the security module must not be used. For all configurable servers, there is a consistency check when the IP address is assigned.

### Running a consistency check

#### Overview

The following consistency checks are available:

- Local consistency checks
- Project-wide consistency checks

In the individual dialog descriptions in this help system, the rules you need to take into account for your entries are listed under the keyword "Consistency check".

#### Local consistency checks

A consistency check is local when it can be performed directly within a dialog. With the following actions, local consistency checks are made:

- After exiting a box
- After exiting a row in a table
- When you confirm a dialog with OK.

#### Project-wide consistency checks

Project-wide consistency checks provide you with information indicating whether or not project data is correctly configured. With the following actions, there is a consistency check through the entire project:

- When compiling a configuration
- When downloading a configuration

> **Note**
>
> You can only download configured data to a security module if the project-wide consistency check for the security module was successful.

### Replacing a security module

#### Module-specific function

Modules can be replaced by modules with higher firmware versions. The local security settings of the modules must be activated for this, see section:  
[Replacing a security module](#replacing-a-security-module-1).

#### Requirement

To be able to replace security modules, their module descriptions must be up to date. To update the module description of security modules, follow the steps below:

1. Select the security module to be edited.
2. In the local security settings, click on the entry "General" > "Catalog information".
3. Click the "Update module description" button.

#### How to access this function

1. Select the security module to be edited in the topology or network view.
2. Right-click on the security module and select the shortcut menu command "Change device...".

### Managing certificates

This section contains information on the following topics:

- [Overview of certificates](#overview-of-certificates)
- [Certificate authorities](#certificate-authorities)
- [Device certificates](#device-certificates)
- [Trusted certificates and root certification authorities](#trusted-certificates-and-root-certification-authorities)
- [Importing certificates](#importing-certificates)
- [Exporting certificates](#exporting-certificates)
- [Assigning certificates](#assigning-certificates)
- [Create/renew certificates](#createrenew-certificates)
- [Replacing certificates](#replacing-certificates)
- [Telecontrol: Handling certificates for TLS](#telecontrol-handling-certificates-for-tls)

#### Overview of certificates

##### Certificate management

The certificate manager in the global security functions contains an overview of all the certificates used in the project. Depending on the device, all fields or only those valid for the device are shown:

- ID: Every certificate in the certificate manager receives an ID. The certificate ID is assigned by the certificate manager when a certificate is created or imported. In certain cases, e.g. with OPC UA server certificates, this ID is used for identification of the certificates. The certificate ID is unique within the project and cannot be changed.
- Common name of subject: Device or certificate authority for which the certificate is valid.
- Serial number: Unique serial number of the certificate that was issued by the certificate issuer.
- Issuer: Shows the name as well as the organization and country of the certificate issuer.
- Serial number of the Issuer: For device certificates, the serial number of the certificate issuer is displayed.
- Valid to: Indicates when the certificate expires.
- Used as: Indicates for which application or service the certificate is used, e.g. as SSL certificate or certificate authority. Further, additional information from the certificate is displayed.
- Private key: Indicates whether or not a private key exists.
- Signature algorithm Indicates the cipher of the private key as well as the hash algorithm used.
- Key length: Shows the key length of the certificate.
- Responsibility: Selection of how the certificate should be kept up to date. You will find more detailed information in the section [Device certificates](#device-certificates).

The data can be changed via the "Renew" or "Create" entry in the shortcut menu.

> **Note**
>
> **Downloading the configuration**
>
> After replacing or renewing certificates, the configuration must be downloaded to the relevant security modules.
>
> After replacing or renewing CA certificates, the configuration must be downloaded to all security modules.

> **Note**
>
> **Current date and current time of day on the security modules**
>
> When using secure communication (for example, HTTPS, VPN...), make sure that the security modules involved have the current time of day and the current date. Otherwise the certificates used are not evaluated as valid and the secure communication does not work.

##### Global certificate manager

Double-click on the "Certificate manager" entry in the global security functions.

In the individual tabs, you have the following commands available in the shortcut menu:

| Command | Meaning |
| --- | --- |
| Import | Import of new/trustworthy certificates and certificate authorities as well as certificate chains with or without private key and encryption; see section [Importing certificates](#importing-certificates). Select one of the following formats:  *.der: DER coded certificate  *.cer: DER coded certificate  *.crt: PEM coded certificate  *.pem: PEM coded certificate   *.p12 formats (up to 256 characters):  - PKSC12 archive: Certificate with associated private key - PKSC12 chain archive: Certificate with associated private key and all certificates of the certification path |
| Create | Opens the "Create certificate" dialog in which you can have a new certificate created by STEP 7 when necessary, for example, when certificates were accidentally deleted; see section [Create/renew certificates](#createrenew-certificates). |
| Export | Export of certificates and certificate chains with or without private key and encryption. Select one of the following formats:  *.der: DER coded (unencrypted) certificate  *.cer: DER coded (unencrypted) certificate  *.crt: PEM coded certificate  *.pem: PEM coded certificate  *.crl: Certificate Revocation List, DER-coded   *.p12 formats (up to 256 characters):  - PKSC12 archive: Certificate with associated private key - PKSC12 chain archive: Certificate with associated private key and all certificates of the certification path   After clicking the "Save" button and depending on the selection, an additional dialog appears in which you can make further settings; see section [Exporting certificates](#exporting-certificates). |
| Show | Opens the certificate dialog of Windows where you see an overview of all certificate data.  For the certificate to be displayed as valid, install it via the "Install certificate..." button of the "General" tab in the Windows certificate store. Appropriate Windows user rights are required to install the certificate. |
| Renew | Opens the "Renew certificate" dialog in which you can have a new certificate created by STEP 7 when necessary.  Example uses: compromised certificate, expired validity, updated encryption method; see section [Create/renew certificates](#createrenew-certificates). |
| Replace | Opens the "Replace certificate" dialog in which you can replace an existing certificate with a new one, for example, when validity has expired; see section [Replacing certificates](#replacing-certificates). |
| Assign | Opens the "Assign certificate" dialog in which you can assign an existing certificate to one or more devices as a device certificate or a trusted certificate; see section [Assigning certificates](#assigning-certificates). |
| Delete | Deletion of manually imported certificates. |

##### Local certificate manager

Certificates that were imported via the certificate manager in the global security functions are not automatically assigned to the corresponding modules. Imported certificates must be included in the list of trustworthy partner certificates manually via the "Certificate manager" entry in the local security settings. Certificates generated by STEP 7 such as SSL certificates or VPN group certificates are automatically assigned to the corresponding modules and do not need to be assigned using the local security settings.

Before certificates can be referenced in program blocks for "Secure Communication", these certificates must be assigned to the security module as device certificates via the local certificate manager. After selecting a table cell, you can either create a new certificate using the "Add" button or use an existing certificate of the project using the check mark symbol. For access to existing certificates of the project and for signing a new certificate by a certificate authority, the check box "Use global security functions for the certificate manager" must be activated.

#### Certificate authorities

##### "Certificate authority (CA)" tab

A CA certificate is a certificate issued by a "Certificate Authority" which generates and signs the device certificates.

Certificate authorities can be:

- The STEP 7 project itself. If the "Common name of subject" and "Issuer" are the same, this is a self-signed certificate; in other words, a certificate issued by the STEP 7 project with private key.
- A higher ranking certificate authority with private key. These third-party certificates are external to the project and are imported into and stored in the certificate store of STEP 7.

The following certificate authorities are automatically generated:

- CA certificates of a project: When you create a new project, CA certificates are generated for the project that use different hash algorithms for the certificate signature. CA certificates for projects are always loaded on the security modules belonging to them. The SSL certificates and OPC UA client/server certificates for the individual security modules are derived from the CA certificates.
- CA group certificates: When you create a new VPN group, a CA certificate is generated for the VPN group. The VPN device certificates for VPN group members are derived from this certificate.

#### Device certificates

##### "Device certificates" tab

Display of the device-specific certificates generated by the certification authorities for modules. These include:

- SSL certificate of a module: An SSL certificate that is derived from a CA certificate of the project is generated for each module that you create. SSL certificates are used for authentication during secure communication between PG/PC and module when downloading the configuration.
- OPC UA client/server certificate of the module: Depending on the configured OPC UA client/server function of the CP 443-1 OPC UA, an OPC UA client/server certificate is generated that is used for authentication with the relevant communications partner.
- VPN group certificate of a module: In addition, a VPN device certificate is generated for each module per VPN group in which it is located.

****Selecting the** 
**Responsibility****

By default, the setting is "User" for all device-specific certificates and cannot be changed. For OPC UA certificates only, the default setting is "System" and you can choose how they should be kept up to date:

- System: After compilation, all certificate parameters (except "Valid from" and "Valid to") are reset to the default settings and updated automatically by the system. Parameters that you added in addition (e.g. for "Subject Alternative Name (SAN)") are deleted. This behavior also applies to the switch from "User" to "System".
- User: After compilation, the certificate parameters (e.g. for "Subject Alternative Name (SAN)") remain unchanged or are maintained the way the user set them in the "Renew certificate" dialog. The parameters are not automatically updated by the system.

#### Trusted certificates and root certification authorities

##### "Trusted root certification authorities" tab

Display of the third-party certificates imported into STEP 7. Server certificates can be imported for example from external FTP servers, project certificates from other STEP 7 projects and certificates required for the external services such as dyn.DNS.

After the import, certificates must be assigned to the corresponding modules via the local security settings or the "Assign" function in the certificate manager. For further information, refer to the section [Overview of certificates](#overview-of-certificates).

#### Importing certificates

##### Importing certificates

If you import or create/renew a file, the system detects automatically which certificates are part of the file.

For example, this may be a certificate chain which consists of the following contents:

- Device certificate A which was issued by certificate authority 1 with private key
- CA certificate B of the certificate authority 1 without private key
- CA certificate C of the certificate authority 2 which issued certificate B without private key

When importing the file, the following certificates are now stored:

- Device certificate A in the "Device certificates" tab; private key: Yes
- CA certificate B of the certificate authority in the tab "Certificate authority (CA)"; private key: No
- CA certificate C of certificate authority 2 in the tab "Certificate authority (CA)"; private key: No

To be able to generate new device certificates with renewal as certificate authority 1, proceed as follows:

- Import a certificate of certificate authority 1 with private key.

  Result:

  - Certificate B of the certificate authority in the "Certificate authority (CA)" tab is not overwritten because it has already been imported.
  - The status of the private key is set from "No" to "Yes".
  - New device certificates can now be signed during renewal.

This behavior also applies to the creation/renewal of certificates, see section [Create/renew certificates](#createrenew-certificates).

Files with max. 256 characters can be imported for the *.p12 format.

#### Exporting certificates

##### Settings for export

Depending on the format, the following options can be selected for the export:

| Available for selection during export: | Format |  |  |  |  |  | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *.cer | *.der | *.crt. | *.pem | *.crl | *.p12 <sup>1)</sup> |  |  |
| Private key | x | x | x | x | - | x | For *.cer and *.der: An additional key file is exported for the certificate. The exported key file cannot be imported again.  For *.crt and *.pem: Stored together with the certificate in a file. |
| Encrypted private key | - | - | x | x | - | - | Selection of the encryption method and input of password possible. If you do not enter a password, the project name is used as the password. |
| Certificate chain | - | - | x | x | - | - | Only possible if the certificates of the certificate chain are stored in the certificate manager. |
| Password only | - | - | - | - | - | x | If you do not enter a password, the project name is used as the password. |
| x: Format is supported  -: Format is not supported   <sup>1)</sup>: Max. 256 characters |  |  |  |  |  |  |  |

##### Export of *.p12 files

The "Use secure key for .p12 file" option can be selected for the export of *.p12 files

- When selected, the encryption algorithms currently considered secure are used to create the PKCS12 container.

  - Certificate: PPKDF2
  - Private key: AES
- When deselected, the encryption algorithms that are no longer considered secure are used to create the PKCS12 container.

  - Certificate: 40-Bit-RC2
  - Private key: 3DES

Before loading the PKCS12 container, check whether the device supports the encryption algorithms.

#### Assigning certificates

##### Meaning

In the "Assign certificate with ID x to device" dialog, you assign an existing certificate to one or more devices.

##### How to access this function

1. Right-click on the list entry of a certificate.
2. Select the "Assign" command from the shortcut menu.
3. The "Assign certificate with ID x to device" dialog opens.
4. Define how the certificate is to be assigned by making a selection for "Used as":

   - Device certificate (not specified): e.g. for Secure OUC or blocks
   - Device certificate: Web server certificate.
   - Trusted certificate: e.g. OPC UA

   A certificate can be assigned to devices as a device certificate and to others as a trusted certificate. Only one certificate per device can be used as the device certificate.

#### Create/renew certificates

##### Renew certificate

In this dialog, you renew CA certificates and device certificates. The function is not valid for imported certificates.

##### Create certificate

In this dialog, you can manually create certificates. This function is useful, for example, when you have accidentally deleted a certificate generated by STEP 7. You can then assign the created certificate to the desired device, see section [Assigning certificates](#assigning-certificates).

##### How to access this function

1. For renewal: Right-click on a list entry in the certificate manager and select the "Renew" command from the shortcut menu.

   For creation: Right-click on an empty row in the certificate manager and select the "Create" command from the shortcut menu.
2. Select the usage:

   - Usage: Value that is entered in the "KeyUsage" extensions of the standard X.509 V3 for digital certificates.
   - Key Usage: Value that is entered in the "ExtendedKeyUsage" extensions of the standard X.509 V3 for digital certificates.
3. Decide whether or not the new certificate will be self-signed or signed by a certificate authority.
4. If the certificate is to be signed by a certificate authority, select the certificate authority to be used with the "Select" button. Only certification authorities that are stored in the certificate store of the current project and have a private key can be selected. See section [Overview of certificates](#overview-of-certificates).
5. Depending on the certificate, enter the following parameters in the corresponding input fields:

| Parameter | Meaning |
| --- | --- |
| Certificate owner | Holder of the certificate. The value for the certificate owner may contain a maximum of 64 characters (with ID). |
| Cipher | Select the encryption method.  Observe the section "Changing the cipher". |
| Key length | Selection depending on cipher.  Fixed code length in bits for RSA: 2048  ECC curve for EC: prime256k1 or secp384r |
| Hash algorithm | Algorithm used for signing the certificate. |
| Valid from | The validity period of the certificate |
| Valid to |  |
| Subject alternative name (SAN) | Depending on the certificate to be renewed, the subject alternative name is displayed with an adaptable name type (e.g. IP address of the used interfaces) and value (e.g. URI of the OPC UA server). |

##### Changing the cipher

> **Note**
>
> **Cipher "EC" only valid for TIM 1531 IRC as of V2.1**
>
> By default, the cipher "RSA" is set for all devices.
>
> You can set the cipher "EC" for all devices, but the method is only valid for the TIM 1531 IRC as of V2.1. For all other devices, an error message appears after compilation.

Proceed as follows to change the cipher:

1. Select the device certificate.
2. Select the "Renew" shortcut menu command.
3. In the "Renew certificate" dialog, select the "Self signed" option.
4. As cipher, select the entry "EC" and choose the algorithm and hash algorithm.

> **Note**
>
> **Encryption parameter "secp256K1" invalid**
>
> You can select the encryption parameter "secp256k1" but will receive an error message after compilation because the parameter is invalid.

Result:

- During compilation, the certificate with the configured settings is assigned to the device.
- In the certificate parameters of the "Renew certificate" dialog, "EC" is now displayed as encryption method.

#### Replacing certificates

##### Meaning

In the "Replace certificate" dialog replace an existing certificate with a new one.

Please note that a CA certificate can only be replaced by a CA certificate and a device certificate can only be replaced by a device certificate.

When replacing a single certificate, the signature is not updated.

##### How to access this function

1. Right-click on the list entry of a certificate.
2. Select the "Replace" entry in the shortcut menu.
3. The "Replace certificate" dialog opens.

All certificates listed in the "Certificates involved" table are derived once again. This means that the CA group certificate of an already configured VPN group can be replaced in the project by the CA group certificate of a different project. The VPN device certificates for the VPN group members are therefore derived from the same CA group certificate in both projects.

After making changes in the certificate manager, download the configuration to all security modules affected.

#### Telecontrol: Handling certificates for TLS

##### Secure communication with telecontrol modules

The communication via TLS described below is supported by the following modules:

- TIM 1531 IRC V2.3 as of firmware version V2.3
- CPU 1500 as of firmware version V2.9
- CP 1542SP-1 IRC as of firmware version V2.2
- CPU 1500 SP as of firmware version V2.9

The communications modules use TLS 1.2; communication complies with IEC/TS 62351-3.

##### Communication between CPU and telecontrol module

**CP: Communication via backplane bus**

If the CPU and telecontrol CP are in the same rack, communication between them runs via the backplane bus. The CPU is automatically assigned to the telecontrol CP.

**TIM 1531 IRC: TLS communication with the CPU via Ethernet**

The TIM 1531 IRC is not inserted in the rack of the CPU but in a separate rack. The connection to the CPU runs over Ethernet and uses secure communication via TLS for all usable telecontrol protocols.

For communication via TLS, you need to use a newly created CPU certificate and specify it to the TIM in the "Subscriber numbers" parameter group. When you create a certificate for the CPU and assign the TIM to the CPU, the certificate is entered automatically.

##### Creating the CPU certificate and assigning the CPU

**Requirements**

The following requirements must be met in order to create and assign certificates:

- As STEP 7 project user, you have at least the rights of the "NET Administrator" role.

  For more on this, see "Security settings > Users and roles > Assigned roles".
- The devices have the required minimum firmware version, see above.
- The configuration data of the CPU is protected.

  For more on this, see "Protection & Security > Protection of confidential PLC configuration data"

To be able to assign your local CPU to the TIM 1531 IRC, the following requirement must be met:

- CPU and TIM 1531 IRC are networked.
- The desired telecontrol protocol is enabled for the TIM under "Communication types".

**Certificates of SIMATIC NET devices**

SIMATIC NET communications modules generally use the global certificate manager. You can find this in the project navigation under "Security settings > Security features".

**Creating the certificate of the CPU**

First, you need to create a certificate generated by the system (global certificate manager of the STEP 7 project) for the CPU. The locally created certificate of the CPU cannot be used for communication.

When the CPU is assigned to the TIM (see below), the ID of the newly created CPU certificate is automatically entered at the following locations:

- In the "Subscriber numbers" dialog of the TIM
- In the certificate manager of the TIM as partner certificate

Proceed as follows to create the CPU certificate:

1. For the CPU, select the parameter group "Protection & Security > Certificate manager > Global security settings".
2. Enable the "Use global security settings for certificate manager" option.

   Note:  
   When the option is enabled, existing CPU certificates are deleted.
3. Go to "Protection & Security > Connection mechanisms > Communication to TIA Portal and HMI".
4. In the "PLC communication certificate" row, right-click on the icon for the drop-down list.
5. Click "Add" under the open drop-down list.

   The "Create certificate" dialog opens with the following options, among others:

   - Usage: TLS Client / Server
   - Certificate authority (CA): Signed by certification authority
   - Common name of subject: Name of the selected CPU
   - Encryption method: EC
   - Hash algorithm: sha256

   If necessary, you can add another address type for the CPU under "Subject Alternative Name (SAN)".
6. Retain the settings and click "OK".

   The newly created TLS certificate is shown in the device certificate table with the "TlsServer" service for the CPU.
7. Open the global certificate manager in the project navigation:

   "Security settings > Security features > Certificate manager > Device certificates"
8. Select the newly created certificate of the CPU (see above for ID) and open the "Assign" shortcut menu.
9. In the list, select the TIM to which the CPU should be assigned.
10. In the "Used as" row in the ("Not assigned") cell, select the "Trusted certificate" option and click on the green checkmark.
11. Close the dialog with OK.

**Assign CPU to TIM 1531 IRC**

1. For the TIM that is to communicate with the CPU, open the "Subscriber numbers" parameter group.
2. Right-click on the icon for the drop-down list in the "Assigned CPU" row.

   The list of networked CPUs opens.
3. Select the CPU to be assigned to the TIM and click on the green checkmark below it.

   The name of the CPU is displayed in the "Assigned CPU" row.

   At the same time, the ID of the certificate created previously for the CPU is automatically displayed in the "Communication certificate" row.

**Further configuration**

Then configure the other stations as communication partners and the corresponding telecontrol connections.

##### TLS for telecontrol connections

**TLS for project-internal telecontrol connections**

You can configure secure communication via TLS for telecontrol connections of communications modules that use one of the following protocols:

- IEC 60870-5
- DNP3

You configure secure communication for the telecontrol connections ("TeleControl" task card).

1. First create the telecontrol connections.
2. Select the main connection and the "Secure Communication (TLS)" parameter group there.
3. Activate the "Enable secure communication" option.

When all certificates of the connection partners are present, the own certificate ID and the partner certificate ID are automatically applied to the entire connection, including sub-connections, for Siemens devices.

**TLS for telecontrol connections with third-party devices**

If you want to use secure communication via TLS for telecontrol connections with third-party devices, you need to perform some additional steps.

You need to create a certificate for the third-party device, apply the ID to the connection parameters, export the certificate and the associated CA certificate, and import it into the third-party device.

First create the connection as described above and then activate the "Enable secure communication" option. Proceed as follows.

**Importing a third-party certificate or creating and assigning it**

Alternatively, you can make the third-party certificate available to the STEP 7 project:

- Import

  If required, you can save and import the certificate of the third-party device in the file system of the engineering station.

  To import, open the "Trusted certificates and root certification authorities" tab in the global certificate manager, click in a free row and open the "Import" shortcut menu.

  You then need to assign the imported certificate to the TIM (see below).
- Create

  Alternatively, you can create a certificate for the third-party device in STEP 7 and import it into the third-party device.

  Follow these steps:

1. Open the global certificate manager in the project navigation:

   "Security settings > Security features > Certificate manager > Device certificates"
2. Click on the "Create" shortcut menu in a free row.

   The "Create certificate" dialog opens.
3. Select the following options for the certificate of the third-party device:

   - Usage: TLS Client / Server
   - Certificate authority (CA): Self signed
   - Common name of subject: Enter the name of the third-party device.

   Adapt the other parameters to the functionality of the third-party device.

   The following are possible, for example:

   - Encryption method: RSA
   - Key length: 2048
   - Hash algorithm: sha256
4. Click "OK" to close the dialog.

   The certificate appears in the table.

   You will need the certificate ID for the assignment and the telecontrol connection.
5. Select the newly created certificate and open the "Assign" shortcut menu.
6. In the list, select the TIM with which the third-party device should communicate via the telecontrol connection.
7. In the "Used as" row in the ("Not assigned") cell, select the "Trusted certificate" option and click on the green checkmark.
8. Close the dialog with OK.

   You will need the certificate ID for the telecontrol connection.

**Exporting a certificate for a third-party device and importing it**

When you have imported the device certificate of the third-party device, you only need to export the device certificate of the TIM and the associated CA certificate.

If you have created the device certificate of the third-party device in STEP 7, you also have to export this.

Follow these steps:

1. Device certificate for the third-party device created in STEP 7

   - In the global certificate manager, open the "Trusted certificates and root certificate authorities" tab.
   - Select the device certificate for the third-party device and click the "Export certificate" shortcut menu.
   - Save the certificate in the file system of the engineering station.

     You can change the default file format "*.der".

     You can find a description of the functions of the certificate file formats in the "Exporting certificates" section in the help system.
2. Device certificate of the TIM

   - In the global certificate manager, switch to the "Device certificates" tab.
   - Select the device certificate of the TIM as partner certificate for the third-party device.
   - Make the "Issuer" column fully visible.

     You need the name of the issuer to export the issuing CA certificate.
   - Export the selected device certificate of the TIM via the "Export certificate" shortcut menu.
3. Issuing CA certificate

   - Change to the "Certificate authority (CA)" tab.
   - Select the CA certificate that is issuer for the device certificate of the TIM.

     When you expand the CA certificate, all derived device certificates are displayed below it, including that of the TIM.
   - Export the selected CA certificate via the "Export certificate" shortcut menu.
4. For communication during runtime, export all saved certificates into the third-party device or its configuration tool.

**Entering the certificate ID in the telecontrol connection**

1. Switch back to the created telecontrol connection, parameter group "Secure Communication (TLS)".
2. Enter the following values manually for connection with a third-party device:

   - Partner certificate ID: ID of the imported or manually created certificate for the third-party device
   - Own certificate ID: ID of the TIM certificate

Continue with the configuration of the other parameters.

### Special features of user management for security functions

#### Access to security functions

You can only access security functions after activating project protection and after a user has successfully logged on. The logged on user must also have the required engineering and runtime rights.

You will find basic information on user management in STEP 7 in the "Using user management" section of the information system.

#### Engineering rights for security modules

These engineering rights allow diagnostics and configuration of security modules:

- View security device configuration: Display of the global security functions and the local security settings of the security modules.
- Edit security device configuration: Configuration of the global security functions and the local security settings of the security modules and perform diagnostics of the security modules.
- Edit hardware configuration: Edit the hardware configuration of all devices in the project. For more information, refer to section "Function rights in the user administration" of the information system.

#### Roles with runtime rights for security modules

As default, the system-defined roles with the prefix "NET" are assigned runtime rights for security modules. Runtime rights provide the rights to execute certain tasks on security modules, for example for diagnostics or updating firmware. To be able to perform these tasks, you must assign your user a suitable system-defined role with the prefix "NET" or a user-defined role with the relevant runtime rights. Just as with engineering rights you cannot change runtime rights for system-defined roles. For user-defined roles you can change the runtime rights as required. You can specify the runtime rights of a user-defined role for each security module.

At least one user must be available who has been assigned a role with full runtime rights for a security module, for example, the system-defined "NET Administrator" role.

The system-defined roles with the prefix "NET" are assigned engineering rights:

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| Open the project read only | **x** | **x** | **x** |
| Open the project with write rights | **x** | **x** | - |
| Edit security settings: "Settings" and "Users and roles" | **x** | - | - |
| View security device configuration | **x** | **x** | **x** |
| Edit security device configuration | **x** | **x** | - |

#### Runtime rights for security modules

Depending on the security module, the following runtime rights are available for selection:

All tables
Runtime rights CP 343-1 Advanced / CP 443-1 Advanced
Runtime rights CP 443-1 OPC UA
Runtime rights CP 1628
Runtime rights SCALANCE S-600 V4
Runtime rights CP 1543-1
Runtime rights CP 1542SP-1 IRC
Runtime rights CP 1543SP-1
Runtime rights CP 1243-1
Runtime rights CP 1242-7
Runtime rights CP 1243-7 LTE
Runtime rights CP 1243-8 IRC

Runtime rights CP 343-1 Advanced / CP 443-1 Advanced

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| FTP: Read files from the CP file system | **x** | **x** | **x** |
| FTP: Write files to the CP file system | **x** | **x** | - |
| Web server: Format CP file system * | **x** | - | - |
| Applets: Read values via PLC tags * | **x** | **x** | **x** |
| Applets: Read values via addresses * | **x** | **x** | **x** |
| Applets: Write values via addresses * | **x** | **x** | - |
| FTP: Read files (DBs) from the S7 CPU ** | **x** | **x** | **x** |
| FTP: Write files (DBs) to the S7 CPU *** | **x** | **x** | - |
| Applets: Read status of the modules in the rack * | **x** | **x** | **x** |
| Applets: Read article numbers of the modules in the rack * | **x** | **x** | **x** |
| Applets: Write values via PLC tags * | **x** | **x** | - |
| SNMP: Read MIB-II | **x** | **x** | **x** |
| SNMP: Write MIB-II | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| SNMP: Read LLDP MIB | **x** | **x** | **x** |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| Web server: Expand IP access control list * | **x** | **-** | - |
| Web server: Access Web diagnostics and CP file system | **x** | **x** | **x** |
| Web server: Send test e-mails * | **x** | **x** | **x** |
| Web server: Update firmware * | **x** | **x** | - |
| SNMP: Read MRP MIB | **x** | **x** | **x** |
| SNMP: Write MRP MIB | **x** | **x** | **-** |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |
| Web server: Load diagnostics texts later * | **x** | **x** | - |

Runtime rights CP 443-1 OPC UA

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| SNMP: Read MIB-II | **x** | **x** | **x** |
| SNMP: Write MIB-II | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| SNMP: Read LLDP MIB | **x** | **x** | **x** |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| Web server: Update firmware | **x** | **x** | - |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |
| Web server: Load diagnostics texts later | **x** | **x** | - |
| OPC UA: Read tags | **x** | **x** | **x** |
| OPC UA: Write tags | **x** | **x** | - |
| Web server: Diagnostics | **x** | **x** | **x** |

Runtime rights CP 1628

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| SNMP: Read MIB-II | **x** | **x** | **x** |
| SNMP: Write MIB-II | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |

Runtime rights SCALANCE S-600 V4

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| SNMP: MIB-II read | **x** | **x** | **x** |
| SNMP: MIB-II write | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| SNMP: Read LLDP MIB | **x** | **x** | **x** |
| Download the configuration files | **x** | **x** | - |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| Web server: Update firmware | **x** | **x** | - |
| SNMP: MRP-MIB read (only for SCALANCE S627-2M) | **x** | **x** | **x** |
| SNMP: MRP-MIB write (only for SCALANCE S627-2M) | **x** | **x** | - |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |

Runtime rights CP 1543-1

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| FTP: Read files from the CP file system | **x** | **x** | **x** |
| FTP: Write files to the CP file system | **x** | **x** | - |
| FTP: Read files (DBs) from the S7 CPU ** | **x** | **x** | **x** |
| FTP: Write files (DBs) to the S7 CPU *** | **x** | **x** | - |
| FTP: FTP client access | **x** | - | - |
| FTP: FTPS client access | **x** | - | - |
| SNMP: Read MIB-II | **x** | **x** | **x** |
| SNMP: Write MIB-II | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| SNMP: Read LLDP MIB | **x** | **x** | **x** |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |
| SNMP: Read IPv6 MIB | **x** | **x** | **x** |

Runtime rights CP 1542SP-1 IRC

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| SNMP: Read MIB-II | **x** | **x** | **x** |
| SNMP: Write MIB-II | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |
| SNMP: Read IPv6 MIB | **x** | **x** | **x** |
| Use TeleService | **x** | - | - |

Runtime rights CP 1543SP-1

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| SNMP: Read MIB-II | **x** | **x** | **x** |
| SNMP: Write MIB-II | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| SNMP: Read LLDP MIB | **x** | **x** | **x** |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |
| SNMP: Read IPv6 MIB | **x** | **x** | **x** |

Runtime rights CP 1243-1

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| SNMP: Read MIB-II | **x** | **x** | **x** |
| SNMP: Write MIB-II | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |
| SNMP: Read IPv6 MIB | **x** | **x** | **x** |
| Use TeleService | **x** | - | - |

Runtime rights CP 1242-7

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| Use TeleService | **x** | - | - |

Runtime rights CP 1243-7 LTE

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| Use TeleService | **x** | - | - |

Runtime rights CP 1243-8 IRC

| Right | NET Administrator | NET Standard | NET Diagnose |
| --- | --- | --- | --- |
| SNMP: Read MIB-II | **x** | **x** | **x** |
| SNMP: Write MIB-II | **x** | **x** | - |
| SNMP: Read automation MIB | **x** | **x** | **x** |
| TIA Portal: Perform diagnostics of the security module | **x** | **x** | **x** |
| SNMP: Read SNMPv2 MIB | **x** | **x** | **x** |
| SNMP: Read IPv6 MIB | **x** | **x** | **x** |

| Symbol | Meaning |
| --- | --- |
| * | To be able to use the function, the runtime right "Web server: Access Web diagnostics and CP file system" must be enabled as well. |
| ** | To be able to use the function, the runtime right "FTP: Read files from CP file system" must be enabled as well. |
| *** | To be able to use the function, the runtime right "FTP: Write files to CP file system" must be enabled as well. |

#### Configuration limits for users and roles on security modules

- Maximum number of users on one security module:

  The maximum number of users assigned a role with runtime rights for a security module is 33 (32 + 1 administrator when creating the project).
- Maximum number of roles on one security module:

  The maximum number of roles that are assigned runtime rights for a security module and that are assigned to users is 37.

#### Parameters for user-specific IP rule sets

When using user-specific IP rule sets, note the following parameters of user management:

- Authentication method "RADIUS" (only for SCALANCE S as of V4):

  The authentication of the user is performed by a RADIUS server when user-specific IP rule sets are activated. The password of the user is not configured in STEP 7 when using this authentication method but must be stored on the RADIUS server. Only use this authentication method for users that only need to log on to the Web page of a security module. A user with the "RADIUS" authentication method cannot log on to STEP 7 projects.

### Authentication using a RADIUS server

#### Module-specific function

This function is available only for SCALANCE S V4 modules or higher, refer to:

[Authentication using a RADIUS server](#authentication-using-a-radius-server-1).

### Generating configuration data for SCALANCE M modules

#### Meaning

You can generate the VPN information for the assignment of parameters to a SCALANCE M using STEP 7. For this to be possible, the module must be in at least one VPN group with a security module or a SOFTNET Security Client. With the generated files, you can then configure the SCALANCE M using the Web Based Management of the device.

#### Generated files

The following file types are generated:

- Export file with the configuration data

  - File type: *.txt file in ASCII format
  - Contains the exported configuration information for the SCALANCE M including information on the additionally generated certificates.
- VPN group certificates of the module

  - File type of the private key: *.p12 file
  - The file contains the module certificate and the key material.
  - Access is password protected.
- CA certificates of VPN groups

  - File type: *.cer file

![SCALANCE M configuration file](images/52280466571_DV_resource.Stream@PNG-de-DE.png)

SCALANCE M configuration file

> **Note**
>
> **No transfer to the SCALANCE M module**
>
> Configuration files are not transferred to the SCALANCE M module. An ASCII file is generated with which you can configure the VPN-relevant properties of the SCALANCE M. To allow this, the SCALANCE M must be located in at least one VPN group with another security module or a SOFTNET security client.

> **Note**
>
> **Protecting exported configuration files from unauthorized access**
>
> Configuration files for SCALANCE M exported from STEP 7 can contain security related information. You should therefore make sure that these files are protected from unauthorized access. This is particularly important when passing on the files.

#### Follow the steps below

1. Select the module of the type "SCALANCE M".
2. In the local security settings, select the entry "SCALANCE M configuration".
3. Select the "Generate SCALANCE M files" check box and select a storage location for the configuration files.
4. Specify a password for the encryption of the VPN group certificate by using the project name as the password or assigning a password of your own.
5. Compile the configuration of the SCALANCE M module.

Result: The files (.txt file and certificates) are stored in the folder you specify.

### Generating configuration data for security devices

#### Meaning

A security device serves as substitute for a device from another manufacturer.

V1.0: The device can only be operated as a VPN device.

V1.1 or higher: You can choose whether the device is operated as VPN device or Internet gateway.

#### Security device as VPN device

You can generate the VPN information for the assignment of parameters to a VPN device using STEP 7. For this to be possible, the VPN device must be in at least one VPN group with a security module. With the generated files, you can then configure the VPN device.

> **Note**
>
> **Protecting exported configuration files from unauthorized access**
>
> Configuration files for VPN devices exported from STEP 7 can contain security related information. You should therefore make sure that these files are protected from unauthorized access. This is particularly important when passing on the files.

To use the security device as VPN device, proceed as follows:

1. Select the security device to be edited.
2. Select the "Settings" entry in the local security settings.
3. V1.1: Select the "VPN device" mode from the drop-down list. "VPN device" is preset for V1.0.
4. Select the "VPN device" entry in the local security settings.
5. Select the "Generate files of the VPN device" check box.
6. Select the mode of the VPN device from the "VPN mode" drop-down list. This selection is only possible when the VPN device is located in a VPN group.

   - VPN client: The VPN device can adopt the following role:   
     Initiator The VPN device actively attempts to establish a VPN connection to the partner.
   - VPN server: The VPN device can adopt the following roles:   
     Initiator/Responder: The VPN device actively attempts to establish a VPN connection to the partner. The receipt of requests for VPN connection establishment is also possible. This role is selected as default in the VPN connection properties.  
     Responder: The receipt of requests for VPN connection establishment is possible.
   - NCP VPN client for Android (as of version 2.1): The VPN device with installed software NCP Secure VPN Client for Android actively attempts to establish a VPN connection to the partner.
   - SOFNET Security Client V5: The VPN device with installed SSC software actively attempts to establish a VPN connection to a partner.
   - SINEMA RC client: The VPN device with installed SINEMA RC client software actively attempts to establish a VPN connection to a partner.
7. Select a storage location for the VPN configuration files.
8. Specify a password for the encryption of the VPN group certificate by using the project name as the password or assigning a password of your own.

If you have configured the VPN device as a "VPN client":

1. Specify the corresponding file types in the "Exported certificates and keys" entry.
2. In the entry "Subnets reachable through tunnel", enter the subnets and/or IP addresses for which tunnel communication will be enabled.

If you have configured the VPN device as a "VPN server":

1. In the "VPN server address (WAN IP address)" box, enter the WAN IP address at which the VPN server can be reached by the initiator of the VPN connection.
2. Specify the corresponding file types in the "Exported certificates and keys" entry.
3. In the entry "Subnets reachable through tunnel", enter the subnets and/or IP addresses for which tunnel communication will be enabled.

If you have configured the VPN device as an "NCP VPN client for Android (as of version V2.1)":

1. In the "NCP VPN client for Android settings" entry, enter the storage path on the NCP VPN client.

**Note**

**Releasing subnets and subscribers with a VPN connection between NCP secure VPN client and SCALANCE S**

The local internal subnet of SCALANCE S modules is released for tunnel communication as default. For this reason, this is always entered as the first released subnet in the file generated for the NCP VPN client. Because the NCP VPN client supports a maximum of 5 entries for released subnets / subscribers, the local internal network of the SCALANCE S module and the first 4 table entries from the "Nodes" entry in the NCP VPN client are released by default. To release other subnets and subscribers for tunnel communication, the file generated by STEP 7 must be suitably adapted.

If you have configured the VPN device as a SOFTNET Security Client V5:

- No additional settings are required.

If you have configured the VPN device as a SINEMA RC client:

1. Select the file to start the SINEMA RC client via the "Search" button.
2. You open the SINEMA RC client with the "Start SINEMA RC client" button.

   No VPN configuration file is created for the SINEMA RC client.

#### Security device as Internet gateway

To use the security device as Internet gateway, proceed as follows:

1. Select the security device to be edited.
2. Select the "Settings" entry in the local security settings.
3. Select the "Internet gateway" mode from the drop-down list.
4. Select the "Internet gateway" entry in the local security settings.
5. Enter the WAN IP address or the FQDN.
6. Via the "Assigned modules" entry, you can assign modules located in a VPN group to the Internet gateway.

### Setting up a firewall

This section contains information on the following topics:

- [Overview of the firewall](#overview-of-the-firewall)
- [Firewall zones](#firewall-zones)
- [Global firewall rule sets](#global-firewall-rule-sets)
- [Local firewall](#local-firewall)
- [IP addresses in IP packet filter rules](#ip-addresses-in-ip-packet-filter-rules)

#### Overview of the firewall

##### Meaning

The firewall functionality of the security modules is intended to protect networks and stations from third-party influence and interference. This means that only certain, previously specified communications relations are permitted. The firewall discards invalid frames without sending a response.

To filter the data traffic, IP addresses, IP subnets, services or MAC addresses can be used. You can also set a limit fro the transmission speed.

The firewall functionality can be configured for the following protocol levels:

- IP firewall with stateful packet inspection (layer 3 and 4)
- Firewall also for Ethernet "non-IP" frames according to IEEE 802.3 (layer 2)

With security modules capable of VPN, the firewall can also be used for the encrypted data traffic (IPsec tunnel). With the SCALANCE S602 Security module, the firewall can only be used for unencrypted data traffic.

##### Firewall rules

Firewall rules describe which packets in which direction are permitted or forbidden. IP rules affect all IP packets of layer 3 or higher. MAC rules only affect frames lower than layer 3.

##### Types of firewall rules

- Global firewall rule sets: Global firewall rule sets can be assigned to several security modules at the same time. Global firewall rule sets are configured in the global security functions.
- Local firewall rules: Local firewall rules are configured in the local security settings of a security module.
- User-specific IP rule sets (only for SCALANCE S): User-specific IP rule sets can be assigned to individual or several security modules at the same time. User-specific IP rule sets are configured in the global security functions and assigned there to one or more users.

  SCALANCE S (RADIUS): User-specific IP rule sets can be assigned individual or multiple users as well as individual or multiple roles.

##### Service definitions

With the aid of service definitions, you can also define firewall rules clearly in a compact form. Service definitions are configured in the global security functions and can be used in the global, local and user-specific firewall rules.

##### Adapting standard rules for IP services

For SCALANCE S modules, you can adapt service-specific firewall rules that are set by default for the interfaces of the security modules. You will find information on configuring these firewall rules in the section [Adapting standard rules for IP services](#adapting-standard-rules-for-ip-services).

##### Automatically generated firewall rules for CP connections

For connections that were configured using CPs, STEP 7 automatically creates firewall rules that allow communication with the partner of the CP in the specified direction (CP active/passive). The connection establishment directions are taken into account. To display these firewall rules, if the advanced firewall mode is enabled, the "Update connection rules" button needs to be clicked. The firewall rules are then displayed in advanced firewall mode.

Which firewall rules are generated automatically is described in the following sections.

- For S7-300 CPs/S7-400 CPs/PC CPs: [Connection-related automatic firewall rules](#connection-related-automatic-firewall-rules) in the section "Security for S7-300 / S7-400 / PC CPs".
- For S7-1200-/S7-1500-CPs: [Connection-related automatic firewall rules](#connection-related-automatic-firewall-rules-1) in the section "Security for S7-1200 / S7-1500 CPs".

##### Enabling the firewall

Firewall functionality for a specific security module is controlled in the local security settings using the "Enable firewall" check box. If the check box is enabled, the firewall can be configured and is effective following the download. For a security module that is a member of a VPN group, the "Enable firewall" check box is activated by default and cannot be deactivated. After switching to advanced firewall mode, it is not possible to switch back to standard mode. For more information about the standard and advanced firewall modes, refer to the section:

[Overview of local firewall rules](#overview-of-local-firewall-rules).

---

**See also**

[User-specific IP rule sets](#user-specific-ip-rule-sets)

#### Firewall zones

This section contains information on the following topics:

- [Assigning firewall zones](#assigning-firewall-zones)

##### Assigning firewall zones

###### Principle

Module families such as SCALANCE SC600 or SCALANCE M800 have zones, e.g. "Device" or "usb0", that are not represented in the global firewall rules. To make the zones available as additional firewall directions for "From" and "To" for firewall rule sets in the global editor, first assign them in the zone editor.

###### Overview

The table on the right shows all available firewall zones that are created in the local device settings under "Security > Firewall > IP Rules".

- **Name**

  Is taken from the local firewall settings and cannot be changed.
- **Defined by**

  - System: The zones are created automatically by the system.

In the left-hand table, you will see the firewall zones already assigned to global firewall rule sets.

- **Name**

  Is taken from the local firewall settings and cannot be changed.

  The zones added by default are:

  - INT (internal)
  - External (external)
  - DMZ (DMZ)
  - Tunnel (IPsec)

  **Defined by**

  - System: The zones are created automatically by the system.
- **Used in rule**

  Shows whether the zone is already used in a firewall rule. If so, the rules cannot be deleted.

  The zones created by default have the status "Always". They cannot be removed, even if they are not used in global firewall rules, because their mapping is represented via the known firewall directions internal/external/DMZ and tunnel.

###### Procedure

1. In the global security functions, select the entry "Firewall" > "Select firewall zones".
2. In the "Available zones" area, select the zones you want to assign to the left-hand side.
3. Click "<<" to assign the selected zone to the selected firewall zone.

###### Result

The firewall zone is available as global firewall rule and can be selected as direction "From" and "To" and assigned to a device.

Firewall rules that are not supported by a device because of an unsupported zone are filtered and a note is displayed.

Firewall rule sets containing zones can be exported and imported.

#### Global firewall rule sets

This section contains information on the following topics:

- [Overview of global firewall rule sets](#overview-of-global-firewall-rule-sets)
- [Global firewall rule sets - conventions](#global-firewall-rule-sets---conventions)
- [Creating global firewall rule sets](#creating-global-firewall-rule-sets)
- [Creating an IP rule set](#creating-an-ip-rule-set)
- [Creating a MAC rule set](#creating-a-mac-rule-set)
- [Assigning global firewall rule sets](#assigning-global-firewall-rule-sets)
- [Exporting and importing global firewall rule sets](#exporting-and-importing-global-firewall-rule-sets)
- [IP services](#ip-services)
- [MAC services](#mac-services)

##### Overview of global firewall rule sets

###### Application

Global firewall rule sets are configured independently of the module in the global security functions. A firewall rule set consists of one or more firewall rules and is assigned to the individual security modules.

In the global firewall rule sets, a distinction is made between the following:

- IP rule sets
- MAC rule sets

The following schematic illustrates the relationship between globally defined rule sets and locally used rule sets.

![Application](images/41733528843_DV_resource.Stream@PNG-en-US.png)

###### Configuring

When configuring global firewall rules, you can make detailed firewall settings. You can allow individual services for a single node or all services for the node for access to the station or network.

###### When are global IP and MAC firewall rules useful?

Global firewall rules are useful if you want to define identical filter criteria for communication with several security modules.

> **Note**
>
> **Assigning firewall rule sets with incompatible firewall rules**
>
> For a security module, only the firewall rules from firewall rule sets are adopted correctly if the security module supports them. A firewall rule contained in a global firewall rule set with the direction "From: External" or "To: Any" is, for example not assigned to a CP 1628. The other firewall rules of the global firewall rule set are adopted if the CP 1628 supports them.

##### Global firewall rule sets - conventions

###### Global firewall rule sets are used locally

The following conventions apply when creating a global set of firewall rules and when assigning it to a module:

- Configuration view

  Global firewall rule sets are configured in the global security functions.
- Priority

  As default, locally defined rules have a higher priority than the global IP and MAC firewall rule sets. Newly assigned global IP and MAC firewall rule sets are therefore initially entered at the bottom of the local rule list.

  The priority can be changed by changing the position in the rule list.
- Entering, changing or deleting rule sets

  Global firewall rule sets cannot be edited in the local rule list of the firewall rules in the module properties. They can only be displayed there and positioned according to the required priority.

  It is not possible to delete a single rule from an assigned rule set in the local security settings. Only the entire rule set can be removed from the local list of rules. The firewall rule sets in the global security functions remain unaffected.

##### Creating global firewall rule sets

###### How to access this function

1. In the global security functions, select the entry "Firewall > Global firewall rule sets > IP rule sets or MAC rule sets".  
   Result: The previously created IP rule sets or MAC rule sets are displayed under the selected entry.
2. Double-click on the entry "Add new IP rule set" or "Add new MAC rule set".  
   Result: The created firewall rule set is displayed with an automatically assigned number below the entry "IP rule sets" or "MAC rule sets".
3. Double-click on the created firewall rule set.  
   Result: In the working area the assignment dialog for firewall rule sets is displayed. The selected firewall rule set is selected in the "Rule set" drop-down list. The required security modules can be assigned to this, see section [Assigning global firewall rule sets](#assigning-global-firewall-rule-sets). In the local security settings, the configurable properties of the firewall rule set are displayed.
4. Enter the following data in the "General" entry in the local security settings:

   - Name: Project-wide, unique name of the rule set. The name appears in the local rule list of the security module after the rule set is assigned.
   - Description (optional): Enter a description of the global rule set.
5. In the local security settings in the entry "Firewall rule set" enter the firewall rules in the list.  
   Note the parameter description in the following sections:

   For IP rule sets: [Defining IP packet filter rules](#defining-ip-packet-filter-rules)

   For MAC rule sets: [Defining MAC packet filter rules](#defining-mac-packet-filter-rules)

   To switch over to the local security settings of another firewall rule set, select this from the "Rule set" drop-down list of the assignment dialog or double-click on the corresponding entry in the global security functions.

###### Result

You have created the global firewall rule set and can now assign this to the required security modules.  
Note the descriptions in the following section:

[Assigning global firewall rule sets](#assigning-global-firewall-rule-sets)

##### Creating an IP rule set

###### Meaning

Firewall rule set: Parameter

| Parameter | Meaning/comment | Available options / ranges of values |
| --- | --- | --- |
| Action | Allow/disallow (enable/block) | - Accept   Allow frames according to definition. - Drop   Block frames according to definition. - Reject   The frames are rejected, and the sender receives a corresponding message.  For firewall rules generated automatically as result of configuring a connection and subsequently adapted manually:  - Accept* - Drop*   If you change automatically created connection rules, when the "*" option is selected they are not recreated and overwritten by STEP 7. |
| From / To | Selection of the communication directions for which the rule will apply. | Described in separate sections.  - For SCALANCE S modules: [IP packet filter directions SCALANCE S](#ip-packet-filter-directions-scalance-s) - For S7-300-/S7-400-/PC CPs: [IP packet filter directions S7-300-/S7-400-/PC-CPs](#ip-packet-filter-directions-s7-300-s7-400-pc-cps) - For S7-1200-/S7-1500 CPs: [IP packet filter directions S7-1200 / S7-1500 CPs](#ip-packet-filter-directions-s7-1200-s7-1500-cps)   The communication direction "Station" includes access to the CP and access to the CPU via the CP.  The communication direction "Any" includes all the firewall directions supported by the security module at the time of loading.  The communication directions "Station", "Backplane bus" (only for CP 1543-1 as of V2.1 with the option "IP routing between communications modules") and "Tunnel" are classified as trusted by default. For communication between trustworthy directions no firewall rules need to be configured.  If you need additional directions via VLANS (zones), create them for the SCALANCE S615, SC600, M800 devices in the editor for firewall zones, see [Assigning firewall zones](#assigning-firewall-zones). |
| IPv6 | If this check box is selected, you can use a previously defined ICMPv6 service in the firewall rule. For some security CPs, after selecting the check box you can enter additional IPv6 addresses in the "Source IP address" and "Destination IP address" text boxes. | The check box can only be selected and deselected if there are no entries in the "Source IP address" and "Destination IP address" text boxes.  If IPv6 is disabled in the local settings of a CP capable of IPv6, you cannot select the "IPv6" check box in the local security settings of the CP and therefore cannot use ICMPv6 services or IPv6 addresses in firewall rules. Existing firewall rules that use IPv6 are shown grayed out if IPv6 is disabled. |
| Source IP Address | The firewall rule is applied to the frames with a sender that has the IP address specified here. If you do not specify an IP address, the firewall rule applies to all nodes in the communication direction you selected in the "From" column. | You can find additional information about IP addresses in the section [IP addresses in IP packet filter rules](#ip-addresses-in-ip-packet-filter-rules).     **Configuration options in ghost mode (only for SCALANCE S S602 as of V3.1):**   If ghost mode is activated, the IP address of the internal node is dynamically determined by the security module at runtime. Depending on the selected direction, you can select one of the following options in the column "Source IP address" (for direction "From internal to external") or in the column "Destination IP address" (for direction "From external to internal"):  - IP address of the internal node: The IP address of the internal node is inserted in the firewall rule by the SCALANCE S. - Limited broadcast: The broadcast IP address 255.255.255.255 is inserted in the firewall rule by the SCALANCE S. - Directed broadcast: The broadcast IP address of the SCALANCE S network is inserted in the firewall rule by the SCALANCE S. A directed broadcast can also be forwarded into the destination network via routers. - Multicast: The multicast address band 224.0.0.0 /24 is added to the firewall rule by the SCALANCE S. After selecting this option, a specific multicast IP address from the multicast address band can be specified as an alternative. |
| Destination IP address | The firewall rule is applied to the frames with a recipient that has the IP address specified here. If you do not specify an IP address, the firewall rules applies to all nodes in the communication direction you selected in the "To" column. |  |
| Service | Selection of the IP/ICMP service or the service group to be used.  Note: Before using a predefined service make sure that its predefined parameters meet your requirements. Pay particular attention to the predefined source and destination ports. | When selected, a window opens in which all pre-defined and configured IP services, ICMP services and service groups are displayed. These are managed in the global security functions under "Firewall > Services > Define services for IP rules". |
| Transmission speed (Mbps) | Limitation of the transmission speed  Can only be set if "Accept" is selected as action.  A packet passes through the firewall if the Accept rule applies and the permitted transmission speed for this rule has not yet been exceeded. | CP 343-1 Adv. / CP 443-1 Adv., S7-1200-/S7-1500-CPs, CP 1628: 0.001 ... 100 Mbps  SCALANCE S: 0.001 ... 1000 Mbps  For global and user-specific rules: 0.001 ... 1000 Mbps  For IP rules with the direction "Backplane bus": 0.001 ... 1 Mbps  Note: If the direction "From tunnel to station" is configured in a firewall rule for the S7-1200/S7-1500 CPs, no transmission speed limitation can be specified.  For CP 1543-1 V2.1 only one transmission speed can be specified if "Any" is configured for one of the two directions. This does not apply to the combination of directions "Any" and "Station". |
| Logging | Enable and disable logging for this rule. If logging is enabled, the settings for the packet filter logging configured in the local security settings apply. | - Enabled - Disabled (default) |
| Number | Automatically assigned number for the rule. The numbers are recalculated when rules are moved. |  |
| Stateful | If this check box is cleared for an IP rule with the "Accept" action, no firewall states are generated by packets to which the Accept rule applies. Firewall states automatically allow the responses to allowed packets.  Can only be adapted if "Accept" is selected as action. Configuration of IP rules without firewall states is only possible for SCALANCE S modules as of firmware V3. If the responses to packets that have passed the firewall according to such IP rules should also be allowed, additional IP rules need to be configured for these responses. | For Accept rules of SCALANCE S ≥ V3:  - enabled (default) - Disabled     For Accept rules of SCALANCE S < V3 and CPs:  - enabled (default)   Note: The check box is not present for CPs; however, the activated option is always used implicitly for Accept rules of CPs.    For Drop rules:  - Disabled (default) |
| Comment | Space for your own explanation of the rule | If a comment is marked with "AUTO", it was created for an automatic connection rule. For rules you have created, entry of a comment is optional. |

Meaning of the entries in the shortcut menu

| Entry in the shortcut menu | Meaning |
| --- | --- |
| Insert rule above | Use this command to insert a rule above the selected rule set. |
| Insert rule below | Use this command to insert a rule below the selected rule set. |
| Delete | This deletes the selected rule set.  Notes on removing a globally defined and locally assigned rule set:  If you delete a rule set here, this only cancels the assignment to the security module. |
| Move up | Use this button to move the selected rule set up one position in the list. As an alternative, you can move the selected rule set by dragging it with the mouse. You can select multiple entries.  The rule set you moved is therefore handled with a higher priority. |
| Move down | Use this button to move the selected rule set down one position in the list. As an alternative, you can move the selected rule set by dragging it with the mouse. You can select multiple entries.  The rule set you moved is therefore handled with a lower priority. |
| Define service for IP rules | This opens the dialog in which you can manage the IP services and service groups. |

##### Creating a MAC rule set

###### Meaning

MAC rule set: Parameter

| Parameter | Meaning/comment | Available options / ranges of values |
| --- | --- | --- |
| Action | Allow/disallow (enable/block) | - Accept   Allow frames according to definition. - Drop   Block frames according to definition. - Reject   The frames are rejected, and the sender receives a corresponding message.  For firewall rules generated automatically as result of configuring a connection and subsequently adapted manually:  - Accept* - Drop*   If you change automatically created connection rules, when the "*" option is selected they are not recreated and overwritten by STEP 7. |
| From / To | Selection of the communications directions for which the rule will apply. | Described in separate sections.  - For SCALANCE S modules: [MAC packet filter directions SCALANCE S](#mac-packet-filter-directions-scalance-s) - For S7-300-/S7-400-/PC CPs: [MAC packet filter directions S7-300-/S7-400-/PC-CPs](#mac-packet-filter-directions-s7-300-s7-400-pc-cps) - For S7-1200-/S7-1500 CPs: [MAC packet filter directions S7-1200 / S7-1500 CPs](#mac-packet-filter-directions-s7-1200-s7-1500-cps)   The communication direction "Station" includes access to the CP and access to the CPU via the CP.  As default, the communication directions "Station" and "Tunnel" are classified as being trustworthy. For communication between trustworthy directions no firewall rules need to be configured. |
| Source MAC address | The firewall rule is applied to the frames with a sender that has the MAC address specified here. If you do not specify a MAC address, the firewall rule applies to all nodes in the communications direction you selected in the "From" column. | MAC address in the correct format |
| Destination MAC address | The firewall rule is applied to the frames with a recipient that has the MAC address specified here. If you do not specify a MAC address, the firewall rule applies to all nodes in the communications direction you selected in the "To" column. |  |
| Service | Selection of the MAC service or the service group to be used.  Note: Before using a predefined service make sure that its predefined parameters meet your requirements. | The drop-down list box displays the predefined and configured services and service groups you can select. These are displayed in the global security functions under "Firewall" > "Services" > "Define services for MAC rules". |
| Transmission speed (Mbps) | Limitation of the transmission speed   Can only be entered if "Accept" is selected for the action.  A packet passes through the firewall if the Accept rule applies and the permitted transmission speed for this rule has not yet been exceeded. | CP 343-1 Adv. / CP 443-1 Adv., S7-1200-/S7-1500-CPs: 0.001 ... 100 Mbps  CP 1628 and SCALANCE S: 0.001 ... 1000 Mbps  For global rules: 0.001 ... 1000 Mbps  Note: If the direction "From tunnel to station" is configured in a firewall rule for the S7-1200/S7-1500 CPs, no transmission speed limitation can be specified. |
| Logging | Enable and disable logging for this rule. If logging is enabled, the settings for the packet filter logging configured in the local security settings apply. | - Enabled - Disabled (default) |
| Number | Automatically assigned number for the rule. The numbers are recalculated when rules are moved. |  |
| Comment | Space for your own explanation of the rule | If a comment is marked with "AUTO", it was created for an automatic connection rule. For rules you have created, entry of a comment is optional. |

Meaning of the entries in the shortcut menu

| Entry in the shortcut menu | Meaning |
| --- | --- |
| Insert rule above | Use this command to insert a rule above the selected rule set. |
| Insert rule below | Use this command to insert a rule below the selected rule set. |
| Delete | This deletes the selected rule set.  Notes on removing a globally defined and locally assigned rule set:  if you delete a rule set here, this only cancels the assignment to the security module. |
| Move up | Use this button to move the selected rule set up one position in the list. As an alternative, you can move the selected rule set by dragging it with the mouse. You can select multiple entries.  The rule set you moved is therefore handled with a higher priority. |
| Move down | Use this button to move the selected rule set down one position in the list. As an alternative, you can move the selected rule set by dragging it with the mouse. You can select multiple entries.  The rule set you moved is therefore handled with a lower priority. |
| Define service for MAC rules | This opens the dialog in which you can manage the IP services and service groups. |

##### Assigning global firewall rule sets

###### Requirement

You have enabled the advanced firewall mode for the security modules you want to assign to a firewall rule set.

###### Procedure

1. In the global security functions, select the entry "Firewall > Global firewall rule sets > Assign module to a firewall rule set".
2. From the "Rule set" drop-down list, select the rule set to which you want to assign the security module.

   In the right-hand table, you will see the security modules that you can assign to the selected firewall rule set. In the left-hand table, you will see the security modules already assigned to the selected firewall rule set.
3. In the "Available modules" area, select the security modules you want to assign to the selected rule set.
4. Click the "<<" button to assign the selected modules to the selected rule set.

###### Result

The global rule set is used by the assigned security modules as a local rule set and appears automatically at the end of the list of firewall rules in the local security settings.

##### Exporting and importing global firewall rule sets

###### Meaning and function

Global IP rule sets and global MAC rule sets can be exported from STEP 7 in the XLSX format and imported into STEP 7. Per firewall rule set an XLSX file is created when you export.

The export and import provides the option of exchanging firewall rule sets between different STEP 7 projects. Exported firewall rule sets can also be edited in Microsoft Excel® and then imported into STEP 7 again. This simplifies the making of mass changes.

Firewall rule sets exported from STEP 7 are largely compatible with the Security Configuration Tool (SCT). Firewall rule sets exported from from the Security Configuration Tool are fully compatible with STEP 7.

> **Note**
>
> **Restrictions when importing firewall rule sets from STEP 7 into the Security Configuration Tool**
>
> In SCT, IPv6 firewall rules and ICMPv6 services are not supported. During import firewall rules identified as IPv6 firewall rules and ICMPv6 services are ignored.
>
> As the transmission speed limit a maximum of 100 Mbps are permitted in SCT. During import firewall rules with more than 100 Mbps are ignored.

###### Exporting firewall rule sets from STEP 7

1. In the global security functions, select the entry "Firewall" > "Global firewall rule sets".
2. Double-click on the "Overview" entry.

   Result: The IP rule sets and MAC rule sets that exist in STEP 7 are displayed in the working area.
3. If you do not want to export all firewall rule sets, enable the check box of the firewall rule sets to be exported.
4. Click the ![Exporting firewall rule sets from STEP 7](images/77633738507_DV_resource.Stream@PNG-de-DE.png) button.
5. In the "Export firewall rule sets" dialog, select whether all firewall rule sets, only the selected firewall rule sets or all firewall rule sets supported by SCT will be exported. With the third option firewall rule sets containing firewall rules containing communication directions not supported by SCT are excluded from the export.
6. Enter a path on which the firewall rule sets will be saved and click the "Export" button.

   Result: Per firewall rule set an XLSX file was created. The XLSX files were named with the name of the corresponding firewall rule set and according to the date and time of the export.

###### Importing firewall rule sets in STEP 7

Exported firewall rule sets can be edited prior to importing them. Refer to the information in the section "Requirements for firewall rule sets to be imported".

Follow the steps outlined below to import firewall rule sets in STEP 7:

1. In the global security functions, select the entry "Firewall" > "Global firewall rule sets".
2. Double-click on the "Overview" entry.

   Result: The IP rule sets and MAC rule sets that exist in STEP 7 are displayed in the working area.
3. Click the ![Importing firewall rule sets in STEP 7](images/77633748363_DV_resource.Stream@PNG-de-DE.png) button.
4. If firewall rule sets of the same name are to be overwritten, select the "Overwrite existing firewall rule sets" check box.

   Note: For the comparison between the firewall rule sets existing in STEP 7 and the XLSX files, only the name of the firewall rule sets is used. The information about the date and time of the XLSX files is ignored.
5. Select the XLSX files to be imported. Multiple selection is possible.
6. Click the "Import" button.

   Result: The firewall rule sets of the selected XLSX files have been imported in STEP 7.

###### Structure of exported IP rule sets

For every IP rule set exported from STEP 7, an XLSX file is created with the following table sheets:

- IP Ruleset: Contains the IP packet filter rules of the IP rule set
- IP Services: Contains the IP services used in packet filter rules of the IP rule set. IP services in the IP service groups used are also displayed.
- ICMP Services: Contains the ICMP services used in packet filter rules of the IP rule set. ICMP services in the IP service groups used are also displayed.
- IP Service Groups: Contains the IP service groups used in IP packet filter rules of the IP rule set. The corresponding IP and ICMP services are displayed for every IP service group.

###### Structure of exported MAC rule sets

For every MAC rule set exported from STEP 7, an XLSX file is created with the following table sheets:

- MAC Ruleset: Contains the MAC packet filter rules of the MAC rule set
- MAC Services: Contains the MAC services used in MAC packet filter rules of the MAC rule set. MAC services in the MAC service groups used are also displayed.
- MAC Service Groups: Contains the MAC service groups used in MAC packet filter rules of the MAC rule set. The corresponding MAC services are displayed for every MAC service group.

###### Conventions for rule sets to be imported

The following conventions apply to firewall rule sets to be imported in STEP 7:

- The files have the file extension *.XLSX and the corresponding Office Open XML format.
- If the name of the XLSX file is longer than 128 characters, the rule set will be created in STEP 7 with a standard name.
- The names of the columns within the table sheets must not be changed, the order of the columns may, however, be changed.
- The names of the table sheets must not be changed, the order of the table sheets may, however, be changed.

###### Permitted parameter values for IP rule sets to be imported

The following values may be entered in the table columns of XLSX files for IP rule sets. Upper and lower case characters are not taken into account when the notation is checked.

Permitted parameter values for table sheet "IP Ruleset"

| Action | From | To | IPv6* | Source IP address | Destination IP Address | Service | Bandwidth | Logging | Stateful | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| - Accept - Drop - Reject | External | - Internal - DMZ - Tunnel - Any - Station - Backplane | - True - False | [free text with max. 255 characters] | [free text with max. 255 characters] | [free text with max. 128 characters] | [Possible values: 0.001…1000] | - True - False | - True - False | [free text with max. 255 characters] |
| Internal | - External - Internal - DMZ - Tunnel - Any - Station |  |  |  |  |  |  |  |  |  |
| DMZ | - External - Internal - Tunnel - Any |  |  |  |  |  |  |  |  |  |
| Tunnel | - External - Internal - DMZ - Tunnel - Any - Station - Backplane |  |  |  |  |  |  |  |  |  |
| Any | - External - Internal - DMZ - Backplane |  |  |  |  |  |  |  |  |  |
| Station | - External - Internal - Tunnel - Backplane |  |  |  |  |  |  |  |  |  |
| Backplane | - Any - External - Station - Tunnel |  |  |  |  |  |  |  |  |  |
| * This column is optional. If the column does not exist when importing into STEP 7, the default value "False" is used in STEP 7. |  |  |  |  |  |  |  |  |  |  |

Permitted parameter values for table sheet "IP Services"

| Name | Protocol | Source Port | Destination Port |
| --- | --- | --- | --- |
| [free text with max. 128 characters] | - UDP - TCP - All | [free text with max. 32 characters] | [free text with max. 32 characters] |

Permitted parameter values for table sheet "ICMP Services"

| Name | ICMPv6* | Type | Code |
| --- | --- | --- | --- |
| [free text with max. 128 characters] | True | - PacketToBig - EchoRequest - EchoReply - MulticastListenerQuery - MulticastListenerReport - V2MulticastListenerReport - MulticastListenerDone - RouterSolicitation - RouterAdvertisement - NeighbourSolicitation - NeighbourAdvertisement - RedirectMessage - InverseDiscoverySolicitation - InverseDiscoveryAdvertisement - HomeDiscoveryRequest - HomeDiscoveryReply - MobilePrefixSolicitation - MobilePrefixAdvertisement - CertificationPathSolicitation - CertificatePathAdvertisement - IcmpMessagesUtilizedBySeamoby - MulticastRouterAdvertisement - MulticastRouterSolicitation - MulticastRouterTermination - FmIpV6 - RplControl | NoCode |
| RouterRenumbering | - RouterRenumberingCommand - RouterRenumberingResult - SequenceNumberReset |  |  |
| IcmpNodeInformationQuery | - ContainsIpV6 - ContainsName - ContainsIpV4 |  |  |
| IcmpInformationResponse | - Successful - RefuseToSupplyAnswer - UnknownQtypeOfQuery |  |  |
| TimeExceeded | - HopLimitExceededInTransit - FragmentReassemblyTimeExceeded |  |  |
| ParameterProblem | - ErroneousHeaderFieldEncountered - UnrecognizedNextHeaderTypeEncountered - UnrecognizedIpV6OptionEncountered |  |  |
| False | - EchoReply - SourceQuench - AlternateHostAddress - EchoRequest - RouterSolicitation - TimestampReply - TimestampRequest - InformationRequest - InformationReply - AddressMaskReply - AddressMaskRequest - MobileHostRedirect - IpV6WhereAreYou - IpV6IAmHere - MobileRegistrationReply - MobileRegistrationRequest - Skip - Star | NoCode |  |
| DestinationUnreachable | - Star - NetUnreachable - HostUnreachable - ProtocolUnreachable - PortUnreachable - FragmentationNeededAndDontFragmentWasSet - SourceRouteFailed - DestinationNetworkUnknown - DestinationHostUnknown - SourceHostIsolated - CommunicationWithDestinationNetworkIsAdministrativelyProhibited - CommunicationWithDestinationHostIsAdministrativelyProhibited - DestinationNetworkUnreachableForTypeOfService - DestinationHostUnreachableForTypeOfService - CommunicationAdministrativelyProhibited - HostPrecedenceViolation - PrecedenceCutOffInEffect |  |  |
| Redirect | - Star - DatagramForNetwork - DatagramForTheHost - DatagramForTheTypeOfServiceAndNetwork - DatagramForTheTypeOfServiceandHost |  |  |
| RouterAdvertisement | - Star - NormalRouterAdvertisement - DoesNotRouteCommonTraffic |  |  |
| TimeExceeded | - Star - TimeToLiveExceededInTransit - FragmentReassemblyTimeExceeded |  |  |
| ParameterProblem | - Star - TheIpHeaderIsInvalid - ArequiredOptionIsMissing |  |  |
| Traceroute | - Star - OutboundPacketSuccessfullyForwarded - NoRouteForOutboundPacketThePacketWasDiscarded |  |  |
| ConversionError | - Star - UnknownOrUnspecifiedError - DontConvertOptionPresent - UnknownMandatoryOptionPresent - KnownUnsupportedOptionPresent - UnsupportedTransportProtocol - OverallLengthExceeded - IpHeaderLengthExceeded - TransportProtocolGreaterThen255 - PortConversionOutOfRange - TransportHeaderLengthExceeded - BitRolloverMissingAndAckSet - UnknownMandatoryTransportOptionPresent |  |  |
| Photuris | - Star - BadSpi - AuthenticationFailed - DecompressionFailed - DecryptionFailed - NeedAuthentication - NeedAuthorization |  |  |
| * This column is optional. If the column does not exist when importing into STEP 7, the default value "False" is used in STEP 7. |  |  |  |

Permitted parameter values for table sheet "IP Service Groups"

| Name | Description | IP Services |
| --- | --- | --- |
| [free text with max. 128 characters] | [free text with max. 255 characters] | [free text, services are separated from each other with commas] |

###### Permitted parameter values for MAC rule sets to be imported

The following values may be entered in the table columns of XLSX files for MAC rule sets. Upper and lower case characters are not taken into account when the notation is checked.

Permitted parameter values for table sheet "MAC Ruleset"

| Action | From | To | Source MAC Address | Destination MAC Address | Service | Bandwidth | Logging | Comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| - Accept - Drop - Reject | External | - Internal - Tunnel - Any - Station | [MAC address in the correct format: xx-xx-xx-xx-xx-xx] | [MAC address in the correct format: xx-xx-xx-xx-xx-xx] | [free text with max. 128 characters] | [Possible values: 0.001…1000] | - True - False | [free text with max. 255 characters] |
| Internal | - External - Tunnel - Any |  |  |  |  |  |  |  |
| Tunnel | - External - Internal - Station |  |  |  |  |  |  |  |
| Any | - External - Internal |  |  |  |  |  |  |  |
| Station | - External - Tunnel |  |  |  |  |  |  |  |

Permitted parameter values for table sheet "MAC Services"

| Name | Protocol | DSAP | SSAP | CTRL | OUI | OUI Type |
| --- | --- | --- | --- | --- | --- | --- |
| [free text with max. 128 characters] | - SNAP - PROFINET IO - ISO - [hexadecimal values beginning with 0x] | [hexadecimal values with max. 2 characters] | [hexadecimal values with max. 2 characters] | [hexadecimal values with max. 2 characters] | [hexadecimal values with max. 6 characters] | [hexadecimal values with max. 4 characters] |

Permitted parameter values for table sheet "MAC Service Groups"

| Name | Description | MAC Services |
| --- | --- | --- |
| [free text with max. 128 characters] | [free text with max. 255 characters] | [free text, services are separated from each other with commas] |

##### IP services

This section contains information on the following topics:

- [Defining IP services](#defining-ip-services)
- [ICMP services](#icmp-services)
- [Creating service groups](#creating-service-groups)
- [Managing service groups](#managing-service-groups)

###### Defining IP services

###### How to access this function

In the global security functions, select the entry "Firewall > Services > Define services for IP rules".

###### Procedure

On this page, you define the IP services. Using the IP service definitions, you can define firewall rules for specific services. You select a name and assign the service parameters to it. You can also select pre-defined IP services.

When you configure the IP rules, you simply use this name.

These services defined in this way can also be grouped together under a group name. Here, too, you can select pre-defined groups.

###### Parameters for IP services

You define the IP services using the following parameters:

IP services: Parameter

| Parameter | Meaning/comment | Available options / ranges of values |
| --- | --- | --- |
| Name | Name for the service that is used as identification in the rule definition or in the group. The names of predefined services cannot be changed. | - Name must not be redundant. |
| Protocol | Display or selection of the protocol type.  For certain models you can enter the protocol number directly. | - Enter protocol number - TCP - UDP - TCP+UDP - All |
| Source port | Filtering is based on the port number specified here; this defines the service access at the frame sender. | If you have entered the protocol number directly, it is not possible to specify a port.  Examples:   *: Port is not checked  20 or 21: FTP service |
| Destination port | Filtering is based on the port number specified here; this defines the service access at the frame recipient. | If you have entered the protocol number directly, it is not possible to specify a port.  Examples:   *: Port is not checked   TCP 80: Web HTTP service   TCP 102: S7 protocol |

###### ICMP services

###### How to access this function

1. In the global security functions, select the entry "Firewall > Services > Define services for IP rules".
2. Select the "ICMP" tab.

###### Principle

Using the definition of ICMP services, you can define succinct and clear firewall rules for specific services. You select a name and assign the service parameters to it. You can also select pre-defined ICMPv4 and ICMPv6 services.

The defined services can be grouped together under a group name. Here, too, you can select pre-defined groups.

When you configure the packet filter rules, you then use this name.

###### System-defined ICMPv4 and ICMPv6 services

The system-defined services are displayed in the table. The values of the pre-defined ICMP services cannot be changed.

If you already use names for system-defined ICMP services in existing projects, these are not displayed in the list. If you want to use all system-defined ICMP services, you need to rename the name already used for the service in a previous version of STEP 7.

###### ICMPv4 and ICMPv6 types

You will find a full list of the ICMP packet types and codes on the website of IANA.

To search, enter the number in brackets after the type.

- ICMPv4-specific types:

  [Link:](https://www.iana.org/assignments/icmpv6-parameters/icmpv6-parameters.xml)
- ICMPv6-specific types:

  [Link:](https://www.iana.org/assignments/icmp-parameters):

###### Parameters for ICMP services

| Parameter | Meaning/comment | Available options / ranges of values |
| --- | --- | --- |
| Name | User-definable name for the service that is used as identification in the rule definition or in the group.  The names of pre-defined ICMPv4 services and ICMPv6 services cannot be changed. | - Freely selectable name. - The same name may be used for an ICMPv4 service and an ICMPv6 service. - The name must be unique within a service. |
| ICMPv6 | If you enable this check box, the ICMP service is declared as an ICMPv6 service and you can select an ICMPv6-specific type and code for the service. An ICMPv6 service can only be used in the firewall rule of a security module that supports IPv6.  When you clear this check box, the ICMP service is declared as ICMPv4 service and you can select an ICMPv4-specific type and code for the service. | - Enabled - Disabled |
| Type | Type of the ICMPv4 or ICMPv6 message.  A few examples are shown below:   Destination unreachable: IP telegram cannot be delivered.  Time Exceeded: Time limit exceeded.  Echo request: Echo request, better known as ping. | If the "ICMPv6" check box is cleared, ICMPv4-specific types can be selected. If the check box is selected, ICMPv6-specific types can be selected. |
| Code | Code of the ICMP type.  The code describes the ICMP packet type in greater detail. The display depends on the selected type.   "*" means all codes are selected. | Values depend on the selected type. |

###### Creating service groups

###### How to access this function

1. In the global security functions, select the entry "Firewall > Services > Define services for IP rules".
2. Select the "Service groups" tab.

###### Forming service groups

You can put several services together by creating service groups. This allows you set up more complex services that you can then use in the packet filter rules simply by selecting the name. IPv4 and IPv6 services can be collected in the same service group.

Create groups in the open "Service groups" tab. You can then assign services to a group in the "Group management" tab.

You can also select pre-defined service groups for ICMPv4 or ICMPv6, for example.

###### Follow the steps below

1. First, create groups in this tab with names to suit your requirements and add a description if required.
2. Select the "Group Management" tab. You can assign the previously specified IP services to the groups defined in this tab.

###### Managing service groups

###### How to access this function

1. In the global security functions, select the entry "Firewall > Services > Define services for IP rules".
2. Select the "Group management" tab.

###### Forming service groups

You can put several services together by creating service groups. This allows you set up more complex services that you can then use in the packet filter rules simply by selecting the name. IPv4 and IPv6 services can be collected in the same service group.

Use the "Group management" tab to assign services to a selected group. This can be a group previously created in the "Service groups" tab or a pre-defined group.

###### Follow the steps below

1. First select a group from the "Service groups" drop-down list in this tab.
2. Then assign the required services from the list box on the right, "Available services", to the group.

##### MAC services

This section contains information on the following topics:

- [Define MAC services](#define-mac-services)
- [Creating service groups](#creating-service-groups-1)
- [Managing service groups](#managing-service-groups-1)

###### Define MAC services

###### How to access this function

In the global security functions, select the entry "Firewall > Services > Define services for MAC rules".

###### Meaning

Using the definition of MAC services, you can define succinct and clear firewall rules for specific services. You select a name and assign the service parameters to it.

These services defined in this way can be grouped together under a group name.

When you configure the global or local packet filter rules, you use this name.

###### Parameters for MAC services

A MAC service definition is formed using protocol-specific MAC parameters:

MAC services - parameters

| Parameter | Meaning/comment | Available options / ranges of values |
| --- | --- | --- |
| Name | User-definable name for the service that is used as identification in the rule definition or in the group. | - Name must not be redundant. |
| Protocol | Name of the protocol type:  - ISO   ISO identifies frames with the following properties:   Lengthfield <= 05DC (hex),  DSAP= userdefined  SSAP= userdefined  CTRL= userdefined - SNAP   SNAP identifies frames with the following properties:   Lengthfield <= 05DC (hex),  DSAP=AA (hex), SSAP=AA (hex),  CTRL=03 (hex),  OUI=userdefined,  OUI-Type=userdefined - PROFINET IO - Alternatively, a protocol number can be entered.   The protocol entries 0800 (hex) and 0806 (hex) are not accepted since these values apply to IP or ARP frames. | - Enter protocol number (0x is added automatically) - ISO - SNAP - PROFINET IO |
| DSAP | Destination Service Access Point: LLC recipient address |  |
| SSAP | Source Service Access Point: LLC sender address |  |
| CTRL | LLC control field |  |
| OUI | Organizationally Unique Identifier  (the first 3 bytes of the MAC address = vendor ID) |  |
| OUI type | Protocol type/identification |  |

> **Note**
>
> **Processing for S7-CPs**
>
> Only settings for ISO frames with DSAP=SSAP=FE (hex) are processed. Other frame types are not relevant for S7 CPs and are therefore discarded even before processing by the firewall.

###### Special settings for SIMATIC NET services

Use the following protocol settings for filtering of specific SIMATIC NET services:

- DCP:

  PROFINET IO
- SiClock :

  OUI= 08 00 06 (hex) , OUI-Type= 01 00 (hex)

###### Creating service groups

###### How to access this function

1. In the global security functions, select the entry "Firewall > Services > Define services for MAC rules".
2. Select the "Service groups" tab.

###### Forming service groups

You can put several services together by creating service groups. This allows you set up more complex services that you can then use in the packet filter rules simply by selecting the name.

Create groups in the open "Service groups" tab. You can then assign services to a group in the "Group management" tab.

You can also select pre-defined service groups, for example, for DCP.

###### Follow the steps below

1. First, create groups in this tab with names to suit your requirements and add a description if required.
2. Select the "Group Management" tab. You can assign the previously specified MAC services to the groups defined in this tab.

###### Managing service groups

###### How to access this function

1. In the global security functions, select the entry "Firewall > Services > Define services for MAC rules".
2. Select the "Group management" tab.

###### Forming service groups

You can put several services together by creating service groups. This allows you set up more complex services that you can then use in the packet filter rules simply by selecting the name.

Use the "Group management" tab to assign services to a selected group. This can be a group previously created in the "Service groups" tab or a pre-defined group.

###### Follow the steps below

1. First select a group from the "Service groups" drop-down list in this tab.
2. Then assign the required services from the list box on the right, "Available services", to the group.

#### Local firewall

This section contains information on the following topics:

- [Overview of local firewall rules](#overview-of-local-firewall-rules)
- [Defining IP packet filter rules](#defining-ip-packet-filter-rules)
- [Defining MAC packet filter rules](#defining-mac-packet-filter-rules)

##### Overview of local firewall rules

###### Meaning

Local firewall rules are configured in the local security settings of a security module and apply only to this security module. After enabling the firewall functionality you can either use predefined firewall rules or define firewall rules in the advanced firewall mode.

###### Using predefined firewall rules

Here, you use simple, predefined rules. You can only enable service-specific rules. The enabled services are allowed for all nodes in the specified direction. You can find detailed information on the definition of firewall rules in this dialog in the following module-specific sections:

- For SCALANCE S: [Local firewall rules for SCALANCE S modules](#local-firewall-rules-for-scalance-s-modules)
- For S7-300/S7-400/PC CPs: [Local firewall rules for S7-300 /S7-400 / PC CPs](#local-firewall-rules-for-s7-300-s7-400-pc-cps)
- For S7-1200/S7-1500 CPs: [Local firewall rules for S7-1200 / S7-1500 CPs](#local-firewall-rules-for-s7-1200-s7-1500-cps)

The communication direction "Station" that can be configured for CPs, includes access to the CP and access to the CPU via the CP.

###### Defining firewall rules in advanced firewall mode

In advanced firewall mode, you can make detailed firewall settings. You can allow individual services for a single node or all services for the node for access to the station or network. You enable the advanced firewall mode using the "Activate firewall in advanced mode" check box. You open the editors for configuration of IP rules and MAC rules in the advanced firewall mode using the corresponding buttons in "Firewall > IP rules". For the configuration options available here in the editors refer to the following section:

For IP packet filter rules: [Defining IP packet filter rules](#defining-ip-packet-filter-rules)

For MAC packet filter rules: [Defining MAC packet filter rules](#defining-mac-packet-filter-rules)

> **Note**
>
> **Deactivating the advanced firewall mode not possible**
>
> Once you have activated the advanced firewall mode, you can no longer deactivate it.

###### Adopting predefined firewall rules in the advanced firewall mode

When you switch over to the advanced firewall mode, enabled predefined firewall rules and logging settings are adopted. If, for example, the "Allow S7 protocol" check box is selected in the direction "From External to Internal" for a SCALANCE S module, an Accept rule with this communication direction and the service "S7" are created automatically in the advanced firewall mode.

If predefined logging settings exist for S7-1200 / S7-1500 CPs, in advanced mode these are not shown as firewall rules but under the entry “Firewall > Log settings” where they can be edited.

###### Configuration limits

| Number of firewall rules (advanced firewall mode) |  |
| --- | --- |
| SCALANCE S | Maximum of 256 |
| S7-1200/S7-1500 CPs | Maximum of 256 |
| CP 343-1 Adv. / 443-1 Adv. | Maximum of 226 |
| CP 1628 | Maximum of 226 |

##### Defining IP packet filter rules

###### Meaning

With IP packet filter rules, you filter according to IP frames, such as TCP, UDP and ICMP.

Within a packet filter rule, you can also fall back on the definitions of the IP services.

Assigned global firewall rules and automatically generated firewall rules for NAT/NAPT are shown as rule sets.

###### Operator controls of the menu bar

The operator controls of the menu bar have the following functions:

| Operator control element | Function |
| --- | --- |
| ![Operator controls of the menu bar](images/101505130635_DV_resource.Stream@PNG-de-DE.png) | Enabling the firewall  Enables the editor for IP rules. If the editor is enabled, the corresponding rules can be configured and are transferred to the module during loading. |
| ![Operator controls of the menu bar](images/101505139467_DV_resource.Stream@PNG-de-DE.png) | Insert rule above  Inserts a rule above the selected rule / the selected rule set. To insert above a rule set, its first line must be selected. |
| ![Operator controls of the menu bar](images/101505647755_DV_resource.Stream@PNG-de-DE.png) | Insert rule below  Inserts a rule below the selected rule / the selected rule set. To insert below a rule set, its first line must be selected. |
| ![Operator controls of the menu bar](images/101505950987_DV_resource.Stream@PNG-de-DE.png) | Move up  Moves the selected rule / the selected rule set one line up. To move a rule set, its first line must be selected. |
| ![Operator controls of the menu bar](images/101505959819_DV_resource.Stream@PNG-de-DE.png) | Move down  Moves the selected rule / the selected rule set one line down. To move a rule set, its first line must be selected. |
| ![Operator controls of the menu bar](images/101506237451_DV_resource.Stream@PNG-de-DE.png) | Expand rule sets  Shows existing rule sets expanded. |
| ![Operator controls of the menu bar](images/101506348683_DV_resource.Stream@PNG-de-DE.png) | Collapse rule sets  Shows existing rule sets collapsed. |
| ![Operator controls of the menu bar](images/101841147147_DV_resource.Stream@PNG-de-DE.png) | Separate  Converts the selected line into a separate rule or rules. If the first line of a rule set is selected, all rules of the rule set are converted into separate rules. If one rule contained in a rule set is selected, this is converted into a separate rule. In addition to this, the following rules of the rule set are converted into a separate rule set. |

###### Advanced IP rule editor

After selecting an IP rule, an advanced IP rule editor appears in the Inspector window under "General > IP rules". It is used for simplified configuration of IP rules. Changes made in this editor are adopted in the selected IP rule.

###### Defining IP rules in the Advanced IP rule editor

The following parameters can be configured:

All tables
Parameters in the IP rule editor 
Meaning of the entries in the shortcut menu

Parameters in the IP rule editor

| Parameter | Meaning/comment | Available options / ranges of values |
| --- | --- | --- |
| **General** |  |  |
| Number | Automatically assigned number for the rule. The numbers are recalculated when rules are moved. |  |
| Comment | Space for your own explanation of the rule | If a comment is marked with "AUTO", it was created for an automatic connection rule. For rules you have created, entry of a comment is optional. |
| **IP rules** |  |  |
| Action | Allow/disallow (enable/block) | - Accept   Allow frames according to definition. - Drop   Block frames according to definition. - Reject   The frames are rejected, and the sender receives a corresponding message.  For firewall rules generated automatically as result of configuring a connection and subsequently adapted manually:  - Accept* - Drop*   If you change automatically created connection rules, when the "*" option is selected they are not recreated and overwritten by STEP 7. |
| From / To | Selection of the communications directions for which the rule will apply. | Described in separate sections.  - For SCALANCE S modules: [IP packet filter directions SCALANCE S](#ip-packet-filter-directions-scalance-s) - For S7-300/S7-400/PC CPs: [IP packet filter directions S7-300-/S7-400-/PC-CPs](#ip-packet-filter-directions-s7-300-s7-400-pc-cps) - For S7-1200/S7-1500 CPs: [IP packet filter directions S7-1200 / S7-1500 CPs](#ip-packet-filter-directions-s7-1200-s7-1500-cps)   The communication direction "Station" includes access to the CP and access to the CPU via the CP.  The communication direction "Any" includes all the firewall directions supported by the security module at the time of loading.  The communication directions "Station", "Backplane bus" (only for CP 1543-1 as of V2.1 with the option "IP routing between communications modules") and "Tunnel" are classified as trusted by default. For communication between trustworthy directions no firewall rules need to be configured. |
| Source IP address | The firewall rule is applied to the frames with a sender that has the IP address specified here. If you do not specify an IP address, the firewall rule applies to all nodes in the communications direction you selected in the "From" column. | In the editor, address ranges can be configured in the text boxes of the "From" and "To" columns. If several address ranges are configured for an IP rule, the number of addresses must match in each case. After configuring address ranges, STEP 7 creates an IP rule set from the selected IP rule that contains a corresponding IP rule for each of the addresses.    You can find additional information about IP addresses in the [IP addresses in IP packet filter rules](#ip-addresses-in-ip-packet-filter-rules) section.     **Configuration options in ghost mode (only for SCALANCE S S602 as of V3.1):**   If ghost mode is activated, the IP address of the internal node is dynamically determined by the security module at runtime. Depending on the selected direction, you can select one of the following options in the column "Source IP address" (for direction "From internal to external") or in the column "Destination IP address" (for direction "From external to internal"):  - IP address of the internal node: The IP address of the internal node is inserted in the firewall rule by the SCALANCE S. - Limited broadcast: The broadcast IP address 255.255.255.255 is inserted in the firewall rule by the SCALANCE S. - Directed broadcast: The broadcast IP address of the SCALANCE S network is inserted in the firewall rule by the SCALANCE S. A directed broadcast can also be forwarded into the destination network via routers. - Multicast: The multicast address band 224.0.0.0 /24 is inserted in the firewall rule by the SCALANCE S. After selecting this option, as an alternative a specific multicast IP address from the multicast address band can be specified. |
| Dest. IP address | The firewall rule is applied to the frames with a recipient that has the IP address specified here. If you do not specify an IP address, the firewall rules applies to all nodes in the communications direction you selected in the "To" column. |  |
| **Additional settings** |  |  |
| Service | Selection of the IP/ICMP service or the service group to be used.  Note: Before using a predefined service make sure that its predefined parameters meet your requirements. Pay particular attention to the predefined source and destination ports. | When selected, a window opens in which all pre-defined and configured IP services, ICMP services and service groups are displayed. These are managed in the global security functions under "Firewall > Services > Define services for IP rules". |
| Transmission speed (Mbps) | Limitation of the transmission speed  Can only be entered if "Accept" is selected for the action.  A packet passes through the firewall if the Accept rule applies and the permitted transmission speed for this rule has not yet been exceeded. | CP 343-1 Adv. / CP 443-1 Adv., S7-1200-/S7-1500-CPs, CP 1628: 0.001 ... 100 Mbps  SCALANCE S: 0.001 ... 1000 Mbps  For global and user-specific rules: 0.001 ... 1000 Mbps  For IP rules with the direction "Backplane bus": 0.001 ... 1 Mbps  Note: If the direction "From tunnel to station" is configured in a firewall rule for the S7-1200/S7-1500 CPs, no transmission speed limitation can be specified.  For CP 1543-1 V2.1 only one transmission speed can be specified if "Any" is configured for one of the two directions. This does not apply to the combination of directions "Any" and "Station". |
| Logging | Enable and disable logging for this rule. If logging is enabled, the settings for the packet filter logging configured in the local security settings apply. | - Enabled - Disabled (default) |
| Number | Automatically assigned number for the rule. The numbers are recalculated when rules are moved. |  |
| Stateful | If this check box is cleared for an IP rule with the "Accept" action, no firewall states are generated by packets to which the Accept rule applies. Firewall states automatically allow the responses to allowed packets.  Can only be adapted if "Accept" is selected for the action. Configuration of IP rules without firewall states is only possible for SCALANCE S modules as of firmware V3. If the responses to packets that have passed the firewall according to such IP rules should also be allowed, additional IP rules need to be configured for these responses. | For Accept rules of SCALANCE S ≥ V3:  - enabled (default) - disabled     For Accept rules of SCALANCE S < V3 and CPs:  - enabled (default)   Note: The check box is not present for CPs; however, the activated option is always used implicitly for Accept rules of CPs.    For Drop rules:  - Disabled (default) |
| Number of copies to create | The selected IP rule is copied. | Select how often the selected rule is to be copied and click on the "Create copies" button. |

Meaning of the entries in the shortcut menu

| Entry in the shortcut menu | Meaning |
| --- | --- |
| Insert rule above | Use this option to insert a rule above the selected rule. |
| Insert rule below | Use this option to insert a rule below the selected rule. |
| Delete | This deletes the selected rule. |
| Save as global rule set | Copies the selected firewall rule(s) and inserts them as a global firewall rule set in the global security functions. The firewall configuration currently configured for the security module remains unaffected by this procedure. |
| Move up | Use this to move the selected rule one position up in the list. As an alternative, you can move the selected rule using drag-and-drop. You can select multiple entries.  This means that the moved rule is treated with a higher priority. |
| Move down | Use this to move the selected rule down. As an alternative, you can move the selected rule using drag-and-drop. You can select multiple entries.  This causes the moved rule to be treated with a lower priority. |
| Define service for IP rules | This opens the dialog in which you can manage the IP services and service groups. |

##### Defining MAC packet filter rules

###### Meaning

With the MAC packet filter rules, you filter according to MAC frames.

Within a packet filter rule, you can also fall back on the definitions of the MAC services.

Assigned global firewall rules are shown as rule sets.

###### Operator controls of the menu bar

The operator controls of the menu bar have the following functions:

| Operator control element | Function |
| --- | --- |
| ![Operator controls of the menu bar](images/101505130635_DV_resource.Stream@PNG-de-DE.png) | Enabling the firewall  Enables the editor for MAC rules. If the editor is enabled, the corresponding rules can be configured and are transferred to the module during loading. |
| ![Operator controls of the menu bar](images/101505139467_DV_resource.Stream@PNG-de-DE.png) | Insert rule above  Inserts a rule above the selected rule / the selected rule set. To insert above a rule set, its first line must be selected. |
| ![Operator controls of the menu bar](images/101505647755_DV_resource.Stream@PNG-de-DE.png) | Insert rule below  Inserts a rule below the selected rule / the selected rule set. To insert below a rule set, its first line must be selected. |
| ![Operator controls of the menu bar](images/101505950987_DV_resource.Stream@PNG-de-DE.png) | Move up  Moves the selected rule / the selected rule set one line up. To move a rule set, its first line must be selected. |
| ![Operator controls of the menu bar](images/101505959819_DV_resource.Stream@PNG-de-DE.png) | Move down  Moves the selected rule / the selected rule set one line down. To move a rule set, its first line must be selected. |
| ![Operator controls of the menu bar](images/101506237451_DV_resource.Stream@PNG-de-DE.png) | Expand rule sets  Shows existing rule sets expanded. |
| ![Operator controls of the menu bar](images/101506348683_DV_resource.Stream@PNG-de-DE.png) | Collapse rule sets  Shows existing rule sets collapsed. |

###### Entering MAC packet filter rules

After enabling the editor the MAC rules can be configured with the following parameters:

All tables
MAC rules: Parameter
Meaning of the menu commands

MAC rules: Parameter

| Parameter | Meaning/comment | Available options / ranges of values |
| --- | --- | --- |
| Action | Allow/disallow (enable/block) | - Accept   Allow frames according to definition. - Drop   Block frames according to definition. - Reject   The frames are rejected, and the sender receives a corresponding message.  For firewall rules generated automatically as result of configuring a connection and subsequently adapted manually:  - Accept* - Drop*   If you change automatically created connection rules, when the "*" option is selected they are not recreated and overwritten by STEP 7. |
| From / To | Selection of the communications directions for which the rule will apply. | Described in separate sections.  - For SCALANCE S modules: [MAC packet filter directions SCALANCE S](#mac-packet-filter-directions-scalance-s) - For S7-300/S7-400/PC CPs: [MAC packet filter directions S7-300-/S7-400-/PC-CPs](#mac-packet-filter-directions-s7-300-s7-400-pc-cps) - For S7-1200/S7-1500 CPs: [MAC packet filter directions S7-1200 / S7-1500 CPs](#mac-packet-filter-directions-s7-1200-s7-1500-cps)   The communication direction "Station" includes access to the CP and access to the CPU via the CP.  As default, the communication directions "Station" and "Tunnel" are classified as being trustworthy. For communication between trustworthy directions no firewall rules need to be configured. |
| Source MAC address | The firewall rule is applied to the frames with a sender that has the MAC address specified here. If you do not specify a MAC address, the firewall rule applies to all nodes in the communications direction you selected in the "From" column. | MAC address in the correct format |
| Destination MAC address | The firewall rule is applied to the frames with a recipient that has the MAC address specified here. If you do not specify a MAC address, the firewall rule applies to all nodes in the communications direction you selected in the "To" column. |  |
| Service | Selection of the MAC service or the service group to be used.  Note: Before using a predefined service make sure that its predefined parameters meet your requirements. | The drop-down list box displays the predefined and configured services and service groups you can select. These are displayed in the global security functions under "Firewall" > "Services" > "Define services for MAC rules". |
| Transmission speed (Mbps) | Limitation of the transmission speed   Can only be entered if "Accept" is selected for the action.  A packet passes through the firewall if the Accept rule applies and the permitted transmission speed for this rule has not yet been exceeded. | CP 343-1 Adv. / CP 443-1 Adv., S7-1200-/S7-1500-CPs: 0.001 ... 100 Mbps  CP 1628 and SCALANCE S: 0.001 ... 1000 Mbps  For global rules: 0.001 ... 1000 Mbps  Note: If the direction "From tunnel to station" is configured in a firewall rule for the S7-1200/S7-1500 CPs, no transmission speed limitation can be specified. |
| Logging | Enable and disable logging for this rule. If logging is enabled, the settings for the packet filter logging configured in the local security settings apply. | - Enabled - Disabled (default) |
| Number | Automatically assigned number for the rule. The numbers are recalculated when rules are moved. |  |
| Comment | Space for your own explanation of the rule | If a comment is marked with "AUTO", it was created for an automatic connection rule. For rules you have created, entry of a comment is optional. |

Meaning of the menu commands

| Button | Meaning |
| --- | --- |
| Delete | This deletes the selected rule or the selected global rule set.  Notes on removing a globally defined and locally assigned rule set:  if you delete a rule set here, this only cancels the assignment to the security module. |
| Save as global rule set (only for local firewall rules) | Copies the selected firewall rule(s) and inserts them as a global firewall rule set in the global security functions. The firewall configuration currently configured for the security module remains unaffected by this procedure. |
| Move up | Use this button to move the selected rule or selected global rule set up one position in the list. As an alternative, you can move the selected rule or the selected rule set by dragging it with the mouse. You can select multiple entries.  The rule / rule set you moved is therefore handled with higher priority. |
| Move down | Use this button to move the selected rule or selected global rule set down one position in the list. As an alternative, you can move the selected rule or the selected rule set by dragging it with the mouse. You can select multiple entries.  The rule / rule set you moved is therefore handled with lower priority. |
| Define service for MAC rules | This opens the dialog in which you can manage the MAC services and service groups. |

#### IP addresses in IP packet filter rules

##### Entering IP addresses in IP packet filter rules

In IP packet filter rules, you have the following options for entering IP addresses:

- Nothing specified

  The rule applies to all IP addresses.
- An IP address

  The rule applies specifically to the specified address.
- Address range

  The rule applies to all the IP addresses covered by the address range.

  An address range is defined by specifying the number of valid bit places in the IP address in the format: [IP address]/[number of bits to be taken into account]

  - [IP address]/24 therefore means that only the most significant 24 bits of the IP address are included in the filter rule. These are the first three octets of the IP address.
  - [IP address ]/25 means that only the first three octets and the highest bit of the fourth octet of the IP address are included in the filter rule.
- Address area

  For the source IP address, an address range can be entered in the following format:

  [Start IP address]-[End IP address]

##### IPv4 addresses

An IPv4 address consists of 4 decimal numbers in the range from 0 to 255 separated from each other by a dot.

Examples of address ranges in IPv4 addresses

| Source IP address or destination IP address | Address range |  | Number of  addresses<sup>*)</sup> |
| --- | --- | --- | --- |
|  | from | to |  |
| 192.168.0.0**/16** | 192.168.0.0 | 192.168.255.255 | 65.536 |
| 192.168.10.0**/24** | 192.168.10.0 | 192.168.10.255 | 256 |
| 192.168.10.0**/25** | 192.168.10.0 | 192.168.10.127 | 128 |
| 192.168.10.0**/26** | 192.168.10.0 | 192.168.10.63 | 64 |
| 192.168.10.0**/27** | 192.168.10.0 | 192.168.10.31 | 32 |
| 192.168.10.0**/28** | 192.168.10.0 | 192.168.10.15 | 16 |
| 192.168.10.0**/29** | 192.168.10.0 | 192.168.10.7 | 8 |
| 192.168.10.0**/30** | 192.168.10.0 | 192.168.10.3 | 4 |
| *) Note: Note that the network address and the broadcast address are not available as IP addresses of network nodes in an address range. |  |  |  |

##### IPv6 addresses

IPv6 addresses consist of 8 fields each with four hexadecimal numbers (128 bits in total). The fields are separated by a colon.

Example: fd00:ffff:ffff:ffff:ffff:ffff:2f33:8f21

Rules / simplifications:

- Leading zeros within a field can be omitted.

  Example: Instead of 2001:0db8:2426:08d3:1457:8a2e:0070:7344 it is also possible to use the notation 2001:db8:2426:8d3:1457:8a2e:70:7344.
- If one or more fields have the value 0 (or 0000), a shortened notation is possible.

  Example: Instead of 2001:0db8:0:0:0:0:1428:57ab it is also possible to use the notation 2001:db8::1428:57ab.

  To ensure uniqueness, this shortened form can only be used once within the entire address.
- Decimal notation with periods

  The last 2 fields or 4 bytes can be written in the normal decimal notation with periods.

  Example: The IPv6 address fd00::ffff.125.1.0.1 is equivalent to fd00::ffff:7d01:1.
- Address range notation in IP packet filter rules: In the same way as IPv4 addresses, IPv6 addresses can also be noted in the form of address ranges.

  Example: The entry "2001:0db8:85a3:08d3:1319:8a2e:0:0/96" covers all IPv6 addresses from 2001:0db8:85a3:08d3:1319:8a2e:0:0 to 2001:0db8:85a3:08d3:1319:8a2e:ffff:ffff.

### Syslog

The global Syslog server is available only for SCALANCE S, X, M, W.

#### Meaning

Syslog according to RFC 3164 is used for transferring short, unencrypted text messages over UDP in the IP network. This requires a Syslog server.

#### Requirements for sending log entries

- The Syslog function is enabled on the device.
- In "System > Events > Configuration", "Syslog" is activated for the relevant event.
- There is a Syslog server in your network that receives the log entries. Since this is a UDP connection, there is no acknowledgment to the sender.
- The IP address or the FQDN (Fully Qualified Domain Name) of the Syslog server is entered in the device.

#### Procedure

1. In the global security functions, select the entry "Syslog server".

   Result: The previously created Syslog servers are displayed under the selected entry.
2. Double-click the "Add new Syslog server" entry.  
   Result: The created Syslog server is displayed with an automatically assigned number below the "Syslog" entry.
3. Double-click the created Syslog server.  
   Result: The assignment dialog for Syslog server is displayed in the work area. The selected Syslog server is selected in the "Syslog server" drop-down list. The required security modules can be assigned to it. The configurable properties of the Syslog server are displayed in the general security settings.
4. Enter the following data in the "General" entry in the local security settings:

| Parameter | Meaning |
| --- | --- |
| Name | Name of the Syslog server.  The name can consist of a maximum of 25 characters. The characters 0-9, a-z, A-Z, - _ can be used. A name must start with a letter and end with a letter or number. Before the '.' character only letters and numbers are permitted, after the '.' character only letters. Before the '_' or '-' character only letters and numbers are permitted. |
| IP Address | Enter the IP address or the FQDN (Fully Qualified Domain Name) of the Syslog server. |
| Server port | Enter the port of the Syslog server being used. |
| TLS | - Enabled   Syslog messages are sent using TLS encryption over TCP. - Disabled   Syslog messages are sent unencrypted over UDP. |
| Comment | Entry of freely selectable, optional comments. |

### Carrying out module-specific log settings

This section contains information on the following topics:

- [Log settings - overview](#log-settings---overview)
- [Configuring local logging](#configuring-local-logging)
- [Configuring system events](#configuring-system-events)
- [Configuring the network Syslog](#configuring-the-network-syslog)

#### Log settings - overview

##### Module-specific function

Some logging functions are only available for certain security modules.

##### Log settings in the configuration

The log settings made here are loaded on the module with the configuration and take effect when the security module starts up.

You can restrict the configured packet filter log settings in the online functions if necessary. For example, you can use the online functions to specify that merely IP logging is displayed if you have configured IP and MAC logging.

##### Logging procedures and event classes

Here, you can specify which data should be logged. As a result, you enable logging as soon as you download the configuration to the security module.

During configuration, you also select one or both of the possible logging procedures:

- Local logging
- Network Syslog

In both logging procedures, the security module recognizes the three following types of events:

- Packet filter events
- Audit events
- System events

#### Configuring local logging

##### How to access this function

1. Select the module to be edited.
2. Select the "Log settings" > "Local log memory" entry in the local security settings.

##### Configuring local logging

All tables
Local logging - settings for log events
Local logging - storage of recorded data

Local logging - settings for log events

| Log event | Meaning | Comments |
| --- | --- | --- |
| Packet filter log (firewall) | The packet filter log records certain packets of the data traffic. Data packets are only logged if they match a configured packet filter rule (firewall) or to which the basic protection reacts (corrupt or invalid packets). This is only possible when logging is enabled for the packet filter rule.  In the "Packets to be logged" drop-down list, you can specify the data packets to be logged:  - "All packets": The data packets that are logged are those to which a configured firewall rule applies. In addition to this, all the response packets to such packets that have passed the firewall according to a configured Accept rule are recorded. - "Status generating packets" (only for SCALANCE S as of V3): The only data packets that are logged are those to which a configured firewall rule (standard mode or advanced mode) applies and that initially generate a status in the firewall. Data packets that pass through the firewall by using this firewall status are not logged. | Packet filter log data is not retentive  The data is stored in volatile memory on the security module and is therefore no longer available after the power supply has been turned off. For retentive storage, you can also save the log data displayed in the "Online & diagnostics" dialog in a file. |
| Audit log | The logging of audit events is always enabled.  The logged information is always stored in the ring buffer.  The audit log automatically records security-relevant events, for example user actions such as activating or deactivating packet logging or downloading configurations to the security module. | Audit log data is retentive.  The data is stored in a retentive memory of the security module and is therefore still available after turning off the power supply.   **Note for CPs:**   The audit log files are not retentive on CPs. You should therefore use a Syslog server to backup this data. |
| System log | The system log automatically logs successive system events, for example the start of a process or the failed login attempt of a user.  Select the "Log settings" > "System events" entry to configure the event filter and cable diagnostics functions. | System log data is not retentive  The data is stored in volatile memory on the security module and is therefore no longer available after the power supply has been turned off. For retentive storage, you can also save the log data displayed in the "Online & diagnostics" dialog in a file. |

Local logging - storage of recorded data

| Storage | Meaning |
| --- | --- |
| Ring buffer | At the end of the buffer, the recording continues at the start of the buffer and overwrites the oldest entries. |
| One-shot buffer | Recording stops when the buffer is full. |

#### Configuring system events

##### How to access this function

1. Select the module to be edited.
2. Select the "Log settings" > "System events" entry in the local security settings.

##### Filtering of the system events

In this dialog, you set a filter level for the system events. As default, the following values are set:

- SCALANCE S: Level 3 (Error)
- CP: Level 3 (Error)

The system events are recorded that have the same priority as the selected filter level and that have a higher priority than the selected filter level. The lower the value of the filter level, the higher its priority and therefore less events are recorded.

The priority of the selected filter level must be the same or lower than the severity set for the cable diagnostics; see the "Setting parameters for line diagnostics" table (not for CPs).

Recommendation: Select "Error" as the filter level or a filter level with a higher priority to prevent recording of general non-critical events.

##### Note for CP

For CPs, select only level 3 or level 6 since only events of these levels are generated for CPs.

- Level 0 to level 3 error messages are output if level 3 is selected.
- If you select level 6, the error messages of levels 0 to 6 are output.

##### Properties of the system events - line diagnostics (only for SCALANCE S)

Line diagnostics generates a special system event. A system event is generated when a selectable percentage of bad frames is reached. This system event is assigned the severity and facility set in this dialog.

Setting parameters for line diagnostics

| Function / option / parameter | Meaning |
| --- | --- |
| Enable | Enabling and disabling logging |
| Limit | Selectable percentage of faulty frames representing the limit at which a system event is triggered. |
| Facility | Select a facility from the drop-down list that identifies the system event to be logged. |
| Severity | Using the severity, you weight the system events of line diagnostics relative to the severity of the other system events. |

> **Note**
>
> **Severity of the system events of line diagnostics**
>
> The system events of the line diagnostics must not have a lower severity than you set for the filter. At a lower severity, these events cannot pass through the filter and will not be logged.

#### Configuring the network Syslog

##### How to access this function

1. Select the module to be edited.
2. Select the "Log settings" > "Network Syslog" entry in the local security settings.

##### Configuring the network Syslog

Network Syslog - basic settings

| Option / parameter |  |
| --- | --- |
| Enable network Syslog | Enables and disables the transfer of logging events to the Syslog server. |
| Syslog server | Enter the IPv4/IPv6 address or the FQDN of the Syslog server. A DNS configuration is required for using an FQDN.  The Syslog server must be accessible from the security module at the specified address and, if applicable, using the router configuration under the "Routing" entry of the local security settings. If the Syslog server cannot be accessed no Syslog messages are sent. You can recognize this operating state on the basis of corresponding system alarms. To activate the sending of the Syslog information again, you may have to update the routing information and initiate a restart of the security module. |
| Enable event classes | Enable the classes of events to be transferred to the Syslog server. You can classify packet filter and audit events according to the Severity and using the Facility according to their origin. |
| Module name | The module name is displayed and cannot be changed at this point. |

> **Note**
>
> **Non-secure transfer of logging events**
>
> Logging events are transferred to Syslog servers in plain language. This should be taken into account when using Syslog servers.

Network Syslog - settings for log events

| Log event | Configuring | Comments |
| --- | --- | --- |
| Packet filter events (firewall) | The packet filter log records certain packets of the data traffic. Data packets are only logged if they match a configured packet filter rule (firewall) or to which the basic protection reacts (corrupt or invalid packets). This is only possible if logging is activated for the packet filter rule.  Syslog alarms can be classified according to their origin and their severity level by setting Facility and Severity. This assignment is carried out with drop-down lists. The severity and facility that you set here is assigned to every event. | Which value you select, depends on the evaluation in the Syslog server.  If you retain the "default" value setting, the security module specifies the combination of facility and severity with which the event is displayed. |
| Audit events | The audit log automatically records security-relevant events, for example user actions such as activating or deactivating packet logging or downloading configurations to the security module.  Assignment of the severity and facility is carried out with drop-down lists. The severity and facility that you set here is assigned to every event. | The value you select for the severity and facility, depends on the evaluation in the Syslog server.  If you retain the "default" value setting, the security module specifies the combination of facility and severity with which the event is displayed. |
| System events | The system log automatically logs successive system events, for example the start of a process or the failed login attempt of a user. | Select the "Log settings" > "System events" entry in the local security settings to configure the event filter and cable diagnostics functions. |

### Security module as router

This section contains information on the following topics:

- [Overview of the routing settings](#overview-of-the-routing-settings)
- [Overview of NAT/NAPT](#overview-of-natnapt)
- [NAT/NAPT routing](#natnapt-routing)
- [Address translation with NAT/NAPT in VPN tunnels](#address-translation-with-natnapt-in-vpn-tunnels)
- [Relationship between NAT/NAPT router and firewall](#relationship-between-natnapt-router-and-firewall)
- [Relationship between NAT/NAPT router and user-specific firewall](#relationship-between-natnapt-router-and-user-specific-firewall)

#### Overview of the routing settings

##### Meaning

If you operate the security module in routing mode, the networks connected to the internal and external interface are transformed into separate subnets. The DMZ interface (SCALANCE S623/S627-2M only) is connected in routing mode regardless of the mode. In routing mode, the frames intended for an existing IP address in the subnet are forwarded. The firewall rules for the direction of transmission also apply.

You have the following additional options:

- Setting specific routes - can be set in the local security settings under "Routing" (SCALANCE S only), see [Specifying routes](#specifying-routes).
- Use standard router - can be set in the local security settings with "External interface [P1] red", "Internal interface [P2] green" or "DMZ interface [P3] yellow" (SCALANCE S623/S627-2M only) see [Configuring IP address parameters](#configuring-ip-address-parameters).  
  A maximum of one standard router can be used per security module.
- NAT/NAPT routing - can be set in the local security settings in "NAT / NAPT" (only for SCALANCE S and CP 343-1 Adv. / CP 443-1 Adv.).

##### Enabling routing mode (required for SCALANCE S modules only)

For this mode, you configure an internal IP address and an internal subnet mask for addressing the router in the internal subnet in the local security settings. All network requests that do not belong to a subnet are forwarded by the security module to a different subnet.

Note: In contrast to the bridge mode of the security module, VLAN tags are lost in routing mode.

1. Select the "Routing mode" option under "Mode" in the local security settings.
2. In the local security settings, enter an internal IP address and an internal subnet mask for addressing the router on the internal subnet in the input boxes under "Internal interface [P2] green" > Ethernet addresses".

#### Overview of NAT/NAPT

##### Requirements

- The security module is in routing mode or the DMZ interface is activated (SCALANCE S623 / S627-2M only).
- Since firewall rules that enable communication in the configured address translation direction are generated automatically for NAT / NAPT rules, the advanced firewall mode and the firewall in the editor for IP rules must be enabled for the security module. For more detailed information, refer to section [Relationship between NAT/NAPT router and firewall](#relationship-between-natnapt-router-and-firewall)

##### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "NAT / NAPT".
3. Call the appropriate editor with the "Open editor" button.
4. When required, configure address translation according to NAT (Network Address Translation) or NAPT (Network Address Port Translation).

##### Address translation with NAT (Network Address Translation)

NAT is a procedure for address translation between two address spaces.  
The main task is to translate private addresses into public addresses; in other words into IP addresses that are used and even routed on the Internet. As a result, the IP addresses of the internal network are not known to the outside in the external network. The internal nodes are only visible to the external network by means of external IP address that is specified in the address translation list (NAT table). If the external IP address is not the address of the security module and if the internal IP address is unique, this is known as 1:1 NAT. With 1:1 NAT, the internal address is translated to this external address without port translation. Otherwise, n:1 NAT is being used.

##### Address translation with NAPT (Network Address Port Translation)

The address translation with NAPT changes the target address and the target port to a communication relation (port forwarding).

Frames coming from the external network or DMZ network and intended for the IP address of the security module are translated. If the destination port of the frame is identical to one of the values specified in the "Source port" column, the security module replaces the destination IP address and the destination port as specified in the corresponding row of the NAPT table. With the reply, the security module uses the values for the destination IP address and destination port as contained in the initial frame as the source IP address and the source port.

The difference to NAT is that with this protocol ports can also be translated. There is no 1:1 translation of the IP address. There is now only a public IP address that is translated to a series of private IP addresses with the addition of port numbers.

##### Address translation in VPN tunnels

Address translations with NAT/NAPT can also be performed for communications relations established via a VPN tunnel. This is supported for connection partners of the type SCALANCE S612 / S623 / S627-2M as of V4.

You will find further information on address translations in VPN tunnels in the following sections:

- [NAT/NAPT routing](#natnapt-routing)
- [Address translation with NAT/NAPT in VPN tunnels](#address-translation-with-natnapt-in-vpn-tunnels)

##### Consistency check - these rules must be adhered to

Among other things, remember the following rules to obtain consistent entries:

- The IP address of the internal interface must not be used in the NAT / NAPT table.
- An IP address used in the NAT/NAPT address conversion list must not be a multicast or broadcast address.
- The external ports assigned for the NAPT translation are in the range > 0 and ≤ 65535.

  Port 123 (NTP), port 443 (HTTPS), port 514 (Syslog), port 161 (SNMP), ports 67+68 (DHCP) and ports 500+4500 (IPsec) are excluded if the relevant services are activated on the security module.
- The external IP address of the security module or the IP address of the DMZ interface may only be used in the NAT table for the action "Source NAT".
- Checking for duplicates in the NAT table

  An external IP address or an IP address in the DMZ network used in the direction "Destination NAT", "Source NAT +Destination NAT" or "Double NAT" may only be used once in each specified direction.
- Checking for duplicates in the NAPT table: A source port number may only be entered once for each interface.
- Internal NAPT ports can be in the range > 0 and ≤ 65535.

---

**See also**

[Overview of the routing settings](#overview-of-the-routing-settings)

#### NAT/NAPT routing

##### Address translation with NAT

The following control elements are available in the menu bar:

| Operator control element | Function |
| --- | --- |
| ![Address translation with NAT](images/105044676491_DV_resource.Stream@PNG-de-DE.png) | Enabling NAT  Enables the editor for NAT rules. If the editor is enabled, the corresponding rules can be configured and are transferred to the module during loading.  Since IP rules that enable communication in the configured address translation direction are generated automatically for NAT rules, the editor for NAT rules can only be enabled when advanced firewall mode is enabled with an active IP firewall. |
| ![Address translation with NAT](images/101505139467_DV_resource.Stream@PNG-de-DE.png) | Insert rule above  Inserts a rule above the selected rule / the selected rule set. To insert above a rule set, its first line must be selected. |
| ![Address translation with NAT](images/101505647755_DV_resource.Stream@PNG-de-DE.png) | Insert rule below  Inserts a rule below the selected rule / the selected rule set. To insert below a rule set, its first line must be selected. |
| ![Address translation with NAT](images/101505950987_DV_resource.Stream@PNG-de-DE.png) | Move up  Moves the selected rule / the selected rule set one line up. To move a rule set, its first line must be selected. |
| ![Address translation with NAT](images/101505959819_DV_resource.Stream@PNG-de-DE.png) | Move down  Moves the selected rule / the selected rule set one line down. To move a rule set, its first line must be selected. |
| ![Address translation with NAT](images/101506237451_DV_resource.Stream@PNG-de-DE.png) | Expand rule sets  Shows existing rule sets expanded. |
| ![Address translation with NAT](images/101506348683_DV_resource.Stream@PNG-de-DE.png) | Collapse rule sets  Shows existing rule sets collapsed. |
| ![Address translation with NAT](images/101841147147_DV_resource.Stream@PNG-de-DE.png) | Separate  Converts the selected line into a separate rule or rules. If the first line of a rule set is selected, all rules of the rule set are converted into separate rules. If one rule contained in a rule set is selected, this is converted into a separate rule. In addition to this, the following rules of the rule set are converted into a separate rule set. |

After creating NAT rules, the corresponding firewall rules are generated and displayed in advanced firewall mode, see section:

[Relationship between NAT/NAPT router and firewall](#relationship-between-natnapt-router-and-firewall)

If PPPoE is activated for the external interface or the DMZ interface, with the action "Destination NAT" the external interface or the DMZ interface cannot be selected as a towards direction. When configuring the action "Source NAT", the IP address cannot be entered in the "Source translation" input box because this is obtained dynamically during runtime.

##### Possible address translations for NAT

The following tables show the input options for address translation with NAT.

##### Action "Destination NAT" - "Redirect"

The action "Destination NAT" can be performed in the following direction:

- External to internal

If the DMZ interface of the security module (SCALANCE S623/S627-2M only) is activated, the action "Destination NAT" can also be performed in the following directions:

- External to DMZ
- DMZ to internal
- DMZ to external

If the SCALANCE S module (only SCALANCE S612/S623/S627-2M as of V4) is in a VPN group and the tunnel interface is enabled, the "Destination NAT" action can also be performed in the following directions:

- Tunnel to internal
- Tunnel to external
- Tunnel to DMZ (only if the DMZ interface is activated)

The following applies, for example for the direction "external to internal": The destination IP address of a frame coming from the external network is checked to see whether it matches the IP address specified in the "Destination IP address" input box. If it matches, the frame is forwarded into the internal network by replacing the destination IP address of the frame with the IP address specified in the "Destination translation" input box. Access from external to internal using the external address is possible.

The following table shows the input required for the action "Destination NAT".

| Box | Possible entries | Meaning |
| --- | --- | --- |
| Source IP address | Not relevant for this action. | - |
| Source translation | Not relevant for this action. | - |
| Destination IP address | IP address in the source network | Destination IP address in the source network with which an IP address in the destination network will be accessed. The destination IP address must not match the IP address of the security module in the source network.  If the destination IP address in a frame matches the address entered, the address is replaced by the corresponding IP address in the destination network.  The specified destination IP address becomes the alias address. This means that the specified IP address is also registered as an IP address on the selected interface. Make sure that the alias address does not cause an IP address conflict in the network. The alias IP addresses of a security module are displayed under the entry "Alias IP addresses" of the relevant interface. |
| Destination translation | IP address in the destination network | The destination IP address is replaced by the IP address specified here. |
| No. | - | Consecutive number assigned by STEP 7 used to reference the firewall rule generated by STEP 7 for the NAT rule. |

##### Action "Source NAT" - "Masquerading"

The action "Source NAT" can be performed in the following direction:

- Internal to external

If the DMZ interface of the security module (SCALANCE S623/S627-2M only) is activated, the action "Source NAT" can also be performed in the following directions:

- Internal to DMZ
- External to DMZ
- DMZ to external

If the SCALANCE S module (only SCALANCE S612/S623/S627-2M as of V4) is in a VPN group and the tunnel interface is enabled, the "Source NAT" action can also be performed in the following directions:

- Internal to tunnel
- External to tunnel
- DMZ to tunnel (only if the DMZ interface is activated)

The following applies, for example for the direction "internal to external": The source IP address of a frame coming from the internal network is checked to see whether it matches the IP address specified in the "Source IP address" input box. If it matches, the frame with the external IP address specified in the "Source translation" input box is forwarded to the external network as a new source IP address. In the external network, the external IP address is effective.

The following table shows the input required for the action "Source NAT".

| Box | Possible entries | Meaning |
| --- | --- | --- |
| Source IP address | IP address in the source network | The source IP address of the specified node is replaced by the IP address specified in the "Source translation" input box. |
| IP address range / IP address band in the source network | The IP addresses of the IP address range / IP address band are replaced by the IP address specified in the "Source translation" input box. |  |
| * | The IP addresses of all nodes in the source network are replaced by the IP address specified in the "Source translation" input box. |  |
| Source translation | IP address in the destination network | Entry of the IP address that will be used as the new source IP address.  If the IP address entered here is not the IP address of the security module, this becomes an alias address. This means that the specified address is also registered as an IP address on the selected interface. Make sure that the alias address does not cause an IP address conflict in the network. The alias IP addresses of a security module are displayed under the entry "Alias IP addresses" of the relevant interface. |
| Destination IP address | Not relevant for this action. | - |
| Destination translation | Not relevant for this action. | - |
| No. | - | Consecutive number assigned by STEP 7 used to reference the firewall rule generated by STEP 7 for the NAT rule. |

> **Note**
>
> You can configure an address translation to the module IP address in the destination network for all frames going from a source network to a destination network. The security module also assigns a port number for each frame. This is an n:1 NAT address translation in which multiple IP addresses of the source network are translated to one IP address of the destination network.
>
> Enter, for example, the following parameters for the direction "internal to external":
>
> - Action: "Source NAT"
> - From: "Internal"
> - To "External"
> - Source IP address: "*"
> - Source translation: External IP address of the security module

##### Action "Source NAT + Destination NAT" - "1:1-NAT"

The action "Source NAT + Destination NAT" can be performed in the following direction:

- Internal to external

If the DMZ interface of the security module (SCALANCE S623/S627-2M only) is activated, the action "Source NAT + Destination" can also be performed in the following directions:

- Internal to DMZ
- External to DMZ
- DMZ to external

If the SCALANCE S module (only SCALANCE S612/S623/S627-2M as of V4) is in a VPN group and the tunnel interface is enabled, the "Source-NAT + Destination-NAT" action can also be performed in the following directions:

- External to tunnel
- Internal to tunnel
- DMZ to tunnel (only if the DMZ interface is activated)

The following applies, for example for the direction "internal to external": When accessing from internal to external, the action "Source NAT" is performed. When accessing from external to internal, the action "Destination NAT" is performed.

The following table shows the input required for the action "Source NAT + Destination NAT":

| Box | Possible entries | Meaning |
| --- | --- | --- |
| Source IP address | IP address in the source network | The configuration is always specified in the source NAT direction. The IP addresses of the destination NAT direction are then inserted automatically by STEP 7. |
| Source translation | IP address in the destination network |  |
| Destination IP address | Not relevant for this action. |  |
| Destination translation | Not relevant for this action. |  |
| No. | - | Consecutive number assigned by STEP 7 used to reference the firewall rules generated by STEP 7 for the NAT rule. |

##### Action "Double NAT"

The action "Double NAT" can be performed for SCALANCE S modules in the following directions:

- Internal to external
- External to internal

If the DMZ interface of the security module (SCALANCE S623/S627-2M only) is activated, the action "Double NAT" can also be performed in the following directions:

- Internal to DMZ
- External to DMZ
- DMZ to internal
- DMZ to external

In every direction, Source and Destination NAT always take place at the same time.  
The following applies, for example for the direction "external to internal": When accessing from external to internal, the source IP address of the external node is replaced (Source NAT). Access to the internal network also uses the external IP address specified in the "Destination IP address" input box (Destination NAT).

You can, for example, use this action if a standard router other than the security module is entered for a device to be accessed using Destination NAT. Response frames from this device are then not sent to the entered standard router but to the corresponding interface of the security module.

The following table shows the input required for the action "Double NAT":

| Box | Possible entries | Meaning |
| --- | --- | --- |
| Source IP address | IP address in the source network | IP address of the node in the source network |
| Source translation | - | The Source NAT address translation is always to the IP address of the security module in the destination network. For this reason, the "Source translation" input box cannot be configured. |
| Destination IP address | IP address in the source network | Destination IP address in the source network with which an IP address in the destination network will be accessed.  If the destination IP address in a frame matches the IP address entered, the IP address is replaced by the IP address specified in the "Destination translation" input box.  If the IP address entered here is not the IP address of the security module, this becomes an alias address. This means that the specified address is also registered as an IP address on the selected interface. Make sure that the alias address does not cause an IP address conflict in the network. The alias IP addresses of a security module are displayed under the entry "Alias IP addresses" of the relevant interface. |
| Destination translation | IP address in the destination network | The destination IP address is replaced by the IP address specified here. |
| No. | - | Consecutive number assigned by STEP 7 used to reference the firewall rule generated by STEP 7 for the NAT rule. |

##### Advanced NAT editor

After selecting a NAT rule, an advanced NAT editor appears in the Inspector window in "Properties > General" and is used for simplified configuration of address ranges for ports and IP addresses. Changes made in this editor are adopted in the selected NAT rule. In addition, selected NAT rules and NAT rule sets can be copied in the advanced NAT editor. To copy a NAT rule set, its first line must be selected. You can specify which of the copied NAT rules is used by adapting the IP rules generated for the NAT rules. Based on examples, the following section illustrates the configuration of address ranges in the advanced NAT editor.

##### Configuring address ranges in the advanced NAT editor

Address ranges can be configured in the text boxes of the "From" and "To" columns. If several address ranges are configured for a NAT rule, the number of addresses must match in each case. After configuring address ranges, STEP 7 creates a NAT rule set from the selected NAT rule that contains a corresponding NAT rule for each of the addresses.

In the text boxes for ports in the "To" column, the placeholder "*" can be used as an alternative. In this case, the port ranges and NAT rules affected are formed according to the other NAT parameters.

##### Address translation with NAPT

The following control elements are available in the menu bar:

| Operator control element | Function |
| --- | --- |
| ![Address translation with NAPT](images/105044684171_DV_resource.Stream@PNG-de-DE.png) | Activate NAPT  Enables the editor for NAPT rules. If the editor is enabled, the corresponding rules can be configured and are transferred to the module during loading. After selecting a NAPT rule, the editor for advanced NAPT settings is available In the "Properties" > "General" tab of the Inspector window. |
| ![Address translation with NAPT](images/101505139467_DV_resource.Stream@PNG-de-DE.png) | Insert rule above  Inserts a rule above the selected rule / the selected rule set. To insert above a rule set, its first line must be selected. |
| ![Address translation with NAPT](images/101505647755_DV_resource.Stream@PNG-de-DE.png) | Insert rule below  Inserts a rule below the selected rule / the selected rule set. To insert below a rule set, its first line must be selected. |
| ![Address translation with NAPT](images/101505950987_DV_resource.Stream@PNG-de-DE.png) | Move up  Moves the selected rule / the selected rule set one line up. To move a rule set, its first line must be selected. |
| ![Address translation with NAPT](images/101505959819_DV_resource.Stream@PNG-de-DE.png) | Move down  Moves the selected rule / the selected rule set one line down. To move a rule set, its first line must be selected. |
| ![Address translation with NAPT](images/101506237451_DV_resource.Stream@PNG-de-DE.png) | Expand rule sets  Shows existing rule sets expanded. |
| ![Address translation with NAPT](images/101506348683_DV_resource.Stream@PNG-de-DE.png) | Collapse rule sets  Shows existing rule sets collapsed. |
| ![Address translation with NAPT](images/101841147147_DV_resource.Stream@PNG-de-DE.png) | Separate  Converts the selected line into a separate rule or rules. If the first line of a rule set is selected, all rules of the rule set are converted into separate rules. If one rule contained in a rule set is selected, this is converted into a separate rule. In addition to this, the following rules of the rule set are converted into a separate rule set. |

After creating NAPT rules, the corresponding firewall rules are generated and displayed in advanced firewall mode, see section:  
[Relationship between NAT/NAPT router and firewall](#relationship-between-natnapt-router-and-firewall)

The IP address translation with NAPT can be performed in the following direction:

- External to internal

If the DMZ interface of the security module (SCALANCE S623/S627-2M only) is activated, the IP address translation with NAPT can also be performed in the following directions:

- External to DMZ
- DMZ to internal
- DMZ to external

If the SCALANCE S module (only SCALANCE S612/S623/S627-2M as of V4) is in a VPN group and the tunnel interface is enabled, the IP address translation with NAPT can also be performed in the following directions:

- Tunnel to internal
- Tunnel to external
- Tunnel to DMZ (only if the DMZ interface is activated)

The following applies, for example for the direction "external to internal": Frames intended for the external IP address of the security module and for the port entered in the "Virtual port" column are forwarded to the specified destination IP address in the internal network and to the specified destination port.

The IP address from which the frames of forwarded into the target network is displayed in the column "Virtual IP address". With a direction from external this is the external IP address of the security module and with a direction from DMZ the IP address of the DMZ interface of the security module.

The following table shows the input required for address translation with NAPT in the "NAPT" tab.

| Box | Possible entries | Meaning |
| --- | --- | --- |
| Virtual port | TCP/UDP port or port range  Example of entering a port range: 78:99 | A node in the source network can send a frame to a node in the destination network by using this port number. |
| Destination IP address | IP address in the destination network | Frames intended for the IP address of the security module in the source network and the TCP/UDP port specified in the "Virtual port" box are forwarded to the IP address specified here. |
| Destination port | TCP/UDP port | Port number to which the frames coming from the source network are forwarded. |
| Protocol | - TCP+UDP - TCP - UDP | Selection of the protocol family for the specified port numbers |
| No. | - | Consecutive number assigned by STEP 7 used to reference the firewall rule generated by STEP 7 for the NAPT rule. |

##### Advanced NAPT editor

After selecting a NAPT rule an advanced NAPT editor appears in the Inspector window in "Properties > General" and is used for simple configuration of address ranges for ports and IP addresses. Changes made in this editor are adopted in the selected NAPT rule. In addition to this, selected NAPT rules and NAPT rule sets can be copied in the advanced NAPT editor. To copy a NAPT rule set its first line must be selected. Which of the copied NAPT rules is used, can be specified by adapting the IP rules generated for the NAPT rules. Based on examples, the following section illustrates the configuration of address ranges in the advanced NAPT editor.

##### Configuration of address ranges in the advanced NAPT editor.

Address ranges can be configured in the text boxes of the "From" and "To" columns. If several address ranges are configured for a NAPT rule, the number of addresses must match in each case. After configuring address ranges, STEP 7 creates a NAPT rule set from the selected NAPT rule that contains a corresponding NAPT rule for each of the addresses.

The following example shows the configuration of address ranges for the virtual port, for the destination IP address and for the destination port.

![Advanced NAPT editor: Example 1](images/105132563211_DV_resource.Stream@PNG-en-US.png)

Advanced NAPT editor: Example 1

In the text boxes for ports in the "To" column, the placeholder "*" can be used as an alternative. In this case, the port ranges and NAPT rules affected are formed according to the other NAPT parameters.

In the following example the port ranges for the virtual port and the destination port are determined by STEP 7:

![Advanced NAPT editor: Example 2](images/105133966859_DV_resource.Stream@PNG-en-US.png)

Advanced NAPT editor: Example 2

To configure the same port range for every NAPT rule of a NAPT rule set, you can specify the start and end port of the port range for the virtual port in the "From" column separated by a colon. For the destination port, such a port range cannot be specified. A placeholder "*" after the colon is interpreted as the maximum value 65535.

In the following example a port range with the explained notation is used for every NAPT rule of the NAPT rule set:

![Advanced NAPT editor: Example 3 (NAPT rules)](images/105138498315_DV_resource.Stream@PNG-en-US.png)

Advanced NAPT editor: Example 3 (NAPT rules)

In example 3, the virtual IP address and the virtual port are identical for every NAPT rule. In this case which NAPT rule is used is decided by the priority of the firewall rules, created by STEP 7 for the NAPT rules. The firewall rule that was created for the NAPT rule with the number NAPT_1.1 has the highest priority.

![Advanced NAPT editor: Example 3 (firewall rules)](images/105138751755_DV_resource.Stream@PNG-en-US.png)

Advanced NAPT editor: Example 3 (firewall rules)

For this reason all frames intended for the IP address 192.168.0.1 and for a port in the range 85...90 are forwarded to destination IP address 192.168.1.5 and to destination port 95.

To uniquely define NAPT rules with the same virtual IP address and same virtual port / port range, source IP addresses can be configured in the relevant IP rules. The source IP addresses then decide which NAPT rule is used.

![Advanced NAPT editor: Supplement to example 3](images/105139517195_DV_resource.Stream@PNG-en-US.png)

Advanced NAPT editor: Supplement to example 3

#### Address translation with NAT/NAPT in VPN tunnels

##### Module-specific function

Address translation with NAT/NAPT in VPN tunnels is only available for SCALANCE S612/S623/S627-2M modules as of V4, refer to the section:  
[Address translation with NAT/NAPT in VPN tunnels](#address-translation-with-natnapt-in-vpn-tunnels-1)

#### Relationship between NAT/NAPT router and firewall

##### Meaning

After creating NAT/NAPT rules, STEP 7 automatically generates firewall rules that enable communication in the configured address translation direction. The generated firewall rules are visible as firewall rule sets in advanced firewall mode and can, if necessary, be expanded (additional IP address / IP address range / IP address band, services, transmission speed). In addition to this, the automatically generated firewall rules should be checked in terms of their priority and their position. If there are also manually configured firewall rules in the rule list that have higher priority than the automatically generated firewall rules, under certain circumstances no NAT / NAPT will be performed.

If there are several identical NAT / firewall pairs of rules, the priority in the firewall rule list decides which rule is used.

Firewall parameters generated by STEP 7 cannot be adapted. After deactivating NAT/NAPT, the firewall rules generated by STEP 7 are disabled.

To clarify the relationship between the NAT/NAPT rules and the corresponding firewall rules, they are identified by corresponding, consecutive numbers.

In firewall rules that were generated automatically for NAT/NAPT rules, the “Stateful” check box cannot be disabled.

The following table shows the system behind the firewall rules generated for NAT rules for SCALANCE S modules.

NAT address translation and corresponding firewall rules for SCALANCE S modules

| NAT action | Created firewall rule |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Action | From | To | Source IP address | Destination IP address |  |
| Destination NAT | Accept | Source network | Destination network | - | IP address specified in the "Destination IP address" input box |
| Source NAT | Accept | Source network | Destination network | IP address of the node specified in the "Source IP address" input box | - |
| Source NAT + Destination NAT | Accept | Source network | Destination network | IP address of the node specified in the "Source IP address" input box | - |
| Accept | Destination network | Source network | - | IP address that was inserted in the "Destination IP address" input box by STEP 7 |  |
| Double NAT | Accept | Source network | Destination network | IP address of the node specified in the "Source IP address" input box | IP address specified in the "Destination IP address" input box |
| Accept | Source network | Destination network | IP address of the node specified in the "Source IP address" input box | IP address of the node specified in the "Destination translation" input box |  |

The following table shows the system behind the firewall rules generated for NAT rules for CP 343-1 Adv. / CP 443-1 Adv.

NAT address translation and corresponding firewall rules for CP 343-1 Adv. / CP 443-1 Adv.

| NAT action | Created firewall rule |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Action | From | To | Source IP address | Destination IP address |  |
| Destination NAT | Drop | External | Station | - | IP address of the security module in the external network |
| Accept | External | Any | - | IP address of the node specified in the "Destination translation" input box |  |
| Source NAT | Accept | Any | External | IP address specified in the "Source translation" input box | - |
| Source NAT + Destination NAT | Accept | Any | External | IP address specified in the "Source translation" input box | - |
| Drop | External | Station | - | IP address of the security module in the external network |  |
| Accept | External | Any | - | IP address of the node that was inserted in the "Destination translation" input box by STEP 7 |  |

The following table shows the system behind the firewall rules generated for NAT rules for SCALANCE S modules.

NAPT translation and firewall rules created for SCALANCE S modules

| Created firewall rule |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Action | From | To | Source IP address | Destination IP address | Service |
| Accept | Source network | Destination network | - | IP address of the security module in the source network | [Service_NAPT_rule] |

The following table shows the system behind the firewall rules generated for NAPT rules for CP 343-1 Adv. / CP 443-1 Adv.

NAPT translations and created firewall rules for CP 343-1 Adv. / CP 443-1 Adv.

| Created firewall rules |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Action | From | To | Source IP address | Destination IP address | Service |
| Drop | External | Station | - | IP address of the security module in the external network | [Service_NAPT_rule] |
| Accept | External | Any | - | IP address of the security module in the external network | [Service_NAPT_rule] |

##### Stateful packet inspection

The firewall and NAT/NAPT router supports the "Stateful Packet Inspection" mechanism. As a result, reply frames can pass through the NAT/NAPT router and firewall without it being necessary for their addresses to be included extra in the firewall rule and the NAT/NAPT address translation.

#### Relationship between NAT/NAPT router and user-specific firewall

##### Module-specific function

The configuration of NAT/NAPT rules in the user-specific firewall is only available for SCALANCE S modules as of V3, refer to the section:

[Relationship between NAT/NAPT router and user-specific firewall](#relationship-between-natnapt-router-and-user-specific-firewall-1)

### Configuring time-of-day synchronization

This section contains information on the following topics:

- [Procedure for time-of-day synchronization](#procedure-for-time-of-day-synchronization)
- [Configuring time-of-day synchronization for a security module](#configuring-time-of-day-synchronization-for-a-security-module)
- [Configuring NTP servers](#configuring-ntp-servers)
- [Assigning the security module to an NTP server (secure)](#assigning-the-security-module-to-an-ntp-server-secure)

#### Procedure for time-of-day synchronization

##### Meaning

For the time synchronization of the transfer of productive data, the date and time are maintained on the security module to verify the validity (time) of a certificate and for time stamping log entries. For the Security functions the time of day of the security modules of a project must be synchronized.

> **Note**
>
> **Configuring the firewall for communication with NTP servers**
>
> If the NTP server cannot be reached by the security module, you will need to allow the frames from the NTP server explicitly in the firewall (UDP, port 123).

> **Note**
>
> Time-of-day synchronization relates solely to the security module and cannot be used to synchronize devices in the internal network of the security module.
>
> Some CPs can forward the time of day to other module of the station.
>
> The CP 443‑1 OPC UA can only receive the time-of-day in the SIMATIC mode from the station but cannot forward it.

> **Note**
>
> Before the security functions of a CP (time-of-day slave) are used, the CP must receive a valid time-of-day frame from the time master.

#### Configuring time-of-day synchronization for a security module

##### How to access this function

1. Select the module to be edited.
2. Select the "Time-of-day synchronization" entry in the local security settings.
3. Select the "Activate time-of-day synchronization" check box.

##### Procedure for time-of-day synchronization

Depending on the security module being used, the following methods can be configured:

| Procedure | Meaning |
| --- | --- |
| Set time with each download | The module time is set automatically to the PC time when a configuration is downloaded. |
| SIMATIC | Time-of-day synchronization by received MMS time-of-day messages (MMS = Manufacturing Message Specification)  For the CP select whether the CP is to adopt or forward the time of day. The CP 1628 always forwards the time of day. The CP 443‑1 OPC UA uses the SIMATIC mode if no time-of-day synchronization using NTP is configured. It can only receive the time-of-day from the station but cannot forward it.  Available directions:  - Automatic   The CP receives the time from the station or from the LAN and forwards it to the station or to the LAN. If several CPUs are being operated in the station, the default setting can lead to collisions. To avoid this, you should specifically define the forwarding direction. - From station   The CP forwards the time of day to the LAN. - From LAN   The CP forwards the time of day from the LAN to the station.   If forwarding of the time of day is enabled, you can use the "Use corrected time" check box to specify whether or not a correction factor included in the time-of-day frame is used. For the CP 1628, this option is is the default and it cannot be disabled. |
| Time of day from partner | The time is obtained from the relevant communications partner.  Synchronization cycle: Specifies the cycle for time-of-day synchronization. For the synchronization cycle of the CP, and individual hour or minute interval can be specified. |
| NTP / NTP (secure) | Time-of-day synchronization by an NTP server / NTP server of the type "NTP (secure)".  - Time zone: In NTP mode, it is generally UTC (Universal Time Coordinated) that is transferred. This corresponds to GMT (Greenwich Mean Time). The time offset from UTC can be set by configuring the local time zone. - Update interval in seconds: Specifies the interval between the time queries in seconds. For SCALANCE S as of V3, the time interval for querying the NTP server is specified automatically.   If the "Enable security functions" check box is enabled in the local security settings of a CP, the setting for the update interval is transferred from the CP's local settings into the CP's local security settings. - Time synchronization on the full minute: With this option, you specify that the time of day is forwarded to the communications bus on the full minute. This option is required for certain special applications. - Accept time from non-synchronized NTP servers Here you can specify whether the security module also accepts the time-of-day from non-synchronized NTP servers. - Forward time of day to station: Disable this option if the CPU requests the time separately from an NTP server. This prevents the time on the CPU obtained directly from the NTP server from being overwritten by the time detected in the CP. The accuracy may be reduced slightly due to forwarding via the CP. - NTP server: Creating NTP servers in the local security settings is described in the section [Configuring NTP servers](#configuring-ntp-servers). |

#### Configuring NTP servers

##### Creating NTP servers of the type "NTP (secure)" in the global security functions

In the global security functions, only NTP servers of the type "NTP (secure)" can be created and assigned to devices.

| 1. In the global security functions, select the entry "NTP". Result: The previously created NTP servers (secure) are displayed under the selected entry. 2. Double-click on the "Add new NTP server" entry. Result: The created NTP server (secure) is displayed with an automatically assigned number below the entry "NTP". 3. Double-click on the created NTP server (secure). Result: In the working area the assignment dialog for NTP servers (secure) is displayed. The selected NTP server (secure) is selected in the "NTP server" drop-down list. The required security modules can be assigned to this, see section [Assigning the security module to an NTP server (secure)](#assigning-the-security-module-to-an-ntp-server-secure). In the local security settings, the configurable properties of the NTP server (secure) are displayed. 4. Enter the following data in the "General" entry in the local security settings:    - Name: A maximum of 25 characters can be used for the name of the NTP server (secure).    - IP address / FQDN: Address of the NTP server (secure).    - Port: NTP server port. The following ports are possible: 123 (default port), 1025 to 36564.    - Synchronization cycle: Interval between two-time queries in seconds. Possible values are 16 to 16284 seconds. 5. Enter the following encryption parameters in the "NTP keys" entry in the local security settings:       | Property | Meaning |    | --- | --- |    | Key ID | Numeric value between 1 and 65534. |    | Hash algorithm | Select the hash algorithm. Observe the length for the NTP key depending on the selection. |    | Hex/ASCII | Select the format for the NTP key. |    | Key | Enter the NTP key. SCALANCE S-600 / S7-CPs Selection MD5 or SHA-1: - Hex: 10 ... 40 characters - ASCII: 5 ... 20 charactersTIM, CP 1628 Selection MD5 or SHA-1: - Hex: 22 ... 40 characters - ASCII: 11 ... 20 charactersSCALANCE SC-600 Selection MD5: - ASCII: 16 ... 128 charactersSelection SHA1: - ASCII: 20 ... 128 charactersSelection DES: - ASCII: 8 charactersThe numbers of characters listed cover all key lengths supported by the security modules. |     To switch over to the local security settings of another NTP server (secure), select this from the "NTP server" drop-down list of the assignment dialog or double-click on the corresponding entry in the global security functions. |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Result

You have created the NTP server (secure) and can now assign it to the required security modules.  
Note the descriptions in the following section:  
[Assigning the security module to an NTP server (secure)](#assigning-the-security-module-to-an-ntp-server-secure)

##### Creating non-secure NTP servers in the local security settings

Non-secure NTP servers must be created in the local security settings

1. Select the module to be edited.
2. Select the "Time-of-day synchronization" entry in the local security settings.
3. Select the synchronization method..
4. Enter a name and the IP address of the NTP server. A maximum of 25 characters can be used for the name. If you have selected the "NTP (secure)" synchronization mode, you can select an NTP server (secure) that you created in the global security functions in the "Name" column.

##### Conventions for names of NTP servers

The characters 0-9, a-z, A-Z, -._ can be used for the names of NTP servers. A name must start with a letter and end with a letter or number. Before the ‘.’ character only letters and numbers are permitted, after the ‘.’ character only letters. Before the ‘_’ or ‘-' character only letters and numbers are permitted.

##### Importing/exporting key list of NTP servers (secure)

Using the "Import" or "Export" commands in the shortcut menu, you can export the key list of the currently selected NTP server (secure) in the global security functions and import the file into an NTP server (secure) or vice versa.

#### Assigning the security module to an NTP server (secure)

##### Requirement

- You have defined an NTP server (secure) in the global security functions.
- "NTP" or "NTP (secure)" is selected as the time-of-day synchronization mode in the local security settings of the security module that you want to assign to an NTP server (secure).

##### Procedure

1. Double-click on the "NTP" entry in the global security functions.
2. Double-click the entry "Assign module to an NTP server".
3. From the "NTP Server" drop-down list, select the NTP server (secure) to which you want to assign a security module.
4. In the "Available modules" section, select the security module that you want to assign to the selected NTP server (secure).
5. Click the "<<" button to assign the selected security module to the selected NTP server (secure).

##### Result

You have assigned the security module to the NTP server (secure). The NTP server (secure) is displayed automatically in the local security settings in the list of NTP servers.

### Security module as DHCP server

#### Module-specific function

The use of the security module as a DHCP server is only possible with SCALANCE S modules, see section:  
[Security module as DHCP server](#security-module-as-dhcp-server-1)

### Configuring SNMP

This section contains information on the following topics:

- [Overview of SNMP](#overview-of-snmp)
- [Configuring SNMP - "SNMP" entry](#configuring-snmp---snmp-entry)

#### Overview of SNMP

##### What is SNMP?

The security module supports the transfer of management information using the Simple Network Management Protocol (SNMP). For this purpose, an SNMP agent that receives and responds to SNMP requests is installed on the security module. The information on the properties of SNMP­compliant devices is entered in MIB files (MIB = Management Information Base) for which the user must have the required rights.

In SNMPv1, the "community string" is also sent. The "community string" is like a password that is transmitted along with the SNMP request. If the community string is correct, the security module replies with the required information. If the string is incorrect, the security module discards the query and does not reply. The community string is transmitted via SNMPv1 without encryption.

SNMPv3 lets you transmit encrypted data.

#### Configuring SNMP - "SNMP" entry

##### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "SNMP".
3. Activate the "Activate SNMP" check box.
4. Select one of the following SNMP protocol versions:

   - SNMPv1

     The security module uses the following default values for the community strings to control the access rights in the SNMP agent. These default values should be adapted to increase security.

     For read access: public

     For read and write access: private

     To enable write access using SNMP, select the "Allow write access" option.
   - SNMPv3

     Select either only an authentication algorithm or an authentication algorithm and an encryption algorithm.

     Authentication algorithm: none, MD5, SHA-1

     Encryption algorithm: none, AES-128, DES
5. If SNMPv3 is to be used, assign a user a role with corresponding activated SNMP rights to enable access to the module via SNMP. An overview of SNMP rights is available in the section:  
   [Special features of user management for security functions](#special-features-of-user-management-for-security-functions).
6. In the "Advanced settings" area, for SCALANCE S modules configure module-specific information about the author, location and e-mail address overwriting the information from the project properties.

   The following applies to values written to the security module by an SNMP tool using an SNMP-SET command:  
   If you select the "Keep values written by SNMP set" check box, the values are not overwritten when there is another download of a STEP 7 configuration to the security module.

**Note**

**Encrypted data transmission with SNMPv3**

You should use SNMPv3 to transmit data in encrypted form in order to enhance security.

**Note**

**Preventing the use of DES**

DES is an insecure encryption algorithm. Therefore, it should only be used for reasons of down compatibility.

**Note**

When using SNMPv3 no RADIUS authentication is possible.

### Configuring proxy ARP

#### Module-specific function

This function is available only for SCALANCE S V3 modules or higher, see section  
[Configuring proxy ARP](#configuring-proxy-arp-1)

### Activate Web server on security module

#### Module-specific function

This function is only available for CP 343-1 Advanced / CP 443-1 Advanced and CP 443-1 OPC UA see section:  
[Activating Web server on security module](#activating-web-server-on-security-module)in the section "Security for S7-300 / S7-400 / PC CPs".

### IPsec VPN tunnel: Creating and assigning VPN groups

This section contains information on the following topics:

- [How to create an IPsec tunnel with VPN groups](#how-to-create-an-ipsec-tunnel-with-vpn-groups)
- [Assigning a security module to a VPN group](#assigning-a-security-module-to-a-vpn-group)
- [Authentication methods](#authentication-methods)
- [VPN group properties](#vpn-group-properties)
- [Modes of VPN groups](#modes-of-vpn-groups)
- [Including security module in configured VPN group](#including-security-module-in-configured-vpn-group)
- [Configuring network nodes reachable through a tunnel](#configuring-network-nodes-reachable-through-a-tunnel)
- [Configuring module- and connection-specific VPN settings](#configuring-module--and-connection-specific-vpn-settings)

#### How to create an IPsec tunnel with VPN groups

##### Requirement

> **Note**
>
> **Current date and current time of day on the security modules**
>
> When using secure communication (for example, HTTPS, VPN...), make sure that the security modules involved have the current time of day and the current date. Otherwise the certificates used are not evaluated as valid and the secure communication does not work.

##### Creating a VPN group

1. In the global security functions, select the entry "VPN groups".  
   Result: The previously created VPN groups are displayed under the selected entry.
2. Double-click the "Add new VPN group" entry.  
   Result: The "Create certificate for VPN group" window opens. The VPN mode is inferred automatically.
3. If necessary, change the automatically created name under "Common name of subject"  
   Result: The created VPN group is displayed with the name you entered for "Common name of subject" below the "VPN groups" entry.

   Alternatively, you can right-click an interface of a module with VPN capability in the network view and create a VPN group with the shortcut menu command "Add new VPN group". The selected security module is automatically assigned to the created VPN group.
4. Double-click on the created VPN group.  
   Result: In the working area the assignment dialog for VPN groups sets is displayed. The selected VPN group is selected in the "VPN" drop-down list. Security modules can be assigned to this in the relevant assignment dialog, see section [Assigning a security module to a VPN group](#assigning-a-security-module-to-a-vpn-group). In the local security settings, the VPN group properties of the selected VPN group can be adapted, see section [Configuring VPN group properties](#configuring-vpn-group-properties).

##### Conventions for names of VPN groups / common names of subject

The characters 0-9, a-z, A-Z, -._ can be used for the names of VPN groups. A name must start with a letter and end with a letter or number. Before the ‘.’ character only letters and numbers are permitted, after the ‘.’ character only letters. Before the ‘_’ or ‘-* character only letters and numbers are permitted.

##### Display of the VPN groups with their properties

If you select a security module that is in one or more VPN group(s), the properties of the VPN group(s) of which the security module is a member are shown in the "Network data" area.

![Display of the VPN groups with their properties](images/77863791883_DV_resource.Stream@PNG-en-US.png)

The following properties of the VPN groups are displayed in columns in the "VPN" tab of the "Network data" area:

| Property/column | Meaning |
| --- | --- |
| VPN | Names of the VPN groups of which the selected security module is member |
| Security module | Names of the assigned security modules |
| Authentication | Type of authentication: Pre-shared key or certificate |
| Group membership until | Date and time up to which the VPN group certificate of the security module is valid |
| Type | Model numbers of the assigned security modules |
| Comment | Comment |

##### Setting the life of certificates

Open the dialog in which you can set the expiry date of the certificate as follows:

1. Select the VPN group you want to edit in the "VPN" tab.
2. In the "Properties" > "General" tab of the Inspector window, select the entry "Authentication".

**Note**

**Expiry of a certificate**

Communication through the VPN tunnel continues after the certificate has expired until the tunnel is terminated or the SA lifetime expires. For more information on certificates, refer to section:  
[Managing certificates](#managing-certificates).

##### Configuration limits

| Number of the VPN tunnel |  |
| --- | --- |
| SCALANCE S612 V4 | Maximum of 128 |
| SCALANCE S623 V4 | Maximum of 128 |
| SCALANCE S627-2M V4 | Maximum of 128 |
| CP 343-1 Advanced / CP 443-1 Advanced | Maximum of 32 |
| CP 1628 | Maximum of 64 |
| S7-1200 CPs/ET 200SP CPs | Maximum of 8 |
| S7-1500 CPs | Maximum of 16 |

For the number of communications relations between subnets of the security module and subnets of other security modules that can be reached via VPN tunnel the following configuration limits apply:

| Number of subnet relations |  |
| --- | --- |
| SCALANCE S612 V4 | Maximum of 128 |
| SCALANCE S623 V4 | Maximum of 128 |
| SCALANCE S627-2M V4 | Maximum of 128 |
| CP 343-1 Advanced / CP 443-1 Advanced | Maximum of 32 |
| CP 1628 | Maximum of 64 |
| S7-1200 / S7-1500 CPs | Maximum of 8 |

#### Assigning a security module to a VPN group

##### Requirements

- You have defined a VPN group in the global security functions. Before assigning security modules to VPN groups, note the rules for this in the section [Modes of VPN groups](#modes-of-vpn-groups).
- VPN must be activated for the following modules before they are assigned to VPN groups.

  VPN connection type "Internet Key Exchange (IKE)" can be selected for the following modules:

  - CP 1243-1 as of V3.1
  - CP 1243-8 IRC as of V3.1
  - CP 1243-7 LTE as of V3.1
  - CP 1543SP-1 as of V2

  VPN connection type "Internet Key Exchange (IKE) v2" can be selected for the following modules:

  - CP 124xx as of V3.5
  - CP 1543SP-1 as of V2.3
  - CP1543-1 as of V4.0
  - CP1545-1 as of V2.0

##### Procedure

1. Double-click on the "VPN groups" entry in the global security functions.
2. Double-click on the "Assign module to a VPN group" entry.
3. From the "VPN" drop-down list, select the VPN group to which you want to assign a security module.
4. In the "Available modules" section, select the security module that you want to assign to the selected VPN group.
5. Click the "<<" button to assign the selected security module to the selected VPN group.

   If the security module doe not support one or more properties of the VPN group box, the module symbol in the area of the assigned modules is displayed with an error symbol ![Procedure](images/95396201483_DV_resource.Stream@PNG-de-DE.png).

   As an alternative to the procedure , in the network view you can assign a security module to an existing VPN group by right clicking on an interface of a module with VPN capability and assign this to the VPN group using the shortcut menu "Assign module to a VPN group" (not possible for SOFTNET Security Client).

##### Result

You have assigned the security module to the VPN group.

#### Authentication methods

##### The following methods are available:

The authentication method is specified per VPN group and decides the type of authentication used.

The following key-based or certificate-based authentication methods are supported:

- Pre-shared key

  Authentication is achieved using a previously specified character string that is distributed to all modules in the group.

  Enter a pre-shared key in the "Key" field under "Authentication" > "General" in the VPN group properties dialog. If you click the "Renew preshared key" button, STEP 7 renews the pre-shared key to be used.
- Certificate

  Certificate-based authentication "Certificate" is the default setting. The procedure is as follows:

  - When a group is created, a CA certificate is generated as a root certificate.
  - Each security module that is a member of the VPN group also receives a group certificate signed with the key of the CA certificate.

  If you click the "Renew certificate " button, STEP 7 renews the CA certificate of the VPN group.

  All certificates are based on the ITU standard X.509v3 (ITU, International Telecommunications Union).

  The certificates are generated by a certificate authority contained in STEP 7.

  > **Note**
  >
  > **Restriction in VLAN operation**
  >
  > No VLAN tagging is transmitted in IP frames via the VPN tunnel of the security module. The VLAN tags included in IP frames are lost when they pass through the security modules because IPsec is used to transfer the IP frames.
  >
  > As default, no IP broadcast or IP multicast frames can be transferred with IPsec through a layer 3 VPN tunnel. Through a layer 2 VPN tunnel of the security module, IP broadcast or IP multicast frames are packaged just like MAC packets including the Ethernet header in UDP and transferred. With these packets, the VLAN tagging is therefore retained.

#### VPN group properties

This section contains information on the following topics:

- [VPN connection establishment by Known Peers and Unknown Peers](#vpn-connection-establishment-by-known-peers-and-unknown-peers)
- [Configuring VPN group properties](#configuring-vpn-group-properties)

##### VPN connection establishment by Known Peers and Unknown Peers

The properties of a VPN group are made up of the selected authentication method and the configured parameters for IKE phase 1 and 2 and during loading are transferred to all VPN group nodes. On the responder the IP addresses of the security modules that may initiate the VPN connection establishment with the configured properties of the VPN group are stored in addition. When a security module attempts to establish a VPN connection to the responder, this first checks whether the IP address of the initiator is known to it. If this is the case, the initiator is a Known Peer. If the VPN group properties proposed by this Known Peer match those stored on the responder for the Known Peer, the responder allows the VPN connection establishment. In addition to the properties of a VPN group, fallback VPN profiles can be assigned to a VPN group. VPN profiles contain predefined properties for the authentication method, IKE phase 1 and 2. Fallback VPN profiles can be used for SCALANCE S-600, CP 343-1 Adv. / CP 443-1 Adv. and CP 1628 as alternative configurations for VPN connection establishment. These come into play when VPN properties of the initiator do not match the VPN properties of the responder. In such cases, fallback VPN profiles ensure the VPN connection establishment. The configured fallback VPN profiles just as the properties of the VPN group are transferred to all VPN group nodes. The priority for the use of the fallback VPN profiles is specified by their order in the configuration. The fallback VPN profiles and the properties of the VPN group must not differ in the authentication method.

If the IP address of the initiator is not known to the responder because the initiator in productive mode for example is connected via a NAT translation, the initiator is an Unknown Peer (Road Warrior). As default the responder allows connection establishment by Unknown Peers. In the module-specific VPN properties of the responder, you can specify whether it allows connection establishment by Unknown Peers and, if so, the VPN group properties used, provided that the module is a SCALANCE S-600, CP 343-1 Adv. / CP 443-1 Adv. or CP 1628 module; see section [Configuring module- and connection-specific VPN settings](#configuring-module--and-connection-specific-vpn-settings).

##### Configuring VPN group properties

###### VPN group properties

> **Note**
>
> **Knowledge of IPsec necessary**
>
> To be able to set these parameters, you require IPsec experience. If you do not make or modify any settings, the defaults apply.

The following settings can be configured in the properties of a VPN group:

- Automatically set compatible VPN configuration (entry: "Settings")
- Authentication method (entry: "General")
- IKE settings (entry: "Advanced settings phase 1")
- IPsec settings (entry: "Advanced settings phase 2")
- Fallback VPN profiles

If the VPN group properties you have configured are less secure than the recommended properties, STEP 7 makes this known to you with an appropriate message text.

###### How to access this function

1. In the global security functions select the VPN group with properties you want to configure under the entry "VPN groups".
2. Select "Open" in the shortcut menu of this entry.

   Result: The VPN group properties appear in the area of the local security settings under "Authentication".
3. Under the "Settings" entry, select whether the compatible VPN configuration should be set automatically. When the function is activated, the settings of the individual group members according to the supported device functions are changed so that they correspond to the optimum security requirements.
4. Under the "General" entry, select whether to use a pre-shared key or certificate for authentication. For more detailed information, refer to section:  
   [Authentication methods](#authentication-methods).
5. Select the IKE version. Depending on the selection, various options are available in the "Advanced settings".

###### Advanced settings phase 1

Phase 1: IKE negotiation of the Security Association (SA) for phase 2:

Here you set the parameters for negotiating the security parameters to be used in phase 2:

The following VPN group properties are supported by the individual modules:

| Module | IKE version | Phase 1 |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| IKE mode | DH group | SA lifetime | Encryption | Authentication |  |  |
| CP 1543-1 (as of V2.1)  CP 1543SP-1 (V2.0)  CP 1243-1 BX30 (as of V3.0)  CP 1243-7 LTE BX30 (as of V3.0)  CP 1243-8 IRC BX30 (as of V3.0) | IKEv1 | Main | Group 1  Group 2  Group 5  Group 14  Group 15 | Time: 1440 … 2500000 minutes | AES-256, 192, 128*: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |
| CP 1543-1 (up to 2.0)  CP 1543SP-1 (V1.0)  CP 1243-1 BX30 (up to V2.1)  CP 1243-7 LTE BX30 (V2.1)  CP 1243-8 IRC BX30 (V2.1) | IKEv1 | Main | Group 1  Group 2  Group 5  Group 14 | Time: 1440 … 2500000 minutes | AES-256, 192, 128*: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |
| CP 343-1 GX31 Advanced  CP 443-1 GX30 Advanced  CP 443-1 OPC UA  CP 1628  SCALANCE S-600 as of V3 | IKEv1 | Main | Group 1  Group 2  Group 5  Group 14 | Time: 1440 … 2500000 minutes | AES-256, 192, 128*: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |
| SOFTNET Security Client V4, V5 (WinXP) | IKEv1 | Main | Group 2  Group 14 | Time: 1440 … 2879 minutes | 3DES-168**: Triple DES***  DES | SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |
| Security device configured as  SOFTNET Security Client V5 (Win7) | IKEv1 | Main | Group 2  Group 14 | Time: 1440 … 2879 minutes | AES-256, 192, 128*: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |
| MD741-1 V1.1, M875 V2.0 | IKEv1 | Main | Group 2 | Time: 1440 … 2500000 minutes | 3DES-168**: Triple DES*** | SHA-1***: Secure Hash Algorithm 1 |
| Security device configured as VPN client  VPN server | IKEv1 | Main  Aggressive | Group 1  Group 2  Group 5  Group 14 - Group 18 | Time: 10 ... 1666666 minutes | AES-256, 192, 128: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |
| IKEv2 | Main | Group 1  Group 2  Group 5  Group 14 - Group 18 | Time: 10 ... 1666666 minutes | AES-256, 192, 128*: Advanced Encryption Standard (CBC, CTR, CCM 16 or GCM 16 mode)  3DES-168**: Triple DES***  DES | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |  |
| Security device configured as  NCP VPN client | IKEv1 | Main  Aggressive | Group 1  Group 2  Group 5  Group 14  Group 15 | Time: 10 … 2500000 minutes | AES-256, 192, 128*: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |
| SCALANCE SC-600  SCALANCE S615 | IKEv1 | Main  Aggressive | Group 1  Group 2  Group 5  Group 14 - Group 18 | Time: 10 … 2500000 minutes | AES-256, 192, 128*: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES*** | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |
| IKEv2 | Main | Group 1  Group 2  Group 5  Group 14 - Group 18 | Time: 10 … 2500000 minutes | AES-256, 192, 128*: Advanced Encryption Standard (CBC, CTR, CCM 16 or GCM 16 mode)  3DES-168**: Triple DES***  DES | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 |  |
| * 256 bit, 192 bit or 128 bit key length  ** 168 bit key length  *** The setting is classified as less secure. It is recommended when possible that you use a more secure setting. |  |  |  |  |  |  |

###### VPN group properties for phase 2

Phase 2: IKE negotiation of the Security Association (SA) for IPsec data exchange:

Here, you set the parameters for negotiating the security parameters used for the IPsec data exchange with ESP (Encapsulating Security Payload) and AH (Authentication Header). Communication in phase 2 is already encrypted.

The following VPN group properties are supported by the individual modules:

| Module | IKE version | Phase 2 |  |  |  |
| --- | --- | --- | --- | --- | --- |
| SA lifetime | Encryption | Authentication | Perfect Forward Secrecy |  |  |
| CP 1543-1 (as of V2.1)  CP 1543SP-1 (V2.0)  CP 1243-1 BX30 (as of V3.0)  CP 1243-7 LTE BX30 (as of V3.0)  CP 1243-8 IRC BX30 (as of V3.0) | IKEv1 | Time: 60 … 16666666 minutes  Limit: 2000 ... 500000 MB | AES-128: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| CP 1543-1 (up to 2.0)  CP 1543SP-1 (V1.0)  CP 1243-1 BX30 (up to V2.1)  CP 1243-7 LTE BX30 (V2.1)  CP 1243-8 IRC BX30 (V2.1) | IKEv1 | Time: 60 … 16666666 minutes  Limit: 2000 ... 500000 MB | AES-128: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| CP 343-1 GX31 Advanced  CP 443-1 GX30 Advanced  CP 443-1 OPC UA  CP 1628  SCALANCE S-600 as of V3 | IKEv1 | Time: 60 … 16666666 minutes  Limit: 2000 ... 500000 MB | AES-128*: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| SOFTNET Security Client V4, V5 (WinXP) | IKEv1 | Time: 60 … 2879 minutes | 3DES-168**: Triple DES***  DES | SHA-1***: Secure Hash Algorithm 1 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| Security device configured as  SOFTNET Security Client V5 (Win7) | IKEv1 | Time: 60 … 2879 minutes | AES-128*: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| MD741-1 V1.1, M875 V2.0 | IKEv1 | Time: 60 … 16666666 minutes | 3DES-168**: Triple DES*** | SHA-1***: Secure Hash Algorithm 1 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| Security device configured as VPN client  VPN server | IKEv1 | Time: 10 ... 16666666 minutes  Limit: 10 ... 4096 MB | AES-256, 192, 128*: Advanced Encryption Standard (CBC, CTR, CCM 16 or GCM 16 mode)  3DES-168**: Triple DES***  DES | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| IKEv2 | Time: 10 ... 16666666 minutes  Limit: 10 ... 4096 MB | AES-256, 192, 128*: Advanced Encryption Standard (CBC, CTR, CCM 16 or GCM 16 mode)  3DES-168**: Triple DES*** | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1  MD5***: Message Digest Algorithm 5 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |  |
| Security device configured as  NCP VPN client | IKEv1 | Time: 10 ... 16666666 minutes  Limit: 10 ... 4096 MB | AES-128: Advanced Encryption Standard (CBC mode)  3DES-168**: Triple DES***  DES | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  MD5***: Message Digest Algorithm 5 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| SCALANCE SC-600  SCALANCE S615 | IKEv1 | Time: 10 ... 16666666 minutes  Limit: 10 ... 4096 MB | AES-256, 192, 128*: Advanced Encryption Standard (CBC, CTR, CCM 16 or GCM 16 mode)  3DES-168**: Triple DES*** | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |
| IKEv2 | Time: 10 ... 16666666 minutes  Limit: 10 ... 4096 MB | AES-256, 192, 128*: Advanced Encryption Standard (CBC, CTR, CCM 16 or GCM 16 mode)  3DES-168**: Triple DES*** | SHA-512: Secure Hash Algorithm 512  SHA-384: Secure Hash Algorithm 384  SHA-256: Secure Hash Algorithm 256  SHA-1***: Secure Hash Algorithm 1 | ON: Diffie Hellman public key values are exchanged for recalculation of the keys.  OFF***: The values already exchanged in phase 1 are used for recalculation of the keys. |  |
| * 256 bit, 192 bit or 128 bit key length  ** 168 bit key length  *** The setting is classified as less secure. It is recommended when possible that you use a more secure setting. |  |  |  |  |  |

###### Configuring fallback VPN profiles

In addition to the properties of a VPN group, fallback VPN profiles can be assigned to a VPN group. VPN profiles contain predefined properties for the authentication method, IKE phase 1 and 2. Fallback VPN profiles can be used as alternative configurations for VPN connection establishment. These come into play when VPN properties of the initiator do not match the VPN properties of the responder. In such cases, fallback VPN profiles ensure the VPN connection establishment. The configured fallback VPN profiles just as the properties of the VPN group are transferred to all VPN group members. The priority for the use of the fallback VPN profiles is specified by their order in the configuration. The fallback VPN profiles and the properties of the VPN group must not differ in the authentication method.

The following fallback VPN profiles are available:

VPN profile 1

| Parameter | Setting |
| --- | --- |
| Authentication method | Certificate |
| IKE mode | Main |
| Phase 1 DH group | Group 14 |
| Phase 1 encryption | AES-256 |
| Phase 1 SA lifetime | SA lifetime proposed by the initiator: 480 minutes  Range permitted by the responder for the SA lifetime: 480 … 2880 minutes |
| Phase 1 authentication | SHA-1 |
| Phase 2 SA lifetime type | Time |
| Phase 2 encryption | AES-128 |
| Phase 2 SA lifetime | SA lifetime proposed by the initiator: 240 minutes  Range permitted by the responder for the SA lifetime: 60 … 2880 minutes |
| Phase 2 authentication | SHA-1 |
| Perfect Forward Secrecy | OFF |

VPN profile 2

| Parameter | Setting |
| --- | --- |
| Authentication method | Certificate |
| IKE mode | Main |
| Phase 1 DH group | Group 2 |
| Phase 1 encryption | AES-256 |
| Phase 1 SA lifetime | SA lifetime proposed by the initiator: 480 minutes  Range permitted by the responder for the SA lifetime: 480 … 2880 minutes |
| Phase 1 authentication | SHA-1 |
| Phase 2 SA lifetime type | Time |
| Phase 2 encryption | 3DES-168 |
| Phase 2 SA lifetime | SA lifetime proposed by the initiator: 2880 minutes  Range permitted by the responder for the SA lifetime: 60 … 2880 minutes |
| Phase 2 authentication | SHA-1 |
| Perfect Forward Secrecy | OFF |

VPN profile 3

| Parameter | Setting |
| --- | --- |
| Authentication method | Certificate |
| IKE mode | Main |
| Phase 1 DH group | Group 2 |
| Phase 1 encryption | 3DES-168 |
| Phase 1 SA lifetime | SA lifetime proposed by the initiator: 480 minutes  Range permitted by the responder for the SA lifetime: 480 … 2880 minutes |
| Phase 1 authentication | SHA-1 |
| Phase 2 SA lifetime type | Time |
| Phase 2 encryption | 3DES-168 |
| Phase 2 SA lifetime | SA lifetime proposed by the initiator: 2880 minutes  Range permitted by the responder for the SA lifetime: 60 … 2880 minutes |
| Phase 2 authentication | SHA-1 |
| Perfect Forward Secrecy | OFF |

VPN profile 4

| Parameter | Setting |
| --- | --- |
| Authentication method | Certificate |
| IKE mode | Main |
| Phase 1 DH group | Group 2 |
| Phase 1 encryption | DES |
| Phase 1 SA lifetime | SA lifetime proposed by the initiator: 480 minutes  Range permitted by the responder for the SA lifetime: 480 … 2880 minutes |
| Phase 1 authentication | MD5 |
| Phase 2 SA lifetime type | Time |
| Phase 2 encryption | 3DES-168 |
| Phase 2 SA lifetime | SA lifetime proposed by the initiator: 2880 minutes  Range permitted by the responder for the SA lifetime: 60 … 2880 minutes |
| Phase 2 authentication | SHA-1 |
| Perfect Forward Secrecy | OFF |

VPN profile 5

| Parameter | Setting |
| --- | --- |
| Authentication method | Pre-shared key |
| IKE mode | Main |
| Phase 1 DH group | Group 2 |
| Phase 1 encryption | 3DES-168 |
| Phase 1 SA lifetime | SA lifetime proposed by the initiator: 480 minutes  Range permitted by the responder for the SA lifetime: 480 … 2880 minutes |
| Phase 1 authentication | SHA-1 |
| Phase 2 SA lifetime type | Time |
| Phase 2 encryption | 3DES-168 |
| Phase 2 SA lifetime | SA lifetime proposed by the initiator: 2880 minutes  Range permitted by the responder for the SA lifetime: 60 … 2880 minutes |
| Phase 2 authentication | SHA-1 |
| Perfect Forward Secrecy | OFF |

After opening a STEP 7 project, that was last stored with an older version than V14 SP1, all existing VPN groups with the authentication method "Certificate" are assigned the predefined fallback VPN profile 2 - 5 as default.

###### Special features for the SOFTNET Security Client and SCALANCE M

Configured fallback VPN profiles are not included in the configuration files for the Road Warrior modules SOFTNET Security Client and SCALANCE M For the SOFTNET Security Client and SCALANCE M modules the following applies:

- Select the VPN profile to be used for VPN connections of SOFTNET Security Client / SCALANCE M modules to SCALANCE S / CPs in the responder settings, see section [Configuring module- and connection-specific VPN settings](#configuring-module--and-connection-specific-vpn-settings).
- For VPN connections from SCALANCE M modules to SCALANCE M modules, the configured VPN group settings are used.
- For VPN connections from SOFTNET Security Client to SCALANCE M modules the settings of VPN profile 3 are always used.

#### Modes of VPN groups

##### VPN modes

Depending on the mode of the security modules that were added to a VPN group, different modes of VPN groups are distinguished. The mode of a VPN group provides information about the security modules and their modes that can be added to the VPN group.

##### Rules for forming groups

Remember the following rules if you want to create VPN groups:

- For SCALANCE S612 / S613 / S623 / S627-2M / SCALANCE M / VPN device

  The first module assigned in a VPN group decides which other modules can be added to it.

  If the first SCALANCE S module to be added is in routing mode or if the first module is a SCALANCE M module or a VPN device, only additional SCALANCE S modules with routing activated or SCALANCE M modules cor VPN devices an be added because SCALANCE M modules and VPN devices always operate in routing mode. If the first SCALANCE S module added is in bridge mode, you can only add other SCALANCE S modules in bridge mode. If you want to change the mode of a VPN group, you have to remove all the modules contained in the group and add them again. A CP and an SSC can be added to a group with a SCALANCE S in bridge or routing mode.
- For CP / SSC

  If a CP / SSC is the first module in a VPN group, security modules can be added in any mode. The next module that decides the mode then also decides the mode of the VPN group. A CP / SSC can be assigned to several VPN groups at the same time and use different modes. The CP / SSC is then operated in mixed mode.
- It is not possible to add a SCALANCE M module to a VPN group that contains a module in bridge mode.

Refer to the following table to see which modules can grouped together in a VPN group:

Security modules and VPN modes

| Module | Can be included in a VPN group in... |  |
| --- | --- | --- |
| Bridge mode | Routing mode |  |
| SCALANCE S612 / S613 / S623 / S627-2M in bridge mode | **x** | **-*** |
| SCALANCE S612 / S613 / S623 / S627-2M in routing mode | **-** | **x** |
| CP 343-1 Adv. / CP 443-1 Adv. | **x** | **x** |
| S7-1200/S7-1500 CPs | **x** | **x** |
| CP 1628 | **x** | **x** |
| SOFTNET Security Client V4.0 | **x** | **x** |
| SCALANCE M875 / VPN device | **-** | **x** |
| * SCALANCE S623/S627-2M modules in bridge mode can be inserted in a VPN group in routing mode if their DMZ interface is activated (not at the same time). |  |  |

#### Including security module in configured VPN group

The configured VPN group properties are adopted for security modules added to in an existing VPN group.

##### Procedure after including a security module in a configured VPN group

Depending on whether or not you have changed the VPN group properties since the last download, you must make a distinction between the following:

- **Case a:** If you have not changed the VPN group properties and the module to be added actively establishes the connection to modules of the type SCALANCE S, CP 343-1 Adv. / CP 443-1 Adv. or CP 1628:

1. Add the new security module to the VPN group.
2. Download the configuration to the new module.

- **Case b:** If you have changed the VPN group properties or the module being added does not actively establish the connection to the already configured modules:

1. Add the new security module to the VPN group.
2. Download the configuration to all modules that belong to the VPN group.

In case a, it is not necessary to reconfigure and load the already commissioned security modules. Active communication is not influenced or interrupted.

##### Procedure after removing an active member from a VPN group

If you remove an active node from an existing VPN group, this can still establish a connection to the group members even if you have downloaded the project to all members of the VPN group again.

If you do not want the removed active node to be able to establish the connection any longer, renew the CA group certificate and download the project again to the members of the VPN group. The certificate can be renewed in the group properties of the VPN group or in the "CA" tab of Certificate Manager.

#### Configuring network nodes reachable through a tunnel

This section contains information on the following topics:

- [Overview](#overview)
- [Automatic learning of internal network nodes](#automatic-learning-of-internal-network-nodes)
- [Configuring IP network nodes manually for SCALANCE S](#configuring-ip-network-nodes-manually-for-scalance-s)
- [Configuring MAC network nodes manually for SCALANCE S](#configuring-mac-network-nodes-manually-for-scalance-s)
- [Configuring internal subnets for SCALANCE S manually](#configuring-internal-subnets-for-scalance-s-manually)
- [Allow access to S7-300 / S7-400 CPs for VPN connection partners](#allow-access-to-s7-300-s7-400-cps-for-vpn-connection-partners)
- [Configuring NDIS nodes for PC CPs that can be reached through the tunnel](#configuring-ndis-nodes-for-pc-cps-that-can-be-reached-through-the-tunnel)
- [Configuring subnets reachable via the backplane bus for CP 1543-1](#configuring-subnets-reachable-via-the-backplane-bus-for-cp-1543-1)

##### Overview

###### Configuring network nodes reachable through a tunnel

Each security module must know the network nodes reachable via a VPN tunnel to be able to recognize the authenticity of a frame.

The security module must know both its own nodes as well as the nodes of the security modules in the same VPN group. This information is used on a security module to decide which data packet will be transferred in which tunnel.

By adding a security module to a VPN group, the local internal nodes/subnets of the security module are automatically made known to the security module. To allow communication via the VPN tunnel with other subnets or nodes of another subnet (routed internal network; DMZ network when the VPN tunnel is on the external interface and vice versa), these subnets or nodes must be enabled for VPN tunnel communication in the configuration.

SCALANCE S modules allow network nodes to be learned automatically or configured statically. The mode of the security module also decides the options available for learning internal network nodes.

###### SCALANCE S in bridge mode

In bridge mode, you can configure the IP/MAC nodes and the subnets or alternatively can allow automatic learning of nodes by the SCALANCE S.

###### SCALANCE S in routing mode

In routing mode there is no automatic learning mode available. Instead, enter entire subnets here that need to be released for tunnel communication.

###### CP 343-1 Advanced / CP 443-1 Advanced and CP 1628

- CP 343-1 Advanced / CP 443-1 Advanced

  Decide whether or not tunnel communication to the CP (Gbit interface) and/or to the internal subnet (PROFINET subnet) is permitted for VPN connection partners in routing mode (SCALANCE S / M).
- CP 1628

  Enter the NDIS nodes you want to be reachable through the tunnel of VPN connection partners in routing mode (SCALANCE S / M).

###### CP 1543-1 as of V2.1 with activated IP routing between communications modules

Enter the subnets or IP addresses reachable via the backplane bus of the station and that need to be released for tunnel communication.

##### Automatic learning of internal network nodes

###### Module-specific function

SCALANCE S modules in bridge mode provide a learning mode with which the internal network nodes can be learned automatically during operation. For more detailed information, refer to the section:  
[Using the learning mode to learn internal nodes](#using-the-learning-mode-to-learn-internal-nodes)

##### Configuring IP network nodes manually for SCALANCE S

###### Module-specific function

How to configure IP network nodes for SCALANCE S modules manually is explained in:  
[Configuring IP network nodes manually](#configuring-ip-network-nodes-manually).

##### Configuring MAC network nodes manually for SCALANCE S

###### Module-specific function

How to configure MAC nodes for SCALANCE S modules manually is explained in:  
[Configuring MAC network nodes manually](#configuring-mac-network-nodes-manually).

##### Configuring internal subnets for SCALANCE S manually

###### Module-specific function

How to configure the internal subnets for SCALANCE S modules is explained in  
[Configuring internal subnets manually](#configuring-internal-subnets-manually).

##### Allow access to S7-300 / S7-400 CPs for VPN connection partners

###### Module-specific function

How to allow access to S7-300 / S7-400 CPs for VPN connection partners is explained in   
[Allow access to S7-300 / S7-400 CPs for VPN connection partners](#allow-access-to-s7-300-s7-400-cps-for-vpn-connection-partners-1) in the section "Security for S7-300 /S7-400 /PC CPs".

##### Configuring NDIS nodes for PC CPs that can be reached through the tunnel

###### Module-specific function

How you configure NDIS nodes for PC CPs that can be reached through the tunnel is explained in   
[Configuring NDIS nodes manually for PC CPs that can be reached through the tunnel](#configuring-ndis-nodes-manually-for-pc-cps-that-can-be-reached-through-the-tunnel) in the section "Security for S7-300 / S7-400 / PC CPs".

##### Configuring subnets reachable via the backplane bus for CP 1543-1

###### Module-specific function

For information on how to configure subnets and network nodes reachable via the backplane bus of the station for CP 1543-1 as of V2.1, see section   
[Configuring S7 subnets reachable via the backplane bus for CP 154x-1](#configuring-s7-subnets-reachable-via-the-backplane-bus-for-cp-154x-1).

#### Configuring module- and connection-specific VPN settings

##### Requirement

The module is a member of a VPN group.

##### Module- and connection-specific settings

With module- and connection-specific settings, you can configure specific VPN settings. Module-specific settings are configured specifically for a security module while connection-specific settings are configured specifically for a security module in a certain VPN group.

You can configure the following **module-specific** properties in the local security settings with the "VPN" entry:

- Dead peer detection
- Permission to initiate connection establishment
- Public address (IP address / FQDN) for communication via Internet gateways
- Responder settings for Road Warrior connections
- Nodes that need to be enabled for tunnel communication

If you select a security module in the list of VPN groups in the "Network data" area, the following **connection-specific** VPN settings can be seen and can be configured:

- Permission to initiate connection establishment
- Partner modules to which tunnel connections exist
- Type of transferred packets
- Selection of the local interface of the selected security module that will serve as the tunnel endpoint
- Selection of the partner interface that will serve as the tunnel endpoint

![Module- and connection-specific settings](images/77195073163_DV_resource.Stream@PNG-en-US.png)

##### Dead peer detection (DPD)

As default, DPD is enabled.

When DPD is enabled, the modules exchange additional messages at selectable intervals if no communication occurs at these points in time. This means that it is possible to recognize whether the IPsec connection is still valid or possibly needs to be re-established. If there is no longer a connection, the security associations (SA) of phase 2 are terminated prematurely. If DPD is disabled, the SA is ended only after the SA lifetime has expired. For information on setting the SA lifetime, see section   
[Configuring VPN group properties](#configuring-vpn-group-properties).

##### Permission to initiate connection establishment

You can restrict the permission for initiating the VPN connection establishment to certain modules in the VPN.

The decisive factor for the setting of the parameter described is the assignment of the address for the gateway of the module you are configuring. If a static IP address is assigned, the module can be found by the partner. If the IP address is assigned dynamically and therefore changes constantly, the partner cannot establish a connection as things stand.

| Mode | Meaning |
| --- | --- |
| Start connection to partner (initiator/responder) (default) | If this option is selected, the module is "active", in other words, it attempts to establish a connection to the partner with a fixed IP address. The reception of requests for VPN connection establishment is also possible.  This option is recommended when you obtain a dynamic IP address from the provider for the gateway of the security module you are configuring.  The partner is addressed using its configured WAN IP address, its configured external module IP address or the configured DNS name. |
| Wait for partner (responder) | If this option is selected, the module is "passive", in other words, it waits for the partner to initiate the connection.  This option is recommended when you have been assigned a static IP address by the provider for the gateway of the security module you are configuring. It means attempts to establish a connection can only be initiated by the partner. This partner can, for example, have a dynamic WAN IP address. |

> **Note**
>
> Make sure that you do not set all the modules in a VPN group to "Wait for connection from remote VPN gateway" otherwise no connection is established.

##### WAN IP address / FQDN - addresses of the modules and gateways in a VPN over Internet

When operating a VPN with IPsec tunnel over the Internet, additional IP addresses are generally required for the Internet gateways such as DSL routers. The individual security or SCALANCE M modules must know the external IP addresses of the partner modules in the VPN.

> **Note**
>
> To use a WAN as an external public network, enter the IP address that you received from the provider as the external IP address, through which the security module is then reachable in the WAN (Internet). To allow the security module to send packets via the WAN, you need to enter your DSL router as "Standard router".
>
> If you use a DSL router as Internet gateway, the following ports (at least) must be opened on it as described in the relevant documentation:
>
> - Port 500 (ISAKMP)
> - Port 4500 (NAT-T)

To allow this, in the module-specific VPN settings, you have the option of assigning an IP address as a "WAN IP address". When you download the module configuration, the group members are then informed of the WAN IP addresses of the partner modules. As an alternative to a WAN IP address, you can also enter an FQDN. Depending on the existing addresses, VPN endpoints are used as default according to the following priorities:

1. WAN address
2. FQDN of the primary dynamic DNS service
3. FQDN of the secondary dynamic DNS service
4. External IP address / DMZ IP address of the security module

Note: After removing an existing WAN address, the external IP address / DMZ IP address is always used.

In the interface selection of the connection-specific VPN settings, you yourself can decide which address the partner will be informed of. In these settings, you can also specify the interface to be used for communication by the nodes of a VPN group and the security module that is authorized to set up connections.

![WAN IP address / FQDN - addresses of the modules and gateways in a VPN over Internet](images/41738185355_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Internal IP address - of a module |
| ② | External IP address - of a module |
| ③ | IP address of an Internet gateway (for example, GPRS gateway) |
| ④ | IP address (WAN IP address) of an Internet gateway (for example, DSL router) |

##### Responder settings for Road Warrior connections

The VPN connection establishment by Unknown Peers (Road Warriors) is allowed by the responder as default with the secure VPN properties of VPN profile 1. You can allow or block the VPN connection establishment by Unknown Peers and the properties used by selecting a VPN group profile and by selecting VPN profiles.

| Operator control element | Meaning |
| --- | --- |
| Allow VPN connection establishment by Road Warriors | The responder allows VPN connection establishment by Unknown Peers. |
| VPN profile 1 - 5 in the selection dialog for VPN profiles | The responder allows VPN connection establishment by unknown peers with the properties of the predefined VPN profiles 1 - 5. The properties of these VPN profiles correspond to the properties of the fallback VPN profiles that you can select for VPN groups, see section [Configuring VPN group properties](#configuring-vpn-group-properties). |
| VPN group profiles in the selection dialog for VPN profiles | The responder allows VPN connection establishment by Unknown Peers with the properties of the VPN group selected in the selection dialog for VPN profiles with a check mark. The VPN groups can be selected in which the responder is located. A maximum of one VPN group can be selected and used as a VPN group profile. With the "Add" button, new VPN groups can be created to which the responder is automatically assigned. These VPN groups can then be selected for the formation of a VPN group profile. If VPN connection establishment by Unknown Peers with the properties of the VPN group in which the responder and the Unknown Peers are located is to be allowed, this VPN group must be selected in the selection dialog. |

After opening a STEP 7 project last saved with a version older than V14 SP1, the check box "Allow VPN connection establishment by Road Warriors" is activated s default. In addition to this, the responder is assigned the predefined VPN profiles 2 - 5.

For VPN connections from SOFTNET Security Client / SCALANCE M-800 modules to SCALANCE S / CPs the selected VPN profile with the highest priority is always used and read out. The authentication method of the selected VPN profile must match the authentication method of the corresponding VPN group. The priority of the VPN profiles is as follows:

1 Selected VPN group profile  
2. VPN profile 1  
3. VPN profile 2  
4. VPN profile 3  
5. VPN profile 4  
6. VPN profile 5

For VPN connections from SCALANCE M875 modules to SCALANCE S / CPs, VPN profile 3 must be selected if the authentication method of the corresponding VPN group is "Certificate". If the authentication method of the corresponding VPN group is "Preshared key", VPN profile 5 must be selected.

##### Configuring internal network nodes

The configuration of internal network nodes is described in the following section:  
[Configuring network nodes reachable through a tunnel](#configuring-network-nodes-reachable-through-a-tunnel)

---

**See also**

[How to create an IPsec tunnel with VPN groups](#how-to-create-an-ipsec-tunnel-with-vpn-groups)

### Establishing an OpenVPN tunnel to the SINEMA Remote Connect server

#### Module-specific function

This function is only available for the following modules:

- CP 1243-1 as of V3.1
- CP 1243-8 IRC as of V3.1
- CP 1243-7 LTE as of V3.1
- CP 1542SP-1 IRC as of V2
- CP 1543SP-1 as of V2

You will find detailed information in the section [Automatic OpenVPN configuration and OpenNPN tunnel establishment](#automatic-openvpn-configuration-and-opennpn-tunnel-establishment) of the chapter "Security for S7-1200-/S7-1500-CPs".

### Configuring router and firewall redundancy

#### Module-specific function

This function is available only for SCALANCE S623/S627-2M as of V4, see section   
[Router and firewall redundancy](#router-and-firewall-redundancy).

### Online functions - diagnostics and logging

This section contains information on the following topics:

- [Overview of diagnostics and logging in](#overview-of-diagnostics-and-logging-in)
- [Function overview online dialog](#function-overview-online-dialog)
- [Functions of the online diagnostics](#functions-of-the-online-diagnostics)
- [Logging functions](#logging-functions)

#### Overview of diagnostics and logging in

For test and monitoring purposes, the security module has diagnostic and logging functions.

- Diagnostic functions

  These include various system and status functions that you can use for an existing network connection to the security module.
- Logging functions

  This involves the logging of system and security events and data packets.

##### Recording events with logging functions

You select the events to be logged in the log settings for the relevant security module.

You can configure the following variants for logging:

- Local logging

  In this variant, you log events in the local buffer of the security module. You can then access these logs, display them and archive them on the service station in the "Online & diagnostics" dialog. The evaluation of the buffer areas of the security module is only possible if there is a network connection to the selected security module.
- Network Syslog

  With Network Syslog, you use a Syslog server that exists in the network. This logs the events according to the configuration in the log settings for the relevant security module.

##### Archiving log data and reading in from a file

You can save the logged events for archiving in a log file and open this later even without a network connection to the security module. You will find the function for opening the log files in the global security functions.

##### Diagnostics in ghost mode (only for SCALANCE S S602 as of V3.1)

When you operate the security module in ghost mode, the external interface of the security module takes over the IP address of the internal node at runtime. Before you can run diagnostics of a security module in ghost mode, you need to establish the connection to the security module via the IP address that the security module obtained from the internal node at runtime.

To find out which IP address the security module currently has, you can search for accessible nodes in STEP 7 using the "Online" > "Accessible devices".

##### Protecting exported log files from unauthorized access

Log files exported from STEP 7 can contain security related information. You should therefore make sure that these files are protected from unauthorized access. This is particularly important when passing on the files.

#### Function overview online dialog

##### Functions of the "Online & diagnostics" dialog

In STEP 7, the security module provides the following functions in the "Online & diagnostics" dialog:

| Entry in the online dialog | Function |
| --- | --- |
| Status | Display of status information about the selected security module, such as the current IP addresses of the interfaces and the current time and date. |
| Interface settings | Overview of the settings of the individual interfaces. |
| Dynamic DNS | Overview of the settings for dynamic DNS. |
| System log | Shows logged system events, starting and stopping logging (only if there is an online connection to SCALANCE S modules) and starting and stopping the reading out of log data from the local buffer of the security module. |
| Audit log | Shows logged security events, starting and stopping reading out of log data from the local buffer of the security module. |
| Packet filter log | Shows logged data packets, starting and stopping logging (only if there is an online connection to SCALANCE S modules) and starting and stopping the reading out of log data from the local buffer of the security module. |
| ARP Table | Display of the ARP table of the security module. |
| Logged-on users | Shows the users logged in to the Internet page for user-specific IP rule sets. |
| Communications status | Display of status information about VPN tunnel connections and members of VPN groups to which the selected security module belongs. |
| SINEMA RC - automatic VPN configuration | Display of the status of the OpenVPN configuration and of OpenVPN connections to the SINEMA RC Server. |
| Internal nodes | Display of the learned or configured internal network nodes of the security module. |
| Dynamically updated firewall rules | Display of the IP addresses that were released dynamically over HTTP or HTTPS, or loaded by a user. |
| Firewall blacklist | Display of the IP addresses that were entered in the blacklist of the firewall. |
| Ghost mode | Dialog for the ghost mode of the SCALANCE S602 with information on the address parameters of the internal node (identical to the external IP address of the security module) and on IP address changes of the internal node. |
| Date and time of day | Date and time setting. |
| Firmware update | Updating the firmware. |

##### Requirements for access

The following requirements must be met to use the online functions of a security module:

- There is a network connection to the selected module.
- The project with which the module was configured is open.
- A user with the required rights must be logged in to the project.
- For CPs, the diagnostics access must be enabled in the firewall (CP 343-1 Adv. / 443-1 Adv. and CP 1628: TCP 443; S7-1200/S7-1500 CPs: TCP 8448).

> **Note**
>
> **Requirement for online diagnostics in ghost mode (only for SCALANCE S S602 as of V3.1)**
>
> Online diagnostics is only available in ghost mode if the security module has learned the IP address of the internal node and has adopted this for its external interface. After this, the security module can be reached via the IP address of the external interface.

##### How to access this function

1. Right-click on the module to process.
2. Select the "Online & diagnostics" command from the shortcut menu.
3. If there is no online connection established to the security module, click the "Connect online" button in the "Diagnostics" entry.

##### Online settings are not saved in the configuration

Settings that you make in online mode (for example settings for the logging memory) are not stored in the configuration on the security module. This is why the configuration settings are always applied at the restart of the module.

#### Functions of the online diagnostics

This section contains information on the following topics:

- [Status information of the security module - "Status" entry](#status-information-of-the-security-module---status-entry)
- [Overview of the individual interfaces - "Interface settings" entry](#overview-of-the-individual-interfaces---interface-settings-entry)
- [Overview of the Dyn. DNS settings - "Dynamic DNS" entry](#overview-of-the-dyn-dns-settings---dynamic-dns-entry)
- [Display of the ARP table - "ARP table" entry](#display-of-the-arp-table---arp-table-entry)
- [Users logged in to the Web page - "Logged in users" entry](#users-logged-in-to-the-web-page---logged-in-users-entry)
- [VPN connections of the security module - "Communication status" entry](#vpn-connections-of-the-security-module---communication-status-entry)
- [Automatic OpenVPN configuration via SINEMA RC Server](#automatic-openvpn-configuration-via-sinema-rc-server)
- [Found internal network nodes - "Internal nodes" entry](#found-internal-network-nodes---internal-nodes-entry)
- [Updated firewall rules - "Dynamically updated firewall rules" entry](#updated-firewall-rules---dynamically-updated-firewall-rules-entry)
- [Display of the firewall blacklist - "Firewall blacklist" entry](#display-of-the-firewall-blacklist---firewall-blacklist-entry)
- [Setting the date and time - "Date and Time" entry](#setting-the-date-and-time---date-and-time-entry)
- [Diagnostics in ghost mode - "Ghost mode" entry](#diagnostics-in-ghost-mode---ghost-mode-entry)

##### Status information of the security module - "Status" entry

###### Meaning

Display of the status of the security module selected in the project.

Online & diagnostics: - "Status" entry

| System and status functions |  | Meaning |
| --- | --- | --- |
| **Overview** |  |  |
| Hardware type |  | The type of the security module. |
| External IP address |  | The external IP address of the security module.  For S7-1200/S7-1500 CPs, CP 1628: The IP address of the Industrial Ethernet interface.  For CP 343-1 Adv. / 443-1 Adv.: The IP address of the Gbit interface. |
| Internal IP address |  | The internal IP address of the security module.  For CP 1628: The IP address of the NDIS interface. If there is more than one NDIS address, only one is displayed.  For CP 343-1 Adv. / 443-1 Adv.: The IP address of the PROFINET interface. |
| DMZ IP address (SCALANCE S623 / S627-2M only) |  | The DMZ IP address of the security module. |
| Tunnel IP address (only SCALANCE S612/S623/S627-2M as of V4) |  | The first alias internal IP address of the security module in the VPN tunnel. |
| Serial number |  | The serial number of the security module. |
| Article number |  | The article number of the security module that is used when ordering. |
| Firmware version |  | The firmware version of the security module. |
| Operating mode |  | Mode of the security module (bridge mode / routing mode) |
| External MAC address |  | The external MAC address of the security module.  For S7-1200/S7-1500 CPs, CP 1628: The MAC address of the Industrial Ethernet interface.  For CP 343-1 Adv. / 443-1 Adv.: The MAC address of the gigabit interface. |
| Internal MAC address |  | The internal MAC address of the security module.  For CP 1628: The MAC address of the NDIS interface.  For CP 343-1 Adv. / 443-1 Adv.: The MAC address of the PROFINET interface. |
| DMZ MAC address (SCALANCE S623 / S627-2M only) |  | The DMZ MAC address of the security module |
| Hardware release |  | The hardware product version of the security module. |
| C-PLUG |  | Shows whether or not a C-PLUG is inserted. |
| **Alias IP addresses** (only for SCALANCE S as of V4) |  |  |
| IP address |  | Alias IP address that was registered on an interface of the security module by a NAT rule. |
| Corresponding Interface |  | Interface of the security module on which the alias IP address was registered. |
| **Local time** |  |  |
| Current time | Date and time that is displayed on the security module.  Format for "German" user interface language: dd.mm.yyyy (date) hh:mm:ss (time)  Format for "English" user interface language: mm/dd/yyyy (date) hh:mm:ss AM/PM (time)  Format for "French", "Italian" and "Spanish" user interface language: dd/mm/yyyy (date) hh:mm:ss (time)  Format for "Chinese" user interface language: yyyy/mm/dd (date) hh:mm:ss   **Note (not for CPs)**   You set the local time on the SCALANCE S module in "Functions" > "Date and time". |  |
| Operating time | Time since the last restart of the security module.  Format with the user interface language "German", "English", "French", "Italian", "Spanish" and "Chinese": dddd.hh:mm:ss |  |
| Time-of-day source | The source from which the date and time are obtained. |  |
| **Configuration** |  |  |
| Created |  | Date and time when the project was first created.   Format with the user interface language "German", "English", "French", "Italian", "Spanish" and "Chinese": dd.mm.yyyy (date) hh:mm:ss (time) |
| Name |  | File name of the project last loaded. |
| Author |  | Name of the user who created the project. Is adopted from the project properties. |
| Compiled |  | Date and time when the project was last compiled.   Format with the user interface language "German", "English", "French", "Italian", "Spanish" and "Chinese": dd.mm.yyyy (date) hh:mm:ss (time) |
| Storage location |  | Specifies the location (e.g. town) that was entered in the properties of an SCT project. |
| **File system (not for CPs)** |  |  |
| RAM |  | Indicates how much RAM and flash is occupied in the file system. |
| Flash |  |  |

##### Overview of the individual interfaces - "Interface settings" entry

###### Module-specific function

This function is available only for SCALANCE S V3 modules or higher, see section  
[Overview of the individual interfaces - "Interface settings" entry](#overview-of-the-individual-interfaces---interface-settings-entry-1)

##### Overview of the Dyn. DNS settings - "Dynamic DNS" entry

###### Module-specific function

This function is available only for SCALANCE S V3 modules or higher, see section  
[Overview of the Dyn. DNS settings - "Dynamic DNS" entry](#overview-of-the-dyn-dns-settings---dynamic-dns-entry-1)

##### Display of the ARP table - "ARP table" entry

###### Module-specific function

This function is available only for SCALANCE S V3 modules or higher, see section  
[Display of the ARP table - "ARP table" entry](#display-of-the-arp-table---arp-table-entry-1)

##### Users logged in to the Web page - "Logged in users" entry

###### Module-specific function

This function is available only for SCALANCE S V3 modules or higher, see section  
[Users logged in to the Web page - "Logged in users" entry](#users-logged-in-to-the-web-page---logged-in-users-entry-1)

##### VPN connections of the security module - "Communication status" entry

###### Meaning

Display of the communication status of the following network components:

- Other security modules of the VPN group to which the selected security module belongs
- Internal network nodes of these security modules

Online & diagnostics: "Communication Status" entry

| System and status functions | Meaning |
| --- | --- |
| Known security devices or modules | Display of the nodes with which the selected security module is in a VPN group. This also shows whether the tunnel status is active or passive. To obtain additional information on one of the nodes, select this in the list.    **Note:**   Configured, inactive tunnels are indicated for CPs only. |
| Endpoints | Display of information on the internal network nodes of the security module that you selected in the "Known security devices or modules" table. For each internal network node, this shows whether it was learned or configured. It also shows the subnet in which the internal network node is located.  With SCALANCE S modules, the subnet of network nodes is only displayed in bridge mode. |
| Tunnel properties | Display of properties of the VPN tunnel established to the security module that you selected in the "Known security devices or modules" table. |

##### Automatic OpenVPN configuration via SINEMA RC Server

###### Module-specific function

This function is only available for the following modules:

- CP 1243-1 as of V3.1
- CP 1243-8 IRC as of V3.1
- CP 1243-7 LTE as of V3.1
- CP 1542SP-1 IRC as of V2
- CP 1543SP-1 as of V2

You will find detailed information in the section [Diagnostics of the automatic OpenVPN configuration and OpenNPN connections](#diagnostics-of-the-automatic-openvpn-configuration-and-opennpn-connections).

##### Found internal network nodes - "Internal nodes" entry

###### Meaning

Display of all learned and configured network nodes. This also displays whether or not the learning mode of the security module is enabled.

##### Updated firewall rules - "Dynamically updated firewall rules" entry

###### Module-specific function

This function is only available for CP 343-1 Adv. / 443-1 Adv., see section:  
[Updated firewall rules - "Dynamically updated firewall rules" entry](#updated-firewall-rules---dynamically-updated-firewall-rules-entry-1) in the section "Security for S7-300 / S7-400 / PC CPs".

##### Display of the firewall blacklist - "Firewall blacklist" entry

###### Module-specific function

This function is available only for SCALANCE S V4 modules or higher, see section   
[Display of the firewall blacklist - "Firewall blacklist" entry](#display-of-the-firewall-blacklist---firewall-blacklist-entry-1).

##### Setting the date and time - "Date and Time" entry

###### Module-specific function

This function is available only for SCALANCE S, see section   
[Setting the date and time - "Date and time" entry](#setting-the-date-and-time---date-and-time-entry-1).

##### Diagnostics in ghost mode - "Ghost mode" entry

###### Module-specific function

This function is available only for SCALANCE S602 as of V3.1, see section   
[Diagnostics in ghost mode - "Ghost mode" entry](#diagnostics-in-ghost-mode---ghost-mode-entry-1).

#### Logging functions

This section contains information on the following topics:

- [Logging system events - "System log" entry](#logging-system-events---system-log-entry)
- [Logging security events - "Audit log" entry](#logging-security-events---audit-log-entry)
- [Logging data packets - "Packet filter log" entry](#logging-data-packets---packet-filter-log-entry)

##### Logging system events - "System log" entry

###### Meaning

Shows logged system events and starting and stopping reading of system events from the local memory of the security module.

The system log automatically logs successive system events, for example the start of a process. The logging can be scaled based on event classes.

| System and status functions | Meaning |
| --- | --- |
| Start/stop logging (not for CPs) | Starts/stops recording of system events. The method and the event classes that are logged are configured in the local security settings. |
| Start/stop reading | Starts/stops reading of system events from the local memory of the security module. If you select the "Save log file" check box, the recorded log data is also saved as file. Select the storage location and enter a file name.   **Note**   If you select the "Save log file" check box after starting reading, the data read out up to then can no longer be saved in a log file. |
| Clear display | Deletes the log data shown in the table. |

You can open log files with saved system events in the global security functions in "Log files (offline view)".

##### Logging security events - "Audit log" entry

###### Meaning

Shows logged security events and starting and stopping reading of security events from the local memory of the security module.

The audit log automatically logs successive security-relevant events. This includes, for example, user actions such as enabling and disabling packet logging.

| System and status functions | Meaning |
| --- | --- |
| Start/stop reading | Starts/stops reading of security events from the local memory of the security module. If you select the "Save log file" check box, the recorded log data is also saved as file. Select the storage location and enter a file name.   **Note**   If you select the "Save log file" check box after starting reading, the data read out up to then can no longer be saved in a log file. |
| Clear display | Deletes the log data shown in the table. |

You can open log files with saved audit events in the global security functions in "Log files (offline view)".

##### Logging data packets - "Packet filter log" entry

###### Meaning

Shows logged data packets and starting and stopping reading of packet filter events.

The packet filter log records certain packets of the data traffic. Data packets are only logged if they match a configured packet filter rule (firewall) or if the basic protection reacts to them (corrupt or invalid packets). This is only possible when logging is enabled for the packet filter rule.

For information about activation of the logging, refer to section   
[Setting up a firewall](#setting-up-a-firewall).

As well as reading the log data from the buffer and transferring it to the display, it can also be saved in a file for archiving.

| System and status functions | Meaning |
| --- | --- |
| Start/stop logging (not for CPs) | Starts/stops logging of data packets. The method with which the data is logged is configured in the local security settings. |
| Start/stop reading | Starts/stops reading out of logged data packets from the local memory of the security module. If you select the "Save log file" check box, the recorded log data is also saved as file. Select the storage location and enter a file name.   **Note**   If you select the "Save log file" check box after starting reading, the data read out up to then can no longer be saved in a log file. |
| Clear display | Deletes the log data shown in the table. |
| Log category | Select the data packets for which the logging will be displayed. The selection depends on the settings you configured offline in the local security settings. Only the data packets for which logging was enabled are logged. If you select a category for which logging was not enabled, no data will be logged for this category. |

You can open log files with saved packet filter events in the global security functions in "Log files (offline view)".

### Download functions

#### Special features when downloading security configurations

Security configurations can influence the reachability of the security module for the configuration PC. This, for example, is the case if there is a tunnel connection configured for one security module to another security module in a configuration and this configuration is downloaded from the configuration PC to the security module. After the download by the configuration PC, the security module can no longer be reached and the reachability test performed as default by STEP 7 following the download of the configuration fails. The error message output by STEP 7 relates solely to the reachability test; the actual download of the configuration is ensured if the project data is consistent and the IP address relationship between the security module and the configuration PC is correct.

Special features when downloading configurations and firmware to SCALANCE S modules are described in the following section:  
[Download functions](#download-functions-1)

#### Uploading configurations to the engineering station

Uploading a configuration from a SCALANCE S module or from the CP 1628 to an engineering station is not possible.

Uploading a configuration from an S7 CP that supports security to an engineering station is also possible if security features were included in the configuration. Configured security functions are not, however, transferred to the engineering station. In the transferred configuration on the engineering station, the "Activate security features" check box is also deselected.

## SCALANCE S

This section contains information on the following topics:

- [Replacing a security module](#replacing-a-security-module-1)
- [Configuring interfaces for SCALANCE S modules](#configuring-interfaces-for-scalance-s-modules)
- [Authentication using a RADIUS server](#authentication-using-a-radius-server-1)
- [Setting up a firewall](#setting-up-a-firewall-1)
- [SCALANCE S module as router](#scalance-s-module-as-router)
- [Security module as DHCP server](#security-module-as-dhcp-server-1)
- [Configuring proxy ARP](#configuring-proxy-arp-1)
- [IPsec tunnel: Creating and assigning groups](#ipsec-tunnel-creating-and-assigning-groups)
- [Router and firewall redundancy](#router-and-firewall-redundancy)
- [Online functions - diagnostics and logging](#online-functions---diagnostics-and-logging-1)
- [Download functions](#download-functions-1)

### Replacing a security module

#### Requirement

To be able to replace security modules, their module descriptions must be up to date. To update the module description of security modules, follow the steps below:

1. Select the security module to be edited.
2. In the local security settings, click on the entry "General" > "Catalog information".
3. Click the "Update module description" button.

#### How to access this function

1. Select the security module to be edited in the topology or network view.
2. Right-click on the security module and select the shortcut menu command "Change device...".

   Based on the following table, you can see which security modules you can replace without data loss and which could involve a possible data loss.

| Initial module | Possible module replacement |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| S602 V4 | S612 V4 | S623 V4 | S623 V4.0.1 | S627-2M V4 | S627-2M V4.0.1 |  |
| S602 V4 | - | **!** | **!** | **!** | **!** | **!** |
| S612 V4 | **!** | - | **x** | **x** | **x** | **x** |
| S623 V4 | **!** | **!** | - | **x** | **x** | **x** |
| S623 V4.0.1 | **!** | **!** | **!** | - | **!** | **x** |
| S627-2M V4 | **!** | **!** | **!** | **!** | - | **x** |
| S627-2M V4.0.1 | **!** | **!** | **!** | **!** | **!** | - |
| **x** Without losses   **!** Possibly with losses  - The module type and the firmware version are not changed. |  |  |  |  |  |  |

### Configuring interfaces for SCALANCE S modules

This section contains information on the following topics:

- [Overview](#overview-1)
- [Setting the operating mode](#setting-the-operating-mode)
- [Configuring IP address parameters](#configuring-ip-address-parameters)
- [Configuring port mode](#configuring-port-mode)
- [Configuring an Internet connection](#configuring-an-internet-connection)
- [Configuring DNS](#configuring-dns)
- [Configuring dynamic DNS](#configuring-dynamic-dns)
- [Configuring LLDP](#configuring-lldp)
- [Media redundancy in ring topologies](#media-redundancy-in-ring-topologies)
- [Special features of the ghost mode](#special-features-of-the-ghost-mode)

#### Overview

##### Configuring the mode

With the mode you specify how interface routing is handled (external/internal). The DMZ interface of the security module (SCALANCE S623/S627-2M only) is always connected in routing mode. For more detailed information, refer to the section  
[Configuring IP address parameters](#configuring-ip-address-parameters)

##### Configuring the interfaces

If the external interface, the DMZ interface (SCALANCE S623/S627-2M only) or the tunnel interface (only SCALANCE S612/S623/S627-2M as of V4 in VPN group(s)) of a security module needs to be configured, it must be activated using the "Activate interface" check box. Set the IP address information for each interface and settings for the individual ports. The following options are available with which you can assign an IP address for the external interface and for the DMZ interface in the "General" entry (SCALANCE S623/S627-2M only):

- Static IP address with subnet mask. For more detailed information, refer to the section  
  [Configuring IP address parameters](#configuring-ip-address-parameters)
- Address assignment using PPPoE. For more detailed information, refer to the section  
  [Configuring an Internet connection](#configuring-an-internet-connection)

  The internal interface and the tunnel interface can only be configured using a static IP address.

If alias IP addresses were registered on the interfaces of the security module due to configuring NAT rules, these are displayed in the "Alias IP addresses" entry.

> **Note**
>
> **External interface and DMZ interface as Internet access**
>
> The simultaneous operation of PPPoE on the external interface and on the DMZ interface (dual ISP) is not possible.

##### Point to Point Protocol over Ethernet (PPPoE)

To allow Internet/WAN access directly via a DSL modem, the IP address on the external interface or on the DMZ interface is assigned using PPPoE. PPPoE is a dial-in protocol for obtaining IP addresses from an Internet service provider (ISP). SCALANCE S is operated here in routing mode.

To use this IP address assignment mode, specify the ISP in the "PPPoE" entry. The IP address, the subnet mask, the standard router and the DNS server of the interface are specified by the ISP.

> **Note**
>
> A configured standard router is not taken into account when using PPPoE. This is assigned dynamically to the module by the ISP.

> **Note**
>
> **No network components between SCALANCE S and DSL modem**
>
> If the interface of a SCALANCE S module is operated using PPPoE, there must be no other network components between this interface and the connected DSL modem, otherwise the dial-in data of the Internet Service Provider may be transferred unencrypted over this link. When using the "CHAP" authentication protocol, the data is transferred encrypted.

##### Configuring media modules

In addition to the functions of the SCALANCE S623, the S627-2M has two media module slots in which an electrical or optical media module with two ports can be inserted. This expands both the external and internal interface by up to two ports. In routing mode, the additional ports of the security module can be used to link the external and internal interface to ring topologies.

To integrate media modules in the SCALANCE S627-2M, select the security module and change to the device view. Then select the required media modules from the hardware catalog.

For ports with the port type "Copper", you can set the transmission speed and the duplex method manually using the port mode. For ports with the port type "Optical", the port mode is fixed by the media module used or by the SFP transceiver used and cannot be adapted.

You will find information on connecting the media module ports to MRP rings in the following section:  
[Media redundancy in ring topologies](#media-redundancy-in-ring-topologies)

#### Setting the operating mode

##### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "Mode".

##### Operating mode - possible selections

You can change the operating mode in this dialog if the security module is not included in a VPN group. If the security module is in a VPN group, the mode cannot be changed.

The selection applies to interface routing between the external and internal interface. The DMZ interface (SCALANCE S623 and S627-2M only) is always connected in routing mode.

| Symbol | Meaning |
| --- | --- |
| Bridge mode | For operation in flat networks. External and internal interface are in the same IP subnet.  For S623 / S627-2M: External and internal interface are in the same IP subnet, the DMZ interface is in a different IP subnet or is deactivated. |
| Routing mode | All interfaces are in different IP subnets. If you have activated the routing mode, you must configure an internal IP address and subnet mask for the internal interface of the security module.   **Note**   If you have enabled the routing mode for the SCALANCE S module, no MAC firewall rules can be defined. |
| Ghost mode (only for SCALANCE S S602 as of V3.1) | In operation, the security module adopts the IP address of the node connected to the internal interface of the security module for the external interface. The IP address data specified for the external interface is only used for downloading the configuration prior to operation in ghost mode. |

#### Configuring IP address parameters

##### Meaning

Specify network parameters such as the IP address and subnet mask for the interface(s) of the security module.

##### How to access this function

1. Select the module to be edited.
2. Select "External interface [P1] red" or "DMZ interface [P3] yellow" in the local security settings. The virtual tunnel interface can only be configured when the security module (only SCALANCE S612/S623/S627-2M as of V4) is in at least one VPN group, refer to the section "Meaning of the tunnel IP address".
3. If applicable, enable the interface using the "Activate interface" check box.
4. Select the "Ethernet addresses" entry.
5. Complete the settings specified in the following table.

**Note**

**Configuration of the internal interface in routing mode**

If you have selected the "Routing" mode for the security module, you must also configure an internal IP address and subnet mask for the internal interface of the security module. You can access this function in the local security settings under "Internal interface [P2] green" > Ethernet addresses".

| Parameter | Meaning |
| --- | --- |
| IP address | IP address for the external interface.  The IP address consists of four decimal numbers from 0 to 255, with each number being separated by a period, for example, 141.80.0.16. |
| Subnet mask | The subnet mask consists of four decimal numbers that are separated by period, for example, 255.255.0.0 |
| Use router (not possible for the tunnel interface) | Select this check box if you want to use a standard router and enter its IP address in the "Router address" input box. |

> **Note**
>
> **Networking the physical interfaces**
>
> Network the physical interfaces of the security module with suitable subnets to avoid IP address conflicts.

##### Meaning of the tunnel IP address

If you use the function "NAT/NAPT in the VPN tunnel" for a SCALANCE S612/S623/S627-2M module as of V4, you need to assign a tunnel IP address for the security module. This ensures the reachability of the security module via the VPN tunnel and provides a configuration and diagnostics option. The configured tunnel IP address can be expanded with alias tunnel IP addresses using suitable NAT / NAPT rules. The subnet mask is fixed at 32 bits for the tunnel IP address and cannot be changed by the configuration. The tunnel IP address can only be configured if the security module is in at least one VPN group.

You will find further information on address translation with NAT/NAPT in VPN tunnels in the following section:  
[Address translation with NAT/NAPT in VPN tunnels](#address-translation-with-natnapt-in-vpn-tunnels-1)

##### Special features with a standard router

- If the IP assignment configured is via "PPPoE", a configured standard router is ignored because the standard route is always automatically via the PPPoE interface.
- If the address assignment configured is with "Static address" and if the security module is connected to the Internet via a DSL (NAPT) router, the DSL router must be entered as the standard router.
- For security modules in ghost mode (SCALANCE S602 as of V3.1 only), no standard routers can be configured since these are identified during runtime. Specific routes cannot be configured for security modules in ghost mode.

#### Configuring port mode

##### Meaning

The port mode specifies the transmission speed and the duplex method. The same parameters should be set for the ports involved in communication.

##### Configurable port modes

For SCALANCE S modules, the following port modes can be configured for the built-in ports:

| Port mode | Meaning |
| --- | --- |
| Autonegotiation | The transmission speed and the duplex setting are selected automatically.   **Note**   A transmission speed of 1000 Mbps and the autocrossing function are supported only if autonegotiation is selected. |
| 10 Mbps, half and full duplex | Transmission speed of 10 Mbps |
| 100 Mbps, half and full duplex | Transmission speed of 100 Mbps |

Deactivating a port is possible only for external ports and for the DMZ port of SCALANCE S623/S627-2M. The port modes for media module ports are configured in the device view and are based on the range of functions of the media module in question.

#### Configuring an Internet connection

##### Requirement

The "PPPoE" entry is only displayed in the local security settings if the IP assignment method "PPPoE" is configured for one of the interfaces.

##### How to access this function

1. Select the security module to be edited
2. In the local security settings, select the entry "PPPoE".

##### Meaning

In this entry, you make settings related to the Internet Service Provider (ISP) if a connection using PPPoE is set for one of the interfaces of the security module.

Settings for the ISP account

| Function | Description |
| --- | --- |
| Authentication protocol | Select none or one of the following authentication protocols:  - PAP (Password Authentication Protocol) - CHAP (Challenge Handshake Authentication Protocol)    **Note**   Both communications partners have to use the same authentication method otherwise no connection can be established. |
| User name | Enter the name for logging in with the ISP account. |
| Password | Enter the password for logging in with the ISP account. |
| Repeat password | Enter the password for logging in with the ISP account again. |

Rules for user names and passwords

| Symbol | Meaning |
| --- | --- |
| Permitted characters | The following characters from the ANSI X 3.4-1986 character set are permitted:  0123456789  A...Z a...z  !#$%&()"*'+`,-./:;<=>?@ [\]_{|}~^ |
| Length of the user name | 1 to 120 characters |
| Length of the password | 1 to 31 characters |

Settings for the connection

| Symbol | Meaning |
| --- | --- |
| **Function** | **Description** |
| Permanent connection | Permanent Internet connection. After the connection has been terminated by the provider, the connection is automatically restored even if there are currently no packets to be sent. |
| On-demand connection | The Internet connection is established automatically if packets need to be sent to the Internet.   In this setting, delays in the sending of packets are possible. |
| Maximum idle time (only with the setting "on-demand connection") | If no packets are sent during a certain time, the Internet connection is automatically terminated. In the "Maximum idle time" box, enter the time in seconds after which the connection will be terminated.  - Default setting: 300 - Minimum value: 10 - Maximum value: 3600 |
| Forced disconnection (only with the "Permanent connection" setting) | Select the check box to be able to adapt the time of the forced disconnection by the security module. |
| Forced disconnection time (only with the "Permanent connection" setting) | The provider terminates the Internet connection automatically after a certain period. If you enter a time of day in this box, the security module terminates the Internet connection itself at this time. This allows disconnection of the Internet connection by the provider to be delayed under certain circumstances. A self-initiated forced disconnection is only possible with an existing permanent connection.  - Default setting: 00.00 - Permitted entries: 00:00 ... 23:59 |

#### Configuring DNS

##### Module-specific function

DNS server and its functions can be used by SCALANCE S modules.

##### DNS

To address network notes using FQDNs the security module must know the IP address of a DNS server that converts the DNS queries to the corresponding IP addresses of the network nodes.

##### Setting up DNS - Follow the steps below:

1. Select the security module to be edited.
2. In the local security settings, select the entry "DNS".

| Option | Meaning |
| --- | --- |
| Obtain DNS server address automatically | The address of the DNS server can be obtained automatically using PPPoE if the security module is connected to the Internet via a DSL modem. Can only be set for the external interface and the DMZ interface. If PPPoE is set for one of these interfaces and no DNS server is configured, the option "Obtain DNS server address automatically" is set by STEP 7. |
| Use the following DNS server address: | Enter the address of the preferred and of the alternative DNS server manually. |

#### Configuring dynamic DNS

##### Dynamic DNS

With dynamic DNS, you can access a constantly changing IP address with a permanently defined name (FQDN). This is necessary, for example, if you want to access a server that can be reached via a public IP address that changes.

The security module signals the current WAN IP address via which the security module can be reached to a provider for dynamic DNS (for example DynDNS.org, no-ip.com). The provider ensures that DNS queries sent to the FQDN of the security module are replied to with the current WAN IP address of the security module.

Dynamic DNS is permitted on the following interfaces:

- External interface
- DMZ interface

##### Requirement

An account has been created with a provides of dynamic DNS and an FQDN has been registered.

##### Setting up dynamic DNS - Follow the steps below:

| 1. Select the security module to be edited. 2. Select the "Dynamic DNS" entry in the local security settings. 3. Activate the "Activate service" check box in the "Primary dynamic DNS service" area and make the following settings:       | Setting | Meaning |    | --- | --- |    | Provider | Choose the provider with which you have set up an account for dynamic DNS. With the predefined providers (DynDNS.org and No-IP.com), the provider update URL and the check IP service URL are already completed. If you select the option "User defined" you can specify the two URLs manually. |    | Service type | Select whether the HTTP or HTTPS protocol will be used for the provider update URL of the predefined provider. |    | FQDN | Enter the host name (e.g. mysecuritymodule) and the domain name (e.g. dyndns.org) that is registered with the provider separated by a period. The FQDN can function as a VPN endpoint and differ from the FQDN in the "VPN" entry. You can configure which VPN endpoint the VPN partner is informed of in the connection-specific VPN settings. The syntax of an FQDN must comply with DNS. Maximum number of characters: 99 |    | Ignore errors when checking the server certificate | To protect the authentication data the certificate of the update server is checked. If the certificate check fails, the HTTPS connection is terminated as default and the account data is not transferred. If you activate the check box, the HTTPS connection is not terminated if the check fails (e.g. with an expired certificate) and the account data is transferred. You are advised not to ignore the check and not to select the check box. The check box can only be activated if the service type "DDNS-HTTPS" was selected. |    | User | Enter the user name that you specified when you created the account. The syntax of a user name must comply with DNS. Maximum number of characters: 24 |    | Password | Enter the password that you specified when you created the account. The syntax of the password must comply with DNS. Maximum number of characters: 24 |    | Monitor IP address change on DSL router | If the security module is connected to the Internet via a DSL router, enabling this function activates the function of the Check IP service. The security module periodically sends queries to determine the current IP address of the DSL router and to detect an IP address change on the DSL router. The IP address specified in this way is sent to the provider with each change ID. |    | Period | Specify the interval at which the Check IP service is called. - Default setting: 20 minutes - Minimum value: 10 minutes - Maximum value: 1440 minutes |    | Provider update URL | Enter the URL with which the security module reports the public IP address to the provider. The placeholder texts <FQDN> and <CurrentWanIP> need to be placed at the correct positions in the URL. The syntax of the URL must comply with DNS. Maximum number of characters: 127 |    | Check IP service URL | Enter the URL that the security module will use to determine its public IP address. The syntax of the URL must comply with DNS. Maximum number of characters: 127 | 4. In case the primary provider fails, create a second provider in the "Secondary dynamic DNS service" area (optional setting). |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

#### Configuring LLDP

##### Module-specific function

This function is available only for SCALANCE S V4 modules or higher.

##### Requirement

The security module is in routing mode.

##### Meaning

LLDP (Link Layer Discovery Protocol) is a protocol used to discover network topologies. A device capable of LLDP can send information about itself to neighboring devices at regular intervals and at the same time receive information from neighboring devices. The received information is stored on every device with LLDP capability in an LLDP MIB file. Network management systems can access these LLDP MIB files using SNMP and therefore recreate the existing network topology.

##### Configurable parameters

The degree of activity of the security module in terms of LLDP can be configured under the "LLDP mode" entry of the relevant interface.

| Parameter | Description |
| --- | --- |
| Name | Name of the port for which the setting is configured. |
| LLDP mode | Configured LLDP mode:  - RxTx: LLDP frames can be sent and received - Off: No LLDP frames can be sent or received |

#### Media redundancy in ring topologies

This section contains information on the following topics:

- [Media redundancy with MRP](#media-redundancy-with-mrp)
- [Configuring MRP for the security module](#configuring-mrp-for-the-security-module)

##### Media redundancy with MRP

###### Module-specific function

This function is available only for SCALANCE S627-2M modules.

###### Meaning

The term "media redundancy" groups together various methods for increasing availability in Industrial Ethernet networks in which devices can be reached over different paths. This might be achieved by meshing networks, arranging parallel transmission paths or by closing a linear bus topology to form a ring.

###### Media redundancy method MRP

Media redundancy within a ring topology is available with SIMATIC NET products among other things with the MRP method (Media Redundancy Protocol).

With this method, one of the nodes is configured as the redundancy manager. The other nodes are redundancy clients. SCALANCE S627-2M modules can only adopt the role of an MRP client. Using test frames, the redundancy manager checks the ring to make sure it is not interrupted. The redundancy clients forward the test frames. If the test frames of the redundancy manager no longer arrive at the other ring port of the redundancy manager due to an interruption, the redundancy manager switches through its two ring ports and informs the redundancy clients of the change immediately.

The time the SCALANCE X switches need to switch through their ring ports as redundancy manager is 200 ms.

###### Note on the use of MRP

- MRP is supported in ring topologies with up to 100 devices. Exceeding this number of devices can lead to a loss of data traffic.
- It is recommended that you set the ring ports involved to full duplex and 100 Mbps. Otherwise there may be a loss of data traffic.

###### Possible uses of MRP on media module ports

MRP is supported only on the media module ports of the SCALANCE S627-2M. The following table shows the possible uses of MRP on the media module ports of a SCALANCE S627-2M:

| Ring ports | Media module 1 |  | Media module 2 |  |
| --- | --- | --- | --- | --- |
| P4 | P5 | P6 | P7 |  |
| MRP Client | - | - | - | - |
| Ring 1 | Ring 1 | - | - |  |
| - | - | Ring 2 | Ring 2 |  |
| Ring 1 | Ring 1 | Ring 2 | Ring 2 |  |

With two lower-layer rings per SCALANCE S module, layer 3 communication is possible between the rings.

##### Configuring MRP for the security module

###### Requirement

- The security module is in routing mode.
- Media modules are configured for the interfaces to be connected to MRP rings.
- The interfaces of the security module to be connected to rings are networked with the relevant ring managers.

###### How to access this function

1. Select the security module to be edited.
2. In the settings of the required interface, select the "Media Redundancy" entry.

###### Configurable parameters

| Parameter | Meaning | Possible selections |
| --- | --- | --- |
| MRP domain (only if the "MRP client" media redundancy role is selected) | The members of an MRP ring are specified with the help of MRP domains. The same MRP domain must be selected for the interfaces of all modules to be connected to the same MRP ring. | Display of the MRP domain used for the interface. |
| Media redundancy role | Selection of the media redundancy protocol or disabling of media redundancy for the interface. | - Not a node in the ring - MRP Client |
| Ring port 1 (only when the media redundancy role "MRP client" is selected) | Name of the first ring port of the selected interface if the media redundancy role "MRP client" was selected for it. | - |
| Ring port 2 (only when the media redundancy role "MRP client" is selected) | Name of the second ring port of the selected interface if the media redundancy role "MRP client" was selected for it. | - |
| Domain settings | Using the domain settings, you can add new MRP domains, edit the names of existing MRP domains and delete existing MRP domains. | - |
| Alternative media redundancy protocol | Select this check box to enable the interface of the security module for other media redundancy protocols. | - Enable interface for other media redundancy protocols - Disable interface for other media redundancy protocols (default setting) |
| Passive listening | Enable this check box if the selected interface will be connected to third-party networks in which STP/RSTP (Spanning Tree Protocol/Rapid Spanning Tree Protocol) is used. | - Activate passive listening (default) - Deactivate passive listening |

#### Special features of the ghost mode

##### Module-specific function

This function is only available for SCALANCE S602.

##### Meaning

In ghost mode, the security module has no IP address of its own, neither on the internal nor on the external interface. Instead, the security module obtains the IP address for its external interface during runtime from a node connected to the internal interface of the security module whose IP address parameters may be unknown at the time of configuration. It is possible to change an IP address of the internal node and a corresponding IP address at the external interface. Since the internal node is identified based on its MAC address, IP address changes are made only for the learned MAC address. No IP address is configured or obtained at the internal interface of the security module.

As regards the MAC addresses, the security module replaces the MAC address of the internal node with the MAC address of the security module in all outgoing packets on the external interface (responses from the internal node).

##### Activating ghost mode

1. Select the module to be edited.
2. In the local security settings, select the entry "Mode".
3. Select the "Ghost mode" option.

##### Configurable module properties

In ghost mode, the following module properties can be configured in the local security settings:

- External interface [P1] red
- Firewall
- Time-of-day synchronization
- Log settings
- SNMP

Since no DNS servers can be configured in ghost mode, no FQDN resolution is possible.

##### Requirement for identifying an internal node

The security module can only obtain the IP address of the internal node if the internal node initiates data communication with a communications partner of the external network.  
In addition to this, the security module does not provide any server services while obtaining the IP address. The security module can only reply to queries from external after data packets have been sent to the security module by the internal node.

##### Port assignment for incoming and outgoing data connections

Since the external interface of the security module and the internal node have the same IP address, the network components must be addressed explicitly via the TCP/UDP ports. For this reason, the ports are either assigned to the security module or the internal node. The assignments of the ports to the relevant devices are shown in the following tables for incoming and outgoing data connections:

Port assignment for incoming connections (from external to security module)

| Service | Port | Protocol | Comment |
| --- | --- | --- | --- |
| Web services, configuration and diagnostics access | 443 | TCP | The HTTPS port is permanently activated for configuration and diagnostics access using STEP 7 and cannot be changed. |
| SNMP | 161 | TCP | Once SNMP is activated in STEP 7, incoming SNMP queries are transmitted via UDP port 161. Transfer via TCP port 161 is also possible, for example, to be able to reach the internal node.     **Note**   After activating SNMP, the SNMP port is permanently assigned to the security module. If SNMP is not activated, the internal node can be accessed using SNMP with the aid of a firewall rule. |
| UDP |  |  |  |

Port assignment for outgoing connections (from security module to external)

| Service | Port | Protocol | Comment |
| --- | --- | --- | --- |
| Syslog | 514 | UDP | If the Syslog service is activated in STEP 7, Syslog messages are transferred via UDP port 514 by the security module. This port assignment cannot be changed. |
| NTP | 123 | UDP | If NTP servers are used for time-of-day synchronization, NTP queries are transferred via UDP port 123. This port assignment cannot be changed. |

##### Recognizable IP addresses and subnet masks

The security module only recognizes internal nodes with IP addresses in the network class ranges A, B or C. The subnet mask is identified by the security module based on the network class (refer to the table "Network classes and corresponding subnet masks"). To allow the subnet mask to be determined correctly, a standard router must be entered for the internal node.

Nodes with IP addresses in the network classes D and E are rejected by the security module.

| Network class | IP addresses |  | Subnet mask |
| --- | --- | --- | --- |
| Low limit | High limit |  |  |
| A | 0.0.0.0 | 127.255.255.255 | 255.0.0.0 |
| B | 128.0.0.0 | 191.255.255.255 | 255.255.0.0 |
| C | 192.0.0.0 | 223.255.255.255 | 255.255.255.0 |
| D | 224.0.0.0 | 239.255.255.255 | Rejected by the security module |
| E | 240.0.0.0 | 255.255.255.255 | Rejected by the security module |

##### Configuration limits

A maximum of one internal node is recognized by the security module. If several internal nodes exist, the security module reacts as follows:

- The first device the security module recognizes in the internal network obtains access to the external network segment if the firewall is suitably configured.
- The data traffic of any additional nodes in the internal network area is blocked in the outgoing direction at level 2 (MAC layer) based on the sender address.

##### Loading configurations and diagnostics after commissioning

After obtaining an IP address from the internal node, the security module has an IP address on the external interface that can differ from the IP address with which the security module was initially configured. To load a configuration or to run diagnostics, in STEP 7 you need to specify the IP address for the connection to the external interface that the security module obtained from the internal node during runtime. This is possible in the local security settings or directly in the "Advanced download" or "Connect online" dialogs. You can find more information on the establishment of online connections in section: [Downloading a configuration](#downloading-a-configuration)

##### Routing information for hierarchical networks on the external interface

If there are hierarchical networks with subnet transitions on the external interface of the security module, the security module needs to obtain the relevant routing information from the internal node. To achieve this, the internal node must respond to ICMP queries sent to it. Responding to ICMP broadcasts is not necessary.

### Authentication using a RADIUS server

This section contains information on the following topics:

- [Overview](#overview-2)
- [Defining a RADIUS server](#defining-a-radius-server)
- [Assigning a RADIUS server to a security module](#assigning-a-radius-server-to-a-security-module)

#### Overview

##### Module-specific function

This function is available only for SCALANCE S V4 modules or higher.

##### Meaning

RADIUS (Remote Authentication Dial-In User Service) is a protocol for authenticating users by servers on which user data can be stored centrally. The use of RADIUS servers can increase the protection of user names, assigned roles and passwords.

##### Scenario for the use of RADIUS servers

Authentication by RADIUS servers can be performed when activating user-specific IP rule sets.

![Scenario for the use of RADIUS servers](images/65882434059_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| 1 | Entry of the user data on the Web page of the security module |
| 2 | Authentication by RADIUS server and activation of the user-specific IP rule set |
| 3 | Access to an automation cell |

The network setup shown above is simply an example. The RADIUS server can also be located in the internal network or in the DMZ network of the security module.

For the configuration options described below, it is assumed that a RADIUS server is configured in STEP 7 and was assigned to the relevant security module. In addition to this, one user or role must be configured with the "RADIUS" authentication method. For more detailed information, refer to the following sections:

- [Defining a RADIUS server](#defining-a-radius-server)
- [Assigning a RADIUS server to a security module](#assigning-a-radius-server-to-a-security-module)

For general information on user-specific IP rule sets, refer to the following section:

- [User-specific IP rule sets](#user-specific-ip-rule-sets)

##### Configuration options

To authenticate the user using a RADIUS server, there are two configuration options available:

- The user and the user's role are known on the security module, only the password management for the user is performed on the RADIUS server. The user and the password are configured on the RADIUS server.

  - A user with the "RADIUS" authentication method is configured.
  - The user is assigned to the user-specific IP rule set.

  Result:

  - When a user logs on to the Web page of the security module, the authentication query is forwarded to the RADIUS server.
  - The RADIUS server runs a password check and signals the result back to the security module.
  - If the password check is passed successfully, the user-specific IP rule set is activated.
- The role is known on the security module, user management is via the RADIUS server. The user and the password are configured on the RADIUS server.

  - A user-defined role or a system-defined role is assigned to the user-specific IP rule set.
  - Under the entry "RADIUS" > "RADIUS settings" in the local security settings of the security module, the check box "Allow RADIUS authentication of unconfigured users" and the check box "Filter ID is required for authentication" are enabled.

  Result:

  - When a user logs on to the Web page of the security module, the authentication and authorization query is forwarded to the RADIUS server.
  - The RADIUS server runs a password check and signals the result back to the security module.
  - Case a: If, in addition to this, the role name is configured on the RADIUS server:

    The RADIUS server returns the role name assigned to the user to the security module.
  - Case b: If the role name is not configured on the RADIUS server:

    The security module assigns the user the system-defined role "radius".
  - If the password check is passed successfully, the user-specific IP rule set is activated.

##### Conventions for RADIUS servers

- The RADIUS servers can be in any network connected to the security module.
- A maximum of two RADIUS servers can be configured per security module. During operation only one of the RADIUS servers is active.
- When defining a RADIUS server, an FQDN can also be used instead of IP an address.
- A maximum of 25 characters can be used for the name of a RADIUS server.

#### Defining a RADIUS server

##### Meaning

Before authentication by a RADIUS server is possible, this first needs to be stored in the STEP 7 project. Following this, you assign the defined RADIUS server to the security module for which the RADIUS server will handle user authentication.

##### Procedure

1. In the global security functions, select the entry "RADIUS".

   Result: The previously created RADIUS servers are displayed under the selected entry.
2. Double-click on the "Add new RADIUS server" entry.  
   Result: The created RADIUS server is displayed with an automatically assigned number below the entry "RADIUS".
3. Double-click on the created RADIUS server.  
   Result: In the working area the assignment dialog for RADIUS servers is displayed. The selected RADIUS server is selected in the "RADIUS server" drop-down list. The required security modules can be assigned to this, see section [Assigning a RADIUS server to a security module](#assigning-a-radius-server-to-a-security-module). In the local security settings, the configurable properties of the RADIUS server are displayed.
4. Enter the following data in the "General" entry in the local security settings:

| Parameter | Meaning |
| --- | --- |
| Name | Name of the RADIUS server.  The name can consist of a maximum of 25 characters. The characters 0-9, a-z, A-Z, -._ can be used. A name must start with a letter and end with a letter or number. Before the ‘.’ character only letters and numbers are permitted, after the ‘.’ character only letters. Before the ‘_’ or ‘-* character only letters and numbers are permitted. |
| IP address / FQDN | IP address or FQDN of the RADIUS server. |
| Port | UDP port via which the RADIUS server can be reached. As default, authentication data is received at port 1812. |
| Shared secret | Entry of the password that will be used when transferring the logon data between the RADIUS server and security modules for encryption.  The following characters from the ANSI X 3.4-1986 character set are permitted:  0123456789  A...Z a...z  !#$%&()"*'+`,-./:;<=>?@ [\]_{|}~^  Length of the shared secret: 1 to 32 characters |
| Repeat shared secret | Confirmation of the password |
| Authentication method | Display of the method used to check the user data. Only the "PAP" method (Password Authentication Protocol) is supported. |
| Retries | Here, enter the maximum number of retries for an attempted request. The initial connection attempt is repeated the number of times specified here before another configured RADIUS server is queried or the login counts as having failed. As default 3 retries are set, this means 4 connection attempts. The range of values is 1 ... 5. |
| Comment | Entry of freely selectable, optional comments. |

##### Result

You have defined a RADIUS server and can now assign this to the required security modules. Note the descriptions in the section below:  
[Assigning a RADIUS server to a security module](#assigning-a-radius-server-to-a-security-module)

#### Assigning a RADIUS server to a security module

##### Requirement

You have defined a RADIUS server.

##### Procedure

1. Select the module to be edited.
2. Select the "RADIUS" entry in the local security settings.
3. Select the "Enable RADIUS authentication" check box.
4. In the "RADIUS timeout" input box, enter the maximum time in seconds that the security module will wait for a response from the RADIUS server.
5. In the "RADIUS repetitions" input box, enter the number of connection establishment attempts with the RADIUS server.
6. Select the "Allow RADIUS authentication of unconfigured users" check box if the user-specific IP rule to be activated was assigned a role instead of a user.
7. Select the "Filter ID is required for authentication" check box if the assigned role is a user-defined role.
8. Under the entry "RADIUS server", select the RADIUS server you want to assign to the security module from the "Name" drop-down list.

   As an alternative, you can assign security modules for which RADIUS authentication is enabled to RADIUS servers in the global security functions. You will find general information on authentication by the RADIUS server in the following section:

   [Authentication using a RADIUS server](#authentication-using-a-radius-server-1)

**Note**

**Changing the method of authentication with the Web server on the security module**

If RADIUS authentication is enabled on the security module, the method for authentication with the Web server is changed from "Digest Access Authentication" to "Basic Access Authentication".

### Setting up a firewall

This section contains information on the following topics:

- [Local firewall rules for SCALANCE S modules](#local-firewall-rules-for-scalance-s-modules)
- [User-specific IP rule sets](#user-specific-ip-rule-sets)
- [IP packet filter directions SCALANCE S](#ip-packet-filter-directions-scalance-s)
- [MAC packet filter directions SCALANCE S](#mac-packet-filter-directions-scalance-s)
- [Adapting standard rules for IP services](#adapting-standard-rules-for-ip-services)

#### Local firewall rules for SCALANCE S modules

This section contains information on the following topics:

- [Configuring a firewall with predefined firewall rules](#configuring-a-firewall-with-predefined-firewall-rules)

##### Configuring a firewall with predefined firewall rules

This section contains information on the following topics:

- [Configuring a firewall using predefined firewall rules](#configuring-a-firewall-using-predefined-firewall-rules)
- [Configuring a firewall with predefined MAC rules](#configuring-a-firewall-with-predefined-mac-rules)

###### Configuring a firewall using predefined firewall rules

###### How to access this function

1. Select the module to be edited.
2. Select the "Firewall" entry in the local security settings.

###### Firewall enabled as default

The "Enable firewall" check box is enabled by default. The firewall is therefore activated automatically and all access from external to the security module is blocked. By clicking the relevant check box, enable the firewall rules for the specific direction.

> **Note**
>
> **Detailed firewall settings in advanced firewall mode**
>
> In advanced firewall mode, you can restrict firewall rules to individual nodes. To change to advanced firewall mode, select the "Enable firewall in advanced mode" check box. For more detailed information about the advanced firewall mode, refer to the section  
> [Overview of local firewall rules](#overview-of-local-firewall-rules)

###### Firewall configuration with VPN

If the security module is in a VPN group, the "Only tunneled communication" check box is enabled as default. This means that only encrypted IPsec data transfer is permitted via the external interface or via the DMZ interface. Only HTTPS access to the module (TCP port 443) remains allowed untunneled.

If you deselect the check box, tunneled communication and also the types of communication selected in the other boxes are permitted.

All tables
Available firewall rules and directions

Available firewall rules and directions

| Service | From internal to external | From external to internal | From internal to DMZ | From DMZ to internal | Enabled ports | Meaning |
| --- | --- | --- | --- | --- | --- | --- |
| Allow IP communication | **x** | **x** | **x** | **x** | - | IP communication for the selected communication directions is allowed. |
| Allow S7 protocol | **x** | **x** | **x** | **x** | TCP port 102 | Communication of the nodes using the S7 protocol is allowed. |
| Allow FTP/FTPS (explicit mode) | **x** | **x** | **x** | **x** | TCP port 20  TCP port 21 | For file management and file access between server and client. |
| Allow HTTP | **x** | **x** | **x** | **x** | TCP port 80 | For communication with a Web server. |
| Allow HTTPS | **x** | **x** | **x** | **x** | TCP port 443 | For secure communication with a Web server, for example, for Web diagnostics. |
| Allow DNS | **x** | **x** | **x** | **x** | TCP port 53  UDP port 53 | Communication connection to a DNS server is allowed. |
| Allow SNMP | **x** | **x** | **x** | **x** | TCP port 161/162   UDP port 161/162 | For monitoring nodes capable of SNMP. |
| Allow SMTP | **x** | **x** | **x** | **x** | TCP port 25 | For sending e-mails via an SMTP server. |
| Allow NTP | **x** | **x** | **x** | **x** | UDP port 123 | For time synchronization |
| Allow DHCP | **x** | **x** | **x** | **x** | UDP port 67  UDP port 68 | Only in bridge mode Communication connection with a DHCP server is permitted. |

Logging

| Option | Action when activated |
| --- | --- |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All IP packets transferred via the tunnel are logged. |
| Log blocked incoming packets | All incoming IP packets that are discarded are logged. |
| Log blocked outgoing packets | All outgoing IP packets that are discarded are logged. |

You can view the logged packets at the "Packet filter log" entry in the "Online & Diagnostics" dialog. For more detailed information, refer to the section [Logging data packets - "Packet filter log" entry](#logging-data-packets---packet-filter-log-entry).

###### Configuring a firewall with predefined MAC rules

###### How to access this function

1. Select the module to be edited.
2. Select the "Firewall" entry in the local security settings.

###### Firewall enabled as default

The "Enable firewall" check box is enabled by default. The firewall is therefore activated automatically and all access from external to the security module is blocked. By clicking the relevant check box, enable the firewall rules for the specific direction.

> **Note**
>
> **Detailed firewall settings in advanced firewall mode**
>
> In advanced firewall mode, you can restrict firewall rules to individual nodes. To change to advanced firewall mode, select the "Enable firewall in advanced mode" check box. For more detailed information about the advanced firewall mode, refer to the section [Overview of local firewall rules](#overview-of-local-firewall-rules).

###### Firewall configuration with VPN

If the security module is in a VPN group, the "Tunnel communication only" check box is enabled as default.

If you deselect the check box, tunneled communication and also the types of communication selected in the other boxes are permitted.

###### Available MAC rules and directions

| Service | From internal to external | From external to internal | Meaning |
| --- | --- | --- | --- |
| Allow MAC communication | **x** | **x** | MAC traffic for the selected communication directions is allowed. |
| Allow ISO protocol | **x** | **x** | ISO traffic for the selected communication directions is allowed. |
| Allow SiClock | **x** | **x** | SiClock time-of-day frames for the selected communication directions are allowed. |
| Allow DCP | **x** | **x** | DCP traffic for assignment of IP addresses is allowed for the selected communications directions. |

Logging

| Option | Action when activated |
| --- | --- |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All MAC packets transferred via the tunnel are logged. |
| Log blocked incoming packets | All incoming MAC packets that are discarded are logged. |
| Log blocked outgoing packets | All outgoing MAC packets that are discarded are logged. |

#### User-specific IP rule sets

This section contains information on the following topics:

- [Overview](#overview-3)
- [Creating and assigning user-specific IP rule sets](#creating-and-assigning-user-specific-ip-rule-sets)

##### Overview

###### Meaning

Initially, individual or multiple users are assigned to user-specific IP rule sets. The user-specific IP rule sets are then assigned to individual or multiple security modules. This makes it possible, to allow user-specific access. If, for example all access to the networks downstream from a security module is blocked, certain nodes can be allowed for a user based on their IP addresses. This means that access is allowed for this user but access remains blocked for other users.

###### User logon via the Internet

The user can log in to the external interface or the DMZ interface via the Web page of the security module. If authentication is successful, the IP rule set defined for the user for the IP address of the device from which the login is made is enabled.

The connection to the Web page of the security module is via HTTPS using the IP address of the connected port and taking into account the valid routing rules:

Example:

External interface: 192.168.10.1

Call up of the login page with: https://192.168.10.1/

Users can log on with every role as long as the user or the role is assigned to a user-specific firewall rule set.

###### Options for authenticating the user

Depending on the authentication method selected when the user who will log in to the security module was created, the authentication is handled by different instances:

- Authentication method "Password": Authentication is handled by the security module.
- Authentication method "RADIUS": Authentication is handled by a RADIUS server (SCALANCE S as of V4 only).

###### Assignment of roles to user-specific IP rule sets

On SCALANCE S modules as of V4, it is also possible to assign user-specific IP rule sets that are assigned to roles. This makes it possible to enable a group of users for access to certain IP addresses.

If a RADIUS server is used for user authentication and a role is assigned to the user-specific IP rule set, users can also be authenticated by the RADIUS server although they are not configured on the security module. These users must be stored on the RADIUS server or on a separate database where they need to be assigned to the role assigned to the user-specific IP rule set in STEP 7. This procedure has the advantage that all user data is stored exclusively on the RADIUS server.

You will find more information on authentication by the RADIUS server in the following section:

[Authentication using a RADIUS server](#authentication-using-a-radius-server-1)

###### User-specific IP rule sets are used locally - conventions

The same conventions as described in the following section apply:  
[Global firewall rule sets - conventions](#global-firewall-rule-sets---conventions)

##### Creating and assigning user-specific IP rule sets

###### Creating user-specific IP rule sets

1. In the global security functions, select the entry "Firewall" > "User-specific IP rule sets" > "IP rule sets".
2. Double-click on the "Add new IP rule set" entry to create a user-specific IP rule set.

   Result: The created user-specific IP rule set is shown in the entry.
3. Double-click on the created user-specific IP rule set.

   Result: In the "Properties" > "General" tab of the Inspector window, the configurable properties of the user-specific IP rules set are displayed.
4. In the Inspector window, click on the "General" entry and enter the following data:

   - Name: Project-wide, unique name of the rule set. The name appears in the local rule list of the security module after the rule set is assigned.
   - Description (optional): Enter a description of the user-specific IP rule set.
5. Click on the "IP rules" entry and enter the firewall rules one after the other in the list.  
   No IP address can be entered in the “Source IP address” box. This is entered automatically when the node logs on to the security module.  
   The “Stateful” check box cannot be disabled for IP rules of user-specific IP rule sets   
   Note the parameter description in the following sections:  
   [Defining IP packet filter rules](#defining-ip-packet-filter-rules)

   Note the special features of firewall rules generated automatically by STEP 7 for NAT/NAPT rules:  
   [Relationship between NAT/NAPT router and user-specific firewall](#relationship-between-natnapt-router-and-user-specific-firewall-1)

###### Create RADIUS user and RADIUS roles locally

In addition to the system-defined users or roles, you can also create RADIUS user and RADIUS roles locally:

1. Click on the "Users and roles" entry in the Inspector window.
2. In the "Available users and roles" area, select the entry "<Create RADIUS user/role>".
3. Enter a name.
4. Select whether the name is to be assigned as user or role.
5. Click the "Create" button.

The created user or role is displayed in the list of available users and roles and can be assigned to a user-specific IP rule set.

###### Delete users and roles

The entry can only be deleted if it is not assigned to any other user-specific IP rule set.

To delete users and roles, follow the steps below:

1. Select the entry you want to delete.
2. In the shortcut menu, select the "Delete" command or press the <Del> key.

###### Assigning user-specific IP rule sets

1. Click on the "Users and roles" entry in the Inspector window.
2. In the "Available users and roles" area, select the users or roles you want to assign to the user-specific IP rule set.
3. Click the "<<" button to assign the selected users or roles to the user-specific rule set. The assignment of roles to user-specific IP rule sets is possible only for SCALANCE S modules as of V4.
4. Assign the created user-specific IP rule set to the required security modules using the entry "Assign user-specific IP rule set" in the global security functions. For this, advanced firewall mode must be enabled for the security modules.

**Note**

**Assignment of user-specific IP rule sets**

- A security module can only be assigned one user-specific rule set per user.
- Due to the assignment, the right to log in to the security module is activated implicitly for all users and roles assigned to the IP rule set.

###### Range of values for the maximum session time

Maximum time for which the user may be logged in to a device. After the time has expired, the user is logged out from the device.

- Default setting: 30 minutes
- Minimum value: 5 minutes
- Maximum value: 480 minutes

###### Result

- The user-specific rule set is used by the assigned security modules as a local rule set and automatically appears in the local list of firewall rules.
- The user can log on with the security module. Authentication of the user is performed depending on the selected authentication method either by the security module or a RADIUS server.

  ![Result](images/41279382667_DV_resource.Stream@PNG-en-US.png)

#### IP packet filter directions SCALANCE S

##### Meaning

Possible selections for the communication directions "From" and "To" in the IP rules of the advanced firewall mode.

##### The following directions are available

| Available options / ranges of values |  | Security module |  |  |
| --- | --- | --- | --- | --- |
| **From** | **To** | **S602** | **S61x** | **S623 / S627-2M** |
| Internal | External | **x** | **x** | **x** |
| Tunnel | - | **x** | **x** |  |
| Any | - | **x** | **x** |  |
| DMZ | - | - | **x** |  |
| Internal | **x** | **x** | **x** |  |
| External | Internal | **x** | **x** | **x** |
| Any | - | - | **x** |  |
| Tunnel | - | - | **x** |  |
| DMZ | - | - | **x** |  |
| Tunnel | Internal | - | **x** | **x** |
| External | - | **x** | **x** |  |
| DMZ | - | - | **x** |  |
| Any | Internal | - | **x** | **x** |
| External | - | - | **x** |  |
| DMZ | - | - | **x** |  |
| DMZ | Internal | - | - | **x** |
| External | - | - | **x** |  |
| Any | - | - | **x** |  |
| Tunnel | - | - | **x** |  |
| **x** = communication direction is configurable  - = communication direction is not configurable |  |  |  |  |

#### MAC packet filter directions SCALANCE S

##### Meaning

Possible selections for the communication directions "From" and "To" in the MAC rules of the advanced firewall mode.

##### The following directions are available

| Available options / ranges of values |  | Security module |  |  |
| --- | --- | --- | --- | --- |
| **From** | **To** | **S602** | **S61x** | **S623 / S627-2M** |
| Internal | External | **x** | **x** | **x** |
| Tunnel | - | **x** | **x** |  |
| Any | - | **x** | **x** |  |
| External | Internal | **x** | **x** | **x** |
| Any | - | - | **x** |  |
| Tunnel | - | - | **x** |  |
| Tunnel | Internal | - | **x** | **x** |
| External | - | **x** | **x** |  |
| Any | Internal | - | **x** | **x** |
| External | - | - | **x** |  |
| **x** = communication direction is configurable  - = communication direction is not configurable |  |  |  |  |

#### Adapting standard rules for IP services

##### Requirement

This function is available only in advanced firewall mode.

##### How to access this function

1. Select the security module to be edited.
2. In the local security settings, select the entry "Firewall" > "Standard rules for IP services".

##### Meaning of the advanced settings

| Parameter | Meaning when activated |
| --- | --- |
| Use advanced status options | The permitted number of connections and firewall statuses per time unit is limited. If a network node exceeds this limit, its IP address is entered in the IP blacklist of the security module. The node can then no longer communicate via the security module. The IP blacklist of the security module can be viewed in online mode. |
| Log all activated rules | Packets that are allowed according to the default rules for IP services are logged. |
| Enable ICMP test for interfaces | Ping queries coming in on an interface of the security module can be forwarded to other interfaces. This means that, for example, ping queries can be made from the external network to the internal interface of the security module. |

##### Default firewall rules for SCALANCE S

The following table lists the default firewall rules for SCALANCE S modules. In some cases, the firewall rules are only set if the relevant service is used by the security module (e.g. SNMP).

| Service | Direction | X1 interface (red) | Interface X2 (green) | Interface X3 (yellow) (only for S623, S627-2M) | Tunnel interface* (not for S602) |
| --- | --- | --- | --- | --- | --- |
| Interface rerouting | outgoing | **-** | **x** | - | **-** |
| HTTPS |  | **x** | **x*** | **x** | **x** |
| ICMP | incoming | **-** | **x** | - | **x** |
| ICMP pathfinder (only for SCALANCE S S602 as of V3.1 in ghost mode) | outgoing | **-** | **x** | - | - |
| SNMP | incoming | **x** | **x** | **x** | **x** |
| Syslog | outgoing | **x** | **x** | **x** | **x** |
| NTP | outgoing | **x** | **x** | **x** | **x** |
| DNS | outgoing | **x** | **x** | **x** | **x** |
| HTTP | outgoing | **x** | **-** | **x** | **-** |
| VPN (IKE) |  | **x** | **-** | **x** | **-** |
| VPN (NAT Traversal) |  | **x** | **-** | **x** | **-** |
| BootP Server | incoming | **-** | **x** | **x** | **-** |
| BootP Client | outgoing | **-** | **x** | **x** | **-** |
| RADIUS | outgoing | **x** | **x** | **x** | **x** |
| CARP (only for SCALANCE S62x as of V4) | outgoing | **x*** | **x*** | - | - |
| Pfsync (only for SCALANCE S62x as of V4) | outgoing | - | - | **x*** | - |

**x** enabled as default

- disabled as default

* cannot be adapted

### SCALANCE S module as router

This section contains information on the following topics:

- [Specifying routes](#specifying-routes)
- [Address translation with NAT/NAPT in VPN tunnels](#address-translation-with-natnapt-in-vpn-tunnels-1)
- [Relationship between NAT/NAPT router and user-specific firewall](#relationship-between-natnapt-router-and-user-specific-firewall-1)

#### Specifying routes

##### Meaning

Specifies routes for addressing subnets that cannot be reached directly via the security module.

##### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the "Routing" entry.
3. Double-click "Add new" in the table to add a route.
4. Enter the following values:

| Parameter | Function | Example of a value |
| --- | --- | --- |
| Network ID | Requests to nodes of the subnet with the network ID and the subnet mask specified here are forwarded to the subnet via the specified router IP address.  Based on the network ID, the router recognizes whether a destination address is inside or outside the subnet.  The specified network ID must not be located in the same subnet as the IP address of the security module. | 192.168.11.0 |
| Subnet mask | The subnet mask determines the network structure. Based on the network ID, the router recognizes whether a destination address is inside or outside the subnet. | 255.255.255.0 |
| Router IP address | IP address of the router that connects to the subnet. As an alternative, an FQDN can be entered for SCALANCE S modules as of V4.  The specified router IP address must be in the same subnet as the IP address of the security module. | 192.168.10.2 |
| Activate rerouting (only for SCALANCE S as of V3) | Select this check box if the frames of the entered route will enter and leave on the same interface of the security module (rerouting). Rerouting is only supported on the internal interface of the security module. |  |

#### Address translation with NAT/NAPT in VPN tunnels

##### Module-specific function

Address translation with NAT/NAPT in VPN tunnels is only available for SCALANCE S612/S623/S627-2M modules.

##### Meaning

Address translations with NAT/NAPT can also be performed for communications relations established via a VPN tunnel.

##### Requirements

The following requirements apply generally to a SCALANCE S module that will perform an address translation with NAT/NAPT in a VPN tunnel:

- The SCALANCE S module is in a VPN group.
- The SCALANCE S module is in routing mode and/or the DMZ interface of the SCALANCE S module is activated.
- The tunnel interface is enabled.
- The advanced firewall mode is enabled.
- The firewall is enabled in the editor for IP rules.

##### Supported address translation directions

The address translation directions described in the following section are supported:  
[NAT/NAPT routing](#natnapt-routing)

##### Supported address translation actions

With tunneled communications relations, the following address translation actions are supported:

- Destination NAT ("Redirect")
- Source NAT ("Masquerading")
- Source and Destination NAT ("1:1-NAT")
- NAPT ("Port forwarding")

You will find basic information on these address translation actions in the following section:  
[NAT/NAPT routing](#natnapt-routing)

##### Supported VPN links

In conjunction with NAT/NAPT, the following VPN links are supported:

| VPN link |  | VPN link is initiated by | Address translation is performed by |
| --- | --- | --- | --- |
| SCALANCE S (a) | SCALANCE S (b) | SCALANCE S (a) or SCALANCE S (b) | SCALANCE S (a) and/or SCALANCE S (b) |
| SCALANCE S | CP 343-1 Adv. / 443-1 Adv. / PC-CP | SCALANCE S or CP 343-1 Adv. / 443-1 Adv. / PC-CP | SCALANCE S |

* Only 1:1 NAT is supported.

SCALANCE S modules of the type SCALANCE S623 V4 and SCALANCE S627-2M V4 that have a VPN endpoint on the external interface and on the DMZ interface can perform address translations on both interfaces at the same time.

##### Address translation characteristics when involved in several VPN groups

If a SCALANCE S module is a member of several VPN groups, the address translation rules configured for the tunnel interface of the SCALANCE S module apply for all VPN connections of this SCALANCE S module.

Please note: Once you have configured a NAT address translation to or from the direction of the tunnel, only the IP addresses involved in the NAT address translation rules can be reached via the VPN tunnel.

#### Relationship between NAT/NAPT router and user-specific firewall

##### Module-specific function

The configuration of NAT/NAPT rules in the user-specific firewall is only available for SCALANCE S modules.

##### Meaning

After creating NAT/NAPT rules, STEP 7 automatically generates a user-specific IP rule set in the user-specific firewall that enables communication in the configured address translation direction. You can then assign this user-specific IP rule set to individual or multiple users and/or individual or multiple roles (only for SCALANCE S modules).

The generated firewall rules can, if necessary, be moved and expanded (additional IP address, services, transmission speed). Firewall parameters generated by STEP 7 cannot be adapted. If the user-specific IP rule set is assigned to a security module with NAT/NAPT deactivated, the NAT/NAPT rules from the user-specific firewall are also applied to this security module.

> **Note**
>
> The address translation actions "Source-NAT + Destination-NAT" and "Double-NAT" are not supported in conjunction with the user-specific firewall.

##### How to access this function

"NAT" or "NAPT" entry in the editor for user-specific IP rules sets, refer to the following section:  
[Creating and assigning user-specific IP rule sets](#creating-and-assigning-user-specific-ip-rule-sets)

##### Supported address translation directions for the action "Source NAT"

The action "Source NAT" can be performed in the following directions:

- External to DMZ
- DMZ to external

No IP address can be entered in the "Source IP address" box. This is entered automatically when the node logs on to the security module.

##### Supported address translation directions for the action "Destination NAT"

The action "Destination NAT" can be performed in the following directions:

- External to internal
- External to DMZ
- DMZ to internal
- DMZ to external
- Tunnel to internal (only SCALANCE S612/S623/S627-2M)
- Tunnel to external (only SCALANCE S612/S623/S627-2M)
- Tunnel to DMZ (only SCALANCE S612/S623/S627-2M)

##### Supported address translation directions for NAPT

The address translation with NAPT can be performed in the following directions:

- External to internal
- External to DMZ
- DMZ to internal
- DMZ to external
- Tunnel to internal (only SCALANCE S612/S623/S627-2M)
- Tunnel to external (only SCALANCE S612/S623/S627-2M)
- Tunnel to DMZ (only SCALANCE S612/S623/S627-2M)

##### NAT/NAPT address translation and corresponding user-specific IP rule sets

In the firewall rules for user-specific IP rule sets generated based on NAT/NAPT rules, no IP address can be entered in the "Source IP address" box. This is entered automatically when the node logs on to the security module. The remaining properties generated locally for individual security modules are identical. Refer to the section   
[Relationship between NAT/NAPT router and firewall](#relationship-between-natnapt-router-and-firewall)

### Security module as DHCP server

This section contains information on the following topics:

- [Overview DHCP server](#overview-dhcp-server)
- [Configuring a DHCP server](#configuring-a-dhcp-server)

#### Overview DHCP server

##### Overview

You can operate the SCALANCE S module on the internal network and on the DMZ network as DHCP server (DHCP = Dynamic Host Configuration Protocol). This allows IP addresses to be assigned automatically to the devices connected to the internal network or the DMZ network.

Simultaneous DHCP server operation on both interfaces is possible (SCALANCE S623/S627-2M only).

The IP addresses are either distributed dynamically from an address range you have specified or you can select a specific IP address and assign it to a particular device. If devices on the internal interface or on the DMZ interface should always be assigned the same IP address for firewall configuration, the address assignment must only be static based on the MAC address or based on the client ID.

##### Requirements

You configure the devices on the internal network or on the DMZ network so that they obtain the IP address from a DHCP server.

Depending on the mode, the security module sends an IP address of the standard router to the nodes in the relevant subnet or you need to inform the nodes in the subnet of a router IP address.

- Router IP address will be transferred

  In the following situations, the DHCP protocol of the security module will inform the nodes of the router IP address:

  - The node is connected to the DMZ interface (SCALANCE S623/S627-2M only)  
    In this case, the security module sends its own IP address as the router IP address.
  - The node is connected to the internal interface and the security module is configured for router mode  
    In this case, the security module sends its own IP address as the router IP address.
  - The node is connected to the internal interface and the security module is not configured for router mode, there is, however, a standard router specified in the configuration of the security module.  
    In this case, the security module transfers the IP address of the standard router as the router IP address.
- Router IP address will not be transferred

  In the following situations, enter the router IP address manually on the node:

  - The node is connected to the internal interface and the security module is not configured for router mode. There is also no standard router specified in the configuration of the security module.

---

**See also**

[Configuring a DHCP server](#configuring-a-dhcp-server)

#### Configuring a DHCP server

##### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "DHCP server".
3. Select the interface for which you want to make the DHCP settings.
4. Make the address assignment. You have the following configuration options:

   - Static address assignment

     Devices with a specific MAC address or client ID are assigned the specified IP addresses. You specify these addresses by entering the devices in the address list in the "Static address assignment" group box.
   - Dynamic address assignment

     Devices whose MAC address or whose client ID was not specified specifically, are assigned a random IP address from the specified address range. For this purpose, activate the "Dynamic IP address pool" check box. Set the address range in the "Dynamic IP address pool" input area.

> **Note**
>
> **Dynamic address assignment - reaction after interrupting the power supply**
>
> Please note that dynamically assigned IP addresses are not saved if the power supply is interrupted. On return of the power, you must therefore make sure that the nodes request an IP address again.
>
> You should therefore only use dynamic address assignment for the following nodes:
>
> - Nodes that are used temporarily in the subnet (such as service devices).
> - Nodes that have been assigned an IP address and send this as the "preferred address" the next time they request an address from the DHCP server (for example PC stations).
>
> For permanent nodes you should preferably use static address assignment by specifying a client ID or the MAC address.

##### Consistency check - these rules must be adhered to

Remember the following rules when making the entries.

- The IP addresses assigned in the address list in the "Static address assignments" group box must not be in the range of the dynamic IP addresses.
- IP addresses, MAC addresses and client IDs may only occur once in the "Static address assignment" table (related to the security module).
- For the statically assigned IP addresses, you must specify either the MAC address or the client ID (computer name).
- The client ID is a string with a maximum of 63 characters. Only the following characters may be used: a-z, A-Z, 0-9 and - (dash).

  **Note**

  In SIMATIC S7, a client ID can be assigned to the devices on the Ethernet interface to allow them to obtain an IP address using DHCP.

  With PCs, the procedure depends on the operating system being used; it is advisable to use the MAC address here for the assignment.
- For the statically assigned IP addresses, you must specify the IP address.
- The following IP addresses must not be in the range of the free IP address range (dynamic IP addresses):

  - All router IP addresses in the "Routing" entry
  - Syslog server
  - Standard router
  - Security module address(es)
- DHCP is supported by the security module on the interface to the internal subnet and on the interface to the DMZ network. The following additional requirements for IP addresses in the range of the dynamic address assignments result from this operational behavior of the security module:

  - Bridge mode

    The range must be within the network defined by the security module.
  - Routing mode

    The range must be within the internal subnet defined by the security module.

    **Note**

    The DMZ network always represents a separate subnet. When using DHCP on the DMZ interface, make sure that the free IP address range (dynamic IP addresses) is within the DMZ subnet.
- The free IP address range must be fully specified by entering the start address and the end address. This end address must be higher than the start address.
- The IP addresses you enter in the address list in the "Static address assignments" input area must be in the address range of the internal subnet or in the DMZ subnet of the security module.

---

**See also**

[Running a consistency check](#running-a-consistency-check)

### Configuring proxy ARP

#### Overview

Proxy ARP allows routers to respond to ARP queries for hosts. The hosts are in networks separated by routers but use the same IP address range.

If PC1 sends an ARP request to PC2, it receives an ARP response and the hardware address of the interface (MAC address of the port of the security module) on which the query was received from the security module located in between and not from PC2. The querying PC1 then sends its data to the security module that then forwards it to PC2.

#### How to access this function

This function is only available for the internal interface of a security module that is a member of a VPN group and is in bridge mode.

1. Select the security module to be edited.
2. In the local security settings, select the entry "Proxy ARP".
3. If the security module is to respond to an ARP query from its own LAN as a substitute for the specific connection partner, enter the corresponding IP address.

### IPsec tunnel: Creating and assigning groups

This section contains information on the following topics:

- [Configuring internal network nodes](#configuring-internal-network-nodes)

#### Configuring internal network nodes

This section contains information on the following topics:

- [Using the learning mode to learn internal nodes](#using-the-learning-mode-to-learn-internal-nodes)
- [Configuring IP network nodes manually](#configuring-ip-network-nodes-manually)
- [Configuring MAC network nodes manually](#configuring-mac-network-nodes-manually)
- [Configuring internal subnets manually](#configuring-internal-subnets-manually)

##### Using the learning mode to learn internal nodes

###### Finding nodes for tunnel communication automatically

One great advantage when configuring and operating tunnel communication is that SCALANCE S modules in bridge mode can find the nodes on the internal interface automatically. New nodes are detected by the security module during operation. The detected nodes are signaled to the security modules belonging to the same VPN group. This allows data exchange within the tunnels of a group in both directions at any time.

###### Detectable nodes

The following nodes are detected:

- Network nodes with IP capability

  Network nodes with IP capability are found when they transmit an ICMP response to the ICMP subnet broadcast.

  IP nodes downstream from routers can be found if the routers pass on ICMP broadcasts.
- ISO network nodes

  You can also teach-in network nodes without IP capability that can be addressed by means of ISO protocols.

  This is only possible if they reply to XID or TEST packets. TEST and XID (Exchange Identification) are auxiliary protocols for exchanging information on layer 2. By sending these packets with a broadcast address, these network nodes can be located.
- PROFINET nodes

  Using DCP (Discovery and basic Configuration Protocol), it is possible to find PROFINET nodes.

Network nodes that do not meet these conditions must be configured manually.

Subnets located on the other side of internal routers also need to be configured manually.

###### How to access the function

1. Select the module.
2. In the local security settings, select the entry "VPN" > "Nodes".

###### Enabling/disabling the learning mode

The learning function is enabled in the configuration as default for every security module.

Learning can also be disabled completely for SCALANCE S. In this case, you will need to configure all internal network nodes participating in the tunnel communication manually.

###### When is it useful to disable the automatic learning mode?

The default settings for the security module assume that internal networks are always secure; in other words, in a normal situation, no network node is connected to the internal network if it is not trustworthy.

Disabling the learning mode can be useful if the internal network is static; in other words, when the number of internal nodes and their addresses do not change.

If the learning mode is disabled, this reduces the load on the medium and the nodes in the internal network resulting from the learning packets. The performance of the security module is also slightly improved since it does not need to process the learning packets.

Note: In the learning mode, all nodes in the internal network are detected. The information relating to VPN configuration limits relates only to nodes that communicate over VPN in the internal network.

> **Note**
>
> If more than 128 internal nodes are being operated, the permitted configuration limits are exceeded and an illegal operating status results. Due to the dynamics in the network traffic, this causes internal nodes that have already been learned to be replaced by new previously unknown internal nodes.

---

**See also**

[Configuring internal subnets manually](#configuring-internal-subnets-manually)

##### Configuring IP network nodes manually

###### Meaning

As an alternative to the learning mode that you enable using the "Enable learning of internal nodes" check box and that allows the security module to learn the internal network nodes dynamically, you can enter the network nodes to be learned manually in the "Internal IP nodes" entry and in doing so enable them for VPN tunnel communication. The MAC address of a network node can be specified as an option.

###### Requirement

- The security module is in bridge mode.
- The security module is a member of a VPN group.

###### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "VPN" > "Nodes" > "Internal IP nodes".

##### Configuring MAC network nodes manually

###### Meaning

As an alternative to the learning mode that you enable using the "Enable learning of internal nodes" check box and that allows the security module to learn the internal network nodes dynamically, you can enter the network nodes to be learned manually in the "Internal MAC nodes" entry and in doing so enable them for VPN tunnel communication.

###### Requirement

- The security module is in bridge mode.
- The security module is a member of a VPN group.

###### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "VPN" > "Nodes" > "Internal MAC nodes".

##### Configuring internal subnets manually

###### Requirement

- The security module is a member of a VPN group.

###### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "VPN" > "Nodes" > "Internal subnets".

###### Security module in bridge mode - "Internal subnets" entry

To be able to enable internal subnets for VPN tunnel communication manually, you need to enter the following address parameters:

| Parameter | Function | Example of a value |
| --- | --- | --- |
| Network ID | Network ID of the subnet to be enabled for VPN tunnel communication.  Based on the network ID, the router recognizes whether a destination address is inside or outside the subnet.  Must not be located in the same subnet as the IP address of the security module. | 192.168.11.0 |
| Subnet mask | The subnet mask determines the network structure. Based on the network ID, the router recognizes whether a destination address is inside or outside the subnet. | 255.255.255.0 |
| Router IP address | IP address of the router via which the subnet you are allowing is reached.  Must be located in the same subnet as the IP address of the security module. | 192.168.10.2 |

###### Security module in routing mode - "Subnets reachable through tunnel" entry

In routing mode, entire subnets are always tunneled. To be able to enable internal subnets reachable via routers, the external subnet or the DMZ subnet for VPN tunnel communication manually, you need to enter the following address parameters:

| Parameter | Function | Example of a value |
| --- | --- | --- |
| Network ID | Network ID of the subnet to be enabled for VPN tunnel communication.  Based on the network ID, the router recognizes whether a destination address is inside or outside the subnet. | 192.168.11.0 |
| Subnet mask | The subnet mask determines the network structure. Based on the network ID, the router recognizes whether a destination address is inside or outside the subnet. | 255.255.255.0 |
| Comment | Entry of additional, optional comments. |  |

### Router and firewall redundancy

This section contains information on the following topics:

- [Overview](#overview-4)
- [Creating redundancy relationships between security modules](#creating-redundancy-relationships-between-security-modules)
- [Configuring redundancy relationships](#configuring-redundancy-relationships)

#### Overview

##### Meaning

Failures of the security modules SCALANCE S623 as of V4 and SCALANCE S627-2M as of V4 can be automatically compensated by routers and firewall redundancy during operation. To do this, group two security modules of the type SCALANCE S623 or SCALANCE S627-2M in a redundancy relationship by activating routers and firewall redundancy for both security modules. Following this, you decide which security module of the redundancy relationship is passive in normal mode (secondary module). You make this setting for the security module of the redundancy relationship that is active in normal operation (primary module). If the primary module fails during operation, the secondary module automatically adopts the function as firewall and (NAT/NAPT) router. To ensure the identical configuration of both security modules, these are connected together via their DMZ interfaces and their configurations are synchronized during operation. In this case, the DMZ interfaces of the security modules involved cannot be used for other purposes.

##### Address redundancy

In addition to their module IP addresses, the two security modules share a common IP address on the external and on the internal interface so that if one of the security modules fails, the IP addresses do not need to be changed. To do this, you need to configure an IP address for the external and for the internal interface of the redundancy relationship.

##### Effects of redundancy relationships on security modules

When you create redundancy relationships between security modules, some properties of these security modules are automatically adapted to establish compatibility with the redundancy relationship. The following properties are affected by this adaptation:

| Module property | Effect on the module property |
| --- | --- |
| Operating mode | Where necessary, the mode is changed to the "Routing mode" option. |
| Membership of VPN groups | Where necessary, the security module is removed from VPN groups. |
| Interface configuration | Where necessary, the external interface and the DMZ interface of the security module are enabled. Where necessary, the IP assignment method "Static address" is configured for all interfaces. |

##### Configuration of security modules in redundancy relationships

After router and firewall redundancy have been enabled and the primary module of the redundancy relationship selected, some of the module properties are configured only using the primary module. The properties configured for the primary module then apply to the redundancy relationship and cannot be configured for the secondary module. The following properties can be configured for the redundancy relationship:

- Basic settings of the redundancy relationship (secondary module, network parameters)
- Firewall (standard rules for IP services are configured separately for the individual security modules).
- Routing
- NAT/NAPT routing (not 1:1 NAT)

The values of the properties listed above are initially adopted from the primary module for the redundancy relationship.

The settings listed below remain active for the individual security modules even after including them in a redundancy relationship. Configuring these properties for the primary module therefore has no effect on the secondary module.

- Interface configuration (disabling interfaces and changing the VIP assignment method "Static address" is not possible).
- Standard rules for IP services (firewall)
- DDNS
- Time-of-day synchronization
- Log settings
- SNMP
- RADIUS

> **Note**
>
> **Loading a configuration on security modules of a redundancy relationship (only SCALANCE S623/S627-2M as of V4)**
>
> The properties of a redundancy relationship configured for the primary module must be loaded both on the primary module and on the secondary module. To load the configuration, the physical IP address via which your engineering station can reach the security module must be used. The virtual IP addresses of the redundancy relationship cannot be used for loading.

> **Note**
>
> **Configuring routing when using routers and firewall redundaancy**
>
> In a redundancy relationship the only routing information that is synchronized between the primary and secondary module is that that was configured statically in the local security settings of the primary module in the “Routing” entry. Routing entries resulting dynamically due to using standard routers are not synchronized. When using routers and firewall redundancy it is therefore recommended that you configure all known routers statically.

#### Creating redundancy relationships between security modules

##### Requirement

The security modules SCALANCE S623/S627-2M as of V4 are not assigned to any other redundancy relationship.

##### Procedure

1. Select the security module that will be the active security module in normal operation (primary module).
2. In the local security settings, select the entry "Router and firewall redundancy".
3. Select the "Router and firewall redundancy" check box.
4. In the "Secondary module" drop-down list, select the security module that will be the passive security module in normal operation.

Result: You have created a redundancy relationship between the security modules.

#### Configuring redundancy relationships

##### How to access this function

1. Select the primary module of the redundancy relationship.
2. In the local security settings, select the entry "Router and firewall redundancy".

##### Configuring network parameters of the redundancy relationship

| Configurable parameter | Meaning |
| --- | --- |
| IP address | IP address of the virtual external or internal interface of the redundancy relationship. The IP address must be located in the external or internal subnet of the primary module. |
| Subnet mask | Subnet mask of the virtual external or internal interface of the redundancy relationship |
| MAC address (adaptable only for SCALANCE S623/S627-2M as of V4.0.1) | MAC address of the virtual external or internal interface of the redundancy relationship |

For general information on configuring network parameters, refer to the following section:  
[Configuring IP address parameters](#configuring-ip-address-parameters)

##### Configuring the firewall

IP packet filter rules for redundancy relationships are configured on the primary module. The communications directions "From external to internal" and "From internal to external" are available.

For general information on configuring IP packet filter rules in advanced firewall mode, refer to the following section:  
[Defining IP packet filter rules](#defining-ip-packet-filter-rules)

##### Configuring address translation with NAT/NAPT

Address translation with NAT/NAPT for the redundancy relationship is configured on the primary module. For redundancy relationships, only Source NAT and NAPT can be configured. With Source NAT, source IP addresses in the internal subnet can only be replaced with the virtual external IP address of the redundancy relationship. No alias IP addresses can be registered on the external interface of the redundancy relationship. With NAPT, only the "External to internal" address translation direction can be configured.

For general information on configuring address translations with NAT/NAPT, refer to the following section:  
[Overview of NAT/NAPT](#overview-of-natnapt)

##### Configuring routing

Routes for the redundancy relationship are configured on the primary module. Standard routers must be specified in the "External interface [P1] red" or "Internal interface [P2] green" entry and must be identical per interface.

For general information on configuring routing, refer to the following section:  
[Specifying routes](#specifying-routes)

### Online functions - diagnostics and logging

This section contains information on the following topics:

- [Overview of the individual interfaces - "Interface settings" entry](#overview-of-the-individual-interfaces---interface-settings-entry-1)
- [Overview of the Dyn. DNS settings - "Dynamic DNS" entry](#overview-of-the-dyn-dns-settings---dynamic-dns-entry-1)
- [Display of the ARP table - "ARP table" entry](#display-of-the-arp-table---arp-table-entry-1)
- [Users logged in to the Web page - "Logged in users" entry](#users-logged-in-to-the-web-page---logged-in-users-entry-1)
- [Display of the firewall blacklist - "Firewall blacklist" entry](#display-of-the-firewall-blacklist---firewall-blacklist-entry-1)
- [Setting the date and time - "Date and time" entry](#setting-the-date-and-time---date-and-time-entry-1)
- [Diagnostics in ghost mode - "Ghost mode" entry](#diagnostics-in-ghost-mode---ghost-mode-entry-1)

#### Overview of the individual interfaces - "Interface settings" entry

##### Meaning

Online diagnostics: "Interface settings" entry

| System and status functions | Meaning |
| --- | --- |
| Interfaces | Table above: General overview of the interfaces of the security module.    Table below: Information on the interface operated via PPPoE.  - Status: Indicates whether or not a connection was established to the Internet Service Provider (ISP). - Current IP address: Current IP address of the interface - Gateway: IP address of the gateway - Primary dynamic DNS service: IP address of the primary dynamic DNS service - Secondary dynamic DNS service: IP address of the secondary dynamic DNS service - Error code (numeric): Error information if no connection could be established to the ISP. |
| CARP (only SCALANCE S623/S627-2M as of V4) | - CARP interface: Display of the virtual CARP interface - Physical interface: Physical interface on which the virtual CARP interface is operated (external / internal). - Status: Displays which of the modules of the redundancy relationship is active. - MAC address: MAC address of the virtual CARP interface - Preferred: Displays which of the modules of the redundancy relationship is configured as the primary module. |
| Media redundancy (SCALANCE S627-2M only) | - Interface: Interface connected to the MRP ring. - Protocol: Protocol used (MRP) - Ring port 1: Name of the first media module port of the interface connected to the MRP ring. - Ring port 2: Name of the second media module port of the interface connected to the MRP ring. - Domain name: Name of the MRP domain. - Discrepancy: Display whether the domain of the client differs from that of the redundancy manager. - Domain UUID: UUID of the MRP domain. |
| Media modules (SCALANCE S627-2M only) | - Port: Port ID(s) of the media module port(s) - Name: Name of the media module - MLFB: MLFB of the media module - Revision: Version of the media module - Discrepancy: Displays whether there are differences between the configuration data in STEP 7 and the media modules. |

#### Overview of the Dyn. DNS settings - "Dynamic DNS" entry

##### Meaning

Online diagnostics: "Dynamic DNS"

| System and status functions | Meaning |
| --- | --- |
| Client status | Indicates whether or not a connection was established to a dyn. DNS server. |
| Current IP address | WAN IP address via which the security module can currently be reached. |
| Defined IP address | IP address currently assigned to the FQDN. |
| Current time | The current time-of-day. |
| Force update | The security module obtains the current IP address of its Internet access and sends an update query to the configured update server(s). This publishes the current IP address on the Internet. The status is displayed in the primary or secondary dynamic DNS service fields. This means, for example that it is possible to check whether configured data such as the user name and password of the dynamic DNS account are correct. |
| Cancel suspension | Cancels the suspension (blocking of IP address updates from the dynamic DNS provider on the security module), for example after the dynamic DNS provider password has been corrected or an error has been eliminated. |
| **Primary and secondary dynamic DNS service** |  |
| FQDN | Fully Qualified Domain Name registered with the provider. |
| Server IP Address | IP address of the update server used. |
| Successful update | Successful update in the dynamic DNS update service. |
| Last update attempt | Last update attempt for DynDNS update service. |
| Last failed update | Last update error in the dynamic DNS update service. |
| Error code | Error status of the last unsuccessful update attempt during a dynamic DNS update. |

##### What is the meaning of the messages?

The messages of the last DDNS update attempt have the following meaning:

| Message | Meaning |
| --- | --- |
| **Success** |  |
| DDNS_OK | The update query was successful. |
| **Connection-related status messages** |  |
| DDNS_E_CON_UDP_SRV_RESOLV_ERR | DNS name of the update server unknown, FQDN cannot be resolved using the known DNS server. |
| DDNS_E_CON_UDP_SRV_UNREACHABLE | Update server unreachable ("Timeout"). |
| **Security-related status messages (errors)** |  |
| DDNS_E_CERT_SUBJECT_INVALID | The common name of the subject in the certificate does not match the domain name of the update server or its IP address. |
| DDNS_E_CERT_UNABLE_TO_GET_ISSUER_CERT | Issuer certificate not found.  The certificate chain could not be followed back to the root CA because an issuer certificate was not found. The trust chain is incomplete. |
| DDNS_E_CERT_SIGNATURE_INVALID | The signature of a certificate could not be read or is invalid. |
| DDNS_E_CERT_NO_TRUST | A certificate in the trust chain is invalid, in other words:  - Not yet valid or ready expired - V3 extensions invalid - Critical V3 extension is not supported |
| DDNS_E_CERT_DEPTH_ZERO_SELFSIGNED_CERT | The update server has supplied a self-signed certificate and the certificate is not in the certificate store for trustworthy root CA certificates. |
| DDNS_E_CERT_SELF_SIGNED_CERT_IN_CHAIN | The certificate chain could be established using non trustworthy certificates but no suitable root CA certificate was found in the certificate store for trustworthy certificates. |
| DDNS_E_CERT_CHAIN_TOO_LONG | The certificate chain exceeds the maximum supported verification depth. |
| DDNS_E_CERT_INVALID_CA | A CA certificate is invalid, in other words expired, not yet valid or the V3 extensions are not suitable for the intended purpose (for example CA not set to TRUE for CA certificates). |
| DDNS_E_CERT_KEYUSAGE_UNSUITED | The V3 extensions key usage or extended key usage set in a certificate of the trust chain are not suitable for the use of the certificate. |
| DDNS_E_CERT_EXTENSION_UNSUPPORTED | A certificate in the trust chain used an extension marked as critical that is not supported. |
| **Agent-related status messages (errors)** |  |
| DDNS_E_AGT_BAD_AGENT | - The update request does not correspond to the structure required by cRSP, for example URL parameters missing. - The update request was sent to an illegal URL on the update server. - The configured update string contains errors. |
|  |  |

#### Display of the ARP table - "ARP table" entry

##### Meaning

Display of the ARP table of the security module.

Online diagnostics: "ARP table" tab

| System and status functions | Meaning |
| --- | --- |
| ARP table | Display of the static (proxy ARP) and dynamic entries of the ARP table on the security module. The "Publication type" tab specifies whether the entry is configured statically or learnt. |

#### Users logged in to the Web page - "Logged in users" entry

##### Meaning

Shows the users logged in to the Internet page for user-specific IP rule sets.

| System and status functions | Meaning |
| --- | --- |
| User name | Name of the logged on user. |
| Source IP address | IP address with which the user logged on. |
| Time remaining | Remaining time before the user is automatically logged off. |
| Maximum time of the session | Configured total time of the session. |
| Log off | The selected user is logged off. |

#### Display of the firewall blacklist - "Firewall blacklist" entry

##### Meaning

Displays the IP addresses of nodes that have exceeded the permitted number of connections and firewall statuses per time unit. These nodes are entered in the IP blacklist of the firewall.

The number of connections and firewall statuses per time unit is only limited if the "Use extended status options" check box is selected in the "Standard rules for IP services" entry in the local security settings.

If you click the "Delete all" button, the displayed IP addresses are removed from the firewall blacklist of the security module. The IP addresses are also no longer displayed.

#### Setting the date and time - "Date and time" entry

##### How to access this function

1. Select the security module whose time and date you want to check or set.
2. Select the "Online & diagnostics" command from the shortcut menu.
3. In online diagnostics, select the "Functions" > "Date and time" entry.

##### Setting the local time on the security module

In this area, you can read out and set the time and date of the security module. When you click the "Apply" button, the security module is assigned the time and date currently entered in the "Date" and "Time" input boxes.

##### Setting the local time on PC

This area shows the current time and current date of the PC on which STEP 7 is installed. If you click the "Adopt for module" button, the security module is assigned the current time and current date of the PC.

#### Diagnostics in ghost mode - "Ghost mode" entry

##### Module-specific function

This function is available only for SCALANCE S602 as of V3.1.

##### Meaning

Display of address information as well as information on IP address changes of the internal node.

| System and status functions | Meaning |
| --- | --- |
| Status of SCALANCE S602 | Display of the status of the security module in relation to operation in ghost mode. |
| IP address | IP address of the internal node (identical to the external IP address of the security module). |
| Subnet mask | Subnet mask of the security module. |
| MAC address | MAC address of the internal node. |
| Node found on | Displays when the internal node was recognized by the security module or when an IP address change was made on the internal node. |
| Number of IP address changes | Number of IP address changes detected by the security module. |
| IP address | IP address in the external network for which the security module requires route information. |
| Standard router | Standard router for the IP address in the external network. |

### Download functions

This section contains information on the following topics:

- [Downloading a configuration](#downloading-a-configuration)
- [Transferring firmware](#transferring-firmware)

#### Downloading a configuration

##### Downloading the configuration / establishing an online connection

1. From the "PG/PC interface" drop-down list of the "Advanced download" dialog or "Connect online", select the network adapter via which you can reach the module.
2. If the module is in the factory settings status, follow the steps below:

   - From the "Connection to interface/subnet" drop-down list, with which your engineering station is connected and for which the IP address to be assigned is configured in the local security settings.
   - Select the "Display all compatible nodes" from the drop-down list.
   - Click the "Start search" button.
   - Result: The module is displayed in the "Select target device" table with its detected MAC address.
   - Select the module entry in the table and click the "Assign IP address" button.
   - Result: The module is assigned the IP address configured in the local security settings for the selected interface.
3. If the module is not in the factory settings status, follow the steps below:

   - From the "Connection with interface/subnet", select the interface / the FQDN address / WAN address of the module via which your engineering station can reach the module. STEP 7 then uses the address configured in the local security settings for the selected component for access to the module.
   - If you select the option "Display devices with the same address" from the drop down list, the nodes will be displayed whose address matches the selected component. If you select the entry "Show all compatible devices", the devices whose module type matches that of the selected module are shown.
   - Click the "Start search" button.
   - Result: The "Address" column of the "Compatible devices in the target subnet" displays the detected IP address / FQDN address of the module.
   - Select the address entry in the table and click the "Load" or "Go online" button.

Ideally, you should configure the modules of a group via the common external network of these modules (interface X1). If the engineering station is located in an internal network, you will need to enable the IP addresses of the other modules of the group explicitly in the firewall of this SCALANCE S and configure this module first.

> **Note**
>
> **Downloading the configuration when operating in ghost mode (only SCALANCE S602 as of V3.1)**
>
> When you operate the security module in ghost mode, the external interface of the security module takes over the IP address of the internal node at runtime. Before you can download a new configuration via the external interface to the security module, you need to specify the IP address for downloading a configuration that the security module obtained from the internal node during runtime.  
> To find out the current IP address of the security module, you can search for reachable nodes in STEP 7 with the menu command "Online" > "Accessible devices".

> **Note**
>
> **Loading a configuration on security modules of a redundancy relationship (only SCALANCE S623/S627-2M as of V4)**
>
> The properties of a redundancy relationship configured for the primary module must be loaded both on the primary module and on the secondary module. To load the configuration, the physical IP address via which your engineering station can reach the security module must be used. The virtual IP addresses of the redundancy relationship cannot be used for loading.

##### Specifying a different address

In the "Compatible devices in target subnet" dialog area, you have the option of specifying an IP address / an FQDN address that differs from the IP address / FQDN address in the local security settings. To do this, enter the IP address / FQDN address of the module in the editable cell in the "Address" table column. After loading, the security module is reachable via the IP address / the FQDN address from the local security settings.

##### Firmware version

The configuration of a SCALANCE S module can also be downloaded to a SCALANCE S module whose firmware version is higher than the firmware version of the SCALANCE S module in STEP 7.

##### Operating mode

Configurations can be downloaded while the SCALANCE S modules are operating. Restart the SCALANCE S module to activate your configuration changes.

> **Note**
>
> **Special characteristics**
>
> - As long as a module has not yet set IP parameters (in other words, prior to the first configuration), there must be no router between the module and the configuration computer.
> - If you swap a PC from the internal to the external interface of the SCALANCE S, access from this PC to the SCALANCE S is blocked for approximately 20 minutes.

##### Configuration status

Prior to each download, the existing configuration on the security module is checked and compared with the configuration to be downloaded from the STEP 7 project. If the configuration of the module originates from the STEP 7 project currently to be downloaded and there are differences between these configurations, it is possible to download only files with differences between the module and project configuration to the security module. In some situations, this can speed up the download.

#### Transferring firmware

##### This needs to be taken into consideration before transferring new firmware

To transfer new firmware to a security module, the following conditions must be met:

- You have the rights required to transfer firmware; refer to section   
  [Special features of user management for security functions](#special-features-of-user-management-for-security-functions).
- The security module is configured with an IP address.

##### The transfer is secure

The firmware is transferred over a secure connection and can therefore also be transferred from the unprotected network.

The firmware itself is signed and encrypted. This ensures that only authentic firmware can be downloaded to the SCALANCE S module.

##### Restart necessary following transfer

Newly downloaded firmware only becomes active after the SCALANCE S module has been restarted. If the transfer is disturbed and aborted, the module starts up again with the old firmware version.

## Security for S7-300 /S7-400 / PC CPs

This section contains information on the following topics:

- [Setting up a firewall](#setting-up-a-firewall-2)
- [Activating Web server on security module](#activating-web-server-on-security-module)
- [IPsec tunnel: Creating and assigning groups](#ipsec-tunnel-creating-and-assigning-groups-1)
- [Online functions - Debug / Diagnostics and Logging](#online-functions---debug-diagnostics-and-logging)

### Setting up a firewall

This section contains information on the following topics:

- [Local firewall rules for S7-300 /S7-400 / PC CPs](#local-firewall-rules-for-s7-300-s7-400-pc-cps)
- [IP packet filter directions S7-300-/S7-400-/PC-CPs](#ip-packet-filter-directions-s7-300-s7-400-pc-cps)
- [MAC packet filter directions S7-300-/S7-400-/PC-CPs](#mac-packet-filter-directions-s7-300-s7-400-pc-cps)
- [Configuring the access list](#configuring-the-access-list)
- [Connection-related automatic firewall rules](#connection-related-automatic-firewall-rules)

#### Local firewall rules for S7-300 /S7-400 / PC CPs

This section contains information on the following topics:

- [Overview S7-300 CPs / S7-400 CPs /PC CPs](#overview-s7-300-cps-s7-400-cps-pc-cps)
- [Configuring a firewall with predefined firewall rules - CP 343-1 Adv. / 443-1 Adv.](#configuring-a-firewall-with-predefined-firewall-rules---cp-343-1-adv-443-1-adv)
- [Configuring a firewall with predefined firewall rules - CP 1628](#configuring-a-firewall-with-predefined-firewall-rules---cp-1628)

##### Overview S7-300 CPs / S7-400 CPs /PC CPs

###### Enabling packet filter rules

If you enable the security function for the CPs in the local security settings, initially all access to and via the CP is permitted. To enable individual packet filter rules, select the "Activate firewall" check box. Then enable the required services. Firewall rules created automatically due to a connection configuration have priority over rules set manually.

> **Note**
>
> **Detailed firewall settings in advanced firewall mode**
>
> In advanced firewall mode, you can restrict firewall rules to individual nodes. To change to advanced firewall mode, select the "Activate firewall in advanced mode" check box.

###### Firewall configuration with VPN

If the security module is added to a VPN group, the firewall is enabled by default. In addition, the "Tunnel communication only" check box is enabled. This means that only encrypted IPsec data transfer is permitted via the external interface. External data traffic is blocked.

If you deselect the check box, tunneled communication and also the types of communication selected in the other boxes are permitted.

###### Updating connection rules

Changes to the connection configuration of CPs also change the connection-related firewall rules. To display the modified firewall rules, click the "Update connection rules" button. The modified firewall rules are then displayed in advanced firewall mode.

##### Configuring a firewall with predefined firewall rules - CP 343-1 Adv. / 443-1 Adv.

This section contains information on the following topics:

- [Configuring a firewall with predefined IP rules - CP 343-1 Adv. / 443-1 Adv.](#configuring-a-firewall-with-predefined-ip-rules---cp-343-1-adv-443-1-adv)
- [Configuring a firewall with predefined MAC rules - CP 343-1 Adv. / 443-1 Adv.](#configuring-a-firewall-with-predefined-mac-rules---cp-343-1-adv-443-1-adv)

###### Configuring a firewall with predefined IP rules - CP 343-1 Adv. / 443-1 Adv.

###### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "Firewall" > "Predefined IP rules".

All tables
Available services and directions
Logging

Available services and directions

| Service | From station/internal to external | External to internal | From external to station | Enabled ports | Meaning |
| --- | --- | --- | --- | --- | --- |
| Allow  IP communication | **x** | **x** | **x** | All | IP traffic for the selected communication directions is allowed. |
| Allow S7 protocol | **x** | **x** | **x** | TCP port 102 | Communication of the nodes using the S7 protocol is allowed. |
| Allow FTP/FTPS (explicit mode) | **x** | **x** | **x** | TCP port 20  TCP port 21 | For file management and file access between server and client. |
| Allow HTTP | **x** | **x** | **x** | TCP port 80 | For communication with a Web server. |
| Allow HTTPS | **x** | **x** | **x** | TCP port 443 | For secure communication with a Web server, for example, for Web diagnostics. |
| Allow DNS | **x** | **x** | - | TCP port 53   UDP port 53 | Communication connection to a DNS server is allowed. |
| Allow SNMP | **x** | **x** | **x** | TCP port 161/162   UDP port 161/162 | For monitoring nodes capable of SNMP. |
| Allow SMTP | **x** | **x** | - | TCP port 25 | For sending e-mails via an SMTP server. |
| Allow NTP | **x** | **x** | - | UDP port 123 | For synchronization of the time of day. |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| IP log settings |  | Action | From | To |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All IP packets transferred via the tunnel are logged. | Accept | Station | Tunnel |
| Accept | Tunnel | Station |  |  |
| Log blocked incoming packets | All incoming IP packets that are discarded are logged. | Drop | External | Station |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings that are made in "Predefined IP rules" and "Predefined MAC rules" have no effect on firewall rules that were automatically created as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

###### Configuring a firewall with predefined MAC rules - CP 343-1 Adv. / 443-1 Adv.

###### How to access this function

1. Select the module to be edited.
2. Select the entry "Firewall" > "Predefined MAC rules".

Available services and directions

| Service | From station to external | From external to station | Meaning |
| --- | --- | --- | --- |
| Allow MAC communication | **x** | **x** | The MAC traffic from station to external and vice versa is allowed. |
| Allow ISO protocol | **x** | **x** | The ISO traffic from station to external and vice versa is allowed. |

Logging

| Option | Action when activated |  | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- | --- |
| MAC log settings |  |  | Action | From | To |
| Log tunneled packets |  | Only active if the security module is a member of a VPN group. All MAC packets transferred via the tunnel are logged. | Accept | Station | Tunnel |
| Accept | Tunnel | Station |  |  |  |
| Log blocked incoming packets |  | All incoming MAC packets that are discarded are logged. | Drop | External | Station |
| Log blocked outgoing packets |  | All outgoing MAC packets that are discarded are logged. | Drop | Station | External |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings that are made in "Predefined IP rules" and "Predefined MAC rules" have no effect on firewall rules that were automatically created as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

##### Configuring a firewall with predefined firewall rules - CP 1628

This section contains information on the following topics:

- [Configuring a firewall with predefined IP rules - CP 1628](#configuring-a-firewall-with-predefined-ip-rules---cp-1628)
- [Configuring a firewall with predefined MAC rules - CP 1628](#configuring-a-firewall-with-predefined-mac-rules---cp-1628)

###### Configuring a firewall with predefined IP rules - CP 1628

###### How to access this function

1. Select the module to be edited.
2. Select the "Security" > "Firewall" > "Predefined IP rules" entry.

All tables
Available services and directions
Logging

Available services and directions

| Service | From external to station | Enabled ports | Meaning |
| --- | --- | --- | --- |
| Allow IP communication | **x** | All | IP traffic from external to station is allowed. |
| Allow S7 protocol | **x** | TCP port 102 | Communication of the nodes using the S7 protocol is allowed. |
| Allow FTP/FTPS (explicit mode) | **x** | TCP port 20  TCP port 21 | For file management and file access between server and client. |
| Allow HTTP | **x** | TCP port 80 | For communication with a Web server. |
| Allow HTTPS | **x** | TCP port 443 | For secure communication with a Web server, for example, for Web diagnostics. |
| Allow DNS | **x** | TCP port 53  UDP port 53 | Communication connection to a DNS server is allowed. |
| Allow SNMP | **x** | TCP port 161/162  UDP port 161/162 | For monitoring nodes capable of SNMP. |
| Allow SMTP | **x** | TCP port 25 | For sending e-mails via an SMTP server. |
| Allow NTP | **x** | UDP port 123 | For synchronization of the time of day. |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| **IP log settings** |  | **Action** | **From** | **To** |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All IP packets transferred via the tunnel are logged. | Accept | Station | Tunnel |
| Accept | Tunnel | Station |  |  |
| Log blocked incoming packets | All incoming IP packets that are discarded are logged. | Drop | External | Station |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings that are made in "Predefined IP rules" and "Predefined MAC rules" have no effect on firewall rules that were automatically created as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

###### Configuring a firewall with predefined MAC rules - CP 1628

###### How to access this function

1. Select the module to be edited.
2. Select the entry "Security" > "Firewall" > "MAC rules".

All tables
Available services and directions

Available services and directions

| Service | From station to external | From external to station | Meaning |
| --- | --- | --- | --- |
| Allow MAC level communication | **x** | **x** | The MAC traffic from external to the station and vice versa is allowed. |
| Allow ISO communication | **x** | **x** | ISO traffic from external to the station and vice versa is allowed. |
| Allow SiClock | **x** | **x** | SiClock time-of-day frames from external to the station and vice versa are allowed. |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| **MAC log settings** |  | **Action** | **From** | **To** |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All MAC packets transferred via the tunnel are logged. | Accept | Station | Tunnel |
| Accept | Tunnel | Station |  |  |
| Log blocked incoming packets | All incoming MAC packets that are discarded are logged. | Drop | External | Station |
| Log blocked outgoing packets | All outgoing MAC packets that are discarded are logged. | Drop | Station | External |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings that are made in "Predefined IP rules" and "Predefined MAC rules" have no effect on firewall rules that were automatically created as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

#### IP packet filter directions S7-300-/S7-400-/PC-CPs

##### Meaning

Possible selections for the communication directions "From" and "To" in the IP rules of the advanced firewall mode.

##### The following directions are available

| Available options / ranges of values |  | Security module |  | Meaning |
| --- | --- | --- | --- | --- |
| **From** | **To** | **CP 343-1 Adv. / 443-1 Adv.** | **CP 1628** |  |
| Internal | Station | **x** | - | Access from the internal network to the station. |
| Any | **x** | - | Access from internal to the external network, VPN tunnel partner and the station. |  |
| External | Station | **x** | **x** | Access from the external network to the station. |
| Any | **x** | - | Access from external to the internal network and the station. |  |
| Station | Internal | **x** | - | Access from the station to the internal network. |
| External | **x** | **x** | Access from the station to the external network. |  |
| Tunnel | **x** | **x** | Access from the station to the VPN tunnel partner. |  |
| Tunnel | Station | **x** | **x** | Access via the VPN tunnel partner to the station. |
| Any | **x** | - | Access from VPN tunnel partners to the internal network and the station. |  |
| Any | External | **x** | - | Access from the internal network and the station to the external network. |

#### MAC packet filter directions S7-300-/S7-400-/PC-CPs

##### Meaning

Possible selections for the communication directions "From" and "To" in the MAC rules of the advanced firewall mode.

##### The following directions are available

| Available options / ranges of values |  | Security module |  | Meaning |
| --- | --- | --- | --- | --- |
| **From** | **To** | **CP 343-1 Adv. / 443-1 Adv.** | **CP 1628** |  |
| External | Station | **x** | **x** | Access from the external network to the station. |
| Station | External | **x** | **x** | Access from the station to the external network. |
| Tunnel | **x** | **x** | Access from the station to the VPN tunnel partner. |  |
| Tunnel | Station | **x** | **x** | Access via the VPN tunnel partner to the station. |

#### Configuring the access list

##### Module-specific function

This function is not available for the CP 1628.

##### Meaning

You set access protection for certain IP addresses using the IP access lists. List entries that have already been created and the corresponding rights are displayed in the local settings of the CP in the entry "Firewall" > "IP rules" (advanced firewall mode).

> **Note**
>
> **Changed behavior after activation of security**
>
> - Once you have activated the security function for a CP, access protection will only apply to the external interface. You can apply access protection to the internal interface as well, by configuring suitable firewall rules in advanced firewall mode.
> - The CP also responds to ARP requests from IP addresses that have not been released (layer 2).
> - If the IP access list of a CP contains no entries and you activate security for the CP, the firewall will be activated and prevent access to the CP from external locations. Configure the corresponding firewall rules in advanced firewall mode so that the CP can be reached.

##### Effect of IP access list entries at activation of security

If security is enabled in the local settings of a CP, the corresponding rules are created in the advanced firewall mode. A firewall rule "Accept" > "External" > "Station" is created for an IP address you specified in the address list. The IP address from the IP access list is used accordingly as source IP address. IP addresses from a defined IP address range are also integrated into corresponding firewall rules.

##### Requirements for editing

Before you can edit created firewall rules, the following condition must be met:

- for editing using STEP 7: "Configure security" configuration right
- for editing using a Web server: Module right "Web: Expand IP access control list"

The requirements for editing the IP access lists outside the local security settings are described in the sections on the specific CPs.

#### Connection-related automatic firewall rules

##### Meaning

For connections that were configured using CPs, STEP 7 automatically creates firewall rules that allow communication with the partner of the CP in the specified direction (CP active/passive). The connection establishment directions are taken into account. To display these firewall rules, if the advanced firewall mode is enabled, the "Update connection rules" button needs to be clicked. The firewall rules are then displayed in advanced firewall mode.

> **Note**
>
> **Releasing UDP multicast connections manually**
>
> No automatic firewall rules are created for UDP multicast connections. To enable the connections, add the relevant firewall rules manually in advanced firewall mode.

Depending on how the connection establishment is configured, the following level 3 firewall rules are created. If the security module is in a VPN group, the direction "External" changes to "Tunnel". This applies only to CPs that support VPN.

The IP address of the connection partner is entered in the "Source IP address" or "Destination IP address" column of these firewall rules.

| CP->external | Action | From | To |
| --- | --- | --- | --- |
| active | Accept | Station | External |
| Drop | External | Station |  |
| passive | Drop | Station | External |
| Accept | External | Station |  |
| active and passive | Accept | External | Station |
| Accept | Station | External |  |

| CP->internal | Action | From | To |
| --- | --- | --- | --- |
| active | Accept | Station | Internal |
| Drop | Internal | Station |  |
| passive | Drop | Station | Internal |
| Accept | Internal | Station |  |
| active and passive | Accept | Internal | Station |
| Accept | Station | Internal |  |

For level 2 connections, "Accept" rules are created for both directions. If the security module is in a VPN group, the direction "External" changes to "Tunnel".

The MAC address of the connection partner is entered in the "Source MAC address" or "Destination MAC address" column of these firewall rules.

| CP->external | Action | From | To |
| --- | --- | --- | --- |
| active, passive, active and passive | Accept | Station | External |
| Accept | External | Station |  |

> **Note**
>
> **Changing the connection configuration**
>
> Changes to the connection configuration of CPs also change the connection-related firewall rules. To display the modified firewall rules, click the "Update connection rules" button.

##### Conventions for automatically created firewall rules

- Priority

  The rules have highest priority and are therefore inserted at the top in the local rule list.
- Deleting rules

  The rules cannot be deleted. Logging can be enabled and services can be assigned. You can also insert a transmission speed and a comment.
- Changing the action

  If you set the action from "Accept" to "Drop" or vice versa, this is overwritten again during renewed system synchronization. If you want to retain your changes, select "Accept*" or "Drop*" as action. In this case, only the IP address is synchronized and the action and direction remain as set. Settings for logging, service, transmission speed and comment are also retained after a renewed system synchronization even without changing the action to "Accept*" or "Drop*". If the configured connection is deleted, the corresponding rules are removed from the list.

##### Security module in VPN group

As default, the "Tunnel communication only" check box is enabled. If you deselect the check box, in addition to tunnel communication between tunnel partners, communication is also possible with network nodes to which there is no tunnel.

- Communication is untunneled if the partner address belongs to a station known in STEP 7 for which no VPN tunnel is configured.
- Communication is through the tunnel if the partner address is a VPN endpoint.
- If it is not clear whether connection should bypass or run through the VPN tunnel, the connection is assigned to the VPN tunnel and a message to this effect is displayed. The assignment can be adapted in advanced firewall mode, for example, by changing the "From" direction "Tunnel" to "External". To avoid this change being overwritten by the next system synchronization, the "Accept*" or "Drop*" action must be selected.

  > **Note**
  >
  > If you want to ensure that only communication through the tunnel is possible, you will need to create suitable firewall rules in advanced firewall mode, for example, for internal nodes or NDIS addresses.
  >
  > To allow only tunneled communication for a CP, add a rule with the following settings:
  >
  > - "Action": "Drop"
  > - "From": "Any"
  > - "To": "External"
  >
  > For the CP 1628, add a rule with the following settings:
  >
  > - "Action": "Drop"
  > - "From": "Station"
  > - "To": "External"
  >
  > In addition to this, you need to remove existing firewall rules that allow untunneled communication.

### Activating Web server on security module

#### Module-specific function

This function is only available for CP 343-1 Adv. / 443-1 Adv. and CP 443-1 OPC UA:

#### Meaning

After activating the Web server, you have access to the Web pages of the module. In the local security settings, you can restrict access to these Web pages for the CP 343-1 Adv. / 443-1 Adv.to the HTTPS protocol. This access is controlled using the "Allow access only using HTTPS" check box. In addition, you must configure the firewall accordingly. For the CP 443-1 OPC UA access to the Web server is only permitted using HTTPS.

### IPsec tunnel: Creating and assigning groups

This section contains information on the following topics:

- [Configuring internal network nodes - "Nodes" entry](#configuring-internal-network-nodes---nodes-entry)

#### Configuring internal network nodes - "Nodes" entry

This section contains information on the following topics:

- [Allow access to S7-300 / S7-400 CPs for VPN connection partners](#allow-access-to-s7-300-s7-400-cps-for-vpn-connection-partners-1)
- [Configuring NDIS nodes manually for PC CPs that can be reached through the tunnel](#configuring-ndis-nodes-manually-for-pc-cps-that-can-be-reached-through-the-tunnel)

##### Allow access to S7-300 / S7-400 CPs for VPN connection partners

###### Possible selections

Decide whether or not the VPN connection partner can have access to the CP and/or the internal subnet of the CP in routing mode (SCALANCE S / M).

###### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "Node".
3. Configure access for the VPN connection partner of the CP in routing mode (SCALANCE S / M):

   - Allow connection to the CP (Gbit interface)
   - Allow connection to the internal subnet (PROFINET subnet)

##### Configuring NDIS nodes manually for PC CPs that can be reached through the tunnel

###### Configuring NDIS nodes that can be reached through the tunnel

The internal nodes are learned and assigned to the routes dynamically. This concerns the NDIS IP addresses of the Windows PC.

###### Follow the steps below

1. Select the module to be edited.
2. In the local security settings, select the entry "Nodes" > "NDIS nodes reachable via tunnel".
3. Enter the NDIS IP addresses.

### Online functions - Debug / Diagnostics and Logging

This section contains information on the following topics:

- [Updated firewall rules - "Dynamically updated firewall rules" entry](#updated-firewall-rules---dynamically-updated-firewall-rules-entry-1)

#### Updated firewall rules - "Dynamically updated firewall rules" entry

##### Module-specific function

This function is only available for CP 343-1 Adv. / 443-1 Adv.

##### Meaning

Display of the IP addresses or IP address ranges that were enabled dynamically using HTTP or HTTPS, or loaded by a user. The rights assigned for accessing the S7 CP are displayed for the enabled IP addresses. An update of the IP addresses in this tab can only be triggered by the following events:

- Extension/modification of the IP access control list
- Update of firewall rules
- Dynamic extensions transmitted to the CP at runtime, for example, PROFINET IO devices

Since only the dynamically updated firewall rules are displayed here, you also need to take into account the firewall rules that were configured offline and downloaded to the station for a full picture of the current firewall status of the module.

## Security for S7-1200-/S7-1500-CPs

This section contains information on the following topics:

- [Setting up a firewall](#setting-up-a-firewall-3)
- [Configuring S7 subnets reachable via the backplane bus for CP 154x-1](#configuring-s7-subnets-reachable-via-the-backplane-bus-for-cp-154x-1)
- [Automatic OpenVPN configuration via SINEMA Remote Connect Server:](#automatic-openvpn-configuration-via-sinema-remote-connect-server)
- [Network authentication for CP1543-1/CP1545/1](#network-authentication-for-cp1543-1cp15451)
- [CP 1545-1 certificates](#cp-1545-1-certificates)

### Setting up a firewall

This section contains information on the following topics:

- [Local firewall rules for S7-1200 / S7-1500 CPs](#local-firewall-rules-for-s7-1200-s7-1500-cps)
- [IP packet filter directions S7-1200 / S7-1500 CPs](#ip-packet-filter-directions-s7-1200-s7-1500-cps)
- [MAC packet filter directions S7-1200 / S7-1500 CPs](#mac-packet-filter-directions-s7-1200-s7-1500-cps)
- [Connection-related automatic firewall rules](#connection-related-automatic-firewall-rules-1)

#### Local firewall rules for S7-1200 / S7-1500 CPs

This section contains information on the following topics:

- [Overview of the local firewall rules for S7-1200 / S7-1500 CPs](#overview-of-the-local-firewall-rules-for-s7-1200-s7-1500-cps)
- [Configuring a firewall with predefined firewall rules - CP 1543-1 / CP 1543SP-1 / CP 1545-1](#configuring-a-firewall-with-predefined-firewall-rules---cp-1543-1-cp-1543sp-1-cp-1545-1)
- [Configuring a firewall with predefined firewall rules - S7-1200 CPs](#configuring-a-firewall-with-predefined-firewall-rules---s7-1200-cps)

##### Overview of the local firewall rules for S7-1200 / S7-1500 CPs

###### Enabling packet filter rules

If you enable the security function for the CPs in the local security settings, initially all access to and via the CP is permitted.

To enable individual packet filter rules, select the "Activate firewall" check box. Then enable the required services. Firewall rules created automatically due to a connection configuration have priority over rules set manually.

> **Note**
>
> **IPv4 packets V2.2 and higher that are not detected**
>
> IP packets that are forwarded directly from the CP to the PLC are not detected by the firewall. If you use the virtual interface W1, e.g. for OPC UA, you need to manually allow the desired services in the firewall of the CP.

> **Note**
>
> **Detailed firewall settings in advanced firewall mode**
>
> In advanced firewall mode, you can restrict firewall rules to individual nodes. To change to advanced firewall mode, select the "Activate firewall in advanced mode" check box.

###### Updating connection rules

Changes to the connection configuration of CPs also change the connection-related firewall rules. To display the modified firewall rules, click the "Update connection rules" button. The modified firewall rules are then displayed in advanced firewall mode.

##### Configuring a firewall with predefined firewall rules - CP 1543-1 / CP 1543SP-1 / CP 1545-1

This section contains information on the following topics:

- [Configuring a firewall using predefined IP rules](#configuring-a-firewall-using-predefined-ip-rules)
- [Configuring a firewall using predefined IPv6 rules](#configuring-a-firewall-using-predefined-ipv6-rules)
- [Configuring a firewall with predefined MAC rules](#configuring-a-firewall-with-predefined-mac-rules-1)

###### Configuring a firewall using predefined IP rules

###### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "Firewall" > "Predefined IP rules".

Available services and directions

| Service | From external to station | Enabled ports | Meaning |
| --- | --- | --- | --- |
| Allow IP communication | **x** | All | IP traffic from external to station is allowed. |
| Allow S7 protocol | **x** | TCP port 102 | Communication of the nodes using the S7 protocol is allowed. |
| Allow FTP/FTPS* (explicit mode) | **x** | TCP port 20  TCP port 21 | For file management and file access between server and client. |
| Allow HTTP | **x** | TCP port 80 | For communication with a Web server. |
| Allow HTTPS | **x** | TCP port 443 | For secure communication with a Web server, for example, for Web diagnostics. |
| Allow SNMP | **x** | TCP port 161/162   UDP port 161/162 | For monitoring nodes capable of SNMP. |
| Allow security diagnostics | **x** | TCP port 8448 | Allow security diagnostics. |
| *not available for CP 1543SP-1 |  |  |  |

From external to CPU via W1 virtual interface

| Service | Enabled ports | Meaning |
| --- | --- | --- |
| Allow IP communication via W1 virtual interface for OPC UA | TCP port 4840 | Access via the virtual interface of the CP to an OPC UA application in the CPU is allowed. |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| IP log settings |  | Action | From | To |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All IP packets transferred via the tunnel are logged. | Accept | Station | Tunnel |
| Accept | Tunnel | Station |  |  |
| Log blocked incoming packets | All incoming IP packets that are discarded are logged.  Note for CPs that support other directions besides "Station", such as "Backplane bus" or "CPU": no additional firewall rules are created for logging packets in these directions.  Create the relevant rules in advanced firewall mode. | Drop | External | Station |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings that are made in "Predefined IP rules" and "Predefined MAC rules" have no effect on firewall rules that were automatically created as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

###### Configuring a firewall using predefined IPv6 rules

###### Meaning

With the predefined IPv6 rules, you have the option of configuring the firewall for services in which IPv6 is used. By enabling a predefined IPv6 rule in the local security settings of the CP, the system-defined ICMPv6 services that can be seen in the global security functions in the "ICMP" tab in "Firewall" > "Services" > "Define services for IP rules" are also enabled in the firewall.

###### How to access this function

1. Select the module to be edited.
2. Select the "Firewall" > "Predefined IPv6 rules" item in the local security settings.

All tables
Predefined IPv6 rules
Logging

Predefined IPv6 rules

| Service | From external to station | Enabled ports | Meaning |
| --- | --- | --- | --- |
| Allow IP communication | **x** | All | IP traffic from external to station is allowed. |
| Allow S7 protocol | **x** | TCP port 102 | Communication of the nodes using the S7 protocol is allowed. |
| Allow FTP/FTPS* (explicit mode) | **x** | TCP port 20  TCP port 21 | For file management and file access between server and client. |
| Allow SNMP | **x** | TCP port 161/162   UDP port 161/162 | For monitoring nodes capable of SNMP. |
| *not available for CP 1543SP-1 |  |  |  |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| IP log settings |  | Action | From | To |
| Log blocked incoming packets | All incoming IP packets that are discarded are logged. | Drop | External | Station |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings made in "Predefined IPv6 rules" have no effect on firewall rules that were automatically generated as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

###### Configuring a firewall with predefined MAC rules

###### How to access this function

1. Select the module to be edited.
2. Select the entry "Firewall" > "Predefined MAC rules".

Available services and directions

| Service | From station to external | From external to station | Enabled ports | Meaning |
| --- | --- | --- | --- | --- |
| Allow MAC communication | **x** | **x** | - | The MAC traffic from external to the station and vice versa is allowed. |
| Allow ISO protocol* | **x** | **x** | - | ISO traffic from external to the station and vice versa is allowed. |
| Allow DCP | **x** | **x** | - | DCP traffic from external to the station and vice versa is allowed. |
| Allow LLDP* | **x** | **x** | - | LLDP traffic from external to the station and vice versa is allowed. |
| *not available for CP 1543SP-1 |  |  |  |  |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| MAC log settings |  | **Action** | **From** | **To** |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All MAC packets transferred via the tunnel are logged. | Accept | Station | Tunnel |
| Accept | Tunnel | Station |  |  |
| Log blocked incoming packets | All incoming MAC packets that are discarded are logged. | Drop | External | Station |
| Log blocked outgoing packets | All outgoing MAC packets that are discarded are logged. | Drop | Station | External |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings that are made in "Predefined IP rules" and "Predefined MAC rules" have no effect on firewall rules that were automatically created as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

##### Configuring a firewall with predefined firewall rules - S7-1200 CPs

This section contains information on the following topics:

- [Configuring a firewall using predefined IP rules](#configuring-a-firewall-using-predefined-ip-rules-1)
- [Configuring a firewall using predefined IPv6 rules](#configuring-a-firewall-using-predefined-ipv6-rules-1)
- [Configuring a firewall with predefined MAC rules](#configuring-a-firewall-with-predefined-mac-rules-2)

###### Configuring a firewall using predefined IP rules

###### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "Firewall" > "Predefined IP rules".

All tables
Available services and directions
Logging

Available services and directions

| Service | From external to station | Enabled ports | Meaning |
| --- | --- | --- | --- |
| Allow IP communication | **x** | All | IP traffic from external to station is allowed. |
| Allow S7 protocol | **x** | TCP port 102 | Communication of the nodes using the S7 protocol is allowed. |
| Allow HTTP | **x** | TCP port 80 | For communication with a Web server. |
| Allow HTTPS | **x** | TCP port 443 | For secure communication with a Web server, for example, for Web diagnostics. |
| Allow SNMP* | **x** | TCP port 161/162   UDP port 161/162 | For monitoring nodes capable of SNMP. |
| Allow security diagnostics | **x** | TCP port 8448 | Allow security diagnostics. |
| * not available for CP 1243-7 LTE |  |  |  |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| IP log settings |  | Action | From | To |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All IP packets transferred via the tunnel are logged. | Accept | Station | Tunnel |
| Accept | Tunnel | Station |  |  |
| Log blocked incoming packets | All incoming IP packets that are discarded are logged. | Drop | External | Station |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings that are made in "Predefined IP rules" and "Predefined MAC rules" have no effect on firewall rules that were automatically created as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

###### Configuring a firewall using predefined IPv6 rules

###### Meaning

With the predefined IPv6 rules, you have the option of configuring the firewall for services in which IPv6 is used. By enabling a predefined IPv6 rule in the local security settings of an S7-1200 CP capable of IPv6, the system-defined ICMPv6 services that can be seen in the global security functions in the "ICMP" tab in "Firewall" > "Services" > "Define services for IP rules" are also enabled in the firewall.

###### How to access this function

1. Select the module to be edited.
2. Select the "Firewall" > "Predefined IPv6 rules" item in the local security settings.

All tables
Available services and directions
Logging

Available services and directions

| Service | From external to station | Enabled ports | Meaning |
| --- | --- | --- | --- |
| Allow IP communication | **x** | All | IP traffic from external to station is allowed. |
| Allow S7 protocol | **x** | TCP port 102 | Communication of the nodes using the S7 protocol is allowed. |
| Allow SNMP | **x** | TCP port 161/162   UDP port 161/162 | For monitoring nodes capable of SNMP. |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| IP log settings |  | Action | From | To |
| Log blocked incoming packets | All incoming IP packets that are discarded are logged. | Drop | External | Station |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings made in "Predefined IPv6 rules" have no effect on firewall rules that were automatically generated as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

###### Configuring a firewall with predefined MAC rules

###### How to access this function

1. Select the module to be edited.
2. Select the entry "Firewall" > "Predefined MAC rules".

Available services and directions

| Service | From station to external | From external to station | Enabled ports | Meaning |
| --- | --- | --- | --- | --- |
| Allow MAC communication | **x** | **x** | - | The MAC traffic from external to the station and vice versa is allowed. |
| Allow DCP | **x** | **x** | - | DCP traffic from external to the station and vice versa is allowed. |

Logging

| Option | Action when activated | Relevant firewall rule |  |  |
| --- | --- | --- | --- | --- |
| MAC log settings |  | **Action** | **From** | **To** |
| Log tunneled packets | Only active if the security module is a member of a VPN group. All MAC packets transferred via the tunnel are logged. | Accept | Station | Tunnel |
| Accept | Tunnel | Station |  |  |
| Log blocked incoming packets | All incoming MAC packets that are discarded are logged. | Drop | External | Station |
| Log blocked outgoing packets | All outgoing MAC packets that are discarded are logged. | Drop | Station | External |

> **Note**
>
> **Relationship between log settings in default mode and firewall rules**
>
> Log settings that are made in "Predefined IP rules" and "Predefined MAC rules" have no effect on firewall rules that were automatically created as a result of configuring a connection. This means, for example, that tunneled frames belonging to a configured connection cannot be logged. In advanced firewall mode, logging can be extended to the automatically generated firewall rules of connections.

#### IP packet filter directions S7-1200 / S7-1500 CPs

##### Meaning

Possible selections for the communication directions "From" and "To" in the IP rules of the advanced firewall mode.

##### The following directions are available

| Available options / ranges of values |  | Meaning |
| --- | --- | --- |
| **From** | **To** |  |
| External | Station | Access from the external network to the station. |
| Backplane bus* | Access from the external network to the backplane bus of the station. |  |
| Any** | Access from the external for all supported directions. |  |
| CPU*** | Access from the external network to the CPU. |  |
| Station | External | Access from the station to the external network. |
| Tunnel | Access from the station to the VPN tunnel partner. |  |
| Backplane bus* | Access from the station to its backplane bus. |  |
| Any** | Access from the station to all supported directions. |  |
| Tunnel | Station | Access by VPN tunnel partners to the station. |
| Backplane bus* | Access from VPN tunnel partners to the backplane bus of the station. |  |
| Any** | Access from NPN tunnel partners to all supported directions. |  |
| Backplane bus* | External | Access from backplane bus of the station to the external network. |
| Tunnel | Access from backplane bus of the station to NPN tunnel partners. |  |
| Station | Access from the backplane bus to the station. |  |
| Any** | Access from the backplane bus to all supported directions. |  |
| Any** | External | Access from all supported directions to the external network. |
| Tunnel | Access from all supported directions to VPN tunnel partners. |  |
| Station | Access from all supported directions to the station. |  |
| Backplane bus* | Access from all supported directions to the backplane bus of the station. |  |
| CPU*** | External | Access from the CPU to the external network. |
| * only for CP 1543-1 as of V2.1 with IPv4 communication. If the option "IP routing between communications modules" is activated, IP routing via the backplane bus can be allowed / blocked via this direction.  * Only for CP 1543-1 as of V2.1  *** Only for CP 1543-1 as of V3.0 |  |  |

#### MAC packet filter directions S7-1200 / S7-1500 CPs

##### Meaning

Possible selections for the communication directions "From" and "To" in the MAC rules of the advanced firewall mode.

##### The following directions are available

| Available options / ranges of values |  | Meaning |
| --- | --- | --- |
| **From** | **To** |  |
| External | Station | Access from the external network to the station. |
| CPU* | Access from the external network to the CPU. |  |
| Station | External | Access from the station to the external network. |
| Tunnel | Access from the station to the VPN tunnel partner. |  |
| Tunnel | Station | Access by VPN tunnel partners to the station. |
| CPU* | External | Access from the CPU to the external network. |
| * Only for CP 1543-1 as of V3.0 |  |  |

#### Connection-related automatic firewall rules

##### Meaning

For connections that were configured using CPs, STEP 7 automatically creates firewall rules that allow communication with the partner of the CP in the specified direction (CP active/passive). The connection establishment directions are taken into account. To display these firewall rules, if the advanced firewall mode is enabled, the "Update connection rules" button needs to be clicked. The firewall rules are then displayed in advanced firewall mode.

> **Note**
>
> **Enabling UDP multicast and UDP broadcast connections manually**
>
> No automatic firewall rules are created for UDP multicast and UDP broadcast connections. To enable the connections, add the relevant firewall rules manually in advanced firewall mode.

Depending on how the connection establishment is configured, the following level 3 firewall rules are created. If the CP is in a VPN group, the direction "External" changes to "Tunnel".

The IP address of the connection partner is entered in the "Source IP address" or "Destination IP address" column of these firewall rules.

| CP->external | Action | From | To |
| --- | --- | --- | --- |
| active | Drop | External | Station |
| Accept | Station | External |  |
| passive | Drop | Station | External |
| Accept | External | Station |  |
| active and passive | Accept | External | Station |
| Accept | Station | External |  |

For level 2 connections, "Accept" rules are created for both directions. If the CP is in a VPN group, the direction "External" changes to "Tunnel".

The MAC address of the connection partner is entered in the "Source MAC address" or "Destination MAC address" column of these firewall rules.

| CP->external | Action | From | To |
| --- | --- | --- | --- |
| active, passive, active and passive | Accept | Station | External |
| Accept | External | Station |  |

> **Note**
>
> **Changing the connection configuration**
>
> Changes to the connection configuration of CPs also change the connection-related firewall rules. To display the modified firewall rules, click the "Update connection rules" button.

##### Conventions for automatically created firewall rules

- Priority

  The rules have highest priority and are therefore inserted at the top in the local rule list.
- Deleting rules

  The rules cannot be deleted. Logging can be enabled and services can be assigned. You can also insert a transmission speed and a comment.
- Changing the action

  If you change the action from "Accept" to "Drop" or vice versa, this is overwritten again during renewed system synchronization. If you want to retain your changes, select "Accept*" or "Drop*" as action. In this case, only the IP address is synchronized and the action and direction remain as set. Settings for logging, service, transmission speed and comment are also retained after a renewed system synchronization even without changing the action to "Accept*" or "Drop*". If the configured connection is deleted, the corresponding rules are removed from the list.

##### Security module in VPN group

As default, the "Tunnel communication only" check box is enabled. If you deselect the check box, in addition to tunnel communication between tunnel partners, communication is also possible with devices to which there is no tunnel.

- Communication is untunneled if the partner address belongs to a station known in STEP 7 for which no VPN tunnel is configured.
- Communication is through the tunnel if the partner address is a VPN endpoint.

  > **Note**
  >
  > If you want to ensure that only communication through the tunnel is possible, you will need to create suitable firewall rules in advanced firewall mode.
  >
  > To allow only tunneled communication for a CP, add a rule with the following settings:
  >
  > - "Action": "Drop"
  > - "From": "Station"
  > - "To": "External"
  >
  > In addition to this, you need to remove existing firewall rules that allow untunneled communication.

### Configuring S7 subnets reachable via the backplane bus for CP 154x-1

#### Requirement

- The security module CP 1543‑1 as of V2.1 / CP 1545‑1 is a member of a VPN group and the option "IP routing between communications modules" is activated.

  > **Note**
  >
  > **S7 routing via the virtual interface**
  >
  > S7 routing via CP works by using the S7 gateway in the CP. If the IP address of the virtual interface "W1" is used as the next S7 router address, forwarding to the defined destination works via the S7 gateway of the CPU but the "back channel" is not guaranteed.

#### How to access this function

1. Select the module to be edited.
2. In the local security settings, select the entry "VPN" > "Nodes" > "Subnets reachable through tunnel".

#### Configuring subnets reachable via the backplane bus

VPN communication with network nodes and subnets reachable via the backplane bus of a station is only possible if this is released for VPN communication. In the entry "Subnets reachable through tunnel" a maximum of 16 addresses or subnets can be specified. IP addresses must be specified with a 32 bit subnet mask, subnets with a permitted subnet mask in the range 1... 31 bits. Broadcast addresses must not be specified.

#### Firewall settings when using the virtual interface W1

When using the virtual CPU interface with the CP as interface, we recommend the following settings:

1. Activate the extended firewall mode.
2. Specify the IP addresses or IP address ranges that are to have access to the CPU and the Web server OPC UA.
3. Make the settings for the protocol and, if necessary, the bandwidth limitation.

### Automatic OpenVPN configuration via SINEMA Remote Connect Server:

This section contains information on the following topics:

- [Automatic OpenVPN configuration and OpenNPN tunnel establishment](#automatic-openvpn-configuration-and-opennpn-tunnel-establishment)
- [Diagnostics of the automatic OpenVPN configuration and OpenNPN connections](#diagnostics-of-the-automatic-openvpn-configuration-and-opennpn-connections)

#### Automatic OpenVPN configuration and OpenNPN tunnel establishment

##### Supported modules

The function is available for several security modules and telecontrol communications modules.

##### Function

The module can establish an OpenVPN connection to the application "SINEMA Remote Connect Server". The OpenVPN connection parameters used for this are specified by the SINEMA Remote Connect Server. The module can call up these connection parameters cyclically and therefore automatically obtains the OpenVPN configuration.

##### Procedure

1. Select the module to be edited.
2. In the local security settings, select the entry "VPN".
3. Select the check box "Activate VPN" and select the VPN connection type "Automatic OpenVPN configuration via SINEMA Remote Connect Server".
4. Set the following parameters for the OpenVPN connection:

| Parameter | Meaning |
| --- | --- |
| SINEMA RC address | IPv4 / IPv6 address, FQDN or PROFINET device name of the SINEMA Remote Connect server from which the module calls up the connection parameters for the OpenVPN connection. |
| SINEMA RC port | Port for the connection to the SINEMA Remote Connect server that is used to call up the connection parameters for the OpenVPN connection. |
| CA Certificate | The module authenticates itself with the SINEMA Remote Connect server with a CA certificate that was downloaded from the server and selected for the module. Only certificates can be selected that were assigned to the module via its local certificate manager.  For the authentication of the SINEMA Remote Connect server, the module checks the CA certificate of the server. At the same time a check is made to establish whether the current time of day on the module is in the validity period of the certificate. |
| Fingerprint | The module authenticates itself with the SINEMA Remote Connect server with the "Fingerprint" property of the CA certificate of the SINEMA Remote Connect server. |
| Device ID | The device ID is assigned by SINEMA Remote Connect server for every module that is configured on the SINEMA Remote Connect server.  The device ID serves to identify a module. |
| Device password | Password configured for the device ID on the SINEMA Remote Connect server. |
| Update interval | Interval in minutes at which the module calls up the OpenVPN connection parameters to be used from the SINEMA Remote Connect server. Whether and with which connection parameters OpenVPN connections can be established is specified by the SINEMA Remote Connect server. With the value "0" the updating is disabled.  Minimum value for updating: 10 minutes  Maximum value for updating: 10080 minutes |
| Connection type | The connection type specifies when the module establishes an OpenVPN connection to the SINEMA Remote Connect Server:  - Permanent: The module establishes an OpenVPN connection after reading the OpenVPN connection parameters. The OpenVPN connection is retained until the connection parameters are changed by the SINEMA Remote Connect Server. - PLC trigger: The module establishes an OpenVPN connection as soon as the selected PLC tag has the value "TRUE". |
| PLC tag for connection establishment | Selection of a tag of the station of the type "BOOL". When the tag has the value "TRUE" the module establishes an OpenVPN connection to the SINEMA Remote Connect server: If the tag has the value "FALSE" the OpenVPN connection is terminated. |

#### Diagnostics of the automatic OpenVPN configuration and OpenNPN connections

##### Meaning

The diagnostics page shows the status of the automatic OpenVPN configuration and the OpenVPN connections.

The status of the automatic OpenVPN configuration indicates whether the module was able to call up the configuration file with the OpenVPN connection parameters to be used from the SINEMA Remote Connect Server.

For OpenVPN connections to the SINEMA Remote Connect Server, the connection status and its causes are displayed.

### Network authentication for CP1543-1/CP1545/1

#### Network authentication and EAP methods

If the CP wants to get access to a network via a switch, the CP must first authenticate itself before access to the network is enabled.

The authentication of the CP is performed via the RADIUS server that verifies the identity of the CP and thus the access to the network.

The communication for authentication runs via the Extensible Authentication Protocol (EAP). It is used for mutual authentication of CP and network and for key exchange for securing the communication.

For this, different EAP methods are available for selection as authentication methods.

#### Activate

1. Select the CP.
2. Select the "Network authentication" entry in the local security settings.
3. Select an EAP method:
4. Make the respective settings for the selected EAP method.

#### Notes on the individual EAP methods

- **MD5**

  The MD5 method is insecure against man-in-the-middle attacks and dictionary attacks. Use a more secure method if possible.
- **TLS**

  Established a secure, encrypted TLS connection. Provides certificate-based and mutual authentication of the client and the network.
- **PEAP**

  PEAP is a two-stage procedure. A secure tunnel is established in the first stage, in which another authentication procedure takes place in the second stage.  
  Unlike the TLS method, PEAP does not necessarily have to verify the identity of the client in the first stage. This is why the configuration of the client certificate is options.
- **TTLS**

  TTLS is a two-stage procedure, as an extension of TLS. Provides certificate-based mutual authentication of the client and the network through an encrypted channel (or tunnel). Requires only server-side certificates, unlike TLS.
- **MSCHAPv2**
    
  Procedure for logging on to Microsoft networks. Used only within a secured tunnel.
- **PWD**

  Can be used in a tunnel (e.g. TTLS) or alone.

#### Settings for the individual EAP methods.

Depending on the EAP method selection, make the following additional settings:

| EAP methods | Identity | Internal EAP method | Authentication settings | Verification settings | Server list |
| --- | --- | --- | --- | --- | --- |
| MD5 | User name  (1 to 256 characters) | - | Password (1 to 256 characters) | - | - |
| TLS | 1 to 256 characters   can also be left blank depending on the configuration of the RADIUS server. | - | - | CA certificate,must be assigned to the CP    Client certificate with private key, must be assigned to the CP | Optional input of one or more servers with * wildcard. Distinguished name or SAN of the server certificate must match for the connection to be established.   If no entry is made, any certificate signed by the certificate authority is allowed. |
| PEAPv0 | User name  (1 to 256 characters) | MD5  MSCHAPv2  PWD | Password (1 to 256 characters) | CA certificate must be assigned to the CP    Client certificate (optional, depending on the configuration of the RADIUS server); if so, then with private key. | Optional input of one or more servers with * wildcard. Distinguished name or SAN of the server certificate must match for the connection to be established.   If no entry is made, any certificate signed by the certificate authority is allowed. |
| TTLS | User name  (1 to 256 characters) | MD5  MSCHAPv2  PWD | - | - | - |
| MSCHAPv2 | User name  (1 to 256 characters) | - | Password (1 to 256 characters)  or  Hash value (MD4 hash of the password; 1 to 32 characters). | - | - |
| PWD | User name  (1 to 256 characters) | - | Password (1 to 256 characters) | - | - |

### CP 1545-1 certificates

This section contains information on the following topics:

- [Third-party certificates](#third-party-certificates)
- [Certificate manager](#certificate-manager)
- [Handling certificates](#handling-certificates)

#### Third-party certificates

##### Certificates of cloud providers

For encrypted communication between the S7 station and broker (MQTT over TLS), you need the root CA certificate of the cloud provider and possibly device certificates or private keys.

The requirements are different for the various cloud providers.

Obtain the required files from your cloud provider or download them from its Internet page.

#### Certificate manager

##### Assignment of certificates

If you use communication with authentication for the CP, you need to import certificates of the communications partners into the STEP 7 project and download them to the CP with the configuration data.

1. Import third-party certificates of all communications partners using the certificate manager in the global security settings.
2. Then assign the certificates of all its communications partners to the CP, either:

   - Using the "Trusted certificates and root certification authorities" table in the global security settings
   - Using the "Certificates of the partner devices" table in the local certificate manager of the module (security)

     In this table, also include the certificates of communications partners whose certificates were generated in the same STEP 7 project.

For a description of the procedure, refer to the section [Handling certificates](#handling-certificates).

#### Handling certificates

##### Certificate for authentication

If you have configured secure communication with authentication for the CP, own certificates and certificates of the communications partner will be required for communication to take place.

All nodes of a STEP 7 project with enabled security functions are supplied with certificates. The STEP 7 project is the certification authority.

> **Note**
>
> **No certificate with security functions disabled.**
>
> If the security functions of the CP are disabled in the STEP 7 project, no certificate will be generated for the CP.

A certificate is created for every application of the CP that requests a certificate. It is shown in STEP 7 in "Global security settings > Certificate manager > Device certificates". As well as additional information, you will find the respective usage of the certificate there (service/application).

You can call up more information about the certificate by selecting the certificate in the table and selecting the shortcut menu "Show".

So that the CP can communicate with non-Siemens partners when the security functions are enabled, the relevant certificates of the partners must be exchanged during communication. To supply the CP with third-party certificates, follow the steps below:

1. Importing third-party certificates from communications partners

   ⇒ Global security settings of the project (certificate manager)
2. Assigning certificates, either:

   - Global security settings > Certificate manager > "Trusted certificates and root certification authorities"
   - Local security settings of the CP > Certificate manager > "Certificates of the partner devices"

The steps are described in the following sections.

##### Importing third-party certificates from communications partners

Import the certificates of the communications partners of third-party vendors using the certificate manager in the global security settings of the STEP 7 project. Follow the steps outlined below:

1. Save the third-party certificate in the file system of the PC of the connected engineering station.
2. In the STEP 7 project open the global certificate manager:

   Global security settings > Certificate manager
3. Open the "Trusted certificates and root certification authorities" tab.
4. Click in a row of the table can select the shortcut menu "Import".
5. In the dialog that opens, import the certificate from the file system of the engineering station into the STEP 7 project.

##### Assigning certificates in the global security settings

Import the partner certificate via: Global security settings > Certificate manager > Trusted certificates > right mouse click. Assign the certificate to the CP (select certificate > right mouse click).

1. Open the "Trusted certificates and root certification authorities" tab.
2. Select the desired certificate.
3. Select "Assign" in the shortcut menu (right mouse button).
4. Select the desired module in the subsequent dialog.

   After the assignment, the certificate appears in the "Certificates of the partner devices" table in the local certificate manager of the module.

##### Assigning certificates locally

To be able to use an imported certificate for the CP, it needs to be displayed in the "Security" parameter group of the CP.

In this table, also include the certificates of communications partners whose certificates were generated in the same STEP 7 project.

Proceed as follows to import:

1. In the STEP 7 project select the CP.
2. Navigate to the parameter group "Security > Certificate manager".
3. In the table, double-click on the cell with the entry "<Add new>".

   The "Certificate manager" table of the Global security settings is displayed.
4. In the table. select the required third-party certificate and to adopt it click the green check mark below the table.

   The selected certificate is displayed in the local table of the CP.

##### Exporting certificates for applications of third-party vendors (e.g. logging server)

For communication with applications of third-party vendors, the third-party application generally also requires the certificate of the CP.

You export the certificate of the CP for communications partners from third-party vendors in much the same way as when importing (see above). Follow the steps outlined below:

1. In the STEP 7 project open the global certificate manager:

   Global security settings > Certificate manager
2. Open the "Device certificates" tab.
3. In the table select the row with the required certificate and select the shortcut menu "Export".
4. Save the certificate in the file system of the PC of the connected engineering station.

Now you can transfer the exported certificate of the CP to the system of the third-party vendor.

**Certificate for logging server**

If you use a logging server in your system, export the SSL certificate for the authentication of the CP on the server.

##### Change certificate: Subject Alternative Name

STEP 7 adopts the properties "DNS name", "IP address", and "URI" of the "Subject Alternative Name" (SAN) parameter from the STEP 7 configuration data.

You can change this parameter of a certificate inn the certificate manager of the global security settings. To do this, select the a certificate in the table of device certificates and call the shortcut menu "Renew". Properties of the parameter "Alternative name of the certificate owner" changed in STEP 7 are not adopted by the STEP 7 project.
