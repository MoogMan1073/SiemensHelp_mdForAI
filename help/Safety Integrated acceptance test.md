---
title: "Safety Integrated acceptance test"
package: StdrSIATenUS
topics: 24
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Safety Integrated acceptance test

This section contains information on the following topics:

- [SINAMICS Safety Integrated acceptance test](#sinamics-safety-integrated-acceptance-test)

## SINAMICS Safety Integrated acceptance test

This section contains information on the following topics:

- [Legal requirements and regulations](#legal-requirements-and-regulations)
- [Overview](#overview)
- [Important notes](#important-notes)
- [Preparing the acceptance test](#preparing-the-acceptance-test)
- [Performing the acceptance test (example)](#performing-the-acceptance-test-example)
- [Transferring acceptance test results](#transferring-acceptance-test-results)
- [Completing the acceptance test with report](#completing-the-acceptance-test-with-report)
- [Using user-defined texts](#using-user-defined-texts)
- [Performing the Safety Activation Test](#performing-the-safety-activation-test)
- [Multiuser Engineering](#multiuser-engineering)

### Legal requirements and regulations

#### Why is acceptance required?

The EC Machinery Directive and DIN EN ISO 13849‑1 stipulate:

- You must check safety-related functions and machine parts after commissioning.

  → Acceptance test

  For SINAMICS Safety Integrated Functions (SI functions) this specifically means: The acceptance test serves to check the functionality of the Safety Integrated monitoring and stop functions used in the drive. When doing this, the correct implementation of the defined safety functions is investigated, the implemented test mechanisms (e.g. measures for the forced checking procedure (test stop) for S120) are checked. The response of the individual monitoring functions by specifically violating the tolerance limits is provoked. This must be performed for all drive-specific Safety Integrated motion monitoring functions.

  > **Note**
  >
  > **Purpose of the acceptance test**
  >
  > The measured values (e.g. distance, time) and the system behavior identified (e.g. initiation of a specific stop) serve to check the plausibility of the configured safety functions. The objective of an acceptance test is to identify potential configuration errors and/or to document the correct function of the configuration. The measured values are typical values (not worst case values). They represent the behavior of the machine at the time of measurement. These measurements do not serve to derive real values (e.g. maximum values for over-travel distances).
- You must create an "acceptance report" showing the test results.

  → Documentation.

#### Requirements

- The acceptance test is linked to a Startdrive Advanced license. You require the appropriate license to be able to use the acceptance test.
- If the project protection is activated:   
  Only a read access is possible without the required [function rights](User%20administration%20and%20security.md#access-control). A user authentication (login) is required.   
  Observe the detailed information under point "[User administration (UMAC)](User%20administration%20and%20security.md#user-management-and-access-control-umac)".

#### Requirements

The acceptance test requirements (configuration check) for electrical drive safety functions emanate from DIN EN 61800-5-2, Section 7.1 Point f). The acceptance test is called "configuration check" in this standard.

#### Acceptance test

The acceptance test comprises two parts:

- Checking whether the safety functions in the converter are correctly set:

  - Does the speed control handle the configured application cases in the machine?
  - Do the set interfaces, times and monitoring functions match the configuration of the machine?
- Checking whether the safety-relevant functions in the plant or machine function correctly.

  This part of the acceptance test goes beyond the converter acceptance test:

  - Are all safety devices, such as protective door monitoring, light barriers or emergency-off switches connected and ready for operation?
  - Does the higher-level control correctly respond to the safety-relevant feedback signals of the converter?
  - Do the converter settings match the configured safety-relevant function in the machine?

#### Documentation

The documentation consists of the following parts:

- Description of the safety-relevant components and functions of the machine or plant.
- Report of the acceptance test results.
- Report of the settings of the safety functions.
- Countersigned documentation.

#### Authorized persons

Personnel from the **machine manufacturer**, who, on account of their technical qualifications and knowledge of the safety functions, are in a position to perform the acceptance test in the correct manner.

| Symbol | Meaning |
| --- | --- |
|  | **Warning** |
| **Unwanted motion due to incorrect parameter changes**  Incorrect parameter changes for SI functions can result in unwanted motion leading to death or severe injury.  - After making a change to a parameter for the Safety Integrated Functions, always perform an acceptance test for the relevant function. - Document the values calculated in an acceptance report. |  |

### Overview

The Safety Integrated acceptance test is a wizard that supports you when performing the acceptance test and for the configuration check of your machine or plant:

- The Safety Integrated acceptance test guides you step-by-step through the acceptance tests for the individual Safety Integrated Functions.
- The wizard explicitly requires from you inputs and actions that you must perform.
- The wizard creates the trace recordings needed for analyzing the machine behavior during the tests.
- The wizard creates the required acceptance report.

> **Note**
>
> **Test workflow and description**
>
> Because the Safety Integrated acceptance test guides you step-by-step through the required tests, we restrict ourselves here to the exemplary description of a test for a drive. All other tests are performed in a similar fashion, independent of the specific SINAMICS drive.

> **Note**
>
> **Availability of the Safety Integrated acceptance test**
>
> The Safety Integrated acceptance test is available for the following SINAMICS drives:
>
> - G120, G120C, G120D, G115D and G110M
> - G130, G150 and S150 (CU320-2)
> - G220
> - S120 (CU320-2 and CU310-2)
> - S210 (up to SINAMICS firmware V5.2.x)
> - S210 (from SINAMICS firmware V6.1)
> - SIMATIC drive controller

### Important notes

> **Note**
>
> **Conditions for the acceptance test**
>
> As far as possible, the acceptance tests are to be carried out at the maximum possible machine speed and acceleration rates to determine the maximum braking distances and braking times that can be expected.

> **Note**
>
> **Acceptance test for Basic, Extended and Advanced Functions**
>
> The Safety Integrated acceptance test provides the user in the function selection those functions that can be tested, depending on the Control Unit and its settings. For the S120, these would be the following settings for example:
>
> - Basic Functions
> - Extended Functions
> - Advanced Functions
> - Control via PROFIsafe
> - Control via onboard terminals

> **Note**
>
> **Trace recordings**
>
> [Trace recordings](Using%20the%20trace%20and%20logic%20analyzer%20function.md#using-the-trace-and-logic-analyzer-function) are used to analyze the machine response while a test is being conducted. Based on the signal characteristics, it can be checked whether the machine response is in line with the expectations of the test engineer. The recorded signals allow, for example, the delay times and over-travel distances to be evaluated. Trace recordings are automatically parameterized and performed by the tool.

> **Note**
>
> **Non-critical alarms**
>
> When evaluating the alarm buffer you can tolerate the following alarms:
>
> - A01697 SI Motion: Motion monitoring test required
> - A35014 TM54F: Test stop required
>
>   These alarms occur after every system startup and can be evaluated as non-critical.
> - A01699 SI CU: Shutdown path test required
>
>   This alarm occurs after the time in p9659 has expired.
>
> You do not need to include these alarms in the acceptance report.

> **Note**
>
> **No acceptance test with alarm A01796**
>
> If the alarm A01796 is active, the pulses are safely canceled, and an acceptance test is not possible.

> **Note**
>
> **Consistency between offline project and drive**
>
> The acceptance test is performed on completion of commissioning. Subsequently, no further parameter changes may be made in the drive.
>
> Prior to the acceptance test, perform an upload of the drive to establish consistency between the offline project and the drive. All checksums are thus consistent.
>
> The results of the acceptance test are saved in the project.
>
> If no further changes occur in the project or the drive parameterization, all checksums will remain unchanged.
>
> A change in the checksums has to be taken into account in the following cases:
>
> - If a change occurs in the drive parameterization following completion of the acceptance test (offline or online), then the functional checksums will be changed.
> - If drive components are replaced, then the hardware-specific checksums will be changed.
>
> Following changes, the acceptance test must be performed again (completely or partially). Recommendations for this purpose are described in the documentation of the SINAMICS.
>
> The report of the Safety Integrated acceptance test can be exported at any time. A check for project consistency between offline and online values is not made here.
>
> For the final documentation of the acceptance report, make sure that there are no inconsistencies in the system.

> **Note**
>
> **Startdrive supports the consistency check**
>
> In Startdrive, the consistency check is continually and automatically performed online. An icon next to the acceptance test in the secondary navigation displays the result of the consistency check.
>
> The following states are displayed:
>
> ![Figure](images/150767578123_DV_resource.Stream@PNG-de-DE.png): The online and offline comparison values are identical.
>
> ![Figure](images/149081587467_DV_resource.Stream@PNG-de-DE.png): The online and offline comparison values differ. The consistency between the offline project and drive must be established by [Download to device](Configuring%20SINAMICS%20G220%20drives.md#loading-the-configuration-from-the-project-to-the-device) or [Upload from device](Configuring%20SINAMICS%20G220%20drives.md#loading-the-configuration-from-the-device-to-the-project).
>
> ![Figure](images/149503415051_DV_resource.Stream@PNG-de-DE.png): An error occurred during the consistency check.

### Preparing the acceptance test

#### Creating an overview of all drives in the project

![Creating an overview of all drives in the project](images/163654051339_DV_resource.Stream@PNG-de-DE.png)

1. Click "Acceptance test" in the project tree.
2. Select the "Overview" screen form in the secondary navigation.
3. Click on "Determine" or "Refresh" to determine all drives with Safety Integrated Functions in your Startdrive project.

   The overview window lists all drives with Safety Integrated Functions as well as their test status.

   ![Example: Identifying drives with SI functions](images/152053024139_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Identifying drives with SI functions](images/152053024139_DV_resource.Stream@PNG-en-US.PNG)

   Example: Identifying drives with SI functions

   Color coding of the test status:

   - Gray: Safety Integrated Functions have been parameterized, but the acceptance test has not yet been performed
   - Red: Acceptance test failed
   - Blue: Acceptance test in the initial state
   - Green: Acceptance test successful
4. Click "Output" to generate an overview as a spreadsheet in "xlsx" format.

   You can open this table in Microsoft Excel and other spreadsheet programs (e.g. LibreOffice).  
   You can use the overview to track and/or document your work progress, especially for projects with several drives.

#### Preparing the acceptance test

The drives to be tested have been fully parameterized and commissioned. Subsequent changes require performing a new acceptance test.

1. Click "Acceptance test" in the project tree.

   Those Safety Integrated Functions available in the drive are listed and can be selected.   
   When doing this, the function packages that you have selected as well as the control type you have set are taken into account.

   ![Example: Function selection for the acceptance test](images/152052497803_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: Function selection for the acceptance test](images/152052497803_DV_resource.Stream@PNG-en-US.PNG)

   Example: Function selection for the acceptance test
2. In the secondary navigation, select the Safety Integrated Functions to be tested for the required drive (or the drive axis).

   The enabled functions are preselected automatically. This preselection can be changed and functions selected or deselected.
3. In the function selection, activate all additional Safety functions for which you wish to perform an acceptance test. Deactivate all functions for which you do not require an acceptance test.
4. Click "Accept" to specify the function selection for the Safety Integrated acceptance test.  
   Entries for the functions to be tested are displayed in the secondary navigation. Navigate with these settings to the individual tests.
5. Establish an online connection to the drive to be tested.

   The acceptance tests can only be performed in the online mode.

#### Resetting test results

1. Click on "Reset test results" to delete all tests performed for this drive up until now.

   This restores the initial state from which you can again perform acceptance tests.

---

**See also**

[Completing the acceptance test with report](#completing-the-acceptance-test-with-report)
  
[Performing the acceptance test (example)](#performing-the-acceptance-test-example)

### Performing the acceptance test (example)

#### Overview

After accepting the function selection in the "[Preparing the acceptance test](#preparing-the-acceptance-test)" step, the functions to be tested are displayed in the secondary navigation.

You can now perform the tests from top to bottom or in any required sequence.

The status of the individual tests is represented as follows:

- Blue: The test is initial and has not yet been tested.
- Green: The test was performed successfully.
- Red: The test was aborted with error. The test can be repeated by reselecting the function.

#### Requirements

- The drive has been completely created and specified in the device configuration.
- The Safety Integrated Functions of the selected drive have been completely configured.
- There is an active online connection between the drive and the operating unit. The project data in the project and drive are consistent.

  The detailed acceptance test functions can only be performed online.
- With active user administration (UMAC):  
  There is an active user account in the project, which is assigned role "Engineering-Administrator" or "Engineering-Standard" (see Engineering rights).

  - Or -

  The user account of the active user is assigned rights "Edit Safety Integrated application", "Open and edit project" and "Control drive in manual mode" via a role.

#### Structure of the acceptance test wizards

The listed wizards have the same structure for every acceptance test.

The upper area contains the workflow that represents the individual test steps and their status.  
The states have the following meaning:

- Blue: Active test step.
- Green: Test step completed.

The instructions for the test steps are displayed in the area below the workflow. The test steps must be performed by the user. After performing the instructions, click "Next" to advance to the next step. At the end, the test is completed by clicking "Finish". The status of this test is then updated in the secondary navigation.

The operator controls for the test steps are located in the lower area. This includes, for example, the control panel for traversing the axis to be tested.

#### Starting and performing the acceptance test

1. Click one of the functions to be tested (SS1 in this case).  
   The wizard is started in the working area.
2. Enter a test designation. This designation also appears later in the acceptance report.
3. You can change the trace settings for this test or use the preassignment. The preassignment is adequate for most applications.

   A change permits adaptation to the mechanical conditions of the machine, e.g. when the axis mechanical system exhibits a very high moment of inertia so that longer ramp-up times for accelerating and braking are required.
4. Observe the safety information and notes on the start screen of the acceptance test.
5. Once you have performed all preparations, click "Start test".  
   The wizard for the selected test opens.
6. In the first step, the drive must be moved so that an emergency stop can be initiated.  
   Select in the "Move drive via" drop-down list whether the drive should be moved via the control panel or via the user program of a higher-level control.

   - Control panel:  
     If the drive is moved via the control panel, it is displayed in this screen.  
     Activate the master control, enter a setpoint and start the motor in the desired direction of rotation.  
     Click "Next" to advance to the next step.
   - User program:  
     Start the traversing process if the drive is being moved using the user program.

   Initiate emergency stop (SS1) on the selected drive.  
   The motor is braked at the OFF3 braking ramp. The transition to STO is made based on the parameter assignment (e.g. after expiration of the delay time or when the shut-down speed is undershot). If a brake configured via SBC is present, it is closed after transition to STO.  
   When using the control panel, return the master control when the drive is at a standstill. Click on "Next" when "SS1 active" is displayed.
7. The previous workflow is recorded and represented as trace.  
   Check the chronological and content workflow of the test based on the signal recording. In this test, STO may be initiated only when the motor has almost become stationary.  
   Click "Next" provided the test workflow meets your expectations.
8. Optional: Save the trace recording of the acceptance test in your Startdrive project to analyze it later.

   For this purpose, call the shortcut menu in the diagram area and click "Add to measurements".

   The trace recording is saved in the project navigation in the drive menu under "Traces &gt; Measurements".
9. Alternatively: Cancel the test by clicking "Cancel" if the workflow does not meet your expectations.  
   In this case, check the correctness of all input conditions and repeat the test, if necessary.  
   Sample scenario: STO is initiated, even though the motor speed is still high. In this case, a possible cause could be incorrect parameterization, e.g. an insufficiently short delay time from SS1 to STO or an excessively high shut-down speed.
10. Deselect SS1 and click "Next".

    The test was performed successfully.
11. Click "Finish" to exit the wizard.

> **Note**
>
> **Canceling the acceptance test**
>
> If a test is ended by clicking "Cancel", the step in which the test was canceled is marked as "Failed" in the protocol.  
> If another window is selected during the test, the test is canceled and marked accordingly in the protocol.
>
> Remedy: If you need to select another window during the test, the application can be handled as a separate window with "Float". With "Embed", the separate window can be integrated again at a later time.

#### Result

The test status in the secondary navigation is updated.

Execute the wizards of all further functions similarly through the tests.

### Transferring acceptance test results

#### Overview

To simplify further acceptance tests, you can transfer the results of successful tests to drives with the same functionality. The Safety Integrated acceptance test wizard lists the suitable drives.

#### Compatible devices for transferring results

The results of the acceptance test can be transferred from a tested drive to a drive instance of the same type under the following conditions:

| Drive type | Function | Drive instance |
| --- | --- | --- |
| G110M  G115D  G120C  CU240E-2  CU240E-2 F  CU240D-2  CU240D-2 F  CU250D-2 F | STO | G110M  G115D  G120C  CU240E-2  CU240E-2 F  CU240D-2  CU240D-2 F  CU250D-2 F |
| G115D | Extended Functions | G115D |
| CU250S-2 | Basic Functions | CU250S-2 |
| CU250S-2 | Extended Functions | CU250S-2 |
| CU240E-2 F  CU240D-2 F  CU250D-2 F | Extended Functions | CU240E-2 F  CU240D-2 F  CU250D-2 F |
| S120 CU320-2 | Basic Functions | S120 CU320-2 |
| S120 CU320-2 | Extended/Advanced Functions | S120 CU320-2 |
| S120 CU310-2 | Basic Functions | S120 CU310-2 |
| S120 CU310-2 | Extended/Advanced Functions | S120 CU310-2 |
| S150 CU320-2 | Basic Functions | S150 CU320-2 |
| S150 CU320-2 | Extended/Advanced Functions | S150 CU320-2 |
| G150 CU320-2 | Basic Functions | G150 CU320-2 |
| G150 CU320-2 | Extended/Advanced Functions | G150 CU320-2 |
| G130 CU320-2 | Basic Functions | G130 CU320-2 |
| G130 CU320-2 | Extended/Advanced Functions | G130 CU320-2 |
| G220 | Extended Functions | G220 |
| S210 (up to SINAMICS firmware V5.2.x) | Basic Functions | S210 (up to SINAMICS firmware V5.2.x) |
| S210 (up to SINAMICS firmware V5.2.x) | Extended Functions | S210 (up to SINAMICS firmware V5.2.x) |
| S210 (from SINAMICS firmware V6.1) | Basic Functions | S210 (from SINAMICS firmware V6.1) |
| S210 (from SINAMICS firmware V6.1) | Extended Functions | S210 (from SINAMICS firmware V6.1) |
| SIMATIC DC | Basic Functions | SIMATIC DC |
| SIMATIC DC | Extended/Advanced Functions | SIMATIC DC |

#### Procedure

1. Open function view "Result transfer" for a drive for which you have successfully completed the acceptance test.
2. Click on the "Determine" button to determine suitable drives.  
   After initial determination, the button changes to "Refresh".
3. Select the drives to which you want to transfer the results.  
   The selected drives become instances of the tested drive.
4. Click the "Apply" button.

#### Result

The transfer status is displayed in the function view.

### Completing the acceptance test with report

#### Overview

The acceptance report can be created at any time, for example, even when individual tests have not yet been performed or completed with faults. This allows the intermediate states also to be documented.

The actual final acceptance report, however, makes sense only when all tests have been performed successfully.

#### Requirement

- All tests have been successfully completed. The individual tests are all identified positively with a green tick.

#### Procedure

The overview under "Create report" lists all drives of the current project with their current test status.

1. In the "Completion" screen form, select the drives for which you wish to create a report.

   You can make any selection of drives, regardless of their test status.

   The drive instances to which the results were transferred are also displayed in the list as drop-down sub-entries. These drive instances are always included in the acceptance report with the selection of the respective main drive.
2. Click on "Create".

   The "Save As..." dialog box opens.

   If you have selected one drive, as default its drive name is preset as a suggestion for the file name for the acceptance test.  
   If you have selected multiple drives, a dialog for selecting the directory for storing the report opens. For each drive selected, a report is saved with the name of the drive.
3. Assign a name for the project and click on "Save".

#### Optional: Creating a function table

You can use the function table to create a user-defined overview that is documented in the acceptance report in addition to the results of acceptance test.  
The overview is structured as follows:

| Column | Explanation |
| --- | --- |
| Operating mode | Select one of the specified operating modes from the drop-down list to map the desired scenario. |
| Description | Enter an explanatory comment for the selected operating mode. |
| Protective device | Select the protective mechanism to be used in the applicable scenario from the drop-down list. |
| Version | Enter an explanatory comment on the protective device being used. |
| Axis | Select the respective drive axis from the drop-down list. |
| Monitoring | Select the Safety Integrated Function being used from the drop-down list. |

#### Result

The acceptance report is created as a table in "xlsx" format and can thus be opened in Microsoft Excel and other spreadsheet programs (e.g. LibreOffice).

The report comprises several individual tables. These include:

- Cover page: Introduction with the machine description
- Drive_x - overview: Documentation of the parameters and traces for this drive
- Drive_x - function test: Documentation of all test data for this drive

  Test status color coding:

  - Red: Failed
  - Yellow: Not tested
  - Green: Test successful
- Completion: Summary and signatures

> **Note**
>
> **Correct display of the acceptance report**
>
> How the acceptance report is displayed is dependent on the Windows settings and spreadsheet program used to call up the file.
>
> - Microsoft Excel  
>   The acceptance report is displayed correctly in Microsoft Excel when the following is configured in the Windows display settings:  
>   Control Panel &gt; Appearance and Personalization &gt; Display &gt; Make text and other items larger or smaller &gt; Option "Smaller – 100%"
> - LibreOffice  
>   The acceptance report is displayed independently of the Windows settings and is thus always correct.

### Using user-defined texts

This section contains information on the following topics:

- [Introduction](#introduction)
- [create user-defined instruction texts](#create-user-defined-instruction-texts)
- [Using user-defined instruction texts](#using-user-defined-instruction-texts)
- [Exporting/importing instruction texts](#exportingimporting-instruction-texts)

#### Introduction

##### Overview

You can use the user-defined texts to describe the instructions of the individual test steps with your own terminology. The operating instructions can thus be geared towards the specfic operation of your machine.

The instuction texts for the individual steps of all test cases are displayed in the screen form. They are marked with the description "System".

![Example: Instruction texts for test steps](images/152053089675_DV_resource.Stream@PNG-en-US.PNG)

Example: Instruction texts for test steps

Either the test cases of the current drive or the sum of all test cases for the drives included in the project can be displayed by means of a filter setting.

You can make the following settings:

- Insert and describe new instruction texts (user defined)
- Change your own instruction texts at a later time
- copy and paste instruction texts
- export and import instruction texts
- assign instruction texts for use with individual drives in the project or apply them as standard for all drives

#### create user-defined instruction texts

##### Overview

Additional rows can be inserted for each test step via the shortcut menu. Each row corresponds to a new, user-defined instruction for this test step. After selecting a row, you can enter a title (comprising a maximum of 32 characters) and a text (comprising a maximum of 6 rows with 140 characters each) in the lower detailed view of this instruction.

> **Note**
>
> The instruction texts with the description "System" are intended for global application and therefore cannot be changed.

##### Creating a new instruction

1. In the list of user-defined texts, select a test case for which you wish to create an instruction.
2. Open the "Add row" shortcut menu.

   The new row called "New user-defined text" is added to the test case.

   ![Example: User-defined instruction](images/152070600715_DV_resource.Stream@PNG-en-US.PNG)

   ![Example: User-defined instruction](images/152070600715_DV_resource.Stream@PNG-en-US.PNG)

   Example: User-defined instruction
3. For the new instruction, enter the title and the text in the fields with the same name.

   The new instruction text is created.

##### Duplicating an existing instruction

1. In the list of user-defined texts, select an instruction in a test case.
2. Open the "Copy" shortcut menu.
3. Then call the "Insert" shortcut menu.

   The copied instruction is inserted in the test case as new instruction at the last position. You can subsequently change the duplicate.
4. For the duplicate instruction, correct the title and the text in the fields with the same names.

##### Deleting a user-defined instruction

1. In the list of user-defined texts, select a user-defined instruction in a test case.

   Global instructions with the "System" identifier cannot be deleted.
2. Open the "Delete" shortcut menu.

   The instruction text is deleted.

#### Using user-defined instruction texts

##### Overview

User-defined instructions must be manually assigned for use on one or several drives.

Option "Use as default" defines the instruction as a global instruction in the project. This option subsequently applies to all drives in the project, regardless of whether or not the instruction was assigned to a drive; it also applies to all drives subsequently added in this project.

##### Procedure

1. Select the required user-defined instruction in the list of user-defined texts.
2. In the "Use of the following drives/axes" area, activate the required drives or axes.

   - Or -

   Activate the "Use as default" option if the instruction is to be globally applied.

**Note**

Only one instruction can be assigned to a specific drive within a single test step. If several instructions are assigned to the same drive, then the last assignment performed will apply.

The same applies for option "Use as default".

#### Exporting/importing instruction texts

##### Overview

To facilitate simple handling, all instruction texts can be exported from the "User-defined texts" area into an Excel spreadsheet format. When exporting, a distinction is not made between user-defined instruction texts and globally used instruction texts.

In the Excel table, you have an overview across all of the instruction texts, and you can freely edit these. User-defined instruction texts can also be reimported from an Excel file.

> **Note**
>
> **Excel files**
>
> When creating a new Excel file, use an existing, previously exported Excel file as a template to ensure correct formatting.
>
> Observe the "Description" tab in the exported Excel file.

> **Note**
>
> **Compatibility of user-defined instruction texts**
>
> The created user-defined instruction texts are usable within a project. Import the instruction texts into other projects, where they can also be used.

##### Exporting instruction texts

1. In the area of user-defined texts, using the filter, select whether instruction texts should be displayed for all drives in the project, or only for the active drive.

   All instruction texts that are displayed, are taken into account for export.
2. Click on the ![Exporting instruction texts](images/151797676555_DV_resource.Stream@PNG-de-DE.png) icon to export the instruction texts.

   The "Save As..." dialog box opens.
3. Assign a file name for the file to be exported.

   The "xlsx" file format is pre-selected.
4. Assign a storage location in your file location and click on "Save".

**Result:**

All displayed instruction texts are saved in an xlsx file.

##### Importing instruction texts

1. Click on the ![Importing instruction texts](images/151797666955_DV_resource.Stream@PNG-de-DE.png) icon to import the instruction texts from a file.

   The "Open" dialog opens.
2. Select the import file of the instruction texts in the file location on your PC/PG and click "Open".

**Result:**

The formatting is checked when importing. If the import is successful, the existing free texts are integrated into the project. If any user-defined instruction texts already exist in the project, they will be overwritten during the import.

- If the file is incorrect, no texts will be imported and the previous texts will remain unchanged.
- If the format of the file is correct, however the file contains invalid data (e.g. a manually changed step ID), no texts will be imported and the previous texts will remain unchanged.

Texts used by safety functions are not imported if these safety functions are not assigned to any drive.

### Performing the Safety Activation Test

This section contains information on the following topics:

- [Introduction](#introduction-1)
- [Activating the Safety Activation Test](#activating-the-safety-activation-test)
- [Creating test cases](#creating-test-cases)
- [Performing test cases](#performing-test-cases)
- [Documenting test results](#documenting-test-results)

#### Introduction

##### Overview

You can use the Safety Activation Test to test the control signals in the automation topology. The Safety Activation Test also checks whether the defined signal path is properly run through – from the sensor through the evaluation up to the drive or actuator – to ensure that no wiring errors or other faults exist.

You can use the acceptance test to test the Safety Integrated Functions in the SINAMICS drive for proper parameterization.

![Safety Activation Test](images/143937339915_DV_resource.Stream@PNG-de-DE.png)

Safety Activation Test

For this purpose, test cases are defined which determine the input conditions (system states) and the expected system responses. Wizards are provided to perform the tests and the results are entered in the acceptance report of the Safety Integrated acceptance test.

#### Activating the Safety Activation Test

##### Overview

For multi-axis SINAMICS S120 drive units, the selection of the Safety Activation Test is offered in the function selection of each axis.

Up to 99 test cases can be defined per drive.

You can add new tests in the secondary navigation. These tests are assigned names in ascending order (SF1, SF2, ...). Existing tests can be duplicated with the shortcut menu or deleted.

Existing test cases can be selected project-wide either as a basis for describing test cases or for re-use.

Selection of an F-PLC is required in order to use the Safety Activation Test.

PLC tags and the Safety Integrated Functions of the drive that are read in during the runtime test execution are used to define the tests.

##### Requirement

- The drive is assigned to a control (PLC) and connected with this.
- There is an active online connection between the drive and the PC/PG.

##### Procedure

1. In the secondary navigation of the acceptance test, select a drive (or a drive axis).
2. In the function view of the drive (or the drive axis), activate option "Safety Activation Test".

#### Creating test cases

##### Procedure

The following entries must be made for each test case:

| 1. Assign a "name" with a maximum length of 130 characters to the test case.     This name will be imported to the report. 2. With the "description" of the test, you define the operating instruction for test execution.     The description must not exceed a maximum of 130 characters and is automatically imported to the test wizard. 3. "Operating mode" refers to the operating modes of your machine. Assign a name (with a maximum of 32 characters) to the operating mode and select the corresponding variable and its state.     During the subsequent performance of the test, it is checked whether the machine is in this operating mode. 4. The "input conditions" are defined in two stages. The PLC tags are used for the definition. Select the required PLC tags and define their state for the beginning of the test ("Initial") and for its completion ("Executed"). 5. With "Reactions", you describe your expectations regarding the response of the actuators. These are the axes of the drive unit for which the responses (the Safety Integrated Functions) and their state are selected. In addition, actuators of the machine (e.g. hydraulic valves) can be integrated with their expected states in the analysis. 6. Optionally: Under "Trace configuration", activate option "Record trace" to activate a PLC trace that logs the results of the test and displays them in a diagram. In Table "Input conditions" and in the second table "Reactions", select the tags that you wish to record using the trace. Under "Trace configuration", then configure the following settings:       | Setting/display |  | Description |    | --- | --- | --- |    | "Recording time" |  |  |    |  | Recording level entry field | Selection of the recording time. |    | Address of the OB text field | Detailed information on the selected recording time. |  |    | "Pretrigger" |  | "Pretrigger" defines the number of samples that are already recorded before the actual trigger condition is fulfilled. If the trigger event occurs immediately or shortly after the recording has been activated, this may result in a shorter recording duration. Pretrigger examples of "Recording duration (a)" = 20 samples and "Pretrigger (b)" = 5 samples: Case 1: Trigger event occurs 50 samples after activation of the recording, an actual recording duration (a) = 20 samples Case 2: Trigger event occurs 2 samples after activation of the recording, an actual recording duration (a) = 17 samples |    |  | Duration input field | Input of the duration in relation to the selection in the drop-down list. |    | Unit drop-down list | Selection of the unit The following settings are possible: - "Samples" - "s" for seconds   The setting depends on the recording level selected in "Trace sample event". |  |    | Resulting pretrigger duration text field | Display of the calculated "Pretrigger" duration. The duration is displayed when recording in constant bus cycle time OBs. |  |    | "Max. recording duration" |  |  |    |  | Max. recording duration text field | Displays the calculated maximum recording duration. The "Max. recording duration" depends on how many signals are recorded and the data type of these signals. |    | "Recording duration" |  |  |    |  | Recording duration entry field | Input of the recording duration in relation to the selected unit. If the "Recording duration = Max. recording duration" check box is activated, then the entries are overwritten by the value displayed in "Max. recording duration". |    | Unit drop-down list | Selection of the unit for the recording duration. The following settings are possible: - "Samples"   The maximum number of samples recorded is the number for which parameters are assigned under recording duration. - "s" for seconds   The setting depends on the recording level selected in "Trace sample event". |  |    | Calculated recording duration text field | Display of the calculated recording duration (only for constant bus cycle time OBs) |  |    | "Trigger tag" |  | The "Trigger tag" specifies a signal that triggers the recording. |    |  | Trigger tag entry field | Enters a signal  **Examples:**  - "DataBlock_1".Temperature - M0.0 - DB1.DBW3 |    | ![Procedure](images/160812991627_DV_resource.Stream@PNG-de-DE.png) | Opens the signal selection table Clicking the symbol opens a table listing possible signals for selection as trigger tag. The selected signal is displayed in the input field. |  |    | Trigger tag address text field | Displays the trigger tag address The field remains empty for purely symbolic signals. |  | |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

##### Example

You can describe extensive test scenarios with the previously described specifications. The following is a textual description for a test case:

The machine is in the automatic mode (Variable_0 = 1). The emergency stop buttons on the control panel (Variable_1 = 0) and on the hand-held device (Variable_2) must be deactivated before beginning the test case. In addition, the protective door (Variable_3 = 0) must be closed.

When performing the test, the emergency stop button on the control panel must be triggered during machine travel (Variable_1 = 1). All other input variables must remain in their original state.

The expectation for this test case is activation of function SS1 (= True) for axis 1. No emergency stop may be executed for axis 2 (STO = False). In addition, the hydraulics must be switched off (Variable_4 = False).

#### Performing test cases

##### Procedure

Test execution is performed in three steps, during which the relevant signal states are displayed in each case:

1. Initializing input conditions  
   Here you prepare the test by setting the signals to the initial state defined in the test case via machine operation.

   When these signal states have been reached, you can switch to the next step.
2. Perform the Safety Activation Test with "Start"  
   Here it is checked whether the defined operating mode is active.

   The description of the test which you defined is displayed here as an execution instruction.

   The signals must take on the "Executed" states defined in the test case on implementation.

   When these signal states have been reached, you can switch to the next step.
3. Checking the response and concluding the test  
   Here the actuators must take on the states defined for the response in the test case.

   When these signal states have been reached, you can switch to the next step and successfully conclude the test case.
4. Optionally, if you activate option "Trace recording" under "Trace configuration":  
   The test sequence is recorded as trace by the PLC and is displayed as diagram in step "Check reaction and complete the test".  
   Check the timing and content of the test based on the signal recording and the diagram of the trace.  
   You can save the measurement results of the trace in your project. The trace recording is saved in your Startdrive project in the project navigation in the PLC drive object menu in the trace tab under "Measurements".

#### Documenting test results

##### Overview

The test cases of the Safety Activation Test are listed in the secondary navigation and, in the same way as the test cases of the Safety Integrated acceptance test, include status information via color coding.

- Blue: Test in the initial state
- Green: Test completed successfully
- Red: Test failed or canceled by the user

The Safety Activation Test is documented as a separate tab in the acceptance report of the Safety Integrated acceptance test. It describes all of the test cases defined at the time the test report was created along with their respective test statuses.

### Multiuser Engineering

This section contains information on the following topics:

- [Introduction](#introduction-2)
- [Single-axis drives:](#single-axis-drives)
- [Multi-axis drives](#multi-axis-drives)

#### Introduction

##### Overview

The acceptance test can be performed in Multiuser Engineering. The following functions are available for this:

- The acceptance test for an axis is performed in a local session and checked into the test results of the server session.   
  In the server session, any existing test results for this axis are overwritten with the results from the local session.
- The Safety Activation Test for a drive is performed in a local session and checked into the test results of the server session.  
  In the server session, any test results for this drive are overwritten with the results from the local session.

##### Requirements

- The requirements of the TIA Portal for working with Multiuser Engineering are met.

##### Multiuser Engineering

The test results of the acceptance test in the secondary navigation are offered as markable objects.

All Safety Integrated Functions of the acceptance test and the test cases of the Safety Activation Test can be checked into the server project.

The following icons are used for identification in Multiuser Engineering:

| Icon | Description |
| --- | --- |
| ![Multiuser Engineering](images/154896062859_DV_resource.Stream@PNG-de-DE.png) | **Markable object**  This object can be marked for check-in by clicking on it. |
| ![Multiuser Engineering](images/154891553419_DV_resource.Stream@PNG-de-DE.png) | **Markable object**   The object has been marked for check-in in the local session. |
| ![Multiuser Engineering](images/154896864779_DV_resource.Stream@PNG-de-DE.png) | **Marked object**   The object was marked for check-in in another session or in the server project view. |
| ![Multiuser Engineering](images/154896054539_DV_resource.Stream@PNG-de-DE.png) | **Marked object with conflict**  The object has been marked for check-in in multiple local sessions or in a local session and in the server project view, causing a conflict. An object should be marked for check-in only once in the entire multiuser workspace. An object marked in red can still be checked in. However, checking in can lead to unwanted overwriting in the server project, since only the version last checked in is adopted in the server project. |
| ![Multiuser Engineering](images/154897231499_DV_resource.Stream@PNG-de-DE.png) | **Object is outdated**   If one of the above icons is also marked with this overlay, the object no longer corresponds to the latest version of the server project and should be updated.   If the object is checked in without being updated, the editing of the other user is overwritten and thus canceled.  Updating ensures that all editors of a multiuser project have a consistent version. |

#### Single-axis drives:

For single-axis drives, the acceptance tests that have been successfully performed at this time are taken into account together for check-in. Individual acceptance tests cannot be marked independently of each other.

If Safety Activation Tests are performed, they are taken into account together with the acceptance tests for the check-in.

After the following changes, the drive is marked for check-in:

- Function selection of the acceptance test
- Configuration of the Safety Activation Test
- Status of one of these tests

##### Example 1

The acceptance test for SS1 under Drive unit_1 was performed successfully in the local session.

The Safety Activation Test SF1 was configured but not performed in the local session.

![Example 1](images/154886418059_DV_resource.Stream@PNG-de-DE.png)

![Example 1](images/154886426379_DV_resource.Stream@PNG-de-DE.png)

##### Example 2

The acceptance test for SS1 under Drive unit_1 was performed successfully in the local session.

The Safety Activation Test SF1 was successfully performed in the local session.

![Example 2](images/154890415499_DV_resource.Stream@PNG-de-DE.png)

![Example 2](images/154890487819_DV_resource.Stream@PNG-de-DE.png)

#### Multi-axis drives

For multi-axis drives, the acceptance tests that have been successfully performed for each axis at this time are taken into account together for check-in. Individual acceptance tests cannot be marked independently of each other.

The Safety Activation Tests are taken into account separately for the check-in.

After the following changes, the drive is marked for check-in:

- Function selection of the acceptance test
- Configuration of the Safety Activation Test
- Status of one of these tests

##### Example 1

The acceptance test for SS1 for the SERVO_03 axis was performed successfully in the local session.

No function was selected for the SERVO_04 axis for the acceptance test.

The Safety Activation Test SF1 was configured but not performed in the local session.

![Example 1](images/154890496139_DV_resource.Stream@PNG-de-DE.png)

![Example 1](images/154891362059_DV_resource.Stream@PNG-de-DE.png)

##### Example 2

The acceptance test for SS1 for the SERVO_03 axis was performed successfully in the local session.

No function was selected for the SERVO_04 axis for the acceptance test.

The Safety Activation Test SF1 was configured but not performed in the local session.

If only a portion of these results is to be checked in, this can be controlled by marking/clearing the icons.

![Example 2](images/154891472779_DV_resource.Stream@PNG-de-DE.png)

![Example 2](images/154891481099_DV_resource.Stream@PNG-de-DE.png)
