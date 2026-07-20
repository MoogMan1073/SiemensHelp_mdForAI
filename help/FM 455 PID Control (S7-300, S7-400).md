---
title: "FM 455 PID Control (S7-300, S7-400)"
package: ProgFBFM455enUS
topics: 63
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# FM 455 PID Control (S7-300, S7-400)

This section contains information on the following topics:

- [PID_FM_455 (S7-300, S7-400)](#pid_fm_455-s7-300-s7-400)
- [FUZ_455 (S7-300, S7-400)](#fuz_455-s7-300-s7-400)
- [FORCE455 (S7-300, S7-400)](#force455-s7-300-s7-400)
- [READ_455 (S7-300, S7-400)](#read_455-s7-300-s7-400)
- [CH_DIAG_455 (S7-300, S7-400)](#ch_diag_455-s7-300-s7-400)
- [PID_PAR_455 (S7-300, S7-400)](#pid_par_455-s7-300-s7-400)
- [CJ_T_PAR_455 (S7-300, S7-400)](#cj_t_par_455-s7-300-s7-400)
- [LP_ZONE (S7-300, S7-400)](#lp_zone-s7-300-s7-400)
- [ADM_ZONE (S7-300, S7-400)](#adm_zone-s7-300-s7-400)
- [ZONE (S7-300, S7-400)](#zone-s7-300-s7-400)
- [DB for HMI (S7-300, S7-400)](#db-for-hmi-s7-300-s7-400)

## PID_FM_455 (S7-300, S7-400)

This section contains information on the following topics:

- [Description PID_FM_455 (S7-300, S7-400)](#description-pid_fm_455-s7-300-s7-400)
- [Mode of operation PID_FM_455 (S7-300, S7-400)](#mode-of-operation-pid_fm_455-s7-300-s7-400)
- [Input parameters PID_FM_455 (S7-300, S7-400)](#input-parameters-pid_fm_455-s7-300-s7-400)
- [Output parameters PID_FM_455 (S7-300, S7-400)](#output-parameters-pid_fm_455-s7-300-s7-400)
- [In/out parameters PID_FM_455 (S7-300, S7-400)](#inout-parameters-pid_fm_455-s7-300-s7-400)
- [Block diagram PID_FM_455 (S7-300, S7-400)](#block-diagram-pid_fm_455-s7-300-s7-400)

### Description PID_FM_455  (S7-300, S7-400)

During operation, the instruction PID_FM_455 is used to:

- Transfer operating parameters to FM 455
- Transfer controller parameters to FM 455
- Read process values from FM 455

Operating parameters are all in/out parameters that lie between the op_par and cont_par parameters in the instance data block of the instruction.

Controller parameters are all in/out parameters that are located after the cont_par parameter in the instance data block of the instruction.

Process values are all output parameters of the instruction after the out_par parameter.

The required data are stored in an instance DB on the CPU. You need one instance DB for each controller channel used. All the in/out parameters are set to FALSE after an instance DB has been created.

#### Call

PID_FM_455 is normally called in the cyclic interrupt OB 35 and requires an initialization routine that is started by setting the parameter COM_RST = TRUE in the start-up of the CPU. A calling of the instruction in the start-up OB is possible, but not necessary. After the initialization routine, PID_FM_455 sets the parameter COM_RST to FALSE.

PID_FM_455 has to be called in the same OB as all the other instructions that access the same FM 455.

If you call the instruction PID_FM_455 as a multiple instance DB, no commissioning interface is available. In this case you must commission the FM 455 via a watch table.

#### Startup

During CPU start-up and during CPU STOP-RUN transition, the parameters on the FM 455 are overwritten with the parameters from the SDB of the CPU.

#### Reaction to error

The output parameter RET_VALU includes the return value RET_VAL of the RD_REC and WR_REC instructions. RET_VALU can be evaluated if the READ_VAR and LOAD_PAR parameters are not reset.

When the instruction PID_FM_455 is called, an I/O access error can occur if the FM 455 is not plugged or is not supplied with voltage. In this case the CPU goes into STOP, if no OB 122 is loaded in the CPU.

---

**See also**

[Mode of operation PID_FM_455 (S7-300, S7-400)](#mode-of-operation-pid_fm_455-s7-300-s7-400)
  
[Input parameters PID_FM_455 (S7-300, S7-400)](#input-parameters-pid_fm_455-s7-300-s7-400)
  
[Output parameters PID_FM_455 (S7-300, S7-400)](#output-parameters-pid_fm_455-s7-300-s7-400)
  
[In/out parameters PID_FM_455 (S7-300, S7-400)](#inout-parameters-pid_fm_455-s7-300-s7-400)
  
[Block diagram PID_FM_455 (S7-300, S7-400)](#block-diagram-pid_fm_455-s7-300-s7-400)

### Mode of operation PID_FM_455  (S7-300, S7-400)

#### Effect of parameters LOAD_OP, READ_VAR and LOAD_PAR

In the initialization routine PID_FM_455 reads the parameters from the system data and stores them in its instance DB. Instance DB and system data are synchronized.

The following table shows how the function of the instruction is influenced by the parameters LOAD_OP, READ_VAR and LOAD_PAR.

| Parameters | TRUE | FALSE |
| --- | --- | --- |
| LOAD_OP | Using the instruction WR_REC to transfer the operating parameters from the CPU to FM 455 | Using direct I/O access in multiplex mode to transfer the operating parameters from the CPU to FM 455 |
| Longer run time | Shorter run time |  |
| The values are effective after a cycle of the CPU or FM. The longer cycle is decisive. | A maximum of 3 cycles of the CPU or FM are required until the values are effective. The longer cycle is decisive |  |
| READ_VAR | Using the instruction RD_REC to read the process value from FM 455 | Using direct I/O access in multiplex mode to read the process values from FM 455 |
| Longer processing time | Shorter processing time |  |
| All parameters are read from FM 455 | The following parameters are **not** read from FM 455  - SP (setpoint from the FM) - ER (error signal) - DISV (disturbance variable) - LMN_A - LMN_B |  |
| Following parameters are updated at **every**  call of the instruction.  - PV (process value) - LMN (manipulated value) - The binary displays | Following parameters are updated at every **fourth** call of the instruction.  - PV (process value) - LMN (manipulated value) - The binary displays |  |
| At the start-up of the CPU, the following values are applied from the FM 455 to the PID_FM_455.  - SP_OP - LMN_OP - SP_OP_ON - LMNOP_ON   If these values were changed on the CPU, they are overwritten with the values from the FM 455 at the next start-up of the CPU | At the start-up of the CPU, the following values are read from the instruction, not from the FM:  - SP_OP - LMN_OP - SP_OP_ON - LMNOP_ON |  |
| LOAD_PAR | All controller parameters are downloaded from the CPU to FM 455. This is practical if the controller parameters are to be changed depending on process states. | No transfer of the controller parameters |

After data transfer as been completed the parameters LOAD_OP, READ_VAR and LOAD_PAR are reset to FALSE.

#### Special features during transfer in multiplex mode

Multiplexing of the data to be transferred during access to the FM 455 via direct I/O accesses is controlled via the PID_FM_455. This multiplex controlling via PID_FM_455 does not function if two instances of the instruction PID_FM_455 access the same channel number of a module. This results in incorrect parameters in the FM 455 (for example, setpoint and manual manipulated value) and incorrect displays at the output parameters of the instruction PID_FM_455.

#### Saving the Parameters in EEPROM

During program controlled re-configuring (LOAD_PAR, LOAD_OP) of the controller module by the instruction PID_FM_455, its run time is extended. The new parameters are effective immediately and are stored additionally in a nonvolatile memory (EEPROM). After each saving of the parameters in the EEPROM, a renewed saving is delayed by 30 minutes, since the life of the EEPROM is limited by the number of write processes. It is possible to save the new parameter in the EEPROM as soon as the power supply returns. The selection of the parameters determines whether the reconfiguration of the controller module by the instruction PID_FM_455 is executed without bumps.

#### Processing times of the PID_FM_455

| Boundary conditions |  |  | Processing time in  CPU 414-2DP |
| --- | --- | --- | --- |
| READ_VAR | LOAD_OP | LOAD_PAR |  |
| FALSE | FALSE | FALSE | 0.077 ms |
| TRUE | FALSE | FALSE | 2.36 ms |
| TRUE*) | TRUE | FALSE | 4.48 ms |
| FALSE | FALSE | TRUE | 2.59 ms |
| TRUE | FALSE | TRUE | 5.15 ms |
| TRUE*) | TRUE | TRUE | 7.1 ms |
| *) If LOAD_OP = TRUE, READ_VAR is also set to TRUE by the PID_FM_455. |  |  |  |

---

**See also**

[Description PID_FM_455 (S7-300, S7-400)](#description-pid_fm_455-s7-300-s7-400)
  
[Input parameters PID_FM_455 (S7-300, S7-400)](#input-parameters-pid_fm_455-s7-300-s7-400)
  
[Output parameters PID_FM_455 (S7-300, S7-400)](#output-parameters-pid_fm_455-s7-300-s7-400)
  
[In/out parameters PID_FM_455 (S7-300, S7-400)](#inout-parameters-pid_fm_455-s7-300-s7-400)
  
[Block diagram PID_FM_455 (S7-300, S7-400)](#block-diagram-pid_fm_455-s7-300-s7-400)

### Input parameters PID_FM_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CHANNEL | 2.0 | INT | 1 | The number of the controller channel to which the instance DB is referenced is configured at the "Channel number" input.  Values of 1 to 16 are permitted. |
| PHASE | 4.0 | INT | 0 | The parameter PHASE can be interconnected with the output parameter PHASE of the instructions TUN_EC or TUN_ES (PID self-tuner). The phase state of the PID Self-Tuner can then be displayed in plain text in the "Commissioning" dialog. This parameter is of no significance for the OP. |

---

**See also**

[Description PID_FM_455 (S7-300, S7-400)](#description-pid_fm_455-s7-300-s7-400)
  
[Mode of operation PID_FM_455 (S7-300, S7-400)](#mode-of-operation-pid_fm_455-s7-300-s7-400)
  
[Output parameters PID_FM_455 (S7-300, S7-400)](#output-parameters-pid_fm_455-s7-300-s7-400)
  
[In/out parameters PID_FM_455 (S7-300, S7-400)](#inout-parameters-pid_fm_455-s7-300-s7-400)
  
[Block diagram PID_FM_455 (S7-300, S7-400)](#block-diagram-pid_fm_455-s7-300-s7-400)

### Output parameters PID_FM_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 6.0 | WORD | 0 | RET_VALU contains the return value RET_VAL of the WR_REC and RD_REC instructions. RET_VALU can be evaluated when QMOD_F reports an error. |
| out_par | 8.0 | WORD | W#16#3130 | The out_par parameter may not be modified by users. It marks the start of the output parameter that is read by the module if READ_VAR = TRUE is set. |
| SP | 10.0 | REAL | 0.0 | The setpoint that is currently in effect is available at the "Setpoint" output. |
| PV | 14.0 | REAL | 0.0 | The process value that becomes effective is issued on the "Process value" output. |
| ER | 18.0 | REAL | 0.0 | The control deviation that becomes effective is issued on the "Control deviation" output. |
| DISV | 22.0 | REAL | 0.0 | The interference that becomes effective is issued on the "Interference" output.  Values from -100 to 100 % are permitted. |
| LMN | 26.0 | REAL | 0.0 | The manipulated value that becomes effective is issued on the "Manipulated value" output. Step controllers without analog position feedback output the unlimited P- + D-action at the LMN parameter.  Values from -100 to 100 % are permitted. |
| LMN_A | 30.0 | REAL | 0.0 | At the output "Manipulated value A of the split range function / position feedback", continuous controllers display the manipulated value A and step controllers with analog position feedback display the position feedback.  The output LMN_A can only be used for an approximate display of a corresponding simulated manipulated variable. The start value LMNRSVAL of the simulated position feedback has to be configured accordingly and becomes effective when LMNRS_ON is set.  Values from -100 to 100 % are permitted. |
| LMN_B | 34.0 | REAL | 0.0 | Continuous controllers display the manipulated value B of the split-range function at the output “Manipulated value B of split-range function”.  Values from -100 to 100 % are permitted. |
| QH_ALM | 38.0 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of H_ALM limit is reported at the output "High limit alarm triggered". |
| QH_WRN | 38.1 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of H_WRN limit is reported at the output "High limit warning triggered". |
| QL_WRN | 38.2 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of the L_WRN limit is reported at output "Low limit warning triggered". |
| QL_ALM | 38.3 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of the L_ALM limit is reported at output "Low limit alarm triggered". |
| QLMN_HLM | 38.4 | BOOL | FALSE | The manipulated value is always limited to a high and a low limit. Violation of the high limit is reported at output "High limit of manipulated value triggered".  (Does not apply to step controllers without analog position feedback) |
| QLMN_LLM | 38.5 | BOOL | FALSE | The manipulated value is always limited to a high and a low limit. Violation of the low limit is reported at output "Low limit of manipulated value triggered".  (Does not apply to step controllers without analog position feedback) |
| QPARA_F | 38.6 | BOOL | FALSE | The module checks the validity of the parameters. A parameter assignment error is displayed at the "Parameter assignment error" output. These parameter assignment errors can also be read out in the module's "Online & Diagnostics" dialog. |
| QCH_F | 38.7 | BOOL | FALSE | The "Channel error" output is set if the controller channel cannot provide valid results. A channel error (for example, wire break) is also set if QPARA_F = 1 or QMOD_F = 1. If QCH_F = TRUE, then the precise error information in the diagnostic data record DS1 of the module is read out. |
| QUPRLM | 39.0 | BOOL | FALSE | The setpoint is limited to a positive and negative slew rate. If the output "Limit of positive setpoint slew rate triggered" is set, the positive setpoint slew rate is limited. |
| QDNRLM | 39.1 | BOOL | FALSE | The setpoint is limited to a positive and negative slew rate. If the output "Limit of negative setpoint slew rate triggered" is set, the setpoint fall is limited. |
| QSP_HLM | 39.2 | BOOL | FALSE | The setpoint is always limited to a high and a low limit. The output "High limit of setpoint value triggered" indicates that the high limit has been exceeded. |
| QSP_LLM | 39.3 | BOOL | FALSE | The setpoint is always limited to a high and a low limit. Violation of the low limit is reported at output "Setpoint low limit triggered". |
| QLMNUP | 39.4 | BOOL | FALSE | This is the "Manipulated value signal up" output.  (Only in the case of step controllers or pulse controllers) |
| QLMNDN | 39.5 | BOOL | FALSE | This is the "Manipulated value signal down" output.  (Only in the case of step controllers or pulse controllers) |
| QID | 39.6 | BOOL | FALSE | QID = TRUE indicates that an identification is running (not that it is enabled). On completion of the identification, the identification result can be read out from the IDSTATUS parameter of the instruction CH_DIAG_455. |
| QSPOPON | 40.0 | BOOL | FALSE | The output "Setpoint operation on" shows if the setpoint is being operated by the configuration tool. If the bit is set, the value SP_OP is applied as setpoint. |
| QLMNSAFE | 40.1 | BOOL | FALSE | If the output "Safety mode" is set, the safety manipulated value is output as the manipulated value. |
| QLMNOPON | 40.2 | BOOL | FALSE | The output “Manipulated value operation on” indicates whether the manipulated value is being operated via the configuration tool. If the bit is set, the value LMN_OP is applied as manipulated value. |
| QLMNTRK | 40.3 | BOOL | FALSE | The output "Follow-up mode" indicates if the manipulated value is being adjusted via an analog input. |
| QLMN_RE | 40.4 | BOOL | FALSE | The output "Manual = 1; Automatic = 0" indicates whether or not the manipulated value is set on the external manipulated value LMN_RE (manual = 1). |
| QLMNR_HS | 40.5 | BOOL | FALSE | The output "High endstop signal of position feedback" indicates if the control valve is at its high endstop. QLMNR_HS = TRUE means: The control valve is at high endstop.  (For step controllers only) |
| QLMNR_LS | 40.6 | BOOL | FALSE | The output "Low endstop signal of position feedback" indicates whether the control valve is at its low endstop. QLMNR_LS = TRUE means: The control valve is at its low endstop.  (For step controllers only) |
| QLMNR_ON | 40.7 | BOOL | FALSE | Output "Position feedback enabled" indicates the set operating mode "Step controller with position feedback" or "Step controller without position feedback". |
| QFUZZY | 41.0 | BOOL | FALSE | If the output parameter is QFUZZY = 1, the controller operates with the fuzzy algorithm. |
| QSPLEPV | 41.1 | BOOL | FALSE | The output "Display of FUZZY controller: Setpoint < process value" is set when the fuzzy controller is switched on, if the setpoint is less than the effective process value. |
| QSPR | 41.2 | BOOL | FALSE | If the output "Split-range operation" is set, the continuous controller is operating in split-range mode. |
| QMAN_FC | 41.4 | BOOL | FALSE | The output "QMAN_FC" is set in the following two cases:  - The slave controller is in manual mode and the master controller is followed up to the process value of the slave controller. - The I-action of the master controller is stopped because the setpoint or manipulated variable of the slave controller is limited or because the slave controller is in manual mode. |
| QPARABUB | 41.7 | BOOL | FALSE | This parameter is set by the FM if the operating parameters are changed via the OP. If READ_VAR = TRUE and if this display is set by the FM, the instruction PID_FM_455 reads out the parameters SP_OP_ON, LMNOP_ON, SP_OP and LMN_OP from the FM and saves them in the instance DB. The instruction thus applies over the operating state of the FM. After the reading process the parameter is set to FALSE. |
| QMOD_F | 42.0 | BOOL | FALSE | The instruction checks that the reading and writing of a data record has been completed. Output "Module error" is set if errors are found. The error cause can be: An incorrect module address at parameter MOD_ADDR, or an incorrect channel number at parameter CHANNEL, or a faulty module. |

---

**See also**

[Description PID_FM_455 (S7-300, S7-400)](#description-pid_fm_455-s7-300-s7-400)
  
[Mode of operation PID_FM_455 (S7-300, S7-400)](#mode-of-operation-pid_fm_455-s7-300-s7-400)
  
[Input parameters PID_FM_455 (S7-300, S7-400)](#input-parameters-pid_fm_455-s7-300-s7-400)
  
[In/out parameters PID_FM_455 (S7-300, S7-400)](#inout-parameters-pid_fm_455-s7-300-s7-400)
  
[Block diagram PID_FM_455 (S7-300, S7-400)](#block-diagram-pid_fm_455-s7-300-s7-400)

### In/out parameters PID_FM_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| <sup>1) </sup>Default values of the module after the first start-up of the PID_FM_455 with COM_RST = TRUE |  |  |  |  |
| COM_RST | 44.0 | BOOL | FALSE | If the parameter COM_RST = TRUE, the instruction PID_FM_455 executes an initialization routine. In doing so the controller parameters (these are all the parameters after cont_par) are read from the FM and stored in the instance DB. In addition, the parameters MOD_ADDR and CHANNEL are checked for validity. After the initialization routine the parameter is set to FALSE. |
| LOAD_OP | 44.1 | BOOL | FALSE | If the in/out parameter "Load operating parameters to FM 455" is set, the operating parameters are loaded into the module and the in/out parameter is reset. |
| READ_VAR | 44.2 | BOOL | FALSE | If the in/out parameter "Read tags from FM 455" is set, the output parameters are read from the module and the in/out parameter is reset. |
| LOAD_PAR | 44.3 | BOOL | FALSE | If the in/out parameter "Load control parameters to FM 455" is set, the control parameters are loaded into the module and the in/out parameter is reset. |
| op_par | 46.0 | WORD | W#16#3130<sup>1)</sup> | The op_par parameter may not be modified by users. It identifies the start of the operating parameters that are transferred to the module, if LOAD_OP = TRUE is set. The end of the operating parameters is identified by cont_par. |
| SP_RE | 48.0 | REAL | 0.0 | An external setpoint is interconnected with the controller at the "External setpoint" input. |
| LMN_RE | 52.0 | REAL | 0.0 | An external manipulated value is interconnected to the controller at the input "External manipulated value".  Values from -100 to 100 % are permitted. |
| SP_OP_ON | 56.0 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the in/out parameter "Enable setpoint operation". If the bit is set, the value SP_OP is applied as setpoint. |
| SAFE_ON | 56.1 | BOOL | FALSE | If the "Adopt safety position" input is set, a safety value is applied as manipulated value.  Note: The actuating signal processing via LMNDN_OP, LMNUP_OP and LMNSOPON on a step controller is of higher priority than the safety manipulated value. |
| LMNOP_ON | 56.2 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the in/out parameter "Enable manipulated value operation". If the bit is set, the value LMN_OP is applied as manipulated value. |
| LMNTRKON | 56.3 | BOOL | FALSE | If input "Follow-up (LMN via AI)" is set, the manipulated value is adjusted to an analog input (AI).  (Does not apply to step controllers without analog position feedback) |
| LMN_REON | 56.4 | BOOL | FALSE | If input "Enable external manipulated value" is set, the external manipulated value LMN_RE is set as the manipulated value. |
| LMNRHSRE | 56.5 | BOOL | FALSE | The signal "Control valve at high endstop" is interconnected at the "High endstop signal of position feedback" input. LMNRHSRE = TRUE means: The control valve is located at the high endstop.  (Only in the case of step controllers) |
| LMNRLSRE | 56.6 | BOOL | FALSE | The signal "Control valve at low endstop" is interconnected at the "Low endstop signal of position feedback" input. LMNRLSRE = TRUE means: The control valve is located at the low endstop.  (Only in the case of step controllers) |
| LMNSOPON | 56.7 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the input "Enable manipulated value operation". If LMNSOPON is set, the signals LMNUP_OP and LMNDN_OP are applied as manipulated value signals.  (Only in the case of step controllers) |
| LMNUP_OP | 57.0 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the input "Manipulated value signal up". If LMNSOPON is set, the value at input "Manipulated value signal up operation" is set as the manipulated value signal.  (Only in the case of step controllers) |
| LMNDN_OP | 57.1 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the input "Manipulated value signal down operation". If LMNSOPON is set, the value at input "Manipulated value signal down operation" is set as the manipulated value signal.  (Only in the case of step controllers) |
| LMNRS_ON | 57.3 | BOOL | FALSE | You can simulate no position feedback if this is not available. The function is enabled by setting the "Enable simulation of position feedback" input The instructions of PID Self-Tuner have access to this parameter as well since at least one simulated manipulated value is required for optimization if a step controller was configured without position feedback. The simulated value is displayed at parameter LMN_A. When the simulation is enabled the value of the parameter LMNRSVAL is set as the starting value.   CAUTION: Offset between the simulation value and real position feedback increases over the time.  (Only for step controllers without analog position feedback) |
| FUZID_ON | 57.4 | BOOL | FALSE | The identification of the fuzzy algorithm is enabled at the "Enable fuzzy identification" input. |
| SP_OP | 58.0 | REAL | 0.0 | The instructions of PID Self-Tuner have access to the in/out parameter "Setpoint operation". If the SP_OP_ON bit is set, the "Setpoint operation" value is applied as the setpoint. |
| LMN_OP<sup>)</sup> | 62.0 | REAL | 0.0 | The instructions of PID Self-Tuner have access to the in/out parameter "Manipulated value operation". If the LMNOP_ON bit is set, the "Manipulated value operation" value is applied as the manipulated value.  Values from -100 to 100 % are permitted. |
| LMNRSVAL | 66.0 | REAL | 0.0 | The instructions of PID Self-Tuner have access to input "Starting value of simulated position feedback". The start value of the simulation is entered at the parameter.  (Only for step controllers without analog position feedback)  Values from -100 to 100 % are permitted. |
| cont_par | 70.0 | WORD | W#16#3130<sup>1)</sup> | The cont_par parameter may not be modified by users. It indicates the start of the controller parameters which are read from the FM and stored in the instance DB, if COM_RST = TRUE is, and which are transferred to the FM when LOAD_PAR = TRUE is set. The end of the controller parameter is the end of the instance DB. |
| P_SEL | 72.0 | BOOL | TRUE <sup>1)</sup> | In the PID algorithm, the PID parts can be switched on and off individually. The proportional action is enabled when the “P-action on” input is set. |
| PFDB_SEL | 72.1 | BOOL | FALSE<sup>1)</sup> | In the PID algorithm, the P- and D-actions can be included in the feedback loop. The proportional action is located in the feedback loop when the input "Enable P-action in feedback loop" is set. |
| MONERSEL | 72.2 | BOOL | FALSE<sup>1)</sup> | The controller has a limit indicator that can be applied either for the process value or the control deviation. If the input "Monitoring: Process value = 0, control deviation = 1" is set, the control deviation will be monitored. |
| SDB_SEL | 72.4 | BOOL | FALSE | SDB_SEL=TRUE: After CPU STOP-RUN, the controller parameters of instruction PID_FM_455 are not overwritten by the SDB parameters in the FMx55. |
| D_EL_SEL | 74.0 | INT | 0<sup>1)</sup> | The D-action element in the PID algorithm can be positioned at a separate input. This is selected via the input “D-action element input for the controller”.  - 0: Control deviation - 1 to 16: Analog input 1 to 16 - 17: Negative process value, D-action in the feedback |
| SP_HLM | 76.0 | REAL | 100.0<sup>1)</sup> | The setpoint is always limited to a high and a low limit. The "Setpoint high limit" input specifies the high limit.  SP_HLM > SP_LLM |
| SP_LLM | 80.0 | REAL | 0.0<sup>1)</sup> | The setpoint is always limited to a high and a low limit. The "Setpoint low limit" input specifies the low limit.  SP_LLM < SP_HLM |
| H_ALM | 84.0 | REAL | 100.0<sup>1)</sup> | You can assign parameters for four limits for monitoring the process value or the control deviation. The "High limit interrupt" input specifies the highest limit.  H_ALM > H_WRN |
| H_WRN | 88.0 | REAL | 90.0<sup>1)</sup> | You can assign parameters for four limits for monitoring the process value or the control deviation. The "High limit warning" input specifies the second highest limit.  Values from H_ALM to L_WRN are permitted. |
| L_WRN | 92.0 | REAL | 10.0<sup>1)</sup> | You can assign parameters for four limits for monitoring the process value or the control deviation. The "Low limit warning" input specifies the second lowest limit.   Values from H_WRN to L_ALM are permitted. |
| L_ALM | 96.0 | REAL | 0.0<sup>1)</sup> | You can assign parameters for four limits for monitoring the process value or the control deviation. The "Low limit alarm" input specifies the lowest limit.  L_ALM < L_WRN |
| HYS | 100.0 | REAL | 1.0<sup>1)</sup> | To prevent flickering of the monitoring displays, a hysteresis can be configured at the "Hysteresis" input.  HYS ≥ 0.0 |
| DEADB_W | 104.0 | REAL | 0.0<sup>1)</sup> | A deadband is applied to the control deviation. The "Deadband width" input determines the size of the deadband.  DEADB_W ≥ 0.0 |
| GAIN | 108.0 | REAL | 1.0<sup>1)</sup> | The "Proportional gain" input specifies controller amplification. |
| TI | 112.0 | REAL | 3000.0<sup>1)</sup> | The "Integration time" input determines the time  response of the integral action. If TI = 0, the integral action is disabled.  TI = 0.0 or TI ≥ 0.5 |
| TD | 116.0 | REAL | 0.0<sup>1)</sup> | The "Derivative-action time" input determines the time response of the differentiator. If TD = 0, the derivative action is disabled.  TD = 0.0 or TD ≥ 1.0 |
| TM_LAG | 120.0 | REAL | 5.0<sup>1)</sup> | The algorithm of the derivative action contains a delay for which parameters can be assigned at the input "Time lag of the derivative action".   TM_LAG ≥ 0.5 |
| LMN_SAFE | 124.0 | REAL | 0.0<sup>1)</sup> | For the manipulated value, a safety value can be configured at the "Safety manipulated value" input.  Values from -100 to 100 % are permitted. |
| LMN_HLM | 128.0 | REAL | 100.0<sup>1)</sup> | The manipulated value is always limited to a high and a low limit. The "Manipulated value high limit" input specifies the high limit.  (Does not apply to step controllers without analog position feedback)  Values from LMN_LLM to 100 % are permitted. |
| LMN_LLM | 132.0 | REAL | 0.0<sup>1)</sup> | The manipulated value is always limited to a high and a low limit. The "Manipulated value low limit" input specifies the low limit.  (Does not apply to step controllers without analog position feedback)  Values from -100 to LMN_HLM are permitted. |
| MTR_TM | 136.0 | REAL | 60.0<sup>1)</sup> | The runtime from endstop to endstop of the control valve is entered at the "Motor actuating time" parameter.   (Only in the case of step controllers) |
| PULSE_TM | 140.0 | REAL | 0.2<sup>1)</sup> | A minimum pulse time can be configured at the "Minimum pulse time" parameter.   (Applies to step controllers or pulse controllers only) |
| BREAK_TM | 144.0 | REAL | 0.2<sup>1)</sup> | A minimum pulse break duration can be assigned with the parameter "Minimum break time."   (Applies to step controllers or pulse controllers only) |

> **Note**
>
> If LOAD_PAR = TRUE is set, all the control parameters are loaded permanently to the EEPROM of FM 455.
>
> If LOAD_OP = TRUE is set, only the setpoint SP_RE of the operating parameters is loaded permanently to the EEPROM of the FM 455. All the other operating parameters are assigned the values 0 or FALSE as default during the startup of FM 455
>
> The EEPROM of the module could become damaged by too frequent write operations. To prevent this, the module delays another write process by 30 minutes after writing of the EEPROM.

---

**See also**

[Description PID_FM_455 (S7-300, S7-400)](#description-pid_fm_455-s7-300-s7-400)
  
[Mode of operation PID_FM_455 (S7-300, S7-400)](#mode-of-operation-pid_fm_455-s7-300-s7-400)
  
[Input parameters PID_FM_455 (S7-300, S7-400)](#input-parameters-pid_fm_455-s7-300-s7-400)
  
[Output parameters PID_FM_455 (S7-300, S7-400)](#output-parameters-pid_fm_455-s7-300-s7-400)
  
[Block diagram PID_FM_455 (S7-300, S7-400)](#block-diagram-pid_fm_455-s7-300-s7-400)

### Block diagram PID_FM_455 (S7-300, S7-400)

#### Overview

The following figures show at which points the parameters of the instruction PID_FM_455 act.

The parameters are effective with three-component controllers, ration/blending controllers, and fixed setpoint or cascade controllers. This also applies for the parameters that exist equally at continuous-action controllers, at controllers with a pulse output as well as at step controllers. Therefore, not all block diagrams are depicted and not all parameter are marked in all figures.

However, the parameters of the instruction PID_FM_455 are contained in all the figures – with the exception of the parameters MOD_ADDR, CHANNEL, QMOD_F, QPARA_F, QCH_F, QLMNR_ON, RET_VALU, COM_RST, LOAD_PAR, READ_VAR, LOAD_OP.

#### Action of the input parameters

Control deviation generation with fixed-value or cascade controller

![Action of the input parameters](images/18118198667_DV_resource.Stream@PNG-en-US.png)

Block diagram of the control algorithm

![Action of the input parameters](images/18118705675_DV_resource.Stream@PNG-en-US.png)

Controller output of the continuous-action controller

![Action of the input parameters](images/18118868363_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (pulse controller operating mode)

![Action of the input parameters](images/18118901771_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (step controller operating mode with position feedback)

![Action of the input parameters](images/18118922379_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (step controller operating mode without position feedback)

![Action of the input parameters](images/18118726283_DV_resource.Stream@PNG-en-US.png)

#### Generating output parameters

The following figures show at which points in the module the output parameters of the instruction PID_FM_455are generated.

Control deviation generation with fixed-value or cascade controller

![Generating output parameters](images/24541655947_DV_resource.Stream@PNG-en-US.png)

Block diagram of the control algorithm

![Generating output parameters](images/18118767499_DV_resource.Stream@PNG-en-US.png)

Controller output of the continuous-action controller

![Generating output parameters](images/18118788107_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (pulse controller operating mode)

![Generating output parameters](images/24541485579_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (step controller operating mode with position feedback)

![Generating output parameters](images/24541583115_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (step controller operating mode without position feedback)

![Generating output parameters](images/18118847755_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Description PID_FM_455 (S7-300, S7-400)](#description-pid_fm_455-s7-300-s7-400)
  
[Mode of operation PID_FM_455 (S7-300, S7-400)](#mode-of-operation-pid_fm_455-s7-300-s7-400)
  
[Input parameters PID_FM_455 (S7-300, S7-400)](#input-parameters-pid_fm_455-s7-300-s7-400)
  
[Output parameters PID_FM_455 (S7-300, S7-400)](#output-parameters-pid_fm_455-s7-300-s7-400)
  
[In/out parameters PID_FM_455 (S7-300, S7-400)](#inout-parameters-pid_fm_455-s7-300-s7-400)

## FUZ_455 (S7-300, S7-400)

This section contains information on the following topics:

- [Description FUZ_455 (S7-300, S7-400)](#description-fuz_455-s7-300-s7-400)
- [Input parameters FUZ_455 (S7-300, S7-400)](#input-parameters-fuz_455-s7-300-s7-400)
- [Output parameters FUZ_455 (S7-300, S7-400)](#output-parameters-fuz_455-s7-300-s7-400)
- [In/out parameters FUZ_455 (S7-300, S7-400)](#inout-parameters-fuz_455-s7-300-s7-400)

### Description FUZ_455 (S7-300, S7-400)

The instruction FUZ_455 is used to read out and write the controller parameters of the fuzzy temperature controller from FM 455.

This function is suitable for the following applications:

- Transferring the controller parameters of the FM 455 that have been established by identification after the module replacement
- Adapting the FM 455 to different processes

  > **Note**
  >
  > It is not permitted to modify the parameters that have been established by the FM 455 by means of an identification as they have been optimized for the process.

#### Mode of operation

The parameters READ_PAR and LOAD_PAR are used to control the mode of operation of the instruction FUZ_455

If READ_PAR = TRUE, FUZ_455 reads the parameters of all the temperature controllers of the FM 455 and stores them in the instance DB. After the temperature controller parameters have been successfully read out, FUZ_455 sets the parameter READ_PAR to FALSE.

If LOAD_PAR = TRUE, FUZ_455 writes the parameters of all the temperature controllers of the FM 455 from the instance DB to the FM 455. After the parameters have been successfully transferred, FUZ_455 sets the parameter LOAD_PAR to FALSE.

#### Call

FUZ_455 requires no initialization routine.

FUZ_455 has to be called in the same OB as all the other instructions that access the same FM 455.

#### Start-up

During the start-up of the CPU you should set the LOAD_PAR parameter of the FUZ_455 instruction and then call the block in the cyclic program, provided LOAD_PAR = TRUE.

---

**See also**

[Input parameters FUZ_455 (S7-300, S7-400)](#input-parameters-fuz_455-s7-300-s7-400)
  
[Output parameters FUZ_455 (S7-300, S7-400)](#output-parameters-fuz_455-s7-300-s7-400)

### Input parameters FUZ_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 512 | The module address that results from the configuration with STEP 7 is set at this input. |

---

**See also**

[Description FUZ_455 (S7-300, S7-400)](#description-fuz_455-s7-300-s7-400)
  
[Output parameters FUZ_455 (S7-300, S7-400)](#output-parameters-fuz_455-s7-300-s7-400)

### Output parameters FUZ_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 2.0 | WORD | 0 | RET_VALU contains the return value RET_VAL of the WR_REC and RD_REC instructions. RET_VALU can be evaluated when QMOD_F reports an error. |
| PARAFFUZ | 4.0 | WORD | 0 | A parameter assignment error created by the the instruction FUZ_455 is displayed at the parameter PARAFFUZ as follows:   High byte of PARAFFUZ = 01: There is a parameter assignment error..   High byte of PARAFFUZ = 00: There is no parameter assignment error.   The low byte contains the offset of the parameter that caused the parameter assignment error, calculated from the static variable FUZ_PAR[1].  For instance, PARAFFUZ = W#16#0104 means that the second parameter is faulty. |

---

**See also**

[Description FUZ_455 (S7-300, S7-400)](#description-fuz_455-s7-300-s7-400)
  
[Input parameters FUZ_455 (S7-300, S7-400)](#input-parameters-fuz_455-s7-300-s7-400)

### In/out parameters FUZ_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| READ_PAR | 6.0 | BOOL | FALSE | If the READ_PAR parameter is set, the fuzzy parameters are read out from the module and stored in the static variables of the instance DB. |
| LOAD_PAR | 6.1 | BOOL | FALSE | If the LOAD_PAR parameter is set, the fuzzy parameters are read out from the static variables of the instance DB module and transferred to the module. |

## FORCE455 (S7-300, S7-400)

This section contains information on the following topics:

- [Description FORCE455 (S7-300, S7-400)](#description-force455-s7-300-s7-400)
- [Input parameters FORCE455 (S7-300, S7-400)](#input-parameters-force455-s7-300-s7-400)
- [Output parameters FORCE455 (S7-300, S7-400)](#output-parameters-force455-s7-300-s7-400)

### Description FORCE455 (S7-300, S7-400)

The instruction FORCE455 is used to simulate (force) the analog and digital input values to support the start-up.

#### Simulating Digital Values

The simulation of the values for the digital inputs 1 to 16 is enabled via the switches S_DION[ i ], where 1 ≤ i ≤ 16. You specify the simulation values at the parameters DI_SIM[ i ]. If S_DION[i] = TRUE, the value DI_SIM[i] is used Instead of the value of digital input i of the module,. The LEDs I1 to I16 always show the status of the associated digital input, even in the case of a simulation.

#### Simulating Analog Values

The simulation of the analog value for the channels 1 to 16 is enabled via the switches S_AION[ i ] or S_PVON[ i ], where 1 ≤ i ≤ 16.

You specify the simulation values for the channels 1 to 16 via the parameter PV_SIM[ i ].

You can have the simulation values become effective at two points:

- S_AION[ i ] = TRUE (1 ≤ i ≤ 16)

  The value PV_SIM[ i ] is used instead of the value of analog input i of the module.
- S_PVON[ i ] = TRUE (1 ≤ i ≤ 16)

  The value PV_SIM[ i ] is used instead of the conditioned value of analog input i of the module.

The following figure shows at which point the simulated analog value is effective.

![Simulating Analog Values](images/18135808267_DV_resource.Stream@PNG-en-US.png)

Enabling and specification of the simulation values (forcing) is not carried out via the parameter assignment interface. This is why the relevant switches and connecting lines are drawn as dotted lines.

#### Call

FORCE455 does not require any initialization routine and is normally called cyclically.

FORCE455 has to be called in the same OB as all the other instructions that access the same FM 455.

#### Startup characteristics

When FM 455 restarts after power off, the simulation switches on the FM 455 are again set to FALSE.

---

**See also**

[Input parameters FORCE455 (S7-300, S7-400)](#input-parameters-force455-s7-300-s7-400)
  
[Output parameters FORCE455 (S7-300, S7-400)](#output-parameters-force455-s7-300-s7-400)

### Input parameters FORCE455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| S_AION | 0.0 | ARRAY [1..16] of BOOL | FALSE | If, for example, the S_AION[1] switch is set to TRUE, the value PV_SIM[1] is used instead of the analog input value 1 of the module. |
| S_PVON | 2.0 | ARRAY [1..16] of BOOL | FALSE | If, for example, the S_PVON[1] switch is set to TRUE, the value PV_SIM[1] is used instead of the conditioned analog input value 1 of the module. |
| PV_SIM | 4.0 | ARRAY [1..16] of REAL | 0.0 | The simulation value for the analog input 1 is specified, for example, at input PV_SIM[1]. If S_PVON = TRUE, then the conditioned analog input value is specified here. If S_PVON = FALSE and S_AION = TRUE, then the analog input value, which is transformed into a conditioned value by means of the conditioning functions, is specified in mA or mV.  Permitted are 0.0 to 20.0 [mA], -1500 to +10000 [mV], or a technical range of values. |
| S_DION | 68.0 | ARRAY [1..16] of BOOL | FALSE | If, for example, the S_DION[1] switch is set to TRUE, the value DI_SIM[1] is used instead of the digital input value 1 of the module. |
| DI_SIM | 70.0 | ARRAY [1..16] of BOOL | FALSE | Simulation value for digital input |
| MOD_ADDR | 72.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |

---

**See also**

[Description FORCE455 (S7-300, S7-400)](#description-force455-s7-300-s7-400)
  
[Output parameters FORCE455 (S7-300, S7-400)](#output-parameters-force455-s7-300-s7-400)

### Output parameters FORCE455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 74.0 | WORD | 0 | RET_VALU contains the return value RET_VAL of the WR_REC and RD_REC instructions. RET_VALU can be evaluated when QMOD_F reports an error. |

## READ_455 (S7-300, S7-400)

This section contains information on the following topics:

- [Description Ready_455 (S7-300, S7-400)](#description-ready_455-s7-300-s7-400)
- [Input parameters READ_455 (S7-300, S7-400)](#input-parameters-read_455-s7-300-s7-400)
- [Output parameters READ_455 (S7-300, S7-400)](#output-parameters-read_455-s7-300-s7-400)

### Description Ready_455 (S7-300, S7-400)

The instruction READ_455 is used to read out the digital and analog input values to support the start-up.

The following values are displayed:

![Figure](images/18137300107_DV_resource.Stream@PNG-en-US.png)

#### Call

READ_455 does not require any initialization routine and is normally called cyclically.

READ_455 has to be called in the same OB as all the other instructions that access the same FM 455.

---

**See also**

[Input parameters READ_455 (S7-300, S7-400)](#input-parameters-read_455-s7-300-s7-400)
  
[Output parameters READ_455 (S7-300, S7-400)](#output-parameters-read_455-s7-300-s7-400)

### Input parameters READ_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default setting | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 512 | The module address that results from the configuration with STEP 7 is set at this input. |

---

**See also**

[Description Ready_455 (S7-300, S7-400)](#description-ready_455-s7-300-s7-400)
  
[Output parameters READ_455 (S7-300, S7-400)](#output-parameters-read_455-s7-300-s7-400)

### Output parameters READ_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| CJ_TEMP | 2.0 | REAL | 0.0 | At the CJ_TEMP output, the measured reference junction temperature is displayed by the module if a thermocouple element input is configured and the reference junction temperature is not configured. |
| STAT_DI | 6.0 | ARRAY [1..16] of BOOL | FALSE | The states of digital inputs 1 to 16 are displayed at the STAT_DI parameters. |
| DIAG[x].PV_PER | (channel number) x 8 | ARRAY [1..16] of STRUCT | 0.0 | The analog input value of the module is displayed, for example, in the units mA or mV, at the DIAG[1].PV_PER parameter. |
| DIAG[x].PV_PHY | (channel number) x 8 + 4 | ARRAY [1..16] of STRUCT | 0.0 | The DIAG[1].PV_PHY parameter, for example, displays the conditioned analog input value of the module in the physical unit. |
| RET_VALU | 136.0 | WORD | 0 | RET_VALU contains the return value RET_VAL of the WR_REC and RD_REC instructions. RET_VALU can be evaluated when QMOD_F reports an error. |

---

**See also**

[Description Ready_455 (S7-300, S7-400)](#description-ready_455-s7-300-s7-400)
  
[Input parameters READ_455 (S7-300, S7-400)](#input-parameters-read_455-s7-300-s7-400)

## CH_DIAG_455 (S7-300, S7-400)

This section contains information on the following topics:

- [Description CH_DIAG_455 (S7-300, S7-400)](#description-ch_diag_455-s7-300-s7-400)
- [Input parameters CH_DIAG_455 (S7-300, S7-400)](#input-parameters-ch_diag_455-s7-300-s7-400)
- [Output parameters CH_DIAG_455 (S7-300, S7-400)](#output-parameters-ch_diag_455-s7-300-s7-400)
- [Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)
- [Block diagrams CH_DIAG_455 (S7-300, S7-400)](#block-diagrams-ch_diag_455-s7-300-s7-400)

### Description CH_DIAG_455 (S7-300, S7-400)

The instruction CH_DIAG_455 is used to read out additional channel-specific diagnostic variables from the module.

#### Call

CH_DIAG_455 does not require any initialization routine and is normally called cyclically.

CH_DIAG_455 has to be called in the same OB as all the other instructions that access the same FM 455.

---

**See also**

[Input parameters CH_DIAG_455 (S7-300, S7-400)](#input-parameters-ch_diag_455-s7-300-s7-400)
  
[Output parameters CH_DIAG_455 (S7-300, S7-400)](#output-parameters-ch_diag_455-s7-300-s7-400)
  
[Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)
  
[Block diagrams CH_DIAG_455 (S7-300, S7-400)](#block-diagrams-ch_diag_455-s7-300-s7-400)

### Input parameters CH_DIAG_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CHANNEL | 2.0 | INT | 1 | The number of the controller channel to which the instance DB is referenced is configured at the "Channel number" input.   Values of 1 to 16 are permitted. |

---

**See also**

[Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)
  
[Description CH_DIAG_455 (S7-300, S7-400)](#description-ch_diag_455-s7-300-s7-400)
  
[Output parameters CH_DIAG_455 (S7-300, S7-400)](#output-parameters-ch_diag_455-s7-300-s7-400)
  
[Block diagrams CH_DIAG_455 (S7-300, S7-400)](#block-diagrams-ch_diag_455-s7-300-s7-400)

### Output parameters CH_DIAG_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SP_R | 4.0 | REAL | 0.0 | If a ratio controller is set, the input value of the setpoint value is assigned to the parameter. |
| PV_R | 8.0 | REAL | 0.0 | The following value is only assigned to the parameter value if the ratio controller is set: (Process value A - Setpoint value offset) / Process value D |
| DIF_I | 12.0 | REAL | 0.0 | The input variable of the D-action is displayed at the DIF_I parameter. This is particularly of interest if, for example, an analog input is configured as the input variable of the D-action component. |
| TRACKPER | 16.0 | REAL | 0.0 | The TRACKPER parameter shows the input variable to which the manipulated value is tracked if the track-manipulated-variable function is enabled on the controller. |
| IDSTATUS | 20.0 | WORD | 0.0 | The state of the identification is displayed at [Parameter IDSTATUS](#parameter-idstatus-s7-300-s7-400) |
| LMN_P | 22.0 | REAL | 0.0 | The P-action of the manipulated variable is displayed at the LMN_P parameter. |
| LMN_I | 26.0 | REAL | 0.0 | The I-action of the manipulated variable is displayed at the LMN_I parameter. |
| LMN_D | 30.0 | REAL | 0.0 | The D-action of the manipulated variable is displayed at the LMN_D parameter. |
| RET_VALU | 34.0 | WORD | 0 | RET_VALU contains the return value RET_VAL of the WR_REC and RD_REC instructions. RET_VALU can be evaluated when QMOD_F reports an error. |

---

**See also**

[Description CH_DIAG_455 (S7-300, S7-400)](#description-ch_diag_455-s7-300-s7-400)
  
[Input parameters CH_DIAG_455 (S7-300, S7-400)](#input-parameters-ch_diag_455-s7-300-s7-400)
  
[Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)
  
[Block diagrams CH_DIAG_455 (S7-300, S7-400)](#block-diagrams-ch_diag_455-s7-300-s7-400)

### Parameter IDSTATUS (S7-300, S7-400)

The IDSTATUS parameter supplies information on the status of identification and contains the four hexadecimal values X, A, I and F.

![Figure](images/26402794251_DV_resource.Stream@PNG-de-DE.png)

| Value | Description |
| --- | --- |
| X | Without meaning (always 0) |
| A | Action number  - 0 = Manual mode (or no closed-loop control mode); - 2 = Closed-loop control; - 4 = Tuning enabled (FUZID_ON = true); - 6 = Transition state from manual mode to 2 or 4; |
| I | Display "Identification running" and "Parameters determined, but not yet stored in EEPROM"  - 0 = Identification not running, no new parameters determined - 1 = Identification running, no new parameters determined - 2 = Identification not running, new parameters determined, but not yet stored in EEPROM - 3 = Identification running, new parameters determined, but not yet stored in EEPROM |
| F | Error number  - 0 = No error - 4 = Excessive step-change of the process value during the identification - 5 = Ratio of time lag to system time constant too large or strongly non-linear behavior of the controlled system. - 6 = Temperature drop or rise during identification start too large. System not settled sufficiently |

---

**See also**

[Description CH_DIAG_455 (S7-300, S7-400)](#description-ch_diag_455-s7-300-s7-400)
  
[Input parameters CH_DIAG_455 (S7-300, S7-400)](#input-parameters-ch_diag_455-s7-300-s7-400)
  
[Output parameters CH_DIAG_455 (S7-300, S7-400)](#output-parameters-ch_diag_455-s7-300-s7-400)
  
[Block diagrams CH_DIAG_455 (S7-300, S7-400)](#block-diagrams-ch_diag_455-s7-300-s7-400)

### Block diagrams CH_DIAG_455 (S7-300, S7-400)

#### Block diagrams CH_DIAG_455

The following diagnostic values of the control deviation are displayed.

![Block diagrams CH_DIAG_455](images/18153828875_DV_resource.Stream@PNG-en-US.png)

The following values of the control algorithm are displayed.

![Block diagrams CH_DIAG_455](images/18153849483_DV_resource.Stream@PNG-en-US.png)

The following values of the continuous-action controller or step controller are displayed.

![Block diagrams CH_DIAG_455](images/18153870091_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Description CH_DIAG_455 (S7-300, S7-400)](#description-ch_diag_455-s7-300-s7-400)
  
[Input parameters CH_DIAG_455 (S7-300, S7-400)](#input-parameters-ch_diag_455-s7-300-s7-400)
  
[Output parameters CH_DIAG_455 (S7-300, S7-400)](#output-parameters-ch_diag_455-s7-300-s7-400)
  
[Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)

## PID_PAR_455 (S7-300, S7-400)

This section contains information on the following topics:

- [Description PID_PAR_455 (S7-300, S7-400)](#description-pid_par_455-s7-300-s7-400)
- [Input parameters PID_PAR_455 (S7-300, S7-400)](#input-parameters-pid_par_455-s7-300-s7-400)
- [Output parameters PID_PAR_455 (S7-300, S7-400)](#output-parameters-pid_par_455-s7-300-s7-400)
- [Alterable parameters (S7-300, S7-400)](#alterable-parameters-s7-300-s7-400)

### Description PID_PAR_455 (S7-300, S7-400)

The instruction PID_PAR_455 is used for the online modification of parameters that cannot be defined via the instruction PID_FM_455. To view the parameters that can be modified, refer to the table Alterable parameters

#### Call

PID_PAR_455 requires an initialization routine, which is initiated by setting the parameter COM_RST = TRUE. To save run time, PID_PAR_455 should not be called cyclically. It should only be called when parameters are to be changed. COM_RST must then be FALSE.

PID_PAR_455 has to be called in the same OB as all the other instructions that access the same FM 455.

#### Mode of operation

In the initialization routine, PID_PAR_455 reads the parameters from the system data and stores them in static variables. Per call, PID_PAR_455 modifies one of these REAL variables and one of these INT variables. At the input parameter INDEX_R or INDEX_I, specify the index numbers of the parameter that you want to modify. At the input parameter VALUE_R or VALUE_I, enter the new values. PID_PAR_455 transfers the entire data record to FM 455 with the modified variables.

To modify additional parameters you have to call **the same** instance DB several times consecutively with COM_RST = FALSE and with different index numbers.

The COM_RST parameter is an input parameter that is not reset by PID_PAR_455.

> **Note**
>
> Please note that parameters that you have changed using PID_PAR_455 are overwritten by the parameters from the system data during the start-up.

#### Start-up

During CPU start-up and during CPU STOP-RUN transition, the parameters on the FM 455 are overwritten with the parameters from the SDB of the CPU.

#### Example

During operation you want to modify the ramp-up time for the reference variable and, depending on the process state, use different analog input values as process value.

- Call PID_PAR_455 using COM_RST = TRUE during the start-up of the CPU.
- To configure the ramp-up time for the reference variable at 10.0, use INDEX_R = 30, VALUE_R = 10.0 and INDEX_I = 0 to call PID_PAR_455 during operation.
- If you want to parameterize the analog input value 4 of the module as the process value, call PID_PAR_455 with INDEX_R = 0, INDEX_I = 50 and VALUE_I = 4 during operation.

---

**See also**

[Input parameters PID_PAR_455 (S7-300, S7-400)](#input-parameters-pid_par_455-s7-300-s7-400)
  
[Output parameters PID_PAR_455 (S7-300, S7-400)](#output-parameters-pid_par_455-s7-300-s7-400)
  
[Alterable parameters (S7-300, S7-400)](#alterable-parameters-s7-300-s7-400)

### Input parameters PID_PAR_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| COM_RST | 0.0 | BOOL | TRUE | If the parameter COM_RST = TRUE, the instruction PID_PAR_455 executes an initialization routine. During this initialization process the parameters are read from the system data of the CPU and saved in the instance DB. |
| MOD_ADDR | 2.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CHANNEL | 4.0 | INT | 1 | The number of the controller channel to which the instance DB is referenced is configured at the "Channel number" input.  Values of 1 to 16 are permitted. |
| INDEX_R | 6.0 | INT | 0.0 | - 0: No REAL parameters are changed - 1 to 48: Each value corresponds to an [alterable REAL parameter](#alterable-parameters-s7-300-s7-400). |
| VALUE_R | 8.0 | REAL | 0.0 | Depends on the relevant parameter |
| INDEX_I | 12.0 | INT | 0.0 | - 0: No INT parameters are changed. - 49 to 61:: Each value corresponds to an [alterable INT parameter](#alterable-parameters-s7-300-s7-400). |
| VALUE_I | 14.0 | INT | 0.0 | Depends on the relevant parameter |

---

**See also**

[Description PID_PAR_455 (S7-300, S7-400)](#description-pid_par_455-s7-300-s7-400)
  
[Output parameters PID_PAR_455 (S7-300, S7-400)](#output-parameters-pid_par_455-s7-300-s7-400)
  
[Alterable parameters (S7-300, S7-400)](#alterable-parameters-s7-300-s7-400)

### Output parameters PID_PAR_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 16.0 | WORD | 0 | RET_VALU contains the return value RET_VAL of the WR_REC and RD_REC instructions. RET_VALU can be evaluated when QMOD_F reports an error. |
| BUSY | 18.0 | BOOL | FALSE | If BUSY = TRUE, the parameters have not yet been applied by the module. The instruction PID_PAR_455 should then be called again in the next cycle. |

---

**See also**

[Description PID_PAR_455 (S7-300, S7-400)](#description-pid_par_455-s7-300-s7-400)
  
[Input parameters PID_PAR_455 (S7-300, S7-400)](#input-parameters-pid_par_455-s7-300-s7-400)
  
[Alterable parameters (S7-300, S7-400)](#alterable-parameters-s7-300-s7-400)

### Alterable parameters (S7-300, S7-400)

List of the REAL and INT parameters on a FM 455 that are to be modified with PID_PAR_455

| Data type | Description |  | Index number |
| --- | --- | --- | --- |
| - | No parameter selected |  | 0 |
| REAL | Filter time constants for analog input |  | 1 |
| REAL | End of scale (100%) |  | 2 |
| REAL | Start of scale (0%) |  | 3 |
| REAL | Polyline, interpolation point 1 input side |  | 4 |
| REAL | Polyline, interpolation point 2 input side |  | 5 |
| REAL | Polyline, interpolation point 3 input side |  | 6 |
| REAL | Polyline, interpolation point 4 input side |  | 7 |
| REAL | Polyline, interpolation point 5 input side |  | 8 |
| REAL | Polyline, interpolation point 6 input side |  | 9 |
| REAL | Polyline, interpolation point 7 input side |  | 10 |
| REAL | Polyline, interpolation point 8 input side |  | 11 |
| REAL | Polyline, interpolation point 9 input side |  | 12 |
| REAL | Polyline, interpolation point 10 input side |  | 13 |
| REAL | Polyline, interpolation point 11 input side |  | 14 |
| REAL | Polyline, interpolation point 12 input side |  | 15 |
| REAL | Polyline, interpolation point 13 input side |  | 16 |
| REAL | Polyline, interpolation point 1 output side |  | 17 |
| REAL | Polyline, interpolation point 2 output side |  | 18 |
| REAL | Polyline, interpolation point 3 output side |  | 19 |
| REAL | Polyline, interpolation point 4 output side |  | 20 |
| REAL | Polyline, interpolation point 5 output side |  | 21 |
| REAL | Polyline, interpolation point 6 output side |  | 22 |
| REAL | Polyline, interpolation point 7 output side |  | 23 |
| REAL | Polyline, interpolation point 8 output side |  | 24 |
| REAL | Polyline, interpolation point 9 output side |  | 25 |
| REAL | Polyline, interpolation point 10 output side |  | 26 |
| REAL | Polyline, interpolation point 11 output side |  | 27 |
| REAL | Polyline, interpolation point 12 output side |  | 28 |
| REAL | Polyline, interpolation point 13 output side |  | 29 |
| REAL | Ramp-up time for control variable |  | 30 |
| REAL | Safety reference variable or safety reference variable ratio |  | 31 |
| REAL | Offset for the setpoint logic operation (ratio / mixed controllers) |  | 32 |
| REAL | Factor for process value B (three-component controllers) |  | 33 |
| REAL | Factor for process value C (three-component controllers) |  | 34 |
| REAL | Offset for process value logic operation (three-component controllers) |  | 35 |
| REAL | Factor for disturbance variable logical operation |  | 36 |
| REAL | Operating point |  | 37 |
| REAL | Aggressiveness at fuzzy controller |  | 38 |
| REAL | Vertices for split-range function: Start of input signal A area |  | 39 |
| REAL | Vertices for split-range function: End of input signal A area |  | 40 |
| REAL | Vertices for split-range function: Start of output signal A area |  | 41 |
| REAL | Vertices for split-range function: End of output signal A area |  | 42 |
| REAL | Vertices for split-range function: Start of input signal B area |  | 43 |
| REAL | Vertices for split-range function: End of input signal B area |  | 44 |
| REAL | Vertices for split-range function: Start of output signal B area |  | 45 |
| REAL | Vertices for split-range function: End of output signal B area |  | 46 |
| REAL | Minimum pulse time |  | 47 |
| REAL | Minimum break time |  | 48 |
| INT | Selection of the reference variable SP or SP_RE for the controller |  | 49 |
| 0 | Setpoint SP_RE of the instruction |  |  |
| 1 to 16 | Analog input value 1 to 16 |  |  |
| 17 to 32 | Manipulated variable (LMN) of controllers 1 to 16 |  |  |
| INT | Selecting the main controlled variable process value A for the controllers |  | 50 |
| 0: | Process value A = 0.0 |  |  |
| 1 to 16: | Analog input value 1 to 16 |  |  |
| INT | Selecting the main controlled variable process value B for the controllers |  | 51 |
| 0 | Process value B = 0.0 |  |  |
| 1 to 16 | Analog input value 1 to 16 |  |  |
| INT | Selecting the auxiliary controlled variable process value C for the controllers |  | 52 |
| 0 | Process value C = 0.0 |  |  |
| 1 to 16 | Analog input value 1 to 16 |  |  |
| INT | Selecting the auxiliary controlled variable process value D for the controllers |  | 53 |
| 0 | Process value D = 0.0 |  |  |
| 1 to 16 | Analog input value 1 to 16 |  |  |
| 17 to 32 | Manipulated variable (LMN) of controllers 1 to 16 |  |  |
| INT | Selection of the disturbance variable DISV for the controller |  | 54 |
| 0 | Disturbance variable = 0.0 |  |  |
| 1 to 16 | Analog input value 1 to 16 |  |  |
| INT | Selection of position follow-up TRACK_PER for the controller |  | 55 |
| 0 | Position follow-up = 0.0 |  |  |
| 1 to 16 | Analog input value 1 to 16 |  |  |
| INT | Selection of position follow-up LMNR_PER for the controller |  | 56 |
| 0 | Position follow-up = 0.0 |  |  |
| 1 to 16 | Analog input value 1 to 16 |  |  |
| INT | Selecting the signal for changeover to safety value for the manipulated value of the controller |  | 57 |
| 0 | Can only be assigned via SAFE_ON of the instruction PID_FM_455 |  |  |
| 1 to 16 | Assignment via SAFE_ON parameter of the instruction PID_FM_455 ORed with digital input 1 to 16 |  |  |
| INT | Selecting the signal for changeover to the follow-up function of the manipulated value of the controller |  | 58 |
| 0 | Can only be assigned via LMNTRKON of the instruction PID_FM_455 |  |  |
| 1 to 16 | Assignment via LMNTRKON parameter of the instruction PID_FM_455 ORed with digital input 1 to 16 |  |  |
| INT | Selecting the signal for changing over the manipulated value of the controller to LMN_RE |  | 59 |
| 0 | Can only be assigned via LMN_REON of the instruction PID_FM_455 |  |  |
| 1 to 16 | Assignment via LMN_REON parameter of the instruction PID_FM_455 ORed with digital input 1 to 16 |  |  |
| INT | Selecting the high limit signal of the position feedback |  | 60 |
| 0 | Can only be assigned via LMNRHSRE of the instruction PID_FM_455 |  |  |
| 1 to 16 | Assignment via LMNRHSRE parameter of the instruction PID_FM_455 ORed with digital input 1 to 16 |  |  |
| INT | Selecting the low limit signal of the position feedback |  | 61 |
| 0 | Can only be assigned via LMNRLSRE of the instruction PID_FM_455 |  |  |
| 1 to 16 | Assignment via LMNRLSRE parameter of the instruction PID_FM_455 ORed with digital input 1 to 16 |  |  |

---

**See also**

[Description PID_PAR_455 (S7-300, S7-400)](#description-pid_par_455-s7-300-s7-400)
  
[Input parameters PID_PAR_455 (S7-300, S7-400)](#input-parameters-pid_par_455-s7-300-s7-400)
  
[Output parameters PID_PAR_455 (S7-300, S7-400)](#output-parameters-pid_par_455-s7-300-s7-400)

## CJ_T_PAR_455 (S7-300, S7-400)

This section contains information on the following topics:

- [Description CJ_T_PAR_455 (S7-300, S7-400)](#description-cj_t_par_455-s7-300-s7-400)
- [Input parameters CJ_T_PAR_455 (S7-300, S7-400)](#input-parameters-cj_t_par_455-s7-300-s7-400)
- [Output parameters CJ_T_PAR_455 (S7-300, S7-400)](#output-parameters-cj_t_par_455-s7-300-s7-400)

### Description CJ_T_PAR_455 (S7-300, S7-400)

The instruction CJ_T_PAR_455 is used for online modification of the configured reference junction temperature. This is necessary if a temperature control system with several FM 455 with thermoelement inputs is to be operated without having to connect a Pt 100 to each FM 455.

#### Call

CJ_T_PAR_455 requires an initialization routine. To this purpose it has to be called once with the COM_RST = TRUE parameter at the start-up of the CPU.

CJ_T_PAR_455 is normally called cyclically. For this purpose COM_RST should be set to FALSE for runtime reasons. The COM_RST parameter is an input parameter that is not reset.

CJ_T_PAR_455 has to be called in the same OB as all the other instructions that access the same FM 455.

#### Example

If an FM 455 measures the reference junction temperature of an extruder control system with more than 16 heating zones, this can be read out by READ_455 at parameter CJ_TEMP and can be parameterized for the other FM 455 via CJ_T_PAR_455.

---

**See also**

[Input parameters CJ_T_PAR_455 (S7-300, S7-400)](#input-parameters-cj_t_par_455-s7-300-s7-400)
  
[Output parameters CJ_T_PAR_455 (S7-300, S7-400)](#output-parameters-cj_t_par_455-s7-300-s7-400)

### Input parameters CJ_T_PAR_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| COM_RST | 0.0 | BOOL | – | If the parameter COM_RST = TRUE, the instruction CJ_T_PAR_455 executes an initialization routine. During this initialization process the parameters are read from the system data of the CPU and saved in the instance DB. |
| MOD_ADDR | 2.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CJ_T | 4.0 | REAL | 0.0 | The reference junction temperature can be specified at parameter CJ_T.   The permissible value range depends on the sensor type. |

---

**See also**

[Description CJ_T_PAR_455 (S7-300, S7-400)](#description-cj_t_par_455-s7-300-s7-400)
  
[Output parameters CJ_T_PAR_455 (S7-300, S7-400)](#output-parameters-cj_t_par_455-s7-300-s7-400)

### Output parameters CJ_T_PAR_455 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 8.0 | WORD | 0 | RET_VALU contains the return value RET_VAL of the WR_REC and RD_REC instructions. RET_VALU can be evaluated when QMOD_F reports an error. |
| BUSY | 10.0 | BOOL | FALSE | If BUSY = TRUE, the parameters have not yet been applied by the module. The instruction CJ_T_PAR_455 should then be called again in the next cycle. |

---

**See also**

[Description CJ_T_PAR_455 (S7-300, S7-400)](#description-cj_t_par_455-s7-300-s7-400)
  
[Input parameters CJ_T_PAR_455 (S7-300, S7-400)](#input-parameters-cj_t_par_455-s7-300-s7-400)

## LP_ZONE (S7-300, S7-400)

This section contains information on the following topics:

- [Description LP_ZONE (S7-300, S7-400)](#description-lp_zone-s7-300-s7-400)
- [Input parameters LP_ZONE (S7-300, S7-400)](#input-parameters-lp_zone-s7-300-s7-400)
- [Output parameters LP_ZONE (S7-300, S7-400)](#output-parameters-lp_zone-s7-300-s7-400)
- [In/out parameters LP_ZONE (S7-300, S7-400)](#inout-parameters-lp_zone-s7-300-s7-400)
- [Static variables LP_ZONE (S7-300, S7-400)](#static-variables-lp_zone-s7-300-s7-400)

### Description LP_ZONE (S7-300, S7-400)

To optimize load on CPU resources and processing of the instruction ZONE at constant bus cycle times at during controller optimization, it is necessary to use the loop scheduler LP_ZONE.

LP_ZONE ensures that only one zone is processed per call of the cyclic interrupt OB.

The instruction LP_ZONE calculates the zone sampling times and transfers them to the instances of instruction ZONE.

#### Call

LP_ZONE is called in a start-up or cyclic interrupt OB. The instructions LP_ZONE, ADM_ZONE and ZONE must all be called at the same cyclic interrupt level, preferably directly in the cyclic interrupt OB. It is not permitted to program separate time reduction ratios for the blocks.

LP_ZONE requires an initialization routine after the insertion or removal of a zone or during the the modification of a call sequence. This initialization routine must be called with the parameter COM_RST = TRUE. The COM_RST bit is passed to the individual zones and their administration block via the LP_SCH interface.

The zone numbers NBR_CALL of the instances of the instructions ZONE and ADM_ZONE and the maximum zone number MNR_CALL of the instruction LP_ZONE are automatically set according to the following routine:

Initial execution of the cyclic interrupt OB after COM_RST of the instruction LP_ZONE has been set:

- LP_ZONE sets the call counter LP_SCH. CALL_CNT to 1.
- ZONE and ADM_ZONE read the call counter and write the value to their in/out parameterNBR_CALL. ZONE increments the call counter by the count by 1. ADM_ZONE leaves it unchanged.

Second run of the cyclic interrupt OB after COM_RST of the instruction LP_ZONE has been set:

- LP_ZONE reads the call counter (total number of zones) and writes the value to MNR_CALL.

#### Mode of operation

Parameter LP_SCH.CALL_CNT is incremented by the count of 1 at every call of the instruction LP_ZONE. The counter is reset to 1 after it has reached the maximum zone number of MNR_CALL. When the ZONE instruction is called, it first check the counter LP_SCH.CALL_CNT. If the counter value and internal zone number NBR_CALL match, the instruction executes its program. The parameter MNR_CALL of the instruction LP_ZONE and NBR_CALL of the instruction ADM_ZONE and ZONE are automatically set by the blocks after a restart.

> **Note**
>
> Interconnect the in/out parameter LP_SCH of the instructions ZONE and ADM_ZONE to the internal structure LP_SCH of the instance DB of the instruction LP_ZONE.
>
> Interconnect input parameter OB_EXC_FREQ of the instruction LP_ZONE to the temporary parameter OBxx_EXC_FREQ of the cyclic interrupt OB.

#### Example

Call sequence in OB33

OB33

...

call LP_ZONE, DB_LP_ZONE

call ADM_ZONE, DB_ADM_ZONE

call ZONE, DB_ZONE1

call ZONE, DB_ZONE2

call ZONE, DB_ZONE3

…

BE

leads the following zone processing cycle:

![Example](images/24538795915_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Input parameters LP_ZONE (S7-300, S7-400)](#input-parameters-lp_zone-s7-300-s7-400)
  
[Output parameters LP_ZONE (S7-300, S7-400)](#output-parameters-lp_zone-s7-300-s7-400)
  
[In/out parameters LP_ZONE (S7-300, S7-400)](#inout-parameters-lp_zone-s7-300-s7-400)
  
[Static variables LP_ZONE (S7-300, S7-400)](#static-variables-lp_zone-s7-300-s7-400)

### Input parameters LP_ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| OB_EXC_FREQ | 0.0 | INT | 0 | Sampling time [ms]; interconnect the parameter with the corresponding local variables of the cyclic interrupt OB. |

---

**See also**

[Description LP_ZONE (S7-300, S7-400)](#description-lp_zone-s7-300-s7-400)
  
[Output parameters LP_ZONE (S7-300, S7-400)](#output-parameters-lp_zone-s7-300-s7-400)
  
[In/out parameters LP_ZONE (S7-300, S7-400)](#inout-parameters-lp_zone-s7-300-s7-400)
  
[Static variables LP_ZONE (S7-300, S7-400)](#static-variables-lp_zone-s7-300-s7-400)

### Output parameters LP_ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MNR_CALL | 2.0 | INT | 0 | Number of zones. Defined automatically after restart. |

---

**See also**

[Description LP_ZONE (S7-300, S7-400)](#description-lp_zone-s7-300-s7-400)
  
[Input parameters LP_ZONE (S7-300, S7-400)](#input-parameters-lp_zone-s7-300-s7-400)
  
[In/out parameters LP_ZONE (S7-300, S7-400)](#inout-parameters-lp_zone-s7-300-s7-400)
  
[Static variables LP_ZONE (S7-300, S7-400)](#static-variables-lp_zone-s7-300-s7-400)

### In/out parameters LP_ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| COM_RST | 4.0 | BOOL | TRUE | Restart; make sure that this bit is set in OB100. |

---

**See also**

[Description LP_ZONE (S7-300, S7-400)](#description-lp_zone-s7-300-s7-400)
  
[Input parameters LP_ZONE (S7-300, S7-400)](#input-parameters-lp_zone-s7-300-s7-400)
  
[Output parameters LP_ZONE (S7-300, S7-400)](#output-parameters-lp_zone-s7-300-s7-400)
  
[Static variables LP_ZONE (S7-300, S7-400)](#static-variables-lp_zone-s7-300-s7-400)

### Static variables LP_ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| LP_SCH | 6.0 | STRUCT |  | Interface between the instructions LP_ZONE and ADM_ZONE or ZONE . |

This is followed by internal parameters which may not be used by users.

---

**See also**

[Description LP_ZONE (S7-300, S7-400)](#description-lp_zone-s7-300-s7-400)
  
[Input parameters LP_ZONE (S7-300, S7-400)](#input-parameters-lp_zone-s7-300-s7-400)
  
[Output parameters LP_ZONE (S7-300, S7-400)](#output-parameters-lp_zone-s7-300-s7-400)
  
[In/out parameters LP_ZONE (S7-300, S7-400)](#inout-parameters-lp_zone-s7-300-s7-400)

## ADM_ZONE (S7-300, S7-400)

This section contains information on the following topics:

- [Description ADM_ZONE (S7-300, S7-400)](#description-adm_zone-s7-300-s7-400)
- [Output parameters ADM_ZONE (S7-300, S7-400)](#output-parameters-adm_zone-s7-300-s7-400)
- [In/out parameters ADM_ZONE (S7-300, S7-400)](#inout-parameters-adm_zone-s7-300-s7-400)
- [Static variables ADM_ZONE (S7-300, S7-400)](#static-variables-adm_zone-s7-300-s7-400)

### Description ADM_ZONE (S7-300, S7-400)

In practice, heating/cooling zones are designed to allow relatively unhindered heat transfer between zones. In such cases, the thermally coupled zones must be organized into a group. The instruction ADM_ZONE manages a group of heating/cooling zones and handles the following functions:

- Switching the heating of all zones on and off
- Enabling and disabling controller optimization
- Group display for channel faults
- Group display for controller optimization errors
- Group display for controller optimization warnings
- Control of the global manipulated value step-changes during controller optimization

#### Call

Call the instructions LP_ZONE, ADM_ZONE and ZONE at the same cyclic interrupt level, preferably immediately in the cyclic interrupt OB. It is not permitted to program separate time reduction ratios for the blocks. Call ADM_ZONE after LP_ZONE and before ZONE.

#### Start-up

Set the restart bit of ADM_ZONE, for example in OB100, or in the first cycle of the cyclic interrupt OB. The heating is disabled at the selected zones after restart and any active controller optimization is canceled.

#### Mode of operation

The actual program is only executed if the call counter of the instruction LP_ZONE has the same value as the internal call number: LP_SCH.CALL_CNT = NBR_CALL.

#### Switching the heating of all zones on and off

Changes at switch HEAT_OFF are transferred as actions to the ADMIN interface and are successively passed to the zones to be administered. If no action is pending, the result is transferred from the ADMIN.QHEAT_OFF zones to in/out parameter HEAT_OFF. Group switch HEAT_OFF is only set to TRUE if the heating is shut down at all zones.

User actions at the HEAT_OFF switch are indicated at the done parameter QHO_DONE. The parameter is set to TRUE by default. It is set to FALSE after a user action. QHO_DONE is reset to TRUE after the heating has been switched on or off at all associated zones.

A zone heating is only in disabled state if the following condition is met: cont_FM455.QLMN_RE = TRUE and cont_FM455.LMN = 0.0

#### Switching controller optimization on and off at all zones

Changes at switch TUN_ON are transferred as actions to the ADMIN interface and are successively passed to the zones to be administered. If no action is pending, the result is transferred from the ADMIN.QTUN_ON zones to in/out parameter TUN_ON. Group switch TUN_ON is only set to FALSE if controller optimization is disabled at all zones.

#### Group display for channel faults

Bit QCH_F indicates whether a channel error of FM 455 is pending on at least one zone. Check on which zone a channel error has occurred. If QCH_F = TRUE, then the precise error information is read out in the diagnostic record DS1 of the module.

#### Group display for controller optimization errors

Bit QTUN_ERR indicates if an error has occurred in at least one instance DB of the ZONESTATUS_H =  3xxxx or STATUS_C = 3xxxx instruction. Check the corresponding zones and to remedy errors follow the steps described at [Parameters STATUS_H and STATUS_C](#parameters-status_h-and-status_c-s7-300-s7-400).

#### Group display for controller optimization warnings

Bit QTUN_ERR indicates if an error has occurred in at least one instance DB of the ZONESTATUS_H =  2xxxx or STATUS_C = 2xxxx instruction. Check the corresponding zones and to remedy errors follow the steps described at [Parameters STATUS_H and STATUS_C](#parameters-status_h-and-status_c-s7-300-s7-400).

#### Sequential control during controller optimization

The administration block ensures that the manipulated value step-change is carried out simultaneously at all zones of this group during controller optimization. After having found their point of inflection, all zones change over to phase 7.

> **Note**
>
> Interconnect the in/out parameter ADMIN of the instruction ZONE with the internal structure ADMIN of the instance DB of ADM_ZONE.
>
> ADM_ZONE is always used in conjunction with LP_ZONE.

---

**See also**

[Output parameters ADM_ZONE (S7-300, S7-400)](#output-parameters-adm_zone-s7-300-s7-400)
  
[In/out parameters ADM_ZONE (S7-300, S7-400)](#inout-parameters-adm_zone-s7-300-s7-400)
  
[Static variables ADM_ZONE (S7-300, S7-400)](#static-variables-adm_zone-s7-300-s7-400)

### Output parameters ADM_ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| QCH_F | 0.0 | BOOL | FALSE | Group message: Channel error |
| QTUN_ERR | 0.1 | BOOL | FALSE | Group message: Error during controller optimization |
| QTUN_WRN | 0.2 | BOOL | FALSE | Group message: Warning during controller optimization |
| QHO_DONE | 0.3 | BOOL | TRUE | Feedback of a HEAT_OFF operation   - 0: HEAT_OFF operation is triggered - 1: HEAT_OFF operation is active at all zones |
| NBR_CALL | 2.0 | INT | 0 | Call number; entered automatically by the instruction after restart. |

---

**See also**

[Description ADM_ZONE (S7-300, S7-400)](#description-adm_zone-s7-300-s7-400)
  
[In/out parameters ADM_ZONE (S7-300, S7-400)](#inout-parameters-adm_zone-s7-300-s7-400)
  
[Static variables ADM_ZONE (S7-300, S7-400)](#static-variables-adm_zone-s7-300-s7-400)

### In/out parameters ADM_ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| HEAT_OFF | 4.0 | BOOL | TRUE | Heating off/on; 1 = off |
| TUN_ON | 4.1 | BOOL | FALSE | Controller optimization on/off; 1 = on |
| COM_RST | 4.2 | BOOL | TRUE | Restart; make sure that this bit is set in OB100. |
| LP_SCH | 6.0 | STRUCT | P#P 0.0 | Interface between the instructions LP_ZONE and ADM_ZONE or ZONE. |

---

**See also**

[Description ADM_ZONE (S7-300, S7-400)](#description-adm_zone-s7-300-s7-400)
  
[Output parameters ADM_ZONE (S7-300, S7-400)](#output-parameters-adm_zone-s7-300-s7-400)
  
[Static variables ADM_ZONE (S7-300, S7-400)](#static-variables-adm_zone-s7-300-s7-400)

### Static variables  ADM_ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| ADMIN | 12.0 | STRUCT |  | Interface between the instructions ADM_ZONE and ZONE . |

This is followed by internal parameters which may not be used by users.

---

**See also**

[Description ADM_ZONE (S7-300, S7-400)](#description-adm_zone-s7-300-s7-400)
  
[Output parameters ADM_ZONE (S7-300, S7-400)](#output-parameters-adm_zone-s7-300-s7-400)
  
[In/out parameters ADM_ZONE (S7-300, S7-400)](#inout-parameters-adm_zone-s7-300-s7-400)

## ZONE (S7-300, S7-400)

This section contains information on the following topics:

- [Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
- [Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
- [Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
- [Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
- [In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
- [Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
- [Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
- [Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
- [Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
- [Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### Description ZONE (S7-300, S7-400)

The instance DB of the instruction ZONE contains the controller data of an individual heating or heating/cooling zone. The instruction ZONE reads and writes data to a channel of FM 455.

The controller functions of FM 455 are supplemented with the following functions:

- Control zone operation
- Ratio factor for heating/cooling zones
- Controller optimization

ZONE is therefore particularly suitable for controlling the heating and heating/cooling zones of extruders.

#### Requirements

The channel of the FM 455 is configured as pulse controller or continuous controller.

The instructions PID_FM_455 and PID_PAR_455 are copied to the user program.

#### Call

Call the instructions LP_ZONE, ADM_ZONE and ZONE at the same cyclic interrupt level, preferably immediately in the cyclic interrupt OB. It is not permitted to program separate time reduction ratios for the blocks. It is essential to position the associated zones in the block after the call of the instruction ADM_ZONE.

#### Start-up

In OB100, set the restart bit of ZONE. The bit is set automatically if you are using LP_ZONE.

Following actions are carried out when initialization routine COM_RST=TRUE

is initiated:

- cont_FM455.SDB_SEL = TRUE: SDB controller parameters cont_FM455.P_SEL...cont_FM455.BREAK_TM are not applied by FM 455. The parameters active in the FM remain active.
- cont_FM455.SP_OP_ON = FALSE: This setting activates setpoint SP_RE.
- cont_FM455.LOAD_PAR = TRUE: The controller parameters are transferred from the instance DB to FM 455.

#### Mode of operation

ZONE includes the instructions PID_FM_455 and PID_PAR_455 as local instances.

ZONE sets the parameters cont_FM455.LOAD_OP = TRUE and cont_FM455.READ_VAR = TRUE at each call. All operating parameters (cont_FM455.SP_RE...cont_FM455.LMNRSVAL) and all process values (cont_FM455.SP...cont_FM455.QMOD_F) are updated as a result.

Controller parameters (cont_FM455.P_SEL...cont_FM455.BREAK_TM) can be modified directly by entering a new value at the instance DB on the CPU and setting the cont_FM455.LOAD_PAR bit for the duration of one cycle. You do not require an auxiliary DB. The bit is reset on successful completion of the transfer. After the restart of the CPU the controllers are not overwritten by the controller parameters of the SDB.

If you are working without LP_ZONE, you must set parameter NBR_CALL=0.

---

**See also**

[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)

The following list contains the parameters of instruction PID_FM_455 that are affected by ZONE:

| Parameters | Comment |
| --- | --- |
| cont_FM455.READ_VAR | Set cyclically to TRUE |
| cont_FM455.LOAD_OP | Set cyclically to TRUE |
| cont_FM455.LOAD_PAR | Set to TRUE during controller optimization and during modification of the CONZONE and RATIOFAC parameters. |
| cont_FM455.MOD_ADDR | Set cyclically at input MOD_ADDR. |
| cont_FM455.CHANNEL | Set cyclically at input CHANNEL. |
| cont_FM455.SDB_SEL | Set to TRUE at restart.  At the CPU transition from RUN to STOP, FM 455 rejects the controller parameters (P_SEL...BREAK_TM) of the SDB. |
| cont_FM455.SP_OP_ON | Set to FALSE at the restart so that SP_RE is active. |
| cont_FM455.SP_RE | Set cyclically to SP_IN |
| cont_FM455.GAIN   cont_FM455.TI  cont_FM455.TD   cont_FM455.TM_LAG   cont_FM455.D_EL_SEL  cont_FM455.PFDB_SEL  cont_FM455.LOAD_PAR | Set during controller optimization, when restoring controller parameters from backup, and when loading PI/PID controller parameters. |
| cont_FM455.LMN_LLM   cont_FM455.LOAD_PAR | Set after modification of RATIOFAC and COOLZONE |
| cont_FM455.LMN_REON   cont_FM455.LMN_RE   cont_FM455.LOAD_OP | Set cyclically |

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)

The following list contains the parameters of instruction PID_PAR_455, that are affected by ZONE:

| Parameters | Comment |
| --- | --- |
| pidpar_FM455.COM_RST | Set to TRUE at restart |
| pidpar_FM455.MOD_ADDR | Set cyclically at input MOD_ADDR. |
| pidpar_FM455.CHANNEL | Set cyclically at input CHANNEL. |
| pidpar_FM455. INDEX_R | Set to 43 after modification of RATIOFAC and COOLZONE |
| pidpar_FM455. VALUE _R | Set after modification of RATIOFAC and COOLZONE: |

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### Input parameters ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 512 | Module address |
| CHANNEL | 2.0 | INT | 1 | Channel number |
| LPSCH_EN | 4.0 | BOOL | TRUE | If LPSCH_EN = TRUE, ZONE is controlled via the instruction LP_ZONE. The in/out parameter LP_SCH must be interconnected with the static variable LP_SCH of the instruction LP_ZONE. Otherwise the CPU goes to STOP with "Range error while reading".  If LPSCH_EN = FALSE, ZONE is processed at each cyclic interrupt cycle. It is not necessary to supply the in/out parameter LP_SCH. The sampling time must be entered at a static variable CYCLE. |
| ADMIN_EN | 4.1 | BOOL | TRUE | If ADMIN_EN = TRUE, several heating/cooling zones are handled via the instruction ADM_ZONE. The in/out parameter ADMIN must be interconnected with the static variable ADMIN of the instruction ADM_ZONE. Otherwise the CPU goes to STOP with "Range error while reading".  If ADMIN_EN = FALSE, ZONE works without the instruction ADM_ZONE. It is not necessary to supply the in/out parameter ADMIN. |

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### In/out parameters ZONE  (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| LP_SCH | 6.0 | STRUCT | P#P 0.0 | Interface between the instructions LP_ZONE and ADM_ZONE or ZONE. |
| ADMIN | 12.0 | STRUCT | P#P 0.0 | Interface between the instructions ADM_ZONE and ZONE . |

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### Static variables ZONE  (S7-300, S7-400)

| Parameters | Address |  | Data type | Default | Description |
| --- | --- | --- | --- | --- | --- |
| cont_FM455 | 18.0 |  | FB   PID_FM_455 |  | Local instance of the instruction PID_FM_455 |
| pidpar_FM455 | 172.0 |  | FB PID_PAR_455 |  | Local instance of the instruction PID_PAR_455 |
| SP_IN | 426.0 |  | REAL | 0.0 | The input SP_IN is used to specify a setpoint. |
| CYCLE | 430.0 |  | REAL | 0.1 | Sets the sampling time for the PID algorithm. If used, the instruction LP_ZONE automatically calculates the sampling time of LP_ZONE. |
| H_OFF_EN | 434.0 |  | BOOL | TRUE | TRUE = switch HEAT_OFF is active and affects the parameters MAN_ON and MAN. |
| TUN_EN | 434.1 |  | BOOL | TRUE | No new controller parameters are calculated if TUN_EN=0 during controller optimization. Caution: the manipulated value step-change is enabled regardless of this setting. |
| COOLZONE | 434.2 |  | BOOL | FALSE | COOLZONE = FALSE: Self-contained heating zone   COOLZONE = TRUE: Heating/cooling zone |
| PID_ON | 434.3 |  | BOOL | TRUE | At the PID_ON input, you can specify whether or not the tuned controller will operate as a PI or PID controller.   PID controller: PID_ON = TRUE  PI controller: PID_ON = FALSE  With certain process types it is nevertheless possible that only a PI controller will be designed despite PID_ON = TRUE. |
| QCH_F | 434.4 |  | BOOL | FALSE | QCH_F = TRUE: A channel error of FM 455 has occurred during the calling of the local instance of the instruction PID_FM_455 (parameter cont_FM455.QCH_F). |
| QTUN_ERR | 434.5 |  | BOOL | FALSE | QTUN_ERR = TRUE: Incorrect operator action occurred during controller optimization.  STATUS_H or STATUS_C = 3xxxx |
| QTUN_WRN | 434.6 |  | BOOL | FALSE | QTUN_WRN = TRUE: : Warning message occurred during controller optimization.  STATUS_H or STATUS_C = 2xxxx |
| QTUNSTCP | 434.7 |  | BOOL | FALSE | QTUNSTCP = TRUE: Tuning was initiated in cold process state and the controller is to be corrected to the operating point after optimization.   MAN_ON = FALSE; MAN = 0 (Heating off)   SP_IN > PV0 +10  (At the start of optimization, the operating point is greater than the process value by the amount of 10) |
| QCONTINU | 435.0 |  | BOOL | TRUE | Indicates whether the zone is ready for the next phase of controller optimization |
| PHASE | 436.0 |  | INT | 0 | The currently active phase of controller optimization is indicated at the [Parameter PHASE](#parameter-phase-s7-300-s7-400) (0 to 7, 11 to13). |
| STATUS_H | 438.0 |  | INT | 0 | [Parameter STATUS_H](#parameters-status_h-and-status_c-s7-300-s7-400) indicates a diagnostic value via the search for the point of inflection during the heating process. |
| STATUS_C | 440.0 |  | INT | 0 | [Parameter STATUS_C](#parameters-status_h-and-status_c-s7-300-s7-400) indicates a diagnostic value via the search for the point of inflection during the cooling process. |
| STATUS_D | 442.0 |  | INT | 0 | [Parameter STATUS_D](#parameters-status_d-s7-300-s7-400) indicates a diagnostic value via the controller design during the heating process. |
| PI_CON | 444.0 |  | STRUCT |  | PI controller parameters |
| GAIN |  | +0.0 | REAL | 0.0 | PI controller gain |
| TI |  | +4.0 | REAL | 0.0 | PI integration time [s] |
|  |  | =8.0 | END_STRUCT |  |  |
| PID_CON | 452.0 |  | STRUCT |  | PID controller parameters |
| GAIN |  |  | REAL | 0.0 | PID controller gain |
| TI |  |  | REAL | 0.0 | PID integration time [s] |
| TD |  |  | REAL | 0.0 | PID derivative action time [s] |
|  | =12.0 |  | END_STRUCT |  |  |
| PAR_SAVE | 464.0 |  | STRUCT |  | The PID parameters are saved in this structure. |
| GAIN |  | +0.0 | REAL | 0.0 | Controller gain |
| TI |  | +4.0 | REAL | 0.0 | Integration time [s] |
| TD |  | +8.0 | REAL | 0.0 | Derivative action time (s) |
| TM_LAG |  | +12.0 | REAL | 0.0 | Time lag of the D-action [s] |
| D_EL_SEL |  | +16.0 | INT | 0 | D-action element input |
| PFDB_SEL |  | +18.0 | BOOL | FALSE | P-action in feedback loop |
| CONZ_ON |  | +18.1 | BOOL | FALSE | Enable control zone |
| CON_ZONE |  | +20.0 | REAL | 100.0 | Control zone band |
| RATIOFAC |  | +24.0 | REAL | 1.0 | Ratio of heating gain/cooling gain of the process. |
|  |  | =28.0 | END_STRUCT |  |  |
| HEAT_OFF | 492.0 |  | BOOL | FALSE | TRUE = disable heating  You must set H_OFF_EN = TRUE to activate HEAT_OFF.   - MAN_ON=TRUE and MAN=0.0 when HEAT_OFF is set. - MAN_ON=FALSE when HEAT_OFF is reset. |
| TUN_ON | 492.1 |  | BOOL | FALSE | Enable controller optimization  Set TUN=TRUE only for one cycle. TUN_ON is reset automatically after tuning. |
| CTUN_ON | 492.2 |  | BOOL | FALSE | Enable only cooling optimization   Set CTUN =TRUE only for one cycle. CTUN _ON is reset automatically after tuning. |
| COM_RST | 492.3 |  | BOOL | FALSE | A initialization routine is initiated |
| TUN_LMN | 494.0 |  | REAL | 80.0 | Process excitation for controller optimization starting in cold process state is initiated by a manipulated value step by the amount of TUN_LMN. |
| TUN_DLMN | 498.0 |  | REAL | 20.0 | Process excitation for controller optimization at the operating point is initiated by a manipulated value step by the amount of TUN_DLMN. |
| TUN_CLMN | 502.0 |  | REAL | -10.0 | Manipulated value after the start of cooling optimization. |
| STAT_TM | 506.0 |  | REAL | 30.0 | Time for steady state condition for controller optimization phase 1 or 11   The process is considered in steady state if the process value or manipulated value do not change by more than the amount of 2*STAT_D_PV or 2*STATDLMN within the time STAT_TM. |
| STAT_DPV | 510.0 |  | REAL | 1.0 | Process value delta for the steady state condition in controller optimization phase 1 or 11   See STAT_TM . |
| STATDLMN | 514.0 |  | REAL | 4.0 | Manipulated value delta for the steady state condition in controller optimization phase 1 or 11   See STAT_TM. |
| RATIOFAC | 518.0 |  | REAL | 1.0 | Ratio of heating gain/cooling gain of the process.   The low output limit and "Range start of the input signal of manipulated value B of the split-range function" are adapted automatically. |
| CON_ZONE | 522.0 |  | REAL | 100.0 | Control zone  If ER >= CON_ZONE, then LMN = LMN_HLM.  If ER <= -CON_ZONE (or -CON_ZONE /RATIOFAC), then LMN = LMN_LLM. |
| MAN | 526.0 |  | REAL | 0.0 | Manual value   HEAT_OFF affects the parameter if  H_OFF_EN=TRUE . |
| MAN_ON | 530.0 |  | BOOL | TRUE | Manual/automatic mode changeover  HEAT_OFF affects the parameter if H_OFF_EN=TRUE . |
| CONZ_ON | 530.1 |  | BOOL | FALSE | TRUE = control zone enabled |
| UNDO_PAR | 530.2 |  | BOOL | FALSE | Copies the controller parameters of structure PAR_SAVE to the following parameters:  - cont_FM455.GAIN - cont_FM455.TI - cont_FM455.TD - cont_FM455.TM_LAG - cont_FM455.D_EL_SEL - cont_FM455.PFDB_SEL - CONZ_ON - CON_ZONE - RATIOFAC   The parameters are then downloaded to FM 455.   This function is not executed in automatic mode. |
| SAVE_PAR | 530.3 |  | BOOL | FALSE | Saves the following controller parameters to the structure PAR_SAVE:  - cont_FM455.GAIN - cont_FM455.TI - cont_FM455.TD - cont_FM455.TM_LAG - cont_FM455.D_EL_SEL - cont_FM455.PFDB_SEL - CONZ_ON - CON_ZONE - RATIOFAC |
| LOAD_PID | 530.4 |  | BOOL | FALSE | Load PI/PID parameters:   If PID_ON=TRUE, it copies the PID parameters of structure PID_CON to the following parameters:   - cont_FM455.GAIN - cont_FM455.TI - cont_FM455.TD - cont_FM455.TM_LAG   If PID_ON=FALSE, it copies the PI parameters of structure PI_CON to the following parameters:   - cont_FM455.GAIN - cont_FM455.TI - cont_FM455.TD = 0.0 - cont_FM455.TM_LAG = 0.5   The parameters are then downloaded to FM455.   This function is not executed in automatic mode. |
| BTUN_DPV | 532 |  | REAL | 0.0 | Process value difference for automatic cancellation of optimization. |
| BTUN_TM | 536 |  | REAL | 300.0 | Time following the manipulated value step-change for automatic cancellation of optimization. |

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### Variables for controller optimization ZONE (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| GAIN_P | 540.0 | REAL | 0.0 | Identified process gain. |
| TU | 544.0 | REAL | 0.0 | Identified time lag of the process. |
| TA | 548.0 | REAL | 0.0 | Identified recovery time of the process. |
| KIG | 552.0 | REAL | 0.0 | Maximum possible rate of rise of the process value during heating. |
| KIG_C | 556.0 | REAL | 0.0 | Maximum decay rate of the process value during cooling. |
| N_PTN | 560.0 | REAL | 0.0 | Order of the process. "Non-integer values" are also possible. |
| TM_LAG_P | 564.0 | REAL | 0.0 | Time constant of a PTN model. (practical values for N_PTN>=2 only). |
| T_P_INF | 568.0 | REAL | 0.0 | Time from process excitation until the point of inflection. |
| P_INF | 572.0 | REAL | 0.0 | Process value change from process excitation until the point of inflection. |
| LMN0 | 576.0 | REAL | 0.0 | Manipulated value at the start of optimization  Calculated in phase 1 (mean value). |
| PV0 | 580.0 | REAL | 0.0 | Process value at the start of optimization  Calculated in phase 1 (mean value). |
| PVDT0 | 584.0 | REAL | 0.0 | Process value slew rate at the start of optimization |
| PVDT | 588.0 | REAL | 0.0 | Current process value slew rate |
| PVDT_MAX | 592.0 | REAL | 0.0 | Maximum derivative of the process value at the point of inflection (sign adapted, always > 0); is used to calculate TU and KIG. |
| NOI_PVDT | 596.0 | REAL | 0.0 | Noise action in PVDT_MAX in %   The higher the noise action, the less accurate (less aggressive) the control parameters. |
| NOISE_PV | 600.0 | REAL | 0.0 | Absolute process value noise   Difference between maximum and minimum process value in phase 1. |
| FIL_CYC | 604.0 | INT | 1 | Number of cycles of mean value filters 1 to 1024;   The process value is determined through FIL_CYC cycles. FIL_CYC is increased from 1 to a max. of 1024 if needed. |
| POI_CMAX | 606.0 | INT | 0 | Maximum number of cycles after inflection point   This time is used to find another (i.e. better) inflection point for measuring noise. The optimization is completed only after this time. |
| POI_CYCL | 608.0 | INT | 0 | Number of cycles after inflection point |
| NBR_CALL | 610.0 | INT | -1 | Call number; is entered automatically after restart. |

This is followed by internal parameters which may not be used by users.

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### Parameters STATUS_H and STATUS_C (S7-300, S7-400)

STATUS_H indicates a diagnostic value via the search for the point of inflection during the heating process, STATUS_C beim during the cooling process.

If a diagnostic value 2xxxx is displayed, QTUN_WRN = TRUE

If a diagnostic value 3xxxx is displayed, QTUN_ERR = TRUE

| STATUS_ H STATUS_C | Description | Remedy |
| --- | --- | --- |
| 0 | Default, or no/no new controller parameters |  |
| 10000 | Tuning completed + suitable controller parameters found |  |
| 2xxxx | Tuning completed + controller parameters uncertain |  |
| 2xx2x | Point of inflection not reached   (only when optimization from cold process state to the operating point QTUNSTCP =TRUE) | If the controller oscillates, weaken the controller parameters, or repeat the test with a smaller manipulated value difference TUN_LMN. |
| 2x1xx | Estimation error TU too small  TU < 3*CYCLE | Reduce CYCLE and repeat the test.  Special case self-contained PT1 process:: Do not repeat the test; weaken the controller parameters if need be. |
| 2x2xx | Estimation error T_P_INF too small T_P_INF < 72.8*CYCLE | see 2x1xx |
| 2x3xx | Estimation error TU too small and estimation error T_P_INF too small | see 2x1xx |
| 3xxxx | Tuning canceled. No controller parameter found. |  |
| 30002 | For heating optimization:  Effective manipulated variable difference < 5%   For cooling optimization:  TUN_CLMN > -5 % | Correct manipulated value difference TUN_LMN, TUN_DLMN or TUN_CLMN. |
| 30003 | Incorrect manipulated variable low output limit for cooling optimization. cont_FM455.LMN_LLM > -5.0 | Set zone as heating/cooling zone COOLZONE =TRUE and check cont_FM455.LMN_LLM. |
| 30004 | Effective manipulated value difference is limited by split-range limits and not by manipulated value limits. | Check limits of the manipulated values and split-range.   Correct manipulated value difference TUN_LMN, TUN_DLMN or TUN_CLMN. |
| 30005 | Sampling time CYCLE deviates by more than 5% from the measured value. | Compare CYCLE with the cycle time of the cyclic interrupt level and monitor possibly existing loop scheduler.   Check CPU load. Excessive load on CPU resources leads to extended sampling times that no longer match CYCLE. |
| 30008 | An attempt is being made to initiate cooling optimization. However, no heating optimization was carried out beforehand (KIG=0.0). | Start with a heating optimization session. |
| 30009 | Safety mode: cont_FM455.QLMNSAFE = TRUE | Exit the safety mode and restart optimization. |
| 30010 | No adequate temperature change after modification of heating/cooling output. | Check the signal profile of the manipulated variable and time. Check plausibility of the parameters BTUN_TM and BTUN_DPV. |

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)
  
[Output parameters ADM_ZONE (S7-300, S7-400)](#output-parameters-adm_zone-s7-300-s7-400)

### Parameters STATUS_D (S7-300, S7-400)

| STATUS_D | Description |
| --- | --- |
| 0 | No controller parameters were calculated. |
| 110 | N_PTN <= 1.5 process type I fast |
| 121 | N_PTN > 1.5 process type I |
| 200 | N_PTN > 1.9 process type II (transition range) |
| 310 | N_PTN >= 2.1 process type III fast |
| 320 | N_PTN > 2.6 process type III |
| 111, 122, 201, 311, 321 | Parameters have been corrected from phase 7. |

> **Note**
>
> STATUS_H = 0 is reset at the end of phase 1. If you cancel optimization in phase 2, STATUS_H = 0 is set. However, STATUS_D still displays the status of the last controller calculation.
>
> The higher the value of STATUS_D, the higher the order of the control process, the greater the TU/TA ratio and the gentler the controller parameters will be.

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameter PHASE (S7-300, S7-400)](#parameter-phase-s7-300-s7-400)

### Parameter PHASE (S7-300, S7-400)

| PHASE | Description |
| --- | --- |
| 0 | No optimization mode; automatic or manual mode |
| 1 | Steady state test; parameter check; feed forwarding of a constant heating manipulated variable |
| 2 | Searching for point of inflection with constant manipulated value |
| 3 (1 cycle per instruction ZONE) | Calculating the process parameters. Saving currently valid controller parameters prior to optimization |
| 4 (1 cycle per instruction ZONE) | Controller design |
| 5 (1 cycle per instruction ZONE) | Following up the controller to the new manipulated variable |
| 7 | Check of the process type (only for heating optimization) |
| 10 | Cooling optimization Wait until all zones zones are in automatic mode (phase > 2). |
| 11 | Cooling optimization Steady state test; parameter check; feed forwarding of a constant cooling manipulated variable |
| 12 | Cooling optimization: Searching for point of inflection with constant manipulated value |
| 13 | Cooling optimization: Calculating the heating/cooling ratio |

#### Heating Tuning Phases during First Adaption

The following figure shows the phases of self-contained heating optimization as a function of the ambient temperature and operating point:

![Heating Tuning Phases during First Adaption](images/18506886155_DV_resource.Stream@PNG-en-US.png)

#### Phases of Heating Tuning at the Operating Point

The following figure shows the phases of a self-contained heating optimization at the operating point.

![Phases of Heating Tuning at the Operating Point](images/18509933451_DV_resource.Stream@PNG-en-US.png)

After optimization was completed and the instruction has returned to Phase 0 and TUN_ON=FALSE is set, the parameters STATUS_H, STATUS_C or QTUN_WRN, QTUN_ERR indicate whether optimization was completed without errors.

---

**See also**

[Description ZONE (S7-300, S7-400)](#description-zone-s7-300-s7-400)
  
[Parameters of instruction PID_FM_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_fm_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Parameters of instruction PID_PAR_455 that are alterable with ZONE (S7-300, S7-400)](#parameters-of-instruction-pid_par_455-that-are-alterable-with-zone-s7-300-s7-400)
  
[Input parameters ZONE (S7-300, S7-400)](#input-parameters-zone-s7-300-s7-400)
  
[In/out parameters ZONE (S7-300, S7-400)](#inout-parameters-zone-s7-300-s7-400)
  
[Static variables ZONE (S7-300, S7-400)](#static-variables-zone-s7-300-s7-400)
  
[Variables for controller optimization ZONE (S7-300, S7-400)](#variables-for-controller-optimization-zone-s7-300-s7-400)
  
[Parameters STATUS_H and STATUS_C (S7-300, S7-400)](#parameters-status_h-and-status_c-s7-300-s7-400)
  
[Parameters STATUS_D (S7-300, S7-400)](#parameters-status_d-s7-300-s7-400)

## DB for HMI (S7-300, S7-400)

This section contains information on the following topics:

- [Description DB 101 to 116 (S7-300, S7-400)](#description-db-101-to-116-s7-300-s7-400)
- [Input parameters DB 101 to 116 (S7-300, S7-400)](#input-parameters-db-101-to-116-s7-300-s7-400)
- [Output parameters DB 101 to 116 (S7-300, S7-400)](#output-parameters-db-101-to-116-s7-300-s7-400)
- [In/out parameters DB 101 to 116 (S7-300, S7-400)](#inout-parameters-db-101-to-116-s7-300-s7-400)

### Description DB 101 to 116 (S7-300, S7-400)

In order to operate the FM 455 if the CPU fails, you require data blocks 101 to 104. You can establish a maximum of three connections from the FM 455 to OPs via MPI.

Operator control of the FM 455 with the OP is only possible in the STOP mode of the CPU or at a CPU failure.

Monitoring of the FM 455 with the OP is always possible.

The variable interface of the FM 455 contains 16 data blocks with the block numbers 101 to 116 for the controller channels 1 to 16 (refer to the following figure).

> **Note**
>
> The contents of the data blocks 101 to 116 do not automatically reflect the parameter value effective at the FM 455. Parameters changed with the OP are only transferred to the FM 455 after the operating bits LOAD_PAR or LOAD_OP have been set.
>
> If you change a parameter using OP operation without setting the corresponding operating bit, the changed parameter value is entered in the data block, but the FM 455 continues to operate internally with the unchanged old value of the parameter.
>
> After the operating bits have been set and the parameters have been transferred to the FM 455, the operating bits LOAD_PAR and LOAD_OP are reset by the FM 455.

![Figure](images/20038568587_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| * | controlled by the READ_VAR parameter of the instance DB |
| ** | controlled by the LOAD_OP and LOAD_PAR parameters |

### Input parameters DB 101 to 116 (S7-300, S7-400)

> **Note**
>
> The EEPROM of the module could become damaged in the case of too frequent write operations. To prevent this, after the description of the EEPROM, the module delays another description by 30 minutes.

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| <sup>1)</sup> Control parameters; <sup>2)</sup> Operating parameters |  |  |  |  |
| SP_HLM<sup>1)</sup> | 0.0 | REAL | 100.0 | The setpoint is always limited to a high and a low limit. The input "Setpoint high limit" indicates the high limit.  SP_HLM > SP_LLM |
| SP_LLM<sup>1)</sup> | 4.0 | REAL | 0.0 | The setpoint is always limited to a high and a low limit. The input "Setpoint low limit" specifies the low limit.  SP_LLM < SP_HLM |
| H_ALM<sup>1)</sup> | 8.0 | REAL | 100.0 | You can assign parameters for four limits for monitoring the process value or the error signal. The input "High limit interrupt" indicates the highest limit.  H_ALM > H_WRN |
| H_WRN<sup>1)</sup> | 12.0 | REAL | 90.0 | You can assign parameters for four limits for monitoring the process value or the error signal. The input “High limit warning” specifies the second to highest limit.  Values from H_ALM to L_WRN are permitted. |
| L_WRN<sup>1)</sup> | 16.0 | REAL | 10.0 | You can assign parameters for four limits for monitoring the process value or the error signal. The input “Low limit warning” specifies the second to highest limit.  Values from H_WRN to L_ALM are permitted. |
| L_ALM<sup>1)</sup> | 20.0 | REAL | 0.0 | You can assign parameters for four limits for monitoring the process value or the error signal. The input "Low limit alarm" specifies the lowest limit.  L_ALM < L_WRN |
| HYS<sup>1)</sup> | 24.0 | REAL | 1.0 | To prevent flickering of the monitoring displays, a hysteresis can be configured at the "Hysteresis" input.  HYS ≥ 0.0 |
| DEADB_W<sup>1)</sup> | 28.0 | REAL | 0.0 | A dead band is applied to the error signal. The "Dead band width" input determines the size of the dead band.  DEADB_W ≥ 0.0 |
| GAIN<sup>1)</sup> | 32.0 | REAL | 1.0 | The "Proportional gain" input specifies controller amplification. |
| TI<sup>1)</sup> | 36.0 | REAL | 3000.0 | The "Integration time" input determines the time  response of the integral action. If TI = 0, the integral action is disabled.  TI = 0.0 or TI ≥ 0.5 |
| TD<sup>1)</sup> | 40.0 | REAL | 0.0 | The "Derivative-action time" input determines the time  response of the differentiator. If TD = 0, the derivative action is disabled  TD = 0.0 or TD ≥ 1.0 |
| TM_LAG<sup>1)</sup> | 44.0 | REAL | 5.0 | The algorithm of the derivative action contains a delay for which parameters can be assigned at the input "Time lag of the derivative action".  TM_LAG ≥ 0.5 |
| LMN_SAFE<sup>1)</sup> | 48.0 | REAL | 0.0 | For the manipulated value, a safety value can be configured at the "Safety manipulated value" input.  Values from -100 to 100 % are permitted. |
| LMN_HLM<sup>1)</sup> | 52.0 | REAL | 100.0 | The manipulated value is always limited to a high and a low limit. The input "Manipulated value high limit" specifies the high limit.  (Does not apply to step controllers without analog position feedback)   Values from LMN_LLM to 100 % are permitted. |
| LMN_LLM<sup>1)</sup> | 56.0 | REAL | 0.0 | The manipulated value is always limited to a high and a low limit. The input "Manipulated value low limit" indicates the low limit.  (Does not apply to step controllers without analog position feedback)   Values from -100 to LMN_HLM are permitted. |
| MTR_TM<sup>1)</sup> | 60.0 | REAL | 60.0 | The runtime of the control valve from limit to limit is entered at the "Motor actuating time" parameter.  (Only in the case of step controllers)   MTR_TM ≥ 0.001 |
| PULSE_TM<sup>1)</sup> | 64.0 | REAL | 0.2 | A minimum pulse duration can be configured on the "Minimum pulse time" parameter.  (Only in the case of step controllers or pulse controllers) |
| BREAK_TM<sup>1)</sup> | 68.0 | REAL | 0.2 | A minimum break time can be set at the "Minimum break time" parameter.  (Only in the case of step controllers or pulse controllers) |
| SP_RE<sup>2)</sup> | 72.0 | REAL | 0.0 | An external setpoint is interconnected at input "External setpoint" with the controller.   Technical range of values (physic. variable) |
| LMN_RE<sup>2)</sup> | 76.0 | REAL | 0.0 | An external manipulated value is interconnected at the input "External manipulated value" with the controller.  Values from -100 to 100 % are permitted. |
| LMNRSVAL<sup>2)</sup> | 80.0 | REAL | 0.0 | The Commissioning dialog provides you with access to the input "Start value of the simulated position feedback". The start value of the simulation is entered at the parameter.  (only for step controllers without analog position feedback).   Values from -100 to 100 % are permitted. |
| SAFE_ON<sup>2)</sup> | 84.0 | BOOL | FALSE | If the "Enable safety position" input is set, a safety value is applied as the manipulated value.  Note: The signal processing of maninpulated values via LMNDN_OP, LMNUP_OP and LMNSOPON on a step controller is of higher priority than the safety manipulated value. |
| LMNTRKON<sup>2)</sup> | 84.1 | BOOL | FALSE | If input "Follow-up (LMN via AI)" is set, the manipulated value is adjusted to an analog input (AI).  (Does not apply to step controllers without analog position feedback) |
| LMN_REON<sup>2)</sup> | 84.2 | BOOL | FALSE | If input "Enable external manipulated value" is set, the external manipulated value LMN_RE is set as the manipulated value. |
| LMNRHSRE<sup>2)</sup> | 84.3 | BOOL | FALSE | The signal “Control valve at high endstop” is interconnected at the input “High stop signal of position feedback”. LMNRHSRE = TRUE means: The control valve is at high endstop.  (Only in the case of step controllers) |
| LMNRLSRE<sup>2)</sup> | 84.4 | BOOL | FALSE | The signal “Control valve at low endstop” is interconnected at the input “Low endstop signal of position feedback”. LMNRLSRE = TRUE means: The control valve is at low endstop.  (Only in the case of step controllers) |
| LMNSOPON<sup>2)</sup> | 84.5 | BOOL | FALSE | If the bit is set at input "Enable manipulated value signal operation", the LMNUP_OP and LMNDN_OP signals are set as the manipulated value signals.  (Only in the case of step controllers) |
| LMNUP_OP<sup>2)</sup> | 84.6 | BOOL | FALSE | If LMNSOPON is set, the value at input "Manipulated value signal up operation" is set as the manipulated value signal.  (Only in the case of step controllers) |
| LMNDN_OP<sup>2)</sup> | 84.7 | BOOL | FALSE | If LMNSOPON is set, the value at input "Manipulated value signal down operation" is set as the manipulated value signal.  (Only in the case of step controllers) |
| MONERSEL<sup>1)</sup> | 85.0 | BOOL | FALSE | The controller has a limit indicator that can be applied either for the process value or the error signal. If the input "Monitoring: Process value = 0, control error = 1" is set, the control error is monitored. |
| LMNRS_ON<sup>2)</sup> | 85.1 | BOOL | FALSE | You can simulate position feedback if this is not available. The function is enabled by setting the "Enable simulation of position feedback" input CAUTION: Offset between the simulation value and real position feedback increases over the time.  (only for step controllers without analog position feedback). |
| FUZID_ON<sup>2)</sup> | 85.2 | BOOL | FALSE | The "Enable fuzzy identification" input is used to enable identification of the fuzzy algorithm. |
| SPINT_EN<sup>2)</sup> | 85.3 | BOOL | FALSE | The input "Operator input: External = 0, Internal = 1" determines the input that is transferred as a setpoint to the module.  SPINT_EN = TRUE: SP_INT is transferred.  SPINT_EN = FALSE: SP_RE is transferred. |
| P_SEL<sup>1)</sup> | 85.4 | BOOL | TRUE | In the PID algorithm, the PID actions can be enabled and disabled separately. The proportional action is enabled if the "Enable P-action" input is set |
| PFDB_SEL<sup>1)</sup> | 85.5 | BOOL | FALSE | In the PID algorithm, the P and D actions can be positioned in the feedback. If input "Enable P-action in feedback" is set, the proportional action is located in the feedback loop. |
| D_EL_SEL<sup>1)</sup> | 86.0 | INT | 0 | The D-action element in the PID algorithm can be positioned at a separate input. This is selected at the input "D-action element input".  - 0: Error signal - 1 to 16:: Analog input 1 to 16 - 17: Negative process value |

---

**See also**

[Output parameters DB 101 to 116 (S7-300, S7-400)](#output-parameters-db-101-to-116-s7-300-s7-400)
  
[In/out parameters DB 101 to 116 (S7-300, S7-400)](#inout-parameters-db-101-to-116-s7-300-s7-400)

### Output parameters DB 101 to 116 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SP | 94.0 | REAL | 0.0 | The setpoint that is currently in effect is available at the "Setpoint" output. |
| PV | 98.0 | REAL | 0.0 | The process value that becomes effective is issued on the "Process value" output. |
| ER | 102.0 | REAL | 0.0 | The control deviation that becomes effective is issued on the "Control deviation" output. |
| DISV | 106.0 | REAL | 0.0 | The interference that becomes effective is issued on the "Interference" output.  Values from -100 to 100 % are permitted. |
| LMN | 110.0 | REAL | 0.0 | The manipulated value that becomes effective is issued on the "Manipulated value" output. Step controllers without analog position feedback output the unlimited P- + D-action at the LMN parameter.   Values from -100 to 100 % are permitted. |
| LMN_A | 114.0 | REAL | 0.0 | At the output "Manipulated value A of the split range function / position feedback", continuous controllers display the manipulated value A and step controllers with analog position feedback display the position feedback.  Step controllers without analog position feedback display the simulated position feedback.   Values from -100 to 100 % are permitted. |
| LMN_B | 118.0 | REAL | 0.0 | Continuous controllers display the manipulated value B of the split-range function at the output “Manipulated value B of split-range function”.   Values from -100 to 100 % are permitted. |
| QH_ALM | 122.0 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of H_ALM limit is reported at the output "High limit alarm triggered". |
| QH_WRN | 122.1 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of H_WRN limit is reported at the output "High limit warning triggered". |
| QL_WRN | 122.2 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of the L_WRN limit is reported at output "Low limit warning triggered". |
| QL_ALM | 122.3 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of the L_ALM limit is reported at output "Low limit alarm triggered". |
| QLMN_HLM | 122.4 | BOOL | FALSE | The manipulated value is always limited to a high and a low limit. Violation of the high limit is reported at output "High limit of manipulated value triggered".  (Does not apply to step controllers without analog position feedback) |
| QLMN_LLM | 122.5 | BOOL | FALSE | The manipulated value is always limited to a high and a low limit. Violation of the low limit is reported at output "Low limit of manipulated value triggered".  (Does not apply to step controllers without analog position feedback) |
| QSPINTON | 122.6 | BOOL | FALSE | The output "Internal setpoint on" indicates that SP_INT was transferred to the module. |
| QPARA_F | 123.0 | BOOL | FALSE | The module checks the validity of the parameters. A parameter assignment error is displayed at the "Parameter assignment error" output. These parameter assignment errors can also be read out in the module's "Online & Diagnostics" dialog. |
| QCH_F | 123.1 | BOOL | FALSE | The "Channel error" output is set if the controller channel cannot provide valid results. A channel error (for example, wire break) is also set if QPARA_F = 1 or QMOD_F = 1. If QCH_F = TRUE, then the precise error information in the diagnostic data record DS1 of the module is read out. |
| QUPRLM | 123.2 | BOOL | FALSE | The setpoint is limited to a positive and negative slew rate. If the output "Limit of positive setpoint slew rate triggered" is set, the positive setpoint slew rate is limited. |
| QDNRLM | 123.3 | BOOL | FALSE | The setpoint is limited to a positive and negative slew rate. If the output "Limit of negative setpoint slew rate triggered" is set, the setpoint fall is limited. |
| QSP_HLM | 123.4 | BOOL | FALSE | The setpoint is always limited to a high and a low limit. The output "High limit of setpoint value triggered" indicates that the high limit has been exceeded. |
| QSP_LLM | 123.5 | BOOL | FALSE | The setpoint is always limited to a high and a low limit. Violation of the low limit is reported at output "Setpoint low limit triggered". |
| QSPOPON | 123.6 | BOOL | FALSE | The output "Setpoint operation on" shows if the setpoint is being operated via the "Commissioning" dialog. If the bit is set, the value SP_OP is applied as setpoint. |
| QLMNSAFE | 123.7 | BOOL | FALSE | If the output "Safety mode" is set, the safety manipulated value is output as the manipulated value. |
| QLMNOPON | 124.0 | BOOL | FALSE | The output "Manipulated value operation on" shows if the manipulated value is being operated via the "Commissioning" dialog. If the bit is set, the value LMN_OP is applied as manipulated value. |
| QLMNTRK | 124.1 | BOOL | FALSE | The output "Follow-up mode" indicates if the manipulated value is being adjusted via an analog input. |
| QLMN_RE | 124.2 | BOOL | FALSE | The output "Manual = 1; Automatic = 0" indicates whether or not the manipulated value is set on the external manipulated value LMN_RE (manual = 1). |
| QLMNR_HS | 124.3 | BOOL | FALSE | The output "High endstop signal of position feedback" indicates if the control valve is at its high endstop. QLMNR_HS = TRUE means: The control valve is at high endstop.  (For step controllers only) |
| QLMNR_LS | 124.4 | BOOL | FALSE | The output "Low endstop signal of position feedback" indicates whether the control valve is at its low endstop. QLMNR_LS = TRUE means: The control valve is at its low endstop.  (For step controllers only) |
| QLMNR_ON | 124.5 | BOOL | FALSE | Output "Position feedback enabled" indicates the set operating mode "Step controller with position feedback" or "Step controller without position feedback". |
| QFUZZY | 124.6 | BOOL | FALSE | If the output "PID algorithm = 0; fuzzy = 1", the controller is working with the fuzzy algorithm. |
| QSPLEPV | 124.7 | BOOL | FALSE | The output "Display of FUZZY controller: Setpoint < process value" is set when the fuzzy controller is switched on, if the setpoint is less than the effective process value. |
| QSPR | 125.0 | BOOL | FALSE | If the output "Split-range operation" is set, the continuous controller is operating in split-range mode. |
| QLMNUP | 125.1 | BOOL | FALSE | This is the "Manipulated value signal up" output.  (Only in the case of step controllers or pulse controllers) |
| QLMNDN | 125.2 | BOOL | FALSE | This is the "Manipulated value signal down" output.  (Only in the case of step controllers or pulse controllers) |
| QBACKUP | 125.4 | BOOL | FALSE | - 0= No backup state (CPU in RUN) - 1= Backup state (CPU in STOP or has failed) |
| QID | 125.5 | BOOL | FALSE | QID = TRUE indicates that an identification is running (not that it is enabled). On completion of the identification, the identification result can be read out from the IDSTATUS parameter of the instruction CH_DIAG_455. |
| QMAN_FC | 125.6 | BOOL | FALSE | The controller is a master controller that is adjusted by the manual mode of a slave controller to its process value or its I-action is stopped, because the setpoint or manipulated value of the slave controller lies in the limit. |
| RET_VALU | 126.0 | WORD | 0 | RET_VALU contains the return value RET_VAL of the RD_REC and WR_REC instructions. RET_VALU can be evaluated when QMOD_F reports an error. |

---

**See also**

[Input parameters DB 101 to 116 (S7-300, S7-400)](#input-parameters-db-101-to-116-s7-300-s7-400)
  
[In/out parameters DB 101 to 116 (S7-300, S7-400)](#inout-parameters-db-101-to-116-s7-300-s7-400)

### In/out parameters DB 101 to 116 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| 1) Operating parameters |  |  |  |  |
| SP_INT | 128.0 | REAL | 0.0 | The in/out parameter "Internal setpoint" is used to specify a setpoint by means of operating and monitoring functions. |
| SP_OP<sup>1)</sup> | 132.0 | REAL | 0.0 | The "Commissioning" dialog can access the in/out parameter "Setpoint operation". If the SP_OP_ON bit is set, the "Setpoint operation" value is applied as the setpoint. |
| LMN_OP<sup>1)</sup> | 136.0 | REAL | 0.0 | The "Commissioning" dialog can access the in/out parameter "Manipulated value operation". If the LMNOP_ON bit is set, the "Manipulated value operation" value is applied as the manipulated value.  Values from -100 to 100 % are permitted. |
| SP_OP_ON<sup>1)</sup> | 140.0 | BOOL | FALSE | The "Commissioning" dialog can access the in/out parameter "Enable setpoint operation". If the bit is set, the value SP_OP is applied as setpoint. |
| LMNOP_ON<sup>1)</sup> | 140.1 | BOOL | FALSE | The "Commissioning" dialog can access the in/out parameter "Enable manipulated value operation". If the bit is set, the value LMN_OP is applied as manipulated value. |
| LOAD_PAR | 140.2 | BOOL | FALSE | If the in/out parameter "Load control parameters to FM 455" is set, the control parameters are loaded into the module and the in/out parameter is reset. |
| LOAD_OP | 140.3 | BOOL | FALSE | If the in/out parameter "Load operating parameters to FM 455" is set, the operating parameters are loaded into the module and the in/out parameter is reset. |

> **Note**
>
> The EEPROM of the module could become damaged by too frequent write operations. To prevent this, the module delays another write process by 30 minutes after writing of the EEPROM.

---

**See also**

[Input parameters DB 101 to 116 (S7-300, S7-400)](#input-parameters-db-101-to-116-s7-300-s7-400)
  
[Output parameters DB 101 to 116 (S7-300, S7-400)](#output-parameters-db-101-to-116-s7-300-s7-400)
