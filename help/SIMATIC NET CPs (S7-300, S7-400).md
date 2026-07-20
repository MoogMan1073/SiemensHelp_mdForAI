---
title: "SIMATIC NET CPs (S7-300, S7-400)"
package: ProgCOMbloc34enUS
topics: 159
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# SIMATIC NET CPs (S7-300, S7-400)

This section contains information on the following topics:

- [Industrial Ethernet (S7-300, S7-400)](#industrial-ethernet-s7-300-s7-400)
- [PROFIBUS (S7-300, S7-400)](#profibus-s7-300-s7-400)
- SIMATIC NET CM/CP (S7-300, S7-400)

## Industrial Ethernet (S7-300, S7-400)

This section contains information on the following topics:

- [Introduction to Ethernet (S7-300, S7-400)](#introduction-to-ethernet-s7-300-s7-400)
- [Instructions for open communications services (SEND/RECEIVE interface) (S7-300, S7-400)](#instructions-for-open-communications-services-sendreceive-interface-s7-300-s7-400)
- [Instructions for access coordination with FETCH/WRITE (S7-300, S7-400)](#instructions-for-access-coordination-with-fetchwrite-s7-300-s7-400)
- [Instructions for connection diagnostics (S7-300, S7-400)](#instructions-for-connection-diagnostics-s7-300-s7-400)
- [Instructions for PROFINET IO (S7-300)](#instructions-for-profinet-io-s7-300)
- [Instructions for programmed connections (S7-300, S7-400)](#instructions-for-programmed-connections-s7-300-s7-400)
- [Instructions for FTP services (S7-300, S7-400)](#instructions-for-ftp-services-s7-300-s7-400)
- [Instructions for ERPC-CP (S7-300)](#instructions-for-erpc-cp-s7-300)

### Introduction to Ethernet (S7-300, S7-400)

This section contains information on the following topics:

- [General notes on the FCs / FBs (S7-300, S7-400)](#general-notes-on-the-fcs-fbs-s7-300-s7-400)
- [Setting parameters for FC calls (S7-300, S7-400)](#setting-parameters-for-fc-calls-s7-300-s7-400)
- [Parameters for specifying a CPU data area (input parameters) (S7-300, S7-400)](#parameters-for-specifying-a-cpu-data-area-input-parameters-s7-300-s7-400)
- [Status information (output parameters) (S7-300, S7-400)](#status-information-output-parameters-s7-300-s7-400)

#### General notes on the FCs / FBs (S7-300, S7-400)

##### Available instructions

The following list shows the numbers of the program blocks (instructions) as supplied. You can change these numbers.

Please note that you must use different instructions the S7­300 and S7­400 (separate libraries).

| Communication service / functional area | Type of instruction | Library |  |
| --- | --- | --- | --- |
|  |  |  |  |
| CP 300 | CP 400 |  |  |
| SEND / RECEIVE   (open communications services) | AG_SEND | x | x |
| AG_RECV | x | x |  |
| AG_LSEND | x <sup>2)</sup> | x |  |
| AG_LRECV | x <sup>2)</sup> | x |  |
| AG_LOCK | x | x |  |
| AG_UNLOCK | x | x |  |
| AG_CNTEX | x | x <sup>3)</sup> |  |
| AG_CNTRL | x | x <sup>3)</sup> |  |
| Programmed communication connections | IP_CONFIG | x | x |
| S7 communication | BSEND | x |  |
| BRCV | x |  |  |
| PUT | x |  |  |
| GET | x |  |  |
| USEND | x |  |  |
| URCV | x |  |  |
| C_CNTRL | x |  |  |
| FTP | FTP_CMD | x | x |
| PROFINET IO | PNIO_SEND | x |  |
| PNIO_RECV | x |  |  |
| PNIO_RW_REC | x |  |  |
| PNIO_ALARM | x |  |  |
| 1) PN_InOut / PN_InOut_Fast is supplied along with the SIMATIC iMap engineering tool.  2) Not to be used with the current CPs and no longer part of the current SIMATIC_NET_CP library  3) Depending on the CP type |  |  |  |

##### Which version of the instructions should I use?

The following descriptions also include information on differences in behavior between the various versions of the instructions. Please check and note the version identifiers of the instructions you are using.

The latest release of the version history for SIMATIC NET instructions can be found on the Internet using the following entry ID:

[9836605](http://support.automation.siemens.com/WW/view/de/9836605)

The global libraries installed with the Automation Workbench contain the versions of the instructions current when the Workbench was released.

> **Note**
>
> We recommend that you always use the latest versions of the instructions for all module types.
>
> You will find information on the current versions of the instructions and the current instructions to download from the Internet in our customer support:
>
> http://support.automation.siemens.com/WW/view/en/8797900
>
> With older module types, this recommendation assumes that you are using the latest firmware for the particular module type.

##### Instructions when modules are replaced

Module replacement in this sense means the replacement of a module with another module that may be a more recent version.

> **Note**
>
> Remember that if you replace a module, you must only use the instructions permitted for the configured CP type in the user program.
>
> We recommend that you always use the latest versions of the instructions for all module types. With older module types, this recommendation assumes that you are using the latest firmware for the particular module type.
>
> You will find more information on replacing modules in our Customer Support on the Internet.

The manuals for specific S7 CPs contain information on the compatibility of the S7­CPs and the corresponding instructions.

---

**See also**

[Symbolic and numerical names of instructions (S7-300, S7-400)](Functional%20description%20of%20S7-300-400%20CPUs%20%28S7-300%2C%20S7-400%29.md#symbolic-and-numerical-names-of-instructions-s7-300-s7-400)
  
[Programming manual "Functions (FC) and Function Blocks (FB) for SIMATIC NET S7 CPs"](http://support.automation.siemens.com/ww/view/de/30564821)

#### Setting parameters for FC calls (S7-300, S7-400)

Before describing the instruction in detail, a few general comments on calling and setting parameters for instructions will be useful at this point.

The general information below applies to the following parameter groups that exist for all instructions:

- Parameters for CP and connection assignment (input parameters)
- Parameters for specifying a CPU data area (input parameters)
- Status information (output parameters)

##### Calling communications instruction for an S7­300

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| Calling the communications instructions for S7-300 in more than one priority class is not permitted! If, for example, you call a communication instruction in OB1 and in OB35, execution of the instruction could be interrupted by the higher­priority OB.  If you call instructions in more than one OB, write your program so that a communications instruction that is currently executing cannot be interrupted by another communications instruction (for example by disabling/enabling interrupts with system instructions). |  |

#### Parameters for specifying a CPU data area (input parameters) (S7-300, S7-400)

##### Specifying the data area on the CPU

When you call an instruction, you transfer the address and length of the data area on the CPU in which the user data is available or will be stored or which can contain further parameter information

The ANY pointer data type is used to address this area.

#### Status information (output parameters) (S7-300, S7-400)

##### Evaluating status codes

For status evaluation, the following parameters must be evaluated in the user program:

- DONE or NDR  
  These parameters (DONE with send jobs and NDR with receive jobs) signal (successful) completion of the job.
- ERROR  
  This indicates that the job could not be executed error­free.
- STATUS  
  This parameter supplies detailed information about the execution of the job. Status codes can be returned during execution of the job (DONE=0 and ERROR=0).

  > **Note**
  >
  > Remember that the status codes DONE, NDR, ERROR, STATUS are updated at each instruction call.

##### Status codes during CP startup

With a warm or hot restart on the Ethernet CP, the output parameters of the instruction are reset as follows:

- DONE = 0
- NDR = 0
- ERROR = 0
- STATUS =

  - 8180<sub>H</sub> for AG_RECV / AG_LRECV
  - 8181<sub>H</sub> for AG_SEND / AG_LSEND / AG_SSEND

### Instructions for open communications services (SEND/RECEIVE interface) (S7-300, S7-400)

This section contains information on the following topics:

- [Instructions for the SEND/RECEIVE interface (S7-300, S7-400)](#instructions-for-the-sendreceive-interface-s7-300-s7-400)
- [AG_SEND / AG_LSEND / AG_SSEND (S7-300, S7-400)](#ag_send-ag_lsend-ag_ssend-s7-300-s7-400)
- [AG_RECV / AG_LRECV / AG_SRECV (S7-300, S7-400)](#ag_recv-ag_lrecv-ag_srecv-s7-300-s7-400)

#### Instructions for the SEND/RECEIVE interface (S7-300, S7-400)

##### Overview

The following instructions are available for transferring data on the SEND/RECEIVE interface:

| Instruction | Can be used with <sup>1)</sup> |  | Meaning |
| --- | --- | --- | --- |
| **S7-300** | **S7-400** |  |  |
| AG_SEND | x | x | for sending data |
| AG_RECV | x | x | for receiving data |
| AG_LSEND |  | x | for sending data |
| AG_LRECV |  | x | for receiving data |
| AG_SSEND |  | x | for sending data |
| AG_SRECV |  | x | for receiving data |

1) Notes on the Instructions for an S7­300 and S7­400

- The following applies to S7­300:

  - With the latest versions of the Ethernet CPs, only AG_SEND and AG_RECV are used; the data length can be up to 8192 bytes.
  - With S7–300 CPs (up to 6GK7 343–1EX10–0XE0 with firmware V2.2), use the instruction AG_LRECV on TCP connections instead of AG_RECV.
- The following applies to S7­400:

  - With AG_SEND / AG_RECV, the data length per job is restricted to <=240 bytes.   
    Longer data records (up to 8192 bytes) can be transferred with the AG_LSEND or AG_LRECV instructions.
  - AG_SSEND and AG_SRECV are for accelerated transfer of data by using optimized communication between CPU and CP in the S7 station. The fast communication has no effect on LAN communication. These two instructions are supported as of STEP 7 V5.4 SP3.
  - On an S7–400, AG_RECV cannot be used on TCP connections but only the AG_LRECV or AG_SRECV instructions.

##### Further information

Please check the supported data area for the S7­CP you are using in the manual for the specific device. You will find an overview of the versions of the instructions in the SIMATIC NET block history.

##### Application

The following diagram illustrates the use of the instructions described here for bi­directional data transfer on a configured connection.

![Application](images/12885612683_DV_resource.Stream@PNG-en-US.png)

##### Specifying the data area on the CPU

When you call an instructions, you transfer the address and length of the data area in the CPU. Remember, that the maximum length of the data area depends on the type and version of the instruction being used.

- AG_SEND and AG_RECV  
  Up to version V3.0 of these instructions, a maximum of 240 bytes can be sent or received. The current versions allow a data area of up to 8192 bytes for an S7­300. With an S7­400, AG_LSEND / AG_LRECV must still be used for larger data areas.
- AG_LSEND / AG_LRECV  
  Using the CPs of the S7­400 and with earlier versions of the S7­300, larger data areas can only be transferred with AG_LSEND or AG_LRECV. Please check the length of the data area in the product information of the CP.
- AG_SSEND / AG_SRECV  
  With CPs of the S7−400 that support PROFINET communication in conjunction with CPUs as of version 5.1, data can be transferred at higher transmission speeds with AG_SSEND or AG_SRECV (does not apply to the CP 443−1 Advanced 6GK7 443–1EX41–0XE0).  
  You can check which CP types are supported by CPUs as of version 5.1 in the manual of your CP (Section "Requirements for use").

The following table shows the limit values of the various connection types.

| INSTRUCTION | ISO transport | ISO-on-TCP | TCP | UDP |
| --- | --- | --- | --- | --- |
| AG_LSEND (S7-400) AG_SEND (S7-300) | 8192 bytes | 8192 bytes | 8192 bytes | 2048 bytes |
| AG_SEND (S7-400) | 240 bytes | 240 bytes | 240 bytes | 240 bytes |
| AG_LRECV (S7-400) AG_RECV (S7-300) | 8192 bytes | 8192 bytes | 8192 bytes | 2048 bytes |
| AG_RECV (S7-400) | 240 bytes | 240 bytes | 240 bytes | 240 bytes |
| AG_SSEND (S7-400) AG_SRECV (S7-400) | 1452 bytes | 1452 bytes | 1452 bytes | 1452 bytes |

> **Note**
>
> For information on the length of the data area you can transfer with older versions of the Ethernet CPs, refer to the product information / manual of the Ethernet CP you are using.

##### Use without job header

On specified connections, the address and job parameters are specified by the connection configuration. The user program only provides the user data in the UDP data area when sending with AG_SEND / AG_LSEND / AG_SSEND or receives the data with AG_RECV / AG_LRECV / AG_SRECV.

##### Use with header

Free UDP connections require a job header in the user data area.

The following schematic illustrates the structure of the job buffer and the meaning and location (high byte / low byte) of the parameters in the job header.

![Sending and receiving on a free UDP connection with programmed addresses](images/12881556747_DV_resource.Stream@PNG-en-US.png)

Sending and receiving on a free UDP connection with programmed addresses

- In the diagram (entries in hexadecimal) the following IP address is assumed as an example: 142.11.40.35;
- For the port address 1003, the following would be entered: For high byte: 03<sub>H</sub>; for low byte: EB<sub>H</sub>.
- The user data area can be up to 2048 bytes. Up to 2042 bytes of user data can be transferred. 6 bytes are reserved for the job header.   
  Please note that the data length specified in the instruction call (LEN parameter) must include the header and the user data!

##### Change call parameters only after job confirmation

> **Note**
>
> Once the job has been triggered, you can only change the call parameters of the call interface of the AG_SEND or AG_RECV instruction after the instruction has confirmed completion of the job with DONE=1 or with ERROR=1.
>
> If you do not keep to this rule, it is possible that the job will be aborted with an error.

##### Status display on the call interface of the instruction; Special situations with AG_SEND / AG_RECV (S7-300*)

The following behavior applies only to the S7-300 with program blocks as of version V4.0.

With AG_SEND and AG_RECV, you receive the following status codes for the operating situations mentioned:

- CP is in STOP.
- Connection is not configured.
- Connection is not established.
- Connection is aborted.

Codes:

- AG_SEND:   
  DONE=0; ERROR=1; Status=8183<sub>H</sub>
- AG_RECV:   
  DONE=0; ERROR=0; Status=8180<sub>H</sub>  
  or  
  DONE=0; ERROR=1; Status=8183<sub>H</sub>

---

**See also**

[General notes on the FCs / FBs (S7-300, S7-400)](#general-notes-on-the-fcs-fbs-s7-300-s7-400)

#### AG_SEND / AG_LSEND / AG_SSEND (S7-300, S7-400)

This section contains information on the following topics:

- [AG_SEND / AG_LSEND / AG_SSEND (Ind. Ethernet) (S7-300, S7-400)](#ag_send-ag_lsend-ag_ssend-ind-ethernet-s7-300-s7-400)
- [Parameters for AG_SEND / AG_LSEND / AG_SSEND (IE) (S7-300, S7-400)](#parameters-for-ag_send-ag_lsend-ag_ssend-ie-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400)

##### AG_SEND / AG_LSEND / AG_SSEND (Ind. Ethernet) (S7-300, S7-400)

###### Description

AG_SEND / AG_LSEND / AG_SSEND pass data to the Ethernet CP for transfer over a configured connection.

The selected data area can be a memory bit area or a data block area.

Error­free execution is indicated when the entire user data area could be sent over Ethernet.

Note:  
Unless otherwise stated, all the following information applies equally to AG_SEND, AG_LSEND and AG_SSEND.

###### Call

Call interface in FBD representation

![Call](images/12881560843_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> If you want to use the AG_SSEND instruction, you will need to select the "SPEED SEND/RECV" mode in the connection properties during configuration of the connection.

---

**See also**

[Parameters for AG_SEND / AG_LSEND / AG_SSEND (IE) (S7-300, S7-400)](#parameters-for-ag_send-ag_lsend-ag_ssend-ie-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400)
  
[AG_SEND / AG_LSEND (PROFIBUS) (S7-300, S7-400)](#ag_send-ag_lsend-profibus-s7-300-s7-400)
  
[Programming manual "Functions (FC) and Function Blocks (FB) for SIMATIC NET S7 CPs"](http://support.automation.siemens.com/ww/view/de/30564821)

##### Parameters for AG_SEND / AG_LSEND / AG_SSEND (IE) (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the AG_SEND / AG_LSEND / AG_SSEND instructions:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| ACT | INPUT | BOOL | 0,1 | If the instruction is called with ACT=1, LEN bytes are sent from the ISO transport data area specified with the SEND parameter.  If the instruction is called with ACT = 0, the status codes DONE, ERROR and STATUS are updated. |
| ID | INPUT | INT | 1,2...64  (S7-400)  1,2...16  (S7-300) | The connection number of the connection is specified in the parameter ID. |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP with STEP 7, the module start address is displayed in the configuration table. Specify this address here. |
| SEND | INPUT | ANY |  | Specifies the address and length  The address of the data area points to one of the alternatives:  - Memory bit area - Data block area |
| LEN | INPUT | INT | On ISO transport and ISO­on­TCP / TCP:  1, 2 to 8192 (or up to "length specified for SEND parameter")    On UDP:  1, 2 to 2048 (or up to "length specified for SEND parameter") | Number of bytes to be sent from the data area with this job. The possible values range from 1 to length specified for the SEND parameter.  - Note the type of instruction:   - For S7-300 The current versions of AG_SEND allow up to 8192 bytes (2048 bytes for UDP) to be transferred.   - For S7-400 With AG_SEND, the data area is restricted to a maximum of 240 bytes.   Note the following with an S7-400:  - Improved performance with shorter data records: Transfer of data records up to 240 bytes results in better performance! This applies regardless of the type used (AG_SEND / AG_LSEND). - With AG_SSEND, the data area is restricted to a maximum of 1452 bytes. |
| DONE | OUTPUT | BOOL | 0: Job active 1: Job done | The status parameter indicates whether or not the job was completed without errors. As long as DONE = 0, no further job can be triggered. When the job is accepted, DONE is set to 0 by the CP. |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code   For the meaning in conjunction with the parameters DONE and STATUS, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400) |
| STATUS | OUTPUT | WORD |  | Status code  For the meaning in conjunction with the parameters DONE and ERROR, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400) |

---

**See also**

[AG_SEND / AG_LSEND / AG_SSEND (Ind. Ethernet) (S7-300, S7-400)](#ag_send-ag_lsend-ag_ssend-ind-ethernet-s7-300-s7-400)

##### Parameters DONE, ERROR, STATUS (S7-300, S7-400)

###### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information about the output parameter RET_VAL in the descriptions of the referenced system program blocks
>
> Which system program blocks are used and are relevant for error evaluation, can be queried in STEP 7.

AG_SEND / AG_LSEND / AG_SSEND status codes

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 1 | 0 | 0000<sub>H</sub> | Job completed without error. |
| 0 | 0 | 0000<sub>H</sub> | No job being executed. |
| 0 | 0 | 8181<sub>H</sub> | Job active. |
| 0 | 1 | 7000<sub>H</sub> | The condition code is possible only with S7-400: The instruction was called with ACT=0; the job has not yet been processed. |
| 0 | 1 | 8183<sub>H</sub> | No configuration or the ISO/TCP service has not yet started on the Ethernet CP. |
| 0 | 1 | 8184<sub>H</sub> | - Illegal data type specified for the SEND parameter. - System error (the source data area is incorrect). |
| 0 | 1 | 8185<sub>H</sub> | LEN parameter longer than SEND source area. |
| 0 | 1 | 8186<sub>H</sub> | ID parameter invalid.   - ID != 1, 2 to 16 (S7-300) - ID != 1, 2 to 64.(S7-400) |
| 0 | 1 | 8302<sub>H</sub> | No receive resources on the destination station. Receiving station cannot process received data quickly enough or has not made any receive resources available. |
| 0 | 1 | 8304<sub>H</sub> | The connection is not established. The send job should only be attempted again after waiting for at least 100 ms. |
| 0 | 1 | 8311<sub>H</sub> | The destination station cannot be obtained under the specified Ethernet address. |
| 0 | 1 | 8312<sub>H</sub> | Ethernet error on the CP. |
| 0 | 1 | 8F22<sub>H</sub> | Source area invalid, e.g.:  Area does not exist in the DB  LEN parameter < 0 |
| 0 | 1 | 8F24<sub>H</sub> | Area error reading a parameter. |
| 0 | 1 | 8F28<sub>H</sub> | Alignment error reading a parameter. |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | Wrong DB number |
| 0 | 1 | 8F3A<sub>H</sub> | Area not loaded (DB). |
| 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the  I/O area. |
| 0 | 1 | 8F44<sub>H</sub> | Access to a parameter to be read during execution of the instruction is prevented. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference  e.g. parameter LEN=0. |
| 0 | 1 | 8090<sub>H</sub> | - Module with this module start address does not exist; - The instruction being used does not match the system family being used (remember to use different instructions for S7­300 and S7­400). |
| 0 | 1 | 8091<sub>H</sub> | Module start address not at a double­word boundary. |
| 0 | 1 | 8092<sub>H</sub> | In the ANY reference, a type other than BYTE is specified. (S7-400 only) |
| 0 | 1 | 80A4<sub>H</sub> | The communication bus connection between the CPU and CP is not established.  (With newer CPU versions) |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | The specified length (in the LEN parameter) is incorrect. |
| 0 | 1 | 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established. |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | CPU resources (memory) occupied. |
| 0 | 1 | 80C4<sub>H</sub> | Communications error   Occurs temporarily and a repetition in the user program will often remedy the problem |
| 0 | 1 | 80D2<sub>H</sub> | Module start address incorrect. |

---

**See also**

[AG_SEND / AG_LSEND / AG_SSEND (Ind. Ethernet) (S7-300, S7-400)](#ag_send-ag_lsend-ag_ssend-ind-ethernet-s7-300-s7-400)

#### AG_RECV / AG_LRECV / AG_SRECV (S7-300, S7-400)

This section contains information on the following topics:

- [AG_RECV / AG_LRECV / AG_SRECV (Ind. Ethernet) (S7-300, S7-400)](#ag_recv-ag_lrecv-ag_srecv-ind-ethernet-s7-300-s7-400)
- [Parameters for AG_RECV / AG_LRECV / AG_SRECV (IE) (S7-300, S7-400)](#parameters-for-ag_recv-ag_lrecv-ag_srecv-ie-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (IE) (S7-300, S7-400)](#parameters-done-error-status-ie-s7-300-s7-400)

##### AG_RECV / AG_LRECV / AG_SRECV (Ind. Ethernet) (S7-300, S7-400)

###### Description

The AG_RECV / AG_LRECV / AG_SRECV instruction receives the data transferred on a configured connection from the Ethernet CP.

The data area specified for the receive data can be a memory bit area or a data block area.

Error­free execution is indicated when the data could be received from the Ethernet CP.

Note:  
Unless otherwise stated, all the following information applies equally to AG_RECV and AG_LRECV / AG_SRECV.

###### Call

Call interface in FBD representation

![Call](images/12881563915_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> If you want to use the AG_SRECV instruction, you will need to select the "SPEED SEND/RECV" mode in the connection properties during configuration of the connection.

---

**See also**

[AG_RECV / AG_LRECV (PROFIBUS) (S7-300, S7-400)](#ag_recv-ag_lrecv-profibus-s7-300-s7-400)
  
[Parameters for AG_RECV / AG_LRECV / AG_SRECV (IE) (S7-300, S7-400)](#parameters-for-ag_recv-ag_lrecv-ag_srecv-ie-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (IE) (S7-300, S7-400)](#parameters-done-error-status-ie-s7-300-s7-400)

##### Parameters for AG_RECV / AG_LRECV / AG_SRECV (IE) (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the AG_RECV / AG_LRECV / AG_SRECV instructions:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| ID | INPUT | INT | 1, 2 to 64 (S7-400) 1, 2 to 16 (S7-300) | The connection number of the ISO transport connection is specified in the ID parameter. |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP with STEP 7, the module start address is displayed in the configuration table. Specify this address here. |
| RECV | INPUT | ANY |  | Specifies the address and length  The address of the data area points to one of the alternatives:  - Memory bit area - Data block area   Note on length:  Performance is improved when transferring data records up to 212 bytes if you also restrict the length to 212 bytes at the RECV parameter.  Point to note with AG_SRECV:  With AG_SRECV, always set RECV to the maximum receive buffer length of 1452 bytes. Otherwise, the following error can occur in certain situations:  NDR=0; ERROR=1; STATUS=8185<sub>H</sub> |
| NDR | OUTPUT | BOOL | 0: - 1: new data | The parameter indicates whether or not new data was accepted. For the meaning in conjunction with the ERROR and STATUS parameters, refer to [AG_RECV / AG_LRECV / AG_SRECV (Ind. Ethernet)](#ag_recv-ag_lrecv-ag_srecv-ind-ethernet-s7-300-s7-400) |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code For the meaning in conjunction with the NDR and STATUS parameters, refer to [AG_RECV / AG_LRECV / AG_SRECV (Ind. Ethernet)](#ag_recv-ag_lrecv-ag_srecv-ind-ethernet-s7-300-s7-400) |
| STATUS | OUTPUT | WORD |  | Status code For the meaning in conjunction with the NDR and ERROR parameters, refer to [AG_RECV / AG_LRECV / AG_SRECV (Ind. Ethernet)](#ag_recv-ag_lrecv-ag_srecv-ind-ethernet-s7-300-s7-400) |
| LEN | OUTPUT | INT | **On ISO Transport and ISO­on­TCP:**   1,2,...8192     **On UDP:**   1,2,...2048 | Specifies the number of bytes accepted from the Ethernet CP and entered in the data area.  Note the type of instruction:  - For S7-300 The current versions of AG_RECV allow up to 8192 bytes (2048 bytes for UDP) to be transferred. - For S7-400 With AG_RECV, the data area is restricted to a maximum of 240 bytes. With AG_SRECV, the data area is restricted to a maximum of 1452 bytes. |

##### Parameters DONE, ERROR, STATUS (IE) (S7-300, S7-400)

###### Condition codes

The following table shows the codes formed by the NDR, ERROR and STATUS parameters that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information about the output parameter RET_VAL in the descriptions of the referenced system program blocks.
>
> Which system program blocks are used and are relevant for error evaluation, can be queried in STEP 7.

AG_RECV / AG_LRECV / AG_SRECV condition codes

| NDR | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 1 | 0 | 0000<sub>H</sub> | New data accepted. |
| 0 | 0 | 8180<sub>H</sub> | There is no data available yet (not with AG_SRECV). |
| 0 | 0 | 8181<sub>H</sub> | Job active. |
| 0 | 1 | 8183<sub>H</sub> | - The configuration is missing; - The ISO transport service has not yet started on the Ethernet CP; - The connection is not established. |
| 0 | 1 | 8184<sub>H</sub> | - Illegal type specified for the RECV parameter; - System error. |
| 0 | 1 | 8185<sub>H</sub> | Destination buffer (RECV) is too short. |
| 0 | 1 | 8186<sub>H</sub> | ID parameter invalid.  ID != 1, 2 to 16 (S7-300).  ID != 1, 2 to 64.(S7-400) |
| 0 | 1 | 8304<sub>H</sub> | The connection is not established. The send job should only be attempted again after waiting for at least 100 ms. |
| 0 | 1 | 8F23<sub>H</sub> | Source area invalid, e.g.:  Area does note exist in the DB. |
| 0 | 1 | 8F25<sub>H</sub> | Area error writing a parameter. |
| 0 | 1 | 8F29<sub>H</sub> | Alignment error writing a parameter |
| 0 | 1 | 8F30<sub>H</sub> | Parameter is in the write­protected first current data block. |
| 0 | 1 | 8F31<sub>H</sub> | Parameter is in the write­protected second current data block. |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | DB number error |
| 0 | 1 | 8F3A<sub>H</sub> | Destination area not loaded (DB). |
| 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the I/O area. |
| 0 | 1 | 8F45<sub>H</sub> | Address of the parameter to be written is disabled in the access track. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, for example illegal ANY reference. |
| 0 | 1 | 8090<sub>H</sub> | - No module with this module start address exists or the CPU is in STOP mode - The instruction being used does not match the system family being used (remember to use different instructions for S7­300 and S7­400). |
| 0 | 1 | 8091<sub>H</sub> | Module start address not at a double­word boundary. |
| 0 | 1 | 8092<sub>H</sub> | In the ANY reference, a type other than BYTE is specified. (S7-400 only) |
| 0 | 1 | 80A0<sub>H</sub> | Negative acknowledgment reading from the module. |
| 0 | 1 | 80A4<sub>H</sub> | The communication bus connection between the CPU and CP is not established. |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | Possible causes:  - The destination area is invalid. - The destination area is too short. - The destination area for the received data was adequately dimensioned.   Remedy: Run another receive call with maximum receive buffer size. This applies regardless of the connection type (unicast / multicast / broadcast) and the device family (S7-300 / S7-400). |
| 0 | 1 | 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established. |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | CPU resources (memory) occupied. |
| 0 | 1 | 80C4<sub>H</sub> | Communications error   Occurs temporarily and a repetition in the user program will often remedy the problem |
| 0 | 1 | 80D2<sub>H</sub> | Module start address incorrect. |

---

**See also**

[AG_RECV / AG_LRECV / AG_SRECV (Ind. Ethernet) (S7-300, S7-400)](#ag_recv-ag_lrecv-ag_srecv-ind-ethernet-s7-300-s7-400)

### Instructions for access coordination with FETCH/WRITE (S7-300, S7-400)

This section contains information on the following topics:

- [Instructions for access coordination with FETCH/WRITE (S7-300, S7-400)](#instructions-for-access-coordination-with-fetchwrite-s7-300-s7-400-1)
- [AG_LOCK (S7-300, S7-400)](#ag_lock-s7-300-s7-400)
- [AG_UNLOCK (S7-300, S7-400)](#ag_unlock-s7-300-s7-400)

#### Instructions for access coordination with FETCH/WRITE (S7-300, S7-400)

##### Overview

The following instructions are available for the FETCH/WRITE function to coordinate access:

| Instruction | can be used with: |  | Meaning |
| --- | --- | --- | --- |
| **S7-300** | **S7-400** |  |  |
| AG_LOCK | x | x | Locks external data access with FETCH/WRITE. |
| AG_UNLOCK | x | x | Releases external data access with FETCH/WRITE. |

##### Caution when Configuring

If you use AG_LOCK and AG_UNLOCK, you must specify the following information for CPs in S7­400 stations in the configuration:

- Under "Properties > Addresses"  
  The "Address setting for LOCK/UNLOCK" option must be selected if the selection is available.

##### How It works

With these instructions, you can coordinate access to system memory areas so that no inconsistent data is created and transferred. The control is from the user program in the S7 CPU that can, if necessary, disable an external FETCH/WRITE access using an AG_LOCK call. After a certain time or after the local write/read access is completed, an AG_UNLOCK job can be used to enable external access again.

Another advantage is that this access lock only applies to the FETCH/WRITE connection specified in the call. If more than one FETCH/WRITE connection is configured, these can, for example, be used for certain specific system areas and a selective access coordination can be implemented.

The following diagram illustrates the usual chronological sequence of memory access coordination controlled in the user program with AG_LOCK and AG_UNLOCK.

![How It works](images/12881566987_DV_resource.Stream@PNG-en-US.png)

The lock job must first be monitored in the user program using the code in the return parameter LOCKED. As long as LOCKED=0 is indicated, it must be assumed that there is still an external FETCH/WRITE access active.

If LOCKED=1 is indicated, this shows that the lock is active; data can now be modified by the user program.

The status code is updated at each instruction call.

#### AG_LOCK (S7-300, S7-400)

This section contains information on the following topics:

- [AG_LOCK (S7-300, S7-400)](#ag_lock-s7-300-s7-400-1)
- [Parameters for AG_LOCK (S7-300, S7-400)](#parameters-for-ag_lock-s7-300-s7-400)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400)

##### AG_LOCK (S7-300, S7-400)

###### Description

Using the AG_LOCK instruction, the data exchange using FETCH or WRITE on the connection selected with the parameter ID is disabled. The LOCKED output indicates whether or not the lock was successful. If the lock was not successful, the job must be triggered again in a later CPU cycle.

The STATUS output indicates the status of the CP for this connection.

###### Call

Call interface in FBD representation

![Call](images/12881723659_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Parameters for AG_LOCK (S7-300, S7-400)](#parameters-for-ag_lock-s7-300-s7-400)
  
[STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400)

##### Parameters for AG_LOCK (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for AG_LOCK:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| ID | INPUT | INT | 1, 2 to 16 for S7­300  1, 2 to 64 for S7­400 | The connection number of the connection is specified in the parameter ID. |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP with STEP 7, the module start address is displayed in the configuration table. Specify this address here. |
| LOCKED | OUTPUT | BOOL | 0: not (yet) locked 1: locked | Shows the status of the access lock requested on the specified FETCH/WRITE connection. |
| STATUS | OUTPUT | WORD |  | Status code  For the meaning, see [STATUS parameter](#status-parameter-s7-300-s7-400) |

---

**See also**

[AG_LOCK (S7-300, S7-400)](#ag_lock-s7-300-s7-400-1)

##### STATUS parameter (S7-300, S7-400)

###### Condition codes

The following table shows the STATUS code that must be evaluated by the user program.

AG_LOCK condition codes

| STATUS | Meaning |
| --- | --- |
| 7000<sub>H</sub> | CP is not processing a job |
| 7001<sub>H</sub> | FETCH active |
| 7002<sub>H</sub> | WRITE active |
| 8183<sub>H</sub> | FETCH/WRITE not configured for this connection (S7-400 only) |
| 8186<sub>H</sub> | ID number not in permitted range (e.g. 1...64 for S7-400 Industrial Ethernet CPs) |
| 80A4<sub>H</sub> | The communication bus connection between the CPU and CP is not established (with newer CPU versions). |
| 80B0<sub>H</sub> | The module does not recognize the data record. |
| 80B1<sub>H</sub> | The specified length (in the LEN parameter) is incorrect. |
| 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established. |
| 80C0<sub>H</sub> | The data record cannot be read. |
| 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 80C2<sub>H</sub> | There are too many jobs pending. |
| 80C3<sub>H</sub> | CPU resources (memory) occupied. |
| 80C4<sub>H</sub> | Communications error   Occurs temporarily and a repetition in the user program will often remedy the problem. |
| 80D2<sub>H</sub> | Module start address incorrect. |

---

**See also**

[AG_LOCK (S7-300, S7-400)](#ag_lock-s7-300-s7-400-1)

#### AG_UNLOCK (S7-300, S7-400)

This section contains information on the following topics:

- [AG_UNLOCK (S7-300, S7-400)](#ag_unlock-s7-300-s7-400-1)
- [Parameters for AG_UNLOCK (S7-300, S7-400)](#parameters-for-ag_unlock-s7-300-s7-400)
- [STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400-1)

##### AG_UNLOCK (S7-300, S7-400)

###### Description

With the aid of the AG_UNLOCK instruction, you enable external access to user memory areas of the S7‑CPU. With FETCH or WRITE, access via the connection selected with the ID parameter is then possible.

The AG_UNLOCK follows an access lock with AG_LOCK.

###### Call

Call interface in FBD representation

![Call](images/44487063691_DV_resource.Stream@PNG-de-DE.png)

###### How It works

To release the connection again, the instruction must clear the LOCK request bit again. The instruction also shows the current status using error messages.

---

**See also**

[STATUS parameter (S7-300, S7-400)](#status-parameter-s7-300-s7-400-1)
  
[Parameters for AG_UNLOCK (S7-300, S7-400)](#parameters-for-ag_unlock-s7-300-s7-400)

##### Parameters for AG_UNLOCK (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for AG_UNLOCK:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| ID | INPUT | INT | 1, 2 to 16 for S7­300  1, 2 to 64 for S7­400 | The connection number of the connection is specified in the parameter ID. (See Configuration) |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP with STEP 7, the module start address is displayed. Specify this address here. |
| STATUS | OUTPUT | WORD |  | Status code:  For the meaning, see [STATUS parameter](#status-parameter-s7-300-s7-400-1) |

---

**See also**

[AG_UNLOCK (S7-300, S7-400)](#ag_unlock-s7-300-s7-400-1)

##### STATUS parameter (S7-300, S7-400)

###### Condition codes

The following table shows the STATUS code that must be evaluated by the user program.

AG_UNLOCK condition codes

| STATUS | Meaning |
| --- | --- |
| 7000<sub>H</sub> | CP is not processing a job |
| 7001<sub>H</sub> | FETCH active |
| 7002<sub>H</sub> | WRITE active |
| 8183<sub>H</sub> | FETCH/WRITE not configured for this connection (S7-400 only) |
| 8186<sub>H</sub> | ID number not in permitted range (e.g. 1...64 for S7-400 Industrial Ethernet CPs) |
| 80A4<sub>H</sub> | The communication bus connection between the CPU and CP is not established (with newer CPU versions). |
| 80B0<sub>H</sub> | The module does not recognize the data record. |
| 80B1<sub>H</sub> | The specified length (in the LEN parameter) is incorrect. |
| 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established. |
| 80C0<sub>H</sub> | The data record cannot be read. |
| 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 80C2<sub>H</sub> | There are too many jobs pending. |
| 80C3<sub>H</sub> | CPU resources (memory) occupied. |
| 80C4<sub>H</sub> | communications error Occurs temporarily and a repetition in the user program will often remedy the problem. |
| 80D2<sub>H</sub> | Module start address incorrect. |

---

**See also**

[AG_UNLOCK (S7-300, S7-400)](#ag_unlock-s7-300-s7-400-1)

### Instructions for connection diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [AG_CNTEX (S7-300, S7-400)](#ag_cntex-s7-300-s7-400)
- [AG_CNTRL for connection diagnostics (S7-300, S7-400)](#ag_cntrl-for-connection-diagnostics-s7-300-s7-400)

#### AG_CNTEX (S7-300, S7-400)

This section contains information on the following topics:

- [AG_CNTEX (S7-300, S7-400)](#ag_cntex-s7-300-s7-400-1)
- [How the PING function works (S7-300, S7-400)](#how-the-ping-function-works-s7-300-s7-400)
- [Parameters for AG_CNTEX (S7-300, S7-400)](#parameters-for-ag_cntex-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-1)
- [Commands and job results - AG_CNTEX (S7-300, S7-400)](#commands-and-job-results---ag_cntex-s7-300-s7-400)

##### AG_CNTEX (S7-300, S7-400)

###### Significance and how It works

With the AG_CNTEX instruction, it is possible run diagnostics on connections and to address devices using the ping command via the network. When necessary, you can initialize connection establishment again using AG_CNTEX.

> **Note**
>
> **AG_CNTRL and AG_CNTEX**
>
> The AG_CNTEX program block provides expanded functionality compared with the AG_CNTRL program block.
>
> All the functions of AG_CNTRL are included in AG_CNTEX and they can be used identically in the user program.

The following actions are possible by setting commands:

- Reading out connection information

  Based on status information, you can decide whether or not it would be useful to reset all or individual connections of the CP.
- Resetting configured connections

  You can reset individual connections or all connections of a CP.
- Aborting the active connection and establishing it again
- Reading out connection types configured on the CP (expanded functionality compared with AG_CNTRL)
- Send PING command (expansion compared with AG_CNTRL)

  You can check whether a specific node is reachable in the network.

The commands of the AG_CNTEX program block are permitted only for SEND/RECV connections based on the ISO / RFC / TCP / UDP protocols.

> **Note**
>
> **Availability in the block library**
>
> If the program block AG_CNTEX is not yet available in the SIMATIC_NET_CP block library, install the current SIMATIC NET block library; you will find this under the following entry ID on the Internet:
>
> [Link:](https://support.industry.siemens.com/cs/ww/en/view/109481127)

###### Call interface

Call interface in FBD representation

![Call interface](images/30071382283_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[How the PING function works (S7-300, S7-400)](#how-the-ping-function-works-s7-300-s7-400)
  
[Parameters for AG_CNTEX (S7-300, S7-400)](#parameters-for-ag_cntex-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-1)
  
[Commands and job results - AG_CNTEX (S7-300, S7-400)](#commands-and-job-results---ag_cntex-s7-300-s7-400)

##### How the PING function works (S7-300, S7-400)

###### Mode of operation / call sequence

With the CMD=8 PING command, you instruct the CP to send 4 successive PING requests over the network to the IP address specified in the job. The PING echo is expected by the CP within the period of time you set in the PING job field.

The CP registers the response times and enters these in the RESULT 1/2 parameters.

The RESULT 1/2 parameters can be queried with PING command CMD=9. As soon as the 4 PING requests have been replied to, or their set monitoring time has been exceeded, execution is confirmed in the DONE=1 parameter. The PING result can then be queried within a maximum of 30 seconds; afterwards, the RESULT entries become invalid.

> **Note**
>
> **PING is only possible over a configured connection**
>
> The PING command is only possible if at least **one** connection for the SEND/RECEIVE interface (TCP, ISO-on-TCP, ISO-Transport, UDP) is configured.

###### Several PING requests at the same time

You can send up to 4 PING requests at the same time to different IP addresses. To do this, you must use the same instance DB for the ping requests. Further PING requests are possible only after completion of at least one of the current PING requests.

If too many PING requests are sent at the same time, an error message to this effect is output (STATUS parameter = 828A<sub>H</sub>).

###### When are PING requests completed?

PING requests count as being completed when one of the following conditions is met:

- The PING result was read out:
- The PING result was not read out but 30 seconds have elapsed since the Ping result was available.

---

**See also**

[AG_CNTEX (S7-300, S7-400)](#ag_cntex-s7-300-s7-400-1)
  
[Commands and job results - AG_CNTEX (S7-300, S7-400)](#commands-and-job-results---ag_cntex-s7-300-s7-400)

##### Parameters for AG_CNTEX (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the AG_CNTEX function:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| ACT | INPUT | BOOL | 0, 1 | The FB must be called with ACT=1.  If it is called with ACT=0, there is no function call and the block is exited again immediately. |
| ID | INPUT | INT | - 1, 2, .., n,  or  - 0 | The connection number of the connection is specified in the parameter ID. The connection number can be found in the configuration. n is the maximum number of connections and is dependent on the product (S7-300 or S7-400).  For a call that addresses all connections, 0 must be specified as the ID. This affects:  - the functions CN_STATUS_ALL (CMD 3) and CN_RESET_ALL (CMD 4) - PING command with CMD 8 or CMD 9 |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP with STEP 7, the module start address is displayed. Specify this address here. |
| CMD | INPUT | INT |  | Command to FB AG_CNTEX |
| PING | INPUT | ANY |  | References a block of data (for example DB) that contains the data structure for the PING command.  The block of data contains the IP address and optional information about the time monitoring and the number of bytes to be transferred in the PING request.  Data structure, see below |
| DONE | OUTPUT | BOOL | 0:  Job still being processed or not yet triggered  1:  Job done | This parameter indicates whether or not the job was completed without errors.  For the meaning in conjunction with the parameters ERROR and STATUS, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-1)  Note:  If DONE=1, RESULT can be evaluated |
| ERROR | OUTPUT | BOOL | 0: No error  1: Error | Error code  For the meaning in conjunction with the parameters DONE and STATUS, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-1) |
| STATUS | OUTPUT | WORD |  | Status code  For the meaning in conjunction with the parameters DONE and ERROR, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-1) |
| RESULT1 | OUTPUT | DWORD |  | Information returned to AG_CNTEX according to the command. |
| RESULT2 | OUTPUT | DWORD |  | Part 2 of the information returned to AG_CNTEX according to the command. |

###### PING block of data

The PING parameter references a block of data with the following data structure:

| Parameter | Data type | Range of values | Note |
| --- | --- | --- | --- |
| IP address | ARRAY [1..4] of Byte |  |  |
| TIMEOUT | INT | 1..60000 ms | Can be specified as an option; default value = 1000 ms |
| Size | INT | 1..1000 bytes | Can be specified as an option; default value = 32 bytes |

---

**See also**

[AG_CNTEX (S7-300, S7-400)](#ag_cntex-s7-300-s7-400-1)

##### Parameters DONE, ERROR, STATUS (S7-300, S7-400)

###### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

The command results in the RESULT1/2 parameters must also be evaluated according to [Commands and job results - AG_CNTEX](#commands-and-job-results---ag_cntex-s7-300-s7-400).

AG_CNTEX codes

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 1 | 0 | 0000<sub>H</sub> | A job (CMD) was transferred successfully to the CP (for example RESET) or a status was read successfully from the CP.  The RESULT1/2 parameters can be evaluated. |
| 0 | 0 | 0000<sub>H</sub> | There has been no block call yet or the program block was called with ACT=0. |
| 0 | 0 | 8181<sub>H</sub> | Job active  The block call must be repeated with the same parameters until DONE or ERROR is signaled. |
| 0 | 1 | 8183<sub>H</sub> | No configuration or the service has not yet started on the Ethernet CP. |
| 0 | 1 | 8184<sub>H</sub> | System error or wrong parameter type. The cause can be:  - Data type of the ANY pointer not correct for the PING parameter. - The ANY pointer references an odd bit address. |
| 0 | 1 | 8186<sub>H</sub> | The ID parameter is invalid. The permitted ID depends on the selected command. |
| 0 | 1 | 8187<sub>H</sub> | The CMD parameter is invalid. |
| 0 | 1 | 8090<sub>H</sub> | Possible meanings:  - No module with this module start address exists; - The program block being used does not match the system family being used (remember to use different program blocks for S7­300 and S7­400); - The function is not supported by this module. |
| 0 | 1 | 8091<sub>H</sub> | The module start address is not at a double­word boundary. |
| 0 | 1 | 8092<sub>H</sub> | The module start address is incorrect. |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established. The corresponding CPU in the H system is in STOP mode. |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | CPU resources (memory) occupied. |
| 0 | 1 | 80C4<sub>H</sub> | Communications error  The error occurs temporarily; it is usually best to repeat the job in the user program. |
| 0 | 1 | 8286<sub>H</sub> | The value for the "Timeout" in the PING data block is outside the valid range of values. |
| 0 | 1 | 8287<sub>H</sub> | The IP address specified in the PING DB is reserved and therefore not permitted. |
| 0 | 1 | 8288<sub>H</sub> | The display occurs only with the PING result request command.  Possible meanings:  - The IP address was not reached by the PING command (for example because the CP was changed to STOP mode after the PING request command was sent); - The PING result has already been read out; - The PING result was not read out within the maximum time of 30 seconds. |
| 0 | 1 | 8289<sub>H</sub> | The data volume for the PING request has exceeded the permitted range (maximum 1000 bytes; see data structure for the PING command) |
| 0 | 1 | 828A<sub>H</sub> | There are already 4 ping requests being processed. New requests are only possible again after processing the existing requests. |
| 0 | 1 | 828B<sub>H</sub> | There is already a PING request being processed for the specified IP address. Use the PING result request to complete the current processing. |

---

**See also**

[AG_CNTEX (S7-300, S7-400)](#ag_cntex-s7-300-s7-400-1)

##### Commands and job results - AG_CNTEX (S7-300, S7-400)

###### Commands and evaluating the job results

The following table shows you the possible commands and the results that can be evaluated in the RESULT1/2 parameters.

> **Note**
>
> **Command evaluation with older CP types or firmware versions**
>
> The commands described below are supported by the current CP types or firmware versions. You should also check the more detailed information under the following entry ID:
>
> [http://support.automation.siemens.com/WW/view/en/33414377](http://support.automation.siemens.com/ww/view/en/33414377)

Commands to FC AG_CNTRL

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 0 | NOP – no operation  The block executes without a job being sent to the CP. |  |  |
| **RESULT (for CMD = 0)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | Executed without error |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | CN_STATUS – connection status  This command returns the status of the connection selected with the ID.  The CP is selected in the LADDR parameter.   If bit 15 (reset ID) is set, this is automatically reset (this action corresponds to the CN_CLEAR_RESET job - see CMD = 5). |  |  |  |
| **RESULT (for CMD = 1)** |  |  | **Value / meaning** |  |
| **Parameter** | **Hex value/range** | **Bit** |  |  |
| RESULT1 | 0000 000*<sub>H</sub> | Bits 0-3: Codes for the send direction  (excluded values: 0x2) |  |  |
| Bit 0 | Connection Type  - 0: No send and receive connection - 1: Connection reserved for send and receive jobs |  |  |  |
| Bit 1 | Status of current job  - 0: No send job being executed - 1: Send job being executed |  |  |  |
| Bits 2+3 | Previous job:   - 00: No information available on previous send job - 01: previous send job completed successfully - 10: previous send job not completed successfully |  |  |  |

| CMD | Meaning |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | CN_STATUS – connection status **(continued for CMD=1)**  This command returns the status of the connection selected with the ID.  The CP is selected in the LADDR parameter.   If bit 15 (reset ID) is set, this is automatically reset (this action corresponds to the CN_CLEAR_RESET job - see CMD = 5). |  |  |  |
| **RESULT (for CMD = 1)** |  |  | **Value / meaning** |  |
| **Parameter** | **Hex value/range** | **Bit** |  |  |
| RESULT1 | 0000 00*0<sub>H</sub> | Bits 4−7: Codes for the receive direction (excluded values: 0x2) |  |  |
| Bit 4 | Connection Type  - 0: No send and receive connection - 1: Connection reserved for send and receive jobs |  |  |  |
| Bit 5 | Status of current job  - 0: No receive job being executed - 1: Receive job being executed |  |  |  |
| Bits 6+7 | Previous job:   - 00: No information available on previous receive job - 01: previous receive job completed successfully - 10: previous receive job not completed successfully |  |  |  |

| CMD | Meaning |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | CN_STATUS – connection status **(continued for CMD=1)**  This command returns the status of the connection selected with the ID.  The CP is selected in the LADDR parameter.   If bit 15 (reset ID) is set, this is automatically reset (this action corresponds to the CN_CLEAR_RESET job - see CMD = 5). |  |  |  |
| **RESULT (for CMD = 1)** |  |  | **Value / meaning** |  |
| **Parameter** | **Hex value/range** | **Bit** |  |  |
| RESULT1 | 0000 0*00<sub>H</sub> | Bits 8-11: Codes for FETCH/WRITE (excluded values: 0x3, 0x7, 0x8, 0xB, 0xF) |  |  |
| Bit 8 | Connection type:   - 0: No FETCH connection - 1: Connection reserved for FETCH jobs |  |  |  |
| Bit 9 | Connection type:   - 0: No WRITE connection - 1: Connection reserved for WRITE jobs |  |  |  |
| Bit 10 | Job status (FETCH/WRITE):  - 0: Job status OK - 1: Job status NOT OK This ID is set in the following situations:   - The job was acknowledged negatively by the CPU   - The job could not be forwarded to the CPU because the connection was in the "LOCKED" status.   - The job was rejected because the FETCH/WRITE header did not have the correct structure. |  |  |  |
| Bit 11 | Status of FETCH/WRITE job  - 0: No job active - 1: Job from LAN active |  |  |  |

| CMD | Meaning |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | CN_STATUS – connection status **(continued for CMD=1)**  This command returns the status of the connection selected with the ID.  The CP is selected in the LADDR parameter.   If bit 15 (reset ID) is set, this is automatically reset (this action corresponds to the CN_CLEAR_RESET job - see CMD = 5). |  |  |  |
| **RESULT (for CMD = 1)** |  |  | **Value / meaning** |  |
| **Parameter** | **Hex value/range** | **Bit** |  |  |
| RESULT1 | 0000 *000<sub>H</sub> | Bits 12-15: General CP information  (excluded values: 0x3, 0xB) |  |  |
| Bit 12 + 13 | Information on connection status:  (only available for SEND/RECV connections based on the ISO/RFC/TCP protocols, with UDP, the corresponding internal information is output)  - 00: Connection is terminated - 01: Connection establishment active - 10: Connection termination active - 11: Connection is established |  |  |  |
| Bit 14 | CP information:   - 0: CP in STOP - 1: CP in RUN |  |  |  |
| Bit 15 | Reset ID  - 0: AG_CNTEX has not yet reset a connection or the reset ID was cleared. - 1: AG_CNTEX caused a connection reset. |  |  |  |
| RESULT1 | **** 0000<sub>H</sub> |  | Bits 16-31: Reserved 0 – reserved for later expansions |  |
| RESULT2 | 0000 0000<sub>H</sub> |  | - reserved for later expansions |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 2 | CN_RESET – connection reset  This command resets the connection selected with ID.  The CP is selected in the LADDR parameter.   Resetting the connection means that a connection is aborted and established again (active or passive depending on the configuration). Data that has been received but not yet entered in the user program when the connection aborts is deleted.  An entry is also generated in the diagnostics buffer in which the job result can be found. |  |  |
| **RESULT (for CMD = 2)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The reset job was transferred to the CP successfully.   The connection abort and subsequent connection establishment were triggered. |  |
| 0000 0002<sub>H</sub> | The reset job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 3 | CN_STATUS_ALL – all connections status  This command returns the connection status of all connections (established/terminated) in the RESULT1/2 parameters (at total of 8 bytes of group information).  The ID parameter must be set to "0" (checked for 0).  The CP is selected in the LADDR parameter.   When necessary, you can obtain detailed information about a terminated or unconfigured connection using a further connection status call with CMD=1. |  |  |
| **RESULT (for CMD = 3)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | **** ****<sub>H</sub>  32 bits with the following validity:  - For S7-400: Bits 0-31 for connections 1 - 32 - For S7-300: Bits 0-15 for connections 1 - 16 | For the relevant connection:  - 0 – connection terminated / not configured - 1 – connection established |  |
| RESULT2 | **** ****<sub>H</sub>  32 bits with the following validity:  - For S7-400: Bits 0-31 for connections 33 - 64 | For the relevant connection:  - 0 – connection terminated / not configured - 1 – connection established |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 4 | CN_RESET_ALL – all connections reset  This command resets all connections.  The ID parameter must be set to "0" (checked for 0).  The CP is selected in the LADDR parameter.   Resetting the connections means that connections are aborted and established again (active or passive depending on the configuration). Data that has been received but not yet entered in the user program when the connection aborts is deleted.  An entry is also generated in the diagnostics buffer in which the job result can be found. |  |  |
| **RESULT (for CMD = 4)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The reset job was transferred to the CP successfully. The connection abort and subsequent connection establishment of all connections were triggered. |  |
| RESULT1 | 0000 0002<sub>H</sub> | The reset job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 5 | CN_CLEAR_RESET - Clear the reset ID  This command resets the reset ID (bit 15 in RESULT1) for the connection selected with ID.  The CP is selected in the LADDR parameter.   This job executes automatically when the connection status is read (CMD=1); the separate job described here is therefore only required in special situations. |  |  |
| **RESULT (for CMD = 5)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The clear job was transferred to the CP successfully. |  |
| RESULT1 | 0000 0002<sub>H</sub> | The Clear job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 6 | CN_DISCON − connection disconnect  This command resets the connection selected with ID and LADDR.  Resetting the connection is achieved by aborting the connection.  Any data in the stack is lost without any message being displayed. The connection is not established again automatically afterwards. The connection can be established again with the CN_STARTCON control job. A diagnostics buffer entry is created in which you will find the job result. |  |  |
| **RESULT (for CMD = 6)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The job was transferred to the CP successfully. The connection abort was initiated. |  |
| RESULT1 | 0000 0002<sub>H</sub> | The job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 7 | CN_STARTCON − start connection  This command establishes a connection selected with ID and LADDR and aborted earlier with the control job CN_DISCON. A diagnostics buffer entry is created in which you will find the job result. |  |  |
| **RESULT (for CMD = 7)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The connection establishment job was transferred to the CP successfully. The connection establishment was initiated. |  |
| RESULT1 | 0000 0002<sub>H</sub> | The connection establishment job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 8 | PING_REQUEST - Send a PING request  This command sends a PING command to the CP. The CP then initiates 4 PING echo requests to the specified IP address. |  |  |
| **RESULT (for CMD = 8)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The ping request was sent to the CP successfully. |  |
| RESULT2 | 0000 0002<sub>H</sub> | The ping request could not be sent to the CP because the corresponding service was not available on the CP.  A possible cause might, for example, be: CP in STOP mode |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 9 | PING_RESULT - Query ping result  This command sends a PING result request to the CP. The CP transfers the results of the 4 executed PING echo requests in the RESULT parameter.  The call is successful when the 4 ping echo requests have been completed on the part of the CP. |  |  |
| **RESULT (for CMD = 9)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | **** ****<sub>H</sub> | 1. Word:  Reply time in ms for the 1st PING echo request.  2. Word:  Reply time in ms for the 2nd PING echo request.  Example:  0005 FFFF<sub>H</sub> Echo 1 -> received after 5 ms  Echo 2 -> no echo in the set monitoring time |  |
| RESULT2 | **** ****<sub>H</sub> | 1. Word:  Reply time in ms for the 3rd PING echo request.  2. Word:  Reply time in ms for the 4th PING echo request.  Example:  0002 3456<sub>H</sub> Echo 3 -> received after 2 ms  Echo 4 -> received after 13398 ms |  |
| Range of values for data words in RESULT1 / RESULT 2: |  |  |  |
|  | 0000<sub>H</sub> | not used |  |
| 0001<sub>H </sub>... EA60<sub>H</sub> | Reply time in ms  0001<sub>H </sub>= 1 ms EA60<sub>H </sub>= 60000 ms |  |  |
| EA61<sub>H </sub>... FFFE<sub>H</sub> | not used |  |  |
| FFFF<sub>H</sub> | Timeout: No echo within the specified monitoring time. |  |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 10 | CONN_TYPE - Connection type  This command requests the CP to specify the current connection type for the specified connection ID. |  |  |
| **RESULT (for CMD = 10)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 000*<sub>H</sub> | The request returns the following values for the possible connection types:  0: no connection set up 1: UDP connection 2: SMTP connection 3: TCP connection 4: Free UDP connection 5: FTP connection 6: ISO transport connection 7: ISO­on­TCP connection |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

###### See also

You will find further information in the FAQ under the following entry ID: [http://support.automation.siemens.com/WW/view/en/33414377](http://support.automation.siemens.com/ww/view/en/33414377)

---

**See also**

[AG_CNTEX (S7-300, S7-400)](#ag_cntex-s7-300-s7-400-1)
  
[How the PING function works (S7-300, S7-400)](#how-the-ping-function-works-s7-300-s7-400)

#### AG_CNTRL for connection diagnostics (S7-300, S7-400)

This section contains information on the following topics:

- [AG_CNTRL (S7-300, S7-400)](#ag_cntrl-s7-300-s7-400)
- [Parameters for AG_CNTRL (S7-300, S7-400)](#parameters-for-ag_cntrl-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-2)
- [Commands and job results for AG_CNTRL (S7-300, S7-400)](#commands-and-job-results-for-ag_cntrl-s7-300-s7-400)

##### AG_CNTRL (S7-300, S7-400)

###### Description

With the AG_CNTRL instruction, you can diagnose connections. When necessary, you can initialize connection establishment again using the instruction.

> **Note**
>
> **AG_CNTRL and AG_CNTEX**
>
> The AG_CNTEX instruction provides expanded functionality compared with the AG_CNTRL instruction.
>
> All the functions of AG_CNTRL are included in AG_CNTEX and they can be used identically in the user program.

The following actions are possible by setting commands:

- Reading out connection information

  Based on status information, you can decide whether or not it would be useful to reset all or individual connections of the CP.
- Resetting configured connections

  You can reset individual connections or all connections of a CP.
- Aborting the active connection and establishing it again

The commands of the AG_CNTRL instruction are permitted only for SEND/RECV connections based on the ISO / RFC / TCP / UDP protocols.

###### Call interface

Call interface in FBD representation

![Call interface](images/12881729803_DV_resource.Stream@PNG-de-DE.png)

###### Further information

FAQ under entry ID [33414377](http://support.automation.siemens.com/WW/view/de/33414377)

---

**See also**

[Parameters for AG_CNTRL (S7-300, S7-400)](#parameters-for-ag_cntrl-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-2)
  
[Commands and job results for AG_CNTRL (S7-300, S7-400)](#commands-and-job-results-for-ag_cntrl-s7-300-s7-400)

##### Parameters for AG_CNTRL (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for AG_CNTRL:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| ACT | INPUT | BOOL | 0, 1 | AG_UNLOCK must be called with ACT=1.  If it is called with ACT=0, there is no function call and the instruction is exited again immediately. |
| ID | INPUT | INT | - 1, 2, .., n,  or  - 0 | The connection number of the connection is specified in the parameter ID. The connection number can be found in the configuration. n is the maximum number of connections and is dependent on the product (S7-300 or S7-400).  If the call addresses all connections (_ALL function with CMD 3 or 4), 0 must be specified as the ID. |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP with STEP 7, the module start address is displayed in the configuration table. Specify this address here. |
| CMD | INPUT | INT |  | Command to AG_CNTRL. |
| DONE | OUTPUT | BOOL | 0:  Job still being processed or not yet triggered  1:  Job done | This parameter indicates whether or not the job was completed without errors.  For the meaning in conjunction with the parameters ERROR and STATUS, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-2)  Note:  If DONE=1, RESULT can be evaluated |
| ERROR | OUTPUT | BOOL | 0: No error  1: Error | Error code  For the meaning in conjunction with the parameters DONE and STATUS, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-2) |
| STATUS | OUTPUT | WORD |  | Status code  For the meaning in conjunction with the parameters DONE and ERROR, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-2) |
| RESULT1 | OUTPUT | DWORD |  | Information returned according to the command sent to AG_CNTRL. |
| RESULT2 | OUTPUT | DWORD |  | Only to be evaluated for S7-400:  Part 2 of the information returned according to the command sent to AG_CNTRL. |

---

**See also**

[AG_CNTRL (S7-300, S7-400)](#ag_cntrl-s7-300-s7-400)

##### Parameters DONE, ERROR, STATUS (S7-300, S7-400)

###### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

The command results in the RESULT1/2 parameters must also be evaluated according to "[Commands and job results for AG_CNTRL](#commands-and-job-results-for-ag_cntrl-s7-300-s7-400)".

AG_CNTRL codes

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 1 | 0 | 0000<sub>H</sub> | A job (CMD) was transferred successfully to the CP (for example RESET) or a status was read successfully from the CP.  The RESULT1/2 parameters can be evaluated. |
| 0 | 0 | 0000<sub>H</sub> | There has been no instruction call yet or the instruction was called with ACT=0. |
| 0 | 0 | 8181<sub>H</sub> | Job active  The instruction call must be repeated with the same parameters until DONE or ERROR is signaled. |
| 0 | 1 | 8183<sub>H</sub> | No configuration or the service has not yet started on the Ethernet CP. |
| 0 | 1 | 8186<sub>H</sub> | The ID parameter is invalid. The permitted ID depends on the selected command; see CMD parameter in "[Commands and job results for AG_CNTRL](#commands-and-job-results-for-ag_cntrl-s7-300-s7-400)" |
| 0 | 1 | 8187<sub>H</sub> | The CMD parameter is invalid. |
| 0 | 1 | 8188<sub>H</sub> | Sequence error in the ACT control (Note: this code does not occur in the product version of the CP / firmware). |
| 0 | 1 | 8189<sub>H</sub> | The CP version / firmware used does not support AG_CNTRL.  The code is set when you call a CP 3431-EX20 with firmware as of V1.3.9; with other CP types, the code 80B0H is set instead.  Note: AG_CNTRL in version V1.0 is supported by the CPs as of CP 343-1EX21/GX21; this code does not occur with these modules. |
| 0 | 1 | 8090<sub>H</sub> | - No module with this module start address exists.  or  - The instruction being used does not match the system family being used (remember to use different instructions for S7­300 and S7­400).   or  - The function is not supported by this module. |
| 0 | 1 | 8091<sub>H</sub> | The module start address is not at a double­word boundary. |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established. The corresponding CPU in the H system is in STOP mode. |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | CPU resources (memory) occupied. |
| 0 | 1 | 80C4<sub>H</sub> | Communications error  The error occurs temporarily; it is usually best to repeat the job in the user program. |
| 0 | 1 | 80D2<sub>H</sub> | The module start address is incorrect. |

---

**See also**

[AG_CNTRL (S7-300, S7-400)](#ag_cntrl-s7-300-s7-400)

##### Commands and job results for AG_CNTRL (S7-300, S7-400)

###### Commands and evaluating the job results

The following table shows you the possible commands and the results that can be evaluated in the RESULT1/2 parameters.

Commands to AG_CNTRL

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 0 | NOP – no operation  AG_CNTRL executes without a job being sent to the CP. |  |  |
| **RESULT (for CMD = 0)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | Executed without error |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | CN_STATUS – connection status  This command returns the status of the connection selected with the ID.  The CP is selected in the LADDR parameter.   If bit 15 (reset ID) is set, this is automatically reset (this action corresponds to the CN_CLEAR_RESET job - see CMD = 5). |  |  |  |
| **RESULT (for CMD = 1)** |  |  | **Value / meaning** |  |
| **Parameter** | **Hex value/range** | **Bit** |  |  |
| RESULT1 | 0000 000*<sub>H</sub> | Bits 0-3: Codes for the send direction  (excluded values: 0x2) |  |  |
| Bit 0 | Connection Type  - 0: No send and receive connection - 1: Connection reserved for send and receive jobs |  |  |  |
| Bit 1 | Status of current job  - 0: No send job being executed - 1: Send job being executed |  |  |  |
| Bits 2+3 | Previous job:   - 00: No information available on previous send job - 01: previous send job completed successfully - 10: previous send job not completed successfully |  |  |  |

| CMD | Meaning |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | CN_STATUS – connection status **(CMD=1 continued)**  This command returns the status of the connection selected with the ID.  The CP is selected in the LADDR parameter.   If bit 15 (reset ID) is set, this is automatically reset (this action corresponds to the CN_CLEAR_RESET job - see CMD = 5). |  |  |  |
| **RESULT (for CMD = 1)** |  |  | **Value / meaning** |  |
| **Parameter** | **Hex value/range** | **Bit** |  |  |
| RESULT1 | 0000 00*0<sub>H</sub> | Bits 4−7: Codes for the receive direction (excluded values: 0x2) |  |  |
| Bit 4 | Connection Type  - 0: No send and receive connection - 1: Connection reserved for send and receive jobs |  |  |  |
| Bit 5 | Status of current job  - 0: No receive job being executed - 1: Receive job being executed |  |  |  |
| Bits 6+7 | Previous job:   - 00: No information available on previous receive job - 01: previous receive job completed successfully - 10: previous receive job not completed successfully |  |  |  |

| CMD | Meaning |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | CN_STATUS – connection status **(CMD=1 continued)**  This command returns the status of the connection selected with the ID.  The CP is selected in the LADDR parameter.   If bit 15 (reset ID) is set, this is automatically reset (this action corresponds to the CN_CLEAR_RESET job - see CMD = 5). |  |  |  |
| **RESULT (for CMD = 1)** |  |  | **Value / meaning** |  |
| **Parameter** | **Hex value/range** | **Bit** |  |  |
| RESULT1 | 0000 0*00<sub>H</sub> | Bits 8-11: Codes for FETCH/WRITE (excluded values: 0x3, 0x7, 0x8, 0xB, 0xF) |  |  |
| Bit 8 | Connection type:   - 0: No FETCH connection - 1: Connection reserved for FETCH jobs |  |  |  |
| Bit 9 | Connection type:   - 0: No WRITE connection - 1: Connection reserved for WRITE jobs |  |  |  |
| Bit 10 | Job status (FETCH/WRITE):  - 0: Job status OK - 1: Job status NOT OK This ID is set in the following situations:   - The job was acknowledged negatively by the CPU   - The job could not be forwarded to the CPU because the connection was in the "LOCKED" status.   - The job was rejected because the FETCH/WRITE header did not have the correct structure. |  |  |  |
| Bit 11 | Status of FETCH/WRITE job  - 0: No job active - 1: Job from LAN active |  |  |  |

| CMD | Meaning |  |  |  |
| --- | --- | --- | --- | --- |
| 1 | CN_STATUS – connection status **(CMD=1 continued)**  This command returns the status of the connection selected with the ID.  The CP is selected in the LADDR parameter.   If bit 15 (reset ID) is set, this is automatically reset (this action corresponds to the CN_CLEAR_RESET job - see CMD = 5). |  |  |  |
| **RESULT (for CMD = 1)** |  |  | **Value / meaning** |  |
| **Parameter** | **Hex value/range** | **Bit** |  |  |
| RESULT1 | 0000 *000<sub>H</sub> | Bits 12-15: General CP information  (excluded values: 0x3, 0xB) |  |  |
| Bit 12 + 13 | Information on connection status:  (only available for SEND/RECV connections based on the ISO/RFC/TCP protocols, with UDP, the corresponding internal information is output)  - 00: Connection is terminated - 01: Connection establishment active - 10: Connection termination active - 11: Connection is established |  |  |  |
| Bit 14 | CP information:   - 0: CP in STOP - 1: CP in RUN |  |  |  |
| Bit 15 | Reset ID  - 0: AG_CNTRL has not yet reset a connection or the reset ID was cleared. - 1: The control instruction caused a connection reset. |  |  |  |
| RESULT1 | **** 0000<sub>H</sub> |  | Bits 16-31: Reserved 0 – reserved for later expansions |  |
| RESULT2 | 0000 0000<sub>H</sub> |  | - reserved for later expansions |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 2 | CN_RESET – connection reset  This command resets the connection selected with ID.  The CP is selected in the LADDR parameter.   Resetting the connection means that a connection is aborted and established again (active or passive depending on the configuration). Data that has been received but not yet entered in the user program when the connection aborts is deleted.  An entry is also generated in the diagnostics buffer in which the job result can be found. |  |  |
| **RESULT (for CMD = 2)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The reset job was transferred to the CP successfully.   The connection abort and subsequent connection establishment were triggered. |  |
| 0000 0002<sub>H</sub> | The reset job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 3 | CN_STATUS_ALL – all connections status  This command returns the connection status of all connections (established/terminated) in the RESULT1/2 parameters (at total of 8 bytes of group information).  The ID parameter must be set to "0" (checked for 0).  The CP is selected in the LADDR parameter.   When necessary, you can obtain detailed information about a terminated or unconfigured connection using a further connection status call with CMD=1. |  |  |
| **RESULT (for CMD = 3)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | **** ****<sub>H</sub> | 32 bits: Connection 1 - 32   - 0 – connection terminated / not configured - 1 – connection established |  |
| RESULT2 | **** ****<sub>H</sub> | 32 bits: Connection 33 - 64  - 0 – connection terminated / not configured - 1 – connection established |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 4 | CN_RESET_ALL – all connections reset:  This command resets all connections.  The ID parameter must be set to "0" (checked for 0).  The CP is selected in the LADDR parameter.   Resetting the connections means that connections are aborted and established again (active or passive depending on the configuration). Data that has been received but not yet entered in the user program when the connection aborts is deleted.  An entry is also generated in the diagnostics buffer in which the job result can be found. |  |  |
| **RESULT (for CMD = 4)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The reset job was transferred to the CP successfully. The connection abort and subsequent connection establishment of all connections were triggered. |  |
| RESULT1 | 0000 0002<sub>H</sub> | The reset job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 5 | CN_CLEAR_RESET – Clear the reset ID  This command resets the reset ID (bit 15 in RESULT1) for the connection selected with ID.  The CP is selected in the LADDR parameter.   This job executes automatically when the connection status is read (CMD=1); the separate job described here is therefore only required in special situations. |  |  |
| **RESULT (for CMD = 5)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The clear job was transferred to the CP successfully. |  |
| RESULT1 | 0000 0002<sub>H</sub> | The Clear job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 6 | CN_DISCON − connection disconnect  This command resets the connection selected with ID and LADDR.  Resetting the connection is achieved by aborting the connection.  Any data in the stack is lost without any message being displayed. The connection is not established again automatically afterwards. The connection can be established again with the CN_STARTCON control job. A diagnostics buffer entry is created in which you will find the job result. |  |  |
| **RESULT (for CMD = 6)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The job was transferred to the CP successfully. The connection abort was initiated. |  |
| RESULT1 | 0000 0002<sub>H</sub> | The job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

| CMD | Meaning |  |  |
| --- | --- | --- | --- |
| 7 | CN_STARTCON − start connection  This command establishes a connection selected with ID and LADDR and aborted earlier with the control job CN_DISCON. A diagnostics buffer entry is created in which you will find the job result. |  |  |
| **RESULT (for CMD = 6)** |  | **Meaning** |  |
| **Parameter** | **Hex value/range** |  |  |
| RESULT1 | 0000 0001<sub>H</sub> | The connection establishment job was transferred to the CP successfully. The connection establishment was initiated. |  |
| RESULT1 | 0000 0002<sub>H</sub> | The connection establishment job could not be transferred to the CP because the service has not started on the CP (for example, CP in STOP). |  |
| RESULT2 | 0000 0000<sub>H</sub> | Default |  |

###### Further information

You will find further information in the FAQ under the following entry ID: [33414377](http://support.automation.siemens.com/WW/view/en/33414377)

---

**See also**

[AG_CNTRL (S7-300, S7-400)](#ag_cntrl-s7-300-s7-400)

### Instructions for PROFINET IO (S7-300)

This section contains information on the following topics:

- [Instructions for PROFINET IO (S7-300)](#instructions-for-profinet-io-s7-300-1)
- [Instructions for cyclic transmission of user data (S7-300)](#instructions-for-cyclic-transmission-of-user-data-s7-300)
- [PNIO_RW_REC (S7-300)](#pnio_rw_rec-s7-300)
- [PNIO_Alarm (S7-300)](#pnio_alarm-s7-300)
- [PROFIenergy (S7-300)](#profienergy-s7-300)

#### Instructions for PROFINET IO (S7-300)

##### Overview

The instructions listed below are available for transferring data cyclically on the PROFINET IO interface. The significance of the instructions differs depending on how you use the CP (as a PROFINET IO controller or PROFINET IO device) in an S7 station.

| Instruction | can be used with: |  | Meaning |
| --- | --- | --- | --- |
| **S7-300** | **S7-400** |  |  |
| PNIO_SEND | x | - | Depending on the mode of the CP:  - On a PROFINET IO controller Sending output data to the PROFINET IO devices. - On a PROFINET IO device Forwarding process input data to the PROFINET IO controller. |
| PNIO_RECV | x | - | Depending on the mode of the CP:  - On a PROFINET IO controller Receiving process input data from the PROFINET IO devices. - On a PROFINET IO device Receiving process output data from the PROFINET IO controller. |

For CPs operating as PROFINET IO controller and IO device at the same time, the instructions are available as of version 2.0.

The instructions listed below are available for transferring data (data records, interrupt information) acyclically on the PROFINET IO interface. The two instructions can only be used in PROFINET IO controller mode.

| Instruction | can be used with: |  | Meaning |
| --- | --- | --- | --- |
| **S7-300** | **S7-400** |  |  |
| PNIO_RW_REC | x | - | - Read data record (from a PROFINET IO device) - Write data record (to a PROFINET IO device) |
| PNIO_ALARM | x | - | Receive alarm information from the PROFINET IO devices |

#### Instructions for cyclic transmission of user data (S7-300)

This section contains information on the following topics:

- [PNIO_SEND (S7-300)](#pnio_send-s7-300)
- [PNIO_RECV (S7-300)](#pnio_recv-s7-300)
- [General characteristics of the instructions for PROFINET IO (S7-300)](#general-characteristics-of-the-instructions-for-profinet-io-s7-300)
- [Data consistency (S7-300)](#data-consistency-s7-300)
- [Substitute values (S7-300)](#substitute-values-s7-300)

##### PNIO_SEND (S7-300)

This section contains information on the following topics:

- [PNIO_SEND (S7-300)](#pnio_send-s7-300-1)
- [Parameters for PNIO_SEND (S7-300)](#parameters-for-pnio_send-s7-300)
- [Parameters DONE, ERROR, STATUS (IE) (S7-300)](#parameters-done-error-status-ie-s7-300)

###### PNIO_SEND (S7-300)

###### Description

The PNIO_SEND instruction is used to transfer data in the PROFINET IO controller or PROFINET IO device modes of the CP.

- Operating as PROFINET IO controller  
  The instruction transfers the process data (outputs) of a specified output area to the CP to be forwarded to PROFINET IO devices and as status display returns the IO consumer status (IOCS) of the outputs of the PROFINET IO devices.
- Operation as PROFINET IO device  
  The instruction reads the preprocessed inputs of the CPU on the PROFINET IO device and transfers them to the PROFINET IO controller (configured I-addresses). In addition to this, the instruction also returns the IO Consumer Status (IOCS) of the PROFINET IO controller as a status code.

The preprocessed process data is available in a DB or bit memory area.

For CPs operating as PROFINET IO controller and IO device at the same time, the instruction is available as of version 2.0. With the additional MODE parameter, you set the mode for which the instruction will be called.

###### Call interface (version 2.0)

Call interface in FBD representation

![Call interface (version 2.0)](images/12881748747_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[General characteristics of the instructions for PROFINET IO (S7-300)](#general-characteristics-of-the-instructions-for-profinet-io-s7-300)
  
[Data consistency (S7-300)](#data-consistency-s7-300)
  
[Parameters for PNIO_SEND (S7-300)](#parameters-for-pnio_send-s7-300)
  
[Parameters DONE, ERROR, STATUS (IE) (S7-300)](#parameters-done-error-status-ie-s7-300)

###### Parameters for PNIO_SEND (S7-300)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the PNIO_SEND function:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD | - | Module start address |
| MODE  (parameters version 2.0 or later) | INPUT | BYTE | Values for X:  - 0Y<sub>H</sub>: Status bits are transferred in IOCS. - 8Y<sub>H</sub>: Restriction to group message in CHECK_IOCS; no status bits in IOCS.   Values for Y:  - X0<sub>H</sub>:   - IO controller mode   - IO device mode (without parallel operation)There is compatibility with the instruction in version 1.0. - X1<sub>H</sub>: IO device mode (with parallel operation) | Specified in the form XY (hexadecimal):  - X sets the transfer of status information. - Y specifies the mode of the CP as IO controller or IO device.   Notes on compatibility;:  - The version 1.0 instruction can continue to be used as long as the CP is not being operated as an IO controller and IO device at the same time. - When MODE=0, the instruction as of version 2.0 behaves like the instruction version 1.0. |
| SEND | IN_OUT | ANY (as VARTYPE only BYTE is permitted) | The address of the data area points to one of the alternatives:  - Memory bit area - Data block area | Specifies the address and length   **IO controller mode:**   The length should match the total length of the distributed IO configured, whereby address gaps are also transmitted.  The length can also be shorter than the total length of the distributed IO, for example when the instruction is called more than once in one OB. It must, however, have the total length in at least one call.    **IO device mode:**   The data structure results from the order of the slots of the input modules configured for this PROFINET IO device on the PROFINET IO controller line and their length without address gaps.  (Please note the more extensive explanations or examples for your CP in the device­specific Part B of this manual)  Notes:  - The instruction begins to transfer the data at address 0 regardless of how you configured the addresses (regardless of the lowest configured address). - Specifying an I/O area is not permitted since you must first check the IOCS for GOOD before data can be accepted in the I/O. |
| LEN | INPUT | INT | Value > 0  The maximum total length of the data areas to be transferred can be found in the device­specific Part B of the device manual in the "Performance data" chapter. This may differ for controller or device mode. | Length of the data area to be transferred in bytes.  The transfer of the data always begins with address 0 regardless of the configuration. Please note that the IO address "0" with a length of 1 is included.   **IO controller mode:**   - The highest configured address of the devices must be specified here. The individual areas are not grouped together. If the instruction is called more than once, LEN can also be shorter than the highest address. The highest address should be specified in at least one call (compare "SEND" parameter). - The data is transferred in the order of the logical addresses (as with PROFIBUS DP).    **IO device mode:**   - The data is transferred in the order of the slots corresponding to the configuration of the input modules on the PROFINET IO controller line for this PROFINET IO device.   Note: Make sure that the length programmed here and the configuration of the PROFINET IO controller are consistent. The entire data area length including any gaps is transferred for the device. |
| DONE | OUTPUT | BOOL | 0: - 1: New data accepted | This parameter indicates whether or not the job was completed without errors. |
| ERROR | OUTPUT | BOOL | 0: -1: Error | Error code |
| STATUS | OUTPUT | WORD | - | Status code |
| CHECK_IOCS | OUTPUT | BOOL | 0: All IOCS set to GOOD  1: At least one IOCS set to BAD | Auxiliary bit that indicates whether or not it is necessary to evaluate the IOCS status area. |
| IOCS | OUTPUT | ANY (as VARTYPE only BYTE is permitted) | The address of the data area points to one of the alternatives:  - Memory bit area - Data block area   Length:  For the maximum value, refer to the device­specific Part B of this manual in the section "Performance data". This may differ for controller or device mode. | A status bit is transferred per byte of user data.  The length information depends on the length in the LEN parameter (one bit per byte)  = (Length LEN + 7/ 8)  Controller mode: Address gaps are also transferred according to the SEND parameter.  Address gaps are transferred with the status GOOD.  Device mode: Address gaps are not transferred.  The instruction begins the transfer of the status for address 0.  Note: The minimum length of the ANY pointer is (length LEN + 7/8) |

> **Note**
>
> Remember that all output parameters may only be evaluated when the instruction signals either DONE = 1 or ERROR = 1.

> **Note**
>
> You must assume that the returned IOCS status does not arrive time­synchronized with the data (SEND parameter) but delayed by one user program cycle. This means: User data and IOCS are not consistent.

---

**See also**

[PNIO_SEND (S7-300)](#pnio_send-s7-300-1)

###### Parameters DONE, ERROR, STATUS (IE) (S7-300)

###### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information in the STEP 7 Standard and System Functions reference manual. The chapter describing error evaluation with the RET_VAL output parameter contains detailed information.
>
> To find out which system instructions are used and are relevant for error evaluation, display the properties dialog of the instruction described here in the "Calls" tab.

Condition codes PNIO_SEND

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | 8180<sub>H</sub> | - Data transfer active;  or  - The CP is in STOP mode. |
| 0 | 0 | 8181<sub>H</sub> | Module does not support version 2.0 of the instruction  Solution: Use version 1.0. |
| 1 | 0 | 0000<sub>H</sub> | New data transferred without error. |
| 0 | 1 | 8183<sub>H</sub> | - PROFINET IO configuration missing;  or  - wrong CPLADDR;   or  - The CP is in STOP mode.   or  - Interconnection of MODE does not match module configuration or incorrect interconnection with MODE > 1   Extra in device mode:  - The connection between PROFINET IO controller and PROFINET IO device is down,   or  - PROFINET IO controller not reachable   or  - Total lengths (configuration and LEN parameter) are not consistent. |
| 0 | 1 | 8184<sub>H</sub> | System error or bad parameter type. |
| 0 | 1 | 8185<sub>H</sub> | Parameter LEN is greater than source area SEND or target buffer (IOCS) is too small. |
| 0 | 1 | 8F22<sub>H</sub> | Area length error reading a parameter (e.g. DB too short). |
| 0 | 1 | 8F23<sub>H</sub> | Area length error writing a parameter (e.g. DB too short). |
| 0 | 1 | 8F24<sub>H</sub> | Range error when reading a parameter. |
| 0 | 1 | 8F25<sub>H</sub> | Range error when writing a parameter. |
| 0 | 1 | 8F28<sub>H</sub> | Alignment error when reading a parameter. |
| 0 | 1 | 8F29<sub>H</sub> | Alignment error when writing a parameter. |
| 0 | 1 | 8F30<sub>H</sub> | Parameter is in the write-protected 1st current data block. |
| 0 | 1 | 8F31<sub>H</sub> | Parameter is in the write-protected 2nd current data block. |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F3A<sub>H</sub> | Destination area is not loaded (DB). |
| 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the I/O area. |
| 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the I/O area. |
| 0 | 1 | 8F44<sub>H</sub> | Access to a parameter to be read during execution of the instruction is prevented. |
| 0 | 1 | 8F45<sub>H</sub> | Access to a parameter to be written during execution of the instruction is prevented. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference. |
| 0 | 1 | 8090<sub>H</sub> | Module with this address does not exist. |
| 0 | 1 | 80A0<sub>H</sub> | Negative acknowledgment writing to the module. |
| 0 | 1 | 80A1<sub>H</sub> | Negative acknowledgment writing to the module. |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | - The specified data record length is incorrect.  or  - The CP changes to STOP. |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | Resources occupied (memory). |
| 0 | 1 | 80C4<sub>H</sub> | Communication error (occurs temporarily, it is usually best to repeat the job in the user program). |

---

**See also**

[PNIO_SEND (S7-300)](#pnio_send-s7-300-1)

##### PNIO_RECV (S7-300)

This section contains information on the following topics:

- [PNIO_RECV (S7-300)](#pnio_recv-s7-300-1)
- [Parameters for PNIO_RECV (S7-300)](#parameters-for-pnio_recv-s7-300)
- [Parameters NDR, ERROR, STATUS (IE) (S7-300)](#parameters-ndr-error-status-ie-s7-300)

###### PNIO_RECV (S7-300)

###### Description

The PNIO_RECV instruction is used to receive data in the PROFINET IO controller or PROFINET IO device modes of the CP.

- Operating as PROFINET IO controller  
  The instruction accepts the process data from PROFINET IO devices (inputs of the controller) and transfers the IO provider status (IOPS) from the PROFINET IO devices to the specified input areas.
- Operating as PROFINET IO device  
  The instruction receives the data transferred by the PROFINET IO controller (configured O-addresses) as well as the IO Provider Status (IOPS) of the PROFINET IO controller and writes them to the data areas on the CPU of the PROFINET IO device reserved for the process outputs.

For CPs operating as PROFINET IO controller and IO device at the same time, the instruction is available as of version 2.0. With the additional MODE parameter, you set the mode for which the instruction will be called.

###### Call interface (version 2.0)

Call interface in FBD representation

![Call interface (version 2.0)](images/12881751819_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[General characteristics of the instructions for PROFINET IO (S7-300)](#general-characteristics-of-the-instructions-for-profinet-io-s7-300)
  
[Data consistency (S7-300)](#data-consistency-s7-300)
  
[Parameters for PNIO_RECV (S7-300)](#parameters-for-pnio_recv-s7-300)
  
[Parameters NDR, ERROR, STATUS (IE) (S7-300)](#parameters-ndr-error-status-ie-s7-300)

###### Parameters for PNIO_RECV (S7-300)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the PNIO_RECV instruction:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD | - | Module start address |
| MODE  (parameters version 2.0 or later) | INPUT | BYTE | Values for X:  - 0Y<sub>H</sub>: Status bits are transferred in IOCS. - 8Y<sub>H</sub>: Restriction to group message in CHECK_IOCS; no status bits in IOCS.   Values for Y:  - X0<sub>H:</sub>   - IO controller mode   - IO device mode (without parallel operation)Compatible with instruction in version 1.0 - X1<sub>H</sub>: IO device mode (with parallel operation) | Specified in the form XY (hexadecimal):  - X sets the transfer of status information. - Y specifies the mode of the CP as IO controller or IO device.   Notes on compatibility;:  - The version 1.0 instruction can continue to be used as long as the CP is not being operated as an IO controller and IO device at the same time. - When MODE=0, the instruction as of version 2.0 behaves like the instruction version 1.0. |
| RECV | IN_OUT | ANY (as VARTYPE only BYTE is permitted) | The address of the data area points to one of the alternatives:  - Memory bit area - Data block area | Specifies the address and length  IO controller mode:  The length should match the total length of the distributed IO configured, whereby address gaps are also transmitted.  The length can also be shorter than the total length of the distributed IO, for example when the instruction is called more than once in one OB. It must, however, have the total length in at least one call.  IO device mode:  The data structure results from the order of the slots of the output modules configured for this PROFINET IO device on the PROFINET IO controller line and their length without address gaps.  Notes:  - The instruction begins to transfer the data at address 0 regardless of how you configured the addresses (regardless of the lowest configured address). - Specifying an I/O area is not permitted since you must first change the IOPS for GOOD before data can be accepted in the I/O. |
| LEN | INPUT | INT | Value > 0  The maximum total length of the data to be transferred can be found in Part B of the device manual in the "Performance data" chapter. This may differ for controller or device mode. | Length of the data area to be transferred in bytes.  The transfer of the data always begins with address 0 regardless of the configuration. Please note that the IO address "0" with a length of 1 is included.  IO controller mode:  - The highest configured address of the devices must be specified here. The individual areas are not grouped together. If the instruction is called more than once, LEN can also be shorter than the highest address. The highest address should be specified in at least one call (compare "RECV" parameter). - The data is transferred in the order of the logical addresses (as with PROFIBUS DP).   IO device mode:  - The data is transferred in the order of the slots corresponding to the configuration of the input modules on the PROFINET IO controller line for this PROFINET IO device. - Note: Make sure that the length programmed here and the configuration of the PROFINET IO controller are consistent. The entire data area length including any gaps is transferred for the device. |
| NDR | OUTPUT | BOOL | 0: - 1: Data accepted | This parameter indicates whether or not the job was completed without errors. |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code |
| STATUS | OUTPUT | WORD | - | Status code |
| CHECK_ IOPS | OUTPUT | BOOL | 0: All IOPS set to GOOD  1: At least one IOPS set to BAD | Auxiliary bit that indicates whether or not it is necessary to evaluate the IOPS status area. |
| IOPS | OUTPUT | ANY (as VARTYPE only BYTE is permitted) | The address of the data area points to one of the alternatives:  - Memory bit area - Data block area   Length:  For the maximum value, refer to Part B of the device manual in the section "Performance data". This may differ for controller or device mode. | A status bit is transferred per byte of user data.  The length information depends on the length in the RECV parameter (one bit per byte)   = (Length LEN + 7/ 8)  Controller mode:  Address gaps are also transferred according to the RECV parameter.  Address gaps are transferred with the status GOOD.  Device mode:  Address gaps are not transferred.  The instruction begins the transfer of the status for address 0.  Note:  - The minimum length of the ANY pointer is  (length LEN + 7/8) |
| ADD_INFO | OUTPUT | WORD | Additional Diagnostic Information  In controller mode:  - 0: No alarm - >0: Number of pending alarms   In device mode, the parameter is always = 0. | Parameter expansion  Note: The ADD_INFO parameter is also updated when there are no INPUT addresses configured on the PROFINET IO controller. In this case, the PNIO_RECV instruction is called with a length LEN > 0 (for example LEN = 1 byte). It then transfers an address gap of 1 byte.  The parameter expansion can be used for CPs as of the following firmware version:  - CP 343−1 (EX30) as of firmware V2.0 - CP 343−1 Lean (CX10) as of firmware V2.0 - CP 343−1 Advanced (GX30) as of firmware V1.0   In older firmware versions, the parameter is reserved. |

> **Note**
>
> Remember that all output parameters may only be evaluated when the instruction signals either NDR = 1 or ERROR = 1.

---

**See also**

[PNIO_RECV (S7-300)](#pnio_recv-s7-300-1)

###### Parameters NDR, ERROR, STATUS (IE) (S7-300)

###### Condition codes

The following table shows the codes formed by the NDR, ERROR and STATUS parameters that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information in the STEP 7 Standard and System Functions reference manual. The chapter describing error evaluation with the RET_VAL output parameter contains detailed information.
>
> To find out which system instructions are used and are relevant for error evaluation, display the properties dialog of the instruction described here in the "Calls" tab.

Condition codes PNIO_RECV

| NDR | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | 8180<sub>H</sub> | - Data acceptance active;  or  - The CP is in STOP mode. |
| 0 | 0 | 8181<sub>H</sub> | Module does not support version 2.0 of the instruction.  Solution: Use version 1.0. |
| 1 | 0 | 0000<sub>H</sub> | New data accepted without error. |
| 0 | 1 | 8183<sub>H</sub> | - PROFINET IO configuration missing;  or   - wrong CPLADDR;   or   - The CP is in STOP mode.   or   - Interconnection of MODE does not match module configuration or incorrect interconnection with MODE > 1.     Extra in device mode:  - The connection between PROFINET IO controller and PROFINET IO device is down   or  - PROFINET IO controller not reachable   or  - Total lengths (configuration and LEN parameter) are not consistent |
| 0 | 1 | 8184<sub>H</sub> | System error or bad parameter type. |
| 0 | 1 | 8185<sub>H</sub> | Destination buffer (RECV of IOCS) is too small. |
| 0 | 1 | 8F22<sub>H</sub> | Area length error reading a parameter (e.g. DB too short). |
| 0 | 1 | 8F23<sub>H</sub> | Area length error writing a parameter (e.g. DB too short). |
| 0 | 1 | 8F24<sub>H</sub> | Range error when reading a parameter. |
| 0 | 1 | 8F25<sub>H</sub> | Range error when writing a parameter. |
| 0 | 1 | 8F28<sub>H</sub> | Alignment error when reading a parameter. |
| 0 | 1 | 8F29<sub>H</sub> | Alignment error when writing a parameter. |
| 0 | 1 | 8F30<sub>H</sub> | Parameter is in the write-protected 1st current data block. |
| 0 | 1 | 8F31<sub>H</sub> | Parameter is in the write-protected 2nd current data block. |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F3A<sub>H</sub> | Destination area is not loaded (DB). |
| 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the I/O area. |
| 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the I/O area. |
| 0 | 1 | 8F44<sub>H</sub> | Access to a parameter to be read during execution of the instruction is prevented. |
| 0 | 1 | 8F45<sub>H</sub> | Access to a parameter to be written during execution of the instruction is prevented. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference. |
| 0 | 1 | 8090<sub>H</sub> | Module with this address does not exist. |
| 0 | 1 | 80A0<sub>H</sub> | Negative acknowledgment writing to the module. |
| 0 | 1 | 80A1<sub>H</sub> | Negative acknowledgment writing to the module. |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | - The specified data record length is incorrect.  or  - The CP changes to STOP. |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | Resources occupied (memory). |
| 0 | 1 | 80C4<sub>H</sub> | Communication error (occurs temporarily, it is usually best to repeat the job in the user program). |

---

**See also**

[PNIO_RECV (S7-300)](#pnio_recv-s7-300-1)

##### General characteristics of the instructions for PROFINET IO (S7-300)

###### IO Consumer Status (IOCS) and IO Provider Status (IOPS)

For both communication partners - CPU/CP on the one hand and IO device on the other - there is the status information GOOD or BAD for the data. This status information is transferred parallel to the data. The status of the partner that sends the data is called IOPS (IO Provider Status), the status of the receiving partner is called IOCS (IO Consumer Status).

The IOPS and IOCS status are not necessarily identical. It is, for example, possible that the S7-300 CPU is in STOP mode (output disable or no PROFINET IO instructions active). In this case, the CP as PROFINET IO controller transfers the BAD status to the IO devices.

###### Relationship between instruction call and IO data

- Operation as PROFINET IO controller  
  As a PROFINET IO controller, the CP does not monitor the cyclic calls of the PNIO_SEND/RECV instructions. If the instructions are not called, the last transferred IO data and IOCS/IOPS data are taken as valid.
- Operation as PROFINET IO device  
  PNIO_SEND and PNIO_RECV each have their own watchdog. Depending on the CPU cycle time, the connection to the PROFINET IO controller is terminated if one of the two instructions is no longer called following the initialization phase.

###### Optimizing data transfer (only when operating as PROFINET IO controller)

It is possible to call the instructions with a length (LEN parameter) that is shorter than the configured total length of the IO data on the PNIO chain.

You can use this so that time­critical data is transferred in every CPU cycle whereas non critical data is not transferred in every cycle.

Example:   
You could, for example, transfer only the first data area (time­critical data) in every cycle and the total length of the configured IO data in every second cycle. To do this, place the time­critical data in the lower area (starting at IO address 0) during configuration.

##### Data consistency (S7-300)

The entire input or output data area of the PROFINET IO controller is always transferred in its entirety and is therefore consistent.

- Operating as PROFINET IO controller  
  Regardless of this, using the length information in the instruction call, you can also read or output an input or output area smaller than the configured area consistently.

Note: You should, however, bear in mind that in terms of the "IO user data" within a PROFINET IO system, data consistency can only be guaranteed within the individual IO slots. This applies regardless of the fact that consistent data transfer between CPU and IO controller is guaranteed for the instructions described here.

###### Instruction call

To guarantee data consistency, you may, however, only access the IO data when the instruction has completed free of errors (output parameter NDR = TRUE). You must also check that the IOCS or IOPS status for the data is GOOD.

###### Example

In a normal situation (depending on the total length of the IO data), the instruction will run over several user program cycles until the condition code DONE/NDR = 1 is signaled.

![Example](images/12881754891_DV_resource.Stream@PNG-en-US.png)

Note: The user program cycle and the cycle of the IO data exchange between the PROFINET IO controller and PROFINET IO devices are independent of each other.

##### Substitute values (S7-300)

###### Operational situations

The setting of substitute values is supported for the two following operational situations:

- Substitute values during startup (mode change on the CPU from STOP to RUN)
- Substitute values if problems are detected (remove/insert or station failure/return)

###### Substitute values during startup

You can initialize the outputs with substitute values by setting a memory bit ("start­up" memory bit) in the start­up OB. In cyclic mode (OB1), evaluate this "startup" memory bit to call the PNIO_SEND instruction with the initialization values when appropriate.

###### Substitute values if a problem occurs (only when operating as PROFINET IO controller)

If there is a fault (device/submodule failed), you can find out which submodules have failed by querying the status information IOCS / IOPS status. You then have the option of setting substitute values.

#### PNIO_RW_REC (S7-300)

This section contains information on the following topics:

- [PNIO_RW_REC (S7-300)](#pnio_rw_rec-s7-300-1)
- [Parameters for PNIO_RW_REC (S7-300)](#parameters-for-pnio_rw_rec-s7-300)
- [Parameters DONE, ERROR, STATUS (IE) (S7-300)](#parameters-done-error-status-ie-s7-300-1)

##### PNIO_RW_REC (S7-300)

###### Description

RW_REC is used both for the "read data record" and the "write data record" function in PROFINET IO controller mode. RW_REC can only execute one of the functions at any one time. The "read data record" or "write data record" function is controlled by the WRITE_REC parameter.

Example: The CP can be informed of the location ID and plant designation using the "write data record" function (if this parameter was not already set in the properties dialog of the CP in STEP 7). This is done using the maintenance data record "IM1" with index AFF1H.

You will find details of the supported data records and their structure at the following Internet address:

`http://support.automation.siemens.com/WW/view/en/19289930`

###### Call interface

Call interface in FBD representation:

![Call interface](images/12881757963_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Parameters DONE, ERROR, STATUS (IE) (S7-300)](#parameters-done-error-status-ie-s7-300-1)
  
[Parameters for PNIO_RW_REC (S7-300)](#parameters-for-pnio_rw_rec-s7-300)

##### Parameters for PNIO_RW_REC (S7-300)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the PNIO_RW_REC instruction:

| Parameter | Declaration | Data type | Possible values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD | - | Module start address |
| WRITE_REC | INPUT | BOOL | 0: Read data record 1: Write data record | Job type;  The parameter must not be changed while the instruction is executing. |
| ID | INPUT | WORD |  | Logical address of the PROFINET IO component (module or submodule). For an output module, bit 15 is set  (example of output address 5: ID:=DW#16#8005).  For a mixed module, the lower of the two addresses must be specified. |
| INDEX | INPUT | WORD | See vendor information for the data record numbers supported by the module. | Data record number that the user wants to read or write. |
| DONE | OUTPUT | BOOL | 0: - 1: Data record transferred successfully | This parameter indicates whether or not the job was completed without errors. |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code |
| STATUS | OUTPUT | WORD | 0: No error Different value: Error (see "[Parameters DONE, ERROR, STATUS (IE)](#parameters-done-error-status-ie-s7-300-1)") | Status code |
| LEN | IN_OUT | INT | The maximum length is 480 bytes. | - Read data record:  OUTPUT parameter only; after a successful read, the length of the read data record is indicated; otherwise 0. - Write data record:  INPUT parameter only; length of the data record to be written is entered here by the user. The length must match the definition of the data record. |
| RECORD | IN_OUT | ANY (as VARTYPE, BYTE, WORD and DWORD are permitted) | The address of the data area points to one of the alternatives:  - Memory bit area - Data block area   The length of the ANY pointer must be greater than or equal to the definition of the data record. | - Read data record:  OUTPUT parameter only; after a successful read, the data of the data record is stored here. If the ANY pointer is too short, as much data as possible is transferred. - Write data record:  INPUT parameter only; the data to be written from the data record is stored here by the user. The ANY pointer must be at least as long as specified in the LEN parameter. |

---

**See also**

[PNIO_RW_REC (S7-300)](#pnio_rw_rec-s7-300-1)

##### Parameters DONE, ERROR, STATUS (IE) (S7-300)

###### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

> **Note**
>
> For entries with the coding 8Fxx<sub>H</sub> under STATUS, note the information in the Reference Manual "STEP 7 - System and Standard Functions for S7-300 and S7-400". The chapter describing error evaluation with the RET_VAL output parameter contains detailed information.

PNIO_RW_REC condition codes

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | 8180<sub>H</sub> | Data transfer active |
| 1 | 0 | 0000<sub>H</sub> | Data record transferred successfully |
| 0 | 1 | 8183<sub>H</sub> | - No PROFINET IO controller configuration, - wrong CPLADDR  or  - CP in STOP mode |
| 0 | 1 | 8184<sub>H</sub> | System error or illegal parameter type |
| 0 | 1 | 8185<sub>H</sub> | Destination buffer (RECORD) is too short |
| 0 | 1 | 8F22<sub>H</sub> | Area length error reading a parameter (e.g. DB too short) |
| 0 | 1 | 8F23<sub>H</sub> | Area length error writing a parameter (e.g. DB too short) |
| 0 | 1 | 8F24<sub>H</sub> | Area error reading a parameter |
| 0 | 1 | 8F25<sub>H</sub> | Area error writing a parameter |
| 0 | 1 | 8F28<sub>H</sub> | Orientation error when reading a parameter |
| 0 | 1 | 8F29<sub>H</sub> | Alignment error writing a parameter |
| 0 | 1 | 8F30<sub>H</sub> | Parameter is in the write-protected first active data block |
| 0 | 1 | 8F31<sub>H</sub> | Parameter is in the write-protected second active data block |
| 0 | 1 | 8F32<sub>H</sub> | The DB number in the parameter is too high |
| 0 | 1 | 8F3A<sub>H</sub> | Destination area not loaded (DB) |
| 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the I/O area |
| 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the I/O area |
| 0 | 1 | 8F44<sub>H</sub> | Access to a parameter to be read during execution of the instruction is prevented |
| 0 | 1 | 8F45<sub>H</sub> | Access to a parameter to be written during execution of the instruction is prevented |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference |
| 0 | 1 | 8090<sub>H</sub> | Module with this address does not exist |
| 0 | 1 | 80A0<sub>H</sub> | Negative acknowledgment reading from the module |
| 0 | 1 | 80A1<sub>H</sub> | Negative acknowledgment writing to the module |
| 0 | 1 | 80A3<sub>H</sub> | General PROFINET IO context management error |
| 0 | 1 | 80A9<sub>H</sub> | PROFINET IO device or module reports an illegal type |
| 0 | 1 | 80B0<sub>H</sub> | Module does not recognize the data record |
| 0 | 1 | 80B1<sub>H</sub> | - The specified data record length is incorrect  or  - The CP changes to STOP |
| 0 | 1 | 80B2<sub>H</sub> | The logical address or the configured slot is not in use |
| 0 | 1 | 80B4<sub>H</sub> | PROFINET IO device or module signaling access to an illegal area |
| 0 | 1 | 80B6<sub>H</sub> | PROFINET IO device or module denies access |
| 0 | 1 | 80B8<sub>H</sub> | The module is signaling an illegal parameter |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is being processed |
| 0 | 1 | 80C2<sub>H</sub> | Too many jobs pending |
| 0 | 1 | 80C3<sub>H</sub> | Resources (memory) occupied |
| 0 | 1 | 80C4<sub>H</sub> | Communication error (occurs temporarily, it is usually best to repeat the job in the user program). |

---

**See also**

[PNIO_RW_REC (S7-300)](#pnio_rw_rec-s7-300-1)

#### PNIO_Alarm (S7-300)

This section contains information on the following topics:

- [PNIO_ALARM (S7-300)](#pnio_alarm-s7-300-1)
- [Parameters for PNIO_ALARM (S7-300)](#parameters-for-pnio_alarm-s7-300)
- [Parameters DONE, NEW, ERROR, STATUS (IE) (S7-300)](#parameters-done-new-error-status-ie-s7-300)

##### PNIO_ALARM (S7-300)

###### Description

The PNIO_ALARM instruction is used for evaluation of alarms by a CP 343-1 operating as PROFINET IO controller and should be called in its user program if the parameter ADD_INFO does not equal 0 in PNIO_RECV. After full and error-free transfer of all OUTPUT parameters of the PNIO_ALARM, the received alarms are automatically acknowledged.

The alarms are forwarded to the user program in the chronological order in which they were signaled. Older alarms that have not yet been signaled to the user program and that become invalid due to more recent alarms are not deleted by the newer alarms.

> **Note**
>
> As long as PNIO_ALARM has not yet been called, the alarms are acknowledged automatically (internally) the CP.
>
> If PNIO_ALARM has been called (at least) once in the user program, it must continue to be called to acknowledge pending alarms. This is the situation when the PNIO_RECV instruction signals a value not equal to "0" in the ADD_INFO parameter.
>
> If PNIO_ALARM is no longer called after it has been called once or more in the user program, alarms are not acknowledged and there is no guarantee that the IO image will be updated correctly. The can occur, for example, following a station return alarm. The need to call PNIO_ALARM can only be reset by restarting the CP (power cycle).

###### Call interface

Call interface in FBD representation

![Call interface](images/12881773835_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Parameters DONE, NEW, ERROR, STATUS (IE) (S7-300)](#parameters-done-new-error-status-ie-s7-300)
  
[Parameters for PNIO_ALARM (S7-300)](#parameters-for-pnio_alarm-s7-300)

##### Parameters for PNIO_ALARM (S7-300)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the PNIO_ALARM instruction:

| Parameter | Declaration | Data type | Possible values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD | - | Start address of the module that caused the error |
| DONE | OUTPUT | BOOL | 0: - 1: Alarm information transferred successfully | This parameter indicates whether or not the job was completed without errors.  If DONE = 1, the NEW parameter must also be checked. |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code |
| NEW | OUTPUT | BOOL | 0: Data transfer active or no new alarm  1: New alarm received and acknowledged | If DONE = 1 and NEW = 1, a new received alarm is signaled. |
| STATUS | OUTPUT | WORD | 0: No error Different value: Error (see Table 1–14) | Status code |
| ID | OUTPUT | WORD |  | Logical start address of the PNIO component that triggers the alarm (module or submodule).  For an output module, bit 15 is set (example of output address 5: ID:=DW#16#8005).  For a mixed module, the lower of the two addresses is specified. |
| LEN | OUTPUT | INT |  | Length of the received alarm information (AINFO) |
| MODE | IN_OUT | DWORD | 0 | Reserved |
| TINFO | IN_OUT | ANY (as VARTYPE, BYTE, WORD and DWORD are permitted) | The address of the data area points to one of the alternatives:  - Memory bit area - Data block area   The length of the ANY pointer must be >= 32 bytes. | (task information)  Destination area for the alarm management information.  The error OB start information (OB header = byte 0 to 19 of TINFO) is reproduced as far as possible by the CP firmware.  See also 1) |
| AINFO | IN_OUT | ANY (as VARTYPE, BYTE, WORD and DWORD are permitted) | The address of the data area points to one of the alternatives:  - Memory bit area - Data block area   The length of the ANY pointer must be greater than or equal to the maximum additional alarm information that can be expected, maximum 1432 bytes (see LEN parameter) | (alarm information)  Destination area for header information and additional alarm information. If the ANY pointer AINFO is too low, the information will be truncated.  See also 1) |

1) Reference Manual "STEP 7 - System and Standard Functions for S7-300 and S7-400", receiving an alarm with the "RALRM" instruction

---

**See also**

[PNIO_ALARM (S7-300)](#pnio_alarm-s7-300-1)

##### Parameters DONE, NEW, ERROR, STATUS (IE) (S7-300)

###### Condition codes

The following table shows the condition codes formed by the DONE, NEW, ERROR and STATUS parameters that must be evaluated by the user program.

> **Note**
>
> For entries with the coding 8Fxx<sub>H</sub> under STATUS, note the information in the Reference Manual "STEP 7 - System and Standard Functions for S7-300 and S7-400". The chapter describing error evaluation with the RET_VAL output parameter contains detailed information.

PNIO_ALARM status codes

| DONE | NEW | ERROR | STATUS | Meaning |
| --- | --- | --- | --- | --- |
| 0 | 0 | 0 | 8180<sub>H</sub> | Data transfer active |
| 1 | 1 | 0 | 0000<sub>H</sub> | Alarm data successfully transferred and alarm acknowledged |
| 1 | 0 | 0 | 0000<sub>H</sub> | No alarm data exist |
| 0 | 0 | 1 | 8183<sub>H</sub> | - No PROFINET IO controller configuration, - wrong CPLADDR  or  - CP in STOP mode |
| 0 | 0 | 1 | 8184<sub>H</sub> | System error or illegal parameter type |
| 0 | 0 | 1 | 8185<sub>H</sub> | Destination buffer (TINFO or AINFO) is too short |
| 0 | 0 | 1 | 8F22<sub>H</sub> | Area length error reading a parameter (e.g. DB too short) |
| 0 | 0 | 1 | 8F23<sub>H</sub> | Area length error writing a parameter (e.g. DB too short) |
| 0 | 0 | 1 | 8F24<sub>H</sub> | Area error reading a parameter |
| 0 | 0 | 1 | 8F25<sub>H</sub> | Area error writing a parameter |
| 0 | 0 | 1 | 8F28<sub>H</sub> | Orientation error when reading a parameter |
| 0 | 0 | 1 | 8F29<sub>H</sub> | Alignment error writing a parameter |
| 0 | 0 | 1 | 8F30<sub>H</sub> | Parameter is in the write-protected first active data block |
| 0 | 0 | 1 | 8F31<sub>H</sub> | Parameter is in the write-protected second active data block |
| 0 | 0 | 1 | 8F32<sub>H</sub> | The DB number in the parameter is too high |
| 0 | 0 | 1 | 8F3A<sub>H</sub> | Destination area not loaded (DB) |
| 0 | 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the I/O area |
| 0 | 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the I/O area |
| 0 | 0 | 1 | 8F44<sub>H</sub> | Access to a parameter to be read during execution of the instruction is prevented. |
| 0 | 0 | 1 | 8F45<sub>H</sub> | Access to a parameter to be written during execution of the instruction is prevented. |
| 0 | 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference |
| 0 | 0 | 1 | 8090<sub>H</sub> | Module with this address does not exist |
| 0 | 0 | 1 | 80A0<sub>H</sub> | Negative acknowledgment reading from the module |
| 0 | 0 | 1 | 80A1<sub>H</sub> | Negative acknowledgment writing to the module |
| 0 | 0 | 1 | 80B0<sub>H</sub> | Module does not recognize the data record |
| 0 | 0 | 1 | 80B1<sub>H</sub> | - The specified data record length is incorrect  or  - The CP changes to STOP |
| 0 | 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read |
| 0 | 0 | 1 | 80C1<sub>H</sub> | The specified data record is being processed |
| 0 | 0 | 1 | 80C2<sub>H</sub> | Too many jobs pending |
| 0 | 0 | 1 | 80C3<sub>H</sub> | Resources (memory) occupied |
| 0 | 0 | 1 | 80C4<sub>H</sub> | Communication error (occurs temporarily, it is usually best to repeat the job in the user program). |

---

**See also**

[PNIO_ALARM (S7-300)](#pnio_alarm-s7-300-1)

#### PROFIenergy (S7-300)

This section contains information on the following topics:

- [PROFIenergy (S7-300)](#profienergy-s7-300-1)
- [PROFIenergy program blocks for the CP 300 (S7-300)](#profienergy-program-blocks-for-the-cp-300-s7-300)
- [PE_START_END_CP (S7-300)](#pe_start_end_cp-s7-300)
- [PE_CMD_CP (S7-300)](#pe_cmd_cp-s7-300)
- [Response data (S7-300)](#response-data-s7-300)
- [PE_I_DEV_CP (S7-300)](#pe_i_dev_cp-s7-300)
- [PE_DS3_WRITE_ET200S_CP (S7-300)](#pe_ds3_write_et200s_cp-s7-300)

##### PROFIenergy (S7-300)

###### PROFIenergy

The PROFIenergy functions in PROFINET are used for energy management of plants. These include the planned or spontaneous shutdown of individual field devices, units or plant sections to save energy. The shutdown takes place during times without production or during breaks in production. Energy and diagnostics data can be read from devices included in the energy concept and that support these functions.

###### PROFIenergy controller

The commands for shutting down are output by the higher-level controller, in PROFINET IO, the IO controller.

With the SIMATIC S7‑300, an S7‑300 CPU with PROFIenergy functionality can be the PROFIenergy controller.

###### PROFIenergy devices

The commands of the PROFIenergy controller are processed by the IO devices with PROFIenergy functionality to shut down connected devices in the field.

In the context of the PROFIenergy program blocks, an IO device with PROFIenergy functionality is known as a PROFIenergy device. With the SIMATIC S7‑300, an S7‑300 CPU with PROFIenergy functionality can be the PROFIenergy device.

###### I‑devices

In SIMATIC S7, an intelligent device (I-device) itself can have subordinate PROFIenergy devices. In this case, the I-device also has the function of a PROFIenergy controller.

###### Energy saving modes and PE_MODE_ID

Many devices support only the operating states "ready to operate" (power ON) and "pause" (power OFF). Scaled energy-saving states with different energy-saving modes can be specified for devices that support this or for groups of units in the controller of the PROFIenergy device. With PROFIenergy, these various states of energy consumption can be assigned to the devices that will be shut down in the field.

The various states of energy consumption are known as "energy-saving modes". For each individual energy-saving mode, a defined "PE_MODE_ID" is specified.

###### Programming of the features of the energy saving modes

The details of the energy-saving modes (addressed field device, pause duration etc) are programmed in the user program of the CPU of the PROFIenergy device.

---

**See also**

[PROFIenergy program blocks for the CP 300 (S7-300)](#profienergy-program-blocks-for-the-cp-300-s7-300)

##### PROFIenergy program blocks for the CP 300 (S7-300)

###### Implementation of the PROFIenergy functions in S7‑300

With a SIMATIC S7-300, the PROFIenergy functions are provided by program blocks for the IO controller and the IO device.

Note that an S7-300 CPU and a CP 300 use different PROFIenergy program blocks.

###### PROFIenergy specification

The functions of the PROFIenergy program blocks for the CP 300 are based on the following specification of the PROFIBUS Users Organization (PNO):

Common Application Profile PROFIenergy, Technical Specification for PROFINET, Version 1.0, January 2010, Order No. 3.802

###### PROFIenergy program blocks for the CP 300

The PROFIenergy program blocks are called by the user program of the CPU. The following PROFIenergy program blocks are available for the PROFIenergy functions of the CP 300:

- CP 300 as IO controller:

  - PE_START_END_CP

    Program block for initiating and ending pauses for power supply and setting defined energy-saving modes for the PROFIenergy device.
  - PE_CMD_CP

    Program block for initiating and ending pauses for power supply and setting defined energy-saving modes and for querying measured energy values from the PROFIenergy device.

  The two program blocks can be used as alternatives. Compared with PE_START_END_CP, PE_CMD_CP has an expanded range of functions for the integration of measured energy values.

  For each PROFIenergy device, the program block must be called separately.

  - PE_DS3_WRITE_ET200_CP

    Does not belong to the PROFIenergy function blocks, but expands the PROFIenergy functions for an ET 200S.

    With PE_DS3_WRITE_ET200_CP, the settings for the switching behavior of up to 8 slots (in this case: power modules) of the ET 200S are specified.
- CP 300 as IO device:

  - PE_I_DEV_CP

    Receives all PROFIenergy commands and allows the user program to execute the PROFIenergy functions.

    Makes the response frames of the IO device available to the IO controller.

    PE_I_DEV_CP is called cyclically by the user program of the IO device.
  - Supplementary program blocks (FC 0...FC 8) for PE_I_DEV_CP:

    These FCs make the response data available for PE_I_DEV_CP. The FCs must be called in the user program and linked with PE_I_DEV_CP.

  If the PROFIenergy device is an I-device and itself has subordinate PROFIenergy devices, PE_START_END_CP or PE_CMD_CP is called in the CPU of the I-device for the subordinate PROFIenergy devices.

###### System and program blocks for transferring data records

The PROFIenergy commands and status information between IO controller and IO device are exchanged by reading and writing data records. This is implemented using the program blocks RDREC and RWREC.

The PROFIenergy data records are described below along with the response data of the individual program blocks.

> **Note**
>
> **Block calls**
>
> PE_START_END_CP, PE_CMD_CP, PE_I_DEV_CP and PE_DS3_WRITE_ET200_CP must not be called at the same time. The next program block can only be called after one of these program blocks as signaled "no error" (VALID = 1) or "error" (ERROR = 1).
>
> The program block PNIO_RW_REC must also not be called at the same time as PE_START_END_CP, PE_CMD_CP, PE_I_DEV_CP or PE_DS3_WRITE_ET200_CP.

---

**See also**

[Meaning and call - PE_START_END_CP (S7-300)](#meaning-and-call---pe_start_end_cp-s7-300)
  
[Meaning and call - PE_CMD_CP (S7-300)](#meaning-and-call---pe_cmd_cp-s7-300)
  
[Meaning and call - PE_I_DEV_CP (S7-300)](#meaning-and-call---pe_i_dev_cp-s7-300)
  
[Meaning and call - PE_DS3_WRITE_ET200_CP (S7-300)](#meaning-and-call---pe_ds3_write_et200_cp-s7-300)
  
[PROFIenergy (S7-300)](#profienergy-s7-300-1)

##### PE_START_END_CP (S7-300)

This section contains information on the following topics:

- [Meaning and call - PE_START_END_CP (S7-300)](#meaning-and-call---pe_start_end_cp-s7-300)
- [Explanation of the formal parameters of PE_START_END_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_start_end_cp-s7-300)
- [Condition codes of PE_START_END_CP (S7-300)](#condition-codes-of-pe_start_end_cp-s7-300)

###### Meaning and call - PE_START_END_CP (S7-300)

###### Significance and how it works

PE_START_END_CP can be used as an alternative to PE_CMD_CP.

PE_START_END_CP is used on the IO controller. It triggers an energy saving pause or ends a pause on the assigned PROFIenergy device.

The program block can be used ideally on IO controllers with IO devices that have only field devices connected to them and no energy data needs to be or can be read out from them.

The energy-saving modes are configured in the user program of the IO device. The energy-saving mode actually adopted is reported back by the IO device after execution of PE_START_END_CP and output at the PE_MODE_ID parameter.

The Pause_Time parameter specifies the length of the energy-saving pause for the IO device. On the IO device, the PE_I_DEV_CP program block checks whether or not the specified duration of the pause is adequately long and can be implemented.

###### Sequence

![Flow chart of the write/read jobs of PE_START_END_CP and PE_CMD_CP](images/42813665803_DV_resource.Stream@PNG-en-US.png)

Flow chart of the write/read jobs of PE_START_END_CP and PE_CMD_CP

Using WRREC, PE_START_END_CP sends a PROFIenergy command as a write job to the IO device. Following this, PE_START_END_CP waits for the acknowledgment from the IO device. To achieve this, the acknowledgement data record is read every 100 milliseconds using the program block RDREC.

As long as no acknowledgement has arrived from the IO device, the read job is repeated for 10 seconds at intervals of 100 ms.

The response data of the IO device is read with RDREC.

###### Call interface in FBD representation

![Call interface in FBD representation](images/42813565067_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Explanation of the formal parameters of PE_START_END_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_start_end_cp-s7-300)
  
[PROFIenergy (S7-300)](#profienergy-s7-300-1)
  
[PROFIenergy program blocks for the CP 300 (S7-300)](#profienergy-program-blocks-for-the-cp-300-s7-300)

###### Explanation of the formal parameters of PE_START_END_CP (S7-300)

###### Explanation of the formal parameters of PE_START_END_CP

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD | I, Q, M, D, L, const. | Module start address of the CP |
| START | INPUT | BOOL | - 1 = command active - 0 = command not active | A rising edge enables the "Start_Pause" command |
| END | INPUT | BOOL | - 1 = command active - 0 = command not active | A rising edge enables the "End_Pause" command |
| ID | INPUT | WORD |  | Logical address of the destination PROFIenergy device |
| PAUSE_ TIME | INPUT | TIME | T#-24D_20H_31M_23S_648MS to T#24D_20H_31M_23S_647MS | IEC time in steps of 1 ms, integer with sign |
| PE_MODE_ ID | OUTPUT | BYTE | - 00<sub>h</sub>: Power OFF (pause) - 01<sub>h</sub>...FE<sub>h</sub>: Configurable - FF<sub>h</sub>: Ready for operation | ID of the energy-saving mode adopted by the IO device after execution of the command. |
| VALID | OUTPUT | BOOL | 0: -  1: Execution completed successfully | This parameter indicates whether or not the job was completed without errors. |
| BUSY | OUTPUT | BOOL | 0: Execution completed, aborted or not yet started  1: Execution active | Condition code of the processing status of the program block |
| ERROR | OUTPUT | BOOL | 0: -  1: Errors | Error code  For the meaning in conjunction with the STATUS parameter, refer to [Condition codes of PE_START_END_CP](#condition-codes-of-pe_start_end_cp-s7-300). |
| STATUS | OUTPUT | WORD |  | Status code  For the meaning in conjunction with the ERROR parameter, refer to [Condition codes of PE_START_END_CP](#condition-codes-of-pe_start_end_cp-s7-300). |

---

**See also**

[Response data (S7-300)](#response-data-s7-300)

###### Condition codes of PE_START_END_CP (S7-300)

###### Condition codes of PE_START_END_CP

PE_START_END_CP is based on the program block PNIO_RW_REC and returns all condition codes of PNIO_RW_REC, see condition codes of the block PNIO_RW_REC.

The following additional PROFIenergy-specific condition codes are output. The error codes of STATUS are valid only in conjunction with ERROR = 1.

Specific condition codes of PE_START_END_CP

| STATUS | Meaning |
| --- | --- |
| **Block-specific errors** |  |
| 8080<sub>h</sub> | Rising edge at START and END at the same time |
| 8081<sub>h</sub> | Length conflict between CMD_PARAM and CMD_PARAM_LEN |
| **PROFIenergy-specific errors** |  |
| FE01<sub>h</sub> | Invalid Service_Request_ID |
| FE02<sub>h</sub> | Invalid Request_Reference |
| FE03<sub>h</sub> | Invalid CMD_MODIFIER |
| FE04<sub>h</sub> | Invalid information about the data structure of a command (Data_Structure_Identifier_RQ) in the frame for writing the PROFIenergy data record |
| FE05<sub>h</sub> | Invalid information about the data structure of a command (Data_Structure_Identifier_RS) in the frame for reading the PROFIenergy data record |
| FE06<sub>h</sub> | Energy saving mode (PE_Mode_ID) not supported |
| FE07<sub>h</sub> | Response longer than max transfer length |
| FE08<sub>h</sub> | Invalid number of commands |
| FE09<sub>h</sub> | Invalid block type (see frame header) |
| FE0A<sub>h</sub> | Invalid block length (see frame header) |
| FE0B<sub>h</sub> | Invalid block version (see frame header) |
| FE50<sub>h</sub> | Not a suitable energy saving mode (PE_Mode_ID) |
| FE51<sub>h</sub> | Value for PAUSE_TIME not supported |
| FE52<sub>h</sub> | PE_Mode_ID not supported |

Details on the parameters of the PROFIenergy-specific errors can be found in the section [Response data](#response-data-s7-300).

##### PE_CMD_CP (S7-300)

This section contains information on the following topics:

- [Meaning and call - PE_CMD_CP (S7-300)](#meaning-and-call---pe_cmd_cp-s7-300)
- [Explanation of the formal parameters of PE_CMD_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_cmd_cp-s7-300)
- [Condition codes of PE_CMD_CP (S7-300)](#condition-codes-of-pe_cmd_cp-s7-300)

###### Meaning and call - PE_CMD_CP (S7-300)

###### Significance and how it works

PE_CMD_CP can be used as an alternative to PE_START_END_CP.

PE_CMD_CP is used on the IO controller and initiates an energy-saving pause or ends a pause on the assigned PROFIenergy device. PE_CMD_CP can also read out further information and energy measured values from an IO device.

The program block can be used ideally on IO controllers with IO devices that have field devices connected to them and energy data needs to be read out from them.

You will find a flowchart of the write/read jobs of PE_CMD_CP in section [Meaning and call - PE_START_END_CP](#meaning-and-call---pe_start_end_cp-s7-300).

The individual commands that can be transferred to the IO device with the program block are assigned defined "Service_Request_IDs". The Service_Request_IDs 01...05 and 16 are assigned in the CMD parameter.

The CMD_MODIFIER parameter specifies the two commands 04 (Query_Modes) and 16 (Query_Measurement) in greater detail.

The CMD_PARA parameter assigns the values for certain parameters to some commands using an Any pointer. The CMD_PARA_LEN parameter specifies the length of this parameter.

The RESPONSE_DATA parameter points to the data area of the response data of the IO device.

###### Call interface in FBD representation

![Call interface in FBD representation](images/42813619979_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Explanation of the formal parameters of PE_CMD_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_cmd_cp-s7-300)
  
[PROFIenergy (S7-300)](#profienergy-s7-300-1)
  
[PROFIenergy program blocks for the CP 300 (S7-300)](#profienergy-program-blocks-for-the-cp-300-s7-300)

###### Explanation of the formal parameters of PE_CMD_CP (S7-300)

###### Explanation of the formal parameters of PE_CMD_CP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD | I, Q, M, D, L, const. | Module start address of the CP |
| REQ | INPUT | BOOL |  | Starts the transfer of the PROFIenergy commands on a rising edge. |
| ID | INPUT | WORD |  | Logical address of the destination PROFIenergy device |
| CMD | INPUT | BYTE | - 01: Start_Pause - 02: End_Pause - 03: Query_Modes - 04: PEM_Status - 05: PE_Identity - 16: Query_Measurement | Service_Request_ID of the PROFIenergy command.  You will find the meaning of the commands below this table. |
| CMD_ MODIFIER | INPUT | BYTE | For "Start_Pause": 00  For "End_Pause": 00  For "Query_Modes":  - 01: List_Energy_Saving _Modes - 02: Get_Mode   For "PEM_Status": 00  For "PE_Identity": 00  For "Query_Measurement":  - 01:  Get_Measurement_List - 02:  Get_Measurement_Values | Modifier of the PROFIenergy command, meaning:  - "Query_Modes" command   - Modifier 01: Reads all supported energy-saving modes (PE_Mode_ID).   - Modifier 02 reads the parameters of the selected PE_Mode_ID. - "Query_Measurement" command   - Modifier 01: Reads the configured Measurement_IDs.   - Modifier 02: Reads the measured values of the selected Measurement_IDs.   You will find information on the parameters in [Response data](#response-data-s7-300) in the section for the particular command.  Modifier 00 means "no options". |
| CMD_PARA | INPUT | ANY |  | Any pointer to parameters for commands  - For command 01 Start_Pause: "Pause_Time" - For command 02 End_Pause: Irrelevant - For command 03 Query_Modes:   - For modifier 01: Irrelevant   - For modifier 02 Get_Mode:     "PE_Mode_ID" - For command 04 PEM_Status: Irrelevant - For command 05 PE_Identity: Irrelevant - For command 16 Query_Measurement:   - For modifier 01: Irrelevant   - For modifier 02 Get_Measurement_Values:     ANY pointer to the data structure with the parameters "Count" and "Measurement_IDs"   You will find information on the parameters in [Response data](#response-data-s7-300) in the section for the particular command.  The entire data area of the data record to be written (Service_Data_Request) is entered. Maximum length: 234 bytes |
| CMD_PARA_LEN | INPUT | INT |  | Actual length of the parameters in CMD_PARA. Max. length: 234 bytes |
| RESPONSE _DATA | INOUT | ANY |  | Pointer to the address of the response data of the IO device (complete frame including block header)   **Note:**  If the area selected is not large enough, only the configured number of bytes is saved. |
| VALID | OUTPUT | BOOL | 0: -  1: Execution completed successfully | The status parameter of the program block indicates whether or not the job was completed without errors. |
| BUSY | OUTPUT | BOOL | 0: Execution not yet started, completed or aborted  1: Execution active | Condition code of the processing status of the program block |
| ERROR | OUTPUT | BOOL | 0: -  1: Errors | Error code  For the meaning in conjunction with the STATUS parameter, refer to [Condition codes of PE_CMD_CP](#condition-codes-of-pe_cmd_cp-s7-300). |
| STATUS | OUTPUT | WORD |  | Status code  For the meaning in conjunction with the ERROR parameter, refer to [Condition codes of PE_CMD_CP](#condition-codes-of-pe_cmd_cp-s7-300). |

###### Service_Request_IDs and meaning of the PROFIenergy commands

The PROFIenergy commands with Service_Request_ID 01...05 and 16 have the following significance:

- **01 = Start_Pause**

  Command for starting an energy-saving pause.

  The IO device selects the configured energy-saving mode. The energy-saving mode is reported back to the controller in the response data.
- **02 = End_Pause**

  Command for ending an energy saving pause
- **03 = Query_Modes**

  Queries the configured energy-saving modes with all corresponding time and energy information on the IO device.

  The queried information is detailed using the CMD_MODIFIER parameter:

  - **List_Energy_Saving_Modes**

    Reads all supported PROFIenergy modes of the IO device.
  - **Get_Mode**

    Reads the data of the selected PROFIenergy mode.
- **04 = PEM_Status**

  Query of the energy-saving mode actually adopted by the field device or the unit group.
- **05 = PE_Identity**

  Queries the PROFIenergy services supported by the IO device.
- **16 = Query_Measurement**

  Queries the energy data of the IO device.

  The queried information is detailed using the CMD_MODIFIER parameter:

  - **Get_Measurement_List**

    Reads all the configured Measurement_IDs on the device.
  - **Get_Measurement_Values**

    Reads the measured energy values of the selected Measurement_IDs.

###### Commands for various device classes

The devices that can be included in PROFIenergy concepts can be divided into three classes that are addressed by the IO controller with different commands:

- IO modules, actuators, motor starters

  Supported commands:

  - Start_Pause, End_Pause
  - Query_Modes, PEM_Status, PE_Identify
- Measuring devices for electrical variables

  Supported commands:

  - Query_Measurement
- Frequency converters

  Supported commands:

  - Start_Pause, End_Pause
  - Query_Modes, PEM_Status, PE_Identify
  - Query_Measurement

    Data of electrical variables data acquired by frequency converters can also be queried.

###### Condition codes of PE_CMD_CP (S7-300)

###### Condition codes of PE_CMD_CP

PE_CMD_CP is based on the program block PNIO_RW_REC and returns all condition codes of PNIO_RW_REC, see condition codes of the block PNIO_RW_REC.

The following additional PROFIenergy-specific condition codes are output. The error codes of STATUS are valid only in conjunction with ERROR = 1.

Specific condition codes of PE_CMD_CP

| STATUS | Meaning |
| --- | --- |
| **Block-specific errors** |  |
| 8081<sub>h</sub> | Length conflict between CMD_PARAM and CMD_PARAM_LEN |
| **PROFIenergy-specific errors** |  |
| FE01<sub>h</sub> | Invalid Service_Request_ID |
| FE02<sub>h</sub> | Invalid Request_Reference |
| FE03<sub>h</sub> | Invalid CMD_MODIFIER |
| FE04<sub>h</sub> | Invalid information on the data structure of a command (Data_Structure_Identifier_RQ) in the frame for the PROFIenergy data record to be written |
| FE05<sub>h</sub> | Invalid information on the data structure of a command (Data_Structure_Identifier_RS) in the frame for the PROFIenergy data record to be read |
| FE06<sub>h</sub> | Energy saving mode (PE_Mode_ID) not supported |
| FE07<sub>h</sub> | Response longer than max transfer length |
| FE08<sub>h</sub> | Invalid number of commands |
| FE09<sub>h</sub> | Invalid block type (see frame header) |
| FE0A<sub>h</sub> | Invalid block length (see frame header) |
| FE0B<sub>h</sub> | Invalid block version (see frame header) |
| FE50<sub>h</sub> | Not a suitable energy saving mode (PE_Mode_ID) |
| FE51<sub>h</sub> | Value for PAUSE_TIME not supported |
| FE52<sub>h</sub> | PE_Mode_ID not supported |

Details on the parameters of the PROFIenergy-specific errors can be found in the section [Response data](#response-data-s7-300).

---

**See also**

Condition codes of PNIO_RW_REC

##### Response data (S7-300)

###### Structure of the response data

The following table shows the structure of the data record (80A0<sub>h</sub>) of the response data of PE_START_END_CP and PE_CMD_CP.

The following table shows an overview of the structure of the data record of the returned response data according to the PROFIenergy specification. The composition of the "Service Data Response" area is described below for the individual PROFIenergy commands.

Structure of the response data

| Block definitions | Attributes | Value | Data type | Description |
| --- | --- | --- | --- | --- |
| Block header | BlockType | 0801<sub>h</sub> | Unsigned16 |  |
| BlockLength |  | Unsigned16 | Frame length (without the "BlockType" and "BlockLength" fields) |  |
| BlockVersionHigh | 01<sub>h</sub> | Unsigned8 |  |  |
| BlockVersionLow | 00<sub>h</sub> | Unsigned8 |  |  |
| Response header | Service_Request_ID | 01<sub>h</sub>...FF<sub>h</sub> | Unsigned8 | 01<sub>h</sub>: Start_Pause  02<sub>h</sub>: End_Pause  03<sub>h</sub>: Query_Modes  04<sub>h</sub>: PEM_Status  05<sub>h</sub>: PE_Identify  06<sub>h</sub>...09<sub>h</sub>: - Reserved -  10<sub>h</sub>: Query_Measurement  11<sub>h</sub>...CF: - Reserved -  D0<sub>h</sub>...FF<sub>h</sub>: Vendor-specific |
| Request_Reference | 01<sub>h</sub>...FF<sub>h</sub> | Unsigned8 | Identification number of the query (mirrored in the response of the IO device) |  |
| Service header response | Status | 01<sub>h</sub>...FF<sub>h</sub> | Unsigned8 | 00<sub>h</sub>: - Reserved -  01<sub>h</sub>: Done  02<sub>h</sub>: Done with error(s)  03<sub>h</sub>: Data incomplete  04<sub>h</sub>...CF<sub>h</sub>: - Reserved -  D0<sub>h</sub>...FF<sub>h</sub>: Depends on the Service_Request_ID |
| Data_Structure_Identifier_RS | 01<sub>h</sub>...FF<sub>h</sub> | Unsigned8 | 00<sub>h</sub>: - Reserved -  01<sub>h</sub>...FF<sub>h</sub>: Data structure dependent on the Service_Request_ID  FF<sub>h</sub>: error |  |
| Service data response |  |  |  | Response data of the IO device  Depending on the particular PROFIenergy command (described below) |

###### Meaning of "Service data request" and "Service data response"

The following sections explain the parameter values for the queries of the IO controller to the IO device (Service Data Request) for each PROFIenergy command and the structure of the response data of the IO device (Service Data Response).

- **Service data request**

  Parameter values for IO controller queries
- **Service data response**

  Structure of the response data of the IO device

###### PROFIenergy command "Start_Pause"

- **Service data request**

  - CMD = 01
  - CMD_MODIFIER = 00
  - CMD_PARA_LEN = 04
  - CMD_PARA = Any pointer to the value for "Pause_Time" (data type "TIME")

    IEC time in steps of 1 ms, integer with sign

    Value: T#-24D_20H_31M_23S_648MS to T#24D_20H_31M_23S_647MS
- **Service data response**

| Parameters | Value | Data type |
| --- | --- | --- |
| PE_Mode_ID * | 01<sub>h</sub>...FF<sub>h</sub> | Unsigned8 |
| - Reserved - | 00<sub>h</sub> | Unsigned8 |
| * Identification number of the energy-saving mode |  |  |

###### PROFIenergy command "End_Pause"

- **Service data request**

  - CMD = 02
  - CMD_MODIFIER = 00
  - CMD_PARA_LEN = 00
  - CMD_PARA = irrelevant
- **Service data response**

| Parameters | Value | Data type |
| --- | --- | --- |
| Time_to_operate * |  | Unsigned32 |
| * Expected time for switching over the PROFIenergy device to "ready to operate" |  |  |

###### PROFIenergy command "Query_Modes" – List_Energy_Saving_Modes

- **Service data request**

  - CMD = 03
  - CMD_MODIFIER = 01
  - CMD_PARA_LEN = 00
  - CMD_PARA = irrelevant
- **Service data response**

| Parameters | Value | Data type |
| --- | --- | --- |
| Number_of_PE_Mode_IDs * | 01<sub>h</sub> | Unsigned8 |
| PE_Mode_IDs |  | Unsigned8 array of Number_of_PE_Mode_IDs (unique ID for mode) |
| * Number of energy-saving modes |  |  |

###### PROFIenergy command "Query_Modes" – Get_Mode

- **Service data request**

  - CMD = 03
  - CMD_MODIFIER = 02
  - CMD_PARA_LEN = 01
  - CMD_PARA = Any pointer to value for PE_MODE_ID (unsigned8)
- **Service data response**

| Parameters | Value | Data type |
| --- | --- | --- |
| PE_Mode_ID | 01<sub>h</sub>...FF<sub>h</sub> | Unsigned8 |
| PE_Mode_Attributes * | 00<sub>h</sub>...01<sub>h</sub> | Unsigned8 |
| Time_min_Pause |  | Unsigned32 |
| Time_to_Pause |  | Unsigned32 |
| Time_to_operate |  | Unsigned32 |
| Time_min_length_of_stay |  | Unsigned32 |
| Time_max_length_of_stay |  | Unsigned32 |
| Mode_Power_Consumption |  | Float32 |
| Energy_Consumption_to_pause |  | Float32 |
| Energy_Consumption_to_operate |  | Float32 |
| * Coding of bit 0: 0 = Only static time and energy measured values available. 1 = Dynamic time and energy measured values available.     Bits 1...7: Reserved |  |  |

###### PROFIenergy command "PEM_Status"

- **Service data request**

  - CMD = 04
  - CMD_MODIFIER = 00
  - CMD_PARA_LEN = 00
  - CMD_PARA = irrelevant
- **Service data response**

| Parameters | Value | Data type |
| --- | --- | --- |
| PE_Mode_ID_Source * | 00<sub>h</sub> 01<sub>h</sub>...FE<sub>h</sub> FF<sub>h</sub> | Unsigned8 |
| PE_Mode_ID_Destination * | 00<sub>h</sub> 01<sub>h</sub>...FE<sub>h</sub> FF<sub>h</sub> | Unsigned8 |
| Time_to_operate |  | Unsigned32 |
| Remaining_time_to_destination |  | Unsigned32 |
| Mode_Power_Consumption |  | Float32 |
| Energy_Consumption_to_Destination |  | Float32 |
| Energy_Consumption_to_operate |  | Float32 |
| * Possible values for "PE_Mode_ID_Source" and "PE_Mode_ID_Destination": 00<sub>h</sub>: PE_Power_off 01<sub>h</sub>...FE<sub>h</sub>: Freely configurable FF<sub>h</sub>: PE_Ready_to_operate |  |  |

###### PROFIenergy command "PE_Identify"

- **Service data request**

  - CMD = 05
  - CMD_MODIFIER = 00
  - CMD_PARA_LEN = 00
  - CMD_PARA = irrelevant
- **Service data response**

| Parameters | Value | Data type |
| --- | --- | --- |
| Count * | 6 | Unsigned8 |
| Start_Pause ** | 01<sub>h</sub> | Unsigned8 |
| End_Pause | 02<sub>h</sub> | Unsigned8 |
| Query_Modes | 03<sub>h</sub> | Unsigned8 |
| PEM_Status | 04<sub>h</sub> | Unsigned8 |
| PE_Identify | 05<sub>h</sub> | Unsigned8 |
| Query_Measurement *** | 10<sub>h</sub> | Unsigned8 |
| * Number of supported PROFIenergy commands  ** Service_Request_ID of the first supported PROFIenergy command  *** Service_Request_ID of the last supported PROFIenergy command |  |  |

###### PROFIenergy command "Query_Measurement" – Get_Measurement_List

- **Service data request**

  - CMD = 16
  - CMD_MODIFIER = 01
  - CMD_PARA_LEN = 00
  - CMD_PARA = irrelevant
- **Service data response**

| Parameters | Value | Data type |
| --- | --- | --- |
| Count * |  | Unsigned8 |
| - Reserved - |  | Unsigned8 |
| Measurement_ID ** |  | Unsigned16 |
| Accuracy_Domain <sup>1</sup> |  | Unsigned8 |
| Accuracy_Class <sup>2</sup> |  | Unsigned8 |
| Range <sup>3</sup> |  | Float32 |
| … |  |  |
| Measurement_ID *** |  | Unsigned16 |
| Accuracy_Domain <sup>1</sup> |  | Unsigned8 |
| Accuracy_Class <sup>2</sup> |  | Unsigned8 |
| Range <sup>3</sup> |  | Float32 |
| * Number of Measurement_IDs  ** First supported Measurement_ID  *** Last supported Measurement_ID |  |  |

<sup>1</sup> Accuracy domain (range 1...4):  
   0 = Reserved  
   1 = Percentage of the measuring range  
   2 = Percentage of the current measured values  
   3 = Accuracy according to IEC 61557-12  
   4 = Accuracy according to EN 50470-3 section 8

<sup>2</sup> Accuracy class (range 1...15):  
   0 = Reserved  
   1 (0.01%) ... 15 (>20%)

<sup>3</sup> Measuring range if Accuracy_Domain = 1; otherwise undefined

###### PROFIenergy command "Query_Measurement" – Get_Measurement_Values

- **Service data request**

  - CMD = 16
  - CMD_MODIFIER = 02
  - CMD_PARA_LEN = length of the data structure in bytes
  - CMD_PARA = Any pointer to data structure with the following structure:

| Parameters | Value | Data type |
| --- | --- | --- |
| Count * |  | Unsigned8 |
| - Reserved - |  | Unsigned8 |
| Measurement_ID ** |  | Unsigned16 |
| … |  |  |
| Measurement_ID *** |  | Unsigned16 |
| * Number of Measurement_IDs  ** First queried measured value  *** Last queried measured value |  |  |

- **Service data response**

| Parameters | Value | Data type |
| --- | --- | --- |
| Count * |  | Unsigned8 |
| - Reserved - |  | Unsigned8 |
| Length_of_Structure | 0002<sub>h</sub>...FFFF<sub>h</sub> | Unsigned16 |
| Measurement_Data_Structure_ID | 1 = simple value | Unsigned8 |
| Measurement_ID ** | 00<sub>h</sub>...FF<sub>h</sub> | Unsigned16 |
| Status_of_Measurement_Value | 1 = valid  2 = not available  3 = not available at times | Unsigned8 |
| Transmission_Data_Type |  | Float32 |
| End_of_demand |  | Unsigned32 or Unsigned16 |
| Length_of_Structure |  | Unsigned16 |
| Measurement_Data_Structure_ID |  | Unsigned8 |
| Measurement_ID *** |  | Unsigned16 |
| Status_of_Measurement_Value |  | Unsigned8 |
| Transmission_Data_Type |  | Float32 |
| End_of_demand |  | Unsigned32 or Unsigned16 |
| * Number of Measurement_IDs  ** First queried measured value  *** Last queried measured value |  |  |

---

**See also**

[Explanation of the formal parameters of PE_CMD_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_cmd_cp-s7-300)
  
[Explanation of the formal parameters of PE_START_END_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_start_end_cp-s7-300)

##### PE_I_DEV_CP (S7-300)

This section contains information on the following topics:

- [Meaning and call - PE_I_DEV_CP (S7-300)](#meaning-and-call---pe_i_dev_cp-s7-300)
- [Explanation of the formal parameters of PE_I_DEV_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_i_dev_cp-s7-300)
- [Condition codes of PE_I_DEV_CP (S7-300)](#condition-codes-of-pe_i_dev_cp-s7-300)
- [Supplementary program blocks for PE_I_DEV_CP (S7-300)](#supplementary-program-blocks-for-pe_i_dev_cp-s7-300)

###### Meaning and call - PE_I_DEV_CP (S7-300)

###### Significance and how it works

The program block PE_I_DEV_CP is used on the PROFIenergy device where it handles the PROFIenergy commands of the IO controller. The PROFIenergy data records (80A0<sub>h</sub>) sent by the IO controller are forwarded by the CP firmware to PE_I_DEV_CP. The PROFIenergy data of the IO device is made available to the IO controller as the response by PE_I_DEV_CP using the PROFIenergy data record (80A0<sub>h</sub>).

The response data of PE_I_DEV_CP is generated by the supplementary functions FC 0 to FC 8, see section [Supplementary program blocks for PE_I_DEV_CP](#supplementary-program-blocks-for-pe_i_dev_cp-s7-300).

###### Call interface in FBD representation

![Call interface in FBD representation](images/42813649291_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Explanation of the formal parameters of PE_I_DEV_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_i_dev_cp-s7-300)
  
[Overview of the FCs (S7-300)](#overview-of-the-fcs-s7-300)
  
[PROFIenergy (S7-300)](#profienergy-s7-300-1)
  
[PROFIenergy program blocks for the CP 300 (S7-300)](#profienergy-program-blocks-for-the-cp-300-s7-300)

###### Explanation of the formal parameters of PE_I_DEV_CP (S7-300)

###### Explanation of the formal parameters of PE_I_DEV_CP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD | I, Q, M, D, L, const. | Module start address of the CP |
| RESET | INPUT | BOOL |  | Resets processing of the program block.  NEW is set to 0. |
| VALID | INPUT | BOOL |  | If the response data was written to the relevant memory area of the IO device, VALID = 1 must be set by the user program. Following this, the program block makes the data available to the IO controller.  NEW is set to 0. |
| CMD | OUTPUT | INT | - 01: Start_Pause - 02: End_Pause - 03: Query_Modes - 04: PEM_Status - 05: PE_Identity - 16: Query_Measurement | Service ID of the PROFIenergy command |
| CMD_ MODIFIER | OUTPUT | INT | - Modifier for Start_Pause: 00 - Modifier for End_Pause: 00 - Query_Modes, Modifier:   - 01 (List_Energy_ Saving_Modes)   - 02 (Get_Mode) - Modifier for PEM_Status: 00 - Modifier for PE_Identity: 00 - Query_Measurement, Modifier:   - 01 (Get_Measurement _List)   - 02 (Get_Measurement _Values) | Modifier of the PROFIenergy commands  Meaning of the modifiers for commands:  - "Query_Modes" command, Modifier:   - 01 (List_Energy_Saving_Modes): Reads all supported PROFIenergy modes   - 02 (Get_Mode): Reads the data of the selected PROFIenergy mode - "Query_Measurement" command, Modifier:   - 01 (Get_Measurement_List): Reads all configured Measurement_IDs.   - 02 (Get_Measurement_Values): Reads the measured values of the selected Measurement_IDs. |
| CMD_PARA | OUTPUT | ANY |  | Any pointer to parameters for the following command modifiers (compare CMD_MODIFIER parameter):  - For "Get_Mode": PE_Mode_ID (ID of the energy-saving mode) length = 1 - For "Get_Measurement_Values": measured values of the Measurement_IDs  length = max. 236 bytes (complete frame of the controller command without header) |
| INDEX | OUTPUT | INT |  | Number of the PROFIenergy data record (80A0<sub>h</sub>) |
| NEW | OUTPUT | BOOL | 0: Execution not yet started, completed or aborted  1: Execution active | Condition codes of the processing status of the program block |
| ERROR | OUTPUT | BOOL | 0: -  1: Errors | Error code  For the meaning in conjunction with the STATUS parameter, refer to [Condition codes of PE_I_DEV_CP](#condition-codes-of-pe_i_dev_cp-s7-300). |
| STATUS | OUTPUT | WORD |  | Status code  For the meaning in conjunction with the ERROR parameter, refer to [Condition codes of PE_I_DEV_CP](#condition-codes-of-pe_i_dev_cp-s7-300). |
| RESPONSE _DATA | INOUT | ANY | See "Response data" of the program block | Pointer to the data area of the response of the IO device (complete response frame including header).  The data area must match the data area of the supplementary program blocks FC 0 - FC 8 (parameter "DATA_ERRORRSP").  Recommended size: At least 244 bytes. If the data area is too small, only the data of the configured bytes are transferred. |

###### Condition codes of PE_I_DEV_CP (S7-300)

###### Condition codes of PE_I_DEV_CP

PE_I_DEV_CP is based on the program block PNIO_RW_REC and returns all condition codes of PNIO_RW_REC, see condition codes of the block PNIO_RW_REC.

---

**See also**

Condition codes of PNIO_RW_REC

###### Supplementary program blocks for PE_I_DEV_CP (S7-300)

This section contains information on the following topics:

- [Overview of the FCs (S7-300)](#overview-of-the-fcs-s7-300)
- [Interconnection of the FCs with PE_I_DEV_CP (S7-300)](#interconnection-of-the-fcs-with-pe_i_dev_cp-s7-300)
- [Common parameters of the FCs (S7-300)](#common-parameters-of-the-fcs-s7-300)
- [Individual parameters of the FCs (S7-300)](#individual-parameters-of-the-fcs-s7-300)

###### Overview of the FCs (S7-300)

###### Function

The supplementary program blocks FC 0 to FC 8 support the preparation of the response data made available to the controller by PE_I_DEV_CP:

- For the response data of each PROFIenergy command, there is a separate program block (FC 1 - FC 8).
- FC 0 generates a common negative response for all PROFIenergy commands.

The FCs are called in the user program. In STEP 7 V5.5, they are available in the standard library in the "PROFIenergy" folder.

The FCs have several common parameters as well as individual parameters. Some of the common parameters of the FCs are interconnected with parameters of PE_I_DEV_CP. With some of the individual input parameters of the FCs, the response data is entered as plain language for the user or stored in the memory area of the IO device.

###### Overview of the FCs

The following supplementary program blocks are made available:

Overview of the supplementary FCs

| Number | Name |
| --- | --- |
| FC 0 | PE_ERROR_RSP |
| FC 1 | PE_START_RSP |
| FC 2 | PE_END_RSP |
| FC 3 | PE_LIST_MODES_RSP |
| FC 4 | PE_GET_MODE_RSP |
| FC 5 | PE_PEM_STATUS_RSP |
| FC 6 | PE_IDENTIFY_RSP |
| FC 7 | PE_MEASUREMENT_LIST_RSP |
| FC 8 | PE_MEASUREMENT_VALUE_RSP |

---

**See also**

[Interconnection of the FCs with PE_I_DEV_CP (S7-300)](#interconnection-of-the-fcs-with-pe_i_dev_cp-s7-300)

###### Interconnection of the FCs with PE_I_DEV_CP (S7-300)

###### Interconnection of the FCs with the program block PE_I_DEV_CP

![Interconnection of the FCs with PE_I_DEV_CP](images/42813074955_DV_resource.Stream@PNG-en-US.png)

Interconnection of the FCs with PE_I_DEV_CP

> **Note**
>
> **Interconnection of the program blocks is an absolute necessity**
>
> PE_I_DEV_CP must be interconnected with FC 0...FC 8 at the parameters shown on a light blue background that are assigned to the corresponding parameters of the FCs indicated by red arrows.

---

**See also**

[Common parameters of the FCs (S7-300)](#common-parameters-of-the-fcs-s7-300)

###### Common parameters of the FCs (S7-300)

###### Common parameters of the supplementary program blocks FC 0 - FC 8

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| **Input parameters** |  |  |  |  |
| ACTIVATE | INPUT | BOOL |  | Instructs the block to copy the input parameters to the "DATA_ERRORRSP" data area are on a rising edge. Is then reset by the block.  Must be set by the user within 10 seconds after a positive edge was detected at PE_I_DEV_NEW. |
| PE_I_DEV_NEW | INPUT | BOOL |  | Must be interconnected with the NEW output parameter of PE_I_DEV_CP.  The block is processed only when 1 is set. |
| CMD | INPUT | INT |  | Must be interconnected with the CMD output parameter of PE_I_DEV_CP. |
| CMD_MODIFIER | INPUT | INT |  | Must be interconnected with the CMD_MODIFIER output parameter of PE_I_DEV_CP. |
| **Output parameters** |  |  |  |  |
| DATA_ERRORRSP | OUTPUT | ANY |  | Pointer to the data area in which the response data will be stored (complete response frame including header).  Must be interconnected with the RESPONSE_DATA output parameter of PE_I_DEV_CP.  Recommended size: At least 244 bytes. |
| VALID | OUTPUT | BOOL | 0: -  1: No error | Is set by the block.  Must be interconnected with the VALID input parameter of PE_I_DEV_CP. |
| ERROR | OUTPUT | BOOL | 0: No error  1: Errors | Error code |
| STATUS | OUTPUT | WORD | 0: No error | Status code  80B1<sub>h</sub>: Error in ANY information (for example wrong area) |

---

**See also**

[Individual parameters of the FCs (S7-300)](#individual-parameters-of-the-fcs-s7-300)

###### Individual parameters of the FCs (S7-300)

###### Individual parameters of FC 0 to FC 8

Below you will find a description of the individual parameters of the FCs.

###### PE_ERROR_RSP

Generates a negative response if the required PROFIenergy command is generally or temporarily not supported. The negative response is not dependent on the requesting command.

Individual parameters of FC 0 PE_ERROR_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| ERROR_CODE | INPUT | BYTE |  | Error number |

###### PE_START_RSP

Initiates an energy saving pause. Generates the response to the "Start_Pause" command. Returns the energy-saving mode adopted by the device.

Individual parameters of FC 1 PE_START_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| PE_Mode_ID | INPUT | BYTE |  | ID of the energy-saving mode that the device or the unit group adopts. |

Return message with the PE_Mode_ID of the energy-saving mode that the field devices or the unit group have adopted.

###### PE_END_RSP

Generates the response to the "End_Pause". command

Individual parameters of FC 2 PE_END_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| Time_to_Operate | INPUT | DWORD |  | Time required to change from the current energy-saving mode after "ready to operate". |

###### PE_LIST_MODES_RSP

Generates the response to the "Query_Modes" > modifier "List_Modes" command (list of the supported energy-saving modes).

The IDs of the energy-saving modes must be specified in the user program.

Individual parameters of FC 3 PE_LIST_MODES_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| Number_of_PE_Mode_IDs | INPUT | BYTE |  | Number of supported energy-saving modes |
| PE_Mode_ID | INPUT | ANY | - 00<sub>h</sub> - 01<sub>h</sub>...FE<sub>h</sub> - FF<sub>h</sub> | Pointer to the area in which the energy-saving modes are stored.  As the user, you will need to store the IDs of the energy-saving modes here. An energy-saving mode ID is configured in the Unsigned8 format. Permitted range: 1 to 254 bytes. |

If the devices or a group need to react differently to different lengths of pause you can set up different energy-saving modes (PE_Mode) to achieve this. You assign a different PE_Mode_ID to the various energy-saving modes.

Possible values for "PE_Mode_ID":

- 00<sub>h</sub>: PE_Power_off
- 01<sub>h</sub>...FE<sub>h</sub>: Freely configurable or vendor-specific
- FF<sub>h</sub>: PE_Ready_to_operate

###### PE_GET_MODE_RSP

Generates the response to the "Query_Modes" > Modifier "Get_Mode". command

Individual parameters of FC 4 PE_GET_MODE_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| PE_Mode_ID | INPUT | BYTE |  | Currently used energy-saving mode ID |
| Time_Min_Pause * | INPUT | Unsigned32 |  | Minimum pause duration for this PE energy-saving mode. It is the sum of the three parameters:  - Time_to_Pause - Time_to_operate - Time_min_length_of_stay |
| Time_to_Pause * | INPUT | Unsigned32 |  | Time from the START edge until the requested energy-saving mode is reached |
| Time_to_operate * | INPUT | Unsigned32 |  | Max. time after turn on before PE_ready_to_operate  Time_to_operate can be used directly for the relevant calculations. The value can either be a static MAX value or can be calculated dynamically by the PE device. |
| Time_min_length_of_stay * | INPUT | Unsigned32 |  | Minimum time that the PE device must remain in this PE_Mode. |
| Time_max_length_of_stay * | INPUT | Unsigned32 |  | Maximum time that the PE device can remain in this PE_Mode. |
| Mode_Power _Consumption ** | INPUT | Float32 |  | Energy consumption in current PE_Mode [kW] |
| Energy_Consumption _to_pause ** | INPUT | Float32 |  | Energy consumption of PE_ready_to_operate until the current PE_Mode [kWh] |
| Energy_Consumption _to_operate ** | INPUT | Float32 |  | Energy consumption from current PE_Mode until PE_ready_to_operate [kWh] |
| * The PROFIenergy profile does not specify an invalid time format. If the time is unlimited, the maximum value FFFFFFFF<sub>h</sub> can be specified. If the time is zero, 00<sub>h</sub> can be used.  ** If an energy consumption value is not defined, 0.0 (Float32) can be specified. |  |  |  |  |

###### PE_PEM_STATUS_RSP

Generates the response to the "PEM_STATUS". command

Individual parameters of FC 5 PE_PEM_STATUS_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| PE_Mode_ID_Source | INPUT | BYTE | - 00<sub>h</sub> - 01<sub>h</sub>...FE<sub>h</sub> - FF<sub>h</sub> | ID of the energy-saving mode actually adopted |
| PE_Mode_ID_Destination | INPUT | BYTE | - 00<sub>h</sub> - 01<sub>h</sub>...FE<sub>h</sub> - FF<sub>h</sub> | ID of the energy-saving mode set by the controller |
| Time_to_operate * | INPUT | Unsigned32 |  | Max. time after turn on before PE_ready_to_operate  Time_to_operate can be used directly for the relevant calculations. The value can either be a static MAX value or can be calculated dynamically by the PE device. |
| Remaining_time_to _destination * | INPUT | Unsigned32 |  | Optional: Time remaining until the requested PE_Mode. Dynamic value or static MAX value |
| Mode_Power _Consumption ** | INPUT | Float32 |  | Energy consumption in current PE_Mode [kW] |
| Energy_Consumption _to_Destination ** | INPUT | Float32 |  | Energy consumption until the requested PE_Mode [kWh] |
| Energy_Consumption _to_operate ** | INPUT | Float32 |  | Energy consumption from current PE_Mode until PE_ready_to_operate [kWh] |
| * The PROFIenergy profile does not specify an invalid time format. If the time is unlimited, the maximum value FFFFFFFF<sub>h</sub> can be specified. If the time is zero, 00<sub>h</sub> can be used.  ** If an energy consumption value is not defined, 0.0 (Float32) can be specified. |  |  |  |  |

Possible values for "PE_Mode_ID_Source" and "PE_Mode_ID_Destination":

- 00<sub>h</sub>: PE_Power_off
- 01<sub>h</sub>...FE<sub>h</sub>: Freely configurable or vendor-specific
- FF<sub>h</sub>: PE_Ready_to_operate

###### PE_IDENTIFY_RSP

Generates the response to the "PE_Identify". command

As the user you need to specify which PROFIenergy commands are supported.

Individual parameters of FC 6 PE_IDENTIFY_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| Count | INPUT | BYTE | 0...6 | Meaning of supported PROFIenergy commands |
| Start_Pause | INPUT | BOOL | 0...1 | - 1: Command is supported - 0: Command is not supported |
| End_Pause | INPUT | BOOL | 0...1 | - 1: Command is supported - 0: Command is not supported |
| Query_Modes | INPUT | BOOL | 0...1 | - 1: Command is supported - 0: Command is not supported |
| PEM_Status | INPUT | BOOL | 0...1 | - 1: Command is supported - 0: Command is not supported |
| PEM_Identify | INPUT | BOOL | 0...1 | - 1: Command is supported - 0: Command is not supported |
| Query_Measurement | INPUT | BOOL | 0...1 | - 1: Command is supported - 0: Command is not supported |

###### PE_MEASUREMENT_LIST_RSP

Generates the response to the "Query_Measurement" > Modifier "Get_Measurement_List". command

Individual parameters of FC 7 PE_MEASUREMENT_LIST_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| Count | INPUT | BYTE |  | Number of supported measured value IDs (Measurement_ID) |
| Measurement_List | INPUT | ANY |  | Pointer to the data area with the supported measured value IDs.  As the user, you store the measured value IDs in this data area.  Per frame, a maximum of 29 measured value IDs can be transferred.  For information on the structure of the array, refer to section [Response data](#response-data-s7-300) > "Query_Measurement" – Get_Measurement_List. |

###### PE_MEASUREMENT_VALUE_RSP

Generates the response to the "Query_Measurement" > Modifier "Get_Measurement_Values". command

Individual parameters of FC 8 PE_MEASUREMENT_VALUE_RSP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| Count | INPUT | BYTE |  | Number of supported Measurement_Values |
| Measurement_Values | INPUT | ANY |  | Pointer to the data area of the measured values (Measurement_Values).  As the user, you store the measured values in this data area.  Per frame, a maximum of 116 measured values can be transferred.  For information on the structure of the array, refer to section [Response data](#response-data-s7-300) > "Query_Measurement" – Get_Measurement_List. |

##### PE_DS3_WRITE_ET200S_CP (S7-300)

This section contains information on the following topics:

- [Meaning and call - PE_DS3_WRITE_ET200_CP (S7-300)](#meaning-and-call---pe_ds3_write_et200_cp-s7-300)
- [Explanation of the formal parameters of PE_DS3_WRITE_ET200S_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_ds3_write_et200s_cp-s7-300)
- [Condition codes of PE_DS3_WRITE_ET200S_CP (S7-300)](#condition-codes-of-pe_ds3_write_et200s_cp-s7-300)

###### Meaning and call - PE_DS3_WRITE_ET200_CP (S7-300)

###### Significance and how it works

PE_DS3_WRITE_ET200_CP is used in the CPU of the CP 300 as a PROFIenergy controller to transfer the settings for switching behavior from power modules to an ET 200S. The switching behavior for up to 8 slots (in this case: power modules) can be transferred.

PE_DS3_WRITE_ET200_CP is not a PROFIenergy program block.

###### Call interface in FBD representation

![Call interface in FBD representation](images/42811153163_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[PROFIenergy (S7-300)](#profienergy-s7-300-1)
  
[PROFIenergy program blocks for the CP 300 (S7-300)](#profienergy-program-blocks-for-the-cp-300-s7-300)
  
[Explanation of the formal parameters of PE_DS3_WRITE_ET200S_CP (S7-300)](#explanation-of-the-formal-parameters-of-pe_ds3_write_et200s_cp-s7-300)

###### Explanation of the formal parameters of PE_DS3_WRITE_ET200S_CP (S7-300)

###### Explanation of the formal parameters of PE_DS3_WRITE_ET200_CP

| Parameters | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD | I, Q, M, D, L, const. | Module start address of the CP |
| ENABLE | INPUT | BOOL |  | Starts the processing of the program block on a rising edge. |
| ID | INPUT | WORD |  | Logical address of the header slot of the IO device |
| SLOT_NO_1 | INPUT | INT |  | Slot number of the first power module |
| FUNC_1 | INPUT | INT |  | Specifies the switching behavior for the power module in terms of starting or ending energy-saving pauses  - 0 (FALSE)   - PAUSE_START:     No influence (power module remains turned on)   - PAUSE_STOP:     Turns the power module on again. - 1 (TRUE)   - PAUSE_START:     Turns the power module off.   - PAUSE_STOP:     Turns the power module on again. |
| ... | INPUT | INT |  |  |
| ... | INPUT | INT |  |  |
| SLOT_NO_8 | INPUT | INT |  | Slot number of the eighth power module |
| FUNC_8 | INPUT | INT |  | See "FUNC_1" |
| BUSY | OUTPUT | BOOL | 0: Execution not yet started, completed or aborted  1: Execution active | Condition code of the processing status of the program block |
| DONE | OUTPUT | BOOL | 0: -  1: Data record transferred successfully | This parameter indicates whether or not the job was completed without errors. |
| ERROR | OUTPUT | BOOL | 0: -  1: Errors | Error code |
| STATUS | OUTPUT | WORD |  | Status code |

For the meaning of DONE, ERROR and STATUS, see [Condition codes of PE_DS3_WRITE_ET200S_CP](#condition-codes-of-pe_ds3_write_et200s_cp-s7-300).

###### Condition codes of PE_DS3_WRITE_ET200S_CP (S7-300)

###### Condition codes of PE_DS3_WRITE_ET200_CP

PE_DS3_WRITE_ET200_CP is based on the program block PNIO_RW_REC and returns all condition codes of PNIO_RW_REC, see condition codes of the block PNIO_RW_REC.

---

**See also**

Condition codes of PNIO_RW_REC

### Instructions for programmed connections (S7-300, S7-400)

This section contains information on the following topics:

- [Overview (S7-300, S7-400)](#overview-s7-300-s7-400)
- [IP_CONFIG (S7-300, S7-400)](#ip_config-s7-300-s7-400)
- [Configuration data block (S7-300, S7-400)](#configuration-data-block-s7-300-s7-400)

#### Overview (S7-300, S7-400)

##### Interplay between programming and configuration

You configure connections on the SEND/RECEIVE interface and the IP configuration of a CP either with STEP 7 or you configure them during runtime of the S7 station via the user program. Mixing these variants on a CP is not possible!

##### Principle of programmed configuration

Configuration data for communication connections and the IP configuration can be transferred to the CPU using an instruction called in the user program.

![Principle of programmed configuration](images/9101695755_DV_resource.Stream@PNG-en-US.png)

The configuration DB can be loaded on the CP at any time. The previously applicable connections and configuration data (IP address, subnet mask, default router, NTP time server and other parameters) are overwritten.

Based on the configuration data, the Ethernet CP recognizes that the communication connections must be set up by the user program.

> **Note**
>
> The functions can only be executed if "Not locked" was configured for the module access protection. Refer to the "Options" tab in the properties dialog of the CP (not available for every CP).
>
> The "Set IP address in user program" option must also be enabled (see properties dialog of the CP or the Ethernet interface of the CP, "IP Configuration" tab).

Based on the configuration data, the Ethernet CP recognizes that the communication connections must be set up by the user program.

> **Note**
>
> As soon as the user program transfers the connection data via the IP_CONFIG instruction, the CPU switches the CP briefly to STOP. The CP receives the system data (including the IP address) and the new connection data and processes them during startup (RUN).

##### Quantity framework

A maximum of 64 connections can be specified in the CP_CONFIG instruction. The most important factor, however, is the maximum number of connections supported by the CP type you are using.

##### Special features / restrictions

- Consistency check only in the configuration

  The connection configuration involves consistency checks that are not possible or only possible with restrictions when using the programmed configuration!
- Connection configuration required on the partner

  When configuring specified connections, you implicitly create the connection for the partner; with a programmed configuration, this is not possible! In this case, you must configure suitable connections for the partner.
- Configuring IP access protection

  Using IP access protection gives you the opportunity of restricting communication over the CP of the local S7 station to partners with specific IP addresses. This parameter assignment also applies to programmed communications connections. You either disable IP access protection in the configuration (= default) or authorize the communications partner.
- DHCP / DNS is supported

  With a programmed configuration, IP addressing is also possible using DHCP (and DNS for the mail service).

  The use of a DHCP server is defined in this case in the IP_CONFIG instruction (not in the configuration).
- No connection information when uploading

  When you upload the S7 station data into the project engineering, this does not contain the data of the programmed configuration.
- Configuring connections for CPs with several interfaces

  If you are using CPs with several interfaces ( for example with a gigabit interface), check the device manual to see whether or not the connection configuration is supported for both interfaces.
- PROFINET IO is not possible at the same time

  On a device you intend to operate as a PROFINET IO controller or IO device, it is not possible to set up the connection using FB55 as described here.
- No use of the IP_CONFIG instruction when operating the CP with fault-tolerant S7 connections

  If you configure fault-tolerant S7 connections via the CP, you cannot use the IP_CONFIG instruction for IP configuration of the CP.

---

**See also**

[IP_CONFIG for programmed communications connections (S7-300, S7-400)](#ip_config-for-programmed-communications-connections-s7-300-s7-400)
  
[Configuration data block (S7-300, S7-400)](#configuration-data-block-s7-300-s7-400)

#### IP_CONFIG (S7-300, S7-400)

This section contains information on the following topics:

- [IP_CONFIG for programmed communications connections (S7-300, S7-400)](#ip_config-for-programmed-communications-connections-s7-300-s7-400)
- [Parameters for IP_CONFIG (S7-300, S7-400)](#parameters-for-ip_config-s7-300-s7-400)
- [Reserved port numbers - IP_CONFIG (S7-300, S7-400)](#reserved-port-numbers---ip_config-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-3)

##### IP_CONFIG for programmed communications connections (S7-300, S7-400)

###### Description

The IP_CONFIG instruction transfers the connection data specified in a data block (configuration DB) to the CP. The configuration DB contains all the connection data to allow the connections for the SEND/RECEIVE interface of an Ethernet CP to be set up.

You can use this variant of programmed communication connections as an alternative to connection configuration with STEP 7.

Depending on the size of the configuration DB, the data may be transferred to the CP in several segments. This means that the instruction must continue to be called until it signals complete transfer by setting the DONE bit to 1.

###### Call

Call interface in FBD representation

![Call](images/12881776907_DV_resource.Stream@PNG-de-DE.png)

> **Note**
>
> **No use of the IP_CONFIG instruction when operating the CP with fault-tolerant S7 connections**
>
> If you configure fault-tolerant S7 connections via the CP, you cannot use the IP_CONFIG instruction for IP configuration of the CP.

> **Note**
>
> **Avoid possible double addressing**
>
> If you use the IP_CONFIG instruction, make sure that the assignment of IP addresses is unique. If an address is detected twice, it is possible that the CP will not become active in the network.

---

**See also**

[Overview (S7-300, S7-400)](#overview-s7-300-s7-400)
  
[Configuration data block (S7-300, S7-400)](#configuration-data-block-s7-300-s7-400)
  
[Parameters for IP_CONFIG (S7-300, S7-400)](#parameters-for-ip_config-s7-300-s7-400)
  
[Reserved port numbers - IP_CONFIG (S7-300, S7-400)](#reserved-port-numbers---ip_config-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-3)
  
[On the Internet under entry ID 30374198](http://support.automation.siemens.com/WW/view/de/30374198)

##### Parameters for IP_CONFIG (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains the formal parameters for the call interface of the "IP_CONFIG" instruction:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| ACT | INPUT | BOOL, TIMER, COUNTER | 0,1 | When the instruction is called with ACT = 1, DBxx is sent to the CP.  If the instruction is called with ACT = 0, only the status codes DONE, ERROR and STATUS are updated. |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP with STEP 7, the module start address is displayed in the configuration table. Specify this address here. |
| CONF_DB | INPUT | ANY |  | The parameter points to the start address of the configuration data area in a data block (data type: byte). |
| LEN | INPUT | INT |  | Length information in bytes for the configuration data area. |
| DONE | OUTPUT | BOOL | 0: - 1: Job completed with data transfer. | The parameter indicates whether the configuration data area was completely transferred.  Remember that it may be necessary to call the instruction several times depending on the size of the configuration data area (in several cycles) until the DONE parameter is set to 1 to signal completion of the transfer.  For the meaning of this parameter in conjunction with the ERROR and STATUS parameters, refer to the following table. |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code  For the meaning of this parameter in conjunction with the DONE and STATUS parameters, refer to the following table. |
| STATUS | OUTPUT | WORD | See following table | Status code  For the meaning of this parameter in conjunction with the DONE and ERROR parameters, refer to the following table. |
| EXT_Status | OUTPUT | WORD |  | If an error occurs in the execution of a job, the parameter indicates which parameter was detected as the cause of the error in the configuration DB.  High byte: Index of the parameter field  Low byte: Index of the subfield within the parameter field |

---

**See also**

[IP_CONFIG for programmed communications connections (S7-300, S7-400)](#ip_config-for-programmed-communications-connections-s7-300-s7-400)

##### Reserved port numbers - IP_CONFIG (S7-300, S7-400)

###### Reserved Port Numbers

The following local port numbers are reserved; do not use these in the connection project engineering.

Reserved Port Numbers

| Protocol | Port number | Service |
| --- | --- | --- |
| TCP | 20, 21 | FTP |
| TCP | 25 | SMTP |
| TCP | 80 | HTTP |
| TCP | 102 | RFC1006 |
| TCP | 135 | RPC-DCOM |
| TCP | 502 | ASA application protocol |
| UDP | 161 | SNMP_REQUEST |
| UDP | 34964 | PN IO |
| UDP | 65532 | NTP |
| UDP | 65533 | NTP |
| UDP | 65534 | NTP |
| UDP | 65535 | NTP |

---

**See also**

[IP_CONFIG for programmed communications connections (S7-300, S7-400)](#ip_config-for-programmed-communications-connections-s7-300-s7-400)

##### Parameters DONE, ERROR, STATUS (S7-300, S7-400)

###### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

IP_CONFIG status codes

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| General codes relating to job execution |  |  |  |
| 1 | 0 | 0000<sub>H</sub> | Job completed without errors |
| 0 | 0 | 8181<sub>H</sub> | Job active |
| Errors detected on the interface between CPU and CP. |  |  |  |
| 0 | 1 | 80A4<sub>H</sub> | - Communication error on the K-bus  or  - Data error: Configuration by the user program is not set. |
| 0 | 1 | 80B1<sub>H</sub> | The number of data bytes to be sent exceeds the upper limit for this service. (upper limit = 16 Kbytes) |
| 0 | 1 | 80C4<sub>H</sub> | Communication error The error can occur temporarily; it is usually best to repeat the job in the user program. |
| 0 | 1 | 80D2<sub>H</sub> | Configuration error The module you are using does not support this service. |
| Errors detected in the evaluation of the IP_CONFIG in the CPU or on the interface between CPU and CP. |  |  |  |
| 0 | 1 | 8183<sub>H</sub> | The CP rejects the requested data record number. |
| 0 | 1 | 8184<sub>H</sub> | System error or bad parameter type. (data type of the ANY pointer CONF_DB not OK)  (Currently only the byte data type is accepted) |
| 0 | 1 | 8185<sub>H</sub> | The value of the LEN parameter is larger than the CONF_DB less the reserved header (4 bytes) or the length information is incorrect. |
| 0 | 1 | 8186<sub>H</sub> | Illegal parameter detected  The ANY pointer CONF_DB does not point to a data block. |
| 0 | 1 | 8187<sub>H</sub> | Illegal status of the IP_CONFIG  Data in the header of CONF_DB was possibly overwritten. |
| Further errors detected on the interface between the CPU and CP. |  |  |  |
| 0 | 1 | 8A01<sub>H</sub> | The status code in the data record is invalid (value is >= 3). |
| 0 | 1 | 8A02<sub>H</sub> | There is no job running on the CP. IP_CONFIG did, however, expect an acknowledgment for the executed job. |
| 0 | 1 | 8A03<sub>H</sub> | There is no job running on the CP and the CP is not ready. IP_CONFIG triggered the first job to read a data record. |
| 0 | 1 | 8A04<sub>H</sub> | There is no job running on the CP and the CP is not ready. IP_CONFIG did, however, expect an acknowledgment for the executed job. |
| 0 | 1 | 8A05<sub>H</sub> | A job is running, there has, however, not been an acknowledgment yet. IP_CONFIG, however, triggered the first job to read a data record. |
| 0 | 1 | 8A06<sub>H</sub> | A job is completed. IP_CONFIG, however, triggered the first job to read a data record. |
| Errors detected when evaluating IP_CONFIG on the CP. |  |  |  |
| 0 | 1 | 8B01<sub>H</sub> | Communication error  The DB could not be transferred. |
| 0 | 1 | 8B02<sub>H</sub> | Parameter error  Double parameter field |
| 0 | 1 | 8B03<sub>H</sub> | Parameter error  The subfield in the parameter field is not permitted. |
| 0 | 1 | 8B04<sub>H</sub> | Parameter error  The length specified in the instruction does not match the length of the parameter fields / subfields. |
| 0 | 1 | 8B05<sub>H</sub> | Parameter error  The length of the parameter field is invalid. |
| 0 | 1 | 8B06<sub>H</sub> | Parameter error  The length of the subfield is invalid. |
| 0 | 1 | 8B07<sub>H</sub> | Parameter error  The ID of the parameter field is invalid |
| 0 | 1 | 8B08<sub>H</sub> | Parameter error  The ID of the subfield is invalid |
| 0 | 1 | 8B09<sub>H</sub> | System error  The connection does not exist |
| 0 | 1 | 8B0A<sub>H</sub> | Data error  The content of the subfield is not correct. |
| 0 | 1 | 8B0B<sub>H</sub> | Structure error  A subfield exists twice. |
| 0 | 1 | 8B0C<sub>H</sub> | Data error  The parameter does not contain all the necessary parameters. |
| 0 | 1 | 8B0D<sub>H</sub> | Data error  The CONF_DB does not contain a parameter field for system data. |
| 0 | 1 | 8B0E<sub>H</sub> | Data error / structure error  The CONF_DB type is invalid. |
| 0 | 1 | 8B0F<sub>H</sub> | System error  The CP does not have enough resources to process CONF_DB completely. |
| 0 | 1 | 8B10<sub>H</sub> | Data error  Configuration by the user program is not set. |
| 0 | 1 | 8B11<sub>H</sub> | Data error  The specified type of the parameter field is invalid. |
| 0 | 1 | 8B12<sub>H</sub> | Data error  Too many connections were specified (either in total or too many for a specific type; for example, only one E­mail connection is possible). |
| 0 | 1 | 8B13<sub>H</sub> | CP­internal error |
| 0 | 1 | 8B14<sub>H</sub> | The active protection level does not permit the action of making changes. |
| Further errors detected on the program interfaces within the CPU (system instruction errors). |  |  |  |
| 0 | 1 | 8F22<sub>H</sub> | Area length error reading a parameter (e.g. DB too short). |
| 0 | 1 | 8F23<sub>H</sub> | Area length error writing a parameter (e.g. DB too short). |
| 0 | 1 | 8F24<sub>H</sub> | Area error reading a parameter. |
| 0 | 1 | 8F25<sub>H</sub> | Area error writing a parameter. |
| 0 | 1 | 8F28<sub>H</sub> | Alignment error reading a parameter. |
| 0 | 1 | 8F29<sub>H</sub> | Alignment error writing a parameter. |
| 0 | 1 | 8F30<sub>H</sub> | The parameter is in the write­protected first current data block. |
| 0 | 1 | 8F31<sub>H</sub> | The parameter is in the write­protected second current data block. |
| 0 | 1 | 8F32<sub>H</sub> | The parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | DB number error |
| 0 | 1 | 8F3A<sub>H</sub> | The target area was not loaded (DB). |
| 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the I/O area. |
| 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the I/O area. |
| 0 | 1 | 8F44<sub>H</sub> | Access to a parameter to be read during execution of the instruction is prevented. |
| 0 | 1 | 8F45<sub>H</sub> | Access to a parameter to be written during execution of the instruction is prevented. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error  For example, an illegal ANY reference was detected. |

---

**See also**

[IP_CONFIG for programmed communications connections (S7-300, S7-400)](#ip_config-for-programmed-communications-connections-s7-300-s7-400)

#### Configuration data block (S7-300, S7-400)

This section contains information on the following topics:

- [Configuration data block (CONF_DB) (S7-300, S7-400)](#configuration-data-block-conf_db-s7-300-s7-400)
- [Parameter field for system data (IP configuration) (S7-300, S7-400)](#parameter-field-for-system-data-ip-configuration-s7-300-s7-400)
- [Subfield types (S7-300, S7-400)](#subfield-types-s7-300-s7-400)
- [Parameter fields for connection types (S7-300, S7-400)](#parameter-fields-for-connection-types-s7-300-s7-400)
- [Parameter field for TCP connection (S7-300, S7-400)](#parameter-field-for-tcp-connection-s7-300-s7-400)
- [Parameter field for UDP connection (S7-300, S7-400)](#parameter-field-for-udp-connection-s7-300-s7-400)
- [Parameter field for an ISO­on­TCP connection (S7-300, S7-400)](#parameter-field-for-an-isoontcp-connection-s7-300-s7-400)
- [Parameter field for an E­mail connection (S7-300, S7-400)](#parameter-field-for-an-email-connection-s7-300-s7-400)
- [Parameter field for FTP connection (S7-300, S7-400)](#parameter-field-for-ftp-connection-s7-300-s7-400)

##### Configuration data block (CONF_DB) (S7-300, S7-400)

###### Meaning

The configuration data block (CONF_DB) contains all the connection data and configuration data (IP address, subnet mask, default router, NTP time server and other parameters) for an Ethernet CP. The configuration data block is transferred to the CP with the IP_CONFIG instruction.

###### Block and Data Structure

The graphic below shows the following:

- Structure resulting from parameter fields and subfields

  - The connections and specific system data are is described by an identically structured parameter field.
  - Individual parameters are characterized by subfields.
- Offset range

  The CONF_DB can start at any point within a data block as specified by an offset range. The address (or offset) must simply be an even number.

  ![Block and Data Structure](images/22791462027_DV_resource.Stream@PNG-en-US.png)

  | Symbol | Meaning |
  | --- | --- |
  | ① | Parameter fields are described below in [Parameter field for system data (IP configuration)](#parameter-field-for-system-data-ip-configuration-s7-300-s7-400) |
  | ② | Subfield types are described below in [Parameter fields for connection types](#parameter-fields-for-connection-types-s7-300-s7-400) |

##### Parameter field for system data (IP configuration) (S7-300, S7-400)

###### Meaning

Below, you will find the parameter field for system data relevant to the IP configuration of the CP and the subfields that need to be specified in it.

Some applications do not require all the subfield types - refer to the table for details.

###### Layout

On CPs with several interfaces, the structure of the parameter field described below applies only to the PROFINET interface.

- **Type = 0**

- **ID = 0**

- Number of subfields = n

- Subfield 1

- Subfield 2

- Subfield n

...

###### Usable subfields

| Subfield |  | Parameter |  |  |
| --- | --- | --- | --- | --- |
| ID | Type | Special features / notes | Application ***) |  |
| 1 | SUB_IP_V4 | Local IP address |  | ++ |
| 2 | SUBNET_MASK | - |  | ++ |
| 8 | SUB_DEF_ROUTER | - |  | + |
| 4 | SUB_DNS_SERV_ADDR <sup>*)</sup> | This subfield can occur from 0 to 4 times. The first entry is the primary DNS server. |  | + |
| 14 | SUB_DHCP_ENABLE | 0: No DHCP  1: DHCP |  | + |
| 15 | SUB_CLIENT_ID | -  Note: Only useful when SUB_DHCP_ENABLE = 1 |  | + |
| 30**) | SUB_DEVICE_NAME | Device name complying with PROFINET IO convention  Enter a device name to make the device individually recognizable for analysis and diagnostics in the network. |  | + |
| *)The subfield type is used only for E-mail connections.  **) ID is supported only be certain CP types.  ***) ++ = mandatory; + = optional |  |  |  |  |

---

**See also**

[Subfield types (S7-300, S7-400)](#subfield-types-s7-300-s7-400)

##### Subfield types (S7-300, S7-400)

Different parameters are required depending on the parameter field. Each parameter is described by a subfield. Which subfields are required is explained in the descriptions of the system data and the connection types in the previous sections.

Each subfield consists of the specific parameter section and the header (4 Byte).

###### Example

The following excerpt from a CONF_DB illustrates the structure of a subfield based on the example of the SUBNET_MASK subfield type.

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| +14.0 | Sub_field_2 | STRUCT |  | // Subfield 2 type SUBNET_MASK |
| +0.0 | Sub_field_ID | INT | 2 | // Subfield ID |
| +2.0 | Sub_field_len | INT | 8 | // Total length of the subfield in bytes |
| +4.0 | Parameter | STRUCT |  | Parameter range of SUBNET_MASK |
| +0.0 | Value_1 | BYTE | B#16#FF |  |
| +1.0 | Value_2 | BYTE | B#16#FF |  |
| +2.0 | Value_3 | BYTE | B#16#FF |  |
| +3.0 | Value_4 | BYTE | B#16#0 |  |
| =4.0 | END_ | STRUCT |  |  |
| =8.0 | END_ | STRUCT |  |  |

###### In total, the following subfield types are available:

| Subfield ID <sup>1)</sup> | Subfield type | Subfield length (in bytes) | Meaning of the Parameter |
| --- | --- | --- | --- |
| 1 | SUB_IP_V4 | 4 + 4 | IP address according to IPv4 |
| 2 | SUBNET_MASK | 4 + 4 | Subnet mask |
| 3 | SUB_DNS_NAME | Length of DNS name + 4 | DNS name |
| 4 | SUB_DNS_SERV_ADDR | 4 + 4 | DNS server address |
| 8 | SUB_DEF_ROUTER | 4 + 4 | IP address of default router |
| 9 | SUB_LOC_PORT | 2 + 4 | Local port |
| 10 | SUB_REM_PORT | 2 + 4 | Remote port, also for E­mail connections |
| 11 | SUB_LOC_TSAP | TSAP length + 4 | Local TSAP |
| 12 | SUB_REM_TSAP | TSAP length + 4 | Remote TSAP |
| 13 | SUB_EMAIL_SENDER | Length of the sender E­mail address + 4 | E­mail address of the sender |
| 14 | SUB_DHCP_ENABLE | 2 + 4 | Obtain an IP address from a DHCP server  - Range of values:   0 = no DHCP    1 = DHCP   (optional) |
| 15 | SUB_CLIENT_ID | Length of the client ID + 4 | (optional) |
| 18 | SUB_CONNECT_NAME | Length of the name + 4 | Name of the connection Possible characters are: a...z, A...Z, 0...9, -, _ |
| 19 | SUB_LOC_MODE | 1 + 4 | Local mode of the connection  - Range of values:   0x00 = SEND/RECV   0x01 = FTP protocol (TCP connection only)   0x10 = S5 addressing mode for FETCH/WRITE *)   0x20 = SPEED SEND/RECV (permitted only for CP 443-1 Advanced)   0x80 = FETCH *)   0x40 = WRITE *)   If you do not set the parameter, the default setting is SEND/RECV.  Note:  FETCH / WRITE require the passive connection establishment setting (see SUB_CON_ESTABL. |
| 20 | SUB_REM_MODE | 1 + 4 | Setting the mode on the communication partner.  (not currently supported) |
| 21 | SUB_KBUS_ADR | 5 | KBUS address of the CPU (relevant only for S7-400) |
| 22 | SUB_CON_ESTABL | 1 + 4 | Type of connection establishment.  With this option, you specify whether connection establishment from this S7 station is active or passive.  - Range of values:   0 = passive    1 = active |
| 23 | SUB_ADDR_IN_DATA-BLOCK | 1 + 4 | Select free UDP connection.  The remote node is entered in the job header of the job buffer by the user program when it calls AG_SEND. This allows any node on Ethernet/LAN/WAN to be reached.  - Range of values:   1 = free UDP connection   0 = other   The parameter is practical only for a UDP connection. |
| 24 | SUB_NTP_SERVER | 4 + 4 | The subfield defines an NTP server from which the CP can obtain its time via the NTP protocol.  For the situation when one or more NTP servers are defined, up to 4 subfields of ID 24 can be defined.  The subfields of ID 24 may only be installed in the system parameter field type 0 / ID 0. |
| 30 | SUB_DEVICE_NAME | Length of the name + 4 | Device name complying with PROFINET IO convention  The device name must comply with DNS conventions, in other words;   - Restriction to a total of 127 characters (letters, numbers, hyphen or period) - Parts of the name within the device name; in other words, a string between two periods, must not exceed a maximum of 63 characters. - No special characters such as umlauts (ä, ö etc.), brackets, underscore, slash, blank etc. The dash (hyphen) is the only permitted special character. - The device name must not begin or end with the "-" or "." character, nor may either of these be the last character. - The device name must not begin with numbers. - The device name must not have the format n.n.n.n (n = 0...999). - The device name must not begin with the character string "port-xyz-" (x, y, z = 0...9). |
| 1) Note: ID numbers not listed are not currently used. |  |  |  |

##### Parameter fields for connection types (S7-300, S7-400)

###### General

Below, you will see which values need to be entered in the parameter fields and which subfields are used for the various connection types.

Some applications do not require all the subfield types - refer once again to the table for details.

###### Connection ID

The ID parameter that precedes each connection parameter field beside the type ID is particularly important.

On programmed connections, you can assign this ID freely within the permitted range of values. You must then use this ID on the call interface of the FCs for the SEND/RECV interface to identify the connection.

Range of values for the connection ID:

- S7-400: 1,2...64
- S7-300: 1,2...16

---

**See also**

[Subfield types (S7-300, S7-400)](#subfield-types-s7-300-s7-400)

##### Parameter field for TCP connection (S7-300, S7-400)

###### Layout

Enter the parameters in the parameter field for TCP connections as follows:

- **Type = 1 ->** 
  ①

- **ID = connection ID ->** 
  ②

- Number of subfields = n

- Subfield 1

- Subfield 2

- Subfield n

...

Legend:

① Identifier for the connection type

② Freely selectable connection reference; must be specified in AG_SEND / AG_RECV.  
Range of values for the connection ID:  
for S7-400: 1, 2...64  
for S7-300: 1,2...16

###### Usable subfields

| Subfield |  | Parameter |  |
| --- | --- | --- | --- |
| ID | Type | Special features / notes | Application ***) |
| 1 | SUB_IP_V4 | IP address of the partner | ++<sup> *)</sup> |
| 9 | SUB_LOC_PORT | - | ++ |
| 10 | SUB_REM_PORT | - | ++<sup> **)</sup> |
| 18 | SUB_CONNECT_NAME | - | + |
| 19 | SUB_LOC_MODE | - | + |
| 21 | SUB_KBUS_ADR | This value is always set to 2 for CPs for the S7­300 and does not need to be specified. | ++ (for S7-400) |
| 22 | SUB_CON_ESTABL | - | ++ |
| *) optional for a passive connection.  ***) ++ = mandatory; + = optional |  |  |  |

---

**See also**

[Subfield types (S7-300, S7-400)](#subfield-types-s7-300-s7-400)

##### Parameter field for UDP connection (S7-300, S7-400)

###### Layout

Enter the parameters in the parameter field for UDP connections as follows:

- **Type = 2 ->** 
  ①

- **ID = connection ID ->** 
  ②

- Number of subfields = n

- Subfield 1

- Subfield 2

- Subfield n

...

Legend:

① Identifier for the connection type

② Freely selectable connection reference; must be specified in AG_SEND / AG_RECV.  
Range of values for the connection ID:  
for S7-400: 1, 2...64  
for S7-300: 1,2...16

###### Usable subfields

| Subfield |  | Parameter |  |
| --- | --- | --- | --- |
| ID | Type | Special features / notes | Application ***) |
| 1 | SUB_IP_V4 | IP address of the partner | ++ |
| 9 | SUB_LOC_PORT | - | ++ |
| 10 | SUB_REM_PORT | - | ++ |
| 18 | SUB_CONNECT_NAME | - | + |
| 19 | SUB_LOC_MODE | - | + |
| 21 | SUB_KBUS_ADR | This value is always set to 2 for CPs for the S7­300 and does not need to be specified. | ++ (for S7-400) |
| 23 | SUB_ADDR_IN_DATABLOCK | If the "Free UDP connection" is selected for this parameter, the parameters SUB_IP_V4 and SUB_REM_PORT are omitted. | + |
| ***) ++ = mandatory; + = optional |  |  |  |

---

**See also**

[Subfield types (S7-300, S7-400)](#subfield-types-s7-300-s7-400)

##### Parameter field for an ISO­on­TCP connection (S7-300, S7-400)

###### Layout

Enter the parameters in the parameter field for ISO-on-TCP connections as follows:

- **Type = 3 ->** 
  ①

- **ID = connection ID ->** 
  ②

- Number of subfields = n

- Subfield 1

- Subfield 2

- Subfield n

...

Legend:

① Identifier for the connection type

② Freely selectable connection reference; must be specified in AG_SEND / AG_RECV.  
Range of values for the connection ID:  
for S7-400: 1, 2...64  
for S7-300: 1,2...16

###### Usable subfields

| Subfield |  | Parameter |  |
| --- | --- | --- | --- |
| ID | Type | Special features / notes | Application ***) |
| 1 | SUB_IP_V4 | IP address of the partner | <sup>++ *)</sup> |
| 11 | SUB_LOC_TSAP | - | ++ |
| 12 | SUB_REM_TSAP | - | ++<sup> *)</sup> |
| 18 | SUB_CONNECT_NAME | - | + |
| 19 | SUB_LOC_MODE | - | + |
| 21 | SUB_KBUS_ADR | This value is always set to 2 for CPs for the S7­300 and does not need to be specified. | ++ (for S7-400) |
| 22 | SUB_CON_ESTABL | - | ++ |
| *) optional for a passive connection.  ***) ++ = mandatory; + = optional |  |  |  |

---

**See also**

[Subfield types (S7-300, S7-400)](#subfield-types-s7-300-s7-400)

##### Parameter field for an E­mail connection (S7-300, S7-400)

###### Meaning

To send E­mails, one E­mail connection must be set up per Advanced CP. The E­mail connection specifies the mail server via which all the mails sent by the Advanced CP are delivered.

###### Layout

Enter the parameters in the parameter field for E-mail connections as follows:

- **Type = 4 ->** 
  ①

- **ID = connection ID ->** 
  ②

- Number of subfields = n

- Subfield 1

- Subfield 2

- Subfield n

...

Legend:

① Identifier for the connection type

② Freely selectable connection reference; must be specified in AG_SEND / AG_RECV.  
Range of values for the connection ID:  
for S7-400: 1, 2...64  
for S7-300: 1,2...16

###### Usable subfields

| Subfield |  | Parameter |  |
| --- | --- | --- | --- |
| ID | Type | Special features / notes | Application ***) |
| 1 | SUB_IP_V4 | IP address of the mail server, over which the E­mails are sent.   You can specify an absolute or alias IP address.   The use of an alias assumes that the Advanced CP knows the address of the domain name server (DNS). This entry must be made when configuring the Advanced CP in HW Config. For more detailed information refer to the online help. | ++ / + <sup>*)</sup> |
| 3 | SUB_DNS_NAME | DNS name of the E­mail server | ++ / + <sup>*)</sup> |
| 13 | SUB_EMAIL_SENDER | E­mail address of the sender | ++ |
| 18 | SUB_CONNECT_NAME | - | + |
| 21 | SUB_KBUS_ADR | This value is always set to 0 for CPs for the S7­300 and does not need to be specified. | ++ (for S7-400) |
| 22 | SUB_CON_ESTABL | - | ++ |
| **) The parameters SUB_IP_V4 and SUB_DNS_NAME are mutually exclusive; one or the other parameter must be specified.  ***) ++ = mandatory; + = optional |  |  |  |

> **Note**
>
> Mail server ports are "well­known ports" and do not need to be specified.

---

**See also**

[Subfield types (S7-300, S7-400)](#subfield-types-s7-300-s7-400)

##### Parameter field for FTP connection (S7-300, S7-400)

###### Meaning

To run an FTP job sequence between the S7 station acting as the FTP client and an FTP server, the Advanced CP must establish a connection to the S7 CPU. This connection is known as an FTP connection.

FTP connections are TCP connections, with the parameter SUB_LOC_MODE set to the "FTP" mode.

###### Layout

Enter the parameters in the parameter field for FTP connections as follows:

- **Type = 1 ->** 
  ①

- **ID = connection ID ->** 
  ②

- Number of subfields = n

- Subfield 1

- Subfield 2

- Subfield n

...

Legend:

① Identifier for the connection type

② Freely selectable connection reference; must be specified in AG_SEND / AG_RECV.  
Range of values for the connection ID:  
for S7-400: 1, 2...64  
for S7-300: 1,2...16

###### Usable subfields

| Subfield |  | Parameter |  |
| --- | --- | --- | --- |
| ID | Type | Special features / notes | Application ***) |
| 18 | SUB_CONNECT_NAME | - | + |
| 19 | SUB_LOC_MODE | here: 0x01 = FTP protocol | ++ |
| 21 | SUB_KBUS_ADR | This value is always set to 0 for CPs for the S7­300 and does not need to be specified. | ++ (for S7-400) |
| ***) ++ = mandatory; + = optional |  |  |  |

---

**See also**

[Subfield types (S7-300, S7-400)](#subfield-types-s7-300-s7-400)

### Instructions for FTP services (S7-300, S7-400)

This section contains information on the following topics:

- [FTP_CMD for FTP services (S7-300, S7-400)](#ftp_cmd-for-ftp-services-s7-300-s7-400)
- [Structure and use of the file DB (S7-300, S7-400)](#structure-and-use-of-the-file-db-s7-300-s7-400)

#### FTP_CMD for FTP services (S7-300, S7-400)

This section contains information on the following topics:

- [Migration from FC 40-44 to FB40 (S7-300, S7-400)](#migration-from-fc-40-44-to-fb40-s7-300-s7-400)
- [Overview of FTP_CMD (S7-300, S7-400)](#overview-of-ftp_cmd-s7-300-s7-400)
- [Input parameter - FTP_CMD (S7-300, S7-400)](#input-parameter---ftp_cmd-s7-300-s7-400)
- [Output parameters and status information FTP_CMD (S7-300, S7-400)](#output-parameters-and-status-information-ftp_cmd-s7-300-s7-400)

##### Migration from FC 40-44 to FB40 (S7-300, S7-400)

###### Comparison of the FTP_CMD program block with older functions FC40...44

All CPs with FTP functionality support the functions FC40...44. This means that existing user programs can be used unchanged.

If you want to convert from the FTP functions FC40...44 to FTP_CMD, you will need to modify your user program.

The following table shows the FTP_CMD commands used to replace the functions FC40...44.

- Correlation is indicated by "X".
- Where there is no correlation, this is indicated by "-".

|  | Commands of the "CMD" parameter of FTP_CMD |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Older FTP functions FC40...44 | CMD = 1 | CMD = 2 | CMD = 3 | CMD = 4 | CMD = 5 | CMD = 6  CMD = 7 CMD = 17 |
| FC40 | X <sup>1)</sup> |  |  |  |  |  |
| FC41 |  | X <sup>2)</sup> |  |  |  |  |
| FC42 |  |  | X <sup>3)</sup> |  |  |  |
| FC43 |  |  |  | X <sup>4)</sup> |  |  |
| FC44 |  |  |  |  | X |  |
|  |  |  |  |  |  | - |
| <sup>1)</sup>...<sup>4)</sup> The parameters of FC40...43 and CMD 1...4 (FTP_CMD) are not identical. (See table below) |  |  |  |  |  |  |

The corresponding parameters that specify a particular function in the functions FC40...FC43 or in the commands of FTP_CMD are listed in the following table.

| Parameters of the FC |  |  | Parameters in FTP_CMD (with CMD 1...4) |  |
| --- | --- | --- | --- | --- |
| FC40: | LOGIN | → | CMD = 1: | NAME_STR |
| FC41: | FILE_NAME | → | CMD = 2: | NAME_STR |
| FC42: | FILE_NAME | → | CMD = 3: | NAME_STR |
| FC43: | FILE_NAME | → | CMD = 4: | NAME_STR |
| FC40...43: | BUFFER_DB_NR | → | Omitted (replaced by instance DB) |  |

---

**See also**

[Overview of FTP_CMD (S7-300, S7-400)](#overview-of-ftp_cmd-s7-300-s7-400)

##### Overview of FTP_CMD (S7-300, S7-400)

###### Meaning

Using the FTP_CMD instruction, you can establish FTP connections and transfer files from and to an FTP server.

The advantages of FTP_CMD are as follows:

- Simplification in the user program by using a command variable instead of different function calls
- Additional function "APPEND"

  "APPEND" allows data to be appended to an existing file.
- Additional function "RETR_PART"

  "RETR_PART" allows selected data areas to be retrieved from a file.
- Additional function "CONNECT_TLS_PRIVATE"

  "CONNECT_TLS_PRIVATE" allows the establishment of secure SSL connections
- The AG_SEND (FC5) function is not required here.

###### Validity

FB40 can be used as of the following module types:

- As of CP 343-1 Advanced (GX30* / GX31)
- As of CP 443-1 Advanced (GX20* / GX30)

  *) "CONNECT-TLS-PRIVATE" function cannot be used.

###### Call interface

Call interface in FBD representation

![Call interface](images/9484546955_DV_resource.Stream@PNG-de-DE.png)

###### System functions called

The following system functions are called by the program block FTP_CMD:

SFC 1, SFC 20, SFC 24, SFC 58, SFC 59

> **Note**
>
> Note that the FTP client services of old SIMATIC S7-300 CPUs, for example the CPU 312 or CPU 315-1AF01, cannot be used because they do not support SFC24.

---

**See also**

[Structure and use of the file DB (S7-300, S7-400)](#structure-and-use-of-the-file-db-s7-300-s7-400)
  
[Output parameters and status information FTP_CMD (S7-300, S7-400)](#output-parameters-and-status-information-ftp_cmd-s7-300-s7-400)
  
[Input parameter - FTP_CMD (S7-300, S7-400)](#input-parameter---ftp_cmd-s7-300-s7-400)
  
[Migration from FC 40-44 to FB40 (S7-300, S7-400)](#migration-from-fc-40-44-to-fb40-s7-300-s7-400)

##### Input parameter - FTP_CMD (S7-300, S7-400)

###### Explanation of the input parameters

Each FTP block call must be supplied with the following input parameters:

Formal parameters of FB40 (FTP_CMD) - input parameters

| Parameter | Declaration | Type | Range of values | Meaning / remarks |
| --- | --- | --- | --- | --- |
| ID | INPUT | INT | For S7-300:  1, 2...16  For S7-400:  1, 2...64 | The FTP jobs are handled on FTP connections. The parameter identifies the connection being used. |
| LADDR | INPUT | WORD |  | Module start address  When you call an FC, you transfer the module start address of the ADVANCED-CP in the LADDR parameter.  You will find the module start address of the ADVANCED CP in the configuration of the ADVANCED CP in "Properties>Addresses>Inputs". |
| CMD | INPUT | BYTE | See table below  - FTP commands in the "CMD" parameter | FTP commands executed when FTP_CMD is called. You will find further information following the table.  If a command is not supported by the CP firmware, an error message with STATUS = 8F6B<sub>H</sub> is output.  Examples of FTP commands:  - RETRIEVE: B#16#3 - CONNECT_TLS_PRIVATE: B#16#11 |
| NAME_STR | INPUT | ANY | Only "BYTE" is permitted as VARTYPE. | The address references a data block area. Here, you specify the address and length of the data area in which the target data is entered.  - When CMD = 1, 17:   With this command, the "NAME_STR" parameter specifies the FTP server to be addressed over the FTP connection with the following attributes: - IP address of the FTP server - User name - Password for the login   These values must be specified as three consecutive strings in the destination range of the ANY pointer. - When CMD = 2, 3, 4, 6, 7:   With this command, the "NAME_STR" parameter specifies the file name on the FTP server, in other words, the data source or data destination. The file name is specified as a string in the destination range of the ANY pointer. - When CMD = 5: Parameter not relevant   You will find example of content further below. |
| FILE_DB_NR | INPUT | INT |  | The data block specified here contains the file DB to be read / written.  The parameter is relevant only when CMD = 2, 3, 6 and 7. |
| OFFSET | INPUT | DWORD |  | Only when CMD = 7:  Offset in bytes starting at which the file will be read. |
| LEN | INPUT | DWORD |  | Only when CMD = 7:  Sublength in bytes that is read starting at the value specified in "OFFSET".  Special features:  - If "DW#16#FFFFFFFF" is specified, the available rest of the file will be read.   Result OK (DONE = 1, STATUS = 0) if no other error occurred. - When OFFSET > length of the original file:   The length of the destination file is displayed in this case in the ACT_LENGTH parameter in the file DB: 0 bytes on the CPU.   Result OK (DONE = 1, STATUS = 0) if no other error occurred. - When OFFSET + LEN > length of the original file (and LEN ≠ 0xFFFFFFFF):   The length of the destination file is displayed in this case in the ACT_LENGTH parameter in the file DB: Available bytes starting at "OFFSET".   Result OK (DONE = 1, STATUS = 0) if no other error occurred. |

###### FTP commands in the "CMD" parameter

The following table explains the meaning of the commands of the "CMD" parameter and which input parameters need to be supplied. The ID and LADDR parameters must always be set to identify the connection.

| CMD | Relevant input parameters (in addition to ID and LADDR) | Meaning / handling |
| --- | --- | --- |
| 0 (NOOP) | - | The called instruction does not execute any action. The status codes are set as follows when these parameters are supplied:  - DONE=1; ERROR=0; STATUS=0 |
| 1 (CONNECT) | NAME_STR | With this command, the FTP client establishes an FTP connection to an FTP server (port 21).  The connection is available under the connection ID specified here for all further FTP commands. Data is then exchanged with the FTP server specified for this user. |
| 2 (STORE) | NAME_STR FILE_DB_NR | This function call transfers a data block (file DB) from the FTP client (S7-CPU) to the FTP server.   Caution: If the file (file DB) already exists on the FTP server, it will be overwritten. |
| 3 (RETRIEVE) | NAME_STR FILE_DB_NR | This function call transfers a file from the FTP server to the FTP client (S7-CPU).   Caution: If the data block (file DB) on the FTP client already contains a file, it will be overwritten. |
| 4 (DELETE) | NAME_STR | With this function call, you delete a file on the FTP server. |
| 5 (QUIT) | No others | With this function call, you establish the FTP connections selected with the ID. |
| 6 (APPEND) | NAME_STR FILE_DB_NR | Similar to "STORE", the "APPEND" command saves a file on the FTP server. With "APPEND", the file on the FTP server is, however, not overwritten. The new content is appended to the existing file.  If the file (file DB) does not exist on the FTP server, it will be created. |
| 7 (RETR_PART) | NAME_STR FILE_DB_NR OFFSET LEN | Using the "RETR_PART" command (retrieve part) , you can request a section of a file from the FTP server.   If very large files are involved, this allows you to restrict the read to the part you currently require.  To do this, you need to know the structure of the file.   Enter the required part of the file using the two parameters "OFFSET" and "LEN" in FB40. |
| 17 (CONNECT_TLS_PRIVATE) | NAME_STR | With the "CONNECT_TLS_PRIVATE" command, the FTP client sets up an SSL-secured FTP connection (FTPS) to an FTP server (port 21). The data of the control connection and the data connection is secure.  The connection is available under the connection ID specified here for all further FTP commands. Data is then exchanged with the FTP server specified for this user.  Requirements:  - The "Security" option must be activated on the CP. - For the FTP connection secured with SSL, certificates must be provides in the CP configuration. |

###### Examples of the content of the "NAME_STR" parameter

The parameter record has the following content:

Content of the parameter record for CMD = 1, 17

| Relative address <sup>2)</sup> | Name | Type <sup>1)</sup> | Example | Meaning |
| --- | --- | --- | --- | --- |
| 0.0 | ip_address | STRING[100] | ’142.11.25.135’ | IP address of the FTP server |
| 102.0 | username | STRING[32] | 'user' | User name for the login on the FTP server |
| 136.0 | password | STRING[32] | 'password' | Password for the login on the FTP server |
| 1) The maximum possible string length is specified 2) The specified values relate to the string lengths specified in "Type". |  |  |  |  |

Content of the parameter record for CMD = 2, 3, 4, 6, 7

| Relative address <sup>2)</sup> | Name | Type <sup>1)</sup> | Example | Meaning |
| --- | --- | --- | --- | --- |
| 170.0 | filename | STRING[ 220] or  STRING[212] | 'plant1/tank2/press.dat' | File name of the source or destination file  Note: If CMD=7 (RETR_PART), the maximum length of the file name is limited to 212 characters. |
| 1) The maximum possible string length is specified 2) The specified values relate to the string lengths specified in "Type". |  |  |  |  |

---

**See also**

[Overview of FTP_CMD (S7-300, S7-400)](#overview-of-ftp_cmd-s7-300-s7-400)

##### Output parameters and status information FTP_CMD (S7-300, S7-400)

###### Introduction

For status evaluation, the following parameters must be evaluated in the user program:

Formal parameters of FB40 (FTP_CMD) - output parameters

| Parameter | Declaration | Type | Range of values | Meaning / remarks |
| --- | --- | --- | --- | --- |
| DONE | OUTPUT | BOOL | 0: - 1: Job executed | This parameter indicates whether or not the job was completed without errors. |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code  This parameter signals that the job could not be executed error-free. |
| STATUS | OUTPUT | WORD | See following table | Status code  This parameter supplies detailed information about the execution of the job. |

The DONE, ERROR and STATUS parameters are updated at every block call.

###### Example

During job execution, FTP_CMD returns the following codes:

- DONE=0
- ERROR=0
- STATUS=8181<sub>H</sub>

Meaning: Job still running.

###### Evaluating status codes

> **Note**
>
> For entries coded with 8FxxH in STATUS, refer to the information in the STEP 7 Standard and System Functions reference manual. The chapter describing error evaluation with the RET_VAL output parameter contains detailed information.

FB 40: Meaning of the STATUS parameter in conjunction with DONE and ERROR

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | 0000<sub>H</sub> | No job being executed. |
| 1 | 0 | 0000<sub>H</sub> | Job completed without error. |
| 0 | 0 | 8181<sub>H</sub> | Job active.  If 8181<sub>H</sub> is indicated permanently: The CP is not released for FTP_CMD (an illegal command for the firmware version (CMD 6, CMD 7 or CMD 17) was called.) |
| 0 | 1 | 8090<sub>H</sub> | - No module with this module start address exists. - The block being used does not match the system family being used (remember to use different blocks for S7­300 and S7­400). |
| 0 | 1 | 8091<sub>H</sub> | Module start address not at a double­word boundary |
| 0 | 1 | 8092<sub>H</sub> | Type information in the ANY pointer is not byte |
| 0 | 1 | 80A4<sub>H</sub> | The communication bus connection between the CPU and CP is not established (with newer CPU versions).  This can, for example, be caused by the following:  - No connection configuration - Maximum number of CPs operating at the same time was exceeded |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | Destination area invalid; for example, destination area > 240 bytes. |
| 0 | 1 | 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established (with older CPU versions). (with newer CPU versions, see 80A4<sub>H</sub>) |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | Resources occupied (memory). |
| 0 | 1 | 80C4<sub>H</sub> | Communications error (occurs temporarily, it is usually best to repeat the job in the user program). |
| 0 | 1 | 80D2<sub>H</sub> | Module start address incorrect. |
| 0 | 1 | 8183<sub>H</sub> | The configuration does not match the job parameters. |
| 0 | 1 | 8184<sub>H</sub> | Illegal data type specified for the NAME_STR parameter. |
| 0 | 1 | 8186<sub>H</sub> | ID parameter invalid. ID = 1, 2....64 |
| 0 | 1 | 8302<sub>H</sub> |  |
| 0 | 1 | 8F22<sub>H</sub> | Source area invalid, for example:  Area does not exist in the DB |
| 0 | 1 | 8F23<sub>H</sub> | Area length error writing a parameter (e.g. DB too short). |
| 0 | 1 | 8F24<sub>H</sub> | Area error reading a parameter |
| 0 | 1 | 8F28<sub>H</sub> | Alignment error reading a parameter |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | DB number error |
| 0 | 1 | 8F3A<sub>H</sub> | Area not loaded (DB) |
| 0 | 1 | 8F50<sub>H</sub> | File DB DB 0 or DB does not exist |
| 0 | 1 | 8F51<sub>H</sub> | Specified file DB data area larger than existing data area |
| 0 | 1 | 8F52<sub>H</sub> | File DB in write-protected memory |
| 0 | 1 | 8F53<sub>H</sub> | File DB max. length < current length |
| 0 | 1 | 8F54<sub>H</sub> | File DB does not contain any valid data. |
| 0 | 1 | 8F55<sub>H</sub> | Header status bit: Locked |
| 0 | 1 | 8F56<sub>H</sub> | The NEW bit in the file DB header was not reset |
| 0 | 1 | 8F57<sub>H</sub> | The FTP client does not have write access to the file DB but rather the FTP server (header status bit: WriteAccess). |
| 0 | 1 | 8F60<sub>H</sub> | Bad user data, for example bad IP address of the FTP server |
| 0 | 1 | 8F61<sub>H</sub> | FTP server not obtainable |
| 0 | 1 | 8F62<sub>H</sub> | Possible meanings:  - Job not supported or rejected by FTP server - The FTP server does not support SSL-secured connections. |
| 0 | 1 | 8F63<sub>H</sub> | File transfer aborted by the FTP server |
| 0 | 1 | 8F64<sub>H</sub> | Error on the FTP control connection; data could not be sent or received; the FTP control connection must be established again after such an error. |
| 0 | 1 | 8F65<sub>H</sub> | Error on the FTP data connection; data could not be sent or received. The job must be called again.  This error can, for example, be caused by RETRIEVE (CMD=3) when the addressed file is already open on the FTP server. |
| 0 | 1 | 8F66<sub>H</sub> | Error reading/writing data from/to the CPU (for example DB does not exist or too short) |
| 0 | 1 | 8F67<sub>H</sub> | Error in the FTP client on the CP; for example attempting to open more than the maximum number of FTP connections. |
| 0 | 1 | 8F68<sub>H</sub> | The job was rejected by the FTP client. This error can, for example, be caused by RETRIEVE (CMD=3) when the value for the parameter MAX_LENGTH was selected too low in the file DB header. |
| 0 | 1 | 8F69<sub>H</sub> | The FTP connection is in an incorrect status, for example:  - The connection is called without a previous connection termination (with the same connection ID) - There is a connection termination for a connection that has already been terminated: - A STORE command was sent on a connection that is not established. |
| 0 | 1 | 8F6A<sub>H</sub> | The connection could not be established due to a temporary resource bottleneck.  Remedy: Repeat the block call. |
| 0 | 1 | 8F6B<sub>H</sub> | Possible causes:  - Wrong value for the CMD parameter - An FTP_CMD command is not supported.   Possible cause: Wrong firmware on the CP Remedy: Firmware update |
| 0 | 1 | 8F6C<sub>H</sub> | A value > 7FFF FFF<sub>H</sub> was set in the OFFSET parameter. |
| 0 | 1 | 8F6D<sub>H</sub> | The FTP client does not support SSL-secured connections. |
| 0 | 1 | 8F6F<sub>H</sub> | Possible causes:  - The certificate contains an invalid value for "notBefore". - The certificate is invalid. The "notBefore" entry contains a time after the current time. |
| 0 | 1 | 8F70<sub>H</sub> | Possible causes:  - The certificate contains an invalid value for "notAfter". - The certificate has elapsed: The "notAfter" entry contains a time before the current time. |
| 0 | 1 | 8F71<sub>H</sub> | The issuer certificate of a non-trustworthy certificate could not be found. |
| 0 | 1 | 8F72<sub>H</sub> | The original CA certificate is invalid. This is either not a CA certificate or its expansions are not consistent with the intended purpose. |
| 0 | 1 | 8F73<sub>H</sub> | The original CA certificate is marked as non-trustworthy for the specified purpose. |
| 0 | 1 | 8F74<sub>H</sub> | Other errors occurred during the verification of a certificate. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, for example illegal ANY reference |

---

**See also**

[Overview of FTP_CMD (S7-300, S7-400)](#overview-of-ftp_cmd-s7-300-s7-400)

#### Structure and use of the file DB (S7-300, S7-400)

This section contains information on the following topics:

- [Structure of the data blocks (file DBs) for FTP services - FTP server mode (S7-300, S7-400)](#structure-of-the-data-blocks-file-dbs-for-ftp-services---ftp-server-mode-s7-300-s7-400)
- [Structure of the data blocks (file DBs) for FTP services - FTP client mode (S7-300, S7-400)](#structure-of-the-data-blocks-file-dbs-for-ftp-services---ftp-client-mode-s7-300-s7-400)
- [FILE_DB_HEADER data block as a template (S7-300, S7-400)](#file_db_header-data-block-as-a-template-s7-300-s7-400)

##### Structure of the data blocks (file DBs) for FTP services - FTP server mode (S7-300, S7-400)

###### Procedure

To transfer data with FTP, create data blocks (file DBs) on the CPU of your S7 station. These data blocks must have certain structure to allow them to be handled as transferable files by the FTP services. They consist of the following sections:

- Section 1: File DB header (has a fixed length (20 bytes) and structure)
- Section 2: User data (has a variable length and structure)

###### File DB header for FTP server mode

Note: The file DB header described here is largely identical to the file DB header for client mode. The differences relate to the following parameters:

- WRITE_ACCESS
- FTP_REPLY_CODE

| Parameter | Type | Value / meaning | Supply |
| --- | --- | --- | --- |
| EXIST | BOOL | The EXIST bit indicates whether the user data area contains valid data.  The retrieve FTP command executes the job only when EXIST=1.  - 0:  The file DB does not contain valid user data ("file does not exist"). - 1: The file DB contains valid user data ("file exists"). | The dele FTP command sets EXIST=0;  The store FTP command sets EXIST=1; |
| LOCKED | BOOL | The LOCKED bit is used to restrict access to the file DB.  - 0: The file DB can be accessed. - 1: The file DB is locked. | The stor and retr FTP commands set LOCKED=1 when they are executed.  The following function is also possible when writing from the user program:  The user program on the S7 CPU can set or reset LOCKED during write access to achieve data consistency.  Recommended sequence in the user program:  1. Check LOCKED bit;  if = 0 2. Set WRITEACCESS bit = 0 3. Check LOCKED bit;  if = 0 4. Set LOCKED bit = 1 5. Write data 6. Set LOCKED bit = 0 |
| NEW | BOOL | The NEW bit indicates whether data has been modified since the last read access.  - 0: The content of the file DB is unchanged since the last write access. The user program of the S7 CPU has registered the last modification. - 1: The user program of the S7 CPU has not yet registered the last write access. | After execution, the stor FTP command sets NEW=1  After reading the data, the user program on the S7-CPU must set NEW=0 to allow store to be used again or to be able to delete the file with the dele FTP command. |
| WRITE_ACCESS | BOOL | 0: The FTP client on the PG/PC has no write access rights for the file DBs on the S7 CPU.  1: The FTP client on the PG/PC has write access rights for the file DBs on the S7 CPU. | During the configuration of the DB, the bit is set to an initialization value.  Recommendation:  Whenever possible, the bit should remain unchanged! In special situations, adaptation during operation is possible. |
| ACT_LENGTH | DINT | Current length of the user data area. The content of this field is only valid when EXIST = 1. | The current length is updated following write access. |
| MAX_LENGTH | DINT | Maximum length of the user data area (length of the entire DB less 20 bytes header). | The maximum length should be specified during configuration of the DB. The value can also be modified by the user program during operation. |
| FTP_REPLY_CODE | INT | This parameter is irrelevant in FTP server mode. | Is set to "0" by the FTP server. |
| DATE_TIME | DATE_AND_TIME | Date and time of the last modification to the file.  The content of this field is only valid when EXIST = 1. | The current date is updated following a write access. If the function for forwarding the time of day is used, the entry corresponds to the time that was passed on. If the function for forwarding the time of day is not used, a relative time is entered. This time relates to the startup of the IT-CP (the initialization value is 1.1.1994 0.0 (midnight)). |

##### Structure of the data blocks (file DBs) for FTP services - FTP client mode (S7-300, S7-400)

###### Procedure

To transfer data with FTP, create data blocks (file DBs) on the CPU of your S7 station. These data blocks must have certain structure to allow them to be handled as transferable files by the FTP services. They consist of the following sections:

- Section 1: File DB header (has a fixed length of 20 bytes)
- Section 2: User data (has a variable length and structure)

###### File DB header for FTP client mode

Note: The file DB header described here is largely identical to the file DB header for server mode. The differences relate to the following parameters:

- WRITE_ACCESS
- FTP_REPLY_CODE

| Parameter | Type | Value / meaning | Supply |
| --- | --- | --- | --- |
| EXIST | BOOL | The EXIST bit indicates whether the user data area contains valid data.  The retrieve FTP command executes the job only when EXIST=1.  - 0:  The file DB does not contain valid user data ("file does not exist"). - 1: The file DB contains valid user data ("file exists"). | The dele FTP command sets EXIST=0;  The stor FTP command sets EXIST=1; |
| LOCKED | BOOL | The LOCKED bit is used to restrict access to the file DB.  - 0: The file DB can be accessed. - 1: The file DB is locked. | The stor and retr FTP commands set LOCKED=1 when they are executed.  The following function is also possible when writing from the user program:  The user program on the S7 CPU can set or reset LOCKED during write access to achieve data consistency.  Recommended sequence in the user program:  1. Check LOCKED bit;  if = 0 2. Set WRITEACCESS bit = 0 3. Check LOCKED bit;  if = 0 4. Set LOCKED bit = 1 5. Write data 6. Set LOCKED bit = 0 |
| NEW | BOOL | The NEW bit indicates whether data has been modified since the last read access.  - 0: The content of the file DB is unchanged since the last write access. The user program of the S7 CPU has registered the last modification. - 1: The user program of the S7 CPU has not yet registered the last write access. | After execution, the stor FTP command sets NEW=1  After reading the data, the user program in the S7-CPU must set NEW=0 to allow a new retr command. |
| WRITE_ACCESS | BOOL | 0: The user program (FTP client blocks) has write access rights for the file DBs on the S7 CPU.  1: The user program (FTP client blocks) has no write access rights for the file DBs on the S7 CPU. | During the configuration of the DB, the bit is set to an initialization value.  Recommendation:  Whenever possible, the bit should remain unchanged! In special situations, adaptation during operation is possible. |
| ACT_LENGTH | DINT | Current length of the user data area. The content of this field is only valid when EXIST = 1. | The current length is updated following write access. |
| MAX_LENGTH | DINT | Maximum length of the user data area (length of the entire DB less 20 bytes header). | The maximum length should be specified during configuration of the DB. The value can also be modified by the user program during operation. |
| FTP_REPLY_CODE | INT | Unsigned integer (16-bit) containing the last reply code from FTP as a binary value.  The content of this field is only valid when EXIST = 1. | This is updated by the FTP client when the FTP command is executed. |
| DATE_TIME | DATE_AND_TIME | Date and time of the last modification to the file.  The content of this field is only valid when EXIST = 1. | The current date is updated following a write access. If the function for forwarding the time of day is used, the entry corresponds to the time that was passed on. If the function for forwarding the time of day is not used, a relative time is entered. This time relates to the startup of the IT-CP (the initialization value is 1.1.1994 0.0 (midnight)). |

##### FILE_DB_HEADER data block as a template (S7-300, S7-400)

###### Meaning

The data type FILE_DB_HEADER is predefined for creating a file DB header.

###### Procedure

To transfer data with FTP, create data blocks (file DBs) on the CPU of your S7 station. These data blocks must have certain structure to allow them to be handled as transferable files by the FTP services. They consist of the following sections:

- Section 1: File DB header (has a fixed length of 20 bytes)
- Section 2: User data (has a variable length and structure)

###### Follow the steps outlined below:

1. For the PLC CPU on which you create the user program with the FTP instructions, create a data block of the type "Global DB".
2. Select the line you want to use as the start line for the file DB.
3. From the drop-down list in the "Data type" column, select a structure element of the type FILE_DB_HEADER.

Result: A data structure with the header structure required for the file DB is created.

> **Note**
>
> **"Add new block" function - type selection**
>
> When you create new data blocks, the "FILE_DB_HEADER" block type is also available under the "Type" entry in the drop-down list. Do not use this option! The data block created in this way only contains the header structure and cannot be expanded by the area required for storing user data.

###### FILE_DB_HEADER data block - example and template for the file DB header

In the declaration view, you will see the following structure:

| Address | Name | Type | Initial value | Comment |
| --- | --- | --- | --- | --- |
| 0.0 |  | STRUCT |  |  |
| +0.0 | bit08 | BOOL | FALSE | reserved |
| +0.1 | bit09 | BOOL | FALSE | reserved |
| +0.2 | bit10 | BOOL | FALSE | reserved |
| +0.3 | bit11 | BOOL | FALSE | reserved |
| +0.4 | bit12 | BOOL | FALSE | reserved |
| +0.5 | bit13 | BOOL | FALSE | reserved |
| +0.6 | bit14 | BOOL | FALSE | reserved |
| +0.7 | bit15 | BOOL | FALSE | reserved |
| +1.0 | EXIST | BOOL | FALSE | if TRUE: FileDB content is valid data |
| +1.1 | LOCKED | BOOL | FALSE | if TRUE: FileDB is locked caused by changes of the content |
| +1.2 | NEW | BOOL | FALSE | if TRUE: FileDB content is new and may not be overwritten |
| +1.3 | WRITE_ACCESS | BOOL | FALSE | if TRUE: Ftp-Server of the IT-CP has write access, else Ftp-Server |
| +1.4 | bit04 | BOOL | FALSE | reserved |
| +1.5 | bit05 | BOOL | FALSE | reserved |
| +1.6 | bit06 | BOOL | FALSE | reserved |
| +1.7 | bit07 | BOOL | FALSE | reserved |
| +2.0 | ACT_LENGTH | DINT | L#0 | actual size of the content in bytes (not including the header of 20 bytes) |
| +6.0 | MAX_LENGTH | DINT | L#0 | max. size of the content in bytes (not including the header of 20 bytes) |
| +10.0 | FTP_REPLY_CODE | INT | 0 | last reply code from the remote FTP server |
| +12.0 | DATE_TIME | DATE_AND_TIME | DT#00-1-1-0:0:0.000 | date and time of last change of the content of the FileDB |
| =20.0 |  | END_STRUCT |  |  |

###### Differences in the modes

File DB header for FTP client mode

The file DB header described here is largely identical for the FTP client mode and FTP server mode. The differences relate to the following parameters:

- WRITE_ACCESS
- FTP_REPLY_CODE

Note the ways in which the descriptions of the parameters differ:

- [Structure of the data blocks (file DBs) for FTP services - FTP server mode](#structure-of-the-data-blocks-file-dbs-for-ftp-services---ftp-server-mode-s7-300-s7-400)
- [Structure of the data blocks (file DBs) for FTP services - FTP client mode](#structure-of-the-data-blocks-file-dbs-for-ftp-services---ftp-client-mode-s7-300-s7-400)

### Instructions for ERPC-CP (S7-300)

This section contains information on the following topics:

- [LOGICAL_TRIGGER for the logical trigger (S7-300)](#logical_trigger-for-the-logical-trigger-s7-300)
- [How LOGICAL_TRIGGER works (S7-300)](#how-logical_trigger-works-s7-300)
- [Explanation of the formal parameters for LOGICAL_TRIGGER (S7-300)](#explanation-of-the-formal-parameters-for-logical_trigger-s7-300)
- [LOGICAL_TRIGGER instruction codes (S7-300)](#logical_trigger-instruction-codes-s7-300)
- [The configuration data block (S7-300)](#the-configuration-data-block-s7-300)

#### LOGICAL_TRIGGER for the logical trigger (S7-300)

##### Meaning of the instruction

The LOGICAL_TRIGGER instruction is available if you want to use a logical trigger for ERPC communication.

To start a logical trigger, call the LOGICAL_TRIGGER instruction in the user program of the CPU in OB1.

Further blocks are required for the LOGICAL_TRIGGER instruction call:

- An automatically generated instance DB
- A data block "CONF_DB"

  This configuration DB contains the configuration data of the logical trigger. You create and configure the configuration DB available in the STEP 7 project.

  If you want to call more than one logical trigger, you will also need to make more than one configuration DB available.

You can change the numbers of the LOGICAL_TRIGGER instruction and the instance DB.

##### Validity

The LOGICAL_TRIGGER instruction can be used with the following module types:

- CP 343‑1 ERPC

##### Call

Call interface in FBD representation

![Call](images/21104418827_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[The configuration data block (S7-300)](#the-configuration-data-block-s7-300)
  
[How LOGICAL_TRIGGER works (S7-300)](#how-logical_trigger-works-s7-300)
  
[Explanation of the formal parameters for LOGICAL_TRIGGER (S7-300)](#explanation-of-the-formal-parameters-for-logical_trigger-s7-300)
  
[LOGICAL_TRIGGER instruction codes (S7-300)](#logical_trigger-instruction-codes-s7-300)

#### How LOGICAL_TRIGGER works (S7-300)

##### Operating principle

The following table shows the steps involved in a trigger call by the user program of the CPU.

| Step | Meaning |
| --- | --- |
| 1 | The LOGICAL_TRIGGER instruction is called at the intended point in the user program of the CPU with the corresponding instance DB and the selected configuration data block CONF_DB.  - If the LOGICAL_TRIGGER instruction is called with ACT = 1, the current trigger data is read and sent to the CP firmware. - If the LOGICAL_TRIGGER instruction is called with ACT = 0, the status codes DONE, ERROR and STATUS are updated. |
| 2 | The LOGICAL_TRIGGER instruction reads the current trigger data. |
| 3 | the LOGICAL_TRIGGER instruction creates the PDU that will be sent to the CP firmware with the current trigger data. |
| 4 | The CP firmware creates the data frame and transfers it to the ERPC application. |
| 5 | The ERPC application sends the data frame to the ERP subscriber (ERP system or MES). |

---

**See also**

[LOGICAL_TRIGGER for the logical trigger (S7-300)](#logical_trigger-for-the-logical-trigger-s7-300)

#### Explanation of the formal parameters for LOGICAL_TRIGGER (S7-300)

##### Explanation of the formal parameters

The following table explains the formal parameters for the call interface of the LOGICAL_TRIGGER instruction:

| Parameter | Declaration | Data type | Possible values | Description |
| --- | --- | --- | --- | --- |
| ACT | INPUT | BOOL | 0 | If the LOGICAL_TRIGGER instruction is called with ACT = 0, the status codes DONE, ERROR and STATUS are updated. |
| 1 | If the LOGICAL_TRIGGER instruction is called with ACT = 1, the current trigger data is read in and sent to the CP. |  |  |  |
| ID | INPUT | INT |  | Trigger ID  This value identifies the logical trigger configured in the ILS Workbench. |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP with STEP 7, the module start address is displayed in the configuration table by HW Config. Specify this address here. |
| CONF_DB | INPUT | INT |  | This data block contains the configuration data of the configured logical trigger. |
| CnfLevel | INPUT | INT | 0: Transport acknowledgment  1: End-to-end acknowledgment | Acknowledgment mode  You can find the relevant acknowledgment based on the STATUS value in the codes of the LOGICAL_TRIGGER instruction.  - 0 = transport acknowledgment (STATUS = 0000<sub>H</sub>)   The job is reported as successful, as soon as the data is transferred to the ERPC application.   This does not necessarily mean that the data frame was sent to the ERP subscriber (ERP system or MES) and does not preclude the ERPC application detecting an error later. - 1 = end-to-end acknowledgment (STATUS = 0001<sub>H</sub>)   The job is only acknowledged after the ERPC application has checked the data.   The "TriggerResponse" variable of the configuration DB (DB_CONF) is used to report whether or not the ERP subscriber could be reached an whether the ERPC application is in store-and-forward mode.   Compared with the transport acknowledgment, the end-to-end acknowledgment means a longer job execution time. |
| DONE | OUTPUT | BOOL | 0: Job active  1: Job completed | The parameter indicates whether or not the job for transferring the configuration data area was handled free of errors.  When the job is accepted, DONE is set to 0 by the CP. As long as DONE = 0, no further job can be triggered.  For the meaning in the context of the ERROR and STATUS parameters, refer to the table "LOGICAL_TRIGGER instruction codes". |
| ERROR | OUTPUT | BOOL | 0: -  1: Error situation | Error code  For the meaning in the context of the DONE and STATUS parameters, refer to the table "LOGICAL_TRIGGER instruction codes". |
| STATUS | OUTPUT | WORD | Refer to the table "LOGICAL_TRIGGER instruction codes". | Status code  For the meaning in the context of the DONE and ERROR parameters, refer to the table "LOGICAL_TRIGGER instruction codes". |

---

**See also**

[LOGICAL_TRIGGER for the logical trigger (S7-300)](#logical_trigger-for-the-logical-trigger-s7-300)
  
[LOGICAL_TRIGGER instruction codes (S7-300)](#logical_trigger-instruction-codes-s7-300)

#### LOGICAL_TRIGGER instruction codes (S7-300)

##### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

LOGICAL_TRIGGER instruction codes

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| **Codes relating to job execution** |  |  |  |
| 1 | 0 | 0000<sub>H</sub> | Job completed without error. The logical trigger was completed successfully. |
| 1 | 0 | 0001<sub>H</sub> | Job completed without error. The database is unreachable (store-and-forward mode). |
| 0 | 0 | 8181<sub>H</sub> | Job active. |
| 0 | 1 | 7000<sub>H</sub> | The LOGICAL_TRIGGER instruction was called with ACT = 0. The job will, however, not be executed.  Call the LOGICAL_TRIGGER instruction at least once with ACT = 1. |
| **Codes relating to configuration and the sequence of the logical trigger** |  |  |  |
| 0 | 1 | 80D2<sub>H</sub> | The CP in use does not support ERPC communication (wrong CP type). |
| 0 | 1 | 8183<sub>H</sub> | The CP in use does not support ERPC communication (wrong CP type). |
| 0 | 1 | 8187<sub>H</sub> | Invalid status of the LOGICAL_TRIGGER instruction (unknown LOGICAL_TRIGGER_STATE).  Call the LOGICAL_TRIGGER instruction again. |
| 0 | 1 | 8A01<sub>H</sub> | The number of configured logical triggers equals 0. |
| 0 | 1 | 8A02<sub>H</sub> | The is no configuration in the configuration DB for this logical trigger.  Check the ILS Workbench configuration. |
| 0 | 1 | 8A03<sub>H</sub> | The structure of the configuration DB is incorrect. The "header identifier" does not have the correct value.  Correct the value of the "ident" variable in the configuration DB (see manual of the ERPC-CP). |
| 0 | 1 | 8A04<sub>H</sub> | The structure of the configuration DB is incorrect.  Download the ILS Workbench configuration to the CP again, create and configure the configuration DB(s) again (see "ERPC‑CP" manual). |
| 0 | 1 | 8A05<sub>H</sub> | The configured configuration DB does not exist on the CPU. |
| 0 | 1 | 8A06<sub>H</sub> | The next call called a trigger that is still running with a different ID.  Check the "ID" in the called LOGICAL_TRIGGER instruction. |
| 0 | 1 | 8A08<sub>H</sub> | The configuration data in the configuration DB does not exist or is incomplete.  If the error occurs only during startup of the S7 station, the cause may be that the configuration data of the logical trigger was not completely transferred to the configuration DB.  If the error continues to occur, check the configuration of the ERPC symbols. |
| 0 | 1 | 8A09<sub>H</sub> | An unknown error was reported in the configuration DB. |
| 0 | 1 | 8A0A<sub>H</sub> | The logical trigger cannot be started because a new trigger configuration is currently being loaded. |
| 0 | 1 | 8A0B<sub>H</sub> | Error identifying the time stamp of the current data record (CPU data) |
| 0 | 1 | 8A0C<sub>H</sub> | The configuration DB was created with the "Unlinked" property.  Correct the object properties of the LOGICAL_TRIGGER instruction. |
| 0 | 1 | 8A0D<sub>H</sub> | Error in the the input parameter CONF_DB of the LOGICAL_TRIGGER instruction. The parameter has the value "0" or higher than the maximum DB number for the CPU. |
| 0 | 1 | 8A0E<sub>H</sub> | The transferred trigger ID is not in the permitted range of 1...16.  Correct the value in the LOGICAL_TRIGGER instruction call in the user program. |
| 0 | 1 | 8A0F<sub>H</sub> | The set acknowledgment mode (CnfLevel) is invalid.  Correct the value in the LOGICAL_TRIGGER instruction call in the user program. |
| 0 | 1 | 8Bxx<sub>H</sub> | Error copying the current variable values to the PDU of the logical trigger. The last two places (xx) are the variable number.  Check the configuration of the symbol involved in the symbol table of the CPU and in the list of ERPC symbols in the properties dialog of the CP. |
| 0 | 1 | 8C01<sub>H</sub> | The internal status code of the LOGICAL_TRIGGER instruction is invalid.  Download the ILS Workbench configuration to the CP again, create and configure the configuration DB(s) again (see "ERPC‑CP" manual). |
| 0 | 1 | 8C02<sub>H</sub> | The return value of the end-to-end acknowledgment is invalid.  Download the ILS Workbench configuration to the CP again, create and configure the configuration DB(s) again (see "ERPC‑CP" manual). |
| 0 | 1 | 8C03<sub>H</sub> | The logical trigger contains more than 255 variables. |
| 0 | 1 | 8C06<sub>H</sub> | Error reading the data record. |
| 0 | 1 | 8D03<sub>H</sub> | The firmware is signaling a timeout during a database action. |
| 0 | 1 | 8D04<sub>H</sub> | The database application is signaling a general error in the acknowledgment of the current action. |
| 0 | 1 | 8E01<sub>H</sub> | The configured configuration DB on the CPU is not large enough.  Change the size of the configuration DB. |
| 0 | 1 | 8E06<sub>H</sub> | No connection has yet been established to the logical trigger. |
| 0 | 1 | 8EXX<sub>H</sub> | These status codes with values for XX<sub>H</sub> in the range 02<sub>H</sub>..FF<sub>H</sub> are generated from an internal trigger response.  If such values occur, they are relevant for service purposes. |

---

**See also**

[LOGICAL_TRIGGER for the logical trigger (S7-300)](#logical_trigger-for-the-logical-trigger-s7-300)
  
[Explanation of the formal parameters for LOGICAL_TRIGGER (S7-300)](#explanation-of-the-formal-parameters-for-logical_trigger-s7-300)

#### The configuration data block (S7-300)

##### Preparing the configuration data block "CONF_DB"

If you use the "logical trigger" ERPC function, you will need to create a data block (DB) in STEP 7 for the configuration data of the logical trigger and specify it in the call parameters of the LOGICAL_TRIGGER instruction. The LOGICAL_TRIGGER instruction accesses DB CONF_DB. CONF_DB has no further significance for the user program.

##### Programming the configuration data block

To identify the newly created DB, you will need to open the DB and specify the "header identifier" and the DB size in the first two free lines.

Open the DB in STEP 7 and configure the first two free lines with the variables "ident" and "data" as follows:

| Address | Name | Type | Initial value | Comment (optional) |
| --- | --- | --- | --- | --- |
| *) |  | `STRUCT` *) |  |  |
| *) | `ident` | `DWORD` | `DW#16#45525043` | header identifier |
| *) | `data` | `array[1..2048]` |  | DB size (see warning below) |
| *) |  | `Byte` |  |  |
| *) |  | `END_STRUCT` *) |  |  |
| *<sup>)</sup> Values are entered by the program |  |  |  |  |

> **Note**
>
> **DB size**
>
> 2 048 bytes are recommended as the DB size. If it becomes apparent during commissioning that this value is not enough, increase it. If a value is too low, this is reported by the LOGICAL_TRIGGER instruction with an error and the STATUS "8A05<sub>H</sub>".

---

**See also**

[LOGICAL_TRIGGER for the logical trigger (S7-300)](#logical_trigger-for-the-logical-trigger-s7-300)

## PROFIBUS (S7-300, S7-400)

This section contains information on the following topics:

- [Introduction to PROFIBUS (S7-300, S7-400)](#introduction-to-profibus-s7-300-s7-400)
- [Instructions for open communications services (SEND/RECEIVE interface) (S7-300, S7-400)](#instructions-for-open-communications-services-sendreceive-interface-s7-300-s7-400-1)
- [Instructions for DP (distributed I/O) with S7-300 (S7-300, S7-400)](#instructions-for-dp-distributed-io-with-s7-300-s7-300-s7-400)

### Introduction to PROFIBUS (S7-300, S7-400)

This section contains information on the following topics:

- [General information on the FCs / FBs for PROFIBUS CPs (S7-300, S7-400)](#general-information-on-the-fcs-fbs-for-profibus-cps-s7-300-s7-400)
- [Setting parameters for block / function calls (S7-300, S7-400)](#setting-parameters-for-block-function-calls-s7-300-s7-400)
- [Parameters for specifying a CPU data area (input parameters) (S7-300, S7-400)](#parameters-for-specifying-a-cpu-data-area-input-parameters-s7-300-s7-400-1)
- [Status information (output parameters) (S7-300, S7-400)](#status-information-output-parameters-s7-300-s7-400-1)

#### General information on the FCs / FBs for PROFIBUS CPs (S7-300, S7-400)

##### Available instructions

The following list shows the symbolic names of the program blocks (instructions) as supplied. You cannot change these symbolic names.

| Communication service / functional area | Instruction (symbolic name) <sup>1)</sup> | Library |  |
| --- | --- | --- | --- |
|  |  |  |  |
| CP 300 | CP 400 |  |  |
| PROFIBUS DP | DP_SEND | x | x |
| DP_RECV | x | x |  |
| DP_DIAG | x | x |  |
| DP_CTRL | x | x |  |
| SEND / RECEIVE  (open communications services) | AG_SEND |  | x |
| AG_RECV |  | x |  |
| AG_LSEND |  | x |  |
| AG_LRECV |  | x |  |
| S7 communication | BSEND |  | x |
| BRCV |  | x |  |
| PUT |  | x |  |
| GET |  | x |  |
| USEND |  | x |  |
| URCV |  | x |  |
| C_CNTRL |  | x |  |
| 1) Note: The following descriptions also include information on differences in behavior between the various versions of the instructions. Please check and note the version identifiers of the instructions you are using. The SIMATIC Manager global libraries installed with the Automation Workbench contain the versions of the instructions current when STEP 7 was released. |  |  |  |

##### Which block version should I use?

The following descriptions also include information on differences in behavior between the various versions of the instructions. Please check and note the version identifiers of the instructions you are using.

> **Note**
>
> We recommend that you always use the latest versions of the instructions for all module types.
>
> You will find information on the current versions of the instructions and the current instructions to download from the Internet in our customer support:
>
> http://support.automation.siemens.com/WW/view/en/8797900
>
> With older module types, this recommendation assumes that you are using the latest firmware for the particular module type.

##### Instructions when modules are replaced

Module replacement in this sense means the replacement of a module with another module that may be a more recent version.

> **Note**
>
> Please remember that if you replace a module, you must only use the instructions permitted for the configured CP type in the user program.
>
> We recommend that you always use the latest versions of the instructions for all module types. With older module types, this recommendation assumes that you are using the latest firmware for the particular module type.
>
> You will find more information on replacing modules in our Customer Support on the Internet.
>
> http://support.automation.siemens.com/WW/view/en/7806643

The manuals contain information on the compatibility of the S7-CPs and the corresponding instructions.

---

**See also**

[Symbolic and numerical names of instructions (S7-300, S7-400)](Functional%20description%20of%20S7-300-400%20CPUs%20%28S7-300%2C%20S7-400%29.md#symbolic-and-numerical-names-of-instructions-s7-300-s7-400)

#### Setting parameters for block / function calls (S7-300, S7-400)

Before describing the instruction in detail, a few general comments on calling and setting parameters for instructions will be useful at this point.

The general information below applies to the following parameter groups that exist for all instructions:

- Parameters for CP and connection assignment (input parameters)
- Parameters for specifying a CPU data area (input parameters)
- Status information (output parameters)

##### Calling communications instruction for an S7­300

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| Calling the communications instructions for S7-300 in more than one priority class is not permitted! If, for example, you call a communication instruction in OB1 and in OB35, execution of the instruction could be interrupted by the higher­priority OB.  If you call instructions in more than one OB, write your program so that a communications instruction that is currently executing cannot be interrupted by another communications instruction (for example by disabling/enabling interrupts with system instructions). |  |

#### Parameters for specifying a CPU data area (input parameters) (S7-300, S7-400)

##### Specifying the data area on the CPU

When you call an instruction, you transfer the address and length of the data area on the CPU in which the user data is available or will be stored or which can contain further parameter information.

The ANY pointer data type is used to address this area.

#### Status information (output parameters) (S7-300, S7-400)

##### Evaluating status codes

For status evaluation, the following parameters must be evaluated in the user program:

- DONE or NDR  
  These parameters (DONE with send jobs and NDR with receive jobs) signal (successful) completion of the job.
- ERROR  
  This indicates that the job could not be executed error­free.
- STATUS  
  This parameter supplies detailed information about the execution of the job. Status codes can be returned during execution of the job (DONE=0 and ERROR=0).

  > **Note**
  >
  > Remember that the status codes DONE, NDR, ERROR, STATUS are updated at each instruction call.

##### Status codes during CP startup

With a warm or hot restart on the Ethernet CP, the output parameters of the instruction are reset as follows:

- DONE = 0
- NDR = 0
- ERROR = 0
- STATUS = 8180H or 8181H

### Instructions for open communications services (SEND/RECEIVE interface) (S7-300, S7-400)

This section contains information on the following topics:

- [Instructions for FDL connections (SEND/RECEIVE interface) (S7-300, S7-400)](#instructions-for-fdl-connections-sendreceive-interface-s7-300-s7-400)
- [AG_SEND / AG_LSEND (S7-300, S7-400)](#ag_send-ag_lsend-s7-300-s7-400)
- [AG_RECV / AG_LRECV (S7-300, S7-400)](#ag_recv-ag_lrecv-s7-300-s7-400)

#### Instructions for FDL connections (SEND/RECEIVE interface) (S7-300, S7-400)

##### Overview

The following instructions are available for the SEND/RECEIVE interface for transferring data on configured FDL connections:

| Instruction | Can be used with <sup>1)</sup> |  | Meaning |
| --- | --- | --- | --- |
| **S7-300** | **S7-400** |  |  |
| AG_SEND | x | x | for sending data |
| AG_RECV | x | x | for receiving data |
| AG_LSEND |  | x | for sending data |
| AG_LRECV |  | x | for receiving data |

1) Notes on the Instructions for an S7­300 and S7­400

To ensure the compatibility of PROFIBUS and Industrial Ethernet on the interface in the user program, you can use the AG_LSEND and AG_LRECV instructions on PROFIBUS as alternatives to AG_SEND and AG_RECV. There is no difference in the interface or the way they function. On PROFIBUS, however, you can only transfer data up to a maximum of 240 bytes even with these instructions although they are intended for longer data records on Industrial Ethernet.

This is only possible if the type and version of the instructions are permitted for the CP type you are using.

With the S7 CPs for S7­300, only the AG_SEND and AG_RECV instructions are used; on Industrial Ethernet even for the transfer of longer data records.

The manuals contain information on the compatibility of the S7-CPs and the corresponding instructions. You will find an overview of the versions of the instructions in the documentation and block history.

##### Application

The following diagram illustrates the use of the AG_SEND / AG_LSEND and AG_RECV / AG_LRECV instructions for bi-directional data transfer on a configured FDL connection.   
With certain connection types, a job header should be included in the user data area.

![Using AG_SEND and AG_RECV on both communications partners](images/12881897739_DV_resource.Stream@PNG-en-US.png)

Using AG_SEND and AG_RECV on both communications partners

##### Application without job header

With a specified FDL connection, the address and job parameters are specified by the configuration of the connection. The user program only provides the user data in the FDL data area when sending with AG_SEND / AG_LSEND or receives the data with AG_RECV / AG_LRECV.

Up to 240 bytes of user data can be transferred. This information applies to AG_SEND and AG_LSEND on PROFIBUS.

##### Working with the job header

The following connection types require a job header in the FDL (user) data area:

- Unspecified FDL connection with free layer 2 access
- FDL connection with broadcast
- FDL connection with multicast

The following schematic illustrates the structure of the job buffer and the meaning and location of the parameters in the job header.

![Sending and receiving via an FDL connection with programmed broadcast addressing](images/12881913867_DV_resource.Stream@PNG-en-US.png)

Sending and receiving via an FDL connection with programmed broadcast addressing

|The user data area can be up to 240 bytes. Up to 236 bytes of user data can be transferred. 4 bytes are reserved for the job header.

Please note that the data length specified in the instruction call (LEN parameter) must include the header and the user data!

#### AG_SEND / AG_LSEND (S7-300, S7-400)

This section contains information on the following topics:

- [AG_SEND / AG_LSEND (PROFIBUS) (S7-300, S7-400)](#ag_send-ag_lsend-profibus-s7-300-s7-400)
- [Parameters for AG_SEND / AG_LSEND (PB) (S7-300, S7-400)](#parameters-for-ag_send-ag_lsend-pb-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (PB) (S7-300, S7-400)](#parameters-done-error-status-pb-s7-300-s7-400)
- [Example of AG_SEND (PB) (S7-300, S7-400)](#example-of-ag_send-pb-s7-300-s7-400)

##### AG_SEND / AG_LSEND (PROFIBUS) (S7-300, S7-400)

###### Description

The FC AG_SEND / AG_LSEND instruction transfers data to the PROFIBUS CP for transmission on a configured FDL connection.

The selected data area can be a process image area, a memory bit area or a data block area.

Error free execution of the function is indicated when the entire FDL data area could be sent on PROFIBUS.

Note:  
Unless otherwise stated, all the following information applies equally to AG_SEND and AG_LSEND.

###### Call

Call interface in FBD representation

![Call](images/12881916939_DV_resource.Stream@PNG-de-DE.png)

###### Calls with job header

The following table shows the connection types and job types for which parameters must be supplied in the job header.

The job header is located in the FDL (user ) data area. It occupies the first 4 bytes and must be added to the length specified in the LEN parameter. The maximum user data length is therefore reduced for jobs with a job header to 236 bytes.

Supplying the job header in the user data area

| Parameter | FDL connection type |  |  |
| --- | --- | --- | --- |
| **Unspecified: free layer 2**  <sup>2)</sup> | **Broadcast** | **Multicast** |  |
| PB address | Address of the destination station  Range of values:  0 to 126 depending on node /  127 for broadcast/multicast | For AG_SEND no relevance; but area must be reserved. | For AG_SEND no relevance; but area must be reserved. |
| LSAP | LSAP of the destination station  Range of values:  0 to 62 depending on node /  63 for broadcast | No significance but area must be reserved. | No significance but area must be reserved. |
| Service <sup>1)</sup> | SDA ( Send Data with Acknowledge):  Value: 00<sub>H</sub>  SDN ( Send Data with No Acknowledge):  Value: 01<sub>H</sub> | No significance but area must be reserved. | No significance but area must be reserved. |

<sup>1)</sup> for broadcast and multicast, only the SDN service is possible.

<sup>2)</sup> The information on broadcast and multicast in this column is relevant only when an unspecified FDL connection is used for broadcast or multicast. On a configured FDL connection (recommended application) with broadcast or multicast as the connection partner, the address parameters are assigned automatically according to the configuration.

---

**See also**

[Parameters for AG_SEND / AG_LSEND (PB) (S7-300, S7-400)](#parameters-for-ag_send-ag_lsend-pb-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (PB) (S7-300, S7-400)](#parameters-done-error-status-pb-s7-300-s7-400)
  
[Example of AG_SEND (PB) (S7-300, S7-400)](#example-of-ag_send-pb-s7-300-s7-400)
  
[AG_SEND / AG_LSEND / AG_SSEND (Ind. Ethernet) (S7-300, S7-400)](#ag_send-ag_lsend-ag_ssend-ind-ethernet-s7-300-s7-400)

##### Parameters for AG_SEND / AG_LSEND (PB) (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the AG_SEND /AG_LSEND instructions:

| Parameter | Declaration | Data type | Possible values | Description |
| --- | --- | --- | --- | --- |
| ACT | INPUT | BOOL | 0, 1 | If the instruction is called with ACT=1, LEN bytes are sent from the ISO transport data area specified with the SEND parameter.  If the instruction is called with ACT = 0, the status codes DONE, ERROR and STATUS are updated. |
| ID | INPUT | INT | 1,2...64  (S7-400)  1,2...16  (S7-300) | The connection number of the FDL connection is specified in the parameter ID. |
| LADDR | INPUT | WORD |  | Module start address  When you configure the CP, the module start address is displayed in the configuration table. Specify this address here. |
| SEND | INPUT | ANY  (only the following are permitted as VARTYPE:  WORD and DWORD are permitted) |  | Specifies the address and length  The address of the data area points to one of the alternatives:  - PI area - Memory bit area - Data block area   With a call with job header, the FDL data area contains the job header and the user data. |
| LEN | INPUT | INT | 1, 2, to 240 (or up to "length specified for SEND parameter") | Number of bytes to be sent from the FDL data area with this job. The possible values range from 1 to length specified for the SEND parameter.  In a call, with job header, the length information is made up of the job header (4 bytes) + user data (1 to 236 bytes). Therefore LEN >= 4 ! |
| DONE | OUTPUT | BOOL | 0: - 1: new data | The status parameter indicates whether or not the job was completed without errors. For the meaning in conjunction with the ERROR and STATUS parameters, refer to the following table. |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code  For the meaning in conjunction with the DONE and STATUS parameters, refer to the following table. |
| STATUS | OUTPUT | WORD | See following table | Status code  For the meaning in conjunction with the DONE and ERROR parameters, refer to the following table. |

---

**See also**

[AG_SEND / AG_LSEND (PROFIBUS) (S7-300, S7-400)](#ag_send-ag_lsend-profibus-s7-300-s7-400)

##### Parameters DONE, ERROR, STATUS (PB) (S7-300, S7-400)

###### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8FxxH in STATUS, refer to the information about the output parameter RET_VAL in the descriptions of the referenced system program blocks.
>
> Which system program blocks are used and are relevant for error evaluation, can be queried in STEP 7.

AG_SEND condition codes

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 1 | 0 | 0000<sub>H</sub> | Job completed without error. |
| 0 | 0 | 0000<sub>H</sub> | No job being executed. |
| 0 | 0 | 8181<sub>H</sub> | Job active. |
| 0 | 1 | 7000<sub>H</sub> | The condition code is possible only with S7-400: The instruction was called with ACT=0; the job has not yet been processed. |
| 0 | 1 | 8183<sub>H</sub> | No configuration or the FDL service has not yet started on the PROFIBUS CP. |
| 0 | 1 | 8184<sub>H</sub> | Possible causes:  - Illegal data type specified for the SEND parameter. - FDL connection without job buffer: System error. - FDL connection with job buffer: Parameter LEN<4 or illegal parameter in job header (with free layer 2 access). |
| 0 | 1 | 8185<sub>H</sub> | LEN parameter longer than SEND source area. |
| 0 | 1 | 8186<sub>H</sub> | ID parameter invalid. ID!=1, 2 to 15, 16. |
| 0 | 1 | 8301<sub>H</sub> | SAP not activated on destination station. |
| 0 | 1 | 8302<sub>H</sub> | No receive resources on the destination station; the receiving station cannot process received data quickly enough or has not prepared any receive resources. |
| 0 | 1 | 8303<sub>H</sub> | The PROFIBUS service (SDA Send Data with Acknowledge) is not supported on this SAP by the destination station.  This condition code can also occur temporarily when connections or gateways are downloaded "in RUN". |
| 0 | 1 | 8304<sub>H</sub> | The FDL connection is not established. |
| 0 | 1 | 8311<sub>H</sub> | The destination station is not obtainable at the specified PROFIBUS address or the service is not possible for the specified PROFIBUS address. |
| 0 | 1 | 8312<sub>H</sub> | PROFIBUS error on the CP: for example, bus short-circuit, own station not in ring. |
| 0 | 1 | 8315<sub>H</sub> | Possible causes:  - Internal parameter error on an FDL connection with job header: Parameter LEN<4 or illegal parameter in job header (with free layer 2 access). - Bus disruption   Possible additional meaning:  - This error code can also occur with bus problems (for example physical disturbances due to bad power connections or different settings for the transmission speed on the nodes). |
| 0 | 1 | 8F22<sub>H</sub> | Source area invalid, e.g.:  Area does not exist in the DB  LEN parameter < 0 |
| 0 | 1 | 8F24<sub>H</sub> | Area error reading a parameter. |
| 0 | 1 | 8F28<sub>H</sub> | Alignment error reading a parameter. |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | DB number error. |
| 0 | 1 | 8F3A<sub>H</sub> | Area not loaded (DB). |
| 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the I/O area. |
| 0 | 1 | 8F44<sub>H</sub> | Address of the parameter to be read is disabled in the access track. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference  e.g. parameter LEN=0 |
| 0 | 1 | 8090<sub>H</sub> | - No module with this module start address exists. - The instruction being used does not match the system family being used (remember to use different instructions for S7­300 and S7­400). |
| 0 | 1 | 8091<sub>H</sub> | Module start address not at a double­word boundary. |
| 0 | 1 | 8092<sub>H</sub> | In the ANY reference, a type other than BYTE is specified. (S7-400 only) |
| 0 | 1 | 80A4<sub>H</sub> | The communication bus connection between the CPU and CP is not established. (with newer CPU versions).  This can, for example, be caused by the following:  - No connection configuration; - The maximum number of CPs that can be operated at one time has been exceeded (for further information, refer to the CP manual). |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | The destination area is invalid. The amount of data to be sent exceeds the upper limit permitted for this service (e.g. destination area > 240 bytes). |
| 0 | 1 | 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established (with older CPU versions; otherwise 80A4<sub>H</sub>; for further information, refer to this code) |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | Resources occupied (memory). |
| 0 | 1 | 80C4<sub>H</sub> | Communications error (occurs temporarily, it is usually best to repeat the job in the user program). |
| 0 | 1 | 80D2<sub>H</sub> | Module start address incorrect. |

---

**See also**

[AG_SEND / AG_LSEND (PROFIBUS) (S7-300, S7-400)](#ag_send-ag_lsend-profibus-s7-300-s7-400)

##### Example of AG_SEND (PB) (S7-300, S7-400)

###### Example of call and evaluation of parameters

Below you will find an executable example of an AG_SEND instruction call and parameter evaluation.

The OB100 listed below belongs to the "AE_460_1" instruction selected here in which the send call takes place; OB100 sets the ACT bit correctly when the CPU starts up.

To function correctly, a DB100 with a size of at least 240 bytes must be loaded.

The program requires a CP at address 256 and a configured connection of the type ISO Transport / ISO­on­TCP / TCP or FDL with ID=1 (please adapt your configuration where necessary !).

|  |  |  |
| --- | --- | --- |
| `//---------------------------------------------------------------------`    `FUNCTION FC 100: VOID`    `TITLE = SENDE_DEMO`    `AUTHOR : Tester`    `FAMILY : S7300`    `NAME : FC5_Demo`    `VERSION : 1.0` |  |  |
| `//---------------------------------------------------------------------`    `BEGIN`     `CALL FC 5 (  ACT := M100.0,  ID := 1,  LADDR := W#16#100,  SEND := P#DB100.dbx0.0 BYTE 240,  LEN := 240,  DONE := M100.1,  ERROR := M100.2,  STATUS := MW102 );`    `//---------------------------------------------------------------------` |  |  |
| `R M100.0;  SET;  A M100.1;  JC done;  SET;  A M100.2;  JC err;` | `// // // // // // //` | `Reset parameter ACT for all further AG_SEND calls  Test for DONE = TRUE   Test for ERROR = TRUE` |
| `//---------------------------------------------------------------------` |  |  |
| `BEU;` | `// //` | `Neither DONE nor ERROR is set, the job is still running.` |
| `//---------------------------------------------------------------------` |  |  |
| `done: S M100.0;  BEU;` | `// //` | `Job completed without error. Set ACT = TRUE so that the following call can trigger the new job.` |
| `//---------------------------------------------------------------------` |  |  |
| `err: NOP 1;  NOP 1;  S M100.0;  BEU;` | `// // // //` | `An error occurred. The status word can be evaluated here. Set ACT to TRUE in any case, so that a new send job can be triggered if the error disappears.` |
| `//---------------------------------------------------------------------`    `END_FUNCTION`    `ORGANIZATION_BLOCK OB100 TITLE = Init_for_FC100 FAMILY: S7300 NAME: SENDE_DEMO_INIT VERSION: 1.0`    `VAR_TEMP`    `OB1_System: array [1..20] of byte;`    `END_VAR`    `//---------------------------------------------------------------------` |  |  |
| `BEGIN  SET  S M100.0 END_ORGANIZATION_BLOCK` | `// // //` | `Initialize ACT parameter` |

#### AG_RECV / AG_LRECV (S7-300, S7-400)

This section contains information on the following topics:

- [AG_RECV / AG_LRECV (PROFIBUS) (S7-300, S7-400)](#ag_recv-ag_lrecv-profibus-s7-300-s7-400)
- [Parameters for AG_RECV / AG_LRECV (PB) (S7-300, S7-400)](#parameters-for-ag_recv-ag_lrecv-pb-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (PB) (S7-300, S7-400)](#parameters-done-error-status-pb-s7-300-s7-400-1)

##### AG_RECV / AG_LRECV (PROFIBUS) (S7-300, S7-400)

###### Description

The AG_RECV / AG_LRECV instruction receives the data transferred on a configured FDL connection from the PROFIBUS CP.

The data area specified for the receive data can be a process image area, a bit address area or a data block area.

Error­free execution is indicated when the data could be received from the PROFIBUS CP.

Note:

Unless otherwise stated, all the following information applies equally to AG_RECV and AG_LRECV.

###### Call interface

Call interface in FBD representation

![Call interface](images/44487998603_DV_resource.Stream@PNG-de-DE.png)

###### Calls with job header

Return parameters in the job header in the FDL (user) data area

| Parameter | FDL connection type |  |  |
| --- | --- | --- | --- |
| **Unspecified: free layer 2)** | **Broadcast** | **Multicast** |  |
| PB address | Address of the sender Range of values: 0 to 126 depending on node |  |  |
| LSAP | LSAP of the sender Values: 0 to 63 depending on node |  |  |
| Service | SDN indication   ( Send Data with No Acknowledge - Indication):   Value: 01<sub>H</sub>  or  SDA indication ( Send Data with Acknowledge - Indication):   Value: 00<sub>H</sub> | SDN indication   ( Send Data with No Acknowledge - Indication):  Value: 7F<sub>H</sub> | SDN indication   ( Send Data with No Acknowledge - Indication):  Value: 7F<sub>H</sub> |

---

**See also**

[Parameters for AG_RECV / AG_LRECV (PB) (S7-300, S7-400)](#parameters-for-ag_recv-ag_lrecv-pb-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (PB) (S7-300, S7-400)](#parameters-done-error-status-pb-s7-300-s7-400-1)
  
[AG_RECV / AG_LRECV / AG_SRECV (Ind. Ethernet) (S7-300, S7-400)](#ag_recv-ag_lrecv-ag_srecv-ind-ethernet-s7-300-s7-400)

##### Parameters for AG_RECV / AG_LRECV (PB) (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the AG_RECV / AG_LRECV instruction:

| Parameter | Declaration | Data type | Possible values | Description |
| --- | --- | --- | --- | --- |
| ID | INPUT | INT | 1, 2 to 16 (S7-300) 1, 2 to 32 (S7-400) | The connection number of the FDL connection is specified in the parameter ID. |
| LADDR | INPUT | WORD |  | Module start address   When you configure the CP, the module start address is displayed in the configuration table. Specify this address here. |
| RECV | INPUT | ANY  (only the following are permitted as VARTYPE:  WORD and DWORD are permitted) |  | Specifies the address and length  The address of the FDL data area points to one of the alternatives:  - PI area - Memory bit area - Data block area   With a call with job header, the FDL data area contains the job header and the user data. |
| LEN | OUTPUT | INT | 1,2,...240 | Specifies the number of bytes to be received in the FDL data area from the PROFIBUS CP.  In a call, with job header, the length information is made up of the job header (4 bytes) + user data (1 to 236 bytes). Therefore LEN >= 4 ! |
| NDR | OUTPUT | BOOL | 0: - 1: new data | This parameter indicates whether new data were received.  For the meaning in conjunction with the ERROR and STATUS parameters, refer to the following table. |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code  For the meaning of this parameter in conjunction with the NDR and STATUS parameters, refer to the following table. |
| STATUS | OUTPUT | WORD | See following table | Status code  For the meaning in conjunction with the NDR and ERROR parameters, refer to the following table. |

---

**See also**

[AG_RECV / AG_LRECV (PROFIBUS) (S7-300, S7-400)](#ag_recv-ag_lrecv-profibus-s7-300-s7-400)

##### Parameters DONE, ERROR, STATUS (PB) (S7-300, S7-400)

###### Condition codes

The following table shows the codes formed by the NDR, ERROR and STATUS parameters that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information about the output parameter RET_VAL in the descriptions of the referenced system program blocks.
>
> Which system program blocks are used and are relevant for error evaluation, can be queried in STEP 7.

AG_RECV / AG_LRECV condition codes

| NDR | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 1 | 0 | 0000<sub>H</sub> | New data accepted. |
| 0 | 0 | 8180<sub>H</sub> | - There is no data available yet. The configuration is missing or the FDL service has not started on the PROFIBUS CP (occurs here instead of the code 0,1,8183<sub>H</sub>). |
| 0 | 0 | 8181<sub>H</sub> | Job active. |
| 0 | 1 | 8183<sub>H</sub> | No configuration or the FDL service has not yet started on the PROFIBUS CP. |
| 0 | 1 | 8184<sub>H</sub> | - Illegal data type specified for the RECV parameter. - System error. |
| 0 | 1 | 8185<sub>H</sub> | Destination buffer (RECV) is too short. |
| 0 | 1 | 8186<sub>H</sub> | ID parameter invalid. ID!=1, 2 to 15, 16. |
| 0 | 1 | 8303<sub>H</sub> | The PROFIBUS service ( SDA - Send Data with Acknowledge) is not supported on this SAP.  This condition code can also occur temporarily when connections or gateways are downloaded "in RUN". |
| 0 | 1 | 8304<sub>H</sub> | The FDL connection is not established. |
| 0 | 1 | 8F23<sub>H</sub> | Source area invalid, e.g.:  Area does note exist in the DB. |
| 0 | 1 | 8F25<sub>H</sub> | Area error writing a parameter. |
| 0 | 1 | 8F29<sub>H</sub> | Alignment error writing a parameter |
| 0 | 1 | 8F30<sub>H</sub> | Parameter is in the write­protected 1st current data block. |
| 0 | 1 | 8F31<sub>H</sub> | Parameter is in the write­protected 2nd current data block. |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | DB number error. |
| 0 | 1 | 8F3A<sub>H</sub> | Destination area not loaded (DB). |
| 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the  I/O area. |
| 0 | 1 | 8F45<sub>H</sub> | Address of the parameter to be written is disabled in the access track. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference. |
| 0 | 1 | 8090<sub>H</sub> | - No module with this module start address exists. - The instruction being used does not match the system family being used (remember to use different instructions for S7­300 and S7­400). |
| 0 | 1 | 8091<sub>H</sub> | Module start address not at a double­word boundary. |
| 0 | 1 | 8092<sub>H</sub> | In the ANY reference, a type other than BYTE is specified. (S7-400 only) |
| 0 | 1 | 80A0<sub>H</sub> | Negative acknowledgment reading from the module. |
| 0 | 1 | 80A4<sub>H</sub> | The communication bus connection between the CPU and CP is not established. (with newer CPU versions).  This can, for example, be caused by the following:  - No connection configuration; - The maximum number of CPs that can be operated at one time has been exceeded (for further information, refer to the CP manual). |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | Possible causes:  - The destination area is invalid. - The destination area is too short. - The destination area for the received data was adequately dimensioned.   Remedy: Run another receive call with maximum receive buffer size. This applies regardless of the connection type (unicast / multicast / broadcast) and the device family (S7-300 / S7-400). |
| 0 | 1 | 80B2<sub>H</sub> | The communication bus connection between the CPU and CP is not established. |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3H | Resources occupied (memory). |
| 0 | 1 | 80C4<sub>H</sub> | Communications error (occurs temporarily, it is usually best to repeat the job in the user program). |
| 0 | 1 | 80D2<sub>H</sub> | Module start address incorrect. |

---

**See also**

[AG_RECV / AG_LRECV (PROFIBUS) (S7-300, S7-400)](#ag_recv-ag_lrecv-profibus-s7-300-s7-400)

### Instructions for DP (distributed I/O) with S7-300 (S7-300, S7-400)

This section contains information on the following topics:

- [Instructions for the S7­300 DP mode (S7-300, S7-400)](#instructions-for-the-s7300-dp-mode-s7-300-s7-400)
- [DP_SEND (S7-300, S7-400)](#dp_send-s7-300-s7-400)
- [DP_RECV (S7-300, S7-400)](#dp_recv-s7-300-s7-400)
- [DP_DIAG (S7-300, S7-400)](#dp_diag-s7-300-s7-400)
- [DP_CTRL (S7-300, S7-400)](#dp_ctrl-s7-300-s7-400)

#### Instructions for the S7­300 DP mode (S7-300, S7-400)

##### Overview

The following instructions are available for the DP master and DP slave modes with an S7­300:

| Instruction | can be used with: |  | Meaning |
| --- | --- | --- | --- |
| DP master | DP slave |  |  |
| DP_SEND | X | X | for sending data |
| DP_RECV | X | X | for receiving data |
| DP_DIAG | X | - | for diagnostic functions initiated by the DP master |
| DP_CTRL | X | - | for control functions |

##### Application

The following diagram illustrates the use of the DP_SEND and DP_RECV instructions on the DP master and DP slave.

![Using the DP_SEND and DP_RECV instructions with DP master and DP slave  Instructionsfor DP mode](images/12881923083_DV_resource.Stream@PNG-en-US.png)

Using the DP_SEND and DP_RECV instructions with DP master and DP slave

#### DP_SEND (S7-300, S7-400)

This section contains information on the following topics:

- [DP_SEND (S7-300, S7-400)](#dp_send-s7-300-s7-400-1)
- [Parameters for DP_SEND (S7-300, S7-400)](#parameters-for-dp_send-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-4)

##### DP_SEND (S7-300, S7-400)

###### Description

The DP_SEND instruction transfers data to the PROFIBUS CP. Depending on the mode of the PROFIBUS CP, DP_SEND has the following significance:

- When used in the DP master

The instruction transfers the data of a specified DP output area to the PROFIBUS CP for output to the distributed I/O system.

- When used in the DP slave

The instruction transfers the input data of the DP slave to the PROFIBUS CP for transfer to the DP master

The selected data area can be a process image area, a memory bit area or a data block area.

Correct execution is signaled when the entire DP data area could be accepted by the PROFIBUS CP.

To start the DP master exactly one DP-SEND or DP-RECV call must precede the call sequence. The following applies to this first call:

If DP-SEND is used for initialization, the transferred data area is not accepted and "0" is sent to the slaves. The user data to be transferred is accepted only with the second block call.

###### Call interface

![Call interface](images/12881990155_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Parameters for DP_SEND (S7-300, S7-400)](#parameters-for-dp_send-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-4)

##### Parameters for DP_SEND (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the DP_SEND instruction:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD |  | Module start address  When you configure the CP, the module start address is displayed in the configuration table. Specify this address here. |
| SEND | INPUT | ANY  (only the following are permitted as VARTYPE:  With DP_SEND as of V3: BYTE  With DP_SEND up to V2.x: BYTE, WORD and DWORD) |  | Specifies the address and length  The address of the DP data area points to one of the alternatives:  - PI area - Memory bit area - Data block area   The length must be set for  - DP master: 1...21600 - DP slave: 1...240 |
| DONE | OUTPUT | BOOL | 0: - 1: new data | The status parameter indicates whether or not the job  was completed without errors. For the meaning in conjunction with the ERROR and STATUS parameters, refer to[Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-4). |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code For the meaning in conjunction with the DONE and STATUS parameters, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-4) |
| STATUS | OUTPUT | WORD |  | Status code For the meaning in conjunction with the DONE and ERROR parameters, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-4) |

---

**See also**

[DP_SEND (S7-300, S7-400)](#dp_send-s7-300-s7-400-1)

##### Parameters DONE, ERROR, STATUS (S7-300, S7-400)

###### Condition codes

The following table shows the condition codes formed based on DONE, ERROR and STATUS that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information about the output parameter RET_VAL in the descriptions of the referenced system program blocks.
>
> Which system program blocks are used and are relevant for error evaluation, can be queried in STEP 7.

DP_SEND condition codes

| DONE | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | 8180<sub>H</sub> | - Startup:   The DP service was started but data acceptance is not yet possible. - Normal operation   Data transfer active. - DP has not started due to:   - CP STOP or   - "No parameter assignment" (occurs here instead of the code 0,1,8183<sub>H</sub>). |
| 1 | 0 | 0000<sub>H</sub> | New data transferred without error. |
| 0 | 1 | 8183<sub>H</sub> | No configuration or the DP service has not yet started on the PROFIBUS CP. |
| 0 | 1 | 8184<sub>H</sub> | System error or bad parameter type. |
| 0 | 1 | 8F22<sub>H</sub> | Area length error reading a parameter (e.g. DB too short). |
| 0 | 1 | 8F23<sub>H</sub> | Area length error writing a parameter (e.g. DB too short). |
| 0 | 1 | 8F24<sub>H</sub> | Area error reading a parameter. |
| 0 | 1 | 8F25<sub>H</sub> | Area error writing a parameter. |
| 0 | 1 | 8F28<sub>H</sub> | Alignment error reading a parameter. |
| 0 | 1 | 8F29<sub>H</sub> | Alignment error writing a parameter. |
| 0 | 1 | 8F30<sub>H</sub> | Parameter is in the write­protected 1st current data block. |
| 0 | 1 | 8F31<sub>H</sub> | Parameter is in the write­protected 2nd current data block. |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | DB number error. |
| 0 | 1 | 8F3A<sub>H</sub> | Destination area not loaded (DB). |
| 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the I/O area. |
| 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the I/O area. |
| 0 | 1 | 8F44<sub>H</sub> | Address of the parameter to be read is disabled in the access track. |
| 0 | 1 | 8F45<sub>H</sub> | Address of the parameter to be written is disabled in the access track. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference. |
| 0 | 1 | 8090<sub>H</sub> | No module with this address exists. |
| 0 | 1 | 8091<sub>H</sub> | Logical base address not at a double word boundary. |
| 0 | 1 | 80A1<sub>H</sub> | Negative acknowledgment writing to the module. |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | The number of data bytes to be sent exceeds the upper limit for this service (applies to DP master and DP slave mode). |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | Resources occupied (memory). |
| 0 | 1 | 80C4<sub>H</sub> | Communications error (occurs temporarily, it is usually best to repeat the job in the user program). |
| 0 | 1 | 80D2<sub>H</sub> | Logical base address incorrect. |

---

**See also**

[DP_SEND (S7-300, S7-400)](#dp_send-s7-300-s7-400-1)

#### DP_RECV (S7-300, S7-400)

This section contains information on the following topics:

- [DP_RECV (S7-300, S7-400)](#dp_recv-s7-300-s7-400-1)
- [Parameters for DP_RECV (S7-300, S7-400)](#parameters-for-dp_recv-s7-300-s7-400)
- [Parameters NDR, ERROR, STATUS (S7-300, S7-400)](#parameters-ndr-error-status-s7-300-s7-400)
- [DPSTATUS - DP_RECV parameters (S7-300, S7-400)](#dpstatus---dp_recv-parameters-s7-300-s7-400)

##### DP_RECV (S7-300, S7-400)

###### Description

The DP_RECV instruction receives data over PROFIBUS. DP_RECV has the following significance depending on the mode of the PROFIBUS CP:

- When used in the DP master  
  DP_RECV receives the process data from the distributed I/O along with status information and enters this in a specified DP input area.
- When used on the DP slave  
  DP_RECV accepts the output data transferred by the DP master in the DP data area specified in the instruction.

The data area specified for the receive data can be a process image area, a bit address area or a data block area.

Error­free execution is signaled when the entire DP data input area could be transferred by the PROFIBUS CP.

Note that the DP_RECV instruction must be called successfully at least once on the DP slave in the user program if output data was configured for this DP slave. Please read the information in the manual.

To start the DP master exactly one DP-SEND or DP-RECV call must precede the call sequence. The following applies to this first call:

- If DP-RECV is used for initialization, the received data is not adopted. The user data to be received is accepted only with the second block call.

###### Additional task: Entering the status byte

The DP_RECV instruction has the following additional task:

- Updating the DP status byte DPSTATUS. This means that DP_RECV handles tasks for DP diagnostics  
  If no receive data is configured, DP_RECV must be called with a length of 1 to update the DPSTATUS status byte (applies only to DP masters).   
  Please read the information in the manual as well.
- Enabling the station list (see [DP_DIAG](#dp_diag-s7-300-s7-400)).

###### Call interface

![Call interface](images/12881993227_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Parameters for DP_RECV (S7-300, S7-400)](#parameters-for-dp_recv-s7-300-s7-400)
  
[Parameters NDR, ERROR, STATUS (S7-300, S7-400)](#parameters-ndr-error-status-s7-300-s7-400)
  
[DPSTATUS - DP_RECV parameters (S7-300, S7-400)](#dpstatus---dp_recv-parameters-s7-300-s7-400)

##### Parameters for DP_RECV (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the DP_RECV instruction:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD |  | Module start address   When you configure the CP, the module start address is displayed in the configuration table. Specify this address here. |
| RECV | INPUT | ANY  (only the following are permitted as VARTYPE:  With DP_RECV as of V3: BYTE  With DP_RECV up to V2.x: BYTE, WORD and DWORD) |  | Specifies the address and length  The address of the DP data area points to one of the alternatives:  - PI area - Memory bit area - Data block area   The length must be set for:  - DP master: 1...2160 - DP slave: 1...240 - DP master; only read status byte: 1   (see also CP manual) |
| NDR | OUTPUT | BOOL | 0: - 1: New data accepted | The status parameter indicates whether or not new data  was accepted. For the meaning in conjunction with the ERROR and STATUS parameters, refer to [Parameters NDR, ERROR, STATUS](#parameters-ndr-error-status-s7-300-s7-400). |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code For the meaning in conjunction with the NDR and STATUS parameters, refer to [Parameters NDR, ERROR, STATUS](#parameters-ndr-error-status-s7-300-s7-400) |
| STATUS | OUTPUT | WORD |  | Status code  For the meaning in conjunction with the parameters NDR and ERROR, refer to [Parameters NDR, ERROR, STATUS](#parameters-ndr-error-status-s7-300-s7-400) |
| DPSTATUS | OUTPUT | Byte | For coding, see below under DPSTATUS | DP status code |

---

**See also**

[DP_RECV (S7-300, S7-400)](#dp_recv-s7-300-s7-400-1)

##### Parameters NDR, ERROR, STATUS (S7-300, S7-400)

###### Condition codes

The following table shows the codes formed by the NDR, ERROR and STATUS parameters that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information about the output parameter RET_VAL in the descriptions of the referenced system program blocks.
>
> Which system program blocks are used and are relevant for error evaluation, can be queried in STEP 7.

| NDR | ERROR | STATUS | Meaning |
| --- | --- | --- | --- |
| 0 | 0 | 8180<sub>H</sub> | - Startup:   The DP service was started but data acceptance is not yet possible. - Normal operation   Data transfer active. - DP has not started due to:   - CP STOP or   - "No parameter assignment" (occurs here instead of the code 0,1,8183<sub>H</sub>). |
| 1 | 0 | 0000<sub>H</sub> | New data accepted without error. |
| 0 | 1 | 8183<sub>H</sub> | No configuration or the DP service has not yet started on the PROFIBUS CP. |
| 0 | 1 | 8184<sub>H</sub> | System error or bad parameter type. |
| 0 | 1 | 8F22<sub>H</sub> | Area length error reading a parameter (e.g. DB too short). |
| 0 | 1 | 8F23<sub>H</sub> | Area length error writing a parameter (e.g. DB too short). |
| 0 | 1 | 8F24<sub>H</sub> | Area error reading a parameter. |
| 0 | 1 | 8F25<sub>H</sub> | Area error writing a parameter. |
| 0 | 1 | 8F28<sub>H</sub> | Alignment error reading a parameter. |
| 0 | 1 | 8F29<sub>H</sub> | Alignment error writing a parameter. |
| 0 | 1 | 8F30<sub>H</sub> | Parameter is in the write­protected 1st current data block. |
| 0 | 1 | 8F31<sub>H</sub> | Parameter is in the write­protected 2nd current data block. |
| 0 | 1 | 8F32<sub>H</sub> | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | DB number error. |
| 0 | 1 | 8F3A<sub>H</sub> | Destination area not loaded (DB). |
| 0 | 1 | 8F42<sub>H</sub> | Timeout reading a parameter from the I/O area. |
| 0 | 1 | 8F43<sub>H</sub> | Timeout writing a parameter to the I/O area. |
| 0 | 1 | 8F44<sub>H</sub> | Address of the parameter to be read is disabled in the access track. |
| 0 | 1 | 8F45<sub>H</sub> | Address of the parameter to be written is disabled in the access track. |
| 0 | 1 | 8F7F<sub>H</sub> | Internal error, e.g. illegal ANY reference. |
| 0 | 1 | 8090<sub>H</sub> | No module with this address exists. |
| 0 | 1 | 8091<sub>H</sub> | Logical base address not at a double word boundary. |
| 0 | 1 | 80A0<sub>H</sub> | Negative acknowledgment reading the module. |
| 0 | 1 | 80B0<sub>H</sub> | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | The number of data bytes to be sent exceeds the upper limit for this service (applies to DP master and DP slave mode). |
| 0 | 1 | 80C0<sub>H</sub> | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> | Resources occupied (memory). |
| 0 | 1 | 80C4<sub>H</sub> | Communications error (occurs temporarily, it is usually best to repeat the job in the user program). |
| 0 | 1 | 80D2<sub>H</sub> | Logical base address incorrect. |

---

**See also**

[DP_RECV (S7-300, S7-400)](#dp_recv-s7-300-s7-400-1)

##### DPSTATUS - DP_RECV parameters (S7-300, S7-400)

###### DPSTATUS

The coding of the DPSTATUS output parameter is different for the DP master mode and DP slave mode.

###### DP master mode

![DP master mode](images/12881996299_DV_resource.Stream@PNG-de-DE.png)

Meaning of the bits in DPSTATUS in DP master mode

| Bit | Meaning |
| --- | --- |
| 7 | not used |
| 6 | This bit is not set.  Please read the information in the manual as well. |
| 5, 4 | Values for DPSTATUS of the DP master:  00 RUN 01 CLEAR 10 STOP (this is now the OFFLINE mode) 11 OFFLINE  Please read the information in the manual as well. |
| 3 | Value 1: Cyclic synchronization is active |
| 2 | Value 0: No new diagnostic data exists Value 1: Evaluation of diagnostic list useful; at least one station has new diagnostic data |
| 1 | Value 0: All DP slaves are in the data transfer phase Value 1: Evaluating the station list is useful |
| 0 | DP mode  Value 0: DP master mode The other bits only have the specified meaning when this bit is not set. |

###### DP slave mode

![DP slave mode](images/12881999371_DV_resource.Stream@PNG-de-DE.png)

Meaning of the bits in DPSTATUS in DP slave mode

| Bit | Meaning |
| --- | --- |
| 7-5 | not used |
| 4 | This bit is not set.  Please read the information in the manual as well. |
| 3 | This bit is not set.  Please read the information in the manual as well. |
| 2 | Value 1: DP master 1 is in the CLEAR mode. The DP slave receives the value 0 in the DP data intended for the outputs. This has no effect on the send data. |
| 1 | Value 1: The configuration/parameter assignment is not yet completed. |
| 0 | Value 1: DP slave mode.   **The other bits only have the specified meaning when this bit is set.** |

> **Note**
>
> Please note, that DPSTATUS must not be evaluated until the return parameter NDR=1 is set.

---

**See also**

[DP_RECV (S7-300, S7-400)](#dp_recv-s7-300-s7-400-1)

#### DP_DIAG (S7-300, S7-400)

This section contains information on the following topics:

- [DP_DIAG (S7-300, S7-400)](#dp_diag-s7-300-s7-400-1)
- [Parameters for DP_DIAG (S7-300, S7-400)](#parameters-for-dp_diag-s7-300-s7-400)
- [Job types for DP_DIAG (S7-300, S7-400)](#job-types-for-dp_diag-s7-300-s7-400)
- [Ring buffer for diagnostics data - DP_DIAG (S7-300, S7-400)](#ring-buffer-for-diagnostics-data---dp_diag-s7-300-s7-400)
- [Parameters NDR, ERROR, STATUS (S7-300, S7-400)](#parameters-ndr-error-status-s7-300-s7-400-1)

##### DP_DIAG (S7-300, S7-400)

###### Description

The DP_DIAG instruction is used to request diagnostic information. The following types of job are possible:

- Request DP station list
- Request DP diagnostics list;
- Request DP single status;
- Read input/output data of a DP slave acyclically
- Read older DP single diagnostic information
- Read DP status.
- Read DP mode for PLC/CP stop
- Read current status of the DP slave.

Diagnostics data can also be requested for a specific slave by specifying a station address.

To transfer the diagnostic data to the CPU, you should reserve a memory area in the CPU and specify this area in the call. This memory area can be a data block area or a bit memory area. The maximum length of the available memory area must also be specified in the job.

> **Note**
>
> The DP_DIAG instruction is only of practical use in the DP master mode.

###### Exclusion

As long as this instruction is running, it must not be supplied with new job data.

Exception: Requesting the DP station list or DP diagnostics list.

###### Call interface

![Call interface](images/12882002443_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Parameters for DP_DIAG (S7-300, S7-400)](#parameters-for-dp_diag-s7-300-s7-400)
  
[Job types for DP_DIAG (S7-300, S7-400)](#job-types-for-dp_diag-s7-300-s7-400)
  
[Ring buffer for diagnostics data - DP_DIAG (S7-300, S7-400)](#ring-buffer-for-diagnostics-data---dp_diag-s7-300-s7-400)
  
[Parameters NDR, ERROR, STATUS (S7-300, S7-400)](#parameters-ndr-error-status-s7-300-s7-400-1)

##### Parameters for DP_DIAG (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the DP_DIAG instruction:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD |  | Module start address   When you configure the CP, the module start address is displayed in the configuration table. Specify this address here. |
| DTYPE | INPUT | BYTE | 0: Station list 1: Diagnostic list 2: Current diagnostic info 3: Older diagnostics info 4: Read   status 5: Read status for  CPU STOP 6: Read status for   CP STOP 7: Read input data   (acyclically) 8: Read output data   (acyclically) 10: Read current status   of the DP slave | Diagnostics type |
| STATION | INPUT | BYTE |  | Station address of the DP slave |
| DIAG | INPUT | ANY  (only the following are permitted as VARTYPE:  BYTE, WORD and DWORD) | The length must be set from 1 to 240 | Specifies the address and length  Address of the data area. References the following alternatives:  - PI area - Memory bit area - Data block area |
| NDR | OUTPUT | BOOL | 0: - 1: new data | This parameter indicates whether or not new data were accepted.  For the meaning in conjunction with the parameters ERROR and STATUS, refer to [Parameters NDR, ERROR, STATUS](#parameters-ndr-error-status-s7-300-s7-400-1) |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code  For the meaning in conjunction with the parameters NDR and STATUS, refer to [Parameters NDR, ERROR, STATUS](#parameters-ndr-error-status-s7-300-s7-400-1) |
| STATUS | OUTPUT | WORD | See list | Status code  For the meaning in conjunction with the parameters NDR and ERROR, refer to [Parameters NDR, ERROR, STATUS](#parameters-ndr-error-status-s7-300-s7-400-1) |
| DIAGLNG | OUTPUT | BYTE | See list | This contains the actual length (in bytes) of the data made available by the PROFIBUS CP, regardless of the buffer size specified in the DIAG parameter.  The following applies to job types with DTYPE 4, 5 and 6  Here, DIAGLNG always has the value "1". The value returned in the DIAG parameter is not relevant for the evaluation in these cases. In these cases, the relevant value is contained in the STATUS parameter. |

---

**See also**

[DP_DIAG (S7-300, S7-400)](#dp_diag-s7-300-s7-400-1)

##### Job types for DP_DIAG (S7-300, S7-400)

###### Job types

The following overview of the specifications for DTYPE, STATION and DIAGLNG shows the permitted or useful entries.

Job types for DP_DIAG

| DTYPE | Corresponds  to job | Parameter  STATION | DIAGLNG | Acknowledgement code  (contained in the STATUS parameter; shown in Table "DP_DIAG codes") |
| --- | --- | --- | --- | --- |
| 0 | Read DP station list | --- | - ignored - | With the DP station list, you obtain information in the user program on the status and availability of DP slaves. The information in the DP station list relates to all DP slaves assigned to the DP master by the configuration. |
| 1 | Read DP diagnostics list | --- | - ignored - | The DP diagnostics list informs the CPU program about the DP slaves with new diagnostics data. |
| 2 | Read current DP single diagnostics data | 1...126 | >=6 | The current DP single diagnostics informs the CPU program of the current diagnostics data of a DP slave. |
| 3 | Read older DP single diagnostic information | 1...126 | >=6 | The older DP single diagnostics informs the CPU program of the older diagnostics data of a DP slave. This data is stored on the PROFIBUS CP and read according to the "last in - first out" principle in the ring buffer.   The structure of the ring buffer is explained below.  If changes occur quickly in the DP slave diagnostic data, this function allows the diagnostic data of a DP slave to be acquired and evaluated in the CPU program of the DP master. |
| 4 | Read the operating status requested with DP-CTRL job (CTYPE=4) |  | =1 | With this job, the DP operating status can be read that was set previously with the DP-CTRL job (CTYPE=4).  Note: The operating status that is read out does not necessarily match the current operating status.  The following operating statuses are possible:  - RUN - CLEAR - STOP (is mapped to the OFFLINE status) <sup>*)</sup> - OFFLINE |
| 5 | Read DP status for CPU STOP |  | =1 | With this job you can find out the DP status to which the PROFIBUS CP changes if the CPU changes to STOP:  - RUN - CLEAR - STOP (is mapped to the OFFLINE status) <sup>*)</sup> - OFFLINE   As default, the PROFIBUS CP changes to the DP status CLEAR if the CPU changes to STOP. |
| 6 | Read DP status for CP STOP |  | =1 | With this job you can find out the DP status to which the PROFIBUS CP changes if the CP changes to STOP:  - STOP (is mapped to the OFFLINE status) <sup>*)</sup> - OFFLINE   As default, the PROFIBUS CP changes to the DP status OFFLINE if the CP changes to STOP. |
| 7 | Read input data | 1...126 | >=1 | With this job, the DP master (class 2) reads the input data of the DP slave. This function is also known as shared input. |
| 8 | Read output data | 1...126 | >=1 | With this job, the DP master (class 2) reads the output data of a DP slave. This function is also known as shared output. |
| 10 | Read current status of the DP slave | 1...126 | >=0 | With this job, you can read out the current status of the DP slave. The following statuses are possible :  - The DP master exchanges data with the DP slave cyclically. - The DP master reads the input data of the DP slave cyclically. - The DP master reads the output data of the DP slaves cyclically. - The DP master is not currently processing this DP slave cyclically. |
| <sup>*) </sup>The STOP status is no longer supported on the latest modules (as of module type DA02). |  |  |  |  |

---

**See also**

[DP_DIAG (S7-300, S7-400)](#dp_diag-s7-300-s7-400-1)

##### Ring buffer for diagnostics data - DP_DIAG (S7-300, S7-400)

###### Ring Buffer for Diagnostic Data

The following diagram illustrates how diagnostic data is read using the "read older DP single diagnostic data" function. The first access reads the **most recent of the older diagnostic data**.

![Ring Buffer for Diagnostic Data](images/12882005515_DV_resource.Stream@PNG-en-US.png)

Ring Buffer for Diagnostic Data

When the current diagnostic data is read out, the read pointer is reset to the first older diagnostic data.

---

**See also**

[DP_DIAG (S7-300, S7-400)](#dp_diag-s7-300-s7-400-1)

##### Parameters NDR, ERROR, STATUS (S7-300, S7-400)

###### Condition codes

The following table shows the codes formed by the NDR, ERROR and STATUS parameters that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information about the output parameter RET_VAL in the descriptions of the referenced system program blocks.
>
> Which system program blocks are used and are relevant for error evaluation, can be queried in STEP 7.

DP_DIAG codes

| NDR | ERROR | STATUS | Possible with DTYPE | Meaning |
| --- | --- | --- | --- | --- |
| 0 | 0 | 8181<sub>H</sub> | 2-10 | Job active.  DP master not started due to   - CP STOP or - No parameter assignment   (occurs here instead of the code 0,1,8183<sub>H</sub>). |
| 0 | 0 | 8182<sub>H</sub> | 0 | Triggering job pointless.  DP master not started due to   - CP STOP or - No parameter assignment   (occurs here instead of the code 0,1,8183<sub>H</sub>). |
| 0 | 0 | 8182<sub>H</sub> | 1 | No new diagnostic data exist.  DP master not started due to   - CP STOP or - No parameter assignment   (occurs here instead of the code 0,1,8183<sub>H</sub>). |
| 1 | 0 | 0000<sub>H</sub> | 0, 1   and 4-9 | Job completed without error.  Note:  With DTYPE 2, 3 and 10, error-free execution is indicated by a status code other than "0". Below you will see the detailed status codes for error-free execution for the range:  82XXH  If an error occurs in execution, you receive status codes in the following ranges:  80XXH, 83XXH, 8FXXH |
| 1 | 0 | 8222<sub>H</sub> | 7,8 | Job completed without error. The length of the DP slave data that was read is not the same as the data length expected by the DP master based on the module list of the DP slave in the CP database. |
| 1 | 0 | 8227<sub>H</sub> | 7,8 | Job completed without error. Message: No data exists. |
| 1 | 0 | 8231<sub>H</sub> | 4,5,6 | Job completed without error. Message: The DP status is already "RUN" |
| 1 | 0 | 8232<sub>H</sub> | 4,5,6 | Job completed without error. Message: The DP status is already "CLEAR" |
| 1 | 0 | 8233<sub>H</sub> | 4,5,6 | Job completed without error. Message: The DP status is already STOP  The STOP status is now the OFFLINE status (here code 8234<sub>H</sub>).  Please read the information in the manual as well. |
| 1 | 0 | 8234<sub>H</sub> | 4,5,6 | Job completed without error. Message: The DP status is already  "OFFLINE" |
| 1 | 0 | 823A<sub>H</sub> | 2,3,7,8 | Job completed without error. Message: 241 or 242 bytes of data were read. 240 bytes of data are available. |
| 1 | 0 | 8241<sub>H</sub> | 2,3,10 | Job completed without error. Message: The specified DP slave was not configured. |
| 1 | 0 | 8243<sub>H</sub> | 2,3,10 | Job completed without error. Message: The module list of the DP slave in the CP database only contains empty modules. |
| 1 | 0 | 8245<sub>H</sub> | 2,3,10 | Job completed without error. Message: The DP slave is in the "read input data cyclically" mode. |
| 1 | 0 | 8246<sub>H</sub> | 2,3,10 | Job completed without error. Message: The DP slave is in the  "read output data cyclically" mode. |
| 1 | 0 | 8248<sub>H</sub> | 2,3,10 | Job completed without error. Note: This is the default code for the named diagnostics types if there is no special situation to signal. |
| 1 | 0 | 8249<sub>H</sub> | 2,3,10 | Job completed without error. Message: The DP slave is deactivated due to a DP mode change ( e.g. CP mode selector set to STOP). |
| 1 | 0 | 824A<sub>H</sub> | 2,3,10 | Job completed without error. Message: The DP slave is deactivated due to a DP_CTRL job in the CPU program. |
| 0 | 1 | 8090<sub>H</sub> | 0-10 | Logical base address of the module is invalid |
| 0 | 1 | 80B0<sub>H</sub> | 0-10 | The module does not recognize the data record or is changing from RUN --> STOP. |
| 0 | 1 | 80B1<sub>H</sub> | 0-10 | Specified data record length incorrect |
| 0 | 1 | 80C0<sub>H</sub> | 0-10 | Data record cannot be read |
| 0 | 1 | 80C1<sub>H</sub> | 0-10 | The specified data record is being processed |
| 0 | 1 | 80C2<sub>H</sub> | 0-10 | Too many jobs pending |
| 0 | 1 | 80C3<sub>H</sub> | 0-8 | Resources (memory) occupied |
| 0 | 1 | 80C4<sub>H</sub> | 0-10 | Communications error |
| 0 | 1 | 80D2<sub>H</sub> | 0-10 | Logical base address wrong |
| 0 | 1 | 8183<sub>H</sub> | 0-10 | DP master not configured. |
| 0 | 1 | 8184<sub>H</sub> | 0-8 | System error or bad parameter type. |
| 0 | 1 | 8311<sub>H</sub> | >=2 | DTYPE parameter outside range of values. |
| 0 | 1 | 8313<sub>H</sub> | 2,3,7,8,10 | STATION parameter outside range of values. |
| 0 | 1 | 8321<sub>H</sub> | >=2 | The DP slave is not providing any valid data. |
| 0 | 1 | 8326<sub>H</sub> | 7,8 | The DP slave has more than 242 bytes of data available. The PROFIBUS CP supports a maximum of 242 bytes. |
| 0 | 1 | 8335<sub>H</sub> | 7,8 | The PROFIBUS CP is in PROFIBUS status: "Station not in ring". |
| 0 | 1 | 8341<sub>H</sub> | 2,3,7,8,10 | The specified slave was not configured |
| 0 | 1 | 8342<sub>H</sub> | 7,8 | The DP slave with the PROFIBUS address specified in the STATION parameter is not obtainable. |
| 0 | 1 | 8349<sub>H</sub> | 7,8 | The DP master is in the OFFLINE mode. |
| 0 | 1 | 8F22<sub>H</sub> | 0-10 | Area length error reading a parameter (e.g. DB too short) |
| 0 | 1 | 8F23<sub>H</sub> | 0-10 | Area length error writing a parameter (e.g. DB too short) |
| 0 | 1 | 8F24<sub>H</sub> | 0-10 | Area error reading a parameter |
| 0 | 1 | 8F25<sub>H</sub> | 0-10 | Area error writing a parameter |
| 0 | 1 | 8F28<sub>H</sub> | 0-10 | Orientation error when reading a parameter |
| 0 | 1 | 8F29<sub>H</sub> | 0-10 | Alignment error writing a parameter |
| 0 | 1 | 8F30<sub>H</sub> | 0-10 | Parameter is in the write­protected 1st current data block |
| 0 | 1 | 8F31<sub>H</sub> | 0-10 | Parameter is in the write­protected 2nd current data block |
| 0 | 1 | 8F32<sub>H</sub> | 0-10 | The DB number in the parameter is too high |
| 0 | 1 | 8F33<sub>H</sub> | 0-10 | DB number error |
| 0 | 1 | 8F3A<sub>H</sub> | 0-10 | Area not loaded (DB) |
| 0 | 1 | 8F42<sub>H</sub> | 0-10 | Timeout reading a parameter from the I/O area |
| 0 | 1 | 8F43<sub>H</sub> | 0-10 | Timeout writing a parameter to the I/O area |
| 0 | 1 | 8F44<sub>H</sub> | 0-10 | Address of the parameter to be read locked in the access track |
| 0 | 1 | 8F45<sub>H</sub> | 0-10 | Address of the parameter to be written is disabled in the access track |
| 0 | 1 | 8F7F<sub>H</sub> | 0-10 | Internal error, e.g. illegal ANY reference |

---

**See also**

[DP_DIAG (S7-300, S7-400)](#dp_diag-s7-300-s7-400-1)

#### DP_CTRL (S7-300, S7-400)

This section contains information on the following topics:

- [DP_CTRL (S7-300, S7-400)](#dp_ctrl-s7-300-s7-400-1)
- [Parameters for DP_CTRL (S7-300, S7-400)](#parameters-for-dp_ctrl-s7-300-s7-400)
- [Job types for DP_CTRL (S7-300, S7-400)](#job-types-for-dp_ctrl-s7-300-s7-400)
- [Command mode and group select - DP_CTRL (S7-300, S7-400)](#command-mode-and-group-select---dp_ctrl-s7-300-s7-400)
- [Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-5)

##### DP_CTRL (S7-300, S7-400)

###### Description

The DP_CTRL instruction transfers control jobs to the PROFIBUS CP. You specify a job field (CONTROL parameter) to specify the control job in greater detail.

The following types of job are possible:

- Global control acyclic/cyclic;
- Delete older diagnostic data;
- Set current DP mode;
- Set DP mode for PLC/CP STOP;
- Read input/output data cyclically;
- Set the operating mode of the DP slave.

There are restrictions relating to the job types listed here (please refer to the information in the manual for the module).

> **Note**
>
> The DP_CTRL instruction is only of practical use in the DP master mode.

###### Connector

As long as this instruction is running, it must not be supplied with new job data.

###### Call interface

![Call interface](images/12882008587_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Parameters for DP_CTRL (S7-300, S7-400)](#parameters-for-dp_ctrl-s7-300-s7-400)
  
[Job types for DP_CTRL (S7-300, S7-400)](#job-types-for-dp_ctrl-s7-300-s7-400)
  
[Command mode and group select - DP_CTRL (S7-300, S7-400)](#command-mode-and-group-select---dp_ctrl-s7-300-s7-400)
  
[Parameters DONE, ERROR, STATUS (S7-300, S7-400)](#parameters-done-error-status-s7-300-s7-400-5)

##### Parameters for DP_CTRL (S7-300, S7-400)

###### Explanation of the formal parameters

The following table explains all the formal parameters for the DP_CTRL instruction:

| Parameter | Declaration | Data type | Range of values | Description |
| --- | --- | --- | --- | --- |
| CPLADDR | INPUT | WORD |  | Module start address   When you configure the CP, the module start address is displayed in the configuration table. Specify this address here. |
| CONTROL | INPUT | ANY  (only the following are permitted as VARTYPE:  BYTE, WORD and DWORD) | The length must be set from 1 to 240 | Specifies the address and length of the CONTROL job field  Address of the data area. References the following alternatives:  - PI area - Memory bit area - Data block area   The length must be at least as long as the number of parameters. |
| DONE | OUTPUT | BOOL | 0: - 1: Job executed without error. | Indicates whether the job was sent and completed without errors.  For the meaning in conjunction with the parameters ERROR and STATUS, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-5) |
| ERROR | OUTPUT | BOOL | 0: - 1: Error | Error code For the meaning in conjunction with the DONE and STATUS parameters, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-5) |
| STATUS | OUTPUT | WORD | See following table 'Return Codes' | Status code For the meaning in conjunction with the DONE and ERROR parameters, refer to [Parameters DONE, ERROR, STATUS](#parameters-done-error-status-s7-300-s7-400-5) |

###### Structure of the CONTROL job field

The control job has the following structure:

![Structure of the CONTROL job field](images/12882011659_DV_resource.Stream@PNG-en-US.png)

###### Example of the job field

With a job field as shown below, a cyclic global control job SYNC and UNFREEZE is sent for group 4 and group 5 without the autoclear option.

![Example of the job field](images/12882014731_DV_resource.Stream@PNG-de-DE.png)

The length in the ANY pointer must be at least 4 (in the example, 30 has been selected).

---

**See also**

[DP_CTRL (S7-300, S7-400)](#dp_ctrl-s7-300-s7-400-1)

##### Job types for DP_CTRL (S7-300, S7-400)

###### Job types

Permitted or feasible specifications for the job are shown in the following overview based on the specification for CTYPE and the information in the job field.

| CTYPE | Corresponds to job | Parameter in job field |  | Description |
| --- | --- | --- | --- | --- |
| **Name** | **Quantity** |  |  |  |
| 0 | Trigger global control | 1. byte: command mode 2nd byte: group select  (See section following this table.) | 2 | A single global control job is sent to the DP slaves selected with group select. The command mode parameter specifies the following global control jobs:  - SYNC - UNSYNC - FREEZE - UNFREEZE - CLEAR - is not supported (please read the information in the manual as well)   It is possible to specify more than one job in the command mode parameter. |
| 1<sup>*)</sup> | Trigger cyclic global control | 1. byte: command mode 2nd byte: group select 3rd byte: autoclear  (See section  following this table.) | 3 | The sending of cyclic global control jobs to the DP slaves selected with group select is triggered on the PROFIBUS CP.   The autoclear parameter is only evaluated with the SYNC global control job. If at least one DP slave in the selected group is not in the data transfer phase and autoclear = 1 is set, the CLEAR mode is activated. In other words, the output data of the DP slaves is set to "0".  The following global jobs can be activated in the command mode parameter:  - SYNC - FREEZE - CLEAR (CLEAR-Bit = 1) - is not supported (please read the information in the manual as well)   or deactivated:  - UNSYNC - UNFREEZE - UNCLEAR (CLEAR bit = 0)   It is possible to specify more than one job in the command mode parameter.  An active cyclic global control job can only be terminated by a further global control job (cyclic or acyclic).  To terminate the job set in the command mode, the job must be canceled. For example, the SYNC job  is canceled by an UNSYNC job. |
| 3 | Delete older DP single diagnostic data | 1. byte:  Slave address 1..126  127 = all slaves | 1 | The older diagnostic data stored on the PROFIBUS CP is deleted for one or all DP slaves. |
| 4 | Set current DP mode | 1. byte:  RUN = 00<sub>H</sub> CLEAR = 01<sub>H</sub> OFFLINE = 03<sub>H</sub> RUN with AUTOCLEAR = 04<sub>H</sub> RUN without AUTOCLEAR = 04<sub>H</sub> | 1 | The DP mode can be set with this job as follows:  - RUN - CLEAR - OFFLINE   The AUTOCLEAR parameter means that the DP master class 1 changes to the CLEAR status automatically when the following condition is met: at least one of the DP slaves with which the DP master class 1 wants to exchange data is not in the data transfer phase.   The RUN without AUTOCLEAR parameter resets AUTOCLEAR.  Notes:  The STOP = 02<sub>H</sub> mode is no longer supported on the later modules (as of module type DA02). STOP = 02<sub>H</sub> is mapped to the OFFLINE mode. |
| 5 | Set DP mode for CPU STOP | 1. byte:  RUN = 00<sub>H</sub> CLEAR = 01<sub>H</sub> OFFLINE = 03<sub>H</sub> | 1 | This job specifies which DP mode the PROFIBUS CP changes to if the CPU changes to STOP:  - RUN - CLEAR - OFFLINE   As default, the PROFIBUS CP changes to the DP status CLEAR if the CPU changes to STOP.  This mode remains set during a CP mode change from RUN --> STOP --> RUN.  Notes:  The STOP = 02<sub>H</sub> mode is no longer supported on the later modules (as of module type DA02). STOP = 02<sub>H</sub> is mapped to the OFFLINE mode. |
| 6 | Set DP mode for CP STOP | 1. byte:  OFFLINE=03<sub>H</sub> | 1 | This job specifies which DP mode the PROFIBUS CP changes to if the CP changes to STOP.  - OFFLINE   As default, the PROFIBUS CP changes to the DP status OFFLINE if the CP changes to STOP.  This mode remains set during a CP mode change from RUN --> STOP --> RUN.  Notes:  The STOP = 02<sub>H</sub> mode is no longer supported on the later modules (as of module type DA02). STOP = 02<sub>H</sub> is mapped to the OFFLINE mode. |
| 7 <sup>*)</sup> | Read input data cyclically (DP master class 2) | 1. byte: slave address 1 to 125 | 1 | This job is not supported.  Please read the information in the manual as well. |
| 8 <sup>*)</sup> | Read output data cyclically (DP master class 2) | 1. byte: slave address 1 to 125 | 1 | This job is not supported.  Please read the information in the manual as well. |
| 9 | Terminate cyclic processing of the DP slave by the DP master (class 1, class 2) | 1. byte: slave address 1 to 125 | 1 | This job terminates the cyclic reading of the input data or output data of the addressed DP slave or the data transfer (DP master class 1).  The DP slave is then no longer processed by the PROFIBUS CP acting as DP master (class 2).   **This deactivates the DP slave.** |
| 10 | Start cyclic processing as DP master (class 1) | 1. byte: slave address 1 to 125 | 1 | The PROFIBUS CP acting as the DP master (class 1) then assigns parameters to the addressed DP slave and starts cyclic data transfer (writing outputs/reading inputs).   **This activates the DP slave.** |
| <sup>*) </sup>This CTYPE is no longer supported on the latest modules (as of module type DA02). |  |  |  |  |

---

**See also**

[DP_CTRL (S7-300, S7-400)](#dp_ctrl-s7-300-s7-400-1)

##### Command mode and group select - DP_CTRL (S7-300, S7-400)

###### Structure of command mode

In the command mode parameter, you specify the modes for input and output data for the cyclic and acyclic global control jobs.

The meaning is as follows:

1 = activated  
0 = not activated

![Structure of command mode](images/12882017803_DV_resource.Stream@PNG-en-US.png)

###### Structure of group select

In the group select parameter, you specify the group to be addressed by the control job specified in the command mode parameter. The group select parameter occupies the second byte in the control job. Each bit defines a possible DP slave group.

The meaning is as follows:

1 = assigned  
0 = not assigned

![Structure of group select](images/12882020875_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[DP_CTRL (S7-300, S7-400)](#dp_ctrl-s7-300-s7-400-1)

##### Parameters DONE, ERROR, STATUS (S7-300, S7-400)

###### Condition codes

The following table shows the return codes formed by the DONE, ERROR and STATUS parameters that must be evaluated by the user program.

> **Note**
>
> For entries coded with 8Fxx<sub>H</sub> in STATUS, refer to the information about the output parameter RET_VAL in the descriptions of the referenced system program blocks.
>
> Which system program blocks are used and are relevant for error evaluation, can be queried in STEP 7.

DP_CTRL condition codes

| DONE | ERROR | STATUS | Possible with CTYPE | Meaning |
| --- | --- | --- | --- | --- |
| 0 | 0 | 8181<sub>H</sub> | 0..10 | Job active.  DP master not started due to:   - CP STOP or - "no parameter assignment"   Note:  The code described here occurs instead of one of the codes described later: 0, 1, 8183<sub>H</sub> 0, 1, 8333<sub> H</sub> 0, 1, 8334<sub>H</sub> |
| 1 | 0 | 0000<sub>H</sub> | 0..10 | **Job completed without error.** |
| 1 | 0 | 8214<sub>H</sub> | 0,1 | **Job completed without error.**  Message: Cyclic global control job is sent as acyclic global control job |
| 1 | 0 | 8215<sub>H</sub> | 0,1 | **Job completed without error.**  The slaves addressed in the selected group are all deactivated. |
| 1 | 0 | 8219<sub>H</sub> | 0,1 | **Job completed without error.**  An attempt was made to send an already active cyclic global control again. The global control continues unchanged. |
| 1 | 0 | 8228<sub>H</sub> | 0,1 | **Job completed without error.**  Message: The DP slaves addressed in the selected groups do not have any input modules. |
| 1 | 0 | 8229<sub>H</sub> | 0,1 | **Job completed without error.**  Message: The DP slaves addressed in the selected groups do not have any output modules. |
| 1 | 0 | 8231<sub>H</sub> | 4,5,6 | **Job completed without error.**  Message: The DP status is already "RUN" |
| 1 | 0 | 8232<sub>H</sub> | 4,5,6 | **Job completed without error.**  Message: The DP status is already "CLEAR" |
| 1 | 0 | 8233<sub>H</sub> | 4,5,6 | **Job completed without error.**  Message: The DP status is already "STOP" |
| 1 | 0 | 8234<sub>H</sub> | 4,5,6 | **Job completed without error.**  Message: The DP status is already "OFFLINE" |
| 1 | 0 | 8235<sub>H</sub> | 4 | **Job completed without error.**  Message: The DP status is already "RUN" with activated AUTOCLEAR |
| 1 | 0 | 8236<sub>H</sub> | 4 | **Job completed without error.**  Message: The DP status is already "RUN" with deactivated AUTOCLEAR |
| 1 | 0 | 8241<sub>H</sub> | 7-10 | **Job completed without error.**  Message: The specified DP slave was not configured. |
| 1 | 0 | 8243<sub>H</sub> | 7-10 | **Job completed without error.**  Message: The DP slave is already deactivated since the module list of the DP slave in the CP database only contains empty modules. |
| 1 | 0 | 8245<sub>H</sub> | 7-10 | **Job completed without error.**  Message: The DP slave is already in the "read input data cyclically" mode |
| 1 | 0 | 8246<sub>H</sub> | 7-10 | **Job completed without error.**  Message: The DP slave is already in the "read output data cyclically" mode |
| 1 | 0 | 8248<sub>H</sub> | 7-10 | **Job completed without error.**  Message: The module list of the DP slave in the CP database contains input, output, or input/output modules. |
| 1 | 0 | 8249<sub>H</sub> | 7-10 | **Job completed without error.**  Message: This slave is deactivated due to a change in the DP mode. |
| 1 | 0 | 824A<sub>H</sub> | 7-10 | **Job completed without error.**  Message: The DP slave is already deactivated due to a DP_CTRL job in the CPU program. |
| 0 | 1 | 8090<sub>H</sub> | 0..10 | No module with this address exists. |
| 0 | 1 | 8091<sub>H</sub> | 0..10 | Logical address not at a double word boundary. |
| 0 | 1 | 80B0<sub>H</sub> | 0..10 | The module does not recognize the data record. |
| 0 | 1 | 80B1<sub>H</sub> | 0..10 | The specified data record length is incorrect. |
| 0 | 1 | 80C0<sub>H</sub> | 0..10 | The data record cannot be read. |
| 0 | 1 | 80C1<sub>H</sub> | 0..10 | The specified data record is currently being processed. |
| 0 | 1 | 80C2<sub>H</sub> | 0..10 | There are too many jobs pending. |
| 0 | 1 | 80C3<sub>H</sub> |  | Resources occupied (memory). |
| 0 | 1 | 8183<sub>H</sub> | 0..10 | The DP master is not configured...  Note:  If the DP master is in "STOP" status, the status 8181<sub> H</sub> can also be output. |
| 0 | 1 | 8184<sub>H</sub> |  | System error or illegal parameter type... |
| 0 | 1 | 8311<sub>H</sub> | 0..10 | CTYPE parameter outside the range of values |
| 0 | 1 | 8312<sub>H</sub> | 0..10 | The length of the area in the CONTROL parameter is too short. |
| 0 | 1 | 8313<sub>H</sub> | 3,7,8,9, 10 | The slave address parameter is outside the range of values. |
| 0 | 1 | 8315<sub>H</sub> | 0,1 | All DP slaves of the group specified in the global control are deactivated (always occurs with an empty group). |
| 0 | 1 | 8317<sub>H</sub> | 8 | The length of the configured output data is greater than the configured receive area of the DP slave.   Activating the slave mode "Read output data" is not possible. |
| 0 | 1 | 8318<sub>H</sub> | 0,1,4,5,6 | The parameter 1st byte of the job data field is outside the range of values. With GLOBAL CONTROL, CLEAR was used with SYNC or a GLOBAL CONTROL with CLEAR set was sent to group 0. |
| 0 | 1 | 831A<sub>H</sub> | 0,1 | At least one DP slave cannot handle FREEZE. |
| 0 | 1 | 831B<sub>H</sub> | 0,1 | At least one DP slave cannot handle SYNC. |
| 0 | 1 | 8333<sub>H</sub> | 0,1 | This job is not permitted in the DP "STOP" mode.  Note: If no DP master is configured, the status 8181<sub> H</sub> can also be output. |
| 0 | 1 | 8334<sub>H</sub> | 0, 1 | This job is not permitted in the DP "OFFLINE" mode.  Note: If no DP master is configured, the status 8181<sub> H</sub> can also be output. |
| 0 | 1 | 8335<sub>H</sub> | 0, 1 | The PROFIBUS CP is in PROFIBUS status: "Station not in ring". |
| 0 | 1 | 8339<sub>H</sub> | 0, 1 | At least one DP slave in the selected group is not in the data transfer phase. |
| 0 | 1 | 833C<sub>H</sub> | 1 | Cyclic global control must not be used in  the "PLC <-> CP free running" mode. This error does not occur on the CP 3425 because this mode is not possible with this CP (PBUS data records are always used for data transfer). |
| 0 | 1 | 8341<sub>H</sub> | 7-10 | The specified DP slave was not configured. |
| 0 | 1 | 8183<sub>H</sub> | 0..10 | DP master not configured. |
| 0 | 1 | 8184<sub>H</sub> | - | System error or bad parameter type. |
| 0 | 1 | 8F22<sub>H</sub> | 0..10 | Area length error reading a parameter (e.g. DB too short). |
| 0 | 1 | 8F23<sub>H</sub> | 0..10 | Area length error writing a parameter. |
| 0 | 1 | 8F24<sub>H</sub> | 0..10 | Area error reading a parameter. |
| 0 | 1 | 8F25<sub>H</sub> | 0..10 | Area error writing a parameter. |
| 0 | 1 | 8F28<sub>H</sub> | 0..10 | Alignment error reading a parameter. |
| 0 | 1 | 8F29<sub>H</sub> | 0..10 | Alignment error writing a parameter. |
| 0 | 1 | 8F30<sub>H</sub> | 0..10 | The parameter is in the write­protected first current data block. |
| 0 | 1 | 8F31<sub>H</sub> | 0..10 | The parameter is in the write­protected second current data block. |
| 0 | 1 | 8F32<sub>H</sub> | 0..10 | Parameter contains a DB number that is too high. |
| 0 | 1 | 8F33<sub>H</sub> | 0..10 | DB number error. |
| 0 | 1 | 8F3A<sub>H</sub> | 0..10 | Area not loaded (DB). |
| 0 | 1 | 8F42<sub>H</sub> | 0..10 | Timeout reading a parameter from the I/O area. |
| 0 | 1 | 8F43<sub>H</sub> | 0..10 | Timeout writing the parameter to the I/O area. |
| 0 | 1 | 8F44<sub>H</sub> | 0..10 | Access to a parameter to be read during execution of the instruction is prevented. |
| 0 | 1 | 8F45<sub>H</sub> | 0..10 | Access to a parameter to be written during execution of the instruction is prevented. |
| 0 | 1 | 8F7F<sub>H</sub> | 0..10 | Internal error, e.g. illegal ANY reference. |
| 0 | 1 | 80C4<sub>H</sub> | 0..10 | Communications error (occurs temporarily, it is usually best to repeat the job in the user program). |
| 0 | 1 | 80D2<sub>H</sub> | 0..10 | Logical base address incorrect. |

---

**See also**

[DP_CTRL (S7-300, S7-400)](#dp_ctrl-s7-300-s7-400-1)
