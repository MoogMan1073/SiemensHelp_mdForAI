---
title: "Displaying Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: CurvesWCCPenUS
topics: 71
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Displaying Tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Displaying tags with Basic Panels (Basic Panels)](#displaying-tags-with-basic-panels-basic-panels)
- [Displaying tags with Runtime Advanced and Panels (Panels, Comfort Panels, RT Advanced)](#displaying-tags-with-runtime-advanced-and-panels-panels-comfort-panels-rt-advanced)
- [Displaying tags with Runtime Professional (RT Professional)](#displaying-tags-with-runtime-professional-rt-professional)

## Displaying tags with Basic Panels (Basic Panels)

This section contains information on the following topics:

- [Outputting tag values in screens (Basic) (Basic Panels)](#outputting-tag-values-in-screens-basic-basic-panels)
- [Configuring trend display for values from the PLC (Basic) (Basic Panels)](#configuring-trend-display-for-values-from-the-plc-basic-basic-panels)

### Outputting tag values in screens (Basic) (Basic Panels)

#### Introduction

In runtime you can output tag values in the screens of the operator device in the form of a trend. A trend is a graphic representation of the values that a tag takes during runtime. Use the "Trend display" graphic object to represent it. Process values for the trend display are loaded by the PLC from the ongoing process.

The values to be displayed are determined individually within a fixed, configurable cycle. Cyclically-triggered trends are suitable for representing continuous curves, such as the changes in the operating temperature of a motor.

#### Displayed values

You will need to configure a trend view in a screen so that tag values are displayed on the HMI device. When configuring the trend view, specify which tag values are to be displayed.

You can control the updating of the trend display by defining the cycle time.

---

**See also**

[Configuring trend display for values from the PLC (Basic) (Basic Panels)](#configuring-trend-display-for-values-from-the-plc-basic-basic-panels)
  
[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Configuring trend display for values from the PLC (Basic) (Basic Panels)

#### Introduction

You use a trend view to graphically represent values that a tag assumes during the process.

#### Requirement

- A screen is open.
- The Inspector window with the trend view properties is open.

#### Procedure

To configure a trend view, follow these steps:

1. Add the "Trend view" object from the toolbox in the "Control" group to the screen.

   ![Procedure](images/70509893131_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/70509893131_DV_resource.Stream@PNG-de-DE.png)
2. Select the "Trend" category from the "Properties" group in the Inspector window and double-click "&lt;Add&gt;" in the "Name" column.

   ![Procedure](images/89643718667_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/89643718667_DV_resource.Stream@PNG-en-US.png)
3. Assign a name to the trend in the "Name" column.
4. In the "Style" column, use the selection button to open the "Style" dialog and select the style of the line.
5. Select the number of trend values in the "Trend values" column.
6. In the "Settings" column, use the selection button to open the "Data source" dialog and select the tags to supply the trend with values.

   Specify the cycle for reading the tags from the PLC.

   ![Procedure](images/70509935371_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/70509935371_DV_resource.Stream@PNG-en-US.png)
7. You can make other settings in the dialogs of the Inspector window. For example, you can select the "Display table" option in the "Table" category to display a value table beneath the trend view.

**Note**

If you hold down the &lt;CTRL&gt; key and double-click the trend view, the trend view is activated. You set the column width and the position of the columns in the table header of the values table in active mode. In order to activate the trend view the zoom factor has to be set to 100 %.

#### Result

In runtime, the values of the selected tags are displayed in the configured trend view.

---

**See also**

[Outputting tag values in screens (Basic) (Basic Panels)](#outputting-tag-values-in-screens-basic-basic-panels)

## Displaying tags with Runtime Advanced and Panels (Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Trends (Panels, Comfort Panels, RT Advanced)](#trends-panels-comfort-panels-rt-advanced)
- [Outputting tag values in screens (Panels, Comfort Panels, RT Advanced)](#outputting-tag-values-in-screens-panels-comfort-panels-rt-advanced)
- [Configuring trend displays for values from the PLC (Panels, Comfort Panels, RT Advanced)](#configuring-trend-displays-for-values-from-the-plc-panels-comfort-panels-rt-advanced)
- [Configuring a trend view for a data log (Panels, Comfort Panels, RT Advanced)](#configuring-a-trend-view-for-a-data-log-panels-comfort-panels-rt-advanced)
- [The structure of a *.CSV file with tags (Panels, Comfort Panels, RT Advanced)](#the-structure-of-a-csv-file-with-tags-panels-comfort-panels-rt-advanced)
- [Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)](#direct-access-to-the-odbc-log-database-panels-comfort-panels-rt-advanced)
- [Representing path trends in the trend view (Panels, Comfort Panels, RT Advanced)](#representing-path-trends-in-the-trend-view-panels-comfort-panels-rt-advanced)

### Trends (Panels, Comfort Panels, RT Advanced)

#### Introduction

A trend is a graphic representation of the values that a tag takes during runtime. In order to display trends, configure a trend view in a screen of your project.

To configure the trend view, specify a trend type for the values to be displayed.

- Log: For displaying the logged values of a tag
- Cyclical real time: For time-triggered display of values
- Bit-triggered real time: For event-triggered display of values
- Bit-triggered buffer: For event-triggered display with buffered data acquisition

#### Displaying logged values

In Runtime, the trend view displays the values of a tag from a data log. The trend shows the logged values in a particular window in time. The operator can move the time window in Runtime to view the desired information from the log.

![Displaying logged values](images/15533314059_DV_resource.Stream@PNG-en-US.png)

#### Pulse-triggered trends

The values to be displayed are determined individually with a definable time pattern. Cyclically-triggered trends are suitable for representing continuous curves, such as the changes in the operating temperature of a motor.

#### Bit-triggered trends

The values to be displayed are event-driven by setting a defined bit in "Trend transfer" tags. The bit is reset after reading has been completed. Bit-triggered trends are useful for displaying fast-changing values, such as the injection pressure for producing plastic parts.

#### Bit-triggered trends with buffered data acquisition

When you set buffered data acquisition, the values to be displayed are buffered in the PLC and read in bit-triggered as a block. These trends are suitable for displaying rapid changes when the course of the trend as a whole is interesting and not so much the individual values.

You configure a switch buffer in the PLC so it can continue to write the new values while the trend buffer is being read. The switch buffer ensures that the PLC does not overwrite values while the operator devices reads the values for the trend.

The switch between the trend buffer and the switch buffer functions as follows:

Whenever the bit assigned to the trend is set in the "Trend transfer 1" tag, all the values are read simultaneously from the trend buffer and are displayed as a trend on the HMI device. The bit in "Trend Transfer 1" is reset after reading has been completed.

While the operator device is reading the tag values from the trend buffer, the PLC writes the new tag values into the switch buffer. When the bit which is assigned to the trend is set in the "Trend transfer 2" tag , all the trend values are read from the switch buffer and displayed at the operator device. While the operating device is reading the switch buffer, the PLC writes again to the trend buffer.

![Bit-triggered trends with buffered data acquisition](images/7204318475_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Configuring a trend view for a data log (Panels, Comfort Panels, RT Advanced)](#configuring-a-trend-view-for-a-data-log-panels-comfort-panels-rt-advanced)
  
[Configuring trend displays for values from the PLC (Panels, Comfort Panels, RT Advanced)](#configuring-trend-displays-for-values-from-the-plc-panels-comfort-panels-rt-advanced)
  
[Outputting tag values in screens (Panels, Comfort Panels, RT Advanced)](#outputting-tag-values-in-screens-panels-comfort-panels-rt-advanced)
  
[Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)](#direct-access-to-the-odbc-log-database-panels-comfort-panels-rt-advanced)
  
[The structure of a *.CSV file with tags (Panels, Comfort Panels, RT Advanced)](#the-structure-of-a-csv-file-with-tags-panels-comfort-panels-rt-advanced)

### Outputting tag values in screens (Panels, Comfort Panels, RT Advanced)

#### Introduction

In runtime you can output tag values in the screens of the operator device in the form of a trend. The process values are loaded by the PLC from the current process or from a log database.

#### Displayed values

You will need to configure a trend view in a screen so that tag values are displayed on the HMI device. When configuring the trend view, specify which tag values are to be displayed.

The following options are available:

- Current values from the PLC  
  Writing of the trend is continued with individual values from the PLC. The following trigger types are available for display in real time:

  - Bit-triggered real time: The time of the update can be controlled by setting a bit. Bit-triggered trends are normally used to visualize rapidly changing values. One example might be the injection pressure in the production of plastic parts.
  - Cyclical real time: You control the update time with a cycle. Cyclically-triggered trends are suitable for representing continuous curves, such as the changes in the operating temperature of a motor.
  - Bit-triggered buffer: The trend contains values that were stored in a buffer in the period between two reads from the PLC. Use this format pattern if the course of the trend as a whole is more interesting than the individual values.
- Logged tag values  
  In runtime, the trend view displays the values of a tag from a data log. The following trigger type is available to display logged tag values:

  - Data log: The trend shows the logged values in a particular window in time. To obtain the requested information from the archive, the operator uses the corresponding operator controls in the screen or in the trend view.

---

**See also**

[Trends (Panels, Comfort Panels, RT Advanced)](#trends-panels-comfort-panels-rt-advanced)

### Configuring trend displays for values from the PLC (Panels, Comfort Panels, RT Advanced)

#### Introduction

You use a trend view to graphically represent values that a tag assumes during the process.

#### Requirement

- A screen is open.

#### Procedure

To configure a trend view, follow these steps:

1. Add the "Trend view" object from the toolbox in the "Controls" group to the screen.
2. Select "Properties . Properties &gt; Trend" in the Inspector window and double-click "Add" in the "Name" field. A new trend is created.
3. If required, enter a unique name for the trend in the "Name" field.
4. In the "Style" column, use the selection button to open the "Style" dialog and select the style of the line.
5. Select the number of trend values in the "Trend values" column.
6. In the "Trend type" column, select the required trend type. The following entries are available:

   - "Bit-triggered real time"
   - "Cyclical real time"
   - "Bit-triggered buffer"
   - "Data log"
7. In the "Settings source" column, use the selection button to open the "Data source" dialog and select the tags to supply the trend with values.

   If you selected the "Cyclical real time" trend type, specify a cycle for reading the tags from the PLC.

   Only for bit-triggered trends:

   - Under "Bit", specify which bit of the "Trend request" tag and of the "Trend transfer" tags are to be assigned to the trend. Select a different value for each trend.
   - Enter a tag under "Trend request" which contains at least as many bits as trends are to be displayed in the trend view. The status of the bits of these tags specifies which trend is currently being displayed at the operator device.

   Only for the trend type "Bit-triggered real time":

   - Enter a tag under "Trend transfer" which contains at least as many bits as trends are to be displayed in the trend view. The status of the bits of these tags specifies for which trend values are to be read from the PLC.

   Only for the trend type "Bit-triggered buffer":

   - Enter a buffer tag for the switch buffer. The tags have to be of the same type and of the same length as the trend tag.
   - Enter a tag each under "Trend transfer 1" and "Trend transfer 2" which contains at least as many bits as trends are to be displayed in the trend view. The status of these tag bits specifies the trend for which values will be read from the PLC. "Trend transfer 1" controls reading from the trend buffer; "Trend transfer 2" controls reading from the switch buffer.
8. You can make other settings in the dialogs of the Inspector window. For example, you can select the "Display table" option in the "Table" category to display a value table beneath the trend view.

> **Note**
>
> If you hold down the &lt;CTRL&gt; key and double-click the trend view, the trend view is activated. You can set the column width and the position of the columns in active mode in the values table. In order to activate the trend view the zoom factor has to be set to 100 %.

#### Result

In runtime, the values of the selected tags are displayed in the configured trend view.

---

**See also**

[Trends (Panels, Comfort Panels, RT Advanced)](#trends-panels-comfort-panels-rt-advanced)

### Configuring a trend view for a data log (Panels, Comfort Panels, RT Advanced)

#### Introduction

You can use a trend view to display logged tag values in Runtime. The trend view shows the logged tag values in a particular window in time. To obtain the requested information from the archive, the operator uses the corresponding operator controls in the screen or in the trend view.

#### Application example

At the end of a shift, for example, an operator wants information about the process carried out during the shift.

#### Requirement

- A data log has been created.
- A screen is open.
- The Inspector window with the trend view properties is open.

#### Procedure

To configure a trend view to display values from a data log, follow these steps:

1. Add the "Trend view" object from the toolbox in the "Controls" group to the screen.
2. Select "Properties . Properties &gt; Trend" in the Inspector window and double-click "Add" in the "Name" field. A new trend is created.
3. If required, enter a unique name for the trend in the "Name" field.
4. In the "Style" column, use the selection button to open the "Style" dialog and select the style of the line.
5. In the "Trend type" column, select the trend type "Data log".
6. In the "Settings" column, use the selection button to open the "Data source" dialog; select the data log and the tags to supply the trend with values.
7. You can make other settings in the dialogs of the Inspector window. For example, you can select the "Display table" option in the "Table" category to display a value table beneath the trend view.

**Note**

If you hold down the &lt;CTRL&gt; key and double-click the trend view, the trend view is activated. You can set the column width and the position of the columns in active mode in the values table. In order to activate the trend view the zoom factor has to be set to 100 %.

#### Result

In runtime, the logged values of the selected tags are displayed in the configured trend view.

---

**See also**

[Trends (Panels, Comfort Panels, RT Advanced)](#trends-panels-comfort-panels-rt-advanced)
  
[Representing path trends in the trend view (Panels, Comfort Panels, RT Advanced)](#representing-path-trends-in-the-trend-view-panels-comfort-panels-rt-advanced)

### The structure of a *.CSV file with tags (Panels, Comfort Panels, RT Advanced)

#### Introduction

In the *.csv (comma-separated value) file format, the "Name" and "Value" table columns of the entry are separated by semicolons. Each table row ends with a line break.

#### Example of a *.CSV file

The example shows a file with logged tag values:

"VarName";"TimeString";"VarValue";"Validity";"Time_ms"

"Var_107";"01.04.98 11:02:52";66,00;1;35886460322,81

"Var_108";"01.04.98 11:02:55 AM";60.00;1;35886460358.73

"Var_109";"01.04.98 11:02:57 AM";59.00;1;35886460381.22

> **Note**
>
> **Delimiters**
>
> To display the contents of "*.CSV" archives, you must ensure that the same character is not used for "Decimal separator" and "List separator" under Windows settings for "Region and language".

#### Structure of a log file in *.csv format

The following values are entered in the individual columns of a log file:

| Parameters | Description |
| --- | --- |
| VarName | Name of the tag from WinCC |
| Time string | Time stamp as a STRING, e.g. readable data format |
| VarValue | Value of the tag |
| Validity | Validity:  1 = value is valid 0 = an error occurred (e.g. interrupted connection) |
| Time_ms | Specify a time stamp as a decimal value (see below for conversion).  Only needed to display the tag values in a trend. |

#### Conversion of the time stamp decimal value

If the value needs to be processed using a different program, proceed as follows:

1. Divide Time_ms by 1,000,000.

   Example: 36343476928:1 000 000 = 36343.476928
2. The whole number portion (36344) is the date calculated from 31.12.1899.

   Example: 36343 results in 02.07.1999

   You can now convert the time stamp value to days in Excel by assigning a corresponding format from the "Date" group to the cells, which contain the time stamp.

   Result: 37986 results in 31.12.2003
3. The value after the comma (0,476928) indicates the time:

   - Multiply the value (0.476928) by 24 to obtain the hours (11.446272).
   - Multiply the remainder (0.446272) by 60 results in the minutes (26.77632).
   - Multiply the remainder (0.77632) by 60 results in the seconds (46.5792).

   Result 11:26:46.579

   This conversion is supported by Microsoft Excel, for example.

---

**See also**

[Trends (Panels, Comfort Panels, RT Advanced)](#trends-panels-comfort-panels-rt-advanced)
  
[Representing path trends in the trend view (Panels, Comfort Panels, RT Advanced)](#representing-path-trends-in-the-trend-view-panels-comfort-panels-rt-advanced)

### Direct access to the ODBC log database (Panels, Comfort Panels, RT Advanced)

#### Introduction

The storage location of a log can be a database or a file.

The database is addressed by means of its "Data source name" (DSN). Select the database you want to use in WinCC from the Windows Start menu under "Settings &gt; Control panel &gt; ODBC Data Sources".

To store log data, specify the DSN, rather than a directory name during configuration. With the DSN, you are referencing the database and the storage location.

#### Application

The entire functional scope of the database is available for additional processing and evaluation of log data.

#### Principle

The data source establishes the connection to the database. You create the data source on the same computer that contains the Runtime software. Then enter the DSN configured here when you create a log in WinCC.

The ODBC interface allows you to use other programs, such as MS Access or MS SQL Server, to access the database directly.

With the "StartProgram" system function, you can also configure a program call (to MS Access, for example) on the HMI device. This does not interrupt Runtime.

---

**See also**

[Trends (Panels, Comfort Panels, RT Advanced)](#trends-panels-comfort-panels-rt-advanced)

### Representing path trends in the trend view (Panels, Comfort Panels, RT Advanced)

#### Introduction

To visualize two-dimensional traverse paths of a machine prior to execution, for example, you can use the f(x) trend view.

#### Implementation

The implementation is based on a data log, in which the coordinates are saved with an identical time stamp.

![Implementation](images/97056032651_DV_resource.Stream@PNG-en-US.png)

The representation of value pairs in the f(x) trend view is based on a data log that reads the calculated value pairs from a CSV file. The time stamps of each value pair are identical, for example, "01/01/2010 00:00:00".

The data records in the CSV file contain the logging tags with the calculated values. You can calculate the values in the PLC, for example, and store them in two data blocks. Then you can use a VB script, for example, to create the CSV file.

The data source for the trend is the data log.

The following settings are relevant for the configuration of the data area:

- The time range must exactly match the time stamps from the CSV file
- The number of "measuring points" must exactly match the number of data records in the CSV file.

#### VB script for creating a CSV file

The following VB script generates "Input_X" and "Input_Y" from the values of the HMI tags. The HMI tags have the "Array (0..10) of Real" data type.

'###########################################################################

' Location of date log and name of data log which are used in f(x) control

Dim ObjFileName, ObjFilePath

' Name of data log

ObjFileName = "TrendControl_f(x)0.csv"

' File location for data log

ObjFilePath = "\Storage Card SD\"

'###########################################################################

' create objects to edit files and use file system

Dim ObjFile, ObjFileSystem

Set ObjFile = CreateObject("FileCtl.File")

Set ObjFileSystem = CreateObject("FileCtl.Filesystem")

'###########################################################################

' Write header into the new data log

ObjFile.LinePrint(Chr(34)&amp;"VarName"&amp;Chr(34)&amp;";"&amp;Chr(34)&amp;"TimeString"&amp;Chr(34)&amp;";"&amp;Chr(34)&amp;"VarValue"&amp;Chr(34)&amp;";"&amp;Chr(34)&amp;"Validity"&amp;Chr(34)&amp;";"&amp;Chr(34)&amp;"Time_ms"&amp;Chr(34))

If Err.Number &lt;&gt; 0 Then

ShowSystemAlarm "Error: Cannot write to data log. " &amp; Err.Number &amp; " " &amp; Err.Description

Err.Clear

OpenAllLogs

TrendControl = 3

Exit Function

End If

'###########################################################################

' Write entries into data log

' Adapt loop counter to length of archive and array of data tag

Dim ObjLoopCount

ObjLoopCount = 10 ' last element of array

Dim ObjIndex, ObjTime, ObjTimeStamp

For ObjIndex = 0 To ObjLoopCount

' Calculate time stamp

' 40179000000 = 01.01.2010 00:00:00

ObjTime = ObjIndex/(60*60*24)*1000

ObjTimeStamp = 40179000000 + ObjTime

' Write x element to log

Dim Objx

Objx = SmartTags("Input_X")(ObjIndex)

ObjFile.LinePrint(Chr(34)&amp;"Temp_x"&amp;Chr(34)&amp;";"&amp;Chr(34)&amp;"01.01.2010 00:00:00"&amp;Chr(34)&amp;";"&amp;Objx&amp;";1;"&amp;ObjTimeStamp)

' Write y element to log

Dim Objy

Objy = SmartTags("Input_Y")(ObjIndex)

ObjFile.LinePrint(Chr(34)&amp;"Temp_y"&amp;Chr(34)&amp;";"&amp;Chr(34)&amp;"01.01.2010 00:00:00"&amp;Chr(34)&amp;";"&amp;Objy&amp;";1;"&amp;ObjTimeStamp)

Next

' Write line counter to log

Dim ObjLineCount

ObjLineCount = 41

ObjFile.LinePrint(Chr(34)&amp;"$RT_COUNT$"&amp;Chr(34)&amp;";"&amp;ObjLineCount&amp;";;;;")

'###########################################################################

' Close new log

ObjFile.close

Set ObjFile = Nothing

Set ObjFileSystem = Nothing

---

**See also**

[The structure of a *.CSV file with tags (Panels, Comfort Panels, RT Advanced)](#the-structure-of-a-csv-file-with-tags-panels-comfort-panels-rt-advanced)
  
[Configuring a trend view for a data log (Panels, Comfort Panels, RT Advanced)](#configuring-a-trend-view-for-a-data-log-panels-comfort-panels-rt-advanced)

## Displaying tags with Runtime Professional (RT Professional)

This section contains information on the following topics:

- [Basics (RT Professional)](#basics-rt-professional)
- [Output of tag values in the form of a trend (RT Professional)](#output-of-tag-values-in-the-form-of-a-trend-rt-professional)
- [Output of tag values in tabular format (RT Professional)](#output-of-tag-values-in-tabular-format-rt-professional)
- [Configuring the value table (RT Professional)](#configuring-the-value-table-rt-professional)
- [Using controls in Runtime (RT Professional)](#using-controls-in-runtime-rt-professional)

### Basics (RT Professional)

This section contains information on the following topics:

- [Outputting the tag values (RT Professional)](#outputting-the-tag-values-rt-professional)
- [Table view (RT Professional)](#table-view-rt-professional)
- [Properties of the trend view (RT Professional)](#properties-of-the-trend-view-rt-professional)
- [f(t) trend view (RT Professional)](#ft-trend-view-rt-professional)
- [f(x) trend view (RT Professional)](#fx-trend-view-rt-professional)
- [Representation Trend Lines (RT Professional)](#representation-trend-lines-rt-professional)
- [Time range basics (RT Professional)](#time-range-basics-rt-professional)
- [Representation Using Common Axes (RT Professional)](#representation-using-common-axes-rt-professional)
- [Making buttons in the toolbar dynamic (RT Professional)](#making-buttons-in-the-toolbar-dynamic-rt-professional)

#### Outputting the tag values (RT Professional)

##### Overview

In Runtime you can output tag values as table or as trend. You can use either process values or logged values as source for the tag values.

Use a table, for example, for comparing tag values. In the table you can, for example, compare fill levels of supply tanks.

Use a trend, for example, for graphically displaying tag values. Using a trend you can, for example, display the development of an engine temperature.

##### Controls for displaying tag values

To display tag values in a table, use the table view.

To display tag values as a trend, use the trend view. The trend view is available in two versions:

- With the "f(t) trend view" you display a tag value against the time, e.g. a temperature trend.
- With the "f(x) trend view" you display a tag value against a second tag value, e.g. the engine speed against the heat produced.

In addition, the value table is a control with which you can create statistics from the displayed values. Furthermore, you can use the value table as reading assistance for the trend view.

##### Configuration

In the table and trend view, you configure the following properties:

- Data connection
- Display mode
- Evaluation of data
- Configuration in Runtime
- Persistence of changed properties in Runtime

---

**See also**

[Table view (RT Professional)](#table-view-rt-professional)
  
[Properties of the trend view (RT Professional)](#properties-of-the-trend-view-rt-professional)
  
[f(t) trend view (RT Professional)](#ft-trend-view-rt-professional)
  
[f(x) trend view (RT Professional)](#fx-trend-view-rt-professional)

#### Table view (RT Professional)

##### Overview

The table view in Runtime shows currently pending process values or logged values in a table. You can arrange the display of the table as you wish.

In Runtime, you create statistics from selected data. You also export the data for further use.

The following image shows a table view in which the fill levels of three supply tanks are shown:

![Overview](images/23358036619_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Outputting the tag values (RT Professional)](#outputting-the-tag-values-rt-professional)

#### Properties of the trend view (RT Professional)

##### Number of trends

Both in the "f(x) trend view" and the "f(t) trend view" you can display an unlimited number of trends. For reasons of clarity, you should not, however, configure more than 8 trends at a time.

##### Resolution of Trend Display

The number of trend values that can be displayed on the screen is limited by the screen resolution and configured size of the trend view. Therefore it is possible that fewer values are displayed in the trend view than actually exist in the period to be represented.

If, for example, in an area of 100 pixels 200 measured values are archived, each pixel represents 2 measured values. The value shown on the screen is that of the most recent data (most recent time stamp).

The figure below shows a trend characteristic where each pixel represents a value pair with 2 measured values:

![Resolution of Trend Display](images/23365468427_DV_resource.Stream@PNG-de-DE.png)

| Symbol | Meaning |
| --- | --- |
| ① | Real measured values |
| ② | Determined trend |
| ③ | Pixels |

---

**See also**

[f(t) trend view (RT Professional)](#ft-trend-view-rt-professional)
  
[f(x) trend view (RT Professional)](#fx-trend-view-rt-professional)
  
[Outputting the tag values (RT Professional)](#outputting-the-tag-values-rt-professional)

#### f(t) trend view (RT Professional)

##### Overview

With the f(t) trend view you can display currently pending process values or archived values in Runtime as a trend against the time. You can create the trend display according to your wishes.

The following figure shows an f(t) trend view displaying two trends simultaneously:

![Overview](images/23385495563_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Properties of the trend view (RT Professional)](#properties-of-the-trend-view-rt-professional)
  
[Outputting the tag values (RT Professional)](#outputting-the-tag-values-rt-professional)

#### f(x) trend view (RT Professional)

##### Overview

With the f(x) trend view you can display currently pending process values or archived values in Runtime as a trend against another tag. You can create the trend display according to your wishes.

The following figure shows an f(x) trend view displaying two trends simultaneously:

![Overview](images/18807243147_DV_resource.Stream@PNG-de-DE.png)

##### Rules for the data source

The following rules must be observed when displaying trends in the f(x) trend view:

- A trend can represent a maximum of 10000 value pairs
- The following sources are allowed to supply a trend with data:

  - Online tags
  - Logging tags
  - Recipe elements
  - User-defined: Data supply of value pairs using a script
- The value pairs are displayed in the f(x) trend view. For the value pairs to be displayed at the same time, update the online tags or logging tags of a trend at the same time in Runtime. Use the same update cycle for each tag, for example.
- The logging tags of a trend must have the same update cycle and must be recorded in a continuous cycle

---

**See also**

[Properties of the trend view (RT Professional)](#properties-of-the-trend-view-rt-professional)
  
[Outputting the tag values (RT Professional)](#outputting-the-tag-values-rt-professional)

#### Representation Trend Lines (RT Professional)

##### Introduction

In a trend view, you display a trend curve with one of the following display types:

- Dots
- Interpolated
- Stepped

Select "Properties &gt; Properties &gt; Trend &gt; Style" to configure the properties of the trend display in the Inspector window.

##### Dots

Values are shown as dots. The display of the points can be configured as you wish.

The following image shows the trend curve with the display form "Dots":

![Dots](images/23382216459_DV_resource.Stream@PNG-de-DE.png)

##### Interpolated

The trend curve is interpolated on a linear basis from the values. The display of the lines and points can be configured as you wish.

The following image shows the trend curve with the display form "Interpolated":

![Interpolated](images/23381142027_DV_resource.Stream@PNG-de-DE.png)

##### Stepped

The trend curve is interpolated as a stepped curve from the values. The display of the lines and points can be configured as you wish.

The following image shows the trend curve with the display form "Stepped":

![Stepped](images/23382076043_DV_resource.Stream@PNG-de-DE.png)

##### Trend curve

With the "Trend curve" option, you can specify where the current values for all trend windows are to be entered. Normally, the current values are written in the trend window from the right.

You configure the "trend curve" in the Inspector window under "Properties &gt; Properties &gt; General &gt; Display".

---

**See also**

[Creating trends for the trend window. (RT Professional)](#creating-trends-for-the-trend-window-rt-professional)

#### Time range basics (RT Professional)

##### Time range

The time range is the range from which the values at the HMI device are shown. The time range is determined by the start time and the end time. The time range is always in the past. If the end time is later than the current system time, the current system time is used as a temporary end time.

A distinction is made between the following time ranges:

- Static time range
- Dynamic time range

##### Static time range

The static time range is determined by fixed start and end times. The values are displayed within this time range.

##### Dynamic time range

The dynamic time range is determined by a period of time beginning with a fixed start time. The end time thus corresponds to the conclusion of the time period.

You set the time period as follows:

- Duration, e.g. 30 minutes
- The number of measurement points multiplied by the update cycle also produces a duration.

##### Configuring time range

Configure the time range for all controls. Configure the time range in the time column or in the time axis for the table view and the f(t) trend view. Configure the time range directly at the trend for the f(x) table view.

---

**See also**

[Configuring the time axes of the the trend view (RT Professional)](#configuring-the-time-axes-of-the-the-trend-view-rt-professional)
  
[Displaying logged values (RT Professional)](#displaying-logged-values-rt-professional)

#### Representation Using Common Axes (RT Professional)

##### Introduction

If you display several trends simultaneously in the trend view, assign each trend its own value and time axis. Alternatively, you can assign a shared time and/or value axis to several trends.

You configure the axes of a trend view in the Inspector window under "Properties &gt; Properties &gt; Time axis / Value axis".

The axes are assigned to the configured trends in the Inspector window under "Properties &gt; Properties &gt; Trends".

##### Representation Using Different Axes

If the values to be displayed in a trend view differ greatly, a common value axis makes no sense. If you assign each trend its own value axis, they should also display different scales. Individual axes can be hidden if required.

The following figure shows two trends with different value axes using an f(t) trend display as example:

![Representation Using Different Axes](images/23396064651_DV_resource.Stream@PNG-de-DE.png)

##### Representation Using Common Axes

If the comparability of the trend lines is important, common axes in a trend view is sensible. Connected trend views can have a common time axis.

![Representation Using Common Axes](images/23385495563_DV_resource.Stream@PNG-de-DE.png)

If you configure trends with a shared time axis, use tags with the same update cycle for the data supply.

In the case of different updating cycles, the length of the time axis is not identical for all tags. Since the trends are updated at different times due to the different updating cycles, a minimal different in the end time for the time axis occurs on each change. As a result, the trends displayed skip slightly to and fro on each change.

#### Making buttons in the toolbar dynamic (RT Professional)

##### Introduction

If you do not wish to operate the control via the toolbar, configure any operator control such as a script on an event. Each control button has a unique ID.

If you want to use a script to trigger a control button, assign the idea of the button to the "ToolbarButtonClick" property.

If you wish to determine which button of a control has been pressed, configure a VB script or a C script at the event "Click toolbar button". The ID of the button is passed on to the script as the parameter "toolbarbuttonID".

##### Example: Opening the configuration dialog for the control using VBS

To open the "Control_1" configuration dialog of the control using VBS, you have the following options:

- Call in a script of an operator control event, e.g. a button:  
  `ScreenItems("Control_1").ToolbarButtonClick = 2`
- As an alternative to the property "ToolbarButtonClick", there are also methods in VBS for operating the toolbar:  
  `Dim obj  
  Set obj = ScreenItems("Control_1")  
  obj.ShowPropertyDialog`

##### Example: Opening the configuration dialog for the control using C script

To open the "Control_1" configuration dialog of the control in a C script, you have the following options:

- `SetPropertyByConstant ("Screen_1", "Control_1", "ToolbarButtonClick", "2");`

---

**See also**

[Using the trend and table view in Runtime (RT Professional)](#using-the-trend-and-table-view-in-runtime-rt-professional)

### Output of tag values in the form of a trend (RT Professional)

This section contains information on the following topics:

- [Configure trend view (RT Professional)](#configure-trend-view-rt-professional)
- [Configuring the time axes of the the trend view (RT Professional)](#configuring-the-time-axes-of-the-the-trend-view-rt-professional)
- [Configuring the value axis of the the trend view (RT Professional)](#configuring-the-value-axis-of-the-the-trend-view-rt-professional)
- [Creating diagrams in the trend view (RT Professional)](#creating-diagrams-in-the-trend-view-rt-professional)
- [Creating trends for the trend window. (RT Professional)](#creating-trends-for-the-trend-window-rt-professional)
- [Defining the data source (RT Professional)](#defining-the-data-source-rt-professional)
- [Configuring toolbar and status bar (RT Professional)](#configuring-toolbar-and-status-bar-rt-professional)
- [Configuring the export of Runtime data (RT Professional)](#configuring-the-export-of-runtime-data-rt-professional)
- [Determining the effect of the online configuration (RT Professional)](#determining-the-effect-of-the-online-configuration-rt-professional)
- [Structure of the time format specification (RT Professional)](#structure-of-the-time-format-specification-rt-professional)
- [Structure of the date format specification (RT Professional)](#structure-of-the-date-format-specification-rt-professional)

#### Configure trend view (RT Professional)

##### Introduction

To display tag values graphically in Runtime, add a trend view to a screen. In the "Tools" task card, two trend views are contained under "Controls":

- f(x) trend view
- f(t) trend view

The axis designations are different for the two trend views:

- The f(x) trend view has an "X axis" and a "Y axis"
- The f(t) trend view has a "time axis" and a "value axis"

##### Requirement

- The screen is opened
- The Inspector window is open

##### Procedure

To configure a trend view, follow these steps:

1. Add the required trend view to the screen from the "Tools" task card.
2. Configure the appearance of the trend view in the Inspector window:

   - Configure the basic properties of the trend view, e.g. "Time base" or "Trend characteristic", under "Properties &gt; Properties &gt; General".
   - Configure the appearance of the trend view under "Properties &gt; Properties &gt; Appearance".
   - Configure the properties of the trend view in Runtime under "Properties &gt; Properties &gt; Window".
3. Configure additional diagrams, if required.
4. Configure the axes of the trend view in the Inspector window.

   - Configure the properties of the axes.
   - Assign each axis to a diagram of the trend view.
5. Enter the trends in the Inspector window that are shown in the trend view:

   - Define the "data source" for each trend.
   - Assign each trend the "diagram" in which it will be displayed.
   - Assign the axes to each trend.
   - Configure the view of each trend.
6. Configure the toolbar and status bar of the trend view.
7. If required, configure the data export from the trend view.
8. If required, configure the security settings of the trend view.

##### Result

The trend view is configured. Define an additional value display if you want to evaluate the data of the trend view in Runtime. You can also configure the value display as a "Ruler".

---

**See also**

[Configuring the time axes of the the trend view (RT Professional)](#configuring-the-time-axes-of-the-the-trend-view-rt-professional)
  
[Configuring the value axis of the the trend view (RT Professional)](#configuring-the-value-axis-of-the-the-trend-view-rt-professional)
  
[Creating diagrams in the trend view (RT Professional)](#creating-diagrams-in-the-trend-view-rt-professional)
  
[Creating trends for the trend window. (RT Professional)](#creating-trends-for-the-trend-window-rt-professional)
  
[Defining the data source (RT Professional)](#defining-the-data-source-rt-professional)
  
[Configuring toolbar and status bar (RT Professional)](#configuring-toolbar-and-status-bar-rt-professional)
  
[Configuring the export of Runtime data (RT Professional)](#configuring-the-export-of-runtime-data-rt-professional)
  
[Determining the effect of the online configuration (RT Professional)](#determining-the-effect-of-the-online-configuration-rt-professional)
  
[Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)

#### Configuring the time axes of the the trend view (RT Professional)

##### Introduction

The time range for trend display is configured with time axes. In a trend view you can create several time axes, which you can assign to one or more diagrams.

If you assign several time axes to a trend view, the sequence of the time axes in the Inspector window corresponds to the sequence in the trend view. If several time axes are aligned to the same side of a trend display, the first time axis in the list takes the lower left position. The last time axis takes the upper right position.

The time axis is available only with the f(t) trend display.

##### Requirement

- The trend view is selected in the screen
- The Inspector window is open

##### Procedure

To configure the time axis of a trend view, follow these steps:

1. Double-click "Add" in the Inspector window under "Properties &gt; Properties &gt; Time axis" to add a new time axis.
2. Enter the "Name" and "Display name" of the time axis.
3. Configure the "axis style".
4. Select the "diagram" to which the time axis will be assigned.
5. Configure the "time range" and "format" of the time display of the time axis.
6. To always update the trends assigned to the time axis in the trend view, activate "Online".

   If you want to compare a current trend display with an earlier trend display, for example, supply the comparison trend from a logging tag.

**Note**

**Printing a fixed time range**

If you want to print a defined time range, deactivate "Online".

##### Result

The time axis is configured. Assign the time axis to one or several trends.

---

**See also**

[Time range basics (RT Professional)](#time-range-basics-rt-professional)
  
[Structure of the time format specification (RT Professional)](#structure-of-the-time-format-specification-rt-professional)
  
[Structure of the date format specification (RT Professional)](#structure-of-the-date-format-specification-rt-professional)

#### Configuring the value axis of the the trend view (RT Professional)

##### Introduction

In a trend view you can create several value axes, which you can assign to one or more diagrams.

The following properties are set by default with a value axis:

- The value range is based on the current values of the assigned trend
- The value axis scale is linear to the value range

Alternatively, you can configure a logarithmic scale:

- In logarithmic scaling, only positive values are displayed.
- In negative logarithmic scaling, only negative values are displayed.

If you configure a value axis for the f(t) trend view, you can also set up axis sections. A value range and a display name are assigned to an axis section.

In the f(x) trend view, the value axis corresponds to both the "X axis" and the "Y axis".

##### Requirement

- The trend view is selected in the screen
- The Inspector window is open

##### Procedure

To configure the value axis of a trend view, follow these steps:

1. Double-click "Add" in the Inspector window under "Properties &gt; Properties &gt; Value axis" to add a new value axis.
2. Enter the "Name" and "Display name" of the value axis.
3. Configure the "axis style".
4. Select the "diagram" to which the value axis will be assigned.
5. If required, configure the "value range" of the value axis.
6. If required, configure the "format" of the value axis labels.
7. If required, configure the "scaling" of the value axis.
8. If you configure an f(t) trend view, you can define "axis sections" if necessary:

   - Activate "User-defined axis sections".
   - To add an axis section, double-click on "Add".
   - Enter the "value range" of the axis section.
   - Configure the "display range" of the axis section.
   - Enter the "display name" of the axis section.

##### Result

The value axis is configured. Assign the value axis to one or several trends.

#### Creating diagrams in the trend view (RT Professional)

##### Introduction

A trend view is assigned a display range as standard, in which you can configure one or more trends.

Alternatively, you can subdivide the display range into several "diagrams". Each "diagram" functions like a standalone trend view. In this way, for example, temperature changes can be displayed clearly without overlapping trends. You can set the height of a diagram using "Range proportion". The "range proportion" establishes how much room is made available to a diagram in the trend view.

##### Calculation of range proportion

The amount of each range proportion can be calculated from the total number of range components. If, for example, you have configured a total of three diagrams, a range proportion of "1" each will result in three diagrams of equal size. To increase the size of range components in relation to each other, increase the range proportion of one or more diagrams. Changes to the range proportions immediately affect the trend view.

##### Requirement

- Trend view is selected
- The Inspector window is open

##### Procedure

Proceed as follows to subdivide a trend view into several diagrams:

1. Double-click on "Add" under "Properties &gt; Properties &gt; Diagrams" in the Inspector window.

   The diagram is added.
2. Enter a meaningful "Name" for the diagram.
3. Select the "range proportion" for the diagram in the trend view.
4. Configure the diagram "grid".
5. Configure the diagram "ruler".

##### Result

The diagram has been created. You can assign one or more trends to each diagram.

#### Creating trends for the trend window. (RT Professional)

##### Introduction

A trend allows you to represent values in the trend view. You assign a time axis and value axis to each trend. The value axis assigned to the trend determines the trend view in which the trend will be displayed.

By default, the data area is based on the current values of the assigned trend.

You can also configure the visualization of limits and values with "uncertain status" for a trend. If a trend exceeds or falls below a configured limit, the trend is colored.

If you assign several trends to a trend view, the sequence of the trends in the Inspector window corresponds to the sequence in the trend view.

##### Requirement

- The trend view is selected in the screen
- Time axes and value axes are configured
- Tags for the data source are configured
- The Inspector window is open

##### Procedure

To add a trend, follow these steps:

1. Double-click on "Add" under "Properties &gt; Properties &gt; Trends" in the Inspector window.
2. Enter a "label" for the trend.
3. If required, configure the "style" of the trend.

   The changes are shown in a preview.
4. Configure the data source.
5. If required, configure the "data area" of the trend.
6. Select the "diagram" in which the trend will be displayed.
7. Assign a "value axis" and "time axis" to the trend.
8. If required, configure the "limits" of the trend.

##### Result

The trend is configured.

---

**See also**

[Representation Trend Lines (RT Professional)](#representation-trend-lines-rt-professional)
  
[Defining the data source (RT Professional)](#defining-the-data-source-rt-professional)

#### Defining the data source (RT Professional)

##### Introduction

Using the data source, you define the sources from which the values are displayed on the HMI device in Runtime. The following sources are available:

- Current process values from tags
- Archived values from logging tags
- Recipe elements (only f(x) trend view)
- Data supply by means of script in Runtime

##### Requirements

- An online tag or logging tag is configured
- Value column or trend has been created
- The Inspector window is open

##### Displaying current process values

Proceed as follows to display current process values:

1. Click "Properties &gt; Properties &gt; Value columns" in the Inspector window to define the data source for a table view.
2. Click "Properties &gt; Properties &gt; Trends" in the Inspector window to define the data source for a trend view.
3. Configure the "data source":

   - Select the entry "Tags" as "Source".
   - If you configure the trend of an f(x) trend view, select one tag each from "X values" and "Y values".
   - If you configure the trend of an f(t) trend view or a value column, select a "tag".
   - Select the "update cycle".

##### Displaying values from a log

Proceed as follows to display values from a log:

1. Click "Properties &gt; Properties &gt; Value columns" in the Inspector window to define the data source for a table view.
2. Click "Properties &gt; Properties &gt; Trends" in the Inspector window to define the data source for a trend view.
3. Configure the "data source":

   - Select the entry "Logging tags" as "Source".
   - If you configure the trend of an f(x) trend view, select one tag each from "X values" and "Y values".
   - If you configure the trend of an f(t) trend view or a value column, select a "tag".

##### Displaying values from recipes

Output values from recipes in a f(x) trend view.

Proceed as follows to display values from a recipe:

1. In the Inspector window, configure the "data source" under "Properties &gt; Properties &gt; Trends":

   - Select the entry "Recipe" as "Source".
   - Under "X values" and "Y values" select one recipe element each.

##### Setting up user-defined data supply in Runtime

If you want to supply the trend values with data by means of scripts in Runtime, you require a script via the API interface.

To create a connection using scripts in Runtime, proceed as follows:

1. In the Inspector window, configure the "data source" under "Properties &gt; Properties &gt; Trends":

   - Select the entry "User-defined" as "Source".
   - Connect the script via the API interface to the corresponding trend.

##### Result

The data supply is configured.

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-principles-for-data-logging-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configure trend view (RT Professional)](#configure-trend-view-rt-professional)
  
[Creating trends for the trend window. (RT Professional)](#creating-trends-for-the-trend-window-rt-professional)

#### Configuring toolbar and status bar (RT Professional)

##### Introduction

You operate the controls in Runtime using the buttons in the toolbar. The status bar displays status messages from the control. During configuration, set the content of the toolbar and status bar.

##### Requirement

- The table view is selected in the screen.
- The Inspector window is open

##### Configuring the toolbar

Proceed as follows to configure the toolbar:

1. In the Inspector window, configure the general properties of the toolbar, such as orientation and background color, under "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - General".
2. In the Inspector window, activate the buttons you need in Runtime under "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - Buttons".

   For information on the functions of the individual buttons, refer to the description of the corresponding WinCC control at "Operation in Runtime".
3. To set the order of the buttons, select the buttons in the list. You can then move the buttons to the desired position.
4. If needed, you can define a "hotkey" for the buttons on the toolbar.
5. If necessary, select the authorization needed to operate the buttons in Runtime.
6. If a button should not be operated in Runtime, unselect "Activate".

   You can reactivate a deactivated a button using a script in Runtime, for example.

##### Configuring the status bar

Proceed as follows to configure the status bar:

1. In the Inspector window, configure the general properties of the status bar, such as orientation and background color, under "Properties &gt; Properties &gt; Status bar &gt; Status bar - General".
2. In the Inspector window, activate the elements you need in Runtime under "Properties &gt; Properties &gt; Status bar &gt; Status bar - Elements".

   For further information on status bar elements, refer to the descriptions of the corresponding WinCC control at "Operation in runtime".
3. To set the order of the elements, select the element in the list. You can then move the element to the desired position.
4. To adjust the width of an element in the status bar, deactivate "Auto-size". You can then enter the width in pixels.

---

**See also**

[Using the trend and table view in Runtime (RT Professional)](#using-the-trend-and-table-view-in-runtime-rt-professional)
  
[Configure trend view (RT Professional)](#configure-trend-view-rt-professional)
  
[Elements of the status bar (RT Professional)](#elements-of-the-status-bar-rt-professional)

#### Configuring the export of Runtime data (RT Professional)

##### Introduction

In Runtime, you can export the displayed data of a control in CSV format. Depending on the control used and the configuration, the user exports all data or only the selected data.

The filename and location of the CSV file are set by the operator on export. Alternatively, you can generate the filename automatically from the following wildcards:

- @OBJECTNAME: Object name of the control
- @CURRENTDATE: Current date
- @CURRENTTIME: Current time

##### Requirement

- The control is selected in the screen
- The Inspector window is open

##### Procedure

To configure the export of Runtime data, proceed as follows:

1. In the Inspector window, open "Properties &gt; Properties &gt; Data export".

   The data export settings are already configured.
2. If necessary, enter your own filename and a path for the export file.
3. Select the "scope" of the data export.
4. Configure the "Operation in Runtime".
5. So that the operator can start the data export, activate "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - Buttons &gt; Export Data" in the Inspector window.

##### Result

In Runtime, the operator can export the data of the control via the toolbar.

---

**See also**

[Configure trend view (RT Professional)](#configure-trend-view-rt-professional)

#### Determining the effect of the online configuration (RT Professional)

##### Introduction

In WinCC you configure the appearance and function of a control in Runtime. In addition, you can allow the operator to configure a control in Runtime. You can set whether changes to configuration in Runtime are retained, such as after a screen change, in the control under "Properties &gt; Properties &gt; Security &gt; Persistence".

- No persistence

  The changes to the configuration are not saved. The changes are discarded on the next screen change and when the project is rejected.
- Persistence

  The changes to the configuration are saved. The changes are retained even after the project is deactivated and activated. You may also select "Response at screen change" to discard changes at the screen change.
- Persistence in Runtime

  The changes to the configuration are only saved during Runtime. If you deactivate the project, the changes are discarded. You may also select "Response at screen change" to discard changes at the screen change.

  > **Note**
  >
  > If you change a configured control and load it onto the HMI device, the changes are overwritten in Runtime regardless of the settings.

##### Requirement

- A configured control
- The Inspector window is open

##### Procedure

To configure the persistence of data in Runtime, proceed as follows:

1. In the Inspector window, open "Properties &gt; Properties &gt; Security".
2. Select "Online configuration".
3. If needed, select the authorization.
4. Select the "Behavior on screen change".

##### Result

The behavior in online configuration is now set. In Runtime, depending on the settings, the user can adjust the configuration of the control.

If several operators are working on the HMI device, the individual configurations are accepted on a change of operator only following a screen change.

---

**See also**

[Configure trend view (RT Professional)](#configure-trend-view-rt-professional)
  
[Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)

#### Structure of the time format specification (RT Professional)

##### Time format

You can overwrite the default time formats of the selection list.

If you want to define your own time formats, note the following:

- Spaces that separate values in the format specification are set at the same position in the time display.
- Note that the entry is case-sensitive.
- Characters that are set in single quotation marks are set unchanged at the same position in the time display.

To set up a format specification, use the following values:

| Value | Description |
| --- | --- |
| h | Hours, 12-hour clock, for single-digit hours without leading zero |
| hh | Hours, 12-hour clock, for single-digit hours with leading zero |
| H | Hours, 24-hour clock, for single-digit hours without leading zero |
| HH | Hours, 24-hour clock, for single-digit hours with leading zero |
| m | Minutes, without leading zero for single-digit minutes |
| mm | Minutes, with leading zero for single-digit minutes |
| s | Seconds, without leading zero for single-digit seconds |
| ss | Seconds, with leading zero for single-digit seconds |
| t | Single-digit AM/PM time identifier: A or P |
| tt | Two-digit AM/PM time identifier: AM or PM |

##### Example

To set up the time display "11:29:40 PM", use the following format specification:

"hh:mm:ss tt"

#### Structure of the date format specification (RT Professional)

##### Time format

The default date formats of the selection list can be overwritten.

When you specify your own date formats, note the following:

- Spaces that separate values in the format specification are set in the same position in the date display.
- Note that the entry is case-sensitive.
- Characters that are set in single quotation marks are set unchanged at the same position in the date display.

To set up a format specification, use the following values:

| Value | Description |
| --- | --- |
| D | Day of the month as number, for single-digit days without leading zero |
| Dd | Day of the month as number, for single-digit days with leading zero |
| Ddd | Weekday shortened with three letters |
| Dddd | Weekday in full form |
| M | Month as number, for single-digit month without leading zero |
| MM | Month as number, for single-digit month with leading zero |
| MMM | Month shortened with three letters |
| MMMM | Month in full form |
| y | Year, only the last two numbers, for years under 10 with leading zero, same as "YY" format |
| yy | Year, only the last two numbers, for years under 10 with leading zero |
| yyyy | Complete, four-digit year specification |

##### Example

Use the following format specification to set up the date display "Wed, Aug 31 13":

"Ddd, MMM dd yy"

### Output of tag values in tabular format (RT Professional)

This section contains information on the following topics:

- [Configuring the Table View (RT Professional)](#configuring-the-table-view-rt-professional)
- [Configuring the time columns of the table view (RT Professional)](#configuring-the-time-columns-of-the-table-view-rt-professional)
- [Configuring the value columns of the table view (RT Professional)](#configuring-the-value-columns-of-the-table-view-rt-professional)
- [Configuring the appearance of the table elements (RT Professional)](#configuring-the-appearance-of-the-table-elements-rt-professional)
- [Configuration of the marking of selected cells and rows (RT Professional)](#configuration-of-the-marking-of-selected-cells-and-rows-rt-professional)
- [Configuring table column sorting (RT Professional)](#configuring-table-column-sorting-rt-professional)
- [Defining the data source (RT Professional)](#defining-the-data-source-rt-professional-1)
- [Configuring toolbar and status bar (RT Professional)](#configuring-toolbar-and-status-bar-rt-professional-1)
- [Configuring the export of Runtime data (RT Professional)](#configuring-the-export-of-runtime-data-rt-professional-1)
- [Determining the effect of the online configuration (RT Professional)](#determining-the-effect-of-the-online-configuration-rt-professional-1)
- [Structure of the time format specification (RT Professional)](#structure-of-the-time-format-specification-rt-professional-1)
- [Structure of the date format specification (RT Professional)](#structure-of-the-date-format-specification-rt-professional-1)

#### Configuring the Table View (RT Professional)

##### Introduction

To display tag values in tables in Runtime, add a table view to a screen. A time stamp is displayed for each value. The values are displayed in value columns, and the time stamps in time columns. Assign the time column to one or several value columns.

##### Procedure

Proceed as follows to configure a table view:

1. Add the required table view to the screen from the "Tools" task card.
2. Configure the appearance of the table view in the Inspector window:

   - Configure the basic properties of the table view, e.g. "Time base", under "Properties &gt; Properties &gt; General".
   - Configure the appearance of the table view under "Properties &gt; Properties &gt; Appearance".
   - Configure the properties of the table view in Runtime under "Properties &gt; Properties &gt; "Window".
3. Configure the columns of the table view in the Inspector window.

   - Configure the properties of the columns.
   - Configure one or more time columns with the time ranges for the table.
   - Configure one or more value columns.
   - Define the data connection for each value column.
   - Assign time columns to the value columns.
4. Configure the appearance of each trend:

   - Configure the "Headers", the "Structure" and the "Grid".
   - If needed, configure the settings for "selecting" table entries.
   - If needed, configure the settings for sorting table entries.
5. Configure the toolbar and status bar of the table view.
6. If required, configure the data export from the table view.
7. If required, configure the security settings of the table view.

##### Result

The table view is configured. Define an additional value table if you want to evaluate the data of the table view in Runtime. You can also configure the value table as "Ruler".

---

**See also**

[Configuring the time columns of the table view (RT Professional)](#configuring-the-time-columns-of-the-table-view-rt-professional)
  
[Configuring the value columns of the table view (RT Professional)](#configuring-the-value-columns-of-the-table-view-rt-professional)
  
[Configuring the appearance of the table elements (RT Professional)](#configuring-the-appearance-of-the-table-elements-rt-professional)
  
[Configuration of the marking of selected cells and rows (RT Professional)](#configuration-of-the-marking-of-selected-cells-and-rows-rt-professional)
  
[Configuring table column sorting (RT Professional)](#configuring-table-column-sorting-rt-professional)
  
[Making buttons in the toolbar dynamic (RT Professional)](#making-buttons-in-the-toolbar-dynamic-rt-professional)
  
[Defining the data source (RT Professional)](#defining-the-data-source-rt-professional-1)
  
[Configuring toolbar and status bar (RT Professional)](#configuring-toolbar-and-status-bar-rt-professional-1)
  
[Configuring the export of Runtime data (RT Professional)](#configuring-the-export-of-runtime-data-rt-professional-1)
  
[Determining the effect of the online configuration (RT Professional)](#determining-the-effect-of-the-online-configuration-rt-professional-1)
  
[Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)

#### Configuring the time columns of the table view (RT Professional)

##### Introduction

The time range for the tabular display is configured via time columns. A table can have separate time columns for several value columns or a common time column.

If you assign several time columns to a table view, the sequence of the time columns in the Inspector window corresponds to the sequence in the table view.

##### Requirement

- The table view is selected in the screen.
- The Inspector window is open

##### Procedure

To configure the time column of a table view, follow these steps:

1. Click "Add" in the Inspector window under "Properties &gt; Properties &gt; Time columns" to add time columns.
2. Enter the "Name" and "Label" of the time column.
3. Configure the "Style" of the time column.
4. Configure the "time range" and "format" of the time display of the time column.
5. Configure the appearance of the "Header" and "Cells".
6. If the values of the time column should be updated automatically, activate "Update".

##### Result

The time column is configured. Assign the time column to one or several value columns.

---

**See also**

[Configuring the value columns of the table view (RT Professional)](#configuring-the-value-columns-of-the-table-view-rt-professional)
  
[Structure of the time format specification (RT Professional)](#structure-of-the-time-format-specification-rt-professional-1)
  
[Structure of the date format specification (RT Professional)](#structure-of-the-date-format-specification-rt-professional-1)

#### Configuring the value columns of the table view (RT Professional)

##### Introduction

You configure the values of the table view via value columns. You can display several value columns in a table, e.g. to compare the fill levels of several containers. Every value column is connected with a time column. The value columns can have a common time column.

If you assign several value columns to a table view, the sequence of the value columns in the Inspector window corresponds to the sequence in the table view. If you assign several value columns to the same time column, the value columns in the list are automatically grouped according to assigned time column.

##### Requirement

- The table view is selected in the screen.
- The Inspector window is open
- The time column is created

##### Procedure

Proceed as follows to configure a value column:

1. Double-click "Add" in the Inspector window under "Properties &gt; Properties &gt; Value columns" to add a new value column.
2. Enter the "Name" and "Label" of the value column.
3. Configure the data source.
4. Assign a time column to the value column.
5. If required, configure the appearance of the "Header" and "Cells".
6. If required, configure the "Sorting" of the value column.

##### Result

The value column is configured.

---

**See also**

[Defining the data source (RT Professional)](#defining-the-data-source-rt-professional)
  
[Configuring the time columns of the table view (RT Professional)](#configuring-the-time-columns-of-the-table-view-rt-professional)
  
[Defining the data source (RT Professional)](#defining-the-data-source-rt-professional-1)

#### Configuring the appearance of the table elements (RT Professional)

##### Introduction

You can adjust the appearance of the table elements to your needs.

##### Requirement

- The table view or value table is selected in the screen.
- The Inspector window is open

##### Procedure

Proceed as follows to configure the colors of the table elements:

1. Define the following properties in the Inspector window under "Properties &gt; Properties &gt; Table &gt; Table - Header":

   - Visibility of the column headers and row headers
   - Alignment of the column headers and row headers
   - Color design of column headers
2. Define the following properties in the Inspector window under "Properties &gt; Properties &gt; Table &gt; Table - Structure":

   - Color design of table content, such as different colors for rows for better differentiation
   - Visibility of empty columns and rows
3. Define the following properties in the Inspector window under "Properties &gt; Properties &gt; Table &gt; Table - Grid":

   - Design of grid lines
   - Character spacing in the table cells

##### Result

The appearance of the table elements is configured. You can also define further properties:

- Behavior and color design when selecting a table entry
- Table entry sorting

---

**See also**

[Configuration of the marking of selected cells and rows (RT Professional)](#configuration-of-the-marking-of-selected-cells-and-rows-rt-professional)
  
[Configuring table column sorting (RT Professional)](#configuring-table-column-sorting-rt-professional)

#### Configuration of the marking of selected cells and rows (RT Professional)

##### Introduction

If, for example, an operator wants to export values from a row, he must select the row. During configuration, define the following:

- Selection area

  For the selection area, configure the following properties:

  - Number of table elements that the operator can select
  - Design of selection area
- Color design of selection area

  Select the colors individually or use a default system-defined color.

##### Requirement

- The table view is selected in the screen.
- The Inspector window is open

##### Procedure

To configure the selection area, follow these steps:

1. In the Inspector window, select the "type" of selection area under "Properties &gt; Properties &gt; Table &gt; Table - Selection &gt; Selection area".
2. If needed, select the "frame" to be displayed around the selection area.
3. Choose the colors for the "cells", "rows", and "frame" as needed.

##### Result

The selection area of the table view is configured. To export the data from a selected area, configure the "data export". To evaluate the data from a selected area, configure a "value display".

---

**See also**

[Defining the data source (RT Professional)](#defining-the-data-source-rt-professional-1)

#### Configuring table column sorting (RT Professional)

##### Introduction

If the operator is to be able to sort individual table columns in Runtime, configure the sorting within the table.

Depending on the configuration, the operator can sort a table column as follows:

- Clicking or double-clicking on the column header
- Clicking on a sorting button

  The sorting button is used to sort the selected column in the configured order. For the sorting button to appear, you must configure a vertical scroll bar.

##### Requirement

- The table view or value table is selected in the screen.
- The Inspector window is open

##### Procedure

To configure the sorting within a table, follow these steps:

1. In the Inspector window, select "Properties &gt; Properties &gt; Table &gt; Table - Sorting &gt; Sort by column header", "Sort with double-click", or "Sort with click".
2. Select the "Sorting order" option.
3. If needed, activate "Display sorting icon" and "Display sorting index".
4. If needed, activate "Display sorting button".
5. If you use the sorting button, select "Properties &gt; Properties &gt; Window &gt; Scroll &gt; Vertical scrollbar &gt; Always" in the Inspector window.

##### Result

The sorting of the table columns is configured.

#### Defining the data source (RT Professional)

##### Introduction

Using the data source, you define the sources from which the values are displayed on the HMI device in Runtime. The following sources are available:

- Current process values from tags
- Archived values from logging tags
- Recipe elements (only f(x) trend view)
- Data supply by means of script in Runtime

##### Requirements

- An online tag or logging tag is configured
- Value column or trend has been created
- The Inspector window is open

##### Displaying current process values

Proceed as follows to display current process values:

1. Click "Properties &gt; Properties &gt; Value columns" in the Inspector window to define the data source for a table view.
2. Click "Properties &gt; Properties &gt; Trends" in the Inspector window to define the data source for a trend view.
3. Configure the "data source":

   - Select the entry "Tags" as "Source".
   - If you configure the trend of an f(x) trend view, select one tag each from "X values" and "Y values".
   - If you configure the trend of an f(t) trend view or a value column, select a "tag".
   - Select the "update cycle".

##### Displaying values from a log

Proceed as follows to display values from a log:

1. Click "Properties &gt; Properties &gt; Value columns" in the Inspector window to define the data source for a table view.
2. Click "Properties &gt; Properties &gt; Trends" in the Inspector window to define the data source for a trend view.
3. Configure the "data source":

   - Select the entry "Logging tags" as "Source".
   - If you configure the trend of an f(x) trend view, select one tag each from "X values" and "Y values".
   - If you configure the trend of an f(t) trend view or a value column, select a "tag".

##### Displaying values from recipes

Output values from recipes in a f(x) trend view.

Proceed as follows to display values from a recipe:

1. In the Inspector window, configure the "data source" under "Properties &gt; Properties &gt; Trends":

   - Select the entry "Recipe" as "Source".
   - Under "X values" and "Y values" select one recipe element each.

##### Setting up user-defined data supply in Runtime

If you want to supply the trend values with data by means of scripts in Runtime, you require a script via the API interface.

To create a connection using scripts in Runtime, proceed as follows:

1. In the Inspector window, configure the "data source" under "Properties &gt; Properties &gt; Trends":

   - Select the entry "User-defined" as "Source".
   - Connect the script via the API interface to the corresponding trend.

##### Result

The data supply is configured.

---

**See also**

[Basics of tags (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](Working%20with%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basics-of-tags-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Basic principles for data logging (Panels, Comfort Panels, RT Advanced, RT Professional)](Archive%20tags%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#basic-principles-for-data-logging-panels-comfort-panels-rt-advanced-rt-professional)
  
[Configuring the Table View (RT Professional)](#configuring-the-table-view-rt-professional)
  
[Configuring the value columns of the table view (RT Professional)](#configuring-the-value-columns-of-the-table-view-rt-professional)

#### Configuring toolbar and status bar (RT Professional)

##### Introduction

You operate the controls in Runtime using the buttons in the toolbar. The status bar displays status messages from the control. During configuration, set the content of the toolbar and status bar.

##### Requirement

- The table view is selected in the screen.
- The Inspector window is open

##### Configuring the toolbar

Proceed as follows to configure the toolbar:

1. In the Inspector window, configure the general properties of the toolbar, such as orientation and background color, under "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - General".
2. In the Inspector window, activate the buttons you need in Runtime under "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - Buttons".

   For information on the functions of the individual buttons, refer to the description of the corresponding WinCC control at "Operation in Runtime".
3. To set the order of the buttons, select the buttons in the list. You can then move the buttons to the desired position.
4. If needed, you can define a "hotkey" for the buttons on the toolbar.
5. If necessary, select the authorization needed to operate the buttons in Runtime.
6. If a button should not be operated in Runtime, unselect "Activate".

   You can reactivate a deactivated a button using a script in Runtime, for example.

##### Configuring the status bar

Proceed as follows to configure the status bar:

1. In the Inspector window, configure the general properties of the status bar, such as orientation and background color, under "Properties &gt; Properties &gt; Status bar &gt; Status bar - General".
2. In the Inspector window, activate the elements you need in Runtime under "Properties &gt; Properties &gt; Status bar &gt; Status bar - Elements".

   For further information on status bar elements, refer to the descriptions of the corresponding WinCC control at "Operation in runtime".
3. To set the order of the elements, select the element in the list. You can then move the element to the desired position.
4. To adjust the width of an element in the status bar, deactivate "Auto-size". You can then enter the width in pixels.

---

**See also**

[Using the trend and table view in Runtime (RT Professional)](#using-the-trend-and-table-view-in-runtime-rt-professional)
  
[Configuring the Table View (RT Professional)](#configuring-the-table-view-rt-professional)
  
[Elements of the status bar (RT Professional)](#elements-of-the-status-bar-rt-professional)

#### Configuring the export of Runtime data (RT Professional)

##### Introduction

In Runtime, you can export the displayed data of a control in CSV format. Depending on the control used and the configuration, the user exports all data or only the selected data.

The filename and location of the CSV file are set by the operator on export. Alternatively, you can generate the filename automatically from the following wildcards:

- @OBJECTNAME: Object name of the control
- @CURRENTDATE: Current date
- @CURRENTTIME: Current time

##### Requirement

- The control is selected in the screen
- The Inspector window is open

##### Procedure

To configure the export of Runtime data, proceed as follows:

1. In the Inspector window, open "Properties &gt; Properties &gt; Data export".

   The data export settings are already configured.
2. If necessary, enter your own filename and a path for the export file.
3. Select the "scope" of the data export.
4. Configure the "Operation in Runtime".
5. So that the operator can start the data export, activate "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - Buttons &gt; Export Data" in the Inspector window.

##### Result

In Runtime, the operator can export the data of the control via the toolbar.

---

**See also**

[Configuring the Table View (RT Professional)](#configuring-the-table-view-rt-professional)

#### Determining the effect of the online configuration (RT Professional)

##### Introduction

In WinCC you configure the appearance and function of a control in Runtime. In addition, you can allow the operator to configure a control in Runtime. You can set whether changes to configuration in Runtime are retained, such as after a screen change, in the control under "Properties &gt; Properties &gt; Security &gt; Persistence".

- No persistence

  The changes to the configuration are not saved. The changes are discarded on the next screen change and when the project is rejected.
- Persistence

  The changes to the configuration are saved. The changes are retained even after the project is deactivated and activated. You may also select "Response at screen change" to discard changes at the screen change.
- Persistence in Runtime

  The changes to the configuration are only saved during Runtime. If you deactivate the project, the changes are discarded. You may also select "Response at screen change" to discard changes at the screen change.

  > **Note**
  >
  > If you change a configured control and load it onto the HMI device, the changes are overwritten in Runtime regardless of the settings.

##### Requirement

- A configured control
- The Inspector window is open

##### Procedure

To configure the persistence of data in Runtime, proceed as follows:

1. In the Inspector window, open "Properties &gt; Properties &gt; Security".
2. Select "Online configuration".
3. If needed, select the authorization.
4. Select the "Behavior on screen change".

##### Result

The behavior in online configuration is now set. In Runtime, depending on the settings, the user can adjust the configuration of the control.

If several operators are working on the HMI device, the individual configurations are accepted on a change of operator only following a screen change.

---

**See also**

[Configuring the Table View (RT Professional)](#configuring-the-table-view-rt-professional)
  
[Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)

#### Structure of the time format specification (RT Professional)

##### Time format

You can overwrite the default time formats of the selection list.

If you want to define your own time formats, note the following:

- Spaces that separate values in the format specification are set at the same position in the time display.
- Note that the entry is case-sensitive.
- Characters that are set in single quotation marks are set unchanged at the same position in the time display.

To set up a format specification, use the following values:

| Value | Description |
| --- | --- |
| h | Hours, 12-hour clock, for single-digit hours without leading zero |
| hh | Hours, 12-hour clock, for single-digit hours with leading zero |
| H | Hours, 24-hour clock, for single-digit hours without leading zero |
| HH | Hours, 24-hour clock, for single-digit hours with leading zero |
| m | Minutes, without leading zero for single-digit minutes |
| mm | Minutes, with leading zero for single-digit minutes |
| s | Seconds, without leading zero for single-digit seconds |
| ss | Seconds, with leading zero for single-digit seconds |
| t | Single-digit AM/PM time identifier: A or P |
| tt | Two-digit AM/PM time identifier: AM or PM |

##### Example

To set up the time display "11:29:40 PM", use the following format specification:

"hh:mm:ss tt"

#### Structure of the date format specification (RT Professional)

##### Time format

The default date formats of the selection list can be overwritten.

When you specify your own date formats, note the following:

- Spaces that separate values in the format specification are set in the same position in the date display.
- Note that the entry is case-sensitive.
- Characters that are set in single quotation marks are set unchanged at the same position in the date display.

To set up a format specification, use the following values:

| Value | Description |
| --- | --- |
| D | Day of the month as number, for single-digit days without leading zero |
| Dd | Day of the month as number, for single-digit days with leading zero |
| Ddd | Weekday shortened with three letters |
| Dddd | Weekday in full form |
| M | Month as number, for single-digit month without leading zero |
| MM | Month as number, for single-digit month with leading zero |
| MMM | Month shortened with three letters |
| MMMM | Month in full form |
| y | Year, only the last two numbers, for years under 10 with leading zero, same as "YY" format |
| yy | Year, only the last two numbers, for years under 10 with leading zero |
| yyyy | Complete, four-digit year specification |

##### Example

Use the following format specification to set up the date display "Wed, Aug 31 13":

"Ddd, MMM dd yy"

### Configuring the value table (RT Professional)

This section contains information on the following topics:

- [Value table basics (RT Professional)](#value-table-basics-rt-professional)
- [Configuring the value table (RT Professional)](#configuring-the-value-table-rt-professional-1)
- [Configuring toolbar and status bar (RT Professional)](#configuring-toolbar-and-status-bar-rt-professional-2)
- [Configuring the appearance of the table elements (RT Professional)](#configuring-the-appearance-of-the-table-elements-rt-professional-1)
- [Configuring table column sorting (RT Professional)](#configuring-table-column-sorting-rt-professional-1)
- [Configuring the export of Runtime data (RT Professional)](#configuring-the-export-of-runtime-data-rt-professional-2)
- [Determining the effect of the online configuration (RT Professional)](#determining-the-effect-of-the-online-configuration-rt-professional-2)

#### Value table basics (RT Professional)

##### Function

The value table displays values or statistics from a control. You establish the content of the value table when you configure it.

##### Overview of the value table

You connect the value table with one of the following controls:

- Table view
- f(x) trend view
- f(t) trend view

A "display mode" is set in the value table. The display mode determines which data are shown in the value table.

##### Display modes

Three different display modes are available in the value table.

- Ruler window

  The ruler window shows the coordinate values of the trends on a ruler or values of a selected line in the table.
- Statistics area window

  The statistics area window shows the values of the lower limit and upper limit of the trends between two rulers or the selected area in the table. You can only connect the statistics area window with the f(t) trend display or the table view.
- Statistics window

  The statistics window displays the statistical evaluation of the trends. Among other things, the statistics include:

  - Minimum
  - Maximum
  - Average
  - Standard deviation
  - Integral

All windows can also display additional information on the connected trends or columns, such as time stamps.

---

**See also**

[Configuring the value table (RT Professional)](#configuring-the-value-table-rt-professional-1)
  
[Creating statistics for Runtime data (RT Professional)](#creating-statistics-for-runtime-data-rt-professional)
  
[Determining the coordinates of a point (RT Professional)](#determining-the-coordinates-of-a-point-rt-professional)

#### Configuring the value table (RT Professional)

##### Introduction

The contents of the value table are shown in columns. The available columns depend on the connected control. A block is assigned to each column. You define the alignment and appearance of the column headers using the blocks. By default, the format of the connected control is used for the display format, such as the time display.

##### Requirements

- The table view or trend view is selected in the screen
- The Inspector window is open

##### Procedure

Proceed as follows to configure a value table:

1. Add the required table view to the screen from the "Tools" task card.
2. Click "Properties &gt; Properties &gt; General &gt; Data source" in the Inspector window to connect the value table to the selected control.
3. Select the "mode" of the value table under "Properties &gt; Properties &gt; General".
4. Configure the properties of the value table columns under "Properties &gt; Properties &gt; Blocks".
5. Configure the "Properties &gt; Properties &gt; Columns":

   - Change the "Visibility", if required
   - Change the "Label", if required
   - If required, change the sequence of columns using "Up" and "Down"
6. Configure the view of the value table in the Inspector window:

   - Configure the view of the value table under "Properties &gt; Properties &gt; Appearance".
   - Configure the properties of the value table in Runtime under "Properties &gt; Properties &gt; "Window".

##### Result

The value table is configured.

---

**See also**

[Value table basics (RT Professional)](#value-table-basics-rt-professional)
  
[Configuring toolbar and status bar (RT Professional)](#configuring-toolbar-and-status-bar-rt-professional-2)
  
[Configuring the appearance of the table elements (RT Professional)](#configuring-the-appearance-of-the-table-elements-rt-professional-1)
  
[Configuring table column sorting (RT Professional)](#configuring-table-column-sorting-rt-professional-1)
  
[Configuring the export of Runtime data (RT Professional)](#configuring-the-export-of-runtime-data-rt-professional-2)
  
[Determining the effect of the online configuration (RT Professional)](#determining-the-effect-of-the-online-configuration-rt-professional-2)

#### Configuring toolbar and status bar (RT Professional)

##### Introduction

You operate the controls in Runtime using the buttons in the toolbar. The status bar displays status messages from the control. During configuration, set the content of the toolbar and status bar.

##### Requirement

- The table view is selected in the screen.
- The Inspector window is open

##### Configuring the toolbar

Proceed as follows to configure the toolbar:

1. In the Inspector window, configure the general properties of the toolbar, such as orientation and background color, under "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - General".
2. In the Inspector window, activate the buttons you need in Runtime under "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - Buttons".

   For information on the functions of the individual buttons, refer to the description of the corresponding WinCC control at "Operation in Runtime".
3. To set the order of the buttons, select the buttons in the list. You can then move the buttons to the desired position.
4. If needed, you can define a "hotkey" for the buttons on the toolbar.
5. If necessary, select the authorization needed to operate the buttons in Runtime.
6. If a button should not be operated in Runtime, unselect "Activate".

   You can reactivate a deactivated a button using a script in Runtime, for example.

##### Configuring the status bar

Proceed as follows to configure the status bar:

1. In the Inspector window, configure the general properties of the status bar, such as orientation and background color, under "Properties &gt; Properties &gt; Status bar &gt; Status bar - General".
2. In the Inspector window, activate the elements you need in Runtime under "Properties &gt; Properties &gt; Status bar &gt; Status bar - Elements".

   For further information on status bar elements, refer to the descriptions of the corresponding WinCC control at "Operation in runtime".
3. To set the order of the elements, select the element in the list. You can then move the element to the desired position.
4. To adjust the width of an element in the status bar, deactivate "Auto-size". You can then enter the width in pixels.

---

**See also**

[Configuring the value table (RT Professional)](#configuring-the-value-table-rt-professional-1)
  
[Elements of the status bar (RT Professional)](#elements-of-the-status-bar-rt-professional)

#### Configuring the appearance of the table elements (RT Professional)

##### Introduction

You can adjust the appearance of the table elements to your needs.

##### Requirement

- The table view or value table is selected in the screen.
- The Inspector window is open

##### Procedure

Proceed as follows to configure the colors of the table elements:

1. Define the following properties in the Inspector window under "Properties &gt; Properties &gt; Table &gt; Table - Header":

   - Visibility of the column headers and row headers
   - Alignment of the column headers and row headers
   - Color design of column headers
2. Define the following properties in the Inspector window under "Properties &gt; Properties &gt; Table &gt; Table - Structure":

   - Color design of table content, such as different colors for rows for better differentiation
   - Visibility of empty columns and rows
3. Define the following properties in the Inspector window under "Properties &gt; Properties &gt; Table &gt; Table - Grid":

   - Design of grid lines
   - Character spacing in the table cells

##### Result

The appearance of the table elements is configured. You can also define further properties:

- Behavior and color design when selecting a table entry
- Table entry sorting

---

**See also**

[Configuring the value table (RT Professional)](#configuring-the-value-table-rt-professional-1)
  
[Configuring table column sorting (RT Professional)](#configuring-table-column-sorting-rt-professional-1)

#### Configuring table column sorting (RT Professional)

##### Introduction

If the operator is to be able to sort individual table columns in Runtime, configure the sorting within the table.

Depending on the configuration, the operator can sort a table column as follows:

- Clicking or double-clicking on the column header
- Clicking on a sorting button

  The sorting button is used to sort the selected column in the configured order. For the sorting button to appear, you must configure a vertical scroll bar.

##### Requirement

- The table view or value table is selected in the screen.
- The Inspector window is open

##### Procedure

To configure the sorting within a table, follow these steps:

1. In the Inspector window, select "Properties &gt; Properties &gt; Table &gt; Table - Sorting &gt; Sort by column header", "Sort with double-click", or "Sort with click".
2. Select the "Sorting order" option.
3. If needed, activate "Display sorting icon" and "Display sorting index".
4. If needed, activate "Display sorting button".
5. If you use the sorting button, select "Properties &gt; Properties &gt; Window &gt; Scroll &gt; Vertical scrollbar &gt; Always" in the Inspector window.

##### Result

The sorting of the table columns is configured.

---

**See also**

[Configuring the value table (RT Professional)](#configuring-the-value-table-rt-professional-1)

#### Configuring the export of Runtime data (RT Professional)

##### Introduction

In Runtime, you can export the displayed data of a control in CSV format. Depending on the control used and the configuration, the user exports all data or only the selected data.

The filename and location of the CSV file are set by the operator on export. Alternatively, you can generate the filename automatically from the following wildcards:

- @OBJECTNAME: Object name of the control
- @CURRENTDATE: Current date
- @CURRENTTIME: Current time

##### Requirement

- The control is selected in the screen
- The Inspector window is open

##### Procedure

To configure the export of Runtime data, proceed as follows:

1. In the Inspector window, open "Properties &gt; Properties &gt; Data export".

   The data export settings are already configured.
2. If necessary, enter your own filename and a path for the export file.
3. Select the "scope" of the data export.
4. Configure the "Operation in Runtime".
5. So that the operator can start the data export, activate "Properties &gt; Properties &gt; Toolbar &gt; Toolbar - Buttons &gt; Export Data" in the Inspector window.

##### Result

In Runtime, the operator can export the data of the control via the toolbar.

---

**See also**

[Configuring the value table (RT Professional)](#configuring-the-value-table-rt-professional-1)

#### Determining the effect of the online configuration (RT Professional)

##### Introduction

In WinCC you configure the appearance and function of a control in Runtime. In addition, you can allow the operator to configure a control in Runtime. You can set whether changes to configuration in Runtime are retained, such as after a screen change, in the control under "Properties &gt; Properties &gt; Security &gt; Persistence".

- No persistence

  The changes to the configuration are not saved. The changes are discarded on the next screen change and when the project is rejected.
- Persistence

  The changes to the configuration are saved. The changes are retained even after the project is deactivated and activated. You may also select "Response at screen change" to discard changes at the screen change.
- Persistence in Runtime

  The changes to the configuration are only saved during Runtime. If you deactivate the project, the changes are discarded. You may also select "Response at screen change" to discard changes at the screen change.

  > **Note**
  >
  > If you change a configured control and load it onto the HMI device, the changes are overwritten in Runtime regardless of the settings.

##### Requirement

- A configured control
- The Inspector window is open

##### Procedure

To configure the persistence of data in Runtime, proceed as follows:

1. In the Inspector window, open "Properties &gt; Properties &gt; Security".
2. Select "Online configuration".
3. If needed, select the authorization.
4. Select the "Behavior on screen change".

##### Result

The behavior in online configuration is now set. In Runtime, depending on the settings, the user can adjust the configuration of the control.

If several operators are working on the HMI device, the individual configurations are accepted on a change of operator only following a screen change.

---

**See also**

[Configuring the value table (RT Professional)](#configuring-the-value-table-rt-professional-1)

### Using controls in Runtime (RT Professional)

This section contains information on the following topics:

- [Using the trend and table view in Runtime (RT Professional)](#using-the-trend-and-table-view-in-runtime-rt-professional)
- [Using trend view in Runtime (RT Professional)](#using-trend-view-in-runtime-rt-professional)
- [Operating table view in Runtime (RT Professional)](#operating-table-view-in-runtime-rt-professional)
- [Starting and Stopping Update (RT Professional)](#starting-and-stopping-update-rt-professional)
- [Creating statistics for Runtime data (RT Professional)](#creating-statistics-for-runtime-data-rt-professional)
- [Displaying logged values (RT Professional)](#displaying-logged-values-rt-professional)
- [Elements of the status bar (RT Professional)](#elements-of-the-status-bar-rt-professional)

#### Using the trend and table view in Runtime (RT Professional)

##### Introduction

You operate the trend and table view using the toolbar buttons.

To operate a button via a script, transfer the "ID" of the button to the script. Use the symbols from the symbol library to label the button. The symbols are available in the "Tools &gt; Graphics" task card under "WinCC graphic folder &gt; Runtime control icons &gt; Trend View".

##### Buttons of the f(x) trend view

The table below shows the buttons that are available in the f(x) trend view:

| Symbol | Name | Function | ID |
| --- | --- | --- | --- |
| ![Buttons of the f(x) trend view](images/23448984971_DV_resource.Stream@PNG-de-DE.png) | "Tooltip" | Calls up the control help. | 1 |
| ![Buttons of the f(x) trend view](images/23942155147_DV_resource.Stream@PNG-de-DE.png) | "Configuration dialog" | Opens the configuration dialog in which you can change the properties of the control | 2 |
| ![Buttons of the f(x) trend view](images/23942162827_DV_resource.Stream@PNG-de-DE.png) | "Ruler" | Displays a ruler that shows the coordinates of the intersection point with a trend in the value table.   Requirement: The value table is configured with "Ruler window" display mode. | 3 |
| ![Buttons of the f(x) trend view](images/33643902475_DV_resource.Stream@PNG-de-DE.png) | "Zoom area" | Zooms the trend view area. You define the area by dragging with the mouse.   Use the "Original view" button to return to the original view. | 4 |
| ![Buttons of the f(x) trend view](images/102270138379_DV_resource.Stream@PNG-de-DE.png) | "Zoom +/-" | Zooms in or out of the trends in the trend view.   Left-click: Zoom in  &lt;Shift + Left-click&gt;: Zoom out  Use the "Original view" button to return to the original view. | 5 |
| ![Buttons of the f(x) trend view](images/33643905803_DV_resource.Stream@PNG-de-DE.png) | "Zoom X axis + /-" | Zooms in or out on the time axis in the trend view.  Left-click: Zoom in  &lt;Shift + Left-click&gt;: Zoom out  Use the "Original view" button to return to the original view. | 6 |
| ![Buttons of the f(x) trend view](images/33643909131_DV_resource.Stream@PNG-de-DE.png) | "Zoom Y axis +/-" | Zooms in or out on the value axis in the trend view.  Left-click: Zoom in  &lt;Shift + Left-click&gt;: Zoom out  Use the "Original view" button to return to the original view. | 7 |
| ![Buttons of the f(x) trend view](images/33643912459_DV_resource.Stream@PNG-de-DE.png) | "Move trend area" | Moves the trend along the value axis and the time axis | 8 |
| ![Buttons of the f(x) trend view](images/33643992587_DV_resource.Stream@PNG-de-DE.png) | "Move axis range" | Moves the trend along the value axis | 9 |
| ![Buttons of the f(x) trend view](images/23980203659_DV_resource.Stream@PNG-de-DE.png) | "Original view" | Returns to the original view from the zoomed display | 10 |
| ![Buttons of the f(x) trend view](images/23929835147_DV_resource.Stream@PNG-de-DE.png) | "Select data connection" | Opens a dialog in which you select the data source:  - Process value archive - Tag - Recipe (only f(x) trend view) | 11 |
| ![Buttons of the f(x) trend view](images/23980633995_DV_resource.Stream@PNG-de-DE.png) | "Select trends" | Opens a dialog in which you can hide and show trends. You can also select which trend is to be placed in the foreground. | 12 |
| ![Buttons of the f(x) trend view](images/102411252619_DV_resource.Stream@PNG-de-DE.png) | "Select time range" | Opens a dialog in which you configure the time range | 13 |
| ![Buttons of the f(x) trend view](images/23980641931_DV_resource.Stream@PNG-de-DE.png) | "Previous trend" | Displays the previous trend in the foreground. | 14 |
| ![Buttons of the f(x) trend view](images/23980803211_DV_resource.Stream@PNG-de-DE.png) | "Next trend" | Displays the next trend in the foreground. | 15 |
| ![Buttons of the f(x) trend view](images/102411244939_DV_resource.Stream@PNG-de-DE.png) | "Stop" | Stops the updated display.   The data is buffered. | 16 |
| ![Buttons of the f(x) trend view](images/102411248779_DV_resource.Stream@PNG-de-DE.png) | "Start" | Continues the updated display.  The buffered values are entered. | 16 |
| ![Buttons of the f(x) trend view](images/23931759499_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the selected values.   The print job is defined in the configuration dialog on the "General" tab. | 17 |
| ![Buttons of the f(x) trend view](images/23933398667_DV_resource.Stream@PNG-de-DE.png) | "Connect backup" | Opens a dialog in which you connect selected archives from WinCC Runtime | 18 |
| ![Buttons of the f(x) trend view](images/23933406859_DV_resource.Stream@PNG-de-DE.png) | "Disconnect backup" | Opens a dialog in which you disconnect selected archives from WinCC Runtime | 19 |
| ![Buttons of the f(x) trend view](images/44731625483_DV_resource.Stream@PNG-de-DE.png) | "Export data" | Exports all or selected data to a *.CSV file.   Depending on the configuration and the privileges, the following options can be available:  - Display export settings and start export - Select file name and directory | 20 |
| ![Buttons of the f(x) trend view](images/44731633419_DV_resource.Stream@PNG-de-DE.png) | "User-defined 1" | Displays the first button created by the user.   The function of the button is user-defined | 1001 |

##### Buttons of f(t) trend view

The table below shows the buttons that are available in the f(t) trend view:

| Symbol | Name | Function | ID |
| --- | --- | --- | --- |
| ![Buttons of f(t) trend view](images/23448984971_DV_resource.Stream@PNG-de-DE.png) | "Tooltip" | Calls up the control help. | 1 |
| ![Buttons of f(t) trend view](images/23942155147_DV_resource.Stream@PNG-de-DE.png) | "Configuration dialog" | Opens the configuration dialog in which you can change the properties of the control | 2 |
| ![Buttons of f(t) trend view](images/102411264395_DV_resource.Stream@PNG-de-DE.png) | "First data record" | Displays the course of a tag within a specified period starting with the first archived value.   Requirement: Values come from a process value archive. | 3 |
| ![Buttons of f(t) trend view](images/102411268235_DV_resource.Stream@PNG-de-DE.png) | "Previous data record" | Displays the course of a tag within the previous time interval, based on the currently displayed time interval.   Requirement: Values come from a process value archive. | 4 |
| ![Buttons of f(t) trend view](images/102411284875_DV_resource.Stream@PNG-de-DE.png) | "Next data record" | Displays the course of a tag within the next time interval, based on the currently displayed time interval.  Requirement: Values come from a process value archive. | 5 |
| ![Buttons of f(t) trend view](images/102411288715_DV_resource.Stream@PNG-de-DE.png) | "Last data record" | Displays the course of a tag within a specified period ending with the last archived value.  Requirement: Values come from a process value archive. | 6 |
| ![Buttons of f(t) trend view](images/23942162827_DV_resource.Stream@PNG-de-DE.png) | "Ruler" | Displays a ruler that shows the coordinates of the intersection point with a trend in the value table.  Requirement: The value table is configured with "Ruler window" display mode. | 7 |
| ![Buttons of f(t) trend view](images/33643902475_DV_resource.Stream@PNG-de-DE.png) | "Zoom area" | Zooms the trend view area. You define the area by dragging with the mouse.  Use the "Original view" button to return to the original view. | 8 |
| ![Buttons of f(t) trend view](images/102270138379_DV_resource.Stream@PNG-de-DE.png) | "Zoom +/-" | Zooms in or out of the trends in the trend view.  Left-click: Zoom in  &lt;Shift + Left-click&gt;: Zoom out  Use the "Original view" button to return to the original view. | 9 |
| ![Buttons of f(t) trend view](images/33643905803_DV_resource.Stream@PNG-de-DE.png) | "Zoom time axis +/-" | Zooms in or out on the time axis in the trend view.  Left-click: Zoom in  &lt;Shift + Left-click&gt;: Zoom out  Use the "Original view" button to return to the original view. | 10 |
| ![Buttons of f(t) trend view](images/33643909131_DV_resource.Stream@PNG-de-DE.png) | "Zoom value axis +/-" | Zooms in or out on the value axis in the trend view.  Left-click: Zoom in  &lt;Shift + Left-click&gt;: Zoom out  Use the "Original view" button to return to the original view. | 11 |
| ![Buttons of f(t) trend view](images/33643912459_DV_resource.Stream@PNG-de-DE.png) | "Move trend area" | Moves the trend along the value axis and the time axis | 12 |
| ![Buttons of f(t) trend view](images/33643992587_DV_resource.Stream@PNG-de-DE.png) | "Move axis range" | Moves the trend along the value axis | 13 |
| ![Buttons of f(t) trend view](images/23980203659_DV_resource.Stream@PNG-de-DE.png) | "Original view" | Returns to the original view from the zoomed display | 14 |
| ![Buttons of f(t) trend view](images/23929835147_DV_resource.Stream@PNG-de-DE.png) | "Select data connection" | Opens a dialog in which you select the data source:  - Process value archive - Tag - Recipe (only f(x) trend view) | 15 |
| ![Buttons of f(t) trend view](images/23980633995_DV_resource.Stream@PNG-de-DE.png) | "Select trends" | Opens a dialog in which you can hide and show trends. You can also select which trend is to be placed in the foreground. | 16 |
| ![Buttons of f(t) trend view](images/102411252619_DV_resource.Stream@PNG-de-DE.png) | "Select time range" | Opens a dialog in which you configure the time range | 17 |
| ![Buttons of f(t) trend view](images/23980641931_DV_resource.Stream@PNG-de-DE.png) | "Previous trend" | Displays the previous trend in the foreground. | 18 |
| ![Buttons of f(t) trend view](images/23980803211_DV_resource.Stream@PNG-de-DE.png) | "Next trend" | Displays the next trend in the foreground. | 19 |
| ![Buttons of f(t) trend view](images/102411244939_DV_resource.Stream@PNG-de-DE.png) | "Stop" | Stops the updated display.  The data is buffered. | 20 |
| ![Buttons of f(t) trend view](images/102411248779_DV_resource.Stream@PNG-de-DE.png) | "Start" | Continues the updated display.  The buffered values are entered. | 20 |
| ![Buttons of f(t) trend view](images/23931759499_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the selected values.  The print job is defined in the configuration dialog on the "General" tab. | 21 |
| ![Buttons of f(t) trend view](images/102411256459_DV_resource.Stream@PNG-de-DE.png) | "Statistics area" | Defines the time frame used to calculate the statistics. | 22 |
| ![Buttons of f(t) trend view](images/44732131595_DV_resource.Stream@PNG-de-DE.png) | "Statistical analysis" | Displays the statistical values from a fixed "statistics area" of the trend or table view in the statistics window of the value table.   Only available with a configured value table | 23 |
| ![Buttons of f(t) trend view](images/23933398667_DV_resource.Stream@PNG-de-DE.png) | "Connect backup" | Opens a dialog in which you connect selected archives from WinCC Runtime | 24 |
| ![Buttons of f(t) trend view](images/23933406859_DV_resource.Stream@PNG-de-DE.png) | "Disconnect backup" | Opens a dialog in which you disconnect selected archives from WinCC Runtime | 25 |
| ![Buttons of f(t) trend view](images/44731625483_DV_resource.Stream@PNG-de-DE.png) | "Export data" | Exports all or selected data to a *.CSV file.  Depending on the configuration and the privileges, the following options can be available:  - Display export settings and start export - Select file name and directory | 26 |
| ![Buttons of f(t) trend view](images/23982456203_DV_resource.Stream@PNG-de-DE.png) | "Relative axis" | Switches from displaying the absolute values to the percentage display of value axis. The high and low limits for the trend correspond with a range of 0 to 100%. | 27 |
| ![Buttons of f(t) trend view](images/44731633419_DV_resource.Stream@PNG-de-DE.png) | "User-defined 1" | Displays the first button created by the user.  The function of the button is user-defined | 1001 |

##### Table view buttons

The following table shows the buttons that are available in the table view:

| Symbol | Name | Function | ID |
| --- | --- | --- | --- |
| ![Table view buttons](images/23448984971_DV_resource.Stream@PNG-de-DE.png) | "Tooltip" | Calls up the control help. | 1 |
| ![Table view buttons](images/23942155147_DV_resource.Stream@PNG-de-DE.png) | "Configuration dialog" | Opens the configuration dialog in which you can change the properties of the control | 2 |
| ![Table view buttons](images/102411264395_DV_resource.Stream@PNG-de-DE.png) | "First data record" | Displays the course of a tag within a specified period starting with the first archived value.   Requirement: Values come from a process value archive. | 3 |
| ![Table view buttons](images/102411268235_DV_resource.Stream@PNG-de-DE.png) | "Previous data record" | Displays the course of a tag within the previous time interval, based on the currently displayed time interval.   Requirement: Values come from a process value archive. | 4 |
| ![Table view buttons](images/102411284875_DV_resource.Stream@PNG-de-DE.png) | "Next data record" | Displays the course of a tag within the next time interval, based on the currently displayed time interval.  Requirement: Values come from a process value archive. | 5 |
| ![Table view buttons](images/102411288715_DV_resource.Stream@PNG-de-DE.png) | "Last data record" | Displays the course of a tag within a specified period ending with the last archived value.  Requirement: Values come from a process value archive. | 6 |
| ![Table view buttons](images/23926371723_DV_resource.Stream@PNG-de-DE.png) | "Edit" | Activates editing of table entries. To edit a value, double-click on the desired table cell.   Requirement: Updated display is stopped. | 7 |
| ![Table view buttons](images/23926379915_DV_resource.Stream@PNG-de-DE.png) | "Copy lines" | Copies the content of the selected lines to the clipboard.   Requirement: Updated display is stopped. | 8 |
| ![Table view buttons](images/23929835147_DV_resource.Stream@PNG-de-DE.png) | "Select data connection" | Opens a dialog in which you select the data source:  - Process value archive - Tag - Recipe (only f(x) trend view) | 9 |
| ![Table view buttons](images/23926797707_DV_resource.Stream@PNG-de-DE.png) | "Select columns" | Opens a dialog in which you can show or hide columns and change the column sequence. | 10 |
| ![Table view buttons](images/102411252619_DV_resource.Stream@PNG-de-DE.png) | "Select time range" | Opens a dialog in which you configure the time range | 11 |
| ![Table view buttons](images/23926805899_DV_resource.Stream@PNG-de-DE.png) | "Previous column" | Moves a value column ahead of the previous value column.   The function refers to the value columns that are assigned to a time axis. | 12 |
| ![Table view buttons](images/23927518091_DV_resource.Stream@PNG-de-DE.png) | "Next column" | Moves a value column behind the next value column.   The function refers to the value columns that are assigned to a time axis. | 13 |
| ![Table view buttons](images/102411244939_DV_resource.Stream@PNG-de-DE.png) | "Stop" | Stops the updated display.   The data is buffered. | 14 |
| ![Table view buttons](images/102411248779_DV_resource.Stream@PNG-de-DE.png) | "Start" | Continues the updated display.  The buffered values are entered. | 14 |
| ![Table view buttons](images/23931759499_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the selected values.   The print job is defined in the configuration dialog on the "General" tab. | 15 |
| ![Table view buttons](images/102411256459_DV_resource.Stream@PNG-de-DE.png) | "Statistics area" | Defines the time frame used to calculate the statistics. | 16 |
| ![Table view buttons](images/44732131595_DV_resource.Stream@PNG-de-DE.png) | "Statistical analysis" | Displays the statistical values from a fixed "statistics area" of the trend or table view in the statistics window of the value table.   Only available with a configured value table | 17 |
| ![Table view buttons](images/23933398667_DV_resource.Stream@PNG-de-DE.png) | "Connect backup" | Opens a dialog in which you connect selected archives from WinCC Runtime | 18 |
| ![Table view buttons](images/23933406859_DV_resource.Stream@PNG-de-DE.png) | "Disconnect backup" | Opens a dialog in which you disconnect selected archives from WinCC Runtime | 19 |
| ![Table view buttons](images/44731625483_DV_resource.Stream@PNG-de-DE.png) | "Export data" | Exports all or selected data to a *.CSV file.   Depending on the configuration and the privileges, the following options can be available:  - Display export settings and start export - Select file name and directory | 20 |
| ![Table view buttons](images/44731633419_DV_resource.Stream@PNG-de-DE.png) | "User-defined 1" | Displays the first button created by the user.   The function of the button is user-defined | 1001 |

##### Buttons of the value table

The table below shows the buttons that are available in the value table:

| Symbol | Name | Function | ID |
| --- | --- | --- | --- |
| ![Buttons of the value table](images/23448984971_DV_resource.Stream@PNG-de-DE.png) | "Tooltip" | Calls up the control help. | 1 |
| ![Buttons of the value table](images/23942155147_DV_resource.Stream@PNG-de-DE.png) | "Configuration dialog" | Opens the configuration dialog in which you can change the properties of the control | 2 |
| ![Buttons of the value table](images/23942162827_DV_resource.Stream@PNG-de-DE.png) | "Ruler" | Displays a ruler that shows the coordinates of the intersection point with a trend in the value table.  Requirement: The value table is configured with "Ruler window" display mode. | 3 |
| ![Buttons of the value table](images/102411256459_DV_resource.Stream@PNG-de-DE.png) | "Statistics area" | Defines the time frame used to calculate the statistics. | 4 |
| ![Buttons of the value table](images/44732131595_DV_resource.Stream@PNG-de-DE.png) | "Statistical analysis" | Displays the statistical values from a fixed "statistics area" of the trend or table view in the statistics window of the value table.  Only available with a configured value table | 5 |
| ![Buttons of the value table](images/23931759499_DV_resource.Stream@PNG-de-DE.png) | "Print" | Prints the selected values.  The print job is defined in the configuration dialog on the "General" tab. | 6 |
| ![Buttons of the value table](images/44731625483_DV_resource.Stream@PNG-de-DE.png) | "Export data" | Exports all or selected data to a *.CSV file.  Depending on the configuration and the privileges, the following options can be available:  - Display export settings and start export - Select file name and directory | 7 |
| ![Buttons of the value table](images/44731633419_DV_resource.Stream@PNG-de-DE.png) | "User-defined 1" | Displays the first button created by the user.  The function of the button is user-defined | 1001 |

#### Using trend view in Runtime (RT Professional)

This section contains information on the following topics:

- [Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)
- [Using the zoom functions in trend windows (RT Professional)](#using-the-zoom-functions-in-trend-windows-rt-professional)
- [Trend to Front (RT Professional)](#trend-to-front-rt-professional)
- [Determining the coordinates of a point (RT Professional)](#determining-the-coordinates-of-a-point-rt-professional)

##### Online configuration of the f(t) trend view (RT Professional)

###### Introduction

In Runtime you configure online and thus change the appearance of the trend view. The table view configuration specifies whether online configurations are retained or discarded on a screen change or after Runtime is ended.

###### Overview

The following buttons make online configuration possible in the trend view:

- "Configuration dialog" button
- "Select data connection" button
- "Select trends" button
- "Select Time Range" button

###### Opening the configuration dialog

To open the configuration dialog, proceed as follows:

1. Click ![Opening the configuration dialog](images/44727320715_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

The configuration dialog is opened. You can change the table appearance, for example, in the configuration dialog.

> **Note**
>
> **Printing a fixed time range**
>
> If you want to print a defined time range, make sure that the following options in the configuration dialog are deactivated:
>
> - "Time axes &gt; Update"
> - "General &gt; Open screen &gt; Launch update".

###### Changing the data connection

The following table shows the configuration options for data connection:

| Field | Description |
| --- | --- |
| Trend | Choose one of the configured trends. |
| Data Source | Define whether the selected trend is supplied with a logging tag or online tag. |
| Tag name | Select the tag name for the data connection. |

Proceed as follows to change the data connection:

1. Click ![Changing the data connection](images/23929835147_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

   The "Archive/tag selection" dialog is opened.
2. Choose the "Value column" for which you want to change the data connection.
3. Select the "Data supply" and the "Tag name".

###### Changing a time range

The following table shows the configuration options for the time range:

| Field | Description |
| --- | --- |
| Time axis | Select the configured time axis for which you want to define a time range. |
| Time range | Set the time range:  - If you want to define a fixed time interval, select setting "Start to end time". Enter the date and time for each. - If you want to define a time period, select the setting "Time range". Define the date and time for the start time. The length of the time interval to be displayed is determined by multiplying the "Factor" by the "Time unit". - If you want to display a certain number of values, select the setting "Number of measurement points". Define the date and time for the start time. Enter the desired number of measurement points in the input field. |

To configure the time range, follow these steps:

1. Click ![Changing a time range](images/102411252619_DV_resource.Stream@PNG-de-DE.png) in the toolbar of the trend view.

   The "Time - Selection" dialog opens.
2. Choose the "Time axis" for which you want to adapt the time range.

   If the trends in a trend view are to be displayed with a common time axis, the specified time range applies to all trends.
3. Configure the time range.

   The entry format of the date and time depends on the Runtime language used.

---

**See also**

[Trend to Front (RT Professional)](#trend-to-front-rt-professional)
  
[Using the zoom functions in trend windows (RT Professional)](#using-the-zoom-functions-in-trend-windows-rt-professional)
  
[Starting and Stopping Update (RT Professional)](#starting-and-stopping-update-rt-professional)
  
[Creating statistics for Runtime data (RT Professional)](#creating-statistics-for-runtime-data-rt-professional)
  
[Displaying logged values (RT Professional)](#displaying-logged-values-rt-professional)
  
[Elements of the status bar (RT Professional)](#elements-of-the-status-bar-rt-professional)
  
[Configure trend view (RT Professional)](#configure-trend-view-rt-professional)

##### Using the zoom functions in trend windows (RT Professional)

###### Introduction

Key functions can be used for zooming in on, zooming out of and returning to the original view for trends, axes and various zoom areas of the trend window.

###### Overview

The following zoom functions are available in the trend window:

- "Zoom area"
- "Original view"
- "Zoom +/-"
- "Zoom time axis +/-"
- "Zoom value axis +/-"
- "Move trend area"

###### Requirement

- The trend view is open
- Buttons with zoom functions are configured
- Runtime is activated

###### Zooming in on a trend view area

Proceed as follows to zoom in on an area of the trend view:

1. Click on ![Zooming in on a trend view area](images/33643902475_DV_resource.Stream@PNG-de-DE.png).

   The updated display is stopped.
2. Drag with the mouse to draw a box around the area to be zoomed.

   If there are at least two measured values within this area, the area of the trend is zoomed.
3. To return to the original view of the trend, click ![Zooming in on a trend view area](images/23980203659_DV_resource.Stream@PNG-de-DE.png).
4. Click on ![Zooming in on a trend view area](images/102411248779_DV_resource.Stream@PNG-de-DE.png) to start the update again.

The default values are used for the axis.

###### Zooming in or out on trends

If you zoom in or out on a trend, the 50% value of the trend is always in the middle of the value axes.

Proceed as follows to zoom in or out on a trend:

1. Click on ![Zooming in or out on trends](images/102270138379_DV_resource.Stream@PNG-de-DE.png).

   The updated display is stopped.
2. To zoom in on a trend, click on the trend with the left mouse button.
3. To zoom out on a trend, hold down the &lt;Shift&gt; key and click on the trend with the left mouse button.
4. To return to the original view of the trend, click ![Zooming in or out on trends](images/23980203659_DV_resource.Stream@PNG-de-DE.png).
5. Click on ![Zooming in or out on trends](images/102411248779_DV_resource.Stream@PNG-de-DE.png) to start the update again.

The default values are used for the axis.

> **Note**
>
> If you change the value area of a value axis on the "Value Axis" tab in the configuration dialog while zooming, the visible zoom area is set to the new value area.

###### Zooming in on the time axis or value axis

While zooming with time or value axes, the 50% value of the trend is always in the middle of the axes.

Proceed as follows to zoom the time axis or value axis:

1. Click ![Zooming in on the time axis or value axis](images/33643905803_DV_resource.Stream@PNG-de-DE.png) to zoom the time axis.

   The updated display is stopped.
2. Click ![Zooming in on the time axis or value axis](images/33643909131_DV_resource.Stream@PNG-de-DE.png) to zoom the value axis.

   The updated display is stopped.
3. To zoom in on an axis, click on the trend view with the left mouse button.
4. To zoom out on an axis, hold down the &lt;Shift&gt; key and click on the trend view with the left mouse button.
5. To return to the original view of the trend, click ![Zooming in on the time axis or value axis](images/23980203659_DV_resource.Stream@PNG-de-DE.png).
6. Click on ![Zooming in on the time axis or value axis](images/102411248779_DV_resource.Stream@PNG-de-DE.png) to start the update again.

The default values are used for the axis.

###### Moving a trend area

Proceed as follows to move the trend area:

1. Click on ![Moving a trend area](images/33643912459_DV_resource.Stream@PNG-de-DE.png).

   The updated display is stopped.
2. While holding the left mouse button pressed, move the cursor in the desired direction in the trend view.

   The displayed area in the trend window is adapted on the time axis and on the value axis.
3. Click on ![Moving a trend area](images/33643912459_DV_resource.Stream@PNG-de-DE.png) again to return to the original view of the trend window.

---

**See also**

[Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)

##### Trend to Front (RT Professional)

###### Introduction

If more than one trend are to be displayed in a trend window, you can use key functions to define which trends will be displayed in the foreground.

###### Requirement

- The following buttons are configured:

  - "Select trends"
  - "Previous trend"
  - "Next trend"
- The project is activated

###### Procedure

Proceed as follows to display a trend in the foreground:

1. Click on ![Procedure](images/23980633995_DV_resource.Stream@PNG-de-DE.png).

   The dialog for displaying or hiding trends is opened. In this dialog you can also define which trend is in the foreground.

   > **Note**
   >
   > The first trend of a trend window cannot be hidden.
2. In order to display the next trend in the foreground, click on ![Procedure](images/23980803211_DV_resource.Stream@PNG-de-DE.png).
3. In order to display the previous trend in the foreground, click on ![Procedure](images/23980641931_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

[Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)

##### Determining the coordinates of a point (RT Professional)

###### Introduction

The "Ruler" button is used to determine the coordinates of a point on the trend by means of a ruler. You can zoom in on an area of the trend to make coordinate finding easier. If you display the ruler in the trend view, you can move the ruler at any time.

If you click on the trend with the mouse, several trend parameters are shown in the tooltip for the trend view.

###### Requirement

- A trend view is configured
- The value table is configured and connected with the trend view
- The "Ruler window" display mode is activated in the value table
- Runtime is activated

###### Procedure

Proceed as follows to determine the coordinates of a point:

1. Click on ![Procedure](images/23942162827_DV_resource.Stream@PNG-de-DE.png) in the trend view.

   The ruler is shown.
2. Move the ruler to the desired position with the mouse.
3. If you want to zoom in on an area, click on ![Procedure](images/33643902475_DV_resource.Stream@PNG-de-DE.png).

   - Move the ruler to the desired position with the mouse.
   - Click ![Procedure](images/23980203659_DV_resource.Stream@PNG-de-DE.png) to return to the original view.

###### Result

In the ruler window of the value table, besides the X value/time stamp and the Y value, the data that you have configured in the value table is shown in the columns.

In the value table, the indices "i" and "u" can be displayed in addition to the values:

- "i.": The displayed value is an interpolated value.
- "u.": The displayed value has an uncertain status:

  - The initial value after Runtime activation is unknown
  - A substitute value is used

    > **Note**
    >
    > You can also identity the "uncertain" status of a value in the displayed trend curve. You must activate the "Value with uncertain status" option on the "Trends" tab under "Limit values".

The following image shows the coordinates of a point in the ruler window of the value table:

![Result](images/23979810315_DV_resource.Stream@PNG-en-US.png)

###### Alternative procedure

Alternatively, you can also connect the value table to the table display. In the "ruler window" display mode, the values of the selected line are displayed in the value table.

---

**See also**

[Value table basics (RT Professional)](#value-table-basics-rt-professional)

#### Operating table view in Runtime (RT Professional)

This section contains information on the following topics:

- [Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)
- [Editing the table field in Runtime (RT Professional)](#editing-the-table-field-in-runtime-rt-professional)
- [Moving columns in the table (RT Professional)](#moving-columns-in-the-table-rt-professional)

##### Online configuration of the table view (RT Professional)

###### Introduction

In Runtime you configure online and thus change the appearance of the table view. The table view configuration specifies whether online configurations are retained or discarded on a screen change or after Runtime is ended.

###### Overview

The following buttons make online configuration possible in table view:

- "Configuration dialog" button
- "Select data connection" button
- "Select columns" button
- "Select Time Range" button

###### Opening the configuration dialog

To open the configuration dialog, proceed as follows:

Click ![Opening the configuration dialog](images/44727320715_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

The configuration dialog is opened. You can change the table appearance, for example, in the configuration dialog.

###### Changing the data connection

The following table shows the configuration options for data connection:

| Field | Description |
| --- | --- |
| Value column | Choose the configured value column for which you want to change the data connection. |
| Data Source | Define whether the selected value column is supplied with a logging tag or online tag. |
| Tag name | Select the tag name for the data connection. |

Proceed as follows to change the data connection:

1. Click ![Changing the data connection](images/23929835147_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

   The "Archive/tag selection" dialog is opened.
2. Choose the "Value column" for which you want to change the data connection.
3. Select the "Data supply" and the "Tag name".

###### Showing or hiding columns

To show or hide columns, follow these steps:

1. Click ![Showing or hiding columns](images/23926797707_DV_resource.Stream@PNG-de-DE.png) in the toolbar.

   The dialog for showing or hiding columns is opened.
2. If required, change the sequence of the value columns that are assigned to a time column.

The value columns can only be moved in reference to the anchored time column.

> **Note**
>
> The first column of a table view cannot be hidden.

###### Changing a time range

The following table shows the configuration options for the time range:

| Field | Description |
| --- | --- |
| Time column | Select the configured time column for which you want to define a time range. |
| time range | Set the time range:  - If you want to define a fixed time interval, select setting "Start to end time". Enter the date and time for each. - If you want to define a time period, select the setting "Time range". Define the date and time for the start time. The length of the time interval to be displayed is determined by multiplying the "Factor" by the "Time unit". - If you want to display a certain number of values, select the setting "Number of measurement points". Define the date and time for the start time. Enter the desired number of measurement points in the input field. |

To configure the time range, follow these steps:

1. Click ![Changing a time range](images/102411252619_DV_resource.Stream@PNG-de-DE.png) in the toolbar of the table view.

   The "Time - Selection" dialog opens.
2. Choose the "Time column" for which you want to adapt the time range.

   If the columns of a table view are to be displayed with a common time axis, the specified time range applies to all columns.
3. Configure the time range.

   The entry format of the date and time depends on the Runtime language used.

---

**See also**

[Editing the table field in Runtime (RT Professional)](#editing-the-table-field-in-runtime-rt-professional)
  
[Moving columns in the table (RT Professional)](#moving-columns-in-the-table-rt-professional)
  
[Starting and Stopping Update (RT Professional)](#starting-and-stopping-update-rt-professional)
  
[Creating statistics for Runtime data (RT Professional)](#creating-statistics-for-runtime-data-rt-professional)
  
[Displaying logged values (RT Professional)](#displaying-logged-values-rt-professional)
  
[Elements of the status bar (RT Professional)](#elements-of-the-status-bar-rt-professional)
  
[Configuring the Table View (RT Professional)](#configuring-the-table-view-rt-professional)

##### Editing the table field in Runtime (RT Professional)

###### Introduction

You change the values displayed in the table view manually using the "Edit" button.

###### Requirement

- The table view is configured
- The "Edit" button is configured
- Runtime is activated

###### Procedure

Proceed as follows to edit a table field in Runtime:

1. Click ![Procedure](images/102411244939_DV_resource.Stream@PNG-de-DE.png) in the table view.

   The updated display is stopped, the process data continues being archived.
2. Click on ![Procedure](images/23926371723_DV_resource.Stream@PNG-de-DE.png).
3. Double click on the desired table field of a value column.
4. Enter the new value.

   The changed value is archived.
5. In order to continue with the display of Runtime data in the table view, click on ![Procedure](images/102411248779_DV_resource.Stream@PNG-de-DE.png).

---

**See also**

[Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)

##### Moving columns in the table (RT Professional)

###### Introduction

The time column is always shown in the first column in the table. The value columns that are assigned to this time column are displayed next. If there are more than one time columns configured, the second time column follows with the assigned value columns.

You can change the sequence of the value columns that are assigned with a time column in Runtime. The value columns can only be moved in reference to the anchored time column. The sequence of the time columns with the assigned value columns are defined on the "Time axes" tab.

###### Requirement

The following buttons are configured:

- "Select columns"
- "Previous column"
- "Next column".

###### Procedure

To change the sequence of the columns, follow these steps:

1. Click on ![Procedure](images/23926797707_DV_resource.Stream@PNG-de-DE.png).

   The dialog for changing the sequence of the columns is opened.
2. To hide a column, deactivate the option before the column name.
3. To move a value column, select the value value column:

   The function refers to the value columns that are assigned to a time column.

   - Click ![Procedure](images/23927518091_DV_resource.Stream@PNG-de-DE.png) to move the value column behind the next value column.
   - Click ![Procedure](images/23926805899_DV_resource.Stream@PNG-de-DE.png) to move the value column in front of the previous value column.

---

**See also**

[Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)

#### Starting and Stopping Update (RT Professional)

##### Introduction

You can continue the update of the data contained in the control with the "Start/Stop" button.

Some buttons stop the update automatically, e.g. "Define statistics area"

The appearance of the button indicates whether the update is stopped or not:

- ![Introduction](images/102411244939_DV_resource.Stream@PNG-de-DE.png): Update has been stopped. To continue the update, click on the button.
- ![Introduction](images/102411248779_DV_resource.Stream@PNG-de-DE.png): The update has been started. To stop the update, click on the button

---

**See also**

[Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)
  
[Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)

#### Creating statistics for Runtime data (RT Professional)

##### Introduction

You can generate an analysis of the process data for the Runtime data in the trend view or table view. You can display the evaluated data in the value table.

##### Requirement

- A trend view or table view is configured
- A value table is configured and connected with the trend view or table view
- Runtime is activated

##### Displaying data in a statistics area window

Requirement: The "Statistics area window" display mode is activated in the value table.

To display data in the statistics area window of the value table, proceed as follows:

1. In the trend view or table view, click on ![Displaying data in a statistics area window](images/102411244939_DV_resource.Stream@PNG-de-DE.png).

   The updated display is stopped, the process data continues being archived.
2. If you wish to evaluate data outside the displayed time range:

   - Click ![Displaying data in a statistics area window](images/102411252619_DV_resource.Stream@PNG-de-DE.png)

     The "Time - Selection" dialog opens.
   - Enter the required time range.

     The data for the defined time range is displayed.
3. If you are using a trend view:

   - Click ![Displaying data in a statistics area window](images/102411256459_DV_resource.Stream@PNG-de-DE.png)

     In the trend view, two vertical lines are displayed on the right and left edges.
   - To define the statistics area, move the two lines to the desired position.
4. If you are using a table view:

   - Use the mouse to select the lines for the desired time range in the table.

     For different columns with different time frames you can select different time ranges for the calculation of statistics.
   - Click ![Displaying data in a statistics area window](images/102411256459_DV_resource.Stream@PNG-de-DE.png) in the toolbar

The evaluated data is displayed in the columns that you have configured in the statistics area window. The following figure shows the display in the statistics area window, using the trend view as an example:

![Displaying data in a statistics area window](images/102411260427_DV_resource.Stream@PNG-en-US.png)

In order to continue with the display of Runtime data, click ![Displaying data in a statistics area window](images/102411248779_DV_resource.Stream@PNG-de-DE.png).

> **Note**
>
> For additional statistical analysis of process data and archiving of results you can write the scripts yourself.

---

**See also**

[Value table basics (RT Professional)](#value-table-basics-rt-professional)
  
[Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)
  
[Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)

#### Displaying logged values (RT Professional)

##### Introduction

Scroll through the displayed data of an archive using the buttons in the toolbar of a trend view or table view. If key combinations are configured, you can also use these for scrolling.

The buttons for browsing in archive are available only if data is supplied through archive tags.

The archived values of a tag are displayed within a time range in the trend or table view.

##### Requirement

- Time range is configured

##### Buttons for Archived Values

To scroll in archived values, proceed as follows:

1. To display the first data record of the time range, click on

   ![Buttons for Archived Values](images/102411264395_DV_resource.Stream@PNG-de-DE.png)

   .
2. To display the previous data record of the time range, click on

   ![Buttons for Archived Values](images/102411268235_DV_resource.Stream@PNG-de-DE.png)

   .
3. To display the next data record of the time range, click on

   ![Buttons for Archived Values](images/102411284875_DV_resource.Stream@PNG-de-DE.png)

   .
4. To display the last data record of the time range, click on

   ![Buttons for Archived Values](images/102411288715_DV_resource.Stream@PNG-de-DE.png)

   .

---

**See also**

[Time range basics (RT Professional)](#time-range-basics-rt-professional)
  
[Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)
  
[Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)
  
[Alarm view (RT Professional)](Creating%20screens%20%28Basic%20Panels%2C%20Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#alarm-view-rt-professional)

#### Elements of the status bar (RT Professional)

##### Elements of the status bar

The status bar of the trend view or table view can contain the following elements:

| Icon | Name | Description |
| --- | --- | --- |
| ![Elements of the status bar](images/102411292555_DV_resource.Stream@PNG-de-DE.png) | Connection status<sup>1</sup> | No faulty data connections |
| ![Elements of the status bar](images/102411295883_DV_resource.Stream@PNG-de-DE.PNG) | Faulty data connections exist |  |
| ![Elements of the status bar](images/102411299211_DV_resource.Stream@PNG-de-DE.PNG) | All data connections are faulty |  |
| "Line 1"<sup>2</sup> | Selected line | Shows the number of the selected line. |
| "Column 2"<sup>2</sup> | Selected column | Shows the number of the selected column. |
| "23.02.2010" | Date | Shows the system date. |
| "23:59:59" | Time | Shows the system time. |
| ![Elements of the status bar](images/102411302539_DV_resource.Stream@PNG-de-DE.png) | Time base | Shows the time base used in the display of times. |
| <sup>1</sup>: If you double-click on the "Connection status" icon, the "Status of the data connections" window opens. The following properties of each data connection are listed in the window:  - Name - Status - Tag name |  |  |
| <sup>2</sup>: Only in the table view |  |  |

---

**See also**

[Online configuration of the f(t) trend view (RT Professional)](#online-configuration-of-the-ft-trend-view-rt-professional)
  
[Online configuration of the table view (RT Professional)](#online-configuration-of-the-table-view-rt-professional)
  
[Configuring toolbar and status bar (RT Professional)](#configuring-toolbar-and-status-bar-rt-professional-2)
