---
title: "Asynchronous instructions (S7-300, S7-400)"
package: ProgParamAll34enUS
topics: 2
devices: [S7-300, S7-400]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Asynchronous instructions (S7-300, S7-400)

This section contains information on the following topics:

- [Difference between synchronous and asynchronous instructions (S7-300, S7-400)](#difference-between-synchronous-and-asynchronous-instructions-s7-300-s7-400)

## Difference between synchronous and asynchronous instructions (S7-300, S7-400)

### Asynchronous instructions

In program processing, a differentiation is made between synchronous and asynchronous instructions.

The "synchronous" and "asynchronous" properties relate to the temporal relationship between the call and execution of the instruction.

- The following applies to synchronous instructions: When the call of a synchronous instruction is ended, the execution is also ended.
- This is different in the case of asynchronous instructions: The execution of an asynchronous instruction can extend over multiple calls. The CPU processes asynchronous instructions in parallel with the cyclic user program. Asynchronous instructions occupy resources in the CPU while they are being processed.

Asynchronous instructions are usually instructions for transferring data (data records for modules, communication data, diagnostics data).

Additional information about asynchronous instructions can be found here:[SIMATIC S7-1500 / ET 200MP Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/86140384) In the system manual under Basics of program processing &gt; Asynchronous instructions​

### Identification of the job

To execute an instruction over multiple calls, the CPU must be able to uniquely assign a subsequent call to a running job of the instruction. To assign a call to a job, the CPU uses one of the following two mechanisms, depending on the type of the instruction:

- The instance of the instruction (with type "SFB" system function block)
- The input parameter of the instruction identifying the job

If you use asynchronous instructions to trigger a process interrupt, output control commands to DP slaves, start a data transfer, or abort a non-configured connection and then call the same instruction again before the current job is completed, the reaction of the instruction will depend on whether the second call involves the same job.

### Passing parameters to program blocks that are to be executed asynchronously

Code blocks (FBs/FCs) and data blocks (DBs) can be created with different access types ("standard" and "optimized"). In code blocks, you can call any instructions. Some instructions (e.g. "WRIT_DBL" and "READ_DBL") are executed asynchronously. These blocks cannot be supplied with tags from TEMP because the data must not be changed during execution.

Ensure that you do not use these instructions in programs in which code blocks of different access types are called reciprocally. This could cause the following to occur:

- A structure from a standard data block is directly or indirectly passed to an optimized code block, which forwards this structure directly or indirectly to one of the blocks mentioned above.
- The reverse scenario, whereby a structure from an optimized code block is directly or indirectly passed to a standard data block, which forwards this structure directly or indirectly to one of the program blocks mentioned above.

Otherwise, a hidden copy of the passed data is created in TEMP, which leads to the asynchronous program blocks returning a negative acknowledgment.

### Parameter REQ

The input parameter REQ (request) is used solely to start the job:

- Trigger the job by setting the input parameter REQ to "1" (case 1).
- If a particular job has been started and not yet completed and you call the instruction again to perform the same job (for example, in a cyclic interrupt OB), then REQ is not evaluated by the instruction (case 2).
- If the job is completed, but the input parameter REQ is still set to "1", the job is immediately started again.

  > **Note**
  >
  > **REQ bit = "1"**
  >
  > Please note that, when the REQ bit is set, the asynchronous instruction will be started again after the previous call is completed. This may not be desired. To make the project clearer and easier to maintain, it is therefore advisable to reset the REQ bit to "0" as early as possible.

### Parameter RET_VAL and BUSY

The output parameters RET_VAL and BUSY indicate the status of the job.

Pay attention to the note in section: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

- In case 1 (first call with REQ = 1), code W#16#7001 will be entered in RET_VAL and BUSY will be set to "1" if system resources are available and the supply of the input parameters is correct.

  If the required system resources are currently being used or the input parameters contain an error, the corresponding error code is entered in RET_VAL and BUSY receives the value "0".
- In case 2 (intermediate call), the code W#16#7002 is entered in RET_VAL (this corresponds to the message that the call is currently still being processed) and BUSY is set to "1".
- The following applies to the last call for a job:

  - For instructions "[DPNRM_DG](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)", "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)" in case of fault-free data transmission, the number of supplied data will be entered in RET_VAL as a positive number in bytes. BUSY has the value "0" in this case.

    If there is an error, then the error information will be entered in RET_VAL and you should not evaluate BUSY in this case.
  - With "[RD_REC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_rec-read-data-record-from-io-s7-300-s7-400), the size of the data record in bytes is entered in RET_VAL or the value 0 if no error has occurred during data transmission. BUSY receives the value "0" in this case. If there is an error, the error code will be entered in RET_VAL and BUSY will receive the value "0".
  - For all other instructions, "0" will be entered in RET_VAL if the job was executed without errors and BUSY will receive the value "0". If there is an error, the error code will be entered in RET_VAL and BUSY will receive the value "0".

> **Note**
>
> If the first and last call coincide, the reaction for RET_VAL and BUSY is the same as for the last call.

### Resources occupied by the job

Every job occupies CPU resources. The instruction "RDREC", for example, occupies memory space for the destination area. These resources are assigned exclusively to this job and are occupied as long as the instruction is active, i.e. as long as BUSY has the value "1".

You cannot change occupied resources or use them for other purposes. For example, you cannot change either the length or the content of the destination area for the instruction "RDREC".

### Overview

The following table provides you with an overview of the relationships explained above. In particular, it shows the possible values of the output parameters if the execution of the job is not completed after an instruction call has been completed.

> **Note**
>
> Following every call, you must evaluate the relevant output parameters in your program.

Relationship between call, REQ, RET_VAL and BUSY during a "running" job.

| Number of the  call | Type of call | REQ | RET_VAL | BUSY | DONE | ERROR |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | First call | 1 | W#16#7001 | 1 | 0 | 0 |
| Error code | 0 | 0 | 1 |  |  |  |
| 2 to (n - 1) | Intermediate call | irrelevant | W#16#7002 | 1 | 0 | 0 |
| n | Last call | irrelevant | W#16#0000 (exceptions: "[RD_REC](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#rd_rec-read-data-record-from-io-s7-300-s7-400)" if the destination area is larger  than the data record transferred; "[DPNRM_DG](Extended%20instructions%20%28S7-300%2C%20S7-400%29.md#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-300-s7-400)", "[X_GET](MPI%20communication%20%28S7-300%2C%20S7-400%29.md#x_get-read-data-from-a-communication-partner-outside-the-local-s7-station-s7-300-s7-400)" and "[I_GET](Communication%20with%20iSlave%20-%20iDevice%20%28S7-300%2C%20S7-400%29.md#i_get-read-data-from-a-communication-partner-within-the-local-s7-station-s7-300-s7-400)"), if no errors have  occurred. | 0 | 1 | 0 |
| Error code if errors occurred | 0 | 0 | 1 |  |  |  |
