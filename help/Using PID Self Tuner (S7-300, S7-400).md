---
title: "Using PID Self Tuner (S7-300, S7-400)"
package: TFTOPIDTunenUS
topics: 16
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using PID Self Tuner (S7-300, S7-400)

This section contains information on the following topics:

- [Tuning continuous controllers and pulse controllers (S7-300, S7-400)](#tuning-continuous-controllers-and-pulse-controllers-s7-300-s7-400)
- [Tuning step controllers (S7-300, S7-400)](#tuning-step-controllers-s7-300-s7-400)

## Tuning continuous controllers and pulse controllers (S7-300, S7-400)

This section contains information on the following topics:

- [Interconnecting TUN_EC with controller (S7-300, S7-400)](#interconnecting-tun_ec-with-controller-s7-300-s7-400)
- [Tuning options (S7-300, S7-400)](#tuning-options-s7-300-s7-400)
- [Tuning phases (S7-300, S7-400)](#tuning-phases-s7-300-s7-400)
- [Performing pretuning (S7-300, S7-400)](#performing-pretuning-s7-300-s7-400)
- [Performing fine tuning (S7-300, S7-400)](#performing-fine-tuning-s7-300-s7-400)
- [Performing cold tuning (S7-300, S7-400)](#performing-cold-tuning-s7-300-s7-400)
- [Performing tuning manually (S7-300, S7-400)](#performing-tuning-manually-s7-300-s7-400)

### Interconnecting TUN_EC with controller (S7-300, S7-400)

The TUN_EC instruction is used to tune a continuous controller or a pulse controller. Depending on the controller, you interconnect TUN_EC with one of the following instructions:

| Controller | Instruction |
| --- | --- |
| FM 355 C, FM 355 S pulse controller | PID_FM |
| FM 455 C, FM 455 S pulse controller | PID_FM |
| PID Basic Functions | CONT_C with or without PULSEGEN |
| Standard PID Control (PID Professional optional package) | PID_CP |
| Modular PID Control (PID Professional optional package) | PID  LMNGEN_C |

Interconnect the input and output parameters of the TUN_EC instruction with the instruction of the controller as follows.

| TUN_EC | PID_FM | CONT_C | PID_CP |
| --- | --- | --- | --- |
| PV | PV | PV | PV |
| LMN | LMN | LMN | LMN |
| NORM_FAC | -- | -- | (NM_PVHR-NM_PVLR)*0.01 |
| WRITE_DIS | OR operation from LOAD_OP and LOAD_PAR | -- | -- |
| MAN_OUT | LMN_RE | MAN | MAN |
| SP_OUT | SP_RE | SP_INT | SP_INT |
| GAIN | GAIN | GAIN | GAIN |
| TI | TI | TI | TI |
| TD | TD | TD | TD |
| TM_LAG | TM_LAG | TM_LAG | TM_LAG |
| RATIOFAC | -- | -- | RATIOFAC |
| PHASE | -- | -- | PHASE |
| QMAN_ON | LMN_REON | MAN_ON | MAN_ON |
| QI_SEL | -- | I_SEL | I_SEL |
| QD_SEL | -- | D_SEL | D_SEL |
| QWRITE | LOAD_PAR and  LOAD_OP | -- | -- |

---

**See also**

[Mode of operation TUN_EC (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_ec-s7-300-s7-400)
  
[TUN_EC (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#tun_ec-s7-300-s7-400)

### Tuning options (S7-300, S7-400)

#### Pretuning

The PID parameters are tuned during the heating process. During this tuning, process identification with subsequent controller design is carried out.

You can request tuning with ADAPT1ST.

When you set ADAPT1ST = TRUE, then ADAPT_ON = TRUE is set, which forces pretuning to be performed. For pretuning, you specify the manipulated variable jump at the LHLM_TUN parameter.

The ADAPT1ST parameter is only required if serious adaptation errors resulted in process parameters that make the automatically calculated manipulated variable jump unsuitable for a re-adaptation.

When ADAPT1ST = TRUE , the initialization routine of the TUN_EC instruction is run. The following pre-assignments are made:

- The system switches to PI controller. The parameters of PI_CON are transferred to the controller for this purpose. If the PI_CON.GAIN and PI_CON.TI parameters both have the value 0.0, they are pre-assigned with PI_CON.GAIN = 1.5 and PI_CON.TI = 3600.0 s.
- PROCESS.GAIN = 999.0
- RATIOFAC = 1.0
- STATUS_H = 0; STATUS_D = 0; STATUS_C = 0

  > **Note**
  >
  > Unless explicitly required, do **not** call TUN_EC during a warm restart of the CPU in its initialization routine as is usual for other instructions. If you do, all process parameters will be lost.

Tuning is started with ADAPT1ST = TRUE and a subsequent setpoint jump ≥ MIN_STEP in the positive direction.

As a rule, the setpoint jump changes from the setpoint of the cold process (ambient temperature) to a point close to the operating point during pretuning. Any setpoint can be used as the initial state as long as it is ensured that the process is in a steady state. You are not permitted to specify any further setpoint jumps during tuning.

Pretuning trend characteristics

![Pretuning](images/26323273227_DV_resource.Stream@PNG-en-US.png)

#### Fine tuning

Fine tuning is possible only after pretuning has been carried out correctly. With ADAPT_ON = TRUE, TUN_EC decides whether it will perform pretuning or fine tuning. If information about the process is already available, TUN_EC automatically calculates a manipulated variable jump and performs fine tuning. If information on the process is not available, pretuning is carried out.

#### Starting tuning

You can start tuning from either automatic mode or manual mode:

- **Starting tuning from automatic mode**

  In automatic mode, set ADAPT_ON or ADAPT1ST = TRUE and specify a setpoint jump ≥ MIN_STEP.
- **Starting tuning from manual mode**

  In manual mode, set ADAPT_ON or ADAPT1ST = TRUE and specify a setpoint jump ≥ MIN_STEP. You must then reset MAN_ON = FALSE in order for the setpoint jump to become effective and tuning to begin.

#### Cooling tuning

Cooling tuning is possible only after pretuning has been carried out correctly. It is started in PHASE 4. When COOLID_ON = TRUE is set, the controller is set to manual mode and LLLM_TUN is output: MAN_OUT = LLLM_TUN. TUN_EC switches to PHASE = 3, and COOLID_ON is reset again immediately. As soon as a point of inflection in the process value trend is found, TUN_EC switches back to closed-loop control (PHASE = 4). TUN_EC determines a ratio factor RATIOFAC, whose value is forwarded to the pulse generator of the controller.

Cooling tuning trend characteristics

![Cooling tuning](images/26300800907_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> - The COOLID_ON start bit can be set at the same time as ADAPT1ST or ADAPT_ON, or during tuning of the controller parameters. This ensures that cooling tuning can be started immediately after tuning of the controller parameters for heating has been completed.
> - In the case of a plant with several thermally coupled temperature zones (e.g., plastics machines), cooling tuning should not be started until all (!) zones have finished pretuning; otherwise, the pretuning results are invalid.

#### Canceling tuning

To cancel the tuning before the setpoint jump, you must set ADAPT_ON = FALSE . To cancel tuning after the setpoint jump (PHASE 2 or 3) or cancel cooling tuning, you must switch to manual mode (MAN_ON = TRUE).

By setting ADAPT_ON, ADAPT1ST or COOLID_ON during active tuning (PHASE 2 or 3), the tuning is not canceled but is instead completed. Because ADAPT_ON, ADAPT1ST or COOLID_ON is not reset, tuning is restarted once the start conditions are met.

### Tuning phases (S7-300, S7-400)

Individual phases are run through during controller tuning. You can read these phases at the PHASE parameter.

#### PHASE = 0

When an instance DB for TUN_EC is created, the PHASE parameter is preassigned with zero and MAN_ON with TRUE. For this reason, the system switches to manual mode (PHASE = 7) after the first cycle. You can start the pretuning directly from manual mode (ADAPT_ON = TRUE) or switch to automatic mode. When you switch to automatic mode MAN_ON = FALSE for the first time, the parameters of PI_CON are applied. The default values for GAIN and TI are: GAIN = 1.5, TI = 1h.

#### PHASE = 2

As soon as you specify a setpoint jump ≥ MIN_STEP in the positive direction toward the operating point of the warm process state, LHLM_TUN is assigned to MAN_OUT in the case of pretuning, while a value calculated by TUN_EC is assigned to MAN_OUT in the case of fine tuning. QMAN_ON = TRUE is also set. Both values are transferred to the PID controller. The PID controller is controlled with them in manual mode. MIN_STEP should be greater than 10% of the operating range of the setpoint and the process value.

#### PHASE = 3

When the point of inflection of the jump response is recognized (STATUS_H = 2) or when the process value has reached 70% of the setpoint jump height (STATUS_H = 3), a PI controller with conservative settings is designed. The controller gain GAIN is limited to the range from 0.2 to 20.0. As of this point, the controller immediately starts working as a PI controller and attempts to bring the controlled system to a steady-state condition. TUN_EC stores the newly determined PI controller parameters in GAIN, TI, and PI_CON. The previous values of the PI controller are saved in PI_CON_OLD. If it takes a long time to reach steady-state condition (creeping transient response during temperature processes), you can set STEADY = TRUE to initiate controller design with the current data when steady-state condition is almost reached. You can also set STEADY = TRUE to re-initiate the controller design with the current data at a later stage in PHASE = 3 or PHASE = 4. This will often provide some additional improvement to the controller design.

If an overshoot occurs or if no point of inflection is found, the manipulated variable jump size LHLM_TUN selected for pretuning may have been too large. This does not necessarily result in poor controller tuning. For the next pretuning, the value you select for LHLM_TUN should be approximately 20% smaller.

When TUN_EC has recognized steady-state condition or when time 30 × TI (TI: integral action time of the PI controller set in PHASE = 3) has elapsed since the setpoint jump, the controller design is improved and the system switches to PHASE = 4. TUN_ES stores the newly determined PI/PID controller parameters in GAIN, TI, TD, and PI_CON or PID_CON. The previous values of the PID controller are saved in PID_CON_OLD. If possible, a PID controller and a PI controller are designed. If PID_ON = TRUE, the PID controller is activated. Otherwise, the PI controller is activated. GAIN is limited in such a way that the loop gain of the open loop (product of GAIN and process gain) is less than 80.0.

#### PHASE = 4

In this phase, the controller controls using its tuned parameters. From this state, you can start cooling tuning, fine tuning, or pretuning.

You can switch bumplessly between the PI controller and PID controller at any time.

---

**See also**

[Mode of operation TUN_EC (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_ec-s7-300-s7-400)

### Performing pretuning (S7-300, S7-400)

#### Requirements

- The instruction and the technology object are loaded on the CPU.
- TUN_EC is interconnected with a continuous controller or a pulse controller.
- MAN_ON = FALSE
- The controller is in automatic mode.
- The process is in steady-state condition.

#### Procedure

To determine the optimal PID parameters during initial commissioning, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value, and manipulated variable are recorded.
2. Select "Pretuning" from the "Mode" drop-down list.

   TUN_EC is ready for tuning.
3. Choose a controller structure.
4. In the "Manipulated variable" field, enter a manipulated variable to be used until the transition to PHASE = 3.
5. Enter a setpoint in the "Setpoint" field. The setpoint jump must be ≥ MIN_STEP. The new manipulated variable only takes effect when another setpoint is entered.
6. Click the ![Procedure](images/23498796811_DV_resource.Stream@PNG-de-DE.png) "Start tuning" icon.

   Setpoint and manipulated variable are transferred to the controller. The pretuning starts. The status of the tuning is displayed.

---

**See also**

[Mode of operation TUN_EC (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_ec-s7-300-s7-400)

### Performing fine tuning (S7-300, S7-400)

#### Requirements

- The instruction and the technology object are loaded on the CPU.
- TUN_EC is interconnected with a continuous controller or a pulse controller.
- MAN_ON = FALSE
- The controller is in automatic mode.
- The process is in steady-state condition.

#### Procedure

To determine the optimal PID parameters at the operating point, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value, and manipulated variable are recorded.
2. Select "Fine tuning" from the "Mode" list.

   TUN_EC is ready for tuning.
3. Choose a controller structure.
4. Enter a setpoint in the "Setpoint" field. The setpoint jump must be ≥ MIN_STEP.
5. Click the ![Procedure](images/23498796811_DV_resource.Stream@PNG-de-DE.png) "Start tuning" icon.

   The new setpoint is sent to the controller. TUN-EC calculates a manipulated variable jump. Fine tuning starts. The status of the tuning is displayed.

---

**See also**

[Mode of operation TUN_EC (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_ec-s7-300-s7-400)

### Performing cold tuning (S7-300, S7-400)

During cooling tuning, the ratio factor is determined for closed-loop controls with two opposing actuators (e.g. heating/cooling).

#### Requirements

- Pretuning has been carried out correctly.
- The instruction and the technology object are loaded on the CPU.
- TUN_EC is interconnected with a continuous controller or a pulse controller.
- MAN_ON = FALSE
- The controller is in automatic mode.
- The process is in steady-state condition.

#### Procedure

To determine the ratio factor, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value, and manipulated variable are recorded.
2. Select "Cooling tuning" from the "Mode" drop-down list.

   TUN_EC is ready for tuning.
3. Choose a controller structure.
4. In the "Manipulated variable" field, enter a manipulated variable that will be used until the point of inflection is found.
5. Click the ![Procedure](images/23498796811_DV_resource.Stream@PNG-de-DE.png) "Start tuning" icon.

   Cooling tuning starts. The status of the tuning is displayed.

### Performing tuning manually (S7-300, S7-400)

You can manually change the PID parameters if oscillations occur or overshoots following setpoint jump changes are present in the closed control loop after pretuning or fine tuning. For example, you can reset the controller gain GAIN to 80% of the original value and the integral action time TI to 150% of the original setting. In a pulse controller, small continuous oscillations may occur, which you can eliminate by expanding the dead zone DEADB_W.

#### Requirements

- The instruction and the technology object are loaded on the CPU.

#### Procedure

To manually determine the optimal PID parameters, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value, and manipulated variable are recorded.
2. Select "Manual" from the "Mode" list.
3. Choose a controller structure.
4. Enter new PID parameters in the "P", "I" and "D" fields.
5. Click the "Send parameters to the controller" icon ![Procedure](images/13477958795_DV_resource.Stream@PNG-de-DE.png) in the "Tuning" group.
6. Select the "Change setpoint" check box in the "Current values" group.
7. Enter a new setpoint and click the ![Procedure](images/13477958795_DV_resource.Stream@PNG-de-DE.png) icon in the "Current values" group.
8. Clear the "Manual mode" check box, if necessary.

   The controller works with the new PID parameters and controls to the new setpoint.
9. Check the quality of the PID parameters based on the trend characteristics.
10. Repeat steps 3 to 9 until you are satisfied with the controller results.

---

**See also**

[Mode of operation TUN_EC (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_ec-s7-300-s7-400)

## Tuning step controllers (S7-300, S7-400)

This section contains information on the following topics:

- [Interconnecting TUN_ES with controller (S7-300, S7-400)](#interconnecting-tun_es-with-controller-s7-300-s7-400)
- [Tuning options (S7-300, S7-400)](#tuning-options-s7-300-s7-400-1)
- [Tuning phases (S7-300, S7-400)](#tuning-phases-s7-300-s7-400-1)
- [Performing pretuning (S7-300, S7-400)](#performing-pretuning-s7-300-s7-400-1)
- [Performing fine tuning (S7-300, S7-400)](#performing-fine-tuning-s7-300-s7-400-1)
- [Performing tuning manually (S7-300, S7-400)](#performing-tuning-manually-s7-300-s7-400-1)

### Interconnecting TUN_ES with controller (S7-300, S7-400)

The TUN_ES instruction is used to tune a step controller. Depending on the controller, you interconnect TUN_ES with one of the following instructions:

| Controller | Instruction |
| --- | --- |
| FM 355 S step controller | PID_FM |
| FM 455 S step controller | PID_FM |
| PID Basic Functions | CONT_S  TCONT_S |
| Standard PID Control (optional package) | PID_ES |
| Modular PID Control (optional package) | PID  LMNGEN_S |

Interconnect the input and output parameters of the TUN_ES instruction with the instruction of the controller.

| TUN_ES | PID_FM | CONT_S | TCONT_S | PID_ES |
| --- | --- | --- | --- | --- |
| PV | PV | PV | PV | PV |
| LMNR | LMN_A | -- | -- | LMNR_IN |
| NORM_FAC | -- | -- | -- | (NM_PVHR-NM_PVLR)*0.01 |
| C_LMNUP | QLMNUP | QLMNUP | QLMNUP | QLMNUP |
| C_LMNDN | QLMNDN | QLMNDN | QLMNDN | QLMNDN |
| LMNR_HS | QLMNR_HS | LMNR_HS | LMNR_HS | LMNR_HS |
| LMNR_ON | QLMNR_ON | -- | -- | LMNR_ON |
| WRITE_DIS | OR operation from LOAD_OP and LOAD_PAR | -- | -- | -- |
| MAN_OUT | LMN_RE | -- | -- | MAN |
| SP_OUT | SP_RE | SP_INT | SP_INT | SP_INT or  SP_EXT |
| GAIN | GAIN | GAIN | GAIN | GAIN |
| TI | TI | TI | TI | TI |
| TD | TD | -- | -- | TD |
| TM_LAG | TM_LAG | -- | -- | TM_LAG |
| MTR_TM | MTR_TM | MTR_TM | MTR_TM | MTR_TM |
| DEADB_W | DEADB_W | DEADB_W | DEADB_W | DEADB_W |
| PHASE | -- | -- | -- | PHASE |
| QMAN_ON | LMN_REON | -- | -- | MAN_ON |
| QLMNS_ON | LMNSOPON | LMNS_ON | LMNS_ON | LMNS_ON |
| QLMNUP | LMNUP_OP | LMNUP | LMNUP | LMNUP |
| QLMNDN | LMNDN_OP | LMNDN | LMNDN | LMNDN |
| QI_SEL | -- | -- | -- | I_SEL |
| QD_SEL | -- | -- | -- | D_SEL |
| QWRITE | LOAD_PAR and  LOAD_OP | -- | -- | -- |

---

**See also**

[Mode of operation TUN_ES (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_es-s7-300-s7-400)
  
[TUN_ES (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#tun_es-s7-300-s7-400)

### Tuning options (S7-300, S7-400)

#### Pretuning

The PID parameters are tuned during the heating process. During this tuning, process identification with subsequent controller design is carried out.

You can request pretuning with ADAPT1ST.

If you set ADAPT1ST = TRUE, then ADAPT_ON = TRUE and the valve are closed (PHASE = 1).

When ADAPT1ST = TRUE , the initialization routine of the TUN_ES instruction is run. The following pre-assignments are made:

- The system switches to PI controller. The parameters of PI_CON are transferred to the controller for this purpose. If the PI_CON.GAIN and PI_CON.TI parameters both have the value 0.0, they are pre-assigned with PI_CON.GAIN = 1.5 and PI_CON.TI = 3600.0 s.
- PROCESS.GAIN = 999.0
- STATUS_H = 0; STATUS_D = 0

  > **Note**
  >
  > Unless explicitly required, do **not** call TUN_ES during a warm restart of the CPU in its initialization routine as is usual for other instructions. If you do, all process parameters will be lost.

After a setpoint jump ≥ MIN_STEP, the motor transition time is measured after which pretuning is carried out. For process excitation during pretuning, TUN_ES uses the LHLM_TUN parameter for the manipulated variable jump. In the case of step controllers with position feedback, the value LHLM_TUN is approached directly. In the case of step controllers without position feedback, the control valve is opened completely and then moved back toward the closed position until the fraction of the motor transition time specified by (100 - LHLM_TUN) has elapsed.

Pretuning with measurement of motor transition time for step controller without position feedback

![Pretuning](images/26297481611_DV_resource.Stream@PNG-en-US.png)

#### Fine tuning

You can use ADAPT_ON to start the tuning only for step controllers with position feedback. TUN_ES uses old process values to determine whether pretuning without measurement of the motor transition time or fine tuning will be performed. Tuning is started with ADAPT_ON = TRUE and a subsequent setpoint jump ≥ MIN_STEP in the positive direction. TUN_ES then immediately enters PHASE = 2 and performs a manipulated variable jump to LHLM_TUN in the case of pretuning or to an automatically calculated manipulated variable in the case of fine tuning.

As a rule, the setpoint jump changes from the setpoint of the cold process (ambient temperature) to a point close to the operating point during pretuning. Any setpoint can be used as the initial state as long as it is ensured that it is a steady state. You are not permitted to specify any further setpoint jumps during tuning.

#### Starting tuning

You can start tuning from either automatic mode or manual mode:

- **Starting tuning from automatic mode**

  In automatic mode, set ADAPT_ON or ADAPT1ST = TRUE and specify a setpoint jump ≥ MIN_STEP.
- **Starting tuning from manual mode**

  In manual mode, set ADAPT_ON or ADAPT1ST = TRUE and specify a setpoint jump ≥ MIN_STEP. You must then reset MAN_ON = FALSE in order for the setpoint jump to become effective and tuning to begin.

#### Canceling tuning

To cancel the tuning before the setpoint jump, you must set ADAPT_ON = FALSE . To cancel the tuning after the setpoint jump (PHASE 2 or 3), you must switch to manual mode (MAN_ON = TRUE or LMNS_ON = TRUE).

By setting ADAPT_ON or ADAPT1ST during active tuning (PHASE 2 or 3), the tuning is not canceled but is instead completed. Because ADAPT_ON or ADAPT1ST is not reset, tuning is restarted once the start conditions are met.

### Tuning phases (S7-300, S7-400)

Individual phases are run through during controller tuning. You can read these phases at the PHASE parameter.

#### PHASE = 0

When an instance DB for TUN_ES is created, the PHASE parameter is preassigned with zero and LMNS_ON with TRUE. For this reason, the system switches to manual mode (PHASE = 7) after the first cycle. You can start the pretuning directly from manual mode (ADAPT_ON = TRUE) or switch to automatic mode. When you switch to automatic mode MAN_ON = FALSE for the first time, the parameters of PI_CON are applied. The default values for GAIN and TI are: GAIN = 1.5, TI = 1h.

#### PHASE = 1

After tuning has been started with ADAPT1ST = TRUE, TUN_ES closes the control valve (manipulated variable = 0 or LMNS_ON = LMNDN = TRUE) and waits for a positive setpoint jump ≥ MIN_STEP.

#### PHASE = 2

As soon as you specify a setpoint jump ≥ MIN_STEP in the positive direction toward the operating point of the warm process state, LHLM_TUN is assigned to MAN_OUT in the case of pretuning and a value calculated by TUN_ES is assigned to MAN_OUT in the case of fine tuning. MIN_STEP should be greater than 10% of the operating range of the setpoint and process value.

In the case of step control with position feedback (LMNR_ON=TRUE), the value TRUE is assigned to QMAN_ON. The controller controls the valve to the value of MAN_OUT, and TUN_ES calculates the motor transition time MTR_TM.

In the case of step control without position feedback, QLMNS_ON and QLMNUP are set to TRUE, and the valve is moved to the high endstop position. When the high endstop is reached (LMNR_HS =TRUE), TUN_ES calculates the motor transition time and forwards it to the controller. The valve is then moved toward the closed position until the value of MAN_OUT is reached (QLMNDN = TRUE).

#### PHASE = 3

When the point of inflection of the jump response is recognized (STATUS_H = 2) or when the process value has reached 70% of the setpoint jump height (STATUS_H = 3), a PI controller with conservative settings is designed. The controller gain GAIN is limited to the range from 0.2 to 20.0. As of this point, the controller immediately starts working as a PI controller and attempts to bring the controlled system to a steady-state condition. TUN_ES stores the newly determined PI controller parameters in GAIN, TI, and PI_CON. The previous values of the PI controller are saved in PI_CON_OLD. If it takes a long time to reach steady-state condition (creeping transient response during temperature processes), you can set STEADY = TRUE to initiate controller design with the current data when steady-state condition is almost reached. You can also set STEADY = TRUE to re-initiate the controller design with the current data at a later stage in PHASE = 3 or PHASE = 4. This will often provide some additional improvement to the controller design.

If an overshoot occurs or if no point of inflection is found, the manipulated variable jump size LHLM_TUN selected for pretuning may have been too large. This does not necessarily result in poor controller tuning. For the next pretuning, the value you select for LHLM_TUN should be approximately 20% smaller.

When TUN_ES has recognized steady-state condition or when time 30 × TI (TI: integral action time of the PI controller set in PHASE = 3) has elapsed since the setpoint jump, the controller design is improved and the system switches to PHASE = 4. TUN_ES stores the newly determined PI/PID controller parameters in GAIN, TI, TD, and PI_CON or PID_CON. The previous values of the PID controller are saved in PID_CON_OLD. If possible, a PID controller and a PI controller are designed. If PID_ON = TRUE, the PID controller is activated, otherwise the PI controller is activated. For complicated processes, TUN_ES always designs a PI controller, irrespective of PID_ON. GAIN is limited in such a way that the loop gain of the open loop (product of GAIN and process gain) is less than 40.0.

#### PHASE = 4

In this phase, the controller controls using its tuned parameters. From this state, you can start a fine tuning or a pretuning.

You can switch bumplessly between the PI controller and PID controller at any time.

---

**See also**

[Scope of TUN_ES (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#scope-of-tun_es-s7-300-s7-400)
  
[Mode of operation TUN_ES (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_es-s7-300-s7-400)

### Performing pretuning (S7-300, S7-400)

The controller parameters are pretuned during the heating process. During this tuning, process identification with subsequent controller design is carried out.

#### Requirements

- The instruction and the technology object are loaded on the CPU.
- TUN_ES is interconnected with a step controller.
- MAN_ON = FALSE
- The controller is in automatic mode.
- The process is in steady-state condition.

#### Procedure

To determine the optimal PID parameters during initial commissioning, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value, and manipulated variable are recorded.
2. Select "Pretuning" from the "Mode" drop-down list.

   TUN_ES is ready for tuning.
3. Choose a controller structure.
4. In the "Manipulated variable" field, enter a manipulated variable to be used until the transition to PHASE = 3.
5. Enter a new setpoint. The setpoint jump must be ≥ MIN_STEP.
6. Click the "Start tuning" icon.

   The pretuning starts. The status of the tuning is displayed.

---

**See also**

[Mode of operation TUN_ES (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_es-s7-300-s7-400)

### Performing fine tuning (S7-300, S7-400)

For step controllers with position feedback, you can start fine tuning.  The controller can be fine tuned online during a positive setpoint jump when there is a change from one operating point to another or when there are changes in the process response.

#### Requirements

- The instruction and the technology object are loaded on the CPU.
- TUN_ES is interconnected with a step controller.
- MAN_ON = FALSE
- LMNR_ON = TRUE for the TUN_ES instruction and the controller.
- The controller is in automatic mode.
- The process is in steady-state condition.

#### Procedure

To determine the optimal PID parameters during initial commissioning, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value, and manipulated variable are recorded.
2. Select "Fine tuning" from the "Mode" list.

   TUN_ES is ready for tuning.
3. Choose a controller structure.
4. Enter a new setpoint. The setpoint jump must be ≥ MIN_STEP.
5. Click the "Start tuning" icon.

   Fine tuning starts. The manipulated variable is determined by TUN_ES. The status of the tuning is displayed.

### Performing tuning manually (S7-300, S7-400)

You can manually change the PID parameters if oscillations occur or overshoots following setpoint jump changes are present in the closed control loop after pretuning or fine tuning. For example, you can reset the controller gain GAIN to 80% of the original value and the integral action time TI to 150% of the original setting.

#### Requirements

- The instruction and the technology object are loaded on the CPU.
- TUN_ES is interconnected with a step controller.
- MAN_ON = FALSE
- The controller is in automatic mode.
- The process is in steady-state condition.

#### Procedure

To manually determine the optimal PID parameters, follow these steps:

1. Click the "Start" icon.

   If there is no online connection, this will be established. The current values for the setpoint, process value, and manipulated variable are recorded.
2. Select "Manual" from the "Mode" list.
3. Choose a controller structure.
4. Enter new PID parameters in the "P", "I" and "D" fields.
5. Click the "Send parameters to the controller" icon in the "Tuning" group.
6. Select the "Change setpoint" check box in the "Current values" group.
7. Enter a new setpoint and click the ![Procedure](images/13477958795_DV_resource.Stream@PNG-de-DE.png) icon in the "Current values" group.
8. Clear the "Manual mode" check box, if necessary.

   The controller works with the new PID parameters and controls to the new setpoint.
9. Check the quality of the PID parameters based on the trend characteristics.
10. Repeat steps 3 to 9 until you are satisfied with the controller results.

---

**See also**

[Mode of operation TUN_ES (S7-300, S7-400)](PID%20Self%20Tuner%20%28S7-300%2C%20S7-400%29.md#mode-of-operation-tun_es-s7-300-s7-400)
