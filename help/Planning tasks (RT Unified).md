---
title: "Planning tasks (RT Unified)"
package: SchedulerWCCUenUS
topics: 7
devices: [RT Unified]
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Planning tasks (RT Unified)

This section contains information on the following topics:

- [Basics (RT Unified)](#basics-rt-unified)
- [Creating tasks with the "Time" trigger (RT Unified)](#creating-tasks-with-the-time-trigger-rt-unified)
- [Creating tasks with the "Tags" trigger (RT Unified)](#creating-tasks-with-the-tags-trigger-rt-unified)
- [Creating tasks with the "Alarms" trigger (RT Unified)](#creating-tasks-with-the-alarms-trigger-rt-unified)

## Basics (RT Unified)

This section contains information on the following topics:

- [Field of application of the Scheduler](#field-of-application-of-the-scheduler)
- [Basic of the scheduler (RT Unified)](#basic-of-the-scheduler-rt-unified)

### Field of application of the Scheduler

In the Scheduler, you configure tasks that are executed in the background regardless of the screen. You create tasks by linking scripts to a trigger. The linked functions will be called when the triggering event occurs.

#### Application example

You use Scheduled tasks to execute event-controlled tasks automatically. For example, you use a task to automate the following:

- Regular swap out of log data
- Printout of an alarm report when an alarm buffer overflow occurs
- Printout of a report at shift end
- Monitoring a tag
- Monitoring of a user change

> **Note**
>
> The availability of the listed examples is dependent on the HMI device.

### Basic of the scheduler (RT Unified)

#### Definition

You use Scheduled tasks to configure tasks which are only to be executed cyclically or at

a specific condition. Each task has a trigger and an action.

#### Triggers

You use the triggers to define when and how often the task is to be processed during runtime. The following triggers are supported:

| Triggers | Type | Description |
| --- | --- | --- |
| Time | Cyclic | Executed cyclically at the set time from runtime start, for example, every 2 seconds with "T2s". |
| Daily  Weekly  Monthly  Yearly | Cyclic | Is executed in cycles starting from runtime start, in each case at the configured time, for example "Daily, 12:00:00 h". |
| Once | Acyclic | Is executed exactly once at the configured time. |
| Tags | Acyclic | Executed when the value of one of the projected tags changes. |
| Alarms | Acyclic | Executed when the state of one of the following alarm properties changes:  - Alarm class, for example "Warning" - Alarm state, for example "Incoming" - Priority, for example "4" |

> **Note**
>
> Local session tags cannot be used as triggers.

#### Trigger an action

If the configured trigger condition is fulfilled, the event "Update" is triggered. You configure a local script, which triggers one or more actions.

#### Filling out property values of one or more tasks automatically

When planning new tasks, Scheduled tasks allows the property values of already defined tasks to be used. Bulk creation of property values is possible in the Scheduled tasks editor. This functionality saves the time that would be needed to create individual tasks.

Follow these steps to fill out the property values of one or more tasks automatically:

1. In the Task editor, select the "Name" or "Trigger" cell.
2. Use the mouse to drag the bottom right-hand corner downwards. The values are transferred to the destination cells.

   ![Filling out property values of one or more tasks automatically](images/148921740171_DV_resource.Stream@PNG-en-US.png)
3. To change the attributes, use the text boxes in the editor or the text boxes under "Properties &gt; Properties &gt; General". In the latter, you can also define the time specifications, for example, time, day, month and year.

   ![Filling out property values of one or more tasks automatically](images/148906128651_DV_resource.Stream@PNG-en-US.png)

#### Overwriting property values of one or more tasks automatically

1. In the "Trigger" column, select the cell whose value you want to change. Select the desired value from the list.
2. To overwrite the changed value in tasks below, select the source cell in the "Trigger" column.
3. Use the mouse to drag the bottom right-hand corner downwards.
4. In the dialog box, confirm your choice with OK. The values are overwritten in the destination cells.

   ![Overwriting property values of one or more tasks automatically](images/149336741131_DV_resource.Stream@PNG-en-US.png)

#### Sorting values in the Scheduler editor

By clicking the column header, the table is sorted alphabetically in the selected column.

---

**See also**

[Creating tasks with the "Time" trigger (RT Unified)](#creating-tasks-with-the-time-trigger-rt-unified)
  
[Creating tasks with the "Tags" trigger (RT Unified)](#creating-tasks-with-the-tags-trigger-rt-unified)
  
[Creating tasks with the "Alarms" trigger (RT Unified)](#creating-tasks-with-the-alarms-trigger-rt-unified)

## Creating tasks with the "Time" trigger (RT Unified)

### Requirement

- The "Scheduler" editor is open.

### Procedure

Follow these steps to create a task with the trigger "Time":

1. Create a new task with "Add".
2. Select the required cycle as the "Trigger", for example "T250ms" for 250 ms.

### Result

The task with the "Time" trigger has been created.

---

**See also**

[Basic of the scheduler (RT Unified)](#basic-of-the-scheduler-rt-unified)
  
[Creating tasks with the "Tags" trigger (RT Unified)](#creating-tasks-with-the-tags-trigger-rt-unified)
  
[Creating tasks with the "Alarms" trigger (RT Unified)](#creating-tasks-with-the-alarms-trigger-rt-unified)

## Creating tasks with the "Tags" trigger (RT Unified)

### Requirement

- The "Scheduler" editor is open.
- You have created a tag that is monitored for changes in value.

### Procedure

Follow these steps to create a task with the trigger "Tags":

1. Create a new task with "Add".
2. Select the option "Tags" as the "Trigger."
3. Select "Properties &gt; Properties &gt; General" in the Inspector window to select the tag.

### Result

The task with the "Tags" trigger has been created.

---

**See also**

[Basic of the scheduler (RT Unified)](#basic-of-the-scheduler-rt-unified)
  
[Creating tasks with the "Time" trigger (RT Unified)](#creating-tasks-with-the-time-trigger-rt-unified)
  
[Creating tasks with the "Alarms" trigger (RT Unified)](#creating-tasks-with-the-alarms-trigger-rt-unified)

## Creating tasks with the "Alarms" trigger (RT Unified)

### Requirement

- The "Scheduler" editor is open.

### Procedure

Follow these steps to create a task with the trigger "Alarms":

1. Create a new task with "Add".
2. Select the option "Alarms" as the "Trigger".
3. Configure the trigger under "Properties &gt; Properties &gt; General" in the Inspector window.

   - Select the "Criterion", for example "Alarm class".
   - Select the "Condition", for example "Not equal".
   - Select the "Operand", for example "Alarm".

### Result

The task with the "Alarms" trigger has been created.

---

**See also**

[Basic of the scheduler (RT Unified)](#basic-of-the-scheduler-rt-unified)
  
[Creating tasks with the "Time" trigger (RT Unified)](#creating-tasks-with-the-time-trigger-rt-unified)
  
[Creating tasks with the "Tags" trigger (RT Unified)](#creating-tasks-with-the-tags-trigger-rt-unified)
