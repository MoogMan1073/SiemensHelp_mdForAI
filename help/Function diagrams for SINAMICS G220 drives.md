---
title: "Function diagrams for SINAMICS G220 drives"
package: StdrG220FuDiOverviewenUS
topics: 2
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Function diagrams for SINAMICS G220 drives

This section contains information on the following topics:

- [Function diagrams for SINAMICS G220 - Overview](#function-diagrams-for-sinamics-g220---overview)

## Function diagrams for SINAMICS G220 - Overview

The structure of the drive functions and the relationship of the individual parameters with other parameters is displayed in the function diagrams:

Explanation of the symbols (Part 1) - 1020 -
  

Explanation of the symbols (Part 2) - 1021 -
  

Explanation of the symbols (Part 3) - 1022 -
  

Overview - 2201 -
  

Isolated digital inputs (DI 0 … DI 5, DI 21 ... DI 22) - 2221 -
  

Digital outputs 0 ... 2 (DO 0 ... DO 2) - 2242 -
  

Analog inputs 0 ... 1 (AI 0 ... AI 1) - 2251 -
  

Analog inputs as digital inputs (DI 11 … DI 12) - 2256 -
  

Analog output 0 (AO 0) - 2261 -
  

Two-wire control - 2272 -
  

Three-wire control - 2273 -
  

Control commands and interrogation commands - 2381 -
  

States - 2382 -
  

Overview - 2401 -
  

Standard telegrams and process data (PZD) - 2415 -
  

Manufacturer-specific telegrams and process data (PZD) - 2418 -
  

Supplementary telegram/free telegrams and process data (PZD) - 2423 -
  

PZD receive signals interconnection - 2440 -
  

STW1 control word interconnection in Interface Mode 3 (VIK/NAMUR) - 2441 -
  

STW1 control word interconnection in Interface Mode 1 - 2442 -
  

STW1 control word interconnection in Interface Mode 2 - 2443 -
  

STW2 control word interconnection in Interface Mode 1 - 2444 -
  

STW2 control word interconnection in Interface Mode 2 - 2445 -
  

PZD send signals interconnection - 2450 -
  

ZSW1 status word interconnection in Interface Mode 3 (VIK-NAMUR) - 2451 -
  

ZSW1 status word interconnection in Interface Mode 1 - 2452 -
  

ZSW1 status word interconnection in Interface Mode 2 - 2453 -
  

ZSW2 status word interconnection in Interface Mode 1 - 2454 -
  

ZSW2 status word interconnection in Interface Mode 2 - 2455 -
  

MELDW status word interconnection - 2460 -
  

Receive telegram free interconnection (r0922 = 999) - 2468 -
  

Send telegram free interconnection (r0922 = 999) - 2470 -
  

Control word, sequence control - 2501 -
  

Status word, sequence control - 2503 -
  

Control word, setpoint channel - 2505 -
  

Status word 1 (r0052) - 2510 -
  

Status word 2 (r0053) - 2511 -
  

Control word 1 (r0054) - 2512 -
  

Supplementary control word 2 (r0055) - 2513 -
  

Control word speed controller (r1406) - 2520 -
  

Status word speed controller (r1407) - 2522 -
  

Status word closed-loop control (r0056) - 2526 -
  

Status word current control (r1408) - 2530 -
  

Status word monitoring 1 - 2534 -
  

Status word monitoring 2 - 2536 -
  

Status word monitoring 3 - 2537 -
  

Status word faults/alarms 1 (r2139) - 2548 -
  

Status word faults/alarms 2 (r2135) - 2549 -
  

Sequence control - Sequencer - 2610 -
  

Sequence control - Missing enables, line contactor control - 2634 -
  

Simple brake control - 2701 -
  

Fail-safe digital inputs (F-DI 0 ... F-DI 2) - 2850 -
  

Fail-safe digital output (F-DO 0) - 2853 -
  

Control signals safe motion monitoring function (Part 1) - 2854 -
  

Control signals safe motion monitoring function (Part 2) - 2855 -
  

Safe State selection - 2856 -
  

Standard telegrams - 2915 -
  

Manufacturer-specific telegrams - 2917 -
  

Overview - 3001 -
  

Fixed speed setpoints, binary selection (p1016 = 2) - 3010 -
  

Fixed speed setpoints, direct selection (p1016 = 1) - 3011 -
  

Motorized potentiometer - 3020 -
  

Main/additional setpoint, setpoint scaling, jog - 3030 -
  

Direction limitation and direction reversal - 3040 -
  

Skip frequency bands - 3050 -
  

Speed limitations - 3051 -
  

Basic ramp-function generator - 3060 -
  

Extended ramp-function generator - 3070 -
  

Ramp-function generator selection, -status word, -tracking - 3080 -
  

Position and temperature sensing, encoders 1 ... 2 - 4704 -
  

Speed actual value and pole position sensing motor encoder (encoder 1) - 4715 -
  

Encoder interface, receive signals, encoder 1 ... 2 - 4720 -
  

Encoder interface, send signals, encoder 1 ... 2 - 4730 -
  

Absolute value for incremental encoder - 4750 -
  

Closed-loop speed control and generation of the torque limits, overview - 6020 -
  

Speed setpoint, droop - 6030 -
  

Precontrol symmetrization, acceleration model - 6031 -
  

Moment of inertia estimator - 6035 -
  

Speed controller - 6040 -
  

Kp_n/Tn_n adaptation - 6050 -
  

Torque setpoint - 6060 -
  

Vdc_max controller and Vdc_min controller - 6220 -
  

U/f control, overview - 6300 -
  

U/f control, voltage boost - 6301 -
  

U/f control, voltage characteristics - 6302 -
  

U/f control, resonance damping - 6310 -
  

U/f control, slip compensation - 6311 -
  

U/f control, Vdc_max controller and Vdc_min controller - 6320 -
  

Closed-loop speed control configuration - 6490 -
  

Flux control configuration - 6491 -
  

Upper/lower torque limit - 6630 -
  

Current/power/torque limits - 6640 -
  

Closed-loop current control, overview - 6700 -
  

Current setpoint filter - 6710 -
  

Iq and Id controllers (Part 1) - 6714 -
  

Iq and Id controllers (Part 2) - 6715 -
  

Id setpoint (permanent-magnet synchronous motor, p0300 = 2xxx) - 6721 -
  

Field weakening characteristic, Id setpoint (induction motor, p0300 = 1xxx) - 6722 -
  

Field weakening controller, flux controller, Id setpoint (induction motor, p0300 = 1xxx) - 6723 -
  

Field weakening controller (permanent-magnet synchronous motor, p0300 = 2xxx) - 6724 -
  

Interface to the power unit (induction motor, p0300 = 1xxx) - 6730 -
  

Interface to the power unit (permanent-magnet synchronous motor, p0300 = 2xxx) - 6731 -
  

Flux setpoint (synchronous reluctance motor, p0300 = 6xxx) - 6790 -
  

Field weakening controller, Id setpoint (synchronous reluctance motor, p0300 = 6xxx) - 6791 -
  

Interface to the power unit (synchronous reluctance motor, p0300 = 6xxx) - 6792 -
  

Display signals - 6799 -
  

Closed-loop speed control and generation of the torque limits, overview - 6820 -
  

Current control, overview - 6821 -
  

Speed setpoint, precontrol symmetrization, acceleration model - 6822 -
  

Speed controller with Kp_n/Tn_n adaptation - 6824 -
  

Torque setpoint - 6826 -
  

Upper/lower torque limit - 6828 -
  

Current/power/torque limits - 6829 -
  

Current setpoint filter - 6832 -
  

Iq and Id controller - 6833 -
  

Flux setpoint (synchronous reluctance motor, p0300 = 6xxx) - 6834 -
  

Field weakening controller, Id setpoint (synchronous reluctance motor, p0300 = 6xxx) - 6835 -
  

Id setpoint (permanent-magnet synchronous motor, p0300 = 2xxx) - 6836 -
  

Field weakening characteristic, flux setpoint (induction motor, p0300 = 1xxx) - 6837 -
  

Field weakening controller, flux controller, Id setpoint (induction motor, p0300 = 1xxx) - 6838 -
  

Field weakening controller (permanent-magnet synchronous motor, p0300 = 2xxx) - 6839 -
  

Interface to the power unit (induction motor, p0300 = 1xxx) - 6841 -
  

Interface to the power unit (permanent-magnet synchronous motor, p0300 = 2xxx) - 6842 -
  

Interface to the power unit (synchronous reluctance motor, p0300 = 6xxx) - 6843 -
  

Overview - 6850 -
  

Characteristic and voltage boost - 6851 -
  

Current/power/torque limits - 6852 -
  

Interface to the power unit (induction motor, p0300 = 1xxx) - 6856 -
  

Friction characteristic - 7010 -
  

External armature short-circuit (EASC, p0300 = 2xxx) - 7014 -
  

Internal armature short-circuit (IASC, p0300 = 2xxx) - 7016 -
  

DC braking (p0300 = 1xxx) - 7017 -
  

Bypass - 7035 -
  

Fixed values, binary selection (p2216 = 2) - 7950 -
  

Fixed values, direct selection (p2216 = 1) - 7951 -
  

Motorized potentiometer - 7954 -
  

Closed-loop control, vector (Part 1) - 7957 -
  

Closed-loop control, vector (Part 2) - 7958 -
  

Kp-/Tn adaptation and Kp-/Tn selection - 7959 -
  

Overview - 8005 -
  

Speed signals (Part 1) - 8010 -
  

Speed signals (Part 2) - 8011 -
  

Torque signals (not available for U/f control) - 8012 -
  

Load monitoring (Part 1) - 8013 -
  

Load monitoring (Part 2) - 8014 -
  

Blocking and stall monitoring - 8015 -
  

Thermal monitoring, motor - 8016 -
  

Motor temperature model 1 (I2t) - 8017 -
  

Motor temperature model 2 - 8018 -
  

Motor temperature model 3 - 8019 -
  

Motor temperature status word faults/alarms - 8020 -
  

Thermal monitoring, power unit - 8021 -
  

Monitoring functions (Part 1) - 8022 -
  

Monitoring functions (Part 2) - 8023 -
  

Variable signaling function 1, 2, 3 - 8024 -
  

Overview - 8050 -
  

Fault buffer - 8060 -
  

Alarm buffer - 8065 -
  

Safety message buffer (p3117 = 0) - 8070 -
  

Command data sets (CDS) - 8560 -
  

Drive data sets (DDS) - 8565 -
  

Encoder data sets (EDS) - 8570 -
  

Motor data sets (MDS) - 8575 -
  

Overview - 8601 -
  

Control word sequence control infeed - 8605 -
  

Status word sequence control infeed - 8606 -
  

Status word infeed - 8608 -
  

Sequencer - 8610 -
  

Missing enable signals, line contactor control - 8612 -
  

Controller modulation depth reserve/DC link voltage - 8615 -
  

Current pre-control/current controller/gating unit - 8617 -
  

Interface to the power unit, control signals, actual values - 8619 -
  

Line voltage monitoring - 8620 -
  

Monitoring the line frequency, DC link voltage and precharging - 8621 -
  

Thermal monitoring power unit infeed - 8622 -
