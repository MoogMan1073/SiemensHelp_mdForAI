---
title: "WinCC Audit (Panels, Comfort Panels, RT Advanced)"
package: GMPWCCPenUS
topics: 49
devices: [Comfort Panels, Panels, RT Advanced]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# WinCC Audit (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Basics (Panels, Comfort Panels, RT Advanced)](#basics-panels-comfort-panels-rt-advanced)
- [Using the Audit trail (Panels, Comfort Panels, RT Advanced)](#using-the-audit-trail-panels-comfort-panels-rt-advanced)
- [Configuring audit functions (Panels, Comfort Panels, RT Advanced)](#configuring-audit-functions-panels-comfort-panels-rt-advanced)
- [Performance features of GMP-compliant configuration (Panels, Comfort Panels, RT Advanced)](#performance-features-of-gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
- [Enabling GMP compliant configuration (Panels, Comfort Panels, RT Advanced)](#enabling-gmp-compliant-configuration-panels-comfort-panels-rt-advanced)

## Basics (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [GMP compliance (Panels, Comfort Panels, RT Advanced)](#gmp-compliance-panels-comfort-panels-rt-advanced)
- [GMP-compliant configuration (Panels, Comfort Panels, RT Advanced)](#gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
- [Audit option (Panels, Comfort Panels, RT Advanced)](#audit-option-panels-comfort-panels-rt-advanced)
- [Scope of logging (Panels, Comfort Panels, RT Advanced)](#scope-of-logging-panels-comfort-panels-rt-advanced)

### GMP compliance (Panels, Comfort Panels, RT Advanced)

#### GMP compliant projects with WinCC

Traceability and therefore the documentation of production data is becoming increasingly important in many sectors such as the pharmaceuticals industry, the food and beverage industry, and the related mechanical engineering industry.

Storage of production data in electronic form offers many advantages compared to paper documents, such as simple acquisition and logging of data.

However, it is also important to ensure that data cannot be falsified and that it can be read at any time.

Industry-specific and general standards for electronic documentation of production data have been developed for this purpose.

The most important set of regulations is the FDA guideline 21 CFR Part 11 for electronic data records and electronic signatures issued by the FDA, the US Food and Drug Administration. The various EU regulations, such as EU 178/2002, also apply for particular industries.

Requirements for production systems in these industries have been developed on the basis of 21 CFR Part 11 and the corresponding layout to comply with GMP (Good Manufacturing Practice). They are also required for other industries.

The following primary requirements are derived from these directives and rules:

- Creation of an Audit Trail or operating trace in runtime

  This document can be used to trace a complete log of which user has run what control function on the machine at what time.
- Important process stages must also be traceable to a specific responsibility, for example with an electronic signature.

### GMP-compliant configuration (Panels, Comfort Panels, RT Advanced)

#### Introduction

"GMP compliant configuration" means creating projects in accordance with "Good Manufacturing Practice". The requirements are set out in FDA rules "21 CFR Part 11". The FDA is the U.S. Food and Drug Administration.

GMP-compliant configuration means HMI devices have electronic production data documentation functionalities.

#### GMP relevant and the audit trail

WinCC offers the "Audit" option for implementing GMP compliance. Using the audit option, the "GMP compliant configuration" function can be enabled.

Enable the "GMP compliant configuration" function directly in the runtime settings of the HMI device. GMP relevant functionalities are then added to WinCC. These functionalities are:

- Audit Trail
- Electronic signature
- Option to label tags as "GMP relevant".
- Option to label tags as "GMP relevant" for recipes.
- NotifyUserAction system function
- Logging of tags using checksum
- Logging of alarms using checksum
- Audit trail record for printing logged changes

A license is required to convert the GMP-relevant functions configured in WinCC in runtime.

Depending on the edition of WinCC, use one of the following licenses:

- WinCC Audit for RT Advanced
- WinCC Audit for SIMATIC Panel

If the labeled objects are executed or changed, then it is saved in a special log, the "Audit Trail".

---

**See also**

[Configuring a checksum for a log (Basic Panels, Panels, Comfort Panels, RT Advanced)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-checksum-for-a-log-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring a checksum for a log (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-checksum-for-a-log-panels-comfort-panels-rt-advanced)

### Audit option (Panels, Comfort Panels, RT Advanced)

#### Advanced functions

The Audit option adds functions to WinCC to ensure that your project is GMP compliant.

You need the SIMATIC WinCC Audit license suitable for your HMI device.

The following functions are added:

- Audit Trail

  For every HMI device, you can create an Audit Trail .

  Operator actions and system processes that are relevant for the FDA-compliance of the process are recorded in an Audit Trail during runtime.

  - User actions such as changes in the values of GMP relevant tags or recipes or the acknowledgment of alarms.
  - Actions by the system, such as starting up runtime or rejection of logon attempts.
- Electronic signature

  You can set mandatory acknowledgment of important user actions in runtime, such as changing recipe data records or tag values.

  All Audit-relevant user actions must be protected by authorization in the user administration.

  The user will then only be able to run these actions if an electronic signature and, if configured appropriately, a comment have been input. The electronic signature and the comment are logged in the audit trail.

#### Extension of the WinCC engineering system

For all HMI devices that support "GMP-compliant configuration", the WinCC engineering system is extended to include the following configuration options when GMP is enabled:

- The entry "AuditTrail" is added to the "Logs" editor.
- A "Good Manufacturing Practice Settings" entry is added to "HMI tags" editor in the inspector window of a "Properties &gt; Properties" tag.
- A "Good Manufacturing Practice" entry is added to "Recipes" editor in the inspector window of a "Properties &gt; Properties" recipe.
- "NotifyUserAction" system function

### Scope of logging (Panels, Comfort Panels, RT Advanced)

#### Introduction

It is important to ensure that audit-related processes are always logged in runtime in the audit trail in a project with the option "Audit".

#### Scope of logging

The following operations are Audit-relevant and are automatically saved in the Audit Trail:

- Runtime sequence

  - Runtime start and runtime stop
  - Project information: Version and project name, of the configuration environment, device, and current runtime configuration
  - Failure of the voltage supply of an active Uninterruptible Power Supply (UPS).
- User administration

  - Logon and logoff of users
  - Invalid logon attempts
  - Import of user administration
  - Changes of user administration
- Alarm system

  - All alarms that are acknowledged by the user.
  - All acknowledgment attempts of the user

    > **Note**
    >
    > **Logging alarm text**
    >
    > To log alarm texts, select the "Log alarm text in Audit Trail" option in the Audit Trail editor:
    >
    > "Audit trail &gt; Properties &gt; Settings" in the "Settings" area
- Log operations

  - Starting, stopping and copying a log
  - Opening and closing all logs
  - Deleting a log
  - Starting a sequence log
  - Long-term logging of a log
- Running specific system functions depending on their functionality and the triggering event

The following audit processes are logged depending on the configuration of the recipes and the tags of the project:

- Change values of GMP-relevant tags by the user
- for GMP-relevant recipes:

  - Storing after changing and creating recipe data records
  - Transfer of recipe data records to the PLC and from the PLC
  - For recipe tags: Changing the setting for the synchronization of the tag values with the PLC ("offline"/"online")
- "NotifyUserAction" system function

  You use the system function "NotifyUserAction" to record user actions that are not automatically recorded by the audit trail.

  You can configure this system function for screen calls, for example You can also configure function lists containing system functions that do not require signature or acknowledgement.

## Using the Audit trail (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Audit Trail (Panels, Comfort Panels, RT Advanced)](#audit-trail-panels-comfort-panels-rt-advanced)
- [Creating an audit trail (Panels, Comfort Panels, RT Advanced)](#creating-an-audit-trail-panels-comfort-panels-rt-advanced)
- [Parameters for the audit trail (Panels, Comfort Panels, RT Advanced)](#parameters-for-the-audit-trail-panels-comfort-panels-rt-advanced)
- [Setting the audit trail language (Panels, Comfort Panels, RT Advanced)](#setting-the-audit-trail-language-panels-comfort-panels-rt-advanced)
- [Low free storage space (Panels, Comfort Panels, RT Advanced)](#low-free-storage-space-panels-comfort-panels-rt-advanced)
- [Logging the audit trail (Panels, Comfort Panels, RT Advanced)](#logging-the-audit-trail-panels-comfort-panels-rt-advanced)
- [Evaluating an audit trail (Panels, Comfort Panels, RT Advanced)](#evaluating-an-audit-trail-panels-comfort-panels-rt-advanced)
- [Audit trail logging concept (Panels, Comfort Panels, RT Advanced)](#audit-trail-logging-concept-panels-comfort-panels-rt-advanced)

### Audit Trail (Panels, Comfort Panels, RT Advanced)

#### Introduction

Configure a log in the settings for Audit Trail editor. This log is used to store changes in tag or recipe values made by the user and other user actions in runtime.

#### "Settings for audit trail" editor

1. In the project view, double-click "AuditTrail" in the "Log" group.
2. Click on the "Settings for audit trail" tab.
3. Change the properties of Audit Trail in the inspector window.

   !["Settings for audit trail" editor](images/114554535819_DV_resource.Stream@PNG-en-US.png)

#### Audit trail work area

You define the settings for the Audit Trail in the "Properties &gt; Properties" inspector window.

You set the name of the log and the storage location and decide whether logging will begin on startup. Also determine if "Forcing" is permitted.

"Forcing" is a function for administrators. It allows the administrator to continue the process even if the maximum log storage space has been exceeded.

Thus, the Audit Trail switches off and must be rebooted using the "StartLogging" system function.

### Creating an audit trail (Panels, Comfort Panels, RT Advanced)

#### Requirements

"GMP compliant configuration" has been selected on the HMI device.

#### Procedure

1. Double-click on the HMI device in the project tree.
2. Double-click "Logs".

   The "Logs" editor will open.
3. Change to the "Audit Trail" tab.

   An audit trail has been created.

   ![Procedure](images/22031137547_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/22031137547_DV_resource.Stream@PNG-en-US.png)
4. Define the following in the inspector window:

   - Name
   - Storage location
   - Logging with runtime start-up
   - Forcing

**Note**

No audit-related user actions are permitted in GMP relevant projects if there is insufficient storage space available for the audit trail.

If the check box "Forcing permitted" is activated and, because of the hardware, there is insufficient storage space in runtime, the administrator can interrupt audit trail logging. The administrator can prevent the process from stopping in this way.

If the administrator enables the "Forcing" function, the interruption of the audit trail by the administrator will be entered in the audit trail as the last entry.

At the end of "Forcing" restart the audit trail using the "StartLogging" system function.

#### Configuring a function list

If necessary, configure a function list for the events "Low free storage space" and "Free space critically low".

The "Low free storage space" event is triggered if the amount of free storage space available for the audit trail in runtime is less than the amount configured in "Minimum storage space in MB".

The "Free space critically low" event is triggered if there is no longer sufficient free storage space for the audit trail in runtime. The value depends on the HMI device.

You can find more detailed information on this in the section: [Low free storage space](#low-free-storage-space-panels-comfort-panels-rt-advanced)

#### Result

Audit relevant user actions are entered in the configured audit trail in runtime.

---

**See also**

[Low free storage space (Panels, Comfort Panels, RT Advanced)](#low-free-storage-space-panels-comfort-panels-rt-advanced)

### Parameters for the audit trail (Panels, Comfort Panels, RT Advanced)

#### Introduction

Configure Audit Trail in the "Logs" editor if you have enabled "GMP compliant configuration" in the runtime settings.

There are two ways of assigning parameters for the audit trail:

- "Settings for audit trail" editor
- "Audit Trail" inspector window

#### Editor "Audit Trail"

The "Audit Trail" editor is an overview of the Audit Trail created.

Only one Audit Trail can be created per HMI device.

Parameters that are assigned for the Audit Trail can be seen in the line. You can select or deselect the parameters displayed.

The parameters of an Audit Trail are also displayed and described in more detail in the inspector window.

#### General inspector window

You can set the following parameters under "Audit trail &gt; Properties &gt; General":

![General inspector window](images/22896422283_DV_resource.Stream@PNG-en-US.png)

#### Name

- Under "Name", assign a name for the Audit Trail .

  Special characters are not permitted when assigning the name.

#### Storage location

- Storage location

  You can choose between:

  - RDB file
  - a CSV file (ASCII)
  - a TXT file (Unicode)

    > **Note**
    >
    > Use "TXT (Unicode)" as storage location for logging Asian languages.
- Path

  Depending on the HMI device, enter the storage location of the Audit Trail under "Path".
- Minimum space in MB

  Specify the size of remaining storage space that triggers the "Little available memory" event.

#### Inspector window settings

You can set the following parameters under "Audit trail &gt; Properties &gt; Properties &gt; Settings":

![Inspector window settings](images/22897633675_DV_resource.Stream@PNG-en-US.png)

#### Logging activation

- Enable logging at runtime start

#### Forcing

- Bypass electronic signature

  Specifies whether the administrator is permitted to run operator actions without entering an electronic signature or comments.
- Forcing allowed if storage space is exhausted

  This function allows the administrator to interrupt audit trail logging in the following scenarios:

  - There is no free storage space available.
  - The storage medium is missing.
  - Access to required storage medium is not possible.

  You can thus prevent the process from stopping.

  After Forcing was carried out, the audit trail log switches off.

  After the end of "Forcing", the audit trail must be restarted with the system function "StartLogging".

#### Settings

- Logging alarm texts in the audit trail.

  > **Note**
  >
  > Use "TXT (Unicode)" as storage location for logging Asian languages.

  For further details on setting the logging language, refer to the following section:

  [Setting the audit trail language](#setting-the-audit-trail-language-panels-comfort-panels-rt-advanced)

---

**See also**

[Setting the audit trail language (Panels, Comfort Panels, RT Advanced)](#setting-the-audit-trail-language-panels-comfort-panels-rt-advanced)

### Setting the audit trail language (Panels, Comfort Panels, RT Advanced)

#### Introduction

The logging language for an Audit Trail is set in the runtime settings.

#### Procedure

1. Double-click on the HMI device in the project tree.
2. Double-click "Runtime settings".
3. Click "General".
4. Select the logging language in the "Logs" area.

   ![Procedure](images/114564952587_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/114564952587_DV_resource.Stream@PNG-en-US.png)

**Note**

If an Asian language was selected, use the "TXT (Unicode)" storage location in the "Audit trail" editor.

### Low free storage space (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Low free storage space (Panels, Comfort Panels, RT Advanced)](#low-free-storage-space-panels-comfort-panels-rt-advanced-1)
- [Free space critically low (Panels, Comfort Panels, RT Advanced)](#free-space-critically-low-panels-comfort-panels-rt-advanced)
- [Configuring the "Low free storage space" event (Panels, Comfort Panels, RT Advanced)](#configuring-the-low-free-storage-space-event-panels-comfort-panels-rt-advanced)

#### Low free storage space (Panels, Comfort Panels, RT Advanced)

##### Description

This event is triggered if the storage space available on the medium to which the Audit Trail is less than the configured minimum.

#### Free space critically low (Panels, Comfort Panels, RT Advanced)

##### Description

This event is triggered if the storage medium to which an Audit Trail is saved provides insufficient storage space due to hardware restrictions.

#### Configuring the "Low free storage space" event (Panels, Comfort Panels, RT Advanced)

##### Requirements

- A GMP- compliant configuration is enabled
- An Audit Trail is created

##### Procedure

1. Click on the Audit Trail in the "Audit Trail" editor.
2. In the Inspector window, click "Properties &gt; General".
3. In the "Free storage space limit in MB" area, select a value that triggers the "Little free space" event.
4. Click on Events in the Inspector window.
5. Click on the "Low free storage space" event.
6. In the function list, specify a system function to execute when an "Overflow" event is triggered.

### Logging the audit trail (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Reporting an audit trail (Panels, Comfort Panels, RT Advanced)](#reporting-an-audit-trail-panels-comfort-panels-rt-advanced)
- [Audit Trail reporting (Panels, Comfort Panels, RT Advanced)](#audit-trail-reporting-panels-comfort-panels-rt-advanced)
- [Parameters for the audit trail report (Panels, Comfort Panels, RT Advanced)](#parameters-for-the-audit-trail-report-panels-comfort-panels-rt-advanced)
- [Printing out an audit trail report (Panels, Comfort Panels, RT Advanced)](#printing-out-an-audit-trail-report-panels-comfort-panels-rt-advanced)

#### Reporting an audit trail (Panels, Comfort Panels, RT Advanced)

##### Introduction

You can print a report of the operations saved in an Audit Trail. All recorded actions are included in the printout.

##### Requirements for reporting

The "Audit Trail report" report object is available for the printout of an Audit Trail.

You can configure the report in the "Report" editor. The report object is only available if the "GMP-compliant configuration" option is set in the runtime settings of the HMI device.

If an Audit must be printed in runtime, initially the logging of Audit Trailmust be stopped using the "StopLogging" system function.

Whilst an Audit Trail is being printed, no user actions are recorded. Ensure that no GMP-relevant user actions are executed whilst the logging is stopped.

After printing is complete without any errors, restart the Audit Trail using the "StartLogging" system function.

The header of the report is printed in the current runtime language. Change the runtime language to the logging language accordingly.

The logged data from Audit are printed in the configured runtime logging language.

In order to receive a complete report, the report object can also be used in a report in conjunction with the "Print alarm" and "Print recipe" report objects.

---

**See also**

[Audit report (Panels, Comfort Panels, RT Advanced)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#audit-report-panels-comfort-panels-rt-advanced)

#### Audit Trail reporting (Panels, Comfort Panels, RT Advanced)

##### Introduction

You use the "Audit Trail" report object to configure a report for the output of Audit Trail contents to a printer.

Once the printout is started in runtime, all entries currently contained in the Audit Trail are printed out.

##### Procedure

To create a report, proceed as follows:

1. Double-click on the "Reports" entry in the project tree.
2. Double-click "Add new report".

   A new report is created and opened in the "Report" editor.
3. Drag &amp; drop the "Audit trail report" object under "Tools &gt; Controls" to the report created.

   ![Procedure](images/114572218507_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/114572218507_DV_resource.Stream@PNG-en-US.png)
4. Click on the "Audit trail report" object.
5. Change the object properties of the "Audit trail report" object in the inspector window.

##### Result

You have created a report for the printout Audit Trail.

---

**See also**

[Audit report (Panels, Comfort Panels, RT Advanced)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#audit-report-panels-comfort-panels-rt-advanced)

#### Parameters for the audit trail report (Panels, Comfort Panels, RT Advanced)

##### Introduction

The "Audit trail report" parameters can be edited in the inspector window.

##### Inspector window appearance

Click on the "Audit trail report" object.

Change the appearance of the "Audit trail report" object in the appearance area of the Inspector window under "Properties &gt; Properties &gt; Layout".

![Inspector window appearance](images/75087548811_DV_resource.Stream@PNG-en-US.png)

You can configure the foreground color, the background color, the style, and the font settings.

It is recommended to set a font size of 16 px for the output.

##### Inspector window layout

Click on the "Audit trail report" object.

Change the position and size of the "Audit trail report" object in the appearance area of the Inspector window under "Properties &gt; Properties &gt; Layout".

![Inspector window layout](images/75087552779_DV_resource.Stream@PNG-en-US.png)

The "Audit trail report" object always fills the space down to the footer on the report page. If you change the height of the object, then you only change the distance of the object to the header. The report printout can involve a large amount of data.

A page break is automatically inserted when the length of the page is exceeded to print out all data.

In the "Visible entries" area, it is determined whether comments are visible on the printed report.

##### Inspector window miscellaneous

Click on the "Audit trail report" object.

Change the name and layer position of the "Audit trail report" object in the appearance area in the Inspector window under "Properties &gt; Properties &gt; Miscellaneous".

![Inspector window miscellaneous](images/75104273547_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Audit report (Panels, Comfort Panels, RT Advanced)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#audit-report-panels-comfort-panels-rt-advanced)

#### Printing out an audit trail report (Panels, Comfort Panels, RT Advanced)

##### Introduction

Since the logging of Audit must be stopped to print out an Audit Trail, a few details regarding this procedure must be noted.

To output an Audit Trail in a report file on the printer, perform the following steps.

- Stop logging using the "StopLogging" system function.
- Start the printout using the "PrintReport" system function.
- Check if the printing is successfully completed.
- If needed, move or delete the Audit Trail with the "ArchiveLogFile" or "ClearLog" system function.
- Start the logging of Audit with the "StartLogging" system function.

  > **Note**
  >
  > Make sure that the complete Audit Trail has finished printing before you delete the Audit Trail.

##### Requirements

- "GMP compliant configuration" has been enabled.
- A report for the printout of an Audit Trail has been configured.
- The screen for the operator control to be configured is open.

##### Procedure

1. Add a button to the screen and select "Events &gt; Click" in the Properties window.
2. In the function list, configure the "StopLogging" system function at the "Click" event and select your Audit Trail log.
3. Insert an additional button and assign the "PrintReport" system function to the "Click" event of this button.
4. Insert an additional button and configure the "StartLogging" system function in the same function list.
5. Assign unique labels to the buttons.
6. Save the project.

> **Note**
>
> Note the device-specific differences when printing PDFs. You can find more information on this under [PDF](Printer%20driver%20%28Comfort%20Panels%29.md#pdf-comfort-panels).

##### Result

You have configured the required buttons and system functions. The operator can perform the operating tasks described in the introduction during runtime to print out an Audit Trail report.

> **Note**
>
> You can also insert the report objects for the output of alarms and recipes in the report for the printout of an Audit Trail. However, since GMP-relevant operations and system processes are not recorded during the print operation, you should preferably print the Audit Trail in a separate operation.

---

**See also**

[Audit report (Panels, Comfort Panels, RT Advanced)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#audit-report-panels-comfort-panels-rt-advanced)
  
[PDF (Comfort Panels)](Printer%20driver%20%28Comfort%20Panels%29.md#pdf-comfort-panels)

### Evaluating an audit trail (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Evaluating audit trails (Panels, Comfort Panels, RT Advanced)](#evaluating-audit-trails-panels-comfort-panels-rt-advanced)
- [Evaluating Audit Trails in AuditViewer (Panels, Comfort Panels, RT Advanced)](#evaluating-audit-trails-in-auditviewer-panels-comfort-panels-rt-advanced)
- [Evaluating Audit Trails with DOS program (Panels, Comfort Panels, RT Advanced)](#evaluating-audit-trails-with-dos-program-panels-comfort-panels-rt-advanced)

#### Evaluating audit trails (Panels, Comfort Panels, RT Advanced)

##### Introduction

The Audit Trail has been saved to the memory card of the HMI device and is also read only.

The Audit Trail is protected by a checksum. This checksum ensures that the entry has not been modified at any later time.

There are two possible ways to evaluate the Audit Trail:

- Use the "Audit Viewer":

  You can easily evaluate the Audit Viewer for external analysis on an Office PC with the help of the Audit Trail.
- Use the "HmiCheckLogIntegrity" DOS program:

  The DOS program makes it possible to carry out an automatic check of the Audit Trail using the return values.

#### Evaluating Audit Trails in AuditViewer (Panels, Comfort Panels, RT Advanced)

##### Introduction

The Audit Viewer allows you to evaluate all Audit Trail data in a table.

##### Requirements

- Audit Viewer is installed
- The Audit Traillog is located on the computer which has Audit Viewer installed.

##### Procedure

1. Start the Audit Viewer on the configuration PC:

   "Start &gt; SIMATIC &gt; Audit Viewer &gt; Audit Viewer"

   This path may be different on your operating system version.
2. Click the ![Procedure](images/22965245451_DV_resource.Stream@PNG-de-DE.png)button.
3. Load the Audit Trail:

   ![Procedure](images/22996447755_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/22996447755_DV_resource.Stream@PNG-de-DE.png)

The "Data Validity Indicator" is lit up in green to indicate that the loaded Audit Trail has not been manipulated.

Each entry in the Audit Trail is time-stamped to allow precise tracking of operator actions. In addition to system events, such as the import of a password list, the system also records failed logon attempts:

---

**See also**

[Evaluating the checksum of log data (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#evaluating-the-checksum-of-log-data-panels-comfort-panels-rt-advanced)
  
[Evaluating the checksum of log data (Basic Panels, Panels, Comfort Panels, RT Advanced)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#evaluating-the-checksum-of-log-data-basic-panels-panels-comfort-panels-rt-advanced)

#### Evaluating Audit Trails with DOS program (Panels, Comfort Panels, RT Advanced)

##### Introduction

Long-term archiving on a server allows an Audit Trail to be checked automatically using return values in a script.

In addition the programmer can integrate the check using the DOS program "HmiCheckLogIntegrity" into the archiving process. "HmiCheckLogIntegrity" then provides the following return values:

- &lt; 0: Different errors, for example, wrong file format or no file exists.
- 1: The checked Audit Trail is valid.
- &gt; 0: The first line that was manipulated will be returned.

Audit Trail logging is only continued if the return value is "1". In both error cases, the administrator or the shift supervisor can be informed.

##### HmiCheckLogIntegrity

The "HmiCheckLogIntegrity.exe" DOS program is in the installation directory under:

"SIEMENS &gt; Automation &gt; WinCC Runtime Advanced"

### Audit trail logging concept (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Format (Panels, Comfort Panels, RT Advanced)](#format-panels-comfort-panels-rt-advanced)
- [Storage location and medium (Panels, Comfort Panels, RT Advanced)](#storage-location-and-medium-panels-comfort-panels-rt-advanced)
- [Protection mechanisms (Panels, Comfort Panels, RT Advanced)](#protection-mechanisms-panels-comfort-panels-rt-advanced)
- [Upgrading WinCC (Panels, Comfort Panels, RT Advanced)](#upgrading-wincc-panels-comfort-panels-rt-advanced)
- [Audit trail behavior in runtime (Panels, Comfort Panels, RT Advanced)](#audit-trail-behavior-in-runtime-panels-comfort-panels-rt-advanced)

#### Format (Panels, Comfort Panels, RT Advanced)

##### Format - Audit Trail

On an HMI device with "GMP compliant configuration", all events which are relevant to the audit are recorded at runtime in the Audit Trail. You have several format options.

Selection is dependent on the display program and the runtime language used:

- RDB file

  Data is saved with quick access in a proprietary database.

  If you require maximum read performance in Runtime, use the "RDB file" storage location.
- CSV file

  To view and evaluate a CSV file use, e.g. Microsoft Excel on your PC.

  > **Note**
  >
  > Double quotation marks or several characters are not permitted as list separators for the storage site "File - CSV (ASCII)". You can find the settings for list separators under "Start &gt; Settings &gt; Control Panel &gt; Regional and Language Options".
- TXT file

  This file format supports all characters that can be used in WinCC. For editing, you will need software that can save files in Unicode, such as Notepad.

  > **Note**
  >
  > Use "File - TXT (Unicode)" to log Asian languages.

##### Audit Trail with checksum

The following files are generated under special circumstances:

- *.keep

  - If a log is started without checksum and will be continued with a checksum.
  - If you update WinCC with a service pack or a new version and the Audit Trail or the log is continued with the checksum.
  - The content of the keep file will remain the same when compared with the original log file.

    > **Note**
    >
    > Before you update WinCC with a Service Pack or a new version, exit and save the Audit Trail or the logs using checksum. After WinCC is updated, the audit trail or logs will be continued with new files using checksum.
- *.bak

  - If runtime has determined a serious, irregular problem in the file.

#### Storage location and medium (Panels, Comfort Panels, RT Advanced)

##### Storage location and medium

Depending on the hardware configuration of the HMI device, the data may be logged locally (on the hard disk of a PC or on the storage card of a panel) or, if present, on a network drive.

> **Note**
>
> **Logging on network drives**
>
> We do not recommend that you log audit trails directly on a network drive. Power supply can be interrupted at any time. This means there is no guarantee for a reliable operation of logs and audit trails.
>
> We recommend you save the logs on your local hard drive, or on a storage medium of the HMI device. Use the system function "ArchiveLogFile" to save the logs long-term on a network drive.

A "GMP compliant configuration" cannot be operated at runtime to the full extent unless it is possible to save all user actions which are relevant to the audit to the Audit Trail. It must be ensured that sufficient storage space is available for the Audit Trail and that the connection to the storage location for the Audit Trail is not disturbed.

##### Error-handling with insufficient free storage space

If there is insufficient storage space, your project can be configured so that the administrator has an option of continuing the process without logging in the audit trail (forcing).

##### Error-handling if there is no storage medium or the connection to the server is interrupted

All audit-relevant user actions are blocked if insufficient storage space is available for the Audit Trai, e.g. due to missing storage medium.

Blocking is canceled as soon as the storage location for the Audit Trail is available again. The block can be skipped by "forcing".

##### Error-handling with long-term logging

If the audit trail must be moved to a server for long-term logging and the connection to the server is interrupted at this time, the following error-handling is required:

The system closes the audit trail and renames it. The system attempts to send the renamed audit trail to the server again in the background.

If disruption in the connection to the server persists, you receive a system alarm telling you that the connection is down. Then the system attempts to send the renamed audit trail every 300 seconds.

The attempt to transmit the data is repeated until successfully completed. The data is also transmitted after a restart of the HMI device.

##### "Forcing"

If the storage space for the audit trail is insufficient, for example if there is no storage medium or it is full, all audit-relevant user actions are automatically blocked.

In this case the audit trail logging can be configured to give an administrator the option of continuing to operate the system without logging the audit trail (forcing).

The administrator can also be given the option of running the system quickly out of a critical state in case of emergency. In this case the administrator can operate the system without the requirement to input the required electronic signatures or comments.

If the administrator uses the "forcing" function, this is logged as the last entry in the audit trail.

After the end of forcing, the audit trail must be restarted with the system function "StartLogging".

#### Protection mechanisms (Panels, Comfort Panels, RT Advanced)

##### Protective mechanisms to prevent changes to audit trail data

The audit trail data are protected against deliberate or accidental changes:

- The directory in which the audit trail is saved can only be accessed with special rights.
- The audit trail files are write-protected.
- Each data record contains a checksum that can be used to detect a change of its contents. This checksum also ensures that the number of lines has not changed in the audit trail file.

Use the "HmiCheckLogIntegrity" tool, included in the audit option, to check whether an audit trail has been changed:

[Evaluating Audit Trails with DOS program](#evaluating-audit-trails-with-dos-program-panels-comfort-panels-rt-advanced)

#### Upgrading WinCC (Panels, Comfort Panels, RT Advanced)

##### Upgrading WinCC

Before you update WinCC with a Service Pack or a new version, you will have to exit and save the Audit Trail or the logs with checksum. After WinCC is updated, the audit trail or logs with checksum will be continued with new files.

Make sure that the logs are started at a defined state with the new version.

#### Audit trail behavior in runtime (Panels, Comfort Panels, RT Advanced)

##### Effects in runtime

The configuration in Audit Trail has the following effects in runtime, depending on the configuration:

- Audit relevant user actions (such as tag changes and recipe changes) are recorded in an audit trail.
- "Enable logging at runtime start" check box enabled:

  The audit trail is started with runtime.
- "Forcing" group, "Allowed if storage space has been exhausted" check box enabled:

  A user with administrator rights can use "forcing" to run operations on the plant even though the audit trail can no longer be logged because of storage space limitations. Interrupting the audit trail prevents the process from being stopped.

  If the check box "Signing may be bypassed" is enabled, the administrator is not required to input electronic signatures, acknowledgments or comments for operator actions that would normally require signing, acknowledgment or comment.
- If the storage space available for the Audit Trail is less than the configured "Minimum storage space in MB", the function list configured for the "Low free storage space" event will be processed.
- If there is insufficient storage space for the audit trail because of hardware limits, the function list configured for the "Free space critically low" event will be processed.

## Configuring audit functions (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Logging tag value changes (Panels, Comfort Panels, RT Advanced)](#logging-tag-value-changes-panels-comfort-panels-rt-advanced)
- [Logging recipe data record changes (Panels, Comfort Panels, RT Advanced)](#logging-recipe-data-record-changes-panels-comfort-panels-rt-advanced)
- [Logging user actions (Panels, Comfort Panels, RT Advanced)](#logging-user-actions-panels-comfort-panels-rt-advanced)
- [Logging system functions (Panels, Comfort Panels, RT Advanced)](#logging-system-functions-panels-comfort-panels-rt-advanced)

### Logging tag value changes (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Tag value change (Panels, Comfort Panels, RT Advanced)](#tag-value-change-panels-comfort-panels-rt-advanced)
- [Logging tag value changes (Panels, Comfort Panels, RT Advanced)](#logging-tag-value-changes-panels-comfort-panels-rt-advanced-1)
- [Effects of tag change (Panels, Comfort Panels, RT Advanced)](#effects-of-tag-change-panels-comfort-panels-rt-advanced)

#### Tag value change (Panels, Comfort Panels, RT Advanced)

##### Changes to tag values

User actions in runtime are recorded in a Audit Trail once "GMP compliant configuration" has been enabled.

When you configure a GMP compliant project, you specify which tags must meet the requirements of Good Manufacturing Practice (GMP).

If the user changes the value of a GMP-relevant tag in runtime, the value change action is logged in the Audit Trail .

> **Note**
>
> The action of changing the value of GMP-relevant tags made by the PLC, or a system function, is not logged in the Audit Trail.
>
> The system functions used to change the values of GMP-relevant tags which are assigned to events that identify a direct user action are logged.
>
> In addition, configure the "NotifyUserAction" system function to make a manual entry in the Audit Trail or to prompt the user for an electronic signature, an acknowledgment, or a comment.
>
> With the "NotifyUserAction" system function only the value changes that are directly triggered by the event to which the system function is configured are entered in the Audit Trail. For example, if additional tags are changed by changing the value of one tag, the additional value changes are not logged in the Audit Trail.

#### Logging tag value changes (Panels, Comfort Panels, RT Advanced)

##### Requirement

- "Configuration conforms to GMP" is activated in "Runtime settings &gt; Good Manufacturing Practice".
- The tags for which you want to configure the GMP settings are created.
- The property view is open.

##### Procedure

1. Open the HMI tags editor.
2. Select the tag for which you are making GMP settings.

   ![Procedure](images/22945516811_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/22945516811_DV_resource.Stream@PNG-en-US.png)
3. Click "GMP relevant" under "Properties &gt; Properties &gt; GMP" in the Inspector window.
4. Specify how the user must confirm a value change in the "Confirmation type" selection field:

   - "None"

     If the value change is logged in the Audit Trail without user confirmation.
   - "Acknowledgment"

     If user acknowledgement of the value change is required.
   - "Electronic signature"

     If the user's electronic signature is required.
5. Enable the "Comment required" check box if the user is required to enter a comment in addition to an electronic signature or acknowledgment.

   This check box is only enabled if "Electronic signature" or "Acknowledgment" is specified under "Type of confirmation".

##### Confirmation type "Electronic signature"

If you have selected the electronic signature as the confirmation type, a selection list with the HMI roles is displayed.

Select which of the roles can confirm a value change.

![Confirmation type "Electronic signature"](images/154423449483_DV_resource.Stream@PNG-en-US.png)

##### Result

If the user changes the value of a GMP-relevant tag in runtime, the value change is entered in the Audit Trail.

#### Effects of tag change (Panels, Comfort Panels, RT Advanced)

##### Effects in runtime

The configuration has the following effects in runtime depending on the properties of the GMP-relevant tags:

- If the user changes the value of a GMP-relevant tag in runtime, the value change is entered in the Audit Trail.
- Electronic signature

  If "Electronic signature" is specified as the "Type of confirmation", the user must log every user-related value change of the tags using an electronic signature. Otherwise the value change will be rejected.

  The user name used to sign the change is logged in the audit trail.
- Acknowledgement

  If "Acknowledgment" is specified as the "Type of confirmation", the user must acknowledge every user-related value change of the tags. Otherwise the value change will be rejected.

  The acknowledgement is logged in the Audit Trail.
- Comments

  If the "Comment required" check box is enabled, the user must also comment every user-related value change of the tags, in addition to acknowledgment or input of the electronic signature. Otherwise the value change will be rejected.

  The entered comment is logged in the Audit Trail.

### Logging recipe data record changes (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Recipe data changes (Panels, Comfort Panels, RT Advanced)](#recipe-data-changes-panels-comfort-panels-rt-advanced)
- [Logging recipe data changes (Panels, Comfort Panels, RT Advanced)](#logging-recipe-data-changes-panels-comfort-panels-rt-advanced)
- [Effects of recipe data change (Panels, Comfort Panels, RT Advanced)](#effects-of-recipe-data-change-panels-comfort-panels-rt-advanced)

#### Recipe data changes (Panels, Comfort Panels, RT Advanced)

##### Changes to recipe data

User actions in runtime that are relevant to the quality of the process, such as changes of tag values or recipe values, are recorded in an Audit Trail once "GMP compliant configuration" has been enabled.

You specify during configuration which recipes must meet the requirements of "Good Manufacturing Practice" (GMP).

For GMP-relevant recipes, the following operations during runtime are recorded in the Audit Trail:

- Storing after changing and creating recipe data records
- Transfer of recipe data records to the PLC and from the PLC
- For recipe tags: Changing the setting for the synchronization of the tag values with the PLC ("offline"/"online") if the recipe tags are configured as "GMP-relevant".

  > **Note**
  >
  > **Differences in the Audit Trail with recipe display and recipe screen**
  >
  > If you use a recipe screen to save recipe data, enable the "GMP-relevant" property for the recipe tags. If the user changes the value of a GMP-relevant recipe tag in runtime, the changed value is recorded in the Audit Trail. You can also configure for the tag to require the user to confirm the value change with an electronic signature and enter a comment.
  >
  > If you use a recipe display to edit data records of a GMP-relevant recipe, the Audit Trail includes a record of which recipe data records were saved or sent to the PLC. The value changes to the recipe tags are not logged in the Audit Trail. Use the "ExportDataRecords" system function to save the value change to data records in a csv file.
  >
  > If you want to make changes to recipe data records in conformance to the FDA, disable "Enable edit mode" in the recipe view. Use the recipe screen and "GMP relevant" recipe tags.

If you export recipe data records in a regulated project, you can assign the recipe data with a checksum. When you later import the recipe data back, you can use the checksum to determine if the recipe data has changed. The following system functions are available for exporting and importing recipe data with a checksum:

- "ExportDataRecordsWithChecksum"
- "ImportDataRecordsWithChecksum"

#### Logging recipe data changes (Panels, Comfort Panels, RT Advanced)

##### Requirement

- "GMP compliant configuration" has been enabled.
- The recipes for which you want to configure the GMP settings are created.
- The property view is open.

##### Procedure

1. Open the recipe editor and select the recipe for which you want to make GMP settings.

   ![Procedure](images/22945526667_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/22945526667_DV_resource.Stream@PNG-en-US.png)
2. Click "GMP relevant" under "Properties &gt; Properties &gt; GMP" in the Inspector window.
3. Under "Settings", select the following:

   - "Record operations in audit trail:"

     If all user actions in runtime that affect this recipe are to be recorded in the Audit Trail.
   - "Sign loading of recipe data":

     If the user is required to confirm the transfer of recipe data records to or from the PLC using an electronic signature.
   - "Signature for saving recipe data: "

     If the user is required to confirm recipe data record saving with an electronic signature.

##### Result

If the user works with the GMP-relevant recipe in runtime, the change is entered in the Audit Trail.

#### Effects of recipe data change (Panels, Comfort Panels, RT Advanced)

##### Effects in runtime

The configuration has the following effects in runtime depending on the properties of the GMP-relevant recipes:

##### Entries in the Audit Trail

Entries are made in the following cases:

- You create and save new recipe data records of a GMP-relevant recipe at runtime.
- You edit recipe data records of a GMP-relevant recipe and save your changes at runtime.
- Recipe data records are transferred to the PLC or recipe data are read from the PLC.
- The "SetRecipeTags" system function is used to change the setting for synchronization of the tag values with the PLC.

  This concerns the following changes:

  - "offline" to "online"
  - "online" to "offline"

##### Electronic signature

The user must enter an electronic signature in the following cases depending on the configuration:

- The "Sign loading of recipe data" check box is set:

  Signature for the transfer of recipe data records to the PLC. Signing is always required if the transfer is triggered with the recipe display functions and even if it is triggered with "SetDataRecordToPLC" system functions.
- The "Sign saving of recipe data" check box is set:

  Sign saving of recipe data records. The signature is always required if the save is triggered with the system functions of the recipe display, and even if it is triggered with the "SetDataRecordToPLC" or "SaveDataRecord" system function.
- The user name used to sign the change is logged in the audit trail.

  > **Note**
  >
  > The triggering of the "ImportDataRecords" system function is entered in the Audit Trail but does not require a signature or a comment. In addition, call the "NotifyUserAction" system function to request an electronic signature with or without user comment.

### Logging user actions (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [User actions with GMP-compliant configuration (Panels, Comfort Panels, RT Advanced)](#user-actions-with-gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
- [Logging modes (Panels, Comfort Panels, RT Advanced)](#logging-modes-panels-comfort-panels-rt-advanced)
- [Configuring the "NotifyUserAction" system function (Panels, Comfort Panels, RT Advanced)](#configuring-the-notifyuseraction-system-function-panels-comfort-panels-rt-advanced)
- [GMP-compliant user administration (Panels, Comfort Panels, RT Advanced)](#gmp-compliant-user-administration-panels-comfort-panels-rt-advanced)

#### User actions with GMP-compliant configuration (Panels, Comfort Panels, RT Advanced)

##### Introduction

In GMP compliant configuration, user actions and system operations in runtime that are relevant for the quality of the process are recorded in an Audit Trail .

For example, a user logon to the system or the change of a tag value are saved in the log.

In runtime, user actions are saved in an Audit Trail under the following conditions:

- "GMP compliant configuration" has been enabled
- A user is logged on to the system

#### Logging modes (Panels, Comfort Panels, RT Advanced)

##### Automatic logging of user actions

The following user actions are recorded in runtime without the need for additional configuration steps if "GMP compliant configuration" is enabled:

- User Administration

  - Logon and logoff of users
  - Import of user administration
- Alarm system

  - All alarms that are acknowledged by the user.

    If an alarm from an alarm group is acknowledged, an entry is made in the Audit Trail indicating that all other alarms of this group have been acknowledged.
  - All acknowledgment attempts of the user

    > **Note**
    >
    > **Logging alarm text**
    >
    > To log alarm texts, select the "Log alarm texts in Audit Trail" option in the Audit Trail editor.
- Log operations

  - Starting and stopping a log
  - Opening and closing all logs
  - Deleting a log
  - Starting a sequence log
  - Copying a log
  - Long-term logging of a log

##### Configuration-dependent logging

The following processes are logged depending on the configuration of the recipes and the tags of the project:

- Change values of GMP-relevant tags by the user
- for GMP-relevant recipes

  - You create and save new recipe data records of a GMP-relevant recipe at runtime.
  - You edit recipe data records of a GMP-relevant recipe and save your changes at runtime.
  - Transfer of recipe data records to the PLC and from the PLC
  - For recipe tags: Changing the setting for the synchronization of the tag values with the PLC ("offline"/"online")

In addition to logging user actions you can configure tags and recipes to require the user to confirm or acknowledge specific actions with an electronic signature or add a comment to the change.

##### Manual logging by means of "NotifyUserAction" system function

This system function is used to record actions in the Audit Trail that are not automatically entered in the Audit Trail. This system function is also used to request the user to enter an electronic signature for the action.

#### Configuring the "NotifyUserAction" system function (Panels, Comfort Panels, RT Advanced)

##### Introduction

This system function is used to log user actions that are not entered automatically entered in the Audit Trail. This system function can also used to request an acknowledgment, or an electronic signature for the user's action.

In this example, the system function is assigned to a button. All operations with this button are logged to the Audit Trail.

##### Requirements

- "GMP-compliant configuration" has been enabled.
- You created the object that is to be assigned the system function.

  A button is used in this example.
- The properties window is open.

##### Procedure

1. Click the button.
2. Click on "Events" in the Inspector window.
3. Assign the "NotifyUserAction" system function to the "Click" event.

#### GMP-compliant user administration  (Panels, Comfort Panels, RT Advanced)

##### SIMATIC Logon

To run a central user and user group administration for several applications or HMI devices, activate SIMATIC Logon.

For more information on user administration and SIMATIC Logon, refer to the following chapter:

[Managing users on the server](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#managing-users-on-the-server-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

---

**See also**

[Managing users on the server (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Configuring%20user%20administration%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#managing-users-on-the-server-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Logging system functions (Panels, Comfort Panels, RT Advanced)

#### Introduction

If system functions are triggered in runtime, this is recorded in the Audit Trail for some system functions. If specific system functions are used on a GMP-relevant object, the user must confirm the triggering.

Some system functions are not supported when using Audit. If you use these system functions in your project, you are solely responsible for them.

The following table shows which system functions are Audit-relevant and whether the user's signature is required:

#### System functions and Audit

| Function (call in script) | Effect of /Audit |
| --- | --- |
| StartLogging (StartLogging) | entered in Audit Trail |
| StopLogging (StopLogging) | entered in Audit Trail |
| ClearLog (ClearLog) | entered in Audit Trail |
| StartNextLog (StartNextLog) | entered in Audit Trail |
| CloseAllLogs (CloseAllLogs) | entered in Audit Trail |
| OpenAllLogs (OpenAllLogs) | entered in Audit Trail |
| LogTag (---) | --- |
| CopyLog (CopyLog) | entered in Audit Trail |
| ActivateScreen (ActivateScreen) | --- |
| ActivateScreenByNumber (ActivateScreenByNumber) | --- |
| ActivatePreviousScreen (ActivatePreviousScreen) | --- |
| SetBitInTag (SetBitInTag) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| ResetBitInTag (ResetBitInTag) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| InvertBitInTag (InvertBitInTag) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| SetBit (SetBit) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| ResetBit (ResetBit) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| InvertBit (InvertBit) | entered in Audit Trail when tag is GMP-relevant  System function must not be applied to tags that require signing or comment. |
| SetBitWhileKeyPressed (---) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| SetDataRecordToPLC (SetDataRecordToPLC) | entered in Audit Trail if the recipe is GMP-relevant  Signing required depending on recipe configuration |
| GetDataRecordTagsFromPLC (GetDataRecordFromPLC) | entered in Audit Trail if the recipe is GMP-relevant |
| ImportDataRecords (ImportDataRecords) | entered in Audit Trail if the recipe is GMP-relevant |
| ImportDataRecordsWithChecksum (ImportDataRecordsWithChecksum) | entered in Audit Trail if the recipe is GMP-relevant |
| ExportDataRecords (ExportDataRecords) | --- |
| ExportDataRecordsWithChecksum (ExportDataRecordsWithChecksum) | --- |
| LoadDataRecord (LoadDataRecord) | entered in Audit Trail if the recipe is GMP-relevant  Signing required depending on recipe configuration |
| SaveDataRecord (SaveDataRecord) | entered in Audit Trail if the recipe is GMP-relevant  Signing required depending on recipe configuration |
| SetDataRecordTagsToPLC (SetDataRecordTagsToPLC) | entered in Audit Trail if the recipe is GMP-relevant  Signing required depending on recipe configuration |
| GetDataRecordTagsFromPLC (GetDataRecordTagsFromPLC) | entered in Audit Trail if the recipe is GMP-relevant |
| SetRecipeTags (SetRecipeTags) | entered in Audit Trail if the recipe is GMP-relevant |
| GetDataRecordName (GetDataRecordName) | --- |
| ClearDataRecordMemory (ClearDataRecordMemory) | Not supported |
| ClearDataRecord (ClearDataRecord) | entered in Audit Trail if the recipe is GMP-relevant |
| PrintScreen (PrintScreen) | --- |
| PrintReport (PrintReport) | --- |
| RecipeViewSaveDataRecord (---) | entered in Audit Trail if the recipe is GMP-relevant  Signing required depending on recipe configuration |
| RecipeViewSaveAsDataRecord (---) | entered in Audit Trail if the recipe is GMP-relevant  Signing required depending on recipe configuration |
| RecipeViewNewDataRecord (---) | --- |
| RecipeViewClearDataRecord (---) | entered in Audit Trail if the recipe is GMP-relevant |
| RecipeViewGetDataRecordFromPLC (---) | entered in Audit Trail if the recipe is GMP-relevant |
| RecipeViewSetDataRecordToPLC (---) | entered in Audit Trail if the recipe is GMP-relevant  Signing required depending on recipe configuration |
| RecipeViewSynchronizeDataRecordWithTags (---) | entered in Audit Trail if the recipe is GMP-relevant  Signing required depending on recipe configuration |
| RecipeViewRenameDataRecord (---) | entered in Audit Trail if the recipe is GMP-relevant |
| RecipeViewBack (---) | --- |
| RecipeViewOpen (---) | --- |
| RecipeViewMenu (---) | --- |
| TrendViewScrollForward (---) | --- |
| TrendViewScrollBack (---) | --- |
| TrendViewExtend (---) | --- |
| TrendViewCompress (---) | --- |
| TrendViewBackToBeginning (---) | --- |
| TrendViewStartStop (---) | --- |
| TrendViewSetRulerMode (---) | --- |
| TrendViewBackToBeginning (---) | --- |
| StatusForceGetValues (---) | Not supported |
| StatusForceSetValues (---) | Not supported |
| AlarmViewAcknowledgeAlarm (---) | entered in Audit Trail |
| AlarmViewEditAlarm (---) | --- |
| AlarmViewShowOperatorNotes (---) | --- |
| HTMLBrowserBack (---) | Not supported |
| HTMLBrowserForward (---) | Not supported |
| HTMLBrowserRefresh (---) | Not supported |
| HTMLBrowserStop (---) | Not supported |
| ScreenObjectCursorUp (---) | --- |
| ScreenObjectCursorDown (---) | --- |
| ScreenObjectPageUp (---) | --- |
| ScreenObjectPageDown (---) | --- |
| PressButton (---) | --- |
| ReleaseButton (---) | --- |
| SmartClientViewConnect (---) | Not supported |
| SmartClientViewDisconnect (---) | Not supported |
| SmartClientViewReadOnlyOn (---) | Not supported |
| SmartClientViewReadOnlyOff (---) | Not supported |
| SmartClientViewRefresh (---) | Not supported |
| SmartClientViewLeave (---) | Not supported |
| ShowAlarmWindow (ShowAlarmWindow) | --- |
| ClearAlarmBuffer (ClearAlarmBuffer) | --- |
| ShowSystemAlarm (ShowSystemAlarm) | --- |
| SetAlarmReportMode (SetAlarmReportMode) | --- |
| Logoff (Logoff) | entered in Audit Trail |
| GetPassword (GetPassword) | --- |
| GetGroupNumber (GetGroupNumber) | --- |
| ExportImportUserAdministration (ExportImportUserAdministration) | Import of user administration is entered in Audit Trail  Export is not entered in Audit Trail |
| Logon (Logon) | entered in Audit Trail |
| GetUserName (GetUserName) | --- |
| TraceUserChange (---) | --- |
| ShowLogOnDialog (---) | --- |
| LinearScaling (LinearScaling) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| InverseLinearScaling (InverseLinearScaling) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| IncreaseFocusedValue (---) | --- |
| DecreaseFocusedValue (---) | --- |
| OpenCommandPrompt (OpenCommandPrompt) | Not supported |
| OpenControlPanel (OpenControlPanel) | Not supported |
| ActivateCleanScreen (---) | --- |
| AdjustContrast (---) | --- |
| CalibrateTouchScreen (CalibrateTouchScreen) | --- |
| OpenScreenKeyboard (OpenScreenKeyboard) | --- |
| OpenTaskManager (OpenTaskManager) | Not supported |
| BackupRAMFileSystem (BackupRAMFileSystem) | Not supported |
| SetAcousticSignal (SetAcousticSignal) | --- |
| ShowOperatorNotes (ShowOperatorNotes) | --- |
| AcknowledgeAlarm (AcknowledgeAlarm) | entered in Audit Trail |
| GoToHome (GoToHome) | --- |
| GoToEnd (GoToEnd) | --- |
| EditAlarm (EditAlarm) | --- |
| DirectKeyScreenNumber (---) | Not supported |
| DirectKey (---) | Not supported |
| SetDeviceMode (SetDeviceMode) | entered in Audit Trail |
| SetDisplayMode (SetDisplayMode) | --- |
| SetConnectionMode (SetConnectionMode) | entered in Audit Trail |
| SetScreenKeyboardMode (SetScreenKeyboardMode) | --- |
| ChangeConnection (ChangeConnection) | Not supported |
| SetLanguage (SetLanguage) | --- |
| SetWebAccess (---) | Not supported |
| StartProgram (StartProgram) | Not supported |
| ShowSoftwareVersion (ShowSoftwareVersion) | --- |
| SimulateTag (---) | Not supported |
| StopRuntime (StopRuntime) | entered in Audit Trail |
| ControlWebServer (ControlWebServer) | Not supported |
| ControlSmartServer (ControlSmartServer) | Not supported |
| OpenInternetExplorer (OpenInternetExplorer) | --- |
| SendEMail (SendEMail) | --- |
| UpdateTag (---) | --- |
| ClearAlarmBufferProTool (ClearAlarmBufferProtoolLegacy) | Not supported |
| Encoding(Encode) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |
| EncodeEx(Encode) | entered in Audit Trail when tag is GMP-relevant  Signature is mandatory, depending on the tag configuration |

## Performance features of GMP-compliant configuration (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Supported HMI devices (Panels, Comfort Panels, RT Advanced)](#supported-hmi-devices-panels-comfort-panels-rt-advanced)
- [Restrictions (Panels, Comfort Panels, RT Advanced)](#restrictions-panels-comfort-panels-rt-advanced)

### Supported HMI devices (Panels, Comfort Panels, RT Advanced)

#### Supported HMI devices

The qualification "GMP relevant configuration" can be configured for the following HMI devices:

- Comfort Panel
- Mobile Panel 2nd Generation
- Panel PC with WinCC RT Advanced
- WinCC RT Advanced

  > **Note**
  >
  > The qualification "GMP" is not supported by WinCC RT Professional.

### Restrictions (Panels, Comfort Panels, RT Advanced)

#### Restrictions

The following functions and configurations cannot be used simultaneously with the qualification "GMP relevant configuration":

- "Watch table" object
- PN direct keys
- DP DirectKey
- Option /Sm@rtServer
- /Sinumerik option
- The functional scope of the HMI devices is only available to a restricted degree in some circumstances because of the limited storage space
- Events of screen objects

  You can set mandatory acknowledgment of important user actions in runtime, such as changing tag values. If you assign an event which has to be acknowledged to a screen object, you may not assign any other events to this graphic object.

  When the event of a screen object is assigned actions which open a user dialog (such as change of a tag value with mandatory acknowledgement), you may not be able to execute these actions at other events.
- Controlling GMP-relevant tags using a slider

  The slider is not suitable for controlling GMP-relevant tags. Any operation of the slider will continuously change the tag value. If this is a GMP-relevant tag, a flood of entries will be generated in the AuditTrail.

## Enabling GMP compliant configuration (Panels, Comfort Panels, RT Advanced)

### Introduction

The Audit Trail and "Electronic Signature" functions are qualified as "GMP compliant configuration".

### Requirements

- A project is created.
- A GMP compatible HMI device has been created.

### Procedure

1. Double-click on the HMI device in the project tree.
2. Double-click "Runtime settings".
3. Click on "GMP".
4. Select "GMP compliant configuration".

   ![Procedure](images/22030323979_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/22030323979_DV_resource.Stream@PNG-en-US.png)

### Result

The Audit option is now enabled for the HMI device.

The following functions can now be configured:

- Audit Trail log
- "NotifyUserAction" system function
- GMP relevant tags
- GMP relevant recipes

---

**See also**

[Configuring a checksum for a log (Basic Panels, Panels, Comfort Panels, RT Advanced)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-checksum-for-a-log-basic-panels-panels-comfort-panels-rt-advanced)
  
[Evaluating the checksum of log data (Basic Panels, Panels, Comfort Panels, RT Advanced)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#evaluating-the-checksum-of-log-data-basic-panels-panels-comfort-panels-rt-advanced)
  
[Configuring a checksum for a log (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-a-checksum-for-a-log-panels-comfort-panels-rt-advanced)
  
[Evaluating the checksum of log data (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#evaluating-the-checksum-of-log-data-panels-comfort-panels-rt-advanced)
