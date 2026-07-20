---
title: "Operating Unified PC (RT Unified)"
package: WinCCRTUenUS
topics: 248
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Operating Unified PC (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Starting and displaying runtime (RT Unified)](#starting-and-displaying-runtime-rt-unified)
- [Runtime operation (RT Unified)](#runtime-operation-rt-unified)
- [Controls (RT Unified)](#controls-rt-unified)
- [Elements (RT Unified)](#elements-rt-unified)
- [Basic objects (RT Unified)](#basic-objects-rt-unified)
- [Popup window (RT Unified)](#popup-window-rt-unified)
- [Tests and error analysis (RT Unified)](#tests-and-error-analysis-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Process screens (RT Unified)](#process-screens-rt-unified)
- [Tags (RT Unified)](#tags-rt-unified)
- [Alarms (RT Unified)](#alarms-rt-unified)
- [Logs (RT Unified)](#logs-rt-unified)
- [Contexts (RT Unified)](#contexts-rt-unified)

### Process screens (RT Unified)

#### Behavior of process screens

Process screens are static and dynamic representations of the plant, plant units or processes. You use the process screens to operate and monitor the plant or areas within it.

A project on an HMI device consists of multiple process screens. When you start Runtime, the process screen that was defined as the start screen is displayed. You navigate between process screens according to a sequence, navigation or link that was defined by the configuration engineer.

The process screen contains static and dynamic screen objects. Screen objects visualize the current process values from the controller memory and record operator inputs that influence the process. Dynamization is realized through the connection of tags to the screen object during configuration.

Process values and operator inputs are exchanged between the controller and the HMI device by means of tags.

A process screen can be opened and operated by several operating stations simultaneously in Runtime.

![Behavior of process screens](images/118533769739_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Displaying a start screen changed by reloading**
>
> A start screen was defined for a project, and the project was started in Runtime. If another start screen is then defined in engineering and the project is loaded into the device again, the last active screen is displayed in Runtime after the connection is established again.
>
> After reloading the project, refresh the screen in Runtime. If your HMI device is a computer, use the F5 key or the browser "Refresh" button to do this.

#### Screen navigation

Process visualization is generally split between multiple process screens, for example on the basis of functional or technological aspects. Changing between process screens is referred to as screen navigation.

#### Popup window

With corresponding configuration in the engineering system, clicking on a screen area opens a popup window containing additional information on the screen area.

Example: A screen represents a pump with its valves. When you click on a valve, a popup window opens with detailed information on the valve as well as input fields. You can check the state of the valve in the pop-up window and edit using the input fields.

#### Predefined styles

The following predefined styles are available for the process screens of the HMI devices:

- Light style
- Dark style
- Expanded style

> **Note**
>
> **Compact mode in light and dark style**
>
> If the following elements in light or dark style fall below specific dimensions, they are automatically displayed in compact mode:
>
> - Bar
> - Slider
> - Gauge
> - Clock

### Tags (RT Unified)

#### Behavior of tags

Tags correspond to defined memory areas to which values are written and/or from which values are read. In runtime, tags are output in trends or tables, for example.

External tags correspond to the process values from the memory of an automation system. They are connected to the tags of a connected PLC.

Internal tags transport values within the HMI device. The internal tag values are only available as long as runtime is running.

**Value changes to external tags**

Value changes to external tags are triggered as follows in runtime:

- By a PLC

  The PLC changes the value of the connected PLC tags.

  During the next update of the external tags, the new value is written to the HMI process image.
- By operator actions or by a script running on the HMI device

  The value change requested in runtime is not directly applied from the HMI process image. Runtime transfers the value to the PLC. The PLC writes the value to the linked PLC tag after successful verification.

  During the next update of the external tags, the new tag value is written to the HMI process picture.

Acquisition mode and acquisition cycle for updating the tags are specified during configuration.

#### Executing the script of a trigger tag

The script defined for a trigger tag in engineering is executed in Runtime in the following cases:

- During start of Runtime

  The start value of the trigger tag is reported to Runtime.
- When the condition defined for the trigger tag occurs

  For example if the trigger tag changes its state or exceeds a limit value.

#### Floating point numbers in the web client

Since the web client is implemented via JavaScript, tag values for floating point numbers can only be displayed with a mantissa of up to 54 bits. This leads to rounding of values with a mantissa greater than 54 bit in Runtime.

> **Note**
>
> Values with a mantissa of up to 64 bits are correctly displayed by I/O fields.

#### Restricted scope of validity "local session"

By default, internal tags apply "system-wide".

As an option, the scope of validity of an internal tag can be limited to "local session". Data related to a session in a multi-user environment is processed independently in each local session.

The use of local session tags is supported in Unified Collaboration and in the web client.

Local session tags permit, for example:

- Individual navigation in screen windows or in different menu structures
- Session-related disabling/enabling of the user
- Session-related position, alignment and rotation of objects in a screen

The values of a local session tag are not saved and will be lost at the end of a session.

### Alarms (RT Unified)

#### Behavior of alarms in Runtime

Depending on the configuration, PLC alarms and HMI alarms from various areas of the plant are displayed in Runtime.

Depending on the configuration, the alarms are labeled according to importance or type and are represented and displayed differently. For example, a pending alarm can be displayed as follows:

![Behavior of alarms in Runtime](images/168652073355_DV_resource.Stream@PNG-en-US.png)

### Logs (RT Unified)

#### Data log

In Runtime, the data logging functions on the server as a log server. On the clients, the data logging functions as a log client. Only the log server accesses the database and compiles and logs the process data. The clients receive log data from the log server.

The log data is visualized in tabular or graphic format on all clients running tag logging in Runtime. The data to be displayed always comes from the log server. All operations on the client are transmitted to the server and the result of the processing is transferred back to the client.

#### Alarm log

Alarms in the project indicate fault states and operating states of a process. They are generally triggered by the controller. Alarms are displayed on the HMI device in screens. All the data associated with an alarm and configuration data are saved in an alarm log, for example, alarm class, time stamp and alarm text. Each alarm class can be logged separately. Alarms are logged either automatically or by operator intervention.

### Contexts (RT Unified)

Contexts allow you to view plant units according to a certain viewpoint, e.g. according to a certain customer, product, job or shift.

#### Principle

Contexts always belong to a plant object. They are indicated as follows:

- User-defined contexts:

  Using a program created with the ODK-API
- System-generated contexts:

  For installed Performance Insight and Calendar option packages: Automatically in Runtime

  Example: When a shift starts in Calendar, an archived context value is created with the shift ID

A log entry is generated each time a context (e.g. "Product") is executed. The logged context saves:

- The context value (e.g. "orange lemonade")
- Start time and end time of the execution time
- The quality code

#### Contexts in the trend control and alarm control

You can filter the content of these controls so that only data that has been generated in a specific plant unit and for the context you have selected is displayed. To do this, select a plant object, a context and one of its logged context values.

**Example**

A press house produces juices for various beverage brands. Using contexts, employees can display in runtime which alarms have occurred:

- During the production of a specific product (cloudy apple juice, clear apple juice, pear juice etc.).
- For orders for a specific customer (Schmitt, Schulze, Meier).
- During a specific shift (early shift, late shift, night shift).

#### Contexts in the "Reports" control.

You have the option of linking the generation of reports to the execution of contexts.

If the templates are configured appropriately, the reports available in the control can also contain information about contexts. When a report was generated as an Excel file and reads both contexts and alarms or tag values, you can then use the Excel filter function to filter the alarms and tags by context.

---

**See also**

[Display context-dependent alarms of a plant object (RT Unified)](#display-context-dependent-alarms-of-a-plant-object-rt-unified)
  
[Display context data of the plant objects in a trend control (RT Unified)](#display-context-data-of-the-plant-objects-in-a-trend-control-rt-unified)
  
[Adding contexts (RT Unified)](#adding-contexts-rt-unified)

## Starting and displaying runtime (RT Unified)

This section contains information on the following topics:

- [Internet browsers for WinCC Unified PC (RT Unified)](#internet-browsers-for-wincc-unified-pc-rt-unified)
- [Displaying runtime (RT Unified)](#displaying-runtime-rt-unified)
- [Installing a certificate when accessing via web client (Unified PC) (RT Unified)](#installing-a-certificate-when-accessing-via-web-client-unified-pc-rt-unified)
- [SwacLogin: Errors after complete download (RT Unified)](#swaclogin-errors-after-complete-download-rt-unified)
- [Logging out user (RT Unified)](#logging-out-user-rt-unified)
- [Changing users in runtime (RT Unified)](#changing-users-in-runtime-rt-unified)
- [Starting and stopping a project (RT Unified)](#starting-and-stopping-a-project-rt-unified)
- [Switching the Runtime language (RT Unified)](#switching-the-runtime-language-rt-unified)

### Internet browsers for WinCC Unified PC (RT Unified)

Ensure you have the latest operating system and browser version if you want to access Runtime Unified with this device.

WinCC Unified displays the runtime elements in HTML5. The browser used also has to support this standard. Since the browsers interpret HTML5 differently, it is possible that objects are displayed differently depending on the browser and the browser version used. For example, browsers sometimes display fonts differently.

Compatibility tests were performed for the following browsers. The focus of the compatibility tests was on the browsers marked with *:

| Operating system | Browser |
| --- | --- |
| Microsoft Windows | - Google Chrome* - Microsoft Edge - Mozilla Firefox, Mozilla Firefox ESR |
| Android | - Google Chrome* - Firefox - Edge |
| iOS, Mac | - Safari* - Google Chrome - Firefox - Edge |

**Browser recommendation**

In view of the performance and support of the Runtime standard elements, Google Chrome has proven to be the preferred browser. Its memory requirements are slightly higher than those of the other browsers.

> **Note**
>
> **Operating system and browser version**
>
> For Runtime operation via Android or iOS, always use the latest operating system.
>
> Use the latest browser version.

> **Note**
>
> **Performance differences in different versions of individual browsers**
>
> The browser versions can differ from each other, which can result in different behavior regarding the memory requirements and speed.

> **Note**
>
> **Suitability for continuous operation**
>
> Mozilla Firefox has proven to be problematic in continuous operation.

#### Known browser problems

The following restrictions apply to the following browsers:

| Internet browser | Limitation |
| --- | --- |
| MS Edge | - If you want to start Runtime in Microsoft Edge and enter the address "https://localhost", the error message "INET_E_RESOURCE_NOT_FOUND" appears. In this case, use the address "https://localhost/WebRH". |
| Mozilla Firefox | - High memory capacity utilization in continuous operation |
| Mozilla Firefox ESR | - Support of touch gestures for touch panels as of Firefox ESR V59 |
| Google Chrome | - High memory capacity utilization in uninterrupted duty depending on the version. - On Android: Grid lines with a line width ≤1 are not displayed correctly. This is due to the browser's own line thickness representation. As a solution, it is helpful to use a line width ≥1. - No correct representation of elements that use an SVG graphic as background graphic scaled in the Engineering System. |

Restrictions to the various functions can also occur, such as the availability of the before and after buttons in the controls.

#### Current information on browser problems

You can find up-to-date information on display problems in browsers at the Siemens Online Support under the entry ID 109757952.

### Displaying runtime (RT Unified)

#### Introduction

Use a web browser (web client) to display and operate the Runtime project running on the HMI device. The following options are available to access and display Runtime:

- From the same device (local web client)  
  The web browser is installed on the same device as Runtime.
- Remote access from the same network   
  The device on which the web browser is installed belongs to the same network as the HMI device.
- Remote access from a foreign network   
  The device on which the web browser is installed does not belong to the same network as the HMI device.

#### Requirement

- The Runtime project is loaded on the HMI device.
- The project runs in runtime.
- The user management configuration of the project is active.
- When using the central user management:

  - At least one user is created in the UMC system.
  - The user created in the UMC system has been imported into the TIA Portal project before the loading.
  - The user has function rights via his/her roles to monitor or monitor and operate the Runtime project.
- When using the local user management:

  - Before the loading, at least one user has been created in TIA Portal.
  - The user has been assigned at least one role. The user has function rights via his/her roles to monitor or monitor and operate the Runtime project.
  - At least one user has the "HMI Administrator" role.

#### Procedure

1. To view the Unified start page, enter the Unified URL in the browser address bar:

   "`https://``<IP address of the HMI device or its FQDN or device name>`"

   To display the Unified Runtime page directly, append the following string to the URL: "`/WebRH`"  
   Step 5 is omitted.

   Example: "`https://141.73.65.245/WebRH`"
2. Press Enter.
3. If you are accessing the Runtime of the HMI device from this device for the first time and there is no corresponding certificate, install the certificate in the browser. Then reload the page.
4. The start page of Runtime is displayed.

   ![Procedure](images/142223250059_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/142223250059_DV_resource.Stream@PNG-de-DE.png)

   If WinCC Unified Online Engineering is installed on the device, the "WinCC Unified Configuration" button also appears.
5. Select "WinCC Unified RT".

   The login page of WinCC Unified Runtime is displayed.
6. Specify the user name and password of a runtime user.
7. (Optional) Select the language in which runtime is displayed.
8. Confirm your entry.

   The Runtime project that is running is displayed in the web browser.

**Note**

Whether you enter the IP address, the FQDN (fully qualified domain name) or the device name in the URL depends on how the web server certificate has been bound to the HMI device. This is defined during Runtime installation or later in the "Website settings" step of WinCC Unified Configuration.

If needed, ask your administrator.

The following restrictions apply to entering the URL:

- FQDN: Only if the HM device belongs to a domain
- IP address: Not when using dynamic IP addresses
- Device name: Only when accessing from the same network

**Note**

When using a local web client, you can also enter the "`localhost`" command.

Example: "`https://localhost/WebRH`"

Regardless of whether the web server certificate is already installed in the browser, you will first see a security warning. Bypass this warning by clicking "Advanced" and "Continue to <link> (unsecure)".

**Note**

If you experience display problems in the web client, completely delete the browser data (history, form entries, etc.).

**Note**

After a complete download of a project, an error (SwacLogin) may occur when opening the WinCC Unified Runtime page.

You can find more information at [SwacLogin: Errors after complete download](#swaclogin-errors-after-complete-download-rt-unified).

**Note**

**Displayed runtime language**

When using central user management, runtime is displayed in the language you have selected in the "User login" dialog during login.

If this language is not available for the current project or if the language setting was not set in the central user management, the following language is displayed:

- Engineering with TIA Portal: The language for which the lowest number was configured in the runtime settings.
- Engineering with Online Engineering: The language set as default language in the "Languages" tab in the "Languages and Resources" editor.

If you do not select a language in the "User login" dialog, runtime is displayed in the language that is set for the browser.

---

**See also**

[Changing users in runtime (RT Unified)](#changing-users-in-runtime-rt-unified)
  
[Activating automatic login (RT Unified)](SIMATIC%20Runtime%20Manager%20%28RT%20Unified%29.md#activating-automatic-login-rt-unified)
  
[Starting and stopping a project (RT Unified)](#starting-and-stopping-a-project-rt-unified)
  
[Installing a certificate when accessing via web client (Unified PC) (RT Unified)](#installing-a-certificate-when-accessing-via-web-client-unified-pc-rt-unified)
  
[Activating user management (RT Unified)](SIMATIC%20Runtime%20Manager%20%28RT%20Unified%29.md#activating-user-management-rt-unified)

### Installing a certificate when accessing via web client (Unified PC) (RT Unified)

#### Using root certificates

To enable web browsers to establish a secure connection to WinCC Unified, the root certificate with which the web server certificate of WinCC Runtime was issued must be known in the web browser as a trusted certification authority.

By installing the web server certificate on the PC device, the public root certificate is made available as a download for installation in web browsers on the WinCC Unified home page.

The procedure for installing the root certificate differs depending on your web browser.

#### Use of self-signed certificates

As an alternative to the root certificate, you can use a self-signed certificate.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Security risk from self-signed certificate**  A self-signed certificate is not issued by a trusted certification authority.   If you use a self-signed certificate from an untrustworthy source, the data transfer is not protected from attacks.   Before using self-signed certificates, check the source.   Depending on the firewall and network settings, the use of self-signed certificates may be prohibited. |  |

The installation of self-signed certificates is not supported by all web browsers. Depending on the web browser, it is possible to define exceptions.

For more detailed information, refer to the operating instructions of the web browser.

#### Installing the root certificate for Chrome and Microsoft Edge

Chrome and Microsoft Edge use the Windows system certificate store.

- On devices **with WinCC Unified installation**, whose certificates have been configured with the WinCC Unified Certificate Manager, these web browsers can immediately establish a secure connection to the WinCC Unified web pages because the root certificate has already been installed in the system certificate store.
- On devices **without WinCC Unified Installation** the root certificate must be installed manually.

To install manually, follow these steps (for example, Microsoft Edge):

1. Open the WinCC Unified home page via the URL https://<host name>

   At first, an error message appears:

   ![Installing the root certificate for Chrome and Microsoft Edge](images/129763286923_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate for Chrome and Microsoft Edge](images/129763286923_DV_resource.Stream@PNG-de-DE.png)
2. Open the field with the error details and confirm that you want to open the web page.
3. On the WinCC Unified home page, select the field "Certificate Authority" and confirm "Open file" in the download dialog.

   The root certificate is downloaded to the default download directory.
4. Open the downloaded file.

   The root certificate is opened with the Windows standard form.

   ![Installing the root certificate for Chrome and Microsoft Edge](images/129696632715_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate for Chrome and Microsoft Edge](images/129696632715_DV_resource.Stream@PNG-de-DE.png)
5. To import the root certificate into Windows, select "Install Certificate".
6. In the certificate import wizard, select "Local Machine" as the storage location, "Trusted Root Certification Authority" as the certificate store and start the import process.

#### Installing the root certificate for Firefox

Firefox uses its own certificate store and must therefore be configured manually on each device once:

1. Open the WinCC Unified home page via the URL https://<host name>

   At first, an error message appears.
2. Open the field "Advanced" and confirm the field "Accept the Risk and Continue".

   An exception is entered for this page in the Firefox certificate management.
3. On the WinCC Unified home page, select the field "Certificate Authority".
4. Save the root certificate. To do this, click "Save file" in the Firefox dialog that follows.
5. Store the certificate in the Firefox certificate store. Proceed as follows:

   - Open the "Settings" page of Firefox.
   - Select "Privacy & Security". There you will find the "Certificates" area further down. Open "Show certificates...".
   - In the "Certificate Management" window, select the "Certification authorities" tab:

     ![Installing the root certificate for Firefox](images/142189917195_DV_resource.Stream@PNG-en-US.png)

     ![Installing the root certificate for Firefox](images/142189917195_DV_resource.Stream@PNG-en-US.png)
   - Click "Import" and select the root certificate you saved in step 3.
   - In the window that opens, select the option "This certificate can identify websites" and confirm your selection.

     The connection to Runtime is now secure. In the Firefox address bar it is still displayed as unsecure.
   - To show the connection as secure in the address bar, click "Server" and remove the exception created by step 2.

#### Installing the root certificate on iOS devices

iOS uses its own certificate store and must therefore be configured manually on each device once. An error message also appears when the WinCC Unified home page is opened.

1. Open the field "Advanced" and confirm the field "Accept the Risk and Continue".
2. On the WinCC Unified home page, select the field "Certificate Authority".

   ![Installing the root certificate on iOS devices](images/129766715275_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129766715275_DV_resource.Stream@PNG-de-DE.png)
3. Select "Install".

   ![Installing the root certificate on iOS devices](images/129772560651_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129772560651_DV_resource.Stream@PNG-de-DE.png)
4. Select "Install" again.

   ![Installing the root certificate on iOS devices](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129772966027_DV_resource.Stream@PNG-de-DE.png)

   You see the entry "Trusted".

   ![Installing the root certificate on iOS devices](images/129772977419_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129772977419_DV_resource.Stream@PNG-de-DE.png)
5. Select "General > Info > Certificate Trust Settings".

   ![Installing the root certificate on iOS devices](images/129773293963_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129773293963_DV_resource.Stream@PNG-de-DE.png)
6. Enable "WinCC Unified CA" and select "Next".

   ![Installing the root certificate on iOS devices](images/129773533707_DV_resource.Stream@PNG-de-DE.png)

   ![Installing the root certificate on iOS devices](images/129773533707_DV_resource.Stream@PNG-de-DE.png)

### SwacLogin: Errors after complete download (RT Unified)

After complete download of a project to a Unified PC, an error can occur when you open the WinCC Unified home page. The error can occur regardless of whether you open the home page locally on the PC or from a different device.

A possible cause of the error is the deletion of the browser cache.

#### Error description

In "Chrome" and "MS Edge", the error is displayed with the following alarm:

![Error description](images/142866988171_DV_resource.Stream@PNG-en-US.png)

In "Firefox", the error is displayed with the following alarm:

![Error description](images/142866998283_DV_resource.Stream@PNG-en-US.png)

After accepting the warning of a potential security risk, the page remains empty in Firefox. Only the background screen is visible.

#### Remedy the error in "Chrome" and "MS Edge"

To fix the error in "Chrome" and "MS Edge", proceed as follows:

1. Open a new tab.
2. Enter the URL address of the identity provider of the UMC server in the address line of the browser. The URL is the same as the one in the error message without "/swaclogin", for example, "https://uadtbf-01.asrd-lab.net/umc-sso".
3. The page with a warning regarding the secure connection is displayed.

   ![Remedy the error in "Chrome" and "MS Edge"](images/145919451659_DV_resource.Stream@PNG-en-US.png)
4. Accept the warning by clicking on "Proceed to uadtbf-01.asrd-lab.net (unsafe)".
5. The home page with the "User login" dialog is displayed.

   ![Remedy the error in "Chrome" and "MS Edge"](images/142879972107_DV_resource.Stream@PNG-en-US.png)

#### Remedy the error in "Firefox"

To remedy the error in "Firefox", follow these steps:

1. Open a new tab.
2. Enter the URL address of the identity provider of the UMC server (ring server) in the address line of the browser, for example, "https://uadtbf-01.asrd-lab.net/umc-sso".
3. A blank page opens. Close the page.
4. Refresh the home page with the function key <F5>. The home page with the "User login" dialog is displayed.

---

**See also**

[Displaying runtime (RT Unified)](#displaying-runtime-rt-unified)

### Logging out user (RT Unified)

If you want to end your Runtime session, you have the following options to log out completely:

- Use the "Logout" system function.
- Log out in the user management.
- Close all instances, i.e. open windows, of the browser in use.

#### Requirement

- You are logged in to Runtime.
- When you want to log out in the Runtime project, the system function "Logout" is configured, for example, to the event "Click left mouse button".

#### Logging out in the Runtime project with the system function "Logout"

- Select the button at which the system function "Logout" is configured.

#### Logging out in the user management

- Select "Logout" from the menu.

  Your session is ended.

  ![Logging out in the user management](images/159514733451_DV_resource.Stream@PNG-en-US.png)

  New data downloaded from the TIA Portal is applied during the next login.

### Changing users in runtime (RT Unified)

#### Introduction

In Runtime, the users that are created in the engineering system can log on.

#### Requirement

- The IP address or the fully qualified name (name and domain) of the PC on which Runtime is installed is entered in the browser.

  If Runtime is installed on the same PC as the browser, the "localhost" designation can also be used.
- A user is logged into runtime.

  You log in by selecting "WinCC Runtime RT" or "User management".

#### Procedure

To log off a user and then log on a different user, proceed as follows:

1. Select "User management" on the start page of Runtime.
2. Expand the menu at the top right.
3. Select "Logout".
4. Log in with a different user.

#### Change logged-on user via RFID card

For local Web clients, WinCC Unified Runtime supports login with RFID and PM-LOGON.

**Requirement**

- Runtime uses local user management.
- Logon via RFID is active for the HMI device.

  This setting is made during installation of Runtime or later in WinCC Unified Configuration in the "User management" step.
- PM-LOGON is installed on the HMI device.
- The teach-in of the used RFID card with PM-LOGON is completed.
- An RFID reader supported by PM-LOGON is connected to the HMI device.
- The local web client is opened and connected to Runtime.
- A user is logged into runtime.

**Procedure**

1. Hold the RFID card in front of the reader or insert the card into the reader.
2. If the entry of a PIN was set in PM-LOGON during the teach-in of the card, enter the PIN.

**Result**

After successful validation of the credentials stored on the card, the user logged-on in Runtime is changed.

If the card requires PIN entry and an incorrect PIN is entered, the previously logged-on user remains logged on.

> **Note**
>
> There is no system feedback about the user change. If required, process screens can be configured in engineering to display the logged-on user.

> **Note**
>
> **Additional information on PM-LOGON**
>
> See the PM-LOGON user help for information:
>
> - For licensing and installation of PM-LOGON
> - To the card readers supported by PM-LOGON
> - To the teach-in of the RFID cards.
>
> You can find the PM-LOGON user help at <https://support.industry.siemens.com/cs/document/109810587/pm-logon-manual?dti=0&lc=en-DE>.

### Starting and stopping a project (RT Unified)

A project must be running on the HMI device for Runtime to be displayed.

If no project is running, follow these steps:

1. Start the SIMATIC Runtime Manager tool on the HMI device.
2. Use the tool to get an overview of which projects are loaded on the HMI device.
3. Start the desired project.

You can find more information about the functions of the SIMATIC Runtime Manager and its operation, in the "SIMATIC Runtime Manager" user help.

---

**See also**

[Exporting tags (RT Unified)](OPC%20UA%20-%20Open%20Platform%20Communications%20%28RT%20Unified%29.md#exporting-tags-rt-unified)
  
[SIMATIC Runtime Manager functions (RT Unified)](SIMATIC%20Runtime%20Manager%20%28RT%20Unified%29.md#simatic-runtime-manager-functions-rt-unified)

### Switching the Runtime language (RT Unified)

#### Introduction

The project running on the HMI device can be configured in multiple languages. If a corresponding operating element has been configured, you have the option of switching the language set on the HMI device during ongoing operation.

The project always starts with the language set in the previous session.

#### Requirement

- The desired language for the project is available on the HMI device.
- An operating element is configured, for example, a button that is linked to the language switching function.

#### Procedure

You can switch between the languages at any time in runtime. Language-specific objects are immediately displayed on the screen in the new language when you switch languages.

Depending on the configuration, you have the following options:

- Use a configured operating element to switch from one language to the next in a list.
- Use a configured operating element to directly set the required language.

## Runtime operation (RT Unified)

This section contains information on the following topics:

- [Overview (RT Unified)](#overview-rt-unified)
- [Operation with the touch screen (RT Unified)](#operation-with-the-touch-screen-rt-unified)
- [Zooming and moving in process screens and screen windows (RT Unified)](#zooming-and-moving-in-process-screens-and-screen-windows-rt-unified)
- [Triggering an action (RT Unified)](#triggering-an-action-rt-unified)
- [Entering a value (RT Unified)](#entering-a-value-rt-unified)
- [Moving operator controls (RT Unified)](#moving-operator-controls-rt-unified)
- [Placing the focus on objects (RT Unified)](#placing-the-focus-on-objects-rt-unified)
- [Operating objects with transparent fill (RT Unified)](#operating-objects-with-transparent-fill-rt-unified)
- [Flashing (RT Unified)](#flashing-rt-unified)

### Overview (RT Unified)

#### Operating variants

The following operating options for Runtime are available:

- Operation with the touch screen

  The device of the web client has a touch-sensitive touchscreen. Use your finger or a suitable touch pen to operate the touch screen.
- Mouse and keyboard operation

  The device of the web client has a mouse and keyboard.

Adhere to the instructions for operating the device in the operating instructions.

#### Individually configured operation

The configuration engineer has various options available for setting up operation.

Examples of actions whose execution is always determined on a project-specific basis:

- Screen change
- Reporting
- Change the Runtime language

There are no specific operating elements to execute certain functions. The configuration engineer specifies the project-specific execution. The screen change can be triggered, for example, via a button.

Information on project-specific operations can be found in the system documentation.

### Operation with the touch screen (RT Unified)

This section contains information on the following topics:

- [Overview of operation with the touch screen (RT Unified)](#overview-of-operation-with-the-touch-screen-rt-unified)
- [Supported gestures (RT Unified)](#supported-gestures-rt-unified)
- [Special features of touch operation (RT Unified)](#special-features-of-touch-operation-rt-unified)

#### Overview of operation with the touch screen (RT Unified)

##### Special features when operating using the touch screen

Operation with the touch screen is characterized by the following special features:

- Enable

  To enable the operating element, use your finger or a suitable touch pen to operate the touch screen. To generate a double-click, touch the operating element twice in rapid succession.
- Value input

  You enter numbers and letters on the touch screen with a screen keyboard.

##### Input using the screen keyboard

The screen keyboard is displayed when you select a screen object that requires input. The screen keyboard is hidden again when input is complete.

Further information on the screen keyboard can be found in the operating instructions of the HMI device.

#### Supported gestures (RT Unified)

##### Definition

Various touch gestures are available for the runtime operation on touch devices. Some touch gestures have different effects in the process screens than in the controls.

> **Note**
>
> **No operation with three or more fingers.**
>
> Only use one or two fingers when operating with touch gestures.
>
> If you use more than two fingers with touch gestures, this can cause incorrect operation.
>
> In the case of multi-touch operation with several fingers, you only operate the respectively configured objects.

##### Requirement

- Zoom gestures: Zooming was configured in the engineering.
- Move in process screen and screen window with 2-finger gesture: Zooming was configured in the engineering.

##### Supported touch gestures in process screens

| Icon | Gesture | Function |
| --- | --- | --- |
| ![Supported touch gestures in process screens](images/102214480139_DV_resource.Stream@PNG-de-DE.png) | Tap | To select an object, tap on the corresponding position in the process screen. |
| ![Supported touch gestures in process screens](images/102199055755_DV_resource.Stream@PNG-de-DE.png) | Zoom | To zoom in or zoom out, drag simultaneously with two fingers. For restrictions on the starting point of the gesture, see section [Special features of touch operation](#special-features-of-touch-operation-rt-unified).  The fingers form the zoom center.  With the exception of pop-up windows opened in the process screen, the entire content of the process screen is zoomed. |
| ![Supported touch gestures in process screens](images/102214596107_DV_resource.Stream@PNG-de-DE.png) | Drag with one finger | After zooming in a process screen, you can move the screen section. To do this, drag with one finger in the desired direction. For restrictions on the starting point of the gesture, see section [Special features of touch operation](#special-features-of-touch-operation-rt-unified).  Pop-up windows open in the process screen are not moved with it. |
| ![Supported touch gestures in process screens](images/102214609035_DV_resource.Stream@PNG-de-DE.png)       ![Supported touch gestures in process screens](images/165522157067_DV_resource.Stream@PNG-de-DE.png) | Drag with two fingers | With the appropriate configuration in the engineering, you can also move the screen section with two fingers, as single gesture or in combination with the zoom gesture. |
| ![Supported touch gestures in process screens](images/102214557451_DV_resource.Stream@PNG-de-DE.png) | Keep pressed | To call the shortcut menu, press for longer than a second on the object or the link.  The function corresponds to a right-click. |

##### Supported touch gestures in screen windows

The following gestures in the screen window only affect the screen window, not the process screen:

| Icon | Gesture | Function |
| --- | --- | --- |
| ![Supported touch gestures in screen windows](images/102214596107_DV_resource.Stream@PNG-de-DE.png) | Drag with one finger | After zooming into a screen window, you can move the screen window section. To do this, drag with one finger in the desired direction. For restrictions on the starting point of the gesture, see section [Special features of touch operation](#special-features-of-touch-operation-rt-unified). |
| ![Supported touch gestures in screen windows](images/102214609035_DV_resource.Stream@PNG-de-DE.png)       ![Supported touch gestures in screen windows](images/165522157067_DV_resource.Stream@PNG-de-DE.png) | Drag with two fingers | With the appropriate configuration in the engineering, you can also move the screen window section with two fingers, as a single gesture or in combination with the zoom gesture. |
| ![Supported touch gestures in screen windows](images/102199055755_DV_resource.Stream@PNG-de-DE.png) | Zoom | With corresponding configuration in the engineering, you can enlarge or reduce the screen window section independent of the zoom factor of the process screen. Drag simultaneously with two fingers (zooming).  If the screen window section is smaller than the content configured for the screen window due to zooming, the fingers serve as zoom center, otherwise the upper left corner of the screen window. |

The following gestures work analogously to the gestures supported in the process screen:

- Tap
- Keep pressed

##### Supported touch gestures in controls

| Icon | Gesture | Behavior | Supported WinCC controls |
| --- | --- | --- | --- |
| ![Supported touch gestures in controls](images/102214480139_DV_resource.Stream@PNG-de-DE.png) | Tap | - To select a row, tap the row. - With corresponding configuration of the control: To select a cell. - To sort a column, click on the column header. - In trend controls:  Zooms in on the trend area along the X/Y axis.   Requirement: The "Zoom +/-", "Zoom time axis +/-" or "Zoom value axis +/-" button is pressed. | - Alarm control - Process control - Trend control - f(x) trend control - Ruler window - System diagnostics control - Parameter set control |
| ![Supported touch gestures in controls](images/102214493067_DV_resource.Stream@PNG-de-DE.png) | Tap with two fingers | Zooms out of the trend control. Requirement: The "Zoom +/-", "Zoom time axis +/-" or "Zoom value axis +/-" button is pressed.  Leave a little space between your fingers when tapping. | - Trend control - f(x) trend control |
| ![Supported touch gestures in controls](images/102214609035_DV_resource.Stream@PNG-de-DE.png) | Drag with two fingers | To scroll vertically or horizontally in the table of the control, drag in the control window with two fingers in the desired direction. | - Alarm control - Process control - Ruler window - System diagnostics control - Parameter set control |
| ![Supported touch gestures in controls](images/102214596107_DV_resource.Stream@PNG-de-DE.png) | Drag with one finger | - Moves the ruler. - Moves the X axis or Y axis.    Requirement: The "Move trend area" or "Move axis area" button is pressed or the control is zoomed in. | - Trend control - f(x) trend control |
| To select multiple rows, tap a row and drag your finger up or down.  With corresponding configuration of the control: To select multiple cells. | - Alarm control - Process control - Ruler window - System diagnostics control - Parameter set control |  |  |
| To adapt the column width, tap a column grid line and drag your finger to the right or left. |  |  |  |
| ![Supported touch gestures in controls](images/102214518795_DV_resource.Stream@PNG-de-DE.png) | Double tap | To edit a cell value, double-tap the cell.  Requirement:  - Table view: The "Edit" button is pressed. - Parameter set control: A parameter set is selected. | - Process control - Parameter set control |
| ![Supported touch gestures in controls](images/102199055755_DV_resource.Stream@PNG-de-DE.png) | Zoom | To zoom in or out in the trend control, drag with two fingers in the control window.  Requirement: Trend control is paused and no zoom button is active. Or "Move trend area" is active. | Trend control |
| ![Supported touch gestures in controls](images/102214750987_DV_resource.Stream@PNG-de-DE.png)     ![Supported touch gestures in controls](images/102214712331_DV_resource.Stream@PNG-de-DE.png) | Swiping (horizontally and vertically) | To quickly scroll left or right or up or down within the table of the control, swipe in the corresponding direction. | - Alarm control - Process control - Ruler window - System diagnostics control - Parameter set control |

#### Special features of touch operation (RT Unified)

##### Multi-touch operation of process pictures

WinCC Unified supports multi-touch operation in screens.

##### Simulation of projects with multi-touch functions

WinCC Unified supports the simulation of configured multi-touch functions. Requirement is that your monitor supports multi-touch operation.

##### Restrictions for touch gestures

Do not start the move 1-finger gesture or 2-finger gesture on the following objects:

- Release button
- Buttons with configured "Release" or "Press" event.
- "Browser" controls
- Custom web controls
- Touch area
- Elements and controls that manage touch gestures themselves (e.g. sliders and trend control)

##### Releasing locked operator controls by two-hand operation

Unified supports safe operation of controls that can be used to change critical system settings, such as control variables with machine limits. Such operator controls can be configured as locked.

Locked operator controls are displayed dimmed in runtime. To operate them, simultaneously press the release button provided for this purpose.

Releasing the locked operator controls by pressing the release button has a cross-screen effect on all open screens.

In Runtime, locked operator controls can only be accessed with the tab sequence if a release button is pressed at the same time.

##### Scrolling in lists and controls

You can scroll through lists and controls by dragging.

##### Special features of the trend control

You enlarge or reduce the view in "Trend control" and "function trend control" objects by pinch-to-zoom with two fingers.

Double tap to switch from the magnified trend control back to the normal view.

The zooming function is limited to the time axis in the "Trend control" object.

If you have enabled the option "Range > Auto-size" during configuration of the value axes in function trend control, the axes are constantly calculated during zooming.

Horizontal scrolling is not supported in the "Trend control" object.

> **Note**
>
> **Current view is not persistent**
>
> The changes of zoom factor and position changed by scrolling are not saved.
>
> The trend control is reset to the default setting during a screen change.

### Zooming and moving in process screens and screen windows (RT Unified)

#### Introduction

Depending on the configuration in the engineering, you have the following options in runtime:

|  | Zooming with | Move screen section with |
| --- | --- | --- |
| Process screen | - Mouse - Keyboard - 2-finger gesture | - Mouse - Keyboard - 1-finger gesture - 2-finger gesture |
| Screen window |  |  |

This section describes how to zoom and move using the mouse and keyboard.

For information on zooming and panning with gestures, see sections [Supported gestures](#supported-gestures-rt-unified) and [Special features of touch operation](#special-features-of-touch-operation-rt-unified).

#### General requirement

- The process screen or the screen window has the focus.
- For zooming: Zooming has been configured in the engineering.
- For moving: The process screen or screen window has been zoomed.

#### Starting point

Possible starting points for zooming or moving in process screens and screen windows are:

- An empty area
- Objects that cannot be zoomed or moved by themselves
- Buttons for which no "OnUp" or "OnDown" event has been configured by default

#### Zoom

**Using a mouse**

Your procedure depends on how zooming in engineering was configured in the runtime settings:

|  | Zooming with <Ctrl> configured  (default) | Zooming without <Ctrl> configured |
| --- | --- | --- |
| Zoom in | Hold down <Ctrl> and move the mouse wheel upwards. | Move the mouse wheel upwards. |
| Zoom out | Hold down <Ctrl> and move the mouse wheel downwards. | Move the mouse wheel downwards. |

Scroll center is the mouse pointer.

**Using a keyboard**

- To zoom in, press <Ctrl + Plus>.
- To zoom out, press <Ctrl + Minus>.

Scroll center is the upper left corner.

**Result**

The entire content of the process screen or screen window is zoomed. Open pop-up windows are not zoomed.

#### Moving a screen section

**Using a mouse**

- Move to the left or right: Hold down the left mouse button and move the mouse in the desired direction.
- Move up or down:

  Your procedure depends on how zooming in engineering was configured in the runtime settings:

  |  | Zooming with <Ctrl> configured  (default) | Zooming without <Ctrl> configured |
  | --- | --- | --- |
  | Moving up | Move the mouse wheel upwards. | Hold down <Ctrl> and move the mouse wheel upwards. |
  | Moving down | Move the mouse wheel downwards. | Hold down <Ctrl> and move the mouse wheel downwards. |

**Using a keyboard**

Use the following keys:

- Arrow keys: Move left/right and up/down
- Screen keys: Move up/down
- <Home>: Show upper left corner
- <End>: Show lower right corner

**Result**

The entire content of the process screen or screen window is moved. Open pop-up windows are not moved.

### Triggering an action (RT Unified)

#### Introduction

Triggering an action at an operating element can mean the following:

- A command is executed.

  Example: Click a button to trigger a script or to execute a pre-defined function.
- An object is enabled.

  Example: To enter a value in a list, click in a table cell.

#### Requirement

- You have navigated to the operating element on which you want to trigger the action.
- The operating element has the focus.

#### Procedure

- Tap the operating element on the touchscreen once or twice in quick succession.

#### Result

The following results are possible:

- The requested command is executed.
- The cursor flashes in the input area of the operating element.

  When accessing via touch devices: The screen keyboard opens.
- The element is selected and can be moved.

### Entering a value (RT Unified)

#### Introduction

Depending on the input format, you enter numerical or alphanumerical values in an input box.

#### Requirement

- The object is an input field or table field.
- The operating element is enabled.

#### Entering a value

1. Enter the desired value.
2. To confirm the value, press the <Enter> key or click on a blank area of the screen.
3. To discard the value, press the <Esc> key.

#### Result

The input is accepted or discarded.

The input box still has the focus.

### Moving operator controls (RT Unified)

#### Introduction

There are screen objects with movable operator controls, e.g. a slider.

#### Requirement

- A movable operating element is selected.

#### Procedure

1. To move the operating element, move it while holding down the mouse button or use a corresponding touch gesture, e.g. "Drag" for a slider.

#### Result

The position of the movable operating element and the display in the screen object have changed.

### Placing the focus on objects (RT Unified)

You have the following options:

- Click on the object.

  > **Note**
  >
  > **Giving focus to objects with a transparent background**
  >
  > If an object has a transparent background, click on a visible area of the object.
- Press <Tab> until the object has the focus.

---

**See also**

[Operating objects with transparent fill (RT Unified)](#operating-objects-with-transparent-fill-rt-unified)

### Operating objects with transparent fill (RT Unified)

The objects displayed on a screen can have transparent ranges.   
Example: Sliders, bars and pointer instruments are enclosed by a transparent rectangle.

#### Requirement

An event which is triggered by operating actions such as typing or clicking has been configured for the object in the engineering.

#### Trigger event

To trigger the event, proceed as follows:

- If the object does not have the focus, click a visible part of the object, e.g. its border.
- If the object already has the focus, the event is also triggered by clicking in the transparent area.

### Flashing (RT Unified)

#### Flashing in Runtime

You can display the objects flashing in Runtime. Scripts can be used to switch flashing on and off and influence the properties of the flashing.

Configure the flashing behavior of an object property in the engineering system for each color setting of an object that supports flashing.

> **Note**
>
> The flashing in Runtime does not change the color value of the property.

## Controls (RT Unified)

This section contains information on the following topics:

- [Overview of controls (RT Unified)](#overview-of-controls-rt-unified)
- [Operating alarms (RT Unified)](#operating-alarms-rt-unified)
- [Displaying tags in Runtime (RT Unified)](#displaying-tags-in-runtime-rt-unified)
- [Screen window (RT Unified)](#screen-window-rt-unified)
- [Web control (RT Unified)](#web-control-rt-unified)
- [Media player](#media-player)
- [System diagnostics display (RT Unified)](#system-diagnostics-display-rt-unified)
- [Plant overview (RT Unified)](#plant-overview-rt-unified)
- [Plant overview with companion controls (RT Unified)](#plant-overview-with-companion-controls-rt-unified)
- [Parameter set control (RT Unified)](#parameter-set-control-rt-unified)
- [Reports (RT Unified)](#reports-rt-unified)
- [Rearranging columns at runtime (RT Unified)](#rearranging-columns-at-runtime-rt-unified)
- [Process diagnostics (RT Unified)](#process-diagnostics-rt-unified)

### Overview of controls (RT Unified)

Runtime has operable controls in process pictures.

The following controls are available depending on the configured access rights:

| Icon | Control | Brief description |
| --- | --- | --- |
| ![Figure](images/100796109323_DV_resource.Stream@PNG-de-DE.png) | Screen window | Displays other screens of the object. |
| ![Figure](images/100799422347_DV_resource.Stream@PNG-de-DE.png) | Trend control | Displays graphical representations of tag values from the current process or from a log in the form of trends with values over time from the controller or a log. |
| ![Figure](images/100799323915_DV_resource.Stream@PNG-de-DE.png) | f(x) trend control | Represents the values of a tag as a function of another tag. |
| ![Figure](images/100799237387_DV_resource.Stream@PNG-de-DE.png) | Browser | Displays HTML pages. |
| ![Figure](images/100799726475_DV_resource.Stream@PNG-de-DE.png) | Media Player | Enables video and audio files to be played. |
| ![Figure](images/100799315083_DV_resource.Stream@PNG-de-DE.png) | Alarm control | Shows currently pending alarms or alarm events from the alarm buffer or alarm log. |
| ![Figure](images/100799610379_DV_resource.Stream@PNG-de-DE.png) | Process control | Represents current or logged process data in a table. |
| ![Figure](images/100799619211_DV_resource.Stream@PNG-de-DE.png) | Trend companion | Displays evaluated data and statistics in a table. |
| ![Figure](images/113765875339_DV_resource.Stream@PNG-de-DE.png) | Parameter set control | Shows the parameter sets with which the PLC is set up for production. |
| ![Figure](images/143103268619_DV_resource.Stream@PNG-de-DE.png) | System diagnostics control | Shows the diagnostic status of multiple PLCs via traffic light SVGs. |
| ![Figure](images/158428626827_DV_resource.Stream@PNG-de-DE.png) | GRAPH overview | Displays the current program status for executed steps of the GRAPH sequencer. |
| ![Figure](images/158428635403_DV_resource.Stream@PNG-de-DE.png) | PLC code view | Displays the current program status of user programs. |
| ![Figure](images/165186523659_DV_resource.Stream@PNG-de-DE.png) | ProDiag overview | Provides an overview of the current status of the configured monitoring. |

### Operating alarms (RT Unified)

This section contains information on the following topics:

- [Basics of alarms (RT Unified)](#basics-of-alarms-rt-unified)
- [Alarm control overview (RT Unified)](#alarm-control-overview-rt-unified)
- [Buttons of the alarm control (RT Unified)](#buttons-of-the-alarm-control-rt-unified)
- [Operate alarm control (RT Unified)](#operate-alarm-control-rt-unified)
- [Filtering alarms (RT Unified)](#filtering-alarms-rt-unified)
- [Display alarms for plant objects (RT Unified)](#display-alarms-for-plant-objects-rt-unified)
- [Display context-dependent alarms of a plant object (RT Unified)](#display-context-dependent-alarms-of-a-plant-object-rt-unified)
- [Sorting alarms (RT Unified)](#sorting-alarms-rt-unified)
- [Disabling individual alarms (RT Unified)](#disabling-individual-alarms-rt-unified)
- [Shelving alarms (RT Unified)](#shelving-alarms-rt-unified)
- [Acknowledging (RT Unified)](#acknowledging-rt-unified)
- [Logging alarms (RT Unified)](#logging-alarms-rt-unified)
- [Displaying alarm statistics (RT Unified)](#displaying-alarm-statistics-rt-unified)
- [Operating alarm statistics (RT Unified)](#operating-alarm-statistics-rt-unified)

#### Basics of alarms (RT Unified)

This section contains information on the following topics:

- [Alarm system (RT Unified)](#alarm-system-rt-unified)
- [Alarms (RT Unified)](#alarms-rt-unified-1)
- [Alarm blocks](#alarm-blocks)
- [Alarm classes](#alarm-classes)
- [Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
- [Alarm states](#alarm-states)

##### Alarm system (RT Unified)

###### Introduction

Alarms show events, operating modes or faults that occur in runtime in the plant.

You can use alarms for diagnostic purposes, for example, when troubleshooting. They will help you to immediately locate the cause of the fault. You can adjust your processes through targeted intervention so that compliant products continue to be produced despite the fault, or the process is stabilized, and the fault only causes a minimal loss of production.

The acquired alarms are displayed on the HMI device in screens. The alarm system logs the alarms from the ongoing process. Targeted access to the alarms combined with supplementary information about individual alarms ensures that faults are localized and cleared quickly. This reduces stoppages or even prevents them altogether.

###### The alarm system in WinCC Unified Scada

The alarm system distinguishes between the following alarms:

|  |  |  |
| --- | --- | --- |
| User-defined alarms | Analog alarms | Display limit value violations (value changes)   They are used to monitor the plant. |
| Discrete alarms | Display status changes   They are used to monitor the plant. |  |
| User-defined PLC alarms | Displays the status values of the PLC.   They are used to monitor the plant and are configured in STEP 7. |  |
| System-defined alarms | System alarms | Are included in the HMI device.   They are used to monitor the HMI device. |
| System-defined PLC alarms | They consist of system diagnostic alarms and system errors.   They are used to monitor the PLC.  The types of system-defined PLC alarms depend on the PLC used. |  |

![The alarm system in WinCC Unified Scada](images/147472166795_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Analog alarms (RT Unified)](#analog-alarms-rt-unified)
  
[Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)
  
[User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)
  
[System alarms (RT Unified)](#system-alarms-rt-unified)
  
[System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)
  
[Alarm control overview (RT Unified)](#alarm-control-overview-rt-unified)

##### Alarms (RT Unified)

This section contains information on the following topics:

- [User-defined alarms (RT Unified)](#user-defined-alarms-rt-unified)
- [System-defined alarms (RT Unified)](#system-defined-alarms-rt-unified)

###### User-defined alarms (RT Unified)

This section contains information on the following topics:

- [Analog alarms (RT Unified)](#analog-alarms-rt-unified)
- [Discrete alarms (RT Unified)](#discrete-alarms-rt-unified)
- [User-defined PLC alarms (RT Unified)](#user-defined-plc-alarms-rt-unified)

###### Analog alarms (RT Unified)

###### Description

Analog alarms display limit violations. An analog alarm is triggered when the value of the trigger tag meets the trigger condition defined on the analog alarm.

Depending on the selected trigger condition, the alarm is triggered, for example, when the condition value is higher than, lower than, or the same as the defined value.

###### Example

When the motor speed reaches a critical range as defined in the engineering, an alarm with matching alarm text is displayed. The alarm text can provide the operator with specific instructions on how to check and remedy the situation.

###### Discrete alarms (RT Unified)

###### Description

A discrete alarm is triggered when the value of a specific bit of a tag changes. The discrete alarms indicate status changes in a plant and are triggered by a controller.

###### Example

Imagine that the state of a valve is to be monitored during operation. The state of the valve is "open" or "closed".

A discrete alarm is configured for each state of the valve. If the status of the valve changes, a discrete alarm is output, containing for example the following alarm text: "Valve closed".

###### User-defined PLC alarms (RT Unified)

###### Example of an alarm

"The temperature in Tank 2 is too high."

###### Description

A user-defined PLC alarm maps the status values of a PLC, for example, time stamp and process values. It is created by a PLC project engineer in STEP 7.

The PLC alarms configured in STEP 7, are applied into the integrated WinCC operation as soon as a connection is established to the PLC.

> **Note**
>
> **Automatic update of new or modified PLC alarms on the HMI device**
>
> If PLC alarms are configured in STEP 7 and an HMI connection to a SIMATIC S7-1500 controller (firmware version 2.0 or higher) is established, and the PLC and HMI device are configured accordingly in the engineering, the PLC alarms are sent to the HMI device and updated automatically. You can find more information in the TIA Portal help for WinCC Unified.

> **Note**
>
> WinCC only supports PLC alarms of a SIMATIC S7-1500 controller. In addition, WinCC only supports PLC alarms that are automatically updated by the central alarm management in the PLC.

###### System-defined alarms (RT Unified)

This section contains information on the following topics:

- [System alarms (RT Unified)](#system-alarms-rt-unified)
- [System-defined PLC alarms (RT Unified)](#system-defined-plc-alarms-rt-unified)

###### System alarms (RT Unified)

###### Description

A system alarm indicates the status of the system and communication errors between the HMI device and the system. System alarms are output in runtime in the configured alarm control. System alarms are output in the language currently set on your HMI device.

The time format (AM/PM or 24-hour format) is based on the selected language. If no translation of the alarm texts exists in this language, English is used as replacement and the corresponding time format is displayed.

###### Example of an alarm

"Memory is full!"

###### System-defined PLC alarms (RT Unified)

> **Note**
>
> **Device dependency**
>
> System-defined PLC alarms are not available for all HMI devices.

###### Description

System-defined PLC alarms are installed with STEP 7 and are only available if WinCC is operated in the STEP 7 environment.

System-defined PLC alarms are used to monitor states and events of a PLC. System-defined PLC alarms consist of system diagnostic alarms and system errors (RSE)

> **Note**
>
> **Automatic update of system diagnostic alarms on the HMI device**
>
> When an HMI connection to a SIMATIC S7-1500 controller (firmware version 2.0 or higher) is established, and the PLC and the HMI device were configured accordingly in the engineering, the system diagnostic alarms are sent to the HMI device and updated automatically. You can find more information in the TIA Portal help for WinCC Unified.

> **Note**
>
> Note the following restrictions:
>
> - WinCC only supports system diagnostic alarms of a SIMATIC S7-1500 controller.
> - WinCC only supports system diagnostic alarms that are automatically updated by the central alarm management in the PLC.

###### Example of an alarm

"CPU maintenance required"

##### Alarm blocks

###### Overview

In Engineering you configure which columns you can see in runtime and which alarm blocks the columns are evaluating. The following section provides an overview of some important alarm blocks.

Example of alarm blocks output in runtime:

| Alarm class | Alarm number | Time of occurrence | State machine | Alarm text | Information | Value | Limit value |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Warning | 1 | 08/27/2017 11:09:14 AM | Alarm with single-mode acknowledgment | Maximum speed reached | This alarm is... | 50 | 27 |

###### Alarm class

The alarm class controls, for example, the display and the acknowledgment concept of the alarm.

###### Alarm number

You identify an alarm by its number (ID).

Change the alarm number, if necessary; for example, with a consecutive alarm number to mark alarms that belong together in your project.

> **Note**
>
> The alarm number of a system alarm has a higher priority than the number of a user-defined alarm. Do not use numbers that are used by system alarms for user-defined alarms.

###### Alarm blocks with time and date

These alarm blocks show the time at which the alarm was active, acknowledged or became inactive, etc.

> **Note**
>
> **Time zones**
>
> By default, the time stamp in the alarm display is converted into the time zone used by the HMI device.
>
> If the alarm display is configured accordingly, the time stamp can be converted to another time zone in Runtime via the "Time base configuration" button.

###### State machine

An alarm has the state machine or the acknowledgment concept of the alarm class.

The state machine is the way an alarm is displayed in various states and processed by the system.

See section [Acknowledgment model](#acknowledgment-model-rt-unified).

###### Alarm state

An alarm always has a specific alarm state in runtime, for example, active or active/acknowledged. Based on the alarm state, you can understand the process that the alarm went through.

###### Alarm text

The alarm text (event text) describes the cause of the alarm.

The alarm text can contain output fields for current values. The value is retained at the time at which the alarm status changes.

###### Priority

Displays the priority of individual alarms.

> **Note**
>
> A priority configured on the alarm has precedence in runtime over the priority configured on the alarm class.

###### Limit value

Analog alarms display limit violations. Depending on the configuration, WinCC outputs the analog alarm as soon as the trigger tag exceeds or undershoots the configured limit value.

###### Computer

Operator input alarms have the "Computer" column in the alarm summary. The computer name is displayed for local alarms and the IP address for alarms from the web client.

###### Users

The user acknowledges the alarm. If an empty user name is passed to an alarm, it does not represent a user name.

For alarms triggered by a variable, no user name is shown in the alarm display.

###### Duration

Returns the time interval in nanoseconds between triggering of the alarm and its previous status change.

---

**See also**

[Alarm classes](#alarm-classes)

##### Alarm classes

###### Introduction

Many alarms occur in a plant; these are all of different importance. To make it clear to you, which alarms are most important, alarms are assigned to alarm classes.

Assignment of the alarms to alarm classes and configuration of the alarm classes takes place in the engineering system.

###### Purpose

The alarm class of an alarm defines the following:

- State machine/acknowledgment model
- Appearance in alarm control (e.g. color)
- Priority

  > **Note**
  >
  > The priority configured on the alarm has precedence in runtime over the priority configured on the alarm class.
- Logging

###### Examples of how to use alarm classes

- The alarm class of the alarm "Fan 1 speed in upper tolerance range" is "Warning". The alarm is displayed with a yellow background. The alarm does not require acknowledgment.
- The alarm "Speed of fan 2 has exceeded upper warning range" is assigned to the "Alarm" alarm class. The alarm is displayed with a red background and flashes at high frequency in runtime. The alarm is displayed until you have acknowledged it.

###### User-defined and predefined alarm classes

The alarms use user-defined or predefined alarm classes:

- Number and configuration of user-defined alarm classes depend on the configuration of the runtime project in the engineering.
- The number and configuration of predefined alarm classes are provided by the system.

  You can find more information on predefine alarm classes in the TIA Portal help for WinCC Unified as well as in the user help for WinCC Unified Online Engineering.

---

**See also**

[Acknowledgment model (RT Unified)](#acknowledgment-model-rt-unified)
  
[Logging basics (RT Unified)](#logging-basics-rt-unified)

##### Acknowledgment model (RT Unified)

###### Introduction

The state machine of an alarm class regulates which statuses the alarms of this alarm class can have. From this it is derived which events can occur for them and whether and how they are acknowledged.

###### State machines

The following state machines are available for HMI alarm classes:

| State machine | Description | Use in predefined alarm classes |
| --- | --- | --- |
| Active | Alarm without inactive state without acknowledgment   This alarm is only displayed in the views "Show logged alarms" and "Show and update logged alarms". | Information  OperatorInputInformation  SystemInformation |
| Active and inactive | Alarm without acknowledgment   This alarm becomes active and inactive without having to be acknowledged. | Notification  SystemNotification |
| Active, requires acknowledgment | Alarm without inactive state with acknowledgment   This alarm must be acknowledged as soon as the event that triggers the alarm occurs. The alarm is pending until it is acknowledged. | AlarmWithoutClearEvent  SystemAlarmWithoutClearEvent  SystemWarningWithoutClearEvent |
| Active and inactive, requires acknowledgment | Alarm with a single acknowledgment  This alarm must be acknowledged as soon as the event that triggers the alarm occurs. The alarm is pending until it is acknowledged and inactive. | Alarm  Critical  OperatorInputRequest  SystemAlarm  SystemWarning  Warning |
| Active and inactive, requires acknowledgment and reset | Alarm with acknowledgment and confirmation   The alarm requires acknowledgment once the event that triggers, the alarm has occurred, or the alarm has been reset. In addition, the alarm requires confirmation when the event that triggers the alarm is no longer pending. The alarm is pending until it is acknowledged and confirmed. | AlarmWithReset  CriticalWithReset  WarningWithReset |

The following state machines are available for HMI alarm classes that are associated with common alarm classes:

- Alarm with a single acknowledgment
- Alarm without acknowledgment

###### Alarms requiring acknowledgment

Alarms that indicate critical or hazardous states in the process must be acknowledgeable. Every change in the status of an alarm that requires acknowledgment is logged.

Acknowledging the alarm confirms knowledge of the condition that caused the alarm. You acknowledge the alarm using the buttons in the alarm control.

###### Acknowledgment and confirmation of alarms

- Group acknowledgment of alarms in the alarm control

  With the "Acknowledge visible alarms" button you acknowledge all alarms pending in the alarm control that are visible and require acknowledgment.
- Single acknowledgment of alarms in the alarm control

  With the "Single acknowledgment" button you acknowledge a single alarm that is selected in the alarm control.
- Single acknowledgment of alarms with acknowledgment and confirmation in the alarm control

  With the "Single acknowledgment" button you acknowledge a single alarm with the state machine "Alarm with acknowledgment and confirmation" after it was previously acknowledged via group acknowledgment or single acknowledgment and was inactive.

> **Note**
>
> If the "Show recent" button is active, the most recent alarm is always displayed first and is selected.
>
> Group acknowledgment is only carried out for the visible alarms.

---

**See also**

[Alarm states](#alarm-states)

##### Alarm states

###### Description

Each alarm has an alarm state. Alarm states are made up from the following events:

- **Active**

  The condition for triggering an alarm is fulfilled. The alarm is displayed, such as "Boiler pressure too high".
- **Inactive**

  The condition for triggering an alarm is no longer fulfilled. The alarm is no longer displayed as the boiler was vented.
- **Acknowledged**

  The operator has acknowledged the alarm.

The alarm state of an alarm at any given time depends on the following factors:

- Which state machine has its alarm class.

  The state machine of an alarm class regulates which events can occur for alarms of this alarm class. From this it is derived which states the alarms can have and whether and how they are acknowledged.

  For an overview of the available state machines, see [Acknowledgment model](#acknowledgment-model-rt-unified).
- Which events occurred for the alarm.

> **Note**
>
> The display texts of the alarm states are different depending on the language and configuration. The texts displayed in Runtime can deviate from the texts shown here.
>
> The active and inactive alarm states can also be displayed in Runtime with Raised and Cleared respectively.
>
> Alarm states are visible to the operator in Runtime through status texts. The status texts can be configured in the Runtime settings.

###### Alarms without acknowledgment

The following table shows the alarm states for alarms without acknowledgment:

| Icon | Alarm state | Status text | Description |
| --- | --- | --- | --- |
| ![Alarms without acknowledgment](images/113621246475_DV_resource.Stream@PNG-de-DE.png) | Active | Incoming | The condition of an alarm is fulfilled.  The alarm does not need to be acknowledged. |
| ![Alarms without acknowledgment](images/113621250187_DV_resource.Stream@PNG-de-DE.png) | Inactive | Normal | The condition of an alarm is no longer fulfilled.  The alarm is no longer pending. |

###### Alarms with acknowledgment

The following table shows the alarm states for alarms with acknowledgment:

| Icon | Alarm state | Status text | Description |
| --- | --- | --- | --- |
| ![Alarms with acknowledgment](images/113621246475_DV_resource.Stream@PNG-de-DE.png) | Active | Incoming | The condition of an alarm is fulfilled. |
| ![Alarms with acknowledgment](images/113621250187_DV_resource.Stream@PNG-de-DE.png) | Active/inactive | Incoming/Outgoing | The condition of an alarm is no longer fulfilled.  The operator has not acknowledged the alarm. |
| ![Alarms with acknowledgment](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Active/inactive/acknowledged | Normal | The condition of an alarm is no longer fulfilled.  The operator has acknowledged the alarm after this time. |
| ![Alarms with acknowledgment](images/113622144139_DV_resource.Stream@PNG-de-DE.png) | Active/acknowledged | Incoming/Acknowledged | The condition of an alarm is fulfilled.  The operator has acknowledged the alarm. |
| ![Alarms with acknowledgment](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Active/acknowledged/inactive | Normal | The condition of an alarm is no longer fulfilled.  The operator acknowledged the alarm while the condition was still fulfilled. |

###### Alarms requiring acknowledgment and confirmation

The following table shows the alarm states for alarms requiring acknowledgment and confirmation:

| Icon | Alarm state | Status text | Description |
| --- | --- | --- | --- |
| ![Alarms requiring acknowledgment and confirmation](images/113621246475_DV_resource.Stream@PNG-de-DE.png) | Active | Incoming | The condition of an alarm is fulfilled. |
| ![Alarms requiring acknowledgment and confirmation](images/113621250187_DV_resource.Stream@PNG-de-DE.png) | Active/inactive | Incoming/Outgoing | The condition of an alarm is no longer fulfilled.   The user has not acknowledged the alarm. |
| ![Alarms requiring acknowledgment and confirmation](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Active/inactive/acknowledged | Incoming/outgoing/acknowledged | The condition of an alarm is no longer fulfilled.   The user acknowledged the alarm after this time. |
| ![Alarms requiring acknowledgment and confirmation](images/113622144139_DV_resource.Stream@PNG-de-DE.png) | Active/acknowledged | Incoming/Acknowledged | The condition of an alarm is fulfilled.   The user has acknowledged the alarm. |
| ![Alarms requiring acknowledgment and confirmation](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Active/acknowledged/inactive | Incoming/acknowledged/outgoing | The condition of an alarm is no longer fulfilled.   The user has acknowledged the alarm while the condition was still fulfilled. |
| ![Alarms requiring acknowledgment and confirmation](images/113622144139_DV_resource.Stream@PNG-de-DE.png) | Normal | Normal | The condition of an alarm is fulfilled.  The user has acknowledged and confirmed the alarm. |

###### Disabled alarms

Operators disable an alarm to, for example, prevent a nuisance alarm from impairing the effectiveness of the system.

- Disabled: The alarm has been deactivated (locked). The alarm transitions to its final state without any further state transitions.
- Not disabled: The alarm is activated (enabled). The alarm is visible again in its last state.

###### Shelved alarms

The display of specific alarms is shelved (suppressed) in order, for example, not to overload the operator with information. Manually reset: The alarm was manually reset by the operator. Shelved due to design: The alarm was automatically shelved due to a condition and is automatically hidden in Runtime.

#### Alarm control overview (RT Unified)

##### Introduction

The alarm control displays PLC alarms and HMI alarms that occur during the process in a plant. The alarm control helps prevent faults in the plant or localize and remedy the causes of a fault.

##### User interface

![User interface](images/168652073355_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Columns for the output alarm blocks |
| ② | Alarm summary  Each alarm is displayed in a separate line.  The alarms that are displayed depend on the view or list selected and whether filters are applied. |
| ③ | Toolbar for operating the alarm control |
| ④ | Information bar |

> **Note**
>
> Selection of alarm blocks, column titles and localization depend on the configuration in engineering.

> **Note**
>
> An alarm appears in the alarm control with the date and time stamp crossed out in the following situations:
>
> - A disabled alarm is enabled again.
> - An alarm is reloaded after a power failure. This applies only to chronological alarming.
> - The automation system is restarted. This applies only to chronological alarming.

##### Views and lists

Depending on the configuration of the alarms and the situation in the system, a large number of alarms can occur in runtime.

The alarm control offers various views and alarm lists that filter the alarm summary and thus provide a better overview:

| View | Description |  |  |
| --- | --- | --- | --- |
| Alarm view | Shows the alarms of the currently selected alarm list.  Available alarm lists: |  |  |
| ![Views and lists](images/104684708875_DV_resource.Stream@PNG-de-DE.png) | Display active alarms | Shows the pending alarms.  If the toolbar is configured accordingly, you use the "Display options setup" button to set the alarms that are displayed in this list.  Default setting: Displays all alarms that are not suppressed. |  |
| ![Views and lists](images/104619907083_DV_resource.Stream@PNG-de-DE.png) | Show logged alarms | Shows the logged alarms.  The display is not updated immediately when new incoming alarms occur. |  |
| ![Views and lists](images/104619914507_DV_resource.Stream@PNG-de-DE.png) | Show and update logged alarms | ​Updates the logged alarms and shows them.   ​The display is updated immediately when new incoming alarms occur. |  |
| ![Views and lists](images/132459375883_DV_resource.Stream@PNG-de-DE.png) | Display defined alarms | ​Displays the defined alarms.​  If the toolbar is configured accordingly, you use the "Display options setup" button to set the alarms that are displayed in this list. |  |
| Alarm statistics | ![Views and lists](images/139055173387_DV_resource.Stream@PNG-de-DE.png) | Displays statistical calculations of logged alarms. |  |

You enable a view or list using the corresponding button in the toolbar.

##### Information bar

The information bar shows the different states related to the alarm servers. The information bar contains the following icons:

| Icon | Meaning |
| --- | --- |
| ![Information bar](images/113612240779_DV_resource.Stream@PNG-de-DE.png) | Shows the status to the alarm servers:  No faulty connections |
| ![Information bar](images/113613266699_DV_resource.Stream@PNG-de-DE.png) | Shows the status to the alarm servers:  Faulty connections |
| ![Information bar](images/113612887947_DV_resource.Stream@PNG-de-DE.png) | Shows the status to the alarm servers:  All connections are faulty |

With the corresponding configuration in engineering, the information bar shows the number of alarms that are not acknowledged in runtime. The counter includes all connected servers, but no filters.

When a context is selected, the information bar shows the values of the selected context.

##### Icons for the alarm state

The column for the alarm state can contain the following icons:

| Icon | Meaning |
| --- | --- |
| In "Show and update logged alarms" list: |  |
| ![Icons for the alarm state](images/113621246475_DV_resource.Stream@PNG-de-DE.png) | Alarm is active |
| ![Icons for the alarm state](images/113621250187_DV_resource.Stream@PNG-de-DE.png) | Alarm is inactive |
| ![Icons for the alarm state](images/113621389835_DV_resource.Stream@PNG-de-DE.png) | Alarm acknowledged |
| In the other lists: |  |
| ![Icons for the alarm state](images/113621246475_DV_resource.Stream@PNG-de-DE.png) | Alarm is active |
| ![Icons for the alarm state](images/113621250187_DV_resource.Stream@PNG-de-DE.png) | Alarm is active/inactive |
| ![Icons for the alarm state](images/113622144139_DV_resource.Stream@PNG-de-DE.png) | Alarm is active/acknowledged |

##### Performance data for SIMATIC Unified PC

| Symbol | Meaning |
| --- | --- |
| Number of controller alarms | 160000 |
| Number of OPC UA A&C alarms | 20000 |
| Number of alarms per second (continuous load) | 20 |
| Number of pending alarm events | Unlimited |
| Number of alarms per 10 seconds (alarm burst) | 8000 |

The maximum number of alarms that can be displayed in Runtime depends on the selected view:

| View | Maximum number of alarms that can be displayed. |
| --- | --- |
| Display active alarms | No limit |
| Display defined alarms |  |
| Alarm statistics |  |
| Show logged alarms | 1000 |
| Show and update logged alarms | 100 |

---

**See also**

[Buttons of the alarm control (RT Unified)](#buttons-of-the-alarm-control-rt-unified)

#### Buttons of the alarm control (RT Unified)

You operate the alarm control using the buttons on the toolbar. The buttons that are available depend on the configuration:

| Button |  | Description |
| --- | --- | --- |
| ![Figure](images/105737677579_DV_resource.Stream@PNG-de-DE.png) | Show active alarms | Show the currently pending alarms.  With the ""Active alarms" setup" button, you set which alarms belong to the active alarms. |
| ![Figure](images/105744561419_DV_resource.Stream@PNG-de-DE.png) | Show logged alarms | Shows the logged alarms.   The display is not updated immediately when new incoming alarms occur. |
| ![Figure](images/105743986699_DV_resource.Stream@PNG-de-DE.png) | Show and update logged alarms | Updates the logged alarms and shows them.   The display is updated immediately when new active alarms occur. |
| ![Figure](images/139055173387_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics - View | Visualizes statistical information of logged alarms, such as frequency and display duration. |
| ![Figure](images/140319034891_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics - Configuration | Setting options for calculating the alarm statistics. |
| ![Figure](images/111480751883_DV_resource.Stream@PNG-de-DE.png) | Show defined alarms | Shows the alarms configured in the system. |
| ![Figure](images/111484705035_DV_resource.Stream@PNG-de-DE.png) | Alarm annunciator | Shows all alarms for which the alarm annunciator was configured. The alarm annunciator is a visual or acoustic signal, such as a horn or warning light, that is displayed in addition to the alarm control in the system. |
| ![Figure](images/105744876811_DV_resource.Stream@PNG-de-DE.png) | First line | Selects the first of the displayed alarms. The visible area of the alarm control is moved, if required.   This button can only be operated if the "Alarms - Show recent" button is disabled. |
| ![Figure](images/105744888075_DV_resource.Stream@PNG-de-DE.png) | Previous line | Selects the previous alarm, starting from the currently selected alarm. The visible area of the alarm control is moved, if required.   The button can only be operated if the "Alarms - Show recent" button is disabled. |
| ![Figure](images/105744963339_DV_resource.Stream@PNG-de-DE.png) | Next line | Selects the next alarm, starting from the currently selected alarm. The visible area of the alarm control is moved, if required.   The button can only be operated if the "Alarms - Show recent" button is disabled. |
| ![Figure](images/105745358603_DV_resource.Stream@PNG-de-DE.png) | Last line | Selects the last of the displayed alarms. The visible area of the alarm control is moved, if required.   This button can only be operated if the "Alarms - Show recent" button is disabled. |
| ![Figure](images/132459718923_DV_resource.Stream@PNG-de-DE.png) | Move to next acknowledgeable alarm | Selects the next alarm that requires acknowledgment, starting from the currently selected alarm. The visible area of the alarm control is moved, if required.   This button can only be operated if the "Alarms - Show recent" button is disabled. |
| ![Figure](images/111747071115_DV_resource.Stream@PNG-de-DE.png) | Previous page | Navigates to the previous page. |
| ![Figure](images/111753102091_DV_resource.Stream@PNG-de-DE.png) | Next page | Navigates to the next page. |
| ![Figure](images/124795642507_DV_resource.Stream@PNG-de-DE.png) | Single acknowledgment | Acknowledges the selected alarm.   If using the multiple selection, the selected alarms which require single acknowledgment are not acknowledged.  A counter shows how many alarms are not acknowledged. The counter includes all connected servers, but no filters. |
| ![Figure](images/105744839947_DV_resource.Stream@PNG-de-DE.png) | Acknowledge visible alarms | Acknowledges all pending, visible and acknowledgeable alarms in the alarm control, if they are not individually acknowledgeable. |
| ![Figure](images/111753200523_DV_resource.Stream@PNG-de-DE.png) | Single confirm | Resets the alarm. Relevant for alarms with the state machine "Alarm with acknowledgment and confirmation", which were already acknowledged and inactive. |
| ![Figure](images/105745483787_DV_resource.Stream@PNG-de-DE.png) | Alarms - Show recent | Defines whether it is always the latest alarm that is selected in the alarm control.   Button not pressed: The "Alarms - Show recent" button is active:  - The most current alarms are always shown first in the alarm control.    Alarms that have been filtered out of the alarm control are not displayed. - The visible area of the alarm control moves automatically, if necessary. - You cannot select the alarms individually or sort them by column.   Button pressed: The "Alarms - Show recent" button is paused. |
| ![Figure](images/111753208843_DV_resource.Stream@PNG-de-DE.png) | Info text - configuration | Opens a dialog that shows a help text configured for the selected alarm. |
| ![Figure](images/100729025803_DV_resource.Stream@PNG-de-DE.png) | Comment - configuration | Opens a dialog for adding a comment. |
| ![Figure](images/111754662795_DV_resource.Stream@PNG-de-DE.png) | Disable alarm | Disables an alarm. |
| ![Figure](images/111754670347_DV_resource.Stream@PNG-de-DE.png) | Enable alarm | Enables a disabled alarm. |
| ![Figure](images/111756030987_DV_resource.Stream@PNG-de-DE.png) | Shelve alarm | Resets an alarm, for example, to prevent a nuisance alarm from impairing the effectiveness of your system. |
| ![Figure](images/111756039563_DV_resource.Stream@PNG-de-DE.png) | Unshelve alarm | Cancels the reset of the respective alarm. |
| ![Figure](images/111756858507_DV_resource.Stream@PNG-de-DE.png) | Copy lines | Copies the selected alarms. |
| ![Figure](images/111758608395_DV_resource.Stream@PNG-de-DE.png) | Time base - configuration | Opens a dialog for setting the time zone for the time information shown in alarms. |
| ![Figure](images/111759508747_DV_resource.Stream@PNG-de-DE.png) | Selection display | Opens a dialog for filtering alarms. Define your own filter criteria or change or remove filters defined in the engineering system. |
| ![Figure](images/105745382667_DV_resource.Stream@PNG-de-DE.png) | Sorting setup | Opens a dialog for setting custom sorting criteria for displayed alarms. |
| ![Figure](images/111759500171_DV_resource.Stream@PNG-de-DE.png) | Display options - configuration | Opens a dialog in which you set which alarms the currently displayed alarm list displays. |
| ![Figure](images/111760208523_DV_resource.Stream@PNG-de-DE.png) | Disabled alarms - Configuration | Opens a dialog for configuring the display options of the disabled alarms. |
| ![Figure](images/105745968651_DV_resource.Stream@PNG-de-DE.png) | Export | Starts the export of alarms to a CSV file. |
| ![Figure](images/113613607051_DV_resource.Stream@PNG-de-DE.png) | Select context | For context-based filtering of alarms.  The alarm control only shows alarms that fall within the time period of the selected context entry. |

#### Operate alarm control (RT Unified)

> **Note**
>
> **Displayed alarms**
>
> The alarms that you see in the alarm control depend on which alarm view or alarm list you have selected in the toolbar.

##### Operation using the mouse

**Selecting and operating alarms**

- Click on an alarm.
- Click a button in the toolbar.

The function of the button is applied to the alarm.

**Rearranging columns**

You can change the column arrangement configured in the engineering here. See section [Rearranging columns at runtime](#rearranging-columns-at-runtime-rt-unified).

**Sorting alarms by column**

You can sort the alarms by column. See section [Sorting alarms](#sorting-alarms-rt-unified).

##### Operation using the keyboard

Press <Shift + Enter> until the focus is on the alarm control. Then select the alarm to be edited and operate it using the toolbar.

Use the following buttons for this:

| Buttons | Description |
| --- | --- |
| <PgUp> | Selects the previous alarm. |
| <PgDn> | Selects the next alarm. |
| <Ctrl + Up>  or   <Home> | If multiple rows were selected, the first row of the selection is selected. |
| <Ctrl + Down>  or   <End> | If multiple rows were selected, the last row of the selection is selected. |
| <Ctrl + Left> | If multiple columns were selected, the first column of the selection is selected. |
| <Ctrl + Right> | If multiple columns were selected, the last column of the selection is selected. |
| <Tab> | Selects the next button in the toolbar. |
| <Shift + Tab> | Selects the previous button in the toolbar. |
| <Enter> | Executes the currently selected button. |
| <Shift + Page Up> | Scrolls to the left column-by-column. |
| <Shift + Page Down> | Scrolls to the right column-by-column. |

##### Alternative operation

- Depending on the configuration, you can also operate the alarm control via the function keys.
- If the alarm control is configured accordingly, all information about the alarm is displayed in a pop-up for a selected alarm. The "Alarms - Show recent" button (Autoscroll) must be disabled for this.

##### Multiple selection of alarms on Panels via touch gesture

**Requirement**

Configuration of the alarm control in the engineering system:

- Under "Properties > Miscellaneous > Alarm control > Selection - Mode", the "Multiple" entry is set for "Static value".
- The "Previous line" and "Next line" buttons are configured.

**Operator control in Runtime**

1. Tap an alarm in the alarm control.

   The alarm is selected.
2. To extend the selection by one or more previous alarms, tap the "Previous line" button until the desired alarms are selected.
3. To extend the selection by one or more subsequent alarms, tap the "Next line" button until the desired alarms are selected.

---

**See also**

[Supported gestures (RT Unified)](#supported-gestures-rt-unified)

#### Filtering alarms (RT Unified)

##### Introduction

You can use filters to control which alarms you see in the alarm view in runtime. To do so, define filter conditions.

The following settings are available in the "Alarm filter" dialog:

| Setting | Description |
| --- | --- |
| "AND/OR" column | Adds additional criteria to the existing criteria with the Boolean operations AND or OR. |
| "Criterion" column | Selection list with the available criteria.  Criteria correspond to the alarm blocks in the alarm control. |
| "Operator" column | Selection list with the available relational operators. |
| "Setup" column | Free text field |
| "Remove" button | Removes the selected filter criterion. |
| "Up/down" button | Moves the selected filter criterion. |
| "Filter" area | Free text area for direct input and editing of filter criteria. |

##### Requirement

The "Selection display" button is configured in the alarm control.

##### Procedure

The following example describes how to define a filter. In the example, a filter is defined that filters for alarms that contain the alarm text "Motor on" and have a priority less than or equal to 5:

1. Click the "Selection display" button.

   ![Procedure](images/111759508747_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/111759508747_DV_resource.Stream@PNG-de-DE.png)

   The "Alarm filter" dialog opens.
2. Click in the "Criterion" column and select the "Alarm text" entry.
3. Click in the "Operator" column and select the "Equal to" entry.
4. In the free text field of the "Setup" column, enter the value "Motor on".
5. In the next row in the "And / Or" column, click "Add" and select the AND logic operation.
6. Click in the "Criterion" column and select the "Priority" entry.
7. Click in the "Operator" column and select the entry "Less than or equal to".
8. Enter the value "5" in the free text field of the "Setting" column.
9. Confirm your entries.
10. Close the dialog.

With some alarm blocks, for example, you can define the start and end times or search texts for "Date" and "Time". Your input must be in the format required in the dialog.

> **Note**
>
> In multi-user systems, make sure that contents displayed in the "Alarm filter" dialog on a client have the same names on all servers.
>
> When filtering by time, the start and stop values are not adjusted automatically when the time base of the alarm control is changed.
>
> Example: At the PC location with the time zone "UTC + 1h", the alarm control has the "Local time zone" time base. You should filter by the time 10:00 to 11:00. Change the time base from "Local time zone" to "UTC". If you want to display the same alarms, change the filter to 9:00 to 10:00 hrs.

##### Result

The filter is applied to all alarm lists in the alarm view.

##### Time-based filtering

**Define the filter period**

During time-based filtering of the alarm control, always define two filter conditions linked via "And". For these conditions, use the operators "Greater than", "Greater than or equal to" and "Less than or equal to".

Do not use the "Equal to" operator. When filtering, you specify the filter period down to the millisecond. Internally, the time stamp of alarms is stored precisely down to the nanosecond and the missing information for nanoseconds is supplemented by 0. A search with "Equal to" will therefore only find alarms whose time stamp has the nanosecond value 0.

Examples:

You can use the following filter conditions to filter for alarms that were triggered between 12:00 and 12:01:

- Filter condition 1: "Raise time", "Greater than or equal to", 12:00:00.000
- Filter condition 2: "And", "Raise time", "Less than or equal to", 12:01:00.001

You can use the following filter conditions to filter for alarms that were triggered at 12:00:00.000 hrs:

- Filter condition 1: "Raise time", "Greater than or equal to", 12:00:00.000
- Filter condition 2: "And", "Raise time", "Less than or equal to", 12:00:00.000

**Change time base**

If the time base of the alarm control is changed, the start value and stop value are not automatically adjusted when you filter by time.  
Example: At the location of the PC with the time zone "UTC + 1h", the time base "Local time zone" was selected for the alarm control. If you filter for the time 10:00 to 11:00 and then change the time base to "UTC", you need to change the start value and stop value of the filter to 9:00 and 10:00 to display the same alarms as before.

---

**See also**

[Display alarms for plant objects (RT Unified)](#display-alarms-for-plant-objects-rt-unified)

#### Display alarms for plant objects (RT Unified)

##### Introduction

In the case of the corresponding configuration, the alarm control shows the alarms of the plant objects that are configured in the plant hierarchy:

- Automatic display

  When the HMI device is assigned to a plant hierarchy or a plant object, and a plant overview and an alarm control are configured for the screen, the alarm control automatically shows the alarms of the plant object selected in the plant overview.
- Manual display through filters

  If no plant overview is configured in the screen, filter the alarm control to display alarms of a plant object.

The alarm control offers the following options for plant object alarms:

- Display the hierarchy path of the alarm source
- Filter the alarm control by plant objects
- Display alarm log of a plant object
- Context-dependent display of plant object alarms

##### General requirements

- The plant hierarchy has been created and a device assigned in the engineering system.
- An alarm control with the column "Area" has been configured in the screen of the assigned device.
- Runtime is active.

##### Filter alarm control by plant objects

**Additional requirements**

- Alarms are available for a plant object from the plant hierarchy.

**Procedure**

1. In Runtime, click the "Selection display" button in the alarm control.
2. Select "Area" as the criterion in the "Alarm filter" dialog.
3. Click the cell of the "Setting" column
4. Click "...".

   A tree of the plant hierarchy is displayed.
5. Select a plant object and confirm your selection.

   ![Filter alarm control by plant objects](images/118535864075_DV_resource.Stream@PNG-en-US.png)

   ![Filter alarm control by plant objects](images/118535864075_DV_resource.Stream@PNG-en-US.png)
6. Under "Operand", select one of the following operators:

   - To display the alarms of the selected plant object, select "Same as".
   - To output the alarms of the lower-level plant objects, select "Begins with".

The alarm control shows its setting according to the alarms of the selected plant object or its lower-level plant objects. The "Area" column shows the complete path of the plant object.

> **Note**
>
> **Display of the filter string for filters configured in engineering**
>
> The plant view is based on a type/instance architecture. When a filter has been configured in engineering that filters the alarm view by plant objects, you will first see a filter string with information from the type level in the "Filter" field of the "Alarm filter" dialog.
>
> If you select an operand under "Operand" or a plant object under "Setting", the filter string changes to the instance level and adopts the device ID.

##### Display alarm log for a plant object

**Additional requirements**

- The alarm log contains entries for a plant object from the plant hierarchy.

**Procedure**

1. In runtime, click on the "Display logged alarms" button.

The alarm control shows the logged alarms of the plant object.

---

**See also**

[Filtering alarms (RT Unified)](#filtering-alarms-rt-unified)
  
[Plant overview (RT Unified)](#plant-overview-rt-unified)

#### Display context-dependent alarms of a plant object (RT Unified)

This section describes how to show alarms that occurred on a plant object that you selected for a context that you selected.

##### Requirement

- An HMI device has been configured.
- An alarm control is configured in the device screen.
- The plant hierarchy has been created and assigned to the HMI device.
- There are alarms for the plant object.
- Contexts and context entries are available for the plant object.
- The "Select context" button is configured in the alarm control.

##### Procedure

1. In the alarm control, click the "Select context" button.

   The "Alarm context" dialog opens.
2. Click "..." and select the plant object whose data you want to display in the alarm control.
3. Select one of the contexts assigned to the plant object in the "Context" drop-down list.

   A list of the entries logged for the context appears under "Logged context values".
4. Select an entry.
5. Click "OK".

The alarm control shows the alarms of the plant object that fall within the time period of the selected entry. The information bar shows the values of the selected context.

> **Note**
>
> **"AND" link with other filters**
>
> When a filter is defined for the alarm control, the filter condition and the context conditions are linked via "AND".
>
> When no alarms appear in the alarm control, check your filter settings by clicking "Selection display".

---

**See also**

[Contexts (RT Unified)](#contexts-rt-unified)

#### Sorting alarms (RT Unified)

##### Introduction

You can control the columns according to which the alarm control sorts the alarms in runtime.

Examples for sorting alarms:

- In descending order by date, time, and alarm number. The latest alarm appears at the top.
- By priority

  You must have defined the priority of the alarms in the "HMI alarms" editor and configured the "Priority" alarm block in the alarm control. As a result, in a single-line alarm control, only the top-priority alarm appears in the alarm window. A lower-priority alarm is not displayed, even if it is more recent. The alarms are displayed in chronological order.
- The "Alarm state" alarm block is sorted by the type of state and not by the configured status texts. For an ascending sort order, the following order is used:

  - Active
  - Inactive
  - Acknowledged
  - Disabled
  - Activated
  - Automatic acknowledgment
  - Emergency acknowledgment
  - Active/Inactive

When sorting the alarm control by columns, define the sort order over up to four columns. An arrow and a number are shown on the right in the column header. The arrow indicates the sort order (ascending or descending). The number beside the arrow indicates the sort order of the column headers.

##### Requirement

- "Allow sorting" is enabled for the respective columns in the configuration of the alarm control.
- The "Show recent" function is paused in the alarm control.

##### Procedure

To filter alarms in the alarm control by column, follow these steps:

1. Click the column header by which you want to sort the alarms first.

   The number "1" is displayed with an arrow pointing upwards for ascending sort order or an arrow pointing downwards for descending sort order.
2. Optional:

   - To reverse the sort order for this column, click the column header again.
   - To cancel the sorting for this column, click the column header a third time.
3. If you want to sort by several columns, click the column header in the required order.

Alternatively, click the "Sorting setup" button and configure the sorting in the "Sorting" dialog.

#### Disabling individual alarms (RT Unified)

> **Note**
>
> **No locking and unlocking of PLC alarms**
>
> Locking and unlocking of PLC alarms for an S7-1500 PLC is not supported.

##### Introduction

If you disable an alarm, the alarm is not checked to determine whether the alarm condition applies. The alarm is not logged.

> **Note**
>
> **Disabled alarm**
>
> Disabled alarms are no longer disabled after a restart of Runtime. Only alarms that are disabled directly in the automation system via data blocks remain disabled (disabled at source).

##### Requirement

- The "Visibility" and "Allow operator control" settings have been enabled for the following buttons in the engineering:

  - "Disable alarm"
  - "Enable alarm"
- The user is authorized to disable and enable alarms.

  > **Note**
  >
  > The "Disable alarms" and "Enable alarms" authorizations must be configured directly one below the other. This is necessary because the authorization level used automatically for the "Enable alarms" authorization is directly below the "Disable alarms" authorization.
- An alarm is displayed on the HMI device.

##### Disable alarm

1. Select one of the following alarm lists in the alarm control:

   - "Show logged alarms"
   - "Show and update logged alarms"
   - "Show defined alarms"
2. Select the alarm.
3. Click "Disable alarm".

##### Result

The alarm is removed from the "Show active alarms" alarm list. Its alarm condition is no longer checked.

The alarm is visible in the alarm lists for logged alarms and defined alarms and has the status "Removed".

##### Enable alarm

To enable a disabled alarm, follow these steps:

1. In the alarm control, select an alarm list for logged alarms or defined alarms.
2. Select the alarm in the alarm list.
3. Click "Enable alarm".

The alarm condition of the alarm is checked again.

#### Shelving alarms (RT Unified)

##### Introduction

You shelve an alarm for a specific period of time, for example, to prevent that a conformity error alarm affects the efficiency of your system.

Shelving can be canceled at any time. To do so, you use the buttons "Shelve alarm" and "Unshelve alarm" in the alarm control in runtime.

##### Requirement

- The "Visibility" and "Allow operation" settings have been activated for the following buttons in the engineering system:

  - "Shelve alarm"
  - "Unshelve alarm"
  - "Show active alarms"
  - "Display options setup"
- To unshelve: An alarm is displayed on the HMI device.

##### Procedure

To shelve an alarm, follow these steps:

1. Select one of the following alarm lists in the alarm control:

   - "Show active alarms"
   - "Show logged alarms"
   - "Update and display logged alarms"
   - "Show defined alarms"
2. Select the alarm.
3. Click the "Shelve alarm" button.

##### Result

The alarm is shelved. Its status remains unchanged.

The shelving creates a log entry. Shelved alarms are still available and logged in the system.

> **Note**
>
> **Display of shelved alarms in the alarm list "Show active alarms"**
>
> Whether shelved alarms are visible in the alarm list for active alarms depends on the settings in the alarm list.
>
> By default, the alarm list for active alarms does not display any shelved alarms.

##### Display shelved alarms

To display the currently shelved alarms, follow these steps:

1. In the alarm control, select the "Show active alarms" alarm list.
2. Click the "Display options setup" button.
3. Activate the option for shelved alarms.

##### Unshelve an alarm

To unshelve an alarm, follow these steps:

1. Display the shelved alarms.
2. Select the alarm in the "Show active alarms" alarm list.
3. Click the "Unshelve alarm" button.
4. If required, hide the shelved alarms from the "Show active alarms" alarm list.

Unshelving is canceled. Canceling the unshelving creates a log entry.

#### Acknowledging (RT Unified)

This section contains information on the following topics:

- [Acknowledging alarms (RT Unified)](#acknowledging-alarms-rt-unified)

##### Acknowledging alarms (RT Unified)

The number of alarms to be acknowledged is indicated by a counter at the "Single acknowledgment" button or, if the alarm control was configured accordingly in engineering, by the information bar.

###### Introduction

You can acknowledge alarms in runtime according to your project configuration settings. You acknowledge alarms as follows:

- In the alarm control with the buttons "Single acknowledgment" and "Acknowledge visible alarms", and for alarms with dual-mode acknowledgment also with the button "Single confirm".
- With customized buttons

When an operator authorization is configured for the buttons, the alarms can only be acknowledged by authorized users.

###### Acknowledgment variants

You acknowledge individual alarms or multiple alarms together in Runtime. The following options are possible:

- Single acknowledgment

  Acknowledgment of an alarm using the "Single acknowledgment" button of the alarm control.
- Group acknowledgment

  Acknowledgment of all pending, visible alarms that require acknowledgment in the alarm control using the "Acknowledge visible alarms" button in the alarm control.
- Dual-mode acknowledgment

  When an alarm requires dual-mode acknowledgment, you must acknowledge both the enabling and disabling of the alarm. Or you acknowledge the alarm and reset it with the "Single confirm" button in the alarm control. The alarm status changes from "Active/Acknowledged" to "Inactive".

###### Requirement

- The "Visibility" and "Allow operator control" settings have been enabled in the engineering for the following buttons of the alarm control:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/132458249611_DV_resource.Stream@PNG-de-DE.png) | Single acknowledgment |
  | ![Requirement](images/132458359435_DV_resource.Stream@PNG-de-DE.png) | Acknowledge visible alarms |
  | ![Requirement](images/132458428939_DV_resource.Stream@PNG-de-DE.png) | Single confirm |
  | ![Requirement](images/132458366859_DV_resource.Stream@PNG-de-DE.png) | Show recent |
- For the single acknowledgment: An alarm that requires acknowledgment is pending.
- For the group acknowledgment: Several alarms that require acknowledgment are pending. The alarms do not require single acknowledgment.

###### Acknowledge alarms individually

To acknowledge an alarm, follow these steps:

- Read the alarm texts of the pending alarm and perform corrective measures, if necessary.
- Pause "Show recent".
- Select the alarm.
- Click "Single acknowledgment" in the alarm control.

###### Result

The alarm status is set to "Acknowledged". When the trigger condition for an alarm no longer applies, the alarm status is set to "Inactive" and no longer displayed on the HMI device.

###### Acknowledging alarms collectively

For group acknowledgment of alarms, follow these steps:

1. Read the alarm texts of the pending alarms and perform corrective actions, if necessary.
2. In the alarm control, click "Acknowledge visible alarms".

> **Note**
>
> The "Acknowledge visible alarms" button acknowledges all visible alarms only if no alarm is selected or highlighted.
>
> If an alarm is selected or highlighted, only the selected or highlighted alarm will be acknowledged after clicking the "Acknowledge visible alarms" button.

###### Result

All pending alarms with the following properties are acknowledged:

- Requires acknowledgment
- Does not require single acknowledgment
- Visible

When the trigger condition for an alarm no longer applies, the alarm status is set to "Inactive" and no longer displayed on the HMI device.

#### Logging alarms (RT Unified)

This section contains information on the following topics:

- [Logging basics (RT Unified)](#logging-basics-rt-unified)
- [Connecting and disconnecting the alarm log backup (RT Unified)](#connecting-and-disconnecting-the-alarm-log-backup-rt-unified)
- [Display logged alarms (RT Unified)](#display-logged-alarms-rt-unified)

##### Logging basics (RT Unified)

###### Introduction

An alarm log documents the alarms that occurred in the monitored process. You can use alarm logging to analyze error states and to document the process. When you analyze the logged alarms, you can extract important business and technical information regarding the operating mode of the plant.

With the appropriate configuration in engineering, logging alarms are created in runtime. If an error or limit violation occurs, for example, an alarm is output in runtime.

​The alarm events are saved in a log database and/or printed out. The alarms logged in the database can be output in runtime if required, for example, in an alarm control.

​The logged alarms are stored in a circular log that consists of multiple single segments.

With the appropriate configuration of the HMI device and a PLC connected to it, the alarms of the connected PLC are logged as well and made available in all configured languages.

###### Operating principle

An alarm is only logged if logging has been configured for its alarm class. The alarm logs are automatically created by the system in runtime.

Each alarm event of an alarm that has occurred is logged, for example, the status change from "Active" to "Active, acknowledged".

> **Note**
>
> **Alarm classes for pure logging**
>
> Alarms of the alarm classes "Information", "OperatorInputInformation" and "SystemInformation" are only used for logging. In runtime, they are only displayed in the alarm lists "Show logged alarms" and "Show and update logged alarms".

###### Content of the alarm log

The alarm logs are used to store all alarm data, including configuration data. You can read all properties of an alarm from the logs, for example, alarm class, time stamp and alarm texts.

A new log segment with the new configuration data is generated whenever you edit configuration data of an alarm. This function prevents any change from influencing alarms logged previously.

The possible number of logged alarms depends on the database used.

> **Note**
>
> The time stamp of a logged alarm is always specified in standard UTC format (Universal Time Coordinated).

Because the alarm configuration is language-specific, the logs contain a configuration data table for each language configured.

###### Storage location and storage media

Log data are stored in a database. You can further process the saved data in other programs for analysis purposes, for example.

###### Backup for log segments

Take backups of your log segments to ensure complete documentation of your process.

> **Note**
>
> **Database types for backups**
>
> - Microsoft SQL
>
>   Must support the "Microsoft ODBC Driver 17 for SQL Server" driver in Version 17.9.
> - SQLite
>
>   Must support the "SQLite3" driver.

> **Note**
>
> Segments from logs for which a backup was created can be restored in runtime. To do so, open SIMATIC Runtime Manager on the HMI device. See also section [Restoring and deleting log segments](SIMATIC%20Runtime%20Manager%20%28RT%20Unified%29.md#restoring-and-deleting-log-segments-rt-unified).

###### Display of logged data

You can view the logged data on the HMI device with the buttons "Show logged alarms" and "Show and update logged alarms".

###### No logging due to overload

When an alarm cannot be written to the log after the configured number of attempts and within the defined time interval, the alarm is lost. The memory state is set to "StorageSystemWriteDataLost" internally. This documents that the number of alarms in the queue exceeds the configured high limit. No more alarms can be written to the log.

The alarm "SystemOverloadAlarm" of the alarm class "ALCL@%SystemInformation" is triggered. It is displayed in the alarm control but not logged.

Possible reasons for the overload:

- There are more alarms in the queue than can be processed.
- The alarms in the queue cannot be processed due to additional error conditions or memory states, for example, because the storage space is used up (memory state "StorageSpaceExceeded").

---

**See also**

[Alarm classes](#alarm-classes)

##### Connecting and disconnecting the alarm log backup (RT Unified)

###### Introduction

When you want to access the data of an archived alarm log, connect the log backup to the project. You can configure an automatic connection or connect the alarm log to the project via a script. The logged alarms are displayed in the alarm control.

If you no longer want to access the backup of a log segment, disconnect the log backup from the project.

###### Requirement

The relevant backup files in "*. ldf" and "*.mdf" format are stored locally.

###### Display Time Range

Alarms are only displayed if you have configured the time range in the alarm control accordingly.

###### Example

You have configured the time range so that only the alarms of the past 24 hours are displayed. When you connect to a log backup containing alarms that are older than 24 hours, these alarms are not included in the alarm control.

###### Automatically connecting to an alarm log

To automatically connect to the alarm log backup, follow these steps:

1. Insert the log backup files in the "RuntimeProjectPath\ProjectName\CommonArchiving" folder.
2. In runtime, the alarm log is automatically connected to the project.

If signing is enabled, signed log backup files that are changed will not be connected automatically. A WinCC system alarm is generated and an entry is added to the Windows event log in the "Application" section.

###### Connecting to the alarm log using a script

Using the "AlarmLogs" VBS object, you can link the log backup files to the project using a script. The log segments are then copied with the "Restore" VBS method to the "Common Archiving" folder of the Runtime project.

###### Automatically disconnecting the alarm log

To automatically disconnect the alarm log backup from the project, follow these steps:

1. Go to the folder "RuntimeProjectPath\ProjectName\CommonArchiving".
2. Remove the log backup files from the folder.

###### Disconnecting from the alarm log using a script

Using the "AlarmLogs" VBS object, you can disconnect the log backup files from the project using a script. The log segments are then removed with the "Remove" VBS method from the "Common Archiving" folder of the Runtime project. For additional information, see the description of the "AlarmLogs" VBS object and the "Remove" VBS method.

##### Display logged alarms (RT Unified)

###### Introduction

You can display the logged alarms with the buttons "Show logged alarms" and "Show and update logged alarms".

###### Requirements

- An alarm log is configured.
- All logged data that is to be displayed must be stored locally on the logging server. The SQL server does not allow access to backup files held elsewhere, such as another computer on the network.
- The buttons "Show logged alarms" and "Show and update logged alarms" are configured in the alarm control.

###### Procedure

1. To display only logged alarms, click the "Show logged alarms" button in the alarm control:

   ![Procedure](images/105743986699_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/105743986699_DV_resource.Stream@PNG-de-DE.png)

   The alarm control shows the logged alarms. The display is not updated immediately when new incoming alarms occur.

   Each page shows a maximum of 1000 alarms. Use the "Previous page" and "Next page" buttons to change pages.
2. Click the "Show and update logged alarms" button in the alarm control to display logged and current alarms:

   ![Procedure](images/105743986699_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/105743986699_DV_resource.Stream@PNG-de-DE.png)

   The alarm control shows the logged alarms. The display is updated immediately when new active alarms occur.

   The alarm control shows a maximum of 100 alarms.

###### Restriction for the alarm list "Show logged alarms"

For log alarms with identical time stamp, it is possible in rare cases that log alarms are skipped when paging forwards and backwards.

To display the skipped alarms, page again, this time in the opposite direction.

> **Note**
>
> In the case of more than 1000 log alarms with identical time stamp, not all skipped alarms can be displayed by scrolling in the opposite direction.

**Example**

- The alarm log contains several 1000 log alarms. Ten alarms of the log have an identical time stamp. The first five are shown at the end of the current page.

  The alarm control is sorted by time stamp in ascending order.
- Click "Next page".

  You see the next 1000 alarms whose time stamp is higher than the time stamp of the last alarm shown on the previous page.

  The remaining five alarms with identical time stamp are skipped on the page change.
- Click "Previous page".

  You will see all ten alarms with identical time stamp as well as the next 990 alarms with lower time stamp.

#### Displaying alarm statistics (RT Unified)

##### Introduction

The alarm statistics represent statistical calculations of logged alarms.

![Introduction](images/139494878987_DV_resource.Stream@PNG-en-US.png)

You can use a button in the alarm control to export the alarm statistics to an Excel file.

> **Note**
>
> **Filter**
>
> A filter set in the alarm control is not effective in the alarm statistics.

> **Note**
>
> **Display options**
>
> Selected display options via the "Display options - setup" button in the alarm control have no effect in the alarm statistics.

##### Requirement

- Alarms are logged.
- For the following button of the alarm control, the "Visibility" and "Allow operator control" are enabled in the engineering system:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/139055173387_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics - view |

##### Procedure

To display the alarm statistics in Runtime, proceed as follows:

1. Click the "Alarm statistics - view" button in the alarm control.

##### Result

The alarms to be displayed in the alarm statistics are specified in the engineering system. Depending on the engineering system, the following columns are displayed:

| Column | Description |
| --- | --- |
| Number | Configured number of the alarm. |
| Frequency | Frequency of an alarm. The system counts the number of occurrences of an alarm with "active" status in the log. If the alarm number is not found, this alarm number is not included in the statistics. |
| Sum active active | Total display time of an alarm in seconds. The time period between the alarm states "active" and "active" is calculated. |
| Sum active inactive | Total display time of an alarm in seconds. The time period between the alarm states "active" and "inactive" is calculated. |
| Sum active acknowledged | Total display time of an alarm in seconds. The time period between the alarm states "active" and "acknowledged" is calculated. |
| Average active active | Average display time of an alarm in seconds. The time period between the alarm states "active" and "active" is calculated. |
| Average active inactive | Average display time of an alarm in seconds. The time period between the alarm states "active" and "inactive" is calculated. |
| Average active acknowledged | Average display time of an alarm in seconds. The time period between the alarm states "active" and "acknowledged" is calculated. |

The calculation of the time of acknowledgment includes the "acknowledged" alarm state. This "acknowledged" alarm state includes the acknowledgment by the controller.

> **Note**
>
> For the calculation, alarms with the status "acknowledged" and "inactive" are only used if a suitable alarm with the status "active" is found in the result set beforehand.
>
> If an alarm from the controller is pending and runtime is disabled and enabled several times, the alarm is entered into the log several times with the state "active". The alarm is also included multiple times in the calculation.

#### Operating alarm statistics (RT Unified)

##### Introduction

Using the alarm statistics setup, you can change the settings for calculating the alarm statistics. The following settings are available:

| Setting | Description |
| --- | --- |
| Time range start | - Now   The current time is displayed as the start time of the calculation. - Fixed   The start time of the calculation can be changed as required. |
| Start time | Start time for the calculation. If the "Now" option is selected under "Time range start", the start time cannot be changed. |
| Time range base | Unit of time for the calculation. The following settings are available:  - Undefined   The default time unit "Minute" is used with this setting. - Millisecond - Second - Minute - Hour - Day - Month - Year |
| Time range factor | The time range factor depends on the "Time range base" setting. For example, if the number 4 is set for the time range factor and "Minutes" is set for the time range base, all alarms that are logged within this period will be evaluated. |

##### Requirement

- Alarms are located in the alarm log.
- For the following button of the alarm control, the "Visibility" and "Allow operator control" are enabled in the engineering:

  | Symbol | Meaning |
  | --- | --- |
  | ![Requirement](images/140319034891_DV_resource.Stream@PNG-de-DE.png) | Alarm statistics - setup |
- The alarm statistics are selected in the alarm control.

##### Procedure

To display the alarm statistics setup in runtime, follow these steps:

1. Click on the "Alarm statistics - setup" button in the alarm control.

   The configuration opens.
2. Change the settings as required.
3. Click the "OK" button.

##### Result

The calculation of the alarm statistics is displayed according to the changed settings.

### Displaying tags in Runtime (RT Unified)

This section contains information on the following topics:

- [Outputting the tag values (RT Unified)](#outputting-the-tag-values-rt-unified)
- [Operating controls (RT Unified)](#operating-controls-rt-unified)
- [Trend companion (RT Unified)](#trend-companion-rt-unified)
- [Trend control (RT Unified)](#trend-control-rt-unified)
- [Process control (RT Unified)](#process-control-rt-unified)

#### Outputting the tag values (RT Unified)

##### Overview

With WinCC you can output tag values in the HMI screen with different screen objects and change them.

- The I/O field is used for the input and output of process values.
- Bars are used for graphic display of the process values in form of a scale.
- Sliders are used for the input and output of process values within a defined range.
- The gauge is used to display the process values in form of an analog gauge.

In runtime you can also output tag values as table or as trend. You can use either process values or logged values as source for the tag values.

- Use a trend for the graphic display of tag values. Trends allows you to display the change in motor temperature, for example.
- Use a table to compare tag values. In the table you can, for example, compare fill levels of supply tanks.

##### Controls for displaying tag values

To display tag values as a trend, use the trend control. The versions of trend views are available:

- "Trend control": You display a tag value over time, for example, the change in temperature. You can compare the current values and logged values or monitor the change in current values on the HMI device.
- "Function trend control": You display a tag value against a second tag value, for example, the engine speed against the heat produced.

You can use the "Trend companion" to create statistics, for example, from the displayed values. Furthermore, you can use the trend companion as reading assistance for the trend control.

To display tag values in a table, use the process control.

![Controls for displaying tag values](images/104046995723_DV_resource.Stream@PNG-de-DE.png)

##### Displayed values

When configuring the trend control, specify which tag values are to be displayed.

- "Online": The trend is continued with current individual values from the PLC.
- "Log": In runtime, the trend control displays the values of a tag from a data log. The trend shows the logged values in a particular window in time. The operator can move the time window in runtime to view the desired information from the log.

#### Operating controls (RT Unified)

This section contains information on the following topics:

- [Starting and Stopping Update (RT Unified)](#starting-and-stopping-update-rt-unified)
- [Creating statistics for Runtime data (RT Unified)](#creating-statistics-for-runtime-data-rt-unified)
- [Displaying logged values (RT Unified)](#displaying-logged-values-rt-unified)
- [Elements of the information line (RT Unified)](#elements-of-the-information-line-rt-unified)
- [Basics of time range (RT Unified)](#basics-of-time-range-rt-unified)
- [Exporting values (RT Unified)](#exporting-values-rt-unified)

##### Starting and Stopping Update (RT Unified)

###### Introduction

You can continue the update of the data contained in the control with the "Start/Stop" buttons.

Some buttons stop the update automatically, e.g. "Define statistics area"

The appearance of the button indicates whether the update is stopped or not:

| Symbol | Meaning |
| --- | --- |
| ![Introduction](images/106392289803_DV_resource.Stream@PNG-de-DE.png) | The update has been stopped. To continue the update, click on the button. |
| ![Introduction](images/106392289803_DV_resource.Stream@PNG-de-DE.png) | The update has been started. To stop the update, click on the button |

##### Creating statistics for Runtime data (RT Unified)

###### Introduction

You can generate an analysis of the process data for the Runtime data in the trend or process control. You can display the evaluated data in the trend companion.

###### Overview

Use the following buttons to create statistics of runtime data:

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/105773331339_DV_resource.Stream@PNG-de-DE.png) | "Start/stop" |
| ![Overview](images/105772702091_DV_resource.Stream@PNG-de-DE.png) | "Select time range" |
| ![Overview](images/111942694667_DV_resource.Stream@PNG-de-DE.png) | "Statistics area" |

###### Requirement

- A trend control or process control is configured.
- A trend companion is configured and connected to the trend or process control.
- Runtime is enabled.

###### Displaying data in a statistics area window

**Requirement:**

The "Statistics area window" display mode is enabled in the trend companion.

To display data in the statistics area window of the trend companion, proceed as follows:

1. In the trend control or process control, click "Stop".

   The updated display is stopped, the process data continues being logged.
2. If you wish to evaluate data outside the displayed time range:

   - Click "Select time range".

     The "Time - Selection" dialog opens.
   - Enter the required time range.

     The data for the defined time range is displayed.
3. If you are using a trend control:

   - Click on the "Statistics area".

     In the trend control, two vertical lines are displayed on the right and left margin.
   - To define the statistics area, move the two lines to the desired position.
4. If you are using a process control:

   - Use the mouse to select the rows for the desired time range in the table.

     For different time columns with different time frames, you can select different time ranges for the calculation of statistics.
   - Click on "Statistic area" in the toolbar.

The evaluated data is displayed in the columns that you have configured in the statistics area window.

To continue with the display of Runtime data, click "Start".

> **Note**
>
> For additional statistical analysis of process data and logging of results, you can write the scripts yourself.

##### Displaying logged values (RT Unified)

###### Introduction

Scroll through the displayed data of a log using the buttons in the toolbar of a trend or process control. If key combinations are configured, you can also use these for scrolling.

The buttons for browsing in logs are available only if data is supplied through logging tags.

The logged values of a tag are displayed within a time range in the trend or process control.

###### Overview

Use the following buttons to display logged values:

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/111939775499_DV_resource.Stream@PNG-de-DE.png) | "First data record" |
| ![Overview](images/105772640907_DV_resource.Stream@PNG-de-DE.png) | "Previous data record" |
| ![Overview](images/105772648331_DV_resource.Stream@PNG-de-DE.png) | "Next data record" |
| ![Overview](images/105772655755_DV_resource.Stream@PNG-de-DE.png) | "Last record" |

###### Requirement

- Time range is configured.

###### Buttons for Archived Values

To scroll in archived values, proceed as follows:

1. To display the first data record of the time range, click on ![Buttons for Archived Values](images/106392381451_DV_resource.Stream@PNG-de-DE.png).
2. To display the previous data record of the time range, click on ![Buttons for Archived Values](images/106392410507_DV_resource.Stream@PNG-de-DE.png).
3. To display the next data record of the time range, click on ![Buttons for Archived Values](images/106392413963_DV_resource.Stream@PNG-de-DE.png).
4. To display the last data record of the time range, click on ![Buttons for Archived Values](images/106392417419_DV_resource.Stream@PNG-de-DE.png).

##### Elements of the information line (RT Unified)

###### Elements of the information bar

The information bar of the trend control or process control can contain the following elements:

| Icon | Name | Description |
| --- | --- | --- |
| ![Elements of the information bar](images/113612240779_DV_resource.Stream@PNG-de-DE.png) | Connection status<sup>1</sup> | No faulty data connections. |
| ![Elements of the information bar](images/113613266699_DV_resource.Stream@PNG-de-DE.png) | Faulty data connections exist. |  |
| ![Elements of the information bar](images/113612887947_DV_resource.Stream@PNG-de-DE.png) | All data connections are faulty. |  |
| "Line 1"<sup>2</sup> | Selected line | Shows the number of the selected line. |
| "Column 2"<sup>2</sup> | Selected column | Shows the number of the selected column. |
| "23.02.2010" | Date | Shows the system date. |
| "23:59:59" | Time | Shows the system time. |
| ![Elements of the information bar](images/102411719947_DV_resource.Stream@PNG-de-DE.png) | Time base | Shows the time base used in the display of times. |
| <sup>1</sup>: If you double-click on the "Connection status" icon, the "Status of the data connections" window opens. The following properties of each data connection are listed in the window:  - Name - Status - Tag name |  |  |
| <sup>2</sup>: Only in the process control |  |  |

##### Basics of time range (RT Unified)

The time range is the range from which the values at the HMI device are shown. The time range is determined by the start time and the end time. The time range is always in the past. If the end time is later than the current system time, the current system time is used as a temporary end time.

A distinction is made between the following time ranges:

- Static time range
- Dynamic time range

###### Static time range

The static time range is determined by fixed start and end times. The values are displayed within this time range.

###### Dynamic time range

The dynamic time range is determined by a period of time beginning with a fixed start time. The end time thus corresponds to the conclusion of the time period.

You set the time period as follows:

- Duration, e.g. 30 minutes
- The number of measurement points multiplied by the update cycle also produces a duration.

###### Configuring time range

Configure the time range for all controls. Configure the time range in the time column or in the time axis for the process control and the f(t) trend control. For the function trend control, configure the time range directly at the trend.

##### Exporting values (RT Unified)

###### Requirement

- The "Export" button is configured in the control.

###### Procedure

1. Optional: For the export of a trend control, check the time format for the time axis configured in the control.

   The time axis of the export file takes on the time format configured in the control.
2. Click "Export" in the control.
3. Enter the name of the target file.
4. For the trend companion and process control: Choose whether all values are exported or just the values selected in the control.
5. Optional: Using "Select format", determine which separator and which character set the target file uses.

   > **Note**
   >
   > **Displaying Asian languages correctly in MS Excel**
   >
   > If Runtime is running in an Asian language, select the character set "UTF-8".

#### Trend companion (RT Unified)

This section contains information on the following topics:

- [Trend companion basics (RT Unified)](#trend-companion-basics-rt-unified)
- [Overview of trend companion (RT Unified)](#overview-of-trend-companion-rt-unified)

##### Trend companion basics (RT Unified)

###### Function

The trend companion displays values or statistics from a control. The content of the trend companion is specified during its configuration.

###### Overview of the trend companion

The trend companion is connected to one of the following controls:

- Trend control
- Function trend control

In the trend companion, a "display mode" is specified during configuration. The display mode determines which data are shown in the trend companion.

###### Display mode

Three different display modes are available in the trend companion.

- Ruler window

  The ruler window shows the coordinate values of the trends on a ruler or values of a selected line in the table.
- Statistics area window

  The statistics area window shows the values of the low limit and high limit of the trends between two rulers or the selected area in the table. You can only connect the statistics area view to the trend control or the process control.
- Statistics window

  The statistics window displays the statistical evaluation of the trends. Among other things, the statistics include:

  - Minimum
  - Maximum
  - Average
  - Standard deviation
  - Integral

All windows can also display additional information on the connected trends or columns, such as time stamps.

##### Overview of trend companion (RT Unified)

With the "Trend companion", you display evaluated data and statistics of a control in a table.

![Figure](images/106546631435_DV_resource.Stream@PNG-en-US.png)

###### Buttons of the trend companion

The toolbar contains buttons for executing specific functions. Depending on the configuration, the following buttons are available for operator input:

| Icon | Name | Function |
| --- | --- | --- |
| ![Buttons of the trend companion](images/111898575499_DV_resource.Stream@PNG-de-DE.png) | Statistical analysis | Displays the statistical values from a defined "statistics range" of the trend or process controls in the statistics window of the trend companion.  Only available with a configured trend companion. |
| ![Buttons of the trend companion](images/111898571915_DV_resource.Stream@PNG-de-DE.png) | Statistics area | Specifies the period for calculation of statistics. |
| ![Buttons of the trend companion](images/105772663179_DV_resource.Stream@PNG-de-DE.png) | Ruler window | Displays a ruler that shows the coordinates of the intersection point with a trend in the trend companion.  Requirement: The trend companion is configured with "Ruler window" display mode. |
| ![Buttons of the trend companion](images/111934860811_DV_resource.Stream@PNG-de-DE.png) | Print | Reserved for future versions. |
| ![Buttons of the trend companion](images/105745968651_DV_resource.Stream@PNG-de-DE.png) | Export | Exports all or selected data to a *.CSV file.  Depending on the configuration and authorizations, the following options may be available:  - Display export settings and start export - Select file name and directory |

###### Rearranging columns

You can change the column arrangement configured in the engineering here. See section [Rearranging columns at runtime](#rearranging-columns-at-runtime-rt-unified).

#### Trend control (RT Unified)

This section contains information on the following topics:

- [Overview of trend control (RT Unified)](#overview-of-trend-control-rt-unified)
- [Overview of function trend control (RT Unified)](#overview-of-function-trend-control-rt-unified)
- [Value aggregation (RT Unified)](#value-aggregation-rt-unified)
- [Using the trend control (RT Unified)](#using-the-trend-control-rt-unified)

##### Overview of trend control (RT Unified)

With the trend control, you show the currently pending process values or logged values as a trend over time. You design the trend display according to your wishes.

![Figure](images/118552206219_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Trend display in future time range**
>
> The trend area located in the future continues the last drawn value.

###### Buttons of the trend controls

The toolbar contains buttons for executing specific functions. Depending on the configuration, the following buttons are available for operator input:

| Icon | Name | Function |
| --- | --- | --- |
| ![Buttons of the trend controls](images/111939775499_DV_resource.Stream@PNG-de-DE.png) | First record | Shows the trend direction starting with the first logged value.  Requirement: The values come from a process value log. |
| ![Buttons of the trend controls](images/105772640907_DV_resource.Stream@PNG-de-DE.png) | Previous record | Shows the trend direction of the previous time range. |
| ![Buttons of the trend controls](images/105773331339_DV_resource.Stream@PNG-de-DE.png) | Start/stop | Stops and starts the trend update.   Started: The trend is continuously updated. It always shows the latest values.  Stopped: New values are buffered and updated as soon as you start the trend update again. |
| ![Buttons of the trend controls](images/105772648331_DV_resource.Stream@PNG-de-DE.png) | Next record | Shows the trend direction of the next time range. |
| ![Buttons of the trend controls](images/105772655755_DV_resource.Stream@PNG-de-DE.png) | Last record | Shows the trend direction up to the last logged value.  Requirement: The values come from a process value log. |
| ![Buttons of the trend controls](images/111940616715_DV_resource.Stream@PNG-de-DE.png) | Previous trend | Displays the previous trend in the foreground. |
| ![Buttons of the trend controls](images/111940625291_DV_resource.Stream@PNG-de-DE.png) | Next trend | Displays the next trend in the foreground. |
| ![Buttons of the trend controls](images/105772663179_DV_resource.Stream@PNG-de-DE.png) | Ruler | Displays a movable ruler that shows the coordinates of the intersection point with a trend in the trend companion.  With stopped trend update, the trend values are also displayed in tooltips.  Requirement: The trend companion is configured with "Ruler window" display mode. |
| ![Buttons of the trend controls](images/105772677899_DV_resource.Stream@PNG-de-DE.png) | Zoom time axis +/- | Zooms into or out of the time axis in the trend control.  Left-click: Zoom in |
| ![Buttons of the trend controls](images/111940774923_DV_resource.Stream@PNG-de-DE.png) | Zoom value axis +/- | Zooms in or out of the value axis in the trend control. |
| ![Buttons of the trend controls](images/105772670603_DV_resource.Stream@PNG-de-DE.png) | Zoom area | Zooms in on the section of the trend control. You define the section by dragging with the mouse.  Use the "Original view" button to return to the original view. |
| ![Buttons of the trend controls](images/111941282955_DV_resource.Stream@PNG-de-DE.png) | Zoom +/- | Enlarges or reduces the view in the trend window. |
| ![Buttons of the trend controls](images/111941292043_DV_resource.Stream@PNG-de-DE.png) | Move trend area | Moves the display in the trend area. |
| ![Buttons of the trend controls](images/111942158219_DV_resource.Stream@PNG-de-DE.png) | Move axes area | Moves the display in the axes area. |
| ![Buttons of the trend controls](images/105772685195_DV_resource.Stream@PNG-de-DE.png) | Original view | Returns to the original view from the zoomed display. |
| ![Buttons of the trend controls](images/105772702091_DV_resource.Stream@PNG-de-DE.png) | Select time range | Opens a dialog in which you configure the time range. |
| ![Buttons of the trend controls](images/111942205707_DV_resource.Stream@PNG-de-DE.png) | Select trends | Opens a dialog in which you set the visibility and sorting of trends. |
| ![Buttons of the trend controls](images/105772694667_DV_resource.Stream@PNG-de-DE.png) | Select data connection | Opens a dialog in which you select the data source:  - Process value log - Tag - Recipe (only function trend control) |
| ![Buttons of the trend controls](images/111942694667_DV_resource.Stream@PNG-de-DE.png) | Statistics area | Enables you to define a time range for which statistical values are determined. Vertical lines which you use to set the time range are displayed in the trend window. |
| ![Buttons of the trend controls](images/111942657675_DV_resource.Stream@PNG-de-DE.png) | Statistical analysis | Opens a statistics window to display the minimum, maximum, average, and standard deviation for the selected time range and the selected trend. |
| ![Buttons of the trend controls](images/111942214283_DV_resource.Stream@PNG-de-DE.png) | Print | Starts printing the trends shown in the trend window. |
| ![Buttons of the trend controls](images/111942707339_DV_resource.Stream@PNG-de-DE.png) | Export | Opens the dialog for saving the trend data in CSV format.  The time axis in the export file takes on the time format configured in the control. If necessary, change the configuration of the time format in the control before the export. |
| ![Buttons of the trend controls](images/113613607051_DV_resource.Stream@PNG-de-DE.png) | Select context | Shows the value range of the resulting data for analysis purposes |

##### Overview of function trend control (RT Unified)

With the function trend control, you display active or logged process values as a function of another tag in a trend. You design the trend display according to your wishes.

![Figure](images/118552577291_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Trend display in future time range**
>
> The trend area located in the future continues the last drawn value.

###### Button of the function trend control

The toolbar contains buttons for executing specific functions. Depending on the configuration, the following buttons are available for operator input:

| Icon | Name | Function |
| --- | --- | --- |
| ![Button of the function trend control](images/100727802635_DV_resource.Stream@PNG-de-DE.png) | Start/Stop | Stops and starts the trend update.  Started: The trend is continuously updated. It always shows the latest values.  Stopped: New values are buffered and updated as soon as you start the trend update again. |
| ![Button of the function trend control](images/105772677899_DV_resource.Stream@PNG-de-DE.png) | Zoom X axis +/- | Zooms into or out of the time axis in the trend control.  Left-click: Zoom in  <Shift + Left-click>: Zoom out  Use the "Original view" button to return to the original view. |
| ![Button of the function trend control](images/105772670603_DV_resource.Stream@PNG-de-DE.png) | Zoom area | Zooms in on the section of the trend control. You define the section by dragging with the mouse.   Use the "Original view" button to return to the original view. |
| ![Button of the function trend control](images/105772677899_DV_resource.Stream@PNG-de-DE.png) | Zoom X axis plus minus | Zooms into or out of the time axis in the trend control.  Left-click: Zoom in  <Shift + Left-click>: Zoom out  Use the "Original view" button to return to the original view. |
| ![Button of the function trend control](images/105773338763_DV_resource.Stream@PNG-de-DE.png) | Zoom Y axis plus minus | Zooms in or out of the value axis in the trend control.  Left-click: Zoom in  <Shift + Left-click>: Zoom out  Use the "Original view" button to return to the original view. |
| ![Button of the function trend control](images/105772685195_DV_resource.Stream@PNG-de-DE.png) | Original view | Returns to the original view from the zoomed display. |
| ![Button of the function trend control](images/111976860427_DV_resource.Stream@PNG-de-DE.png) | Previous trend | Displays the previous trend in the foreground. |
| ![Button of the function trend control](images/111977701259_DV_resource.Stream@PNG-de-DE.png) | Next trend | Displays the next trend in the foreground. |
| ![Button of the function trend control](images/105772663179_DV_resource.Stream@PNG-de-DE.png) | Ruler | Displays a ruler that shows the coordinates of the intersection point with a trend in the trend companion.   Requirement: The trend companion is configured with "Ruler window" display mode. |
| ![Button of the function trend control](images/111941292043_DV_resource.Stream@PNG-de-DE.png) | Move trend area | You can move the trends in the trend window along the X axis and the Y axis using the button.  Values from the future trend area apply the last displayed value. |
| ![Button of the function trend control](images/111942158219_DV_resource.Stream@PNG-de-DE.png) | Move axes area | You can move the trends in the trend window along the value axis using the button. |
| ![Button of the function trend control](images/105772702091_DV_resource.Stream@PNG-de-DE.png) | Select time range | Opens a dialog in which you configure the time range. |
| ![Button of the function trend control](images/111942205707_DV_resource.Stream@PNG-de-DE.png) | Select trends | Opens a dialog for setting the visibility of trends. |
| ![Button of the function trend control](images/105772694667_DV_resource.Stream@PNG-de-DE.png) | Select data connection | Opens a dialog in which you select the data source:  - Process value log - Tag - Recipe |
| ![Button of the function trend control](images/111942214283_DV_resource.Stream@PNG-de-DE.png) | Print | Click this button to print the trend shown in the trend window. The print job used during printing is defined in the configuration dialog in the "General" tab. |
| ![Button of the function trend control](images/111942707339_DV_resource.Stream@PNG-de-DE.png) | Export data | This button is used for exporting all or the selected runtime data to a csv file. |

##### Value aggregation (RT Unified)

###### Introduction

If the number of process values or archive values to be displayed for the selected time range in a trend control is larger than the number of pixels available for the trend, they will be aggregated.

Which values are aggregated to a trend value depends on the loading time of the trend control. For this reason, screen changes can result in a change of the trend line.

###### Avoid aggregation

To avoid that values are aggregated, select a shorter time range or enlarge the width of the trend control.

###### Example

- Pixels available for the trend: 600
- Measuring interval of the tag set as the data source: 10 times per s
- Time range: 10 minutes,

i.e. in the selected time range, 6000 values are measured or logged. When drawing the trend, 10 values are aggregated to each trend value.

The trend displays different values depending on the loading time. The following graphics illustrate how the last two aggregated trend values change when the loading time is 11:00:0019 instead of 11:00:0024.

- Loading time 11:00:0019:

  ![Example](images/129886225163_DV_resource.Stream@PNG-en-US.png)
- Loading time 11:00:0024:

  ![Example](images/129886402187_DV_resource.Stream@PNG-en-US.png)

##### Using the trend control (RT Unified)

This section contains information on the following topics:

- [Online configuration of the trend control (RT Unified)](#online-configuration-of-the-trend-control-rt-unified)
- [Add new trend (RT Unified)](#add-new-trend-rt-unified)
- [Using the zoom functions in trend windows (RT Unified)](#using-the-zoom-functions-in-trend-windows-rt-unified)
- [Sorting trends (RT Unified)](#sorting-trends-rt-unified)
- [Hiding and showing trends (RT Unified)](#hiding-and-showing-trends-rt-unified)
- [Determining the coordinates of a point (RT Unified)](#determining-the-coordinates-of-a-point-rt-unified)
- [Select data connection of a trend (RT Unified)](#select-data-connection-of-a-trend-rt-unified)
- [Changing the time range of a trend (RT Unified)](#changing-the-time-range-of-a-trend-rt-unified)
- [Display context data of the plant objects in a trend control (RT Unified)](#display-context-data-of-the-plant-objects-in-a-trend-control-rt-unified)

###### Online configuration of the trend control (RT Unified)

###### Introduction

In Runtime, you configure online and thus change the appearance of the trend control.

During the configuration of the trend control, it is specified whether online configurations are retained or discarded during a screen change or after Runtime is ended.

###### Overview

Use the following buttons to configure the trend control in Runtime:

|  |  |  |
| --- | --- | --- |
| ![Overview](images/105772694667_DV_resource.Stream@PNG-de-DE.png) | "Select data connection" | Opens a dialog in which you can set the source from which a configured trend is supplied.  Possible sources are the tags or logging tags of an HMI device or plant object and UDTs. |
| ![Overview](images/111942205707_DV_resource.Stream@PNG-de-DE.png) | "Select trends" | Opens a dialog in which you set the visibility and sorting of trends. |
| ![Overview](images/105772702091_DV_resource.Stream@PNG-de-DE.png) | "Select time range" | Opens a dialog in which you configure the time range. |

In addition, you have the options to add additional trends using drag-and-drop operation.

---

**See also**

[Select data connection of a trend (RT Unified)](#select-data-connection-of-a-trend-rt-unified)
  
[Add new trend (RT Unified)](#add-new-trend-rt-unified)

###### Add new trend (RT Unified)

Adding new trends is not supported by the f(x) trend control.

###### Requirement

- A trend control and an IO field are configured in the process screen.
- The IO field has a link to a tag with numeric data type.

###### Procedure

Drag and drop the IO field onto the trend control.

For trend controls with multiple trend areas, drag the IO field to the desired trend area.

###### Result

If the tag in the trend area is not already used as the source of a trend, a new trend is added to the trend area and plotted. The trend represents the process values of the tags.

You can change the visibility of the trend via the "Select trends" button or via a script.

Changing the screen and refreshing the page removes the trend from the trend area.

###### Using the zoom functions in trend windows (RT Unified)

> **Note**
>
> **Scrolling in a zoomed in trend control**
>
> When the trend control is zoomed in, you can scroll using the mouse wheel:
>
> - Move the mouse wheel to scroll up or down.
> - Press <Shift> and move the mouse wheel to scroll to the left or right.

###### Introduction

Key functions can be used for zooming in on, zooming out of and returning to the original view for trends, axes and various zoom areas of the trend window.

###### Overview

The following zoom functions are available in the trend window:

|  |  |  |
| --- | --- | --- |
| ![Overview](images/105772677899_DV_resource.Stream@PNG-de-DE.png) | Zoom time axis +/- | Zooming in or out of time axis |
| ![Overview](images/111940774923_DV_resource.Stream@PNG-de-DE.png) | Zoom value axis +/- | Zooming in or out of value axis |
| ![Overview](images/105772670603_DV_resource.Stream@PNG-de-DE.png) | Zoom area | Zooming in on a trend control area |
| ![Overview](images/111941282955_DV_resource.Stream@PNG-de-DE.png) | Zoom +/- | Zooming in or out on trend |
| ![Overview](images/105772685195_DV_resource.Stream@PNG-de-DE.png) | Original view | Returning to the original view |

###### Requirement

- The trend control is open
- Buttons with zoom functions are configured
- Runtime is enabled

###### Zooming in on a trend control area

**Via the toolbar**

1. Click "Zoom area" in the toolbar.

   The updated display is stopped.
2. Drag with the mouse to draw a box around the area to be zoomed.

   If there are at least two measured values within this area, the area of the trend is zoomed.
3. To return to the original view of the trend, click "Original view".
4. To restart the update, click "Start/Stop".

The default values are used for the axis.

**Using the mouse wheel**

Requirement: No zoom button was clicked in the toolbar.

1. Pause the update of the trend control.
2. Press <Ctrl> and move the mouse wheel.

###### Zooming in or out on trends

If you zoom in or out on a trend, the 50% value of the trend is always in the middle of the value axes.

Proceed as follows to zoom in or out on a trend:

1. Click "Zoom +/-".

   The updated display is stopped.
2. To zoom in on a trend, click on the trend with the left mouse button.
3. To zoom out on a trend, hold down the <Shift> key and click on the trend with the left mouse button.
4. To return to the original view of the trend, click "Original view".
5. To restart the update, click "Start/Stop".

The default values are used for the axis.

> **Note**
>
> If you change the value area of a value axis on the "Value Axis" tab in the configuration dialog while zooming, the visible zoom area is set to the new value area.

###### Zooming in on the time axis or value axis

While zooming with time or value axes, the 50% value of the trend is always in the middle of the axes.

Proceed as follows to zoom the time axis or value axis:

1. To zoom in or out on the time axis, click on "Zoom time axis +/-".

   The updated display is stopped.
2. To zoom in or out on the value axis, click on "Zoom value axis +/-".

   The updated display is stopped.
3. To zoom in on an axis, click on the trend control with the left mouse button.
4. To zoom out on an axis, hold down the <Shift> key and click on the trend control with the left mouse button.
5. To return to the original view of the trend, click "Original view".
6. To restart the update, click "Start/Stop".

The default values are used for the axis.

###### Zooming using touch gestures

Refer to the section [Supported gestures](#supported-gestures-rt-unified).

###### Sorting trends (RT Unified)

If a trend area contains multiple trends, you can select the order of the trends.

You have the following options:

- Specify the top trend
- Specify the order of all trends

###### Specify the trend order

**Requirement**

The "Select trend" button is configured in the toolbar.

**Procedure**

1. Click "Select trend" in the toolbar.
2. Click on a trend.
3. Move the trend to the selected position using the buttons.
4. Repeat these steps for the other trends.

> **Note**
>
> The trend at the top position is displayed in the trend area as the top trend.

###### Specify the top trend

In the drop-down list of the trend area, select the trend that you want to display as top trend.

Alternatively, use the "Select trend" button in the toolbar and move the desired trend to the top position.

###### Hiding and showing trends (RT Unified)

###### Requirement

The "Select trend" button is configured in the toolbar.

###### Procedure

1. Click "Select trend" in the toolbar.
2. Disable the trend option to hide a trend.
3. Enable the trend option to show a trend.

###### Determining the coordinates of a point (RT Unified)

###### Introduction

The "Ruler" button is used to determine the coordinates of a point on the trend by means of a ruler. You can zoom in on an area of the trend to make coordinate finding easier. If you display the ruler in the trend control, you can move the ruler at any time.

If you click on the trend with the mouse, several trend parameters are shown in the tooltip for the trend control.

###### Requirement

- A trend control is configured
- A trend companion is configured and connected with the trend control
- The "Ruler window" display mode is activated in the trend companion
- Runtime is activated

###### Procedure

Proceed as follows to determine the coordinates of a point:

1. Click "Ruler" in the trend control.

   The ruler is shown.
2. Move the ruler to the desired position with the mouse.
3. If you want to zoom in on an area, click on "Zoom area".

   - Move the ruler to the desired position with the mouse.
   - To return to the original view, click "Original view".

###### Result

In the ruler window of the trend companion, besides the X value/time stamp and the Y value, the data that you have configured in the trend companion is shown in the columns.

In the trend companion, the indices "i" and "u" can be displayed in addition to the values:

- "i.": The displayed value is an interpolated value.
- "u.": The displayed value has an uncertain status:

  - The start value after Runtime activation is unknown
  - A substitute value is used

    > **Note**
    >
    > You can also display the "uncertain" status of a value in the displayed trend curve. You must activate the "Value with uncertain status" option on the "Trends" tab under "Limits".

###### Alternative procedure

Alternatively, you can also connect the trend companion to the process control. In the "ruler window" display mode, the values of the selected row are displayed in the trend companion.

###### Select data connection of a trend (RT Unified)

You have the option to set in Runtime the source from which a trend is supplied.

Possible sources:

- Tags and logging tags of an HMI device, plant object or PLC
- UDTs

###### Requirement

- An HMI device has been configured.
- A trend control is configured in the screen of the device.
- To display logging tags: A data log has been configured.
- To display the tags of a plant object: The plant hierarchy has been created and assigned to the HMI device.
- Runtime is active.

###### Procedure

|  |  |  |
| --- | --- | --- |
| 1. Click on "Select data connection" in the toolbar of the trend control.     The "Selection of logs/tags" dialog opens. 2. Click "Trend:" and select a trend. 3. Click "Tag".    The "Browser view" dialog opens in which you specify how the selected trend is supplied with data.                ![Procedure](images/118555404811_DV_resource.Stream@PNG-en-US.png)         ![Procedure](images/118555404811_DV_resource.Stream@PNG-en-US.png) 4. (Optional) Define in a filter. 5. Use the toolbar to configure the display in the dialog:        |  |  |  |    | --- | --- | --- |    | ![Procedure](images/114189909515_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/114189909515_DV_resource.Stream@PNG-de-DE.png) | "Small icons" |  |    | ![Procedure](images/114190276491_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/114190276491_DV_resource.Stream@PNG-de-DE.png) | "List" |  |    | ![Procedure](images/114190310667_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/114190310667_DV_resource.Stream@PNG-de-DE.png) | "Details" |  | 6. Use the toolbar to configure the contents of the dialog:        |  |  |  |    | --- | --- | --- |    | ![Procedure](images/114190319243_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/114190319243_DV_resource.Stream@PNG-de-DE.png) | "Online tags" | Shows the device and its tags. |    | ![Procedure](images/114190353419_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/114190353419_DV_resource.Stream@PNG-de-DE.png) | "Logging tags" | Shows the device and its logging tags. |    | ![Procedure](images/114190361995_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/114190361995_DV_resource.Stream@PNG-de-DE.png) | "CPM" | Shows the plant hierarchy and the plant object tags. |    | ![Procedure](images/114190370571_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/114190370571_DV_resource.Stream@PNG-de-DE.png) | "UDT" | Shows the device and its UDTs. |    | ![Procedure](images/114190379147_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/114190379147_DV_resource.Stream@PNG-de-DE.png) | "CPM logging tags " | Shows the plant hierarchy and the logging tags of the plant objects. | 7. In the tree, select the object whose data you want to display in the trend control. 8. Select a tag as the data source. 9. Confirm your entries. |  |  |

The values of the tags are displayed in the trend control. If the path belongs to a plant object, the path of the plant object is also shown in the trend control.

![Procedure](images/110988270475_DV_resource.Stream@PNG-en-US.png)

###### Changing the time range of a trend (RT Unified)

###### Procedure

To configure the time range, follow these steps:

1. Click "Select time range" in the toolbar of the trend control.

   The "Time selection" dialog opens.
2. Under "Time axes", select the time axis with the time range you want to adjust.

   Under "Trend area", you can see to which trend area the selected time axis belongs.

   If the trends in a trend control are to be displayed with a common time axis, the specified time range applies to all trends.
3. Configure the time range as described below.

> **Note**
>
> The format of date and time depends on the Runtime language used.

###### Configure time range

1. Select the "Time interval" entry in "Setting".
2. Select date and time of the start time.
3. Set the duration of the time range. To do this, enter a factor and select the time unit.

   Example: "90" as the factor and "Seconds" as the time unit for a duration of one and a half minutes.
4. Confirm your entries.

The time range of the time axis is adjusted:

- If the preset start time has been changed:

  - The trend update is paused.
  - The time axis starts with the selected start time.
- If the preset start time has been retained: The trend update continues. The preset start time is not included in the time axis.
- The duration of the time axis results from the factor and time unit.

###### Configure start time and end time

1. Select the "Start time and end time" entry in "Setting".
2. Select the date and time of the start time and end time.
3. Confirm your entries.

The time range of the time axis is adjusted:

- If the preset start time and/or end time has been changed:

  - The trend update is paused.
  - The time axis starts with the start time.
- If the preset start time and end time have been retained: The trend update continues. The preset start time and end time are not included in the time axis.
- The duration of the time axis results from the start time and end time.

###### Configure number of measuring points

1. Select the "Measuring points" entry in "Setting".
2. Select date and time of the start time.
3. Enter the number of desired measuring points under "Measuring points".
4. Confirm your entries.

The time range of the time axis is adjusted:

- If the preset start time has been changed:

  - The trend update is paused.
  - The time axis starts with the start time.
- If the preset start time has been retained: The trend update continues. The preset start time is not included in the time axis.
- The duration of the time axis results from the number of measuring points multiplied by the update cycle.

---

**See also**

[Basics of time range (RT Unified)](#basics-of-time-range-rt-unified)

###### Display context data of the plant objects in a trend control (RT Unified)

This section describes how to show context-dependent data of a plant object in the trend control.

The evaluation is relevant, for example, in connection with the WinCC Performance Insight in order to analyze the effectiveness or the fault rate of the plant.

###### Requirement

- A trend control is configured in the screen of an HMI device.
- The plant hierarchy has been created and assigned to the HMI device.
- The data source of one of the trends in the trend control is a plant object.
- To display the logging tags of the plant object: A data log has been configured.
- Contexts are available for the plant object.
- The "Select context" button is configured for the trend control.

###### Procedure

1. In the trend control, click "Select context".
2. Select the plant object set as data source.
3. Select one of the contexts assigned to the plant object in the "Context" drop-down list.

   A list of the entries logged for the context appears under "Logged context values".
4. Select an entry.
5. Click "OK".

   ![Procedure](images/110988279051_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/110988279051_DV_resource.Stream@PNG-en-US.png)

###### Result

The time period of the selected entry is applied to the time axis of the trend area. The trend represents the data that falls within the time period of the selected entry.

> **Note**
>
> **Effect on other trend areas**
>
> If the plant object selected as data source has multiple interface tags and trends from other trend areas of the trend control display these tags, their time axes are also updated accordingly.

---

**See also**

[Select data connection of a trend (RT Unified)](#select-data-connection-of-a-trend-rt-unified)
  
[Contexts (RT Unified)](#contexts-rt-unified)

#### Process control (RT Unified)

This section contains information on the following topics:

- [Overview of process control (RT Unified)](#overview-of-process-control-rt-unified)
- [Using the process control (RT Unified)](#using-the-process-control-rt-unified)

##### Overview of process control (RT Unified)

With the process control, you display active or logged process values in a table. You design the display of the table as you wish.

You create statistics from selected data. You also export the data for further use.

![Figure](images/105790537227_DV_resource.Stream@PNG-de-DE.png)

###### Buttons of the process control

The following table shows the buttons that are available in the process control:

| Icon | Name | Function | ID |
| --- | --- | --- | --- |
| ![Buttons of the process control](images/111939775499_DV_resource.Stream@PNG-de-DE.png) | "First data record" | Displays the history of a tag within a specified time range starting with the first logged value.  Requirement: Values come from a process value log. | 0 |
| ![Buttons of the process control](images/105772640907_DV_resource.Stream@PNG-de-DE.png) | "Previous data record" | Displays the history of a tag within the previous time interval, based on the currently displayed time interval.  Requirement: Values come from a process value log. | 1 |
| ![Buttons of the process control](images/105773272715_DV_resource.Stream@PNG-de-DE.png) | "Start/stop" | Stops and starts the column update. The values are buffered and updated as soon as you start the column update again. | 2 |
| ![Buttons of the process control](images/105772648331_DV_resource.Stream@PNG-de-DE.png) | "Next data record" | Displays the history of a tag within the next time interval, based on the currently displayed time interval.  Requirement: Values come from a process value log. | 3 |
| ![Buttons of the process control](images/105772655755_DV_resource.Stream@PNG-de-DE.png) | "Last record" | Displays the history of a tag within a specified time range ending with the last logged value.  Requirement: Values come from a process value log. | 4 |
| ![Buttons of the process control](images/105790085259_DV_resource.Stream@PNG-de-DE.png) | "Edit" | Activates editing of table entries. To edit a value, double-click in the desired table cell.  Requirement: Updated display is stopped. | 5 |
| ![Buttons of the process control](images/105790092811_DV_resource.Stream@PNG-de-DE.png) | "Previous column" | Moves the value column in front of the previous value column.  The function refers to the value columns that are assigned to a time axis. | 6 |
| ![Buttons of the process control](images/105790509707_DV_resource.Stream@PNG-de-DE.png) | "Next column" | Moves the value column to behind the next value column.  The function refers to the value columns that are assigned to a time axis. | 7 |
| ![Buttons of the process control](images/105772702091_DV_resource.Stream@PNG-de-DE.png) | "Select time range" | Opens a dialog in which you configure the time range. | 8 |
| ![Buttons of the process control](images/105772694667_DV_resource.Stream@PNG-de-DE.png) | "Select data connection" | Opens the dialog for selecting the logs and tags of an HMI device, plant object or PLC that serve as data source for this table view. | 9 |
| ![Buttons of the process control](images/112273930251_DV_resource.Stream@PNG-de-DE.png) | "Create archive value" | Creates a table entry for a log value.  Enter the log value manually. Its time stamp corresponds to the time at which you added the table entry. | 10 |
| ![Buttons of the process control](images/112273939083_DV_resource.Stream@PNG-de-DE.png) | "Delete archive value" | Deletes a logged value. | 11 |
| ![Buttons of the process control](images/105745968651_DV_resource.Stream@PNG-de-DE.png) | "Export" | Exports all or selected data to a *.CSV file.  Depending on the configuration and authorizations, the following options may be available:  - Display export settings and start export - Select file name and directory | 12 |

##### Using the process control (RT Unified)

This section contains information on the following topics:

- [Online configuration of the process control (RT Unified)](#online-configuration-of-the-process-control-rt-unified)
- [Editing a table field (RT Unified)](#editing-a-table-field-rt-unified)
- [Moving value columns (RT Unified)](#moving-value-columns-rt-unified)

###### Online configuration of the process control (RT Unified)

###### Introduction

In Runtime, you configure online and thus change the layout of the process control. The process control configuration specifies whether online configurations are retained or discarded on a screen change or after Runtime is ended.

###### Overview

The following buttons make online configuration possible in process control:

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/105772694667_DV_resource.Stream@PNG-de-DE.png) | "Select data connection" |
| ![Overview](images/105772702091_DV_resource.Stream@PNG-de-DE.png) | "Select time range" |

###### Changing the data connection

The following table shows the configuration options for data connection:

| Field | Description |
| --- | --- |
| Value column | Choose the configured value column for which you want to change the data connection. |
| Data Source | Define whether the selected value column is supplied with a logging tag or online tag. |
| Tag name | Select the tag name for the data connection. |

Proceed as follows to change the data connection:

1. Click "Select data connection" in the toolbar.

   The "Log/tag selection" dialog is opened.
2. Choose the "Value column" for which you want to change the data connection.
3. Select the "Data supply" and the "Tag name".

###### Changing a time range

The following table shows the configuration options for the time range:

| Field | Description |
| --- | --- |
| Time column | Select the configured time column for which you want to define a time range. |
| Time range | Set the time range:  - If you want to define a fixed time interval, select the setting "Start to end time". Enter the date and time for each. - If you want to define a time period, select the setting "Time range". Define the date and time for the start time. The length of the time interval to be displayed is determined by multiplying the "Factor" by the "Unit of time". - If you want to display a certain number of values, select the setting "Number of measuring points". Define the date and time for the start time. Enter the desired number of measuring points in the input field. |

To configure the time range, follow these steps:

1. Click "Select time range" in the toolbar of the process control.

   The "Time - Selection" dialog opens.
2. Choose the "Time column" for which you want to adapt the time range.

   If the columns of a process control are to be displayed with a common time axis, the specified time range applies to all columns.
3. Configure the time range.

   The entry format of the date and time depends on the Runtime language used.

###### Editing a table field (RT Unified)

###### Introduction

You change the values displayed in the process control manually using the "Edit" button.

###### Overview

The following buttons allow you to edit the table fields:

| Symbol | Meaning |
| --- | --- |
| ![Overview](images/105773272715_DV_resource.Stream@PNG-de-DE.png) | "Start/stop" |
| ![Overview](images/105790085259_DV_resource.Stream@PNG-de-DE.png) | "Edit" |

###### Requirement

- The process control is configured
- The "Edit" button is configured
- Runtime is activated

###### Procedure

Proceed as follows to edit a table field in Runtime:

1. Click "Stop" in a process control.

   The updated display is stopped, the process data continues being logged.
2. Click "Edit".
3. Double click on the desired table field of a value column.
4. Enter the new value.

   The changed value is logged.
5. To continue with the display of Runtime data in the process control, click on "Start".

###### Moving value columns (RT Unified)

You can rearrange the value columns assigned to a time axis.

###### Via the toolbar

1. Click on a column.
2. To move a column to the left, select "Previous column" in the toolbar

   The column is shifted one position to the left.

   If you have selected the first column, it is moved to the end of the value columns.
3. To move a column to the right, select "Next column" in the toolbar.

   The column is shifted one position to the right.

   If you selected the last column, it is moved to the beginning of the value columns.

###### With the mouse

See section [Rearranging columns at runtime](#rearranging-columns-at-runtime-rt-unified).

### Screen window (RT Unified)

#### Use

The "Screen window" object is used to display other screens of the project in the current screen. To continuously update the content of a screen window, for example, the object must be dynamized. Custom menus and toolbars can add specific buttons to the screen window.

You can also use independent screen windows independently of the screen in question. With appropriate hardware equipment and support by the operating system, you can also control multiple monitors and map processes in a more comprehensive and differentiated manner.

![Use](images/105837748363_DV_resource.Stream@PNG-de-DE.png)

#### Layout

The settings for the position, geometry, style and color of the object are made during configuration.

In particular, the following properties are changed:

- Zoom factor: Defines the size of the embedded screen.
- Screen section: Defines the section of the embedded screen that is displayed in the screen window. If the embedded screen is larger than the screen window, you configure scroll bars for the screen window.
- Independent screen windows: Specified that the screen windows are displayed independently from the screen in which they were configured.

> **Note**
>
> **Cascading screen windows**
>
> Screen windows can also display screens which, in turn, contain screen windows. Up to 14 cascaded screen windows can be displayed.

### Web control (RT Unified)

#### Introduction

The "Browser" control is designed for the visualization of simple HTML pages. It allows creation of centrally stored machine-specific descriptions, which are displayed from different HMI devices.

You have access to the data of the local user management in Runtime via a browser.

![Introduction](images/105837739659_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> Switching the functionality of the web control as a file explorer, in the following ways, for example, is not enabled in WinCC:
>
> - Entry of a folder or drive, e.g. "\" or "C:", or
> - Connection to an FTP server, for example, "ftp://"
>
> One reason this function is not implemented is to prevent inadvertent changes to files, their deletion or execution.
>
> When configuring, ensure that the operator can only enter valid Internet addresses, for example, by using symbolic I/O fields. Configure a password-protected input for service purposes.

> **Note**
>
> **Page navigation in the web control**
>
> Whether you can navigate back and forth between the pages that you have viewed in the web control depends on the browser and browser versions in which Runtime is running. If the browser or browser versions do not support page navigation, the buttons in the web control are disabled.

#### Displayed content

Remember the following notes when using the control:

- The "Browser" control only shows contents that are supported by the browser in which Runtime is open.
- The control is implemented as IFrame. Pages with X-Frame option settings that prevent the display in an IFrame are not displayed in the control.
- As compared to a standard browser, the "Browser" control has limited functionality:

  - Navigation from the "Browser" control is not supported (top-level navigation).
  - Calls of queries and dialogs (pop-ups and modal dialogs) are only supported if they were activated in the file <Path for the WinCC Unified installation directory>WinCCUnified\WebRH\public\content\custom\CustomSettings.json:

    `{"CustomSettings": {"HmiWebControl" : {"AllowPopups" : true,"AllowModals" : true}}}`

    > **Note**
    >
    > Pop-ups and modal dialogs stop the update.
  - Links to embedded files, for example, *.pdf or *.xls, are not supported.
  - Queries and dialogs that are conducted during the access of, for example, protected pages are not supported.

### Media player

#### Use

In Runtime, the media player is used to play multimedia files via an https connection.

![Use](images/105838190987_DV_resource.Stream@PNG-de-DE.png)

#### Layout

The settings for the position, style and color of the object are made during configuration.

In particular, the following properties are changed:

- Display operator controls: Specifies the buttons in runtime.
- Show tracker: establishes, whether a slider is available for the operation.

#### Supported file formats

The media player supports all formats that support the HTML5 video tag.

#### Restrictions

> **Note**
>
> **Play restrictions**
>
> - The web control security settings do not allow local files to be played.
> - Playing multimedia files in the Runtime control system depends on factors such as the installed operating system, the browser used and video and audio codecs installed on the machine.
>
>   Examples:
>
>   - Internet Explorer does not play any video file with an embedded .wav audio file.
>   - Most browsers do not support .avi files.
> - The browser determines which video formats are supported.
>
>   You can find an overview of the video formats supported by popular browsers [here](https://www.w3schools.com/html/html5_video.asp).
>
>   You can find a detailed overview of the browser version used or between browsers [here](https://html5test.com/compare/browser/index.html).
> - iOS guidelines for the <video autoplay> element are available [here](https://webkit.org/blog/6784/new-video-policies-for-ios/).

> **Note**
>
> **Requirements for video files**
>
> To play video files in the Windows Server 2008 R2 SP1 and 2012 R2, install the Microsoft feature "Desktop Experience". You will find more detailed information on this topic on the Internet in the Microsoft documentation.

> **Note**
>
> **Data loss when copying the project**
>
> If you copy the project to another PC, keep the following in mind:
>
> Files indicated in the WinCC Media Control are not copied along with the other files if they are dynamically linked and no UNC path is specified. You have to load the files into the project again.

### System diagnostics display (RT Unified)

#### Use

You can use the "System diagnostics control" object to display the diagnostic status of several PLCs using traffic light SVGs. The diagnostic status contains the overall status of all relevant PLCs. The merged state is always the worst state of all PLCs.

#### Defining the properties of the system diagnostics control

You define the properties of the system diagnostics control in the Inspector window under "Properties > Properties".

![Defining the properties of the system diagnostics control](images/160544793227_DV_resource.Stream@PNG-en-US.png)

#### Selecting the view type

You select the view type in the following way:

1. Click "Properties > Properties > General > View type" in the Inspector window.
2. Select between the "Matrix view", "Diagnostic view" and the "Distributed I/O view".

Selection of the matrix view as start view is recommended. From the matrix view, you can switch to the diagnostic view using the corresponding button in the toolbar.

**Matrix view**

With the matrix view, you have the possibility to check the status of your PLCs and their lower-level hardware components.

All hardware components are displayed as tiles. You can configure the display as well as the content of the tiles:

Make the settings for hardware details and tiles under "Properties > Properties > General > Matrix view".

![Selecting the view type](images/160598299403_DV_resource.Stream@PNG-en-US.png)

**Diagnostic view**

The diagnostic view shows the diagnostic buffer of the PLC with the diagnostic events of the currently selected PLC.

It is not possible to switch between different PLCs in Runtime. Navigating to the diagnostic view via the selected PLC in the matrix view is recommended.

Under "Properties > Properties > General > Diagnostic view", you make the settings for the rows, header, grid lines, scroll bar, cells and columns.

![Selecting the view type](images/160598250123_DV_resource.Stream@PNG-en-US.png)

**Distributed I/O view**

The distributed I/O view shows the distributed devices of the Profinet IO system.

The requirement is that only one PLC is configured with a Profinet IO system. Otherwise, Runtime changes back to the matrix view.

Using the "Start page" button, you can switch from the distributed I/O view to the diagnostic overview. From the distributed I/O view, you can also jump to the diagnostic buffer.

If the Profinet IO system is not accessible, the diagnostic overview is displayed.

If you change the device version from 18.00.01.01 to 18.00.01.00, the matrix view is displayed and the distributed I/O view is not visible in the selection field.

#### Setting up column sorting

To set up the column sorting in the diagnostic view, follow these steps:

1. In the Inspector window, click "Properties > Properties > General > Diagnostic view > Columns > [0] Column".
2. Select the sorting direction and sorting order for the individual columns.

#### Dynamization of graphic properties with tags or scripts

You can dynamize the following properties containing a graphic with a tag or with a script:

- Graphic
- Icon

#### Access protection in Runtime

Configure access protection with the property "Operator control - allow" in the Inspector window under "Properties > Properties > Security". A logged-in user having the required authorization can acknowledge and edit the system diagnostics control using the buttons in the system diagnostics control.

#### Configuring the information bar

The information bar of the system diagnostics control shows the connection status and path.

The connection status is not displayed while the PLC is starting.

To configure the information bar, follow these steps:

1. Configure the general properties of the information bar, such as the font and background color, under "Properties > Properties > Miscellaneous > Information bar".
2. Configure the display of the information bar elements under "Properties > Properties > Miscellaneous > Information bar > Elements".

#### Toolbar

You can define the buttons of the system diagnostics control in Runtime and their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Toolbar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the system diagnostics control:

| Button |  | Function |
| --- | --- | --- |
| ![Toolbar](images/155631893131_DV_resource.Stream@PNG-de-DE.png) | Home | Shows the home page. |
| ![Toolbar](images/143094621963_DV_resource.Stream@PNG-de-DE.png) | Reload | Updates the view of the diagnostic event. |
| ![Toolbar](images/132458615563_DV_resource.Stream@PNG-de-DE.png) | First line | Selects the first of the pending diagnostic events. The visible area of the view is moved. |
| ![Toolbar](images/132458689035_DV_resource.Stream@PNG-de-DE.png) | Previous line | Selects the previous diagnostic event, starting from the currently selected diagnostic event. The visible area of the view is moved. |
| ![Toolbar](images/132458681611_DV_resource.Stream@PNG-de-DE.png) | Next line | Selects the next diagnostic event, starting from the currently selected diagnostic event. The visible area of the view is moved. |
| ![Toolbar](images/132458622987_DV_resource.Stream@PNG-de-DE.png) | Last line | Selects the last of the pending diagnostic events. The visible area of the view is moved. |
| ![Toolbar](images/143097143051_DV_resource.Stream@PNG-de-DE.png) | Share view | Enables/disables the detail view. |
| ![Toolbar](images/156264938379_DV_resource.Stream@PNG-de-DE.png) | Previous | Navigates to the previous PLC. |
| ![Toolbar](images/155631901707_DV_resource.Stream@PNG-de-DE.png) | Show diagnostic buffer | Changes from the matrix view to the diagnostic view. The diagnostic view shows the diagnostics buffer of the PLC.   This button is only enabled if a PLC or one of its lower-level modules is shown in the matrix view. |

#### Setting the time zone

Under Properties > Properties > Miscellaneous > Time zone, you set the desired time zone by entering a decimal value for the time zone.

- "0" and positive numerical values: The values correspond to the index values of the Microsoft time zones.
- "-1": The local time zone of the device.

> **Note**
>
> **In Runtime, you also have the option of setting the time zone via a selection list.**

---

**See also**

[Activating system diagnostics (S7-1200/1500) (RT Unified)](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#activating-system-diagnostics-s7-12001500-rt-unified)
  
[Configuring diagnostics indicators (S7-1200/1500) (RT Unified)](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#configuring-diagnostics-indicators-s7-12001500-rt-unified)
  
[Configuring system diagnostics of the controller (S7-1200/1500) (RT Unified)](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#configuring-system-diagnostics-of-the-controller-s7-12001500-rt-unified)

### Plant overview (RT Unified)

#### Introduction

The "Plant overview" object shows you the configured plant hierarchy in Runtime. In the plant overview, you can navigate through the system to the plant objects and see the plant at a glance.

With the corresponding configuration of the lower-level plant objects and the assigned HMI device during the engineering, the plant overview also offers you the following options:

- Obtaining an overview of the plant objects for which alarms are available
- Displaying the alarms of a plant object
- Display of configured screens of a plant object.

#### Overview of the Plant overview

![Overview of the Plant overview](images/140062014859_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| 1 | Toolbar |
| 2 | Menu bar |
| 3 | Filter bar |
| 4 | Plant tree |
| 5 | Alarm icon  Alarms are available for the plant object or one of its lower-level plant objects. |

The following buttons are available in the toolbar and in the filter bar:

| Icon | Name | Function |
| --- | --- | --- |
| ![Overview of the Plant overview](images/112293564299_DV_resource.Stream@PNG-de-DE.png) | Expand all | Expands all lower-level plant objects of the plant object selected in the control. |
| ![Overview of the Plant overview](images/112293572875_DV_resource.Stream@PNG-de-DE.png) | Collapse all | Recursively collapses all lower-level plant objects of the selected plant object. |
| ![Overview of the Plant overview](images/140086161419_DV_resource.Stream@PNG-de-DE.png) | Expand or collapse the filter bar | Opens or closes the filter bar. |
| ![Overview of the Plant overview](images/114736578699_DV_resource.Stream@PNG-de-DE.png) |  | Filters the plant overview:  - No filter: You see all plant objects - For plant objects for which alarms are available - According to plant objects for which screen windows are configured |
| ![Overview of the Plant overview](images/140087821195_DV_resource.Stream@PNG-de-DE.png) | Search field | Filters according to the entered text. |

When configuring in the engineering system, you can hide the toolbar and menu bar.

#### Requirement

- The plant view has been created and assigned to an HMI device.
- The "Plant overview" object is configured in the screen of the assigned HMI device.
- Optional:

  - The "Dynamic" navigation type is configured in the engineering system for the plant overview.
  - A root node is configured in the engineering system for the plant overview.
- Runtime is active.

#### Operation

**Expand and collapse plant tree**

- To show all lower-level plant objects of a plant object, click the "Expand all" button.

  To collapse the plant tree, click "Collapse all".
- To expand only the lower-level objects of the next level, click the button with the triangle next to the plant object.

  To collapse the level again, click again on the button with the triangle.

  Alternatively, you can double-click the plant object to expand or collapse lower-level objects.

**Select plant objects**

- To select a plant object, click on the plant object in the plant tree.

  The path to the selected plant object appears in the menu bar of the "Plant overview" object:

  ![Operation](images/114727539083_DV_resource.Stream@PNG-de-DE.png)
- To see which lower-level objects a plant object displayed in the menu bar has at the next level, click the arrow in the menu bar next to the plant object.

  ![Operation](images/114736477195_DV_resource.Stream@PNG-de-DE.png)
- To go from the menu bar to the overview, click on one of the plant objects shown in the menu bar.

**Dynamic navigation**

If dynamic navigation is enabled in the engineering system, specify the level from which the plant tree is displayed.

The buttons of the toolbar and the filter bar relate to the displayed area.

- To select a plant object, click on the object in the menu bar or double-click on the object in the plant tree.

  The levels below the selected plant object are available.
- To navigate up one level, click on the up arrow next to the plant object.

  ![Operation](images/140087830539_DV_resource.Stream@PNG-de-DE.png)

**Root node**

You have the option of defining a root node in the engineering system.

If a root node is configured, the root node and all objects below the root node are available in the plant overview.

---

**See also**

[Display alarms for plant objects (RT Unified)](#display-alarms-for-plant-objects-rt-unified)

### Plant overview with companion controls (RT Unified)

#### Requirement

- The plant view has been created and assigned to a device.
- The "Plant overview" object is configured in the screen of the assigned device.
- The objects "Alarm control" and "Screen window" are configured in the screen of the assigned device and configured as companion controls of the plant overview.
- Screens are configured at the plant objects.
- Runtime is active.

#### Display alarms

To display the alarms of a plant object, click on the alarm icon.

The alarm control shows the alarms of the plant object.

> **Note**
>
> The alarm icon only appears when an alarm has occurred at the respective plant object or one of its lower-level objects. The alarm icon disappears again when the alarm is no longer present.

#### Show a screen of a plant object

To show the screen of a plant object, click on the plant object.

The screen window shows the screen of the assigned HMI device.

If you have not configured any screen window, a screen of the plant object with text box "$POName$" appears.

> **Note**
>
> "$POName$" is an expression with which the name of the plant object is resolved.

### Parameter set control (RT Unified)

This section contains information on the following topics:

- [Overview of parameter set control (RT Unified)](#overview-of-parameter-set-control-rt-unified)
- [Operate parameter set control (RT Unified)](#operate-parameter-set-control-rt-unified)

#### Overview of parameter set control (RT Unified)

##### Introduction

Set up the machine for production in Runtime using parameter sets. The elements in a parameter set are defined in engineering by defining its parameter set type.

In Runtime, the parameter sets are displayed in the parameter set control. In the control, you manage the parameter sets and load a parameter set into the PLC to set up a machine for production.

##### Example

A bakery generates the following parameter set types in the engineering system:

- Bread
- Bread rolls
- Cake

The elements of the parameter set types define the ingredients of these products. For example, the parameter set type "Bread" has the following elements:

- Flour
- Salt
- Syrup
- Yeast
- Water

In Runtime, the bakery creates parameter sets for the "bread" parameter set type for the bread types to be produced:

- White bread
- Wholewheat bread
- French bread

The quantities required for this type of bread are entered in the elements.

During production, an operator selects the parameter set to be produced next and writes it to the PLC.

##### User interface

![User interface](images/143833696139_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Area for selecting the parameter set types and parameter sets |
| ② | Parameter table   Displays the values of the selected parameter set or parameter set type. The columns in the table depend on the configuration in engineering. |
| ③ | Toolbar |
| ④ | Information bar  The elements in the information bar depend on the configuration in engineering. |

> **Note**
>
> **Fixed parameter set type**
>
> The parameter set control in the engineering system can be configured so that you are only offered the parameter sets of a certain parameter set type and cannot select any other parameter set types.

##### Parameter set control buttons

The toolbar contains buttons for executing specific functions. Depending on the configuration, the following buttons are available for operator input:

|  | Button | Function |
| --- | --- | --- |
| ![Parameter set control buttons](images/110181830795_DV_resource.Stream@PNG-de-DE.png) | Create | Creates a new parameter set. |
| ![Parameter set control buttons](images/110183221771_DV_resource.Stream@PNG-de-DE.png) | Save | Saves a parameter set. |
| ![Parameter set control buttons](images/110183230347_DV_resource.Stream@PNG-de-DE.png) | Save as | Opens the selection dialog for the storage path of the selected parameter set. |
| ![Parameter set control buttons](images/110183264523_DV_resource.Stream@PNG-de-DE.png) | Rename | Renames the selected parameter set.  The new name must be unique. |
| ![Parameter set control buttons](images/110183337099_DV_resource.Stream@PNG-de-DE.png) | Write to PLC | Save the parameter set and writes it to the PLC. |
| ![Parameter set control buttons](images/110183345675_DV_resource.Stream@PNG-de-DE.png) | Read from PLC | Reads a Parameter set type or parameter set from the PLC. |
| ![Parameter set control buttons](images/110183443851_DV_resource.Stream@PNG-de-DE.png) | Import | Imports parameter sets to a TSV file. |
| ![Parameter set control buttons](images/110183503627_DV_resource.Stream@PNG-de-DE.png) | Export | Exports parameter sets to a TSV file. |
| ![Parameter set control buttons](images/110183512203_DV_resource.Stream@PNG-de-DE.png) | Cancel | Cancels the process. |
| ![Parameter set control buttons](images/154713266059_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes the selected parameter set.  The table shows the default values at the parameter set type. |

##### Rearranging columns

You can change the column arrangement configured in the engineering here. See section [Rearranging columns at runtime](#rearranging-columns-at-runtime-rt-unified).

#### Operate parameter set control (RT Unified)

This section contains information on the following topics:

- [Create parameter sets (RT Unified)](#create-parameter-sets-rt-unified)
- [Managing parameter sets (RT Unified)](#managing-parameter-sets-rt-unified)
- [Exporting and importing parameter sets (RT Unified)](#exporting-and-importing-parameter-sets-rt-unified)
- [Transferring parameter sets (RT Unified)](#transferring-parameter-sets-rt-unified)
- [Updating the UDTs (RT Unified)](#updating-the-udts-rt-unified)

##### Create parameter sets (RT Unified)

###### Requirements

- Parameter set types were configured in the engineering system.
- The parameter set control is configured in the screen of the device that is active in Runtime.

###### Create a new parameter set

To create a new parameter set, follow these steps:

1. Select a parameter set type in the parameter set control in "Parameter set type".

   The parameter table loads the columns and default values predefined at the parameter set type.
2. Click the "Create" button.
3. Optional: Enter the name of the new parameter set in "Parameter set name".

   The name must be unique for the parameter set type.
4. Optional: Enter the ID of the parameters set in "Number".

   The number must be unique for the parameter set type.
5. The find the values of the parameters set by clicking in a table cell and modifying the value predefined by the parameter set type.
6. Confirm.

**Note**

**Cancel creation**

Another parameter set parameters set type cannot be selected until you have saved the new parameter set or clicked on "Cancel".

The parameter set is created and saved.

###### Create a version of the existing parameter set

To create a new parameter set based on an existing parameter set, follow these steps:

1. Select a parameter set type in the parameter set control in "Parameter set type".
2. Select a parameter set in "Parameter set".

   The parameter set table loads the columns and values defined for the parameter set.
3. Click the "Save as" button.

   The "Save parameter set as" dialog opens.
4. Optional:

   - Overwrite the automatically generated name in "Parameter set name".

     The name must be unique.
   - Overwrite the ID in "Number".
5. Confirm.

   The new parameter set is created.
6. To change the values taken over from the original parameter set, click in a table cell and enter a new value.
7. Click the "Save" button.

The parameter set is created and saved.

##### Managing parameter sets (RT Unified)

###### Introduction

You manage parameter sets for different productions in a parameter set control in runtime. You have the following options for managing parameter sets:

- Create new parameter sets
- Copy parameter sets
- Change parameter sets
- Delete parameter sets
- Rename parameter sets

###### Requirement

- At least one parameter set type with elements has been created.
- A parameter set control has been configured.
- The project is in runtime.

###### Creating a new parameter set

To create a new parameter set, proceed as follows:

1. In the "Parameter set type" field, select the parameter set type for which you want to create a new parameter set.

   The elements of the selected parameter set type are displayed in the table.

   ![Creating a new parameter set](images/115373673227_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115373673227_DV_resource.Stream@PNG-en-US.png)
2. Click the "Create" button.

   The "Create parameter set" dialog opens.

   ![Creating a new parameter set](images/115378931339_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115378931339_DV_resource.Stream@PNG-en-US.png)
3. Enter a unique parameter set name under "Parameter set name".
4. Enter a unique parameter set ID under "Number".
5. Confirm the dialog.

   A new parameter set has been created and saved. The parameters of the new parameter set are displayed in the table. The parameters have the same values in the columns "Name" and "Unit of measurement" as the elements of the previously selected parameter set type. The defined start values are applied for the "Value" column. If you have not defined start values, the corresponding default values are used.

   ![Creating a new parameter set](images/115379043851_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115379043851_DV_resource.Stream@PNG-en-US.png)
6. Enter values for the parameters in the "Value" column.

   Depending on the configuration, the parameters already contain start values.

   ![Creating a new parameter set](images/115379053963_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115379053963_DV_resource.Stream@PNG-en-US.png)
7. Click the "Save" button.

   ![Creating a new parameter set](images/115379448075_DV_resource.Stream@PNG-en-US.png)

   ![Creating a new parameter set](images/115379448075_DV_resource.Stream@PNG-en-US.png)

**Note**

If you do not make any entries in the "Create parameter set" dialog and confirm the dialog, a new parameter set is also created and saved. In this case the new parameter set, however, has a unique parameter set name and a unique parameter set ID which were both automatically assigned by the system.

**Note**

The character ' is not permitted in the value of a parameter set.

###### Copying a parameter set

To copy a parameter set, proceed as follows:

1. In the "Parameter set type" field, select the parameter set type in which you want to copy an existing parameter set.

   The elements of the selected parameter set type are displayed in the table.
2. In the "Parameter set" field, select the parameter set you want to copy.

   The parameters of the selected parameter set are displayed in the table.
3. Click the "Save as" button.

   The "Save parameter set" dialog opens. A unique parameter set name is pre-assigned to the "Parameter set name" field.

   ![Copying a parameter set](images/115379637387_DV_resource.Stream@PNG-en-US.png)

   ![Copying a parameter set](images/115379637387_DV_resource.Stream@PNG-en-US.png)
4. Enter a different unique parameter set name under "Parameter set name" as required.
5. Enter a unique parameter set ID under "Number" as required.
6. Confirm the dialog.

**Note**

If you do not enter a parameter set ID under "Number" in the "Save parameter set" dialog and confirm the dialog, a unique parameter set ID is automatically assigned to the new parameter set.

###### Changing the parameter set

To change a parameter set, proceed as follows:

1. In the "Parameter set type" field, select the parameter set type in which you want to change an existing parameter set.

   The elements of the selected parameter set type are displayed in the table.
2. In the "Parameter set" field, select the parameter set you want to change.

   The parameters of the selected parameter set are displayed in the table.
3. Edit the values of the parameters in the "Value" column.
4. Click the "Save" button.

###### Deleting a parameter set

To delete a parameter set, proceed as follows:

1. In the "Parameter set type" field select the parameter set type in which you want to delete an existing parameter set.

   The elements of the selected parameter set type are displayed in the table.
2. In the "Parameter set" field, select the parameter set you want to delete.

   The parameters of the selected parameter set are displayed in the table.
3. Click "Delete".

###### Renaming a parameter set

To rename a parameter set, proceed as follows:

1. In the "Parameter set type" field, select the parameter set type in which you want to rename an existing parameter set.

   The elements of the selected parameter set type are displayed in the table.
2. In the "Parameter set" field, select the parameter set you want to rename.

   The parameters of the selected parameter set are displayed in the table.
3. Click the "Rename" button.

   The "Rename parameter set" dialog opens.

   ![Renaming a parameter set](images/115379941899_DV_resource.Stream@PNG-en-US.png)

   ![Renaming a parameter set](images/115379941899_DV_resource.Stream@PNG-en-US.png)
4. Enter a different unique name for the parameter set under "Parameter set name".
5. Confirm the dialog.

##### Exporting and importing parameter sets (RT Unified)

###### Introduction

In a parameter set control in runtime you export parameter sets from the parameter set memory to a "*.tsv" file to be able to edit them a text editor. In a parameter set control in runtime you furthermore import parameter sets from a "*.tsv" file into the parameter set memory. A "*.tsv" file is a text file that uses the tabulator as a list separator.

> **Note**
>
> To export and import the parameter sets, you can also use the system functions in the function list or in the scripts:
>
> - With the system function "ExportParameterSets" or "ExportParameterSets", the parameter sets are exported from the parameter set memory to a "*.tsv" file.
> - With the system function "ImportParameterSets" or "ImportParameterSets", the parameter records are imported from a "*.tsv" file into the parameter set memory.
>
> If the parameter `OutputStatus` is set to `True`, a status message is output in an alarm control configured in the screen.

###### Requirement

- At least one parameter set type with elements has been created.
- A parameter set control has been configured.
- The project is in runtime.

###### Exporting parameter sets of a parameter set type

Follow these steps to export the parameter sets of a parameter set type:

1. In the "Parameter set type" field, select the parameter set type whose parameter sets you want to export.

   ![Exporting parameter sets of a parameter set type](images/115380273035_DV_resource.Stream@PNG-en-US.png)

   ![Exporting parameter sets of a parameter set type](images/115380273035_DV_resource.Stream@PNG-en-US.png)
2. Click the ![Exporting parameter sets of a parameter set type](images/137222023435_DV_resource.Stream@PNG-de-DE.png) "Export" button.

   The "Export parameter set" dialog box opens. The name of the parameter set control is pre-assigned in the "File name" field.

   ![Exporting parameter sets of a parameter set type](images/143206337291_DV_resource.Stream@PNG-en-US.png)

   ![Exporting parameter sets of a parameter set type](images/143206337291_DV_resource.Stream@PNG-en-US.png)
3. If appropriate, change the name of the file to which you want to export the parameter sets under "File name".
4. Enable "Generate checksum" to export the parameter data set with a checksum.

   Parameter data sets with a checksum cannot be imported if they have been manipulated in the meantime.
5. Confirm the dialog.

   The parameter sets are exported to a ".tsv" file.

   This file is stored according to the download settings.

   The file has the following structure:

   - The first line contains the file header. The file header consists of identifier, delimiter, version of the exported file, decimal symbol and information on the number of languages in which the name of the parameter sets is stored.

     The line must not be changed. Otherwise, it is not possible to import parameter sets.
   - The second line contains the name of the parameter set type.
   - The third row contains the headers for parameter sets. LCID of the language and the names of the parameter set type items are listed.

     The header for parameter sets must not be changed.
   - From the fourth line on the parameter sets are listed.

   ![Exporting parameter sets of a parameter set type](images/115381790859_DV_resource.Stream@PNG-en-US.png)

   ![Exporting parameter sets of a parameter set type](images/115381790859_DV_resource.Stream@PNG-en-US.png)

###### Edit exported file

1. You can customize the file to meet your needs:

   - Change the values of existing parameters.
   - Add parameter sets.

   To be able to import the parameter sets after editing, note the following information:
2. Save the changes.

**Note**

- The parameters must be valid for the defined data type.
- The parameters must be within the limits defined in the parameter set type item.
- ID and name of the individual parameter sets must be unique.

###### Importing parameter sets into a parameter set type

To be able to import parameter sets, note the following requirements:

> **Note**
>
> - The import file must have the same file header and the same header for parameter sets as the export file. Otherwise, it is not possible to import parameter sets.
> - There is no parameter set with the same display name in any of the configured languages.
> - The numerical values in the import file are within the permitted value range of the corresponding configured data type.

To import parameter sets into a parameter set type, follow these steps:

1. In the "Parameter set type" field, select the parameter set type into which you want to import the parameter sets.
2. Click the ![Importing parameter sets into a parameter set type](images/137222031627_DV_resource.Stream@PNG-de-DE.png) "Import" button.

   The "Import parameter set" dialog box opens.

   ![Importing parameter sets into a parameter set type](images/143206326667_DV_resource.Stream@PNG-en-US.png)

   ![Importing parameter sets into a parameter set type](images/143206326667_DV_resource.Stream@PNG-en-US.png)
3. Select the file from which you want to import the parameter sets.
4. To overwrite parameter sets in the parameter set control that have the same ID as the imported parameter sets, activate the "Overwrite" option.

   Any added parameter sets whose IDs and parameter set names deviate from the existing parameter sets are imported regardless of the "Overwrite" option.
5. Enable "Check checksum" when importing a parameter data set exported with the "Generate checksum" option.
6. Confirm the dialog.

   The parameter sets are imported to the parameter set type.

**Note**

If you deactivate overwriting and if a parameter set with the same ID or the same parameter set name exists in the parameter set control, the import of parameter sets is not possible.

##### Transferring parameter sets (RT Unified)

###### Introduction

You have assigned an external HMI tag of the data type HMI or PLC user data type to a parameter set type. In a parameter set control in runtime you transfer the values of parameter sets to the PLC via the HMI tag. The parameter set values are used to set up machines for different productions.

In a parameter set control in runtime you furthermore read active parameter sets from the PLC into the parameter set control via the HMI tag. The read parameter set values are stored in the parameter set memory. By reading from the PLC, you call up currently used values from production machines for later use.

> **Note**
>
> You can also use system functions in the function list or in scripts to transfer parameter sets between HMI device and PLC:
>
> - With the system function "ReadAndSaveParameterSet" or "ReadAndSaveParameterSet", a parameter set is read from the PLC and saved in the parameter set memory.
> - With the system function "LoadAndWriteParameterSet" or "LoadAndWriteParameterSet", a parameter set is loaded from the parameter set memory and written to the PLC.

###### Requirement

- A parameter set type with elements has been created.
- An external HMI tag of the data type HMI or PLC user data type is assigned to the parameter set type.
- A parameter set control has been configured.
- The project is in runtime.
- At least one parameter set has been created in the parameter set type.

###### Transferring a parameter set to the PLC

To transfer a parameter set to the PLC, follow these steps:

1. In the "Parameter set type" field, select the parameter set type.
2. In the "Parameter set" field, select the parameter set whose values you want to transfer to the PLC.

   ![Transferring a parameter set to the PLC](images/115381863307_DV_resource.Stream@PNG-en-US.png)

   ![Transferring a parameter set to the PLC](images/115381863307_DV_resource.Stream@PNG-en-US.png)
3. Click the "Write to PLC" button.

###### Reading a parameter set from PLC

To read a parameter set from the PLC, follow these steps:

1. In the "Parameter set type" field, select the parameter set type.
2. In the "Parameter set" field, select the parameter set whose values you want to read from the PLC.
3. Click the "Read from PLC" button.

**Note**

If do you not select a parameter set in the in the "Parameter set" field, a new parameter set is created in the parameter set control while reading from the PLC.

> **Note**
>
> A parameter set cannot be read from the PLC if minimum and/or maximum values are defined for a parameter set type item and the value in the parameter set to be transferred is outside this range. An alarm is triggered.

###### Result

- You have transferred the values of parameter sets between the HMI device and PLC.
- If parameter set data was not saved in Runtime, this data is saved by writing to the PLC in Runtime.

##### Updating the UDTs (RT Unified)

Parameter set types are linked to UDTs. If the UDT of a parameter set type is replaced or edited in the engineering system, the derived parameter sets are updated accordingly in Runtime after the next compilation and loading:

- Replacement of the UDT

  The parameter sets created in Runtime are retained. They adopt the elements and default values of the new UDT.
- Assignment of another UDT version

  The parameter sets created in Runtime are retained. New elements are assigned default values, deleted elements are removed.

### Reports (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified-1)
- [Requirements and restrictions (RT Unified)](#requirements-and-restrictions-rt-unified)
- [Workflow for working with reports in Runtime (RT Unified)](#workflow-for-working-with-reports-in-runtime-rt-unified)
- [The user interface of the "Reports" control (RT Unified)](#the-user-interface-of-the-reports-control-rt-unified)
- [Setting global email settings (RT Unified)](#setting-global-email-settings-rt-unified)
- [Configuring job parameters (RT Unified)](#configuring-job-parameters-rt-unified)
- [Configuring report jobs (RT Unified)](#configuring-report-jobs-rt-unified)
- [Running a report job manually (RT Unified)](#running-a-report-job-manually-rt-unified)
- [Downloading reports (RT Unified)](#downloading-reports-rt-unified)
- [Exporting an offline configuration file (RT Unified)](#exporting-an-offline-configuration-file-rt-unified)
- [Transferring the control configuration (RT Unified)](#transferring-the-control-configuration-rt-unified)
- [Configuring enable paging (RT Unified)](#configuring-enable-paging-rt-unified)
- [Inconsistencies and error diagnostics (RT Unified)](#inconsistencies-and-error-diagnostics-rt-unified)
- [Dynamic placeholder (RT Unified)](#dynamic-placeholder-rt-unified)
- [System alarm reporting (RT Unified)](#system-alarm-reporting-rt-unified)
- [Configuring report templates in the add-in (RT Unified)](#configuring-report-templates-in-the-add-in-rt-unified)

#### Basics (RT Unified)

This section contains information on the following topics:

- [Reporting in Runtime (RT Unified)](#reporting-in-runtime-rt-unified)
- [Basics of Reporting (RT Unified)](#basics-of-reporting-rt-unified)
- [Version compatibility (RT Unified)](#version-compatibility-rt-unified)

##### Reporting in Runtime (RT Unified)

###### Introduction

You can use WinCC Unified Reporting to generate production reports in tabular form in runtime for the following project data:

- Logging tags and tags
- Logging alarms
- Contexts:

  - User-defined contexts:

    These contexts are created and executed by a program created with the ODK API.
  - System-generated contexts

    When the Performance Insight and Calendar option packages are installed, these contexts are executed by the system during Runtime.
- Audit Trail of the Runtime device
- If Plant Intelligence options are installed, you can use the WinCC Unified Local Reporting option to generate production logs for additional project data.

  You can find more information in the Help for the respective Plant Intelligence option.

The production reports can be generated as XLSX file or PDF file and sent automatically as an email to a specified group of recipients. For example, you can generate an XLSX report that outputs all alarms occurring in a production line. You then distribute or archive the report for analysis purposes.

![Introduction](images/115612377099_DV_resource.Stream@PNG-de-DE.png)

###### Functional scope

In the "Reports" control in runtime, you configure report jobs that use the report templates defined in the Excel add-in. To do so, Reporting offers the following functions in Runtime:

- Maintenance of the global email settings (contact data and SMTP server configuration)
- Maintenance of job parameters, especially import and export of report templates
- Creating new report jobs and managing existing report jobs
- Overview of the generated reports
- Download or deletion of the reports

##### Basics of Reporting (RT Unified)

###### Report templates

A report template is an Excel file (.xslx) that was created with the WinCC Unified Excel add-in. The report template has access to the data of the data source with which the add-in is connected.

For each report template, you define which segments are contained in the reports using the template and which data source items are evaluated by the segments.

After you have imported report templates into the "Reports" control in Runtime, you can select them for configuring report jobs.

###### Data sources

The data source is the source from which you select data source items when you configure the report template.

The following connection modes and data sources are available:

- Connection mode: Online

  The data source is the project that is running on the Runtime server to which the add-in is connected.
- Connection mode: Offline

  Data source is a configuration file. You generate the configuration file by exporting the data source items of the project to a file in the "Reports" control in Runtime. You can use this file to create additional report templates without connecting to a runtime server.

###### Options and data source items

Options control the types of data source items to which the report template has access.

Data source items are the specific objects whose data is read from the Runtime project during report generation.

The following options and types of data source items are available in Reporting, depending on the installed software:

| Software | Option | Types of data source items |
| --- | --- | --- |
| WinCC Unified basic installation | Alarms | Logging alarms  Alarm statistics for logging alarms |
| WinCC Unified basic installation | Logging tag | Logging tags |
| WinCC Unified basic installation | Tag | Tags |
| WinCC Unified basic installation | User-defined column | User-defined texts or Excel formulas |
| WinCC Unified basic installation | Context | User-defined contexts<sup>1</sup> |
| WinCC Unified basic installation | Audit | Audit |
| Performance Insight option package | Performance Insight | Local KPIs and operands of the PI option Performance Insight:  - KPIs - Logged KPIs - Operands (counters and numerical operands) - Machine states - Downtime analysis - System-generated contexts |
| Line Coordination option package | Line Coordination | Jobs |
| Calendar option package | Context | System-generated contexts |
| <sup>1</sup> Only for Unified PC |  |  |

###### Report jobs and job parameters

A report job is a job for generating reports in Runtime. A new report is generated each time the report job is performed.

The job parameters of the report order determine the details of its execution, such as which trigger it has, which report template it uses and the format of the report.

Report jobs are executed automatically when their trigger event occurs or manually by the user.

###### Reports

A report (production report) is an XLSX file or PDF file that is generated when a report job is executed in Runtime. The data source items from the Runtime project defined in the report template are read during generation, and their data are imported into a table in the report.

###### Using general Excel functions

In addition to the specific add-in functions, you also have access to the standard Excel functions in a report template. These include:

- Layout functions
- Functions for graphical preparation or analysis of the data imported from Runtime, such as charts, pivot tables and formulas

See also [Tips on design and layout](#tips-on-design-and-layout-rt-unified).

##### Version compatibility (RT Unified)

###### Introduction

When loading a Runtime project for which the "Reports" control has been configured, the general rules for version compatibility of WinCC Unified apply.

The rules described here also apply for the interaction between add-in, data source, report template and runtime version of the project in which reports are generated.

###### Compatibility between add-in and data source

The add-in can use the following data sources:

| Add-in | Online data source | Offline data source |
| --- | --- | --- |
| V16 | Runtime project V16 | Configuration file generated with a Runtime project V16 |
| V17 | Runtime project V16 or V17 | Configuration file generated with a Runtime project V16 or V17 |

###### Compatibility between add-in and report template

The following report templates can be opened and edited in the add-in:

| Add-in | Report template |
| --- | --- |
| V16 | Created with a V16 add-in |
| V17 | - Created with a V17 add-in - Created with a V16 add-in   If the add-in is connected to a V17 data source when you open the report template, you will be prompted to migrate the report template to V17.    If the add-in is connected to a V16 data source when the report template is opened, no migration is necessary. |

> **Note**
>
> **Migration of report templates**
>
> The migration of the report template is not reversible. A report template migrated from V16 to V17 can no longer be opened in a V16 add-in.
>
> If migration is not desired, connect the add-in to a V16 data source before opening the report template.

> **Note**
>
> **Scope of functions of report templates**
>
> The functions available in the configuration of the report template in the add-in depend on the version of the data source used by the add-in.

###### Compatibility between report template and runtime project

In a runtime project, reports can be generated using the following report templates:

| Report template | Version of the runtime project |
| --- | --- |
| V16 | V16 and V17 |
| V17 | V17 |

#### Requirements and restrictions (RT Unified)

The following requirements and restrictions apply to configuring report jobs and generating reports on Unified PCs, both in runtime and during simulation.

##### Enable Reporting

The reporting functionality must be enabled for the Runtime project that is running or being simulated on the HMI device.

You activate the reporting functionality of a Runtime project before loading it into the device in TIA Portal: "Runtime settings" of the HMI device > "Reporting" > "Enable Reporting" option

> **Note**
>
> **Devices with a device version lower than V18**
>
> Reporting is always enabled for HMI devices with a device version lower than V18.

#### Workflow for working with reports in Runtime (RT Unified)

##### Introduction

The following workflow describes which works are required in the "Reports" control so that production reports are generated in Runtime.

The reports can be stored as file in the file system and sent as an attachment to an e-mail. Alternatively, an e-mail without attachment can also be sent about the generation of the report. In this way, employees from management and production are promptly informed about the production situation, regardless of their location.

You can send the e-mail using a secure SMTP server (authentication with user name and password or via certificate) or an unsecured SMTP server, for example, an internal company mail server.

##### Requirement

- Requirements in TIA Portal:

  - The necessary project data were configured for the HMI device for which reports are to be created.
  - The "Reports" control was placed on an HMI screen of the device.
  - The "Enable Reporting" option was enabled in the Runtime settings of the device.
  - (Optional) The storage locations for reports and the Reporting database were configured in the Runtime settings of the device.
- The HMI device has been compiled, loaded into Runtime and its Runtime project has the status "Running".
- The HMI device has access to report templates.
- Unified PC: If one of the report templates used in Runtime evaluates contexts, contexts must have been configured for the currently running Runtime project and executed in Runtime.
- For cross-project and cross-Runtime use of report templates: The data sources used in the report template can also be found on the HMI device. Make sure that the names and plant hierarchy are consistent.

##### Procedure

1. To send reports by e-mail, configure the global e-mail settings:

   - When one of the servers requires a certificate for sending e-mails, upload the certificate.
   - Create contacts for the e-mail receivers and e-mail senders.
   - Create the required SMTP server configurations.
2. Configure job parameters for report templates, triggers and targets.

   These job parameters will then be available to you for selection when configuring the report jobs.
3. Configure report jobs.

   Reports are generated in Runtime when the report jobs are executed.
4. (Optional) Perform report orders manually.
5. In the control, get an overview of which reports have been generated.
6. Download the reports, if necessary.
7. (Optional) To reuse the configuration of the "Reports" control, such as on a device in another network, transfer the existing configuration from the control from one device to the control of the other device.

##### Configuring job parameters

First, you configure which job parameters are available for selection during the configuration of the report jobs. You configure the following job parameters:

- The available report templates

  The report template defines which data the report outputs. Import and/or delete templates, if required.
- The available triggers

  The trigger defines when a report job is executed. Add triggers, edit triggers or delete them.
- The available targets

  Targets define whether reports are made available to users in the file system or via e-mails. Add targets, edit triggers, or delete them.

You set further job parameters while configuring a report job in the "Report jobs" tab.

##### Configuring a report job

You configure the following for each report job:

- Name of the report job
- Used report template
- Name of the reports generated by this template

  > **Note**
  >
  > **Texts through dynamic placeholders**
  >
  > Placeholders are available to you when defining the report name. The placeholders are evaluated and replaced by text during execution of the report.
  >
  > See also [Dynamic placeholder](#dynamic-placeholder-rt-unified).
- Targets of the generated report

  To send e-mails, select a target of the type "E-mail".
- Per target: The target format of the generated report

  Possible formats: .XLSX and .PDF
- Trigger
- Comment
- Activate

---

**See also**

[Setting global email settings (RT Unified)](#setting-global-email-settings-rt-unified)
  
[Configuring job parameters (RT Unified)](#configuring-job-parameters-rt-unified)
  
[Configuring report jobs (RT Unified)](#configuring-report-jobs-rt-unified)
  
[Running a report job manually (RT Unified)](#running-a-report-job-manually-rt-unified)
  
[Downloading reports (RT Unified)](#downloading-reports-rt-unified)
  
[Transferring the control configuration (RT Unified)](#transferring-the-control-configuration-rt-unified)
  
[Configuring report templates in the add-in (RT Unified)](#configuring-report-templates-in-the-add-in-rt-unified)

#### The user interface of the "Reports" control (RT Unified)

> **Note**
>
> **Automatic data transfer**
>
> Changes in the "Reports" control are saved automatically.

##### Layout

You create and manage report jobs in the "Reports" control. You also have access to the reports generated by the report jobs.

The control has the following structure:

![Layout](images/158985390731_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| 1 | Tab for the configuration and management of reports, report jobs, job parameters and global settings |
| 2 | Toolbar  The buttons you see depend on the tab. |
| 3 | Work area   On the "Reports", "Report jobs" and "Job parameters" tabs: List of elements available on the tab  On the "Global settings" tab: The settings |
| 4 | Options for selecting the elements  You can select elements individually or all at once. |
| 5 | Detail area  Shows the properties of the selected element. |
| 6 | Information bar |

##### Tab

**"Reports" tab**

Here you can see which reports have been generated. You can download or delete reports via the toolbar.

The "Status" column shows Information:

- On the status of the generated report files (XLSX and PDF)
- On the status of the targets (File system and E-mail)

Overview of the status icons:

| Status | Description |
| --- | --- |
| ![Tab](images/136004352139_DV_resource.Stream@PNG-de-DE.png) | Execution has been successfully completed. |
| ![Tab](images/136004343563_DV_resource.Stream@PNG-de-DE.png) | An error occurred during execution. |
| ![Tab](images/136004437771_DV_resource.Stream@PNG-de-DE.png) | Execution is in progress. |

A click on an icon opens a detailed status message.

**"Report jobs" tab**

Here you create new report jobs, manage existing report jobs or start a report job manually.

**"Job parameters" tab**

Here you manage the parameters with which you configure the report jobs in the "Report jobs" tab.

**"Global settings" tab**

Here you make the following settings:

- For sending e-mails
- For transfer of the control configuration
- For creating an offline configuration file
- For configuring paging

##### Toolbar

The following buttons are available in the toolbars of the tab:

| Icon | Button |  |
| --- | --- | --- |
| ![Toolbar](images/129288141323_DV_resource.Stream@PNG-de-DE.png) | Delete | Deletes the elements whose option is enabled in the work area. |
| ![Toolbar](images/129286967947_DV_resource.Stream@PNG-de-DE.png) | - Add new - Import | - Creates a new element. - "Job parameters > Templates" tab: To import a report template into Runtime |
| ![Toolbar](images/129288760331_DV_resource.Stream@PNG-de-DE.png) | Run | In the "Report jobs" tab.  Manually creates a report for the report job whose option is enabled in the work area. |
| ![Toolbar](images/129288150155_DV_resource.Stream@PNG-de-DE.png) | Export | - In the "Job parameters > Templates" tab: To export report templates - In the "Reports" tab:  To download reports to the client |

##### Information bar

The button in the information bar displays general information sent by the reporting service, for example, on whether a report job has been executed.

#### Setting global email settings (RT Unified)

This section contains information on the following topics:

- [Setting global email settings (RT Unified)](#setting-global-email-settings-rt-unified-1)
- [Upload certificates (RT Unified)](#upload-certificates-rt-unified)
- [Maintaining contacts (RT Unified)](#maintaining-contacts-rt-unified)
- [Maintenance of the SMTP server configuration (RT Unified)](#maintenance-of-the-smtp-server-configuration-rt-unified)

##### Setting global email settings (RT Unified)

If configured accordingly, an e-mail is sent automatically after a report job is executed. The e-mail can include the report as an attachment.

Maintenance of the basic settings for sending e-mails is carried out in the "Global settings" tab:

- If necessary: The certificates that the e-mail sender uses to authenticate itself at the SMTP servers.
- The contact information of the e-mail senders and e-mail receivers.
- The configuration of the SMTP server via which the e-mails are sent.

##### Upload certificates (RT Unified)

Store the certificates of the SMTP servers that require authentication via certificate.

###### Requirement

- You have access to the storage location of a valid certificate file.

###### Procedure

1. In the "Reports" control, click on the "Global settings > Certificates" tab.
2. Click "Add new" in the toolbar.

   Alternative: In the work area, click "Add new".
3. In the dialog that opens, select the certificate file.
4. Confirm your input.
5. Optional: Select the uploaded certificate in the work area and enter a comment on the certificate in the detail area.

###### Result

The certificates uploaded here are available in the "Contacts" tab.

##### Maintaining contacts (RT Unified)

Store the data of the e-mail senders and email recipients.

###### Procedure

To create a new contact, follow these steps:

1. In the "Reports" control, click on the "Global settings > Contacts" tab.
2. Click "Add new".
3. Enter the name of the contact.
4. Enter the e-mail address of the contact.
5. To use the contact as a sender for an SMTP server that requires authentication with a certificate, select the appropriate certificate under "Certificate".
6. To use the contact as a sender for an SMTP server that requires authentication with a user name and password, enter the password.

   The e-mail address is used as the user name.
7. (Optional) Enter a comment relating to the contact.

###### Result

The contacts configured here are available:

- As the e-mail sender in the SMTP server configuration.
- As an e-mail recipient when configuring "target" job parameters with the target type e-mail

##### Maintenance of the SMTP server configuration (RT Unified)

Store the data of the SMTP servers via which the e-mails are sent.

###### Requirement

Contacts that are suitable as senders have been entered in the "Global Settings > Contacts" tab.

###### Procedure

To create a new SMTP server configuration, follow these steps:

| 1. In the "Reports" control, click on the "Global settings > SMTP" tab. 2. Click "Add new". 3. Specify the following:       | Field | Description |    | --- | --- |    | "Name" | Enter the name of the SMTP server configuration. |    | "Address" | Enter the URL of the SMTP server. Servers without authentication (e.g. company-internal mail servers) and with authentication are permitted. Example: URL of a company mail server: `mail.<``Company name``>.com` |    | "Port" | Enter the port number of the SMTP server. Default setting: 25 |    | "Sender" | In the list, select the contact that is used as the sender for this SMTP server configuration.  All contacts maintained under "Contacts" are offered to you for selection. Select a sender that meets the respective requirements of the server. |    | "Comment" | (Optional) Enter a comment relating to the SMTP server configuration. | |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

###### Result

The servers configured here are available when configuring the "Target" job parameters with the target type email.

#### Configuring job parameters (RT Unified)

This section contains information on the following topics:

- [Configuring job parameters (RT Unified)](#configuring-job-parameters-rt-unified-1)
- [Importing and exporting report templates (RT Unified)](#importing-and-exporting-report-templates-rt-unified)
- [Deleting templates (RT Unified)](#deleting-templates-rt-unified)
- [Configure trigger (RT Unified)](#configure-trigger-rt-unified)
- [Add target with target type "E-mail" (RT Unified)](#add-target-with-target-type-e-mail-rt-unified)
- [Add a target with "File system" target type (Unified PC) (RT Unified)](#add-a-target-with-file-system-target-type-unified-pc-rt-unified)

##### Configuring job parameters (RT Unified)

Job parameters define the details of a report job.

You configure the following parameters on the "Job parameters" tab:

- Templates
- Trigger

  Define trigger when a report job is executed.
- Targets

  Targets define how a report is made available to users. The following target types are available:

  - "E-mail"

    An e-mail is sent after a report job is executed. The report generated by the report job can be included with the e-mail as an attachment.
  - "File system"

    The reports generated by the report job are stored in the file system.

The parameters configured here are available to you for selection when configuring the report jobs in the "Report jobs" tab.

You define the remaining job parameters while configuring a report job in the "Report jobs" tab.

---

**See also**

[Importing and exporting report templates (RT Unified)](#importing-and-exporting-report-templates-rt-unified)
  
[Deleting templates (RT Unified)](#deleting-templates-rt-unified)
  
[Configure trigger (RT Unified)](#configure-trigger-rt-unified)
  
[Add target with target type "E-mail" (RT Unified)](#add-target-with-target-type-e-mail-rt-unified)

##### Importing and exporting report templates (RT Unified)

###### Requirement

- The "Reports" control is placed on a screen of the project.
- The "Job parameters > Templates" tab is visible in the control.
- Import: You have access to the storage location of the report template.
- Export: Report templates have been imported into the control.

###### Importing report template

1. Click "Add new" in the toolbar.

   Alternative: In the work area, click "Add new".
2. In the dialog that opens, select the file of a report template.
3. Confirm your input.
4. Optional: In the work area, select the imported report template in the work area and enter a comment describing the template in the detail area.

**Note**

**No validation**

The template is not validated during import.

###### Exporting report templates

1. In the work area, select the options next to the report templates you want to export.
2. Click "Export" in the toolbar.

The report templates are downloaded to the download folder or a user-defined directory according to the device settings.

##### Deleting templates (RT Unified)

###### Requirement

- The "Reports" control is placed on a screen of the project.
- The "Job parameters > Templates" tab is visible in the control.
- Templates have been imported into the control.

###### Procedure

1. In the work area, select the options next to the templates you want to delete.
2. Click "Delete" in the toolbar.

**Deleting used templates**

The "In use" column shows whether the template is used by a report job.

If you delete a template that is used by a report job, the report job is marked as inconsistent and no longer executed.

##### Configure trigger (RT Unified)

###### Introduction

In the "Job Parameters > Triggers" tab you configure which automatic triggers are available for selection when configuring report jobs.

Report jobs with automatic triggers are executed if the report jobs on the "Report jobs" tab are set to active and their trigger event occurs. Users can also start the execution manually.

###### Requirement

- The "Reports" control is placed on a screen of the project.
- The "Job parameters > Trigger" tab is visible in the control.
- To use the trigger type "Context trigger": Contexts are available in the project.

###### Add trigger

| 1. In the work area of the tab, click "Add new".    A new trigger is created and displayed in the detail area. 2. Assign a unique name to the trigger. 3. Select the trigger mode:        | Trigger type | Triggering the trigger |    | --- | --- |    | "Tag trigger" | Automatically when the configured value condition occurs at the tag defined in the trigger. |    | "Serial trigger" | Automatically within the user-defined interval when the time defined by the series has been reached. |    | "Context trigger" | Automatically when the selected context is started or stopped. Optional: By using a condition, you can also limit the triggering of the trigger to specific context values. | 4. Depending on the selected trigger type, set the settings for the new trigger as described below. 5. Optional: Enter a comment for the trigger. |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

###### Settings for tag trigger

| Symbol | Meaning |
| --- | --- |
| 1. Click "Select tag". 2. Click "Load". 3. Select the required tag and click "OK". 4. Set the condition and the condition value.    Example:        | Symbol | Meaning |    | --- | --- |    | Set tag | <tag name> |    | Condition | > |    | Condition value | 100 |     The trigger will be initiated when the tag receives a value greater than 100. |  |

###### Settings for serial triggers

| Symbol | Meaning |
| --- | --- |
| 1. Select the serial pattern.    The series pattern defines the occurrence and time at which the trigger is initiated.    Example: Weekly > Every 2 weeks > Fridays 2. Select the series area.    The series range defines the period in which the trigger is initiated.       | Symbol | Meaning |    | --- | --- |    | "Start" | Specify the start date |    | "Time" | Specify the time at which the trigger is initiated. |    | "End on" | Specify the end date. The trigger will be executed for the last time on this day. |    | "End after" | Determine the number of dates after which the series ends. |    | "No end date" | The series runs indefinitely. | |  |

###### Settings for context triggers

| Symbol | Meaning |
| --- | --- |
| 1. Click "Select context". 2. In the "Context selection" dialog, click "Select plant object". 3. In the "Browser view" dialog, select a plant object and confirm your input.    In the "Context selection" dialog you can see all contexts that have been defined for the selected plant object. 4. Select a context and confirm your input. 5. Under "Context status", select when the trigger will be triggered:       | Symbol | Meaning |    | --- | --- |    | "Started" | When starting the context. |    | "Stopped" | When stopping the context. | 6. Optional: To bind the execution of the report order to certain context values, you define a condition:       | Symbol | Meaning |    | --- | --- |    | "Condition" | Select an operator. |    | "Value" | Select a context value. |     Example:       | Symbol | Meaning |    | --- | --- |    | Plant object | "MyPlant.hierarchy::PlantView/Bottling" |    | Context | "Product" |    | Context state | "Started" |    | Condition | = |    | Value | "Orange lemonade" |     Report jobs with this trigger are always executed when the context "Product" defined on the plant object "Bottling" is started with the value "Orange lemonade". |  |

###### Delete trigger

Select the option of the desired trigger in the work area of the "Job Parameters > Triggers" tab and click "Delete" in the toolbar.

###### Edit trigger

1. Enable the option of the desired trigger in the work area of the tab.
2. In the detail area, edit the settings of the trigger.

**Note**

**No change of the trigger type**

The trigger type can only be set when adding the trigger.

##### Add target with target type "E-mail" (RT Unified)

###### Requirement

- The "Reports" control is placed on a screen of the project.
- The receivers of the e-mails are maintained as contacts in the "Global settings > Contacts" tab.
- An SMTP server, with which the e-mail is to be sent, has been configured in the "Global settings > SMTP" tab.

###### Procedure

1. In the "Reports" control, click on the "Job parameters > Targets" tab.
2. In the work area of the tab, click "Add new".
3. Select "E-mail" as target type.

   A new target is created and displayed in the detail area.
4. Assign a unique name to the target.
5. Select an SMTP server configuration.
6. Add the desired receivers and CC receivers:

   - To do so, select a contact from the list "Add receiver" or "Add CC receiver".
   - Add the contact by clicking "+".
7. Enter the e-mail subject.

   To integrate the report name into the subject line, use the placeholder {ReportName}.
8. Enter the e-mail text.

   To integrate the report name into the email text, use the placeholder {ReportName}.
9. (Optional) Enter a comment.

###### Result

The target is available for selection when configuring report jobs.

An e-mail is sent after a report job is executed with this target. The e-mail can include the report as attachment.

---

**See also**

[Dynamic placeholder (RT Unified)](#dynamic-placeholder-rt-unified)

##### Add a target with "File system" target type (Unified PC) (RT Unified)

This section describes how to add a target with the "File system" target type on a Unified PC in Runtime.

###### Introduction

A reporting job with a target of the "File system" target type saves reports to a file system.

When configuring the report jobs, you can choose from pre-configured and user-defined targets of this target type.

**Preconfigured targets**

The following targets with "File system" target type are pre-configured:

| Symbol | Meaning |
| --- | --- |
| Local project storage location | The reports are stored in the following folder: `<Project folder of the Runtime project>\``Reports` |
| Local main storage location | The reports are stored in the local main storage location for reports. The local main storage location is configured in TIA Portal in the Runtime settings of the HMI device.  If this setting has not been set in TIA Portal, the reports are stored in the folder configured during the installation of Runtime or later in the "WinCC Unified Configuration" tool: |

You can select these targets in the "Report jobs" tab. You cannot edit or delete these targets in the "Job parameters > Targets" tab.

**User-defined targets**

In the "Reports" control, you can create user-defined targets of the "File system" target type. These user-defined targets are always subfolders of the local main storage location.

###### Requirement

- The "Reports" control is placed on a process picture.

###### Procedure

To add user-defined targets of the "File system" target type, follow these steps:

1. In the "Reports" control, click on the "Job parameters > Targets" tab.
2. In the work area of the tab, click "Add new".
3. Select "File system" as target type.

   A new target is created and displayed in the detail area.

   Under "Destination path", you can see the path to the local main storage location for reports.
4. Assign a unique name to the target.
5. Under "Subfolder", enter the path to the subfolder in which the report is to be saved.

   Use the following notation: <folder name> or <folder name>\<folder name>\...
6. (Optional) Enter a comment.

**Note**

**Relative path information**

The path specification is relative to the local main storage location for reports.

###### Result

The target is available for selection when configuring report jobs.

When a report job with this target is being executed, the generated report is stored in the subfolder of the local main storage location defined as the target. If the folder entered under "Target path" does not exist, it is created by the system.

> **Note**
>
> **Change of the local main storage location for reports**
>
> When the local main storage location for reports changes, the targets are automatically adapted. New reports are stored relative to the new local main storage location. The old folders are not deleted.

#### Configuring report jobs (RT Unified)

This section contains information on the following topics:

- [Creating a report job (RT Unified)](#creating-a-report-job-rt-unified)
- [Managing report jobs (RT Unified)](#managing-report-jobs-rt-unified)
- [Configuring report names (RT Unified)](#configuring-report-names-rt-unified)
- [Execution of report jobs (RT Unified)](#execution-of-report-jobs-rt-unified)

##### Creating a report job (RT Unified)

###### Introduction

A report job is a job for generating reports in Runtime. The configuration of a report job controls the details of the generation.

###### Requirement

- The "Reports" control is configured on a screen of the project.
- The following job parameters were configured in the control:

  - At least one template has been imported.
  - To automatically execute a report job: Triggers are configured in the "Job parameters > Trigger" tab.
- For sending an email after execution of the report job:

  - Email contacts were configured in the global settings.
  - An SMTP server was configured in the global settings.
  - A target of the target type "E-mail" was configured in the "Job parameters > Targets" tab.
- For a report job with the target format PDF:

  - Microsoft Office Excel or LibreOffice is installed on the runtime server.
  - Depending on whether Excel or LibreOffice is installed, the information required for PDF creation was provided during the Runtime installation or in the "WinCC Unified Configuration" tool.

###### Procedure

1. Select the "Report jobs" tab in the "Reports" control.
2. Select "Add new" in the work area or click "Add new" in the toolbar.
3. In the detail area, enter a name for the report job.
4. Select a report template.
5. Configure the report name. See section [Configuring report names](#configuring-report-names-rt-unified).

   The configuration is applied to all reports generated by the report job.
6. Under "Targets", you determine how the reports are to be made available to users. Follow these steps:

   - Click "Add target".

     You see the targets configured in the tab "Job parameters > Targets".
   - Select a target.
   - Add the target by clicking "+".

     The target is added to the table to define the target formats.

     ![Procedure](images/134910569739_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/134910569739_DV_resource.Stream@PNG-en-US.png)
   - Determine the formats in which the reports generated by the report job are provided for the target. In the table, activate the options of the desired formats for each target.
   - To remove a target from the report job, click the "Remove" button in the table.
7. Under "Trigger", select which event triggers the execution of the report job:

   - If the report job is only to be executed manually, select "Manual".
   - If the report job is to be executed automatically, select one of the other triggers configured under "Trigger".
8. (Optional) Enter a comment for the report job.
9. Specify whether the automatic execution of the report job is active or paused. To do this, set the slider "Enabled" or "Disabled".

**Note**

**Sending emails without a report**

If you deactivate both options for targets with "E-mail" target type, an email without attachment is sent after the report job has been executed.

**Note**

**PDF as target type**

Generating PDFs with Excel is significantly slower than with LibreOffice. To generate large PDF reports, it is therefore recommended that you install LibreOffice.

A PDF report created by LibreOffice can deviate in content or layout from a PDF report generated with Excel, for example, if the report template uses common Excel features that LibreOffice does not support, such as special fonts or chart types.

**Note**

You can also execute the report job manually.

**Note**

You can still execute disabled report jobs manually.

###### Result

The report job is saved automatically.

When its trigger occurs, the report job is executed. A report is generated and made available as configured under "Targets".

---

**See also**

[Execution of report jobs (RT Unified)](#execution-of-report-jobs-rt-unified)
  
[Configure trigger (RT Unified)](#configure-trigger-rt-unified)
  
[Add a target with "File system" target type (Unified PC) (RT Unified)](#add-a-target-with-file-system-target-type-unified-pc-rt-unified)
  
[Add target with target type "E-mail" (RT Unified)](#add-target-with-target-type-e-mail-rt-unified)
  
[Tips on design and layout (RT Unified)](#tips-on-design-and-layout-rt-unified)

##### Managing report jobs (RT Unified)

###### Requirement

- The "Reports" control is configured on a screen of the project.
- Report jobs have been configured in the control.

###### Procedure

1. Select the "Report jobs" tab in the "Reports" control.
2. To edit a report job, proceed as follows:

   - Select the report job in the work area.
   - In the detail area, edit the settings of the report job.

     You have the same options as when creating a report job.
3. To delete report jobs, proceed as follows:

   - In the work area, enable the options next to the report job.
   - Click "Delete" in the toolbar.

##### Configuring report names (RT Unified)

> **Note**
>
> Make sure that the generated report name does not violate the policy of the operating system regarding the maximum length of file names.

###### Introduction

The default name of reports is `Report_{NNN}`.

To use different report names, enter one or more placeholders at the report job. The placeholders are combined to form the report name during execution of the report.

**Placeholder types**

Placeholders have one of the following types:

| Placeholder type | Description |  |
| --- | --- | --- |
| Text | For user-defined fixed texts |  |
| Counter | On automatic numbering | Dynamic placeholders  The placeholders are broken down into values during execution of the report. |
| Date format | For outputting the generation time |  |
| Tag | To output the process value of an online tag |  |

**Unique report names**

If the report name uses counter or date format placeholders, the report job generates unique report names.

###### Requirement

- The "Reports" control contains a screen of the runtime project that is running.

###### Procedure

You can enter the placeholders manually in the "Report name" field or you can have the software help you configure the report name.

To have the software help configure the report name, follow these steps:

|  |  |  |
| --- | --- | --- |
| 1. Select the "Report jobs" tab in the "Reports" control. 2. Select a report job in the work area.    You can see the settings for the report job in the detail area. 3. Next to "Report name", click "Configure".    You see the following operator controls:               ![Procedure](images/148826369803_DV_resource.Stream@PNG-en-US.png)         ![Procedure](images/148826369803_DV_resource.Stream@PNG-en-US.png)        |  |  |  |    | --- | --- | --- |    | ① | List for selection of the placeholder type |  |    | ② | Button for adding a placeholder of the selected type |  |    | ③ | Table for configuring or removing the placeholder |  |       |  |  |  |    | --- | --- | --- |    | **Note**  For the default report name, the "Report name" has the value `Report_{NNN}` and the table shows the placeholders "`Report_`" and "`NNN`". To swap the order of placeholders or to add a placeholder in the center, delete the placeholders and then add them in the desired order. |  |  | 4. Optional: To delete the default placeholders, click "x" in the placeholder table. 5. Select the desired type under "Select placeholder type".      |  |  |  |    | --- | --- | --- |    | **Note**  A report name can contain only one counter. |  |  | 6. Click "+".    An empty placeholder of the corresponding type is added at the end of the table. 7. Enter the placeholder under "Value" in the placeholder table.       | Placeholder type | Description | Example |    | --- | --- | --- |    | "Text" | Enter the text. | `Report_` |    | "Date format" | Enter a date placeholder. | A list of permitted placeholders and examples can be found in section [Dynamic placeholder](#dynamic-placeholder-rt-unified). |    | "Counter" | Enter a counter placeholder. |  |    | "Tag" | Enter the full name of an online tag. | `RT1_Brewery::BatchNo` |       |  |  |  |    | --- | --- | --- |    | **Note**  Enter the dynamic placeholders without any markup characters. |  |  |     Alternatively, you can select an online tag via the user interface. Follow these steps:    - Click the "..." button on the tag placeholder.    - In the "Tag selection" dialog, click the "Search" button.      You can see all the tags of the Runtime project that is running.        |  |  |  |      | --- | --- | --- |      | **Note**   **Scrolling and filtering**  Use the page navigation buttons to scroll forward or backward. To filter the displayed tags, enter a filter string in "Filter" and click "Search". You use the wildcard "*" to filter by partial strings. ​For example: - *T* returns all tags with a "T" in their name. - *T returns all tags that end in "T". - T* returns all tags that start with "T".​When filtering for structures, the separators must be part of the filter string. |  |  |                 ![Procedure](images/149794338187_DV_resource.Stream@PNG-en-US.png)           ![Procedure](images/149794338187_DV_resource.Stream@PNG-en-US.png)    - Click the desired tag.    - Confirm with "OK". |  |  |

In the "Report name" field, the placeholder you added is appended to the end of the report name.

###### Alternative procedure

To enter the placeholders manually, proceed as follows:

1. Select the "Report jobs" tab in the "Reports" control.
2. Select a report job in the work area.

   You can see the settings for the report job in the detail area.
3. Enter the desired combination of fixed texts and dynamic placeholders manually in the "Report name" field.

   Use markup characters for the dynamic placeholders. See section [Dynamic placeholder](#dynamic-placeholder-rt-unified).

Example:

| "Report name" value | Generated report name |
| --- | --- |
| `Report_{yyyymmdd}_{HHMMss}_{@PC1_Brewery::BatchNo}` | `Report_20190101_170001_BatchNo_87002314` |

###### Result

When generating a report, the dynamic placeholders are resolved and all placeholders are merged to form the report name.

If a process value contains a character that is not permitted in file names, it is replaced by an underscore.

If there is an error resolving the name, e.g. because the tag is not found in runtime, the tag placeholder in the name is replaced by `ERR`. The process is logged in the generation status of the report.

##### Execution of report jobs (RT Unified)

###### Automatic and manual execution

**Automatic execution**

Report jobs that have a tag trigger, serial trigger or context trigger and are set to active on the "Report jobs" tab are automatically executed when their trigger occurs.

**Manual execution**

Report jobs with a trigger of the "Manual" type must always be executed manually.

In addition, you can at any time manually execute report jobs that have a tag trigger, serial trigger or context trigger.

###### System response to errors

- Error adding the report job to the queue

  The execution of the report job is discarded. A system alarm documents the error.
- Error executing the job

  In the "Reports" control, "Reports" tab, the status icon indicates the error. A click on the icon opens a detailed status message.

  A system alarm documents the error.

---

**See also**

[Running a report job manually (RT Unified)](#running-a-report-job-manually-rt-unified)
  
[Configure trigger (RT Unified)](#configure-trigger-rt-unified)

#### Running a report job manually (RT Unified)

You can execute report jobs manually at any time, regardless of their trigger type. This also applies to report jobs that were disabled in the "Report Jobs" tab and whose automatic execution is therefore paused.

##### Requirement

Report jobs have been configured in the "Reports" control.

##### Procedure

1. Select the "Report jobs" tab in the "Reports" control.
2. In the work area, enable the option next to the report job that you want to execute manually.
3. Click "Execute" in the toolbar.

##### Result

The report is generated. You can download it in the "Reports" tab.

#### Downloading reports (RT Unified)

You can download the reports stored by the report job in the file system to your device.

Depending on which file formats have been set in the report job, you can download the report as an XLSX file and as a PDF file.

##### Requirement

- Report jobs with the target type "File system" have been configured and executed in the "Reports" control.

##### Procedure

1. Select the "Reports" tab in the "Reports" control.
2. In the work area, select the option in the left column for each report that you want to download.
3. Enable the desired target formats in the "Files" column.
4. Click "Export" in the toolbar.

**Note**

**Generation status**

You are only offered successfully generated formats.

In the "Status" column you can check whether the generation for a format has failed. For a detailed status message click on the icon of a target format.

##### Result

The reports are downloaded into the download directory of the browser.

You can edit, distribute, or log the reports.

---

**See also**

[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)

#### Exporting an offline configuration file (RT Unified)

An offline configuration file is required to configure reporting templates in the Reporting Excel add-in without an online connection to the Runtime server.

##### Requirement

- The "Reports" control is placed on a screen of the project.
- The Runtime project has data that can serve as data source elements in the reporting template, such as alarms and logging tags.

##### Procedure

1. In the "Reports" control, click on the "Global settings > Configuration" tab.
2. Enter the name of the offline configuration file under "Offline-configuration".
3. Click "Export offline configuration".

##### Result

A JSON file with the data source elements of the Runtime project is created. The file is downloaded to the download folder or a user-defined directory according to the device settings.

You can select the configuration file in the Reporting Excel add-in as data source for an offline connection.

#### Transferring the control configuration (RT Unified)

You have the option of reusing the settings in the "Reports" control, for example, on a device in another network. To do this, export the existing configuration on the one device from the control to a ZIP file. Then import the file into a "Reports" control on the other device.

##### Scope

The transfer covers the following data:

- Global settings, without passwords and certificates
- Job parameters, including the report templates available in the control
- Report jobs

Reports are not transferred.

##### Requirement

- The "Reports" control is placed on a screen in the project running in Runtime.
- Export: Settings have been made, e.g. contacts maintained, report templates imported, and report jobs created in the "Reports" control.
- Import: You have access to the ZIP file generated by the export on the device on which Runtime is installed.

##### Export configuration

1. In the "Reports" control, select the "Global settings > Configuration" tab.
2. Enter the name of the export file under "Export/import configuration > Export".
3. Click "Export configuration".

The configuration is exported to a ZIP file and downloaded to the default download directory of the device.

##### Import configuration

1. In the "Reports" control, select the "Global settings > Configuration" tab.
2. Click "Select import file" under "Export/import configuration".
3. Select the ZIP file in File Explorer and confirm your selection.
4. Runtime checks whether the control already contains configurations:

   - No: The configuration is imported.
   - Yes:

     Select "OK" to import the configuration. The existing configuration is overwritten.

     Select "Cancel" to cancel the import.

#### Configuring enable paging (RT Unified)

To set how many entries the lists in the work area of the "Reports" control display per page, follow these steps:

1. In the "Reports" control, click on the "Global settings > Configuration" tab.
2. Under "List Settings", select the number of entries.

If a list has more entries, these are split over several pages. Use the buttons below the list to switch pages.

> **Note**
>
> The setting is lost through a screen change.

#### Inconsistencies and error diagnostics (RT Unified)

> **Note**
>
> Inconsistent report jobs are not executed.
>
> The templates available in the "Reports" control are not validated.

##### Display of inconsistencies and errors

Errors and inconsistencies are displayed as follows:

| Symbol | Meaning |
| --- | --- |
| In the control | If job parameters are affected.  Examples:  - No template is set for a report job. - A tag that triggers a report job is deleted in the engineering system. The project is reloaded into the device. |
| In the "Error log" worksheet of the report | Errors or inconsistencies affecting the content of the report.  Example: The report evaluates data from a tag that is no longer available in runtime. |
| As system alarm | For errors and inconsistencies that do not affect job parameters or the contents of the report.  Example: The ExecuteReport system function transfers a report job that does not exist. |

##### Job parameters

The following values lead to errors and inconsistencies:

| Parameter | Invalid values | Default setting |
| --- | --- | --- |
| "Name" | Zero, empty or already assigned name | "New report job" |
| "Template" | Zero, empty or "None".  Name of a template that is not imported | "None" |
| "Target name" | Zero or empty | "NewReportJob[NN]" |

#### Dynamic placeholder (RT Unified)

##### Introduction

Dynamic placeholders are evaluated when the report job is executed and replaced with text in runtime.

The following job parameters can contain placeholders:

- Report name
- Targets with the target type "E-mail": Subject and text of the email

##### Dynamic placeholders for report names

Use dynamic placeholders for counters and/or dates to generate unique report names:

| Counter placeholder | Description | Example |  | Area |
| --- | --- | --- | --- | --- |
| Configuration | Result |  |  |  |
| {N} | Automatic numbering | Rep_{N} | Rep_1 | 0...9 |
| {NN} | Rep_{NN} | Rep_01 | 00...99 |  |
| {NNN} | Rep_{NNN} | Rep_001 | 000...999 |  |

| Date placeholder | Description | Example |  | Area |
| --- | --- | --- | --- | --- |
| Configuration | Result |  |  |  |
| {yy} | Current year | Rep_{yy} | Rep_18 | Valid year with 2 digits |
| {yyyy} | Rep_{yyyy} | Rep_2018 | Valid year with 4 digits |  |
| {m} | Current month | Rep_{m} | Rep_1 | Valid month, no prefixed 0 for months in single-digit range |
| {mm} | Rep_{mm} | Rep_01 | Valid month, prefixed 0 for months in single-digit range |  |
| {mmm} | Rep_{mm} | Rep_Jan | Month abbreviation with 3 characters |  |
| {mmmm} | Rep_{mmmm} | Rep_January | Month with full name |  |
| {d} | Current day of the month | Rep_{d} | Rep_1 | Valid day, no prefixed 0 for days in single-digit range |
| {dd} | Rep_{dd} | Rep_01 | Valid day, prefixed 0 for days in single-digit range |  |
| {ddd} | Rep_{ddd} | Rep_Mon | Day abbreviation with 3 characters |  |
| {dddd} | Rep_{dddd} | Rep_Monday | Day with full name |  |
| {h} | Current hour | Rep_{h} | Rep_1 | Current hour (12-hour clock), no prefixed 0 for single-digit values |
| {hh} | Rep_{hh} | Rep_01 | Current hour (12-hour clock), prefixed by 0 for single-digit values |  |
| {H} | Rep_{H} | Rep_13 | Current hour (24-hour clock), no prefixed 0 for single-digit values |  |
| {HH} | Rep_{HH} | Rep_13 | Current hour (24-hour clock), prefixed by 0 for single-digit values |  |
| {M} | Current minute | Rep_{M} | Rep_6 | Valid minute, no prefixed 0 for single-digit values |
| {MM} | Rep_{MM} | Rep_06 | Valid minute, prefixed by 0 for single-digit values |  |
| {s} | Current second | Rep_{s} | Rep_41 | Valid second, no prefixed 0 for single-digit values |
| {ss} | Rep_{ss} | Rep_41 | Valid second, prefixed by 0 for single-digit values |  |

Use a dynamic placeholder for tags to integrate process values in the report name:

| Tag placeholder | Description | Example |  | Area |
| --- | --- | --- | --- | --- |
| Configuration | Result |  |  |  |
| {@<Full  Tag name>} | Process value of an online tag | Rep_{@PC1_LineA::MyTag1} | Rep_On | Process value of the online tags  If the value contains a character that is not permitted in file names, it is replaced by an underscore.  If there is an error resolving the name, e.g. because the tag is not found in runtime, the tag placeholder in the name is replaced by `ERR`. The process is logged in the generation status of the report. |

Examples:

| Definition with placeholder | Generated report name |
| --- | --- |
| LineA_{yyyymmdd}_{HHMMss} | LineA_20190101_170001 |
| LineA_{yymmmd}_{hhMMss} | LineA_19Jan1_050001 |
| LineA_{NNN} | LineA_014 |
| LineA_{yyyymmdd}_{HHMMss}_BatchNo_{@PC1_Brewery::BatchNo} | LineA_20190101_170001_BatchNo_87002314 |

##### Placeholder for email subject and email text

To integrate the report name into the subject line or the email text, use the following dynamic placeholder {ReportName}.

##### Markup

Use the following markup characters for dynamic placeholders:

- Placeholders for counter and date: `{}`
- Placeholders for tags: `{@}`

> **Note**
>
> There is no markup in the placeholder table for defining the report name. See also section [Configuring report names](#configuring-report-names-rt-unified).

#### System alarm reporting (RT Unified)

##### System alarm reporting

The following is the list of the most important system alarms.

| ID | Alarm text | Effect/causes | Solution |
| --- | --- | --- | --- |
| 538640385 | Initialization of the reporting service failed | Initialization of the reporting service fails. | Contact Siemens customer service. |
| 538640386 | Report Data Provider cannot be started | The data provider for reports could not be started. | Contact Siemens customer service. |
| 538640387 | The report cannot be started for the job [name]. | The Report Creator for report jobs cannot be started. | Check the report job settings.  If you use the "ExecuteReport" system function, check the name of the report job and the parameters passed when calling the function. |
| 538640388 | An error occurred during communication with the database server | The reporting database cannot be found or access is not possible for other reasons. | Check whether the reporting database is available at the storage location configured in the Runtime settings in engineering.  Examples:   - Does the folder specified as storage location in the Runtime settings exist? - Has the folder been specified in the correct notation? - On a panel: Is the SD card plugged in? |
| 538640389 | The creation of the report job [name] failed | The Report Creator is missing information about the report job.   A possible reason for this are problems with processing the report template. | Check the report job settings and the report template. |
| 538640390 | Report failed | Report Creator reports an error while generating the report. | Check the detailed error message for the report:   Control "Reports" > "Reports" tab > "Status" column. |

#### Configuring report templates in the add-in (RT Unified)

This section contains information on the following topics:

- [Requirements (RT Unified)](#requirements-rt-unified)
- [Login (RT Unified)](#login-rt-unified)
- [Setting up a data source (RT Unified)](#setting-up-a-data-source-rt-unified)
- [Configuring report templates (RT Unified)](#configuring-report-templates-rt-unified)
- [Making general settings (RT Unified)](#making-general-settings-rt-unified)
- [Undo and redo (RT Unified)](#undo-and-redo-rt-unified)
- [Tips on design and layout (RT Unified)](#tips-on-design-and-layout-rt-unified)

##### Requirements (RT Unified)

This section contains information on the following topics:

- [General requirements and restrictions (RT Unified)](#general-requirements-and-restrictions-rt-unified)
- [Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)
- [Installing the Excel manifest (RT Unified)](#installing-the-excel-manifest-rt-unified)
- [Setting up read access to the Excel manifest (RT Unified)](#setting-up-read-access-to-the-excel-manifest-rt-unified)
- [Adding the Reporting add-in in Excel (RT Unified)](#adding-the-reporting-add-in-in-excel-rt-unified)
- [Configuring Internet Explorer and Edge (RT Unified)](#configuring-internet-explorer-and-edge-rt-unified)

###### General requirements and restrictions (RT Unified)

The following requirements and restrictions apply to the configuration of report templates.

###### Installing the Excel add-in

The installation of the Reporting add-in on a computer requires that the operating system and the local MS Excel installation are regularly updated.

If there are problems with the installation, check the version of the local MS Excel installation. Lengthy maintenance intervals between the operating system and Excel can cause problems during installation of the add-in.

Update the operating system and the Excel version if necessary.

To install the add-in with a local Excel installation, MS Excel with build 16.0.6769 or higher is required.

> **Note**
>
> **Note the Microsoft upgrade restrictions**
>
> If you have an Excel installation that cannot be upgraded to Build 16.0.6769 or higher (for example, because Excel was installed using a single Office license), purchase a current Office version or use Online Office.

###### IIS settings for standalone installation of the Excel Add-In

To install the Excel Add-In on a PC without Unified Runtime, the same IIS (Internet Information Services) settings must be active in Windows that are required to install WinCC Unified Runtime on a PC.

You can find additional information in the "SIMATIC Unified PC Installation" user help section on the software and hardware requirements.

###### Enable Reporting

The Runtime project that is the data source of a report template must have reporting functionality enabled.

You activate the reporting functionality of a Runtime project before loading it into the device in TIA Portal: "Runtime settings" of the HMI device > "Reporting" > "Enable Reporting" option

> **Note**
>
> **Devices with a device version lower than V18**
>
> Reporting is always enabled for HMI devices with a device version lower than V18.

###### Unified Comfort Panel

Contexts are not supported for Unified Comfort Panel. This option is not available in a report template with a Unified Comfort Panel as data source.

---

**See also**

[Version compatibility (RT Unified)](#version-compatibility-rt-unified)

###### Installation of the Reporting add-in (RT Unified)

> **Note**
>
> **Regular updates of operating system and MS Excel**
>
> The installation of the Reporting add-in on a computer requires that the operating system and the local MS Excel installation are regularly updated.
>
> If there are problems with the installation, check the version of the local MS Excel installation. Lengthy maintenance intervals between the operating system and Excel can cause problems during installation of the add-in.
>
> Update the operating system and the Excel version if necessary.
>
> To install the add-in with a local Excel installation, MS Excel with build 16.0.6769 or higher is required.

> **Note**
>
> **Note the Microsoft upgrade restrictions**
>
> If you have an Excel installation that cannot be upgraded to Build 16.0.6769 or higher (for example, because Excel was installed using a single Office license), purchase a current Office version or use Online Office.

###### Procedure

1. Install the Excel manifest on the computer.
2. Set up read access to the installation path of the Excel manifest.
3. Add the add-in to Excel.

---

**See also**

[Installing the Excel manifest (RT Unified)](#installing-the-excel-manifest-rt-unified)
  
[Setting up read access to the Excel manifest (RT Unified)](#setting-up-read-access-to-the-excel-manifest-rt-unified)
  
[Adding the Reporting add-in in Excel (RT Unified)](#adding-the-reporting-add-in-in-excel-rt-unified)

###### Installing the Excel manifest (RT Unified)

###### Procedure

1. In the installation package of WinCC Unified on "DVD_2", double-click the file "Support\Reporting\SIMATIC_WinCC_Unified_Reporting_<Version number>.exe".
2. Select the target directory to which the underlying ZIP file is extracted and confirm your input.

   The ZIP file is extracted and setup starts automatically.
3. Follow the setup instructions.
4. In the "Configuration" step, select the option for the Excel add-in.
5. Click "Next" and follow the setup instructions.

**Note**

**Start setup manually**

To start the setup manually after the file was extracted, select the option "Extract the setup files without being installed".

Start the setup later by running the "Setup.exe" file as administrator in the target directory.

---

**See also**

[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)

###### Setting up read access to the Excel manifest (RT Unified)

###### Requirement

The Excel manifest is installed.

###### Procedure

Give the users that create templates with the Excel add-in read access to the installation path of the Excel manifest: <target directory>\WinCCUnifiedReporting\Excelmanifest

> **Note**
>
> This step is also necessary if the user belongs to a group in the user management with general read permission.

---

**See also**

[Installing the Excel manifest (RT Unified)](#installing-the-excel-manifest-rt-unified)
  
[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)

###### Adding the Reporting add-in in Excel (RT Unified)

###### Requirement

- The Excel manifest is installed on the PC.
- Read access to the installation path of the Excel manifest is set up.
- The following software is available on the computer:

  - Local Excel

    MS Excel (Build 16.0.6769 or higher)

    > **Note**
    >
    > **Regular updates of operating system and MS Excel**
    >
    > The installation of the Reporting add-in on a computer requires that the operating system and the local MS Excel installation are regularly updated.
    >
    > If there are problems with the installation, check the version of the local MS Excel installation. Lengthy maintenance intervals between the operating system and Excel can cause problems during installation of the add-in.
    >
    > Update the operating system and the Excel version if necessary.

    > **Note**
    >
    > **Note the Microsoft upgrade restrictions**
    >
    > If you have an Excel installation that cannot be upgraded to Build 16.0.6769 or higher (for example, because Excel was installed using a single Office license), purchase a current Office version or use Online Office.
  - Or Office online

###### Procedure

1. Open Microsoft Excel.
2. Open the "Trust Center" under "File" > "Options".
3. Click "Trust Center Settings".
4. Click "Catalogs of trusted add-ins".
5. Add the catalog using the URL "\\<Computer name>\Excelmanifest".

   ![Procedure](images/142754073355_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142754073355_DV_resource.Stream@PNG-en-US.png)
6. Make sure that the check mark in the "Show in Menu" column is set.
7. End and restart Excel.
8. In the "Insert" menu, click "My Add-ins".

   ![Procedure](images/142759971979_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142759971979_DV_resource.Stream@PNG-en-US.png)

   In the "Office Add-ins" dialog box, the Siemens add-in is displayed under "Shared folders".
9. Select the add-in and click "Add".

   ![Procedure](images/142760213003_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/142760213003_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Installing the Excel manifest (RT Unified)](#installing-the-excel-manifest-rt-unified)
  
[Setting up read access to the Excel manifest (RT Unified)](#setting-up-read-access-to-the-excel-manifest-rt-unified)
  
[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)

###### Configuring Internet Explorer and Edge (RT Unified)

The Reporting Excel add-in uses the certificate that was selected during installation of WinCC Unified Runtime or later in "WinCC Unified Configuration".

Some browsers do not recognize self-signed certificates as trusted. If you use a self-signed certificate for WinCC Unified Runtime, you must add the certificate to the list of trusted certificates in Internet Explorer or Edge on the device on which the Excel add-in is installed.

You can find detailed information on handling certificates here.

###### Trusting self-signed certificates

The following section describes the procedure for adding a self-signed certificate to the list of trusted certificates, using Internet Explorer as an example:

1. Start Internet Explorer.
2. In the address line, enter the host name entered when creating the certificate.

   You will receive a security warning.
3. Click "Continue to this website (not recommended)".
4. Click "View Certificates".
5. Click "Install Certificate".
6. Click "Place all certificates in the following store" and "Browse".
7. Click "Trusted Root Certification Authorities" followed by "OK".
8. Exit the dialog.
9. If you receive a security warning as to whether you want to trust the certificate, confirm it with "Yes".
10. Load the page again.

**Note**

Do not use the preset options for automatic selection of the certificate store.

##### Login (RT Unified)

A login dialog opens in the Excel add-in in the following cases:

- After start of Excel and the add-in
- When using an online connection: When the connection to the Runtime server must be re-established.

  Examples:

  - Runtime has been reloaded.
  - The security token has expired due to a timeout.

###### Requirement

- The add-in is installed.
- When using an online connection:

  - A Runtime server is accessible.
  - A Runtime project is running on the server for which reporting is enabled.

###### Procedure

In order to use an online connection, log onto a Runtime server:

1. Under "Server", enter the device name or FQDN (Fully qualified domain name) or the IP address of the server on which the project is running that is to serve as the data source for the report template:

   - If the device name/FQDN is used to address the Runtime web page, use Device Name/FQDN.
   - If IP address is used for addressing, enter the IP address.
2. Enter the user name and password of a user that is registered on the server in the Runtime user management.
3. Click "Login".

**Note**

If Runtime is installed on the same computer as the add-in, it is not allowed to enter the string "localhost" under "Server" to register the add-in.

In order to use an offline connection, click "Go offline".

###### Result

**Online connection**

The add-in is connected to the Runtime server and the options available there are loaded.

You can now create report templates.

**Offline connection**

Before you create report templates, set up the offline connection.

---

**See also**

[Installation of the Reporting add-in (RT Unified)](#installation-of-the-reporting-add-in-rt-unified)
  
[Setting up an offline connection (RT Unified)](#setting-up-an-offline-connection-rt-unified)
  
[General requirements and restrictions (RT Unified)](#general-requirements-and-restrictions-rt-unified)

##### Setting up a data source (RT Unified)

This section contains information on the following topics:

- [Using an online connection (RT Unified)](#using-an-online-connection-rt-unified)
- [Using an offline connection (RT Unified)](#using-an-offline-connection-rt-unified)

###### Using an online connection (RT Unified)

This section contains information on the following topics:

- [Introduction to online connection (RT Unified)](#introduction-to-online-connection-rt-unified)
- [Setting up an online connection (RT Unified)](#setting-up-an-online-connection-rt-unified)
- [Removing options (RT Unified)](#removing-options-rt-unified)

###### Introduction to online connection (RT Unified)

When an online connection is present, the add-in establishes a connection to a Runtime server. The project running on the server serves as data source for the add-in.

The connection settings allow you to:

- Change the connected Runtime server to another Runtime server
- When a report template that was created with a different Runtime server than the currently connected server is reused: check the options available on the server and delete the options that were not loaded

###### Setting up an online connection (RT Unified)

###### Requirements

- A Runtime server is accessible.
- A Runtime project is running on the server.

###### Procedure

1. In the "Data sources" group on the "WinCC Unified" tab, click on "Connections".
2. Click "Online" under "Connections" in the add-in.
3. Under "Server", enter the server name.

   Use the same spelling as when the Runtime server certificate was created.
4. Click "Load".

**Note**

If Runtime is installed on the same computer as the add-in, use of the name "localhost" is not permitted.

###### Result

- A server node is created.
- The add-in is connected to the Runtime server and its options are loaded.

  Data source items of these options can be added to report templates. Their data can be read in from Runtime to Excel.

  > **Note**
  >
  > To check which options were loaded, click on the server node.
  >
  > Options that are being used in the currently open report template but are not available on the connected server have a red icon. You can remove the option:
- If no connection can be established or an incorrect server name has been entered, the add-in will display a corresponding error message.

---

**See also**

[Removing options (RT Unified)](#removing-options-rt-unified)

###### Removing options (RT Unified)

###### Introduction

If you reuse report templates across servers, e.g. in order to adapt an existing template for another project, it may be necessary to remove unavailable options from the connection settings.

The procedure for this is presented using the Performance Insight option as an example.

###### Requirement

- The add-in was connected to a server on which the Performance Insight (PI) option is installed.
- A report template that uses KPIs was created with the add-in.
- The add-in was then connected to a server without the Performance Insight option installed for the purpose of adapting the template to the project running there.

###### Removing an option

| Symbol | Meaning |
| --- | --- |
| 1. In the "Data sources" group on the "WinCC Unified" tab, click on "Connections". 2. Under "Connections", click on "Online". 3. Select the server node.    You see the loaded options under the server node:       | Symbol | Meaning |    | --- | --- |    | ![Removing an option](images/133086623499_DV_resource.Stream@PNG-de-DE.png)      ![Removing an option](images/133086623499_DV_resource.Stream@PNG-de-DE.png) | Available options  The following applies to data source items of these options: - They can be added to the report template. - Their data can be read in from Runtime to Excel in the add-in. |    | ![Removing an option](images/133098420875_DV_resource.Stream@PNG-de-DE.png)      ![Removing an option](images/133098420875_DV_resource.Stream@PNG-de-DE.png) | Unavailable options In the example: Performance Insight  The following applies to data source items of these options: - They cannot be added to the report template. - If the report template already has a data source element of this option, its data cannot be read in from Runtime to Excel. | 4. Select the "Performance Insight" option under the server node. 5. Click the "Delete" button next to the option. 6. Confirm your input. |  |

###### Result

The option is removed from the connection settings.

Next, remove all data source items of this option from the report template.

###### Reloading an option

When the add-in is connected to a Runtime server, all options available on the server are loaded.

To reload an option that was deleted in the connection settings but is available on the server, select the server node and click "Load".

###### Using an offline connection (RT Unified)

This section contains information on the following topics:

- [Introduction to offline connection (RT Unified)](#introduction-to-offline-connection-rt-unified)
- [Setting up an offline connection (RT Unified)](#setting-up-an-offline-connection-rt-unified)
- [Removing options (RT Unified)](#removing-options-rt-unified-1)

###### Introduction to offline connection (RT Unified)

With the offline connection, the add-in uses a configuration file as data source.

The connection settings allow you to:

- Change the configuration file used
- When reusing a report template with a configuration based on a Runtime server different to that of the currently selected configuration file: Check the available options and delete the options that were not loaded.

###### Setting up an offline connection (RT Unified)

###### Requirement

An offline configuration file was created in the "Reports" control in Runtime. The configuration file is available on the device.

###### Procedure

1. In the "Data sources" group on the "WinCC Unified" tab, click on "Connections".
2. Under "Connections", click on "Offline".
3. Click "Open offline configuration".
4. Select the desired file in the window that opens and confirm your entries.
5. Click "Load".
6. Select the desired options.
7. Confirm your entries.

###### Result

- A server node is created. The node bears the name of the server on which the configuration file is based.
- The configuration file, together with its options, is loaded into the add-in. The data of the configuration file is available for configuring the report template.

  > **Note**
  >
  > To check which options were loaded, click on the server node.
  >
  > Options that are being used in the currently open report template but are not available in the configuration file have a red icon. You can remove the option:

---

**See also**

[Removing options (RT Unified)](#removing-options-rt-unified-1)
  
[Exporting an offline configuration file (RT Unified)](#exporting-an-offline-configuration-file-rt-unified)

###### Removing options (RT Unified)

###### Introduction

If you reuse report templates across servers, e.g. in order to adapt an existing template for another project, it may be necessary to remove unavailable options from the connection settings.

The procedure for this is presented using the Performance Insight option as an example.

###### Requirement

- The add-in was changed over to an offline connection whose configuration file does not include Performance Insight.
- A report template was opened in the add-in whose configuration is based on a connection to a Runtime server on which Performance Insight is installed.

###### Removing an option

| Symbol | Meaning |
| --- | --- |
| 1. In the "Data sources" group on the "WinCC Unified" tab, click on "Connections". 2. Under "Connections", click on "Offline". 3. Select the server node.    You see the loaded options under the server node:       | Symbol | Meaning |    | --- | --- |    | ![Removing an option](images/133086623499_DV_resource.Stream@PNG-de-DE.png)      ![Removing an option](images/133086623499_DV_resource.Stream@PNG-de-DE.png) | Available options  The following applies to data source items of these options: - They can be added to report templates. - Their data can be read in from the configuration file to Excel. |    | ![Removing an option](images/133098420875_DV_resource.Stream@PNG-de-DE.png)      ![Removing an option](images/133098420875_DV_resource.Stream@PNG-de-DE.png) | Unavailable options In the example: Performance Insight  The following applies to data source items of these options: - They cannot be added to the report template. - If the report template already has a data source element of this option, its data cannot be read in from the configuration file to Excel. | 4. Select the "Performance Insight" option under the server node. 5. Click the "Delete" button next to the option. 6. Confirm your input. |  |

###### Result

The option is removed from the connection settings.

Next, remove all data source items of this option from the report template.

###### Reloading an option

When a configuration file is loaded, all options available in the file are loaded.

To reload an option that was deleted in the connection settings but is available in the configuration file, select the server node and click "Load".

##### Configuring report templates (RT Unified)

This section contains information on the following topics:

- [Workflow for configuring report templates (RT Unified)](#workflow-for-configuring-report-templates-rt-unified)
- [User interface of the add-in (RT Unified)](#user-interface-of-the-add-in-rt-unified)
- [Working with segments (RT Unified)](#working-with-segments-rt-unified)
- [Adding data source items (RT Unified)](#adding-data-source-items-rt-unified)
- [Delete data source elements (RT Unified)](#delete-data-source-elements-rt-unified)
- [Working with configurations (RT Unified)](#working-with-configurations-rt-unified)
- [Changing the column sequence (RT Unified)](#changing-the-column-sequence-rt-unified)
- [Reading Runtime data in Excel (RT Unified)](#reading-runtime-data-in-excel-rt-unified)
- [Calculation modes for data source elements (RT Unified)](#calculation-modes-for-data-source-elements-rt-unified)

###### Workflow for configuring report templates (RT Unified)

###### Requirement

An online connection or offline connection has been established.

###### Procedure

To create a new report template, proceed as follows:

1. Open a new Excel file.
2. Add a segment.

   You can choose between time series segments and single value segments.
3. Add data source items to the segment.

   The exact procedure depends on the type of the data source item.
4. Optional: If you do not want a data source item to use the default configuration, determine its configuration.

   You have the following options:

   - Select an existing configuration.
   - Create a new configuration and select it.
   - Define a local configuration.
5. Optional: To define additional segments, repeat steps 2 to 4.
6. Optional: When using an online connection, test the template by reading the runtime data of selected segments or all segments.

---

**See also**

[Setting up a data source (RT Unified)](#setting-up-a-data-source-rt-unified)

###### User interface of the add-in (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Structure

If you click on "Segments" in the "Configuration" group, you see the following interface:

![Structure](images/142022624523_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Toolbar |
| ② | Work area |

Toolbar buttons:

| Button | Tooltip | Description |
| --- | --- | --- |
| ![Structure](images/142025031051_DV_resource.Stream@PNG-de-DE.png) | "Segment configuration" | Loads the interface to add and edit segments in the work area. |
| ![Structure](images/142024796299_DV_resource.Stream@PNG-de-DE.png) | "Data source item configuration" | Loads the interface for adding and editing the configuration of a data source item in the work area. |
| ![Structure](images/142024587787_DV_resource.Stream@PNG-de-DE.png) | "Basic settings" | Loads the interface for setting the language settings in the work area. |
| ![Structure](images/142023530251_DV_resource.Stream@PNG-de-DE.png) | "Update all" | Reads the Runtime data of the connected data source into the data tables of the segments. |
| ![Structure](images/142024787723_DV_resource.Stream@PNG-de-DE.png) | "Delete Runtime data" | Removes all Runtime data from the report template. |
| ![Structure](images/142024907275_DV_resource.Stream@PNG-de-DE.png) | Logoff | Logs out the user currently logged in to the add-in. |
| ![Structure](images/142025039627_DV_resource.Stream@PNG-de-DE.png) | Help | Opens the user help for the add-in. |

---

**See also**

[The segment user interface (RT Unified)](#the-segment-user-interface-rt-unified)

###### Working with segments (RT Unified)

This section contains information on the following topics:

- [Basic information on segments (RT Unified)](#basic-information-on-segments-rt-unified)
- [Standard column (RT Unified)](#standard-column-rt-unified)
- [The segment user interface (RT Unified)](#the-segment-user-interface-rt-unified)
- [Create segments (RT Unified)](#create-segments-rt-unified)
- [Formats for relative time information (RT Unified)](#formats-for-relative-time-information-rt-unified)
- [Edit segments (RT Unified)](#edit-segments-rt-unified)
- [Delete segments (RT Unified)](#delete-segments-rt-unified)

###### Basic information on segments (RT Unified)

###### Definition

A report template consists of any number of segments. Each segment is a container to which you can add any number of data source items. The segment reads the data from its data source items.

There are time series segments and single value segments.

> **Note**
>
> **Hierarchical segments of PI options**
>
> Hierarchical segments are also available with PI Options installed. For more information on this, refer to the PI Options help.

###### Time series segments

A time series segment documents the data of its data source items in a defined time period.

It has a legend table and a data table.

**Data source items**

Time series segments can have the following data source items:

- Logging alarms
- Alarm statistics
- Logging tags
- User-defined columns
- Contexts
- Audit

> **Note**
>
> **Data source items of the PI options**
>
> If PI options are installed, additional data source items can be added. For more information on this, refer to the PI Options help.

**Legend table**

The table header row provides general information about the segment and its data source items.

You decide which type of information is provided when you create or edit the segment.

**Data table**

The data table outputs the data of the data source items. It documents how the data source items have changed in the defined time period.

The data table of a time series segment has the following columns:

| Columns |  | Description |
| --- | --- | --- |
| Time stamp column |  | Always output  Always output as the first column |
| Per data source item | Standard column | The standard column provides the standard property of the data source item. This property depends on the type of data source item.  For a data source item of the Tag type, e.g. the tag value |
| Optional columns | Provide more information about the data source item. What information this is depends on the type of the data source item.  For a data source item of the Tag type, e.g. the quality code of the tag value  You change the default settings for visibility, column title and order of these columns in the configuration of the data source item. |  |

In the default setting, the data source items in the data table have the order in which they were added to the segment.

> **Note**
>
> When the standard columns and optional columns provide numerical values, you can have the actual values replaced with texts or graphics from a text list or graphic list when importing the Runtime data.

###### Single value segments

A single value segment documents exactly one value for its data source items.

**Data source items**

Single value segments can have the following data source items:

- Logging tags
- Tags

> **Note**
>
> **Data source items of the PI options**
>
> If PI options are installed, additional data source items can be added. For more information on this, refer to the PI Options help.

**Data table**

The data table of a single value segment has the following columns per data source item:

| Columns | Description |
| --- | --- |
| Standard column | The standard column provides the standard property of the data source item.   For tags and logging tags: the tag value |
| Optional columns | Provide more information about the data source item.  For tags and logging tags:   - Time stamp - Data source item - Quality code of the tag value   You change the default settings for the visibility of these columns in the configuration of the data source item. |

The data table of a single value segment shows the data source items in the order in which they were added to the segment.

> **Note**
>
> When the standard columns and optional columns provide numerical values, you can have the actual values replaced with texts or graphics from a text list or graphic list when importing the Runtime data.

Single row segments do not have a table header row. However, in the configurations of their data source items, you can determine whether a caption is inserted for the displayed columns and the position at which this occurs.

---

**See also**

[Standard column (RT Unified)](#standard-column-rt-unified)

###### Standard column (RT Unified)

###### Introduction

For each data source item of a segment, a standard column is added in the data table of the segment.

###### Content of the standard column

The standard column provides the standard property of the data source item and depends on the type of the data source item:

| Data source item type | Default column title | Value |
| --- | --- | --- |
| Logging alarm | "Alarm ID" | Alarm IDs of the displayed alarms |
| Alarm statistics | "Alarm statistics [ID]" | Alarm IDs of the alarms displayed in the alarm statistics |
| Tag or logging tag | "<Name of the tags or logging tags>" | Value of the tag or logging tag |
| Context | "<Name of the context object>" | Context name |
| Audit | "Audit [<object name>]" | The name of the object monitored by the Audit Trail |
| User-defined column | Name entered when creating the data source item | As set in the configuration of the data source item:  - A fixed string.  Or - A dynamically calculated string |

###### Changing the column title

You can replace the default column title with a localizable display name. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified).

###### Replacing numerical values

If the standard column provides numeric values, you have the option to have the actual values replaced with texts or graphics from a text list or graphic list when the Runtime data is read in. See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).

User-defined columns are excluded from this.

---

**See also**

[Basic information on segments (RT Unified)](#basic-information-on-segments-rt-unified)

###### The segment user interface (RT Unified)

###### Structure

The interface for creating and editing segments has the following structure:

![Structure](images/143835346443_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| ① | Filter  Filters the list of segments by name. |
| ② | Button for creating a segment |
| ③ | List of segments  Each segment has buttons for reading in, editing and deleting the segment.  The following configuration is displayed for each segment:  - Segment name - Number of data source items - Insertion location of the segment in the Excel file - Time span - If context filters have been configured: The filter string   A click on the segment opens the area with the data source items. |

###### Create segments (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- The data source is set up.
- To filter the time interval of the time series segment depending on the context: There are contexts in the project that run on the connected Runtime server or are the basis of the configuration file.

###### Procedure

|  |  |  |
| --- | --- | --- |
| 1. Click on "Segments" in the "Configuration" group. 2. Click "New segment". 3. Select "New time series segment" or "New single value segment". 4. Enter a segment name.       |  |  |  |    | --- | --- | --- |    | **Note**  Note the Excel restrictions for naming tables (for example, do not use blanks). Change the segment name only via the add-in, not via the Excel property "Table name". Do not change the name of the worksheet after creating the segment. The add-in addresses the segment by the segment name and the worksheet name. |  |  | 5. For a time series segment, make the following settings in addition:     - Under "File location" you determine where the segment will be inserted in the file. Enter the name of the worksheet and the cell.      Alternatively, click "Select a cell" and use the cell currently selected in the Excel file:                 ![Procedure](images/129293998859_DV_resource.Stream@PNG-de-DE.png)           ![Procedure](images/129293998859_DV_resource.Stream@PNG-de-DE.png)    - Under "Start" and "End", you determine the time period for which values are read into the segment.          |  |  |  |      | --- | --- | --- |      | ![Procedure](images/129294283275_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/129294283275_DV_resource.Stream@PNG-de-DE.png) | "Absolute date/time" | Select a date and a time. The information is absolute to the current date. |      | ![Procedure](images/129293991435_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/129293991435_DV_resource.Stream@PNG-de-DE.png) | "Relative date/time" | Select a reference time and a time interval. The information is relative to the current date. See also [Formats for relative time information](#formats-for-relative-time-information-rt-unified). |      | ![Procedure](images/129293995147_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/129293995147_DV_resource.Stream@PNG-de-DE.png) | "Date/Time of the cell" | Applies the value of the cell currently highlighted in the Excel file. Make sure that the cell supplies a valid time. |      | ![Procedure](images/129294850187_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/129294850187_DV_resource.Stream@PNG-de-DE.png) | "Date/Time of the tag" | Applies the value of the set tag. Make sure that the tag supplies a valid time. Possible data types:  - DateTime - String - Integer |    - (Optional) Under "Properties of the legend table", you configure the contents to be displayed in the table header row of the segment:         |  |  |  |      | --- | --- | --- |      | "Name" "Start" "End" "State" | General information on the segment |  |      | "Context filter" | If the segment time was limited by a context filter: The filter string is output. See step 6. |  |      | "Audit status" | If the segment has an audit data source item, the field shows the overall status of the audit data: - Green field: No manipulations of the Audit Trail were found in the queried time range. - Red field: Manipulations of the Audit Trail were found in the queried time range. Single or multiple entries have been deleted, added or changed. |  |      | "Header" | The table header row includes a list of the segment's data source items showing general information about these data source items. The information displayed for the data source items depends on their type. Example of contexts: Display name of the context, context provider, hierarchy path, short name of the context, full name of the context, option |  |       Use the check boxes to remove information from or add information to the legend table.      To change the sorting in the table header row, move the mouse pointer to a row and shift it using the arrow buttons or drag-and-drop. 6. (Optional) You can filter the time interval of the time series segment depending on the context. You can define up to two filter conditions.    Proceed as follows:    - Under "Context filter", click "+" or "Add new condition row".       The condition line is added.    - Click on "+" in the condition line.    - Under "Select context", select the root of the common plant model.       In the next row, you see the top level of the common plant model.    - Navigate through the common plant model to plant objects with contexts.      Plant objects and contexts can be recognized by the following icons:         |  |  |  |      | --- | --- | --- |      | ![Procedure](images/133490847499_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/133490847499_DV_resource.Stream@PNG-de-DE.png) | Plant object |  |      | ![Procedure](images/133490838923_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/133490838923_DV_resource.Stream@PNG-de-DE.png) | Context |  |    - Select a context.    - Select an operator.    - Enter a value.    - (Optional) Use "+" or "Add new condition row" to create a second condition and select whether the two conditions are to be linked with a logical AND or OR. 7. (Optional) Under "Autofit", configure whether the column width and row height of the data table is automatically adapted to the text read from Runtime. 8. Confirm your entries with "OK". |  |  |

###### Result

The segment is created and added to the list of segments:

Next, add data source items to the segment. Your procedure depends on the type of the new data source item.

---

**See also**

[Tips on design and layout (RT Unified)](#tips-on-design-and-layout-rt-unified)
  
[Adding data source items (RT Unified)](#adding-data-source-items-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

###### Formats for relative time information (RT Unified)

###### Definition of a relative time information

The relative times are entered using a reference time and a time interval.

![Definition of a relative time information](images/129297375883_DV_resource.Stream@PNG-de-DE.png)

###### Reference time

Use one of the following characters for the reference time:

- "*" - Now
- "t" (today) - Today at midnight
- "y" (yesterday) - Yesterday at midnight
- "1-31" - Specific day of the current month

###### Time interval

- "y" (year): +1y = plus 1 year
- "mo" (month): +1mo = plus 1 month
- "w" (week): +1w = plus 1 week
- "d" (day): +1d = plus 1 day
- "h" (hour): +1h = plus 1 hour
- "m" (minute): +1m = plus 1 minute
- "s" (second): +1s = plus 1 second
- "ms" (milliseconds): +250ms = plus 250 milliseconds

###### Examples

- *-1y: One year ago today
- t+8h: Today at 8:00 am
- y+8h: Yesterday at 8:00 am
- 1+8h: The first day of the current month at 8:00 am
- *-1d: One day ago
- *-2h-30m-30s: 2 hours, 30 minutes and 30 seconds ago

---

**See also**

[Create segments (RT Unified)](#create-segments-rt-unified)

###### Edit segments (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Edit" next to a segment in the list of segments.
3. Edit the segment.

   You can make the same settings as when creating the segment.

###### Delete segments (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Delete" next to a segment in the list of segments.
3. Confirm your entries with "OK".

###### Adding data source items (RT Unified)

This section contains information on the following topics:

- [Adding log alarms (RT Unified)](#adding-log-alarms-rt-unified)
- [Adding alarm statistics (RT Unified)](#adding-alarm-statistics-rt-unified)
- [Add logging tags (RT Unified)](#add-logging-tags-rt-unified)
- [Adding tags (RT Unified)](#adding-tags-rt-unified)
- [Adding contexts (RT Unified)](#adding-contexts-rt-unified)
- [Adding user-defined columns (RT Unified)](#adding-user-defined-columns-rt-unified)
- [Add Audit (RT Unified)](#add-audit-rt-unified)

###### Adding log alarms (RT Unified)

###### Requirement

- There are logging alarms in the project that runs on the connected Runtime server or is the basis of the configuration file.
- The "Alarm" option is enabled in the connection settings.
- The "WinCC Unified" tab is visible in Excel.
- A time series segment is available.

###### Adding logging alarms

1. Click on "Segments" in the "Configuration" group.

   The list with the segments already created is loaded into the add-in.
2. Select a segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Alarms" option.
5. Select the "Alarm" entry under "Select alarms".
6. Under "Select alarms", select the entry "Alarm [ID]".
7. To cancel your selection, select the entry "Alarm [ID]" under "Selected data source items" and click "Delete".
8. Confirm with "OK".

**Note**

**Change selection criteria**

After you have added alarms, you can change the selection criteria and add more data source items to the segment.

For example: Output tags and alarms in the same segment.

###### Result

- The data source item for logging alarms is added to the add-in below the segment.
- The configuration of the data source item controls which data is added when importing the runtime data into the data table.

  > **Note**
  >
  > With the default setting, the data source item uses the default configuration. It shows all logging alarms of the project.

To display data that deviates from the default configuration, select one of the following options:

- Select a different matching configuration.
- Create your own configuration.
- Edit a configuration.
- Overwrite a configuration locally.

---

**See also**

[Creating or editing configurations for log alarms (RT Unified)](#creating-or-editing-configurations-for-log-alarms-rt-unified)
  
[Select configuration (RT Unified)](#select-configuration-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

###### Adding alarm statistics (RT Unified)

###### Introduction

To output statistical calculations for logging alarms in a report, add alarm statistics to a report template. The following calculations are available:

- Frequency of an alarm
- Average display time per state machine
- Total display time per state machine
- Maximum display time per state machine
- Minimum display time per state machine

The alarm statistics add columns with statistical calculations and columns with general alarm properties of the recorded alarms to the reports.

You can find more information about calculations in alarm statistics in the help for the alarm control.

###### Requirement

- The "Alarm" option is enabled in the connection settings.
- The "WinCC Unified" tab is visible in Excel.
- A time series segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list with the segments already created is loaded.
2. Select a time series segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Alarm" option.
5. Under "Select alarms", select the entry "Alarm statistic [ID]".
6. Under "Select alarm statistic" select the entry "Alarm statistic [ID]".
7. (Optional) To cancel your selection, select the entry "Alarm statistic [ID]" under "Selected data source items" and click "Delete".
8. Confirm with "OK".

**Note**

**Change selection criteria**

After adding the alarm statistics, you can change the selection criteria and add more data source items.

###### Result

The added data source item for alarm statistics is displayed below the segment and inserted into the data table.

First, the data table shows the contents configured in the default configuration for alarm statistics. To output other contents, select or create a configuration.

###### Add logging tags (RT Unified)

###### Requirement

- The project on which the connected Runtime server runs or the basis of the configuration file has logging tags.
- The "Logging tag" option was selected while setting up of the connection.
- The "WinCC Unified" tab is visible in Excel.
- A single value segment or time series segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list of segments is loaded.
2. Select a segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Logging tag" option.
5. Optional: To reduce the load time, filter which tags are loaded to the selection under "Add filter".

   The preset filters "*" return all logging tags of the project.

   - "Tag name": Enter the name of the tag whose logging tags you want to add.
   - "Logging tag name": Enter the name of the logging tags you want to add.

   Note that the entry is case-sensitive.
6. Click "Load".

   The logging tags of the project are filtered and provided under "Select tags".
7. Optional: Further reduce the number of tags that are offered for selection by clicking next to "Select logging tags" and entering another filter string.

   The list of tags you are being offered is filtered while you type.
8. Select one or more tags under "Select logging tags".

   The tags are added to the "Selected data source items" list.
9. To remove one or more data source items from "Selected data source items", select them and click "Delete".
10. Confirm with "OK".

    The added logging tags are shown below the segment and added to the Excel table.
11. If you have added the logging tag to a single value segment:

    - In the Excel worksheet, select the cell in which the logging tag is to be inserted.
    - Click the "Select a cell" button on the data source item of the logging tag.

      Alternatively, enter the name of the worksheet and the cell.

**Note**

**Filter by partial string**

You use the wildcard "*" to filter by partial strings.

For example:

- *T* returns all tags with a "T" in their name.
- *T returns all tags that end in "T".
- T* returns all tags that start with "T".

When filtering for structures, the separators must be part of the filter string.

For example: The following filters return the logging tags for all tags of the device "HMI_RT_1":

- Filter for tag: "HMI_RT_1::*"
- Filter for logging tag: "*"

**Note**

**Change selection criteria**

After you have added a tag, you can select a different option or a different filter and add additional data source items.

For example: Output KPIs and logging tags in the same segment.

---

**See also**

[Create or edit configurations for logging tags (RT Unified)](#create-or-edit-configurations-for-logging-tags-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

###### Adding tags (RT Unified)

###### Requirement

- The project on which the connected Runtime server runs or the basis of the configuration file has tags.
- The "Tag" option was enabled when the connection was set up.
- The "WinCC Unified" tab is visible in Excel.
- A single value segment is available.

###### Procedure

|  |  |  |
| --- | --- | --- |
| 1. Click on "Segments" in the "Configuration" group.    The list of segments is loaded. 2. Select the single value segment.    The segment is extended by the area for the data source items. 3. Click "+". 4. Select the "Tag" option. 5. Optional: To reduce the load time, filter which tags are loaded to the selection under "Add filter".    Under "Tag name", enter a filter, e.g. the name of the tag. Note that the entry is case-sensitive.    The default filter "*" returns all tags of the project.      |  |  |  |    | --- | --- | --- |    | **Note**  **Filter by partial string** You use the wildcard "*" to filter by partial strings. For example: - *T* returns all tags with a "T" in their name. - *T returns all tags that end in "T". - T* returns all tags that start with "T".When filtering for structures, the separators must be part of the filter string. For example: The filter "HMI_RT_1::*" returns all tags of the device "HMI_RT_1". |  |  | 6. Click "Load".    The tags of the project are filtered and provided under "Select tags".    You can recognize structs and arrays in the list by the following items:                ![Procedure](images/142101483915_DV_resource.Stream@PNG-de-DE.png)         ![Procedure](images/142101483915_DV_resource.Stream@PNG-de-DE.png)        |  |  |  |    | --- | --- | --- |    | ① | Button to display the members of the struct or array |  |    | ② | "Select all included data source items" Button that adds all members with a simple data type to the list of selected data source items |  | 7. Optional: Further reduce the number of tags that are offered for selection by clicking next to "Select tags" and entering another filter string.               ![Procedure](images/142126586763_DV_resource.Stream@PNG-en-US.png)         ![Procedure](images/142126586763_DV_resource.Stream@PNG-en-US.png)      The list of tags you are being offered is filtered while you type. 8. Select which tags will be added to the segment. You have the following options:       | Target | Procedure | Result |    | --- | --- | --- |    | Show the members of a struct or array. | Click the button with the arrow next to the struct or array. | A second "Select tags" list is added, in which you can see all the members of the struct or array. You can add to the segment any members that have a simple data type, e.g. bool, float or string. |    | Add all members of a struct or array. | Next to the struct or array, click "Select all included data source items". | All members with a simple data type are added to the "Selected data source items" list and marked as selected under "Select tags": |    | Select tags with simple data type. | Under "Select tag", click the required tags. | The tags are added to the "Selected data source items" list and marked as selected under "Select tags":            ![Procedure](images/142128090763_DV_resource.Stream@PNG-de-DE.png)      ![Procedure](images/142128090763_DV_resource.Stream@PNG-de-DE.png) |       |  |  |  |    | --- | --- | --- |    | **Note**  **Automatic filtering when displaying the members or selection of all members**  If you click the button to display the members of a struct or array or activate the option to select their members, the struct or array is set as a filter: - The list under "Select tags" only shows the struct or array. - A second "Select tags" list is added below this, in which you can see all members of the struct or array.To see all available tags again, delete the filters. |  |  |     |  |  |  |    | --- | --- | --- |    | **Note**  **Change selection criteria** After you have added a tag, you can select a different option or a different filter and add additional data source items. |  |  | 9. To remove tags from the segment, click on the tags in "Selected data source items" and click "Delete". 10. Confirm with "OK". |  |  |

The added tags are added to the segment.

When the report template is updated in the add-in and when the report is generated in runtime, the tag values are inserted into the data table.

---

**See also**

[Creating or editing configurations for tags: (RT Unified)](#creating-or-editing-configurations-for-tags-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

###### Adding contexts (RT Unified)

###### Introduction

To display in a report which contexts are to run during a certain time period, add only contexts to a segment in the report template.

To display which process data has been accumulated during the runtimes of a context, add the context and other data source items, such as logging tags or logging alarms, to the segment.

###### Requirement

- There are contexts in the project that run on the connected Runtime server or are the basis of the configuration file.
- The "Context" option is enabled in the connection settings.
- The "WinCC Unified" tab is visible in Excel.
- A time series segment is available.

###### Adding a context to a segment

| Symbol | Meaning |
| --- | --- |
| 1. Click on "Segments" in the "Configuration" group.    The list with the segments already created is loaded. 2. Select a segment.    The segment is extended by the area for the data source items. 3. Click "+". 4. Select the "Context" option. 5. Select a context:    - Under "Select a context definition", select the root of the plant model.       In the next row, you see the top level of the common plant model.    - Navigate through the common plant model to plant objects with contexts.      Plant objects and contexts can be recognized by the following icons:         | Symbol | Meaning |      | --- | --- |      | ![Adding a context to a segment](images/133490847499_DV_resource.Stream@PNG-de-DE.png)      ![Adding a context to a segment](images/133490847499_DV_resource.Stream@PNG-de-DE.png) | Plant object |      | ![Adding a context to a segment](images/133490838923_DV_resource.Stream@PNG-de-DE.png)      ![Adding a context to a segment](images/133490838923_DV_resource.Stream@PNG-de-DE.png) | Context |    - Select the desired contexts.      All selected contexts are included in the "Selected data source items" list     | Symbol | Meaning |    | --- | --- |    | **Note**  **Change selection criteria** After you have added a context, you can select a different option and add additional data source items. For example: Context and logging tags in the same segment. |  | 6. To remove one or more data source items from "Selected data source items", select them and click "Delete". 7. Confirm with "OK". |  |

###### Result

The selected contexts are displayed below the segment and inserted into the data table.

If you do not want a context to use the default configuration, select its configuration next.

**Content of the data table after executing the segment**

In segments to which only contexts or contexts and user-defined columns have been added:

- A line is inserted for each context whose runtime falls within the time period of the segment.
- "Time stamp" column: The time at which the context was started

In segments that combine contexts with logging tags or logging alarms:

- All logged values with the same time stamp are displayed per row.
- "Time stamp" column: The logging event
- "Start time" column: The time at which the context was started
- "Context " <Context name>"" column: The value passed to the context at start
- If no context was started at the time of logging, the context cells remain empty.

**Example**

The following data source items were added to a segment:

- The "Product" context

  Runtime of the context: 15:00:00 to 19:59:59 hours

  The context was started with the "Orange lemonade" value.
- The "Logged_Rotation" logging tag

  Logging cycle: 2s
- The "Logged_Temperature" logging tag

  Logging cycle: 5s
- The user-defined "Unit" column

  It contains the unit for "Logged temperatures".

Content of the data table after execution of the segment:

![Result](images/133584517899_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| Lines 2 to 6 | Values were logged for "Logged_Rotation" and "Logged_Temperature", while the "Product" context ran with the "Orange lemonade" value. |
| Line 8 | A value was logged for "Logged_Rotation" while no context was running. |

---

**See also**

[Contexts (RT Unified)](#contexts-rt-unified)

###### Adding user-defined columns (RT Unified)

###### Introduction

User-defined columns supplement the data of the other data source items of a time series segment with additional information:

- With a fixed string

  The string appears in each cell of the column.

  Example: Display measurement unit of the tag values in report
- With a formula

  The formula is calculated during generation for each cell in the dynamic column.

  Example: The sum of the tag values output in the report.

The configuration of the user-defined column controls which string or formula it uses.

###### Requirement

- The "User-defined column" option was enabled when the connection was set up.
- The "WinCC Unified" tab is visible in Excel.
- A time series segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list of segments is loaded.
2. Select a segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the option "User-defined column".
5. Enter the name of the column under "name".
6. Click "Select" or press <ENTER>.

   The column is included in the list "Selected data source items".
7. Select a configuration for the user-defined column.
8. To remove one or more data source items from "Selected data source items", select them and click "Delete".
9. Confirm with "OK".

**Note**

**Change selection criteria**

After you have added a column, you can select a different option or a different filter and add additional data source items.

The added columns are displayed below the segment and inserted into the data table.

---

**See also**

[Creating and editing configurations for user-defined columns (RT Unified)](#creating-and-editing-configurations-for-user-defined-columns-rt-unified)
  
[Select configuration (RT Unified)](#select-configuration-rt-unified)
  
[Working with configurations (RT Unified)](#working-with-configurations-rt-unified)

###### Add Audit (RT Unified)

###### Introduction

To output the Runtime device Audit Trail in a report, add an Audit data source item to a report template.

You can find more information about the Audit option in WinCC Unified in the Totally Integrated Automation Portal help.

###### Requirement

- The Audit option was activated in the engineering for the Runtime device.
- The "Audit" option is activated in the connection settings of the Excel add-in.
- The "WinCC Unified" tab is visible in Microsoft Excel.
- A time series segment is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.

   The list with the segments already created is loaded.
2. Select a time series segment.

   The segment is extended by the area for the data source items.
3. Click "+".
4. Select the "Audit" option.
5. Select the Audit Trail.
6. (Optional) To undo your selection, select the Audit Trail under "Selected data source items" and click "Delete".
7. Confirm with "OK".

###### Result

The audit data source item is displayed below the segment.

When an Audit Trail is configured for the data source, the Audit data is added to the report when the Runtime data is read into Microsoft Excel and when it is generated in Runtime:

- In the legend table: Identifier of the overall status of the Audit Trail for the queried time range in the "Audit Status" field

  | Value | Description |
  | --- | --- |
  | Green | No manipulations of the Audit Trail were found in the queried time range. |
  | Red | Manipulations of the Audit Trail were found in the queried time range. Single or multiple entries have been deleted, added or changed. |

  Requirement: The "Audit status" option is activated on the segment under "Header properties".

  > **Note**
  >
  > **Overall status for check mode "None"**
  >
  > If the check mode "None" is set in the configuration of the audit data sources item, the "Audit status" field is always green.
- In the data table of the segment: Identifier of manipulations

  | Type of manipulation | Identifier in the data table |
  | --- | --- |
  | Value of entries changed | Directly at the entries |
  | Entries added |  |
  | Entries deleted | The manipulated time range receives a start and end entry. |

First, the data table shows the contents configured in the standard configuration for Audit. To output other contents, select or create a configuration.

###### Delete data source elements (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment with a data source element is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Expand a segment by clicking on it.

   The area for adding and editing data source elements appears.
3. Move the mouse pointer over a data source element and click "Delete".

###### Working with configurations (RT Unified)

This section contains information on the following topics:

- [Basics of configuration (RT Unified)](#basics-of-configuration-rt-unified)
- [Creating or editing configurations for log alarms (RT Unified)](#creating-or-editing-configurations-for-log-alarms-rt-unified)
- [Creating or editing configurations for an alarm statistics (RT Unified)](#creating-or-editing-configurations-for-an-alarm-statistics-rt-unified)
- [Create or edit configurations for logging tags (RT Unified)](#create-or-edit-configurations-for-logging-tags-rt-unified)
- [Creating or editing configurations for tags: (RT Unified)](#creating-or-editing-configurations-for-tags-rt-unified)
- [Creating or editing configurations for contexts (RT Unified)](#creating-or-editing-configurations-for-contexts-rt-unified)
- [Creating and editing configurations for user-defined columns (RT Unified)](#creating-and-editing-configurations-for-user-defined-columns-rt-unified)
- [Adding or editing configurations for audit (RT Unified)](#adding-or-editing-configurations-for-audit-rt-unified)
- [Select configuration (RT Unified)](#select-configuration-rt-unified)
- [Overwrite a configuration locally (RT Unified)](#overwrite-a-configuration-locally-rt-unified)
- [Delete configuration (RT Unified)](#delete-configuration-rt-unified)
- [Configuring optional columns (RT Unified)](#configuring-optional-columns-rt-unified)
- [Assigning text lists and graphic lists (RT Unified)](#assigning-text-lists-and-graphic-lists-rt-unified)
- [Setting a display name for standard column (RT Unified)](#setting-a-display-name-for-standard-column-rt-unified)

###### Basics of configuration (RT Unified)

The configuration of a data source item defines the values of a data source element that are displayed in a segment or how they are calculated and displayed.

There are specific configuration settings for each data-source-item type.

Data source items used in time series segments use a different configuration than data source items used in single-value segments.

You have the following options:

- Use standard configuration.

  There is a standard configuration for all types of data source items. Once added, data source items use the default configuration of their type.

  You can edit the standard configurations.
- Use user-defined configuration.

  You can create any number of user-defined configurations for all types of data source items.

  You can select one of the user-defined configurations on the data source item.
- Overwrite a configuration locally.

  You can overwrite the configuration selected at the data source item locally.

###### Creating or editing configurations for log alarms (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Creating a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration > Logging alarm configuration".
4. Enter the name of the configuration under "Configuration name".
5. (Optional) Enter texts or graphics from a text list or graphic list in the standard column instead of the alarm IDs.

   See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).
6. (Optional) Change the default settings of the optional columns. The optional columns are used to display the alarm properties.

   See [Configuring optional columns](#configuring-optional-columns-rt-unified).
7. (Optional) Filter the logging alarms to be displayed. You define a filter query for this purpose. The filter query can consist of up to two conditions.

   Proceed as follows:

   - Under "Filter", click "+" or "Add new condition row".
   - Select an alarm property, an operator, and enter a value.
   - Optional: Use "+" or "Add new condition row" to create additional conditions. Select whether the conditions are to be linked with a logical AND or OR.
8. Enable the option "Use system colors" so that the alarms are highlighted with the same colors as in the alarm control.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for logging alarms.
4. Edit the configuration settings. You have the same options as when creating the configuration.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Creating or editing configurations for an alarm statistics (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration > Alarm statistics configuration".
4. Enter the name of the configuration under "Configuration name".
5. (Optional) Enter texts or graphics from a text list or graphic list in the standard column instead of the alarm IDs.

   See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).
6. (Optional) Change the default settings of the optional columns. The optional columns are used to display the statistical calculations and alarm properties.

   See [Configuring optional columns](#configuring-optional-columns-rt-unified).
7. (Optional) Filter the contents to displayed in the alarm statistics. You define a filter query for this purpose. The filter query can consist of up to two conditions.

   Proceed as follows:

   - Under "Filter", click "+" or "Add new condition row".
   - Select an alarm property, an operator, and enter a value.
   - Optional: Use "+" or "Add new condition row" to create additional conditions. Select whether the conditions are to be linked with a logical AND or OR.
8. Enable the option "Use system colors" so that the alarms are highlighted with the same colors as in the alarm control.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item.
>
> See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for alarm statistics.
4. Edit the configuration settings. You have the same options as when creating the configuration.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Create or edit configurations for logging tags (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Creating a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration".
4. To create a configuration for logging tags in a time series segment, select the entry "Logging tag configuration".

   To create a configuration for logging tags in a single value segment, select the entry "Single value configuration logging tag".
5. Enter the name of the configuration under "Configuration name".
6. Under "Calculation mode", select the data to be written if no current value is available.
7. (Optional) If the configuration is for logging tags with the numeric data type, you can output texts or graphics from a text list or graphic list in the standard column instead of the tag value.

   See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).
8. Set the other settings as described below.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for logging tags.
4. Edit the configuration settings.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Additional settings for time series segments

In time series segments, the following additional settings are available for logging tags:

| Setting | Description |
| --- | --- |
| "Interval" | Only for the "Stepped" and "Interpolated" calculation modes. |
| "Columns" > "Quality Code" | (Optional) Change the default settings of the optional "Quality Code" column.  See [Configuring optional columns](#configuring-optional-columns-rt-unified). |

###### Additional settings for single value segments

In single value segments, the following additional settings are available for logging tags:

| Setting | Description |
| --- | --- |
| "Time stamp" | Determine the date and time for which the value is read.   Proceed as described below. |
| "Show captions" | Define whether a header is displayed in the columns for the time stamp, the data source item and the quality code. |
| "Show time stamp" | Determine whether and where this information is displayed in the table. The information is always in relation to the value cell. |
| "Show data source item" |  |
| "Show quality code" |  |

To set the "Time stamp", select one of the following options:

|  |  |  |
| --- | --- | --- |
| ![Additional settings for single value segments](images/129294283275_DV_resource.Stream@PNG-de-DE.png) | Absolute time information | Select a date and a time.  The information is absolute. |
| ![Additional settings for single value segments](images/129293991435_DV_resource.Stream@PNG-de-DE.png) | Relative time information | Select a reference time and a time interval.  The information is relative to the current date. |
| ![Additional settings for single value segments](images/129293995147_DV_resource.Stream@PNG-de-DE.png) | Read time information from cell | Applies the value of the cell currently highlighted in the Excel file.  Make sure that the cell supplies a valid time. |
| ![Additional settings for single value segments](images/129294850187_DV_resource.Stream@PNG-de-DE.png) | Read time information from tag | Applies the value of the set tag.  Make sure that the tag supplies a valid time.  Possible data types:   - DateTime - String - Integer |

---

**See also**

[Calculation modes for data source elements (RT Unified)](#calculation-modes-for-data-source-elements-rt-unified)

###### Creating or editing configurations for tags: (RT Unified)

###### Requirements

- The "WinCC Unified" tab is visible in Excel.

###### Creating a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration": ![Creating a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration> Tag single value configuration".
4. Enter the name of the configuration under "Name".
5. (Optional) If the configuration is for tags with the numeric data type, you can output texts or graphics from a text list or graphic list in the standard column instead of the tag value.

   See [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).
6. Set the other settings as described below.
7. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration".
3. Click a configuration for tags.
4. Edit the configuration settings.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Settings for single value segments

In single value segments, the following settings are available for tags:

| Setting | Description |
| --- | --- |
| "Show captions" | Select whether a header is displayed in the columns for the time stamp, the data source item and the quality code. |
| "Show time stamp" | Select whether the time stamp is output with the value. |
| "Show data source item" | Select whether the data source element is also output. |
| "Show quality code" | Select whether the quality code is output with the value. |

###### Creating or editing configurations for contexts (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Core statement

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Core statement](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Core statement](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration".
4. Select the entry "Configuration context".
5. Enter the name of the configuration under "Configuration name".
6. (Optional) Change the default settings of the optional columns. The optional columns are used to display important contextual information.

   See [Configuring optional columns](#configuring-optional-columns-rt-unified).
7. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified).

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for contexts.
4. Edit the configuration settings.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Creating and editing configurations for user-defined columns (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Procedure

|  |  |  |  |
| --- | --- | --- | --- |
| 1. Click on "Segments" in the "Configuration" group. 2. Click "Data source item configuration":               ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)         ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png) 3. Click "New Configuration > User-defined column configuration". 4. Enter the name of the configuration under "Configuration name". 5. Under "Formula", select one of the following options:    - Enter a fixed string.      The string is transferred into each cell of the column.    - Enter an Excel formula.      The formula is copied into each cell of the user-defined column and adapted to the respective row.       To prevent a part of the formula from being adjusted, place the character "$" in front of it.      Example         |  |  |  |  |      | --- | --- | --- | --- |      | Formula in configuration |  | =B2+C2 | =B$2+C2 |      | Adapting the formula in the report | in line 2 | =B2+C2 | =B2+C2 |      | in line 3 | =B3+C3 | =B2+C3 |  |      | in line 4 | =B4+C4 | =B2+C4 |  |         |  |  |  |  |      | --- | --- | --- | --- |      | **Note**  **No validity check**  The formula is not tested for correctness during either input or dynamic adaptation. |  |  |  | 6. Confirm your entries with "OK". |  |  |  |

###### Adding or editing configurations for audit (RT Unified)

###### Introduction

**Check mode**

The check mode of the configuration of an audit data source item determines

- Whether an integrity check is performed when the Runtime data is read, and what is checked.

  You can output the overall result of the check in the table header row in the "Audit status" field.
- Which audit data records are provided in the data table.

Possible check modes:

| Symbol | Meaning |
| --- | --- |
| "None" | Provides the data for all audit data records that fall within the requested time range. No integrity check is carried out.  Default setting |
| "Check only" | Checks all audit data records that fall within the requested time range without providing their data.   It is tested whether data records have been manipulated, deleted or added. |
| "Check entries" | Checks the audit data records. Provides the data that falls within the queried time range and that was not deleted from the Audit Trail or added later.   It is checked whether data records have been manipulated. |
| "Check all" | Checks all audit data records. Provides the data that falls within the queried time range.   It is tested whether data records were manipulated, deleted from the audit trail or subsequently added. |

**Filter type**

An audit data record consists of two entries:

- An entry for the user expectation
- An entry for the system response.

User expectation and system response may differ. In addition, there are situations in which only one of the two data records is created.

The filter type controls which data records and which entries are included in the report.

Possible filter types:

| Filter type | User expectation equals system response | User expectation does not equal system response | Data record entry for user expectation or system response is missing |
| --- | --- | --- | --- |
| "Show all data in detail" | Both data record entries are inserted. |  | The existing data record entry is inserted. |
| "Show data and conformity errors" | The data record entry with the user expectation is inserted. | Both data record entries are inserted. |  |
| "Show only data with conformity errors" | No data record entry inserted. |  |  |

###### Requirement

- The "WinCC Unified" tab is visible in Excel.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click "New Configuration > Audit configuration".
4. Enter the name of the configuration under "Name".
5. Select a check mode:
6. Specify a filter type.

   Preset value: "Show data and conformity errors"
7. (Optional) Change the default settings of the optional columns. The optional columns are used to display the audit attributes.

   You can find more information on configuring the optional columns in the WinCC Unified object model > Creating production logs > Configuring optional columns.
8. (Optional) To further filter the inserted content, define a filter query.

   The filter query can consist of up to two conditions. Proceed as follows:

   - Under "Filter", click "+" or "Add new condition row".
   - Select an Audit attribute, an operator and enter the value of the attribute.
   - Optional: Use "+" or "Add new condition row" to create additional conditions. Select whether the conditions are to be linked with a logical AND or OR.
9. Confirm your entries with "OK".

> **Note**
>
> To not use the default column title for the standard column, set a display name in the local configuration of the data source item. You can find more information on setting the display name in the WinCC Unified object model > Creating production logs > Setting the display name for the standard column.

###### Editing a configuration

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration":

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

   ![Editing a configuration](images/142024796299_DV_resource.Stream@PNG-de-DE.png)
3. Click a configuration for Audit.
4. Edit the configuration settings. You have the same options as when creating the configuration.
5. Confirm your entries with "OK".

The changes are applied the next time you read in the Runtime data.

###### Examples of the configuration of the filter type

The following table contains examples of data records that were generated in Runtime through changes to tags monitored by Audit:

| Data record ID | Tag name | Modified by | Old value | New value | Description |
| --- | --- | --- | --- | --- | --- |
| 1A | Motor1_Speed | User1 | 0 | 10 | An operator changes the speed of a motor in an I/O field of an HMI screen.  User expectation and system response are identical. |
| 1B | Motor1_Speed | System | 0 | 10 |  |
| 2A | ValvePercentile | User1 | 0 | 100 | An operator opens a valve using a slider on an HMI screen.  The valve has a physical blockage and cannot be opened. Therefore, no data record entry for the system response is generated. |
| 3A | ValvePercentile | User1 | 0 | 99 | A physical block has been removed and the operator repeats the entry. The valve reacts, but cannot be fully opened.  User expectation and system response differ. |
| 3B | ValvePercentile | System | 0 | 49 |  |
| 4B | Motor2_Speed | System | 0 | 20 | An operator changed the speed of another motor. The resulting data record was manipulated, and the user expectation entry was deleted.  There is only one entry for the system response. |

The following table shows which data record entries are inserted into the data table depending on the filter type selected when generating the report:

| Data record ID | Tag name | Modified by | Old value | New value |
| --- | --- | --- | --- | --- |
| Filter type "Show all data in detail" |  |  |  |  |
| 1A | Motor1_Speed | User1 | 0 | 10 |
| 1B | Motor1_Speed | System | 0 | 10 |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |
| Filter type "Show data and conformity errors" |  |  |  |  |
| 1A | Motor1_Speed | User1 | 0 | 10 |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |
| Filter type "Show only data with conformity errors" |  |  |  |  |
| 2A | ValvePercentile | User1 | 0 | 100 |
| 3A | ValvePercentile | User1 | 0 | 99 |
| 3B | ValvePercentile | System | 0 | 49 |
| 4B | Motor2_Speed | System | 0 | 20 |

---

**See also**

[Configuring optional columns (RT Unified)](#configuring-optional-columns-rt-unified)
  
[Setting a display name for standard column (RT Unified)](#setting-a-display-name-for-standard-column-rt-unified)

###### Select configuration (RT Unified)

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment with a data source item is available.
- There is a user-defined configuration for the type of the data source item.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Select the segment.

   The segment is extended by the area for the data source items.
3. Select the desired configuration from a data source item in the drop-down list.
4. Click "OK".

###### Result

The changes are applied the next time you read in the runtime data.

###### Overwrite a configuration locally (RT Unified)

A local configuration overwrites the configuration selected at the data source item. It applies only to the data source item for which it was entered.

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A segment with a data source item is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Select the segment.

   The segment is expanded to include the plant complex for the data source items.
3. Move the mouse over a data source item and click "Edit".

   You create a local configuration that first adopts the values of the original configuration.
4. Enter a name for the local configuration.
5. (Optional) Set a display name. See [Setting a display name for standard column](#setting-a-display-name-for-standard-column-rt-unified).
6. Make the remaining settings as required.

   You can make the same settings as in the default and custom configurations.
7. Confirm your entries with "OK".

###### Result

The changes are applied the next time you read in the Runtime data.

###### Delete configuration (RT Unified)

###### Requirement

A configuration is available.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Click "Data source item configuration".
3. Move the mouse to a configuration.
4. Click "Delete".

**Note**

**Default configurations cannot be deleted**

You can edit default configurations but not delete them.

###### Result

- The configuration is deleted.
- Data source items with this configuration obtain a local configuration with the same settings.

###### Configuring optional columns (RT Unified)

###### Introduction

In time series segments, data source items of the following types have optional columns:

- Logging tag
- Logging alarm
- Alarm statistics
- Audit
- Context

The optional columns of a data source item depend on its type. The configuration of the data source items controls whether and how the data table shows these columns.

This section describes how to configure the optional columns.

###### Requirements

The data source item configuration is open. The configuration must apply to a time series segment.

###### Showing and hiding columns

1. To show an optional column in the data table, enable the option for the desired column in the "Columns" area.
2. To hide a column, disable its option.

###### Changing the column title

The data table uses as default column titles the identifiers you see in the "Columns" area. To change the default column titles, do the following.

1. In the "Columns" area, move the mouse pointer to an optional column.
2. Click the button with the pin.
3. Assign a unique column title.

**Note**

**Localization**

The column title is stored in the Runtime language currently set in the basic settings of the add-in.

To localize the column title, change the Runtime language and repeat your entry in the new language.

###### Changing the column sequence

To change the order of the optional columns in the data table, proceed as described in [Changing the column sequence](#changing-the-column-sequence-rt-unified).

###### Assigning text list or graphic list

The values of numeric columns can be replaced by texts or graphics when the Runtime data is read in.

To assign a suitable text list or graphic list to the property, proceed as described in [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).

###### Assigning text lists and graphic lists (RT Unified)

###### Introduction

If standard columns and optional columns of data source items output numerical values, you can assign text lists and graphic lists to these columns. When the Runtime data is read in, the cell values of these columns are replaced by texts or graphics from the assigned lists.

This function improves the readability of the report and helps to draw the reader's attention to important information.

> **Note**
>
> **Restrictions**
>
> - Tags/logging tags
>
>   Assign a text list or graphic list to the standard column of data source items with a Tag or Logging tag type only if the tag or logging tag has a numeric data type.
>
>   You can assign a text list or graphic list to the optional "Quality Code" column regardless of the data type of the tag.
> - User-defined columns
>
>   It is not possible to assign a text list or graphic list for data source items with the User-defined column type.
> - Context and audit
>
>   Usually, the names of context objects and audit objects displayed in the standard column do not contain purely numerical values. It is not recommended to assign a text list or graphic list.

###### Example

Add two data source items with the same logging tag to a time series segment.

For the first data source item, use the default configuration. This causes the report to output the tag value in the standard column.

For the second data source item, select a configuration in which a graphic list is assigned to the standard column. The graphic list contains representational graphics staggered by value range. As a result, the report outputs a graphic in the standard column.

After reading in the Runtime data, the standard column of the second data source item makes readers of the report aware of limit violations. Readers can get the exact tag value from the standard column of the first data source item.

###### Requirements

- A segment with a data source item was created in the add-in.
- Suitable text lists or graphic lists have been configured in engineering for the connected data source.

###### Assigning text lists and graphic lists to the standard column

1. Click on "Segments" in the "Configuration" group.
2. Select the segment.

   The data source items of the segment are displayed.
3. Move the mouse over a data source item and click "Edit".

   The local configuration of the data source item opens.
4. Select a suitable list under "Assign text/graphic list".
5. To preview the selected list and its graphics or texts, click the "i" button.

   To hide the preview, click the "i" button again.

###### Assigning optional columns to text lists and graphic lists

1. Click on "Segments" in the "Configuration" group.
2. Select one of the following options:

   To make the assignment apply to a specific data source item, follow these steps:

   - Select the segment.

     The data source items of the segment are displayed.
   - Move the mouse over the data source item and click "Edit".

     The local configuration of the data source item opens.

   To make the assignment apply to multiple data source items of the same type, follow these steps:

   - Click "Data source item configuration": ![Assigning optional columns to text lists and graphic lists](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

     You can see all default and custom configurations.
   - Click on the desired configuration.

     The configuration opens.
3. In the "Columns" area, click the following button next to the desired optional column:

   ![Assigning optional columns to text lists and graphic lists](images/142024587787_DV_resource.Stream@PNG-de-DE.png)

   ![Assigning optional columns to text lists and graphic lists](images/142024587787_DV_resource.Stream@PNG-de-DE.png)

   An interface for assigning a text list or graphic list is loaded into the add-in.
4. Select the desired graphic list or text list from the drop-down list.
5. To preview the selected list and its graphics or texts, click the "i" button.

   To hide the preview, click the "i" button again.
6. Confirm your entries.

**Note**

If you are connected offline to the data source, no preview of graphic lists is available.

###### Result

When the Runtime data is read in, the assigned lists are searched for an entry that matches the actual cell value:

- If a matching entry is found, the corresponding text or graphic is inserted into the data table.
- If no matching entry is found, the actual cell value is inserted.

> **Note**
>
> The assignment of graphic lists slows down the import of the Runtime data into the Excel add-in.

---

**See also**

[Standard column (RT Unified)](#standard-column-rt-unified)
  
[Basic information on segments (RT Unified)](#basic-information-on-segments-rt-unified)

###### Setting a display name for standard column (RT Unified)

###### Introduction

You can assign a display name for the standard column of a data source item. When a display name is set, it is used in the data table instead of the default column title and is listed in the table header row.

Display names make reports clearer, for example, when data source items for contexts or tags have very long names.

You set the display name in the local configuration of the data source item.

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- There is a segment with a matching data source item.

###### Procedure

1. Click on "Segments" in the "Configuration" group.
2. Expand a segment by clicking on it.

   The area for adding and editing data source elements appears.
3. Move the mouse pointer to the data source item and click "Edit".

   The local configuration of the data source item opens.
4. Enter the desired column title in "Display name".

   The column title must be unique within the segment.
5. Confirm your entry with "OK".

**Note**

**Localization**

The column title is stored in the Runtime language currently set in the basic settings of the add-in.

To localize the column title, change the Runtime language and repeat your entry in the new language.

###### Result

- The data table uses the display name as the column title for the standard column of the data source item.
- As long as the following conditions are met, the "Display name" column is inserted into the table header row:

  - Display of the header row in table header row is enabled.

    Make this setting at the segment.
  - A display name is set for at least one data source item of the segment.

  The column lists the display names of all data source items. If no display name is set for a data source item, its cell remains empty.

> **Note**
>
> - If you assign a different configuration to the data source item, the display name is retained.
> - To return to the display of the default column title after assigning a display name, enter the name of the data source item under "Display name".

---

**See also**

[Standard column (RT Unified)](#standard-column-rt-unified)
  
[Overwrite a configuration locally (RT Unified)](#overwrite-a-configuration-locally-rt-unified)

###### Changing the column sequence (RT Unified)

###### Introduction

For a time series segment, you can change the default column order of the data table.

You have the following options:

- Specify the order which the data source items have in the data table.
- For each data source item: Set the order of its optional columns.

> **Note**
>
> The time stamp column always appears first.

###### Requirement

- The "WinCC Unified" tab is visible in Excel.
- A time series segment has been created.

###### Change the order of data source items

**Procedure**

1. Click on "Segments" in the "Configuration" group.
2. Click the time series segment in the list of time series segments.

   The data source items of the segment are displayed.
3. Left-click a data source item and move it up or down using drag-and-drop operation.

**Result**

The order of data source items in the segment interface is changed.

The next time the Runtime data is read in, the data table outputs the data source items in this order.

###### Changing the order of optional columns

**Procedure**

1. Select one of the following options:

   To change the column order of a particular data source item, follow these steps:

   - Select the segment.

     The data source items of the segment are displayed.
   - Move the mouse over the data source item and click "Edit".

     The local configuration of the data source item opens.

   To change the column order for all data source items that use the same configuration, follow these steps:

   - Click "Data source item configuration":

     ![Changing the order of optional columns](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

     ![Changing the order of optional columns](images/142024796299_DV_resource.Stream@PNG-de-DE.png)

     You can see all default and custom configurations.
   - Click on the desired configuration.

     The configuration opens.
2. Move the mouse pointer to a column under "Columns".

   The columns you see depend on the type of data source item.
3. Move the column up or down using the arrow buttons or drag-and-drop.

**Result**

The order of the optional columns in the configuration is changed.

The next time the Runtime data is read in, the data table outputs the optional columns in the changed order.

---

**See also**

[Basic information on segments (RT Unified)](#basic-information-on-segments-rt-unified)
  
[Configuring optional columns (RT Unified)](#configuring-optional-columns-rt-unified)

###### Reading Runtime data in Excel (RT Unified)

> **Note**
>
> Reading in Runtime data in Excel is used for testing. It is not intended for mass retrieval of data, as is the case when report jobs are executed in Runtime.

###### Requirement

An online connection is established.

###### Reading in all segments

1. Select "WinCC Unified > Segments".
2. Click "Update all":

   ![Reading in all segments](images/142023530251_DV_resource.Stream@PNG-de-DE.png)

   ![Reading in all segments](images/142023530251_DV_resource.Stream@PNG-de-DE.png)

###### Reading in individual segments

1. Select "WinCC Unified > Segments".
2. Next to a segment in the list of segments click, "Update":

   ![Reading in individual segments](images/142023530251_DV_resource.Stream@PNG-de-DE.png)

   ![Reading in individual segments](images/142023530251_DV_resource.Stream@PNG-de-DE.png)

###### Result

The segment or segments are run. The Runtime data of your data source items are read into Excel.

> **Note**
>
> **Controlling the column width and row height**
>
> When the automatic adjustment of the column width and row height is disabled in the segment properties, the text read in may be truncated or the formula results are replaced with "#" characters.
>
> Check the column widths and row heights and adjust them manually, if required, or select automatic adjustment. Manual adaptations only apply in the Excel add-in. They are not included in the generated reports.

> **Note**
>
> **Removing Runtime data from report template**
>
> Remove the Runtime data from the report template before you save the report template and make it available for uploading to Runtime.
>
> To do this, click the "Delete Runtime data" button ![Result](images/142024787723_DV_resource.Stream@PNG-de-DE.png) in the toolbar of the Excel add-in.

###### Diagnostics during the data query

Successful execution of the data query is documented by the add-in with a status message in the table.

If an error occurs during the data query, a general error message is displayed under status. In addition, detailed error messages are displayed in the "ErrorLog" worksheet.

###### Calculation modes for data source elements (RT Unified)

If there is no current value for a data source item for a requested point in time, the following calculation modes are available.

###### Calculation modes for tags

The following calculation modes are available for tags of a time series segment:

| Calculation mode | Description |
| --- | --- |
| Raw | The actual value available for the specified period. If no data are available, no value is output. |
| Stepped | If no data are available, the last value is used.  With this mode you can also use values with an invalid quality code. |
| Interpolate | The values are interpolated linearly for the specified time period.  With this mode you can only use values with a valid quality code. |

The following calculation modes are available for tags of a single value segment:

| Calculation mode | Description |
| --- | --- |
| Interpolate | The values are interpolated linearly for the specified time period.  With this mode you can only use values with a valid quality code. |
| Left | If no data is available, the last value before the specified period is used. |
| Right | If no data is available, the last value after the specified period is used. |

---

**See also**

[Create or edit configurations for logging tags (RT Unified)](#create-or-edit-configurations-for-logging-tags-rt-unified)

##### Making general settings (RT Unified)

This section contains information on the following topics:

- [Adapting the work area (RT Unified)](#adapting-the-work-area-rt-unified)
- [Changing the language (RT Unified)](#changing-the-language-rt-unified)
- [Zooming in the add-in (RT Unified)](#zooming-in-the-add-in-rt-unified)

###### Adapting the work area (RT Unified)

###### Undocking and moving the add-in

To enlarge your working area, you can undock the Excel add-in:

1. Open the drop-down list in the header of the add-in.
2. Click "Move".
3. Move the mouse pointer to the desired location and click the left mouse button.
4. To move the add-in again, keep the left mouse button pressed in the header of the add-in and move the mouse.
5. To dock the add-in again, double-click in the header of the add-in.

###### Adapting the size of the add-in

1. Open the drop-down list in the header of the add-in.
2. Click "Resize".
3. Move the mouse pointer to the left to make the add-in wider or to the right to make it narrower.
4. Left-click when you have reached the desired size.

###### Changing the language (RT Unified)

###### Changing the add-in language

The Excel add-in automatically uses the same user interface language as Excel. If you are using a language for Excel that is not included in the Unified options, English is used as the default language.

You can select the language for the contents of the report independently of the interface. To select another language, the language must be configured in Runtime.

###### Selecting the language for the report

1. Select "WinCC Unified > Segments".
2. Click "Basic settings":

   ![Selecting the language for the report](images/142024587787_DV_resource.Stream@PNG-de-DE.png)

   ![Selecting the language for the report](images/142024587787_DV_resource.Stream@PNG-de-DE.png)
3. Under "Runtime language", select the language of the report content.
4. Under "Query language" you select which language data queries have that require user input, e.g. filter definitions.

###### Zooming in the add-in (RT Unified)

###### Procedure

To zoom in or out of the display in the add-in, press <CTRL> and move the mouse wheel.

##### Undo and redo (RT Unified)

The Excel functions "Undo" and "Redo" are not available in the add-in.

##### Tips on design and layout (RT Unified)

This section includes tips on the visual design of reports. The apply for:

- Report templates
- Reports that were generated as XLSX file

> **Note**
>
> **Deviating PDF results**
>
> A PDF report created by LibreOffice can deviate in content or layout from a PDF report generated with Excel, for example, if the report template uses common Excel features that LibreOffice does not support, such as special fonts or chart types.

###### Arranging segments

Always place the segments of a report template side by side or each in their own worksheet.

Because the data tables of the segments grow dynamically, tables can overlap when segments are placed one below the other. In the add-in, this causes an error of the OfficeExtension.Error class when reading in the Runtime data.

###### Changing the column sequence

See section [Changing the column sequence](#changing-the-column-sequence-rt-unified).

###### Adapt column width and row height

For each segment of a report template, check whether the column widths and row heights of your data table are wide or high enough for the values to be read. If this is not the case, texts in the generated report are truncated or the formula results are replaced with "#" characters.

To do this, select one of the following options:

- In the properties of the segments, select the options for automatic adjustment of the column width and row height.
- Click "Update all"![Adapt column width and row height](images/142023530251_DV_resource.Stream@PNG-de-DE.png) in the report template.

  Values are imported to Excel from the data source. Check the column widths and row heights and adjust them manually, if required.

  > **Note**
  >
  > The manual adaptations apply only in the Excel add-in. They are not included in the generated reports.

###### Replacing numerical values

If columns of a data source item output numeric values, you can assign text lists and graphic lists to the columns. When the Runtime data is read in, the cell values of these columns are replaced by texts or graphics from the assigned lists. This improves the readability of the report and helps to draw the reader's attention to important information.

Example: Visualizing limit violations of tags with graphics

See section [Assigning text lists and graphic lists](#assigning-text-lists-and-graphic-lists-rt-unified).

###### Preparing imported Runtime data

Adjust the cell formatting of the Runtime data, for example, font, color, alignment, or number format. The rows inserted when reading the Runtime data adopt the formatting.

Add diagrams, pivot tables or formulas that graphically visualize, structure or evaluate the data imported from Runtime.

> **Note**
>
> If you have read Runtime data into the report template for better data preparation, remove it before saving the report template and making it available for upload to Runtime.
>
> To do this, click the "Delete Runtime data" button ![Preparing imported Runtime data](images/142024787723_DV_resource.Stream@PNG-de-DE.png) in the toolbar of the Excel add-in.

###### Set up page

Use "File > Print > Set up page" to define details for printing the report, for example:

- Alignment of the report (portrait format or landscape format)
- Scaling, for example, to print all columns on one page
- Inserting a user-defined header or footer

The print settings set in the report template are applied in Runtime when a report job is executed for PDF generation.

###### Renaming worksheets and segments

When you add a segment to a report template in the add-in, a table is created in Excel. The add-in addresses the table by the name of the worksheet and segment.

Do not rename worksheets after adding segments.

Do not change the table name of a segment using the Excel property "Table name". Edit the segment in the add-in and rename it there.

### Rearranging columns at runtime (RT Unified)

#### Introduction

You can rearrange the table columns in the following table-based controls:

- Alarm control
- Trend companion
- Process control
- Parameter set control
- System diagnostics control

#### Requirement

Configuration of the control in the engineering requires rearrangement of the columns.

#### Procedure

To move a column, drag-and-drop its column header onto the column header of another column.

> **Note**
>
> The time column cannot be moved.

#### Result

The moved column is inserted at the position that the cursor had when the drag-and-drop movement ended.

The new arrangement only applies to the current client. If you change the page or refresh the browser window, the arrangement is lost.

> **Note**
>
> If you move a column next to the hidden column and then unhide it, it is always shown to the right of the moved column when it is unhidden.

#### Example 1: Inserting columns to the left or the right

The procedure is illustrated based on the example of an alarm control. In the initial situation, the table of the alarm control has the following column arrangement:

![Example 1: Inserting columns to the left or the right](images/150312214667_DV_resource.Stream@PNG-de-DE.png)

To insert the "Origin" column to the right of the "Alarm text" column, proceed as follows:

1. Use drag-and-drop to move the column header of "Origin" to the right half of the column header of the "Alarm text" column.

   ![Example 1: Inserting columns to the left or the right](images/150321298443_DV_resource.Stream@PNG-de-DE.png)

   ![Example 1: Inserting columns to the left or the right](images/150321298443_DV_resource.Stream@PNG-de-DE.png)
2. The "Origin" column is inserted to the right of the "Alarm text" column.

   ![Example 1: Inserting columns to the left or the right](images/150321691019_DV_resource.Stream@PNG-de-DE.png)

   ![Example 1: Inserting columns to the left or the right](images/150321691019_DV_resource.Stream@PNG-de-DE.png)

To insert the "Origin" column to the left of the "Alarm text" column, proceed as follows:

1. Use drag-and-drop to move the column header of "Origin" to the left half of the column header of the "Alarm text" column.

   ![Example 1: Inserting columns to the left or the right](images/150321699595_DV_resource.Stream@PNG-de-DE.png)

   ![Example 1: Inserting columns to the left or the right](images/150321699595_DV_resource.Stream@PNG-de-DE.png)
2. The "Origin" column is inserted to the left of the "Alarm text" column.

   ![Example 1: Inserting columns to the left or the right](images/150321823371_DV_resource.Stream@PNG-de-DE.png)

   ![Example 1: Inserting columns to the left or the right](images/150321823371_DV_resource.Stream@PNG-de-DE.png)

#### Example 2: Reordering of columns in combination with hidden columns

The example illustrates the rearrangement of columns in combination with hidden columns.

- The alarm view has the same column order as in Example 1.
- The alarm view has been configured in the engineering system in such a way that the display of the "Origin" column is controlled dynamically in runtime by setting a tag.

To reorder the columns in combination with hidden columns, proceed as follows:

1. Hide the "Origin" column by setting the tag.
2. Insert the "Status text" column to the left of the "Area" column.
3. Unhide the "Origin" column by setting the tag.

The columns have the order "Alarm class", "Status text", "Origin", "Area", "Alarm text".

### Process diagnostics (RT Unified)

This section contains information on the following topics:

- [Basics of supervision with ProDiag (RT Unified)](#basics-of-supervision-with-prodiag-rt-unified)
- [Requirements and licensing (RT Unified)](#requirements-and-licensing-rt-unified)
- [Objects for the supervision and diagnostics of plants](#objects-for-the-supervision-and-diagnostics-of-plants)
- [GRAPH overview](#graph-overview)
- [Configuring a GRAPH overview (RT Unified)](#configuring-a-graph-overview-rt-unified)
- [PLC code view (RT Unified)](#plc-code-view-rt-unified)
- [Configuring the PLC code view](#configuring-the-plc-code-view)
- [ProDiag overview](#prodiag-overview)
- [Configuring the ProDiag overview](#configuring-the-prodiag-overview)
- [Initial value acquisition and criteria analysis (RT Unified)](#initial-value-acquisition-and-criteria-analysis-rt-unified)

#### Basics of supervision with ProDiag (RT Unified)

##### Introduction

The TIA Portal functionality, ProDiag (Process Diagnostics), is used to monitor and determine errors that occur in your plant or machine. You can use ProDiag to show the type of error, the cause of the error and the location of the error on the HMI device.

##### Use

You can use ProDiag functions to monitor your plant and to visualize it on an HMI device. The main objective of ProDiag is the reduction of downtime and loss of production after an error occurs, and the avoidance of errors using timely warnings. Diagnostic and display objects provide specific information for the operator for troubleshooting and show the processes on an HMI device on site.

##### Principle

In STEP 7, you create operand supervisions and configure the settings according to your requirements. When an error occurs, a supervision alarm is generated based on the criteria you have configured. The configured supervision instances are stored in the preset ProDiag function block. You can use the automatically generated ProDiag FBs or create and configure your own ProDiag FBs according to technological aspects.

##### Advantages

ProDiag enables you to configure supervisions and monitor your plant without changing the user program code.

You perform plant diagnostics on your HMI device. The data is automatically synchronized in order to keep the display on your HMI device always up-to-date.

#### Requirements and licensing (RT Unified)

##### Introduction

You configure the ProDiag supervisions in TIA Portal with STEP 7 and create the screen objects for monitoring and diagnostics with WinCC. You need a license to use the ProDiag functionality and the corresponding screen objects.

##### Software requirements

You need the following products to configure ProDiag supervisions and visualization on the HMI device:

- TIA Portal STEP 7 Professional
- WinCC Unified

##### Hardware requirements

ProDiag functionality is available for CPUs of the S7-1500 series with firmware version 2.0 or higher.

The objects for the supervision and diagnostics of plants are available for the following HMI devices:

- WinCC Unified

> **Note**
>
> Objects for supervision and diagnostics of plants can be used under the "Full access" and "Read access" protection levels configured in the CPU.
>
> ProDiag objects under the "HMI access" and "No access" protection levels cannot be used.

##### Licensing of ProDiag supervisions

The number of ProDiag monitors that you configure with STEP 7 is licensed. You do not need a license for the first 25 supervisions, licenses must be used for additional supervisions.

| Number of supervisions | <= 25 | <= 250 | <= 500 | <= 750 | <= 1000 | > 1000 *) |
| --- | --- | --- | --- | --- | --- | --- |
| Number of licenses | None | 1 | 2 | 3 | 4 | 5 |
| *) If it is clear from the beginning that > 1000 supervisions are required in the project, a license to use supervisions can be ordered without limitation. |  |  |  |  |  |  |

##### Licensing of ProjDiag objects

To use the objects for the diagnostics and supervision in conjunction with the ProDiag supervision in your program, you need a WinCC Unified ProDiag license.

##### Enable process diagnostics

To activate process diagnostics on an HMI device, follow these steps:

1. Open the "Runtime settings" of the HMI device in the project tree.
2. Under Process diagnostics, select the "Enable process diagnostics" option.

The display of process diagnostic alarms is enabled in runtime.

![Enable process diagnostics](images/164261333771_DV_resource.Stream@PNG-en-US.png)

#### Objects for the supervision and diagnostics of plants

##### Introduction

WinCC offers the following objects for displaying the current monitoring status and for fault diagnostics in the program code:

- GRAPH overview
- PLC code view
- ProDiag overview
- Criteria analysis control

##### GRAPH overview

The "GRAPH overview" object is used to display the current program status for executed steps of the GRAPH sequencer.

##### PLC code view

The "PLC code view" object is used to display the current program status of user programs that have been programmed in the LAD, FBD or GRAPH graphic programming languages.

##### ProDiag overview

The "ProDiag overview" object provides an overview of the current status of the supervisions in the context of a ProDiag Overview supervision block.

##### Criteria analysis control

The "Criteria analysis control" object is used to display the faulty operands in the user program that were determined for a selected alarm by criteria analysis.

#### GRAPH overview

##### Use

The "GRAPH Overview" object is used to display the current program status for executed steps of the GRAPH sequencer. Errors during execution of a program are displayed directly at the corresponding step.

The following information is displayed in the "GRAPH Overview" object:

- Name and status of the function block
- Status of initial and simultaneous steps
- Number and name of the first step currently executed step
- Operating mode for running the GRAPH sequencer

WinCC supports the display of step names for the GRAPH blocks in multiple languages starting from Version 6.0. The step names will then be displayed in the selected Runtime language following a language changeover in Runtime. If the selected language is not available, the names are displayed in the default language (English).

![Use](images/164599456139_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> To view the program status of an GRAPH instance data block in the "GRAPH overview" object, set the block's instance-specific properties to "Visible in HMI" and "Accessible from HMI".

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Process > Tag": Assign the tag.
- "Function bar": Specifies the buttons of the GRAPH overview.

##### Operating mode

There are four modes of operation available to you for running the GRAPH sequence:

- AUTO (default setting) - Automatically switches to the next step when the transition is fulfilled.
- TAP - Automatically switches to the next step when the transition is fulfilled and there is an edge change from "0" to "1" at the T_PUSH parameter.
- TOP - Automatically switches to the next step when the transition is fulfilled or there is an edge change from "0" to "1" at the T_PUSH parameter.
- MAN - The next step is not automatically enabled when the transition is fulfilled. You can select and deselect the steps manually.

> **Note**
>
> You set the operating mode by modifying the interface parameters of the GRAPH block in your control program.

In WinCC Unified Runtime, you can customize the name for the operating mode that is displayed in the GRAPH overview.

##### Configuring a compact view

You can also configure a compact GRAPH overview without function bar buttons and operating mode display.

To display a compact GRAPH overview in single-line compatibility mode, drag the control to the desired size.

##### Symbols

The symbols displayed in the GRAPH overview are pre-defined:

| Symbol |  | Function |
| --- | --- | --- |
| ![Symbols](images/81523267723_DV_resource.Stream@PNG-de-DE.png) | Error | Indicates that an error has occurred during the execution of a step. |
| ![Symbols](images/81524872587_DV_resource.Stream@PNG-de-DE.png) | Initial step | Indicates that the currently executing step is the first step in the GRAPH step sequence. |
| ![Symbols](images/81523276555_DV_resource.Stream@PNG-de-DE.png) | Simultaneous step | Shows that there are other simultaneous steps in the GRAPH step sequence in addition to the current one. |

##### Function bar

You can define the buttons of the GRAPH overview in runtime along with their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Function bar > Elements". By default, only the "Next Step" button is available. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the GRAPH overview:

| Button |  | Function |
| --- | --- | --- |
| ![Function bar](images/162811779467_DV_resource.Stream@PNG-de-DE.png) | Next Step | Jumps to the next step in parallel step. When you get to the last step, you can jump back to the first step. |
| ![Function bar](images/162811783435_DV_resource.Stream@PNG-de-DE.png) | Jump to Alarm Control | Opens the configured alarm control with the error message in WinCC Unified.  The button is intended to be populated with appropriate system functions/scripts. |
| ![Function bar](images/162821541003_DV_resource.Stream@PNG-de-DE.png) | Jump To PLC code view | Opens the configured PLC code view.  The button is intended to be populated with appropriate system functions/scripts.  Ideally, use the "OpenGRAPHViewerFromOverview" system function. |
| ![Function bar](images/162821544971_DV_resource.Stream@PNG-de-DE.png) | Jump to TIA Portal | Several script functions are available for opening the TIA Portal. |

#### Configuring a GRAPH overview (RT Unified)

##### Introduction

You can use the GRAPH overview to view the current program status for the executed steps of a GRAPH sequencer.

##### Requirement

- A PLC including a GRAPH instance data block has been created.
- GRAPH instance data block contains at least one tag which is visible in HMI and accessible from HMI.

  > **Note**
  >
  > The process tag you are using for the GRAPH overview must be visible in HMI and accessible from HMI.
  >
  > To identify the tags of the GRAPH data block as visible and accessible for HMI, open the GRAPH function block, select the block in the work area, and select "Edit > Internal parameters visible/accessible from HMI" in the menu bar. Then compile the program blocks.
- An HMI device has been created.
- You have created a screen.
- The Inspector window is open.

##### Procedure

1. Drag-and-drop the GRAPH overview from the toolbox view into the configured screen.
2. In the Inspector window, click "Properties > Properties > Miscellaneous".
3. Open the selection button under "PLC Source > Tag".

   The "Add new object" dialog opens.
4. Select the corresponding PLC in the "Program blocks" folder.
5. Select the corresponding PLC tag of the GRAPH instance data block.
6. To display the GRAPH overview in compatibility mode without function bar buttons and operating mode display, drag the object to the desired size, whereby multiple basic views are possible.
7. Under "Properties > Properties > Miscellaneous > Function bar > Elements", specify the buttons to be displayed in the object.

   ![Procedure](images/159222117899_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/159222117899_DV_resource.Stream@PNG-en-US.png)
8. Under "Properties > Events", you can assign system functions or scripts to the buttons in the GRAPH overview in order, for example, to jump to the alarm control or the PLC code view in Runtime and to open the TIA Portal.

**Note**

If no connection was configured between the HMI device and the selected PLC, a connection is set up automatically.

In addition, an HMI tag is created which is connected to the PLC tag.

##### Result

The GRAPH overview is inserted in the screen. The current status of the GRAPH step sequence is displayed in Runtime.

---

**See also**

[GRAPH overview](#graph-overview)

#### PLC code view (RT Unified)

##### Use

The "PLC code view" object is used to display the current program status of user programs that have been programmed in the LAD, FBD or GRAPH graphic programming languages.

A variety of information about the user program is displayed in the PLC code view:

- Information area
- Symbol line
- Detail view
- Transition/Interlock view

![Use](images/162821795211_DV_resource.Stream@PNG-en-US.png)

##### Layout

In the Inspector window, you can change the settings for the position, geometry, style, and color of the object. You can adapt the following properties in particular:

- "Function bar": Specifies the buttons of the PLC code view control.
- "Symbol line": Shows information about the first or the selected icon.

##### Information area

In the information area of the PLC code view, you are shown:

- In the left area, the GRAPH sequence.
- In the right area, the details, e.g. for the step or for the transition. In the ProDiag view, the networks to the supervised operands are displayed in this area.

##### Buttons of the function bar

You can define the buttons of the PLC code view control in runtime along with their operator authorizations in the Inspector window under "Properties > Properties > Miscellaneous > Function bar > Elements". Some buttons are enabled by default. To display additional buttons in the object, activate the "Visibility" property in the settings of the corresponding button.

The following buttons are available for the PLC code view:

| Button |  | Function |
| --- | --- | --- |
| ![Buttons of the function bar](images/162823707019_DV_resource.Stream@PNG-de-DE.png) | Previous | Navigates to the previous sequence / previous network. |
| ![Buttons of the function bar](images/162823710987_DV_resource.Stream@PNG-de-DE.png) | Continue | Navigates to the next sequence / next network. |
| ![Buttons of the function bar](images/162823714955_DV_resource.Stream@PNG-de-DE.png) | Zoom in | Enlarges the information area. |
| ![Buttons of the function bar](images/162823757323_DV_resource.Stream@PNG-de-DE.png) | Zoom out | Reduces the information area. |
| ![Buttons of the function bar](images/162823761291_DV_resource.Stream@PNG-de-DE.png) | Toggle GRAPH mode | Switches between manual and automatic step selection for the active step. |
| ![Buttons of the function bar](images/162823765259_DV_resource.Stream@PNG-de-DE.png) | Toggle detail view | 1. GRAPH view: Switches between the transition and interlock networks.  2. ProDiag view: Switches between network and the whole block. |
| ![Buttons of the function bar](images/162825361163_DV_resource.Stream@PNG-de-DE.png) | Toggle criteria analysis | Switches between the network view including criteria analysis and the standard network display without criteria analysis. |

#### Configuring the PLC code view

##### Introduction

To display the PLC program networks in the graphic programming languages LAD, FBD and GRAPH in Runtime, insert a PLC code viewer control into your project.

##### Requirement

- At least one PLC has been created.
- An HMI device has been created.
- An HMI connection has been established between the controller and HMI device.
- The process diagnosis is activated on the HMI device.
- You have created a screen.

##### Procedure

1. Drag-and-drop the PLC code view control from the toolbox view.
2. In the Inspector window, click "Properties > Properties > Function bar".
3. Select the buttons that you require in Runtime, for example: Back, Next, Zoom in.

   ![Procedure](images/164407799563_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/164407799563_DV_resource.Stream@PNG-en-US.png)

##### Result

The PLC code view is inserted in the screen. In Runtime, PLC user programs can be displayed that are programmed in the graphic programming languages LAD and FBD as well as GRAPH.

You can populate the PLC code viewer using system functions, e.g. jump from the GRAPH overview or from the alarm, or you can select the corresponding parameters directly.

---

**See also**

[PLC code view (RT Unified)](#plc-code-view-rt-unified)
  
[OpenViewGRAPHByBlock (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#openviewgraphbyblock-rt-unified)
  
[OpenGRAPHViewFromOverview (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#opengraphviewfromoverview-rt-unified)
  
[OpenPLCCodeViewByAlarm (RT Unified)](Using%20system%20functions%20%28RT%20Unified%29.md#openplccodeviewbyalarm-rt-unified)

#### ProDiag overview

##### Use

The "ProDiag overview" object provides an overview of the current status of the configured monitoring in Runtime.

When an error occurs, the type of error and the error category are determined in the ProDiag overview. You can navigate directly to the alarm control to find the error and you can jump from the corresponding alarm to the PLC code viewer control. You can display the affected program code in the PLC code viewer control.

![Use](images/164456222219_DV_resource.Stream@PNG-en-US.png)

The "ProDiag overview" object is available for WinCC Unified.

##### Layout

In the Inspector window, you customize the position, geometry, style, color and font types of the object. You can adapt the following properties in particular:

- Displayed buttons
- Names and colors for categories
- Names and colors for monitoring types

##### Monitoring types and categories

You can display a maximum of 8 categories and 6 monitoring types in the "ProDiag overview" object. The following pre-defined categories and monitoring types are available:

| Designation | Categories |
| --- | --- |
| E (Error) | Error |
| W (Warning) | Warning |
| I (Info) | Information |
| C4 ... C8 | Additional categories |

Rename the categories C4 to C8, which are created by default, according to your requirements.

| Designation | Monitoring type |
| --- | --- |
| O (Operand) | Operand error |
| I (Interlock) | Interlock error |
| R (Reaction) | Reaction error |
| A (Action) | Action error |
| P (Position) | Position error |
| M (Message error) | Alarm |

You can change display symbols of the supervision types and categories at any time in the Inspector window under "Miscellaneous".

##### Symbols

The icons displayed in the ProDiag overview are fixed.

| Icon | Name | Function |
| --- | --- | --- |
| ![Symbols](images/80801398795_DV_resource.Stream@PNG-de-DE.png) | Error | Indicates that an error has occurred. |

##### "Jump to Alarm Control" button

The "Jump to Alarm Control" button in the ProDiag overview is activated by default.

| Button | Name | Function |
| --- | --- | --- |
| !["Jump to Alarm Control" button](images/164643614091_DV_resource.Stream@PNG-de-DE.png) | Jump to Alarm Control | Opens the configured alarm control with the error message after system functions or scripts have been assigned to the button. |

##### Deactivated display

If there is a faulty connection to the controller during runtime, the object "ProDiag overview" is displayed grayed-out (unavailable). This deactivated display can be due to the following:

- The controller is deactivated
- The configured ProDiag program block was removed from the control program
- The controller is in Stop mode

As soon as the cause of the error is removed and the connection reestablished, the ProDiag overview shows the current online status of the monitoring during runtime.

#### Configuring the ProDiag overview

##### Introduction

The ProDiag overview is used to monitor your machine or system at runtime and determination of diagnostic information in the event of a fault occurring.

Once you have set the status tag in the object and the connection to a ProDiag FB has been established, the status of the "State" status tag of the corresponding PLC data type is queried. In Runtime, the states of the monitored operands are represented as symbols in the ProDiag overview, similar to a traffic light colors.

In WinCC, you configure the display and the representation of categories and supervision types that are displayed in the "ProDiag overview" object independent of the supervision settings in STEP 7.

##### Requirements

- At least one S7-1500 controller has been created.
- At least one supervision instance has been configured.
- A ProDiag FB and ProDiag DB are available.
- A PC station or an HMI device that supports the ProDiag functionality has been created.
- An HMI connection has been established between the controller and HMI device.
- An screen is created and the Inspector window is open.

##### Procedure

1. Drag-and-drop the ProDiag overview from the toolbox view.
2. In the Inspector window, select "Properties > Properties > General".
3. Open the selection button under the "Tag" property.
4. Select the status tag of ProDiag FB.

   Alternatively, you can add the corresponding status tags from the detail view using drag-and-drop.

   ![Procedure](images/164610422411_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/164610422411_DV_resource.Stream@PNG-en-US.png)
5. Under "Properties > Properties > Miscellaneous > P Diag Categories", define the names and colors for the supervision categories.
6. Under "Properties > Properties > Miscellaneous > P Diag Supervision types", define the names and colors for the supervision types.
7. Under "Properties > Events", you can configure a system function for the "Alarm view - Button tapped" event to jump from the ProDiag overview to the alarm view in Runtime.

##### Result

The ProDiag overview is inserted in the screen. The current states of the supervised events are displayed in Runtime.

---

**See also**

[ProDiag overview](#prodiag-overview)

#### Initial value acquisition and criteria analysis (RT Unified)

This section contains information on the following topics:

- [Overview of initial value acquisition and criteria analysis (RT Unified)](#overview-of-initial-value-acquisition-and-criteria-analysis-rt-unified)
- [Supported instructions (RT Unified)](#supported-instructions-rt-unified)
- [Criteria analysis view](#criteria-analysis-view)
- [Configuring the criteria analysis view](#configuring-the-criteria-analysis-view)
- [Outputting alarms with criteria (RT Unified)](#outputting-alarms-with-criteria-rt-unified)
- [Criteria analysis in the "GRAPH overview" object](#criteria-analysis-in-the-graph-overview-object)

##### Overview of initial value acquisition and criteria analysis (RT Unified)

###### Introduction

In the TIA Portal you have the option of testing the execution of your user program on the HMI device. The data and values on the HMI device are continuously synchronized with the PLC and updated. You therefore see the current program status with the actual values of the signal states on the HMI device.

If an error occurs in your plant, you have the option of jumping to the program code from the corresponding error message and displaying the error location in the network in the “PLC code view". In the "Criteria analysis view" object, you see the faulty operands for a selected GRAPH alarm or ProDiag alarm at a glance.

The initial value acquisition and criteria analysis functions enable you to record the values at the time of the error and to quickly identify the faulty operands in the program.

The actual value acquisition and criteria analysis functions are available for GRAPH function blocks, ProDiag function blocks and safety programs (F-blocks).

###### Requirement

- The initial value acquisition is available in WinCC Unified Runtime for the following blocks:

  - For the GRAPH function blocks as of version 6.0.
  - For the ProDiag function blocks as of version 2.0.
- Maximum of 32 statuses can be recorded. The initial values for a network that contains more than 32 elements are not recorded.

###### Initial value acquisition

With the help of initial value acquisition you can acquire the values at the time of the error in the PLC, display them in the PLC code view and compare them with the actual values. With initial value acquisition you continuously record the signal states of Boolean operands and results of comparators in transitions and interlocks.

The signal states are recorded in a defined order from top left to bottom right:

![Initial value acquisition](images/95190347147_DV_resource.Stream@PNG-de-DE.png)

You activate initial value acquisition individually for each GRAPH block in the user program. A maximum of 32 signal states of Boolean operands can be recorded per interlock or per transition of a GRAPH step. Each individual signal state occupies one bit. The values are saved in a DWORD.

In the following example you can see the principle and order in which the initial values are recorded in the interlock:

![Initial value acquisition](images/95015296267_DV_resource.Stream@PNG-de-DE.png)

###### Criteria analysis

Initial value acquisition in the PLC enables the analysis of criteria and operands with error in the program. You see the evaluation of the criteria analysis on your HMI in the PLC code view. In addition, in the "Criteria analysis view" object, you can use the criteria analysis to have the faulty operands displayed for a selected GRAPH alarm or ProDiag alarm.

> **Note**
>
> If the upstream network has been changed, the alarm is not be triggered again. This leads to inconsistencies between the network and faulty operands. As a result, the criteria analysis view cannot correctly display the faulty operands. If the alarm is triggered again, the faulty operands are displayed correctly again in the criteria analysis view.

For the blocks for which you have activated initial value acquisition, after the jump the initial value view is displayed by default in the PLC code view. In addition, the operands with error and criteria are highlighted visually in the initial value view.

All information about the selected operand can be seen in one line of the PLC code view.

In the event of an error in a comparator, both operands are marked as having errors. Only the recorded values are shown in the initial value view. To see the actual values of the tags, change to the actual value view.

##### Supported instructions (RT Unified)

###### Introduction

You see the initial values and the results of the criteria analysis in the "PLC code view" object.

For global supervisions, the initial values of all Boolean operands in the network are recorded. If the network contains multiple individual power rails that are not connected to each other, only the initial values of the respective power rail are recorded.

For local supervisions, only the initial values that are specified as conditions for the supervised parameter for the block call are recorded.

###### Supported instructions

The following instructions are supported in LAD and FBD for initial value acquisition:

| Instructions | Display on the HMI device |
| --- | --- |
| **Bit logic operations** |  |
| Normally open contact | Initial values and criteria analysis |
| Normally closed contact |  |
| Invert RLO | The instruction is supported but it is not relevant for initial values or the criteria analysis. |
| Assignment |  |
| Negate assignment |  |
| Reset output | Initial values |
| Set output |  |
| Set/reset flip-flop | Initial values and criteria analysis up to and including the instruction box |
| Reset/set flip-flop |  |
| **Comparator operations** |  |
| Equal | Initial values and criteria analysis |
| Not equal |  |
| Greater or equal |  |
| Less or equal |  |
| Greater than |  |
| Less than |  |
| **Timers** |  |
| TP | Initial values and criteria analysis up to and including the instruction box |
| TON | Initial values and criteria analysis |
| TOF | Initial values and criteria analysis up to and including the instruction box |
| TONR |  |
| **Counters** |  |
| CTU | Initial values and criteria analysis up to and including the instruction box |
| CTD |  |
| CTUD |  |

For bit logic operations, the status of the operand is recorded. For comparators, the result of the comparison is recorded.

For flip-flops, both inputs (R and S) are recorded if they are interconnected.

For timers and counters, the status of the operand at the output, and the inputs if they are interconnected, are recorded. (For example, for CTUD: CU, CD, R, LD)

The FBD instructions AND and OR are also supported for initial value acquisition and criteria analysis. The FBD instruction EXCLUSIVE OR is not supported by the initial value acquisition and criteria analysis.

##### Criteria analysis view

###### Use

The "Criteria analysis view" object shows you the faulty operands in the user program that have triggered a selected ProDiag alarm or GRAPH alarm. As a result, you have the option of seeing the list of faulty operands in addition to the alarm in the same screen.

To see the evaluation of the criteria analysis in the "Criteria analysis view" object in Runtime, select the initial value acquisition in the settings of the function blocks in the user program. The initial value acquisition is available for GRAPH function blocks as of version 6.0 and ProDiag function blocks as of version 2.0.

To enable the link to the corresponding error message, configure a reference to a previously configured alarm control. If you select a GRAPH alarm or a ProDiag alarm in the alarm control in Runtime, then the name, address, comment and value of the operand that caused this error is displayed in the criteria analysis view.

![Use](images/172315208331_DV_resource.Stream@PNG-de-DE.png)

You see the incoming alarms and the faulty operands at a glance in Runtime if you configure the criteria analysis view and its linked alarm control in the same screen.

> **Note**
>
> Criteria analysis is only available for the user programs for which initial value acquisition has been activated.
>
> Activate initial value acquisition in the properties of the following blocks:
>
> - ProDiag function blocks with version greater than or equal to V2.0
> - GRAPH function blocks with version greater than or equal to 6.0

###### Layout

You change the settings for the position, style, colors, and fonts of the object in the Inspector window.

###### Columns

The following columns are displayed in the criteria analysis view in Runtime.

| Column | Description |
| --- | --- |
| Symbol name | Symbolic name of the operand in the user program. |
| Address | Absolute address of the operand. |
| Value | The value of the operand at the time of the error. |
| Comment | Additional comments from the user program in the language that is loaded into the controller. |

---

**See also**

[Configuring the criteria analysis view](Using%20the%20diagnostics%20functions%20%28RT%20Unified%29.md#configuring-the-criteria-analysis-view)

##### Configuring the criteria analysis view

###### "Criteria analysis view" object

The "Criteria analysis view" object shows you the faulty operands in the user program that have triggered a selected ProDiag alarm or GRAPH alarm. It is used to list the initial values in a separate view in order to obtain an overview of the fault status of the plant.

If you select the incoming ProDiag alarm or GRAPH alarm in the alarm control in Runtime, you see the operands that were determined in the criteria analysis view.

You configure the criteria analysis view and its linked alarm control in the same screen.

###### Requirement

- The HMI device is connected to the controller.
- A ProDiag program version 2.0 or a GRAPH program Version 6.0 or higher is installed on the controller.
- Process diagnostics is enabled in the "Runtime settings > Process diagnostics > General" of the Unified Runtime device.
- Initial value acquisition is enabled for the function blocks.
- An alarm control has been configured.

###### Procedure

1. Move the criteria analysis view from the toolbox window using drag-and-drop.
2. Click on "Properties > Properties" in the Inspector window.
3. Open the selection button under the "Data source" property.
4. Select the configured alarm control.

   ![Procedure](images/169740338059_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/169740338059_DV_resource.Stream@PNG-en-US.png)

###### Result

The criteria analysis view is configured in the screen and connected to the alarm control. For a selected alarm you can see detailed information in Runtime about that operands that triggered this alarm.

##### Outputting alarms with criteria (RT Unified)

###### Introduction

When initial value acquisition is activated, the values of the faulty operands are recorded at the time of the error and missing criteria are analyzed and determined.

You have the option to add additional information about faulty operands to the GRAPH and ProDiag alarms and output them on your HMI device. If an error occurs in the program flow in runtime, the error message also indicates the faulty operands in the faulty network. You see detailed information on all operands with error of the error message in the "Criteria analysis view" object.

![Introduction](images/110359669003_DV_resource.Stream@PNG-en-US.png)

In WinCC Unified Runtime, you have the option to add additional information to the alarms. For this, select the appropriate text that you want to extend under "Runtime settings > Process diagnostics > Criteria analysis > Extend text", i.e. alarm text, info text or additional text 1 - 9. You can extend the texts with the first faulty operand or with all faulty operands.

The following information can be added to the operands:

- Symbol: The symbolic name of the first or all faulty operands.
- Absolute address: The address of the first or all faulty operands.
- Value: The value of the first or all faulty operands at the time of the fault.
- Comment: Multilingual comments that were configured in the user program.

The additional information is separated in the alarm by semicolons and spaces.

> **Note**
>
> The order of the additional information that is added to the alarm is predefined and cannot be changed.

> **Note**
>
> To completely display the alarms from the controller on the HMI device, the "Automatic update" option must be selected under "Runtime settings > Alarms > Controller alarms" for the relevant connection. You can find additional information on complete alarms under "[Sending a complete alarm from the controller to the HMI device](Configuring%20alarms%20%28RT%20Unified%29.md#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)".

###### Criteria analysis in the alarm system

You visualize the alarms for the criteria analysis in the following steps:

- You enable the initial value acquisition in the properties of the ProDiag function block or GRAPH function block of the user program
- You enable the options to extend the alarm texts or info texts in the runtime settings of the HMI device

###### Extend alarms

1. Open the "Runtime settings" editor of the HMI device.
2. Click "Process diagnostics > Criteria analysis".
3. Under "Criteria analysis > Extend text", select which texts you want to extend.
4. Select the additional information to be added to the alarm text in the alarm, such as symbol name, address and value of the first faulty operand and comment.

   ![Extend alarms](images/169740348171_DV_resource.Stream@PNG-en-US.png)

   ![Extend alarms](images/169740348171_DV_resource.Stream@PNG-en-US.png)

###### Result

If an error occurs, you see not only the alarm text in the alarm control but also the operands that triggered the error message.

---

**See also**

[Sending complete alarms from the controller to the HMI device and automatically updating them (RT Unified)](Configuring%20alarms%20%28RT%20Unified%29.md#sending-complete-alarms-from-the-controller-to-the-hmi-device-and-automatically-updating-them-rt-unified)

##### Criteria analysis in the "GRAPH overview" object

###### Extension of the "GRAPH overview" object with the criteria analysis

To display the criteria analysis in the "GRAPH overview" object, the criteria analysis must be enabled in the Inspector window under "Properties > Properties > Information bar > Elements".

![Extension of the "GRAPH overview" object with the criteria analysis](images/171168840459_DV_resource.Stream@PNG-en-US.png)

###### Result

In runtime, the information bar of the "GRAPH overview" object displays the symbolic name of the 1st faulty operand.

![Result](images/172315199499_DV_resource.Stream@PNG-de-DE.png)

## Elements (RT Unified)

This section contains information on the following topics:

- [Overview of elements (RT Unified)](#overview-of-elements-rt-unified)
- [Using elements (RT Unified)](#using-elements-rt-unified)

### Overview of elements (RT Unified)

Operable elements are available in process pictures in Runtime.

The following elements are available depending on the configured access rights:

| Icon | Element | Brief description |
| --- | --- | --- |
| ![Figure](images/100853481867_DV_resource.Stream@PNG-de-DE.png) | Bar | Represents tags graphically. The bar graph can be labeled with a value scale. |
| ![Figure](images/100853909131_DV_resource.Stream@PNG-de-DE.png) | I/O field | Used for entry and display of process values. |
| ![Figure](images/152318614923_DV_resource.Stream@PNG-de-DE.png) | Symbolic I/O field | A drop-down list with texts or graphics for display and input in runtime. |
| ![Figure](images/100854098059_DV_resource.Stream@PNG-de-DE.png) | Check box | Used for display and selection of multiple options. |
| ![Figure](images/100854106891_DV_resource.Stream@PNG-de-DE.png) | List box | Used for display and selection of multiple list entries. |
| ![Figure](images/100854166923_DV_resource.Stream@PNG-de-DE.png) | Radio button | Used for display and selection of various options of which only one can be selected. |
| ![Figure](images/118530845579_DV_resource.Stream@PNG-de-DE.png) | Switch | Used for toggling between two predefined states. |
| ![Figure](images/100854184587_DV_resource.Stream@PNG-de-DE.png) | Button | Executes a configured function. |
| ![Figure](images/100854219019_DV_resource.Stream@PNG-de-DE.png) | Slider | Used for monitoring and changing process values within a defined range and adjusts them. By adjusting the slider, you intervene in the process and correct the displayed process value. |
| ![Figure](images/100854386315_DV_resource.Stream@PNG-de-DE.png) | Clock | Used for display of date and time. |
| ![Figure](images/100854523147_DV_resource.Stream@PNG-de-DE.png) | Gauge | Represents numerical values in the form of an analog gauge. For example, it can be seen at a glance whether the boiler pressure is in the normal range. |

### Using elements (RT Unified)

This section contains information on the following topics:

- [Bar (RT Unified)](#bar-rt-unified)
- [IO field (RT Unified)](#io-field-rt-unified)
- [Symbolic IO field (RT Unified)](#symbolic-io-field-rt-unified)
- [Check box (RT Unified)](#check-box-rt-unified)
- [List box (RT Unified)](#list-box-rt-unified)
- [Option buttons (RT Unified)](#option-buttons-rt-unified)
- [Switch](#switch)
- [Button](#button)
- [Slider (RT Unified)](#slider-rt-unified)
- [Clock (RT Unified)](#clock-rt-unified)
- [Gauge (RT Unified)](#gauge-rt-unified)

#### Bar (RT Unified)

##### Application

The tags are displayed graphically with the "Bar" object. The bar graph can be labeled with a value scale.

![Application](images/105847980171_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, colors and fonts of the object are made during configuration.

In particular, the following properties are changed:

- Color transition: Specifies the change in color display when limit values are exceeded.
- Limit marking: Displays the configured limit value as an arrow.
- Bar segments: Defines the gradations on the bar scale.
- Scale gradation: Defines the position of the zero point on a bar scale.

If the object falls below a certain size in the light or dark style, it is automatically displayed in compact mode.

##### Color transition

The display of the color change is specified during configuration.

| Color transition | Description |
| --- | --- |
| "Segmented" | If a particular limit was reached, the bar changes color segment by segment. With segmented display, for example, the limits exceeded by the displayed value are visualized. |
| "Entire bar" | If a particular limit was reached, the entire bar changes color. |

#### IO field (RT Unified)

##### Use

The "I/O field" object is used to enter and display process values.

![Use](images/105848785547_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, color and fonts of the object are made during configuration.

In particular, the following properties are changed:

- Mode: Specifies the behavior of the object in Runtime.
- Display format: Specifies the display format in the I/O field for input and output of values.
- Hidden input: Specifies whether the input value is displayed normally or encrypted during input.

  > **Note**
  >
  > **Reports**
  >
  > In reports, I/O fields only output data. "Output" mode is preset. Properties for configuring input are not available, e.g. "hidden input".

##### Mode

The behavior of the I/O field is specified during configuration.

| Mode | Description |
| --- | --- |
| "Input/output" | Values can be input and output in the I/O field. |
| "Output" | The I/O field is used for the output of values only. |

##### Layout

The "display format" for the input and output of values is specified during configuration.

| Layout |  |
| --- | --- |
| "Binary" | Input and output of values in binary form |
| "Date" | Input and output of date information. The format depends on the language setting on the HMI device. |
| "Date/time" | Input and output of date and time information. The format depends on the language setting on the HMI device. |
| "Decimal" | Input and output of values in decimal form |
| "Hexadecimal" | Input and output of values in hexadecimal form |
| "Time" | Input and output of times. The format depends on the language setting on the HMI device. |
| "Character string" | Input and output of character strings. |

##### Hidden input

In Runtime the input can be displayed normally or encrypted, for example for hidden input of a password. A "*" is displayed for every character during hidden input. The data format of the value entered cannot be recognized.

##### Avoid overlaps in output fields

If several I/O fields are configured as output fields with a transparent background in a screen, these I/O fields may overlap. The transparent part of the one field covers the digits of the other field. This may cause display problems. In order to avoid such overlaps, the border of the I/O fields must be set to zero during configuration.

##### Limits

During configuration, colors can be specified for the values that exceed or fall below limits.

When there is a limit violation, the background color of the I/O field changes according to the configuration, even if the I/O field is in input mode.

A limit range can also be defined for the input in the I/O field for the configuration.

If you enter a numeric value outside this limit, it is not applied; for example, 80 with a limit of 78. In this case, a system alarm is generated on the HMI device if an alarm window is configured. The original value is displayed again.

##### Decimal places for numerical values

The number of decimal places can be specified for a numerical input field during configuration. The number of decimal places is checked when you enter a value in this type of I/O field. Decimal places in excess of the limit are ignored. Empty decimal places are filled with "0".

In the exponential display, the displayed numerical value is represented with a maximum precision of nine decimal places.

##### Setting an LTime PLC tag via HMI

S7-1500 tags with data type LTime have the unit nanoseconds (ns). IO fields that are linked with such a PLC tag have the unit 100 ns.

HMI user inputs to the I/O field are converted to ns when the value is sent to the PLC.

> **Note**
>
> **MAX_SAFE_INTEGER**
>
> Depending on the JavaScript engine of the web client, the actual value may lose accuracy during communication between the HMI device and the controller due to rounding if it is outside the value range of MAX_SAFE_INTEGER.
>
> Additional information on MAX_SAFE_INTEGER can be found [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Number/MAX_SAFE_INTEGER).

##### Behavior when switching between input fields

When you change from one input field to another within a screen due to an operator input and the on-screen keyboard appears, the "Exit field" event is not immediately triggered for the previous field. Rather, it is only triggered after the on-screen keyboard is closed.

##### No events during the input

While an I/O field is in input mode, no events are transmitted to the server for the I/O field.

Terminate the input mode with Enter or Esc so that the events configured for the I/O field in engineering take effect again.

#### Symbolic IO field (RT Unified)

##### Use

The "Symbolic I/O field" list is used for displaying texts and graphics in runtime as well as text input, if configured.

The displayed texts or graphics are assigned to the potential tag values.

![Use](images/162573536267_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> Selecting the default entry is not possible in runtime.

##### Layout

The settings for the position, geometry, style, color and fonts of the object are made during configuration.

In particular, the following properties are changed:

- "Mode": Specifies the response of the object in runtime.
- "Resource list": Specifies the text or graphic list that will be associated with the object.

##### Mode

The behavior of the symbolic I/O field is specified during configuration.

| Mode | Description |
| --- | --- |
| "Output" | The symbolic IO field is used for the output of values. |
| "Input/output" | The symbolic IO field is used for the input and output of values. |

#### Check box (RT Unified)

##### Application

You use the "Checkbox" object to select multiple options. Checkboxes can be activated by default so that the user changes the default values only as required. Multiple options can be selected if the corresponding properties are dynamized.

![Application](images/105848805771_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, color and fonts of the object are made during configuration.

In particular, the following properties are changed:

- Number of the checkboxes: Defines the number of options.
- Selection of the checkboxes: Defines which options are displayed as activated by default.

##### Default setting of the checkboxes

Each option is represented by a bit in a 32-bit word. To activate a field, the corresponding bit must have the value "1". The 32-bit word contains the information for all options of the checkbox list. The value of the "Presetting enabled" property is specified in hexadecimal format.

#### List box (RT Unified)

##### Application

You use the "List box" object to present and select multiple list entries. List entries are selected by default so that the default setting can be changed only when necessary. If the list box is larger than the selection rectangle, WinCC automatically adds a scroll bar to the right margin.

![Application](images/105848908171_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, color and fonts of the object are made during configuration.

In particular, the following properties are changed:

- Number of entries: Defines the number of list entries.
- Selection of entries: Defines which entry is displayed as activated by default.

##### Default setting of the list boxes

Each option is represented by a bit in a 32-bit word. To activate a field, the corresponding bit must have the value "1". The 32-bit word contains the information for all texts of the list of list boxes. The value of the "Selected fields" property is given in hexadecimal notation.

#### Option buttons (RT Unified)

##### Application

You use the "Option button" object for selection of various options. Options are selected by default so that the default setting can be changed only when necessary. Only one option can be selected if the corresponding property is dynamized.

![Application](images/105849112587_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, color and fonts of the object are made during configuration.

In particular, the following properties are changed:

- Number of fields
- Selection of the fields: Specifies which fields are displayed as activated.

#### Switch

##### Application

With the "Switch" object you switch between two predefined states. The current state of the "Switch" object is visualized with either a label or a graphic.

![Application](images/105849148043_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, color and fonts of the object are made during configuration.

In particular, the following property is changed:

- Type: Defines the graphic representation of the object.

##### Type

The display of the switch is specified during configuration.

| Type | Description |
| --- | --- |
| "Switch" | The two states of the "Switch" are displayed in the form of a switch. The position of the switch indicates the current state. The switch is switched by moving it. |
| "Switch with text" | The switch is shown as a button. The current state is visualized with a label. The switch is switched by clicking the button. |
| "Switch with graphic" | The switch is shown as a button. The current state is visualized with a graphic. The switch is switched by clicking the button. |

#### Button

##### Use

With the "Button" object, you execute a configured function.

![Use](images/105849460235_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, color and font of the object are made during configuration.

In particular, the following properties are changed:

- Mode: Defines the graphic representation of the object.
- Text / Graphic: Defines whether the Graphic view is static or dynamic.
- Define hotkey: Defines a key, or shortcut that the operator can use to actuate the button.

  > **Note**
  >
  > You can only define a hotkey for HMI devices with keys.

##### Mode

The display of the button is specified during configuration.

| Mode | Description |
| --- | --- |
| "Invisible" | The button is not visible. |
| "Text" | The button is displayed with text. This text explains the function of the button. |
| "Graphic" | The button is displayed with a graphic. This graphic represents the function of the button. |
| "Graphic or text" | The button is displayed with text or graphics.  If the graphic cannot be displayed, the corresponding text is displayed. |
| "Graphic and text" | The button is displayed with text and graphic. |

Different options are available depending on the device.

##### Text / Graphic

Depending on the "Mode" property, the display can be specified as a static or dynamic display. The display is specified during configuration.

You can, for example, select the following options for the "Graphic" or "Text" type.

| Type | Option | Description |
| --- | --- | --- |
| "Graphic" | "Graphic" | With "Graphic when button "not pressed"", a graphic is specified that is displayed in the button for the "OFF" state.  When "Graphic when button "pressed"" is selected, a graphic for the "ON" state can be entered. |
| "Graphics list" | The graphic in the button depends on the state. The corresponding entry from the graphics list is displayed depending on the state. |  |
| "Text" | "Text" | With "Text when button "not pressed"", a text is specified that is displayed in the button for the "OFF" state.  When "Text when button "pressed"" is selected, a text for the "ON" state can be entered. |
| "Text list" | The text in the button depends on the state. The entry from the text list corresponding to the state is displayed. |  |

##### Hotkey

A key or key combination that the operator can use to actuate the button can be defined during configuration.

#### Slider (RT Unified)

##### Use

Process values are monitored and adapted within a defined range with the "Slider" object. The monitored range is visualized in the form of a slider. By adjusting the slider, you intervene in the process and correct the displayed process value.

![Use](images/105849539851_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, color and fonts of the object are made during configuration.

In particular, the following properties are changed:

- Maximum Value and Minimum Value: Specifies the top and bottom values of the scale.
- Display current value: Specifies whether the current position of the controller appears below the slider.
- Display of bars: The sliders above and below the bar can be hidden.
- You can represent limits and ranges in different colors. The colors are defined during configuration.

If the object falls below a certain size in the light or dark style, it is automatically displayed in compact mode.

##### Behavior during operation

The displayed value on the slider control may deviate from the actual value of the associated tag in the following circumstances:

- The value range (minimum and maximum value) configured for the slider control does not correspond to the configured limits for the slider control tag.
- An invalid password has been entered for a password-protected slider control.

#### Clock (RT Unified)

##### Use

The "Clock" object displays the date and time.

![Use](images/118533042187_DV_resource.Stream@PNG-de-DE.png)

By default, the "Clock" object displays the date and time of the client.

If the "Process value" property of the clock is connected to a DateTime tag, the clock uses the tag value as a start value and continues counting. When the tag value is changed, the clock is synchronized and continues counting from the new value.

##### Layout

The display of the clock is configured in the engineering, for example:

- Whether hour markers are displayed as graduation marks or numbers.
- Whether hour hand, minute hand and second hand are displayed.

When the object in the light or dark style is less than 100 pixels high or wide in runtime, the clock is automatically displayed in compact mode.

#### Gauge (RT Unified)

##### Use

The "Gauge" object shows numeric values in the form of an analog gauge. For example, it can be seen at a glance whether the boiler pressure is in the normal range.

> **Note**
>
> The gauge is for display only and cannot be controlled by the operator.

![Use](images/105849678603_DV_resource.Stream@PNG-de-DE.png)

##### Layout

The settings for the position, geometry, style, color and fonts of the object are made during configuration.

In particular, the following properties are changed:

- Display peak value: Specifies whether the actual measuring range is indicated with a peak indicator.
- Maximum Value and Minimum Value: Specifies the top and bottom values of the scale.
- Start value of the danger range and start value of the warning range: Specifies the scale value from which the danger range and the warning range start.
- Display normal range: Specifies whether the normal range is shown in color on the scale.
- Color of individual ranges: Different operating modes, such as normal range, warning range and danger range, are shown in different colors so that the operator can distinguish them easily.

If the object falls below a certain size in the light or dark style, it is automatically displayed in compact mode.

> **Note**
>
> The use of many differently sized "Gauge" objects can reduce the performance in Runtime. With "Gauge", avoid minimally different heights and widths, for example, 48 pixels, 49 pixels, 51 pixels, etc. Use the same sizes instead.

##### Display peak value

The "Display peak value" property can be used to enable a marker function for the maximum and minimum pointer movement in Runtime. The actual measuring range is shown with a min/max pointer.

##### Color of individual ranges

The normal range, danger range and warning range can be displayed in different colors. The colors are defined during configuration.

## Basic objects (RT Unified)

In addition to controls and elements, HMI screens contain basic objects such as circles, polygons or text boxes. Basic objects are often used for design purposes, but can also provide information about the process.

Dynamically configured basic objects react to changes in the process or to operator actions. Example: In engineering, a text box is linked to a text list that defines text entries for the value range of a tag. In Runtime, the text box always shows the text assigned to the current tag value. When the tag changes its value, the content of the text box changes.

### Overview of basic objects

Depending on the configuration, screens can contain the following basic objects:

- Line
- Polyline
- Polygon
- Ellipse
- Ellipse segment
- Circle segment
- Elliptical arc
- Circular arc
- Circle
- Rectangle
- Text box
- Graphic view

### Process values in text fields

If a text box has been connected to a tag in engineering, the text box shows the process value of the tag in runtime.

If the text box was connected to a tag and a text list, the text box shows the text list entry that corresponds to the tag value.

> **Note**
>
> If no default value is assigned to the text list and the tag value is outside the defined value range of the text list, the last valid process value displayed by the text box is output.

## Popup window (RT Unified)

Popup windows are freely movable windows that open when an event configured in the engineering system occurs. They show, for example, additional information on a partial area of the process image.

You close a popup window using the button in the top right corner of the popup window.

### Example

Runtime shows a screen with an overview graphic for a pump and its valves.

**Configuration in the engineering system**

A faceplate instance was positioned on the screen for each valve, which is displayed by the graphic of the valve. The faceplate instances have a script that opens an additional faceplate instance in a popup window in Runtime. This second instance shows detailed information on the valve as well as input fields.

**Behavior in Runtime**

When you click on a valve in the overview graphic in the screen, a popup window opens. In the popup window, you can check the state of the valve and edit the valve using the input fields.

## Tests and error analysis (RT Unified)

This section contains information on the following topics:

- [Trace logs for function calls and tag values (RT Unified)](#trace-logs-for-function-calls-and-tag-values-rt-unified)
- [Debugging scripts (RT Unified)](#debugging-scripts-rt-unified)

### Trace logs for function calls and tag values (RT Unified)

WinCC Unified provides trace logging for error analysis. Tag values and function calls can be logged for test purposes and for troubleshooting with the trace.

All trace outputs with "Fatal", "Error" or "Warning" severity are stored in LOG files (.log) in the directory "%ProgramData%\Siemens\Automation\Logfiles\WinCC_Unified_SCADA_Vxx". In case of problems you must send these files to SIEMENS Customer Support.

#### TraceViewer

The LOG files can be viewed with the TraceViewer. It is located in the installation directory of WinCC Unified under "WinCCUnified\bin". To open the Trace Viewer start the file "RTILtraceViewer.exe".

![TraceViewer](images/102880705803_DV_resource.Stream@PNG-de-DE.png)

### Debugging scripts (RT Unified)

This section contains information on the following topics:

- [Basics of debugging (RT Unified)](#basics-of-debugging-rt-unified)
- [Design and function of the debugger (RT Unified)](#design-and-function-of-the-debugger-rt-unified)
- [Enabling the debugger (RT Unified)](#enabling-the-debugger-rt-unified)
- [Starting the debugger (RT Unified)](#starting-the-debugger-rt-unified)
- [Working with breakpoints (RT Unified)](#working-with-breakpoints-rt-unified)
- [Step-by-step execution of scripts (RT Unified)](#step-by-step-execution-of-scripts-rt-unified)
- [Show values (RT Unified)](#show-values-rt-unified)

#### Basics of debugging (RT Unified)

##### Introduction

For example, you can use a debugger to test whether correct values are being transferred to tags and whether abort conditions are being correctly implemented. Check the following in the debugger:

- Source code of functions
- Function sequence
- Values

> **Note**
>
> Your code is displayed in the debugger but is write-protected.

##### Basic procedure

To find an error, check the script with the debugger.

The following options are available for your support:

- Setting breakpoints
- Step-by-step execution
- Viewing values parallel to execution of the script

You do not edit the code of your scripts directly in the debugger. When you find an error, follow these steps:

1. Correct the error in the engineering system.
2. Compile the changed code.
3. Load the runtime.
4. Update the debugger.

#### Design and function of the debugger (RT Unified)

Google Chrome provides the user interface of the debugger. Not all functions of the user interface of the debugger are relevant for debugging WinCC Unified Scripts. Only the functions that are needed to debug scripts in WinCC Unified are explained below.

You can find more information on Chrome DevTools under: https://developers.google.com/web/tools/chrome-devtools/.

The debugger is divided into two areas:

- Debugger for screens
- Debugger for jobs

With the debugger for screens you view scripts at screens and screen objects. With the debugger for jobs, you view scripts that you have configured in the Scheduler.

##### Start page of the debugger

After the debugger has been started, its start page is displayed.

The available contents differ depending on the selected area.

On the start page of the debugger for screens you can see two different contexts:

- Dynamizations (e.g. "UMCadmin@192.168.116.144 VCS_1 Dynamics")
- Events (e.g. "UMCadmin@192.168.116.144 VCS_1 Events")

The name of the contexts is composed as follows:

- UMCadmin: User name
- 192.168.116.144: IP address of the computer
- VCS: Name of the graphic component
- _1: Number of the open client
- Events/Dynamics: Scripts at events or dynamizations

> **Note**
>
> A client corresponds to a tab in Google Chrome in which the runtime is open. When you have opened runtime in multiple tabs, multiple clients are used. The client opened first is given the number 1. Numbering is reset when the runtime is restarted.

On the start page of the debugger for jobs you can see the context "JobsExecution".

##### User interface of the debugger

![User interface of the debugger](images/133867069451_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Navigation area |
| ② | Code display area |
| ③ | Console |
| ④ | Debugging area |

##### Navigation area

In the navigation area, the available contents for the screen shown in runtime are displayed in groups. The available groups vary depending on the use of scripts and functions.

**Groups in the debugger for screens**

The debugger for screens can contain the following groups in the dynamizations context:

- A group for scripts that were configured for dynamizations.
- One group per screen window in which scripts were configured for dynamizations.

The debugger for screens can contain the following groups in the events context:

- A group for scripts that were configured for events.
- One group for functions that were configured for events using the function list.
- One group per screen window in which scripts were configured for events.
- One group per screen window in which functions were configured for events using the function list.

**Groups in the debugger for jobs**

The debugger for jobs can contain the following groups:

- A group for scripts that were configured for tasks.
- One group for functions that were configured for tasks using the function list.

##### Code display area

Your code is displayed in the code display area. The rows are numbered.

##### Debugging area

The debugging area offers the following relevant options for WinCC Unified:

- Toolbar: Control for executing the script
- "Watch": Display of values
- "Callstack": Display of the current call stack
- "Scope": Available local values ("Local"), functions ("Module") and global values ("Global"),
- "Breakpoints": List of set breakpoints

#### Enabling the debugger (RT Unified)

##### Requirement

- SIMATIC Runtime Manager is installed.
- The logged-on user belongs to the Windows user group "SIMATIC HMI".

> **Note**
>
> The debugger is only available locally.
>
> Remote access from the debugger to other devices is not possible.

##### Procedure

The debugger is disabled by default.

> **Note**
>
> The debugger should be disabled in production operation, as using the debugger can endanger system stability and security. Actions can accumulate if the debugger is, for example, at a breakpoint for a long time or the screen is not refreshed.

To enable the debugger, follow these steps:

1. Start the SIMATIC Runtime Manager application.
2. Click the ![Procedure](images/140347454603_DV_resource.Stream@PNG-de-DE.png) button in the toolbar.
3. Switch to the "Scripts Debugger" tab.
4. To enable the debugger for screens, select the "Enable" check box in the "Screen debugger" area.
5. To enable the debugger for scheduled tasks, select the "Enable" check box in the "Scheduler debugger" area.
6. Assign an available port number to the debugger for screens (default port number: 9222).
7. Assign an available port number to the debugger for jobs (default port number: 9224).
8. Confirm your entries.

> **Note**
>
> Start Runtime after enabling the debugger.

#### Starting the debugger (RT Unified)

##### Requirement

- Google Chrome (as of version 70) is installed.
- A project is opened in runtime.
- The debugger was activated in SIMATIC Runtime Manager.

> **Note**
>
> The debugger is only available locally.
>
> Remote access from the debugger to other devices is not possible.

##### Procedure

1. In a new tab, call up the URL chrome://inspect in Google Chrome.
2. The home page of the Chrome DevTools is loaded in the tab.
3. Click "Devices".
4. Select the "Discover network targets" check box.
5. Click "Configure".
6. In the "Target discovery settings" dialog box, enter one of the following strings:

   - `127.0.0.1:`
     `<Port number>`
   - `localhost:`
     `<Port number>`

   Use the port entered for the Script Debugger in SIMATIC Runtime Manager.
7. Press <Enter>.
8. Click "Done".
9. Under "Remote Target", click "inspect" for the desired target.

   The DevTools open in a separate window with the selected target.
10. In the DevTools, select "Sources".

    The debugger is displayed.
11. Click "Toggle screencast".
12. In the navigation area under "Page", select the desired script module.

##### Updating the debugger

The debugger must be updated:

- After starting a new project
- After restarting a running project, for example, because you have reloaded the project in engineering with "Download to device > Software (all)".
- After a screen change in Runtime

The connection to the debugger is lost in each case. Google Chrome therefore shows an error message and asks whether you want to restore the connection.

To restore the connection, proceed as follows:

1. Close the DevTools window.
2. On the DevTools start page under "Remote Target", click "inspect" again for the desired target.

##### Stopping the debugger

Exit the debugger by closing the DevTools window and, if necessary, the DevTools homepage.

This does not stop runtime.

#### Working with breakpoints (RT Unified)

Set breakpoints to stop the execution of the script at certain points and thus localize errors step-by-step. Previously set breakpoints are still available after updating the debugger.

##### Requirement

- Runtime has started.
- The debugger has been started.
- The group you want to debug is selected.

##### Pause script

To pause the execution of a script, you have 2 options:

- To pause the script immediately, click the ![Pause script](images/153087836939_DV_resource.Stream@PNG-de-DE.png) "Pause script execution" button while the script is being executed.
- Set a breakpoint in the desired line.

  The script pauses when a breakpoint is reached.

To pause a script at a breakpoint that is configured to an event, follow these steps:

1. Set a breakpoint in the script.
2. Trip the respective event in runtime.

   The script pauses at the breakpoint.

##### Setting breakpoints

You have several options to set a breakpoint in a line of the script:

- Click on the line number.
- Right-click the line number and select "Add Breakpoint".

All set breakpoints are displayed in the debugging area under "Breakpoints".

##### Linking breakpoints to conditions

To link a breakpoint to a condition, proceed as follows:

1. Open the shortcut menu of the relevant line.
2. Select the entry "Add conditional breakpoint".

   Execution of the script is stopped at the breakpoint when the condition is fulfilled.

Edit conditions as follows:

1. Open the shortcut menu of the relevant line.
2. Select the entry "Edit breakpoint...".

To prevent the script from pausing at a selected line, proceed as follows:

1. Open the shortcut menu of the respective line.
2. Select the entry "Never pause here".

##### Showing and hiding breakpoints

When you hide a breakpoint, its position is retained. The script then ignores the hidden breakpoint. When you need the breakpoint again, it can simply be shown.

In the debugging area, all breakpoints set in the selected group are displayed under "Breakpoints".

You have several options to show a breakpoint:

- Set the check mark in front of the relevant breakpoint in the debugging area under "Breakpoints".
- Alternatively, right-click the number of the respective line in the code display area and then select "Enable breakpoint".

You have several options to hide a breakpoint:

- Remove the check mark in front of the relevant breakpoint in debugging area under "Breakpoints".
- Alternatively, right-click the number of the respective line in the code display area and then select "Disable breakpoint".

To show or hide all breakpoints, follow these steps:

1. Open the shortcut menu in the debugging area under "Breakpoints".
2. Select "Enable all breakpoints" or "Disable all breakpoints"

##### Enabling and disabling breakpoints

You can enable or disable all breakpoints independent of showing or hiding individual breakpoints.

You have several options to enable or disable all breakpoints:

- Click on the ![Enabling and disabling breakpoints](images/153087832971_DV_resource.Stream@PNG-de-DE.png) "Deactivate breaktpoints" button in the debugging area.
- Open the shortcut menu of a breakpoint in the debugging area and select "Activate breakpoints" or "Deactivate breakpoints".
- Press <Ctrl + F8>.

##### Deleting breakpoints

You have several options to delete a breakpoint:

- Click on the breakpoint in the code display area.
- Open the shortcut menu of the breakpoint in the code display area and select "Remove breakpoint".
- Open the shortcut menu in the debugging area under "Breakpoints" and select "Remove breakpoint"..

To delete breakpoints, the shortcut menu offers the following additional options in the debugging area under "Breakpoints":

- Delete all breakpoints ("Remove all breakpoints​")
- Delete all breakpoints except the selected breakpoint ("Remove other breakpoints​")

#### Step-by-step execution of scripts (RT Unified)

##### Introduction

The following options are available to execute your script step-by-step:

- Execute script to the next breakpoint
- Force execution of a script
- Execute script to the next function call
- Jump into a function
- Jump out of a function
- Execute script up to a selected line
- Pause at Exceptions
- Use call stack

##### Requirement

- The group you want to debug is selected.
- The script pauses at a breakpoint.

##### Execute script to the next breakpoint

To pause the continuation of a script, you have several options:

- Click on the ![Execute script to the next breakpoint](images/153085429387_DV_resource.Stream@PNG-de-DE.png) "Resume script execution" button in the debugging area.
- Press the <F8> key.

  The script is executed to the next breakpoint. If there is no other breakpoint, the script is executed completely.

##### Force execution of a script

To ignore the following breakpoints when resuming execution of a paused script, proceed as follows:

1. Click and hold down the ![Force execution of a script](images/153085429387_DV_resource.Stream@PNG-de-DE.png) "Resume script execution" button.

   The ![Force execution of a script](images/153087788555_DV_resource.Stream@PNG-de-DE.png) "Force script execution" button appears.
2. Move the mouse pointer to the ![Force execution of a script](images/153087788555_DV_resource.Stream@PNG-de-DE.png) "Force script execution" button while keeping the mouse button pressed.
3. Now release the mouse button.

   The script is executed to the end.

##### Execute script to the next function call

If a line with a breakpoint contains a function that you are not interested in, you can suppress the debugging of this function:

- Click on the ![Execute script to the next function call](images/153077472907_DV_resource.Stream@PNG-de-DE.png) "Step over next function call" button in the debugging area.
- Press the <F10> key.

  The function is executed without the script pausing within the function.

##### Jumping into a function

If the script pauses in a line containing a function that interests you, you can pause the script in that function:

- Click on the ![Jumping into a function](images/153087792523_DV_resource.Stream@PNG-de-DE.png) "Step into next function call" button in the debugging area.
- Press the <F11> key.

  The script pauses in the first line of the function.

> **Note**
>
> You can only jump into functions that you have defined yourself.

##### Jump out of a function

If the script pauses within a function that you are not interested in, you can suppress further debugging of this function:

- Click on the ![Jump out of a function](images/153087796491_DV_resource.Stream@PNG-de-DE.png) "Step out of current function" button in the debugging area.
- Press the key combination <Shift + F11>.

> **Note**
>
> You can only jump out of a function that you have defined yourself.

##### Execute script up to a selected line

To pause a paused script again at a selected line, proceeds as follows:

1. Right-click the number of the line in the code display area.
2. Select the entry "Continue to here".

   The script pauses at the selected line.

##### Pause at Exceptions

- To pause the script at Exceptions, click on the ![Pause at Exceptions](images/153087800459_DV_resource.Stream@PNG-de-DE.png) "Pause on exceptions" button in the debugging area.

##### Use call stack

- To jump into a function of the call stack, click on the corresponding entry under "Call Stack".

> **Note**
>
> You can only jump into functions that you have defined yourself.

#### Show values (RT Unified)

##### Introduction

To identify errors in your script efficiently, have current values displayed while the script is being executed. This way you can view properties of objects or parameters of functions, for example. You can find additional information on objects and their properties under "WinCC Unified Object Model".

##### Requirements

- The group you want to debug is selected.
- The script pauses at a breakpoint.

##### Procedure

You view values by moving the mouse over the label in the code display area.

You also have the following options to view values:

- In the debugging area under "Scope"
- In the debugging area under "Watch"
- In the console

##### "Scope" area

All local values ("Local"), functions ("Module") and global values ("Global") that are defined at this time are displayed in the "Scope" area.

The values cannot be edited.

##### "Watch" area

In the "Watch" area, you view how values change in the course of a script.

The following buttons are available to you:

- !["Watch" area](images/123343572619_DV_resource.Stream@PNG-de-DE.png) "Add expression": Add a value
- !["Watch" area](images/123343581195_DV_resource.Stream@PNG-de-DE.png) "Refresh": Refresh the "Watch" area
- !["Watch" area](images/123355558027_DV_resource.Stream@PNG-de-DE.png) "Delete watch expression": Delete a value from the "Watch" area. Available when the mouse pointer is located above the respective value.

##### Console

The values available at the current time can be called in the console.

- You show or hide the console with <Esc>.

Call the current values in the console as follows:

1. Enter the name of a local or global value in the console.
2. Press <Enter>.
