---
title: "Technological functions"
package: ReadMeTFenUS
topics: 4
devices: [S7-1200, S7-1500, S7-1500T, S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Technological functions

This section contains information on the following topics:

- [Notes on Motion Control (S7-1200, S7-1500, S7-1500T)](Notes%20on%20Motion%20Control%20%28S7-1200%2C%20S7-1500%2C%20S7-1500T%29.md#notes-on-motion-control-s7-1200-s7-1500-s7-1500t)
- [Notes on additional technology functions (S7-1500)](#notes-on-additional-technology-functions-s7-1500)
- [Notes on other technology functions (S7-1200)](#notes-on-other-technology-functions-s7-1200)
- [Notes on technological functions (S7-300, S7-400)](#notes-on-technological-functions-s7-300-s7-400)
- SIMATIC STEP 7 Easy Motion Control
- SIMATIC STEP 7 PID Professional

## Notes on additional technology functions (S7-1500)

### Parameters of the technology objects in TIA Portal Openness

You can find a list of the available technology object parameters in the product information "Parameters of the technology objects in TIA Portal Openness" on the [internet](https://support.industry.siemens.com/cs/ww/en/view/109744932).

### S_USSI on S7‑1500

Note the following when using the instruction S_USSI of the distributed I/O ET 200S 1SI on an S7‑1500.

The parameter ANZ shows the value 0 even in the case of an error.

If the CPU is switched to stop with the S_USSI instruction, check all possible errors listed at the parameter ANZ.

### PtP module with CM 1243-5 PROFIBUS Master

You have to make the following settings in the instance DB of the instructions when using the PtP modules CM PtP RS232 BA, CM PtP RS422/485 BA, CM PtP RS232 HF, CM PtP RS422/485 HF and CM PtP with a CM 1243-5 PROFIBUS Master with firmware ≤ V1.3.4:

- **Send_P2P**

  max_record_len = 240
- **Modbus_Master**

  Send_P2P.max_record_len = 240
- **Modbus_Slave**

  Send_P2P.max_record_len = 240

### PID_Temp on CPU 1500 V1.7

Note the following when using PID_Temp on a CPU 1500 with firmware version V1.7:

- The integrated dead zone in PID_Temp must not be used on CPU 1500 V1.7.

  Do not change the preset 0.0 of the associated parameters Retain.CtrlParams.Heat.DeadZone and Retain.CtrlParams.Cool.DeadZone.
- If the cooling output is active (PidOutputSum < 0.0, OutputCool <> 0.0) for a closed loop controller with active cooling and PID parameter switchover (Config.ActivateCooling = TRUE, Config.AdvancedCooling = TRUE) while "Pretuning cooling" is started (Mode = 1, Heat.EnableTuning = FALSE, Cool.EnableTuning = TRUE), aborts with error ErrorBits = 16#0040_0000.

  - In this case use "Fine tuning cooling" (Mode = 2, Heat.EnableTuning = FALSE, Cool.EnableTuning = TRUE)

  or

  - Before starting the pretuning, switch to manual mode with a manual value larger than 0.0 (Mode = 4, ManualValue ≥ 0.0).

As of firmware version V1.8, these two restrictions no longer apply.

## Notes on other technology functions (S7-1200)

### PtP modules with CM 1243-5 PROFIBUS Master

You have to make the following settings in the instance DB of the instructions when using the PtP modules CM PtP RS232 BA, CM PtP RS422/485 BA, CM PtP RS232 HF, CM PtP RS422/485 HF and CM PtP with a CM 1243-5 PROFIBUS Master with firmware ≤ V1.3.4:

- **Send_P2P**

  max_record_len = 240
- **Modbus_Master**

  Send_P2P.max_record_len = 240
- **Modbus_Slave**

  Send_P2P.max_record_len = 240

## Notes on technological functions (S7-300, S7-400)

### Parameter assignment for the FM x51 and FM x52

In contrast to the information in the Online Help, if you change the measuring system, the previously entered parameter values are not converted to the new measuring system.

### Programming FM x50-1, FM x51 and FM x52

The "initial values" specified in the parameter tables in the online help regarding the instructions correspond to the "default value" in the software interface of the user programming.

### IM 174 migration

During the migration of projects with IM 174, the parameter assignment of IM 174 is set to default values. It is absolutely necessary to set parameters for IM 174 again after the migration.
