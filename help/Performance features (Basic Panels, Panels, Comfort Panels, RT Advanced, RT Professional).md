---
title: "Performance features (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: SystemLimitsWCCPenUS
topics: 16
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Performance features (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [General technical specifications (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#general-technical-specifications-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Performance features of the devices (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#performance-features-of-the-devices-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

## General technical specifications (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Permitted characters (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#permitted-characters-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Recommended printers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#recommended-printers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Printing via print server (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#printing-via-print-server-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Memory requirement of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#memory-requirement-of-recipes-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Memory requirements of recipes for Basic Panels (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#memory-requirements-of-recipes-for-basic-panels-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Permitted characters (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The following table shows the restrictions that must be observed when allocating names and passwords.

#### Permitted characters

| Names / Passwords | Restriction |
| --- | --- |
| Computer names | The name must start with a letter. |
| Names of objects | Do not use the characters ? " / \ * &lt; &gt; % |
| Names and passwords in user view | Do not use the characters ? " / \ § &amp; $ % |
| Recipe data | Do not use the characters , ; |
| Names of alarm logs | In the storage location file - RDB, file - CSV (ASCII) and file -TXT (Unicode)   do not use the characters \ / * ? : " &lt; &gt;| |
| For the storage location database, use only the characters a-z A-Z 0-9 _ @ # $  The characters _ @ # $ cannot be used as the first character of a name. |  |
| Name of HMI tags | HMI tag names may not start with the character @.  For Runtime Professional, do not use the characters : ? " ' \ * %  Do not use spaces for Runtime Professional. |
| Names of screens | Do not use the characters ? " / \ * &lt; &gt;  Avoid the characters . : in screens for Runtime Professional |
| Tag names in faceplates | Do not use the characters . @ |
| Property names of the faceplates | Do not use any UNICODE characters (for example, Chinese characters) in the names.  The name must start with a letter.  The name may not contain more than 255 characters. |
| Names of AuditTrails | Do not use any special characters. |
| Names of customized user data types as library objects (RT Professional) | Do not use the characters : ? " \\ \ * $ % " '  The name may not contain more than 128 characters. |
| Names of C scripts and VB scripts as library objects | The name must start with an ASCII letter, followed by an alphanumeric ASCII character or underscore. The name may not contain more than 128 characters. |
| Names of connections | Do not use spaces or special characters. |
| Name of VB functions | Do not use spaces, special characters or VB keywords. |
| Name of Windows user groups and Windows users when using SIMATIC Logon | Do not use the characters / \ |
| Communication / OPC: names used | Do not use either spaces or the characters . : ? " ' \ * % |

> **Note**
>
> **Device dependency - quotes in project name**
>
> WinCC Professional projects whose names are in quotes have not been compiled.
>
> When you create an HMI device for WinCC RT Professional, do not use quotation marks within the project name.

### Recommended printers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Recommended printers

The current list of printers recommended for use with the HMI devices is available on the Internet at:

[Link to the current printer list](http://support.automation.siemens.com/WW/llisapi.dll?aktprim=0&lang=en&referer=%2fWW%2f&func=cslib.csinfo&siteid=csius&caller=view&extranet=standard&viewreg=WW&nodeid0=10805558&objaction=csopen)

> **Note**
>
> All HMI devices except for a PC and Panel PC support only one printer at their USB port, even if several ports are available.

> **Note**
>
> **Driver versions**
>
> Two driver versions cannot be installed on the same device at the same time. If you have already installed a driver and want to install a new one, first uninstall the existing driver. This behavior affects all printer drivers (PDF, HTML and PostScript).

---

**See also**

[Printer list](http://support.automation.siemens.com/WW/llisapi.dll?aktprim=0&lang=en&referer=%2fWW%2f&func=cslib.csinfo&siteid=csius&caller=view&extranet=standard&viewreg=WW&nodeid0=10805558&objaction=csopen)

### Printing via print server (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Print servers enable access to network printers. Print jobs are routed to a corresponding printer via the print server.

> **Note**
>
> Printing takes place via the print server for the following HMI devices:
>
> - KTP Mobile Panels (as of device version V13)
> - Comfort Panels
> - PC with WinCC Runtime Advanced

#### Requirements

- The print server deploys the "RAW" mode.

  > **Note**
  >
  > For additional information on settings, refer to the relevant print server documentation.
- The device is interconnected via Ethernet with the print server or with a printer featuring an integrated print server.
- External print servers are interconnected with a printer via USB port.
- The IP address and port used are identical in the "Printer Properties" of the HMI device and on the print server.

#### Procedure

1. Open the "Control Panel" on your HMI device.
2. Select "Printer". The "Printer Properties" dialog box opens.

   ![Procedure](images/13096411531_DV_resource.Stream@PNG-de-DE.png)

   ![Procedure](images/13096411531_DV_resource.Stream@PNG-de-DE.png)
3. Select a printer from the "Printer Language" selection list.
4. Select the "PrintServer" entry from the "Port" selection list.
5. Enter the IP address and the port used for communication with the printer in the "IP:Port" input field.
6. Select any additional printer settings.

**Note**

Use ":" as delimiter between the IP address and the port number. For example: "192.168.56.23:**9100**".

> **Note**
>
> You can also print over the network.
>
> Select the "Port" entry from the "Network:" selection list for this.
>
> In the "Network:" selection box, select the network path, consisting of the computer name and the printer name, for example "\\server12\\printer01".

### Memory requirement of recipes (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The following calculation of memory requirements of recipes is only valid for Windows CE devices.

#### Calculation of memory requirements

The memory space required by each recipe (in KB) is derived from the sum of D1 + D2 + D3.

Valid is:

- D1 = (number of entries x 5 + M + 8):1024

  Applies to M:

  M = Accumulated length of all tag names = sum of characters in all tag names (UTF8 coded, max. 255 bytes per tag name) used in the entries.
- D2 = [(number of data records x 12) + 4]:1024
- D3 = [number of data records x (data record length + N) + 4]:1024

  Applies to N:

The total length of the name of the corresponding data record in all languages (max. 255 bytes per language) + overhead per data record (1 byte + number of languages * 3 bytes).

D1, D2 and D3 are rounded to the next higher number.

#### Memory requirements for using arrays

The memory required by each recipe (in KB) is derived from the sum of D1 + D2 + D3.

Valid is:

- D1 = (number of entries x 5 + M + 8):1024

  Each element of the tag array used counts as a single entry.

  Applies to M:

  M = (length of the array tag name + K) x  number of array elements

  Applies to K:

  K = 3: 2 to 9 elements in the array

  K = 4: 10 to 99 elements in the array

  K = 5: 100 to 999 elements in the array

  K = 6: 1000 to 9999 elements in the array

  K = 7: 10000 to 12000 elements in the array
- D2 = [(number of data records x 12) + 4] : 1024
- D3 = [number of data records x (data record length + N) + 4] : 1024

  Applies to N:

The total length of the name of the corresponding data record in all languages (max. 255 bytes per language) + overhead per data record (1 byte + number of languages * 3 bytes).

D1, D2 and D3 are rounded to the next higher number.

> **Note**
>
> If you use both tags and arrays in a recipe, you have to add the results of both formulas to calculate the total memory required.

### Memory requirements of recipes for Basic Panels (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

The following calculation of the memory requirements for recipes applies to Basic Panels.

#### Restrictions

The HMI device provides 39 KB of memory space for recipes. This memory space may not be exceeded. The total memory space for recipes is calculated as follows: Total of all recipes + recipe with highest memory requirement.

Each recipe may not exceed a maximum memory space of 19 KB.

#### Calculation of memory requirements

The memory space requirement of each recipe (in KB) is calculated based on the three addends D1 + D2 + D3.

Valid is::

- D1 = number of data records x M

  Rule for M (size of a data record):

  M = 1 x number of elements of a byte + 2 x number of elements of 2 bytes + 4 x number of elements of 4 bytes + 8 x number of elements of 8 bytes + K

  Rule for K (size of the string elements):

  K = number of string elements x (string length + 1) x 2

- D2 - data record size

  D2 = 4 + number of languages x 8 + number of languages x (4 + 4 x number of data records + (length of the data record name + 1) x 2 x number of data records) + 8 + 8 x number of data records

  Or rewritten:

  D2 = 12 + 8 x number of data records + number of languages x (12 + number of data records x (4 + (length of the data record name +1) x 2))

- D3 - shared memory

  D3 = 14 + number of elements

> **Note**
>
> Arrays and single elements can be calculated as described above.

## Performance features of the devices (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basic Panel (Basic Panels)](#basic-panel-basic-panels)
- [Basic Panel 2nd Generation (Basic Panels)](#basic-panel-2nd-generation-basic-panels)
- [Mobile Panel (Panels, Comfort Panels)](#mobile-panel-panels-comfort-panels)
- [Comfort Panel (Panels, Comfort Panels)](#comfort-panel-panels-comfort-panels)
- [WinCC Runtime Advanced (RT Advanced)](#wincc-runtime-advanced-rt-advanced)
- [WinCC Runtime Professional (RT Professional)](#wincc-runtime-professional-rt-professional)
- [Orientation help for performance in Runtime (WinCC Runtime Professional) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#orientation-help-for-performance-in-runtime-wincc-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Orientation help for communication in Runtime (WinCC Runtime Professional) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#orientation-help-for-communication-in-runtime-wincc-runtime-professional-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Basic Panel (Basic Panels)

#### Basic Panel

The following table helps you assess whether your project meets the performance features of the HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

#### Tags

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of tags in the project<sup> 1)</sup> | 250 | 500 | 250 (mono) 500 (color) | 500 | 500 | 500 |
| Number of PowerTags<sup> 2)</sup> | -- | -- | -- | -- | -- | -- |
| Number of elements per array | 100 | 100 | 100 | 100 | 100 | 100 |
| Number of local tags | -- | -- | -- | -- | -- | -- |
| Number of structures | -- | -- | -- | -- | -- | -- |
| Number of structure elements | -- | -- | -- | -- | -- | -- |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the total number of all internal tags and all used PowerTags. |
| 2) | PowerTags are tags used for communication between controller and HMI. For a panel, the number of PowerTags is limited by the maximum number of tags in the project. |

#### Alarms

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of alarm classes | 32 | 32 | 32 | 32 | 32 | 32 |
| Number of discrete alarms | 200 | 200 | 200 | 200 | 200 | 200 |
| Number of analog alarms | 15 | 15 | 15 | 15 | 15 | 15 |
| Length of an alarm in characters | 80 | 80 | 80 | 80 | 80 | 80 |
| Number of process values per alarm | 8 | 8 | 8 | 8 | 8 | 8 |
| Size of the alarm buffer<sup> 1)</sup> | 256 | 256 | 256 | 256 | 256 | 256 |
| Number of queued alarm events | 64 | 64 | 64 | 64 | 64 | 64 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all states of the alarms of all configured alarm classes and includes the alarms of alarm classes which are not shown in an alarm view due to the configuration. |

#### Screens

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of screens | 50 | 50 | 50 | 50 | 50 | 50 |
| Number of objects per screen | 30 | 30 | 30 | 30 | 30 | 30 |
| Number of tags per screen<sup> 1)</sup> | 30 | 30 | 30 | 30 | 30 | 30 |
| Number of complex objects per screen<sup> 2)</sup> | 5 | 5 | 5 | 5 | 5 | 5 |
| Number of array elements per screen<sup> 3)</sup> | 100 | 100 | 100 | 100 | 100 | 100 |

| Symbol | Meaning |
| --- | --- |
| 1) | This includes all tags used in scripts or used to animate objects. |
| 2) | Complex objects include: Bars, sliders, symbol library, clock, and all objects from the Controls area. |
| 3) | This also includes array elements contained in recipes. |

#### Recipes

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of recipes | 5 | 5 | 5 | 5 | 5 | 5 |
| Number of elements per recipe<sup> 1)</sup> | 20 | 20 | 20 | 20 | 20 | 20 |
| User data length in bytes per data record | -- | -- | -- | -- | -- | -- |
| Number of data records per recipe | 20 | 20 | 20 | 20 | 20 | 20 |
| Reserved memory for data records in the internal Flash | 40 KB | 40 KB | 40 KB | 40 KB | 40 KB | 40 KB |

| Symbol | Meaning |
| --- | --- |
| 1) | If arrays are used, each array element counts as one recipe element |

#### Logs

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of logs | -- | -- | -- | -- | -- | -- |
| Number of entries per log (including all log segments) <sup>1)</sup> | -- | -- | -- | -- | -- | -- |
| Number of log segments of all logs | -- | -- | -- | -- | -- | -- |
| Cyclic trigger for tag logging | -- | -- | -- | -- | -- | -- |
| Number of tags that can be logged per log | -- | -- | -- | -- | -- | -- |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of entries for the "segmented circular log" logging method is the total number for all sequential logs. The product of the number of sequential logs and the number of data records per sequential log may not exceed the system limit |

#### Trends

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of trends<sup> 1)</sup> | 25 | 25 | 25 | 25 | 25 | 25 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all trends in all trend views of a device. |

#### Text lists and graphics lists

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of graphics lists | 100 | 100 | 100 | 100 | 100 | 100 |
| Number of text lists | 150 | 150 | 150 | 150 | 150 | 150 |
| Number of entries per text or graphics list | 30 | 30 | 30 | 30 | 30 | 30 |
| Number of graphic objects of all graphic lists | 500 | 500 | 500 | 500 | 500 | 500 |
| Number of text elements of all text lists | 500 | 500 | 500 | 500 | 500 | 500 |

#### Scripts

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of scripts <sup>1)</sup><sup>2)</sup> | -- | -- | -- | -- | -- | -- |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of scripts results from the number of user-defined functions (global scripts in the project tree) and the number of internal scripts in the faceplates. If an faceplate type uses a script, the number of scripts of each faceplate instance must be considered. |
| 2) | A maximum of 20 simultaneously triggered scripts can be processed. |

#### Communication

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of connections | 4 | 4 | 4 | 4 | 4 | 4 |
| Number of connections based on "SIMATIC HMI HTTP" | -- | -- | -- | -- | -- | -- |

#### Help system

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Length of a tooltip in characters | 500 | 500 | 500 | 500 | 500 | 500 |

#### Languages

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of runtime languages | 5 | 5 | 5 | 5 | 5 | 5 |

#### Scheduler

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Time-triggered tasks<sup> 1)</sup> | -- | -- | -- | -- | -- | -- |

| Symbol | Meaning |
| --- | --- |
| 1) | Event-triggered tasks are not relevant for the system limits |

#### User administration

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Number of user groups | 50 | 50 | 50 | 50 | 50 | 50 |
| Number of authorizations | 32 | 32 | 32 | 32 | 32 | 32 |
| Number of users of all user groups | 50 | 50 | 50 | 50 | 50 | 50 |

#### Project

|  | KP300 Basic | KP400 Basic | KTP400 Basic | KTP600 Basic | KTP1000 Basic | TP1500 Basic |
| --- | --- | --- | --- | --- | --- | --- |
| Size of the project file "*.srt" | 1024 KB | 1024 KB | 1024 KB | 1024 KB | 1024 KB | 1024 KB |

---

**See also**

[S7-1200 manual](http://support.automation.siemens.com/WW/view/en/36932465/0/en)

### Basic Panel 2nd Generation (Basic Panels)

#### Basic Panel 2nd Generation

The following table helps you assess whether your project meets the performance features of the HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

#### Tags

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of tags in the project<sup> 1)</sup> | 800 | 800 | 800 | 800 |
| Number of PowerTags<sup> 2)</sup> | -- | -- | -- | -- |
| Number of elements per array | 100 | 100 | 100 | 100 |
| Number of local tags | -- | -- | -- | -- |
| Number of structures | -- | -- | -- | -- |
| Number of structure elements | -- | -- | -- | -- |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the total number of all internal tags and all used PowerTags. |
| 2) | PowerTags are tags used for communication between controller and HMI. For a panel, the number of PowerTags is limited by the maximum number of tags in the project. |

#### Alarms

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of alarm classes | 32 | 32 | 32 | 32 |
| Number of discrete alarms | 1000 | 1000 | 1000 | 1000 |
| Number of analog alarms | 25 | 25 | 25 | 25 |
| Length of an alarm in characters | 80 | 80 | 80 | 80 |
| Number of process values per alarm | 8 | 8 | 8 | 8 |
| Size of the alarm buffer<sup> 1)</sup> | 256 | 256 | 256 | 256 |
| Number of queued alarm events | 64 | 64 | 64 | 64 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all states of the alarms of all configured alarm classes and includes the alarms of alarm classes which are not shown in an alarm view due to the configuration. |

#### Screens

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of screens | 250 | 250 | 250 | 250 |
| Number of objects per screen | 100 | 100 | 100 | 100 |
| Number of tags per screen<sup> 1)</sup> | 100 | 100 | 100 | 100 |
| Number of complex objects per screen<sup> 2)</sup> | This information is not relevant for Basic Panels 2nd Generation. |  |  |  |
| Number of recipe displays per screen | 10 | 10 | 10 | 10 |
| Number of trend views per screen | 8 | 8 | 8 | 8 |
| Number of alarm displays per screen | 20 | 20 | 20 | 20 |
| Number of user displays per screen | 1 | 1 | 1 | 1 |
| Number of system diagnostic displays per screen | 5 | 5 | 5 | 5 |
| Number of system functions per screen | 150 | 150 | 150 | 150 |
| Number of multiplex tags per screen | 100 | 100 | 100 | 100 |

| Symbol | Meaning |
| --- | --- |
| 1) | This includes all tags used in scripts or used to animate objects. |
| 2) | Complex objects include: Bars, sliders, symbol library, clock, and all objects from the Controls area. |

#### Recipes

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of recipes | 50 | 50 | 50 | 50 |
| Number of elements per recipe<sup> 1)</sup> | 100 | 100 | 100 | 100 |
| User data length in KB per data record | 32 | 32 | 32 | 32 |
| Number of data records per recipe | 100 | 100 | 100 | 100 |
| Reserved memory for data records in the internal Flash | 256 KB | 256 KB | 256 KB | 256 KB |

| Symbol | Meaning |
| --- | --- |
| 1) | If arrays are used, each array element counts as one recipe element |

#### Logs

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of data logs | 1 | 1 | 1 | 1 |
| Number of alarm logs | 1 | 1 | 1 | 1 |
| Number of entries per log (including all log segments) <sup>1)</sup> | 10000 | 10000 | 10000 | 10000 |
| Number of log segments of all logs | 400 | 400 | 400 | 400 |
| Number of tags that can be logged per log | 10 | 10 | 10 | 10 |
| Cyclic trigger for tag logging | 1 s | 1 s | 1 s | 1 s |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of entries for the "segmented circular log" logging method is the total number for all sequential logs. The product of the number of sequential logs and the number of data records per sequential log may not exceed the system limit |

#### Trends

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of trends<sup> 1)</sup> | 25 | 25 | 25 | 25 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all trends in all trend views of a device. |

#### Text lists and graphics lists

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of graphics lists | 100 | 100 | 100 | 100 |
| Number of text lists | 300 | 300 | 300 | 300 |
| Number of entries per text or graphics list | 100 | 100 | 100 | 100 |
| Number of graphic objects of all graphic lists | 1000 | 1000 | 1000 | 1000 |
| Number of text elements of all text lists | 2500 | 2500 | 2500 | 2500 |

#### Scripts

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of scripts <sup>1)</sup><sup>2)</sup> | -- | -- | -- | -- |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of scripts results from the number of user-defined functions (global scripts in the project tree) and the number of internal scripts in the faceplates. If an faceplate type uses a script, the number of scripts of each faceplate instance must be considered. |
| 2) | A maximum of 20 simultaneously triggered scripts can be processed. |

#### Communication

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of connections | 4 | 4 | 4 | 4 |
| Number of connections based on "SIMATIC HMI HTTP" | -- | -- | -- | -- |

#### Help system

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Length of a tooltip in characters | 500 | 500 | 500 | 500 |

#### Languages

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of runtime languages | 10 | 10 | 10 | 10 |

#### Scheduler

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Time-triggered tasks<sup> 1)</sup> | -- | -- | -- | -- |

| Symbol | Meaning |
| --- | --- |
| 1) | Event-triggered tasks are not relevant for the system limits |

#### User administration

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Number of user groups | 50 | 50 | 50 | 50 |
| Number of authorizations | 32 | 32 | 32 | 32 |
| Number of users of all user groups | 50 | 50 | 50 | 50 |

#### Project

|  | KTP400 Basic | KTP700 Basic | KTP900 Basic | KTP1200 Basic |
| --- | --- | --- | --- | --- |
| Size of the project file "*.srt" | 10 MB | 10 MB | 10 MB | 10 MB |

### Mobile Panel (Panels, Comfort Panels)

#### Mobile Panel

The following tables of system limits help you assess whether your project conforms to the system limits of a given HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

#### Tags

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile TP1000F Mobile |
| --- | --- | --- | --- |
| Number of tags in the project<sup> 1)</sup> | 2048 | 2048 | 2048 |
| Number of PowerTags<sup> 2)</sup> | -- | -- | -- |
| Number of elements per array | 1000 | 1000 | 1000 |
| Number of local tags | 1000 | 1000 | 1000 |
| Number of structures | 999 | 999 | 999 |
| Number of structure elements | 400 | 400 | 400 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the total number of all internal tags and all used PowerTags. |
| 2) | PowerTags are tags used for communication between controller and HMI. For a panel, the number of PowerTags is limited by the maximum number of tags in the project. |

#### Alarms

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F MobileKTP700F Mobile |
| --- | --- | --- | --- |
| Number of alarm classes | 32 | 32 | 32 |
| Number of discrete alarms | 4000 | 4000 | 4000 |
| Number of analog alarms | 200 | 200 | 200 |
| Length of an alarm in characters | 80 | 80 | 80 |
| Number of process values per alarm | 8 | 8 | 8 |
| Size of the alarm buffer<sup> 1)</sup> | 1024 | 1024 | 1024 |
| Number of queued alarm events | 500 | 500 | 500 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all states of the alarms of all configured alarm classes and includes the alarms of alarm classes which are not shown in an alarm view due to the configuration. |

#### Screens

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F MobileKTP700F Mobile |
| --- | --- | --- | --- |
| Number of screens | 500 | 500 | 500 |
| Number of objects per screen | 50 | 400 | 400 |
| Number of tags per screen<sup> 1)</sup> | 50 | 400 | 400 |
| Number of complex objects per screen<sup> 2)</sup> | 5 | 20 | 20 |

| Symbol | Meaning |
| --- | --- |
| 1) | This includes all tags used in scripts or used to animate objects. |
| 2) | Complex objects include: Bars, sliders, symbol library, clock, and all objects from the Controls area. |

#### Recipes

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F MobileKTP700F Mobile |
| --- | --- | --- | --- |
| Number of recipes | 300 | 300 | 300 |
| Number of elements per recipe<sup> 1)</sup> | 1000 | 1000 | 1000 |
| User data length in bytes per data record | 262144 | 262144 | 262144 |
| Number of data records per recipe | 500 | 500 | 500 |
| Reserved memory for data records in the internal Flash | 2 MB | 2 MB | 2 MB |

| Symbol | Meaning |
| --- | --- |
| 1) | If arrays are used, each array element counts as one recipe element |

#### Logs

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F MobileKTP700F MobileKTP700F Mobile |
| --- | --- | --- | --- |
| Number of logs | 50 | 50 | 50 |
| Number of entries per log (including all log segments) <sup>1)</sup> | 20000 | 20000 | 20000 |
| Number of log segments of all logs | 400 | 400 | 400 |
| Cyclic trigger for tag logging | 1 s | 1 s | 1 s |
| Number of tags that can be logged per log | 2048 | 2048 | 2048 |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of entries for the "segmented circular log" logging method is the total number for all sequential logs. The product of the number of sequential logs and the number of data records per sequential log may not exceed the system limit |

#### Trends

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Number of trends<sup> 1)</sup> | 300 | 300 | 300 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all trends in all trend views of a device. |

#### Text lists and graphics lists

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Number of graphics lists | 500 | 500 | 500 |
| Number of text lists | 500 | 500 | 500 |
| Number of entries per text or graphics list | 500 | 500 | 500 |
| Number of graphic objects of all graphic lists | 4000 | 4000 | 4000 |
| Number of text elements of all text lists | 40000 | 40000 | 40000 |

#### Scripts

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Number of scripts <sup>1)</sup><sup>2)</sup> | 100 | 100 | 100 |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of scripts results from the number of user-defined functions (global scripts in the project tree) and the number of internal scripts in the faceplates. If an faceplate type uses a script, the number of scripts of each faceplate instance must be considered. |
| 2) | A maximum of 20 simultaneously triggered scripts can be processed. |

#### Communication

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile/TP1000F Mobile |
| --- | --- | --- | --- |
| Number of connections | 8 | 8 | 8 |
| Number of connections based on "SIMATIC HMI HTTP" | 8 | 8 | 8 |
| Maximum number of connected Sm@rtClients (including a service client) | 3 | 3 | 3 |

**Address length of OPC UA server variables**

Maximum address length of OPC UA server variables for addressing by a SIMATIC HMI OPC UA client: 256 characters

#### Mobile Wireless

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Number of zones | 254 | 254 | 254 |
| Number of effective ranges | -- | -- | -- |
| Number of assigned transponders - zones | -- | -- | -- |
| Number of assigned transponders - effective ranges | -- | -- | -- |
| Number of effective ranges (RFID) | -- | -- | -- |
| Number of RFID tags that can be assigned to effective ranges (RFID) in a project | -- | -- | -- |

#### Help system

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Length of a tooltip in characters | 500 | 500 | 500 |

#### Languages

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Number of runtime languages | 32 | 32 | 32 |

#### Scheduler

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Time-triggered tasks<sup> 1)</sup> | 48 | 48 | 48 |

| Symbol | Meaning |
| --- | --- |
| 1) | Event-triggered tasks are not relevant for the system limits |

#### User administration

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Number of user groups | 50 | 50 | 50 |
| Number of authorizations | 32 | 32 | 32 |
| Number of users of all user groups | 50 | 50 | 50 |

#### Project

|  | KTP400F Mobile | KTP700 Mobile / KTP700F Mobile | KTP900 Mobile / KTP900F Mobile |
| --- | --- | --- | --- |
| Size of the project file "*.fwc" | 4 MB | 12 MB | 12 MB |

---

**See also**

[S7-1200 manual](http://support.automation.siemens.com/WW/view/en/36932465/0/en)

### Comfort Panel (Panels, Comfort Panels)

#### Comfort Panel

The following tables of system limits help you assess whether your project conforms to the system limits of a given HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

> **Note**
>
> **Graphic objects on Comfort Panels**
>
> The use of 32-bit graphic objects increases memory requirements for the project file on Comfort Panels.  
> The use of jpeg graphic objects reduces memory requirements for the project file on Comfort Panels.

#### Tags

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of tags in the project<sup> 1)</sup> | 1024 | 2048 | 4096 | 4096 | 4096 |
| Number of PowerTags<sup> 2)</sup> | -- | -- | -- | -- | -- |
| Number of elements per array | 1000 | 1000 | 1000 | 1000 | 1000 |
| Number of local tags | 500 | 1000 | 2000 | 2000 | 2000 |
| Number of structures | 999 | 999 | 999 | 999 | 999 |
| Number of structure elements | 400 | 400 | 400 | 400 | 400 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the total number of all internal tags and all used PowerTags. |
| 2) | PowerTags are tags used for communication between controller and HMI. For a panel, the number of PowerTags is limited by the maximum number of tags in the project. |

#### Alarms

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of alarm classes | 32 | 32 | 32 | 32 | 32 |
| Number of discrete alarms | 2000 | 4000 | 6000 | 6000 | 6000 |
| Number of analog alarms | 50 | 200 | 200 | 200 | 200 |
| Length of a message text in characters | 80 | 80 | 80 | 80 | 80 |
| Number of process values per alarm | 8 | 8 | 8 | 8 | 8 |
| Size of the alarm buffer<sup> 1)</sup> | 256 | 1024 | 1024 | 1024 | 1024 |
| Number of queued alarm events | 64 | 500 | 500 | 500 | 500 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all states of the alarms of all configured alarm classes and includes the alarms of alarm classes which are not shown in an alarm view due to the configuration. |

#### Screens

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of screens | 500 | 500 | 750 | 750 | 750 |
| Number of objects per screen | 50 | 400 | 600 | 600 | 600 |
| Number of tags per screen<sup> 1)</sup> | 50 | 400 | 400 | 400 | 400 |
| Number of complex objects per screen<sup> 2)</sup> | 5 | 20 | 40 | 40 | 40 |

| Symbol | Meaning |
| --- | --- |
| 1) | This includes all tags used in scripts or used to animate objects. |
| 2) | Complex objects include: Bars, sliders, symbol library, clock, and all objects from the Controls area. |

#### Recipes

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of recipes | 100 | 300 | 500 | 500 | 500 |
| Number of elements per recipe<sup> 1)</sup> | 200 | 1000 | 2000 | 2000 | 2000 |
| User data length in KB per data record | 32 | 256 | 512 | 512 | 512 |
| Number of data records per recipe | 200 | 500 | 1000 | 1000 | 1000 |
| Reserved memory for data records in the internal Flash | 512 KB | 2 MB | 4 MB | 4 MB | 4 MB |

| Symbol | Meaning |
| --- | --- |
| 1) | If arrays are used, each array element counts as one recipe element. |

#### Logs

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of logs | 10 | 50 | 50 | 50 | 50 |
| Number of entries per log (including all log segments) <sup>1)</sup> | 10000 | 20000 | 50000 | 50000 | 50000 |
| Number of log segments of all logs | 400 | 400 | 400 | 400 | 400 |
| Cyclic trigger for tag logging | 1 s | 1 s | 1 s | 1 s | 1 s |
| Number of tags that can be logged per log | 100 | 2048 | 2048 | 2048 | 2048 |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of entries for the "segmented circular log" logging method is the total number for all sequential logs. The product of the number of sequential logs and the number of data records per sequential log may not exceed the system limit |

#### Trends

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of trends <sup>1)</sup> | 50 | 300 | 400 | 400 | 400 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all trends in all trend views of a device. |

#### Text lists and graphics lists

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of graphics lists | 100 | 500 | 500 | 500 | 500 |
| Number of text lists | 300 | 500 | 500 | 500 | 500 |
| Number of entries per text or graphics list | 30 | 500 | 500 | 500 | 500 |
| Number of graphic objects of all graphic lists | 1000 | 4000 | 4000 | 4000 | 4000 |
| Number of text elements of all text lists | 2500 | 40000 | 40000 | 40000 | 40000 |

#### Scripts

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of scripts <sup>1)</sup><sup>2)</sup> | 50 | 100 | 200 | 200 | 200 |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of scripts results from the number of user-defined functions (global scripts in the project tree) and the number of internal scripts in the faceplates. If an faceplate type uses a script, the number of scripts of each faceplate instance must be considered. |
| 2) | A maximum of 20 simultaneously triggered scripts can be processed. |

#### Communication

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of connections incl. HTTP connections and OPC connections | 4 | 8 | 8 | 8 | 8 |
| Number of OPC connections including OPC UA | 4 | 8 | 8 | 8 | 8 |
| Number of connections based on "SIMATIC HMI HTTP" | 4 | 8 | 8 | 8 | 8 |
| Maximum number of connected Sm@rtClients (including a service client) | 2 | 3 | 3 | 2 | 1 |

**Address length of OPC UA server variables**

Maximum address length of OPC UA server variables for addressing by a SIMATIC HMI OPC UA client: 256 characters

#### Help system

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Length of a tooltip in characters | 500 | 500 | 500 | 500 | 500 |

#### Languages

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of runtime languages | 32 | 32 | 32 | 32 | 32 |

#### Scheduler

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Time-triggered tasks<sup> 1)</sup> | 10 | 48 | 48 | 48 | 48 |

| Symbol | Meaning |
| --- | --- |
| 1) | Event-triggered tasks are not relevant for the system limits. |

#### User administration

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Number of user groups | 50 | 50 | 50 | 50 | 50 |
| Number of authorizations | 32 | 32 | 32 | 32 | 32 |
| Number of users of all user groups | 50 | 50 | 50 | 50 | 50 |

#### Project

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200  TP700 Comfort Outdoor  TP1500 Comfort Outdoor | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Size of the project file "*.fwc" | 4 MB | 12 MB | 24 MB | 24 MB | 24 MB |

---

**See also**

[S7-1200 manual](http://support.automation.siemens.com/WW/view/en/36932465/0/en)

### WinCC Runtime Advanced (RT Advanced)

#### WinCC Runtime Advanced

The following tables of system limits help you assess whether your project conforms to the system limits of a given HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

#### Tags

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of tags in the project<sup> 1)</sup> | 6144 | 12288 | 24576 |
| Number of PowerTags<sup> 2)</sup> | 128 - 4096 | 128 – 8192 | 128-16384 |
| Number of elements per array | 1600 | 1600 | 1600 |
| Number of internal tags | 2048 | 4096 | 8192 |
| Number of structures | 999 | 999 | 999 |
| Number of structure elements | 400 | 400 | 400 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the total number of all internal tags and all used PowerTags. |
| 2) | PowerTags are tags used for communication between controller and HMI. For a panel, the number of PowerTags is limited by the maximum number of tags in the project. |

#### Alarms

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of alarm classes | 32 | 32 | 32 |
| Number of discrete alarms | 4000 | 6000 | 6000 |
| Number of analog alarms | 500 | 500 | 500 |
| Length of an alarm in characters | 80 | 80 | 80 |
| Number of process values per alarm | 8 | 8 | 8 |
| Size of the alarm buffer<sup> 1)</sup> | 1024 | 2048 | 2048 |
| Number of queued alarm events | 500 | 500 | 500 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all states of the alarms of all configured alarm classes and includes the alarms of alarm classes which are not shown in an alarm view due to the configuration. |

#### Screens

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of screens | 500 | 750 | 750 |
| Number of objects per screen | 400 | 600 | 600 |
| Number of tags per screen<sup> 1)</sup> | 400 | 400 | 400 |
| Number of complex objects per screen<sup> 2)</sup> | 40 | 40 | 40 |

| Symbol | Meaning |
| --- | --- |
| 1) | This includes all tags used in scripts or used to animate objects. |
| 2) | Complex objects include: Bars, sliders, symbol library, clock, and all objects from the Controls area. |

#### Recipes

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of recipes | 999 | 1000 | 1000 |
| Number of elements per recipe<sup> 1)</sup> | 2000 | 2000 | 2000 |
| User data length in KB per data record | 256 | 512 | 512 |
| Number of data records per recipe | 5000 | 5000 | 5000 |
| Reserved memory for data records in the internal Flash | -- | -- | -- |

| Symbol | Meaning |
| --- | --- |
| 1) | If arrays are used, each array element counts as one recipe element |

> **Note**
>
> To ensure optimal performance of the recipe display in runtime, it is recommended to create no more than 500 recipe queries or 500 recipe query elements.

#### Logs

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of logs | 100 | 100 | 100 |
| Number of entries per log (including all log segments) <sup>1)</sup> | 500000 | 500000 | 500000 |
| Number of log segments of all logs | 400 | 400 | 400 |
| Cyclic trigger for tag logging | 1 s | 1 s | 1 s |
| Number of tags that can be logged per log | 6144 | 12288 | 24576 |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of entries for the "segmented circular log" logging method is the total number for all sequential logs. The product of the number of sequential logs and the number of data records per sequential log may not exceed the system limit |

#### Trends

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of trends<sup> 1)</sup> | 800 | 800 | 800 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the number of all trends in all trend views of a device. |

#### Text lists and graphics lists

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of graphics lists | 500 | 500 | 500 |
| Number of text lists | 500 | 500 | 500 |
| Number of entries per text or graphics list | 3500 | 3500 | 3500 |
| Number of graphic objects of all graphic lists | 2000 | 4000 | 4000 |
| Number of text elements of all text lists | 30000 | 40000 | 40000 |

#### Scripts

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of scripts <sup>1)</sup><sup>2)</sup> | 200 | 200 | 200 |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of scripts results from the number of user-defined functions (global scripts in the project tree) and the number of internal scripts in the faceplates. If an faceplate type uses a script, the number of scripts of each faceplate instance must be considered. |
| 2) | A maximum of 100 simultaneously triggered scripts can be processed. |

#### Communication

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of connections | 8 | 8 | 8 |
| Number of OPC connections including OPC UA | 8 | 8 | 8 |
| Number of connections based on "SIMATIC HMI HTTP" | 16 | 16 | 16 |
| Maximum number of connected Sm@rtClients (including a service client) | 4 <sup>1)</sup> | 4 <sup>1)</sup> | 4 <sup>1)</sup> |

**PROFIBUS: Number of connections**

With Runtime Professional up to 8 MPI connections or PROFIBUS Softnet connections are licensed, for example CP5622. Additional PROFIBUS Softnet licenses are not required.

With a corresponding SIMATIC NET license you may also establish more than 8 PROFIBUS connections. For this you need PROFIBUS Hardnet, for example CP5623.

**Address length of OPC UA server variables**

Maximum address length of OPC UA server variables for addressing by a WinCC OPC UA client: 256 characters

#### Help system

|  | KTP400  KP400 | TP700, KP700  TP900, KP900  TP1200, KP1200 | TP1500  KP1500 | TP1900 | TP2200 |
| --- | --- | --- | --- | --- | --- |
| Length of a tooltip in characters | 320 <sup>1)</sup>  500 <sup>2)</sup> | 320 <sup>1)</sup>  500 <sup>2)</sup> | 320 <sup>1)</sup>  500 <sup>2)</sup> | 320 <sup>1)</sup>  500 <sup>2)</sup> | 320 <sup>1)</sup>  500 <sup>2)</sup> |

| Symbol | Meaning |
| --- | --- |
| 1)  2) | For devices with HMI device version 12 or lower  For devices with HMI device version higher than 12 |

#### Languages

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of runtime languages | 32 | 32 | 32 |

#### Scheduler

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Time-triggered tasks<sup> 1)</sup> | 48 | 48 | 48 |

| Symbol | Meaning |
| --- | --- |
| 1) | Event-triggered tasks are not relevant for the system limits |

#### User administration

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Number of user groups | 50 | 50 | 50 |
| Number of authorizations | 32 | 32 | 32 |
| Number of users of all user groups | 100 | 100 | 100 |

#### Project

|  | WinCC Runtime Advanced  Device version prior to 13 | WinCC Runtime Advanced  Device version as of 13 | WinCC Runtime Advanced device version greater than or equal to 14 |
| --- | --- | --- | --- |
| Size of the project file "*.fwc" | No limiting | No limiting | No limiting |

---

**See also**

[S7-1200 manual](http://support.automation.siemens.com/WW/view/en/36932465/0/en)

### WinCC Runtime Professional (RT Professional)

#### WinCC Runtime Professional

The following tables of system limits help you assess whether your project conforms to the system limits of a given HMI device.

The specified maximum values are not additive. It cannot be guaranteed that configurations running on the devices at the full system limits will be functional.

In addition to the specified limits, allowances must be made for restrictions imposed by configuration memory resources.

#### Tags

|  | WinCC Runtime Professional |
| --- | --- |
| Number of tags in the project<sup> 1)</sup> | 500,000 |
| Number of PowerTags<sup> 2)</sup> | Depends on the license |
| Number of elements per array | 2,000 |

| Symbol | Meaning |
| --- | --- |
| 1) | Corresponds to the total number of all internal tags and all used PowerTags. |
| 2) | PowerTags are tags used for communication between controller and HMI. For a panel, the number of PowerTags is limited by the maximum number of tags in the project. |

#### Screens

It is possible that image files larger than 100 MB are not displayed in WinCC Runtime.

|  | WinCC Runtime Professional |
| --- | --- |
| Objects per screen <sup>1)</sup> | No limit <sup>2)</sup> |
| Layers per screen | 32 |
| Screens per project | No limit <sup>2)</sup> |
| Screen size in pixels | 10,000 x 10,000 |
| Screen object nesting | 20 |
| Number of colors | 24-bit color depth, 8-bit alpha channel for transparency |

| Symbol | Meaning |
| --- | --- |
| 1) | The number and complexity of objects affects performance |
| 2) | Limited by system resources. |

#### Alarms

|  | WinCC Runtime Professional |
| --- | --- |
| Configurable alarms per server/single-station | 150,000 |
| Process tags per alarm line | 10 |
| User text blocks per alarm line | 10 |
| Alarm classes | 256 |
| Alarm priorities | 17 (0...16) |

#### Alarms in Runtime

|  | Maximum |
| --- | --- |
| Alarms per alarm log | No limit <sup>1)</sup> |
| Alarms per historical alarm list (short-term) | 1,000 |
| Alarms per historical alarm list (long-term) | 1,000 <sup>2)</sup> |
| Alarms per alarm control | 5,000 <sup>3)</sup> |

| Symbol | Meaning |
| --- | --- |
| 1) | Limited by system resources. |
| 2) | On single-station, or server or client per server if "LongTimeArchiveConsistency" has been set to "no". On single-station, server, or client if "LongTimeArchiveConsistency" has been set to "yes". |
| 3) | On single-station or server, or on client per server. |

> **Note**
>
> Alarm bursts and continuous alarm load may be generated simultaneously on a single-user station or server.

#### Logs

|  | WinCC Runtime Professional |
| --- | --- |
| Trend view per screen | 25 |
| Trends per trend view | 80 |
| Values per trend view | A maximum of 134,217,728 bytes can be transferred from the Tag Logging Server to the trend views. If a process value contains 20 bytes, approximately 6.7 million values can be displayed or exported to a *.csv file. |
| Table view per screen | 25 |
| Columns per table view | 12 |
| Values per table view | 30,000 |
| Logs per single-station/server | 100 |
| Logging tags per single-station/server <sup>1)</sup> | 80,000 |

| Symbol | Meaning |
| --- | --- |
| 1) | Depends on the Logging PowerPack used for logging tags. The basic version contains 500 logging tags. |

> **Note**
>
> Screen selection times may be extremely long in the event of multiple maximum values.

#### Recipes

|  | WinCC Runtime Professional |
| --- | --- |
| Number of recipes | No limit |
| Number of recipe elements <sup>1)</sup> | 500 |
| Number of recipe data records | 10,000 |
| Number of views | No limit |

| Symbol | Meaning |
| --- | --- |
| 1) | Maximum 1,000,000 recipe elements in total |

> **Note**
>
> To ensure optimal performance of the recipe display in runtime, it is recommended to create no more than 500 recipe queries or 500 recipe query elements.

**Example of a permissible configuration limit in Runtime**

You reach the maximum number of 1,000,000 recipe elements, for example, with the following configurations:

- 10,000 recipe data records each with 100 recipe elements
- 2,000 recipe data records each with 500 recipe elements

Assumption: Each recipe element is connected to a tag.

Keep in mind that such configuration limits are also influenced by the hardware used and by other configurations.

#### Reports

|  | WinCC Runtime Professional |
| --- | --- |
| Configurable reports | No limit <sup>1)</sup> |
| Report lines per detail view | 66 |
| Tags per report <sup>2)</sup> | 300 |

| Symbol | Meaning |
| --- | --- |
| 1) | Limited by system resources. |
| 2) | The number of tags per report depends on the performance of process communication. |

#### Reports in runtime

|  | Maximum |
| --- | --- |
| Alarm sequence reports running simultaneously per server/client | 1 |
| Alarm log reports running simultaneously | 3 |

#### User administration

|  | Maximum |
| --- | --- |
| Number of users | 200 |

#### Communication

|  | S7-1200 | S7-1511 | S7-1513 | S7-1516 | S7-1518 |
| --- | --- | --- | --- | --- | --- |
| Maximum number of WinCC system | 2 | 20 | 30 | 41 | 62 |
| ISO-on-TCP connections | - | 64, 4 of which are reserved for ES | 96, 4 of which are reserved for ES | 128, 4 of which are reserved for ES | 192, 4 of which are reserved for ES |
| Maximum number of connected PLCs per Runtime | 128 |  |  |  |  |
| Maximum number of connected PLCs with Softnet via a network adapter | 128 |  |  |  |  |

| Symbol | Meaning |
| --- | --- |
| - Note that a maximum of 200 tags per controller should be configured for communication with S7-1200 PLCs. - If several HMI devices access a PLC, this limit applies for all HMI devices. - You can learn how many HMI devices can simultaneously access a SIMATIC S7-1200 in the manual for the PLC.   Entry ID: [36932465](https://support.industry.siemens.com/cs/document/36932465/simatic-s7-s7-1200-automatisierungssystem?dti=0&lc=de-WW) |  |

**Relation between HMI connection and connection resource**

An HMI connection to WinCC RT Professional requires up to three connection resources.

> **Note**
>
> **Different limits for connections over PROFIBUS and PROFINET**
>
> Note that connections over PROFIBUS have other limits regarding relations between the HMI connections and the connection resources than PROFINET.
>
> For communication over PROFIBUS and SIMATIC NET you must also take into account the limits of the SIMATIC NET components (CPs).
>
> You can find additional information about SIMATIC NET components in the respective SIMATIC NET manual: "PC software SIMATIC NET PC".

**PROFIBUS: Number of connections**

With Runtime Professional up to 8 MPI connections or PROFIBUS Softnet connections are licensed, for example CP5622. Additional PROFIBUS Softnet licenses are not required.

With a corresponding SIMATIC NET license you may also establish more than 8 PROFIBUS connections. For this you need PROFIBUS Hardnet, for example CP5623.

#### OPC UA

|  | WinCC Runtime Professional |
| --- | --- |
| Maximum address length of OPC UA server variables for addressing by a WinCC OPC UA client | 256 characters |

#### Configurations - configuration limits in the multi-station system

|  | WinCC Runtime Professional |
| --- | --- |
| WinCC clients in a system | 32 <sup>1) 2)</sup> |
| Web clients in a system | 150 <sup>2) 3)</sup> |

| Symbol | Meaning |
| --- | --- |
| 1) | The number of clients is reduced to four if the server also used as operator station. |
| 2) | Mixed configuration: 32 clients + 3 Web clients |
| 3) | Mixed configuration: 50 Web clients + 1 WinCC client |

### Orientation help for performance in Runtime (WinCC Runtime Professional) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### WinCC Runtime Professional

The following tables help you to assess operational performance of your project in Runtime.

> **Note**
>
> The values specified greatly depend on the hardware used.

#### Screens in Runtime

| Screen change from an empty screen to... | Time in seconds |
| --- | --- |
| Screen with standard objects (100 objects) | 1 |
| Screen with 2480 I/O fields (8 internal tags) | 2 |
| Screen with 1000 I/O fields (1000 internal tags) | 1 |
| 10 MB screen (bitmap) | 1 |
| Alarm view | 2 |
| Table view with 4 columns, each with 120 values <sup>1)</sup> | 1 |

| Symbol | Meaning |
| --- | --- |
| 1) | The values specified are valid for data from "Tag Logging Fast". |

#### Alarms in Runtime

|  | Maximum |
| --- | --- |
| Continuous alarm load without losses (single-station/server) | 10/sec |
| Message burst (single-station/server) | 2000/10 seconds at intervals of 5 minutes <sup>1)</sup> |

| Symbol | Meaning |
| --- | --- |
| 1) | Alarms are possibly lost if the interval before the next message burst is less than five minutes. |

> **Note**
>
> Message bursts and continuous alarm load may be generated simultaneously on a single-station or server.

#### Logs in runtime

|  | Maximum |
| --- | --- |
| Logging in database for server/single-station (Tag Logging Fast) | 5000 values/second <sup>1) </sup> |
| Logging in database for server/single-station (Tag Logging Slow) | 1000 values/second <sup>1)</sup> <sup>2)</sup> |
| Number of values printed in a report | The number of values printed depends on the number of values displayed in the trend view. |

| Symbol | Meaning |
| --- | --- |
| 1) | The values specified are valid for logging data without signature. |
| 2) | With Tag Logging Slow, expect longer screen selection times for a given amount of data than for Tag Logging Fast. |

#### Recipes in Runtime - boundary conditions

| Hardware used | Software used | Configuration |
| --- | --- | --- |
| Intel® Core™ i3-6100U 2.30 GHz  4 GB RAM  No hardware connection | Windows 7  WinCC V14.0 SP1 | One WinCC tag per field  300,000 entries each: - 10 fields with 30,000 data records - 500 fields with 600 data records |

#### Recipes in Runtime - measured values

|  | 10 fields | 500 fields |
| --- | --- | --- |
| Screen change to a screen with integrated recipe view.  Result of measurement depends on the fill level of the control:  It can take up to 15 seconds for complete display upon initial loading or if considerable configuration changes are made in the user log. | 1 second | 5 seconds |
| Read data record:  Read the value to the corresponding tag after the button in the recipe view was clicked. | 1 - 2 seconds <sup>1)</sup> | n seconds <sup>2)</sup> |
| Write data record:   Write the value to the corresponding tag and display of the tag in the I/O field after the button in the recipe view was clicked. | 1 - 3 seconds <sup>1)</sup> | n seconds <sup>2)</sup> |
| Focus change from the first to the last data record. | 1 - 2 seconds | 1 - 2 seconds |

| Symbol | Meaning |
| --- | --- |
| 1) | 10 fields with a total of 10 tags. |
| 2) | 500 fields with a total of 500 tags. |

#### Reports in runtime

|  | Maximum |
| --- | --- |
| Alarm sequence reports running simultaneously per server/client | 1 |
| Alarm log reports running simultaneously | 3 |

### Orientation help for communication in Runtime (WinCC Runtime Professional) (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### WinCC Runtime Professional

Install the SIMATIC NET software from the supplied DVD. To use WinCC Runtime Professional with a S7-1200 / S7-1500 controller, you must not exceed the specific system limitations for the corresponding S7 controller. The following explains the system limits for tags, whose values are reported by an S7-1200/S7-1500. The "WinCC Channel Diagnosis" tool is used to make the determination.

> **Note**
>
> Refer to the [parameter tables](https://support.industry.siemens.com/cs/ww/de/view/98699910/en) for the specific system limits of your S7-1200 / S7-1500 controller .

#### Attributes

| Attribute | Description |
| --- | --- |
| Plc Attributes (max) | This value refers to the maximum number of tags that can be read cyclically. By default, the communication load of an S7 controller is not configured under 30% (default value: 50%).  "Plc Attributes" can be used by one or more WinCC Runtime systems. The number of concurrent tags of all connected WinCC Runtime systems for each S7 controller therefore needs to be added up. You can learn how to determine the number of concurrent tags in the section "Critical factors of concurrent tags". |
| Minimum Plc Attributes (free) | The "Minimum Plc Attributes (free)" value is based on empirical values. The value applies to the steady state with no screen change. The minimum number „Minimum Plc Attributes (free)" may be temporarily lower. If the number approaches 0, cyclic reading with low cycle times begins, briefly slowing down communication with the S7 controller. |
| Number WinCC Runtime Professional | The "Number WinCC Runtime Professional" indicates the maximum number of WinCC Runtime Professional systems which can be connected to a S7 controller. The number includes a WinCC ES that is connected to the S7 controller. |
| Subscription Memory | The "Subscription Memory" stores a certain amount of messages sent by the PLC. If the limits of the "Subscription Memory" are exceeded, the messages are not displayed completely.  When the limits of the "Subscription Memory" are exceeded, you can follow these steps:  - Reduce the number of subscriptions - Move to scalar values, for example: Integer/LongInteger require less memory capacity than a string - Use a higher version of the PLC that allows more subscriptions |

#### Example

> **Note**
>
> To ensure stable communication with the S7 controller, you should not exceed the "Number of concurrent tags per S7".

You can read the values for the "Plc Attributes (max)", "Minimum Plc Attributes (free)" columns of the parameter table from the WinCC Channel Diagnosis Tool under "CCS7PLUSCHANNEL" and the corresponding connection. The number of concurrent tags per S7 controller can be determined from the "Plc Tag Subscriptions" counter: The number of registered tags per cycle time is displayed. In the following example, the number of registered tags is 2003 (500 ms: 103 tags, 1 s: 400 tags, 2 s: 500 tags, 5 s: 1000 tags).

![Example](images/80378788619_DV_resource.Stream@PNG-de-DE.png)

#### Critical factors of concurrent tags

The number of concurrent tags can be obtained from the following table. Cycle times less than 5 seconds are relevant here. Generally, only the tags which are detected by an S7 controller are relevant. In the example above, these are the tags of the "PLC1516" connection.

| Functionality | Concurrent tags |
| --- | --- |
| Archiving | Sum of all tags per acquisition cycle. |
| HMI alarms | Number tags for discrete alarms + number tags for analog alarms + number associated values from tags per alarm. |
| Scheduler | Sum of all unused tags per cyclic event. With SmartTags, only the Smart Tags with cache usage are relevant.   Number of trigger tags used. |
| Scripts | This affects cyclic scripts, specifically the functions within that use a cache. Information about using the cache is provided in the documentation. Examples:  - HmiRuntime.Tags().Read 0. - SmartTags when using the cache.   All affected tags are included in the count. |
| Screen | Number of tags directly related to object properties.   Number tags used directly in controls with cycles (for example, gauge control, trend views, table views).   Number of tags used in cyclic animations, C scripts, VB scripts.  Number of trigger tags used. |
| OPC server (DA / UA) | Sum of all cyclically reported items. |
| Control Development | Sum of all cyclically read tags. |

---

**See also**

[S7-1200 / S7-1500 parameter tables](https://support.industry.siemens.com/cs/ww/de/view/98699910/en)
