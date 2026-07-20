---
title: "Planning tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)"
package: SchedulerWCCPenUS
topics: 31
devices: [Basic Panels, Comfort Panels, Panels, RT Advanced, RT Professional]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Planning tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#basics-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Planning tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#planning-tasks-basic-panels-panels-comfort-panels-rt-advanced-rt-professional-1)
- [Examples for Runtime Professional (RT Professional)](#examples-for-runtime-professional-rt-professional)
- [Examples for Runtime Advanced and Panels (Basic Panels, Panels, Comfort Panels, RT Advanced)](#examples-for-runtime-advanced-and-panels-basic-panels-panels-comfort-panels-rt-advanced)

## Basics (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Field of application of the Scheduler (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-scheduler-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Working with tasks and triggers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-tasks-and-triggers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Work area of the "Scheduler" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#work-area-of-the-scheduler-editor-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
- [Triggers (Basic Panels)](#triggers-basic-panels)
- [Triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#triggers-panels-comfort-panels-rt-advanced-rt-professional)
- [Timers for cyclic triggers (Panels, Comfort Panels, RT Advanced)](#timers-for-cyclic-triggers-panels-comfort-panels-rt-advanced)
- [Tag triggers (RT Professional)](#tag-triggers-rt-professional)
- [Function list (Basic Panels)](#function-list-basic-panels)
- [Function list (Panels, Comfort Panels, RT Advanced, RT Professional)](#function-list-panels-comfort-panels-rt-advanced-rt-professional)
- [Print task (RT Professional)](#print-task-rt-professional)
- [Integrating local VB scripts (RT Professional)](#integrating-local-vb-scripts-rt-professional)
- [Integrating local C scripts (RT Professional)](#integrating-local-c-scripts-rt-professional)

### Field of application of the Scheduler (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Definition

You can use the Scheduler to configure tasks to run independent of the screen in the background. You create tasks by linking system functions or scripts to a trigger. The linked functions will be called when the triggering event occurs.

#### Example of an application

The Scheduler is used to execute event-controlled tasks automatically. For example, you use a task to automate the following:

- Regular swap out of log data
- Printout of an alarm report when an alarm buffer overflow occurs
- Printout of a report at shift end
- Monitoring a tag
- Monitoring of a user change

> **Note**
>
> The availability of the listed examples is determined by the HMI device.

---

**See also**

[Working with tasks and triggers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#working-with-tasks-and-triggers-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Planning tasks with acyclic triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#planning-tasks-with-acyclic-triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Working with tasks and triggers (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

A task consists of a trigger and a task type.

![Introduction](images/88835342987_DV_resource.Stream@PNG-en-US.png)

#### Starting a task

Controlled by a trigger, the Scheduler starts the task linked to the trigger.

---

**See also**

[Field of application of the Scheduler (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#field-of-application-of-the-scheduler-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Work area of the "Scheduler" editor (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

Double-click on "Scheduler" to open it in the project view. The work area shows the scheduled tasks, which consist of the trigger and the task type, for example, the function list.

#### Structure

The work area consists of the table of jobs.

![Structure](images/88835342987_DV_resource.Stream@PNG-en-US.png)

The table of tasks shows specified tasks with their properties, such as triggers. You select a task type and a trigger. You assign a name and a comment to the task. The description provides a written summary of the task including the timing for the task.

#### Inspector window

The "Properties" tab of the Inspector window is split into two parts.

The "Job" area lists the name of the job and the job type. The "Starting time" area shows the trigger. The area is different depending on the trigger selected.

In the "Events" tab use the function list with system functions that will be executed in the task.

> **Note**
>
> You can obtain more detailed information about the elements of the user interface using the tooltips. To do so, move the mouse pointer to the relevant object or press &lt;F1&gt; if the object has already been selected.

---

**See also**

[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Triggers (Basic Panels)

#### Introduction

A trigger is linked to a task and forms the triggering event which will call this task. The task is executed when the trigger occurs.

#### Event trigger

When a task is linked to a system event, the task will be triggered by the event. System events include, for example, Runtime stop, screen change, user change, etc.

Each system event can only be configured once for each HMI device.

#### Deactivating job

If you do not need a certain job temporarily, deactivate the job in the Engineering System. You also use the trigger "Deactivated" to make a previously configured system event available once again.

Example: Task "A" is planned with the system event "Shutdown". This system event is then no longer available for another task "B". Select "Disabled" as the trigger for task "A" to make the "Runtime stop" system event available again.

> **Note**
>
> The available triggers depend on the HMI device.

---

**See also**

[Triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Tag triggers (RT Professional)](#tag-triggers-rt-professional)
  
[Timers for cyclic triggers (Panels, Comfort Panels, RT Advanced)](#timers-for-cyclic-triggers-panels-comfort-panels-rt-advanced)

### Triggers (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

A trigger is linked to a task and forms the triggering event which will call this task. The task is executed when the trigger occurs.

> **Note**
>
> The available triggers depend on the HMI device.

#### Types of triggers

The Scheduler recognizes different types of triggers:

#### Acyclic triggers

They consist of a specification for the date and time of day. Tasks with an acyclic trigger are performed once by the Scheduler on the specified date and at the specified time.

#### Cyclic triggers

Tasks linked to a cyclic trigger occur regularly at a specific point in time.

- Standard cycle: With a standard cycle, the beginning of the first interval coincides with the start of Runtime. The length of the interval is determined by the cycle.
- Trigger with defined starting time: You specify a start time and a time interval. You can use cyclic triggers to perform tasks on a daily or weekly basis, for example. For example, you can select a "Weekly" trigger to specify a week as the interval. You specify the beginning of the interval with the day of the week and the time of day.
- The fastest trigger available for Runtime Professional is 250 ms.

> **Note**
>
> **User-defined cycles**
>
> You have defined your own cycles. You can only use cycles in the Scheduler whose maximum value amounts to one hour.

#### Event trigger

When a task is linked to a system event, the task will be triggered by the event. In contrast to cyclic triggers, system events usually occur acyclically. A Runtime stop is a system event, for example.

Each system event can only be configured once for each HMI device.

#### Deactivating job

If you do not need a certain job temporarily, deactivate the job in the Engineering System. You also use the trigger "Deactivated" to make a previously configured system event available once again.

Example: Task "A" is planned with the "User change" system event. This system event is then no longer available for another task "B". Select "Disabled" as the trigger for task "A" to make the "User change" system event available again.

---

**See also**

[Function list (Panels, Comfort Panels, RT Advanced, RT Professional)](#function-list-panels-comfort-panels-rt-advanced-rt-professional)
  
[Planning tasks with event triggers (Basic Panels, Panels, Comfort Panels, RT Advanced)](#planning-tasks-with-event-triggers-basic-panels-panels-comfort-panels-rt-advanced)
  
[Triggers (Basic Panels)](#triggers-basic-panels)
  
[Timers for cyclic triggers (Panels, Comfort Panels, RT Advanced)](#timers-for-cyclic-triggers-panels-comfort-panels-rt-advanced)
  
[Tag triggers (RT Professional)](#tag-triggers-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Timers for cyclic triggers (Panels, Comfort Panels, RT Advanced)

#### Timers for cyclic and acyclic triggers

You have the option to change the start time of a task dynamically in Runtime. You can select an HMI variable as the timer. The value of the tag determines the start time for the task during Runtime.

> **Note**
>
> An HMI tag must be of the type "DateTime". A PLC tag must be of the type "Date and Time" or "DTL".

As long as the operator does not change the tag after Runtime starts, the start time configured in the task is valid. As soon as the operator enters a change to the tag, the current value of the tag is always the start time. To reset the configured time as the start time, the operator has to enter the configured time again.

---

**See also**

[Triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Triggers (Basic Panels)](#triggers-basic-panels)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)

### Tag triggers (RT Professional)

#### Tag triggers

In addition to acyclic, cyclic and event triggers, WinCC offers tag triggers.

Tag triggers consist of the specification of one or more tags. A task linked to such a trigger is only performed when the value of the tag changes. This reduces the load on the system. The cycle in which the tag values are scanned can be set individually for each tag. Select a value ranging from "250 ms" to once an hour for the scanned cycles. You can also define your own user cycles.

#### Rules for selecting the trigger

Use the tag trigger instead of the cyclic trigger for tag processing. This reduces the load on the system.

- Tag triggers

  The task is performed only when the value of the tag changes.

  ![Rules for selecting the trigger](images/9536111755_DV_resource.Stream@PNG-de-DE.png)= task is executed.

  ![Rules for selecting the trigger](images/76068833291_DV_resource.Stream@PNG-en-US.png)
- Cyclic triggers

  You have selected "10 seconds" as the cyclic trigger. The task will be executed when the trigger occurs.

  ![Rules for selecting the trigger](images/9536111755_DV_resource.Stream@PNG-de-DE.png)= task is executed.

  ![Rules for selecting the trigger](images/76068124811_DV_resource.Stream@PNG-en-US..png)

---

**See also**

[Triggers (Basic Panels)](#triggers-basic-panels)
  
[Triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)

### Function list (Basic Panels)

#### Function list

A trigger starts the function list. The function list is executed line by line. Each line contains a system function. You can configure exactly one function list for each task.

> **Note**
>
> The choice of configurable system functions in a function list depends on the selected trigger and the HMI device.

---

**See also**

[Function list (Panels, Comfort Panels, RT Advanced, RT Professional)](#function-list-panels-comfort-panels-rt-advanced-rt-professional)
  
[Integrating local VB scripts (RT Professional)](#integrating-local-vb-scripts-rt-professional)
  
[Integrating local C scripts (RT Professional)](#integrating-local-c-scripts-rt-professional)

### Function list (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Function list

A trigger starts the function list. The function list is executed line by line. Each line contains a system function or a local script. You can configure exactly one function list for each task.

> **Note**
>
> The choice of configurable system functions in a function list depends on the selected trigger and the HMI device.

#### Processing of system functions and scripts

System functions and scripts in a function list are processed in Runtime sequentially from top to bottom.

Use a script with loops, conditional statements and abort conditions to program non-sequential and conditional procedures.

---

**See also**

[Triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Planning tasks with acyclic triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#planning-tasks-with-acyclic-triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Function list (Basic Panels)](#function-list-basic-panels)
  
[Print task (RT Professional)](#print-task-rt-professional)
  
[Integrating local VB scripts (RT Professional)](#integrating-local-vb-scripts-rt-professional)
  
[Integrating local C scripts (RT Professional)](#integrating-local-c-scripts-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Print task (RT Professional)

#### Introduction

In addition to the "Function list", WinCC Runtime Professional also includes the "Print job" task type.

#### Print job

You print the report by creating a print job. When a cyclic or acyclic trigger occurs, the Scheduler starts the printout of a report. You define the scope of printing and the time range of the report beforehand in the "Print jobs" editor. In addition, you specify whether the report will be printed or written into a file.

![Print job](images/12465496075_DV_resource.Stream@PNG-en-US.png)

If you have selected "Print job" as the task type, an additional field will appear in the "Task" area. Select the predefined print job for the task in the "Print job" field.

> **Note**
>
> Activate "Scheduled print jobs in runtime" in the start sequence of WinCC Runtime to use the "Print job" job type.
>
> Click on "Runtime settings &gt; Services &gt; Scheduled print jobs in runtime" in the editor.

---

**See also**

[Create a print job (RT Professional)](Working%20with%20reports%20%28Panels%2C%20Comfort%20Panels%2C%20RT%20Advanced%2C%20RT%20Professional%29.md#create-a-print-job-rt-professional)
  
[Function list (Panels, Comfort Panels, RT Advanced, RT Professional)](#function-list-panels-comfort-panels-rt-advanced-rt-professional)
  
[Planning tasks with cyclic triggers (RT Professional)](#planning-tasks-with-cyclic-triggers-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)

### Integrating local VB scripts (RT Professional)

#### Introduction

In addition to the "Function list" and "Print job" task types, Professional Runtime also allows you to integrate local VB scripts.

#### Integrating local VB scripts

You can create and edit local scripts. You can also convert the system functions offered in the function list in a local script and edit the code. The local VB script is stored with the task.

A trigger starts the script in Runtime. Once you have converted a function list to a VB script, you can no longer access the function list for this task. You will have to delete the VB script to access the function list once again.

The Scheduler allows you to start VB scripts independent of screens. The VB scripts give you access to tags and screens in Runtime.

There is no common data area between scripts in the Scheduler and screens. Scripts in the Scheduler and screens can be synchronized with the DataSet object or tags. The data type of VBS variables is always VARIANT.

The local VB script is not executed simultaneously. The script last triggered is put into a queue until it is processed.

> **Note**
>
> When you create a script, the "Option explicit" statement is entered automatically in the declaration section and cannot be deleted. The statement is necessary to avoid errors from incorrectly spelled tags without declaration.
>
> The statement requires you to always define tags with the "Dim" statement in your code. Do not use the "Option explicit" statement in your code, as it can lead to Runtime errors.

#### Requirement

Enable "Tasks in Runtime" in the startup sequence of WinCC to use the function list and local scripts.

Click "Runtime settings &gt; Services &gt; Tasks in Runtime" in the editor.

> **Note**
>
> You cannot call C scripts in VB scripts and vice versa.

#### User cycles as triggers

If you use user cycles as triggers for VB scripts, the scripts are always executed in Runtime with a granularity of 250 ms.

---

**See also**

[Function list (Panels, Comfort Panels, RT Advanced, RT Professional)](#function-list-panels-comfort-panels-rt-advanced-rt-professional)
  
[Function list (Basic Panels)](#function-list-basic-panels)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)

### Integrating local C scripts (RT Professional)

#### Introduction

In addition to the "Function list" and "Print job" task types, Runtime Professional also allows you to integrate local C scripts.

#### Integrating local C scripts

You can create and edit local scripts. You can also convert the system functions offered in the function list in a local C script and edit the code. The local C script is stored with the task.

A trigger starts the script in Runtime. Once you convert a function list to a C-script, you can no longer access the function list for this task. You will have to delete the C script to access the function list once again.

A trigger starts the local C script in Runtime.

The local C script is not executed simultaneously. The script last triggered is put into a queue until it is processed.

#### Requirement

Enable "Tasks in Runtime" in the startup sequence of WinCC to use the function list and local scripts.

Click "Runtime settings &gt; Services &gt; Tasks in Runtime" in the editor.

> **Note**
>
> You cannot call C scripts in VB scripts and vice versa.

#### User cycles as triggers

If you use user cycles as triggers for C scripts, the scripts are always executed in Runtime with a granularity of 250 ms.

---

**See also**

[Function list (Basic Panels)](#function-list-basic-panels)
  
[Function list (Panels, Comfort Panels, RT Advanced, RT Professional)](#function-list-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)

## Planning tasks (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

This section contains information on the following topics:

- [Planning tasks with acyclic triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#planning-tasks-with-acyclic-triggers-panels-comfort-panels-rt-advanced-rt-professional)
- [Planning tasks with cyclic triggers (RT Professional)](#planning-tasks-with-cyclic-triggers-rt-professional)
- [Planning tasks with event triggers (Basic Panels, Panels, Comfort Panels, RT Advanced)](#planning-tasks-with-event-triggers-basic-panels-panels-comfort-panels-rt-advanced)
- [Administer task (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#administer-task-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)

### Planning tasks with acyclic triggers (Panels, Comfort Panels, RT Advanced, RT Professional)

#### Introduction

You are planning a one-time Runtime stop for maintenance work. The task starts a function which requires Runtime to stop.

#### Requirements

- The "Scheduler" editor is open.
- The Inspector window is open.

#### Procedure

1. Click "Add..." in the table of the task area.
2. Enter "Maintenance at end of year" as the "Name."
3. Select "Once" as the "Trigger."
4. Select "31.12.2008" in the "Properties &gt; Properties &gt; General &gt; on" field of the Inspector window.
5. Enter the time "18:00" in the "at" field.
6. Click "Properties &gt; Events" in the Inspector window.
7. Select the "StopRuntime" system function in the function list.
8. Select "Runtime" as the "Mode".

   ![Procedure](images/79474014859_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/79474014859_DV_resource.Stream@PNG-en-US.png)

#### Result

The task is executed once. Runtime will be stopped at 18:00 on December 31, 2008.

> **Note**
>
> **"StopRuntime" event on RT Professional**
>
> Please note that the "StopRuntime" event means runtime is in the process of ending and that some functionalities are therefore no longer available.

---

**See also**

[Planning tasks with cyclic triggers (RT Professional)](#planning-tasks-with-cyclic-triggers-rt-professional)
  
[Planning tasks with event triggers (Basic Panels, Panels, Comfort Panels, RT Advanced)](#planning-tasks-with-event-triggers-basic-panels-panels-comfort-panels-rt-advanced)
  
[Administer task (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)](#administer-task-basic-panels-panels-comfort-panels-rt-advanced-rt-professional)
  
[Function list (Panels, Comfort Panels, RT Advanced, RT Professional)](#function-list-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Planning tasks with cyclic triggers (RT Professional)

#### Introduction

You plan a task that starts the daily printout of a report.

#### Requirements

- You have created an HMI device with Runtime Professional.
- The "Daily alarm report" print task has been created.
- The "Scheduler" work area is open.

#### Procedure

1. Click "Add..." in the table of the task area.
2. Select "Print task" under "Type."
3. Enter "Daily alarm report printout" as the "Name."
4. Select "Daily" as the "Trigger."
5. In the Inspector window "Properties &gt;Properties &gt; General &gt; at" enter the time "18:00".
6. Select the "Daily alarm report" print task in the "Task" area.

   ![Procedure](images/73131627403_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/73131627403_DV_resource.Stream@PNG-en-US.png)
7. Open the "Runtime settings &gt; Services" editor.
8. Enable "Start sequence of WinCC Runtime &gt; Planned print jobs in Runtime".

#### Result

The report "Daily alarm report" will be printed every day at 18:00 hours.

---

**See also**

[Planning tasks with acyclic triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#planning-tasks-with-acyclic-triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Print task (RT Professional)](#print-task-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Planning tasks with event triggers (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Introduction

You plan a task that generates a screen change when the user changes.

#### Requirements

- The "Scheduler" work area is open.
- You have created the "Start" screen.

#### Procedure

1. Click "Add..." in the table of the task area.
2. Enter "Screen change at user change" as the "Name."
3. Select "User change" as the "Trigger."
4. In the Inspector window, select "Properties &gt; Events".
5. Select the "Screen/ActivateScreen" system function in the function list.
6. Select the "Start" screen in the screen name field.

   ![Procedure](images/61718716683_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/61718716683_DV_resource.Stream@PNG-en-US.png)

#### Result

The task is executed with the "User change" event. When a new user logs on successfully, the "Start" screen is called up.

---

**See also**

[Planning tasks with acyclic triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#planning-tasks-with-acyclic-triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Administer task (Basic Panels, Panels, Comfort Panels, RT Advanced, RT Professional)

#### Changing the designation

1. In the work area, double-click the field in the "Name" column.
2. Change the name of the task.
3. Confirm your entry with &lt;Return&gt;.

As an alternative, you can change the designation in the "Job &gt; Name" box of the Inspector window.

#### Changing triggers

1. In the work area, mark the field in the "Trigger" column.
2. Open the drop-down list using the ![Changing triggers](images/41396870411_DV_resource.Stream@PNG-de-DE.png) button and select the trigger you require.

You can alternatively change the trigger in the "Starting time" area of the Inspector window.

#### Deleting a task

1. Select one or more lines for the tasks to be deleted.
2. Open the shortcut menu with the right button and select the menu command "Delete".

As an alternative, delete one or more tasks by using the &lt;Del&gt; button.

---

**See also**

[Planning tasks with acyclic triggers (Panels, Comfort Panels, RT Advanced, RT Professional)](#planning-tasks-with-acyclic-triggers-panels-comfort-panels-rt-advanced-rt-professional)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
  
[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)

## Examples for Runtime Professional (RT Professional)

This section contains information on the following topics:

- [Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)
- [Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
- [Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
- [Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)

### Example: Activate the start screen daily  (RT Professional)

#### Introduction

You plan a task that activates the start screen daily with a logon dialog before the shift begins.

#### Requirements

- A "start screen" has been created.
- The "Scheduler" work area is open.

#### Procedure

1. Click "Add..." in the "Task" table.
2. Enter "Activate start screen" as the "Name".
3. Select "Function list" as the "Type".
4. Select "Daily" as the "Trigger."
5. In the Inspector window "Properties &gt;Properties &gt; General &gt; at" enter the time "05:30".
6. In the Inspector window, open "Properties &gt; Events".
7. Select the system function "ActivateScreen" from the "Screens" group in the function list.
8. Enter "Start screen" as the "Screen name".

   ![Procedure](images/41398411019_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/41398411019_DV_resource.Stream@PNG-en-US.png)
9. Open the "Runtime settings &gt; Services" editor.
10. Activate "Scheduled tasks in Runtime".

#### Result

The "Start screen" is activated daily at 5:30 a.m.

---

**See also**

[Example: Printing a report once (RT Professional)](#example-printing-a-report-once-rt-professional)
  
[Example: Reading the current user name (RT Professional)](#example-reading-the-current-user-name-rt-professional)
  
[Example: Increment a tag (RT Professional)](#example-increment-a-tag-rt-professional)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)

### Example: Printing a report once (RT Professional)

#### Task

You plan a task that prints out a report once at the end of the year.

#### Requirement

- The "Annual overview" print task is created.

#### Procedure

1. Click "Add..." in the table of the task area.
2. Enter "Annual summary" as the "Name".
3. Select "Print task" as the "Type".
4. Select "Once" as the "Trigger."
5. Select "31.12.2010" in the "Properties &gt; Properties &gt; General &gt; on" field of the Inspector window.
6. Enter the time "22:00" in the "at" field.
7. Select the "Annual overview" print task in the "Task" area.

   ![Procedure](images/19894363531_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/19894363531_DV_resource.Stream@PNG-en-US.png)
8. Open the "Runtime settings &gt; Services" editor.
9. Enable "Start sequence of WinCC Runtime &gt; Scheduled print jobs in Runtime".

#### Result

The "Annual overview" print job will be started on December 31, 2008 at 10:00 p.m.

---

**See also**

[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)

### Example: Reading the current user name (RT Professional)

#### Introduction

You plan a task that writes the current user into a text field.

#### Requirements

- A "Screen_1" screen has been created.
- A "Textfield_1" text field has been created in the "Screen_1" screen.
- The "Scheduler" work area is open.

#### Procedure

1. Click "Add..." in the table of the task area.
2. Enter "Reading the user name" as the "Name".
3. Select "Tag trigger" as the "Trigger".
4. Click "Properties &gt; Properties &gt; General &gt; Add trigger" in the Inspector window.
5. Select the "@CurrentUser" system variable.
6. Select "1 min" as the "Cycle".
7. In the Inspector window, open "Properties &gt; Events".
8. Click ![Procedure](images/25646108683_DV_resource.Stream@PNG-de-DE.png) in the "Function list" area.
9. Enter the following VB script:

Sub Action ()

Dim user

user = HMIRuntime.Tags("@CurrentUser").Read

HMIRuntime.Screens("Screen_1").ScreenItems("Textfield_1").Text = user

End Sub

1. Open the "Runtime settings &gt; Services" editor.
2. Activate "Scheduled tasks in Runtime".

#### Result

When the tag value changes, the current user is written into the "Textfield_1" text field.

---

**See also**

[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)

### Example: Increment a tag (RT Professional)

#### Introduction

You schedule a task that increments the value of a tag by one every hour.

#### Requirements

- You have created an HMI device with Runtime Professional.
- The "Scheduler" work area is open.
- The "Tag1" tag has been created.

#### Procedure

1. Click "Add..." in the table of the task area.
2. Select "Function list" as the "Type."
3. Enter "Count up tag" as the "Name."
4. Select "1 hour" as the "Trigger".
5. In the Inspector window, under "Properties &gt; Properties &gt; General &gt; Starting time &gt; at minute" enter the value "35:00".
6. In the Inspector window, open "Properties &gt; Events".
7. Click ![Procedure](images/25646108683_DV_resource.Stream@PNG-de-DE.png) in the "Function list" area.
8. Enter the following program code in the entry field:

Sub Action ()

Dim objTag1

Dim lngValue

Set objTag1 = HMIRuntime.Tags("Tag1")

lngValue = objTag1.Read

objTag1.Write lngValue + 1

End Sub

1. Open the "Runtime settings &gt; Services" editor.
2. Select "Scheduled tasks in Runtime".

#### Result

The tag is incremented cyclically.

---

**See also**

[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)

## Examples for Runtime Advanced and Panels (Basic Panels, Panels, Comfort Panels, RT Advanced)

This section contains information on the following topics:

- [Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)
- [Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
- [Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
- [Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
- [Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
- [Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)

#### Task

Configure an I/O field which displays the logged on user. Configure a task which updates the I/O field when the logged on user changes.

#### Requirements

- A "CurrentUser" tag of the "String" type is created.
- A screen has been created and opened.
- An I/O field is created in the screen.

#### Procedure

1. Click on the "I/O field" object.
2. In the Inspector window, select "Properties &gt; Properties &gt; General":

   - Select "String" as the "Display format."
   - Select "CurrentUser" as the "Variable."
   - Select "Output" as the mode.
3. Change to the work area of the Scheduler.
4. Click "Add..." in the table of the task area.
5. Enter "CurrentUser" as the "Name".
6. Select "User change" as the "Trigger."
7. In the Inspector window, select "Properties &gt; Events".
8. Select the system function "ReadUserName" from the "User Management" group in the function list.
9. Select "CurrentUser" as the "Variable."

   ![Procedure](images/41395952907_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/41395952907_DV_resource.Stream@PNG-en-US.png)

#### Result

When a new user logs on successfully, the "ReadUserName" function is called up. The "CurrentUser" tag is updated and displayed in the I/O field of the newly logged on user.

If a user does not log on successfully, the logged on user is logged off. The I/O field continues to display the user previously logged on until a new user logs on successfully.

---

**See also**

[Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)](#example-weekly-printout-of-a-report-panels-comfort-panels-rt-advanced)
  
[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: Activate the start screen daily (RT Professional)](#example-activate-the-start-screen-daily-rt-professional)

### Example: Weekly printout of a report (Panels, Comfort Panels, RT Advanced)

#### Introduction

You plan a task that starts the weekly printout of a report.

#### Requirements

- A "Weekly report" report has been created.
- The "Scheduler" work area is open.

#### Procedure

1. Click "Add..." in the table of the task area.
2. Enter "Weekly report printout for end of shift" as the "Name."
3. Select "Weekly" as the "Trigger."
4. Select "Properties &gt; Properties &gt; General &gt; on day" "Friday" in the Inspector window.
5. Enter the time "18:00" in the "at" field.

   ![Procedure](images/111974684555_DV_resource.Stream@PNG-en-US.png)

   ![Procedure](images/111974684555_DV_resource.Stream@PNG-en-US.png)
6. In the Inspector window, select "Properties &gt; Events".
7. Select the "Print/PrintReport" system function in the function list.
8. Select "Weekly report" report.

#### Result

The weekly print task starts on Friday at 18:00.

---

**See also**

[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)

### Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)

#### Introduction

A cyclic trigger, for example "Starting daily at 18:00," is configured in the Engineering System. The time "18:00" is fixed as a constant. To change the start time in Runtime, select a tag as the "Timer." The value of the tag determines the start time of the task during Runtime.

#### Task

You plan a task that swaps out log data daily and has the "LogTime" tag as the timer. You configure a "LogTime" tag in an input field.

#### Requirements

- The "DataLogSource" source log has been created as a data log.
- The "DataLogDestination" destination log has been created as a data log.
- A "ChangeLogTime" screen has been created.

#### Procedures overview

1. Creating a timer tag: You create a tag with which you change the starting point of the log data swap in Runtime.
2. Configuring a Date/time field: The operator changes the starting point of the task by using the Date/Time field in Runtime.
3. Configure the task with a timer tag: You create a task whose start time can be changed dynamically in Runtime.

#### Result

If nothing is entered in the "LogDataTimeField" input field, then the task starts daily at 18:00 by default. The log data are swapped out. If an operator enters 19:00 in the "LogDataTimeField" input field, then the log data are swapped out at 19:00. Provided the value of the tag is not changed again before the task starts.

---

**See also**

[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)
  
[Example: Update user following change of user (Basic Panels, Panels, Comfort Panels, RT Advanced)](#example-update-user-following-change-of-user-basic-panels-panels-comfort-panels-rt-advanced)

### Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)

#### Task

In the following example you configure the "LogTime" variable.

#### Procedure

1. Open the "HMI tags" editor.
2. Click "Add..." in the table of the task area.
3. Enter "LogTime" as the "Name" of the variable.
4. Select "Internal variable" in the "Connection" column.
5. Select "DateTime" in the "Date type" column.

#### Result

A variable of the "DateTime" type has been created.

---

**See also**

[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)

### Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)

#### Task

In the following example you configure a Date/time field. To change the starting point of the task in Runtime, link the "LogTime" variable to the Date/time field.

#### Requirements

- The "LogTime" variable of the "DateTime" type has been created.
- The "ChangeLogTime" screen is open.

#### Procedure

1. In the toolbox view, drag-and-drop a "Date/time field" from the "Basic objects" category to the screen.
2. In the Inspector window, click "Properties &gt;Properties &gt; General".
3. Disable the "System time."
4. Click "Variable" and select "LogTime."
5. Disable "Display date" and enable "Display time."
6. Select "Input/output" as the "Mode."
7. Click "Properties &gt; Miscellaneous."
8. Enter "LogDataTimeField" as the "Name".

#### Result

The operator enters a time using the created date/time field.

---

**See also**

[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 1. Configuring a tag for Runtime (Panels, Comfort Panels, RT Advanced)](#example-1-configuring-a-tag-for-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)](#example-3-configuring-archiving-with-a-timer-variable-panels-comfort-panels-rt-advanced)

### Example: 3. Configuring archiving with a timer variable (Panels, Comfort Panels, RT Advanced)

#### Task

In the following example you configure a task with a timer tag with which you change the starting point of the task in Runtime.

#### Requirements

- The "LogTime" tag has been created.
- The "DataLogSource" source log has been created as a data log.
- The "DataLogDestination" destination log has been created as a data log.
- The Scheduler work area is open.

#### Procedure

1. Click "Add..." in the table of the task area.
2. Enter "Swap out log daily at a tag time" as the "Name".
3. Select "Daily" as the "Trigger".
4. In the Inspector window "Properties &gt;Properties &gt; General &gt; at" enter the time "18:00".
5. Select the "LogTime" tag as the "Standard timer".
6. In the Inspector window, open "Properties &gt; Events".
7. Select the "System functions/Logs/CopyLog" system function in the function list.
8. Select these settings:

   - Select "Data log" as the "Log type".
   - Select "DataLogDestination" as the "Destination log".
   - Select "DataLogSource" as the "Source log".
   - Select "Overwrite" as the "Mode".
   - Select "Yes" for "Delete source log".

     ![Procedure](images/61722694027_DV_resource.Stream@PNG-en-US.png)

     ![Procedure](images/61722694027_DV_resource.Stream@PNG-en-US.png)

#### Result

If nothing is entered in the "LogDataTimeField" input field, then the task starts daily at 18:00 by default. The log data are swapped out. If an operator enters 19:00 in the "LogDataTimeField" input field, then the log data are swapped out at 19:00. Provided the value of the tag is not changed again before the task starts.

---

**See also**

[Example: Changing the starting point of a task in Runtime (Panels, Comfort Panels, RT Advanced)](#example-changing-the-starting-point-of-a-task-in-runtime-panels-comfort-panels-rt-advanced)
  
[Example: 2. Configuring a Date/time field (Panels, Comfort Panels, RT Advanced)](#example-2-configuring-a-datetime-field-panels-comfort-panels-rt-advanced)
