---
title: "Establishing a remote connection with TeleService"
package: PETeleServenUS
topics: 83
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Establishing a remote connection with TeleService

This section contains information on the following topics:

- [Basics of working with TeleService](#basics-of-working-with-teleservice)
- [Working with the phone book](#working-with-the-phone-book)
- [Remote connections as dial-up connections](#remote-connections-as-dial-up-connections)
- [Remote VPN connections](#remote-vpn-connections)
- [CPU controlled TeleService remote connections](#cpu-controlled-teleservice-remote-connections)
- [Notes on troubleshooting](#notes-on-troubleshooting)

## Basics of working with TeleService

This section contains information on the following topics:

- [Introduction to TeleService](#introduction-to-teleservice)
- [TeleService functionality](#teleservice-functionality)
- [Telephone book at TeleService](#telephone-book-at-teleservice)

### Introduction to TeleService

#### Introduction

TeleService gives your controller telecommunication capability. You can manage, control and monitor distributed plants centrally by means of remote connections.

#### Scope of functions

TeleService allows you to use the range of TIA portal functions via a telephone network or an Internet connection by establishing a remote connection to a remote system. The online connection allows you to edit a remote system in the usual way with the TIA Portal.

#### Advantages

Using TeleService offers the following advantages:

- You can easily access even remote sections of plants and include them in a complete system.
- You can offer rapid help and support in the event of faults in a remote system without having to go there yourself.
- You can employ your resources effectively.
- It significantly reduces costs.
- It can significantly reduce plant downtimes.
- It improves the efficiency of your plant.

---

**See also**

[TeleService functionality](#teleservice-functionality)

### TeleService functionality

#### TeleService fields of application

TeleService offers the following the fields of application:

- **Access to remote systems (remote maintenance):**
    
  You can manage, control, and monitor remote systems centrally by means of remote connections.   
  This is possible with an S7-300/400 CPU, an S7-1200 CPU and an S7-1500 CPU and a TS Adapter MPI or a TS Adapter IE.
- **Establishing connections from and to remote systems (PG-AS remote link):**
    
  You can use PRODAVE MPI V5.0 and newer to establish a remote connection to a remote system, and the communications instruction "PG_DIAL" to establish a remote connection from a remote system.  
  This is possible with an S7-300/400 CPU and a TS Adapter MPI.
- **Data exchange between systems (AS-AS remote link):**
    
  The communications instruction "AS_DIAL" allows two automation systems to exchange process data over the telephone network.   
  This is possible with an S7-300/400 CPU and a TS Adapter MPI.
- **Sending a text message from a system:**
    
  An automation system can send a message (SMS) via a GSM wireless modem using the communications instruction "SMS_SEND" ".  
  This is possible with an S7-300/400 CPU and a TS Adapter MPI.
- **Sending an email from a system**
    
  An automation system can also send an email with the following communications instructions and a TS Adapter IE .

  - S7-300/400 CPUs (CPU S7-31x-2PN/DP or CPU 41x-3PN/D) use the instruction "AS_MAIL"
  - S7-1200 CPUs use the instruction "TM_MAIL"
  - S7-1500 CPUs use the instruction "TMAIL_C"

### Telephone book at TeleService

#### Introduction

By double clicking the "phone book" folder in the project tree you open the phone book editor displaying the TeleService phone book.

Each version of the TIA Portal has its own "global phone book". If a global phone book from an earlier version of the TIA Portal is found in a more recent version of the TIA Portal, you will be asked once if you want to import this phone book.

This gives you the advantage of being able to import the system data from the previous version into the more recent version of the TIA Portal.

#### Global phone book properties

The global phone book is used in TeleService to manage specific system data that are required to establish a remote connection.

When you open the phone book for the first time, you will see an empty phone book with all available columns; in all other cases, the last phone book edited is displayed.

You can enter any number of systems in a phone book. Systems contain the data required for establishing a remote connection, for example, the name and location of the device and the phone number to be dialed, along with all country-specific details. With VPN connections, you can enter an IP address or a DNS name instead of the phone number.

The TS adapters used for establishing the connection are distinguished by color, depending on whether a TS Adapter MPI or a TS Adapter IE is used for establishing the connection.

---

**See also**

[Working with the phone book](#working-with-the-phone-book)

## Working with the phone book

This section contains information on the following topics:

- [Basics on working with the phone book](#basics-on-working-with-the-phone-book)
- [Structure of the phone book](#structure-of-the-phone-book)
- [Symbols in the phone book](#symbols-in-the-phone-book)
- [Manage phone book](#manage-phone-book)

### Basics on working with the phone book

#### Working with the phone book

You have the following options when working with a phone book:

- Open phone book
- Save phone book
- Import phone book data
- Export phone book data
- Printing the phone book
- Use phone book data to establish a remote connection

You can implement these functions simply and easily by using the buttons in the phone book toolbar.

> **Note**
>
> **Access to phone books**
>
> The phonebook is user specific in TeleService. However, it is not possible to access the global phone book with more than one instance of the TIA portal at the same time.

---

**See also**

[Open phone book](#open-phone-book)
  
[Saving phone book](#saving-phone-book)
  
[Exporting phone book data](#exporting-phone-book-data)
  
[Printing the phone book](#printing-the-phone-book)
  
[Structure of the phone book](#structure-of-the-phone-book)

### Structure of the phone book

#### Introduction

A global phone book in TeleService is used to manage the data you require for establishing a remote connection. Once you have created the connection data and saved it in the phone book, you can access it each time you want to establish a remote connection.

> **Note**
>
> **Telephone book as of V17**
>
> The database format of the telephone book is no longer supported. Import the telephone book into a TIA version &lt;= V16 and export it. The file format is updated during the export.

#### Structure of the phone book

The integrated global phone book in TeleService contains the following columns:

| Column name | Description |
| --- | --- |
| Plant name | Enter a name for your system. |
| Adapter type | Select the TS Adapter type used in the drop-down list: TS Adapter MPI or TS Adapter IE. |
| Connection type | Select the required connection type: Dial-up connection or VPN connection. |
| Area code | Enter the required area code.  This column is only active with dial-up connections. This column cannot be edited for VPN connections. |
| Phone number/Address | Enter the required connection data for establishing the remote connection. For dial-up connections, this can be a phone number, and for VPN connections a DNS name or an IP address. |
| Country | Enter the country code.  This column is only active with dial-up connections. This column cannot be edited for VPN connections. |
| Fingerprint | Here you enter the associated fingerprint for setting up a VPN connection to the TS Adapter IE Advanced. |
| User name | Enter the user name you have logged on under. |
| Password | Enter the password for this user name. |
| Group | Enter the group if you have carried out grouping. |
| Company | Enter the company to be contacted. |
| Department | Enter the relevant department. |
| Street | Enter the street. |
| Town/City | Enter the town or city to which the remote connection is to be established. |
| Comment | Enter a comment if required. |

#### Showing or hiding columns

You can show or hide the individual columns. To do so, select the required column header and open the shortcut menu with the right mouse button.

### Symbols in the phone book

#### Meaning of the TeleService icons

The following table shows the meaning of the TeleService icons:

| Symbol | Meaning |
| --- | --- |
| ![Meaning of the TeleService icons](images/40690483851_DV_resource.Stream@PNG-de-DE.png) | Open the global phone book |
| ![Meaning of the TeleService icons](images/40690487307_DV_resource.Stream@PNG-de-DE.PNG) | Imports a phone book |
| ![Meaning of the TeleService icons](images/40690490763_DV_resource.Stream@PNG-de-DE.PNG) | Exports a phone book |
| ![Meaning of the TeleService icons](images/40684956683_DV_resource.Stream@PNG-de-DE.png) | Establishes a remote connection |
| ![Meaning of the TeleService icons](images/40690480395_DV_resource.Stream@PNG-de-DE.png) | Terminates the active remote connection |
| ![Meaning of the TeleService icons](images/40684960139_DV_resource.Stream@PNG-de-DE.PNG) | Establishes a remote connection or terminates it |
| ![Meaning of the TeleService icons](images/23000935819_DV_resource.Stream@PNG-de-DE.png) | Displays the connection to a TS Adapter IE in the phone book |
| ![Meaning of the TeleService icons](images/23001635211_DV_resource.Stream@PNG-de-DE.png) | Displays the connection to a TS Adapter MPI in the phone book |
| ![Meaning of the TeleService icons](images/40697202315_DV_resource.Stream@PNG-de-DE.PNG) | Adds a new row to the phone book |
| ![Meaning of the TeleService icons](images/40697300363_DV_resource.Stream@PNG-de-DE.PNG) | Inserts a new row in the phone book |

### Manage phone book

This section contains information on the following topics:

- [Open phone book](#open-phone-book)
- [Inserting rows in the phone book](#inserting-rows-in-the-phone-book)
- [Showing and hiding columns in the phone book](#showing-and-hiding-columns-in-the-phone-book)
- [Saving phone book](#saving-phone-book)
- [Importing phone book data](#importing-phone-book-data)
- [Exporting phone book data](#exporting-phone-book-data)
- [Printing the phone book](#printing-the-phone-book)
- [Defining dialing rules](#defining-dialing-rules)

#### Open phone book

##### Opening phone books

To open the phone book, follow these steps:

1. In the project tree, double-click on the "Phone book" folder under "Online access" &gt; "TeleService".
2. The phone book opens so that you can enter or edit the required system data.

#### Inserting rows in the phone book

##### Inserting rows in the phone book

To insert a new row in the phone book, follow these steps:

1. Select the row in front of which you want to insert a new row.
2. Click the "Insert row" button in the toolbar.

##### Result

A new row is inserted in the phone book above the selected row.

#### Showing and hiding columns in the phone book

##### Showing and hiding columns

To show or hide columns in the phone book, follow these steps:

1. Click a column header.
2. In the shortcut menu, select the "Show/hide columns" command.

   The selection of available columns is displayed.
3. To show a column, select the column's check box.
4. To hide a column, clear the column's check box.

##### Result

The respective columns are shown or hidden when displaying the phone book.

#### Saving phone book

##### Saving phone books

When you exit the phone book editor or the TIA Portal, you are asked whether you want to save the global phone book.

Click "Yes" to save the phone book.

#### Importing phone book data

##### Introduction

It is possible to import the phone book data from an external file or from an older version of the TIA Portal.

##### Requirement

You have already created an import-capable phone book file.

You have already created a phone book with an older version of the TIA Portal.

##### Importing phone book data from a phone book file

To import phone book data from a phone book file, follow these steps:

1. Open the "TeleService" folder under "Online access" in the project tree.
2. Double-click on the "Phone book" folder.
3. Click the "Import" button in the toolbar.
4. Confirm the query as to whether the current version of the work phone book should be saved, if appropriate with "Yes" and in the next dialog select where the phone book will be saved.
5. If you do not want to save the current state of the phone book, answer the prompt with "No". In the subsequent dialog, select the phone book file to which the current phone book should be stored.
6. Close the dialog box with "OK".

##### Result

The imported phone book data is displayed in the global phone book.

> **Note**
>
> **Defining dialing rules**
>
> Dialing rules must be defined before the "area code" and "country" columns in the imported phone book can be edited for dial-up connections.
>
> To define dialing rules, follow the link in the history.

##### Importing phone book data from an older version of the TIA Portal

To import the phone book data from an older version of the TIA Portal follow the steps below:

1. Open the "TeleService" folder under "Online access" in the project tree.
2. Double-click on the "Phone book" folder.
3. Click the "Import" button in the toolbar.
4. Confirm the query as to whether the current version of the work phone book should be saved, if appropriate with "Yes" and in the next dialog select where the phone book will be saved.
5. If you do not want to save the current state of the phone book, answer the prompt with "No".
6. In the following dialog enter the following path information "%appdata%\siemens\automation\TeleService\GlobalTeleServicePhoneBook.tel".
7. Close the dialog box with "OK".

##### Result

The phone book data imported from an older version of the TIA Portal is displayed in the global phone book.

> **Note**
>
> **Defining dialing rules**
>
> Dialing rules must be defined before the "area code" and "country" columns in the imported phone book can be edited for dial-up connections.
>
> To define dialing rules, follow the link in the history.

---

**See also**

[Defining dialing rules](#defining-dialing-rules)

#### Exporting phone book data

##### Introduction

It is possible to export phone book data to an external file.

##### Requirement

You have already created a phone book under TeleService with the corresponding system data.

##### Procedure

To export the phone book data, follow these steps:

1. Open the "TeleService" folder in project tree.
2. Double-click on the "Phone book" folder.
3. Click the "Export" button in the toolbar.
4. In the next dialog box, select where the current phone book is to be exported.
5. Close the dialog box with "OK".

##### Result

The exported phone book data are saved in the specified export file.

#### Printing the phone book

##### Printing phone books

You can print out all or some of the data in a phone book.

##### Proceed as follows:

1. Open the phone book.
2. Select the **Project &gt; Print** menu command or click on the appropriate button in the toolbar. The "Print" dialog will open.
3. Specify whether you wish to print the complete phone book or just part of it and set all other options.
4. Start the print job with "OK".

##### Result

The phone book data is printed on the default printer. If the printout is more than one page long, an identifier is printed after the page number at the bottom right corner of the page to indicate that there is another page. The last page does not have this symbol, indicating that no more pages are to follow.

#### Defining dialing rules

##### Procedure

To define location-specific dialing rules, follow these steps:

1. Open the "Online access" folder in the TIA Portal and select the "TeleService" folder.
2. Use the shortcut menu to access the "TeleService" properties.
3. In the dialog that follows, open the "Advanced settings" tab and activate the "Use dialing rules" option.
4. Click the "Adapt" button.
5. In the dialog that follows, enter the required location information for connection establishment.

   - For new locations, enter the country or region and the corresponding area code.
   - If required, set the correct destination code and pre-dial line for local/long-distance calls.
   - Select your chosen dialing mode for the location.
6. Exit the dialog by clicking "OK".
7. In the next dialog, select the location from which you wish to dial, and click "OK".
8. In the TeleService dialog that follows, check that the correct location appears under "Location".
9. Confirm your entries by clicking "OK".

> **Note**
>
> **Modem operation on a local loop or extension**
>
> You do not need to specify a pre-dial line if you operate your modem on a local loop (main telephone line). The fields for the pre-dial lines for local calls and long-distance calls must be empty.  
> If you operate your modem on an extension, you should enter the pre-dial lines which need to be called to access a local loop.

##### Example of the use of dialing rules

The following example illustrates the use of location-specific dialing rules for the city of Karlsruhe in Germany.

- In the TeleService phone book, you enter the phone number "1234567", without the area code and without the country code.

  **Result:**

  The phone number "1234567" is always dialed, irrespective of the location of the caller.
- In addition to the phone number "1234567", you enter the location-specific dial parameters for the Karlsruhe area code "0721" and the country code "+49" for Germany in the TeleService phone book.

  **Result:**

  "1234567" is dialed from Karlsruhe.

  "07211234567" is dialed from other towns in Germany.

  "00497211234567" is dialed from other countries.

> **Note**
>
> **Display in the phone book**
>
> The "area code" and "country" columns in the TeleService phone book can only be edited once you have defined the dialing rules as detailed above.

## Remote connections as dial-up connections

This section contains information on the following topics:

- [Basics for establishing a dial-up connection](#basics-for-establishing-a-dial-up-connection)
- [Telephone networks and modems](#telephone-networks-and-modems)
- [Access protection for dial-up connections](#access-protection-for-dial-up-connections)
- [TS adapter MPI](#ts-adapter-mpi)
- [TS adapter IE](#ts-adapter-ie)
- [Establishing a dial-up connection to a remote system](#establishing-a-dial-up-connection-to-a-remote-system)

### Basics for establishing a dial-up connection

#### Using a TS Adapter for dial-up connections

A TS Adapter is needed for establishing a remote dial-up connection using TeleService.

The TS Adapter is used to prepare an automation system for use with TeleService by connecting it to a telephone network via a modem. The TS Adapter has an integrated parameter memory in which a parameter set for TeleService operation is stored.

With the function "export adapter parameter", different parameter sets can be saved in external files, and reloaded in the TS Adapter via the function "import adapter parameter".

#### Establishing a remote dial-up connection

You can choose between a number of different TS Adapters, each of which offers a different functionality and different connection options.

The figure below shows two possible configurations for establishing a dial-up connection to a system with the TS Adapter IE.

![Establishing a remote dial-up connection](images/31204812171_DV_resource.Stream@PNG-en-US.png)

#### Overview of possible TS Adapter:

The TS Adapter comes in the following versions:

- TS Adapter II (also designated "TS Adapter MPI")
- TS Adapter IE Standard (also designated "TS Adapter IE")
- TS Adapter IE Basic (also designated "TS Adapter IE")

#### Designation "TS Adapter"

In the following pages, the designation "TS Adapter" stands for all versions. The relevant product designation is listed beside information which only applies to a specific version, for example, "TS Adapter II" or "TS Adapter IE Standard".

> **Note**
>
> For more detailed information on your TS Adapter, please refer to the documentation supplied with the TS Adapter.

---

**See also**

[Short description of the TS adapter MPI](#short-description-of-the-ts-adapter-mpi)
  
[Short description of the TS adapter IE](#short-description-of-the-ts-adapter-ie)
  
[Exporting adapter parameters](#exporting-adapter-parameters)
  
[Importing adapter parameters](#importing-adapter-parameters)

### Telephone networks and modems

This section contains information on the following topics:

- [Supported telephone networks and modems](#supported-telephone-networks-and-modems)
- [Installing the local modem](#installing-the-local-modem)
- [Connecting and configuring the remote modem](#connecting-and-configuring-the-remote-modem)

#### Supported telephone networks and modems

##### Telephone networks which can be used

TeleService can be used with digital networks (ISDN), analog networks and wireless networks (with GSM technology). This version supports a remote connection to a TS Adapter.

##### Modem support

TeleService has been implemented to be independent of the modem. This means that all standard modems which can be installed in the Windows Control Panel and are visible as modems can also be used by TeleService.

The choice of modem type is determined primarily by the existing hardware of the programming device/PC and the telephone network to be used.

##### The following modem types/media are supported:

- Modems (external modems at the COM interface, internal modems and PCMCIA cards)
- External ISDN adapter at the COM interface or USB interface
- Internal ISDN adapter with virtual COM interface (for example AVM CAPI port)
- External ISDN modems (ISDN adapter with integrated analog modem functionality) at the COM interface or USB interface
- Radio network modems with GSM technology, PCMCIA adapter card or data cable and mobile phone

##### Gateways

Gateways between the various telephone networks are in principle possible. Remote connections from an ISDN adapter to an analog modem and vice versa only function with special ISDN telephone adapters.

##### Performance in telephone networks

The data throughput of a remote connection depends on the modem and telephone network used and the quality of the telephone line.

#### Installing the local modem

##### Introduction

If you have already installed a modem for data transfer in your operating system, this modem can also be used for TeleService.

If a modem has not yet been installed for your operating system, one must be installed before you can establish a remote connection with TeleService.

##### Procedure

Proceed as follows:

1. Make sure your programming device/PC and the modem are switched off.
2. Physically connect the external modem to a COM or USB interface on your programming device/PC. You can also install an internal modem or a PCMCIA card in accordance with the manufacturer's specifications.
3. Now switch on the modem and then the programming device or the PC.

##### Result

Plug-and-play modems are recognized and installed automatically by the operating system. Dialogs will take you through the installation procedure.

> **Note**
>
> **Modems without plug-and-play**
>
> If your modem is not recognized automatically when switched on, you will have to install it yourself using the Control Panel.
>
> Please refer to the information in the documentation supplied with your modem.

#### Connecting and configuring the remote modem

##### Introduction

A modem must also be connected to the remote system before you can work with TeleService. This modem is designated the "remote modem".

##### Configuring the remote modem

The modem receives all parameters required for operation from the TS Adapter connected. These include data for initializing the modem and settings for serial transmission between the TS Adapter and the modem.

The data required for the remote modem is specified during the configuration of the TS Adapter.

The modem may be internal or external depending on the TS Adapter used.

##### How to connect a TS Adapter with an internal modem

1. Switch off the TS Adapter.
2. Connect the TS Adapter to the automation system.
3. Connect the TS Adapter to the telephone line.
4. Switch on the TS Adapter.

##### How to connect a TS Adapter with an external modem

1. Switch off the modem.
2. Connect the TS Adapter to the automation system.
3. Connect the TS Adapter to the modem using a modem cable.
4. Connect the modem to the telephone line.
5. Switch on the modem.
6. Switch on the TS Adapter.

> **Note**
>
> **Please note the following information on configuring the remote modem:**
>
> - The default parameters for the modem and the serial port set in the TS Adapter should in most cases ensure successful operation; changes in the parameter assignment will only be needed in rare cases.
> - You need only change the parameter assignment of the TS Adapter if a modem connection is not established or if factory settings are to be adapted or optimized.
> - TS Adapter parameter assignment can be changed via either a direct or a remote connection.

### Access protection for dial-up connections

This section contains information on the following topics:

- [Access protection information](#access-protection-information)
- [TeleService callback options](#teleservice-callback-options)
- [Levels of protection](#levels-of-protection)
- [Setting up access protection and callback number for the TS adapter](#setting-up-access-protection-and-callback-number-for-the-ts-adapter)
- [Complete a callback in TeleService](#complete-a-callback-in-teleservice)

#### Access protection information

##### Introduction

When you assign the parameters for your TS adapter, you can restrict access to the parameters of the TS adapter and access to remote systems.

##### Scope of access protection

Access protection only exists for remote connections; TS adapter parameter assignment can be accessed at any time in direct connection mode.

Access protection also exists in direct connection for the TS adapter IE.

##### Access protection information

The TS Adapter MPI is not delivered with access protection activated. There is a default password for the TS adapter IE.

The first user who assigns the parameters for this adapter can therefore activate access protection by defining the password for a user and/or a callback number.

This is a multi-level access protection with several users, each with or without administrator rights. For the TS adapter MPI there is only one adminstrator and no more than two users.

For a modem connection, only an administrator can define the two users and change and, if necessary, delete their settings. Those logged in as users can only change their own passwords and their own callback numbers. However, with the TS adapter MP you can access the process of assigning parameters of the TS adapter in direct connection, without restriction.

##### Advantages

Access protection offers the following advantages:

- Unauthorized access by persons outside the system is almost impossible.
- The plant operator bears most of the telephone costs.

#### TeleService callback options

##### Callback variants

The costs of a telephone connection are normally borne by the caller who establishes the dial-up connection.

TeleService can, however, be used so that after a short initial connection the modem connection is established again in the opposite direction, in other words initiated by the TS Adapter (callback). In this case, the plant operator bears the costs of the callback.

##### There are two callback variants in TeleService:

1. Callback to a number specified during connection establishment.
2. Callback to a number stored on the TS Adapter.

#### Levels of protection

##### Introduction

You can set up one of two possible levels of access protection for TeleService access to the TS Adapter. Different options are available with each protection level.

##### Access protection options

**Access protection level 1:**

The TS Adapter  is protected by the user name and password. You can access the TS Adapter via any telephone line and specify any callback number during connection establishment.

**Access protection level 2:**

The TS Adapter is protected by the user name, password, and the callback number. You can only access the TS Adapter from one telephone connection per user.

The table below sets out the above conditions for the various protection levels:

| Level of access protection | Administrator/User password | Callback number |
| --- | --- | --- |
| 1 | enter | do not enter |
| 2 | enter | enter |

##### Logging on to TS Adapter

When you log on to the TS Adapter and after you have set up access protection, enter your user name, the corresponding password and, if desired, a callback number:

| Level of access protection | Administrator/User password | Callback number |
| --- | --- | --- |
| 1 | enter | do not enter or enter any callback number |
| 2 | enter | do not enter |

If you have entered a callback number during connection establishment (access protection level 1) or have stored a callback number in the TS Adapter (access protection level 2), the modem connection is disconnected and the TS Adapter calls the specified number back.

#### Setting up access protection and callback number for the TS adapter

##### Introduction

During the parameter assignment for the TS adapter MPI in TeleService, you can set up access protection and a callback number for the parameter assignment of the adapter and connection to the remote system. The following describes the parameter assignment for a TS adapter MPI. The parameter assignment of a TS adapter IE is carried out in analog. The specific method is described in the web help of this adapter.

##### Requirement

A TS Adapter MPI is connected to your computer and is displayed in the project tree under "Accessible nodes".

##### Procedure

To set up access protection for the TS adapter, proceed as follows:

1. Click on the command "Assign TS Adapter MPI parameters" in the project tree.
2. Open the "Access security" tab.
3. Enter a password for your user name and/or number that you want the modem to call back following logon.

   - If you are an administrator, you can change all the settings for administrators and users, and delete or create users.
   - If you are logged on as a user, you can only change your own settings (password and callback number).
4. Confirm all entries before exiting the dialog with "OK".
5. Click the "Yes" button to confirm the following query.

##### Result

The parameter assignment for the access protection and the callback number is saved in the non-volatile memory of the TS adapter MPI.

> **Note**
>
> **Important points to note when setting up access protection:**
>
> - The settings in the "Modem" tab must correspond to the conditions at the plant if callback functionality is to be guaranteed.
> - Entering an incorrect callback number in the role of "ADMIN" user will mean you are no longer able to access the TS Adapter MPI over a remote connection!
> - Test the callback number before you enter it as the "ADMIN" user by calling the given callback number during connection establishment (access protection level 1).

#### Complete a callback in TeleService

##### Callback options

Two different callback variants can be set up in TeleService.

The following callback options are available:

- Callback to a number specified during connection establishment.
- Callback to a number stored on the TS Adapter

##### Callback to a number specified during connection establishment

1. In the project tree of the TIA Portal, click the "Online access" folder.
2. Click on the "TeleService" folder it contains.
3. Double-click the "Set up/close remote connection" entry. The "Set up remote connection to the remote system" dialog opens.
4. In the "Adapter type" drop-down list, select the adapter type used.
5. Select the "dial-up connection" under "Connection type" if it is not already selected.
6. Select the modem you are using under "Local Settings".
7. Enter the phone number to be dialed in the appropriate box or open the phone book by clicking on the button behind it and take the desired phone number from the phone book.
8. Enter your user name and associated password of the TS adapter.
9. If you want a "Connection setup with callback", select the appropriate option button.
10. Click the "Connect" button to establish the required remote connection. This button only becomes active when you have entered all the parameters needed to establish a remote connection. Any remote connection is displayed under "Status".
11. Enter the desired callback number in the dialog that follows.

##### Result

The remote connection to the desired system is made with callback.

The connected system is shown with the corresponding icon in the project tree.

> **Note**
>
> This procedure is useful if the costs of the modem connection are to be borne by the plant operator and if the actual callback number is not fixed, which means callback is not always to the same receiver. It is particularly useful for mobile users.

##### Callback to a number stored on the TS Adapter

1. Assign the parameters for the desired callback number in the TS adapter.
2. Establish a connection to the TS adapter as described above, and observe the following features:

   - Enter the user name and password for which the callback number parameters are assigned in the TS adapter.
   - The check box "Establish a connection with callback" does not have to be selected, since the callback number is already known by the TS adapter.

##### Result

Callback to a number stored on the TS adapter has been established. If a remote connection is established, the callback occurs from the remote system.

> **Note**
>
> This procedure offers the highest level of access protection. However, it does pose a risk: if the callback number stored on the TS Adapter is not correct, it will no longer be possible to access the TS Adapter over a modem connection. The device can in such a case only be put back into operation by changing the parameter settings on site.

### TS adapter MPI

This section contains information on the following topics:

- [Short description of the TS adapter MPI](#short-description-of-the-ts-adapter-mpi)
- [How the TS adapter MPI works](#how-the-ts-adapter-mpi-works)
- [Operating a TS adapter MPI in direct connection mode](#operating-a-ts-adapter-mpi-in-direct-connection-mode)
- [Operating a TS adapter MPI in modem connection mode](#operating-a-ts-adapter-mpi-in-modem-connection-mode)
- [TS adapter MPI configuration options](#ts-adapter-mpi-configuration-options)
- [Configuring TS adapter MPI](#configuring-ts-adapter-mpi)
- [Restoring default parameter assignment for TS adapter MPI](#restoring-default-parameter-assignment-for-ts-adapter-mpi)
- [Exporting adapter parameters](#exporting-adapter-parameters)
- [Importing adapter parameters](#importing-adapter-parameters)

#### Short description of the TS adapter MPI

##### TS Adapter MPI:

The designation "TS Adapter MPI" is a collective term for allTS Adapter with an MPI/DP interface.

The TS Adapter MPI comes in the following versions:

- As TS Adapter I (parameters cannot be assigned via the TIA Portal)
- as TS Adapter II

The table below provides a short description of the functionalities. For detailed information on your TS Adapter, please refer to the documentation supplied with your TS Adapter.

| TS Adapter II: |  |
| --- | --- |
| Direct connection | Connection via the Universal Serial Bus (USB). The firmware can be replaced.   The modem is integrated or can also be connected as external modem. The TS Adapter II switches automatically between the modems. As long as no external modem is connected, the adapter will use the internal modem. |
| There are two variants | - With internal analog modem. An external modem can also be connected to the RS232 port. - With internal ISDN adapter. An external modem can also be connected to the RS232 port. |

##### Use of the designation "TS Adapter"

For TeleService the designation "TS Adapter" is the generalization for all versions. The relevant product designation is listed beside information which only applies to a specific version of a TS Adapter, for example, "TS Adapter II", "TS Adapter IE Standard" or "TS Adapter IE Basic".

#### How the TS adapter MPI works

##### How the TS Adapter MPI Works

In line with the configuration, the TS Adapter MPI connects the serial port or USB port of your programming device/personal computer (direct connection) or the serial port of a modem (modem connection) to the MPI/PROFIBUS network of your automation system.

The TS Adapter MPI has a non-volatile memory. Parameters for the following functions are stored in this memory:

- The MPI/PROFIBUS network (network parameters)
- The mode of the modem used
- The serial port to the modem
- Access protection

##### Default parameter assignment

The TS Adapter comes with default parameter assignment. The parameters can be set and saved to the non-volatile memory of the TS adapter in a parameter assignment session.

When "Direct connection" is configured, the TS Adapter will only use the network parameters for access to the MPI/PROFIBUS network.

In the "Modem connection" configuration, all the parameters stored on the TS Adapter will be activated.

> **Note**
>
> For more detailed information on the configuration of your TS Adapter, please refer to the documentation supplied with it.

#### Operating a TS adapter MPI in direct connection mode

##### Direct connection with TS Adapter MPI

The direct connection is used to assign the parameters of the TS Adapter MPI. The same configuration also allows you to go online in the TIA Portal and thereby check the assigned MPI/PROFIBUS parameters for bus compatibility. This means that (as with a PC adapter) SIMATIC S7/C7 systems can be accessed via the MPI/DP interface without an MPI/PROFIBUS module occupying a slot for a programming device/PC.

Access protection for the TS Adapter is not active in direct connection configuration. This means that the parameter assignment of the TS Adapter can be changed without any problems, for example by importing adapter parameters.

> **Note**
>
> **Display of the TS Adapter MPI in the TIA Portal**
>
> As soon as you have connected a TS Adapter MPI to the programming device/PC via the USB interface, the "TS Adapter" folder is displayed in the project tree in the TIA Portal.
>
> When you open the folder, you can assign the parameters of the connected TS Adapter MPI via the following dialog.

##### Establishing the direct connection for TS Adapter MPI

Direct connection mode means there is a direct connection via the TS Adapter MPI between the programming device/personal computer on which TeleService is installed and the automation system. No modem is required.

The figure below shows the configuration of the TS Adapter MPI with a direct connection.

![Establishing the direct connection for TS Adapter MPI](images/28958603147_DV_resource.Stream@PNG-en-US.png)

#### Operating a TS adapter MPI in modem connection mode

##### Introduction to the modem connection with TS Adapter MPI

This configuration allows you to dial into a remote system. To do this, you establish a remote connection to a remote system using TeleService on a telephone network. Via the established modem connection you can then process the selected plant as usual with the TIA Portal.

##### Establishing a modem connection with TS Adapter MPI

This connection between the programming device or PC on which TeleService is installed and the automation system in which the TS Adapter MPI is inserted in the MPI/DP interface is made through a modem route.

The configuration therefore includes the programming device or PC via the telephone network and the TS Adapter MPI on the MPI/DP interface of the automation system.

The figure below shows the structure of the modem connection.

![Establishing a modem connection with TS Adapter MPI](images/40648379275_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> **Parallel operation between direct and modem connection**
>
> The TS Adapter II has two connections for communication with PG/PC, both of which can be connected at the same time. At the same time, connect the USB interface with the PG/PC and the modem interface with the telephone network.
>
> In this configuration you can either use the direct or the modem connection.
>
> A parallel operation is **not** possible!

#### TS adapter MPI configuration options

##### Useful information on configuring the TS Adapter MPI

The TS Adapter MPI can be configured in both direct connection mode and via an existing remote connection.

The following parameter assignment options are available:

- [Reconfiguration](#configuring-ts-adapter-mpi)
- [Restoring default parameter assignment](#restoring-default-parameter-assignment-for-ts-adapter-mpi)
- [Importing adapter parameters](#importing-adapter-parameters)
- [Exporting adapter parameters](#exporting-adapter-parameters)
- [Setting up access protection](#setting-up-access-protection-and-callback-number-for-the-ts-adapter)

##### Parameter assignment

Configure your TS Adapter in accordance with the documentation supplied with the TS Adapter. It will detail the exact procedure for parameter assignment.

> **Note**
>
> **Please note the following when configuring the TS Adapter MPI**
>
> - If you change the current parameter settings when there is an established remote connection, there is a risk it will not subsequently be possible to establish a modem connection with the modified parameters. The TS Adapter MPI can in this case only be configured in direct connection mode.
> - This means that either parameter assignment must be carried out with a programming device/personal computer at the plant location or the TS Adapter MPI must be brought to the location of the local programming device/personal computer in order to be configured.

##### Positive acknowledgement

During parameter assignment, the data is written to the non-volatile memory of the TS Adapter MPI. The parameter assignment process is not acknowledged positively until all precautions have been taken to ensure that parameter changes have been carried out correctly and will thus survive a power failure.

##### Changes become effective for the TS Adapter MPI as follows:

- The serial parameters, the modem parameters and the parameters for access protection are activated once the remote connection has been terminated.
- The modified network parameters are activated immediately.

#### Configuring TS adapter MPI

##### Introduction

The TS Adapter MPI can be configured in both direct connection mode and via an existing remote connection in modem connection mode.

The following describes the method for assigning parameters.

##### Requirement

A TS Adapter MPI is connected to your computer and the folder "TS Adapter" is displayed in the project tree under "Online access".

##### Procedure

To assign the parameters for the TS Adapter MPI im Direktanschluss , follow these steps:

1. Double-click the "Online access" folder in the project tree.
2. Open the required folder:

   - The "TS Adapter" folder for a direct connection.
   - For an existing remote connection, the "TeleService" folder followed by the folder with the required system name.
3. Select the command "Assign TS Adapter MPI parameters". The "Assign TS Adapter MPI parameters" dialog opens.
4. Set the required parameters in the individual tabs of the dialog.
5. Confirm your entries with "OK".

##### Result

The configured parameters are saved in the non-volatile memory of the TS Adapter MPI. Parameter assignment is then complete.

#### Restoring default parameter assignment for TS adapter MPI

##### Introduction

You can restore the default, factory state parameters of the TS Adapter MPI.

##### Requirement

A TS Adapter MPI is connected to your computer and is displayed in the project tree under "Online access" in the "TeleService" folder.

##### Procedure

To restore the default parameter assignment for the TS Adapter MPI, follow the steps below:

1. Open the "TeleService" folder in project tree.
2. Double-click the "TS Adapter MPI" folder.
3. Select the command "Assign TS Adapter MPI parameters". The "Assign TS Adapter MPI parameters" dialog opens.
4. Click the "Reset" button under "General".
5. Confirm your entries with "OK".

##### Result

The TS Adapter MPI default parameters set on delivery are restored.

---

**See also**

[TS adapter MPI configuration options](#ts-adapter-mpi-configuration-options)

#### Exporting adapter parameters

##### Introduction

You can export the configuration of a TS Adapter MPI to an external file. The configuration saved in this file can be imported in turn into any number of TS Adapter MPI.

This can for example be useful if you want to assign identical parameters to multipleTS Adapter MPI or if you want save, document or distribute the parameter set.

##### Requirement

A TS Adapter MPI is connected to your computer and is displayed in the project tree under "Online access" in the "TeleService" folder.

##### Procedure

To export the adapter parameters of a TS adapter MPI, follow the steps below:

1. Open the "TeleService" folder in project tree.
2. Double-click the "TS Adapter MPI" folder.
3. Select the command "Assign TS Adapter MPI parameters". The "Assign TS Adapter MPI parameters" dialog opens.
4. Click the "Export" button.
5. A window will open in which you can select the file to which you wish to export the configuration of the TS Adapter MPI.
6. Confirm with "Save".

##### Result

The parameters of the TS Adapter MPI are saved in the specified file (*.tap). The export of the adapter parameters is now complete.

#### Importing adapter parameters

##### Introduction

You can import the configuration of a TS Adapter MPI from a previously created export file (*.tap).

The configuration saved in this file can be imported into any number of TS Adapter. This can for example be useful if you want to assign identical parameters to multiple TS Adapter MPI.

You can import parameters locally in direct connection mode or via an existing remote connection in modem connection mode.

The TS Adapter takes on the parameters from the selected export file and continues working with these settings. All settings made up to this point that have not been saved in an export file are lost.

Before importing the file, back up the current configuration in an export file. You can restore the configuration if necessary.

##### Requirement

- A TS Adapter MPI is connected to your computer and is displayed in the project tree under "Online access" in the "TeleService" folder.

##### Procedure

To import the adapter parameters of a TS Adapter MPI:

1. Open the "TeleService" folder in project tree.
2. Double-click the "TS Adapter MPI" folder.
3. Select the command "Assign TS Adapter MPI parameters". The "Assign TS Adapter MPI parameters" dialog opens.
4. Click the "Import" button.
5. A dialog will open in which you can select the file to which you wish to import the configuration of the TS Adapter MPI.
6. Confirm the next dialog with "Yes".

##### Result

The parameters selected are saved in the non-volatile memory of the TS Adapter MPI. Adapter parameter import is then complete.

### TS adapter IE

This section contains information on the following topics:

- [Short description of the TS adapter IE](#short-description-of-the-ts-adapter-ie)
- [How the TS adapter IE works](#how-the-ts-adapter-ie-works)
- [Connection Types](#connection-types)
- [TS Adapter IE parameter assignment options](#ts-adapter-ie-parameter-assignment-options)
- [Parameter assignment for TS Adapter IE](#parameter-assignment-for-ts-adapter-ie)

#### Short description of the TS adapter IE

##### TS Adapter IE

The designation "TS Adapter IE" is a collective term for allTS Adapter with an Ethernet port.

The TS Adapter IE comes in the following versions:

- as TS Adapter IE Standard
- as TS Adapter IE Basic

The tables below provide a short description of the functionalities. For detailed information on your TS Adapter, please refer to the documentation supplied with it.

TS Adapter IE Standard:

Direct connection by means of Industrial Ethernet (IE). Firmware update possible. Modem integrated or external. The TS Adapter IE cannot automatically switch between modems like the TS Adapter II. Parameters are assigned via a Web interface.

**There are 2 variants:**

- With internal analog modem. An external modem can also be connected to the RS232 port.

- With internal ISDN adapter. An external modem can also be connected to the RS232 port.

TS Adapter IE Basic:

Direct connection by means of Industrial Ethernet (IE). Firmware update possible. Plug-in modules. Parameters are assigned via a Web interface.

**There are 4 variants:**

- TS Adapter IE Basic MODEM:  
  Basic device TS Adapter IE Basic with TS Module MODEM for operation on the analog telephone network.

- TS Adapter IE Basic ISDN:  
  Basic device TS Adapter IE Basic with TS Module ISDN for operation on ISDN telephone systems.

- TS Adapter IE Basic GSM:  
  Basic device TS Adapter IE Basic with TS Module GSM for operation on the GSM radio network.

- TS Adapter IE Basic RS232:  
  Basic device TS Adapter IE Basic with TS Module RS232 for connecting an external modem.

##### Use of the designation "TS Adapter"

"TS Adapter" is used in the TeleService online help as a general designation for all versions. The relevant product designation is listed beside information which only applies to a specific version of a TS Adapter, e.g. "TS Adapter I", "TS Adapter II", "TS Adapter IE Standard" or "TS Adapter IE Basic".

#### How the TS adapter IE works

##### How the TS Adapter IE works

The TS Adapter IE connects the telephone network or the serial port of a modem with the Industrial Ethernet of your automation system.

The TS Adapter IE has a non-volatile memory. Parameters for the following functions are stored in this memory:

- The mode of the modem used
- The serial port to the modem
- Access protection

##### Default parameter assignment

The TS Adapter IE comes with default parameter assignment. The parameters can be set and saved to the non-volatile memory of the TS adapter in a parameter assignment session.

> **Note**
>
> For more detailed information on the configuration of your TS Adapter, please refer to the documentation supplied with it.

#### Connection Types

##### Connection types of the TS Adapter IE Basic

The following diagrams show the connection types possible with the TS Adapter IE Basic.

##### Direct connection

In the direct connection to the PG/PC, you can set the TS Adapter IE Basic through Ethernet.

> **Note**
>
> The operation of the TS Adapter IE Basic without a TS module is not permitted.

![Direct connection](images/67498643083_DV_resource.Stream@PNG-de-DE.png)

Direct connection

##### Connection to the telephone network

In order to have a direct connection to the telephone network, you must connect the TS Adapter IE Basic together with one of the following TS modules:

- TS Module Modem
- TS Module ISDN

  ![Direct connection to the telephone network](images/28958679179_DV_resource.Stream@PNG-en-US.png)

  Direct connection to the telephone network

More information about the TS modules can be found in the *TS Adapter modular* manual.

##### Connection to the GSM network

In order to connect to the GSM network, you must operate the TS Adapter IE Basic together with this TS module:

- TS Module GSM

  ![Connection to the GSM network](images/28958731147_DV_resource.Stream@PNG-en-US.png)

  Connection to the GSM network

More information about the TS modules can be found in the *TS Adapter modular* manual.

##### Connection to the telephone network through an external modem

For the connection to an external modem, you must operate the TS Adapter IE Basic together with this module:

- TS Module RS232

  ![Connection to an external modem](images/28958711563_DV_resource.Stream@PNG-en-US.png)

  Connection to an external modem

More information about the TS modules can be found in the *TS Adapter modular* manual.

#### TS Adapter IE parameter assignment options

##### Useful information for configuring the TS Adapter IE

The TS Adapter IE is configured via a Web interface.

Web help associated with the parameter assignment interface is made available for the configuring the TS Adapter IE.

The following parameter assignment options are available:

- Reconfiguration
- Restoring default parameter assignment
- Importing adapter parameters
- Exporting adapter parameters

> **Note**
>
> **Parameter assignment**
>
> Configure your TS Adapter in accordance with the documentation supplied with the TS Adapter. It will detail the exact procedure for parameter assignments.

#### Parameter assignment for TS Adapter IE

##### Introduction

The TS Adapter IE can be configured in both direct connection mode and via an existing remote connection in modem connection mode.

Both parameter assignment options are described below.

Specific details for assigning parameters of the TS Adapter IE can be obtained from the TS Adapter IE documentation.

##### Parameter assignment of the TS Adapter IE in direct connection

##### Requirement

There is a LAN connection to your TS Adapter IE.

The TS Adapter IE Basic is connected to the power supply.

##### Procedure

To assign the parameters for the TS Adapter IE , follow these steps:

1. In the project tree of the TIA Portal, open the "Online access" folder.
2. Double-click on the Ethernet port of your computer.
3. Double-click on the "Display accessible nodes" command. The TS Adapter IE is then displayed.
4. Double-click on the &lt;TS Adapter IE&gt; folder and then on "Online and diagnostic", and assign the desired IP address to the TS Adapter IE in the following dialogs. Please note that the IP address of the PG/PC interface card is located in the same subnet as the IP address that you issue for the TS Adapter IE.
5. Update the view in the project tree for the "Accessible nodes", so that the TS Adapter IE is displayed with the newly allocated IP address.
6. Open the folder &lt;TS Adapter IE&gt; in the device list.
7. Double-click the command "Assign TS Adapter IE parameters". The allocated web interface opens for assigning the parameters of the TS Adapter IE.
8. Complete the "logon" for the web interface.
9. Set the required parameters in the individual tabs of the dialog.
10. Confirm your entries with "Save settings".

##### Result

The configured parameters are saved in the non-volatile memory of the TS Adapter IE. Parameter assignment is then complete.

##### Parameter assignment of the TS Adapter IE using a remote connection

##### Requirement

There is an established remote connection to a TS Adapter IE .

##### Procedure

1. In the project tree of the TIA Portal, open the "Online access" folder.
2. Open the "TeleService" folder followed by the required system folder.
3. Double-click the command "Assign TS Adapter IE parameters". The associated web interface for assignment of the TS Adapter IE parameters opens. The "logon" for the web interface takes place automatically with the login data of the remote connection.
4. Set the required parameters in the individual tabs of the dialog.
5. Confirm your entries with "Save settings".

##### Result

The configured parameters are saved in the non-volatile memory of the TS Adapter IE. Parameter assignment is then complete.

### Establishing a dial-up connection to a remote system

This section contains information on the following topics:

- [Establishing a dial-up connection](#establishing-a-dial-up-connection)
- [Terminating a dial-up connection](#terminating-a-dial-up-connection)

#### Establishing a dial-up connection

##### Introduction to establishing a remote dial-up connection

A dial-up connection is established when you use TeleService to dial into a remote system via a telephone network. The programming device/personal computer is connected to the telephone network with TeleService via a modem. At the other end, the automation system is connected to the telephone line via a configured TS Adapter and a modem.

##### Requirements

A local modem is installed and configured.

The TS Adapter is located in the remote system.

A remote modem is installed and parameters have been assigned.

##### Proceed as follows:

1. In the project tree of the TIA Portal, click the "Online access" folder.
2. Click on the "TeleService" folder it contains.
3. Double-click the "Set up/close remote connection" entry. The "Set up remote connection to the remote system" dialog opens.
4. In the "Adapter type" drop-down list, select the adapter type used.
5. Under "Connection type", select "Dial-up connection".
6. Select the modem you are using under "Local settings".
7. Enter the phone number to be dialed in the appropriate box or open the phone book by clicking on the button behind it and take the desired phone number from the phone book.
8. Enter your user name and the corresponding password.
9. If you want a "Connection setup with callback", select the appropriate option button.
10. Click the "Connect" button to establish the required remote connection. This button only becomes active when you have entered all the parameters needed to establish a remote connection. Any remote connection is displayed under "Status".

##### Result

The dial-up connection to the desired system is established.

The dialog closes as soon as the dial-up connection is established. The following message appears in the status bar of the TIA Portal: "Remote connection is up". You can now use the remote connection with the TIA Portal and communicate with the automation system.

##### Connection cannot be established

If the connection cannot be established, try to find the cause using the "Notes on troubleshooting".

##### Terminating the connection

Once you have finished editing the remote system, exit the remote connection in the project tree by double-clicking on the entry "Establish/disconnect remote connection".

By exiting the TIA Portal, you are also terminating the remote connection.

#### Terminating a dial-up connection

##### Terminating an active dial-up connection

> **Note**
>
> **Terminating the dial-up connection**
>
> You should go offline in the TIA Portal before you terminate the remote connection.

##### Proceed as follows:

1. Double-click the "Set up/close remote connection" entry in the TIA Portal.
2. Confirm the prompt in the dialog that follows with "Yes".

##### Result

The connection is terminated.

## Remote VPN connections

This section contains information on the following topics:

- [Basics for establishing a VPN connection](#basics-for-establishing-a-vpn-connection)
- [Basics of CA certificates](#basics-of-ca-certificates)
- [Installing CA certificates for VPN connections](#installing-ca-certificates-for-vpn-connections)
- [Deleting CA certificates for VPN connections](#deleting-ca-certificates-for-vpn-connections)
- [Establishing a VPN connection to a remote system](#establishing-a-vpn-connection-to-a-remote-system)
- [TS Adapter IE Advanced](#ts-adapter-ie-advanced)

### Basics for establishing a VPN connection

#### Using a TS Adapter IE Advanced for VPN connections

A TS Adapter IE Advanced is required to establish a VPN connection using TeleService.

#### VPN definition

VPN stands for "Virtual Private Network". This is a private network of computers based on a public network infrastructure.

VPN is used to create a connection that is as secure as possible between devices in a private network at different locations and the gateway of another network.

A VPN device has direct access to the gateway in the other network over an encrypted connection.

#### VPN connections

When a VPN connection is established with TeleService, a CA certificate and a unique fingerprint generated from it are used for the unique identification of the TS Adapter IE Advanced. The VPN connection allows a communication that is secure from tapping and manipulation between the remote PC and the TS Adapter.

If you want to establish a VPN connection to multiple remote networks, you will require a separate TS Adapter IE Advanced as an interface for each network. The networks connected by the TS Adapter can used identical IP addresses internally. Only the external IP addresses (WAN) of the TS Adapters need to be different.

Only one VPN connection to a TS Adapter is possible at any one time.

> **Note**
>
> **Authentication**
>
> Please not that the CA certificate exclusively authenticates the TS Adapter IE Advanced.
>
> As in the case of dial-up connections, users are authenticated via the login (user name and password).
>
> Therefore, use only a secure password for the login.

#### See also

- [Establishing VPN connections](#establishing-vpn-connections)
- [Terminating VPN connections](#terminating-vpn-connections)

### Basics of CA certificates

#### Introduction

To establish a secure VPN connection with TeleService, you need to generate a CA certificate with a unique fingerprint when you configure the TS Adapter IE Advanced.

You can install this CA certificate on every PC that should have access to the TS adapter IE advanced.

- Using the automatic download in the TeleService connection dialog, by entering the fingerprint for the CA certificate
- Manually by using the Microsoft® Management Console.

#### Definition of CA certificate

A CA certificate is a digital certificate issued by a "certificate authority" or "certification authority", hereinafter referred to as "CA". In the case of the TS Adapter IE Advanced, self-signed certificates are used; the certification authority in this case is the TS Adapter IE Advanced itself.

Certificates for "SSTP" (Secure Socket Tunneling Protocol) and "HTTPS" (Hypertext Transfer Protocol Secure) are derived from the CA certificate.

CA certificates contain a "key" and additional information used for authentication and for encrypting and decrypting confidential data. Additional information includes the validity period, references to certificate revocation lists, etc. which are included in the certificate by the CA.

#### Using CA certificates with TeleService

A CA certificate with a unique fingerprint is generated by the TS Adapter to uniquely identify the TS Adapter IE Advanced as connection partner for the remote PC.

This CA certificate must be saved in the Windows certificate store of your programming device/PC before you can establish a VPN connection. When you access the Web server using a direct connection, a security warning will appear if no CA certificate exists. In such cases, however, you can choose to ignore the warning and allow the connection.

> **Note**
>
> **Handling CA certificates**
>
> Specialist knowledge of the operating system is required for handling CA certificates. CA certificates should only be managed by trained personnel!
>
> You require administrator rights to manage CA certificates.

#### Definition of fingerprint

The fingerprint is a 20-byte hexadecimal expression. It provides a unique value for a CA certificate and is used to identify a specific CA certificate.

A fingerprint is calculated dynamically using the SHA-1 algorithm and is not physically contained in the CA certificate.

#### Use of fingerprints with TeleService

The CA certificate is used to uniquely identify the TS Adapter IE Advanced as connection partner. A unique 20-byte fingerprint of this certificate is generated each time a CA certificate is generated by the TS Adapter IE Advanced. It is calculated automatically by the TS Adapter IE Advanced when the certificate is generated. Each certificate has a specific, unique fingerprint. This fingerprint must be transferred securely to your computer, for example by phone or in an encrypted e-mail. You need to enter this fingerprint in the connection dialog when establishing a VPN connection with TeleService, unless the CA certificate is already saved on your PC in the Windows certificate store.

You will find the fingerprint for your TS Adapter IE Advanced in the web interface for the TS Adapter IE Advanced. To open the web interface, double-click the command "Assign TS Adapter IE parameters" in the device list in the TIA Portal. Perform the Web login to view the fingerprint in the "Security &gt; Certificates" tab.

#### CA certificate download during connection establishment

When the connection is established, TeleService checks whether a suitable CA certificate is installed in the Windows certificate store of your programming device/PC. If an appropriate certificate is found, the VPN connection is established as an SSTP connection (Secure Socket Tunneling Protocol).

If no appropriate CA certificate is found, the CA certificate is first loaded by the corresponding TS Adapter IE Advanced. The TS Adapter IE Advanced is called by the remote address entered in the connection dialog. If this download of the CA certificate is successful, the fingerprint of the downloaded CA certificate is calculated and compared with the fingerprint entered in the connection dialog. If the two fingerprints match, a dialog opens and you are prompted to save the CA certificate in the Windows certificate store of your programming device/PC. You require administrator rights to save the CA certificate.

The VPN connection is then established.

#### See also

- [Installing CA certificates for VPN connections](#installing-ca-certificates-for-vpn-connections)
- [Deleting CA certificates for VPN connections](#deleting-ca-certificates-for-vpn-connections)

### Installing CA certificates for VPN connections

#### Installing CA certificates

To establish a secure VPN connection between your programming device/PC and a remote system with TeleService, you require a valid CA certificate generated by the TS Adapter IE Advanced. This must be saved in the Windows certificate store of your programming device/PC.

A CA certificate can be installed manually or using an automatic download.

CA certificates are managed with the Microsoft® Management Console.

> **Note**
>
> **Handling CA certificates**
>
> Specialist knowledge of the operating system is required for handling CA certificates. CA certificates should only be managed by trained personnel!
>
> You require administrator rights to manage CA certificates!

#### Requirement

A CA certificate has yet to be installed in the Windows certificate store on your computer.

#### Installing CA certificates using the automatic download

Proceed as follows:

1. Log on to the system as administrator.
2. Transfer the fingerprint for the CA certificate from the TS Adapter IE Advanced to your computer using a "secure route", for example by phone or in an encrypted e-mail.

   You will find the fingerprint for your TS Adapter IE Advanced in the web interface for the TS Adapter IE Advanced. To open the web interface, double-click the command "Assign TS Adapter IE parameters" in the device list in the TIA Portal. Perform the Web login to view the fingerprint in the "Security &gt; Certificates" tab.
3. In the project tree of the TIA Portal, click the "Online access" folder.
4. Click on the "TeleService" folder it contains.
5. Double-click the "Set up/close remote connection" entry. The "Set up remote connection to the remote system" dialog opens.
6. Select the "TS Adapter IE" as Adapter type from the drop-down list.
7. Under "Connection type", select "VPN".
8. Enter the IP address / DNS name for the TS Adapter IE Advanced to be contacted in the relevant field. Alternatively, you can apply any existing data from the phone book by clicking the corresponding button.
9. Enter your user name and the corresponding password.
10. Copy the fingerprint displayed in the web interface for the TS Adapter IE Advanced to the "Fingerprint" column.
11. Click the "Connect" button to establish the required remote connection. This button only becomes active when you have entered all the parameters needed to establish a remote connection.
12. No valid CA certificate is found, because no CA certificate has been installed on your PC yet.

    A "normal" connection (not a VPN connection) is therefore established and the certificate required is downloaded from the TS Adapter IE Advanced to the working memory of your computer. The fingerprint is then calculated (SHA-1 algorithm) and compared with the fingerprint entered in the connection dialog. If the two fingerprints match, a dialog opens and you are prompted to save the CA certificate in the Windows certificate store of your programming device/PC.
13. Confirm that you want to save the CA certificate.

> **Note**
>
> **Restart of STEP 7 required after renewal of CA certificate**
>
> STEP 7 must be restarted after renewal of the CA certificate on the TS Adapter IE Advanced before the remote connection can be established with the help of the new fingerprint. Otherwise, it may not be possible to store the CA certificate in the Windows certificate memory and the remote connection cannot be established.

#### Result

The VPN connection to the required TS Adapter IE Advanced is established. The dialog closes once the connection is established.

#### Manual installation of CA certificates

Proceed as follows:

1. Log on to the system as administrator.
2. Open the Windows Certificate Manager on your programming device/PC with the Microsoft® Management Console.

   Click "Start", enter "mmc" in the search field and press ENTER.

   The console will open.
3. Open the "File" menu and click "Add/remove snap-in...".

   The "Add/remove snap-in..." dialog will open.
4. Double-click "Certificates" in the "Snap-in" list and select "Computer account" in the dialog that opens.
5. Select "Local computer" in the next dialog and click "Finish" and "OK".

   The console root opens and the "Certificates (local computer)" folder appears.
6. Open the displayed "Certificates (local computer)" folder and click "Trusted certification authorities".
7. Click the "Certificates " folder and use the shortcut menu to access the command "All tasks" &gt; "Import...".
8. Note the information that appears in the "Certificate - Import wizard" dialog and click "Next".
9. In the dialog that follows, click "Browse ..." and select the required CA certificate.
10. Then click "Next" twice and subsequently "Finish" to install the CA certificate.

#### Result

The selected CA certificate is installed at the specified location in the Windows certificate memory.

> **Note**
>
> **Additional information ...**
>
> ... on installing CA certificates can be found using the "F1" button in the online help of your operating system.

### Deleting CA certificates for VPN connections

#### Deleting CA certificates

Proceed as follows:

1. Log on to the system as administrator.
2. Open the Windows Certificate Manager on your programming device/PC with the Microsoft® Management Console.

   Click "Start", enter "mmc" in the search field and press the ENTER KEY.

   The console will open.
3. Open the "File" menu and click "Add/remove snap-in...".

   The snap-in selection dialog will open.
4. Double-click "Certificates" in the "Snap-in" list and select "Computer account" in the dialog that opens.
5. Select "Local computer" in the next dialog and click "Finish" and "OK".

   The console root opens and the "Certificates (local computer)" folder appears.
6. Open the displayed "Certificates (local computer)" folder and click "Trusted certification authorities".
7. Open the "Certificates" folder, select the required CA certificate and click "Delete" in the shortcut menu.
8. Confirm the next prompt with "Yes".

#### Result

The selected CA certificate is deleted from the list of available certificates.

### Establishing a VPN connection to a remote system

This section contains information on the following topics:

- [Establishing VPN connections](#establishing-vpn-connections)
- [Terminating VPN connections](#terminating-vpn-connections)

#### Establishing VPN connections

##### Introduction to establishing VPN connections

A VPN connection is established when you use TeleService to connect to a remote system over the Internet.

Your programming device/PC with installed TIA Portal is connected to the Internet at one end for this. At the other end, the automation system is connected to the Internet via the WAN (Wide Area Network) interface of the configured TS Adapter IE Advanced.

##### Requirement

Your programming device/PC is connected to the Internet.

There is a TS Adapter IE Advanced in the remote system.

The TS Adapter IE Advanced has been configured and is connected to the Internet.

The CA certificate required for identifying the TS Adapter has been generated and installed in the Windows certificate store of your programming device/PC.

##### Proceed as follows:

1. In the project tree of the TIA Portal, click the "Online access" folder.
2. Click on the "TeleService" folder it contains.
3. Double-click the "Set up/close remote connection" entry. The "Set up remote connection to the remote system" dialog opens.
4. Select the "TS Adapter IE Advanced" as "Adapter type" from the drop-down list.
5. Enter "VPN" as "connection type".
6. Enter the IP address / DNS name for the TS Adapter IE Advanced to be contacted in the relevant field. Alternatively, you can apply any existing data from the phone book by clicking the corresponding button.
7. Enter your user name and the corresponding password.
8. Click the "Establish" button to establish the required VPN connection. This button only becomes active once you have entered all the parameters needed for establishing the remote connection.

##### Result

The VPN connection to the required system is established. "Status" indicates the progress in establishing the connection. The dialog closes once the VPN connection is established. The following message appears in the status bar of the TIA Portal: "Remote connection is up". You can now use the remote connection with the TIA Portal and communicate with the automation system.

##### Connection cannot be established

If the connection cannot be established, try to find the cause using the "Notes on troubleshooting".

> **Note**
>
> **Rules for IP addresses**
>
> - Only use IP addresses which have not yet been assigned in the plant network.
> - If the IP address configured for the TS Adapter IE Advanced has already been assigned in the system network, the TS Adapter IE Advanced can only be addressed by its MAC address.

---

**See also**

[Installing CA certificates for VPN connections](#installing-ca-certificates-for-vpn-connections)

#### Terminating VPN connections

##### Terminating an active VPN connection

> **Note**
>
> **Terminating the VPN connection**
>
> You should go offline in the TIA Portal before you terminate the VPN connection.

##### Proceed as follows:

1. Double-click the "Set up/close remote connection" entry in the TIA Portal.
2. Confirm the prompt in the dialog that follows with "Yes".

##### Result

The VPN connection is terminated.

### TS Adapter IE Advanced

This section contains information on the following topics:

- [Short description of the TS Adapter IE Advanced](#short-description-of-the-ts-adapter-ie-advanced)
- [Connection types](#connection-types-1)
- [TS Adapter IE Advanced parameter assignment options](#ts-adapter-ie-advanced-parameter-assignment-options)
- [Parameter assignment for TS Adapter IE Advanced](#parameter-assignment-for-ts-adapter-ie-advanced)

#### Short description of the TS Adapter IE Advanced

##### TS Adapter IE Advanced

The TS Adapter IE Advanced has the following properties:

- Direct connection over Industrial Ethernet (IE), 2 ports
- WAN (Wide Area Network) interface for VPN connections
- Firmware update supported
- Plug-in modules
- Parameters are assigned via a Web interface.

> **Note**
>
> **Further information on the TS Adapter IE Advanced**
>
> For detailed information on your TS Adapter, please refer to the documentation supplied with your TS Adapter.

#### Connection types

##### TS Adapter IE Advanced connection types

The following diagrams show the types of connection possible with the TS Adapter IE Advanced.

##### Direct connection

In the direct connection to the programming device/PC, you can set the TS Adapter IE Advanced parameters over the Ethernet.

![TS Adapter IE Advanced - direct connection](images/52622940299_DV_resource.Stream@PNG-de-DE.png)

TS Adapter IE Advanced - direct connection

##### Connection to the Internet (DSL modem/router)

In order to connect to the Internet, you must operate the DSL modem/router at the WAN connection of the TS Adapter IE Advanced.

![TS Adapter IE Advanced - connection to the Internet](images/54560071307_DV_resource.Stream@PNG-en-US.png)

TS Adapter IE Advanced - connection to the Internet

##### Connection to the company network (Intranet)

In order to connect to the Intranet, you must operate plant network (Ethernet) at one of the two LAN connections of the TS Adapter IE Advanced.

![TS Adapter IE Advanced - connection to company network (Intranet)](images/52622972555_DV_resource.Stream@PNG-de-DE.png)

TS Adapter IE Advanced - connection to company network (Intranet)

##### Additional information

For more detailed information on the TS modules, please refer to the documentation supplied with your TS Adapter IE Advanced.

#### TS Adapter IE Advanced parameter assignment options

##### Basics on configuring the TS Adapter IE

The TS Adapter IE Advanced is configured via a Web interface.

Web help in the Web interface is available for assigning TS Adapter IE Advanced parameters.

Parameter assignment options include:

- Reconfiguration
- Restoring default parameter assignment
- Importing adapter parameters
- Exporting adapter parameters

> **Note**
>
> **Parameter assignment**
>
> Configure your TS Adapter IE Advanced in accordance with the documentation supplied. This details the exact procedure for parameter assignment.

#### Parameter assignment for TS Adapter IE Advanced

##### Introduction

The TS Adapter IE Advanced can be configured in both direct connection mode and via an existing remote connection.

Both parameter assignment options are described below.

Specific details on assigning parameters for the TS Adapter IE Advanced are available in the TS Adapter IE Advanced documentation.

##### Assigning parameters for the TS Adapter IE Advanced in direct connection

##### Requirement

There is a LAN connection to your TS Adapter IE Advanced.

##### Procedure

To assign parameters for the TS Adapter IE Advanced, follow the steps below:

1. In the project tree of the TIA Portal, open the "Online access" folder.
2. Double-click on the Ethernet port of your computer.
3. Double-click on the "Display accessible nodes" command. The TS Adapter IE Advanced is then displayed.
4. Double-click on the "TS Adapter IE Advanced" folder and then on "Online and diagnostics", and assign the desired IP address to the TS Adapter in the dialogs that follow. Please note that the IP address of the programming device/PC interface card must be located in the same subnet as the IP address that you assign for the TS Adapter IE Advanced.
5. Update the view in the project tree for the "Accessible nodes", so that the TS Adapter IE Advanced is displayed with the newly assigned IP address.
6. Open the folder "TS Adapter IE Advanced" in the device list.
7. Double-click the command "Assign TS Adapter IE parameters". The corresponding web interface opens for assigning TS Adapter parameters.
8. Complete the "logon" for the web interface.
9. Set the required parameters in the individual tabs of the dialog.
10. Confirm your entries with "Save settings".

##### Result

The configured parameters are saved in the non-volatile memory of the TS Adapter IE Advanced. Parameter assignment is then complete.

##### Assigning parameters for the TS Adapter IE Advanced using a remote connection

##### Requirement

There is an established remote connection to a TS Adapter IE Advanced..

##### Procedure

1. In the project tree of the TIA Portal, open the "Online access" folder.
2. Open the "TeleService" folder followed by the required plant folder.
3. Double-click the command "Assign TS Adapter IE parameters". The associated web interface for assignment of the TS Adapter IE parameters opens. The "logon" for the web interface takes place automatically with the login data of the remote connection.
4. Set the required parameters in the individual tabs of the dialog.
5. Confirm your entries with "Save settings".

##### Result

The configured parameters are saved in the non-volatile memory of the TS Adapter IE Advanced. Parameter assignment is then complete.

## CPU controlled TeleService remote connections

This section contains information on the following topics:

- [Overview of CPU controlled remote connections](#overview-of-cpu-controlled-remote-connections)
- [Establishing a connection from and to remote systens (PG-AS-remote coupling)](#establishing-a-connection-from-and-to-remote-systens-pg-as-remote-coupling)
- [Data exchange between remote systems (AS-AS-remote coupling)](#data-exchange-between-remote-systems-as-as-remote-coupling)
- [Send SMS from a system](#send-sms-from-a-system)
- [Send an email from a system](#send-an-email-from-a-system)

### Overview of CPU controlled remote connections

#### Introduction

TeleService offers a range of options for establishing remote connections; these differ according to the CPU used. The initiative for establishing a connection starts from the CPU. The communication instructions given below are used for the individual connection options.

#### Connection establishment with S7-300/400 CPUs

The following communication instructions are available:

- Communication instruction "PG_DIAL": Establish remote connection to programming device/PC
- Communication instruction "SMS_SEND": Send text message (SMS)
- Communication instruction "AS_DIAL": Establish remote connection to AS
- Communication instruction "AS_MAIL": Transfer email

#### Connection establishment with S7-1200 CPUs

The following communication instruction is available:

- Communication instruction "TM_MAIL": Transfer email

#### Connection establishment with S7-1500 CPUs

The following communication instruction is available:

- Communication instruction "TMAIL_C": Transfer email

> **Note**
>
> **Description of individual communication instructions**
>
> More detailed information on the available communication instructions can be found in the information system of the TIA Portal in the "References &gt; Communication &gt; TeleService" directory.

---

**See also**

[TS Adapter IE parameter assignment options](#ts-adapter-ie-parameter-assignment-options)

### Establishing a connection from and to remote systens (PG-AS-remote coupling)

This section contains information on the following topics:

- [Remote plant access to a programming device/personal computer](#remote-plant-access-to-a-programming-devicepersonal-computer)
- [Requirements for establishing a connection](#requirements-for-establishing-a-connection)

#### Remote plant access to a programming device/personal computer

##### Introduction

You can establish a remote connection to and communicate with a remote system using the application TeleService and a TS Adapter MPI. The initiative for establishing the remote connection comes from the programming device/personal computer.

However, events which require rapid intervention often occur at a remote system. In such cases, the automation system can initiate a remote connection to a programming device/personal computer if an asynchronous event occurs.

The graphic below shows the components which are required for establishing a connection from a plant to a programming device/personal computer.

![How the "PG_DIAL" communications instruction works](images/28958807051_DV_resource.Stream@PNG-en-US.png)

How the "PG_DIAL" communications instruction works

#### Requirements for establishing a connection

##### Introduction

Certain hardware and software requirements must be fulfilled if a remote system is to establish a remote connection to a programming device/personal computer. These requirements are detailed below.

##### Hardware requirements:

The only hardware required for establishing a remote connection from a remote system to a programming device/personal computer is that needed for accessing the remote system from the programming device/personal computer.

Your user program calls the "PG_DIAL"  communication instruction to establish the connection. This can only be executed on an S7-300 or S7-400 CPU on which S7 basic communication is implemented.

A TS Adapter I , version 5.0 or later, or a TS Adapter II must be used.

##### Software requirements on the system side:

The "PG_DIAL" communication instruction is included in the scope of delivery of TeleService and is installed when the TIA Portal is installed. You will find the installed communications instructions in the task card of the block editor in the folder "Communication &gt; TeleService".

If a remote system is to establish a remote connection to a programming device/PC, the user program of the system must call the "PG_DIAL" communication instruction.

##### Software requirements on the programming device/PC side:

You require a software product on the programming device/PC which, with TeleService, waits for a call from a remote system, recognizes this call and informs your user program.

### Data exchange between remote systems (AS-AS-remote coupling)

This section contains information on the following topics:

- [AS-AS remote link basics](#as-as-remote-link-basics)
- [Hardware and software requirements for AS-AS remote link](#hardware-and-software-requirements-for-as-as-remote-link)

#### AS-AS remote link basics

##### Introduction

The AS-AS remote link allows two automation systems to exchange process data via the telephone network.

##### Requirement

Communication instruction "AS_DIAL" is available if you use a CPU from the S7-300/400 family.

##### Definition: Local and remote automation system

- The automation system from which the initiative to establish the remote connection originates is described as **local**.
- The automation system to which the remote connection is to be established is described as **remote**.

##### Data exchange over the AS-AS remote link

Data exchange is carried out using specific communication instructions for non-configured S7 connections. Use the communication instruction "AS_DIAL" to establish a remote connection to the automation system.

More detailed information on establishing the connection can be found in the information system in the directory "References &gt; Communication &gt; TeleService".

The following graphic shows the components required for establishing a connection from a local to a remote automation system.

![Data exchange over the AS-AS remote link](images/28958838539_DV_resource.Stream@PNG-en-US.png)

Data exchange over the AS-AS remote link

#### Hardware and software requirements for AS-AS remote link

##### Introduction

Certain hardware and software requirements must be fulfilled before a local automation system can establish a remote connection to a remote automation system. These requirements are detailed below.

##### Hardware requirements

The only hardware you need for transferring process data from a local to a remote automation system is that also needed for accessing the respective automation system from the programming device/personal computer.

To establish and terminate the remote connection, the user program of the TIA Portal of the local CPU calls a communication instruction. This communication instruction can be executed on an S7-300/400 CPU or a C7 CPU. The communication instruction requires S7 basic communication to be implemented on the CPU. The remote CPU must also support S7 basic communication.

A TS Adapter I, version V5.1 or later, or a TS Adapter II must be used.

##### Software requirements

The "AS_DIAL" communication instruction is included in the scope of delivery of TeleService. When installed, the instruction is integrated in the library of the TIA Portal in the task card of the Communication instructions folder under TeleService. In order to establish and terminate a remote connection to a remote automation system from a local automation system, the "AS_DIAL" communication instruction must be called in the user program of the TIA Portal on the local CPU.

![Hardware and software requirements for AS-AS remote link](images/28958870027_DV_resource.Stream@PNG-en-US.png)

Hardware and software requirements for AS-AS remote link

### Send SMS from a system

This section contains information on the following topics:

- [Requirements for sending an SMS](#requirements-for-sending-an-sms)

#### Requirements for sending an SMS

##### Introduction

Certain hardware and software requirements must be fulfilled before a system can send an SMS. These requirements are detailed below.

##### Hardware requirements

To send an SMS from a system, you will require a GSM wireless modem and a TS Adapter MPI.

A TS Adapter I, version V5.2 or later, or a TS Adapter II must be used.

##### Software requirements on the system side

The "SMS_SEND" communication instruction is included in the scope of delivery of TeleService. When installed, the instruction is integrated in the library of the TIA Portal in the task card of the Communication instructions folder under TeleService. If a system is to send an SMS, the user program of the system must call the "SMS_SEND" communication instruction.

![How the "SMS_SEND" communication instruction works](images/28958888715_DV_resource.Stream@PNG-en-US.png)

How the "SMS_SEND" communication instruction works

> **Note**
>
> You may be able to send an SMS not only to a cell phone but also to an email address or a fax device by using additional services offered by the cell phone service provider.

### Send an email from a system

This section contains information on the following topics:

- [Requirements for sending e-mails](#requirements-for-sending-e-mails)

#### Requirements for sending e-mails

##### Introduction

The following hardware and software requirements must be fulfilled if a system is to send an email:

##### Hardware requirements

You need a TS Adapter IE to send an email from a system and one of the CPUs listed below:

- a CPU 31x2 PN/DP as of firmware version V2.5
- a CPU 41x-3 PN/DP
- a CPU of the S7-1200 series
- a CPU of the S7-1500 series

##### Software requirements on the system side

Various communication instructions are included in the scope of delivery of TeleService depending on the CPU. When installed, they are integrated in the library of the TIA Portal in the task card of the Communication instructions folder under TeleService.

If a system is to send an email, the user program of the system must call the corresponding CPU-dependent communication instruction.

The following communication instructions are available for sending an email:

- S7-300/400 CPUs: Uses the communication instruction "AS_MAIL": Transfer email
- S7-1200 CPU V2.x and V3.x: Uses the communication instruction "TM_MAIL": Transfer email
- S7-1200 CPU &gt;V4.0: Uses the communication instruction "TMAIL_C": Transfer email
- S7-1500 CPUs: Uses the communication instruction "TMAIL_C": Transfer email

The respective communication instruction transfers an email from a CPU to a mail server by means of the Simple Mail Transfer Protocol (SMTP) with the "LOGIN" authentication method. The data is transferred unencrypted with this SMTP process.

The figure below shows an example with the "AS_MAIL" communication instruction:

![Software requirements on the system side](images/42332578955_DV_resource.Stream@PNG-en-US.png)

The "Use gateway/router" property must also be set for the Ethernet interface in the configuration of the CPU on which the "AS_MAIL" communication instruction runs. (available in the device configuration under Ethernet addresses and there under IP protocol)The IP address of the Ethernet interface of the TS Adapter IE is to be specified as "Address".

> **Note**
>
> You can find further information in the task card in the "Communication instructions" folder under TeleService.

## Notes on troubleshooting

This section contains information on the following topics:

- [General information on troubleshooting for modem problems](#general-information-on-troubleshooting-for-modem-problems)
- [Recording a log file for the modem](#recording-a-log-file-for-the-modem)
- [Dial-up connection to the TS Adapter is not established](#dial-up-connection-to-the-ts-adapter-is-not-established)
- [Dial-up connection from the TS Adapter is not established](#dial-up-connection-from-the-ts-adapter-is-not-established)
- [Modem connection is interrupted](#modem-connection-is-interrupted)
- [Checklist for troubleshooting the modem](#checklist-for-troubleshooting-the-modem)
- [Modem alarms](#modem-alarms)
- [Possible error messages with VPN connections](#possible-error-messages-with-vpn-connections)

### General information on troubleshooting for modem problems

#### Introduction

The information below should help you establish and eliminate the causes of any modem problems.

1. Enable "Record log file" for data traffic between PG/PC and modem. The entries in this file can provide valuable information for determining the cause of errors.
2. Switch on the loudspeaker on your local modem. Select a volume loud enough to be clearly heard.

   You can then hear whether:

   - there is a dial tone at the connection
   - the modem called is busy
   - the modem called accepts the call.

#### Common modem problems

Modem connection problems are among the most common modem problems:

- Modem connection is not established
- Modem connection is interrupted

The topics below contain tables detailing possible causes and providing information on eliminating the error in question.

---

**See also**

[Dial-up connection to the TS Adapter is not established](#dial-up-connection-to-the-ts-adapter-is-not-established)
  
[Dial-up connection from the TS Adapter is not established](#dial-up-connection-from-the-ts-adapter-is-not-established)
  
[Modem connection is interrupted](#modem-connection-is-interrupted)
  
[Modem alarms](#modem-alarms)
  
[Recording a log file for the modem](#recording-a-log-file-for-the-modem)

### Recording a log file for the modem

#### Introduction

It is advisable to record a log file as this makes it easier to find the causes of faults in a modem.

#### Procedure:

Proceed as follows:

1. Activate the properties dialog of the modem used via the "Phone and modem options" option in the Control Panel.
2. Check the settings of the "Log" option in the "Diagnostics" tab and, if necessary, change the log file settings so that the file is recorded.

#### Result:

Activity between the programming device/personal computer and the modem are entered in the log file. If there are problems establishing the connection, you can evaluate the data recorded in the log file to determine the cause of the error.

### Dial-up connection to the TS Adapter is not established

#### Dial-up connection to TS Adapter is not established

The table below sets out possible causes and how to eliminate them if no remote connection to the TS Adapter can be established.

| Possible cause | Check/Remedy |
| --- | --- |
| Cabling faulty | - Are all the connecting cables connected correctly? - Are the connectors loose? |
| Dial parameters for main telephone line and extension incorrectly set | - Do the properties and dial parameters of your modem match the phone connection to main phone line or extension? - Do not specify a dial-out code in the "Dial parameters" dialog if you operate your modem on a local loop (main telephone line).   The fields for the dial-out code for local calls and long-distance calls must be empty. |
| Dialing mode incorrectly set | - Is the correct dialing mode (tone/pulse) set in the dialog for the dial parameters of your modem? - Use a connected telephone to check the connection on which you want to operate the modem.   You should hear crackling noises on the telephone during pulse dialing and tones of varying pitches during tone dialing.   Set the corresponding dialing mode in the modem dial parameters. |
| Dial disable active | - The dial disable function is a country-specific modem property which, depending on the modem, becomes effective after one or more unsuccessful attempts to establish a connection. - If your modem still does not respond after several attempts to dial, the dial disable function may be active. Characters are still sent to the modem after the dial command but the modem does not start the dialing process. The driver receives a general error message. - Refer to the modem documentation for information on how the dial disable function is implemented for your modem. - Create a [log file](#recording-a-log-file-for-the-modem) (modemlog.txt) in which the activities between the programming device/personal computer and modem are recorded.   Then check whether the file contains an entry caused by dial disable (e.g. DELAYED). |
| Phone connection defective or busy | - Connect a phone and check whether a dial tone can be heard on this connection. - Any analog phone connected on the same connection must be hung up.   You cannot establish an additional modem connection on this connection if there is an existing phone connection. |
| Serial parameters set incorrectly | - Are the correct values entered in the "Settings" tab for modem properties (8 data bits, no parity, 1 stop bit)?   Is the correct COM interface set in the "General" tab for the modem properties? |
| Initialization string of the TS Adapter is not suitable for the modem. | - Familiarize yourself with the modem initialization string requirements and set the string accordingly.    [Procedure for configuring the TS Adapter IE](#how-the-ts-adapter-ie-works) |
| Settings for error correction between the modem at the TS Adapter and the modem at the PC/programming device are not compatible. | - Adapt the modem settings.    [Useful information on configuring the TS Adapter MPI](#ts-adapter-mpi-configuration-options)     [Restoring the default parameter assignment of a TS Adapter MPI](#restoring-default-parameter-assignment-for-ts-adapter-mpi)     [Procedure for configuring the TS Adapter IE](#configuring-ts-adapter-mpi) |

### Dial-up connection from the TS Adapter is not established

#### No callback from TS Adapter

The table below sets out possible causes and how to eliminate them if there is no callback from the TS Adapter.

| Possible cause | Check/Remedy |
| --- | --- |
| Errors in the location or call settings in the TS Adapter | Check the TS Adapter parameter assignment:  - Are the dialing mode and dial-out code set correctly for your phone connection? - Does the modem at the TS Adapter  support the characters configured for the dial-out code? - Is "Wait for dial tone before dialing" deactivated for an extension? |
| Initialization of modem insufficient | Check the string for modem initialization:  - The modem may require a further initialization in order to establish a remote connection. - Properties of the modem initialization string for the TS Adapter MPI |
| Callback number is incorrect | Check the configuration of the callback number you assigned. |

#### No call from TS Adapter MPI

The table below sets out possible causes and and how to remedy them if there is no call from the TS Adapter MPI.

| Possible cause | Check/Remedy |
| --- | --- |
| Phone number is incorrect | Is the required number being transferred to the communication instruction "PG_DIAL" ? |
| TS Adapter MPI  parameter assignment incorrect | Check the TS Adapter MPI parameter assignment:  - Are the dialing mode and dial-out code set correctly for your phone connection? - Does the modem at the TS Adapter MPI support the characters configured for the dial-out code? - Is "Wait for dial tone before dialing" deactivated for an extension? |

### Modem connection is interrupted

#### Modem connection is interrupted

The table below sets out possible causes and and how to remedy them if the modem connection is interrupted.

| Possible cause: | Check / Remedy: |
| --- | --- |
| Metering pulses in the line | Metering pulses will be generated if you have applied to the phone company for a metering clock. This may mean that the modem no longer recognizes the carrier signal and switches off.  - Set a longer waiting or switch-off time at the modem. - Have the metering pulse deactivated by the phone company. |
| Shielding | - Are the connection cables used shielded sufficiently? - Make sure that the modem cables do not run next to power cables and that they are as far as possible from power supply units and monitors. |
| Protocol timeout | - Set fixed monitoring times. |
| Automatic connection termination | - Deactivate the option that terminates an existing connection automatically after a specified time without data transfer ("Terminate after idle of ..."). |
| Data flow control deactivated | - Click on the "Extended" button in the "Settings" tab of the modem properties and activate the following options in the dialog displayed (if available and not yet set):   - Data flow control   - Hardware (RTS/CTS)   - Data compression   - Error control |
| Initialization string of the TS Adapter  is not suitable for the modem | - Set the modem initialization string in accordance with the following requirements.   See also: [TS Adapter IE parameter assignment options](#ts-adapter-ie-parameter-assignment-options) |

---

**See also**

[TS adapter MPI configuration options](#ts-adapter-mpi-configuration-options)

### Checklist for troubleshooting the modem

#### Introduction

The following list should help you establish the potential cause of any problems with the modem. The help topics below set out how and in which dialogs you define the relevant settings.

#### Modem connection cannot be established:

- Check the cabling and the connections.
- Check whether the correct dialing mode (tone/pulse) is set.
- If your modem does not react after several attempts to dial, a dial disable function may be active. Familiarize yourself with dial disable on your modem.
- Are you operating your modem on a main telephone line or on an extension line? Configure the properties and dialing parameters of the modem accordingly.
- Enable the log file option in the advanced properties. The next attempt to establish a connection will then be recorded in a file in the Windows directory.
- Ensure that the ISDN TAs used work with the same B and D channel protocol.

#### The modem connection is terminated:

- Metering pulses can have a negative affect on a connection. Have the pulses deactivated by your telephone company.
- Set fixed monitoring times.
- Deactivate the option that terminates an existing connection automatically after a specified time without data transfer (idle).
- Make sure that you have activated RTS/CTS for data flow control.

### Modem alarms

#### Information in the log file

The modem alarms are entered in a log file if you have activated the recording function.

The log file contains the following information:

| Alarm: | Possible cause: | Remedy: |
| --- | --- | --- |
| NO DIALTONE | A phone call may currently be being carried out on this line. | - Repeat the process once the phone call is over. |
| NO CARRIER | The device dialed is not ready, is not a modem or cannot establish a connection in the set operating mode. | - Check the numbers and the settings. |
| BUSY | The device dialed is busy. | - Try again later. |
| DELAYED: ... | Dial disable | - Refer to the modem documentation for information on how the dial disable function is implemented for your modem and if necessary remove it. |

### Possible error messages with VPN connections

#### VPN connection to TS Adapter IE Advanced is not established

The table below sets out possible errors and how to eliminate them if no VPN connection to the TS Adapter IE Advanced can be established.

| Possible errors | Check/Remedy |
| --- | --- |
| The error message "The webpage cannot be displayed" appears when the Web interface is accessed. | - Note: This problem occurs when the Windows certificate store contains a CA certificate with the same name as the CA certificate which has just been generated. - If a CA certificate for this TS adapter is already installed in the Windows certificate store and you have generated a new CA certificate on the TS adapter, remove the old CA certificate from the Windows certificate store and install the newly generated CA certificate. - See also: [Installing CA certificates for VPN connections](#installing-ca-certificates-for-vpn-connections) - See also: [Deleting CA certificates for VPN connections](#deleting-ca-certificates-for-vpn-connections) |
| Error message: "Unexpected error in application". | - Check whether other users have been saved in the TS Adapter IE Advanced user database. - The user "Administrator" cannot establish a remote connection. |
| Error message: "No corresponding CA certificate was found in the Windows certificate store". | - Use the automatic certificate download. Enter the fingerprint in the corresponding field in the connection dialog. - See also: [Establishing VPN connections](#establishing-vpn-connections)   Or - Export the CA certificate from the Web interface of the TS Adapter IE Advanced and install it manually in the Windows certificate store. - See also: [Installing CA certificates for VPN connections](#installing-ca-certificates-for-vpn-connections) |
| Error message: "The remote address specified does not correspond to the remote address of the TS Adapter". | - You must use the remote address which you specified in the TS Adapter IE Advanced to establish the connection. - You cannot use the IP address if you have entered the DNS name (and vice versa). |
| Error message: "The signature of the certificate could not be verified". | - If you have generated a new CA certificate on the TS Adapter IE Advanced, you need to delete the old CA certificate from the Windows certificate store and install the new one. - See also: [Deleting CA certificates for VPN connections](#deleting-ca-certificates-for-vpn-connections) - See also: [Installing CA certificates for VPN connections](#installing-ca-certificates-for-vpn-connections) |
| Error message: "Protocol error" | - Check that the IP address of the service PC is set in the configuration of the TS Adapter IE Advanced (Parameters &gt; Plant network) |
| Error message: "Connection setup error." | - Check to make sure that the LAN IP-address of the TS Adapter IE Advanced and the IP address of your network cards are in the same subnet. If this is the case, deactivate this network card before you establish the remote connection. |
| An e-mail cannot be sent. | - Check whether there is a network/Internet connection at the WAN port. - Check whether the mail server is accessible. - Check whether the outgoing connections in the TS Adapter IE Advanced are valid. - Check whether the SMTP port in the firewall is open for outgoing connections. |
