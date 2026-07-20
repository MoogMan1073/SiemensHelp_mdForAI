---
title: "Configuring the Web server (S7-300, S7-400, S7-1500)"
package: HWCWeb34enUS
topics: 44
devices: [S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Configuring the Web server (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Information about the web server (S7-300, S7-400, S7-1500)](#information-about-the-web-server-s7-300-s7-400-s7-1500)
- [Reading out service data (S7-300, S7-400, S7-1500)](#reading-out-service-data-s7-300-s7-400-s7-1500)
- [Standard websites (S7-300, S7-400, S7-1500)](#standard-websites-s7-300-s7-400-s7-1500)
- [Creating and loading user pages (S7-300, S7-400, S7-1500)](#creating-and-loading-user-pages-s7-300-s7-400-s7-1500)

## Information about the web server (S7-300, S7-400, S7-1500)

### Introduction

The Web server lets you monitor and administer the CPU through authorized users by means of a network. This permits evaluation and diagnostics over long distances. All you need is a web browser.

Alarms and status information are visualized on HTML pages.

### Web browser

You need a web browser to access the HTML pages of the CPU.

You will find information on the Web browsers and Web browser versions with which the Web server was tested in the manuals listed and linked below.

> **Note**
>
> If you access the Web server of the CPU using a communications processor (CP), ensure that the cache (temporary Internet files) is enabled in your browser. Choose the "Automatically" option in the cache settings of your browser.
>
> If the cache is disabled or if a setting other than "Automatically" is made in your browser, this may result in slow access times and incomplete display.

### Reading information via the Web server

The following information can be read from the CPU. The availability of the respective web pages depends on the CPU and its firmware version.

[Documentation for S7-300](http://support.automation.siemens.com/WW/view/en/12996906)

[Documentation for S7-400](http://support.automation.siemens.com/WW/view/en/44444467)

[Documentation for S7-1500](http://support.automation.siemens.com/WW/view/en/59193560)

Below you will find an overview of the information available on the individual Web pages of the Web server of the CPU S7-1500.

| Information | Description |
| --- | --- |
| Start page with general CPU information | The start page provides an overview of general information on the CPU, the name of the CPU, the type of CPU and basic information on the current operating state. |
| Diagnostics: Identification information | Displays the static identification information such as serial number, article number and version numbers. |
| Diagnostics: Memory | Current values on the memory in use. |
| Content of the diagnostic buffer | Displays the content of the diagnostics buffer with the most recent entries first. |
| Status of the modules | Displays whether the components of a station are in proper order, if, for example, there are maintenance requirements or components cannot be reached. |
| Firmware update | As a user with suitable access rights, you have the option of updating the firmware of CPUs, of the display or individual central or distributed modules with an update file. |
| Alarms | Displays project-oriented alarm text with filters and sorting options. |
| Information about communication | Display of the communication connections, display of the resources as well as interface parameters and port statistics. |
| Topology | Display of the topology with the graphic, table views and status overview for networked PROFINET participants. |
| Status of the tags | Display of the status of user program operands for observing the values.  Tip: When the tag status page is exited, the entries made on it are not saved. If you want to monitor the same entered tag again later on, create a bookmark in your Web browser for the "Tag status" page. Otherwise, you will have to enter the tag again when the page is re-opened. |
| Watch tables | Display of the watch tables created with STEP 7.  See [Tips on using watch tables in the web server](#tips-on-using-watch-tables-in-the-web-server-s7-300-s7-400-s7-1500) |
| User pages (if such Web pages/Web applications have been configured and loaded) | The user pages deliver a list of Web pages with customer-specific Web applications.  With the first call of the "WWW" instruction in the user program, the link to the user page is displayed on this Web page . A click on the link opens the user page in a new window. |
| File browser | S7-1500: The file browser lists files and directories that are located on the SIMATIC Memory Card.   Files can be downloaded, deleted, renamed or uploaded regardless of the file type.   Directories can only be created, deleted or renamed.   The Filebrowser only grants you read access to the "DataLogs" and "Backups" directories. System files are not displayed in the file browser and can therefore not be changed or deleted.  System files are the order file and all the special directories including their content which are referenced by the order file. |
| Data logs | Display and call up of the data logs generated by the user program.    **Note**:  If you open large data log files via this Web page, the processing times of the data log instructions that process this data log file can increase considerably.   Although the processing time of the priority class (OB in which the data log instruction is called) does not increase, the output parameter BUSY is set for the duration of the processing. |
| Online backup | S7-1500 (firmware V2.0 or higher): Backing up and restoring the CPU configuration. You can back up a CPU configuration using the Web server with the corresponding access rights. If necessary, you can restore this configuration at a later time. You can create as many backups as you want and store a variety of configurations for a CPU. |
| Motion diagnostics | S7-1500 (firmware V2.0 or higher): Displays the status, errors, technology interrupts and the current values of technology objects (TOs), for example, speed axis (TO_SpeedAxis), positioning axis (TO_PositioningAxis), synchronous axis (TO_SynchronousAxis), external encoder (TO_ExternalEncoder), measuring input (TO_MeasuringInput), cam (TO_OutputCam), cam track (TO_CamTrack). The "Motion diagnostics" Web page provides detailed information on the configured technology objects in the Diagnostics and Service overview views. |
| Trace | Display of measurements stored on the SIMATIC memory card. |

### Web access to the CPU via PG/PC

Proceed as follows to access the Web server:

1. Connect the client (PG/PC) to the CPU via the PROFINET interface.

   If you do not access the web via the PROFINET interface of the CPU but via the interface of a CP (e.g., CP 1543-1), the web pages load much more slowly than with the connection via the interface of the CPU. Make sure that the cache settings (temporary Internet files) of the browser are set to "Automatic" in this case.
2. Open the web browser.

   Enter the IP address of the CPU in the "Address" field of the Web browser in the format http://ww.xx.yy.zz (example: http://192.168.3.141).  
   The start page of the CPU is opened. You can navigate from the start page to additional information.  
   If the start page does not appear, make sure that the Web server was activated in the configuration and that the configuration was loaded.

### Web access to an S7-300/400 CPU via HMI devices and mobile devices

The Web server also supports the Windows Terminal Service so that in addition to the operation of programming devices and PCs, thin client solutions with mobile devices (e.g. PDA, MOBIC T8) and rugged local stations (e.g. SIMATIC MP370 with ThinClient/MP option) with Windows CE are possible.

Proceed as follows to access the Web server:

1. Connect the client (HMI device, PDA) with the CPU via the PROFINET interface.
2. Open the web browser.

   Enter the IP address of the CPU in the "Address" field of the Web browser in the format http://ww.xx.yy.zz /basic (example: http://192.168.3.141/basic).  
   The start page of the CPU is opened. From the start page, you can navigate to further information.

HMI devices operating with the Windows CE operating system V 5.x or earlier process CPU information in a browser specially developed for Windows CE. The information appears in a simplified format in this browser.

> **Note**
>
> **Using SIMATIC Micro Memory Card with Web server (S7-300)**
>
> The configuration data for the Web server is stored on the SIMATIC Micro Memory Card. That is why we recommend using a SIMATIC Micro Memory Card with at least 512 KB.
>
> You can also use the Web server without SIMATIC Micro Memory Card. The CPU must have been assigned an IP address to permit operation.
>
> - The content of the diagnostic buffer is displayed in hexadecimal code.
> - Start page, identification and communication information and tag status are displayed as plain text.
> - Following displays remain empty:
>
>   - Topology
>   - Alarms
>   - Status of the modules
> - The automatic page refresh is also activated without SIMATIC Micro Memory Card and without configuration.

### Web access to an S7-1500 CPU via HMI devices and mobile devices

HMI devices operating with the preinstalled Windows CE operating system (V 5.x or earlier) process CPU information in a browser specially developed for Windows CE. The information appears in a simplified format in this browser.

The Web server offers web pages with reduced complexity which have been optimized for devices with small screens and low computing power.

Requirement for access with mobile devices:

- WLAN connection for the CPU (WLAN Access Point, for example, SCALANCE W788-1RR or SCALANCE W784-1)
- Activated Web server on the CPU
- WLAN has to be activated for the mobile device and a connection to the access point has to be established.

The procedure for a mobile device is identical to that for other devices (programming device/PC). In the browser, you enter the IP address of the CPU interface, download the certificate and install it subsequently.

### Web access to an S7-1500 CPU via the Web API

From firmware version V2.8 onwards, the S7-1500 CPUs offer a web-based API (Web API) as an interface for reading and writing CPU data.

The Web API can be reached via POST requests to the following URL:https://[ip_address]/api/jsonrpc

Through the Web API, clients (such as web browsers) call methods in the S7-1500 CPU that enable reading and writing of CPU data. This includes, for example, logging in and logging out as an authorized user and methods for querying the Web API itself, as well as methods for maintaining the session.

The JSON-RPC 2.0 (JavaScript Object Notation Remote Procedure Call) protocol is used. This protocol is based on HTTP. For example, web browsers have access via the Web API using JavaScript for asynchronous requests.

The information on which CPU variants have a Web API and which clients can use the Web API, as well as explanations and examples of the Web API methods, can be found in the function manual "[Webserver](http://support.automation.siemens.com/WW/view/en/59193560)".

### Security

Make sure that you protect the CPU from being compromised through the use of different methods, for example, by limiting network access and using firewalls.

The Web server offers the following security functions:

- Access via the secure transmission protocol HTTPS
- Configurable user authorization via user list

---

**See also**

[Requirements for web access (S7-300, S7-400, S7-1500)](#requirements-for-web-access-s7-300-s7-400-s7-1500)
  
[Certificates for the Web server (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#certificates-for-the-web-server-s7-1500)
  
[How communication with certificates works: HTTP over TLS (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#how-communication-with-certificates-works-http-over-tls-s7-1200-s7-1500-s7-1500t)
  
[Working with multi-language projects](Editing%20project%20data.md#working-with-multi-language-projects)

## Reading out service data (S7-300, S7-400, S7-1500)

The web server of an S7-1500 CPU gives you the option of saving service data. In addition to the contents of the diagnostic buffer, service data includes additional information on the internal status of the CPU. If you should encounter a problem with the CPU that you cannot resolve, you have the option of submitting the service data to the Service&amp;Support team.

### Procedure

1. Enter the following address in the address bar of your web browser:  
   "http://&lt;CPU IP address&gt;/save_service_data.html", e.g.,  
   "http://192.168.3.141/save_service_data.html"
2. Your screen displays the service data page with a button for saving the service data.

   ![Procedure](images/48087108235_DV_resource.Stream@PNG-de-DE.png)
3. Save the service data locally on your display device by clicking "Save ServiceData".

### Result

The data is saved into a .dmp file with the following naming convention: "&lt;MLFB&gt;&lt;serial number&gt;&lt;time stamp&gt;.dmp". The file name can be changed subsequently.

---

**See also**

[Saving service data (S7-1200, S7-1500)](Device%20and%20network%20diagnostics.md#saving-service-data-s7-1200-s7-1500)

## Standard websites (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Requirements for web access (S7-300, S7-400, S7-1500)](#requirements-for-web-access-s7-300-s7-400-s7-1500)
- [Settings for operation (S7-300, S7-400, S7-1500)](#settings-for-operation-s7-300-s7-400-s7-1500)
- [Enable the web server (S7-300, S7-400, S7-1500)](#enable-the-web-server-s7-300-s7-400-s7-1500)
- [Access only through HTTPS (S7-300, S7-400, S7-1500)](#access-only-through-https-s7-300-s7-400-s7-1500)
- [Activate automatic update (S7-300, S7-400, S7-1500)](#activate-automatic-update-s7-300-s7-400-s7-1500)
- [Set the regional web language (S7-300, S7-400, S7-1500)](#set-the-regional-web-language-s7-300-s7-400-s7-1500)
- [User administration (S7-300, S7-400, S7-1500)](#user-administration-s7-300-s7-400-s7-1500)
- [Server security (S7-300, S7-400, S7-1500)](#server-security-s7-300-s7-400-s7-1500)
- [Tips on using watch tables in the web server (S7-300, S7-400, S7-1500)](#tips-on-using-watch-tables-in-the-web-server-s7-300-s7-400-s7-1500)
- [Display classes of the messages (S7-300, S7-400, S7-1500)](#display-classes-of-the-messages-s7-300-s7-400-s7-1500)

### Requirements for web access (S7-300, S7-400, S7-1500)

In the following, the requirements for accessing standard CPU websites are explained, and the effects of missing or existing configuration information are illustrated.

#### Requirement

The web server must be started.

The web server does not start until you have enabled it in the "Web server" area of the CPU properties.

Note the following:

- The websites are transmitted by default through a non-secure connection and are not protected from third party access. If you want to transmit the websites in an encrypted fashion, then enable the "Only permit access through HTTPS" option in the CPU characteristics. Make sure that the URL of the CPU begins with https:// in this case.
- Access through HTTPS only works if the time was set in the CPU.
- For further access protection, create a user in the "Web server" area of the CPU properties.
- The full functionality of the web pages in relation to module state, topology and alarms requires system diagnostic data to be generated and loaded (Report System Error) for S7-300/400 CPUs. After the web server has been activated, a query appears asking if the system diagnostics is to be enabled. You should acknowledge this query with "Yes".

#### Logon

To access the standard websites, no logon is required. A user must be logged on to execute certain actions like changing the operating mode of the CPU or for write access. The input fields for logging on are located in the upper left corner on each standard website.

![Logon](images/21057223947_DV_resource.Stream@PNG-en-US.png)

If you logon as a user, you have to enter the user name and password here. The user name and password are set in the "Web server" area of the CPU properties.

#### Web access without project information

Without configuration, only basic information is available on the standard websites. This information is available in different languages:

- Diagnostic buffer entries are not displayed as clear text without configuration information, but rather only as a hexadecimal code.
- If the web server supports the CPU tag tables (watch tables):

  The tag tables page does not display any tags without configuration. You can always open up a tag status.

#### Web access with configuration information

Texts are contained in the selected languages in the configuration information:

- Text for diagnostic buffer entries as short/long text
- For S7-300/400 CPUs: Alarm texts; for example, alarm component AlarmS/SQ, AlarmD/DQ
- If tag tables (watch tables) are supported: Tag tables with the symbols and comments contained in them

The texts for diagnostic buffer entries and alarms are shown during operation in the language that you set in your web browser.

---

**See also**

[Settings for operation (S7-300, S7-400, S7-1500)](#settings-for-operation-s7-300-s7-400-s7-1500)
  
[User administration (S7-300, S7-400, S7-1500)](#user-administration-s7-300-s7-400-s7-1500)

### Settings for operation (S7-300, S7-400, S7-1500)

#### Settings for operation

To use a CPU web server and set the behavior of the web server, you have to highlight the CPU in the network view, device view or topology view.

Execute the following settings in the Inspector window under "Properties &gt; General &gt; Web server", for example:

- Enable the web server
- Limiting web access to secure Hypertext transmission protocol (HTTPS)
- Activate automatic update
- Multilingual (set project languages for Web server and CPU display)
- Expanding user lists
- Using watch tables in the web server
- For S7-300/400 CPUs: Selecting the display classes of the alarms

Every PROFINET interface of an S7-1500 CPU or of a PROFINET CP or a PROFINET-CM can also be enabled or disabled for "external" access to the web server. It is simplest to manage this access centrally in the properties of the CPU. To do so, click the "Web server &gt; Overview of interfaces" area in the "Properties" tab of the inspector window and activate the interfaces through which access is allowed.

---

**See also**

[Project text basics](Editing%20project%20data.md#project-text-basics)
  
[Requirements for web access (S7-300, S7-400, S7-1500)](#requirements-for-web-access-s7-300-s7-400-s7-1500)
  
[Enable the web server (S7-300, S7-400, S7-1500)](#enable-the-web-server-s7-300-s7-400-s7-1500)
  
[Activate automatic update (S7-300, S7-400, S7-1500)](#activate-automatic-update-s7-300-s7-400-s7-1500)
  
[Set the regional web language (S7-300, S7-400, S7-1500)](#set-the-regional-web-language-s7-300-s7-400-s7-1500)
  
[User administration (S7-300, S7-400, S7-1500)](#user-administration-s7-300-s7-400-s7-1500)
  
[Access only through HTTPS (S7-300, S7-400, S7-1500)](#access-only-through-https-s7-300-s7-400-s7-1500)
  
[Display classes of the messages (S7-300, S7-400, S7-1500)](#display-classes-of-the-messages-s7-300-s7-400-s7-1500)
  
[Information about the web server (S7-300, S7-400, S7-1500)](#information-about-the-web-server-s7-300-s7-400-s7-1500)

### Enable the web server (S7-300, S7-400, S7-1500)

#### Enable the web server

The web server is disabled by default. The corresponding option box must be enabled to have the CPU show websites.

This setting can be found in the Inspector window under "Properties &gt; General &gt; Web server"; optional box "Enable web server for this module".

If the web server was activated, a prompt is displayed for S7-300/400 CPUs asking whether the system diagnostics (Report System Errors) should be enabled. Click on "Yes" if the required modules and texts should be generated with "Report System Errors" so that the alarm texts are available in the web browser during operation. For S7-1200/1500 CPUs, system diagnostics is always enabled (cannot be disabled).

In the case of S7-1500 CPUs with several PROFINET interfaces or when CPs with PROFINET interfaces are configured, you additionally have to activate the interfaces through which web server access is to be allowed. This setting is located under "Properties &gt; General &gt; Web server &gt; Overview of interfaces".

### Access only through HTTPS (S7-300, S7-400, S7-1500)

#### Access only through HTTPS

HTTPS is used for the encryption and authentication of the communication between the browser and web server.

The web pages are transmitted by default via non-secure connection and are not protected from attacks by third parties. If you always want to transmit web pages and login information to the browser in secure form, enable the "Permit access only with HTTPS" option in the CPU properties. Note that the URL of the CPU starts with "https://" in this case.

Note: Prerequisite for the use of the secure transmission protocol "HTTPS" is a valid Web server certificate in the CPU.

#### Requirements for access via HTTPS

For error-free HTTPS access from your Web browser to the Web server of the CPU, the following conditions must be met:

- The current time is set on the CPU.  
  The following generally applies: When using secure communication (for example, HTTPS, secure OUC, OPC UA), make sure that the corresponding modules have the current time of day and the current date. Otherwise, the modules evaluate the used certificates as invalid and the secure communication does not work.
- The IP address of the CPU must be set.
- A valid root certificate offered by the CPU should be installed in the Web browser.

  If no certificate is installed, a warning is output recommending that you do not use the page. To view this page, you must explicitly "Add an exception".

  A valid root certificate (certification authority) is available for download on the "Intro" web page of the Web server under "Download certificate".

  You can find instructions for installing the certificate in the help system of your Web browser and in the [FAQ](https://support.industry.siemens.com/cs/ww/en/view/103528224) with the entry ID 103528224 on the Service&amp;Support Internet page.

> **Note**
>
> To protect against manipulation from the outside, download the certificate only in an environment that is guaranteed not to be compromised.
>
> Installation of the root certificate has to be carried out once for each display device you wish to use.

#### Example of access to web pages with HTTPS protocol

To access web pages of the CPU with HTTPS protocol, enter the URL in the following format: https://ww.xx.yy.zz, with ww.xx.yy.zz being the IP address of the CPU.

Example entry: https://192.168.3.141

You can recognize an encrypted connection by a lock symbol in the status bar of the web page.

#### Access protection

The certificate establishes an encrypted connection that prevents tapping or distortion of the communication but does not provide access protection. This means you have to protect your CPU from unauthorized access with the corresponding configuration in the user management.

---

**See also**

[Certificates for the Web server (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#certificates-for-the-web-server-s7-1500)
  
[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)

### Activate automatic update (S7-300, S7-400, S7-1500)

#### Activate automatic update

With the "Automatic updating" check box activated, the web sites are automatically updated in the time intervals set under the "Update interval". The "Identification" website is excluded from the updating.

Proceed as follows to activate the automatic updating:

1. Select the check box "Activate automatic update" under "Properties &gt; General &gt; Web server &gt; Automatic update".
2. Enter the updating interval.

   > **Note**
   >
   > **Update time**
   >
   > The set activation interval is the shortest updating time. Larger amounts of data or several HTTP/HTTPS connections increase the update time.

### Set the regional web language (S7-300, S7-400, S7-1500)

#### Set the regional web language

To select the regional languages for language-dependent texts which will be downloaded to the CPU, proceed as follows:

1. Navigate to the "Multilingual" area in the Inspector window.
2. Activate the required languages for display in the web browser in the first column; the number of selectable languages is specific to the CPU.
3. Assign the desired project language to the languages of the display / Web server.

   The project languages that are assigned must be activated and the corresponding texts (translations) must be in the project. The project language selection can be found in the project navigation under "Languages &amp; Resources".

   Through these assignments, for example, display texts not available in the CPU will be downloaded in the selected language (with language and country code) when loading the CPU.

   ![Set the regional web language](images/91820820747_DV_resource.Stream@PNG-en-US.png)

   > **Note**
   >
   > If you activate the web server and do not assign a language, messages and diagnostic information are displayed in a hexadecimal code.

---

**See also**

[Multilingual (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#multilingual-s7-1500)

### User administration (S7-300, S7-400, S7-1500)

#### User Management

The User Management offers the following possibilities:

- Create users
- Set execution rights
- Assign passwords

With this assignment, users are exclusively entitled to options that are assigned to the execution rights.

- If a user is configured, this user can access the web pages according to his access authorizations after logging on with his password.
- Depending on the CPU and firmware used, you can assign different user rights. Rights that your CPU does not support cannot be selected.
- A user called "Everybody" with minimal access rights is created by default in the user list: Read access to the intro and start page. The "Everybody" user is defined without assignment of a password.
- As a non-logged-in user, you always access the Web server as the "Everybody" user by default. It does not matter in this case whether you have configured additional users.

  However, you can assign all access authorizations available in STEP 7 to the "Everybody" user. Because the "Everybody" user is defined in STEP 7 without assignment of a password, pay close attention to the access authorizations you assign to this user. Individual authorizations, such as the option to change the operating mode, may pose a safety risk.

  For assigning of safety-related authorizations, we recommend the following: Configure a user and always assign a password!

#### Recommendations for password assignment

- Assign secure passwords to users during configuration.

  An example of a secure password is one which is only used for a single application, is more than 8 characters long, and consists of lower-case and upper-case letters as well as special characters and numbers (?!+%$1234...).
- Do not use commonly used character sequences on the computer keyboard or words from the dictionary.
- Change the password at regular intervals. If possible, select the "Permit access only with HTTPS" option as soon as you have assigned a password to at least one user.

### Server security (S7-300, S7-400, S7-1500)

A Web server certificate has to be generated and assigned to the CPU for SIMATIC S7‑1500 CPUs as of firmware V2.0 to use the HTTPS transmission protocol.

The Web server certificate is also prerequisite for user administration of the Web server (password protection).

#### Requirements

You have opened the properties of the CPU (Inspector window).

#### Procedure

The settings for generation of a Web server certificate are located in the CPU properties in the "Web server &gt; Security" area.

You can generate or select certificates in this area. A distinction is made as to whether or not you are using the certificate manager in the global security settings.

For additional information of the certificate manager and the procedure involved refer to "See also".

#### Generation of Web server certificates depending on the CPU firmware version

With SIMATIC S7-1500 CPUs as of firmware V2.0, you have to create the certificate for the Web server of the CPU with STEP 7 yourself and assign it to the Web server in the CPU properties. This certificate is also downloaded to the CPU automatically when the hardware configuration is downloaded.

The STEP 7 project itself has a root certificate (CA, Certification Authority) with which the Web server certificate can be signed. Logging in for the certificate manager in the global security settings is required to this purpose.

Exception:

When you update the firmware of an S7‑1500 CPU or ET 200SP with firmware version &lt; V2.0 to a firmware version ≥ V2.0, a valid server certificate is automatically generated by the CPU and used. The same applies to the replacement parts scenario in which a newer CPU replaces a CPU with firmware version &lt; V2.0.

In these cases the Web server certificate of STEP 7 is not used.

---

**See also**

[Certificates for the Web server (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#certificates-for-the-web-server-s7-1500)
  
[What you should know about the certificate manager (S7-1500)](Functional%20description%20of%20S7-1500%20CPUs%20%28S7-1500%29.md#what-you-should-know-about-the-certificate-manager-s7-1500)
  
[Global security certificate manager (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#global-security-certificate-manager-s7-1200-s7-1500-s7-1500t)
  
[Certificate management with TIA Portal (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#certificate-management-with-tia-portal-s7-1200-s7-1500-s7-1500t)
  
[Device-dependent security features (S7-1200, S7-1500, S7-1500T)](Configuring%20devices%20and%20networks.md#device-dependent-security-features-s7-1200-s7-1500-s7-1500t)

### Tips on using watch tables in the web server (S7-300, S7-400, S7-1500)

#### Using watch tables in the web server

You can also display configured watch tables in the web server.

To do so, you must select the desired watch tables in STEP 7 in the CPU parameter area "Web server &gt; Watch tables" and set which access is to be permitted:

- Read access
- Read/write access

To be able to read values from and write values to the CPU, you need to have configured a user with the appropriate access rights in STEP 7.

To be able to write data, the "Referrer" transfer must be activated in your Web browser (this is the default in all common browsers).

#### Tip

When you use watch tables in the web server, these tables must be consistent; this means the referenced tags (e.g. DB elements) must not have been revised later in the watch table.

When you change the variables referenced in the watch tables after creating and downloading the watch tables, follow these steps to prevent inconsistencies:

1. Compile the user program (Compile &gt; Software).
2. Open all watch tables used by the web server and close them again.

   This step updates the references of the watch tables to the tags used.
3. Compile the hardware configuration (Compile &gt; Hardware …).

   This step updates the web server configuration with the watch tables used.
4. Load the changes (Download &gt; Hardware and software).

### Display classes of the messages (S7-300, S7-400, S7-1500)

#### Display classes of the messages

All display classes of the messages are activated in the basic configuration. The messages for the selected display classes are displayed during operation on the "Messages" website. Messages for display classes that are not selected are shown as hexadecimal code and not as plain text.

How to configure the display classes:

- for "Report System Errors" in the Inspector window under "Properties &gt; General &gt; System diagnostics"
- for module-related messages in the message editor

  > **Note**
  >
  > **Reducing memory requirements**
  >
  > You can reduce the memory requirements for the web server configuration by selecting only the display classes of the messages that should be used.

## Creating and loading user pages (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [What you need to know about user pages (S7-300, S7-400, S7-1500)](#what-you-need-to-know-about-user-pages-s7-300-s7-400-s7-1500)
- [Procedure overview (S7-300, S7-400, S7-1500)](#procedure-overview-s7-300-s7-400-s7-1500)
- [Creating web pages (S7-300, S7-400, S7-1500)](#creating-web-pages-s7-300-s7-400-s7-1500)
- [User page as start page and size recommendations (S7-300, S7-400, S7-1500)](#user-page-as-start-page-and-size-recommendations-s7-300-s7-400-s7-1500)
- [AWP commands for controlling Web pages (S7-300, S7-400, S7-1500)](#awp-commands-for-controlling-web-pages-s7-300-s7-400-s7-1500)
- [Creating and loading a data block (S7-300, S7-400, S7-1500)](#creating-and-loading-a-data-block-s7-300-s7-400-s7-1500)
- [Structure of the PLC program (S7-300, S7-400, S7-1500)](#structure-of-the-plc-program-s7-300-s7-400-s7-1500)
- [Web Control DB (S7-300, S7-400, S7-1500)](#web-control-db-s7-300-s7-400-s7-1500)
- [Interaction with the user program (S7-300, S7-400, S7-1500)](#interaction-with-the-user-program-s7-300-s7-400-s7-1500)
- [Displaying custom web pages in the browser (S7-300, S7-400, S7-1500)](#displaying-custom-web-pages-in-the-browser-s7-300-s7-400-s7-1500)
- [Create multilingual user defined websites (S7-300, S7-400, S7-1500)](#create-multilingual-user-defined-websites-s7-300-s7-400-s7-1500)
- [Language switching for custom web pages (S7-300, S7-400, S7-1500)](#language-switching-for-custom-web-pages-s7-300-s7-400-s7-1500)
- [Example of a language switch (S7-300, S7-400, S7-1500)](#example-of-a-language-switch-s7-300-s7-400-s7-1500)
- [Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)
- [Using source files for web server user-defined pages in STEP 7 (TIA Portal) (S7-300, S7-400, S7-1500)](#using-source-files-for-web-server-user-defined-pages-in-step-7-tia-portal-s7-300-s7-400-s7-1500)

### What you need to know about user pages (S7-300, S7-400, S7-1500)

#### Concept

The concept of user pages or of user-defined web pages allows you to access freely-designed web pages of the CPU with a web browser. The Web server of the CPU provides this function.

You are not dependent on special tools for the design and functionality of the user-defined web pages. You can adapt the pages in the layout with CSS, provide dynamic content with JavaScript or use any framework to produce web pages. The totality of files processed by the Web server is also referred to as the "web application".

#### Web application and user program

Using HTML code in user-defined web pages (AWP commands), you can also transmit data via a web browser to the user program of the CPU for further processing and can display data from the operand area of the CPU in the web browser.

You can use script instructions (such as Javascript) to optimize your web pages, for example to dynamically change contents or validate user entries.

To synchronize between the user program and the Web server, but also to initialize, you must call the WWW (SFC 99) instruction in the user program.

- If no interaction is required between the web application and the user program, for example, if a web page only provides static information, only initialization in the user program is required.
- If a simple data exchange is necessary between PLC tags and tags in web applications, to display the contents of PLC tags or write a value in a PLC tag for example, the syntax for reading and writing tags has to be observed. In this case only an initialization is required in the user program, for example in the startup OB.
- If a further interaction is required between the web application and the user program, you must handle status and control information from the Web Control DB in addition to the synchronization between Web server and user program. This is the case, for example, when user entries are transmitted via the web browser to the Web server for evaluation by the CPU. Unlike simple data exchange, the user program directly influences the time at which the requested web page is relayed back to the web browser. In this case, you must be acquainted with the concept of manual fragments and the structure of the Web Control DB.

#### Integration of the HTML sources via the TIA Portal

The parameters for an integration of the HTML sources in the TIA Portal are located in the properties of the respective CPU with Web server:

| Parameter | Meaning |
| --- | --- |
| HTML directory | Directory of the HTML sources for the web applications. You can input the path directly or navigate to the directory by using the button next to the entry field.   It is advantageous if you integrate your Web pages with relative paths. To do this you have to insert the directory in which you store the HTML sources for the Web application in the STEP 7 project directory, for example, in a new directory "Webpages". You then specify the relative path name as the HTML directory; in the example ".\Webpages".   Advantages of using relative paths:   - The user-defined Web pages are archived together with the STEP 7 project. - The Web pages are copied to the new path with the menu command "Project &gt; Save as...". - When copying the project to another path using the Windows Explorer, it is no longer necessary to adapt the HTML directory path to generate new Web DBs. - Several control systems in a project that use the same HTML pages also have the same HTML directory path information. |
| Start HTML page | Path to the Start HTML page. You can input the path directly or navigate to the HTML page with the button next to the entry field. The start HTML page is the HTML page to be opened at the start of the web application. |
| Application name | Optional name for the application. This name is used to further divide or group the web pages. When an application name already exists, the URL is displayed in the following format:"http://a.b.c.d/awp/&lt;Application name&gt;/&lt;Page name&gt;.html" |

#### Initialization

User-defined web pages are "packaged" in data blocks for processing by the CPU. You must generate appropriate data blocks from the source data (HTML files, images, JavaScript files, etc.) during configuration to be able to download the web application into the CPU. The Web Control DB takes on a special role (default: DB 333). It contains status and control information as well as links to additional data blocks with coded web pages. Data blocks that contain coded web pages are termed "Fragment DBs".

When the data block is downloaded into the CPU, the CPU does not "know" that user-defined web pages are coded inside it. The "WWW" (SFC 99) instruction, for example, in the Startup OB informs the CPU which DB is the Web Control DB. The user-defined web pages can be accessed via a web browser after this initialization.

#### Synchronization

If the user program is to exchange data with the user-defined web pages, the WWW (SFC 99) instruction must be used in the cyclic program section.

Examples of interaction between user program and web page:

- Check received data
- Assemble and send back data to the web browser making the request

In this case, the status information must be able to be evaluated and control information must be transmitted to the Web server, for example, to release a requested web page.

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)
  
[WWW: Synchronizing user pages (S7-1200, S7-1500)](Web%20server%20%28S7-1200%2C%20S7-1500%29.md#www-synchronizing-user-pages-s7-1200-s7-1500-1)
  
[S7-1500 web server](http://support.automation.siemens.com/WW/view/en/59193560)

### Procedure overview (S7-300, S7-400, S7-1500)

#### Basic

In this chapter, the basic procedure is explained step-by-step to create, load and use user-defined websites in the operating phase.

The following image displays the procedure for the creation and display of user-defined websites:

![Basic](images/24771890827_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Programming a web application (using suitable tools when required and AWP commands for dynamic pages when applicable). |
| ② | Web application consists of individual source files, for example, *.html, *.gif, *.js, ... |
| ③ | With STEP 7:  - Generating the data blocks (web-control-DB and fragment-DBs) from source files. The DBs contain meta information and the complete web application including the images and the dynamic and static parts of the web application. The DBs are stored in the project navigation under "System blocks". - Open the "WWW" (SFC 99) instruction in the user program. The instruction initializes the web server of the CPU for a web application. - If needed, program out interaction between web server and user program |
| ④ | Load the modules in the CPU. |
| ⑤ | Open website in the browser. The opening of websites from the CPU occurs through the Entry of the IP address of the CPU. |

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

### Creating web pages (S7-300, S7-400, S7-1500)

Web design tools from various companies can be used to create user-defined web pages. As a rule, the web pages should be programmed and designed compliant to the conventions of the W3C (World Wide Web Consortium). No check is made for compliance to W3C criteria in the web server of the CPU.

#### Rules

- The tool must be able to directly edit the HTML code so that the AWP command can be inserted into the HTML page.

  Only the AWP commands are parsed in the CPU and, for example, replaced by values from the user program/process image of the CPU.
- Files containing AWP commands must be coded in UTF-8. In the metadata of the HTML page, therefore, set the attribute charset to UTF-8 and save the file UTF-8 coded.
- Files containing AWP commands must not contain the following sequence: ]]
- Files containing AWP commands must not contain the following sequence outside of the "Tag read ranges" (:=&lt;Tag name&gt;:): :=

  Tip: Replace the first character of a prohibited sequence with its character coding; for the colon, for example, &amp;#58;.

A small example for a custom web page should make clear the basic design.

#### Requirement

- The CPU must have a web server and the web server of the CPU must be activated.
- To be able to access PLC tags with write access as a user, you must be logged on as "admin".
- For the example below, PLC tags must be defined for those PLC tags that are to be shown on the web page. This is shown here for the first tab used, "Tank_below_max".

  ![Requirement](images/21252750603_DV_resource.Stream@PNG-en-US.png)

#### Creating user-defined web pages

The following code for an example web page reads values from the process image and provides them in a table.

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd"&gt;  
&lt;html&gt;  
 &lt;head&gt;

&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8"&gt;

&lt;title&gt;Mix&lt;/title&gt;

&lt;/head&gt;

&lt;body&gt;

&lt;h1&gt;Mix&lt;/h1&gt;

&lt;h2&gt; Actual State &lt;/h2&gt;

&lt;table border="1"&gt;

&lt;tr&gt;

&lt;th&gt;Variable&lt;/th&gt;

&lt;th&gt;State&lt;/th&gt;

&lt;/tr&gt;

&lt;tr&gt;

&lt;td&gt;Tank below max&lt;/td&gt;

&lt;td&gt;:="Tank_below_max":&lt;/td&gt;

&lt;/tr&gt;

&lt;tr&gt;

&lt;td&gt;Tank above min&lt;/td&gt;

&lt;td&gt;:="Tank_above_min":&lt;/td&gt;

&lt;/tr&gt;

&lt;/table&gt;

&lt;/body&gt;

&lt;/html&gt;

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

### User page as start page and size recommendations (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Defining the user page as start page (S7-300, S7-400, S7-1500)](#defining-the-user-page-as-start-page-s7-300-s7-400-s7-1500)
- [Recommendations for the size of Web pages (S7-300, S7-400, S7-1500)](#recommendations-for-the-size-of-web-pages-s7-300-s7-400-s7-1500)

#### Defining the user page as start page (S7-300, S7-400, S7-1500)

##### Defining the user page as start page

In addition to the default intro page, you can also define the start page of your user pages as the start page of the Web server.

##### Requirements

- You have configured a user in STEP 7 whom you have assigned at least the authorization "... open user-defined web pages".
- The CPU is in RUN mode.

##### Procedure

Proceed as follows to define the user pages in STEP 7 as start page of the Web server:

1. Select the CPU in the device configuration.
2. Open the settings in the Inspector window of the CPU under "Properties &gt; General &gt; Web server".
3. Select the entry "AWP1" in the area "Entry page" under "Select entry page".

If you now enter the IP address of the CPU in the browser, a connection is automatically established to your user pages.

If you want to access the web pages of your CPU again, link the web pages from your user pages, via the URL "http://a.b.c.d./Portal/Portal.mwsl?PriNav=Start" or "https://a.b.c.d/Portal/Portal.mwsl?PriNav=Start" for example. In this case, the information "a.b.c.d" represents, as an example, the IP address of the configured CPU.

Example of link in HTML:

&lt;a href="/Portal/Portal.mwsl?PriNav=Start"&gt;SIMATIC web pages&lt;/a&gt;

> **Note**
>
> If you define your user page as start page of the Web server, all direct access to the web pages of the CPU is disabled. This applies also to the bookmarks you saved for the web pages of the CPU as well as the page for reading out the service data.

**Reading out service data**

If you define your user page as start page of the Web server, all direct access to the web pages for reading out the service data is also disabled.   
If you want to continue to read out service data via the Web server when servicing is required, here is how you can link the service data page directly to your user page.  
Just as for the web pages of the CPU, link the service data page e.g. via the URL "http://a.b.c.d/save_service_data" or "https://a.b.c.d/save_service_data", the "a.b.c.d" here is an example of the IP address of the configured CPU.

Example of link in HTML:

&lt;a href="/save_service_data"&gt;Service data&lt;/a&gt;

##### Reference

You can find additional information on the topic of user page as start page in the FAQ with entry ID 67184104 on the [Online Support](https://support.industry.siemens.com/cs/ww/en/view/67184104) Internet page.

#### Recommendations for the size of Web pages (S7-300, S7-400, S7-1500)

##### Influence of the Web page size on the required memory and performance

Extensive HTML pages, especially those with a lot of images, take up a lot of space in the load memory. Note the following tips:

- Select a SIMATIC Memory Card with enough memory to provide sufficient load memory.
- Limit the data volume of the HTML pages to 1 MB.

  When the data volume of the HTML pages exceeds 1 MB, performance losses may occur as only 1 MB data is saved in the cache.
- Limit the size of a file of an HTML page to 512 kB.

  When a single file of an HTML page exceeds 512 kB, problems can occur when sending the file from the Web server to the browser.

Have the file sizes displayed in the file explorer of the directory in which the Web application lies. Where necessary and possible, reduce the file sizes.

### AWP commands for controlling Web pages (S7-300, S7-400, S7-1500)

This section contains information on the following topics:

- [Using AWP commands in Web pages (S7-300, S7-400, S7-1500)](#using-awp-commands-in-web-pages-s7-300-s7-400-s7-1500)
- [Reading tags (S7-300, S7-400, S7-1500)](#reading-tags-s7-300-s7-400-s7-1500)
- [Particular points for PLC tags of the String and Character type (S7-300, S7-400, S7-1500)](#particular-points-for-plc-tags-of-the-string-and-character-type-s7-300-s7-400-s7-1500)
- [Writing tags (S7-300, S7-400, S7-1500)](#writing-tags-s7-300-s7-400-s7-1500)
- [Special tags (S7-300, S7-400, S7-1500)](#special-tags-s7-300-s7-400-s7-1500)
- [Enumeration types (S7-300, S7-400, S7-1500)](#enumeration-types-s7-300-s7-400-s7-1500)
- [Simplified use of enumeration types (S7-300, S7-400, S7-1500)](#simplified-use-of-enumeration-types-s7-300-s7-400-s7-1500)
- [Using arrays (S7-300, S7-400, S7-1500)](#using-arrays-s7-300-s7-400-s7-1500)
- [Using structures (S7-300, S7-400, S7-1500)](#using-structures-s7-300-s7-400-s7-1500)
- [Rules for arrays and structures (S7-300, S7-400, S7-1500)](#rules-for-arrays-and-structures-s7-300-s7-400-s7-1500)
- [Definition of fragments (S7-300, S7-400, S7-1500)](#definition-of-fragments-s7-300-s7-400-s7-1500)
- [Importing fragments (S7-300, S7-400, S7-1500)](#importing-fragments-s7-300-s7-400-s7-1500)

#### Using AWP commands in Web pages (S7-300, S7-400, S7-1500)

With AWP (Automation Web Programming) commands, you declare the interface between your user pages (Web application, e.g. a simple HTML page) and the CPU data.

To develop user pages or Web applications, you need only observe the restrictions of the Web browser. In one of the programming languages of STEP 7, control with the user program in the CPU which CPU data is displayed at what time in the Web browser of the viewer.

Use AWP commands, which you comment within the HTML page, to declare data to be used for intentional interaction between the Web application and the user program.

You insert AWP commands as HTML comments with a special syntax into HTML pages. Using AWP commands, the following features can be implemented:

- Read PLC tags
- Write PLC tag
- Read special tags
- Write special tags
- Define enum types
- Assign tags to enum types
- Defining fragments
- Import fragments

##### Syntax of AWP commands

An AWP command begins with "`<!-- AWP_`" and ends with " `-->`". In JavaScript files, the commands should also be enclosed by JavaScript comments ("`/*...*/`").

##### Notation rules for PLC tag names within an AWP command

The AWP commands "AWP_In_Variable" and "AWP_Out_Variable" contain a name attribute and optionally a use attribute. A PLC tag name is assigned to these attributes, by means of which the PLC tags in the browser are written or read. The following rules apply to handling PLC tag names in HTML code:

- PLC tags must be enclosed in quotation marks (" ... ").
- PLC tags used in AWP commands must also be enclosed by single quotation marks ('" ... "') or with quotation marks masked by a backslash ("\" ... \"").
- If the PLC tag name contains the character \ (backslash) or * (star), this character must be designated with the escape sequence \\ as standard character of the PLC tag name. See below for examples.
- If the PLC tag name in the AWP command is also enclosed by single quotation marks and the single quotation mark (') occurs within the name, it must also be designed as normal character by the escape sequence \'.
- If an absolute address (input, output, bit memory) is used in AWP command, it is enclosed by single quotation marks.

| PLC tag | PLC tag in HTML code |
| --- | --- |
| "Velocity" | &lt;!-- AWP_In_Variable Name='"Velocity"' --&gt;  &lt;!-- AWP_In_Variable Name="\"Velocity\"" --&gt; |
| "abc\de" | &lt;!-- AWP_In_Variable Name='"abc\\de"' --&gt; |
| "abc'de" | &lt;!-- AWP_In_Variable Name='"abc\'de"' --&gt; |
| "abc'de" | &lt;!-- AWP_In_Variable Name="abcde" Use'"abc\'de"' --&gt; |
| "DB name".tag | &lt;!-- AWP_In_Variable Name='"DB name".tag' --&gt; |
| "Plc1".Data[1].typeDataStruct.value | &lt;!-- AWP_In_Variable Name='"Plc1".Data[1].typeDataStruct.value' --&gt; |
| - | &lt;!-- AWP_Out_Variable Name=’flag1’ Use='M0.0' --&gt; |

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

#### Reading tags (S7-300, S7-400, S7-1500)

User-defined web pages can read PLC tags.

The PLC tag must be specified by a PLC tag name.

These OUT variables (direction of output as viewed from the controller) are inserted at any location within the HTML text with the syntax described in the following.

##### Syntax

:=&lt;varname&gt;:

These references are replaced when the Web server is in operation by the current values of the PLC tag in each case.

`<varname>` can be a simple, global PLC tag but also a complete tag path to a structural element.

##### Notation rules for PLC tag names

- PLC tags in HTML code are enclosed by quotation marks ("), if they are defined in the tag table. In the case of data block tags, the name of the data block is enclosed by quotation marks. If special characters are used in the structure elements of the data block, for example the dot (.) or blank, this part must also be enclosed by quotation marks.
- Quotation marks are not used for absolute addresses of inputs, outputs or bit memories.

| PLC tag | PLC tag in HTML code |
| --- | --- |
| "DB_name".var_name | :="DB_name".var_name: |
| "DB_name"."var.name" | :="DB_name"."var.name": |
| "memory" | :="memory": |
| - | :=I0.0:  :=Q0.0:  :=MW100:  :=%MW100: |
| "My_Data_Block".flag1 | &lt;!-- AWP_Out_Variable Name='flag1' Use='"My_Data_Block".flag1' --&gt;  ...  :=flag1: |

- If the PLC tag name contains the character : (colon) or \ (backslash), this character must be designated with the escape sequence \: or \\ as standard character of the PLC tag name.

| PLC tag | PLC tag in HTML code |
| --- | --- |
| "abc:de" | :="abc\:de": |
| "abc\de" | :="abc\\de": |

- Special characters "&lt;, &amp;, &gt;"

  Display problems can occur if these characters are contained in the tag name (for example, "a&lt;b").

  Avoid expressions such as :="a&lt;b": in the HTML page.

  To prevent display problems from occurring, use e.g. an AWP command with a use expression according to the pattern depicted below. The use attribute defines the PLC tag with the problematic character, the name attribute defines the name without problematic character, as it is used in the HTML page.

| PLC tag | PLC tag in HTML code |
| --- | --- |
| "a&lt;b" | &lt;!-- AWP_Out_Variable Name='simplename' Use='"a&lt;b"' --&gt;  ...  :=simplename: |

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

#### Particular points for PLC tags of the String and Character type (S7-300, S7-400, S7-1500)

##### Reading tags of the String and Character type

Below, these types of quotation marks are used in the explanation: single quotation marks ('), double quotation marks (").

As of firmware V1.6, with the "Read PLC tags" function, the CPU outputs tags of the String or Character type enclosed in single quotation marks to the browser.  
For example:

- "Varname".MyString = ABC string tag
- You read the tag in HTML using the function :="Varname".MyString:
- The Web server outputs the character string 'ABC' to the browser

##### Using String or Character tags in expressions

On your HTML page, you use an expression in which the character string for reading a tag is enclosed in quotation marks, for example in forms.

Possible HTML code used:

&lt;input type="text" name="appfield" value="myvalue"&gt;

If you read the displayed value for the "value" attribute from a PLC tag in this expression, the HTML code appears as follows:

&lt;input type="text" name="appfield" value=":="Varname".MyString:"&gt;

By reading the PLC tag, the Web server outputs the value 'ABC'. In HTML, the code is then represented as follows:

&lt;input type="text" name="appfield" value=" 'ABC' "&gt;

If you have used single quotation marks instead of double quotation marks in your HTML code to enclose the attributes, the Web server passes on the content of the tags enclosed in two single quotation marks to the browser. As a result of this, the browser does not output the content of the String or Character tag, since two consecutive single quotation marks each form a closed sequence. The values to be read are located between these sequences and are not output by the browser.

In this context, note in particular that the character string with double quotation marks is not identical to two single quotation marks even if they appear to be identical.

> **Note**
>
> The code is not adapted automatically during an update to firmware as of V1.6.   
> Adapt your HTML code if you have used single quotation marks to enclose attributes for the "Read PLC tags" function.

![Using String or Character tags in expressions](images/94699918603_DV_resource.Stream@PNG-en-US.png)

#### Writing tags (S7-300, S7-400, S7-1500)

Custom web pages can write data into the CPU.

This requires an AWP command that identifies the PLC tag to be written.

The PLC tag must also be specified by a PLC tag name.

The IN tags (direction of input as viewed from the controller) are placed on the browser page. This can be done, for example, in a form.

The tags are either set in the HTTP header (by cookie or POST method) or in the URL (GET method) by the browser and are then written by the web server into the respective PLC tag.

##### Syntax

To allow the IN tags to be written to the CPU, the tags must first be defined by an explicit AWP instruction:

&lt;!-- AWP_In_Variable Name='"&lt;Varname1&gt;"' Name='"&lt;Varname2&gt;"' Name='"&lt;Varname3&gt;"' --&gt;

Several tags can be defined in an instruction - such as that shown above.

In cases where the name of the tag that you use for the web application is not identical to the name of the PLC tag, the "Use" parameter can be used to assign to a PLC tag.

&lt;!-- AWP_In_Variable Name=’&lt;Varname_Webapp&gt;’ Use=’&lt;PLC_Varname&gt;’

##### Example

The "AWP_In_Variable" AWP command is indispensable when handling forms.

&lt;form method="post" action="/awp/appl/x.html"&gt;  
 &lt;p&gt;  
 &lt;input name='"var1"' type="text"&gt;  
 &lt;input value="set" name='"Button1"' type="submit"&gt;  
 &lt;/p&gt;  
&lt;/form&gt;

In the form defined above, tags "var1" and "Button1" are transferred to the web server by "post". The user places the "var1" tag in the form field. The "Button1" tag has the fixed value "set". To allow the "var1" and "Button1" tags to be written to the CPU, the following instruction must be included in the same fragment:

&lt;!-- AWP_In_Variable Name='"var1"' Name='"Button1"' --&gt;

Because global tags are enclosed in quotation marks, the name must be enclosed in the AWP command by apostrophes or by masked quotation marks (\").

&lt;!-- AWP_In_Variable Name=’"Info".par1’ --&gt;

##### Conditions for write access during operation

The following requirement has to be met in order for a user to be able to write to PLC tags from a user-defined web page.

- A user was set up and is logged on.

This rules applies to all writing access to web pages on a CPU.

---

**See also**

[User administration (S7-300, S7-400, S7-1500)](#user-administration-s7-300-s7-400-s7-1500)
  
[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

#### Special tags (S7-300, S7-400, S7-1500)

Special tags are mainly HTTP tags set in the definition of the World Wide Web Consortium (W3C) . Special tags are also used for cookies and server tags.

The AWP command to read and write special tags differ only in that they have additional parameters than the AWP command used to read and write normal tags.

##### Reading a special tag

The Web server can read PLC tags and transfer these to special tags in the HTTP Response Header. You can, for example, read a URL for a diversion to another web page and transfer to the special tag HEADER:Location using the special tag HEADER:Location.

The following special tags can be read:

| Name | Description |
| --- | --- |
| COOKIE_VALUE:name | Value of cookie with name: "name" |
| COOKIE_EXPIRES:name | Execution time of cookie with name: "name" in seconds (must be set beforehand). |
| HEADER:Status | HTTP status code (if no other value has been set, status code 302 is returned). |
| HEADER:Location | Path for forwarding to another page. Status code 302 must be set. |
| HEADER:Retry-After | Anticipated time in which the service is not available. Status code 503 must be set. |
| HEADER: … | All other header tags can also be forwarded in this way. |

Use the AWP command "AWP_Out_Variable" to specify which PLC tags are to be transferred in the HTTP header to the web browser.

Basic structure:

&lt;!-- AWP_Out_Variable Name="&lt;Typ&gt;:&lt;Name&gt;" [Use="&lt;Varname&gt;"] --&gt;

##### Parameter description

- Name: Type and name of special tag
- Use (optional parameter): In cases where the name of the special tag is not identical to the name of the PLC tag, parameter "Use" can be used to assign to a PLC tag.

Example:

&lt;!-- AWP_Out_Variable Name="COOKIE_VALUE:siemens" Use='"info".language' --&gt;

##### Writing a special tag

In principle, all HTTP tags written in the HTTP header by the web browser can be evaluated by the user program of the CPU. Examples of tag types:

| Name | Description |
| --- | --- |
| HEADER:Accept-Language | Accepted or preferred language |
| HEADER:Authorization | Proof of authorization for a requested resource |
| HEADER:Host | Host and port of the requested resource |
| HEADER:User-Agent | Information on the browser |
| HEADER: … | All other header tags can also be forwarded in this way |
|  |  |
| SERVER:current_user_id | Indicates whether a user is logged on (current_user_id=0: no user logged on) |
| SERVER:current_user_name | User name of the user logged on |
| SERVER:GET | Request method is GET |
| SERVER:POST | Request method is POST |
|  |  |
| COOKIE_VALUE:name | Value of cookie with name: "name" |

The AWP command "AWP_In_Variable" is used to define which special tags are to be evaluated in the user program of the CPU.

Basic structure:

&lt;!-- AWP_In_Variable Name="&lt;Typ&gt;:&lt;Name&gt;" [Use="&lt;Varname&gt;"] --&gt;

Parameter description:

Name: Type and name of special tag

Use (optional parameter): In cases where the name of the special tag is not identical to the name of the PLC tag, the parameter Use can be used to assign to a PLC tag.

##### Examples:

&lt;!-- AWP_In_Variable Name="COOKIE_VALUE:siemens" Use='"info".language' --&gt;

The tag name in the HTTP header is replaced by the PLC tag name specified by Use . The cookie is written to the PLC tag "info".language .

&lt;!-- AWP_In_Variable Name='COOKIE_VALUE:siemens' Use='"info".language' --&gt;

The tag name in the HTTP header is replaced by the PLC tag name specified by Use. The cookie is written to the PLC tag "info".language .

&lt;!-- AWP_In_Variable Name='"COOKIE_VALUE:siemens"' --&gt;

The HTTP-header variable is written in the same-name PLC variable.

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

#### Enumeration types (S7-300, S7-400, S7-1500)

##### Enumeration types (enums)

Numerical values from the PLC program can be converted into text and vice versa using enums. The numerical values can also be assigned for several languages.

##### Creating enums

Enter an AWP command using the following syntax at the start of the HTML file:

&lt;!-- AWP_Enum_Def Name="&lt;Name of the enum type&gt;" Values='0:"&lt;Text_1&gt;", 1:"&lt;Text_2&gt;", ... , x:"&lt;Text_x&gt;"' --&gt;

For example, for German values to be saved as an HTML file in the "de" folder of the HTML directory:

&lt;!-- AWP_Enum_Def Name="Enum1" Values='0:"an", 1:"aus", 2:"Störung"' --&gt;

For example, for English values, to be saved as an HTML file in the "en" folder of the HTML directory:

&lt;!-- AWP_Enum_Def Name="Enum1" Values='0:"on", 1:"off", 2:"error"' --&gt;

##### Assigning enums

Tags are assigned from the user program to the individual enum texts using a special AWP command:

&lt;!-- AWP_Enum_Ref Name="&lt;VarName&gt;" Enum="&lt;EnumTypeName&gt;" --&gt;

&lt;VarName&gt; is thereby the symbolic name from the user program and &lt;EnumTypeName&gt; is the previously set name of the enum type.

> **Note**
>
> In each fragment in which enum texts are referenced by a PLC tag, this PLC tag must be assigned by the appropriate AWP command of the enum type name.
>
> Ensure that no AWP command for importing fragments is positioned between an enum assignment and enum usage because this import can result in the enum assignment lying in a different fragment than the enum usage.

##### Example

Enum type "state" is defined with values "0" and "1". "0" means "off", "1" means "on":

&lt;!-- AWP_Enum_Def Name="state" Values='0:"off", 1:"on"' --&gt;

The following code is contained in the HTML code of the web page to be output:

&lt;!-- AWP_Enum_Ref Name="operating state" Enum="state" --&gt;

:=operating state:

Depending on the value of the "operating state" tag, the ´result displayed is no longer "0" or "1", but "off" or "on".

---

**See also**

[Definition of fragments (S7-300, S7-400, S7-1500)](#definition-of-fragments-s7-300-s7-400-s7-1500)

#### Simplified use of enumeration types (S7-300, S7-400, S7-1500)

At S7-1200 CPUs as of firmware version 4 it is possible to use enumerations directly in AWP commands to read and write PLC variables.

You create enums as described in the previous section, and you can then utilize the values with user program read and write commands.

##### Creating enums

&lt;!-- AWP_Enum_Def Name="&lt;Name des Enum Typs&gt;" Values='0:"&lt;Text_1&gt;", 1:"&lt;Text_2&gt;", ... , x:"&lt;Text_x&gt;"' --&gt;

##### Utilizing enums in the user program read and write commands

&lt;!-- AWP_In_Variable Name='&lt;Varname&gt;' Enum="&lt;EnumType&gt;" --&gt;

&lt;!-- AWP_Out_Variable Name='&lt;Varname&gt;' Enum="&lt;EnumType&gt;" --&gt;

##### Example of reading PLC tags

**&lt;!-- AWP_Enum_Def Name='AlarmEnum' Values='0:"No alarms", 1:"Tank is full", 2:"Tank is empty"' --&gt;&lt;!-- AWP_Out_Variable Name='"Alarm"' Enum="AlarmEnum" --&gt;...&lt;p&gt;The current value of "Alarm" is :="Alarm":&lt;/p&gt;**

If the value of "Alarm" in the CPU is "2", the following text will be displayed on the HTML page:

'The current value of "Alarm" is Tank is empty' because the enum definition assigns the string "Tank is empty" to the numerical value 2.

##### Example of writing PLC tags

**&lt;!-- AWP_Enum_Def Name='AlarmEnum' Values='0:"No alarms", 1:"Tank is full", 2:"Tank is empty"' --&gt;&lt;!-- AWP_In_Variable Name='"Alarm"' Enum='AlarmEnum' --&gt;...**

**&lt;form method="POST"&gt;**

**&lt;p&gt;&lt;input type="hidden" name='"Alarm"' value="Tank is full" /&gt;&lt;/p&gt;**

**&lt;p&gt;&lt;input type="submit" value='Set Tank is full' /&gt;&lt;/p&gt;**

**&lt;/form&gt;**

Because the enum definition assigns the string "Tank is full" to the numerical value "1", the value "1" is written to the PLC tag "Alarm".

#### Using arrays (S7-300, S7-400, S7-1500)

The Web server provides the user program commands AWP_Start_Array and AWP_End_Array for accessing all values of an array.

Only one-dimensional arrays are supported.

Multidimensional arrays of form array[x][y] are not supported.

##### Syntax

**&lt;!-- AWP_Start_Array Name='"&lt;DB name&gt;".&lt;array name&gt;' --&gt;**

**... Content of the array, utilized keywords:** 
**ArrayIndex**
 **and** 
**value**
**..**

**&lt;!-- AWP_End_Array --&gt;**

##### Parameter

| Symbol | Meaning |
| --- | --- |
| &lt;Name&gt; | Defines the name of the array whose elements you want to access.   You require the DB name and the name of the array corresponding to the data block structure defined in STEP 7.  The name must be within single or double quotation marks. The DB name is within double quotation marks. |
| &lt;ArrayIndex&gt; | Index of an array element |
| &lt;value&gt; | Value of an array element |

##### Example

The example reads all elements of the "MyArray" structure in the "DB_Name" data blocks of the CPU and displays the index and the values of the tags on the user-defined web page.

![Example](images/51976898571_DV_resource.Stream@PNG-en-US.png)

**&lt;!-- AWP_Start_Array Name='"DB_Name".MyArray' --&gt;**

**Index:** 
**:=ArrayIndex:** 
**Value:** 
**:=value:**

**&lt;!-- AWP_End_Array --&gt;**

The code indicated above generates the following display:

Index: 1 Value: 42

Index: 2 Value: 43

Index: 3 Value: 44

##### Representation of arrays of the data type BOOL with S7-1500

The output of arrays of the type BOOL is always filled to the next full 8 bits. This particular feature only occurs with BOOL arrays.

**Example:**

"DB_1".bitArray is a BOOL array with 5 elements.

&lt;!-- AWP_Start_Array Name='"DB_1".bitArray' --&gt;

:=ArrayIndex: -&gt; :=value:

&lt;!-- AWP_End_Array --&gt;

Output:

0 -&gt; value from "DB_1".bitArray[0]

1 -&gt; value from "DB_1".bitArray[1]

2 -&gt; value from "DB_1".bitArray[2]

3 -&gt; value from "DB_1".bitArray[3]

4 -&gt; value from "DB_1".bitArray[4]

5 &gt; 0

6 &gt; 0

7 &gt; 0

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

#### Using structures (S7-300, S7-400, S7-1500)

The Web server provides user program commands for accessing structures in order to access the values of a PLC tag of data type STRUCT.

##### Syntax

**&lt;!-- AWP_Start_Struct Name='"&lt;DB name&gt;".&lt;struct name&gt;' --&gt;**

**... Content of structure ...**

**&lt;!-- AWP_End_Struct --&gt;**

##### Parameter

| Symbol | Meaning |
| --- | --- |
| &lt;Name&gt; | Defines the name of the structure whose elements you want to access.   You require the DB name and the name of the structure corresponding to the data block structure defined in STEP 7.  The name must be within single or double quotation marks. The DB name is within double quotation marks. |

##### Example

The example reads elements of the "MyStruct" structure in the "DB_Name" data blocks of the CPU and displays the value of the tag on the user-defined web page.

![Example](images/51976893323_DV_resource.Stream@PNG-en-US.png)

**&lt;!-- AWP_Start_Struct Name='"DB_Name".MyStruct' --&gt;**

**:=A:**

**:=B:**

**:=C:**

**&lt;!-- AWP_End_Struct --&gt;**

The code indicated above corresponds to the following commands:

**:="DB_Name".MyStruct.A:**

**:="DB_Name".MyStruct.B:**

**:="DB_Name".MyStruct.C:**

#### Rules for arrays and structures (S7-300, S7-400, S7-1500)

Arrays and structures can be nested.

##### Rules

AWP_Start_Array and AWP_End_Array commands must be used in pairs. They must not be overlapped.

Permissible construction:

AWP_Start_Array

AWP_Start_Struct

AWP_End_Struct

AWP_End_Array

**Non**permissible construction (overlapping):

AWP_Start_Array

AWP_Start_Struct

AWP_End_Array

AWP_End_Struct

#### Definition of fragments (S7-300, S7-400, S7-1500)

##### Fragments

Fragments are "logical sections" of a web page to be processed by the CPU individually.

Fragments are usually complete pages but can also be individual elements such as files (for example, images) or complete documents.

##### Defining fragments

&lt;!-- AWP_Start_Fragment Name="&lt;Name&gt;" [Type="&lt;Type&gt;"] [ID="&lt;Id&gt;"] [Mode=&lt;Mode&gt;]--&gt;

The start of a fragment is specified by this command. A fragment runs to the start of the next fragment or to the end of the file.

- &lt;Name&gt; Indicates the name of the fragment.

  The name must start with a letter [a-zA-Z] or an underscore ( _ ). Letters, underscores or numbers [0-9] can follow after this first character.
- &lt;Type&gt; Indicates the type of the fragment.

  - "manual" The user program is informed of the request for a fragment; the web page to be returned can be changed by the user program.
  - "automatic" The page is automatically processed (default).
- &lt;id&gt; A numeric ID can be stipulated for the fragment. If no ID is assigned, the fragment is automatically assigned an ID. For manual pages (&lt;Type&gt;=manual) , the fragment can be addressed in the user program of the CPU by this ID.

  > **Note**
  >
  > Keep the ID low because the highest ID influences the size of the Web Control DB.
- &lt;Mode&gt; Fragments support the visible and hidden modes.

  - "visible" The fragment is a part of the web page. This mode is preset and can also be omitted.
  - "hidden" The fragment is not part of the web page. However, the fragment will be saved in the Web DB and is available to the user program for inserting in a requested web page. You use an exchange of the fragment ID (Web-Control-DB.fragment_index tag) to insert a "hidden" fragment in the requested web page.

The input document is completely divided into fragments by the "AWP_Start_Fragment" command. "AWP_End_Fragment" is therefore unnecessary.

Without a start fragment command, a file is mapped as a fragment; the fragment name is derived from the file name. If a file is divided into several fragments (by "AWP_Start_Fragment"), the file must begin with the "AWP_Start_Fragment" command.

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)
  
[Enumeration types (S7-300, S7-400, S7-1500)](#enumeration-types-s7-300-s7-400-s7-1500)
  
[Importing fragments (S7-300, S7-400, S7-1500)](#importing-fragments-s7-300-s7-400-s7-1500)

#### Importing fragments (S7-300, S7-400, S7-1500)

You can declare a fragment in an HTML page and import this fragment into other web pages.

##### Example

A company logo is to be displayed on all web pages of a web application.

There is only one instance of the HTML code for the fragment that displays the company logo. You can import the fragment as often and into as many HTML files as required.

##### Syntax

&lt;!-- AWP_Import_Fragment Name = "&lt;name&gt;"--&gt;

- &lt;name&gt; is the name of the fragment to be imported.

##### Example

HTML code within a web page that declares a fragment:

&lt;!-- AWP_Start_Fragment Name = "My_Company_Logo" --&gt;

&lt;p&gt;&lt;img src = "compay_logo.jpg"&gt;&lt;/p&gt;

##### Example

HTML code within another web page that imports the declared fragment:

&lt;!-- AWP_Import_Fragment Name = "My_Company_Logo" --&gt;

---

**See also**

[Definition of fragments (S7-300, S7-400, S7-1500)](#definition-of-fragments-s7-300-s7-400-s7-1500)

### Creating and loading a data block (S7-300, S7-400, S7-1500)

#### Requirement

- All source files required for the web application (*.html, *.js, *.png, ...) have been created.
- The source files are located in one folder, but only those source files that are required for the web application. No other files may be located in this folder.

#### Procedure

To create data blocks from the source files for user-defined web pages in STEP 7, proceed as follows:

1. Select the CPU, for example, in the device configuration.
2. Select the properties for user-defined web pages in the inspector window under "Properties &gt; General &gt; Web server".
3. As "HTML source", select the folder that contains the source files for the web application.
4. Enter the HTMP page to be opened on starting the web application as the start HTML page.
5. Enter a name for the application if required.
6. You can supplement a range of file name extensions as "Files with dynamic content" if necessary. Only enter those file name extensions that also contain AWP commands.
7. The number for the Web Control DB and for the fragment DB start number can be kept as long as they are not already being used by your user program.
8. Click on the "Generate" button to create DBs from the source files.

   The generated data blocks are saved in the project navigation in the "System block" folder (in the "Web server" subfolder).
9. In the CPU, select the network view to be loaded and then select the "Download to device" command in the "Online" menu to download the blocks. Compilation of the blocks is implicitly initiated before downloading.

   If errors are reported during this process, you must correct these errors before you can download the configuration.

#### Tips for generating the web data blocks

When you click on the "Generate blocks" button in the area "Web server &gt; User-defined pages", STEP 7 checks whether the corresponding web data blocks can be generated.

The following causes prevent the generation of web data blocks:

- Length of file names and tag names is too long

  If you have a comprehensive web application with many files and directories, the generation of the web data blocks may possibly fail. If this happens, the generation is aborted with the message "Text list overflow...". The cause is system-internal size limitations for management information saved in the web data block.

  Solution: Use short file names and short tag names.
- Files with dynamic content (file with AWP commands) are too large

  When the files with dynamic content (e.g. *.htm, *.html) are too large (for S7-1500 CPUs, e.g., larger than ca. 64 kB), you will see the following message "WebInt: Unable to read files for web application ..." with information on the file size and the path to the file that causes the error.

  Solution: Use the following AWP command to fragment the file:

  `<!-- AWP_Start_Fragment Name='<Fragmentname>' -->`

  The command divides the file internally into multiple segments that can be processed individually by the CPU.

---

**See also**

[Definition of fragments (S7-300, S7-400, S7-1500)](#definition-of-fragments-s7-300-s7-400-s7-1500)
  
[Importing fragments (S7-300, S7-400, S7-1500)](#importing-fragments-s7-300-s7-400-s7-1500)

### Structure of the PLC program (S7-300, S7-400, S7-1500)

Your user program must call the " WWW" instruction to even allow the web application, for example, the user-defined web pages, to be available to the CPU on the standard web pages and to allow them to be called up there.

The Web Control DB you have created from the source files is the input parameter (CTRL_DB) for the "WWW" instruction. The Web Control DB references the content of the user-defined web pages coded in the fragment DB and then receives status and control information.

#### Calling the "WWW" instruction in the startup program

If you do not want the user program to influence requested web pages, it is sufficient to only call the "WWW" instruction once in a startup OB. This instruction initializes communication between the web server and the CPU.

#### Calling the "WWW" instruction in the cyclic program

The "WWW" instruction can also be called in an OB processed in cycles (for example, OB 1). This has the advantage of being able to respond to web server requests from within the user program. Manual fragments must be used for this.

In this case, you must evaluate information from the Web Control DB in order to identify the requested web page or the requested fragment. On the other hand, you must set a bit in the user program in order to explicitly release the web page to be returned by the web server after processing the web page request.

The structure of the Web Control DB is described in the following section.

### Web Control DB (S7-300, S7-400, S7-1500)

The Web Control DB (DB 333 by default) is created by STEP 7 and contains information on the structure of user pages, the status of communication and any errors that occur.

Additional fragment DBs are also created as well as the Web Control DB. These fragment DBs (there may also only be one fragment DB) are referenced in the Web Control DB. The fragment DBs contain the web pages and media data coded in fragments, for example, images. The content of the fragment DB cannot be changed by the user program. It is created automatically and is only for data management.

The status and control tags of the Web Control DB are accessed via symbols.

The following lists the tags of the Web Control DB required for status evaluation and to control interaction.

The Web Control DB provides two types of information:

- Global status information: Not bound to a concrete web page request.
- Request status and control information: Information about queued requests.

#### Global status information

| Symbol | Meaning |
| --- | --- |
| "WEB-Control_DB".commandstate.init | Activates and initializes the web application. |
| "WEB-Control_DB".commandstate.deactivate | Deactivates the web application. |
| "WEB-Control_DB".commandstate.inititializing | The web application is initialized (read Web Control DB, etc.). |
| "WEB-Control_DB".commandstate.error | Web application could not be initialized. The reason is coded in "WEB-Control_DB".commandstate.last_error . |
| "WEB-Control_DB".commandstate.deactivating | The web application is closed. |
| "WEB-Control_DB".commandstate.initialized | The web application has been initialized and is ready. |
| "WEB-Control_DB".commandstate.last_error | Refer to the next table for a value table of possible errors. |

| Last_error | Description |
| --- | --- |
| 1 | Fragment DB is inconsistent (does not match the Web Control DB). |
| 2 | A web application already exists with this name. |
| 3 | Memory problem initializing in the web server. |
| 4 | Inconsistent data in the Web Control DB. |
| 5 | A fragment DB is not available (not loaded). |
| 6 | No AWP ID for a fragment DB. |
| 7 | The enum fragment is not available (contains the texts and information on the enum types). |
| 8 | An action requested via the command flag in the Web Control DB is prohibited in the current state. |
| 9 | Web application is not initialized (if there is no reinitializing after disabling). |
| 10 | Web server is disabled. |
| ... | Last_error is reset once the web application has been successfully initialized. |

#### Request status information

Request status information is bound to one of four possible requests, x = [1 … 4].

| Symbol | Meaning |
| --- | --- |
| "WEB-Control_DB".requesttab[x].idle | Nothing need be done. |
| "WEB-Control_DB".requesttab[x].waiting | The user program must react to a request from a manual fragment and explicitly initiate further processing in the web browser. |
| "WEB-Control_DB".requesttab[x].sending | The web server is occupied with processing the request/fragment. |
| "WEB-Control_DB".requesttab[x].aborting | The TCP connection is closed by the web server. |

#### Request control information

Request control information is bound to one of four possible requests, x = [1 … 4].

| Symbol | Meaning |
| --- | --- |
| "WEB-Control_DB".requesttab[x].continue | Releases the fragment being processed for transmission. Processing of the next fragment is initiated. |
| "WEB-Control_DB".requesttab[x].repeat | Releases the fragment being processed for transmission. The fragment is then processed again. |
| "WEB-Control_DB".requesttab[x].abort | Closes the TCP connection. |
| "WEB-Control_DB".requesttab[x].finish | Releases the fragment being processed for transmission. Stops further processing of requests (terminates the request). |

#### Example:

The tag for the DB is: "WEB-Control_DB". Whether errors have occurred during initialization of the web application can be determined by requesting bit "WEB-Control_DB".commandstate.error in the user program.

If an error has occurred you can analyze it using the "WEB-Control_DB".commandstate.last_error value.

### Interaction with the user program (S7-300, S7-400, S7-1500)

With the help of manual fragments, you can make sure that the user program reacts synchronously to browser entries so that the returned website can be prepared by the user program.

#### Fragment type

To react directly to the received data in the user program, the "manual" fragment type (for "manual sites") must be used for the fragment that the data writes:

&lt;!-- AWP_Start_Fragment Name="testfrag" ID="1" Type="manual" --&gt;

The values are always transferred to the Web server of the CPU for automatic and manual pages in the same way:

Example:

&lt;form method="POST" action=""&gt;  
&lt;p&gt;  
&lt;input type="submit" value="Set new value"&gt;  
&lt;input type="text" name='"Velocity"' size="20"&gt;  
&lt;/p&gt;  
&lt;/form&gt;

#### User program for manual fragments

In the CPU user program, the "WWW" (SFC 99) instruction must be cyclically opened with the usage of manual sites.

To react to the values entered in the browser, it is required to evaluate the request that the manual site places for the Web server in the user program. The web-control-DB (for example, DB 333) must investigate pending requests to do this. The array that manages four requests is contained in the "requesttab" section of the Web Control DB. Each element of the array contains information about the respective request in a structure.

A simple AWL program example shows how pending requests are checked provided the variables from the web-control-DB.

U "WEB-Control_DB".requesttab[1].waiting

JCN R2

L "WEB-Control_DB".requesttab[1].fragment_index

L 1

JU PdRq // request pending

R2: U "WEB-Control_DB".requesttab[2].waiting

JCN R3

L "WEB-Control_DB".requesttab[2].fragment_index

L 2

JU PdRq // request pending

R3: U "WEB-Control_DB".requesttab[3].waiting

JCN R4

L "WEB-Control_DB".requesttab[3].fragment_index

L 3

JU PdRq // request pending

R4: U "WEB-Control_DB".requesttab[4].waiting

JCN NoRq

L "WEB-Control_DB".requesttab[4].fragment_index

L 4

JU PdRq // request pending

NoRq: L 0

T #frag_index

T #req_index

JU Exit

PdRq: T #req_index

POP

T #frag_index

Exit: BE

If there is a request present, this AWL program section writes the fragment ID in the variable #frag_index and the request number (value range 1-4) in the variable #req_index.

With this information, the information transferred in the request can now be processed in the AWL program for each fragment ID separately (for example, plausibility check).

If the processing of the request by the AWL program is complete, the request must be answered and the corresponding entry under "requesttab" from the web-control DB (for example, DB 333) must be reset.

A simple AWL program example for answering requests:

SET

L #req_index

SPL Con0

JU Con0

JU Con1

JU Con2

JU Con3

JU Con4

Con0: JU Exit

Con1: = "WEB-Control_DB".requesttab[1].continue

JU Exit

Con2: = "WEB-Control_DB".requesttab[2].continue

JU Exit

Con3: = "WEB-Control_DB".requesttab[3].continue

JU Exit

Con4: = "WEB-Control_DB".requesttab[4].continue

JU Exit

Exit: BE

#### Principle sequence of a browser request with interaction from the user program

The following figure shows the simplified, principle sequence of the web browser request on the effects of Web Control DB content and the actions required from the user program until the processed web page is returned (response).

![Principle sequence of a browser request with interaction from the user program](images/20975357451_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

### Displaying custom web pages in the browser (S7-300, S7-400, S7-1500)

#### Display web pages in browser

Web pages are called from the standard web pages of the web browser.

In addition to the other links in the navigation bar, the standard web pages also have a link to "user pages".

Click on the "user pages" link to open the web browser you have configured as the default HTML page.

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

### Create multilingual user defined websites (S7-300, S7-400, S7-1500)

You have the possibility to provide your user-defined websites in the different languages.

#### Requirements

The language-dependent HTML sites will be filed in a folder structure that contains the following language abbreviations:

![Requirements](images/21150777483_DV_resource.Stream@PNG-de-DE.png)

#### Defined language abbreviations

The language abbreviations "de", "en", "fr", "es", "it" and "zh-CHS" are defined. Other language folders or other language folders labeled differently are not supported.

If needed, you can create more folders in the same folder hierarchy for other files; for example, an "img" folder for images and a "script" folder for Java script files.

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

### Language switching for custom web pages (S7-300, S7-400, S7-1500)

#### Requirements

The HTML pages are contained in the predefined language folders, for example, HTML pages with German text are in the "de" folder, HTML pages with English text are in the "en" folder.

#### Language switching concept

Language switching is based on a predefined cookie named "siemens_automation_language". If the cookie is set to value "de", at the next web page request or web page update, the web server switches to the web page from the "de" folder.

Similarly, the web server switches to the web page from the "en" folder when the cookie is set to "en".

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

### Example of a language switch (S7-300, S7-400, S7-1500)

The example is designed as follows:

- In both language folders "de" and "en", you will find the language-dependent HTML files with the same names, for example, "langswitch.html". The text displayed within the two files is in German or English corresponding with the folder name.
- Additionally, there is a folder "script" in the folder structure in which the Java script file "lang.js" is located. Functions are stored in this file that are required for the language switch.

#### Design of the "langswitch.html" file ("de" folder)

The meta data "Content-Language", charset and path to the Java script file are set in the header of the file.

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"&gt;

&lt;html&gt;

&lt;head&gt;

&lt;meta http-equiv="Content-Language" content="de"&gt;

&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8"&gt;

&lt;title&gt;Language Switch German Site&lt;/title&gt;

&lt;script type="text/javascript" src="script/lang.js" &gt;&lt;/script&gt;

&lt;/head&gt;

In the body of the file, the language selection occurs with the help of the HTML element "select". The select element activates a selection list and contains the options "de", labeled with "German" and "en", labeled with "English"; "de" is preselected.

With the help of the event handler "onchange", the function "DoLocalLanguageChange(this)" is opened. The "this" parameter transfers the select-object with the selected option to this function. "onchange" executes the option to open the function upon each change.

&lt;!-- Language Selection --&gt;

&lt;table&gt;

&lt;tr&gt;

&lt;td align="right" valign="top" nowrap&gt;

&lt;!-- change language immediately on change of the selection --&gt;

&lt;select name="Language" onchange="DoLocalLanguageChange(this)" size="1"&gt;

&lt;option value="de" selected &gt;German&lt;/option&gt;

&lt;option value="en" &gt;English&lt;/option&gt;

&lt;/select&gt;

&lt;/td&gt;

&lt;/tr&gt;

&lt;/table&gt;

&lt;!-- Language Selection End--&gt;

#### Design of the file "langswitch.html" (folder "en")

The header of the HTML file with English text is designed analog to the HTML file with German text.

&lt;!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"&gt;

&lt;html&gt;

&lt;head&gt;

&lt;meta http-equiv="Content-Language" content="en"&gt;

&lt;meta http-equiv="Content-Type" content="text/html; charset=utf-8"&gt;

&lt;title&gt;Language switching english page&lt;/title&gt;

&lt;script type="text/javascript" src="script/lang.js" &gt;&lt;/script&gt;

In the body of the file, the language selection occurs with the help of the HTML element "select". In contrast to the German HTML file, the English option is preselected and the text and labels are in English.

&lt;!-- Language Selection --&gt;

&lt;table&gt;

&lt;tr&gt;

&lt;td align="right" valign="top" nowrap&gt;

&lt;!-- change language immediately on change of the selection --&gt;

&lt;select name="Language" onchange="DoLocalLanguageChange(this)" size="1"&gt;

&lt;option value="de" &gt;German&lt;/option&gt;

&lt;option value="en" selected &gt;English&lt;/option&gt;

&lt;/select&gt;

&lt;/td&gt;

&lt;/tr&gt;

&lt;/table&gt;

&lt;!-- Language Selection End--&gt;

#### Design of the "lang.js" file (in the "script" folder)

The "DoLocalLanguageChange" function is defined in the Java script file, which opens the "SetLangCookie" function with the language selection value. SetLangCookie combines the cookie name and cookie value and sets the cookie through the corresponding document.cookie property. To make the web server react to the setting of cookies with the display of the desired language, the website must be reloaded (top.window.location.reload).

function DoLocalLanguageChange(oSelect) {

SetLangCookie(oSelect.value);

top.window.location.reload();

}

function SetLangCookie(value) {

var strval = "siemens_automation_language=";

// this is the cookie by which the web server

// detects the desired language

// this name is required by the web server

strval = strval + value;

strval = strval + "; path=/ ;";

// set path to the application, since otherwise

// path would be set to the requesting page would not get the cookie

/*

use expiration if this cookie should live longer

than the current browser session

var now = new Date();

var endttime = new Date(now.getTime() + expiration);

strval = strval + "; expires=" + endttime.toGMTString() + ";";

*/

document.cookie = strval;

}

---

**See also**

[Additional information and sample applications (S7-300, S7-400, S7-1500)](#additional-information-and-sample-applications-s7-300-s7-400-s7-1500)

### Additional information and sample applications (S7-300, S7-400, S7-1500)

#### Information and examples for user-defined pages

Examples and further explanations are available in the Siemens Industry online support.

- You can find the function manual for the Web server of an S7-1500 CPU [here](http://support.automation.siemens.com/WW/view/en/62046437?Datakey=47071380).
- An example for accessing the Web server of an S7-1200 using an iPad and for integrating the jQuery library is available [here](http://support.automation.siemens.com/WW/view/en/62046437?Datakey=47071380).
- An application example for the creation of a user-defined web page is available [here](http://support.automation.siemens.com/WW/view/en/58862931).
- A description of the options for updating user-defined web pages with HTML5 code or JavaScript is available [here](http://support.automation.siemens.com/WW/view/en/62543256).
- An overview of the topic of industrial security is available [here](http://support.automation.siemens.com/WW/view/en/50203404).

#### Simple examples for special applications

For the features described above, we provide you with documented examples with sample HTML pages and - depending on the application - with corresponding TIA project/user program; see [here](https://support.industry.siemens.com/cs/ww/en/view/68011496).

Apart from basic descriptions and projects, you will also find simple examples for the Web server of SIMATIC S7-1200/S7-1500.

---

**See also**

[S7-1500 web server](http://support.automation.siemens.com/WW/view/en/59193560)

### Using source files for web server user-defined pages in STEP 7 (TIA Portal) (S7-300, S7-400, S7-1500)

During migration of STEP 7 projects, the sources for the web server user-defined pages, such as HTML pages and graphics, are not automatically applied to the new project in the TIA Portal.

After the migration, you must integrate the sources of your user-defined pages in your project. Proceed as follows:

1. Copy the source data to a directory that can be accessed by the TIA Portal.
2. Enter the paths to the source files in the CPU properties under "Web server &gt; User-defined pages".
3. Then compile the hardware configuration.
