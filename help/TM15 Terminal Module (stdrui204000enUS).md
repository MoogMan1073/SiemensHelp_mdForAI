---
title: "TM15 Terminal Module"
package: stdrui204000enUS
topics: 7
source: Siemens TIA Portal Information System (offline help, en-US)
---


# TM15 Terminal Module

This section contains information on the following topics:

- [TM15 overview](#tm15-overview)
- [Parameterize TM15](#parameterize-tm15)

## TM15 overview

This section contains information on the following topics:

- [TM15 description](#tm15-description)
- [TM15 interfaces](#tm15-interfaces)

### TM15 description

The TM15 Terminal Module (TM) is a terminal expansion module for snapping on to a standard mounting rail according to DIN 50022. The number of available digital inputs/outputs within a drive system can be expanded with the TM15. It provides 24 bidirectional digital inputs/outputs (isolated into three groups).

The TM15 is inserted into the device view via the hardware catalog and connected via DRIVE-CLiQ.

### TM15 interfaces

#### Description

![TM15 interfaces](images/147820317835_DV_resource.Stream@PNG-en-US.png)

TM15 interfaces

## Parameterize TM15

This section contains information on the following topics:

- [TM15 bidirectional digital inputs/outputs](#tm15-bidirectional-digital-inputsoutputs)
- [TM15 control logic](#tm15-control-logic)

### TM15 bidirectional digital inputs/outputs

Here you can change the interconnection of the bidirectional digital inputs/outputs on the input/output component.

- You can assign bidirectional digital inputs/outputs in the function. This means they can be parameterized either as an input or an output.
- Digital inputs are used for the acquisition of digital signals. For example, drive enables can be controlled externally.
- For every digital input signal there is the corresponding inverted signal which can also be used for interconnection.
- Digital outputs are used for the feedback of signals such as enables.

#### Parameterizing digital inputs/outputs

1. If you want to simplify the view of the screen form, activate the "Optimize view" option.

   The display is then reduced to the essentials. Bidirectional digital inputs cannot be edited in the optimized view. Interconnections are still possible in every view.
2. If you want to assign digital outputs (0...7, 8…15, 16…23), proceed as follows:

   - Interconnect the signal sinks ([r4022](SINAMICS%20Parameter%20SERVO.md#r402201-cobo-digital-inputs-status)) for the digital outputs 0...7, 8…15, 16…23.
   - Interconnect the signal sinks ([r4023](SINAMICS%20Parameter%20SERVO.md#r402301-bo-digital-inputs-status-inverted)) for the inverted digital outputs 0...7, 8…15, 16…23.
3. If you want to assign digital inputs (0...7, 8…15, 16…23), interconnect the signal sources for the digital inputs or the inverted digital inputs 0...7, 8…15, 16…23.

#### Function diagrams (FD)

- Terminal Module 15 (TM15) - Digital inputs/outputs bidirectional (DI/DO 0 ... DI/DO 7) - 9400 -
- Terminal Module 15 (TM15) - Digital inputs/outputs bidirectional (DI/DO 8 ... DI/DO 15) - 9401 -
- Terminal Module 15 (TM15) - Digital inputs/outputs bidirectional (DI/DO 16 ... DI/DO 23) - 9402 -

#### Additional parameters

---

### TM15 control logic

The interconnections for control/status words of the faults and alarms are displayed and can be edited here.

#### Parameterizing the control logic

1. Select in the drop-down list of the "Control logic" screen form which status words (r2139) or control words (r2138) should be displayed so they can then be interconnected.
2. Then interconnect the individual bits of the status and control words displayed in the screen form.

   A green LED indicates that the corresponding bit of the control or status word is set. If the bit value of the control or status word results from the logical interconnection of several signal sources, the type of the logical interconnection is displayed by the associated logic symbol.

#### Function diagrams (FD)

- Internal control/status words - Control word faults/alarms - 2546 -
- Internal control/status words - Status word faults/alarms 1 and 2 - 2548 -
