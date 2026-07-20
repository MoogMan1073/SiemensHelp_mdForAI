---
title: "Modbus slave (RTU) (S7-300, S7-400)"
package: ProgFBMBenUS
topics: 6
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Modbus slave (RTU) (S7-300, S7-400)

This section contains information on the following topics:

- [Modbus instructions (S7-300, S7-400)](#modbus-instructions-s7-300-s7-400)
- [MODB_341: Modbus slave instruction for CP 341 (S7-300, S7-400)](#modb_341-modbus-slave-instruction-for-cp-341-s7-300-s7-400)
- [MODB_441: Modbus slave instruction for CP 441 (S7-300, S7-400)](#modb_441-modbus-slave-instruction-for-cp-441-s7-300-s7-400)
- [ERROR_NR, ERROR_INFO parameters (S7-300, S7-400)](#error_nr-error_info-parameters-s7-300-s7-400)
- [SYSTAT error message area (S7-300, S7-400)](#systat-error-message-area-s7-300-s7-400)

## Modbus instructions (S7-300, S7-400)

### Introduction

The Modbus masters do not need separate Modbus instructions for communication.

### Instructions of CP 341

The data transfer between CP 341 and the CPU is handled using the instructions P_SND_RK and P_RCV_RK.

Instructions of CP 341

| Instruction | Meaning |
| --- | --- |
| P_RCV_RK | Using the P_RCV_RK instruction, you can receive data from a communication partner and save the data to a data block or provide data for the communication partner. |
| P_SND_RK | Using the P_SND_RK instruction, you can send the entire area or a section of a data block to a communication partner or fetch data from a communication partner. |

### Instructions from the automation system S7-400

The data transfer between CP 441 and the CPU is handled using the instructions BSEND and BRCV.

Instructions from the automation system S7-400

| SFB | Meaning |
| --- | --- |
| BSEND | With the instruction BSEND, you can send data from a S7-data range to a communication partner with a destination. |
| BRCV | With the instruction BRCV, you can receive the data from a communication partner and transfer it to a S7-data range. |

## MODB_341: Modbus slave instruction for CP 341 (S7-300, S7-400)

### Description

The MODB_341 instruction and associated driver enable a communication connection between a Modbus master control system and the CP 341 communication module as "Modbus-capable" slave system.

### Operating principle

In the user program, the MODB_341 instruction is is called in the cyclic routine. The instruction uses the associated IDB_MODB_341 instance DB as the working area.

The MODB_341 instruction initializes the CP and executes the Modbus functions which the driver cannot execute by itself.

The MODB_341 instruction must be performed following every cold or warm restart of the CPU. Initialization is triggered by a rising edge at the input CP_START. The instruction deletes the instance DB, calls system instruction SZL_LESEN to read the I, Q, F, T and C address areas from the CPU and saves these to the instance DB. This procedure allows you to check whether the write requests from the Modbus master system are out of range.

A SEND job reports the number of the instance DB and the currently successful initialization progress to the CP.

Once the SEND job is completed without errors, output CP_START_OK is set and initialization of the instruction is completed.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| LADDR | INPUT | Int | Base address of the CP  Use HW Config assignment |
| START_TIMER | INPUT | Timer | Timer for start of monitoring time |
| START_TIME | INPUT | S5Time | Time value for start of monitoring time |
| OB_MASK | INPUT | BOOL | Mask I/O access errors, delay interrupts  FALSE:  I/O access errors are not masked.  TRUE:  I/O access errors are masked and interrupts are delayed. |
| CP_START | INPUT | BOOL | Start instruction initialization |
| CP_START_FM | INPUT | BOOL | Initialization is triggered with a rising edge at CP_START. |
| CP_START_NDR | OUTPUT | BOOL | Info: Write request from the CP |
| CP_START_OK | OUTPUT | BOOL | Startup completed without error  TRUE:  The initialization job could be completed without error before the monitoring time elapsed. |
| CP_START_ERROR | OUTPUT | BOOL | Startup canceled with error  TRUE:  The initialization job could not be completed without error even after the monitoring time had elapsed. |
| ERROR_NR | OUTPUT | Word | Error number  Allocation, see [ERROR_NR, ERROR_INFO parameters](#error_nr-error_info-parameters-s7-300-s7-400) |
| ERROR_INFO | OUTPUT | Word | Additional error info  Allocation, see [ERROR_NR, ERROR_INFO parameters](#error_nr-error_info-parameters-s7-300-s7-400) |

### How to Handle an Error

If the SEND job is terminated with errors, CP_START is reset and CP_START_ERROR is set.

If initialization ends with errors, Modbus communication is not possible. All requests from the Modbus master system are answered with an exception code frame.

After power on, the CP needs several seconds to complete the hardware and memory test before it is ready for operation. The initialization attempts carried out by the MODB_341 instruction within this period are terminated with error. For this reason, the instruction repeats its initialization job several times within the monitoring time.

If the initialization is successfully completed within the configured START-TIME of the START-TIMERS, CP_START_OK is set. If the initialization job cannot be completed without errors even after the monitoring time has elapsed, CP_START_ERROR is set.

## MODB_441: Modbus slave instruction for CP 441 (S7-300, S7-400)

### Description

The MODB_441 instruction and associated driver enable a communication connection between a Modbus master control system and the CP 441-2 communication module as "Modbus-capable" slave system.

### Operating principle

In the user program, the MODB_441 instruction is is called in the cyclic routine. The instruction uses the associated IDB_MODB_441 instance DB as the working area.

The Modbus function codes 01, 02, 03, 04, 06 and 16 are processed directly by the CP. For function codes 05 and 15, the instruction handles the bit-by-bit entry of the data in the SIMATIC memory range.

The MODB_441 instruction initializes the CP and executes the Modbus functions which the driver cannot execute by itself.

The MODB_441 instruction must be performed following every cold or warm restart of the CPU. Initialization is triggered by a rising edge at the input CP_START. The instruction deletes the instance DB, calls system instruction SZL_LESEN to read the I, Q, F, T and C address areas from the CPU and saves these to the instance DB. This procedure allows you to check whether the write requests from the Modbus master system are out of range.

A SEND job reports the number of the instance DB and the currently successful initialization progress to the CP.

Once the SEND job is completed without errors, output CP_START_OK is set and initialization of the instruction is completed.

### Parameters

| Parameters | Declaration | Data type | Description |
| --- | --- | --- | --- |
| ID | INPUT | Word | Connection ID  Connection ID from configuration of the data link. |
| START_TIMER | INPUT | Timer | Timer for start of monitoring time |
| START_TIME | INPUT | S5Time | Time value for start of monitoring time |
| STATUS_TIMER | INPUT | Timer | Read Timer for SYSTAT |
| STATUS_TIME | INPUT | S5Time | Read time interval for SYSTAT |
| OB_MASK | INPUT | BOOL | Mask I/O access errors, delay interrupts  FALSE:  I/O access errors are not masked.  TRUE:  I/O access errors are masked and interrupts are delayed. |
| CP_START | INPUT | BOOL | Start instruction initialization |
| CP_START_FM | INPUT | BOOL | Initialization is triggered with a rising edge at CP_START. |
| CP_START_NDR | OUTPUT | BOOL | Info: Write request from the CP |
| CP_START_OK | OUTPUT | BOOL | Startup completed without error  TRUE:  The initialization job could be completed without error before the monitoring time elapsed. |
| CP_START_ERROR | OUTPUT | BOOL | Startup canceled with error  TRUE:  The initialization job could not be completed without error even after the monitoring time had elapsed. |
| ERROR_NR | OUTPUT | Word | Error number  Allocation, see [ERROR_NR, ERROR_INFO parameters](#error_nr-error_info-parameters-s7-300-s7-400) |
| ERROR_INFO | OUTPUT | Word | Additional error info  Allocation, see [ERROR_NR, ERROR_INFO parameters](#error_nr-error_info-parameters-s7-300-s7-400) |

### How to Handle an Error

If the SEND job is terminated with errors, CP_START is reset and CP_START_ERROR is set.

If initialization ends with errors, Modbus communication is not possible. All requests from the Modbus master system are answered with an exception code frame.

After power on, the CP needs several seconds to complete the hardware and memory test before it is ready for operation. The initialization attempts carried out by the MODB_441 instruction within this period are terminated with error. For this reason, the instruction repeats its initialization job several times within the monitoring time.

If the initialization is successfully completed within the configured START-TIME of the START-TIMERS, CP_START_OK is set. If the initialization job cannot be completed without errors even after the monitoring time has elapsed, CP_START_ERROR is set.

## ERROR_NR, ERROR_INFO parameters (S7-300, S7-400)

### Error classes

| Error numbers from ... to | Description | Meaning |
| --- | --- | --- |
| 1 ... 9 | Instruction and CP initialization error | Error numbers 1 to 9 indicate that initialization was terminated with errors. The CP_START_ERROR parameter is set to 1.  Modbus communication to the master system is not possible. |
| 10 ... 19 | Error executing a function code | Error numbers 10 to 19 indicate that an error occurred during the processing of a function code. The CP transmitted an invalid execution job to the communication instruction.  The error is also reported to the driver.  Subsequent execution jobs continue to be processed. |
| 90 ... 99 | Other faults/errors | A processing error has occurred.  The error is not reported to the driver.  Subsequent execution jobs continue to be processed. |

### ERROR_NR, ERROR_INFO parameters

| ERROR_ No (decimal) | ERROR_INFO | Error Text | Remedy |
| --- | --- | --- | --- |
| 0 | 0 | No error |  |
| 1 | SFC 51->RET_VAL | Error reading the system status list with SFC 51. | Analyze RET_VAL in ERROR_INFO; eliminate the cause. |
| 2 |  | Timeout of CP initialization or error during CP initialization | Check if the CP interface was assigned the "Modbus slave" protocol in the parameters.  Analyze ERROR_INFO. |
| P_SND_RK -> STATUS | Error in P_SND_RK job | Check module address LADDR at the communication instruction. |  |
| SFB 12->STATUS | Error in BSEND job | Check the connection ID in the communication instruction. |  |
| 10 | Processing Code | The driver transferred an invalid processing function to the communication instruction. | CP restart (Power_On) |
| 11 | Start address | The driver transferred an invalid start address to the communication instruction. | Check Modbus address of Modbus master system. |
| 12 | Register number | The driver transferred an invalid number of registers to the communications instruction: Number of registers = 0. | Check number of registers of Modbus master system, if required restart CP (Power_ON) |
| 13 | Register number | The driver transferred an invalid number of registers to the communications instruction: Number of registers > 128. | Check number of registers of Modbus master system, if required restart CP (Power_ON) |
| 14 | Memory bits M - End Address | Attempted access to SIMATIC memory area "memory bits" in excess of range end.  Attention: Range length in SIMATIC CPU is CPU type-dependent. | Reduce Modbus start address and/or access length in Modbus master system. |
| 15 | Outputs Q – End Address | Attempted access to SIMATIC memory area "outputs" in excess of range end.  Attention: Range length in SIMATIC CPU is CPU type-dependent. | Reduce Modbus start address and/or access length in Modbus master system. |
| 16 | Timers T – End Address | Attempted access to SIMATIC memory area "timers" in excess of range end.  Attention: Range length in SIMATIC CPU is CPU type-dependent. | Reduce Modbus start address and/or access length in Modbus master system. |
| 17 | Counters C – End Address | Attempted access to SIMATIC memory area "counters" in excess of range end.  Attention: Range length in SIMATIC CPU is CPU type-dependent. | Reduce Modbus start address and/or access length in Modbus master system. |
| 18 | 0 | The driver transferred an invalid SIMATIC memory area to the communication instruction. | If required, restart CP (Power_On) |
| 19 |  | Error during access to SIMATIC I/Os. | Check if the required I/Os exist and are error-free. |
| 90 | P_SND_RK -> STATUS | Error transmitting an acknowledgment message to the driver using the P_SND_RK instruction | Analyze the STATUS information |
| SFB 12->STATUS | Error transmitting an acknowledgment message to the driver using SFB 12 BSEND | Analyze the STATUS information |  |
| 91 | SFB 22->STATUS | Error reading SYSTAT with SFB 22 (STATUS) | Analyze the STATUS information |
| 92 | P_RCV_RK -> STATUS | Error executing a RECEIVE/FETCH call using the P_RCV_RK instruction | Analyze P_RCV_RK-STATUS |

## SYSTAT error message area (S7-300, S7-400)

### Event classes

| Event class | Meaning |
| --- | --- |
| 5 | Error executing a CPU job |
| 8 | Receive errors |
| 14 (0E<sub>H</sub>) | General processing error |

### STATUS parameter

| Error code(W#16#...) | Description | Remedy |
| --- | --- | --- |
| 0518 | Transmission frame length exceeded (> 4 KB) or insufficient transmission frame length for SEND. | Check the communication instruction; reload it if necessary. |
| 0806 | Character delay time ZVZ exceeded | Error by the partner device or repair disruptions on the transmission line. |
| 080C | A character transmission error was detected (parity error, overrun error or stop bit error (frame)). | Check if the transmission lines are affected by interference. Modify the system configuration or the cable routing.  Check the consistency of the settings for the protocol parameters baud rate, number of data bits, parity and number of stop bits at the CP and link partner. |
| 080D | BREAK  The receive line to the partner device is disrupted. | Establish the connection between the devices or switch on the partner device.  In TTY mode, check if there is a line current flow in idle state. For an RS422/485(X27) connection, check or modify the default configuration of the 2-wire receive line R(A) and R(B). |
| 0830 | Broadcast is not allowed with this function code. | The MODBUS master system can use the broadcast function only for the function codes enabled for this purpose. |
| 0831 | Function code received is invalid. | This function code cannot be used with this driver. |
| 0832 | Maximum number of bits or registers exceeded or the number of bits cannot be divided by the value 16 for access to the SIMATIC memory area for timers and counters. | Limit the maximum number of bits to 2040 and of the registers to 127. Access to SIMATIC timers/counters only in 16‑bit intervals only. |
| 0833 | The number of bits or registers for function code FC 15/16 and frame element byte_count do not match. | Adjust the number of bits, number of registers or the byte_count. |
| 0834 | Illegal bit coding for "Set bit / Reset bit" recognized. | Always use the codes 0000 hex or FF00 hex for FC 05. |
| 0835 | Invalid diagnostics subcode (≠ 0000 hex) detected for function code FC 08 "Loop back test". | Always use subcode 0000 hex for FC 08. |
| 0836 | The internally calculated value of the CRC 16 checksum does not match the CRC checksum received. | Check the calculation of the CRC checksum at the MODBUS master system. |
| 0837 | Message frame sequence error: The MODBUS master system sent a new request message frame before the driver transmitted the last response message frame. | Increase the timeout for the slave response message frame at the MODBUS master system. |
| 0E01 | Error during initialization of the driver-specific SCC process. | Reassign parameters of driver and reload. |
| 0E02 | Error during startup of driver: Wrong SCC process active (SCC driver). The driver cannot function with this SCC driver. | Reassign parameters of driver and reload. |
| 0E03 | Driver startup error: Incorrect data transfer process is active (interface to the SFBs). The driver does not work with this data transfer process. | Reassign parameters of driver and reload. |
| 0E04 | Driver startup error: Invalid interface module. The driver cannot be operated with the configured interface module. | Check and correct the parameter assignment. |
| 0E05 | Error with driver dongle: No dongle plugged in, or inserted dongle is faulty. The driver is not ready to run. | Check if a driver dongle is plugged into the CP. If the inserted dongle is faulty, replace it with a correct dongle. |
| 0E06 | Error with driver dongle: The dongle has no valid content. The driver is not ready to run. | Obtain a correct dongle from the Siemens office which supplied you with the driver. |
| 0E10 | Internal error procedure:  default branch in Send automatic device. | CP restart (Power_On) |
| 0E11 | Internal error procedure:  default branch in Receive automatic device. | CP restart (Power_On) |
| 0E12 | Internal error active automatic device:  Default branch | CP restart (Power_On) |
| 0E13 | Internal error passive automatic device:  Default branch | CP restart (Power_On) |
| 0E20 | This connection requires 8 data bits. The driver is not ready for operation. | Correct the parameter assignment of the driver. |
| 0E21 | The parameterized multiplication factor for the character delay time is not within the range of 1 to 10. The driver is operating with default setting 1. | Correct the parameter assignment of the driver. |
| 0E22 | The operating mode set for the driver is illegal.  Specify "Normal" or "Interference Suppression". The driver is not ready for operation. | Correct the parameter assignment of the driver. |
| 0E23 | Parameter assignment with invalid value for the slave address. Slave address 0 is invalid. The driver is not ready for operation. | Correct the parameter assignment of the driver. |
| 0E24 | Invalid limits were configured for write access. The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E25 | An invalid "from/to" combination was configured in the specification of the "Conversion of the Modbus addresses with function code FC 01, 05, 15" area.  (Memory bits, outputs, timers, counters area). The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E26 | An invalid "from/to" combination was configured in the specification of the "Conversion of the Modbus addresses with function code FC 02" area.  (Memory bits, inputs area). The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E27 | An overlap was configured in the specification of the "Conversion of the Modbus addresses with function code FC 01, 05, 15" area.  (Memory bits, outputs, timers, counters area). The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E28 | An overlaps was configured in the specification of the "Conversion of the Modbus addresses with function code FC 02" area.  (Memory bits, inputs area). The driver is not ready. | Correct the parameter assignment of the driver. |
| 0E2E | An error occurred when reading the interface parameter file. The driver is not ready to run. | Restart CP (Power_On). |
| 0E30 | Internal error during data transmission to CPU:  Unexpected acknowledgment Passive. | Can be ignored if it happens intermittently. |
| 0E31 | Timeout during data transfer to the CPU. | Check CP-CPU interface. |
| 0E32 | Error occurred during data transmission to CPU with RCV: Exact failure reason (detailed error) is in SYSTAT before this entry. | Check CP-CPU interface. |
| 0E33 | Internal error during data transfer to the CPU:  Illegal status of automatic device | Check CP-CPU interface. |
| : |  |  |
| 0E38 | An error has occurred accessing SIMATIC areas "Memory bit, output, timers, counters, input" with the function code FC 01 or FC 02: For example, input not available or attempt to read beyond the end of the area. | Check whether the addressed SIMATIC area exists and that no attempt was made to access beyond the end of the area. |
| 0E39 | An error has occurred accessing the SIMATIC "Data block" area with the function code FC 03, 04, 06, 16: Data block not available or too short. | Check if the addressed data block exists and is sufficiently long. |
| 0E3A | Error executing a write job with function codes FC 05, 15: Instance DB of the MODBUS instruction does not exist or is of insufficient length. | Check if the instance DB assigned in the parameters of the MODBUS communications instruction exists and whether it is of sufficient length. |
| 0E3B | Timeout (waiting for acknowledgement) in the execution of a write job by the Modbus communication instruction. | Check the connection configuration and the CP-CPU interface (SFB SEND); if necessary, reload the MODBUS communication instruction. |
| 0E3C | Illegal job with this driver. | Only SFB SEND, STATUS (CP 441-2 only) are permitted. |
| 0E50 | In the word-based SIMATIC timers/counters areas, the resulting residual bit number from the Modbus address is ≠ 0. | Only use MODBUS addresses which result in valid bit numbers. |
| 0E51 | The received Modbus address is outside the configured "from/to" areas. | Only use addresses as address information in the request message frame that have previously been defined in the configuration. |
| 0E52 | - A SIMATIC area limit was exceeded during an access attempt by the Modbus master system: Resulting DB number < 1 - Write access to an unreleased area (configuration) - Write access to the instance DB of the communication instruction | Access area limited to valid SIMATIC memory areas. |
| 0E53 | A SIMATIC area limit was exceeded during an access attempt by the Modbus master system:  For example, overflow from the formation of the resulting DB no. (> 65535) | Access area limited to valid SIMATIC memory areas. |
| 0E54 | Access beyond the configured area end or access beyond the SIMATIC area end. | Access area limited to valid SIMATIC memory areas. |
| 0E55 | Write access to this SIMATIC memory area is not allowed. | Write only to the SIMATIC memory bits, outputs data areas. |
| 0E56 | Data link operation not possible because the communication instruction is inactive. | Call the MODBUS communication instruction at cyclic intervals in the STEP 7 user program. If necessary, re-initialize the communication instruction. |
| 0E57 | An error has occurred executing the MODBUS function code in the communication instruction. | Analyze the exact cause. |
