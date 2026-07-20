---
title: "FM 355 PID Control (S7-300, S7-400)"
package: ProgFBFM355enUS
topics: 41
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# FM 355 PID Control (S7-300, S7-400)

This section contains information on the following topics:

- [PID_FM (S7-300, S7-400)](#pid_fm-s7-300-s7-400)
- [FUZ_355 (S7-300, S7-400)](#fuz_355-s7-300-s7-400)
- [FORCE355 (S7-300, S7-400)](#force355-s7-300-s7-400)
- [READ_355 (S7-300, S7-400)](#read_355-s7-300-s7-400)
- [CH_DIAG (S7-300, S7-400)](#ch_diag-s7-300-s7-400)
- [PID_PAR (S7-300, S7-400)](#pid_par-s7-300-s7-400)
- [CJ_T_PAR (S7-300, S7-400)](#cj_t_par-s7-300-s7-400)
- [DB for HMI (S7-300, S7-400)](#db-for-hmi-s7-300-s7-400)

## PID_FM (S7-300, S7-400)

This section contains information on the following topics:

- [Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
- [Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
- [Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
- [Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
- [In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
- [Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)

### Description PID_FM  (S7-300, S7-400)

During operation, the instruction PID_FM is used to:

- Transfer operating parameters to FM 355
- Transfer controlller parameters to FM 355
- Read process values from FM 355

Operating parameters are all in/out parameters that lie between the op_par and cont_par parameters in the instance data block of the instruction.

Controller parameters are all in/out parameters that are located after the cont_par parameter in the instance data block of the instruction.

Process values are all output parameters of the instruction after the out_par parameter.

The required data are stored in an instance DB on the CPU. You need one instance DB for each controller channel used. All the in/out parameters are set to FALSE after an instance DB has been created.

#### Call

PID_FM is normally called in the cyclic interrupt OB 35 and requires an initialization routine that is started by setting the parameter COM_RST = TRUE in the start-up of the CPU. A calling of the instruction in the start-up OB is possible, but not necessary. After the initialization routine, PID_FM sets the parameter COM_RST to FALSE. If FM 355 is used in distributed I/Os, this can take a few call cycles.

PID_FM has to be called in the same OB as all the other instructions that access the same FM 355.

If you call the instruction PID_FM as a multiple instance DB, no commissioning interface is available. In this case you must commission the FM 355 via a watch table.

#### Start-up

During CPU start-up and during CPU STOP-RUN transition, the parameters on the FM 355 are overwritten with the parameters from the SDB of the CPU.

#### Responses in the event of an error

The RET_VALU output parameter contains the 2nd and 3rd bytes of the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated if the READ_VAR and LOAD_PAR parameters are not reset.

When the instruction PID_FM is called, an I/O access error can occur if the FM 355 is not plugged or is not supplied with voltage. In this case the CPU goes into STOP, if no OB 122 is loaded in the CPU.

---

**See also**

[Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
  
[Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
  
[Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)
  
[Input parameters DB 101 to 104 (S7-300, S7-400)](#input-parameters-db-101-to-104-s7-300-s7-400)
  
[Changing parameters with the HMI (S7-300, S7-400)](Using%20FM%20355%20%28S7-300%2C%20S7-400%29.md#changing-parameters-with-the-hmi-s7-300-s7-400)
  
[Creating and supplying instance DBs (S7-300, S7-400)](Using%20FM%20355%20%28S7-300%2C%20S7-400%29.md#creating-and-supplying-instance-dbs-s7-300-s7-400)

### Mode of operation PID_FM  (S7-300, S7-400)

#### Effect of parameters LOAD_OP, READ_VAR and LOAD_PAR

In the initialization routine PID_FM reads the parameters from the system data and stores them in its instance DB. Instance DB and system data are synchronized.

The following table shows how the function of the instruction is influenced by the parameters LOAD_OP, READ_VAR and LOAD_PAR.

| Parameter | TRUE | FALSE |
| --- | --- | --- |
| LOAD_OP | Transfer operating parameters with the instructions WRREC and RDREC. | Transfer operating parameters via direct I/O access in muliplex mode. |
| READ_VAR is set to TRUE | READ_VAR is not changed |  |
| Longer run time | Shorter run time |  |
| The values are effective after a cycle of the CPU or FM. The longer cycle is decisive. | A maximum of 3 cycles of the CPU or PM are required until the values are effective. The longer cycle is decisive |  |
| READ_VAR | Transfer process values with the instructions WRREC and RDREC. | Process values are transferred via direct I/O accesses in multplex mode. |
| Longer processing time | Shorter processing time |  |
| All parameters are read from FM 355 | The following parameters are **not** read from FM 355  - SP (setpoint from the FM) - ER (error signal) - DISV (disturbance variable) - LMN_A - LMN_B |  |
| Following parameters are updated at **every**  call of the instruction.  - PV (process value) - LMN (manipulated value) - The binary displays | Following parameters are updated at every **fourth** call of the instruction.  - PV (process value) - LMN (manipulated value) - The binary displays |  |
| At the start-up of the CPU, the following values are applied from the FM 355 to the PID_FM.  - SP_OP - LMN_OP - SP_OP_ON - LMNOP_ON   If these values were changed on the CPU, they are overwritten with the values from the FM 355 at the next start-up of the CPU | At the start-up of the CPU, the following values are read from the instruction, not from the FM:  - SP_OP - LMN_OP - SP_OP_ON - LMNOP_ON |  |
| LOAD_PAR | All controller parameters are downloaded from the CPU to the FM 355. This is practical if the controller parameters are to be changed depending on process states. | No transfer of the controller parameters |

After data transfer as been completed the parameters LOAD_OP, READ_VAR and LOAD_PAR are reset to FALSE.

#### Use in distributed I/O

When the FM 355 is used in distributed I/O, the data transfer and the resetting of the parameters can take a few call cycles.

#### Special features during transfer in multiplex mode

Multiplexing of the data to be transferred during access to the FM 355 via direct I/O accesses is controlled via the PID_FM. This multiplex controlling via PID_FM does not function if two instances of the instruction PID_FM access the same channel number of a module. This results in incorrect parameters in the FM 355 (for example, setpoint and manual manipulated value) and incorrect displays at the output parameters of the instruction PID_FM.

#### Saving the Parameters in EEPROM

During program controlled re-configuring (LOAD_PAR, LOAD_OP) of the controller module by the instruction PID_FM, its run time is extended. The new parameters are always immediately effective. Controller parameters and the operating parameter SP_ER are stored additionally in a nonvolatile memory (EEPROM). After each saving of the parameters in the EEPROM, a renewed saving is delayed by 30 minutes, since the life of the EEPROM is limited by the number of write processes. It is possible to save the new parameter in the EEPROM as soon as the power supply returns. The selection of the parameters determines whether the reconfiguration of the controller module by the instruction PID_FM is executed without bumps.

#### Processing times PID_FM

| Boundary conditions |  |  | Processing time in |  |
| --- | --- | --- | --- | --- |
| READ_VAR | LOAD_OP | LOAD_PAR | CPU 314 | CPU 414-2DP |
| FALSE | FALSE | FALSE | 0.65 ms | 0.077 ms |
| TRUE | FALSE | FALSE | 2.85 ms | 2.36 ms |
| TRUE | TRUE | FALSE | 4.56 ms | 4.48 ms |
| FALSE | FALSE | TRUE | 3.75 ms | 2.59 ms |
| TRUE | FALSE | TRUE | 5.95 ms | 5.15 ms |
| TRUE | TRUE | TRUE | 7.66 ms | 7.1 ms |

---

**See also**

[Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
  
[Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
  
[Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)
  
[Input parameters DB 101 to 104 (S7-300, S7-400)](#input-parameters-db-101-to-104-s7-300-s7-400)
  
[Changing parameters with the HMI (S7-300, S7-400)](Using%20FM%20355%20%28S7-300%2C%20S7-400%29.md#changing-parameters-with-the-hmi-s7-300-s7-400)

### Input parameters PID_FM (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CHANNEL | 2.0 | INT | 1 | The number of the controller channel to which the instance DB îs referenced is configured at the "Channel number" input.   Values of 1 to 4 are permissible. |
| PHASE | 4.0 | INT | 0 | The parameter PHASE can be interconnected with the output parameter PHASE of the instructions TUN_EC or TUN_ES (PID Self-Tuner). The phase state of the PID Self-Tuner can then be displayed in plain text in the "Commissioning" dialog. This parameter is not relevant for the OP. |

---

**See also**

[Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
  
[Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
  
[Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)
  
[Input parameters DB 101 to 104 (S7-300, S7-400)](#input-parameters-db-101-to-104-s7-300-s7-400)

### Output parameters PID_FM (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 6.0 | WORD | 0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated when an error is reported via QMOD_F. |
| out_par | 8.0 | WORD | W#16#3130 | The out_par parameter may not be modified by users. It marks the start of the output parameter that is read by the module if READ_VAR = TRUE is set. |
| SP | 10.0 | REAL | 0.0 | The setpoint that is currently in effect is available at the "Setpoint" output. |
| PV | 14.0 | REAL | 0.0 | The process value that becomes effective is issued on the "Process value" output. |
| ER | 18.0 | REAL | 0.0 | The control deviation that becomes effective is issued on the "Control deviation" output. |
| DISV | 22.0 | REAL | 0.0 | The interference that becomes effective is issued on the "Interference" output.  Values from -100 to 100 % are permitted. |
| LMN | 26.0 | REAL | 0.0 | The manipulated value that becomes effective is issued on the "Manipulated value" output. Step controllers without analog position feedback output the unlimited P- + D-action at the LMN parameter.  Values from -100 to 100 % are permitted. |
| LMN_A | 30.0 | REAL | 0.0 | At the output "Manipulated value A of the split range function / position feedback", continuous controllers display the manipulated value A and step controllers with analog position feedback display the position feedback.  The output LMN_A can only be used for an approximate display of a corresponding simulated manipulated variable. The start value LMNRSVAL of the simulated position feedback has to be configured accordingly and becomes effective when LMNRS_ON is set.  Values from -100 to 100 % are permitted. |
| LMN_B | 34.0 | REAL | 0.0 | Continuous controllers display the manipulated value B of the split-range function at the output “manipulated value B of the split-range function”.  Values from -100 to 100 % are permitted. |
| QH_ALM | 38.0 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of H_ALM limit is reported at the output "High limit alarm triggered". |
| QH_WRN | 38.1 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of H_WRN limit is reported at the output "High limit warning triggered". |
| QL_WRN | 38.2 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of the L_WRN limit is reported at output "Low limit warning triggered". |
| QL_ALM | 38.3 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of the L_ALM limit is reported at output "Low limit alarm triggered". |
| QLMN_HLM | 38.4 | BOOL | FALSE | The manipulated value is always limited to a high and a low limit. Violation of the high limit is reported at output "High limit of manipulated value triggered".  (Does not apply to step controllers without analog position feedback) |
| QLMN_LLM | 38.5 | BOOL | FALSE | The manipulated value is always limited to a high and a low limit. Violation of the low limit is reported at output "Low limit of manipulated value triggered".  (Does not apply to step controllers without analog position feedback) |
| QPARA_F | 38.6 | BOOL | FALSE | The module checks the validity of the parameters. A parameter assignment error is displayed at the "Parameter assignment error" output. These parameter assignment errors can also be read out in the module's "Online &amp; Diagnostics" dialog. |
| QCH_F | 38.7 | BOOL | FALSE | The "Channel error" output is set if the controller channel cannot provide valid results. A channel error (for example, wire break) is also set if QPARA_F = 1 or QMOD_F = 1. If QCH_F = TRUE, then the precise error information in the diagnostic data record DS1 of the module is read out. |
| QUPRLM | 39.0 | BOOL | FALSE | The setpoint is limited to a positive and negative slew rate. If the output "Limit of positive setpoint slew rate triggered" is set, the positive setpoint slew rate is limited. |
| QDNRLM | 39.1 | BOOL | FALSE | The setpoint is limited to a positive and negative slew rate. If the output "Limit of negative setpoint slew rate triggered" is set, the setpoint fall is limited. |
| QSP_HLM | 39.2 | BOOL | FALSE | The setpoint is always limited to a high and a low limit. The output "High limit of setpoint value triggered" indicates that the high limit has been exceeded. |
| QSP_LLM | 39.3 | BOOL | FALSE | The setpoint is always limited to a high and a low limit. Violation of the low limit is reported at output "Setpoint low limit triggered". |
| QLMNUP | 39.4 | BOOL | FALSE | This is the "Manipulated value signal up" output.  (Only in the case of step controllers or pulse controllers) |
| QLMNDN | 39.5 | BOOL | FALSE | This is the "Manipulated value signal down" output.  (Only in the case of step controllers or pulse controllers) |
| QID | 39.6 | BOOL | FALSE | QID = TRUE indicates that an identification is running (not that it is enabled). On completion of the identification, the identification result can be read out from the IDSTATUS parameter of the instruction CH_DIAG. |
| QSPOPON | 40.0 | BOOL | FALSE | Output "Setpoint operation on" indicates whether the operator controls the setpoint using the instruction TUN_EC or TUN_ES. If the bit is set, the value SP_OP is applied as setpoint. |
| QLMNSAFE | 40.1 | BOOL | FALSE | If the output "Safety mode" is set, the safety manipulated value is output as the manipulated value. |
| QLMNOPON | 40.2 | BOOL | FALSE | Output "Setpoint operation on" indicates whether the operator controls the manipulated value using the instruction TUN_EC or TUN_ES. If the bit is set, the value LMN_OP is applied as manipulated value. |
| QLMNTRK | 40.3 | BOOL | FALSE | The output "Follow-up mode" indicates if the manipulated value is being adjusted via an analog input. |
| QLMN_RE | 40.4 | BOOL | FALSE | The output "Manual = 1; Automatic = 0" indicates whether or not the manipulated value is set on the external manipulated value LMN_RE (manual = 1). |
| QLMNR_HS | 40.5 | BOOL | FALSE | The output "High endstop signal of position feedback" indicates if the control valve is at its high endstop. QLMNR_HS = TRUE means: The control valve is at high endstop.  (For step controllers only) |
| QLMNR_LS | 40.6 | BOOL | FALSE | The output "Low endstop signal of position feedback" indicates whether the control valve is at its low endstop. QLMNR_LS = TRUE means: The control valve is at its low endstop.  (For step controllers only) |
| QLMNR_ON | 40.7 | BOOL | FALSE | Output "Position feedback enabled" indicates the set operating mode "Step controller with position feedback" or "Step controller without position feedback". |
| QFUZZY | 41.0 | BOOL | FALSE | If the output parameter is QFUZZY =1, the controller operates with the fuzzy algorithm. |
| QSPLEPV | 41.1 | BOOL | FALSE | The output "Display of FUZZY controller: Setpoint &lt; process value" is set when the fuzzy controller is switched on, if the setpoint is less than the effective process value. |
| QSPR | 41.2 | BOOL | FALSE | If the output "Split-range operation" is set, the continuous controller is operating in split-range mode. |
| QMAN_FC | 41.4 | BOOL | FALSE | The output "QMAN_FC" is set in the following two cases:  The slave controller is in manual mode and the master controller is followed up to the process value of the slave controller.  The I-action of the master controller is stopped because the setpoint or manipulated variable of the slave controller is limited or because the slave controller is in manual mode. |
| QPARABUB | 41.7 | BOOL | FALSE | This parameter is set by the FM if the operating parameters are changed via the OP. If READ_VAR = TRUE and if this display is set by the FM, the instruction PID_FM reads out the parameters SP_OP_ON, LMNOP_ON, SP_OP and LMN_OP from the FM and saves them in the instance DB. The instruction thus applies over the operating state of the FM. After the reading process the parameter is set to FALSE. |
| QMOD_F | 42.0 | BOOL | FALSE | The instruction checks that the reading and writing of a data record has been completed. Output "Module error" is set if errors are found. The error cause can be: An incorrect module address at parameter MOD_ADDR, or an incorrect channel number at parameter CHANNEL, or a faulty module. |

---

**See also**

[Input parameters DB 101 to 104 (S7-300, S7-400)](#input-parameters-db-101-to-104-s7-300-s7-400)

### In/out parameters PID_FM (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| <sup>1) </sup>Default values of the module after the first start-up of the PID_FM with COM_RST = TRUE |  |  |  |  |
| COM_RST | 44.0 | BOOL | FALSE | If the parameter COM_RST = TRUE, the instruction PID_FM executes an initialization routine. In doing so the controller parameters (these are all the parameters after cont_par) are read from the FM and stored in the instance DB. In addition, the parameters MOD_ADDR and CHANNEL are checked for validity. After the initialization routine the parameter is set to FALSE. |
| LOAD_OP | 44.1 | BOOL | FALSE | If the in/out parameter "Load operating parameters to FM 355" is set, the operating parameters are loaded into the module and the in/out parameter is reset. |
| READ_VAR | 44.2 | BOOL | FALSE | If the in/out parameter "Read tags from FM 355" is set, the output parameters are read from the module and the in/out parameter is reset. |
| LOAD_PAR | 44.3 | BOOL | FALSE | If the in/out parameter "Load control parameters to FM 355" is set, the control parameters are loaded into the module and the in/out parameter is reset. |
| op_par | 46.0 | WORD | W#16#3130<sup>1)</sup> | The op_par parameter may not be modified by users. It identifies the start of the operating parameters that are transferred to the module, if LOAD_OP = TRUE is set. The end of the operating parameters is identified by cont_par. |
| SP_RE | 48.0 | REAL | 0.0 | An external setpoint is interconnected with the controller at the "External setpoint" input. |
| LMN_RE | 52.0 | REAL | 0.0 | An external manipulated value is interconnected to the controller at the input "External manipulated value".  Values from -100.0 to 100.0 (%) are permitted. |
| SP_OP_ON | 56.0 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the in/out parameter "Enable setpoint operation". If the bit is set, the value SP_OP is applied as setpoint. |
| SAFE_ON | 56.1 | BOOL | FALSE | If the "Adopt safety position" input is set, a safety value is applied as manipulated value.   Note: The actuating signal processing via LMNDN_OP, LMNUP_OP and LMNSOPON on a step controller is of higher priority than the safety manipulated value. |
| LMNOP_ON | 56.2 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the in/out parameter "Enable manipulated value operation". If the bit is set, the value LMN_OP is applied as manipulated value. |
| LMNTRKON | 56.3 | BOOL | FALSE | If input "Follow-up (LMN via AI)" is set, the manipulated value is adjusted to an analog input (AI).  (Does not apply to step controllers without analog position feedback) |
| LMN_REON | 56.4 | BOOL | FALSE | If input "Enable external manipulated value" is set, the external manipulated value LMN_RE is set as the manipulated value. |
| LMNRHSRE | 56.5 | BOOL | FALSE | The signal "Control valve at high endstop" is interconnected at the "High endstop signal of position feedback" input. LMNRHSRE = TRUE means: The control valve is located at the high endstop.  (Only in the case of step controllers) |
| LMNRLSRE | 56.6 | BOOL | FALSE | The signal "Control valve at low endstop" is interconnected at the "Low endstop signal of position feedback" input. LMNRLSRE = TRUE means: The control valve is located at the low endstop.  (Only in the case of step controllers) |
| LMNSOPON | 56.7 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the input "Enable manipulated value operation". If the bit is set, the signals LMNUP_OP and LMNDN_OP are applied as manipulated value signals.  (Only in the case of step controllers) |
| LMNUP_OP | 57.0 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the input "Manipulated value signal up". If LMNSOPON is set, the value at input "Manipulated value signal up operation" is set as the manipulated value signal.  (Only in the case of step controllers) |
| LMNDN_OP | 57.1 | BOOL | FALSE | The instructions of PID Self-Tuner have access to the input "Manipulated value signal down operation". If LMNSOPON is set, the value at input "Manipulated value signal down operation" is set as the manipulated value signal.  (Only in the case of step controllers) |
| LMNRS_ON | 57.3 | BOOL | FALSE | You can simulate no position feedback if this is not available. The function is enabled by setting the "Enable simulation of position feedback" input The instructions of PID Self-Tuner have access to this parameter as well since at least one simulated manipulated value is required for optimization if a step controller was configured without position feedback. The simulated value is displayed at parameter LMN_A. When the simulation is enabled the value of the parameter LMNRSVAL is set as the starting value.   CAUTION: Offset between the simulation value and real position feedback increases over the time.  (Only for step controllers without analog position feedback) |
| FUZID_ON | 57.4 | BOOL | FALSE | The identification of the fuzzy algorithm is enabled at the "Enable fuzzy identification" input. |
| SP_OP | 58.0 | REAL | 0.0 | The instructions of PID Self-Tuner have access to the in/out parameter "Setpoint operation". If the SP_OP_ON bit is set, the "Setpoint operation" value is applied as the setpoint. |
| LMN_OP | 62.0 | REAL | 0.0 | The instructions of PID Self-Tuner have access to the in/out parameter "Manipulated value operation". If the LMNOP_ON bit is set, the "Manipulated value operation" value is applied as the manipulated value.  Values from -100.0 to 100.0 (%) are permitted |
| LMNRSVAL | 66.0 | REAL | 0.0 | The instructions of PID Self-Tuner have access to input "Starting value of simulated position feedback". The start value of the simulation is entered at the parameter.  (Only for step controllers without analog position feedback)   Values from -100.0 to 100.0 (%) are permitted |
| cont_par | 70.0 | WORD | W#16#3130 <sup>1)</sup> | The cont_par parameter may not be modified by users. It indicates the start of the controller parameters which are read from the FM and stored in the instance DB, if COM_RST = TRUE is, and which are transferred to the FM when LOAD_PAR = TRUE is set. The end of the controller parameter is the end of the instance DB. |
| P_SEL | 72.0 | BOOL | TRUE <sup>1)</sup> | In the PID algorithm, the PID parts can be switched on and off individually. The proportional action is enabled when the "P-action on" input is set. |
| PFDB_SEL | 72.1 | BOOL | FALSE   <sup>1)</sup> | In the PID algorithm, the P- and D-actions can be included in the feedback loop. The proportional action is located in the feedback loop when the input "Enable P-action in feedback loop" is set. |
| MONERSEL | 72.2 | BOOL | FALSE   <sup>1)</sup> | The controller has a limit indicator that can be applied either for the process value or the control deviation. If the input "Monitoring: Process value = 0, control deviation = 1" is set, the control deviation will be monitored. |
| D_EL_SEL | 74.0 | INT | 0 <sup>1)</sup> | The D-action element in the PID algorithm can be positioned at a separate input. This is selected at the input "D-action element input".  0: Control deviation  1 to 4: Analog input 1 to 4  17: Negative process value, D-action in the feedback |
| SP_HLM | 76.0 | REAL | 100.0   <sup>1)</sup> | The setpoint is always limited to a high and a low limit. The "Setpoint high limit" input specifies the high limit.   SP_HLM &gt; SP_LLM |
| SP_LLM | 80.0 | REAL | 0.0   <sup>1)</sup> | The setpoint is always limited to a high and a low limit. The "Setpoint low limit" input specifies the low limit.  SP_LLM &lt; SP_HLM |
| H_ALM | 84.0 | REAL | 100.0   <sup>1)</sup> | You can assign parameters for four limits for monitoring the process value or the control deviation. The "High limit interrupt" input specifies the highest limit.   H_ALM &gt; H_WRN |
| H_WRN | 88.0 | REAL | 90.0   <sup>1)</sup> | You can assign parameters for four limits for monitoring the process value or the control deviation. The "High limit warning" input specifies the second highest limit.  Values from H_ALM to L_WRN are permitted. |
| L_WRN | 92.0 | REAL | 10.0   <sup>1)</sup> | You can assign parameters for four limits for monitoring the process value or the control deviation. The "Low limit warning" input specifies the second lowest limit.  Values from H_WRN to L_ALM are permitted. |
| L_ALM | 96.0 | REAL | 0.0   <sup>1)</sup> | You can assign parameters for four limits for monitoring the process value or the control deviation. The "Low limit alarm" input specifies the lowest limit.  L_ALM &lt; L_WRN |
| HYS | 100.0 | REAL | 1.0   <sup>1)</sup> | To prevent flickering of the monitoring displays, a hysteresis can be configured at the "Hysteresis" input.  HYS ≥ 0.0 |
| DEADB_W | 104.0 | REAL | 0.0   <sup>1)</sup> | A deadband is applied to the control deviation. The "Deadband width" input determines the size of the deadband.   DEADB_W ≥ 0.0 |
| GAIN | 108.0 | REAL | 1.0   <sup>1)</sup> | The "Proportional gain" input specifies controller amplification. |
| TI | 112.0 | REAL | 3000.0   <sup>1)</sup> | The "Integration time" input determines the time  response of the integral action. If TI = 0, the integral action is disabled  TI = 0.0 or TI ≥ 0.5 |
| TD | 116.0 | REAL | 0.0   <sup>1)</sup> | The "Derivative-action time" input determines the time response of the differentiator. If TD = 0, the derivative action is disabled.  TD = 0.0 or TD ≥ 1.0 |
| TM_LAG | 120.0 | REAL | 5.0   <sup>1)</sup> | The algorithm of the derivative action contains a delay for which parameters can be assigned at the input "Time lag of the derivative action".   TM_LAG ≥ 0.5 |
| LMN_SAFE | 124.0 | REAL | 0.0   <sup>1)</sup> | For the manipulated value, a safety value can be configured at the "Safety manipulated value" input.  Values from -100.0 to 100.0 (%) are permitted. |
| LMN_HLM | 128.0 | REAL | 100.0   <sup>1)</sup> | The manipulated value is always limited to a high and a low limit. The "Manipulated value high limit" input specifies the high limit.  (Does not apply to step controllers without analog position feedback)  Values from LMN_LLM to 100.0 (%) are permitted. |
| LMN_LLM | 132.0 | REAL | 0.0   <sup>1)</sup> | The manipulated value is always limited to a high and a low limit. The "Manipulated value low limit" input specifies the low limit.  (Does not apply to step controllers without analog position feedback)  Values from -100.0 to LMN_HLM (%) are permitted. |
| MTR_TM | 136.0 | REAL | 60.0   <sup>1)</sup> | The runtime from endstop to endstop of the control valve is entered at the "Motor actuating time" parameter.   (Only in the case of step controllers)  Values of MTR_TM ≥ 0.001 are permitted. |
| PULSE_TM | 140.0 | REAL | 0.2   <sup>1)</sup> | A minimum pulse time can be configured at the "Minimum pulse time" parameter.   (Applies to step controllers or pulse controllers only)  Values of PULSE_TM ≥ 0.0 are permitted. |
| BREAK_TM | 144.0 | REAL | 0.2   <sup>1)</sup> | A minimum pulse break duration can be assigned with the parameter "Minimum break time."   (Applies to step controllers or pulse controllers only)  Values of BREAK_TM ≥ 0.0 are permitted. |

> **Note**
>
> If LOAD_PAR = TRUE is set, all the control parameters are loaded permanently to the EEPROM of the FM 355.
>
> If LOAD_OP = TRUE, only the setpoint SP_RE of the operating parameters is loaded permanently to the EEPROM of the FM 355. All the other operating parameters are assigned the values 0 or FALSE as default during the startup of FM 355
>
> The EEPROM of the module could become damaged by too frequent write operations. To prevent this, the module delays another write process by 30 minutes after writing of the EEPROM.

---

**See also**

[Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
  
[Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
  
[Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)
  
[Input parameters DB 101 to 104 (S7-300, S7-400)](#input-parameters-db-101-to-104-s7-300-s7-400)

### Block diagram PID_FM (S7-300, S7-400)

#### Overview

The following figures show at which points the parameters of the instruction PID_FM act.

The parameters are effective with three-component controllers, ration/blending controllers, and fixed setpoint or cascade controllers. This also applies for the parameters that exist equally at continuous controllers, at controllers with a pulse output as well as at step controllers. Therefore, not all block diagrams are depicted and not all parameter are marked in all figures.

However, the parameters of the instruction PID_FM are contained in all the figures – with the exception of the parameters MOD_ADDR, CHANNEL, QMOD_F, QPARA_F, QCH_F, QLMNR_ON, RET_VALU, COM_RST, LOAD_PAR, READ_VAR, LOAD_OP.

#### Action of the input parameters

Error signal generation with fixed setpoint or cascade controllers

![Action of the input parameters](images/18118198667_DV_resource.Stream@PNG-en-US.png)

Block diagram of the control algorithm

![Action of the input parameters](images/18118705675_DV_resource.Stream@PNG-en-US.png)

Controller output of the continuous controller

![Action of the input parameters](images/18118868363_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (pulse controller operating mode)

![Action of the input parameters](images/18118901771_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (step controller operating mode with position feedback)

![Action of the input parameters](images/18118922379_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (step controller operating mode without position feedback)

![Action of the input parameters](images/18118726283_DV_resource.Stream@PNG-en-US.png)

#### Generating output parameters

The following figures show at which points in the module the output parameters of the instruction PID_FMare generated.

Error signal generation with fixed setpoint or cascade controllers

![Generating output parameters](images/24541655947_DV_resource.Stream@PNG-en-US.png)

Block diagram of the control algorithm

![Generating output parameters](images/18118767499_DV_resource.Stream@PNG-en-US.png)

Controller output of the continuous controller

![Generating output parameters](images/18118788107_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (pulse controller operating mode)

![Generating output parameters](images/24541485579_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (step controller operating mode with position feedback)

![Generating output parameters](images/24541583115_DV_resource.Stream@PNG-en-US.png)

Controller output of the step controller (step controller operating mode without position feedback)

![Generating output parameters](images/18118847755_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
  
[Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
  
[Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
  
[Input parameters DB 101 to 104 (S7-300, S7-400)](#input-parameters-db-101-to-104-s7-300-s7-400)

## FUZ_355 (S7-300, S7-400)

This section contains information on the following topics:

- [Description FUZ_355 (S7-300, S7-400)](#description-fuz_355-s7-300-s7-400)
- [Input parameters FUZ_355 (S7-300, S7-400)](#input-parameters-fuz_355-s7-300-s7-400)
- [Output parameters FUZ_355 (S7-300, S7-400)](#output-parameters-fuz_355-s7-300-s7-400)
- [In/out parameters FUZ_355 (S7-300, S7-400)](#inout-parameters-fuz_355-s7-300-s7-400)

### Description FUZ_355 (S7-300, S7-400)

The instruction FUZ_355 is used to read out and write the controller parameters of the fuzzy temperature controller from FM 355.

This function is suitable for the following applications:

- Transferring the controller parameters of the FM 355 that have been established by identification after the module replacement
- Adapting the FM 355 to different processes

  > **Note**
  >
  > It is not permitted to modify the parameters that have been established by the FM 355 by means of an identification as they have been optimized for the process.

#### Mode of operation

The parameters READ_PAR and LOAD_PAR are used to control the mode of operation of the instruction FUZ_355

If READ_PAR = TRUE, FUZ_355 reads the parameters of all the temperature controllers of the FM 355 and stores them in the instance DB. After the temperature controller parameters have been successfully read out, FUZ_355 sets the parameter READ_PAR to FALSE.

If LOAD_PAR = TRUE, FUZ_355 writes the parameters of all the temperature controllers of the FM 355 from the instance DB to the FM 355. After the parameters have been successfully transferred, FUZ_355 sets the parameter LOAD_PAR to FALSE.

#### Call

FUZ_355 requires no initialization routine.

If the FM 355 is used in distributed I/Os, it may take a few call cycles until the parameters READ_PAR and LOAD_PAR are reset to FALSE. Therefore, call the instruction FUZ_355 conditionally, as long as READ_PAR = TRUE or LOAD_PAR = TRUE.

FUZ_355 has to be called in the same OB as all the other instructions that access the same FM 355.

#### Start-up

During the start-up of the CPU you should set the LOAD_PAR parameter of the FUZ_355 instruction and then call the block in the cyclic program, provided LOAD_PAR = TRUE.

---

**See also**

[Input parameters FUZ_355 (S7-300, S7-400)](#input-parameters-fuz_355-s7-300-s7-400)
  
[Output parameters FUZ_355 (S7-300, S7-400)](#output-parameters-fuz_355-s7-300-s7-400)
  
[In/out parameters FUZ_355 (S7-300, S7-400)](#inout-parameters-fuz_355-s7-300-s7-400)

### Input parameters FUZ_355 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |

---

**See also**

[Description FUZ_355 (S7-300, S7-400)](#description-fuz_355-s7-300-s7-400)
  
[Output parameters FUZ_355 (S7-300, S7-400)](#output-parameters-fuz_355-s7-300-s7-400)
  
[In/out parameters FUZ_355 (S7-300, S7-400)](#inout-parameters-fuz_355-s7-300-s7-400)

### Output parameters FUZ_355 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 2.0 | WORD | 0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated when an error is reported via QMOD_F. |
| PARAFFUZ | 4.0 | WORD | 0 | A parameter assignment error created by the the instruction FUZ_355 is displayed at the parameter PARAFFUZ as follows:   High byte of PARAFFUZ = 01: There is a parameter assignment error..   High byte of PARAFFUZ = 00: There is no parameter assignment error.   The low byte contains the offset of the parameter that caused the parameter assignment error, calculated from the static variable FUZ_PAR[1].  For instance, PARAFFUZ = W#16#0104 means that the second parameter is faulty. |

### In/out parameters FUZ_355 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| READ_PAR | 6.0 | BOOL | FALSE | If the READ_PAR parameter is set, the fuzzy parameters are read out from the module and stored in the static variables of the instance DB. |
| LOAD_PAR | 6.1 | BOOL | FALSE | If the LOAD_PAR parameter is set, the fuzzy parameters are read out from the static variables of the instance DB module and transferred to the module. |

---

**See also**

[Description FUZ_355 (S7-300, S7-400)](#description-fuz_355-s7-300-s7-400)
  
[Input parameters FUZ_355 (S7-300, S7-400)](#input-parameters-fuz_355-s7-300-s7-400)
  
[Output parameters FUZ_355 (S7-300, S7-400)](#output-parameters-fuz_355-s7-300-s7-400)

## FORCE355 (S7-300, S7-400)

This section contains information on the following topics:

- [Description FORCE355 (S7-300, S7-400)](#description-force355-s7-300-s7-400)
- [Input parameters FORCE355 (S7-300, S7-400)](#input-parameters-force355-s7-300-s7-400)
- [Output parameters FORCE355 (S7-300, S7-400)](#output-parameters-force355-s7-300-s7-400)

### Description FORCE355 (S7-300, S7-400)

The instruction FORCE355 is used to simulate (force) the analog and digital input values to support the start-up.

#### Simulating Digital Values

The simulation of the values for the digital inputs 1 to 8 is enabled via the switches S_DION[ i ], where 1 ≤ i ≤ 8. You specify the simulation values at the parameters DI_SIM[ i ]. If S_DION[i] = TRUE, the value DI_SIM[i] is used Instead of the value of digital input i of the module,. LEDs I1 to I8 also always display the state of the corresponding digital input during simulation.

#### Simulating Analog Values

The simulation of the analog values for the channels one to 4 is enabled via the switches S_AION[ i ] or S_PVON[ i ], where 1 ≤ i ≤ 4.

You specify the simulation values for the channels one to 4 via the parameter PV_SIM[ i ].

You can have the simulation values become effective at two points:

- S_AION[ i ] = TRUE (1 ≤ i ≤ 4)

  The value PV_SIM[ i ] is used instead of the value of analog input i of the module.
- S_PVON[ i ] = TRUE (1 ≤ i ≤ 4)

  The value PV_SIM[ i ] is used instead of the conditioned value of analog input i of the module.

The following figure shows at which point the simulated analog value is effective.

![Simulating Analog Values](images/18135808267_DV_resource.Stream@PNG-en-US.png)

Enabling and specification of the simulation values (forcing) is not carried out via the parameter assignment interface. This is why the relevant switches and connecting lines are drawn as dotted lines.

#### Call

FORCE355 does not require any initialization routine and is normally called cyclically.

FORCE355 has to be called in the same OB as all the other instructions that access the same FM 355.

#### Startup characteristics

When FM 355 restarts after power off, the simulation switches on the FM 355 are again set to FALSE.

---

**See also**

[Input parameters FORCE355 (S7-300, S7-400)](#input-parameters-force355-s7-300-s7-400)
  
[Output parameters FORCE355 (S7-300, S7-400)](#output-parameters-force355-s7-300-s7-400)

### Input parameters FORCE355 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| S_AION | 0.0 | ARRAY [1..4] of BOOL | FALSE | If, for example, the S_AION[1] switch is set to TRUE, the value PV_SIM[1] is used instead of the analog input value 1 of the module. |
| S_PVON | 2.0 | ARRAY [1..4] of BOOL | FALSE | If, for example, the S_PVON[1] switch is set to TRUE, the value PV_SIM[1] is used instead of the conditioned analog input value 1 of the module. |
| PV_SIM | 4.0 | ARRAY [1..4] of REAL | 0.0 | The simulation value for the analog input 1 is specified, for example, at input PV_SIM[1]. If S_PVON = TRUE, then the conditioned analog input value is specified here. If S_PVON = FALSE and S_AION = TRUE, then the analog input value, which is transformed into a conditioned value by means of the conditioning functions, is specified in mA or mV.  Permitted are 0.0 to 20.0 [mA], -1500 to +10000 [mV], or a technical range of values. |
| S_DION | 20.0 | ARRAY [1..8] of BOOL | FALSE | If, for example, the S_DION[1] switch is set to TRUE, the value DI_SIM[1] is used instead of the digital input value 1 of the module. |
| DI_SIM | 22.0 | ARRAY [1..8] of BOOL | FALSE | Simulation value for digital input |
| MOD_ADDR | 24.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |

---

**See also**

[Description FORCE355 (S7-300, S7-400)](#description-force355-s7-300-s7-400)
  
[Output parameters FORCE355 (S7-300, S7-400)](#output-parameters-force355-s7-300-s7-400)

### Output parameters FORCE355 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 26.0 | WORD |  | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated when an error is reported via QMOD_F. |

## READ_355 (S7-300, S7-400)

This section contains information on the following topics:

- [Description READ_355 (S7-300, S7-400)](#description-read_355-s7-300-s7-400)
- [Input parameters READ_355 (S7-300, S7-400)](#input-parameters-read_355-s7-300-s7-400)
- [Output parameters READ_355 (S7-300, S7-400)](#output-parameters-read_355-s7-300-s7-400)

### Description READ_355 (S7-300, S7-400)

The instruction READ_355 is used to read out the digital and analog input values to support the start-up.

The following values are displayed:

![Figure](images/18137300107_DV_resource.Stream@PNG-en-US.png)

#### Call

READ_355 does not require any initialization routine and is normally called cyclically.

READ_355 has to be called in the same OB as all the other instructions that access the same FM 355.

---

**See also**

[Input parameters READ_355 (S7-300, S7-400)](#input-parameters-read_355-s7-300-s7-400)
  
[Output parameters READ_355 (S7-300, S7-400)](#output-parameters-read_355-s7-300-s7-400)

### Input parameters READ_355 (S7-300, S7-400)

| Parameters | Address | Data type | Default setting | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |

---

**See also**

[Description READ_355 (S7-300, S7-400)](#description-read_355-s7-300-s7-400)
  
[Output parameters READ_355 (S7-300, S7-400)](#output-parameters-read_355-s7-300-s7-400)

### Output parameters READ_355 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| CJ_TEMP | 2.0 | REAL | 0.0 | At parameter CJ_TEMP the reference junction temperature measured at the reference point is expressed degrees C or in degrees F (depending on which temperature unit has been parameterized). If no "Thermocouple" sensor type was configured or if the configured reference junction temperature was selected at all the analog inputs, 0.0 is displayed at the CJ_TEMP parameter. |
| STAT_DI | 6.0 | ARRAY [1..8] of BOOL | FALSE | The actual states of digital inputs 1 to 8 are displayed at parameters STAT_DI[1] to STAT_DI[8], even if these are simulated. |
| DIAG[x].PV_PER | (channel number) x 8 | ARRAY [1..4] of STRUCT | 0.0 | The values of analog inputs one to four are displayed at parameters DIAG[1].PV_PER to DIAG[4].PV_PER in the unit mA or mV. If the simulation of the analog input value has been enabled via the instruction FORCE355, the simulated value will be shown. |
| DIAG[x].PV_PHY | (channel number) x 8 + 4 | ARRAY [1..4] of STRUCT | 0.0 | The conditioned analog input value one to four is displayed in physical unit at the parameters DIAG[1].PV_PHY to DIAG[4].PV_PHY If the simulation of the conditioned physical analog input value is enabled via the instruction FORCE355, the simulated value is displayed. |
| RET_VALU | 40.0 | WORD | 0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated when an error is reported via QMOD_F. |

## CH_DIAG (S7-300, S7-400)

This section contains information on the following topics:

- [Description CH_DIAG (S7-300, S7-400)](#description-ch_diag-s7-300-s7-400)
- [Input parameters CH_DIAG (S7-300, S7-400)](#input-parameters-ch_diag-s7-300-s7-400)
- [Output parameters CH_DIAG (S7-300, S7-400)](#output-parameters-ch_diag-s7-300-s7-400)
- [Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)
- [Block diagrams CH_DIAG (S7-300, S7-400)](#block-diagrams-ch_diag-s7-300-s7-400)

### Description CH_DIAG (S7-300, S7-400)

The instruction CH_DIAG is used to read out additional channel-specific diagnostic variables from the module.

#### Call

CH_DIAG does not require any initialization routine and is normally called cyclically.

CH_DIAG has to be called in the same OB as all the other instructions that access the same FM 355.

---

**See also**

[Input parameters CH_DIAG (S7-300, S7-400)](#input-parameters-ch_diag-s7-300-s7-400)
  
[Output parameters CH_DIAG (S7-300, S7-400)](#output-parameters-ch_diag-s7-300-s7-400)
  
[Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)
  
[Block diagrams CH_DIAG (S7-300, S7-400)](#block-diagrams-ch_diag-s7-300-s7-400)

### Input parameters CH_DIAG (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| MOD_ADDR | 0.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CHANNEL | 2.0 | INT | 1 | The number of the controller channel to which the instance DB is referenced is configured at the "Channel number" input.  Values of 1 to 4 are permitted. |

---

**See also**

[Description CH_DIAG (S7-300, S7-400)](#description-ch_diag-s7-300-s7-400)
  
[Output parameters CH_DIAG (S7-300, S7-400)](#output-parameters-ch_diag-s7-300-s7-400)
  
[Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)
  
[Block diagrams CH_DIAG (S7-300, S7-400)](#block-diagrams-ch_diag-s7-300-s7-400)

### Output parameters CH_DIAG (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SP_R | 4.0 | REAL | 0.0 | If a ratio controller is set, the input value of the setpoint value is assigned to the parameter. |
| PV_R | 8.0 | REAL | 0.0 | The following value is only assigned to the parameter value if the ratio controller is set: (Process value A - Setpoint value offset) / Process value D |
| DIF_I | 12.0 | REAL | 0.0 | The input variable of the D-action is displayed at the DIF_I parameter. This is particularly of interest if, for example, an analog input is configured as the input variable of the D-action. |
| TRACKPER | 16.0 | REAL | 0.0 | The TRACKPER parameter shows the input variable to which the output value is tracked if the track-manipulated-variable function is enabled on the controller. |
| IDSTATUS | 20.0 | WORD | 0.0 | The state of the identification is displayed at [Parameter IDSTATUS](#parameter-idstatus-s7-300-s7-400). |
| LMN_P | 22.0 | REAL | 0.0 | The P-action of the manipulated variable is displayed at the LMN_P parameter. |
| LMN_I | 26.0 | REAL | 0.0 | The I-action of the manipulated variable is displayed at the LMN_I parameter. |
| LMN_D | 30.0 | REAL | 0.0 | The D-action of the manipulated variable is displayed at the LMN_D parameter. |
| RET_VALU | 34.0 | WORD | 0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated when an error is reported via QMOD_F. |

---

**See also**

[Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)

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

[Description CH_DIAG (S7-300, S7-400)](#description-ch_diag-s7-300-s7-400)
  
[Input parameters CH_DIAG (S7-300, S7-400)](#input-parameters-ch_diag-s7-300-s7-400)
  
[Output parameters CH_DIAG (S7-300, S7-400)](#output-parameters-ch_diag-s7-300-s7-400)
  
[Block diagrams CH_DIAG (S7-300, S7-400)](#block-diagrams-ch_diag-s7-300-s7-400)

### Block diagrams CH_DIAG (S7-300, S7-400)

The following diagnostic values of the control deviation are displayed.

![Figure](images/18153828875_DV_resource.Stream@PNG-en-US.png)

The following values of the control algorithm are displayed.

![Figure](images/18153849483_DV_resource.Stream@PNG-en-US.png)

The following values of the continuous controller or step controller are displayed.

![Figure](images/18153870091_DV_resource.Stream@PNG-en-US.png)

---

**See also**

[Description CH_DIAG (S7-300, S7-400)](#description-ch_diag-s7-300-s7-400)
  
[Input parameters CH_DIAG (S7-300, S7-400)](#input-parameters-ch_diag-s7-300-s7-400)
  
[Output parameters CH_DIAG (S7-300, S7-400)](#output-parameters-ch_diag-s7-300-s7-400)
  
[Parameter IDSTATUS (S7-300, S7-400)](#parameter-idstatus-s7-300-s7-400)

## PID_PAR (S7-300, S7-400)

This section contains information on the following topics:

- [Description PID_PAR (S7-300, S7-400)](#description-pid_par-s7-300-s7-400)
- [Input parameters PID_PAR (S7-300, S7-400)](#input-parameters-pid_par-s7-300-s7-400)
- [Output parameters PID_PAR (S7-300, S7-400)](#output-parameters-pid_par-s7-300-s7-400)
- [Alterable parameters (S7-300, S7-400)](#alterable-parameters-s7-300-s7-400)

### Description PID_PAR (S7-300, S7-400)

The instruction PID_PAR is used for the online modification of parameters that cannot be defined via the instruction PID_FM. To view the parameters that can be modified, refer to the table [Changeable parameters](#alterable-parameters-s7-300-s7-400)

#### Call

PID_PAR requires an initialization routine. It is automatically triggered if the system data (SDB default data of the FM 355) has not yet been read from the instruction PID_PAR. You can also start the initialization yourself with COM_RST=TRUE, which is usually done in OB100 since the system data is sent to the FM 355 after STOP-RUN of the CPU. The initialization process lasts several cycles. No data is sent to the FM 355 via WRREC during the initialization. The block automatically resets the COM_RST parameter after the initialization.

To save run time, PID_PAR should not be called cyclically. It should only be called when parameters are to be changed. COM_RST must then be FALSE.

PID_PAR has to be called in the same OB as all the other instructions that access the same FM 355.

If the FM 355 is used in distributed I/Os, it may take a few call cycles until the parameters have been transferred to the FM 355. The BUSY parameter has the value TRUE until the transfer has been completed. You should call PID_PAR as many times as necessary until BUSY = FALSE and RET_VALU = 0.

#### Mode of operation

In the initialization routine, PID_PAR reads the parameters from the system data and stores them in static variables. Per call, PID_PAR modifies one of these REAL variables and one of these INT variables. At the input parameter INDEX_R or INDEX_I, specify the index numbers of the parameter that you want to modify. At the input parameter VALUE_R or VALUE_I, enter the new values. PID_PAR transfers the entire data record to FM 355 with the modified variables.

To modify additional parameters you have to call **the same** instance DB several times consecutively with COM_RST = FALSE and with different index numbers.

The COM_RST parameter is an input parameter that is not reset by PID_PAR.

> **Note**
>
> Please note that parameters that you have changed using PID_PAR are overwritten by the parameters from the system data during the start-up.

#### Start-up

During CPU start-up and during CPU STOP-RUN transition, the parameters on the FM 355 are overwritten with the parameters from the SDB of the CPU.

#### Example

During operation you want to modify the ramp-up time for the reference variable and, depending on the process state, use different analog input values as process value.

- Call PID_PAR using COM_RST = TRUE during the start-up of the CPU.
- To configure the ramp-up time for the reference variable at 10.0, use INDEX_R = 30, VALUE_R = 10.0 and INDEX_I = 0 to call PID_PAR during operation.
- If you want to parameterize the analog input value 4 of the module as the process value, call PID_PAR with INDEX_R = 0, INDEX_I = 50 and VALUE_I = 4 during operation.

---

**See also**

[Alterable parameters (S7-300, S7-400)](#alterable-parameters-s7-300-s7-400)
  
[Input parameters PID_PAR (S7-300, S7-400)](#input-parameters-pid_par-s7-300-s7-400)
  
[Output parameters PID_PAR (S7-300, S7-400)](#output-parameters-pid_par-s7-300-s7-400)

### Input parameters PID_PAR (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| COM_RST | 0.0 | BOOL | TRUE | If the parameter COM_RST = TRUE, the instruction PID_PAR executes an initialization routine. During this initialization process the parameters are read from the system data of the CPU and saved in the instance DB. |
| MOD_ADDR | 2.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CHANNEL | 4.0 | INT | 1 | The number of the controller channel to which the instance DB is referenced is configured at the "Channel number" input.  Values 1 to 4 are permitted. |
| INDEX_R | 6.0 | INT | 0.0 | - 0: No REAL parameters are changed - 1 to 48: Each value corresponds to a [changeable REAL parameter](#alterable-parameters-s7-300-s7-400). |
| VALUE_R | 8.0 | REAL | 0.0 | Depends on the relevant parameter |
| INDEX_I | 12.0 | INT | 0.0 | - 0: No INT parameters are changed. - 49 to 61: Each value corresponds to a [changeable INT parameter](#alterable-parameters-s7-300-s7-400). |
| VALUE_I | 14.0 | INT | 0.0 | Depends on the relevant parameter |

---

**See also**

[Description PID_PAR (S7-300, S7-400)](#description-pid_par-s7-300-s7-400)
  
[Alterable parameters (S7-300, S7-400)](#alterable-parameters-s7-300-s7-400)
  
[Output parameters PID_PAR (S7-300, S7-400)](#output-parameters-pid_par-s7-300-s7-400)

### Output parameters PID_PAR (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 16.0 | WORD | 0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated when an error is reported via QMOD_F. |
| BUSY | 18.0 | BOOL | FALSE | If BUSY = TRUE, the parameters have not yet been transferred from the module (in the case of distributed I/Os). The instruction PID_PAR should then be called again in the next cycle. |

### Alterable parameters (S7-300, S7-400)

List of the REAL and INT parameters on a FM 355 that are to be modified with PID_PAR

| Data type | Description | Index number |
| --- | --- | --- |
| – | No parameter selected | 0 |
| REAL | Filter time constant for analog input | 1 |
| REAL | End of scale (100%) | 2 |
| REAL | Start of scale (0%) | 3 |
| REAL | Polyline, Interpolation point 1 input side | 4 |
| REAL | Polyline, Interpolation point 2 input side | 5 |
| REAL | Polyline, Interpolation point 3 input side | 6 |
| REAL | Polyline, Interpolation point 4 input side | 7 |
| REAL | Polyline, Interpolation point 5 input side | 8 |
| REAL | Polyline, Interpolation point 6 input side | 9 |
| REAL | Polyline, Interpolation point 7 input side | 10 |
| REAL | Polyline, Interpolation point 8 input side | 11 |
| REAL | Polyline, Interpolation point 9 input side | 12 |
| REAL | Polyline, Interpolation point 10 input side | 13 |
| REAL | Polyline, Interpolation point 11 input side | 14 |
| REAL | Polyline, Interpolation point 12 input side | 15 |
| REAL | Polyline, Interpolation point 13 input side | 16 |
| REAL | Polyline, Interpolation point 1 output side | 17 |
| REAL | Polyline, Interpolation point 2 output side | 18 |
| REAL | Polyline, Interpolation point 3 output side | 19 |
| REAL | Polyline, Interpolation point 4 output side | 20 |
| REAL | Polyline, Interpolation point 5 output side | 21 |
| REAL | Polyline, Interpolation point 6 output side | 22 |
| REAL | Polyline, Interpolation point 7 output side | 23 |
| REAL | Polyline, Interpolation point 8 output side | 24 |
| REAL | Polyline, Interpolation point 9 output side | 25 |
| REAL | Polyline, Interpolation point 10 output side | 26 |
| REAL | Polyline, Interpolation point 11 output side | 27 |
| REAL | Polyline, Interpolation point 12 output side | 28 |
| REAL | Polyline, Interpolation point 13 output side | 29 |
| REAL | Ramp-up time for reference variable | 30 |
| REAL | Safety reference variable or safety Reference variable response | 31 |
| REAL | Offset for setpoint link (ratio/blending controller) | 32 |
| REAL | Factor for process value B (three-component controller) | 33 |
| REAL | Factor for process value C (three-component controller) | 34 |
| REAL | Offset for process value link (three-component controller) | 35 |
| REAL | Factor for disturbance variable link | 36 |
| REAL | Operating point | 37 |
| REAL | Aggressivity at fuzzy controller | 38 |
| REAL | Vertices for split-range function: Start of input signal A range | 39 |
| REAL | Vertices for split-range function: End of input signal A range | 40 |
| REAL | Vertices for split-range function: Start of output signal A range | 41 |
| REAL | Vertices for split-range function: End of output signal A range | 42 |
| REAL | Vertices for split-range function: Start of input signal B range | 43 |
| REAL | Vertices for split-range function: End of input signal B range | 44 |
| REAL | Vertices for split-range function: Start of output signal B range | 45 |
| REAL | Vertices for split-range function: End of output signal B range | 46 |
| REAL | Minimum pulse time | 47 |
| REAL | Minimum break time | 48 |
| INT | Selection of the reference variable SP or SP_RE for the controller  0: Setpoint SP_RE of the instruction  1 to 4: Analog input value 1 to 4  17 to 20: Manipulated variable (LMN) of controllers 1 to 4 | 49 |
| INT | Selection of the main controlled variable process value A for the controller  0: Process value A = 0.0  1 to 4: Analog input value 1 to 4 | 50 |
| INT | Selection of the auxiliary controlled variable process value B for the controller  0: Process value B = 0.0  1 to 4: Analog input value 1 to 4 | 51 |
| INT | Selection of the auxiliary controlled variable process value C for the controller  0: Process value C = 0.0  1 to 4: Analog input value 1 to 4 | 52 |
| INT | Selection of the auxiliary controlled variable process value D for the controller  0: Process value D = 0.0  1 to 4: Analog input value 1 to 4  17 to 20: Manipulated variable (LMN) of controllers 1 to 4 | 53 |
| INT | Selection of the disturbance variable DISV for the controller  0: Disturbance variable = 0.0  1 to 4: Analog input value 1 to 4 | 54 |
| INT | Selection of position follow-up TRACK_PER for the controller  0: Position follow-up = 0.0  1 to 4: Analog input value 1 to 4 | 55 |
| INT | Selection of position follow-up LMNR_PER for the controller  0: Position follow-up = 0.0  1 to 4: Analog input value 1 to 4 | 56 |
| INT | Selection of the signal for switching to the safety value for the manipulated value of the controller  0: Can only be assigned via SAFE_ON of the instruction PID_FM  1 to 8: Assignment via SAFE_ON parameter of the instruction PID_FM ORed with digital input 1 to 8 | 57 |
| INT | Selecting the signal for switching over to tracking function of the manipulated value of the controller  0: Can only be assigned via LMNTRKON of the instruction PID_FM  1 to 8: Assignment via LMNTRKON parameter of the instruction PID_FM ORed with digital input 1 to 8 | 58 |
| INT | Selecting the signal for changing over the manipulated value of the controller to LMN_RE  0: Can only be assigned via LMN_REON of the instruction PID_FM  1 to 8: Assignment via LMN_REON parameter of the instruction PID_FM ORed with digital input 1 to 8 | 59 |
| INT | Selecting the high limit signal of the position feedback  0: Can only be assigned via LMNRHSRE of the instruction PID_FM  1 to 8: Assignment via LMNRHSRE parameter of the instruction PID_FM ORed with digital input 1 to 8 | 60 |
| INT | Selecting the low limit signal of the position feedback  0: Can only be assigned via LMNRLSRE of the instruction PID_FM  1 to 8: Assignment via LMNRLSRE parameter of the instruction PID_FM ORed with digital input 1 to 8 | 61 |

---

**See also**

[Description PID_PAR (S7-300, S7-400)](#description-pid_par-s7-300-s7-400)
  
[Input parameters PID_PAR (S7-300, S7-400)](#input-parameters-pid_par-s7-300-s7-400)
  
[Output parameters PID_PAR (S7-300, S7-400)](#output-parameters-pid_par-s7-300-s7-400)

## CJ_T_PAR (S7-300, S7-400)

This section contains information on the following topics:

- [Description CJ_T_PAR (S7-300, S7-400)](#description-cj_t_par-s7-300-s7-400)
- [Input parameters CJ_T_PAR (S7-300, S7-400)](#input-parameters-cj_t_par-s7-300-s7-400)
- [Output parameters CJ_T_PAR (S7-300, S7-400)](#output-parameters-cj_t_par-s7-300-s7-400)

### Description CJ_T_PAR (S7-300, S7-400)

The instruction CJ_T_PAR is used for online modification of the configured reference junction temperature. This is necessary if a temperature control system with several FM 355 with thermoelement inputs is to be operated without having to connect a Pt 100 to each FM 355.

#### Call

CJ_T_PAR requires an initialization routine. For this purpose it has to be called once with the COM_RST = TRUE parameter at the start-up of the CPU.

CJ_T_PAR is normally called cyclically. For this purpose COM_RST should be set to FALSE for runtime reasons. The COM_RST parameter is an input parameter that is not reset.

CJ_T_PAR has to be called in the same OB as all the other instructions that access the same FM 355.

If the FM 355 is used in distributed I/Os, it may take a few call cycles until the parameters have been transferred to the FM 355. The BUSY parameter has the value TRUE until the transfer has been completed. You should therefore call the instruction CJ_T_PAR as many times as necessarry when changing parameters until BUSY = FALSE.

#### Example

If an FM 355 measures the reference junction temperature of an extruder control system with more than four heating zones, this can be read out by READ_355 at parameter CJ_TEMP and can be parameterized for the other FM 355 via CJ_T_PAR.

---

**See also**

[Input parameters CJ_T_PAR (S7-300, S7-400)](#input-parameters-cj_t_par-s7-300-s7-400)
  
[Output parameters CJ_T_PAR (S7-300, S7-400)](#output-parameters-cj_t_par-s7-300-s7-400)

### Input parameters CJ_T_PAR (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| COM_RST | 0.0 | BOOL | FALSE | If the parameter COM_RST = TRUE, the instruction CJ_T_PAR executes an initialization routine. During this initialization process the parameters are read from the system data of the CPU and saved in the instance DB. |
| MOD_ADDR | 2.0 | INT | 256 | The module address that results from the configuration with STEP 7 is set at this input. |
| CJ_T | 4.0 | REAL | 0.0 | The reference junction temperature can be specified at parameter CJ_T.  The permissible value range depends on the sensor type. |

---

**See also**

[Description CJ_T_PAR (S7-300, S7-400)](#description-cj_t_par-s7-300-s7-400)
  
[Output parameters CJ_T_PAR (S7-300, S7-400)](#output-parameters-cj_t_par-s7-300-s7-400)

### Output parameters CJ_T_PAR (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| RET_VALU | 8.0 | WORD | 0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated when an error is reported via QMOD_F. |
| BUSY | 10.0 | BOOL | FALSE | If BUSY = TRUE, the parameters have not yet been transferred from the module (in the case of distributed I/Os). The instruction PID_PAR should then be called again in the next cycle. |

## DB for HMI (S7-300, S7-400)

This section contains information on the following topics:

- [Description DB 101 to 104 (S7-300, S7-400)](#description-db-101-to-104-s7-300-s7-400)
- [Input parameters DB 101 to 104 (S7-300, S7-400)](#input-parameters-db-101-to-104-s7-300-s7-400)
- [Output parameters DB 101 to 104 (S7-300, S7-400)](#output-parameters-db-101-to-104-s7-300-s7-400)
- [In/out parameters DB 101 to 104 (S7-300, S7-400)](#inout-parameters-db-101-to-104-s7-300-s7-400)

### Description DB 101 to 104 (S7-300, S7-400)

In order to operate the FM 355 if the CPU fails, you require data blocks 101 to 104. You can establish a maximum of three connections from the FM 355 to OPs via MPI.

Operator control of the FM 355 with the OP is only possible in the STOP mode of the CPU or at a CPU failure.

Monitoring of the FM 355 with the OP is always possible.

The variable interface of the FM 355 contains four data blocks with the block numbers 101 to 104 for the controller channels 1 to 4 (refer to the following figure).

> **Note**
>
> The contents of the data blocks 101 to 104 do not automatically reflect the parameter value effective at the FM 355. Parameters changed with the OP are only transferred to the FM 355 after the operating bits LOAD_PAR and LOAD_OP have been set.
>
> If you change a parameter using OP operation without setting the corresponding operating bit, the changed parameter value is entered in the data block, but the FM 355 continues to operate internally with the unchanged old value of the parameter.
>
> After the operating bits have been set and the parameters have been transferred to the FM 355, the operating bits LOAD_PAR and LOAD_OP are reset by the FM 355.

![Figure](images/20021443851_DV_resource.Stream@PNG-en-US.png)

| Symbol | Meaning |
| --- | --- |
| * | controlled by the READ_VAR parameter of the instance DB |
| ** | controlled by the LOAD_OP and LOAD_PAR parameters |

---

**See also**

[Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
  
[Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
  
[Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
  
[Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)

### Input parameters DB 101 to 104 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SP_HLM | 0.0 | REAL | 100.0 | The setpoint is always limited to a high and a low limit. The "Setpoint high limit" input specifies the high limit.  SP_HLM &gt; SP_LLM |
| SP_LLM | 4.0 | REAL | 0.0 | The setpoint is always limited to a high and a low limit. The "Setpoint low limit" input specifies the low limit.  SP_LLM &lt; SP_HLM |
| H_ALM | 8.0 | REAL | 100.0 | You can configure four limits for monitoring the process value or error signal. The "High limit interrupt" input specifies the highest limit.  H_ALM &gt; H_WRN |
| H_WRN | 12.0 | REAL | 90.0 | You can configure four limits for monitoring the process value or error signal. The "High limit warning" input specifies the second to highest limit.  Values from H_ALM to L_WRN are permitted. |
| L_WRN | 16.0 | REAL | 10.0 | You can configure four limits for monitoring the process value or error signal. The "Low limit warning" input specifies the second to lowest limit.  Values from H_WRN to L_ALM are permitted. |
| L_ALM | 20.0 | REAL | 0.0 | You can configure four limits for monitoring the process value or error signal. The "Low limit alarm" specifies the lowest limit.  L_ALM &lt; L_WRN |
| HYS | 24.0 | REAL | 1.0 | To prevent flickering of the monitoring displays, a hysteresis can be configured at the "Hysteresis" input.   HYS ≥ 0.0 |
| DEADB_W | 28.0 | REAL | 0.0 | A dead band is applied to the error signal. The "Dead band width" input determines the size of the dead band.  DEADB_W ≥ 0.0 |
| GAIN | 32.0 | REAL | 1.0 | The "Proportional gain" input specifies controller gain. |
| TI | 36.0 | REAL | 3000.0 | The "Integration time" input determines the time  response of the integrator. If TI = 0, the integral action is disabled.  TI = 0.0 or TI ≥ 0.5 |
| TD | 40.0 | REAL | 0.0 | The "Derivative-action time" input determines the time response of the differentiator. If TD = 0, the derivative action is disabled  TD = 0.0 or TD ≥ 1.0 |
| TM_LAG | 44.0 | REAL | 5.0 | The algorithm of the D-action includes a time lag that can be configured at the "Time lag of the D-action" input.  TM_LAG ≥ 0.5 |
| LMN_SAFE | 48.0 | REAL | 0.0 | At the "Safety manipulated value" input, a safety value can be configured for the manipulated value, .   Values from -100.0 to 100.0 (%) are permitted. |
| LMN_HLM | 52.0 | REAL | 100.0 | The manipulated value is always limited to a high and a low limit. The "High limit limit of manipulated value" input specifies the high limit.  (This does not apply to step controllers without analog position feedback)   Values from LMN_LLM to 100.0 (%) are permitted. |
| LMN_LLM | 56.0 | REAL | 0.0 | The manipulated value is always limited to a high and a low limit. The "Low limit of manipulated value" input specifies the low limit.   (This does not apply to step controllers without analog position feedback)   Values from -100.0 to LMN_HLM (%) are permitted. |
| MTR_TM | 60.0 | REAL | 60.0 | The runtime from endstop to endstop of the control valve is entered at the "Motor actuating time" parameter.  (Applies to step controllers only).  MTR_TM ≥ 0.001 |
| PULSE_TM | 64.0 | REAL | 0.2 | A minimum pulse duration can be configured at the "Minimum pulse time" parameter.  (Applies to step controllers or pulse controllers only)  PULSE_TM ≥ 0.0 |
| BREAK_TM | 68.0 | REAL | 0.2 | A minimum break time can be configured at the "Minimum break time" parameter.  (Applies to step controllers or pulse controllers only)  BREAK_TM ≥ 0.0 |
| SP_RE | 72.0 | REAL | 0.0 | An external setpoint is interconnected with the controller at the "External setpoint" input. |
| LMN_RE | 76.0 | REAL | 0.0 | An external manipulated value is interconnected with the controller at the "External manipulated value" input. |
| LMNRSVAL | 80.0 | REAL | 0.0 | The Commissioning dialog provides you with access to the input "Start value of the simulated position feedback". The start value of the simulation is entered at the parameter.  (Only for step controllers without analog position feedback)  Values from -100.0 to 100.0 (%) are permitted. |
| SAFE_ON | 84.0 | BOOL | FALSE | If the "Adopt safety position" input is set, a safety value is applied as manipulated value.  Note: The signal processing of manipulated values via LMNDN_OP , LMNUP_OP and LMNSOPON on a step controller is of higher priority than the safety manipulated value. |
| LMNTRKON | 84.1 | BOOL | FALSE | If input "Follow-up (LMN via AI)" is set, the manipulated value is adjusted to an analog input (AI).  (This does not apply to step controllers without analog position feedback) |
| LMN_REON | 84.2 | BOOL | FALSE | If input "Enable external manipulated value" is set, the external manipulated value LMN_RE is set as the manipulated value. |
| LMNRHSRE | 84.3 | BOOL | FALSE | The signal "Control valve at high endstop" is interconnected at the "High endstop signal of position feedback" input. LMNRHSRE = TRUE means: The control valve is at high endstop.  (Applies to step controllers only). |
| LMNRLSRE | 84.4 | BOOL | FALSE | The signal "Control valve at low endstop" is interconnected at the "Low endstop signal of position feedback" input. LMNRLSRE = TRUE means: The control valve is at the low endstop.  (Applies to step controllers only). |
| LMNSOPON | 84.5 | BOOL | FALSE | If the bit is set at input "Enable manipulated value signal operation", the LMNUP_OP and LMNDN_OP signals are set as the manipulated value signals.  (Applies to step controllers only). |
| LMNUP_OP | 84.6 | BOOL | FALSE | If LMNSOPON is set, the value at input "Manipulated value signal up operation" is set as the manipulated value signal.  (Applies to step controllers only). |
| LMNDN_OP | 84.7 | BOOL | FALSE | If LMNSOPON is set, the value at input "Manipulated value signal down operation" is set as the manipulated value signal.  (Applies to step controllers only). |
| MONERSEL | 85.0 | BOOL | FALSE | The controller possesses a limit value detector that can be applied either for the process value or for the error signal. If the input "Monitoring: Process value = 0, Error signal = 1" is set, the errcr signal will be monitored. |
| LMNRS_ON | 85.1 | BOOL | FALSE | You can simulate no position feedback if this is not available. The function is enabled by setting the "Enable simulation of position feedback" input  CAUTION: Offset between the simulation value and real position feedback increases over the time.  (Only for step controllers without analog position feedback) |
| FUZID_ON | 85.2 | BOOL | FALSE | The identification of the fuzzy algorithm is enabled at the input "Enable fuzzy identification". |
| SPINT_EN | 85.3 | BOOL | FALSE | The input "Operator input: External = 0, Internal = 1" determines the input that is transferred as a setpoint to the module.  SPINT_EN = TRUE: SP_INT is transferred.  SPINT_EN = FALSE: SP_RE is transferred. |
| P_SEL | 85.4 | BOOL | TRUE | It is possible to enable or disable PID actions individually in the PID algorithm. The proportional action is enabled when the "Enable P-action" input is set. |
| PFDB_SEL | 85.5 | BOOL | FALSE | In the PID algorithm, the P- and D-actions can be included in the feedback loop. The proportional action is located in the feedback loop when the "Enable P-action in feedback loop" input is set. |
| D_EL_SEL | 86.0 | INT | 0 | The D-action element in the PID algorithm can be assigned to a separate input. This is selected at the input "D-action element input".  0: Error signal  1 to 4: Analog input 1 to 4  17: negative process value |

---

**See also**

[Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
  
[Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
  
[Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
  
[Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)

### Output parameters DB 101 to 104 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SP | 94.0 | REAL | 0.0 | The setpoint that is currently in effect is available at the "Setpoint" output. |
| PV | 98.0 | REAL | 0.0 | The process value that becomes effective is issued on the "Process value" output. |
| ER | 102.0 | REAL | 0.0 | The control deviation that becomes effective is issued on the "Control deviation" output. |
| DISV | 106.0 | REAL | 0.0 | The interference that becomes effective is issued on the "Interference" output.  Values from -100.0 to 100.0 (%) are permitted. |
| LMN | 110.0 | REAL | 0.0 | The manipulated value that becomes effective is issued on the "Manipulated value" output. Step controllers without analog position feedback output the unlimited P- + D-action at the LMN parameter.   Values from -100.0 to 100.0 (%) are permitted. |
| LMN_A | 114.0 | REAL | 0.0 | At the output "Manipulated value A of the split range function / position feedback", continuous controllers display the manipulated value A and step controllers with analog position feedback display the position feedback.  Step controllers without analog position feedback display the simulated position feedback.   Values from -100.0 to 100.0 (%) are permitted. |
| LMN_B | 118.0 | REAL | 0.0 | Continuous controllers display the manipulated value B of the split-range function at the output “Manipulated value B of split-range function”.   Values from -100.0 to 100.0 (%) are permitted. |
| QH_ALM | 122.0 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Violation of H_ALM limit is reported at the output "High limit alarm triggered". |
| QH_WRN | 122.1 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Exceeding of the limit H_WRN is signaled at the "High limit warning triggered" output. |
| QL_WRN | 122.2 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Exceeding of the limit L_WRN is signaled at the "Low limit warning triggered" output. |
| QL_ALM | 122.3 | BOOL | FALSE | The process value or the controlled variable is monitored for four limits. Exceeding of the limit L_ALM is signaled at the "Low limit alarm triggered" output. |
| QLMN_HLM | 122.4 | BOOL | FALSE | The manipulated value is always limited to a high and a low limit. Violation of the high limit is reported at output "High limit of manipulated value triggered".  (Does not apply to step controllers without analog position feedback) |
| QLMN_LLM | 122.5 | BOOL | FALSE | The manipulated value is always limited to a high and a low limit. Violation of the low limit is reported at output "Low limit of manipulated value triggered".  (Does not apply to step controllers without analog position feedback) |
| QSPINTON | 122.6 | BOOL | FALSE | The output "Internal setpoint on" indicates that SP_INT was transferred to the module. |
| QPARA_F | 123.0 | BOOL | FALSE | The module checks the validity of the parameters. A parameter assignment error is displayed at the "Parameter assignment error" output. These parameter assignment errors can also be read out in the module's "Online &amp; Diagnostics" dialog. |
| QCH_F | 123.1 | BOOL | FALSE | The "Channel error" output is set if the controller channel cannot provide valid results. A channel error (for example, wire break) is also set if QPARA_F = 1 or QMOD_F = 1. If QCH_F = TRUE, then the precise error information in the diagnostic data record DS1 of the module is read out. |
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
| QSPLEPV | 124.7 | BOOL | FALSE | The output "Display of FUZZY controller: Setpoint &lt; process value" is set when the fuzzy controller is switched on, if the setpoint is less than the effective process value. |
| QSPR | 125.0 | BOOL | FALSE | If the output "Split-range operation" is set, the continuous controller is operating in split-range mode. |
| QLMNUP | 125.1 | BOOL | FALSE | This is the "Manipulated value signal up" output.  (Only in the case of step controllers or pulse controllers) |
| QLMNDN | 125.2 | BOOL | FALSE | This is the "Manipulated value signal down" output.  (Only in the case of step controllers or pulse controllers) |
| QBACKUP | 125.4 | BOOL | FALSE | 0= No backup state (CPU in RUN)  1= Backup state (CPU in STOP or has failed) |
| QID | 125.5 | BOOL | FALSE | QID = TRUE indicates that an identification is running (not that it is enabled). On completion of the identification, the identification result can be read out from the IDSTATUS parameter of the instruction CH_DIAG. |
| QMAN_FC | 125.6 | BOOL | FALSE | The controller is a master controller that is adjusted by the manual mode of a slave controller to its process value or its I-action is stopped, because the setpoint or manipulated value of the slave controller lies in the limit. |
| RET_VALU | 126.0 | WORD | 0 | RET_VALU contains the 2nd and 3rd bytes from the STATUS parameter of the RDREC and WRREC instructions. RET_VALU can be evaluated when an error is reported via QMOD_F. |

---

**See also**

[Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
  
[Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
  
[Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
  
[Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)

### In/out parameters DB 101 to 104 (S7-300, S7-400)

| Parameters | Address | Data type | Default | Description |
| --- | --- | --- | --- | --- |
| SP_INT | 128.0 | REAL | 0.0 | The in/out parameter "Internal setpoint" is used to specify a setpoint by means of operating and monitoring functions. |
| SP_OP | 132.0 | REAL | 0.0 | The "Commissioning" dialog can access the in/out parameter "Setpoint operation". If the SP_OP_ON bit is set, the "Setpoint operation" value is applied as the setpoint. |
| LMN_OP | 136.0 | REAL | 0.0 | The "Commissioning" dialog can access the in/out parameter "Manipulated value operation". If the LMNOP_ON bit is set, the "Manipulated value operation" value is applied as the manipulated value.  Values from -100.0 to 100.0 (%) are permitted. |
| SP_OP_ON | 140.0 | BOOL | FALSE | The "Commissioning" dialog can access the in/out parameter "Enable setpoint operation". If the bit is set, the value SP_OP is applied as setpoint. |
| LMNOP_ON | 140.1 | BOOL | FALSE | The "Commissioning" dialog can access the in/out parameter "Enable manipulated value operation". If the bit is set, the value LMN_OP is applied as manipulated value. |
| LOAD_PAR | 140.2 | BOOL | FALSE | If the in/out parameter "Load control parameters to FM 355" is set, the control parameters are loaded into the module and the in/out parameter is reset. |
| LOAD_OP | 140.3 | BOOL | FALSE | If the in/out parameter "Load operating parameters to FM 355" is set, the operating parameters are loaded into the module and the in/out parameter is reset. |

---

**See also**

[Description DB 101 to 104 (S7-300, S7-400)](#description-db-101-to-104-s7-300-s7-400)
  
[Description PID_FM (S7-300, S7-400)](#description-pid_fm-s7-300-s7-400)
  
[Mode of operation PID_FM (S7-300, S7-400)](#mode-of-operation-pid_fm-s7-300-s7-400)
  
[Input parameters PID_FM (S7-300, S7-400)](#input-parameters-pid_fm-s7-300-s7-400)
  
[Output parameters PID_FM (S7-300, S7-400)](#output-parameters-pid_fm-s7-300-s7-400)
  
[In/out parameters PID_FM (S7-300, S7-400)](#inout-parameters-pid_fm-s7-300-s7-400)
  
[Block diagram PID_FM (S7-300, S7-400)](#block-diagram-pid_fm-s7-300-s7-400)
