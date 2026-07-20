---
title: "Using Team Engineering"
package: ProgTeamMain2MenUS
topics: 2
source: Siemens TIA Portal Information System (offline help, en-US)
---


# Using Team Engineering

This section contains information on the following topics:

- [Overview of working with Team Engineering](#overview-of-working-with-team-engineering)
- [Using Multiuser Engineering](Using%20Multiuser%20Engineering.md#using-multiuser-engineering)
- [Using Multiuser Commissioning](Using%20Multiuser%20Commissioning.md#using-multiuser-commissioning)
- [Using Exclusive Engineering](Using%20Exclusive%20Engineering.md#using-exclusive-engineering)
- [Commissioning projects with PLC synchronization](Commissioning%20projects%20with%20PLC%20synchronization.md#commissioning-projects-with-plc-synchronization)
- [Exchanging data with Inter Project Engineering (IPE)](Exchanging%20data%20with%20Inter%20Project%20Engineering%20%28IPE%29.md#exchanging-data-with-inter-project-engineering-ipe)

## Overview of working with Team Engineering

### Introduction

You have a choice of different functionalities for editing your automation tasks in the TIA Portal; all of these functionalities are grouped under the collective term Team Engineering .

Team Engineering supports convenient working in a team.

The advantage of this is that you can work with multiple users simultaneously in projects. This approach significantly reduces the configuring times for your projects. You can commission your plant faster and thus speed up the start of production.

Team Engineering offers different functions for the following development phases:

- For the engineering phase
- For the commissioning phase

In the engineering phase you develop your projects as part of a team. A suitable and useful project structure is created for working together on the project that takes into consideration all the requirements of the project. This includes, for example, a completely configured hardware configuration and an expedient distribution of the projects into program parts or software units that can be edited individually.

In the commissioning phase you take your project into operation together and at the same time. You download your project versions to the CPU with the support of the corresponding Team Engineering functionalities.

### Functionalities of Team Engineering

TIA Portal offers different functions and options for working together on a project in a team and at the same time:

- Multiuser Engineering and Multiuser Commissioning
- Software Units
- PLC synchronization
- Inter Project Engineering (IPE)

Below you will find a list of the different options for working with all functionalities of Team Engineering .

| Symbol | Meaning |
| --- | --- |
| **Multiuser Engineering and Multiuser Commissioning** |  |
| With Multiuser Engineering you can edit multiuser projects together and at the same time in multiple local sessions. You create your projects offline and initially download them to the multiuser server. The multiuser server supports the convenient synchronization of projects and allows you to conduct tests locally.    With Multiuser Commissioning you can conveniently commission your completely configured projects within the team. The multiuser server project is also updated after each download to the CPU during the commissioning phase, and a new revision is created for the server project.  This has the following advantages:  Synchronization of the multiuser project takes place over the server project when working in the local sessions.  The project versions in the CPU and on the multiuser server are always consistent after download to the CPU.     See also:   [Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)    [Working with asynchronous commissioning](Using%20Multiuser%20Commissioning.md#working-with-asynchronous-commissioning)      **Combined application options:**   The functionality of software units and IPE can also be used as part of Multiuser Engineering and Multiuser Commissioning. | ![Functionalities of Team Engineering](images/124907850123_DV_resource.Stream@PNG-en-US.png) |
| **PLC synchronization** |  |
| A "master project" that already contains the completely configured hardware configuration with all required program objects is used as the basis for PLC synchronization.   This project is downloaded to the jointly used CPU and then distributed by means of project copies to up to five participating engineering systems.   The project copies of the master project can be edited independently and offline at the same time.   Depending on the firmware version of the CPU in use, certain online functions can also be executed at the same time from several engineering systems on the shared CPU, for example: Monitoring and operator control of blocks on the CPU and trace functions.   Only one ES can download data to the CPU at any given time.  The changes made by the other editors are displayed in the "Software synchronization" dialog during downloading and are synchronized automatically, if possible.  A manual synchronization is required for concurrent changes. You are supported by the compare editor during manual synchronization of your changes.    See also:   [Basics of PLC synchronization](Commissioning%20projects%20with%20PLC%20synchronization.md#basics-of-plc-synchronization) | ![Functionalities of Team Engineering](images/124907855115_DV_resource.Stream@PNG-en-US.png) |
| **Software units** |  |
| You structure your user program with the help of software units. This means you can, for example, combine all the programming elements required for "Motor_1" into one software unit.   Here, too, a "master project" that already contains the completely configured hardware configuration with all required software units serves as the basis.  This project is downloaded in the jointly used CPU and then distributed by means of project copies to up to five participating engineering systems, each of which will then work exclusively on the software units it has been assigned.  Each software unit comes with its own subordinate programming elements such as tag tables, for example, which guarantee independent working in the individual units.  The software units can be edited offline independent of one another and at the same time, plus they can be downloaded to the CPU without the need for synchronization when observing specific requirements.  The software units are integrated back into the master project at the end of the commissioning phase with each ES copying the software units it has edited back into the master project.  See also:         **Combined application options:**   The functionality of software units can also be used with IPE as well as Multiuser Engineering and Commissioning. | ![Functionalities of Team Engineering](images/124908167307_DV_resource.Stream@PNG-en-US.png) |
| **Inter Project Engineering (IPE)** |  |
| The functionality of Inter Project Engineering, hereinafter referred to as IPE, is used to exchange the controller data in a source project between different projects with the help of a device proxy.   You can then transfer this data to other projects, for visualization in HMI, for example, and use it there for further configuration.  Inter Project Engineering gives you a simple way of providing controller data from a PLC programming across multiple projects for an HMI configuration.    See also:   [Basics of Inter Project Engineering (IPE)](Exchanging%20data%20with%20Inter%20Project%20Engineering%20%28IPE%29.md#basics-of-inter-project-engineering-ipe)      **Combined application options:**   The IPE functionality can also be used with PLC synchronization as well as with software units and with Multiuser Engineering and Commissioning. | ![Functionalities of Team Engineering](images/112071654667_DV_resource.Stream@PNG-en-US.png) |

---

**See also**

[Introduction to Multiuser Engineering](Using%20Multiuser%20Engineering.md#introduction-to-multiuser-engineering)
  
[Working with asynchronous commissioning](Using%20Multiuser%20Commissioning.md#working-with-asynchronous-commissioning)
  
[Basics of PLC synchronization](Commissioning%20projects%20with%20PLC%20synchronization.md#basics-of-plc-synchronization)
  
[Basics of Inter Project Engineering (IPE)](Exchanging%20data%20with%20Inter%20Project%20Engineering%20%28IPE%29.md#basics-of-inter-project-engineering-ipe)
