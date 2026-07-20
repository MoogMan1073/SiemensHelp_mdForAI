---
title: "Working with reports (Panels, Comfort Panels, RT Advanced, RT Professional)"
package: ReportsRTWCCPenUS
topics: 72
devices: [Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Working with reports (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-reports-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Objects in reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-reports-panels-comfort-panels-rt-advanced-rt-professional)

## Basics (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#reports-panels-comfort-panels-rt-advanced-rt-professional)
- [Structure of reports (Panels, Comfort Panels, RT Advanced)](#structure-of-reports-panels-comfort-panels-rt-advanced)
- [Structure of reports (RT Professional)](#structure-of-reports-rt-professional)

### Reports (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Reports are used to record process data and processed production cycles. You have the opportunity, for example, to create regular shift reports, output batch data, or record the production process for quality control (QC).

#### Creating reports

A report is created and edited in the "Reports" editor. In this editor, you configure the following report items:

- Formal appearance

  Specify the formal layout of the report in the Inspector window. In this window, for example, you specify the page format, page margins, title page, back page, headers, or footers for the report.

  Moreover, you can specify whether to output the different pages with or without watermark in the reports for Runtime Professional.
- Content

  In the work area, specify the content of the report, for example, the alarms of a shift. To this purpose, insert the corresponding objects into the detail page(s).

  You can also design the title page, back page, headers, and footers as you please. For watermarked pages, create additional pages to be included as "background image" in the output.

The modular structure lets you configure reports that suit all of your applications.

> **Note**
>
> The "Reports" editor is not available at HMI devices that do not support reporting.

#### Report output

In Runtime, report output is event-driven or time-driven.

- Time-driven: Automatic print at specific dates, times or intervals.
- Event-driven: Printing is initiated by specific events, e.g. click on a button, or a limit is exceeded.

The configuration of report output differs depending on the Runtime version.

In Runtime Advanced, the configured reports are output on the default printer of the HMI device.

For Runtime Professional, make the following decisions with the help of a print job:

- Output of selected pages, or of all pages of the report
- Output of all data, or only the data of a specific period
- Output of the report to a printer or file
- Whether the operator is allowed to select a printer or modify the scope of pages for report output
- Whether the report that is output is displayed in the print job list of an application window configured accordingly

#### Print function of screen objects

Certain screen objects of Runtime Professional, e.g. the alarm view, contain a default button function (printer icon) for the report output. WinCC employs predefined system reports for the output. You can can customize these to suit your requirements, or replace them with a report of your individual design.

---

**See also**

[Structure of reports (Panels, Comfort Panels, RT Advanced)](#structure-of-reports-panels-comfort-panels-rt-advanced)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure of reports (RT Professional)](#structure-of-reports-rt-professional)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[Principles for report output (RT Professional)](#principles-for-report-output-rt-professional)
  
[Basics for system traces and system print jobs (RT Professional)](#basics-for-system-traces-and-system-print-jobs-rt-professional)

### Structure of reports (Panels, Comfort Panels, RT Advanced)

#### Introduction

A report in WinCC consists of several sections that can be enabled or disabled, as required.

#### Sections of a report

The following figure shows an example of the different sections of a report in the "Reports" editor.

![Sections of a report](images/82712770571_DV_resource.Stream@PNG-en-US.png)

#### Title page and back page

The title page contains important information about the report content. The back page is used, for example, as Impressum, on which you provide contact information of shift managers or service technicians. The title page and back page are output separately on a single page. Each of them consist of exactly one page and page breaks are not used.

#### Detail page

Configure the output of runtime data such as recipe or alarm reports on the detail pages of the report.

Use the shortcut menu on the detail page to insert additional detail pages or change their order.

#### Header and footer

The header and footer are output on each detail page of the report. You typically insert the page numbers or the date in the header or footer.

---

**See also**

[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#reports-panels-comfort-panels-rt-advanced-rt-professional)
  
[Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)](#principles-for-preparation-of-reports-panels-comfort-panels-rt-advanced)

### Structure of reports (RT Professional)

#### Introduction

A report in WinCC consists of several sections that can be enabled or disabled, as required.

#### Sections of a report

The following figure shows an example of the different sections of a report in the "Reports" editor.

![Sections of a report](images/112104569739_DV_resource.Stream@PNG-en-US.png)

#### Title page and back page

The title page contains important information about the report content. The back page is used, for example, as Impressum, on which you provide contact information of shift managers or service technicians. The title page and back page are output separately on a single page. The page has a precise length and no page break, regardless of whether you configured a dynamic object to be output on that page.

#### Detail page

Configure the output of runtime data such as recipe or alarm reports on the detail pages of the report.

Use the shortcut menu on the detail page to insert additional detail pages or change their order.

#### Header and footer

The header and footer are output on each detail page of the report. You typically insert the project name, report name, page numbers or the date in the header or footer.

#### Watermarks

The title, detail and back pages can be output with a watermark. The page is printed with its superimposed watermark.

With the help of a watermark, output an object "A" next to an object of variable length "B" without displacing object "A". Example: You want to output an output field (A) next to a table (B) on all pages.

The title and back pages, as well as the detail pages have separate watermarks.

---

**See also**

[Reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#reports-panels-comfort-panels-rt-advanced-rt-professional)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

## Working with reports (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Creating reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#creating-reports-panels-comfort-panels-rt-advanced-rt-professional)
- [Report output (Panels, Comfort Panels, RT Advanced, RT Professional)](#report-output-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Operation in Runtime (Panels, Comfort Panels, RT Advanced, RT Professional)](#operation-in-runtime-panels-comfort-panels-rt-advanced-rt-professional)

### Creating reports (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)](#principles-for-preparation-of-reports-panels-comfort-panels-rt-advanced)
- [Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
- [Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
- [Report design tools (RT Professional)](#report-design-tools-rt-professional)
- [Continuous alarm reporting (RT Professional)](#continuous-alarm-reporting-rt-professional)
- [CSV file for trend output (RT Professional)](#csv-file-for-trend-output-rt-professional)
- [CSV file for output of a table (RT Professional)](#csv-file-for-output-of-a-table-rt-professional)
- [Administration of detail pages (Panels, Comfort Panels, RT Advanced, RT Professional)](#administration-of-detail-pages-panels-comfort-panels-rt-advanced-rt-professional)

#### Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)

##### Introduction

A report in WinCC consists of several sections that can be enabled or disabled, as required.

- Title page
- Back page
- Detail pages
- Headers and footers for the detail pages

> **Note**
>
> Up to 35 detail pages are available to you per report.

##### Procedure

The following figure shows the general procedure for creating a report:

![Procedure](images/2222004107_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| 1) | Settings depend on the report object used. |

##### Tools for the design of reports

The tools that you can use to design reports are available in the "Tools" task card.

- For graphic design insert "basic objects", "elements" and "graphics" in the different sections of the report. For example, for a Logo in the header, separation lines and a page number in the footer.
- Using the "Controls" in the detail pages, configure the output of runtime data.

  > **Note**
  >
  > The "Screens" editor provides many objects for designing a report – however, with restricted functionality. Data input properties are not available. The I/O fields in the reports, for example, serve only to output data.

##### Position and size of objects

Insert the objects at the position where you want them to be output in the report. The objects are output in their configured size and with the following special features:

On the detail pages, configure "recipe reports" or "alarm reports" that serve to output runtime data in tabular format.

- The width of the table is set up automatically to fit the width of the detail page. You cannot modify the width.
- WinCC automatically wraps the height of the table to fit the data content for output in the report. The table can be continued on the next page.

  In the detail page, WinCC automatically extends tables of dynamic length to the bottom margin.

The following figure shows an example of a detail page in the report and its output in Runtime:

| Symbol | Meaning |
| --- | --- |
| Detail page in the report | Report output in Runtime |
| ![Position and size of objects](images/21494367755_DV_resource.Stream@PNG-de-DE.png) | ![Position and size of objects](images/21494558731_DV_resource.Stream@PNG-de-DE.png) |

##### Additional detail pages

Use the shortcut menu on the detail page to insert additional detail pages or change their order.

---

**See also**

[Overview of report output (RT Professional)](#overview-of-report-output-rt-professional)
  
[Printing reports (Panels, Comfort Panels, RT Advanced)](#printing-reports-panels-comfort-panels-rt-advanced)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
  
[Structure of reports (Panels, Comfort Panels, RT Advanced)](#structure-of-reports-panels-comfort-panels-rt-advanced)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Administration of detail pages (Panels, Comfort Panels, RT Advanced, RT Professional)](#administration-of-detail-pages-panels-comfort-panels-rt-advanced-rt-professional)
  
[Objects in reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-reports-panels-comfort-panels-rt-advanced-rt-professional)

#### Principles for preparation of reports (RT Professional)

##### Introduction

A report in WinCC consists of several sections that can be enabled or disabled, as required.

- Title page
- Back page
- Detail pages
- Headers and footers for the detail pages
- Watermarks for title page, back page, detail page

> **Note**
>
> Up to 35 detail pages are available to you per report.

##### Procedure

The following figure shows the general procedure for creating a report:

![Procedure](images/1736888715_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| 1) | Settings depend on the report object used. |

##### Tools for the design of reports

The objects that you can use to design the reports are available in the "Tools" task card.

> **Note**
>
> The "Screens" editor provides many objects for designing a report – however, with restricted functionality. Data input properties are not available. The I/O fields in the reports, for example, serve only to output data.

##### Positioning objects

Insert the objects at the position where you want them to be output in the report. However, you should be aware that WinCC ignores white spaces at the start of the detail page when the report is output. The top object marks the start of the detail page on the printed copy.

The following figure shows an example of a detail page in the report and its output in Runtime:

| Symbol | Meaning |
| --- | --- |
| Detail page in the report | Report output in Runtime |
| ![Positioning objects](images/21490095627_DV_resource.Stream@PNG-de-DE.png) | ![Positioning objects](images/21490107403_DV_resource.Stream@PNG-de-DE.png) |

To include a white space in the output, extend the header accordingly. You can also place an "invisible" object on the detail page at the required start. For example a white line that is not visible on white paper.

##### Size of objects

Objects are output in their configured size.

On the detail pages, configure "controls" and "report objects" for the output of Runtime data. WinCC aligns the Runtime data to fit the object frame – with one special feature: If you configure an object like a table with dynamic length, WinCC automatically adjusts the height of the table to fit the amount of data to print. The table can be continued on the next page. WinCC adapts no more than the object height and places all following objects underneath the the object, as configured in the detail page.

The following figure shows an example of a detail page in the report and its output in Runtime:

| Symbol | Meaning |
| --- | --- |
| Detail page in the report | Report output in Runtime |
| ![Size of objects](images/21490095627_DV_resource.Stream@PNG-de-DE.png) | ![Size of objects](images/21494672907_DV_resource.Stream@PNG-de-DE.png) |

Usually, the "controls" and "report objects" are assigned a dynamic length and output Runtime data in tabular format. The following objects are included:

- Recipe report
- Alarm report
- Table view
- ODBC database table
- Alarm sequence report
- CSV provider tables
- Control Hardcopy
- Control Data
- Control information

##### Objects next to dynamic objects

In a detail page, do not place other objects next to objects that have a dynamic length. Given the fact that the position of the objects cannot be clearly defined, WinCC possibly outputs these with errors. Instead, configure the objects as watermark.

The following figure shows an example of a watermark and a detail page in the report and the output in Runtime:

| Symbol | Meaning |
| --- | --- |
| Watermark and detail page in the report | Report output in Runtime |
| ![Objects next to dynamic objects](images/21494063627_DV_resource.Stream@PNG-de-DE.png) | ![Objects next to dynamic objects](images/21494075403_DV_resource.Stream@PNG-de-DE.png) |

##### Title page and back page

The title page and back page are output separately on a single page. WinCC will not continue output on the next page if you configured an object with dynamic length for the title or back page. Runtime data of the object exceeding the output capacity of a single page is not output to the full extent in the report.

##### Additional detail pages

Use the shortcut menu on the detail page to insert additional detail pages or change their order.

---

**See also**

[Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)](#principles-for-preparation-of-reports-panels-comfort-panels-rt-advanced)
  
[Printing reports (RT Professional)](#printing-reports-rt-professional)
  
[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[CSV file for trend output (RT Professional)](#csv-file-for-trend-output-rt-professional)
  
[CSV file for output of a table (RT Professional)](#csv-file-for-output-of-a-table-rt-professional)
  
[Continuous alarm reporting (RT Professional)](#continuous-alarm-reporting-rt-professional)
  
[Reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#reports-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure of reports (RT Professional)](#structure-of-reports-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Administration of detail pages (Panels, Comfort Panels, RT Advanced, RT Professional)](#administration-of-detail-pages-panels-comfort-panels-rt-advanced-rt-professional)
  
[Principles for report output (RT Professional)](#principles-for-report-output-rt-professional)
  
[Objects in reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-reports-panels-comfort-panels-rt-advanced-rt-professional)

#### Create a report  (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Requirement

A project with an HMI device is open.

##### Procedure

To create a report, proceed as follows:

1. Double-click "Add new report" under "Reports" in the project navigation.

   A new blank report is displayed in the "Reports" editor.
2. Select the "Report properties" command in the shortcut menu of the report.
3. In the "Properties > Properties > General" area of the Inspector window, specify whether you want to configure the "Title page", "Back page", "Header" and "Footer" in the report.

   The report sections are updated accordingly.

   ![Procedure](images/111909488779_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111909488779_DV_resource.Stream@PNG-en-US.png)
4. Configure the format, the page layout, and the page margins of the report under "Properties > Properties > Layout."

   ![Procedure](images/111909493259_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111909493259_DV_resource.Stream@PNG-en-US.png)
5. Enter a meaningful report name under "Properties > Properties > Miscellaneous."
6. Design the report sections as required.

   Drag and drop the necessary basic objects, elements, graphic images and controls from the "Tools" task card to the required position.

   Alternatively, you can also copy or move objects already configured from a screen to the report.
7. Configure the objects in the Inspector window:

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[CSV file for trend output (RT Professional)](#csv-file-for-trend-output-rt-professional)
  
[CSV file for output of a table (RT Professional)](#csv-file-for-output-of-a-table-rt-professional)
  
[Continuous alarm reporting (RT Professional)](#continuous-alarm-reporting-rt-professional)
  
[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
  
[Reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#reports-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure of reports (Panels, Comfort Panels, RT Advanced)](#structure-of-reports-panels-comfort-panels-rt-advanced)
  
[Structure of reports (RT Professional)](#structure-of-reports-rt-professional)
  
[Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)](#principles-for-preparation-of-reports-panels-comfort-panels-rt-advanced)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[Administration of detail pages (Panels, Comfort Panels, RT Advanced, RT Professional)](#administration-of-detail-pages-panels-comfort-panels-rt-advanced-rt-professional)
  
[Working with objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-objects-panels-comfort-panels-rt-advanced-rt-professional)
  
[Objects in reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#objects-in-reports-panels-comfort-panels-rt-advanced-rt-professional)

#### Report design tools (RT Professional)

##### Tools for the design of reports

In the "Reports" editor, use the objects in the "Tools" task card to design the reports:

- For graphic design insert "basic objects", "elements" and "graphics" in the different sections of the report. For example, for a Logo in the header, separation lines and a page number in the footer.
- Using the "Controls" in the detail pages, configure the output of runtime data.
- If you want to use your own reports instead of the system reports for the print function of a screen object, configure the output of Runtime data with the help of the "Report objects".

  > **Note**
  >
  > The "Screens" Editor provides many objects, though with restricted functionality, that you can use to design a report. Data input properties are not available. The I/O fields in the reports, for example, serve only to output data.

##### Elements

The following table provides an overview of the objects of the "Elements" panel:

| Object | Application |
| --- | --- |
| Date/time field | For output of the current data and time  You can customize the output format. |
| I/O field | For the output of process values  You can choose between different output formats. |
| Project name | For output of the project name  The name can be output with or without path definition. |
| Report name | For output of the report name |
| Page number | For output of the page number and total number of pages  You can customize the output format. |

##### Output of data in tabular format

For a time-driven or event-driven output of data in table form, configure the following controls in reports:

| Control | Use in report |
| --- | --- |
| Table view | For time-driven output of the values of one or several logging tags  Each row of the table represents the status of the selected logging tag at a specific time. |
| ODBC database table | For the output of data that does not originate from WinCC  The data is output in tabular format via the ODBC interface. |
| CSV provider tables | For the output of data of a CSV file   The data of a CSV file must conform to a specific structure. You can select a CSV file, or configure a tag for dynamic selection of the CSV file. |

A print function is already integrated in the "Table view" control in the "Screens" editor (button in Runtime). The "Table view" uses preconfigured system reports for printing. You can specify in the system reports if you want to output all data or only the current data displayed in the object (snapshot). You match system reports to your requirements or use individually designed reports instead of the system reports.

##### Data output in trends

For a time-driven or event-driven output of data in trend form, configure the following controls in reports:

| Controls | Use in report |
| --- | --- |
| f(t) trend view in reports | For the output of logging tags as a function of time |
| f(x) trend view in reports | For the output of logging tags as a function of other logging tags, e.g. the temperature profile as a function of pressure  You can also compare the trend to a setpoint trend. |
| CSV provider trends | For the output of data of a CSV file   The data of a CSV file must conform to a specific structure. You can select a CSV file, or configure a tag for dynamic selection of the CSV file. |

A print function is already integrated in the "f(t) trend view" and "f(x) trend view" controls in the "Screens" editor (button in Runtime). For printing, these controls use preconfigured system reports that you can customize to suit your requirements.

##### Output of recipes

For a time-driven or event-driven output of recipe data, configure the following controls in reports:

| Control | Use in report |
| --- | --- |
| Recipe view | For the output of recipe elements |

A print function is already integrated in the "Recipe view" control in the "Screens" editor (button in Runtime). This control uses preconfigured system reports for printing. You can specify in the system reports if you want to output all data or only the current data displayed in the object (snapshot). You match system reports to your requirements or use individually designed reports instead of the system reports.

##### Output of alarms

WinCC offers several options for alarm reporting.

For a time-driven or event-driven output of alarms, configure the following control in reports:

| Control | Use in report |
| --- | --- |
| Alarm view | For the output of alarms that occur during the process in a plant.  WinCC outputs current alarms, suppressed alarms or alarms from the historical alarm list (short-term), depending on the configuration. |

A print function is already integrated in the "Alarm view" control in the "Screens" editor (button in Runtime). This control uses preconfigured system reports for printing. You can specify in the system reports if you want to output all alarms or only the current alarms displayed in the object (snapshot). You match system reports to your requirements or use individually designed reports instead of the system reports.

WinCC lets you continuously output alarms after the start of Runtime, for example, to a line printer. All you have to do is activate this output. WinCC offers two preconfigured system reports that you can adapt to meet your requirements: one for output in the line layout and one for output in the page layout.

##### Output of a snapshot from Runtime

To output a snapshot of Runtime in a report, configure the following control in reports:

| Control | Use in report |
| --- | --- |
| Hardcopy | For the output of a snapshot from Runtime  WinCC outputs the entire content of the screen, of the active window, or of an individually selected screen area, depending on the configuration. |

##### Data output via ODBC interface

To read data from external sources using the ODBC interface and output them in a report, configure the following controls in reports.

| Control | Use in report |
| --- | --- |
| ODBC database field | For the output of data from a field of an external database table |
| ODBC database table | For the output of external database tables |

##### Report objects

Certain screen objects, e.g. in the alarm view, contain a default button function (printer icon) for the report output.

For reports that you want to use for the printing a screen object instead of a preconfigured system report, configure the output of Runtime data with the help of the "Report objects".

The following table shows the report objects that you can use in the reports:

| Object | Use in report |
| --- | --- |
| Control Hardcopy | For output of the screen object as it is displayed in Runtime (snapshot) |
| Control Data | For output of the current data of the screen object  The data is output in tabular format. |
| Control Information | To output the data source, for example, window title, object name or screen name |

---

**See also**

[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[Control Data (RT Professional)](#control-data-rt-professional)
  
[Control hard copy (RT Professional)](#control-hard-copy-rt-professional)
  
[Control Information (RT Professional)](#control-information-rt-professional)
  
[CSV provider trends (RT Professional)](#csv-provider-trends-rt-professional)
  
[CSV provider tables (RT Professional)](#csv-provider-tables-rt-professional)
  
[Date/time field (RT Professional)](#datetime-field-rt-professional)
  
[f(t) trend view in reports (RT Professional)](#ft-trend-view-in-reports-rt-professional)
  
[f(x) trend view in reports (RT Professional)](#fx-trend-view-in-reports-rt-professional)
  
[Hardcopy (RT Professional)](#hardcopy-rt-professional)
  
[Alarm view in reports (RT Professional)](#alarm-view-in-reports-rt-professional)
  
[ODBC database field (RT Professional)](#odbc-database-field-rt-professional)
  
[ODBC database table (RT Professional)](#odbc-database-table-rt-professional)
  
[Project name (RT Professional)](#project-name-rt-professional)
  
[Report name (RT Professional)](#report-name-rt-professional)
  
[Recipe view in reports (RT Professional)](#recipe-view-in-reports-rt-professional)
  
[Page number (RT Professional)](#page-number-rt-professional)
  
[Table view in reports (RT Professional)](#table-view-in-reports-rt-professional)
  
[Continuous alarm reporting (RT Professional)](#continuous-alarm-reporting-rt-professional)

#### Continuous alarm reporting (RT Professional)

##### Alarm sequence report

An alarm sequence report outputs alarms that occur on the HMI device continuously in chronological order, for example, to a line printer.

To use the preconfigured alarm sequence report, you only need to activate it.

If you only want to output specific alarms, for example, adapt the report to match your needs.

##### Activation and configuration

The output of the pre-configured alarm sequence report is configured in the "Alarm sequence report" system print job.

To automatically run the system print job at the start of Runtime:

- In the Runtime settings of the HMI device activate "Services > Start sequence of WinCC Runtime  > Alarm sequence report".

The alarm sequence report is output in the default line layout to a line printer.

To output the alarm report in the page layout:

- Open the "Alarm sequence report" system print job and deactivate the "Use line report" option under "Properties > Properties > General".

WinCC assigns the appropriate system report to the system print job.

Customize the system reports to suit your requirements:

- "@AlarmSequenceReportForPagePrinter" for output in page layout
- "@AlarmSequenceReportForLinePrinter" for output in line layout

---

**See also**

[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Alarm sequence report (RT Professional)](#alarm-sequence-report-rt-professional)
  
[Basics for system traces and system print jobs (RT Professional)](#basics-for-system-traces-and-system-print-jobs-rt-professional)
  
[Alarm view in reports (RT Professional)](#alarm-view-in-reports-rt-professional)

#### CSV file for trend output (RT Professional)

##### Requirements for a CSV file that is used for the output of trends

To enable output in a table, the data in the CSV file must have a defined structure.

In the report, the "CSV provider trends" object visualizes the CSV file data in trends. The data of a CSV file must conform to the structure described below.

The CSV file must contain a paragraph for the different parts of the graphic object. A paragraph, in turn, can contain several lines. The following paragraphs are mandatory:

- "Graph": Contains the number of trends and specifications concerning visualization of the graphic object
- "Trends": Contains information on the trend visualization
- "Trend values": Contains the values of the trends

The syntax is identical in all paragraphs. The first line marks the beginning of a paragraph and defines the interpretation of the paragraph data. The other lines of a paragraph contain the actual values of the graphic object or trends.

Use a semicolon to separate the values. Insert line breaks to mark the end of lines.

##### "Graph" paragraph:

The first line of the "Graph" paragraph must contain the following entry:

#Trend_T; Name; Curves; DateFrom; DateTo; Common Y-Axis; Font; Fontsize

The second line has to contain the values for the graphic object.

| Name | Meaning | Comment |
| --- | --- | --- |
| Name | Name of the trend view or file |  |
| Curves | Number of trends |  |
| DateFrom | Start of the time range | Notation: 2000-10-30 10:15:00.000 |
| DateTo | End of the time range | Notation: 2000-10-30 10:15:00.000 |
| Common Y-Axis | Common Y axis |  |
| Font | Font |  |
| Fontsize | Font size |  |

Example:

| Line | Content |
| --- | --- |
| 1 | #Trend_T; Name; Curves; DateFrom; DateTo; Common Y-Axis; Font; Fontsize |
| 2 | "TrendControl1";3;"2001-10-10 16:30:00.000";"2001-10-10 16:40:00.000";0;"Arial";10 |

##### "Trends" paragraph:

The first line of the "Trend" paragraph must contain the following entry:

#Curve; Num; Name; Count; dMin; dMax; Color; Width; CurveType;  Filling

For each trend that is visualized in the graphic object, the paragraph must contain a separate line that specifies the trend values.

| Name | Meaning | Comment |
| --- | --- | --- |
| Num | Trend number | beginning with 0 |
| Name | Trend name |  |
| Count | Number of values |  |
| dMin | Low limit of the trend (for scaling) |  |
| dMax | High limit of the trend (for scaling) |  |
| Color | Color of the Y axis | in hexadecimal notation |
| Width | Line thickness in points | e.g. 1.5 |
| CurveType | Trend type | LINE, DOTS, STEP |
| Filling | Fill color for fields | 0=no, 1=yes |

Example:

| Line | Content |
| --- | --- |
| 1 | #Curve; Num; Name; Count; dMin; dMax; Color; Width; CurveType; Filling |
| 2 | 0;"Temperature";3;10;30;0x00ff0000;1;STEP;0 |
| 3 | 1;"Pressure";5;0;50;0x0000ff00;2;DOTS;0 |
| ... |  |

##### Structure of the "Trend values" data record

The first line of the "Trend values" paragraph must contain the following entry:

#Data; Num; Date; Value; Flags; Color

For each value that is visualized in the trends, the paragraph must contain a separate line that specifies the coordinates.

| Name | Meaning | Comment |
| --- | --- | --- |
| Num | Trend number | beginning with 0 |
| Date | Value on the X axis of the trend | Notation: 2000-10-30 10:15:00.000 |
| Value | Value on the Y axis of the trend |  |
| Flags | Limits / time overlap |  |
| Color | Color of the trend section | in hexadecimal notation  If you did not define a color for the trend, the color of the associated Y axis is applied to the trend. |

Example:

| Line | Content |
| --- | --- |
| 1 | #Data; Num; Date; Value; Flags; Color |
| 2 | 0;"2001-10-10 16:30:00.000";22;0;0x000000FF |
| 3 | 0;"2001-10-10 16:31:00.000";24;0; |
| ... |  |

---

**See also**

[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[CSV provider trends (RT Professional)](#csv-provider-trends-rt-professional)

#### CSV file for output of a table (RT Professional)

##### Requirements for a CSV file to be output in tabular format

In the report, the "CSV provider table" object visualizes the CSV file data in tabular format in the report. The data of a CSV file must conform to the structure described below.

The CSV file must contain a paragraph for the different parts of the table. A paragraph, in turn, can contain several lines. The following paragraphs are mandatory:

- "Table": Specifies the number of columns, the font, and the font size
- Columns": Specifies the headers, widths, and alignment of the columns
- "Data" Contains the data

The syntax is identical in all paragraphs. The first line marks the beginning of a paragraph. The first line describes how the data of the paragraph are interpreted. The other lines of a paragraph contain the actual values of the graphic object or trends.

Use a semicolon to separate the values. Insert line breaks to mark the end of lines.

##### "Table" paragraph

The first line of the "Table" paragraph must contain the following entry:

#Table; Name; Columns; Font; Fontsize

The second line has to contain the values for the table.

| Name | Meaning | Comment |
| --- | --- | --- |
| Name | Name of the table view |  |
| Columns | Number of columns |  |
| Font | Font |  |
| Fontsize | Font size |  |

Example:

| Line | Content |
| --- | --- |
| 1 | #Table; Name; Columns; Font; Fontsize |
| 2 | "Tab_9";4;"Arial";14 |

##### "Columns" paragraph

The first line of the "Columns" paragraph must contain the following entry:

#Column; Num; Header; Width; Alignment

For each table column to be visualized in the graphic object, the paragraph must contain a separate line that specifies the column values.

| Name | Meaning | Comment |
| --- | --- | --- |
| Num | Column number | beginning with 0 |
| Header | Column header |  |
| Width | Ratio of the width between columns | Example: For a table with three columns, you specify the following widths: 2, 4, and 8.   As a result, the third column is output with twice the width of the second and three times the width of the first column.  Column width in characters = [table width in number of characters] x [Width] / [Total of Width all values of the columns] |
| Alignment | Alignment | Left/Central/Right |

Example:

| Line | Content |
| --- | --- |
| 1 | #Column; Num; Header; Width; Alignment |
| 2 | 1;"Number";6;L |
| 3 | … |
| 4 | … |

##### "Values" paragraph

The first line of the "Values" paragraph must contain the following entry:

#Data; Color; Col1; Col2; Col3; ...

For each line of the table, this paragraph must contain a separate line that specifies the relevant column values.

| Name | Meaning | Comment |
| --- | --- | --- |
| Color | Line color | Notation as in HTML as six-digit Hex number: 0xbbggrr   (hex blue blue green green red red) |
| Col1 | Data of column 1 |  |
| Col2 | Data of column 2 |  |
| Col3 | Data of column 3 |  |

Example:

| Line | Content |
| --- | --- |
| 1 | #Data; Color; Col1; Col2; Col3; Col4 |
| 2 | 0xFF00FF;"05/06/02";"15.55.53";86;"+/-" |
| 3 | 0x32b400;"05/06/02";"15.55.54";87;"+/-" |
| 4 | 0x32b400;"05/06/02";"16.00.00";82;"+/-" |

##### Preparing data in the spreadsheet program

As demonstrated in the examples above, the first value in the first line of a paragraph represents the paragraph identifier, e.g. "#Data" as identifier of the "Values" paragraph. The next lines of the paragraph do not contain this identifier.

If you process the lines of a paragraph (of a CSV file) in a spreadsheet program such as Microsoft Excel, the column headers and values will not be congruent.

In order to avoid this effect, insert a semicolon ";" as wildcard at the beginning of the lines that contain the actual values:

- The column headers and values are now correctly aligned vertically in Excel.
- WinCC ignores the semicolon ";" at the beginning of the line and outputs the data correctly in a trend or table.

Example:

| Line | Content |
| --- | --- |
| 1 | #Data; Color; Col1; Col2; Col3; Col4 |
| 2 | ;0xFF00FF;"05/06/02";"15.55.53";86;"+/-" |
| 3 | ;0x32b400;"05/06/02";"15.55.54";87;"+/-" |

##### Control characters for formatting values

The control characters are used to specify value attributes such as the color, font style, or the alignment. The control characters always lead the value. You can combine several control characters: "<B><U>output text", for example, returns the words "output text" in bold and underscored format. No distinction is made between upper and lower case text.

The following table provides an overview of the control characters:

| Symbol | Meaning |
| --- | --- |
| <END> | Ends a sequence of control characters. The remaining text is applied as specified. |
| <COLOR=#rrggbb> | Font color; notation as six-digit Hex number with the following byte sequence: #rrggbb   (red red green green blue blue) |
| <BGCOLOR=#rrggbb> | Background color on hexadecimal notation |
| <B> | Bold font style |
| <U> | Underlined font style |
| <I> | Italic font style |
| <STRIKE> | Strikethrough font style |
| <ALIGN=left> | Text aligned left |
| <ALIGN=center> | Text centered |
| <ALIGN=right> | Text aligned right |

> **Note**
>
> **Different notation for color definitions**
>
> Colors are defined by a six-digit hexadecimal number.
>
> In the "Values" paragraph, the line color has the same notation as in HTML, with the following byte sequence:
>
> 0xbbggrr (blue blue green green red red).
>
> To format a single value, the colors in the control character <Color> are defined by an inverted sequence:
>
> #rrggbb (red red green green blue blue).

---

**See also**

[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[CSV provider tables (RT Professional)](#csv-provider-tables-rt-professional)

#### Administration of detail pages (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Adding a detail page

1. Open the shortcut menu of a detail page.
2. Select the command "Pages > Insert page before" or "Pages > Insert page after."

   Depending on the selected command, the new detail page is inserted either before or after the existing detail page.

##### Deleting a detail page

1. Open the shortcut menu of the detail page that you want to remove.
2. Select the command "Pages > Delete detail page".

   The detail page is deleted.

##### Sorting detail pages

1. Open the shortcut menu of the detail page that you want to move.
2. Select the "Pages > Move one page up" or "Pages > Move one page down" command.

   Depending on the selected command, the detail page is moved either upward or downward.

##### Showing and hiding sections

1. To show or hide a specific section, click on the plus or minus sign in the title bar of the section in the working area.
2. If you want to show or hide all sections of a report, select the command "Show all pages" or "Hide all pages" in the report shortcut menu.

---

**See also**

[Structure of reports (Panels, Comfort Panels, RT Advanced)](#structure-of-reports-panels-comfort-panels-rt-advanced)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Structure of reports (RT Professional)](#structure-of-reports-rt-professional)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)
  
[Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)](#principles-for-preparation-of-reports-panels-comfort-panels-rt-advanced)

### Report output (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Report output (Panels, Comfort Panels, RT Advanced)](#report-output-panels-comfort-panels-rt-advanced)
- [Report output (RT Professional)](#report-output-rt-professional)
- [System reports and system print jobs (RT Professional)](#system-reports-and-system-print-jobs-rt-professional)

#### Report output (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Principles for report output (Panels, Comfort Panels, RT Advanced)](#principles-for-report-output-panels-comfort-panels-rt-advanced)

##### Principles for report output (Panels, Comfort Panels, RT Advanced)

###### Introduction

In Runtime Advanced, report output is event-driven or time-driven.

###### Configuration steps

Configuring event-driven output:

- An event is configured on a button or tag with the "PrintReport" system function.

Configuring time-driven output:

- In the scheduled tasks, configure a "Print job" task and assign it the desired report.

  In the task properties, specify the time and frequency of report output.

###### Output in Runtime

On the control panel of the HMI device, the report is output to the printer that is specified as the default printer.

The default printer enabled for a HMI device can be found in the "Printer list". For further information about the "Printer list", refer to the Internet page of Siemens Customer Support and the Article ID "11376409".

---

**See also**

[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
  
[Overview of report output (RT Professional)](#overview-of-report-output-rt-professional)

#### Report output (RT Professional)

This section contains information on the following topics:

- [Overview of report output (RT Professional)](#overview-of-report-output-rt-professional)
- [Principles for report output (RT Professional)](#principles-for-report-output-rt-professional)
- [Create a print job (RT Professional)](#create-a-print-job-rt-professional)
- [Configuring automatic start of a print job in the scheduled tasks (RT Professional)](#configuring-automatic-start-of-a-print-job-in-the-scheduled-tasks-rt-professional)

##### Overview of report output (RT Professional)

###### Introduction

In Runtime, report output is event-driven or time-driven.

You can also display the pending print jobs as a list in Runtime. Operators can use this print job list to decide which report they want to output.

###### Event-driven output

The report is output after an event was generated.

Examples:

- A tag value changes or exceeds a limit.
- Alarm is incoming, outgoing or acknowledged
- Action by the operator, for example, clicking a button

###### Time-driven output

The report is output automatically.

Examples:

- Once at a specified date, e.g. on December 31, 2010 at 6:30 AM
- At intervals, e.g. daily at 8 am, or on Mondays at 6 pm

###### Configuration steps

The configuration of a time-driven or event-driven report output differs depending on the Runtime version.

To display the print job list in Runtime, configure the "Application window" control in screens. The application window shows all or only select print jobs, depending on the configuration.

---

**See also**

[Create a print job (RT Professional)](#create-a-print-job-rt-professional)
  
[Configuring automatic start of a print job in the scheduled tasks (RT Professional)](#configuring-automatic-start-of-a-print-job-in-the-scheduled-tasks-rt-professional)
  
[Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)](#principles-for-preparation-of-reports-panels-comfort-panels-rt-advanced)
  
[Basics for system traces and system print jobs (RT Professional)](#basics-for-system-traces-and-system-print-jobs-rt-professional)
  
[Principles for report output (RT Professional)](#principles-for-report-output-rt-professional)
  
[Principles for report output (Panels, Comfort Panels, RT Advanced)](#principles-for-report-output-panels-comfort-panels-rt-advanced)
  
[Planning tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Planning%20tasks%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#planning-tasks-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
  
[System reports and system print jobs (RT Professional)](#system-reports-and-system-print-jobs-rt-professional)
  
[Report output (RT Professional)](#report-output-rt-professional)

##### Principles for report output (RT Professional)

###### Introduction

In Runtime Professional, report output is event-driven or time-driven.

###### Configuration steps

- Under Reports, create a print job and assign it the desired report.

  In the print job properties, specify the number of pages, the time range, and the output format (printer or file) of the report.
- To configure a time-driven output, create a task of the type "Print job" in the scheduled tasks and assign the desired print job to this task.

  In the task properties, specify the time and frequency of report output.
- To configure an event-driven output, configure an event to the selected object to run a C Script for calling the "ReportJob" function, e.g.

  - `ReportJob("<Name of print job>","PRINTJOB");` to output the print job
  - `ReportJob("<Name of print job>","PREVIEW");` to output a print preview

> **Note**
>
> **Screen objects with preconfigured report output**
>
> Certain screen objects, e.g. in the alarm view, contain a default button function (printer icon) for the report output. You can choose to modify the default system reports, or use a report with individual design.

###### Output in Runtime

The report is written as follows depending on the configuration:

- On the printer that is specified as the default printer in the control panel of the HMI device.

  The default printer enabled for a HMI device can be found in the "Printer list". For additional information about the "Printer list", refer to the Internet page of Siemens Service & Support and the Article ID "11376409".
- On a network printer that is available for the HMI device.
- In a file in EMF format.

###### Output of reports

Reports are output to the printer in graphic mode. The use of a serial printer is not recommended because of the accumulated data volume.

For proper output, the printer must support the paper format and page layout of the report.

> **Note**
>
> The value of a tag in the report is read and output at the moment of printing. A substantial period of time may elapse between printing out the first and the last page of a report consisting of several pages. This may lead to the same tag being output with a different value on the last page than on the first page.

---

**See also**

[Reports (Panels, Comfort Panels, RT Advanced, RT Professional)](#reports-panels-comfort-panels-rt-advanced-rt-professional)
  
[Overview of report output (RT Professional)](#overview-of-report-output-rt-professional)
  
[Create a print job (RT Professional)](#create-a-print-job-rt-professional)
  
[Configuring automatic start of a print job in the scheduled tasks (RT Professional)](#configuring-automatic-start-of-a-print-job-in-the-scheduled-tasks-rt-professional)
  
[System reports and system print jobs (RT Professional)](#system-reports-and-system-print-jobs-rt-professional)

##### Create a print job (RT Professional)

###### Introduction

You define the following in the print job:

- Scope of the print job: all pages, or specific pages only
- Time period during which report entries are output
- Printer on which the report is printed
- File to which the report is saved

###### Requirement

The "Print jobs" editor is open.

###### Procedure

Proceed as follows to create a new print job:

1. In the "Name" column, double-click in the "<Add>" cell.

   A new print job is inserted.

   ![Procedure](images/25759633419_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25759633419_DV_resource.Stream@PNG-en-US.png)
2. In the "Properties > Properties > General" dialog of the Inspector window, enter a "Name" for the print job and select the "Report".
3. Under "Dialog type", specify whether the operator is allowed to modify the report settings prior to output.

   ![Procedure](images/25759624715_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25759624715_DV_resource.Stream@PNG-en-US.png)
4. Under "Properties > Properties > Page range", specify whether the print job outputs all or only specific pages.

   ![Procedure](images/25759616011_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25759616011_DV_resource.Stream@PNG-en-US.png)
5. Under "Properties > Properties > Time range", specify the time period for the output of report entries.

   ![Procedure](images/25759543307_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25759543307_DV_resource.Stream@PNG-en-US.png)
6. If you want to print the report, enable the "Printer" option under "Properties > Properties > Output > Print output".

   The report is output to the default printer of the HMI device.
7. You can select up to three printers if you want to output the report to a different printer.

   ![Procedure](images/25759534603_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/25759534603_DV_resource.Stream@PNG-en-US.png)
8. If the report should be exported to a file, select "Properties > Properties > Target file > Print to file > Print to file (*.emf)".   
   A folder name is created using the information in "Target directory prefix" and the time stamp at the time of printing. The reports are created in the runtime project directory under "PRT_OUT" in a folder of this name.

   ![Procedure](images/72494833803_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/72494833803_DV_resource.Stream@PNG-en-US.png)

###### Result

The print job is created for the report.

- For time-driven output in Runtime, create a "Print job" task in the scheduled tasks. Assign the required print job to this task.
- For event-driven output, assign the object an event that runs a C script for calling the "PrintJob" function.

---

**See also**

[Overview of report output (RT Professional)](#overview-of-report-output-rt-professional)
  
[Principles for report output (RT Professional)](#principles-for-report-output-rt-professional)
  
[Configuring automatic start of a print job in the scheduled tasks (RT Professional)](#configuring-automatic-start-of-a-print-job-in-the-scheduled-tasks-rt-professional)

##### Configuring automatic start of a print job in the scheduled tasks (RT Professional)

###### Introduction

A task of the "print job" type specifies the time and frequency of automatic report output (time-driven output).

###### Requirements

- A print job has been created.

###### Procedure

To create a task for automatic start of a print job, follow these steps:

1. In the "Runtime settings" of the HMI device activate "Services > Start sequence of WinCC Runtime > Scheduled print jobs in Runtime".
2. Create a new task in the scheduled tasks.
3. Enter a "Name" for the task under "Properties > Properties > General".
4. Select the "Print job" setting in the "Type" field.
5. Select the required "print job".
6. Under "Start time", specify the time and frequency of report output, for example, daily at 5 PM:

   ![Procedure](images/24407910795_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/24407910795_DV_resource.Stream@PNG-en-US.png)

###### Result

The task for time-driven report output was created successfully.

---

**See also**

[Principles for report output (RT Professional)](#principles-for-report-output-rt-professional)
  
[Create a print job (RT Professional)](#create-a-print-job-rt-professional)
  
[Printing reports (RT Professional)](#printing-reports-rt-professional)
  
[Overview of report output (RT Professional)](#overview-of-report-output-rt-professional)

#### System reports and system print jobs (RT Professional)

This section contains information on the following topics:

- [Basics for system traces and system print jobs (RT Professional)](#basics-for-system-traces-and-system-print-jobs-rt-professional)
- [Changing system reports and system print jobs (RT Professional)](#changing-system-reports-and-system-print-jobs-rt-professional)
- [Creating an individual layout for the report output of a screen object (RT Professional)](#creating-an-individual-layout-for-the-report-output-of-a-screen-object-rt-professional)

##### Basics for system traces and system print jobs (RT Professional)

###### System reports and system print jobs for the print function of screen objects

Certain screen objects, e.g. in the alarm view, contain a default button function (printer icon) for the report output.

The "Print" button of the screen object is linked to a preconfigured system print job. The system print job, in turn, outputs a preconfigured system report.

System reports output a "snapshot", or "all data" of the screen object.

- Snapshot: The report outputs the data currently displayed in the screen object.
- All data: The report outputs all data content of the screen object.

The following table identifies the preconfigured system reports and system print jobs for the screen objects.

| Screen object | Default | Print scope | System print job | System reports |
| --- | --- | --- | --- | --- |
| f(t) trend view | X | Snapshot | Function Trend Control - Picture | @Function Trend Control - Picture |
| f(x) trend view | X | Snapshot | Online Trend Control - Picture | @Online Trend Control - Picture |
| Table view |  | Snapshot | Online Table Control – Picture | @Online Table Control – Picture |
| X | All data | Online Table Control - Table | @Online Table Control - Table |  |
| Alarm view |  | Snapshot | Alarm Control – Picture | @Alarm Control – Picture |
| X | All data | Alarm Control - Table | @Alarm Control - Table |  |
| Recipe view |  | Snapshot | Recipe Control - Picture | @Recipe Control - Picture |
| X | All data | Recipe Control - Table | @Recipe Control - Table |  |
| Value table |  | Snapshot | Ruler Control - Picture | @Ruler Control - Picture |
| X | All data | Ruler Control - Table | @Ruler Control - Table |  |

Usually, there is no need to configure the report output. Customize the system print job or system report to suit your requirements: You can also choose to assign a screen object a different, preconfigured system print job, or a print job you created for the output of a report with individual design.

###### System print reports and system print job for alarm sequence reports

The output of an alarm sequence report is configured in a system print job. If you have activated "Properties > Properties > General > Use line report", WinCC uses the alarm sequence report with line layout. If you have not activated this option, WinCC uses the alarm sequence report with page layout.

| Layout | System print job | System report |
| --- | --- | --- |
| Page layout | Alarm sequence report | @AlarmSequenceReportForPagePrinter |
| Line layout | Alarm sequence report | @AlarmSequenceReportForLinePrinter |

---

**See also**

[Overview of report output (RT Professional)](#overview-of-report-output-rt-professional)
  
[Continuous alarm reporting (RT Professional)](#continuous-alarm-reporting-rt-professional)
  
COLUMNS (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)
  
[Principles for report output (RT Professional)](#principles-for-report-output-rt-professional)
  
[Changing system reports and system print jobs (RT Professional)](#changing-system-reports-and-system-print-jobs-rt-professional)

##### Changing system reports and system print jobs (RT Professional)

###### Displaying system reports and system print jobs in the project navigation

The system reports and system print jobs are stored in the project template and not displayed automatically in the project navigation. If you want to modify a system report or system print job, display these in the project navigation.

To do this, follow these steps:

- In the project navigation select the command "Add system report" in the shortcut menu of the "Reports" folder.

The project navigation also shows the system reports under "Reports".

![Displaying system reports and system print jobs in the project navigation](images/25768034827_DV_resource.Stream@PNG-en-US.png)

The list of "Print jobs" was extended to include system print jobs.

![Displaying system reports and system print jobs in the project navigation](images/25759667723_DV_resource.Stream@PNG-en-US.png)

###### Changing system print jobs and system reports

You can modify system print jobs and system reports similar to "normal" print jobs and report, however, with the following restrictions:

- For system print jobs, you cannot rename the report or change its default assignment.
- You cannot add detail pages to system reports.

###### Validity of changes

In the project, any modification to system reports and system print jobs affect all objects assigned the system report or system print job.

> **Note**
>
> **Cancel changes**
>
> To restore the preconfigured status of WinCC, for example, after the control for output of data was accidentally deleted in the report, first delete the system report or the system print job and then select the "Add system reports" command in the shortcut menu of the "Reports" folder in the project tree.

###### Deleting unnecessary system reports and system print jobs

To only show reports and print jobs used in the project (e. g. after migration), you can delete the system reports and system print jobs using the shortcut menu.

If the deleted report or the deleted print job is used in the project, the system report and the system print job preconfigured in WinCC are used.

To display all system reports and system print jobs once again, select the command "Add system reports" in the shortcut menu of the "Reports" folder in the project tree.

- Any deleted system reports and system print jobs will be shown once again. The preconfigured WinCC status is restored. The status at the time of deletion is not reconstructed.
- All other system reports and system print jobs remain the same.

---

**See also**

[Basics for system traces and system print jobs (RT Professional)](#basics-for-system-traces-and-system-print-jobs-rt-professional)
  
COLUMNS (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

##### Creating an individual layout for the report output of a screen object (RT Professional)

###### Introduction

If you do not want to use the default system print job (including the system report) that is linked to the screen object for report output, assign this screen object a different system print job, or a report with individual layout.

###### Using a different system print job

Proceed as follows to assign a different system print job to the screen object:

1. Select the screen object.
2. Select the system print job under "Properties > Properties > General > Print".

###### Using a report with individual layout

Proceed as follows to use a report with individual layout:

1. Create the report.
2. Define the content of the detail page.

   - To output a snapshot of the data currently displayed in the screen object, insert the "Control Hardcopy" report object.
   - To output all report data in table form that are currently contained in the screen object, insert the "Control Data" report object.
   - To include the data source in the report, e.g. window title, name of the object or screen, insert the "Control Screen" report object.
3. Create a print job and assign it to the report.
4. Select the screen object and then select the print job under "Properties > Properties > General > Print".

### Working with objects (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)
- [Deleting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#deleting-an-object-panels-comfort-panels-rt-advanced-rt-professional)
- [Inserting several objects of the same type (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-several-objects-of-the-same-type-panels-comfort-panels-rt-advanced-rt-professional)
- [Positioning objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#positioning-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Moving an object forward or backward (Basic, Advanced, Professional) (Panels, Comfort Panels, RT Advanced, RT Professional)](#moving-an-object-forward-or-backward-basic-advanced-professional-panels-comfort-panels-rt-advanced-rt-professional)
- [Resizing objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#resizing-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Selecting multiple objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-multiple-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Repositioning and resizing multiple objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#repositioning-and-resizing-multiple-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Aligning objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#aligning-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Rotating objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#rotating-objects-panels-comfort-panels-rt-advanced-rt-professional)
- [Flipping objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#flipping-objects-panels-comfort-panels-rt-advanced-rt-professional)

#### Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

In the "Screens" or "Reports" editor, insert the objects to the "Toolbox" task card. Use the mouse to drag the objects into the work area. You either keep the objects in their original size, or scale them up or down when you paste them.

In addition, you can copy or move objects via the clipboard from one editor to another, for example to transfer a screen object to a report. Alternatively, you can also use the mouse instead of the clipboard for copying and moving:

- Copy: <Ctrl + Drag&Drop>
- Moving: Drag&drop

  > **Note**
  >
  > **Basic Panels**
  >
  > The "Reports" editor is not available for Basic Panels.

##### Requirement

The "Tools" task card is open.

##### Inserting objects in their standard size

1. In the "Toolbox" task card, select the desired graphic object or the desired graphic in the WinCC graphics folder.

   When you move the cursor across the work area, it turns into a crosshair with an appended object icon.
2. Click the location in the work area where you want to insert the object or graphic.

   The object is inserted with its standard size at the desired position in the work area.

Alternatively, double-click the object in the "Toolbox" task card.

##### Copying an object

1. Select the desired object.
2. Select "Copy" in the shortcut menu.
3. Click the desired location and select "Paste" in the shortcut menu.

WinCC inserts a copy of the object at the desired location. You can only change the properties that are appropriate for the relevant context.

Example: In the "Screens" editor, you can set the mode for input and output for I/O fields. In the "Reports" editor, the mode is set to "Output".

Original and copy are not interconnected and are configured independently from one another.

##### Inserting lines

1. Select the desired graphic object in the "Tools" task card.
2. Click on a location in the work area. A line in the standard size is inserted.

##### Inserting a polygon or polyline

1. Select the desired object "Polyline" or "Polygon" in the "Tools" task card.
2. Click on a location in the work area. This fixes the starting point of the object.
3. Click another location in the work area. A corner point is set.
4. For every additional corner point, click on the corresponding location in the work area.
5. Double-click on a location in the work area. The last corner point is set.

   This fixes all the points of the polygon or polyline.

**Note**

**Basic Panels**

The "Polyline" and "Polygon" objects are not available for Basic Panels.

> **Note**
>
> If you want to insert several objects of the same type, use the "Stamp" function. This avoids having to reselect the object in the "Tools" task card every time before inserting it. To do so, select the ![Inserting a polygon or polyline](images/60629650059_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar of the "Tools" task card.

---

**See also**

[Deleting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#deleting-an-object-panels-comfort-panels-rt-advanced-rt-professional)
  
[Inserting several objects of the same type (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-several-objects-of-the-same-type-panels-comfort-panels-rt-advanced-rt-professional)
  
[Positioning objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#positioning-objects-panels-comfort-panels-rt-advanced-rt-professional)
  
[Resizing objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#resizing-objects-panels-comfort-panels-rt-advanced-rt-professional)
  
[Selecting multiple objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#selecting-multiple-objects-panels-comfort-panels-rt-advanced-rt-professional)
  
[Repositioning and resizing multiple objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#repositioning-and-resizing-multiple-objects-panels-comfort-panels-rt-advanced-rt-professional)
  
[Aligning objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#aligning-objects-panels-comfort-panels-rt-advanced-rt-professional)
  
[Rotating objects (Panels, Comfort Panels, RT Advanced, RT Professional)](#rotating-objects-panels-comfort-panels-rt-advanced-rt-professional)

#### Deleting an object (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can delete objects individually or with a multiple selection.

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object that you want to delete.

   To delete multiple objects, keep the <Shift> key pressed and select the objects to be deleted one after the other. Alternatively, drag and maximize an area around the desired objects with the mouse.
2. Select "Delete" from the shortcut menu.

##### Result

The selected objects are deleted.

---

**See also**

[Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Inserting several objects of the same type (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

WinCC offers the possibility to "stamp" several objects of the same type directly one after the other, i.e. paste without having to reselect the object every time. In addition you have the possibility of multiplying an object that has already been inserted.

##### Requirement

The "Tools" task card is open.

##### Inserting several objects of one type

1. Select the object that you want to insert in the "Tools" task card.
2. Click the ![Inserting several objects of one type](images/60629650059_DV_resource.Stream@PNG-de-DE.png) icon in the toolbar of the "Tools" task card.

   The "Stamp" function is activated.
3. To insert the object with its standard size, click the relevant insertion position in the work area.

   To insert the object with another size, position the mouse pointer at the desired location in the work area. Press the left mouse button and drag the object to the required size.

   The object is inserted in the work area as soon as you release the mouse button.
4. Repeat step 3 to insert further objects of the same type.
5. Click the ![Inserting several objects of one type](images/60629650059_DV_resource.Stream@PNG-de-DE.png) icon again.

   The "Stamp" function is deactivated.

**Note**

You can copy existing objects using the drag-and-drop +<CTRL> function. The existing object is not moved in this case. You paste a copy of this object into the new position instead.

##### Inserting and multiplying an object

1. Insert the desired object from the "Tools" task card.
2. Press the <Ctrl> key and position the cursor on one of the handles displayed in the figure shown below.

   ![Inserting and multiplying an object](images/6340346507_DV_resource.Stream@PNG-en-US.png)

   ![Inserting and multiplying an object](images/6340346507_DV_resource.Stream@PNG-en-US.png)
3. Drag the handles to the right and/or down while keeping the left mouse button pressed.
4. The object is multiplied depending on available space if you keep moving the cursor.

   ![Inserting and multiplying an object](images/8144852875_DV_resource.Stream@PNG-de-DE.png)

   ![Inserting and multiplying an object](images/8144852875_DV_resource.Stream@PNG-de-DE.png)

##### Result

You have pasted and stamped an object in a screen.

---

**See also**

[Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Positioning objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you select an object, it is enclosed by a rectangle with resizing handles. This rectangle is the selection rectangle. The position of an object is defined by the coordinates of the top left corner of the rectangle surrounding the object.

![Introduction](images/14138611339_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> If the position is outside the work area the object is not displayed in Runtime.

##### Position and align

You have the possibility of having a grid displayed in the work area. You have three options for easier positioning of objects:

- "Snap to grid" When you resposition objects, they are automatically snapped and pasted to the grid. If you hold down the <Alt> key, the object is no longer snapped to the grid.
- "Snap to objects" When you reposition objects, they are displayed with help lines. You can use other objects for orientation during positioning.
- "None": You position the objects in any position.

You activate and deactivate the grid and options as follows:

- In the "Options > Settings > Visualization > Screens" menu
- In the "Layout > Grid" task card

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object you want to move.

   The selected object is framed by a rectangle with resizing handles.

   ![Procedure](images/14138611339_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/14138611339_DV_resource.Stream@PNG-de-DE.png)
2. Left-click the object and keep the mouse button pressed.
3. Move the mouse pointer onto the new position.

   The contour of the object moves with the mouse and displays the new position for the object.

   ![Procedure](images/14138619275_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/14138619275_DV_resource.Stream@PNG-de-DE.png)

   The object initially remains at its original position.
4. Now release the mouse button.

   The object is moved into the position indicated by the contour of the selection rectangle.

##### Alternative procedure

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter the X and Y values for the position under "Position & Size".

##### Result

The object appears at its new position.

---

**See also**

[Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Moving an object forward or backward (Basic, Advanced, Professional) (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can use the "Order" functions in the shortcut menu of a selected object or in the toolbar to move a selected object in front of or behind other objects within an object layer.

> **Note**
>
> ActiveX controls are always positioned in front of an object layer (.NET property).

##### Requirement

You have opened a screen which contains a layer with multiple objects.

##### Procedure

1. Select the object you want to move forward or backward.
2. Select the "Sort" command and one of the following commands from the shortcut menu:

| Icon | Description |
| --- | --- |
| ![Procedure](images/14139870219_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object before all the other objects of the same layer |
| ![Procedure](images/14139873803_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object to the lowest position in the same layer |
| ![Procedure](images/14824879627_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object up by one position |
| ![Procedure](images/14824887563_DV_resource.Stream@PNG-de-DE.png) | Moves the selected object down by one position |

##### Alternative procedure

1. Open the "Layers" palette of the "Layout" task card.
2. Navigate to the required object.
3. Hold down the mouse button, and drag the object in the tree topology to the required position in the layer.
4. Now release the mouse button.

##### Result

The object is moved up or down.

#### Resizing objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

When you select an object, it is enclosed by a rectangle with handles. You have the following options of resizing an object:

- Drag the handles using the mouse.
- Modify the "Size" property in the Inspector window.

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object you want to resize.

   The selection rectangle appears. The following figure shows a selected object:

   ![Procedure](images/14138611339_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/14138611339_DV_resource.Stream@PNG-de-DE.png)
2. Drag a resizing contact of the rectangle to a new position.

   The size of the object changes.

   - The size of the object is aligned to the grid pattern, provided the "Snap to grid" function is set.
   - Press <ALT> to disable this function while you drag the object.

     In order to scale the object proportionally, keep the <Shift> key pressed while changing the size with the mouse.

##### Alternative procedure

1. In the Inspector window, select "Properties > Properties > Layout".
2. Enter the size of the object under "Position & Size".

##### Harmonizing the object size

1. Select the objects.
2. Now, click one of the following buttons: ![Harmonizing the object size](images/25693595659_DV_resource.Stream@PNG-de-DE.png) or ![Harmonizing the object size](images/14139797259_DV_resource.Stream@PNG-de-DE.png) or ![Harmonizing the object size](images/14139800843_DV_resource.Stream@PNG-de-DE.png)

   The size of the selected objects is matched to each other.

The following screen shows how the selected objects are adapted to the height of the reference object:

| Symbol | Meaning |
| --- | --- |
| ![Harmonizing the object size](images/6340523531_DV_resource.Stream@PNG-de-DE.png) | ![Harmonizing the object size](images/10274694667_DV_resource.Stream@PNG-de-DE.png) |

| Icon | Description |
| --- | --- |
| ![Harmonizing the object size](images/14139797259_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the width of the reference object. |
| ![Harmonizing the object size](images/14139800843_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the height of the reference object. |
| ![Harmonizing the object size](images/25693595659_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the width and height of the reference object. |

##### Result

The object now appears with its new size.

---

**See also**

[Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Selecting multiple objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

Select all objects you want to align with each other or to change global properties. This procedure is called "multiple selection."

The Inspector window shows all the properties of the selected objects.

You now have several options of selecting multiple objects:

- Draw a selection frame around the objects.
- Hold down the <Shift> key, and click the required objects.

##### Selection frame of a multiple selection

The selection frame surrounds all objects of a multiple selection. The selection frame is comparable with the rectangle that surrounds an individual object.

The selection frame is not visible. When you have made your multiple selection, the following frame is displayed:

- The reference object is indicated by the rectangle around it.
- The other selected objects are indicated by a dashed-line frame.

##### Specifying a reference object

The reference object is the object upon which the other objects are oriented. The reference object is framed by a rectangle with handles. The following figure shows a reference object with two other selected objects:

![Specifying a reference object](images/23810439179_DV_resource.Stream@PNG-de-DE.png)

You have the following options to specify the reference object:

- Select the objects via multiple selection. The object selected first is then the reference object.
- Draw a selection frame around the objects. The reference object compiled automatically. If you wish to specify a different object within the selection as the reference object, click on the desired object. This action does not cancel your multiple selection.

##### Requirement

You have opened the work area containing at least two objects.

##### Selecting multiple objects with a selection frame

1. Position the mouse pointer in the work area close to one of the objects to be selected.
2. Hold down the mouse button, and draw a selection frame around the objects to be selected.

Or:

1. Hold down the <Shift> key.
2. Click the relevant objects, working in succession.

   All the selected objects are identified by frames.

   The object selected first is identified as reference object.

**Note**

To remove an object from the multiple selection, press <SHIFT>, hold it down and then click the relevant object once again.

##### Result

Multiple objects are selected. One of those is identified as the reference object. You can now perform the following steps:

- Changing the object properties of all the objects
- Resizing all the objects by the same ratio, by dragging the selection frame to increase or reduce the size
- Moving all the objects in one group
- Aligning the objects to the reference object

---

**See also**

[Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Repositioning and resizing multiple objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Possible modifications

After you have selected multiple objects, you edit them:

- Shift using the mouse

  - To change the absolute position of the marked objects, position the mouse pointer over an object, and shift the multiple selection with the mouse button pressed.
  - To resize all the objects by the same ratio, grab the resizing handles of the reference object.
- Move over the work area with the icons of the toolbar

  - Change the position of the marked objects with respect to each other
  - Align the height and width of the marked objects
- Moving with the shortcut menu commands of the work area

  - Change the position of the marked objects with respect to each other
  - Align the height and width of the marked objects

---

**See also**

[Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Aligning objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Procedure

1. Select the objects via multiple selection.
2. Specify an object as the reference object.
3. Select the desired command in the toolbar or the shortcut menu - see table below.

   The selected objects will be aligned.

##### Aligning objects flush

The selected objects will be aligned flush to the reference object.

| Icon | Description |
| --- | --- |
| ![Aligning objects flush](images/14138671627_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the left edge of the reference object. |
| ![Aligning objects flush](images/14139626763_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the vertical center axis of the reference object. |
| ![Aligning objects flush](images/13283458059_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the right edge of the reference object. |
| ![Aligning objects flush](images/14139673355_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the upper edge of the reference object. |
| ![Aligning objects flush](images/14139681035_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the horizontal center axis of the reference object. |
| ![Aligning objects flush](images/14139701771_DV_resource.Stream@PNG-de-DE.png) | Aligns the selected objects to the lower edge of the reference object. |
| ![Aligning objects flush](images/14139747851_DV_resource.Stream@PNG-de-DE.png) | Centers the selected objects to the center points of the reference object. |
| ![Aligning objects flush](images/25602636683_DV_resource.Stream@PNG-de-DE.png) | Centers the selected objects vertically in the screen. |

##### Snap to object

When you reposition objects, they are displayed with help lines. You can use other objects for orientation during positioning.

![Snap to object](images/41595801227_DV_resource.Stream@PNG-de-DE.png)

If you are working with the keyboard, press the Alt key. When you move the selected object with the arrow keys, the next anchor point is displayed.

##### Distributing objects evenly

You need at least three selected objects. A reference object is not required.

1. Select the objects.
2. Click one of the buttons "Distribute horizontally equal" or "Distribute vertically equal".

   The selected objects are distributed at equal distances.

The following screen shows how you align the vertical spacing of the selected objects:

| Symbol | Meaning |
| --- | --- |
| ![Distributing objects evenly](images/41609043211_DV_resource.Stream@PNG-de-DE.png) | ![Distributing objects evenly](images/41610037643_DV_resource.Stream@PNG-de-DE.png) |

| Icon | Description |
| --- | --- |
| ![Distributing objects evenly](images/14139755787_DV_resource.Stream@PNG-de-DE.png) | Aligns the horizontal distance between the objects.   The position of the objects on the extreme left and right side remains unchanged. All other objects are distributed evenly between them. |
| ![Distributing objects evenly](images/14139759627_DV_resource.Stream@PNG-de-DE.png) | Aligns the vertical distance between the objects.   The position of the objects at the extreme top and bottom (right and left) remains unchanged. All other objects are distributed evenly between them. |

---

**See also**

[Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Rotating objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can rotate a suitable object clockwise or counterclockwise around its center axis in steps of 90°.

> **Note**
>
> Not all the objects can be rotated. Some objects that can be rotated in screens cannot be rotated in reports.

You can also rotate multiple objects using the multiple selection function. Certain WinCC objects such as buttons cannot be rotated.

The alignment of elements in an object will change in a rotated object. The following figure shows how a rectangle and an ellipse behave under the different commands for rotating an object:

![Introduction](images/14146396043_DV_resource.Stream@PNG-en-US.png)

##### Requirement

You have opened the work area containing at least one object.

##### Procedure

1. Select the object that you want to rotate.
2. Click one of the following toolbar icons:

   ![Procedure](images/14146129803_DV_resource.Stream@PNG-de-DE.png), to rotate the object clockwise around its center point. The angle of rotation is 90°.

   ![Procedure](images/14146133387_DV_resource.Stream@PNG-de-DE.png), to rotate the object counterclockwise around its center point. The angle of rotation is 90°.

   ![Procedure](images/14146354571_DV_resource.Stream@PNG-de-DE.png), to rotate the object clockwise by 180°.

##### Result

The object is shown at its new angle.

---

**See also**

[Inserting an object (Panels, Comfort Panels, RT Advanced, RT Professional)](#inserting-an-object-panels-comfort-panels-rt-advanced-rt-professional)

#### Flipping objects (Panels, Comfort Panels, RT Advanced, RT Professional)

##### Introduction

You can flip an object along its vertical or horizontal center axis. The alignment of elements in an object will change when you flip an object. The following figure shows how a rectangle and an ellipse behave under the different commands for flipping an object.

![Introduction](images/14658859147_DV_resource.Stream@PNG-en-US.png)

##### Requirement

You have opened a screen which contains at least one object.

##### Procedure

1. Select the object that you want to flip.
2. Click the "Flip" command in the shortcut menu and select one of the options displayed:

   - ![Procedure](images/14146613259_DV_resource.Stream@PNG-de-DE.png), to flip the selected object along its vertical center axis.
   - ![Procedure](images/14146617099_DV_resource.Stream@PNG-de-DE.png), to flip the selected object along its horizontal center axis.

##### Result

The object is shown at its flipped position.

### Operation in Runtime (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Printing reports (Panels, Comfort Panels, RT Advanced)](#printing-reports-panels-comfort-panels-rt-advanced)
- [Printing reports (RT Professional)](#printing-reports-rt-professional)

#### Printing reports (Panels, Comfort Panels, RT Advanced)

##### Printing a report in Runtime

If you have configured an object with the "PrintReport" system function, the operator can print out a report in Runtime. To do this, the operator uses the "Print report" button on a screen. The operator can set or change further settings for the report. The report is output to the default printer.

> **Note**
>
> With Panels, note that depending on the printer used, the objects placed at the edge in the report can be cut off during printing.
>
> Make sure that your report has a suitable size.

---

**See also**

[Printing reports (RT Professional)](#printing-reports-rt-professional)
  
[Principles for preparation of reports (Panels, Comfort Panels, RT Advanced)](#principles-for-preparation-of-reports-panels-comfort-panels-rt-advanced)

#### Printing reports (RT Professional)

##### Starting the report printout in Runtime by the operator

The operator starts printing of a report by using the "Print" button in the following screen objects in Runtime:

- f(x) trend view
- f(t) trend view
- Table view
- Alarm view
- Recipe view

If you have specified in the print job that a dialog is displayed for the selection of a printer or to specify properties, the operator changes these settings in Runtime.

If you have configured a button and linked it to an appropriate script, the operator can start the report printout using this button.

##### Automatic start of the report printout

The report printout is started automatically in Runtime in the following situations:

- You have linked a print job with a "Print job" type task.
- You have linked a global script for the report printout with a task.

- Under "Services" in the runtime settings of the HMI device, select the item "Scheduled print jobs in Runtime".

##### Print job/Script diagnostics

All or selected print jobs are shown in the "Print job/Script diagnostics" object depending on the configuration when they are queued in runtime. Depending on the configuration the operator can start the report printout, specify the print options and display a print preview in the "Print job/Script diagnostics" object.

---

**See also**

[Principles for report output (RT Professional)](#principles-for-report-output-rt-professional)
  
[Basics for system traces and system print jobs (RT Professional)](#basics-for-system-traces-and-system-print-jobs-rt-professional)
  
[Principles for preparation of reports (RT Professional)](#principles-for-preparation-of-reports-rt-professional)

## Objects in reports (Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Overview (Panels, Comfort Panels, RT Advanced, RT Professional)](#overview-panels-comfort-panels-rt-advanced-rt-professional)
- [Audit report (Panels, Comfort Panels, RT Advanced)](#audit-report-panels-comfort-panels-rt-advanced)
- [Control Data (RT Professional)](#control-data-rt-professional)
- [Control hard copy (RT Professional)](#control-hard-copy-rt-professional)
- [Control Information (RT Professional)](#control-information-rt-professional)
- [CSV provider trends (RT Professional)](#csv-provider-trends-rt-professional)
- [CSV provider tables (RT Professional)](#csv-provider-tables-rt-professional)
- [Date/time field (Panels, Comfort Panels, RT Advanced)](#datetime-field-panels-comfort-panels-rt-advanced)
- [Date/time field (RT Professional)](#datetime-field-rt-professional)
- [I/O field (Panels, Comfort Panels, RT Advanced, RT Professional)](#io-field-panels-comfort-panels-rt-advanced-rt-professional)
- [f(t) trend view in reports (RT Professional)](#ft-trend-view-in-reports-rt-professional)
- [f(x) trend view in reports (RT Professional)](#fx-trend-view-in-reports-rt-professional)
- [Graphic view (Panels, Comfort Panels, RT Advanced, RT Professional)](#graphic-view-panels-comfort-panels-rt-advanced-rt-professional)
- [Graphic I/O field (Panels, Comfort Panels, RT Advanced)](#graphic-io-field-panels-comfort-panels-rt-advanced)
- [Hardcopy (RT Professional)](#hardcopy-rt-professional)
- [Alarm view in reports (RT Professional)](#alarm-view-in-reports-rt-professional)
- [Alarm sequence report (RT Professional)](#alarm-sequence-report-rt-professional)
- [Alarm report (Panels, Comfort Panels, RT Advanced)](#alarm-report-panels-comfort-panels-rt-advanced)
- [ODBC database field (RT Professional)](#odbc-database-field-rt-professional)
- [ODBC database table (RT Professional)](#odbc-database-table-rt-professional)
- [Project name (RT Professional)](#project-name-rt-professional)
- [Report name (RT Professional)](#report-name-rt-professional)
- [Recipe view in reports (RT Professional)](#recipe-view-in-reports-rt-professional)
- [Recipe report (Panels, Comfort Panels, RT Advanced)](#recipe-report-panels-comfort-panels-rt-advanced)
- [Page number (Panels, Comfort Panels, RT Advanced)](#page-number-panels-comfort-panels-rt-advanced)
- [Page number (RT Professional)](#page-number-rt-professional)
- [Symbolic I/O field (Panels, Comfort Panels, RT Advanced)](#symbolic-io-field-panels-comfort-panels-rt-advanced)
- [Table view in reports (RT Professional)](#table-view-in-reports-rt-professional)
- [Text field (Panels, Comfort Panels, RT Advanced, RT Professional)](#text-field-panels-comfort-panels-rt-advanced-rt-professional)

### Overview (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Objects in the "Reports" editor

Different objects are available in the "Reports" editor:

- Objects for formal design of a report,

  for example, "Page number", "Line" or "Circle"
- Objects for output of contents,

  for example, objects for alarm reports or output of recipes

The next section describes report-specific objects with special properties. Simple design objects are not further explained.

### Audit report (Panels, Comfort Panels, RT Advanced)

#### Application

With the audit report, the content of the audit trail of a HMI device is output as a report.

![Application](images/74904888075_DV_resource.Stream@PNG-en-US.png)

#### Requirements

The "audit report" object is available only if the following requirements are met:

- The HMI device supports a GMP-compliant configuration.
- GMP-compliant configuration is active in the Runtime settings of the HMI device.

Note that operator actions and system operations are only recorded if a corresponding log is configured.

#### Layout

In the Inspector window the position, shape, style, color and font types of the object are customized. In particular, the following can be adjusted:

- Visibility of the comment

---

**See also**

[Enabling GMP compliant configuration (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#enabling-gmp-compliant-configuration-panels-comfort-panels-rt-advanced)
  
[Audit Trail (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#audit-trail-panels-comfort-panels-rt-advanced)
  
[Creating an audit trail (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#creating-an-audit-trail-panels-comfort-panels-rt-advanced)
  
[Reporting an audit trail (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#reporting-an-audit-trail-panels-comfort-panels-rt-advanced)
  
[Audit Trail reporting (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#audit-trail-reporting-panels-comfort-panels-rt-advanced)
  
[Parameters for the audit trail report (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#parameters-for-the-audit-trail-report-panels-comfort-panels-rt-advanced)
  
[Printing out an audit trail report (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#printing-out-an-audit-trail-report-panels-comfort-panels-rt-advanced)
  
[Logging the audit trail (Panels, Comfort Panels, RT Advanced)](WinCC%20Audit%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%29.md#logging-the-audit-trail-panels-comfort-panels-rt-advanced)

### Control Data (RT Professional)

#### Application

You need report objects if you want to configure a report with individual layout for the report output function of a screen object.

The "Control Data" report object outputs all data contained in the screen object in table form – including those data that are currently invisible in the screen object in Runtime.

![Application](images/90808531595_DV_resource.Stream@PNG-en-US.png)

#### Layout

Customize the frame and color settings in the Inspector window. You can adapt the following properties in particular:

- Control type whose content is output
- Control objects of the screen object to be included in the visualization
- Position & size

#### Control type

Specify in the Inspector window under "Properties > Properties > General > Control type", if the value at the ruler position, the content of the object or the object is output.

- In the "f(x) trend view" and the "f(t) trend view" select either the "Ruler" or "Other control" option.
- For all other screen objects select "Other control".

#### Control objects of the screen object

In the Inspector window, select "Properties > Properties > General > Content" to specify whether to include the toolbar, the status bar and the scroll bar in the screen object.

#### Size & position

In the Inspector window, select "Properties > Properties > Layout" to specify the size and position of the report object.

The table is output in the report in accordance with the width of the report object. Therefore, configure a report object with suitable width.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Control hard copy (RT Professional)

#### Application

You need report objects if you want to configure a report with individual layout for the report output function of a screen object.

The "Control Hardcopy" object output a snapshot of the screen object. Only the data that is visible in the screen object in Runtime is output.

![Application](images/90816749451_DV_resource.Stream@PNG-en-US.png)

#### Layout

Customize the frame and color settings in the Inspector window.

You can adapt the following properties in particular:

- Control type whose content is output
- Specifies the control objects of the screen objects to include in the visualization.
- Size & position

#### Control type

Specify in the Inspector window under "Properties > Properties > General > Control type", if the value at the ruler position, the content of the object or the object is output.

- In the "f(x) trend view" and the "f(t) trend view" select either the "Ruler" or "Other control" option.
- For all other screen objects select "Other control".

#### Control objects of the screen object

In the Inspector window, select "Properties > Properties > Content" to specify whether to include the toolbar, the status bar and the scroll bar in the screen object.

#### Size & position

In the Inspector window, select "Properties > Properties > Layout" to specify the size and position of the report object.

In the report, the screen object is resized to fit the frame of the report object. Therefore, configure a report object of a suitable size.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Control Information (RT Professional)

#### Application

You need report objects if you want to configure a report with individual layout for the report output function of a screen object.

The "Control Information" report object outputs the window title, the screen object name or the screen name. This way you include, for example, the data source in the report.

![Application](images/90819216523_DV_resource.Stream@PNG-en-US.png)

#### Layout

Customize the frame, color, font, and font size settings in the Inspector window. You can adapt the following properties in particular:

- Control type whose content is output
- Content

#### Control type

Specify in the Inspector window under "Properties > Properties > General > Control type", if the value at the ruler position, the content of the object or the object is output.

- In the "f(x) trend view" and the "f(t) trend view" select either the "Ruler" or "Other control" option.
- For all other screen objects select "Other control".

#### Content

In the Inspector window, select "Properties > Properties > General > Content" to specify the information to output with the report object:

- Window title
- Object name
- Screen name

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### CSV provider trends (RT Professional)

#### Application

The "CSV provider trends" object outputs data from a file in the format "*.csv" as trends in the report.

Page breaks are inserted automatically in the report depending on the amount of output data. The configured width is not changed in the report. Subsequent objects are shifted automatically.

![Application](images/12763271947_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Data source

#### Data source

Specify the data source under "Properties > Properties > General > Provider". You can select a CSV file, or configure an internal tag for dynamic selection of the CSV file. This means that the data output is changed directly at the HMI device. The tag must be of data type "String" or "WString".

> **Note**
>
> For their visualization in trends, the data in the CSV file must have a defined structure.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### CSV provider tables (RT Professional)

#### Application

The "CSV provider tables" object outputs data from a CSV file in tabular format in the report.

Page breaks are inserted automatically in the report, depending on the amount of output data. The configured width is not changed in the report. Subsequent objects are shifted automatically.

![Application](images/12769054091_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Data source
- Applying fonts from the data source

#### Data source

Specify the data source under "Properties > Properties > General > Provider". You can select a CSV file, or configure an internal tag for dynamic selection of the CSV file. This means that the data output is changed directly at the HMI device. The tag must be of data type "String" or "WString".

> **Note**
>
> To enable output in a table, the data in the CSV file must have a defined structure.

#### Applying fonts from the data source

Under "Properties > Properties > General > Font", specify whether to apply the font and font size from the CSV file for the report output.

If you deactivate the "Font from data source" and "Font size from data source" options, the settings you specified under "Format Text > Style" are used.

---

**See also**

[CSV provider trends (RT Professional)](#csv-provider-trends-rt-professional)
  
[CSV file for output of a table (RT Professional)](#csv-file-for-output-of-a-table-rt-professional)
  
[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Date/time field (Panels, Comfort Panels, RT Advanced)

#### Application

The "Date/time field" object shows the system time of the HMI device or the date and / or time of a connected tag. The layout depends on the language setting on the HMI device.

![Application](images/82712941707_DV_resource.Stream@PNG-de-DE.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. In the "Properties > Properties > General" dialog, you can adapt the following properties in particular:

- Long date/time format: This setting defines the format displayed for the data and / or time.
- System time: Specifies whether to use the system time of the HMI device, or the data and / or time of a connected tag.

#### Long date/time format

| Option | Description |
| --- | --- |
| "Enabled" | Date and / or time is fully displayed, for example "Sunday, December 31, 2000 10:59:59 AM" |
| "Disabled" | Date and / or time is displayed in abbreviated form, e.g. "12/31/2000 10:59:59 AM" |

#### System time

| Option | Description |
| --- | --- |
| "Enabled" | The system time of the HMI device is displayed |
| "Disabled" | The date and / or time of the connected tag is displayed  Select a tag of the "DateTime" data type, e.g. an internal tag. Information about data types which are available for connection to other PLCs can be found in the documentation about the respective communication drivers. |

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Date/time field (RT Professional)

#### Application

The "Date/time field" object outputs the date and / or time in an individually configured format in the report.

![Application](images/12827488395_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Display format of date and / or time

#### Display format of date and time

Specify the date and / or time format under "Properties > Properties > General > Format". You can combine wildcards and any text.

The following table shows which wildcards you can use:

| Wildcards | Implementation | Example |
| --- | --- | --- |
| %a | Weekday abbreviated | Sun |
| %A | Weekday in full form | Sunday |
| %b | Month abbreviated | Dec |
| %B | Month in full form | December |
| %c | Date and time in standard format | 12/31/2000 10:59:59 AM |
| %d | Day as decimal value (01 to 31) | 31 |
| %H | Hours in 24 hour format (00 to 23) | 22 |
| %I | Hours in 12 hour format (01 to 12) | 10 |
| %j | Day of the year as decimal value (000 of 366) | 366 |
| %m | Month as decimal value (01 to 12) | 12 |
| %M | Minute as decimal value (00 to 59) | 59 |
| %p | PM/AM notation for the 12 hour format | AM |
| %S | Second as decimal value (00 to 59) | 59 |
| %U | Week of year as decimal value (01 to 51) | 50 |
| %x | Date in standard format | 12/31/2000 |
| %X | Time in standard format | 10:59 AM |
| %y | Year without century as decimal value (00 to 99) | 00 |
| %Y | Year with century as decimal value | 2000 |
| %z | Time zone as name | W. European Standard Time |
| %% | Percent character | % |

#### Examples

The following table shows a few examples of the combination of wildcards and text:

| Format | Output example |
| --- | --- |
| Date: %x time: %H:%M | Date: 12/31/2000 time: 22:59 |
| Printout of %a %c | Printout of Sun 12/06/2010 10:59:59 AM |

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### I/O field (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Application

The "I/O field" object is used to enter process values.

![Application](images/23650123275_DV_resource.Stream@PNG-de-DE.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Display format: Specifies the format in which the values in the I/O field are output.

  > **Note**
  >
  > The "I/O field" object is also available in "Screens" editor. In reports, the object only outputs data. Accordingly only configure the output of data for application in reports.

#### Display format

The "display format" for the output of values is specified in "Properties > Properties > General > Format", in the Inspector window.

| Layout |  |
| --- | --- |
| "Binary" | Output of values in binary form |
| "Date" * | Output of date specifications. The format depends on the language setting on the HMI device. |
| "Date/time" * | Output of date and time specifications. The format depends on the language setting on the HMI device. |
| "Decimal" * | Output of values in decimal form. |
| "Hexadecimal" | Output of values in hexadecimal form. |
| "Time" * | Output of time specifications. The format depends on the language setting on the HMI device. |
| "Character string" | Output of strings. |
| *: not in Runtime Professional |  |

#### Avoid overlaps with output fields

If several I/O fields are configured as output fields with a transparent background in a report, these I/O fields may overlap. The transparent part of the one field covers the digits of the other field. This may cause display problems in the report. In order to avoid such overlaps, set the margins of the I/O fields to zero in the object properties under "Properties > Properties > Appearance". Activate "Properties > Properties > Layout > Fit object to contents."

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### f(t) trend view in reports (RT Professional)

#### Application

You use the "f(t) trend view" object to visualize logging tag values in the form of trends as a function of time. The report displays the status that the trend profile had at the time of the start of the print job.

![Application](images/12685926283_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Reduced functional scope of the output in reports**
>
> The configuration of the object in the "Reports" editor differs only slightly compared to its configuration in the "Screens" editor.
>
> The functional scope of the object is adapted for the output in reports: In the "Reports" editor, for example, it is not possible to configure operating elements in Runtime.

#### Special features for the output in reports

In contrast to the configuration in the screen, you can dynamize the properties of each trend with tags, for example, the display and the data supply. This way you can, for example, use a report several times.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### f(x) trend view in reports (RT Professional)

#### Application

You use the "f(x) trend view" object to represent the values of a tag as a function of another tag. This means that you can present temperature trends as a function of the pressure, for example. The report displays the status that the trend profile had at the time of the start of the print job.

You can also compare the trend to a setpoint trend.

![Application](images/12685918347_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Reduced functional scope for the output in reports**
>
> The configuration of the object in the "Reports" editor differs only slightly compared to its configuration in the "Screens" editor.
>
> The functional scope of the object is adapted for the output in reports: In the "Reports" editor, for example, it is not possible to configure operating elements in Runtime.

#### Special features for the output in reports

In contrast to the configuration in the screen, you can dynamize the properties of each trend with tags, for example, the display and the data supply. This way you can, for example, use a report several times.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Graphic view (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Application

The "Graphic view" object is used to display graphics.

![Application](images/24337004939_DV_resource.Stream@PNG-de-DE.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Graphic: Specifies the graphic file that is displayed in the object.
- Adjust graphic: Specifies the automatic size stretching for objects with graphics.

#### Inserting graphics

Use the following graphic formats in the "Graphic view" object: *.bmp, *.tif, *.png, *.ico, *.emf, *.wmf, *.gif, *.svg, *.jpg or *.jpeg. You may also use graphics as OLE objects in the Graphic view .

1. Click "Properties > Properties > General" in the Inspector window.
2. Select the graphic that you wish to insert.

   The graphic preview is shown in the right pane.
3. Click "Apply" to insert the graphic in the Graphic view .

#### Adjust graphic

Whether a graphic displayed in a Graphic view is stretched to the size of the Graphic view in runtime is specified in the Inspector window.

1. Click "Properties > Properties > Layout" in the Inspector window.
2. Select one of the following options from the "Fit to size" area:

   - Do not adapt automatically
   - Fit graphic to object size
   - Fit object size to graphic
   - Adjust object size to graphic

### Graphic I/O field (Panels, Comfort Panels, RT Advanced)

#### Application

With the "Graphic I/O field" object, the graphics of a graphics list are displayed, depending on the tag value. In the Inspector window, the tag and graphics list are configured, under "Properties > Properties > General":

![Application](images/23678812811_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> The "Graphic I/O field" object is also available in "Screens" editor. In reports, the object only outputs data. Accordingly only configure the output of data for application in reports.

#### Layout

Customize settings for color, frame, position and object size in the inspector window. In particular, the "Fit to size" is defined by specifying whether the object is adjusted to the graphics during output in the report or the graphic is adjusted in the object.

---

**See also**

[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Hardcopy (RT Professional)

#### Application

Use the "Hardcopy" object to output a snapshot of the screen content in the report.

![Application](images/12837634571_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Specifying the range

#### Specifying the range

Under "Properties > Properties > Range", specify the screen content to output in the report:

- "Current window (1)": Active window
- "Selected section (2)": Selected section
- "Entire screen (0)": Complete content

You can assign a tag of the "Number" type for dynamic range selection. The settings are made as follows:

- 0 = "Entire screen"
- 1 = "Current window"
- 2 = "Selected section"

Specify the following properties for a "Selected section (0)":

- X position of the upper left point of the area
- Y position of the upper left point of the area
- Width in pixels
- Height in pixels

You can assign a dynamic tag to each property.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Alarm view in reports (RT Professional)

#### Application

The "Alarm view" object displays alarms that occur during the process in a plant. You also use the alarm view to visualize alarms in list format. WinCC offers various views, such as "Current alarms" or "Historical alarm list" (short-term).

The report displays the status that the alarm view had at the time of the start of the print job.

![Application](images/12861996811_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Reduced functional scope of the output in reports**
>
> The configuration of the object in the "Reports" editor differs only slightly compared to its configuration in the "Screens" editor.
>
> The functional scope of the object is adapted for the output in reports: In the "Reports" editor, for example, it is not possible to configure operating elements in Runtime.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Continuous alarm reporting (RT Professional)](#continuous-alarm-reporting-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
BackColor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

### Alarm sequence report (RT Professional)

#### Application

The "Alarm sequence report" object outputs all alarms from the HMI device as of the start of Runtime continuously in chronological order. It is only used in the "@AlarmSequenceReportForPage" system report that specified the output of the WinCC alarm sequence report in page layout.

You specify which alarms are output in the object properties.

Page breaks are inserted automatically in the report, depending on the amount of output data. The configured width is not changed in the report. Subsequent objects are shifted automatically.

![Application](images/12837131659_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[SQL Statements for Filtering the Alarm View (RT Professional)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#sql-statements-for-filtering-the-alarm-view-rt-professional)
  
[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Continuous alarm reporting (RT Professional)](#continuous-alarm-reporting-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)
  
[Changing system reports and system print jobs (RT Professional)](#changing-system-reports-and-system-print-jobs-rt-professional)

### Alarm report (Panels, Comfort Panels, RT Advanced)

#### Application

Use the "Alarm report" object to output alarms of the selected alarm classes from the alarm buffer or alarm log to the report.

![Application](images/74756709771_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Source
- Alarm classes
- Time range
- Additional settings for the display
- Visible columns

#### Specifying the source

Under "Properties > Properties > General > Settings > Source", specify whether to display alarms from the alarm buffer, or from the alarm log. Select the alarm log in the "Alarm log" dialog.

> **Note**
>
> The "Alarm log" source is only available if the HMI device supports logs.

#### Specifying alarm classes

Under "Properties > Properties > General > Alarm classes, enable the alarm classes for the alarms output to the report.

#### Specifying the time range

If you want to restrict alarm output to a specific time range, select the start and end tags for the time range in the "Properties > Properties > General > Time range" dialog. The tag must be of the "DateTime" type.

#### Additional settings for the display

Under "Properties > Properties > General > Settings, specify the following settings for the display in the alarm report:

- Under "Sorting", specify whether to start the display with the oldest or most recent alarm.
- Under "Lines per entry", specify the number of lines to be available for each alarm. The required number of lines depends on the following factors:

  - Number and width of the selected columns for the output
  - Font size used
  - Paper format of the printer
- Select "Visible heading" to enable the display of column headers.
- Select "Display milliseconds" to enable the display of milliseconds for time data.

#### Visible columns

Under ""Properties > Properties > Layout > Visible columns", enable the columns to be displayed in the alarm report.

---

**See also**

[Configuring reporting of alarms (Panels, Comfort Panels, RT Advanced)](Working%20with%20alarms%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#configuring-reporting-of-alarms-panels-comfort-panels-rt-advanced)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### ODBC database field (RT Professional)

#### Application

Using the "ODBC database field" object, you can output data from a single table row in the report via the ODBC interface. The ODBC interface is used for the consistent output of data that does not originate from WinCC in the report.

Page breaks are inserted automatically in the report, depending on the amount of output data. The configured width is not changed in the report. Subsequent objects are shifted automatically.

![Application](images/12837422603_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **ODBC-drivers**
>
> Only 64-bit ODBC drivers are supported by Windows 10 systems.

#### Layout

In the Inspector window, you customize the position, shape, style, colors, and font types of the object. You can adapt the following properties in particular:

- Settings for the SQL connection
- Data selection for the SQL statement

#### Text format

Specify the data source under "Properties > Properties > Text format > Alignment". You have the options of displaying the text as horizontal text on the left or right or centered.

> **Note**
>
> The "Alignment > Vertical" setting has no effect in Runtime.

#### Connection settings

Under "Properties > Properties > SQL connection", specify the data source, user name, and password for the SQL connection. You can assign dynamic tag to all settings. This means that the data output is changed directly at the HMI device.

#### Data selection

Under "Properties > Properties > SQL statement", specify the data area to visualize in the report. Enter "Select-Statement".

Enter the required "Select-Statement" in the text field of the same name or select the "Tag" that supplies the Select-Statement. The tag must be of the "String" or "WString" type.

You can dynamize the Select-Statement in the input field of the same name with tags. To do so you select "Insert reportfield" at the required text passage in the shortcut menu and then select the required tag.

> **Note**
>
> Enter only "Select-Statements".

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### ODBC database table (RT Professional)

#### Application

Using the "ODBC database table" object, you can output data from a table in the report via the ODBC interface. The ODBC interface is used for the consistent output of data that does not originate from WinCC in the report.

Page breaks are inserted automatically in the report, depending on the amount of output data. The configured width is not changed in the report. Subsequent objects are shifted automatically.

![Application](images/12837444747_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **ODBC-drivers**
>
> Only 64-bit ODBC drivers are supported by Windows 10 systems.

#### Layout

In the Inspector window, you customize the position, shape, style, colors, and font types of the object. You can adapt the following properties in particular:

- Settings for the SQL connection
- Data selection for the SQL statement
- Table layout, e.g. number of columns and circular list

#### Connection settings

Under "Properties > Properties > SQL connection", specify the data source, user name, and password for the SQL connection. You can assign dynamic tag to all settings. This means that the data output is changed directly at the HMI device.

#### Data selection

Under "Properties > Properties > SQL statement", specify the data area to visualize in the report.

Enter the required "Select-Statement" in the text field of the same name or select the "Tag" that supplies the Select-Statement. The tag must be of the "String" or "WString" type.

You can dynamize the Select-Statement in the input field of the same name with tags. To do so you select "Insert reportfield" at the required text passage in the shortcut menu and then select the required tag.

> **Note**
>
> Enter only "Select-Statements".

#### Circular list

In the Inspector window, use the "Circular list" option under "Properties > Properties > Table" to specify the way the data is distributed to the table columns.

- "Circular list" disabled

  The table rows are filled in descending order.

  A value is output in the first column of a row. The other columns will stay empty.
- "Circular list" is enabled

  The table rows are filled in descending order.

  All columns of a row are filled left to right.

  > **Note**
  >
  > This option is only effective if the data is supplied in one column and if the configured table has several columns.

#### Example:

You configure a table with three columns. At the time of report output, the screen object contains the following data: A1, A2, A3, B1, B2, B3, C1, C3, D4

The following table shows the result with deactivated "Circular list" option:

| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| A1 |  |  |
| A2 |  |  |
| A3 |  |  |
| B1 |  |  |
| B2 |  |  |
| ... |  |  |

The following table shows the result with activated "Circular list" option:

| Column 1 | Column 2 | Column 3 |
| --- | --- | --- |
| A1 | A2 | A3 |
| B1 | B2 | B3 |
| C1 | C3 | D4 |

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Project name (RT Professional)

#### Application

Use the "Project name" object to output the name of the current project in the report.

![Application](images/12837039371_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Format of the project name

#### Format of the project name

In the "Format" field under "Properties > Text format > Style", specify the output format for the project name. You can use a placeholder for the project name and enter any text, if necessary.

The following table shows which wildcards you can use:

| Wildcards | Value |
| --- | --- |
| "%R" | Path and project name |
| "%r" | Project name (without path information) |

#### Examples

The following table shows a few examples of the combination of wildcards and text:

| Format | Output example |
| --- | --- |
| Project: %R | Project: D:\WinCC\Projects\MP277_Mixing |
| Created for project "%r" | Created for project "MP277_Mixing" |

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Report name (RT Professional)

#### Application

Use the "Report name" object to output the report name in the report.

![Application](images/12836966027_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Format of the report name

#### Format of the report name

In the "Format" field under "Properties > Text format > Style", specify the output format for the report name. You can use a placeholder for the report name and enter any text, if necessary.

The following table shows which wildcards you can use:

| Wildcards | Value |
| --- | --- |
| "%L" or "%l" | Report name |

#### Example

The following table shows a few examples of the combination of wildcards and text:

| Format | Output example |
| --- | --- |
| Report: %L | Report: Alarms |

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Recipe view in reports (RT Professional)

#### Application

Use the "Recipe view" object to display recipe elements in tabular format. The report displays the status that the recipe view had at the time of the start of the print job.

![Application](images/21845170699_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **Reduced functional scope of the output in reports**
>
> The configuration of the object in the "Reports" editor differs only slightly compared to its configuration in the "Screens" editor.
>
> The functional scope of the object is adapted for the output in reports: In the "Reports" editor, for example, it is not possible to configure operating elements in Runtime.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Definition and applications (RT Professional)](Working%20with%20recipes%20%28RT%20Professional%29.md#definition-and-applications-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Recipe report (Panels, Comfort Panels, RT Advanced)

#### application

Use the "Recipe report" object to output the elements of recipe data records in the report.

![application](images/74772321547_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color, and font types of the object. You can adapt the following properties in particular:

- Recipe
- Data record
- Format
- Visible entries

#### Selecting a recipe

Specify the recipes to be output in the recipe report under "Properties > Properties > General > Recipe". You can define the recipes based on their recipe name, or on a range of recipe numbers. Under "First recipe" and "Last recipe", enter a value or select a tag.

You can also choose to display all recipes.

#### Selecting a data record

Under "Properties > Properties > General > Data record", specify which data records of the selected recipes are to be output in the recipe report. You can define the data records based on the data record name, or on a range of data record numbers. Under "First recipe" and "Last recipe", enter a value or select a tag.

You can also choose to display all data records of the selected recipes.

#### Format

In the "Format" field of the "Properties > Properties > Layout > Settings" dialog, specify whether to output the data records as a table in column format or line report format.

WinCC updates the preview in the detail page accordingly.

#### Visible entries

Under ""Properties > Properties > Layout > Visible entries", enable the columns to be displayed in the recipe report. Select "Show headings" to enable the display of column headers.

---

**See also**

[Definition and applications (RT Professional)](Working%20with%20recipes%20%28RT%20Professional%29.md#definition-and-applications-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Page number (Panels, Comfort Panels, RT Advanced)

#### application

Use the "Page number" object to output the current page number in the report.

![application](images/76064467979_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the inspector window, change the settings for color, font, position and object size. In particular, specify "Size adaptation":

#### Fit to size

Under "Properties > Properties > Layout > Fit to size", the "Fit object to content" option is used to specify whether WinCC adjusts to the object size of the field content:

- Enabled "Fit object to contents" option:

  WinCC automatically adjusts the size of the object to the configured format. The font size and field length are defined under "Properties > Properties > General > Text".

  The object can be moved in the working area, however, the size cannot be changed. During report output, the entire field content is output at the time of report output.
- Disabled "Fit object to contents" option:

  Customize the field size by yourself. WinCC does not resize the field for report output. It can be possible that not all content of the field is output in the report. Therefore, configure a field of sufficient size.

---

**See also**

[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Page number (RT Professional)

#### Application

The "Page number" object outputs the current page number or the total number of pages in the report in the header or footer of the report.

![Application](images/76064467979_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, change the settings for color, font, frame, alignment as well as position and object size. In particular you set the format of the page number.

#### Format

Under "Properties > General > Text > Format", specify the format of the page numbers to be displayed. You can use a wildcard for the page numbers and enter a user-specific text.

The following table shows which wildcards you can use:

| Wildcards | Value |
| --- | --- |
| "%N", or "%n" | Current page number |
| "%T", or "%t" | Total number of pages in the report |

#### Examples

The following table shows a few examples of the combination of wildcards and text:

| Format | Output example |
| --- | --- |
| Page %n of %t | Page 2 of 10 |
| %n/%t | 2/10 |

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Symbolic I/O field (Panels, Comfort Panels, RT Advanced)

#### application

With the "Symbolic I/O field" object, the content of a text list in reports is displayed, depending on the tag value. In the inspector window, the tag and text list is configured under "Properties > Properties > General":

![application](images/23690496907_DV_resource.Stream@PNG-de-DE.png)

#### Layout

In the inspector window, change the settings for color, frame, font, position and object size. In particular, the "Fit to size" is defined, by specifying whether the object size is adjusted to the text during output in the report or not.

> **Note**
>
> The "Symbolic I/O field" object is also available in "Screens" editor. In reports, the object only outputs data. Accordingly only configure the output of data for application in reports.

---

**See also**

[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Table view in reports (RT Professional)

#### Application

You use the "Table view" object to display the process data in a table. Each row of the table represents the status of the selected process tags at a specific time.

The report displays the status that the table had at the time of the start of the print job.

![Application](images/31341195659_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Reduced functional scope of the output in reports**
>
> The configuration of the object in the "Reports" editor differs only slightly compared to its configuration in the "Screens" editor.
>
> The functional scope of the object is adapted for the output in reports: In the "Reports" editor, for example, it is not possible to configure operating elements in Runtime.

#### Special features for the output in reports

By contrast to the configuration in the screen, you can assign tags with dynamic properties for the time and value columns. This way you can, for example, use a report several times.

---

**See also**

[Report design tools (RT Professional)](#report-design-tools-rt-professional)
  
[Create a report (Panels, Comfort Panels, RT Advanced, RT Professional)](#create-a-report-panels-comfort-panels-rt-advanced-rt-professional)

### Text field (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Application

The "Text field" is a closed object which you can fill with a color.

![Application](images/56785035659_DV_resource.Stream@PNG-en-US.png)

#### Layout

In the Inspector window, you customize the position, shape, style, color and font types of the object. You can adapt the following properties in particular:

- Text: Specifies the text for the text field.
- Size of text field: Defines whether the size of the object is adapted to the space required by the largest list entry.

#### Text

Specify the text for the text field in the Inspector window.

1. In the Inspector window, select "Properties > Properties > General".
2. Enter a text.

   For texts over several lines you can set a line break by pressing the key combination <Shift + Enter>.

#### Size of text field

In the Inspector window, you can define whether the size of the object is adapted to the space required by the largest list entry.

1. In the Inspector window, select "Properties > Properties > Layout".
2. Activate "Resize > Fit to contents".
