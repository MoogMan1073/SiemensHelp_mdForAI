---
title: "FM 355-2 Temperature Control (S7-300, S7-400)"
package: ProgFBFM3552enUS
topics: 42
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# FM 355-2 Temperature Control (S7-300, S7-400)

This section contains information on the following topics:

- [FMT_PID (S7-300, S7-400)](#fmt_pid-s7-300-s7-400)
- [FMT_PAR (S7-300, S7-400)](#fmt_par-s7-300-s7-400)
- [FMT_DS1 (S7-300, S7-400)](#fmt_ds1-s7-300-s7-400)
- [FMT_TUN (S7-300, S7-400)](#fmt_tun-s7-300-s7-400)
- [FMT_PV (S7-300, S7-400)](#fmt_pv-s7-300-s7-400)
- [FMT_CJ_T (S7-300, S7-400)](#fmt_cj_t-s7-300-s7-400)

## FMT_PID (S7-300, S7-400)

This section contains information on the following topics:

- [Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
- [Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
- [Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
- [Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
- [In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
- [Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
- [Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
- [Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
- [Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
- [Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
- [Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
- [Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Description FMT_PID (S7-300, S7-400)

During operation, the instruction FMT_PID is used to:

- Transfer operating parameters to FM 355-2
- Transfer controlller parameters to FM 355-2
- Read process values from FM 355-2

Operating parameters are all static variables of instance DB in the structure OP.

Controller parameters are all static variables of instance DB in the structure PAR.

Process values are all static variables of instance DB in the structure OUT.

The data required for the FMT_PID are stored in an instance DB on the CPU. The FMT_PID is program controlled to read data from the FM 355-2 and to write data to the FM 355-2.

#### Call

The instruction FMT_PID has to be called in the same OB as all the other instructions that access the same FM 355-2.

FMT_PID is called in the cyclic interrupt OB. It requires an initialization routine that is started by setting the COM_RST = TRUE parameter in the start-up of the CPU. After the initialization routine, FMT_PID sets the parameter COM_RST to FALSE.

If you call the instruction FMT_PID as a multiple instance DB, no commissioning interface is available. In this case you must commission the FM 355-2 via a watch table or with the instruction FMT_TUN.

#### Calling in Distributed I/O

The following has to be noted in the case of a distributed structure and simultaneous calling of FMT_PID and FMT_TUN:

- It is not permitted to set LOAD_OP simultaneously with FMT_PID and FMT_TUN.
- It is not permitted to set READ_OUT simultaneously with FMT_PID and FMT_TUN.

Reason: Both FBs access FM 355-2 via the same data records.

You must therefore ensure that only one of the two FBs reads or writes a data record at the same time.

#### Start-up

During CPU start-up and during CPU STOP-RUN transition, the parameters on the FM 355-2 are overwritten with the parameters from the SDB of the CPU.

#### Responses in the event of an error

The RET_VALU output parameter contains the 2nd and 3rd bytes of the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated if the READ_PAR and LOAD_PAR parameters are not reset.

When the instruction FMT_PID is called, an I/O access error can occur if the FM 355-2 is not plugged or is not supplied with voltage. In this case the CPU goes into STOP, if no OB 122 is loaded in the CPU.

If an error occurs when reading/writing a data set, QMOD_F and QCH_F must be set. In the case of parameter assignment errors, QPAR_F and QCH_F are set.

---

**See also**

[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Mode of operation FMT_PID (S7-300, S7-400)

#### Effect of parameters LOAD_OP, READ_OUT, LOAD_PAR and READ_PAR

In the initialization routine FMT_PID reads the parameters from the system data and stores them in its instance DB. Instance DB and system data are synchronized.

The following figure shows how the function of the instruction is influenced by the parameters LOAD_OP, READ_OUT, LOAD_PAR and READ_PAR.

![Effect of parameters LOAD_OP, READ_OUT, LOAD_PAR and READ_PAR](images/24541674763_DV_resource.Stream@PNG-en-US.png)

The following table contains detailed information depending on the values of the parameters.

| Parameters | TRUE | FALSE |
| --- | --- | --- |
| LOAD_OP | The static variables of the structure OP are transferred cyclically FM 355-2 with the instructions WRREC and RDREC.  The output parameters are read from the FM 355-2. | The static variables of the structure OP are transferred via the input and output areas of the module. This is not possible if two instances of the instruction FMT_PID access the same channel number of a module. |
| READ_VAR is set to TRUE | READ_VAR is not changed |  |
| In the following situations LOAD_OP is automatically TRUE:  - If you have set one of the following parameters: TUN_ST, TUN_CST, SAVE_PAR,UNDO_PAR and LOAD_PID - If you modify TUN_ON - If you modify the setpoint SP_RE. |  |  |
| Longer run time | Shorter run time |  |
| The values are effective after a cycle of the CPU or FM. The longer cycle is decisive. | A maximum of 3 to 4 cycles of the CPU or FM are required until the values are effective. The longer cycle is decisive |  |
| All operating parameters are transferred | Only the operating parameters up to and including LMN_DN are transferred.  In automatic mode, only the setpoint SP_RE is transferred.  In manual mode, only the manual manipulated value LMN_RE is transferred. |  |
| READ_OUT | The static variables of the structure OUT are read cyclically from FM 355-2 with the instructions WRREC and RDREC and stored in the structure OUT. | The static variables of the structure OUT are transferred via the input and output areas of the module and stored in the structure OUT. |
| In the following situation READ_OUT is automatically TRUE:  - During an optimization QTUN_ON = TRUE - When you modify the setpoint SP_RE | This is not possible if two instances of the instruction FMT_PID access the same channel number of a module. |  |
| Longer processing time | Shorter processing time |  |
| All parameters are read from FM 355 | The following parameters are **not** read from FM 355  - SP (setpoint from the FM) - ER (error signal) - DISV (disturbance variable) - LMN_A - LMN_B - PHASE - STATUS_H - STATUS_C - STATUS_D - ZONE_TUN |  |
| READ_PAR | All static variables of the structure PAR are read from the FM 355-2 an stored in the instance DB on the CPU. | No transfer of the controller parameters to the CPU  You can change the individual parameters in the user program. |
| LOAD_PAR | All static variables of the structure PAR are downloaded from the CPU to the FM 355-2. This is necessary if the control parameters on the CPU have changed based on the process states. | No transfer of the controller parameters to the FM 355-2 |

After data transfer has been completed, the parameters LOAD_OP, READ_OUT, LOAD_PAR and READ_PAR are reset to FALSE.

#### Use in distributed I/O

When the FM 355-2 is used in distributed I/O, the data transfer and the resetting of the parameters can take a few call cycles.

#### Processing times FMT_PID

During program controlled re-configuring (LOAD_PAR, LOAD_OP) of the FM 355-2 by FMT_PID, its runtime is extended. The new parameters are always immediately effective.

| Boundary conditions |  |  | Processing time in |  |
| --- | --- | --- | --- | --- |
| READ_OUT | LOAD_OP | LOAD_PAR READ_PAR | CPU 315-2-DP | CPU 416-2 DP |
| FALSE | FALSE | FALSE | 0.65 ms | 0.04 ms |
| TRUE | FALSE | FALSE | 2.85 ms | 0.30 ms |
| TRUE | TRUE | FALSE | 4.56 ms | 0.55 ms |
| FALSE | FALSE | TRUE | 3.58 ms*) | 0.30 ms |
| TRUE | FALSE | TRUE | 5.8 ms*) | 0.56 ms |
| TRUE | TRUE | TRUE | 7.41 ms*) | 0.82 ms |
| *) If READ_PAR is set instead of LOAD_PAR, the CPU 315-2 DP processing time is increased by 0.35 ms. |  |  |  |  |

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Input parameters FMT_PID (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | At this input you will find the module address resulting from configuration under STEP 7. |
| CHANNEL | 2.0 | INT | 0 | Number of the controller channel to which the instance DB is referenced.   Values from 0 to 3 are permitted |

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Output parameters FMT_PID (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| QMOD_F | 4.0 | BOOL | FALSE | The instruction checks that the reading and writing of a data record has been completed. If errors are identified, the QMOD_F output is set. The cause of errors can be: An incorrect module address on the MOD_ADDR parameter, an incorrect channel number on the CHANNEL parameter or a defective module. |
| RET_VALU | 6.0 | WORD | W#16#0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the instructions RDREC and WRREC. |

### In/out parameters FMT_PID (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| COM_RST | 8.0 | BOOL | FALSE | If COM_RST = TRUE, the instruction FMT_PID executes an initialization routine and resets COM_RST. This initialization routine is imperative every time the CPU starts up. |
| LOAD_OP | 8.1 | BOOL | FALSE | If the in/out parameter LOAD_OP is set, the operating parameters are downloaded to the module, the output parameters are read and the in/out parameters are reset. |
| READ_OUT | 8.2 | BOOL | FALSE | If the in/out parameter READ_OUT is set, the output parameters are read from the module and stored in the OUT structure of the instance DB and the I/O parameters are reset. |
| LOAD_PAR | 8.3 | BOOL | FALSE | If the in/out parameter LOAD_PAR is set, the controller parameters are downloaded to the module and the in/out parameter is reset. |
| READ_PAR | 8.4 | BOOL | FALSE | If the parameter READ_PAR = TRUE is set, then the controller parameters are read from FM 355-2 and stored in the PAR structure of the instance DB. The in/out parameter is then reset. |

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Static variables FMT_PID.OP (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| vers_nr | 10.0 | WORD | W#16#3230 | The vers_nr parameter may not be modified by users. It identifies the start of the operating parameters that are transferred to the module, if LOAD_OP = TRUE is set. |
| SP_RE | 12.0 | REAL | 0.0 | An external setpoint is interconnected with the controller at input SP_RE. |
| LMN_RE | 16.0 | REAL | 0.0 | An external manipulated value is interconnected with the controller at input LMN_RE.  Values from -100.0 to 100.00 (%) are permitted. |
| SAFE_ON | 20.0 | BOOL | FALSE | When SAFE_ON is set, a safety value is applied as manipulated value. |
| LMNTRKON | 20.1 | BOOL | FALSE | If LMNTRKON is set, the manipulated value is corrected to an analog input (AI)   (This does not apply to step controllers without analog position feedback) |
| LMN_REON | 20.2 | BOOL | FALSE | If LMN_REON is set, the external manipulated value LMN_RE is applied (manual mode). |
| LMNRHSRE | 20.3 | BOOL | FALSE | The "Control valve at high endstop" signal can be interconnected with a digital input of the FM 355-2 or at the LMNRHSRE input. LMNRHSRE = TRUE means: The control valve is at high endstop.   (Applies to step controllers only) |
| LMNRLSRE | 20.4 | BOOL | FALSE | The "Control valve at high endstop" signal can be interconnected with a digital input of the FM 355-2 or at the LMNRLSRE input. LMNRLSRE = TRUE means: The control valve is at the low endstop.   (Applies to step controllers only) |
| LMNS_ON | 20.5 | BOOL | FALSE | Enable manipulated value operation   (Applies to step controllers only; manual mode). |
| LMN_UP | 20.6 | BOOL | FALSE | Manipulated value signal up operation   (Applies to step controllers only). |
| LMN_DN | 20.7 | BOOL | FALSE | Manipulated value signal down operation   (Applies to step controllers only). |
| SAVE_PAR | 22.0 | BOOL | FALSE | Saves the current contoller parameters to the output parameters of the instruction FMT_TUN.  - FMT_TUN.SAV_PFAC=PFAC_SP - FMT_TUN.SAV_GAIN =GAIN - FMT_TUN.SAV_TI =TI - FMT_TUN.SAV_TD = TD - FMT_TUN.SAV_D_F =D_F - FMT_TUN.SAV_CONZ = CON_ZONE - FMT_TUN.SAV_RATI =RATIOFAC - FMT_TUN.SAV_CZON=CONZ_ON - FMT_TUN.SAV_PSEL=P_SEL |
| UNDO_PAR | 22.1 | BOOL | FALSE | The saved controller parameters are retrieved again, also in automatic mode.   - PFAC_SP= FMT_TUN.SAV_PFAC - GAIN = FMT_TUN.SAV_GAIN - TI = FMT_TUN.SAV_TI - TD = FMT_TUN.SAV_TD - D_F = FMT_TUN.SAV_D_F - CON_ZONE = FMT_TUN.SAV_CONZ - RATIOFAC = FMT_TUN.SAV_RATI - CONZ_ON= FMT_TUN.SAV_CZON - P_SEL= FMT_TUN.SAV_PSEL |
| LOAD_PID | 22.2 | BOOL | FALSE | If PID_ON=TRUE, it loads the PID parameters (PID_GAIN, PID_TI, PID_TD).  If PID_ON=FALSE, the PI parameters (PI_GAIN, PI_TI) are loaded. (Even in automatic mode) |
| TUN_ON | 22.3 | BOOL | FALSE | TUN_ON=TRUE switches the FM 355-2 to ready for optimization (PHASE=1): The manipulated value is averaged until the manipulated value excitation is applied. |
| TUN_ST | 22.4 | BOOL | FALSE | If the setpoint is to remain constant during controller optimization at the operating point, a manipulated value step-change by the amount of TUN_DLMN is enabled by TUN_ST=TRUE (PHASE = 1 or PHASE = 2) |
| TUN_CST | 22.5 | BOOL | FALSE | Starts cooling optimization by applying a manipulated manipulated value step-change in the amount of TUN_CLMN (PHASE = 1 or PHASE = 2) |

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Static variables FMT_PID.PAR (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| vers_nr | 24.0 | WORD | W#16#3230 | The vers_nr parameter may not be modified by users. It identifies the start of the controller parameters, which are read from the FM with READ_PAR = TRUE and stored in the instance DB or transferred to the FM with LOAD_PAR = TRUE. |
| P_SEL | 26.0 | BOOL | TRUE | It is possible to enable or disable PID actions individually in the PID algorithm. The P-action is enabled if the input P_SEL is set. |
| MONERSEL | 26.1 | BOOL | FALSE | The controller possesses a limit value detector that can be applied either for the process value or for the error signal. If MONERSEL is set, the error signal is monitored. |
| PID_ON | 26.2 | BOOL | TRUE | After optimization or in the case of LOAD_PID =TRUE, the PID parameters are enabled. If PID_ON =FALSE, the PI parameters are loaded.  With certain process types it is nevertheless possible that only a PI controller will be designed despite PID_ON = TRUE. |
| CONZ_ON | 26.3 | BOOL | FALSE | TRUE = control zone enabled  FALSE = control zone off |
| D_EL_SEL | 28.0 | INT | 16 | The D-action element in the PID algorithm can be assigned to a separate input This is selected at the D_EL_SEL parameter.   - D_EL_SEL = 0 to D_EL_SEL = 3: Analog input 0 to 3 - D_EL_SEL = 16: error signal - D_EL_SEL = 17: negative process value |
| SP_HLM | 30.0 | REAL | 100.0 | The setpoint is always limited to a high and a low limit. The SP_HLM parameter specifies the high limit.  SP_HLM > SP_LLM |
| SP_LLM | 34.0 | REAL | 0.0 | The setpoint is always limited to a high and a low limit. The SP_LLM parameter specifies the low limit.  SP_LLM < SP_HLM |
| H_ALM | 38.0 | REAL | 100.0 | Highest limit for monitoring the process value or the error signal.  H_ALM > H_WRN |
| H_WRN | 42.0 | REAL | 90.0 | Second to highest limit for monitoring the process value or the error signal.  H_WRN > H_ALM |
| L_WRN | 46.0 | REAL | 10.0 | Second to lowest limit for monitoring the process value or the error signal.  Values from H_WRN to L_ALM are permitted. |
| L_ALM | 50.0 | REAL | 0.0 | Lowest limit for monitoring the process value or the error signal.  Values from L_ALM to L_WRN are permitted. |
| HYS | 54.0 | REAL | 1.0 | The parameters can be assigned for a hysteresis to prevent the monitoring displays from flickering.  HYS >= 0.0 |
| DEADB_W | 58.0 | REAL | 0.0 | A dead band is applied to the error signal. The DEADB_W parameter determines the size of the dead band.  DEADB_W >= 0.0 |
| PFAC_SP | 62.0 | REAL | 1.0 | PFAC_SP specifies the effective P-action when there is a setpoint change.  Values from 0.0 to 1.0 are permitted. |
| GAIN | 66.0 | REAL | 1.0 | The GAIN parameter specifies the controller gain.  The control direction is inverted by means of a negative sign of GAIN. |
| TI | 70.0 | REAL | 3000.0 | The TI parameter (integral-action time) determines the time response of the integrator. If TI = 0.0, the integral action is disabled.  TI = 0.0 or TI >= 0.5 |
| TD | 74.0 | REAL | 0.0 | The TD (rate time) paramter determines the time response of the derivative action (D-action element). If TD = 0.0, the derivative action is disabled  TD = 0.0 or TD >= 1.0 |
| D_F | 78.0 | REAL | 5.0 | The time constant TD/D_F that is effective for the D-action element is limited internally to ≥ sampling time/2.  Values from 5.0 to 10.0 are permitted. |
| LMN_SAFE | 82.0 | REAL | 0.0 | A safety value can be parameterized for the manipulated value.  Values from -100.0 to 100.0 (%) are permitted. |
| LMN_HLM | 86.0 | REAL | 100.0 | The manipulated value is always limited to a high and a low limit. The LMN_HLM parameter specifies the high limit.  (This does not apply to step controllers without analog position feedback).  Values from LMN_LLM to 100.0 (%) are permitted. |
| LMN_LLM | 90.0 | REAL | 0.0 | The manipulated value is always limited to a high and a low limit. The LMN_LLM parameter specifies the low limit.   (This does not apply to step controllers without analog position feedback).  Values from -100.0 to LMN_HLM (%) are permitted. |
| MTR_TM | 94.0 | REAL | 60.0 | Runtime of the control valve from stop to stop   (Applies to step controllers only).  MTR_TM >= 0.001 |
| PULSE_TM | 98.0 | REAL | 0.0 | Minimum pulse duration   (Applies to step controllers or pulse controllers only) |
| BREAK_TM | 102.0 | REAL | 0.0 | Minimum pulse duration   (Applies to step controllers or pulse controllers only) |
| RATIOFAC | 106.0 | REAL | 0.0 | Ratio of heating gain/cooling gain for the process.   RATIOFAC <> 0.0 has the following effect:  - LMN = LMN * RATIOFAC for LMN<0.0; - CON_ZONE 50 % greater   Values from 0.01 to 100.0 or 0.0 are permitted. |
| CON_ZONE | 110.0 | REAL | 100.0 | Control zone width  If ER >= CON_ZONE, then LMN = LMN_HLM.  If ER <= -CON_ZONE, then LMN = LMN_LLM.  If RATIOFAC <> 0.0 and ER <= -CON_ZONE/RATIOFAC, then LMN = LMN_LLM.  CON_ZONE > 0.0 |
| TUN_DLMN | 114.0 | REAL | 20.0 | Process excitation for controller optimization results from a manipulated value step-change of TUN_DLMN.  Values from -100.0 to 100.0 (%) are permitted. |
| TUN_CLMN | 118.0 | REAL | -20.0 | Manipulated variable step-change after start of cooling optimization by TUN_CST.  Values from -100.0 to 100.0 (%) are permitted. |

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Static variables FMT_PID.OUT (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| vers_nr | 122.0 | WORD | W#16#3230 | The vers_nr parameter may not be modified by users. It marks the start of the output parameter that is read by the module if READ_OUT = TRUE is set. |
| PV | 124.0 | REAL | 0.0 | Effective process value. |
| LMN | 128.0 | REAL | 0.0 | The effective output value is output at the LMN output.  In the case of step controllers without analog position feedback, the unlimited P- + D-action is output at the LMN output.  Values from -100.0 to 100.0 (%) are permitted. |
| QLMNSAFE | 132.1 | BOOL | FALSE | If the QLMNSAFE output is set, the safety output value is output as output value. |
| QLMNTRK | 132.3 | BOOL | FALSE | Output QLMNTRK indicates if the output value is being corrected via an analog input. |
| QLMN_RE | 132.4 | BOOL | FALSE | The QLMN_RE output indicates if LMN_REON is set and the external output value LMN_RE is applied as the output value. |
| QLMNR_HS | 132.5 | BOOL | FALSE | QLMNR_HS = TRUE means: The control valve is at high endstop. (Applies to step controllers only) |
| QLMNR_LS | 132.6 | BOOL | FALSE | QLMNR_LS = TRUE means: The control valve is at the low endstop.  (Applies to step controllers only) |
| QLMNR_ON | 132.7 | BOOL | FALSE | QLMNR_ON = TRUE means:  Step controller with position feedback. |
| QSTEPCON | 133.0 | BOOL | FALSE | Step controller / pulse controller  - QSTEPCON = 0: Pulse controller or continuous controller - QSTEPCON = 1: Step controller |
| QSPR | 133.1 | BOOL | FALSE | If the QSPR output is set, the continuous controller operates in split-range mode. |
| QMAN_FC | 133.3 | BOOL | FALSE | This controller is a master controller. It is manually followed up to the process value of a slave controller, or its I-action is disabled because the setpoint or manipulated variable of the slave controller has reached the limit. |
| QH_ALM | 134.0 | BOOL | FALSE | High limit H_ALM overshot by process value or error value. |
| QH_WRN | 134.1 | BOOL | FALSE | Process value or control deviation exceeds second to highest limit H_WRN. |
| QL_WRN | 134.2 | BOOL | FALSE | Process value or control deviation has dropped below the second to lowest limit L_WRN. |
| QL_ALM | 134.3 | BOOL | FALSE | Process value or control deviation has dropped below the lowest limit L_ALM. |
| QLMN_HLM | 134.4 | BOOL | FALSE | The QLMN_HLM output reports that the high output value limit LMN_HLM has been reached.   (This does not apply to step controllers without analog position feedback). |
| QLMN_LLM | 134.5 | BOOL | FALSE | The QLMN_LLM output reports that the low output value limit LMN_LLM has been reached.  (This does not apply to step controllers without analog position feedback) |
| QPAR_F | 134.6 | BOOL | FALSE | The module checks the reliability of the parameters. A parameter assignment error is indicated at output QPAR_F. |
| QCH_F | 134.7 | BOOL | FALSE | The QCH_F output is set if the controller channel is unable to supply any valid results. A channel error (for example, wire break) is also set if QPAR_F = TRUE or QMOD_F = TRUE. If QCH_F = TRUE, then the precise error information in the diagnostic data record DS1 of the module is read out. |
| QUPRLM | 135.0 | BOOL | FALSE | The setpoint is limited to a positive and negative slew rate.  If the QUPRLM output is set, the setpoint rise is limited. |
| QDNRLM | 135.1 | BOOL | FALSE | The setpoint is limited to a positive and negative slew rate.  If the QDNRLM output is set, the setpoint decay is limited. |
| QSP_HLM | 135.2 | BOOL | FALSE | The QSP_HLM output reports that the high setpoint limit SP_HLM has been reached. |
| QSP_LLM | 135.3 | BOOL | FALSE | The QSP_LLM output reports that the low setpoint limit SP_LLM has been reached. |
| QLMNUP | 135.4 | BOOL | FALSE | "Output value signal up" output   (Applies to step controllers or pulse controllers only) |
| QLMNDN | 135.5 | BOOL | FALSE | "Output value signal down" output  (Applies to step controllers or pulse controllers only) |
| QTUN_ON | 135.6 | BOOL | FALSE | QTUN_ON = TRUE indicates that tuning is in progress. |
| PAR_ACT | 135.7 | BOOL | FALSE | Updating controller parameters |
| SP | 136.0 | REAL | 0.0 | Effective setpoint |
| ER | 140.0 | REAL | 0.0 | Effective control deviation (SP- PV) |
| DISV | 144.0 | REAL | 0.0 | Effective disturbance variable  Values from -100.0 to 100.0 (%) are permitted. |
| LMN_A | 148.0 | REAL | 0.0 | Continuous or pulse controllers display the output value A of the split-range function at the LMN_A output; step controllers with analog position feedback display the position feedback there.  Values from -100.0 to 100.0 (%) are permitted. |
| LMN_B | 152.0 | REAL | 0.0 | Continuous or pulse controllers display the output value B of the split-range function at output LMN_B.  Values from -100.0 to 100.0 (%) are permitted. |
| PHASE | 156.0 | INT | 0 | Indicates the controller tuning phases.  - PHASE = -1: Canceling of controller tuning, for example with parallel tuning of several channels. The value lasts for a few cycles and is used as cancelation signal between the instruction FMT_PID and the module. - PHASE = 0: No tuning mode; automatic or manual mode - PHASE = 1: Ready to start tuning; check parameters, wait for excitation, measure the sampling times - PHASE = 2: Actual tuning: Searching for point of inflection with constant output value. - PHASE = 3: Calculating process parameters. Saving valid controller parameters prior to tuning. - PHASE = 4: Controller design - PHASE = 5: Following up the controller to the new manipulated variable - PHASE = 6: Following up the controller to the new manipulated variable - PHASE = 7: Check of process type, if process type II or III was determined (during heating optimiation only). |
| STATUS_H | 158.0 | INT | 0 | [Parameters STATUS_H](#parameters-status_h-s7-300-s7-400) displays a diagnostic value via the search for the point of inflection during heating process. |
| STATUS_C | 160.0 | INT | 0 | [Parameters STATUS_C](#parameters-status_c-s7-300-s7-400) displays a diagnostic value via the search for the point of inflection during cooling process. |
| STATUS_D | 162.0 | INT | 0 | [Parameters STATUS_D](#parameters-status_d-s7-300-s7-400) indicates a diagnostic value of the controller design during the heating process. |
| ZONE_TUN | 164.0 | WORD | W#16#0 | In HEX code, each of the four digits represents one channel, arranged in the following order from left to right: Channel 0, 1, 2, 3. ZONE_TUN = 0 means that the selected channel will not be tuned as a group with other channels. A value <> 0000 shows - in each case with a 1 - the channels that will be tuned as a group. |

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Block diagrams (S7-300, S7-400)

#### Overview

The following figures show at which points the parameters of the instruction FMT_PID act.

As far as three-component controllers and ratio/mixing controllers are concerned, the parameters affect the same point as with fixed setpoint or cascade controllers. This also applies to the parameters that are equally in place for continuous controllers, controllers with pulse output as well as step controllers. It is generally correct that identical buttons also contain identical parameters. For reasons of clarity, not all structure diagrams are depicted, thereore, and not all parameters are marked in all figures.

However, the parameters of the instruction FMT_PID are contained in all the figures – with the exception of the parameters MOD_ADDR, CHANNEL, QMOD_F, QPAR_F, QCH_F, QLMNR_ON, RET_VALU, COM_RST, LOAD_PAR, READ_PAR, READ_OUT and LOAD_OP.

The following figures show the places in the module affected by the parameters of the FMT_PID.

#### Action of the input parameters

The following figure shows the control deviation for a fixed-value or cascade controller.

![Action of the input parameters](images/18704877451_DV_resource.Stream@PNG-en-US.png)

The following figure shows the block diagram of the control algorithm.

![Action of the input parameters](images/18704895755_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the continuous controller (FM 355-2 C).

![Action of the input parameters](images/18704032139_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the pulse controller (FM 355-2 S).

![Action of the input parameters](images/18704914059_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the step controller with position feedback (FM 355-2 S).

![Action of the input parameters](images/18704932363_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the step controller without position feedback (FM 355-2 S).

![Action of the input parameters](images/18704950667_DV_resource.Stream@PNG-en-US.png)

#### Generating output parameters

The following figures show at which points in the module the output parameters of the instruction FMT_PID are generated.

The following figure shows the control deviation for a fixed-value or cascade controller.

![Generating output parameters](images/18704968971_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the continuous controller (FM 355-2 C).

![Generating output parameters](images/18704859147_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the pulse controller (FM 355-2 S).

![Generating output parameters](images/18704987275_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the step controller with position feedback (FM 355-2 S).

![Generating output parameters](images/24541623563_DV_resource.Stream@PNG-en-US.png)

The following figure shows the controller output of the step controller without position feedback (FM 355-2 S).

![Generating output parameters](images/24541604747_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Parameters STATUS_H (S7-300, S7-400)

STATUS_H indicates a diagnostic value via the search for the point of inflection during the heating process.

If a diagnostic value 2xxxx is displayed, optimization is completed but the controller parameters are uncertain.

If a diagnostic value 3xxxx is displayed, the optimization is canceled (PHASE = 0 and TUN_ON = FALSE) and the controller switches to the previous operating mode.

| STATUS_ H | Description | Remedy |
| --- | --- | --- |
| 0 | Default or no or still no new controller parameters |  |
| 10000 | Optimization completed + suitable controller parameters found |  |
| 2xxxx | Optimization completed + controller parameters uncertain |  |
| 2xxx1 | effective motor actuating time >= 65% of the point of inflection time T_P_INF | Compensation of TU and T_P_INF is not performed any more. This leads to the design of a softer controller |
| 2xx2x | Point of inflection not reached   (only with excitation via setpoint step-change) | If the controller oscillates, reduce the controller parameters or repeat test with lower TUN_DLMN. |
| 2x1xx | Estimation error   TU <= 3*Sampling time | Repeat test. |
| 2x2xx | Serious estimation error (TU < sampling time) | Repeat test.  Special case PT1-only process: Do not repeat the test; reduce the controller parameters if necessary |
| 2x3xx | Estimation error TU too high | Repeat test under better conditions. |
| 21xxx | Estimation error N_PTN < 1 | Repeat test under better conditions. |
| 22xxx | Estimation error N_PTN > 10 | Repeat test under better conditions. |
| 3xxxx | Optimization interrupted in phase 1 due to incorrect parameter assignment |  |
| 30001 | Simultaneous setting of TUN_ON and TUN_ST | Restart optimization. |
| 30002 | |TUN_DLMN| < 5 % or value of effective LMN modification < 5 %  - Transition in phase 99 (Phase 0 in a parallel optimization process) - Output LMN = LMN0 | Either you configured for TUN_DLMN a value that is too low, or the manipulated variable was near to a control limit prior to start of optimization.  In this case, you must prevent the controller from settling to the new setpoint and from unnecessary leaving the stationary operating point (not possible with parallel optimization process).  You should now proceed as follows:  - If necessary, cancel setpoint and set TUN_ON to FALSE. - TUN_DLMN correct. - If TUN_DLMN >= 5%, check manipulated value limits. - Restart optimization. |
| 30004 | |TUN_DLMN| < 5 % or effective LMN modification < 5 %  The effective manipulated value difference limited by split–range limits and not by manipulated value limits.   - Transition in phase 99 (Phase 0 in a parallel optimization process) - Output LMN = LMN0 | See STATUS_H=30002:  Also take into account that, for example, with LMN_A < 5 % a heating optimization with negative TUN_DLMN is not possible (reason: the cooling power must not be adjusted). |
| 30009 | Safety mode | Close safety mode and restart optimization. |

> **Note**
>
> At the end of phase 1, STATUS_H = 0 is reset.
>
> If you cancel optimization in phase 2, STATUS_H = 0. However, STATUS_D still displays the status of the last controller calculation.

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Parameters STATUS_C (S7-300, S7-400)

STATUS_C indicates a diagnostic value via the search for the point of inflection during cooling process.

If a diagnostic value 2xxxx is displayed, optimization is completed, but the controller parameters are uncertain.

If a diagnostic value 3xxxx is displayed, the optimization is canceled (PHASE = 0 and TUN_ON = FALSE) and the controller switches to the previous operating mode.

| STATUS_ C | Description | Remedy |
| --- | --- | --- |
| 0 | Default or no or still no new controller parameters |  |
| 10000 | Optimization completed + suitable controller parameters found |  |
| 2xxxx | Optimization completed + controller parameters uncertain |  |
| 2x3xx | Estimation error TU too high | Repeat test under better conditions. |
| 21xxx | Estimation error N_PTN < 1 | Repeat test under better conditions. |
| 22xxx | Estimation error N_PTN > 10 | Repeat test under better conditions. |
| 3xxxx | Optimization interrupted in phase 1 due to incorrect parameter assignment |  |
| 30001 | Simultaneous setting of TUN_ON and TUN_CST | Restart optimization. |
| 30002 | Only for step controllers without analog position feedback:  |TUN_CLMN| < 5 % or value of effective LMN modification < 5 %  - Transition to phase 0 - TUN_ON = FALSE | Either you configured for TUN_CLMN a value that is too low, or the manipulated variable was near to a control limit prior to start of optimization.  In this case, you must prevent the controller from settling to the new setpoint and from unnecessary leaving the stationary operating point (not possible with parallel optimization process).  You should now proceed as follows:  - If necessary cancel setpoint and set TUN_ON to FALSE. - TUN_CLMN correct. - Check the manipulated value limits, if |TUN_CLMN| >= 5% and the sign was correct. - Restart optimization. |
| 30003 | TUN_CLMN <= -5%, butLMN_LLM > -5%.  - Transition to phase 0 - TUN_ON = FALSE | The low limit LMN_LLM is too high (e.g. 0%) and therefore prevents the output of cooling power.  - Correct low limit LMN_LLM. - Restart optimization. |
| 30004 | TUN_CLMN > -5 % or effective LMN modification > -5 %  The effective manipulated value difference limited by split–range limits and not by manipulated value limits.   - Transition to phase 0 - TUN_ON = FALSE | See STATUS_C=30002:  Also take into account that, for example, with LMN_A < 5 % a heating optimization with negative TUN_DLMN is not possible (reason: the cooling power must not be adjusted). |
| 30008 | TUN_CST but without previous heating optimization  - Transition to phase 0 - TUN_ON = FALSE | First start heating optimization |
| 30009 | Safety mode | Close safety mode and restart optimization. |

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

### Parameters STATUS_D (S7-300, S7-400)

| STATUS_D | Description |
| --- | --- |
| 0 | No controller parameters have been calculated. |
| 110 | N_PTN <= 1.5 Process type I fast |
| 121 | N_PTN > 1.5 Process type I |
| 122 | N_PTN = 1.9 process type I after phase 7 (before N_PTN > 1.9) |
| 200 | N_PTN > 1.9 Process type II (transition range) |
| 310 | N_PTN >= 2.1 Process type III fast |
| 320 | N_PTN > 2.6 Process type III |

> **Note**
>
> If you interrupt optimization in phase 2, STATUS_H = 0 is. However, STATUS_D still displays the status of the last controller calculation.
>
> The higher the value of STATUS_D, the higher the order of the control process, the greater the ratio TU/TA and the gentler the controller parameters will be.

---

**See also**

[Description FMT_PID (S7-300, S7-400)](#description-fmt_pid-s7-300-s7-400)
  
[Mode of operation FMT_PID (S7-300, S7-400)](#mode-of-operation-fmt_pid-s7-300-s7-400)
  
[Input parameters FMT_PID (S7-300, S7-400)](#input-parameters-fmt_pid-s7-300-s7-400)
  
[Output parameters FMT_PID (S7-300, S7-400)](#output-parameters-fmt_pid-s7-300-s7-400)
  
[In/out parameters FMT_PID (S7-300, S7-400)](#inout-parameters-fmt_pid-s7-300-s7-400)
  
[Static variables FMT_PID.OP (S7-300, S7-400)](#static-variables-fmt_pidop-s7-300-s7-400)
  
[Static variables FMT_PID.PAR (S7-300, S7-400)](#static-variables-fmt_pidpar-s7-300-s7-400)
  
[Static variables FMT_PID.OUT (S7-300, S7-400)](#static-variables-fmt_pidout-s7-300-s7-400)
  
[Block diagrams (S7-300, S7-400)](#block-diagrams-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)

## FMT_PAR (S7-300, S7-400)

This section contains information on the following topics:

- [Description FMT_PAR (S7-300, S7-400)](#description-fmt_par-s7-300-s7-400)
- [Input parameters FMT_PAR (S7-300, S7-400)](#input-parameters-fmt_par-s7-300-s7-400)
- [Output parameters FMT_PAR (S7-300, S7-400)](#output-parameters-fmt_par-s7-300-s7-400)
- [In/out parameters FMT_PAR (S7-300, S7-400)](#inout-parameters-fmt_par-s7-300-s7-400)
- [Parameters INDEX (S7-300, S7-400)](#parameters-index-s7-300-s7-400)

### Description FMT_PAR (S7-300, S7-400)

The instruction FMT_PAR is used for online modification of parameters that cannot be defined via instruction FMT_PID.

#### Call

FMT_PAR has to be called in the same OB as all the other instructions that access the same FM 355-2.

To save runtime, FMT_PAR should only be called using LOAD=TRUE, if parameters are to be modified.

#### Operating principle

With FMT_PAR, you can modify one REAL-parameter and one of the INT parameters for each call.

At [Parameters INDEX](#parameters-index-s7-300-s7-400) specify the index numbers of the parameter you want to modify. At the input parameter VALUE_R or VALUE_I, specify the new values.

If you want to modify several parameters, you must call the same instance DB several times in succession using LOAD_PAR = TRUE and different index numbers.

If FM 355-2 is used in distributed I/O, it may take a few call cycles until the parameters are applied to FM 355-2. As long as the transfer has not been completed, parameter LOAD_PAR retains the value TRUE. When modifying parameters, keep repeating the call of instruction FMT_PAR until LOAD_PAR = FALSE is.

> **Note**
>
> Please note that parameters, modified using FMT_PAR,are overwritten at startup of CPU with the parameters from the system data.

#### Example

You want to modify in operating mode the startup time of the ramp for the reference variable as well as,depending on the process state, use different analog input values as process value.

- To configure the startup time for the reference variable at 10.0 call FMT_PAR in the current mode with INDEX = 30 and VALUE_R = 10.0.
- If you want to configure the analog input value 4 of the module as process value, call FMT_PAR with INDEX = 50 and VALUE_I = 4 during operation.

---

**See also**

[Input parameters FMT_PAR (S7-300, S7-400)](#input-parameters-fmt_par-s7-300-s7-400)
  
[Output parameters FMT_PAR (S7-300, S7-400)](#output-parameters-fmt_par-s7-300-s7-400)
  
[In/out parameters FMT_PAR (S7-300, S7-400)](#inout-parameters-fmt_par-s7-300-s7-400)
  
[Parameters INDEX (S7-300, S7-400)](#parameters-index-s7-300-s7-400)

### Input parameters FMT_PAR (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CHANNEL | 2.0 | INT | 0 | Number of controller channel to which the instance DB refers.  Values from 0 to 3 are permitted. |
| INDEX | 4.0 | INT | 0 | 0 to 100 |
| VALUE_R | 6.0 | REAL | 0.0 | Depending on respective parameter |
| VALUE_I | 10.0 | INT | 0 | Depending on respective parameter |

---

**See also**

[Description FMT_PAR (S7-300, S7-400)](#description-fmt_par-s7-300-s7-400)
  
[Output parameters FMT_PAR (S7-300, S7-400)](#output-parameters-fmt_par-s7-300-s7-400)
  
[In/out parameters FMT_PAR (S7-300, S7-400)](#inout-parameters-fmt_par-s7-300-s7-400)
  
[Parameters INDEX (S7-300, S7-400)](#parameters-index-s7-300-s7-400)

### Output parameters FMT_PAR (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 12.0 | WORD | W#16#0 | RET_VALU contains the 2nd and 3rd bytes from parameter STATUS of instruction WRREC. |

### In/out parameters FMT_PAR (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| LOAD_PAR | +14.0 | BOOL | FALSE | If the in/out parameters LOAD_PAR is set, VALUE_R or VALUE_I are written on the module.INDEX indicates which parameter is overwritten. Thereafter LOAD_PAR is reset. |

---

**See also**

[Description FMT_PAR (S7-300, S7-400)](#description-fmt_par-s7-300-s7-400)
  
[Input parameters FMT_PAR (S7-300, S7-400)](#input-parameters-fmt_par-s7-300-s7-400)
  
[Output parameters FMT_PAR (S7-300, S7-400)](#output-parameters-fmt_par-s7-300-s7-400)
  
[Parameters INDEX (S7-300, S7-400)](#parameters-index-s7-300-s7-400)

### Parameters INDEX (S7-300, S7-400)

| INDEX | Description | Data type |
| --- | --- | --- |
| 0 | no parameter selected | - |
| 1 | Filter time constant for the analog input | REAL |
| 2 | Scaling of analog input end of measuring range equals 100% | REAL |
| 3 | Scaling of analog input end of measuring range equals 0% | REAL |
| 4 | Polyline, interpolation point 1 supply side | REAL |
| 5 | Polyline, interpolation point 2 supply side | REAL |
| 6 | Polyline, interpolation point 3 supply side | REAL |
| 7 | Polyline, interpolation point 4 supply side | REAL |
| 8 | Polyline, interpolation point 5 supply side | REAL |
| 9 | Polyline, interpolation point 6 supply side | REAL |
| 10 | Polyline, interpolation point 7 supply side | REAL |
| 11 | Polyline, interpolation point 8 supply side | REAL |
| 12 | Polyline, interpolation point 9 supply side | REAL |
| 13 | Polyline, interpolation point 10 supply side | REAL |
| 14 | Polyline, interpolation point 11 supply side | REAL |
| 15 | Polyline, interpolation point 12 supply side | REAL |
| 16 | Polyline, interpolation point 13 supply side | REAL |
| 17 | Polyline, interpolation point 1 output side | REAL |
| 18 | Polyline, interpolation point 2 output side | REAL |
| 19 | Polyline, interpolation point 3 output side | REAL |
| 20 | Polyline, interpolation point 4 output side | REAL |
| 21 | Polyline, interpolation point 5 output side | REAL |
| 22 | Polyline, interpolation point 6 output side | REAL |
| 23 | Polyline, interpolation point 7 output side | REAL |
| 24 | Polyline, interpolation point 8 output side | REAL |
| 25 | Polyline, interpolation point 9 output side | REAL |
| 26 | Polyline, interpolation point 10 output side | REAL |
| 27 | Polyline, interpolation point 11 output side | REAL |
| 28 | Polyline, interpolation point 12 output side | REAL |
| 29 | Polyline, interpolation point 13 output side | REAL |
| 30 | Startup time of the ramp for the reference variable | REAL |
| 31 | Safety manipulated value | REAL |
| 32 | Offset for setpoint link (ratio/blending controller) | REAL |
| 33 | Factor for process value B (three component controller) | REAL |
| 34 | Factor for process value C (three component controller) | REAL |
| 35 | Offset for process value link (three-component controller) | REAL |
| 36 | Factor for disturbance variable link | REAL |
| 37 | Operating point | REAL |
| 38 | unused | REAL |
| 39 | Vertices for split range function Start of input signal A range | REAL |
| 40 | Vertices for split range function End of input signal A range | REAL |
| 41 | Vertices for split range function Start of output signal A range | REAL |
| 42 | Vertices for split range function: End of output signal A range | REAL |
| 43 | Vertices for split range function Start of input signal B range | REAL |
| 44 | Vertices for split range function End of input signal B range | REAL |
| 45 | Vertices for split range function: Start of output signal B range | REAL |
| 46 | Vertices for split range function: End of output signal B range | REAL |
| 47 | Minimum pulse time | REAL |
| 48 | Minimum break time | REAL |
| 49 | Selection of the reference variable SP or SP_RE for the controller  - -1: Setpoint SP_RE of the instruction - 0 to 3: Analog input value 0 to 3 - 16 to 19: Manipulated variable (LMN) of controllers 0 to 3 - 32 to 35: Control variable A of controllers 0 to 3 - 48 to 51: Control variable B of controllers 0 to 3 | INT |
| 50 | Selection of the main controlled variable process value A for the controller  - -1: Process value A = 0.0 - 0 to 3: Analog input value 0 to 3 | INT |
| 51 | Selection of the auxiliary controlled variable process value B for the controller  - -1: Process value B = 0.0 - 0 to 3: Analog input value 0 to 3 | INT |
| 52 | Selection of the auxiliary controlled variable process value C for the controller  - -1: Process value C = 0.0 - 0 to 3: Analog input value 0 to 3 | INT |
| 53 | Selection of the auxiliary controlled variable process value D for the controller  - -1: Process value D = 0.0 - 0 to 3: Analog input value 0 to 3 - 16 to 19: Manipulated variable (LMN) of controllers 0 to 3 | INT |
| 54 | Selection of the disturbance variable DISV for the controller  - -1: Disturbance variable = 0.0 - 0 to 3: Analog input value 0 to 3 | INT |
| 55 | Selection on the correction input switch. On the measuring point MP TRACKPER the value can be read off with tool tip.  - -1: Position follow-up = 0.0 - 0 to 3: Analog input value 0 to 3 | INT |
| 56 | Selection on the position feedback input switch for step controllers with position feedback.  - -1: Position follow-up = 0.0 - 0 to 3: Analog input value 0 to 3 | INT |
| 57 | Selecting the signal for transition to safety value for the manipulated value of the controller  - -1: Can only be assigned via SAFE_ON of instruction FMT_PID - 0 to 7: Assignment via SAFE_ON parameter of the instruction FMT_PID ORed with digital input 0 to 7 | INT |
| 58 | Selecting signal for switching over to adjustment function of the manipulated value of the controller.  - -1: Can only be assigned via LMNTRKON of instruction FMT_PID - 0 to 7: Assignment via LMNTRKON parameter of the instruction FMT_PID ORed with digital input 0 to 7 | INT |
| 59 | Selecting the signal for changing over the manipulated value of the controller to LMN_RE  - -1: Can only be assigned via LMN_REON of instruction FMT_PID - 0 to 7: Assignment via LMN_REON parameter of the instruction FMT_PID ORed with digital input 0 to 7 | INT |
| 60 | Selecting the high limit signal of the position feedback  - -1: Can only be assigned via LMNRHSRE of instruction FMT_PID - 0 to 7: Assignment via LMNRHSRE parameter of the instruction FMT_PID ORed with digital input 0 to 7 | INT |
| 61 | Selecting the low limit signal of the position feedback  - -1: Can only be assigned via LMNRLSRE of instruction FMT_PID - 0 to 7: Assignment via LMNRLSRE parameter of the instruction FMT_PID ORed with digital input 0 to 7 | INT |

---

**See also**

[Description FMT_PAR (S7-300, S7-400)](#description-fmt_par-s7-300-s7-400)
  
[Input parameters FMT_PAR (S7-300, S7-400)](#input-parameters-fmt_par-s7-300-s7-400)
  
[Output parameters FMT_PAR (S7-300, S7-400)](#output-parameters-fmt_par-s7-300-s7-400)
  
[In/out parameters FMT_PAR (S7-300, S7-400)](#inout-parameters-fmt_par-s7-300-s7-400)

## FMT_DS1 (S7-300, S7-400)

This section contains information on the following topics:

- [Description FMT_DS1 (S7-300, S7-400)](#description-fmt_ds1-s7-300-s7-400)
- [Input parameters FMT_DS1 (S7-300, S7-400)](#input-parameters-fmt_ds1-s7-300-s7-400)
- [Output parameter FMT_DS1 (S7-300, S7-400)](#output-parameter-fmt_ds1-s7-300-s7-400)
- [In/out parameters FMT_DS1 (S7-300, S7-400)](#inout-parameters-fmt_ds1-s7-300-s7-400)
- [Assignments of DS1 (S7-300, S7-400)](#assignments-of-ds1-s7-300-s7-400)

### Description FMT_DS1 (S7-300, S7-400)

Instruction FMT_DS1 is available to you for reading the diagnostic data record DS1.

#### Mode of operation

If parameter READ_DS1 = TRUE, then diagnostic data record DS1 is read from FM 355-2 and written to the structure DS1 of the instance DB. Thereafter the in/out parameter is reset.

This only makes sense, if an error is reported in a channel in DS0.

#### Call

FMT_DS1 has to be called in the same OB as all the other instructions that access the same FM 355-2.

FMT_DS1 requires no initialization routine.

To always obtain the updated diagnostic values, set the parameter READ_DS1 cyclically to TRUE in OB 82.

After the diagnostic values have been successfully read, FMT_DS1 resets the parameter READ_DS1.

---

**See also**

[Input parameters FMT_DS1 (S7-300, S7-400)](#input-parameters-fmt_ds1-s7-300-s7-400)
  
[Output parameter FMT_DS1 (S7-300, S7-400)](#output-parameter-fmt_ds1-s7-300-s7-400)
  
[In/out parameters FMT_DS1 (S7-300, S7-400)](#inout-parameters-fmt_ds1-s7-300-s7-400)
  
[Assignments of DS1 (S7-300, S7-400)](#assignments-of-ds1-s7-300-s7-400)

### Input parameters FMT_DS1 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |

---

**See also**

[Description FMT_DS1 (S7-300, S7-400)](#description-fmt_ds1-s7-300-s7-400)
  
[Output parameter FMT_DS1 (S7-300, S7-400)](#output-parameter-fmt_ds1-s7-300-s7-400)
  
[In/out parameters FMT_DS1 (S7-300, S7-400)](#inout-parameters-fmt_ds1-s7-300-s7-400)
  
[Assignments of DS1 (S7-300, S7-400)](#assignments-of-ds1-s7-300-s7-400)

### Output parameter FMT_DS1 (S7-300, S7-400)

| Parameter | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| DS1 | 2.0 | STRUCT |  | The diagnostic data record DS1 contains bytes from 0 to 12. The first 4 bytes are identical with the diagnostic data record DS0. |
| RET_VALU | 16.0 | WORD | W#16#0 | RET_VALU contains the 2nd and 3rd bytes from parameter STATUS of instruction RDREC. |

### In/out parameters FMT_DS1 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| READ_DS1 | 18.0 | BOOL | FALSE | If parameter READ_DS1 = TRUE, then diagnostic data record DS1 is read from FM 355-2 and written to the structure DS1of the instance DB. Thereafter the in/out parameter is reset. |

---

**See also**

[Description FMT_DS1 (S7-300, S7-400)](#description-fmt_ds1-s7-300-s7-400)
  
[Input parameters FMT_DS1 (S7-300, S7-400)](#input-parameters-fmt_ds1-s7-300-s7-400)
  
[Output parameter FMT_DS1 (S7-300, S7-400)](#output-parameter-fmt_ds1-s7-300-s7-400)
  
[Assignments of DS1 (S7-300, S7-400)](#assignments-of-ds1-s7-300-s7-400)

### Assignments of DS1 (S7-300, S7-400)

The following table shows the assignments of diagnostic data record DS1. The first 4 bytes are identical to diagnostic data record DS0. Any bits not listed have no meaning and are zero.

| Byte | Bit | Meaning | Remark |  | Event no. |
| --- | --- | --- | --- | --- | --- |
| 0 | 0 | Module fault | Is set at each diagnostics event |  | 8:x:00 |
| 1 | Internal error | Is set at every internal error:  - Time monitoring addressed - EPROM error - ADU/DAU error - Analog input hardware error |  | 8:x:01 |  |
| 2 | External error | Is set at every external error:  - Missing external auxiliary voltage - Parameter assignment error - Analog input wire break (only in range 4 to 20 mA) - Analog input undershoot of measuring range - Analog input overshoot of measuring range - Analog output load break - Analog output short circuit |  | 8:x:02 |  |
| 3 | Error in one channel | See from byte 7 for further breakdown |  | 8:x:03 |  |
| 4 | Missing external auxiliary voltage | 24 V supply for FM 355-2 failed |  | 8:x:04 |  |
| 6 | Unused | - |  | - |  |
| 7 | Parameter assignment error | The module is unable to use a parameter. Reason: Parameters unknown or illegal combination of parameters. |  | 8:x:07 |  |
| 1 | 0 ... 3 | Module class | 8 is always assigned. |  | - |
| 4 | Channel-specific diagnosis | Is set, when the module can provide additional channel information and a channel error exists (see byte 7 to 12) |  | - |  |
| 2 | 3 | Time monitoring addressed (watchdog) | Hardware error |  | 8:x:33 |
| 3 | 2 | EPROM error | Module defect |  | 8:x:42 |
| 4 | ADU/DAU error | Module defect |  | 8:x:44 |  |
| 4 | 0 ... 7 | Channel type | 75H is always assigned. |  | - |
| 5 | 0 ... 7 | Length of the diagnostics information | 8 is always assigned. |  | - |
| 6 | 0 ... 7 | Number of channels | 5 always assigned (4 controllers + 1 reference channel) |  | - |
| 7 | 0 ... 4 | Channel error vector | One bit is assigned to each channel (0...3; 4 for reference channel). |  | - |
| 8 | 0 | Analog input hardware error | Channel-specific diagnostics channel 0 |  | 8:x:B0 |
| 1 | Unused |  | 8:x:B1 |  |  |
| 2 | Analog input wire break (only in range 4 to 20 mA) |  | 8:x:B2 |  |  |
| 3 | Unused |  | 8:x:B3 |  |  |
| 4 | Analog input undershoot of measuring range |  | 8:x:B4 |  |  |
| 5 | Analog input overshoot of measuring range |  | 8:x:B5 |  |  |
| 6 | Analog output wire break | Only with the current output of the continuous-action controller. | 8:x:B6 |  |  |
| 7 | Analog output short circuit | Only with the voltage output of the continuous-action controller | 8:x:B7 |  |  |
| 9 | 0 ... 7 | See byte 8 | Channel-specific diagnostics channel 1 |  | See above |
| 10 | 0 ... 7 | See byte 8 | Channel-specific diagnostics channel 2 |  | See above |
| 11 | 0 ... 7 | See byte 8 | Channel-specific diagnostics channel 3 |  | See above |
| 12 | 0 ... 5 | See byte 8 | Diagnostics for reference channel |  | See above |

---

**See also**

[Description FMT_DS1 (S7-300, S7-400)](#description-fmt_ds1-s7-300-s7-400)
  
[Input parameters FMT_DS1 (S7-300, S7-400)](#input-parameters-fmt_ds1-s7-300-s7-400)
  
[Output parameter FMT_DS1 (S7-300, S7-400)](#output-parameter-fmt_ds1-s7-300-s7-400)
  
[In/out parameters FMT_DS1 (S7-300, S7-400)](#inout-parameters-fmt_ds1-s7-300-s7-400)

## FMT_TUN (S7-300, S7-400)

This section contains information on the following topics:

- [Description FMT_TUN (S7-300, S7-400)](#description-fmt_tun-s7-300-s7-400)
- [Input parameter FMT_TUN (S7-300, S7-400)](#input-parameter-fmt_tun-s7-300-s7-400)
- [Output parameters FMT_TUN (S7-300, S7-400)](#output-parameters-fmt_tun-s7-300-s7-400)
- [In/out parameters FMT_TUN (S7-300, S7-400)](#inout-parameters-fmt_tun-s7-300-s7-400)
- [Static variables FMT_TUN.OUT (S7-300, S7-400)](#static-variables-fmt_tunout-s7-300-s7-400)

### Description FMT_TUN (S7-300, S7-400)

With instruction FMT_TUN you obtain additional detailed information (e.g. backup controller parameters) during controller optimization.

> **Note**
>
> However, for performing controller optimization the instruction FMT_PID is adequate. You can start optimization and observe the status information with this instruction.

#### Call

FMT_TUN has to be called in the same OB as all the other instructions that access the same FM 355-2.

FMT_TUN requires no initialization routine.

Set parameter READ_OUT cyclically to TRUE to receive constantly the updated values.

After the parameters have been successfully read out, FMT_TUN resets the parameter READ_OUT.

#### Mode of operation

After downloading the controller parameters with LOAD_PAR = TRUE or the operating parameters with LOAD_OP = TRUE the parameters do not take effect immediately. Only after the cycle time of FM355-2 (depending on the number of channels up to 500 ms) the controller parameters are available for reading back with READ_PAR or the output parameters with READ_OUT. This also applies after downloading the system data (CPU transition from STOP to RUN) as well as when reading the output parameters FMT_TUN.

#### Call at distributed configuration

In the case of disturbed configuration and simultaneous call of FMT_PID and FMT_TUN, the following must be noted.

- LOAD_OP must not be set simultaneously at FMT_PID and FMT_TUN.
- READ_OUT must not be set simultaneously at FMT_PID and FMT_TUN.

Reasons: Both instructions access FM355-2 via the same data records. You must therefore make sure that at the same time only one of the two FBs reads or writes a data record at the same time.

---

**See also**

[Input parameter FMT_TUN (S7-300, S7-400)](#input-parameter-fmt_tun-s7-300-s7-400)
  
[Output parameters FMT_TUN (S7-300, S7-400)](#output-parameters-fmt_tun-s7-300-s7-400)
  
[In/out parameters FMT_TUN (S7-300, S7-400)](#inout-parameters-fmt_tun-s7-300-s7-400)
  
[Static variables FMT_TUN.OUT (S7-300, S7-400)](#static-variables-fmt_tunout-s7-300-s7-400)

### Input parameter FMT_TUN (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CHANNEL | 2.0 | INT | 0 | Number of controller channel to which the instance DB refers.   Values from 0 to 3 are permitted. |

---

**See also**

[Description FMT_TUN (S7-300, S7-400)](#description-fmt_tun-s7-300-s7-400)
  
[Output parameters FMT_TUN (S7-300, S7-400)](#output-parameters-fmt_tun-s7-300-s7-400)
  
[In/out parameters FMT_TUN (S7-300, S7-400)](#inout-parameters-fmt_tun-s7-300-s7-400)
  
[Static variables FMT_TUN.OUT (S7-300, S7-400)](#static-variables-fmt_tunout-s7-300-s7-400)

### Output parameters FMT_TUN (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| PI_GAIN | 4.0 | REAL | 0.0 | PI controller parameters |
| PI_TI | 8.0 | REAL | 0.0 | PI controller parameters |
| PID_GAIN | 12.0 | REAL | 0.0 | PID controller parameters |
| PID_TI | 16.0 | REAL | 0.0 | PID controller parameters |
| PID_TD | 20.0 | REAL | 0.0 | PID controller parameters |
| SAV_PFAC | 24.0 | REAL | 0.0 | Saved controller parameters FMT_PID.PAR.PFAC_SP |
| SAV_GAIN | 28.0 | REAL | 0.0 | Saved controller parameters FMT_PID.PAR.GAIN |
| SAV_TI | 32.0 | REAL | 0.0 | Saved controller parameters FMT_PID.PAR.TI |
| SAV_TD | 36.0 | REAL | 0.0 | Saved controller parameters FMT_PID.PAR.TD |
| SAV_D_F | 40.0 | REAL | 0.0 | Saved controller parameters FMT_PID.PAR.D_T |
| SAV_RATI | 44.0 | REAL | 0.0 | Saved controller parameters FMT_PID.PAR.RATIOFAC |
| SAV_CONZ | 48.0 | REAL | 0.0 | Saved controller parameters FMT_PID.PAR.CON_ZONE |
| SAV_PSEL | 52.0 | BOOL | FALSE | Saved controller parameters FMT_PID.PAR.P_SEL |
| SAV_CZON | 52.1 | BOOL | FALSE | Saved controller parameters FMT_PID.PAR.CONZ_ON |
| RET_VALU | 54.0 | WORD | W#16#0 | RET_VALU contains the 2nd and 3rd bytes from parameter STATUS of instruction RDREC. |

### In/out parameters FMT_TUN (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| READ_OUT | 56.0 | BOOL | FALSE | If the in/out parameter READ_OUT is set, the output parameters are read from FM 355-2. |

---

**See also**

[Description FMT_TUN (S7-300, S7-400)](#description-fmt_tun-s7-300-s7-400)
  
[Input parameter FMT_TUN (S7-300, S7-400)](#input-parameter-fmt_tun-s7-300-s7-400)
  
[Output parameters FMT_TUN (S7-300, S7-400)](#output-parameters-fmt_tun-s7-300-s7-400)
  
[Static variables FMT_TUN.OUT (S7-300, S7-400)](#static-variables-fmt_tunout-s7-300-s7-400)

### Static variables FMT_TUN.OUT (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| vers_nr | 58.0 | WORD | W#16#3230 | The vers_nr parameter may not be modified by users. It marks the start of the output parameter that is read by the module if READ_OUT = TRUE is set. |
| PV | 60.0 | REAL | 0.0 | Process value that becomes effective. |
| LMN | 64.0 | REAL | 0.0 | The effective manipulated value that is currently in effect is output at output LMN.  For step controller without analog position feedback the unlimited P- + D-action is output at output LMN.  Values from -100.0 to 100.0 (%) are permitted. |
| QLMNSAFE | 68.1 | BOOL | FALSE | If output QLMNSAFE is set, the safety manipulated value is output as manipulated value. |
| QLMNTRK | 68.3 | BOOL | FALSE | Output QLMNTRK indicates if the manipulated value is being compensated via an analog input. |
| QLMN_RE | 68.4 | BOOL | FALSE | The output QLMN_RE indicates if LMN_REON is set and the external manipulated value LMN_RE is applied as the manipulated value. |
| QLMNR_HS | 68.5 | BOOL | FALSE | QLMNR_HS = TRUE means: Control valve is at the high endstop. (Only in the case of step controllers) |
| QLMNR_LS | 68.6 | BOOL | FALSE | QLMNR_LS = TRUE means: The control valve is located at the low endstop.  (Only in the case of step controllers) |
| QLMNR_ON | 68.7 | BOOL | FALSE | QLMNR_ON = TRUE means:  Step controller with position feedback. |
| QSTEPCON | 69.0 | BOOL | FALSE | Step controllers/pulse controllers  0 = Pulse controller or continuous controller   1 = step controller |
| QSPR | 69.1 | BOOL | FALSE | If output QSPR is set, the continuous controller works in the split-range mode. |
| QMAN_FC | 69.3 | BOOL | FALSE | The controller is a master controller that is adjusted by the manual mode of a slave controller to its process value or its I-action is stopped, because the setpoint or manipulated value of the slave controller lies in the limit. |
| QH_ALM | 70.0 | BOOL | FALSE | High limit H_ALM exceeded by process value or error signal. |
| QH_WRN | 70.1 | BOOL | FALSE | Process value or error signal exceeds second to highest limit H_WRN. |
| QL_WRN | 70.2 | BOOL | FALSE | Process value or error signal has dropped below the second to lowest limit L_WRN. |
| QL_ALM | 70.3 | BOOL | FALSE | Process value or error signal has dropped below the lowest limit L_ALM. |
| QLMN_HLM | 70.4 | BOOL | FALSE | The output QLMN_HLM reports that the high manipulated value limit LMN_HLM. has been reached.   (Does not apply to step controllers without analog position feedback). |
| QLMN_LLM | 70.5 | BOOL | FALSE | The output QLMN_LLM reports that the high manipulated value limit LMN_LLM has been reached.  (Does not apply to step controllers without analog position feedback) |
| QPAR_F | 70.6 | BOOL | FALSE | The module checks the parameters for validity. A parameter assignment error is indicated on output QPAR_F. |
| QCH_F | 70.7 | BOOL | FALSE | The output QCH_F is set if the controller channel is unable to supply any valid results. A channel error (for example, wire break) is also set if QPAR_F = 1 or QMOD_F = 1. If QCH_F = TRUE, then the precise error information in the diagnostic data record DS1 of the module is read out. |
| QUPRLM | 71.0 | BOOL | FALSE | The setpoint is limited to a positive and negative gradient.  If the output QUPRLM is set, the setpoint rise is limited. |
| QDNRLM | 71.1 | BOOL | FALSE | The setpoint is limited to a positive and negative gradient.  If the output QDNRLM is set, the setpoint fall is limited. |
| QSP_HLM | 71.2 | BOOL | FALSE | The output QSP_HLM reports that the high setpoint limit SP_HLM has been reached. |
| QSP_LLM | 71.3 | BOOL | FALSE | The output QSP_LLM reports that the low setpoint limit SP_LLM has been reached. |
| QLMNUP | 71.4 | BOOL | FALSE | "Manipulated value signal up" output.   (Only in the case of step controllers or pulse controllers) |
| QLMNDN | 71.5 | BOOL | FALSE | "Manipulated value signal down" output.  (Only in the case of step controllers or pulse controllers) |
| QTUN_ON | 71.6 | BOOL | FALSE | QTUN_ON = TRUE indicates that optimization is in progress. |
| PAR_ACT | 71.7 | BOOL | FALSE | Updating controller parameters |
| SP | 72.0 | REAL | 0.0 | Effective actual setpoint. |
| ER | 76.0 | REAL | 0.0 | Negative deviation |
| DISV | 80.0 | REAL | 0.0 | Effective actual disturbance variable.   Values from -100.0 to 100.0 (%) are permitted. |
| LMN_A | 84.0 | REAL | 0.0 | In the case of continuous or pulse controllers of manipulated value A of the split-range function and for step controllers with analog position feedback, the position feedback is displayed on output LMN_A.   Values from -100.0 to 100.0 (%) are permitted. |
| LMN_B | 88.0 | REAL | 0.0 | On output LMN_B, in the case of continuous or pulse controllers, manipulated value B of the split-range function is displayed.  Values from -100.0 to 100.0 (%) are permitted. |
| PHASE | 92.0 | INT | 0 | Indicates the controller optimization phases. <sup>*)</sup>  0..7 |
| STATUS_H | 94.0 | INT | 0 | Diagnostics value for searching for point of inflection during heating optimization   See [parameter FMT_PID.STATUS_H](#parameters-status_h-s7-300-s7-400) |
| STATUS_C | 96.0 | INT | 0 | Diagnostics value for searching for point of inflection during cooling optimization.   See [parameter FMT_PID.STATUS_C](#parameters-status_c-s7-300-s7-400) |
| STATUS_D | 98.0 | INT | 0 | Diagnostics value for controller design during heating optimization  See [parameter FMT_PID.STATUS_D](#parameters-status_d-s7-300-s7-400) |
| ZONE_TUN | 100.0 | WORD | W#16#0 | In HEX code, each one of the four digits represents one channel, arranged in the following order from left to right: Channel 0, 1, 2, 3. ZONE_TUN = 0 means that the channel selected will not be optimized together with other channels. A value <> 0000 shows - in each case with a 1 - the channels which will be optimized as a group. |
| GAIN_P | 152.0 | REAL | 0.0 | Identified steady state gain (phys. variable) /%.   In the case of process type I, GAIN_P tends to be estimated too low. |
| TU | 156.0 | REAL | 0.0 | Identified time lag of process.  TU≥ 3*Sampling time |
| TA | 160.0 | REAL | 0.0 | Identified recovery time of process.   In the case of process type I, TA tends to be estimated too low. |
| KIG | 164.0 | REAL | 0.0 | Maximum possible rate of rise of the process value. (phys. variable) /s  GAIN_P = 0.01 * KIG * TA |
| N_PTN | 168.0 | REAL | 0.0 | Order of the process "Non-integer values" are also possible.  Values from 0.1 to 10.0 are permitted. |
| TM_LAG_P | 172.0 | REAL | 0.0 | Time constant of a PTN model.  (practical values for N_PTN>=2 only). |
| T_P_INF | 176.0 | REAL | 0.0 | Time from process excitation to inflection point. |
| P_INF | 180.0 | REAL | 0.0 | Change in process value from process excitation to inflection point. |
| LMN0 | 184.0 | REAL | 0.0 | Manipulated value at the start of optimization  Is established in phase 1 (average)  Values from -100.0 to 100.0 (%) are permitted. |
| PV0 | 188.0 | REAL | 0.0 | Process value at the start of optimization  Is established in phase 1 (average). |
| PVDT0 | 192.0 | REAL | 0.0 | Process value slew rate at the start of optimization  Sign is adapted.   (phys. variable) /s |
| PVDT | 196.0 | REAL | 0.0 | Current process value slew rate  Sign is adapted.  (phys. variable) /s |
| PVDT_MAX | 200.0 | REAL | 0.0 | Maximal process value modification (phys. variable) /s  Maximum derivative of the process value at the point of inflection (sign adapted, always > 0); is used to calculate TU and KIG. |
| NOI_PVDT | 204.0 | REAL | 0.0 | Noise action in PVDT_MAX in %  The larger the noise action, the less precise (softer) are the controller parameters. |
| NOISE_PV | 208.0 | REAL | 0.0 | Absolute process value noise action (phys. variable) /s  The difference between maximum and minimum process value in phase 1. |
| FIL_CYC | 212.0 | INT | 0 | Number of cycles of the mean value filter  The process value is determined through FIL_CYC cycles. FIL_CYC is increased from 1 to a max. of 1024 if needed. |
| POI_CMAX | 214.0 | INT | 0 | Maximum number of cycles after inflection point  This time is used to find another (i.e. better) inflection point in case of measuring noise. Only then is optimization completed. |
| POI_CYCL | 216.0 | INT | 0 | Number of cycles after inflection point |

---

**See also**

[Description FMT_TUN (S7-300, S7-400)](#description-fmt_tun-s7-300-s7-400)
  
[Input parameter FMT_TUN (S7-300, S7-400)](#input-parameter-fmt_tun-s7-300-s7-400)
  
[Output parameters FMT_TUN (S7-300, S7-400)](#output-parameters-fmt_tun-s7-300-s7-400)
  
[In/out parameters FMT_TUN (S7-300, S7-400)](#inout-parameters-fmt_tun-s7-300-s7-400)
  
[Parameters STATUS_H (S7-300, S7-400)](#parameters-status_h-s7-300-s7-400)
  
[Parameters STATUS_C (S7-300, S7-400)](#parameters-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

## FMT_PV (S7-300, S7-400)

This section contains information on the following topics:

- [Description FMT_PV (S7-300, S7-400)](#description-fmt_pv-s7-300-s7-400)
- [Input parameter FMT_PV (S7-300, S7-400)](#input-parameter-fmt_pv-s7-300-s7-400)
- [Output parameter FMT_PV (S7-300, S7-400)](#output-parameter-fmt_pv-s7-300-s7-400)
- [in/out parameters FMT_PV (S7-300, S7-400)](#inout-parameters-fmt_pv-s7-300-s7-400)

### Description FMT_PV (S7-300, S7-400)

Instruction FMT_PV is for reading or writing process values (analog and digital input values) to support startup.

#### Call

FMT_PV has to be called in the same OB as all the other instructions that access the same FM 355-2.

FMT_PV requires no initialization routine.

Set parameter LOAD_PV cyclically to TRUE if you wish to write cyclically simulated process values to FM 355-2.

Set parameter READ_PV cyclically to TRUE to receive constantly the updated process values.

After the diagnostic values have been successfully written or read, FMT_PV resets the parameter LOAD_PV or READ_PV .

#### Simulation of the analog values (LOAD_PV = TRUE)

The simulation of the analog value for the channels 0 to 3 is enabled via the switches S_AION[ i ] or S_PVON[ i ], where 0 ≤ i ≤ 3. The figure below shows the point at which the simulated analog value becomes effective.

You specify the simulation values for the channels 0 to 3 via the parameter PV_SIM[ i ].

You can have the simulation values become effective at two points:

- S_AION[ i ] = TRUE (0 ≤ i ≤ 3)

  The value PV_SIM[ i ] is used instead of the value of analog input i of the module.
- S_PVON[ i ] = TRUE (0 ≤ i ≤ 3)

  The value PV_SIM[ i ] is used instead of the conditioned value of analog input i of the module.

#### Simulation of the digital values (LOAD_PV = TRUE)

The simulation of the values for the digital inputs 0 to 7 is enabled via the switches S_DION[ i ], where 0 ≤ i ≤ 7 is.

You lay down the simulation values via parameter DI_SIM[ i ].

- S_DION[ i ] = TRUE (0 ≤ i ≤ 7)

  Instead of the value of digital input i of the module, the value DI_SIM[ i ] is used.

  > **Note**
  >
  > LEDs I0 to I7 always display the state of the associated digital input, also during simulation.

  ![Simulation of the digital values (LOAD_PV = TRUE)](images/18650204427_DV_resource.Stream@PNG-en-US.png)

  > **Note**
  >
  > Enabling and specification of the simulation values (Force) does not take place via the configuration software. This is why the relevant switches and connecting lines are drawn as dotted lines.

#### Displaying the process values (READ_PV = TRUE)

The following values are displayed:

- The actual state of digital inputs 0 to 7 are displayed at parameters STAT_DI[0] to STAT_DI[7], even if these are simulated.
- The value of analog inputs 0 to 3 is displayed on parameters DIAG[0].PV_PER to DIAG[3].PV_PER in mA or mV units. If the simulation of the analog input value was enabled, the simulated value is displayed.
- The conditioned analog input value 0 to 3 is displayed on parameters DIAG[0].PV_PHY to DIAG[3].PV_PHY in physical unit. If the simulation of the conditioned physical analog input value was enabled, the simulated value is displayed.

  ![Displaying the process values (READ_PV = TRUE)](images/18650913931_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> The updating of the process values can be delayed if FM 355-2 is loaded compared to instruction FMT_PID.

#### Start-up

When FM 355-2 restarts after power off, the simulation switches on the FM 355-2 are again set to FALSE.

---

**See also**

[Input parameter FMT_PV (S7-300, S7-400)](#input-parameter-fmt_pv-s7-300-s7-400)
  
[Output parameter FMT_PV (S7-300, S7-400)](#output-parameter-fmt_pv-s7-300-s7-400)
  
[in/out parameters FMT_PV (S7-300, S7-400)](#inout-parameters-fmt_pv-s7-300-s7-400)

### Input parameter FMT_PV (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| S_AION | 0.0 | ARRAY [0..3] of BOOL | FALSE | If, for example, the S_AION[1] switch is set to TRUE, the value PV_SIM[1] is used instead of the analog input value 1 of the module. |
| S_PVON | 2.0 | ARRAY [0..3] of BOOL | FALSE | If, for example, the S_PVON[1] switch is set to TRUE, the value PV_SIM[1] is used instead of the conditioned analog input value 1 of the module. |
| PV_SIM | 4.0 | ARRAY [0..3] of REAL | 0.0 | The simulation value for the analog input 1 is specified, for example, at input PV_SIM[1]. If S_PVON = TRUE, then the conditioned analog input value is specified here. If S_PVON = FALSE and S_AION = TRUE, then the analog input value, which is transformed into a conditioned value by means of the conditioning functions, is specified in mA or mV.   0.0 to 20.0 [mA] or  -1500 to +10000 [mV] or technical value range |
| S_DION | 20.0 | ARRAY [0..7] of BOOL | FALSE | If, for example, the S_DION[1] switch is set to TRUE, the value DI_SIM[1] is used instead of the digital input value 1 of the module. |
| DI_SIM | 22.0 | ARRAY [0..7] of BOOL | FALSE |  |
| MOD_ADDR | 24.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |

---

**See also**

[Description FMT_PV (S7-300, S7-400)](#description-fmt_pv-s7-300-s7-400)
  
[Output parameter FMT_PV (S7-300, S7-400)](#output-parameter-fmt_pv-s7-300-s7-400)
  
[in/out parameters FMT_PV (S7-300, S7-400)](#inout-parameters-fmt_pv-s7-300-s7-400)

### Output parameter FMT_PV (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| STAT_DI | 26.0 | ARRAY [0..7] of BOOL | FALSE | The states of digital inputs 0 to 7 are displayed at the STAT_DI parameters. |
| DIAG[x].PV_PER | 28+  (Channel number x8) | ARRAY [0..3] of STRUCT | 0.0 | The analog input value of the module is displayed, for example, in the units mA or mV, at the DIAG[x].PV_PER parameter. |
| DIAG[x].PV_PHY | 32+ (Channel number x8) | ARRAY [0..3] of STRUCT | 0.0 | The DIAG[x].PV_PHY parameter, for example, displays the conditioned analog input value of the module in the physical unit. |
| RET_VALU | 60.0 | WORD | W#16#0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the instructions RDREC and WRREC. |

### in/out parameters FMT_PV (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| LOAD_PV | 62.0 | BOOL | FALSE | When the in/out parameter LOAD_PV is set, the simulation values in PV_SIM and DI_SIM are written to FM 355-2 in accordance with the switch positions and the in/out parameter is reset. |
| READ_PV | 62.1 | BOOL | FALSE | If the parameter READ_PV = TRUE, the reference junction temperature is read from the module. Thereafter the in/out parameter is reset. |

---

**See also**

[Description FMT_PV (S7-300, S7-400)](#description-fmt_pv-s7-300-s7-400)
  
[Input parameter FMT_PV (S7-300, S7-400)](#input-parameter-fmt_pv-s7-300-s7-400)
  
[Output parameter FMT_PV (S7-300, S7-400)](#output-parameter-fmt_pv-s7-300-s7-400)

## FMT_CJ_T (S7-300, S7-400)

This section contains information on the following topics:

- [Description FMT_CJ_T (S7-300, S7-400)](#description-fmt_cj_t-s7-300-s7-400)
- [Input parameters FMT_CJ_T (S7-300, S7-400)](#input-parameters-fmt_cj_t-s7-300-s7-400)
- [Output parameters FMT_CJ_T (S7-300, S7-400)](#output-parameters-fmt_cj_t-s7-300-s7-400)
- [In/out parameters FMT_CJ_T (S7-300, S7-400)](#inout-parameters-fmt_cj_t-s7-300-s7-400)

### Description FMT_CJ_T (S7-300, S7-400)

Instruction FMT_CJ_T is for reading the measured reference junction temperature and for changing the parameterized reference junction temperature online. This is necessary if a temperature control system with several FM 355-2 with thermoelement inputs is to be operated without having to connect a Pt 100 to each FM 355-2.

#### Call

FMT_PAR has to be called in the same OB as all the other instructions that access the same FM 355-2.

If FM 355-2 is used in distributed I/O, it may take a few call cycles until the parameters are applied to FM 355-2. As long as the transfer has not been completed, parameter LOAD_CJ retains the value TRUE. So keep repeating your call of FMT_CJ_T when modifying parameters until the block sets LOAD_CJ = FALSE.

#### Mode of operation

If, for example, an FM 355-2 measures the reference junction temperature of an extruder control system with more than four heating zones, it can be read with READ_CJ = TRUE on parameter CJ_T_OUT and can be parameterized for the other FM 355-2 via CJ_TEMP and LOAD_CJ.

On parameter CJ_T_OUT the reference junction temperature measured at the reference point is expressed in degrees C or in degrees F (depending on which temperature unit has been parameterized).

On parameter CJ_T_OUT 0.0. is displayed if:

- no sensor of the "Thermoelement" type has been parameterized,
- the parameterized reference junction temperature was selected on all analog inputs,
- the internal compensation was selected on all analog inputs.

---

**See also**

[Input parameters FMT_CJ_T (S7-300, S7-400)](#input-parameters-fmt_cj_t-s7-300-s7-400)
  
[Output parameters FMT_CJ_T (S7-300, S7-400)](#output-parameters-fmt_cj_t-s7-300-s7-400)
  
[In/out parameters FMT_CJ_T (S7-300, S7-400)](#inout-parameters-fmt_cj_t-s7-300-s7-400)

### Input parameters FMT_CJ_T (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CJ_TEMP | 2.0 | REAL | 0.0 | The reference junction temperature can be specified at parameter CJ_TEMP. |

---

**See also**

[Description FMT_CJ_T (S7-300, S7-400)](#description-fmt_cj_t-s7-300-s7-400)
  
[Output parameters FMT_CJ_T (S7-300, S7-400)](#output-parameters-fmt_cj_t-s7-300-s7-400)
  
[In/out parameters FMT_CJ_T (S7-300, S7-400)](#inout-parameters-fmt_cj_t-s7-300-s7-400)

### Output parameters FMT_CJ_T (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| CJ_T_OUT | 6.0 | REAL | 0.0 | At the CJ_T_OUT output, the measured reference junction temperature is displayed by the module if a thermocouple element input is configured and the reference junction temperature is not configured. |
| RET_VALU | 10.0 | WORD | W#16#0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the instructions RDREC and WRREC. |

### In/out parameters FMT_CJ_T (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| LOAD_CJ | 12.0 | BOOL | FALSE | If the in/out parameter LOAD_CJ has been set, the configured reference junction temperature on the module is overwritten with the value CJ_TEMP and the in/out parameter is reset. |
| READ_CJ | 12.1 | BOOL | FALSE | If the parameter READ_CJ = TRUE, the reference junction temperature is read from the module. Thereafter the in/out parameter is reset. |

---

**See also**

[Description FMT_CJ_T (S7-300, S7-400)](#description-fmt_cj_t-s7-300-s7-400)
  
[Input parameters FMT_CJ_T (S7-300, S7-400)](#input-parameters-fmt_cj_t-s7-300-s7-400)
  
[Output parameters FMT_CJ_T (S7-300, S7-400)](#output-parameters-fmt_cj_t-s7-300-s7-400)
