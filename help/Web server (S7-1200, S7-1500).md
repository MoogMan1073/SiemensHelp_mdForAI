---
title: "Web server (S7-1200, S7-1500)"
package: ProgKomWEBServ2MenUS
topics: 4
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Web server (S7-1200, S7-1500)

This section contains information on the following topics:

- [WWW: Synchronizing user pages (S7-1200, S7-1500)](#www-synchronizing-user-pages-s7-1200-s7-1500)

## WWW: Synchronizing user pages (S7-1200, S7-1500)

This section contains information on the following topics:

- [WWW: Synchronizing user pages (S7-1200, S7-1500)](#www-synchronizing-user-pages-s7-1200-s7-1500-1)
- [Program example of WWW (S7-1200, S7-1500)](#program-example-of-www-s7-1200-s7-1500)

### WWW: Synchronizing user pages (S7-1200, S7-1500)

#### Description

The instruction WWW initializes the web server of the CPU or synchronizes user-defined web pages, in short: "user pages", with the user program in the CPU.

Together with the Web server, user web pages make it possible for the CPU to access freely designed web pages of the CPU with a web browser.

Use script instructions (such as Javascript) and HTML code in user web pages to transfer data via a web browser for further processing to the CPU and to display data from the operand area of the CPU in the web browser. To synchronize the user program and the Web server, but also to initialize, call the instruction "WWW" in the user program.

#### Initialization

User web pages are "packaged" in data blocks for processing by the CPU. You will have to generate appropriate data blocks from the source files (HTML files, screens, Javascript files, ...) during configuration. The Web Control DB takes on a special role (default: DB 333). It contains status and control information as well as links to additional data blocks with coded web pages. The data blocks with coded web pages are called fragment DBs.

When the data blocks are downloaded into the CPU, the CPU does not "know" that user web pages are coded inside it. The instruction "WWW" in the startup OB, for example, will inform the CPU which DB is the Web Control DB. After this initialization, the user pages are accessible via a web browser.

#### Synchronization

If you want the user program to interact with the user pages, then the instruction "WWW" must be used in the cyclical program part.

Examples of interaction between user program and web page:

- Check received data
- Assemble and send back data to the web browser making the request

In this case it must be possible to evaluate the current status information and the Web server must receive control information, such as release of a web page requested by a web browser.

#### Parameter

The following table shows the parameters of the "WWW" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| CTRL_DB | Input | DB_WWW | I, Q, M, D, L or constant | Data block that describes the user pages (Web control DB) |
| RET_VAL | Output | INT | I, Q, M, D, L | Error information |

You can find additional information on valid data types under [Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types).

#### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. There are no web page requests that have to be released by the user program. |
| 00xy | x: indicates whether an error has occurred during initialization of the Web Control DB (CTRL_DB):  x=0: No errors occurred.  x=1: Error occurred. The error is coded in the byte "CTRL_DB.last_error" of the Web Control DB, see description of Web Control DB.  y: Number of the pending request. Several requests are possible (e. g. requests "0" and "1" are pending: y="3".  y="1": Request "0"  y="2": Request "1"  y="4": Request "2"  y="8": Request "3" |
| 803A | The specified Web Control DB does not exist on the CPU. |
| 8081 | Incorrect version or incorrect format of the Web Control DB. |
| 8082 | Web server is not enabled. |
| 8083 | User-defined web pages (user-defined pages) are not enabled for the communication with the web server. Only the web-based API (Web API) and web applications based on it are released. |
| 80C1 | There are no resources to initialize the web application, for example, because only two or four web applications may be running. |

#### Example

You will find the example here: [Program example of WWW](#program-example-of-www-s7-1200-s7-1500).

You can find additional information and the program code for the example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).

---

**See also**

[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)
  
[What you need to know about user pages (S7-300, S7-400, S7-1500)](Configuring%20the%20Web%20server%20%28S7-300%2C%20S7-400%2C%20S7-1500%29.md#what-you-need-to-know-about-user-pages-s7-300-s7-400-s7-1500)

### Program example of WWW (S7-1200, S7-1500)

#### Introduction

In the following example, you synchronize a user-defined Website with the program example in a CPU S7-1500 and test the program example via a Web server.

#### Requirement

Create nineteen tags in a global data block for storing the data.

![Requirement](images/84891884555_DV_resource.Stream@PNG-de-DE.png)

#### Interconnect parameters - in FB “SLI_FB_www“

You create the following interconnections in an FB "SLI_FB_www": You call the FB in an OB1.

**Network 1**: Interconnect the parameters of the "WWW" instruction as follows.

![Interconnect parameters - in FB “SLI_FB_www“](images/95833818379_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: You create the program for the Website in the FC “SLI_FC_MainWebProg_www“. You then call the FC “SLI_FC_MainWebProg_www“ in network 2 of the FB.

![Interconnect parameters - in FB “SLI_FB_www“](images/84892035083_DV_resource.Stream@PNG-de-DE.png)

#### Interconnecting parameters - in FC "SLI_FC_SetTOD_www"

In an FC “SLI_FC_SetTOD_www“ you create a program for using a time-of-day interrupt OB (OB11). You create the following interconnections:

**Network 1**: In the FC you interconnect the following local tags with the instructions “RD_SYS_T“ and “T_ADD“.

![Interconnecting parameters - in FC "SLI_FC_SetTOD_www"](images/84901456523_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: This is followed by interconnecting the tags for setting the time-of-day interrupt OB.

The local tag “#startDateTime“ (data type “Date_And_Time”) transfers the start time to the time-of-day interrupt OB.

![Interconnecting parameters - in FC "SLI_FC_SetTOD_www"](images/84901465355_DV_resource.Stream@PNG-de-DE.png)

**Network 3**: This is followed by interconnecting the tags for activating the time-of-day interrupt OB.

![Interconnecting parameters - in FC "SLI_FC_SetTOD_www"](images/84901474187_DV_resource.Stream@PNG-de-DE.png)

#### Interconnecting parameters - in the OB “SLI_todOB_www“

In the time-of-day interrupt OB “SLI_todOB_www“ (OB11) you create the following interconnections for cyclic increasing of the tag “tankLevel“.

![Interconnecting parameters - in the OB “SLI_todOB_www“](images/84892348939_DV_resource.Stream@PNG-de-DE.png)

#### Interconnecting parameters - in FC "SLI_FC_MainWebProg_www"

You create the following interconnections in the FC "SLI_FC_MainWebProg_www“.

The program “SLI_FC_MainWebProg_www“ allows control of a motor, a valve and the tank filling. In addition to this the output of various interrupt statuses is made possible. The program is controlled via the Web server.

**Network 1**: You call the FC “SLI_FC_SetTOD_www“ in the FC “SLI_FC_MainWebProg_www“.

![Interconnecting parameters - in FC "SLI_FC_MainWebProg_www"](images/84892095115_DV_resource.Stream@PNG-de-DE.png)

**Network 2**: This is followed by interconnecting the tags for opening the valve.

![Interconnecting parameters - in FC "SLI_FC_MainWebProg_www"](images/84892167947_DV_resource.Stream@PNG-de-DE.png)

**Network 3**: This is followed by interconnecting the tags for starting the motor.

![Interconnecting parameters - in FC "SLI_FC_MainWebProg_www"](images/84892240779_DV_resource.Stream@PNG-de-DE.png)

**Network 4**: This is followed by interconnecting the tags for querying the interrupt status “1“.

![Interconnecting parameters - in FC "SLI_FC_MainWebProg_www"](images/84892249611_DV_resource.Stream@PNG-de-DE.png)

**Networks 5 to 8**: This is followed by interconnecting the tags for querying the interrupt status “2“.

Interconnect the tags for querying the other interrupt statuses in the same way.

![Interconnecting parameters - in FC "SLI_FC_MainWebProg_www"](images/84892258443_DV_resource.Stream@PNG-de-DE.png)

**Network 9**: This is followed by interconnecting the tags for resetting the the motor and the filling of the tank..

![Interconnecting parameters - in FC "SLI_FC_MainWebProg_www"](images/84892292875_DV_resource.Stream@PNG-de-DE.png)

**Network 10**: This is followed by interconnecting the tags for resetting all the other values (BOOL).

![Interconnecting parameters - in FC "SLI_FC_MainWebProg_www"](images/84892301707_DV_resource.Stream@PNG-de-DE.png)

#### Setting CPU properties

Make the following settings in the CPU properties:

- Activate web server access under "... &gt; PROFINET interface &gt; Access to the web server".
- In “CPU properties &gt; Web server enable the Web server for the module,
- In the section “User administration“ create a new user with read and write rights.
- Make the following settings in the section "User pages":

  - You set the “HTML file path”.

    > **Note**
    >
    > The storage path should be the same as the path of the Sample Library for Instructions (SLI). The folder name is “SLI_html“. For example: “C:\TIA\_library\SLI_html“.
  - Enter the text "index.html" for the Start HTML page.
  - For the application you enter the name “WWW sample“.
  - Click the "Create block" button. The Web DB (333) and the Fragment DB (334) are then created.

#### Result for WWW

If the normally open contact ("executeWWW") supplies the signal state "TRUE", the "WWW" instruction is executed. The number of the data block that describes user defined Website is stored via the the input parameter CTRL_DB ("333"). The “WWW“ instruction initializes the user defined Website in the Web server of the CPU and immediately synchronizes the program example.

The output parameter RET_VAL ("returnValueWWW") indicates that the processing is running without errors.

![Result for WWW](images/84891893387_DV_resource.Stream@PNG-de-DE.png)

#### Result for the Web server

You call the Web server via the “Internet browser &gt; IP of the Web server”. You log in with your user name user name and -password.

In the Web server in “User pages” a link to the website defined by the user is displayed.

![Result for the Web server](images/84892396171_DV_resource.Stream@PNG-de-DE.png)

On the Website of the program example it is possible for you to output tags and transfer new values to the tags.

![Result for the Web server](images/84892405003_DV_resource.Stream@PNG-de-DE.png)

#### Functions used in the HTML document

Below you will see excerpts of the functions used in the program example with which the tags are transferred to the source code in the HTML document. For each function a tag is implemented via a call in the HTML document and at the relevant location in the HTML document is used with a further call.

| Function | To call in the HTML document | To output in the HTML element |
| --- | --- | --- |
| Data output: | &lt;!-- AWP_In_Variable Name='"SLI_gDB_www".tankLevel' --&gt; | :="SLI_gDB_www".tankLevel: |
| Enumeration (value replacement): | &lt;!-- AWP_Enum_Def Name="OpValvValue" Values='0:"Closed", 1:"Opened"' --&gt; | &lt;!-- AWP_Enum_Ref Name='"SLI_gDB_www".valveOutput' Enum="OpValvValue" --&gt;:="SLI_gDB_www".valveOutput: |
| Value change (from INT): | &lt;!-- AWP_In_Variable Name='"SLI_gDB_www".flowrate' --&gt; | &lt;form method="post" action="" onsubmit="return check();"&gt;   &lt;input type="text" name='"SLI_gDB_www".flowrate' size="10px"/&gt;   &lt;input class="button1" type="submit" value="Set flowrate"/&gt;  &lt;/form&gt; |
| Value change (from BOOL): | &lt;!-- AWP_Enum_Def Name="ResetValue" Values='0:"Off", 1:"On"' --&gt; | &lt;form method="post" action=""&gt;  &lt;input class="button1" type="submit" value="Reset"/&gt;  &lt;input type="hidden" name='"SLI_gDB_www".reset' size="34px" value="1"/&gt;  &lt;/form&gt; |

#### Program code

You can find additional information and the program code for the above-named example here: [Sample Library for Instructions](Example%20libraries%20%28S7-1200%2C%20S7-1500%29.md#sample-library-for-instructions-s7-1200-s7-1500).
