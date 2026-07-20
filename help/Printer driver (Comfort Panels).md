---
title: "Printer driver (Comfort Panels)"
package: PrinterWCCCenUS
topics: 9
devices: [Comfort Panels]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Printer driver (Comfort Panels)

This section contains information on the following topics:

- [Validity (Comfort Panels)](#validity-comfort-panels)
- [Supported HMI devices (Comfort Panels)](#supported-hmi-devices-comfort-panels)
- [Setting up the printer driver (Comfort Panels)](#setting-up-the-printer-driver-comfort-panels)
- [Installation (Comfort Panels)](#installation-comfort-panels)
- [Transferring the Options (Comfort Panels)](#transferring-the-options-comfort-panels)

## Validity (Comfort Panels)

### Validity

This document includes a description of the enhancements made possible with optional package printer driver.

Install the optional package to implement the extended functionality. The installation provides new printer drivers for several HMI devices.

If necessary you can install individual printer drivers with the tool SIMATIC ProSave on your HMI device. For more details on which printer drivers are available for which HMI devices please refer to the section "Supported HMI devices".

### Installation

Please follow the instructions in the "Installation" section to install the "Optional package printer driver V1.4".

### Application example

You can find an application example on the subject "Printing with HMI Panels" on the internet at

["Printing with SIMATIC Comfort Panels" application example](https://support.industry.siemens.com/cs/ww/en/view/58205602)

---

**See also**

["Printing with SIMATIC Comfort Panels" application example](https://support.industry.siemens.com/cs/ww/en/view/58205602)

## Supported HMI devices (Comfort Panels)

### Contents of the add-on package

The "Add-on package printer driver V1.4" contains the following printer drivers for the specified HMI devices.

The printer driver supports all printer options of the HMI device.

| HMI device | Brother P-Touch  **QL 650 TD** <sup>1)</sup> | Brightek WH-AB, WH-C1, WH-E19 | Postscript |
| --- | --- | --- | --- |
| KP400 Comfort  KTP400 Comfort | USB | USB | Yes |
| KP700 Comfort   TP700 Comfort | USB | USB | Yes |
| KP900 Comfort   TP900 Comfort | USB | USB | Yes |
| KP1200 Comfort   TP1200 Comfort | USB | USB | Yes |
| KP1500 Comfort   TP1500 Comfort | USB | USB | Yes |
| TP1900 Comfort | USB | USB | Yes |
| TP2200 Comfort | USB | USB | Yes |
| USB: Connect printer directly to HMI device via USB port   <sup>1) </sup>Report printout only. |  |  |  |
|  |  |  |  |

> **Note**
>
> Please note that Postscript is a well-known and open communication protocol and theoretically, for this reason, statements could be changed by third parties. It is recommended that the printer be connected by USB in plants where security is especially critical.

## Setting up the printer driver (Comfort Panels)

This section contains information on the following topics:

- [Postscript (Comfort Panels)](#postscript-comfort-panels)
- [HTML (Comfort Panels)](#html-comfort-panels)
- [PDF (Comfort Panels)](#pdf-comfort-panels)

### Postscript (Comfort Panels)

#### Define PostScript V1.4 as printer on the HMI device

1. Open the Control Panel.
2. Start the "Printer" application.
3. Under "Printer Language" in the "Printer Properties" dialog, select: the entry "PostScript V1.4".

**Note**

Not all printers support PostScript. Make sure that your printer supports this printer language.

Select the "Draft mode" option to increase the print speed.

### HTML (Comfort Panels)

#### Introduction

The application "HTMLSettings.exe" is available on the desktop of the HMI device after installation of the "HMTL V1.3" printer driver.

#### Selecting the storage location

1. Open the application "HTMLSettings.exe" on the desktop of your HMI device.
2. Open "Storage Location" in the tab.
3. Under "Primary Location", select "USB-Stick", for example, for the storage location.
4. Select the directory in which the file is to be saved after printing.

#### Selecting the file name

1. Open the "HTMLSettings.exe" application
2. Open the "HTML File Names" tab
3. Select the settings for the names of the HTML file for the print-out.
4. Click on "Apply" to confirm your settings.
5. Select "Default" to retain the default settings for file name assignment.

#### Selecting columns for printing reports

1. Open the "HTMLSettings.exe" application
2. Open the "Columns Attributes" tab.
3. Select an attribute in the "Available Columns" category:
4. Add this attribute to your selection with the ">>" button.
5. If required, define whether the selected attribute is to be displayed as an image or as a hyperlink in the HTML file.
6. To deselect attributes from the "Selected Columns" category, select an attribute and click the "<<" button.

#### Selecting style sheets

1. Open the "HTMLSettings.exe" application
2. Open the "Advanced Options" tab.
3. Under "Enter Style Sheet File Path", select the storage location of the style sheets you wish to use.
4. Select the file to be used.
5. Select the directory for links.
6. Select the directory for images.

#### Defining HTML V1.3 as printer on the HMI device

1. Open the Control Panel.
2. Start the "Printer" application.
3. Under "Printer Language" in the "Printer Properties" dialog, select: the entry "HTML V1.3".
4. Select "Draft Mode" for rapid storage of the HTML file.

### PDF (Comfort Panels)

#### Introduction

The application "PDFSettings.exe" is available on the desktop of the HMI device after installation of the "PDF V1.3" printer driver.

#### Selecting the storage location

1. Start the application "PDFSettings.exe" on the desktop of your HMI device.
2. Open "Storage Location" in the tab.
3. Under "Primary Location", select "USB-Stick", for example, for the storage location.
4. Select the directory in which the file is to be saved after printing.

#### Selecting the file name

1. Open the "PDFSettings.exe" application
2. Open the "PDF File Names" tab
3. Select the settings for the names of the PDF file for the print-out.
4. Click on "Apply" to confirm your settings.
5. Select "Default" to retain the default settings for file name assignment.

#### Define PDF V1.3 as printer on the HMI device

1. Open the Control Panel.
2. Start the "Printer" application.
3. In the "Printer Properties" dialog, select the entry "PDF V1.3" under "Printer Language:".
4. Select "Draft Mode" for rapid storage of the PDF file.

#### Rule

The table below shows the device-specific differences for printing PDFs:

| Mode | KP700 Comfort  TP700 Comfort  KP900 Comfort  TP900 Comfort  KP1200 Comfort  TP1200 Comfort | KP1500 Comfort  TP1500 Comfort  TP1900 Comfort  TP2200 Comfort |
| --- | --- | --- |
| Normal Mode | 10 seconds per page | 2 seconds per page |
| Draft Mode | 2-3 seconds per page | 1 second per page |

## Installation (Comfort Panels)

### Requirements

ProSave is installed on the PC.

### Procedure

1. Double click the "PROSAVE-OPT.exe" file.
2. Select "<Setup>" in the "WinZip Self-Extractor" dialog.
3. Select the language for the installation menu.
4. Select "<Continue>" in the "Optional package printer driver setup" dialog.
5. Confirm the next box with "<Install>".
6. Confirm the "Optional package printer driver setup" message with "<Finish>".

**Note**

To transfer the printer driver to a HMI device, please follow the instructions in the chapter "Transfer of options".

## Transferring the Options (Comfort Panels)

### Requirements

The HMI device is connected to a PC on which ProSave is installed.

### Procedure

1. Restart ProSave on your PC.
2. Select the corresponding HMI device type in the "General" tab.
3. Select the type of connection between the HMI device and the PC.
4. Set the connection parameters.
5. Select the "Options" tab.
6. Select the desired printer driver under "Available options".
7. Set "Transfer" mode on the HMI device.

   If automatic transfer mode is enabled on the HMI device, the device automatically sets "Transfer" mode when a transfer is initiated.
8. Select ">>" on the PC to start the transfer.
9. Follow the ProSave instructions and the instructions which appear on the HMI device.

   During the installation of the printer driver, a status display appears indicating the progress of the operation.

### Result

When the installation is complete, the new printer driver is displayed in ProSave in the "Installed options" area. The new printer driver can now be used on the HMI device.
