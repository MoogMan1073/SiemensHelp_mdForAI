---
title: "Asynchronous instructions (S7-1200, S7-1500)"
package: ProgParamAll2MenUS
topics: 2
devices: [S7-1200, S7-1500, S7-1500T]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Asynchronous instructions (S7-1200, S7-1500)

This section contains information on the following topics:

- [Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)](#difference-between-synchronous-and-asynchronous-instructions-s7-1200-s7-1500)

## Difference between synchronous and asynchronous instructions (S7-1200, S7-1500)

### Asynchronous instructions

In program processing, a differentiation is made between synchronous and asynchronous instructions.

The "synchronous" and "asynchronous" properties relate to the temporal relationship between the call and execution of the instruction.

- The following applies to synchronous instructions: When the call of a synchronous instruction is ended, the execution is also ended.
- This is different in the case of asynchronous instructions: The execution of an asynchronous instruction can extend over multiple calls. The CPU processes asynchronous instructions in parallel with the cyclic user program. Asynchronous instructions occupy resources in the CPU while they are being processed.

Asynchronous instructions are usually instructions for transferring data (data records for modules, communication data, diagnostics data).

Additional information about asynchronous instructions can be found here: [SIMATIC S7-1500 / ET 200MP Manual Collection](https://support.industry.siemens.com/cs/ww/en/view/86140384) in the system manual under Basics of program processing > Asynchronous instructions​

### Identification of the job

To execute an instruction over multiple calls, the CPU must be able to uniquely assign a subsequent call to a running job of the instruction. To assign a call to a job, the CPU uses one of the following two mechanisms, depending on the type of the instruction:

- The instance of the instruction (with type "SFB" system function block)
- The input parameter of the instruction identifying the job

If you use asynchronous instructions to trigger a process interrupt, output control commands to DP slaves, start a data transfer, or abort a non-configured connection and then call the instruction again before the current job is completed, the reaction of the instruction will depend on whether the second call involves the same job.

### Passing parameters to program blocks that are to be executed asynchronously

In code blocks, you can call any instructions. Some instructions (e.g. "WRIT_DBL" and "READ_DBL") are executed asynchronously. With asynchronously executed instructions, larger amounts of data at the inputs must not be changed during execution because they are processed in small parts. It follows that these parameters cannot be supplied with tags from TEMP.

Code blocks (FBs/FCs) and data blocks (DBs) can be created with different access types ("standard" and "optimized").

Ensure that asynchronous instructions are not used in parts of the program in which code blocks with different kinds of access call each other. This could cause the following to occur:

- A structure from a standard data block is directly or indirectly passed to an optimized code block, which forwards this structure directly or indirectly to one of the blocks mentioned above.
- The reverse scenario, whereby a structure from an optimized code block is directly or indirectly passed to a standard data block, which forwards this structure directly or indirectly to one of the program blocks mentioned above.

Otherwise, a hidden copy of the passed data is created in TEMP, which leads to the asynchronous program blocks returning a negative acknowledgment.

### EN parameter

The input parameter EN (enable) determines whether an instruction is called. If EN = 0, the instruction is not called; if EN = 1, the instruction is called.

For synchronously executed instructions, the call corresponds to the execution. If the call takes place, the instruction is executed. If the call does not take place, then it is not executed.

This is different with asynchronous instructions. The execution can be started by the call. If the execution has been started, then the instruction is executed in the background regardless of whether the call is repeated.

At the start of execution, input parameters with simple data types are applied and evaluated. For input parameters with complex data types (arrays and structures), a pointer to the data is stored so that the instruction can be executed even if it is no longer called.

With the end of the call, the values of the output parameters are copied into the connected tags. Without a call, i.e. with EN = 0, this copying process does not take place, so that the connected tags remain unchanged.

### REQ parameter

The input parameter REQ (request) is used solely to start the job or prepare the start.

A distinction must be made between level-controlled and edge-controlled instructions.

The following applies to level-controlled instructions:

- You trigger the job by setting the input parameter REQ to "1" (case 1).
- If a particular job has been started and not yet completed and you call the instruction again to perform the same job (for example, in a cyclic interrupt OB), REQ is then not evaluated by the instruction (case 2).
- If the job is completed, but the input parameter REQ is still set to "1", the job is then immediately started again.

  > **Note**
  >
  > **REQ bit = "1"**
  >
  > Please note that, when the REQ bit is set, the asynchronous instruction will be started again after the previous call is completed. This may not be desired. To make the project clearer and easier to maintain, it is therefore advisable to reset the REQ bit to "0" as early as possible.

The following applies to edge-controlled instructions such as RecipeExport and RecipeImport:

- They are activated by a rising edge at REQ. A preparatory call with REQ = 0 is necessary before you make the first call with REQ = 1.
- After the execution has been triggered, you can set REQ back to 0. Further changes from 0 to 1 and back are ignored as long as the execution continues.

### Parameter RET_VAL and BUSY

The output parameters RET_VAL and BUSY indicate the status of the job.

Pay attention to the note in section: [Evaluating errors with output parameter RET_VAL](Programming%20basics.md#evaluating-errors-with-output-parameter-ret_val)

- For a call with REQ = 0 and available system resources, W#16#7000 is entered in RET_VAL and BUSY is set to "0".

  > **Note**
  >
  > **Call with REQ = 0 when system resources are assigned**
  >
  > If an asynchronous instruction with REQ = 0 is called for an S7-1500 CPU, all available resources are assigned at this time and this call not an intermediate call of a job that is already running, the error code W#16#80C3 (temporary resource error) is entered in RET_VAL.
  >
  > For an S7-300 CPU, the error code W#16#7000 (first call with REQ = 0) is entered in RET_VAL under these boundary conditions.
- In case 1 (first call with REQ = 1), code W#16#7001 is entered in RET_VAL and BUSY is set to "1" if system resources are available and the supply of the input parameters is correct.

  If the required system resources are currently being used or the input parameters contain an error, the corresponding error code is entered in RET_VAL and BUSY receives the value "0".
- In case 2 (intermediate call), the code W#16#7002 is entered in RET_VAL (this corresponds to the message that the call is currently still being processed) and BUSY is set to "1".
- The following applies to the last call for a job:

  - For instruction "[DPNRM_DG](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#dpnrm_dg-read-diagnostics-data-from-a-dp-slave-s7-1200-s7-1500)", the number of data in bytes will entered as integer in RET_VAL in case there are no errors in data transmission. BUSY has the value "0" in this case.

    If there is an error, then the error information will be entered in RET_VAL and you should not evaluate BUSY in this case.
  - For all other instructions, "0" will be entered in RET_VAL if the job was executed without errors and BUSY will receive the value "0". If there is an error, the error code will be entered in RET_VAL and BUSY will receive the value "0".

> **Note**
>
> If the first and last call coincide, the reaction for RET_VAL and BUSY is the same as for the last call.

### Overview

The following table provides you with an overview of the relationships explained above. In particular, it shows the possible values of the output parameters if the execution of the job is not completed after an instruction call has been completed.

> **Note**
>
> Following every call, you must evaluate the relevant output parameters in your program.

Relationship between call, REQ, RET_VAL and BUSY during a "running" job.

| Number of the  call | Type of call | EN | REQ | RET_VAL | BUSY | DONE | ERROR | ENO |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 0 | Preparatory call <sup>1)</sup> | 1 | 0 | W#16#7000 | 0 | 0 | 0 | True |
| 1 | First call | 1 | 1 | W#16#7001 | 1 | 0 | 0 | True |
| Error code | 0 | 0 | 1 | False |  |  |  |  |
| 2 to (n - 1) | Intermediate call | 1 | Irrelevant (recommended 0 <sup>2)</sup>) | W#16#7002 | 1 | 0 | 0 | True |
| n | Last call | 1 <sup>3)</sup> | irrelevant | W#16#0000 (exceptions: [RD_REC](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rd_rec-read-data-record-from-io-s7-1500) and [RD_DPARA](Extended%20instructions%20%28S7-1200%2C%20S7-1500%29.md#rd_dpara-read-module-data-record-asynchronously-s7-1500): The successfully read data length is written to the parameter STATUS.) | 0 | 1 | 0 | True |
| Error code if errors occurred | 0 | 0 | 1 | False |  |  |  |  |
| <sup>1)</sup> This line is only available for edge-controlled instructions.   <sup>2)</sup> To prevent an unintentional restart after the end of execution   <sup>3)</sup> To record the successful execution of an asynchronous instruction, EN = 1 must be present at this time. |  |  |  |  |  |  |  |  |
