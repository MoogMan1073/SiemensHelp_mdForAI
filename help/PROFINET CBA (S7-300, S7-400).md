---
title: "PROFINET CBA (S7-300, S7-400)"
package: ProgKomPNetCBA34enUS
topics: 5
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# PROFINET CBA (S7-300, S7-400)

This section contains information on the following topics:

- [Information regarding PN_IN, PN_OUT, and PN_DP (S7-300, S7-400)](#information-regarding-pn_in-pn_out-and-pn_dp-s7-300-s7-400)
- [PN_IN: Update the inputs of the user program interface (S7-300, S7-400)](#pn_in-update-the-inputs-of-the-user-program-interface-s7-300-s7-400)
- [PN_OUT: Update the outputs of the user program interface (S7-300, S7-400)](#pn_out-update-the-outputs-of-the-user-program-interface-s7-300-s7-400)
- [PN_DP: Update DP interconnections (S7-300, S7-400)](#pn_dp-update-dp-interconnections-s7-300-s7-400)

## Information regarding PN_IN, PN_OUT, and PN_DP (S7-300, S7-400)

### 

> **Note**
>
> By default, the operating system updates both the PROFINET CBA component as well as the DP interconnections at the cycle control point. If, however, you have disabled these automatic updates in the configuration (for example to improve the time response of the CPU), you will have to perform the updates yourself. This is done by calling the "[PN_IN](#pn_in-update-the-inputs-of-the-user-program-interface-s7-300-s7-400)", "[PN_OUT](#pn_out-update-the-outputs-of-the-user-program-interface-s7-300-s7-400)" and "[PN_DP](#pn_dp-update-dp-interconnections-s7-300-s7-400)" instructions at appropriate times. These updates can only be disabled as a group and not individually in the configuration.

### Shadow memory

The interface DB is the user program interface for the PROFINET CBA component. To ensure that the inputs and outputs are consistent when the associated program sections are running, each interface DB has an identically structured memory area that is managed by the operating system. This area is called "shadow memory". In your program, you can only access the interface DB, and other (external) PROFINET CBA components can only access the shadow memory. This arrangement prevents conflicts in accessing the inputs and outputs of the interface DB.

### Updating the PROFINET CBA component

The data consistency provided by the use of the shadow memory means that updating the PROFINET CBA component takes place in the following two steps:

- The inputs in the shadow memory are copied to the inputs of the interface DB before your program for the PROFINET CBA component starts
- The outputs of the interface DB are copied to the outputs of the shadow memory after your program for the PROFINET CBA component has run

The PROFINET CBA component is updated on CPUs with an integrated PROFINET interface either by the operating system or by the [PN_IN](#pn_in-update-the-inputs-of-the-user-program-interface-s7-300-s7-400)" and "[PN_OUT](#pn_out-update-the-outputs-of-the-user-program-interface-s7-300-s7-400)" instructions (depending on how you configured the PROFINET CBA component when you created it). The following schematic diagram illustrates the update by the "[PN_IN](#pn_in-update-the-inputs-of-the-user-program-interface-s7-300-s7-400)" and "[PN_OUT](#pn_out-update-the-outputs-of-the-user-program-interface-s7-300-s7-400)" instructions.

![Updating the PROFINET CBA component](images/19164337803_DV_resource.Stream@PNG-en-US.png)

The system-side update always occurs at the cycle control point.

If, on the other hand, you perform the update using the "[PN_IN](#pn_in-update-the-inputs-of-the-user-program-interface-s7-300-s7-400)" and "[PN_OUT](#pn_out-update-the-outputs-of-the-user-program-interface-s7-300-s7-400)" instructions, you will need to call "[PN_IN](#pn_in-update-the-inputs-of-the-user-program-interface-s7-300-s7-400)" at the start of the OB containing the program associated with the PROFINET CBA component and "[PN_OUT](#pn_out-update-the-outputs-of-the-user-program-interface-s7-300-s7-400)" at the end of this OB. This procedure is shown using OB 30 as an example in the following Fig.

![Updating the PROFINET CBA component](images/19164351499_DV_resource.Stream@PNG-en-US.png)

> **Note**
>
> (More than one PROFINET interface DB on a device):
>
> With multifunction components, it is possible to update all interface DBs with one job (DBNO=0) – similar to the update at the cycle control point but triggered by an instruction. If an error occurs when updating an interface DB, the updating of the other interface DBs continues. A negative RET_VAL relates to one of the updated interface DBs.

### Updating the DP interconnections

The DP interconnections are updated either by the operating system or by the "[PN_DP](#pn_dp-update-dp-interconnections-s7-300-s7-400)" instruction, depending on how you configured the PROFINET CBA component when you created it.

## PN_IN: Update the inputs of the user program interface (S7-300, S7-400)

### Description

With the "PN_IN" instruction, you copy the input data in PROFINET CBA from the shadow memory of the PROFINET CBA component to the associated interface DB. After conclusion of the instruction, your application has the current input data available to it.

### Parameters

The following table shows the parameters of the "PN_IN" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| DBNO | Input | WORD | I, Q, M, D, L or constant | DB no. of the interface DB (DBNO=0: Updating all PROFINET CBA interface DBs) |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### RET_VAL parameter

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8001 | PROFINET CBA configuration is not available or invalid. |
| 8002 | The DB number does not match the one in the component configuration. |
| 8004 | The DB number matches the one in the component configuration, but the DB is not yet loaded. |
| 8005 | The interface DB was compiled with the keyword UNLINKED, in other words, it is only in the load memory but not in the work memory. |
| 8006 | The interface DB is write-protected in the CPU. |
| 80B1 | Length error when reading or writing. The component configuration does not fit the loaded DB. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## PN_OUT: Update the outputs of the user program interface (S7-300, S7-400)

### Description

With the instruction "PN_OUT", you copy the output data generated in your application from the interface DB of the PROFINET CBA component to the associated shadow memory. After conclusion of the instruction, the other PROFINET CBA components have the current output data available to them.

### Parameters

The following table shows the parameters of the "PN_OUT" instruction:

| Parameters | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| DBNO | Input | WORD | I, Q, M, D, L or constant | DB no. of the interface DB (DBNO=0: Updating of all PROFINET interface DBs) |
| RET_VAL | Return | INT | I, Q, M, D, L | Error information |
|  |  |  |  |  |

You will find more detailed information on valid data types in "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### RET_VAL parameter

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | No error occurred. |
| 8001 | PROFINET CBA configuration is not available or invalid. |
| 8002 | The DB number does not match the one in the component configuration. |
| 8004 | The DB number matches the one in the component configuration, but the DB is not yet loaded. |
| 8005 | The interface DB was compiled with the keyword UNLINKED, in other words, it is only in the load memory but not in the work memory. |
| 8006 | The interface DB is write-protected in the CPU. |
| 80B1 | Length error when reading or writing. The component configuration does not fit the loaded DB. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |

## PN_DP: Update DP interconnections (S7-300, S7-400)

### Description

With the "PN_DP" instruction you update all

- interconnections between PROFINET CBA components on the local PROFIBUS and
- interconnections with cyclic transmission between PROFINET CBA components on the local PROFIBUS and external PROFINET CBA components. The interconnections apply between networks (between Industrial Ethernet and PROFIBUS DP).

### Functional description

"PN_DP" is an asynchronous instruction, its processing extends, if necessary, over multiple calls. To start updating the DP interconnections, call "PN_DP" with REQ=1.

The output parameters RET_VAL and BUSY indicate the status of the job.

See also: [Difference between synchronous and asynchronous instructions](Asynchronous%20instructions%20%28S7-300%2C%20S7-400%29.md#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400).

### Parameters

The following table shows the parameters of the "PN_DP" instruction:

| Parameter | Declaration | Data type | Memory area | Description |
| --- | --- | --- | --- | --- |
| REQ | Input | BOOL | I, Q, M, D, L | REQ = 1: Initiate update of the DP interconnections |
| RET_VAL | Return | INT | I, Q, M, D, L | If an error occurs while the instruction is being executed, the return value contains an error code. |
| BUSY | Output | BOOL | I, Q, M, D, L | BUSY=1:  The updating of the DP interconnection is not yet complete. |
|  |  |  |  |  |

For additional information on valid data types, refer to "[Overview of the valid data types](Data%20types.md#overview-of-the-valid-data-types)".

### Parameter RET_VAL

| Error code  (W#16#...) | Explanation |
| --- | --- |
| 0000 | Job completed without error. |
| 7000 | First call with REQ = 0: Update of DP interconnections not initiated. BUSY has the value "0". |
| 7001 | (only relevant for S7-400:) First call with REQ = 1: BUSY has the value "1". |
| 7002 | (only relevant for S7-400:) Intermediate call (REQ irrelevant). The updating of the DP interconnections is not yet completed. BUSY has the value "1". |
| 8001 | PROFINET CBA configuration is not available or invalid. |
| 8095 | You have initiated another update of the DP interconnections in a higher priority class. However, the update in the priority class with lower priority (by the operating system or a "PN_DP" processing) is still running. |
| 8xyy | General error information  See also: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val) |
