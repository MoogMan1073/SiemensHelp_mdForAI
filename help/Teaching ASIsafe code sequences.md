---
title: "Teaching ASIsafe code sequences"
package: ASIsafeCodefenUS
topics: 9
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Teaching ASIsafe code sequences

This section contains information on the following topics:

- [Operating principle of code sequences of safe AS-i slaves](#operating-principle-of-code-sequences-of-safe-as-i-slaves)
- ["Teach ASIsafe code sequences" dialog](#teach-asisafe-code-sequences-dialog)
- [Description of the “Slave Status” column](#description-of-the-slave-status-column)
- [Description of the “Code sequence" column](#description-of-the-code-sequence-column)
- [Description of the "F-IN 1...2" column](#description-of-the-f-in-12-column)
- [Description of the "F-OUT 1...4" column](#description-of-the-f-out-14-column)
- [Display of teaching progress](#display-of-teaching-progress)
- ["Transfer taught code sequences" dialog](#transfer-taught-code-sequences-dialog)

## Operating principle of code sequences of safe AS-i slaves

### Function of the code sequences

To monitor safety-related AS‑i input slaves, they must be declared to the system. To do this, the F-CM AS-i Safety module requires information about the code sequences sent by the slaves. To prevent mix-ups of the AS-i input slaves on an AS-i bus, each slave must use a different code sequence. The code sequences are permanently stored in the input slave.

The recording, checking, and storing of these code sequences in the F-CM is referred to as "teaching code sequences".

Once the F-CM detects a new code sequence, the teaching of the code sequences starts automatically. The user must confirm the transfer of the code sequences into the memory to prevent unauthorized changes to the AS-i components.

The F-CM module checks each code sequence for correctness of data content and then sets the safe input image depending on the evaluation.

### Initial commissioning

During initial commissioning, the code sequences are taught at the F-CM from the safe AS-i input slaves that exist on the AS-i bus and then transferred into the non-volatile memory. Both the slaves for which input monitoring is activated as well as the other safe input slaves are detected.

### Replacement of a safe input slave

After replacement of a safe input slave, the new code sequence must be taught and saved.

### Transferring code sequences

In the non-volatile memory, you can transfer the code sequences in one of the following ways:

- Click the "Transfer taught code sequences" button in the "Teaching ASIsafe" dialog box.
- Press the optional "TEACH" button for at least 3 seconds (see also "F-CM AS-i Master ST" manual).

### Replacement of the F-CM module

The non-volatile memory is located in the BaseUnit, which means that code tables that are transferred after the F-CM module is replaced are retained.

### Unsaved code sequences

For safe input slaves having code sequences that are not saved or do not correspond to the saved code sequence, the input channel is passivated and assigned the substitute value 0.

### Safety-related communication for safe AS-i outputs

Safety-related communication for safe AS-i outputs also uses code sequences. However, they have a different data structure compared to the code sequences of safe input slaves. The code sequences for safe AS-i outputs do not have to be taught and transferred.

## "Teach ASIsafe code sequences" dialog

### Description of the "Teach ASIsafe code sequences" dialog

The dialog displays an overview of the existing code sequences of the safety-oriented AS-i slaves. For this purpose, code sequences read in at the AS-i bus can be transferred to the F-CM AS-i Safety ST module memory.

Code sequences can be read in by activating the dialog under "Functions" in "Online & Diagnostics" of the F-CM.

See also: [Operating principle of code sequences of safe AS-i slaves](#operating-principle-of-code-sequences-of-safe-as-i-slaves)

The dialog can only be opened if there is an online connection to the controller or F-CM.

Before the teaching of the code sequences, load the hardware configuration into the controller modules so that the online configuration of the F-CM agrees with the offline configuration.

The "ASIsafe code sequences" dialog does not make any changes to the module configuration and can also be opened for information during operation.

The displayed information is obtained online from the F-CM module. There is no comparison with the offline configuration in this case.

The dialog displays the following information for each AS-i address within the "AS‑i addresses 0…15" and "AS‑i addresses 16…31":

[Slave status](#description-of-the-slave-status-column)

[Code sequence](#description-of-the-code-sequence-column)

[F-IN 1…2](#description-of-the-f-in-12-column)

[F-OUT 1…4](#description-of-the-f-out-14-column)

Information on the slave status is displayed in the TIA Portal for the AS-i address 0.

Under this information, you will find the [Transfer taught code sequences](#transfer-taught-code-sequences-dialog) button and the [progress display for the teaching process](#display-of-teaching-progress).

You can exit the dialog at any time without having to make changes to the data. Code sequences can also be only partially transferred.

## Description of the “Slave Status” column

### Slave status

The "Slave status" column displays information about the AS‑i address via a color code:

Gray: The AS-i slave is neither configured nor detected on the AS-i network.

Green (without checkmark): The address is present on the AS‑i bus but is not activated in the configuration of the F‑CM (input monitoring/output control deactivated). The slave on the AS‑i bus is a safe slave or a standard slave. It is available for use by the AS‑i master or another module.

Green with checkmark: The address is present on the AS‑i bus and corresponds to the configuration of the F‑CM (input monitoring or output control is activated).

Yellow: Error detected: The address is present on the AS‑i bus but does not correspond to the configuration of the F‑CM (input monitoring or output control is activated). Check the slave, replace the slave with the required slave or change the configuration.

Red: Error detected: The address is not present on the AS‑i bus but is required in the configuration of the F‑CM (input monitoring or output control is activated). Check whether the slave exists on the bus and was included in the communication by the AS-i master. Check whether the slave is contained in the configuration of the AS‑i master and correct the bus configuration as required.

## Description of the “Code sequence" column

The "Code sequence" column shows information about the AS‑i address via a color code:

Gray: No code sequence is needed for the address

Green (without checkmark): A new code sequence was taught but not transferred to the memory. The transfer is possible via the "Transfer taught code sequences" button.

Green with checkmark: The code sequence was transferred to the non-volatile memory.

Note: The status is also displayed when the output control is activated for this address. The code sequences for safe outputs are automatically pre-defined in the F-CM and are not transferred into the non-volatile memory of the code sequences.

Yellow: Error detected: A code sequence was taught that is already being used by another slave. Safe operation is not possible. Replace the slave with a different slave.

Red: Warning or error: The address is sending an incomplete or invalid code sequence. Check whether the ON signal is assigned to both inputs of the safe input slave. If required, actuate the associated safety contacts (contacts must be closed). Check whether there is a cross circuit at the inputs and correct the wiring of the inputs as needed.

## Description of the "F-IN 1...2" column

The states of the safety-related AS-i input channels are displayed in the F-IN1 and F-IN2 columns via a color code.

### Meanings of the color codes for F-IN 1...2

Red: Error, e.g. code sequence error. The status of the input channel cannot be read in. The substitute value 0 is used.

Yellow: The input channel shows the value 0 (OFF state) or is not present.

> **Note**
>
> **Condition monitoring**
>
> The status indication is unambiguous once the code sequence has been taught for a safe input slave (ON signal assigned to both inputs), or when an ON signal has been read in for externally controlled safe output slaves.

Green: Signal=1: Contact F-IN closed

White: Signal=0: Contact F-IN open

Gray: The input channel is not present. A safe input slave was not detected at the address.

## Description of the "F-OUT 1...4" column

The states of the safety-related AS-i output channels are displayed in the columns F-OUT1 to F-OUT4 via a color code.

### Meanings of the color codes for F-OUT 1...4

Red: Error, e.g. code sequence error. The status of the output channel cannot be read in.

Yellow: The output channel shows the value 0 (OFF state) or is not present.

> **Note**
>
> **Condition monitoring**
>
> The status indication is unambiguous once the code sequence has been taught for a safe input slave (ON signal assigned to both inputs), or when an ON signal has been read in for externally controlled safe output slaves.

Green: Signal=1: Channel On (ON status)

White: Signal=0: Channel Off (OFF status)

Gray: The output channel is not present. A safe output slave was not detected at the address.

## Display of teaching progress

### Progress bar "Teaching in progress"

If at least one safe slave whose code sequence has not yet been taught is detected on the AS‑i bus, an active progress bar is displayed. Check the displays in the "Code sequence" column and ensure that the safe slaves send their code sequences.

### Trained slaves

The "Trained slaves" output field shows the number of code sequences that has already been applied in relation to the number of code sequences that can still be applied. The number ratio of the output field "Taught slaves" is also displayed as a percentage. If the display reads 100%, all of the code sequences of the existing safe AS-i slaves are transferred into the non-volatile memory.

## "Transfer taught code sequences" dialog

### Description of the "Transfer taught code sequences" dialog

After the "Transfer taught code sequences" button is actuated, a dialog opens with a prompt asking if the code sequences should be transferred. You must confirm that you are addressing the correct module. As a check, the green LED "ADDR" on the front panel of the F-CM module flashes.

- You can cancel the prompt using the "No" button without transferring the code sequences.
- If you click "Yes", the taught code sequences are transferred into the non-volatile memory. Next, the input data of the safe AS-i input slaves is evaluated, allowing reintegration in the safety program.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Plant components can be switched on**  Depending on the safety program, the transfer of code sequences may cause plant components to be switched on. Before the transfer, ensure that no personnel injuries or property damage can occur. After transferring, check the safety equipment for proper functioning. |  |

The "Transfer taught code sequences" button is deactivated when all taught code sequences have already been transferred to the non-volatile memory.
