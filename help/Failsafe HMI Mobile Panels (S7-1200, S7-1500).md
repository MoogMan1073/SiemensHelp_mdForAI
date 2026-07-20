---
title: "Failsafe HMI Mobile Panels (S7-1200, S7-1500)"
package: FSHMIMobile1500enUS
topics: 11
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Failsafe HMI Mobile Panels (S7-1200, S7-1500)

This section contains information on the following topics:

- [Overview (S7-1200, S7-1500)](#overview-s7-1200-s7-1500)
- [Mobile Panel 277F IWLAN F-FB (S7-1200, S7-1500)](#mobile-panel-277f-iwlan-f-fb-s7-1200-s7-1500)
- [Mobile Panel 2nd Generation F-FB (S7-1200, S7-1500)](#mobile-panel-2nd-generation-f-fb-s7-1200-s7-1500)

## Overview (S7-1200, S7-1500)

This document describes the instructions for the following HMI devices:

- Mobile Panel 277F IWLAN, Mobile Panel 277F IWLAN V2, Mobile Panel 277F IWLAN (RFID tag)
- Mobile Panels 2nd Generation

## Mobile Panel 277F IWLAN F-FB (S7-1200, S7-1500)

This section contains information on the following topics:

- [Using F-FBs (S7-1200, S7-1500)](#using-f-fbs-s7-1200-s7-1500)
- [F_DB_STATES: Data exchange (S7-1200, S7-1500)](#f_db_states-data-exchange-s7-1200-s7-1500)
- [F_FB_MP: Mobile Panel status (S7-1200, S7-1500)](#f_fb_mp-mobile-panel-status-s7-1200-s7-1500)
- [F_FB_RNG_4, F_FB_RNG_16 (S7-1200, S7-1500)](#f_fb_rng_4-f_fb_rng_16-s7-1200-s7-1500)

### Using F-FBs (S7-1200, S7-1500)

#### Required F FBs

You must integrate the following fail-safe blocks in your safety program:

- For each HMI device: An F_FB_MP

  The assigned HMI device is monitored by this F FB.
- For each effective range: An F_FB_RNG_4 or alternatively an F_FB_RNG_16

  The assigned effective range is managed by this F FB.

  The number of HMI devices that should get permission to log onto the effective range determines the F FB that is called, F_FB_RNG_4 or F_FB_RNG_16:

  - F_FB_RNG_4 For a maximum of 4 HMI devices
  - F_FB_RNG_16 For a maximum of 16 HMI devices
- An F_DB_STATES with a WORD data type or a comparable address area in an available F DB.

  Using this F DB, data is exchanged between the F_FB_MP of the HMI deice and F_FB_RNG_n of the effective range.
- ESTOP1; with this block, you can ensure that the operator must first provide confirmation after an emergency stop before the plant can be restarted. You can find this block in the Distributed Safety F library in the F Application Blocks block container.

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Naming conventions for F-application blocks**  Ensure the following matches when changing the names of F application blocks:  - The symbolic name in the symbol table - The name in the object properties of the block (header) |  |

#### Rules for the safety program

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Emergency stop button not evaluated without F_FB_RNG**  The emergency stop button can only be evaluated if you call an F_FB_RNG_n in your safety program.  Always call an F_FB_RNG_n in your safety program, even if you do not use effective ranges in your plant. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Prohibited restart of the plant**  Once the emergency stop button has been triggered, the plant can only be restarted after operator acknowledgment. Use the FB F_ESTOP1 in your safety program to ensure acknowledgment by the operator. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Emergency stop button is evaluated with delayed**  If the cycle time for the OB 35 block (in conjunction with controllers of the type S7-300/400) or MAIN_SAFETY (in conjunction with controllers of the type S7-1500) is set too high, this can cause loss of frames and delayed evaluation of the output "E-STOP" of F_FB_RNG_n.   Set the cycle time lower than that for the PROFINET IO time. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Caution** |
| **Safety states not evaluated**  The safety states, such as a global rampdown, can only be evaluated if you call an F_FB_RNG_n in your safety program.  Always call an F_FB_RNG_n in your safety program, even if you do not use effective ranges in your plant. |  |

The F FBs used are called cyclically and in a specific order in the safety program. You need to call the F FBs in the following order in your safety program:

1. All F_FB_MP
2. All F_FB_RNG_n

The operator must always acknowledge errors, such as communication errors. You cannot use any automatic acknowledgment in your safety program, therefore.

#### Interconnection of the F FBs

The following figure is a schematic representation of the interconnection of F FBs to one another and to the PII and PIQ.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Direct evaluation of the process images not allowed**  You cannot directly evaluate the PII and PIQ in your program. |  |

![Interconnection of the F FBs](images/11415411979_DV_resource.Stream@PNG-de-DE.png)

#### Application example

You can find application examples in the [Internet](http://support.automation.siemens.com/WW/view/en/20229806/136000).

#### F I/O DB

An F I/O DB is automatically generated in HW Config for every F I/O.

The access to the F I/O and working with the F I/O DB is described in detail in the manual "[SIMATIC Safety - Configuration and Programming](http://support.automation.siemens.com/WW/view/en/54110126)", "F I/O Access" section.

---

**See also**

[F_DB_STATES: Data exchange (S7-1200, S7-1500)](#f_db_states-data-exchange-s7-1200-s7-1500)
  
[F_FB_MP: Mobile Panel status (S7-1200, S7-1500)](#f_fb_mp-mobile-panel-status-s7-1200-s7-1500)
  
[F_FB_RNG_4, F_FB_RNG_16 (S7-1200, S7-1500)](#f_fb_rng_4-f_fb_rng_16-s7-1200-s7-1500)

### F_DB_STATES: Data exchange (S7-1200, S7-1500)

#### Validity

This description applies to version 1.0 of the F_DB_STATES.

#### Functional description:

Using this F DB, data is exchanged between the F_FB_MP of the HMI device and the F_FB_RNG_n of the effective range. As a result, data cannot be exchanged directly between two F-FBs. In an F_DB_STATES, you can save the data for up to 126 HMI devices. One word of the data block is reserved for each HMI device.

#### Structure

The F_DB_STATES has the following structure:

| F_DB_STATES |  | Processing in F_FB_MP: | Processing in F_FB_RNG_n: |
| --- | --- | --- | --- |
| Word 1= MP 1 INT_STATUS | Bit 0 = State MP_Excluded | Written | Read |
| Bit 1 = State MP_Included | Written | Read |  |
| Bit 2 = State MP_CommError | Written | Read |  |
| Bit 3 = State MP_QuitCommError | Written | Read |  |
| Bit 8 = RNG_STAT | Read | Written |  |
| Bit 9 = RNG_BUSY | Read | Written |  |
| Bit 10 = RNG_OVER | Read | Written |  |
| Bit 11 = VALID_ID | Read | Written |  |

#### Cyclical use

The data of the F_DB_STATES are reset twice per cycle.

At the start of the cycle, the input INT_STAT of the F_FB_MP is set to the data of the F_DB_STATES. After processing of the F_FB_MP, the bit 0 to bit 3 of the F_DB_STATES will be supplied with the latest values of the F_FB_MP.

Then the input MPn_STAT assigned to the HMI device F_FB_RNG_n will be set to the data of the F_DB_STATES. After processing of the F_FB_RNG_n, the bit 8 to bit 11 of the F_DB_STATES will be supplied with the latest values of the F_FB_RNG_n.

The latest values will be read by the F_FB_MP and processed further in the next cycle.

---

**See also**

[Using F-FBs (S7-1200, S7-1500)](#using-f-fbs-s7-1200-s7-1500)
  
[F_FB_MP: Mobile Panel status (S7-1200, S7-1500)](#f_fb_mp-mobile-panel-status-s7-1200-s7-1500)
  
[F_FB_RNG_4, F_FB_RNG_16 (S7-1200, S7-1500)](#f_fb_rng_4-f_fb_rng_16-s7-1200-s7-1500)

### F_FB_MP: Mobile Panel status (S7-1200, S7-1500)

#### Inputs

| Parameters | Data type | Description | Interconnection |
| --- | --- | --- | --- |
| QBAD | Bool | QBAD indicates whether there is a passivation of the F-I/O. | F-I/O DB: DBx2.1 = QBAD |
| ACK_REQ | Bool | Acknowledgement required  After a communication error, the fail-safe system sets QBAD  =  1 and ACK_REQ = 0.  ACK_REQ = 1 indicates that the PROFIsafe message frames are being exchanged again. | F-I/O DB: DBx2.2 = ACK_REQ |
| S7_MP_RES | Bool | This input is set to reset the status of the F_FB_MP to its "original state" from the F-CPU.  - The HMI device has removed the status. - If a ramp-down or shutdown was set, it is not reset. - If the HMI device was logged on in the effective range, it is now released again.   The input is only evaluated if Q_BAD = 1.  Setting the input S7_MP_RES is necessary if the HMI device cannot return itself to a defined state, for example when an internal error occurs or the battery is discharged. | Must be specifically interconnected for plant.   The safety program must ensure that automatic restart of the plant is not possible after S7_MP_RES is set. The operator must strictly ensure that he executes a separate operator action to commence the restart. |
| S7_ACK_ERR | Bool | Communication errors may not be acknowledged automatically.  This input is set to have the F-CPU to acknowledge a communication error during ongoing PROFIsafe communication.   The F_FB_MP only responds to a rising edge. | Must be specifically interconnected for plant. |
| MP_DATA | Int | User data of the inputs of the F-process image | PII: Int 1 = MP_DATA |
| MP_RNG | Int | ID of the effective range in which the HMI device is located. | PII: Int 2 = MP_RNG |
| MP_STAT | Word | Data is exchanged with F_FB_RNG_n through this input/output via F_DB_STATES. | F_DB_STATES |

#### Outputs

| Parameters | Data type | Description | Interconnection |
| --- | --- | --- | --- |
| ACK_REI | Bool | Acknowledgement for reintegration  The automatic reintegration is regulated via the F-I/O DB through this output. | F-I/O DB: DBx0.2 = ACK_REI |
| MP_DATA_Q | Int | User data of the outputs of the F-process image: | PIQ:  Int 1 = MP_DATA |
| MP_RNG_Q | Int | This output transfers the effective range ID to the HMI device. | PIQ:  Int 2 = MP_RNG |
| DIAG | Word | Information about any occurring errors is provided through this output for servicing purposes.   Bit 0: HMI removed  Bit 1: HMI integrated  Bit 2: Communication error on the HMI device  Bit 3: Communication error must be acknowledged.  Bit 4 to bit 15: Reserved | You can evaluate the DIAG output in your program. |

#### Enable inputs EN and ENO

When you call a fail-safe block, the enable input EN and enable output ENO appear automatically.

Note the following:

- Do not connect these I/Os
- Do not supply these I/Os with "0"
- Do not evaluate these I/Os

#### Validity

This description applies to version 1.0 of the F_FB_MP.

> **Note**
>
> Insert the FC 176: F_BO_W and FC 177: F_W_BO blocks into your safety program as these blocks are called by F_FB_MP. You can find these blocks in the Distributed Safety F library in the F Application Blocks block container.

#### Wiring

You have to wire the inputs and outputs of the F-FB manually. No automatic wiring is performed.

#### Purpose

The assigned Mobile Panel 277F IWLAN HMI device is monitored with the F_FB_MP.

You need to use a separate F_FB_MP for each Mobile Panel 277F IWLAN.

The F_FB_MP performs the following tasks:

- The block integrates the HMI device in the safety program of the F-CPU after startup.
- The block removes the HMI device from the safety program after a communication error. As soon as the communication error has been corrected and the operator has acknowledged this, the block integrates the HMI device back into the safety program.
- The block sends the states of the HMI device to F_FB_RNG_n via F_DB_STATES.

  The following HMI device states are possible:

  - "Integrated"
  - "Removed"
  - "Communication error"
  - "Acknowledgement required"

The QBAD output of the F-I/O is monitored for integrating and removing the HMI device.

- QBAD = 0: PROFIsafe communication is taking place between the HMI device and the F-CPU.
- QBAD = 1: No PROFIsafe communication is not taking place between the HMI device and the F-CPU.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Inadmissible automatic restart of the plant**  The safety program must ensure that automatic restart of the plant is not possible after S7_MP_RES is set. The operator must strictly ensure that he executes a separate operator action to commence the restart. |  |

#### Addresses of PII and PIQ

You can find the start addresses of PII and PIQ in the PROFIsafe settings of the HMI device in HW Config.

---

**See also**

[Using F-FBs (S7-1200, S7-1500)](#using-f-fbs-s7-1200-s7-1500)
  
[F_DB_STATES: Data exchange (S7-1200, S7-1500)](#f_db_states-data-exchange-s7-1200-s7-1500)
  
[F_FB_RNG_4, F_FB_RNG_16 (S7-1200, S7-1500)](#f_fb_rng_4-f_fb_rng_16-s7-1200-s7-1500)

### F_FB_RNG_4, F_FB_RNG_16 (S7-1200, S7-1500)

FB162: Effective range for 4 Mobile Panel (F_FB_RNG_4) / FB 163 Effective range for 16 Mobile Panel (F_FB_RNG_16)

#### Inputs

| Parameters | Data type | Description | Interconnection |
| --- | --- | --- | --- |
| RNG_ID | Integer | Click on this input and enter the ID of the effective range to be monitored by F_FB_RNG_n. The RNG_ID must be unique throughout the plant and is set in WinCC flexible. | --- |
| OVERRIDE | Bool | 0 = "Override" mode inactive,  1 = "Override" mode active | Result of the link between the override switch and the protection mechanism |
| MPn_DATA* | Int | User data of the inputs of the fail-safe process image. | PII:  Int 1 = MP_DATA |
| MPn_RNG* | Int | ID of the effective range in which the HMI device is located. | PII:  Int 2 = MP_RNG |
| MPn_F_KEY* | Int | Reserved |  |
| MPn_STAT* | Word | Data is exchanged with F_FB_MP through this input/output via F_DB_STATES. | F_DB_STATES |
| *MPn is used as follows:  - With F_FB_RNG_4 for HMI device 1 to HMI device 4 - With F_FB_RNG_16 for HMI device 1 to HMI device 16 |  |  |  |

#### Outputs

| Parameters | Data type | Description | Interconnection |
| --- | --- | --- | --- |
| E_STOP | Bool | Emergency stop  Evaluation of the emergency-off button of all HMI devices connected to F_FB_RNG_n.   0 =  at least one emergency stop pressed,  1 = no emergency stop pressed | You can detect if an emergency stop is pressed with this output. |
| GLOB_RD | Bool | Global rampdown | You can detect if a global rampdown has been triggered with this output. |
| LOC_RD | Bool | Local rampdown | You can detect if a local rampdown has been triggered with this output. |
| SHUTDOWN | Bool | Shutdown | You can detect if a shutdown has been triggered with this output. |
| ENABLE | Bool | This output passes the state of the enabling button for the HMI device logged on in the effective range.  0 = enabling button not pressed,  1 = enabling button pressed | You can detect if the enabling button has been pressed with this output. |
| F-KEYS | Word | Reserved |  |
| RNG_BUSY | Bool | This output passes the state of the effective range.   0 = effective range free,  1 = effective range in use | You can detect if the effective range is free or in use with this output.  You use this output, for example, to control a light that indicates the allocation of the effective range in the plant. |
| DIAG | Word | This output indicates which of the HMI devices with permission to log on in the effective range are actually logged on.  Bit 0: 1st panel logged on Bit 1: 2nd panel logged on Bit 2: 3rd panel logged on Bit 3: 4th panel logged on  With F_FB_RNG_16: Bit 4: 5th panel logged on ...  Bit 14: 15th panel logged on Bit 15: 16th panel logged on | You can evaluate the DIAG output in your user program. |

#### Enable inputs EN and ENO

When you call a fail-safe block, the enable input EN and enable output ENO appear automatically.

Please observe the following:

- Do not connect these I/Os.
- Do not set "0" for these I/Os.
- Do not evaluate these I/Os.

#### Validity

This description applies to the following F FB:

- F_FB_RNG_4, version 1.0
- F_FB_RNG_16, version 1.0

When the term "F_FB_RNG_n" is used, the information applies to both F-FB.

> **Note**
>
> Insert the FC 176: F_BO_W and FC 177: F_W_BO blocks into your safety program since these blocks are called by F_FB_RNG_n. You can find these blocks in the Distributed Safety F library in the F Application Blocks block container.

#### Wiring

You have to wire the inputs and outputs of the F FB manually. No automatic wiring is performed.

#### Usage

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Emergency-off button not evaluated**  The emergency-off button can only be evaluated if you call an F_FB_RNG_n in your safety program.  Always call an F_FB_RNG_n in your safety program, even if you do not use effective ranges in your plant. |  |

The assigned effective range is managed by this F FB.

You need call one of the following F FB for every effective range when using the Mobile Panel 277F IWLAN:

- F_FB_RNG_4 "Effective range for 4 Mobile Panels"
- F_FB_RNG_16 "Effective range for 16 Mobile Panels"

The FB you need to call depends on how many HMI devices are used in the effective range:

- If you configure a logon for up to 4 HMI devices in this effective range, use F_FB_RNG_4.
- If you configure a logon for up to 16 HMI devices in this effective range, use F_FB_RNG_16.

#### How it works

The F FB performs the following depending on the state of the HMI devices assigned to the effective range:

- Connect the outputs of F_FB_RNG_n
- Prepare the output user data

Each HMI device can take one of the following states in the effective range:

- Removed without communication error

  The HMI device is successfully removed from the safety program of the F CPU. This ends PROFIsafe communication. The HMI device has no influence on the outputs of F_FB_RNG_n.
- Integrated without communication error

  The actual operating state of the HMI device in the effective range

  F_FB_RNG_n reacts as follows:

  - The HMI device is supplied with user data, such as the effective range ID and the status of the HMI device in the effective range, if it is located in the effective range.
  - If no other HMI device is logged on in the effective range, the operator can log on the HMI device in the effective range.
  - The outputs of F_FB_RNG_n are set according to the state of the enabling button of the logged on HMI device.

    The setting for E-STOP output depends on whether or not the HMI device is logged on in the effective range.
  - The RNG_BUSY output of F_FB_RNG_n is set to "1" if the HMI device is logged on in the effective range.
  - The operator can activate the "Override" mode if needed.
  - If the operator wants to exit the effective range, he can log off the HMI device from the effective range.
- Removed with communication error

  PROFIsafe communication with the HMI device was interrupted without explanation.

  The following outputs are set in F_FB_RNG_n:

  - GLOB_RD, if the HMI device was not logged on in the effective range.
  - SHUTDOWN, if the HMI device was logged on in the effective range.

    The corresponding signal is reset following acknowledgment of the communication error or the MP status reset is set. The allocated effective range is enabled again by F_FB_RNG_n for logging on of an HMI device .
- Integrated with communication error

  PROFIsafe communication with the HMI device is resumed after a brief interruption, enabling user data to be exchanged again between the HMI device and F CPU. As long as communication error in not acknowledged, F_FB_RNG_n reacts as follows:

  - The HMI device is supplied with user data (effective range ID, status of the HMI device in the effective range), if it is located in the effective range.
  - If the emergency stop of the HMI device is pressed, the E_STOP output of F_FB_RNG_n is set to "0".

#### Override in the safety program

The override switch should only be active as long as the protective mechanism is active.

Connect the following in the safety program to ensure this reaction:

- The switch position of the override switch with the evaluation signals of the protective device
- The result of the first link with the OVERRIDE input of F_FB_RNG_n

#### Addresses of PII and PIQ

You can find the start address of the PII and PIQ in HW Config in the PROFIsafe settings for the HMI device.

---

**See also**

[Using F-FBs (S7-1200, S7-1500)](#using-f-fbs-s7-1200-s7-1500)
  
[F_DB_STATES: Data exchange (S7-1200, S7-1500)](#f_db_states-data-exchange-s7-1200-s7-1500)
  
[F_FB_MP: Mobile Panel status (S7-1200, S7-1500)](#f_fb_mp-mobile-panel-status-s7-1200-s7-1500)

## Mobile Panel 2nd Generation F-FB (S7-1200, S7-1500)

This section contains information on the following topics:

- [Using F-FBs (S7-1200, S7-1500)](#using-f-fbs-s7-1200-s7-1500-1)
- [F_FB_KTP_Mobile (S7-1200, S7-1500)](#f_fb_ktp_mobile-s7-1200-s7-1500)
- [F_FB_KTP_RNG (S7-1200, S7-1500)](#f_fb_ktp_rng-s7-1200-s7-1500)

### Using F-FBs (S7-1200, S7-1500)

#### Required F FBs

You must integrate the following fail-safe blocks in your safety program:

- For each HMI device: a FB198: F_FB_KTP_Mobile  
  The assigned HMI device is monitored by this F FB.
- For each connection box: a FC199: F_FB_KTP_RNG  
  The F_FB_KTP_RNG supplies the safety-related signals for the machine part that is associated with a connection box.
- FB 215: ESTOP1; with this block, you can ensure that the operator must first provide confirmation after an emergency stop before the plant can be restarted. You can find this module in the F-library "Safety Advanced" in the following block container:  
  "Communication &gt; Failsafe HMI Mobile Panels &gt; -- KTP Mobile --"

| Symbol | Meaning |
| --- | --- |
|  | **Notice** |
| **Naming conventions for F-application blocks**  Ensure the following parameters match when changing the names of an F-application block:  - The symbolic name in the symbol table - The name in the object properties of the block (header) |  |

#### Rules for the safety program

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Emergency stop button not evaluated**  The emergency stop button can only be evaluated in the following cases:  - System with emergency stop function, without enabling function: The output GLOBAL_E_STOP of F_FB_KTP_Mobile is used in the safety program. - System with acknowledgment and emergency stop function: F_FB_KTP_RNG is evaluated by the safety program.   In a system with an emergency stop function, use the output GLOBAL_E_STOP of F_FB_KTP_Mobile in your safety program.  In a system with an acknowledgment and an emergency stop function, use F_FB_KTP_RNG in your safety program. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Prohibited restart of the plant**  Once the emergency stop button has been triggered, the plant can only be restarted after operator acknowledgment. Use the FB 215 ESTOP1 in your safety program to ensure acknowledgment by the operator. |  |

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Emergency stop button is evaluated with delayed**  If the cycle time for the OB 35 block (in conjunction with controllers of the type S7-300/400) or MAIN_SAFETY (in conjunction with controllers of the type S7-1500 ) is set too high, this can cause loss of frames and delayed evaluation of the output "E-STOP" of F_FB_RNG_n.   Set the cycle time lower than that for the PROFINET IO time. |  |

The F FBs used are called cyclically and in a specific order in the safety program. You need to call the F FBs in the following order in your safety program:

1. All F_FB_KTP_Mobile
2. All F_FB_KTP_RNG

The operator must always acknowledge errors, such as communication errors. You cannot use any automatic acknowledgment in your safety program, therefore.

#### Interconnection of the F FBs

The following figure is a schematic representation of the interconnection of F FBs to one another and to the PII and PIQ.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Direct evaluation of the process images not allowed**  You cannot directly evaluate the PII and PIQ in your program. |  |

![Interconnection of the F FBs](images/76213146123_DV_resource.Stream@PNG-de-DE.png)

#### Application example

You can find application examples in the [Internet](http://support.automation.siemens.com/WW/view/en/20229806/136000).

#### F I/O DB

An F I/O DB is automatically generated in HW Config for every F I/O.

The access to the F I/O and working with the F I/O DB is described in detail in the manual "[SIMATIC Safety - Configuration and Programming](http://support.automation.siemens.com/WW/view/en/54110126)", "F I/O Access" section.

---

**See also**

[F_FB_KTP_Mobile (S7-1200, S7-1500)](#f_fb_ktp_mobile-s7-1200-s7-1500)
  
[F_FB_KTP_RNG (S7-1200, S7-1500)](#f_fb_ktp_rng-s7-1200-s7-1500)

### F_FB_KTP_Mobile (S7-1200, S7-1500)

#### Inputs

| Parameter | Data type | Description | Interconnection |
| --- | --- | --- | --- |
| QBAD | Bool | QBAD indicates whether there is an F-I/O communication fault. | F-I/O DB: DBx2.1 = QBAD |
| ACK_REQ | Bool | Acknowledgement required  After a communication error, the fail-safe system sets QBAD  =  1 and ACK_REQ = 0.  ACK_REQ = 1 indicates that the PROFIsafe message frames are being exchanged again. | F-I/O DB: DBx2.2 = ACK_REQ |
| RESET | Bool | This input resets the status of the F_FB_KTP_Mobile to its "original state".  The input is only evaluated if Q_BAD = 1.  Setting the input RESET is necessary if the HMI device cannot return itself to a defined state, for example when an internal error occurs.  This input responds to a rising edge. | Must be specifically interconnected for plant.   The safety program must ensure that automatic restart of the plant is not possible after RESET is set. The operator must strictly ensure that he executes a separate operator action to commence the restart. |
| ACK_ERR | Bool | Communication errors may not be acknowledged automatically.  This input is set to have the F-CPU to acknowledge a communication error during ongoing PROFIsafe communication.  This input responds to a rising edge. | Must be specifically interconnected for plant. |
| MP_DATA | Int | User data of the F-process image input | PII: Int 1 = MP_DATA |

#### Outputs

| Parameter | Data type | Description | Interconnection |
| --- | --- | --- | --- |
| ACK_REI | Bool | Acknowledgement for reintegration  The automatic reintegration is regulated via the F-I/O DB through this output. | F-I/O DB: DBx0.2 = ACK_REI |
| GLOBAL_E_STOP | Bool | This output returns device-specific emergency stop information. |  |
| MP_E_STOP | Word | This output returns the effective-range-specific emergency stop information for the F_FB_KTP_RNG. |  |
| MP_ENABLE | Word | This output returns the effective-range-specific "Acknowledgment" information for the F_FB_KTP_RNG. |  |
| MP_DATA_Q | Int | User data of the fail-safe process image's inputs: | PIO:  Int 1 = MP_DATA |
| DIAG | Word | Information about any occurring errors is provided through this output for servicing purposes. The value has the following meaning:  0x0001: HMI removed  0x0002: HMI device integrated; emergency stop and acknowledgment button are available.  0x0004: Communication error occurred, emergency stop activated, enabling button deactivated   0x0008: Communication error must be acknowledged. Emergency stop is enabled; acknowledgement button is disabled.  0x0010: HMI device removed, integration is being prepared.  All other values: Reserved | You can evaluate the DIAG output in your program. |

#### Enable inputs EN and ENO

When you call a fail-safe block, the enable input EN and enable output ENO appear automatically.

Note the following:

- Do not connect these I/Os
- Do not supply these I/Os with "0"
- Do not evaluate these I/Os

#### Wiring

You have to wire the inputs and outputs of the F-FB manually. No automatic wiring is performed.

#### Purpose

The assigned HMI device is monitored with the F_FB_KTP_Mobile.

You need to use a separate F_FB_KTP_Mobile for each HMI device.

F_FB_KTP_Mobile performs the following tasks:

- The block integrates the HMI device in the safety program of the F-CPU after startup.
- The block removes the HMI device from the safety program after a communication error. As soon as the communication error has been corrected and the operator has acknowledged this, the block integrates the HMI device back into the safety program.
- The block sends the states of the HMI device to F_FB_KTP_RNG_n.

  The following HMI device states are possible:

  - "Removed"
  - "Integrated"
  - "Communication error"
  - "Communication error, acknowledgement required"

QBAD monitors the output of the F-I/O for integrating and removing the HMI device.

- QBAD = 0: PROFIsafe communication is taking place between the HMI device and the F-CPU.
- QBAD = 1: No PROFIsafe communication is not taking place between the HMI device and the F-CPU.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Inadmissible automatic restart of the plant**  The safety program must ensure that automatic restart of the plant is not possible after RESET is set. The operator must strictly ensure that he executes a separate operator action to commence the restart. |  |

#### Addresses of PII and PIQ

You can find the start addresses of PII and PIQ in the PROFIsafe settings of the HMI device in HW Config.

---

**See also**

[Using F-FBs (S7-1200, S7-1500)](#using-f-fbs-s7-1200-s7-1500-1)
  
[F_FB_KTP_RNG (S7-1200, S7-1500)](#f_fb_ktp_rng-s7-1200-s7-1500)

### F_FB_KTP_RNG (S7-1200, S7-1500)

#### Inputs

| Parameter | Data type | Description | Interconnection |
| --- | --- | --- | --- |
| ID | Word | The connection box is uniquely identified by the ID set on the connection box. The ID must be unique throughout the plant and must match the value of this parameter. The value has the following meaning:  0 or &gt; 254: Invalid box ID, emergency stop and acknowledgment button are disabled.  1...254: Valid box ID, emergency stop and acknowledgment button enabled depending on the mode of the HMI device. | --- |
| E_STOP_EXT | Bool | External information on the state of the emergency stop button of another F_FB_KTP_RNG with cascading. |  |
| ENABLE_EXT | Bool | External information on the state of the acknowledgement button of another F_FB_KTP_RNG with cascading. |  |
| ACTIVATE_ENABLE | Bool | This input allows the acknowledgement button to be enabled and disabled. |  |
| MP1_E_STOP | Word | Information from the F_FB_KTP_Mobile on the state of the emergency stop button of HMI device 1 |  |
| MP1_ENABLE | Word | Information from the F_FB_KTP_Mobile on the state of the acknowledgment button of HMI device 1 |  |
| MP2_E_STOP | Word | Information from the F_FB_KTP_Mobile on the state of the emergency stop button of HMI device 2 |  |
| MP2_ENABLE | Word | Information from the F_FB_KTP_Mobile on the state of the acknowledgment button of HMI device 2 |  |

#### Outputs

| Parameter | Data type | Description | Interconnection |
| --- | --- | --- | --- |
| E_STOP | Bool | This output is used to detect whether the emergency stop button on an HMI device connected to the F_FB_KTP_RNG is pressed.  0 = at least one emergency stop pressed,  1 = no emergency stop pressed |  |
| ENABLE | Bool | This output is used to detect whether the acknowledgment button on an HMI device connected to the F_FB_KTP_RNG is pressed.  1 = at least once acknowledgement button pressed,  0 = no acknowledgement button pressed | You can detect if the enabling button has been pressed with this output. |

#### Enable inputs EN and ENO

When you call a fail-safe block, the enable input EN and enable output ENO appear automatically.

Note the following:

- Do not connect these I/Os.
- Do not set "0" for these I/Os.
- Do not evaluate these I/Os.

#### Wiring

You have to wire the inputs and outputs of the F-FB manually. No automatic wiring is performed.

#### Purpose

In an F-system with enabling function and emergency stop function, you need an F_FB_KTP_RNG for each connection box.

#### Operating principle

Depending on the state of the HMI device connected to the connection box, the F-FB switches the outputs of the F_FB_KTP_RNG and prepares the output user data.

Each HMI device can take one of the following states on the connection box:

- Logged off without communication error

  The HMI device is successfully removed from the safety program of the F-CPU. The HMI device has no influence on the outputs of F_FB_KTP_RNG.
- Logged on without communication error

  The actual operating mode of the HMI device on the connection box.

  F_FB_KTP_RNG responds as follows:

  - The HMI device is supplied with user data, for example the ID of the connection box.
  - The output ENABLE is set according to the state of the acknowledgement button of the HMI device.

    The output E_STOP is set according to the state of the emergency stop button of the HMI device.
  - If the operator wishes to disconnect the HMI device from the connection box, he must log off the HMI device before disconnecting it from the safety program.
- Logged on with communication error

  PROFIsafe communication with the HMI device is resumed after a brief interruption, enabling user data to be exchanged again between the HMI device and F CPU. As long as the communication error in not acknowledged, F_FB_KTP_RNG behaves as follows:

  - The HMI device is supplied with user data, for example the ID of the connection box.
  - The outputs E_STOP and ENABLE return the value "0" regardless of the switch position of the emergency stop button and the acknowledgment button.

#### Addresses of PII and PIQ

You can find the start address of the PII and PIQ in the PROFIsafe settings for the HMI device.

#### Cascading

In order to use more than two HMI devices on a connection box, you can cascade multiple F_FB_KTP_RNG blocks. Cascading F_FB_KTP_RNG works with the same ID. The following figure shows an example of the cascade structure of the multiple F_FB_KTP_RNG.

![Cascading](images/76213146123_DV_resource.Stream@PNG-de-DE.png)

---

**See also**

[Using F-FBs (S7-1200, S7-1500)](#using-f-fbs-s7-1200-s7-1500-1)
  
[F_FB_KTP_Mobile (S7-1200, S7-1500)](#f_fb_ktp_mobile-s7-1200-s7-1500)
