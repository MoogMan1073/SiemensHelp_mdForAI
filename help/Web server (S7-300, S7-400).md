---
title: "Web server (S7-300, S7-400)"
package: ProgKomWEBServ34enUS
topics: 2
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Web server (S7-300, S7-400)

This section contains information on the following topics:

- [WWW: Synchronizing user-defined web pages (S7-300, S7-400)](#www-synchronizing-user-defined-web-pages-s7-300-s7-400)

## WWW: Synchronizing user-defined web pages (S7-300, S7-400)

### Description

The instruction WWW initializes the Web server of the CPU or synchronizes user-defined web pages with the user program in the CPU.

User-defined web pages together with the Web server make it possible for the CPU to access freely designed web pages of the CPU with a web browser.

Use script instructions (such as Javascript) and HTML code in user-defined web pages to transfer data via a web browser for further processing to the CPU and to display data from the operand area of the CPU in the web browser. Call the WWW instruction in the user program for synchronization of the user program and the Web server as well as initialization.

### Initialization

User-defined web pages are "packaged" in data blocks for processing by the CPU. You will have to generate appropriate data blocks from the source files (HTML files, screens, Javascript files, ...) during configuration. The Web Control DB takes on a special role (default: DB 333). It contains status and control information as well as links to additional data blocks with coded web pages. The data blocks with coded web pages are called fragment DBs.

When the data block is downloaded into the CPU, the CPU does not "know" that user-defined web pages are coded inside it. The instruction "WWW" in the startup OB, for example, will inform the CPU which DB is the Web Control DB. The user-defined web pages can be accessed via a web browser after this initialization.

### Synchronization

If you want the user program to interact with the user-defined web pages, then the instruction WWW must be used in the cyclical program part.

Examples of interaction between user program and web page:

- Check received data
- Assemble and send back data to the web browser making the request

In this case it must be possible to evaluate the current status information and the Web server must receive control information, such as release of a web page requested by a web browser.

### Parameter

The following table shows the parameters of the instruction "WWW":

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| CTRL_DB | Input | BLOCK_DB | I, Q, M, D, L or constant | Data block that describes the user-defined web pages (Web Control DB) |
| RET_VAL | Output | INT | I, Q, M, D, L | Error information |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. There are no web page requests that have to be released by the user program. |
| 00xy | x: indicates whether an error has occurred during initialization of the Web Control DB (CTRL_DB):  x=0: No errors occurred.  x=1: Error occurred. The error is coded in the byte "CTRL_DB.commandstate.last_error" of the Web Control DB, see description of Web Control DB.  y: Number of the pending request. Several requests are possible (e. g. requests "0" and "1" are pending: y="3".  y="1": Request "0"  y="2": Request "1"  y="4": Request "2"  y="8": Request "3" |
| 803A | The specified Web Control DB does not exist on the CPU. |
| 8081 | Incorrect version or incorrect format of the Web Control DB |
| 80C1 | There are no resources to initialize the web application, for example, because only two or four web applications may be running. |
