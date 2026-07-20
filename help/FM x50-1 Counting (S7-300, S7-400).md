---
title: "FM x50-1 Counting (S7-300, S7-400)"
package: ProgFBFMx50_1V3enUS
topics: 10
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# FM x50-1 Counting (S7-300, S7-400)

This section contains information on the following topics:

- [CNT_CTRL (S7-300, S7-400)](#cnt_ctrl-s7-300-s7-400)
- [DIAG_INF (S7-300, S7-400)](#diag_inf-s7-300-s7-400)
- [CNT_CTL1 (S7-300, S7-400)](#cnt_ctl1-s7-300-s7-400)
- [CNT_CTL2 (S7-300, S7-400)](#cnt_ctl2-s7-300-s7-400)
- [Additional references for FM x50-1 Counter V3 (S7-300, S7-400)](#additional-references-for-fm-x50-1-counter-v3-s7-300-s7-400)

## CNT_CTRL (S7-300, S7-400)

### Description

The CNT_CTRL instruction is used to control the counting and measuring modes.

You need to use the [CNT_CTL1](#cnt_ctl1-s7-300-s7-400) instruction to change parameters in runtime or set and reset the outputs of the counter module.

### Operating principle

The CNT_CTRL instruction works only in a non-isochronous OB.  
In an isochronous OB, use the instruction [CNT_CTL1](#cnt_ctl1-s7-300-s7-400) or [CNT_CTL2](#cnt_ctl2-s7-300-s7-400).

The data needed for the CNT_CTRL instruction is stored in the [counter DB](#counter-data-block-s7-300-s7-400) in the CPU. The CNT_CTRL instruction cyclically transfers data from this DB to the counter module and fetches data from the counter module.

### Call

The CNT_CTRL instruction can be called once for each counter in the cycle or optionally in a time-controlled program. The call is not allowed in an event-driven interrupt program.

### Parameter

| Parameter | Declaration | Data type | Description | The user ... | The instruction ... |
| --- | --- | --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the counter data block | Enters this | Queries this |
| SW_GATE | INPUT | BOOL | Counter control bit SW gate (start/stop) | Sets and resets this | Queries this |
| GATE_STP | INPUT | BOOL | Counter control bit gate stop | Sets and resets this | Queries this |
| OT_ERR_A | INPUT | BOOL | Acknowledge operator error | Sets and resets this | Queries this |
| OT_ERR | OUTPUT | BOOL | Operator error occurred | Queries this | Sets and resets this |
| L_DIRECT | IN-OUT | BOOL | Trigger bit for direct loading of a counter | Sets this | Queries and resets this |
| L_PREPAR | IN-OUT | BOOL | Trigger bit for preparatory loading of a counter | Sets this | Queries and resets this |
| T_CMP_V1 | IN-OUT | BOOL | Transfer trigger bit for comparison value 1 | Sets this | Queries and resets this |
| T_CMP_V2 | IN-OUT | BOOL | Transfer trigger bit for comparison value 2 | Sets this | Queries and resets this |
| RES_SYNC | IN-OUT | BOOL | Delete synchronization status bit | Sets this | Queries and resets this |
| RES_ZERO | IN-OUT | BOOL | Delete zero crossing status bit | Sets this | Queries and resets this |

### Executing jobs

Initiate jobs for the counter module using the instruction parameters L_DIRECT, L_PREPAR, T_CMP_V1, T_CMP_V2, RES_SYNC, RES_ZERO, OT_ERR_A and GATE_STP.

Depending on the command, you need to enter the load value or a comparison value prior to the calling of the instruction in the counter DB.

A configured IN/OUT parameter (L_DIRECT, L_PREPAR, T_CMP_V1, T_CMP_V2, RES_SYNC and RES_ZERO) is deleted by the CNT_CTRL instruction upon completion of the command.

### Startup characteristics

As soon as the CNT_CTRL instruction detects a startup (CPU or FM startup), any pending command is deferred and the startup is first acknowledged. A command you have already initiated is not lost, but is not executed until the startup is completed.

### Reaction to errors

An operator error occurring during the call of the instruction is reported at the OT_ERR parameter. The error information can be read from the counter DB (OT_ERR_B tag). You can then use the OT_ERR_A parameter to acknowledge the operator error. No additional operator error is reported until you acknowledge the previous error.

## DIAG_INF (S7-300, S7-400)

### Description

If the trigger parameter is set (IN_DIAG = TRUE), the DIAG_INF instruction reads data record DS 1 from the counter module and makes it available in the [counter DB](#counter-data-block-s7-300-s7-400) (starting at DW 54).

### Operating principle

The data record is transferred using the RDSYSST instruction. The return code of this instruction (RET_VAL) is copied to the RET_VAL parameter of the DIAG_INF instruction. Once DIAG_INF instruction has been executed, the IN_DIAG trigger parameter is reset and the transfer is reported as completed.

### Call

The DIAG_INF instruction can be called in the cycle and in the interrupt program. However, calling it in a time-controlled program is not recommended.

### Parameter

| Parameter | Declaration | Data type | Description | The user ... | The instruction ... |
| --- | --- | --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the counter data block | Enters this | Queries this |
| RET_VAL | OUTPUT | INT | Return code of the instruction RDSYSST | Queries this | Enters this |
| IN_DIAG | IN-OUT | BOOL | Read trigger bit of diagnostics data record DS 1 | Sets and queries this | Resets this |

## CNT_CTL1 (S7-300, S7-400)

### Description

The CNT_CTL1 instruction is used to control the counting and measuring modes.

In addition to the functions in the CNT_CTRL instruction , the CNT_CTL1 instruction enables you to change parameters in runtime and to set and reset the outputs of the counter module.

### Operating principle

The data needed for the CNT_CTL1 instruction is stored in the [counter DB](#counter-data-block-s7-300-s7-400) in the CPU. The CNT_CTL1 instruction cyclically transfers data from this DB to the counter module and fetches data from the counter module.

### Call

The CNT_CTL1 instruction can be called once for each counter in the cycle or optionally in a time-controlled or an isochronous interrupt OB. The call is not allowed in an event-driven interrupt program.

### Parameter

| Parameter | Declaration | Data type | Description | The user ... | The instruction ... |
| --- | --- | --- | --- | --- | --- |
| DB_NO | INPUT | INT | Number of the counter data block | Enters this | Queries this |
| SW_GATE | INPUT | BOOL | Counter control bit SW gate (start/stop) | Sets and resets this | Queries this |
| GATE_STP | INPUT | BOOL | Counter control bit gate stop | Sets and resets this | Queries this |
| OT_ERR_A | INPUT | BOOL | Acknowledge operator error | Sets and resets this | Queries this |
| SET_DO0 | INPUT | BOOL | Set/Reset output DO0 | Sets and resets this | Queries this |
| SET_DO1 | INPUT | BOOL | Set/Reset output DO1 | Sets and resets this | Queries this |
| OT_ERR | OUTPUT | BOOL | Operator error occurred | Queries this | Sets and resets this |
| L_DIRECT   <sup>2)</sup>    <sup>3)</sup> | IN-OUT | BOOL | **Counting:**  Trigger bit for direct and preparatory loading of a counter | Sets this | Queries and resets this |
| **Measuring:**  Must NOT be set | **-** | Queries and resets this |  |  |  |
| L_PREPAR   <sup>2)</sup>    <sup>3)</sup> | IN-OUT | BOOL | **Counting:**  Trigger bit for preparatory loading of a counter | Sets this | Queries and resets this |
| **Measuring:** Transfer low limit | Sets this | Queries and resets this |  |  |  |
| T_CMP_V1   <sup>2)</sup> | IN-OUT | BOOL | **Counting:** Transfer trigger bit for comparison value 1 | Sets this | Queries and resets this |
| **Measuring:** Transfer high limit | Sets this | Queries and resets this |  |  |  |
| T_CMP_V2   <sup>2)</sup> | IN-OUT | BOOL | **Counting:**  Transfer trigger bit for comparison value 2 | Sets this | Queries and resets this |
| **Measuring:**  Update time | Sets this | Queries and resets this |  |  |  |
| C_DOPARA   <sup>1)</sup> | IN-OUT | BOOL | Trigger bit for parameter change | Sets this | Queries and resets this |
| RES_SYNC | IN-OUT | BOOL | Delete synchronization status bit | Sets this | Queries and resets this |
| RES_ZERO | IN-OUT | BOOL | Reset status bits for zero pass, overflow, underflow and comparator or measurement end | Sets this | Queries and resets this |
| <sup>1)</sup> You may not set this parameter simultaneously with one of the L_DIRECT, L_PREPAR, T_CMP_V1 or T_CMP_V2 parameters.   <sup>2)</sup> You may not set these parameters simultaneously with the C_DOPARA parameter.   <sup>3)</sup> You may not set these parameter simultaneously. |  |  |  |  |  |

### Executing jobs

Initiate jobs for FM x50‑1 using the instruction parameters L_DIRECT, L_PREPAR, T_CMP_V1, T_CMP_V2, C_DOPARA, RES_SYNC, RES_ZERO and OT_ERR_A.

Depending on the command, enter the corresponding values (load value, comparison value, low limit, high limit and the update time) in the counter DB prior to calling the instruction.

See also:

- [Value transfer using CNT_CTL1](#value-transfer-using-cnt_ctl1-s7-300-s7-400)
- [DB parameters for value transfer (count modes)](#db-parameters-for-transferring-values-counting-modes-s7-300-s7-400)
- [DB parameters for value transfer (count modes)](#db-parameters-for-transferring-values-measuring-modes-s7-300-s7-400)

The CNT_CTL1 instruction deletes an IN-OUT parameter (L_DIRECT, L_PREPAR, T_CMP_V1, T_CMP_V2, C_DOPARA, RES_SYNC and RES_ZERO) when the command is completed. This enables you to recognize that the command has been completed by FM x50‑1. If necessary, you can let this information be known to your user program.

### Startup characteristics

As soon as the CNT_CTL1 instruction detects a startup (CPU or FM startup), any pending command is deferred and the startup is first acknowledged. A command you have already initiated is not lost, but is not executed until the startup is completed.

### Reaction to error

An operator error occurring during the call of the instruction is reported at the OT_ERR parameter. The error information can be read from the counter DB (OT_ERR_B tag). You can then use the OT_ERR_A parameter to acknowledge the operator error. No additional operator error is reported until you acknowledge the previous error.

## CNT_CTL2 (S7-300, S7-400)

### Description

The function of the CNT_CTL2 instruction is basically the same as the [CNT_CTL1](#cnt_ctl1-s7-300-s7-400) instruction.

The differences compared to the CNT_CTL1 instruction are discussed in the following section.

### Operating principle

The CNT_CTL2 instruction is particularly suitable for applications involving rapid, successive transfer of the same command (for example, load comparison value) to FM x50‑1. At the very best, the CNT_CTL1 instruction lets you initiate new jobs at every fifth PROFIBUS DP cycle, while the CNT_CTL2 instruction can handle this at every second PROFIBUS DP cycle.

The instruction is ready to process a command as soon as the corresponding trigger bit is set to 0. The completion of a command is not displayed separately.

If a communication problem or a data or operator error occurs, this can no longer be attributed to a specific command. For this reason, the instruction interrupts command execution and generates an **ID 90** operator error requiring acknowledgment. Once you acknowledged the error by setting the OT_ERR_A parameter, the instruction continues to process any jobs pending.

The acknowledgment of an operator error is successfully completed as soon as OT_ERR parameter is reset. You should keep the OT_ERR_A parameter set until this happens to ensure reliable acknowledgment. You should not initiate additional jobs until the acknowledgment is successful.

> **Note**
>
> It is not allowed to initiate several value transfers simultaneously with the CNT_CTL2 instruction.

### Call

The CNT_CTL2 instruction works only in an isochronous OB.

If the CNT_CTL2 instruction is called in a non-isochronous OB, it generates an **ID 91** operator error. This would also prevent data communication with FM x50‑1.

## Additional references for FM x50-1 Counter V3 (S7-300, S7-400)

This section contains information on the following topics:

- [Counter data block (S7-300, S7-400)](#counter-data-block-s7-300-s7-400)
- [Value transfer using CNT_CTL1 (S7-300, S7-400)](#value-transfer-using-cnt_ctl1-s7-300-s7-400)
- [DB parameters for transferring values (counting modes) (S7-300, S7-400)](#db-parameters-for-transferring-values-counting-modes-s7-300-s7-400)
- [DB parameters for transferring values (measuring modes) (S7-300, S7-400)](#db-parameters-for-transferring-values-measuring-modes-s7-300-s7-400)

### Counter data block (S7-300, S7-400)

#### Function

The counter DB is the data interface between the user program and FM x50‑1. It contains and applies all data necessary to control and operate the module.

Before the parameter assignment of the module, you must provide the following valid data to the counter DB.

- Module address (address 6.0)
- Channel start address (address 8.0)
- Length of the user data interface (address 12.0)

The counter module manual contains an example of how you can implement the transfer of the module address, the channel address, and the length of the user data to the counter DB in OB 100.

Alternatively, you can also have the module address entered automatically using the "Enter module address in DB" function in the device configuration of FM x50-1.

#### Configuration

The counter DB is divided into different areas:

| Channel DB |  |
| --- | --- |
| Instruction parameters, addresses |  |
| Transfer area for values to be written |  |
| Control interface |  |
| Transfer area for values to be read |  |
| Error numbers |  |
| Feedback interface |  |
| Parameters for FM 450‑1 |  |
| Diagnostics data |  |

#### Contents

The table below shows the contents of the counter DB.

> **Note**
>
> You may not change any data not listed in this table.

| Address | Tag | Data type | Initial value | Comment |  |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  | Counting  FM 350‑1 / FM 450‑1 | Measuring FM 350‑1 |
| **Instruction parameters, addresses** |  |  |  |  |  |
| 0.0 | AR1_BUFFER | DWORD | DW#16#0 | AR1 Buffer | AR1 Buffer |
| 4.0 | FP | BYTE | B#16#0 | Flag byte | Flag byte |
| 5.0 | RESERVED | BYTE | B#16#0 | Reserved | Reserved |
| 6.0 | MOD_ADR | WORD | W#16#0 | Module address | Module address |
| 8.0 | CH_ADR | DWORD | DW#16#0 | Channel address | Channel address |
| 12.0 | U_D_LGTH | BYTE | B#16#0 | Length user data | Length user data |
| 13.0 | A_BYTE_0 | BYTE | B#16#0 | Reserved | Reserved |
| **Transfer area for values to be written** |  |  |  |  |  |
| 14.0 | LOAD_VAL <sup>1)</sup> | DINT | L#0 | New load value  (write user) | Low limit  (write user) |
| 18.0 | CMP_V1 <sup>1)</sup> | DINT | L#0 | New comparison value 1  (write user) | High limit  (write user) |
| 22.0 | CMP_V2 <sup>1)</sup> | DINT | L#0 | New comparison value 2  (write user) | Update time (write user) |
| **Control interface** |  |  |  |  |  |
| 26.0 | A_BIT0_0 | BOOL | FALSE | Reserved | Reserved |
| 26.1 | TFB | BOOL | FALSE | Reserved / test free | Reserved |
| 26.2 | A_BIT0_2 | BOOL | FALSE | Reserved | Reserved |
| 26.3 | A_BIT0_3 | BOOL | FALSE | Reserved | Reserved |
| 26.4 | A_BIT0_4 | BOOL | FALSE | Reserved | Reserved |
| 26.5 | A_BIT0_5 | BOOL | FALSE | Reserved | Reserved |
| 26.6 | A_BIT0_6 | BOOL | FALSE | Reserved | Reserved |
| 26.7 | A_BIT0_7 | BOOL | FALSE | Reserved | Reserved |
| 27.0 | ENSET_UP <sup>1)</sup> | BOOL | FALSE | Enable setting in forward direction  (write user) | - |
| 27.1 | ENSET_DN <sup>1)</sup> | BOOL | FALSE | Enable setting in backward direction  (write user) | - |
| 27.2 | A_BIT1_2 | BOOL | FALSE | Reserved | Reserved |
| 27.3 | A_BIT1_3 | BOOL | FALSE | Reserved | Reserved |
| 27.4 | A_BIT1_4 | BOOL | FALSE | Reserved | Reserved |
| 27.5 | A_BIT1_5 | BOOL | FALSE | Reserved | Reserved |
| 27.6 | A_BIT1_6 | BOOL | FALSE | Reserved | Reserved |
| 27.7 | A_BIT1_7 | BOOL | FALSE | Reserved | Reserved |
| 28.0 | CTRL_DO0 <sup>1)</sup> | BOOL | FALSE | Enable digital output DO0  (write user) | Enable digital output DO0  (write user) |
| 28.1 | CTRL_DO1 <sup>1)</sup> | BOOL | FALSE | Enable digital output DO1  (write user) | Enable digital output DO1  (write user) |
| 28.2 | A_BIT2_2 | BOOL | FALSE | Reserved | Reserved |
| 28.3 | A_BIT2_3 | BOOL | FALSE | Reserved | Reserved |
| 28.4 | A_BIT2_4 | BOOL | FALSE | Reserved | Reserved |
| 28.5 | A_BIT2_5 | BOOL | FALSE | Reserved | Reserved |
| 28.6 | A_BIT2_6 | BOOL | FALSE | Reserved | Reserved |
| 28.7 | A_BIT2_7 | BOOL | FALSE | Reserved | Reserved |
| 29.0 | A_BIT3_0 | BOOL | FALSE | Reserved | Reserved |
| 29.1 | A_BIT3_1 | BOOL | FALSE | Reserved | Reserved |
| 29.2 | A_BIT3_2 | BOOL | FALSE | Reserved | Reserved |
| 29.3 | A_BIT3_3 | BOOL | FALSE | Reserved | Reserved |
| 29.4 | A_BIT3_4 | BOOL | FALSE | Reserved | Reserved |
| 29.5 | A_BIT3_5 | BOOL | FALSE | Reserved | Reserved |
| 29.6 | A_BIT3_6 | BOOL | FALSE | Reserved | Reserved |
| 29.7 | A_BIT3_7 | BOOL | FALSE | Reserved | Reserved |
| **Transfer area for values to be read** |  |  |  |  |  |
| 30.0 | LATCH_LOAD <sup>1)</sup> | DINT | L#0 | Current load or latch value (read user) | Current measured value (read user) |
| 34.0 | ACT_CNTV <sup>1)</sup> | DINT | L#0 | Current count value  (read user) | Current count value  (read user) |
| Error numbers |  |  |  |  |  |
| 38.0 | DA_ERR_W <sup>1)</sup> | WORD | W#16#0 | Data error word  (read user) | Data error word  (read user) |
| 40.0 | OT_ERR_B <sup>1)</sup> | BYTE | B#16#0 | Operation error byte  (read user) | Operation error byte  (read user) |
| **Feedback interface** |  |  |  |  |  |
| 41.0 | E_BIT0_0 | BOOL | FALSE | Reserved | Reserved |
| 41.1 | STS_TFB | BOOL | FALSE | Reserved / status test free | Reserved |
| 41.2 | DIAG | BOOL | FALSE | FM 350-1: Diagnostic event (read user)  FM 450-1: Reserved | Diagnostic event (read user) |
| 41.3 | E_BIT0_3 | BOOL | FALSE | Reserved | Reserved |
| 41.4 | DATA_ERR <sup>1)</sup> | BOOL | FALSE | Data error bit  (read user) | Data error bit  (read user) |
| 41.5 | E_BIT0_5 | BOOL | FALSE | Reserved | Reserved |
| 41.6 | E_BIT0_6 | BOOL | FALSE | Reserved | Reserved |
| 41.7 | PARA <sup>1)</sup> | BOOL | FALSE | Module parameters assigned  (read user) | Module parameters assigned  (read user) |
| 42.0 | E_BYTE_0 | BYTE | B#16#0 | Reserved | Reserved |
| 43.0 | STS_RUN <sup>1)</sup> | BOOL | FALSE | Status counter running  (read user)  This bit corresponds to bit 2<sup>0</sup> of the counter. 0 = LED CR is off 1 = LED CR is lit | Status counter running  (read user)  This bit corresponds to bit 2<sup>0</sup> of the counter. 0 = LED CR is off 1 = LED CR is lit |
| 43.1 | STS_DIR <sup>1)</sup> | BOOL | FALSE | Status count direction  (read user) | Status count direction  (read user) |
| 43.2 | STS_ZERO <sup>1)</sup> | BOOL | FALSE | Status zero-crossing  (read user) | End of measurement  (read user) |
| 43.3 | STS_OFLW <sup>1)</sup> | BOOL | FALSE | Status overflow  (read user) | Status overflow  (read user) |
| 43.4 | STS_UFLW <sup>1)</sup> | BOOL | FALSE | Status underflow  (read user) | Status underflow  (read user) |
| 43.5 | STS_SYNC <sup>1)</sup> | BOOL | FALSE | Status counter synchronized (read user) | - |
| 43.6 | STS_GATE <sup>1)</sup> | BOOL | FALSE | Status internal gate  (read user) | Status internal gate  (read user) |
| 43.7 | STS_SW_G <sup>1)</sup> | BOOL | FALSE | Status SW gate  (read user) | Status SW gate  (read user) |
| 44.0 | STS_SET <sup>1)</sup> | BOOL | FALSE | Status digital input SET  (read user) | Status digital input DI Set  (read user) |
| 44.1 | STS_LATCH <sup>1)</sup> | BOOL | FALSE | New latch value (only in isochronous mode) / Reserved | - |
| 44.2 | STS_STA <sup>1)</sup> | BOOL | FALSE | Status digital input START (read user) | Status digital input DI Start (read user) |
| 44.3 | STS_STP <sup>1)</sup> | BOOL | FALSE | Status digital input STOP (read user) | Status digital input DI Stop (read user) |
| 44.4 | STS_CMP1 <sup>1)</sup> | BOOL | FALSE | Status output comparison value 1 (read user) | Status output comparison value 1 (read user) |
| 44.5 | STS_CMP2 <sup>1)</sup> | BOOL | FALSE | Status output comparison value 2 (read user) | Status output comparison value 2 (read user) |
| 44.6 | STS_COMP1 <sup>1)</sup> | BOOL | FALSE | Saved status of comparator 1 / Reserved | - |
| 44.7 | STS_COMP2 <sup>1)</sup> | BOOL | FALSE | Saved status of comparator 2 / Reserved | - |
| 45.0 | E_BIT3_0 | BOOL | FALSE | Reserved | Reserved |
| 45.1 | E_BIT3_1 | BOOL | FALSE | Reserved | Reserved |
| 45.2 | E_BIT3_2 | BOOL | FALSE | Reserved | Reserved |
| 45.3 | E_BIT3_3 | BOOL | FALSE | Reserved | Reserved |
| 45.4 | E_BIT3_4 | BOOL | FALSE | Reserved | Reserved |
| 45.5 | E_BIT3_5 | BOOL | FALSE | Reserved | Reserved |
| 45.6 | E_BIT3_6 | BOOL | FALSE | Reserved | Reserved |
| 45.7 | E_BIT3_7 | BOOL | FALSE | Reserved | Reserved |
| **Parameters for**  **FM 450‑1** |  |  |  |  |  |
| 46.0 | ACT_CMP1 <sup>1)</sup> | DINT | L#0 | Reserved / Current comparison value 1 (read user) | Reserved |
| 50.0 | ACT_CMP2 <sup>1)</sup> | DINT | L#0 | Reserved / Current comparison value 2 (read user) | Reserved |
| **The following diagnostic information is entered by the**  **DIAG_INF**  **instruction** |  |  |  |  |  |
| 54.0 | MDL_DEFECT | BOOL | FALSE | Module fault | Module fault |
| 54.1 | INT_FAULT | BOOL | FALSE | Internal error | Internal error |
| 54.2 | EXT_FAULT | BOOL | FALSE | External error | External error |
| 54.3 | PNT_INFO | BOOL | FALSE | Channel errors (breakdown from DW 58) | Channel errors (breakdown from DW 58) |
| 54.4 | EXT_VOLTAGE | BOOL | FALSE | Auxiliary voltage fault | Auxiliary voltage fault |
| 54.5 | FLD_CNNCTR | BOOL | FALSE | Front connector | Front connector |
| 54.6 | NO_CONFIG | BOOL | FALSE | No parameter assignment | No parameter assignment |
| 54.7 | CONFIG_ERR | BOOL | FALSE | Faulty parameters | Faulty parameters |
| 55.0 | MDL_TYPE | BYTE | B#16#0 | Module type | Module type |
| 56.0 | SUB_MDL_ERR | BOOL | FALSE | Wrong/missing interface module | Wrong/missing interface module |
| 56.1 | COMM_FAULT | BOOL | FALSE | Communication error | Communication error |
| 56.2 | MDL_STOP | BOOL | FALSE | RUN/STOP operating mode display | RUN/STOP operating mode display |
| 56.3 | WTCH_DOG_FAULT | BOOL | FALSE | Watchdog (FM) | Watchdog (FM) |
| 56.4 | INT_PS_FLT | BOOL | FALSE | Internal power supply fault | Internal power supply fault |
| 56.5 | PRIM_BATT_FLT | BOOL | FALSE | Battery monitoring | Battery monitoring |
| 56.6 | BCKUP_BATT_FLT | BOOL | FALSE | Bad buffer | Bad buffer |
| 56.7 | RESERVED_2 | BOOL | FALSE | Reserved | Reserved |
| 57.0 | RACK_FLT | BOOL | FALSE | Rack fault | Rack fault |
| 57.1 | PROC_FLT | BOOL | FALSE | CPU fault | CPU fault |
| 57.2 | EPROM_FLT | BOOL | FALSE | EPROM fault | EPROM fault |
| 57.3 | RAM_FLT | BOOL | FALSE | RAM fault | RAM fault |
| 57.4 | ADU_FLT | BOOL | FALSE | ADU fault | ADU fault |
| 57.5 | FUSE_FLT | BOOL | FALSE | Fuse | Fuse |
| 57.6 | HW_INTR_FLT | BOOL | FALSE | Hardware interrupt lost | Hardware interrupt lost |
| 57.7 | RESERVED_3 | BOOL | FALSE | Reserved | Reserved |
| 58.0 | CH_TYPE | BYTE | B#16#0 | Channel type | Channel type |
| 59.0 | LGTH_DIA | BYTE | B#16#0 | Length of the diagnostic data per channel | Length of the diagnostic data per channel |
| 60.0 | CH_NO | BYTE | B#16#0 | Number of channels | Number of channels |
| 61.0 | GRP_ERR1 | BOOL | FALSE | Group error channel 1 | Group error channel 1 |
| 61.1 | GRP_ERR2 | BOOL | FALSE | Reserved / Group error channel 2 | Not used with FM 350 |
| 61.2 | D_BIT7_2 | BOOL | FALSE | DS1 byte 7 bit 2 | DS1 byte 7 bit 2 |
| 61.3 | D_BIT7_3 | BOOL | FALSE | DS1 byte 7 bit 3 | DS1 byte 7 bit 3 |
| 61.4 | D_BIT7_4 | BOOL | FALSE | DS1 byte 7 bit 4 | DS1 byte 7 bit 4 |
| 61.5 | D_BIT7_5 | BOOL | FALSE | DS1 byte 7 bit 5 | DS1 byte 7 bit 5 |
| 61.6 | D_BIT7_6 | BOOL | FALSE | DS1 byte 7 bit 6 | DS1 byte 7 bit 6 |
| 61.7 | D_BIT7_7 | BOOL | FALSE | DS1 byte 7 bit 7 | DS1 byte 7 bit 7 |
| 62.0 | CH1_SIGA | BOOL | FALSE | Channel 1, error signal A | Channel 1, error signal A |
| 62.1 | CH1_SIGB | BOOL | FALSE | Channel 1, error signal B | Channel 1, error signal B |
| 62.2 | CH1_SIGZ | BOOL | FALSE | Channel 1, error zero signal | Channel 1, error zero signal |
| 62.3 | CH1_BETW | BOOL | FALSE | Channel 1, error between channels | Channel 1, error between channels |
| 62.4 | CH1_5V2 | BOOL | FALSE | Channel 1, error sensor power supply 5.2V | Channel 1, error sensor power supply 5.2V |
| 62.5 | D_BIT8_5 | BOOL | FALSE | DS1 byte 8 bit 5 | DS1 byte 8 bit 5 |
| 62.6 | D_BIT8_6 | BOOL | FALSE | DS1 byte 8 bit 6 | DS1 byte 8 bit 6 |
| 62.7 | D_BIT8_7 | BOOL | FALSE | DS1 byte 8 bit 7 | DS1 byte 8 bit 7 |
| 63.0 | D_BYTE9 | BYTE | B#16#0 | DS1 byte 9 | DS1 byte 9 |
| 64.0 | CH2_SIGA | BOOL | FALSE | Reserved / Channel 2, error signal A | Reserved |
| 64.1 | CH2_SIGB | BOOL | FALSE | Reserved / Channel 2, error signal B | Reserved |
| 64.2 | CH2_SIGZ | BOOL | FALSE | Reserved / Channel 2, error zero signal | Reserved |
| 64.3 | CH2_BETW | BOOL | FALSE | Reserved / Channel 2, error between channels | Reserved |
| 64.4 | CH2_5V2 | BOOL | FALSE | Reserved / Channel 2, error sensor power supply 5.2V | Reserved |
| 64.5 | D_BIT10_5 | BOOL | FALSE | DS1 byte 10 bit 5 | DS1 byte 10 bit 5 |
| 64.6 | D_BIT10_6 | BOOL | FALSE | DS1 byte 10 bit 6 | DS1 byte 10 bit 6 |
| 64.7 | D_BIT10_7 | BOOL | FALSE | DS1 byte 10 bit 7 | DS1 byte 10 bit 7 |
| 65.0 | D_BYTE11 | BYTE | B#16#0 | DS1 byte 11 | DS1 byte 11 |
| 66.0 | D_BYTE12 | BYTE | B#16#0 | DS1 byte 12 | DS1 byte 12 |
| 67.0 | D_BYTE13 | BYTE | B#16#0 | DS1 byte 13 | DS1 byte 13 |
| 68.0 | D_BYTE14 | BYTE | B#16#0 | DS1 byte 14 | DS1 byte 14 |
| 69.0 | D_BYTE15 | BYTE | B#16#0 | DS1 byte 15 | DS1 byte 15 |
| <sup>1)</sup> Tags in the DB that you can/must input or read when working with the FM x50-1 |  |  |  |  |  |

### Value transfer using CNT_CTL1 (S7-300, S7-400)

#### Value transfer

Transfer the operating mode-specific values by setting these instruction parameters:

| Mode | Instruction parameters |
| --- | --- |
| Counting | L_DIRECT, L_PREPAR, T_CMP_V1, T_CMP_V2, C_DOPARA |
| Measuring | L_PREPAR, T_CMP_V1, T_CMP_V2, C_DOPARA |

You must first place the values to be transferred in the DB beforehand.

See also:

- [DB parameters for value transfer (count modes)](#db-parameters-for-transferring-values-counting-modes-s7-300-s7-400)
- [DB parameters for value transfer (count modes)](#db-parameters-for-transferring-values-measuring-modes-s7-300-s7-400)

You can transfer several values at the same time:

| In operating mode ... | ... You can transfer at the same time |  |
| --- | --- | --- |
| Counting | Load value | (DB parameter LOAD_VAL) |
| Comparison value 1 | (DB parameter CMP_V1) |  |
| Comparison value 2 | (DB parameter CMP_V2) |  |
| Measuring | Low limit | (DB parameter LOAD_VAL) |
| High limit | (DB parameter CMP_V1) |  |
| Updating time | (DB parameter CMP_V2) |  |

If an incorrect value is transferred, you have to acknowledge this operator error with OT_ERR_A before FM 350‑1 can accept further values. You should then correct the value rejected with the operator error and transfer it again.

> **Note**
>
> If you use the L_DIRECT, L_PREPAR, T_CMP_V1 or T_CMP_V2 instruction parameters to load the LOAD_VAL, CMP_V1 or CMP_V2 values, you cannot use the C_DOPARA instruction parameter at the same time to reconfigure parameters.
>
> This would cause an OT_ERR operating error requiring acknowledgment with OT_ERR_A.

#### Time required to transfer values

Refer to the table below for the time required to transfer values:

| Using FM 350‑1 |  | Time requirement |
| --- | --- | --- |
| Centralized |  | At least 4 OB 1 cycles |
| Distributed (non-isochrone mode) |  | At least 5 PROFIBUS DP cycles |
| Distributed (isochrone mode) |  |  |
| - At transmission of only one value |  | - 5 PROFIBUS DP cycles |
| - At simultaneous initiation of the transmission of several values |  |  |
|  | - For the 1st value: - For the 2nd value: - For the 3rd value: | - 5 PROFIBUS DP cycles after initiation - 6 PROFIBUS DP cycles after initiation - 7 PROFIBUS DP cycles after initiation |

### DB parameters for transferring values (counting modes) (S7-300, S7-400)

#### Preparation

Before calling the [CNT_CTRL](#cnt_ctrl-s7-300-s7-400), [CNT_CTL1](#cnt_ctl1-s7-300-s7-400) or [CNT_CTL2](#cnt_ctl2-s7-300-s7-400) instruction, you need to write the following valid data to the data block:

- Module address (DB address 6.0)
- Channel start address (DB address 8.0)
- Length of the user data interface (DB address 12.0)

These data should be transferred to the DB in OB 100 at every startup.

#### DB parameters for transferring values (counting modes)

The following table shows the DB area to which you transfer the LOAD_VAL, CMP_V1 and CMP_V2 parameters.

Parameter LOAD_VAL (bytes 14 to 17) has two meanings:

- If you set the L_DIRECT or L_PREPAR instruction parameter, LOAD_VAL is interpreted as a load value.
- If you set instruction parameter C_DOPARA, you can use byte 14 to define the characteristics of outputs DO0 and DO1. Bytes 15 and 16 are interpreted as hysteresis and pulse duration.

You can set only one of the L_DIRECT, L_PREPAR and C_DOPARA instruction parameters at any time.

| DB address | Parameters | Data type | Meaning |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 14.0 | LOAD_VAL | DINT | Load value; direct and preparatory loading with instruction parameter L_DIRECT Load value; preparatory loading with instruction parameter L_PREPAR |  |  |  |  |
| Characteristics of the DO0 and DO1 outputs, the hysteresis and the pulse duration; defined with the C_DOPARA instruction parameter: |  |  |  |  |  |  |  |
| **Bit 3** | **Bit 2** | **Bit 1** | **Bit 0** | **Reaction of output DO0** |  |  |  |
| x | 0 | 0 | 0 | Inactive |  |  |  |
| x | 0 | 0 | 1 | Active from the comparison value to high limit |  |  |  |
| x | 0 | 1 | 0 | Active from the comparison value to low limit |  |  |  |
| x | 0 | 1 | 1 | Active on reaching the comparison value for pulse duration (up/down) |  |  |  |
| x | 1 | 0 | 0 | Active on reaching the comparison value for pulse duration (up) |  |  |  |
| x | 1 | 0 | 1 | Active on reaching the comparison value for pulse duration (down) |  |  |  |
| **Bit 7** | **Bit 6** | **Bit 5** | **Bit 4** | **Characteristics of output DO1** |  |  |  |
| x | 0 | 0 | 0 | Inactive |  |  |  |
| x | 0 | 0 | 1 | Active from the comparison value to high limit |  |  |  |
| x | 0 | 1 | 0 | Active from the comparison value to low limit |  |  |  |
| x | 0 | 1 | 1 | Active on reaching the comparison value for pulse duration (up/down) |  |  |  |
| x | 1 | 0 | 0 | Active on reaching the comparison value of the up count pulse width |  |  |  |
| x | 1 | 0 | 1 | Active on reaching the comparison value of the down count pulse width |  |  |  |
| x | 1 | 1 | 0 | Switch at comparison values |  |  |  |
| 15.0 | Hysteresis (value range 0 to 255) |  |  |  |  |  |  |
| 16.0 | Pulse duration (value range 0 to 250) |  |  |  |  |  |  |
| 17.0 | Reserve = 0 |  |  |  |  |  |  |
| 18.0 | CMP_V1 | DINT | Comparison value 1; load with the T_CMP_V1 instruction parameter |  |  |  |  |
| 22.0 | CMP_V2 | DINT | Comparison value 2; load with the T_CMP_V2 instruction parameter |  |  |  |  |
| x = irrelevant |  |  |  |  |  |  |  |

### DB parameters for transferring values (measuring modes) (S7-300, S7-400)

#### Preparation

Before calling the [CNT_CTRL](#cnt_ctrl-s7-300-s7-400), [CNT_CTL1](#cnt_ctl1-s7-300-s7-400) or [CNT_CTL2](#cnt_ctl2-s7-300-s7-400) instruction, you need to write the following valid data to the data block:

- Module address (DB address 6.0)
- Channel start address (DB address 8.0)
- Length of the user data interface (DB address 12.0)

These data should be transferred to the DB in OB 100 at every startup.

#### DB parameters for transferring values (measuring modes)

The following table shows the DB area to which you transfer the LOAD_VAL, CMP_V1 and CMP_V2 parameters.

Parameter LOAD_VAL (bytes 14 to 17) has two meanings:

- If you set the L_PREPAR instruction parameter, LOAD_VAL is interpreted as a low limit.
- If you set the C_DOPARA instruction parameter, you can use byte 14 to specify the characteristics of output DO0.

You can set only one of the L_PREPAR and C_DOPARA instruction parameters at any time.

| DB address | Parameters | Data type | Meaning |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| 14.0 | LOAD_VAL | DINT | Low limit; load with the L_PREPAR instruction parameter |  |  |  |
| Characteristics of DO0; specify in the C_DOPARA instruction parameter |  |  |  |  |  |  |
| **Bits 2 to 7** | **Bit 1** | **Bit 0** | **Reaction of output DO0** |  |  |  |
| Irrelevant | 0 | 0 | No comparison |  |  |  |
| Irrelevant | 0 | 1 | Active outside the limits |  |  |  |
| Irrelevant | 1 | 0 | Active upon violation of low limit |  |  |  |
| Irrelevant | 1 | 1 | Active upon violation of high limit |  |  |  |
| 15.0 | Reserve = 0 |  |  |  |  |  |
| 16.0 | Reserve = 0 |  |  |  |  |  |
| 17.0 | Reserve = 0 |  |  |  |  |  |
| 18.0 | CMP_V1 | DINT | High limit; load with the T_CMP_V1 instruction parameter |  |  |  |
| 22.0 | CMP_V2 | DINT | Update time; load with the T_CMP_V2 instruction parameter |  |  |  |
