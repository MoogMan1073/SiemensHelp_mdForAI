---
title: "G120 CU250S-2 vector"
package: StdrG120CU250SVectorenUS
topics: 175
source: Siemens TIA Portal Information System (offline help, en-US)
---


# G120 CU250S-2 vector

This section contains information on the following topics:

- [Overview](#overview)
- [Making basic settings](#making-basic-settings)
- [Parameterizing inputs/outputs](#parameterizing-inputsoutputs)
- [Preparing setpoints in the setpoint channel](#preparing-setpoints-in-the-setpoint-channel)
- [Selecting the operating mode](#selecting-the-operating-mode)
- [Parameterizing the drive functions](#parameterizing-the-drive-functions)
- [Application functions](#application-functions)
- [Fieldbus](#fieldbus)
- [Interconnections](#interconnections)

## Overview

This section contains information on the following topics:

- [G120 CU250S-2 V overview](#g120-cu250s-2-v-overview)
- [G120 CU250S-2 V function diagram overview](#g120-cu250s-2-v-function-diagram-overview)

### G120 CU250S-2 V overview

#### Overview

The distributed SINAMICS G120 CU250S-2 frequency inverter belongs to the SINAMICS G series. It has the same advantages, such as a modular system and innovative safety engineering (Safety Integrated) and combines these with a special design and high degree of protection. It incorporates positioning functionality and is characterized by extended safety functions, as well as fail-safe inputs and outputs.

SINAMICS G120 CU250S-2 is available in the following versions:

- CU250S-2
- CU250S-2 DP
- CU250S-2 PN
- CU250S-2 CAN

The TIA Portal supports you in the parameterization and commissioning of the drive.

> **Note**
>
> **G120 CU250S-2 servo**
>
> You can only commission the vector version of the CU250S-2 with Startdrive. If you have set the "Servo" mode on the hardware switch of the device, an appropriate message is displayed.

### G120 CU250S-2 V function diagram overview

The structure of the drive functions and the relationship of the individual parameters with other parameters is displayed in the function diagrams:

Explanation of the symbols (Part 1) - 1020 -
  

Explanation of the symbols (Part 2) - 1021 -
  

Explanation of the symbols (Part 3) - 1022 -
  

Handling BICO technology - 1030 -
  

Connection overview - 2201 -
  

Isolated digital inputs (DI 0 … DI 6) - 2221 -
  

Isolated digital inputs (DI 16 … DI 19) - 2222 -
  

Digital inputs/outputs, bidirectional (DI/DO 24 … DI/DO 25) - 2230 -
  

Digital inputs/outputs, bidirectional (DI/DO 26 … DI/DO 27) - 2231 -
  

Digital outputs (DO 0 … DO 2) - 2242 -
  

Analog inputs 0 ... 1 (AI 0 ... AI 1) - 2251 -
  

Analog inputs as digital inputs (DI 11 … DI 12) - 2256 -
  

Analog outputs 0 … 1 (AO 0 … AO 1) - 2261 -
  

2-wire control - 2272 -
  

3-wire control - 2273 -
  

Control commands and interrogation commands - 2381 -
  

States - 2382 -
  

Overview - 2401 -
  

PROFIdrive, EtherNet/IP - addresses and diagnostics - 2410 -
  

PROFIdrive - Standard telegrams and process data (PZD) - 2421 -
  

PROFIdrive - Manufacturer-specific/free telegrams and process data (PZD) - 2422 -
  

PROFIdrive - PZD receive signals, interconnection - 2440 -
  

PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
  

PROFIdrive - STW1 control word interconnection (p2038 = 0) - 2442 -
  

PROFIdrive - STW2 control word interconnection (p2038 = 0) - 2444 -
  

PROFIdrive - STW3 control word interconnection - 2446 -
  

PROFIdrive - PZD send signals, interconnection - 2450 -
  

PROFIdrive - ZSW1 status word interconnection (p2038 = 2) - 2451 -
  

PROFIdrive - ZSW1 status word interconnection (p2038 = 0) - 2452 -
  

PROFIdrive - ZSW2 status word interconnection (p2038 = 0) - 2454 -
  

PROFIdrive - ZSW3 status word interconnection - 2456 -
  

PROFIdrive - MELDW status word interconnection - 2460 -
  

PROFIdrive - POS_STW positioning control word interconnection - 2462 -
  

PROFIdrive - POS_STW1 positioning control word 1 interconnection - 2463 -
  

PROFIdrive - POS_STW2 positioning control word 2 interconnection - 2464 -
  

PROFIdrive - POS_ZSW positioning status word interconnection - 2465 -
  

PROFIdrive - POS_ZSW1 positioning status word 1 interconnection - 2466 -
  

PROFIdrive - POS_ZSW2 positioning status word 2 interconnection - 2467 -
  

PROFIdrive - Receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
  

PROFIdrive - Send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
  

PROFIdrive - Status words, free interconnection - 2472 -
  

EtherNet/IP - control word/status word interconnection - 2473 -
  

PROFIdrive - STW1 control word interconnection (p0108.4 = 1) - 2475 -
  

PROFIdrive - SATZANW block selection interconnection - 2476 -
  

PROFIdrive - AKTSATZ status word interconnection - 2477 -
  

PROFIdrive - ZSW1 status word interconnection (p0108.4 = 1) - 2479 -
  

PROFIdrive - MDI_MOD - MDI mode interconnection - 2480 -
  

Control word, sequence control (r0898) - 2501 -
  

Status word, sequence control (r0899) - 2503 -
  

Control word, setpoint channel (r1198) - 2505 -
  

Status word 1 (r0052) - 2510 -
  

Status word 2 (r0053) - 2511 -
  

Control word 1 (r0054) - 2512 -
  

Supplementary control word (r0055) - 2513 -
  

Control word, speed controller (r1406) - 2520 -
  

Status word, speed controller (r1407) - 2522 -
  

Status word, closed-loop control (r0056) - 2526 -
  

Status word, current control (r1408) - 2530 -
  

Status word, monitoring functions 1 (r2197) - 2534 -
  

Status word, monitoring functions 2 (r2198) - 2536 -
  

Status word, monitoring functions 3 (r2199) - 2537 -
  

Control word, faults/alarms (r2138) - 2546 -
  

Status word, faults/alarms 1 and 2 (r2139 and r2135) - 2548 -
  

Sequence control - Sequencer - 2610 -
  

Sequence control - Missing enables, line contactor control - 2634 -
  

Simple brake control - 2701 -
  

Parameter manager - 2800 -
  

Monitoring functions and faults/alarms - 2802 -
  

Status words - 2804 -
  

SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
  

STO (Safe Torque Off) (Part 2) - PM240-2 FS D-F - 2812 -
  

F-DI (Fail-safe Digital Input) - 2813 -
  

SBC (Safe Brake Control) - 2814 -
  

Parameter manager - 2818 -
  

SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
  

SLS (Safely-Limited Speed) - 2820 -
  

SSM (Safe Speed Monitor) - 2823 -
  

SDI (Safe Direction) - 2824 -
  

Control and status word - 2840 -
  

Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
  

Fail-safe digital output (F-DO 0) - 2853 -
  

Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
  

Safe State selection - 2856 -
  

F-DO assignment - 2857 -
  

Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -
  

Standard telegrams - 2915 -
  

Manufacturer-specific telegrams - 2917 -
  

Overview - 3001 -
  

Fixed speed setpoints, binary selection (p1016 = 2) - 3010 -
  

Fixed speed setpoints, direct selection (p1016 = 1) - 3011 -
  

Motorized potentiometer - 3020 -
  

Main/additional setpoint, setpoint scaling, jog - 3030 -
  

Direction limitation and direction reversal - 3040 -
  

Skip frequency bands and speed limits - 3050 -
  

Basic ramp-function generator - 3060 -
  

Extended ramp-function generator - 3070 -
  

Ramp-function generator selection, -status word, -tracking - 3080 -
  

Generation of the speed limits (p0108.8 = 0) - 3095 -
  

Jog mode - 3610 -
  

Referencing/reference point approach mode (p2597 = 0) - 3612 -
  

Flying referencing mode (p2597 = 1) - 3614 -
  

Traversing block mode, external block change - 3615 -
  

Traversing block mode - 3616 -
  

Travel to fixed stop - 3617 -
  

Direct setpoint specification / MDI mode, dynamic response values - 3618 -
  

Direct setpoint specification / MDI mode - 3620 -
  

Operating mode control - 3625 -
  

Traversing range limits - 3630 -
  

Interpolator - 3635 -
  

Control word, block selection / MDI selection - 3640 -
  

Status word 1 (r2683) - 3645 -
  

Status word 2 (r2684) - 3646 -
  

Status word, active traversing block / MDI active (r2670) - 3650 -
  

Position actual value preprocessing - 4010 -
  

Position controller - 4015 -
  

Standstill/positioning monitoring - 4020 -
  

Dynamic following error monitoring, cam sequencer - 4025 -
  

Position and temperature sensing, encoders 1 ... 2 - 4704 -
  

Speed actual value and pole position sensing, ASM/PMSM motor encoder (encoder 1) - 4715 -
  

Encoder interface, receive signals, encoder 1 ... 2 - 4720 -
  

Encoder interface, send signals, encoder 1 ... 2 - 4730 -
  

Reference mark search with equivalent zero mark, encoder 1 - 4735 -
  

Absolute value for incremental encoder - 4750 -
  

Application classes (p0096), overview - 6019 -
  

Closed-loop speed control and generation of the torque limits, overview - 6020 -
  

Speed setpoint, droop - 6030 -
  

Precontrol symmetrization, acceleration model - 6031 -
  

Moment of inertia estimator - 6035 -
  

Speed controller - 6040 -
  

Kp_n/Tn_n adaptation - 6050 -
  

Torque setpoint - 6060 -
  

Vdc_max controller and Vdc_min controller (PM240) - 6220 -
  

U/f control, overview - 6300 -
  

U/f control, characteristic and voltage boost - 6301 -
  

U/f control, resonance damping and slip compensation - 6310 -
  

U/f control, Vdc_max controller and Vdc_min controller (PM240) - 6320 -
  

Closed-loop speed control configuration - 6490 -
  

Flux control configuration - 6491 -
  

Upper/lower torque limit - 6630 -
  

Current/power/torque limits - 6640 -
  

Current control, overview - 6700 -
  

Current setpoint filter - 6710 -
  

Iq and Id controller - 6714 -
  

Id setpoint (PMSM, p0300 = 2xx) - 6721 -
  

Field weakening characteristic, flux setpoint (ASM, p0300 = 1) - 6722 -
  

Field weakening controller, flux controller, Id setpoint (ASM, p0300 = 1) - 6723 -
  

Field weakening controller (PMSM, p0300 = 2xx) - 6724 -
  

Interface to the Power Module (ASM, p0300 = 1) - 6730 -
  

Interface to the Power Module (PMSM, p0300 = 2xx) - 6731 -
  

Display signals - 6799 -
  

Closed-loop speed control and generation of the torque limits, overview (p0096 = 2) - 6820 -
  

Current control, overview (p0096 = 2) - 6821 -
  

Speed setpoint, precontrol symmetrization, acceleration model (p0096 = 2) - 6822 -
  

Moment of inertia estimator (p0096 = 2) - 6823 -
  

Speed controller with Kp_n/Tn_n adaptation (p0096 = 2) - 6824 -
  

Torque setpoint (p0096 = 2) - 6826 -
  

Vdc_max controller and Vdc_min controller (p0096 = 2) - 6827 -
  

Current/power/torque limits (p0096 = 2) - 6828 -
  

Current setpoint filter (p0096 = 2) - 6832 -
  

Iq and Id controller (p0096 = 2) - 6833 -
  

Id setpoint (PMSM, p0300 = 2xx, p0096 = 2) - 6836 -
  

Field weakening characteristic, flux setpoint (ASM, p0300 = 1, p0096 = 2) - 6837 -
  

Field weakening controller, flux controller, Id setpoint (ASM, p0300 = 1, p0096 = 2) - 6838 -
  

Field weakening controller (PMSM, p0300 = 2xx, p0096 = 2) - 6839 -
  

Interface to the Power Module (ASM, p0300 = 1, p0096 = 2) - 6841 -
  

Interface to the Power Module (PMSM, p0300 = 2xx, p0096 = 2) - 6842 -
  

U/f control, overview (p0096 = 1) - 6850 -
  

U/f control, characteristic and voltage boost (p0096 = 1) - 6851 -
  

U/f control, resonance damping and slip compensation (p0096 = 1) - 6853 -
  

U/f control, Vdc_max controller and Vdc_min controller (p0096 = 1) - 6854 -
  

U/f control, interface to the Power Module (ASM, p0300 = 1xx, p0096 = 1) - 6856 -
  

Friction characteristic - 7010 -
  

DC braking (ASM, p0300 = 1) - 7017 -
  

Sampling times of the runtime groups - 7200 -
  

AND 0 … 3 - 7210 -
  

OR 0 … 3 - 7212 -
  

XOR 0 … 3 - 7214 -
  

NOT 0 … 5 - 7216 -
  

ADD 0 … 2, SUB 0 … 1 - 7220 -
  

MUL 0 … 1, DIV 0 … 1 - 7222 -
  

AVA 0 … 1 - 7224 -
  

NCM 0 … 1 - 7225 -
  

PLI 0 … 1 - 7226 -
  

MFP 0 … 3, PCL 0 … 1 - 7230 -
  

PDE 0 … 3 - 7232 -
  

PDF 0 … 3 - 7233 -
  

PST 0 … 1 - 7234 -
  

RSR 0 … 2, DFR 0 … 2 - 7240 -
  

BSW 0 … 1, NSW 0 … 1 - 7250 -
  

LIM 0 … 1 - 7260 -
  

PT1 0 … 1 - 7262 -
  

INT 0, DIF 0 - 7264 -
  

LVM 0 … 1 - 7270 -
  

Fixed values, binary selection (p2216 = 2) - 7950 -
  

Fixed values, direct selection (p2216 = 1) - 7951 -
  

Motorized potentiometer - 7954 -
  

Closed-loop control - 7958 -
  

Overview - 8005 -
  

Speed messages 1 - 8010 -
  

Speed messages 2 - 8011 -
  

Torque messages, motor blocked/stalled - 8012 -
  

Load monitoring - 8013 -
  

Thermal monitoring, motor, motor temperature status word, faults/alarms - 8016 -
  

Motor temperature model 1 (I2t) - 8017 -
  

Motor temperature model 2 - 8018 -
  

Motor temperature model 3 - 8019 -
  

Thermal monitoring, power unit - 8021 -
  

Monitoring functions 1 - 8022 -
  

Monitoring functions 2 - 8023 -
  

Overview - 8050 -
  

Fault buffer - 8060 -
  

Alarm buffer - 8065 -
  

Faults/alarms trigger word (r2129) - 8070 -
  

Faults/alarms configuration - 8075 -
  

Command data sets (CDS) - 8560 -
  

Drive data sets (DDS) - 8565 -
  

Encoder data sets (EDS) - 8570 -
  

Receive telegram, free PDO mapping (p8744 = 2) - 9204 -
  

Receive telegram, predefined connection set (p8744 = 1) - 9206 -
  

Send telegram, free PDO mapping (p8744 = 2) - 9208 -
  

Send telegram, predefined connection set (p8744 = 1) - 9210 -
  

CANopen control word interconnection - 9220 -
  

Status word, CANopen (r8784) - 9226 -
  

Configuration, addresses and diagnostics - 9310 -
  

STW1 control word interconnection - 9342 -
  

ZSW1 status word interconnection - 9352 -
  

Receive telegram, free interconnection via BICO (p0922 = 999) - 9360 -
  

Send telegram, free interconnection via BICO (p0922 = 999) - 9370 -
  

Status words, free interconnection - 9372 -

## Making basic settings

This section contains information on the following topics:

- [Configuration summary](#configuration-summary)
- [G120 CU250S-2 V drive data sets DDS](#g120-cu250s-2-v-drive-data-sets-dds)
- [G120 CU250S-2 V command data sets CDS](#g120-cu250s-2-v-command-data-sets-cds)
- [G120 CU250S-2 V reference variables](#g120-cu250s-2-v-reference-variables)
- [G120 CU250S-2 V I/O configuration](#g120-cu250s-2-v-io-configuration)
- [G120 CU250S-2 V units](#g120-cu250s-2-v-units)

### Configuration summary

In "Configuration summary", you can view the overall summary such as general information, parameters, units and other details of the components.

**Exporting the configuration summary**

Click "Configuration summary> Export", to the export the configuration summary in .csv format.

### G120 CU250S-2 V drive data sets DDS

#### Drive data sets

To switch between different drive configurations (control type, motor), parameterize up to four drive data sets. Binector inputs [p0820](SINAMICS%20Parameter%20G120.md#p08200n-bi-drive-data-set-selection-dds-bit-0-1) and [p0821](SINAMICS%20Parameter%20G120.md#p08210n-bi-drive-data-set-selection-dds-bit-1) are used to select a drive data set. They form the number of the drive data set (0 … 3) in binary format (where p0821 is the most significant bit). See also [Drive data sets (DDS)](Configuring%20SINAMICS%20G120-G115D-G110M%20drives.md#drive-data-sets-dds).

#### Selecting a drive data set

To select a drive data set, interconnect bit 0 and bit 1 appropriately.

- Bit 0

  Selection of the parameter that supplies the signal for bit 0 ([p0820](SINAMICS%20Parameter%20G120.md#p08200n-bi-drive-data-set-selection-dds-bit-0-1)) for the drive data set selection.
- Bit 1

  Selection of the parameter that supplies the signal for bit 1 ([p0821](SINAMICS%20Parameter%20G120.md#p08210n-bi-drive-data-set-selection-dds-bit-1)) for the drive data set selection.

#### Function diagrams (FD)

- Drive data sets (DDS) - 8565 -

#### Additional parameters

---

---

**See also**

[Switching data sets for the parameterizing](Configuring%20SINAMICS%20G120-G115D-G110M%20drives.md#switching-data-sets-for-the-parameterizing)

### G120 CU250S-2 V command data sets CDS

Parameterize the settings for the command sources, setpoint sources and status messages in up to four command data sets. Binector inputs [p0810](SINAMICS%20Parameter%20G120.md#p0810-bi-command-data-set-selection-cds-bit-0-1) to [p0811](SINAMICS%20Parameter%20G120.md#p0811-bi-command-data-set-selection-cds-bit-1) are used to select a command data set. They form the number of the command data set (0 … 3) in binary format (where p0811 is the most significant bit). See also [Command data sets (CDS)](Configuring%20SINAMICS%20G120-G115D-G110M%20drives.md#command-data-sets-cds).

#### Selecting a command data set

To select a command data set, interconnect bit 0 and bit 1 appropriately.

- Bit 0

  Selection of the parameter that supplies the signal for bit 0 ([p0810](SINAMICS%20Parameter%20G120.md#p0810-bi-command-data-set-selection-cds-bit-0-1)) for the command data set selection.
- Bit 1

  Selection of the parameter that supplies the signal for bit 1 ([p0811](SINAMICS%20Parameter%20G120.md#p0811-bi-command-data-set-selection-cds-bit-1)) for the command data set selection.

#### Copying a command data set

1. In the "From command data set" drop-down list, select the source data set.
2. In the "To command data set" drop-down list, select the target data set.
3. Click the "Copy" button to copy the settings of one data set to another data set. All the relevant parameters of the source data set are copied to the target data set.

#### Example

For example, to parameterize CDS1 in DDS2, you must make the following settings for the parameters.

| Command data set CDS | Drive data set DDS |
| --- | --- |
| p0810[0] = 1 | [p0820](SINAMICS%20Parameter%20G120.md#p08200n-bi-drive-data-set-selection-dds-bit-0-1)[1] = 0 |
| p0811[0] = 0 | [p0821](SINAMICS%20Parameter%20G120.md#p08210n-bi-drive-data-set-selection-dds-bit-1)[1] = 1 |
| r50 = 1 | r51 = 2 |

#### Function diagrams (FD)

- Command data sets (CDS) - 8560 -

#### Additional parameters

---

---

**See also**

[Switching data sets for the parameterizing](Configuring%20SINAMICS%20G120-G115D-G110M%20drives.md#switching-data-sets-for-the-parameterizing)

### G120 CU250S-2 V reference variables

#### Reference variables / scaling

Reference variables that correspond to 100% are required for the display of units in percent. Enter these reference variables in parameters [p2000](SINAMICS%20Parameter%20G120.md#p2000-reference-speed-reference-frequency) to [p2003](SINAMICS%20Parameter%20G120.md#p2003-reference-torque). During the drive configuration, Startdrive calculates the parameters and uses these values then as reference values for the percentage input in the context of the respective parameter.

You can specify the following variables:

- Reference speed / reference frequency (p2000)
- Reference voltage ([p2001](SINAMICS%20Parameter%20G120.md#p2001-reference-voltage-1))
- Reference current ([p2002](SINAMICS%20Parameter%20G120.md#p2002-reference-current))
- Reference torque (p2003)
- Reference power ([r2004](SINAMICS%20Parameter%20G120.md#r2004-reference-power))

#### Procedure

1. To specify the values for the reference variables, enter the values in the text fields of the parameters.
2. Activate "Inhibit automatic reference value calculation" if you want to inhibit an automatic reference value calculation as performed in the motor identification.

#### Result

The reference values are for a percentage input of the values.

#### Additional parameters

---

### G120 CU250S-2 V I/O configuration

In the "I/O configuration", you can see the fieldbus protocol with the corresponding telegram setting as well as the inputs/outputs of the module and its current interconnections clearly displayed in a table.

#### Used setting of [p0015](SINAMICS%20Parameter%20G120.md#p0015-macro-drive-unit-10) (macro of drive unit)

The text field displays the setting of p015. You set predefined I/O configurations via p015, which are then interconnected via a drive macro.

#### Fieldbus protocol and telegram selection

The text fields show the selected fieldbus and the selected telegram.

1. To change the fieldbus protocol, select the appropriate protocol in the drop-down list.
2. To change the telegram, click "Change configuration". The "Receive direction" dialog is displayed.
3. Edit the telegram and the PZD interconnection there.

#### Configuring inputs/outputs

1. To display the I/O configuration of the inputs/outputs, select which configuration you want to view in the drop-down list.
2. Click "Change configuration" to jump to the respective configuration page of the input/output.

#### Additional parameters

---

### G120 CU250S-2 V units

#### Description

You can select the unit system that the system is to use here. If you want to use the unit system depending on reference variables, you must define these reference variables at [G120 CU250S-2 V reference variables](#g120-cu250s-2-v-reference-variables).

> **Note**
>
> Parameters such as type plate data cannot be switched in referenced units. You can only switch between SI and US units.

#### Unit system ([p0505](SINAMICS%20Parameter%20G120.md#p0505-selecting-the-system-of-units))

Select the unit system from the following entries in the drop-down list:

- SI unit system: Displays the SI units in SI
- Referenced unit system/SI: Displays the units in relation (%) to SI units
- US unit system: Displays the units in the US unit system
- Referenced unit system/SI: Displays the units in relation (%) to the US unit system

  > **Note**
  >
  > If you want to switch the units, the reference parameters first have to be calculated and preassigned via a download. You then have to load the data via an upload to the PG/PC. Only then are the deactivated fields activated.
  >
  > You can then adapt the reference data and reload them to the drive.

**Technological units (only when technology controller selected)**

You can select from this drop-down list the unit to be used for the technology controller.

#### Additional settings

**Motor standard ([p0100](SINAMICS%20Parameter%20G120.md#p0100-iecnema-standards))**

- Select whether you want to use the SI or the US motor standard. You can set the unit system of the rated motor power or the rated power of the power unit (HP or kW).

#### Additional parameters

---

## Parameterizing inputs/outputs

This section contains information on the following topics:

- [G120 CU250S-2 V overview of the interfaces](#g120-cu250s-2-v-overview-of-the-interfaces)
- [G120 CU250S-2 V digital inputs](#g120-cu250s-2-v-digital-inputs)
- [G120 CU250S-2 V relay outputs](#g120-cu250s-2-v-relay-outputs)
- [G120 CU250S-2 V bidirectional inputs/outputs](#g120-cu250s-2-v-bidirectional-inputsoutputs)
- [G120 CU250S-2 V analog inputs](#g120-cu250s-2-v-analog-inputs)
- [G120 CU250S-2 V analog outputs](#g120-cu250s-2-v-analog-outputs)
- [G120 CU250S-2 V measuring inputs](#g120-cu250s-2-v-measuring-inputs)

### G120 CU250S-2 V overview of the interfaces

#### Interfaces at the front of the Control Unit

To access the interfaces at the front of the Control Unit, you must unplug the Operator Panel (if one is being used) and open the front doors.

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| ![User interfaces CU250S-2](images/103276260619_DV_resource.Stream@PNG-en-US.png)   User interfaces CU250S-2 | ① | Memory card slot |  |  |  |  |
| ② | Connection to the Operator Panel |  |  |  |  |  |
| ③ | Switch for analog inputs |  |  |  |  |  |
|  | I | 0/4 mA … 20 mA |  | ![Interfaces at the front of the Control Unit](images/103276271499_DV_resource.Stream@PNG-en-US.png) |  |  |
|  | U | -10/0 V … 10 V |  |  |  |  |
| ④ | Terminal blocks |  |  |  |  |  |
| ⑤ | Selecting the control mode |  |  |  | Without function; leave the switch set to "Vector". |  |
| ⑥ | USB interface for connection to a PC |  |  |  |  |  |
| ⑦ | Status LED |  |  |  |  |  |
| ![Interfaces at the front of the Control Unit](images/103276288267_DV_resource.Stream@PNG-en-US.png) |  |  |  |  |  |  |
| ⑧ | Selecting the fieldbus address:  - PROFIBUS - USS - Modbus RTU - CanOpen |  | ![Interfaces at the front of the Control Unit](images/103276293003_DV_resource.Stream@PNG-en-US.png) |  |  |  |

![Interfaces at the bottom](images/103276297739_DV_resource.Stream@PNG-en-US.png)

Interfaces at the bottom

### G120 CU250S-2 V digital inputs

#### Description

The digital inputs are pre-assigned with certain functions at the factory. You can adapt these interconnections or make additional interconnections. If you are using safety functions, the interconnected safety inputs are only displayed after the parameterization of the safety functions.

Depending on the version of the Control Unit, up to eight digital inputs are available.

**Inverter control**

- [Converter control using digital inputs](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#converter-control-using-digital-inputs)
- [Two-wire control, method 1](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#two-wire-control-method-1)
- [Two-wire control, method 2](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#two-wire-control-method-2)
- [Two-wire control, method 3](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#two-wire-control-method-3)
- [Three-wire control, method 1](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#three-wire-control-method-1)
- [Three-wire control, method 2](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#three-wire-control-method-2)

You can find an overview of the interface assignments which are carried out by the macro of p15 under [SINAMICS G120 interface assignments - CU240B-2](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#sinamics-g120-interface-assignments---cu240b-2).

#### Current I/O configuration

The text field displays the current I/O configuration (setting of p15). The digital inputs are pre-assigned accordingly.

#### Terminals

The assigned LEDs show the current signal states.

#### Digital inputs 0...5

- "Digital inputs 0...5" ([r0722](SINAMICS%20Parameter%20G120.md#r0722012-cobo-cu-digital-inputs-status-5).0 ... r722.5); signal sources for interconnecting the digital inputs.
- "Digital inputs 0...5 inverted" ([r0723](SINAMICS%20Parameter%20G120.md#r0723012-cobo-cu-digital-inputs-status-inverted-5).0 ... r723.5); signal sources for interconnecting the inverted digital inputs.

#### Digital inputs 11...12

When required, interconnect two analog inputs as digital inputs DI 11 and DI 12 (r722.11 and r722.12).

#### Function diagrams (FD)

- Isolated digital inputs (DI 0 … DI 6) - 2221 -
- Isolated digital inputs (DI 16 … DI 19) - 2222 -

#### Additional parameters

---

### G120 CU250S-2 V relay outputs

#### Description

The relay outputs are pre-assigned with functions at the factory.

They are usually used for outputting faults and alarms, see also [SINAMICS G120 interface assignments - CU240B-2](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#sinamics-g120-interface-assignments---cu240b-2).

#### Current I/O configuration

The text field displays the current I/O configuration (setting of p15). The relay outputs are pre-assigned accordingly.

#### Relay output 0...2

- "Relay output 1" ([p0730](SINAMICS%20Parameter%20G120.md#p0730-bi-cu-signal-source-for-terminal-do-0-3)); signal source for interconnecting relay output 1
- "Relay output 2" ([p0731](SINAMICS%20Parameter%20G120.md#p0731-bi-cu-signal-source-for-terminal-do-1-5)); signal source for interconnecting relay output 2
- "Relay output 3" ([p0732](SINAMICS%20Parameter%20G120.md#p0732-bi-cu-signal-source-for-terminal-do-2-3)); signal source for interconnecting relay output 3
- Click the "Invert" button to invert the signals.

#### Additional parameters

---

### G120 CU250S-2 V bidirectional inputs/outputs

#### Description

Three fixed digital outputs are available: DO 0 … DO 2:

- Relay outputs, 30 VDC / max. 0.5 A with resistive load.

Four switchable digital outputs are also available:

- DO 24 … DO27: Transistor outputs
- Max. 0.1 A per output
- An external power supply via terminals 31 and 32 is required
- 2 ms update time

**Inverter control**

- [Converter control using digital inputs](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#converter-control-using-digital-inputs)
- [Two-wire control, method 1](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#two-wire-control-method-1)
- [Two-wire control, method 2](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#two-wire-control-method-2)
- [Two-wire control, method 3](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#two-wire-control-method-3)
- [Three-wire control, method 1](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#three-wire-control-method-1)
- [Three-wire control, method 2](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#three-wire-control-method-2)

You can find an overview of the interface assignments which are carried out by the macro of p15 under [SINAMICS G120 interface assignments - CU240B-2](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#sinamics-g120-interface-assignments---cu240b-2).

#### Current I/O configuration

The text field displays the current I/O configuration (setting of p15). The digital inputs are pre-assigned accordingly.

#### Terminals

The assigned LEDs show the current signal states.

#### Bidirectional digital inputs/outputs 24...27

| Symbol | Meaning |
| --- | --- |
| ![Bidirectional digital inputs/outputs 24...27](images/103276493963_DV_resource.Stream@PNG-en-US.png) | Button to switch between digital input and digital output |

- "Bidirectional digital inputs/outputs 0...5" ([r0722](SINAMICS%20Parameter%20G120.md#r0722012-cobo-cu-digital-inputs-status-5)) or ([p0738](SINAMICS%20Parameter%20G120.md#p0738-bi-cu-signal-source-for-terminal-dido-24)); signal sources for interconnecting the digital inputs/outputs.
- "Status signal of the bidirectional digital inputs/outputs 0–5 inputs" ([r0723](SINAMICS%20Parameter%20G120.md#r0723012-cobo-cu-digital-inputs-status-inverted-5)); signal sources for interconnecting the inverted digital inputs.

#### Function diagrams (FD)

- Digital inputs/outputs, bidirectional (DI/DO 24 … DI/DO 25) - 2230 -
- Digital inputs/outputs, bidirectional (DI/DO 26 … DI/DO 27) - 2231 -

#### Additional parameters

---

### G120 CU250S-2 V analog inputs

#### Description

Depending on the Control Unit version, the inverter has one or two analog inputs. You use it, for example, to specify speed setpoints manually.

The following setting options apply for the analog inputs:

- Analog input 0: Voltage or current
- Analog input 1: Voltage or current

BICO technology can be used to set further interconnection of the analog input, e.g. as a speed setpoint or setpoint for the technology controller. See also [Analog input as setpoint source](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#analog-input-as-setpoint-source).

#### Current I/O configuration

The text field displays the current I/O configuration (setting of p15). The analog inputs are pre-assigned accordingly.

#### Analog input as voltage or current input ([p0756](SINAMICS%20Parameter%20G120.md#p075603-cu-analog-inputs-type-2))

In order to determine whether the analog input is to be used as a voltage or current input, select one of the following settings:

- Unipolar voltage input (0 V...+10 V)

  The analog input is configured as a voltage input.
- Monitored unipolar voltage input (+2 V...+10 V)

  The analog input is configured as a voltage input. In addition, wire-break detection is active.
- Unipolar current input (0 mA...+20 mA)

  The analog input is configured as a current input.
- Monitored unipolar current input (+4 mA...+20 mA)

  The analog input is configured as a current input. In addition, wire-break detection is active.
- Bipolar voltage input (-10 V...+10 V)

  The analog input is configured as a voltage input. The input range is +/-10 V.

#### Current input voltage / current input current

The field ([r0752](SINAMICS%20Parameter%20G120.md#r075203-co-cu-analog-inputs-input-voltagecurrent-actual-2)) shows the current input voltage or the current input current.

#### Scaling (scaling characteristic)

Analog inputs supply a normalized analog signal (current, voltage or temperature). This analog signal is converted via the scaling in the value range -100%...100%. With the deadband, you are specifying a range around the zero point in which the analog input is not evaluated. This hides fluctuations around the zero point from the hardware end, for example, which could be present if a sensor is connected to the input as a setpoint device.

1. To define a scaling characteristic, click the "Scaling" button.

   The "Scaling" dialog box is displayed.
2. To specify the corner points for the ordinate, enter values in fields y1 ([p0758](SINAMICS%20Parameter%20G120.md#p075803-cu-analog-inputs-characteristic-value-y1-2)) and y2 ([p0760](SINAMICS%20Parameter%20G120.md#p076003-cu-analog-inputs-characteristic-value-y2-2)) in [%].
3. To specify the corner points for the abscissa, enter values in fields x1 ([p0757](SINAMICS%20Parameter%20G120.md#p075703-cu-analog-inputs-characteristic-value-x1-2)) and x2 ([p0759](SINAMICS%20Parameter%20G120.md#p075903-cu-analog-inputs-characteristic-value-x2-2)).
4. Enter a value to define a "deadband" ([p0764](SINAMICS%20Parameter%20G120.md#p076403-cu-analog-inputs-dead-zone-2)) around the zero point.

#### Smoothing

1. To compensate temporary variations in the measured value at the analog input, specify a time constant at "Smoothing" ([p0753](SINAMICS%20Parameter%20G120.md#p075303-cu-analog-inputs-smoothing-time-constant-2)).
2. The larger the smoothing time constant, the slower the response of the analog input to changes in the measured value.

#### Wire-break detection

The response threshold is parameterized via [p0761](SINAMICS%20Parameter%20G120.md#p076103-cu-analog-inputs-wire-breakage-monitoring-response-threshold-2).

1. To detect a wire break, select a "monitored" voltage or current input as setting (p756).
2. To display a wire break (signal loss) with a delay, enter a delay time ([p0762](SINAMICS%20Parameter%20G120.md#p076203-cu-analog-inputs-wire-breakage-monitoring-delay-time-2)).

#### Analog input 0 ... 1

- "Analog input 0 ... 1" ([r0755](SINAMICS%20Parameter%20G120.md#r075503-co-cu-analog-inputs-actual-value-in-percent-2)); signal source for displaying the scaled and smoothed value of the analog input in [%].

#### Function diagrams (FD)

- Analog inputs 0 ... 1 (AI 0 ... AI 1) - 2251 -

#### Additional parameters

---

### G120 CU250S-2 V analog outputs

#### Description

The Control Unit has two analog outputs (AO). You can use the analog outputs to display a wide range of signals, e.g. the current speed, the current output voltage or the current output current.

#### Current I/O configuration

The text field displays the current I/O configuration (setting of p15). The analog outputs are pre-assigned accordingly.

#### Analog output as voltage or current output ([p0776](SINAMICS%20Parameter%20G120.md#p077602-cu-analog-outputs-type-2))

In order to determine whether the analog output is to be used as a voltage or current output, select one of the following settings:

- Unipolar voltage output (0 V...+10 V)

  The analog output is configured as a voltage output.
- Unipolar current output (0 mA...+20 mA)

  The analog output is configured as a current output.
- Unipolar current output (+4 mA...+20 mA)

  The analog output is configured as a current output.

#### Analog output 0...1

- Analog output 0...1 ([p0771](SINAMICS%20Parameter%20G120.md#p077102-ci-cu-analog-outputs-signal-source-2)); signal source for interconnecting the analog output.

#### Inversion

- Inversion ([p0782](SINAMICS%20Parameter%20G120.md#p078202-bi-cu-analog-outputs-invert-signal-source-2)); signal source for inversion of the analog output.

#### Scaling (scaling characteristic)

1. To define a scaling characteristic, click the "Scaling" button.

   The "Scaling" dialog box is displayed.
2. To specify the corner points for the ordinate, enter values in fields y1 ([p0778](SINAMICS%20Parameter%20G120.md#p077802-cu-analog-outputs-characteristic-value-y1-2)) and y2 ([p0780](SINAMICS%20Parameter%20G120.md#p078002-cu-analog-outputs-characteristic-value-y2-2)) in [%].
3. To specify the corner points for the abscissa, enter values in fields x1 ([p0777](SINAMICS%20Parameter%20G120.md#p077702-cu-analog-outputs-characteristic-value-x1-2)) and x2 ([p0779](SINAMICS%20Parameter%20G120.md#p077902-cu-analog-outputs-characteristic-value-x2-2)).

#### Smoothing

1. To compensate temporary variations in the measured value at the analog output, specify a time constant at "Smoothing" ([p0773](SINAMICS%20Parameter%20G120.md#p077302-cu-analog-outputs-smoothing-time-constant-2)).
2. The larger the smoothing time constant, the slower the response of the analog output to changes in the measured value.

#### Function diagrams (FD)

- Analog outputs 0 … 1 (AO 0 … AO 1) - 2261 -

#### Additional parameters

---

### G120 CU250S-2 V measuring inputs

#### Monitoring the speed via digital input and measuring input

The monitoring sensor is connected to digital input 3.

The speed is calculated from the pulse signal of the digital input in the "measuring input".

For more detailed information, see [Monitoring the speed via digital input](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#monitoring-the-speed-via-digital-input).

#### Parameters of the measuring input

1. Enter a value at "Measuring input edge" ([p0581](SINAMICS%20Parameter%20G120.md#p0581-measuring-probe-edge)) to set the edge for the evaluation of the measuring input signal for the actual speed value measurement.
2. Enter a value at "Measuring input pulses per revolution" ([p0582](SINAMICS%20Parameter%20G120.md#p0582-measuring-probe-pulses-per-revolution)).
3. Enter a value at "Measuring input maximum measuring time" ([p0583](SINAMICS%20Parameter%20G120.md#p0583-measuring-probe-maximum-measuring-time)) to specify the maximum measuring time.

   If there is no new pulse before the end of the maximum measuring time, the actual speed value in [r0586](SINAMICS%20Parameter%20G120.md#r0586-co-measuring-probe-speed-actual-value) is set to zero. The timer is restarted with the next pulse.
4. Enter a value for the gear ratio ([p0585](SINAMICS%20Parameter%20G120.md#p0585-measuring-probe-gear-factor)).

   The measured speed is multiplied by the BERO gear ratio and displayed in r0586.
5. Interconnect a signal ([r0586](SINAMICS%20Parameter%20G120.md#r0586-co-measuring-probe-speed-actual-value)) to display the actual speed value.

#### Additional parameters

---

## Preparing setpoints in the setpoint channel

This section contains information on the following topics:

- [G120 CU250S-2 V setpoint sources and setpoint preparation](#g120-cu250s-2-v-setpoint-sources-and-setpoint-preparation)
- [Motorized potentiometer](#motorized-potentiometer)
- [G120 CU250S-2 V fixed setpoints and fixed setpoint interconnection](#g120-cu250s-2-v-fixed-setpoints-and-fixed-setpoint-interconnection)
- [G120 CU250S-2 V speed setpoint](#g120-cu250s-2-v-speed-setpoint)
- [G120 CU250S-2 V speed limitation](#g120-cu250s-2-v-speed-limitation)
- [Ramp-function generator](#ramp-function-generator)

### G120 CU250S-2 V setpoint sources and setpoint preparation

#### Overview of the setpoint sources and the setpoint preparation

The setpoint source is the interface via which the inverter receives its setpoint, see also [Overview of the setpoint sources](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#overview-of-the-setpoint-sources). The following options are available:

- Motorized potentiometer simulated in the inverter
- Analog input of the inverter
- Fixed setpoints stored in the inverter
- Fieldbus interface of the inverter

Depending on the parameterization, the setpoint in the inverter has one of the following meanings:

- Speed setpoint for the motor
- Torque setpoint for the motor
- Setpoint for a process variable

  The inverter receives a setpoint for a process variable, e.g. the level of a liquid container, and calculates the speed setpoint internally in the technology controller.

#### Overview of the setpoint preparation

The setpoint preparation modifies the speed setpoint. For example, it limits the setpoint to a maximum and a minimum value and prevents speed jumps of the motor via the ramp-function generator.

- Minimum speed and maximum speed
- Ramp-function generator

### Motorized potentiometer

This section contains information on the following topics:

- [G120 CU250S-2 V motorized potentiometer](#g120-cu250s-2-v-motorized-potentiometer)
- [G120 CU250S-2 V motorized potentiometer ramp-function generator](#g120-cu250s-2-v-motorized-potentiometer-ramp-function-generator)

#### G120 CU250S-2 V motorized potentiometer

##### Parameterizing the motorized potentiometer

The motorized potentiometer enables speed control of the motor. You specify the speed, e.g. via analog inputs, and then transfer these values to the motor via a ramp-function generator. The function is intended for manual control of the drive or for automatic speed specification. Switch from automatic mode to manual mode, for example, to traverse the motor. The ramp-function generator of the motorized potentiometer can be switched off in automatic operation.

- With manual control, you manually specify the setpoint via a digital input, for example.
- In automatic mode, a higher-level controller, for example, specifies the setpoint. You then interconnect the signal source via BICO.

See also [Motorized potentiometer as setpoint source](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#motorized-potentiometer-as-setpoint-source).

##### Setpoint higher/lower

1. "Setpoint higher" ([p1035](SINAMICS%20Parameter%20G120.md#p10350n-bi-motorized-potentiometer-setpoint-raise-3)); signal source to increase the setpoint.
2. "Setpoint lower" ([p1036](SINAMICS%20Parameter%20G120.md#p10360n-bi-motorized-potentiometer-lower-setpoint-3)); signal source to decrease the setpoint.

##### Maximum value / minimum value

1. To specify limit values for the speed setpoint in manual mode, enter a maximum value ([p1037](SINAMICS%20Parameter%20G120.md#p10370n-motorized-potentiometer-maximum-speed)) or minimum value ([p1038](SINAMICS%20Parameter%20G120.md#p10380n-motorized-potentiometer-minimum-speed)).

   The "Maximum speed" or "Minimum speed" is not overshot or undershot when using the motorized potentiometer.
2. "Invert" ([p1039](SINAMICS%20Parameter%20G120.md#p10390n-bi-motorized-potentiometer-inversion)); signal source to invert the minimum or maximum setpoint.

##### Automatic setpoint / manual

1. "Automatic setpoint" ([p1041](SINAMICS%20Parameter%20G120.md#p10410n-bi-motorized-potentiometer-manualautomatic)) signal source for the setpoint in automatic mode.

   The motorized potentiometer is effective in manual mode, the speed setpoint is specified via the "Automatic setpoint" in automatic mode.
2. "Manual/Automatic" (p1041); signal source for switching from manual to automatic mode.
3. Select whether you want to use the ramp-function generator in automatic mode at "Ramp-function generator active for automatic mode".

##### Saving the setpoint

The output of the motorized potentiometer [r1050](SINAMICS%20Parameter%20G120.md#r1050-co-motorized-potentiometer-setpoint-after-ramp-function-generator) is saved after OFF and the motorized potentiometer is set to the saved value after ON if [p1030](SINAMICS%20Parameter%20G120.md#p10300n-motorized-potentiometer-configuration).0 = 1. The ramp-function generator of the motorized potentiometer moves from this start value in the direction of the new setpoint. With p1030.0 a decision is made as to whether the ramp-function generator of the motorized potentiometer is based on the motorized potentiometer output that was valid before the OFF command or on a start value specified by [p1040](SINAMICS%20Parameter%20G120.md#p10400n-motorized-potentiometer-starting-value). Parameter p1030.3 decides whether or not the setpoint is stored in a non-volatile memory.

- Click "Saving active" (p1030.0) to store the setpoint in the volatile memory (not in power-independent manner).
- Click "Saving to NVRAM active" (p1030.3) to save the setpoint in the non-volatile memory.

For saving important data, the inverter has a NVRAM (Non-Volatile Random Access Memory). The setpoint of the motorized potentiometer is stored in power-independent manner there.   
The value is re-loaded after PowerOn and specified as the start value after OFF1 enable.  
Saving in NVRAM only occurs if p1030.0=1 and p1030.3=1, i.e. if "Yes" is selected in both drop-down menus.

##### Function diagrams (FD)

- Control word, sequence control (r0898) - 2501 -
- Motorized potentiometer - 3020 -

##### Additional parameters

---

#### G120 CU250S-2 V motorized potentiometer ramp-function generator

##### Parameterizing the ramp-function generator of the motorized potentiometer

The ramp-function generator (RFG) ramps the speed setpoint up and down without acceleration jumps. The inverter increases or decreases the speed value via a defined acceleration/deceleration ramp until the speed setpoint is reached.

##### Initial rounding active ([p1030](SINAMICS%20Parameter%20G120.md#p10300n-motorized-potentiometer-configuration))

An initial rounding results in an S-shaped ramp which provides smooth transitions for acceleration and deceleration.

- To interconnect a fixed specified rounding, select "Yes" in the "Initial rounding active" drop-down list.

  The set ramp-up or ramp-down time can be exceeded with the initial rounding.

##### Ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down time parameters, whereby these refer to the speed limit n max.

1. Enter a value for the ramp-up time ([p1047](SINAMICS%20Parameter%20G120.md#p10470n-motorized-potentiometer-ramp-up-time)). The smaller the value, the faster the drive accelerates.
2. Enter a value for the ramp-down time ([p1048](SINAMICS%20Parameter%20G120.md#p10480n-motorized-potentiometer-ramp-down-time)). The smaller the value, the faster the drive decelerates.

##### Setting value

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the motorized potentiometer setting value.

1. "Accept setting value" ([p1043](SINAMICS%20Parameter%20G120.md#p10430n-bi-motorized-potentiometer-accept-setting-value)); signal source to accept the setting value.
2. "Setting value" ([p1044](SINAMICS%20Parameter%20G120.md#p10440n-ci-motorized-potentiometer-setting-value)); signal source for the setting value at the motorized potentiometer.

##### Start value

Enter a start value ([p1040](SINAMICS%20Parameter%20G120.md#p10400n-motorized-potentiometer-starting-value)) for the motorized potentiometer. The ramp-function generator of the motorized potentiometer moves from this start value in the direction of the new setpoint.

##### Function diagrams (FD)

- Control word, sequence control (r0898) - 2501 -
- Motorized potentiometer - 3020 -

##### Additional parameters

---

### G120 CU250S-2 V fixed setpoints and fixed setpoint interconnection

#### Using fixed setpoints

Assign free speed setpoints as fixed setpoints. The values entered here are transferred directly to the motor. To activate the appropriate fixed speeds, interconnect the signals to digital inputs. See also [Fixed speed as setpoint source](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#fixed-speed-as-setpoint-source).

#### Fixed speed selection ([p1016](SINAMICS%20Parameter%20G120.md#p1016-fixed-speed-setpoint-select-mode-1))

1. Select whether the fixed speed selection is to be performed via "Binary-coded fixed speed selection" or via "Fixed frequency selection with adder".

   - With "Binary-coded fixed speed selection", select the fixed speed via the four selection bits.
   - With "Fixed speed selection with adder", also select the fixed speed via the selection bits. If several fixed speeds are active, the speeds will be added.

#### Fixed speed activated

1. "Fixed speed activated" ([r1025](SINAMICS%20Parameter%20G120.md#r10250-bo-fixed-speed-setpoint-status)); signal source for display of the status of the fixed speeds (0/1 = off/on).
2. "Fixed speed 1...4" ([p1020](SINAMICS%20Parameter%20G120.md#p10200n-bi-fixed-speed-setpoint-selection-bit-0-2)...[p1023](SINAMICS%20Parameter%20G120.md#p10230n-bi-fixed-speed-setpoint-selection-bit-3-1)); signal source for setting the selection bits of the speed setpoint.

#### Fixed speed 1...4 "Direct selection"

1. Enter fixed speed setpoints in the "Fixed speed 1...4" fields.
2. The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.

#### Fixed speed 1…15 "Binary-coded selection"

1. Enter fixed speed setpoints in the "Fixed speed 1...15" fields.
2. The effective speed setpoint is then determined via the 0/1 combinations of the four selection bits.

#### Fixed speed active

"Fixed speed active" ([r1024](SINAMICS%20Parameter%20G120.md#r1024-co-fixed-speed-setpoint-effective-2)); signal source to display the active fixed speed setpoint.

#### Fixed setpoint interconnection

1. Enter fixed speed setpoints in the "Fixed value 1...15" ([p1001](SINAMICS%20Parameter%20G120.md#p10010n-co-fixed-speed-setpoint-1-1)...[p1015](SINAMICS%20Parameter%20G120.md#p10150n-co-fixed-speed-setpoint-15-1)) fields.
2. To set percentage values for the "Fixed value 1" or "2" ([p2900](SINAMICS%20Parameter%20G120.md#p29000n-co-fixed-value-1)...[p2901](SINAMICS%20Parameter%20G120.md#p29010n-co-fixed-value-2)), enter a value at "Fixed value 1" or "Fixed value 2". You can use the percentage fixed values, for example, as signal source for the scaling of the main or additional setpoint in the "Speed setpoint" screen form.
3. To enter a fixed torque value, enter a value at "Fixed value M" ([p2930](SINAMICS%20Parameter%20G120.md#p29300n-co-fixed-value-m-nm)).

These values are used as signal source to interconnect the fixed speed to another BICO signal.

#### Function diagrams (FD)

- Fixed speed setpoints, binary selection (p1016 = 2) - 3010 -
- Fixed speed setpoints, direct selection (p1016 = 1) - 3011 -

#### Additional parameters

---

### G120 CU250S-2 V speed setpoint

#### Parameterizing the speed setpoint

Parameterize the speed setpoint in the setpoint channel via the following properties:

- Main/additional setpoint and setpoint modification
- Jog
- Direction of rotation limitation and direction reversal

See also [Invert setpoint](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#invert-setpoint), [Inhibit direction of rotation](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#inhibit-direction-of-rotation) and [Running the motor in jog mode (JOG function)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#running-the-motor-in-jog-mode-jog-function).

The supplementary setpoint can be used to incorporate correction values from lower-level controllers. Both variables are imported simultaneously via two separate or one setpoint source and added in the setpoint channel.

#### Technology controller as speed setpoint

1. In order to use the technology controller output as main setpoint, select "Technology controller as main speed setpoint" ([p2251](SINAMICS%20Parameter%20G120.md#p2251-technology-controller-mode-2)) in the drop-down list.

   - Click the "PID" button to parameterize the technology controller.
2. In order to use the technology controller output as additional setpoint, select "Technology controller as additional speed setpoint" in the drop-down list.

   The technology controller output is then interconnected to the setpoint as additional setpoint in the "Ramp-function generator".

#### Main/additional setpoint and setpoint modification

1. "Main setpoint" ([p1070](SINAMICS%20Parameter%20G120.md#p10700n-ci-main-setpoint-7)); signal source for interconnection of the main setpoint.
2. "Main setpoint scaling" ([p1071](SINAMICS%20Parameter%20G120.md#p10710n-ci-main-setpoint-scaling)); signal source for scaling of the main setpoint. Interconnect, for example, "Fixed value 1" at "Fixed setpoint interconnection" as signal source.
3. "Additional setpoint" ([p1075](SINAMICS%20Parameter%20G120.md#p10750n-ci-supplementary-setp)); signal source for interconnection of the additional setpoint.
4. "Additional setpoint scaling" ([p1076](SINAMICS%20Parameter%20G120.md#p10760n-ci-supplementary-setpoint-scaling)); signal source for scaling of the additional setpoint. Interconnect, for example, "Fixed value 2" at "Fixed setpoint interconnection" as signal source.

#### Jog

"Jog" is oriented towards typical "finger tapping" with which you can traverse a motor through short taps. To traverse a motor via "Jog", e.g. a motor after a program interruption, enter speed setpoints in the following fields:

1. Enter a value for "Jog 1 speed setpoint" ([p1058](SINAMICS%20Parameter%20G120.md#p10580n-jog-1-speed-setpoint)).
2. Enter a value for "Jog 2 speed setpoint" ([p1059](SINAMICS%20Parameter%20G120.md#p10590n-jog-2-speed-setpoint)).
3. Alternatively, interconnect signal sources for Jog 1 and Jog 2:

   - "Jog bit 0" ([p1055](SINAMICS%20Parameter%20G120.md#p10550n-bi-jog-bit-0-1)); signal source for Jog 1
   - "Jog bit 1" ([p1056](SINAMICS%20Parameter%20G120.md#p10560n-bi-jog-bit-1-1)); signal source for Jog 2

#### Direction of rotation limitation and direction reversal

A direction reversal in the setpoint channel can be achieved by selecting the direction reversal [p1113](SINAMICS%20Parameter%20G120.md#p11130n-bi-setpoint-inversion-10). However, if the specification of a negative or positive setpoint via the setpoint channel is to be prevented, this can be disabled via parameter [p1110](SINAMICS%20Parameter%20G120.md#p11100n-bi-inhibit-negative-direction-1).

1. "Setpoint inversion" (p1113); signal source for setting the reversal of the direction of rotation.
2. "Disable negative direction" (p1110); signal source to disable the negative direction of rotation.

#### Speed limit setpoint channel

To limit the speed in the setpoint channel, enter a value for the "Speed limit setpoint channel".

#### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103276782987_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V speed limitation](#g120-cu250s-2-v-speed-limitation) |

#### Function diagrams (FD)

- Direction limitation and direction reversal - 3040 -
- Main/additional setpoint, setpoint scaling, jog - 3030 -

#### Additional parameters

---

---

**See also**

[Skip frequency bands and minimum speed](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#skip-frequency-bands-and-minimum-speed)

### G120 CU250S-2 V speed limitation

#### Parameterizing the speed limitation

Limit the speed setpoint by a minimum and maximum speed. Set skip values, e.g. to prevent mechanical resonance effects. See also [G120 CU250S-2 V speed setpoint](#g120-cu250s-2-v-speed-setpoint) and [Skip frequency bands and minimum speed](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#skip-frequency-bands-and-minimum-speed).

#### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/103276809611_DV_resource.Stream@PNG-en-US.png) | [Maximum speed](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#maximum-speed) |

#### Skip frequency bands

If a drive train has points of resonance in the range from 0 rpm to the setpoint speed, define skip frequency bands for these points. The skip frequency bands prevent operation of the drive at these points of resonance. Resonances can cause mechanical vibrations.

1. To define skip frequency bands, click the "Skip frequency bands" button.
2. Enter values in the Skip value 1...4 fields ([p1091](SINAMICS%20Parameter%20G120.md#p10910n-skip-speed-1)…[p1094](SINAMICS%20Parameter%20G120.md#p10940n-skip-speed-4)) in order to define up to four skip frequency bands.
3. Enter a value for the skip frequency band ([p1101](SINAMICS%20Parameter%20G120.md#p11010n-skip-speed-bandwidth)). This defines the bandwidth of the skip frequency bands 1...4.

   If you enter "0" as value, the input fields for the skip values are deactivated.

#### Minimum limitation

1. To enter a minimum value for the speed setpoint, click the "Minimum limitation" button.
2. Enter a value for the lower limit of the speed setpoint at "Minimum speed" ([p1080](SINAMICS%20Parameter%20G120.md#p10800n-minimum-speed)).

#### Maximum limitation

1. To enter a maximum value for the speed setpoint, click the "Maximum limitation" button.
2. "Speed limit of positive direction of rotation" ([p1051](SINAMICS%20Parameter%20G120.md#p10510n-ci-speed-limit-rfg-positive-direction-of-rotation-1)); signal source for interconnection of the speed limitation in the positive direction of rotation.
3. Enter a value for the upper limit of the speed setpoint at "Maximum speed" ([p1082](SINAMICS%20Parameter%20G120.md#p10820n-maximum-speed-3)).
4. "Speed limit of negative direction of rotation" ([p1052](SINAMICS%20Parameter%20G120.md#p10520n-ci-speed-limit-rfg-negative-direction-of-rotation-1)); signal source for interconnection of the speed limitation in the negative direction of rotation.

#### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103276812939_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V ramp-function generator](#g120-cu250s-2-v-ramp-function-generator) |

#### Function diagrams (FD)

- Skip frequency bands and speed limits - 3050 -

#### Additional parameters

---

### Ramp-function generator

This section contains information on the following topics:

- [G120 CU250S-2 V ramp-function generator](#g120-cu250s-2-v-ramp-function-generator)
- [G120 CU250S-2 V basic ramp-function generator](#g120-cu250s-2-v-basic-ramp-function-generator)
- [G120 CU250S-2 V extended ramp-function generator](#g120-cu250s-2-v-extended-ramp-function-generator)

#### G120 CU250S-2 V ramp-function generator

##### Parameterizing the ramp-function generator

A ramp-function generator is used to prevent sudden setpoint jumps and therefore abrupt acceleration. A change at the ramp-function generator input is passed on to the output via a defined ramp. See also [Ramp-function generator](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#ramp-function-generator-1).

##### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/103276782987_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V speed limitation](#g120-cu250s-2-v-speed-limitation) |

Select one of the following ramp-function generator types in the drop-down list:

- [G120 CU250S-2 V basic ramp-function generator](#g120-cu250s-2-v-basic-ramp-function-generator)

  The basic ramp-function generator passes on the input values to the output via linear ramps, i.e. there is no rounding at the start and end of the range, the speed setpoint is accelerated or decelerated linearly.
- [G120 CU250S-2 V extended ramp-function generator](#g120-cu250s-2-v-extended-ramp-function-generator)

  With the extended ramp-function generator, acceleration and deceleration are not linear.

Various enables are required for the ramp-function generator.

##### Enables

1. "Frequency setpoint enabled" ([p1142](SINAMICS%20Parameter%20G120.md#p11420n-bi-enable-setpointinhibit-setpoint-5)); signal source for enabling the frequency setpoint.
2. "Start ramp-function generator" ([p1141](SINAMICS%20Parameter%20G120.md#p11410n-bi-continue-ramp-function-generatorfreeze-ramp-function-generator-3)); signal source to start the ramp-function generator.

"OFF1 enable" and "OFF3 enable" are set via the control word "Sequential control system". Check the individual bits of the control word at "Diagnostics>Control/status words". Check the interconnection at "Diagnostics>Interconnections".

The control inputs of the ramp-function generator take effect as follows:

- 1st priority: OFF3
- 2nd priority: Ramp-function generator enable
- 3rd priority: Ramp-function generator start
- 4th priority: Setpoint enable

To view the status of the internal enables, click "Internal enables".

The following internal enables are required (r46):

- "OFF1 internal enable:" ([r0046](SINAMICS%20Parameter%20G120.md#r0046031-cobo-missing-enable-signal-4)[16] shows whether a fault response is present at OFF1. The enable is made only when the fault has been corrected and acknowledged, and the switching on inhibit removed with OFF1 = 0.
- "OFF3 internal enable:" (r0046[18]) shows whether an OFF3 has not yet been completed or an OFF3 fault response is present.
- "Power unit enable missing:" (r0046[21]) missing, when the pulse enable is present and the speed setpoint has not yet been enabled, because:

  - The power unit does not issue an enable (e.g. because DC-link voltage is too low)
  - The holding brake opening time ([p1216](SINAMICS%20Parameter%20G120.md#p1216-motor-holding-brake-opening-time)) has not yet expired
- "Enable operation missing:" (r0046[3]) shows that the signal source in [p0852](SINAMICS%20Parameter%20G120.md#p08520n-bi-enable-operationinhibit-operation-4) is a 0 signal.

##### PID controller operation

- In order to use the technology controller output as additional setpoint, select "Technology controller as additional speed setpoint" in the drop-down list.

  The technology controller output is then interconnected to the setpoint as additional setpoint in the "Ramp-function generator".

##### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103276864523_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V open-loop/closed-loop control type](#g120-cu250s-2-v-open-loopclosed-loop-control-type) |

##### Function diagrams (FD)

- Basic ramp-function generator - 3060 -
- Ramp-function generator selection, -status word, -tracking - 3080 -

##### Additional parameters

---

#### G120 CU250S-2 V basic ramp-function generator

##### Parameterizing the basic ramp-function generator

With the basic ramp-function generator, the input values are passed on to the output via linear ramps, i.e. there is no rounding at the start and end of the range; the drive is accelerated or decelerated linearly.

See also [Basic ramp-function generator](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#basic-ramp-function-generator).

##### Ramp-up time and ramp-down time

The ramp-function generator is parameterized via the ramp-up and ramp-down time parameters, whereby these refer to the speed limit n max.

1. Enter the maximum speed (maximum possible speed) at "n max" ([p1082](SINAMICS%20Parameter%20G120.md#p10820n-maximum-speed-3)).
2. Enter a value for the ramp-up time ([p1047](SINAMICS%20Parameter%20G120.md#p10470n-motorized-potentiometer-ramp-up-time)).
3. Enter a value for the ramp-down time ([p1048](SINAMICS%20Parameter%20G120.md#p10480n-motorized-potentiometer-ramp-down-time)).
4. Enter a value for the OFF3 ramp-down time ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)). This is the ramp-down time from maximum speed down to standstill for the OFF3 command.

##### Setting value

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the ramp-function generator setting value.

1. "Accept setting value" ([p1143](SINAMICS%20Parameter%20G120.md#p11430n-bi-ramp-function-generator-accept-setting-value-1)); signal source to accept the setting value.
2. "Setting value" ([p1144](SINAMICS%20Parameter%20G120.md#p11440n-ci-ramp-function-generator-setting-value-1)); signal source for the setting value at the ramp-function generator.

##### Function diagrams (FD)

- Basic ramp-function generator - 3060 -
- Ramp-function generator selection, -status word, -tracking - 3080 -

##### Additional parameters

---

#### G120 CU250S-2 V extended ramp-function generator

##### Parameterizing the extended ramp-function generator

The acceleration (deceleration) is linear. The acceleration can be described by a ramp for a set rounding (without rounding, the acceleration jumps to the value specified by the ramp-up or ramp-down time).

See also [Extended ramp-function generator](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#extended-ramp-function-generator).

##### Entering rounding parameters

1. Enter the maximum speed (maximum possible speed) at "n max" ([p1082](SINAMICS%20Parameter%20G120.md#p10820n-maximum-speed-3)).
2. Enter a value for the "Initial rounding 1" or 2 ([p1130](SINAMICS%20Parameter%20G120.md#p11300n-ramp-function-generator-initial-rounding-off-time-1)).
3. Enter a value for the "Final rounding 1" or 2 ([p1131](SINAMICS%20Parameter%20G120.md#p11310n-ramp-function-generator-final-rounding-off-time-1)).
4. Enter a value for the "Ramp-up time" ([p1120](SINAMICS%20Parameter%20G120.md#p11200n-ramp-function-generator-ramp-up-time-3)) to ramp up the speed setpoint from standstill to the maximum speed.
5. Enter a value for the "Ramp-down time" ([p1121](SINAMICS%20Parameter%20G120.md#p11210n-ramp-function-generator-ramp-down-time-5)) to ramp down the speed setpoint from the maximum speed to standstill.

##### OFF3-relevant parameters

When an OFF3 occurs, the drive is braked along the OFF3 deceleration ramp.

1. Enter a value for the "OFF3 ramp-down time" ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)). The value describes the ramp-down time from maximum speed to standstill with OFF3.
2. Enter a value for the "OFF3 initial rounding" ([p1136](SINAMICS%20Parameter%20G120.md#p11360n-off3-initial-rounding-off-time-1)).
3. Enter a value for the "OFF3 final rounding" ([p1137](SINAMICS%20Parameter%20G120.md#p11370n-off3-final-rounding-off-time)).

##### Ramp-function generator rounding type

To specify a rounding type, select one of the following options from the drop-down list:

- "Continuous smoothing" ([p1134](SINAMICS%20Parameter%20G120.md#p11340n-ramp-function-generator-rounding-off-type) = 0); the rounding is always active, i.e. when setpoint changes occur, they only take effective after the final rounding has been completed. This can result in overshoot.
- "Discontinuous smoothing"(p1134 = 1); a change in the setpoint causes a final rounding to be aborted. This prevents an overshoot. However, this can result in abrupt changes of the velocity/acceleration (jerk).

##### Effective ramp-up and ramp-down times

The "Effective ramp-up/ramp-down time" is calculated according to the following formula:

- Effective ramp-up time = ramp-up time + initial rounding/2 + final rounding/2
- Effective ramp-down time = ramp-down time + initial rounding/2 + final rounding/2

##### Setting values

Setting values are the values to which the ramp-function generator jumps automatically. You set the ramp-function generator output to the ramp-function generator setting value.

1. "Accept setting value" ([p1143](SINAMICS%20Parameter%20G120.md#p11430n-bi-ramp-function-generator-accept-setting-value-1)); signal source to accept the setting value.
2. "Setting value" ([p1144](SINAMICS%20Parameter%20G120.md#p11440n-ci-ramp-function-generator-setting-value-1)); signal source for the setting value at the ramp-function generator.

##### Function diagrams (FD)

- Extended ramp-function generator - 3070 -
- Ramp-function generator selection, -status word, -tracking - 3080 -

##### Additional parameters

---

## Selecting the operating mode

This section contains information on the following topics:

- [Setpoint addition](#setpoint-addition)
- [Open-loop/closed-loop control type](#open-loopclosed-loop-control-type)
- [Torque setpoints](#torque-setpoints)
- [Torque limiting](#torque-limiting)
- [Current controller / power unit](#current-controller-power-unit)
- [G120 CU250S-2 V motor](#g120-cu250s-2-v-motor)
- [Motor encoder](#motor-encoder)

### Setpoint addition

This section contains information on the following topics:

- [G120 CU250S-2 V setpoint addition](#g120-cu250s-2-v-setpoint-addition)
- [G120 CU250S-2 V interpolator](#g120-cu250s-2-v-interpolator)
- [G120 CU250S-2 V maximum limitation](#g120-cu250s-2-v-maximum-limitation)
- [G120 CU250S-2 V droop feedback](#g120-cu250s-2-v-droop-feedback)

#### G120 CU250S-2 V setpoint addition

##### Description

The additional setpoint can be used to enter correction values from higher-level closed-loop controls. This can be easily carried out using the addition point for the main/additional setpoint in the setpoint channel. Both variables are imported simultaneously via two separate or one setpoint source and added in the setpoint channel.

Speed setpoint 1and Speed setpoint 2can be added to the speed setpoint after the ramp-function generator.

##### Signal source

| Symbol | Meaning |
| --- | --- |
| Ramp-function generator | [G120 CU250S-2 V ramp-function generator](#g120-cu250s-2-v-ramp-function-generator) |

##### Speed setpoint 1 and speed setpoint 2

To connect additional setpoints, proceed as follows:

- Interconnect a signal source for speed setpoint 1 with [p1155](SINAMICS%20Parameter%20G120.md#p11550n-ci-speed-controller-speed-setpoint-1).
- Interconnect a signal source for speed setpoint 2 with [p1160](SINAMICS%20Parameter%20G120.md#p11600n-ci-speed-controller-speed-setpoint-2).

##### Display parameters

- [r0898](SINAMICS%20Parameter%20G120.md#r0898010-cobo-control-word-sequence-control).6 displays whether the setpoint is enabled.
- r898.4 displays whether the ramp-function generator is enabled.
- [r1169](SINAMICS%20Parameter%20G120.md#r1169-co-speed-controller-speed-setpoints-1-and-2) displays the speed setpoint after the addition of the additional setpoints.
- [r1150](SINAMICS%20Parameter%20G120.md#r1150-co-ramp-function-generator-speed-setpoint-at-the-output) displays the speed setpoint at the ramp-function generator output.
- [r1170](SINAMICS%20Parameter%20G120.md#r1170-co-speed-controller-setpoint-sum) displays the speed setpoint at the output of the setpoint addition.

##### Droop feedback ([p1488](SINAMICS%20Parameter%20G120.md#p14880n-droop-input-source))

If you have selected "Speed control" or "Torque control" as control type, the drop-down list for the selection of droop input is displayed:

The following options are possible:

- [0] Droop feedback not connected
- [1] Droop feedback of the torque setpoint
- [2] Droop feedback of the speed controller output
- [3] Droop feedback of the speed controller integral output

If option 1, 2 or 3 is selected, the button for the configuration of the droop feedback is displayed.

| Symbol | Meaning |
| --- | --- |
| ![Droop feedback (p1488)](images/103276987531_DV_resource.Stream@PNG-en-US.png) | Click the button to configure the[G120 CU250S-2 V droop feedback](#g120-cu250s-2-v-droop-feedback). |

##### Interpolator

| Symbol | Meaning |
| --- | --- |
| ![Interpolator](images/103276980107_DV_resource.Stream@PNG-en-US.png) | Click the button to configure the[G120 CU250S-2 V interpolator](#g120-cu250s-2-v-interpolator). |

##### Maximum limitation

| Symbol | Meaning |
| --- | --- |
| ![Maximum limitation](images/103276983819_DV_resource.Stream@PNG-en-US.png) | Click the button to configure the[G120 CU250S-2 V maximum limitation](#g120-cu250s-2-v-maximum-limitation). |

##### Function diagrams (FD)

- Ramp-function generator selection, -status word, -tracking - 3080 -

##### Additional parameters

---

#### G120 CU250S-2 V interpolator

##### Description

The switched on interpolator causes a finer grading of the speed setpoints from the ramp-function generator by calculating intermediate steps (interpolation).

Setpoint channel and PROFIBUS run in a slower time slice. The interpolator is used to linear interpolate the setpoints in the grid of the speed controller cycle. This avoids strong excitations caused by large steps in the speed setpoint.

- In the drop-down list (p1189), select whether the interpolator is to be active (default setting) or switched off.

##### Function diagrams (FD)

- Ramp-function generator selection, -status word, -tracking - 3080 -
- Interpolator - 3635 -

##### Additional parameters

---

#### G120 CU250S-2 V maximum limitation

##### Parameterizing the speed limitation

Limit the speed setpoint through a maximum speed. This is the maximum speed value the motor should have. A change of this value has an effect on the controller and ramp-function generator settings. There are other limitation variants, i.e. an individual fixed limit can be specified for the negative and the positive direction of rotation.

The value "n max pos" always has priority.

> **Note**
>
> **Changing the maximum speed**
>
> Changing the maximum speed [p1082](SINAMICS%20Parameter%20G120.md#p10820n-maximum-speed-3) has an effect on the following functions:
>
> - OFF3 deceleration ramp
> - Ramp-function generator
> - Motorized potentiometer

##### Parameters of the maximum limit

1. "Speed limit" ([p1051](SINAMICS%20Parameter%20G120.md#p10510n-ci-speed-limit-rfg-positive-direction-of-rotation-1)); signal source for interconnection of the speed limitation of the ramp-function generator in the positive direction of rotation.
2. "Speed limit in positive direction of rotation" ([p1085](SINAMICS%20Parameter%20G120.md#p10850n-ci-speed-limit-in-positive-direction-of-rotation)); signal source for interconnection of the speed limitation in the positive direction of rotation.
3. At "n max pos" ([p1083](SINAMICS%20Parameter%20G120.md#p10830n-co-speed-limit-in-positive-direction-of-rotation)), enter a value for the limitation of the positive speed setpoint.
4. At "Maximum speed" (p1082), enter a value for the maximum speed.
5. At "n max neg" ([p1086](SINAMICS%20Parameter%20G120.md#p10860n-co-speed-limit-in-negative-direction-of-rotation)), enter a value for the limitation of the negative speed setpoint.
6. "Speed limit in negative direction of rotation" ([p1088](SINAMICS%20Parameter%20G120.md#p10880n-ci-speed-limit-in-negative-direction-of-rotation)); signal source for interconnection of the speed limitation in the negative direction of rotation.
7. "Speed limit RFG negative direction of rotation" ([p1052](SINAMICS%20Parameter%20G120.md#p10520n-ci-speed-limit-rfg-negative-direction-of-rotation-1)); signal source for interconnection of the speed limitation of the ramp-function generator in the negative direction of rotation.

##### Function diagrams (FD)

- Skip frequency bands and speed limits - 3050 -

##### Additional parameters

---

#### G120 CU250S-2 V droop feedback

##### Parameterizing the droop feedback

The droop ensures that the speed setpoint is reduced proportionately as the load torque increases.

See also [Advanced settings](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#advanced-settings).

##### Signal source ([p1488](SINAMICS%20Parameter%20G120.md#p14880n-droop-input-source))

| Symbol | Meaning |
| --- | --- |
| Droop of the torque setpoint | [G120 CU250S-2 V torque setpoint](#g120-cu250s-2-v-torque-setpoint) |
| Droop of the speed controller output | [G120 CU250S-2 V speed controller](#g120-cu250s-2-v-speed-controller) |

##### Droop feedback

1. "Droop feedback enable" ([p1492](SINAMICS%20Parameter%20G120.md#p14920n-bi-droop-feedback-enable)); signal source to enable the droop feedback.
2. To scale the droop feedback, enter a value for "Droop scaling" ([p1489](SINAMICS%20Parameter%20G120.md#p14890n-droop-feedback-scaling)).

##### Droop compensation torque

1. Enter a value at "Droop compensation torque scaling" ([p1487](SINAMICS%20Parameter%20G120.md#p14870n-droop-compensation-torque-scaling)) to scale the compensation torque within the droop calculation.
2. "Droop compensation torque" ([p1486](SINAMICS%20Parameter%20G120.md#p14860n-ci-droop-compensation-torque)); signal source for setting the compensation torque.

##### Function diagrams (FD)

- #Speed setpoint, droop - 6030 -

##### Additional parameters

---

### Open-loop/closed-loop control type

This section contains information on the following topics:

- [G120 CU250S-2 V open-loop/closed-loop control type](#g120-cu250s-2-v-open-loopclosed-loop-control-type)
- [Speed controller](#speed-controller)
- [V/f control](#vf-control)
- [Torque control](#torque-control)

#### G120 CU250S-2 V open-loop/closed-loop control type

##### Setting the open-loop/closed-loop control types

There are two different open-loop control or closed-loop control methods for induction motors:

| Symbol | Meaning |
| --- | --- |
| ![Setting the open-loop/closed-loop control types](images/103277159179_DV_resource.Stream@PNG-en-US.png) | Control with V/f characteristic ([G120 CU250S-2 V V/f control](#g120-cu250s-2-v-vf-control)) |
| ![Setting the open-loop/closed-loop control types](images/103277162507_DV_resource.Stream@PNG-en-US.png) | Field-oriented control (vector control - [G120 CU250S-2 V speed controller](#g120-cu250s-2-v-speed-controller)) |

To set the open-loop/closed-loop control type, select the corresponding entry in the drop-down list (p1300).

##### Decisive criterion

V/f control is perfectly suitable for almost all applications in which the speed of induction motors is to be changed. Examples of applications in which V/f control is typically used:

- Pumps
- Fans
- Compressors
- Horizontal conveyors

The commissioning of vector control takes more time than the commissioning of V/f control. However, in comparison to V/f control, vector control has the following advantages:

- The speed is more stable for motor load changes.
- Shorter ramp-up times when the setpoint changes.
- Acceleration and deceleration are possible with an adjustable maximum torque.
- Improved protection of the motor and the driven machine as a result of the adjustable torque limiting.
- Full torque is possible at standstill.
- Torque control is only possible with vector control.

#### Speed controller

This section contains information on the following topics:

- [G120 CU250S-2 V speed controller](#g120-cu250s-2-v-speed-controller)
- [SINAMICS G120 CU250S-2 V precontrol](#sinamics-g120-cu250s-2-v-precontrol)

##### G120 CU250S-2 V speed controller

###### Parameterizing the speed controller

The G120 CU250S-2 uses sensorless closed-loop speed control (SLVC); it contains the following components:

- PI controller
- Speed controller precontrol
- Droop

The sum of the output variables forms the torque setpoint which is reduced to a permissible size by means of the torque setpoint limitation. See also [Setting and optimizing the speed controller](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-and-optimizing-the-speed-controller), [Properties of the vector control](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#properties-of-the-vector-control) and [Advanced settings](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#advanced-settings).

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/103277219083_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V setpoint addition](#g120-cu250s-2-v-setpoint-addition) |

###### Control type and speed controller optimization

1. Select the control type in the "Control type" ([p1300](SINAMICS%20Parameter%20G120.md#p13000n-open-loopclosed-loop-control-operating-mode-13)) drop-down list, e.g. sensorless closed-loop speed control.
2. In the "Speed optimization at the next ON command" ([p1960](SINAMICS%20Parameter%20G120.md#p1960-rotating-measurement-selection-3)), whether you want to optimize the speed controller or determine and optimize the motor data. In addition to the motor data identification, these measurements are also used for the self-optimization of the speed control.

   The following options are available for this:

- [0] Disabled, the optimization is deactivated
- [1] Rotating measurement in encoderless operation
- [2] Rotating measurement with encoder
- [3] Speed controller optimization with encoderless operation
- [4] Speed controller optimization with encoder

###### PI speed controller

1. Enter the gain factor for the PI speed controller at "P gain factor" ([p1470](SINAMICS%20Parameter%20G120.md#p14700n-speed-controller-encoderless-operation-p-gain-1)).
2. Enter the integral time for the PI speed controller at "Integration time" ([p1472](SINAMICS%20Parameter%20G120.md#p14720n-speed-controller-encoderless-operation-integral-time)).
3. The speed controller deviation is displayed at r64.
4. The torque setpoint before the additional torque is displayed at [r1508](SINAMICS%20Parameter%20G120.md#r1508-co-torque-setpoint-before-supplementary-torque-2).

###### Actual speed value

To form the controller deviation, the actual speed value is either supplied by a motor encoder (closed-loop control with encoder) or a calculated value is used.

1. Enter the smoothing time for the actual speed value at "Smoothing" ([p1452](SINAMICS%20Parameter%20G120.md#p14520n-speed-controller-speed-actual-value-smoothing-time-sensorless)).
2. The smoothed actual speed value is displayed at [r1445](SINAMICS%20Parameter%20G120.md#r1445-co-actual-speed-smoothed).
3. The non-smoothed actual speed value is displayed at r61.

###### Precontrol

| Symbol | Meaning |
| --- | --- |
| ![Precontrol](images/103277235595_DV_resource.Stream@PNG-en-US.png) | [SINAMICS G120 CU250S-2 V precontrol](#sinamics-g120-cu250s-2-v-precontrol) |

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103277215755_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V torque setpoint](#g120-cu250s-2-v-torque-setpoint) |

###### Function diagrams (FD)

- Speed controller - 6040 -
- Kp_n/Tn_n adaptation - 6050 -

###### Additional parameters

---

---

**See also**

[G120 CU250S-2 V droop feedback](#g120-cu250s-2-v-droop-feedback)

##### SINAMICS G120 CU250S-2 V precontrol

###### Parameterizing the precontrol

The command behavior of the speed control loop is improved when the acceleration torque is calculated from the speed setpoint and the speed controller is series-connected.

###### Motor moment of inertia and scaling

The motor moment of inertia [p0341](SINAMICS%20Parameter%20G120.md#p03410n-motor-moment-of-inertia-1) is calculated directly during the commissioning or the complete parameterization ([p0340](SINAMICS%20Parameter%20G120.md#p03400n-automatic-calculation-motorcontrol-parameters-2) = 1). The factor [p0342](SINAMICS%20Parameter%20G120.md#p03420n-ratio-between-the-total-and-motor-moment-of-inertia-1) between the total moment of inertia J and the motor moment of inertia is determined manually or via the speed controller optimization. The acceleration is calculated from the speed difference over time dn/dt.

1. To specify the motor moment of inertia (p341), enter a value at "Motor moment of inertia".
2. To calculate the inertia of the total system, enter a value at "Motor inertia" (p342).
3. To adapt the effect of the precontrol variable depending on the application, enter the weighting factor [%] at "Scaling" ([p1496](SINAMICS%20Parameter%20G120.md#p14960n-acceleration-precontrol-scaling-2)).

###### Function diagrams (FD)

- Precontrol symmetrization, acceleration model - 6031 -
- Speed controller - 6040 -

###### Additional parameters

---

#### V/f control

This section contains information on the following topics:

- [G120 CU250S-2 V V/f control](#g120-cu250s-2-v-vf-control)
- [G120 CU250S-2 V V/F control characteristics](#g120-cu250s-2-v-vf-control-characteristics)
- [G120 CU250S-2 V V/f characteristic settings](#g120-cu250s-2-v-vf-characteristic-settings)
- [G120 CU250S-2 V V/f control I_max controller](#g120-cu250s-2-v-vf-control-i_max-controller)
- [G120 CU250S-2 V slip compensation](#g120-cu250s-2-v-slip-compensation)

##### G120 CU250S-2 V V/f control

###### Description

The simplest solution for a control procedure is the V/f curve. Whereby the stator voltage for the induction motor or synchronous motor is controlled proportionately to the stator frequency. This method has proved successful in a wide range of applications with low dynamic requirements, such as:

- Pumps and fans,
- Belt drives
- and other similar processes.

See also [Properties of V/f control](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#properties-of-vf-control), [Characteristics of V/f control](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#characteristics-of-vf-control) and [Selecting the V/f characteristic](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#selecting-the-vf-characteristic).

###### Signal sources

| Symbol | Meaning |
| --- | --- |
| ![Signal sources](images/103277298571_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V ramp-function generator](#g120-cu250s-2-v-ramp-function-generator) |

| Symbol | Meaning |
| --- | --- |
| ![Signal sources](images/103277305227_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V V/f control I_max controller](#g120-cu250s-2-v-vf-control-i_max-controller) |

###### Parameterizing V/f control

1. To activate the V/f control, select one of the entries for the "V/f control" in the drop-down list ([p1300](SINAMICS%20Parameter%20G120.md#p13000n-open-loopclosed-loop-control-operating-mode-13)).
2. The voltage output on the I_max controller is displayed at [r1344](SINAMICS%20Parameter%20G120.md#r1344-i_max-controller-voltage-output-1).
3. The frequency output of the I_max controller is displayed at [r1343](SINAMICS%20Parameter%20G120.md#r1343-co-i_max-controller-frequency-output-1).
4. The smoothed voltage at the output is displayed at r72.
5. The setpoint sum of the speed controller is displayed at [r1170](SINAMICS%20Parameter%20G120.md#r1170-co-speed-controller-setpoint-sum).
6. The non-smoothed actual speed value is displayed at r63.
7. The smoothed output frequency is displayed at r24.

###### Screen forms that can be called

1. To parameterize the V/f characteristic of the selected V/f control, click the [V/f characteristic](#g120-cu250s-2-v-vf-control-characteristics) button.
2. To parameterize the [slip compensation](#g120-cu250s-2-v-slip-compensation), click the button with the same name.

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103277301899_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V current controller / power unit](#g120-cu250s-2-v-current-controller-power-unit) |

###### Function diagrams (FD)

- U/f control, overview - 6300 -

###### Additional parameters

- ---

##### G120 CU250S-2 V V/F control characteristics

###### Description

At low output frequencies, the V/f characteristics supply only a low output voltage. Along with the influence of the ohmic resistance at low frequencies, this can result in a too low output voltage. To counteract this, a voltage boost can be set to achieve the following:

- Implement the magnetization of the induction motor
- Maintain the load
- Compensate for the losses (ohmic losses in the winding resistors) in the system
- Generate a breakaway/acceleration/braking torque

See also [Characteristics of V/f control](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#characteristics-of-vf-control).

###### V/f control with linear characteristic ([p1300](SINAMICS%20Parameter%20G120.md#p13000n-open-loopclosed-loop-control-operating-mode-13) = 0)

Standard case

###### V/f control with linear characteristic and FCC (flux current control) (p1300 = 1)

Characteristic that compensates for voltage losses in the stator resistance for static/dynamic loads (flux current control FCC). This is particularly useful for small motors, since they have a relatively high stator resistance.

###### V/f control with parabolic characteristic (p1300 = 2)

Characteristic that takes into account the motor torque curve (e.g. fan/pump).

- Square-law characteristic (f2 characteristic)
- Energy saving because the low voltage also results in small currents and losses

###### V/f control with linear characteristic Eco mode (p1300 = 4) or with parabolic characteristic (p1300 = 7)

The Eco mode is suitable for applications with a low dynamic response and allows energy savings of up to 40%.

It uses an algorithm that approaches the optimum operating point of the motor (essentially dependent on the load and the speed) in the range of 80 ... 125% of the setpoint voltage. The algorithm is activated when the setpoint is reached and remains unchanged for 5 s. It is deactivated when the setpoint changes or if the Vdc_max or Vdc_min controller is active. In such cases the inverter accelerates to 100% of the voltage setpoint.

###### Function diagrams (FD)

- U/f control, overview - 6300 -

###### Additional parameters

---

##### G120 CU250S-2 V V/f characteristic settings

###### Settings for the V/f characteristic ([p1300](SINAMICS%20Parameter%20G120.md#p13000n-open-loopclosed-loop-control-operating-mode-13) = 0 ... 7)

The following parameters can be set for the V/f characteristics:

1. To set a permanent voltage boost from standstill up to the rated speed, enter a value at "Permanent voltage boost" ([p1310](SINAMICS%20Parameter%20G120.md#p13100n-starting-current-voltage-boost-permanent-3)).
2. To set a speed-dependent voltage boost, enter a value at "Voltage boost when accelerating" ([p1311](SINAMICS%20Parameter%20G120.md#p13110n-starting-current-voltage-boost-when-accelerating-1)).

   The voltage boost disappears as soon as the setpoint is reached.
3. To set a voltage boost at start-up, enter a value at "Voltage boost when starting" ([p1312](SINAMICS%20Parameter%20G120.md#p13120n-starting-current-voltage-boost-when-starting-1)).

   The results in an additional voltage boost during start-up.

###### Function diagrams (FD)

- U/f control, overview - 6300 -

###### Additional parameters

---

##### G120 CU250S-2 V V/f control I_max controller

###### Parameterizing the I_max controller

To avoid overloads during motor operation, the inverter has a current limitation controller in the V/f characteristic operating mode. See also [Overcurrent protection](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#overcurrent-protection).

###### P gain and integral time

1. Enter the integration time constant of the I_max frequency controller at "Integral time" ([p1341](SINAMICS%20Parameter%20G120.md#p13410n-i_max-frequency-controller-integral-time-3)).
2. Enter the proportional gain of the I_max voltage controller at "Proportional gain" ([p1340](SINAMICS%20Parameter%20G120.md#p13400n-i_max-frequency-controller-proportional-gain)).
3. Enter a value for the current limit at "Current limit" ([p0640](SINAMICS%20Parameter%20G120.md#p06400n-current-limit-1)).
4. Enter a value for the proportional gain at "I_max voltage controller proportional gain" [p1345](SINAMICS%20Parameter%20G120.md#p13450n-i_max-voltage-controller-proportional-gain-1).
5. Enter a value for the integral time at "I_max voltage controller integral time" [p1346](SINAMICS%20Parameter%20G120.md#p13460n-i_max-voltage-controller-integral-time-1).
6. The maximum output current is displayed at r67.
7. The non-smoothed absolute value of the actual current value is displayed at r68.
8. The voltage output value on the I_max controller is displayed at [r1344](SINAMICS%20Parameter%20G120.md#r1344-i_max-controller-voltage-output-1).
9. The frequency output of the I_max controller is displayed at [r1343](SINAMICS%20Parameter%20G120.md#r1343-co-i_max-controller-frequency-output-1).

###### Function diagrams (FD)

- U/f control, overview - 6300 -

###### Additional parameters

---

##### G120 CU250S-2 V slip compensation

###### Parameterizing the slip compensation

The slip compensation ensures that the motor speed is kept constant irrespective of the load. Reduction of the motor speed with increasing load is a typical feature of induction motors.

Synchronous motors do not show this effect and the parameter has no effect here.

###### Activating the slip compensation

1. Enter the percentage setpoint of the slip compensation in relation to the rated motor slip at "Scaling" ([p1335](SINAMICS%20Parameter%20G120.md#p13350n-slip-compensation-scaling-4)). The slip compensation only becomes active when a scaling > 0.0% is entered.
2. Enter the percentage limitation of the slip compensation in relation to the rated motor slip at "Limit value" ([p1336](SINAMICS%20Parameter%20G120.md#p13360n-slip-compensation-limit-value-1)).
3. The frequency setpoint is displayed at r20.
4. The calculated actual speed value is displayed at r63.
5. The rated motor slip is displayed at [r0330](SINAMICS%20Parameter%20G120.md#r03300n-rated-motor-slip).
6. The actual slip compensation value is displayed at [r1337](SINAMICS%20Parameter%20G120.md#r1337-co-actual-slip-compensation-1).
7. The calculated actual slip compensation value is displayed at r1337.

###### Function diagrams

- U/f control, resonance damping and slip compensation - 6310 -

###### Additional parameters

---

#### Torque control

This section contains information on the following topics:

- [G120 CU250S-2 V torque control](#g120-cu250s-2-v-torque-control)

##### G120 CU250S-2 V torque control

###### Parameterizing the torque control

Torque control is part of the vector control and normally receives its setpoint from the speed controller output. By deactivating the speed controller and directly entering the torque setpoint, the speed control becomes torque control. The drive then no longer controls the motor speed but the torque that the motor generates. See also [Torque control](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#torque-control).

###### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/103277298571_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V ramp-function generator](#g120-cu250s-2-v-ramp-function-generator) |

###### PI torque controller

1. Enter the gain factor for the PI speed controller at "P gain factor" ([p1470](SINAMICS%20Parameter%20G120.md#p14700n-speed-controller-encoderless-operation-p-gain-1)).
2. Enter the integral time for the PI speed controller at "Integration time" ([p1472](SINAMICS%20Parameter%20G120.md#p14720n-speed-controller-encoderless-operation-integral-time)).
3. The speed controller deviation is displayed at r64.
4. The torque setpoint before the additional torque is displayed at [r1508](SINAMICS%20Parameter%20G120.md#r1508-co-torque-setpoint-before-supplementary-torque-2).

###### Actual speed value

To form the controller deviation, the actual speed value is either supplied by a motor encoder (closed-loop control with encoder) or a calculated value is used.

1. Enter the smoothing time for the actual speed value at "Smoothing" ([p1452](SINAMICS%20Parameter%20G120.md#p14520n-speed-controller-speed-actual-value-smoothing-time-sensorless)).
2. The smoothed actual speed value is displayed at [r1445](SINAMICS%20Parameter%20G120.md#r1445-co-actual-speed-smoothed).
3. The non-smoothed actual speed value is displayed at r61.

###### Precontrol

| Symbol | Meaning |
| --- | --- |
| ![Precontrol](images/103277235595_DV_resource.Stream@PNG-en-US.png) | [SINAMICS G120 CU250S-2 V precontrol](#sinamics-g120-cu250s-2-v-precontrol) |

###### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103277215755_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V torque setpoint](#g120-cu250s-2-v-torque-setpoint) for torque control with encoder  For torque control without encoder, the signal is passed on for the torque limiting. |

###### Function diagrams (FD)

- Speed controller - 6040 -
- Kp_n/Tn_n adaptation - 6050 -

###### Additional parameters

---

### Torque setpoints

This section contains information on the following topics:

- [G120 CU250S-2 V torque setpoint](#g120-cu250s-2-v-torque-setpoint)
- [G120 CU250S-2 V torque limiting](#g120-cu250s-2-v-torque-limiting)

#### G120 CU250S-2 V torque setpoint

##### Parameterizing the torque setpoints

Edit the torque setpoint through scaling or by injecting a main setpoint. The supplementary torque acts for the torque control as well as for the speed control. This feature with the additional torque setpoint enables a precontrol torque to be implemented for speed control.

##### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/103277162507_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V open-loop/closed-loop control type](#g120-cu250s-2-v-open-loopclosed-loop-control-type) |

##### Parameterizing the supplementary torque

1. "Supplementary torque 1" ([p1511](SINAMICS%20Parameter%20G120.md#p15110n-ci-supplementary-torque-1)); signal source to interconnect the supplementary torque 1.
2. "Supplementary torque 1 scaling" ([p1512](SINAMICS%20Parameter%20G120.md#p15120n-ci-supplementary-torque-1-scaling)); signal source for scaling the supplementary torque 1.
3. "Supplementary torque 2" ([p1513](SINAMICS%20Parameter%20G120.md#p15130n-ci-supplementary-torque-2)); signal source to interconnect the supplementary torque 2.
4. "Supplementary torque 2 scaling" ([p1514](SINAMICS%20Parameter%20G120.md#p15140n-supplementary-torque-2-scaling)); input of the scaling for the supplementary torque 2.

##### Parameterizing the torque

1. "Torque setpoint" ([p1503](SINAMICS%20Parameter%20G120.md#p15030n-ci-torque-setpoint)); signal source to interconnect the torque setpoint.
2. "Speed/torque control" ([p1501](SINAMICS%20Parameter%20G120.md#p15010n-bi-change-over-between-closed-loop-speedtorque-control)); signal source for switching between speed and torque control.

##### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103277515275_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V motor](#g120-cu250s-2-v-motor) |

##### Function diagrams (FD)

- Torque setpoint - 6060 -

##### Additional parameters

---

---

**See also**

[G120 CU250S-2 V motor](#g120-cu250s-2-v-motor)

#### G120 CU250S-2 V torque limiting

##### Parameterizing the torque limiting

If the torque limits are specified externally (e.g. tension controller), the drive can only be shut down with a specified torque (generally not the maximum torque). It is possible to switch over to the maximum torque via the torque limit extension.

If the drive is not shut down within the parameterized deceleration time, the infeed switches off and the drive coasts to a standstill.

##### Scaling the torque limits

You can set externally specified torque limits individually for the drive via the scaling of the torque limits.

1. "Torque limit upper scaling without offset" ([p1552](SINAMICS%20Parameter%20G120.md#p15520n-ci-torque-limit-upper-scaling-without-offset)); signal source for scaling an externally specified upper torque limit.
2. "Torque limit lower scaling without offset" ([p1554](SINAMICS%20Parameter%20G120.md#p15540n-ci-torque-limit-lower-scaling-without-offset)); signal source for scaling an externally specified lower torque limit.

##### Function diagrams (FD)

- Torque setpoint - 6060 -

##### Additional parameters

---

### Torque limiting

This section contains information on the following topics:

- [G120 CU250S-2 V torque limiting](#g120-cu250s-2-v-torque-limiting-1)
- [G120 CU250S-2 V upper torque limit](#g120-cu250s-2-v-upper-torque-limit)
- [G120 CU250S-2 V current limitation](#g120-cu250s-2-v-current-limitation)
- [G120 CU250S-2 V power limit](#g120-cu250s-2-v-power-limit)
- [G120 CU250S-2 V lower torque limit](#g120-cu250s-2-v-lower-torque-limit)

#### G120 CU250S-2 V torque limiting

##### Description

All limits act on the torque setpoint, which is either available at the speed controller output in the case of speed control, or as torque input with torque control. The minimum or the maximum is used from the various limits. This minimum/maximum is calculated cyclically and displayed in parameters [r1538](SINAMICS%20Parameter%20G120.md#r1538-co-upper-effective-torque-limit) and [r1539](SINAMICS%20Parameter%20G120.md#r1539-co-lower-effective-torque-limit-1).

- r1538 CO: Upper effective torque limit
- r1539 CO: Lower effective torque limit

These cyclic values therefore limit the torque setpoint at the speed controller output / torque input or display the instantaneous maximum possible torque.

##### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/103277215755_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V torque setpoint](#g120-cu250s-2-v-torque-setpoint) |

The torque limiting can be parameterized via the following dialog boxes:

- [G120 CU250S-2 V upper torque limit](#g120-cu250s-2-v-upper-torque-limit)
- [G120 CU250S-2 V current limitation](#g120-cu250s-2-v-current-limitation)
- [G120 CU250S-2 V power limit](#g120-cu250s-2-v-power-limit)
- [G120 CU250S-2 V lower torque limit](#g120-cu250s-2-v-lower-torque-limit)

##### Torque limit

The "Torque limit" dialog box shows the applied current upper and lower torque limits.

- Click the "Torque limiting" button to display the upper and lower torque limits.

##### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103277301899_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V current controller / power unit](#g120-cu250s-2-v-current-controller-power-unit) |

##### Function diagrams (FD)

- Upper/lower torque limit - 6630 -
- Current/power/torque limits - 6640 -

##### Additional parameters

---

#### G120 CU250S-2 V upper torque limit

##### Parameterizing the upper torque limit

Parameterize the fixed upper torque limit.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **"Motor runs away"**  Negative values when setting the upper torque limit can result in motor "runaway". |  |

##### Parameterizing the upper torque limit

1. Enter a value for the fixed upper torque limit in "Torque limit upper" ([p1520](SINAMICS%20Parameter%20G120.md#p15200n-co-torque-limit-upper)).
2. "Torque limit upper" ([p1522](SINAMICS%20Parameter%20G120.md#p15220n-ci-torque-limit-upper)); signal source to interconnect the fixed upper torque limit.
3. Enter a value for the scaling of the upper torque limit in "Scaling" ([p1524](SINAMICS%20Parameter%20G120.md#p15240n-co-torque-limit-uppermotoring-scaling)).
4. "Torque limit upper scaling" ([p1528](SINAMICS%20Parameter%20G120.md#p15280n-ci-torque-limit-upper-scaling-1)); signal source for interconnecting the scaling for the upper torque limit.

##### Function diagrams (FD)

- Upper/lower torque limit - 6630 -
- Current/power/torque limits - 6640 -

##### Additional parameters

---

#### G120 CU250S-2 V current limitation

##### Parameterizing the current limitation

Parameterize the limits for the torque-producing current. At the most the torque-producing current may be equal to the maximum permissible motor current. The smaller value of both applies.

The current limitation also limits the maximum available torque, i.e. if a greater torque has to be reached, the current limit also has to be adjusted.

##### Procedure

1. To parameterize the current limitation, enter a value in "Current limit" ([p0640](SINAMICS%20Parameter%20G120.md#p06400n-current-limit-1)).
2. The parameter is part of the basic commissioning and is preassigned appropriately at change of ([p0305](SINAMICS%20Parameter%20G120.md#p03050n-rated-motor-current)).

##### Function diagrams (FD)

- Upper/lower torque limit - 6630 -
- Current/power/torque limits - 6640 -

##### Additional parameters

---

#### G120 CU250S-2 V power limit

##### Parameterizing the power limit

Parameterize a value for the maximum available power.

##### Procedure

1. Enter a value in "Power limit motoring" ([p1530](SINAMICS%20Parameter%20G120.md#p15300n-power-limit-motoring-1)). The motoring power is the power taken from the DC link.
2. Enter a value in "Power limit regenerative" ([p1531](SINAMICS%20Parameter%20G120.md#p15310n-power-limit-regenerative-1)). The regenerative power is fed back from the drive to the DC link.

##### Function diagrams (FD)

- Upper/lower torque limit - 6630 -
- Current/power/torque limits - 6640 -

##### Additional parameters

---

#### G120 CU250S-2 V lower torque limit

##### Parameterizing the lower torque limit

Parameterize the lower torque limit.

| Symbol | Meaning |
| --- | --- |
|  | **Danger** |
| **"Motor runs away"**  Positive values when setting the lower torque limit can result in motor "runaway". |  |

##### Parameterizing the lower torque limit

1. Enter a value for the fixed lower torque limit in "Torque limit lower" ([p1521](SINAMICS%20Parameter%20G120.md#p15210n-co-torque-limit-lower)).
2. "Torque limit lower" ([p1523](SINAMICS%20Parameter%20G120.md#p15230n-ci-torque-limit-lower)); signal source to interconnect the fixed lower torque limit.
3. Enter a value for the scaling of the lower torque limit in "Scaling" ([p1525](SINAMICS%20Parameter%20G120.md#p15250n-co-torque-limit-lower-scaling)).
4. "Torque limit lower scaling" ([p1528](SINAMICS%20Parameter%20G120.md#p15280n-ci-torque-limit-upper-scaling-1)); signal source for interconnecting the scaling for the lower torque limit.

##### Function diagrams (FD)

- Upper/lower torque limit - 6630 -
- Current/power/torque limits - 6640 -

##### Additional parameters

---

### Current controller / power unit

This section contains information on the following topics:

- [G120 CU250S-2 V current controller / power unit](#g120-cu250s-2-v-current-controller-power-unit)
- [G120 CU250S-2 V power unit / operating values](#g120-cu250s-2-v-power-unit-operating-values)

#### G120 CU250S-2 V current controller / power unit

##### Description

No settings are required for operating the current controller. After initial start-up, the current controller is sufficiently optimized for most applications. The settings of the controller can be further optimized for special application cases.

##### Startup current (encoderless vector control)

Here you set the parameters for the startup current of the drive.

1. Enter a value in % under "Static torque setpoint" (p1610). In this way, you set the torque setpoint for low speeds for encoderless vector control.
2. Enter a value in % under "Supplementary acceleration torque" (p1611). In this way, you set the dynamic torque setpoint for low speeds for encoderless vector control.
3. At "Smoothing" (p1616), enter a value for the smoothing time of the current setpoint.

##### Signal source

| Symbol | Meaning |
| --- | --- |
| ![Signal source](images/103277515275_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V torque limiting](#g120-cu250s-2-v-torque-limiting-1) |

##### PWM

Click the "PWM" button to set the parameters for the "Power unit / operating values".

##### Signal processing

| Symbol | Meaning |
| --- | --- |
| ![Signal processing](images/103277705867_DV_resource.Stream@PNG-en-US.png) | [G120 CU250S-2 V motor](#g120-cu250s-2-v-motor) |

##### Function diagrams (FD)

- Iq and Id controller - 6714 -
- Id setpoint (PMSM, p0300 = 2xx) - 6721 -

#### G120 CU250S-2 V power unit / operating values

##### Setting the power unit / operating values

Parameterize the operating values of the power unit.

##### Procedure

1. Enter the value for the pulse frequency setpoint (inverter switching frequency) at "Pulse frequency" ([p1800](SINAMICS%20Parameter%20G120.md#p18000n-pulse-frequency-setpoint-2)).
2. "Actual pulse frequency" ([r1801](SINAMICS%20Parameter%20G120.md#r180101-co-pulse-frequency)); displays the current pulse frequency.
3. Select one of the following settings in the "Modulator mode" ([p1802](SINAMICS%20Parameter%20G120.md#p18020n-modulator-mode-18)) drop-down list (the selection depends on the Power Module):

   - Automatic changeover SVM/FLB
   - Space vector modulation (SVM)
   - SVM without overcontrol
   - SVM/FLB without overcontrol
   - SVM/FLB with modulation depth reduction
   - Optimized pulse patterns
4. Enter the value for the maximum modulation at "Maximum modulation depth" ([p1803](SINAMICS%20Parameter%20G120.md#p18030n-maximum-modulation-depth-5)).
5. To adapt the motor direction of rotation without setpoint inversion, select "Reverse the output phase sequence" ([p1820](SINAMICS%20Parameter%20G120.md#p18200n-reverse-the-output-phase-sequence-1)) in the drop-down list:

   - "ON"; the motor direction of rotation is reversed
   - "OFF"; the motor direction of rotation remains

##### Function diagrams (FD)

- Iq and Id controller - 6714 -
- Id setpoint (PMSM, p0300 = 2xx) - 6721 -

##### Additional parameters

---

### G120 CU250S-2 V motor

#### Description

The parameters of the motor are clearly displayed here:

- Output voltage; smoothed output voltage (r25)
- Output current; smoothed actual current absolute value (r27)
- Torque; smoothed actual torque value (r31)
- Power; smoothed actual active power value (r32)
- Actual speed; smoothed actual speed value (r21)
- Speed setpoint; smoothed speed setpoint (r20)
- Motor temperature (r35)

The current data is displayed in online mode.

#### Additional parameters

---

### Motor encoder

This section contains information on the following topics:

- [G120 CU250S-2 V motor encoder](#g120-cu250s-2-v-motor-encoder)
- [G120 CU250S-2 encoder data](#g120-cu250s-2-encoder-data)
- [ENDAT + SIN/COS encoder](#endat-sincos-encoder)
- [SSI encoder](#ssi-encoder)
- [TTL/HTL incremental encoder](#ttlhtl-incremental-encoder)
- [SIN/COS incremental encoders](#sincos-incremental-encoders)
- [Resolver](#resolver)

#### G120 CU250S-2 V motor encoder

##### Description

You define the parameters for speed value recording via the motor encoder here.

Amongst other things you can parameterize a smoothing of the speed value. This causes the variation peaks to be filtered.

> **Note**
>
> If you have not selected any encoder, you can do this later using the drive wizard, see also [Configuring the encoder](Running%20through%20the%20wizard.md#configuring-the-encoder).

**Encoder data**

- Click the "Encoder data" button to open the encoder data and details.

**Inversion**

- Click the "Invert" button to invert the actual speed value.

**Smoothing**

- Enter the "Smoothing time constant" [p1441](SINAMICS%20Parameter%20G120.md#p14410n-actual-speed-smoothing-time) for smoothing the actual speed value.

##### Function diagrams (FD)

- Position and temperature sensing, encoders 1 ... 2 - 4704 -
- Speed actual value and pole position sensing, ASM/PMSM motor encoder (encoder 1) - 4715 -
- Encoder interface, receive signals, encoder 1 ... 2 - 4720 -
- Encoder interface, send signals, encoder 1 ... 2 - 4730 -
- Reference mark search with equivalent zero mark, encoder 1 - 4735 -
- Absolute value for incremental encoder - 4750 -

##### Additional parameters

---

#### G120 CU250S-2 encoder data

##### Description

In this dialog box you specify the user-defined encoder data for external encoders. The encoders that can be used depend on the inverter used.

##### General

Enter the general encoder data for external encoders in this tab.

The technical data of the external encoder is on the encoder. Note the data and enter it or activate the appropriate options.

**Encoder type**

- Select whether you use a linear or a rotary encoder.

The following encoder measuring systems can be configured via the selection list:

> **Note**
>
> The setting options are dependent on the encoder type. Detailed descriptions of the setting options can be found in the online help for the encoder types.

- [ENDAT + SIN/COS encoder](#endat-sincos-encoder)
- [SSI encoder](#ssi-encoder)
- [TTL/HTL incremental encoder](#ttlhtl-incremental-encoder)
- [SIN/COS incremental encoders](#sincos-incremental-encoders)
- [Resolver](#resolver)

> **Note**
>
> The actual position values are normalized to encoder lines in the PROFIdrive profile. With the SSI encoder without incremental tracks, the single-turn resolution is taken over as the number of pulses per revolution as a substitute.

##### Details

You can specify further parameters for the selected encoders (motor and load encoders) (encoder 1 to 3) in this tab.

The data for the selected encoders will be transferred automatically.

**Gear ratio**

The gear ratio is the ratio of encoder revolutions to revolutions of the drive shaft.

> **Note**
>
> Parameters p432 and p433 are also used for indirect measuring systems and therefore have no relation to the motor.
>
> For example, the encoder for the indirect measuring system can be mounted for the position determination behind the load gearbox and also above a measuring gearbox.

**Inversion**

Because the installation direction of the encoder (at the right- or left-hand side) cannot be defined, but rather depends on the conditions of the machine (linear motor, torque motor, etc.), you can invert the position and the speed, and thus perform a direction reversal.

1. Activate the "Invert actual speed value" option to invert the actual speed value.
2. Activate the "Invert actual position value" option to invert the actual position value.

**Fine resolution**

- Specify the fine resolution of the incremental actual position values [bits]:

  - G1_IST1
  - G1_IST2 (only for absolute encoder)

#### ENDAT + SIN/COS encoder

##### Description

Absolute encoders (absolute shaft encoders) are designed on the same scanning principle as incremental encoders, but have a greater number of tracks. For example, if there are 13 tracks, then 2<sup>13</sup> = 8192 steps are coded for singleturn encoders. The code used is a one-step code (Gray code) which prevents any scanning errors from occurring. After switching on the machine, the position value is transferred immediately to the evaluation module. Data is transferred between the encoder and the evaluation module via EnDat.

Two protocols are supported:

- EnDat01; the encoders generally have a sin/cos track and are connected to SMx20, SME25 or SME125.
- Endat22; the encoders generally have no incremental tracks and are connected to SMC40.

> **Note**
>
> **EnDat encoder functional scope**
>
> SIEMENS does not support the full functional scope of EnDat encoder

A reference point approach is omitted, but an absolute encoder adjustment must be performed during the first commissioning with a higher-level controller or EPOS.

![EnDat absolute encoder](images/103277844619_DV_resource.Stream@PNG-en-US.png)

EnDat absolute encoder

**Identify encoder**

- Select the option if you want to fetch the encoder configuration from the encoder (only online).

**Incremental tracks**

The parameters for the number of pulses/revolution are transferred over the course of the encoder identification (for EnDat22, that corresponds to a virtual number of pulses).

##### Gear ratio / measuring gearbox

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

#### SSI encoder

##### SSI encoder

SSI encoders use the SSI protocol for the data transfer. The SSI protocol is a serial data transfer between an encoder and an evaluation module.

> **Note**
>
> **Data sheet of the encoder being used**
>
> To parameterize the SSI protocol, it is absolutely necessary that you have the encoder data sheet at hand. Use the information in the data sheet to set the protocol parameters. Not all encoders support the parameterizable functions.

**Encoder type SSI**

The following general parameters can be selected for the SSI encoder type:

- "Motor encoder": This option is selected for each first added encoder (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- "Rotary": Select this option when a rotatory encoder is available.
- "Linear": Select this option when a linear scale is available.

**Power supply ([p0404](SINAMICS%20Parameter%20G120.md#p04040n-encoder-configuration-effective-2))**

- Select the appropriate voltage supply for your encoder:

  - 5 V
  - 24 V
  - "Remote sense"; remote sensing ensures that a possible voltage drop along the cable is compensated.

##### Absolute SSI protocol

**Multiturn**

- Select in the drop-down list whether your encoder is multiturn-conform:

**Singleturn resolution ([p0423](SINAMICS%20Parameter%20G120.md#p04230n-absolute-encoder-rotary-singleturn-resolution-1))**

Singleturn encoders divide one rotation (360 degrees mechanical) into a specific number of encoder pulses, e.g. 8192. A unique code word is assigned to each position. After 360° the position values are repeated.

- Enter the singleturn resolution based on your encoder data sheet.

**Multiturn resolution ([p0421](SINAMICS%20Parameter%20G120.md#p04210n-absolute-encoder-rotary-multiturn-resolution-1))**

Multiturn encoders also record the number of revolutions, in addition to the absolute position within one revolution. To do this, further code disks which are coupled via gear steps with the encoder shaft are scanned. When evaluating 12 additional tracks, this means that an additional 4096 revolutions can be coded.

- Enter the multiturn resolution based on your encoder data sheet.

##### SSI protocol structure

The SSI connection between the encoder and the encoder module is established using four wires. This is a serial transmission.

The data transmission with the SSI protocol is performed in just one direction, i.e. the data is transferred from the encoder to the evaluation module. The data is a position value for a rotary or linear measuring system and, possibly, further bits that describe the position value.

The structure of the telegram differs depending on the encoder manufacturer and the measuring system. Consequently, you must use the information provided by the manufacturer that describes the protocol structure in detail. Manufacturers frequently extend the position value and leading and trailing zero bits to produce a telegram length of 13, 21 or 25 bits. Whereby this information is extended to 9 bits for a telegram of 21 bits or to 12 bits for a telegram of 25 bits. In the meantime, however, any telegram length is common. In the following example, 29-bit position data is transferred and extended with 3 bits before and after the position.

| Bits before the position |  |  | Position bits |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | Bits after the position |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| x | x | x | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | p | x | x | x |
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 | 32 | 33 | 34 |
| P indicates the position bits; x indicates the possible position of fault, alarm and parity bits. |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

##### Parameters that can be set for the SSI protocol

**Code ([p0429](SINAMICS%20Parameter%20G120.md#p04290n-encoder-ssi-configuration-1))**

- Here, select which code versions your encoder supports:

  - Gray code; special coding of transfer signals; when transitioning from one position to another, only one bit is always changed.
  - Binary code; binary-coded transfer signals

**Baud rate ([p0427](SINAMICS%20Parameter%20G120.md#p04270n-encoder-ssi-baud-rate-1))**

- Here, enter the baud rate for the SSI encoder.

  When setting the baud rate, also take into account the update rate of the speed or actual position value. All bits must be transferred within the cycle, as otherwise the data transfer is too slow and only performed every xth cycle. If you are using an SSI encoder with incremental track, the incremental track is used for the speed control.

  **Example**: For a baud rate of 100 kHz and an SSI length of 35 bits, 10x35 µs = 350 µs + 30 µs monoflop time = 380 µs are required to transfer the SSI value. If the current controller cycle is faster, you must set a higher baud rate.

  The possible baud rate depends on the cable length (see the diagram).

  ![Parameters that can be set for the SSI protocol](images/103174189067_DV_resource.Stream@PNG-en-US.png)

**Parameterizing the protocol**

For the protocol, define the "Position length", "Bit before position" and "Bit after position" parameters:

1. Enter a value for the "Position length in bits" ([p0447](SINAMICS%20Parameter%20G120.md#p04470n-encoder-ssi-number-of-bits-absolute-value-1)). Refer to the encoder data sheet to identify which value is suitable for your encoder. For a singleturn encoder, for example, 13 bits are used for the position information, and 25 bits for a multiturn encoder (this contains 13 bits of singleturn information).

   Also observe the count direction for the position bit. For the examples shown here, the protocols start with "0" (ascending from left to right). However, there are also manufacturers who have defined a different way of counting, starting from the MSB, counting downward from left to right. Therefore, compare the setting with the data in the encoder data sheet.
2. Enter a value for the "Bits before the position" ([p0446](SINAMICS%20Parameter%20G120.md#p04460n-encoder-ssi-number-of-bits-before-the-absolute-value-1)); see the diagram above.
3. Enter a value for the "Bits after the position" ([p0448](SINAMICS%20Parameter%20G120.md#p04480n-encoder-ssi-number-of-bits-after-the-absolute-value-1)); see the diagram above.

##### Bit functions in the SSI protocol

If alarm bits, error bits or parity bits signal errors when transferring data, in Startdrive, alarms or faults are output in the inspector window.

**Alarm bit ([p0435](SINAMICS%20Parameter%20G120.md#p04350n-encoder-ssi-alarm-bit-1)) – only if the encoder supports it**

If the encoder manufacturer has added alarm bits to the position value, you should certainly evaluate these because they provide the only possibility to output alarms regarding the position value. For example, the encoder may be soiled.

The alarm bit triggers an alarm on the SINAMICS device (A3x412, with x=1,2,3 for encoder 1, 2, 3). You can set the position and state (high or low active).

1. At "Bit activation", activate the alarm bit.
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. At "Logical state", select at which level (high active or low active) the alarm bit should be output. High active means that the corresponding alarm is displayed on the SINAMICS when the bit is set.

**Error bits ([p0434](SINAMICS%20Parameter%20G120.md#p04340n-encoder-ssi-error-bit-1)) – only if the encoder supports it**

If the encoder manufacturer has added error bits to the position value, you must also evaluate them because they allow you to determine the validity of the position value.

Error bits trigger a fault on the SINAMICS device (F3x112, with x=1,2,3 for encoder 1, 2, 3). You can set the position and state (high or low active).

1. At "Bit activation", select the bit number for the error bit. You can parameterize several error bits (see online help for parameters)
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. At "Logical state", select at which level (high active or low active) the error bit should be output. High active means that the corresponding fault is displayed on the SINAMICS when the bit is set.

**Parity bits ([p0436](SINAMICS%20Parameter%20G120.md#p04360n-encoder-ssi-parity-bit-1)) – only if the encoder supports it**

Another possibility to validate the transmission is to transfer a parity bit in the telegram. This is a parity check for all of the bits of the telegram content. The following settings apply for the parity: even (= low level) and odd (= high level). Refer to the data sheet to see whether the encoder uses "even" or "odd" as checking criterion for the parity bit.

Example for "even" parity:

The number of bits filled with 1 in the telegram must always be even. An odd number of set bits is compensated by the parity bit. If an uneven number of set bits is nevertheless determined in the evaluation module, a fault is output on the SINAMICS side (F3x110 Bit 11, with x=1,2,3 for encoder 1, 2, 3).

For "uneven" parity, the inverse logic applies accordingly.

1. At "Bit activation", select the bit number for the parity bit.
2. At "Bit position", enter the position of the bit in the SSI protocol.
3. Under "Logic state", select whether the parity bit has even or odd logic.

**Example telegram**

![SSI encoder example telegram](images/103174138891_DV_resource.Stream@PNG-en-US.png)

SSI encoder example telegram

**Monoflop time ([p0428](SINAMICS%20Parameter%20G120.md#p04280n-encoder-ssi-monoflop-time-1))**

The monoflop time describes the minimum wait time between two transfers of the absolute value for the SSI encoder. The set value must be greater than or equal to the value specified in the data sheet for the encoder.

- Enter the monoflop time.

**Transfer the position value twice (p0429) – only if the encoder supports it**

Some manufacturers allow a position value to be transferred twice; this is called "ring shift" or "fetch doubled". It detects transmission errors, although it extends the time taken to transfer the position value. At least one fill bit is necessary between reading out the first time and second time. You can also refer to the encoder data sheet for the number of fill bits. The following example shows the use of fill bits:

- Select "Double transfer" and enter a value for the fill bits ([p0449](SINAMICS%20Parameter%20G120.md#p04490n-encoder-ssi-number-of-bits-filler-bits-1)).

![SSI encoder position value](images/103174151179_DV_resource.Stream@PNG-en-US.png)

SSI encoder position value

##### Gear ratio / measuring gearbox

Gearboxes or measuring gearboxes are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

#### TTL/HTL incremental encoder

##### Description

These encoders operate analogously to the SIN/COS incremental encoders, although they supply a different output level. They are also referred to as pulse or square-wave encoders. The signals are quadrupled by an edge evaluation.

- HTL (High Voltage Transistor Logic); in unipolar design can be connected to the SMC30.
- RS 422 difference signals (TTL = Transistor Transistor Logic); in bipolar design can be connected to the SMC30.
- The resolution can be improved by a factor of four for TTL and HTL encoders through edge evaluation.
- TTL/HTL encoders are offered in the Startdrive with and without SSI protocol.

> **Note**
>
> **Using the SSI protocol**
>
> You can find information about the SSI protocol at [SSI encoder](#ssi-encoder).

**TTL/HTL encoder mode of operation.**

![TTL pulse encoder](images/103174101515_DV_resource.Stream@PNG-en-US.png)

TTL pulse encoder

After the signal edges of tracks A and B have been evaluated, direction-dependent speed and position information is available.

**Absolute position**

After a machine is switched on, a reference point approach must be carried out to determine the absolute position.

**HTL/TTL encoder type**

The following general parameters can be selected for the HTL/TTL encoder type:

- "Motor encoder": This option is selected for each first added encoder (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- "Rotary": Select this option when a rotary encoder is available.
- "Linear": Select this option when a linear scale is available.

**Power supply ([p0404](SINAMICS%20Parameter%20G120.md#p04040n-encoder-configuration-effective-2))**

- Select the appropriate voltage supply for your encoder:

  - 5 V
  - 24 V (HTL encoder)
  - "Remote sense"; activate this option if you want to use remote sensing to ensure that a possible voltage drop along the cable is compensated.

**Incremental tracks**

The resolution of the encoder is determined by its "number of pulses". This value is located on the encoder type plate and in the associated data sheet.

- "Number of pulses per revolution": Enter the pulse number for the encoder.
- "Level": Select whether you use an HTL (High Threshold Logic) or a TTL (Transistor-Transistor Logic) encoder.
- "Signal": Select whether the encoder transfers a unipolar (ground-based) or a bipolar (differential) signal. Unipolar signals lie in the range von 0 ... 5 V. Bipolar signals lie in the range von -5 ... 5 V.
- "Track monitoring": Activate this option if you want to monitor the incremental track. Note that TTL signals can only be evaluated bipolarly.

**Zero marks (p0404)**

Zero marks serve as reference signal for incremental encoders. Select the appropriate zero signal for your encoder:

- No zero mark
- No zero mark monitoring
- One zero mark per revolution
- Several zero marks per revolution (equidistant zero marks):

  - The number of pulses between the two equidistant zero marks are parameterized at "Zero mark distance".
  - "Number of zero marks": Enter the number of zero marks here. Enter a number ≥ 2.
- Irregular zero marks: Select this option if the zero marks are not equidistant and thus no gap monitoring of the zero marks is possible.
- [Distance-coded zero marks](Configuring%20SINAMICS%20S-G-MV%20drives.md#distance-coded-zero-marks)

##### Gear ratio / measuring gearbox

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

---

**See also**

[SSI encoder](#ssi-encoder)

#### SIN/COS incremental encoders

##### Description

Incremental encoders operate on the principle of optoelectronic scanning of dividing discs with the transmitted-light method. The light source is a light emitting diode (LED). The light-dark modulation generated as the encoder shaft rotates is picked up by photoelectronic elements. With an appropriate arrangement of the line pattern on the dividing disk connected to the shaft and the fixed aperture, the photoelectronic elements provide two trace signals A and B at 90° to one another, as well as a reference signal R. The encoder electronics amplify these signals and convert them to sin/cos 1 Vpp.

**Absolute position**

After a machine is switched on, a reference point approach must be carried out to determine the absolute position.

**SIN/COS encoder operation**

![Sine/cosine incremental encoder](images/103277890955_DV_resource.Stream@PNG-en-US.png)

Sine/cosine incremental encoder

**SIN/COS encoder type**

The following general parameters can be selected for the SIN/COS encoder type:

- "Motor encoder": This option is selected for each first added encoder (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- "Rotary": Select this option when a rotatory encoder is available.
- "Linear": Select this option when a linear scale is available.

**Power supply ([p0404](SINAMICS%20Parameter%20G120.md#p04040n-encoder-configuration-effective-2))**

- Select the appropriate voltage supply for your encoder:

  - 5 V
  - "Remote sense"; remote sensing ensures that a possible voltage drop along the cable is compensated.

**Incremental tracks ([p0408](SINAMICS%20Parameter%20G120.md#p04080n-rotary-encoder-pulse-number-1))**

- Enter the number of pulses per revolution for your encoder. The number of pulses per revolution can also be specified in bits in the encoder data sheets. Encoder pulse number = 2<sup>resolution in bit</sup>.

**Coarse synchronization (p0404)**

- Select how coarse synchronization is to be carried out. You thereby define how the pole position identification is to be carried out.

  - Track C/D; the flux position can be determined using the C/D track and the zero mark, which is adjusted to the magnetic position of the rotor. As the C/D track only has one encoder pulse per mechanical revolution, the accuracy of this determination method is only adequate for starting. Therefore, you must carry out fine synchronization, see also [Enable logic (servo)"](Servo%20drives%20%28highly%20dynamic%29.md#enable-logic-servo).
  - Hall sensor (only for linear motors); Hall sensors are used that measure the magnetic flux. Two sensors are used, which supply information equivalent to a C/D track for each pole pair.
  - None

**Zero marks (p0404)**

Zero marks serve as reference signal for incremental encoders. Select the appropriate zero signal for your encoder:

- No zero mark
- Equidistant zero marks (evaluate several zero marks):

  - The number of pulses between the two equidistant zero marks are parameterized at "Zero mark distance".
- Irregular zero marks: Select this option if the zero marks are not equidistant and thus no gap monitoring of the zero marks is possible.
- [Distance-coded zero marks](Configuring%20SINAMICS%20S-G-MV%20drives.md#distance-coded-zero-marks)

##### Gear ratio / measuring gearbox

Gearbox or measuring gearbox are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

#### Resolver

##### Description

Resolvers are rotary encoders that supply an absolute signal within a pole pitch. Therefore, resolvers do not have to be homed.

In principle, a resolver is made up of two components:

- Two stator windings offset by 90°
- One rotor

With the aid of an excitation voltage (typically 8 kHz), two tracks offset by 90° are generated according to the transformer principle, with an amplitude that depends upon the rotor position. The evaluation of the signals that are still modulated with the excitation frequency is done in the SMx10, which means that the speed, actual position value, rotor position and reference point are available.

![Resolver](images/103277924491_DV_resource.Stream@PNG-en-US.png)

Resolver

> **Note**
>
> When a multi-pole resolver is used, the number of resolver poles matches the number of motor poles.

**Encoder type Resolver**

The following general parameters can be selected for the resolver encoder type:

- "Motor encoder": This option is selected for each first added encoder (measuring system 1). When you add an additional encoder that you want to use as motor encoder, you must activate the option there. The option is then deactivated in the first added encoder.
- "Rotary": This option is preselected for resolvers.

**Enter the number of pole pairs ([p0408](SINAMICS%20Parameter%20G120.md#p04080n-rotary-encoder-pulse-number-1))**

- Enter the number of pole pairs that the associated encoder provides.

##### Gear ratio / measuring gearbox

Gearboxes or measuring gearboxes are relevant only for some motor types, e.g. for 1FW3 torque motors. The gear ratio is the ratio of encoder revolutions ([p0432](SINAMICS%20Parameter%20G120.md#p04320n-gearbox-factor-encoder-revolutions)) to the number of motor or load revolutions ([p0433](SINAMICS%20Parameter%20G120.md#p04330n-gearbox-factor-motorload-revolutions)) and is also designated as transmission ratio.

This information is contained in the motor data sheet.

##### Additional parameters

---

## Parameterizing the drive functions

This section contains information on the following topics:

- [G120 CU250S-2 V shutdown functions](#g120-cu250s-2-v-shutdown-functions)
- [Brake control](#brake-control)
- [Safety Integrated](#safety-integrated)
- [G120 CU250S-2 V flying restart](#g120-cu250s-2-v-flying-restart)
- [G120 CU250S-2 V Vdc controller](#g120-cu250s-2-v-vdc-controller)
- [G120 CU250S-2 V Vdc controller switch-on level](#g120-cu250s-2-v-vdc-controller-switch-on-level)
- [G120 CU250S-2 V automatic restart](#g120-cu250s-2-v-automatic-restart)
- [Messages and monitors](#messages-and-monitors)

### G120 CU250S-2 V shutdown functions

#### Parameterizing the shutdown functions

Parameterize the shutdown functions of the G120 CU250S drive. See also [Shutdown functions OFF1, OFF2 and OFF3](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#shutdown-functions-off1-off2-and-off3).

#### Parameters of the shutdown functions

1. "Pulse enable" ([p0852](SINAMICS%20Parameter%20G120.md#p08520n-bi-enable-operationinhibit-operation-4)); signal source to interconnect the pulse enable.
2. "OFF1" ([p0840](SINAMICS%20Parameter%20G120.md#p08400n-bi-on-off-off1-11)); signal source to interconnect OFF1.
3. "OFF2"

   - "OFF2" ([p0844](SINAMICS%20Parameter%20G120.md#p08440n-bi-no-coast-down-coast-down-off2-signal-source-1-6)); signal source 1 to interconnect OFF2
   - "OFF2" ([p0845](SINAMICS%20Parameter%20G120.md#p08450n-bi-no-coast-down-coast-down-off2-signal-source-2)); signal source 2 to interconnect OFF2
4. "OFF3"

   - "OFF3" ([p0848](SINAMICS%20Parameter%20G120.md#p08480n-bi-no-quick-stop-quick-stop-off3-signal-source-1-5)); signal source 1 to interconnect OFF3
   - "OFF3" ([p0849](SINAMICS%20Parameter%20G120.md#p08490n-bi-no-quick-stop-quick-stop-off3-signal-source-2-2)); signal source 2 to interconnect OFF3
   - Enter a value for the ramp-down time ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)) from maximum speed to standstill at "Ramp-down time for OFF3".

#### Additional parameters

---

### Brake control

This section contains information on the following topics:

- [G120 CU250S-2 V brake control](#g120-cu250s-2-v-brake-control)
- [G120 CU250S-2 V motor holding brake](#g120-cu250s-2-v-motor-holding-brake)
- [G120 CU250S-2 V DC brake](#g120-cu250s-2-v-dc-brake)

#### G120 CU250S-2 V brake control

##### Selection of the brake type

The following brakes are available for the G120 CU250S-2 inverter:

- [Motor holding brake](#g120-cu250s-2-v-motor-holding-brake)
- [DC brake](#g120-cu250s-2-v-dc-brake)
- Compound brake

See also [Braking functions of the converter](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#braking-functions-of-the-converter).

##### Function diagrams (FD)

- Simple brake control - 2701 -
- DC braking (ASM, p0300 = 1) - 7017 -

---

**See also**

[Comparison of the electrical braking methods](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#comparison-of-the-electrical-braking-methods)

#### G120 CU250S-2 V motor holding brake

##### Selection of the motor holding brake

Depending on the selected function, the schematic diagram of the signal characteristic and the display of the parameters change. See also [Motor holding brake](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#motor-holding-brake).

- Select one of the following options ([p1215](SINAMICS%20Parameter%20G120.md#p1215-motor-holding-brake-configuration-2)) from the drop-down list:

  - Motor holding brake as for sequential control system; the motor holding brake is effective as specified by the sequential control system.
  - Motor holding brake permanently open; the motor holding brake has no effect.
  - Motor holding brake as for execution control, connection via BICO; signal is issued via interconnected parameters.

##### Parameters of the motor holding brake

1. Enter the opening time of the holding brake at "Motor holding brake, opening time" ([p1216](SINAMICS%20Parameter%20G120.md#p1216-motor-holding-brake-opening-time)). The setpoint acceptance after controller enable is delayed by this time. With n set = 0 rpm, the speed control has already been activated at controller enable in order to prevent a sagging of the axis.
2. Enter the application time of the holding brake at "Motor holding brake closing time" ([p1217](SINAMICS%20Parameter%20G120.md#p1217-motor-holding-brake-closing-time)). Along with the speed threshold it is a criterion for closing the holding brake. If the closing time has elapsed after removing the controller enable, the "Open holding brake" signal is removed. Alternatively, the brake can already be closed having reached the speed threshold. After the closing delay time has elapsed, the pulse enable will be blocked.
3. "Speed when opening" ([p1475](SINAMICS%20Parameter%20G120.md#p14750n-ci-speed-controller-torque-setting-value-for-motor-holding-brake)); signal source to interconnect the torque when opening the motor holding brake.
4. "Open brake command" ([r0899](SINAMICS%20Parameter%20G120.md#r0899011-cobo-status-word-sequence-control)); signal source to display the "Open brake" command.
5. "Close brake command" (r899); signal source to display the "Close brake" command.

##### "Open brake" dialog box

1. Click "Open brake" to parameterize the opening of the brake. The "Open brake" dialog box opens.
2. "Brake must be opened" ([p0855](SINAMICS%20Parameter%20G120.md#p08550n-bi-unconditionally-release-holding-brake)); signal source to interconnect the "Brake must be opened" signal.

##### "Close brake" dialog box

1. Click "Close brake" to parameterize the closing of the brake. The "Close brake" dialog box opens.
2. Enter the speed threshold for the standstill detection at "Threshold" ([p1226](SINAMICS%20Parameter%20G120.md#p12260n-threshold-for-zero-speed-detection-2)). Along with the closing delay time it is a criterion for closing the holding brake. If the speed threshold has been reached after removing the controller enable, the Release holding brake signal is cancelled. Alternatively, the brake can already be closed due to elapsed closing delay time.
3. Enter the delay time for the pulse suppression at "Delay" ([p1228](SINAMICS%20Parameter%20G120.md#p1228-pulse-cancellation-delay-time-2)).
4. Enter the monitoring time for the standstill detection at "Monitoring time" ([p1227](SINAMICS%20Parameter%20G120.md#p1227-zero-speed-detection-monitoring-time-1)). After reaching the speed threshold the monitoring time is started. After the monitoring time has elapsed, the Release holding brake signal is cancelled.
5. "Brake must be closed" ([p0858](SINAMICS%20Parameter%20G120.md#p08580n-bi-unconditionally-close-holding-brake)); signal source to interconnect "Holding brake must be closed".

##### Status words

Shows the parameters of the brake control status word.

##### Function diagrams (FD)

Simple brake control - 2701 -

##### Additional parameters

---

#### G120 CU250S-2 V DC brake

##### Selection of the DC brake

During the DC braking, the kinetic energy from the motor and the driven machine will be converted to heat in the motor. DC current is fed in which quickly brakes the motor and holds the shaft in its position after the end of the braking duration. See also [DC braking](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#dc-braking).

Depending on the selected function, the schematic diagram of the signal characteristic and the display of the parameters change.

1. Select one of the following options from the drop-down list ([p1231](SINAMICS%20Parameter%20G120.md#p12310n-dc-braking-configuration-1)):

   - DC braking
   - DC braking for OFF1/OFF3; the DC brake is activated for OFF1/OFF3
   - DC braking under start speed
2. Select one of the following options to trigger the DC brake:

   - "DC brake via BICO" to activate the DC brake via a BICO signal
   - "DC brake for fault" to activate the DC brake in the event of a fault

##### Parameters of the DC brake

1. "Enable DC brake" ([p1230](SINAMICS%20Parameter%20G120.md#p12300n-bi-dc-braking-activation)); signal source for activating the DC brake (only for DC brake via BICO). The enable signal can be provided via the digital inputs or USS (PROFIBUS).
2. Enter the start speed for the DC brake (only for DC brake for fault) at "Speed setpoint" ([p1234](SINAMICS%20Parameter%20G120.md#p12340n-speed-at-the-start-of-dc-braking-1)).
3. Enter a value for the motor de-excitation time ([p0347](SINAMICS%20Parameter%20G120.md#p03470n-motor-de-excitation-time)).
4. Enter a value for the braking current (only for DC brake for fault) at "Braking current" ([p1232](SINAMICS%20Parameter%20G120.md#p12320n-dc-braking-braking-current)).
5. Enter a value for the duration of the DC braking ([p1233](SINAMICS%20Parameter%20G120.md#p12330n-dc-braking-time-1)) on (only for DC brake for fault).
6. Enter the demagnetization time at "t_de-excitat." (p347). This is the time until the next pulse enable.
7. Enter the braking current at "I_brake" (p1232). The value is entered in [%] and defines the size of the direct current in [%] relative to the rated motor current ([p0305](SINAMICS%20Parameter%20G120.md#p03050n-rated-motor-current)).

##### Function diagrams (FD)

- DC braking (ASM, p0300 = 1) - 7017 -

##### Additional parameters

---

### Safety Integrated

This section contains information on the following topics:

- [G120 Safety Integrated overview](#g120-safety-integrated-overview)
- [Selecting and activating safety functions](#selecting-and-activating-safety-functions)
- [G120 safe actual value acquisition without encoder](#g120-safe-actual-value-acquisition-without-encoder)
- [Basic functions](#basic-functions)
- [Extended functions](#extended-functions)
- [Test stop](#test-stop)
- [Safety inputs/outputs](#safety-inputsoutputs)

#### G120 Safety Integrated overview

##### Description

Most drives of the G120 family are equipped with the "Safe torque off (STO)" drive-autonomous safety function (exception, e.g. G120P). This function is available in the basic functions.

The extended functions provide additional safety functions such as SS1, SLS, SSM and SDI. See also [Control type / safety functions for extended functions](#control-type-safety-functions-for-extended-functions).

**Activating the safety commissioning**

Before the safety functions are edited, the safety commissioning must be activated and the safety functionality selected:

- [Activating safety functions](#activating-safety-functions)
- [Selecting the safety functionality](#selecting-the-safety-functionality)

**Basic functions**

Detailed information about basic functions can be found at:

- [G120 control type / safety functions for basic functions](#g120-control-type-safety-functions-for-basic-functions).
- [G120 safe torque off, safe brake control and safe stop 1](#g120-safe-torque-off-safe-brake-control-and-safe-stop-1)

**Extended functions**

Detailed information about extended safety functions can be found at:

- [Actual value acquisition](#g120-safe-actual-value-acquisition-without-encoder)
- [G120 safe torque off, safe brake control and safe stop 1](#g120-safe-torque-off-safe-brake-control-and-safe-stop-1-1)
- [G120 safe stop functions (SS1, SBR/SAM)](#g120-safe-stop-functions-ss1-sbrsam)
- [G120 safely-limited speed (SLS)](#g120-safely-limited-speed-sls)
- [G120 safe speed monitoring (SSM)](#g120-safe-speed-monitoring-ssm)
- [G120 safe direction (SDI)](#g120-safe-direction-sdi)
- [G120 acceptance mode](#g120-acceptance-mode)

**Safety inputs/outputs**

Detailed information about the parameterization of the safety inputs/outputs can be found at [Safety inputs/outputs](#safety-inputsoutputs).

**PROFIsafe**

For PROFIsafe, you require a telegram extension that you can set at Cyclic data exchange > Telegram configuration. See also [Editing telegrams](Communication%20and%20telegrams.md#editing-telegrams).

##### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- FD-2840 58)
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

#### Selecting and activating safety functions

This section contains information on the following topics:

- [Activating safety functions](#activating-safety-functions)
- [Selecting the safety functionality](#selecting-the-safety-functionality)
- [Accepting the safety settings](#accepting-the-safety-settings)

##### Activating safety functions

###### Requirement

To edit the safety settings, the drive must be online. The settings are protected by a password. As long as the safety commissioning is not activated, the safety screen forms cannot be edited.

| Icon | Description |
| --- | --- |
| ![Requirement](images/103124173707_DV_resource.Stream@PNG-en-US.png) | Startdrive is not online. You can only edit the safety functions offline. |
| ![Requirement](images/103124177419_DV_resource.Stream@PNG-en-US.png) | Startdrive is online. The safety functions have not been activated yet. |
| ![Requirement](images/103124181131_DV_resource.Stream@PNG-en-US.png) | The safety functions have been activated (safety commissioning is active). |

###### Activating the safety settings and entering the password​

To activate the safety settings, proceed as follows:

1. Click "Go online".
2. Click the "Activate safety commissioning" icon in the title bar of the parameterization editor.

![Activating the safety commissioning](images/117270410635_DV_resource.Stream@PNG-en-US.png)

Activating the safety commissioning

The icon background changes to yellow.

The dialog box for the password input opens.

![Password input](images/103124156939_DV_resource.Stream@PNG-en-US.png)

Password input

1. Enter the password.

   You only have to enter a new password at the first start to replace the "not secure" default password.
2. Click "OK" to accept the settings.

###### Result

The safety commissioning is activated.

##### Selecting the safety functionality

###### Selecting the safety functionality

After activating the safety functionality, select the safety functionality:

1. In the secondary navigation, select "Safety Integrated > Select safety functionality".
2. Select between the following in the drop-down list:

   - No safety function
   - Basic function
   - Extended functions

###### Basic functions

The screen form changes as follows when the basic functions are selected:

![Safety basic functions](images/103124213643_DV_resource.Stream@PNG-en-US.png)

Safety basic functions

1. Click the buttons to execute the corresponding tasks:

   - [Control type / safety functions](#g120-control-type-safety-functions-for-basic-functions) allows the control type (terminal/PROFIsafe) and the safety functions to be parameterized.
   - [Test stop](#test-stop) allows the forced checking procedure (test stop) to be parameterized.
   - F-DI/F-DO/PROFIsafe allows the terminals of PROFIsafe parameters to be set.

###### Extended functions

The screen form changes as follows when the extended functions are selected:

![Safety extended functions](images/103124217611_DV_resource.Stream@PNG-en-US.png)

Safety extended functions

1. Click the buttons to execute the corresponding tasks:

   - "[Actual value acquisition](#g120-safe-actual-value-acquisition-without-encoder)" allows the gear ratio and the actual value acquisition to be parameterized.
   - "[Control type / safety functions](#control-type-safety-functions-for-extended-functions)" allows the control type (terminal/PROFIsafe) and the safety functions to be parameterized.
   - "[Test stop](#test-stop)" allows the forced checking procedure (test stop) to be parameterized.
   - "[F-DI/F-DO/PROFIsafe](#g120-f-dif-doprofisafe)" allows the terminals of PROFIsafe parameters to be set.
   - "[Acceptance](#g120-acceptance-mode)" allows the acceptance mode to be parameterized and activated.

---

**See also**

[G120 safe torque off, safe brake control and safe stop 1](#g120-safe-torque-off-safe-brake-control-and-safe-stop-1)

##### Accepting the safety settings

###### Accepting safety settings

After you have parameterized all safety functions, the drive must accept the settings.

![Deactivating safety functions](images/113597741707_DV_resource.Stream@PNG-en-US.png)

Deactivating safety functions

- ① To accept the settings and deactivate the safety functions, click the icon in the title bar again.

  The following steps are executed:

  - The parameter settings are copied from CPU 1 to CPU 2.
  - Copy RAM to ROM is offered.
  - Safety mode is deactivated, the icon changes to a yellow border.
- ② Go offline with the drive.

You can only continue with the parameterization of the "normal" settings. The dialog boxes are no longer deactivated.

#### G120 safe actual value acquisition without encoder

##### Description

You can parameterize the safe actual value acquisition and the gear ratio for safety without encoder here. For further information, see [Setting the gear ratio and tolerance](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-gear-ratio-and-tolerance) and [Setting encoderless actual value acquisition](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-encoderless-actual-value-acquisition).

##### Actual value synchronization

A cross-comparison is made of the actual positions of CPU 1 and CPU 2 for the actual value synchronization.

- If required, adapt the value at "Actual value tolerance" ([p9542](SINAMICS%20Parameter%20G120.md#p9542-si-motion-act-val-comp-tolerance-cross-ch-processor-1)).

##### Gear ratio

At "Gear ratio", parameterize the mechanical system of the drive. The gear ratio is the ratio of encoder revolutions to revolutions of the drive shaft (load revolutions).

1. At "Actual value tolerance" (p9542), enter the tolerance for the cross-comparison of the actual position between CPU 1 and CPU 2.
2. At "Number of load revolutions" ([p9521](SINAMICS%20Parameter%20G120.md#p952107-si-motion-gearbox-motorload-denominator-processor-1)), enter the number of load revolutions.
3. At "Number of encoder revolutions" ([p9522](SINAMICS%20Parameter%20G120.md#p952207-si-motion-gearbox-motorload-numerator-processor-1)), enter the number of encoder revolutions.
4. The current number of motor pole pairs is displayed at "Motor pole pair number" ([r0313](SINAMICS%20Parameter%20G120.md#r03130n-motor-pole-pair-number-actual-or-calculated)).

##### Parameters of the encoderless actual value acquisition

The following parameters are available for the safe motion monitoring of the extended safety functions:

1. At "Actual value acquisition delay time" ([p9586](SINAMICS%20Parameter%20G120.md#p9586-si-motion-actual-value-sensing-sensorless-delay-time-p1)), enter a value for the evaluation delay for encoderless actual value acquisition after the pulse enable. Also note the online help for this parameter.
2. At "Actual value acquisition filter time" ([p9585](SINAMICS%20Parameter%20G120.md#p9585-si-motion-actual-value-sensing-encoderless-fault-tolerance-cu)), enter a value for the filter time for the actual value smoothing for encoderless actual value acquisition.
3. At "Fault tolerance" (p9585), enter a value for the tolerance of the plausibility monitoring of the current and voltage angle.
4. The current deviation of the velocity monitoring is displayed at "Velocity tolerance" ([r9787](SINAMICS%20Parameter%20G120.md#r9787-si-motion-diagnostics-sensorless-velocity-deviation)).
5. At "Actual value acquisition minimum current" ([p9588](SINAMICS%20Parameter%20G120.md#p9588-si-motion-actual-value-sensing-sensorless-minimum-current-p1)), enter a value for the minimum current for encoderless actual value acquisition with respect to 10 mA (1% = 10 mA).
6. At "Voltage tolerance acceleration" ([p9589](SINAMICS%20Parameter%20G120.md#p9589-si-motion-actual-value-sensing-sensorless-accel-limit-p1)), enter a value for the voltage tolerance to suppress acceleration peaks.

   An increase in this percentage value means that voltage peaks must have a greater amplitude during acceleration operations in order not to influence the actual value acquisition.

##### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

##### Additional parameters

---

#### Basic functions

This section contains information on the following topics:

- [G120 control type / safety functions for basic functions](#g120-control-type-safety-functions-for-basic-functions)
- [G120 safe torque off, safe brake control and safe stop 1](#g120-safe-torque-off-safe-brake-control-and-safe-stop-1)

##### G120 control type / safety functions for basic functions

###### Description

You can configure the control type and the safety functions of the extended functions here.

When the control type is selected, the contents of the safety screen forms are adapted accordingly.

###### Control type

Terminals and PROFIsafe are available as control types:

- Select "Via terminal" if you want to use the safe digital I/Os of a drive.
- Select "Via PROFIsafe" if you want to control the safety functions from a higher-level controller.
- Select "Via terminals (basic) and PROFIsafe (extended)" if you want to control the basic functions via terminals, and the parameters of the extended safety functions via PROFIsafe.

Information on how to assign the F-DIs can be found at [Safety inputs/outputs](#safety-inputsoutputs).

###### Safety functions

You can reach the various safety functions via the buttons in the screen form:

- STO to parameterize Safe Torque Off

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -

##### G120 safe torque off, safe brake control and safe stop 1

###### Description

You can parameterize the STO (Safe Torque Off) function via terminal and PROFIsafe here. If you require the "STO active" checkback signal in your higher-level controller, you must interconnect the signal accordingly.

For a description of the STO function, see also [Safe Torque Off (STO)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#safe-torque-off-sto), [In Startdrive, how are the safe terminals assigned to a safety function?](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#in-startdrive-how-are-the-safe-terminals-assigned-to-a-safety-function) and [Enabling SBC](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#enabling-sbc).

The function is enabled simultaneously with the selection.

**Interconnecting the "STO active" checkback signal**

- "STO active output" ([r9773](SINAMICS%20Parameter%20G120.md#r9773031-cobo-si-status-processor-1-processor-2)); signal source to display the status of STO.

###### STO via PM terminals (PM240-2)

STO via PM terminals can be activated via the drop-down list for the PM240-2. This function is a hardware function of the PM240-2 Power Module. If you want to use this function, you must enable both terminals on the Power Module via DIP switches. Read the documentation of the Power Module or the Drive-integrated Safety Functions - Safety Integrated for G120, G110M and ET200pro-2 Function Manual.

> **Note**
>
> These functions are only supported with PM240-2 frame sizes D and E. They can be identified in **[p9771](SINAMICS%20Parameter%20G120.md#r9771-si-common-functions-processor-1-2).19/[p9871](SINAMICS%20Parameter%20G120.md#r9871-si-common-functions-processor-2-2).19**.

###### Safe brake control (SBC) and Safe stop 1 delay time (G120 CU250S-2 only)

The safe brake control function supplies a safe output signal to control an external brake.

1. To enable the "Safe brake control", select "[1] Enable SBC" in the drop-down list.
2. Enter a value at "Safe stop 1 delay time" ([p9652](SINAMICS%20Parameter%20G120.md#p9652-si-safe-stop-1-delay-time-processor-1)). This is the setting of the pulse suppression delay time for the "Safe stop 1" function

   (SS1) for braking with the OFF3 ramp-down time ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)). The delay time must be greater than the OFF3 ramp-down time.

**Description: The SS1 function without speed monitoring**

![SS1_without monitoring commissioning](images/103124364811_DV_resource.Stream@PNG-en-US.png)

SS1_without monitoring commissioning

When SS1 is selected, the inverter brakes the motor with the OFF3 ramp-down time. Irrespective of the current speed, the inverter switches the motor torque off after the

delay time with the STO function.

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -

###### Additional parameters

---

#### Extended functions

This section contains information on the following topics:

- [Control type / safety functions for extended functions](#control-type-safety-functions-for-extended-functions)
- [G120 safe torque off, safe brake control and safe stop 1](#g120-safe-torque-off-safe-brake-control-and-safe-stop-1-1)
- [G120 safe stop functions (SS1, SBR/SAM)](#g120-safe-stop-functions-ss1-sbrsam)
- [G120 safely-limited speed (SLS)](#g120-safely-limited-speed-sls)
- [G120 safe speed monitoring (SSM)](#g120-safe-speed-monitoring-ssm)
- [G120 safe direction (SDI)](#g120-safe-direction-sdi)
- [G120 acceptance mode](#g120-acceptance-mode)
- [G120 safe acceleration monitor (SAM)](#g120-safe-acceleration-monitor-sam)
- [G120 safe brake ramp (SBR)](#g120-safe-brake-ramp-sbr)

##### Control type / safety functions for extended functions

###### Description

You select the safety functions for the extended functions here.

![Selecting safety functions](images/103278075275_DV_resource.Stream@PNG-en-US.png)

Selecting safety functions

###### Safety functions

You can reach the various safety functions via the buttons in the screen form:

- ① STO to parameterize Safe Torque Off
- ② SS1 to parameterize Safe Stop 1
- ③ SLS to parameterize Safely-Limited S​peed
- ④ SDI to parameterize Safe Direction
- ⑤ SSM to parameterize Safe Speed Monitor

###### Enabling safety functions

To enable the safety functions, select "Enable" in the drop-down lists.

##### G120 safe torque off, safe brake control and safe stop 1

###### Description

You can parameterize the STO (Safe Torque Off) function via terminal and PROFIsafe here. If you require the "STO active" checkback signal in your higher-level controller, you must interconnect the signal accordingly.

For a description of the STO function, see also [Safe Torque Off (STO)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#safe-torque-off-sto), [In Startdrive, how are the safe terminals assigned to a safety function?](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#in-startdrive-how-are-the-safe-terminals-assigned-to-a-safety-function) and [Enabling SBC](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#enabling-sbc).

The function is enabled simultaneously with the selection.

**Interconnecting the "STO active" checkback signal**

- "STO active output" ([r9773](SINAMICS%20Parameter%20G120.md#r9773031-cobo-si-status-processor-1-processor-2)); signal source to display the status of STO.

###### STO via PM terminals (PM240-2)

STO via PM terminals can be activated via the drop-down list for the PM240-2. This function is a hardware function of the PM240-2 Power Module. If you want to use this function, you must enable both terminals on the Power Module via DIP switches. Read the documentation of the Power Module or the Drive-integrated Safety Functions - Safety Integrated for G120, G110M and ET200pro-2 Function Manual.

> **Note**
>
> These functions are only supported with PM240-2 frame sizes D and E. They can be identified in **[p9771](SINAMICS%20Parameter%20G120.md#r9771-si-common-functions-processor-1-2).19/[p9871](SINAMICS%20Parameter%20G120.md#r9871-si-common-functions-processor-2-2).19**.

###### Safe brake control (SBC) and Safe stop 1 delay time (G120 CU250S-2 only)

The safe brake control function supplies a safe output signal to control an external brake.

1. To enable the "Safe brake control", select "[1] Enable SBC" in the drop-down list.
2. Enter a value at "Safe stop 1 delay time" ([p9652](SINAMICS%20Parameter%20G120.md#p9652-si-safe-stop-1-delay-time-processor-1)). This is the setting of the pulse suppression delay time for the "Safe stop 1" function

   (SS1) for braking with the OFF3 ramp-down time ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)). The delay time must be greater than the OFF3 ramp-down time.

**Description: The SS1 function without speed monitoring**

![SS1_without monitoring commissioning](images/103124364811_DV_resource.Stream@PNG-en-US.png)

SS1_without monitoring commissioning

When SS1 is selected, the inverter brakes the motor with the OFF3 ramp-down time. Irrespective of the current speed, the inverter switches the motor torque off after the

delay time with the STO function.

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -

###### Additional parameters

---

##### G120 safe stop functions (SS1, SBR/SAM)

###### Safe Stop 1 (SS1)

The "Safe Stop 1" (SS1) safety function brakes the motor safely with a subsequent transition to "Safe Torque Off" (STO) state. The specified setpoint for the motion control is ignored when SS1 is selected. You can enable and disable SS1 for the configuration of each drive axis of the drive controller. When SS1 is selected, the drive brakes actively on the OFF3 ramp and then changes to the pulse cancellation with possibly activation of SBC. See also [Setting SS1](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-ss1).

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Risk of fatal injury from voltage hazard at the motor**  For active STO, although the motor no longer receives any torque-generating electrical energy, it is not disconnected from the power supply system. Consequently, STO is not a replacement for safe power system disconnection for maintenance work.  Take appropriate precautionary measures for any maintenance work. |  |

###### SS1 with delay time

1. At "Delay time SS1/STOP B -> STO" ([p9556](SINAMICS%20Parameter%20G120.md#p9556-si-motion-pulse-cancellation-delay-time-processor-1)), enter a value for the delay time for the safe pulse suppression after STOP B.
2. At "Shutdown speed SS1" ([p9560](SINAMICS%20Parameter%20G120.md#p9560-si-motion-pulse-cancellation-shutdown-speed-processor-1)), enter a value for the pulse suppression.

   The transition is made to the pulse cancellation state:

   - After a parameterized delay time at the latest.
   - When the actual speed value has reached the configured shutdown speed (p9560, shutdown speed for transition to the pulse cancellation) (requirement: Encoder is available).
3. Enter a value for the "Load-side velocity resolution" ([p9732](SINAMICS%20Parameter%20G120.md#r973201-si-motion-velocity-resolution)).

###### SS1 without delay time with brake ramp - Safe Brake Ramp (SBR)

The Safe Brake Ramp function is also provided for SS1 without delay time. The Safe Brake Ramp (SBR) function provides a safe method for monitoring the brake ramp, see also [G120 safe brake ramp (SBR)](#g120-safe-brake-ramp-sbr).

1. At "Delay time SS1/STOP B -> STO" (p9556), enter a value for the delay time for the safe pulse suppression after STOP B.
2. At "Shutdown speed SS1" (p9560), enter a value for the pulse suppression.

   The transition is made to the pulse cancellation state:

   - After a parameterized delay time at the latest.
   - When the actual speed value has reached the configured shutdown speed (p9560, shutdown speed for transition to the pulse cancellation) (requirement: Encoder is available).
3. Enter a value for the "Load-side velocity resolution" (p9732).

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

###### Additional parameters

---

##### G120 safely-limited speed (SLS)

###### Description

The "Safely-Limited Speed" (SLS) function is used to protect a drive against unintentional high speed. This is achieved by monitoring the current drive speed in conjunction with a speed limit value. See also [Setting SLS](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-sls).

You can parameterize up to four different speed values for each drive axis. Although SLS becomes active only after a delay time, the deselection takes affect immediately. Set the delay time so that it satisfies the safety requirements of the current machine (upper limit) and the higher-level motion controller is capable of braking the drive to the monitored speed.

> **Note**
>
> The dialog box only shows the velocity limits that are possible for the selected control.

###### Safely-limited speed with delay time

1. Select "With delay time" in the drop-down list.
2. At "Delay time for selection of SLS -> SLS active" ([p9551](SINAMICS%20Parameter%20G120.md#p9551-si-motion-sls-changeover-delay-time-processor-1)), enter a value.
3. At "Speed setpoint limit" ([p9533](SINAMICS%20Parameter%20G120.md#p9533-si-motion-sls-setpoint-speed-processor-1)), enter the weighting factor to determine the setpoint limit from the selected speed limit. The active setpoint limit will be displayed.
4. At "Speed limit values 1-4" ([p9531](SINAMICS%20Parameter%20G120.md#p953103-si-motion-sls-limit-values-processor-1)), enter a value for the speed limit values. The values for levels 1 – 4 are freely settable.
5. At "SLS-specific stop responses 1-4" ([p9563](SINAMICS%20Parameter%20G120.md#p956303-si-motion-sls-specific-stop-response-processor-1)), select the required stop response when the speed limit value is exceeded.

###### Safely-limited speed without delay time

1. Select "Without delay time" in the drop-down list. The button to parameterize SBR is displayed, see also [G120 safe brake ramp (SBR)](#g120-safe-brake-ramp-sbr).
2. At "Speed setpoint limit" (p9533), enter the weighting factor to determine the setpoint limit from the selected speed limit. The active setpoint limit will be displayed.
3. At "Speed limit values 1-4" (p9531), enter a value for the speed limit values. The values for levels 1 – 4 are freely settable.
4. At "SLS-specific stop responses 1-4" (p9563), select the required stop response when the speed limit value is exceeded.

###### Supplementary conditions for active SLS

- At drive standstill with missing OFF1 enable (r46.0 = 1), STO becomes active as soon as SLS has been active for five seconds.
- When the OFF1, OFF2 and OFF3 enables are removed, the pulses are suppressed and STO becomes active.
- STO becomes inactive after deselection of SLS or after selection and deselection of STO.

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

###### Additional parameters

---

##### G120 safe speed monitoring (SSM)

###### Description

You can parameterize the "Safe Speed Monitor" here. See also [Setting SSM](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-ssm).

###### Adjustable parameters

1. At "SSM with hysteresis" ([p9501](SINAMICS%20Parameter%20G120.md#p9501-si-motion-enable-safety-functions-processor-1)), select "Enable" in the drop-down list to use the speed hysteresis for Safe Speed Monitor.
2. At "Filter time" ([p9545](SINAMICS%20Parameter%20G120.md#p9545-si-motion-ssm-filter-time-processor-1)), enter a value for the filter time.
3. At "Hysteresis" ([p9547](SINAMICS%20Parameter%20G120.md#p9547-si-motion-ssm-velocity-hysteresis-processor-1)), enter a value for the speed hysteresis. The value is used for the SSM checkback signal to detect standstill.
4. At "Velocity limit" ([p9546](SINAMICS%20Parameter%20G120.md#p9546-si-motion-ssm-speed-limit-processor-1)), enter a value for the limit (SSM, Safe Speed Monitor) in mm/min or rpm.

   The Safe Speed Monitor function supplies a safe checkback signal when the drive speed drops below the speed limit. When exceeding the limit value, no drive-autonomous reaction occurs.
5. At "SSM active during pulse suppression checkback signal" ([p9509](SINAMICS%20Parameter%20G120.md#p9509-si-motion-behavior-during-pulse-cancellation-processor-1)), select whether SSM remains active during a pulse suppression, or becomes inactive.

   **Velocity below SSM limit value**.

   - **Active SSM** checkback signal for pulse suppression **remains active**. When the standstill monitoring threshold is reached, then the torque-generating energy supply to the motor is safely interrupted (STO) by means of safe pulse cancellation. The inverter ensures that the motor speed remains below the SSM monitoring threshold. Therefore, the **Active SSM** signal remains active even when the motor is switched off.
   - **Active SSM** checkback signal for pulse suppression **becomes inactive**. When the standstill monitoring threshold is reached, then the torque-generating energy supply to the motor is not safely interrupted by means of safe pulse cancellation. The motor speed is not safely below the SSM monitoring threshold. Therefore, the inverter sets the **Active SSM** signal to inactive when the motor is switched off.

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

###### Additional parameters

---

##### G120 safe direction (SDI)

###### Description

With SDI (Safe Direction), you check the direction of the drive. Alternatively, either the positive or negative direction is checked. If the drive runs in the unsafe direction, the parameterized STOP response is triggered. See also [Setting SDI](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-sdi).

###### Adjustable parameters

1. At "SDI" ([p9501](SINAMICS%20Parameter%20G120.md#p9501-si-motion-enable-safety-functions-processor-1)), select "Enable" from the drop-down list to monitor the safe direction.
2. At "Delay time for selection of SDI -> SDI active" ([p9565](SINAMICS%20Parameter%20G120.md#p9565-si-motion-sdi-delay-time-processor-1)), enter a delay time for the safe direction. Between the selection of SDI and the activation of SDI, the direction can be reversed by an external controller during the delay time. After the delay time has expired, monitoring of the Safe Direction is started.
3. At "Tolerance" ([p9564](SINAMICS%20Parameter%20G120.md#p9564-si-motion-sdi-tolerance-processor-1)), enter a value for the position tolerance. If the drive turns in the unsafe direction within the tolerance, the parameterized STOP response is triggered.
4. Select the response that is to be triggered in the "Stop response" ([p9566](SINAMICS%20Parameter%20G120.md#p9566-si-motion-sdi-stop-response-processor-1)) drop-down list.
5. At "SDI active during pulse suppression checkback signal" ([p9509](SINAMICS%20Parameter%20G120.md#p9509-si-motion-behavior-during-pulse-cancellation-processor-1)), select whether SDI remains active during a pulse suppression, or becomes inactive.
6. "Positive setpoint limit" ([r9733](SINAMICS%20Parameter%20G120.md#r973302-co-si-motion-setpoint-speed-limit-effective)).[0]; signal source for the positive setpoint limit.
7. "Negative setpoint limit" (r9733).[1]; signal source for the negative setpoint limit.

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

###### Additional parameters

---

##### G120 acceptance mode

###### Description

You can activate acceptance mode here. Whenever a change is made to the safety parameters, the functions affected must undergo a new acceptance test; to run this test, you must activate acceptance mode.

The acceptance test procedure is described in the SINAMICS G120 Safety Functions Function Manual. Further information can be found at [Acceptance test](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#acceptance-test).

> **Note**
>
> **Acceptance test only after completed commissioning**
>
> The acceptance test must only be carried out after the safety functions have been commissioned and a POWER ON reset.
>
> You must document the test in writing.

###### Acceptance mode

1. Click the button to activate acceptance mode.
2. At "Acceptance test mode time limit ([p9558](SINAMICS%20Parameter%20G120.md#p9558-si-motion-acceptance-test-mode-time-limit-processor-1)), enter a maximum time for the acceptance test (preliminary setting is 40 seconds). The test is stopped automatically when the time limit is exceeded.

**Diagnostics**

The LEDs on the right-hand margin indicate the current status of the test.

###### Additional parameters

---

##### G120 safe acceleration monitor (SAM)

###### Safe Acceleration Monitor (SAM)

The "Safe Acceleration Monitor" (SAM) function is used for safe monitoring of the acceleration. It is not a separate safety function, but part of the SS1 safety function. A STOP A is generated if any drive acceleration within the ramp-down phase exceeds the tolerance defined in [p9348](SINAMICS%20Parameter%20G120.md#p9348-si-motion-sam-actual-velocity-tolerance-processor-2)/[p9548](SINAMICS%20Parameter%20G120.md#p9548-si-motion-sam-actual-velocity-tolerance-processor-1).

###### Adjustable parameters

1. At "Velocity tolerance" (p9548), enter a value for the actual velocity tolerance.
2. At "Shutdown speed acceleration monitoring" ([p9568](SINAMICS%20Parameter%20G120.md#p9568-si-motion-sam-velocity-limit-processor-1)), enter a value for the velocity limit of SAM.
3. Enter a value for the ramp-down time from maximum speed to standstill for the OFF3 command at "Ramp-down time for OFF3" ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)).
4. At "Maximum speed" ([p1082](SINAMICS%20Parameter%20G120.md#p10820n-maximum-speed-3)), enter a value for the greatest possible speed.

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

###### Additional parameters

---

##### G120 safe brake ramp (SBR)

###### Safe Brake Ramp

The "Safe Brake Ramp" (SBR) function provides a safe method for monitoring the brake ramp.

After SS1 or SLS is triggered (when using the speed setpoint limitation), the motor is braked immediately along the OFF3 ramp. After the delay time expires [p9582](SINAMICS%20Parameter%20G120.md#p9582-si-motion-brake-ramp-delay-time-processor-1)/[p9382](SINAMICS%20Parameter%20G120.md#p9382-si-motion-brake-ramp-delay-time-processor-2), monitoring of the braking ramp will be started. The motor is monitored to ensure that it does not exceed the set brake ramp (SBR) during braking.

###### Adjustable parameters

1. At "Delay time" (p9582), enter a delay time for the braking ramp. After the delay time, monitoring of the braking ramp will be started.
2. At "Monitoring time" ([p9583](SINAMICS%20Parameter%20G120.md#p9583-si-motion-brake-ramp-monitoring-time-processor-1)), enter a value for the monitoring time to determine the braking ramp.
3. At "Reference velocity" ([p9581](SINAMICS%20Parameter%20G120.md#p9581-si-motion-brake-ramp-reference-value-processor-1)), enter a value for the reference value to determine the braking ramp.
4. Enter a value for the ramp-down time from maximum speed to standstill for the OFF3 command at "Ramp-down time for OFF3" ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)).
5. At "Maximum speed" ([p1082](SINAMICS%20Parameter%20G120.md#p10820n-maximum-speed-3)), enter a value for the greatest possible speed.

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

###### Additional parameters

---

#### Test stop

##### Description

Parameterize the settings for the forced checking procedure (test stop) here.

To meet the requirements of the DIN EN ISO 13849‑1 and IEC 61508 standards in terms of timely fault detection, the inverter must test its safety-related circuits regularly - at least once a year - for correct functioning. The inverter monitors the regular test of its safety-related circuits that monitor the speed of the motor, and to safely interrupt the torque-generating energy supply to the motor through the safe pulse suppression.

##### Basic functions

For a detailed description, see also [Setting the forced checking procedure (test stop)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-forced-checking-procedure-test-stop).

1. At "Forced checking procedure of the shutdown paths" ([p9659](SINAMICS%20Parameter%20G120.md#p9659-si-forced-checking-procedure-timer)), enter the interval for performing the forced checking procedure and testing of the safety shutdown paths.

   Within the parameterized time, the safe standstill (SH) must be deselected at least once. The monitoring time is reset at every SH deselection.
2. "Test of the shutdown paths required" ([r9773](SINAMICS%20Parameter%20G120.md#r9773031-cobo-si-status-processor-1-processor-2)); displays the safety status on the drive. Evaluate alarm A01699 in your higher-level controller, for example, by interconnecting r9773.31 to a digital output or a bit in the fieldbus status word.

##### Extended functions

For a detailed description, see also [Setting the forced checking procedure (test stop)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-forced-checking-procedure-test-stop-1).

1. At "Forced checking procedure of the shutdown paths" (p9659), enter the interval for performing the forced checking procedure and testing of the safety shutdown paths.

   Within the parameterized time, the safe standstill (SH) must be deselected at least once. The monitoring time is reset at every SH deselection.
2. "Test of the shutdown paths required" (r9773); displays the safety status on the drive. Evaluate alarm A01699 in your higher-level controller, for example, by interconnecting r9773.31 to a digital output or a bit in the fieldbus status word.
3. In "Test stop selection" ([p9705](SINAMICS%20Parameter%20G120.md#p9705-bi-si-motion-test-stop-signal-source-1)), select the signal source for the test stop of the safe motion monitoring.
4. Enter the maximum value at "Forced checking procedure of the shutdown paths" ([p9559](SINAMICS%20Parameter%20G120.md#p9559-si-motion-forced-checking-procedure-timer-processor-1)).
5. "Forced checking procedure required" ([r9723](SINAMICS%20Parameter%20G120.md#r9723016-cobo-si-motion-diagnostic-signals-integrated-in-the-drive)) shows that a forced checking procedure is required.

##### STO via PM terminals with PM240-2

For a detailed description, see also [Setting the forced checking procedure (test stop)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-forced-checking-procedure-test-stop).

1. At "Forced checking procedure of the PM terminals" ([p9661](SINAMICS%20Parameter%20G120.md#p9661-si-forced-checking-procedure-sto-via-pm-terminals-time)), enter the interval for performing the forced checking procedure and testing of the safety shutdown paths.

   Within the parameterized time, the HW STO must be deselected at least once. The monitoring time is reset at every STO deselection.
2. "Test of the PM terminals required" (r9773); using this signal, the inverter signals that a forced checking procedure (test stop) for the Power Module terminals is required.

##### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -

##### Additional parameters

---

#### Safety inputs/outputs

This section contains information on the following topics:

- [G120 F-DI/F-DO/PROFIsafe](#g120-f-dif-doprofisafe)
- [G120 F-DI assignment](#g120-f-di-assignment)
- [G120 configuration of the safe state](#g120-configuration-of-the-safe-state)

##### G120 F-DI/F-DO/PROFIsafe

###### Description

Parameterize the settings of the SINAMICS G120 for the fail-safe inputs and outputs here.

Different parameters are displayed in the screen form, depending on the control type.

###### G120 CU250S-2 inputs

For further information, see also [G120 CU250S-2 V digital inputs](#g120-cu250s-2-v-digital-inputs).

###### PM terminal configuration

Here you parameterize the discrepancy time for the switchover of the fail-safe digital input for STO to processor 1.

Because of the different runtimes of the two monitoring channels, an F-DI switchover is not effective at the same time.

After an F-DI switchover, a comparison of the dynamic data is not performed during the discrepancy time which can be set here.

###### F-DI configuration

The signal states on the two terminals of an F-DI are then monitored whether they attain the same logical signal state within the discrepancy time.

For internal errors or limit value violations, the drive-internal safety function enters a safety alarm in a special alarm buffer.

1. At "F-DI discrepancy time" ([p9650](SINAMICS%20Parameter%20G120.md#p9650-si-f-di-changeover-discrepancy-time-processor-1)), enter a discrepancy time [ms].
2. At "F-DI input filter" ([p9651](SINAMICS%20Parameter%20G120.md#p9651-si-sto-debounce-time-processor-1)), enter a time [ms] for the input filter (debounce time) for the F-DIs and the readback input for the forced checking procedure.
3. Select the fail-safe digital input for the "Acknowledgement internal event" signal in the "F-DI selection" ([p10006](SINAMICS%20Parameter%20G120.md#p10006-si-motion-acknowledgment-internal-event-f-di-processor-1)).

###### F-DO configuration (only for devices with F-DO)

F-DO forced checking procedure:

The forced checking procedure of the fail-safe output is the regular self-test of the inverter, in which the inverter checks whether the output can be shut down (deactivated).

- "Forced checking procedure signal source" ([p10007](SINAMICS%20Parameter%20G120.md#p10007-bi-si-motion-forced-checking-procedure-f-do-signal-source)); signal source selection for the start of the forced checking procedure.
- Enter a value at "Test cycle force checking procedure F-DO" ([p10003](SINAMICS%20Parameter%20G120.md#p10003-si-motion-forced-checking-procedure-timer-1)).

A six-way AND logic operation is connected downstream of the output terminal pair of the F-DO; the signal sources for the inputs of the AND can be selected via parameter [p10042](SINAMICS%20Parameter%20G120.md#p1004205-si-motion-f-do-signal-sources-processor-1):

- No function
- STO active
- SS1 active
- SLS active
- SSM checkback signal active
- Safe state
- Internal event
- SDI positive active
- SDI negative active

Parameters for the F-DO test

1. Select the "Test" option ([p10046](SINAMICS%20Parameter%20G120.md#p10046-si-motion-f-do-feedback-signal-input-activation)) if the assigned DI channel is to be evaluated in the case of force checking procedure (test stop).
2. In the drop-down list, select the test stop mode ([p10047](SINAMICS%20Parameter%20G120.md#p10047-si-motion-f-do-test-stop-mode-processor-1-1)).
3. At "Delay time for test stop" ([p10001](SINAMICS%20Parameter%20G120.md#p10001-si-motion-delay-time-for-test-stop-at-do-processor-1)), enter a delay time [ms]. The test time specifies the maximum waiting time for the transient condition of an external actuator.

###### PROFIsafe configuration

Only the PROFIsafe address is required for control of the safety functions via PROFIsafe, see also [PROFIsafe properties and configuration](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#profisafe-properties-and-configuration).

1. To enter the PROFIsafe address, switch to the inspector window and click the "General" tab at "Properties".
2. Click the "Telegram configuration" button.
3. Select "Cyclic data exchange" in the navigation.
4. In the telegram configuration, click "Add telegram" and add a telegram.

   The telegram is added and two further dialog boxes for the safety setpoints and actual values are displayed.
5. Switch to the Safety setpoints and copy the value at the drive "Safety address".
6. Insert the safety address here.

> **Note**
>
> **Unique PROFIsafe addresses**
>
> Ensure that the PROFIsafe addresses are unique. Check your settings carefully, see also [Checking the PROFIsafe address](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#checking-the-profisafe-address).

###### F-DI 0 ... F-DI 2 routing configuration

The safe status of the F-DIs selected is transferred via PROFIsafe to an F-controller. You can set the transfer for each F-DI.

1. Click the buttons for F-DI 0 ... F-DI 2 ([p10050](SINAMICS%20Parameter%20G120.md#p10050-si-motion-profisafe-f-di-transfer-processor-1)) to enable the transmission (solid line) or to interrupt the transmission (no connection).
2. Under "F-DI discrepancy time" ([p10002](SINAMICS%20Parameter%20G120.md#p10002-si-motion-f-di-changeover-discrepancy-time-processor-1)), enter a value for the discrepancy time of the fail-safe digital inputs.
3. Under "F-DI input filter" ([p10017](SINAMICS%20Parameter%20G120.md#p10017-si-motion-digital-inputs-debounce-time-processor-1)), enter a value for the debounce time for the digital inputs.

###### Dialog boxes that can be called

Call [G120 configuration of the safe state](#g120-configuration-of-the-safe-state) for the parameterization of the safe state.

###### G120 CU250S-2 function diagrams (FD)

- SS1 (Safe Stop 1), STO (Safe Torque Off) (Part 1) - 2810 -
- F-DI (Fail-safe Digital Input) - 2813 -
- SBC (Safe Brake Control) - 2814 -
- SS1 (Safe Stop 1), internal STOP A, B, F - 2819 -
- SLS (Safely-Limited Speed) - 2820 -
- SSM (Safe Speed Monitor) - 2823 -
- SDI (Safe Direction) - 2824 -
- Control and status word - 2840 -
- Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
- Fail-safe digital output (F-DO 0) - 2853 -
- Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -
- Safe State selection - 2856 -
- F-DO assignment - 2857 -
- Extended Functions via PROFIsafe (p9601.2 = 1 and p9601.3 = 1) - 2858 -

###### Additional parameters

---

##### G120 F-DI assignment

###### Description

Parameterize the safety functions of the drive here and specify the function of the fail-safe digital inputs F-DI.

###### F-DI selection

1. Select the setting for the fail-safe digital input ([p10022](SINAMICS%20Parameter%20G120.md#p10022-si-motion-sto-input-terminal-processor-1)) that you want to use for "STO" from the drop-down list.
2. Select the setting for the fail-safe digital input ([p10023](SINAMICS%20Parameter%20G120.md#p10023-si-motion-ss1-input-terminal-processor-1)) that you want to use for "SS1" from the drop-down list.
3. Select the setting for the fail-safe digital input ([p10026](SINAMICS%20Parameter%20G120.md#p10026-si-motion-sls-input-terminal-processor-1)) that you want to use for "SLS" from the drop-down list.
4. Select the setting for the fail-safe digital input ([p10030](SINAMICS%20Parameter%20G120.md#p10030-si-motion-sdi-positive-input-terminal-processor-1)) that you want to use for "SDI negative" from the drop-down list.
5. Select the setting for the fail-safe digital input ([p10031](SINAMICS%20Parameter%20G120.md#p10031-si-motion-sdi-negative-input-terminal-processor-1)) that you want to use for "SDI positive" from the drop-down list.

###### Selection options

Select one of the following settings from the drop-down list:

- [0] Static active; select this option if you want the function to always be activated without assigning a F-DI.
- F-DI 1
- F-DI 2
- F-DI 3
- [255] Static inactive; select this option if you want the function to always be deactivated without assigning a F-DI.

###### G120 CU250S-2 function diagrams (FD)

Extended Functions via F-DI (p9601.2 = 1 and p9601.3 = 0) - 2855 -

###### Additional parameters

---

##### G120 configuration of the safe state

###### Description

You can parameterize the safety functionality of the drive here.

**Signal source for safe_state**

The status signals of the drive-internal dbMM monitoring function can be selected for the drive.

The signals are high-active and combined with OR. The number of signal sources depends on the selection for the special operation transition.

**Safe state output signal**

The safe state of the drive can be achieved through various states of the safety functions. Several status signals can therefore be combined by an OR operation in the Safe state output signal. The result is generated in both monitoring channels and provided separately for the output on the individual digital outputs X131/5 and X131/6 of the F-DO.

###### G120 CU250S-2 function diagrams (FD)

Safe State selection - 2856 -

### G120 CU250S-2 V flying restart

#### Description

The "Flying restart" (enabled with the [p1200](SINAMICS%20Parameter%20G120.md#p12000n-flying-restart-operating-mode-2) operating mode) provides the capability of switching an inverter on a motor that is still turning. Switching on the inverter without the flying restart function would not allow any flux to build up in the motor while it is turning. Since the motor cannot generate any torque without flux, this can cause it to switch off due to overcurrent (F07801). See also [Flying restart – switching on while the motor is running](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#flying-restart-switching-on-while-the-motor-is-running).

The flying restart function first determines the speed of the drive with which V/f control or vector control is initialized so that the inverter frequency and the motor frequency can be synchronized.

During the standard start-up procedure for the inverter, the motor must be at a standstill. The inverter then accelerates the motor from standstill to the setpoint speed. In many cases, however, this prerequisite is not met. Two different situations are possible in this case:

- The drive rotates as a result of external influences such as water (pump drives) or air (fan drives). In this case, the drive can also rotate against the direction of rotation.
- The drive rotates as a result of a previous shutdown (e.g. OFF 2 or power failure). The drive slowly coasts to a standstill as a result of the kinetic energy stored in the drive train (Example: induced-draft fan with a high moment of inertia and a steeply descending load characteristic in the lower speed range).

#### Setting the operating mode

Flying restart is activated depending on the selected operating mode (p1200):

- 0: Flying restart is inactive
- 1: Flying restart is always active. Start in the setpoint direction
- 4: Flying restart is always active. Start only in the setpoint direction

  > **Note**
  >
  > Before flying restart is activated, the demagnetization time is elapsed, enabling the voltage at the motor terminals to be decreased. Otherwise, when the pulses are enabled, high equalizing currents can occur due to a phase short-circuit.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Risk of fatal injury from the acceleration of the motor due to detection current**  If the "Flying restart" (p1200) function is active, the drive may still be accelerated by the detection current! For this reason, entering the area around the motors in this condition can cause death, serious injury, or considerable material damage.  Take proper precautions before entering the work area. |  |

#### Additional parameters

---

### G120 CU250S-2 V Vdc controller

#### Description

The Vdc control can be activated using the appropriate measures if an overvoltage or undervoltage is present in the DC link. See also [Limiting the maximum DC-link voltage](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#limiting-the-maximum-dc-link-voltage).

#### Overvoltage in the DC link

Typical cause:

The drive is operating in regenerative mode and is supplying too much energy to the DC link.

Remedy:

Reduce the regenerative torque to maintain the DC-link voltage within permissible limits. With the Vdc controller activated, the inverter may automatically extend the ramp-down time of a drive if the shutdown supplies too much energy to the DC link.

#### Undervoltage in the DC link

Typical cause:

Failure of the supply voltage or infeed for the DC link.

Remedy:

Specify a regenerative torque for the rotating drive to compensate the existing losses, thereby stabilizing the voltage in the DC link (kinetic buffering).

#### Configuration ([p1240](SINAMICS%20Parameter%20G120.md#p12400n-vdc-controller-configuration-vector-control-6))

- Select the configuration for the DC-link voltage controller (Vdc controller) in the control mode. Depending on the selected configuration, the schematic diagram of the signal characteristic and the display of the parameters change.

  > **Note**
  >
  > **Enable Vdc-max controller, Enable Vdc-max controller and Vdc-min controller**:
  >
  > The following applies when the specified DC-link voltage limit is reached:
  >
  > The Vdc-max controller limits the power fed back in order to keep the DC-link voltage below the maximum DC-link voltage during braking.
  >
  > The ramp-down times are increased automatically.
  >
  > **Enable Vdc-min controller, Enable Vdc-max controller and Vdc-min controller**:
  >
  > When the switch-on level of the Vdc-min controller has been reached, the following applies:
  >
  > The Vdc-min controller limits the power drawn from the DC link in order to keep the DC-link voltage above the minimum DC-link voltage during acceleration.
  >
  > The motor is braked in order to utilize its kinetic energy for buffering the DC link.

#### Vdc_min controller response ([p1256](SINAMICS%20Parameter%20G120.md#p12560n-vdc_min-controller-response-kinetic-buffering))

- Select the response for the Vdc_min controller (kinetic buffering). The following are possible:

  - "Support Vdc until undervoltage, n<[p1257](SINAMICS%20Parameter%20G120.md#p12570n-vdc_min-controller-speed-threshold)->F07405"
  - "Support Vdc at undervoltage, n<p1257-> F07405, t>[p1255](SINAMICS%20Parameter%20G120.md#p12550n-vdc_min-controller-time-threshold)->F07406"

#### Dynamic factor ([p1243](SINAMICS%20Parameter%20G120.md#p12430n-vdc_max-controller-dynamic-factor)) (Vdc_max controller)

The "dynamic factor" for the DC-link voltage controller (Vdc_max controller) is displayed here.

100% means that gain, integral time and derivative time are used in accordance with their basic settings based on a theoretical controller optimization.

The dynamic factor can be used if subsequent optimization is required. Gain, integral time and derivative time are rated with a dynamic factor.

If more than one module is connected in the DC link, the dynamic factor must be increased in accordance with the additional capacities / module capacity ratio for the relevant module.

#### Dynamic factor ([p1247](SINAMICS%20Parameter%20G120.md#p12470n-vdc_min-controller-dynamic-factor-kinetic-buffering)) (Vdc_min controller)

The "dynamic factor" for the Vdc_min controller (kinetic buffering) is displayed here.

100% means that gain, integral time and derivative time are used in accordance with their basic settings based on a theoretical controller optimization.

The dynamic factor can be used if subsequent optimization is required. Gain, integral time and derivative time are rated with a dynamic factor.

If more than one module is connected in the DC link, the dynamic factor must be increased in accordance with the additional capacities / module capacity ratio for the relevant module.

#### Function diagrams (FD)

- Vdc_max controller and Vdc_min controller (PM240) - 6220 -
- U/f control, Vdc_max controller and Vdc_min controller (PM240) - 6320 -

#### Additional parameters

---

### G120 CU250S-2 V Vdc controller switch-on level

#### Parameterizing the switch-on level

Parameterize the switch-on level of the Vdc controller. When the value falls below this level the Vdc_min controller is activated, when the level is exceeded, the Vdc_max controller is activated.

#### Parameters of the Vdc_min switch-on level

1. Enter a value in [%] for the "Switch-on level" ([p1245](SINAMICS%20Parameter%20G120.md#p12450n-vdc_min-controller-switch-in-level-kinetic-buffering-4)) for the Vdc_min controller (kinetic buffering).
2. Enter a value in [%] for the "Speed threshold" ([p1257](SINAMICS%20Parameter%20G120.md#p12570n-vdc_min-controller-speed-threshold)). If the speed falls below this threshold, a fault is signaled.
3. Enter a value in [%] for the "Vdc controller dynamic factor" ([p1247](SINAMICS%20Parameter%20G120.md#p12470n-vdc_min-controller-dynamic-factor-kinetic-buffering)).

   - 100% means that gain, integral time and derivative time are used in accordance with their basic settings based on a theoretical controller optimization.
   - The dynamic factor can be used if subsequent optimization is required. Gain, integral time and derivative time are rated with a dynamic factor.
4. Enter a value in [s] for "Fault F7406 if T power failure >" ([p1255](SINAMICS%20Parameter%20G120.md#p12550n-vdc_min-controller-time-threshold)). If this is exceeded, a fault is signaled.

#### Parameters of the Vdc_max switch-on level

1. Enter a value in [%] for "Vdc_max controller dynamic factor" ([p1243](SINAMICS%20Parameter%20G120.md#p12430n-vdc_max-controller-dynamic-factor)).

   - 100% means that gain, integral time and derivative time are used in accordance with their basic settings based on a theoretical controller optimization.
   - The dynamic factor can be used if subsequent optimization is required. Gain, integral time and derivative time are rated with a dynamic factor.
   - If more than one module is connected in the DC link, the dynamic factor must be increased in accordance with the additional capacities / module capacity ratio for the relevant module.

#### Function diagrams (FD)

- Vdc_max controller and Vdc_min controller (PM240) - 6220 -
- U/f control, Vdc_max controller and Vdc_min controller (PM240) - 6320 -

#### Additional parameters

---

### G120 CU250S-2 V automatic restart

#### Description

The automatic restart function automatically restarts the drive after an undervoltage or a power failure. See also [Automatic switch-on](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#automatic-switch-on).

The alarms present are acknowledged and the drive is restarted automatically. The drive can be restarted in two ways:

- The standard procedure starting from standstill, or
- The flying restart function. For drives with small inertia loads and load torques where the drive can be brought to a standstill within seconds (such as pump drives with water gauges), the start from standstill is recommended.

  | Symbol | Meaning |
  | --- | --- |
  |  | **Warning** |
  | **Risk of fatal injury from restarting the motor**  When the "automatic restart" function is active ([p1210](SINAMICS%20Parameter%20G120.md#p1210-automatic-restart-mode-3) > 1), the motor automatically starts after a power failure. This is especially critical after longer power failures.   Reduce the risk of accidents in your machine or system to an acceptable level by applying suitable measures, e.g. protective doors or covers. |  |

#### Settings

To prevent the motor from switching to phase opposition when the drive is being restarted, there is a delay while the motor demagnetizes (t = 2.3 x motor magnetization time constant). Once this time has elapsed, the inverter is enabled and the motor is supplied with power.

1. In the "Function selection" (p1210) drop-down list, select the restart method that you want to use:

   - p1210[0]; inhibit automatic restart
   - p1210[1]; acknowledge all faults without restarting
   - p1210[4]; restart after line supply failure without additional start attempts
   - p1210[6]; restart after fault with additional start attempts
   - p1210[14]; restart after fault following manual acknowledgement
   - p1210[16]; restart after fault following manual acknowledgement
   - p1210[26]; acknowledge all faults and reclose in the event of an ON command
2. At "Automatic restart monitoring time" ([p1213](SINAMICS%20Parameter%20G120.md#p121301-automatic-restart-monitoring-time)), enter a time (not with [0] and [1]).
3. At "Delay time start attempts" ([p1212](SINAMICS%20Parameter%20G120.md#p1212-automatic-restart-delay-time-start-attempts)), enter a time (not with [0] and [1]).
4. At "Number of start attempts" ([p1211](SINAMICS%20Parameter%20G120.md#p1211-automatic-restart-start-attempts)), enter the number (not with [0] and [1]).
5. At "Monitoring time for resetting the fault counter" (p1213), enter a time (not with [0] and [1]).

#### Additional parameters

---

### Messages and monitors

This section contains information on the following topics:

- [G120 CU250S-2 V motor temperature](#g120-cu250s-2-v-motor-temperature)
- [G120 CU250S-2 V load torque monitoring](#g120-cu250s-2-v-load-torque-monitoring)
- [Speed messages](#speed-messages)

#### G120 CU250S-2 V motor temperature

##### Monitoring the motor temperature

Parameterize the motor temperature monitoring. See also [Motor temperature monitoring using a temperature sensor IP20](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#motor-temperature-monitoring-using-a-temperature-sensor-ip20).

##### Response with overtemperature

Select one of the following as "Response to overtemperature" ([p0610](SINAMICS%20Parameter%20G120.md#p06100n-motor-overtemperature-response)):

- No response, only alarm
- Alarm with reduction of I_max and fault
- Alarm and fault, no reduction of I_max

##### Temperature sensor

Select the "Temperature sensor" ([p0601](SINAMICS%20Parameter%20G120.md#p06010n-motor-temperature-sensor-type)) from the following options:

- No sensor
- PTC thermistor
- KTY84
- Bimetallic NC contact
- Pt1000

##### Parameters of the motor temperature

1. Enter a value for the "Ambient temperature" ([p0625](SINAMICS%20Parameter%20G120.md#p06250n-motor-ambient-temperature-during-commissioning)). This is the temperature at the time of motor identification.
2. Enter a value ([p0604](SINAMICS%20Parameter%20G120.md#p06040n-mot_temp_mod-2sensor-alarm-threshold-1)) for the motor temperature alarm threshold. When this value is exceeded, an alarm is issued.
3. Enter a value ([p0605](SINAMICS%20Parameter%20G120.md#p06050n-mot_temp_mod-12sensor-threshold-and-temperature-value)) for the motor temperature fault threshold. When this value is exceeded, a fault is issued.

##### Function diagrams (FD)

- Thermal monitoring, motor, motor temperature status word, faults/alarms - 8016 -

##### Additional parameters

---

#### G120 CU250S-2 V load torque monitoring

##### Parameterizing the load torque monitoring

This function enables the monitoring of the power transmission between the motor and the driven machine. Typical applications are, for example, V belts, flat belts or chains that grip belt pulleys or sprocket wheels of drive and output shafts, and thereby transmit peripheral speeds and forces. The load monitoring can identify blockages in the working machine and interruptions to the power transmission.

During load monitoring, the current speed/torque curve is compared with the programmed speed/torque curve. If the current value is outside of the programmed tolerance band, then a fault or alarm is triggered depending on the "Load torque monitoring response" parameter. See also [Load torque monitoring (system protection)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#load-torque-monitoring-system-protection).

##### Load monitoring configuration ([p2193](SINAMICS%20Parameter%20G120.md#p21930n-load-monitoring-configuration-1))

To configure the load monitoring, select one of the following options:

- Monitoring switched off
- Torque and load failure monitoring
- Speed and load failure monitoring
- Load failure monitoring

##### Load torque monitoring response ([p2181](SINAMICS%20Parameter%20G120.md#p21810n-load-monitoring-response-1))

To parameterize the response of the load torque monitoring, select one of the following options in the drop-down list:

- "Load monitoring disabled"
- "A07920 for torque/speed too low"

  There is a negative difference of the torque to the torque/speed envelope curve (too low).  
  No response.
- "A07921 for torque/speed too high"

  There is a positive difference of the torque to the torque/speed envelope curve (too high).  
  No response.
- "A07922 for torque/speed out of tolerance"

  There is a difference of the torque to the torque/speed envelope curve.  
  No response.
- "F07923 for torque/speed too low"

  There is a negative difference of the torque to the torque/speed envelope curve (too low).  
  OFF1 (OFF2, OFF3, NONE) as response.
- "F07924 for torque/speed too high"

  There is a positive difference of the torque to the torque/speed envelope curve (too high).  
  OFF1 (OFF2, OFF3, NONE) as response.
- "F07925 for torque/speed out of tolerance"

  There is a difference of the torque to the torque/speed envelope curve.  
  OFF1 (OFF2, OFF3, NONE) as response.

##### Load torque monitoring in first quadrant ([p2149](SINAMICS%20Parameter%20G120.md#p21490n-monitoring-configuration))

To activate the load torque monitoring in the first quadrant, click "Yes" in the drop-down list.

##### Parameterizing speed/torque thresholds

The load torque monitoring allows up to three torque and speed thresholds to be parameterized as envelope curves. The torque thresholds are located on the abscissa.

- Load monitoring torque threshold 1, lower ([p2186](SINAMICS%20Parameter%20G120.md#p21860n-load-monitoring-torque-threshold-1-lower-1))
- Load monitoring torque threshold 1, upper ([p2185](SINAMICS%20Parameter%20G120.md#p21850n-load-monitoring-torque-threshold-1-upper-1))
- Load monitoring torque threshold 2, lower ([p2188](SINAMICS%20Parameter%20G120.md#p21880n-load-monitoring-torque-threshold-2-lower-1))
- Load monitoring torque threshold 2, upper ([p2187](SINAMICS%20Parameter%20G120.md#p21870n-load-monitoring-torque-threshold-2-upper-1))
- Load monitoring torque threshold 3, upper ([p2189](SINAMICS%20Parameter%20G120.md#p21890n-load-monitoring-torque-threshold-3-upper-1))

The speed thresholds are located on the ordinate.

- Load monitoring speed threshold value 1 ([p2182](SINAMICS%20Parameter%20G120.md#p21820n-load-monitoring-speed-threshold-value-1))
- Load monitoring speed threshold value 2 ([p2183](SINAMICS%20Parameter%20G120.md#p21830n-load-monitoring-speed-threshold-value-2))
- Load monitoring speed threshold value 3 ([p2184](SINAMICS%20Parameter%20G120.md#p21840n-load-monitoring-speed-threshold-value-3))

##### Delay times

A fault or alarm message can be delayed via the delay time parameter. This prevents false alarms caused by brief transitional states.

- Load monitoring delay time ([p2192](SINAMICS%20Parameter%20G120.md#p21920n-load-monitoring-delay-time))

##### Load monitoring speed deviation

Setting of the permissible speed deviation during load monitoring ([p3231](SINAMICS%20Parameter%20G120.md#p32310n-load-monitoring-speed-deviation)).

##### Load monitoring

- "Load monitoring, actual speed value" ([p3230](SINAMICS%20Parameter%20G120.md#p32300n-ci-load-monitoring-speed-actual-value)); signal source to interconnect the actual speed value.
- "Load monitoring failure detection" ([p3232](SINAMICS%20Parameter%20G120.md#p32320n-bi-load-monitoring-failure-detection)); signal source to detect a failure.

##### Function diagrams (FD)

- Load monitoring - 8013 -

##### Additional parameters

---

#### Speed messages

This section contains information on the following topics:

- [G120 CU250S-2 V actual speed value messages](#g120-cu250s-2-v-actual-speed-value-messages)
- [G120 CU250S-2 V speed messages](#g120-cu250s-2-v-speed-messages)
- [G120 CU250S-2 V setpoint / actual value message](#g120-cu250s-2-v-setpoint-actual-value-message)

##### G120 CU250S-2 V actual speed value messages

###### Description

Comparators are provided for the monitoring of the actual speed and setpoint thresholds that are used to activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or

initiate product steps for other plant sections (e.g. open gates for pumps and fans).

**Parameters**

1. Enter the time constant of the PT1 element for smoothing the actual speed/velocity value at "Smoothing" ([p2153](SINAMICS%20Parameter%20G120.md#p21530n-speed-actual-value-filter-time-constant)).

   The smoothed actual speed/velocity is compared with the threshold values and is only used for messages.
2. Set the hysteresis speed (bandwidth) for the message "f or n comparison value reached or exceeded" (BO: [r2199](SINAMICS%20Parameter%20G120.md#r219905-cobo-status-word-monitoring-3).1) at "Hysteresis speed 1" ([p2142](SINAMICS%20Parameter%20G120.md#p21420n-hysteresis-speed-1)).
3. Select the parameters with which the signal "f or n comparison value reached/exceeded" is to be interconnected at "f or n comparison value reached/exceeded" (r2199). Several interconnections are possible.

   Interconnect binector output:

   The "f or n comparison value reached/exceeded" signal is generated under consideration of hysteresis speed 1, speed threshold value 1 and the ON delay.
4. Enter the speed threshold 1 at "Speed threshold 1" ([p2141](SINAMICS%20Parameter%20G120.md#p21410n-speed-threshold-1)).
5. Enter the ON delay time for signal |n_act| > speed threshold at "ON delay" ([p2156](SINAMICS%20Parameter%20G120.md#p21560n-on-delay-comparison-value-reached)).
6. Set the bandwidths for the following messages at "Hysteresis speed 2" ([p2140](SINAMICS%20Parameter%20G120.md#p21400n-hysteresis-speed-2)):

   - |n_act| < speed threshold 2
   - n_set > speed threshold 2
7. Enter the speed threshold 2 at "Speed threshold 2" ([p2155](SINAMICS%20Parameter%20G120.md#p21550n-speed-threshold-2)).
8. Set the bandwidths for the for the message n_act > n_max at "Hysteresis speed n_act > n_max" ([p2162](SINAMICS%20Parameter%20G120.md#p21620n-hysteresis-speed-n_act-n_max)).
9. Select the parameters which are to be interconnected with the n_act > n_max signal at "|n_act| > n_max" ([r2197](SINAMICS%20Parameter%20G120.md#r2197013-cobo-status-word-monitoring-1-1)). Several interconnections are possible.

   Interconnect binector output:

   Signal n_act > n_max is generated under consideration of hysteresis speed n_act > n_max.

   For a negative speed limit, the hysteresis is effective below the limit value and for a positive speed limit, above the limit value.

   Note:  
   The limits are set in the setpoint channel; see also [G120 CU250S-2 V speed limitation](#g120-cu250s-2-v-speed-limitation).

###### Function diagrams (FD)

- Speed messages 1 - 8010 -
- Generation of the speed limits (p0108.8 = 0) - 3095 -
- Skip frequency bands and speed limits - 3050 -

###### Additional parameters

---

##### G120 CU250S-2 V speed messages

###### Description

Comparators are provided for the monitoring of the actual speed and setpoint thresholds that are used to activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

**Parameters**

1. Set the bandwidths for the following messages at "Hysteresis speed 3" ([p2150](SINAMICS%20Parameter%20G120.md#p21500n-hysteresis-speed-3)):

   - |n_act| < speed setpoint 3
   - n_set >= 0
   - n_act >= 0

   The calculation mode is defined using [p0340](SINAMICS%20Parameter%20G120.md#p03400n-automatic-calculation-motorcontrol-parameters-2).
2. Select the parameters which are to be interconnected with the n_act >= 0 signal at "|n_act| >= 0" ([r2197](SINAMICS%20Parameter%20G120.md#r2197013-cobo-status-word-monitoring-1-1)). Several interconnections are possible.

   Signal n_act >= 0 is generated under consideration of hysteresis speed 3.
3. Select the parameters which are to be interconnected with the |n_act| < speed threshold 3 signal at "|n_act| < speed threshold 3" ([r2199](SINAMICS%20Parameter%20G120.md#r219905-cobo-status-word-monitoring-3)). Several interconnections are possible.

   Signal |n_act| < speed threshold 3 is generated under consideration of hysteresis speed 3 and speed threshold 3.
4. Set the speed threshold 3 for |n_act| < speed setpoint 3 at "Speed threshold 3" ([p2161](SINAMICS%20Parameter%20G120.md#p21610n-speed-threshold-3)).
5. Select the parameters which are to be interconnected with the |n_act| < p2161 signal at "|n_act| < p2161" ([r2198](SINAMICS%20Parameter%20G120.md#r2198412-cobo-status-word-monitoring-2)). Several interconnections are possible.
6. Select the parameters which are to be interconnected with the n_set > 0 signal at "n_set > 0" (r2198).
7. Select the signal source for the speed setpoint messages at "n_set / n_set 2" ([p2151](SINAMICS%20Parameter%20G120.md#p21510n-ci-speed-setpoint-for-messagessignals)).

###### Function diagrams (FD)

- Speed messages 1 - 8010 -
- Speed messages 2 - 8011 -

###### Additional parameters

---

##### G120 CU250S-2 V setpoint / actual value message

###### Description

Comparators are provided for the monitoring of the actual speed and setpoint thresholds that are used to activate monitoring functions (e.g. air flow monitor for fans, pressure switch for pumps) or initiate product steps for other plant sections (e.g. open gates for pumps and fans).

**Parameters**

1. Set the bandwidth for the following message at "Hysteresis speed 4" ([p2164](SINAMICS%20Parameter%20G120.md#p21640n-hysteresis-speed-4)):

   - Speed setp - act val deviation in tolerance t_off
2. Enter a speed threshold at "Speed threshold 4" ([p2163](SINAMICS%20Parameter%20G120.md#p21630n-speed-threshold-4)).
3. Enter the OFF delay time for the message "Speed setp - act val deviation in tolerance t_off" at "OFF delay" ([p2166](SINAMICS%20Parameter%20G120.md#p21660n-off-delay-n_act-n_set)).
4. Interconnect a signal for the display of the 1st status word to be interconnected at "Speed setp - act val deviation in tolerance t_off" ([r2197](SINAMICS%20Parameter%20G120.md#r2197013-cobo-status-word-monitoring-1-1)) (see also online help for the parameter).
5. Select whether you want to output an alarm message in the "Alarm message" ([p2149](SINAMICS%20Parameter%20G120.md#p21490n-monitoring-configuration)) drop-down list.
6. Enter an ON delay time for the signal "Speed setp - act val deviation in tolerance t_off" at "ON delay" ([p2167](SINAMICS%20Parameter%20G120.md#p21670n-switch-on-delay-n_act-n_set)).
7. Set a signal source for the "Ramp-function generator active" signal at "RFG active" ([p2148](SINAMICS%20Parameter%20G120.md#p21480n-bi-rfg-active)) for the following messages:

   - Speed setp - act val deviation in tolerance t_on
   - Ramp-up/ramp-down completed
8. Interconnect a signal for the display of the Monitoring 3 status word at "Speed setp - act val deviation in tolerance t_on" ([r2199](SINAMICS%20Parameter%20G120.md#r219905-cobo-status-word-monitoring-3)) (see also online help for the parameter).
9. Interconnect a signal for the display of the Monitoring 3 status word at "Ramp-up/ramp-down completed" (r2199) (see also online help for the parameter).

###### Function diagrams (FD)

- Speed messages 1 - 8010 -
- Speed messages 1 - 8010 -

###### Additional parameters

---

## Application functions

This section contains information on the following topics:

- [Basic positioner](#basic-positioner)
- [Position controller](#position-controller)
- [Technology controller](#technology-controller)
- [Free function blocks](#free-function-blocks)

### Basic positioner

This section contains information on the following topics:

- [Limitation](#limitation)
- [EPOS jogging](#epos-jogging)
- [Homing](#homing)
- [Traversing blocks](#traversing-blocks)
- [Direct setpoint specification / MDI](#direct-setpoint-specification-mdi)

#### Limitation

This section contains information on the following topics:

- [Limit traversing range](#limit-traversing-range)
- [Limiting the traversing profile](#limiting-the-traversing-profile)

##### Limit traversing range

###### Description

The dynamic limitations, the limits for the software limit switches and the STOP cams for the Basic Positioner function module, are parameterized here.

**Limit traversing range**

The traversing range can be limited using both software and hardware.

**Software limit switch**

1. "Activate software limit switch; signal source for activation of the software limit switch ([p2582](SINAMICS%20Parameter%20G120.md#p2582-bi-epos-software-limit-switch-activation)) (static dynamic). The software limit switch is defined, for example, by a traversing range limit. The software limit switch is active only when a homing has been performed and the modulo correction is not active.
2. "Activate modulo correction"; signal source for activation of the modulo correction ([p2577](SINAMICS%20Parameter%20G120.md#p2577-bi-epos-modulo-correction-activation)).
3. Enter a negative ([p2580](SINAMICS%20Parameter%20G120.md#p2580-co-epos-software-limit-switch-minus)) and a positive end position ([p2581](SINAMICS%20Parameter%20G120.md#p2581-co-epos-software-limit-switch-plus)) and interconnect the signals [p2579](SINAMICS%20Parameter%20G120.md#p2579-ci-epos-software-limit-switch-plus-signal-source) and [p2578](SINAMICS%20Parameter%20G120.md#p2578-ci-epos-software-limit-switch-minus-signal-source).

**STOP cams**

1. Activate the STOP cams ([p2568](SINAMICS%20Parameter%20G120.md#p2568-bi-epos-stop-cam-activation)) via BICO interconnection (static or dynamic). The STOP cam is specified by a signal from the hardware that you must parameterize, e.g. using a BERO signal.
2. Select a signal source for both the minus STOP cam ([p2569](SINAMICS%20Parameter%20G120.md#p2569-bi-epos-stop-cam-minus)) and plus STOP cam ([p2570](SINAMICS%20Parameter%20G120.md#p2570-bi-epos-stop-cam-plus)).

   When a STOP cam is detected, a stop is performed with the maximum deceleration. Only those motions that leave the STOP cams are permitted for approached STOP cams.

###### G120 CU250S-2 function diagrams (FD)

- Traversing range limits - 3630 -

###### Additional parameters

---

##### Limiting the traversing profile

###### Description

You specify the limits for the traversing profile here.

For further information, see also [Limiting the traversing profile](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#limiting-the-traversing-profile).

###### Maximum limitations of the basic positioner

1. Under "Max. velocity" ([p2571](SINAMICS%20Parameter%20G120.md#p2571-epos-maximum-velocity)), enter a value in LU for the maximum velocity.

   The maximum velocity defines the maximum travel velocity [1000 LU/min]. A change immediately limits the velocity of a running traversing block.

   The "Corresponds to speed" field displays the converted speed, the "Max. speed" field the maximum speed.

   The limitation acts in positioning operation (jogging, processing the traversing blocks, setpoint direct input, travel to homing point).
2. At "Max. acceleration" ([p2572](SINAMICS%20Parameter%20G120.md#p2572-epos-maximum-acceleration)), enter a value in LU for the maximum acceleration.
3. At "Max. deceleration" ([p2573](SINAMICS%20Parameter%20G120.md#p2573-epos-maximum-deceleration)), enter a value in LU for the maximum deceleration.

   The maximum acceleration/deceleration are used to specify the maximum acceleration for increasing the velocity and the maximum deceleration for reducing the velocity. Both values act in positioning operation (jogging, processing the traversing blocks, setpoint direct input, travel to homing point).

   Enter a value for the maximum acceleration.
4. At "Max. jerk" ([p2574](SINAMICS%20Parameter%20G120.md#p2574-epos-jerk-limiting-1)), enter a value for the maximum jerk.
5. Click on the button "Accept ramp down values" to accept the values for the "maximum acceleration" and "maximum deceleration" to the OFF1 ramp down time and OFF3 ramp down time fields.
6. Under "OFF1 ramp down time" ([p1121](SINAMICS%20Parameter%20G120.md#p11210n-ramp-function-generator-ramp-down-time-5)), parameterize the OFF1 ramp down time for the ramp-function generator.
7. Under "OFF3 ramp down time" ([p1135](SINAMICS%20Parameter%20G120.md#p11350n-off3-ramp-down-time-5)), parameterize the OFF3 ramp down time for the ramp-function generator.

**Jerk limitation**

1. Under "Max. jerk" ([p2575](SINAMICS%20Parameter%20G120.md#p2575-bi-epos-jerk-limiting-activation)), enter a value in LU for the maximum jerk limitation.

   The converted values for the minimum acceleration time and minimum deceleration time are displayed in the adjacent fields. The tooltip shows the conversion formulas.
2. '"Jerk limitation activation" (p2575); signal source for the activation of the EPOS jerk limitation.

> **Note**
>
> If the command Jerk is used in the traversing blocks, the Jerk limitation activation may not be interconnected!

###### G120 CU250S-2 function diagrams (FD)

- Traversing range limits - 3630 -

###### Additional parameters

---

#### EPOS jogging

This section contains information on the following topics:

- [EPOS jogging configuration](#epos-jogging-configuration)
- [EPOS jogging diagnostics](#epos-jogging-diagnostics)

##### EPOS jogging configuration

###### Description

Jogging is the simplest position-controlled traversing possibility. For example, you can use "EPOS jogging incremental" to traverse the drive either with endless traversing (jogging) or over a parameterizable section. In jogging operation, the parameterized maximum acceleration or maximum deceleration is used for the acceleration or deceleration, respectively.

For further information, see also [Jog velocity](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#jog-velocity), [Incremental jogging](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#incremental-jogging) and [Setting jogging](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-jogging).

###### Digital signals

- Click "Digital signals" to edit the binector inputs and outputs for "Jog".

1. "EPOS jog 1 signal source" ([p2589](SINAMICS%20Parameter%20G120.md#p2589-bi-epos-jog-1-signal-source)); interconnection of the signal source for EPOS jog 1.
2. "EPOS jog 2 signal source" ([p2590](SINAMICS%20Parameter%20G120.md#p2590-bi-epos-jog-2-signal-source)); interconnection of the signal source for EPOS jog 2.
3. "EPOS jogging incremental" ([p2591](SINAMICS%20Parameter%20G120.md#p2591-bi-epos-jogging-incremental)); interconnection of the signal source for EPOS jogging incremental.

The movement results only from the Jogging 1 (p2589) or Jogging 2 (p2590) traversing command. The following jogging dependencies apply:

- p2591 = 0 (EPOS jogging incremental is not active)

  - When a traversing command is specified for jogging 1 (p2589), endless traversing with velocity jogging 1 ([p2585](SINAMICS%20Parameter%20G120.md#p2585-epos-jog-1-setpoint-velocity)) results.
  - When a traversing command is specified for jogging 2 (p2590), endless traversing with velocity jogging 2 ([p2586](SINAMICS%20Parameter%20G120.md#p2586-epos-jog-2-setpoint-velocity)) results.
  - If jogging 1 and jogging 2 are triggered simultaneously, no movement takes place and a warning message (A7457) is output.
  - If jogging 1 and jogging 2 are triggered successively, the current velocity is retained and a warning message A7457 will be output.
- p2591 = 1 (EPOS jogging incremental)

  - A traversing command with velocity jogging 1 (p2585) is specified for jogging 1 (p2589) to traverse the traverse path in [p2587](SINAMICS%20Parameter%20G120.md#p2587-epos-jog-1-traversing-distance).
  - A traversing command with velocity jogging 2 (p2590) is specified for jogging 2 (p2586) to traverse the traverse path in [p2588](SINAMICS%20Parameter%20G120.md#p2588-epos-jog-2-traversing-distance).
  - If jogging 1 and jogging 2 are triggered simultaneously, the traversing distance in p2587 is always traversed at the velocity in p2589.
  - If jogging 1 and jogging 2 are triggered successively, the traverse command that arrives last will be ignored.

###### Outputs

Interconnect the binector outputs to display the parameters of the position status words.

###### Analog signals

1. Click "Analog signals" to edit the connector inputs and outputs for "Jog".
2. "Velocity override" ([p2646](SINAMICS%20Parameter%20G120.md#p2646-ci-epos-velocity-override)); interconnection of the signal source of the velocity override. The velocity override is a factor that you can use to influence the velocity (0% ... 100%).

###### Configuring the jogging setpoints

1. Click the button to open the "Configure jog setpoints" dialog box.
2. At "EPOS jog 1 setpoint velocity" (p2585), enter a value [1000 LU/min]. Velocity setpoint 1 is used, or retain setpoint.
3. At "EPOS jog 2 setpoint velocity" (p2586), enter a value [1000 LU/min]. Velocity setpoint 2 is used, or retain setpoint.
4. At "EPOS jog 1 traversing distance" (p2587), enter a value for the traversing distance for incremental jogging 1. The drive traverses relatively or retains the setpoint.
5. At "EPOS jog 2 traversing distance" (p2588), enter a value for traversing distance 1 for incremental jogging 1. The drive traverses relatively or retains the setpoint.
6. Click the "Ramp-function generator" button to show the settings for the ramp-function generator in the jogging mode.

###### Parameterizing ramp-function generator jog

You can parameterize an acceleration ramp and a deceleration ramp with the ramp-function generator:

1. Enter a value for the maximum acceleration during ramp-up at "Maximum acceleration" ([p2572](SINAMICS%20Parameter%20G120.md#p2572-epos-maximum-acceleration)).
2. Enter a value to limit the deceleration during braking at "Maximum deceleration" ([p2573](SINAMICS%20Parameter%20G120.md#p2573-epos-maximum-deceleration)).

###### Outputs

- Connect the connector outputs to display the parameters of the position status words.

###### G120 CU250S-2 function diagrams (FD)

- Jog mode - 3610 -

###### Additional parameters

---

##### EPOS jogging diagnostics

###### Description

All the variables that are relevant for the operating mode are displayed here. This provides an overview and a diagnostic capability for the current state of the "EPOS jogging" mode.

###### G120 CU250S-2 function diagrams (FD)

- Jog mode - 3610 -

#### Homing

This section contains information on the following topics:

- [Homing](#homing-1)
- [Homing configuration](#homing-configuration)
- [Homing diagnostics](#homing-diagnostics)
- [Active homing / homing procedure](#active-homing-homing-procedure)
- [Passive homing](#passive-homing)

##### Homing

###### Description

The absolute dimensional reference for the machine zero point must be established to permit positioning. This procedure is called homing. See also [Referencing methods](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#referencing-methods).

The following homing types are possible:

**Set home position**

The current actual position of the drive then becomes the home position. The following positioning jobs are then always performed based on this home position.

**Travel to home position (active homing - incremental)**

For an incremental measuring system, you can also use travel to home position to move the drive without higher-level control to its home position. The drive itself controls and monitors the homing cycle.

**Absolute encoder calibration (active homing - absolute)**

Absolute encoders have to be adjusted during commissioning. Once the machine has been switched off, the encoder’s position information is retained. The absolute encoder will first be adjusted to the home position, e.g. by jogging.

**Flying homing (passive homing)**

For flying homing, the homing overlays a traversing block (jogging, traversing blocks or setpoint direct predefinition / MDI mode). In this case, the traversing block of the associated mode will be performed and also the evaluation of the measuring input activated. With the recognition of the measuring input, the difference of the homing point coordinate and the determined measured value will be corrected on-the-fly (during the motion) taking account of the window limits and the traversing block completed.

###### G120 CU250S-2 function diagrams (FD)

- Referencing/reference point approach mode (p2597 = 0) - 3612 -
- Flying referencing mode (p2597 = 1) - 3614 -

##### Homing configuration

###### Description

You can perform the configuration for homing here. For further information, see [Referencing methods](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#referencing-methods) and [Setting the reference point approach](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-reference-point-approach).

**Digital signals**

1. Click "Digital signals" to edit the binector inputs and outputs for "Homing".
2. "Start homing" ([p2595](SINAMICS%20Parameter%20G120.md#p2595-bi-epos-referencing-start)); signal source to start the homing procedure.
3. "Set home position" ([p2596](SINAMICS%20Parameter%20G120.md#p2596-bi-epos-set-reference-point)); signal source that you would like to use in order to initiate the Set home position command.

   The home position can be set when no traversing command is active or has been interrupted by an intermediate stop.
4. "Homing type selection" ([p2597](SINAMICS%20Parameter%20G120.md#p2597-bi-epos-referencing-type-selection)); signal source with which you want to specify the homing type. Active homing and passive homing are possible. For passive homing, level 1 must be present at the binector input; level 0 must be present correspondingly for active homing.
5. "Homing procedure homing cam" ([p2611](SINAMICS%20Parameter%20G120.md#p2611-epos-search-for-reference-approach-velocity-reference-point)); signal source that specifies the homing cam.
6. "Homing procedure reversing cam, minus" ([p2613](SINAMICS%20Parameter%20G120.md#p2613-bi-epos-search-for-reference-reversing-cam-minus)); signal source for the reversing cam in the negative traversing direction.
7. "Homing procedure reversing cam, plus" ([p2614](SINAMICS%20Parameter%20G120.md#p2614-bi-epos-search-for-reference-reversing-cam-plus)); signal source for the reversing cam in the positive traversing direction.

**Outputs**

Display the parameters of the position status words via the binector outputs.

**Analog signals**

1. Click "Analog signals" to edit the connector inputs and outputs for "Homing".
2. "Velocity override" ([p2646](SINAMICS%20Parameter%20G120.md#p2646-ci-epos-velocity-override)); signal source for the velocity override. The velocity override is a factor that you can use to influence the velocity.
3. "Home position coordinate" (2598); signal source for the coordinate of the home position.

**Outputs**

The connector outputs can be used to display the parameters of the position status words.

###### G120 CU250S-2 function diagrams (FD)

- Referencing/reference point approach mode (p2597 = 0) - 3612 -
- Flying referencing mode (p2597 = 1) - 3614 -

###### Additional parameters

---

##### Homing diagnostics

###### Description

All the variables that are relevant for the operating mode are displayed here. This provides an overview and a diagnostic capability for the current state of the "Active homing" mode.

##### Active homing / homing procedure

###### Description

You edit the parameters for active homing here. Different screen forms will be displayed depending on whether you are using an incremental encoder or an absolute encoder.

For further information, see also [Setting the reference point approach](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-reference-point-approach), [Set reference point](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#set-reference-point) and [Absolute encoder adjustment](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#absolute-encoder-adjustment).

**Incremental encoder**

If you use an incremental encoder, you can select one of the following options for **homing mode**:

- Homing cam and encoder zero mark
- Encoder zero mark
- External zero mark

**Start direction for homing procedure ([p2604](SINAMICS%20Parameter%20G120.md#p2604-bi-epos-search-for-reference-start-direction))**

- Select whether you want to perform homing in the positive or negative direction.

**External zero mark selection ([p0494](SINAMICS%20Parameter%20G120.md#p04940n-equivalent-zero-mark-input-terminal-1))**

- Select the signal that supplies the external zero mark in the drop-down list. If you change the signal, you receive messages providing further information.

**Approach possibilities**

1. Enter a velocity ([p2605](SINAMICS%20Parameter%20G120.md#p2605-epos-search-for-reference-approach-velocity-reference-cam)) to be used to traverse to the homing cam [100 LU/min]. The homing procedure starts only when a homing cam is present ([p2607](SINAMICS%20Parameter%20G120.md#p2607-epos-search-for-reference-reference-cam-present) = 1).
2. Enter a velocity ([p2611](SINAMICS%20Parameter%20G120.md#p2611-epos-search-for-reference-approach-velocity-reference-point)) to be used to traverse to the home position [100 LU/min]. This velocity is used for traversing between the synchronization with the zero mark and the reaching of the home position.
3. Enter a velocity ([p2608](SINAMICS%20Parameter%20G120.md#p2608-epos-search-for-reference-approach-velocity-zero-mark)) to be used to traverse to the zero mark [100 LU/min] (only homing cam and encoder zero mark). This velocity is used for traversing between the recognition of the homing cam and the synchronization with the zero mark.

**Home position coordinate**

- Enter a home position coordinate [LU] ([p2599](SINAMICS%20Parameter%20G120.md#p2599-co-epos-reference-point-coordinate-value)). The position value will be set as current axis position after the homing or calibration.

**Home position offset**

- Enter a home position offset ([p2600](SINAMICS%20Parameter%20G120.md#p2600-epos-search-for-reference-reference-point-offset)). For incremental measuring systems, after the recognition of the zero mark, the axis will traverse by the home position offset. The axis has reached the home position of this position, and accepts the home position coordinate as new actual value.

**Tolerance for travel to the zero mark**

- Enter a value for a tolerance range for the distance to the zero mark ([p2610](SINAMICS%20Parameter%20G120.md#p2610-epos-search-for-ref-tol-bandwidth-for-distance-to-zero-mark)).

**Maximum distance to zero mark**

- Enter a value for the maximum distance ([p2609](SINAMICS%20Parameter%20G120.md#p2609-epos-search-for-reference-max-distance-ref-cam-and-zero-mark)) that the axis may travel on leaving the homing cam in order to reach the zero mark.

**Maximum distance to homing cam**

- Enter a value for the maximum distance ([p2606](SINAMICS%20Parameter%20G120.md#p2606-epos-search-for-reference-reference-cam-maximum-distance)) that the axis may travel in order to reach the homing cam.

**Absolute encoder**

If you use an absolute encoder, you only need to perform an absolute value calibration.

- Click the "Perform absolute encoder adjustment" button. The button is active only online. If the calibration is successful, a message appears.

###### G120 CU250S-2 function diagrams (FD)

- Referencing/reference point approach mode (p2597 = 0) - 3612 -
- Flying referencing mode (p2597 = 1) - 3614 -

###### Additional parameters

---

##### Passive homing

###### Description

Passive homing, also called flying homing, can be used for each mode (jogging, offset and setpoint direct specification / MDI) and will overlay the respective mode. Passive homing is identical for incremental and absolute measuring systems (encoder).

For further information, see also [Setting the flying referencing](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-flying-referencing).

You can configure measuring input 1 or measuring input 2 for the passive homing. If necessary, you must search for the homing mark via the expert list.

**Select measuring input**

1. "Select measuring input" ([p2510](SINAMICS%20Parameter%20G120.md#p251003-bi-lr-selecting-measuring-probe-evaluation)); signal source to select whether measuring input 2 or measuring input 1 is to be activated.
2. Select the digital input via which "Measuring input 1 input terminal" ([p0488](SINAMICS%20Parameter%20G120.md#p048802-measuring-probe-1-input-terminal-1)) is to be recognized.
3. Select the digital input via which "Measuring input 2 input terminal" ([p0489](SINAMICS%20Parameter%20G120.md#p048902-measuring-probe-2-input-terminal-1)) is to be recognized.

**Edge evaluation**

- "Edge evaluation" ([p2511](SINAMICS%20Parameter%20G120.md#p251103-bi-lr-measuring-probe-evaluation-edge)); signal source used to specify whether the measuring input is to evaluate the positive or the negative edge.

**Positioning mode for relative positioning**

- Select whether or not the correction made for relative positioning is to be taken into account for the traversing distance in the drop-down list ([p2603](SINAMICS%20Parameter%20G120.md#p2603-epos-flying-referencing-positioning-mode-relative)).

**Inner window**

- Enter a value for the inner window ([p2601](SINAMICS%20Parameter%20G120.md#p2601-epos-flying-referencing-inner-window)) for the window evaluation [LU]. If the position difference for a previously homed drive is less than the inner window (p2601), the old actual position value is retained. If the position difference is larger than the inner window and less than the outer window, the actual position value will be corrected.

**Outer window**

- Enter a value for the outer window ([p2602](SINAMICS%20Parameter%20G120.md#p2602-epos-flying-referencing-outer-window)) for the window evaluation [LU]. If the position difference for a previously homed drive is larger than the outer window (p2602), a warning will be output.

###### G120 CU250S-2 function diagrams (FD)

- Referencing/reference point approach mode (p2597 = 0) - 3612 -
- Flying referencing mode (p2597 = 1) - 3614 -

###### Additional parameters

---

#### Traversing blocks

This section contains information on the following topics:

- [Traversing blocks configuration](#traversing-blocks-configuration)
- [Traversing blocks diagnostics](#traversing-blocks-diagnostics)
- [Traversing blocks parameterization](#traversing-blocks-parameterization)
- [External block change](#external-block-change)
- [Configuration of the fixed stop](#configuration-of-the-fixed-stop)
- [Configuration of the digital output of traversing blocks](#configuration-of-the-digital-output-of-traversing-blocks)

##### Traversing blocks configuration

###### Description

"Traversing blocks" are used to define up to 16 traversing blocks in the drive. The BICO interconnection is used for the selection and the activation.

For further information, see also [Traversing blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#traversing-blocks-1).

> **Note**
>
> As the binectors and connectors are already connected as standard, the BICO interconnections do not normally need to be edited.

###### Digital signals

1. Click "Digital signals" to edit the binector inputs and outputs for traversing blocks.
2. Use "Activate EPOS traversing block" to interconnect the source for the activation command. A positive edge starts the traversing block selected at "Block selection".
3. "Fixed stop reached" ([p2637](SINAMICS%20Parameter%20G120.md#p2637-bi-epos-fixed-stop-reached)); signal source for the fixed stop detection. You can also set this in the "Fixed stop configuration" dialog box.
4. "Fixed stop outside monitoring window" ([p2638](SINAMICS%20Parameter%20G120.md#p2638-bi-epos-fixed-stop-outside-the-monitoring-window)); signal source for the fixed stop detection. You can set the monitoring window in the "Fixed stop configuration" dialog box.
5. "Torque limit reached" ([p2639](SINAMICS%20Parameter%20G120.md#p2639-bi-epos-torque-limit-reached)); signal source for the "Torque limit reached" feedback.
6. "EPOS intermediate stop" ([p2640](SINAMICS%20Parameter%20G120.md#p2640-bi-epos-intermediate-stop-0-signal)); signal source for a stop command. You can continue the traversing block using a 0/1 change.
7. "EPOS reject traversing block" ([p2641](SINAMICS%20Parameter%20G120.md#p2641-bi-epos-reject-traversing-task-0-signal)); signal source for the "Reject traversing block" command. The currently active traversing block will be stopped with maximum deceleration and cannot be continued.

###### Select traversing blocks

The "Traversing block selection bit 0 ... bit 3" ([p2625](SINAMICS%20Parameter%20G120.md#p2625-bi-epos-traversing-block-selection-bit-0)) binector inputs can be used to select the required traversing block (0 ... 16).

###### Outputs

The binector outputs display the parameters of the position status words.

###### Analog signals

1. Click "Analog signals" to edit the connector inputs and outputs for traversing blocks.
2. "Velocity override" ([p2646](SINAMICS%20Parameter%20G120.md#p2646-ci-epos-velocity-override)); signal source for the velocity override. The velocity override is a factor that you can use to influence the velocity.

###### Outputs

The connector outputs display the parameters of the position status words.

###### Programming traversal requests

- Click the "Program traversing blocks" button to open the appropriate screen form.

###### G120 CU250S-2 function diagrams (FD)

- Traversing block mode, external block change - 3615 -
- Traversing block mode - 3616 -

###### Additional parameters

---

##### Traversing blocks diagnostics

###### Description

All the variables that are relevant for the operating mode are displayed here. This provides an overview and a diagnostic capability for the current state of the "Traversing blocks" mode.

##### Traversing blocks parameterization

###### Description

You parameterize the traversing blocks here. Up to 16 blocks are possible. You parameterize each individual traversing block in the table. The various parameters are entered in the columns.

For further information, see also [Setting traversing blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-traversing-blocks), [Travel to fixed stop](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#travel-to-fixed-stop) and [Application examples](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#application-examples).

**Maximum number of blocks**

- Click "Edit" to edit the maximum number of blocks. The number of rows in the table then changes accordingly.

If you reduce the number of traversing blocks, the excessive traversing blocks will be lost.

###### Parameterizing the traversing blocks

The following parameters can be used to parameterize a traversing block:

**Index**

The Index column shows the index of the corresponding parameters.

**Number [-1, 0, ... 15]**

The number represents the block number ([p2616](SINAMICS%20Parameter%20G120.md#p26160n-epos-traversing-block-block-number)). It is used to uniquely identify the request when a selection is made using the block selection bit 0 ... 3 signals. If there are several requests, they are edited in ascending order. Traversal requests with number -1 will be ignored. This allows the request to be removed from the sequence without deleting it. You can specify any request number [0 ... 15]. This means, for example, you can define a request 5 after request 2 and reserve numbers 3 and 4 for subsequent editing.

**Job**

Select one of the following jobs in the "Job" drop-down list:

- [1] POSITIONING -> initiates a traversing motion until the target position is reached.
- [2] FIXED_STOP -> allows a clamping torque and a clamping force to be entered for the fixed stop; activates the Configuration of fixed stop button, which you can use to call a dialog for configuring the fixed stop parameters.
- [3] ENDLESS_POS -> accelerates to the defined velocity.
- Until the software limit switch is reached.
- Until the travel area limit is reached.
- Until the motion is interrupted by BB/intermediate stop.
- Until the motion is aborted by BB/Reject traversing block.
- [4] ENDLESS_NEG -> see above.
- [5] WAIT - defines a wait time for the following job.
- [6] GOTO -> allows you to make jumps within a series of traversal requests. The block number to which the jump is to be made must be specified as request parameter (see below).
- [7] SET_O -> allows up to two digital outputs to be set at the same time.
- [8] RESET_O -> allows up to two digital outputs to be reset at the same time.
- [9] JERK -> enables jerk limitation.

**Request parameter**

The supplementary information for the requests is queried here:

- WAIT -> wait time in [ms].
- GOTO -> block number (see request).
- SET_O -> set digit output 1, 2 or both (3).
- RESET_O -> reset digit output 1, 2 or both (3).
- JERK -> "1" to activate or "0" to deactivate.
- FIXED_STOP -> input of the clamping torque [0.01 Nm] and clamping force [Nm].

**Request mode**

Specify the positioning mode here:

- ABSOLUTE - > travel to the specified position.
- RELATIVE -> traverse the axis by the specified value.
- ABS_POS (only for activated modulo correction) -> travel to the specified position in the direction of increasing actual position values.
- ABS_NEG (only for activated modulo correction) -> travel to the specified position in the direction of decreasing actual position values.

**Position**

- Enter the target position to be traveled to in the traversing block.

**Velocity**

- Enter the velocity with which the traversing command will be performed. The value is influenced by the velocity override.

**Acceleration**

- Enter a value for the acceleration override. The value is influenced by the maximum acceleration.

**Deceleration**

- Enter a value for the delay override. The value is influenced by the maximum deceleration.

**Transition**

The transition specifies the continuation condition when the next traversing block is to be activated. The following settings are possible:

- END -> ends the traversing block; the continuation condition can be used for the pure single operation (each request will be started individually) or for the last traversing block of a sequence.
- CONTINUE_WITH_STOP -> travel is made to exactly the position specified in the traversing block and the axis will be braked to standstill. The following request will be performed without a restart by the "Activate traversing block" ([p2631](SINAMICS%20Parameter%20G120.md#p2631-bi-epos-activate-traversing-task-0---1)) signal as soon as the actual position lies within the positioning window.
- CONTINUE_FLYING -> the following traversing block is processed immediately when the time to apply the brake is reached. If a direction reversal needs to be made, the behavior corresponds to that for CONTINUE_WITH_STOP, i.e. it will be braked to standstill.
- CONTINUE_EXTERNAL -> behavior as with CONTINUE_FLYING, but an immediate block change can be triggered via the signal at the binector input [p2632](SINAMICS%20Parameter%20G120.md#p2632-epos-external-block-change-evaluation) "External block change" up to the time to apply the brake. If an external block change is not triggered, there is a flying change to the next block at the time to apply the brake.
- CONTINUE_EXTERNAL_WAIT -> a flying change to the next request can be triggered during the entire motion phase via the control signal "External block change". If an "external block change" is not triggered, the axis remains in the parameterized target position until the signal is issued.
- CONTINUE_EXTERNAL_ALARM -> the behavior is as with CONTINUE_EXTERNAL_WAIT, but warning A07463 "External traversing block change in traversing block x not requested" is output if an "external block change" has not been triggered before standstill is reached. The alarm can be converted to an alarm with a stop response so that block processing can be aborted if the control signal is not issued.

**Hide**

If you remove the traversing block from the display, it will not be processed. The traversing block then behaves as if it had request number -1.

###### G120 CU250S-2 function diagrams (FD)

- Traversing block mode, external block change - 3615 -
- Traversing block mode - 3616 -

###### Additional parameters

---

##### External block change

###### Description

You parameterize a traversing block change using an external signal here. You have the possibility to interconnect the signal using a measuring input or using BICO. If a valid signal is detected via the measuring input or a signal is issued via BICO, the next traversing block will be started.

Use the measured value determination to specify the signal source and the edge evaluation of the measured value to be processed. You can specify the behavior for a traversing block change during the configuration of the traversing blocks.

**Measured value determination**

1. At "Measuring input selection" ([p2510](SINAMICS%20Parameter%20G120.md#p251003-bi-lr-selecting-measuring-probe-evaluation)), select the measuring input that you want to use. Either permanently or using a signal source.
2. At "Measuring input 1 input terminal" or "Measuring input 2 input terminal" ([p0488](SINAMICS%20Parameter%20G120.md#p048802-measuring-probe-1-input-terminal-1)), select the digital input to be used to detect the measuring input.
3. Use "Edge evaluation" ([p0489](SINAMICS%20Parameter%20G120.md#p048902-measuring-probe-2-input-terminal-1)) to interconnect the source used to specify whether the measuring input is to evaluate the positive or the negative edge.

**External block change using measuring input**

- "External block change" ([p2661](SINAMICS%20Parameter%20G120.md#p2661-bi-epos-measured-value-valid-feedback-signal)), signal source for the "Measured value valid" feedback signal.

**External block change using BICO**

- "External block change" ([p2633](SINAMICS%20Parameter%20G120.md#p2633-bi-epos-external-block-change-0---1)); signal source for the "External block change" setting.

**External traversing block change**

- Select whether the traversing block change is to be initiated using measuring input or using BICO in the drop-down list ([p2632](SINAMICS%20Parameter%20G120.md#p2632-epos-external-block-change-evaluation)).

###### G120 CU250S-2 function diagrams (FD)

- Traversing block mode, external block change - 3615 -
- Traversing block mode - 3616 -

###### Additional parameters

---

##### Configuration of the fixed stop

###### Description

With "Travel to fixed stop", you can, for example, traverse sleeves against the workpiece with a specified torque. You can parameterize the clamping torque in the traversing block. You can parameterize the fixed stop monitoring window in this dialog box. This allows you, for example, to prevent the drive from traversing beyond the window when the fixed stop breaks away.

For further information, see [Travel to fixed stop](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#travel-to-fixed-stop).

**Fixed stop detection**

1. Select which source you want to use for the fixed stop detection from the drop-down list:

   - "Fixed stop detection via external signal": Enables the fixed stop to be detected, e.g. via BERO.
   - "Fixed stop via maximum following error": Enables a following error signaling the "Fixed stop reached" state to be defined (in LU = Length Unit).
2. Enter values in the "Position tolerance after fixed stop detection" ([p2634](SINAMICS%20Parameter%20G120.md#p26340n-epos-fixed-stop-maximum-following-error)) input fields. These enable a monitoring window for the position to be defined in the fixed stop.

###### G120 CU250S-2 function diagrams (FD)

- Travel to fixed stop - 3617 -

###### Additional parameters

---

##### Configuration of the digital output of traversing blocks

###### Description

Digital output 1 and digital output 2

- Interconnect the digital outputs in order to be display r2683.10 and r2683.11 (traversing block active).

#### Direct setpoint specification / MDI

This section contains information on the following topics:

- [Direct setpoint specification / MDI configuration](#direct-setpoint-specification-mdi-configuration)
- [Direct setpoint specification / MDI diagnostics](#direct-setpoint-specification-mdi-diagnostics)
- [Positioning / MDI fixed setpoints](#positioning-mdi-fixed-setpoints)

##### Direct setpoint specification / MDI configuration

###### Description

You can use the predefined dynamic values (velocity, position, acceleration and delay) to perform absolute and relative positioning. With the setup, you can perform an "endless" position-controlled procedure with direct predefined dynamic values (velocity, position, acceleration and delay). You can switch between both modes on the fly. The dynamic values (velocity, position, acceleration and delay) can be specified using the Dynamic fixed setpoints screen form. A PZD transferred via PROFIBUS, for example, can be used as source.

Select one of two modes for the direct setpoint specification:

- Positioning
- Setting up

For further information, see also [Direct setpoint specification (MDI)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#direct-setpoint-specification-mdi).

> **Note**
>
> Absolute direct setpoint specification is possible only for homed axis.

**Digital signals**

1. Click "Digital signals" to edit the binector inputs and outputs for the "Direct setpoint specification".
2. "Direct setpoint specification / MDI selection" ([p2647](SINAMICS%20Parameter%20G120.md#p2647-bi-epos-direct-setpoint-inputmdi-selection)); signal source for the selection of the "Direct setpoint specification / MDI" mode. The selection of this parameter (signal 1) is requirement for **both** modes. If after "Setup" you want to change the mode, the signal must be wired irrespective of whether or not the switching is made on the fly.
3. "Setup selection" ([p2653](SINAMICS%20Parameter%20G120.md#p2653-bi-epos-direct-setpoint-inputmdi-setting-up-selection)); signal source for the selection of the "Setup" mode.
4. "No intermediate stop / intermediate stop" ([p2640](SINAMICS%20Parameter%20G120.md#p2640-bi-epos-intermediate-stop-0-signal)); signal source for a stop command. You can continue the traversing block using a 0/1 change.
5. "Reject traversing block / 0 signal" ([p2641](SINAMICS%20Parameter%20G120.md#p2641-bi-epos-reject-traversing-task-0-signal)); signal source for the "Reject traversing block" command. The currently active traversing block will be stopped with maximum deceleration and cannot be continued (this is not true for the continuous transfer of the setpoints using [p2649](SINAMICS%20Parameter%20G120.md#p2649-bi-epos-direct-setpoint-inputmdi-transfer-type-selection)=1).
6. "Positioning type selection" ([p2648](SINAMICS%20Parameter%20G120.md#p2648-bi-epos-direct-setpoint-inputmdi-positioning-type)); signal source for the selection of the positioning type. "Signal 0" at the binector input means relative positioning; "signal 1" means absolute positioning.
7. "Positive direction selection" ([p2651](SINAMICS%20Parameter%20G120.md#p2651-bi-epos-direct-setpoint-inputmdi-direction-selection-positive)) or "Negative direction selection" ([p2652](SINAMICS%20Parameter%20G120.md#p2652-bi-epos-direct-setpoint-inputmdi-direction-selection-negative)); signal sources for the positive and negative direction selection. The settings depend on each other.

**Outputs**

The binector outputs can be used to display the parameters of the position status words.

**Select acceptance type**

You can use the two binector inputs to control the acceptance type of the setpoints.

1. "Setpoint acceptance edge" ([p2650](SINAMICS%20Parameter%20G120.md#p2650-bi-epos-direct-setpoint-inputmdi-setpoint-acceptance-edge)); signal source for the setpoint acceptance edge.
2. "Transfer type selection" (p2651); signal source for the selection of the transfer type. "Signal 0" allows the setpoints to be accepted using an edge. This requires that you interconnect "Setpoint acceptance edge". "Signal 1" allows a continuous acceptance of the setpoints.

In the "Setup" mode, you also accept the setpoints continuously or edge-controlled.

**Analog signals**

1. Click "Analog signals" to edit the connector inputs and outputs for setpoint specification.
2. "Velocity override" ([p2646](SINAMICS%20Parameter%20G120.md#p2646-ci-epos-velocity-override)); signal source for the velocity override. The velocity override is a factor that you can use to influence the velocity (0%...100%).
3. "Position setpoint" ([p2642](SINAMICS%20Parameter%20G120.md#p2642-ci-epos-direct-setpoint-inputmdi-position-setpoint)); signal source for the position value for direct setpoint specification / MDI.
4. "Acceleration override" ([p2644](SINAMICS%20Parameter%20G120.md#p2644-ci-epos-direct-setpoint-inputmdi-acceleration-override)); signal source for the acceleration override.
5. "Deceleration override" ([p2645](SINAMICS%20Parameter%20G120.md#p2645-ci-epos-direct-setpoint-inputmdi-deceleration-override)); signal source for the deceleration override.
6. "Mode adjustment" ([p2654](SINAMICS%20Parameter%20G120.md#p2654-ci-epos-direct-setpoint-inputmdi-mode-adaptation)); signal source to set the MDI mode via PROFIBUS telegram 110.

**Outputs**

The connector outputs can be used to display the parameters of the position status words.

###### G120 CU250S-2 function diagrams (FD)

- Direct setpoint specification / MDI mode, dynamic response values - 3618 -
- Direct setpoint specification / MDI mode - 3620 -
- Status word, active traversing block / MDI active (r2670) - 3650 -

###### Additional parameters

---

##### Direct setpoint specification / MDI diagnostics

###### Description

All the variables that are relevant for the operating mode are displayed here. This provides an overview and a diagnostic capability for the current state of the "Direct setpoint specification / MDI mode".

##### Positioning / MDI fixed setpoints

###### Description

You enter the appropriate values for the direct setpoint specification here, when, for example, process data (PROFIdrive) is not to be used to specify the setpoints. The values are then used as source for the corresponding parameters for setpoint direct predefinition - analog signals.

For further information, see also [Direct setpoint specification (MDI)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#direct-setpoint-specification-mdi).

1. Enter a value for the "Position setpoint" ([p2690](SINAMICS%20Parameter%20G120.md#p2690-co-epos-position-fixed-setpoint)).
2. Enter a value for the "Velocity setpoint" ([p2691](SINAMICS%20Parameter%20G120.md#p2691-co-epos-velocity-fixed-setpoint)).
3. Enter a value for the "Acceleration override" ([p2692](SINAMICS%20Parameter%20G120.md#p2692-co-epos-acceleration-override-fixed-setpoint)). The acceleration override is a factor that you can use to influence the acceleration (0% ... 100%).
4. Enter a value for the "Deceleration override" ([p2693](SINAMICS%20Parameter%20G120.md#p2693-co-epos-deceleration-override-fixed-setpoint)). The deceleration override is a factor that you can use to influence the deceleration (0% ... 100%).

###### G120 CU250S-2 function diagrams (FD)

- Direct setpoint specification / MDI mode, dynamic response values - 3618 -
- Direct setpoint specification / MDI mode - 3620 -

###### Additional parameters

---

### Position controller

This section contains information on the following topics:

- [Mechanical system](#mechanical-system)
- [Actual position value preparation](#actual-position-value-preparation)
- [Position controller group](#position-controller-group)
- [Monitoring](#monitoring)

#### Mechanical system

##### Description

The dialog box displays the mechanical system configured in the drive wizard. Depending on the encoder type selected for position control and the encoder type selected for the motor encoder, various configurations are represented for the mechanical system.

Further information can be found at [Define the resolution](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#define-the-resolution), [Modulo range setting](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#modulo-range-setting) and [Setting the backlash](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-the-backlash).

**Edit**

1. Click Edit to switch the dialog box to edit mode. Then edit all the drive configuration settings.
2. Click Accept to accept all new settings.

   > **Note**
   >
   > If you have edited the parameters in the dialog box and then clicked Apply, the actual position value preparation is restarted. The system responds in the same way as in the case of a restart, i.e. homing is also reset.

##### Encoder

The display box shows the encoder selected in the dimension system.

##### LU per load revolution (Encoder resolution)

The maximum possible position resolution for the specified mechanical system and encoder data is displayed here.

The maximum value per load revolution is calculated as follows:

Maximum value per load revolution = absolute value of the product of "Encoder pulse number per revolution" and "Fine resolution" multiplied by the quotient from "Motor revolutions" divided by "Load revolutions".

##### Resolution and motor/load revolutions

1. "Encoder pulse number per revolution" ([p0408](SINAMICS%20Parameter%20G120.md#p04080n-rotary-encoder-pulse-number-1)); display field for the encoder pulse number per revolution for encoders from the list ([p0400](SINAMICS%20Parameter%20G120.md#p04000n-encoder-type-selection-2)). If you are using a user-defined encoder, enter the pulse number per revolution here.
2. "Fine resolution" ([p0418](SINAMICS%20Parameter%20G120.md#p04180n-fine-resolution-gx_xist1-in-bits-1)); display field for the fine resolution. The fine resolution specifies the fractional amounts between two encoder lines.
3. At "Load revolutions" ([p2505](SINAMICS%20Parameter%20G120.md#p25050n-lr-motorload-load-revolutions)), enter a value for the load revolutions of the gear ratio between the motor shaft and load shaft.
4. At "Length unit LU per load revolution" ([p2506](SINAMICS%20Parameter%20G120.md#p25060n-lr-length-unit-lu-per-load-revolution)), enter a value to set the neutral length unit LU per load revolution.
5. At "Motor revolutions" ([p2504](SINAMICS%20Parameter%20G120.md#p25040n-lr-motorload-motor-revolutions)), enter a value for the motor revolutions of the gear ratio between the motor shaft and load shaft.

**Modulo range and modulo correction**

1. Enter a value at "Modulo range" ([p2576](SINAMICS%20Parameter%20G120.md#p2576-epos-modulo-correction-modulo-range)). The modulo range is used for the modulo correction of the axes.
2. "Activate modulo correction" ([p2577](SINAMICS%20Parameter%20G120.md#p2577-bi-epos-modulo-correction-activation)); signal source for activation of the modulo correction.

##### Backlash

- Enter a value at "Backlash" ([p2583](SINAMICS%20Parameter%20G120.md#p2583-epos-backlash-compensation)). The backlash on reversal occurs, for example, for the motion reversal of a spindle, and describes the play between the spindle and the table.

##### Additional parameters

---

#### Actual position value preparation

##### Description

The interconnection of the actual position value preparation is displayed here. The actual position value preparation is used to prepare the encoder signals (actual position values) for path units used for the position control. Various correction values can be applied here.

For further information, see also [Read actual position value](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#read-actual-position-value).

##### Input variables

1. "Encoder_x"; the position value (increments) provided by the assigned encoder is supplied as input value.
2. "Correction value of actual position value processing" ([p2513](SINAMICS%20Parameter%20G120.md#p251303-ci-lr-position-actual-value-preprocessing-corrective-value)); signal source to interconnect a correction value for the actual value evaluation. If you have activated the modulo correction in the mechanical system, you can also use the modulo correction as source.
3. "Correction value activation" ([p2512](SINAMICS%20Parameter%20G120.md#p251203-bi-lr-pos-actual-value-preprocessing-activate-corr-value-edge)); signal source for activation of the correction value.
4. "Position setting value" ([p2525](SINAMICS%20Parameter%20G120.md#p25250n-co-lr-encoder-adjustment-offset)); signal source for the setting value of the "Set actual position value" function.
5. "Set position value" ([p2514](SINAMICS%20Parameter%20G120.md#p251403-bi-lr-activate-position-actual-value-setting)); signal source for the activation of the "Set actual position value" function.
6. "Position offset" ([p2516](SINAMICS%20Parameter%20G120.md#p251603-ci-lr-position-offset)); signal source for the position offset. The position offset can be used to apply an offset to the actual position value. This enables backlash on reversal compensation to be implemented, for example. This must first be activated during the drive configuring.

##### Output variables

1. "Actual position value" ([r2521](SINAMICS%20Parameter%20G120.md#r252103-co-lr-position-actual-value)); shows the current actual position value.
2. "Current velocity" ([r2522](SINAMICS%20Parameter%20G120.md#r252203-co-lr-velocity-actual-value)); shows the actual velocity value.
3. "Actual position value valid" ([r2526](SINAMICS%20Parameter%20G120.md#r252609-cobo-lr-status-word)); shows whether the actual position value is valid (status word of the position controller).

##### G120 CU250S-2 function diagrams (FD)

- Position actual value preprocessing - 4010 -

##### Additional parameters

---

#### Position controller group

This section contains information on the following topics:

- [Setpoints / position controller](#setpoints-position-controller)
- [Position controller precontrol](#position-controller-precontrol)
- [Position controller precontrol balancing](#position-controller-precontrol-balancing)
- [Position controller](#position-controller-1)
- [Position control adaptation](#position-control-adaptation)
- [Position control limitation](#position-control-limitation)

##### Setpoints / position controller

###### Description

You parameterize the setpoints for the position controller of the technology controller here.

The interpolator (basic positioner function block or, for example, superimposed control / position setpoint of the position controller ([p2530](SINAMICS%20Parameter%20G120.md#p2530-ci-lr-position-setpoint)), velocity setpoint of the position controller ([p2531](SINAMICS%20Parameter%20G120.md#p2531-ci-lr-velocity-setpoint))) is coupled to the position controller using a fine interpolator that adapts a clock pulse scaling to the position control cycle clock. The clock ratio will be detected automatically.

The position setpoint filter is implemented as PT1 element; the balancing filter is implemented as lag element and PT1 element. The speed precontrol can be scaled and disabled using the value 0.

###### Position controller setpoint parameters

1. "Velocity setpoint" (p2531); signal source for the velocity setpoint of the position controller.
2. "Position setpoint" (p2530); signal source for the position setpoint of the position controller.
3. "Actual position value" ([p2532](SINAMICS%20Parameter%20G120.md#p2532-ci-lr-position-actual-value)); signal source for the actual position value of the position controller.
4. At "Time constant" ([p2533](SINAMICS%20Parameter%20G120.md#p25330n-lr-position-setpoint-filter-time-constant)), enter a value for the time constant of the position setpoint filter. This reduces the effective Kv factor (position loop gain).

###### Dialog boxes that can be called

- [Position controller precontrol](#position-controller-precontrol)
- [Position controller precontrol balancing](#position-controller-precontrol-balancing)

###### G120 CU250S-2 function diagrams (FD)

- Position controller - 4015 -

###### Additional parameters

---

##### Position controller precontrol

###### Description

With the precontrol, the setpoint in the position controller is weighted with a factor. This reduces the following error that occurs in the position control loop because of the "low-pass characteristics". However, if you set the factor too high, this results in overshoot at the velocity transitions in the position controller. Overshoot is reduced through low-pass filtering of the position setpoint in the [Position controller precontrol balancing](#position-controller-precontrol-balancing).

For further information, see also [Precontrol and gain](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#precontrol-and-gain).

- Enter a factor for the speed/velocity setpoint ([p2534](SINAMICS%20Parameter%20G120.md#p25340n-lr-speed-precontrol-factor)).

This factor also deactivates the precontrol when it is assigned the value 0. When the axis control loop has been optimally set as well as an equivalent time constant of the speed control loop precisely determined, the precontrol factor has the value 100%.

###### G120 CU250S-2 function diagrams (FD)

- Position controller - 4015 -

###### Additional parameters

---

##### Position controller precontrol balancing

###### Description

The precontrol balancing is implemented as delay element and PT1 element.

- At "Balancing filter (dead time)" ([p2535](SINAMICS%20Parameter%20G120.md#p25350n-lr-speed-precontrol-balancing-filter-dead-time-1)), enter a factor that is used as multiplier of the sampling time for internal correcting times for the position controller. The sampling time is 8 ms.
- At "Balancing filter (PT1)" ([p2536](SINAMICS%20Parameter%20G120.md#p25360n-lr-speed-precontrol-symmetrizing-filter-pt1)), enter the balancing time [0 ... 100 ms].

###### G120 CU250S-2 function diagrams (FD)

- Position controller - 4015 -

###### Additional parameters

---

##### Position controller

###### Description

The position controller is a PI controller. In this way, it is also possible to compensate even the smallest system deviations. The PI controller is mainly used for the velocity control, because an integrator component in a position controller causes an overshoot of the axis until the integrator component has decayed.

For further information, see also [Optimizing the position controller](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#optimizing-the-position-controller).

###### Parameters of the closed-loop position control

1. Enter a value for the P-gain ([p2538](SINAMICS%20Parameter%20G120.md#p25380n-lr-proportional-gain)). The P-gain specifies for which traversing speed which following error occurs (without precontrol).
2. If necessary, enter a value for the integral action time ([p2539](SINAMICS%20Parameter%20G120.md#p25390n-lr-integral-time)) (0 ms = P controller; > 0 ms = PI controller).

**Enable the position controller**

To enable the position controller, both enables must be set. The two enable parameters are linked with AND.

1. "1st position controller enable" ([p2549](SINAMICS%20Parameter%20G120.md#p2549-bi-lr-enable-1)); signal source for enable 1 of the position controller.
2. "2nd position controller enable" ([p2550](SINAMICS%20Parameter%20G120.md#p25500n-bi-lr-enable-2)); signal source for enable 2 of the position controller.

**Output variables**

1. "Speed precontrol" ([r2561](SINAMICS%20Parameter%20G120.md#r2561-co-lr-speed-precontrol-value)); shows the value for the velocity/speed precontrol.
2. "Torque precontrol" ([r2564](SINAMICS%20Parameter%20G120.md#r2564-co-lr-torque-precontrol-value)); shows the value for the torque precontrol. The value is obtained using the differentiation of the speed precontrol value over time.
3. "Speed setpoint" ([r2562](SINAMICS%20Parameter%20G120.md#r2562-co-lr-total-speed-setpoint)); shows the speed setpoint after the limitation.
4. "Speed" ([r2560](SINAMICS%20Parameter%20G120.md#r2560-co-lr-speed-setpoint)); shows the speed setpoint that results from the sum of the speed controller precontrol and the position controller output.

###### Dialog boxes that can be called

- [Position control adaptation](#position-control-adaptation)
- [Position control limitation](#position-control-limitation)

###### G120 CU250S-2 function diagrams (FD)

- Position controller - 4015 -

###### Additional parameters

---

##### Position control adaptation

###### Description

The P-gain can be modified using the [p2537](SINAMICS%20Parameter%20G120.md#p2537-ci-lr-position-controller-adaptation) connector input. This connector input has r0001=100% as default setting.

- "Adaptation" (p2537); signal source for the adaptation of the position controller.

###### G120 CU250S-2 function diagrams (FD)

- Position controller - 4015 -

###### Additional parameters

---

##### Position control limitation

###### Description

You use the limitation to enter a limit for the speed at the position controller output.

1. At "Position controller limit" ([p2540](SINAMICS%20Parameter%20G120.md#p2540-co-lr-position-controller-output-speed-limit)), enter a value for the speed limit.

   Or
2. "Position controller output limitation" ([p2541](SINAMICS%20Parameter%20G120.md#p2541-ci-lr-position-controller-output-speed-limit-signal-source)); signal source for the limitation of the position controller output. As default setting, the signal is interconnected to p2540. If you change this interconnection, the "Position controller limit" input field is deactivated and the value for the limitation must be supplied via the interconnected signal.

The"Position controller limit" input field can only be edited when p2541 is interconnected to p2540; the input field is only displayed in this case.

###### G120 CU250S-2 function diagrams (FD)

- Control word, block selection / MDI selection - 3640 -

###### Additional parameters

---

#### Monitoring

This section contains information on the following topics:

- [Position/standstill monitoring](#positionstandstill-monitoring)
- [Following error monitoring](#following-error-monitoring)
- [Output cams position controller](#output-cams-position-controller)

##### Position/standstill monitoring

###### Position monitoring

On the basis of a positioning window, the entry of the axis into the specified position at the end of a positioning motion is monitored. This requires the specification of a positioning window and a time interval.

For further information, see also [Standstill and positioning monitoring](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#standstill-and-positioning-monitoring).

1. At "Positioning window" ([p2544](SINAMICS%20Parameter%20G120.md#p2544-lr-positioning-window)), enter a value (value = 0, positioning monitoring is deactivated; value >= 1, positioning monitoring is active). The positioning monitoring defines the range at the target position in which the actual position value must lie after the positioning monitoring time has expired.
2. Enter a value at "Position monitoring time" ([p2545](SINAMICS%20Parameter%20G120.md#p2545-lr-positioning-monitoring-time)). The positioning monitoring time defines the range which after its expiration the following error must lie once within the positioning window.

**Standstill monitoring**

The standstill monitoring monitors the actual position of the axis after a traversing has completed. Two windows are specified for the standstill monitoring.

1. At "Standstill window" ([p2542](SINAMICS%20Parameter%20G120.md#p2542-lr-standstill-window)), enter a value (value = 0, standstill monitoring is deactivated; value >= 1, standstill monitoring is active). The standstill window defines the range at the target position in which the actual position value must lie after the standstill window monitoring time has expired.
2. Enter a value at "Standstill monitoring time" ([p2543](SINAMICS%20Parameter%20G120.md#p2543-lr-standstill-monitoring-time)). The standstill monitoring time defines the range which after its expiration the following error must lie within the standstill window. The standstill window is monitored cyclically.

**Position reached**

"Position reached" ([r2684](SINAMICS%20Parameter%20G120.md#r2684015-cobo-epos-status-word-2)); shows whether the position setpoint has been reached (yes/no).

###### G120 CU250S-2 function diagrams (FD)

- Standstill/positioning monitoring - 4020 -
- Dynamic following error monitoring, cam sequencer - 4025 -

###### Additional parameters

---

##### Following error monitoring

###### Description

The following error is the difference between a ramp-shaped, variable setpoint and the associated actual value. The more dynamic a control loop is, the smaller the resulting following error is. A maximum following error for the actual position value is often specified for the monitoring of position control loops. If this following error is violated, the position control aborts the current positioning operation and generates a fault message.

For further information, see also [Following error monitoring](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#following-error-monitoring).

1. At "Maximum dynamic following error" ([p2546](SINAMICS%20Parameter%20G120.md#p25460n-lr-dynamic-following-error-monitoring-tolerance)), enter the maximum deviation between the calculated and the measured actual position value before an error occurs (value = 0, dyn. following error monitoring is deactivated; value >= 1 dyn. following error monitoring is active).
2. "Travel to fixed stop active" ([p2552](SINAMICS%20Parameter%20G120.md#p2552-bi-lr-signal-travel-to-fixed-stop-active)); signal source for the "Travel to fixed stop active" message.

**Following error within tolerance**

"Following error within tolerance" ([r2684](SINAMICS%20Parameter%20G120.md#r2684015-cobo-epos-status-word-2)); shows whether a following error is active or not.

###### G120 CU250S-2 function diagrams (FD)

- Standstill/positioning monitoring - 4020 -
- Dynamic following error monitoring, cam sequencer - 4025 -

###### Additional parameters

---

##### Output cams position controller

###### Description

Using the position-dependent switching signals 1 and 2, cams can be simulated without any mechanical equipment (e.g. at inaccessible positions), dependent on the actual position value. The absolute cam switching positions are entered via parameter, and the associated cam switching signals are output as output signal. The reference is guaranteed only for a homed axis. See also [Cam sequencer](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#cam-sequencer).

1. At "Cam switching position 1" ([p2547](SINAMICS%20Parameter%20G120.md#p2547-lr-cam-switching-position-1)), enter a value for cam switching position 1.
2. At "Cam switching position 2" ([p2548](SINAMICS%20Parameter%20G120.md#p2548-lr-cam-switching-position-2)), enter a value for cam switching position 2.

   > **Note**
   >
   > For position values less than the cam switching position, the associated status bit supplies a "1 signal", otherwise a "0 signal".

**Cam switching signals**

1. "Cam switching signal 1" ([r2683](SINAMICS%20Parameter%20G120.md#r2683014-cobo-epos-status-word-1)); shows whether the actual position value is less than or equal to cam switching position 1.
2. "Cam switching signal 2" (r2683); shows whether the actual position value is less than or equal to cam switching position 2.

###### G120 CU250S-2 function diagrams (FD)

- Standstill/positioning monitoring - 4020 -
- Dynamic following error monitoring, cam sequencer - 4025 -

###### Additional parameters

---

### Technology controller

This section contains information on the following topics:

- [Technology controller - overview](#technology-controller---overview)
- [G120 CU250S-2 V technology controller motorized potentiometer](#g120-cu250s-2-v-technology-controller-motorized-potentiometer)
- [G120 CU250S-2 V MOP ramp-function generator of the technology controller](#g120-cu250s-2-v-mop-ramp-function-generator-of-the-technology-controller)
- [G120 CU250S-2 V technology controller fixed setpoints](#g120-cu250s-2-v-technology-controller-fixed-setpoints)
- [G120 CU250S-2 V technology controller PID control](#g120-cu250s-2-v-technology-controller-pid-control)
- [G120 CU250S-2 V technology controller PID controller](#g120-cu250s-2-v-technology-controller-pid-controller)
- [G120 CU250S-2 V technology controller ramp-up/ramp-down time](#g120-cu250s-2-v-technology-controller-ramp-upramp-down-time)
- [G120 CU250S-2 V output limitation of the technology controller](#g120-cu250s-2-v-output-limitation-of-the-technology-controller)

#### Technology controller - overview

##### SINAMICS G120 technology controller

Simple closed-loop control functions can be implemented with the technology controller, e.g.:

- Level control
- Temperature control
- Dancer roll position control
- Pressure control
- Flow control
- Simple closed-loop controls without higher-level controller
- Tension control

Further information can be found at [Setting up and opimize the controller](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-up-and-opimize-the-controller).

##### Properties of the technology controller

- [G120 CU250S-2 V technology controller motorized potentiometer](#g120-cu250s-2-v-technology-controller-motorized-potentiometer)
- [G120 CU250S-2 V technology controller fixed setpoints](#g120-cu250s-2-v-technology-controller-fixed-setpoints)
- [G120 CU250S-2 V technology controller PID control](#g120-cu250s-2-v-technology-controller-pid-control)
- [G120 CU250S-2 V technology controller ramp-up/ramp-down time](#g120-cu250s-2-v-technology-controller-ramp-upramp-down-time)
- [G120 CU250S-2 V output limitation of the technology controller](#g120-cu250s-2-v-output-limitation-of-the-technology-controller)

#### G120 CU250S-2 V technology controller motorized potentiometer

##### Parameterizing the technology controller motorized potentiometer

The motorized potentiometer enables a setpoint to be specified for the technology controller. The setpoint is specified via a ramp-function generator.

For more detailed information, see also [Setting up and opimize the controller](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-up-and-opimize-the-controller).

##### Setpoint higher/lower

1. "Setpoint higher" ([p2235](SINAMICS%20Parameter%20G120.md#p22350n-bi-technology-controller-motorized-potentiometer-raise-setpoint)); signal source to increase the setpoint.
2. "Setpoint lower" ([p2236](SINAMICS%20Parameter%20G120.md#p22360n-bi-technology-controller-motorized-potentiometer-lower-setpoint)); signal source to decrease the setpoint.

##### Maximum value / minimum value

- To specify limit values for the speed setpoint in manual mode, enter a maximum value ([p2237](SINAMICS%20Parameter%20G120.md#p22370n-technology-controller-motorized-potentiometer-maximum-value)) and a minimum value ([p2238](SINAMICS%20Parameter%20G120.md#p22380n-technology-controller-motorized-potentiometer-minimum-value)).

  The "Maximum speed" or "Minimum speed" is not overshot or undershot when using the motorized potentiometer.

##### Saving the setpoint

1. To save the setpoint after switching the motor off, select "Yes" in the "Saving active" drop-down list.
2. To save the setpoint retentively, select "Yes" in the "Saving to NVRAM active" the drop-down list.

##### Function diagrams (FD)

- Motorized potentiometer - 7954 -

##### Additional parameters

---

#### G120 CU250S-2 V MOP ramp-function generator of the technology controller

##### Parameterizing the MOP ramp-function generator of the technology controller

The ramp-function generator ramps the setpoint up and down without acceleration jumps. The ramp-function generator is parameterized via the ramp-up time and ramp-down time parameters. The times refer to the time needed to reach the reference setpoint (0% or 100%) in the specified time.

##### Initial rounding active ([p2230](SINAMICS%20Parameter%20G120.md#p22300n-technology-controller-motorized-potentiometer-configuration))

- To interconnect a fixed specified rounding, select "Yes" in the "Initial rounding active" drop-down list.

  The set ramp-up or ramp-down time can be exceeded with the initial rounding.

##### Ramp-up time and ramp-down time

The ramp-function generator is parameterized via the "Ramp-up and ramp-down time" parameters, whereby these refer to the speed limit n max.

1. Enter a value for the ramp-up time ([p2247](SINAMICS%20Parameter%20G120.md#p22470n-technology-controller-motorized-potentiometer-ramp-up-time)).
2. Enter a value for the ramp-down time ([p2248](SINAMICS%20Parameter%20G120.md#p22480n-technology-controller-motorized-potentiometer-ramp-down-time)).

##### Start value

- Enter a start value ([p2240](SINAMICS%20Parameter%20G120.md#p22400n-technology-controller-motorized-potentiometer-starting-value)) for the motorized potentiometer. This value takes effect when the drive is turned on.

##### Function diagrams (FD)

- Motorized potentiometer - 7954 -

##### Additional parameters

---

#### G120 CU250S-2 V technology controller fixed setpoints

##### Parameterizing the fixed setpoints of the technology controller

Parameterize the fixed setpoints of the technology controller. Fixed setpoints are speed setpoints freely stored by the user.

##### Fixed setpoint selection

- Select whether the fixed setpoint selection is to be performed via "Binary-coded fixed setpoint selection" or via "Fixed setpoint selection with adder"([p2216](SINAMICS%20Parameter%20G120.md#p22160n-technology-controller-fixed-value-selection-method)).

  - With "Binary-coded fixed setpoint selection", select the fixed setpoint via the four selection bits.
  - With "Fixed setpoint selection with adder", also select the fixed setpoint via the selection bits. If several fixed setpoints are active, the setpoints will be added.

##### Fixed setpoint activated

1. "Fixed setpoint activated" ([r2225](SINAMICS%20Parameter%20G120.md#r22250-cobo-technology-controller-fixed-value-selection-status-word)); signal source for display of the status of the fixed setpoints (0/1 = off/on).
2. "Fixed setpoint 1 ... 4" ([p2220](SINAMICS%20Parameter%20G120.md#p22200n-bi-technology-controller-fixed-value-selection-bit-0)...[p2223](SINAMICS%20Parameter%20G120.md#p22230n-bi-technology-controller-fixed-value-selection-bit-3)); signal sources for setting the selection bits of the speed setpoint.

##### Fixed setpoint 1 ... 4 "Fixed setpoint selection with adder"

1. Enter fixed speed setpoints in the "Fixed setpoint 1...4" ([p2201](SINAMICS%20Parameter%20G120.md#p22010n-co-technology-controller-fixed-value-1)) fields.
2. The effective speed setpoint then results from the addition of the individual speed setpoints according to the selection bits.

**Fixed setpoint active**

"Fixed setpoint active" (r2225); signal source to display the active fixed speed setpoint.

##### Fixed setpoint interconnection "Binary-coded fixed setpoint selection"

- Enter fixed speed setpoints in the "Fixed value 1...15" (p2201) fields.

You then interconnect these values via the connected signal sources.

##### Function diagrams (FD)

- Fixed values, binary selection (p2216 = 2) - 7950 -
- Fixed values, direct selection (p2216 = 1) - 7951 -

##### Additional parameters

---

#### G120 CU250S-2 V technology controller PID control

##### Parameterizing the PID control

SINAMICS G120 contains an integrated technology controller (PID controller) for simple closed-loop control functions such as level control or temperature control. The P, I and D component can each be set and switched-off separately. Switching off is performed by entering a "0" in the appropriate parameter ([p2200](SINAMICS%20Parameter%20G120.md#p22000n-bi-technology-controller-enable)).

For more detailed information, see also [Setting up and opimize the controller](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#setting-up-and-opimize-the-controller).

##### Parameterizing the technology controller

1. In order to use the technology controller as main setpoint, select "Technology controller as main speed setpoint" ([p2251](SINAMICS%20Parameter%20G120.md#p2251-technology-controller-mode-2)) in the drop-down list.
2. In order to use the technology controller as additional setpoint, select "Technology controller as additional speed setpoint" in the drop-down list.

   The technology controller output is then interconnected to the setpoint as additional setpoint in the "Ramp-function generator".
3. "Technology controller enable" (p2200); signal source for activating the PID controller.
4. If you have selected "Technology controller as main speed setpoint", enter a value between 0...200% as start value for the PID controller.

##### Main and additional setpoint

1. "Setpoint source" ([p2253](SINAMICS%20Parameter%20G120.md#p22530n-ci-technology-controller-setpoint-1)); signal source for interconnecting the setpoint source. The PID motorized potentiometer, fixed setpoints, analog inputs or the fieldbus interface can be used as the setpoint source.
2. To scale the setpoints, enter a value between 0...100% at "Scaling" ([p2255](SINAMICS%20Parameter%20G120.md#p2255-technology-controller-setpoint-1-scaling)).
3. "Additional setpoint" ([p2254](SINAMICS%20Parameter%20G120.md#p22540n-ci-technology-controller-setpoint-2)); signal source to interconnect the additional setpoint. The additional setpoint is added to the main setpoint.
4. To scale the additional setpoint, enter a value between 0...100% at "Scaling" ([p2256](SINAMICS%20Parameter%20G120.md#p2256-technology-controller-setpoint-2-scaling)).

##### Parameterizing the actual value source

1. "Actual value source" ([p2264](SINAMICS%20Parameter%20G120.md#p22640n-ci-technology-controller-actual-value)); signal source to interconnect the actual value.
2. In order to apply a smoothing filter to the actual value, enter a value between 0...60 s at "Smoothing" ([p2265](SINAMICS%20Parameter%20G120.md#p2265-technology-controller-actual-value-filter-time-constant)).
3. To limit the actual value, enter a value for the upper limit ([p2267](SINAMICS%20Parameter%20G120.md#p2267-technology-controller-upper-limit-actual-value)) and a value for the lower limit ([p2268](SINAMICS%20Parameter%20G120.md#p2268-technology-controller-lower-limit-actual-value)).
4. To increase to the actual value, enter a value between 0...500% at "Scaling" ([p2269](SINAMICS%20Parameter%20G120.md#p2269-technology-controller-gain-actual-value)).
5. At "Function" ([p2270](SINAMICS%20Parameter%20G120.md#p2270-technology-controller-actual-value-function)), select an arithmetic function that is to be used on the actual value.

##### Parameterizing the output of the technology controller

1. "Technology controller output scaling" ([p2296](SINAMICS%20Parameter%20G120.md#p22960n-ci-technology-controller-output-scaling)); signal source for scaling the technology output. Parameter [p2295](SINAMICS%20Parameter%20G120.md#p2295-co-technology-controller-output-scaling) is interconnected as default setting. If you want to use a different value for the scaling, change the interconnection.
2. To scale the technology controller directly, enter a value between -100...100% at "Scaling" (p2295).
3. "Technology controller output" ([r2294](SINAMICS%20Parameter%20G120.md#r2294-co-technology-controller-output-signal)); signal source to display the output signal of the technology controller.

##### Function diagrams (FD)

- Closed-loop control - 7958 -

##### Additional parameters

---

#### G120 CU250S-2 V technology controller PID controller

##### Parameterizing the PID controller

Parameterize the technology controller either as a P, I, PI or PID controller.

> **Note**
>
> The value 0 deactivates the corresponding controller component.

##### Parameters of the PID controller

To parameterize the PID controller of the technology controller, proceed as follows:

1. Select one of the following options in the "Technology controller type" ([p2263](SINAMICS%20Parameter%20G120.md#p2263-technology-controller-type)) drop-down list:

   - [0] D component in the actual value signal; the differential component of the controller is used on the actual value signal with this setting. Use the setting for example, if the actual value signal contains large deflections that have to be cleaned up quickly in the setpoint via the D component in the controller.
   - [1] D component in the fault signal (displays the "differentiation time"); the differential component of the controller is used on the setpoint / actual value difference with this setting.
2. Enter a value for the "P gain factor" ([p2248](SINAMICS%20Parameter%20G120.md#p22480n-technology-controller-motorized-potentiometer-ramp-down-time)).
3. Enter a value for the "Integration time" ([p2285](SINAMICS%20Parameter%20G120.md#p2285-technology-controller-integral-time)).
4. Enter a value for the "Differentiation time" ([p2274](SINAMICS%20Parameter%20G120.md#p2274-technology-controller-differentiation-time-constant)).
5. "Technology controller precontrol signal" ([p2289](SINAMICS%20Parameter%20G120.md#p22890n-ci-technology-controller-precontrol-signal)); signal source to interconnect the precontrol signal of the technology controller.

##### Function diagrams (FD)

- Closed-loop control - 7958 -

##### Additional parameters

---

#### G120 CU250S-2 V technology controller ramp-up/ramp-down time

##### Parameterizing the ramp-up/ramp-down time

Ramp-up and ramp-down times are used to prevent sudden setpoint jumps and therefore abrupt acceleration. A change at the PID controller input is passed on to the output via a defined ramp.

##### Ramp-up time and ramp-down time

To parameterize the ramp-up time or ramp-down time for the PID controller, proceed as follows:

1. Enter a value for the ramp-up time ([p2257](SINAMICS%20Parameter%20G120.md#p2257-technology-controller-ramp-up-time)).
2. Enter a value for the ramp-down time ([p2258](SINAMICS%20Parameter%20G120.md#p2258-technology-controller-ramp-down-time)).

##### Function diagrams (FD)

- Closed-loop control - 7958 -

##### Additional parameters

---

#### G120 CU250S-2 V output limitation of the technology controller

##### Parameterizing the output limits

Parameterize the maximum and minimum limits for the technology controller.

> **Note**
>
> The limits are entered in [%].

For some applications, the PID output variable must be limited to defined values. This can be achieved using fixed limits. To prevent large jumps of the PID controller output when the device is switched on, these PID output limits will be ramped-up via the ramp time from 0 to the appropriate values (upper limit for the PID output or lower limit for the PID output ). As soon as the limits are reached, the dynamic response of the PID controller is no longer limited by this ramp-up/ramp-down time.

##### Parameters of the output limits

To set the output limits of the PID controller, proceed as follows:

1. Maximum limit ([p2297](SINAMICS%20Parameter%20G120.md#p22970n-ci-technology-controller-maximum-limit-signal-source-1)); signal source for setting the maximum limit.
2. Limit offset ([p2299](SINAMICS%20Parameter%20G120.md#p22990n-ci-technology-controller-limit-offset-1)); signal source to interconnect an offset for the output limits.
3. Minimum limit ([p2298](SINAMICS%20Parameter%20G120.md#p22980n-ci-technology-controller-minimum-limit-signal-source-1)); signal source for setting the minimum limit.
4. Enter a value for the "Ramp-up/ramp-down time" ([p2293](SINAMICS%20Parameter%20G120.md#p2293-technology-controller-ramp-upramp-down-time)).

##### Function diagrams (FD)

- Closed-loop control - 7958 -

##### Additional parameters

---

### Free function blocks

This section contains information on the following topics:

- [Logical functions](#logical-functions)
- [Arithmetic functions](#arithmetic-functions)
- [Time functions](#time-functions)
- [Memory functions](#memory-functions)
- [Switch functions](#switch-functions)
- [Control functions](#control-functions)
- [Complex functions](#complex-functions)

#### Logical functions

##### Logical functions of the free function blocks

Startdrive has the following logical free function blocks:

- [AND](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#and)
- [OR](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#or)
- [XOR (exclusive OR)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#xor-exclusive-or)
- [NOT (inverter)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#not-inverter)
- [NCM numeric comparator](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#ncm-numeric-comparator)

For general information about the free function blocks, see [Logical and arithmetic functions using function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#logical-and-arithmetic-functions-using-function-blocks).

##### General parameters

You can enter the runtime group and the run sequence via the following general parameters:

1. Select the sequence in which the function blocks are to be calculated within the runtime group at "Run sequence". A function block with a low number is calculated before a function block with a high number.
2. From the drop-down list, select a runtime group which you want to assign to the function block.

##### AND block

The block links the binary variables at the inputs to a logic AND. The condition is "true" when all the connected input signals of a block are "true" (1).

**AND 0**

- [p20030](SINAMICS%20Parameter%20G120.md#p2003003-bi-and-0-inputs)[0]...p20030[3]; input signals for logic AND 0
- [r20031](SINAMICS%20Parameter%20G120.md#r20031-bo-and-0-output-q); output signal for logic AND 0

**AND 1**

- [p20034](SINAMICS%20Parameter%20G120.md#p2003403-bi-and-1-inputs)[0]...p20034[3]; input signals for logic AND 1
- [r20035](SINAMICS%20Parameter%20G120.md#r20035-bo-and-1-output-q); output signal for logic AND 1

**AND 2**

- [p20038](SINAMICS%20Parameter%20G120.md#p2003803-bi-and-2-inputs)[0]...p20030[3]; input signals for logic AND 2
- [r20039](SINAMICS%20Parameter%20G120.md#r20039-bo-and-2-output-q); output signal for logic AND 2

**AND 3**

- [p20042](SINAMICS%20Parameter%20G120.md#p2004203-bi-and-3-inputs)[0]...p20030[3]; input signals for logic AND 3
- [r20043](SINAMICS%20Parameter%20G120.md#r20043-bo-and-3-output-q); output signal for logic AND 3

##### OR block

The block links the binary variables at the inputs to a logic OR. The condition is "true" when one of the connected input signals of a block is "true" (1).

**OR 0**

- [p20046](SINAMICS%20Parameter%20G120.md#p2004603-bi-or-0-inputs)[0]...p20046[3]; input signals for logic OR 0
- [r20047](SINAMICS%20Parameter%20G120.md#r20047-bo-or-0-output-q); output signal for logic OR 0

**OR 1**

- [p20050](SINAMICS%20Parameter%20G120.md#p2005003-bi-or-1-inputs)[0]...p20050[3]; input signals for logic OR 1
- [r20051](SINAMICS%20Parameter%20G120.md#r20051-bo-or-1-output-q); output signal for logic OR 1

**OR 2**

- [p20054](SINAMICS%20Parameter%20G120.md#p2005403-bi-or-2-inputs)[0]...p20030[3]; input signals for logic OR 2
- [r20055](SINAMICS%20Parameter%20G120.md#r20055-bo-or-2-output-q); output signal for logic OR 2

**OR 3**

- [p20058](SINAMICS%20Parameter%20G120.md#p2005803-bi-or-3-inputs)[0]...p20058[3]; input signals for logic OR 3
- [r20059](SINAMICS%20Parameter%20G120.md#r20059-bo-or-3-output-q); output signal for logic OR 3

##### XOR block

The block links the binary variables at the inputs to an exclusive XOR. The condition is "true" when an odd number of the connected input signals of a block is "true" (1).

**XOR 0**

- [p20062](SINAMICS%20Parameter%20G120.md#p2006203-bi-xor-0-inputs)[0]...p20062[3]; input signals for logic XOR 0
- [r20063](SINAMICS%20Parameter%20G120.md#r20063-bo-xor-0-output-q); output signal for logic XOR 0

**XOR 1**

- [p20066](SINAMICS%20Parameter%20G120.md#p2006603-bi-xor-1-inputs)[0]...p20066[3]; input signals for logic XOR 1
- [r20067](SINAMICS%20Parameter%20G120.md#r20067-bo-xor-1-output-q); output signal for logic XOR 1

**XOR 2**

- [p20070](SINAMICS%20Parameter%20G120.md#p2007003-bi-xor-2-inputs)[0]...p20070[3]; input signals for logic XOR 2
- [r20071](SINAMICS%20Parameter%20G120.md#r20071-bo-xor-2-output-q); output signal for logic XOR 2

**XOR 3**

- [p20074](SINAMICS%20Parameter%20G120.md#p2007403-bi-xor-3-inputs)[0]...p20074[3]; input signals for logic XOR 3
- [r20075](SINAMICS%20Parameter%20G120.md#r20075-bo-xor-3-output-q); output signal for logic XOR 3

##### NOT block

The block inverts the binary variables at the input and transfers the result to the output.

**NOT 0**

- [p20078](SINAMICS%20Parameter%20G120.md#p20078-bi-not-0-input-i); input signal for logic NOT 0
- [r20079](SINAMICS%20Parameter%20G120.md#r20079-bo-not-0-inverted-output); output signal for logic NOT 0

**NOT 1**

- [p20082](SINAMICS%20Parameter%20G120.md#p20082-bi-not-1-input-i); input signal for logic NOT 1
- [r20083](SINAMICS%20Parameter%20G120.md#r20083-bo-not-1-inverted-output); output signal for logic NOT 1

**NOT 2**

- [p20086](SINAMICS%20Parameter%20G120.md#p20086-bi-not-2-input-i); input signal for logic NOT 2
- [r20087](SINAMICS%20Parameter%20G120.md#r20087-bo-not-2-inverted-output); output signal for logic NOT 2

**NOT 3**

- [p20090](SINAMICS%20Parameter%20G120.md#p20090-bi-not-3-input-i); input signal for logic NOT 3
- [r20091](SINAMICS%20Parameter%20G120.md#r20091-bo-not-3-inverted-output); output signal for logic NOT 3

**NOT 4**

- [p20300](SINAMICS%20Parameter%20G120.md#p20300-bi-not-4-input-i); input signal for logic NOT 4
- [r20301](SINAMICS%20Parameter%20G120.md#r20301-bo-not-4-inverted-output); output signal for logic NOT 4

**NOT 5**

- [p20304](SINAMICS%20Parameter%20G120.md#p20304-bi-not-5-input-i); input signal for logic NOT 5
- [r20305](SINAMICS%20Parameter%20G120.md#r20305-bo-not-5-inverted-output); output signal for logic NOT 5

##### NCM - numeric comparison

The block compares two numeric input values of the REAL type. Depending on the result, one of the three outputs is set.

**Numeric comparison 0**

- [p20312](SINAMICS%20Parameter%20G120.md#p2031201-ci-ncm-0-inputs)[0]...p20312[1]; input values that are to be compared.
- [r20313](SINAMICS%20Parameter%20G120.md#r20313-bo-ncm-0-output-qu); output signal if a > b
- [r20314](SINAMICS%20Parameter%20G120.md#r20314-bo-ncm-0-output-qe); output signal if a = b
- [r20315](SINAMICS%20Parameter%20G120.md#r20315-bo-ncm-0-output-ql); output signal if a < b

**Numeric comparison 1**

- [p20318](SINAMICS%20Parameter%20G120.md#p2031801-ci-ncm-1-inputs)[0]...p20318[1]; input values that are to be compared.
- [r20319](SINAMICS%20Parameter%20G120.md#r20319-bo-ncm-1-output-qu); output signal if a > b
- [r20320](SINAMICS%20Parameter%20G120.md#r20320-bo-ncm-1-output-qe); output signal if a = b
- [r20321](SINAMICS%20Parameter%20G120.md#r20321-bo-ncm-1-output-ql); output signal if a < b

##### Function diagrams (FD)

- AND 0 … 3 - 7210 -
- OR 0 … 3 - 7212 -
- XOR 0 … 3 - 7214 -
- NOT 0 … 5 - 7216 -
- NCM 0 … 1 - 7225 -

##### Additional parameters

---

#### Arithmetic functions

##### Arithmetic functions of the free function blocks

The free function blocks of Startdrive have the following arithmetic functions:

- [ADD (adder)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#add-adder)
- [SUB (subtracter)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#sub-subtracter)
- [MUL (multiplier)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#mul-multiplier)
- [DIV (divider)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#div-divider)
- [AVA (absolute value generator with sign evaluation)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#ava-absolute-value-generator-with-sign-evaluation)
- [Polyline](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#polyline)

For general information about the free function blocks, see [Logical and arithmetic functions using function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#logical-and-arithmetic-functions-using-function-blocks).

##### General parameters

You can enter the runtime group and the run sequence via the following general parameters:

1. Select the sequence in which the function blocks are to be calculated within the runtime group at "Run sequence". A function block with a low number is calculated before a function block with a high number.
2. From the drop-down list, select a runtime group which you want to assign to the function block.

##### ADD (adder)

The block adds (taking into account the sign) the values entered at the X inputs. The sum is output at output Y.

Algorithm:

Y = X1 + X2 + X3

**ADD 0**

- [p20094](SINAMICS%20Parameter%20G120.md#p2009403-ci-add-0-inputs)[0]...p20094[3]; input signals for the summands of ADD 0
- [r20095](SINAMICS%20Parameter%20G120.md#r20095-co-add-0-output-y); output signal (sum) of ADD 0

**ADD 1**

- [p20098](SINAMICS%20Parameter%20G120.md#p2009803-ci-add-1-inputs)[0]...p20098[3]; input signals for the summands of ADD 1
- [r20099](SINAMICS%20Parameter%20G120.md#r20099-co-add-1-output-y); output signal (sum) of ADD 1

**ADD 2**

- [p20308](SINAMICS%20Parameter%20G120.md#p2030803-ci-add-2-inputs)[0]...p20308[3]; input signals for the summands of ADD 2
- [r20309](SINAMICS%20Parameter%20G120.md#r20309-co-add-2-output-y); output signal (sum) of ADD 2

##### SUB (subtracter)

This function block subtracts (in accordance with the sign) the value entered at input X1 from the value entered at input X0.

The difference is output at output Y.

**SUB 0**

- [p20102](SINAMICS%20Parameter%20G120.md#p2010201-ci-sub-0-inputs)[0]; input signal for the minuend of SUB 0
- p20102[1]; input signal for the subtrahend of SUB 0
- [r20103](SINAMICS%20Parameter%20G120.md#r20103-co-sub-0-difference-y); output signal (difference) of SUB 0

**SUB 1**

- [p20106](SINAMICS%20Parameter%20G120.md#p2010601-ci-sub-1-inputs)[0]; input signal for the minuend of SUB 1
- p20106[1]; input signal for the subtrahend of SUB 1
- [r20107](SINAMICS%20Parameter%20G120.md#r20107-co-sub-1-difference-y); output signal (difference) of SUB 1

##### MULT (multiplier)

The block multiplies (taking into account the sign) the values entered at the generic inputs X 1 to 4. The result is output at output Y.

**MULT 0**

- [p20110](SINAMICS%20Parameter%20G120.md#p2011003-ci-mul-0-inputs)[0]...p20110[3]; input signal for the factors X1 to X4 of MULT 0
- [r20111](SINAMICS%20Parameter%20G120.md#r20111-co-mul-0-product-y); output signal of the product of MULT 0.

**MULT 1**

- [p20114](SINAMICS%20Parameter%20G120.md#p2011403-ci-mul-1-inputs)[0]...p20114[3]; input signal for the factors X1 to X4 of MULT 1
- [r20115](SINAMICS%20Parameter%20G120.md#r20115-co-mul-1-product-y); output signal of the product of MULT 1.

##### DIV (divider)

The block divides the value input at connection X1 by the value input at connection X2. The result is output at outputs Y, YIN, and MOD.

**DIV 0**

- [p20118](SINAMICS%20Parameter%20G120.md#p2011801-ci-div-0-inputs)[0]; input signal for the dividend X0 of DIV 0
- p20118[1]; input signal for the divisor X1 of DIV 0
- [r20119](SINAMICS%20Parameter%20G120.md#r2011902-co-div-0-quotient)[0]; output signal for the quotient Y of DIV 0
- r20119[1]; output signal for the integer quotient YIN of DIV 0
- r20119[2]; output signal for the remainder MOD of DIV 0
- r20119[0]; output signal for the case "Division by ZERO" of DIV 0

**DIV 1**

- [p20123](SINAMICS%20Parameter%20G120.md#p2012301-ci-div-1-inputs)[0]; input signal for the dividend X0 of DIV 1
- p20123[1]; input signal for the divisor X1 of DIV 1
- [r20124](SINAMICS%20Parameter%20G120.md#r2012402-co-div-1-quotient)[0]; output signal for the quotient Y of DIV 1
- r20124[1]; output signal for the integer quotient YIN of DIV 1
- r20124[2]; output signal for the remainder MOD of DIV 1
- r20124[0]; output signal for the case "Division by ZERO" of DIV 1

##### AVA

The block generates the absolute value of the value present at input X (input variable). The result is output at output Y.

Y = |X|

If the input variable is negative, digital output SN is set to 1.

**AVA**

- [p20128](SINAMICS%20Parameter%20G120.md#p20128-ci-ava-0-input-x); input signal for input variable X
- [r20129](SINAMICS%20Parameter%20G120.md#r20129-co-ava-0-output-y); output signal for output variable Y
- [r20130](SINAMICS%20Parameter%20G120.md#r20130-bo-ava-0-input-negative-sn); output signal if the input signal had a negative sign

**AVA**

- [p20133](SINAMICS%20Parameter%20G120.md#p20133-ci-ava-1-input-x); input signal for input variable X
- [r20134](SINAMICS%20Parameter%20G120.md#r20134-co-ava-1-output-y); output signal for output variable Y
- [r20135](SINAMICS%20Parameter%20G120.md#r20135-bo-ava-1-input-negative-sn); output signal if the input signal had a negative sign

##### Polyline

The block adapts output variable Y arbitrarily to input variable X by means of up to 20 breakpoints in 4 quadrants.

Interpolation is carried out linearly between the inflection points. Outside of A1 and A20, the characteristic curve runs horizontally.

**Polyline 0**

- [p20372](SINAMICS%20Parameter%20G120.md#p20372-ci-pli-0-input-x); input signal for input variable X of polyline 0
- [r20373](SINAMICS%20Parameter%20G120.md#r20373-co-pli-0-output-y); output signal for output variable Y of polyline 0
- Input value 0 to input value 20; input values for the breakpoints of the four quadrants
- Output value 0 to output value 20; output values for the breakpoints of the four quadrants

**Polyline 1**

- [p20378](SINAMICS%20Parameter%20G120.md#p20378-ci-pli-1-input-x); input signal for input variable X of polyline 1
- [r20379](SINAMICS%20Parameter%20G120.md#r20379-co-pli-1-output-y); output signal for output variable Y of polyline 1
- Input value 0 to input value 20; input values for the breakpoints of the four quadrants
- Output value 0 to output value 20; output values for the breakpoints of the four quadrants

##### Function diagrams (FD)

- ADD 0 … 2, SUB 0 … 1 - 7220 -
- MUL 0 … 1, DIV 0 … 1 - 7222 -
- AVA 0 … 1 - 7224 -
- PLI 0 … 1 - 7226 -

##### Additional parameters

---

#### Time functions

##### Time functions of the free function blocks

The free function blocks of Startdrive have the following time functions:

- [MFP (pulse generator)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#mfp-pulse-generator)
- [PCL (pulse shortener)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#pcl-pulse-shortener)
- [PST (pulse stretcher)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#pst-pulse-stretcher)
- [PDE (ON delay)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#pde-on-delay)
- [PDF (OFF delay)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#pdf-off-delay)

For general information about the free function blocks, see [Logical and arithmetic functions using function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#logical-and-arithmetic-functions-using-function-blocks).

##### General parameters

You can enter the runtime group and the run sequence via the following general parameters:

1. Select the sequence in which the function blocks are to be calculated within the runtime group at "Run sequence". A function block with a low number is calculated before a function block with a high number.
2. From the drop-down list, select a runtime group which you want to assign to the function block.

##### Pulse generator

The pulse generator is used as timer for generating a pulse with a fixed duration. It can be used as a pulse-reduction monoflop or as a pulse-stretching monoflop.

The rising edge of a pulse at input I sets output Q to 1 for the pulse duration T.

**Pulse generator 0**

- [p20138](SINAMICS%20Parameter%20G120.md#p20138-bi-mfp-0-input-pulse-i); input pulse I of MFP 0
- [p20139](SINAMICS%20Parameter%20G120.md#p20139-mfp-0-pulse-duration-in-ms); input field for the pulse duration
- [r20140](SINAMICS%20Parameter%20G120.md#r20140-bo-mfp-0-output-q); output signal for the output of MFP 0

**Pulse generator 1**

- [p20143](SINAMICS%20Parameter%20G120.md#p20143-bi-mfp-1-input-pulse-i); input pulse I of MFP 1
- [p20144](SINAMICS%20Parameter%20G120.md#p20144-mfp-1-pulse-duration-in-ms); input field for the pulse duration
- [r20145](SINAMICS%20Parameter%20G120.md#r20145-bo-mfp-1-output-q); output signal for the output of MFP 1

**Pulse generator 2**

- [p20354](SINAMICS%20Parameter%20G120.md#p20354-bi-mfp-2-input-pulse-i); input pulse I of MFP 2
- [p20355](SINAMICS%20Parameter%20G120.md#p20355-mfp-2-pulse-duration-in-ms); input field for the pulse duration
- [r20356](SINAMICS%20Parameter%20G120.md#r20356-bo-mfp-2-output-q); output signal for the output of MFP 2

**Pulse generator 3**

- [p20359](SINAMICS%20Parameter%20G120.md#p20359-bi-mfp-3-input-pulse-i); input pulse I of MFP 3
- [p20360](SINAMICS%20Parameter%20G120.md#p20360-mfp-3-pulse-duration-in-ms); input field for the pulse duration
- [r20361](SINAMICS%20Parameter%20G120.md#r20361-bo-mfp-3-output-q); output signal for the output of MFP 3

##### PST - pulse stretching

The pulse-stretching block is used for generating a pulse with a minimum duration and with an additional reset input.

The rising edge of a pulse at input I sets output Q to 1. Output Q does not return to 0 until input pulse I is 0 and pulse duration T has expired. Output Q can be set to zero at any time via reset input R with R = 1.

**Pulse stretching 0**

- [p20178](SINAMICS%20Parameter%20G120.md#p2017801-bi-pst-0-inputs)[0]; input pulse for PST 0
- p20178[1]; reset input for PST 0
- [p20179](SINAMICS%20Parameter%20G120.md#p20179-pst-0-pulse-duration-in-ms); input field for the pulse duration
- [r20180](SINAMICS%20Parameter%20G120.md#r20180-bo-pst-0-output-q); output signal for the output of PST 0

**Pulse stretching 1**

- [p20183](SINAMICS%20Parameter%20G120.md#p2018301-bi-pst-1-inputs)[0]; input pulse for PST 1
- p20183[1]; reset input for PST 1
- [p20184](SINAMICS%20Parameter%20G120.md#p20184-pst-1-pulse-duration-in-ms); input field for the pulse duration
- [r20185](SINAMICS%20Parameter%20G120.md#r20185-bo-pst-1-output-q); output signal for the output of PST 1

##### PCL - pulse reduction

The pulse-reduction block is used to limit the pulse duration.

The rising edge of a pulse at input I sets output Q to 1. Output Q becomes 0 when input I becomes 0 or pulse duration T has expired. With T=0, a pulse duration of one cycle applies.

**Pulse reduction 0**

- [p20148](SINAMICS%20Parameter%20G120.md#p20148-bi-pcl-0-input-pulse-i); input pulse for PCL 0
- [p20149](SINAMICS%20Parameter%20G120.md#p20149-pcl-0-pulse-duration-in-ms); input field for the pulse duration
- [r20150](SINAMICS%20Parameter%20G120.md#r20150-bo-pcl-0-output-q); output signal for the output of PCL 0

**Pulse reduction 1**

- [p20153](SINAMICS%20Parameter%20G120.md#p20153-bi-pcl-1-input-pulse-i); input pulse for PCL 1
- [p20154](SINAMICS%20Parameter%20G120.md#p20154-pcl-1-pulse-duration-in-ms); input field for the pulse duration
- [r20155](SINAMICS%20Parameter%20G120.md#r20155-bo-pcl-1-output-q); output signal for the output of PCL 1

##### PDE - ON delay

The ON-delay block contains a timer with ON delay of the BOOL type.

The pulse delay time at the input T is taken over with the rising edge at input I. After this time has elapsed, output Q is set to 1. Output Q becomes 0 when I becomes 0.

**ON delay 0**

- [p20158](SINAMICS%20Parameter%20G120.md#p20158-bi-pde-0-input-pulse-i); input pulse for PDE 0
- [p20159](SINAMICS%20Parameter%20G120.md#p20159-pde-0-pulse-delay-time-in-ms); input field for the pulse delay time
- [r20160](SINAMICS%20Parameter%20G120.md#r20160-bo-pde-0-output-q); output signal for the output of PDE 0

**ON delay 1**

- [p20163](SINAMICS%20Parameter%20G120.md#p20163-bi-pde-1-input-pulse-i); input pulse for PDE 1
- [p20164](SINAMICS%20Parameter%20G120.md#p20164-pde-1-pulse-delay-time-in-ms); input field for the pulse delay time
- [r20165](SINAMICS%20Parameter%20G120.md#r20165-bo-pde-1-output-q); output signal for the output of PDE 1

**ON delay 2**

- [p20334](SINAMICS%20Parameter%20G120.md#p20334-bi-pde-2-input-pulse-i); input pulse for PDE 2
- [p20335](SINAMICS%20Parameter%20G120.md#p20335-pde-2-pulse-delay-time-in-ms); input field for the pulse delay time
- [r20336](SINAMICS%20Parameter%20G120.md#r20336-bo-pde-2-output-q); output signal for the output of PDE 2

**ON delay 3**

- [p20339](SINAMICS%20Parameter%20G120.md#p20339-bi-pde-3-input-pulse-i); input pulse for PDE 3
- [p20340](SINAMICS%20Parameter%20G120.md#p20340-pde-3-pulse-delay-time-in-ms); input field for the pulse delay time
- [r20341](SINAMICS%20Parameter%20G120.md#r20341-bo-pde-3-output-q); output signal for the output of PDE 3

##### PDF - OFF delay

The OFF-delay block contains a timer with OFF delay of the BOOL type.

The falling edge of a pulse at block input I resets output Q to 0 after pulse-stretching time T. Output Q becomes 1 when I becomes 1.

**OFF delay 0**

- [p20168](SINAMICS%20Parameter%20G120.md#p20168-bi-pdf-0-input-pulse-i); input pulse for PDF 0
- [p20169](SINAMICS%20Parameter%20G120.md#p20169-pdf-0-pulse-extension-time-in-ms); input field for the pulse-stretching time
- [r20170](SINAMICS%20Parameter%20G120.md#r20170-bo-pdf-0-output-q); output signal for the output of PDF 0

**OFF delay 1**

- [p20173](SINAMICS%20Parameter%20G120.md#p20173-bi-pdf-1-input-pulse-i); input pulse for PDF 1
- [p20174](SINAMICS%20Parameter%20G120.md#p20174-pdf-1-pulse-extension-time-in-ms); input field for the pulse-stretching time
- [r20175](SINAMICS%20Parameter%20G120.md#r20175-bo-pdf-1-output-q); output signal for the output of PDF 1

**OFF delay 2**

- [p20344](SINAMICS%20Parameter%20G120.md#p20344-bi-pdf-2-input-pulse-i); input pulse for PDF 2
- [p20345](SINAMICS%20Parameter%20G120.md#p20345-pdf-2-pulse-extension-time-in-ms); input field for the pulse-stretching time
- [r20346](SINAMICS%20Parameter%20G120.md#r20346-bo-pdf-2-output-q); output signal for the output of PDF 2

**OFF delay 3**

- [p20349](SINAMICS%20Parameter%20G120.md#p20349-bi-pdf-3-input-pulse-i); input pulse for PDF 3
- [p20350](SINAMICS%20Parameter%20G120.md#p20350-pdf-3-pulse-extension-time-in-ms); input field for the pulse-stretching time
- [r20351](SINAMICS%20Parameter%20G120.md#r20351-bo-pdf-3-output-q); output signal for the output of PDF 3

##### Function diagrams (FD)

- MFP 0 … 3, PCL 0 … 1 - 7230 -
- PDE 0 … 3 - 7232 -
- PDF 0 … 3 - 7233 -
- PST 0 … 1 - 7234 -

##### Additional parameters

---

#### Memory functions

##### Time functions of the free function blocks

The free function blocks of Startdrive have the following memory functions:

- [RSR (RS flip-flop, reset dominant)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#rsr-rs-flip-flop-reset-dominant)
- [DFR (D flip-flop, reset dominant)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#dfr-d-flip-flop-reset-dominant)

For general information about the free function blocks, see [Logical and arithmetic functions using function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#logical-and-arithmetic-functions-using-function-blocks).

##### General parameters

You can enter the runtime group and the run sequence via the following general parameters:

1. Select the sequence in which the function blocks are to be calculated within the runtime group at "Run sequence". A function block with a low number is calculated before a function block with a high number.
2. From the drop-down list, select a runtime group which you want to assign to the function block.

##### RSR flip-flop

The RS flip-flop function block is used as a binary value memory

With logical 1 at input S, output Q is set to logical 1. If input R is set to logical 1, output Q is set to logical 0. If both inputs are logical 0, Q does not change. If both inputs are logical 1, however, Q is logical 0 because the reset input dominates. Output QN always has the opposite value to Q.

**RS flip-flop 0**

- [p20188](SINAMICS%20Parameter%20G120.md#p2018801-bi-rsr-0-inputs)[0]; input signal set of RS flip-flop 0
- p20188[1]; input signal reset of RS flip-flop 0
- [r20189](SINAMICS%20Parameter%20G120.md#r20189-bo-rsr-0-output-q); output signal Q of RS flip-flop 0
- [r20190](SINAMICS%20Parameter%20G120.md#r20190-bo-rsr-0-inverted-output-qn); inverted output signal QN of RS flip-flop 0

**RS flip-flop 1**

- [p20193](SINAMICS%20Parameter%20G120.md#p2019301-bi-rsr-1-inputs)[0]; input signal set of RS flip-flop 1
- p20193[1]; input signal reset of RS flip-flop 1
- [r20194](SINAMICS%20Parameter%20G120.md#r20194-bo-rsr-1-output-q); output signal Q of RS flip-flop 1
- [r20195](SINAMICS%20Parameter%20G120.md#r20195-bo-rsr-1-inverted-output-qn); inverted output signal QN of RS flip-flop 1

**RS flip-flop 2**

- [p20324](SINAMICS%20Parameter%20G120.md#p2032401-bi-rsr-2-inputs)[0]; input signal set of RS flip-flop 2
- p20324[0]; input signal reset of RS flip-flop 2
- [r20325](SINAMICS%20Parameter%20G120.md#r20325-bo-rsr-2-output-q); output signal Q of RS flip-flop 2
- [r20326](SINAMICS%20Parameter%20G120.md#r20326-bo-rsr-2-inverted-output-qn); inverted output signal QN of RS flip-flop 2

##### DFR flip-flop

The DFR flip-flop function block of the BOOL type is used as D flip-flop with reset dominance.

If inputs S and R are logical 0, the D input data is switched through to output Q when a rising edge is present at trigger input I.

Output QN always has the opposite value to Q. With logical 1 at input S, output Q is set to logical 1.

If input R is set to logical 1, output Q is set to logical 0. If both inputs are logical 0, Q does not change.

If inputs S and R are logical 1, however, Q is logical 0 because the reset input dominates.

**DFR flip-flop 0**

- [p20198](SINAMICS%20Parameter%20G120.md#p2019803-bi-dfr-0-inputs)[2]; input signal set S of DFR flip-flop 0
- p20198[1]; input signal D input of DFR flip-flop 0
- p20198[0]; input signal trigger signal I of DFR flip-flop 0
- p20198[3]; input signal reset R of DFR flip-flop 0
- [r20199](SINAMICS%20Parameter%20G120.md#r20199-bo-dfr-0-output-q); output signal Q of DFR flip-flop 0
- [r20200](SINAMICS%20Parameter%20G120.md#r20200-bo-dfr-0-inverted-output-qn); output signal QN of DFR flip-flop 0

**DFR flip-flop 1**

- [p20203](SINAMICS%20Parameter%20G120.md#p2020303-bi-dfr-1-inputs)[2]; input signal set S of DFR flip-flop 1
- p20203[1]; input signal D input of DFR flip-flop 1
- p20203[0]; input signal trigger signal I of DFR flip-flop 1
- p20203[3]; input signal reset R of DFR flip-flop 1
- [r20204](SINAMICS%20Parameter%20G120.md#r20204-bo-dfr-1-output-q); output signal Q of DFR flip-flop 1
- [r20205](SINAMICS%20Parameter%20G120.md#r20205-bo-dfr-1-inverted-output-qn); output signal QN of DFR flip-flop 1

**DFR flip-flop 2**

- [p20329](SINAMICS%20Parameter%20G120.md#p2032903-bi-dfr-2-inputs)[2]; input signal set S of DFR flip-flop 2
- p20329[1]; input signal D input of DFR flip-flop 2
- p20329[0]; input signal trigger signal I of DFR flip-flop 2
- p20329[3]; input signal reset R of DFR flip-flop 2
- [r20330](SINAMICS%20Parameter%20G120.md#r20330-bo-dfr-2-output-q); output signal Q of DFR flip-flop 2
- [r20331](SINAMICS%20Parameter%20G120.md#r20331-bo-dfr-2-inverted-output-qn); output signal QN of DFR flip-flop 2

##### Function diagrams (FD)

- RSR 0 … 2, DFR 0 … 2 - 7240 -

##### Additional parameters

---

#### Switch functions

##### Switch functions of the free function blocks

The free function blocks of Startdrive have the following switch functions:

- [NSW (numerical selector)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#nsw-numerical-selector)
- [BSW (binary selector)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#bsw-binary-selector)

For general information about the free function blocks, see [Logical and arithmetic functions using function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#logical-and-arithmetic-functions-using-function-blocks).

##### NSW - numerical selector

The block switches one of two numeric input variables (REAL type) to the output.

**Switch 0**

- [p20219](SINAMICS%20Parameter%20G120.md#p20219-bi-nsw-0-switch-setting-i); input signal for switch position I of switch 0
- [p20218](SINAMICS%20Parameter%20G120.md#p2021801-ci-nsw-0-inputs)[0]; input X0 of switch 0
- p20218[1]; input X1 of switch 0
- [r20220](SINAMICS%20Parameter%20G120.md#r20220-co-nsw-0-output-y); output Y of switch 0

**Switch 0**

- [p20224](SINAMICS%20Parameter%20G120.md#p20224-bi-nsw-1-switch-setting-i); input signal for switch position I of switch 1
- [p20223](SINAMICS%20Parameter%20G120.md#p2022301-ci-nsw-1-inputs)[0]; input X0 of switch 1
- p20223[1]; input X1 of switch 1
- [r20225](SINAMICS%20Parameter%20G120.md#r20225-co-nsw-1-output-y); output Y of switch 1

##### BSW - binary selector

The block switches one of two binary input variables to the output.

**Switch 0**

- [p20209](SINAMICS%20Parameter%20G120.md#p20209-bi-bsw-0-switch-setting-i); input signal for switch position I of switch 0
- [p20208](SINAMICS%20Parameter%20G120.md#p2020801-bi-bsw-0-inputs)[0]; input I0 of switch 0
- p20208[1]; input I1 of switch 0
- [r20210](SINAMICS%20Parameter%20G120.md#r20210-bo-bsw-0-output-q); output Q of switch 0

**Switch 0**

- [p20214](SINAMICS%20Parameter%20G120.md#p20214-bi-bsw-1-switch-setting-i); input signal for switch position I of switch 1
- [p20213](SINAMICS%20Parameter%20G120.md#p2021301-bi-bsw-1-inputs)[0]; input I0 of switch 1
- p20213[1]; input I1 of switch 1
- [r20215](SINAMICS%20Parameter%20G120.md#r20215-bo-bsw-1-output-q); output Q of switch 1

##### Function diagrams (FD)

- BSW 0 … 1, NSW 0 … 1 - 7250 -

##### Additional parameters

---

#### Control functions

##### Control functions of the free function blocks

The free function blocks of Startdrive have the following control functions:

- [LIM (limiter)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#lim-limiter)
- [PT1 (smoothing element)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#pt1-smoothing-element)
- [INT (integrator)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#int-integrator)
- [DIF (derivative action element)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#dif-derivative-action-element)

For general information about the free function blocks, see [Logical and arithmetic functions using function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#logical-and-arithmetic-functions-using-function-blocks).

##### General parameters

You can enter the runtime group and the run sequence via the following general parameters:

1. Select the sequence in which the function blocks are to be calculated within the runtime group at "Run sequence". A function block with a low number is calculated before a function block with a high number.
2. From the drop-down list, select a runtime group which you want to assign to the function block.

##### LIM - limitation

The function block is used for the limitation. The upper and the lower limits can be set. It is indicated when the set limits are reached.

The function block transfers input variable X to its output Y. The input variable is limited depending on LU and LL.

**Limitation 0**

- [p20228](SINAMICS%20Parameter%20G120.md#p20228-ci-lim-0-input-x); input signal X for LIM0 of limitation 0
- [p20229](SINAMICS%20Parameter%20G120.md#p20229-lim-0-upper-limit-value-lu); input field for the upper limit value of limitation 0
- [p20230](SINAMICS%20Parameter%20G120.md#p20230-lim-0-lower-limit-value-ll); input field for the lower limit value of limitation 0
- [r20232](SINAMICS%20Parameter%20G120.md#r20232-bo-lim-0-input-quantity-at-the-upper-limit-qu); display parameter for "Upper limit value reached" of limitation 0
- [r20231](SINAMICS%20Parameter%20G120.md#r20231-co-lim-0-output-y); output signal Y of limitation 0
- [r20233](SINAMICS%20Parameter%20G120.md#r20233-bo-lim-0-input-quantity-at-the-lower-limit-ql); display parameter for "Lower limit value reached" of limitation 0

**Limitation 1**

- [p20236](SINAMICS%20Parameter%20G120.md#p20236-ci-lim-1-input-x); input signal X for LIM0 of limitation 1
- [p20237](SINAMICS%20Parameter%20G120.md#p20237-lim-1-upper-limit-value-lu); input field for the upper limit value of limitation 1
- [p20238](SINAMICS%20Parameter%20G120.md#p20238-lim-1-lower-limit-value-ll); input field for the lower limit value of limitation 1
- [r20240](SINAMICS%20Parameter%20G120.md#r20240-bo-lim-1-input-quantity-at-the-upper-limit-qu); display parameter for "Upper limit value reached" of limitation 1
- [r20239](SINAMICS%20Parameter%20G120.md#r20239-co-lim-1-output-y); output signal Y of limitation 1
- [r20241](SINAMICS%20Parameter%20G120.md#r20241-bo-lim-1-input-quantity-at-the-lower-limit-ql); display parameter for "Lower limit value" reached of limitation 1

##### Smoothing

The function block is used as a delay element of the 1st order and as a smoothing element.

Input variable X, dynamically delayed by smoothing time constant T, is switched to output Y.

**Smoothing 0**

- [p20244](SINAMICS%20Parameter%20G120.md#p2024401-ci-pt1-0-inputs)[0]; input signal for input X of smoothing 0
- [p20246](SINAMICS%20Parameter%20G120.md#p20246-pt1-0-smoothing-time-constant-in-ms); input field for the smoothing constant of smoothing 0
- p20244[1]; input signal for the setting value SV of smoothing 0
- [p20245](SINAMICS%20Parameter%20G120.md#p20245-bi-pt1-0-accept-setting-value-s); input signal for "Apply setting value" of smoothing 0
- [r20247](SINAMICS%20Parameter%20G120.md#r20247-co-pt1-0-output-y); output signal Y for smoothing 0

**Smoothing 1**

- [p20250](SINAMICS%20Parameter%20G120.md#p2025001-ci-pt1-1-inputs)[0]; input signal for input X of smoothing 1
- [p20252](SINAMICS%20Parameter%20G120.md#p20252-pt1-1-smoothing-time-constant-in-ms); input field for the smoothing constant of smoothing 1
- p20250[1]; input signal for the setting value SV of smoothing 1
- [p20251](SINAMICS%20Parameter%20G120.md#p20251-bi-pt1-1-accept-setting-value-s); input signal for "Apply setting value" of smoothing 1
- [r20253](SINAMICS%20Parameter%20G120.md#r20253-co-pt1-1-output-y); output signal Y for smoothing 1

##### Integration

The function block is used for integration and has the following functions:

- Set initial value
- Adjustable integral-action time constant
- Adjustable limits
- For normal integrator operation, a positive limit value must be specified for the upper limit LU and a negative limit value for the lower limit LL.

**Integration 0**

- [p20256](SINAMICS%20Parameter%20G120.md#p2025601-ci-int-0-inputs)[0]; input signal for input X
- p20256[1]; input signal for the setting value SV
- [p20260](SINAMICS%20Parameter%20G120.md#p20260-bi-int-0-accept-setting-value-s); input signal for "Apply setting value"
- [r20262](SINAMICS%20Parameter%20G120.md#r20262-bo-int-0-integrator-at-the-upper-limit-qu); input field for the upper limit value
- [r20263](SINAMICS%20Parameter%20G120.md#r20263-bo-int-0-integrator-at-the-lower-limit-ql); input field for the lower limit value
- rr20262; display parameter for "Upper limit value reached"
- [r20261](SINAMICS%20Parameter%20G120.md#r20261-co-int-0-output-y); output signal Y
- r20263; display parameter for "Lower limit value reached"

##### Differentiation

The function block is used to perform a differentiation.

Output variable Y is proportional to the rate of change of input variable X multiplied by differentiation time constant TD.

**Differentiation 0**

- [p20284](SINAMICS%20Parameter%20G120.md#p20284-ci-dif-0-input-x); input signal for input X
- [p20285](SINAMICS%20Parameter%20G120.md#p20285-dif-0-differentiating-time-constant-in-ms); input field for the differentiation time constant TD
- [r20286](SINAMICS%20Parameter%20G120.md#r20286-co-dif-0-output-y); output signal Y

##### Function diagrams (FD)

- LIM 0 … 1 - 7260 -
- PT1 0 … 1 - 7262 -
- INT 0, DIF 0 - 7264 -

##### Additional parameters

---

#### Complex functions

##### Complex functions of the free function blocks

The free function blocks of Startdrive have the following complex functions:

- [LVM (double-sided limit monitor with hysteresis)](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#lvm-double-sided-limit-monitor-with-hysteresis)

For general information about the free function blocks, see [Logical and arithmetic functions using function blocks](Commissioning%20SINAMICS%20G120-G115D-G110M%20drives.md#logical-and-arithmetic-functions-using-function-blocks).

##### General parameters

You can enter the runtime group and the run sequence via the following general parameters:

1. Select the sequence in which the function blocks are to be calculated within the runtime group at "Run sequence". A function block with a low number is calculated before a function block with a high number.
2. From the drop-down list, select a runtime group which you want to assign to the function block.

##### Limit monitor

This BOOL-type function block monitors an input variable by comparing it with selectable reference variables.

Application:

- Monitoring setpoints, actual and measured values.
- Suppressing frequent switching (jitter).
- This function block provides a window discriminator function.

**Limit monitor 0**

- [p20266](SINAMICS%20Parameter%20G120.md#p20266-ci-lvm-0-input-x); input signal E
- [p20267](SINAMICS%20Parameter%20G120.md#p20267-lvm-0-interval-average-value-m); input field for the mean interval value M
- [p20268](SINAMICS%20Parameter%20G120.md#p20268-lvm-0-interval-limit-l); input field for the interval limit L
- [p20269](SINAMICS%20Parameter%20G120.md#p20269-lvm-0-hyst-hy); input field for the hysteresis H
- [r20270](SINAMICS%20Parameter%20G120.md#r20270-bo-lvm-0-input-quantity-above-interval-qu); output signal QU for "Interval overshot"
- [r20271](SINAMICS%20Parameter%20G120.md#r20271-bo-lvm-0-input-quantity-within-interval-qm); output signal QM for "Interval observed"
- [r20272](SINAMICS%20Parameter%20G120.md#r20272-bo-lvm-0-input-quantity-below-interval-ql); output signal QL for "Interval undershot"

**Limit monitor 1**

- [p20275](SINAMICS%20Parameter%20G120.md#p20275-ci-lvm-1-input-x); input signal E
- [p20276](SINAMICS%20Parameter%20G120.md#p20276-lvm-1-interval-average-value-m); input field for the mean interval value M
- [p20277](SINAMICS%20Parameter%20G120.md#p20277-lvm-1-interval-limit-l); input field for the interval limit L
- [p20278](SINAMICS%20Parameter%20G120.md#p20278-lvm-1-hyst-hy); input field for the hysteresis H
- [r20279](SINAMICS%20Parameter%20G120.md#r20279-bo-lvm-1-input-quantity-above-interval-qu); output signal QU for "Interval overshot"
- [r20280](SINAMICS%20Parameter%20G120.md#r20280-bo-lvm-1-input-quantity-within-interval-qm); output signal QM for "Interval observed"
- [r20281](SINAMICS%20Parameter%20G120.md#r20281-bo-lvm-1-input-quantity-below-interval-ql); output signal QL for "Interval undershot"

##### Function diagrams (FD)

- LVM 0 … 1 - 7270 -

##### Additional parameters

---

## Fieldbus

This section contains information on the following topics:

- [G120 CU250S-2 V PROFIdrive receive direction](#g120-cu250s-2-v-profidrive-receive-direction)
- [G120 CU250S-2 V PROFIdrive send direction](#g120-cu250s-2-v-profidrive-send-direction)
- [G120 CU250S-2 V PZD send/receive direction diagnostics](#g120-cu250s-2-v-pzd-sendreceive-direction-diagnostics)

### G120 CU250S-2 V PROFIdrive receive direction

#### Description

Parameterize the PROFIdrive telegram in the receive direction.

#### Inactive interconnections

- To hide parts of the telegram that are not used, activate the option "Hide inactive interconnections".

#### Telegram selection

1. In the list, select the telegram with which you want to transfer the data.

   Only those telegrams available for the drive are offered. The interconnections of the control words or receive words have already been created. The selected telegram is displayed in the form of a table.

   If you select the Free telegram configuration, you can define the process data in the receive direction as you choose.
2. Click the control words / receive words buttons which the telegram offers. The receive signal is displayed in a separate window bit-by-bit. The LED displays allow diagnostics of the individual bits.
3. Click the ![Telegram selection](images/103278573835_DV_resource.Stream@PNG-en-US.png) button to display the control word / receive word bit-by-bit. For the free telegram configuration, the signals can be interconnected bit-by-bit here.

#### Function diagrams (FD)

- PROFIdrive - Standard telegrams and process data (PZD) - 2421 -
- PROFIdrive - Manufacturer-specific/free telegrams and process data (PZD) - 2422 -
- PROFIdrive - PZD receive signals, interconnection - 2440 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 0) - 2442 -
- PROFIdrive - STW2 control word interconnection (p2038 = 0) - 2444 -
- PROFIdrive - PZD send signals, interconnection - 2450 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 2) - 2451 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 0) - 2452 -
- PROFIdrive - ZSW2 status word interconnection (p2038 = 0) - 2454 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection - 2464 -
- PROFIdrive - Receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
- PROFIdrive - Send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
- PROFIdrive - Status words, free interconnection - 2472 -
- Control word, sequence control (r0898) - 2501 -
- Status word, sequence control (r0899) - 2503 -
- Control word, setpoint channel (r1198) - 2505 -
- FD-2510 (53)
- Status word 2 (r0053) - 2511 -
- Control word 1 (r0054) - 2512 -
- Supplementary control word (r0055) - 2513 -
- Control word, speed controller (r1406) - 2520 -
- Status word, speed controller (r1407) - 2522 -
- FD-2526 (66)
- Status word, current control (r1408) - 2530 -
- Status word, monitoring functions 1 (r2197) - 2534 -
- Status word, monitoring functions 2 (r2198) - 2536 -
- Status word, monitoring functions 3 (r2199) - 2537 -
- Control word, faults/alarms (r2138) - 2546 -
- Status word, faults/alarms 1 and 2 (r2139 and r2135) - 2548 -

### G120 CU250S-2 V PROFIdrive send direction

#### Description

Parameterize the PROFIdrive telegram in the send direction.

#### Inactive interconnections

- To hide parts of the telegram that are not used, activate the option "Hide inactive interconnections".

#### Telegram

1. In the list, select the telegram with which you want to transfer the data.

   Only those telegrams available for the drive are offered. The interconnections of the control words or receive words have already been created. The selected telegram is displayed in the form of a table.

   If you select the Free telegram configuration, you can define the process data in the send direction as you choose.
2. Click the status word / send word buttons which the telegram offers. The send signal is displayed in a separate window bit-by-bit. The LED displays allow diagnostics of the individual bits.

#### Function diagrams (FD)

- PROFIdrive - Standard telegrams and process data (PZD) - 2421 -
- PROFIdrive - Manufacturer-specific/free telegrams and process data (PZD) - 2422 -
- PROFIdrive - PZD receive signals, interconnection - 2440 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 0) - 2442 -
- PROFIdrive - STW2 control word interconnection (p2038 = 0) - 2444 -
- PROFIdrive - PZD send signals, interconnection - 2450 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 2) - 2451 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 0) - 2452 -
- PROFIdrive - ZSW2 status word interconnection (p2038 = 0) - 2454 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection - 2464 -
- PROFIdrive - Receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
- PROFIdrive - Send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
- PROFIdrive - Status words, free interconnection - 2472 -
- Control word, sequence control (r0898) - 2501 -
- Status word, sequence control (r0899) - 2503 -
- Control word, setpoint channel (r1198) - 2505 -
- FD-2510 (53)
- Status word 2 (r0053) - 2511 -
- Control word 1 (r0054) - 2512 -
- Supplementary control word (r0055) - 2513 -
- Control word, speed controller (r1406) - 2520 -
- Status word, speed controller (r1407) - 2522 -
- FD-2526 (66)
- Status word, current control (r1408) - 2530 -
- Status word, monitoring functions 1 (r2197) - 2534 -
- Status word, monitoring functions 2 (r2198) - 2536 -
- Status word, monitoring functions 3 (r2199) - 2537 -
- Control word, faults/alarms (r2138) - 2546 -
- Status word, faults/alarms 1 and 2 (r2139 and r2135) - 2548 -

### G120 CU250S-2 V PZD send/receive direction diagnostics

#### Description

You can display a diagnosis of the status or control words of the selected telegram here.

#### Function diagrams (FD)

- PROFIdrive - Standard telegrams and process data (PZD) - 2421 -
- PROFIdrive - Manufacturer-specific/free telegrams and process data (PZD) - 2422 -
- PROFIdrive - PZD receive signals, interconnection - 2440 -
- PROFIdrive - STW1 control word interconnection (p2038 = 2) - 2441 -
- PROFIdrive - STW1 control word interconnection (p2038 = 0) - 2442 -
- PROFIdrive - STW2 control word interconnection (p2038 = 0) - 2444 -
- PROFIdrive - PZD send signals, interconnection - 2450 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 2) - 2451 -
- PROFIdrive - ZSW1 status word interconnection (p2038 = 0) - 2452 -
- PROFIdrive - ZSW2 status word interconnection (p2038 = 0) - 2454 -
- PROFIdrive - POS_STW1 positioning control word 1 interconnection - 2463 -
- PROFIdrive - POS_STW2 positioning control word 2 interconnection - 2464 -
- PROFIdrive - Receive telegram, free interconnection via BICO (p0922 = 999) - 2468 -
- PROFIdrive - Send telegram, free interconnection via BICO (p0922 = 999) - 2470 -
- PROFIdrive - Status words, free interconnection - 2472 -
- Control word, sequence control (r0898) - 2501 -
- Status word, sequence control (r0899) - 2503 -
- Control word, setpoint channel (r1198) - 2505 -
- FD-2510 (53)
- Status word 2 (r0053) - 2511 -
- Control word 1 (r0054) - 2512 -
- Supplementary control word (r0055) - 2513 -
- Control word, speed controller (r1406) - 2520 -
- Status word, speed controller (r1407) - 2522 -
- FD-2526 (66)
- Status word, current control (r1408) - 2530 -
- Status word, monitoring functions 1 (r2197) - 2534 -
- Status word, monitoring functions 2 (r2198) - 2536 -
- Status word, monitoring functions 3 (r2199) - 2537 -
- Control word, faults/alarms (r2138) - 2546 -
- Status word, faults/alarms 1 and 2 (r2139 and r2135) - 2548 -

## Interconnections

This section contains information on the following topics:

- [G120 CU250S-2 V interconnections](#g120-cu250s-2-v-interconnections)

### G120 CU250S-2 V interconnections

#### Description

Parameterize the "Interconnections" of the Control Unit.

Each drive unit contains a large number of interconnectable input and output variables and internal control variables. BICO (BInector COnnector) technology allows the drive to be adapted to a wide variety of conditions. Digital and analog signals, which can be connected freely by means of BICO parameters, are identified by the prefix BI, BO, CI or CO in their parameter name. These parameters are identified accordingly in the parameter list or in the function diagrams.

---

**See also**

[BICO technology for drives](Configuring%20SINAMICS%20G120-G115D-G110M%20drives.md#bico-technology-for-drives)
