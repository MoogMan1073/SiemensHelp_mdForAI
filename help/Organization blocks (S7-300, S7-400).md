---
title: "Organization blocks (S7-300, S7-400)"
package: ProgOB34enUS
topics: 25
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Organization blocks (S7-300, S7-400)

This section contains information on the following topics:

- [English designations of the OB types (S7-300, S7-400)](#english-designations-of-the-ob-types-s7-300-s7-400)
- [Overview of organization blocks (S7-300, S7-400)](#overview-of-organization-blocks-s7-300-s7-400)
- [Cyclic program (OB 1) (S7-300, S7-400)](#cyclic-program-ob-1-s7-300-s7-400)
- [Time-of-day interrupt organization blocks (OB 10 to OB 17) (S7-300, S7-400)](#time-of-day-interrupt-organization-blocks-ob-10-to-ob-17-s7-300-s7-400)
- [Time-delay interrupt organization blocks (OB 20 to OB 23) (S7-300, S7-400)](#time-delay-interrupt-organization-blocks-ob-20-to-ob-23-s7-300-s7-400)
- [Cyclic interrupt organization blocks (OB 30 to OB 38) (S7-300, S7-400)](#cyclic-interrupt-organization-blocks-ob-30-to-ob-38-s7-300-s7-400)
- [Hardware interrupt organization blocks (OB 40 to OB 47) (S7-300, S7-400)](#hardware-interrupt-organization-blocks-ob-40-to-ob-47-s7-300-s7-400)
- [Status interrupt OB (OB 55) (S7-300, S7-400)](#status-interrupt-ob-ob-55-s7-300-s7-400)
- [Update interrupt OB (OB 56) (S7-300, S7-400)](#update-interrupt-ob-ob-56-s7-300-s7-400)
- [OB for manufacturer-specific alarms (OB 57) (S7-300, S7-400)](#ob-for-manufacturer-specific-alarms-ob-57-s7-300-s7-400)
- [Synchronous cycle interrupt OBs (OB 61 to OB 64) (S7-300, S7-400)](#synchronous-cycle-interrupt-obs-ob-61-to-ob-64-s7-300-s7-400)
- [Time error OB (OB 80) (S7-300, S7-400)](#time-error-ob-ob-80-s7-300-s7-400)
- [Power supply error organization block (OB 81) (S7-300, S7-400)](#power-supply-error-organization-block-ob-81-s7-300-s7-400)
- [Diagnostic interrupt OB (OB 82) (S7-300, S7-400)](#diagnostic-interrupt-ob-ob-82-s7-300-s7-400)
- [Insert/remove module interrupt organization block (OB 83) (S7-300, S7-400)](#insertremove-module-interrupt-organization-block-ob-83-s7-300-s7-400)
- [CPU hardware fault organization block (OB 84) (S7-300, S7-400)](#cpu-hardware-fault-organization-block-ob-84-s7-300-s7-400)
- [Priority class error organization block (OB 85) (S7-300, S7-400)](#priority-class-error-organization-block-ob-85-s7-300-s7-400)
- [Rack failure organization block (OB 86) (S7-300, S7-400)](#rack-failure-organization-block-ob-86-s7-300-s7-400)
- [Communication error organization block (OB 87) (S7-300, S7-400)](#communication-error-organization-block-ob-87-s7-300-s7-400)
- [Processing interrupt OB (OB 88) (S7-300, S7-400)](#processing-interrupt-ob-ob-88-s7-300-s7-400)
- [Background organization block (OB 90) (S7-300, S7-400)](#background-organization-block-ob-90-s7-300-s7-400)
- [Startup organization blocks (OB 100, OB 101 and OB 102) (S7-300, S7-400)](#startup-organization-blocks-ob-100-ob-101-and-ob-102-s7-300-s7-400)
- [Programming error organization block (OB 121) (S7-300, S7-400)](#programming-error-organization-block-ob-121-s7-300-s7-400)
- [I/O access error organization block (OB 122) (S7-300, S7-400)](#io-access-error-organization-block-ob-122-s7-300-s7-400)

## English designations of the OB types (S7-300, S7-400)

### English designation of the OB types

When an OB is created in the "Add new block" dialog, the OB types can only be displayed in English for technical reasons – irrespective of the set user interface language. In order to facilitate handling, the following table lists the English terms and their corresponding designations in the set user interface language. The table applies to the superset of S7-300 and S7-400 CPUs.

| English designation of the OB type in the "Add new block" dialog. |  |  | Designation in the information system |
| --- | --- | --- | --- |
| Time interrupts |  |  | Time interrupts |
|  | Time of day |  | Time-of-day interrupts |
|  |  | TOD_INT0 [OB10] to TOD_INT7 [OB17] | Time-of-day interrupt OBs |
|  | Time delay |  | Time-delay interrupts |
|  |  | DEL_INT0 [OB20] to DEL_INT3 [OB23] | Time-delay interrupt OBs |
|  | Cyclic |  | Cyclic interrupts |
|  |  | CYC_INT0 [OB30] to CYC_INT8 [OB38] | Cyclic interrupt OBs |
| Hardware Interrupts |  |  | Hardware interrupts |
|  |  | HW_INT0 [OB40] to HW_INT7 [OB47] | Hardware interrupt OB |
| Startup |  |  | Startup |
|  |  | BACKGROUND [OB90] | Background OB |
|  |  | COMPLETE RESTART [OB100] | Warm restart |
|  |  | RESTART [OB101] | Hot restart |
|  |  | COLD RESTART [OB102] | Cold restart |
| Alarming |  |  |  |
|  |  | DP: STATUS ALARM [OB55] | Status interrupt OB |
|  |  | DP: UPDATE ALARM [OB56] | Update interrupt OB |
|  |  | DP: MANUFACTURE ALARM [OB57] | Vendor-specific interrupt OB |
|  |  | MULTI_INT [OB 60] | Multicomputing interrupt OB |
|  |  | SYNC_1 [OB61] to SYNC_4 [OB64] | Isochronous mode interrupt OBs |
| Fault Interrupts |  |  | Fault |
|  |  | CYCL_FLT [OB 80] | Time error OB |
|  |  | PS_FLT [OB81] | Power supply error OB |
|  |  | I/O_FLT1 [OB82] | Diagnostic interrupt OB |
|  |  | I/O_FLT2 [OB83] | Pull/plug interrupt OB |
|  |  | CPU_FLT [OB84] | CPU hardware fault OB |
|  |  | OBNL_FLT [OB85] | Program execution error OB |
|  |  | RACK_FLT [OB86] | Rack failure OB |
|  |  | COMM_FLT [OB87] | Communications error OB |
|  |  | BREAKUP ERROR [OB88] | Processing abort OB |
|  |  | PROG_ERR [OB121] | Programming error OB |
|  |  | MOD_ERR [OB122] | I/O access error OB |

## Overview of organization blocks (S7-300, S7-400)

### Organization blocks

Organization blocks (OBs) are the interface between the CPU operating system and the user program. OBs are used to execute specific program sections:

- At CPU startup
- In cyclic or clocked execution
- Whenever errors occur
- Whenever hardware interrupts occur.

Organization blocks are executed according to the priority they have been allocated.

### Available OBs

Not all CPUs can process all OBs available in S7. See the operation list of your CPU to determine which OBs are available to you.

### Start events and default priority class

The following table contains the start event belonging to each OB as well as the default priority class.

| OB | Start event | Default priority class | Explanation |
| --- | --- | --- | --- |
| OB 1 | End of startup or end of OB 1 | 1 | Free cycle |
| OB 10 | Time-of-day interrupt 0 | 2 | No default time specified |
| OB 11 | Time-of-day interrupt 1 | 2 |  |
| OB 12 | Time-of-day interrupt 2 | 2 |  |
| OB 13 | Time-of-day interrupt 3 | 2 |  |
| OB 14 | Time-of-day interrupt 4 | 2 |  |
| OB 15 | Time-of-day interrupt 5 | 2 |  |
| OB 16 | Time-of-day interrupt 6 | 2 |  |
| OB 17 | Time-of-day interrupt 7 | 2 |  |
| OB 20 | Time-delay interrupt 0 | 3 | No default time specified |
| OB 21 | Time-delay interrupt 1 | 4 |  |
| OB 22 | Time-delay interrupt 2 | 5 |  |
| OB 23 | Time-delay interrupt 3 | 6 |  |
| OB 30 | Cyclic interrupt 0 (default: 5 s sampling time) | 7 | Cyclic interrupts |
| OB 31 | Cyclic interrupt 1 (default: 2 s sampling time) | 8 |  |
| OB 32 | Cyclic interrupt 2 (default: 1 s sampling time) | 9 |  |
| OB 33 | Cyclic interrupt 3 (default: 500 ms sampling time) | 10 |  |
| OB 34 | Cyclic interrupt 4 (default: 200 ms sampling time) | 11 |  |
| OB 35 | Cyclic interrupt 5 (default: 100 ms sampling time) | 12 |  |
| OB 36 | Cyclic interrupt 6 (default: 50 ms sampling time) | 13 |  |
| OB 37 | Cyclic interrupt 7 (default: 20 ms sampling time) | 14 |  |
| OB 38 | Cyclic interrupt 8 (default: 10 ms sampling time) | 15 |  |
| OB 40 | Hardware interrupt 0 | 16 | Hardware interrupts |
| OB 41 | Hardware interrupt 1 | 17 |  |
| OB 42 | Hardware interrupt 2 | 18 |  |
| OB 43 | Hardware interrupt 3 | 19 |  |
| OB 44 | Hardware interrupt 4 | 20 |  |
| OB 45 | Hardware interrupt 5 | 21 |  |
| OB 46 | Hardware interrupt 6 | 22 |  |
| OB 47 | Hardware interrupt 7 | 23 |  |
| OB 55 | Status interrupt | 2 | DPV1 interrupts |
| OB 56 | Update interrupt | 2 |  |
| OB 57 | Manufacturer-specific interrupt | 2 |  |
| OB 61 | Isochronous mode interrupt 1 | 25 | Isochronous mode interrupts |
| OB 62 | Isochronous mode interrupt 2 | 25 |  |
| OB 63 | Isochronous mode interrupt 3 | 25 |  |
| OB 64 | Isochronous mode interrupt 4 | 25 |  |
| OB 80 | Time error | 26, 28 <sup>1</sup> | Asynchronous error interrupts |
| OB 81 | Power supply error | 26, 28 <sup>1</sup> for S7-300,  25, 28 <sup>1</sup> for S7-400 |  |
| OB 82 | Diagnostic interrupt | 26, 28 <sup>1</sup> for S7-300,  25, 28 <sup>1</sup> for S7-400 |  |
| OB 83 | Pull/plug interrupt | 26, 28 <sup>1</sup> for S7-300,  25, 28 <sup>1</sup> for S7-400 |  |
| OB 84 | CPU hardware fault | 26, 28 <sup>1</sup> for S7-300,  25, 28 <sup>1</sup> for S7-400 |  |
| OB 85 | Priority class error | 26, 28 <sup>1</sup> for S7-300,  25, 28 <sup>1</sup> for S7-400 |  |
| OB 86 | Failure of an expansion device, of a DP master system or a device for distributed I/O | 26, 28 <sup>1</sup> for S7-300,  25, 28 <sup>1</sup> for S7-400 |  |
| OB 87 | Communication error | 26, 28 <sup>1</sup> for S7-300,  25, 28 <sup>1</sup> for S7-400 |  |
| OB 88 | Processing interrupt | 28 |  |
| OB 90 | Warm restart or cold restart or deleting of a block being executed in OB 90, or loading of an OB 90 into the CPU or end of OB 90 | 29 <sup>2)</sup> | Background cycle |
| OB 100 | Warm restart | 27 <sup>1</sup> | Startup |
| OB 101 | Hot restart | 27 <sup>1</sup> |  |
| OB 102 | Cold restart | 27 <sup>1</sup> |  |
| OB 121 | Programming error | Priority class of the OB that has caused the error | Synchronous error interrupts |
| OB 122 | I/O access error | Priority class of the OB that has caused the error |  |
| <sup>1</sup>Priority classes 27 and 28 are valid in the priority class model of the startup.   <sup>2</sup>Priority class 29 corresponds to priority 0.29. This means that the background cycle has lower priority than does the free cycle. |  |  |  |

## Cyclic program (OB 1) (S7-300, S7-400)

### Description

The operating system of the S7 CPU executes OB 1 cyclically. When OB 1 has been executed, the operating system starts executing OB 1 again. Cyclic execution of OB 1 is started after the startup has been completed. You can call instructions in OB 1.

### Function of OB 1

OB 1 has the lowest priority of all OBs that are monitored for runtime. With the exception of OB 90 all other OBs can interrupt execution of OB 1. The following events cause the operating system to call OB 1:

- End of startup processing
- The execution of OB 1 (the previous cycle) has finished.

When OB 1 has been executed, the operating system sends global data. Before restarting OB 1, the operating system writes the process image output to the output modules, updates the process image input, and receives any global data for the CPU.

S7 monitors the maximum cycle time, ensuring a maximum response time. The value for the maximum cycle time is preset to 150 ms. You can set a new value or you can restart the time monitoring anywhere within your program with the "RE_TRIGR" instruction. If your program exceeds the maximum cycle time for OB 1, then the operating system calls OB 80 (time error OB). If OB 80 has not been programmed, the CPU changes to STOP mode.

Apart from monitoring the maximum cycle time, it is also possible to guarantee a minimum cycle time. The operating system will delay the start of a new cycle (writing of the process image output to the output modules) until the minimum cycle time has been reached.

The configuration is used to change the maximum and minimum cycle time parameters.

### Local data for OB 1

The following table describes the temporary (TEMP) tags for OB 1. The tag names are the default names of OB 1.

| Tag | Data type | Description |
| --- | --- | --- |
| OB1_EV_CLASS | BYTE | Event class and identifiers:  B#16#11: OB 1 is active |
| OB1_SCAN_1 | BYTE | - B#16#01: Completion of the warm restart - B#16#02: Completion of the hot restart - B#16#03: Completion of the free cycle - B#16#04: Completion of the cold restart - B#16#05: First OB 1 cycle of the new master CPU after master-reserve switchover and STOP of the previous master |
| OB1_PRIORITY | BYTE | Priority class: 1 |
| OB1_OB_NUMBR | BYTE | OB number (01) |
| OB1_RESERVED_1 | BYTE | Reserved |
| OB1_RESERVED_2 | BYTE | Reserved |
| OB1_PREV_CYCLE | INT | Runtime of last scan cycle (ms). |
| OB1_MIN_CYCLE | INT | Minimum cycle time (ms) since the last startup |
| OB1_MAX_CYCLE | INT | Maximum cycle time (ms) since the last startup |
| OB1_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

## Time-of-day interrupt organization blocks (OB 10 to OB 17) (S7-300, S7-400)

### Description

S7 provides up to eight OBs (OB 10 to OB 17) which can be started once or periodically. You can assign parameters for your CPU in such a manner that these OBs are processed in the following intervals:

- Once
- Every minute
- Hourly
- Daily
- Weekly
- Monthly
- Yearly
- End of month

  > **Note**
  >
  > For monthly execution of a time-of-day interrupt OB, only the days 1, 2, to 28 can be used as a starting date.

### Function of time-of-day interrupt OBs

To start a time-of-day interrupt, you must first set and then activate the interrupt. The three following start possibilities exist:

- Automatic start of the time-of-day interrupt. This occurs if you have both set and activated the time-of-day interrupt per configuration. The following table shows the principle possibilities when activating a time-of-day interrupt per configuration.
- You set the time-of-day interrupt per configuration and then activate it by calling the "[ACT_TINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)" instruction in your program.
- You set the time-of-day interrupt by calling the "[SET_TINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#set_tint-set-time-of-day-interrupt-s7-300-s7-400)" instruction and then activate it by the "[ACT_TINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#act_tint-enable-time-of-day-interrupt-s7-300-s7-400)" instruction.

| Interval | Description |
| --- | --- |
| Not activated | The time-of-day interrupt OB is not executed, even when it is loaded in the CPU. You can activate the time-of-day interrupt by calling the "ACT_TINT" instruction. |
| Activated once only | The time-of-day interrupt OB is canceled automatically after it runs once as specified.  Your program can use the "SET_TINT" instruction to reset the time-of-day interrupt and the "ACT_TINT" instruction to reactivate it. |
| Activated periodically | When the time-of-day interrupt occurs, the CPU calculates the next start time for the time-of-day interrupt based on the current time of day and the period. |

> **Note**
>
> If you configure a time-of-day interrupt in such a way that the corresponding OB is to be processed once, the date and time must not be in the past (relative to the real-time clock of the CPU).
>
> If you configure a time-of-day interrupt in such a way that the corresponding OB is to be processed periodically, but the start date and time are in the past, then the time-of-day interrupt will be processed the next time it is due. This is illustrated in the following figure which shows the initial processing of a time-of-day interrupt OB if the start time is in the past, and if periodic activation has been set.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the call of time-of-day interrupt OBs, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

![Function of time-of-day interrupt OBs](images/63732931467_DV_resource.Stream@PNG-en-US.png)

### Conditions that effect the time-of-day interrupt OBs

As a time-of-day interrupt occurs only at specific intervals, certain conditions can affect the function of the associated OBs during execution of your program. The following table shows some of these conditions and describes how these affect the processing of the time-of-day interrupt OB.

| Symbol | Meaning |
| --- | --- |
| **Condition** | **Result** |
| Your program calls the "[CAN_TINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#can_tint-cancel-time-of-day-interrupt-s7-300-s7-400)" instruction and cancels a time-of-day interrupt. | The operating system deletes the start event (date and time) of the time-of-day interrupt. You have to reset and activate the start event if the OB is to be called again. |
| Your program tried to activate a time-of-day interrupt OB that was not loaded in the CPU at the time of activation. | The operating system then calls OB 85. If OB 85 has not been programmed (loaded to the CPU), then the CPU switches to STOP mode. |
| By synchronizing or correcting the system clock of the CPU you preset the time, and the start event, the date or the time for a time-of-day interrupt OB is skipped. | The operating system calls OB 80 and codes the number of the time-of-day interrupt OB and the start event information in OB 80.  The operating system then processes the time-of-day interrupt OB once, regardless of how often this OB actually should have been processed. The start event information of OB 80 shows the date and the time at which the time-of-day interrupt OB was initially skipped. |
| By synchronizing or correcting the system clock of the CPU you reset the time, and the start event, the date or the time for a time-of-day interrupt OB is repeated. | S7-400-CPUs: If the time-of-day interrupt OB was already activated before the time was reset, it is not called again for the times that have already passed.  S7-300-CPUs: The time-of-day interrupt OB is carried out. |
| The CPU carries out a warm restart or a cold restart. | Each time-of-day interrupt OB that was configured by an instruction then adopts the configuration again that you have specified.  If you have configured a time-of-day interrupt in such a way that the associated OB is started once and have set and activated it by means of configuration, then the OB will be called once after a warm restart or cold restart of the operating system as long as the configured starting time lies in the past (referring to the real time clock of the CPU). |
| A time-of-day interrupt OB is still being processed while the start event for the next interval is already occurring. | The operating system then calls OB 80. If OB 80 has not been programmed, the CPU changes to STOP mode.  Otherwise, the requested OB execution takes place after processing of OB 80 and the time-of-day interrupt OB is complete. |

### Local data of the time-of-day interrupt OB

The following table includes the temporary (TEMP) tags of a time-of-day interrupt OB. The default names of OB 10 are selected as tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB10_EV_CLASS | BYTE | Event class and identifiers: B#16#11: Interrupt is active |
| OB10_STRT_INFO | BYTE | B#16#11: Start request for OB 10  (B#16#12: Start request for OB 11)   :   :  (B#16#18: Start request for OB 17) |
| OB10_PRIORITY | BYTE | Assigned priority class; default value: 2 |
| OB10_OB_NUMBR | BYTE | OB number (10 to 17) |
| OB10_RESERVED_1 | BYTE | Reserved |
| OB10_RESERVED_2 | BYTE | Reserved |
| OB10_PERIOD_EXE | WORD | The OB is processed at the specified interval:  W#16#0000: Once  W#16#0201: Every minute  W#16#0401: Hourly  W#16#1001: Daily  W#16#1201: Weekly  W#16#1401: Monthly  W#16#1801: Yearly  W#16#2001: End of month |
| OB10_RESERVED_3 | INT | Reserved |
| OB10_RESERVED_4 | INT | Reserved |
| OB10_DATE_TIME | DATE_AND_TIME | Date and time when  the OB was called |

## Time-delay interrupt organization blocks (OB 20 to OB 23) (S7-300, S7-400)

### Description

S7 provides up to four OBs (OB 20 to OB 23) which are executed after a specified delay. Every time-delay interrupt OB is started by calling the "[SRT_DINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#srt_dint-start-time-delay-interrupt-s7-300-s7-400)" instruction. The delay time is an input parameter of the instruction.

When your program calls the "[SRT_DINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#srt_dint-start-time-delay-interrupt-s7-300-s7-400)" instruction, you provide the OB number, the delay time, and a user-specific identifier. After the specified delay, the associated OB starts. You can also cancel execution of a time-delay interrupt that has not yet started.

### Function of time-delay interrupt OBs

After the delay time has expired, whose value in milliseconds you have provided to the "[SRT_DINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#srt_dint-start-time-delay-interrupt-s7-300-s7-400)" instruction together with an OB number, the operating system will start the corresponding OB.

To use the time-delay interrupts, you must perform the following tasks:

- You must call the "[SRT_DINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#srt_dint-start-time-delay-interrupt-s7-300-s7-400)" instruction.
- You must download the time-delay interrupt OB to the CPU as part of your program.

Time-delay interrupt OBs are executed only when the CPU is in RUN mode. A warm restart or a cold restart clears any start events for a time-delay interrupt OB. If a time-delay interrupt has not yet been activated, you can use the "[CAN_DINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#can_dint-cancel-time-delay-interrupt-s7-300-s7-400)" instruction to cancel its execution.

The delay time is measured with a precision of 1 ms. A delay time can be immediately started after your sequence. You can query the status of a time-delay interrupt using the "[QRY_DINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#qry_dint-query-time-delay-interrupt-status-s7-300-s7-400)" instruction.

The operating system calls an asynchronous error OB if one of the following events occur:

- If the operating system attempts to start an OB that is not loaded and you have specified its number when calling the "[SRT_DINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#srt_dint-start-time-delay-interrupt-s7-300-s7-400)" instruction.
- If the next start event for a time-delay interrupt occurs before the corresponding time-delay interrupt OB has been completely executed.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the call of time-delay interrupt OBs, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

### Local data for time-delay interrupt OBs

The following table shows the temporary (TEMP) tags of a time-delay interrupt OB. The tag names are the default names of OB 20.

| Tag | Data type | Declaration | Description |
| --- | --- | --- | --- |
| OB20_EV_CLASS | BYTE | TEMP | Event class and identifiers:  B#16#11: Interrupt is active |
| OB20_STRT_INF | BYTE | TEMP | - B#16#21: Start request for OB 20 - (B#16#22: Start request for OB 21) - (B#16#23: Start request for OB 22) - (B#16#24: Start request for OB 23) |
| OB20_PRIORITY | BYTE | TEMP | Assigned priority class: Default values 3 (OB 20) to 6 (OB 23)  Default value for S7-1500 CPUs: 3 |
| OB20_OB_NUMBR | BYTE | TEMP | OB number (20 to 23) |
| OB20_RESERVED_1 | BYTE | TEMP | Reserved |
| OB20_RESERVED_2 | BYTE | TEMP | Reserved |
| OB20_SIGN | WORD | TEMP | User ID: Input parameter SIGN from the call of the "[SRT_DINT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#srt_dint-start-time-delay-interrupt-s7-300-s7-400)" instruction |
| OB20_DTIME | TIME | TEMP | Assigned delay time in ms |
| OB20_DATE_TIME | DATE_AND_TIME | TEMP | Date and time when the OB was called |

## Cyclic interrupt organization blocks (OB 30 to OB 38) (S7-300, S7-400)

### Description

S7 provides up to nine cyclic interrupt OBs (OB 30 to OB 38). You can use it to start programs after equidistant time phases. The following table shows the default values for the time frame and priority classes for the cyclic interrupt OBs.

| Cyclic interrupt OB | Default value for time frame | Default value for the priority class |
| --- | --- | --- |
| OB 30 | 5 s | 7 |
| OB 31 | 2 s | 8 |
| OB 32 | 1 s | 9 |
| OB 33 | 500 ms | 10 |
| OB 34 | 200 ms | 11 |
| OB 35 | 100 ms | 12 |
| OB 36 | 50 ms | 13 |
| OB 37 | 20 ms | 14 |
| OB 38 | 10 ms | 15 |

### Function of the cyclic interrupt OBs

The equidistant start times of the cyclic interrupt OBs are determined by the cycle clock and the phase offset.

> **Note**
>
> You must make sure that the run time of each cyclic interrupt OB is significantly shorter than its interval. If a cyclic interrupt OB has not been completely executed before it is due for execution again because the interval has expired, the time error OB (OB 80) is started. The cyclic interrupt that caused the error is executed later.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the call of the cyclic interrupt OBs, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

Refer to the specifications of your specific CPU for the range of the parameters cycle clock, priority class, and phase offset. You can change parameter settings through configuration.

### Local data for cyclic interrupt OBs

The following table shows the temporary (TEMP) tags of a cyclic interrupt OB.

| Tag | Data type | Description |
| --- | --- | --- |
| OB3x_EV_CLASS | BYTE | Event class and identifiers:  B#16#11: Interrupt is active |
| OB3x_STRT_INF | BYTE | - B#16#30: Special start request for a cyclic interrupt OB in the H-system (assigned special handling on changeover to the "Redundant" system state) - B#16#31: Start request for OB 30   …  - B#16#36: Start request for OB 35    …  - B#16#39: Start request for OB 38 - B#16#3A: Start request for cyclic interrupt OBs (OB 30 to OB 38) if the following conditions are met:   - Cycle time &lt; 32768 μs   - The cycle time or phase offset or both cannot be represented as an integer ms value. |
| OB3x_PRIORITY | BYTE | Assigned priority class; default values: 7 (OB 30) to 15 (OB 38)   Default values for S7-1500 CPUs: 8 to 14; 16 to 17 |
| OB3x_OB_NUMBR | BYTE | OB number (30 to 38) |
| OB3x_RESERVED_1 | BYTE | Reserved |
| OB3x_RESERVED_2 | BYTE | Reserved |
| OB3x_PHS_OFFSET | INT | for OBs 30 to 34 and 36 to 38:  - If OB3x_STRT_INF=B#16#3A: phase offset in μs - In all other cases: phase offset in ms |
| OB35_PHASE_OFFSET | WORD | for OB 35:  - If OB35_STRT_INF=B#16#3A: phase offset in μs - In all other cases: phase offset in ms |
| OB3x_RESERVED_3 | INT | Reserved |
| OB3x_EXC_FREQ | INT | - If OB3x_STRT_INF=B#16#3A: Cycle clock in μs - In all other cases: Cycle clock in milliseconds |
| OB3x_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called. |

## Hardware interrupt organization blocks (OB 40 to OB 47) (S7-300, S7-400)

### Description

S7 provides up to eight independent hardware interrupts each with its own OB.

Per configuration you specify which channels will trip a hardware interrupt,

- under which supplementary condition for each signal module.
- Which hardware interrupt OB is assigned to the individual groups of channels (as default, all hardware interrupts are processed by OB 40).

With CPs and FMs, you must use the appropriate software for the module for this.

You select the priority classes for the individual hardware interrupt OBs per configuration.

### Function of the hardware interrupt OBs

After the module triggers a hardware interrupt the operating system identifies the slot and determines the associated hardware interrupt OB. If this has a higher priority than the priority class active at the moment then it will be started. The channel-specific acknowledgment is sent after this hardware interrupt OB has been executed.

If another event that triggers a hardware interrupt occurs on the same module during the time between identification and acknowledgment of a hardware interrupt, the following applies:

- If the event occurs on the channel that previously triggered the hardware interrupt, then the associated interrupt is lost. The following figure illustrates the connection between a process signal and the execution of the associated hardware interrupt OB based on the example of a channel of a digital input module. The triggering event is the rising edge. The associated hardware interrupt OB is OB 40.

  ![Function of the hardware interrupt OBs](images/63732936203_DV_resource.Stream@PNG-en-US.png)
- If the event occurs on a different channel of the same module, then no hardware interrupt can be triggered at that moment. However, it is not lost, it is then triggered after the currently active hardware interrupt has been acknowledged.

If a hardware interrupt is triggered the OB of which is currently active on account of a hardware interrupt of another module, then the new request is registered and the OB is worked off at the specified time.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the call of the hardware interrupt OBs, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

You can use the "[WR_PARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_parm-write-module-data-record-s7-300-s7-400)", " [WR_DPARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_dparm-transfer-data-record-s7-300-s7-400)", and "[PARM_MOD](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#parm_mod-transfer-module-data-records-s7-300-s7-400)" instructions to assign the hardware interrupt parameters for a module.

### Local data of the hardware interrupt OBs

The following table shows the temporary (TEMP) tags of a hardware interrupt OB. The default names of OB 40 have been selected as tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB40_EV_CLASS | BYTE | Event class and identifiers:  B#16#11: Interrupt is active |
| OB40_STRT_INF | BYTE | - B#16#41: Interrupt via interrupt line 1 - B#16#42: Interrupt via interrupt line 2 (for S7-400 only) - B#16#43: Interrupt via interrupt line 3 (for S7-400 only) - B#16#44: Interrupt via interrupt line 4 (for S7-400 only) - B#16#45: WinAC: Interrupt triggered by PC  Note: The interrupt lines 1, ... 4 are assigned in the multicomputing mode of the CPUs 1, ... 4. |
| OB40_PRIORITY | BYTE | Assigned priority class: Default values:   16 (OB 40) to 23 (OB 47)   Default value for S7-1500 CPUs: 16 |
| OB40_OB_NUMBR | BYTE | OB number (40 to 47) |
| OB40_RESERVED_1 | BYTE | Reserved |
| OB40_IO_FLAG | BYTE | - B#16#54: Input module - B#16#55: Output module - B#16#00: Not available |
| OB40_MDL_ADDR | WORD | Logical start address of the module that has triggered the interrupt |
| OB40_POINT_ADDR | DWORD | - In the case of digital modules:  Bit array containing the inputs on the module that have triggered the hardware interrupt Refer to the respective module description for information on the assignment of bits of OB40_POINT_ADDR to the module channels. - In the case of analog modules:bit field with the information as to which channel has exceeded which thresholds (refer to the module description for the precise structure). - In the case of CPs or IMs: Interrupt status of the module (not user-relevant) |
| OB40_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

> **Note**
>
> If you are using a DPV1-capable CPU, you can use the "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" instruction to obtain additional information about the interrupt that goes beyond the start information of the OB. This also applies if the DP master is operated in S7 compatible mode.

## Status interrupt OB (OB 55) (S7-300, S7-400)

### Description

The CPU operating system calls OB 55 if a status interrupt was triggered by the slot of a DPV1 slave or of an IO device. This might be the case if a component (module or rack) of a DPV1 slave or of an IO device changes its operating mode, for example from RUN to STOP. For precise information on events that trigger a status interrupt, refer to the documentation provided by the manufacturer of the DPV1 slave or the IO device.

> **Note**
>
> If S7-400 CPUs or S7-400 PROFIBUS CPs are set to the "S7 compatible" DP mode, no status interrupt OB (OB 55) can be used.

### Local data of the status interrupt OB

The following table shows the temporary (TEMP) tags of the status interrupt OB. The tag names are the default names of OB 55.

| Tag | Data type | Description |
| --- | --- | --- |
| OB55_EV_CLASS | BYTE | Event class and identifiers:  B#16#11 (incoming event) |
| OB55_STRT_INF | BYTE | - B#16#55: Status interrupt for DP - B#16#58: Status interrupt for PROFINET IO |
| OB55_PRIORITY | BYTE | Assigned priority class, default value: 2 or 4 (for S7-1500 CPUs) |
| OB55_OB_NUMBR | BYTE | OB number (55) |
| OB55_RESERVED_1 | BYTE | Reserved |
| OB55_IO_FLAG | BYTE | Input module: B#16#54  Output module: B#16#55 |
| OB55_MDL_ADDR | WORD | Logical start address of the interrupt triggering component (module) |
| OB55_LEN | BYTE | Length of the data block supplied by the interrupt |
| OB55_TYPE | BYTE | ID for interrupt type "status interrupt" |
| OB55_SLOT | BYTE | Slot number of the component triggering the interrupt (module) |
| OB55_SPEC | BYTE | Specifier:  - Bit 0 to 1: Interrupt specifier - Bit 2: Add_Ack - Bit 3 to 7: Seq. no. |
| OB55_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

> **Note**
>
> The meaning of OB55_LEN, OB55_TYPE, OB55_SLOT, OB55_SPEC indicated in the table above applies only to a status interrupt for DP. If the status interrupt is for PROFINET IO, you must organize the local tags as indicated in the next table.

> **Note**
>
> You can obtain complete supplemental information on the interrupt from the telegram by calling the "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" instruction within OB 55.

If you want to program OB55 dependent on start events, we recommend that you organize the local tags as follows:

| Tag | Data type |
| --- | --- |
| OB55_EV_CLASS | BYTE |
| OB55_STRT_INF | BYTE |
| OB55_PRIORITY | BYTE |
| OB55_OB_NUMBR | BYTE |
| OB55_RESERVED_1 | BYTE |
| OB55_IO_FLAG | BYTE |
| OB55_MDL_ADR | WORD |
| OB55_Z2 | WORD |
| OB55_Z3 | WORD |
| OB55_DATE_TIME | DATE_AND_TIME |

Depending on the start event, the tags OB55_Z2 and OB55_Z3 contain different information. This is explained in greater detail below.

### Meaning of OB55_Z2

| OB55_STRT_INF | Meaning of OB55_Z2 |
| --- | --- |
| B#16#55 | - Low byte: ID for interrupt type "status interrupt" - High byte: Length of the data block supplied by the interrupt |
| B#16#58 | ID for interrupt type:  - W#16#0005: Status interrupt |

### Meaning of OB55_Z3

| OB55_STRT_INF | Meaning of OB55_Z3 |
| --- | --- |
| B#16#55 | - Low byte: Specifier   - Bits 0 to 1: Interrupt specifier   - Bit 2: Add_Ack   - Bits 3 to 7: Sequence number - High byte: Slot of component triggering the interrupt (module) |
| B#16#58 | Interrupt specifier  - Bits 0 to 10: Sequence number (value range 0 to 2047) - Bits 11 to 15: 0 |

## Update interrupt OB (OB 56) (S7-300, S7-400)

### Description

The CPU operating system calls OB 56 if an update interrupt was triggered by the slot of a DPV1 slave or of an IO device. This can be the case if you have changed the parameters for the slot of a DPV1 slave or of an IO device (via local or remote access). For precise information on events that trigger an update interrupt, refer to the documentation provided by the manufacturer of the DPV1 slave or the IO device.

> **Note**
>
> If S7-400 CPUs or S7-400 PROFIBUS CPs are set to the "S7 compatible" DP mode, no update interrupt OB (OB 56) can be used.

### Local data of the update interrupt OB

The following table shows the temporary (TEMP) tags of the update interrupt OB. The tag names are the default names of OB 56.

| Tag | Data type | Description |
| --- | --- | --- |
| OB56_EV_CLASS | BYTE | Event class and identifiers:  B#16#11 (incoming event) |
| OB56_STRT_INF | BYTE | - B#16#56: Update interrupt for DP - B#16#59: Update interrupt for PROFINET IO |
| OB56_PRIORITY | BYTE | Assigned priority class, default value: 2 or 4 (for S7-1500 CPUs) |
| OB56_OB_NUMBR | BYTE | OB number (56) |
| OB56_RESERVED_1 | BYTE | Reserved |
| OB56_IO_FLAG | BYTE | Input module: B#16#54  Output module: B#16#55 |
| OB56_MDL_ADDR | WORD | Logical start address of the interrupt triggering component (module) |
| OB56_LEN | BYTE | Length of the data block supplied by the interrupt |
| OB56_TYPE | BYTE | ID for the interrupt type "Update interrupt" |
| OB56_SLOT | BYTE | Slot number of the component triggering the interrupt (module) |
| OB56_SPEC | BYTE | Specifier:  - Bit 0 to 1: Interrupt specifier - Bit 2: Add_Ack - Bit 3 to 7: Seq. no. |
| OB56_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

> **Note**
>
> The meaning of OB56_LEN, OB56_TYPE, OB56_SLOT, OB56_SPEC indicated in the table above applies only to an update interrupt for DP. If the update interrupt is for PROFINET IO, you must organize the local tags as indicated in the next table.

> **Note**
>
> You can obtain complete supplemental information on the interrupt from the telegram by calling the "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" instruction within OB 56.

If you want to program OB 56 dependent on start events, we recommend that you organize the local tags as follows:

| Tag | Data type |
| --- | --- |
| OB56_EV_CLASS | BYTE |
| OB56_STRT_INF | BYTE |
| OB56_PRIORITY | BYTE |
| OB56_OB_NUMBR | BYTE |
| OB56_RESERVED_1 | BYTE |
| OB56_IO_FLAG | BYTE |
| OB56_MDL_ADR | WORD |
| OB56_Z2 | WORD |
| OB56_Z3 | WORD |
| OB56_DATE_TIME | DATE_AND_TIME |

Depending on the start event, the tags OB56_Z2 and OB56_Z3 contain different information. This is explained in greater detail below.

### Meaning of OB56_Z2

| OB56_STRT_INF | Meaning of OB56_Z2 |
| --- | --- |
| B#16#56 | - Low byte: ID for the interrupt type "Update interrupt" - High byte: Length of the data block supplied by the interrupt |
| B#16#59 | ID for the interrupt type  - W#16#0006: Update interrupt - W#16#001E: Upload-and-Retrieval-Alarm   In the Siemens Industry Online Support you can find the function block IPARSERV which serves as a application example that you can use to save additional configuration data when required by a PROFINET device or a module used within it to a DB and restore it following maintenance or repair. A PROFINET device sends a Upload-and-Retrieval-Alarm to the IO controller and uses the Update-Alarm OB for this. [https://support.industry.siemens.com/cs/ww/en/view/45841087](https://support.industry.siemens.com/cs/ww/en/view/45841087) |

### Meaning of OB56_Z3

| OB56_STRT_INF | Meaning of OB56_Z3 |
| --- | --- |
| B#16#56 | - Low byte: Specifier   - Bits 0 to 1: Interrupt specifier   - Bit 2: Add_Ack   - Bits 3 to 7: Sequence number - High byte: Slot of component triggering the interrupt (module) |
| B#16#59 | Interrupt specifier:  - Bits 0 to 10: Sequence number (value range 0 to 2047) - Bits 11 to 15: 0 |

## OB for manufacturer-specific alarms (OB 57) (S7-300, S7-400)

### Description

The CPU operating system calls OB 57 if a manufacturer-specific interrupt was triggered by the slot of a DPV1 slave or of an IO device.

> **Note**
>
> If S7-400 CPUs or S7-400 PROFIBUS CPs are set to the "S7 compatible" DP mode, no manufacturer-specific interrupt OB (OB 57) can be used.

### Local data of the manufacturer-specific interrupt OB

The table below contains the temporary (TEMP) tags of the manufacturer-specific interrupt OB. Selected tag names are the default names of OB 57.

| Tag | Data type | Description |
| --- | --- | --- |
| OB57_EV_CLASS | BYTE | Event class and identifiers:  B#16#11 (incoming event) |
| OB57_STRT_INF | BYTE | - B#16#57: Manufacturer interrupt for DP - B#16#5A: Manufacturer interrupt for PROFINET IO - B#16#5B: IO: Profile-specific interrupt |
| OB57_PRIORITY | BYTE | Assigned priority class, default value: 2 or 4 (for S7-1500 CPUs) |
| OB57_OB_NUMBR | BYTE | OB number (57) |
| OB57_RESERVED_1 | BYTE | Reserved |
| OB57_IO_FLAG | BYTE | Input module: B#16#54  Output module: B#16#55 |
| OB57_MDL_ADDR | WORD | Logical start address of the interrupt triggering component (module) |
| OB57_LEN | BYTE | Length of the data block supplied by the interrupt |
| OB57_TYPE | BYTE | ID for the interrupt type "Vendor-specific interrupt" |
| OB57_SLOT | BYTE | Slot number of the component triggering the interrupt (module) |
| OB57_SPEC | BYTE | Specifier:  - Bit 0 to 1: Interrupt specifier - Bit 2: Add_Ack - Bit 3 to 7: Seq. no. |
| OB57_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

> **Note**
>
> The meaning of OB57_LEN, OB57_TYPE, OB57_SLOT, OB57_SPEC indicated in the table above applies only to a manufacturer-specific interrupt for DP. If the manufacturer-specific interrupt is for PROFINET IO, you must organize the local tags as indicated in the next table.

> **Note**
>
> You can obtain complete supplemental information on the interrupt from the telegram by calling the "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" instruction within OB 57.

If you want to program OB 57 dependent on start events, we recommend that you organize the local tags as follows:

| Tag | Data type |
| --- | --- |
| OB57_EV_CLASS | BYTE |
| OB57_STRT_INF | BYTE |
| OB57_PRIORITY | BYTE |
| OB57_OB_NUMBR | BYTE |
| OB57_RESERVED_1 | BYTE |
| OB57_IO_FLAG | BYTE |
| OB57_MDL_ADR | WORD |
| OB57_Z2 | WORD |
| OB57_Z3 | WORD |
| OB57_DATE_TIME | DATE_AND_TIME |

Depending on the start event, the tags OB57_Z2 and OB57_Z3 contain different information. This is explained in greater detail below.

### Meaning of OB57_Z2

| OB57_STRT_INF | Meaning of OB57_Z2 |
| --- | --- |
| B#16#57 | - Low byte: ID for the interrupt type "Vendor-specific interrupt" - High byte: Length of the data block supplied by the interrupt |
| B#16#5A | ID for interrupt type:  - W#16#0020 to 007F: Manufacturer-specific interrupt |

### Meaning of OB57_Z3

| OB57_STRT_INF | Meaning of OB57_Z3 |
| --- | --- |
| B#16#57 | - Low byte: Specifier   - Bits 0 to 1: Interrupt specifier   - Bit 2: Add_Ack   - Bits 3 to 7: Sequence number - High byte: Slot of component triggering the interrupt (module) |
| B#16#5A | Interrupt specifier  - Bits 0 to 10: Sequence number (value range 0 to 2047) - Bits 11 to 15: 0 |

## Synchronous cycle interrupt OBs (OB 61 to OB 64) (S7-300, S7-400)

### Description

Isochronous mode interrupts give you the option of starting programs isochronously with the DP cycle or PN send clock. OB 6y, 1 &lt;= y &lt;= 4, serves as an interface OB to the isochronous mode interrupt TSAL y. You can set the priority for OB 61 to 64 between 0 (OB deselected) and from 2 to 26.

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Direct access**  In the case of direct access with L or T commands (e.g., L PIB, T PQB) or with use of the "[DPRD_DAT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" and "[DPWR_DAT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)" instructions, avoid accessing I/O areas to which process image partitions with OB6x connection (isochronous mode interrupts) are assigned. |  |

### Local data for the isochronous mode interrupt OB

The following table describes the temporary (TEMP) tags of the isochronous mode interrupt OB. The default names of OB 61 have been selected as tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB61_EV_CLASS | BYTE | Event class and identifiers:  B#16#11: Interrupt is active |
| OB61_STRT_INF | BYTE | B#16#64: Start request for OB 61  : B#16#67: Start request for OB 64 |
| OB61_PRIORITY | BYTE | Assigned priority class; default value: 25 or 21 (for S7-1500 CPUs) |
| OB61_OB_NUMBR | BYTE | OB number: 61 ... 64 |
| OB61_RESERVED_1 | BYTE | Reserved |
| OB61_RESERVED_2 | BYTE | Reserved |
| OB61_GC_VIOL | BOOL | GC violation with PROFIBUS DP |
| OB61_FIRST | BOOL | First use after startup or stop status |
| OB61_MISSED_EXEC | BYTE | Number of failed starts of OB 61 since last execution of OB 61 |
| OB61_DP_ID | BYTE | DP master system ID of isochronous DP master system (1 to 32) or PROFINET IO System ID of isochronous PNIO system (100 to 115) |
| OB61_RESERVED_3 | BYTE | Reserved |
| OB61_RESERVED_4 | WORD | Reserved |
| OB61_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

## Time error OB (OB 80) (S7-300, S7-400)

### Description

The CPU operating system calls OB 80 whenever an error occurs while executing an OB, such errors include:

- Exceeding the cycle time
- Acknowledgement error in the execution of an OB
- Setting time forward (time skip) to start an OB

If for example a start event occurs for a cyclic interrupt OB, before the previous execution of the same OB has been completed, then the operating system calls OB 80.

If OB 80 has not been programmed, the CPU changes to STOP mode.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the call of the time error OB, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

> **Note**
>
> If OB 80 is called twice during the same cycle due to the cycle time being exceeded, then the CPU changes to STOP mode. You can prevent this by calling the "RE_TRIGR" instruction at a suitable point.

### Note on use of "Report System Errors"

"Report System Errors" delays the processing of interrupts that occur during its execution time.

If the **Execution time of "****Report System Errors****" &gt; 50% of cycle time** condition is met, this effect is greater (here, the execution time of "Report System Errors" is understood to mean the sum of all processing times of "Report System Errors" within the cycle time). This can lead to the call of the time error OB and possibly to CPU STOP (if the time error OB is not loaded).

The following measures are available to prevent this:

- If you are using isochronous mode interrupt OBs (OB 61 to OB 64), you must ensure that these are called less frequently per time unit than before. You achieve this by increasing the associated "Application cycle factor" parameter for each isochronous mode interrupt OB.
- Increase the ratio (cycle time - execution time of "Report System Errors")/( execution time of "Report System Errors"). The following two options are available for this:

  - If you call "Report System Errors" in cyclic interrupt OBs (OB 30 to OB 38), then increase the cycle clocks for the associated OBs.
  - In OB 1, increase the execution time of the program section independent of "Report System Errors". You achieve this, for example, by using the "WAIT" instruction.

### Local data for the time error OB

The following table lists the temporary (TEMP) tags of the time error OB. The default names of OB 80 have been selected as tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB80_EV_CLASS | BYTE | Event class and identifiers: B#16#35 |
| OB80_FLT_ID | BYTE | Error code (possible values: B#16#01, B#16#02, B#16#05, B#16#06, B#16#07, B#16#08, B#16#09, B#16#0A, B#16#0B) |
| OB80_PRIORITY | BYTE | Priority class: OB 80 runs with priority class 26 in RUN mode, and in the event of an overflow of the OB request buffer with priority class 28  For S7-1500 CPUs: Priority 22 |
| OB80_OB_NUMBR | BYTE | OB number (80) |
| OB80_RESERVED_1 | BYTE | Reserved |
| OB80_RESERVED_2 | BYTE | Reserved |
| OB80_ERROR_INFO | WORD | Error information: Depends on the error code |
| OB80_ERR_EV_CLASS | BYTE | Class of the event that caused the error |
| OB80_ERR_EV_NUM | BYTE | Number of the event that caused the error |
| OB80_OB_PRIORITY | BYTE | Error information: Depends on the error code |
| OB80_OB_NUM | BYTE | Error information: Depends on the error code |
| OB80_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

The error code-dependent tags have the following meaning:

| Error code | Tag | Bit | Meaning |
| --- | --- | --- | --- |
| B#16#01 |  |  | Cycle time exceeded |
|  | OB80_ERROR_INFO |  | Runtime of last scan cycle (ms) |
|  | OB80_ERR_EV_CLASS |  | Class of the event that triggered the interrupt |
|  | OB80_ERR_EV_NUM |  | Number of the event that triggered the interrupt |
|  | OB80_OB_PRIORITY |  | Priority class of the OB that was being processed when the error occurred |
|  | OB80_OB_NUM |  | Number of the OB that was active when the error occurred |
| B#16#02 |  |  | The requested OB is still being processed. |
|  | OB80_ERROR_INFO |  | The corresponding temporary tag of the requested OB. This tag is determined by OB80_ERR_EV_CLASS and OB80_ERR_EV_NUM. |
|  | OB80_ERR_EV_CLASS |  | Class of the event that triggered the interrupt |
|  | OB80_ERR_EV_NUM |  | Number of the event that triggered the interrupt |
|  | OB80_OB_PRIORITY |  | Priority class of the OB that caused the error (e.g.: "7" for OB 30/priority class 7, which should have been started but was not able to be started) |
|  | OB80_OB_NUM |  | Number of the OB that caused the error (e.g.: "30" for OB 30, which should have been started but was not able to be started) |
| B#16#05 |  |  | Expired time interrupt due to time jump |
|  | OB80_ERROR_INFO | Bit 0 set | For the time interrupt 0, the starting time lies in the past |
|  |  | ... |  |
|  |  | Bit 7 set | For the time interrupt 7, the starting time lies in the past |
|  |  | Bit 8 to 15 | Not used |
|  | OB80_ERR_EV_CLASS |  | Not used |
|  | OB80_ERR_EV_NUM |  | Not used |
|  | OB80_OB_PRIORITY |  | Not used |
|  | OB80_OB_NUM |  | Not used |
| B#16#06 | Same as for error code B#16#05 |  | Expired time interrupt upon re-entry into RUN after HOLD |
| B#16#07 | Same as for error code B#16#02 |  | Overflow of the OB request buffer for the current priority class (each OB start request for a priority class is entered in the associated OB request buffer; the entry is deleted again after the end of the OB. If a priority class has more OB start requests than the maximum possible number of entries in the associated OB request buffer, OB 80 is called with error code B#16#07.) |
| B#16#08 | Same as for error code B#16#02 |  | Isochronous mode interrupt - time error |
| B#16#09 | Same as for error code B#16#02 |  | Interrupt loss due to high interrupt load |
| B#16#0A |  |  | Resume RUN after CiR |
|  | OB80_ERROR_INFO |  | CiR synchronization time in ms |
| B#16#0B |  |  | Technology synchronization interrupt - time error |
|  | OB80_ERR_EV_NUM |  | Number of the event that triggered the interrupt: W#16#116A |
|  | OB80_OB_PRIORITY |  | Priority class of the OB that was being processed when the error occurred |
|  | OB80_OB_NUM |  | Number of the OB that was active when the error occurred: 65 |
| B#16#0C |  |  | (only for S7-1500 R/H CPUs) cycle time exceeded for the second time |
|  | OB80_ERROR_INFO |  | Runtime of last scan cycle (ms) |
|  | OB80_ERR_EV_CLASS |  | Class of the event that triggered the interrupt |
|  | OB80_ERR_EV_NUM |  | Number of the event that triggered the interrupt |
|  | OB80_OB_PRIORITY |  | Priority class of the OB that was being processed when the error occurred |
|  | OB80_OB_NUM |  | Number of the OB that was active when the error occurred |

## Power supply error organization block (OB 81) (S7-300, S7-400)

### Description

The CPU operating system calls OB 81 whenever an event occurs that is triggered by an error or fault related to the power supply (only on an S7-400) or the back-up battery (for either an incoming or outgoing event).

In S7-400, OB 81 is only called in the event of a battery fault if the battery test function has been activated with the BATT.INDIC switch.

The CPU does not change to STOP mode if OB 81 is not programmed.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the call of the power supply error OB, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

### Local data for the power supply error OB

The following table lists the temporary (TEMP) tags of the power supply error OB. The default names of OB 81 have been selected as tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB81_EV_CLASS | BYTE | Event class and identifiers:  - B#16#38: Outgoing event - B#16#39: Incoming event |
| OB81_FLT_ID | BYTE | Error code (possible values: B#16#21, B#16#22, B#16#23, B#16#25, B#16#26, B#16#27, B#16#31, B#16#32, B#16#33) |
| OB81_PRIORITY | BYTE | Priority class: Can be set during configuration  e.g., values 2 to 26 can be set for RUN mode. |
| OB81_OB_NUMBR | BYTE | OB number (81) |
| OB81_RESERVED_1 | BYTE | Reserved |
| OB81_RESERVED_2 | BYTE | Reserved |
| OB81_RACK_CPU | WORD | - Bits 0 to 7: B#16#00 - Bits 8 to 15:   - For a standard CPU: B#16#00   - For a H-CPU: Bits 8 to 10: Rack no., bit 11: 0=Reserve CPU, 1=Master CPU, bits 12 to 15: 1111 |
| OB81_RESERVED_3 | BYTE | Relevant only for error codes B#16#31, B#16#32 and B#16#33 |
| OB81_RESERVED_4 | BYTE | Relevant only for error codes B#16#31, B#16#32 and B#16#33 |
| OB81_RESERVED_5 | BYTE | Relevant only for error codes B#16#31, B#16#32 and B#16#33 |
| OB81_RESERVED_6 | BYTE | Relevant only for error codes B#16#31, B#16#32 and B#16#33 |
| OB81_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

The tags OB81_RESERVED_i, 3 ≤ i ≤ 6 indicate the expansion racks on which the battery backup (error code B#16#31), the back-up voltage (error code B#16#32) or the 24-V power supply (error code B#16#33) has failed or returned. The following table shows which bit is assigned to which expansion rack in the tags OB81_RESERVED_i, 3 ≤ i ≤ 6.

|  | OB81_RESERVED_6 | OB81_RESERVED_5 | OB81_RESERVED_4 | OB81_RESERVED_3 |
| --- | --- | --- | --- | --- |
| Bit 0 | Reserved | 8. expansion rack | 16. expansion rack | Reserved |
| Bit 1 | 1. expansion rack | 9. expansion rack | 17. expansion rack | Reserved |
| Bit 2 | 2. expansion rack | 10. expansion rack | 18. expansion rack | Reserved |
| Bit 3 | 3. expansion rack | 11. expansion rack | 19. expansion rack | Reserved |
| Bit 4 | 4. expansion rack | 12. expansion rack | 20. expansion rack | Reserved |
| Bit 5 | 5. expansion rack | 13. expansion rack | 21. expansion rack | Reserved |
| Bit 6 | 6. expansion rack | 14. expansion rack | Reserved | Reserved |
| Bit 7 | 7. expansion rack | 15. expansion rack | Reserved | Reserved |

The bits in the tags OB81_RESERVED_i have the following meaning (for the expansion rack concerned):

When the event occurs, the expansion racks are marked (the corresponding bits are set) on which at least one battery or back-up voltage or the 24 V power supply has failed. Expansion racks on which at least one battery or back-up voltage or the 24 V power supply failed earlier are no longer indicated. When the event is eliminated and the backup is restored on at least one expansion rack, this is signaled (the corresponding bits are set).

The following table shows the event that started OB81:

| OB81_EV_CLASS | OB81_FLT_ID | Meaning |
| --- | --- | --- |
| B#16#39/B#16#38 | B#16#21 | At least one back-up battery of the central rack is exhausted/problem eliminated (BATTF)   **Note:** The incoming event occurs only if one of the two batteries (in the case of redundant buffer batteries) fails. If the other battery then fails, the event does not occur again. |
| B#16#39/B#16#38 | B#16#22 | Buffer voltage in the central device is missing / remedied (BAF). |
| B#16#39/B#16#38 | B#16#23 | Failure of the 24-V supply in the central device / remedied. |
| B#16#39/B#16#38 | B#16#25 | At least one buffer battery in at least one redundant central device is empty / remedied (BATTF). |
| B#16#39/B#16#38 | B#16#26 | Buffer voltage in at least one redundant central device is missing / remedied (BAF). |
| B#16#39/B#16#38 | B#16#27 | Failure of the 24-V supply in at least one redundant central device / remedied. |
| B#16#39/B#16#38 | B#16#31 | At least one buffer battery in at least one expansion unit is empty / remedied (BATTF). |
| B#16#39/B#16#38 | B#16#32 | Buffer voltage in at least one expansion unit is missing / remedied (BAF). |
| B#16#39/B#16#38 | B#16#33 | Failure of the 24-V supply in at least one expansion unit / remedied. |

### Sample program for OB 81

A sample STL program will show you how you can read the error code in OB 81.

The program is structured as follows:

The error code in OB 81 (OB81_FLT_ID) is read and compared with the identifier for the "At least one back-up battery of the central rack is exhausted" (B#16#21) and "Back-up voltage in the central rack is not present" (B#16#22) events.

If the error code corresponds to one of the indicated events, the program jumps to the BF label. Otherwise, the block is terminated.

Starting at the BF label, the program sets the Battery error tag if the event is an incoming event. If the event is an outgoing event, the program resets this tag.

|  |  |
| --- | --- |
| L B#16#21 | //Identifier for the "At least one back-up battery of the central rack is exhausted" event |
| L #OB81_FLT_ID | //Error code in OB 81 |
| ==I | //If the same, |
| JC BF | //then jump to BF |
| L B#16#22 | //Identifier for the "Back-up voltage in central rack is not present" event |
| ==I | //If the same as the error code in OB 81, |
| JC BF | //then jump to BF |
| BEU | //No alarm about battery error |
|  |  |
| BF: L B#16#39 | //Identifier for incoming event |
| L #OB81_EV_CLASS | //Event class and identifiers for OB 81 call |
| ==I | //If the same, |
| S Battery error | //then set the battery error (tag from the tag table) |
| L B#16#38 | //Identifier for outgoing event |
| ==I | //If the same as the event class and identifiers for the OB 81 call, |
| R Battery error | //then reset the battery error (tag from the tag table) |

## Diagnostic interrupt OB (OB 82) (S7-300, S7-400)

### Description

If a module with diagnostics capability for which you have enabled the diagnostic interrupt detects a change in its diagnostic state, it sends a diagnostic interrupt request to the CPU:

- There is a problem or a component requires maintenance or both (incoming event).
- There is no problem and no further components require maintenance (outgoing event).

The operating system then calls OB 82.

The local tags of OB 82 contain the logical start address as well as four bytes of diagnostics data of the defective module (see the following table).

If OB 82 has not been programmed, the CPU changes to STOP mode.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the call of the diagnostic interrupt OB, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

> **Note**
>
> For PROFINET IO controllers, you can specify during configuration whether or not communication interrupts are to trigger a call of the diagnostic interrupt OB. These interrupts involve diagnostic events of the PROFINET interface.
>
> Default setting: these events do not trigger an OB 82 call.

### Local data for diagnostic interrupt OB

The following table lists the temporary (TEMP) tags of the diagnostic interrupt OB. The default names of OB 82 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB82_EV_CLASS | BYTE | Event class and identifiers:  - B#16#38: outgoing event: module error-free (all errors have been corrected.) - B#16#39: incoming event: module will be or remain faulty (with change in the number of its pending errors) |
| OB82_FLT_ID | BYTE | Error code (B#16#42) |
| OB82_PRIORITY | BYTE | - Priority class; can be set via configuration - For S7-1500 CPUs: priority, default value: 5 |
| OB82_OB_NUMBR | BYTE | OB number (82) |
| OB82_RESERVED_1 | BYTE | Reserved |
| OB82_IO_FLAG | BYTE | - For S7-300/S7-400:   - Input module: B#16#54   - Output module: B#16#55 - For S7-1500: zero |
| OB82_MDL_ADDR | WORD | - For S7-300/S7-400: Logical start address of the module where the fault occurred - For S7-1500: Hardware identifier of the hardware object that triggered the diagnostic interrupt |
| OB82_MDL_DEFECT <sup>1)</sup> | BOOL | Module is defective |
| OB82_INT_FAULT | BOOL | Internal fault |
| OB82_EXT_FAULT | BOOL | External fault |
| OB82_PNT_INFO | BOOL | Channel fault |
| OB82_EXT_VOLTAGE | BOOL | External auxiliary voltage missing |
| OB82_FLD_CONNCTR | BOOL | Front panel connector not plugged in |
| OB82_NO_CONFIG | BOOL | Module parameters not assigned |
| OB82_CONFIG_ERR | BOOL | Incorrect parameters on module |
| OB82_MDL_TYPE | BYTE | - Bit 0 to 3: Module class - Bit 4: Channel information exists - Bit 5: User information exists - Bit 6: Diagnostic interrupt from substitute - Bit 7:    - For S7-300/S7-400: Maintenance required   - For S7-1500: Maintenance demanded |
| OB82_SUB_MDL_ERR | BOOL | Application module is missing or has an error |
| OB82_COMM_FAULT | BOOL | Communication problem |
| OB82_MDL_STOP | BOOL | Operating mode  (0: RUN, 1: STOP) |
| OB82_WTCH_DOG_FLT | BOOL | Watchdog timer responded |
| OB82_INT_PS_FLT | BOOL | Internal power supply failed |
| OB82_PRIM_BATT_FLT | BOOL | Battery exhausted |
| OB82_BCKUP_BATT_FLT | BOOL | Entire backup failed |
| OB82_RESERVED_2 | BOOL | - For S7-300/S7-400: Maintenance demanded - For S7-1500: Maintenance required |
| OB82_RACK_FLT | BOOL | Expansion rack failure |
| OB82_PROC_FLT | BOOL | Processor failure |
| OB82_EPROM_FLT | BOOL | EPROM fault |
| OB82_RAM_FLT | BOOL | RAM fault |
| OB82_ADU_FLT | BOOL | ADC/DAC error |
| OB82_FUSE_FLT | BOOL | Fuse tripped |
| OB82_HW_INTR_FLT | BOOL | Hardware interrupt lost |
| OB82_RESERVED_3 | BOOL | Reserved |
| OB82_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |
| <sup>1)</sup> With S7-1500-CPUs, the variables OB82_MDL_DEFECT to OB82_RESERVED_3 contain at events of a PROFIBUS device the data record 0 in the form as it is generated in the PROFIBUS slave. |  |  |

> **Note**
>
> If you are using a DPV1-capable CPU, you can use the "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" instruction to obtain additional information about the interrupt that goes beyond the start information of the OB. This also applies if the DP master is operated in S7 compatible mode.

### Programming OB 82

You must add OB 82 to the blocks of your CPU. Write the program that is to be executed in OB 82 to the generated block, and load the block to the CPU as part of your user program.

You can use OB 82, for example, as follows:

- You evaluate the start information in OB 82.
- You carry out detailed diagnostics of the error that occurred.

If a diagnostic interrupt is triggered, the faulty module automatically enters 4 bytes of diagnostics data and their start address in the start information of the diagnostic interrupt OB and in the diagnostics buffer. This provides you with information about when an error occurred and on which module.

With a suitable program in OB 82, you can evaluate additional diagnostics data for the faulty module (which channel the error occurred on, which error has occurred). You can use the "[RDSYSST](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rdsysst-read-system-status-list-s7-300-s7-400)" instruction to read out module diagnostics data and the "[WR_USRMSG](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400)" instruction to enter this information in the diagnostics buffer. You can also send a user-defined diagnostics alarm to a logged-on monitoring device.

## Insert/remove module interrupt organization block (OB 83) (S7-300, S7-400)

### Description

The CPU operating system calls OB 83 after a configured module has been pulled or plugged in.

If you have not programmed OB 83, the CPU changes to STOP mode.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the pull/plug interrupt OB call, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

### Removing and inserting modules

Every removal and insertion of a configured module (not allowed: power supply modules, CPUs, adapter casings and IMs) in RUN, STOP, or STARTUP mode results in a pull/plug interrupt. This interrupt causes an entry in the diagnostics buffer and in the system status list for the CPU involved. The pull/plug OB is also started if the CPU is in RUN mode. If this OB has not been programmed, the CPU changes to STOP mode.

The removal and insertion of S7-400 modules is monitored within the system every second. To enable the CPU to detect the removal and insertion of an S7-400 module, a minimum time interval of two seconds must elapse between removal and insertion. This minimum time is slightly higher for other modules.

If you remove a configured module in RUN mode, OB 83 is started. An access error may be detected first if the module is accessed directly or when the process image is updated.

If you insert a module in a configured slot in RUN mode, the operating system checks whether the type of the module inserted matches the configuration. OB 83 is then started and parameters are assigned if the module types match.

### Points to note about S7-300, ET 200S and ET 200Pro

- The removal and insertion of central IO devices is not permitted in S7-300.
- With S7-300 CPUs, there is a pull/plug interrupt only for 31x PN/DP CPUs, and then only for PROFINET IO components.
- On an ET 200Pro, for example with an IM 154-4-8 CPU, there is a pull/plug interrupt only for central IO devices.
- On an ET 200S, for example with an IM151-8 PN/DP CPU, there is a pull/plug interrupt only for central IO devices.

### Local data for pull/plug OB

The following table lists the temporary (TEMP) tags of the pull/plug OB. The default names of OB 83 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB83_EV_CLASS | BYTE | Event class and identifiers:  - B#16#32: End of module parameter reassignment - B#16#33: Start of module parameter reassignment - B#16#38: Module inserted - B#16#39: Module removed or not responding, or end of parameter reassignment |
| OB83_FLT_ID | BYTE | Error code (possible values: B#16#51, B#16#54, B#16#55, B#16#56, B#16#57, B#16#58, B#16#61, B#16#63, B#16#64, B#16#65, B#16#66, B#16#67, B#16#68, B#16#71, B#16#72, B#16#73) |
| OB83_PRIORITY | BYTE | Priority class; can be set via configuration  For S71500 CPUs: priority, default value: 6 |
| OB83_OB_NUMBR | BYTE | OB number (83) |
| OB83_RESERVED_1 | BYTE | Identification of module or submodule/interface module |
| OB83_MDL_TD | BYTE | Range:  - B#16#54: I/O range of inputs (PI) - B#16#55: I/O range of outputs (PQ) |
| OB83_MDL_ADDR | WORD | - Central or distributed PROFIBUS DP: Logical start address of the module affected. If it is a mixed module, it is the smallest logical address used in the module. If the I and O addresses in the mixed block are equal, the logical start address is the one that receives the event identifier. - Distributed PROFINET IO: Logical start address of the module/submodule |
| OB83_RACK_NUM | INT | - If OB83_RESERVED_1 =B#16#A0: number of the submodule/interface submodule (low byte) - If OB83_RESERVED_1 = B#16#C4:   - central: rack number   - distributed PROFIBUS DP: number of the DP station (low byte) and DP master system ID (high byte)   - Distributed PROFINET IO: physical address: identifier bit (bit 15, 1 = PROFINET IO), IO system ID (bits 11 to 14) and device number (bits 0 to 10) |
| OB83_MDL_TYPE | WORD | For S7-300/S7-400:  - Central or distributed PROFIBUS DP: Module type of the module affected (X: not relevant for user). Module types not listed here are documented in the manual of the relevant module.   - W#16#X5XX: analog module   - W#16#X8XX: function module   - W#16#XCXX: CP   - W#16#XFXX: digital module   - W#16#8340: substitution type ID for input module   - W#16#9340: substitution type ID for output module   - W#16#A340: substitution type ID for combination module (I/O)   - W#16#F340: substitution type ID for empty module or module that cannot be uniquely identified (e.g. with packed addresses)   - Module types not listed here are documented in the manual of the relevant module. - Distributed PROFINET IO:   - W#16#8101: module type of the inserted module is the same as the module type of the removed module   - W#16#8102: module type of the inserted module is not the same as the module type of the removed module |
| For S7-1500:  - W#16#8101: For all pull events; for all plug events except for the insertion of a module with incorrect module type - W#16#8102: module type of the inserted module is not the same as the module type of the removed module |  |  |
| OB83_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

The following table shows which event caused the start of OB 83.

| OB83_EV_CLASS | OB83_FLT_ID | Meaning |
| --- | --- | --- |
| B#16#39 | B#16#51 | - PROFINET IO module removed - For the CPUs 1510SP-1 PN and 1512SP-1 PN: IO module removed |
| B#16#39 | B#16#54 | - PROFINET IO submodule removed - For the CPUs 1510SP-1 PN and 1512SP-1 PN: IO submodule removed |
| B#16#38 | B#16#54 | - PROFINET IO submodule inserted and matches configured submodule - For the CPUs 1510SP-1 PN and 1512SP-1 PN: IO submodule inserted and matches configured submodule |
| B#16#38 | B#16#55 | - PROFINET IO submodule inserted, but does not match configured submodule - For the CPUs 1510SP-1 PN and 1512SP-1 PN: IO submodule inserted, but does not match configured submodule |
| B#16#38 | B#16#56 | - PROFINET IO submodule inserted, but error in module parameter assignment - For the CPUs 1510SP-1 PN and 1512SP-1 PN: IO submodule inserted, but error in module parameter assignment |
| B#16#38 | B#16#57 | - PROFINET IO submodule or module inserted, but with a fault or maintenance - For the CPUs 1510SP-1 PN and 1512SP-1 PN: IO submodule or module inserted, but with fault or maintenance |
| B#16#38 | B#16#58 | - PROFINET IO submodule, access error corrected - For the CPUs 1510SP-1 PN and 1512SP-1 PN: IO submodule, access error corrected |
| B#16#39 | B#16#61 | Module removed or not responding   OB83_MDL_TYPE: Actual module type |
| B#16#38 | B#16#61 | Module inserted, module type OK  OB83_MDL_TYPE: Actual module type |
| B#16#38 | B#16#63 | Module inserted but module type is incorrect  OB83_MDL_TYPE: Actual module type |
| B#16#38 | B#16#64 | Module inserted but faulty (module ID cannot be read)  OB83_MDL_TYPE: Configured module type |
| B#16#38 | B#16#65 | Module inserted but there is an error in module parameter assignment  OB83_MDL_TYPE: Actual module type |
| B#16#39 | B#16#66 | Module not responding, load voltage error |
| B#16#38 | B#16#66 | Module responds again, load voltage error corrected |
| B#16#33 | B#16#67 | Start module parameter reassignment |
| B#16#32 | B#16#67 | End of module parameter reassignment |
| B#16#39 | B#16#68 | Module parameter reassignment terminated with error |
| B#16#39 | B#16#71: | In the "RUN-Redundant" system state of an S7-1500R/H system, a configured central module was unplugged. The redundancy to its partner module was lost. |
| B#16#38 | B#16#72 | In the "RUN-Redundant" system state of an S7-1500R/H system, a configured central module was plugged in. The redundancy to its partner module has been restored. |
| B#16#38 | B#16#73 | In the "RUN-Redundant" system state of an S7-1500R/H system, a configured central module was plugged in, but with a fault. The redundancy to its partner module has been restored. |

> **Note**
>
> If you are using a DPV1 or PROFINET capable CPU, you can use the "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" instruction to obtain additional information about the interrupt that goes beyond the start information of the OB. This also applies if the DP master is operated in S7 compatible mode.

### Programming OB 83

You must add OB 83 to the blocks of your CPU. Write the program that is to be executed in OB 83 to the generated block, and load the block to the CPU as part of your user program.

You can use OB 83, for example, as follows:

- You evaluate the start information in OB 83.
- You then assign parameters for the newly inserted module using the "[WR_PARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_parm-write-module-data-record-s7-300-s7-400)", "[WR_DPARM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_dparm-transfer-data-record-s7-300-s7-400)", "[PARM_MOD](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#parm_mod-transfer-module-data-records-s7-300-s7-400)", "[WR_REC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_rec-write-data-record-to-io-s7-300-s7-400)", and "[RD_REC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_rec-read-data-record-from-io-s7-300-s7-400)" instructions.

## CPU hardware fault organization block (OB 84) (S7-300, S7-400)

### Description

The CPU operating system calls OB 84 in the following cases:

- After memory errors have been detected and corrected

- For WinAC RTX: Errors in the operating system (e.g., "blue screen")

If you have not programmed OB 84, the CPU does not change to STOP mode

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the CPU hardware error OB, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

### Local data for the CPU hardware fault OB

The following table includes the temporary (TEMP) tags of the CPU hardware fault. The default names of OB 84 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB84_EV_CLASS | BYTE | Event class and identifiers:  - B#16#38: outgoing event - B#16#35, B#16#39: incoming event |
| OB84_FLT_ID | BYTE | Error code (B#16#82, B#16#83, B#16#85, B#16#86, B#16#87) |
| OB84_PRIORITY | BYTE | Priority class; can be set via configuration (hardware configuration) |
| OB84_OB_NUMBR | BYTE | OB number (84) |
| OB84_RESERVED_1 | BYTE | Reserved |
| OB84_RESERVED_2 | BYTE | Reserved |
| OB84_RESERVED_3 | WORD | Reserved |
| OB84_RESERVED_4 | DWORD | Reserved |
| OB84_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

The following table shows which event caused the start of OB 84:

| OB84_EV_CLASS | OB84_FLT_ID | Start event of OB 84 |
| --- | --- | --- |
| B#16#35 | B#16#82 | Memory error in operating system detected and corrected |
| B#16#35 | B#16#83 | Accumulation of detected and corrected memory errors |
| B#16#35 | B#16#85 | Error in PC operating system |
| B#16#39 | B#16#86 | Performance of an H-Sync link affected |
| B#16#35 | B#16#87 | Multi-bit memory error detected and corrected |

### Programming OB 84

You must add OB 84 to the blocks of your CPU. Write the program that is to be executed in OB 84 to the generated block, and load the block to the CPU as part of your user program.

You can use OB 84, for example, as follows:

- You evaluate the start information in OB 84.
- You send an alarm to the diagnostics buffer using the "[WR_USMSG](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400)" instruction.

## Priority class error organization block (OB 85) (S7-300, S7-400)

### Description

The CPU operating system calls OB 85 whenever one of the following events occurs:

- Start event for a non-loaded OB (except OB 80, OB 81, OB 82, OB 83, and OB 86)
- Error when the operating system accesses a block
- I/O access error during update of the process image by the system (if the OB 85 call was not suppressed due to the configuration).

  > **Note**
  >
  > If OB 85 has not been programmed, the CPU changes to STOP mode when one of these events is detected.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the priority class error OB, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

### Local data for the priority class error OB

The following table lists the temporary (TEMP) tags of the priority class error OB. The default names of OB 85 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB85_EV_CLASS | BYTE | Event class and identifiers: B#16#35, B#16#38 (only for error code B#16#B3 and B#16#B4), B#16#39 (only for error code B#16#B1, B#16#B2, B#16#B3 and B#16#B4) |
| OB85_FLT_ID | BYTE | Error code (possible values: B#16#A1, B#16#A2, B#16#A3, B#16#A4, B#16#B1, B#16#B2, B#16#B3, B#16#B4) |
| OB85_PRIORITY | BYTE | Priority class; can be set via configuration |
| OB85_OB_NUMBR | BYTE | OB number (85) |
| OB85_RESERVED_1 | BYTE | Reserved |
| OB85_RESERVED_2 | BYTE | Reserved |
| OB85_RESERVED_3 | INT | Reserved |
| OB85_ERR_EV_CLASS | BYTE | Class of the event that caused the error |
| OB85_ERR_EV_NUM | BYTE | Number of the event that caused the error |
| OB85_OB_PRIOR | BYTE | Priority class of the OB that was being processed when the error occurred (only for some error codes; for more details, see below). |
| OB85_OB_NUM | BYTE | Number of the OB that was being processed when the error occurred (only for some error codes; for more details, see below). |
| OB85_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

If you want to program OB 85 dependent on the possible error codes, we recommend that you organize the local tags as follows:

| Tag | Data type |
| --- | --- |
| OB85_EV_CLASS | BYTE |
| OB85_FLT_ID | BYTE |
| OB85_PRIORITY | BYTE |
| OB85_OB_NUMBR | BYTE |
| OB85_DKZ23 | BYTE |
| OB85_RESERVED_2 | BYTE |
| OB85_Z1 | WORD |
| OB85_Z23 | DWORD |
| OB85_DATE_TIME | DATE_AND_TIME |

The following table shows which event caused OB 85 to start and how the error code-dependent tags are assigned.

| OB85_EV_CLASS | OB85_FLT_ID | Meaning |
| --- | --- | --- |
| B#16#35 | B#16#A1 | Your program or the operating system (based on your configuration) creates a start event for an OB that is not loaded on the CPU.  - OB85_Z1: The corresponding temporary tag of the requested OB. This is determined by OB85_Z23. - OB85_Z23:   - High word: Class and number of the event causing the OB call   - Low word, high byte: Program level active at the time of the error  Low word, low byte: Active OB |
| B#16#35 | B#16#A2 | Your program or the operating system (based on your configuration) creates a start event for an OB that is not loaded on the CPU.  OB85_Z1 and OB85_Z23 as for OB85_FLT_ID=B#16#A1 |
| B#16#35 | B#16#A3 | Error when the operating system accesses a block  - OB85_Z1: Error ID of the operating system   - High byte: 1=integrated function, 2=IEC timer   - Low byte: 0=no error resolution, 1=block not loaded, 2=area length error, 3=write-protect error - OB85_Z23:   - High word: Block number   - Low word: Relative address of the MC7 command causing the error. The block type must be taken from OB 85_DKZ23 (B#16#88: OB, B#16#8C: FC, B#16#8E: FB, B#16#8A: DB). |
| B#16#35 | B#16#A4 | PROFINET interface DB cannot be addressed |
| B#16#34 | B#16#A4 | PROFINET interface DB can be addressed again |
| B#16#39 | B#16#B1 | I/O access error when updating the process image of the inputs  - OB85_DKZ23: ID of the type of process image transfer during which the I/O access error occurred   - B#16#10: Byte access   - B#16#20: Word access   - B#16#30: DWord access   - B#16#56 or B#16#57: Transmitting a configured consistency range - OB85_Z1: Reserved for internal use by the CPU: Logical start address of the module If OB85_RESERVED_2 has the value B#16#76, then OB85_Z1 contains the return value of the instruction involved ("[DPRD_DAT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)", "[DPWR_DAT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)", "[UPDAT_PI](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#updat_pi-update-the-process-image-inputs-s7-300-s7-400)", or "[UPDAT_PO](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#updat_po-update-the-process-image-outputs-s7-300-s7-400)"). - OB85_Z23:   - Byte 0: If OB85_DKZ23=B#16#57: Process image partition no.   - Byte 1: Irrelevant, if OB85_DKZ23=B#16#10, 20, or 30; length of the consistency range in bytes, if OB85_DKZ23=B#16#57   - Byte 0 and byte 1, if OB85_DKZ23=B#16#56: Length of the consistency range in bytes   - Bytes 2 and 3: The I/O address causing the I/O access error, if OB85_DKZ23=B#16#10, 20, or 30;  Logical start address of the consistency range, if OB85_DKZ23=B#16#57 |
| B#16#39 | B#16#B2 | I/O access error when transferring the process image output to the output modules  OB85_DKZ23, OB85_Z1 and OB85_Z23 as for OB85_FLT_ID=B#16#B1 |
| You obtain the error codes B#16#B1 and B#16#B2, if you have configured the repeated OB 85 call for I/O access errors for the system-side process image update. |  |  |
| B#16#39/B#16#38 | B#16#B3 | I/O access error when updating the process image input, incoming/outgoing  - OB85_DKZ23: ID of the type of process image transfer during which the I/O access error occurred   - B#16#10: Byte access   - B#16#20: Word access   - B#16#30: DWord access   - B#16#56 or B#16#57: Transmitting a configured consistency range - OB85_Z1: Reserved for internal use by the CPU: Logical start address of the module If OB85_RESERVED_2 has the value B#16#76, then OB85_Z1 contains the return value of the instruction involved ("[DPRD_DAT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dprd_dat-read-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)", "[DPWR_DAT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpwr_dat-write-consistent-data-of-a-dp-standard-slave-s7-300-s7-400)", "[UPDAT_PI](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#updat_pi-update-the-process-image-inputs-s7-300-s7-400)", or "[UPDAT_PO](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#updat_po-update-the-process-image-outputs-s7-300-s7-400)"). - OB85_Z23:   - Byte 0: If OB85_DKZ23=B#16#57: Process image partition no.   - Byte 1: Irrelevant, if OB85_DKZ23=B#16#10, 20, or 30; length of the consistency range in bytes, if OB85_DKZ23=B#16#57   - Byte 0 and byte 1, if OB85_DKZ23=B#16#56: Length of the consistency range in bytes   - Bytes 2 and 3: The I/O address causing the I/O access error, if OB85_DKZ23=B#16#10, 20, or 30;  Logical start address of the consistency range, if OB85_DKZ23=B#16#57 |
| B#16#39/B#16#38 | B#16#B4 | I/O access error when updating the process image of the outputs incoming/outgoing  OB85_DKZ23, OB85_Z1, OB85_Z23 as for OB85_FLT_ID=B#16#B3 |
| You obtain the error codes B#16#B3 and B#16#B4 if you only configured the OB 85 call for incoming and outgoing I/O access errors for system side process image table updating. After a cold or warm restart, all access to non-existing inputs and outputs will be reported as incoming I/O access errors during the next process image table update. |  |  |

### Programming OB 85

You must add OB 85 to the blocks of your CPU. Write the program that is to be executed in OB 85 in the generated block, and load the block to the CPU as part of your user program.

You can use OB 85, for example, as follows:

- To evaluate the start information of OB 85 and to determine which module is missing or defective (information regarding the module start address).
- You determine the slot of the module involved using the "[LGC_GADR](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#lgc_gadr-determine-the-slot-belonging-to-a-logical-address-s7-300-s7-400)" instruction.

## Rack failure organization block (OB 86) (S7-300, S7-400)

### Description

The CPU operating system calls OB 86 in the following cases:

- Failure of a central expansion unit (not for S7-300) is detected (both if incoming or outgoing event).
- Failure of a DP master system is detected (both if incoming or outgoing event).
- Failure of a distributed I/O device (PROFIBUS DP or PROFINET IO) is detected (both if incoming or outgoing event).
- You have deactivated a distributed I/O device (PROFIBUS DP or PROFINET IO) with the "[D_ACT_DP](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#d_act_dp-enabledisable-dp-slaves-s7-300-s7-400)" instruction using MODE=4.
- You have activated a distributed I/O device (PROFIBUS DP or PROFINET IO) with the "[D_ACT_DP](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#d_act_dp-enabledisable-dp-slaves-s7-300-s7-400)" instruction using MODE=3.
- The failure of a PROFINET IO system or a PROFINET IO station or some of the submodules of a PROFINET I-device has been detected.

If OB 86 has not been programmed, the CPU changes to STOP mode when this type of error is detected.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the rack failure OB, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

### Local data for the rack failure OB

The following table lists the temporary (TEMP) tags of the rack failure OB. The default names of OB 86 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB86_EV_CLASS | BYTE | Event class and identifiers:  - B#16#32: Activation of a device with the "D_ACT_DP" instruction using MODE=3 - B#16#33: Deactivation of a device with the "D_ACT_DP" instruction using MODE=4 - B#16#38: outgoing event - B#16#39: incoming event |
| OB86_FLT_ID | BYTE | Error code (possible values: B#16#C1, B#16#C2, B#16#C3, B#16#C4, B#16#C5, B#16#C6, B#16#C7, B#16#C8, B#16#C9, B#16#CA, B#16#CB, B#16#CC, B#16#CD, B#16#CE, B#16#CF, B#16#F8, B#16#F9) |
| OB86_PRIORITY | BYTE | Priority class; can be set via configuration  For S7-1500 CPUs: priority, default value: 6 |
| OB86_OB_NUMBR | BYTE | OB number (86) |
| OB86_RESERVED_1 | BYTE | Reserved |
| OB86_RESERVED_2 | BYTE | Reserved |
| OB86_MDL_ADDR | WORD | Depends on the error code |
| OB86_RACKS_FLTD | ARRAY [0 ..31]  OF BOOL | Depends on the error code |
| OB86_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

If you want to program OB 86 depending on the possible error codes, we recommend that you organize the local tags as follows:

| Tag | Data type |
| --- | --- |
| OB86_EV_CLASS | BYTE |
| OB86_FLT_ID | BYTE |
| OB86_PRIORITY | BYTE |
| OB86_OB_NUMBR | BYTE |
| OB86_RESERVED_1 | BYTE |
| OB86_RESERVED_2 | BYTE |
| OB86_MDL_ADDR | WORD |
| OB86_Z23 | DWORD |
| OB86_DATE_TIME | DATE_AND_TIME |

The following table shows which event caused the start of OB 86.

| OB86_EV_CLASS | OB86_FLT_ID | Meaning |
| --- | --- | --- |
| B#16#39 | B#16#C1 | Expansion rack failure  - OB86_MDL_ADDR: Logical start address of the IM - OB86_Z23: contains a bit for each possible expansion rack: Each expansion rack that caused a call of OB 86 is reported as having failed (the respective bits are set). Expansion racks that previously failed are no longer shown.   - Bit 0: always 0   - Bit 1: 1. expansion rack   - :   - Bit 21: 21. expansion rack   - Bit 22 to 29: always 0   - Bit 30: Failure of at least one expansion rack in the SIMATIC S5 area   - Bit 31: always 0 |
| B#16#38 | B#16#C1 | Expansion rack operational again  OB86_MDL_ADDR as for OB86_FLT_ID=B#16#C1. The expansion racks that are operational again are reported in OB86_Z23 (the respective bits are set). |
| B#16#38 | B#16#C2 | Expansion rack operational again (expansion rack failure with discrepancy between expected and actual configuration)  - OB86_MDL_ADDR: Logical start address of the IM - OB86_Z23: Contains one bit for every possible expansion rack, see OB86_FLT_ID B#16#C1. Meaning of a set bit: In the affected expansion rack:   - modules with incorrect module IDs exist.   - Configured modules missing.   - At least one module is defective. |
| B#16#39 | B#16#C3 | Distributed I/O: Failure of a DP master system Only an incoming event causes OB 86 start with error code B#16#C3. An outgoing event causes OB 86 start with error code B#16#C4 and event class B#16#38: The return of each lower-level DP device has an OB 86 start as consequence.)  - OB86_MDL_ADDR: Logical start address of the DP master - OB86_Z23: DP master system ID:   - Bit 0 to 7: Reserved   - Bit 8 to 15: DP master system ID   - Bit 16 to 31: Reserved |
| B#16#39/B#16#38 | B#16#C4 | Failure of a DP device  - OB86_MDL_ADDR: Logical start address of the DP master - OB86_Z23: Address of the affected DP slave:   - Bit 0 to 7: No. of the DP device   - Bit 8 to 15: DP master system ID   - Bit 16 to 30: Logical start address, if an S7 slave is used, or diagnostics address if a DP standard slave is used.   - Bit 31: I/O identifier |
| B#16#39/B#16#38 | B#16#C5 | Return of a DP device, but device faulty  OB86_MDL_ADDR and OB86_Z23 as with FLT_ID=B#16#C4 |
| B#16#38 | B#16#C6 | Expansion unit return, but error in module parameter assignment  - OB86_MDL_ADDR: Logical start address of the IM - OB86_Z23: contains a bit for each possible expansion rack:   - Bit 0: always 0   - Bit 1: 1. expansion rack   - …   - Bit 21: 21. expansion rack   - Bit 22 to 30: Reserved   - Bit 31: always 0 - Meaning of the set bit: In the affected expansion rack,   - modules with incorrect module IDs exist.   - Modules with missing or incorrect parameters exist. |
| B#16#38 | B#16#C7 | Return of a DP device, but error in module parameter assignment  - OB86_MDL_ADDR: Logical start address of the DP master - Address of the affected DP slave:   - Bit 0 to 7: No. of the DP device   - Bit 8 to 15: DP master system ID   - Bit 16 to 30: Logical start address of the DP slave   - Bit 31: I/O identifier |
| B#16#38 | B#16#C8 | Return of a DP device, however discrepancy in configured and actual configuration  - OB86_MDL_ADDR: Logical start address of the DP master - OB86_Z23: Address of the affected DP slave:   - Bit 0 to 7: No. of the DP device   - Bit 8 to 15: DP master system ID   - Bit 16 to 30: Logical start address of the DP slave   - Bit 31: I/O identifier |
| B#16#32/B#16#33 | B#16#C9 | Activation/deactivation of a DP slave with the "D_ACT_DP" instruction using MODE=3/MODE=4   - OB86_MDL_ADDR: Logical start address of the DP master - OB86_Z23: Address of the affected DP slave   - Bit 0 to 7: No. of the DP device   - Bit 8 to 15: DP master system ID   - Bit 16 to 30: Logical start address, if an S7 slave is used, or diagnostics address if a DP standard slave is used.   - Bit 31: I/O identifier |
| B#16#39 | B#16#CA | PROFINET IO system failure  - OB86_MDL_ADDR: Logical start address of the IO controller - OB86_Z23:   - Bit 0 to 10: 0 (station number)   - Bit 11 to 14: IO system ID   - Bit 15: 1   - Bit 16 to 31: 0 |
| B#16#39/38 | B#16#CB | PROFINET IO device failure/device return  - OB86_RESERVED_1: B#16#C4 - OB86_MDL_ADDR: Logical start address of the IO controller - OB86_Z23:   - Bit 0 to 10: Station number   - Bit 11 to 14: IO system ID   - Bit 15: 1   - Bit 16 to 30: Logical start address of the station   - Bit 31: I/O identifier   Note: Before you check in your program whether a PROFINET IO station failure is the cause for the OB 86 start, you should check whether a PROFINET IO system failure occurred. |
| B#16#/38 | B#16#CC | PROFINET IO station return with problem or maintenance  - OB86_RESERVED_1: B#16#C4 - OB86_MDL_ADDR: Logical start address of the IO controller - OB86_Z23:   - Bit 0 to 10: Station number   - Bit 11 to 14: IO system ID   - Bit 15: 1   - Bit 16 to 30: Logical start address of the station   - Bit 31: I/O identifier |
| B#16#38 | B#16#CD | PROFINET IO device return, expected and actual configuration differ  - OB86_MDL_ADDR: Logical start address of the IO controller - OB86_Z23:   - Bit 0 to 10: Station number   - Bit 11 to 14: IO system ID   - Bit 15: 1   - Bit 16 to 30: Logical start address of the station   - Bit 31: I/O identifier |
| B#16#38 | B#16#CE | PROFINET IO station return, error in module parameter assignment  - OB86_MDL_ADDR: Logical start address of the IO controller - OB86_Z23:   - Bit 0 to 10: Station number   - Bit 11 to 14: IO system ID   - Bit 15: 1   - Bit 16 to 30: Logical start address of the station   - Bit 31: I/O identifier |
| B#16#32/B#16#33 | B#16#CF | Activation/deactivation of a PROFINET IO device with the "D_ACT_DP" instruction using MODE=3/MODE=4   - OB86_MDL_ADDR: Logical start address of the IO controller - OB86_Z23:   - Bit 0 to 10: Station number   - Bit 11 to 14: IO system ID   - Bit 15: 1   - Bit 16 to 30: Logical start address of the station   - Bit 31: I/O identifier |
| B#16#39/B#16#38 | B#16#F8 | Failure/return of some of the submodules of a PROFINET I-device  - OB86_MDL_ADDR: Logical start address of the IO controller - OB86_Z23:   - Bit 0 to 10: Station number   - Bit 11 to 14: IO system ID   - Bit 15: 1   - Bit 16 to 30: Logical start address of the station   - Bit 31: I/O identifier |
| B#16#38 | B#16#F9 | Return of some of the submodules of a PROFINET I-device with a device configuration difference  - OB86_MDL_ADDR: Logical start address of the IO controller - OB86_Z23:   - Bit 0 to 10: Station number   - Bit 11 to 14: IO system ID   - Bit 15: 1   - Bit 16 to 30: Logical start address of the station   - Bit 31: I/O identifier |

> **Note**
>
> If you are using a DPV1 or PROFINET capable CPU, you can use the "[RALRM](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#description-ralrm-s7-300-s7-400)" instruction to obtain additional information about the interrupt that goes beyond the start information of the OB. This also applies if the DP master is operated in S7 compatible mode.

### Programming OB 86

You must add OB 86 to the blocks of your CPU. Write the program that is to be executed in OB 86 to the generated block, and load the block to the CPU as part of your user program.

You can use OB 86, for example, as follows:

- To evaluate the start information of OB 86 and to determine which rack is defective or missing
- You enter an alarm in the diagnostic buffer using the "[WR_USMSG](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#wr_usmsg-write-a-user-diagnostics-event-to-the-diagnostic-buffer-s7-300-s7-400)" instruction and send the alarm to a monitoring device.

## Communication error organization block (OB 87) (S7-300, S7-400)

### Description

The CPU operating system calls OB 87 when an event occurs that was triggered by a communication error.

If you have not programmed OB 87 and a start event for OB 87 occurs, your CPU will react as follows:

- An S7-300 CPU changes to STOP mode.
- An S7-400 CPU does not change to STOP mode.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the communication error OB, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

### Local data for communication error OB

The following table lists the temporary (TEMP) tags of the communication error OB. The default names of OB 87 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB87_EV_CLASS | BYTE | Event class and identifiers: B#16#39 |
| OB87_FLT_ID | BYTE | Error code  (possible values: B#16#D2, B#16#D3, B#16#D4, B#16#D5, B#16#E1, B#16#E2, B#16#E3, B#16#E4, B#16#E5, B#16#E6) |
| OB87_PRIORITY | BYTE | Priority class; can be set via configuration |
| OB87_OB_NUMBR | BYTE | OB number (87) |
| OB87_RESERVED_1 | BYTE | Reserved |
| OB87_RESERVED_2 | BYTE | Reserved |
| OB87_RESERVED_3 | WORD | Depends on the error code |
| OB87_RESERVED_4 | DWORD | Depends on the error code |
| OB87_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

The error code-dependent tags have the following meaning:

| Error code | Tag | Meaning |
| --- | --- | --- |
| B#16#D2 |  | It is not possible to send the diagnostics entries at present. |
| B#16#D3 |  | Synchronization message frames cannot be sent (master). |
| B#16#D4 |  | Illegal time jump through time synchronization |
| B#16#D5 |  | Error in adopting the synchronization time (slave) |
|  | OB87_RESERVED_3 | Includes no extra information |
|  | OB87_RESERVED_4 | Includes no extra information |
| B#16#E1 |  | Incorrect message frame identifier in global data communication |
| B#16#E2 |  | GD package status cannot be entered in a DB |
|  | OB87_RESERVED_3 | DB number |
|  | OB87_RESERVED_4 | - High word: Includes no extra information |
|  |  | - Low word: GD circle number (high byte), GD packet number (low byte) |
| B#16#E3 |  | Message frame length error in global data communication |
| B#16#E4 |  | Illegal GD package number received |
|  | OB87_RESERVED_3 | Interface identifier (0: K bus, 1: MPI) |
|  | OB87_RESERVED_4 | - High byte: GD loop number - Low byte: Includes no extra information |
| B#16#E5 |  | Error accessing DB when exchanging data via communication function blocks |
|  | OB87_RESERVED_1 | Block type: B#16#88: OB, B#16#8A: DB, B#16#8C: FC, B#16#8E: FB |
|  | OB87_RESERVED_3 | Reserved for internal use by the CPU |
|  | OB87_RESERVED_4 | - High word: Number of the block with the MC7 instruction that has caused the error - Low word: Relative address of the MC7 instruction that has caused the error |
| B#16#E6 |  | GD package status cannot be entered in a DB |
|  | OB87_RESERVED_3 | DB number |
|  | OB87_RESERVED_4 | Includes no extra information |
|  |  |  |

### Programming OB 87

You must add OB 87 to the blocks of your CPU. Write the program that is to be executed in OB 87 to the generated block, and load the block to the CPU as part of your user program.

You can use OB 87, for example, as follows:

- You evaluate the start information in OB 87.
- You create a data block when the data block for the status information of the shared data communication is missing.

## Processing interrupt OB (OB 88) (S7-300, S7-400)

### Description

The CPU operating system calls OB 88 after a program block execution is been aborted. Possible causes of the abort are:

- Nesting depth exceeded for synchronous errors
- Nesting depth exceeded for block calls (U stack)
- Error during allocation of local data

If you have not programmed OB 88 and processing is interrupted, the CPU goes to STOP mode (event W#16#4570).

If program block execution is aborted in priority class 28, the CPU goes into STOP mode.

You can use the "[DIS_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_irt-disable-interrupt-event-s7-300-s7-400)" instruction to disable the processing interrupt OB, the "[EN_IRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_irt-enable-interrupt-event-s7-300-s7-400)" instruction to re-enable it, and the "[DIS_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dis_airt-delay-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" and "[EN_AIRT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#en_airt-enable-execution-of-higher-priority-interrupts-and-asynchronous-error-events-s7-300-s7-400)" instructions to delay it.

### Local data of the processing interrupt OB

The following table lists the temporary (TEMP) tags of the processing interrupt OB. The default names of OB 88 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB88_EV_CLASS | BYTE | Event class and identifiers: B#16#35 |
| OB88_SW_FLT | BYTE | Error code  Possible values:  - B#16#71: Nesting depth of nesting levels exceeded - B#16#72: Nesting depth of Master Control Relay exceeded - B#16#73: Nesting depth exceeded for synchronous errors - B#16#74: Nesting depth of block calls (U stack) exceeded - B#16#75: Nesting depth of block calls (B stack) exceeded - B#16#76: Error in local data allocation - B#16#78: Unknown instruction - B#16#7A: Jump instruction with destination outside of the block   Please refer to the operation list for your CPU to determine which error codes apply to your CPU. |
| OB88_PRIORITY | BYTE | Priority class: 28 |
| OB88_OB_NUMBR | BYTE | OB number (88) |
| OB88_BLK_TYPE | BYTE | Type of block in which the error occurred:  - B#16#88: OB - B#16#8C: FC - B#16#8E: FB - B#16##00: Could not determine interrupt source |
| OB88_RESERVED_1 | BYTE | Reserved |
| OB88_FLT_PRIORITY | BYTE | Priority class of the OB that has caused the error |
| OB88_FLT_OB_NUMBR | BYTE | Number of the OB that has caused the error |
| OB88_BLK_NUM | WORD | Number of the block with the MC7 instruction that has caused the error |
| OB88_PRG_ADDR | WORD | Relative address of the MC7 instruction that has caused the error |
| OB88_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

### Programming OB 88

You must add OB 88 to the blocks of your CPU. Write the program that is to be executed in OB 88 to the generated block, and load the block to the CPU as part of your user program.

You can use OB 88, for example, as follows:

- You evaluate the start information in OB 88.
- You enter the cause of the error in an alarm data block.

## Background organization block (OB 90) (S7-300, S7-400)

### Description

With S7 you can monitor a maximum cycle time and guarantee a minimum cycle time. If the execution time of OB 1 including all the nested interrupt processing and system activities is less than the minimum cycle time that you have specified, the operating system reacts as follows:

- It calls the background OB (providing it exists on the CPU).
- It delays the next OB 1 start (if OB 90 does not exist on the CPU).

### Function of the background OB

OB 90 has the lowest priority of all OBs. It is interrupted by any system activity and any interrupt (even by OB 1 after the minimum cycle time has elapsed) and is only resumed if the selected minimum cycle time has not yet been reached. The only exception is the execution of instructions that are started in OB 90. These are executed with the priority of OB 1 and are therefore not interrupted by OB 1. There is no time monitoring of OB 90.

The user program in OB 90 is processed starting with the first instruction in the following situations:

- Following a warm, cold, or hot restart
- After loading or deleting a block
- After downloading OB 90 to the CPU in RUN mode
- After terminating the background cycle

  > **Note**
  >
  > In configurations in which the minimum cycle time and the maximum cycle time are almost the same, the cycle time may be exceeded unexpectedly when instructions are called in the background OB.

### Local data for the background OB

The following table describes the temporary (TEMP) tags of OB 90. The tag names are the default names of OB 90.

| Tag | Data type | Description |
| --- | --- | --- |
| OB90_EV_CLASS | BYTE | Event class and identifiers: B#16#11: Active |
| OB90_STRT_INF | BYTE | - B#16#91: Warm restart/cold restart/hot restart - B#16#92: Deletion of a block - B#16#93: Downloading of OB 90 to the CPU in RUN mode - B#16#95: Termination of the background cycle |
| OB90_PRIORITY | BYTE | Priority class: 29 (corresponds to priority 0.29) |
| OB90_OB_NUMBR | BYTE | OB number (90) |
| OB90_RESERVED_1 | BYTE | Reserved |
| OB90_RESERVED_2 | BYTE | Reserved |
| OB90_RESERVED_3 | INT | Reserved |
| OB90_RESERVED_4 | INT | Reserved |
| OB90_RESERVED_5 | INT | Reserved |
| OB90_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

## Startup organization blocks (OB 100, OB 101 and OB 102) (S7-300, S7-400)

### Startup types

A distinction is made between the following types of startup

- Hot restart (S7-400)
- Warm restart
- Cold restart

In the following table, you can see which OB is called by the operating system during startup.

| Startup type | Corresponding OB |
| --- | --- |
| Hot restart | OB 101 |
| Warm restart | OB 100 |
| Cold restart | OB 102 |

### Startup events

The CPU executes a startup as follows:

- After POWER ON
- After a request by a communication function (via a menu command from the programming device or by calling the "[START](S7%20communication%20%28S7-300%2C%20S7-400%29.md#start-execute-a-warm-restart-or-cold-restart-on-a-remote-device-s7-400)" or "[RESUME](S7%20communication%20%28S7-300%2C%20S7-400%29.md#resume-initiate-a-hot-restart-on-a-remote-device-s7-400)" instruction on a different CPU)

Depending on the start event, the particular CPU, and its parameters, the appropriate startup OB (OB 100, OB 101, or OB 102) is called. With suitable programming, you can make certain default settings for your cyclic program in these blocks.

### Local data for startup OBs

The following table shows the temporary (TEMP) tags of a startup OB. The default names have been selected as tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB10x_EV_CLASS | BYTE | Event class and identifiers: B#16#13: active |
| OB10x_STRTUP | BYTE | Startup request:  - B#16#81: Manual warm restart request - B#16#82: Automatic warm restart request - B#16#83: Request for manual hot restart - B#16#84: Request for automatic hot restart - B#16#85: Request for manual cold restart - B#16#86: Request for automatic cold restart - B#16#87: Master: Request for manual cold restart - B#16#88: Master: Request for automatic cold restart - B#16#8A: Master: Request for manual warm restart - B#16#8B: Master: Request for automatic warm restart |
| OB10x_PRIORITY | BYTE | Priority class: 27 or 1 (for S7-1500 CPUs) |
| OB10x_OB_NUMBR | BYTE | OB number (100, 101, or 102) |
| OB10x_RESERVED_1 | BYTE | Reserved |
| OB10x_RESERVED_2 | BYTE | Reserved |
| OB10x_STOP | WORD | Number of the event that switched the CPU to STOP, see [Event class 4 - stop events and other mode changes](Events%20%28S7-300%2C%20S7-400%29.md#event-class-4---stop-events-and-other-mode-changes-s7-300-s7-400) |
| OB10x_STRT_INFO | DWORD | Supplementary information about the current startup |
| OB10x_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

The following table shows the assignment of the tags OB10x_STR_INFO.

| Bit no. | Meaning | Possible binary values | Explanation |
| --- | --- | --- | --- |
| 31-24 | Startup information | 0000 xxxx | Rack number 0 (H CPUs only) |
| 0100 xxxx | Rack number 1 (H-CPUs only) |  |  |
| 1000 xxxx | Rack number 2 (H-CPUs only) |  |  |
| 0001 xxxx | Multicomputing (S7-400 only) |  |  |
| 0010 xxxx | Operation of more than one CPU in the segmented rack (S7-400 only) |  |  |
| xxxx xxx0 | No difference between expected and actual configuration  (S7-300 only) |  |  |
| xxxx xxx1 | Difference between expected and actual configuration  (S7-300 only) |  |  |
| xxxx xx0x | No difference between expected and actual configuration |  |  |
| xxxx xx1x | Difference between expected and actual configuration |  |  |
| xxxx x0xx | Not an H CPU |  |  |
| xxxx x1xx | H CPU |  |  |
| xxxx 0xxx | Clock for time stamp not battery-backed at last POWER ON |  |  |
| xxxx 1xxx | Clock for time stamp battery-backed at last POWER ON |  |  |
| 23-16 | Startup type just performed  Note: These bits have no meaning for S7-1500 CPUs. | 0000 0001 | Warm restart for multicomputing without operator input on the CPU according to parameter assignment (S7-400 only) |
| 0000 0011 | Warm restart triggered by mode selector |  |  |
| 0000 0100 | Warm restart triggered by PG operator input |  |  |
| 0000 0101 | Cold restart in multicomputing without operator input on the CPU according to parameter assignment (S7-400 only) |  |  |
| 0000 0111 | Cold restart triggered with mode selector |  |  |
| 0000 1000 | Cold restart triggered by PG operator input |  |  |
| 0000 1010 | Hot restart in multicomputing without operator input on the CPU according to parameter assignment (S7-400 only) |  |  |
| 0000 1011 | Hot restart triggered with mode selector  (S7-400 only) |  |  |
| 0000 1100 | Hot restart triggered by PG operator input (S7-400 only) |  |  |
| 0001 0000 | Automatic warm restart after battery-backed POWER ON |  |  |
| 0001 0001 | Cold restart after battery-backed POWER ON according to parameter assignment |  |  |
| 0001 0011 | Warm restart triggered with mode selector; last POWER ON battery-backed |  |  |
| 0001 0100 | Warm restart triggered by PG operator input; last POWER ON battery-backed |  |  |
| 0010 0000 | Automatic warm restart after non-battery-backed POWER ON (with memory reset by system) |  |  |
| 0010 0001 | Cold restart after non-battery-backed POWER ON (with memory reset by system) |  |  |
| 0010 0011 | Warm restart triggered with mode selector; last POWER ON not battery-backed |  |  |
| 0010 0100 | Warm restart triggered by PG operator input; last POWER ON not battery-backed |  |  |
| 1010 0000 | Automatic hot restart after battery-backed POWER ON according to parameter assignment (S7-400 only) |  |  |
| 15-12 | Permissibility of automatic startup  Note: These bits have no meaning for S7-1500 CPUs. | 0000 | Automatic startup illegal, memory reset requested |
| 0001 | Automatic startup illegal, parameter modifications, etc. necessary |  |  |
| 0111 | Automatic warm restart permitted |  |  |
| 1111 | Automatic restart (warm/hot) permitted  (S7-400 only) |  |  |
| 11-8 | Permissibility of manual startup  Note: These bits have no meaning for S7-1500 CPUs. | 0000 | Startup illegal, memory reset requested |
| 0001 | Startup illegal, parameter modifications, etc. necessary |  |  |
| 0111 | Warm restart permitted |  |  |
| 1111 | Warm restart and hot restart permitted (S7-400 only) |  |  |
| 7-0 | Last valid intervention or setting of the automatic startup at POWER ON | 0000 0000 | No startup |
| 0000 0001 | Warm restart in multicomputing without operator input on the CPU according to parameter assignment (S7-400 only) |  |  |
| 0000 0011 | Warm restart triggered by mode selector |  |  |
| 0000 0100 | Warm restart triggered by PG operator input |  |  |
| 0000 0101 | Cold restart in multicomputing without operator input on the CPU according to parameter assignment (S7-400 only) |  |  |
| 0000 0111 | Cold restart triggered with mode selector |  |  |
| 0000 1000 | Cold restart triggered by PG operator input |  |  |
| 0000 1010 | Hot restart in multicomputing without operator input on the CPU according to parameter assignment (S7-400 only) |  |  |
| 0000 1011 | Hot restart triggered with mode selector (S7-400 only) |  |  |
| 0000 1100 | Hot restart triggered by PG operator input (S7-400 only) |  |  |
| 0001 0000 | Automatic warm restart after battery-backed POWER ON |  |  |
| 0001 0001 | Cold restart after battery-backed POWER ON according to parameter assignment |  |  |
| 0001 0011 | Warm restart triggered with mode selector; last POWER ON battery-backed |  |  |
| 0001 0100 | Warm restart triggered by PG operator input; last POWER ON battery-backed |  |  |
| 0010 0000 | Automatic warm restart after non-battery-backed POWER ON (with memory reset by system) |  |  |
| 0010 0001 | Cold restart after non-battery-backed POWER ON (with memory reset by system) |  |  |
| 0010 0011 | Warm restart triggered with mode selector; last POWER ON not battery-backed |  |  |
| 0010 0100 | Warm restart triggered by PG operator input; last POWER ON not battery-backed |  |  |
| 1010 0000 | Automatic hot restart after battery-backed POWER ON according to parameter assignment (S7-400 only) |  |  |

---

**See also**

[Principles of the STARTUP mode (S7-300, S7-400)](Functional%20description%20of%20S7-300-400%20CPUs%20%28S7-300%2C%20S7-400%29.md#principles-of-the-startup-mode-s7-300-s7-400)

## Programming error organization block (OB 121) (S7-300, S7-400)

### Description

The CPU operating system calls OB 121 whenever an event occurs that is caused by an error related to the processing of the program. For example, if your program calls a block that has not been loaded on the CPU, OB 121 is called.

### Function of the programming error OB

OB 121 is executed in the same priority class as the interrupted block.

If OB 121 is not programmed, the CPU changes the operating mode from RUN to STOP.

S7 provides the following instructions for use in masking and unmasking start events of OB 121 during the execution of your program:

- The "[MSK_FLT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#msk_flt-mask-synchronous-error-events-s7-300-s7-400)" instruction masks certain error codes.
- The "[DMSK_FLT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)" instruction unmasks the error codes that were masked by the "[MSK_FLT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#msk_flt-mask-synchronous-error-events-s7-300-s7-400)" instruction.
- The "[READ_ERR](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#read_err-read-out-event-status-register-s7-300-s7-400)" instruction reads the event status register.

### Local data for the programming error OB

The following table lists the temporary (TEMP) tags of the programming error OB. The default names of OB 121 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB121_EV_CLASS | BYTE | Event class and identifiers: B#16#25 |
| OB121_SW_FLT | BYTE | Error code (possible values: B#16#21, B#16#22, B#16#23, B#16#24, B#16#25, B#16#26, B#16#27, B#16#28, B#16#29, B#16#30, B#16#31, B#16#32, B#16#33, B#16#34, B#16#35, B#16#3A, B#16#3C, B#16#3D, B#16#3E, B#16#3F) |
| OB121_PRIORITY | BYTE | Priority class of the OB where the error occurred  For S7-1500 CPUs: priority, default value: 7 |
| OB121_OB_NUMBR | BYTE | OB number (121) |
| OB121_BLK_TYPE | BYTE | Type of block where the error occurred (no valid value is entered here in case of S7-300): B#16#88: OB, B#16#8A: DB, B#16#8C: FC, B#16#8E: FB |
| OB121_RESERVED_1 | BYTE | Reserved |
| OB121_FLT_REG | WORD | Source of the error (depends on error code); for example:  - Register in which the conversion error occurred - Incorrect address (read/write error) - Incorrect timer/counter/block number - Incorrect memory area |
| OB121_BLK_NUM | WORD | Number of the block with the MC7 command that caused the error (no valid number is entered here for an S7-300) |
| OB121_PRG_ADDR | WORD | Relative address of the MC7 instruction that has caused the error  FB) (no valid number is entered here for an S7-300) |
| OB121_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

The error code-dependent tags have the following meaning:

| Error code | Tag | Meaning |
| --- | --- | --- |
| B#16#21 |  | BCD conversion error |
|  | OB121_FLT_REG | Identifier for the affected tab (W#16#0000: battery 1) |
| B#16#22 |  | Area length error when reading |
|  | OB121_RESERVED_1 | - Bit 7 to 4 type of access:   - 0: Bit access,   - 1: Byte access,   - 2: Word access,   - 3: DWord access - Bit 3 to 0 memory area:   - 0: I/O area   - 1: Process image input   - 2: Process image output   - 3: Bit memory   - 4: Global DB   - 5: Instance DB   - 6: own local data   - 7: Local data of the caller |
| B#16#23 |  | Area length error when writing |
|  | OB121_RESERVED_1 | Same as for error code B#16#22 |
| B#16#28 |  | Read access to a byte, word or double word with a pointer, the bit address of which is not 0 |
|  | OB121_RESERVED_1 | Same as for error code B#16#22 |
| B#16#29 |  | Write access to a byte, word or double word with a pointer, the bit address of which is not 0  Faulty byte address. Refer to OB121_RESERVED_1 for the data area and the type of access |
|  | OB121_RESERVED_1 | Same as for error code B#16#22 |
| B#16#24 |  | Area error when reading |
|  | OB121_FLT_REG | The low byte contains the identifier for the unauthorized area (B#16#86 own local data area) |
| B#16#25 |  | Area error when writing |
|  | OB121_FLT_REG | The low byte contains the identifier for the unauthorized area (B#16#86 own local data area) |
| B#16#26 |  | Error in timer number |
|  | OB121_FLT_REG | Unauthorized number |
| B#16#27 |  | Error in counter number |
|  | OB121_FLT_REG | Unauthorized number |
| B#16#30 |  | Write access to a write-protected global DB |
|  | OB121_FLT_REG | Unauthorized DB number |
| B#16#31 |  | Write access to a write-protected instance DB |
|  | OB121_FLT_REG | Unauthorized DB number |
| B#16#32 |  | DB number error when accessing a global DB |
|  | OB121_FLT_REG | Unauthorized DB number |
| B#16#33 |  | DB number error when accessing an instance DB |
|  | OB121_FLT_REG | Unauthorized DB number |
| B#16#34 |  | Number error during FC call |
|  | OB121_FLT_REG | FC number |
| B#16#35 |  | FB number error during FC call |
|  | OB121_FLT_REG | FB number |
| B#16#3A |  | Access to a DB that is not loaded; the DB number is located in the permitted area |
|  | OB121_FLT_REG | DB number |
| B#16#3C |  | Access to an FC that is not loaded; the FC number lies in the permissible area |
|  | OB121_FLT_REG | FC number |
| B#16#3D |  | Access to an instruction that is not available; the SFC number is located in the permitted area |
|  | OB121_FLT_REG | SFC number |
| B#16#3E |  | Access to an FB that is not loaded; the FB number lies in the permissible area |
|  | OB121_FLT_REG | FB number |
| B#16#3F |  | Access to an SFB that is not available; the SFB number lies in the permissible area |
|  | OB121_FLT_REG | SFB number |

### Programming OB 121

You must add OB 121 to the blocks of your CPU. Write the program that is to be executed in OB 121 to the generated block, and load the block to the CPU as part of your user program.

You can use OB 121, for example, as follows:

- You evaluate the start information in OB 121.
- You enter the cause of the error in an alarm data block.

## I/O access error organization block (OB 122) (S7-300, S7-400)

### Description

The CPU operating system calls OB 122 whenever an error occurs while accessing data on a module. For example, if the CPU detects a read error when accessing data on a signal module, the operating system calls OB 122.

### Function of the I/O access error OB

OB 122 is executed in the same priority class as the interrupted block. If OB 122 is not programmed, the CPU changes the operating mode from RUN to STOP.

S7 provides the following instructions for use in masking and unmasking start events of OB 122 during the execution of your program:

- The "[MSK_FLT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#msk_flt-mask-synchronous-error-events-s7-300-s7-400)" instruction masks certain error codes.
- The "[DMSK_FLT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dmsk_flt-unmask-synchronous-error-events-s7-300-s7-400)" instruction unmasks the error codes that were masked by the "[MSK_FLT](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#msk_flt-mask-synchronous-error-events-s7-300-s7-400)" instruction.
- The "[READ_ERR](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#read_err-read-out-event-status-register-s7-300-s7-400)" instruction reads the event status register.

### Local data for the I/O access error OB

The following table lists the temporary (TEMP) tags of the I/O access error OB. The default names of OB 122 have been selected as the tag names.

| Tag | Data type | Description |
| --- | --- | --- |
| OB122_EV_CLASS | BYTE | Event class and identifiers: B#16#29 |
| OB122_SW_FLT | BYTE | Error code:  - B#16#42: I/O access error, reading. - B#16#43: I/O access error, writing. |
| OB122_PRIORITY | BYTE | Priority class of the OB where the error occurred  For S7-1500 CPUs: priority, default value: 7 |
| OB122_OB_NUMBR | BYTE | OB number (122) |
| OB122_BLK_TYPE | BYTE | Type of block where the error occurred (B#16#88: OB, B#16#8C: FC, B#16#8E: FB) (no valid number is entered here for an S7-300) |
| OB122_MEM_AREA | BYTE | Memory area and access type:  - Bit 7 to 4: Access type   - 0: Bit access   - 1: Byte access   - 2: Word access   - 3: DWord access - Bit 3 to 0: memory area   - 0: I/O area   - 1: Process image input   - 2: Process image output |
| OB122_MEM_ADDR | WORD | Memory address where the error occurred |
| OB122_BLK_NUM | WORD | Number of the block with the MC7 command that caused the error (no valid number is entered here for an S7-300) |
| OB122_PRG_ADDR | WORD | Relative address of the MC7 command that caused the error  (no valid value is entered here for an S7-300) |
| OB122_DATE_TIME | DATE_AND_TIME | Date and time when the OB was called |

### Sample program for OB 122

The following sample program will provide a substitute value in the "REPL_VAL" instruction. If an input module fails, the processing of the L PEB0 instruction generates a synchronous error and starts OB 122. The load command reads in the value 0 by default. However, you can use the "[REPL_VAL](STL%20%28S7-300%2C%20S7-400%29.md#repl_val-enter-substitute-value-s7-300-s7-400)" instruction to specify any substitute value suitable for the process. This instruction replaces the ACCU content with the specified substitute value.

| STL | Description |
| --- | --- |
| L B#16#42 | //Identifier for "I/O access error reading" event |
| L #OB122_SW_FLT | //Error code of OB 122 |
| ==I | //If the same, |
| SPB Qfeh | //then jump to Qfeh |
| L B#16#43 | //Identifier for "I/O access error writing" event |
| &lt;&gt;I | //If not the same as the error code in OB 122, |
| SPB STOP | //then jump to STOP |
| Qfeh: |  |
| CALL "REPL_VAL" | //Call the "REPL_VAL" instruction |
| VAL:= DW#16#2912 | //Substitute value that is loaded in ACCU 1 |
| RET_VAL:= #error | //Save the return value in #error |
| L #error | //Return value of the "REPL_VAL" instruction |
| L 0 |  |
| ==I | //If the same as 0 (no error has occurred), |
| BEC | //then end the block |
| STOP: |  |
| CALL "STP" | //Call the "STP" instruction: The CPU switches to STOP mode. |
