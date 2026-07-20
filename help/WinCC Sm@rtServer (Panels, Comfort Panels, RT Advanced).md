---
title: "WinCC Sm@rtServer (Panels, Comfort Panels, RT Advanced)"
package: WebFeaturesWCCAenUS
topics: 81
devices: [Comfort Panels, Panels, RT Advanced]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Sm@rtServer (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics (Panels, Comfort Panels, RT Advanced)](#basics-panels-comfort-panels-rt-advanced)
- [Remote control via Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#remote-control-via-smrtserver-panels-comfort-panels-rt-advanced)
- [E-mail notification from runtime (Panels, Comfort Panels, RT Advanced)](#e-mail-notification-from-runtime-panels-comfort-panels-rt-advanced)
- [Display integrated Service-Pages (Panels, Comfort Panels, RT Advanced)](#display-integrated-service-pages-panels-comfort-panels-rt-advanced)
- [Access via SIMATIC HMI HTTP Protocol (Panels, Comfort Panels, RT Advanced)](#access-via-simatic-hmi-http-protocol-panels-comfort-panels-rt-advanced)
- [Connection to the Office-world (Panels, Comfort Panels, RT Advanced)](#connection-to-the-office-world-panels-comfort-panels-rt-advanced)

## Basics (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Sm@rt Options (Panels, Comfort Panels, RT Advanced)](#smrt-options-panels-comfort-panels-rt-advanced)
- [Application scenarios (Panels, Comfort Panels, RT Advanced)](#application-scenarios-panels-comfort-panels-rt-advanced)
- [HMI devices suitable for use (Panels, Comfort Panels, RT Advanced)](#hmi-devices-suitable-for-use-panels-comfort-panels-rt-advanced)
- [Settings for Sm@rt Options (Panels, Comfort Panels, RT Advanced)](#settings-for-smrt-options-panels-comfort-panels-rt-advanced)
- [Settings for remote control (Panels, Comfort Panels, RT Advanced)](#settings-for-remote-control-panels-comfort-panels-rt-advanced)
- [Use and restrictions of Sm@rt Options (Panels, Comfort Panels, RT Advanced)](#use-and-restrictions-of-smrt-options-panels-comfort-panels-rt-advanced)
- [Setting up secure communication between WebClient and Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#setting-up-secure-communication-between-webclient-and-smrtserver-panels-comfort-panels-rt-advanced)

### Sm@rt Options (Panels, Comfort Panels, RT Advanced)

#### Introduction

Using the Sm@rt Options from WinCC, you can communicate between HMI-systems or to an HMI-System by means of TCP/IP-connections (e.g.LAN).

> **Note**
>
> The Sm@rt options are not supported by PCs with multi-touch operation.

#### Use of the Sm@rt Options

- Distributed operator stations with Sm@rtClients for controlling large machines or machines that are spread out over a large area.
- Operator stations with system-wide access to current process data via the communication driver "SIMATIC HTTP Protocol".
- Local servicing solution for the central archiving, analysis and additional processing of process data.
- Provision of current process data for higher-level systems (SCADA, production management systems, office applications).
- Remote control of an HMI-System by means of Internet, Intranet and LAN.
- Sending of E-Mails on the basis of messages and events
- Provisioning of Standard-HTML-Pages in HMI-system with service-and maintenance information as well as diagnostic functions.
- Easy download of files from the Web browser on the Panel with the "Save as" browser command.

User benefits:

- Flexible solution for access to HMI systems and process data from any location
- Reduction of load on the field bus:

  For example, the combination of WinCC Runtime and SIMATIC panels enables a factory control system to have access to process data. No load is placed by the factory level on the sensitive field level with respect to the necessary communication requirements. These requirements are handled by HMI Runtime along with the SIMATIC-panels.
- Expensive on-site service visits to be avoided by using the remote control. Unplanned non-operation periods are reduced and the system productivity is increased.

  > **Note**
  >
  > On devices with version V12, the password "100" is preset for the Sm@rtServer and for the integrated Web server. This password should be changed for security reasons.
  >
  > On devices with version V13, no passwords are preset.

### Application scenarios (Panels, Comfort Panels, RT Advanced)

#### E-Mailing and remote diagnostics

A factory has a service contract with an external service company. The HMI device and the service technician's PC are linked together over a TCP/IP-ready network. E-mail delivery of certain alarms to the service technician was configured in the project. The service technician accesses the HMI device via the Internet and executes remote diagnostics.

![E-Mailing and remote diagnostics](images/8405953931_DV_resource.Stream@PNG-en-US.png)

#### Application example:

Amongst other things,flow rates are measured in the process control of a cooling unit. Contamination in a feed line reduces the flow of coolant. When the flow rate drops below the configured threshold value, the operating device displays a warning. In addition,this warning is also dispatched as an e-mail to the assigned service technician.

The service technician then establishes a connection with the remote device and takes the appropriate actions.

Advantage: An alarm that reaches the service technician in a timely manner helps to minimize unplanned downtime.

#### Distributed operator stations

Distributed operator systems, the Sm@rtClients are used for controlling large machines or machines that are spread out over a large area.

The Client-HMI device connects to Sm@rtServer via the Sm@rtClient-Display.

The operator can operate and monitor the system from various locations. The operator sees the same image at each operator station, whereby only one station can be operated at one point of time.

The type of operation is also named as a coordinated operation. Then you must change the configuration only at Sm@rtServer.

#### Access to the tags via SIMATIC HMI HTTP Protocol

#### Operator stations with system-wide access

For use of the SIMATIC HMI HTTP Protocol, you can provide tags of HMI-device (HTTP-Server) to another device (HTTP-Client).

Thus the local as well as centrally used HMI-systems have access to the tags of other stations. Cell-concepts or line-concepts can be simply implemented. De-centrally obtained information is available centrally.

This concept also permits the setting of cost-effective and small central servicing. There are additional options for archiving, analysis and additional processing of registered process data, if a PC is used for that.

#### Remote monitoring and remote control- servicing solution

If you connect the use of the SIMATIC HMI HTTP Protocol and the Sm@rtServer with each other, you can implement a complex servicing solution.

For this,display the interested tags of the HMI-devices on the Service-PC. If necessary, use the PC for the remote monitoring and remote control of a specific HMI-device.

The locally used HMI-devices are connected with each other and the total process is controlled comprehensively.

The concept of the remote servicing is possible by using the Sm@rtClient-Display in the servicing HMI-Application. The operator has access to the respectively desired local HMI-device through flexible configuration of the Sm@rtClient-Display.

#### Connection to the Office-world

The possibility of data exchange exists between HMI-device and office-applications, e.g. MS Excel, with help of VBA-Macro.

For this, the HMI-device must support the Web-Service(SOAP). A script or macro is called in the external application, which has only read or write access to the concerned tags according to provided syntax.

### HMI devices suitable for use (Panels, Comfort Panels, RT Advanced)

#### HMI devices suitable for use

The following table shows the HMI-devices that are suitable for the use of Sm@rt Options.

The number of the connections based on "SIMATIC HMI HTTP Protocol" and the number of maximum connected Sm@rtClients depends on the HMI-device. For additional information see the "Performance features" documentation and in the technical manual of your HMI-device.

Technical data subject to change.

| HMI device | Sm@rt Options |
| --- | --- |
| KTP700 Mobile Panel  KTP900 Mobile Panel | Yes |
| KTP400F Mobile Panel  KTP700F Mobile Panel   KTP900F Mobile Panel | Yes |
| Comfort Panels | Yes |
| WinCC Runtime Advanced | Yes |

#### Combining options on panels

The following table shows which options and functions on the panels can be combined with each other.

Technical data subject to change.

|  | SIMATIC HMI HTTP Protocol | Sm@rt Options | HTML browser |
| --- | --- | --- | --- |
| **SIMATIC HMI HTTP Protocol** | -- | Yes | Yes |
| **Sm@rtServer** | Yes | -- | No |
| **HTML browser** | Yes | No | -- |

---

**See also**

[Use and restrictions of Sm@rt Options (Panels, Comfort Panels, RT Advanced)](#use-and-restrictions-of-smrt-options-panels-comfort-panels-rt-advanced)
  
[Configuration (Panels, Comfort Panels, RT Advanced)](#configuration-panels-comfort-panels-rt-advanced-2)

### Settings for Sm@rt Options  (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuration in WinCC (Panels, Comfort Panels, RT Advanced)](#configuration-in-wincc-panels-comfort-panels-rt-advanced)
- [Configurations on the HMI device (Panels, Comfort Panels, RT Advanced)](#configurations-on-the-hmi-device-panels-comfort-panels-rt-advanced)

#### Configuration in WinCC (Panels, Comfort Panels, RT Advanced)

##### Introduction

In the "Runtime-Settings" Editor, configure the requirements for using the Sm@rt Options.

As an alternative, configure the settings in the Control Panel of the HMI-device.

Note that the settings on the HMI device have a higher priority than the settings in the WinCC project.

##### Open

Double-click on the "Runtime-settings" entry in the project tree. In the "Runtime-settings" editor, click on the "Services".

![Open](images/129155294987_DV_resource.Stream@PNG-en-US.png)

##### "Remote control" Group.

Enter the settings for the selected HMI device in the work area:

- "Remote control" Group.

  - Start Sm@rtServer

    Configures the HMI device as Sm@rtServer.

##### "Read/write tags" group for Panels

- Operate as OPC server

  Configures the HMI device as an OPC server.
- HTTP channel server

  Configures the HMI device as HTTP server.
- Web service SOAP

  Activates tag access via SOAP.

##### "Read/write tags" group for Comfort Panels

- Operate as OPC UA server

  Configures the HMI device as an OPC UA server.
- HTTP channel server

  Configures the HMI device as HTTP server.
- Web service SOAP

  Activates tag access via SOAP.

##### "Read/write tags" group for RT Advanced

- Operate as OPC server

  - OPC DCOM server

    Configures the HMI device as an OPC DCOM server.
  - OPC UA server

    Configures the HMI device as an OPC UA server.
- HTTP channel server

  Configures the HMI device as HTTP server.
- Web service SOAP

  Activates tag access via SOAP.

##### "Diagnostics" Group

- HTML pages

  Activates service pages of the HMI device.

##### "SMTP Communication" Group

Activates service pages of the HMI device. "SMTP Communication" Group

- Server name

  Enter the name of the SMTP server through which you want to send E-mails.
- Port

  Enter the port number. The SMTP port number depends on the outgoing mail server of your service provider. You can obtain the port number from your service provider.
- Sender name

  Enter the sender name. The recipient sees in the E-Mail from which device the E-mail originates, e.g. "HMI device Production line 2". If the function is not supported by the SMTP-Server, delete the entry. You can obtain more detailed information for this from your service provider.
- E-mail address

  If you use an SMTP server that requires a valid e-mail address for authentication, enter it here, for example, "John.Doe@gmx.net.
- Login

  If you use an SMTP server that requires a user name for authentication, enter it here. You can obtain the user name from your service provider.
- Password

  If you are using an SMTP server that requires a password for authentication, enter this password. You can obtain the user name from your service provider.
- The server requires a secure connection (SSL).

  The data are sent via an SSL connection. Your service provider can tell you if your mail server supports an SSL connection.

#### Configurations on the HMI device (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Settings on the HMI device (Panels, Comfort Panels, RT Advanced)](#settings-on-the-hmi-device-panels-comfort-panels-rt-advanced)
- [WinCC Runtime Advanced Internet, "Email" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-email-tab-panels-comfort-panels-rt-advanced)
- [WinCC Runtime Advanced Internet, "Proxy" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-proxy-tab-panels-comfort-panels-rt-advanced)
- [WinCC Runtime Advanced Internet, "Web Server" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-web-server-tab-panels-comfort-panels-rt-advanced)
- [WinCC Runtime Advanced Internet, "Remote" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-remote-tab-panels-comfort-panels-rt-advanced)
- ["Sm@rtServer Settings" dialog (Panels, Comfort Panels, RT Advanced)](#smrtserver-settings-dialog-panels-comfort-panels-rt-advanced)
- [User administration for web server (Panels, Comfort Panels, RT Advanced)](#user-administration-for-web-server-panels-comfort-panels-rt-advanced)

##### Settings on the HMI device (Panels, Comfort Panels, RT Advanced)

###### Introduction

The Sm@rt Options settings in the HMI device are configured in the dialog box "WinCC Runtime Advanced Internet".

Additional tabs may be included in the dialog "WinCC Runtime Advanced Internet". This depends on which options are activated for the network operation in the project.

Note that the settings on the control unit have a higher priority than the settings in the WinCC-project.

###### Tabs

You have opened the dialog "WinCC Runtime Advanced Internet" with the symbol "WinCC Runtime Advanced Internet" ![Tabs](images/9232729995_DV_resource.Stream@PNG-de-DE.png).

The "WinCC Runtime Advanced Internet" dialog of the control panel can contain the following tabs:

- [WinCC Runtime Advanced Internet, "Email" tab](#wincc-runtime-advanced-internet-email-tab-panels-comfort-panels-rt-advanced)
- [WinCC Runtime Advanced Internet, "Proxy" tab](#wincc-runtime-advanced-internet-proxy-tab-panels-comfort-panels-rt-advanced)
- [WinCC Runtime Advanced Internet, "Web Server" tab](#wincc-runtime-advanced-internet-web-server-tab-panels-comfort-panels-rt-advanced)
- [WinCC Runtime Advanced Internet, "Remote" tab](#wincc-runtime-advanced-internet-remote-tab-panels-comfort-panels-rt-advanced)

###### Input area plan

At Sm@rtServer and Sm@rtClient, the same input area plan must be set.

The Sm@rtServer uses the Standard-Input area plan of the operating system: (Start>Settings>Control Panel> Country settings>Tab "Entry"). These changes become effective after system restart.

At Sm@rtClient, the same input area plan must be set like at Sm@rtServer. No restart is necessary after the switchover of input area plan at Sm@rtClient.

##### WinCC Runtime Advanced Internet, "Email" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

Specifies the settings for the E-Mailing.

###### Settings

- SMTP server

  - Use the default of project file

    The SMTP-Server name from the WinCC-Project is used.
  - Enter the name of the SMTP server through which you want to send E-mails.
  - Port

    Enter the port number. The SMTP port number depends on the outgoing mail server of your service provider. You can obtain the port number from your service provider.
- Name

  - Name of sender

    Enter the sender name. The receipient sees in the E-Mail, from which device the E-mail originates, e.g. "HMI device Production line 2".

    If the function is not supported by the SMTP-Server, delete the entry. You can obtain more detailed information for this from your service provider.
  - eMail Address of sender

    If you use an SMTP server that requires a valid e-mail address for authentication, enter it here, for example, "John.Doe@gmx.net.

**Dialog "**
**Advanced Email Settings**
**"**

- Authentication

  - Use the default of project file

    The user name and password from the WinCC project are used.
  - Disable authentication

    Authentication is not required.
  - Use panel settings for authentication

    The settings of the HMI-device are used. Enter the user name under "Login" and the password under "Password". You can obtain the user name and password from your service provider.
- Encryption

  - Use the default of project file

    The setting from the WinCC-Project is used.
  - Enable SSL

    The user data and e-mail are encrypted for transmission.
  - Disable SSL

    The user data and e-mail are sent un-encrypted.

---

**See also**

[Settings on the HMI device (Panels, Comfort Panels, RT Advanced)](#settings-on-the-hmi-device-panels-comfort-panels-rt-advanced)

##### WinCC Runtime Advanced Internet, "Proxy" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog box

Settings for utilizing the Proxy-Server.

> **Note**
>
> Enter the Proxy-Server in "Internet Options" at PC.

###### Settings

- Use proxy server

  Activate the "Use Proxy Server" if access is given in your network via Proxy-server.
- Proxy

  Enter the name or the address of the proxy-server.
- Port

  Enter the port of the proxy-server.

##### WinCC Runtime Advanced Internet, "Web Server" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

The following is configured:

- The utilization of the integrated web server and of the HTTP-Server
- User and user web authorizations

###### Settings

**Tag access**

Governs the access to tags via the "SIMATIC HMI HTTP protocol":

- "Read/write": Read and write access
- "Read only": Read access only

**Tag authenticate**

Governs the authentification in case of access to variables via the SIMATIC HMI HTTP Protocol":

- "No authentication": No authentication is required for access.
- "Authentication required": Authentication is required for access.

  You specify the user name and password when configuring the "SIMATIC HMI HTTP Protocol" communication driver.

**Enable Remote-Transfer for Projects** 
**(DELETE)**

This setting enables remote transfer of project files.**(DELETE)**

**Deny RSA key exchange**

Rejects the RSA key exchange.

If the communication partner requires an RSA key exchange, you can allow this procedure by deactivating the "Deny RSA key exchange" option in the Internet settings of the integrated web server.

**Start automatically after booting**

(on panel only)

The web server is automatically started after the HMI device boots. As a result, the web server is utilized independent of the runtime.

> **Note**
>
> **Start web server automatically on PC**
>
> Add a link with the program "Miniweb.exe" in the Autostart-Organizer in order to start the web server automatically after the PC starts. The program is located in the installation index of runtime.

**Close with Runtime**

The web server is closed along with Runtime.

**User Administration**

After entering the password, the "UserDatabase-Edit". dialog opens. The "UserDatabase-Edit" dialog is the [user administration of the web server](#user-administration-for-web-server-panels-comfort-panels-rt-advanced).

**Start Webserver**

Starts the web server.

**Close Webserver**

Ends the web server.

##### WinCC Runtime Advanced Internet, "Remote" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

Settings for the Sm@rtServer

###### Settings

**Start automatically after booting**

The Sm@rtServer is automatically started after the HMI device boots. Otherwise the Sm@rtServer starts together with the Runtime.

**Close with runtime**

The Sm@rtServer is closed together with Runtime.

**Change settings**

Opens the "Sm@rtServer Settings" dialog for specifying the passwords, authorizations, the screen update mechanism and the behavior when connections are terminated.

> **Note**
>
> This dialog is titled "Sm@rtServer: Default Local System Properties" on the panel.

The dialog contains the following tabs:

- ["Server" tab](#server-tab-panels-comfort-panels-rt-advanced)
- ["Polling" tab](#polling-tab-panels-comfort-panels-rt-advanced)
- ["Display" tab](#display-tab-panels-comfort-panels-rt-advanced)
- ["Query" tab](#query-tab-panels-comfort-panels-rt-advanced)
- ["Administration" tab](#administration-tab-panels-comfort-panels-rt-advanced)
- ["Certificates" tab](#certificates-tab-panels-comfort-panels-rt-advanced)

**Start Remoting**

Starts the Sm@rt Server explicitly.

**Stop Remoting**

Ends the Sm@rt Server explicitly.

##### "Sm@rtServer Settings" dialog (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- ["Server" tab (Panels, Comfort Panels, RT Advanced)](#server-tab-panels-comfort-panels-rt-advanced)
- ["Polling" tab (Panels, Comfort Panels, RT Advanced)](#polling-tab-panels-comfort-panels-rt-advanced)
- ["Display" tab (Panels, Comfort Panels, RT Advanced)](#display-tab-panels-comfort-panels-rt-advanced)
- ["Query" tab (Panels, Comfort Panels, RT Advanced)](#query-tab-panels-comfort-panels-rt-advanced)
- ["Administration" tab (Panels, Comfort Panels, RT Advanced)](#administration-tab-panels-comfort-panels-rt-advanced)
- ["Certificates" tab (Panels, Comfort Panels, RT Advanced)](#certificates-tab-panels-comfort-panels-rt-advanced)

###### "Server" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

Specifying passwords, web authorizations and the disconnection.

###### **Incoming connections**

Settings for handling an attempt to establish a connection.

- Accept socket connections

  This setting enables the connection to the HMI device. It is a basic requirement for using the Sm@rtServers from the outside.

  If this check box is deactivated, no remote monitoring and no remote control is possible.
- Encrypt communication

  Allows an encrypted connection between Sm@rtClient and Sm@rtServer.
- Password 1

  First password for remote access. "View only" is disabled by default.
- Password 2

  Second password for remote access. "View only" is enabled by default.

  This password can be provided as a reserve password for third-party users (such as service technicians); it can be modified when necessary without significant effort within the organization.
- View only

  If this check box is enabled, read access (monitoring mode) is the only access available when the corresponding password is entered.

  Default: Enabled

  > **Note**
  >
  > On devices with version V12, the password "100" is preset for the Sm@rtServer and for the integrated Web server. This password should be changed for security reasons.
  >
  > On devices with version V13, no passwords are preset.

###### **Enable network packets queuing (slower)**

This setting enables splitting of data into multiple data packets, which are sent separately over the network. It is useful when multiple clients are connected.

###### **Display or port numbers to use**

Here, you select the TCP/IP port in the network where the Sm@rtServer waits for attempts to establish a connection.

- "Auto": The Sm@rtServer automatically searches for the appropriate port by itself.
- "Display": The server uses port 5900 plus display number. For HTTP, the server utilizes Port 5800 plus display number.
- "Ports": You enter the port numbers for "main" and "HTTP" yourself.

###### **No local input during client session**

The keyboard and mouse on the server-HMI device are disabled as long as connections are active.

For example, this setting is useful when an HMI device is being administered from outside.

###### **Remove desktop wallpaper** (on PC only)

This setting removes the screen background on the PC, thus saving transmission effort.

Default: Enabled

###### **When last client disconnects** (on PC only)

This setting governs the behavior after disconnection of the last client connection:

- "Do nothing": No reaction
- "Lock workstation": Server PC is locked.
- "Logoff workstation": Server PC is logged off.

The latter two settings are only useful if the Sm@rtServer is running as a service.

---

**See also**

[WinCC Runtime Advanced Internet, "Remote" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-remote-tab-panels-comfort-panels-rt-advanced)

###### "Polling" tab  (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

Specifying the screen update and the use of virtual graphics driver.

###### **Polling modes**(on PC only)

The settings govern the screen update.

Most changes are recognized automatically by the server. In case of problems, you can enter additional settings here.

The update method cannot be set on the panel. The settings is always "Poll Full Screen".

- Poll foreground window (On PC only)

  Updates the current window.

  It increases the load on the server.
- Poll window under cursor (On PC only)

  Updates the window that is located under the mouse cursor. The window is updated when a change occurs in the operator control element under the mouse cursor.

  Default: Enabled
- Poll full screen (On PC only)

  This setting specifies an update each time the screen changes. This setting provides you the lowest display error but places a maximum load on the server.
- Polling cycle

  Determine the suitable setting for your configuration. Make sure that the selected update cycle is not too short, since it affects the computer load.

###### **Window polling**

- Poll console windows Only (On PC only)

  This setting specifies an additional update when changes occur in a console window (MS input requirement).
- Poll on event received only (Only on the PC)

  This setting specifies an additional update each time an entry is made.

  Default: Enabled
- Mirror driver status

  (Only on the PC with a mirror driver installed)

  Provides information about the status of the virtual graphics driver.

###### **Mirror driver options** (only on a PC with installed mirror driver)

Enable direct access to display driver's mirror screen

The shared-memory area of the virtual graphics driver is used for the display. The setting improves the performance.

###### **Troubleshooting** (on PC only)

- Don't use VNCHooks.DLL while polling full screen

  VNCHooks.dll is used by default for the screen update. If VNCHooks.dll causes problems when using other program, select this setting.
- Don't use mirror display driver even if available

  (Only on the PC with a mirror driver installed)

  Use this setting only for troubleshooting.

---

**See also**

[WinCC Runtime Advanced Internet, "Remote" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-remote-tab-panels-comfort-panels-rt-advanced)

###### "Display" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

Setting of the screen display.

###### **Sharing area**(on PC only)

- Full desktop

  The entire desktop of the server is accessed.
- Primary display

  The main screen of the multi-monitor configuration is displayed.

###### **Downscale to**(on PC only)

Scales the screen to be transferred according your inputs. Servers with Windows CE ignore this setting.

---

**See also**

[WinCC Runtime Advanced Internet, "Remote" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-remote-tab-panels-comfort-panels-rt-advanced)

###### "Query" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

Settings for incoming connection attempts.

> **Note**
>
> This dialog is titled "Default Local System Advanced" on the panel.

###### **Query settings**

These settings govern acceptance of incoming attempts to establish a connection.

- Query console on incoming connections

  The Sm@rtServer registers the incoming attempts to establish a connection and displays a dialog on the screen in which the connection attempt is accepted or rejected.
- Query timeout

  Set the waiting time.
- Default action

  Select the response to an attempt to establish a connection once the waiting time expires:

  - "Refuse": Reject attempt (operator control mode - single mode)
  - "Accept": Accept attempt (operator control mode – shared mode)

###### **Allow option to accept without authentication**

The dialog for handling attempts to establish connections also contains the button "Accept without password" . This gives you the option to accept an attempt to establish connection without a password.

---

**See also**

[WinCC Runtime Advanced Internet, "Remote" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-remote-tab-panels-comfort-panels-rt-advanced)

###### "Administration" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

Specifications for session management.

> **Note**
>
> This dialog is titled "Default Local System Advanced" on the panel.

###### Administration

- Disable empty passwords

  Select this check box in order to allow an empty "Password 1".

  Default: Enabled
- Allow loopback connections

  This setting allows connections to your own HMI device. It is useful and necessary when security software is used for secure (encoded) connections.
- Allow only loopback

  This setting allows only connections to your own HMI device.

###### Logging

- Log info to SmartServer.log

  (On the panel: Log information to file)

  This setting writes information to the server logbook.
- Log detailed debugging information

  This setting writes expanded information to the server logbook (for locating errors).

With HMI devices operating with Windows CE, the log is only created when the MMC card is inserted. If the MMC card is inserted, the log is created directly on the card.

The log files are created in the following path on a PC: C:\Documents and Settings\All Users\Application Data\Siemens\HmiRTm

###### Forced write access

This setting governs forced access in an emergency contrary to normal session management.

- Password needed

  If this check box is not selected, every operator can force access in emergencies as follows:

  - Pressing the <Shift> key four times
  - Clicking four times
  - Touching the screen four times

  If this check box is selected, an attempt must be made to gain access and a password must also be entered to force access.

  In this case, enter the applicable password in the input box underneath. If a password is not entered, it is not possible to force access in an emergency.

  Default: Enabled

  > **Note**
  >
  > On the server, access can only be forced by pressing the <Shift> key four times, clicking four times, or touching the screen four times.

###### HTTP-Server

- Enable built-in HTTP server

  If this check box is activated, the Java-Applet is automatically downloaded on the PC when the connection is first established.

  The Java applet accesses the Java VM that is installed on the client and enables remote monitoring and remote control using Internet Explorer.

  Default: Enabled
- Enable applet params in URLs

  Forwards all parameters of the URL to the Sm@rtClient application.
- https

  If this check box is selected, the Java applet is downloaded securely.

  Default: Enabled

###### Connection priority

These settings govern handling of attempts to establish a connection by non-shared clients.

- Disconnect existing connections

  When an attempt is made to establish a connection by a non-shared client, the attempt is accepted; the existing connections are disconnected (single mode).
- Automatic shared sesssions

  When an attempt is made to establish a connection by a non-shared client, the attempt is accepted; the prior existing connections are retained. Access is controlled using session management in shared mode.

  Default: Enabled
- Active user timeout

  For shared mode, enter the time that must elapse without any actions on the active HMI device before access can be changed.

  Default setting: 10 seconds
- Refuse concurrent connections

  If a non-shared client is already connected to the server, attempts to establish a connection by other non-shared clients are rejected.

---

**See also**

[WinCC Runtime Advanced Internet, "Remote" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-remote-tab-panels-comfort-panels-rt-advanced)
  
[Remote control by means of web browser (Panels, Comfort Panels, RT Advanced)](#remote-control-by-means-of-web-browser-panels-comfort-panels-rt-advanced)

###### "Certificates" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog

The "Certificate" tab shows you all security certificates and their properties.

You can also import and delete security certificates.

###### Selection

In the "Selection" list, select a certificate with the properties you want to view.

- You can use the "Delete" button to delete the selected certificate.
- You can use the "Import" button to import the selected certificate.

The "Import" button is active if the entry "Imported Certificate" is selected.

###### Certificate

You see the following certificate properties in the "Certificate" area:

- Issued to: Name of the organizational unit for which the certificate was issued
- Issued by: Name of the certificate issuer
- Valid from... to: The validity period of the certificate
- Thumbprint: The fingerprint of the certificate

---

**See also**

[Configuring a separate certificate for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-a-separate-certificate-for-smrtserver-panels-comfort-panels-rt-advanced)

##### User administration for web server  (Panels, Comfort Panels, RT Advanced)

###### Introduction

Different web authorizations for the operation and monitoring are allocated to the users in the user administration.

###### Requirement

- The "WinCC Runtime Advanced Internet" dialog is open.
- The "Web Server" tab is displayed.

###### Entries and settings

Click "User Administration" in the "Web Server" tab and enter the password.

> **Note**
>
> On devices with version V12, the password "100" is preset for the Sm@rtServer and for the integrated Web server. This password should be changed for security reasons.
>
> On devices with version V13, no passwords are preset.

The "UserDatabase-Edit" dialog is opened.

The "UserDatabase-Edit" dialog has three tabs:

- Tab "User Manager"

  User administration for creation or deletion of users.

  Create a new user using "New"; Delete a user using "Remove". The recreation and deletion become effective using "Apply".
- Tab "Description"

  You can store a description of or comments on the users selected on the "User Manager" tab.
- Tab "Authorizations"

  Specify the web authorizations for the users selected on the "User Manager" tab. You use "Add" to activate a web authorization and "Remove" to deactivate one.

  By default, the password is initially preset to "100" and all web authorizations are granted to users with "Administrator" rights.

  For read and write access to the file browser, the user must possess the web authorizations "FileBrowserAdministrator" and "FileBrowserUser".

  > **Note**
  >
  > In principle, every user who has access to the control panel can manage users and web authorizations. If necessary, protect the control panel from unwanted access.

###### List of web authorizations

The following web authorizations exist:

| Web authorization | Authorized for: |
| --- | --- |
| UserData | Import and export of recipes |
| UserAdministrator | Import and export of password lists |
| RuntimeAccess | Starting and stopping of runtime |
| Engineering | HTTP transfer from ES to the target device |
| FileBrowserUser | Read access to the file browser |
| FileBrowserAdministrator | Read/write access to the file browser |
| RTCommunication | Utilization of the SIMATIC HMI HTTP server |
| SoapUser | Read/write access via web service (SOAP) |

---

**See also**

[Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)](#setting-wincc-runtime-advanced-internet-panels-comfort-panels-rt-advanced-1)

### Settings for remote control (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Session management for remote control (Panels, Comfort Panels, RT Advanced)](#session-management-for-remote-control-panels-comfort-panels-rt-advanced)
- [Configuring Sm@rtServer for remote control (Panels, Comfort Panels, RT Advanced)](#configuring-smrtserver-for-remote-control-panels-comfort-panels-rt-advanced)
- [Configure Sm@rtClient for remote control (Panels, Comfort Panels, RT Advanced)](#configure-smrtclient-for-remote-control-panels-comfort-panels-rt-advanced)
- [Touch mode (Panels, Comfort Panels, RT Advanced)](#touch-mode-panels-comfort-panels-rt-advanced)
- [Sm@rtClient-Application (Panels, Comfort Panels, RT Advanced)](#smrtclient-application-panels-comfort-panels-rt-advanced)

#### Session management for remote control  (Panels, Comfort Panels, RT Advanced)

##### Introduction

WinCC enables remote monitoring and remote control of HMI devices over a TCP/IP-ready network such as a LAN or the Internet. Remote monitoring and remote control is implemented in different ways:

- Remote control by means of Internet Explorer
- Remote control by means of the Sm@rtClient-application
- Remote control by means of the Sm@rtClient-display in

Only one device can ever have access to the HMI-device. Which device is permitted access is determined by the session management.

##### Session management options

Session management is used to control access. The client-server connection can be in one of two modes:

- Monitoring mode
- Control mode

##### Monitoring mode

If the client accesses the server in monitoring mode, the operator can see the current screen of the HMI device and track all changes. He can monitor the server but cannot operate.

In the monitoring mode, all the keys on the client retain their standard functions.

If remote control was started from the Sm@rtClient display, the operator uses the <Tab> key or the cursor keys to go to the next object in the current screen of the client project.

##### Control mode

If the client accesses the server in operator control mode, the operator can use the mouse and the keyboard to control the server from the client. If an access attempt is made from another client, the assignment of operating permission depends on the settings at the server and at the clients.

In operator control mode, the client keys act on the server screen. Thus, the operator uses the <Tab> key to go to the next object in the current screen of the project running on the server.

If remote control was started from the Sm@rtClient display, the operator can only go to another object or screen in the project on the client by using an additionally configured function or an additional menu command. The operator to this menu command as follows:

- On the Touch-device, in which he touches the screen longer than 1 sec.
- On the keyboard =device, in which he masks on the menu with <Shift+Control> and operates it with <Alt> and the keyboard.

In both operating modes, the Sm@rtServer is set so that the operator at the remotely controlled device, the server, can be prevented from performing any activities.

In an emergency, the operator can exact the user rights on a remotely controlled HMI device as well as on an inactive HMI device. If no password is specified, the operator must click the user interface four times consecutively, touch the screen four times consecutively, or press the <Shift> key four times consecutively. If a password is specified, the operator must click once or press a key on the client and then enter the specified password.

##### Settings for session management

You make settings for session management on the server and on the client in the Control Panel "WinCC Internet Settings".

#### Configuring Sm@rtServer for remote control (Panels, Comfort Panels, RT Advanced)

##### Introduction

The Sm@rtServer has an internal security concept based on passwords and special settings for session management.

##### Security concept for the Sm@rtServer

Remote monitoring and remote control of the Sm@rtServer from the Sm@rtClient is protected by two functions:

- Encrypt encryption of communication to the server
- Passwords

##### Encrypt communication to the Sm@rtServer

The "Encrypt communication" function provides a secure connection between Sm@rtClient and Sm@rtServer.

After you have activated the "Encrypt communication" function, the Sm@rtServer sends a Sm@rtServer-specific certificate to the Sm@rtClient.

The Sm@rtClient must support the "Encrypt communication" function for encrypted communication.

The certificate sent by the Sm@rtServer must be accepted to establish communication on the Sm@rtClient.

All connections between Sm@rtClient and Sm@rtServer are then only possible on the basis of the exchanged certificate.

##### Passwords for the Sm@rtServer

Remote monitoring and remote control of the Sm@rtServer from the Sm@rtClient is protected by two passwords.

The second password is used as a further password for additional access, for example, as a service password.

> **Note**
>
> **Passwords for the Sm@rtServer**
>
> No passwords have been preset.
>
> Therefore, assign the passwords before you use the Sm@rtServer.

> **Note**
>
> **Password assignment in fail-safe Mobile Panels 2nd Generation**
>
> To prevent accidental write access, the option "Disable empty passwords" is enabled by default and cannot be changed. Enter two new passwords under "Password 1" and "Password 2". Enter one of the two passwords for access to the Sm@rtServer.

##### Settings on the Sm@rtServer

The settings on the server govern which remote operators can access the runtime of the server.

The passwords for access are set on the server. Open "WinCC Runtime Advanced Internet" in the control panel. On the "Remote" tab, click "Change Settings". In the "Server" tab of the subsequent dialog, enter the passwords of the Sm@rtClient. For both passwords, you can use "View only" to set the monitoring mode and to exclude control mode.

On the panel, this dialog is called "Sm@rtServer: Default Local System Properties" and contains fewer dialog elements than the dialog on the PC.

##### Control mode

To enable control mode, the "View only" check box must be cleared, at least for "Password 1" (Password 1).

![Control mode](images/85467517963_DV_resource.Stream@PNG-de-DE.png)

The manner in which the individual remote control station can access the server is set on the "Administration" tab.

![Control mode](images/85467521803_DV_resource.Stream@PNG-de-DE.png)

- "Disconnect existing connections"

  When an access attempt is made by an non-shared client, the previous connection is automatically disconnected and control is transferred to the new client.

  When an attempt is made to access by a shared client, the behavior is the same as described for "Automatic shared sessions".
- "Automatic shared sessions"

  When an access attempt is made, control is transferred to the new client.

  The condition for transferring control is that no action has been undertaken by the previously active client for a period of time (in seconds) as specified in the "Active user timeout" setting.
- "Refuse concurrent connections"

  When an attempt is made to access by a non-shared client, this access attempt is rejected so long as the operator station that currently has access is still connected to the server.

  When an attempt is made to access by a shared client, the behavior is the same as described for "Automatic shared sessions".

##### Disabling local operator control of the server

To do so, open the "WinCC Internet Settings" in the Control Panel. On the "Remote" tab, click "Change Settings". On the "Server" tab in the subsequent dialog, select "No local input during client session".

##### Password for forced access

A password can be specified in "Forced Write Access" for forced access in an emergency.

##### Sm@rtServer as a service

You can let the Sm@rtServer run as a service. The operator can then also access the service-HMI device from the client-HMI device, for example, when the screen saver with password becomes active.

Select the check box "Start automatically after booting" in "WinCC Runtime Advanced Internet" on the "Remote" tab.

##### Sm@rtServer as service in Windows

The Sm@rtServer always runs as a service under Windows. You cannot stop the Sm@rtServer in Runtime with the Notification Area in the taskbar. You have the following options for stopping the Sm@rtServer:

- Stop using the "ControlSmartServer" system function

  Configure the "ControlSmartServer" system function to a button, for example. Select the "Stop" mode at the system function. You can stop the Sm@rtServer in Runtime by clicking the button.
- Stopping the Sm@rtServer in the Control Panel:

  Open "WinCC Runtime Advanced Internet" in the Control Panel and select the "Remote" tab. Click on the "Stop" button. Sm@rtServer is stopped.
- Stopping Sm@rtServer by stopping Runtime:

  Open "WinCC Runtime Advanced Internet" in the Control Panel and select the "Remote" tab. Activate the "Close with Runtime" option. The Sm@rtServer is stopped at the stop of Runtime.

---

**See also**

[Configuring secure communication for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-secure-communication-for-smrtserver-panels-comfort-panels-rt-advanced)
  
[Touch mode (Panels, Comfort Panels, RT Advanced)](#touch-mode-panels-comfort-panels-rt-advanced)

#### Configure Sm@rtClient for remote control (Panels, Comfort Panels, RT Advanced)

##### Settings on the client PC

- Monitoring mode

  At the client-PC you limit the connection to observation mode, if required. This allows you to prevent unintended control operations.

  - If connection is via the Sm@rtClient application

    In the following "Sm@rtClient Connection" of Sm@rtClient-application, click "Options..." button.

    In the "Sm@rtclient Options" dialog, select the setting"View only (inputs ignored)".
  - If connection is via Internet Explorer

    Click on the button "Options..." and select "View only" in the subsequent dialog.
- Layout

  You can also specify whether or not the HMI-device is to be displayed with the same layout in the Sm@rtClient application. This is useful if you access from a PC on a touch device. In order to suppress the layout, select the "Sm@rtclient Options" setting in the "Suppress Device Layout" dialog.

  In addition, you can use "Scale by" to zoom in or out of the layout. To use "Scale by", the Suppress Device Layout setting must be selected or the HMI-device must not supply any layout. Otherwise, the desktop is always displayed with a zoom setting of 100%.

  > **Note**
  >
  > If you scale the display, the performance may be impaired in some situations:
  >
  > - Strong scaling, for example from 1600 x 1200 px to 640 x 480 px.
  > - Scaling with non-matching scaling factors, for example from a 4:3 resolution to 16:10 resolution.

##### Configuring of the Sm@rtClient-display

You can configure the Sm@rtClient display in different ways, and thereby set certain inputs: The server name, the password for accessing Sm@rtServer or the restriction to the monitoring mode.

##### Encrypted communication

You must enable the "Encrypt communication" function for encrypted communication with the Sm@rtServer.

- Support for the "Encrypt communication" function on the Sm@rtClient

  If the Sm@rtClient does not support the "Encrypt communication" function, no communication is possible with a Sm@rtServer which has enabled the "Encrypt communication" function.

  Enable the "Encrypt communication" function on the Sm@rtServer.
- Enabling the "Encrypt communication" function on the Sm@rtServer by the Sm@rtClient

  You can also enable the "Encrypt communication" function on the Sm@rtServer from the Sm@rtClient:

  - Establish a connection to the server.
  - Enable the "Encrypt communication" function in the "Standard VNC Authentication" dialog.
  - Certificates are exchanged between the Sm@rtServer and Sm@rtClient.
  - The certificate sent by the Sm@rtServer must be accepted by the Sm@rtClient.

#### Touch mode (Panels, Comfort Panels, RT Advanced)

##### Overview

Depending on your project requirements, it may be necessary to completely disable the operation of capacitive multi-touch PCs or resistive touch PCs while these are connected to the HMI devices over Sm@rtServer or Sm@rtClient.

Multi-touch PCs are disabled for basic inputs with "No local input during client session" as long as they are connected to an HMI device.

To also prevent gestures, you must also block the "Extended Touch" functionality or switch the device to single-touch mode.

A device on which a Sm@rtServer is running can be remotely operated by a Sm@rtClient installed on an HMI device. "Duplicate operations" in which inputs can be made on the server and the client device simultaneously, are prevented with the "No local input during client sessions" option.

However, this option only blocks basic keyboard and mouse operation. Gestures are still possible on the server device. To disable these as well, proceed as follows depending on the hardware used.

##### Switching off touch mode on PCs with resistive display

1. Open the IPC wizard on the server device in the Windows Start menu with the command "All Programs > UPDD > Settings".
2. Under "Click Mode", disable the "Extended Touch" option.

##### Switching off touch mode on capacitive multi-touch PCs

1. Open "IPC Wizard > Panel Configuration Center" (version 2.1 or higher).

   All recognized devices are displayed under "Panel Configuration Center > Touch settings". The set touch mode is also displayed for each device.
2. To change the touch mode of a device, click the respective "Switch Mode" button.

The touch mode of the device changes accordingly to single-touch mode.

> **Note**
>
> Operate those multi-touch PCs that cannot be switched to single-touch mode (e.g. ITP1000) in "View only" mode only.
>
> To do so, enable the setting "View only (inputs ignored)" in the "Sm@rtClient Options" dialog.

---

**See also**

[Configuring Sm@rtServer for remote control (Panels, Comfort Panels, RT Advanced)](#configuring-smrtserver-for-remote-control-panels-comfort-panels-rt-advanced)

#### Sm@rtClient-Application (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Dialog "New Sm@rtServer: Connection" (Panels, Comfort Panels, RT Advanced)](#dialog-new-smrtserver-connection-panels-comfort-panels-rt-advanced)
- ["Options" dialog, "Connections" tab (Panels, Comfort Panels, RT Advanced)](#options-dialog-connections-tab-panels-comfort-panels-rt-advanced)
- ["Options" dialog, "Globals" tab (Panels, Comfort Panels, RT Advanced)](#options-dialog-globals-tab-panels-comfort-panels-rt-advanced)

##### Dialog "New Sm@rtServer: Connection" (Panels, Comfort Panels, RT Advanced)

###### Introduction

This dialog opens when you click the "Sm@rtClient" button in the taskbar.

###### Purpose of the dialog box

This dialog is used for selecting the server and the connection method.

**Sm@rtServer:**

Enter the address of the server to which the connection is to be established. You can find the various options for entering the address under "[Remote control by means of the Sm@rtClient application](#remote-control-by-means-of-the-smrtclient-application-panels-comfort-panels-rt-advanced) ".

**Connection profil**

Select the type of connection to the server according to the network you are using.

**Listening mode**

If you enable this function, the Sm@rtClient application is minimized and appears as a button in the Windows taskbar. The Sm@rtClient waits for the Sm@rtServer to establish a connection. To establish the connection, click the "Sm@rtServer" button in the Windows taskbar of the server. Select "Add new client" in the context menu.

**Options**

The "Sm@rtClient Options" dialog containing the technical settings for the Sm@rtClient-application is displayed.

---

**See also**

[Remote control by means of the Sm@rtClient application (Panels, Comfort Panels, RT Advanced)](#remote-control-by-means-of-the-smrtclient-application-panels-comfort-panels-rt-advanced)
  
["Options" dialog, "Globals" tab (Panels, Comfort Panels, RT Advanced)](#options-dialog-globals-tab-panels-comfort-panels-rt-advanced)
  
["Options" dialog, "Connections" tab (Panels, Comfort Panels, RT Advanced)](#options-dialog-connections-tab-panels-comfort-panels-rt-advanced)

##### "Options" dialog, "Connections" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog box

Technical settings for the Sm@rtClient-application are specified in this dialog box.

Only change the settings here in special cases.

> **Note**
>
> You can also specify these settings in the Java Applet. Note that some of the dialog elements are named differently there.

**Format and encodings**

Settings for compressing (encoding) the screen data of the server.

- Use encoding

  Preassigned based on the selection under "Connection profile".

  Select the desired compression or "Raw" (no compression).
- User 8-bit color

  (Only in the Java-Applet): Reduces the color depth at the client to 8 bits (256 colors). The data are then transferred faster. However, incorrect colors may result.
- Custom Compression level

  Allows individual customizing of the compression level in the "Level" input field:

  1 = least compression (faster); 9 = maximum compression (slower).
- Allow JPEG compression

  Allows the use of JPEG compression (involves losses).

  Enter the "Screen quality" in the input field underneath:   
  1 = least compression (faster); 9 = maximum compression (slower).
- Allow CopyRect encoding

  (In the Java-Applet: Use CopyRect. Encoding)

  Allows compression while using "similar rectangles".

**Restrictions**

- Viewonly (inputs ingnored)

  Sets the view mode for this client irrespective of the settings on the server.
- Disable clipboard transfer

  Disables the clipboard that is used to transfer data from one PC to another. Applies only to the copying and pasting of texts.

  This functionality is not available at a Windows CE server.

**Display**

Settings for the screen display

- Scale by

  Zooms in or zooms out the desktop to be displayed. To use "Scale by", the Suppress Device Layout setting must be selected or the HMI-device must not supply any layout. Otherwise, the desktop is displayed with a zoom setting of 100%.
- Fullscreen Mode

  Displays the desktop to be shown in full-screen mode. If the server screen is larger than the screen of the client, it is scrolled automatically by the mouse movement.
- Suppress Device Layout

  In the Sm@rtClient application window, the entire layout of remote HMI-device is not shown.
- Use CTRL + Cursor Key for Scrolling

  The key combinations <CTRL> + cursor key are used to scroll within the local screen. They are no longer transferred to the server.

**Mouse**

(In the Java-Applet: Mouse buttons 2 and 3)

Settings for the evaluation of mouse actions

- Emulate 3 Buttons (with 2-button click)

  Emulation of a three-button mouse by a two-button mouse.
- Swap mouse buttons 2 and 3

  (In the Java-Applet: reversed/normal)

  Mouse buttons 2 and 3 are swapped.

**Mouse cursor**

(In the Java-Applet: Cursor shape updates)

Settings for the display of the cursor

Select the type of transfer of the mouse actions:

- Track remote cursor locally

  The information on the location of the cursor is transferred separately from the screen information. This speeds up the transfer of the cursor. (JavaApplet: Enabled)
- Let remote server deal with mouse cursor

  Tracks the server cursor to the client cursor. This allows more accurate cursor positioning. (YES: Ignore)
- Don't show remote cursor

  The cursor at the server is not included in the transfer. (YES: Disable)

**Request shared session**

(In the Java-Applet: Share desktop)

Declares this client to be a non-exclusive client.

---

**See also**

[Dialog "New Sm@rtServer: Connection" (Panels, Comfort Panels, RT Advanced)](#dialog-new-smrtserver-connection-panels-comfort-panels-rt-advanced)

##### "Options" dialog, "Globals" tab (Panels, Comfort Panels, RT Advanced)

###### Purpose of the dialog box

Technical settings for the Sm@rtClient-application are carried out in this dialog box.

Only change the settings here in special cases.

> **Note**
>
> You can also carry out these settings in the Java Applet. Note that some of the dialog elements are named differently there.

**Interface options**

- Show toolbars by default

  Displays the toolbar.
- Warn at switching to the full-screen mode

  Outputs a message before the full-screen mode is activated.
- Enable Onscreen keyboard

  Enables the display of the on-screen keyboard
- Number of connection to remember

  The client creates a list of the recently used connections. This setting specifies the number of connections listed.
- Clear the list of saved connections

  The list is cleared.

**Local cursor shape**

Specifies the appearance of the local cursor. This allows you to better differentiate between the local cursor and remote cursor.

**Listening mode**

- Accept reverse VNC connections on TCP port

  Specifies the TCP port number. The Sm@rtClient waits for the Sm@rtServer to establish the connection over this TCP port number.

**Logging**

- Write log to a file

  Writes information in the logbook of the Sm@rtClient-application.
- Verbosity level

  Writes expanded information to the server logbook of the Sm@rtClient-application (for locating faults). The amount of detail in the information is dependent on the verbosity level setting.

### Use and restrictions of Sm@rt Options (Panels, Comfort Panels, RT Advanced)

#### Use restrictions

While using the Sm@rt Options, observe the following instructions:

- HMI devices suitable for use

  For additional information, refer to "[Usable HMI devices](#hmi-devices-suitable-for-use-panels-comfort-panels-rt-advanced)".
- Sm@rtServer and Sm@rtClient

  - If a PC is used as a Sm@rtServer, select the highest-performance platform available.
  - Use only simple projects.
  - Avoid photographs and color gradients in screens.
  - Avoid heavy background loads during operation, for example, those from user-defined functions or logs.
  - The number of the maximum connected Sm@rt Clients depends on the Server-HMI device. For additional information, see the "Performance features" documentation.
  - To improve the performance of the Sm@rtServer, you can disable hardware acceleration of the graphics card .
  - When a PC with a touchscreen accesses a Sm@rtServer client, the following applies to the touch operation of the Sm@rtClient:

    Standard touch operation such as clicking or scrolling in lists is possible, but touch gestures and events such as "Press" and "Release" are not supported.
  - You inevitably loose performance at the HMI when you access the HMI-device using the Sm@rtClient functionality.
- SIMATIC HMI HTTP Protocol

  - Tag exchange via the SIMATIC HMI HTTP Protocol is not suitable for exchanging bulk data.
  - The maximum number of connections depends on the HMI device: For additional information, see the "Performance features" documentation
- Access protection

  To protect access to an HMI device using different passwords, use the first password for protected access and the second password for unprotected access; for example, remote control with password and remote monitoring without password.
- Port

  The web server connects to the network at the port 80. To run it without problems, make sure port 80 is not in use by any other application, such as IIS World Wide Web Publishing Service.
- Integrated HTML-pages

  - The size of the HTML pages must not exceed 100 Kb in case of Windows CE. In case of exceeding of the given value, these pages are spooled on external storage media.
  - If you display tags on HTML-pages using the entry type "Cyclic on use", it can lead to data-inconsistency.
- E-mailing

  The E-mailing function is not suitable for the mass dispatch of E-Mails. It is meant for sending important messages.
- Timeout

  If the connection between server and client is interrupted, the server will register this disconnection only with a certain delay. The delay is based on the Windows standard configuration of TCP/IP Timeout.
- Communication between WebClient and Sm@rtServer

  Java is no longer supported by future browser versions.

  In these cases, use the following alternatives as Sm@rtClient:

  - Sm@rtClient.exe
  - Sm@rtClient app for smartphones

#### Use-requirements in the company network

In order to implement the mentioned scenario, the accesses to the company network must be enabled. If the company network is protected by a Firewall, the system administrator must release the appropriate ports for that.

- Access to the integrated HTML-pages

  The web server connects to the network at the port 80.
- Access to Sm@rtServer for downloading the Java-Applet using the Internet Explorer

  The Sm@rtServer is connected to the network at the Port 5800 for downloading the Java-applet.
- Access to the Sm@rtServer using the Internet Explorer for remote monitoring and remote control

  The Sm@rtServer is connected to the network at the port 5900.

  > **Note**
  >
  > If you change the ports of the Sm@rtServer you must customize the links in the used Html-pages accordingly. More information to modify the Html-pages is provided in "Example: Configure integrated webserver".

#### Use in fail-safe 2nd Generation Mobile Panels

If the Sm@rtServer on an HMI device is enabled by a local user, an operator can control and monitor the HMI device over a Sm@rtClient from outside the plant.

Note the following information when using the Sm@rtServer option on fail-safe 2nd Generation Mobile Panels.

> **Note**
>
> **The Sm@rtServer function needs to be taken into consideration in the risk analysis for fail-safe automation systems.**
>
> Sufficient protection from potential risks is be ensured if the use of the Sm@rtServer is not taken into account in the risk analysis.
>
> A risk analysis that takes account of the Sm@rtServer function is required for each fail-safe automation system. This also applies if the Sm@rtServer function is used subsequently in an existing system. It is the plant operator's responsibility to conduct the risk analysis.

> **Note**
>
> **Rules for the hazardous area**
>
> To avoid injury and damage in the hazardous area, the local operator may only enable the Sm@rtServer function on an HMI device if the following conditions are met:
>
> - The local operator can see the hazardous area.
> - The local operator is able to recognize risks to persons in time.
> - The local operator is capable of taking immediate action to avoid hazards.
> - There are no people in the hazardous area.
>
> It is the plant operator's responsibility to ensure compliance with these conditions.

You can find more information on using Sm@rtServer on fail-safe 2nd Generation Mobile Panels in the manual for the HMI device.

---

**See also**

[HMI devices suitable for use (Panels, Comfort Panels, RT Advanced)](#hmi-devices-suitable-for-use-panels-comfort-panels-rt-advanced)

### Setting up secure communication between WebClient and Sm@rtServer (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring secure communication for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-secure-communication-for-smrtserver-panels-comfort-panels-rt-advanced)
- [Configuring a separate certificate for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-a-separate-certificate-for-smrtserver-panels-comfort-panels-rt-advanced)
- [Installing self-signed Sm@rtServer certificates in Internet Explorer (Panels, Comfort Panels, RT Advanced)](#installing-self-signed-smrtserver-certificates-in-internet-explorer-panels-comfort-panels-rt-advanced)
- [Installing self-signed Sm@rtServer certificates in Firefox (Panels, Comfort Panels, RT Advanced)](#installing-self-signed-smrtserver-certificates-in-firefox-panels-comfort-panels-rt-advanced)
- [Configuring secure communication on the WebClient (Panels, Comfort Panels, RT Advanced)](#configuring-secure-communication-on-the-webclient-panels-comfort-panels-rt-advanced)

#### Configuring secure communication for Sm@rtServer (Panels, Comfort Panels, RT Advanced)

##### Introduction

You can configure secure communication for the communication between Sm@rtServer and WebClient.

Before secure communication can be configured, a number of settings in the "Sm@rtServer Settings" dialog are required and the security certificate needs to be installed in your Web browser.

To open the "Sm@rtServer Settings" dialog, click the "Change settings" button in the "WinCC Runtime Advanced Internet" dialog.

You can use either a self-signed, automatically generated certificate or a separate certificate for secure communication.

The Java applet can also be downloaded to the Sm@rtServer over the WebClient with secure communication.

##### Principle

The following steps are required to configure secure communication:

- Enable the "Encrypt communication" option on the Sm@rtServer.

  Alternatively, you can enable the "Secure" option on the login Website in the WebClient.
- In the "Sm@rtServer Settings" dialog on the "Administration" tab, go to "HTTP-Server" and enable the "https" function.
- Import separate certificate or automatically generated, self-signed certificate.
- Install the self-signed certificate the first time a connection is established.

> **Note**
>
> In V14 and higher, "https" is disabled by default and therefore has no impact when older versions are upgraded to V14 and higher versions.

If the "https" check box is cleared, the user can decide in the WebClient whether to upload the Java applet over http or https by specifying "http" or "https" in the URL.

> **Note**
>
> The security certificate for the Sm@rtServer is located in the Windows certificate store. No certificates can be exported on the HMI devices.

The certificate name is as follows: <IP address>.

> **Note**
>
> If you update to Sm@rtServer V14 or higher, the Sm@rtClients must confirm the certificates again.

---

**See also**

[Installing self-signed Sm@rtServer certificates in Internet Explorer (Panels, Comfort Panels, RT Advanced)](#installing-self-signed-smrtserver-certificates-in-internet-explorer-panels-comfort-panels-rt-advanced)
  
[Installing self-signed Sm@rtServer certificates in Firefox (Panels, Comfort Panels, RT Advanced)](#installing-self-signed-smrtserver-certificates-in-firefox-panels-comfort-panels-rt-advanced)
  
[Configuring a separate certificate for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-a-separate-certificate-for-smrtserver-panels-comfort-panels-rt-advanced)
  
[Configuring secure communication on the WebClient (Panels, Comfort Panels, RT Advanced)](#configuring-secure-communication-on-the-webclient-panels-comfort-panels-rt-advanced)

#### Configuring a separate certificate for Sm@rtServer (Panels, Comfort Panels, RT Advanced)

##### Principle

For secure communication between Sm@rtServer and WebClient, you can use either automatically generated, self-signed certificates, or separate certificates**.**

You save the separate certificates beforehand in the SmartServer.pfx or SmartServer.p12 file. On HMI devices with Windows CE, this file is saved under \flash\simatic; on PCs, it is saved under \ProgramData\Siemens\CoRtHmiRTm\SmartServer.

You then import the certificate to the certificate store using the "Sm@rtServer" dialog and install the corresponding client certificate in your Web browser.

##### Importing separate certificates

1. Open the "Sm@rtServer" dialog.
2. Enable the "Certificate" tab.
3. Click the "Import" button.

   The SmartServer.pfx file is deleted after import. The certificates are stored in the certificate store on the HMI device under My Certificates and on the PC under WinCC Panel RT VNC Service.

> **Note**
>
> In the "Sm@rtServer" dialog on the "Certificate" tab, you can view both automatically generated and imported certificates and their attributes.

---

**See also**

["Certificates" tab (Panels, Comfort Panels, RT Advanced)](#certificates-tab-panels-comfort-panels-rt-advanced)
  
[Installing self-signed Sm@rtServer certificates in Internet Explorer (Panels, Comfort Panels, RT Advanced)](#installing-self-signed-smrtserver-certificates-in-internet-explorer-panels-comfort-panels-rt-advanced)
  
[Configuring secure communication for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-secure-communication-for-smrtserver-panels-comfort-panels-rt-advanced)
  
[Installing self-signed Sm@rtServer certificates in Firefox (Panels, Comfort Panels, RT Advanced)](#installing-self-signed-smrtserver-certificates-in-firefox-panels-comfort-panels-rt-advanced)

#### Installing self-signed Sm@rtServer certificates in Internet Explorer (Panels, Comfort Panels, RT Advanced)

##### Procedure

The following procedure has been tested and released for Internet Explorer 10.

The first time a connection to Sm@rtServer is established, Internet Explorer reports a problem with the Website's security certificate.

1. Select the "Continue to this website (not recommended)" option.

   The "Security Warning" dialog appears.
2. In the "Security Warning" dialog, click "Continue".
3. Click "Certificate error" in the Internet Explorer address bar.
4. Click on the "View certificates" button.

   The "Certificate" dialog appears.
5. Click on the "Install Certificate" button.
6. Select the certificate store "Trusted Root Certification Authorities" for installation of the Sm@rtServer certificate.

   Once you have installed the certificate, you can export it from the certificate store and install it on other PCs with WebClients for connection to the same Sm@rtServer.

---

**See also**

[Configuring a separate certificate for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-a-separate-certificate-for-smrtserver-panels-comfort-panels-rt-advanced)
  
[Configuring secure communication for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-secure-communication-for-smrtserver-panels-comfort-panels-rt-advanced)

#### Installing self-signed Sm@rtServer certificates in Firefox (Panels, Comfort Panels, RT Advanced)

##### Procedure

The following procedure has been tested and released with Firefox 31.8.

At least Java Version 8 Update 51 must be installed in Firefox for use of the Java applet.

> **Note**
>
> Please note that in some browsers self-signed certificates are classified as untrustworthy. To avoid this, install your own certificate from a recognized certification body.

The first time a connection to Sm@rtServer is established, Firefox reports a problem with the Website's security certificate.

1. In the "This connection is untrusted" dialog, click the "Add exception" button.

   The "Add security exception" dialog appears.
2. In the "Add security exception" dialog, click "Get certificate".
3. Then click "View"

   The "Certificate Viewer" dialog appears.
4. In the "Certificate Viewer" dialog on the "Details" tab, select the certificate and click "Export".
5. Click "Close".
6. Click on the "Confirm security exception" button.
7. Open the Java Control Panel using the Control Panel.
8. On the "Security" tab, click the "Manage certificates" button.

   The "Certificates" dialog opens.
9. In the "Certificates" dialog, import the exported certificates under certificate type "Secure Site CA".

   The import can also be executed on other PCs with WebClients for connection to the same Sm@rtServer.

---

**See also**

[Configuring secure communication for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-secure-communication-for-smrtserver-panels-comfort-panels-rt-advanced)
  
[Configuring a separate certificate for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-a-separate-certificate-for-smrtserver-panels-comfort-panels-rt-advanced)

#### Configuring secure communication on the WebClient (Panels, Comfort Panels, RT Advanced)

##### Basics

You can also configure secure communication with the Sm@rtServer on the login page of the WebClient. When the "Secure" option is enabled, the Sm@rtServer and WebClient communicate securely. The "Secure" option is enabled by default.

> **Note**
>
> When the "Secure" option is enabled, the Sm@rtServer and WebClient communicate securely even if secure communication has not been set for the Sm@rtServer.

> **Note**
>
> **Certificate comparison**
>
> The result of the certificate comparison between Sm@rtServer and WebClient is displayed in the "Thumbprint" field on the login page.
>
> If the login page has been saved as a Website in htm or html format and is then accessed with a double-click, the fingerprint is checked. The fingerprint of the Sm@rtServer certificate is checked against the fingerprint that is saved in the htm file. The "Thumbprint" field is displayed in green if the two match and in red if they do not.

---

**See also**

[Configuring secure communication for Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-secure-communication-for-smrtserver-panels-comfort-panels-rt-advanced)

## Remote control via Sm@rtServer (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Types of the remote control (Panels, Comfort Panels, RT Advanced)](#types-of-the-remote-control-panels-comfort-panels-rt-advanced)
- [Distributed operator stations (Panels, Comfort Panels, RT Advanced)](#distributed-operator-stations-panels-comfort-panels-rt-advanced)

### Types of the remote control (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Remote control and remote monitoring by means of Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#remote-control-and-remote-monitoring-by-means-of-smrtserver-panels-comfort-panels-rt-advanced)
- [Remote control by means of web browser (Panels, Comfort Panels, RT Advanced)](#remote-control-by-means-of-web-browser-panels-comfort-panels-rt-advanced)
- [Remote control by means of the Sm@rtClient application (Panels, Comfort Panels, RT Advanced)](#remote-control-by-means-of-the-smrtclient-application-panels-comfort-panels-rt-advanced)
- [Remote control via the Sm@rtClient display during runtime (Panels, Comfort Panels, RT Advanced)](#remote-control-via-the-smrtclient-display-during-runtime-panels-comfort-panels-rt-advanced)

#### Remote control and remote monitoring by means of Sm@rtServer (Panels, Comfort Panels, RT Advanced)

##### Introduction

The Sm@rtOptions of WinCC enable the access from HMI device or PC to a remote HMI device via Ethernet.

##### Requirement

- The License Key "Sm@rtServer" is available at the Server-HMI device.

  > **Note**
  >
  > The 14-day license is not supported by Windows CE devices.

  > **Note**
  >
  > As of WinCC V15.1 the Sm@rtServer option is available and configurable for all 2nd generation Mobile Panels without a license. See the important notes in the Siemens Industry Online Support entry ID [109758056](https://support.industry.siemens.com/cs/ww/en/view/109758056).
- Both devices are linked via a TCP/IP-ready network, that is via a LAN or the Internet.
- "Sm@rtServer" is activated in the WinCC-Project of the Server-HMI device for the "Services in Runtime".
- Additional requirements must be satisfied according to the type of implementation.

##### Implementing remote access

The Sm@rtServer supports remote monitoring or remote control on the remote device (server).

Remote monitoring or remote control can be implemented on the local device (client) in various ways:

- By means of Internet Explorer
- By means of the Sm@rtClient-application

##### Access via HTML pages

The Sm@rt Options enable access for remote control with Microsoft Internet Explorer and by means of integrated HTML pages of the server.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Ethernet communication**  In Ethernet-based communication, such as PROFINET IO, HTTP, Sm@rt Options and OPC, it is the end user who is responsible for the security of his data network. The proper functioning of the device cannot be guaranteed in all circumstances; targeted attacks, for example, can lead to an overloading of the device. |  |

#### Remote control by means of web browser (Panels, Comfort Panels, RT Advanced)

##### Introduction

On the client HMI device, the connection to the remote HMI device is established by means of a web browser

The web browser shows only the screen of the remote HMI device, that of the server HMI device. If task switching is not locked on the server HMI device, you can access the desktop.

##### Requirement

- The Client-HMI device is a PC.
- A current web browser is installed.
- The Client-and Server-certificates are installed to ensure the data security when transferred via internet.
- The Java-Applet is installed. The Java applet accesses the Java runtime environment that is installed on the client.

  > **Note**
  >
  > You achieve the best results if you have installed the latest Java Runtime Environment (JRETM) of Sun Microsystems. Go to www.java.com to download this program.

##### Process flow

Enter the address of the remote device in the web browser. The address consists of the server name and the HTTP port number that is set on the server. The default setting is: 5800.

Examples of addressing: "https://MyPanel:5800" or "https://192.168.168.1:5800".

> **Note**
>
> The connection is only possible with https.

The following VNC authentication dialog contains the "Thumbprint" and "Password" fields. If there is no "Thumbprint" field, your browser cache still contains the old dialog. In this case, clear your web browser cache and try connecting again.

##### Restrictions

The "Force write access with password" function cannot be implemented using the Java applet.

---

**See also**

["Administration" tab (Panels, Comfort Panels, RT Advanced)](#administration-tab-panels-comfort-panels-rt-advanced)

#### Remote control by means of the Sm@rtClient application  (Panels, Comfort Panels, RT Advanced)

##### Introduction

The Sm@rtClient application provides the connection to the remote HMI device on the remote HMI device.

##### Requirement

- The Client-and Server-certificates are installed to ensure the data security when transferred via internet.
- The Client-HMI device is a PC.

##### Process flow

The remote control via the Sm@rtClient-application works as follows:

- Start Sm@rtClient application
- Establish connection
- Password input
- Perform operator control or monitoring on the HMI device

##### Start Sm@rtClient application

You can access the Sm@rtClient application, the program "SmartClient.exe", in various ways:

- By installing WinCC Runtime on the client device you have automatically installed the Sm@rtClient application.
- You have several options if WinCC Runtime is not installed on the client device:

  - Copy the Sm@rtClient application from the WinCC product-DVD from the folder "Support\SmartClient".
  - Copy the Sm@rtClient application from the "...\Siemens\Automation\WinCC RT Advanced" folder of another PC using a floppy disk or the Intranet.

##### Establish connection

In order to establish the connection to the remote HMI device, call the Sm@rtClient application and enter the IP address of the server.

- IP address or server name:port number
- IP address or server name:display number

Example: "192.168.0.1::5800"

You can also start the Sm@rtClient application with the command line: "smartclient.exe 192.168.0.1". The logon dialog box opens.

Or you start the Sm@rtClient application via the command line with password: "smartclient.exe 192.168.0.1 /password <Password>".

> **Note**
>
> If the Sm@rtServer at the server HMI device does not run as a service, the connection established with the Sm@rtClient application is interrupted automatically as soon as the keyboard shortcut CTRL+ALT+DEL is pressed at the server HMI device or the screen saver is activated. In order for the Sm@rtServer to run as a service, the "Start automatically after booting" check box in the "Remote" tab in the "WinCC Runtime Advacned Internet Settings" dialog must be activated.

##### Password input

- Password input at the Sm@rtServer

  Instead of the on-screen keyboard, the following message is displayed on the Sm@rtClient if you enter the password directly at the Sm@rtServer: "Remote access by Sm@rt Options is in Progress. Please wait until the input of values has been ended." This measure prevents keyboard input for entering the password from being displayed on the Sm@rtClient.
- Password input at the Sm@rtClient

  The on-screen keyboard is hidden on the Sm@rtServer due to the actions carried out on the Sm@rtClient. Use the local on-screen keyboard for entries at the Sm@rtClient. The local on-screen keyboard will be displayed automatically on the Sm@rtClient or in the Sm@rtClient view. Close the on-screen keyboard manually. Select "Input > Hide Input Panel" to hide the local on-screen keyboard.

  > **Note**
  >
  > The entries with full-screen keyboard are not protected on HMI devices with a screen size of ≤ 6''.
  >
  > Entries in Control Panel Applets which do not use the full-screen keyboard are protected.

  > **Note**
  >
  > Hidden password input is not supported by the on-screen keyboards of third-party products.

  > **Note**
  >
  > You cannot enter special characters with the keyboard shortcut Alt Gr.

##### Perform operator control or monitoring on the HMI device

In the Sm@rtClient application window, the entire layout of the remote HMI device is shown. Depending on the configuration, you can specify monitoring only or operator control of all keys, including the function keys, with the mouse. In addition, the entire desktop can be accessed in the case of a PC.

For operator control via the keyboard, the following is available:

| Keyboard shortcut | Function |
| --- | --- |
| <ALT+CTRL+SHIFT+O> | Opens the "Sm@rtClient Options" dialog |
| <ALT+CTRL+SHIFT+F> | Switches over to full screen mode |
| <ALT+CTRL+SHIFT+R> | Updates the display |
| <ALT+CTRL+SHIFT+N> | Opens the "New Sm@rtServer Connection" dialog |
| <ALT+CTRL+SHIFT+S> | Save as |
| <ALT+CTRL+SHIFT+T> | Displays and hides the toolbar |

---

**See also**

[Dialog "New Sm@rtServer: Connection" (Panels, Comfort Panels, RT Advanced)](#dialog-new-smrtserver-connection-panels-comfort-panels-rt-advanced)

#### Remote control via the Sm@rtClient display during runtime (Panels, Comfort Panels, RT Advanced)

##### Introduction

The Sm@rt options of WinCC enables access from the HMI device or PC to a remote HMI device via Ethernet.

##### Requirement

- The License Key "Sm@rtServer" is available at the Server-HMI device.
- Both devices are linked via a TCP/IP-ready network, that is, via a LAN or the Internet.
- HMI-device is configured as Sm@rtServer. For more information, refer to "[Configure Sm@rtServer](#configure-smrtserver-panels-comfort-panels-rt-advanced)".
- The Sm@rtClient-Display in an image is added in the client-HMI device project. For more information, refer to "[Project Sm@rtClient](#project-smrtclient-panels-comfort-panels-rt-advanced)".

##### Implementing remote access

The Sm@rtServer supports remote monitoring or remote control on the remote device (server).

On the client HMI device, the connection to the Sm@rtServer is made during runtime by means of the Sm@rtClient display.

On the HMI device only the screen of the server, and not the soft keys, is displayed.

The form of the cursor is not a part of the screen and is therefore not transmitted. Only the coordinates of the cursor are transmitted.

> **Note**
>
> If a soft-key is activated on the client HMI device, then observe the following:
>
> This signal is transferred to the Server-HMI device and becomes effective there, only if no function was configured at the soft-key.
>
> Otherwise, the function projected on the client-HMI device is executed.

##### Use of direct keys for remote access

You can only operate direct keys locally on the server. Although the key for the direct key can be operated on the Sm@rtClient, no bit is set in the I/O range of the PLC.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Ethernet communication**  In Ethernet-based communication, such as PROFINET IO, HTTP, Sm@rt Options and OPC, it is the end user who is responsible for the security of his data network. The proper functioning of the device cannot be guaranteed in all circumstances; targeted attacks, for example, can lead to an overloading of the device. |  |

##### Password input at the Sm@rtServer

Instead of the on-screen keyboard, the following message is displayed on the Sm@rtClient if you enter the password directly at the Sm@rtServer: "Remote access by Sm@rt Options is in Progress. Please wait until the input of values has been ended." This measure prevents keyboard input for entering the password from being displayed on the Sm@rtClient.

##### Password input at the Sm@rtClient

The on-screen keyboard is hidden on the Sm@rtServer due to the actions carried out on the Sm@rtClient. Use the local on-screen keyboard for entries at the Sm@rtClient. The local on-screen keyboard will be displayed automatically on the Sm@rtClient or in the Sm@rtClient view.

Close the local on-screen keyboard manually. Select "Input > Hide Input Panel" to hide the local on-screen keyboard.

> **Note**
>
> The entries with full-screen keyboard are not protected on HMI devices with a screen size of ≤ 6''.
>
> Entries in Control Panel Applets which do not use the full-screen keyboard are protected.

> **Note**
>
> Hidden password input is not supported by the on-screen keyboards of third-party products.

> **Note**
>
> You cannot enter special characters with the keyboard shortcut Alt Gr.

---

**See also**

[Project Sm@rtClient (Panels, Comfort Panels, RT Advanced)](#project-smrtclient-panels-comfort-panels-rt-advanced)
  
[Configure Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configure-smrtserver-panels-comfort-panels-rt-advanced)

### Distributed operator stations (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuration (Panels, Comfort Panels, RT Advanced)](#configuration-panels-comfort-panels-rt-advanced)
- [Configure distributed operator stations (Panels, Comfort Panels, RT Advanced)](#configure-distributed-operator-stations-panels-comfort-panels-rt-advanced)
- [Configure Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configure-smrtserver-panels-comfort-panels-rt-advanced)
- [Project Sm@rtClient (Panels, Comfort Panels, RT Advanced)](#project-smrtclient-panels-comfort-panels-rt-advanced)

#### Configuration (Panels, Comfort Panels, RT Advanced)

##### Configuration

Multiple HMI devices are used as decentralized, coordinated operator stations that have access to a centralized HMI device connected to the PLC.

The HMI devices are linked via a TCP/IP-network, (LAN or Intranet /Internet).

![Distributed HMI](images/7737400715_DV_resource.Stream@PNG-en-US.png)

Distributed HMI

Only one HMI device, the Sm@rtServer contains the configuration data. The Sm@rtServer is controlled from the HMI devices.

The decentralized operator stations are the Sm@rtClients. These operator stations display the same process screen of the server. A Sm@rtClient-Display is configured in the process screen for the operation and monitoring.

All devices have the same screen resolution.

The operator stations are in shared mode. As soon as a defined period of time elapses without any action on an operator station, another operator station can become active. If Sm@rtClient display is configured accordingly, the user can also log off directly.

##### Advantages

- Operator control and monitoring can be performed from various locations without significant efforts.

  The project only has to run on one HMI device configured as a server. The same client project runs on all other HMI devices; the Sm@rtClient display object is contained in a screen on these devices. The screen of the server is displayed via the Sm@rtClient display.
- The server is situated remotely from the machine and is thus not exposed to the environmental conditions of the machinery room.
- Coordinated operation is provided by the Sm@rtServer. Additional PLC investments are not required. For example, the load on the field bus is also reduced – the communication load on the bus is removed due to the interlocking mechanisms on the PLC side.

#### Configure distributed operator stations  (Panels, Comfort Panels, RT Advanced)

##### Introduction

Operator control of an extensive printing machine need to have the option to exercise control, when necessary, at multiple locations along the machinery. Depending on his current location, the operator must be able to access the process from an operator station in the vicinity.

##### Requirement

- The HMI-device with the configuration data is connected with the control.
- The server-HMI device and the Client-HMI devices are networked with each other via TCP/IP-Network.
- The License Key "Sm@rtServer" is available.

##### Configuration steps

The following basic steps are necessary for configuring the distributed operator stations:

| Step |  |
| --- | --- |
| 1 | [Configuring Sm@rtServer](#configuring-smrtserver-panels-comfort-panels-rt-advanced) |
| 2 | [Setting WinCC Runtime Advanced Internet](#setting-wincc-runtime-advanced-internet-panels-comfort-panels-rt-advanced) |
| 3 | [Project Sm@rtClient](#project-smrtclient-panels-comfort-panels-rt-advanced) |
|  |  |

#### Configure Sm@rtServer (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring Sm@rtServer (Panels, Comfort Panels, RT Advanced)](#configuring-smrtserver-panels-comfort-panels-rt-advanced)
- [Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)](#setting-wincc-runtime-advanced-internet-panels-comfort-panels-rt-advanced)

##### Configuring Sm@rtServer (Panels, Comfort Panels, RT Advanced)

###### Requirement

- The WinCC-Project for the Server-HMI device is configured.

###### Procedure

Proceed as follows to configure the Sm@rtServer in WinCC:

1. Double-click on the "Runtime-settings" entry in the project tree.
2. In the "Runtime-settings" editor, click on the "Services".
3. Enable "Sm@rtServer" in the group "RemoteControl".
4. Transfer the compiled WinCC-project to the Server-HMI-device.

###### Result

The Server-HMI device is configured as Sm@rtServer .

##### Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)

###### Requirement

- The "Control Panel" opens.
- The "WinCC Runtime Advanced Internet" dialog is open.
- The "Remote" tab is displayed.

###### Procedure

Proceed as follows to change the "WinCC Runtime Advanced Internet" settings on the Sm@rtServer:

1. On the "Remote" tab, select "Start automatically after booting".
2. Click on the "Change settings" button. The "Sm@rtServer Settings" dialog opens.

   ![Procedure](images/85467517963_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/85467517963_DV_resource.Stream@PNG-de-DE.png)
3. On the "Server" tab, select "Accept socket connections".
4. Enable "Encrypt communication" to establish an encrypted connection to the server.
5. Enter a password for "Password 1 "and "Password 2". Click "Apply".
6. Click on the "Administration" tab.

   ![Procedure](images/85467521803_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/85467521803_DV_resource.Stream@PNG-de-DE.png)
7. In the area Connection priority", select Automatic shared sessions". For "Active user timeout" enter time that must elapse without any actions on the active HMI device before access can be changed. After the entered time has expired, you do not need to enter the password again.
8. Under the "Forced write access", clear "Password needed" for the forced access to the HMI device Click "Apply". Click "OK" to close all opened dialogs.

###### Result

The settings were changed. The changes will be effective after restarting the Sm@rtServer.

---

**See also**

[Settings on the HMI device (Panels, Comfort Panels, RT Advanced)](#settings-on-the-hmi-device-panels-comfort-panels-rt-advanced)
  
[WinCC Runtime Advanced Internet, "Remote" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-remote-tab-panels-comfort-panels-rt-advanced)
  
["Server" tab (Panels, Comfort Panels, RT Advanced)](#server-tab-panels-comfort-panels-rt-advanced)
  
["Administration" tab (Panels, Comfort Panels, RT Advanced)](#administration-tab-panels-comfort-panels-rt-advanced)
  
[Project Sm@rtClient (Panels, Comfort Panels, RT Advanced)](#project-smrtclient-panels-comfort-panels-rt-advanced)

#### Project Sm@rtClient (Panels, Comfort Panels, RT Advanced)

##### Requirement

- The WinCC project for the client HMI device is configured.
- The "Screens" editor is open.
- The Inspector window is shown.
- The "Tools" task card is open.

##### Procedure

Proceed as follows to configure the Sm@rtClient:

1. Insert the Sm@rtClient display in the start screen.
2. In the Inspector window, click "Properties > Properties > General".
3. Enter the IP address or the name of the server HMI device in the "Address Sm@rtServer" field.
4. Enter "Password 1" configured on the server in the "Password" field.
5. Activate the "Encrypt communication" function in the "Options" area.

   When the "Encrypt communication" function is enabled, the connection to the server is encrypted through the exchange of certificates.
6. Activate the setting "Allow Menu".

   This provides the operator with the option of logging off using the menu.

   ![Procedure](images/129156533899_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/129156533899_DV_resource.Stream@PNG-en-US.png)
7. Transfer the compiled project to all operator stations.

##### Result

The Sm@rtClient display was added to the start screen in the WinCC project of the Sm@rtClient.

After the Sm@rtServer and the operator stations are started for the first time, a check is carried out as to whether communication is encrypted.

- If communication is encrypted, save the certificate of the Sm@rtServers on the HMI device.

  Afterwards, you connect the Sm@rtClient with the Sm@rtServer using encrypted communication.
- If communication is not encrypted, you connect the Sm@rtClient with the Sm@rtServer without a certificate.

In order to control the server from an operator station, the operator must wait a specified amount of time following the last action on another HMI device.

If the operator uses the menu of the Sm@rtClient display to log off at the previously used HMI device, he can immediately control the server at the next HMI device.

---

**See also**

[Remote control via the Sm@rtClient display during runtime (Panels, Comfort Panels, RT Advanced)](#remote-control-via-the-smrtclient-display-during-runtime-panels-comfort-panels-rt-advanced)
  
["Server" tab (Panels, Comfort Panels, RT Advanced)](#server-tab-panels-comfort-panels-rt-advanced)
  
[Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)](#setting-wincc-runtime-advanced-internet-panels-comfort-panels-rt-advanced)

## E-mail notification from runtime (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Process flow (Panels, Comfort Panels, RT Advanced)](#process-flow-panels-comfort-panels-rt-advanced)
- [Specify trigger for E-Mailing (Panels, Comfort Panels, RT Advanced)](#specify-trigger-for-e-mailing-panels-comfort-panels-rt-advanced)
- [Configure secure e-mail notification from Runtime (Panels, Comfort Panels, RT Advanced)](#configure-secure-e-mail-notification-from-runtime-panels-comfort-panels-rt-advanced)

### Process flow (Panels, Comfort Panels, RT Advanced)

#### Introduction

WinCC Runtime Advanced with the Sm@rtService offers the option of sending messages automatically via email.

The automatic e-mailing feature ensures that all people affected by the machine status (for example, shift engineer and sales manager) are informed in a timely manner.

#### Contents and triggers for e-mailing

The following events can trigger an e-mail to be sent:

- Alarm of a certain alarm class
- Event in which a standard function has been configured, such as a tag value change, etc.

Such an e-mail can have the following contents:

- Alarm text with process tags (maximum of 256 characters)
- Date/time
- E-mail address for replies

If you use e-mail gateways or SMS gateways, you receive access to standard networks, which requires external service providers. If configured accordingly, in critical situations the operator station sends an SMS to your mobile phone.

#### Enabling e-mailing and SMS

The HMI device can send e-mails to an SMTP server only. The server sends the e-mails to the addresses configured in the server.

Nothing else is required to send e-mails to addresses in the company network. However, an external service provider is required to access standard networks.

If an SMS communication is to be sent to service personnel, an SMS gateway is required as well.

#### Settings on the HMI device

The settings for emailing on the HMI device are made in the "Email" tab under "WinCC Runtime Advanced Internet" on the control panel.

The "Sender" entry field is assigned the default value "Automation HMI device." A change is useful if you want the recipient to be able to identify the device from which the e-mail originated, e.g. "HMI device on production line 2"

You can also use an SMTP server that support authentication to send e-mail.

The following authentication modes can be configured:

- Authentication by means of a valid e-mail address
- Authentication by means of user name and password

Data can also be encrypted and sent via an SSL connection. This means the data cannot be manipulated or read.

> **Note**
>
> E-mails encrypted with TLS1.2 can be sent as of TIA Portal V14 on Comfort Panels and KTP Mobile Panels.

### Specify trigger for E-Mailing (Panels, Comfort Panels, RT Advanced)

#### Requirement

- You have to create WinCC project.

#### Procedure

Proceed as follows to send a message when an alarm is triggered:

1. Double-click on the "HMI-Alarms" entry in the project tree.
2. Click the "Alarm classes" tab in the "HMI-Alarms" editor.
3. Select the alarm class, e.g. "Errors".
4. Enter the E-Mail-Address in the inspector window under "Properties > Properties > General".
5. Create an analog or discrete message with this alarm class.

#### Result

The trigger to send a message was configured. A message is automatically sent when a message of this alarm class is triggered.

### Configure secure e-mail notification from Runtime (Panels, Comfort Panels, RT Advanced)

#### Introduction

If you send e-mail via the SMTP protocol, the sender is not verified. To ensure secure transmission of e-mails, you can use SMTP servers that support SMTP AUTH (authentication).

You must log on to the SMTP server to send e-mails. The following authentication modes can be configured:

- Authentication by means of a valid e-mail address
- Authentication by means of user name and password

The data can also be sent via an SSL connection. SSL (Secure Socket Layer) encrypts e-mails and user data for transmission. This means the e-mail cannot be manipulated or read during transmission.

#### Requirement

- The SMTP server supports SMTP AUTH and STARTTLS. You can obtain more detailed information from your service provider.
- User name and password or a valid e-mail address for logon to the SMTP Server. You can obtain this data from your service provider.
- The SMTP server is available.
- The e-mail address of the service technician is entered in the alarm class.
- An analog or discrete alarm has been created for this alarm class.

#### Procedure in WinCC

1. Double-click on the "Runtime-settings" entry in the project tree.
2. In the "Runtime-settings" editor, click on the "Services".
3. Enter the sender name to be shown in e-mail under "Sender name". If the SMTP server does not support the function, delete the entry.
4. Assign a port number.

   Port number 25 is assigned by default.

   The port number in WinCC must match the port number in the "WinCC Internet Settings" on the HMI device.
5. Enter the authentication data.

   - Authentication by means of a valid e-mail address

     Type in the e-mail address required for SMTP authentication in the "E-mail address" input field.
   - Authentication by means of user name and password

     Enter the user name and your password. You can obtain the user name and password from your service provider.
6. Enable "The server requires a secure connection (SSL)".

**Note**

You can only configure the port number with the following HMI devices:

- Comfort Panels
- RT Advanced

#### Procedure on the HMI device

> **Note**
>
> Note that the settings on the HMI device have a higher priority than the settings in the WinCC project.

1. Open the "WinCC Runtime Advanced Internet " dialog in the control panel of the HMI device.
2. Click on the "E-mail" tab.
3. Specify the SMTP server.

   - Select "Use the default project file" if you want to use the SMTP server defined in the project.
   - Deactivate "Use the default project file" if you do not want to use the SMTP server defined in the project. Specify the required SMTP server. For HMI devices with Windows CE, specify the computer name or the FQDN (Fully Qualified Domain Name).
4. Assign a port number.

   Port number 25 is assigned by default.

   The port number must match the port number in the WinCC Internet Settings in the HMI device.
5. Enter the sender name given in the e-mail under "Name of the sender". If the SMTP server does not support the function, delete the entry.
6. Enter the authentication data.
7. Enter a valid e-mail address at "eMail address of sender" if required for authentication.

   - Click "Advanced" if you need a user name and password for authentication. The "Advanced Email Settings" dialog opens.
8. Type in the user name and password in the "Advanced Email Settings" dialog.

   - Enable "Use the default of the project file" to use default user data you have defined in the project.
   - Select "Use panel settings for authentication" if you do not want to use the user data defined in the project. Enter the user name and password.
9. Enable transmission via SSL.

   - To use the project settings, enable "Use the default of project file" and SSL in WinCC.

**Note**

You can only configure the port number with the following HMI devices:

- Comfort Panels
- RT Advanced

#### Result

If a tag such as a mixer speed exceeds configured limits, a corresponding alarm is displayed on the HMI device. The data is sent to the SMTP server via SSL connection. The e-mail is sent to the field service technician after successful logon.

## Display integrated Service-Pages (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Integrated Webserver (Panels, Comfort Panels, RT Advanced)](#integrated-webserver-panels-comfort-panels-rt-advanced)
- [Service-pages of the web server (Panels, Comfort Panels, RT Advanced)](#service-pages-of-the-web-server-panels-comfort-panels-rt-advanced)
- [Installing the client and server certificates for SSL (Panels, Comfort Panels, RT Advanced)](#installing-the-client-and-server-certificates-for-ssl-panels-comfort-panels-rt-advanced)
- [Configure access to service-pages (Panels, Comfort Panels, RT Advanced)](#configure-access-to-service-pages-panels-comfort-panels-rt-advanced)
- [Create own Service-pages (Panels, Comfort Panels, RT Advanced)](#create-own-service-pages-panels-comfort-panels-rt-advanced)

### Integrated Webserver (Panels, Comfort Panels, RT Advanced)

#### Introduction

The operator can display and navigate between web pages during runtime using the web server integrated in the HMI device.

The integrated web server displays the integrated service-pages. Depending on the configuration, own configured HTML-pages or Service-pages of a server accessible over Ethernet are be displayed.

#### Requirement

- "HTML-Pages" is activated in the WinCC-Project of the Server-HMI device for the "Services in Runtime".

  > **Note**
  >
  > It is always possible on a PC to access HTML-pages in runtime, although the option "HTML-pages" is cleared. Setup always installs the standard pages of the Web Server on the PC. Assign an administrator password to prevent unauthorized access to the pages.

#### Purpose of the web server

The integrated web server permits HTML pages to be displayed during runtime over one of the following routes:

- Internet Explorer
- HTML browser screen object during runtime (not on Windows CE devices)

The following are displayed:

- internal [Service-pages](#service-pages-of-the-web-server-panels-comfort-panels-rt-advanced) available by default on the HMI-device
- Other pages that you configure
- Other Internet pages

An operator or service technician can access service-critical information via the HTML pages. The standard HTML pages provide the following options:

- Remote control (if the HMI device is configured as a Sm@rtServer)
- Remote control using Microsoft Internet Explorer
- Starting and stopping of runtime
- Remote access to recipe data records and password lists
- Display of system information
- File management using a file browser
- Downloading of configuration data
- A "DATETIME" tag always returns a date within the range from 1.1.1970 00:00:00 to 31.12.2037 23:59:59.
- The "Export recipes" function requires the following authorizations:

  - PC: "UserData"
  - other HMI devices: "UserData" and "FileBrowserUser"

#### HTML browser for HTML pages

The HTML-pages are also displayed using the configured "HTML browser" screen object (not on Windows-CE devices).

You can can also arrange for input or activation of an Internet address. As soon as the operator enters or activates an address, the HTML browser opens the relevant page.

The appearance and functionality of the HTML browser screen object depends on the HMI device type. On PCs, the HTML browser corresponds to the Internet Explorer installed.

> **Note**
>
> Note that the HTML browser options during runtime are restricted due to operating device capacities and options.

### Service-pages of the web server (Panels, Comfort Panels, RT Advanced)

#### Introduction

The operator can use Internet Explorer or the HTML browser screen object during runtime to display service-pages without any additional configuration.

You can also create own service-pages. For detailed information, refer to "Configure In-house service-pages".

#### Requirement

- "HTML-Pages" is activated in the WinCC-Project of the Server-HMI device for the "Services in Runtime".

  > **Note**
  >
  > It is always possible on a PC to access HTML-pages in runtime, although the option"HTML-pages" is cleared. Setup always installs the standard pages of the Web Server on the PC. Assign an administrator password to prevent unauthorized access to the pages.

#### Service-pages

WINCC Runtime has the following service-pages:

- start.html: Home page
- RemoteControl.html: Remote control (only for Internet Explorer)
- Control.html: Control functions
- StatusDetails.html: System diagnostics
- Browse.html: File browser (only for Internet Explorer)

#### Home page: Start.html

The start page contains the links to all other pages and displays current information about the project: Mode, software versions, device data, etc.

#### "Remote control": RemoteControl.html

The "Remote control" page enables operator control of the HMI device for which a page is to be displayed. This page can only be displayed by using the Internet Explorer.

#### "Control functions": Control.html

The "Control functions" page enables the following options on the HMI device for which a page is to be displayed:

- Starting and stopping of HMI runtime

  > **Note**
  >
  > The transfer mode must be set in the Loader-menu on the HMI-device.
- Exporting and importing of recipes

  > **Note**
  >
  > After importing recipes with Sm@rtService (HTML pages), restart Runtime. The imported recipes only become active the next time Runtime is started.
- Exporting and importing password lists

  > **Note**
  >
  > The password list must be named "pdata.pwl." It is exported to the following directory:
  >
  > On Windows CE-devices: In the "\Flash\simatic\" target directory
  >
  > On PCs: the folder that was set in the file "HMILoader.exe".
  >
  > The password list is exported and becomes active the next time Runtime is started.

#### "System diagnostics": StatusDetails.html

The "System diagnostics" page contains system alarms from the alarm buffer.

#### "File Browser" – Browse.html

The "File Browser" page is used to administer directories and files on the remote device. This page can be displayed with any Internet browser.

> **Note**
>
> The maximum file size for upload or download via the file browser is 2 GB.

### Installing the client and server certificates for SSL (Panels, Comfort Panels, RT Advanced)

#### Introduction

To ensure data security, data are encoded for transmission over the Internet. Encoding and decoding is performed by appropriate software – the certificates for SSL (Secure Sockets Layer).

- The client certificate for SSL must be installed on devices that are to be used to control a remote device.
- The server certificate for SSL must be installed on HMI devices that are to allow remote control.

### Configure access to  service-pages (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configure integrated web server (Panels, Comfort Panels, RT Advanced)](#configure-integrated-web-server-panels-comfort-panels-rt-advanced)
- [Display and remote-control Service-Pages (Panels, Comfort Panels, RT Advanced)](#display-and-remote-control-service-pages-panels-comfort-panels-rt-advanced)

#### Configure integrated web server  (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configure WinCC-Project (Panels, Comfort Panels, RT Advanced)](#configure-wincc-project-panels-comfort-panels-rt-advanced)
- [Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)](#setting-wincc-runtime-advanced-internet-panels-comfort-panels-rt-advanced-1)

##### Configure WinCC-Project  (Panels, Comfort Panels, RT Advanced)

###### Requirements

- The WinCC-Project of the server-HMI-device is configured.

###### Procedure

Proceed as follows to configure the HMI device in such a way that other HMI devices or PCs can be connected to it:

1. Double-click on the "Runtime-settings" entry in the project tree.
2. In the "Runtime-settings" editor, click on the "Services".
3. Enable the "HTML-Pages" in the "Diagnostics" group.
4. Transfer the compiled WinCC-project to the Server-HMI-device.

###### Result

The Server-HMI-device is configured as web server.

##### Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)

###### Requirement

- The "WinCC Runtime Advanced Internet" dialog is open.
- The "Web Server" tab is displayed.

###### Procedure

Proceed as follows to change the "WinCC Runtime Advanced Internet" settings on the HMI device:

1. Click "User Administration" in the "Web Server" tab.
2. Open the "UserDatabase-Edit" dialog.
3. Click "Add" in the "User manager" tab to create a new user.
4. Enter a user name and specify a password.
5. Click "Apply".
6. Click the "Authorizations" tab.
7. Specify on the "Authorizations" tab, which functions can the user carry out on the HTML-pages of an HMI-device. You can find more detailed information on this in the section "[User administration for web server](#user-administration-for-web-server-panels-comfort-panels-rt-advanced) ".
8. Close the "UserDatabase-Edit" dialog.
9. On the "Remote" tab, select the "Start automatically after booting" check box.
10. Click "Change settings" and select the "Enable connections" check box in the "Sm@rtServer Settings" dialog.
11. Specify a password for "Password2" so that the HMI device can be remotely controlled by the service technician.

###### Result

A user was created on the HMI device in the user administration of the Web server and configured for the remote control.

The service technician can be connected to the HMI-device by means of the Internet Explorer and the Sm@rtClient Application. After disconnecting the connection, the HMI-device can be operated from his PC.

---

**See also**

[WinCC Runtime Advanced Internet, "Web Server" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-web-server-tab-panels-comfort-panels-rt-advanced)
  
[User administration for web server (Panels, Comfort Panels, RT Advanced)](#user-administration-for-web-server-panels-comfort-panels-rt-advanced)
  
["Server" tab (Panels, Comfort Panels, RT Advanced)](#server-tab-panels-comfort-panels-rt-advanced)

#### Display and remote-control Service-Pages (Panels, Comfort Panels, RT Advanced)

##### Requirements

- A user is created on the HMI-device in the user administration for the web server.
- The web server is started.
- The Client-and Server-certificates are installed to ensure the data security when transferred via internet.

##### Procedure

To display and control the service pages, follow these steps:

1. Start the Internet Explorer on the configuration-PC and connect with the "Homepage" of the HMI-device.

   ![Procedure](images/8435338763_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/8435338763_DV_resource.Stream@PNG-de-DE.png)
2. For "Name" and for "Password", enter the data of the user configured in the user administration of the web server. Click "Login".
3. Click "System Diagnostics". The system alarms from the alarm buffer are displayed on this page.
4. Click "Remote Control" to remotely control the HMI-device.

##### Result

The service-pages are displayed. The HMI-device can be operated or monitored via the service-pages.

A keyboard units cannot be operated completely in the Internet Explorer, since only the screen content is displayed. Use the Sm@rtClient-Application to remotely control the keys of HMI-device. The Sm@rtClient-Application can be located under "Start > Program > Siemens Automation > Runtime Systems > WinCC Runtime Advanced > Sm@rtClient"

### Create own Service-pages (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics (Panels, Comfort Panels, RT Advanced)](#basics-panels-comfort-panels-rt-advanced-1)
- [Create service-page for displaying process values (Panels, Comfort Panels, RT Advanced)](#create-service-page-for-displaying-process-values-panels-comfort-panels-rt-advanced)
- [Transfer Service-pages (Panels, Comfort Panels, RT Advanced)](#transfer-service-pages-panels-comfort-panels-rt-advanced)

#### Basics (Panels, Comfort Panels, RT Advanced)

##### Introduction

The basic framework of the service-pages corresponds to a normal HTML-file.

- Declaration of the document type
- Header with data for the title
- Body - content to be displayed.

##### Variable parameters in Service-pages

You can specify variable parameters in HTML documents. As soon as a page with variable parameters is opened, the parameters are replaced by specific values.

<BODY > Welcome on <MWSL><!-- write(GetVar("[Parameter]")); --></MWSL></BODY>

##### Available variable parameter

| Parameters | Meaning |
| --- | --- |
| ProgramMemoryComplete | CE only: Total program memory |
| ProgramMemoryFree | CE only: Program memory available |
| ProgramMemoryUsed | CE only: Program memory utilized |
| FlashComplete | CE only: Total flash memory |
| ObjStrComplete | CE only: Total available flash memory |
| ObjStrFree | CE only: Volatile memory available |
| ObjStrUsed | CE only: Volatile memory utilized |
| DeviceType | Type of target device as specified in the control panel. |
| BtLdVer | CE only: Bootloader-version, as specified in the control panel. |
| BtLdRelDate | CE only: Bootloader release date |
| ImageVersion | CE only: Image version as it appears on the loader |
| DramSize | CE only: Size of DRAM |
| HostName | The name by which the device is logged on/identified in the network. |
| RtState | Indicates whether Runtime is running on the target device. |
| SystemMessageTable | Outputs a table containing the current system events. |

In the example below, the "HostName" parameter is replaced by the network-name of the device.

<BODY > Welcome on <MWSL><!-- write(GetVar("[HostName]")); --></MWSL></BODY>

##### Process tag

Process tag values can also be displayed in HTML pages. The syntax is the same as for device tags. Use the tag name as a placeholder for the tag value, , e.g. Tag_1.

<BODY > Welcome on <MWSL><!-- write(GetVar("[Tag_1")); --></MWSL></BODY>

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Data inconsistency caused by HTML pages**  Note the information below if the "Cyclic in operation" acquisition mode is set at tag:  1. If this tag is not displayed on the HMI device, the HTML page displays the incorrect tag value in the following situations:    - The HTML page display a "0" value at its first call. The HTML page only displays the correct value after it is called again or updated.    - The last value is displayed if the connection to the PLC goes down. 2. The HTML page also displays the correct tag value if the tag is displayed on the HMI device. |  |

Situation 1 is based on standard behavior: If a tag is currently not in use currently and its value is not acquired in "Cyclic continuous" mode, the tag is loaded with its initial value in Runtime. Instead of reading the values from the PLC, however, the HTML page receives these from Runtime.

##### Link own Service-pages

If a user connects to an HMI device, he is automatically forwarded to the start page http://<Device name>/www/start.html. This page represents the starting point for the HTML-pages of the web server. Every standard page is accessible from the start page via a link. For this reason, you insert a link for each of your HTML pages in the start page.

> **Note**
>
> When inserting links in the HTML page, you must differentiate between relative and absolute links. Make sure that absolute links start with "/www" to ensure that the document will be searched for in the correct directory. Example: "/www/MyDocument.HTML".

##### Storage location of the service-pages

If files are to be located during a transfer, they must be in a specific directory:

- on a PC with Windows operating system: "C.\ProgramData\Siemens\CoRtHmiRTm\MiniWeb14.x.x\WebContent"

#### Create service-page for displaying process values  (Panels, Comfort Panels, RT Advanced)

##### Requirement

The Ta_1 and Tag_2 tags are created in the WinCc-Project.

##### Procedure

To create an own Service-page, follow these steps:

1. Copy the "WebContents" ZIP-file in a random work directory on your Configuration-PC and un-zip the ZIP-file.
2. Create a copy of start.html and rename the copy in "tag.hml".
3. Open the "tag.html" in a text editor, e.g. Notepad.
4. Replace the existing table with a new table, in which the process values of "Tag_1" and "Tag_2" tags are displayed. Save the file"tag.html".

   ![Procedure](images/8441274891_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/8441274891_DV_resource.Stream@PNG-de-DE.png)
5. Open the "start.html" file and add a hyperlink to page "tag.html". Expand the available navigation bar, in which you supplement the existing table by an entry.

   ![Procedure](images/8442665483_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/8442665483_DV_resource.Stream@PNG-de-DE.png)
6. Save start.html.

##### Result

You have created the service-page "tag.html". You have added a hyperlink on the start page in order to navigate to the service-page from the start-page.

#### Transfer Service-pages (Panels, Comfort Panels, RT Advanced)

##### Transfer files using the standard-path (Active Sync/CF- card)

Proceed as follows to transfer files via the standard-path:

1. Copy the changed HTML pages and pictures according to "\Flash\Simatic\WebContent".

   Access then takes place with "http://<device>/www/<HTML page>".

##### Transfer files via the project transfer

Proceed as follows to transfer the files via the project transfer:

1. Add the changed files to the ZIP-file "WebContents". This file must contain all HTML pages and associated pictures.

   Make sure to provide the correct path information because the files are unpacked in the directories specified in the zip file. Incorrect path information results in errors in direct addressing or due to links.
2. To transfer the ZIP file "WebContents", copy it to a specific directory.
3. Transfer the project to the HMI device.

   The ZIP-file "WebContents" is transferred to the Windows CE device where it is unzipped.

##### Transfer files using the File Browser

Proceed as follows in order to transfer files using the file transfer:

> **Note**
>
> The maximum file size for upload or download via the file browser is 2 GB.

1. Start the Internet Explorer on the configuration-PC and connect with the "Homepage" of the HMI-device.
2. Log-on to the internal Web Server to work with the File Browser.

   For read and write access to the file browser, the user must possess the web authorizations "FileBrowserAdministrator" and "FileBrowserUser" .
3. Click on "Browse" in the File Browser . The file selection dialog opens.
4. Navigate to the file storage location by means of this dialog. Select the desired file and click "Open."

   ![Transfer files using the File Browser](images/8442675723_DV_resource.Stream@PNG-de-DE.png)

   ![Transfer files using the File Browser](images/8442675723_DV_resource.Stream@PNG-de-DE.png)
5. Click "Upload File". The file is copied in the directory of the internal web server.

---

**See also**

[Basics (Panels, Comfort Panels, RT Advanced)](#basics-panels-comfort-panels-rt-advanced-1)

## Access via SIMATIC HMI HTTP Protocol (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuration (Panels, Comfort Panels, RT Advanced)](#configuration-panels-comfort-panels-rt-advanced-1)
- [Configure access via SIMATIC HTTP Protocol (Panels, Comfort Panels, RT Advanced)](#configure-access-via-simatic-http-protocol-panels-comfort-panels-rt-advanced)
- [Permissible data types (SIMATIC HMI HTTP protocol) (Panels, Comfort Panels, RT Advanced)](#permissible-data-types-simatic-hmi-http-protocol-panels-comfort-panels-rt-advanced)
- [Configure HTTP server (Panels, Comfort Panels, RT Advanced)](#configure-http-server-panels-comfort-panels-rt-advanced)
- [Configuring HTTP clients (Panels, Comfort Panels, RT Advanced)](#configuring-http-clients-panels-comfort-panels-rt-advanced)
- [Commissioning an HTTP- connection (Panels, Comfort Panels, RT Advanced)](#commissioning-an-http--connection-panels-comfort-panels-rt-advanced)

### Configuration (Panels, Comfort Panels, RT Advanced)

#### Configuration

During the communication via SIMATIC HMI HTTP Protocol, an HMI-device accesses the tags of a different HMI-device. The access is "read-only" or "read and write" depending on the configuration of the concerned HMI-device.

The HMI device providing the tags is the HTTP-server; the other HMI-device is the HTTP-client. However, access to tags functions in both directions.

![Configuration](images/7737746443_DV_resource.Stream@PNG-en-US.png)

### Configure access via SIMATIC HTTP Protocol  (Panels, Comfort Panels, RT Advanced)

#### Introduction

The tags in service-application should be illustrated in an overview for a configuration from multiple HMI-devices.

The panels in the machine level are used as tag server. The service-application illustrating tags of machines in an overview image runs on a PC.

#### Requirement

- The HMI-devices are networked via a TCP/IP-network with each other.

#### Configuration steps

The following basic steps are required to configure the access via "SIMATIC HMI Protocol".

| Step |  |
| --- | --- |
| 1 | [Configure WinCC-Project](#configure-wincc-project-panels-comfort-panels-rt-advanced-1) |
| 2 | [Setting WinCC Runtime Advanced Internet](#setting-wincc-runtime-advanced-internet-panels-comfort-panels-rt-advanced-2) |
| 3 | [Configuring HTTP connections in the client](#configuring-http-connections-in-the-client-panels-comfort-panels-rt-advanced) |
| 4 | [Configure the HTTP-Client tags](#configure-the-http-client-tags-panels-comfort-panels-rt-advanced) |
|  |  |

---

**See also**

[Permissible data types (SIMATIC HMI HTTP protocol) (Panels, Comfort Panels, RT Advanced)](#permissible-data-types-simatic-hmi-http-protocol-panels-comfort-panels-rt-advanced)

### Permissible data types (SIMATIC HMI HTTP protocol) (Panels, Comfort Panels, RT Advanced)

#### Permitted data types

When configuring tags, the data types listed below can be used.

| Data types in the HTTP Protocol | Length | Signs | Range of values |
| --- | --- | --- | --- |
| Bool | 0 | No | true (-1) or false (0) |
| Char | 1 byte | Yes | -128 to 127 |
| Byte | 1 byte | No | 0 to 255 |
| Int | 2 bytes | Yes | -32768 to 32767 |
| UInt | 2 bytes | No | 0 to 65535 |
| Long | 4 bytes | Yes | -2,147,483,648 to 2,147,483,647 |
| ULong | 4 bytes | No | 0 to 4,294,967,295 |
| Float | 4 bytes | Yes | -3.402823E38 to -1.401298E-45 for negative values and 1.401298E-45 to 3.402823E38 for positive values |
| Double | 8 bytes | Yes | -1.79769313486231E308 to -4.94065645841247E-324 for negative values and 4.94065645841247E-324 to 1.79769313486232E308 for positive values |
| String | 1 to  255 byte | –––– |  |
| DateTime | 8 bytes | –––– | 1.1.1970 00:00:00 up to 31.12.2037 23:59:59 |

Please note that data types may be defined in external controllers which have different names in WinCC. To ensure correct assignment, please observe the tag definition in the external controllers.

> **Note**
>
> It is not possible to access array tags from an HTTP client.

---

**See also**

[Configure WinCC-Project (Panels, Comfort Panels, RT Advanced)](#configure-wincc-project-panels-comfort-panels-rt-advanced-1)

### Configure HTTP server (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configure WinCC-Project (Panels, Comfort Panels, RT Advanced)](#configure-wincc-project-panels-comfort-panels-rt-advanced-1)
- [Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)](#setting-wincc-runtime-advanced-internet-panels-comfort-panels-rt-advanced-2)

#### Configure WinCC-Project  (Panels, Comfort Panels, RT Advanced)

##### Requirement

- The WinCC-Project for the Server-HMI device is configured.

##### Procedure

Proceed as follows to configure the HTTP-Server:

1. Double-click on the "Runtime-settings" entry in the project tree.
2. In the "Runtime-settings" editor, click on the "Services".
3. Select "SIMATIC HMI HTTP Server" in the group "Read/write tags".
4. Check the data types of the tags. The HTTP-client can access only those tags, whose data type is supported by communication driver "SIMATIC HMI HTTP Protocol". For additional information, refer to "[Permissible data types (SIMATIC HMI HTTP Protocol)](#permissible-data-types-simatic-hmi-http-protocol-panels-comfort-panels-rt-advanced)".
5. Transfer the compiled WinCC-project to the Server-HMI-device.

##### Result

The HMI-device is HTTP-server configured.

---

**See also**

[Permissible data types (SIMATIC HMI HTTP protocol) (Panels, Comfort Panels, RT Advanced)](#permissible-data-types-simatic-hmi-http-protocol-panels-comfort-panels-rt-advanced)

#### Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)

##### Requirement

- The "Control Panel" opens.
- The "WinCC Runtime Advanced Internet " dialog is open.
- The "Web Server" tab is displayed.

##### Procedure

Proceed as follows to change the "WinCC Runtime Advanced Internet" settings on the HTTP server:

1. Specify the access to tags in case of "Tag access".

   - "Read/write": read and write access
   - "Read only": read access
2. Specify the authentification for access in case of "Tag authenticate":

   - "No authentication": No authentication required.
   - "Authentication required": A password is required for the access. Specify the password for configuring the connection via the SIMATIC HMI HTTP Protocol.
3. Click "User Administration" in the "Web Server" tab. Enter your password. The "UserDatabase-Edit" dialog is opened. For detail instructions, refer to "[User administration for Webserver](#user-administration-for-web-server-panels-comfort-panels-rt-advanced) ".
4. Click "Add" in the "User manager" tab to create a new user. Enter a user name and specify a password. Click on "Apply".
5. Click the "Authorizations" tab.
6. Specify the web-authorizations on the tab "Authorizations". The user must have the Web-authorization "RTCommunication" for utilizing the SIMATIC HTTP Server.
7. Close all open dialog boxes.

##### Result

The settings were changed. The changes will be effective after the restart of the WebServer.

---

**See also**

[Settings on the HMI device (Panels, Comfort Panels, RT Advanced)](#settings-on-the-hmi-device-panels-comfort-panels-rt-advanced)
  
[WinCC Runtime Advanced Internet, "Web Server" tab (Panels, Comfort Panels, RT Advanced)](#wincc-runtime-advanced-internet-web-server-tab-panels-comfort-panels-rt-advanced)
  
[User administration for web server (Panels, Comfort Panels, RT Advanced)](#user-administration-for-web-server-panels-comfort-panels-rt-advanced)

### Configuring HTTP clients (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuring HTTP connections in the client (Panels, Comfort Panels, RT Advanced)](#configuring-http-connections-in-the-client-panels-comfort-panels-rt-advanced)
- [Configure the HTTP-Client tags (Panels, Comfort Panels, RT Advanced)](#configure-the-http-client-tags-panels-comfort-panels-rt-advanced)

#### Configuring HTTP connections in the client (Panels, Comfort Panels, RT Advanced)

##### Requirement

The communication driver "SIMATIC HMI HTTP Protocol" is installed.

##### Procedure

Proceed as follows to create an HTTP-connection:

1. Double-click on the "Connections" entry in the project tree. The "Connections" editor opens.
2. Create a connection. Select "SIMATIC HMI HTTP Protocol" for "Communication driver".

   ![Procedure](images/88810584459_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/88810584459_DV_resource.Stream@PNG-en-US.png)
3. Select "Ethernet" for "Interface". Select the protocol type "http://" or "https://" for address.
4. Enter the name of the HTTP-server or its IP address.

   Ask your network administrator for the specific name or parameters of your network.

   If the server has already been commissioned, you can read out the IP address on the server as well:

   - Panel  
     Click "Start > Programs > Command Prompt" on the server and enter the "ipconfig" command using the screen keyboard. Press <Enter> to display the IP-address.
   - For PC/Panel PC  
     Click on the server on "Start > Run", enter "Cmd", and press <Enter>. The command interpreter is displayed. Enter the "ipconfig" command. Press <Enter> to display the IP-address.
5. If the "HTTPS" protocol type is selected, you can establish how the HTTPS-client verifies the properties of the server-certificate and how it should react in the event of error:

   - "Allow invalid computer names for certificates"
   - "Allow expired certificates"
   - "Allow certificates signed by unknown publishers"
6. If the "Authentication required" option is selected on the HTTP server, enter the user name and the password.
7. Enter the time for "Timeout" after which disconnection is identified.

##### Result

A connection was created in the WinCC-Project of the HTTP-Client. You can find more detailed information on an HTTPS connection under "[Commissioning an HTTP- connection](#commissioning-an-http--connection-panels-comfort-panels-rt-advanced)".

---

**See also**

[Setting WinCC Runtime Advanced Internet (Panels, Comfort Panels, RT Advanced)](#setting-wincc-runtime-advanced-internet-panels-comfort-panels-rt-advanced-2)
  
[Commissioning an HTTP- connection (Panels, Comfort Panels, RT Advanced)](#commissioning-an-http--connection-panels-comfort-panels-rt-advanced)

#### Configure the HTTP-Client tags (Panels, Comfort Panels, RT Advanced)

##### Requirement

- An HTTP-connection was created in the WinCC-Project of the HTTP-Client.
- A tag is created in the WinCC-Project of the HTTP-Server. The data type of the tags is supported by SIMATIC HMI HTTP Protocols .

##### Procedure

To create tags on the HTTP-client, proceed as follows:

1. Open the "HMI- tags" folder in the project tree and double-click the entry "Standard-tag table". The "Tags" editor opens.
2. Enter a clear tag-name for "Name" in the Inspector window under "Properties > Properties > General".
3. Select the HTTP-connection for "Connection".
4. Select the data type for "data type".

   The client does not check any verification of the tag name and the data type. Pay attention that the selected data type here matches the data type of the tags in the HTTP-server. You can find more detailed information on this under "[Permissible data types (SIMATIC HMI HTTP Protocol)](#permissible-data-types-simatic-hmi-http-protocol-panels-comfort-panels-rt-advanced)".

   Array tags are not permitted.
5. Enter the exact name of the tag that is to be communicated with on the HTTP-server in the "Address" field.

   If the tag to be addressed is in a sub-folder, the complete path along with tag name must be given as address, e.g.[folder name]\[Tag name].

##### Result

A tag was created in the WinCC-Project of the Client-HMI-device. The tag has access to the HTTP-server tag via an HTTP-connection. You can use an "E/A-Field" in an image to display the process value of this tag.

---

**See also**

[Permissible data types (SIMATIC HMI HTTP protocol) (Panels, Comfort Panels, RT Advanced)](#permissible-data-types-simatic-hmi-http-protocol-panels-comfort-panels-rt-advanced)

### Commissioning an HTTP- connection (Panels, Comfort Panels, RT Advanced)

#### Introduction

To establish an HTTP connection, you must perform the following actions:

- In the "Connections" editor of WinCC ES, configure the connection as an "https://" protocol type and define how the HTTPS client should verify the properties of the server certificate and respond to errors.
- Install a valid certificate on the HTTPS client.

  Certificates are necessary for server authentication. Using certificates you can ensure that the server with which the connection is to be developed is actually the server for which it is outputting.

#### Principle of an HTTPS connection

After runtime start, the HTTPS client establishes a connection to the HTTPS server. The HTTPS server presents its certificate, which the client verifies for authenticity. The session code that can only be read by the HTTPS server is then transmitted. The session code is now available on both sides and enables a symmetrical data encryption.

> **Note**
>
> The certificate contains the current time. The current time can lead to problems if the time zones of the server and client are different. For example, a certificate generated on a server with an Asian time zone only becomes valid on a client with European time zone in the future (8 hours).

#### Preparation for installing a certificate on the client

The HTTPS server generates the certificate itself during the first HTTPS client access. The HTTPS server saves the certificate to the "Cert.cer" file. The file is stored in the following directory:

- On a PC/Panel PC (with Windows) in the directory "<Runtime Directory>\SystemRoot\SSL"
- On Windows CE-based devices in the directory "Flash\Simatic\SystemRoot\SSL"

The certificate must be stored on the HTTPS client on a storage medium from which it can be launched with a double click. You can select from the following transfer options:

| Server | Client | Possible file transfer |
| --- | --- | --- |
| with Windows (PC, Panel PC) | with Windows (PC, Panel PC) | - Diskette - USB stick - LAN (Ethernet) - Internet Explorer (via TCP/IP if service is already running) |
| with Windows CE (Comfort Panels) | with Windows (PC, Panel PC) | - Memory card - ActiveSync (serial) |
| with Windows (PC, Panel PC) | with Windows CE (Comfort Panels) |  |
| with Windows CE (Comfort Panels) | with Windows CE (Comfort Panels) | - Memory card |

#### Installing a certificate on a client with Windows

Insert the storage medium on which you have saved the "Cert.cer" file into the HTTPS client or open the directory in which the file is located. Double click on the file and follow the instructions in the Windows dialog.

Tip: The Internet Explorer provides an easy way to install a certificate. Connect to this device via HTTPS (e.g.: https://<my device>). The browser establishes if a certificate has not yet been imported. In this case, the browser asks if you want to install the certificate. Any faults in the certificate are displayed.

#### Installing a certificate on a client with Windows CE

Insert the memory card on which you have saved the converted "Cert.cer" file into the HTTPS client. WinCC includes the "InstallCert.exe" tool for importing certificates with Windows CE.

You can implement the installation as follows:

- In Explorer:  
  Double click the "Cert.cer" file to install the certificate.
- At the command prompt:  
  Enter "InstallCert /[command parameter] [filename]".

  - command parameters:

    Parameter /r must be specified because the certificate used in WinCC Runtime Advanced is a root certificate.

    A root certificate is the main certificate and is used to verify the authenticity of all other certificates transferred.
  - filename

    You must specify the certificate file with its complete path (e.g. "\Storage Card\Cert.cer")

A status alarm is output when you completed the installation. Runtime has to be restarted after the installation of a certificate on Windows CE- HMI devices with HTTPS clients. It is necessary to restart Runtime so that an HTTPS connection can be established.

#### The file "Cert.cer" cannot be opened.

If the "Cert.cer" file generated on the HTTPS server cannot be opened on HMI devices based on Windows CE 5.0 by double-clicking the client, follow these steps:

1. Open the Control Panel.
2. Select "Certificates > My Certificates".
3. Click the "Import" button.

   A dialog box opens.
4. Select the "From a File" menu in the file browser and select the "Cert.cer" file.

## Connection to the Office-world (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Configuration (Panels, Comfort Panels, RT Advanced)](#configuration-panels-comfort-panels-rt-advanced-2)
- [Creating a VBA macro in MS Excel (Panels, Comfort Panels, RT Advanced)](#creating-a-vba-macro-in-ms-excel-panels-comfort-panels-rt-advanced)

### Configuration (Panels, Comfort Panels, RT Advanced)

#### Data access via web service (SOAP)

WinCC provides options for utilization of web-service (SOAP). Web service (SOAP) is based on the Simple Object Access Protocol. Use of this protocol enables an external application to access tags of an HMI device via Ethernet. If the company network is protected by a Firewall, the system administrator must release the appropriate ports.

![Communication with other applications](images/7738417547_DV_resource.Stream@PNG-en-US.png)

Communication with other applications

For example, a device is accessing two HMI devices. The operator sees the values of certain tags and can modify them.

You can use Microsoft Excel, for example, to display tags. You will require the latest version of "MS SOAP Toolkit V2.0" for this purpose. This version is available from Microsoft as a download.

Data access via SOAP is not supported as of Windows 7. Use OPC to display the tags in MS Excel. You can find more detailed information on this under "[Configuring OPC clients](OPC%20for%20Runtime%20Advanced%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#panels-comfort-panels-rt-advanced-2)".

#### Data access to Windows CE HMI-devices

The data access via the Web-service(SOAP) on Windows CE-HMI-devices functions using only the device name and not via the IP-address.

Enter the device name of the HMI-device with the appropriate IP-address in the hosts-file. The hosts file is given in the directory "%windir%\system32\drivers\etc\", e.g. C:\WINNT\system32\drivers\etc.

The engineering object name, e.g. DEVICE, must be set in the control panel on the HMI device under "System > Device Name". Please change the default device name to ensure that the device name is unique within the network.

#### Example for the entry in the hosts-file:

192.168.56.198 DEVICE

Replace the IP address by the device name in the SOAP client:

objRuntime.mssoapinit http://DEVICE/soap/RuntimeAccess?wsdl

#### Data access with GetValue, SetValue

Access to a tag in SOAP using GetValue or SetValue functions require a special syntax.

- GetValue: "Sinus_1"
- SetValue: Sinus_1

The tag name must be given in inverted commas for GetValue. The message "Runtime is offline" will otherwise be output when runtime is accessed.

> **Note**
>
> Note that the tag name entry is case-sensitive.

### Creating a VBA macro in MS Excel (Panels, Comfort Panels, RT Advanced)

#### Introduction

Data access over the network via web service (SOAP) is to be used to permit certain tags of an HMI device to be displayed and reset.

For this purpose, macros are written in Excel, which: 1) obtain the relevant tags on the PC over the network and display them, and 2) transfer reset values back to the HMI device.

The task can be solved using VBA macros "ReadTagValue" and "WriteTagValue," which obtain and display the relevant tags in Excel over an appropriate interface and return them to the HMI device over the network. Note that the tag name entry is case-sensitive.

#### Requirement

- The SOAP toolkit is installed.
- "Web-Service (SOAP)" is selected in the WinCC-Project under "Services in Runtime".

#### Procedure

1. Insert the "Control element toolbox" toolbar in your workbook in Microsoft Excel.
2. Create a command button. Label the button "ReadTagValue" and name it "Read value".
3. Double-click this command button.

   The macro editor is displayed. The "Click" event is already preset.
4. Write the "ReadTagValue" macro ("intVarTag_1" designates the actual tag value):

'--------------------------------------------------------------

Private Sub ReadTagValue_Click()

Dim objRuntime

Dim intVarTag_1

Dim objWorksheet

Set objWorksheet = Excel.Worksheets("Sheet1")

Set objRuntime = CreateObject("MSSOAP.SoapClient")

objRuntime.mssoapinit "HTTP://servername/soap/RuntimeAccess?wsdl"

objRuntime.ConnectorProperty("AuthUser") = "Administrator"

objRuntime.ConnectorProperty("AuthPassword") = "100"

Var = objWorksheet.Cells(1, 3)

intVarTag_1 = objRuntime.GetValue(Var)

objWorksheet.Cells(1, 1) = intVarTag_1

End Sub

'---------------------------------------------------------------

1. Insert a command button. Label the command button "WriteTagValue" and name it "Write value".
2. Double-click this button.
3. Write the "WriteTagValue" macro ("intVarTag_1" designates the return value of the operation):

'---------------------------------------------------------------

Private Sub WriteTagValue()

Dim objRuntime

Dim intVarTag_1

Dim objWorksheet

Set objWorksheet = Excel.Worksheets("Sheet1")

Set objRuntime = CreateObject("MSSOAP.SoapClient")

objRuntime.mssoapinit "HTTP://servername/soap/RuntimeAccess?wsdl"

objRuntime.ConnectorProperty("AuthUser") = "Administrator"

objRuntime.ConnectorProperty("AuthPassword") = "100"

Var = objWorksheet.Cells(2,3)

Value = objWorksheet.Cells(2,5)

intVarTag_1 = objRuntime.SetValue(Var,Value)

objWorksheet.Cells(2,8) = intVarTag_1

End Sub

'---------------------------------------------------------------

#### Result

As soon as you call "ReadTagValue_Click" macro by clicking the button"Read-value", the specified intVarTag_1tag is obtained from the HMI device using the specified device address and displayed in the cell (1,1).

As soon as you call Macro "WriteTagValue" by clicking the "Write value" button, the tag name is read from the cell (2,3), and the tag value is transferred from cell (2,5) to the HMI device.

---

**See also**

[Configuration in WinCC (Panels, Comfort Panels, RT Advanced)](#configuration-in-wincc-panels-comfort-panels-rt-advanced)
