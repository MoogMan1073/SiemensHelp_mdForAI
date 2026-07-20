---
title: "Using modular PID control (S7-300, S7-400)"
package: TFTOPIDModenUS
topics: 20
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using modular PID control (S7-300, S7-400)

This section contains information on the following topics:

- [Scope of Modular PID Control functions (S7-300, S7-400)](#scope-of-modular-pid-control-functions-s7-300-s7-400)
- [Basic steps for setting up a controller FB (S7-300, S7-400)](#basic-steps-for-setting-up-a-controller-fb-s7-300-s7-400)
- [Programming the controller FB (S7-300, S7-400)](#programming-the-controller-fb-s7-300-s7-400)
- [Complex controller structures (S7-300, S7-400)](#complex-controller-structures-s7-300-s7-400)
- [Commissioning the controller FB (S7-300, S7-400)](#commissioning-the-controller-fb-s7-300-s7-400)

## Scope of Modular PID Control functions (S7-300, S7-400)

In many control tasks, the classic PID controller which controls the processes is not the only key element. Complex signal processing is also required.

Modular PID Control includes instructions with functions for processing the process value and setpoint and calculating and tuning the manipulated variable.

The following controllers are possible:

- Continual controller
- Step controller for actuators with integrating behavior
- Pulse controller

You can implement controllers for different applications by connecting individual instructions.

- Fixed value controller
- Cascade controller
- Ratio controller
- Mixing controller
- Split range controller
- Override controller
- Controller with disturbance variable processing
- Multi-variable controller

Both slow (temperature, filling levels etc.) and fast controlled systems (flow, pressure, etc.) can be controlled.

You can call multiple control loops equidistantly but with different sampling intervals using the instruction LP_SCHED_M. You alter the sampling time of the control loop in accordance with the slowness of the controlled system.

This ensures the even distribution of the CPU load.

Use the PID Self-Tuner to commission and fine-tune the PID parameters.

## Basic steps for setting up a controller FB (S7-300, S7-400)

### Basic procedure for programming a controller

You program a controller as the function block (controller FB), for example with STL. Your controller FB must have at least the following parameters:

- Input parameter COM_RST
- Input parameter CYCLE
- Input parameter for setpoint
- Input parameter for process value
- Output parameter for the manipulated variable
- In/out parameter for the manual output value (continual controller)

Depending on controller requirements, you can also set the following parameters

- Input parameter for position feedback (step controller)
- Input parameter for disturbance variable
- Output parameter for the processed process value
- Output parameter for the processed setpoint
- Output parameter for limit violation

The details of how to set the inputs and outputs depend on your specific situation, for example on whether the process value is in I/O or floating-point format, on the type of position feedback, etc.

Call the Modular PID Control instructions in the controller FB and connect the input and output parameters. Call the controller FB you have created, for example in OB 100 or in a cyclic interrupt OB.

The following steps are needed to program a controller with Modular PID Control.

| Step | Description |
| --- | --- |
| 1. | [Processing setpoints](#processing-setpoints-s7-300-s7-400) |
| 2. | [Processing the process value](#processing-the-process-value-s7-300-s7-400) |
| 3. | [Generating and processing the control deviation](#generating-and-processing-the-control-deviation-s7-300-s7-400) |
| 4. | [Applying the disturbance variable](#applying-the-disturbance-variable-s7-300-s7-400) (optional) |
| 5. | Calculating the manipulated variable  - [Creating a continual controller](#creating-a-continual-controller-s7-300-s7-400) - [Creating a pulse controller](#creating-a-pulse-controller-s7-300-s7-400) - [Creating a step controller](#creating-a-step-controller-s7-300-s7-400) |
| 6. | [Processing position feedback](#processing-position-feedback-s7-300-s7-400) |

---

**See also**

[Processing setpoints (S7-300, S7-400)](#processing-setpoints-s7-300-s7-400)
  
[Processing the process value (S7-300, S7-400)](#processing-the-process-value-s7-300-s7-400)
  
[Generating and processing the control deviation (S7-300, S7-400)](#generating-and-processing-the-control-deviation-s7-300-s7-400)
  
[Applying the disturbance variable (S7-300, S7-400)](#applying-the-disturbance-variable-s7-300-s7-400)
  
[Creating a continual controller (S7-300, S7-400)](#creating-a-continual-controller-s7-300-s7-400)
  
[Creating a pulse controller (S7-300, S7-400)](#creating-a-pulse-controller-s7-300-s7-400)
  
[Creating a step controller (S7-300, S7-400)](#creating-a-step-controller-s7-300-s7-400)
  
[Processing position feedback (S7-300, S7-400)](#processing-position-feedback-s7-300-s7-400)

## Programming the controller FB (S7-300, S7-400)

This section contains information on the following topics:

- [Processing setpoints (S7-300, S7-400)](#processing-setpoints-s7-300-s7-400)
- [Processing the process value (S7-300, S7-400)](#processing-the-process-value-s7-300-s7-400)
- [Generating and processing the control deviation (S7-300, S7-400)](#generating-and-processing-the-control-deviation-s7-300-s7-400)
- [Applying the disturbance variable (S7-300, S7-400)](#applying-the-disturbance-variable-s7-300-s7-400)
- [Creating a continual controller (S7-300, S7-400)](#creating-a-continual-controller-s7-300-s7-400)
- [Creating a pulse controller (S7-300, S7-400)](#creating-a-pulse-controller-s7-300-s7-400)
- [Creating a step controller (S7-300, S7-400)](#creating-a-step-controller-s7-300-s7-400)
- [Processing position feedback (S7-300, S7-400)](#processing-position-feedback-s7-300-s7-400)

### Processing setpoints (S7-300, S7-400)

#### Instructions for processing the setpoint

You can use the following instructions:

- SP_GEN: Enter setpoint manually
- ROC_LIM: Limit rate of change
- LAG1ST: Smooth setpoint
- NONLIN: Linearize setpoint
- LIMITER: Limit setpoint
- RMP_SOAK: Specify setpoint according to ramp/soak
- SCALE_M: Scale setpoint
- NORM: Normalize setpoint

#### Example of setpoint processing

It should be possible to increase or decrease a specified setpoint manually. The rate of change is limited to prevent jumps in the setpoint.

Proceed as follows to process the setpoint as described in the example:

1. At the controller FB, in this case PIDCTR, declare an input parameter SP_IN of the data type "Real".
2. Connect SP_IN to a variable containing the required setpoint.
3. Call the instruction SP_GEN as a multi-instance in the controller FB and connect SP_IN to SP_GEN.DF_OUTV.
4. Assign parameters for the high and low setpoint limit in the SP_GEN_Instance structure of the multi-instance.
5. Call the instruction ROC_LIM as a multi-instance in the controller FB and connect SP_GEN.OUTV to ROC_LIM.INV via a temporary variable.
6. Assign parameters for the maximum rates of change in the ROC_LIM_Instance structure of the multi-instance.
7. To generate the control deviation, subtract the processed process value from ROC_LIM.OUTV or connect ROC_LIM.OUTV to ERR_MON.SP.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB PIDCTR.

![Example of setpoint processing](images/34981369867_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Processing the process value (S7-300, S7-400)](#processing-the-process-value-s7-300-s7-400)
  
[Description SP_GEN (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-sp_gen-s7-300-s7-400)
  
[Description ROC_LIM (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-roc_lim-s7-300-s7-400)
  
[Description LAG1ST (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-lag1st-s7-300-s7-400)
  
[Description NONLIN (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-nonlin-s7-300-s7-400)
  
[Description LIMITER (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-limiter-s7-300-s7-400)
  
[Description RMP_SOAK (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-rmp_soak-s7-300-s7-400)
  
[Description SCALE_M (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-scale_m-s7-300-s7-400)
  
[Description NORM (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-norm-s7-300-s7-400)

### Processing the process value (S7-300, S7-400)

#### Instructions for processing the process value

You can use the following instructions:

- CRP_IN: Scale I/O value
- LAG1ST: Smooth process value
- LIMITER: Limit process value
- LIMALARM: Monitor process value
- NONLIN: Linearize process value
- SCALE_M: Scale process value
- NORM: Normalize process value

#### Example of process value processing

The process value is in I/O format and is to be monitored to ensure compliance with the process value limits.

Proceed as follows to process the process value as described in the example:

1. At the controller FB, in this case PIDCTR, declare an input parameter PV_PER of the data type "Word".
2. Connect PV_PER to the I/O input at which the process value is measured.
3. Call the instruction CRP_IN as a multi-instance in the controller FB, for example with the name CRP_IN_Instance_PV.
4. Connect PV_PER to CRP_IN.INV_PER.
5. Assign parameters for factor and offset for scaling in the CRP_IN_Instance_PV structure of the multi-instance.
6. Call the instruction LIMALARM as a multi-instance in the controller FB and connect CRP_IN.OUTV to LIMALARM.INV via a temporary variable.
7. Assign parameters for the process value limits in the LIMALARM_Instance structure of the multi-instance.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB PIDCTR.

![Example of process value processing](images/34980431371_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Processing setpoints (S7-300, S7-400)](#processing-setpoints-s7-300-s7-400)
  
[Generating and processing the control deviation (S7-300, S7-400)](#generating-and-processing-the-control-deviation-s7-300-s7-400)
  
[Description CRP_IN (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-crp_in-s7-300-s7-400)
  
[Description LAG1ST (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-lag1st-s7-300-s7-400)
  
[Description LIMITER (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-limiter-s7-300-s7-400)
  
[Description LIMALARM (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-limalarm-s7-300-s7-400)
  
[Description NONLIN (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-nonlin-s7-300-s7-400)
  
[Description SCALE_M (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-scale_m-s7-300-s7-400)
  
[Description NORM (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-norm-s7-300-s7-400)

### Generating and processing the control deviation (S7-300, S7-400)

#### Establishing and limiting the control deviation

There are two ways to establish the control deviation. Either program the subtraction of the process value from the setpoint, or use the instruction ERR_MON. The instruction ERR_MON already includes control deviation monitoring.

#### Instructions for processing the control deviation

You can use the following instructions:

- A_DEAD_B: Route control deviation through adaptive deadband
- DEADBAND: Route control deviation through deadband

#### Example of subtraction

The control deviation is produced by subtraction and routed through a deadband.

Proceed as follows to determine the control deviation as described in the example:

1. Call the instruction DEADBAND as multi-instance and connect DEADBAND.INV to the difference between setpoint and process value, e.g. ROC_LIM.OUTV - CRP_IN.OUTV.
2. Assign parameters for the deadband width and a deadband displacement in the DEADBAND_Instance structure of the multi-instance.

   The processed control deviation is output at DEADBAND.OUTV.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB PIDCTR.

![Example of subtraction](images/34981664267_DV_resource.Stream@PNG-de-DE.png)

#### Example of the use of ERR_MON

The control deviation is calculated and monitored with the instruction ERR_MON.

Proceed as follows to determine the control deviation as described in the example:

1. Call the ERR_MON instruction as a multi-instance.
2. Using temporary variables, connect the processed setpoint to ERR_MON.SP, e.g. ROC_LIM.OUTV, and the processed process value to ERR_MON.PV, e.g. CRP_IN.OUTV.

   The control deviation is output at ERR_MON.ER.
3. Assign parameters for control deviation monitoring in the ERR_MON_Instance structure of the multi-instance.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB PIDCTR_ER.

![Example of the use of ERR_MON](images/34981893515_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Processing the process value (S7-300, S7-400)](#processing-the-process-value-s7-300-s7-400)
  
[Applying the disturbance variable (S7-300, S7-400)](#applying-the-disturbance-variable-s7-300-s7-400)
  
[Description A_DEAD_B (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-a_dead_b-s7-300-s7-400)
  
[Description DEADBAND (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-deadband-s7-300-s7-400)
  
[Description ERR_MON (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-err_mon-s7-300-s7-400)

### Applying the disturbance variable (S7-300, S7-400)

#### Instructions for processing the disturbance variable

You can use the following instructions:

- CRP_IN: Scale I/O value
- DIF: Respond to fast changes
- LAG1ST: Filter disturbances
- NON_LIN: Linearize disturbance variable
- SCALE_M: Scale disturbance variable
- NORM: Normalize disturbance variable

#### Example of disturbance variable processing

The disturbance variable is in I/O format. The signal is to be smoothed and linearized with a characteristic curve.

Proceed as follows to process the disturbance variable as described in the example:

1. At the controller FB, declare an input parameter DISV_PER of the data type "Word".
2. Connect DISV_PER to the I/O input at which the disturbance variable is measured.
3. Call the instruction CRP_IN as a multi-instance in the controller FB, for example with the name CRP_IN_Instance_DISV.
4. Connect DISV_PER to CRP_IN.INV_PER.
5. Assign parameters for factor and offset for scaling in the CRP_IN_Instance_DISV structure of the multi-instance.
6. Call the instruction LAG1ST as a multi-instance in the controller FB and connect CRP_IN.OUTV to LAG1ST.INV via a temporary tag.
7. Assign parameters for the time delay in the LAG1ST_Instance structure of the multi-instance.
8. Call the instruction NONLIN as a multi-instance in the controller FB and connect LAG1ST.OUTV to NONLIN.INV via a temporary tag.
9. Create a [Global data block DB_NONLIN](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-db_nonlin-s7-300-s7-400) in which you save the time slices of the characteristic curve.
10. Assign parameters for the number of the global data block with the characteristic curve in the NONLIN_Instance structure of the multi-instance.
11. The processed disturbance variable is output at NONLIN.OUTV.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB CTR_C_FF.

![Example of disturbance variable processing](images/34982060043_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Generating and processing the control deviation (S7-300, S7-400)](#generating-and-processing-the-control-deviation-s7-300-s7-400)
  
[Creating a continual controller (S7-300, S7-400)](#creating-a-continual-controller-s7-300-s7-400)
  
[Creating a pulse controller (S7-300, S7-400)](#creating-a-pulse-controller-s7-300-s7-400)
  
[Creating a step controller (S7-300, S7-400)](#creating-a-step-controller-s7-300-s7-400)
  
[Description CRP_IN (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-crp_in-s7-300-s7-400)
  
[Description DIF (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-dif-s7-300-s7-400)
  
[Description LAG1ST (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-lag1st-s7-300-s7-400)
  
[Description NONLIN (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-nonlin-s7-300-s7-400)
  
[Description SCALE_M (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-scale_m-s7-300-s7-400)
  
[Description NORM (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-norm-s7-300-s7-400)

### Creating a continual controller (S7-300, S7-400)

You will need the instructions PID, LMNGEN_C and CRP_OUT for a continual controller with an analog manipulated variable.

#### Procedure

Follow these steps to program a continual controller with an analog manipulated variable:

1. At the controller FB, declare an in/out parameter MAN of the data type "Real".

   You will require MAN to commission the controller with the PID Self-Tuner.
2. Call the instructions PID, LMNGEN_C and CRP_OUT as multi-instances in the controller FB.
3. At the controller FB, declare an in/out parameter MAN of the data type "Real" and connect MAN to LMNGEN_C.MAN.
4. Assign the parameters for the response of the control algorithm, e.g. whether the derivative action is used, in the PID_Instance structure of the controller DB.
5. Assign parameters for the manipulated value and rate of change limits, for example, in the LMNGEN_C_Instance structure of the multi-instance.
6. Assign parameters for the factor and offset for converting the floating-point value to I/O format in the CRP_OUT_Instance structure of the multi-instance.
7. Connect PID.ER to the control deviation via a temporary variable, e.g. ROC_LIM.OUTV - CRP_IN.OUTV or ERR_MON.ER.
8. If you are connecting a disturbance variable, connect PID.DISV to the processed signal of the disturbance variable, e.g. NONLIN.OUTV, using a temporary variable.
9. Connect the output parameter PID.PID_LMNG to the input parameter LMNGEN_C.PID_LMNG and the output parameter LMNGEN_C.LMNG_PID to the input parameter PID.LMNG_PID with the instruction BLKMOV.
10. Connect LMNGEN_C.LMN to CRP_OUT.INV using a temporary variable.
11. At the controller FB, declare an output parameter LMN_PER of the data type "Word" and connect CRP_OUT.OUTV to LMN_PER.
12. Connect LMN_PER to the analog output of the CPU which controls the actuator.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB CTR_C_FF .

![Procedure](images/34982380043_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Applying the disturbance variable (S7-300, S7-400)](#applying-the-disturbance-variable-s7-300-s7-400)
  
[Description PID (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-pid-s7-300-s7-400)
  
[Description LMNGEN_C (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-lmngen_c-s7-300-s7-400)
  
[Description CRP_OUT (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-crp_out-s7-300-s7-400)

### Creating a pulse controller (S7-300, S7-400)

For a pulse controller, you generate a continuous manipulated variable in floating-point format with the instructions PID and LMNGEN_C. On the basis of this continuous manipulated variable, you then generate a pulse train with pulse width modulation using the instruction PULSEGEN_M.

#### Generating a continuous manipulated variable in floating-point format

1. At the controller FB, in this case PIDCTR, declare an output parameter LMN of the data type "Real".
2. Call the instructions PID and LMNGEN_C as multi-instances in the controller FB.
3. Connect and assign parameters for PID and LMNGEN_C as described for the continual controller.
4. Connect LMNGEN_C.LMN to the output parameter LMN of the controller FB.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB PIDCTR.

![Generating a continuous manipulated variable in floating-point format](images/34982815243_DV_resource.Stream@PNG-de-DE.png)

#### Generating a pulse train

Follow these steps to generate a pulse train from the continuous manipulated variable:

1. Create a function, e.g. FC50, with the input parameters COM_RST and CYCLE.
2. Create a [Global data block for DB_LOOP](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-for-db_loop-s7-300-s7-400) in which to assign parameters for the cycle times for calling the controller FB and the pulse generator PULSEGEN_M.

   The ratio of cycle time of the controller FB call to PULSEGEN_M should be ≥ 20.
3. Call the LP_SCHED_M instruction in the function.
4. Connect LP_SCHED_M.DB_NBR to the global data block .
5. Call your controller FB, e.g. PIDCTR, if DB_LOOP.LOOP_DAT[1].ENABLE = TRUE.
6. Connect DB_LOOP.LOOP_DAT[1].COM_RST and DB_LOOP.LOOP_DAT[1].CYCLE to input parameters COM_RST and CYCLE of the controller FB.
7. Set DB_LOOP.LOOP_DAT[1].ENABLE = FALSE.
8. Call the instruction PULSEGEN_M if DB_LOOP.LOOP_DAT[2].ENABLE = TRUE.
9. Connect DB_LOOP.LOOP_DAT[2].COM_RST and DB_LOOP.LOOP_DAT[2].CYCLE to PULSEGEN_M.COM_RST and PULSEGEN_M.CYCLE.
10. Connect PULSEGEN_M.INV to the output parameter LMN of your controller FB.
11. Interconnect PULSEGEN_M.PER_TM with the input parameter CYCLE of your controller FB.
12. Set DB_LOOP.LOOP_DAT[2].ENABLE = FALSE.
13. Connect PULSEGEN_M.QPOS_P and, if necessary, PULSEGEN_M.QNEG_P to the digital outputs of the CPU which control the actuator.
14. Call the function in OB 100 and in the cyclic interrupt OB.

    ![Generating a pulse train](images/84101596555_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Applying the disturbance variable (S7-300, S7-400)](#applying-the-disturbance-variable-s7-300-s7-400)
  
[Description PID (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-pid-s7-300-s7-400)
  
[Description LMNGEN_C (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-lmngen_c-s7-300-s7-400)
  
[Description PULSEGEN_M (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-pulsegen_m-s7-300-s7-400)
  
[Description LP_SCHED_M (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-lp_sched_m-s7-300-s7-400)

### Creating a step controller (S7-300, S7-400)

You will require the instructions PID and LMNGEN_S for a step controller.

#### Procedure

Proceed as follows to program a step controller:

1. Call the instructions PID and LMNGEN_S as multi-instances in the controller FB.
2. Assign the parameters for the response of the control algorithm, e.g. whether the derivative action is used, in the PID_Instance structure of the multi-instance.
3. Assign parameters in the LMNGEN_S_Instance structure of the multi-instance, for example specify that no position feedback is to be used, to LMNR_ON = FALSE.
4. Connect PID.ER to the control deviation via a temporary variable, e.g. DEADBAND.OUTV or ERR_MON.ER.
5. If you are connecting a disturbance variable, connect PID.DISV to the processed signal of the disturbance variable, e.g. CRP_IN.OUTV, using a temporary variable.
6. Connect the output parameter PID.PID_LMNG to the input parameter LMNGEN_S.PID_LMNG and the output parameter LMNGEN_S.LMNG_PID to the input parameter PID.LMNG_PID with the instruction BLKMOV.
7. At the controller FB, declare the output parameters QLMNUP and QLMNDN of the data type "Bool".
8. Connect LNMGEN_S.QLMNUP and LMNGEN_S. QLMNDN to these output parameters.
9. Connect the output parameters of the controller FB to the digital outputs of the CPU which control the actuator.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB PIDCTR_S.

![Procedure](images/35014914955_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Applying the disturbance variable (S7-300, S7-400)](#applying-the-disturbance-variable-s7-300-s7-400)
  
[Processing position feedback (S7-300, S7-400)](#processing-position-feedback-s7-300-s7-400)
  
[Description PID (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-pid-s7-300-s7-400)
  
[Description LMNGEN_S (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-lmngen_s-s7-300-s7-400)

### Processing position feedback (S7-300, S7-400)

Position feedback configuration depends upon the actuator used.

- Actuator with analog position feedback
- Actuator with digital endstop signals

#### Requirement

You have already programmed a step controller.

#### Creating a step controller with analog position feedback

The following instructions are useful for processing analog position feedback.

- CRP_IN: Scale I/O value
- NONLIN: Linearize position feedback
- SCALE_M: Scale position feedback
- NORM: Normalize position feedback

**Example of analog position feedback**

An actuator provides position feedback in I/O format; this should to be factored into the manipulated variable calculation.

1. At the controller FB, declare an input parameter LMNR_PER of the data type "Word".
2. Connect LMNR_PER to the I/O input.
3. Call the instruction CRP_IN as a multi-instance in the controller FB, for example with the name CRP_IN_Instance_LMNR.
4. Connect LMNR_PER to CRP_IN.INV_PER.
5. Assign parameters for factor and offset for scaling in the CRP_IN_Instance_LMNR structure of the multi-instance.
6. Connect CRP_IN.OUTV to LMNGEN_S.LMNR_IN using a temporary variable.
7. Activate position feedback with LMNR_ON = TRUE in the LMNGEN_S_Instance structure of the multi-instance.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB PIDCTR_SAF.

![Creating a step controller with analog position feedback](images/35021237771_DV_resource.Stream@PNG-de-DE.png)

#### Creating a step controller with digital position feedback

1. At the controller FB, declare the input parameters LMNR_HS and LMNR_LS of the data type "Bool".
2. Connect the input parameters LMNR_HS and LMNR_LS to LMNGEN_S.LMNR_HS and LMNGEN_S.LMNR_LS.
3. Activate position feedback with LMNR_ON = TRUE in the LMNGEN_S_Instance structure.

The diagram below shows how the Modular PID Control instructions are called and connected in the controller FB PIDCTR_SDF.

![Creating a step controller with digital position feedback](images/35021620619_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Creating a step controller (S7-300, S7-400)](#creating-a-step-controller-s7-300-s7-400)
  
[Description CRP_IN (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-crp_in-s7-300-s7-400)
  
[Description NONLIN (S7-300, S7-400)](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#description-nonlin-s7-300-s7-400)

## Complex controller structures (S7-300, S7-400)

This section contains information on the following topics:

- [Single-loop ratio controller (S7-300, S7-400)](#single-loop-ratio-controller-s7-300-s7-400)
- [Multi-loop ratio controller (S7-300, S7-400)](#multi-loop-ratio-controller-s7-300-s7-400)
- [Cascade controller (S7-300, S7-400)](#cascade-controller-s7-300-s7-400)
- [Multi-variable controller (S7-300, S7-400)](#multi-variable-controller-s7-300-s7-400)

### Single-loop ratio controller (S7-300, S7-400)

The diagram below shows a typical control loop of a single-loop ratio controller.

![Figure](images/35002269707_DV_resource.Stream@PNG-en-US.png)

The ratio between two process values is adjusted to a defined setpoint with a PID algorithm.

#### Procedure

Proceed as follows to create a single-loop ratio controller:

1. Program process value processing as outlined below in your controller FB.
2. To avoid division by zero, you must limit the value range for the process value PV_PER2 to Values > Zero with the instruction LIMITER.

The diagram below shows a controller FB, in this case RATIOCTR, for a single-loop ratio controller with a continual manipulated variable.

![Procedure](images/34986969995_DV_resource.Stream@PNG-de-DE.png)

### Multi-loop ratio controller (S7-300, S7-400)

The diagram below shows a typical control loop for a multi-loop ratio controller.

![Figure](images/34985515787_DV_resource.Stream@PNG-en-US.png)

#### Programming a control loop

Follow these steps to program this example with Modular PID Control:

1. Program a controller FB for the master controller, e.g. PIDCTR_PV.
2. Program one or more controller FBs for the slave controllers, e.g. RB_CTR_S.
3. Program a function in which you can call and connect the four controllers.

#### Programming a master controller

Proceed as follows to program the master controller:

1. Program the master controller in line with your requirements as described in section [Programming the controller FB](#programming-the-controller-fb-s7-300-s7-400).
2. At the controller FB, in this case PIDCTR_PV, declare an output parameter PV of the data type "Real" at which you output the processed process value of the master controller.

The diagram below shows the master controller interconnection, using the controller FB PIDCTR_PV as an example.

![Programming a master controller](images/35021791755_DV_resource.Stream@PNG-de-DE.png)

#### Programming slave controllers

Proceed as follows to program the slave controllers:

1. Program the slave controllers in line with your requirements as described in section [Programming the controller FB](#programming-the-controller-fb-s7-300-s7-400).
2. At the controller FB, in this case RB_CTR_S, declare an input parameter RATIO_FAC of the data type "Int". The processed setpoint, e.g. SCALE.OUTV, of the slave controller is multiplied by this value.

The diagram below shows the slave controller interconnection, using the controller FB RB_CTR_S as an example.

![Programming slave controllers](images/34985539595_DV_resource.Stream@PNG-de-DE.png)

#### Calling and connecting controllers

Proceed as follows to call and connect master and slave controllers:

1. Create a function, e.g. FC50,, with the input parameters COM_RST and CYCLE.
2. Call the LP_SCHED_M instruction in the function.
3. Create a [Global data block for DB_LOOP](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-for-db_loop-s7-300-s7-400) in which to assign parameters for the number of controllers and the cycle times for calling the master controller and slave controller.

   The cycle times of the slave controllers must be shorter than or equal to the cycle time of the master controller.
4. Call the controller FB for the master controller, in this case PIDCTR_PV, if DB_LOOP.LOOP_DAT[1].ENABLE = TRUE.
5. Connect DB_LOOP.LOOP_DAT[1].COM_RST and DB_LOOP.LOOP_DAT[1].CYCLE to the input parameters COM_RST and CYCLE of the master controller.
6. Set DB_LOOP.LOOP_DAT[1].ENABLE = FALSE.
7. Call the controller FB for the first slave controller, in this case RB_CTR_S, if DB_LOOP.LOOP_DAT[2].ENABLE = TRUE.
8. Connect DB_LOOP.LOOP_DAT[2].COM_RST and DB_LOOP.LOOP_DAT[2].CYCLE to COM_RST and CYCLE of the slave controller.
9. Connect the output parameter PV of the master controller to the input parameter SP_IN of the slave controller.
10. Set DB_LOOP.LOOP_DAT[2].ENABLE = FALSE.
11. Repeat the last four steps for the two other slave controllers. Increase the array counter for each controller.
12. Connect the manipulated variables to the outputs of the CPU.
13. Call the function in OB 100 and in the cyclic interrupt OB.

The diagram below shows controller calls and interconnection, using the function FC50 as an example.

![Calling and connecting controllers](images/84101124107_DV_resource.Stream@PNG-de-DE.png)

### Cascade controller (S7-300, S7-400)

The diagram below shows a typical control loop for a cascade controller.

![Figure](images/34985559307_DV_resource.Stream@PNG-en-US.png)

#### Programming a control loop

Follow these steps to program this example with Modular PID Control:

1. Program a controller FB for the master controller, e.g. PIDCTR.
2. Program a controller FB for the slave controller, e.g. PIDCTR_SAF.
3. Program a function in which you can call and connect the two controllers.
4. Call the LP_SCHED_M instruction in the function.
5. Create a [Global data block for DB_LOOP](Modular%20PID%20Control%20%28S7-300%2C%20S7-400%29.md#global-data-block-for-db_loop-s7-300-s7-400) in which to assign parameters for the number of controllers and the cycle times for calling the master controller and slave controller.

   The cycle time of the slave controller must be less than or equal to the cycle time of the master controller.
6. Call the controller FB for the master controller if DB_LOOP.LOOP_DAT[1].ENABLE = TRUE.
7. Connect DB_LOOP.LOOP_DAT[1].COM_RST and DB_LOOP.LOOP_DAT[1].CYCLE to the input parameters COM_RST and CYCLE of the master controller.
8. Set DB_LOOP.LOOP_DAT[1].ENABLE = FALSE.
9. Call the controller FB for the slave controller if DB_LOOP.LOOP_DAT[2].ENABLE = TRUE.
10. Connect DB_LOOP.LOOP_DAT[2].COM_RST and DB_LOOP.LOOP_DAT[2].CYCLE to COM_RST and CYCLE of the slave controller.
11. Connect the output parameter LMN of the master controller to the input parameter SP_IN of the slave controller.
12. Set DB_LOOP.LOOP_DAT[2].ENABLE = FALSE.
13. Connect the manipulated variable of the slave controller to the analog output of the CPU which controls the actuator.
14. Call the function in OB 100 and in the cyclic interrupt OB.

The diagram below shows controller calls and interconnection, using the function FC50 as an example.

![Programming a control loop](images/84101010059_DV_resource.Stream@PNG-de-DE.png)

### Multi-variable controller (S7-300, S7-400)

The diagram below shows a typical control loop for a multi-variable controller. Two PID controllers with continuous output are switched to the process.

![Figure](images/34985591563_DV_resource.Stream@PNG-en-US.png)

#### Programming a control loop

Follow these steps to program this example with Modular PID Control:

1. At the controller FB, in this case MUL_CTR, declare the following input parameters:

   - COM_RST of the data type "Bool"
   - CYCLE of the data type "Time"
   - SP_IN1 and SP_IN2of the data type "Real"
   - PV_PER1 and PV_PER2 of the data type "Word"
2. At the controller FB, declare the output parameters LMN_PER1 and LMN_PER2 of the data type "Word".
3. Program setpoint and process value processing and calculation of the manipulated variable for both PID controllers.
4. To calculate the control deviation of the first PID controller, subtract the processed process value PV_PER1 from the product of the setpoint SP_IN1 and the manipulated variable of the second PID controller.
5. To calculate the control deviation of the second PID controller, subtract the processed process value PV_PER2 from the product of the setpointSP_IN2 and the manipulated variable of the first PID controller.
6. Connect the manipulated variables LMN_PER1 and LMN_PER2 to two analog outputs which control the actuators.
7. Call the controller FB in OB 100 and in the cyclic interrupt OB.

The diagram below shows the call, using the controller FB MUL_CTR as an example.

![Programming a control loop](images/34985603467_DV_resource.Stream@PNG-de-DE.png)

The diagram below shows the controller interconnection, using the controller FB MUL_CTR as an example.

![Programming a control loop](images/34985615371_DV_resource.Stream@PNG-de-DE.png)

## Commissioning the controller FB (S7-300, S7-400)

This section contains information on the following topics:

- [Commissioning the continual controller (S7-300, S7-400)](#commissioning-the-continual-controller-s7-300-s7-400)
- [Commissioning the step controller (S7-300, S7-400)](#commissioning-the-step-controller-s7-300-s7-400)

### Commissioning the continual controller (S7-300, S7-400)

You can commission your controller FB with the PID Self-Tuner and determine the optimum PID parameters.

#### Procedure

Proceed as follows to commission a continual controller or a pulse controller:

1. Call the controller FB in a cyclic interrupt OB and connect the input and output parameters.
2. Call the instruction TUN_EC in the same cyclic interrupt OB.
3. Connect the instruction TUN_EC to your controller FB as follows:

   - TUN_EC.PV to the processed process value, e.g. the static variable CRP_IN_Instance_PV.OUTV or the output parameter PV
   - TUN_EC.LMN to the manipulated variable in real format, e.g. the static variable LMNGEN_C_Instance.LMN
   - TUN_EC.MAN to the in/out parameter for the manual value, e.g. MAN.
   - TUN_EC.SP_OUT to the input parameter for the setpoint, e.g. SP_IN
   - TUN_EC.GAIN to the proportional gain, e.g. PID_Instance.GAIN
   - TUN_EC.TI to the integral action time, e.g. PID_Instance.TI
   - TUN_EC.TD to the derivative action time, e.g. PID_Instance.TD
   - TUN_EC.TM_LAG to the time delay, e.g. PID_Instance.TM_LAG
4. Click the "![Procedure](images/35383750539_DV_resource.Stream@PNG-de-DE.png)" icon in the TUN_EC instruction.

   The commissioning editor for TUN_EC opens. The operation of the commissioning editor is explained under PID Self-Tuner.

### Commissioning the step controller (S7-300, S7-400)

You can commission your controller FB with the PID Self-Tuner and determine the optimum PID parameters.

#### Procedure

Follow the steps below to commission a step controller:

1. Call the controller FB in a cyclic interrupt OB and connect the input and output parameters.
2. Call the instruction TUN_ES in the same cyclic interrupt OB.
3. Connect the instruction TUN_ES to your controller FB as follows:

   - TUN_ES.PV to the processed process value, e.g. the static variable CRP_IN_Instance _PV.OUTV or the output parameter PV
   - TUN_ES.LMNR_IN to the processed position feedback, e.g. LMNGEN_S_instance.LMNR_IN
   - TUN_ES.C_LMNUP and TUN_ES.C_LMNDN to the manipulated variable signals, e.g. the output parameters QLMN_UP and QLMNDN
   - TUN_ES.LMNR_HS to the high endstop signal, e.g. LMNGEN_S_Instance.LMNR_HS
   - TUN_ES.LMNR_ON to the position feedback switch, e.g. LMNGEN_S_Instance.LMNR_ON
   - TUN_ES.SP_OUT to the input parameter for the setpoint, e.g. SP_IN
   - TUN_ES.GAIN to the proportional gain, e.g. PID_Instance.GAIN
   - TUN_ES.TI to the integral action time, e.g. PID_Instance.TI
   - TUN_ES.TD to the derivative action time, e.g. PID_Instance.TD
   - TUN_ES.TM_LAG to the time delay, e.g. PID_Instance.TM_LAG
   - TUN_ES.MTR_TM to the motor transition time, e.g. LMNGEN_S_Instance.MTR_TM
   - If you are using a deadband, TUN_ES.DEADB_W to the deadband width, e.g. DEADBAND_Instance.OUTV
   - TUN_ES.QLMNUP and TUN_ES.QLMNDN to the manipulated variable signals LMNGEN_S_Instance.LMNUP and LMNGEN_S_Instance.LMNDN
4. Click the "![Procedure](images/35383750539_DV_resource.Stream@PNG-de-DE.png)" icon in the TUN_ES instruction.

   The commissioning editor for TUN_ES opens. The operation of the commissioning editor is explained under PID Self-Tuner.
